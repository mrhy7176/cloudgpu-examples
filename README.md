# cloudgpu-examples

Code examples for [cloudgpu.app](https://cloudgpu.app/?utm_source=github): GPU rental billed by the minute and an OpenAI-compatible AI API gateway, on one prepaid balance.

Everything here runs against the public endpoint `https://cloudgpu.app/v1`. It is OpenAI-compatible, so the official OpenAI SDKs work unchanged: set `base_url` and use a CloudGPU API key.

| Example | What it shows |
|---|---|
| [`python/chat.py`](python/chat.py) | Chat completion with the `openai` package, streaming on |
| [`python/image_flux.py`](python/image_flux.py) | Image generation with FLUX.1 through `/v1/images/generations` |
| [`python/transcribe.py`](python/transcribe.py) | Speech to text with Whisper through `/v1/audio/transcriptions` |
| [`node/chat.mjs`](node/chat.mjs) | Same chat call from Node.js with the `openai` package |
| [`curl/chat.sh`](curl/chat.sh) | The raw HTTP request, nothing else |
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

Model IDs are listed live at https://cloudgpu.app/api. As of 8 September 2026 the text models are `deepseek-v4-flash`, `deepseek-v4-pro`, `glm-5.3-flash`, `glm-5.2`, `glm-5.1`, `kimi-k3`, `kimi-k2.7-code`, `kimi-k2.6`, `kimi-k2.5` and `minimax-m3`; image models `flux-1-schnell` and `flux-1-dev`; speech `kokoro-tts` and `chatterbox-tts`; transcription `whisper-v3` and `whisper-v3-turbo`. `curl/models.sh` prints the live list.

## Notes

- Billing is prepaid. Top up at https://cloudgpu.app/billing with Alipay, Google Pay, Apple Pay, Visa or Mastercard, or USDT (TRC-20). Unused balance does not expire.
- The gateway forwards each request to the infrastructure serving that model; there is no automatic failover. Prompt and completion bodies are not stored; token counts, model and error codes are kept for billing.
- Issues and pull requests welcome. If an example stops working, open an issue and we will fix it the same day.

## License

MIT
