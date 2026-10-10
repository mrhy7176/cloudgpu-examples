# Claude Code with cloudgpu.app

Claude Code is how you use Claude models on cloudgpu.app. Point the official Claude Code CLI (or the Claude Code IDE extensions, which read the same settings) at our endpoint with your cloudgpu.app key, and every Claude model below is billed at half the official per-token price from your prepaid balance.

> **Claude models are currently available through Claude Code only.** Requests for `claude-*` models from any other client (Cursor, Cline, Continue, OpenClaw, the OpenAI or Anthropic SDKs, curl, LangChain, ...) are not supported and will fail. The other models on the gateway (DeepSeek, GLM, Kimi, MiniMax, gpt-oss, FLUX, Whisper and more) work in any OpenAI-compatible client; see [`cursor/README.md`](../../cursor/README.md).

## 1. Environment variables

```bash
export ANTHROPIC_BASE_URL=https://cloudgpu.app
export ANTHROPIC_AUTH_TOKEN=cgw-sk-...                 # your cloudgpu.app key
export ANTHROPIC_MODEL=claude-sonnet-5-5               # or claude-opus-5-5, claude-opus-4-7, ...
export ANTHROPIC_DEFAULT_HAIKU_MODEL=claude-sonnet-5-5
claude
```

- `ANTHROPIC_BASE_URL` is the bare host. Claude Code adds the API path itself; do not append `/v1`.
- `ANTHROPIC_AUTH_TOKEN` is your cloudgpu.app key (`cgw-sk-...`), created in the [API console](https://cloudgpu.app/api/console?utm_source=github).
- `ANTHROPIC_DEFAULT_HAIKU_MODEL` matters: Claude Code uses the Haiku slot for background tasks (titles, summaries, quick checks). There is no Haiku model on the gateway, so without this line those calls ask for a model the gateway does not serve and error. Mapping it to `claude-sonnet-5-5` makes them work; they are billed at Sonnet prices.

Optional, if you switch models with `/model` and want the `opus` / `sonnet` aliases to resolve to IDs the gateway serves:

```bash
export ANTHROPIC_DEFAULT_OPUS_MODEL=claude-opus-5-5
export ANTHROPIC_DEFAULT_SONNET_MODEL=claude-sonnet-5-5
```

## 2. Or put it in `~/.claude/settings.json`

So it applies to every session, including the IDE extensions, without touching your shell profile:

```json
{
  "env": {
    "ANTHROPIC_BASE_URL": "https://cloudgpu.app",
    "ANTHROPIC_AUTH_TOKEN": "cgw-sk-...",
    "ANTHROPIC_MODEL": "claude-sonnet-5-5",
    "ANTHROPIC_DEFAULT_HAIKU_MODEL": "claude-sonnet-5-5"
  }
}
```

Use `claude-opus-5-5` as `ANTHROPIC_MODEL` if you want Opus by default. A project-level `.claude/settings.json` works the same way, but do not commit a file that contains your key.

## 3. Check it

```bash
claude -p "Reply with the single word: ok"
```

Then check that the request shows up in usage on https://cloudgpu.app/api/console.

## Models you can set

`ANTHROPIC_MODEL` (and `/model`) accepts any of these IDs:

| Model | Input / output, USD per 1M tokens (ours / official) |
|---|---|
| `claude-opus-5-5` | **$2.00** / $4.00 · **$10.00** / $20.00 |
| `claude-opus-5`, `claude-opus-4-8`, `claude-opus-4-7`, `claude-opus-4-6` | **$2.50** / $5.00 · **$12.50** / $25.00 |
| `claude-sonnet-5-5`, `claude-sonnet-5` | **$1.00** / $2.00 · **$5.00** / $10.00 |
| `claude-sonnet-4-6` | **$1.50** / $3.00 · **$7.50** / $15.00 |
| `claude-fable-5-1`, `claude-fable-5` | **$5.00** / $10.00 · **$25.00** / $50.00 |

Prices as of 8 October 2026; the live table at https://cloudgpu.app/api wins if it disagrees. Start on `claude-sonnet-5-5` and switch to `claude-opus-5-5` for the hard tasks; agentic sessions re-send a lot of context, so input tokens dominate the bill.

## Troubleshooting

- **401 / auth errors**: the key must be a cloudgpu.app key (`cgw-sk-...`). If you were previously signed in to Claude Code with another account, sign out with `/logout` and start again so the environment variables are used.
- **404**: `ANTHROPIC_BASE_URL` must be `https://cloudgpu.app`, not `https://cloudgpu.app/v1`.
- **Model errors on background tasks**: `ANTHROPIC_DEFAULT_HAIKU_MODEL` is not set, so Claude Code is asking for a Haiku model.
- **It works in Claude Code but not in my script / editor plugin**: expected. Claude models are currently available through Claude Code only. For other clients, use one of the non-Claude models on `https://cloudgpu.app/v1`.
