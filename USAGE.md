# CopilotAgent 使用文档

CopilotAgent 是一个基于 GitHub 的自进化型 AI Agent 运行平台，适合 AI 项目管理、技能快速集成、自动化运维、自我持续学习与知识沉淀。

---

## 目录结构说明

```
.
├── .agent/               # 智能体主控实现（Agent主逻辑、管理API等）
├── .agent_memory/        # Agent 长期记忆体，各类上下文、目标、AI历史数据
│   ├── README.md
│   └── goals.yaml        # 目标示例
├── .agent_skills/        # 可插拔 Skill 能力包目录，每个技能即插即用
│   ├── README.md
│   ├── seo_audit/
│   │   ├── skill.yaml
│   │   └── main.py
│   └── daily_digest/
│       ├── skill.yaml
│       └── main.py
├── .github/workflows/    # GitHub Actions 自动化目录（如每日资讯聚合）
├── projects/             # 由AI孵化的子项目
└── README.md             # 项目简介与入口
```

---

## 快速上手步骤

### 1. 克隆项目

```bash
git clone https://github.com/CherryIce/CopilotAgent.git
cd CopilotAgent
```

### 2. 安装依赖环境

平台使用 Python（推荐 3.8+），部分技能需要 `requests` 和 `beautifulsoup4` 等依赖：

```bash
pip install -r requirements.txt
# 如无 requirements.txt，可直接安装核心依赖：
pip install requests beautifulsoup4 pyyaml
```

### 3. 查看/编辑长期目标

长期目标和上下文存储在 `.agent_memory/goals.yaml`，可用文本或YAML记录要完成的任务、需求或开发意图：

```yaml
- date: 2026-04-29
  goal: "测试CopilotAgent的技能注册与记忆功能"
```

### 4. 运行Agent主程序（技能与记忆加载示例）

```bash
python .agent/agent.py
```
该脚本会扫描技能包、列出所有已注册技能，并打印当前目标记忆体内容。

### 5. 新增/接入技能模块（Skill）

- 在 `.agent_skills/` 下创建新的技能包目录，需包含 `skill.yaml`（元信息）与主实现文件（如 `main.py`）。
- 示例（SEO分析技能）：

```yaml
# .agent_skills/seo_audit/skill.yaml
name: seo_audit
description: "网站SEO问题分析与优化建议"
inputs:
  - name: url
    type: string
outputs:
  - name: report
    type: markdown
dependencies: ["requests", "beautifulsoup4"]
version: "0.1.0"
```
```python
# .agent_skills/seo_audit/main.py
def seo_audit(url):
    # 实现SEO抓取与分析
    ...
```
- 主程序（agent.py）/自动化脚本会自动扫描注册可用的技能

### 6. 运行技能包

可直接通过命令行方式手动调用技能：

```bash
python .agent_skills/seo_audit/main.py "https://example.com"
python .agent_skills/daily_digest/main.py
```

产出内容将自动写入 `.agent_memory/digests/` 等指定目录。

### 7. 自动化：GitHub Actions 工作流

部分自动化操作（如每日技术摘要）可用 GitHub Actions 实现：
- 配置文件位于 `.github/workflows/`
- Example: 每天自动运行 daily_digest，结果写入记忆体

如遇权限，可由仓库拥有者调整 workflow 目录写入权限。

---

## 进阶用法

### 1. 持久化上下文
- 通过 `.agent_memory/` 实现所有对话、知识、操作流程等全生命周期持久化，便于 AI 自动回溯和学习。

### 2. 批量技能集成
- 任何标准化 `skill.yaml` + 代码目录即可直接plug&play，所有技能可被自动发现、注册和批处理。

### 3. AI自动孵化子项目
- 在 `projects/` 下由 Agent 或技能直接派生、管理子项目。

### 4. 持续自进化
- 可在主控 `.agent/` 下增加自学习、自优化机制（如基于历史记忆体做策略优化、知识归纳等）。

---

## 常见问题 Q&A

**Q: 如何接入新技能？**
A: 在 `.agent_skills/` 创建独立目录并提供标准化 `skill.yaml` 及实现脚本即可。

**Q: 如何自动运作/定时执行？**
A: 配置 `.github/workflows/`，即可实现定时运行与自动 GitHub Actions 集成。

**Q: 如何扩展记忆体或目标体系？**
A: 直接编辑/补充 `.agent_memory/` 下的 YAML/文本文件即可，所有持久化结构自动被主控及技能可读取。

---

## 参考

- [README.md](./README.md) — 项目入口
- [技能包开发说明 .agent_skills/README.md](./.agent_skills/README.md)
- [记忆体机制 .agent_memory/README.md](./.agent_memory/README.md)

如需更详细的二次开发集成、定制业务场景支持、各类自动化技能接入，欢迎直接扩展相关目录、完善技能库或与 Copilot 对话自动生成目标文件！
