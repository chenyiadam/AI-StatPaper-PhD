#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
style_check.py —— AI 味符号与用词机械扫描（第四个检查脚本）
=============================================================
对应：prompts/05 P21（去 AI 味）、checklists/C4-A、journals/ 改造清单。
原则（与 Polaris 一致）：确定性代码做重活——符号与高频词扫描交给脚本，
语义层裁决（是否真的 AI 腔）留给 P21 与人工。

检查规则：

【英文符号】
  R1  em-dash（--- 或 —）出现在正文句子中 → AI 高频特征，清除
      （改从句/逗号/括号，见 P21 工序 1）
  R2  带空格的 "-- "（如 "text -- text"）→ 同上
  R3  en-dash（– 或 --）仅当两侧都是数字/页码时保留（1990--2000、
      267--288 是统计论文规范用法）；其余位置的 en-dash 报告

【英文用词】（词边界匹配，不区分大小写）
  R4  AI 高频词黑名单（delve/leverage/pivotal/underscore/...）
  R5  AI 高频短语（"It is worth noting"/"plays a vital role"/...）
  R6  连接词密度：Moreover/Furthermore/Additionally 单文件 > 3 次报告
  R7  "not only ... but also" 排比结构

【中文符号与用词】
  R8  全角破折号"——"：报告全部出现位置（中文论文允许少量使用，
      但 AI 生成稿密度异常；逐条裁决，建议改冒号/括号/逗号）
  R9  中文 AI 高频短语（"值得注意的是"/"综上所述"/"不难发现"等）
  R10 商业腔词（"赋能"/"抓手"/"闭环"）——学术文禁用

用法：
  python style_check.py main.tex [appendix.tex ...] [--md paper.md]
依赖：仅标准库。退出码：0 通过 / 1 发现问题 / 2 用法错误。
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

# ---------------- 词表（与 prompts/05 P21 保持同步） ----------------

BANNED_WORDS_EN = [
    "delve", "leverage", "pivotal", "crucial", "comprehensive",
    "utilize", "utilise", "underscore", "unveil", "foster",
    "tapestry", "realm", "testament", "transcend", "traverse",
    "garner", "ameliorate", "accentuate", "intricate", "meticulous",
    "seamless", "seamlessly", "holistic", "paramount",
]

BANNED_PHRASES_EN = [
    "it is worth noting", "plays a vital role", "plays a crucial role",
    "in recent years", "first and foremost", "paves the way",
    "sheds light on", "a testament to", "in the realm of",
    "navigating the", "ever-evolving", "cutting-edge",
]

CONNECTORS = ["Moreover", "Furthermore", "Additionally", "Notably"]

BANNED_PHRASES_ZH = [
    "值得注意的是", "综上所述", "不难发现", "由此可见",
    "赋能", "抓手", "闭环", "深耕", "量质齐升", "多点开花",
]

EM_DASH_RE = re.compile(r"---|—")
SPACED_DDASH_RE = re.compile(r" -- ")
ENDASH_RE = re.compile(r"--|–")
EN_DASH_OK_RE = re.compile(r"\d\s*(?:--|–)\s*\d")       # 1990--2000 / 267–288
PAGE_RANGE_RE = re.compile(r"(?:pages?|pp\.)\s*\d+\s*(?:--|–)\s*\d+", re.I)
NOT_ONLY_RE = re.compile(r"\bnot only\b[^.?!]{0,200}?\bbut also\b", re.I | re.S)
ZH_DASH_RE = re.compile(r"——")


def strip_comments_tex(text: str) -> str:
    return "\n".join(line.split("%", 1)[0] if not line.lstrip().startswith("%")
                     else "" for line in text.splitlines())


def scan_text(name: str, text: str) -> list[str]:
    issues: list[str] = []

    def loc(i: int) -> str:
        return f"{name}:{text.count(chr(10), 0, i) + 1}"

    # R1/R2 em-dash 与带空格 --（全角"——"由 R8 专项报告，此处剔除避免重复）
    text_en = ZH_DASH_RE.sub("", text)
    for m in EM_DASH_RE.finditer(text_en):
        issues.append(f"[R1 em-dash] {loc(m.start())}: …{text_en[max(0, m.start()-30):m.end()+30].strip()}…")
    for m in SPACED_DDASH_RE.finditer(text_en):
        issues.append(f"[R2 空格--] {loc(m.start())}: …{text_en[max(0, m.start()-30):m.end()+30].strip()}…")

    # R3 en-dash：剔除合法数字区间与 em-dash 后报告剩余（避免把 --- 误报为 --）
    tmp = EM_DASH_RE.sub("", text)
    tmp = EN_DASH_OK_RE.sub("", tmp)
    tmp = PAGE_RANGE_RE.sub("", tmp)
    for m in ENDASH_RE.finditer(tmp):
        issues.append(f"[R3 en-dash存疑] {loc(m.start())}: …{tmp[max(0, m.start()-30):m.end()+30].strip()}…"
                      "（非数字区间，确认是否应为逗号/连字符）")

    # R4 英文黑名单词（词边界）
    for w in BANNED_WORDS_EN:
        for m in re.finditer(rf"\b{w}\b", text, re.I):
            issues.append(f"[R4 黑名单词] {loc(m.start())}: {m.group(0)}")

    # R5 英文黑名单短语
    for p in BANNED_PHRASES_EN:
        for m in re.finditer(re.escape(p), text, re.I):
            issues.append(f"[R5 黑名单短语] {loc(m.start())}: {p}")

    # R6 连接词密度
    for c in CONNECTORS:
        n = len(re.findall(rf"\b{c}\b", text))
        if n >= 3:
            issues.append(f"[R6 连接词密度] {name}: {c} 出现 {n} 次（≥3，删减后靠逻辑衔接）")

    # R7 not only ... but also
    for m in NOT_ONLY_RE.finditer(text):
        issues.append(f"[R7 排比结构] {loc(m.start())}: …{m.group(0)[:60]}…")

    # R8 中文全角破折号
    for m in ZH_DASH_RE.finditer(text):
        issues.append(f"[R8 中文破折号] {loc(m.start())}: …{text[max(0, m.start()-20):m.end()+20].strip()}…")

    # R9/R10 中文短语
    for p in BANNED_PHRASES_ZH:
        for m in re.finditer(re.escape(p), text):
            issues.append(f"[R9 中文AI短语] {loc(m.start())}: {p}")

    return issues


def read_text_compat(f: Path) -> str:
    """读文件：优先 utf-8，失败回落 gbk（Windows 常见编码）。"""
    raw = f.read_bytes()
    try:
        return raw.decode("utf-8")
    except UnicodeDecodeError:
        return raw.decode("gbk", errors="replace")


def main() -> int:
    ap = argparse.ArgumentParser(description="AI 味符号与用词扫描")
    ap.add_argument("tex", nargs="*", type=Path, help="LaTeX 文件（自动去注释）")
    ap.add_argument("--md", nargs="*", type=Path, default=[], help="Markdown 文件（不去注释）")
    args = ap.parse_args()
    files = [(f, True) for f in args.tex] + [(f, False) for f in args.md]
    files = [(f, s) for f, s in files if f.exists()]
    if not files:
        print("用法：python style_check.py main.tex [appendix.tex ...] [--md x.md]")
        return 2

    issues: list[str] = []
    for f, is_tex in files:
        text = read_text_compat(f)
        if is_tex:
            text = strip_comments_tex(text)
        issues.extend(scan_text(f.name, text))

    print("=" * 62)
    print("AI 味符号与用词扫描报告")
    print("=" * 62)
    print(f"扫描：{[f.name for f, _ in files]}；问题条目 {len(issues)}")
    if issues:
        print("\n".join(issues))
        print("\n处理原则：R1/R2/R7 必改；R4/R5 逐词裁决（确属本义可保留并说明）；")
        print("R3 区分数字区间（保留）与连接用法（改写）；R8 逐条裁决密度；")
        print("语义层复查交给 prompts/05 P21。")
        return 1
    print("全部通过 ✓（符号与高频词层面未发现 AI 味）")
    return 0


if __name__ == "__main__":
    sys.exit(main())
