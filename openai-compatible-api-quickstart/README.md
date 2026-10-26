# How do I call CloudGPU's OpenAI-compatible API from curl, Python or a coding agent?

Send requests to `https://cloudgpu.app/v1` with an `Authorization: Bearer` header carrying your `cgw-sk-` key; existing OpenAI SDK code only needs a new `base_url` and key (CloudGPU /api/docs, read 2026-10-27).

Updated 2026-10-27

This folder has three small, copy-paste examples:

- **A. curl**: one chat request and the model list.
- **B. Python**: the official OpenAI Python SDK, normal and streaming.
- **C. Aider**: the terminal coding agent, pointed at the same endpoint.

Model ids and the current per-model rates are in the table on the [CloudGPU AI API page](https://cloudgpu.app/api?utm_source=github&utm_medium=referral&utm_campaign=202611_seg04_codingagent&utm_content=gh_ex_api). The examples use `deepseek-v4-flash`, the model in the /api/docs examples; swap in any chat model id from that table or from `GET /v1/models`.

## 0. Get a key

1. Sign in at cloudgpu.app, open the API Console (cloudgpu.app/api/console) and create a key. Copy the `cgw-sk-...` value: it is shown once. CloudGPU stores only a hash of it, so if you lose it, create a new one.
2. Add balance on the [Billing](https://cloudgpu.app/billing) page. API calls are paid from your balance (the same balance GPU rentals use).
3. Put the key in an environment variable, so it stays out of your code and your git history:

   ```bash
   export CLOUDGPU_API_KEY="cgw-sk-..."
   ```

## A. curl

### A1. Chat completion

The request from /api/docs:

```bash
curl https://cloudgpu.app/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $CLOUDGPU_API_KEY" \
  -d '{
    "model": "deepseek-v4-flash",
    "messages": [
      {"role": "system", "content": "You are a helpful assistant."},
      {"role": "user", "content": "Say hi in one sentence."}
    ]
  }'
```

/api/docs says the response has the same shape as OpenAI's chat completion, so the text is in `choices[0].message.content`.

For streaming, add `"stream": true` to the body; the response is Server-Sent Events in the OpenAI-compatible streaming format.

### A2. List models

```bash
curl https://cloudgpu.app/v1/models \
  -H "Authorization: Bearer $CLOUDGPU_API_KEY"
```

Use an `id` from this list as `model`. An id that isn't in the catalog returns `400 model_not_found`.

### A3. Check your setup without spending anything

Without the header you get a 401 (checked 2026-10-27):

```bash
curl -s https://cloudgpu.app/v1/models
# {"error":{"type":"authentication_error","code":"missing_authorization","message":"Provide an Authorization: Bearer <api_key> header."}}
```

If you see `invalid_api_key` instead, the key is wrong or revoked.

## B. Python (official OpenAI SDK)

CloudGPU doesn't ship its own SDK; the OpenAI SDK works with a `base_url` override (/api/docs). According to the official `openai` docs on PyPI ([pypi.org/project/openai](https://pypi.org/project/openai/), read 2026-10-27), the SDK installs with `pip install openai` and needs Python 3.10 or later. The examples below use the 1.x-style client, so install at least 1.0:

```bash
pip install "openai>=1.0"
```

`quickstart.py`:

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["CLOUDGPU_API_KEY"],      # cgw-sk-... from the API Console
    base_url="https://cloudgpu.app/v1",
)

resp = client.chat.completions.create(
    model="deepseek-v4-flash",
    messages=[{"role": "user", "content": "Say hi."}],
)
print(resp.choices[0].message.content)
print(f"Used {resp.usage.total_tokens} tokens")
```

`stream.py` (same client, `stream=True`):

```python
for chunk in client.chat.completions.create(
    model="deepseek-v4-flash",
    messages=[{"role": "user", "content": "Count to 5."}],
    stream=True,
):
    delta = chunk.choices[0].delta.content
    if delta:
        print(delta, end="", flush=True)
```

Use `client.chat.completions` as above. The /api/docs endpoint list has `POST /v1/chat/completions` and no Responses endpoint, so don't rely on `client.responses.create`; we haven't checked what it returns.

## C. Aider (terminal coding agent)

According to the official Aider docs ([OpenAI compatible APIs](https://aider.chat/docs/llms/openai-compat.html), read 2026-10-27), Aider "can connect to any LLM which is accessible via an OpenAI compatible API endpoint": set `OPENAI_API_BASE` and `OPENAI_API_KEY`, then prefix the model name with `openai/`.

```bash
python -m pip install aider-install
aider-install

export OPENAI_API_BASE=https://cloudgpu.app/v1
export OPENAI_API_KEY=$CLOUDGPU_API_KEY

cd /to/your/project
aider --model openai/deepseek-v4-flash
```

On Windows the Aider docs use `setx OPENAI_API_BASE <endpoint>` and `setx OPENAI_API_KEY <key>`, then a new shell. Aider may print a model warning for model names it doesn't know; the docs cover this in their model warnings section. We haven't run Aider against every model; try a small edit first.

## Errors you may see

Errors follow the OpenAI-compatible shape: HTTP status plus `{ "error": { "type", "code", "message" } }` (/api/docs).

| Status | code | What to do |
|---|---|---|
| 401 | `missing_authorization` | Add the `Authorization: Bearer $CLOUDGPU_API_KEY` header. |
| 401 | `invalid_api_key` | Key unknown or revoked: create a new one in the API Console. |
| 400 | `model_not_found` | Use an id from `GET /v1/models`. |
| 402 | `insufficient_balance` | Add balance under Billing. |
| 429 | `rate_limit_exceeded` | Per-minute or per-day limit hit; wait and retry. |
| 503 | `upstream_not_configured` | The model is temporarily unavailable; retry later or use another model. |

## FAQ

**What is the base URL for the CloudGPU API?**
`https://cloudgpu.app/v1`. Chat requests go to `POST /v1/chat/completions` and the model list is `GET /v1/models`.

**Do I need a special SDK?**
No. Use the official OpenAI Python or Node.js SDK and set `base_url` (Python) or `baseURL` (Node) to `https://cloudgpu.app/v1`, with your `cgw-sk-` key as the API key.

**Which model id should I use?**
Any id from `GET /v1/models` or the table on cloudgpu.app/api. The examples here use `deepseek-v4-flash`, the id used in the /api/docs examples.

**How do I use it with a coding agent such as Aider?**
Point the agent's OpenAI-compatible base URL at `https://cloudgpu.app/v1` and use your key. For Aider that is `OPENAI_API_BASE` and `OPENAI_API_KEY`, then `aider --model openai/<model-id>`.

## Sources (read 2026-10-27)

- CloudGPU /api/docs: base URL, `Authorization: Bearer` header, endpoint list, curl / Python / streaming examples, error codes.
- CloudGPU /api: OpenAI-compatible endpoint description and model table.
- Official Aider docs, ["OpenAI compatible APIs"](https://aider.chat/docs/llms/openai-compat.html): `OPENAI_API_BASE`, `OPENAI_API_KEY`, `openai/` model prefix, install commands.
- Official `openai` docs on PyPI ([pypi.org/project/openai](https://pypi.org/project/openai/), read 2026-10-27): install command, Python 3.10+ requirement.
