# 开工必读

项目：`C:\dev\ask-cli`
Python：3.12.10（项目内 `.venv`）
模型：DeepSeek（`deepseek-chat`）

## 每次开新终端，先做这三步

```powershell
cd C:\dev\ask-cli
.\.venv\Scripts\Activate.ps1
python --version
```

必须看到提示符前面有 `(.venv)`，才算激活成功。

忘了激活的症状：`ModuleNotFoundError: No module named 'openai'`（明明装了）。

## 当前进度

- [x] Python 3.12 + VS Code + Git
- [x] 虚拟环境 `.venv`
- [x] `openai` + `python-dotenv`
- [x] `.env` 配好 DeepSeek key
- [x] `hello.py` 跑通（30 token）
- [x] Day1-B：三参数 + 对话循环 `chat.py` + 超时与计费
- [x] Day1-C：argparse 封装 `ask.py` + git 提交 + 推送到 GitHub
- [x] Day1 硬指标完成：`2026-11-10`

远程仓库：https://github.com/Folie1314/ask-cli

## 文件说明

| 文件 | 用途 |
|---|---|
| `hello.py` | 最小验证脚本，跑通即止 |
| `chat.py` | 交互式多轮对话，带历史记忆 |
| `ask.py` | 命令行工具 `python ask.py "问题" [-t 0]` |

## 下一步（Day2）

Prompt 四种写法 + JSON 结构化输出 + 20 次稳定性测试。

## 常用

| 目的 | 命令 |
|---|---|
| 用 VS Code 打开项目 | `code .` |
| 装包 | `python -m pip install 包名` |
| 看已装的包 | `python -m pip list` |

pip 已配清华镜像（`pypi.tuna.tsinghua.edu.cn`），装包不用加 `-i` 参数。
