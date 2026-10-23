# Claude on cloudgpu.app

Claude Opus, Sonnet and Fable through `https://cloudgpu.app/v1`, at 50% of the official per-token price, on one prepaid balance.

Claude models work with any client:

- **OpenAI-compatible** `POST https://cloudgpu.app/v1/chat/completions` for the OpenAI SDKs, Cursor, Cline, Continue, OpenClaw, LangChain and curl (examples: [`python/`](python/), [`node/`](node/), [`curl/`](curl/), tool guides in [`tools/`](tools/)).
- **Claude Messages API** `POST https://cloudgpu.app/v1/messages` for Claude Code and the `anthropic` SDK (examples: [`messages-api/`](messages-api/)).

## Set up Claude Code

```bash
export ANTHROPIC_BASE_URL=https://cloudgpu.app
export ANTHROPIC_AUTH_TOKEN=cgw-sk-...                 # your cloudgpu.app key
export ANTHROPIC_MODEL=claude-sonnet-5-5               # or claude-opus-5-5, claude-opus-4-7, ...
export ANTHROPIC_DEFAULT_HAIKU_MODEL=claude-sonnet-5-5 # no Haiku on the gateway
claude
```

Full guide, including `~/.claude/settings.json`, model aliases and troubleshooting: [`tools/claude-code.md`](tools/claude-code.md).

## Prices (8 October 2026)

USD per 1M tokens. "Ours" is what you are billed; "official" is the published list price for the same model. Every row is exactly half.

| Model | Input (ours / official) | Output (ours / official) |
|---|---|---|
| `claude-opus-5-5` | **$2.00** / $4.00 | **$10.00** / $20.00 |
| `claude-opus-5` | **$2.50** / $5.00 | **$12.50** / $25.00 |
| `claude-opus-4-8` | **$2.50** / $5.00 | **$12.50** / $25.00 |
| `claude-opus-4-7` | **$2.50** / $5.00 | **$12.50** / $25.00 |
| `claude-opus-4-6` | **$2.50** / $5.00 | **$12.50** / $25.00 |
| `claude-sonnet-5-5` | **$1.00** / $2.00 | **$5.00** / $10.00 |
| `claude-sonnet-5` | **$1.00** / $2.00 | **$5.00** / $10.00 |
| `claude-sonnet-4-6` | **$1.50** / $3.00 | **$7.50** / $15.00 |
| `claude-fable-5-1` | **$5.00** / $10.00 | **$25.00** / $50.00 |
| `claude-fable-5` | **$5.00** / $10.00 | **$25.00** / $50.00 |

There is no Haiku model on the gateway. Prices can change; the live table is at https://cloudgpu.app/api and wins if it disagrees with this file.

## Setup

1. Sign up at https://cloudgpu.app (email or Google).
2. Top up at https://cloudgpu.app/billing: Alipay, Google Pay, Apple Pay, Visa or Mastercard from $5 in one checkout, or USDT (TRC-20). Balance is prepaid and does not expire.
3. Create a key in the API console at https://cloudgpu.app/api/console and export it:

```bash
export CLOUDGPU_API_KEY=cgw-sk-...
```

## Examples

### OpenAI-compatible (works today)

| File | What it shows |
|---|---|
| [`python/chat.py`](python/chat.py) | `openai` Python SDK with `base_url="https://cloudgpu.app/v1"`, streaming |
| [`node/chat.mjs`](node/chat.mjs) | `openai` Node SDK with `baseURL: "https://cloudgpu.app/v1"`, streaming |
| [`curl/chat.sh`](curl/chat.sh) | Raw `POST /v1/chat/completions` |

### Claude Messages API format (`/v1/messages`)

| File | What it shows |
|---|---|
| [`messages-api/messages.sh`](messages-api/messages.sh) | Raw `POST /v1/messages` with `x-api-key` and `anthropic-version: 2023-06-01` |
| [`messages-api/messages.py`](messages-api/messages.py) | `anthropic` Python SDK with `base_url="https://cloudgpu.app"` (no `/v1`; the SDK adds it) |

## Tools

| Tool | Guide | Status |
|---|---|---|
| Cursor | [`tools/cursor.md`](tools/cursor.md) | Works today (OpenAI-compatible) |
| Cline | [`tools/cline.md`](tools/cline.md) | Works today (OpenAI-compatible) |
| Continue | [`tools/continue.md`](tools/continue.md) | Works today (OpenAI-compatible) |
| OpenClaw | [`tools/openclaw.md`](tools/openclaw.md) | Works today (OpenAI-compatible) |
| Claude Code | [`tools/claude-code.md`](tools/claude-code.md) | Works today (`/v1/messages`) |

## Which model

Start with `claude-sonnet-5-5` ($1.00 / $5.00). Move a task to `claude-opus-5-5` ($2.00 / $10.00) only when Sonnet's answer is not good enough; the 2x gap is the biggest lever on the bill. `claude-fable-5-1` is the most expensive line here.

## What to know before you rely on it

- This is a gateway, not a first-party Claude account. It runs in Hong Kong and forwards each request to an upstream. There is no automatic failover, so an upstream outage is an outage here. We do not promise an SLA.
- Prompt and completion bodies are not stored; token counts are kept for billing.
- Make a small first top-up, run your real workload for a day, then decide.
