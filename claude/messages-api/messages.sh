#!/usr/bin/env bash
#
# Claude Messages API format (POST /v1/messages) on cloudgpu.app.
# Same request shape the `anthropic` SDKs and Claude Code send.
#   export CLOUDGPU_API_KEY=cgw-sk-...
#   bash messages.sh
set -euo pipefail
MODEL="${MODEL:-claude-sonnet-5-5}"
curl -sS https://cloudgpu.app/v1/messages \
  -H "x-api-key: ${CLOUDGPU_API_KEY}" \
  -H "anthropic-version: 2023-06-01" \
  -H "Content-Type: application/json" \
  -d "{
    \"model\": \"${MODEL}\",
    \"max_tokens\": 1024,
    \"messages\": [{\"role\": \"user\", \"content\": \"Say hello in one sentence.\"}]
  }"
echo
