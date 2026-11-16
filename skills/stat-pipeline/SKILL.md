---
name: stat-pipeline
description: 统计学论文全流程编排 skill。use when 用户提出"写一篇统计学论文/从选题到投稿/帮我推进论文的下一个阶段"等整体性任务，或不知道当前该用哪个 skill 时，由本 skill 判断所处阶段并调度其他 stat-* skills 与对应提示词。
metadata:
  version: "1.0"
  related_skills: [stat-research, stat-theory-check, stat-simulation-audit, stat-writing, stat-citation-verify, stat-reviewer, stat-format-lint]
---

# stat-pipeline · 统计论文全流程编排

## 硬性纪律（不可协商）

1. **AI 产出的是研究起点，不是论文。** 每个阶段的交付物必须过对应检查清单，
   由作者裁决后才能进入下一阶段。
2. **引用核验前置**：任何要写进正文的引用，先过 stat-citation-verify 三层核验。
3. **数字溯源**：论文中每个数字必须能指向实验输出文件中的单元格（±0.01 容差），
   小整数、年份、章节号豁免。
4. **大声降级**：无法核验的内容明确标注 `[AI-待核验]` 留给作者，绝不悄悄混入正文。

## 七阶段流水线与阶段门禁

```
S0 立项（stat-postsub + P33 研究章程）──▶ S1 科学问题 ──gate1──▶ S2 文献
──gate2──▶ S3 理论 ──gate3──▶ S4 实验 ──gate4──▶ S5 撰写 ──gate5──▶
S6 审稿模拟 ──gate6──▶ S7 期刊适配（stat-journal-fit + journals/）
──gate7──▶ S8 投稿执行·出版跟进（stat-postsub + P34–P38）
```

| 阶段 | 使用的 skill / 提示词 | 阶段门禁（不通过不进入下一阶段） |
|---|---|---|
| S1 科学问题 | stat-research + `prompts/01` | C1 清单每项能写出具体回答；贡献三条可指认 |
| S2 文献 | stat-research + stat-citation-verify + `prompts/02` | 检索式可复现（PRISMA 记录）；文献池 Zotero 入库 |
| S3 理论 | stat-theory-check + `prompts/03` | C2 清单逐项裁决；每个"显然"已展开 |
| S4 实验 | stat-simulation-audit + `prompts/04` | 冒烟测试通过；C3 清单；结果 CSV 已归档 |
| S5 撰写 | stat-writing + `prompts/05` | 各节初稿 + P21 去 AI 味 + `style_check.py` 符号扫描 + 记号表同步 |
| S6 审稿模拟 | stat-reviewer + `prompts/06` | 三份意见聚合裁决完；必须修项全部修复 |
| S7 期刊适配·格式·投稿 | **stat-journal-fit + `journals/` + `prompts/07`** → stat-format-lint + `presubmit_check.py` + `checklists/C7`+`C8` | 该刊改造清单全过；presubmit 零阻断（或逐条不修理由）；C8 三遍法走完；C7 倒计时清单完成 |
| S8 投稿执行·出版跟进 | stat-postsub + `prompts/08`（P34–P38）+ `docs/11` | P34 预检通过；通信存档；决策三路（修改/拒稿/录用）按 P37 执行 |

## 运行协议

1. **定位阶段**：先问作者（或从工作目录状态判断）当前处于 S1–S7 哪个阶段；
   判断依据：有没有 `refs.bib`（S2 前无）、有没有定理稿（S3 前无）、
   有没有结果 CSV（S4 前无）、有没有全文（S5 前无）。
2. **单阶段推进**：一次只推进一个阶段；结束时输出：
   - 本阶段完成项与未完成项（对照门禁）
   - 下一阶段的第一步动作（具体到"打开哪个文件跑哪条提示词"）
3. **门禁裁决权在作者**：AI 汇报"门禁通过"只是初判，作者明确确认后才切换阶段。
4. **阶段回滚合法**：审稿模拟发现理论漏洞（S6→S3）是正常现象，回滚时只重跑
   受影响的下游阶段。

## 会话开始模板（作者可直接粘贴）

```text
我在写一篇统计学论文：
- 方向：{{高维推断 / 因果推断 / 纵向数据 / …}}
- 当前阶段：{{S1-S7 或"不确定"}}
- 已有材料：{{如"问题陈述一页 + 30 篇文献笔记"}}
- 本轮目标：{{如"把定理 1 的证明审完"}}
请按 stat-pipeline 流程定位我的阶段，检查门禁缺口，给我本轮的
具体执行步骤（用哪条提示词/哪个清单/哪个脚本）。
```

## 相关文件

- 全流程方法论文档：`docs/01-全流程总览.md`
- 各阶段详细操作：`docs/02`–`docs/08`
- 检查清单：`checklists/C1`–`C7`；自动化脚本：`scripts/`
