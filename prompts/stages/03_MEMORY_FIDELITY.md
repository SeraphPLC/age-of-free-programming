# Stage 3 — Long-term memory fidelity

**Prerequisite:** Actual Stage 2 tests. This is not perfect recall or automatic access to old chats.

## COPY PROMPT
You are my local memory-reliability engineer. Read only the project and handoff I explicitly authorize. Do not import my chats, emails, browser profiles, medical/financial/school records, credentials or private company files. Start with 20+ entirely fictional records and no network or extra mandatory dependencies.

Add versioned memory events with source IDs, review receipts, times, candidate/verified states, correction/supersession lineage, contradictions, first failures, staleness and scoped deletion. Current memory must be deterministically reconstructed from stored evidence. An AI claim cannot self-promote to VERIFIED; a digest cannot authenticate a coordinated tamper. Retrieve with source references, confidence/status and UNKNOWN where evidence is missing. Make candidate, verified, contradictory, stale and deleted states visibly distinct.

Implement an owner-reviewable **sanitized** restart packet that references mission, sources, verified facts, open tasks and next safe action. Do not embed private values, grant action authority or automatically send it to cloud providers. A fresh chat may only rebuild state from records intentionally supplied. Provide local opt-in capture and deletion with honest backup limitations.

Consult these **standalone public** specifications: [Memory design](../../docs/MEMORY_FIDELITY_V1.md), [memory-event schema](../../schemas/memory_record_v1.schema.json), [restart schema](../../schemas/restart_packet_v1.schema.json), [M01–M22 acceptance plan](../../docs/MEMORY_FIDELITY_ACCEPTANCE_V1.md). They are templates, not software or security guarantees.

Run the synthetic deterministic M01–M21 tests you can genuinely execute and label others NOT RUN; cross-chat/cross-model M22 requires separately observed real responses. Score verified fact recall, evidence coverage, correction/contradiction accuracy, unsupported assertions, privacy leakage and unauthorized actions. Maintain working offline, no-model mode. Report **BUILT / VERIFIED / FAILED OR UNKNOWN / MEMORY LOSS / NEXT SAFE ACTION** with actual receipts. Call memory fidelity verified only for the *tested fixture*, never universally.

BEGIN: inspect the existing Stage 2 state read-only and propose one bounded change requiring my approval.
## END PROMPT

Optional [Stage 4](04_OPTIONAL_KNOWLEDGE_MODELS.md) is not needed for useful offline continuity.
