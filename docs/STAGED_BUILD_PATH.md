# Build a Personal AI OS without overwhelming one AI chat

**Free educational path — no installed app is supplied by this repository.** The long [v0.4 master prompt](../prompts/BUILD_YOUR_OWN_AI_OS_v0.4_MEMORY_FIDELITY_CANDIDATE.md) remains available as the detailed specification, but beginners should usually work **one stage at a time**, each with actual test evidence.

**Different AI service?** See [public methods for frontier AI apps, coding tools and optional APIs](FRONTIER_AI_ACCESS_METHODS.md). You do not need every provider or a paid API. A chat-only AI can help plan and save a handoff; real code/testing requires a computer-capable tool and your permission.

**Want to understand the system before building?** Read the [11-part public Mesh architecture reference](architecture/README.md). Its neurons, connections, memory and human-control mechanisms are educational explanations, **not instructions to connect to private Seraph** or proof that all proposed features are running.

## Which path fits your tools?

| Your setup | Start with | What you really get |
| --- | --- | --- |
| Ordinary AI chat, no computer control | [Stage 0](../prompts/stages/00_CHAT_ONLY_CONTINUITY.md) | A manual, privacy-safe state card; no installed software |
| ChatGPT with a connected and approved **Remote Desktop Commander** test device | **[Recommended setup and security guide](RECOMMENDED_COMPUTER_SETUP.md)**, then [Stage 1](../prompts/stages/01_OFFLINE_CORE.md) | The AI can create and test files on **your own isolated computer**, with a separate third-party trust boundary |
| AI can read/write/execute on **your approved** computer (Codex, Claude Code, similar) | [Stage 1](../prompts/stages/01_OFFLINE_CORE.md) | A chance to actually build and test a Python/SQLite program |
| You can run a few commands by copying files from chat | [Stage 1](../prompts/stages/01_OFFLINE_CORE.md) | Smaller file batches and manual verification; takes more effort |
| You only want basic continuity | [Simple alternative](SIMPLEST_VALID_PATH.md) | A local handoff file plus version control; no elaborate database |

**Safety:** Remote computer access is optional and powerful. Read the setup's security warning: configured allowed directories and blocked commands are **not** an operating-system sandbox. Start with a throwaway VM or restricted user, fictional records, and the smallest approved folder.

**Stage order:** [0: manual chat](../prompts/stages/00_CHAT_ONLY_CONTINUITY.md) → [1: offline CLI](../prompts/stages/01_OFFLINE_CORE.md) → [2: tasks, evidence, backup](../prompts/stages/02_TASKS_EVIDENCE_RECOVERY.md) → [3: memory fidelity](../prompts/stages/03_MEMORY_FIDELITY.md) → [4: optional knowledge/models](../prompts/stages/04_OPTIONAL_KNOWLEDGE_MODELS.md).

You can stop at any working stage. Stage 4 is optional, and even Stage 3 does not require an AI provider after the local code is built.

## How to begin and resume

1. **Copy just the current stage's prompt** into the AI you chose, not all five stages at once.
2. Require tool capability disclosure, one explicitly approved new folder, synthetic test data, and real command output.
3. Check that the stage's acceptance tests actually ran. Ask for code, exact command receipts and remaining failures, not merely a confident summary.
4. Save the source and test records **on your own computer**. Keep personal information out of any cloud chat.
5. Have the assistant make a small **sanitized handoff card**. Open a fresh chat and provide **the next stage prompt plus only the approved sanitized handoff**; where the AI can access the same local folder, require it to verify current files and revision rather than trust the card.
6. In the new chat, permissions must be approved again. A saved handoff does not authorize installs, edits, sending messages or account changes.

## Minimal synthetic handoff example

```text
MISSION: Create an imaginary greenhouse task tracker.
PROJECT STATE: Stage 1, local source version demo-001 (confirm on disk)
KNOWN: A Python/SQLite CLI is proposed; verify actual files and tests.
DONE: init/status/doctor were reported by prior AI; local receipts must be checked.
OPEN: Task claims, evidence journal and backup/restore not tested.
AUTHORITY: NONE CARRIED OVER. Human approval required before changes.
FAILED/UNKNOWN: No cross-chat test; no model interface.
NEXT: Verify Stage 1 source and results read-only; propose Stage 2 change.
```

Do not paste actual private file paths, credentials, cloud access tokens, private task content, account names, database copies or real client information into online chats.

## What counts as completing 1.0?

A project author may choose to label a **bounded functional release 1.0** when the core CLI, durable task/evidence state, separate-directory restore and appropriate security/negative tests are actually working and documented **for that implementation and platform**. Advanced knowledge/model adapters and exhaustive M01–M22 tests are separate higher-level goals. Do not call this public repository itself an installed AI OS or guarantee independent model-to-model fidelity.

To evaluate broader memory claims, use the [memory adversarial plan](MEMORY_FIDELITY_ACCEPTANCE_V1.md). A Stage 1 smoke test is not a Stage 3 long-term memory certification.

## A note on cost and user control

The offline core uses Python's standard library and SQLite. Users may need to install Python from a trusted source; they should not copy unexplained shell commands into terminals. Online AI assistants, coding agents, and optional models have independent pricing, subscriptions, privacy and licensing terms. This free prompt does not provide free access to those services.

**For a simpler workflow:** a handoff file in a local Git project plus a short `AGENTS.md` or `CLAUDE.md` is often enough to avoid repeating background context. Our added value is **negative testing, evidence and authority control**, not merely persisting text.
