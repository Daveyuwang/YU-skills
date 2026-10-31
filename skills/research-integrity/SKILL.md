---
name: research-integrity
description: >-
  Audit a paper's consistency and evidence when an integrity check or concrete
  concern warrants it. Use for 论文诚信核查、数据一致性 and 证据审计; not for
  routine writing edits.
---

# Research Integrity Review

Examine whether the paper's claims, methods, results, and citations agree with
the evidence available. This is a focused review for the user or a human
reviewer, not a verdict on intent, misconduct, or whether AI wrote the paper.
Use it when an integrity review is requested or a concrete evidence concern
calls for one; do not turn ordinary writing or idea development into an
automatic, heavyweight audit.

## Set the evidence scope

- **Manuscript only:** Check internal consistency, reported arithmetic,
  citations where accessible, and whether claims match the described evidence.
  The paper alone cannot establish that its data or results are genuine or
  reveal how its code actually behaved.
- **Manuscript and source:** Source files can provide precise locations for
  equations, tables, and references, but do not by themselves establish the
  underlying experimental facts.
- **Code, data, or result artifacts also available:** Check the relevant
  claims against accessible configurations, evaluation logic, data provenance,
  and result files. Matching artifacts is not a reproduction. Claim
  reproduction only if the relevant work was actually run and checked.

State what was examined and what remains unavailable. Missing access does not
prove a missing artifact, a failed experiment, or misconduct.

## Review proportionately

Start with the central claims and the uncertainties that matter for the task.
For manuscript-level checks, use [paper consistency](references/paper-consistency.md).
For evaluation design or artifact checks, use
[experimental evidence](references/experimental-evidence.md). Read only what
is relevant and available; do not build a ledger, hashing system, multi-agent
workflow, or scoring apparatus merely because the source project uses one.

Check the source passages, tables, figures, citations, or artifacts directly.
Where PDF extraction is uncertain, inspect the relevant rendered page before
asserting a mismatch. Run a calculation or check when it can resolve a real
uncertainty; do not imply that experiments were rerun when they were not.

## Report grounded findings

For each material finding, identify the claim and the evidence with precise
locations, explain the mismatch and its significance, and state any plausible
alternative explanation or missing information. A serious contradiction needs
an anchored claim and the evidence that conflicts with it; an unverified
suspicion is not the same as a finding.

Distinguish observations from inferences. If no material issue is found, say
so for the material actually checked rather than certifying the whole paper.
Do not treat writing style or a surface resemblance to a known pattern as
evidence of authorship, intent, or misconduct.

Adapted from [Anti-Autoresearch](https://github.com/wanshuiyin/Anti-Autoresearch);
its MIT notice is in [LICENSE-Anti-Autoresearch.txt](LICENSE-Anti-Autoresearch.txt).
