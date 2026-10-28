# Prototype type guide

Classify the prototype purpose during triage. Emphasize the matching row inside the standard brief. Do not add headings. Do not design the interface.

| Prototype purpose | Brief emphasis |
|---|---|
| Communicate a concept | Core flow, key screens, primary message, stakeholder decision needed |
| Validate usability | Tasks, success/failure signals, states, feedback, navigation assumptions |
| Test feasibility | Data inputs, integrations, technical constraints, unknowns, smallest experiment |
| Align stakeholders | Scope boundaries, tradeoffs, approval criteria, explicit non-goals |

If they are not building a prototype, say so in Prototype question and follow the delivery context in `brief-template.md` (AI-agent build or research artifact).

## Communicate a concept

- Write the flow as the steps the user named, in order.
- List only screens or moments they named. If they named none, ask which moment the viewer must see. Do not invent a screen inventory.
- Primary message is one sentence the viewer should remember.
- The stakeholder decision is a yes/no or a choice between options they stated.
- Success looks like that decision getting made, not “people liked it.”

## Validate usability

The brief needs a prototype question, the task, a success signal, and a failure signal.

Prototype question form: “Can [specific person] complete [specific task] without [the help or error they named]?”

Include only the heuristics the task actually stresses. Turn them into checks, not a scorecard.

| Heuristic | Ask or check |
|---|---|
| Visibility of system status | What does the person see while an action is in progress, and immediately after it succeeds or fails? |
| Match between system and the real world | Which words must match the words they already use for this task? |
| User control and freedom | How do they undo, cancel, or leave without losing the place they were in? |
| Consistency and standards | Which existing flow, if they named one, must this match? |
| Error prevention | What mistaken action should be difficult, and what must not be destroyed? |

Navigation assumptions belong in Assumptions only after the user confirms them (for example, “Settings stays in the same place as today”). Unconfirmed navigation belongs in Open questions. Do not draw the navigation.

Worked requirement, after the user says they want to know whether people can find billing without being told:

- Prototype question: Can a first-time account owner open billing without asking for help?
- Success: they open the billing page from the starting screen on the first attempt.
- Failure: they open the wrong section, go back more than once, or ask where billing is.
- Check: the label they see uses the word “billing,” which is the word they use today.

## Test feasibility

- Name the data inputs and integrations the user said exist. Do not add systems.
- Put technical unknowns in Open questions.
- The build sequence is the smallest experiment that would answer the prototype question, plus a stop if a named unknown is still open.
- Success is whether the experiment answered the question, not whether a full feature shipped.

## Align stakeholders

- In scope and out of scope are the approval boundary.
- State the tradeoff they are actually choosing, in their words.
- Approval criteria are observable: what the approver will accept, and what they will reject.
- Non-goals are listed even when they are someone else’s idea that this round will not include.

## AI-agent handoff

Not a prototype type. Use it when delivery context is an AI-agent build.

- Ordered build steps.
- One or more acceptance criteria per story, including edge cases the user accepted.
- Open questions for anything the agent must not invent: files, schema, stack, visual design, copy, metrics, timelines.
- Step 1 does not require an unstated technical choice.

## Research or discovery artifact

- The prototype or artifact question is what someone must learn.
- Do not convert unknown user behavior into a requirement.
- Keep solution stories out until the problem is confirmed.
