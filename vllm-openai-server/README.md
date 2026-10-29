# How do I serve a model like Qwen2.5 with vLLM on a rented GPU?

Rent a GPU with CUDA already installed, `pip`/`uv` install vLLM, run `vllm serve <model>`, and you get an OpenAI-compatible API at `http://localhost:8000/v1` on that machine, which you can reach from your laptop through an SSH tunnel ([vLLM Quickstart](https://docs.vllm.ai/en/latest/getting_started/quickstart/), read 2026-10-27).

Updated 2026-10-27

This folder walks through it on a CloudGPU **Raw GPU** instance with a small model,
[Qwen/Qwen2.5-1.5B-Instruct](https://huggingface.co/Qwen/Qwen2.5-1.5B-Instruct) (Apache-2.0 license, read on its model card and LICENSE file 2026-10-27). It is the model the vLLM Quickstart uses, so every command below matches the docs.

- **1.** Start a Raw GPU instance.
- **2.** Check the environment.
- **3.** Install vLLM and serve the model (official vLLM commands).
- **4.** Test it on the instance with curl.
- **5.** Reach it from your laptop over SSH.
- **6.** Back up your work and destroy the instance.

VRAM need depends on model, precision and workflow; see [How much VRAM do I need to run an LLM?](https://cloudgpu.app/guides/how-much-vram-do-i-need-to-run-an-llm) before you swap in a bigger model.

## 1. Start a Raw GPU instance

1. Go to [Deploy](https://cloudgpu.app/deploy?utm_source=github&utm_medium=referral&utm_campaign=202611_seg05_localllm&utm_content=gh_ex_vllm) and pick **Raw GPU**. Our deploy page describes it as "a raw GPU with JupyterLab + CUDA pre-installed. SSH access, root on a dedicated container, install any Python/CUDA libs you want."
2. Pick a card. We offer the RTX 5090 and the other cards listed on [/pricing](https://cloudgpu.app/pricing). The instance is billed per minute (see [/terms](https://cloudgpu.app/terms)).
3. Open the instance in your Dashboard and connect: SSH (`ssh -p <port> <user>@<host>`, with the host, port and user from your instance) or the JupyterLab terminal.

## 2. Check the environment first

Run these before installing anything, so you know which GPU, driver, CUDA toolkit and Python you have:

```bash
nvidia-smi
nvcc --version
python3 --version
```

According to the official vLLM docs ([GPU installation](https://docs.vllm.ai/en/latest/getting_started/installation/gpu/)), vLLM needs Linux, Python 3.11 – 3.14 and an NVIDIA GPU with compute capability 7.5 or higher; its pre-built wheels are compiled with CUDA 12.9 by default, and the docs recommend a fresh Python environment. Compare that with what the commands above print on your instance.

## 3. Install vLLM and serve the model

According to the official vLLM docs ([Quickstart](https://docs.vllm.ai/en/latest/getting_started/quickstart/), NVIDIA CUDA tab), create an environment with `uv` and install vLLM:

```bash
uv venv --python 3.12 --seed
source .venv/bin/activate
uv pip install vllm --torch-backend=auto
vllm download-kernels
```

- If `uv` isn't installed yet, the [uv docs](https://docs.astral.sh/uv/getting-started/installation/) list `pip install uv` as one install method (`python3 -m pip install uv`). Run `uv --version` first; if it's missing, install it that way.
- `--torch-backend=auto` lets `uv` pick the PyTorch build that matches the installed CUDA driver; the vLLM docs say `vllm download-kernels` installs precompiled kernels that vLLM would otherwise download and compile at startup.
- The vLLM docs also note that NVIDIA Blackwell GPUs need PyTorch wheels built for CUDA 12.8 or later. The RTX 5090 is a Blackwell card; we haven't checked the default install above on it, so if vLLM fails to start, check the installed PyTorch CUDA version first.

Then start the OpenAI-compatible server. The Quickstart command is:

```bash
vllm serve Qwen/Qwen2.5-1.5B-Instruct
```

By default it listens on `http://localhost:8000`; `--host` and `--port` change the address, and `--api-key` (or the `VLLM_API_KEY` environment variable) makes the server check for a key in the request header (vLLM Quickstart). To keep it bound to the instance only and protected by a key:

```bash
export VLLM_API_KEY="pick-a-long-random-string"
vllm serve Qwen/Qwen2.5-1.5B-Instruct --host 127.0.0.1 --port 8000
```

The first start downloads the model weights from Hugging Face.

## 4. Test it on the instance

In a second terminal on the instance (the requests from the vLLM Quickstart; add the header because the server now checks a key):

```bash
curl http://localhost:8000/v1/models \
  -H "Authorization: Bearer $VLLM_API_KEY"

curl http://localhost:8000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $VLLM_API_KEY" \
  -d '{
    "model": "Qwen/Qwen2.5-1.5B-Instruct",
    "messages": [
      {"role": "system", "content": "You are a helpful assistant."},
      {"role": "user", "content": "Who won the world series in 2020?"}
    ]
  }'
```

The answer is in `choices[0].message.content`, the standard OpenAI-compatible chat completion shape.

From Python, the official `openai` package works with `base_url="http://localhost:8000/v1"` (vLLM Quickstart):

```python
import os
from openai import OpenAI

client = OpenAI(api_key=os.environ["VLLM_API_KEY"], base_url="http://localhost:8000/v1")
resp = client.chat.completions.create(
    model="Qwen/Qwen2.5-1.5B-Instruct",
    messages=[{"role": "user", "content": "Tell me a joke."}],
)
print(resp.choices[0].message.content)
```

## 5. Reach it from your laptop (SSH port forward)

Keep the server bound to `127.0.0.1` on the instance and forward the port over SSH. On your laptop:

```bash
ssh -N -L 8000:127.0.0.1:8000 -p <port> <user>@<host>
```

Leave that running; on your laptop `http://localhost:8000/v1` now reaches the vLLM server, so the curl and Python examples above work unchanged (set `VLLM_API_KEY` locally to the same value). Any tool that accepts a custom OpenAI-compatible base URL can use it the same way.

Use the SSH user, host and port from your instance. We haven't checked port forwarding on a Raw GPU instance as written; if the tunnel won't open, run the curl tests on the instance instead.

## 6. When you're done

Back up your work, then destroy the instance from the Dashboard. Local instance data is deleted when the instance is destroyed, so copy off anything you want to keep first (scripts, configs, outputs; model weights can be downloaded again from Hugging Face). Billing stops when you destroy the instance (see [/terms](https://cloudgpu.app/terms)).

## FAQ

**How do I serve a model like Qwen2.5 with vLLM on a rented GPU?**
Start a GPU instance with CUDA installed (on CloudGPU: Deploy → Raw GPU), install vLLM with `uv pip install vllm --torch-backend=auto`, then run `vllm serve <hugging-face-model-id>`. The OpenAI-compatible API is at `http://localhost:8000/v1` on the instance.

**How do I call the vLLM server from my laptop?**
Forward the port over SSH (`ssh -N -L 8000:127.0.0.1:8000 -p <port> <user>@<host>`) and point your client at `http://localhost:8000/v1`. If you started vLLM with `--api-key` or `VLLM_API_KEY`, send it as `Authorization: Bearer <key>`.

**Which GPU should I rent for my model?**
VRAM need depends on model, precision and workflow. See [How much VRAM do I need to run an LLM?](https://cloudgpu.app/guides/how-much-vram-do-i-need-to-run-an-llm) and the cards on [/pricing](https://cloudgpu.app/pricing).

**How is the rented GPU billed?**
Billed per minute, rounded up, 1-minute minimum. Billing stops when you destroy the instance (see [/terms](https://cloudgpu.app/terms)).

## Sources (read 2026-10-27)

- Official vLLM docs: [Quickstart](https://docs.vllm.ai/en/latest/getting_started/quickstart/) (prerequisites, `uv` install commands, `vllm download-kernels`, `vllm serve`, default `localhost:8000`, `--host` / `--port` / `--api-key` / `VLLM_API_KEY`, curl and `openai` examples) and [GPU installation](https://docs.vllm.ai/en/latest/getting_started/installation/gpu/) (Linux, Python 3.11 – 3.14, compute capability 7.5+, CUDA 12.9 wheels, Blackwell note). vLLM is Apache-2.0; this folder only links to it.
- [uv installation docs](https://docs.astral.sh/uv/getting-started/installation/): `pip install uv`.
- [Qwen/Qwen2.5-1.5B-Instruct](https://huggingface.co/Qwen/Qwen2.5-1.5B-Instruct) model card and LICENSE: Apache License 2.0.
- CloudGPU [/deploy](https://cloudgpu.app/deploy) (Raw GPU description), [/docs](https://cloudgpu.app/docs), [/pricing](https://cloudgpu.app/pricing) (card list), [/terms](https://cloudgpu.app/terms) (billing, data deleted on destroy).
