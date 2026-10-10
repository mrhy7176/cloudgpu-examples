# Cline with cloudgpu.app

> **Claude models are currently available through Claude Code only.** Setting a `claude-*` Model ID in Cline will not work; use [Claude Code](claude-code.md) for Claude. Cline works with the other models on the gateway, as below.

In the Cline panel in VS Code, open **Settings** (gear icon) and set:

| Field | Value |
|---|---|
| API Provider | **OpenAI Compatible** |
| Base URL | `https://cloudgpu.app/v1` |
| API Key | your `cgw-sk-...` key |
| Model ID | `kimi-k2.7-code` (or `deepseek-v4-pro`, `deepseek-v4-flash`, `glm-5.2`) |

Click **Done** and send a short prompt to check it.

## Notes

- Use the **OpenAI Compatible** provider and a model ID exactly as listed on https://cloudgpu.app/api.
- Cline's agent loop sends the whole task context on every step, so input tokens dominate the bill. Try `deepseek-v4-flash` for routine steps and switch the Model ID to `kimi-k2.7-code` or `deepseek-v4-pro` for the hard tasks.
- Cline's own cost estimate may not match what you are billed; the real charge is in usage on https://cloudgpu.app/api/console.
- If Cline asks for model info such as context window, leave the defaults unless you hit a limit.
