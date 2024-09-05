import OpenAI from 'openai';

const openai = new OpenAI();

export const callOpenAI = async (base64: string) => {
  const stream = await openai.chat.completions.create({
    model: 'gpt-4o-mini',
    messages: [
      { role: 'user', content: "画像からカロリー、たんぱく質、炭水化物、などをキーとして、実際の摂取量の数値を読み取り、Jsonデータとして返却してください。" },
      { role: 'user', content:  `data:image/jpeg;base64,${base64}`}
    ],
    stream: true,
  });
  for await (const chunk of stream) {
    process.stdout.write(chunk.choices[0]?.delta?.content || '');
  }
};
