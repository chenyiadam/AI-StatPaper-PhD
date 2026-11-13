# JMLR · Journal of Machine Learning Research

> 机器学习理论/方法旗舰（统计与 ML 交叉论文的常见去向）。档案为惯例性总结，投稿前以官网为准。

## 定位与偏好

**发什么**：机器学习的理论与方法——学习理论、优化、高维统计与
ML 交叉（如高维推断、非参数方法、因果+ML）、有理论保证的新算法。
统计方法论文若算法与学习视角突出，JMLR 是合法去向。

**不发什么**：无理论支撑的纯应用/基准刷分、领域窄且无一般性方法
贡献的论文。

## 结构惯例

- 篇幅宽松（JMLR 无严格页数上限，但审稿人讨厌冗余）；附录可以很长。
- 惯例骨架：Introduction（含 contributions 列表）→ Related Work
  （常为独立节且要求**全面**——JMLR 极重视相关工作覆盖度）→
  Problem Setup → Method → Theory → Experiments → Conclusion。
- Experiments 常含标准 benchmark 数据集（UCI/合成 + 公开数据），
  计算效率与可扩展性是常规考核项。
- 代码开源几乎是隐性要求（官方有 reproducibility 强调）。

## 语言与语气

- 引用样式为 JMLR 自有 bst（编号制！与统计刊不同）。
- ML 话语体系：算法复杂度、可扩展性、benchmark 对比、消融实验
  （ablation）是标配词汇；统计论文迁移时注意术语对齐
  （如"协变量"→"特征 features"的双语并用策略）。
- 贡献列表 (i)(ii)(iii) 与统计刊同构。

## 理论呈现

- 定理呈现类似统计（assumptions→theorem→proof 在 appendix）；
  但审稿人构成不同：ML 理论审稿人对 concentration inequalities、
  generalization bounds 话语更熟悉，对经典统计渐近（Donsker 等）
  要写得更自足。
- 收敛速率用 ML 惯用记法（excess risk、sample complexity）桥接。

## 实验（模拟 + 数据）期望

- 模拟 + 真实数据 + **计算可扩展性实验**（运行时间 vs n/p 曲线）；
  消融实验（去掉正则项/换损失）是 ML 审稿人的固定问题。
- 基准必须含 ML 社区公认的强方法（不只是统计刊那几个）。

## 格式硬要求（核对项）

- [ ] 模板：JMLR 官方 jmlr LaTeX 样式
- [ ] 引用样式：jmlr bst（编号制）
- [ ] 匿名：以官网为准（历史上 JMLR 为非盲，作者信息保留——务必核对）
- [ ] 补充材料/代码仓库链接

## 该刊专属改造清单（初稿 → JMLR 可投）

- [ ] Related Work 独立成节并扩容（ML 文献全覆盖，含近年会议论文）
- [ ] 术语桥接表：统计记号 ↔ ML 记法（excess risk/sample complexity）
- [ ] 补计算可扩展性实验（时间-规模曲线图）
- [ ] 补消融实验（组件贡献拆解）
- [ ] 代码仓库 + 复现脚本（JMLR 读者会跑）
- [ ] 引用样式切 jmlr bst；定理环境对齐模板
- [ ] Experiments 补 ML 基准方法对比
