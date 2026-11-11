"""反例：只说"要 JSON"，不给任何格式约束，看模型怎么自由发挥。

跑法：python bad_json.py
"""

import json
import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com",
    timeout=30.0,
)

TEXT = "我想在周三晚上7点去健身房练腿，大概练1小时，强度中等。"

# 关键差别：只说"提取成 JSON"，没说字段、没说不要包装、没说不要解释
PROMPT = f"把下面这段话提取成 JSON：{TEXT}"

for i in range(1, 4):
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[{"role": "user", "content": PROMPT}],
        temperature=0,
    )
    raw = response.choices[0].message.content

    print(f"--- 第 {i} 次原始输出（repr，能看到隐藏字符）---")
    print(repr(raw))

    try:
        json.loads(raw)
        print("→ 可直接解析：是\n")
    except json.JSONDecodeError as exc:
        print(f"→ 可直接解析：否（{exc.msg}）\n")
