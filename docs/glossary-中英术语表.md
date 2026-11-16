# 统计学核心术语中英对照表（写作与翻译专用）

> 用法：中英互译时随提示词一并贴给 AI（`prompts/P22-中英互译.md`），要求按本表译名统一。
> 约定：estimator=估计量（规则/随机变量），estimate=估计值（实现）——**这两个词混用是中文统计论文第一大硬伤**。

## 1. 基础概念

| 中文 | 英文 | 备注 |
|---|---|---|
| 总体/样本 | population / sample | |
| 参数估计 | parameter estimation | |
| 点估计/区间估计 | point estimation / interval estimation | |
| 估计量/估计值 | estimator / estimate | 见顶部约定 |
| 估计误差 | estimation error | |
| 偏差/方差 | bias / variance | |
| 均方误差 | mean squared error (MSE) | |
| 无偏性 | unbiasedness | |
| 一致性/相合性 | consistency | 中文论文统一用"相合性"（大陆规范）或"一致性"，全文一致即可 |
| 有效性 | efficiency | |
| 充分性 | sufficiency | |
| 渐近性 | asymptotics | |
| 渐近正态 | asymptotic normality | |
| 依概率收敛/几乎必然收敛 | convergence in probability / almost sure convergence | |
| 依分布收敛 | convergence in distribution | |
| 大数定律/中心极限定理 | law of large numbers / central limit theorem | LLN / CLT |
| 收敛速率 | convergence rate | |

## 2. 假设检验与置信推断

| 中文 | 英文 | 备注 |
|---|---|---|
| 原假设/备择假设 | null hypothesis / alternative hypothesis | H₀ / H₁ |
| 显著性水平 | significance level | |
| 第一类错误/第二类错误 | type I error / type II error | |
| 检验功效 | power (of a test) | |
| p 值 | p-value | 斜体 p |
| 置信区间/置信水平 | confidence interval / confidence level | |
| 置信带 | confidence band | |
| 覆盖率 | coverage (probability) | |
| 临界值 | critical value | |
| 拒绝域 | rejection region | |
| 多重检验 | multiple testing | |
| 伪发现率 | false discovery rate (FDR) | Benjamini–Hochberg |
| 家族错误率 | family-wise error rate (FWER) | |

## 3. 回归与高维统计

| 中文 | 英文 | 备注 |
|---|---|---|
| 响应变量/协变量 | response variable / covariates | 自变量=explanatory variable |
| 设计矩阵 | design matrix | |
| 截距项 | intercept | |
| 最小二乘 | least squares | OLS=ordinary least squares |
| 岭回归/套索回归 | ridge regression / lasso | Lasso 全文统一大写或小写 |
| 弹性网 | elastic net | |
| 稀疏性 | sparsity | |
| 活跃集/真值 | active set / ground truth | |
| 支撑集 | support (set) | |
| 变量选择/特征选择 | variable selection / feature selection | 统计口径用 variable selection |
| 预言性质 | oracle property | 统一译"预言性质"或保留 oracle，全文一致 |
| 欠光滑条件 | undersmoothing | |
| 伸缩参数/调谐参数 | tuning parameter | 勿译"参数"造成歧义 |
| 交叉验证 | cross-validation (CV) | |
| 样本外预测 | out-of-sample prediction | |
| 过拟合 | overfitting | |

## 4. 渐近理论与函数型/非参数

| 中文 | 英文 | 备注 |
|---|---|---|
| 维度/样本量 | dimension / sample size | p / n |
| 高维 | high-dimensional | |
| 渐近方差 | asymptotic variance | |
| 三明治方差估计 | sandwich variance estimator | |
| Delta 方法 | delta method | |
| 经验过程 | empirical process | |
| Donsker 类 | Donsker class | |
| 一致收敛 | uniform convergence | |
| 逐点收敛 | pointwise convergence | |
| 核估计/带宽 | kernel estimation / bandwidth | |
| 样条 | spline | |
| 局部多项式 | local polynomial | |
| 最优速率/minimax 速率 | optimal rate / minimax rate | |
| 下界 | lower bound | |
| 正则条件 | regularity conditions | |

## 5. 因果推断

| 中文 | 英文 | 备注 |
|---|---|---|
| 因果效应 | causal effect | |
| 潜在结果 | potential outcomes | |
| 平均处理效应 | average treatment effect (ATE) | |
| 倾向得分 | propensity score | |
| 混杂变量 | confounders | |
| 随机对照试验 | randomized controlled trial (RCT) | |
| 双重差分 | difference-in-differences (DID) | |
| 断点回归 | regression discontinuity design (RDD) | |
| 工具变量 | instrumental variable (IV) | |
| 双重机器学习 | double/debiased machine learning (DML) | |
| 敏感性分析 | sensitivity analysis | |

## 6. 计算与贝叶斯

| 中文 | 英文 | 备注 |
|---|---|---|
| 马尔可夫链蒙特卡洛 | Markov chain Monte Carlo (MCMC) | |
| 先验/后验分布 | prior / posterior distribution | |
| 后验抽样 | posterior sampling | |
| 吉布斯抽样 | Gibbs sampler | |
| 哈密顿蒙特卡洛 | Hamiltonian Monte Carlo (HMC) | |
| 后验预测检验 | posterior predictive check | |
| 收敛诊断 | convergence diagnostics | R̂（Gelman–Rubin） |
| 置信区间（贝叶斯） | credible interval | 勿与 confidence interval 混译 |
| 凸优化 | convex optimization | |
| 梯度下降 | gradient descent | |
| 坐标下降 | coordinate descent | |
| 收敛性 | convergence | |
| 计算复杂度 | computational complexity | |

## 7. 数据与实验

| 中文 | 英文 | 备注 |
|---|---|---|
| 模拟研究 | simulation study | |
| 数据生成过程 | data-generating process (DGP) | |
| 蒙特卡洛标准误 | Monte Carlo standard error | |
| 重复次数 | number of replications | |
| 场景 | scenario | |
| 敏感性分析 | sensitivity analysis | |
| 缺失数据 | missing data | |
| 缺失机制 | missingness mechanism | MCAR/MAR/MNAR |
| 异常值/杠杆点 | outlier / leverage point | |
| 稳健性 | robustness | |
| 协变量偏移 | covariate shift | |
| 复现/可复现性 | replication / reproducibility | 注意 replication 也指"重复抽样" |
