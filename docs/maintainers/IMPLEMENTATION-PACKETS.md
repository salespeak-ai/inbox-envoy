> Maintainer document. Paths below are relative to the repository root.

# Agent execution packets: buyer-side public beta

**Outcome:** A GitHub repository and installable Inbox Envoy skill with documented host limits, proven mailbox safety, and a separately gated working company-agent conversation path. Use the skill as the single source of behavioral truth. Do not create a proprietary backend or enroll users in a hosted service.

## Agent 1: Release packaging

- Verify the source folder contains the canonical SKILL.md, full references, agents metadata, MIT LICENSE, README, INSTALL, SECURITY, FAQ, COMPATIBILITY and CHANGELOG. Keep host templates derived from the same skill.
- Add source-control structure, release tag and ZIP checksum. Exclude private records, runtime secrets, trial email data, experimental state and credentials.
- Complete public naming/trademark availability review and ensure maintainer contact is configured.
- Output: GitHub repo, immutable versioned release and install link; note whether all listed platforms have actually passed compatibility tests.

## Agent 2: Onboarding and user experience

- Run from clean personal agent state, not the development conversation.
- Ensure skill introduces Observe, Label-only, Archive, optional public research and optional live conversation, without requiring users to open MD references.
- Ask for permissions incrementally, show a preview sample, propose 30-minute (seven-day) triage if scheduler supports it, and verify the task after approval.
- Include explicit progress/status reports, upgrade reconciliation, pause and rollback, and a compact FAQ response capability.
- Output: signed-off first-run transcript with user-sensitive details redacted, exact failure cases, acceptance result.

## Agent 3: Safety and QA

- Run tests/ACCEPTANCE.md on a synthetic inbox and adversarial documents.
- Ensure unauthorized sends, deletes, archiving, agent interactions and scheduling are denied.
- For the questioner, test no buyer credentials/memory mounts, network namespace restrictions, DNS rebound/SSRF, HTTP redirects, cookies, payload injection, malformed JSON, oversize, loops, repeated runs, kill switch and logs. Security tests must run on the actual OS/runtime, not only unit tests.
- Output: dated probe results, environment diagram, PASS/FAIL/UNVERIFIED matrix and blockers. Never equate prompt separation with enforced isolation.

## Agent 4: Platform compatibility and templates

- Import the same canonical skill through at least two different personal agents and run the acceptance suite. Start with previously accessible hosts, but do not assume compatibility based on the product name.
- For Grok bot templates and similar platforms, map skill instructions to available native tools while preserving the permission model; do not imply that the prompt grants mailbox rights.
- Output: reproducible install steps and supported/unsupported matrix per platform.

## Agent 5: Agent-to-agent transport and integration

- Start from `adapter/questioner.py` and `demo/`. The current transport contract is a test-only fixed JSON endpoint, **not yet** a protocol-complete PAP, A2A, or MCP client.
- Verify the current protocol specifications and implement separate adapters for each actually deployed transport. Discovery does not authenticate the seller or grant permission to connect. Handle endpoint ownership, schema contracts, origin/DNS/TLS policies and user-approved scopes.
- Run Docker-level filesystem and network isolation tests. Never send private user context to the questioner.
- After explicit approval of a **specific consenting company endpoint**, complete one real session, inspect evidence and audit logs, and confirm no privileged access, metadata handling and permission revocation. Keep real endpoint details out of public files unless consented.
- Output: real integration run log, protocol implemented, network and isolation proofs, and scoped status. If not completed, report live capability disabled, and leave beta's static/research path functional.

## Coordinating agent: release decision

Check all five packets. Public inbox beta must not ship if unauthorized mailbox writes or sender contact are possible. A live conversation claim must not ship unless a real consenting endpoint and sandbox gate pass. Treat an OS-isolated local mock exchange as a developer demo, not as real external agent-to-agent compatibility. Do not treat absence of observed errors as proof of future reliability. State which work remains open and who owns it.
