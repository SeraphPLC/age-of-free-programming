# Privacy, Intellectual Property and Public Release Gate
**The Age of Free Programming | 2026-10-24 | PUBLIC-SAFE**

## What this policy covers
This repository publishes educational text for people to guide an AI assistant through building a small, local-first continuity project. The public repository is **not** the private Seraph project, does not contain or authorize private Seraph code, and does not have to disclose original corporate research, PLC papers, machine topology, agent control endpoints, accounts or unpublished internal documents.

**No claim of zero risk is made.** Technical and legal safeguards reduce exposure; they are not guarantees or a substitute for qualified professional review.

## Privacy and personal data

- This repository does not operate its own app backend, user database, telemetry collector, marketing tracker or login system. However, GitHub, social platforms and AI providers may process account and usage information under their own policies. Do not equate "local-first" with absolute privacy.
- Treat **GitHub Issues, commit metadata, pull requests, pasted Facebook comments and most public AI-chat sharing links as public and potentially persistent**. Never submit actual names, account addresses, personal email addresses, phone numbers, faces, identity documents, precise locations, bank/benefits information, educational records, medical records, family details, credentials, tokens, private case evidence, internal employee information or complete unredacted logs.
- Test with made-up tasks and synthetic data. Never upload private databases, real resumes/handoff cards, backups, browser profiles, credential stores or local source collections. Strip metadata, usernames, pathnames, hostnames, IP addresses, time-sensitive links and indirect identifiers from screenshots or output.
- Users who enter information into an online AI chat must independently review the provider's actual privacy controls and data-processing terms; **this repository does not control provider retention or training**.
- Report accidental secret disclosure privately. Revoke leaked credentials first; deleting current files or Issues cannot be relied on to erase all historic copies.
- Historical public commits include a personal author email address. This remains a KNOWN OPEN PRIVACY ITEM. Future CLI commits on the inspected Macs use a GitHub no-reply identity, but old commits and web/API writes are not automatically corrected. Public Issues are disabled; coordinated history and cache review is still required.

## Copyright, database rights, and third-party terms

- **A public hyperlink is not a license.** Publicly readable websites, official government pages, Wikimedia resources, Git repositories, archived books, model weights, datasets, images and software packages may each impose different conditions. Record exact author, upstream URL, date, version, license, attribution, commercial reuse rights, AI-training rights, redistribution rights and any non-copyright terms per asset.
- Do **not** import the private Seraph PLC canon, unpublished equations, original proprietary models, internal architecture, secrets, local archives, completed personal overlays or unreleased company documents into this repository. Generic ideas such as task ledgers, evidence, restart state and permission gates may be discussed independently without copying private source expression.
- Wikipedia text is commonly CC BY-SA; individual images can carry different licenses. iFixit content is CC BY-NC-SA 3.0 and its published terms restrict AI training. Regular PhET HTML simulations carry CC BY-NC 4.0 and have additional brand and commercial-use conditions. These resources may be **linked to as references**; their full contents must not be copied into a public or commercial bundle without a documented lawful basis.
- Open-source software licenses, model weight licenses, training datasets, text/content licenses and provider API agreements are distinct. A tool having an open-source implementation does not license every model or dataset used with it. Avoid using unapproved mirrors and pirate copies.
- Keep an itemized manifest, source identity and specific permitted use for any later third-party package, archive, model or data. Default **BLOCKED** for rights that are unknown. Do not automatically fetch, scrape, mirror, index, embed, fine-tune, redistribute, sell or commercially display third-party content.
- Artificial intelligence may generate source text resembling other code. Inspect generated artifacts for identifiable copyrighted sections and unlicensed dependencies before publishing. Do not guarantee users own every line of generated output; ownership and rights can depend on provider terms and applicable law.

## Naming, endorsement and marketing
- "AI OS" is an educational project nickname for a layer **on top of** an existing operating system, not a replacement computer OS. Do not advertise a ready-to-install, independently security-audited, autonomous, production, revenue-generating or government/medical-certified product.
- Mention of OpenAI, Anthropic, Google, GitHub, Microsoft, xAI, Kiwix, Wikimedia, iFixit, PhET, schools or government agencies is descriptive identification, **not endorsement, partnership or trademark permission**.
- Tests are evidence **only within the tested version, platform and scope**. A synthetic Linux reference test run does not prove fresh-chat builder reproducibility, Mac/Windows compatibility, privacy compliance or independent Council acceptance.
- Never market outcomes, savings, medical results, legal conclusions, deployment, cross-model acceptance or provider access that cannot be traced to actual qualified receipts.

## Public release admission checklist
All items must be checked before a **new** release of executable code, bundled data, AI model, automation or installed service (not merely a text correction):

1. **Owner and scope:** documented rights-holder or authorized release approver, exact files and protected/private materials excluded. Check that the version and audience are explicit.
2. **Secrets, identities and history:** scan the current tree **and commit/PR history** for credentials, identifiers, private links, accounts, machine locations, employment/customer/student/medical data and hidden metadata. Correct before publication; history cleanup requires a separate plan and approval.
3. **Source rights:** inventory the SBOM for code and source/asset manifest for all third-party content, exact licenses, attribution, modification, distribution, commercial and AI-training terms. Have a human review conflicts.
4. **Security:** malicious-file/symlink/path-traversal checks, permissions, network destination allowlist, bounded compute, dependency advisories, prompt-injection tests, offline negative tests, safe secrets storage and actual restore/rollback tests.
5. **Privacy:** data-minimization review, test datasets synthetic, cloud-provider disclosure and retention, no default telemetry, no unrelated filesystem scan or background accounts, public-report redaction checks.
6. **Proof:** run reproducible tests with source revision, command, exit status and sanitized receipt; record FAIL and NOT RUN; never fabricate independent reviewers or describe proposals as deployed.
7. **Authority and cost:** no payment, API billing, account changes, messaging, publication, browsing a private account, external provider dispatch, credential operations, production deployment, merge or destructive change without exact separate approval.
8. **Release controls:** review public diff and history, GitHub repository visibility and commit author privacy; designate a stop/rollback path, vulnerability report channel and incident owner. Then record a human release decision.

If any protected requirement is UNKNOWN, **hold the executable or dataset release** and continue only with public-safe educational pointers.

## Known open issues as of this audit
- **Historical public commit metadata exposes an author email.** A future `noreply` setting cannot undo earlier commits; a history rewrite may break hashes and not remove forks/caches. No history rewrite is authorized or performed here.
- The public prompts have no selected repository-wide open-source license for future generated software or unrestricted relicensing. This is not fixed by choosing an irrevocable Creative Commons license without the appropriate rights-holder decision. See [sharing and license status](SHARING_AND_LICENSE_STATUS.md).
- Full legal, source-by-source license, cross-platform security and independently verified fresh-chat implementation reviews have **not** been completed.
- GitHub public issue participants may still voluntarily disclose personal information despite warnings. Review submitted reports and escalate confidential disclosures through the private vulnerability channel.

## Verification references
[GitHub repository licensing](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository) · [GitHub historical commit email privacy](https://docs.github.com/en/account-and-profile/how-tos/email-preferences/setting-your-commit-email-address) · [GitHub history removal limitations](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository) · [iFixit licensing](https://www.ifixit.com/Info/Licensing) · [PhET licensing](https://phet.colorado.edu/en/licensing/) · [Wikimedia terms](https://foundation.wikimedia.org/wiki/Terms_of_Use)

**This is a practical release-control policy, not a formal legal opinion or assurance that a particular use is lawful.**
