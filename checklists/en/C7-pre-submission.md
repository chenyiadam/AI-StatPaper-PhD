<!-- Translated from the Chinese original; the Chinese version remains canonical. -->

# C7 · Pre-Submission Final Checklist (T-minus-7-days countdown)

> Usage: start 7 days before the planned submission date, one group per day. Click submit only when every box
> is ticked.
> Combined use: first run the three simulated reviewers ([P24](../../prompts/06-审稿与投稿.md)) → fix →
> then run this checklist.

## Day −7: Content consistency

- [ ] 1.1 Every number/conclusion in the abstract matches the body (abstracts are the classic thing forgotten
      after revisions)
- [ ] 1.2 The Introduction's (i)(ii)(iii) contributions correspond one-to-one with the body sections and
      theorem numbers, in the same order
- [ ] 1.3 Every "will be proved/shown in Section X" promise in the text has been honored
      (search forthcoming / will show)
- [ ] 1.4 The order of λ, the assumption numbers, and the rate constants agree across the method/simulation/
      appendix trio
- [ ] 1.5 Figure/table numbering continuous and every one cited; appendix references A.x resolve in the main file
- [ ] 1.6 Replication-package links work (a separate anonymized repository prepared for the submission version);
      the README one-command run tested

## Day −6: Run the automated checks

- [ ] 2.1 [`citation_check.py`](../../scripts/citation_check.py) passes (text–bibliography agreement both ways)
- [ ] 2.2 [`notation_check.py`](../../scripts/notation_check.py) passes (notation conflicts/undefined warnings
      at zero, or adjudicated one by one)
- [ ] 2.3 [`fig_table_check.py`](../../scripts/fig_table_check.py) passes (every figure/table cited;
      caption self-containment spot-checked)
- [ ] 2.4 [`style_check.py`](../../scripts/style_check.py) fully processed (AI-flavor symbols and high-frequency
      words: must-fix items at zero, adjudications on record — em-dash asides / blacklist words / connective
      density / Chinese AI phrases)
- [ ] 2.5 LaTeX compiles with zero errors; warnings reviewed (overfull boxes handled one by one)
- [ ] 2.6 Spelling and grammar check (e.g., Writefull/LanguageTool), with proper nouns added to the dictionary
      to prevent false corrections

## Day −5: Closing the simulated-review loop

- [ ] 3.1 The opinions of the three independent reviewer roles (statistical theory / applied methodology /
      presentation standards) collected and de-duplicated
- [ ] 3.2 Every comment classified: must fix / worth fixing / answer in the letter — fixes are fixed,
      explanations drafted into the rebuttal
- [ ] 3.3 "The page the referee is most likely to attack" confirmed: the assumptions section, size calibration,
      the choice of λ, fairness of the SOTA comparison
- [ ] 3.4 The cover letter written: a one-sentence contribution + why this journal fits + a no-dual-submission
      statement

## Day −3: Ethics and compliance

- [ ] 4.1 The AI-use disclosure complete (filled in item by item per the
      [Appendix D template](../../templates/latex/appendix.tex)), compliant with the target journal's latest AI policy
- [ ] 4.2 All citations passed the three-layer [C6](../../checklists/C6-引用核验清单.md) verification, with the
      records on file
- [ ] 4.3 Data licensing and informed consent (for human-subject data); sensitive variables handled compliantly
- [ ] 4.4 Conflict-of-interest statement; funding acknowledgment format correct
- [ ] 4.5 Author list and order confirmed by all authors; ORCID filled in

## Day −1: The submission package

- [ ] 5.1 All files prepared per the submission-system checklist: main / supplement / replication package /
      cover letter / suggested reviewers
- [ ] 5.2 The PDF inspected page by page: fonts embedded, figures clear, no leftover TODO/AICHECK/REFCHECK red
      text (before compiling, global-search \TODO, \AICHECK, \REFCHECK and confirm zero hits)
- [ ] 5.3 Submission-system metadata filled in completely; after uploading, download the receipt PDF and
      inspect it once more
- [ ] 5.4 Archiving: final manuscript + sources + replication package archived by date, saved as a git tag
