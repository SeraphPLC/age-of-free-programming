# AI Development: Broad Option Universe — Public Research Atlas v1
**24 October 2026 · Educational and privacy-preserving · Possibilities, not configuration**

> **No usage disclosure.** This directory is a deliberately broad, mixed-order selection of possible programs, AI families, hosted services, datasets, and research tools. **An item's presence neither confirms nor denies that any particular organization or project uses, installs, licenses, connects, endorses, or has access to it.** Order was shuffled within each use-case group and does not communicate selection, priority or deployment.

This catalog answers two questions for someone developing an independent personal AI continuity project: **Why might I consider this option?** and **How might I use it responsibly?** It is not a product inventory or a bill of materials. It offers **304 possible technology entries across 14 areas**, including competing or overlapping alternatives. This is a large illustrative cross-section, **not literally every product**, which is impossible in a changing ecosystem.

## Start with the safest development contract

The minimal educational exercise can be a local text binder plus a basic Python and SQLite task ledger—without a model, paid API, external data source, network listener, public server or autonomous worker. Everything below is optional, and adding a capability is a distinct operator-approved change. Cloud models may transmit text; local apps can still access files or call networks; public GitHub commits and issues can expose identities and records; a publicly available dataset may lack redistribution or AI-training permission.

**Alternatives must be chosen for the end user's own requirements.** None of these descriptions instructs anyone to install, activate, download, scrape, authenticate, pay, publish, grant computer access, or contact another person. Before any of that, apply the [Privacy, IP and Release Gate](PRIVACY_IP_AND_RELEASE_GATE.md), [Sharing/License Status](SHARING_AND_LICENSE_STATUS.md), and [Security policy](../SECURITY.md).

## How to read the tables

- **Why consider:** a plausible development role, *not* a measured endorsement.
- **How to experiment:** a narrowly bounded hypothetical use with reproducible tests.
- **Review first:** potential privacy, licensing, supply-chain, safety, cost or account-access concerns.
- **All options are unselected by default.** A subscription, installed icon, model listing or source link is not proof of callable access or authorization. A tool producing text is not authorized to act on your files or accounts.


## 1. Model families, assistants and reasoning services

Potential reasoning, coding, multilingual, embedding and research engines. A provider's name does not tell you which exact model/version answered; obtain a provider receipt for actual work.

| Option / alternative | Why someone might consider it | How a developer could use it | Review before use |
| --- | --- | --- | --- |
| **Amazon Nova / Titan** | Managed foundation-model and embedding options | Try a synthetic model comparison using an isolated approved AWS environment with fixed budgets. | Region, IAM, rates and cloud processing. |
| **GitHub Copilot** | IDE and code-review assisted development surface | Propose small changes to a disposable repo and require human diff review and tests before accepting. | IDE/repository access, PR permissions and hidden model identity. |
| **Snowflake Arctic** | Data-oriented language-model research candidate | Compare small representative SQL/text tasks using an exact available checkpoint or authorized host. | Check status and model license for current versions. |
| **OpenAI gpt-oss** | Possible open-weight local reasoning option | Evaluate exact checkpoint in a qualified local server using synthetic prompts and regression tests. | Verify model license, runtime and resources. |
| **Mistral / Magistral** | Open and commercial multilingual reasoning options | Compare an exact model revision on localized question-answer tests; attach through a separately authorized chat or API adapter. | Weight terms, disclosure and hosting jurisdiction. |
| **Google Gemma** | Open-weight alternatives for modest devices and larger systems | Test exact size and quantization for offline summarization or bounded question-answering before adoption. | Usage rules, model card and device capacity. |
| **Microsoft Phi** | Smaller model candidates for lightweight reasoning | Use tiny synthetic tasks to characterize what it handles reliably; preserve fallback for complex requests. | Not suitable as unreviewed action authority. |
| **Microsoft Copilot** | Manual writing and productivity assistant surface | Ask for nonconfidential drafting or analysis, then transfer approved results to user-owned files. | Microsoft data access and product-specific permissions. |
| **IBM Granite** | Enterprise-oriented coding and language models | Benchmark a permitted checkpoint on code explanation and document tasks, recording provenance and its model-card conditions. | Model license, data controls and accuracy. |
| **MiniMax models** | Optional text or multimodal model family | Investigate an official model card and test on narrow synthetic modalities through authorized interface. | Provider-specific rights and cost. |
| **Z.ai / GLM** | Alternative coding and multilingual model routes | Compare structured-output correctness on public examples, recording vendor and host distinctly. | Data disclosure, model identity and compliance. |
| **Nous Hermes** | Open-model fine-tune family for experimentation | Evaluate an appropriately licensed release for instruction-following while keeping local tool permissions disabled. | Community origin, benchmark and licensing. |
| **Anthropic Claude** | Independent architecture critique and detailed specification analysis | Hand an exact-version artifact to an authorized independent session; record changes suggested, evidence, and disagreements. | Provider terms and no presumed independent seat. |
| **Cohere Command / Rerank / Embed** | Retrieval-grounded answers, ranking and vector representations | Retrieve candidate passages first, then rerank or embed them using approved provider/local models and measured relevance tests. | External document disclosure and usage rights. |
| **Kimi / Moonshot AI** | Alternative long-context or coding-oriented family | Test repository-level reasoning on a public test fixture via a legitimate provider surface; verify exact available model name. | Entitlement, model origin and transport. |
| **Google Gemini** | Long-context and multimodal reasoning | Supply a redacted problem plus bounded reference packet; compare citations and structured outputs with independent tests. | Cloud retention, API vs consumer entitlement. |
| **DeepSeek** | Alternative reasoning and coding model families | Compare reproducible synthetic coding tasks; use an independently chosen legitimate host or permitted local revision. | Licensing, hosting and data-transfer review. |
| **xAI Grok** | Alternative interpretation and adversarial questions | Give an explicitly nonconfidential hypothesis to a qualified chat surface and demand counterexamples and source checks. | Provider privacy terms and social data reliability. |
| **Perplexity Sonar / Research** | Web-grounded discovery and citation suggestions | Request recent-source searches on an approved nonsecret question, then inspect original primary documents yourself. | Third-party retrieval, citation error and possible billing. |
| **Databricks DBRX** | Alternative enterprise/open-model research | Explore model cards and run representative public-data tests where a supported serving route exists. | Model availability, weight license and compute. |
| **OpenAI GPT family** | Broad analysis, code assistance and multimodal inputs | Send an exact redacted work packet through a chosen user app or separately authorized developer API; preserve tested outcomes. | Chat plan is not API access; billing and privacy. |
| **AI21 Jamba** | Hybrid architecture text-generation choices | Compare licensed model output on long-document extraction with explicit citation accuracy scoring. | Account access, rights and vendor terms. |
| **NVIDIA Nemotron** | NVIDIA-developed reasoning or agentic model family | Benchmark permitted checkpoints on task-planning and tool-use evaluation data without granting execution rights. | Weight and serving dependencies. |
| **Alibaba Qwen / Qwen Coder / Qwen VL** | Multilingual, code and vision-language alternatives | Run specialized benchmark suites on chosen legally permitted model releases; route to role-matched tasks only. | Revision/model-card conditions; image-data rights. |
| **Meta Llama** | Many possible self-hosted general model sizes | Select an exact licensed weight set, run it in an approved inference engine, test memory and factuality. | License conditions and hardware load. |

## 2. Model hosting, API marketplaces and inference gateways

Places where a developer could request model output without necessarily running model weights on their own hardware. None is presumed available or free.

| Option / alternative | Why someone might consider it | How a developer could use it | Review before use |
| --- | --- | --- | --- |
| **Amazon Bedrock** | One managed surface for multiple model providers | Select authorized model families, lock IAM and spend, and compare source-grounded synthetic tasks. | Multiple providers, region-specific policies and cost. |
| **Baseten** | Deployment platform for production inference | Evaluate an authenticated test endpoint using measured latency, autoscaling and model-version rollback tests. | Deployment permissions and spend. |
| **GroqCloud** | Fast inference endpoint candidate | Benchmark latency and output consistency on fixed public prompts through a separate billing-controlled adapter. | Hosted data, quotas and model availability. |
| **Hugging Face Inference Providers** | Catalog and hosted model endpoints | Discover official models, inspect cards/licenses, then use a minimal approved test endpoint. | Provider routing and uncertain asset permissions. |
| **RunPod** | Rentable GPU compute environment | Isolate a temporary model service for nonprivate tests and remove credentials and disks after a verified stop. | Exposed ports, rented environment and costs. |
| **Fireworks AI** | Hosted model deployment and inference | Use a narrowly authorized synthetic benchmark to compare throughput, schema conformance and model versions. | API credentials, spend and data residency. |
| **Google Vertex AI** | Enterprise ML and model hosting | Test a managed endpoint with least-privilege service identity and monitor model/evaluation logs. | Region, cloud IAM, payment and data handling. |
| **OpenRouter** | Multi-provider model routing interface | Compare the same sanitized packet through individually named routes and preserve underlying provider IDs when given. | Gateway plus upstream disclosure, model substitution. |
| **Azure AI Foundry** | Managed enterprise AI lifecycle and model selection | Create a segregated test project with strict identity and budget policy, then compare several model deployments. | Tenant permissions, retention and cost. |
| **Cerebras Inference** | Specialized high-throughput inference service | Benchmark token latency and response accuracy against a local reference using public data. | External requests and rate limits. |
| **Cloudflare Workers AI** | Serverless AI inference near web applications | Add a gated endpoint for nonsecret low-volume inputs, testing regional limits, quotas and response behavior. | Billing, outbound requests and privacy. |
| **Together AI** | Hosted open-model options | Test a specific model/server pairing with pinned request parameters and a synthetic public test corpus. | Account keys, model/hosting changes. |
| **NVIDIA NIM** | Packaged inference microservice choices | Test a compatible model container behind a restricted gateway with resource/health monitoring. | Container licensing and network access. |
| **DeepInfra** | Alternative managed model inference | Compare only source-approved inputs and retain exact model host, region and terms with each receipt. | External-provider privacy and rate charges. |
| **Modal** | Serverless Python/GPU compute possibility | Launch an isolated reproducible experiment from pinned code, then shut it down and review execution logs. | Remote secrets and time-based charges. |
| **Replicate** | Hosted model inference experiments | Select a published model revision, compare identical synthetic inputs, and record the actual image/text output contract. | Public model provenance and third-party hosting. |

## 3. Local-capable model runners, desktop UIs and inference engines

These could make inference possible without uploading prompts when genuinely configured for local processing. Local software may still download models, call the network or expose a server.

| Option / alternative | Why someone might consider it | How a developer could use it | Review before use |
| --- | --- | --- | --- |
| **vLLM** | High-throughput model serving on suitable accelerators | Serve a pinned compatible model within a contained test host and measure throughput, queueing and output validation. | Network bind, GPU access and weight license. |
| **Open WebUI** | Self-hosted interface for multiple model endpoints | Connect only allowlisted local endpoints first; turn off unreviewed plugins and external searches. | Auth, connectors and content storage. |
| **LibreChat** | Multi-provider chat interface option | Configure user-chosen model routes with separate credentials, role limits and restricted tool access. | Conversation storage and external connectors. |
| **llamafile** | Portable packaged-model experiment approach | Verify signed/offical binary and compatible model bundle before local testing; avoid executing unknown shared downloads. | Binary trust and executable provenance. |
| **GPT4All** | Consumer-friendly local model experiments | Use an approved downloaded model with local test documents and inspect generated answers against originals. | Weight rights and indexing permissions. |
| **ExLlamaV2** | Optimized quantized-model research on compatible GPUs | Load documented supported formats in a private test environment and record correctness and memory limits. | GPU-specific dependency and maintenance. |
| **AnythingLLM** | Document-oriented assistant workspace | Attach an approved knowledge folder and model route, verify citations, and disable broad agent tools by default. | Workspace storage, plugins and remote features. |
| **LocalAI** | Self-hosted model-server compatibility layer | Put a selected model behind a local API in a container and verify no external access or unintended tools. | Dependency footprint, updates and network. |
| **Ollama** | Convenient local model lifecycle and API | Import or pull a specifically approved model; keep the service private and test no outbound inference. | Optional cloud tags, model downloads and ports. |
| **llama.cpp** | Lightweight local inference and quantization tools | Serve a checked GGUF model on loopback or run it as a CLI; compare output against reproducible prompts. | Quantization accuracy and bind settings. |
| **MLX-LM** | Apple silicon local model experimentation | Convert/load compatible weights and benchmark inference in an isolated workspace with source-digest records. | Model licensing and device memory. |
| **SGLang** | Efficient serving for supported model architectures | Prototype controlled high-volume inference against synthetic workloads with explicit queue, timeout and GPU limits. | Server deployment security. |
| **text-generation-webui** | Flexible local model evaluation UI | Place it in a disposable environment to compare sampling and prompt behavior without linking sensitive files. | Plugins, dependency updates and open ports. |
| **Jan** | Local conversational interface alternative | Download an explicitly licensed model through an approved path, test with network disabled and keep its API bound privately. | Software/model origin and localhost exposure. |
| **LM Studio** | GUI for discovering and running selected local models | Start a limited local model server only when needed; test network-disabled use and file-access behavior. | Download source, server exposure and optional remote integrations. |
| **Msty** | Desktop model/chat organization alternative | Compare model endpoints and document search within a synthetic workspace; review any cloud synchronization setting. | App-specific terms and local/cloud mixing. |

## 4. Editors, coding agents and software engineering assistants

Helpful for writing and testing code; access to local files, terminal, browser and Git remotes must be separately authorized.

| Option / alternative | Why someone might consider it | How a developer could use it | Review before use |
| --- | --- | --- | --- |
| **Continue** | Pluggable editor model-assistance extension | Attach a selected local or approved remote model and benchmark code completion inside a synthetic project. | Configured endpoint and extension permissions. |
| **OpenHands** | Software-task agent experimentation | Give it a throwaway repository and explicit test tasks, inspect execution logs, then manually approve patches. | Container privileges, internet and repository writes. |
| **Claude Code** | Code review, repo exploration and assisted implementation | Provide a specifically bounded workspace and use recorded diff/test acceptance gates. | Local file and tool permissions; provider data policy. |
| **Amazon Q Developer** | Cloud-integrated coding assistance option | Run reviewable code suggestions on a disposable project while limiting AWS identity and deployment access. | IAM and cloud coupling. |
| **Gemini CLI** | Model-assisted terminal coding and analysis | Run an authorized synthetic analysis with explicit file and command rules; log any external model calls. | Provider account, permissions and data transport. |
| **Roo Code** | Configurable agent-style editor extension | Define explicit command approval and provider limits before allowing operations on a disposable workspace. | Extension/tool permissions and external models. |
| **Codex CLI** | Code generation and repository operations | Use a sandbox workspace and hold all commits, networking and privileged commands behind review. | Credential scope, filesystem and cost. |
| **GitHub Copilot** | In-editor code proposals and PR commentary | Accept snippets only after checking source/license provenance, diff scope and tests; distinguish advisory from coding-agent behavior. | Repo write authority and model selector. |
| **Replit Agent** | Browser-based project bootstrap alternative | Build a nonsecret prototype in a temporary hosted workspace and export code for independent local tests. | Hosted data, billing and publishing. |
| **Cursor** | AI-aware IDE for navigation and code generation | Permit narrowly scoped code edits in a test repo and use source-control comparisons to validate them. | Indexed source disclosure and auto-command modes. |
| **Windsurf** | Integrated AI-assisted code navigation and edits | Review agent-generated changes in a feature branch and verify external tool permissions. | Editor cloud and autonomy settings. |
| **VS Code** | Broad editor, language-server and debugging ecosystem | Install only approved extensions and run tests before merging an AI-assisted patch. | Extension marketplace and workspace trust. |
| **Zed** | Fast editor for agent-assisted project work | Use reviewable patches and source-control diffs while isolating provider and model configurations. | Extension access and cloud settings. |
| **Cline** | User-supervised coding agent extension | Restrict file system/terminal commands and use actual tests to decide whether proposed edits are acceptable. | Tool side effects and token expenditure. |
| **Aider** | Terminal-oriented AI pair programming | Scope it to a small branch, use model provider credentials only in secure storage, and review every proposed code change. | Shell/repo access and API billing. |
| **Sourcegraph Cody** | Code search and developer assistance alternative | Query authorized repository context for explanations or safe refactoring suggestions, then independently test modifications. | Repository indexing disclosure. |
| **JetBrains IDEs** | Mature development environment with coding tools | Use type-checkers, debugger, Git diffs and optional AI features within a user-controlled project. | Plugins and telemetry choices. |
| **Neovim** | Extensible terminal editor and language servers | Combine LSP/test plugins with an optional approved model client while keeping human review of generated code. | Plugin supply chain. |
| **Tabnine** | Code completion and developer assistance alternative | Evaluate completion quality against local tests and verify whether selected configuration keeps context private. | Model hosting and organization terms. |
| **VSCodium** | Editor distribution alternative | Add only audited extensions and use local linters, tests and Git in an isolated project. | Extension supply chain. |
| **OpenCode** | Agentic coding terminal application alternative | Run a controlled coding request on a disposable repo; lock read/write/command permissions before testing. | Tool execution and chosen model route. |

## 5. Agent, orchestration and tool-calling software frameworks

Libraries for building model-backed applications; adopting one does not automatically create durable memory, secure authority or autonomous workers.

| Option / alternative | Why someone might consider it | How a developer could use it | Review before use |
| --- | --- | --- | --- |
| **DSPy** | Optimizing prompts and model programs | Evaluate candidate prompt changes against a frozen development set and a separate holdout test set. | Evaluation data quality and model costs. |
| **LangChain** | Broad integrations and retrieval/application patterns | Prototype source retrieval and model responses with fixed test cases before allowing new connectors. | Dependency sprawl and prompt-injection exposure. |
| **Spring AI** | Java ecosystem model integrations | Attach an approved model adapter to a Spring service, preserve typed inputs and constrain data exchange. | Java/cloud service configuration. |
| **Vercel AI SDK** | TypeScript streaming and provider integrations | Build a user interface that streams typed responses from a chosen model route and validates returned data. | Provider routing and front-end leakage. |
| **CrewAI** | Role-oriented collaborative agent workflows | Simulate planners/reviewers on synthetic work, store independently produced artifacts and manually verify conclusions. | Role labels do not prove independent models. |
| **OpenAI Agents SDK** | Agent handoffs and tool calling | Create a bounded agent with typed tools and capture traces, requiring owner approval before protected actions. | API/provider data and external calls. |
| **LlamaIndex** | Data-to-model retrieval and agent workflows | Ingest permitted synthetic records, compare exact citation recall and benchmark parser accuracy. | Source licensing and over-broad indexing. |
| **Mastra** | TypeScript agent and workflow tooling | Define TypeScript step graphs, runtime schemas and tests before attaching any paid model endpoint. | Service persistence and secrets. |
| **Letta** | Memory-focused agent architecture | Compare persisted facts and summarization across restarts without allowing a memory record to become privileged instructions. | Memory privacy and poisoning. |
| **LangGraph** | Graph workflows with state persistence and interruption | Model tasks as explicit states, require pause/resume tests and route external actions through approvals. | Checkpoint privacy and stale authority. |
| **smolagents** | Minimal agent coding patterns | Prototype a no-network, read-only agent and inspect every generated tool action before enabling it. | Code execution and arbitrary tools. |
| **AutoGen (legacy)** | Historical multi-agent experimentation reference | Examine older examples only after checking active maintenance and migration to newer supported frameworks. | Archived/deprecated component risk. |
| **Model Context Protocol (MCP)** | Standardized exposure of tools and resources | Build read-only, least-privilege tool descriptors, pin tool versions and require approval for new capabilities. | Malicious connectors and changed tool definitions. |
| **Strands Agents** | Agent runtime and tool composition option | Construct a tool allowlist, attach a sandboxed model interface and trace every proposed action. | Cloud and tool privilege boundaries. |
| **Microsoft Agent Framework** | .NET/Python multi-agent workflows | Evaluate documented agent handoffs, durable checkpoints and human-in-the-loop gates in a synthetic app. | Framework migration and connected service roles. |
| **Agent-to-Agent (A2A) protocol** | Cross-agent message interchange candidate | Exchange narrow signed or authenticated task envelopes, test replay protection and treat external agent claims as untrusted. | Identity, provenance and role grants. |
| **Agno** | Lightweight multi-agent and knowledge orchestration | Evaluate a simple model + tool + memory prototype under synthetic data with deterministic action receipts. | Plugin loading and storage. |
| **Google Agent Development Kit** | Google-oriented agent development | Prototype well-scoped agents, tool cards and state transfers with independent tests; keep provider choices explicit. | Provider connections and cloud scope. |
| **Semantic Kernel** | Enterprise-style AI integration library | Wrap business functions behind typed callable interfaces and check logging, identity and permission boundaries. | Cross-service identity and data flow. |
| **Haystack** | Search pipelines and RAG components | Build a parser/retriever/reranker chain using permitted documents and measure answer grounding. | Document rights and connector permissions. |
| **PydanticAI** | Typed agents and validated structured outputs | Define a narrow tool schema, validate returned data, and reject unsafe action requests before execution. | Model routing and tool permissions. |
| **AG2** | Multi-agent conversation orchestration | Test real distinct worker outputs with an immutable assignment and reviewer rubric rather than role-playing a single answer. | Tool execution and reviewer independence. |

## 6. Workflows, schedulers, queues and collaboration automation

Automations are optional; a chat message by itself does not schedule a running task or authorize external communications.

| Option / alternative | Why someone might consider it | How a developer could use it | Review before use |
| --- | --- | --- | --- |
| **cron / Task Scheduler** | Built-in periodic local scheduling | Trigger nonprivileged health checks with explicit log rotation and a stop/remove procedure. | Background persistence and overlapping jobs. |
| **Zapier** | Cross-app automation as a service | Trial a read-only workflow with test accounts and examine what external data the Zap can access. | Connector privileges and recurring charges. |
| **Inngest** | Event-driven background workflows | Use a synthetic webhook trigger and deterministic job receipt, then audit deduplication/retry behavior. | External webhook security. |
| **systemd timers** | Local Linux scheduled tasks | Start an approved maintenance check with logs, bounded permissions and documented stop controls. | Unattended execution. |
| **Celery** | Python distributed task queues | Queue an idempotent background job with retries, owner tracking and worker-side permission checks. | Redis/broker storage and runaway jobs. |
| **GitLab CI/CD** | Alternative source-control automation | Define a safe pipeline for lint, tests and artifact signing, not deployment, until release approval. | CI tokens and secrets. |
| **Argo Workflows** | Kubernetes-native job graphs | Run a contained evaluation DAG with service-account limits and resource quotas. | Cluster privileges and paid infrastructure. |
| **n8n** | Self-hostable and hosted workflow automation | Use a tightly scoped automation with disabled production credentials, then audit every node and destination. | Credentials, outbound calls and update policy. |
| **Make** | SaaS task integrations | Test a narrow workflow with synthetic webhooks and minimal connector scope before enabling real accounts. | Third-party data and operation volume. |
| **Windmill** | Script-based internal workflows | Create typed input jobs and require approval between plan and execution; log nonsecret results. | Workspace permissions and scripts. |
| **Temporal** | Durable workflow execution | Represent task retries and compensation logic as workflows and verify behavior after a simulated worker crash. | Persistent services and idempotency. |
| **Dagster** | Data pipeline lineage and reliability | Schedule a test ETL pipeline with observable step outputs and no private source content. | Cloud workers and connector permissions. |
| **Apache Airflow** | Scheduled data DAGs | Model deterministic evidence collection as a DAG and keep user data off shared workers without consent. | Infrastructure and task credentials. |
| **Activepieces** | Visual workflow automation | Configure a hypothetical read-only notification flow and require explicit owner approval before any external send. | OAuth scopes and hosted execution. |
| **Node-RED** | Visual event and device orchestration | Simulate incoming events with generated data and keep actuators disconnected until authority is designed. | Local network devices and plugins. |
| **GitHub Actions** | CI/testing for repositories | Run an isolated test matrix with read-only token permissions and no secrets on untrusted PRs. | Workflow injection and token privileges. |
| **Prefect** | Python flow orchestration | Store retry and task state with explicit checkpoints; check failure recovery using controlled synthetic data. | Hosted agent/service connections. |

## 7. Databases, memory, retrieval and knowledge search

Persistence and retrieval are different from truth. All user data stores need encryption/access controls and tested backups as appropriate.

| Option / alternative | Why someone might consider it | How a developer could use it | Review before use |
| --- | --- | --- | --- |
| **Redis + vector search** | Fast caches and optional retrieval | Cache nonsecret task results behind TTL and prevent cache data from becoming a source of truth. | Network exposure and persistence settings. |
| **SQLite FTS5** | Minimal offline text search | Store authorized documents in a small local DB and use full-text queries to retrieve exact source lines. | Database path, backups and data minimization. |
| **OpenSearch** | Search and analytics backend | Build source-aware full-text or vector queries behind authentication and monitor query privileges. | Managed index leakage and network services. |
| **PostgreSQL + pgvector** | Durable relational and vector memory | Keep tasks in relational tables with explicit schemas while scoring cited embeddings in separate indexed columns. | Server credentials and backup/restore. |
| **MinIO** | S3-compatible object storage option | Save encrypted approved artifacts with versioned manifests and test immutable references without public buckets. | Bucket policies and exposed endpoints. |
| **Qdrant** | Structured vector search with filtering | Search a tagged approved corpus by source rights and document version, returning citations for review. | Collection access and deployment. |
| **Milvus** | Dedicated vector similarity service | Test large synthetic embedding retrieval with dimension and batch sizing controls before provisioning production. | Distributed service security. |
| **DuckDB** | Embedded analytical SQL engine | Compute statistics on offline benchmark outputs without uploading raw training or user data. | Local file access and memory. |
| **Neo4j** | Graph relationships and citations | Represent source-author-event links, then require every claimed edge to carry a real citation and date. | Graph permissions and invented relationships. |
| **Elasticsearch** | Mature text, analytics and optional vector search | Index public sample material and test that protected records cannot be queried by unauthorized roles. | Service licensing and operational footprint. |
| **MariaDB** | Relational alternative for persistent task data | Store normalized task/approval relations and verify transactions and point-in-time backups. | Role-based database privileges. |
| **Vespa** | Large-scale search and relevance serving | Prototype a hybrid retrieval service and compare relevance metrics on permitted reference documents. | Cluster complexity and resource cost. |
| **Weaviate** | Vector/keyword search with metadata | Compare retrieval with controlled metadata filters for license, language and trusted source class. | Cloud self-hosting choice and API scope. |
| **Meilisearch** | Fast search-driven UI indexing | Build a local searchable test catalog and prevent public endpoints from revealing protected text. | Index API exposure. |
| **Typesense** | Search-as-you-type and hybrid lookup | Provide a responsive source-title search while retaining links to original documents for verification. | API keys and public-search indexing. |
| **FAISS** | Local similarity-search library | Create a tiny vector index for synthetic text and compare exact nearest-neighbor results with a baseline. | Embedding privacy and index license. |
| **Chroma** | Vector-retrieval prototypes | Insert a few permitted passages and track which citation anchors are returned to an AI. | Stored embeddings and collection access. |
| **LanceDB** | Embedded vector/data search options | Index a documented synthetic corpus with source IDs and reversible deletion tests. | Embedding model and embedded-file access. |

## 8. Encyclopedias, archives, research and other large knowledge sources

Every source here is a candidate for discovery; a source being publicly accessible does not grant commercial redistribution, bulk copying or model-training rights.

| Option / alternative | Why someone might consider it | How a developer could use it | Review before use |
| --- | --- | --- | --- |
| **Wikipedia** | Broad multilingual encyclopedia | Use a dated article revision for background context and cross-check its citations with authoritative sources. | CC BY-SA and stale information. |
| **Kiwix Library** | Offline ZIM reference archives | Download only chosen permitted packages, maintain a source manifest and verify a local reader retrieves a page. | Archive license and stale snapshots. |
| **Project Gutenberg** | Historical and public-domain books | Filter by individual work and jurisdiction, then retain edition, author and provenance for legitimate offline use. | Exceptions, trademark and bulk-download terms. |
| **Wikibooks** | Open collaborative teaching material | Index only permitted learning pages with authorship, page revision and license notes. | Attribution/share-alike and corrections. |
| **Data.gov** | US public dataset discovery | Select exact agency datasets, record date/schema and inspect third-party content rights before ingestion. | Updates and data quality. |
| **EBRAINS / siibra** | Brain atlas and study discovery | Build a source crosswalk across atlases and verify coordinates, species and licenses for each dataset. | Dataset licenses differ from software license. |
| **Library of Congress** | Historical documents and media | Link catalog records and inspect item rights before downloading or republishing documents/images. | Individual collection rights. |
| **Smithsonian Open Access** | Museums and research reference materials | Filter open-access assets, retain identifiers and maker/source attribution, check any item-specific restrictions. | Trademark/publicity and rights statements. |
| **Biodiversity Heritage Library** | Natural-history reference works | Use item/volume bibliographic records, check public-domain status for each region and extract permitted passages. | Historical science can be outdated. |
| **PhET** | Interactive science education simulations | Open the official simulation in a learner's browser or reference its metadata; license any offline bundle separately. | Noncommercial and software-specific terms. |
| **Semantic Scholar** | Paper search and citation graph discovery | Find influential related research and retrieve bibliographic IDs, confirming originals before citing. | API terms and paper rights. |
| **OpenStax** | Educational textbooks | Use licensed chapters as learning references with version and attribution checks; do not presume every supplemental asset shares the textbook license. | Text/asset terms. |
| **OpenAlex** | Scholarly metadata and discovery | Identify works/authors/venues and link DOIs; use source metadata to cross-check claims rather than copy paywalled papers. | Work-level copyright. |
| **iFixit** | Repair procedures and parts knowledge | Reference official repair guides for private reading; avoid bundling content, training on it or using it commercially without rights review. | Noncommercial/share-alike and AI-training restrictions. |
| **National Archives (US)** | Primary federal historical records | Prefer catalog/record links and date/source provenance rather than reposting raw scans indiscriminately. | Third-party and privacy exceptions. |
| **Allen Brain Atlas** | Anatomical and cell-type data sources | Align species, tissue coordinates and studies before comparing model predictions with public measurements. | Dataset permissions and scientific provenance. |
| **Crossref** | DOI and bibliographic metadata | Resolve published work versions and citation relationships, checking paper license separately from metadata. | Abstract and publisher copyright. |
| **Internet Archive** | Historical media and document discovery | Point to item metadata; download only where access rights and explicit license permit that use. | Public access is not redistribution permission. |
| **Wikimedia Commons** | Images, audio and media | Filter files by individual license, author, attribution and reuse purpose rather than copying whole categories. | Personality/trademark and CC terms. |
| **HathiTrust** | Library digitization and bibliographic data | Search metadata and obtain only texts where access and reuse rules explicitly allow downloads. | Copyright and partner terms. |
| **MIT OpenCourseWare** | University course materials | Reference open teaching pages or independently licensed PDFs with proper attribution. | Noncommercial/derivative rules vary by asset. |
| **USGS** | Earth science, terrain and hazard datasets | Map authoritative data layers by collection/date, preserving uncertainty and location scope. | Licenses, agency conditions and stale hazards. |
| **OpenStreetMap** | Geospatial map data | Use area extracts with required ODbL attribution and update checks instead of copying a commercial map service. | Share-alike obligations and privacy. |
| **NOAA** | Weather, oceans and climate data | Retrieve official datasets for a specified place/time and keep observation dates and usage rules attached. | Live alerts outrank cached files. |
| **Zenodo** | Research datasets and reproducible artifacts | Prefer DOI-tagged official releases with explicit source, license and integrity manifests for any local copy. | Per-record licensing and author attribution. |
| **NeuroMorpho.Org** | Neuron reconstruction datasets | Inspect morphology species, original study and attribution rules before geometry import. | CC attribution and original-paper citation. |
| **Open Library** | Book catalog and lending discovery | Index bibliographic metadata and external identifiers rather than downloading restricted full texts. | Access restrictions and copyright. |
| **NASA Earthdata** | Earth-observation scientific datasets | Access via approved account if needed; record data products, calibration and public-use constraints. | Entitlements, storage and provenance. |
| **Wiktionary** | Dictionary and translation entries | Provide disambiguation and multilingual terminology lookup with retained source and revision IDs. | CC attribution and inaccurate entries. |
| **PubMed** | Biomedical publication indexing | Search PMID records and follow citations to original studies, tracking retractions and publication dates. | Abstract/full-text rights differ. |
| **NIH NCBI Bookshelf** | Biomedical book/reference lookup | Retrieve official chapter and citation metadata for a bounded research question, respecting each book's rights. | Medical reliance and content terms. |
| **arXiv** | Preprints and scientific manuscripts | Identify version and publication status, then compare claims to journal papers and replications when available. | Preprint uncertainty and paper copyright. |
| **Wikidata** | Structured public-entity reference | Query entity IDs and citation qualifiers, checking original references before treating a property as settled fact. | Source errors and freshness. |
| **Federal Register / eCFR / GovInfo** | Public legal and regulatory records | Query official source and effective date, then distinguish proposed from operative rules and verify applicability. | Jurisdiction and temporal validity. |
| **Europeana** | Cultural-heritage resource catalog | Use collection/item identifiers and Europeana rights statements to choose truly reusable objects. | Rights vary per item. |
| **BigBrain Project** | High-resolution neuroanatomical datasets | Evaluate sample geometry, coordinate space and documented segmentation on a small noncommercial test first. | Dataset-specific noncommercial licensing. |

## 9. Document parsing, ingestion, browsers and data preparation

Reading a document and executing instructions found inside it must remain separate security operations.

| Option / alternative | Why someone might consider it | How a developer could use it | Review before use |
| --- | --- | --- | --- |
| **Calibre** | E-book organization and conversion | Catalog legitimately obtained books and convert only where license and copy protection allow it. | Copyright/DRM and metadata. |
| **Docling** | Structured PDF and document conversion | Convert approved files into source-labeled blocks, retaining page references and verifying tables manually. | OCR data and conversion errors. |
| **PyMuPDF** | Fast PDF text, image and page processing | Extract bounded segments with page identifiers from legally accessible PDFs and compare output to originals. | License/reuse and PDF security. |
| **pypdf** | PDF document manipulation in Python | Extract or split owner-provided PDFs without external service calls and validate extraction boundaries. | Embedded metadata and legal rights. |
| **Playwright** | Reproducible browser UI testing | Automate a disposable test web app with synthetic accounts and human approval before touching live accounts. | Auth cookies and browser permissions. |
| **GROBID** | Scholarly PDF structure extraction | Extract title/authors/references from user-owned papers and validate each parsed DOI against the original. | Parser errors and article rights. |
| **MarkItDown** | Convert common content to Markdown | Use on nonsecret documents and inspect output for hidden metadata and dropped tables. | Parser execution and file content scope. |
| **OCRmyPDF** | Add searchable OCR layer to PDFs | Process permitted scans locally and verify text accuracy without uploading original documents. | Resource use and sensitive scans. |
| **Selenium** | Browser automation and test suite | Run test interactions in a dedicated browser profile against an owned or authorized test environment. | Account authorization and challenge handling. |
| **Apache Tika** | Multi-format content detection/extraction | Extract text from synthetic documents in a resource-limited service and retain original filename/version mapping. | Java/parser attack surface. |
| **Tesseract OCR** | Local text recognition from images | Run on nonprivate scan samples, compare result with image and store OCR uncertainty rather than treating it as fact. | Scan rights and recognition errors. |
| **Zotero** | Citation and source organization | Save stable citation metadata and attach only authorized copies; export clean bibliographies for evidence reports. | Sync privacy and attached files. |
| **trafilatura** | Article text extraction | Clean publicly permitted HTML snapshots, attach URLs and dates, and avoid sites requiring authorization or prohibited scraping. | Publisher access and copyright. |
| **Scrapy** | Structured site-crawling framework | Crawl only a publisher-authorized small dataset under rate limits and source licensing checks. | Site terms, robots and overcollection. |
| **Unstructured** | Heterogeneous file ingestion pipeline | Partition synthetic PDFs/HTML/email into typed chunks, then discard unsupported content before embedding. | Sensitive metadata and dependencies. |
| **Pandoc** | Document format conversion | Transform a user-owned Markdown document into accessible publishing formats with citation and heading checks. | Template dependencies and copied content. |
| **Beautiful Soup** | HTML parsing library | Parse locally saved permitted sample pages to extract structured metadata without running webpage instructions. | Crawl/access terms and malformed HTML. |

## 10. Testing, quality assurance, observability and model evaluation

The primary acceptance oracle is independently repeatable tests and verifiable source data, not a model's unsupported 'PASS'.

| Option / alternative | Why someone might consider it | How a developer could use it | Review before use |
| --- | --- | --- | --- |
| **Hypothesis** | Property-based Python tests | Generate edge cases for transaction, path and parser functions rather than relying only on hand-selected examples. | Test seed reproducibility. |
| **Locust / k6** | Load and reliability testing | Generate synthetic concurrent requests against an owned local service and validate rate limits before production. | Do not stress public sites. |
| **LangSmith** | Agent traces and dataset evaluation | Replay a bounded task dataset and compare each release's step traces with a human-reviewed baseline. | Provider-hosted trace content. |
| **Braintrust** | Experiment comparisons for LLM apps | Compare model/prompt versions on fixed public inputs and store verified per-case deltas. | Third-party event storage. |
| **Garak** | LLM vulnerability probing | Run bounded, authorized synthetic adversarial prompts against a test model endpoint with no external actions. | Test scope and resource use. |
| **OpenTelemetry** | Portable tracing instrumentation | Emit nonsecret task durations, tool names and errors into an approved collector; redact source content before export. | Trace leakage and endpoint config. |
| **mypy / Pyright** | Static Python type checking | Fail builds where data schema and optional values can cause unsafe call or state assumptions. | Plugin/runtime differences. |
| **Langfuse** | LLM tracing and prompt iteration | Log versioned prompt IDs and sanitized tool outcomes; compare actual costs and latency before changing models. | Prompt content privacy and hosted storage. |
| **Promptfoo** | Prompt and model regression tests | Run a frozen synthetic prompt suite across candidate models and compare failures, refusals and citation quality. | Hosted/cloud eval settings. |
| **ruff + pre-commit** | Fast linting and commit-time checks | Add deterministic formatting and secret-check hooks that must pass before accepting contributions. | Tool version pinning and skipped hooks. |
| **Grafana + Prometheus** | Operational metrics and dashboards | Observe nonsecret queue delay, process health and error rates without logging full user prompts. | Open dashboards and retention. |
| **Arize Phoenix** | Traces and retrieval evaluation | Review agent spans and evidence support on synthetic questions before trying it on sensitive workloads. | Hosted vs self-hosted telemetry. |
| **Sentry** | Application error monitoring | Capture redacted exceptions and stack traces, checking that logs do not include credentials or private paths. | Cloud telemetry and retention. |
| **pytest** | Practical automated Python test suite | Capture command, environment, exit code and failure artifacts for each implementation change. | Test fixtures must contain no secrets. |
| **OWASP ZAP** | Web application dynamic security testing | Scan only a local test site with explicit authorization and report high-confidence issues without touching third-party services. | Scanner scope and active requests. |
| **MLflow** | Experiment/model artifact tracking | Record model revision, metrics, parameters and provenance on a controlled training experiment. | Artifact leakage and remote backends. |
| **coverage.py** | Code coverage analysis | Measure untested branches of the offline reference implementation and add regression tests before claiming reliability. | Coverage not proof of security. |
| **W&B Weave** | Model and agent call observation | Track prompt versions, evaluation outputs and latency for permitted datasets and endpoints. | Project visibility and telemetry. |
| **DeepEval** | LLM test assertions and evaluation | Add answer groundedness and tool-calling correctness checks with synthetic ground-truth examples. | Judge-model uncertainty and spend. |
| **Inspect AI** | Structured model evaluation experiments | Build a reproducible model benchmark with recorded tasks, sample sizes, scorer versions and raw results. | Evaluation harness code and model access. |
| **Ragas** | Retrieval-augmented answer evaluation | Measure context relevance and faithfulness using a held-out, licensed document test set. | Evaluation metric/model bias. |

## 11. Privacy, source code, supply chain and identity safeguards

Security tools provide evidence and guardrails, not absolute protection. All scanning and testing must be authorized.

| Option / alternative | Why someone might consider it | How a developer could use it | Review before use |
| --- | --- | --- | --- |
| **1Password / Bitwarden / OS keychain** | Credential storage and approval option | Keep accounts and tokens in trusted key stores, passing short-lived scoped handles instead of plaintext in chat. | Vault access and user authentication. |
| **Renovate** | Automated dependency update proposals | Generate reviewable PRs for pinned dependency bumps, requiring tests and owner merge approval. | Auto-merge and untrusted updates. |
| **age** | Small-file encryption utility | Encrypt local backup keys or transport bundles for named recipients, retaining offline recovery procedures. | Key loss and recipient mistakes. |
| **Tailscale** | Encrypted device-to-device overlay networking | Connect only specifically approved devices with access policies and service allowlists. | Network identity and unintended exposure. |
| **HashiCorp Vault** | Centralized policy-controlled secret lifecycle | Use short-lived credentials and audit per-tool access instead of exposing secrets to prompts or environment dumps. | Dedicated service and authority. |
| **Gitleaks** | Detect accidentally committed secret patterns | Scan staged changes and historical commits before a release; rotate real secrets found. | Hash pattern coverage and public history persistence. |
| **CodeQL** | Code security analysis | Run scoped static checks on a controlled codebase and review findings before merging patches. | Analysis coverage and repository permissions. |
| **Dependabot** | Repository dependency alerts and updates | Review patches on pinned dependencies and run tests before any human-approved merge. | GitHub dependency access. |
| **detect-secrets** | Baseline credential patterns in source code | Maintain a reviewed allowlist for known false positives and fail on newly introduced real secrets. | Baseline quality. |
| **WireGuard** | Explicit encrypted network tunnel | Establish a minimal device-to-device tunnel only after a threat-model and access-rule review. | Endpoint and firewall configuration. |
| **Grype** | Dependency vulnerability scanning | Check a pinned software-bill-of-materials against disclosed advisories and document updates. | Database freshness and false positives. |
| **Semgrep** | Pattern-based code review | Add rules for sensitive shell execution, SQL operations and exposed endpoints; review findings manually. | Rulesets and code confidentiality. |
| **Sigstore Cosign** | Software artifact signing and verification | Validate provenance/signatures of a release or container before distributing it to users. | Signing-key control and trust roots. |
| **SOPS** | Secret-file encryption in version-controlled workflows | Encrypt approved configuration values and require operator-controlled keys; never commit decrypted values. | Key management. |
| **Cedar** | Attribute-based authorization policies | Define subject/action/resource grants and test denials for secret reads, payments and publishing before integrating tool runners. | Policy and identity correctness. |
| **OpenSSF Scorecard** | Open-source dependency health checks | Assess maintainers' release controls, branch protection, token practices and vulnerability hygiene before adoption. | Heuristic score, not safety certificate. |
| **Trivy** | Scanner for dependencies, containers and configuration | Scan images and files for known vulnerabilities and misconfigurations before running them. | Advisory coverage and network updates. |
| **OWASP Dependency-Check** | Vulnerable component detection | Inventory third-party libraries in an authorized build and gate upgrades on verified advisories. | False matches and data freshness. |
| **TruffleHog** | Secret discovery in authorized repositories | Examine sanitized findings in a repository you own and revoke discovered live credentials quickly. | Scan scope and sensitive matches. |
| **Syft** | Generate a software bill of materials | Record exact dependencies in a distributable package and compare against a licensed approved manifest. | Incomplete runtime dependencies. |
| **Open Policy Agent** | Authorization policy decision engine | Check planned external action against explicit owner, role and data-class rules before any executor runs. | Policy drift and misconfiguration. |
| **Bandit** | Python source security linting | Review unsafe subprocess, temporary-file and deserialization patterns in a synthetic project. | Static-analysis false positives. |
| **OpenTofu / Terraform security rules** | Infrastructure configuration review | Preview resource changes and block public networks or secrets before an authorized deploy. | State files and cloud cost. |
| **OSV-Scanner** | Open-source vulnerability matching | Scan manifest or lockfile versions and document affected packages without silently upgrading them. | Advisory completeness. |
| **Snyk** | Security-scanning service alternative | Inspect selected dependency or code vulnerabilities under approved repository access, then compare with other scanners. | External source-code disclosure. |
| **GitHub private vulnerability reporting** | Confidential inbound security reports | Provide a private channel for a researcher to report a flaw without public exploit disclosure. | Platform accounts and reporter guidance. |

## 12. Interfaces, APIs, apps and deployment surfaces

Publishing a user interface is a separate security event; a localhost-only experiment is not automatically suitable for a public website.

| Option / alternative | Why someone might consider it | How a developer could use it | Review before use |
| --- | --- | --- | --- |
| **Firebase** | Managed authentication/data hosting option | Validate rules against synthetic role tests and never expose secrets or confidential data in client code. | Cloud data policies and quotas. |
| **HTMX** | Server-rendered interface enhancement | Add minimal interactive status navigation to a protected server while validating every state mutation separately. | Backend auth and CSRF. |
| **Render** | App hosting alternative | Deploy a staged nonsecret service with health checks and explicit rollback plan. | Network exposure and running charges. |
| **Flask** | Small Python web endpoint | Render an offline training UI with escaping, explicit Host checks and no write actions. | Development server not for production. |
| **Cloudflare Workers** | Edge-hosted API and web functions | Deploy a synthetic demo behind authentication and rate-limiting only after data-processing and release approval. | Cloud requests and billable usage. |
| **Electron** | Web-tech desktop application wrapper | Package a controlled local interface using context isolation and restricted IPC bridges. | Large dependency/update surface. |
| **PySide / Qt** | Native GUI applications | Build a no-network desktop task reader with OS-native file pickers and visible permission prompts. | GUI event/privilege boundaries. |
| **Supabase** | Hosted Postgres/auth/storage alternative | Check row-level access policies using test identities before any personal data is stored. | Public client keys vs service keys. |
| **Django** | Web application framework with permissions and models | Prototype a multiuser system with test roles and authorization checks at every database query. | Authentication and internet hosting. |
| **Streamlit** | Rapid data dashboard prototyping | Display synthetic task metrics from a read-only data source without exposing a web listener to the Internet. | Session secrets and remote sharing. |
| **FastAPI** | Typed Python service endpoints | Expose strictly read-only health/status routes to loopback with input validation and no credential data. | Unauthenticated service exposure. |
| **Tauri** | Desktop app shell alternative | Wrap a local status dashboard with narrowly scoped filesystem commands and run packaging/security tests. | Native bridge permission design. |
| **SvelteKit** | Modern reactive frontend/server framework | Build a lightweight source navigator using an approved read-only JSON API. | Server actions and SSR data exposure. |
| **Railway** | Managed app/database deployment | Use a temporary test project with spending cap and fake records to compare operability. | Account secrets and paid resources. |
| **Gradio** | Quick model/demo interactive components | Test a small local model with fabricated inputs and no unrestricted public sharing links. | Upload retention and exposed demo URLs. |
| **Next.js** | Full-stack React web application framework | Build a public demo using fake data and separate API endpoints, keeping private state server-side. | Server functions and external analytics. |
| **Vercel** | Managed web deployment alternative | Host only a deliberately public demonstration with synthetic data and inspect build-time environment variables. | Deployment and third-party logging. |
| **Cloudflare Pages / Netlify static site** | Documentation publication options | Publish only public-safe Markdown and generated HTML with no analytics or personalized tracking by default. | Hosting account and privacy. |
| **Netlify** | Static site/function hosting candidate | Publish read-only documentation or fake-data demo once repository source and legal rights are approved. | Build logs and service tokens. |
| **Flutter** | Cross-platform UI toolkit | Build a client that displays sanitized task status while protecting local file and network permissions. | Platform signing and data storage. |
| **JupyterLab** | Notebook interface for experiments | Execute only synthetic datasets and export reproducible scripts/tests before sharing a result. | Notebook metadata and server exposure. |
| **Fly.io** | Application hosting on managed machines | Trial a geographically scoped service with secrets manager and restricted ports. | Region, VM and network configuration. |
| **React** | Component-based UI library | Render a task board from sanitized JSON, rejecting HTML injection and never putting API keys in browser bundles. | Client-side data leaks. |

## 13. Speech, images, video, accessibility and model training

Media often contains identifiable faces/voices and copyrighted material; use synthetic or consented samples and review the specific training or generation rights.

| Option / alternative | Why someone might consider it | How a developer could use it | Review before use |
| --- | --- | --- | --- |
| **MLX** | Apple silicon ML and inference tools | Evaluate a compatible model locally with explicit memory, precision and accuracy measurements. | Model compatibility and licensing. |
| **Tesseract** | Image-to-text OCR | Process a mock receipt or fabricated screenshot locally, then validate every extracted value against the source. | Recognition errors and metadata. |
| **LLaMA-Factory** | Fine-tuning experiments across supported families | Compare approved adaptation recipes only on datasets with demonstrable training rights. | Configuration and data governance. |
| **Roboflow / FiftyOne** | Computer vision dataset and inspection tools | Validate detection ground truth on synthetic/consented images and document annotation quality. | Hosted image privacy and copyright. |
| **ComfyUI** | Composable visual generation workflow UI | Create controlled image workflows using checked model components and locally generated assets. | Custom node execution and model rights. |
| **Kokoro TTS** | Speech synthesis model family | Test an exact legally permitted voice checkpoint locally and review audio quality and accent suitability. | Voice weights and language coverage. |
| **Stable Diffusion ecosystem** | Local image-generation options | Use appropriately licensed model weights and original prompts for illustrative media assets; retain provenance. | Training rights and image likeness. |
| **PEFT / LoRA** | Parameter-efficient adaptation of licensed models | Fine-tune on rights-cleared synthetic examples and verify no unintended memorization. | Original weight and training-data terms. |
| **DVC** | Dataset and model artifact versioning | Track checksums and source manifests separate from Git while storing large assets in a user-approved location. | Storage permissions and source rights. |
| **ElevenLabs** | Commercial voice and audio synthesis options | Produce a test narration from authorized voices, tracking licensing and consent for each voice. | Voice consent and subscription costs. |
| **Piper TTS** | Local speech synthesis candidate | Generate an offline accessibility narration using voice assets with explicit use rights. | Voice/model terms. |
| **Unsloth** | Fine-tuning and inference optimization tooling | Compare low-memory adaptation steps against a reproducible public-data baseline. | Environment dependencies and model licenses. |
| **FFmpeg** | Audio/video preprocessing | Trim or transcode legally owned recordings offline before a separate consented analysis pipeline. | Copyright and embedded metadata. |
| **JAX** | Functional accelerator-based ML computation | Prototype gradient/optimization experiments with deterministic test inputs and compare reference calculations. | Hardware/backend and reproducibility. |
| **Google MediaPipe / OpenPose alternatives** | Human pose and gesture interfaces | Use local video samples with participant consent and test for false detection before action triggers. | Biometric storage and mistaken actions. |
| **AssemblyAI** | Cloud audio intelligence API | Analyze only consented synthetic speech for diarization or topic summaries with retention limits. | Third-party audio and billing. |
| **OpenCV** | Computer vision processing and image analysis | Detect visual features on synthetic images and save only aggregate results unless content retention is approved. | Personal imagery and bias. |
| **MediaPipe** | Vision, gesture and on-device perception | Run landmark experiments on a consented sample or synthetic camera feed without transmitting frames. | Biometric privacy and false positives. |
| **Argilla** | Dataset curation and feedback workflows | Capture quality judgments on model outputs, retaining evaluation criteria without uploading private prompts. | Hosted datasets and access rights. |
| **Whisper / faster-whisper** | Speech-to-text transcription alternatives | Transcribe a synthetic or consented audio sample, compare word-error rate and remove identifying metadata. | Speaker privacy and language errors. |
| **Deepgram** | Hosted speech APIs | Send only opt-in audio for a short transcription benchmark with deletion and retention policies reviewed. | Remote voice data. |
| **Pytorch** | Neural-network training and inference | Train a toy model on generated data with versioned seeds and separate validation metrics. | Hardware, packages and training data rights. |
| **Qwen VL / LLaVA families** | Vision-language model candidates | Ask grounded questions about nonprivate diagrams and measure agreement with verified annotations. | Model licenses and image leakage. |
| **Hugging Face Transformers** | Model loading and experimentation library | Fetch only approved pinned model revisions and run synthetic benchmark tasks with provenance. | Remote code execution flags and model cards. |
| **Label Studio** | Human annotation and labeling workbench | Prepare a small non-identifying dataset for expert review with clear annotator rights and export rules. | Annotation confidentiality and cloud. |

## 14. Source control, packaging, testing environments, backup and recovery

Multiple interchangeable choices; cloud sync, CI runners and backups may copy private data, so configure and test each access boundary.

| Option / alternative | Why someone might consider it | How a developer could use it | Review before use |
| --- | --- | --- | --- |
| **OpenSSF Scorecard / SBOM standards** | Open-source supplier transparency | Record upstream maintenance, dependencies and artifact hashes so a release reviewer can evaluate exposure. | Scores and manifests can be incomplete. |
| **Terraform / OpenTofu** | Declarative infrastructure-as-code alternatives | Preview resource configuration changes, including unwanted network/public storage, before human-approved deployment. | State may include secrets and cost. |
| **GitLab** | Source-control, CI and issue management | Maintain reviewed merge requests and isolated pipelines using synthetic artifacts for any public project. | Cloud vs self-hosted data. |
| **GitHub** | Distributed version control hosting and review | Use public-safe docs only or a private repo for sensitive work, enabling protected merge/review workflows. | Commit metadata is persistent and public in public repos. |
| **GitHub Actions / GitLab CI** | Automated code testing after source changes | Run test matrices on generated public fixtures, withholding protected workflow tokens from untrusted contributions. | Build secrets and third-party actions. |
| **Ansible** | Repeatable host configuration recipes | Apply an idempotent dry-run to a lab machine using limited permissions, retaining a clear rollback plan. | Remote privileged execution. |
| **Time Machine / ZFS / Btrfs snapshots** | Local version and rollback options | Capture an offline snapshot before a project upgrade and verify restored files against manifests. | Snapshots are not isolated secure backups. |
| **Bitbucket / Azure DevOps** | Alternative Git hosting and enterprise pipelines | Enforce review and issue traceability with least-privilege CI identities. | Provider/project data access. |
| **Nix** | Reproducible package and development environments | Pin build inputs and compare a clean build across supported systems before public release. | Dependency provenance and binary caches. |
| **restic** | Encrypted backup automation | Snapshot approved files to a chosen encrypted location and test recovery before relying on it. | Repository credentials and retention policy. |
| **GitHub Codespaces** | Hosted development environments | Spin up a disposable public demo repo with limited secrets, then destroy the environment after tests. | Cloud compute and source data. |
| **BorgBackup** | Encrypted, deduplicated backups | Back up only user-approved project folders, then prove restore into a separate directory. | Key retention and backup leakage. |
| **Backblaze B2 / Wasabi / Cloudflare R2** | Optional object storage providers | Store encrypted approved backups with least-privilege keys and measure restore and ongoing costs. | Remote data and account access. |
| **Podman** | Container tooling with rootless options | Execute an isolated synthetic build with disabled network and a read-only filesystem mapping. | Containers not strong universal sandbox. |
| **Syncthing** | Peer-to-peer file synchronization | Synchronize an explicitly selected test folder between authorized devices, checking conflict and deletion behavior. | Replication can spread mistakes. |
| **uv / Poetry / Conda** | Alternative Python environment managers | Create pinned isolated dependencies for a synthetic project and document exactly which package versions were installed. | Package supply chain and lockfiles. |
| **Forgejo / Gitea** | Self-hostable Git repository services | Preserve code and issues on owned infrastructure with role-based repo access and tested backups. | Server maintenance and access control. |
| **rclone** | File transfer and backup transport | Copy only approved encrypted archives to a named destination with logging and checksum verification. | Remote configuration secrets. |
| **Kopia** | Encrypted backup and snapshot program | Run synthetic restore drills and verify that incremental backups preserve necessary versions. | Destination and master-key recovery. |
| **Kubernetes / K3s** | Container orchestration choices | Deploy only after the project requires multiple services, with restrictive service accounts and network policy tests. | Cluster complexity and credentials. |
| **Docker** | Packaging and container runtime | Build a minimal test image with pinned bases and no production secrets, then scan it before running. | Root daemon and untrusted images. |

## Alternative build patterns (fictional examples, not actual stacks)

Each route below deliberately presents **several choices**. Choose none until requirements, rights, permissions, and test results are clear. The presence or ordering of tools does not imply use in any existing system.

| Imaginary development goal | Possible components to compare (choose independently) | Why and how | Stop/verification rule |
| --- | --- | --- | --- |
| Local-first beginner continuity | `SQLite FTS5 / DuckDB / PostgreSQL`; `Python scripts / JupyterLab / FastAPI` | Start with synthetic events and a deterministic status command; only add a web UI after backup/restore and restart tests. | No cloud, download, service or public listener required. |
| Offline encyclopedia assistant | `Kiwix / Gutenberg / local permitted Markdown`; `Haystack / LlamaIndex / plain SQLite FTS5` | Verify the exact source license and snapshot, then test retrieving cited passages without an AI model. | Source rights and reader tests must PASS; no bulk mirror by default. |
| Model comparison laboratory | `Mistral / Phi / Gemini / Llama / Claude / Qwen`; `Promptfoo / Inspect AI / pytest` | Freeze nonprivate questions and evaluate exact model/version, answer quality, token usage and real provider receipts. | Never mistake a wrapper label or simulated reviewer for an independent model response. |
| Coding study and patch review | `Continue / Aider / Cline / Copilot / CodeQL / VS Code / Zed` | Use disposable code, inspect diffs, run deterministic tests and leave merges under human control. | No direct production repo writes or uncontrolled terminal commands. |
| Accessibility and dictation | `Piper / Deepgram / Whisper / AssemblyAI / Vosk` | Process synthesized/consented audio; compare transcript quality and chosen local-versus-cloud route. | Voice consent, retention, licensing and deletion policy. |
| Data-intensive local research | `DuckDB / LanceDB / Qdrant / Neo4j / Postgres`; `Crossref / OpenAlex / PubMed` | Tie every claim to source records, dates and citation IDs, testing for invented relationships. | No patient records, scraping bypass or unlicensed full-text ingest. |
| Browser test harness | `Selenium / Playwright / Browser automation libraries`; `OWASP ZAP / pytest` | Test an owned dummy site with fake accounts and a clean browser profile. | Never automate other people's accounts or bypass security challenges. |
| Multi-actor workflow research | `Temporal / LangGraph / Dagster / CrewAI / Prefect` | Simulate pause, crash, owner takeover, retry and human approval using nonsecret task packets. | A model role cannot inherit approval or silently make external changes. |
| Native desktop assistant | `Tauri / PySide / Electron / Flutter`; `LM Studio / llama.cpp / Jan` | Prototype a read-only dashboard and test file, model and local-network boundaries with network disabled. | No launch at login or system-wide file access without consent. |
| Public educational demo | `Netlify / GitHub Pages / Cloudflare Pages / Vercel`; `React / SvelteKit / HTML` | Publish only original text and fake-data examples with a clear copyright and privacy note. | Check build logs, commit email and trackers before publication. |
| Regulated or sensitive research | `CodeQL / SOPS / OPA / Syft / Gitleaks`; `local text-only processing` | First classify records and rights; run static scans, data-minimization and human-reviewed source checks. | Do not put private records into public repos, model prompts or telemetry. |
| Reproducible model research | `PyTorch / JAX / PEFT / Transformers / MLflow` | Train on generated or permission-cleared material, record exact checkpoint, dataset rights and evaluation. | Never assume downloadable models allow commercial fine-tuning or redistribution. |

## A useful admission record for any chosen option

Keep the same fields regardless of product name:

```yaml
option_id: candidate-001
display_name: CHOOSE_FROM_CATALOG
reason_for_consideration: SPECIFIC_USER_GOAL
source_or_maintainer: OFFICIAL_SOURCE_UNVERIFIED
version_or_model_id: UNVERIFIED
license_and_terms: UNVERIFIED
rights_to_distribute: NOT_AUTHORIZED
rights_to_train_on_content: NOT_AUTHORIZED
privacy_classification: SYNTHETIC_ONLY
data_leaves_device: UNKNOWN
required_network_destinations: UNKNOWN
required_file_and_account_permissions: NONE_APPROVED
incremental_cost_and_budget: ZERO_UNTIL_APPROVED
hardware_requirements: UNKNOWN
installation_status: NOT_ASSESSED
connection_status: NOT_CONNECTED_BY_THIS_CATALOG
test_fixture: GENERATED_FAKE_DATA
test_command_and_receipt: NOT_RUN
independent_security_review: NOT_DONE
owner_approval_for_specific_action: NOT_GRANTED
fallback_and_stop_control: REQUIRED_BEFORE_ACTIVATION
```

Use the same structure for a model, dataset, knowledge archive, application, browser plugin, GPU host or developer tool. **No catalog row is automatically entitled to user accounts, confidential documents, API keys or protected operations.**

## Privacy and legal guardrails

1. **Never infer what an organization uses from this catalog.** Do not add real model counts, machine names, account details, credential sources, internal infrastructure, private Git URLs, or operational statuses to this public directory.
2. **Software license, model-weight license, dataset license, online-service contract and media rights are different.** Reading, citation, indexing, embedding, training, commercial sale and redistribution may each need distinct rights. Unknown means do not perform that use.
3. **Model/provider connectors are trust boundaries.** External content is data, not instructions. Require consent before browser/device access, account login, purchase, sending messages, deployment, repo changes or destructive actions.
4. **AI security threats include prompt injection, untrusted tool definitions, sensitive information disclosure, excessive agency, model/data poisoning and supply-chain compromise.** Review the official [OWASP GenAI Security Project](https://genai.owasp.org/); scan dependencies and restrict tokens before execution.
5. **User-side privacy matters:** never request account addresses, unique IDs, private transcripts, personal screenshots, medical/education/financial details or actual projects to prove a build succeeded. Synthetic traces suffice.
6. **Cloud and local claims are conditional:** hosted services require data/retention review; local apps may still download packages, synchronize or expose HTTP endpoints. Explicitly test network-disabled behavior before claiming true offline use.
7. **No products are installed by reading this list.** Every option requires its own official version and terms verification at the time it is considered. In a market with frequent rebrands and deprecations, names/links are informative, not a guarantee of current availability.
8. **No implied partnership, endorsement, certification or legal opinion.** Brand names are descriptive third-party references. This resource is not security advice for a real production deployment or a legal clearance certificate.

## Official documentation references for spot-checking

- [NVIDIA: Local inference backend comparisons](https://developer.nvidia.com/ai-apps-for-rtx-pcs/inference-backends)
- [LM Studio: local models and endpoint documentation](https://lmstudio.ai/docs/app)
- [Microsoft Agent Framework](https://learn.microsoft.com/en-us/agent-framework/)
- [Google Gemini model and API documentation](https://ai.google.dev/gemini-api/docs/models)
- [Amazon Bedrock supported model families](https://docs.aws.amazon.com/bedrock/latest/userguide/model-cards.html)
- [OpenSSF Scorecard supplier-risk heuristics](https://github.com/ossf/scorecard)
- [OWASP GenAI Security Project](https://genai.owasp.org/)
- [Wikimedia Terms of Use](https://foundation.wikimedia.org/wiki/Terms_of_Use)
- [iFixit licensing](https://www.ifixit.com/Info/Licensing)
- [PhET licensing](https://phet.colorado.edu/en/licensing)
- [OpenStreetMap copyright](https://www.openstreetmap.org/copyright)
- [Project Gutenberg license](https://www.gutenberg.org/policy/license)

These links illustrate how to verify official source claims, **not** an assertion that any provider or tool has been chosen. Licensing, API pricing, model cards, geographic availability and privacy policies may change.

---

*Free community research atlas. A wide menu of possibilities—not a list of installed, employed, authorized or connected systems. Keep private project architecture private. The mission outlives the model.*
