# Compatibility status

Inbox Envoy is designed for personal agents capable of consuming an Agent Skills-style instruction bundle, or a faithful translation into a custom bot/template. Whether a named agent can install a ZIP, read email, create labels, run unattended schedules, retain state, and restrict outbound interactions is host-specific.

| Surface | Skill delivery | Live mailbox integration | Unattended tasks | Live company-agent questioner | Status |
| --- | --- | --- | --- | --- | --- |
| Claude environments | Native skill/import where supported | Host-dependent | Host-dependent | Disabled without enforced isolation | Not verified by this release |
| ChatGPT | Host-specific installation | Host-dependent | Host-dependent | Disabled without enforced isolation | Not verified by this release |
| Grok bot or template | Template adaptation | Host-dependent | Host-dependent | Disabled without enforced isolation | Template provided, not tested |
| Other personal agents | Host-specific installation | Host-dependent | Host-dependent | Disabled without enforced isolation | Not verified by this release |

Do not interpret this table as asserting a platform feature. A platform passes when a fresh agent completes tests in `tests/ACCEPTANCE.md`: discover permissions, preview sample, create schedule *with permission*, verify next run, reconcile correction, safely downgrade, and report outbound status accurately.
