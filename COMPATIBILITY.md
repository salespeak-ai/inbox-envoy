# Compatibility status

Inbox Envoy is designed for personal agents capable of consuming an Agent Skills-style instruction bundle, or a faithful translation into a custom bot/template. Whether a named agent can install a ZIP, read email, create labels, run unattended schedules, retain state, and restrict outbound interactions is host-specific.

| Surface | Skill delivery | Live mailbox integration | Unattended tasks | Live company-agent questioner | Status |
| --- | --- | --- | --- | --- | --- |
| Claude environments | Native skill/import where supported | Host-dependent | Host-dependent | Disabled without enforced isolation | Not verified by this release |
| ChatGPT | Host-specific installation | Host-dependent | Host-dependent | Disabled without enforced isolation | Not verified by this release |
| Grok bot or template | Template adaptation | Host-dependent | Host-dependent | Disabled without enforced isolation | Template provided, not tested |
| Other personal agents | Host-specific installation | Host-dependent | Host-dependent | Disabled without enforced isolation | Not verified by this release |

Do not interpret this table as asserting a platform feature. A platform passes when a fresh agent completes tests in `tests/ACCEPTANCE.md`: discover permissions, preview sample, create schedule *with permission*, verify next run, reconcile correction, safely downgrade, and report outbound status accurately.


<!-- BEGIN D1-D2A 2026-11-06 -->
## Personal-agent portability and capabilities

Inbox Envoy is designed to work with **all personal agents able to load skill instructions (or equivalent custom instructions) and use an authorized mailbox connection**. This statement describes the skill's portability, not certification that every agent can autonomously read, schedule, label, or send mail.

- **Observe:** Requires authorized read access. It must not modify mail or contact senders.
- **Label/archive:** Requires explicit user permission and actual host mail tools; archive only approved calibrated safe categories and keep recovery possible.
- **Scheduled triage:** Requires a host scheduler that can be created, inspected and revoked by the user.
- **Draft-only evidence screening:** Requires separate screening opt-in and draft ability. The full first message is previewed for approval.
- **Autonomous screening:** Requires separately verified host-enforced isolation, output controls, auditable send permissions, rate and thread caps, a working kill switch, and revocation. Otherwise draft-only.

Use the host's skill import workflow or equivalent instruction installation. Run [`tests/ACCEPTANCE.md`](tests/ACCEPTANCE.md) for the host's actual capabilities. Tests of individual sending or protocol features should be stated as tested/unverified separately from general instruction portability.
<!-- END D1-D2A 2026-11-06 -->
