# Methods Writing

Make the method understandable as a connected solution. The guiding idea is
**先给全貌，再讲细节**: give readers the overall picture before the details.
Adapt the guidance to the field, the material, and the requested scope.

## Plan a Methods section

1. Identify the method's modules or stages and how they relate. For each,
   work out its workflow, why it is needed, and why its design can work. A
   brief table or mind map can help distinguish these answers.
2. Sketch the pipeline, or use a suitable existing figure, as a planning aid.
   Show the inputs, outputs, components, and important flows between them,
   including branches or feedback when relevant. Organize subsections around
   the resulting conceptual or operational structure.
3. Plan each important module around its motivation, design, and technical
   advantage. Draft the **module design first** to establish the concrete
   process; then add the motivation and advantages. In the final prose, a
   useful order is motivation → design → advantage, adapted to the material.

For an excerpt or a narrow edit, reuse the available context and apply only
the relevant steps. Do not impose a new diagram, overview, or module structure
when the task does not call for one. When a figure is useful but does not yet
exist, a sketch can be a working aid or a proposal; do not invent a figure
number or imply that a finished figure already exists.

## Overview

A useful progression is: briefly state the setting and objective, including
inputs and outputs when relevant; summarize the core contribution; refer to a
suitable existing pipeline figure if available; then walk through the major
components and their corresponding subsections. The setting and contribution
can often each be explained in one or two sentences. Show how the components
connect rather than merely listing headings. Adapt the length and order to the
material, and use only actual figure and section numbers.

## Explain each important module

- **Motivation:** What problem or need makes the module useful? Explain its
  role in the pipeline and the specific difficulty it addresses. Use prior
  limitations when relevant and supported, rather than inventing a problem.
- **Design:** Describe the representations, data structures, network design,
  or other components that matter. Explain the operational flow: inputs →
  key operations and their connections → outputs. Include enough detail for
  understanding and, when required, reproduction.
- **Technical advantage:** Explain why the design can address the difficulty
  and what benefit it provides. Connect the mechanism to that benefit;
  distinguish an intended effect from an experimentally established result.

These elements can be integrated naturally rather than given fixed headings
or repeated mechanically for every routine step. Allocate detail to the
contribution-bearing choices; compress conventional material only when doing
so preserves accuracy and necessary reproducibility.

## Review clarity

- After drafting, extract the main point of each paragraph and read the
  sequence. Check that the section's logic, each paragraph's role, and the
  purpose of important steps are understandable. For a deeper review, use
  [flow review](flow-review.md).
- Use a consistent name for the same concept, and explain terminology changes
  when a genuine distinction is intended.
- Introduce notation when it does useful work, define necessary symbols at an
  appropriate point, and use them consistently. Prefer plain language when a
  symbol adds complexity without helping. Before removing or changing a
  symbol, check its use elsewhere and preserve the technical meaning.

If a rationale, implementation detail, or other information essential to the
requested task cannot be recovered from the material, flag the gap to the author
rather than creating it.
