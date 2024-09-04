import OpenAI from 'openai';

const openai = new OpenAI();

export const callOpenAI = async (base64: string) => {
  const stream = await openai.chat.completions.create({
    model: 'gpt-4o',
    messages: [
      { role: 'user', content: "画像からキーと数値を読み込んで、Jsonデータとして返却してください。" },
      { role: 'user', content:  `data:image/jpeg;base64,${base64}`}
    ],
    stream: true,
  });
  for await (const chunk of stream) {
    process.stdout.write(chunk.choices[0]?.delta?.content || '');
  }
};
