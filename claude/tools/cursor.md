# Cursor with cloudgpu.app

> **Claude models are currently available through Claude Code only.** Adding a `claude-*` model to Cursor will not work; use [Claude Code](claude-code.md) for Claude. Cursor works with the other models on the gateway, as below.

Cursor talks to custom models over the OpenAI protocol, so this uses the OpenAI-compatible endpoint `https://cloudgpu.app/v1`.

1. **Settings → Models → API Keys → OpenAI API Key**: paste your `cgw-sk-...` key.
2. Turn on **Override OpenAI Base URL** and set it to:

   ```
   https://cloudgpu.app/v1
   ```

3. **Add model**: type a model ID exactly as listed on https://cloudgpu.app/api, for example `kimi-k2.7-code`, `deepseek-v4-pro`, `deepseek-v4-flash` or `glm-5.2`, then enable it in the model list.
4. Click **Verify**. If it reports an invalid key, check that the base URL ends in `/v1` and has no trailing slash.
5. Pick the model in the chat / agent model dropdown.

## Notes

- Cursor's menu names move between versions; if the labels above differ, look for "OpenAI API Key" and "Override OpenAI Base URL".
- Your key is used for the chat and agent models you select. Cursor's built-in Tab completion runs on Cursor's own models and does not use your key.
- `kimi-k2.7-code` is the coding-tuned model on the gateway; `deepseek-v4-flash` is the cheap everyday option. Live prices: https://cloudgpu.app/api.
