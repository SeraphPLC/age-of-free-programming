# 01 — Entry ports, decision gates, and output ports

[Routing atlas](README.md) · [Provider alternatives](03_PROVIDER_OPTIONS_AND_FALLBACKS.md) · [Recovery](04_HANDOFF_EVIDENCE_AND_RECOVERY.md)

**Scope:** This is a public reference model of the **observable Seraph-aligned workflow**, not a copy of private port mappings, wire protocols, security policies, schedules, or connection identifiers. "Port" means an abstract interface or stage; it does **not** mean a published TCP/UDP socket. A browser chat, file, local CLI, HTTPS API, and MCP tool are different surfaces.

## 1. Three physical ways a user can enter

| Input category | Observable entry | What the user controls | When to use | Alternative if unavailable |
| --- | --- | --- | --- | --- |
| Manual chat | Ordinary AI website or app | The text they submit | Free planning, review, sanitized handoff | Another chat, offline notes |
| Local program | A user-owned process opening local records | Project working directory, code and installed model | Offline, private or deterministic tasks | Manual file inspection; no model necessary |
| Authorized tool connection | User-owned computer tool, coding CLI, eligible MCP connector, or approved API | Actual connector permissions, device, account and spending choices | Creation of real files, tests, bounded integrations | Qualified alternative tool; human action |

The destination must never be inferred just from a provider name. A subscription may exist without CLI, API, device pairing, specific model, current session, quota or cost authorization.

## 2. Port catalog — all visible decision checkpoints

At each port, the network either records a justified transition or stops. The status must survive a worker change. Paths after a STOP are **proposals**, not silent executions.

| Port | Receives | Admission requirement | Emitted signal | If blocked or unverified |
| --- | --- | --- | --- | --- |
| P00 INTAKE | New goal, authorized continuation request, or explicit restart | Human intent within scope | Mission candidate | Ask one essential, nonsensitive detail or HOLD |
| P01 PRIVACY | Incoming user/source data | Minimum necessary, appropriate destination | Redacted task context | Local-only handling or reject disclosure |
| P02 GROUNDING | Current approved project records | Source identity and freshness checked | Known/current/unknown distinctions | Cold recovery or stop with evidence gap |
| P03 TASK TYPE | Grounded mission and next work item | One defined deliverable and success criterion | Domain, risk, I/O needs, dependencies | Decompose; do not dispatch a vague mega-task |
| P04 CAPABILITY DISCOVERY | Registered user-chosen options | Inventory is inspected before probing | Candidate provider/tool list | Manual/chat-only path; do not invent a connection |
| P05 HARD ELIGIBILITY | Candidate routes | Capable, qualified, healthy enough, permitted, affordable | Eligible set with exclusion reasons | HOLD if empty; no marketing-name substitution |
| P06 TASK-FIT SELECTION | Eligible routes | Selection addresses this task, not generic leaderboard | One primary and conditional fallbacks | Human decision if equally viable and cost/privacy differ |
| P07 MODEL INPUT | Minimal prompt, sanitized evidence | Model/tool knows role and output expectation | Work request and audit reference | Narrow scope or choose another route |
| P08 NO-TOOL REASONING | AI response | Output clearly identified as advisory | Draft, critique, question, plan | Never call it a test or file mutation |
| P09 ACTION PREFLIGHT | Proposed external or local tool action | Real scope, current owner, target, replay safety, permissions | Permit/deny decision, not yet completion | Human approval or BLOCKED |
| P10 TOOL EXECUTION | Approved action | Execution environment independently enforces scope | Real tool observation | Failed or ambiguous outcome preserved |
| P11 RESULT INGEST | Response, file or tool output | Claimed producer and exact task identified | Unverified result candidate | Quarantine unsupported or mismatched content |
| P12 SOURCE VERIFICATION | Candidate result | Sufficient independent source or test evidence | VERIFIED / FAILED / UNKNOWN for bounded claim | Seek evidence, not persuasive consensus |
| P13 WRITE/STORE | Admitted evidence or correction | Local owner-approved destination; private data minimized | Durable record and readback | Preserve candidate pending safe storage |
| P14 REVIEW CHOICE | Result requiring scrutiny | Independent reviewer needed for task/risk | Review request or reason for no review | Local tests and explicit human review |
| P15 SECOND WORKER | Sanitized review packet | A qualified separate route; same exact revision | Independent critique and provenance | Mark unavailable, never invent participation |
| P16 RECONCILIATION | Disagreement, stale state, ambiguous external action | Actual state checked before any consequential repeat | Corrected conclusion or BLOCKED | Escalate to operator |
| P17 CONTINUITY EXIT | Current state and next work | Compact complete status, source references, approval state | Sanitized handoff / next safe work | Incomplete handoff explicitly marked |

These are **fictional pedagogical port numbers**. They do not identify Seraph's actual control port IDs or private schemas.

## 3. The real order: discover → qualify → select → execute → verify

**Step 1 — establish the goal.** Capture purpose, constraints, accepted evidence, and what remains unfinished. A prior conversation is background, not unquestionable truth.

**Step 2 — inspect the capability inventory.** Find all *user-authorized* candidate interfaces already known. Do not run a connectivity test against every service on every start. An old reachable route remains known but is not automatically healthy today.

**Step 3 — filter hard exclusions first.** An interface lacking an essential capability, current qualification, appropriate privacy, session availability, or financial authorization is NOT SELECTABLE even if it would be extremely intelligent.

**Step 4 — compare viable interfaces for the actual task.** Prefer demonstrated task fit and minimal disclosure, then consider latency, reliability, human burden, durability and paid-entitlement value. This atlas intentionally publishes **no private Seraph weights or hidden ranking formula**. A user's independent router can use transparent, adjustable preferences.

**Step 5 — perform only the authorized operation.** A read-only model critique is different from a coding agent with filesystem write access. A named provider reached through an aggregator is different from the same provider's direct API. Preserve those differences.

**Step 6 — verify and advance.** Tool dispatch is not execution; executed action is not independently verified success. Save actual observations with source revision and route provenance. Stop or reconcile before changing providers if the preceding action may have caused external side effects.

## 4. Allowed branch outcomes

Each port should produce one of these **public reference statuses**:

| Status | Meaning | May promote to completed work? |
| --- | --- | --- |
| READY | Prerequisites satisfied; eligible to consider | No |
| SELECTED | A route was chosen | No |
| DISPATCHED | An attempt was issued | No |
| OBSERVED | A response or effect was actually read | Not by itself |
| VERIFIED | Exact bounded acceptance evidence passed | Yes, only within verified scope |
| FAILED | A test or execution definitively failed | No |
| UNAVAILABLE | Route could not be reached or lacks required entitlement | No |
| UNQUALIFIED | Ability or independence was not established | No |
| RECONCILE | External consequence may have occurred; outcome uncertain | No — do not blindly retry |
| NEEDS_APPROVAL | Protected authority not established | No |
| BLOCKED | No safe current route exists | No |

An AI cannot promote its own prose from DISPATCHED to VERIFIED. No idle worker, heartbeat, saved chat, or green UI light is a proof of useful progress.

## 5. Generic data contract for one public reference signal

**Illustrative interface, not Seraph's private data schema.** Use synthetic IDs and redact all private values before crossing an AI-provider boundary.

~~~json
{
  "demo_schema": "community-route-signal-v0",
  "mission": "fictional-library-assistant",
  "work": "check-draft-against-public-sources",
  "source_revision": "demo-revision-2",
  "input_class": "sanitized-public-text",
  "required_ability": "source-backed-critique",
  "route": "provider-selected-after-qualification",
  "transport_class": "manual-chat-or-approved-tool",
  "action_scope": "read-only-advisory",
  "state": "READY",
  "evidence_reference": "local-synthetic-record",
  "next_when_verified": "independent-review-or-human-decision"
}
~~~

No OAuth token, cookie, secret URL, raw logs, user hostname, IP address, private project path, or financial account field belongs in a public packet.

## 6. Example of a stopped transition

**Scenario:** A user has an active subscription to a research AI, but the browser account is signed out and there is no tested API connection.

- P04 knows the provider as a **candidate**.
- P05 rejects it for this specific automatic dispatch due to missing current invocation qualification.
- P06 checks other qualified user-approved options, such as a different already-connected research client or manual browser research.
- If no eligible source-access route exists, the work stays BLOCKED or becomes a manual handoff.
- The system must **not** claim the paid subscription proves a working API, borrow another service's credentials, or fabricate a response from the requested model.

**Failure and fallback are separate from the task mission.** A temporary tool problem does not erase the mission, and a new worker cannot grant itself permission to repair the environment by accessing unrelated accounts.

## 7. Minimal interface acceptance tests

1. Unknown user goal does not create an executable work order.
2. Private information crossing an unapproved boundary is denied before dispatch.
3. Stale route is not labeled healthy without appropriate evidence.
4. Subscription-only route without invocation qualification is excluded.
5. A failed primary chooses another **already-qualified** compatible candidate, not a newly invented connection.
6. No qualified candidates causes BLOCKED, not silent downgrade.
7. A no-tools AI response can never produce a fake filesystem receipt.
8. A tool action with ambiguous external consequences enters RECONCILE, not immediate retry.
9. The successor recovers the same decision and evidence source without inheriting past approvals.
10. A final handoff distinguishes proven facts from model suggestions.

See [port-to-provider examples](02_PORT_TO_AI_TO_AI_MAPS.md) and the [synthetic test lab](05_ATOMIC_BUILD_AND_TEST_LAB.md).
