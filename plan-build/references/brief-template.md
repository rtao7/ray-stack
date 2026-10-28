# Brief template

Use this structure for the confirmed brief only. The H1 is exactly `Ready-to-paste brief`. Fill every field from something the user said, or move the gap to Assumptions or Open questions. Never leave `TBD`, `TODO`, or bracket placeholders.

```md
# Ready-to-paste brief

## Context
- Request source:
- Primary user:
- Secondary users / approvers:
- Problem or opportunity:
- Current behavior / workaround:

## Desired outcome
- User outcome:
- Business or client outcome:
- Prototype question:
- Success looks like:

## Scope
- In scope:
- Out of scope:
- Future considerations:

## User stories
- As a [user], I want [goal] so that [benefit].

## Acceptance criteria
- Given [context], when [action], then [observable result].

## Constraints
- Technical:
- Design/brand:
- Data/privacy:
- Timeline/budget:
- Platform:

## Assumptions
- 

## Open questions
- 

## Build sequence
1. 
2. 
3. 
```

An unconfirmed draft uses the same sections under `# Draft brief (unconfirmed)`. Do not call a draft ready to paste.

## How to fill each section

**Context.** Name the source and the people. The problem is the stakeholder need (ISO/IEC/IEEE 29148), written without the proposed feature as the subject. Current behavior is the workaround they described. If they did not describe one, write that it was not stated and add an open question. Do not invent a persona.

**Desired outcome.** User outcome and business outcome are separate. Success looks like an observable event, not an adjective. Prototype question is the specific question a prototype must answer. If they are not prototyping, write “No prototype. This brief is for [the delivery context they stated].”

**Scope.** In scope is the smallest useful version they agreed to. Out of scope is only what they said they are not doing. Future considerations are real items they postponed, not a wishlist you created. All three are present even when the value is “None stated.”

**User stories.** One story per user goal. The “so that” clause is the benefit, not a repeat of the feature. Split stories that fail INVEST. Do not put unconfirmed edge behavior in a story.

**Acceptance criteria.** At least one Given/When/Then per story. Checklist bullets are only for rules and constraints. Each criterion names an observable result. Edge cases appear here only after the user accepts them.

**Constraints.** Five labels always appear. Use “None stated” when the user did not give one. A constraint is something they said limits the work. A preference you inferred is an assumption, not a constraint.

**Assumptions.** Statements you will treat as true only because the user confirmed them or explicitly allowed you to proceed. Prefix nothing as if it were a fact they never saw.

**Open questions.** Decisions the implementer must not make. File paths, schemas, visual design, metrics, timelines, and stack choices go here when the user did not provide them.

**Build sequence.** Ordered steps. Step 1 is the first action an implementer can take without inventing a missing decision. Later steps may say “stop until open question N is answered.” Do not add steps for work that is out of scope.

## When to expand or compress

Keep confirmed facts. Do not add sections. Depth changes inside the sections above.

| Delivery context | Expand | Compress |
|---|---|---|
| Concept demo | Desired outcome (primary message and the decision the viewer must make), Scope (the flow and the screens the user named) | Constraints, unless brand or channel was specified |
| Usability validation | Desired outcome (prototype question, task, success and failure), Acceptance criteria (states, feedback, wayfinding) | Business outcome, unless they named one |
| Feasibility test | Constraints, Open questions, Build sequence (smallest experiment and the inputs it needs) | Extra user stories beyond the experiment |
| Stakeholder alignment | Scope (boundaries, tradeoffs, what approval means), Out of scope | Implementation steps beyond what the approver must see |
| AI-agent build | Acceptance criteria (including accepted edge cases), Open questions, Build sequence | Vision and background the agent does not need |
| Research or discovery | Problem, Open questions, the prototype or artifact question | User stories that presume a solution |

For a developer or AI-agent handoff, map this template to IEEE 830 practice without renaming headings: Context is purpose, Scope is scope, stories and acceptance criteria are the functional requirements, Constraints and Assumptions stay explicit.

## Structural rules

- Keep the user’s terms for the product, the user, and the actions.
- Do not add requirements they did not confirm.
- Do not add a tech stack, data model, API, metric, or timeline they did not state.
- Every story in User stories has a matching observable criterion in Acceptance criteria.
- Step 1 of Build sequence is present and specific.
