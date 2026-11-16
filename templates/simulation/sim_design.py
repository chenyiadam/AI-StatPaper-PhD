# =====================================================================
# 模拟实验骨架（Python 版）—— 与 R 版等价的 numpy/scipy 实现
# 用法: python sim_design.py --seed 2026 --rep 500
# 统计论文实验纪律（对应 checklists/C3）:
#   - 场景网格显式、DGP 与论文公式一一对应并注释
#   - 种子规则化；结果 CSV 带种子与日期
#   - 指标一次算全: RMSE / TPR / FDR / 区间长度 / 覆盖率 / 耗时
#   - 核心方法放 methods/ours.py，模拟脚本只做调度
# =====================================================================
from __future__ import annotations

import argparse
import time
from dataclasses import dataclass
from itertools import product
from pathlib import Path

import numpy as np
import pandas as pd


@dataclass
class Scenario:
    n: int
    p: int
    signal: str
    error: str


def make_scenarios() -> list[Scenario]:
    return [
        Scenario(n=n, p=p, signal=sig, error=err)
        for n, p, sig, err in product(
            [200, 500], [100, 1000], ["weak", "strong"], ["normal", "t3"]
        )
    ]


def gen_data(sc: Scenario, seed: int):
    """DGP 与论文 5.1 节公式对应：线性模型 + 次高斯设计 + 重尾误差选项。"""
    rng = np.random.default_rng(seed)
    s = max(3, sc.p // 20)
    beta0 = np.zeros(sc.p)
    beta0[:s] = (1.0 if sc.signal == "strong" else 0.5) * np.sqrt(
        2 * np.log(sc.p) / sc.n
    )
    X = rng.standard_normal((sc.n, sc.p))
    if sc.error == "normal":
        eps = rng.standard_normal(sc.n)
    else:  # t3, 标准化到单位方差
        eps = rng.standard_t(3, sc.n) / np.sqrt(3 / 1.5)
    y = X @ beta0 + eps
    return X, y, beta0, np.arange(s)


def fit_method(method: str, X, y, lam) -> dict:
    """统一接口：返回估计、选中集合、置信区间。TODO 替换为真实实现。"""
    p = X.shape[1]
    if method == "lasso":
        # TODO: 接入 sklearn.linear_model.Lasso 或 cvxpy
        est = np.zeros(p)
        sel = np.where(est != 0)[0]
        ci = np.column_stack([est, est])
    elif method == "ours":
        raise NotImplementedError("替换为本文方法（from methods.ours import fit）")
    else:
        raise ValueError(method)
    return {"est": est, "sel": sel, "ci": ci}


def evaluate(res: dict, beta0: np.ndarray, active: np.ndarray) -> dict:
    err = float(np.sqrt(np.mean((res["est"] - beta0) ** 2)))
    sel = res["sel"]
    tpr = float(np.mean(np.isin(sel, active))) if len(sel) else 0.0
    fdr = float(np.mean(~np.isin(sel, active))) if len(sel) else 0.0
    lo, hi = res["ci"][:, 0], res["ci"][:, 1]
    ci_len = float(np.mean(hi - lo))
    sel_arr = np.asarray(sel, dtype=int)
    cov = float(np.mean((beta0[sel_arr] >= lo[sel_arr]) & (beta0[sel_arr] <= hi[sel_arr]))) if len(sel) else np.nan
    return {"RMSE": err, "TPR": tpr, "FDR": fdr, "CI_len": ci_len, "CI_cov": cov}


def run(seed: int, nrep: int) -> pd.DataFrame:
    rows = []
    for i, sc in enumerate(make_scenarios(), start=1):
        for method in ["lasso", "ours"]:
            reps = []
            for r in range(nrep):
                s = seed + 1000 * i + r          # 种子规则化
                X, y, beta0, active = gen_data(sc, s)
                lam = np.sqrt(np.log(sc.p) / sc.n)
                t0 = time.perf_counter()
                res = fit_method(method, X, y, lam)
                elapsed = time.perf_counter() - t0
                row = evaluate(res, beta0, active)
                row["time_s"] = elapsed
                reps.append(row)
            agg = pd.DataFrame(reps).mean(numeric_only=True)
            agg |= {n: getattr(sc, n) for n in ["n", "p", "signal", "error"]}
            agg["method"] = method
            rows.append(agg)
            print(f"scenario {i} method={method} done")
    return pd.DataFrame(rows)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--seed", type=int, default=2026)
    ap.add_argument("--rep", type=int, default=500)
    a = ap.parse_args()
    out = Path("output")
    out.mkdir(exist_ok=True)
    df = run(a.seed, a.rep)
    path = out / f"sim_seed{a.seed}_rep{a.rep}.csv"
    df.to_csv(path, index=False)
    print(df)
    print(f"saved -> {path}")
