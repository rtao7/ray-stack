# Example: one slice of a long PRD

**Input:** a PRD for “Fieldnotes,” a research-library product, with these sections:

1. Account and single sign-on
2. Upload documents
3. Highlight and annotate
4. Share a highlight by link
5. Team comments
6. Admin analytics
7. Billing

The skill does not turn the PRD into one brief. It names those slices and asks which one to focus on.

**The user chose:** section 4, share a highlight by link. They said sections 1–3 already exist in the product, and comments, analytics, and billing are not this project. The PM is the approver. The reader of the link may not have an account.

# Ready-to-paste brief

## Context
- Request source: PM request, sliced from the Fieldnotes PRD. The slice is “share a highlight by link.” The rest of the PRD was declined for this brief.
- Primary user: A signed-in researcher who already has a highlight in a document.
- Secondary users / approvers: The person who opens the link, who may not have an account. The PM approves the slice.
- Problem or opportunity: The researcher cannot show a colleague the exact highlight without sending the whole document or a screenshot.
- Current behavior / workaround: The researcher pastes a screenshot of the highlight into a message.

## Desired outcome
- User outcome: The researcher can send one link that opens that highlight, and the recipient can read the highlighted passage.
- Business or client outcome: The PM can accept this sharing slice without pulling comments, analytics, or billing into the same work.
- Prototype question: No prototype. This brief is the slice handoff for the share-by-link behavior.
- Success looks like: A recipient without an account opens the link and sees the highlighted passage and the document title. They do not see the rest of the document.

## Scope
- In scope:
  - Create a link for one existing highlight.
  - Open that link without requiring the recipient to sign in.
  - Show the highlighted passage and the document title only.
  - Let the researcher turn that link off so a later open no longer shows the passage.
- Out of scope:
  - Account creation, login, and single sign-on changes.
  - Uploading documents.
  - Creating or editing highlights and annotations.
  - Team comments.
  - Admin analytics.
  - Billing.
  - Showing the full document to the recipient.
- Future considerations:
  - Commenting on a shared highlight, which remains in PRD section 5 and is not this slice.

## User stories
- As a signed-in researcher, I want a link to one highlight so that a colleague can read that passage without a screenshot.
- As a recipient without an account, I want the link to show that passage and the document title so that I can read it without signing up.
- As a signed-in researcher, I want to turn an existing highlight link off so that a later visitor no longer sees the passage.

## Acceptance criteria
- Given a signed-in researcher has one existing highlight, when they create a link, then they receive a URL for that highlight only.
- Given a recipient is not signed in, when they open a link that is still on, then they see the highlighted passage and the document title, and they do not see the rest of the document and are not asked to create an account.
- Given the researcher has turned the link off, when any recipient opens that URL, then the passage is not shown.
- Given the researcher has not created a link, when a person guesses a highlight URL shape, then no passage is shown. The exact unguessable form of the URL is an open question and must not be invented here.

## Constraints
- Technical: Sections 1–3 already exist. This slice must use an existing highlight. Do not specify the API, token format, or storage.
- Design/brand: None stated beyond showing the passage and the document title. Do not invent the page layout.
- Data/privacy: The recipient sees only the highlighted passage and the document title. The user said the rest of the document stays hidden. No other privacy rule was stated.
- Timeline/budget: None stated.
- Platform: The link opens in a browser. No other client was requested.

## Assumptions
- “Existing highlight” means a highlight the product can already save in section 3. The PM confirmed this slice does not change how highlights are created.
- Turning a link off keeps the highlight itself. The PM confirmed the highlight remains for the owner.

## Open questions
- How a link is made hard to guess. Not decided. Do not choose a token scheme in this brief.
- What the recipient sees when the link is off or unknown: a blank page, a short explanation, or something else. Not decided.
- Whether the researcher can have more than one live link for the same highlight. Not decided.

## Build sequence
1. Confirm with the PM the two link-display open questions that block the recipient page: the off-link message, and whether multiple live links are allowed. Do not design a token scheme.
2. Let a signed-in researcher create one link for one existing highlight and copy the URL.
3. Let a signed-out recipient open a live link and see only the passage and the document title.
4. Let the researcher turn that link off, and check that a later open does not show the passage.
