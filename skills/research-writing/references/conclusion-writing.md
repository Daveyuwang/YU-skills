# Conclusions, Limitations, and Future Work

Close with the problem, the paper's central contribution, and the significance
supported by its evidence. For a complete paper, include a concise account of
relevant limitations in the conclusion or in a separate section as the venue
and document require. Add a concrete future direction when it follows from the
work. For a narrow edit, keep to the user's requested scope.

## Identify a meaningful limitation

- Prefer a limitation grounded in the task goal, setting, or evaluated scope
  when it genuinely matters to the paper. Explain its practical consequence
  and, when appropriate, the opportunity it leaves for future work.
- Check what is established: a limited experimental range is not by itself
  proof that the method cannot operate beyond that range. Distinguish the
  intended setting, what was tested, and observed failure. For example,
  tests on 100–300-frame videos alone do not establish that longer videos are
  impossible to handle.
- A field-wide constraint shared by strong prior methods may be a meaningful
  boundary of the task rather than a regression unique to this method. Assess
  it against relevant comparable work instead of treating every boundary as
  a distinctive weakness.
- Report a material technical limitation or tradeoff when it affects the
  paper's claims, interpretation, or required reporting. Describe it precisely
  in context rather than using broad self-undermining language. Do not invent
  either a limitation or a reassuring comparison when evidence is missing.

## Assess metric tradeoffs in context

YU's preference is to strengthen a task-relevant metric without materially
degrading other central metrics when feasible. Compare the method with relevant
baselines using the task's customary evaluation measures and the paper's
actual goals. A tradeoff can be valuable under an appropriate constraint: for
example, lower memory use may be worth longer training in some settings.
Its importance depends on the magnitude, the intended use, and the evidence;
do not classify it as severe or negligible solely because a particular metric
is conventional or because a baseline is called state of the art.

## Keep future work distinct

A future direction is a possible extension; it is not automatically an
observed limitation. Connect one to a real boundary when the evidence supports
that link. Avoid an unrelated wish list, unsupported promises, or conclusions
that introduce new results.
