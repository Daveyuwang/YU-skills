# Pragmatic Coding: Source Notes

Source: YU's `HERO-anti-overdefense.md` summary and the original
[HERO Anti-OverDefense rules](https://github.com/wanshuiyin/HERO-Anti-OverDefense/blob/main/RULES.md),
by Ruofeng Yang, distributed under the MIT license. The applicable notice is
included with the [skill](../skills/pragmatic-coding/LICENSE-HERO.txt).

The [pragmatic-coding skill](../skills/pragmatic-coding/SKILL.md) distills the
four themes: unjustified hashing, defenses for unsupported edge cases,
mechanical rechecks, and unnecessary scaffolding. It also retains the central
distinction between identifying real problems and keeping fixes proportional,
including the legitimate roles of focused smoke tests and bounded exploratory
checks. The source's longer case catalog is not loaded into the skill.

The adaptation uses the actual project and threat model rather than assuming
every environment is private. It preserves explicit user, project, and
higher-priority requirements. The source notes a possible conflict over
co-author markers in another environment; the skill omits unrequested markers
while respecting applicable attribution requirements rather than changing
that environment's configuration.

YU's later coding preferences add minimal, well-structured code and project
layouts. The research directory map is illustrative; projects should create
only useful directories and retain their existing conventions. The guidance
also distinguishes research READMEs, which should support a small experiment
and paper reproduction, from application READMEs, which should present real
features in a polished, attractive way. A project can serve both audiences.

HERO is designed as automatically loaded agent instructions, while a skill is
selected as needed. This repository points its [AGENTS.md](../AGENTS.md) at the
skill for coding work here; other projects need their own agent instruction or
explicit invocation if they require the same always-on behavior.
