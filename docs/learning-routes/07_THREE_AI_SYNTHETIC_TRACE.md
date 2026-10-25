# 07 — Three-AI fictional trace, from intake to verified handoff

[Atlas index](README.md) · [Port catalog](01_PORTS_AND_DECISION_POINTS.md) · [Provider alternatives](03_PROVIDER_OPTIONS_AND_FALLBACKS.md) · [Evidence](04_HANDOFF_EVIDENCE_AND_RECOVERY.md)

**This is an illustrative storyboard. None of the named AI providers is claimed to have been invoked in this example.** The roles are generic, fictional, and can be assigned to actual qualified user-owned tools later. A human can reproduce the exercise with local files and mock responses.

## Mission: Build a tiny offline catalog for an imaginary museum

A fictional museum wants a small offline program that lists ten public-domain-style invented exhibits, checks that descriptions are present, and produces a short text report.

**Scope:** Python standard library, synthetic descriptions, no public website requests, no database of real visitors, no purchases, no personal identity, no automatic deployment.

**Acceptance conditions:** source exists in an isolated project folder; tests actually run; one intentionally broken case is detected; a successor AI can reconstruct the unfinished task from durable state; the human decides whether to publish.

## Actors and boundaries

| Participant | Logical role | What it may do in the example | What it cannot claim |
| --- | --- | --- | --- |
| Operator | Defines mission and approves protected changes | Choose objective, local test folder, permissible use | Not replaced by a model |
| Controller | Maintains mission and routes tasks | Classify task, choose only qualified options, store handoffs | Cannot execute merely by describing an action |
| Research-A | Public-source/style adviser | Suggest safe content categories | Cannot verify live sources without actual retrieval |
| Coder-B | Authorized local coding assistant | Create files only in user's isolated toy project | Cannot publish or spend money |
| Critic-C | Separate review-only worker | Examine the same exact source revision | Cannot edit files or certify tests it did not run |
| Test Tool | Real deterministic Python process | Run test suite and report exit/output | Cannot make subjective source-rights decisions |
| Durable Record | Local mission/evidence ledger | Preserve attempts, tests, corrections and next task | A saved claim is not independently proven truth |

**AI choice is optional:** Research-A could be a qualified ChatGPT, Perplexity, Gemini, Claude or local model as fits the exact task. Coder-B could be Claude Code, Gemini CLI, Copilot CLI, Kimi Code, Qwen Code, or an eligible ChatGPT session connected to a user-authorized tool. Critic-C could be a separate actually contacted qualified provider or a human reviewer. **No specific provider is automatically connected or paid for.**

## Step 1: P00 → P03 — Intake and decomposition

The human says: "Build a fictional offline museum catalog for a beginner."

The controller captures:
- Mission ID: **museum-demo**.
- Tasks: T1 synthetic records; T2 local program; T3 tests; T4 critique; T5 human completion review.
- Authority: propose and inspect synthetic files; no publishing, networking or payments.
- Evidence policy: real source/test readback required for VERIFIED.

**Other option at this point:** If the user only has ordinary web chat, produce copyable file drafts and a manual checklist. Do not claim source was created on their computer.

## Step 2: P04 → P06 — Capability selection for T1

**Primary candidate:** Research-A if it is qualified to generate safe synthetic examples. It needs no live web retrieval for this exercise.

**Alternatives:** The human invents the fictional exhibits, Coder-B generates the sample fixtures, or a qualified local model drafts generic descriptions.

**Exclude:** Any route requiring real visitor data or paid external access. If the task changes to factual historical exhibits, the required capability changes to genuine source retrieval and rights verification.

**Result:** A candidate description list is returned and locally retained as synthetic content. It is not a claim of historical accuracy.

## Step 3: P07 → P09 — Bounded assignment to Coder-B

Coder-B receives only:
- The mission and synthetic test cases.
- The user's approved isolated folder.
- The intended file outputs.
- Permitted dependencies: Python standard library.
- Explicit limit: do not open browser profiles, scan unrelated files or connect to external services.
- Requirement: show actual file changes and test output.

**Other options:** If Coder-B lacks a local writing tool, try another already-qualified local coding surface or ask the user to create files manually. A great coding model without a tool is still **advisory only**.

**Failure to avoid:** Giving the model a general computer shell with unrestricted access and treating a friendly prompt as technical confinement. Use real isolation and user privileges.

## Step 4: P10 → P12 — Actual deterministic execution

Coder-B proposes source, then the user authorizes the isolated write. A real tool creates the files. The separate test program executes.

There are four genuinely different signals:

| Event | State before verification | State after a valid check |
| --- | --- | --- |
| Coder-B says "I wrote the file" | Claimed source | Observed only after file readback |
| Python test invoked | ATTEMPTED | OBSERVED when process exit/output returns |
| Test output says PASS | OBSERVED | VERIFIED only within the tested criteria and revision |
| Coder-B says "project complete" | Candidate claim | Final project closure still requires human acceptance |

**Other option:** A human executes the same synthetic tests locally if the coding assistant cannot run processes.

**Intentional failure:** One exhibit lacks a description. A real test should fail, and its failure record must remain. Do not fabricate a PASS merely to satisfy the story.

## Step 5: P13 → P15 — Independent review by Critic-C

Critic-C gets the exact testable revision plus a sanitized excerpt of the program and test expectations.

It receives **no live credentials, real machine path, private account data or irrelevant chat history**.

The critic's assignment:

> Review the supplied synthetic source revision. Identify cases the tests might miss, contradict assumptions if appropriate, and label any claim you cannot verify without a real tool. Do not pretend to execute code, access the source repository or use external research unless an actual qualified tool is present.

**Other choices:** A second direct AI provider, a local model as a labeled supplemental check, or a human. If the user requires three independent frontier providers and only one responds, record **one**, not three.

**Result:** Critic-C might identify an empty description edge case. This is a critique, not proof that the fix was made.

## Step 6: P16 — Feedback and evidence reconciliation

Coder-B receives the critic's bounded finding, not the entire private working directory. A correction is proposed and accepted by the human if it falls within the approved scope.

A fresh real test process runs again against the exact revised source. The old failed run remains part of the history; the newer passing result is tied to the new revision.

**Other path:** If the critique is unsupported, preserve disagreement and seek deterministic evidence or human review. The critic does not silently become authority.

## Step 7: P17 — Stop the original AI and recover in a new session

A durable handoff card is produced:

~~~text
MISSION: Offline synthetic museum catalog.
CURRENT_REVISION: Toy source version 3.
VERIFIED: Local tests on version 3 passed in a real process.
OPEN: Human must review output formatting and rights statement.
FAILED_HISTORY: Version 2 failed empty-description test; retained.
AUTHORITY: New AI session has read-only advice permission.
MODEL_STATUS: Coder-B no longer active. Critic-C review completed on version 3 only.
NEXT: Confirm report formatting from real local output; do not publish automatically.
~~~

The operator closes Coder-B and opens a new AI conversation (or uses a different model). The successor checks the saved **local** state instead of assuming it inherited the old context.

**Other options:** Same provider in a fresh chat, different cloud provider with sanitized packet, installed local model, or manual continuity review.

**Stop condition:** If current source is unavailable, source revision unknown, or a protected prior action has uncertain effect, resume is **PARTIAL or BLOCKED** rather than invented confidence.

## Step 8: Human completion decision

The tests may pass, but the human still decides whether the fictional museum tool satisfies the need.

No code publishing, new external accounts, real customer outreach or commercial use is implied.

If the user chooses to publish their *independently created* code, source rights, license, dependency and privacy review are separate decisions.

## Router transcript (illustrative, NOT execution evidence)

| Turn | Input port | Selected role | Alternative offered | Required observation | Next |
| --- | --- | --- | --- | --- | --- |
| 1 | P00 | Controller | Manual mission notes | Mission saved | P03 |
| 2 | P03 | Controller | Re-scope task | Five bounded tasks | P04 |
| 3 | P04 | Research-A | Human/local synthetic author | Fictional records produced | P11 |
| 4 | P11 | Controller | Hold unsupported output | Synthetic status verified | P13 |
| 5 | P06 | Coder-B | Other qualified CLI / manual | Exact file write permission | P09 |
| 6 | P10 | Authorized local tool | Human terminal | Real file readback and test exit | P12 |
| 7 | P12 | Test Tool | Correct/hold | Intentional failure identified | P16 |
| 8 | P15 | Critic-C | Another real reviewer / human | Actual critique of exact source | P16 |
| 9 | P16 | Coder-B + Test Tool | Human fix | Changed source and rerun results | P12 |
| 10 | P17 | Controller | Manual state card | Durable sanitized handoff | New session |
| 11 | P02 | Successor model | Human recovery | Exact current revision/unknowns | P03 |
| 12 | P17 | Human operator | Delay | Final reviewed acceptance | Stop |

## What if something goes wrong between two neurons?

**Research-A disappears:** Keep received synthetic records; if no response, use another author or mark the step incomplete. No fake research result.

**Coder-B loses the shell connection:** Preserve actual local state. A qualified different coding tool may continue after readback. Do not assume the prior candidate was saved.

**Critic-C never answers:** Critique remains NOT RECEIVED. Don't create a fictional vote or convert Coder-B into its own independent critic.

**Cloud quota is exhausted:** Use an already qualified local/other provider if its capability and privacy fit, or stop. No silent paid-API charges.

**New worker has no prior context:** Reconstruct from the local ledger. The lack of personal chat memory is expected, not a reason to invent state.

**External consequential action times out:** Although the fictional museum example performs no real external actions, the general rule remains: check the target's real outcome before repeating via any route.

## Exercise for the reader

Try the same fictional five-task mission three ways:

1. Ordinary chat plus manual state notes.
2. A local toy continuity layer with one AI and real Python tests.
3. The local continuity layer with two genuinely separate model/provider sessions, passing only sanitized packets.

Compare correctness, verified progress, duplicate actions, reconstruction burden, privacy exposure and actual costs. Record unsuccessful attempts as carefully as successful ones.

A demonstration showing several different AI names on a chart is **not** evidence that they participated. A useful Seraph-inspired organization preserves **task identity and actual evidence across the participant changes**.

**This is how to teach an atomic routing workflow without exposing private Seraph's exact internal wiring.**
