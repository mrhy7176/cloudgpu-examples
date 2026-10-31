import { createOpenAICompatible } from '@ai-sdk/openai-compatible';
import { generateText } from 'ai';

if (!process.env.CLOUDGPU_API_KEY) {
  console.error('CLOUDGPU_API_KEY is not set. Create a key at https://cloudgpu.app/api/console and run: export CLOUDGPU_API_KEY=...');
  process.exit(1);
}

const cloudgpu = createOpenAICompatible({
  name: 'cloudgpu',
  apiKey: process.env.CLOUDGPU_API_KEY,
  baseURL: 'https://cloudgpu.app/v1',
});

const { text } = await generateText({
  model: cloudgpu.chatModel('kimi-k3'),
  prompt: 'Write a one-sentence summary of what a GPU does.',
});

console.log(text);
