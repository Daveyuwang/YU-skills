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

Check that the proposed change addresses the actual need before implementing
it. Use the simplest maintainable solution that meets the task. For changes
that span modules, decide where responsibilities belong and how the modules
interact before editing. Keep related code together and follow project
conventions that fit the task. Add files, directories, abstractions,
dependencies, and configuration only when they serve a clear purpose.

Keep scratch scripts and outputs outside source directories, and remove your
temporary files when finished. Archive superseded files only when they have a
concrete use, such as reproducing a result.

For repository organization or project READMEs, consult
[repository design](references/repository-design.md). It covers research
experiment management and the different needs of research and application
audiences.

## Find real problems; keep fixes in scope

- Understand the requested behavior and supported use from the project,
  including documented examples, public interfaces, and real data. Check old
  documentation and implementation choices against the current request and
  observed behavior before carrying them forward. Report genuine in-scope
  issues even if they sound rare. A supported path can establish reachability
  without a full reproduction. State what remains unverified.
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

Start with the fastest check or experiment that directly exercises the changed
behavior or resolves the current uncertainty. Use the normal entry point and
real dependencies where practical. For data-dependent changes, inspect
representative real inputs and outputs and check them against the expected
behavior. A passing test you wrote is insufficient evidence on its own if it
does not cover those inputs and outcomes. State any gaps in coverage.

Avoid mocks and smoke tests for verification. Run checks required by the user,
project, or governing instructions, and scope your claims to what each check
establishes. Reuse evidence from a real run that already covers the change.
During fast iteration, a focused check can be enough. Run the full suite when
required or when the scope of the change, a failure, or remaining uncertainty
warrants it. In reviews, report actual findings and say when the work is
correct.

## Keep moving and communicate clearly

When several reasonable, reversible approaches fit, choose one and proceed.
Tell the user which assumptions and defaults you introduced beyond the request.
Flag consequential assumptions before acting and repeat them in the final reply.
Ask when essential information is unavailable, the options materially diverge,
or the action needs authorization.

Keep code, comments, documentation, and review descriptions focused on the
final behavior and useful decisions. Omit abandoned approaches, process
traces, defensive boilerplate, and unrequested generator or co-author markers.
Follow explicit attribution requirements. Keep commit messages short and plain,
and name the change in the subject. Report material failures, limitations, or
tradeoffs when needed to understand the outcome.

Adapted from [HERO Anti-OverDefense](https://github.com/wanshuiyin/HERO-Anti-OverDefense);
its MIT notice is in [LICENSE-HERO.txt](LICENSE-HERO.txt).
