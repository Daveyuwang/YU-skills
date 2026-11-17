# Brief Template

Copy the block below into `brief.md` and fill each section. Delete a section
only when it does not apply. The script adds the reviewer rules on top, so the
brief holds only the task.

```markdown
# Cross-check: <one-line subject>

## Decision
<What YU or the author will do next, and how each outcome would change it.>

## Request
> "<YU's words, verbatim>" (YU, YYYY-MM-DD)

<Only the context needed to read the quote. Mark any paraphrase as yours.>

## Materials
Working directory: <absolute path>
- Under review: <paths, `git diff <base>..<head> -- <paths>`, document sections>
- Reference: <specs, data, logs, earlier results, saved copies of pages>
- To reproduce: <commands and the files they produce>

## Claims to attack
1. <Claim as the author states it.> Rests on: <path:line, command, or table>.
2. <...>

## Settled (do not reargue)
- <Decision> (source: <quote and date, or spec path>). Flag only a factual error.

## Known open issues
- <Issue already tracked, so effort goes elsewhere.>

## Out of scope
- <...>

## Return format
1. One line per claim: holds, fails, or partly holds, with the deciding evidence.
2. Findings, most severe first. For each: location, what fails with a concrete
   case (input or state, then the wrong result), evidence marked verified or
   inferred, severity (changes the decision, should fix, or minor), and the fix
   or test that would settle it.
3. The strongest objection to the overall approach, if any, and the evidence
   that would change your mind.
4. Insights that are not defects: a better framing, a missed alternative, a
   simpler route.
5. What you could not check, and why.
6. Gaps in this brief that limited the check.
```

## Notes

- Drop "Known open issues" when the check should show whether the peer finds
  an issue on its own.
- For a review skill with its own output schema, such as an ARIS verdict or
  score, keep that schema unchanged and fill the other sections only where the
  skill leaves room.
- For a follow-up round, send only what changed: the disputed findings, your
  evidence, and what you want decided.
