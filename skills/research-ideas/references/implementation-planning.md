# Advancing a Chosen Research Direction

Treat the agreed idea, method, or story as the current working hypothesis.
Help make it concrete and rigorous; do not restart a general assessment of
whether it is worth doing merely because there is uncertainty or related work.
When project code and results are available, inspect the relevant parts before
proposing work. Identify what is already implemented or measured and build on
it instead of presenting completed work as a new proposal.

## Build a testable plan

1. Translate the central claim into the implementation and evidence it needs.
   Identify the core mechanism, important design choices, assumptions, and
   practical constraints.
2. Plan relevant baselines, ablations, and diagnostic experiments. Specify
   what observations would support the claimed effect and what would challenge
   the proposed explanation. Make comparisons and controls appropriate to the
   actual task and resources.
3. When difficulties arise, first consider adjustments that preserve the core
   idea. Explain the tradeoffs and the smallest useful test for each serious
   option. Distinguish a proposed experiment from a completed result.

## Separate three kinds of issue

- **Experimental uncertainty:** A question that needs measurement or a
  controlled comparison. Specify the test and how its outcomes inform the
  interpretation.
- **Implementation issue:** A difficulty that can plausibly be resolved by
  changing the design, engineering, or resources while retaining the core
  hypothesis. Explain the adjustment and its cost.
- **Core risk:** A concrete concern that could invalidate the central claim,
  such as substantive prior-work overlap or evidence against the mechanism.
  Give the evidence, a minimal decisive check where possible, and a repair path
  that preserves the idea if one exists.

Recommend reconsidering the direction only when key evidence actually makes
the core claim difficult to sustain, or when the user asks for reevaluation.
Do not hide contrary evidence or fabricate support to keep the story intact.
