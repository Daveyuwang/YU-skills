---
name: cross-check
description: >-
  Hand work to the other coding agent for an adversarial check and bring back
  verified findings: Claude Code sends to Codex (GPT), and Codex sends to
  Claude Code (Claude). Use whenever YU wants a second model to attack,
  review, audit, red-team, or give a second opinion on a plan, diff, bug
  diagnosis, experiment, result, claim, or draft, even when YU only says "ask
  Codex", "let GPT check", or "have Claude look". Also use whenever another
  skill sends work to a reviewer model, including every ARIS review skill
  (research-review, auto-review-loop, kill-argument, experiment-audit,
  paper-claim-audit), so the model defaults and handoff rules apply. Also
  applies to 交叉审查、对抗性检查、第二意见 and 让 Codex 或 Claude 审一下.
---

# Cross-check

A strong model from another family tries to break the work before anyone acts
on it. Its value comes from independence: it does not share the author's
context, assumptions, or blind spots. It also knows only the brief and the
files it can read, so the brief decides what the check can find.

## Peer and model

The peer is the other agent: Codex when you run in Claude Code, Claude Code
when you run in Codex. Defaults are the strongest models YU uses:

| Peer | Model | Effort |
| --- | --- | --- |
| Codex | `gpt-6.2-astra` (GPT-6.2 Astra) | `max` |
| Claude Code | `claude-fable-5-2` (Fable 5.2) | `xhigh` |

- Use the defaults without asking YU about models.
- When YU names a model or effort, map it to the exact id, use it for this
  check, and confirm in one line with the served model the script prints. If
  the script exits 2, the served model is unknown or differs from the request,
  or Codex ran at a different effort: tell YU before using the reply. Claude
  Code does not report its effort, so the Claude direction confirms the model
  only.
- When YU changes the default ("use X from now on"), run
  `python <this skill>/scripts/cross_check.py defaults --to <peer> --model <id> --effort <level>`
  and show the output. It validates the choice and writes
  `~/.yu-skills/cross-check.json`.
- A session keeps its model and effort, so a different model needs a new run
  directory.

## Review skills such as ARIS

ARIS reviewer skills are a main use. Keep their prompts, independence rules,
rounds, traces, and verdict formats, and change only the model routing:

- Codex reviewer calls pin the default Codex model in place of the skill's
  model. Use `max` where the skill says `xhigh`, and keep `ultra`, which is
  above `max`.
- The reviewer must come from the other model family. From Codex, send the
  review to Claude through this skill's script, which sets the effort (ARIS's
  `claude-code` bridge cannot), rather than to a native Codex subagent.
- When the skill fixes the reply format, do not add sections to it. Report
  what the reviewer could not check in your own summary.

The same routing applies to any other workflow that asks a second model to
review, audit, or argue against the work.

## Workflow

1. **Name the decision.** State what will change depending on the result. A
   check tied to one decision gets a focused answer, so split broad requests.
2. **Write the brief** to `<project>/.cross-check/<YYYY-MM-DD>-<slug>/brief.md`
   (or the project's own trace location) from the
   [brief template](references/brief.md). A reviewer handed the author's
   conclusion tends to confirm it, so:
   - Point to primary material: absolute paths, diff ranges, commands, raw
     outputs. Save a copy into the run directory of anything the peer cannot
     read, such as web pages, chat-only context, or files on another machine.
   - Quote YU's requirements verbatim with dates and label any paraphrase.
   - State each claim as the author makes it, with the evidence it rests on.
     Ask the peer to break it ("find a case where X fails"), not to confirm it.
   - Leave out your verdict, confidence, and preferred answer. Include your
     reasoning only when the reasoning is under review, and label it so.
   - List settled decisions with their source so the peer does not reargue
     them. The peer may still flag a factual error in one.
3. **Check the brief.** A reader without this conversation could do the check
   from the brief and the files. Every path and diff range resolves, and the
   brief describes the files as they are now. No secrets or `.env*` contents.
4. **Send.** A check at max effort can take 10 to 40 minutes, so run it in the
   background or with a long timeout:
   `python <this skill>/scripts/cross_check.py send --to codex --run-dir <dir> --cwd <project>`
   From Codex, use `--to claude` and run it outside the Codex sandbox, since
   it needs network access and the peer's home directory. The script adds the
   reviewer rules, keeps the peer read-only, and records the served model.
   The Codex peer can run commands in a read-only sandbox. The Claude peer can
   only read files, so save diffs and test or script output it needs into the
   run directory, and pass `--add-dir` for directories outside `--cwd`.
5. **Verify the reply.** Check every finding against the primary material.
   Sort findings into confirmed, rejected (with your evidence), and needs YU.
   The peer can be wrong with confidence, and agreement is not proof.
6. **Rebut or confirm fixes if useful.** Write disputed findings with your
   evidence, or the fixes you made, to `round-02.md` and send it with
   `--prompt-file` to continue the same session. Stop after two or three
   rounds, or when a round adds no new evidence.
7. **Report to YU:** findings that matter for the decision, what you changed or
   will change, what you rejected and why, insights beyond defects, what stays
   open, the served model and effort, and the run directory. Quote the raw
   reply where exact wording matters.

## When you are the peer

Follow the reviewer rules at the top of the brief and its return format. Do
not hand the task to another agent. If the brief is missing material, say what
is missing first, then check what you can.

## Uses

| Check | Send | Ask the peer to attack |
| --- | --- | --- |
| Code change | diff, requirement, test commands and output | wrong behavior on supported paths, missed callers, untested cases |
| Bug diagnosis | symptom, logs, repro, the hypothesis as a claim | other causes that fit the evidence, a test that separates them |
| Plan or design | plan file, goal, constraints | false premises, missing steps, simpler options, hard-to-undo steps |
| Experiment before a run | spec, config, thresholds, cost estimate | confounds, leakage, thresholds that cannot fail, cost errors |
| Results to claims | claim text, tables, scripts, raw outputs | numbers that do not match, claims beyond the evidence, other explanations |
| Writing | the section and the evidence it relies on | unsupported claims, likely misreadings |
| Skills and prompts | the files, intended behavior, sample tasks | ambiguous or conflicting rules, cases an agent would get wrong |
