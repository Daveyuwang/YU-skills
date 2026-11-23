---
name: grill-me
description: >-
  Interview the user to sharpen a plan, idea, or design. Use when the user asks
  for a design interview or says "grill me", "grill with docs", or 追问我的方案.
---

# Grill Me

Keep the interview and recap in chat by default. Use the documentation
workflow below when the user asks to grill with docs or to record the
interview's decisions.

## Run the interview

Map the plan as a tree of decisions. Settle the choices that constrain other
choices first. Focus on decisions that can change the outcome.

1. Look up facts in the available code, documents, data, or sources. Ask the
   user to make choices and supply information you cannot determine from
   those materials. Surface conflicts that affect a decision.
2. Ask a numbered round of questions whose prerequisites are settled. Give
   your recommended answer and the reason for it under each question. Phrase
   the question so a simple agreement accepts the recommendation when
   practical. Ask one question per round if the user prefers it.
3. Wait for the answers and build the next round from the choices they
   unblock. Continue with independent questions while a prerequisite is open.

Close when the consequential choices are settled or explicitly deferred.
Recap the design, the open decisions, and any documentation updates. Wait
for the user to confirm the recap before implementation.

## Record project decisions

Read the relevant code, glossary, and architecture decision records (ADRs).
Use `GLOSSARY-MAP.md` to locate the relevant domain context if the project
has a map. Check any conflicting description against the code and ask the
user which behavior should guide the design.

Use concrete scenarios to test the boundary between concepts. Propose a
canonical term for any overloaded language and confirm it with the user.
Record agreed terms with a short definition and any aliases to avoid. Use
the project's existing glossary or create a root `GLOSSARY.md` when the
first entry is ready.

Offer an ADR when a decision is costly to reverse, would surprise a future
reader without its rationale, and involves a real trade-off. Record the
context, decision, and reason once the user agrees. Use the project's existing
location and format. Otherwise, create a numbered file such as
`docs/adr/0001-order-cancellation.md` when the first ADR is needed.

Adapted from Matt Pocock's `mattpocock/skills`. [Grill me](https://github.com/mattpocock/skills/blob/abeeaf95660ba9e8b7c753eb38f441ca707a8823/skills/productivity/grill-me/SKILL.md) · [Grill with docs](https://github.com/mattpocock/skills/blob/abeeaf95660ba9e8b7c753eb38f441ca707a8823/skills/engineering/grill-with-docs/SKILL.md) · [Grilling](https://github.com/mattpocock/skills/blob/abeeaf95660ba9e8b7c753eb38f441ca707a8823/skills/productivity/grilling/SKILL.md) · [Domain modeling](https://github.com/mattpocock/skills/blob/abeeaf95660ba9e8b7c753eb38f441ca707a8823/skills/engineering/domain-modeling/SKILL.md) · [MIT license](LICENSE-Matt-Pocock.txt)
