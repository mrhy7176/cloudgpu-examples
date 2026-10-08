<!-- REQUIRES /v1/messages — do not publish until live -->

# Claude Code with cloudgpu.app

Claude Code speaks the Claude Messages API format (`POST /v1/messages`), so it needs the gateway's Messages endpoint, not the OpenAI-compatible one.

## 1. Environment variables

```bash
export ANTHROPIC_BASE_URL=https://cloudgpu.app
export ANTHROPIC_AUTH_TOKEN=cgw-sk-...
export ANTHROPIC_MODEL=claude-sonnet-5-5          # or claude-opus-5-5
export ANTHROPIC_DEFAULT_HAIKU_MODEL=claude-sonnet-5-5
claude
```

- `ANTHROPIC_BASE_URL` is the bare host. Claude Code appends `/v1/messages` itself; do not add `/v1`.
- `ANTHROPIC_AUTH_TOKEN` is sent as `Authorization: Bearer cgw-sk-...`.
- `ANTHROPIC_DEFAULT_HAIKU_MODEL` matters: Claude Code uses the Haiku slot for background tasks (titles, summaries, quick checks). There is no Haiku model on the gateway, so without this line those calls ask for a model the gateway does not serve and error. Mapping it to `claude-sonnet-5-5` makes them work; they are billed at Sonnet prices.

Optional, if you switch models with `/model` and want the `opus` / `sonnet` aliases to resolve to IDs the gateway serves:

```bash
export ANTHROPIC_DEFAULT_OPUS_MODEL=claude-opus-5-5
export ANTHROPIC_DEFAULT_SONNET_MODEL=claude-sonnet-5-5
```

## 2. Or put it in `~/.claude/settings.json`

So it applies to every session without touching your shell profile:

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

## Troubleshooting

- **401 / auth errors**: the key must be a cloudgpu.app key (`cgw-sk-...`). If you were previously signed in to Claude Code with another account, sign out with `/logout` and start again so the environment variables are used.
- **404**: `ANTHROPIC_BASE_URL` must be `https://cloudgpu.app`, not `https://cloudgpu.app/v1`.
- **Model errors on background tasks**: `ANTHROPIC_DEFAULT_HAIKU_MODEL` is not set, so Claude Code is asking for a Haiku model.

## Cost

Per million tokens, 8 October 2026: `claude-sonnet-5-5` $1.00 in / $5.00 out, `claude-opus-5-5` $2.00 / $10.00 (half the official price). Agentic sessions re-send a lot of context, so input tokens dominate. Live prices: https://cloudgpu.app/api.
