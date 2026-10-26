# How do I connect Open WebUI to a remote Ollama server?

Set Open WebUI's `OLLAMA_BASE_URL` to the remote server's URL when you start it; Open WebUI then lists and chats with the models on that server instead of a local one ([Open WebUI README](https://github.com/open-webui/open-webui#readme), read 2026-10-27).

Updated 2026-10-27

This folder shows two ways to run it:

- **A. Everything on your own machine** (local Ollama + local Open WebUI).
- **B. Ollama on a rented GPU, Open WebUI on your laptop**, for models that don't fit your local VRAM.
  VRAM need depends on model, precision and workflow; see [How much VRAM do I need to run an LLM?](https://cloudgpu.app/guides/how-much-vram-do-i-need-to-run-an-llm).

## A. Local: Ollama + Open WebUI on one machine

1. Install Ollama (Linux, official script):

   ```bash
   curl -fsSL https://ollama.com/install.sh | sh
   ollama pull qwen2.5:0.5b
   ```

2. Start Open WebUI with Docker (official command from the Open WebUI README):

   ```bash
   docker run -d -p 3000:8080 --add-host=host.docker.internal:host-gateway \
     -v open-webui:/app/backend/data --name open-webui --restart always \
     ghcr.io/open-webui/open-webui:main
   ```

   Or without Docker (also from the README):

   ```bash
   pip install open-webui
   open-webui serve
   ```

3. Open `http://localhost:3000` (Docker) or the address `open-webui serve` prints.

## B. Remote: Ollama on CloudGPU, Open WebUI on your laptop

### B1. Start an Ollama instance

1. Go to [Deploy](https://cloudgpu.app/deploy?utm_source=github&utm_medium=referral&utm_campaign=202611_seg05_localllm&utm_content=gh_ex_owui), pick the **Ollama** template and a card (we offer the RTX 5090 and the other cards listed on [/pricing](https://cloudgpu.app/pricing)), and click Deploy. The instance is billed per minute (see [/terms](https://cloudgpu.app/terms)).
2. In your Dashboard, open the instance and click **API**. Your endpoint looks like
   `https://<random-id>-i.cloudgpu.app` (replace `<random-id>` with the id on your instance row).
3. Check it answers (the request from our [docs](https://cloudgpu.app/docs)):

   ```bash
   curl https://<random-id>-i.cloudgpu.app/api/chat \
     -H "Content-Type: application/json" \
     -d '{"model": "qwen2.5:0.5b", "messages": [{"role": "user", "content": "Hello"}], "stream": false, "keep_alive": "30m"}'
   ```

   `keep_alive` keeps the model loaded between requests; Ollama unloads idle models after 5 minutes by default.

### B2. Point Open WebUI at it

Use the README's "Ollama on a different server" form with your endpoint:

```bash
docker run -d -p 3000:8080 \
  -e OLLAMA_BASE_URL=https://<random-id>-i.cloudgpu.app \
  -v open-webui:/app/backend/data --name open-webui --restart always \
  ghcr.io/open-webui/open-webui:main
```

Without Docker: `OLLAMA_BASE_URL=https://<random-id>-i.cloudgpu.app open-webui serve`.

Open `http://localhost:3000`. Per the Open WebUI README, it then uses the Ollama server at that URL, so the models on the instance should show up in the model picker. We haven't run this exact pairing ourselves; if the list is empty, run the B1 curl check again.

### B3. Pull a bigger model

Our [docs](https://cloudgpu.app/docs) say the Ollama template supports any model in the Ollama library: use the **Pick Model** button on the instance to pull one. Pick a model that fits the card's VRAM.

### B4. When you're done

Destroy the instance from the Dashboard. Billing stops when you destroy the instance (see [/terms](https://cloudgpu.app/terms)).

## Option: Raw GPU instead of the Ollama template

If you want your own Ollama version or extra tools, pick **Raw GPU** on Deploy (JupyterLab + CUDA pre-installed, SSH access). Check the environment first, then install Ollama with the official script:

```bash
nvidia-smi
nvcc --version
curl -fsSL https://ollama.com/install.sh | sh
OLLAMA_HOST=127.0.0.1:11434 ollama serve &
ollama pull qwen2.5:0.5b
```

Reach it from your laptop through an SSH tunnel, then use `OLLAMA_BASE_URL=http://host.docker.internal:11434` (Docker) or `http://127.0.0.1:11434` (pip):

```bash
ssh -N -L 11434:127.0.0.1:11434 <user>@<instance-ssh-host> -p <port>
```

Use the SSH user, host and port from your instance. We haven't checked this tunnel on a Raw GPU instance; Ollama's docs say it binds `127.0.0.1:11434` by default, which is what the tunnel forwards.

## FAQ

**How do I connect Open WebUI to a remote Ollama server?**
Start Open WebUI with `OLLAMA_BASE_URL` set to the remote server's URL, for example `-e OLLAMA_BASE_URL=https://<random-id>-i.cloudgpu.app` in the Docker command.

**Do I need a GPU on my laptop to use Open WebUI?**
No. Open WebUI is the interface; the model runs wherever Ollama runs. In option B that is the rented GPU.

**Which GPU should I rent for my model?**
VRAM need depends on model, precision and workflow. See [How much VRAM do I need to run an LLM?](https://cloudgpu.app/guides/how-much-vram-do-i-need-to-run-an-llm) and the cards on [/pricing](https://cloudgpu.app/pricing).

**How is the rented GPU billed?**
Billed per minute, rounded up, 1-minute minimum. Billing stops when you destroy the instance (see [/terms](https://cloudgpu.app/terms)).

## Sources (read 2026-10-27)

- Open WebUI README: install and `OLLAMA_BASE_URL` commands. Open WebUI is under the Open WebUI License; this folder only links to it and does not redistribute it.
- Ollama Linux install docs (`docs/linux.mdx` in the Ollama repo).
- CloudGPU [/docs](https://cloudgpu.app/docs) and [/deploy](https://cloudgpu.app/deploy).
