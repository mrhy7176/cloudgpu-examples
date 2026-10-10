# Claude on cloudgpu.app

**Claude Code at half the official Claude API price.** Claude Opus, Sonnet and Fable, billed per token from one prepaid balance.

> **Claude models are currently available through Claude Code only** (the official Claude Code CLI and its IDE extensions). Calling `claude-*` models from anything else, including Cursor, Cline, Continue, OpenClaw, the OpenAI or Anthropic SDKs, curl and LangChain, is not supported right now and will fail. Every other model on the gateway (DeepSeek, GLM, Kimi, MiniMax, Qwen, gpt-oss, FLUX, Whisper and more) works in any OpenAI-compatible client through `https://cloudgpu.app/v1`; see the [top-level README](../README.md).

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

## Account setup

1. Sign up at https://cloudgpu.app (email or Google).
2. Top up at https://cloudgpu.app/billing: Alipay, Google Pay, Apple Pay, Visa or Mastercard from $5 in one checkout, or USDT (TRC-20). A first top-up of $10 or more gets a $5 bonus. Balance is prepaid and does not expire.
3. Create a key in the API console at https://cloudgpu.app/api/console and use it as `ANTHROPIC_AUTH_TOKEN`.

## Tools

| Tool | Guide | Claude models | Other models |
|---|---|---|---|
| Claude Code (CLI and IDE extensions) | [`tools/claude-code.md`](tools/claude-code.md) | **Yes** | — |
| Cursor | [`tools/cursor.md`](tools/cursor.md) | No | Yes (OpenAI-compatible) |
| Cline | [`tools/cline.md`](tools/cline.md) | No | Yes (OpenAI-compatible) |
| Continue | [`tools/continue.md`](tools/continue.md) | No | Yes (OpenAI-compatible) |
| OpenClaw | [`tools/openclaw.md`](tools/openclaw.md) | No | Yes (OpenAI-compatible) |

## Which model

Start with `claude-sonnet-5-5` ($1.00 / $5.00). Move a task to `claude-opus-5-5` ($2.00 / $10.00) only when Sonnet's answer is not good enough; the 2x gap is the biggest lever on the bill. `claude-fable-5-1` is the most expensive line here.

## What to know before you rely on it

- This is an independent gateway, not a first-party Claude account. It runs in Hong Kong and has no automatic failover. We do not promise an SLA.
- Prompt and completion bodies are not stored; token counts are kept for billing.
- Make a small first top-up, run your real workload for a day, then decide.
