---
name: stat-writing
description: 统计学论文写作与润色 skill。use when 用户要起草论文某节（Introduction/方法/摘要等）、润色学术英文、去 AI 味、中英互译、设计图表与 caption——即论文阶段 S5（撰写）的全部任务。
metadata:
  version: "1.0"
  related_skills: [stat-pipeline, stat-format-lint]
---

# stat-writing · 论文撰写与语言

## 硬性纪律

1. **只改表达不改内容**：任何改变数学含义、条件范围、结论强度的润色都违规；
   不确定是否属内容改动，列出问作者而不是改。
2. **以段落为单位处理**（Manubot ai-revision 实践）：整章一次改 = 大面积失控；
   逐段给出"原句→改句→理由"三栏，作者逐段接受/拒绝。
3. **AI 生成内容先打标**：初稿中 AI 写的句子包 `\AICHECK{}`，核验后清除；
   `scripts/notation_check.py` 会扫描残留。
4. **起草顺序固定**（Polaris 纪律）：Introduction → Method → Experimental
   Setup → Results → Discussion → Abstract（最后写）；Related Work 可最后。
5. 每个数字有出处、每个引用来自受控文献池（核验过的 refs.bib）。

## 工作流

### A. 各节起草（用对应提示词，全部在 `prompts/05-论文撰写.md`）

| 节 | 提示词 | 要点 |
|---|---|---|
| Introduction | P17 | 五段式：科学问题→方法缺口→本文方法→贡献列表→文献与结构；禁"In recent years"开头 |
| Methodology | P18 | 2.1 setup/记号 → 2.2 估计量（式后三项解读+差分）→ 2.3 算法；公式是句子的一部分 |
| Theoretical results | P18 模式 + stat-theory-check | Assumptions→Main theorem→Remark→Proof sketch；全文证明在附录 |
| 图表 | P19 | 图表选型表 → caption 自含模板 → 正文引用句 ×2 |
| 摘要与标题 | P23 | 六句结构（S1–S6）；标题=方法名+统计问题+方法类型；摘要数字与正文一致 |

### B. 语言润色（逐节滚动）
1. **P20** 学术润色：三栏输出 + 重点清除 AI 高频词（delve/crucial/pivotal/
   comprehensive/utilize/leverage/moreover 连用…）+ 时态纪律 + 术语表对齐
   + 末尾"内容改动风险清单"。
2. **P21** 去 AI 味：模板化结构/高频词/三连排比/空洞强调/拟人化/同构段落/
   从句套娃；手法优先级 = 删 > 拆 > 换 > 调；标尺是 Casella/Hastie 式
   平实直接文风。
3. 中文论文：C4-C 组（翻译腔、"的"字链、全角标点）+ 术语表中文列。

### C. 中英互译
用 **P22**：术语绝对优先（`docs/glossary-中英术语表.md`）+ 数学符号原样 +
句法重构非直译 + 量化表达保真 + 输出新术语暂定表与拿不准句。

## 质量底线（每个交付物自查）

- [ ] C4 清单 A/B 组过一遍（AI 味、时态、术语、差分句式）
- [ ] 每个论断有出处（引用/定理号/表号/明确标注为主张）
- [ ] 贡献列表与正文对应（C4-D2）
- [ ] 新记号登记进记号表；`scripts/notation_check.py` 通过
- [ ] 术语表有更新则同步提交（本项目约定）

## 相关文件

`prompts/05-论文撰写.md`（P17–P23）· `checklists/C4-写作语言检查清单.md` ·
`checklists/C5-格式图表检查清单.md` · `docs/glossary-中英术语表.md` ·
`docs/06-阶段五-论文撰写.md` · `templates/latex/main.tex`
