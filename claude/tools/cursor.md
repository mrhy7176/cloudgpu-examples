# Claude in Cursor via cloudgpu.app

Cursor talks to custom models over the OpenAI protocol, so this uses the OpenAI-compatible endpoint, which works today.

1. **Settings → Models → API Keys → OpenAI API Key**: paste your `cgw-sk-...` key.
2. Turn on **Override OpenAI Base URL** and set it to:

   ```
   https://cloudgpu.app/v1
   ```

3. **Add model**: type `claude-sonnet-5-5` (and `claude-opus-5-5` if you want it), then enable it in the model list.
4. Click **Verify**. If it reports an invalid key, check that the base URL ends in `/v1` and has no trailing slash.
5. Pick the model in the chat / agent model dropdown.

## Notes

- Cursor's menu names move between versions; if the labels above differ, look for "OpenAI API Key" and "Override OpenAI Base URL".
- If Cursor already lists a built-in Claude model with the same name, make sure the one you select is the custom entry you added; otherwise the request may go through Cursor's own plan instead of your key. If in doubt, watch your balance on https://cloudgpu.app/api/console after a test prompt.
- Your key is used for the chat and agent models you select. Cursor's built-in Tab completion runs on Cursor's own models and does not use your key.
- Prices per million tokens: `claude-sonnet-5-5` $1.00 in / $5.00 out, `claude-opus-5-5` $2.00 / $10.00 (8 October 2026; live table at https://cloudgpu.app/api).
