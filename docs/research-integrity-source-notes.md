# Research Integrity: Source Notes

Source: YU's `anti-autoresearch.md` summary and the original
[Anti-Autoresearch project](https://github.com/wanshuiyin/Anti-Autoresearch),
distributed under the MIT license. Its notice is included with the
[research-integrity skill](../skills/research-integrity/LICENSE-Anti-Autoresearch.txt).

The skill retains the useful distinctions between manuscript-level checks,
source-level locations, and checks requiring experimental artifacts; it requires
grounded findings and does not infer intent or authorship. A finding is assessed
in its actual context, including plausible alternative explanations.

The upstream project contains a much larger taxonomy, ledger, automated
adjudicator, and multi-agent workflow. They are not automatically installed or
required by this adaptation. The case-specific examples in YU's source are
prompts for possible checks, not findings about any paper. The ordinary
research-writing skill keeps its own lightweight claim–evidence check.

Two false-positive boundaries are particularly useful. Integer-count checks
need a suitable quantity, known denominator, and the stated rounding; the
[GRIM study](https://research.rug.nl/en/publications/the-grim-test-a-simple-technique-detects-numerous-anomalies-in-th/)
illustrates the importance of granularity assumptions for integer means. Error
bar overlap alone does not settle significance, as discussed by
[Cumming and Finch](https://pubmed.ncbi.nlm.nih.gov/15740449/). Artifact
matching is not equivalent to reproducing an experiment.
