"""让模型稳定输出 JSON：约束 → 校验 → 失败重试。

跑法：python json_demo.py
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

PROMPT = f"""从下面的文字中提取信息，输出 JSON。

文字：{TEXT}

只输出 JSON 本体，不要用 ``` 代码块包裹，不要任何解释文字。
字段和类型必须严格如下：
{{"day": "周一/周二/周三/周四/周五/周六/周日", "time": "HH:MM 24小时制", "activity": "训练内容", "duration_min": 整数分钟, "intensity": "低/中/高"}}
"""

REQUIRED = {"day", "time", "activity", "duration_min", "intensity"}


def strip_code_fence(text: str) -> str:
    """模型有时会自作主张包一层 ```json ... ```，剥掉它。"""
    text = text.strip()
    if text.startswith("```"):
        text = text.split("\n", 1)[1] if "\n" in text else text
        text = text.rsplit("```", 1)[0]
    return text.strip()


def ask_json(max_retries: int = 3) -> tuple[dict, int]:
    """返回 (解析成功的字典, 用了几次)。三次都失败则抛异常。"""
    last_err: Exception | None = None

    for attempt in range(1, max_retries + 1):
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[{"role": "user", "content": PROMPT}],
            temperature=0,
        )
        raw = response.choices[0].message.content

        try:
            data = json.loads(strip_code_fence(raw))
        except json.JSONDecodeError as exc:
            last_err = exc
            continue

        missing = REQUIRED - data.keys()
        if missing:
            last_err = ValueError(f"缺字段 {missing}")
            continue

        return data, attempt

    raise RuntimeError(f"重试用尽：{last_err}")


if __name__ == "__main__":
    ok = 0
    total_attempts = 0

    for i in range(1, 21):
        try:
            data, attempts = ask_json()
            ok += 1
            total_attempts += attempts
            print(f"[{i:02d}] OK（第 {attempts} 次） {data}")
        except RuntimeError as exc:
            total_attempts += 3
            print(f"[{i:02d}] 失败 {exc}")

    print(f"\n结果：成功 {ok}/20，平均每次调用 {total_attempts / 20:.2f} 次")
