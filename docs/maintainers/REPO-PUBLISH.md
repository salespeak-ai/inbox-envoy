> Maintainer document. Paths below are relative to the repository root.

# Instructions for the publishing agent

Create the public GitHub repository from the **contents** of this directory (the directory `inbox-envoy` should become the repo root). The repository must include `SKILL.md`, `references/`, `agents/`, docs, tests, templates, and adapter/demo files.

1. Verify the open-source copyright and name clearance with the project owner; MIT LICENSE is already included but the maintainer must confirm ownership.
2. Publish main branch and configure GitHub Actions. Verify `ci.yml` runs in the root repository.
3. Run fresh installation smoke tests on two named personal-agent environments, recording platform-specific limitations and permissions in `COMPATIBILITY.md` before claiming those environments are verified.
4. Publish the canonical skill package as a GitHub release attachment named `skill.zip` (folder root `inbox-envoy/`). Add SHA-256 to release notes. Do not upload synthetic runtime secrets, private mailbox data, or developer logs.
5. Offer the universal installation prompt from `INSTALL.md` and the Grok bot template from `templates/` as separate distribution mechanisms. The latter is not an actual published bot until the platform-specific publishing action succeeds.
6. Clearly label live company-agent sessions as optional/disabled unless the target environment has passed security and real-endpoint gates. The included local fixture is a technology demonstration only.
7. Report the exact repository URL, release tag, downloadable ZIP and installed-host test status to the owner. Do not claim publication before GitHub confirms it.
