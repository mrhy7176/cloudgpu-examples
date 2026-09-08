#!/usr/bin/env bash
# The raw request. Nothing else to it.
#   export CLOUDGPU_API_KEY=sk-...
#   bash chat.sh
set -euo pipefail
curl -sS https://cloudgpu.app/v1/chat/completions \
  -H "Authorization: Bearer ${CLOUDGPU_API_KEY}" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "deepseek-v4-flash",
    "messages": [{"role": "user", "content": "Say hello in one sentence."}]
  }'
echo
