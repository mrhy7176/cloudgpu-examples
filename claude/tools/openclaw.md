# Claude in OpenClaw via cloudgpu.app

Works today through the OpenAI-compatible endpoint. OpenClaw accepts custom OpenAI-compatible providers; register cloudgpu.app as one and point the agent at a Claude model.

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
          { id: "claude-sonnet-5-5", name: "Claude Sonnet 5.5 (CloudGPU)" },
          { id: "claude-opus-5-5", name: "Claude Opus 5.5 (CloudGPU)" }
        ]
      }
    }
  },
  agents: {
    defaults: {
      model: { primary: "cloudgpu/claude-sonnet-5-5" }
    }
  }
}
```

Export `CLOUDGPU_API_KEY=cgw-sk-...` in the environment OpenClaw runs in, then restart it.

## Notes

- OpenClaw's config schema changes between releases. If a key above is rejected, check the "custom providers" / "models" section of the OpenClaw docs for your version; the values that matter are the base URL `https://cloudgpu.app/v1`, the OpenAI-compatible (chat completions) API type, your key and the model ID.
- An always-on agent can spend tokens while you are not watching. Start on `claude-sonnet-5-5` and a small balance, check usage in https://cloudgpu.app/api/console after the first day.
