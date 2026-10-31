# Vercel AI SDK with CloudGPU

CloudGPU's OpenAI-compatible model API (`https://cloudgpu.app/v1`) used through the Vercel AI SDK's [`@ai-sdk/openai-compatible`](https://ai-sdk.dev/providers/openai-compatible-providers) provider. Two examples: `generateText` and `streamText`.

## Install

```bash
npm install ai @ai-sdk/openai-compatible
```

## API key

Create a key at https://cloudgpu.app/api/console, then:

```bash
export CLOUDGPU_API_KEY=...
```

## Provider

```js
import { createOpenAICompatible } from '@ai-sdk/openai-compatible';

const cloudgpu = createOpenAICompatible({
  name: 'cloudgpu',
  apiKey: process.env.CLOUDGPU_API_KEY,
  baseURL: 'https://cloudgpu.app/v1',
});
```

## Examples

`generate.mjs` calls `generateText` with `kimi-k3` and prints the text:

```bash
npm run generate
```

```js
const { text } = await generateText({
  model: cloudgpu.chatModel('kimi-k3'),
  prompt: 'Write a one-sentence summary of what a GPU does.',
});
```

`stream.mjs` calls `streamText` with `glm-5.2` and prints each chunk of `textStream`. It sets `includeUsage: true` on the provider so usage is returned with the stream:

```bash
npm run stream
```

```js
const result = streamText({
  model: cloudgpu.chatModel('glm-5.2'),
  prompt: 'Explain what an HTTP API gateway does in three short sentences.',
});
for await (const chunk of result.textStream) process.stdout.write(chunk);
```

## Switching models

Pass a different model ID to `cloudgpu.chatModel(...)`, for example `kimi-k3`, `glm-5.2`, `deepseek-v4.1-flash` or `deepseek-v4-pro`. The current list is returned by:

```bash
curl https://cloudgpu.app/v1/models -H "Authorization: Bearer $CLOUDGPU_API_KEY"
```

## Links

- CloudGPU API docs: https://cloudgpu.app/api/docs
- AI SDK OpenAI Compatible provider docs: https://ai-sdk.dev/providers/openai-compatible-providers
