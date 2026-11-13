---
name: stat-format-lint
description: LaTeX 格式与一致性检查 skill。use when 用户要检查论文格式、修交叉引用、清理编号错位、检查图表规范、准备投稿版（匿名化/页数/模板切换）——即论文阶段 S7（格式定稿）与投稿包准备。
metadata:
  version: "1.0"
  related_skills: [stat-pipeline, stat-writing]
---

# stat-format-lint · 格式检查与投稿准备

## 硬性纪律

1. **机械检查交给脚本，语义裁决留给人**：本 skill 调度 `scripts/` 下四个脚本
   做确定性检查，脚本输出的问题逐条人工裁决后再修。
2. **编译两遍再判**：所有"引用断裂"判断在 `latexmk`/两次 xelatex + bibtex
   之后做。
3. **红线标记清零**：`\TODO{}`、`\AICHECK{}`、`\REFCHECK{}` 在投稿版编译前
   必须全部清除（脚本会扫）。

## 工作流

### A. 自动化检查（每次定稿前必跑）

```bash
# 1. 引用一致性：正文 \cite 与 refs.bib 双向、字段完整性、孤儿条目
python scripts/citation_check.py main.tex appendix.tex --bib refs.bib

# 2. 记号与环境：重复 label/宏、悬空引用、未引用定理、"显然"扫描
python scripts/notation_check.py main.tex appendix.tex supplement.tex

# 3. 图表：label 与引用闭环、caption 自含、三线表纪律、手写编号
python scripts/fig_table_check.py main.tex appendix.tex

# 4. AI 味符号与用词：em-dash 插入语、黑名单词、连接词密度、中文 AI 短语
python scripts/style_check.py main.tex appendix.tex
```

退出码非 0 时，按脚本输出逐条处理，直到通过或逐条给出"不修理由"。

### B. 统计论文特有格式纪律（人工，对照 C5 清单）

1. 定理体系：`\newtheorem` 集中定义；assumption 单独编号；
   交叉引用全部 `\cref/\eqref`。
2. 三线表：booktabs；竖线禁用；数字按小数点对齐；表注含重复次数与判据。
3. 数学排版：算子正体（\mathrm{Var}）、$\mathbb{E},\mathbb{P}$、转置 `^\top`；
   行间公式后标点；where 从句定义新符号。
4. 图：矢量 PDF、色盲友好配色（Okabe-Ito/viridis）、黑白可辨冗余编码、
   300 dpi 以上（位图）。
5. 术语与缩写：首次出现给全称；estimator/estimate 区分贯穿全文。

### C. 模板与期刊适配

1. 从 `templates/latex/main.tex`（JASA 风格骨架）出发；切刊时只换文档类与
   bst，不动内容层。
2. 页数超限迁移路径：证明 → 附录；次要表格 → 补充材料；补充材料
   （`supplement.tex`）独立编译可解析。
3. 双盲准备：作者信息/致谢/基金/自引改第三人称/复现包用匿名仓库；
   单独出 anonymous 版本分支。
4. 行号（line package）与投稿系统要求逐项对照。

### D. 投稿包检查（C7 倒计时清单的 Day −3/−1 部分）

- [ ] 编译零 error，warning 过目（overfull box 逐个处理）
- [ ] 全局搜索 TODO/AICHECK/REFCHECK 清零
- [ ] PDF 逐页目检：字体嵌入、图表清晰、超链接正确
- [ ] 复现包：README 一键命令实测；环境锁定文件在；DOI 已生成
- [ ] 投稿系统元数据 + 建议审稿人 + cover letter 就绪
- [ ] 下载回执 PDF 再目检一遍

## 常见问题速修表

| 症状 | 根因 | 修法 |
|---|---|---|
| 交叉引用 "？?" | 单遍编译/label 拼错 | latexmk 全流程；notation_check 找拼错 |
| 图表未引用 | 忘 \cref | fig_table_check 输出未引用清单 |
| 参考文献字段缺失 | 手打条目 | 从出版商官方 BibTeX 重导出 |
| 定理编号错位 | 手写编号 | 全改 \cref + 环境 |
| 附录引用主文断裂 | supplement 独立编译 | 补充材料内自含 label |
| 匿名版泄露身份 | 致谢/链接残留 | grep 致谢、thanks、github 字样 |

## 相关文件

`scripts/citation_check.py` · `scripts/notation_check.py` ·
`scripts/fig_table_check.py` · `scripts/style_check.py` ·
`checklists/C5-格式图表检查清单.md` · `checklists/C7-投稿前终检清单.md` ·
`docs/08-阶段七-格式与投稿.md` ·
`../journals/`（期刊风格档案：风格改写归 stat-journal-fit，本 skill 只管格式层） ·
`templates/latex/`（main.tex / appendix.tex / supplement.tex / refs.bib）
