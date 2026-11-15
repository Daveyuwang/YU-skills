# From Project to Technical Report or Paper

A strong project can produce a second deliverable. Build the product or
framework first, then adapt it to a research setting to produce a more
rigorous technical report, which can later become a conference paper. The
working system gives the research a better demo, evaluation in real use, and
artifacts that others can run.

The risk is overlap. Product features alone rarely make a research
contribution, so the move needs its own novelty check and, where needed,
changes to the project or the study that create a distinct contribution.

## Prepare while building

These cost little during development and much to reconstruct later:

- Keep the evaluation reproducible: datasets, fixed seeds, scripts that
  regenerate every reported number, and the raw results.
- Record design decisions, failed attempts, and negative results as they
  happen. They become the method and analysis sections.
- Keep baselines and ablations runnable, for example with switches that turn
  off one component at a time.
- Keep tuning data separate from held-out evaluation data.

## Find the research contribution

Ask what building the project revealed that others do not know. A
contribution can be a new problem framing, a benchmark or measurement that
exposes something unmeasured, a mechanism with evidence for why it works, or
an analysis of a failure mode. State it as a claim that an experiment can
support or refute.

## Check novelty, then adapt

Run research-ideas' [prior-work assessment](../../research-ideas/references/prior-work-assessment.md)
on the candidate research claims, not on the product's feature list. Search
papers as well as tools. If a claim overlaps substantially with prior work,
adapt before writing: sharpen the question, change the setting or the
evaluation, or add the mechanism or analysis that makes the contribution
distinct. This can mean new experiments or a new component in the project.
Stop only on a substantive collision as research-ideas defines it.

## Choose the deliverable

- **Technical report:** the system, its design rationale, and a full
  evaluation. It has value even with modest novelty and can appear first.
- **Workshop paper:** one focused finding with solid evidence.
- **Conference paper:** a clear research contribution, strong baselines,
  ablations, and held-out evaluation. Choose the venue by the type of
  contribution, such as systems, security, or machine learning.

Then use [research-writing](../../research-writing/SKILL.md) for the text,
[research-figures](../../research-figures/SKILL.md) for figures, and
[research-integrity](../../research-integrity/SKILL.md) before submission.

## Keep the two deliverables consistent

Generate the numbers in the README and the report with the same scripts and
versions. Make product claims and paper claims agree. Bring work done for the
paper back into the product if it improves the product.
