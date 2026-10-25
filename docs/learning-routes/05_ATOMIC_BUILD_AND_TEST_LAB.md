# 05 — Atomic build and test lab: your own local AI routing prototype

[Atlas](README.md) · [Ports](01_PORTS_AND_DECISION_POINTS.md) · [Alternatives](03_PROVIDER_OPTIONS_AND_FALLBACKS.md)

**Purpose:** Convert the public functional maps into a **small, independent learning project** that a novice can build with their own AI and computer. This document is an implementation **assignment and acceptance plan**, not an installation script, published source-code release, protected Seraph routing algorithm, or claim that these tests have been executed on the reader's machine.

Do not copy Seraph's private code, schemas, node identifiers, internal protocols, control plane, privileged hooks or unpublished benchmarks. Use **fictional inputs** and ordinary publicly known engineering practices. This is a clean-room educational prototype with **the same intended observable decisions**, not an exact private implementation clone.

## 1. A correct minimal success case

The beginner should be able to start a completely fictional five-task project using local files and Python, choose among a few **simulated** AI/tool roles, reject options that lack prerequisites, preserve a failed attempt, pass the unfinished task to a fresh simulated successor, and demonstrate that the next valid task is chosen from durable state.

**Prohibited claims:**
- A simulated provider response is **not** a real Claude/Gemini/ChatGPT/Perplexity/Grok response.
- A script showing SELECTED or ATTEMPTED does **not** prove the external AI executed.
- A fake local approval object is not proof of a person's identity or real spending authority.
- Passing a toy test does not qualify a production Seraph Mesh.
- The project must not contact actual customer accounts, real payment APIs, personal documents or private source.

## 2. Suggested learner-owned directory layout

These are **new, invented educational filenames** chosen for readability. They are not Seraph's private filesystem layout or schema.

~~~text
Seraph-Learning/
  README.md                    # Your own mission and safety rules
  requirements.txt             # Blank if using Python standard library only
  state/                       # Local-only records; never publish
    project.sqlite             # Fictional missions/tasks/events
  specs/
    ports.md                   # P00–P17 contracts
    provider-options.md        # User-chosen illustrative capability list
    evidence-rules.md          # What counts as an actual local receipt
  examples/
    fictional-task.json        # Synthetic input
    fictional-review.json      # A fabricated mock explicitly labeled MOCK
  tests/
    test_goal_intake.py
    test_route_admission.py
    test_handoff.py
    test_failure_modes.py
  src/
    local_ledger.py            # Simple storage model
    route_candidates.py        # Deterministic option filtering
    synthetic_workers.py       # Fake responders, NO provider API calls
    public_demo.py             # CLI for the toy
  out/                         # Private local synthetic test results
~~~

A file under state/ can contain simulated identifiers, but should not contain a real username, device path, auth token, email, account balance or provider credential. Ignore local state and out/ in any public repository. A fictional record can use abstract source IDs rather than sensitive paths.

**Why begin with mock workers?** They let you verify routing, preservation and fallback without any subscriptions, API calls, model-induced variability or exposure of personal information. Real provider connections are an optional later project requiring separate permission and qualification.

## 3. The stepwise learning build

### Stage 00 — define exact purpose and constraints

Write a local MISSION: **route synthetic tasks between simulated workers while preserving status and evidence**. Define success as reproducible results, not a particular AI brand.

Show the planned project directory to the human before creating files. Don't scan unrelated folders. Use standard Python, SQLite, and built-in testing at first. Require the project to work offline.

### Stage 01 — implement durable records

Create a local ledger that can store:
- A fictional mission and exact current revision.
- At least five small tasks and dependencies.
- Task dispositions, including OPEN, ATTEMPTED, FAILED, RECONCILE, VERIFIED.
- Evidence references and reviewer notes.
- An append-only history that makes earlier failures visible.
- A human decision record used **only in simulations**; do not convert it to real external authority.

**Check:** close the process; reopen the database; confirm tasks and failures still exist. Reconstructed output must match the saved version. An AI-generated description alone is not enough.

### Stage 02 — list mock worker capabilities

Define 3–5 simulated options, each with a generic name and bounded ability:
- A public-source advice worker, no machine tools.
- A coding worker with permission to modify only the toy workspace.
- A review-only worker with no write permissions.
- A local deterministic test process.
- A deliberately unavailable or unqualified worker.

Do not name a mock after an actual provider in a way that suggests it was invoked. Clearly label mocks.

**Check:** the unavailable worker is never selected for execution simply because it has the most impressive descriptive ability.

### Stage 03 — enforce the eligibility filter

For each toy work item, require:
- Exact task type and input class.
- Required ability.
- Declared output contract.
- Task-bound privacy designation.
- Current simulated route availability.
- Simulated approval for any toy side effect.
- Exact source revision, so stale reviews cannot pass.

A route failing a required condition is excluded before any preference ranking. Do not use the real user's subscription details as sample data.

**Check:** missing a hard requirement cannot be compensated by a high quality rating.

### Stage 04 — choose and record a primary and alternatives

For each synthetic task, produce:
1. The primary eligible worker and the precise reason.
2. Every other qualified worker and the condition under which it would be chosen.
3. Every disqualified worker and its explicit reason.
4. The source revision and simulation run ID.
5. What must be verified before an effect counts.

This is the user-visible decision explanation. A real production privacy or authority decision must rely on software-enforced controls, not a generated explanation.

**Check:** two calls with identical toy state and preferences make the same decision; source changes cause a documented re-evaluation.

### Stage 05 — run simulated advisory work

Dispatch a fictional request to a mock response function. Keep a clear separation between:
- Request created.
- Mock response returned.
- Response's claims examined.
- Deterministic acceptance checks performed.
- Result qualified or rejected.

Do not pretend a mock response is an Anthropic, OpenAI, Google, GitHub, Perplexity or xAI response.

**Check:** a mock that prints "I have passed" cannot turn FAIL into VERIFIED.

### Stage 06 — connect a real local test tool

With the user's separate authorization for the toy folder only, run a real Python test process over **synthetic files**. Save exit status, observed output and input revision in a local evidence record.

A standard-library test invocation might resemble:

~~~text
python3 -m unittest discover -s tests -v
~~~

This command is only an example; it is not evidence of tests in the reader's environment until someone actually executes it and captures results.

**Check:** a successful test run and a worker's textual claim of success produce different evidence categories.

### Stage 07 — add next-worker review

Create an independent mock critic that receives the same fictional source revision and returns a candidate critique. It must not silently edit source or change the first worker's evidence. Preserve disagreements.

If using real models later, record direct versus brokered provenance and actual provider response. Do not claim independence when multiple responses are generated by one model instance.

**Check:** a missing reviewer response stays NOT RECEIVED; it does not count as a completed review.

### Stage 08 — inject failures and switch workers

Use predetermined synthetic failure cases:
- A provider becomes unavailable.
- An expected file is absent.
- A review is stale.
- A mock tool claims success but nothing changed.
- A toy action has ambiguous outcome.
- Two simulated workers propose overlapping changes.
- An action would disclose marked-private content.
- A successor has a smaller capability set.

**Check:** the system does not re-run ambiguous consequential toy actions without reconciliation; it never loses the original failure.

### Stage 09 — cold restart and completion

Stop the application completely. Start a new process without retaining the old AI conversation. Read the project records, reconstruct active tasks, identify the first safe next item and explain why.

**Check:** exact source revisions, open failures, simulated authority and verification state survive. End with a privacy-reduced handoff; do not reveal the actual full database.

## 4. Atomic test matrix — 24 negative and positive cases

These are **new fictional public exercises**, not Seraph's private qualification fixtures or hidden benchmark prompts.

| ID | Scenario | Expected result |
| --- | --- | --- |
| L-01 | New fictional mission with clear goal | Mission recorded; no external connection |
| L-02 | Mission has no success condition | Request limited clarification / BLOCKED |
| L-03 | Input marked private but cloud route requested | Deny disclosure |
| L-04 | Source revision missing | Do not claim grounded analysis |
| L-05 | Known provider route with stale health | Refresh relevant capability or exclude |
| L-06 | Paid plan exists, no authorized API/tool | Not selectable for API execution |
| L-07 | Eligible researcher and source task | Proper candidate chosen |
| L-08 | Chat-only worker asked to edit file | Refused as execution route |
| L-09 | Coding CLI able to write synthetic local folder | May select only after permission |
| L-10 | Mock worker returns "PASS" with no test | Advisory only; not VERIFIED |
| L-11 | Real local Python test exits successfully | Bounded test result recorded |
| L-12 | Python test fails | FAILURE and source revision preserved |
| L-13 | Worker name changes; task unchanged | Mission remains consistent |
| L-14 | Primary unavailable before consequential action | Try another eligible option |
| L-15 | All providers unqualified | BLOCKED; no invented invocation |
| L-16 | Two mocks editing same fictional resource | Prevent overlapping write or halt |
| L-17 | Worker proposes unauthorized publication | NEEDS_APPROVAL |
| L-18 | Simulated external send times out ambiguously | RECONCILE; no automatic resend |
| L-19 | Reviewer returns no response | Reviewer seat NOT RECEIVED |
| L-20 | Reviewer reports on old revision | STALE; no current approval |
| L-21 | Two models claim agreement but sources missing | UNKNOWN factual support |
| L-22 | Process stops mid-project; new process resumes | Correct unfinished task and failure history |
| L-23 | Saved data corrupted | Stop, preserve evidence; do not fabricate recovery |
| L-24 | Clean synthetic run completes five tasks | Only verified bounded tasks marked complete |

### Additional robustness exercises

- Repeat seed-controlled test runs under different random failure orderings.
- Simulate a long-running task losing its worker.
- Simulate a model changing its response format unexpectedly.
- Change task privacy after candidate selection but before dispatch; the old eligibility must not survive.
- Simulate interrupted backup and restore to an empty directory.
- Test that old authorization text cannot approve a new scope.
- Compare a plain-chat/manual-log baseline against the local continuity prototype for time and recovery accuracy.

A passing run should preserve the **raw evidence**, including failed tests and operator corrections, in the learner's local test environment.

## 5. What to measure

| Metric | Definition | Why it matters |
| --- | --- | --- |
| Correct recovery count | Number of interrupted eligible trials safely resumed with the correct remaining task | Measures continuity, not confidence |
| Duplicate consequential actions | Number of repeated operations with possible external effects | Must be zero in protected tests |
| Unauthorized executions | Operations actually performed without required authorization | Must be zero |
| Unsupported success claims | Claims promoted to VERIFIED without sufficient observed evidence | Must be zero |
| Missing evidence caught | Missing or stale receipts correctly identified | Helps prevent false conclusions |
| Human reconstruction burden | Manual corrections/steps needed to recover after restart | Should be compared to ordinary chat |
| Route substitution errors | Wrong model/provider/tool substituted for an explicitly required one | Must be zero |
| Privacy boundary violations | Protected test data sent beyond permitted destination | Must be zero |
| Time to correct next action | Time until the **first correct and permitted** post-restart action | Misleading if only measuring quick guesses |
| Cost and resource use | Actual incremental paid calls, local run time, storage | Must be measured; not guessed |

The pilot's outcome is comparative evidence only if you also test the **same scenario without the continuity layer**. Ordinary notes and careful humans can outperform an elaborate AI router; that is a legitimate result.

## 6. How real AIs become optional providers later

Do not begin by collecting API keys from every company. First ensure that the offline toy passes its own checks.

For one optional provider addition:
1. Choose one actual provider and official supported interface.
2. Read that provider's terms, account privacy policy, data retention and pricing.
3. Decide whether fictional data alone is sufficient (it should be for qualification).
4. Identify the exact task ability: chat/research/code review/file action.
5. Run one **user-approved** low-risk capability test and preserve the actual response.
6. Record the route's qualifications and limitations.
7. Reject any attempt to claim a second uninvoked provider participated.
8. Add another provider only for a demonstrated need and independently qualified role.

**Developer APIs may charge separately** from consumer subscriptions. Credentials belong in appropriate secure local or provider-managed storage, not AI-generated source files, GitHub commits or cloud handoff cards.

## 7. Public release gate for executable prototypes

The public Age of Free Programming repository currently distributes educational prompts and documentation. Publishing a downloadable runnable router is a **separate code-release decision**. Before adding source code or installers, the rights holder must authorize the license, file scope, third-party dependencies, privacy/security checks, cross-platform tests, support path and public disclosure classification.

Do not copy private Seraph Mesh implementation to skip that process. Independent learners can build their **own new projects** from public tutorials under the applicable AI provider/tool and software licenses.

## 8. What "atomic" means in this guide

Atomic does **not** mean a literal simulation of biological neurons or unrestricted reproduction of a private AI control plane. Here it means:

- One input has one recorded classification.
- One candidate route has an explicit qualification outcome.
- One action has a defined scope and expected result.
- One worker cannot erase another worker's preserved failure.
- One test result is tied to a particular project revision.
- One handoff distinguishes facts, unknowns, permissions and next safe work.
- One ambiguity cannot become two irreversible actions through automatic retries.

Build the smallest trustworthy piece first, verify it, and then connect the next piece.

Continue with [privacy boundaries](06_PRIVACY_AND_TRUST_BOUNDARIES.md) and the [three-worker example](07_THREE_AI_SYNTHETIC_TRACE.md).
