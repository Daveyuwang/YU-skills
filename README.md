# YU Skills

Personal AI agent skills shaped by YU's workflows, preferences, and standards.
The repository is English-first; Chinese wording is retained where it helps
preserve the meaning of a source or preference.

## Setup for coding agents

If YU shares this repository on its own or asks you to use YU Skills, set up
the plugin in the current agent's user profile. Carry out the steps below and
report the result. A separate request about the repository defines the task
for that session.

1. Check for the `yu-workflows` marketplace and the
   `yu-skills@yu-workflows` plugin. Use `codex plugin marketplace list` and
   `codex plugin list --marketplace yu-workflows` in Codex. Use
   `claude plugin marketplace list` and `claude plugin list` in Claude Code.
2. Reuse an existing marketplace registration. Run the missing commands from
   [Install in Codex and Claude Code](#install-in-codex-and-claude-code) to
   register and install the plugin. If it is disabled, run the Codex
   `plugin add` command again or run
   `claude plugin enable yu-skills@yu-workflows --scope user`.
3. Read [YU's workflow defaults](docs/personal-defaults.md) and put that
   section in the current profile's instructions file. For Codex, use
   `AGENTS.md` in `CODEX_HOME` (default `~/.codex`), or the active
   `AGENTS.override.md` if present. For Claude Code, use `CLAUDE.md` in
   `CLAUDE_CONFIG_DIR` (default `~/.claude`). Update the YU section in place
   if it already exists and preserve the rest of the file.
4. Check that the plugin is enabled and that the defaults are in the active
   instructions file. Tell YU which profile is ready and to start a new
   chat or session. If a step requires GitHub access or another user action,
   report the step that is blocked.

On Windows with Codex desktop, use the running app's bundled `codex.exe` if
`codex` is unavailable on PATH. In PowerShell,
`Get-Process -Name codex | Select-Object -First 1 -ExpandProperty Path` gives
its path.

## Skills

- [Clear writing](skills/clear-writing/SKILL.md): concise, direct prose.
- [Research writing](skills/research-writing/SKILL.md): research papers,
  arguments, tables, and evidence-backed claims.
- [Research figures](skills/research-figures/SKILL.md): scientific figures,
  plots, and method diagrams.
- [Pragmatic coding](skills/pragmatic-coding/SKILL.md): minimal code,
  repository structure, and proportionate checks.
- [Adaptive reflection](skills/adaptive-reflection/SKILL.md): reassess complex,
  evolving research or engineering work.
- [Research ideas](skills/research-ideas/SKILL.md): develop ideas, assess
  novelty, and plan implementation and experiments.
- [Research integrity](skills/research-integrity/SKILL.md): audit a paper's
  consistency and support from available evidence.

[Source notes](docs/) record YU's guidance and external sources, including
original Chinese wording where it matters.

## Install in Codex and Claude Code

Install `yu-skills@yu-workflows` once per agent and user profile. Both plugins
use the same `skills/` directory. Run the pair of commands for your agent
from any directory. Use a GitHub account with access to this repository.

**Codex**

```sh
codex plugin marketplace add Daveyuwang/YU-skills
codex plugin add yu-skills@yu-workflows
```

**Claude Code**

```sh
claude plugin marketplace add Daveyuwang/YU-skills
claude plugin install yu-skills@yu-workflows --scope user
```

To use a local checkout for development, run the commands at its root and
replace `Daveyuwang/YU-skills` with `"$PWD"`.

In Codex desktop, restart the app after registering the marketplace to refresh
the Plugins page. Look for **YU Skills** under **YU Workflows**. In Claude Code,
start a new session or run `/reload-plugins` in an existing session. Windows
and WSL use separate user profiles. Run the relevant commands in each
environment where you use the agent.

## Use the workflows

For personal defaults in every project, append
[YU's workflow defaults](docs/personal-defaults.md) to `~/.codex/AGENTS.md`
for Codex or `~/.claude/CLAUDE.md` for Claude Code. Preserve any instructions
already in those files. Start a new session after editing. The defaults tell
the agent which skills to use when you describe the work in your own words.

Try “Tighten this email to my advisor”, “Fix this parser and check the edge
case”, or “帮我重写论文摘要”. You can also select a skill directly with
`$yu-skills:clear-writing` in Codex or `/yu-skills:clear-writing` in Claude
Code. Check the installed bundle with
`codex plugin list --marketplace yu-workflows` or
`claude plugin details yu-skills`.

## Update the plugin

For a GitHub install, refresh the marketplace and then update the plugin.

| Agent | Refresh the marketplace | Update the plugin |
| --- | --- | --- |
| Codex | `codex plugin marketplace upgrade yu-workflows` | `codex plugin add yu-skills@yu-workflows` |
| Claude Code | `claude plugin marketplace update yu-workflows` | `claude plugin update yu-skills@yu-workflows --scope user` |

Start a fresh session after updating. For a local checkout, run just the
plugin update command. When releasing skill changes, bump the version in both
`.codex-plugin/plugin.json` and `.claude-plugin/plugin.json` before pushing.

For an agent that loads standalone skills, copy the complete skill folder
with its references and license notices to that agent's skill directory.
Codex discovers standalone user skills in `~/.agents/skills/`, and Claude
Code uses `~/.claude/skills/`. Use one installation method per skill to
avoid duplicate entries. See the [Codex plugin guide](https://developers.openai.com/plugins/build/plugins)
and the [Claude Code marketplace guide](https://code.claude.com/docs/en/plugin-marketplaces).

## Research project template

[Research workspace](templates/research-workspace/README.md) is a copyable
folder for a research brief, current state, findings, and experiment records.
Copy it into a project as `.research/`, then follow its setup instructions.

