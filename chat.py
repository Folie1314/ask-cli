"""对话循环：读输入 → 出结果 → 再读输入。"""

import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com",
)

# 对话历史。每次请求都把这个列表整份发给模型，这就是"它为什么记得上一句"
messages = []

while True:
    user_input = input("\n你：")

    if user_input.strip().lower() in ("exit", "quit", "q"):
        print("再见。")
        break

    messages.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=messages,
        temperature=1.5,
    )

    reply = response.choices[0].message.content
    messages.append({"role": "assistant", "content": reply})

    print(f"\nAI：{reply}")
    print(f"[本轮 token：{response.usage.total_tokens}｜历史消息数：{len(messages)}]")
