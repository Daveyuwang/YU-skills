---
name: handoff
description: >-
  Write a portable Markdown brief from the current conversation so another
  session, agent, or teammate can continue the work. Use when the user asks
  for a handoff file or 交接文档.
---

# Handoff

Write one short Markdown file that a reader can use without access to this
conversation. Tailor it to the next session's purpose if the user specifies
one.

- State the goal, constraints, relevant decisions, and why they were made.
- Capture the work in progress, verified results, and important open questions
  or unverified assumptions. Give the next action and any blocker that affects it.
- Link to existing specs, architecture decisions, issues, commits, or diffs by
  path or URL. Include the working directory or revision if it is needed to
  resolve a reference. Check that the intended reader can access key material.
- Include a short **Suggested skills** section naming skills relevant to the
  next action.

Redact credentials, unnecessary personal information, and sensitive details
from the brief and its links. Save to the user's requested path, or create a
uniquely named file in the OS temporary directory outside the workspace.
Return the absolute path so the user can pass the file to the next reader.

Adapted from Matt Pocock's `mattpocock/skills`. [Upstream source](https://github.com/mattpocock/skills/blob/abeeaf95660ba9e8b7c753eb38f441ca707a8823/skills/productivity/handoff/SKILL.md) · [MIT license](LICENSE-Matt-Pocock.txt)
