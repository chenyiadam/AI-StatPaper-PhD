<!-- Translated from the Chinese canonical version (prompts/08-立项与投稿执行.md). -->
# 08 · Project initiation & submission execution (P33–P38)

> Companions: `docs/11-阶段八-投稿执行与出版跟进.md` (Chinese) ·
> `skills-en/stat-postsub/SKILL.md` · `templates/cover-letter.md`.
> This file completes both ends of the pipeline: **S0 project charter** (P33)
> and **S8 submission execution & post-submission** (P34–P38). The cover letter
> itself lives in `templates/cover-letter.md` (venue version via P32).

---

## P33 · Research project charter (S0)

**When**: before or alongside S1; mandatory before writing for collaborations.
**Input**: draft problem statement + data/compute status + collaborator list.
**Verify**: AI's role is to interrogate your plan, not to make decisions; data
access, compute, and authorship are human confirmations.

```text
You are a research-project management consultant. Interrogate the plan below
for gaps that would delay or kill the paper. Ask questions and produce lists —
do not decide for me.

[Plan draft] {{question in one sentence + expected timeline + data source +
compute + collaborators}}
[Target output] {{venue shortlist + preprint intent}}

Interrogate item by item:
1. Backward-planned milestones: from "target submission month" — theory done /
   experiments done / first draft / mock review / journal adaptation /
   submission; weeks per stage; ≥ 25% total buffer? Which stage slips most
   (usually theory or data access)?
2. Data-availability pre-check: how long does the application take? Ethics
   approval? If it fails, what is the backup dataset (write it into the
   charter NOW, not after failure)?
3. Compute budget: where do the core-hours for the simulation grid come from
   (cross-check the P13 grid)?
4. Authorship agreement (CRediT per person):
   Conceptualization / Methodology / Software / Validation / Formal analysis /
   Investigation / Data curation / Writing – original draft / Writing – review
   & editing / Visualization / Supervision / Funding acquisition.
   Author ORDER is confirmed in writing today; it is not renegotiated at
   submission.
5. Preregistration decision tree (three questions):
   - Does the target venue accept/welcome Registered Reports?
   - Does the real-data analysis need a pre-analysis plan (PAP) fixed BEFORE
     seeing outcomes? If yes: pre-register primary analysis / sensitivity
     analyses / exclusion rules (OSF).
   - Neither → write down explicitly "no preregistration; methodological
     study without confirmatory testing", for the referee who will ask.
6. Literature monitoring plan: arXiv keyword subscriptions, Google Scholar
   Alerts, a monthly "has anyone scooped us" sweep (owner + cadence).
7. Risk register: each risk → trigger signal → contingency plan (plan B) →
   owner.
```

---

## P34 · Submission-system execution checklist (S8)

**When**: submission day. AI produces the venue's field-filling plan; you
execute field by field.
**Verify**: technical (formatting) rejections are a large share of desk
rejections — this checklist exists to prevent exactly that.

```text
You are a submission-system consultant. From the venue's author guidelines,
produce a field-by-field filling plan.

[System] {{Editorial Manager / ScholarOne / other + screenshots or field list}}
[Files] main / anonymized main / supplement / replication package / cover
letter / reporting checklist (if applicable)
[Metadata] title/abstract/keywords/authors & affiliations/funding/acknowledgments

Output:
1. File pre-check per file: naming per system rules; format correct (PDF /
   Word / TeX source); anonymized-version leak scan done (acknowledgments /
   funding / self-citations / repo links / file-metadata author names);
   figure resolution & format; within size limits?
2. Mandatory-field mapping (what to paste in each):
   - Data availability statement (cite the replication-package DOI)
   - Funding statement (full grant names and format)
   - Conflict of interest (every author)
   - AI-use disclosure (one line, pointing to Appendix D)
   - Ethics/IRB, trial registration number (if applicable)
   - CRediT contributions (per the P33 charter)
3. Common technical veto points: word/page limits, abstract length, keyword
   count, reference style, figure/table caps, supplement size.
4. Upload sequence: which file first (wrong order can make the system pick the
   wrong main document); after submission, download the receipt PDF and
   inspect page by page; record the manuscript ID and submission date (needed
   for status inquiries).
5. Within 48 hours: confirm the status moved to "with editor"/"under review";
   if not, one status-confirmation email (P36 template 1).
```

---

## P35 · Preprint strategy (arXiv and siblings)

**When**: decided before submission; executed after each revision round.
**Verify**: venue preprint policies differ (most statistics venues allow; a few
have embargoes) — check per venue.

```text
You are a scholarly-publishing strategy consultant. Give me the preprint
decision and execution list.

[Paper] {{title / area / target venue}}
[Author situation] {{first arXiv submission? (determines the endorsement issue)}}

Output:
1. Policy check: the venue's preprint policy (allowed / embargo / version
   rules) — with the verification actions (official site + cross-check recent
   venue papers' arXiv records).
2. Endorsement gate: first-time arXiv submitters need an endorsement in the
   category — how to get one (a collaborator or a scholar who has posted in
   the category; start weeks early; a backup category).
3. Version discipline:
   - posting before submission: cite the arXiv ID in a footnote (referees can
     reach the replication package)
   - after each revision: sync the arXiv version; the changelog states changes
   - after acceptance: update to the accepted version, link the DOI.
4. License interplay: arXiv license choice vs. the venue's OA policy (default
   to arXiv's non-exclusive license unless the venue says otherwise).
5. The "why NOT to post" list (double-blind concerns, collaborator agreements)
   — record the decision in the P33 charter instead of agonizing in submission
   week.
```

---

## P36 · Status inquiries & nudges (etiquette + three templates)

**When**: past the venue's stated timeline. **Principles: polite, infrequent, factual.**
**Verify**: nudges do not speed up refereeing; they only rescue forgotten
manuscripts. More than one inquiry per month backfires.

```text
You are a publishing-etiquette consultant. First give me the decision rules,
then a template per situation.

[Situation] {{manuscript ID / submission date / current system status / the
venue's stated average timeline}}

Decision rules (answer first):
1. Timing: desk decisions usually 2–6 weeks; external review 3–6 months (the
   venue's stated numbers rule). Inquire at stated-time + 4 weeks; ≥ 6 weeks
   between two inquiries on the same manuscript.
2. Addressee: managing editor / editorial office — never individual referees.
3. Content: facts only (ID, dates, elapsed time); no hints that the editor is
   negligent.

Three situation templates (English, each ≤ 120 words):
- Template 1 · timeline inquiry: subject "Status inquiry — Manuscript ID {{}}";
  body = identity in one line + facts (submitted X months ago, status Y) +
  request (any timeline information would be appreciated) + thanks.
- Template 2 · stalled review: status "Required reviews completed" for Z weeks —
  request appointing a substitute referee or moving to decision; tone stays
  "for your consideration".
- Template 3 · revision pending long: revised X months ago, no status change —
  ask whether anything further is needed from the authors.
Self-check per letter: any accusatory tone? Any speculation beyond facts?
Delete it.
```

---

## P37 · Decision response, three routes (accept / revise / reject)

**When**: the day the decision arrives. Cool off 24 hours first (especially
for rejections).

```text
You are a publishing-workflow consultant. Give me the execution path per
decision type.

[Decision] {{Accept / Minor / Major / Reject(-with-resubmit) / Desk reject}}
[Comments] {{paste or summarize}}
[Constraints] {{revision deadline / other manuscripts in flight / time budget}}

A. Accept → proofs stage via P38.
B. Revise (minor/major) →
   1. All comments into P25 aggregation → P26 response letter → revision
      (S5/S6 disciplines apply; a "minor" revision does NOT exempt you from
      style_check and number reconciliation).
   2. Timeline: acknowledge within 1 week; if an extension is genuinely
      needed, one template (≤ 100 words): additional experiments under way,
      may we have until date X — ask once for 30–60 days; never repeatedly.
   3. Literature freshness: rerun the search (P33's monitoring plan) before
      revising; cite recent work where warranted — never token-cite.
C. Reject (incl. desk reject) →
   1. After the 24-hour cooldown, triage the comments: technical errors
      (must fix) / scope mismatch (just change venue) / misreadings
      (prevent via cover letter).
   2. Appeal assessment: only when a factual error is provable (e.g., a lemma
      the referee claims is missing actually exists); appeals rarely succeed —
      the default route is fix-and-resubmit elsewhere.
   3. Re-submission decision: re-select via journals/ profiles (absorb ALL
      comments first; resubmitting the unchanged version to a sibling journal
      burns your reputation); sync the preprint.
   4. Mindset clause: top-venue rejections are part of the process; treat the
      reviews as a free stat-reviewer ensemble.
```

---

## P38 · Proofs & post-publication

**When**: from acceptance to one month after publication.

```text
You are a post-production consultant. Checklists and templates per stage.

[Stage] {{Proofs / published online / error found after publication}}

A. Proofs discipline:
   1. Fix typographical errors only (typos/format/figure quality); content
      changes require the errata process — far more costly than keeping a
      wart.
   2. Answer author queries one by one: "AQ1: author response…" (brief,
      precise; do not rewrite sentences).
   3. Check: author name spellings and order, affiliations, grant numbers,
      corresponding-author mark, abstract & keywords, figure/table numbering
      and quality, reference pages, ORCID.
   4. Deadline: usually 48–72 hours; missing it delays publication.
B. Copyright & OA decisions: license choice (CC BY vs. NC), OA fees and green
   archiving policy (which version may go to the institutional repo / arXiv),
   page/color charges (if any).
C. First 30 days after publication:
   1. Promotion checklist (restrained version): group homepage / one-paragraph
      institutional news; social posts state only proven conclusions + the
      replication link; do not mass-email PDFs (send the DOI link).
   2. Monitoring: Google Scholar citation alerts; on finding a substantive
      error → contact the editor immediately for an errata/correction
      (template: the wrong statement + the right statement + impact assessment
      + updated replication package).
   3. Feed new checklist items distilled from the refereeing process back into
      this project (CONTRIBUTING).
```
