# Introducing the Pipeline

After establishing the challenge, explain the paper's solution so the reader
can understand its central idea, how it addresses that challenge, and why it
matters. This is an introduction-level account; use
[Methods writing](method-writing.md) for the detailed method itself.

## Work out the story before drafting

Identify the challenge the pipeline addresses, the actual technical
contribution, and the underlying reason the approach can work. For an
established task, also identify the supported benefit relative to the relevant
prior approaches. For a new task, explain the value of the approach without
forcing a direct comparison when no appropriate comparator is available.

Distinguish **what is contributed**, **why it can work**, and **what advantages
follow**. Ground the account in the supplied material and flag essential gaps
instead of inventing a mechanism, observation, result, or comparative benefit.

## Common responsibilities

- Introduce the approach and its purpose, using its name if one exists.
  Connect it explicitly to the challenge.
- Explain the key idea in one or two clear sentences when feasible
  (**一两句话里介绍清楚我们的key idea**). Give enough context for the reader
  to understand the concept without jumping into unexplained terminology.
- Describe what the essential steps do and how they connect, even when the
  pipeline is simple. Make the relevant inputs, operations, and outputs clear
  when needed to understand the contribution. Do not substitute abstract
  insights or novel-sounding module names for the actual process. YU cautions
  against “把pipeline步骤讲得新奇.” Explain the intended advantage, while
  reserving detailed implementation for the Methods section.
- Separate a design rationale or anticipated advantage from a demonstrated
  experimental result. State comparisons and conditions only as supported.
- If an appropriate teaser exists, refer to its actual figure number and use
  it to illuminate the basic idea. When none is available, propose one if it
  would help and fits the task; do not invent a figure or cross-reference.

## Choose a presentation pattern

These patterns can overlap. Select and combine them according to the actual
contributions, rather than forcing the work into a fixed template.

### One contribution, multiple advantages

Introduce the method and key idea → explain the essential operation → explain
the distinct advantages and why they arise. One contribution may yield several
advantages; do not automatically present each as a separate contribution.

### Two related contributions

Introduce the overall method and its key idea → explain the first contribution
and its benefit → introduce the additional challenge → explain the second
contribution and how it addresses that challenge. Often the second component
addresses a difficulty introduced or exposed by the first; state that
dependency only when it is real. If the contributions are complementary but
independent, connect them honestly through their shared objective.

### A new module in an existing pipeline

Explain the established pipeline enough to locate the new module → identify
what the paper changes or adds → explain the module's mechanism and its
advantage in that pipeline. Credit the earlier method, distinguish reused
components from the paper's contribution, and support claimed comparisons
with relevant evidence.

### An observation motivates the contribution

State the key innovation → explain the accessible observation that motivated
it → show how the method realizes that insight → explain its supported
advantages. Make the connection from observation to design explicit and
distinguish an observed property from an untested interpretation.

For example, a closed contour has cyclic structure; a method can use circular
convolution to respect that structure when combining neighboring vertex
features. Explain any performance advantage using the evidence available for
the actual work.
