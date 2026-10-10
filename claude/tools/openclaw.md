# OpenClaw with cloudgpu.app

> **Claude models are currently available through Claude Code only.** Registering a `claude-*` model in OpenClaw will not work; use [Claude Code](claude-code.md) for Claude. OpenClaw works with the other models on the gateway, as below.

OpenClaw accepts custom OpenAI-compatible providers; register cloudgpu.app as one and point the agent at one of its models.

In `~/.openclaw/openclaw.json`:

```json5
{
  models: {
    mode: "merge",
    providers: {
      cloudgpu: {
        baseUrl: "https://cloudgpu.app/v1",
        apiKey: "${CLOUDGPU_API_KEY}",
        api: "openai-completions",
        models: [
          { id: "kimi-k2.7-code", name: "Kimi K2.7 Code (CloudGPU)" },
          { id: "deepseek-v4-flash", name: "DeepSeek V4 Flash (CloudGPU)" }
        ]
      }
    }
  },
  agents: {
    defaults: {
      model: { primary: "cloudgpu/deepseek-v4-flash" }
    }
  }
}
```

Export `CLOUDGPU_API_KEY=cgw-sk-...` in the environment OpenClaw runs in, then restart it.

## Notes

- OpenClaw's config schema changes between releases. If a key above is rejected, check the "custom providers" / "models" section of the OpenClaw docs for your version; the values that matter are the base URL `https://cloudgpu.app/v1`, the OpenAI-compatible (chat completions) API type, your key and the model ID.
- An always-on agent can spend tokens while you are not watching. Start on a cheap model and a small balance, and check usage in https://cloudgpu.app/api/console after the first day.
