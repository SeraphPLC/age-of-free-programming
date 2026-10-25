# The simplest useful continuity system

You do **not** have to build a full AI OS to get much of the value.

Create an ordinary local folder for a **fictional** project containing `MISSION.md`, `HANDOFF.md`, `DECISIONS.md`, and `FAILURES.md`. Keep the contents out of cloud chats unless redacted. If you already use Git, version the nonprivate instructions and preserve a clear revision. Never commit secrets, medical/financial records, credentials, real databases or personal task logs to a public repository.

Use [Stage 0](../prompts/stages/00_CHAT_ONLY_CONTINUITY.md) to have an AI produce a state card. A new AI can read that card and say what it knows and what is missing. If you use a coding agent that supports repository instruction files, you can adapt these **generic templates** to your own local project: [AGENTS example](../templates/AGENTS.example.md) or [CLAUDE example](../templates/CLAUDE.example.md). Neither template automatically installs an agent, changes permissions, or connects to any publisher.

**Tradeoff:** This simple setup saves context and helps with handoffs, but does not solve concurrency, event tampering, source-backed memory recall, robust recovery, or audits by itself. Add those only if they improve your specific use case; [staged software builder](STAGED_BUILD_PATH.md) is for people who need the extra correctness.
