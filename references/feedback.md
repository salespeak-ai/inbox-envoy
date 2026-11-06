# Feedback reconciliation and learning contract

Use this reference whenever classifying, reconciling labels, learning from user corrections, restoring archived mail, or answering how to correct a classification.

## Core principle
A user's explicit correction or a detected external mailbox change outranks the model's old classification **for that message**. Respect the change without treating it as permission to create a sender/domain-wide rule. Do not overwrite a correction on a later sweep. New messages in the same thread are independent and eligible for triage.

## Capability and approval
- Determine whether the host can read current message labels/folders and persist an action ledger across runs. Mailbox event history is optional, not required. Do not claim to know who changed a label unless event identity is actually available.
- Before first active reconciliation, ask permission to inspect previously Envoy-labeled messages, record minimal metadata, and learn from label changes. If unsupported, allow corrections by chat and disclose that Gmail/Outlook changes will not be learned automatically.
- Use host-native storage (small file or database) and scheduling; do not require a new service. Keep the record private and avoid retaining message bodies.

## Ledger and bootstrap
Record mailbox/account ID, stable message ID (and thread ID), applied Envoy status, time and action/actor (`envoy`), last observed label state, revision/lock status, source of correction, and prior correction history. Capture only metadata needed for reconciliation; encrypt or restrict access as the host permits.

For already labeled mail at upgrade time, **import the current labels as a neutral baseline**, not as proof the label was correct, nor as evidence a user corrected it. Example: importing 73 existing messages creates 73 baseline records and **zero** training events. Where an old action ledger exists, migrate it safely. Do not remove or reset existing labels to establish a baseline.

Perform updates atomically and coordinate concurrent triage, investigation and digest tasks with a transaction, single-writer queue, or lock. On a failed write, do not claim a correction was saved. Prevent retries from duplicating the same correction event.

## Reconciliation each sweep
For each eligible ledgered message within the supported comparison window (a rolling 30 days is an acceptable default), compare *the previous Envoy-applied status* to currently observed Envoy labels. Reconcile before triaging new mail.

- Unchanged: no correction event.
- Different active Envoy status: record `external_label_change`, the before/after status, message ID and detection time. Preserve the new status and lock **this message's classification** against routine re-labeling, archiving and star changes. Do not claim it was the user if another agent/filter could have changed it.
- All Envoy status labels removed: record `external_label_removal`, preserve no-label state, and do not reapply. Do not treat unrelated label changes as Envoy corrections.
- User restores a filtered email to Inbox without changing Envoy label: treat as a **possible override**, preserve it in Inbox, suspend automatic re-archiving of that message, and offer confirmation in a digest when needed. Do not silently infer that `Filtered` should become `Important`.
- Envoy itself changes labels: atomically update the ledger's applied status so the next comparison does **not** count its own work as an external correction.
- More than one active Envoy status label or ambiguous/contradictory state: do not guess, leave mailbox unchanged and surface in Review / audit as appropriate.

For messages older than the reconciliation window, preserve permanent de-duplication and override tombstones; do not resume relabeling them merely because they are no longer compared. If storage disappears, treat all preexisting Envoy labels as externally owned, leave them alone, rebuild a conservative baseline, and tell the user that prior feedback history is unavailable. Never infer history from Gmail's current state alone.

## Learning: three levels of authority
1. **Explicit correction in chat:** apply to the individual message when authorized. Capture the reason if given. A general rule such as "always mark this sender important" requires an unambiguous explicit instruction or separate confirmation.
2. **Manual/external label correction:** strongest evidence for *that message's* new category, but only weak-to-moderate evidence for future messages because provenance may be unknown. Log as an example; do not silently create a global rule.
3. **Behavioral signals** such as unread, opened, deleted, archived: weak; never create unconditional policies from them.

If the same sender/category is corrected repeatedly (e.g., 2-3 times), **suggest** a narrowly scoped rule in a digest, including examples and exceptions. Activate it only after the user confirms. Even confirmed rules may not override security checks or make an unsafe sender trusted blindly.

Correcting `Filtered` to `Important`/`Opportunities`, or restoring a mistakenly archived valuable message, is a high-cost error: report it, add an anonymized regression example where practical, and pause or narrow the affected automatic archive rule until reviewed. Provide one-tap recovery instructions where tools permit.

## Scope, transparency, and audits
- Lock the individual **message**, not an entire thread or domain. Replies/new messages can be assessed normally while respecting the previous message's lock.
- Never assume a label change is from the owner; call it an **external correction** unless provenance is known.
- Count actual corrections and recoveries; distinguish confirmed user corrections from unverified external changes in weekly quality reports.
- Reconcile label changes without changing message read/unread state or removing non-Envoy labels.
- Record what could not be checked: retention window, missing history, state-store reliability, permissions and concurrent-task handling.

## Acceptance examples
1. Baseline 73 labeled messages: zero correction events on import.
2. `Envoy/Review` changed to `Envoy/Important`: preserve and lock only that message; no permanent domain rule.
3. `Envoy/Filtered` removed: do not reapply.
4. `Envoy/Filtered` message restored to Inbox without label change: do not re-archive; mark possible override.
5. Corrected thread receives new reply: classify new message independently.
6. Envoy changes a label itself: ledger update prevents false external-correction record.
7. Label changed by an unknown other automation: call it external; respect change but do not claim user intent.
8. State loss: never reclassify historical labels as new; rebuild baseline conservatively.
9. Simultaneous scheduled jobs: no lost updates or duplicate events.
10. Message ages beyond comparison window: override/tombstone still prevents future relabeling.
