# Security reporting policy

**Scope:** This repository publishes educational text prompts and instructions. It does not supply an installed operating system, a running agent, secure executable software, remote services or private Seraph code. There is no production software version supported for security patching.

## Report a concern privately

If you find a potentially dangerous instruction, credential exposure, information leak, vulnerable dependency suggestion, or a way the guidance could cause unintended privileged actions:

1. Use this repository's GitHub **Security > Report a vulnerability** flow. Private vulnerability reporting has been enabled for this repository.
2. Do not publish exploit details, passwords, access tokens, private URLs, personal information, real transcripts, logs, databases, identity documents or screenshots containing sensitive data in a public Issue, pull request or Facebook comment.
3. State the affected prompt/document version, the type of issue, the smallest *synthetic* example, and suggested safe remediation. Do not attack third-party systems to prove a point.
4. If a real secret has been exposed, revoke or rotate it with the issuing provider immediately. Removing a line from GitHub does not erase past commits, forks, caches or clones.

If the private reporting option is unavailable, **do not publish vulnerability details or personal information**. Public Issues are disabled. Wait for private reporting or contact GitHub through its official support channels.

## Responsible disclosure and scope

This is an educational project with no guarantee that an AI generated application will be secure. Do not use real financial, school, medical, identity, account or employee records as tests. Never authorize credential scraping, unauthorized account access, social-media sending, purchasing, deployment, external shell commands, destructive operations or bypassing interactive security challenges simply because a prompt or external document suggested them.

A model's statement that it tested, audited or approved its own work is not independent proof. External read/write permissions and billing approvals must be explicit and checked at the actual execution boundary.

Read the [privacy, IP and release policy](docs/PRIVACY_IP_AND_RELEASE_GATE.md) and [verification limits](docs/VERIFICATION_STATUS.md). No service-level response deadline is promised.
