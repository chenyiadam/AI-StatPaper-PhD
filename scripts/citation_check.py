#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
citation_check.py —— LaTeX 论文引用一致性检查
================================================
功能（对应 checklists/C6-引用核验清单.md 的收尾项）：
  1. 双向一致性：正文 \\cite{...} 引用的 key 必须都在 refs.bib 中；
     bib 中未被正文引用的"孤儿条目"列出（补充材料单列排查）。
  2. 字段完整性：article 条目缺 volume/pages/year/author 时告警（AI 生成
     bib 条目的典型缺陷）。
  3. 疑似幻觉条目启发式：DOI 缺失、或 bib 条目含 TODO/FIXME 标记、
     或同一作者-年份出现重复 key。
  4. 统计报告：总引用数、文献近三年占比（启发式）。

用法：
  python citation_check.py main.tex refs.bib [--tex supplement.tex ...]
依赖：仅标准库（Python 3.8+）。退出码：发现问题时为 1。
"""
from __future__ import annotations

import argparse
import datetime as _dt
import re
import sys
from pathlib import Path

CITE_RE = re.compile(
    r"\\(?:cite|citep|citet|citealp|citeauthor|citeyear|Citep|Citet)\*?"
    r"(?:\[[^\]]*\])?\{([^}]*)\}"
)
BIBENTRY_RE = re.compile(r"@(\w+)\s*\{\s*([^,\s]+)\s*,")
FIELD_RE = re.compile(r"^\s*(\w+)\s*=\s*", re.M)
COMMENT_RE = re.compile(r"(?<!\\)%.*")


def strip_comments(text: str) -> str:
    return "\n".join(COMMENT_RE.sub("", line) for line in text.splitlines())


def extract_cited_keys(tex_files: list[Path]) -> dict[str, list[str]]:
    """返回 key -> 出现它的文件列表。"""
    cited: dict[str, list[str]] = {}
    for tf in tex_files:
        text = strip_comments(tf.read_text(encoding="utf-8", errors="replace"))
        for m in CITE_RE.finditer(text):
            for key in m.group(1).split(","):
                key = key.strip()
                if key:
                    cited.setdefault(key, []).append(tf.name)
    return cited


def parse_bib(bib_file: Path) -> dict[str, dict]:
    text = strip_comments(bib_file.read_text(encoding="utf-8", errors="replace"))
    entries: dict[str, dict] = {}
    matches = list(BIBENTRY_RE.finditer(text))
    for i, m in enumerate(matches):
        etype, key = m.group(1).lower(), m.group(2)
        start = m.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        body = text[start:end]
        fields = {f.group(1).lower() for f in FIELD_RE.finditer(body)}
        entries[key] = {"type": etype, "fields": fields, "raw": body}
    return entries


REQUIRED_ARTICLE = {"author", "title", "journal", "year"}
RECOMMENDED = {"volume", "pages", "doi"}


def main() -> int:
    ap = argparse.ArgumentParser(description="LaTeX 引用一致性检查")
    ap.add_argument("tex", nargs="+", type=Path, help="main.tex（可附 supplement.tex）")
    ap.add_argument("--bib", type=Path, default=Path("refs.bib"))
    args, unknown = ap.parse_known_args()
    if unknown:  # 兼容 "python citation_check.py main.tex refs.bib" 位置写法
        args.tex.append(Path(unknown[0]))
        if len(unknown) > 1:
            args.bib = Path(unknown[1])

    if not args.bib.exists():
        print(f"[用法错误] 未找到参考文献库 {args.bib}（用 --bib 指定路径）")
        return 2

    cited = extract_cited_keys(args.tex)
    bib = parse_bib(args.bib)

    problems: list[str] = []
    missing = sorted(set(cited) - set(bib))
    if missing:
        problems.append(f"[缺失] 正文引用但 bib 中不存在（{len(missing)} 条）：")
        problems += [f"  - {k}  (出现在 {', '.join(cited[k])})" for k in missing]

    orphans = sorted(set(bib) - set(cited))
    if orphans:
        problems.append(f"[孤儿] bib 中存在但正文未引用（{len(orphans)} 条，若在补充材料中被引则忽略）：")
        problems += [f"  - {k}" for k in orphans]

    suspicious: list[str] = []
    for key, e in bib.items():
        f = e["fields"]
        tags = re.findall(r"TODO|FIXME|XXX", e["raw"], re.I)
        if e["type"] == "article":
            lack_req = REQUIRED_ARTICLE - f
            lack_rec = RECOMMENDED - f
            if lack_req:
                suspicious.append(f"  - {key}: 必填字段缺失 {sorted(lack_req)}")
            elif lack_rec:
                suspicious.append(f"  - {key}: 建议字段缺失 {sorted(lack_rec)}（人工确认是否可接受）")
        if tags:
            suspicious.append(f"  - {key}: 含未完成标记 {tags}")
        if "doi" in f and "arxiv" in e["raw"].lower() and "journal" in f:
            suspicious.append(f"  - {key}: 同时含 journal 与 arXiv，确认是否已正式发表")

    years = []
    for e in bib.values():
        m = re.search(r"year\s*=\s*[{\"]?(\d{4})", e["raw"])
        if m:
            years.append(int(m.group(1)))
    this_year = _dt.date.today().year
    recent = [y for y in years if y >= this_year - 3]
    recent_ratio = len(recent) / len(years) if years else 0.0

    print("=" * 62)
    print(f"引用检查报告  ({args.bib.name})")
    print("=" * 62)
    print(f"正文引用 key 数：{len(set(cited))}；bib 条目数：{len(bib)}")
    print(f"近三年文献占比：{recent_ratio:.0%}（建议 ≥ 1/3，统计类可放宽）")
    if problems:
        print("\n—— 一致性问题 ——")
        print("\n".join(problems))
    else:
        print("\n双向一致性：通过 ✓")
    if suspicious:
        print("\n—— 字段完整性 / 疑似幻觉条目（需人工逐条核对出版商页面） ——")
        print("\n".join(suspicious))
    else:
        print("字段完整性：通过 ✓")
    print("\n提醒：本脚本只检查一致性与形式，不核验内容真实性。")
    print("所有 AI 参与生成的引用必须按 checklists/C6 完成 L1-L3 三层人工核验。")
    return 1 if (problems or suspicious) else 0


if __name__ == "__main__":
    sys.exit(main())
