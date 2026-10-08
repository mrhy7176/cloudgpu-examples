# cloudgpu-examples

Code examples for [cloudgpu.app](https://cloudgpu.app/?utm_source=github): GPU rental billed by the minute and an OpenAI-compatible AI API gateway, on one prepaid balance, for developers outside mainland China.

Everything here runs against the public endpoint `https://cloudgpu.app/v1`. It is OpenAI-compatible, so the official OpenAI SDKs work unchanged: set `base_url` and use a CloudGPU API key.

## Claude at half the official price

Claude Opus, Sonnet and Fable are on the same endpoint, at 50% of the official per-token price. Full examples and tool guides: [`claude/`](claude/README.md).

USD per 1M tokens, as of 8 October 2026 (ours / official list):

| Model | Input | Output |
|---|---|---|
| `claude-opus-5-5` | **$2.00** / $4.00 | **$10.00** / $20.00 |
| `claude-opus-5`, `claude-opus-4-8`, `claude-opus-4-7`, `claude-opus-4-6` | **$2.50** / $5.00 | **$12.50** / $25.00 |
| `claude-sonnet-5-5`, `claude-sonnet-5` | **$1.00** / $2.00 | **$5.00** / $10.00 |
| `claude-sonnet-4-6` | **$1.50** / $3.00 | **$7.50** / $15.00 |
| `claude-fable-5-1`, `claude-fable-5` | **$5.00** / $10.00 | **$25.00** / $50.00 |

No Haiku model. Live prices: https://cloudgpu.app/api.

```python
from openai import OpenAI

client = OpenAI(base_url="https://cloudgpu.app/v1", api_key="cgw-sk-...")
resp = client.chat.completions.create(
    model="claude-sonnet-5-5",
    messages=[{"role": "user", "content": "Write a unit test for this function."}],
)
print(resp.choices[0].message.content)
```

Works today in Cursor, Cline, Continue and OpenClaw through the OpenAI-compatible endpoint ([setup guides](claude/README.md#tools)). Claude Code support needs the `/v1/messages` endpoint, which is not live yet.

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

- Billing is prepaid. Top up at https://cloudgpu.app/billing with Alipay, Google Pay, Apple Pay, Visa or Mastercard from $5 in one checkout, or USDT (TRC-20). A first top-up of $10 or more gets a $5 bonus. Unused balance does not expire.
- Requests are forwarded to each model's upstream (the DeepSeek, GLM, Kimi, MiniMax and FLUX models are served from the US; Claude models go through a separate upstream). The gateway itself runs in Hong Kong and has no automatic failover. Prompt and completion bodies are not stored; token counts, model, latency and error codes are kept for billing.
- Issues and pull requests welcome. If an example stops working, open an issue and we will fix it the same day.

## License

MIT
