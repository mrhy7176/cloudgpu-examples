"""Chat completion against cloudgpu.app with the official OpenAI SDK.

    pip install -r requirements.txt
    export CLOUDGPU_API_KEY=sk-...
    python chat.py "Explain KV cache in two sentences"
"""
import os
import sys

from openai import OpenAI

client = OpenAI(
    base_url="https://cloudgpu.app/v1",
    api_key=os.environ["CLOUDGPU_API_KEY"],
)

prompt = sys.argv[1] if len(sys.argv) > 1 else "Say hello in one sentence."

# Model IDs and live prices: https://cloudgpu.app/api
stream = client.chat.completions.create(
    model="deepseek-v4-flash",
    messages=[{"role": "user", "content": prompt}],
    stream=True,
)
for chunk in stream:
    delta = chunk.choices[0].delta.content if chunk.choices else None
    if delta:
        print(delta, end="", flush=True)
print()
