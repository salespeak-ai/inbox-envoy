# Install Inbox Envoy through your personal agent

**Paste this to your personal agent:**

> Install the Inbox Envoy skill from the attached ZIP or this repository using your supported skill workflow. Read `SKILL.md`. Check your actual mailbox, scheduler, state, and research capabilities, then walk me through onboarding. Start in Observe with no mailbox changes and no external contact. Show the operational readiness report. Do not schedule or change anything until I approve.

If your agent does not support native skill packages, ask it whether it supports a trusted custom-instructions or bot-template import. If it cannot load the skill and its references consistently, do not claim installation succeeded. Never ask users to paste mailbox passwords into a prompt.

## Grant the narrowest mail access

Your agent can only misuse rights it holds. Grant what the current mode needs, and widen later.

| Mode | Gmail | Outlook (Microsoft Graph) |
| --- | --- | --- |
| Observe | `gmail.readonly` | `Mail.Read` |
| Label-only / Archive | `gmail.modify` (also allows sending; Gmail has no label-only scope that excludes send) | `Mail.ReadWrite` (no send; it can delete, which Envoy never does) |
| Sender screening | add `gmail.compose` or `gmail.send` only when you approve screening | add `Mail.Send` only when you approve screening |

On Gmail, Label-only means the connector can technically send. That is why triage runs as a tool-less classifier plus a separate actor (see "Triage isolation" in `SKILL.md`). Ask your agent to report whether its host enforces that split. If the host connector does not let you choose scopes, ask the agent which rights it holds and record the answer.

Scope descriptions: [Gmail API scopes](https://developers.google.com/workspace/gmail/api/auth/scopes), [Microsoft Graph permissions](https://learn.microsoft.com/en-us/graph/permissions-reference).

## Expected first run

1. Explain Observe, Label-only and reversible Archive; seller conversations are optional separate permissions.
2. Detect authorized inbox, read/sent access, label/archive rights, scheduler, durable state and retrieval limits.
3. Offer opportunity research: off / search-only / verified-public-page research; explain direct network metadata.
4. Preview a small recent-mail classification sample without touching messages; invite corrections.
5. Propose 30-minute daily triage (7 days), a slower investigation queue and daily digest; get explicit approval and verify tasks after creating them.
6. Report what is enabled, verified, unavailable and what approval is needed next.

## Upgrades

Tell the agent to replace the skill instructions, preserve learned preferences, saved label ledger, approvals and existing tasks, compare recurring tasks with the desired schedule, and avoid duplicating the scheduler. Updating a ZIP does not automatically stop old jobs or enable new permissions.

## Host-native templates

See `templates/GROK-BOT-TEMPLATE.md` and `templates/HOST-ADAPTER.md` for a copy-ready bot prompt and an acceptance checklist. They are template text, not deployed bots or certified integrations.


<!-- BEGIN D1-D2A 2026-11-06 -->
## Portable installation and D2a setup

Import the skill with your personal agent's supported skill or instruction workflow. Begin in Observe/read-only; check mail, scheduler, draft and isolation tools before offering any other mode. Sender contact remains a distinct opt-in. Preview the full new evidence-request template before authorizing changes, particularly when upgrading an existing customized active template. Default skill attribution is off. Optional signature wording is manual only.
<!-- END D1-D2A 2026-11-06 -->
