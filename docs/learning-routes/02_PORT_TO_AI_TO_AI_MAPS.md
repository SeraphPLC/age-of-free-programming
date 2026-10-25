# 02 — Port → appropriate AI → next AI → evidence: routing maps

[Atlas index](README.md) · [Port catalog](01_PORTS_AND_DECISION_POINTS.md) · [Provider alternatives](03_PROVIDER_OPTIONS_AND_FALLBACKS.md)

**Interpretation:** The following maps preserve Seraph's **observable task-fit workflow and fallback discipline**, but are **generic routes for a reader's independent project**, not copies of private Mesh connections. A named service is a **possible choice only when that exact session, tool and capability are qualified, authorized, cost-admitted and currently usable**. Nothing below proves that the user has a subscription or that a provider was contacted.

**Who passes messages?** In most examples an approved controller or human transfers the packet. Ordinary AI web apps cannot be presumed to call one another. A drawn arrow denotes an **approved handoff of minimized information**, not a secret direct API connection.

## Map A — Public-source research and fact checking

~~~mermaid
flowchart LR
 IN["P00: Public research question"] --> G["Ground goal, freshness and source rules"]
 G --> R{"Qualified source retrieval?"}
 R -->|Yes| P["Research AI: Perplexity, Gemini, ChatGPT with search, or another verified route"]
 R -->|No| M["Manual public-source research or BLOCKED"]
 P --> E["Capture specific sources and retrieval dates"]
 E --> V["Separate critic: Claude, Gemini, ChatGPT, Copilot advisory, etc. if qualified"]
 V --> D["Deterministic source/claim cross-check"]
 D --> H["Human decides whether conclusion is adequately supported"]
 M --> H
~~~

**Primary eligibility:** Ability to retrieve and attribute relevant sources; fresh evidence; acceptable disclosure. Examples: an actually connected Perplexity research product, a qualified Gemini research environment, or a ChatGPT session with appropriate live web tools. **Other choice:** a browser operated by the human, with manual source notes. **Next AI:** a *different, actually reachable* reviewer with the **same sanitized evidence**, instructed to challenge claims rather than blindly agree.

**Atomic transitions:**
- Research worker produces claims + source references, **not** a verified final answer.
- Source checker verifies dates, source fit, independence and conflicting primary records.
- Independent reviewer marks SUPPORTED / DISPUTED / INSUFFICIENT with reasons.
- Human owns consequential publication or public allegation.
- If no retrieval route, manual research is more truthful than pretending a chat-only model searched the internet.

## Map B — Program construction from a user requirement

~~~mermaid
flowchart LR
 IN["P00: User's software objective"] --> D["Task decomposition; local project state"]
 D --> C{"Qualified coding tool and isolated test machine?"}
 C -->|Yes| B["Claude Code / Gemini CLI / Copilot CLI / Qwen Code / Kimi Code / approved computer tool"]
 C -->|No| H["Chat-only plan + manual files; no false build claim"]
 B --> F["Real source files + synthetic tests"]
 F --> T["Deterministic test process"]
 T --> R{"Independent review required?"}
 R -->|Yes| A["Separate qualified AI reviewer or human"]
 R -->|No| S["Save source revision and verified test evidence"]
 A --> S
 S --> O["Human approves any publication/deployment"]
~~~

**Primary choice:** The **coding surface with actual authorized filesystem and terminal capabilities**, not necessarily the most famous model. A model inside a normal web chat may be an excellent planner but cannot magically create local files. **Possible choices:** Claude Code, Gemini CLI, GitHub Copilot CLI/IDE, Kimi Code, Qwen Code, or eligible ChatGPT with a qualified computer connector.

**Other routes at the same point:** A compatible local coding tool with a licensed model, a human terminal operator, or chat-only copyable files. A lost remote tool connection should be re-evaluated against known eligible alternatives; do not tell the user the project is disconnected merely because one optional adapter failed.

**Next AI choices:** A different model qualified for source-code review, a bounded Copilot review feature for a live PR where permitted, or a human reviewer. Neither testing nor reviewing implies permission to merge or deploy.

## Map C — Private or offline-sensitive work

~~~mermaid
flowchart LR
 IN["Sensitive objective"] --> Q{"Can minimum data safely leave local environment?"}
 Q -->|No| L["Qualified installed local model / local Python tool"]
 Q -->|Yes, expressly approved| X["Qualified external model, with only needed redacted context"]
 L --> E["Local evidence and task state"]
 X --> E
 E --> K["Local verification"]
 K --> U["Human-owned decision"]
~~~

**Primary choice when data cannot leave:** A capable installed local model (for example a user-owned Ollama runtime with a suitable licensed model), or deterministic local software without an AI. **Alternatives:** Another approved offline model, entirely manual review, or BLOCKED. **Do not silently send raw data to a cloud provider** just because the local model is slower or less capable. User-specific cloud approval is a separate choice, and an external provider cannot be represented as "offline."

## Map D — A multi-model critique / independent frontier council

~~~mermaid
flowchart TD
 I["Sanitized exact input revision"] --> B["Controller: task, scope, expected independent critiques"]
 B --> P{"What real qualified independent provider seats are available?"}
 P -->|Only one| O["One real review + record missing seats"]
 P -->|Several| C["Send identical bounded packets to distinct verified providers"]
 C --> R1["Research-focused provider response"]
 C --> R2["Code or scientific critique provider response"]
 C --> R3["General adversarial reasoning provider response"]
 R1 --> E["Preserve each response and provenance"]
 R2 --> E
 R3 --> E
 E --> X["Compare evidence, disagreement and risks"]
 X --> T["Independent tests + human judgment"]
 O --> T
~~~

**Routing rule:** No fake five-seat participation. A single service selecting several underlying models may still create a **mediated provider trust boundary**; capture wrapper identity and the exposed underlying model, then judge independence honestly. A provider-managed Copilot response whose underlying model is undisclosed stays **model identity unknown**.

**Next AI choices:** Another direct provider where actually qualified; otherwise a local model as an explicitly supplemental check, *not* a substitute for a required independent external seat. A five-person "AI Council" role-play inside one AI chat is one AI response, not five providers.

**Stop:** If a task requires a particular model or minimum independent reviewer count, do not silently substitute a different model or count a blocked seat.

## Map E — Literature, education and document production

**Port:** Plain-language educational objective → permitted source discovery → AI outline/draft → independent content critique → deterministic spelling/link/reference checks → rights review → human publication gate.

**AI choices at source discovery:** Perplexity, Gemini or ChatGPT with verified retrieval capability, a public library database or ordinary manual browsing. **Drafting choices:** ChatGPT, Claude, Gemini, Kimi or an approved installed model. **Critique choices:** a different available model, subject-matter expert, or reviewer with source access. **Non-AI:** local document generator and reproducible formatting checks.

**Alternative paths:** When rights cannot be established, link to the source and write original explanations rather than copying; when any sensitive data appears, sanitize or restrict distribution; when no reviewer is available, label REVIEW_PENDING.

**Never infer** that AI-generated materials are licensed for redistribution or that a completed document equals a qualified publication.

## Map F — Visual understanding, images and multimodal observations

**Port:** A user-owned image or fictional visual problem → permissions and sensitivity review → model with **actual** image input support → optional second visual reviewer → source/measurement checks → human use decision.

**Possible models:** ChatGPT, Gemini, Claude or other verifiably vision-capable interfaces. **Alternatives:** User-written description, traditional image tools or manual observation. **Important:** A model describing something in an image does not establish real-world authenticity, a person's identity, or authority to publish someone else's photograph.

If no image transport is qualified, mark the model's vision ability unavailable **in the current route**, even if its product webpage says it supports images somewhere else.

## Map G — A protected real-world operation

~~~mermaid
flowchart TD
 T["Task proposes external effect"] --> C["Check exact target, human authority, current ownership, replay consequences"]
 C --> V{"All required controls demonstrably satisfied?"}
 V -->|No| S["HOLD / NEEDS_APPROVAL"]
 V -->|Yes| E["User-approved capable tool attempts action"]
 E --> R{"Exact external outcome independently observed?"}
 R -->|Yes| P["Record evidence and reconciliation"]
 R -->|No or uncertain| H["RECONCILE: inspect state, no blind retry"]
 P --> Z["Human confirms completion"]
~~~

**Examples:** Publishing a document, purchasing a service, sending a real customer email, merging a protected branch, changing account permissions or deploying code. **AI-choice is secondary**; protected operations require a capable underlying tool with independently enforced permission, exact-target and idempotency constraints. Chat-only AI output is advisory.

**Alternatives:** Another **already-qualified** execution route may be selected **only after ruling out uncertain external effects from the previous attempt**. A different model must not turn one unresolved payment attempt into two payments.

## Map H — Recovery from an exhausted or failed AI conversation

**Port:** Interruption, missing model, changed client, exhausted context → read durable mission record → discover last verified work → compare exact source revision → classify unresolved actions → choose any currently qualified successor AI → re-evaluate permissions → resume safe unfinished task.

**AI choices:** A new chat in the same provider, a genuinely different model, a capable local model or a manual reconstruction. **Not automatically inherited:** provider login, private repository access, machine identity, old approvals, working tool connection, outstanding payment authorization or a prior worker's memory.

**Next AI:** The chosen successor does not need to imitate the previous AI's personality; it needs the same **verified mission constraints** and a correct next action. If records cannot be read, report PARTIAL / BLOCKED, not "fully rehydrated."

## Map I — Computer access and tool failures

**Port:** Need local filesystem readback, code execution or GUI interaction → qualify existing user-owned tool.

**Typical options:**
1. An already-approved **local CLI or IDE tool** for code and tests.
2. A currently qualified **connected computer tool** for real terminal/file work.
3. A currently qualified desktop/GUI adapter when needed.
4. Another existing eligible option whose permission scope is appropriate.
5. Manual human action **after** qualified automated options are exhausted or an operation is inherently human-only.

**This ordering is a public learning example, not Seraph's actual private machine topology or priority ranking.** A failure of an optional GUI connector is not evidence that the local coding CLI, project source or AI reasoning is dead.

If the tool was modifying an external system when it failed, first reconcile the target's actual state. Switching adapters cannot erase uncertain side effects.

## Map J — Design or science hypothesis exploration

**Port:** Hypothesis → primary evidence search → explicit assumptions and alternative explanations → qualified model critique → deterministic math or external experiment plan → independent adversarial review → human interpretation.

**Candidates:** Source-capable Gemini, Perplexity or ChatGPT for discovery; Claude, ChatGPT, Gemini, Grok, Kimi, Copilot advisory or local models for separately scoped critique when available. **Alternative:** Researcher reviewing peer-reviewed papers and running local calculations. **Stop:** No experimental evidence means a hypothesis stays hypothetical; model consensus is not scientific validation.

## Map K — Small-business workflow organization

**Port:** Owner's objective → sanitized project binder → AI drafts and compares plans → local schedule/task tracker → optional external system integration only after human approval and qualified permissions → objective measurement of time/cost and corrections.

**Possible choices:** ChatGPT/Claude/Gemini for planning, a local model where privacy matters, coding assistant to build a local tool, Perplexity for public market research where qualified. **Next step:** the owner verifies facts and chooses the action; do not let one marketing AI automatically purchase advertisements or contact customers without authorization.

## The critical switch: provider choice and operation type

The **same model** might be useful for two tasks under radically different conditions:

| Scenario | Qualified route needed | What a successful response proves |
| --- | --- | --- |
| ChatGPT summarizes supplied synthetic text | Model chat | A written summary was returned |
| ChatGPT calls approved file tool | Actual connected computer/file capability | The observed file operation happened if readback confirms it |
| Claude reviews a design | Claude advisory session | Claude returned a critique |
| Claude Code modifies local program | CLI, OS permissions, bounded project scope | Files changed; tests still need execution |
| Gemini web discusses Python | Web chat | Advice, not executed Python |
| Gemini CLI builds Python | Actual CLI with approved local environment | Local code/test outputs exist if observed |
| Perplexity Search cites a page | Source-capable Perplexity search route | An attributed response, subject to source verification |
| Perplexity Computer performs hosted work | User-authorized cloud computer | Cloud-side result, not arbitrary local-machine access |
| Copilot code review comments on PR | Verified review-only action | Review comment, not source mutation |
| Copilot coding agent edits source | Separately authorized coding action | Candidate source change requiring checks |
| Ollama runs installed model | Local inference route | Local model response; not an independent cloud frontier seat |

## Every arrow requires an answer to four questions

1. **Who really received the packet?** Provider, model when known, wrapper, tool and session.
2. **What actually crossed the boundary?** Sanitized text, references, file bytes or no data.
3. **What real permission covered this action?** None for advice; explicit permission for tool use; separate authority for protected side effects.
4. **What evidence came back?** Raw response, observed test exit, source/reference check, explicit failure or no response.

These maps provide a faithful **functional routing discipline**. They do not claim that every named provider is currently connected or that their direct invocation is equivalent.

Continue with [route admissibility and fallback options](03_PROVIDER_OPTIONS_AND_FALLBACKS.md) and [handoff evidence](04_HANDOFF_EVIDENCE_AND_RECOVERY.md).
