# Example: vague self-generated idea

**Input:** “I want an app for tracking my plants.”

The skill does not brief this input. It stays in conversation until the gaps below are answered and the user confirms the reflection.

Questions it asks across turns, one or two at a time:

- Who is this for, and what goes wrong with the plants today?
- What is the one action this version must support, and what would you observe if it worked?
- What do you think we should do?
- What are we deliberately not doing?

**Confirmed in conversation, then briefed:**

- The user is the only person who waters about 15 houseplants at home.
- They forget which plants were watered and sometimes water everything so they will not underwater one.
- Today they use memory and a note that they stop updating.
- The useful action is a due list plus marking a plant watered.
- Success is a weekday morning where they water only the due plants and update the note’s replacement without opening a second app.
- They do not want photo identification, a social feed, shopping, care articles, or accounts for other people.
- No prototype. They want a brief before any build.
- No deadline, brand, or codebase was stated.

# Ready-to-paste brief

## Context
- Request source: Self-generated idea from the person who owns the plants.
- Primary user: The plant owner, who waters their own houseplants at home.
- Secondary users / approvers: None. No one else approves this version.
- Problem or opportunity: The owner cannot tell which plants were already watered, so some plants are watered again on days they are not due.
- Current behavior / workaround: The owner relies on memory and a note they stop updating.

## Desired outcome
- User outcome: On a watering day, the owner can see which plants are due and mark those they watered.
- Business or client outcome: None. This is for the owner’s own use.
- Prototype question: No prototype. This brief is for a later build decision.
- Success looks like: On a weekday morning, the owner waters the plants shown as due, marks each one watered, and does not open a second app to do either step.

## Scope
- In scope:
  - A list of the owner’s plants.
  - A way to see which of those plants are due today.
  - A way to mark a listed plant as watered today.
- Out of scope:
  - Identifying a plant from a photo.
  - A social feed, comments, or sharing.
  - Shopping for plants or supplies.
  - Care articles or advice content.
  - Accounts or profiles for anyone other than the owner.
- Future considerations:
  - Reminders, only if the owner later asks for them. They are not part of this version.

## User stories
- As the plant owner, I want to see which of my plants are due today so that I do not water plants that are not due.
- As the plant owner, I want to mark a due plant as watered today so that the list no longer tells me to water it.

## Acceptance criteria
- Given the owner has plants and opens the list on a watering day, when the list is shown, then each plant the owner still needs to water today is visibly grouped as due, and plants that are not due are not in that group.
- Given a plant is shown as due, when the owner marks it watered, then it is no longer shown as due and the list does not require a second app.
- Given the owner has no plants yet, when they open the list, then the list tells them there are no plants and does not show a due plant.

## Constraints
- Technical: None stated. Do not choose a stack, storage model, or framework.
- Design/brand: None stated. Do not invent a visual design.
- Data/privacy: The owner said the plants are their own household plants and no other person’s account is involved. No other privacy rule was stated.
- Timeline/budget: None stated.
- Platform: None stated. The owner said “app” and did not choose a platform.

## Assumptions
- “Due today” uses a watering interval and last-watered date the owner will supply per plant. The owner agreed this is the rule, and also agreed the specific interval values are entered by them rather than looked up from a plant database.
- A plant with no last-watered date is shown as due. The owner confirmed this.

## Open questions
- Which platform this should run on. Not chosen.
- Whether a plant that is due but skipped should stay due the next day. The owner has not decided.

## Build sequence
1. Confirm the platform open question with the owner. Do not pick a platform or a tech stack.
2. Let the owner add a plant with a name, a watering interval they enter, and an optional last-watered date.
3. Show which of those plants are due today using the confirmed due rule, and let the owner mark a plant watered today.
4. Check the acceptance criteria against an empty list, a plant with no last-watered date, and a plant that is not due.
