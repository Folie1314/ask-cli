"""同一个问题，五种 prompt 写法，对比输出差异。

跑法：python prompt_compare.py
"""

import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com",
    timeout=30.0,
)

QUESTION = "给我一份减脂餐建议"

PROMPTS = {
    "1_裸问": QUESTION,
    "2_给角色": (
        f"你是一位有十年临床经验的注册营养师，擅长为健身人群设计减脂饮食。{QUESTION}"
    ),
    "3_给约束": (
        f"{QUESTION}\n"
        "要求：只列早、中、晚三餐；每餐最多 3 样食物；总字数不超过 120 字；"
        "不要任何解释和开场白。"
    ),
    "4_给示例": (
        f"{QUESTION}\n\n"
        "参考下面这个例子的风格来回答：\n"
        "早餐：鸡蛋2个 + 燕麦50g\n"
        "午餐：鸡胸肉150g + 糙米100g + 西兰花200g\n"
        "晚餐：三文鱼100g + 混合沙拉\n"
        "请按同样的格式给出你的建议，只给内容，不要解释。"
    ),
    "5_给格式": (
        f"{QUESTION}\n"
        "严格按下面的格式输出，不要任何多余文字：\n"
        "早餐：<食物>\n午餐：<食物>\n晚餐：<食物>\n总热量：<数字>kcal"
    ),
}

for name, prompt in PROMPTS.items():
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[{"role": "user", "content": prompt}],
        temperature=0,
    )
    print("=" * 62)
    print(f"【{name}】  token={response.usage.total_tokens}")
    print("-" * 62)
    print(response.choices[0].message.content)
    print()
