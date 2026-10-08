#!/usr/bin/env bash
# Claude through the OpenAI-compatible chat/completions endpoint. Works today.
#   export CLOUDGPU_API_KEY=cgw-sk-...
#   bash chat.sh                      # claude-sonnet-5-5
#   MODEL=claude-opus-5-5 bash chat.sh
set -euo pipefail
MODEL="${MODEL:-claude-sonnet-5-5}"
curl -sS https://cloudgpu.app/v1/chat/completions \
  -H "Authorization: Bearer ${CLOUDGPU_API_KEY}" \
  -H "Content-Type: application/json" \
  -d "{
    \"model\": \"${MODEL}\",
    \"messages\": [{\"role\": \"user\", \"content\": \"Say hello in one sentence.\"}]
  }"
echo
