# YU Skills

Personal AI agent skills shaped by YU's workflows, preferences, and standards.
The repository is English-first; Chinese wording is retained where it helps
preserve the meaning of a source or preference.

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

## Use a skill in another project

Each folder under `skills/` is a complete skill. Copy the whole folder,
including its references and any license notice, to a location your agent
discovers. Keep this repository as the source for updates; copied skills do
not update automatically.

For a Codex project, copy a skill into the project's `.agents/skills/` folder.
For example, run this from this repository in bash or WSL after replacing the
project path:

```bash
project_dir="/path/to/project"
mkdir -p "$project_dir/.agents/skills"
cp -R skills/research-writing "$project_dir/.agents/skills/"
```

Replace `research-writing` with any skill folder above. If the target already
exists, compare it before copying or merging. For personal use in multiple
projects, Codex also discovers skills under `~/.agents/skills/`. Copies with
the same name in different locations may both appear. Other agents may use
different locations; follow their setup instructions.

Ask for a matching task or invoke the skill by name, for example
`$research-writing`. Codex can select matching skills automatically; if a new
skill does not appear, restart Codex. See the
[official skill locations](https://developers.openai.com/codex/build-skills).

To make a skill a project default, add an instruction to the project's existing
`AGENTS.md`, such as:

```text
For research writing, read and apply .agents/skills/research-writing/SKILL.md.
```

Adjust the path for the installed skill and preserve existing instructions.

## Research project template

[Research workspace](templates/research-workspace/README.md) is a copyable
folder for a research brief, current state, findings, and experiment records.
Copy it into a project as `.research/`, then follow its setup instructions.

