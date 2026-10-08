# Claude in Cline via cloudgpu.app

Works today through the OpenAI-compatible endpoint.

In the Cline panel in VS Code, open **Settings** (gear icon) and set:

| Field | Value |
|---|---|
| API Provider | **OpenAI Compatible** |
| Base URL | `https://cloudgpu.app/v1` |
| API Key | your `cgw-sk-...` key |
| Model ID | `claude-sonnet-5-5` (or `claude-opus-5-5`) |

Click **Done** and send a short prompt to check it.

## Notes

- Use the **OpenAI Compatible** provider, not Cline's built-in Claude provider. The built-in one speaks the Messages API format at `/v1/messages`, which is not live on the gateway yet.
- Cline's agent loop sends the whole task context on every step, so input tokens dominate the bill. Sonnet at $1.00 per million input tokens is the sensible default; switch the Model ID to `claude-opus-5-5` for the hard tasks.
- If Cline asks for model info such as context window, leave the defaults unless you hit a limit.
