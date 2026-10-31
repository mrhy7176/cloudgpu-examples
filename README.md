# cloudgpu-examples

Code examples for [cloudgpu.app](https://cloudgpu.app/?utm_source=github): GPU rental billed by the minute and an OpenAI-compatible AI API gateway, on one prepaid balance, for developers outside mainland China.

Everything here runs against the public endpoint `https://cloudgpu.app/v1`. It is OpenAI-compatible, so the official OpenAI SDKs work unchanged: set `base_url` and use a CloudGPU API key.

## Let your AI coding assistant rent the GPU

[cloudgpu-mcp](https://github.com/mrhy7176/cloudgpu-mcp) is an MCP server for Cursor, Cline, opencode, Claude Code, VS Code and other MCP clients. Ask the assistant to fine-tune or run something on a GPU, and it quotes the price, rents a GPU once you agree, runs the job, downloads the results and shuts the GPU down. CloudGPU's servers enforce a budget and time limit on every instance it rents.

```bash
claude mcp add cloudgpu --env CLOUDGPU_API_KEY=cgw-sk-... -- npx -y cloudgpu-mcp
```

Setup for every client: https://cloudgpu.app/docs/mcp

## Claude at half the official price

Claude Opus, Sonnet and Fable are on the same endpoint, at 50% of the official per-token price. Full examples and tool guides: [`claude/`](claude/README.md).

No Haiku model. Current per-token prices for every model: https://cloudgpu.app/pricing.

```python
from openai import OpenAI

client = OpenAI(base_url="https://cloudgpu.app/v1", api_key="cgw-sk-...")
resp = client.chat.completions.create(
    model="claude-sonnet-5-5",
    messages=[{"role": "user", "content": "Write a unit test for this function."}],
)
print(resp.choices[0].message.content)
```

Works in Cursor, Cline, Continue and OpenClaw through the OpenAI-compatible endpoint, and in Claude Code and the `anthropic` SDKs through the native `/v1/messages` endpoint ([setup guides](claude/README.md#tools)).

| Example | What it shows |
|---|---|
| [`python/chat.py`](python/chat.py) | Chat completion with the `openai` package, streaming on |
| [`python/image_flux.py`](python/image_flux.py) | Image generation with FLUX.1 through `/v1/images/generations` |
| [`python/transcribe.py`](python/transcribe.py) | Speech to text with Whisper through `/v1/audio/transcriptions` |
| [`node/chat.mjs`](node/chat.mjs) | Same chat call from Node.js with the `openai` package |
| [`curl/chat.sh`](curl/chat.sh) | The raw HTTP request, nothing else |
| [`claude/`](claude/README.md) | Claude via the OpenAI SDK (Python, Node), cURL, and tool guides for Cursor, Cline, Continue, OpenClaw and Claude Code |
| [`curl/models.sh`](curl/models.sh) | List the models your key can call |
| [`cursor/README.md`](cursor/README.md) | Cursor, Cline and Continue settings |
| [`ollama-on-rented-gpu/README.md`](ollama-on-rented-gpu/README.md) | Calling Ollama or vLLM on a GPU you rented, via its public HTTPS endpoint |
| [`ai-sdk/`](ai-sdk/README.md) | Vercel AI SDK (`@ai-sdk/openai-compatible`): generateText and streamText |

## Setup

1. Create an account at https://cloudgpu.app/login (email or Google; no phone number or card needed to sign up).
2. Create an API key on the [API console](https://cloudgpu.app/api/console?utm_source=github).
3. Export it:

```bash
export CLOUDGPU_API_KEY=cgw-sk-...
```

## Models

Model IDs and current per-token prices are listed live at https://cloudgpu.app/api. As of 8 September 2026 the text models are `deepseek-v4-flash`, `deepseek-v4-pro`, `glm-5.3-flash`, `glm-5.2`, `glm-5.1`, `kimi-k3`, `kimi-k2.7-code`, `kimi-k2.6`, `kimi-k2.5`, `minimax-m3` and `gpt-oss-120b`; image models `flux-1-schnell` and `flux-1-dev`; speech `kokoro-tts` and `chatterbox-tts`; transcription `whisper-v3` and `whisper-v3-turbo`. `curl/models.sh` prints the live list.

## Notes

- Billing is prepaid. Top up at https://cloudgpu.app/billing with Alipay, Google Pay, Apple Pay, Visa or Mastercard from $5 in one checkout, or USDT (TRC-20). Unused balance does not expire.
- The gateway runs in Hong Kong and forwards each request to the infrastructure serving that model; there is no automatic failover. Prompt and completion bodies are not stored; token counts, model, latency and error codes are kept for billing.
- Issues and pull requests welcome. If an example stops working, open an issue and we will fix it the same day.

## License

MIT

Maintained with the Claude Code GitHub Action.
