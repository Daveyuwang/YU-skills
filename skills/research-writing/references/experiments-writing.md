# Experiments Writing and Organization

Treat experiments as evidence for the paper's contribution. Organize the
evaluation around the questions the paper needs to answer, and adapt the
depth to the task, available results, field, and venue.

## Plan the evidence

Consider three complementary questions:

1. **Comparison:** How does the method perform against relevant alternatives
   under the conditions that matter to its claimed contribution?
2. **Ablation:** What do the key contributions, modules, and design choices
   contribute, and under which conditions?
3. **Applications and demos:** Which meaningful or challenging cases reveal
   the method's capabilities and practical value?

Select the questions and experiments that fit the actual work; not every
paper needs all three forms. Distinguish experiments that have been completed
from proposed ones, and do not invent data, results, or claims.

## Comparisons

- Compare against strong, relevant methods, including suitable recent work and
  established baselines. Use a fair evaluation protocol and explain material
  differences in data, training, tuning, or computational resources.
- If there is no directly comparable baseline, consider defensible adaptations
  of related methods and informative variants or simplified versions of the
  proposed method. Explain what each comparison can establish. A comparison
  among the paper's own variants does not by itself establish superiority over
  external methods.
- Choose metrics and settings that reflect the actual contribution, and state
  results under their measured conditions rather than claiming blanket
  superiority.

## Ablations and sensitivity

- Test the core contributions and important components against the complete
  method. A central table, optionally paired with qualitative comparisons, can
  show their effects together.
- Follow with focused analyses of important module choices when useful: for
  example, a component's alternative designs, hyperparameter sensitivity, or
  sensitivity to input quality. Smaller tables or figures can make these
  results easy to read.
- Change the factor of interest while keeping the evaluation comparable where
  practical; document relevant changes and interpret interactions carefully.
  Use the number and form of analyses needed for the claims, not a fixed set
  of tables or figures.

## Applications and demonstrations

Choose meaningful applications or challenging cases that expose the method's
distinctive capabilities. Describe the input, conditions, and any selection
needed to interpret the example. Demos can show potential under those
conditions, but a few examples do not establish typical performance or a
formal upper bound. Connect the demo to the paper's main contribution.

## Results, captions, and layout

- In the main text, explain the result's significance and the evidence behind
  it. Keep claims aligned with the reported comparisons and conditions.
- Make each figure or table caption concise and interpretable: identify the
  experiment or setting, with relevant notation, variants, metrics, units, or
  visual markings explained in the caption or accompanying notes. Include a
  brief takeaway when useful; leave extended interpretation to the main text.
- In a two-column layout, YU prefers placing a single-column figure or table
  in the right column when practical, so text can begin at the upper left.
  Defer to the venue's format, figure readability, and placement near the
  relevant discussion; do not force a brittle layout.

For detailed table design, use [research tables](research-tables.md).

For examples of component and sensitivity ablations, see
[NeRF, Section 6.4](https://arxiv.org/pdf/2003.08934) and
[Learning Neural Volumetric Representations of Dynamic Humans in Minutes, Section 4.3](https://arxiv.org/pdf/2302.12237).
These illustrate possible organization; they are not required templates or
citations for unrelated work.
