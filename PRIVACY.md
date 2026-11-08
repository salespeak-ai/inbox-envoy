# Privacy

Inbox Envoy is a set of instructions (`SKILL.md` and `references/`) plus a small standard-library Python reference client. It is not a hosted service. This page describes what the package itself does with data. Last updated 2026-11-07.

## What Salespeak receives

Nothing. The package contains no Salespeak endpoint, account, API key, hosted backend, telemetry, analytics or callback. Salespeak, the maintainer, does not receive your email, your relevance profile, your labels or your decisions. You can check this by reading the package.

## Where your data is processed

The skill runs inside the personal agent you install it in. That agent (the host), its model provider, your mail provider and any connector you attach process your data under their own privacy policies. Inbox Envoy does not change those policies and cannot verify them for you. Review them before you grant mailbox access.

Your relevance profile, labels and preferences are stored wherever your host stores skill state. Inbox Envoy never deletes mail.

## What leaves your agent, and only if you turn it on

- **Public research (default):** to check an unfamiliar offer, your agent searches and reads public web pages. Those requests go through your host's own browsing or search tools.
- **Sender screening (opt-in):** your agent sends an evidence request to the sender of a cold email. If you also keep the default guidance link, that email links to a general page on salespeak.ai. The link has no per-user tracking code and carries nothing about you. A sender who opens it is subject to the [Salespeak website privacy policy](https://salespeak.ai/privacy-policy/). You can turn the link off.
- **Company-agent exchange (opt-in):** your agent sends questions about the offer to an agent endpoint the seller publishes. The questions are about the offer, not about you, and the reference client sends no destination by default.
- **Signature line (manual):** if you add the optional signature line yourself, it links to the same general page. The skill never edits your signature.

## Contact

Questions about this policy: open an issue at https://github.com/salespeak-ai/inbox-envoy/issues. Security reports: see [SECURITY.md](SECURITY.md).
