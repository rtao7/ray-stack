# Example: handoff to an implementing agent

**Input:** “Build this with Cursor.”

The skill does not write code. It produces this brief only after the conversation below, then asks whether to hand the brief to an implementing agent.

**Confirmed before the brief:**

- The existing app already stores plants with `name`, `lastWatered` (the user said this is a calendar date), and `intervalDays` (a whole number the owner typed).
- There is already a plant list. The user forbade a redesign, a new backend, and accounts.
- “Today” means the calendar date on the device running the app.
- A plant with no `lastWatered` is due. The owner marks watered from the list, which sets `lastWatered` to that device date.
- Marking the same plant again on the same device date leaves it not due.
- Edge cases the user accepted are in the acceptance criteria. Unknowns stay open.

# Ready-to-paste brief

## Context
- Request source: Owner request to have an AI agent build the due-today behavior in the current app.
- Primary user: The plant owner, using the existing plant list.
- Secondary users / approvers: None. The implementing agent is the audience of this brief, not a product user.
- Problem or opportunity: The owner cannot see which stored plants are due today, so they water from memory.
- Current behavior / workaround: The app stores plants, and the owner decides what to water without a due list.

## Desired outcome
- User outcome: The owner sees which plants are due today and marks a plant watered from that list.
- Business or client outcome: None. Personal use.
- Prototype question: No prototype. This brief is for an AI-agent build.
- Success looks like: On the device date, a plant appears as due only when it has no lastWatered date or when lastWatered plus intervalDays is on or before that device date, and marking it watered removes it from due for that same date.

## Scope
- In scope:
  - Group due plants on the existing plant list.
  - Compute due from `lastWatered`, `intervalDays`, and the device calendar date.
  - Mark a plant watered from that list by setting `lastWatered` to the device calendar date.
- Out of scope:
  - A new backend, new database, or new account system.
  - A visual redesign of the list.
  - Photo identification, reminders, shopping, or care articles.
  - Changing how a plant is created, except reading the fields that already exist.
- Future considerations:
  - Push or email reminders. The owner postponed them.

## User stories
- As the plant owner, I want plants that are due today grouped on the existing list so that I can water those and skip the others.
- As the plant owner, I want to mark a due plant watered from that list so that it is not shown as due for the rest of that device date.

## Acceptance criteria
- Given a plant whose `lastWatered` plus `intervalDays` is on or before the device calendar date, when the owner opens the plant list, then that plant is in the due group.
- Given a plant whose `lastWatered` plus `intervalDays` is after the device calendar date, when the owner opens the plant list, then that plant is not in the due group.
- Given a plant with no `lastWatered` and a present `intervalDays`, when the owner opens the plant list, then that plant is in the due group.
- Given a plant in the due group, when the owner marks it watered, then `lastWatered` becomes the device calendar date and the plant is not in the due group.
- Given the owner marks that same plant watered again on that same device date, when the list refreshes, then the plant stays out of the due group and no second last-watered value is created.
- Given the owner has no plants, when they open the list, then the list shows that there are no plants and shows no due group.
- Given a plant whose `intervalDays` is missing, when the list renders, then the plant is not placed in the due group by inventing an interval. Placement of that plant is an open question and the agent stops on it.

## Constraints
- Technical: Change the existing app only. Do not add a backend. The user said `lastWatered` is a calendar date and `intervalDays` is a whole number they entered. File paths were not given.
- Design/brand: Do not redesign the list. No brand rules were stated. Group due plants in the existing list rather than on a new screen.
- Data/privacy: Use the plant fields already stored. Do not add accounts or new personal data.
- Timeline/budget: None stated.
- Platform: The app the owner already runs. No new platform.

## Assumptions
- The device calendar date is the date in the device’s current local timezone, with no separate user-selected timezone. The owner confirmed this.
- Marking watered is the only writer of `lastWatered` in this work. The owner confirmed this slice does not edit past dates.

## Open questions
- Which file or component renders the plant list. Not named. The agent must locate it in the current codebase and must not create a second list if one exists.
- Whether `lastWatered` is stored as a date-only value or as a timestamp. The user called it a calendar date. If the code uses a timestamp, the agent must not invent a timezone conversion beyond the device-local calendar date, and must ask before changing stored values.
- What to show for a plant with no `intervalDays`. Not decided. Do not invent a default interval.

## Build sequence
1. Locate the existing plant list and the stored form of `lastWatered` and `intervalDays`. If either field is absent, stop. Do not add a backend, an account system, or a new screen.
2. If `intervalDays` can be missing, stop and ask the owner what to show. Do not pick a default number.
3. On the existing list, group plants that match the due rule, using the device calendar date.
4. Add mark-watered on a due plant so `lastWatered` becomes that device calendar date, including the same-day second mark.
5. Check the acceptance criteria for: due, not due, missing `lastWatered`, missing `intervalDays` (stop), empty list, and marking watered twice on the same device date.
