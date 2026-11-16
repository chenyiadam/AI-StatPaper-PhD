#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
fig_table_check.py —— 图表引用与 caption 完整性检查
=====================================================
功能（对应 checklists/C3-C / C5-C/D）：
  1. 每个图/表环境都有 \label 且被正文 \cref/\ref 引用。
  2. caption 存在且长度下限（自含性启发式：< 40 字符视为“caption 不自含”）。
  3. 启发式数字一致性抽查：正文中出现的 "Figure X"/"Table X" 手写编号
     （非 \cref）时告警——手写编号改稿易错位。
  4. booktabs 纪律：\hline 与 \toprule/\midrule 混用告警；
     检测表格中的竖线 "|"（统计三线表禁用）。

用法：
  python fig_table_check.py main.tex [appendix.tex ...]
依赖：仅标准库。
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

COMMENT_RE = re.compile(r"(?<!\\)%.*")


def strip_comments(text: str) -> str:
    return "\n".join(COMMENT_RE.sub("", line) for line in text.splitlines())


def main() -> int:
    ap = argparse.ArgumentParser(description="图表引用与 caption 检查")
    ap.add_argument("tex", nargs="+", type=Path)
    args = ap.parse_args()

    labels: dict[str, list[str]] = {}
    refs: set[str] = set()
    issues: list[str] = []

    for f in args.tex:
        text = strip_comments(f.read_text(encoding="utf-8", errors="replace"))
        lines = text.splitlines()

        # 图/表环境
        for env in ("figure", "figure*", "table", "table*"):
            pattern = re.compile(
                r"\\begin\{" + env + r"\}(.*?)\\end\{" + env + r"\}", re.S
            )
            for i, m in enumerate(pattern.finditer(text), 1):
                block = m.group(1)
                lab = re.search(r"\\label\{([^}]*)\}", block)
                cap = re.search(r"\\caption\{?(.{0,400})", block)
                where = f"{f.name} {env}#{i}"
                if not lab:
                    issues.append(f"[无label] {where} 缺少 \\label")
                else:
                    labels[lab.group(1)] = [where]
                if not cap or not cap.group(1).strip():
                    issues.append(f"[无caption] {where}")
                elif len(cap.group(1)) < 40:
                    issues.append(
                        f"[caption偏短] {where}（自含性不足，caption 应不看正文可懂）: "
                        f"{cap.group(1)[:60]!r}"
                    )
                # 三线表纪律
                if env.startswith("table"):
                    if "\\toprule" not in block and "\\hline" in block:
                        issues.append(f"[三线表] {where}: 用 \\hline 而非 \\toprule/\\midrule")
                    for ln, line in enumerate(block.splitlines(), 1):
                        if "&" in line and re.search(r"\|\s*&|&\s*[^&]*\|", line):
                            issues.append(f"[竖线] {where} 第{ln}行含竖线分隔（三线表禁用）")

        # 引用收集 + 手写编号告警
        for i, line in enumerate(lines, 1):
            refs.update(m.group(1) for m in re.finditer(r"\\(?:cref|Cref|ref)\{([^}]*)\}", line))
            if re.search(r"(?:Figure|Table|Fig\.)\s~?\d", line) and "\\cref" not in line \
                    and "\\ref" not in line and "caption" not in line:
                issues.append(f"[手写编号] {f.name}:{i}: 用 \\cref 代替手写 Figure/Table 编号 -> {line.strip()[:70]}")

    unused = sorted(set(labels) - refs)
    if unused:
        issues.append("[未引用] 以下图/表从未被正文引用：")
        issues += [f"  - {k} ({labels[k]})" for k in unused]

    print("=" * 62)
    print("图表检查报告")
    print("=" * 62)
    print(f"扫描文件：{[f.name for f in args.tex]}；图表 label 数：{len(labels)}")
    if issues:
        print("\n".join(issues))
        return 1
    print("全部通过 ✓")
    return 0


if __name__ == "__main__":
    sys.exit(main())
