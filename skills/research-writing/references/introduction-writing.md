# Introduction Writing

Plan the introduction by working backward from the contribution, then write
the story forward: **倒推，然后正推**. This is a prewriting exercise; the
[reverse outline](flow-review.md) diagnoses an existing draft.

## Work backward

1. Identify the technical problem and why existing approaches do not provide
   a well-established solution in the relevant setting.
2. Identify the paper's actual contributions. Depending on the work, these may
   include a valuable task, evaluation metric, technical problem, or technique.
3. Explain their benefits and why they address the challenge. Identify the
   **new insight (新认知)** if the material supports one.
4. Determine which prior approaches and technical limitations will lead the
   reader to that challenge and insight. Establish the logic before drafting.

For an existing task, begin with the challenge the paper addresses; identify a
relevant prior approach that encounters it, and, when helpful, trace which
earlier limitations motivated that approach. Include only the links needed to
make the challenge understandable. For a new task, establish its actual
setting and challenge without inventing a history of prior methods.

When developing the technical-challenge and prior-work discussion, use
[technical challenge storylines](technical-challenge-storylines.md) to choose
among an established task, an established insight, and a new task or setting.
When introducing the paper's own approach and contributions, use
[introducing the pipeline](pipeline-introduction.md).

## Tell the story forward

A common progression is task and application → relevant previous approaches →
their limitations and technical causes → the paper's approach and
contributions → their advantages and insight → representative evidence and,
where appropriate, a concise contribution summary. Adapt the order and detail
to the paper and venue.

Choose the opening based on what the audience knows:

- For an unfamiliar task, explain the task, then motivate its applications.
- For a familiar task, begin with the relevant application or context.
- For a new setting of a familiar task, YU prefers introducing the broader
  application first and then specifying the setting.
- When the context makes it natural, introduce a relevant prior approach and
  the challenge in the first paragraph. YU prefers this early clarity when it
  works, though the opportunity is relatively uncommon. More often, develop
  enough prior-method context first; it may take several paragraphs before
  the reader can appreciate the challenge.

Use only as much prior-work context as the reader needs before the
contribution; the challenge storylines give more detailed options.

## Frame the challenge and contribution

- Explain both the observable limitation and its technical reason, focusing on
  the challenge the paper actually solves. Help the reader see why the
  solution is worth seeking and how the paper's insight motivates it.
- Do not lead with a deliberately naive solution and then narrate the paper as
  a sequence of small patches to it
  (**不要先写一个naive solution，然后再写我们对这个naive solution的改进**).
  Present the actual central idea and its value directly. Accurately represent
  the relationship to prior work and the contribution's true degree of
  novelty, including when it is incremental.
- Support statements about prior methods and their limitations with the
  available sources; do not invent citations or imply that a limitation is
  universal when it applies only in a particular setting. Flag unresolved
  factual gaps to the author.
