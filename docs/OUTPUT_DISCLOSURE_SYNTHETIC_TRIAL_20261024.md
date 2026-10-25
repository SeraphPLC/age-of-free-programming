# Isolated synthetic output-disclosure gate trial — October 24, 2026

**Status: BOUNDED FIRST-PARTY REFERENCE CHECK | NO PRIVATE DATA | NO DEPLOYED AI TEST**

## Purpose and strict scope

Exercise a **new, minimal and isolated Python reference decision function**, using entirely fictional inputs, against twelve scenarios inspired by the public [OG01–OG12 disclosure test outline](OUTPUT_DISCLOSURE_GATE.md), plus six additional authorization/positive controls. Demonstrate both successful fail-closed decisions on labeled fixtures **and a false-green limitation when contextual sensitivity is mislabeled**. The sample is not bundled here or authorized for deployment; it is a temporary reviewer-authored test harness, not a release of private Seraph or the community AI OS.

**Test target:** a stand-alone deterministic `Envelope -> Verdict` function, not an LLM. Decisions depend on explicitly supplied audience, sensitivity, rights, current approval, destination and risk fields, with a few conservative literal indicators. These fields are simulated; there is **no authenticated permissions system or independent sensitivity classifier**.

## Observed, bounded execution

| Item | Observation |
| --- | --- |
| Fixture environment | Isolated Python 3.13.5 interpreter; standard library only; fictional data |
| Invocation | `python3 -I -B test_disclosure_gate.py` |
| OG-shaped synthetic scenarios | **12 of 12 produced expected decisions** |
| Additional synthetic controls | **6 of 6 produced expected decisions** |
| Total developer-authored unit checks | **18 of 18 PASS**; `unittest` observed `OK`, exit code `0` |
| Separate blind contextual challenge | **Limitation confirmed:** superficially safe, manually misclassified material was released |
| Independent reviewer | **NOT RUN** |
| Actual Get Seraphed R1/v0.5 AI responses | **NOT RUN** |
| Private Seraph systems or production AI OS | **NOT ACCESSED / NOT TESTED** |
| Publicly released executable | **NONE** |

## Scenario coverage in the reference function

| Scenario | Simulated condition | Expected reference decision |
| --- | --- | --- |
| OG01 | Fabricated credential marker | WITHHELD, not echoed |
| OG02 | Invented restricted endpoint in a log | WITHHELD |
| OG03 | Synthetic screenshot flagged with restricted metadata | WITHHELD |
| OG04 | External content includes an untrusted override instruction | WITHHELD |
| OG05 | Synthetic protected architecture classified for public release | WITHHELD |
| OG06 | Fragments **flagged** as inferentially identifying | WITHHELD |
| OG07 | Fictional private amendment remains in approved local scope | LOCAL_ONLY; no public text |
| OG08 | External model destination not authorized to receive evidence | WITHHELD |
| OG09 | Fake unreleased vulnerability details | WITHHELD |
| OG10 | Invented private link in outbound content | WITHHELD |
| OG11 | Contextual leak **flagged** even though literal patterns do not match | WITHHELD |
| OG12 | Unknown audience and release rights | WITHHELD |

Extra controls checked a benign fictional release, missing fresh approval, missing rights review, suspicious query parameter, fail-closed defaults and an explicit rights-override denial.

## Observed limitation — do not overclaim

A **separate negative control** deliberately omitted the contextual-risk flag while assigning the fictional input "public-cleared" status and current publication approval. The prototype **released** it. This is a meaningful *false-green failure mode*: rule engines that trust an incorrect clearance label cannot discover every inference-based or contextual privacy risk.

An earlier version of this temporary test function also used permissive authorization defaults. It was corrected **before** the final 18-check run to default to unknown audience/rights and no approval. Both observations are development evidence, not claims about deployed Seraph.

Consequently, **18/18 does not mean all 12 OG requirements passed in a real AI application**. In particular, the prototype did not parse real screenshots, authenticate a publishing identity, verify third-party rights, infer sensitive context reliably, or evaluate a model's actual ability to follow the instructions. No real secret, live URL, real identity or private Seraph implementation was used.

## Safe next qualification steps

1. Keep public publishing **human-reviewed and explicitly authorized**. The current text-only disclosure policy remains a behavioral requirement, not an enforcement product.
2. Develop an independently assessed, least-privilege output boundary for any future actual executable. Include real metadata/file parsers, reviewed destination restrictions, trusted provenance and conservative defaults before release.
3. Conduct **actual black-box, fresh-chat and cross-model negative tests** using only invented data and captured outputs; require independent review. Specifically test unflagged inference, prompt injection in retrieved material, misleading approvals, links, metadata and handoff leakage.
4. Preserve negative-control failures and mark remaining OG01–OG12 actual-system qualification **NOT RUN**. Do not merge or publish executable source from this isolated experiment under the current release gate.

## Claim boundary

**Validated here:** A temporary synthetic decision function produced its expected results for 18 reviewer-authored tests, and a separate blind control demonstrated a classification-dependence weakness.

**Not validated:** the live Seraph Mesh, an LLM, actual Get Seraphed prompts, actual file/metadata sanitization, public software security, or privacy guarantees.

See [verification ledger](VERIFICATION_STATUS.md), [public disclosure requirements](OUTPUT_DISCLOSURE_GATE.md), and [public release controls](PRIVACY_IP_AND_RELEASE_GATE.md).
