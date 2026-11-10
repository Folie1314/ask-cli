"""命令行 AI 提问工具。

用法：
    python ask.py "你的问题"
    python ask.py "你的问题" -t 0
    python ask.py --help
"""

import argparse
import os
import sys

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com",
    timeout=30.0,      # 30 秒没响应就放弃，不无限等待
    max_retries=2,     # 网络抖动时自动重试 2 次
)


def ask(question: str, temperature: float = 1.0) -> str:
    """把问题发给模型，返回回答文本。"""
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[{"role": "user", "content": question}],
        temperature=temperature,
    )
    return response.choices[0].message.content


def main() -> None:
    parser = argparse.ArgumentParser(description="向 DeepSeek 提一个问题")
    parser.add_argument("question", help="你要问的问题，用引号包起来")
    parser.add_argument(
        "-t",
        "--temperature",
        type=float,
        default=1.0,
        help="随机性，0-2 之间，默认 1.0；要稳定输出就用 0",
    )
    args = parser.parse_args()

    try:
        print(ask(args.question, args.temperature))
    except Exception as exc:
        print(f"出错了：{exc}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
