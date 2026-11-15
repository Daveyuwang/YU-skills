---
name: pragmatic-coding
description: >-
  Use YU's coding conventions to implement a feature, fix a bug, refactor,
  review code, choose tests, or organize a repo or README. Prefer simple
  changes and targeted verification. Use for 修 bug、重构、代码审查 and 项目结构.
---

# Pragmatic Coding

Complete the requested work using judgment grounded in the project. Keep the
solution proportional, but do not dismiss real defects or skip verification
that the task, project, or higher-priority instructions require.

## Keep code and structure minimal

Use the smallest clear, maintainable implementation that meets the task.
Keep related responsibilities easy to find and follow existing project
conventions. Add files, directories, abstractions, dependencies, and
configuration only when they have a useful role. Minimal code still needs the
correctness, readability, and verification the task requires.

For repository organization or project READMEs, consult
[repository design](references/repository-design.md). It covers research
experiment management and the different needs of research and application
audiences.

## Find real problems; keep fixes in scope

- Understand the requested behavior and supported use from the project,
  including documented examples, public interfaces, and real data. Report a
  genuine issue in scope even if it sounds rare; a supported path can establish
  reachability without a full reproduction. State what remains unverified.
- Do not add guards, feature flags, compatibility layers, migrations, or
  wrappers solely for scenarios that the project does not need to support.
  Preserve existing supported behavior and address real failure modes.
- Match security and validation to the actual environment and requirements.
  A local single-user tool does not automatically need an adversarial threat
  model; exposed or security-sensitive systems may have one. Do not infer away
  a real threat or an explicit requirement.
- Avoid checksums, hashes, or fingerprints added only for reassurance. They can
  be useful when they replace materially more expensive work and affect the
  next action, or when integrity, security, provenance, or the task actually
  requires them. For example, an available digest may avoid rereading an
  unchanged large file; hashing every row to perform an ordinary comparison
  is not justified merely because the hashes are read.

## Verify with purpose

Choose checks that address a live uncertainty and whose outcome can affect
the next step. A bounded exploratory run to discover which consumer broke can
be appropriate even when the exact failure is unknown. Exercise the changed
behavior with an appropriately small realistic test or smoke run; if a real
run already covers the same path, avoid duplicating it without a reason.

Run checks explicitly required by the user, project, or governing instructions.
Once appropriate checks pass, repeat or broaden them only when changes,
failures, or a new concern justify it. Use judgment rather than manufacturing
scorecards or findings; say when the reviewed work is correct.

## Keep moving and communicate clearly

When several reasonable, reversible approaches fit, choose one and proceed.
Ask when essential information is unavailable, the options materially diverge,
or the action needs authorization. A nonblocking detail need not stop the task.

Keep code, comments, documentation, and review descriptions focused on the
final behavior and useful decisions. Omit abandoned approaches, process
traces, defensive boilerplate, and unrequested generator or co-author markers;
follow explicit attribution requirements. Report material failures, limitations,
or tradeoffs when needed to understand the outcome.

Adapted from [HERO Anti-OverDefense](https://github.com/wanshuiyin/HERO-Anti-OverDefense);
its MIT notice is in [LICENSE-HERO.txt](LICENSE-HERO.txt).
