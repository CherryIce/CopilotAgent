# CopilotAgent — AI Agent × GitHub 基础设施

本项目聚焦于打造一个以 GitHub 仓库为核心的自进化型 AIAgent 运行平台，包括：

- **🧠 文件即记忆：** 通过 `.agent_memory/` 持久化 Agent 的长期记忆与上下文
- **🔧 技能包抽象（Skill as Module）：** 所有AI能力以 `.agent_skills/` 下的Skill包，具备自描述、易扩展、可复用特性
- **⚡ GitHub Actions 自动化驱动：** Agent 各种自动综述、Issue调度、自动编程等通过Actions流水线持续运转
- **🚀 Vibe Coding 全流程AI孵化：** 需求至上线全流程皆由Agent技能+自动化串联完成

## 项目结构

```
.agent_memory/   # Agent记忆体，存储对话、知识等
.agent_skills/   # 可独立复用的技能能力包
.agent/          # 智能体主程序
.github/workflows/ # 自动化流程
projects/        # AI孵化出的子项目
```

## 快速开始

1. 查看 `.agent_skills/README.md` 了解Skill开发标准，支持Skill自动检索与集成
2. 查看 `.agent_memory/README.md` 了解长期记忆机制
3. 每日自动运作见 `./github/workflows/`
