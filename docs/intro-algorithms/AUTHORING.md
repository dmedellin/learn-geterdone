# Authoring an Introduction to Algorithms course: the brief every author works from

The hand-off for writing one course of the read-along of Cormen, Leiserson,
Rivest and Stein, *Introduction to Algorithms*, 3rd ed. (MIT Press, 2009). The
design authority is `docs/intro-algorithms/PLAN.md`; where this file and the
plan differ, the plan wins, and you say so in your report. The Subject is built
the way Code Complete and Enterprise Application Patterns were:
`docs/code-complete/AUTHORING.md` sections "The loop for each lesson", "What
every lesson must do", "Voice, in short" and "Lessons from Capital and
Phenomenology" apply in full (read CLRS for McConnell, and the kit named in
§C for cckit).

## Read first, in this order

1. `AGENTS.md` §0, §7, §8 (**never read `site/`**, never open
   `release/contract*.json`), and `content/AGENTS.md` (math a voice can read).
2. `docs/intro-algorithms/PLAN.md` in full (it is short).
3. For a lab on an existing kit: the kit module's docstring under
   `scripts/mathpath/labs/` and the matching Algorithms lesson's `lab` cfg in
   `content/algorithms/` (PLAN §C names it). Copy the cfg's SHAPE, write your
   own instance, label and panel text. For `itakit`:
   `docs/intro-algorithms/kit-report.md` (wait for it if absent; it is being
   written while you start).
4. One finished course as the shape reference:
   `content/code_complete/c2_high_quality_code/__init__.py` and `part_a.py`.
   Same fields, ranges and enforcement (`scripts/preview_subject.py`
   EXACT/RANGES: 3 concepts, 3 mistakes, 4–5 steps, 3–4 quiz, 3–8 key lines of
   at most 46 columns, 7–18 body blocks).

## The text

Private extraction of the operator's copy, outside the repository:
`/tmp/claude-0/-home-claude/17954386-cf49-5ad8-8658-74439f803e6b/scratchpad/book/clrs.txt` (one form feed per PDF page; printed page p = PDF page p + 21).
Helpers in `/tmp/claude-0/-home-claude/17954386-cf49-5ad8-8658-74439f803e6b/scratchpad/tools/`:
`python3 book.py '<regex>' [-C n]` (prints printed page),
`python3 page.py N [M]` (printed pages N..M),
`python3 quotes.py FILE` (lines `tag|printedpage|quote` → OK/LOOSE/MISS),
`python3 overlap.py <dir> 8` (every run of ≥ 8 words shared with the book).
Read the sections behind every claim before you write "the authors show";
never read the file whole.

Copyright rules are PLAN §E: one opening quotation ≤ 40 words, ≤ 60 words of
quotation a lesson, exact, with `# printed p. N` beside the dict; never the
book's pseudocode, figures, tables, example data or exercises; cite by chapter
and section in prose. Never copy any stretch of the text into the repository,
the project files or a report.

## Where you write

- `content/intro_algorithms/cN_<name>/__init__.py` (the COURSE dict,
  replacing `COURSE = None`), `part_a.py`, and `part_b.py` past five lessons.
  The course `how_to` carries the attribution: a read-along of Cormen,
  Leiserson, Rivest and Stein, *Introduction to Algorithms*, 3rd edition (MIT
  Press, 2009), with instances written for these lessons.
- **Course 1's author only** also completes `PATH` in
  `content/intro_algorithms/__init__.py` (tagline, description, key,
  sequence_intro, why_order, prerequisites, footer_lead) from PLAN §A, mirroring
  `content/enterprise_patterns/__init__.py` field for field, with 8 courses and
  61 lessons (fix the numbers if the final count differs).
- `content/spoken/intro_algorithms.py`: spoken forms the read-out cannot
  settle. Others write to it at the same time: re-read it just before each
  edit, add only a block headed `# <Your course title>`, never touch another.
- Nothing else. Do not touch `scripts/`, `tests/`, `site/`, other courses or
  the kits. If a kit cannot show something, write the lesson with what it can
  show and list the gap in your report.
- Do not commit or push, and run no git command that changes the index or the
  working tree; other authors share this checkout.

## The loop

Render your course only:
`python3 scripts/preview_subject.py intro_algorithms --course <course-slug> --out <dir>`
with `<dir>` a new folder under `/tmp/claude-0/-home-claude/17954386-cf49-5ad8-8658-74439f803e6b/scratchpad/preview/`.
Gated kits (`build_paths.KITS_WITH_EXPECTATIONS`) need an `expect` on every
preset: write `expect: {}` first, run
`node scripts/labcheck.js --observe <dir>/site/<course>/<lesson>/index.html`,
and pin each tile string only after checking it against your own count by
hand. Ungated kits (`sortkit`, `heap`, `seqkit`, `number`, `simplex`,
`duality`) take presets as their Algorithms lessons do. Open each lesson once
in Playwright (`require('playwright')`, `chromium.launch()`), load each
preset, try the exercise. Re-run `preview_subject.py` until it prints OK; run
`/usr/bin/python3 scripts/speechcheck.py` and fix every unspoken run. Run
`quotes.py` on every quotation and `overlap.py` on your course directory
until every run it prints is a title, a procedure name, a counted quotation or
standard mathematical phrasing. Try to argue for every wrong quiz answer; if
you can, rewrite it.

If the package fails to import because another course is mid-edit, wait a
minute and retry.

## Report

End with a short report (under 400 words): lessons written; every §C deviation
and why; any kit gap; renderer or read-out problems; each quotation with its
`quotes.py` result; `overlap.py` final state; the preview command's final
output line; spoken forms added.
