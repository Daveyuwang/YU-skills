# YU Skills

Eight skills for Codex and Claude Code based on YU's writing, coding, research,
and open-source project workflows.

## Setup for coding agents

If the user shares this repository link on its own or asks to use YU Skills,
run the setup for the current agent and user profile.

1. Check for the `yu-workflows` marketplace and the
   `yu-skills@yu-workflows` plugin with the agent's `plugin marketplace list`
   and `plugin list` commands. Reuse a working registration and run the missing
   [install commands](#install-in-codex-and-claude-code). To enable a disabled
   plugin, rerun
   `codex plugin add yu-skills@yu-workflows` or run
   `claude plugin enable yu-skills@yu-workflows --scope user`.
2. Merge the [workflow defaults](docs/personal-defaults.md) into the user's
   instructions. Use `AGENTS.md` under `CODEX_HOME` (default `~/.codex`), or
   `AGENTS.override.md` if active. For Claude Code, use `CLAUDE.md` under
   `CLAUDE_CONFIG_DIR` (default `~/.claude`). Replace an existing YU section
   in place.
3. Verify that the plugin is enabled and the defaults are saved. Report which
   profile is ready and tell the user to start a new session. Report any step
   that needs the user's help.

If `codex` is missing from PATH on Windows, locate the running desktop app's
bundled CLI with
`Get-Process -Name codex | Where-Object Path | Select-Object -First 1 -ExpandProperty Path`.

## Install in Codex and Claude Code

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

For automatic skill selection, add the [workflow defaults](docs/personal-defaults.md)
to your user instructions as described above. Start a new session. In Codex
desktop, restart the app if the plugin list needs to refresh. Install separately
for each profile you use, including Windows and WSL.

To invoke a skill directly, use `$yu-skills:clear-writing` in Codex or
`/yu-skills:clear-writing` in Claude Code.

## Skills

- [Clear writing](skills/clear-writing/SKILL.md) for concise prose.
- [Research writing](skills/research-writing/SKILL.md) for manuscripts, tables, and evidence-backed claims.
- [Research figures](skills/research-figures/SKILL.md) for scientific plots and method diagrams.
- [Pragmatic coding](skills/pragmatic-coding/SKILL.md) for focused code changes and checks.
- [Adaptive reflection](skills/adaptive-reflection/SKILL.md) for complex research and engineering plans.
- [Research ideas](skills/research-ideas/SKILL.md) for research questions, novelty, and experiment planning.
- [Research integrity](skills/research-integrity/SKILL.md) for auditing claims and evidence.
- [OSS ideas](skills/oss-ideas/SKILL.md) for choosing, validating, and committing to open-source projects, and turning them into research.

## Development and updates

Both plugins use `skills/`. For local development, run the install commands
from the checkout and use `"$PWD"` as the marketplace source. Bump the version
in both plugin manifests when releasing skill changes.

| Agent | Refresh a GitHub marketplace | Update the plugin |
| --- | --- | --- |
| Codex | `codex plugin marketplace upgrade yu-workflows` | `codex plugin add yu-skills@yu-workflows` |
| Claude Code | `claude plugin marketplace update yu-workflows` | `claude plugin update yu-skills@yu-workflows --scope user` |

For a local checkout, run just the plugin update command. Start a new session
after updating.

For a standalone install, copy the whole skill folder to `~/.agents/skills/`
for Codex or `~/.claude/skills/` for Claude Code. Use one installation method
per skill to avoid duplicates.

[Source notes](docs/) record YU's original guidance and references. Copy the
[research workspace template](templates/research-workspace/README.md) to
`.research/` in a research project.

