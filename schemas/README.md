# Educational memory-data schemas (standalone, no external integration)

The two JSON Schema Draft 2020-12 documents in this folder describe small, generic local-first project-memory formats. They are **not software**, do not contain callbacks, authentication, private company data, real personal information or a working database, and do not create an automatic connection to any remote system.

| File | Purpose |
| --- | --- |
| [memory_record_v1.schema.json](memory_record_v1.schema.json) | Data shape for candidate facts, corrections, verification receipts, contradictions, invalidation and synthetic deletion events |
| [restart_packet_v1.schema.json](restart_packet_v1.schema.json) | Minimal, source-linked cold-start handoff with **zero inherited action permissions** |
| [Synthetic memory event](../examples/memory_record_synthetic.json) | Fake greenhouse example, never real user data |
| [Synthetic restart packet](../examples/restart_packet_synthetic.json) | Fake task recovery example, no private connections |

Both schema identifiers use local **URNs**, not publisher endpoints. The `$schema` reference names the public JSON Schema dialect; it is not an instruction to fetch anything online. A user's own program can bundle a trusted validator **offline**, but the beginner Python/SQLite system does not need a third-party package.

For an immediate standard-library-only syntax check, run from the public project root:

```sh
python3 -m json.tool schemas/memory_record_v1.schema.json > /dev/null
python3 -m json.tool schemas/restart_packet_v1.schema.json > /dev/null
python3 -m json.tool examples/memory_record_synthetic.json > /dev/null
python3 -m json.tool examples/restart_packet_synthetic.json > /dev/null
```

On Windows, use `py -3 -m json.tool` in place of `python3 -m json.tool`. This checks **JSON syntax only**, not full conformance with JSON Schema, user consent, accurate memory, attack resistance or privacy.

**Semantic gates (application code must enforce these):** a field reading `verification_status=verified` cannot prove a real independent review; a `review_receipt_id` can be fabricated; `private_data_included=false` is not an automated PII scan; and `authority_grant=false` is a data contract that must be enforced by a trusted action gateway. Treat schema-valid but unsupported facts as **UNKNOWN**.

Reference: [Memory architecture](../docs/MEMORY_FIDELITY_V1.md), [Acceptance tests](../docs/MEMORY_FIDELITY_ACCEPTANCE_V1.md), and [Independence boundary](../docs/NO_BACKLINK_INDEPENDENCE_V1.md).
