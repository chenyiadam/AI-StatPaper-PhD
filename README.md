<div align="center">

# AI-StatPaper-PhD

**用 AI 写出博士水平的统计学论文：全流程工作流 · 提示词库 · Skill 技能包 · 可复现模板 · 自动化检查**

七阶段流水线 · 38 条可复制提示词 · 10 个可安装 Skill · 7 份检查清单 · 4 个检查脚本 · 9 份期刊风格档案

*从立项到发表，AI 做苦力，人做决策，门禁保质量。*

中文 · **[English](README.en.md)**

</div>

---

## 这是什么

一份**面向统计学博士生与青年研究者**的开源工程：把"用 AI 写论文"从一句
口号变成可执行、可审计、可复现的流水线。

它不生成论文——它让你在 AI 的加速下，自己产出**深刻的科学问题、经得起
逐行攻击的理论证明、可复现的模拟与真实数据实验、以及严谨到格式层面的
学术文本**。

```mermaid
flowchart LR
    S0[S0 立项] --> S1[S1 科学问题] --> S2[S2 文献] --> S3[S3 理论] --> S4[S4 实验]
    S4 --> S5[S5 撰写] --> S6[S6 审稿模拟] --> S7[S7 期刊适配·格式·投稿] --> S8[S8 投稿执行·出版跟进]
    S6 -.回滚.-> S3
```

每一个环节都有：**方法论**（`docs/`）→ **提示词**（`prompts/`，P01–P38）→
**检查清单**（`checklists/`，C1–C7）→ **自动化脚本**（`scripts/`，×4）→
**期刊风格档案**（`journals/`，×9）→ **一键化 skill**（`skills/`，×9）。

## 为什么是你需要的（独特优势）

现有的 AI 学术工具（OpenScholar、Polaris、ARS、GPT Academic、各类提示词合集）
解决了"通用学术"问题。但**统计学论文有它们都不处理的硬核**：
定理-证明体系、渐近理论、模拟研究的 size 校正、覆盖率对真参数、
JASA 式结构惯例。本项目做了五件它们没做的事：

| # | 独特点 | 一句话 |
|---|---|---|
| 1 | **理论检查流水线** | 六类证明漏洞扫描（$O_p$ 运算、事件完整性、KKT 条件、维数陷阱、幻觉引理引用）+ 双模型交叉攻击 + 反例构造——`prompts/03` + `checklists/C2` + `skills/stat-theory-check` |
| 2 | **三层引用核验工程化** | 存在性 → 字段一致性 → 内容支撑；"无法验证 ≠ 无效"；一条引用三张核验卡——`checklists/C6` + `skills/stat-citation-verify` + `scripts/citation_check.py` |
| 3 | **实验审计与数字对账** | 论文中每个数字必须溯源到实验输出单元格（±0.01 容差）；基准调参公平性协议；冒烟测试清单——`prompts/04` + `checklists/C3` |
| 4 | **门禁制七阶段流水线** | 每阶段出口有可判定的门禁；不过不进；降级要大声（`[AI-待核验]`），绝不悄悄混入——`skills/stat-pipeline` + `docs/01` |
| 5 | **统计学双语深度** | 60+ 词条中英术语表（estimator/estimate 之辨）+ 中英互译纪律 + JASA 风格 LaTeX 骨架——`docs/glossary` + `templates/latex/` |
| 6 | **期刊风格档案库** ⭐ | 9 个统计学主流/顶级期刊档案（JASA/AoS/Biometrika/JRSS-B/AOAS/Biometrics/SIM/JMLR/中文核心）+ P28–P32 适配链，把初稿改造成该刊可投状态——`journals/` + `skills/stat-journal-fit` |
| 7 | **AI 味符号扫描器** ⭐ | 第四个脚本 style_check.py：em-dash 插入语（数值区间 en-dash 保留）、30+ 黑名单词、连接词密度、中文 AI 短语——确定性代码做符号层的重活 |

方法论内核借鉴了被验证过的开源实践（**Polaris** 的"确定性代码做重活、
LLM 只做判断"与 fact pack 数字对账；**AI Scientist** 的审稿 rubric 与
ensemble 聚合；**OpenScholar** 的 Self-Feedback 与引文核验；
**open-academic-paper-gen** 的三层引用核验；**Manubot** 的段落级 AI 修改；
**awesome-ai-research-writing**（微软亚研院/字节 Seed 等研究员技巧合集）的
五段式提示词骨架、修改阈值机制与 AI 味词黑名单）——完整谱系与出处见
[docs/10-开源项目谱系.md](docs/10-开源项目谱系.md)。
期刊风格档案（`journals/`）基于各期刊公开的作者指南与长期惯例整理，
投稿前以官网最新指南为准。

## 30 秒上手

```bash
git clone <本仓库>
# 1) 体验机械检查（无需任何模型）
python scripts/citation_check.py templates/latex/main.tex templates/latex/refs.bib
python scripts/notation_check.py templates/latex/main.tex
python scripts/style_check.py templates/latex/main.tex    # AI 味符号与用词扫描
# 2) 体验第一条提示词
#    打开 prompts/01-科学问题与选题.md，把 P01 整段复制进任意 AI 对话框
# 3) 安装全部 skill（Claude Code）
cp -r skills/* your-paper-project/.claude/skills/
```

## 仓库结构

```
AI-StatPaper-PhD/
├── README.md / README.en.md  ← 你在这里（中/英）
├── docs/                     方法论（10 篇 + 术语表，中文）
│   ├── 01-全流程总览.md          七阶段流水线 + 五条全局原则 + 门禁表
│   ├── 02~08-阶段一~七.md        每阶段的方法、操作流程、门禁
│   ├── 09-学术诚信与AI使用披露.md  红线 + 披露模板 + 人的不可替代清单
│   ├── 10-开源项目谱系.md        借鉴了谁、借了什么、怎么改的
│   └── glossary-中英术语表.md    60+ 统计术语双语表
├── prompts/                  提示词库（P01–P38，可直接复制）
│   ├── 01-科学问题与选题.md      P01 凝练 · P02 空白定位 · P03 贡献陈述
│   ├── 02-文献调研与引用.md      P04 检索 · P05 精读 · P06 综述 · P07 三层核验
│   ├── 03-理论推导与检查.md      P08 定理体系 · P09 证明起草 · P10 逐行攻击
│   │                           P11 假设审查 · P12 反例构造
│   ├── 04-实验设计与审计.md      P13 模拟设计 · P14 代码审计 · P15 解读 · P16 真实数据
│   ├── 05-论文撰写.md           P17–P23（各节起草/润色/去AI味/互译/摘要）
│   ├── 06-审稿与投稿.md         P24 三审稿人 · P25 聚合 · P26 回复信 · P27 终检
│   ├── 07-期刊风格适配.md        P28 风格剖析 · P29 结构重排 · P30 风格改写
│   │                           P31 格式迁移 · P32 合规终检
│   ├── 08-立项与投稿执行.md      P33 研究章程 · P34 投稿系统 · P35 预印本
│   │                           P36 催稿 · P37 决策三路 · P38 校样与发表后
│   └── en/                      英文版（与中文 1:1 对应，供国际用户使用）
├── journals/                 期刊风格档案库（初稿 → 该刊可投状态）⭐
│   ├── README.md                通用改造工作流 + 改造前后对照
│   ├── JASA / Annals-of-Statistics / Biometrika / JRSS-B / AOAS
│   ├── Biometrics / Statistics-in-Medicine / JMLR / 中文核心期刊
│   └── en/                      英文版档案
├── skills/                   可安装技能包（10 个，中文，含安装说明）
│   ├── stat-pipeline            全流程编排（阶段定位 + 门禁）
│   ├── stat-research            选题与文献
│   ├── stat-theory-check        定理与证明审查 ⭐
│   ├── stat-simulation-audit    实验设计与代码审计 ⭐
│   ├── stat-writing             撰写与润色
│   ├── stat-citation-verify     三层引用核验 ⭐
│   ├── stat-reviewer            审稿模拟与修回
│   ├── stat-journal-fit         期刊风格适配 ⭐（调度 journals/ 档案）
│   ├── stat-format-lint         格式检查与投稿准备
│   └── stat-postsub             投稿执行与出版跟进（催稿/决策三路/校样）
├── skills-en/                英文版 SKILL.md（技能名相同，供国际用户安装）
├── checklists/               检查清单（C1–C7，中文）
│   └── en/                      英文版清单
├── scripts/                  可执行检查工具（仅标准库，Python 3.8+；对英文论文同样适用）
│   ├── citation_check.py        正文-bib 双向一致 + 字段完整性 + 幻觉信号
│   ├── notation_check.py        重复宏/label、悬空引用、"显然"扫描、TODO 残留
│   ├── fig_table_check.py       图表引用闭环、caption 自含、三线表纪律
│   └── style_check.py           AI 味符号与用词（em-dash 插入语、黑名单词、中文 AI 短语）
├── templates/                可复用模板
│   ├── latex/                   JASA 风格论文骨架（main/appendix/supplement/refs.bib）
│   ├── quarto/paper.qmd         代码-正文同文件的动态论文
│   ├── simulation/              模拟实验骨架（R + Python，种子规则化）
│   ├── project/复现包结构.md      TIER 4.0 复现包目录 + README 骨架
│   ├── cover-letter.md          投稿信模板（P32 产出该刊版）
│   └── response-letter.tex      审稿回复信模板（意见斜体/修改标蓝）
└── examples/                 示例（最小走通样例，中文）
```

⭐ = 本项目原创性最强的部件。

**多语言说明**：操作性资产（提示词/技能/清单/期刊档案）中英双语；`docs/` 方法论文、
`examples/` 与脚本输出信息暂为中文——脚本本身对英文论文完全适用，欢迎 PR 补充英文翻译；
术语表本身即双语。

## 推荐工作流（一篇方法型统计论文）

| 周 | 阶段 | 动作 | 用什么 |
|---|---|---|---|
| 1–2 | 选题+文献 | 凝练问题、检索、精读 30 篇 | P01–P05 · C1 |
| 3–6 | 理论 | 定理体系 → 证明 → 双模型攻击 | P08–P12 · C2 · skill: stat-theory-check |
| 5–8 | 实验（并行） | 设计 → 审计 → 冒烟 → 全量 | P13–P15 · C3 · templates/simulation |
| 8–10 | 撰写 | 各节起草 → 润色 → 去AI味 | P17–P23 · C4 · skill: stat-writing |
| 11 | 审稿模拟 | 三审稿人两轮 → 修复 | P24–P27 · skill: stat-reviewer |
| 12 | 期刊适配+定稿 | 风格适配 → 四脚本 → 倒计时 → 提交 | journals/ · P28–P32 · scripts ×4 · C5–C7 · skill: stat-journal-fit, stat-format-lint |
| 13+ | 投稿执行·出版跟进 | 系统提交 → 预印本 → 状态跟踪/催稿 → 决策三路 → 校样 | P33–P38 · docs/11 · skill: stat-postsub |

**全程伺服**：stat-citation-verify（每条引用）· stat-pipeline（迷路时定位阶段）。

## 配套工具链（开源生态，按环节选用）

| 环节 | 工具 | 说明 |
|---|---|---|
| 文献管理 | [Zotero](https://www.zotero.org/) + [Better BibTeX](https://github.com/retorquere/zotero-better-bibtex) | citekey 规范、GB/T 7714 支持 |
| 文献问答 | [OpenScholar](https://openscholar.allen.ai/) / [PaperQA2](https://github.com/Future-House/paper-qa) | 带真实引文的综述式回答（引用仍需 C6 核验） |
| 翻译润色 | [GPT Academic](https://github.com/binary-husky/gpt_academic) | PDF/LaTeX 整篇翻译、多模型并行 |
| 动态论文 | [Quarto](https://quarto.org/) | 代码-正文-图表同文件，数字不可能抄错 |
| 终稿排版 | LaTeX / Overleaf | 配合 `templates/latex/` 骨架 |
| 复现发布 | Zenodo / OSF | 取 DOI，论文引用复现包 |
| 论文即代码 | [Manubot](https://manubot.org/) | Git + CI + PR 式协作（课题组综述尤其合适） |

## 三条铁律

1. **AI 给出的每条引用，人工核验通过前视为不存在。**
   （通用模型引文幻觉率 78%–90%，OpenScholar/Nature 2026）
2. **AI 生成的证明，逐行审查通过前视为有误。**
3. **论文中的每个数字，必须能溯源到实验输出。**

更多诚信规范与披露模板：[docs/09-学术诚信与AI使用披露.md](docs/09-学术诚信与AI使用披露.md)。

## 适合谁 / 不适合谁

✅ **适合**：统计学/生物统计/计量方向博士生与青年研究者；
要写方法型论文（方法+定理+模拟+数据）；愿意做核验工作换质量的人。

❌ **不适合**：想要"一键生成论文"的人（本项目的设计前提是学术诚信红线）；
非实证/非方法类写作（纯理论数学、纯综述另议）。

## 参与

见 [CONTRIBUTING.md](CONTRIBUTING.md)。尤其欢迎：
新方向的经验（贝叶斯/因果/函数型数据的专用清单）、更多检查脚本、
真实案例的"审稿人吐槽 → 清单条目"转化。

## 许可与致敬

代码与文档：MIT。本项目融合了 [docs/10-开源项目谱系.md](docs/10-开源项目谱系.md)
所列开源项目的思想与规则（OpenScholar · Polaris · open-academic-paper-gen ·
AI Scientist · PaperQA2 · Manubot · GPT Academic · awesome-ai-research-writing ·
ARS · Quarto · TIER Protocol 等），全部致敬与出处见谱系页。

<div align="center">
<sub>如果这个项目帮你少走了一个月弯路，欢迎点一个 ⭐</sub>
</div>
