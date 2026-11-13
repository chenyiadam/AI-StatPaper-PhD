# Changelog

All notable changes to this project are documented in this file.
The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/);
versioning follows [Semantic Versioning](https://semver.org/).

## [Unreleased]

### Planned
- English translations of `docs/` methodology essays and `examples/`
- Number-reconciliation script (paper numbers ↔ experiment output, ±0.01)
- More journal profiles (Bernoulli, EJS, JBES, Biostatistics, …)

## [1.2.0] - 2026-11-13

### Added
- **Full-lifecycle completion (S0 + S8)**: `docs/11` with the venue-calibrated
  theory-check intensity table (L3 line-by-line for AoS/Biometrika → L1 for
  application venues), the editorial-system status decoder, and inquiry
  etiquette
- Prompts P33–P38 (`prompts/08-立项与投稿执行.md` + English version):
  P33 research charter (milestones, data backup, CRediT authorship,
  preregistration decision tree, literature monitoring), P34
  submission-system field plan, P35 preprint strategy (arXiv endorsement),
  P36 status inquiries & nudges (three templates), P37 decision routes
  (revise / reject & resubmit / accept), P38 proofs & post-publication
  (errata template)
- New skill `stat-postsub` (Chinese + English) covering S0 and S8
- Checklist C3-D8: pre-analysis-plan item for confirmatory analyses

### Changed
- Pipeline expanded to nine stages (S0–S8); stat-pipeline, both READMEs,
  and both skill indexes updated accordingly

## [1.1.0] - 2026-11-13

### Added
- **Journal style adaptation system**: `journals/` with 9 venue profiles
  (JASA, Annals of Statistics, Biometrika, JRSS-B, AOAS, Biometrics,
  Statistics in Medicine, JMLR, Chinese core journals) + prompts P28–P32 +
  skill `stat-journal-fit` — reshapes a passing draft into a venue-ready
  submission
- **`scripts/style_check.py`**, the 4th check script: deterministic scan of
  AI-flavor symbols and words — prose em-dashes (numeric-range en-dashes kept),
  30+ flagged words, connector density, "not only…but also", Chinese AI tells
- `templates/cover-letter.md` and `templates/response-letter.tex`
- `templates/project/复现包结构.md` (TIER-4.0-style replication-package layout)
- **Bilingual release**: `README.en.md`, `prompts/en/` (P01–P32),
  `skills-en/` (9 skills), `journals/en/`, `checklists/en/`
- GitHub community files: CODE_OF_CONDUCT, CHANGELOG, CITATION.cff,
  issue/PR templates, CI workflow

### Changed
- Pipeline stage S7 renamed "Journal fit · formatting · submission" with the
  stat-journal-fit seven-step workflow inserted before formatting
- P20/P21 enriched: protected-zone rules (GPT Academic-style), modification
  thresholds, dual back-translation output, AI-flavor word blacklist,
  em-dash/en-dash distinction
- SKILL.md frontmatter aligned with the Agent Skills specification
  (metadata blocks, trigger-style descriptions)

## [1.0.0] - 2026-11-12

### Added
- Seven-stage gated pipeline (question → literature → theory → experiments →
  writing → mock review → submission) with five global principles
- 27 prompts (P01–P27) across six categories
- 8 skills following the Agent Skills specification
- 7 checklists (C1–C7) incl. the 30+-item theory checklist and the
  three-layer citation verification checklist
- 3 check scripts (citation/notation/figure-table), stdlib-only
- Templates: JASA-style LaTeX skeleton, Quarto paper, R/Python simulation
  skeletons, bilingual glossary (60+ terms)
- Worked demo (`examples/`) and methodology docs (`docs/01`–`docs/10`)
