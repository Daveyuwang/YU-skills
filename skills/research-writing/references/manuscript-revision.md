# Whole-Paper Revision

Use a question-driven self-review to improve the paper, not merely to list
possible objections. Apply this workflow to substantive revision of a full
manuscript; for an excerpt or a narrow edit, adapt only the relevant questions.

## Working process

1. Read the manuscript and available evidence. Identify the central claims,
   contributions, and the scope of the material that can actually be checked.
2. Write a tailored self-review question list covering the five groups below.
   For an editable working manuscript, append it as a clearly marked temporary
   section at the end of the paper. Keep a LaTeX document structurally valid;
   if there is an `\end{document}`, place the section before it.
3. Use the questions to prioritize and make the requested revisions. Resolve
   what the supplied material supports; identify missing evidence, proposed
   experiments, or design issues that prose alone cannot fix. Do not invent
   results or treat an unanswered question as an established flaw.
4. Revisit the questions and tell the author about consequential unresolved
   issues. Keep the working list out of a clean submission-ready deliverable
   if one is requested, while preserving it separately when appropriate.

If the user requests review only or does not want embedded notes, present the
questions and findings separately without editing the manuscript. Do not claim
to review material that was not supplied.

## Five question groups

### 1. Contribution and insight

What new knowledge, capability, or meaningful contribution does the reader
gain? Are the approach and its likely improvement already well explored or
predictable from closely related work? If the method is straightforward,
what supported insight, setting, or practical value makes it worth reporting?
An often-encountered failure case can itself be important; assess the novelty
and value of the explanation or solution, not the rarity of the failure.

### 2. Clarity and reproducibility

Can the intended reader understand and reproduce the relevant method and
experiments from the supplied details? Are the roles, motivations, and
connections of important modules clear? Identify missing technical information
instead of guessing it.

### 3. Strength of results

Are the improvements meaningful for the paper's goal and supported relative
to appropriate baselines and variability? Even when a method performs better,
are its absolute results adequate for the intended use? Consider the relevant
setting and tradeoffs; a small numerical gain is not automatically unimportant.
Trace the claims, especially in the abstract and introduction, to the results
and conditions that support them; use [claim–evidence checks](claim-evidence.md)
for the detailed process.

### 4. Completeness of evaluation

Are important baselines, ablations, evaluation metrics, or sufficiently
challenging data missing? Do the experiments support the core claims and
isolate the contributions or design choices they are meant to test? Separate
analyses already completed from those that would need to be performed; use
[experiments writing](experiments-writing.md) for the detailed guidance.

### 5. Method and experimental design

Are the setting and assumptions realistic for the intended application? Are
the proposed mechanisms technically coherent, and is the method robust rather
than dependent on unexplained per-scene tuning? Do new costs or limitations
materially offset the claimed benefits under the stated conditions? Assess
these questions against the available evidence and relevant constraints.
