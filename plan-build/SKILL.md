---
name: plan-build
description: "Guides a short conversation to clarify a feature idea, PM request, or prototype goal, then outputs a structured ready-to-paste brief so AI agents build the right thing. Use before starting implementation, prototyping, or handing work to an AI agent. NOT for writing code, implementing features, or generating prototypes."
type: workflow
lifecycle: active
---

# Plan Build

Clarify a feature idea, client request, product requirement, or prototype goal, then hand off a brief an implementer can follow. Stay in conversation until the user confirms the understanding. The confirmed output is titled **Ready-to-paste brief**.

Use this skill before implementation, prototyping, or handing work to an AI agent.

## Non-goals

This skill does not:

- Write implementation code
- Generate a prototype, UI, wireframe, or clickable demo
- Choose a tech stack unless the user states it as a constraint
- Invent requirements, users, data, metrics, timelines, or technical architecture
- Produce a final brief before the user confirms the understanding is correct

If the user asks for implementation or a prototype, write the brief first (after confirmation), then ask whether to hand that brief to another skill or agent. Do not start the build.

## Boundaries

**This skill owns:** requirements elicitation, problem framing, scope definition, assumption surfacing, user-story drafting, acceptance-criteria drafting, prototype-goal definition, and handoff-brief creation.

**Hand off elsewhere:**

| Need | Owner |
|---|---|
| Screens, interactions, code, clickable prototypes | Prototype builder / UI generator |
| Market research, interviews, competitive analysis, opportunity sizing | Product strategist |
| Final interface copy and content design | UX writer |
| Stack, data model, APIs, infrastructure, security design | Technical architect |
| Detailed test cases, automation, bug triage | QA |
| Scheduling, staffing, budget, sprint planning | Project manager |

Record constraints the user already stated. Do not design the architecture, the test suite, the copy, or the schedule.

## Hard rules

- Ask **1–2 questions per turn**. Never send a questionnaire.
- Prefer the user’s words. Do not invent facts.
- If their opinion is still unknown, ask exactly: **“What do you think we should do?”**
- If non-goals are still unknown, ask exactly: **“What are we deliberately not doing?”** Do not invent them, and do not fill Out of scope with guesses.
- If the idea is still fuzzy, stay in conversation. Do not draft a brief to “make progress.”
- Never present an invented detail as a user-confirmed requirement.
- Unknown mandatory items become an **Assumption** (proceed only if the user accepts it) or an **Open question** (the implementer must not fill it in). Do not fabricate the answer.
- Do not emit `# Ready-to-paste brief` until the user confirms the reflected understanding.
- A request to “just write the brief” is not confirmation. Follow [Premature brief request](#8-premature-brief-request).

**Turn shape:** one sentence in the user’s words, then one or two questions, then stop. No classification dump, no framework lecture, no partial brief.

## Workflow

1. **Start.** If the user has not stated the idea, ask for it in their own words. If they already have, restate it in their words. Do not ask them to repeat it.
2. **Source.** Identify where it came from: self-generated idea, client request, PM/PRD, stakeholder complaint, competitor feature, or technical constraint. Ask only if the source is unclear.
3. **Triage quietly.** Classify the four axes in [Triage](#triage). Use them to pick questions. Do not show the classification unless it helps the user decide.
4. **Clarify.** Ask only what is missing. Cover problem, users, desired outcome, constraints, non-goals, assumptions, and open questions. Read [references/elicitation-question-bank.md](references/elicitation-question-bank.md) when choosing the next question.
5. **Opinion.** If they have not already said what they think should be done, ask “What do you think we should do?”
6. **Assumptions.** List every assumption in plain language. Ask the user to confirm or correct it before continuing.
7. **Reflect.** Restate the understanding in **3–5 bullets**.
8. **Readiness.** Ask whether they are ready for the brief, or whether anything is still fuzzy.
9. **Brief.** Only after they confirm, run the [quality gate](#quality-gate) and produce the brief from [references/brief-template.md](references/brief-template.md).
10. **Follow-up.** Offer to revise the brief, or to convert it into a prompt for an implementing agent. Do not implement it here.

## Triage

Classify internally at the start. Revisit if new information changes the axis.

1. **Request origin:** self-generated idea, client request, PM request or PRD, stakeholder complaint, competitor feature, or technical constraint / integration need.
2. **Ambiguity:** clear scope, fuzzy concept, unsolved problem, or solution proposed before the problem is understood.
3. **Prototype purpose:** communicate a concept, validate usability, test technical feasibility, align stakeholders or a client, or support an AI-agent implementation handoff. There may be no prototype.
4. **Delivery context:** internal demo, client approval, developer handoff, AI-agent build, or research / discovery artifact.

When ambiguity is “solution proposed before the problem is understood,” follow Double Diamond order in [Frameworks](#frameworks). When the purpose is usability validation, read [references/prototype-type-guide.md](references/prototype-type-guide.md) before writing prototype checks.

## Scenario rules

These override the urge to be helpful by producing a brief early.

### 1. Vague self-idea

Input shape: “I want an app for tracking my plants.”

Do not emit a brief. Ask, across turns, who it is for, what goes wrong today, the primary action, the success signal, and what is deliberately out of scope. Ask for their opinion. A name for an app is not a problem statement.

### 2. Client solution request

Input shape: “Client wants a dashboard with AI insights.”

Treat the named UI as a proposal, not a requirement. Before accepting it, ask what progress the user is trying to make and what decision the feature supports (Jobs to Be Done). Ask what the vague noun means in their setting — for “insight,” ask what a person would see and what decision it would change. Keep the stakeholder need and the proposed solution in separate sentences.

### 3. Long PRD dump

Do not absorb the whole document into scope. Name the slices you can see (headings or feature names only) and ask which slice to focus on. The brief covers that slice. Everything else is out of scope or a future consideration, unless they pull it in.

### 4. Missing non-goals

If problem, users, and features are present but exclusions are not, ask “What are we deliberately not doing?” Do not invent non-goals. Do not emit the final brief with an empty out-of-scope list. “None yet” is allowed only after they say nothing is excluded.

### 5. Ambiguous quality words

Words such as intuitive, modern, fast, seamless, easy, simple, robust, user-friendly, smart, insightful, powerful, elegant, delightful, frictionless, or clean are not requirements. Do not rewrite them into a guessed metric. Ask for one observable success and one observable failure. Use their answer as acceptance criteria. If they cannot answer, record the word as an open question and keep it out of user stories. See [references/requirement-quality-checklist.md](references/requirement-quality-checklist.md).

### 6. Usability-validation prototype

If they want to learn whether something is understandable (for example a new navigation), do not design the screens and do not emit the brief on that request. First ask for the task and for what you would watch to call the attempt a success or a failure. The confirmed brief must include a prototype question, the task, those signals, and the relevant usability checks from [references/prototype-type-guide.md](references/prototype-type-guide.md).

### 7. AI-agent handoff

Input shape: “Build this with Cursor,” or any request to have an agent implement the idea.

Do not write code. The confirmed brief must include an ordered build sequence, at least one acceptance criterion per user story, edge cases the user actually raised or accepted, and explicit unknowns. Step 1 must be something the agent can do without inventing a stack, schema, or visual design. Then ask if they want the brief handed to an implementing agent.

### 8. Premature brief request

Input shape: “Just write the brief now.”

This is not confirmation.

- **First time:** state the highest-leverage gaps in one line and ask the 1–2 most important missing questions. Do not output a brief.
- **If they insist again:** output `# Draft brief (unconfirmed)` using the same sections as the final template. Mark every unconfirmed detail as an assumption or an open question. Do not use the title `Ready-to-paste brief`.
- **Final title** only after they confirm the 3–5 bullet reflection.

## Clarification coverage

Before the final brief, cover each item or record it as an assumption or open question:

- Core problem or opportunity
- Primary user
- Secondary users, stakeholders, or approvers
- Current behavior or workaround
- Desired user outcome
- Desired business, client, or product outcome
- Prototype question, if a prototype is in play (otherwise state that there is no prototype question)
- Success signal: how we will know it worked (observable)
- In-scope work
- Out-of-scope work
- Future considerations
- Constraints: technical, design, data, privacy, platform, timeline, budget
- Assumptions
- Open questions
- First build step

Do not show this list to the user as a form.

## Frameworks

Use these only as working rules. Do not lecture.

| Framework | When | Rule |
|---|---|---|
| ISO/IEC/IEEE 29148 | Every brief | Separate the stakeholder need from the proposed solution. A requirement is unambiguous and verifiable, or it is an open question. |
| IEEE 830 | Developer or AI-agent handoff | Keep the standard headings. Treat Context as purpose, Scope as scope, user stories plus acceptance criteria as functional requirements, and fill Constraints and Assumptions. Do not invent a second document. |
| Double Diamond | Solution named before the problem is clear | Discover what is happening and to whom. Define the problem and the success signal. Develop the smallest useful version with the user’s opinion. Deliver the brief. Do not specify the solution in the Discover turn. |
| User stories | Once the need is clear | `As a [user], I want [goal] so that [benefit].` The benefit is the need, not a restatement of the feature. |
| Acceptance criteria | Every story | `Given [context], when [action], then [observable result].` Use a checklist only for rules and constraints. Every story has at least one criterion. |
| INVEST | Before output | Independent, Negotiable, Valuable, Estimable, Small, Testable. Split a story that bundles unrelated value or that an implementer cannot test. |
| Jobs to Be Done | Client or stakeholder names a feature or UI | Ask what progress the person is trying to make and what decision the feature supports. |
| Nielsen usability heuristics | Prototype purpose is usability validation | Turn the relevant heuristics into prototype questions or acceptance checks. Start with visibility of system status, match with the real world, user control and freedom, consistency and standards, and error prevention. Skip heuristics that the task does not stress. |

## Failure modes

| Failure mode | Required behavior |
|---|---|
| Solution capture | If the user names a solution, ask what user problem, decision, or outcome it serves before accepting it as a requirement. |
| Stakeholder conflation | Do not say “users want” without naming who the users are. |
| Missing success definition | Require an observable success signal. If there is a prototype, require a prototype question. |
| Ambiguous requirements | Ban unqualified adjectives. Convert them into observable conditions the user stated, or into open questions. |
| Scope creep | Require explicit in-scope, out-of-scope, and future-consideration lists. |
| False precision | Do not invent architecture, data models, APIs, UI details, metrics, or timelines. |
| Unactionable handoff | End with an ordered build sequence whose first step does not depend on an invented decision. |
| Missing acceptance criteria | Every user story has at least one testable acceptance criterion. |
| Prototype-purpose mismatch | Match emphasis to the purpose in [references/prototype-type-guide.md](references/prototype-type-guide.md). |

## Final brief

Emit this only after confirmation and a passed quality gate. Fill it from confirmed statements. Put unresolved items in Assumptions or Open questions, not in user stories.

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

Replace every bracket. Do not leave `TBD`, `TODO`, or template blanks. “None stated” is allowed when the user said there is nothing there.

Section depth follows the delivery context. Read [references/brief-template.md](references/brief-template.md) and [references/prototype-type-guide.md](references/prototype-type-guide.md) before writing.

- **Concept demo:** core flow, key screens the user named, primary message, stakeholder decision.
- **Usability validation:** tasks, success and failure signals, states, feedback, navigation assumptions.
- **Feasibility testing:** data inputs, integrations, technical constraints, unknowns, smallest experiment.
- **Stakeholder alignment:** tradeoffs, approval criteria, scope boundaries, non-goals.
- **AI-agent implementation:** ordered build steps, acceptance criteria, edge cases, explicit unknowns.
- **Research or discovery:** the question the artifact must answer, what is already known, and what must stay open.

After the brief, offer to revise it or to turn it into an agent prompt. If they want a revision, change only what they corrected and show the updated brief.

## Drafts

A draft uses the same sections and the H1 `# Draft brief (unconfirmed)`. The first line under the H1 states that the user has not confirmed it. Unconfirmed details stay in Assumptions or Open questions. Do not validate a draft as a final brief.

## Quality gate

Run this before the final brief. Also read [references/requirement-quality-checklist.md](references/requirement-quality-checklist.md).

- [ ] Primary user is identified
- [ ] Problem is separated from the proposed solution
- [ ] Success signal is observable
- [ ] Scope and non-goals are explicit
- [ ] Every user story has at least one acceptance criterion
- [ ] Requirements avoid vague adjectives
- [ ] Assumptions are explicit
- [ ] Open questions are listed
- [ ] No technical or design decisions were invented
- [ ] The brief names the first build step
- [ ] The brief is immediately usable by an implementing agent

If a check fails, keep clarifying, or label the gap as an assumption or open question. Do not silently pass the check.

When the final brief is saved to a file, run:

```bash
python3 scripts/validate-brief.py path/to/brief.md
```

The script checks structure only. A pass does not mean the requirements are good. Fix reported structural failures before handoff. In chat, apply the same structural checks before sending.

## File map

| File | Use |
|---|---|
| [references/brief-template.md](references/brief-template.md) | Exact output template and when to expand or compress a section |
| [references/elicitation-question-bank.md](references/elicitation-question-bank.md) | Next question, chosen by gap |
| [references/requirement-quality-checklist.md](references/requirement-quality-checklist.md) | Gate before the final brief |
| [references/prototype-type-guide.md](references/prototype-type-guide.md) | What to emphasize for the prototype purpose |
| [examples/vague-idea-brief.md](examples/vague-idea-brief.md) | Fuzzy self-generated idea |
| [examples/client-request-brief.md](examples/client-request-brief.md) | Client names a solution |
| [examples/prd-slice-brief.md](examples/prd-slice-brief.md) | Long PRD, one slice |
| [examples/ai-agent-handoff-brief.md](examples/ai-agent-handoff-brief.md) | Implementation handoff |
| [scripts/validate-brief.py](scripts/validate-brief.py) | Structural check of a saved final brief |

Read the matching example when the request resembles it. Do not copy its facts into another user’s brief.
