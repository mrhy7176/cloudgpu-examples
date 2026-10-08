"""Claude through cloudgpu.app with the official OpenAI SDK (chat/completions).

Works today: the gateway is OpenAI-compatible, so only base_url and the key change.

    pip install -r requirements.txt
    export CLOUDGPU_API_KEY=cgw-sk-...
    python chat.py "Refactor this function and explain the change"
    CLAUDE_MODEL=claude-opus-5-5 python chat.py "Plan a migration from Flask to FastAPI"
"""
import os
import sys

from openai import OpenAI

client = OpenAI(
    base_url="https://cloudgpu.app/v1",
    api_key=os.environ["CLOUDGPU_API_KEY"],
)

prompt = sys.argv[1] if len(sys.argv) > 1 else "Say hello in one sentence."

# claude-sonnet-5-5 is the everyday default; claude-opus-5-5 for harder work.
# Model IDs and live prices: https://cloudgpu.app/api
model = os.environ.get("CLAUDE_MODEL", "claude-sonnet-5-5")

stream = client.chat.completions.create(
    model=model,
    messages=[{"role": "user", "content": prompt}],
    stream=True,
)
for chunk in stream:
    delta = chunk.choices[0].delta.content if chunk.choices else None
    if delta:
        print(delta, end="", flush=True)
print()
