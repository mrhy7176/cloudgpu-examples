# Calling Ollama or vLLM on a GPU you rented

When you deploy the **Ollama**, **vLLM**, **SGLang** or **ComfyUI** template on cloudgpu.app, the API port of that template is published at a public HTTPS address of the form

```
https://<random-16-char-id>-i.cloudgpu.app
```

shown on your dashboard next to the instance. It is only reachable while the instance runs, and only that one port is exposed; SSH and JupyterLab stay on the supplier's own address.

## Ollama

Ollama serves an OpenAI-compatible API under `/v1`, so the same SDK code works with the rented GPU as the base URL and no key:

```python
from openai import OpenAI

client = OpenAI(base_url="https://<id>-i.cloudgpu.app/v1", api_key="ollama")
r = client.chat.completions.create(
    model="qwen3:32b",
    messages=[{"role": "user", "content": "hello"}],
)
print(r.choices[0].message.content)
```

Pull a model first, over SSH or through the API:

```bash
curl https://<id>-i.cloudgpu.app/api/pull -d '{"name": "qwen3:32b"}'
curl https://<id>-i.cloudgpu.app/api/tags
```

## vLLM

The vLLM template starts an OpenAI-compatible server on the published port. Same client code; the `model` field is the Hugging Face ID the template loaded (shown in the instance log).

## Things to know

- The tunnel is rate-capped per instance (a few MB/s). Fine for chat and embeddings; do not pull model weights through it, do that over SSH on the machine.
- Cold model load on first request adds roughly 60 to 90 seconds for a 32B model; after that, about a second per chat call from Europe or the US through Cloudflare.
- Billing is per minute. Stop the instance from the dashboard when you are done; the unused part of the pre-authorised hour is refunded.

Longer write-up: https://cloudgpu.app/blog/ollama-cloud-gpu-public-api-2026
