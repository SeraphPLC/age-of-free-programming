# Frontier AI choices for your own continuity project

**Public educational guide | October 2026 | No private Seraph access**

This page explains **public, official ways** to use major AI services as part of an independent personal project. It is a companion to [Get Seraphed Community R1 (Living)](../prompts/GET_SERAPHED_COMMUNITY_R1_LIVING.md) and the [beginner computer setup guide](RECOMMENDED_COMPUTER_SETUP.md). It does not disclose or provide any private Seraph Mesh route, account, machine, paid entitlement, code, credential or proprietary implementation.

**These are options, not connections that are already active for you.** Do not install every AI or buy subscriptions just to begin. A single supported chat can maintain a sanitized handoff card; an authorized local coding tool can build the offline Stage 1 program.

For the **conceptual** reasons to coordinate multiple providers rather than treating them as one mind, see [Mesh anatomy, Chapter VIII](architecture/chapters/08-frontier-ai-ecosystem.md). This is not a claim that all advertised provider routes are active in one user's installation.

**How does the next AI actually get selected?** [Port → AI → next AI public routing maps](learning-routes/02_PORT_TO_AI_TO_AI_MAPS.md) and the [capability/fallback guide](learning-routes/03_PROVIDER_OPTIONS_AND_FALLBACKS.md) explain conditional provider choices, qualifications, source evidence, privacy and stop conditions. None of the named providers is assumed connected or automatically billed.

## Choose one of three methods

**Method A: Chat-only.** Use an AI's official website or app, copy the free community prompt, and manually save a sanitized project handoff. No computer tool or installed program is implied.

**Method B: Real local development.** Use the provider's approved coding CLI/IDE/desktop tool, or an authorized compatible MCP tool. Work within an isolated, newly created test environment using fictional records. Run actual Python tests and inspect their outputs.

**Method C: Developer API.** Use an official API under your own credentials, pricing, and approval. A consumer subscription or browser login does **not** automatically entitle you to free API calls or computer access.

## Public access matrix

| Provider or model family | Chat-only method | Real local coding or computer method | Developer or additional method |
| --- | --- | --- | --- |
| **ChatGPT / OpenAI** | [ChatGPT](https://chatgpt.com/) | Eligible ChatGPT [computer connector](RECOMMENDED_COMPUTER_SETUP.md); tool availability depends on plan | [OpenAI API](https://developers.openai.com/api/docs/quickstart), separately billed |
| **Claude / Anthropic** | [Claude](https://claude.ai/) | [Claude Code](https://support.claude.com/en/articles/14552382-your-first-day-in-claude-code), desktop tools or officially supported remote MCP | [Anthropic console](https://console.anthropic.com/), separate API terms |
| **Gemini / Google** | [Gemini](https://gemini.google.com/) | [Gemini CLI](https://github.com/google-gemini/gemini-cli/blob/main/docs/get-started/index.md), including an optional documented Desktop Commander extension | [Gemini API / AI Studio](https://ai.google.dev/gemini-api/docs/get-started) |
| **Perplexity** | [Perplexity](https://www.perplexity.ai/), Pro Search and Research if available | [Perplexity Computer](https://www.perplexity.ai/products/computer) can perform supported **cloud-side** workflows; do not assume local computer access | [Perplexity API platform](https://www.perplexity.ai/api-platform) |
| **GitHub Copilot** | [GitHub](https://github.com/features/copilot) code assistance and formal PR review | [Copilot CLI](https://docs.github.com/en/copilot/get-started/cli-quickstart), [VS Code or JetBrains](https://docs.github.com/en/copilot/concepts/copilot-surfaces/copilot-in-ides) | Supported IDE/MCP tools under plan and policy |
| **Microsoft Copilot** | [Copilot](https://copilot.com/) | Microsoft 365 tools or authorized organizational workflows, **not presumed local terminal access** | [Copilot Studio](https://learn.microsoft.com/en-us/microsoft-copilot-studio/agents-overview) |
| **Grok / xAI** | [Grok](https://grok.com/) official website/app | Manual handoff unless the actual client exposes an approved computer tool | [xAI API](https://docs.x.ai/developers/quickstart) with separate credits |
| **Kimi / Moonshot** | [Kimi](https://www.kimi.com/) | [Kimi Code](https://www.kimi.com/en/help/kimi-code/code-docs-index) desktop/CLI/VS Code | [Kimi API](https://www.kimi.com/en/help/kimi-api/api-overview) |
| **Qwen / Alibaba** | [Qwen](https://qwen.ai/) | [Qwen Code](https://qwenlm.github.io/qwen-code-docs/en/users/quickstart/) or a licensed local model | Alibaba/Qwen provider account and developer terms |
| **Ollama / local models** | Optional local chat interface | [Ollama](https://ollama.com/download) CLI with models supported by your hardware | Local API. An Ollama **cloud** model is not local-only |
| **JetBrains AI Assistant** | IDE assistant, **not an independent model family** | [JetBrains AI](https://www.jetbrains.com/ai/) or an eligible Copilot integration | Identify the selected underlying provider/model |

The latest model selector available **to your own account** is authoritative. Public provider model catalogs do not prove any specific model, subscription benefit or tool entitlement. Frontier model families may also be offered by an aggregator such as Perplexity or GitHub Copilot. Record the aggregator **and** named model where disclosed; one wrapper is not automatically an independent provider.

## Practical methods by service

**ChatGPT:** Start with the [free Community R1 prompt](../prompts/GET_SERAPHED_COMMUNITY_R1_LIVING.md). To build real files, use an authorized connected computer tool where supported by your plan. The separate [Desktop Commander guide](RECOMMENDED_COMPUTER_SETUP.md) gives a beginner path. Read [OpenAI's plugin guidance](https://help.openai.com/en/articles/20001256-plugins-in-chatgpt) before granting app permissions.

**Claude:** Use the Claude web/desktop app for the chat-only handoff, or follow the official [Claude Code setup](https://support.claude.com/en/articles/14552382-your-first-day-in-claude-code) to work in a new local project. Claude also documents [custom remote MCP connectors](https://support.claude.com/en/articles/11176164-use-connectors-to-extend-claude-s-capabilities). An API subscription and a chat subscription are different access routes.

**Gemini:** Use Gemini web for a manual continuity card. For direct project-file work, use [Gemini CLI](https://github.com/google-gemini/gemini-cli/blob/main/docs/get-started/index.md); check its current **Node.js 20+** requirement and your own login. Desktop Commander publishes a [supported Gemini CLI extension](https://github.com/desktop-commander/remote-desktop-commander). This does **not** imply ordinary Gemini web chat supports the same extension.

**Perplexity:** Use its own web/app Search, Pro or Research modes for sourced research. If you select a Claude, GPT, Gemini or Grok model inside Perplexity, the response still travels through **Perplexity**. Perplexity Computer can use provider-hosted work environments under eligible plans, but is not proof of access to local personal files. Its API is separate.

**GitHub Copilot:** Use an eligible IDE plugin or [Copilot CLI](https://docs.github.com/en/copilot/get-started/cli-quickstart) for a synthetic coding task; current CLI installation documentation lists **Node.js 22+** for npm. The [Desktop Commander vendor documentation](https://github.com/desktop-commander/remote-desktop-commander) includes VS Code/Copilot options. [Formal Copilot code review](https://docs.github.com/en/copilot/how-tos/copilot-on-github/use-copilot-agents/copilot-code-review) is different from asking a coding agent to modify files.

**Microsoft Copilot:** Use the official [personal or Microsoft 365 app](https://support.microsoft.com/en-us/microsoft-365-copilot/what-is-microsoft-copilot-app) as appropriate to your account. Work/school organizational policies and charges differ from consumer Copilot. For a beginner, copy a sanitized review packet and carry out actual coding through a separate authorized tool; do not claim consumer Copilot has an arbitrary terminal.

**Grok/xAI:** Use [Grok](https://grok.com/) to challenge a sanitized plan and return its response. Its developer API has a separate account and usage costs. A Grok option selected inside another AI service is not automatically equivalent to direct xAI execution.

**Kimi/Moonshot:** Use the Kimi website for analysis or [Kimi Code's official desktop/CLI/editor](https://www.kimi.com/en/help/kimi-code/code-docs-index) for actual software development. Verify app permissions on an isolated project. A Kimi model presented by GitHub Copilot is a Copilot-routed model, not a direct Moonshot API receipt.

**Qwen:** Use Qwen web as a chat option, [Qwen Code](https://qwenlm.github.io/qwen-code-docs/en/users/quickstart/) as a native coding route, or a legitimately licensed Qwen model in Ollama. Account requirements, billing and model capability differ.

**Ollama:** Install from [Ollama's official site](https://ollama.com/download), verify your actual local model list, and run only a model you have installed and approved. Local models can keep text off cloud inference services, but model downloads may require internet and cloud-hosted Ollama models are a separate data boundary. Not every local model meets an external frontier-review standard.

**JetBrains/other IDEs:** An IDE is an execution surface, not necessarily the AI provider. The underlying model, plugin, permissions and actual test results must be identified independently.

## Can every provider directly use Desktop Commander?

**No.** The [Desktop Commander supported-client instructions](https://github.com/desktop-commander/remote-desktop-commander) explicitly describe integrations for **ChatGPT (when eligible), Claude web/desktop/Code, Gemini CLI, and VS Code/GitHub Copilot**, as well as other compatible MCP clients. This does not establish direct access from every Perplexity, Microsoft Copilot, Grok, Kimi or ordinary Gemini browser conversation.

Its hosted remote service creates an additional third-party trust boundary. Do not assume folder allowlists or blocked-command settings create a secure operating-system sandbox. Use an isolated low-privilege user, virtual machine or carefully configured container and fictional data. [Read the full optional setup and safety guide](RECOMMENDED_COMPUTER_SETUP.md).

## A method that works with any AI: the sanitized handoff

The simplest cross-provider fallback is **manual and auditable**:

1. On your own computer, verify what source files and tests really exist.
2. Write a small **MISSION / KNOWN / DONE / OPEN / AUTHORITY / NEXT** card that omits personal, financial, account, medical or private project data.
3. Paste the card into the new AI's official chat and ask it to reconstruct the next safe task. Do not paste private credentials, raw logs, or a real project database.
4. Preserve its actual advice, limitations, model/route as exposed, date and dissent.
5. Execute changes only through your own authorized local tool. Rerun actual deterministic tests and save the receipts locally.
6. A new AI chat inherits **no previous permission** merely because a handoff exists.

**Multiple AI reviewers:** Give each the **same sanitized source revision** independently. A model that wrote a change should not accept its own review. Five names in one chat, two aliases for the same model, or an unanswered dispatch are not five independent verified reviewers. An optional external review is useful; it is not required for a beginner's first offline task tracker.

## Recommended starting order and privacy rules

**Start with one AI.** Use the community prompt or [Stage 0](../prompts/stages/00_CHAT_ONLY_CONTINUITY.md). For real programming, choose **one** supported coding tool and follow [Stage 1](../prompts/stages/01_OFFLINE_CORE.md) with synthetic data, restricted permissions and observed tests. Add other models only if a specific independent critique or capability is needed.

No Seraph publisher account, provider subscription, remote-computer tool or third-party API key is included by this repository. Model/vendor accounts, privacy policies, tool permissions, local machine resources and usage costs remain each user's responsibility.

**Never share private Seraph infrastructure, passwords, OAuth codes, financial/account records, bank information, medical/school files, real chat exports or unredacted logs.** No provider access listed on this page has been installed or qualified on every visitor's computer.

**The mission outlives the model. The user owns the project and chooses its AI.**
