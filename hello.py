"""第一段脚本：验证 API 通不通。"""

import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()  # 从 .env 读取密钥，密钥不写进代码

client = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com",
)

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[{"role": "user", "content": "用一句话介绍你自己"}],
)

print(response.choices[0].message.content)
print(f"\n本次消耗 token：{response.usage.total_tokens}")
