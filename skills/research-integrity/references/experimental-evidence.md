# Evaluation and Artifact Evidence

Use the paper's reported setup to identify relevant questions; use accessible
code, data, configurations, and outputs to verify what actually ran where
possible. Do not infer artifact-level behavior solely from the manuscript.

- **Comparisons:** Check whether important baselines, metrics, and conditions
  support the reported comparison. Account for meaningful differences in
  training data, tuning, compute, or model variants and for justified limits
  on baseline availability.
- **Ablations and reporting:** Check whether a claimed component effect is
  isolated by the comparison and whether reported datasets, metrics, seeds,
  and settings correspond to the claims. A labeled pilot, best configuration,
  or expanded appendix run is not automatically a contradiction.
- **Data and evaluation:** Where relevant evidence is available, inspect
  ground-truth provenance, train/test separation, preprocessing, metric
  computation, and whether model-generated or proxy labels are identified
  accurately. Agreement between raters does not by itself establish label
  accuracy, and a simulated evaluation does not by itself establish real-user
  performance. Do not equate an unreported detail with proof that it was absent.
- **LLM-based judging:** If a central evaluation relies on a model judge, check
  the documented judge, its relationship to the evaluated models, and relevant
  validation or bias controls. A shared model family or an unreported check
  alone does not prove a biased result.
- **Artifact correspondence:** Compare reported values with the relevant
  result files, metric keys, configurations, and code paths when available.
  A file not supplied to the review is unavailable; it is not automatically a
  nonexistent or fabricated result.

Clearly distinguish a paper-level concern, an artifact-level discrepancy, and
an experiment actually reproduced. Run additional checks when they can resolve
a material uncertainty and fit the task's scope and available resources.
