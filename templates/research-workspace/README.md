# Research Workspace

This folder helps a research project keep the information needed to continue
its work: the question, current state, evidence, and experiment records. Use
only the parts the project needs. The files are starter documents, not claims
that an experiment has been planned or run.

## Add it to a project

1. Copy this folder into the project, using `.research/` as a convenient name.
   If a research folder already exists, inspect it first and merge only useful
   pieces without overwriting existing records.
2. Fill in [brief.md](brief.md), and reconcile [status.md](status.md) and
   [findings.md](findings.md) with the project. Mark missing facts as unknown.
3. Copy [experiments/TEMPLATE.md](experiments/TEMPLATE.md) for a test when a
   record is useful. Link to the actual data, logs, and results.

If the project already maintains equivalent findings, status, or experiment
records, use those as the source of truth and link to them instead of copying
their contents into this folder.

The folder does not require a specific agent or runtime. To make it discoverable
to an agent that reads a project-root `AGENTS.md`, add an instruction such as
the following to that file without replacing existing instructions:

```text
For this project's research work, consult .research/README.md and the relevant
brief, status, findings, and experiment records before proceeding.
```

Adjust the path if the folder has a different name. Copying it does not
authorize experiments, paid resources, or changes outside the requested work.

## Fit the project

Use the existing project structure where it works. Keep reusable code,
configuration, run entry points, artifacts, and final reports easy to find.
Use notebooks for exploration and put reusable experiment logic in code.
Create directories only as needed.

The project README should help a newcomer set up the project, run a small
experiment, understand its outputs, and find the commands for reproducing the
paper's main results when applicable. Use commands and results grounded in the
project, and identify unavailable or unverified steps.

## Work from evidence

- Use the question, existing evidence, time, and compute to choose the next
  informative test. Treat a chosen idea as a working hypothesis and investigate
  contrary evidence.
- Record the baseline, change, input version, evaluation conditions, and
  source of each result. Make comparisons appropriate to the question and
  explain meaningful differences in data, metrics, compute, or time budget.
- Separate plans, observations, and interpretations. Distinguish reanalysis
  from new data collection and note which commands or results were verified.
  Recheck dependencies on older code or configuration after material changes;
  treat screening results as preliminary until the next decision is supported.
- For constrained runs, estimate duration and cost, including startup and
  evaluation when material. Revisit estimates as evidence changes. Record
  constraints and required approvals without storing credentials here.

## Keep state useful

Use experiment records and source artifacts to support findings. Keep status as
a short handoff with active runs, latest evidence, the next action, and any
real blocker. Update it after material progress and before handoff. Avoid
duplicating logs or creating planning files the project does not use.

This template draws on ideas from [Open Research Loop](https://github.com/vukrosic/auto-research/tree/f229de2bf558982f476a2088748daf4250c48088).
