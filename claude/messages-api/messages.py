# <!-- REQUIRES /v1/messages — do not publish until live -->
"""Claude Messages API format on cloudgpu.app with the official `anthropic` Python SDK.

base_url is the bare host: the SDK appends /v1/messages itself.

    pip install -r requirements.txt
    export CLOUDGPU_API_KEY=cgw-sk-...
    python messages.py "Explain KV cache in two sentences"
"""
import os
import sys

import anthropic

client = anthropic.Anthropic(
    base_url="https://cloudgpu.app",
    api_key=os.environ["CLOUDGPU_API_KEY"],
)

prompt = sys.argv[1] if len(sys.argv) > 1 else "Say hello in one sentence."

# Model IDs and live prices: https://cloudgpu.app/api
with client.messages.stream(
    model=os.environ.get("CLAUDE_MODEL", "claude-sonnet-5-5"),
    max_tokens=4096,
    messages=[{"role": "user", "content": prompt}],
) as stream:
    for text in stream.text_stream:
        print(text, end="", flush=True)
print()
