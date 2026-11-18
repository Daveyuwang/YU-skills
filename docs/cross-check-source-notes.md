# Cross-check: Source Notes

Source: YU's request in a Claude Code conversation (2026-11-17). The
[cross-check skill](../skills/cross-check/SKILL.md) turns it into a two-way
handoff between Claude Code and Codex with a written brief, a read-only peer,
recorded model identity, and verification of the reply before it reaches YU.

> 我想连通codex 做adversarial check这样的工作流，并让handoff内容准确，从而能够进行符合预期的adversarial check，最终获得insights and feedback. and vice versa, codex -> claude code (the former will be claude -> codex)
>
> and we need to select the model, by default, using the latest most powerful models.
> for codex (chatgpt), current we will use GPT-6.2 Astra (max reasoning effort)
> for Claude, we will use Fable-5.2 (extra-high / xhigh).
>
> for sure, the models could be changed. and the agent (codex/claude code) should take the user request (the agent doesn't need to proactively ask for model choice), when model is specified, change and confirm it.

> all ARIS review plugins are one of the main use cases for this kind of dual-model/agent (two different most powerful models). but not limited to it. we should write a skill and let the agent know to generalize (or the skill itself in natural generalizes to other similar use cases)
>
> write concise, clear and useful skill as specified to let the agent do expected behavior and meet our requirements.

Decisions made while building it:

- "Confirm" means reporting the model the peer actually served, read from the
  peer's own records, not the requested name. Codex records the model and
  effort of each turn. Claude Code reports the models it used but not the
  effort.
- Codex models also offer `ultra`, one level above `max`. The default follows
  YU's `max`. ARIS deep audits that ask for `ultra` keep it.
- In Codex, ARIS's default reviewer is a native Codex subagent, which is the
  same model family. The skill routes those reviews to Claude instead.
- The Claude peer gets only Read, Grep, and Glob with no MCP servers. The
  Codex peer runs its commands in the read-only sandbox but keeps the MCP
  servers its configuration enables: a config override can disable servers
  defined in `config.toml` but not those that plugins provide. In a test
  (2026-11-17), a read-only Codex peer could call `node_repl` but declined a
  requested file write, citing the read-only policy. Whether `node_repl`
  itself enforces the sandbox was not tested.
