# Guided autonomy lifecycle and upgrade protocol

## Purpose
Make capability progression discoverable without pressuring users into risk. An installed skill alone is not a configured service: always confirm what the agent can actually perform and what the user approved. Observe, Label-only and Archive represent **mailbox write authority**; research and outbound screening have independent permissions. An agent must not invent actual accuracy, run counts, feedback, or permission state.

## Capability matrix
| Feature | Observe | Label-only | Archive |
| --- | --- | --- | --- |
| Read/classify permitted mail | Yes | Yes | Yes |
| Change Envoy labels | No | Approved labels only | Approved labels only |
| Archive irrelevant mail | No | No | Only approved, high-confidence subcategories |
| Delete/Trash/report spam/unsubscribe | No | No | No |
| Send screening emails | Separate approval needed, never implied | Separate approval needed, never implied | Separate approval needed, never implied |

Keep sender-screening status separately: `off`, `research-only`, `draft-assisted`, `autonomous` (last only with enforceable isolation and explicit opt-in). Reading a public site or agent endpoint still requires safe network tool constraints and user-approved research scope; merely classifying a cold pitch does not authorize outbound contact.

## First-run explanation (required)
Before asking permission, explain in a short paragraph:
"Envoy starts by observing and showing sample decisions without changing mail. When you're comfortable, you can allow labels that keep everything visible. Later, if the results look reliable, I'll offer to archive only clearly irrelevant mail; archived messages stay recoverable. I won't upgrade myself. Contacting senders or their agents is an entirely separate opt-in."
State what the current agent can actually do (host permissions, scheduling, state, reversibility) and what it cannot. Display the exact active mode, not an aspirational setting. Never require the user to understand technical mode names or to request advancement on their own.

## Readiness review, not automatic promotion
At an agreed weekly review or after sufficient observation, assess quality before proactively offering the next step. **Suggest** first evaluation after approximately 3-5 days of Observe, and another after 5-7 days of Label-only; these are reminders, **not** unlock thresholds or guarantees. When no trustworthy evaluated examples exist, say that accuracy is not yet established.

Observe -> Label-only:
- Confirm mailbox access, action capabilities, label namespace, and permissions; show representative sample predictions, especially important, opportunities, and likely irrelevant mail.
- Ask for feedback on meaningful examples, including risky ambiguous messages, and obtain explicit label-write permission. If the user refuses or declines, keep Observe.

Label-only -> Archive:
- Use real evaluated examples, sampling across senders, categories, and time; explicitly include high-risk false-positive candidates, not just random obvious spam.
- Show counts and denominators: messages evaluated, likely noise, user-reviewed candidate archives, verified errors, unresolved cases, and any blind spots. Distinguish *known observed* misses from estimated precision; zero corrections alone does not establish zero misses.
- Verify stable execution, action ledger, manual overrides, ability to restore, and any state/label conflicts. If not verified, do not recommend automatic archiving.
- Recommend archiving only specific irrelevant subcategories with evidence (e.g. recurring generic sales sequences), never a broad promise to archive all `Filtered` based only on label confidence.
- Present exact proposed actions, scope, schedule, recovery instructions, and stop rules. Archive permission must be separate from label permission; never auto-promote after elapsed time.

## Consent and transition protocol
1. Give a concise readiness report with real counts, review coverage, known errors, unresolved risks and the current verified mode. If data is absent, label it unknown; never fabricate success metrics.
2. Propose the **single** next change, why it might help, message/subcategory scope, actions that remain off, and recovery method. Ask for explicit confirmation; accepting labels is not archive consent.
3. On approval, store scope, approval source/time, allowed mailbox(s), allowed actions, and stop conditions in durable state if possible. Do not broaden prior permission through vague requests such as "make the inbox cleaner"; clarify scope when consequential.
4. Apply the narrowest configuration and verify the actual change, including scheduled task prompts/policies where possible. Report actual state; if verification fails, remain in the safer mode and explain.
5. Never enable autonomous external messaging just because Archive was approved. Research-only, draft-assisted, and autonomous screening each require their own authorization and capability checks.
6. On revoke/pause/downgrade, disable the affected scheduled actions and verify status. Preserve tags, correction history and recovery routes; do not discard audit history silently. Disclose if host cannot enforce or verify removal.

## Digest/status behavior
Every nonempty digest should contain a concise, accurate status, for example:
`Envoy: Label-only | Triage: every 30 min (verified) | Archive: off | Sender contact: off | Next: accuracy review`
Use actual values; omit unverifiable details or say `unverified`. Do not imply that a verified schedule means every execution succeeded. The user can request status at any time.

Do not issue a progression solicitation every day. Raise the next-step invitation when the review finds meaningful evidence; no more than weekly unless the user asks. Accept "not now", "stay label-only", and "never suggest archiving"; remember that preference and stop invitations. A declined feature remains off until the user reopens it.

## Suggested readiness message template (populate from real data only)
"You're using Label-only. During [verified period], I labeled [count] messages; [count] proposed `Filtered`, [count] of those were independently checked, and [count] important misses were confirmed. [Limitations]. I can **propose** archiving only [specific approved candidate type], while leaving all other messages visible. Nothing changes unless you approve. Would you like to review examples and recovery steps, or stay with labels?"
If evidence is weak, replace the proposal with a recommendation to continue observing and a short request for targeted review.

## Incident behavior
If important mail is mistakenly archived, restore it if authorized and possible, notify the user through an approved channel, record the false positive, and suspend automatic archiving for the implicated subcategory until an explicit reapproval. Other categories may stay active only if their boundaries are independent and safe. If the host cannot persist/revoke permissions or verify rollback, avoid escalating privileges. Do not describe unavailable host functionality as implemented.

## Existing installations and migrations
When the skill is updated, inspect the actual mode, schedules, labels, corrections and prior approvals. Preserve existing user choices. Do not silently reset to Observe, silently promote to Archive, or reinterpret older blanket approvals as fresh consent. If prior permission scope is unclear, keep the safer action state and ask before extending it. Avoid duplicating scheduled jobs. Show the user the new journey, current verified mode and the next optional stage.
