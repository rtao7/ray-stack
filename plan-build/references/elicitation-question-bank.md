# Elicitation question bank

Pick the next question by the **gap**, not by a fixed script. Ask one or two questions. Skip a question the user already answered. Use their words in the question when you can.

When that gap is still open, ask it in these words:

- “What do you think we should do?”
- “What are we deliberately not doing?”

If the user already answered the gap, do not ask it again. If the idea is fuzzy, stay on Problem and User. Do not jump to Handoff.

## Problem

Use when the need, the source, or the workaround is unclear. If they named a solution first, ask these before accepting the solution.

- What is happening today?
- What breaks, gets delayed, or frustrates someone, and who is that someone?
- Where did this request come from: you, a client, a PM or PRD, a complaint, a competitor, or a technical limit?
- What do people do now instead?
- What progress is the person trying to make, and what decision does this request support?
- If we ignored the feature you named, what would still be wrong?

## User

Use when “users” are unnamed, or when the buyer, approver, and daily user might differ.

- Who exactly experiences this problem?
- Who else is affected, and who has to approve the result?
- Is the person you are describing yourself, a customer, or someone you are guessing about?
- Who is explicitly not the user of this version?

## Outcome

Use when success is a slogan, a feature list, or missing.

- What must be true after this exists?
- How will we know it worked, in something a person could observe?
- What would count as a failure on the first try?
- What decision should a client or stakeholder be able to make after seeing this?
- What do you think we should do?

## Scope

Use when the request is a theme, a full PRD, or a growing feature list.

- What is the smallest version that would still be useful?
- Which part of this document should we focus on?
- What are we deliberately not doing?
- What should wait until a later version?
- What should an implementer refuse to add if it comes up mid-build?

## Constraints

Use when a limit is implied (“we already have…”, “legal said…”, “by Friday”) or when you are tempted to pick a stack, layout, or metric.

- What platforms, data, brand rules, deadlines, or integrations already apply?
- What did you already decide we must use or must not change?
- What limit is real, and what is a preference?
- Is there a deadline or budget you want in the brief, or should that stay unset?

Do not invent a limit to fill a quiet constraint. “None stated” is an acceptable answer after you ask.

## Prototype

Use when they mention a demo, prototype, test, or stakeholder review. Skip when they only want a written handoff and have said so.

- Should this communicate a concept, validate usability, test feasibility, or align stakeholders?
- What question should the prototype answer, in one sentence?
- What task will someone attempt, and what will you watch for?
- What would convince the approver to say yes, and what would be a no?

## Handoff

Use when the brief will go to a developer or an AI agent, including “build this with Cursor.”

- What must an implementing agent know before it edits anything?
- What may it not assume about the stack, the data, the files, or the design?
- Which edge cases have you actually decided, and which are still open?
- What is the first build step, and what should stop the agent until you answer?
