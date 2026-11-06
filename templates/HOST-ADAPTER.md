# Host acceptance contract

The canonical skill must remain portable. Host adapters translate common intents into the platform's existing capabilities, never override the safety constraints.

## Detect, do not assume

- Mailbox read and thread context; whether checking unread marks messages read.
- Mutable labels/folders, archive, sending scopes, official authentication, history of manual changes (or reconciliation using saved ledger).
- Scheduled jobs/events, timezone, persistence across restarts, duplicate run handling, task listing and cancellation.
- Public research and safe direct fetch restrictions; network access metadata and costs.
- True security isolation and outbound egress enforcement for live agent interactions.

## Functional outputs

Report `mode`, `research_scope`, `triage_schedule_verified`, `last_success`, `mailbox_writes`, `archive`, `agent_conversation`, `sender_email`, `state_persistence`, `gaps`, and `next_permission_request` in ordinary language. Never fabricate a task ID. Distinguish 'user approved' from 'agent configured and verified'.

## Required downgrade behavior

Stop authorized autonomous writes and outgoing communications promptly, cancel relevant scheduled tasks, verify cancellation, and preserve recoverable user classifications. Never turn off unrelated user automations.
