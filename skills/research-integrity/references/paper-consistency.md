# Manuscript Consistency

Check the claims and evidence relevant to the requested review. Give priority
to the abstract, introduction, conclusion, and other load-bearing statements,
then trace them to the corresponding text, tables, figures, or appendix.

## Claims and methods

- Compare the claim with the actual result and its setting: method variant,
  dataset and split, metric, baseline, aggregation, and conditions. Different
  labeled configurations or rounding may explain apparent discrepancies.
- Check that the method and assumptions being evaluated match what the paper
  claims. Inspect whether the evidence supports the stated scope and whether
  an ablation or proof actually distinguishes the claimed mechanism.
- Check figure and table captions against the displayed content, notation,
  axes, and sample descriptions. Inspect the rendered figure or page when
  extraction may have lost structure or mathematical symbols.

## Numerical and statistical interpretation

- Recompute important reported changes using the stated baseline and units.
  Distinguish a relative percentage change from a percentage-point difference,
  account for rounding, and check which direction of the metric is better.
- Check denominators, sample sets, aggregation, seed counts, and whether an
  uncertainty quantity is a standard deviation, standard error, or interval.
  An apparent mismatch may reflect a labeled subset or a different statistic.
- Apply integer-count or rounding feasibility checks only when the quantity is
  actually a proportion of known integer counts under the stated aggregation.
  Do not assume the same test applies to an unknown denominator, macro average,
  F1, or AUC; check the metric's definition before using any feasibility test.
- Overlapping error bars alone do not settle statistical significance. Use the
  relevant reported test or analysis and its assumptions; if information is
  missing, identify the uncertainty instead of declaring a statistical error.

## Citations and derivations

When a citation is important to the claim, verify the work's identity and
whether its content actually supports the cited proposition. Check definitions,
assumptions, and derivation steps for consequential theoretical claims. An
inaccessible source or extraction failure is an unresolved check, not proof of
an invented citation or invalid proof.
