# oss-lab1-git-practice

开源软件通识 · 实验一：GitHub 平台项目协作实践

本仓库用于演示 Git 本地版本控制、远程仓库协作、分支合并与 GitHub 协作流程。

## 项目说明（hotfix 分支修正；主分支调整）

本项目提供一个简单的问候脚本，作为练习 Git 分支与协作流程的载体。

## 目录结构

- `hello.py`：问候脚本
- `README.md`：项目说明

## 协作说明

本段由协作者克隆仓库后补充，用于演示 clone 与 push。

## farewell 用法

```python
from hello import farewell
print(farewell("Open Source"))
```

## 使用示例

```bash
python hello.py
# Hello, Open Source!
# Goodbye, Open Source!
```

## 贡献指南

1. Fork 本仓库并克隆到本地；
2. 新建分支：`git switch -c feature/your-change`；
3. 提交修改并推送到自己的 Fork；
4. 向本仓库提交 Pull Request。

详见 [CONTRIBUTING.md](CONTRIBUTING.md)。