# Example: client names a solution

**Input:** “Client wants a dashboard with AI insights.”

The skill does not accept “dashboard” or “AI insights” as the requirement. It asks what job the dashboard is supposed to do, which decision it supports, and what the client would count as an insight.

**Separated need and proposal:**

- Proposal, not yet a requirement: a dashboard that shows AI insights.
- Job, after asking: before the Monday 9:00 account review, the account director chooses which accounts to call that week.
- Decision supported: which accounts to call, and the one sentence the director will say about each.
- “Insight,” after asking, means a row built only from metrics and thresholds the client already uses: account name, metric name, current value, the client’s threshold, and whether the value is past that threshold. It does not mean a generated paragraph, a new score, or a chatbot answer.

**Also confirmed:** the client approver is the VP of Customer Success. The prototype is for alignment, not model development. Success is the director defending five call choices from those rows alone.

# Ready-to-paste brief

## Context
- Request source: Client request, brought by the account director. The client asked for a dashboard with AI insights.
- Primary user: The account director who prepares the Monday 9:00 account review.
- Secondary users / approvers: The VP of Customer Success, who approves whether this is the right aid before any further build.
- Problem or opportunity: The director cannot show, from the metrics the team already has, which accounts need a call this week and why.
- Current behavior / workaround: The director scans several existing reports and writes the call list by hand the morning of the review.

## Desired outcome
- User outcome: The director can choose up to five accounts to call and state the reason from the same row the VP can see.
- Business or client outcome: The VP can approve or reject this call-list approach before the team spends time on a model or a new dashboard product.
- Prototype question: Does a row of existing metric, threshold, and over-threshold state let the director pick the Monday call list without a written paragraph?
- Success looks like: In the alignment review, the director names the accounts to call and the reason for each using only those row fields, and the VP accepts or rejects that format. The director does not ask for a metric the client does not already track.

## Scope
- In scope:
  - A single list for the Monday review.
  - At most five accounts, chosen from rows that use metrics and thresholds the client already tracks.
  - Each row shows account name, metric name, current value, the client’s existing threshold, and whether the value is past that threshold.
  - A prototype or static listing sufficient for the VP to approve or reject that format.
- Out of scope:
  - A chatbot or free-form generated paragraph.
  - A score, prediction, or metric the client does not already calculate.
  - Replacing the CRM or the existing reports.
  - Sending email or scheduling calls.
  - A mobile app.
- Future considerations:
  - A standing dashboard, only if the VP approves this list format. Not part of this round.

## User stories
- As the account director, I want to see which accounts passed a threshold we already use so that I can choose who to call before Monday’s review.
- As the VP of Customer Success, I want to see the same rows as the director so that I can approve or reject this format before any model work.

## Acceptance criteria
- Given the client’s existing account metrics and the thresholds the client already set, when the director opens the Monday list, then each shown row contains the account name, metric name, current value, threshold, and whether the value is past the threshold, and no generated paragraph.
- Given more than five accounts are past a threshold, when the list is prepared, then it shows no more than five accounts and does not hide the fact that others also passed.
- Given the director is in the alignment review, when they explain a call choice, then they can point to a field on that row for the reason.
- Given the VP reviews the list, when they respond, then the outcome recorded is approve this format or reject this format. A new metric request is a rejection of this scope, not a silent addition.

## Constraints
- Technical: Use metrics and thresholds the client already produces. Do not introduce a model. No system names were given beyond the reports the director already opens.
- Design/brand: None stated. Do not invent a visual system. The listing must remain readable as rows of the fields above.
- Data/privacy: Use only account metrics the director already uses in the Monday review. No new personal data was requested.
- Timeline/budget: The list is needed for a Monday alignment review. No budget was stated. No build date beyond that review was stated.
- Platform: The director and VP must be able to look at the same list in the review. No product surface was chosen.

## Assumptions
- “Past the threshold” uses the comparison the client already uses for that metric. The director confirmed the brief must not define a new comparison.
- The director, not an automated ranker, chooses the five accounts when more than five qualify. The director confirmed this.

## Open questions
- Which existing report or export is the source of the metric values. Not named.
- What to show when a tracked metric is missing for an account. Not decided.
- Where the shared list lives for the review. Not chosen.

## Build sequence
1. Ask the director which existing report supplies the metric, the threshold, and the current value. Do not connect a system that was not named.
2. Prepare one list of at most five accounts using only those fields and the director’s choice of who to call.
3. Review that list with the VP against the acceptance criteria and record approve or reject.
4. Stop. Do not design a production dashboard unless the VP approves this format.
