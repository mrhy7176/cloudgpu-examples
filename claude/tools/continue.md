# Claude in Continue via cloudgpu.app

Works today through the OpenAI-compatible endpoint.

Add to `~/.continue/config.yaml`:

```yaml
models:
  - name: Claude Sonnet 5.5 (CloudGPU)
    provider: openai
    model: claude-sonnet-5-5
    apiBase: https://cloudgpu.app/v1
    apiKey: ${{ secrets.CLOUDGPU_API_KEY }}
    roles:
      - chat
      - edit
      - apply
  - name: Claude Opus 5.5 (CloudGPU)
    provider: openai
    model: claude-opus-5-5
    apiBase: https://cloudgpu.app/v1
    apiKey: ${{ secrets.CLOUDGPU_API_KEY }}
    roles:
      - chat
```

Put `CLOUDGPU_API_KEY=cgw-sk-...` in `~/.continue/.env` (or paste the key directly in place of the `secrets` reference for a quick test). Reload the window and pick the model in the Continue sidebar.

## Notes

- Keep `provider: openai`. Continue's Claude-specific provider expects the Messages API format, which is not live on the gateway yet.
- For tab autocomplete, a large Claude model is slow and expensive per keystroke; a small, cheap model is a better fit for that role.
