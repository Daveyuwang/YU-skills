# Repository Design

Use a clear structure with only the parts the project needs. Fit the existing
layout and conventions before adding new directories. Keep reusable logic in
one sensible place and keep entry points focused on orchestration.

## Research project layout

This is a useful pattern, not a required scaffold. Names and boundaries may
change to suit the project or its existing experiment tools.

| Directory | Responsibility |
| --- | --- |
| `src/` | Reusable algorithms, model interfaces, and evaluation logic. |
| `configs/` | Models, baselines, experiment conditions, and hyperparameters. |
| `scripts/` | Entry points for experiments, data preparation, result aggregation, and paper reproduction. |
| `tests/` | Useful unit and integration tests, including metric correctness. |
| `runs/` | Run logs, raw outputs, traces, and metadata. |
| `reports/` | Final tables and figures used in the paper. |
| `notebooks/` | Exploratory analysis; keep reusable experiment logic in code. |
| `docs/` | Experiment design, data sources, reproduction, and implementation details. |

Experiment management is part of the project design. For each meaningful run,
make it possible to find its status, configuration, code revision, data and
split, relevant environment and seeds, metrics, logs, and output artifacts.
Record actual observations separately from plans. Compare results with an
appropriate baseline under relevant, comparable conditions. Reuse the
project's experiment tracker or artifact storage when it already serves these
needs; a particular directory, database, or tracking service is not required.

## README for a research project

The reader should be able to start from a fresh checkout, run a small
experiment, interpret its output, and find the procedure for reproducing the
paper's main results. Include the prerequisites, setup and data access needed
for that path, a concrete small-run command, the output location and format,
and the meaning of key metrics. Give the main reproduction commands and any
material resource, environment, or evaluation conditions. Explain whether a
command analyzes recorded data, exercises a mock, or collects new results.
If a step is not available or has not been verified, state its status. Ground
commands and results in the actual project.

## README for a software or AI application

Lead with the application's value and real features. Make the page polished
and easy to scan, using an available screenshot, demo, or other genuine visual
when it helps readers understand the product. Give a direct way to try or run
it. Do not invent features, visuals, links, or performance claims for
presentation. A project that is both research and a showcase can combine
these needs in one README.
