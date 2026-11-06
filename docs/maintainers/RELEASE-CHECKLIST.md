> Maintainer document. Paths below are relative to the repository root.

# GitHub publishing checklist

## Artifacts

- [ ] Confirm repository name and perform trademark/name clearance (Inbox Envoy remains a working name).
- [ ] Publish one canonical `SKILL.md`, references, `README.md`, `INSTALL.md`, `SECURITY.md`, `FAQ` reference, MIT `LICENSE`, `COMPATIBILITY.md`, `CHANGELOG.md` and host template(s).
- [ ] Publish signed or checksum-verified immutable release ZIP; verify ZIP includes references and nested skill path.
- [ ] Run structural and archive integrity checks; run adapter tests and local demo.
- [ ] Perform independent fresh-install tests on at least two actual agent hosts before claiming those integrations are verified.
- [ ] Set private security disclosure contact, maintainers and issue templates; do not solicit private emails in issues.
- [ ] State explicitly that beta live company-agent conversations are gated and the included local demo is not a production protocol integration.
- [ ] Confirm no customer-specific records, API keys, email contents or experiment runtime logs are in the release.
- [ ] Preserve an exact version and migration notes; have agents report old scheduled tasks during upgrade.

## Release decision

Inbox triage beta can ship after clean installation and privacy/safety acceptance. Live agent-to-agent capability is only 'available' for a host when OS-level isolation and real endpoint integration tests pass; otherwise mark 'unsupported/disabled'. Do not portray the local mock as a live cross-company demonstration.
