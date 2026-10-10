# Continue with cloudgpu.app

> **Claude models are currently available through Claude Code only.** A `claude-*` model in Continue will not work; use [Claude Code](claude-code.md) for Claude. Continue works with the other models on the gateway, as below.

Add to `~/.continue/config.yaml`:

```yaml
models:
  - name: Kimi K2.7 Code (CloudGPU)
    provider: openai
    model: kimi-k2.7-code
    apiBase: https://cloudgpu.app/v1
    apiKey: ${{ secrets.CLOUDGPU_API_KEY }}
    roles:
      - chat
      - edit
      - apply
  - name: DeepSeek V4 Flash (CloudGPU)
    provider: openai
    model: deepseek-v4-flash
    apiBase: https://cloudgpu.app/v1
    apiKey: ${{ secrets.CLOUDGPU_API_KEY }}
    roles:
      - chat
      - autocomplete
```

Put `CLOUDGPU_API_KEY=cgw-sk-...` in `~/.continue/.env` (or paste the key directly in place of the `secrets` reference for a quick test). Reload the window and pick the model in the Continue sidebar.

## Notes

- Keep `provider: openai` and use model IDs exactly as listed on https://cloudgpu.app/api.
- For tab autocomplete, a small, cheap model such as `deepseek-v4-flash` is a better fit than a large one.
