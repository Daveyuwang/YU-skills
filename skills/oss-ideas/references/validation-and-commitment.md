# Validating and Committing to a Project

## Prove value with a measurement users care about

Measure the outcome a user cares about, not only a component score. For a
tool that sits between users and a system, that is usually whether the user's
task still succeeds. Compare doing nothing, the naive approach, and the
proposed approach on the same tasks. A clear number, such as task success
rising from 56% to 97%, becomes the project's headline and later the core of
any report.

Keep the measurement honest:

- If rules or settings were tuned on your own benchmark, also evaluate on
  public held-out data, and say which numbers are optimistic.
- Disclose any change made after seeing held-out results.
- Report where the project loses, not only where it wins.
- Add end-to-end checks with the real hosts, such as real agents and real
  APIs, alongside the benchmark. Use real runs, not mocks.

## Gate the commitment on a comparison

Before long-term investment, compare the project with the closest tools on
the same benchmark and on public datasets that other projects use. Run each
competitor in its strongest documented configuration and note where that
differs from its defaults. Decide the outcomes in advance:

- leads on the core value: proceed;
- leads only on a secondary point: reposition around that point;
- leads on nothing that matters: stop.

## Build a product, not a demo

YU's projects should be usable: "要可用，而不是 toy". Plan these alongside the
technical work:

- an install path a stranger can follow, with sensible defaults;
- failures that tell the user what happened, and that fail safe where the
  project protects something;
- integration with the tools people already use, as plugins, adapters, or a
  proxy, so adoption does not require changing habits;
- resource use proportional to the host: a helper should not use more memory
  or start more slowly than the tool it serves;
- documentation a newcomer can follow, and daily use by YU.

Prefer fewer features that work end to end. Keep code minimal and remove
superseded code, following [pragmatic coding](../../pragmatic-coding/SKILL.md).

## Commit with a version 1 bar

Once YU decides to invest, write a one-page brief: the problem, the users,
why now, the differentiators, the minimum viable product, and the version 1
bar. A useful version 1 bar for a showcase project includes a public release,
prebuilt packages, a published benchmark and comparison, a stated threat
model or limits, a short demo, and a few outside users. Plan milestones
against it, and research each milestone to a solid plan before starting it.

Check that the name is free on the relevant package registries and GitHub.
Keep the repository private until YU approves making it public; releases and
registry publishing also need YU's approval.
