# Using cloudgpu.app in Cursor, Cline and Continue

All three speak the OpenAI protocol, so you only change the base URL and the key.

> **Claude models are currently available through Claude Code only.** `claude-*` model IDs will not work in Cursor, Cline or Continue; for Claude, see [`claude/tools/claude-code.md`](../claude/tools/claude-code.md). Every other model on the gateway works here.

## Cursor

Settings → Models → **OpenAI API Key**: paste your CloudGPU key.
Turn on **Override OpenAI Base URL** and set it to:

```
https://cloudgpu.app/v1
```

Then add a custom model name, for example `deepseek-v4-flash` or `kimi-k2.7-code`, and select it. Cursor's own "Verify" button sends a test request; if it says the key is invalid, check that the base URL has `/v1` at the end. More detail: [`claude/tools/cursor.md`](../claude/tools/cursor.md).

## Cline (VS Code)

Provider: **OpenAI Compatible**
Base URL: `https://cloudgpu.app/v1`
API key: your CloudGPU key
Model ID: `deepseek-v4-flash` (or any non-Claude ID from https://cloudgpu.app/api)

## Continue

In `~/.continue/config.yaml`:

```yaml
models:
  - name: DeepSeek V4 Flash (CloudGPU)
    provider: openai
    model: deepseek-v4-flash
    apiBase: https://cloudgpu.app/v1
    apiKey: ${{ secrets.CLOUDGPU_API_KEY }}
```

## Which model for coding

`kimi-k2.7-code` is the coding-tuned model on the gateway and `deepseek-v4-pro` the larger general one; `deepseek-v4-flash` is several times cheaper and fine for autocomplete-style use. Try two on the same task before you decide; they are billed per token, so the comparison costs cents. Current prices per million tokens are on https://cloudgpu.app/api; off-peak DeepSeek pricing is passed through automatically.
