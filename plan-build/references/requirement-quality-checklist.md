# Requirement quality checklist

Run this before emitting `# Ready-to-paste brief`. This is a structural and wording gate, not a market or technical review. If an item fails, ask another question or move the gap to Assumptions or Open questions.

## Gate

- [ ] Every requirement is observable or verifiable. A person could tell whether it happened.
- [ ] No vague adjectives remain in stories, acceptance criteria, or success: intuitive, modern, fast, seamless, easy, simple, robust, user-friendly, smart, insightful, powerful, elegant, delightful, frictionless, clean, nice, better.
- [ ] Each user story has at least one acceptance criterion.
- [ ] Stories are small, valuable, and independent enough to build in the listed order. Split a story that bundles two unrelated outcomes.
- [ ] Assumptions are explicit, and each one was shown to the user.
- [ ] Non-goals are explicit in Out of scope. They came from the user, including an explicit “nothing is excluded.”
- [ ] No technical or design decision appears unless the user stated it or it is labeled as an open question the implementer must not resolve alone.
- [ ] Build sequence step 1 is a concrete first action and does not depend on a hidden invention.
- [ ] Primary user is a specific person or role, not “users.”
- [ ] The problem sentence still makes sense if the proposed feature name is deleted.
- [ ] Nothing in the brief contradicts an open question.

## Vague words

Do not translate the adjective yourself.

1. Quote the word.
2. Ask for one case that would count as success and one that would count as failure.
3. Write Given/When/Then from their answer.
4. If they have no answer, put the word in Open questions and leave it out of User stories.

Example input: “Make onboarding seamless and intuitive.”

Ask: “What can a new person finish, and what happening would mean they got stuck?”

Only after they answer (for example, they can add the first item without leaving the page, and a blank name does not pretend to save) may you write:

- Given a new person with no items, when they enter the required name and save, then the item appears on the list and they never leave that page.
- Given a blank required name, when they choose save, then nothing is created and the name field shows that a name is required.

“Seamless” and “intuitive” do not appear in the criterion.

## Story check (INVEST)

Before output, for each story:

| Check | Fail when |
|---|---|
| Independent | It cannot be tested unless a later story is also built |
| Negotiable | It prescribes an unrequested layout, algorithm, or vendor |
| Valuable | The “so that” clause only repeats the feature |
| Estimable | Scope depends on an open question hidden inside the story |
| Small | It describes a whole product rather than one outcome |
| Testable | The matching criterion uses a vague adjective or has no observable result |

## Assumption vs open question

- **Assumption:** the brief may proceed as if this is true. The user confirmed it or explicitly told you to proceed with it.
- **Open question:** the implementer stops or avoids that decision. Do not also write the answer into a user story.

Do not put the same unresolved point in both places with two different answers.
