# 期刊风格档案库（初稿 → 该刊可投状态）

> 用途：同一篇方法型统计论文，投 JASA 与投 Biometrika 的"正确长相"完全不同。
> 本目录给出主流/顶级期刊的**风格档案**（定位、结构惯例、理论呈现、格式硬要求、
> 专属改造清单），配合 `prompts/07-期刊风格适配.md`（P28–P32）与
> `skills/stat-journal-fit/SKILL.md`，把初稿改造成目标期刊的投稿状态。

## ⚠️ 档案性质声明

本档案总结的是**长期稳定的惯例与共识**（发什么、怎么组织、定理怎么放），
**不是**官方投稿指南的逐条转录。页数上限、引用格式细节、匿名政策等会调整——
**投稿前必须以期刊官网最新 Author Guidelines 为准**（改造清单里已留核对项）。
发现档案与官网冲突时，以官网为准，并欢迎提 PR 修正本档案。

## 档案清单

| 档案 | 期刊 | 一句话定位 |
|---|---|---|
| [JASA.md](JASA.md) | Journal of the American Statistical Association | ASA 旗舰，方法+应用双轨 |
| [Annals-of-Statistics.md](Annals-of-Statistics.md) | Annals of Statistics | IMS 旗舰，纯理论 |
| [Biometrika.md](Biometrika.md) | Biometrika | 简洁方法论，理论密度极高 |
| [JRSS-B.md](JRSS-B.md) | JRSS Series B | 方法+实质应用 |
| [AOAS.md](AOAS.md) | Annals of Applied Statistics | IMS 应用旗舰 |
| [Biometrics.md](Biometrics.md) | Biometrics | 生物统计方法+医学应用 |
| [Statistics-in-Medicine.md](Statistics-in-Medicine.md) | Statistics in Medicine | 医学统计应用 |
| [JMLR.md](JMLR.md) | JMLR | 机器学习理论/方法（统计交叉） |
| [中文核心期刊.md](中文核心期刊.md) | 应用概率统计/数理统计与管理/统计研究 等 | 中文统计学核心 |

## 通用改造工作流（七步，详见 prompts/07）

```
选刊决策 → 风格剖析(P28) → 结构重排(P29) → 风格改写(P30)
→ 格式与引用迁移(P31) → 该刊合规终检(P32) → 投稿包
```

| 步骤 | 输入 | 输出 | 质量门槛 |
|---|---|---|---|
| 1 选刊决策 | 贡献类型 + 期刊档案 | 目标刊 + 备选刊 + 理由 | 档案"发什么/不发什么"逐条对得上 |
| 2 风格剖析 | 2–3 篇该刊同方向论文 | 风格规则卡（句式/密度/呈现惯例） | 规则可操作（能对照改写） |
| 3 结构重排 | 初稿 + 该刊结构惯例 | 章节迁移计划 + 重排稿 | 贡献-章节-定理对应不断裂 |
| 4 风格改写 | 重排稿 + 规则卡 + P20 协议 | 期刊风格稿 | 段落级三栏输出，逐段裁决 |
| 5 格式迁移 | 风格稿 + 该刊格式要求 | 可编译投稿版 | 模板/引用样式/图表全迁移 |
| 6 合规终检 | 投稿版 + 档案改造清单 | 零阻断清单 | C8 三遍法走完 + C7 + 档案清单全项通过 |
| 7 投稿包 | 上一步 | 全部文件 + cover letter | 用 `templates/cover-letter.md` |

## 改造前后对照（什么叫"改成该刊风格"）

**改前（AI 味初稿，任何刊都不会收的表达）：**

> Our novel framework, which seamlessly integrates robust estimation with
> debiased inference, not only achieves optimal rates but also paves the way
> for practitioners — a crucial step toward reliable high-dimensional analysis.

**改后（JASA 方法论文风格）：**

> We propose a robust debiased estimator for high-dimensional regression.
> Under Assumption 1 it attains the minimax rate $\sqrt{s\log p/n}$ and
> supports valid confidence intervals (Theorem 2); in simulations the empirical
> coverage ranged from 94.2% to 95.7% across all scenarios (Table 2).

差异点：删掉 novel/seamlessly/not only-but also/破折号插入语等 AI 特征；
每个论断挂定理号/表号；结论带具体数字；句子短、主动、可核查。

## 与其他部件的关系

- 本目录 = **数据**（期刊档案）；`skills/stat-journal-fit` = **逻辑**（调度）；
  `prompts/07` = **弹药**（提示词）。架构沿用 ARS/Polaris 的"技能+资源"分离。
- 改写仍走 P20/P21 的润色与去 AI 味协议（三栏输出、修改阈值、保护区）；
  本目录只解决"往哪个方向改"。
- 选刊犹豫时先跑 P28 剖析两三个候选刊，把规则卡并排比较再定。
