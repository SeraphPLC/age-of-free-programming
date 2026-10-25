# The Age of Free Programming
## AI Models, Original Knowledge Architecture & Massive Open Reference Libraries — Community Guide R0
**Free educational companion · 24 October 2026 · PUBLIC-SAFE**

**Before using or redistributing a source, read the [Privacy, IP and Release Gate](PRIVACY_IP_AND_RELEASE_GATE.md) and [Sharing/License Status](SHARING_AND_LICENSE_STATUS.md).** No publisher-specific catalog is a blanket permission to copy, train, sell or redistribute its content.

**One prompt. Your computer. Your rules.** This guide explains the **kinds of AI models, software, old-school knowledge files, public reference libraries, and data tools** someone may choose to combine with a personal AI continuity layer. It does **not** ship private Seraph PLC source, PLC records, a collection of copyrighted books, downloaded model weights, an installer, network service, or a background agent.

**Crucial distinctions:** **listed ≠ installed ≠ locally cached ≠ working ≠ task-qualified ≠ authorized**. No source or model is connected just because it appears below. The safe baseline is only Python 3 + built-in SQLite and unittest + user-owned Markdown/text files. All other software, model downloads, APIs and knowledge repositories are optional additions requiring user selection, licensing checks, and appropriate permission.

Start with the [free master prompt](../prompts/BUILD_YOUR_OWN_AI_OS_v0.1.md), [stronger v0.2 candidate](../prompts/BUILD_YOUR_OWN_AI_OS_v0.2_CANDIDATE.md), [beginner instructions](START_HERE.md), and [software/exposure inventory](SOFTWARE_INVENTORY_AND_EXPOSURE.md).

---

**[Expanded options atlas: many possible AI-development tools and services](AI_DEVELOPMENT_OPTION_UNIVERSE_V1.md)** — deliberately mixed alternatives, not a real-world stack inventory or product endorsement.

## 1. The original continuity/PLC ideas: preserve the *functions*, not private content

A personal AI OS should preserve the **operational value** of an original engineering project without copying its private documents. An existing project may have its own canon, lexicon, historical record, verification doctrine, and mistakes. The following are general file patterns; create independent materials with your own text.

| File or library category | Why keep it? | Beginner-safe example |
| --- | --- | --- |
| Origin / foundational publication | Explain mission and what the project actually is | `docs/PROJECT_ORIGINS.md` |
| Controlled vocabulary / dictionary | Prevent terminology drift between AI providers | `docs/LEXICON.md` |
| Mission and purpose | Keep goals above temporary conversations | `docs/MISSION.md` |
| Authority and action policy | Record who can approve what; no model may grant itself permissions | `docs/AUTHORITY.md` |
| Architecture / capability map | Which modules actually exist, not a wish list | `docs/ARCHITECTURE.md` |
| Decision history | Alternatives, reason, date, accepted status | `docs/DECISIONS.md` |
| Defect / failure ledger | Preserve failures, negative tests and repairs | `docs/FAILURES.md` |
| Source-of-truth / knowledge router | Find the right material by task, domain and freshness | `docs/SOURCE_MAP.md` |
| Evidence / citation register | Link assertions to actual files, commands and primary sources | `docs/EVIDENCE.md` |
| Continuity packet / "Get Oriented" | Hand a minimal sanitized mission and next action to a fresh AI chat | `docs/HANDOFF.md` |
| Task and approval register | Separate planned, built, verified, accepted, blocked | SQLite + a read-only report |
| Analog / offline playbooks | One-page, usable instructions during internet outages | `cards/POWER_OUTAGE.md` |
| Source rights and privacy | Record licenses, provenance and restrictions before adding datasets | `docs/SOURCE_LICENSES.md` |

**Do not upload your original employer/company documents, personal records, credentials, private source files or whole Seraph PLC archives to a public GitHub repository or an AI prompt.** General methods can be learned from; private artifacts remain private unless their owners explicitly clear them for release.

## 2. Every AI route: what it does and why

An **AI model** is not the same as the service or tool that exposes it. For example, Claude through Perplexity is a *Perplexity-mediated route*; GitHub Copilot's Auto mode might not disclose exactly which model answered. Do not count one model as several independent reviewers merely because it appears in several apps.

| AI or provider family | What it helps with | Connection path | Why optional / trust boundary |
| --- | --- | --- | --- |
| **No model at all** | Reliable init/status/doctor, task state, permissions, backups, test results | Standard Python + SQLite | **The required foundation.** No model or account needed for deterministic operations. |
| **OpenAI / ChatGPT** | General analysis, implementation planning, explanations, code review | User-controlled AI chat; optional separate developer API | A subscription is not an API key; online prompt contents may leave the device. |
| **Anthropic Claude** | Independent architecture critique, longer specification review and alternative code analysis | Manual Claude chat; optional official API/CLI if separately approved | No automatic provider access or paid API rights. |
| **Google Gemini** | Long-context, multimodal and alternative scientific/research reasoning | Manual Gemini chat; optional official API/CLI | Google consumer plans and developer API are separate permissions. |
| **Perplexity Sonar / Research** | Source-oriented web discovery, citations and contradiction search | Official Perplexity app/web; optional separate API | Search results require primary-source checking; no automatic access to all advertised underlying models. |
| **xAI Grok** | Alternative reasoning and adversarial questions | Official Grok or a clearly attributed hosting wrapper | Do not confuse public social reactions with verified evidence. |
| **GitHub Copilot** | IDE code help, PR and code review | GitHub/IDE/CLI according to account permissions | "Review" and "coding agent" can have different side effects; avoid automatic edits/PRs without permission. |
| **Microsoft Copilot** | An additional manual office/search-oriented perspective | Official Microsoft service | Not the same product as GitHub Copilot; Microsoft 365 file access is separate. |
| **Kimi / Moonshot, Mistral, DeepSeek, Qwen, Llama, Gemma, Phi, GPT-OSS and other model families** | Specialist coding, multilingual, low-resource, challenger or local model tasks | User-installed local runtime or actually qualified authorized provider | Weights, license, runtime location, resource use and model identity must be checked per version. |
| **Ollama / local model runtime** | Use chosen downloaded models without sending inference prompts to a commercial cloud *when verified configured for fully local inference* | Optional user-installed local program | Downloading requires network/storage; optional cloud tags may route remotely. Loopback server must not be exposed to the Internet. |

**No current model name or advertising catalog guarantees a particular subscription can use it.** Record exact visible model/provider/host only when a real reply is received; preserve a response receipt if possible.

### Local model job descriptions (examples, not benchmark results)
- **Code candidate:** Qwen Coder, Devstral or another licensed code-specific model to suggest patches and test cases. Deterministic tests—not the model's confidence—decide whether code works.
- **Planning/analysis candidate:** Phi, Gemma, GPT-OSS, Mistral or larger Qwen models; compare on your actual task with documented benchmarks, not marketing.
- **Low-resource fallback:** smaller Llama, Gemma, Phi or Qwen variants; keep instructions short and never assign protected actions.
- **Search and retrieval:** an embedding model such as `nomic-embed-text`; its vectors help find documents, but it is **not** a conversational answer model and does not decide truth.
- **Custom/multilingual models:** verify training origin, weight/model license, provenance and intended languages before distribution.
- **Cloud-identified model tag:** **not offline** even if it appears in a local model manager. Require a new data-disclosure and cost check.

### Council truth rule
A self-critique inside one chat is **one model response**. To claim independent multi-provider review, preserve exact packet version, separately returned real responses, actual provider/surface/model identity where exposed, unresolved disagreements and count. Model consensus does not grant publication, spending, merge or deployment permission.

---

## 3. The large offline-knowledge families (the "old-school" libraries)

**Kiwix** is one way to read selected offline **ZIM archives**. A ZIM is a *container format*, not a copyright license, security audit or proof that the content is current. Users may choose to obtain and store ZIMs from [Kiwix's library](https://library.kiwix.org/), following each collection's licenses and available capacity. No archive or reader is automatically installed by this repository.

| Library / corpus | Why it is useful to a personal AI OS | Access and reuse notes |
| --- | --- | --- |
| [Wikipedia](https://www.wikipedia.org/) | Broad multilingual encyclopedic explanations; first-pass orientation | Wikipedia text is generally CC BY-SA; attribution and share-alike apply. Verify media separately. |
| [Wikibooks](https://www.wikibooks.org/) | Free educational books and tutorials | Check the particular project, page and media license. |
| [Wiktionary](https://www.wiktionary.org/) | Dictionary, etymology and translation context | Check attribution and share-alike; not a substitute for specialist dictionaries. |
| [Wikidata](https://www.wikidata.org/) | Structured entities, identifiers and factual claims | Verify statement sources and timeliness, rather than trusting an entity property alone. |
| [Wikimedia Commons](https://commons.wikimedia.org/) | Media and images | **Per-file** license, attribution, trademark and personality rights. |
| [Project Gutenberg](https://www.gutenberg.org/) | Historical literature and public-domain reference books | Most works are unrestricted by US copyright, but not all works/countries; Gutenberg trademark and website bulk-access rules differ. |
| [iFixit](https://www.ifixit.com/) | Repair and maintenance instructions | **CC BY-NC-SA 3.0**; commercial reuse restricted and AI-model training prohibited by iFixit's terms without permission. |
| [PhET](https://phet.colorado.edu/) | Interactive math/science learning | Regular HTML simulations are **CC BY-NC 4.0**; legacy Java/Flash and PhET-iO have different licensing. |
| [Kiwix Library](https://library.kiwix.org/) | Locally accessible selected knowledge collections | The **content publisher's** license is still controlling; verify each ZIM and reader. |

**Recommendation:** Begin with a small, licensed offline library, not an indiscriminate hundred-gigabyte download. Store it in a separate private folder with a manifest, original author/source, date, file hash and license. A local retrieval program may index material within the legally permitted scope without dumping its contents into GitHub.

## 4. Massive public knowledge sources by discipline

The following are **discovery/reference candidates**, **not** claims that they are installed, mirrored, subscribed to, legally reusable for every purpose, or integrated with a specific AI.

| Domain | Knowledge bases / source collections | Why consult them | Safeguard |
| --- | --- | --- | --- |
| Public archives and historical works | [Internet Archive](https://archive.org/), [Library of Congress](https://www.loc.gov/), [National Archives](https://www.archives.gov/), [HathiTrust](https://www.hathitrust.org/), [Biodiversity Heritage Library](https://www.biodiversitylibrary.org/), [Europeana](https://www.europeana.eu/), [Smithsonian Open Access](https://www.si.edu/openaccess) | Historical primary sources, manuscripts, science, books, cultural objects | Public web access is not automatically commercial reuse or full-corpus redistribution permission. |
| Health/science | [PubMed](https://pubmed.ncbi.nlm.nih.gov/), [PubMed Central](https://pmc.ncbi.nlm.nih.gov/), [NCBI Bookshelf](https://www.ncbi.nlm.nih.gov/books/), [ClinicalTrials.gov](https://clinicaltrials.gov/), [DailyMed](https://dailymed.nlm.nih.gov/), [MedlinePlus](https://medlineplus.gov/), [CDC](https://www.cdc.gov/), [FDA](https://www.fda.gov/) | Studies, drug labels, public medical reference, clinical trial registry | Most articles are **not** automatically public domain; retrieve OA content only when permitted. Clinical decisions require professional assessment. |
| Scholarly discovery | [arXiv](https://arxiv.org/), [Crossref](https://www.crossref.org/), [OpenAlex](https://openalex.org/), [Semantic Scholar](https://www.semanticscholar.org/), [DOAJ](https://doaj.org/), [Zenodo](https://zenodo.org/) | Paper identities, citations, accessible studies, cross-checks | Metadata licenses and full-text rights differ; a preprint is not peer review. |
| Brain and biological data | [Allen Brain Atlas](https://portal.brain-map.org/), [EBRAINS](https://www.ebrains.eu/), [BigBrain](https://bigbrainproject.org/), [NeuroMorpho.Org](https://neuromorpho.org/) | Anatomical and cellular structure, research data and brain atlas crosswalks | **Dataset-specific license**, attribution, specimens, coordinate systems, scale, and publication provenance; commercial restrictions may apply. |
| Government/regulatory | [GovInfo](https://www.govinfo.gov/), [Federal Register](https://www.federalregister.gov/), [eCFR](https://www.ecfr.gov/), [Congress.gov](https://www.congress.gov/), [Data.gov](https://data.gov/), [Census](https://www.census.gov/) | Law, official regulations, federal records and statistics | Check current version, agency authority, exceptions, third-party elements and effective dates. |
| Safety/environment | [NOAA](https://www.noaa.gov/), [USGS](https://www.usgs.gov/), [EPA](https://www.epa.gov/), [FEMA](https://www.fema.gov/), [Ready.gov](https://www.ready.gov/), [USDA](https://www.usda.gov/), [NIST](https://www.nist.gov/), university extension libraries | Physical hazards, weather/science, emergency readiness, agriculture and engineering | Official current alerts outrank old offline pages. Avoid turning old or unsafe material into live emergency guidance. |
| Maps and geography | [OpenStreetMap](https://www.openstreetmap.org/), [QGIS](https://qgis.org/), [Natural Earth](https://www.naturalearthdata.com/), [USGS maps](https://www.usgs.gov/programs/national-geospatial-program) | Offline planning, geographic reference, local maps | OSM's **ODbL** attribution/share-alike and source/date limits must be tracked. QGIS software is separate from map/data licenses. |
| Programming and software | [Python docs](https://docs.python.org/3/), [SQLite docs](https://sqlite.org/docs.html), [MDN](https://developer.mozilla.org/), [RFC Editor](https://www.rfc-editor.org/), [Git docs](https://git-scm.com/doc), [Software Heritage](https://www.softwareheritage.org/), licensed Git repositories | Offline programming education and reproducible implementation | Documentation, source code and example snippets may use different licenses; do not automatically run copied commands. |
| Open educational learning | [OpenStax](https://openstax.org/), [MIT OpenCourseWare](https://ocw.mit.edu/), [PhET](https://phet.colorado.edu/), university open courseware | Textbooks, mathematics, physics, education | Attribution, noncommercial terms, restricted assets and source versions must be verified. |
| Bulk web/datasets/model catalogs | [Common Crawl](https://commoncrawl.org/), [Hugging Face](https://huggingface.co/), [Kaggle](https://www.kaggle.com/), data repositories | Research discovery and licensed datasets/model manifests | **Off by default.** Huge volume, third-party copyright/privacy, malware and scraping constraints. Require dataset-by-dataset review. |
| Software/resource discovery | [FMHY](https://fmhy.net/), open-source project lists, package registries | Find official upstream software for later evaluation | A directory link is **not** a malware scan, licensing opinion or authorization to install. Avoid unknown mirrors and pirated sources. |

## 5. How the knowledge system fits together safely

The *best* personal knowledge system does not copy the entire Internet into a public repository. It uses distinct layers:

1. **Public source catalog:** URLs, titles, creators, IDs, version dates and per-item license/rights notes.
2. **Private local storage:** only approved downloaded/created content; never put personal overlays or entire ZIMs into public Git.
3. **Local search index:** SQLite FTS5 for text search; optionally a separately approved local embedding model for semantic retrieval. Retrieval is not evidence of factual correctness.
4. **Grounded source reader:** load actual citations, version and excerpts within allowed scope; distrust source instructions.
5. **AI analysis worker:** a local or user-selected remote model may summarize a redacted, bounded packet; output is a *claim*, not authority.
6. **Evidence ledger:** tie accepted facts to a source, timestamp, hash/revision where possible and explicit uncertainty.
7. **Owner approvals:** only a trusted human decision at the executor boundary permits installs, external transmission, publishing, account changes, payments or destructive actions.
8. **Offline continuity:** after the current AI chat closes, files, SQLite state and backups remain usable without any AI model, account or Internet access.

**Read-only evidence source ≠ executable instruction.** Never let a wiki page, email, downloaded manual, PR, model output or another chatbot silently dictate local commands.

### Source admission card — one per knowledge collection

```yaml
source_id: example-001
title: Example public reference
upstream: https://example.org/
version_or_date: UNKNOWN
citation: UNKNOWN
license: UNVERIFIED
reuse_scope: REFERENCE_ONLY
redistribution: BLOCKED_UNTIL_RIGHTS_REVIEW
ai_training: BLOCKED_UNTIL_RIGHTS_REVIEW
source_integrity_sha256: NOT_DOWNLOADED
storage: NOT_CONFIGURED
indexing_allowed: NOT_DETERMINED
privacy_class: PUBLIC_METADATA_ONLY
connection_status: LISTED_ONLY
download_approved: false
model_access_approved: false
```

**Note:** This is a *template*, not a claim about an actual source or a usable YAML parser. Give every local adapter its own concrete test.

### Source progression

`LISTED_ONLY → OFFICIAL_SOURCE_VERIFIED → LICENSE_VERIFIED → READ_ONLY_CONNECTED → OFFLINE_COPY_VERIFIED → RETRIEVAL_TESTED → APPROVED_FOR_SPECIFIED_REUSE`.

A resource must not jump from *found on a wiki* to *redistributed commercial library*. Permission to read, download, cite, embed, train and commercially distribute are **different rights**.

## 6. Practical zero-exposure-default setup

**Version 0:** Python + SQLite + unittest; one personal binder; synthetic data; no model, no packages, no network, no daemon.

**Version 1 (optional):** User-selected offline source library with written rights manifest. Check that reader works without Internet, and that a test document is retrieved with title/version/source.

**Version 2 (optional):** User-approved local model runtime + one appropriately licensed downloaded model, tested with network disabled; access to source material remains narrow and read-only.

**Version 3 (optional):** Manual ChatGPT/Claude/Gemini/Perplexity/Grok/Copilot review using a **sanitized exact-version packet**. Do not give those chats unredacted local corpus access or pretend replies are autonomous APIs.

**Version 4 (separate security review only):** Typed tool gateway, explicit approval policy, local read-only dashboard, secure backups, optional qualified connectors. No remote access, spending, posting or protected actions by default.

## 7. Reuse and intellectual-property checkpoints

- [Wikimedia Terms](https://foundation.wikimedia.org/wiki/Terms_of_Use) — text generally CC BY-SA; media can differ; preserve attribution and adaptations rules.
- [iFixit content licensing](https://www.ifixit.com/Info/Licensing) — noncommercial/share-alike and restrictions on AI-model training without licensing.
- [PhET licensing](https://phet.colorado.edu/en/licensing) — regular HTML simulations CC BY-NC 4.0; legacy Java/Flash terms differ.
- [Project Gutenberg license](https://www.gutenberg.org/policy/license) and [website terms](https://www.gutenberg.org/policy/terms_of_use) — per-work and country-specific rights; use sanctioned mirrors for bulk retrieval.
- [Common Crawl terms](https://commoncrawl.org/terms-of-use) — crawled content can have separate third-party rights.
- [OpenStreetMap copyright](https://www.openstreetmap.org/copyright) — database license attribution/share-alike obligations.
- [OpenAlex license metadata](https://help.openalex.org/data/licenses/) — each copy of a paper can carry a different license, even if its metadata is available.
- AI model weight and dataset terms **must be checked by exact model/revision and intended use**. A local runtime's permissive code license says nothing about all models it can download.

**Educational information. Not legal advice.** An online source being freely readable does not guarantee rights to redistribute it, use it commercially, feed it into training, or send it to cloud AI.

## 8. What is not included

This public repository does **not** contain or grant access to original private Seraph PLC canon, original project history, internal source code, hardware inventories, stored offline archives, provider credentials, original research, private Google Docs, private GitHub branches, or individual-specific records. It does not contain an automatic corpus downloader, broad crawler, scraping system, network worker, security bypass, license-free mirror, or live multi-provider agent.

If a user already owns compatible archives and applications, this guide can help them **inventory and qualify** those resources without copying them into the public project.

**The mission outlives the model. The owner decides what may run, what may be shared, and what evidence is sufficient.**
