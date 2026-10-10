# cloudgpu-examples

Code examples for [cloudgpu.app](https://cloudgpu.app/?utm_source=github): GPU rental billed by the minute and an OpenAI-compatible AI API gateway, on one prepaid balance, for developers outside mainland China.

The code examples here run against the public endpoint `https://cloudgpu.app/v1`. It is OpenAI-compatible, so the official OpenAI SDKs work unchanged: set `base_url` and use a CloudGPU API key. (Claude models are the exception: they are available through Claude Code only, see below.)

## Claude Code at half the official Claude API price

Claude Opus, Sonnet and Fable are billed at 50% of the official per-token price. **Claude models are currently available through Claude Code only** (the official Claude Code CLI and its IDE extensions); calling them from Cursor, Cline, Continue, the OpenAI or Anthropic SDKs, curl or any other client is not supported right now. Setup and tool guides: [`claude/`](claude/README.md).

```bash
export ANTHROPIC_BASE_URL=https://cloudgpu.app
export ANTHROPIC_AUTH_TOKEN=cgw-sk-...
export ANTHROPIC_MODEL=claude-sonnet-5-5               # or claude-opus-5-5, claude-opus-4-7, ...
export ANTHROPIC_DEFAULT_HAIKU_MODEL=claude-sonnet-5-5
claude
```

USD per 1M tokens, as of 8 October 2026 (ours / official list):

| Model | Input | Output |
|---|---|---|
| `claude-opus-5-5` | **$2.00** / $4.00 | **$10.00** / $20.00 |
| `claude-opus-5`, `claude-opus-4-8`, `claude-opus-4-7`, `claude-opus-4-6` | **$2.50** / $5.00 | **$12.50** / $25.00 |
| `claude-sonnet-5-5`, `claude-sonnet-5` | **$1.00** / $2.00 | **$5.00** / $10.00 |
| `claude-sonnet-4-6` | **$1.50** / $3.00 | **$7.50** / $15.00 |
| `claude-fable-5-1`, `claude-fable-5` | **$5.00** / $10.00 | **$25.00** / $50.00 |

No Haiku model. Live prices: https://cloudgpu.app/api.

## Every other model: one OpenAI-compatible endpoint

DeepSeek, GLM, Kimi, MiniMax, gpt-oss, FLUX, Whisper and the rest work everywhere through `https://cloudgpu.app/v1`, including Cursor, Cline, Continue, OpenClaw and any OpenAI SDK ([tool settings](cursor/README.md)). The examples below all use these models.

| Example | What it shows |
|---|---|
| [`python/chat.py`](python/chat.py) | Chat completion with the `openai` package, streaming on |
| [`python/image_flux.py`](python/image_flux.py) | Image generation with FLUX.1 through `/v1/images/generations` |
| [`python/transcribe.py`](python/transcribe.py) | Speech to text with Whisper through `/v1/audio/transcriptions` |
| [`node/chat.mjs`](node/chat.mjs) | Same chat call from Node.js with the `openai` package |
| [`curl/chat.sh`](curl/chat.sh) | The raw HTTP request, nothing else |
| [`claude/`](claude/README.md) | Claude in Claude Code (the only supported client for Claude models), plus Cursor, Cline, Continue and OpenClaw guides for the other models |
| [`curl/models.sh`](curl/models.sh) | List the models your key can call |
| [`cursor/README.md`](cursor/README.md) | Cursor, Cline and Continue settings (non-Claude models) |
| [`ollama-on-rented-gpu/README.md`](ollama-on-rented-gpu/README.md) | Calling Ollama or vLLM on a GPU you rented, via its public HTTPS endpoint |

## Setup

1. Create an account at https://cloudgpu.app/login (email or Google; no phone number or card needed to sign up).
2. Create an API key on the [API console](https://cloudgpu.app/api/console?utm_source=github).
3. Export it (for Claude Code, use it as `ANTHROPIC_AUTH_TOKEN` instead):

```bash
export CLOUDGPU_API_KEY=cgw-sk-...
```

## Models

Model IDs and current per-token prices are listed live at https://cloudgpu.app/api. As of 8 September 2026 the text models are `deepseek-v4-flash`, `deepseek-v4-pro`, `glm-5.3-flash`, `glm-5.2`, `glm-5.1`, `kimi-k3`, `kimi-k2.7-code`, `kimi-k2.6`, `kimi-k2.5`, `minimax-m3` and `gpt-oss-120b`; image models `flux-1-schnell` and `flux-1-dev`; speech `kokoro-tts` and `chatterbox-tts`; transcription `whisper-v3` and `whisper-v3-turbo`. Claude models are listed in the section above and are available through Claude Code only. `curl/models.sh` prints the live list.

## Notes

- Billing is prepaid. Top up at https://cloudgpu.app/billing with Alipay, Google Pay, Apple Pay, Visa or Mastercard from $5 in one checkout, or USDT (TRC-20). A first top-up of $10 or more gets a $5 bonus. Unused balance does not expire.
- The gateway runs in Hong Kong and forwards each request to the infrastructure serving that model; there is no automatic failover. Prompt and completion bodies are not stored; token counts, model, latency and error codes are kept for billing.
- Issues and pull requests welcome. If an example stops working, open an issue and we will fix it the same day.

## License

MIT
