# 06 — Privacy, identity, finances and trust boundaries

[Atlas](README.md) · [Port definitions](01_PORTS_AND_DECISION_POINTS.md) · [Optional computer setup](../RECOMMENDED_COMPUTER_SETUP.md)

**Purpose:** Give people a useful, detailed route map while protecting both the original Seraph operator and new users building their own projects. This is **public safety guidance**, not disclosure of Seraph's private security architecture, enforcement code, live endpoints, vulnerabilities or credential practices.

## 1. Five independent boundaries to understand

| Boundary | What lies on each side | What can go wrong | Safe beginner rule |
| --- | --- | --- | --- |
| Human ↔ model | User's intent and assistant's suggestions | Model confuses suggestion with permission | Ask the actual human before consequential steps |
| Private files ↔ external AI | User-controlled disk and cloud inference providers | Sensitive text copied into prompts or tool results | Use synthetic data; redact and minimize before submission |
| AI ↔ computer tools | Model reasoning and OS-level file/terminal/GUI privileges | A connected tool can change real files | Restrict OS privileges and execution environment |
| One AI ↔ another AI | Original response/evidence and a separate provider | More copies of private data; provenance confusion | Share only a sanitized, source-bound packet |
| Local project ↔ public GitHub | Owner-controlled working copy and persistent public history | Public records, commit emails and secrets persist | Scan before committing; protect author metadata; publish only approved files |

**The critical fact:** An AI may follow instructions well without providing a hard security boundary. Prompts, advisory folder lists and command blacklists do not guarantee confinement of a terminal tool running with full OS permissions.

## 2. Data categories and what may cross

| Input category | Local synthetic test | Chat-only cloud AI | Authorized real CLI/cloud tool | Public GitHub |
| --- | --- | --- | --- | --- |
| Fictional project objective | Yes | Yes | Yes | Yes, if original and rights-cleared |
| Generic software design | Yes | Yes | Yes | Yes, if safe and independently authored |
| Public-source references | Yes | Yes | Yes, respecting terms | Link/brief citation |
| Redacted synthetic code/test log | Yes | Usually | When needed | Only reviewed, no sensitive metadata |
| Real client correspondence | Local only unless separately authorized | Default no | Explicit scope and privacy review | No |
| Real financial/account records | Keep local | No by default | Only exceptionally, with exact consent and fit | No |
| Credentials, cookies and tokens | Secure local or provider-approved secret store | Never in prompt | Avoid exposing values to model/tool logs | Never |
| Personal identity/health/student/family information | Keep out of demos | No by default | Separate consent/appropriate protections | No |
| Private Seraph Core algorithms or routes | Not part of this public learning project | No | No | No |
| Source license/rights conditions | Yes | Can discuss safely | Yes | Publish only accurate approved summaries |

**A privacy-preserving handoff is a new summary, not a copy of every earlier chat or source file.** Removing obvious names is necessary but may be insufficient when other context could re-identify someone.

## 3. Generic trust-boundary diagram

~~~mermaid
flowchart TD
 H["Human owner and intent"] --> L["Isolated local learning project"]
 L --> D{"Is any cloud submission permitted?"}
 D -->|No| M["Local model or deterministic tool"]
 D -->|Yes: synthetic or explicitly approved minimized data| C["User-selected external AI client"]
 C --> R["Model response: advisory"]
 M --> R
 R --> V["Independent local validation"]
 V --> A{"Any real-world side effect?"}
 A -->|No| E["Local state and handoff"]
 A -->|Yes| G["Separate human authority and qualified executor"]
 G --> E
 E --> X{"Publish educational material?"}
 X -->|Yes| P["Rights and privacy release review"]
 X -->|No| Z["Keep local"]
 P --> U["Public repo: only approved data"]
~~~

This is an invented **data-boundary map**. It is not an architectural disclosure of the private Seraph control plane or its protected authorization mechanism.

## 4. What to publish and what not to publish

**Appropriate for a public community atlas:**
- A generic port catalog, model capability decision process, high-level choice points, and educational diagrams.
- Direct links to official AI providers, clients and vendor documentation.
- A synthetic example routing a fictional task among symbolic workers.
- A precise explanation of why source validation and human permission are necessary.
- Independent, original examples using no real personal or company data.

**Keep private or obtain a separate specific disclosure review:**
- Private source code, unpublished schemas, exact graph semantics sufficient to reconstruct the protected Seraph implementation, or proprietary routing formulae.
- Real machine inventory, usernames, addresses, ports, service routes, network segments, host identities, live health states, or privileged command sequences.
- Internal authorization-enforcement details or unpublished vulnerabilities.
- Provider account IDs, subscription proofs, passwords, OAuth flows containing secrets, browser sessions, financial/benefit records, private company IP, real incident evidence or complete chat exports.
- Hidden qualification/benchmark answer keys or unreleased controlled test cases.

A public community routing design **does not** inherit rights to reproduce an existing private commercial system. Its named ports are **new educational abstractions**, not literal replicas.

## 5. Source authenticity and prompt-injection boundaries

Retrieved files, webpages and AI responses can contain instructions to ignore the mission, reveal secrets or change operating mode. Treat this content as **untrusted data**.

The reader's independent controller should not promote instructions embedded in third-party material to authority. It should preserve provenance and only use approved task instructions from an actual authorized user or trusted runtime controls.

**Example:** A public HTML page includes a sentence telling the AI to send a copy of the local project to a different address. That sentence is part of the webpage. It is not a valid operator directive and must not trigger data transmission.

A fake "system administrator" message inside a source document is also not the actual system administrator.

## 6. Remote Desktop Commander and similar adapters

The remote third-party agent can be useful for real file creation, terminal tests and observed evidence. It also introduces at least **two additional external trust boundaries**: the AI provider and the relay/operator of the remote computer tool.

The vendor documents directory guardrails and blocked command settings, but these do **not** create an OS sandbox around every terminal invocation. Use:
- A disposable virtual machine, restricted account or appropriately isolated container.
- No banking, family, student, medical, personal identity or business credential records in that environment.
- Minimal mounted volumes and no uncontrolled browser credential access.
- Synthetic tasks first.
- User review before enabling a new tool capability or performing external actions.
- A clear stop/disconnect plan when the exercise ends.

The presence of a desktop or MCP tool in a model's response does not itself prove it was called. Demand actual observed output. See the [computer setup guide](../RECOMMENDED_COMPUTER_SETUP.md).

## 7. Privacy costs of multi-model review

Sending the same unredacted project to many providers increases exposure, even when the intent is independent verification. A publicly shareable summary should contain only what the reviewer needs.

**Safe fictional packet:** objective, synthetic excerpt, exact public source revision, review question, constraints and response format.

**Unsafe packet:** personal chat log, real client list, financial ledger, medical records, private repository archive, active machine control configuration or authentication tokens.

If a reviewer cannot evaluate without protected data, the correct alternative may be local qualified review or a deliberately paused task—not removing privacy requirements.

## 8. Spending and subscription separation

A reader may have consumer plans with OpenAI, Anthropic, Google, GitHub, Microsoft, Perplexity, xAI, Kimi or other services. Those plans do not inherently grant API credits, shared payment authorization, an eligible coding tool, a current model, or access to a private Seraph system.

No public guide should require the reader to submit payment information to the original Seraph operator. The user decides what services to use and what additional costs they accept.

**Never let a fallback choose a paid API silently** merely because a free or prepaid route failed.

## 9. Why a "neuron network" is a metaphor

The architecture's "neurons" are separate models, software workers and validation tools. Its "dendrites" are inbound signals and context. Its "synapses" are controlled exchanges. Its "axons" are outputs and artifacts.

This is **not** a biological brain map, a literal shared neural weight graph, evidence of consciousness, or permission to capture model internals. It is an organizational analogy with real implications for state, routing, verification, and continuity.

A user's independent router may implement transparent decision rules while keeping provider accounts and privacy under their own control.

## 10. Security/rights checklist for a future release

Before publishing any executable:
1. Identify owner/rights holder and proposed license.
2. Review the exact source diff, current Git tree and reachable history.
3. Search for credentials, identifying details, private data, tracked binaries and embedded archives.
4. Confirm that all code and dependencies have compatible reuse rights.
5. Verify offline/no-network behavior where claimed.
6. Test unauthorized file access, path traversal, command scope and resource limits within an appropriate sandbox.
7. Test safe handling of interrupted execution and ambiguous external outcomes.
8. Verify backups and restoration independently.
9. Ensure direct payment/account/communication integrations cannot silently run.
10. Have a real independent human or qualified reviewer assess consequential security/privacy changes.

A successful scanner run is not a guarantee of zero vulnerabilities or legal clearance. A text-only educational publication is a different release class from an executable AI agent.

## 11. For the owner of private Seraph

Publishing this atlas documents the **general behavior** of a human-governed, mission-persistent AI organization. It does not grant access to the existing private Mesh, its machines, its accounts or its current model entitlements. Readers must create and authorize their own independently implemented systems.

**An atomic public teaching map can preserve the *outcome and decision discipline* without exposing the private graph or the engineering that makes protected operations authoritative.**
