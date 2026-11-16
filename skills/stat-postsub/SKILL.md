---
name: stat-postsub
description: 投稿执行与出版跟进 skill。use when 用户要执行投稿系统提交、决定预印本策略（arXiv endorsement）、询问稿件状态或催稿、处理修改/拒稿/录用决策、管理校样与版权 OA、处理发表后事宜（宣传/勘误）——即阶段 S0 立项（P33）与 S8（P34–P38）的全部任务。
metadata:
  version: "1.0"
  related_skills: [stat-pipeline, stat-journal-fit, stat-reviewer]
---

# stat-postsub · 投稿执行与出版跟进

## 硬性纪律

1. **只讲事实、低频礼貌**：所有编辑通信 ≤ 120 词、只含编号/日期/状态等事实，
   同稿两次询问间隔 ≥ 6 周，永远发给编辑部而非审稿人。
2. **校样不动内容**：proof 阶段只改错排；内容改动走 errata 程序。
3. **承诺对应真实文件**：投稿系统里填的数据声明/AI 披露/CRediT 必须与
   实际文件一致（P33 章程与 C7 记录为准）。
4. **拒稿冷静期**：收到拒稿 24 小时内不做任何提交动作。

## 工作流（对应 P33–P38，见 `prompts/08-立项与投稿执行.md`）

### A. S0 立项（P33，写作之前）
研究章程七问：里程碑倒排（≥25% 缓冲）→ 数据可得性预检（含备选）→
算力预算 → 作者分工（CRediT 逐人 + 顺序书面确认）→ 预注册决策树
（Registered Reports / 预分析计划 / 书面化的不预注册理由）→ 文献监控计划 →
风险登记册。

### B. 投稿执行（P34–P35，投稿日）
1. P34 逐字段方案：文件预检（匿名泄漏/格式/大小）→ 强制字段映射
   （数据声明/基金/COI/AI 披露/CRediT）→ 技术性否决点自查 → 上传顺序 →
   receipt 目检 → **记录投稿编号与日期**。
2. P35 预印本：政策核对 → endorsement 路径 → 版本同步纪律 → license 联动。
3. 48 小时内确认状态流转，未流转发一封状态确认（P36 模板 1）。

### C. 等待与催稿（P36）
状态解码表与询问时机见 `docs/11-阶段八-投稿执行与出版跟进.md` 8.3 节；
三情形英文模板在 P36。产出每次通信的存档（project/ai_logs/ 同级建
project/correspondence/）。

### D. 决策响应（P37）
- 修改：P25 聚合 → P26 回复信 → 修改稿走 stat-writing/stat-format-lint
  全纪律；延期申请一次到位；**每轮修改前文献保鲜检索**。
- 拒稿：冷静期 → 意见分诊 → 申诉评估（默认不申诉）→ journals/ 重新选刊 →
  **转投前按新刊重新校准理论检查档位**（docs/11 8.6 节校准表）。
- 录用：进 E。

### E. 校样与发表后（P38）
校样清单（只改错排、AQ 逐条、48–72h）→ 版权/OA/license 决策 →
上线后 30 天（克制宣传/引用监控/errata 模板）→ 把审稿暴露的新问题
写回 `checklists/`（CONTRIBUTING）。

## 状态快速解码（细节见 docs/11 8.3）

`Submitted→With Editor`（初筛 2–6 周）→ `Under Review`（外审 3–6 个月，
以期刊自述为准）→ `Required Reviews Completed`（待决策 2–8 周）→
`Decision in Process`（1–4 周）。超时询问：自述周期 + 4 周。

## 相关文件

`prompts/08-立项与投稿执行.md`（P33–P38）·
`docs/11-阶段八-投稿执行与出版跟进.md`（校准表/解码表/礼仪）·
`templates/cover-letter.md` · `templates/response-letter.tex` ·
`checklists/C7-投稿前终检清单.md` · `journals/`（转投选刊）
