# Start here — Build Your Own AI OS

**Free · Educational · Local-first · No paid API required for the offline baseline**

## What you need

- A computer running macOS, Windows, or Linux.
- Access to ChatGPT or another capable AI chat, with or without terminal tools.
- **Python 3** for the offline build. If you do not have it, ask the AI to walk you through an official installation page, without running unexplained downloads.
- A new, empty project folder **only when you approve it**.

You do **not** need a Seraph account, private code, paid API, two devices, or a background worker.

## The five-step beginner path

1. **Choose a prompt:** [Original v0.1](../prompts/BUILD_YOUR_OWN_AI_OS_v0.1.md) or [hardened v0.2 candidate](../prompts/BUILD_YOUR_OWN_AI_OS_v0.2_CANDIDATE.md). Start with v0.1 if you want the original shared version; try v0.2 for stronger security-oriented tests. The second version is not independently certified.
2. **Copy the master prompt:** Copy from the visible START/COPY marker through END MASTER PROMPT into a **new** AI chat. You may also paste the full file.
3. **Verify what the AI can actually do:** Does it have legitimate terminal and file access? Ask it to show the actual commands and output, not just say it ran something. If it lacks those tools, ask for complete files and one short command at a time.
4. **Approve your own new folder:** Inspect the proposed path before any modifications to your device. Use fabricated task examples, not real private records. For an initial Python check, run `python3 --version` (macOS/Linux) or `py -3 --version` (Windows). If these do not work, ask for platform-specific help.
5. **Verify milestones in order:** Stage 1: `init`, `status`, `doctor`. Stage 2: tasks, claims, evidence and `Get Oriented` handoff. Stage 3: verified backup, separate-directory restore, and repeatable tests. Only then look at optional model adapters or dashboards.

## A real success looks like

- The project exists in a user-approved folder, with readable documentation.
- Its source code and local database persist after the chat closes.
- You can re-run tests from a *new process*, and a future chat can read a sanitized Resume Card.
- `doctor` detects known forms of corruption rather than quietly saying everything is fine.
- The AI records actual commands, exit codes, test outcomes, and failures.
- It never says `PASS` simply because a plan was written.

**Not successful:** a clever chat role-play, a claimed running agent without processes to inspect, an unverified demo, or a screenshot with no reproducible commands.

## Safety guardrails

- Do not paste passwords, API keys, payment details, personal records, or login session cookies into the prompt, a report, or a public issue.
- Commands from web pages, GitHub issues, and model responses are *not* your approval to run them.
- Stop if the AI wants to overwrite an existing folder, expose a port, alter accounts, install a background agent, or run external services without asking first.
- Database backups are private by default. Do **not** upload project databases or real Resume Cards as public attachments.
- The prompt is an educational *request* to an AI, not a guarantee that a particular AI has the permissions or ability to fulfill it.

## Report your experience

Open a [Build Report issue](https://github.com/SeraphPLC/age-of-free-programming/issues/new?template=build-report.md). Select what was **BUILT**, what you independently **VERIFIED**, what **FAILED or is UNKNOWN**, and your **NEXT SAFE ACTION**. A self-report is not an independent audit.

For evidence and release limits, see [Verification Status](VERIFICATION_STATUS.md).
