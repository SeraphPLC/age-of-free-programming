# Recommended computer setup: ChatGPT + Desktop Commander (optional)

**Free community educational guide · October 2026 · No private Seraph account or installation required**

**Want an AI to create and test real Python files on your computer instead of asking you to copy/paste code?** A supported AI client plus a user-authorized computer tool can do that. One documented option is **ChatGPT + Remote Desktop Commander**.

This is an **optional third-party service**, not supplied by Seraph, not an official partnership, not a verified sandbox, and NOT access to private Seraph Core or Mesh. You may instead start with the [chat-only continuity prompt](../prompts/stages/00_CHAT_ONLY_CONTINUITY.md), use a local MCP-compatible desktop assistant, or follow [Stage 1](../prompts/stages/01_OFFLINE_CORE.md) manually. Reading or copying this project's educational prompts never requires installing Desktop Commander.

**Read the security warning before connecting a computer.** Once authorized, the AI can run real tools with the permissions of the operating-system account running the agent. This is different from simply pasting a prompt.

## Choose the approach that fits your comfort level

| Your situation | Start here | What happens |
| --- | --- | --- |
| Chat only; no file or terminal access | [Stage 0](../prompts/stages/00_CHAT_ONLY_CONTINUITY.md) | Manual, privacy-reduced mission and handoff card; no installed software |
| ChatGPT with eligible plugin access and a safely isolated test computer | **This guide** and [Stage 1](../prompts/stages/01_OFFLINE_CORE.md) | AI can create files and run tests on your authorized computer |
| Local desktop assistant with MCP support | [Free local Desktop Commander MCP](https://desktopcommander.app/mcp/) | No hosted remote relay; still grants powerful local file/terminal access |
| Already have a qualified coding agent | [Staged build path](STAGED_BUILD_PATH.md) | No Desktop Commander required |

## Requirements, pricing, and who receives your data

As advertised on the [official Desktop Commander pricing page](https://desktopcommander.app/pricing/) when this guide was prepared:

- **Remote Free:** $0/month; currently 10,000 tool calls per month.
- **Remote Pro:** $20/month; the advertised plan offers unlimited tool calls.
- **Local MCP:** free and open source, with no separate hosted remote subscription or monthly call ceiling. Requires a compatible desktop client.
- **Your AI client:** ChatGPT, Claude and other providers may require their own account, plan, usage allowance or connector permission. The Remote Free plan does **not** pay for an AI subscription or API usage.
- **Remote device:** Node.js **18 or newer** for the device-agent command, Python **3** for the offline AI OS exercise, and a supported computer running macOS, Windows or Linux.
- **Remote account:** the hosted route requires **your own Desktop Commander account** and device pairing. You never register an account with the publisher of this Seraph educational repository.

Pricing, connector eligibility and terms can change: check the [current price page](https://desktopcommander.app/pricing/) and [official setup guide](https://github.com/desktop-commander/remote-desktop-commander/blob/main/docs/SETUP.md). The local MCP implementation is open source; **the hosted remote relay is a proprietary service**, with a different third-party privacy and trust boundary.

Your connected AI may request local file contents or command outputs and send those through the remote relay and the AI provider. The [provider security policy](https://github.com/desktop-commander/remote-desktop-commander/blob/main/SECURITY.md) describes encrypted transport, transient relayed tool data and operational telemetry. The [ChatGPT plugin listing](https://chatgpt.com/plugins/remote-desktop-commander) also warns that relevant chats and memories may be shared with the connected app; use a fresh, minimal-context project chat and review your ChatGPT data and app controls before connecting. Read the current terms and privacy policies for **both** services. This project has no reason to receive your personal, financial, account, student, medical or business records.

## Critical safety notice: configuration is not a sandbox

**Desktop Commander's directory allowlist and command blocklist are safeguards, not a hard security boundary.** The vendor explicitly warns that tools execute with your operating-system account permissions. The [local server documentation](https://github.com/wonderwhy-er/DesktopCommanderMCP) explains that terminal commands can access paths outside configured allowed directories, and command blocks may be bypassed by shells, scripts, interpreters and alternate execution routes.

**An allowed-project-folder setting is not a guarantee that the AI cannot access other files.** Neither are sentences such as "only work in my project folder." For meaningful containment use a **separate low-privilege OS account, throwaway VM or container with restricted mounts** that has no private files, browser sessions, credentials, bank records or other sensitive access. Keep backups. Never run the device agent as root/administrator for this exercise.

Protect the AI account and Desktop Commander account with multifactor authentication where offered. Pair **only a computer you control**, and stop the device agent when you are finished.

## Step-by-step remote setup

### Step 1 — Prepare a safe project environment

Use a separate test account or isolated virtual machine. Create a **new, empty** folder called **Seraph-Learning** there. Do not use an existing personal project and do not make your real documents, home directory, synced drives or credential store accessible to the test environment.

Write down its absolute path on your own computer (you do not need to publish it). Use fictional task data.

### Step 2 — Check Node.js and Python

On macOS or Linux, open Terminal:

~~~text
node --version
python3 --version
~~~

On Windows, open PowerShell or Command Prompt:

~~~text
node --version
py -3 --version
~~~

Node.js must be **v18 or newer**. If something is missing, follow the official Node.js or Python vendor installation instructions. Review any installer. Do not run an unexplained "curl | bash" download command from a chat.

### Step 3 — Pair the test device

1. Open the [official remote setup guide](https://github.com/desktop-commander/remote-desktop-commander/blob/main/docs/SETUP.md).
2. Visit [mcp.desktopcommander.app](https://mcp.desktopcommander.app/) and sign in to **your own** Desktop Commander account.
3. On your isolated machine, review and run the provider's documented command:

~~~text
npx @wonderwhy-er/desktop-commander@latest remote
~~~

The command downloads and executes third-party npm code. The version named "latest" can change; prefer a specifically reviewed version for repeatable long-term use.

4. The terminal shows a pairing code, and a browser verification page opens. **Approve only when the codes match exactly.**
5. Confirm your test machine appears in your dashboard, and leave its agent terminal running while you use it.

Never share OAuth tokens, pairing codes, cookies, device keys or browser storage with the Seraph publisher or in a public issue.

### Step 4 — Connect your AI client

In ChatGPT, connect the official [Remote Desktop Commander plugin](https://chatgpt.com/plugins/remote-desktop-commander) when available to your plan and workspace. Review requested permissions. Follow the authorization flow using the **same Desktop Commander account** as Step 3.

If your AI client instead supports a custom remote MCP connector, the provider's documented endpoint is:

~~~text
https://mcp.desktopcommander.app/mcp
~~~

See the [official supported-client instructions](https://github.com/desktop-commander/remote-desktop-commander). Some custom-connector workflows require a plan with developer settings. Do **not** bypass a workplace administrator or plan restriction if the plugin/connector is unavailable. Use chat-only, manual or compatible local MCP instead.

### Step 5 — Inspect and reduce scope before building

In a **separate configuration chat**, tell the connected AI:

> Use Desktop Commander to show the relevant current configuration **without listing my files or printing account data**. Do not change it yet. Explain which controls affect file operations and which do **not** restrict terminal access. Ask before each configuration change.

If your particular version exposes a configuration update tool, you may ask it to set an allowed-folder **guardrail**, substituting your own *absolute* Seraph-Learning directory:

~~~json
{"key":"allowedDirectories","value":["/absolute/path/to/Seraph-Learning"]}
~~~

Then read it back with the provider's config-read tool. An empty allowed-directory list can mean unrestricted access; **do not use an empty list**.

You may also request a **basic** blocked-command guardrail, such as:

~~~json
{"key":"blockedCommands","value":["rm","rmdir","del","Remove-Item","sudo","format"]}
~~~

This **does not** prevent destruction or reading of other files through Python, shells or other execution methods. For real containment, rely on a separate restricted operating-system environment; never treat this command list as an authorization system. If configuration cannot be read back, **do not enable write/execute access to a computer containing private data**.

### Step 6 — Verify the tools with a read-only check

Ask:

> Using Desktop Commander, identify only the isolated computer I paired. Check the Python version and list **only the empty Seraph-Learning folder**. Do not search my home directory, scan drives, touch browser profiles, access accounts, install anything or write a file. Show the actual tool response and command exit status, not a proposed command.

If the AI only **describes** commands rather than returning real tool output, it has not verified execution. Stop and review connector setup.

### Step 7 — Build Stage 1 with explicit permission

Open [Stage 1: the offline Python/SQLite core](../prompts/stages/01_OFFLINE_CORE.md). Paste its stage prompt along with this temporary scope instruction:

> Use my **isolated** Seraph-Learning folder only after I approve the exact path. Never change Desktop Commander settings in this build chat. First show a read-only implementation plan, then request permission before changing files or executing new command classes. Use synthetic data and Python standard-library modules only. No external network requests, cloud accounts, paid APIs, daemons, purchases, publishing, destructive operations or access to other folders. Run real init/status/doctor checks and tests. Record commands, exit codes, results and failures. Stop if the requested operation exceeds scope or a guardrail appears ineffective.

A legitimate Stage 1 completion means actual source files exist in the approved environment and actual test commands ran. A confident narrative is not evidence.

### Step 8 — Handoff, stop and revoke

1. Inspect the generated source and rerun tests in a **new process**.
2. Keep full databases, backups, personal paths and raw receipts **on your own device**. Never paste them into public GitHub issues or an online AI chat.
3. Save a **sanitized** handoff with MISSION, KNOWN, DONE, OPEN, AUTHORITY and NEXT. No old approval carries over to the next AI conversation.
4. Stop the device agent with **Ctrl+C** in its running terminal. The computer is then no longer reachable through that agent.
5. If needed, revoke that device in the [Desktop Commander dashboard](https://mcp.desktopcommander.app/) and disconnect its AI plugin.

The public prompt does **not** install a background worker or magically make work continue with all chats closed.

## What has and has not been validated

This connection can let an authorized AI **actually create files and run tests** on a user-owned computer, replacing the exhausting manual copy/paste loop. It does **not** prove that the AI OS builder prompt has been independently reproduced on every OS or model, that any file/terminal action is secure, or that cross-model continuity is flawless.

No private Seraph software, source, Mesh access, personal account information, AI subscriptions, API tokens, cloud credits or sensitive financial material is shared by this educational guide. The installed software and connected accounts, if any, are **yours and the third-party providers'**, not this project's.

**Official references:** [Remote setup](https://github.com/desktop-commander/remote-desktop-commander/blob/main/docs/SETUP.md) · [Remote security](https://github.com/desktop-commander/remote-desktop-commander/blob/main/SECURITY.md) · [Current pricing](https://desktopcommander.app/pricing/) · [Local open-source MCP](https://github.com/wonderwhy-er/DesktopCommanderMCP) · [ChatGPT plugin](https://chatgpt.com/plugins/remote-desktop-commander).

**The mission outlives the model. The machine, data and decision to connect it remain yours.**
