// Claude through cloudgpu.app from Node.js with the official OpenAI SDK (chat/completions).
//
//   npm install
//   export CLOUDGPU_API_KEY=cgw-sk-...
//   node chat.mjs "Refactor this function and explain the change"
//   CLAUDE_MODEL=claude-opus-5-5 node chat.mjs "Plan a migration from Express to Fastify"
import OpenAI from "openai";

const client = new OpenAI({
  baseURL: "https://cloudgpu.app/v1",
  apiKey: process.env.CLOUDGPU_API_KEY,
});

const prompt = process.argv[2] ?? "Say hello in one sentence.";

// claude-sonnet-5-5 is the everyday default; claude-opus-5-5 for harder work.
// Model IDs and live prices: https://cloudgpu.app/api
const model = process.env.CLAUDE_MODEL ?? "claude-sonnet-5-5";

const stream = await client.chat.completions.create({
  model,
  messages: [{ role: "user", content: prompt }],
  stream: true,
});
for await (const chunk of stream) {
  process.stdout.write(chunk.choices[0]?.delta?.content ?? "");
}
process.stdout.write("\n");
