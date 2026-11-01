# Reviewing an Accelerate course: the brief

You review one finished course of the read-along of Forsgren, Humble and Kim,
*Accelerate* (2018), for accuracy against the book and for teaching. The model
is `docs/reviews/enterprise-patterns-domain-logic-review.md` (read its first 80
lines for the shape). Read `docs/accelerate/PLAN.md`,
`docs/accelerate/AUTHORING.md` (it names the text and the tools) and the parts
of `docs/accelerate/kit-report.md` your course's labs use. Never read `site/`;
never read the book file whole; never copy the book's text into the review
beyond the few words needed to locate a passage.

Write ONLY `docs/reviews/accelerate-<course-slug-without-accelerate->-review.md`.
Change nothing else; the course's author applies the fixes. Run no git command
that changes the index or working tree.

## What to check

1. **Gates.** `python3 scripts/preview_subject.py accelerate --course <slug> --out /tmp/claude-0/-home-claude/5c90b399-20f2-5d19-9db3-f3c6934b2289/scratchpad/rev/<slug>` prints OK. `quotes.py` on every quotation (exact, PDF page right, ≤ 40 words opening, ≤ 60 a lesson). `overlap.py <course dir> 8`: every run is a title, a section or capability name, an answer option, or a counted quotation — list any other.
2. **Accuracy.** For every sentence that says what the book found, reports, argues, recommends or measured — every percentage, ratio, year, threshold and named method — read the pages behind it with `book.py`/`page.py` and say whether the book supports it. A finding stated as a cause where the book says correlation or prediction, a figure from the wrong year, a statistic misdefined, a claim credited to the wrong chapter or author (Chapter 16 is the Bells'): each is a MUST-FIX with the location (file:line) and replacement text.
3. **Labs.** Load each lesson in Playwright (`require('playwright')`, `chromium.launch()`, `file://` on the preview's pages), each preset; check the tiles against the prose and worked lines by your own computation; type the exercise in and check it against the quiz `why`. A figure in the prose the lab does not print, or prints differently, is a MUST-FIX. Check at 375 px for sideways scroll.
4. **Teaching.** Every wrong quiz answer: try to argue for it; if you can, it is a MUST-FIX with a replacement. Is the lab's figure actually connected to the chapter's finding, or is it decoration? Does each lesson close on the gap the material clause names (a figure about the stated sample, not a finding, not a cause)? Is the lesson fair where the book names its own limits? Any lesson using the book's tables, figures, survey items or example data as lab data is a MUST-FIX.
5. **Copyright.** No table, figure, survey item or list reproduced beyond names; no close paraphrase of a passage (8-word runs are caught by the scanner; look for 5–7-word near-runs in definitions too).

## Report shape

Sections: Gates; MUST-FIX (numbered, file:line, what is wrong, the book's
position with PDF page, replacement text); SHOULD-FIX; NOTE; and a one-line
verdict. Under 1,500 words. Your final message to the orchestrator: the path
of the review, counts of MUST/SHOULD/NOTE, and the three most important
findings in a sentence each.
