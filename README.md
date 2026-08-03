# MathLab

MathLab 是一个面向数学、理论物理与未来 AI-for-Math 学习的 Python 实验仓库。目标不是积累零散脚本，而是逐步学会编写可安装、可测试、可解释、可复现的科学计算软件。

## Prerequisites

- Windows 11 and PowerShell
- Git
- [uv](https://docs.astral.sh/uv/)
- CPython 3.14（由 uv 按 `.python-version` 管理）

## Install and synchronize

在仓库根目录运行：

```powershell
uv python install
uv sync
```

这会创建仓库本地的 `.venv`，安装 MathLab、科学计算依赖和开发工具，并使用 `uv.lock` 保持环境可复现。

## Quality checks

```powershell
uv run pytest
uv run pytest --cov=mathlab --cov-report=term-missing
uv run ruff check .
uv run ruff format --check .
uv run mypy src
uv build
```

可选地运行全部 pre-commit hooks：

```powershell
uv run pre-commit run --all-files
```

## Directory map

```text
exercises/   short, learner-authored Python exercises
src/mathlab/ reusable and tested package code
tests/       automated behavior tests
projects/    longer mathematical and physical projects
notebooks/   exploration and exposition, not reusable implementations
docs/        syllabus, progress, errors, concepts, and assessments
```

## JupyterLab

Start JupyterLab from the repository root:

```powershell
uv run jupyter lab
```

Keep exploration in notebooks, then move reusable computation into `src/mathlab` and add tests.

## Learning rule

先独立完成练习的第一次实质性尝试，再请 Codex 提示、调试或评审。特别是短程序、核心算法的初版、基础测试设计和月度 blank-file test，应先在没有生成答案的情况下完成。

## First session checklist

1. Run `uv sync`.
2. Run `uv run pytest` and read the five smoke tests.
3. Explain the coefficient order and one Horner-method evaluation by hand.
4. Open `docs/syllabus.md` and identify the current week.
5. Create the first entry in `docs/progress.md` after completing independent work.
