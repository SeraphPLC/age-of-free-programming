# 03 — Task-fit selection: AI, transport and fallback options

[Atlas](README.md) · [Eleven route maps](02_PORT_TO_AI_TO_AI_MAPS.md) · [Provider setup](../FRONTIER_AI_ACCESS_METHODS.md)

This document shows **how a reader's independent router can make the same kinds of decisions that Seraph's documented philosophy requires**, without exporting the private ranking weights, connection graph, control-plane algorithms or current provider entitlements.

## 1. A fixed order of decisions, not a fixed "best AI"

**Never start by picking the model with the most impressive advertising.** Start with the actual task, its exact constraints, and the currently available qualified routes. Different interfaces exposing the same brand may have entirely different permissions.

The public decision order is:

1. **Recover mission context:** current source, next legitimate task, known failures, earlier verified decisions.
2. **Classify work:** source research, software coding, formal code review, scientific analysis, document drafting, visual interpretation, local processing, approval-required action, restart, or other bounded domain.
3. **Classify sensitivity:** public synthetic, private local-only, user-permitted external redaction, protected side effect.
4. **Discover known alternatives:** user-provided registry of apps, CLIs, connectors, locally installed tools, and manual options; no scan of private device/account data without permission.
5. **Apply all hard gates:** exact capability, implementation, current qualification, adequate liveness evidence, acceptable data destination, owner permission, current work ownership, cost/entitlement and replay safety.
6. **Compare only eligible routes:** task success evidence, privacy, durability, operator effort, latency and approved cost. Do **not** publish or infer private Seraph numeric scoring.
7. **Select one bounded route:** label all alternatives and why they were not selected. Before dispatch, verify the exact tool/action mode.
8. **Execute or request advice:** record real outcome; never turn a planning result into an execution receipt.
9. **Verify independently:** run real deterministic tests/source checks or obtain qualified external criticism.
10. **Fallback safely:** retry with a compatible qualified option only when the prior operation cannot cause unrecognized duplicate consequences; otherwise RECONCILE.
11. **Persist evidence and handoff:** new worker reconstructs from durable state, not the prior model's self-description.

**Critical invariants:**

- Known route ≠ currently healthy route.
- Purchased subscription ≠ active API or a qualified tool session.
- Connected ≠ authorized.
- Qualified worker ≠ permission to publish.
- Dispatch ≠ observed execution.
- Heartbeat ≠ material progress.
- Hash match ≠ independent correctness.
- Model agreement ≠ source proof.
- A different model name inside one intermediary ≠ independent provider execution.
- Every missing external review remains missing, even when the user asked for a larger council.

## 2. Model-family suitability versus actual route qualification

Each row represents a **possibility**, not an active connection.

| Provider/family | Plausible best-fit task | Possible direct entry | Other option at this point | Reason to exclude |
| --- | --- | --- | --- | --- |
| OpenAI / ChatGPT | General planning, writing, coding advice, multimodal, available web/tools | Official ChatGPT client; supported computer tool; separate API | Claude, Gemini, local model, Copilot advisory | Current session lacks tool, no approved data disclosure or spend |
| Anthropic / Claude | Long-form analysis, code reasoning, substantive critique | Claude chat, Claude Code, supported MCP, separately approved API | Copilot advisory, Gemini CLI, ChatGPT, Qwen/Kimi coding tool | Requested direct Claude route not actually qualified; wrapper cannot be relabeled |
| Google / Gemini | Research, multimodal tasks, structured long-context critique, coding CLI | Gemini app, Gemini CLI, separate API | Perplexity research, ChatGPT search, Claude review | Model/tool availability unverified, sensitive data destination, API cost |
| Perplexity | Attributed public-source discovery | Official Perplexity Search/Research, eligible Computer, separate API | Gemini/ChatGPT with actual search, manual browsing | Paid Pro plan alone not evidence of usable automated invocation |
| GitHub Copilot | Repository-facing code advice, qualified review, local CLI/IDE development | Eligible CLI/IDE; separately qualified PR-review action | Claude Code, Gemini CLI, independent human reviewer | No specific PR or wrong action mode; hidden underlying model identity |
| Microsoft Copilot | General personal/work assistance under Microsoft permissions | Copilot web, organizational M365/Studio route | ChatGPT, Claude, manual office workflow | Corporate workspace rules prevent tool use; not a local shell by default |
| xAI / Grok | Alternative critique, questioning assumptions | Grok app; approved xAI API | Claude, Gemini, ChatGPT, Kimi | No actual call, consumer chat lacks machine action, spend blocked |
| Moonshot / Kimi | Long-context drafting, reasoning or coding via Kimi Code | Kimi app, Code CLI/desktop, separate API | Claude Code, Qwen Code, Copilot CLI | Wrapper identity unknown, model capability not qualified |
| Qwen | Coding assistant or suitably licensed local model | Qwen website, Qwen Code, local licensed model | Kimi Code, local Ollama, Gemini CLI | Model installed? correct version/license/terms? actual test result? |
| Ollama / local models | Local inference without cloud submission when configured | Local CLI/loopback on user machine | Another installed local model, deterministic code, manual review | Insufficient hardware, context, capability or unavailable model |
| Deterministic Python/SQLite | Ledger, parsing, verification and tests | Local Python process | Manual audit, other deterministic program | Not a substitute for judgment or frontier research |
| Human/operator | Source judgment, irreversible approvals, contextual decisions | Direct human review | Delay, manual specialist, qualified professional | Cannot be silently replaced by a model for protected decisions |

**Provider wrappers:** The "actual route" may be a product that offers underlying models through a broker. Record both. If underlying model is not exposed, say unknown rather than assigning a name. Provider independence and execution truth require actual separate responses.

## 3. Preferred paths, alternate paths and stop conditions

The **examples are original public suggestions**. The preferred choice is **conditional on proven capability**, not a prediction about someone's accounts.

| Task and constraint | Conditional first consideration | Second choice | Third/manual choice | Mandatory stop |
| --- | --- | --- | --- | --- |
| Public-source research | Qualified search-oriented service (e.g. Perplexity) | Qualified search-capable Gemini or ChatGPT | Human verified browsing, public library | No sources available; don't fabricate citations |
| Software build with file access | Current authorized local coding CLI/IDE | Qualified computer connector in an isolated environment | Human terminal and copyable files | No authorized write route; don't claim installation |
| Deep code critique without tools | Qualified independent Claude/Copilot/Gemini/ChatGPT reviewer | Different real model/family | Human code reviewer | Required specific reviewer unavailable; label gap |
| Exact repository PR review | Provider-managed PR-review surface specifically qualified for that PR | Qualified local diff review + human | Separate source-aware independent reviewer | No live verified PR identity or review action approval |
| Strictly local sensitive task | Suitable installed local model or deterministic tool | Another qualified local runtime | Human offline process | Confidential input cannot leave; no unsafe cloud fallback |
| Visual desktop task | Approved GUI-computer tool for exact device | Another qualified GUI adapter | Human physical interaction | No GUI access; do not infer screenshots or clicks |
| Generic document draft | Available text model + local text editor | Another text model, template | Human manual writing | Missing source rights or unapproved disclosure |
| Five independent reviews | Real separately qualified providers with responses | Fewer real reviews explicitly labeled | Human expert and unresolved seats | Do not simulate count or silently substitute |
| High-consequence financial/account action | Exact approved underlying application + human authority | Manual user action | Don't proceed | Unknown outcome, wrong target, unauthorized spending |
| Exhausted chat continuity | Current durable local/repo state + new qualified AI | Different AI, manual handoff | Human source reconstruction | Unknown critical state; do not assume completed |
| Budget or quota exhausted | Another qualified no-new-spend route for the same task | Local/offline route if appropriate | User approval for new spend | New cost has not been approved |
| Model/service changed | Re-evaluate current provider model/tool and rerun task-scoped checks | Existing qualified alternative | Safe read-only/manual route | Old qualification no longer valid for this exact capability |

## 4. Four orthogonal dimensions of "the next AI"

A successor selection is only legitimate when all four questions have answers:

**A. Capability:** What is the next *specific* responsibility? Source retrieval, drafting, coding, critique, image interpretation, or an exact tool action? A research model and an executor are not interchangeable.

**B. Identity/provenance:** Was the response delivered through a direct provider, a provider-managed wrapper, an IDE, a browser, or a local runtime? If that route hides the underlying model, independence remains UNKNOWN.

**C. Authority:** Was it read-only advice, a real file mutation, an external-system mutation, or publication? A model response cannot self-grant tool privileges. Permission must be enforced by the actual executor and scope.

**D. Evidence:** Did the requested action complete according to an independently observed acceptance check? If a tool did not run, this is planning, not execution. If an external side effect is uncertain, it is RECONCILE, not FAILED-SAFE-TO-RETRY.

## 5. How to make the public registry transparent

Readers may write a **small, local, user-controlled capability list**. The following is fictional and does not disclose Seraph's own registry design:

| Local display name | Tools confirmed in this user installation | Privacy posture | Current check | Decision for synthetic task |
| --- | --- | --- | --- | --- |
| Example-A research chat | Web search with source links | External AI, synthetic/public only | Observed in this session | Eligible for public research |
| Example-B code CLI | Write local project files, run Python | Local executor; AI model may be cloud | Test tool passed in isolated VM | Eligible for synthetic coding |
| Example-C model | Chat only, no tool privileges | External AI, synthetic only | Login known, execution untested | Advisory only; not code execution |
| Example-D local model | Offline inference after installation | Local | Model unavailable | Not selectable |
| Example-E human | Manual review and explicit authorization | User owned | Available when asked | Protected decision only |

The implementation should **not** embed private access tokens in the registry. It should refer to user-approved credential storage without exposing or copying the secrets to AI workers.

**Do not hard-code a single route as permanently best.** An option can be excellent for one task and ineligible for another. Low cost never turns an unqualified route into a qualified one.

## 6. Failure-aware switching

| Failure observation | Correct interpretation | Next choice |
| --- | --- | --- |
| Provider says "model not available" before invoking action | Route unavailable | Consider different already-qualified model or manual |
| Remote machine tool quota exceeded before any operation | Optional adapter unavailable | Another qualified local tool/GUI route; do not call the whole Mesh dead |
| API key or login missing | Not connected/qualified | Use authenticated UI or another already authorized method, or ask human |
| Worker produced code but no test was run | Candidate source only | Run deterministic tests; no "PASS" label |
| Network timed out during a public-source search | Unknown response, but typically no consequential effect | Retry within limits or use qualified alternative with evidence of no side effect |
| Network timed out during payment, email send, publication | Outcome ambiguous | RECONCILE actual external state; **not** automatic alternate provider resend |
| Reviewer disagrees with another reviewer | Genuine dissent | Trace claims and evidence; no automatic majority victory |
| Local data cannot leave device | Cloud route forbidden | Qualified local tool or halt |
| Tool installed but not authorized for file write | Read-only capability | Plan/critique, never write |
| Chat session exhausted | Worker lost context | Reload durable state, requalify task-specific route/authority |

## 7. A route score is not an authorization mechanism

A public independent router *may* maintain a readable, user-editable preference ordering, such as:

**Exact ability and evidence of success → privacy/data minimization → continuity → reliability → user burden and approved cost.**

Treat that as an **illustrative ranking rubric, not Seraph's original private numerical weights or selection algorithm**. Whatever prioritization a learner chooses, a failed hard gate removes the option; it must not be rescued by popularity, subscription perks, or ranking.

An expensive model with no real qualified tool cannot make a protected file change. An inexpensive local program with a real test may be more appropriate.

## 8. Optional red-team questions before release

- Does the route chooser ever silently change the model requested by the human?
- Can one wrapper response be counted as two independent providers?
- Can an unauthenticated API endpoint be described as "connected" because a browser is logged in?
- Can a model move a task to VERIFIED by writing the word PASS?
- Can a downstream worker inherit a previous worker's permission or secret?
- Can a failed payment/email dispatch be blindly repeated through another route?
- Can the router expose private context to a cheaper external provider without separate authority?
- Can a model with no source retrieval invent citations and still appear qualified?
- Are route failures preserved or erased when the router changes providers?
- Do automatic alternates stop when no safe eligible option exists?

Every question needs a **specific synthetic test and observed result**. A design document is not a test receipt.

Next: [handoffs and durable evidence](04_HANDOFF_EVIDENCE_AND_RECOVERY.md).
