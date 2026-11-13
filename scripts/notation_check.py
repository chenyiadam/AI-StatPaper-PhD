#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
notation_check.py —— LaTeX 论文记号与数学环境一致性检查
==========================================================
功能（对应 checklists/C2-E5 与 docs/08 格式规范）：
  1. 定理环境清单：扫描 theorem/lemma/proposition/corollary/assumption
     的 \newtheorem 定义与文中 \label，报告重复 label。
  2. 交叉引用审计：\cref/\ref 引用的 label 是否都存在；定义后从未被
     引用的定理/假设（审稿人视角：无用的定理要删）。
  3. 记号冲突启发式：检测同一宏被 \newcommand 定义多次；
     检测 TODO/AICHECK/REFCHECK 自检标记是否残留。
  4. "显然"扫描：中文"显然|易得|不难发现"与英文 "obviously|it is easy
     to see|clearly" 出现位置清单——按 C2-C4 逐条裁决或展开。

用法：
  python notation_check.py main.tex appendix.tex supplement.tex
依赖：仅标准库。退出码：发现问题时为 1。
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

COMMENT_RE = re.compile(r"(?<!\\)%.*")

THM_ENVS = ["theorem", "lemma", "proposition", "corollary", "assumption",
            "definition", "remark", "example"]

LABEL_RE = re.compile(r"\\label\{([^}]*)\}")
REF_RE = re.compile(r"\\(?:cref|Cref|ref|eqref)\{([^}]*)\}")
NEWCMD_RE = re.compile(r"\\(?:re)?newcommand\{?\\(\w+)\}?")
NEWTHM_RE = re.compile(r"\\newtheorem\{(\w+)\}")
BEGIN_ENV_RE = re.compile(r"\\begin\{(\w+\*?)\}")
OBVIOUS_RE = re.compile(
    r"(显然|易得|易见|不难发现|obviously|it is easy to see|clearly[, ]|trivially)", re.I
)
TODOTAG_RE = re.compile(r"\\(?:TODO|AICHECK|REFCHECK)\b")


def strip_comments(text: str) -> str:
    return "\n".join(COMMENT_RE.sub("", line) for line in text.splitlines())


def audit(files: list[Path]) -> int:
    issues: list[str] = []
    labels: dict[str, list[str]] = {}
    refs: set[str] = set()
    commands: dict[str, list[str]] = {}
    thm_defined: list[str] = []
    envs_used: list[str] = []
    obvious_hits: list[str] = []
    todo_hits: list[str] = []

    for f in files:
        text = strip_comments(f.read_text(encoding="utf-8", errors="replace"))
        for m in LABEL_RE.finditer(text):
            labels.setdefault(m.group(1), []).append(f.name)
        refs.update(m.group(1) for m in REF_RE.finditer(text))
        for m in NEWCMD_RE.finditer(text):
            commands.setdefault(m.group(1), []).append(f.name)
        for m in NEWTHM_RE.finditer(text):
            thm_defined.append(m.group(1))
        for m in BEGIN_ENV_RE.finditer(text):
            envs_used.append(m.group(1).rstrip("*"))
        for i, line in enumerate(text.splitlines(), 1):
            if OBVIOUS_RE.search(line):
                obvious_hits.append(f"  {f.name}:{i}: {line.strip()[:90]}")
            # 宏定义行本身不算"残留"（TODO/AICHECK 是模板基础设施）
            if TODOTAG_RE.search(line) and r"\newcommand" not in line:
                todo_hits.append(f"  {f.name}:{i}: {line.strip()[:90]}")

    # 1) 重复 label
    dup = {k: v for k, v in labels.items() if len(v) > 1}
    if dup:
        issues.append("[重复 label] 同名 label 出现多次：")
        issues += [f"  - {k} -> {v}" for k, v in dup.items()]

    # 2) 引用不存在的 label
    dangling = sorted(refs - set(labels))
    if dangling:
        issues.append("[悬空引用] \\ref/\\cref 引用了不存在的 label：")
        issues += [f"  - {k}" for k in dangling]

    # 3) 定义后从未引用的定理/假设（提醒：无用的定理删掉或并入 remark）
    thm_labels = {k for k in labels
                  if any(k.startswith(p) for p in
                         ("thm", "lem", "prop", "cor", "asm", "ass", "defn", "def:"))}
    unused = sorted(thm_labels - refs)
    if unused:
        issues.append("[未引用结果] 以下定理/引理/假设从未被引用（删除或说明用途）：")
        issues += [f"  - {k}" for k in unused]

    # 4) 重复宏定义
    dupcmd = {k: v for k, v in commands.items() if len(v) > 1}
    if dupcmd:
        issues.append("[重复宏定义] 同一宏多次 \\newcommand（会覆盖或报错）：")
        issues += [f"  - \\{k} -> {v}" for k, v in dupcmd.items()]

    # 5) 定理环境使用但未定义
    for env in set(envs_used) & set(THM_ENVS):
        if env not in thm_defined:
            issues.append(f"[未定义环境] 使用了 \\begin{{{env}}} 但未 \\newtheorem{{{env}}}")

    # 6) “显然”与自检标记
    if obvious_hits:
        issues.append("[“显然”扫描] 以下位置的“显然/易得/clearly”需逐条展开或替换为引理引用：")
        issues += obvious_hits
    if todo_hits:
        issues.append("[自检标记残留] TODO/AICHECK/REFCHECK 未清零：")
        issues += todo_hits

    print("=" * 62)
    print("记号与数学环境检查报告")
    print("=" * 62)
    print(f"扫描文件：{[f.name for f in files]}")
    print(f"label 总数 {len(labels)}；引用 {len(refs)}；定理环境定义 {sorted(set(thm_defined))}")
    if issues:
        print("\n".join(issues))
        print(f"\n共 {len(issues)} 组提示。逐条裁决后重跑，直到无问题。")
        return 1
    print("全部通过 ✓")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description="LaTeX 记号与数学环境检查")
    ap.add_argument("tex", nargs="+", type=Path)
    args = ap.parse_args()
    missing = [f for f in args.tex if not f.exists()]
    if missing:
        print("文件不存在：", [str(m) for m in missing])
        return 2
    return audit(args.tex)


if __name__ == "__main__":
    sys.exit(main())
