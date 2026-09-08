#!/usr/bin/env bash
# List the model IDs your key can call.
set -euo pipefail
curl -sS https://cloudgpu.app/v1/models -H "Authorization: Bearer ${CLOUDGPU_API_KEY}"
echo
