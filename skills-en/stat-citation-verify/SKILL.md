---
name: stat-citation-verify
description: Citation verification. use when the user wants to add citations, verify AI-provided references, check refs.bib, generate BibTeX entries, or confirm whether a reference supports a claim — any task touching reference authenticity or support.
metadata:
  version: "1.0"
  related_skills: [stat-pipeline, stat-research]
---

# stat-citation-verify · Three-layer citation verification

## Hard disciplines (why this skill exists)

1. **Default stance: every AI-provided citation does not exist until human
   verification passes.** General-purpose models hallucinate 78–90% of
   citations in open literature QA (OpenScholar, Nature).
2. **Unverifiable ≠ invalid**: API failures and timeouts output "unverified",
   never "fabricated" (Polaris rule) — verdicts downgrade loudly, never
   silently pass.
3. **No second-hand citation**: L3 requires opening the original PDF;
   abstract-only checks count as "partially verified".
4. **Never delete a flagged citation**: problems go to the author for
   adjudication (re-cite / delete / replace); AI does not act on its own.

## The three layers (per citation)

### L1 · Existence (does this paper exist?)
1. DOI resolves: `https://doi.org/<DOI>` lands on that title; or Crossref:
   `https://api.crossref.org/works/<DOI>`.
2. Title hits on Google Scholar / Semantic Scholar.
3. Authors are real: they have other work in this area (AI often stitches two
   real authors into one fake reference).
4. Volume/issue/pages match the publisher page verbatim; arXiv IDs
   well-formed.
5. **Red flags**: a title suspiciously tailored to your claim; a journal–topic
   mismatch; Chinese-language references with no CNKI match (AI hallucinates
   Chinese metadata at high rates).

### L2 · Field consistency (is the bib entry right?)
1. BibTeX entries come from the publisher's official export (Scholar export
   cross-checked with the publisher page) — **AI-generated entries are never
   pasted in directly**.
2. Author list complete and ordered; online-first vs. final year distinguished;
   journal abbreviations consistent; arXiv preprints upgraded to the published
   version when one exists.
3. Mechanical layer: `scripts/citation_check.py` (bidirectional text–bib
   consistency, required fields, TODO residue, journal+arXiv coexistence).

### L3 · Content support (does it support your claim?)
1. Open the PDF; go to where the claimed evidence should live (theorem?
   experiment? discussion?).
2. Three failure modes:
   - **condition-dropping**: the original is conditional; your citation dropped
     the condition (most common in statistics)
   - **strength mismatch**: a numerical-experiment finding cited as a theorem
   - **misattribution**: similar conclusion, different paper.
3. Placement correctness: method provenance / theorem provenance / data source
   each cited where they belong — **wrong theorem provenance is a referee's
   favorite offense**.
4. Better-source check: if an earlier or more authoritative original exists,
   cite that.

## Output format (a verification card per citation)

```
Citation: Author (Year) Title. Journal vol(issue):pages. DOI
L1 existence: pass/suspect (evidence: doi.org result, Scholar hit)
L2 fields: pass/fixed (per-field verdicts; corrected entry attached)
L3 support: supports / partial / needs rewording / cannot judge
   (evidence location in the original: section/page/paragraph)
Author action: use as-is / reword the citing sentence / replace / re-verify
Log: date · actions · PDF path
```

## Batch mode (whole-paper sweep)

1. `scripts/citation_check.py main.tex refs.bib` for form issues.
2. A card per citation (L1/L2 batchable; L3 one by one, by hand).
3. Summary: total / L1 pass rate / L2 fixes / L3 distribution / pending items.
4. Close with `checklists/en/C6-citation-verification.md` (density, recency
   mix, records archived).

## Related files

`prompts/en/02` (P07) · `checklists/en/C6-citation-verification.md` ·
`scripts/citation_check.py` · `docs/03` (Chinese)
