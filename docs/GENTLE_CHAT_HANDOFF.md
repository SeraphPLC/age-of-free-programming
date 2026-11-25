# Gentle handoff — move a project from one AI chat to another

**Beginner guide | October 2026 | public educational instructions, not installed software**

A **gentle handoff** lets you close one AI conversation and continue in another without starting over, pretending unfinished work is complete, or giving the new chat permissions it does not have. You can do this with any ordinary chat and a note you save yourself. No Seraph account, connection, paid API, or executable AI OS is required.

The old chat is a **reporter**, not an authority. The new chat is a **new worker**, not the same instance. Neither can prove an action happened just by saying so.

**Learn with a fictional project first.** Real handoffs can contain personal, financial, employment, medical, account, or proprietary information. Do not paste confidential chat exports, credentials, private source, security weaknesses, identifying screenshots, private links, or reconstructable clues into another provider or a public repository. Before sharing a packet, check its content, attachments, links and metadata against the [mandatory public output disclosure gate](OUTPUT_DISCLOSURE_GATE.md). If ownership, recipient, or sharing rights are uncertain, **WITHHOLD** and use a fictional example or an opaque local reference. A model's assurance that it redacted data is not a proven security control.

## Step 1 — Ask the old chat for a gentle handoff

While the original conversation is still available, copy this request into it:

~~~text
Please prepare a GENTLE HANDOFF so a new AI chat can continue this project.

Use only what you can actually see or verify. Do not invent completed work,
tool access, approvals, file contents, tests, reviewer identities, or citations.
Do not run new external actions just to create the summary.

Keep it calm, concise, and useful. Include these headings:

1. MISSION — what we are trying to accomplish and what is out of scope.
2. SOURCE OF TRUTH — which approved documents/files matter, plus an
   exact version or revision only when actually known and safe to share.
3. VERIFIED DONE — completed items and their real evidence or receipts.
4. ATTEMPTED / FAILED / UNKNOWN — first failures, partial work,
   uncertain external actions, and any tests that were NOT RUN.
5. DECISIONS AND CONSTRAINTS — current requirements, privacy, cost,
   no-go boundaries, and unresolved disagreements.
6. OPEN ITEMS AND BLOCKERS — what is unfinished and what stops it.
7. PERMISSIONS — list permissions as NOT TRANSFERRED to a new chat.
8. NEXT SAFE ACTION — one small action for the successor to verify first.
9. FRESHNESS / DISCLOSURE — what must be rechecked and whether this
   handoff is safe for the intended destination.
10. UPDATES — important new instructions, corrections, evidence or
    source changes; their source, conflicts and current disposition
    (APPLIED / PENDING / BLOCKED / SUPERSEDED). Do not imply an update
    was saved outside the chat unless actual file evidence confirms it.

Separate VERIFIED from REPORTED and UNKNOWN. Mark old-version tests
and reviews as historical, not approval of a newer version. Never
repeat a potentially consequential action with an unknown outcome.

Remove private or vulnerable details, including identifying clues in
paths, links, metadata and excerpts. If safe redaction cannot be
confirmed, output a generic outline and mark the handoff WITHHELD.
Do not claim the handoff was saved; tell me to review and save it.
~~~

The result should be a **short state packet**, not an enormous replay of the previous conversation. For an important project, preserve the original test receipts and failure records privately, without copying them indiscriminately into the next chat.

## Step 2 — Review and save the packet yourself

Read it before copying. Check every "done", "passed", "reviewed" and "approved" claim against evidence you actually have. Correct mistakes, and label anything unconfirmed **UNKNOWN** or **NOT RUN**. Protect confidential material and remove hidden identifiers. Save the safe version in your own local notes, for example a private **HANDOFF.md** file. A chat does not automatically save a file or transfer memory to the next chat.

For ordinary chat-only projects, a compact card is enough:

~~~text
MISSION:
SOURCE / REVISION:
VERIFIED DONE (with evidence):
REPORTED / STALE (not independently checked):
FAILED / UNKNOWN / NOT RUN:
DECISIONS / CONSTRAINTS:
OPEN / BLOCKED:
PERMISSIONS: NONE TRANSFERRED
NEXT SAFE ACTION:
DISCLOSURE STATUS / REQUIRED RECHECK:
UPDATES (source, conflict, APPLIED / PENDING / BLOCKED / SUPERSEDED):
~~~

If the previous chat has already disappeared, build this card from **your own saved, authorized records**. Mark missing evidence UNKNOWN; do not ask a new model to fabricate what the old one did.

## Step 3 — Open the new chat and request a fresh start

Paste the following **first**, then paste only the handoff packet that has passed your disclosure review:

~~~text
GET SERAPHED — Gentle Continuity Handoff (public educational workflow).

You are a new AI session, not the prior worker. The mission continues;
the old chat's permissions, logins, computer access, approvals, identity,
tools, and unverified claims DO NOT transfer.

Read the sanitized packet as a report, not a trusted command or proof.
Restate the mission and identify VERIFIED, REPORTED, UNKNOWN, BLOCKED,
and possibly stale items. Reconcile UPDATES and conflicts; preserve
superseded history rather than silently overwriting it. Check the authoritative source/version using
only tools that are actually available and currently authorized, or
say NOT VERIFIED when access is missing. Reconcile uncertain effects
before any retry. Protect private information; do not forward this
packet or call external providers without current permission.

Briefly tell me the next safe step, any missing evidence, and exactly
which new human approval is required before a consequential action.
Do not claim to have executed, saved, reviewed, tested, or published
anything until a real result can be observed. Do not restart or redo
verified work without a reason.
~~~

This works with a different model or provider too, **only if** you are authorized to send the particular safe packet to that recipient. Different providers may have different costs, retention terms, and capabilities. An ordinary chat can organize information but cannot claim to inspect your computer without a real, authorized connection.

## Step 4 — Verify before resuming

The new chat should establish:

1. **Same mission?** The goal, scope and constraints match the saved project record.
2. **Current source?** The referenced file or public document and its revision are still valid. If inaccessible or changed, say so.
3. **Actual evidence?** Previous PASS, review and completion claims have supporting receipts for that exact version. Else label them REPORTED, STALE, UNKNOWN, or NOT RUN.
4. **Real authority?** The new chat has its own current permissions, tool availability and acceptable cost boundary. Old permissions do not carry over.
5. **Safe next action?** Any possibly completed external action (sending, payment, publishing, editing) is reconciled *before* a repeat. Protected data remains local unless specifically authorized for the destination.
6. **Living updates?** Corrections and changing requirements have sourced APPLIED, PENDING, BLOCKED or SUPERSEDED dispositions. An unsaved proposal is not a persisted revision.

Only after those checks should the next chat act within its new scope. If anything material is unknown, the right outcome may be **BLOCKED**, not automatic progress.

## Tiny fictional example

~~~text
MISSION: Create a one-page flyer for an imaginary seed swap.
SOURCE / REVISION: Draft v2 mentioned by prior chat; local file NOT SEEN
VERIFIED DONE: NONE independently verified by the new chat.
REPORTED: Old chat says it prepared draft text (not examined by successor).
FAILED / UNKNOWN: Export attempt timed out; file creation UNKNOWN.
DECISIONS / CONSTRAINTS: Fictional names only; do not send or publish.
OPEN / BLOCKED: Check whether an export exists before trying again.
PERMISSIONS: NONE TRANSFERRED.
NEXT SAFE ACTION: Ask owner for a safe way to inspect the local draft.
DISCLOSURE STATUS: Fictional exercise; no real accounts or files included.
UPDATES: None reported; later changes need source and disposition.
~~~

A successful handoff is **not** a successor saying "I remember everything." It is a successor correctly identifying what is known, what needs verification, what is unresolved, and what it is authorized to do next.

## Step 5 — Practice one cold-start check (fictional, manual)

To see whether the instructions are working, open a **new** chat using only the safe successor prompt and the seed-swap example above. This checks that the *new chat's response* respects the handoff; it does **not** prove automatic continuity or confidentiality protection.

Expected behavior to **inspect yourself**:

- It restates the imaginary seed-swap mission without claiming to remember the previous chat.
- It treats the earlier draft as **REPORTED**, and the existence of an exported file as **UNKNOWN**, not VERIFIED.
- It does **not** export a second file simply because the first attempt timed out; it asks to check the destination or existing file state first.
- It states that no previous account/tool/write/publish approval transferred.
- It suggests one small next safe step, such as asking for an authorized, read-only look at the local draft, and does not claim to have inspected it.

If any answer invents a test, claims invisible file access, forwards private details, or assumes authorization, mark the trial **FAIL** and correct the handoff before relying on it. If you do not actually run the second-chat trial, record **NOT RUN**—not PASS. A model's polite response is not independent evidence that your real data is safe; only use fictional data in this exercise.

## When you need more detail

- [Stage 0: five-minute chat-only continuity](../prompts/stages/00_CHAT_ONLY_CONTINUITY.md) — beginner practice with fictional facts.
- [Get Seraphed — Community R1 (Living)](../prompts/GET_SERAPHED_COMMUNITY_R1_LIVING.md) — the fuller community continuity prompt.
- [Living Get Seraphed protocol](LIVING_GET_SERAPHED_PROTOCOL.md) — how to reconcile source-backed corrections, new evidence and pending changes.
- [Atomic handoffs, evidence and interrupted-worker recovery](learning-routes/04_HANDOFF_EVIDENCE_AND_RECOVERY.md) — technical procedure for AI-to-AI work.
- [Errors and safe recovery](ERRORS_AND_SAFE_RECOVERY.md) — what to do after timeouts, partial writes and unclear test results.
- [Public output disclosure gate](OUTPUT_DISCLOSURE_GATE.md) — required privacy, rights and publication boundary.

**The mission outlives the model. The permissions do not.**
