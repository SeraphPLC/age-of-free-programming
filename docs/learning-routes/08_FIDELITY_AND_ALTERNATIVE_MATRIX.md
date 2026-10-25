# 08 — Seraph-aligned routing fidelity and alternatives, decision by decision

[Atlas index](README.md) · [Port catalog](01_PORTS_AND_DECISION_POINTS.md) · [AI-to-AI maps](02_PORT_TO_AI_TO_AI_MAPS.md) · [Provider choices](03_PROVIDER_OPTIONS_AND_FALLBACKS.md)

**Purpose:** Preserve the **observable Seraph decision discipline** at every handoff while helping independent users build their own system. The difference between fidelity and cloning is explicit: **the public behavior is described; the protected Seraph implementation is not disclosed.** This is not an exact copy of the private Mesh route registry, scoring weights, transport setup, operating topology, message format, private security rules, or privileged integration code.

## Fidelity legend

- **Behavioral invariant:** The rule a Seraph-aligned workflow is expected to follow.
- **Preferred path:** The first *eligible* task-fit action, **not a universally preferred brand**.
- **Alternatives:** Actual choices available at this same decision point; never infer connection or permission merely because listed.
- **STOP:** The condition where an ethical and technically correct system refuses automatic advancement.
- **Observable evidence:** What a new user should be able to check. These are generic acceptance targets, not a claim of tests run in private Seraph.

## Atom-by-atom fidelity matrix

| Decision atom | Seraph-aligned behavior | First eligible route | Other choices at this exact decision | STOP or unresolved case | Observable check |
| --- | --- | --- | --- | --- | --- |
| **R01 Begin** | Read actual goal and known state before selecting worker | Current locally saved mission | Sanitized user handoff, first-time synthetic goal | Conflicting mission instructions | Source-aware mission card |
| **R02 Discover** | Consult known route inventory before claiming no connection | User's already-known qualified tools | Explicitly discovered authorized alternatives | No relevant route inventory / no permission to inspect | Candidate list with freshness labels |
| **R03 Scope probe** | Refresh only task-relevant liveness evidence | Check exact needed capability | Reuse sufficiently fresh qualified evidence | Probe would access unauthorized account | Live result or UNKNOWN; no all-device sweep |
| **R04 Exact ability** | Capability is not generic brand reputation | Research tool for real sources; coding tool for real files | Human/manual tool if qualified | Route cannot actually perform required task | Rejected alternatives recorded |
| **R05 Implementation** | A feature named in a document may not exist in this installation | Verified installed tool or reachable supported service | Manual non-executing guidance | Feature only proposed, mocked or absent | Tool/version evidence |
| **R06 Qualification** | An option is not eligible until the exact operation is qualified | Proven, appropriately scoped route | Another tested equivalent | Only plan, login, marketing promise or old canary | Qualification proof for task |
| **R07 Current health** | Historical reachability is not current liveness | Current observed route | Reusable task-relevant health record | Connection health unknown and required | Fresh-or-valid observation |
| **R08 Entitlement** | Purchased/subscribed access is not API access | Included verified session within plan | Eligible alternative with known terms | API credential, quota or price unverified | Cost/source of entitlement noted |
| **R09 Privacy** | Data disclosure boundary is independent of model quality | Safe local or minimized external context | Human-only, genuinely offline local model | Required sensitive data cannot leave | Data classification and destination |
| **R10 Authorization** | Technical ability does not confer right to act | User-approved scope and tool-controlled execution | Draft-only advisory, human-performed step | Consent missing, stale, unrelated or denied | Current exact approval, not old chat memory |
| **R11 Worker ownership** | Parallel work must avoid conflicting changes | One owner for bounded write | Disjoint independent workers or read-only reviewers | Overlapping uncoordinated mutation | One acknowledged current owner |
| **R12 Select** | Task-fit among eligible routes, not fixed universal best AI | Highest supported task suitability within constraints | Next suitable qualified peer or explicit user preference | No route satisfies mandatory gates | Selection reason and exclusions |
| **R13 No-tools model** | Advice is not execution | Obtain answer/draft, label unexecuted | Real local tool or human terminal after approval | Model claims files created without tool | No false file/test receipt |
| **R14 Tool admission** | Read, edit and protected operations differ | Minimal permitted action | Keep as suggestion, request approval | Protected side effect lacks authority | Action class and scope |
| **R15 Provider provenance** | A platform/model wrapper is not direct independent identity | Record actual application and model if exposed | Record unknown underlying model | Identity or seat cannot be verified | Honest route identity |
| **R16 Dispatch** | Requested is not received | Actual supported provider/tool invocation | Manual packet transfer | Unsupported app-to-app connection | Dispatch event, not fabricated response |
| **R17 Observation** | Response is not automatically a verified result | Capture actual response/output | Inspect original file, test or source manually | No observable result | OBSERVED or NOT RUN |
| **R18 Evidence** | Claims require bounded checks | Reproduce test or inspect source | Independent qualified reviewer | No evidence for success | Version-bound verified result |
| **R19 Review** | Independent critique is real participation, not roleplay | Distinct qualified reviewer with same revision | Human specialist, deterministic test | Reviewer unavailable or same unverified backend | Actual returned critique, disagreements |
| **R20 Failure** | Preserve failed attempts and old evidence | Record failure and cause | Narrow repair task for qualified worker | A new worker tries to erase failure history | Durable negative record |
| **R21 Ambiguous effect** | Do not blindly retry potentially consequential writes | Reconcile actual external state | Human checks platform/account | Outcome cannot be determined | RECONCILE / BLOCKED, not repeated effect |
| **R22 Nonambiguous route failure** | Next already-known, already-qualified fallback | Next eligible compatible route | Manual or waiting path | New route would violate privacy/authority | Fallback selection and prior failure |
| **R23 New worker** | Restore mission from durable state rather than prior model identity | Fresh qualified session reading current records | Sanitized manual state card | Source revision/evidence missing | Correct recovery with no imported authority |
| **R24 Progress** | A heartbeat and an active process are not verified progress | Observable accepted task output | Explicit idle/blocked status | Merely “connected” or “still running” | Actual artifact and checks |
| **R25 Store** | Preserve evidence and source lineage outside AI chat | User-owned local records | Sanitized user-approved store | Storage not writable/verified | Write/readback or human-saved card |
| **R26 Human decision** | The owner governs high-stakes changes | Approval for precise text, operation and destination | Keep draft, postpone, refuse | A model announces authorization | Approved scope is explicit |
| **R27 Completion** | Mission ends only when requested bounded conditions verified | Tests and actual final state | Declare partial outcome with open items | Unverified conditions | Version-specific acceptance |
| **R28 Recovery failure** | A new chat cannot simply invent missing state | Seek minimal safe source evidence | Work read-only or remain blocked | No coherent state available | UNKNOWN honestly preserved |

**Interpretation:** The table is a *public generic comparison against documented functional principles*, not proof that all these private Seraph components are live or that these are the identifiers used in Seraph's implementation.

## The provider choice is different for every task

There is no permanently correct answer to "Which model goes next?" In a user-owned Community Edition, the next **eligible** route could differ even when the mission remains the same.

| Task family | Preferred *type* of worker | Other qualified choices | Real validator / next actor |
| --- | --- | --- | --- |
| Public fact finding | Search/research tool with accessible source receipts | Perplexity, ChatGPT Search, browsing-capable Gemini/Claude, official manual search | Source and date verifier; then independent reasoning AI if useful |
| Software implementation | Approved local file+terminal coding assistant | Claude Code, Gemini CLI, GitHub Copilot CLI, Qwen Code, Kimi Code, eligible ChatGPT computer tool, human terminal | Local Python tests; independent reviewer; human deploy gate |
| Read-only code review | Independent qualified code critic | Different provider family, verified Copilot PR review, human developer | Source checks and deterministic tests |
| Scientific hypothesis | Source-grounded specialist analysis | Qualified frontier model, manual literature review, independent domain expert | Factual critique, experimental design, human researcher |
| Protected personal work | Genuine local-only model or deterministic tool | Human-only handling, specifically approved redacted external request | Local check; private human decision |
| Image/document/audio | Appropriate proven multimodal or extraction tool | Another qualified visual model, human transcription for public nonsensitive data | Human or second model + original observation |
| Publication | Sourced draft, independent fact/privacy review | Multiple AI critiques, human editorial review | Human approval, authorized publication, verify public result |
| Model context exhausted | Fresh worker reconstructing saved source state | Another provider, manual card, local model | Real repository/file check, source-consistency test |
| Task timeout after consequential attempt | State reconciliation, not another model | Human verifies external status | No blind resend or duplicate operation |
| Provider quota exhausted | Already qualified equivalent within budget | Manual, offline model, pause | Privacy/cost and capability recheck |
| External advanced council | Truly independent, actually responding qualified external reviewer | Another provider, expert human, reduced review with missing seats labeled | Actual source/version and response receipt |
| Local routine council | User-approved installed local model(s) | Deterministic test, human peer | Do not relabel a local seat as external independent frontier review |

**Provider examples are options, not currently connected accounts.** Subscription, plan and API entitlements must be established by each person for their own environment. A model exposed through an aggregator may need its platform and backend provenance recorded separately.

## End-to-end map with explicit alternatives

~~~mermaid
flowchart TD
 A["Human mission / fresh chat"] --> B["Restore mission + source evidence"]
 B --> C["Discover user-owned route inventory"]
 C --> D{"Task constraints and mandatory eligibility satisfied?"}
 D -->|No| H["Manual safe path / HOLD"]
 D -->|Yes| E["Choose task-fit primary"]
 E --> F{"Actual tool action?"}
 F -->|No| G["Bounded model reasoning"]
 F -->|Yes| I{"Exact authority and privacy fit?"}
 I -->|No| H
 I -->|Yes| J["Real tool operation in user's approved environment"]
 G --> K["Capture actual result"]
 J --> K
 K --> L{"Evidence sufficient for bounded claim?"}
 L -->|Yes| M["Local evidence + source revision"]
 L -->|No| N{"Prior external consequence ambiguous?"}
 N -->|Yes| O["Reconcile before trying anything else"]
 N -->|No| P["Record failure; select next eligible fallback"]
 P --> D
 O -->|Unresolved| H
 O -->|Resolved| P
 M --> Q{"Independent review needed?"}
 Q -->|Yes| R["Next distinct qualified AI or expert"]
 Q -->|No| S["Handoff / complete task"]
 R --> T["Save disagreement + reverify changed artifacts"]
 T --> S
 S --> U{"Protected real-world effect?"}
 U -->|Yes| V["Human exact-scope approval and observed outcome"]
 U -->|No| W["Next task / end"]
 V --> W
~~~

The arrows depict conceptual handoffs orchestrated by the user or a user-approved controller, **not direct model-to-model network privileges**. If the current AI's browser chat cannot send a message to another AI service, the user may transfer a sanitized card manually; nothing in this diagram creates that integration automatically.

## Acceptance challenges for faithfulness

A local independent toy should demonstrate these cases **before** it claims to follow this public behavior:

1. A route can exist in inventory without current health evidence.
2. A purchased provider subscription with no callable tool cannot execute a task.
3. A model that can write text but not files is not a coding executor.
4. A new model may resume a mission but receives no inherited action authority.
5. A provider outage triggers the next already qualified alternative, not a random unqualified tool.
6. A protected external action with an uncertain outcome is reconciled, not replayed.
7. A lower-cost candidate that violates a privacy hard gate is excluded.
8. An unreturned reviewer is counted as zero independent reviews.
9. Two model names behind one intermediary are not presumed independent.
10. A successful write is distinct from a verified result.
11. A changed source revision invalidates stale test/review acceptance.
12. A chat closing does not erase failures or silently complete its remaining tasks.
13. A missing necessary capability produces BLOCKED/manual, not invented connection or fabricated success.
14. No selected route implies authorization without a separate actual user/tool decision.
15. A human approving a draft is not proof the draft was published.

These are **test proposals for the reader**, not results of an actual Community Edition software qualification. The [atomic build lab](05_ATOMIC_BUILD_AND_TEST_LAB.md) provides a larger synthetic test matrix; the [three-worker trace](07_THREE_AI_SYNTHETIC_TRACE.md) illustrates the same fidelity.

## The protected difference

A publicly reproducible **teaching exercise** can match the outward rules—mission persists, route eligibility is checked, alternatives are compared, evidence is verified, permissions stay human, interrupted work is recovered—without importing any of the original Seraph's proprietary protocol, private scoring constants, operational graph, live machine or provider identities, internal schemas, unpublished benchmarks, or security-control implementation.

**That is the closest useful public behavioral fidelity consistent with protecting the existing private Seraph and its operator.**
