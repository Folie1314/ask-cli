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
- [x] `hello.py` 写好，**待跑通**
- [ ] Day1-B：三参数 + 循环 + 三个坑
- [ ] Day1-C：argparse 封装 + git init + 第一次 commit

## 下一步

```powershell
python hello.py
```

预期：输出一段自我介绍 + `本次消耗 token：xx`。

## 常用

| 目的 | 命令 |
|---|---|
| 用 VS Code 打开项目 | `code .` |
| 装包 | `python -m pip install 包名` |
| 看已装的包 | `python -m pip list` |

pip 已配清华镜像（`pypi.tuna.tsinghua.edu.cn`），装包不用加 `-i` 参数。
