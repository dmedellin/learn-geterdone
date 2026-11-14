# Reviewing a Wealth of Nations course: the brief

You review finished courses of The Wealth of Nations, Read Along, for
accuracy against Smith's text and for teaching, and **you apply the fixes
yourself** (the authors have finished). Read `docs/wealth-of-nations/PLAN.md`
(§0, §A, your courses in §C, §E, §F), `docs/wealth-of-nations/AUTHORING.md`
(it names the text and the tools: `grep_text.py`, `quotes.py`), and the
sections of `docs/wealth-of-nations/kit-report-a.md` / `kit-report-b.md`
your courses' labs use. Never read `site/`; never read the text file whole.

You may edit only your courses' files under `content/wealth_of_nations/`,
your courses' block in `content/spoken/wealth_of_nations.py`, and your review
file `docs/reviews/wealth-of-nations-<course-slug-without-wealth->-review.md`
(one per course). Other reviewers work in the same checkout at the same
time. Run no git command that changes the index or the working tree.

## What to check, and fix

1. **Gates.** `python3 scripts/preview_subject.py wealth_of_nations --course <slug> --out <dir under /tmp/claude-0/-home-claude/799ff4e6-d40c-554f-8670-3d4578ce9497/scratchpad/rev/>`
   prints OK, before and after your fixes. `quotes.py` on the course
   directory: no MISS.
2. **Accuracy against the text.** For every sentence that says what Smith
   says, argues, reports or computes, and every one of his figures, find the
   line and say whether the text supports it. Smith given a verdict the text
   does not contain, a figure misread, a passage credited to the wrong Book or
   chapter, a later writer's view put in Smith's mouth: fix it.
3. **Accuracy about others.** Every claim about another writer (Mandeville,
   Cantillon, Hume, Quesnay, Turgot, Ricardo, Malthus, Say, List, Marx,
   Viner, Rothschild, modern economists and historians), with dates and
   titles. If you are not confident a claim is right, soften it to what you
   are sure of or remove it; a confident wrong attribution is worse than none.
   The authors flagged some as written from memory.
4. **Labs.** For each preset: check the pinned tiles against your own
   arithmetic and against the prose and worked example; a figure in the prose
   the lab does not print, or prints differently, is a defect. Every preset id
   must appear in a body paragraph with its figure. A preset whose tiles a
   reader is told to ignore is a defect: re-configure it so every tile it
   shows means something, or drop it. If a preset changes, re-pin from
   `node scripts/labcheck.js --observe <page>` after checking by hand.
5. **Teaching.** For every wrong quiz answer, try to argue for it; if you can,
   rewrite it. Correct answers should be spread across positions. Each lesson
   closes on what the arithmetic cannot settle. Smith presented at strength,
   critics at strength, no praise of either side in the lesson's own voice.
6. **Prose.** Plain, warm, exact; no slang, no "let's", no filler. Fix
   awkward sentences you meet; do not rewrite good ones.

## Report

One file per course, under 800 words: Gates (before/after), fixes made
(file, what, why, with the text line for accuracy fixes), anything left
undone and why. Your final message: the review paths, counts of fixes, and
the three most important fixes in a sentence each.
