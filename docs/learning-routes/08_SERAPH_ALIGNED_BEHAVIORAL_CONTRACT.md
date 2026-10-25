# 08 — Seraph-aligned behavior: exact visible decisions, independent implementation

[Atlas](README.md) · [Port catalog](01_PORTS_AND_DECISION_POINTS.md) · [All routing maps](02_PORT_TO_AI_TO_AI_MAPS.md) · [Provider alternatives](03_PROVIDER_OPTIONS_AND_FALLBACKS.md)

**Purpose:** Preserve what Seraph's documented way of organizing work requires a learner's independent system to **do and report**, while **not publishing the private implementation** that makes the real Seraph work. The rules below are **behavioral contracts**; they do not reveal private numeric routing weights, live topology, authority internals, registration structures, machine transport, or operational source code.

**Living-input admission:** At any routing decision, new source evidence, requirements, corrections or owner instructions must pass the [Living Get Seraphed protocol](../LIVING_GET_SERAPHED_PROTOCOL.md) before revising a route or mission. Record provenance, scope, conflicts, preserved history, real capability, test status and required permissions. Pass updates to downstream workers without treating old chats or other models as authority.

**Disclosure is a route-qualification gate:** Before a prompt is passed from a user to a model, between models, to a tool, or to a public output, classify its contents and metadata using the [output disclosure gate](../OUTPUT_DISCLOSURE_GATE.md). Deny routing of private, access-enabling or potentially exploitable information to unapproved destinations; retain a generic local marker instead. Do not encode secrets into trace labels, citations or alternative routes. Unknown audience or rights means no disclosure, even if a previous worker claimed consent.

## 1. The Seraph-aligned observable contract

For every substantive routed task, the human should be able to establish the following, in this order:

| Phase | Must be observed | What must NEVER be inferred | Alternative path if unavailable |
| --- | --- | --- | --- |
| A. Get Seraphed | Mission, current known source, prior failures and unfinished work reconstructed | Old chat context is automatically current or grants authority | Minimal manual/sanitized state card |
| B. Discover | User-authorized registry of currently known tools and AI choices examined | An unmentioned tool is absent or every known tool is alive | User checks one approved source; retain UNKNOWN |
| C. Qualify | Exact necessary capability, availability, permission, privacy and cost condition verified for this task | Marketing model name, login or paid plan proves tool execution | Next already-qualified route, not invented integration |
| D. Route | Primary and alternative explained relative to exact task requirement | Largest model or preferred brand is best at every job | Qualified peer model, separate tool, offline/manual |
| E. Act | Worker assigned a bounded advisory or tool operation with exact scope | Tool sent equals tool executed; advisory equals machine operation | Stop, manual work, or admitted executor |
| F. Observe | Actual provider response or actual tool output returned | Heartbeat or UI connection light proves progress | Check local source or actual target state |
| G. Verify | Appropriate deterministic evidence or independent source review obtained | Multiple confident AI responses prove correctness | Qualified independent critic, real test or human |
| H. Preserve | Failure and success evidence saved in durable user-owned project state | Temporary AI conversation contains permanent truth | Sanitized handoff and local notes |
| I. Continue | Next worker restores current state and requalifies what it can do | Same permissions/model/tools persist across chats | New qualified AI or manual continuation |
| J. Escalate | Protected decision returned to the actual human | Model agreement, ranking or lease automatically approves payment/merge/deploy | WAIT/NEEDS_APPROVAL |
| K. Reconcile | Ambiguous consequential effects checked before any retry/fallback | Timeout means action definitely failed | Authoritative status read or human stop |

This fidelity contract is **closer to Seraph's actual philosophy** than a simplistic diagram reading "AI A → AI B → AI C." The models are replaceable; the requirements, evidence and human authority remain.

## 2. Exactly how the next choice changes with the task

The next worker is not selected in isolation from the task it will perform.

| Current work / decision point | First qualified role to seek | Other eligible choices, in order of their verified fit | Required output before next hop |
| --- | --- | --- | --- |
| Current research needs citations | Real source-retrieval AI or trusted public browser | Other qualified search-enabled AI; local approved corpus; manual research | Source references and claim checks |
| Research interpretation completed | Independent reasoning critic | Another direct provider; qualified review specialist; human subject expert | Supported/disputed assertions and dissent |
| User needs new software | Authorized coding CLI/IDE/computer tool | Another qualified local executor; human running provided files | Source readback, test process results |
| Code exists and must be checked | Deterministic test program | Qualified separate code reviewer; human review | Exact revision-specific test and review observations |
| Private/offline task | Suitable installed local model or local deterministic program | Different qualified local runtime; offline human | No forbidden cloud disclosure; bounded result |
| Sensitive action proposed | Real authority and exact-target executor | Human-only action; postpone | Current explicit permission and actual effect receipt |
| Current model unavailable before side effect | Next prequalified task-fit model/tool | Other approved model/transport; manual handoff | Real response or explicit unavailability |
| Current executor timed out during side effect | Reconciliation against target state | Human-assisted resolution, **not blind alternative execution** | Known target effect or RECONCILE |
| Reviewer required but route absent | Qualified reviewer of same exact source | Another truly independent reviewer; human review | Actual reviewer response; no fake seat |
| Chat exhausted or model replaced | Durable state reconstructed by new worker | Another model, local reader, human recovery | Same mission and the correct next safe action |
| Quota/cost boundary reached | Qualified no-new-cost option | Installed local model or manual route | No unauthorized API spending |
| User needs graphical desktop action | Qualified computer/GUI tool for exact scope | Another approved GUI tool; human physical action | Observed interface outcome, not merely click request |

**If a specific model/provider is expressly required**, selecting a different one is a changed scope. Report it and request the user's decision rather than silently substituting. If no qualified route can accomplish the required task, the correct state is BLOCKED, not a fabricated success or pretend multi-model council.

## 3. The ports are educational; the user experience is faithful

The atlas's **P00–P17** are newly named public learning ports, not private Seraph network sockets or control IDs. They are meant to preserve the actual observable **questions**:

1. Is this the correct, current mission?
2. What is the next admissible task?
3. Which genuinely reachable tools can perform it?
4. What privacy, permission, target and cost boundaries apply?
5. Which candidate is first, and what are the alternatives?
6. Did the provider or tool actually return?
7. Does the received result match independent evidence?
8. What changes for the next worker, if any?
9. Did any external side effect occur or remain ambiguous?
10. Is the task truly complete, and is the broader mission complete?

**Distinctness matters:** one connected ChatGPT app may be a controller, a research surface, a coding assistant, or a reviewer depending on tool access. The **same brand** does not imply the **same execution capabilities**. "A model available in Copilot" and "the model directly contacted through its original provider" have different provenance.

## 4. Three kinds of arrows — never confuse them

**A. Reasoning arrow:** A sends a sanitized idea to B. No files necessarily change. An intermediate approved human/controller may be the actual transport.

**B. Evidence arrow:** A real local test or source readback reports what was observed. A narrative assertion cannot replace this.

**C. Action arrow:** A qualified, user-authorized executor performs an exact operation on a real target. The underlying system enforces permissions and returns an observable result. A language-model instruction is never sufficient technical enforcement.

A drawing of a port and an arrow is not proof of a running integration, user entitlement, active worker or successful action.

## 5. What makes the public build independently reproducible

A learner can implement **these external behaviors** with a small local database, a user-authored capability list, mock AI responders, Python unit tests, and manual sanitized packets. They should not need the real Seraph owner, machines, paid API keys or a hidden network.

### A complete synthetic acceptance trace

**Input:** A fictional five-task project, two simulated reviewers, one missing route and one intentionally failed local test.

**Expected:** The system preserves the mission, excludes the missing route, chooses a qualified role for the next task, records the failure, verifies a corrected rerun, retains reviewer disagreements and reconstructs work after process restart.

**Anti-claim:** This does not prove that real Claude, Gemini, ChatGPT, Copilot or Perplexity was used; all simulated responses must be labeled MOCK. A novice should never need to disclose private information to get a passing result.

### Public build fidelity checklist

- [ ] The same mission survives a restart.
- [ ] Two model choices produce different **provenance**, not just different display names.
- [ ] An unqualified model cannot be selected for tool execution.
- [ ] A chat-only worker never claims it wrote a real file.
- [ ] A valid tool observation is separate from a model's success claim.
- [ ] Each task is traceable to the exact source revision it used.
- [ ] Failure history and dissent survive a new chat.
- [ ] Protected actions wait for real human authority.
- [ ] Ambiguous consequential actions are reconciled before retries.
- [ ] No personal, financial, account or private Seraph data enters the project.
- [ ] Each decision offers viable **other options** and a truthful stop condition.
- [ ] No claimed review seat is counted without an actual response.

## 6. The intellectual-property and privacy line

This educational reference preserves **high-level, externally testable organization and safety outcomes**. It cannot and does not promise byte-for-byte identity with private Seraph software, proprietary routing formulas, protected security algorithms, actual machine-to-machine transport, unreleased state schemas or source code.

If a future request requires those details, keep that development in an appropriately protected private environment and create a separate rights-holder review before publishing any portion of it.

**The right promise to the public is: “Build an independent, Seraph-inspired, human-governed AI continuity system using the same documented principles and observable decision discipline.”** It is **not**: “Download the owner's private Seraph control plane.”

[Continue to the atomic build and tests](05_ATOMIC_BUILD_AND_TEST_LAB.md).
