# CloudGPU MCP server

Let your AI coding assistant rent a GPU on [CloudGPU](https://cloudgpu.app), run a job, bring the results back and shut the GPU down.

> "Fine-tune Qwen2.5-7B with LoRA on data/train.jsonl on a 4090 and put the adapter in ./outputs."

The assistant checks live prices and quotes you, rents the GPU once you say yes, uploads your code and data, starts training in the background, watches the logs, downloads the adapter and destroys the instance. You get the files and the final cost.

Works with any MCP client that can start a local server: **Cursor, Cline, opencode, Claude Code, VS Code, Windsurf, Continue, Claude Desktop**.

## Install

1. Create an API key at [cloudgpu.app/api](https://cloudgpu.app/api). The same key and balance also cover the OpenAI-compatible [model API](https://cloudgpu.app/api/docs).
2. Add the server to your client (Node.js 18+).

<details open>
<summary><b>Cursor / Windsurf / Cline / Claude Desktop</b></summary>

```json
{
  "mcpServers": {
    "cloudgpu": {
      "command": "npx",
      "args": ["-y", "https://cloudgpu.app/mcp/cloudgpu-mcp-0.1.0.tgz"],
      "env": { "CLOUDGPU_API_KEY": "cgw-sk-..." }
    }
  }
}
```
Cursor: `~/.cursor/mcp.json` · Cline: MCP Servers → Configure · Claude Desktop: `claude_desktop_config.json`
</details>

<details>
<summary><b>Claude Code</b></summary>

```bash
claude mcp add cloudgpu --env CLOUDGPU_API_KEY=cgw-sk-... -- npx -y https://cloudgpu.app/mcp/cloudgpu-mcp-0.1.0.tgz
```
</details>

<details>
<summary><b>opencode</b> (<code>opencode.json</code>)</summary>

```json
{
  "mcp": {
    "cloudgpu": {
      "type": "local",
      "command": ["npx", "-y", "https://cloudgpu.app/mcp/cloudgpu-mcp-0.1.0.tgz"],
      "environment": { "CLOUDGPU_API_KEY": "cgw-sk-..." }
    }
  }
}
```
</details>

<details>
<summary><b>VS Code</b> (<code>.vscode/mcp.json</code>)</summary>

```json
{
  "servers": {
    "cloudgpu": {
      "command": "npx",
      "args": ["-y", "https://cloudgpu.app/mcp/cloudgpu-mcp-0.1.0.tgz"],
      "env": { "CLOUDGPU_API_KEY": "cgw-sk-..." }
    }
  }
}
```
</details>

3. Optional but recommended: copy [`rules/cloudgpu.md`](rules/cloudgpu.md) into your project as `AGENTS.md`, `.cursor/rules/cloudgpu.md`, `.clinerules/cloudgpu.md` or `CLAUDE.md`. It tells the assistant to quote before renting, download before shutting down, and never leave a GPU running.

## Tools

| Tool | What it does |
|---|---|
| `get_account` | Balance, and how many instances the account may run at once |
| `list_gpus` | GPU models with VRAM, live price per GPU-hour and availability |
| `list_templates` | Ready-made images: JupyterLab, Ollama, ComfyUI, LLaMA-Factory, … |
| `estimate_cost` | Live quote for a GPU and a number of hours, plus your balance afterwards; returns a `quote_id` |
| `create_instance` | Rents from an approved quote, with a budget, a time limit and an idle limit |
| `get_status` / `list_instances` | Status, minutes run, cost so far, auto-shutdown limits |
| `run_command` | Runs a command on the instance; `background=true` for long jobs |
| `tail_logs` | Latest log lines, whether the job finished, GPU utilisation |
| `upload` / `download` | Files and folders between your computer and the instance (SFTP) |
| `stop_instance` | Destroys the instance and stops billing |
| `list_models` | Models on the OpenAI-compatible API, for inference without renting a GPU |

The server also provides the rules as a resource (`cloudgpu://rules`) and a `train_on_cloudgpu` prompt.

## Guardrails

- **A quote first.** `create_instance` only takes a `quote_id` from `estimate_cost` and `user_confirmed=true`.
- **Server-side limits.** Every instance is created with `max_spend_usd`, `max_hours` and an idle limit (60 minutes by default). CloudGPU's servers check them every minute and destroy the instance when one is hit, even if your client has disconnected or your laptop is asleep.
- **Your own ceiling.** `CLOUDGPU_MAX_SPEND_USD` (default 50) and `CLOUDGPU_MAX_HOURS` (default 24) cap what the assistant may set.
- **Results before shutdown.** After commands have run, `stop_instance` refuses until something has been downloaded, unless the user confirms `force=true`.
- **Secrets stay out of the chat.** The instance's SSH login is used inside this process and never returned to the model. Tool output is scrubbed of the API key and login details. Uploading `.ssh`, `.env`, key files or your whole home directory needs `allow_sensitive=true`.
- **The instance stays manageable.** Commands that change the root password, SSH configuration, firewall or the platform's monitoring agent are refused. CloudGPU shuts down instances that it can no longer monitor.
- **Read-only mode.** `CLOUDGPU_READ_ONLY=1` registers only the look-up tools.

## Configuration

| Env | Default | |
|---|---|---|
| `CLOUDGPU_API_KEY` | (required) | From https://cloudgpu.app/api |
| `CLOUDGPU_MAX_SPEND_USD` | `50` | Highest budget the assistant may set for one instance |
| `CLOUDGPU_MAX_HOURS` | `24` | Longest time limit the assistant may set |
| `CLOUDGPU_READ_ONLY` | off | `1` = look-up tools only |

## Without MCP

The server wraps the public REST API, which any agent or script can call with the same key:

```bash
curl https://cloudgpu.app/v1/gpu/offers -H "Authorization: Bearer $CLOUDGPU_API_KEY"

curl -X POST https://cloudgpu.app/v1/gpu/instances \
  -H "Authorization: Bearer $CLOUDGPU_API_KEY" -H "Content-Type: application/json" \
  -d '{"gpu_model":"RTX 4090","max_minutes":120,"max_spend_usd":2,"idle_minutes":30}'
```

Reference: [cloudgpu.app/api/docs](https://cloudgpu.app/api/docs#gpu) · OpenAPI: [cloudgpu.app/openapi.json](https://cloudgpu.app/openapi.json) · For LLMs: [cloudgpu.app/llms.txt](https://cloudgpu.app/llms.txt)

## Billing

Prepaid USD balance, GPUs billed per minute; top up at [cloudgpu.app/billing](https://cloudgpu.app/billing). When the balance runs out, running instances are destroyed and their disks erased, so keep enough balance for the job and download results as you go.

## License

MIT
