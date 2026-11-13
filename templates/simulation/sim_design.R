# =====================================================================
# 模拟实验骨架（R 版）—— 统计论文模拟研究的可复现骨架
# 配套文档：docs/05-阶段四-实验设计.md；检查清单 checklists/C3-实验检查清单.md
# 用法：Rscript sim_design.R --seed 2026 --rep 500
# 原则：
#   1. 场景网格显式定义（n × p × 信号强度 × 误差分布 × 方法）
#   2. 随机种子固定且写入输出文件名
#   3. 每个方法独立函数，接口统一
#   4. 评价指标一次性算全：误差、模型选择、覆盖率先、区间长度、耗时
#   5. 输出为 tidy 数据框，直接可出表出图
# =====================================================================

suppressPackageStartupMessages({
  library(Matrix)
})

args <- commandArgs(trailingOnly = TRUE)
SEED <- as.integer(ifelse(length(args) >= 2, args[which(args == "--seed") + 1], 2026))
NREP <- as.integer(ifelse(length(args) >= 2, args[which(args == "--rep") + 1], 500))

# ---------------------------------------------------------------
# 1. 场景网格：每个字段都要能映射到论文 Table 1 的一列
# ---------------------------------------------------------------
make_scenarios <- function() {
  expand.grid(
    n = c(200, 500),            # 样本量
    p = c(100, 1000),           # 维度
    signal = c("weak", "strong"), # 信号强度 beta_j* = signal * sqrt(2 log p / n)
    error = c("normal", "t3"),  # 误差分布（重尾稳健性）
    stringsAsFactors = FALSE
  )
}

# ---------------------------------------------------------------
# 2. 数据生成过程（DGP）：与论文 5.1 节的公式逐条对应，编号注释
# ---------------------------------------------------------------
gen_data <- function(n, p, signal, error, seed) {
  set.seed(seed)
  s <- max(3, floor(p / 20))            # 活跃变量数 s
  beta0 <- rep(0, p)
  beta0[1:s] <- signal * sqrt(2 * log(p) / n)
  X <- matrix(rnorm(n * p), n, p)        # DGP-1: 次高斯设计
  eps <- switch(error,
    normal = rnorm(n),
    t3     = rt(n, df = 3) / sqrt(3)     # DGP-2: 重尾误差，标准化到单位方差
  )
  y <- as.numeric(X %*% beta0 + eps)     # DGP-3: 线性模型
  list(X = X, y = y, beta0 = beta0, active = 1:s)
}

# ---------------------------------------------------------------
# 3. 方法接口：每个方法返回统一的 list（est / sel / ci），便于统一评价
#    TODO: 换成你的方法与基准方法
# ---------------------------------------------------------------
fit_method <- function(method, X, y, lambda) {
  n <- nrow(X); p <- ncol(X)
  switch(method,
    lasso = {
      # TODO: glmnet 实现；此处为占位
      est <- rep(0, p)
      sel <- which(est != 0)
      ci  <- cbind(est, est)             # 占位置信区间
      list(est = est, sel = sel, ci = ci)
    },
    ours = {
      # TODO: 本文方法实现（放 methods/ours.R，勿把核心代码塞进模拟脚本）
      stop("替换为本文方法")
    }
  )
}

# ---------------------------------------------------------------
# 4. 评价指标：一次算全，避免事后补实验
# ---------------------------------------------------------------
evaluate <- function(res, truth, active) {
  err  <- sqrt(mean((res$est - truth)^2))            # RMSE
  tpr  <- mean(res$sel %in% active)                  # 真阳率
  fdr  <- mean(!(res$sel %in% active))               # 伪发现率
  ci_len <- mean(res$ci[, 2] - res$ci[, 1])          # 平均区间长度
  ci_cov <- mean(truth[res$sel] >= res$ci[res$sel, 1] &
                 truth[res$sel] <= res$ci[res$sel, 2]) # 覆盖率（仅对被选变量）
  c(RMSE = err, TPR = tpr, FDR = fdr, CI_len = ci_len, CI_cov = ci_cov)
}

# ---------------------------------------------------------------
# 5. 主循环
# ---------------------------------------------------------------
run_all <- function() {
  scenarios <- make_scenarios()
  methods <- c("lasso", "ours")
  out <- list(); k <- 1
  for (sc in seq_len(nrow(scenarios))) {
    for (m in methods) {
      reps <- vector("list", NREP)
      for (r in 1:NREP) {
        seed <- SEED + 1000 * sc + r   # 种子规则化：场景与重复共同决定
        d <- gen_data(scenarios$n[sc], scenarios$p[sc],
                      scenarios$signal[sc], scenarios$error[sc], seed)
        lambda <- sqrt(log(scenarios$p[sc]) / scenarios$n[sc])  # TODO: 交叉验证或理论取值
        fit <- tryCatch(fit_method(m, d$X, d$y, lambda), error = function(e) NULL)
        reps[[r]] <- if (is.null(fit)) NA else evaluate(fit, d$beta0, d$active)
      }
      mat <- do.call(rbind, Filter(is.data.frame, reps))
      agg <- cbind(scenarios[sc, ], method = m,
                   as.data.frame(t(colMeans(mat, na.rm = TRUE))),
                   sd = apply(mat, 2, sd, na.rm = TRUE)[1])
      out[[k]] <- agg; k <- k + 1
      message(sprintf("场景 %d/%d, 方法 %s 完成", sc, nrow(scenarios), m))
    }
  }
  result <- do.call(rbind, out)
  # 输出文件带种子与重复数，天然可追溯
  write.csv(result,
            sprintf("output/sim_seed%d_rep%d_%s.csv", SEED, NREP,
                    format(Sys.Date(), "%Y%m%d")),
            row.names = FALSE)
  invisible(result)
}

system.time(res <- run_all())
print(res)
