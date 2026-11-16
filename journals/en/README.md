<!-- Translated from the Chinese original; the Chinese version remains canonical. -->

# Journal Style Profiles (From first draft to submission-ready for the target journal)

> Purpose: the "right look" of the same methodological statistics paper differs completely
> between JASA and Biometrika. This directory provides **style profiles** for leading and top
> journals (positioning, structural conventions, presentation of theory, hard formatting
> requirements, and journal-specific adaptation checklists), to be used together with
> [`prompts/07-期刊风格适配.md`](../../prompts/07-期刊风格适配.md) (P28–P32) and
> [`skills/stat-journal-fit/SKILL.md`](../../skills/stat-journal-fit/SKILL.md)
> to reshape a first draft into a submission-ready manuscript for the target journal.

## ⚠️ Nature of these profiles

These profiles summarize **long-standing, stable conventions and community consensus**
(what gets published, how papers are organized, where theorems go); they are **not** a
verbatim transcription of the official submission guidelines. Page limits, citation-style
details, anonymity policies and the like do change — **before submitting you must follow
the journal's latest official Author Guidelines** (the adaptation checklists include a
verification item for exactly this). Wherever a profile conflicts with the official
website, the website prevails; PRs correcting these profiles are welcome.

## Profiles

| Profile | Journal | One-line positioning |
|---|---|---|
| [JASA.md](JASA.md) | Journal of the American Statistical Association | ASA flagship; dual Theory & Methods and Applications tracks |
| [Annals-of-Statistics.md](Annals-of-Statistics.md) | Annals of Statistics | IMS flagship; pure theory |
| [Biometrika.md](Biometrika.md) | Biometrika | Compact methodology; extremely high theory density |
| [JRSS-B.md](JRSS-B.md) | JRSS Series B | Methodology + substantive applications |
| [AOAS.md](AOAS.md) | Annals of Applied Statistics | IMS flagship for applications |
| [Biometrics.md](Biometrics.md) | Biometrics | Biostatistical methodology + medical applications |
| [Statistics-in-Medicine.md](Statistics-in-Medicine.md) | Statistics in Medicine | Medical statistics applications |
| [JMLR.md](JMLR.md) | JMLR | Machine learning theory/methods (at the statistics interface) |
| [Chinese-Core-Journals.md](Chinese-Core-Journals.md) | 应用概率统计 / 数理统计与管理 / 统计研究, among others | Chinese core journals in statistics |

## The general adaptation workflow (seven steps; details in prompts/07)

```
Journal selection → style profiling (P28) → structural re-arrangement (P29) → restyling (P30)
→ format and citation migration (P31) → journal-compliance final check (P32) → submission package
```

| Step | Input | Output | Quality gate |
|---|---|---|---|
| 1 Journal selection | Contribution type + journal profiles | Target journal + backup journal + rationale | The profile's "publishes / does not publish" lists match item by item |
| 2 Style profiling | 2–3 papers in the same direction from the target journal | Style rule card (sentence patterns / density / presentation conventions) | Rules are actionable (one can rewrite against them) |
| 3 Structural re-arrangement | First draft + the journal's structural conventions | Section migration plan + re-arranged draft | The contribution–section–theorem mapping never breaks |
| 4 Restyling | Re-arranged draft + rule card + P20 protocol | Journal-styled manuscript | Paragraph-level three-column output, adjudicated paragraph by paragraph |
| 5 Format migration | Styled manuscript + the journal's format requirements | Compilable submission version | Template / citation style / figures and tables fully migrated |
| 6 Compliance final check | Submission version + the profile's adaptation checklist | Zero-blocker checklist | C8 three passes + C7 + every item of the profile checklist passes |
| 7 Submission package | Previous step | All files + cover letter | Use [`templates/cover-letter.md`](../../templates/cover-letter.md) |

## Before and after: what "restyled for the journal" means

**Before (an AI-flavored draft — phrasing no journal would accept):**

> Our novel framework, which seamlessly integrates robust estimation with
> debiased inference, not only achieves optimal rates but also paves the way
> for practitioners — a crucial step toward reliable high-dimensional analysis.

**After (JASA methodology-paper style):**

> We propose a robust debiased estimator for high-dimensional regression.
> Under Assumption 1 it attains the minimax rate $\sqrt{s\log p/n}$ and
> supports valid confidence intervals (Theorem 2); in simulations the empirical
> coverage ranged from 94.2% to 95.7% across all scenarios (Table 2).

What changed: the AI tells — novel / seamlessly / not only…but also / em-dash asides — are deleted;
every claim is tied to a theorem or table number; conclusions carry concrete numbers; sentences are
short, active, and checkable.

## Relationship to the other components

- This directory is the **data** (journal profiles); [`skills/stat-journal-fit`](../../skills/stat-journal-fit/SKILL.md)
  is the **logic** (orchestration); [prompts/07](../../prompts/07-期刊风格适配.md) is the **ammunition**
  (the prompts). The architecture follows ARS/Polaris's "skill + resource" separation.
- Rewriting still goes through the polishing and de-AI-flavor protocols of
  [P20/P21](../../prompts/05-论文撰写.md) (three-column output, revision thresholds, protected zones);
  this directory only answers "in which direction to revise".
- When undecided about the target journal, run [P28](../../prompts/07-期刊风格适配.md) profiling on two or
  three candidates, compare the rule cards side by side, and only then decide.
