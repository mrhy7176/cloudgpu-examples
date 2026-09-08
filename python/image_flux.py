"""Generate an image with FLUX.1 through the OpenAI-compatible images endpoint.

    export CLOUDGPU_API_KEY=sk-...
    python image_flux.py "a lighthouse at dawn, film photo"
Writes out.png in the current directory.
"""
import base64
import os
import sys

from openai import OpenAI

client = OpenAI(base_url="https://cloudgpu.app/v1", api_key=os.environ["CLOUDGPU_API_KEY"])

prompt = sys.argv[1] if len(sys.argv) > 1 else "a lighthouse at dawn, film photo"

# flux-1-schnell is the cheap fast one; flux-1-dev for quality. Prices: https://cloudgpu.app/api
result = client.images.generate(
    model="flux-1-schnell",
    prompt=prompt,
    size="1024x1024",
    response_format="b64_json",
)
with open("out.png", "wb") as f:
    f.write(base64.b64decode(result.data[0].b64_json))
print("wrote out.png")
