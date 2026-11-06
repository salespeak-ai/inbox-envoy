# Agent-to-agent reference adapter

This is runnable Python 3.9+ standard-library code (CI runs 3.13) for a **fixed JSON-over-HTTPS seller evidence endpoint**. It asks exactly two neutral questions from a public offer identifier and claim IDs, does not accept private buyer data, pins an IP and TLS hostname, rejects redirects, limits sizes and sanitizes seller output. It does **not** implement live A2A, PAP or MCP protocol sessions. Publishing a discovery card alone is not proof that a compatible endpoint exists.

## Local fixture

The bundled `demo/compose.yaml` uses an isolated internal Docker network and a synthetic seller HTTP fixture. The HTTP exception (`allow_local_demo`) is limited to the named `seller` container and **must never be enabled for a public endpoint**. To test locally, install Docker and run `docker compose -f demo/compose.yaml up --build --abort-on-container-exit --exit-code-from questioner` from the repository root. Docker is not installed in the package-building environment, so that exact OS isolation must be verified by your deployment agent.

A normal unit-test path uses `python -m unittest discover -s tests -p 'test_*.py'` and does not contact a real seller.

## Real company integration is not automatic

To connect to a real consenting company, the operator must separately verify domain ownership, protocol compatibility, pinned globally routable IP, TLS and an approved network policy, run adversarial containment and denial tests in its target runtime, and collect explicit user authorization. Add a protocol-specific adapter for PAP/A2A/MCP as applicable. Do not mount mailbox tokens, private files or private prompts in the questioner. Configure the OS/container's egress restrictions independently; in-process destination checks are defense in depth only. Never pass private relevance criteria to the adapter.

`questioner.py` is a transport reference, not a secure turnkey launch mode. The universal skill must mark live interaction **disabled** until all protections are independently demonstrated.

## Hardening still required before production traffic

- External network egress enforcement and robust DNS pinning/re-resolution across runtime lifecycle; the code's fixed IP selection is not a firewall.
- Per-user quota/durable request ledger and a kill switch enforced at the host orchestration layer. This reference limits each invocation to two questions but does not enforce a global lifetime quota.
- Real transport adapters and endpoint ownership checks for PAP, A2A and MCP. No arbitrary card-advertised URLs.
- Independent red-team tests of inbound evidence fields, HTML/script injection, and attempted tool escalation.
- A truthful UI state: `live_company_agent_conversation: unavailable` until a specific deployment passes all gates.
