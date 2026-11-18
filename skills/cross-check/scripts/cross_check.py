#!/usr/bin/env python3
"""Send a cross-check brief to the other coding agent and save its reply.

  python cross_check.py send --to codex|claude --run-dir DIR [--prompt-file F]
                             [--cwd DIR] [--add-dir DIR] [--model M] [--effort E]
  python cross_check.py defaults [--to codex|claude] [--model M] [--effort E]

Round 1 sends DIR/brief.md under the reviewer rules. Later rounds continue the
same peer session and need --prompt-file. Each round writes round-NN.prompt.md,
round-NN.reply.md, round-NN.meta.json, and round-NN.log into DIR.

One send at a time per run directory. Exit codes: 0 reply saved and the
served model matches; 2 reply saved but the served model is unknown or differs,
or Codex reports a different or no effort; 1 no usable reply.
"""
import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

BUILTIN = {
    "codex": {"model": "gpt-6.2-astra", "effort": "max"},
    "claude": {"model": "claude-fable-5-2", "effort": "xhigh"},
}
CLAUDE_EFFORTS = ["low", "medium", "high", "xhigh", "max"]
USER_FILE = Path.home() / ".yu-skills" / "cross-check.json"
PEER_ENV = "YU_CROSS_CHECK_PEER"

PEER_HEADER = """You are the independent reviewer in a cross-check. Another coding agent did
the work described below and wants it attacked before anyone acts on it.

- Work read-only: do not edit files, commit, or install anything. Do not pass
  this task to another agent or model.
- Skip `.env*` files and never print secrets.
- Read the listed materials yourself. The author's claims are claims to test,
  not facts, and their list is not complete: first ask what else could change
  the decision, then try to make each claim fail. Run cheap checks (tests,
  searches, recomputed numbers) where your tools allow.
- Mark each point as verified (you read or ran it) or inferred.
- Report what matters for the stated decision. If a claim holds, say so
  plainly and do not pad the reply with minor findings.
- If the brief lacks material you need or is ambiguous, say what is missing.
- Use the return format the brief asks for. When it fixes the exact form of
  the reply, keep that form and put other notes only where it allows.

---

"""


def fail(msg):
    print(f"cross-check: {msg}", file=sys.stderr)
    sys.exit(1)


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path, data):
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8", newline="\n")


def load_defaults():
    merged = {peer: dict(v) for peer, v in BUILTIN.items()}
    if USER_FILE.exists():
        for peer, v in read_json(USER_FILE).items():
            merged.setdefault(peer, {}).update(v)
    return merged


def codex_home():
    return Path(os.environ.get("CODEX_HOME") or Path.home() / ".codex")


def validate(peer, model, effort):
    if peer == "claude":
        if effort not in CLAUDE_EFFORTS:
            fail(f"Claude Code effort must be one of {', '.join(CLAUDE_EFFORTS)}; got {effort!r}")
        return
    cache = codex_home() / "models_cache.json"
    if not cache.exists():
        return
    models = {m.get("slug"): m for m in read_json(cache).get("models", [])}
    if model not in models:
        fail(f"unknown Codex model {model!r}; available: {', '.join(sorted(k for k in models if k))}")
    levels = [x.get("effort") if isinstance(x, dict) else x
              for x in models[model].get("supported_reasoning_levels") or []]
    if levels and effort not in levels:
        fail(f"{model} supports effort {', '.join(levels)}; got {effort!r}")


def find_codex():
    found = os.environ.get("CODEX_BIN") or shutil.which("codex")
    if found:
        return found
    # The Windows desktop app keeps its CLI in a hashed folder that changes on update.
    bundled = Path(os.environ.get("LOCALAPPDATA", "")) / "OpenAI" / "Codex" / "bin"
    exes = sorted(bundled.glob("*/codex.exe"), key=lambda p: p.stat().st_mtime)
    if exes:
        return str(exes[-1])
    fail("codex CLI not found; set CODEX_BIN")


def call(cmd, prompt, cwd, log_path):
    env = dict(os.environ, **{PEER_ENV: "1"})
    p = subprocess.run(cmd, input=prompt, capture_output=True, text=True, encoding="utf-8",
                       errors="replace", cwd=cwd, env=env)
    log_path.write_text(p.stdout + "\n--- stderr ---\n" + p.stderr, encoding="utf-8", newline="\n")
    return p.returncode, p.stdout, p.stderr


def codex_turn_contexts(thread_id):
    """(model, effort) of every turn the Codex session files record, oldest first."""
    out = []
    for f in sorted((codex_home() / "sessions").glob(f"*/*/*/rollout-*-{thread_id}.jsonl")):
        for line in f.read_text(encoding="utf-8", errors="replace").splitlines():
            try:
                rec = json.loads(line)
            except json.JSONDecodeError:
                continue
            if rec.get("type") == "turn_context":
                p = rec.get("payload", {})
                out.append((p.get("model"), p.get("effort")))
    return out


def run_codex(prompt, session, model, effort, cwd, reply_path, log_path):
    common = ["--json", "-m", model, "-c", f'model_reasoning_effort="{effort}"',
              "--skip-git-repo-check", "-o", str(reply_path)]
    if session:
        cmd = [find_codex(), "exec", "resume", *common, "-c", 'sandbox_mode="read-only"', session, "-"]
    else:
        cmd = [find_codex(), "exec", *common, "-s", "read-only", "-C", cwd, "-"]
    turns_before = len(codex_turn_contexts(session)) if session else 0
    rc, stdout, stderr = call(cmd, prompt, cwd, log_path)

    thread_id, usage, errors, warnings = None, None, [], []
    for line in stdout.splitlines():
        try:
            ev = json.loads(line)
        except json.JSONDecodeError:
            continue
        if ev.get("type") == "thread.started":
            thread_id = ev.get("thread_id")
        elif ev.get("type") == "turn.completed":
            usage = ev.get("usage")
        elif ev.get("type") == "turn.failed":
            errors.append(ev)
        elif ev.get("type") == "error":  # can be a recovered stream error, such as a reconnect
            warnings.append(ev)
    if not thread_id:
        errors.append("no thread id")
    elif session and thread_id != session:
        errors.append(f"resume returned thread {thread_id}, expected {session}")
    if rc != 0:
        errors.append(f"codex exited {rc}: {stderr.strip()[-1000:]}")
    if usage is None and not errors:
        errors.append("no turn.completed event")
    reply = reply_path.read_text(encoding="utf-8", errors="replace").strip() if reply_path.exists() else ""
    if not reply and not errors:
        errors.append("empty reply")

    turns = codex_turn_contexts(thread_id) if thread_id else []
    served = turns[-1] if len(turns) > turns_before else (None, None)
    return {"ok": not errors, "session_id": thread_id, "served_model": served[0],
            "served_effort": served[1], "served_source": "Codex session file (client turn settings)",
            "usage": usage, "errors": errors, "warnings": warnings}


def is_dated(served, model):
    """True when served is model plus a date snapshot suffix, such as claude-x-20261101."""
    return re.fullmatch(re.escape(model) + r"-\d{8}", served) is not None


def run_claude(prompt, session, model, effort, cwd, add_dirs, reply_path, log_path):
    exe = shutil.which("claude") or fail("claude CLI not found on PATH")
    # File reading only: no shell (git status and git diff can write) and no MCP servers.
    cmd = [exe, "-p", "--output-format", "json", "--model", model, "--effort", effort,
           "--tools", "Read,Grep,Glob", "--strict-mcp-config", "--permission-mode", "dontAsk"]
    for d in add_dirs:
        cmd += ["--add-dir", d]
    if session:
        cmd += ["--resume", session]
    rc, stdout, stderr = call(cmd, prompt, cwd, log_path)
    try:
        out = json.loads(stdout)
    except json.JSONDecodeError:
        out = {}
    if not isinstance(out, dict):
        out = {}

    errors = []
    if out.get("is_error") or rc != 0:
        errors.append(out.get("result") or f"claude exited {rc}: {stderr.strip()[-1000:]}")
    reply = (out.get("result") or "").strip()
    if not errors and not reply:
        errors.append("empty reply")
    if not errors and not out.get("session_id"):
        errors.append("no session id")
    if not errors:
        reply_path.write_text(out["result"], encoding="utf-8", newline="\n")

    # modelUsage is aggregate: it shows the requested model took part, not which model wrote the reply.
    used = out.get("modelUsage") or {}
    dated = [m for m in used if is_dated(m, model)]
    served = model if model in used else dated[0] if dated else next(iter(used)) if len(used) == 1 else None
    return {"ok": not errors, "session_id": out.get("session_id"), "served_model": served,
            "served_effort": None, "served_source": "modelUsage (aggregate); Claude Code does not report effort",
            "usage": {"by_model": used, "cost_usd": out.get("total_cost_usd")},
            "errors": errors}


def reserve_round(run_dir, prompt):
    """Claim the next round number by creating its prompt file exclusively."""
    n = 1
    while True:
        path = run_dir / f"round-{n:02d}.prompt.md"
        if any((run_dir / f"round-{n:02d}.{ext}").exists() for ext in ("prompt.md", "reply.md", "meta.json", "log")):
            n += 1
            continue
        try:
            with open(path, "x", encoding="utf-8", newline="\n") as f:
                f.write(prompt)
            return n, run_dir / f"round-{n:02d}"
        except FileExistsError:
            n += 1


def cmd_send(a):
    if os.environ.get(PEER_ENV):
        fail("this process is itself a cross-check peer; reviewers do not delegate")
    run_dir = Path(a.run_dir).resolve()
    run_dir.mkdir(parents=True, exist_ok=True)
    lock = run_dir / ".send.lock"
    try:
        fd = os.open(lock, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
    except FileExistsError:
        fail(f"another send is using {run_dir}; delete {lock.name} if none is running")
    os.write(fd, str(os.getpid()).encode())
    os.close(fd)
    try:
        send(a, run_dir)
    finally:
        lock.unlink(missing_ok=True)


def send(a, run_dir):
    session_file = run_dir / "session.json"
    session = read_json(session_file) if session_file.exists() else None

    if session:
        if session["peer"] != a.to:
            fail(f"{run_dir} holds a {session['peer']} session; use a new run dir for {a.to}")
        for key in ("model", "effort"):
            asked = getattr(a, key)
            if asked and asked != session[key]:
                fail(f"session uses {key} {session[key]!r}; start a new run dir to switch to {asked!r}")
        if a.cwd and str(Path(a.cwd).resolve()) != session["cwd"]:
            fail(f"session uses cwd {session['cwd']}; start a new run dir to change it")
        model, effort, cwd = session["model"], session["effort"], session["cwd"]
        add_dirs = list(dict.fromkeys(session.get("add_dirs", []) + [str(Path(d).resolve()) for d in a.add_dir]))
        if not a.prompt_file:
            fail("later rounds need --prompt-file")
        prompt_path = Path(a.prompt_file)
    else:
        defaults = load_defaults()[a.to]
        model, effort = a.model or defaults["model"], a.effort or defaults["effort"]
        cwd = str(Path(a.cwd or os.getcwd()).resolve())
        add_dirs = [str(Path(d).resolve()) for d in a.add_dir]
        prompt_path = Path(a.prompt_file) if a.prompt_file else run_dir / "brief.md"
    validate(a.to, model, effort)
    if not prompt_path.exists():
        fail(f"prompt file not found: {prompt_path}")
    prompt = prompt_path.read_text(encoding="utf-8")
    if not session:
        prompt = PEER_HEADER + prompt

    rnd, stem = reserve_round(run_dir, prompt)
    reply_path = Path(f"{stem}.reply.md")
    reply_path.unlink(missing_ok=True)
    sid = session["session_id"] if session else None
    started = time.time()
    log_path = Path(f"{stem}.log")
    if a.to == "codex":
        res = run_codex(prompt, sid, model, effort, cwd, reply_path, log_path)
    else:
        # The Claude peer reads only under its cwd and --add-dir, so the run dir is always added.
        readable = list(dict.fromkeys(add_dirs + [str(run_dir)]))
        res = run_claude(prompt, sid, model, effort, cwd, readable, reply_path, log_path)
    if sid and res["session_id"] != sid:
        # Claude Code may give a resumed conversation a new id; the history carries over.
        res["resumed_from"] = sid

    served = res["served_model"]
    model_match = (served == model or (a.to == "claude" and is_dated(served, model))) if served else None
    effort_match = res["served_effort"] == effort if res["served_effort"] else None
    meta = {"round": rnd, "peer": a.to, "requested_model": model, "requested_effort": effort, **res,
            "model_match": model_match, "effort_match": effort_match, "cwd": cwd, "add_dirs": add_dirs,
            "seconds": round(time.time() - started, 1),
            "finished": datetime.now(timezone.utc).isoformat(timespec="seconds")}
    write_json(Path(f"{stem}.meta.json"), meta)
    if res["ok"]:
        write_json(session_file, {"peer": a.to, "session_id": res["session_id"], "model": model,
                                  "effort": effort, "cwd": cwd, "add_dirs": add_dirs})

    print(f"peer: {a.to}  session: {res['session_id']}  round: {rnd}  seconds: {meta['seconds']}")
    print(f"requested: {model} / {effort}")
    print(f"served:    {res['served_model'] or 'unknown'} / {res['served_effort'] or 'not reported'}")
    if not res["ok"]:
        fail(f"round {rnd} failed; see {stem}.log and {stem}.meta.json: {res['errors'][:2]}")
    print(f"reply: {reply_path}")
    effort_ok = effort_match is True if a.to == "codex" else effort_match is not False
    if model_match is not True or not effort_ok:
        print("WARNING: the served model or effort differs from the request or is unknown; "
              "tell YU before using this reply", file=sys.stderr)
        sys.exit(2)


def cmd_defaults(a):
    if a.model or a.effort:
        if not a.to:
            fail("--to is required with --model or --effort")
        data = read_json(USER_FILE) if USER_FILE.exists() else {}
        data.setdefault(a.to, {}).update({k: v for k, v in (("model", a.model), ("effort", a.effort)) if v})
        merged = {**BUILTIN[a.to], **data[a.to]}
        validate(a.to, merged["model"], merged["effort"])
        USER_FILE.parent.mkdir(parents=True, exist_ok=True)
        write_json(USER_FILE, data)
    print(json.dumps({"file": str(USER_FILE), "defaults": load_defaults()}, indent=2))


class Parser(argparse.ArgumentParser):
    """Usage errors exit 1, so exit 2 keeps its documented meaning."""

    def error(self, message):
        self.print_usage(sys.stderr)
        fail(message)


def main():
    p = Parser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("send")
    s.add_argument("--to", choices=["codex", "claude"], required=True)
    s.add_argument("--run-dir", required=True)
    s.add_argument("--prompt-file")
    s.add_argument("--cwd", help="peer working directory (default: current directory)")
    s.add_argument("--add-dir", action="append", default=[], help="extra readable directory (Claude peer)")
    s.add_argument("--model")
    s.add_argument("--effort")
    s.set_defaults(func=cmd_send)
    d = sub.add_parser("defaults")
    d.add_argument("--to", choices=["codex", "claude"])
    d.add_argument("--model")
    d.add_argument("--effort")
    d.set_defaults(func=cmd_defaults)
    a = p.parse_args()
    a.func(a)


if __name__ == "__main__":
    main()
