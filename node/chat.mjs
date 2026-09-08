// Chat completion against cloudgpu.app from Node.js with the official OpenAI SDK.
//
//   npm install
//   export CLOUDGPU_API_KEY=sk-...
//   node chat.mjs "Explain KV cache in two sentences"
import OpenAI from "openai";

const client = new OpenAI({
  baseURL: "https://cloudgpu.app/v1",
  apiKey: process.env.CLOUDGPU_API_KEY,
});

const prompt = process.argv[2] ?? "Say hello in one sentence.";

// Model IDs and live prices: https://cloudgpu.app/api
const stream = await client.chat.completions.create({
  model: "deepseek-v4-flash",
  messages: [{ role: "user", content: prompt }],
  stream: true,
});
for await (const chunk of stream) {
  process.stdout.write(chunk.choices[0]?.delta?.content ?? "");
}
process.stdout.write("\n");
