# JASA · Journal of the American Statistical Association

> ASA 旗舰刊。档案为惯例性总结，投稿前以 ASA 官网最新作者指南为准。

## 定位与偏好

**发什么**：两条轨道——
- **Theory & Methods**：新统计方法 + 实质理论保证（相合性/渐近分布/速率/
  推断有效性）。纯数值技巧或无定理的方法论很难进入。
- **Applications & Case Studies**：以**新应用或新数据**为中心的贡献，
  方法可以是组合创新，但必须解决该应用领域的关键统计难题。

**不发什么**：纯模拟比较、已有方法的增量变体（换个罚函数/换个核函数）、
没有真实数据的方法论文（T&M 轨也期望至少一个数据集说明实践相关性）。

## 结构惯例

- Introduction 五段式（本项目 `prompts/P17` 即按此设计）：科学问题 →
  方法缺口 → 本文方法 → **贡献列表 (i)(ii)(iii)** → 文献与结构。
  贡献列表是 JASA 的招牌结构，每条要能指认到定理/表号。
- 方法节先 setup/记号，再估计量，再算法；理论节 = Assumptions →
  Main theorem → Remark（与文献速率对比）→ Proof sketch；
  **全文证明放 appendix 或 supplement**（正文页数紧张）。
- Discussion 节：局限 + 扩展 + 实践建议，审稿人非常看这一节是否诚实具体。
- 摘要约 200 词以内，必须有理论结论与量化实验结论各至少一句。

## 语言与语气

- author-year 引用（chicago 类样式），\citep/\citet 分工。
- 自信但克制：可以说 "We propose / We establish"，禁 novel/seamlessly/
  significantly（无数字支撑的）。
- 应用文风：非统计读者能读懂 Introduction 与 Discussion（跨领域读者群大）。

## 理论呈现

- 定理密度：T&M 轨通常 2–4 个主要结果（估计误差界 + 渐近分布/推断定理为标配）。
- 假设必须逐条有 Remark（强弱对比、能否放松）；速率与 minimax 下界对齐
  或说明缺口。
- 下界论证（Le Cam/Fano）是加分项，若有，放附录并核对散度计算。

## 实验（模拟 + 数据）期望

- 模拟：场景网格 + 至少一个重尾/边界场景；size 校正与覆盖率必查；
  基准方法必须调参（ASA 审稿人对"稻草人对照"零容忍）。
- 真实数据：T&M 轨至少一个；Applications 轨通常两个以上，且数据可得性
  声明 + 复现包（ASA 强调 reproducibility，建议 Zenodo/Code Ocean DOI）。

## 格式硬要求（核对项）

- [ ] 模板/样式：按官网指南（正文一般双倍行距、页数上限以官网为准）
- [ ] 引用样式：author-year（chicago 系）
- [ ] 补充材料：证明长版/额外模拟/复现包，独立编译可解析
- [ ] 数据与代码可得性声明必写
- [ ] 匿名要求：以官网为准（历史上 JASA 各轨不同）

## 该刊专属改造清单（初稿 → JASA 可投）

- [ ] 贡献列表改造成 (i)(ii)(iii) 且每条挂定理/表号（P03）
- [ ] 证明全部移出正文（正文只留 Proof sketch），appendix 补全引理链
- [ ] 每条假设加 Remark（强弱对比 + 放松讨论）
- [ ] 基准方法补调参说明（同网格 CV），表格加"调参协议"表注
- [ ] 复现包 DOI 与数据可得性声明落位
- [ ] Discussion 扩到"局限→扩展→实践建议"三块，局限对应可做的研究问题
- [ ] 跑 `scripts/style_check.py` 清 AI 味符号与用词
- [ ] 摘要重写：六句结构（P23）+ 200 词内 + 含速率与覆盖率数字
