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

- Download model weight files over SSH on the machine. Use the public HTTPS address for chat, embeddings, and the API calls above.
- The first request loads the model onto the instance. Later chat calls use the model already loaded.
- Billing is per minute. Stop the instance from the dashboard when you are done.

Longer write-up: https://cloudgpu.app/blog/ollama-cloud-gpu-public-api-2026
