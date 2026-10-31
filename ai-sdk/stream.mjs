import { createOpenAICompatible } from '@ai-sdk/openai-compatible';
import { streamText } from 'ai';

if (!process.env.CLOUDGPU_API_KEY) {
  console.error('CLOUDGPU_API_KEY is not set. Create a key at https://cloudgpu.app/api/console and run: export CLOUDGPU_API_KEY=...');
  process.exit(1);
}

const cloudgpu = createOpenAICompatible({
  name: 'cloudgpu',
  apiKey: process.env.CLOUDGPU_API_KEY,
  baseURL: 'https://cloudgpu.app/v1',
  includeUsage: true,
});

const result = streamText({
  model: cloudgpu.chatModel('glm-5.2'),
  prompt: 'Explain what an HTTP API gateway does in three short sentences.',
});

for await (const chunk of result.textStream) {
  process.stdout.write(chunk);
}
process.stdout.write('\n');
