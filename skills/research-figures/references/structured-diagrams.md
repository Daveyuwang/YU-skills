# Structured Research Diagrams

Use this approach when the brief calls for a conventional, systematic, or
standardized diagram. A disciplined visual grammar is useful even when no
formal notation is required. Apply the shared figure and pipeline guidance
alongside it.

## Choose the representation

Identify the question the diagram answers and map the real entities,
relationships, sequence, and boundaries from the source. Choose the diagram
type accordingly: a flowchart for steps and decisions, a block diagram for
components and dependencies, a sequence diagram for time-ordered exchanges,
or a layered architecture for responsibilities and connections. Choose an
explicit notation such as UML, BPMN, or a domain-specific standard only if it
fits the content or is requested. Verify its actual symbol and connector rules
before claiming compliance; do not invent a hybrid and call it standard.

## Build a consistent visual grammar

- Give each recurring role a consistent shape, line treatment, and label style.
  Use distinct connector types for distinct relationships, with a legend when
  their meaning is not obvious. Do not imply direction, causality, sequence,
  or a decision that is absent from the source.
- Establish a clear reading direction, align related components to a grid, and
  use consistent spacing and component sizes where their roles are comparable.
  Let important modules have more room when needed. Route connectors to their
  actual endpoints and avoid unnecessary crossings and ambiguous junctions.
- Keep nesting, layer boundaries, and repeated elements consistent. Label
  branches and feedback locally. Compress repeated detail only when doing so
  preserves the scientific distinctions needed to understand the method.
- Prefer native shapes and editable text and connectors, or a reproducible
  diagram source that exports vector graphics. Choose the tool for the output
  and required control, for example a vector editor, PowerPoint, draw.io,
  Graphviz, Mermaid, or TikZ. Check that the delivered format retains the
  editability the user needs.

Render at final size and inspect both the visual grammar and the scientific
meaning. If a requested standard conflicts with a visual preference, follow the
standard and explain any necessary compromise.
