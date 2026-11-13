# Skill 技能包（可直接安装）

> 8 个 skill，遵循 [Agent Skills 规范](https://agentskills.io/specification)（Anthropic 发布）：
> YAML frontmatter 含 `name`（与目录名一致）+ `description`（触发条件式写法）+
> `metadata`（版本与 related_skills）；正文三层渐进披露——name/description 常驻
> system prompt，激活时加载正文，清单与脚本按需读取。
> 适用于 Claude Code / 其他支持 SKILL.md 的 agent 工具（如兼容 OpenSkills/MCP 标准的环境）。

## 安装方式

### 方式一：Claude Code（本仓库根目录直接可用）
把 `skills/` 下各目录复制到项目 `.claude/skills/` 或用户级
`~/.claude/skills/`：

```bash
# 项目级安装（推荐，随仓库走）
cp -r skills/*  your-paper-project/.claude/skills/

# 用户级安装
cp -r skills/*  ~/.claude/skills/
```

安装后重启会话，skill 会按 description 自动触发；也可显式调用：
> 使用 stat-theory-check skill 审查 theorem 1 的证明

### 方式二：手动对话使用（任何 AI 工具）
没有 skill 机制的工具（网页版对话等）：直接打开对应 `SKILL.md`，
把正文（去掉 frontmatter）贴进对话第一条消息，再继续工作流。

## 技能清单与流水线位置

| Skill | 流水线阶段 | 触发场景 |
|---|---|---|
| [stat-pipeline](stat-pipeline/SKILL.md) | 全程 | 用户描述了一个完整论文任务，需要编排各阶段 |
| [stat-research](stat-research/SKILL.md) | 阶段一·二 | 选题、检索文献、做笔记、写综述 |
| [stat-theory-check](stat-theory-check/SKILL.md) | 阶段三 | 审查定理、证明、假设 |
| [stat-simulation-audit](stat-simulation-audit/SKILL.md) | 阶段四 | 审计模拟/分析代码、检查实验设计 |
| [stat-writing](stat-writing/SKILL.md) | 阶段五 | 起草与润色各节、去 AI 味、中英互译 |
| [stat-citation-verify](stat-citation-verify/SKILL.md) | 全程 | 核验引用（三层核验） |
| [stat-reviewer](stat-reviewer/SKILL.md) | 阶段六 | 三审稿人模拟、meta-review、回复信 |
| [stat-journal-fit](stat-journal-fit/SKILL.md) | 阶段七前半 | 选刊、期刊风格适配、格式与引用迁移、该刊 cover letter（调度 `journals/` 档案） |
| [stat-format-lint](stat-format-lint/SKILL.md) | 阶段七后半 | LaTeX 格式、图表、引用一致性与 AI 味符号的机械检查 |
| [stat-postsub](stat-postsub/SKILL.md) | 阶段 S0·S8 | 投稿系统执行、预印本、催稿与状态跟踪、决策三路、校样与发表后 |

## 设计约定（与仓库其他部分的关系）

- 每个 skill 内部**引用本仓库的清单与脚本**（`checklists/`、`scripts/`、`prompts/`），
  因此安装 skill 时建议整个仓库克隆，相对路径才可解析；
  若单独复制 skill，请把用到的清单一并复制到 skill 目录旁。
- 硬性纪律写在 skill 正文顶部（AI 不可绕过）：引用必须核验、证明必须逐行、
  数字必须溯源。
- 所有 skill 输出都带"人工核验点"，**AI 通过 ≠ 通过**。
