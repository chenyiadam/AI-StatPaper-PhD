#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
presubmit_check.py —— 定稿投稿前一键检查（编排器 + C8 新增检查）
====================================================================
对应 checklists/C8-定稿逐项检查清单.md。两层：
  第一层·编排：依次运行四个既有脚本并汇总退出码
    citation_check / notation_check / fig_table_check / style_check
  第二层·新增确定性检查（C8 的 [自动] 项）：
    N1  摘要词数（A4）与关键词数量
    N2  三级标题使用提示（A5）
    N3  \item 滥用：单条目列表 / 连续列表环境 / 一节内列表环境 > 3（A10）
    N4  正文直引号与 scare-quotes（A10；LaTeX 应用 `` '' 或改写）
    N5  元说明/承诺句扫描（D3：In this section we will / As mentioned above /
        we will show / 本节将 / 如前所述 等，报告位置与密度）
    N6  定理环境数量分布（C4：corollary>theorem 等异常信号）
    N7  正文-附录对应初查（C2：正文定理标签未在附录出现 → 清单供人工裁决）
    N8  表格列内小数位一致性（A9：同一列小数位数混合）

用法：
  python presubmit_check.py main.tex [appendix.tex supplement.tex] [--bib refs.bib]
依赖：仅标准库；同目录下需有四个既有脚本。
退出码：0 全通过 / 1 有必改项（N4/N7/摘要词数越界或任一子脚本失败）/
        2 用法错误。其余检查为提示项（逐条人工裁决，见 C8 三遍法）。
"""
from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

SCRIPTS_DIR = Path(__file__).resolve().parent

# ---------------- 通用工具 ----------------

def read_text(f: Path) -> str:
    raw = f.read_bytes()
    try:
        return raw.decode("utf-8")
    except UnicodeDecodeError:
        return raw.decode("gbk", errors="replace")


def strip_comments(text: str) -> str:
    return "\n".join(line.split("%", 1)[0] if not line.lstrip().startswith("%")
                     else "" for line in text.splitlines())


# ---------------- 第一层：编排四个既有脚本 ----------------

def run_subscripts(tex_files: list[Path], bib: Path) -> list[tuple[str, int]]:
    jobs = [
        ("citation_check", [str(tex_files[0])] + [str(p) for p in tex_files[1:2]]
         + ["--bib", str(bib)]),
        ("notation_check", [str(p) for p in tex_files]),
        ("fig_table_check", [str(p) for p in tex_files]),
        ("style_check", [str(p) for p in tex_files]),
    ]
    results = []
    for name, args in jobs:
        print("\n" + "=" * 62)
        print(f">>> 子脚本 {name}.py")
        print("=" * 62)
        try:
            r = subprocess.run([sys.executable, str(SCRIPTS_DIR / f"{name}.py")] + args)
            results.append((name, r.returncode))
        except FileNotFoundError as e:
            print(f"[错误] 无法运行 {name}.py: {e}")
            results.append((name, 2))
    return results


# ---------------- 第二层：C8 新增检查 ----------------

ABSTRACT_RE = re.compile(r"\\begin\{abstract\}(.*?)\\end\{abstract\}", re.S)
KEYWORDS_RE = re.compile(r"\\begin\{keywords?\}(.*?)\\end\{keywords?\}|"
                         r"(?:Keywords?|关键词)\s*[:：]\s*([^\n]{3,})")
CMD_RE = re.compile(r"\\[a-zA-Z]+\*?(\[[^\]]*\])?")
LIST_BEGIN_RE = re.compile(r"\\begin\{(itemize|enumerate|description)\}")
ITEM_RE = re.compile(r"\\item\b")
SECTION_RE = re.compile(r"\\(sub)*section\{")
QUOTE_RE = re.compile(r'"([^"\n]{1,80})"')
SCARE_RE = re.compile(r"so-called|所谓的")
META_PATTERNS = [
    r"In this (?:section|subsection|chapter)[^.]{0,60}?we (?:will|shall)",
    r"[Ww]e will (?:show|prove|discuss|describe|demonstrate|present)",
    r"[Aa]s (?:mentioned|discussed|noted) (?:above|earlier|before)",
    r"It should be noted that",
    r"[Tt]he following (?:section|chapter) (?:will|describes)",
    r"本节将", r"下面将", r"如前所述", r"值得指出的是", r"需要说明的是",
]
THM_BEGIN_RE = re.compile(r"\\begin\{(theorem|lemma|proposition|corollary|remark)\}")
THM_LABEL_RE = re.compile(r"\\label\{(thm|lem|prop|cor|asm)[^}]*\}")
NUM_RE = re.compile(r"\d+\.(\d+)")


def n1_abstract_keywords(text: str) -> list[str]:
    out = []
    m = ABSTRACT_RE.search(text)
    if m:
        words = len(CMD_RE.sub(" ", m.group(1)).split())
        out.append(f"[N1 摘要] 词数 = {words}（统计刊常见区间 150–250；以目标刊为准）")
        if words > 0 and (words < 100 or words > 300):
            out.append("      ⚠ 越出 100–300 宽松区间——[必改] 核对目标刊词数要求")
            out.append("\x00BLOCK")
    else:
        out.append("[N1 摘要] 未找到 abstract 环境（若有标题页摘要请人工计数）")
    kw = KEYWORDS_RE.search(text)
    if kw:
        blob = kw.group(1) or kw.group(2) or ""
        n = max(blob.count(",") + blob.count("；") + blob.count(";") + blob.count("、"), 0) + 1
        out.append(f"[N1 关键词] 约 {n} 个（常 3–6；排序规则按刊：字母序/重要性序）")
    return out


def n2_headings(text: str, fname: str) -> list[str]:
    n3 = len(re.findall(r"\\subsubsection\{", text))
    return [f"[N2 三级标题] {fname}: \\subsubsection 出现 {n3} 次——"
            "核对目标刊是否允许三级标题（部分刊仅两级）"] if n3 else []


def n3_item_abuse(text: str, fname: str) -> list[str]:
    out = []
    lines = text.splitlines()
    # 单条目列表 & 连续列表
    begins = [(i, m.group(1)) for i, ln in enumerate(lines)
              for m in [LIST_BEGIN_RE.search(ln)] if m]
    ends = {i for i, ln in enumerate(lines) if "\\end{itemize" in ln
            or "\\end{enumerate" in ln or "\\end{description" in ln}
    for i, _ in begins:
        # 找对应 end
        j = next((k for k in range(i + 1, len(lines)) if k in ends), None)
        if j is None:
            continue
        n_items = sum(1 for ln in lines[i:j + 1] if ITEM_RE.search(ln))
        if n_items == 1:
            out.append(f"[N3 单条目列表] {fname}:{i + 1} —— 只有一个 \\item，改写为普通段落")
        # 连续列表环境（之间无正文段落）
        nxt = [k for k, _ in begins if k > j]
        if nxt and nxt[0] - j <= 2:
            out.append(f"[N3 连续列表] {fname}:{i + 1} 与 {fname}:{nxt[0] + 1} "
                       "之间无正文——合并或插入过渡句")
    # 每节列表环境密度
    section_starts = [i for i, ln in enumerate(lines) if SECTION_RE.search(ln)]
    bounds = section_starts + [len(lines)]
    for a, b in zip(bounds, bounds[1:]):
        cnt = sum(1 for i, _ in begins if a <= i < b)
        if cnt > 3:
            out.append(f"[N3 列表密度] {fname}:{a + 1} 起的 section 含 {cnt} 个列表环境"
                       "（>3，检查是否列表化滥用）")
    return out


def n4_quotes(text: str, fname: str) -> list[str]:
    out = []
    for i, ln in enumerate(text.splitlines(), 1):
        for m in QUOTE_RE.finditer(ln):
            out.append(f"[N4 直引号] {fname}:{i}: \"{m.group(1)[:50]}\" —— "
                       "LaTeX 应用 ``...'' 或改写；若为比喻/强调用法，直接删引号")
        if SCARE_RE.search(ln):
            out.append(f"[N4 scare-quotes] {fname}:{i}: 含 so-called —— "
                       "确认必要，多数应删")
    return out


def n5_meta(text: str, fname: str) -> list[str]:
    out = []
    hits = 0
    for pat in META_PATTERNS:
        for m in re.finditer(pat, text):
            hits += 1
            line_no = text.count("\n", 0, m.start()) + 1
            out.append(f"[N5 元说明] {fname}:{line_no}: {m.group(0)[:60]} —— "
                       "节首一句 roadmap 可留；逐段预告/回头指涉改写为直接陈述")
    if hits > 3:
        out.append("      ⚠ 元说明密度 > 3，[必改] 逐条清除后再复跑")
        out.append("\x00BLOCK")
    return out


def n6_theorem_usage(files: list[tuple[str, str]]) -> list[str]:
    counts = {}
    for fname, text in files:
        for m in THM_BEGIN_RE.finditer(text):
            counts[m.group(1)] = counts.get(m.group(1), 0) + 1
    if not counts:
        return ["[N6 定理环境] 未检出定理类环境（若为纯应用文可忽略）"]
    out = ["[N6 定理环境分布] " + ", ".join(f"{k}: {v}" for k, v in sorted(counts.items()))]
    t = counts.get("theorem", 0)
    c = counts.get("corollary", 0)
    l = counts.get("lemma", 0)
    if c > t and t > 0:
        out.append(f"      ⚠ corollary({c}) 多于 theorem({t})——检查环境是否用错"
                   "（主结果应标 theorem）")
    if t == 0 and (c or l):
        out.append("      ⚠ 无 theorem 但有 lemma/corollary——主结果环境标错？")
    if l > 4 * max(t, 1):
        out.append(f"      ⚠ lemma({l}) 偏多——检查是否把主结果降格成了引理")
    return out


def n7_appendix_map(files: list[tuple[str, str]]) -> list[str]:
    main_names = [f for f, t in files if "appendix" not in f and "supplement" not in f]
    aux_names = [f for f, t in files if "appendix" in f or "supplement" in f]
    if not aux_names:
        return ["[N7 附录对应] 未提供 appendix/supplement 文件，跳过（纯正文论文可无附录）"]
    aux_text = "\n".join(t for f, t in files if f in aux_names)
    main_text = "\n".join(t for f, t in files if f in main_names)
    labels = set(m.group(0) for m in re.finditer(
        r"\\label\{(?:thm|lem|prop|cor)[^}]*\}", main_text))
    missing = []
    for lab in sorted(labels):
        key = lab[len("\\label{"):-1]
        if key not in aux_text:
            missing.append(key)
    out = [f"[N7 正文-附录对应] 主文定理类标签 {len(labels)} 个；附录未出现 {len(missing)} 个"]
    for k in missing:
        out.append(f"      - {k}（若正文内已证/属陈述性结果则合法，逐条人工确认）")
    if missing:
        out.append("      ⚠ 存在附录无对应的主文结果——[必改项阈值由人工裁决："
                   "确认每条的证明位置]")
        out.append("\x00BLOCK")
    return out


def n8_table_decimals(files: list[tuple[str, str]]) -> list[str]:
    out = []
    tab_re = re.compile(r"\\begin\{table\*?\}(.*?)\\end\{table\*?\}", re.S)
    for fname, text in files:
        for ti, m in enumerate(tab_re.finditer(text), 1):
            rows = [ln for ln in m.group(1).splitlines()
                    if ln.count("&") >= 1 and not ln.strip().startswith("%")]
            ncols = max((ln.count("&") + 1 for ln in rows), default=0)
            for col in range(ncols):
                places = set()
                for ln in rows:
                    cells = ln.split("&")
                    if col < len(cells):
                        for nm in NUM_RE.findall(cells[col]):
                            places.add(len(nm))
                if len(places) > 1:
                    out.append(f"[N8 小数位] {fname} 表#{ti} 第{col + 1}列 "
                               f"小数位混合 {sorted(places)} —— 统一到固定位数"
                               "（three-digits rule）")
    return out


def run_new_checks(tex_files: list[Path]) -> tuple[list[str], bool]:
    files = [(p.name, strip_comments(read_text(p))) for p in tex_files]
    main_files = [(f, t) for f, t in files
                  if "appendix" not in f and "supplement" not in f]
    findings: list[str] = []
    blocked = False
    for f, t in main_files:
        findings += n1_abstract_keywords(t)
        findings += n2_headings(t, f)
        findings += n3_item_abuse(t, f)
        findings += n4_quotes(t, f)
        findings += n5_meta(t, f)
    findings += n6_theorem_usage(files)
    findings += n7_appendix_map(files)
    findings += n8_table_decimals(files)
    if "\x00BLOCK" in findings:
        blocked = True
        findings = [x for x in findings if x != "\x00BLOCK"]
    return findings, blocked


# ---------------- main ----------------

def main() -> int:
    ap = argparse.ArgumentParser(description="定稿投稿前一键检查（C8 编排器）")
    ap.add_argument("tex", nargs="+", type=Path)
    ap.add_argument("--bib", type=Path, default=Path("refs.bib"))
    args = ap.parse_args()
    tex_files = [p for p in args.tex if p.exists()]
    if not tex_files:
        print("用法错误：未找到任何 .tex 文件")
        return 2

    sub_results = run_subscripts(tex_files, args.bib)

    print("\n" + "=" * 62)
    print("C8 新增检查（对应 checklists/C8-定稿逐项检查清单.md）")
    print("=" * 62)
    findings, blocked = run_new_checks(tex_files)
    print("\n".join(findings) if findings else "新增检查：无发现 ✓")

    print("\n" + "=" * 62)
    print("总汇")
    print("=" * 62)
    sub_fail = [n for n, rc in sub_results if rc not in (0,)]
    for n, rc in sub_results:
        print(f"  {n}.py: {'通过' if rc == 0 else f'退出码 {rc}（有发现，见上）'}")
    ok = not sub_fail and not blocked and not findings
    print(f"结论：{'全部通过 ✓' if ok else '存在待裁决/待修项 —— 按 C8 三遍法处理'}")
    print("修正在提示词里做：格式→P31 · 语言→P20/P21 · 引文→P07 · 理论→P10")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
