# Authoring an Accelerate course: the brief every author works from

The hand-off for writing one course of the read-along of Forsgren, Humble and
Kim, *Accelerate* (IT Revolution, 2018). The design authority is
`docs/accelerate/PLAN.md`; where this file and the plan differ, the plan
wins, and you say so in your report. The Subject is built the way
Domain-Driven Design was: `docs/code-complete/AUTHORING.md` sections "The loop
for each lesson", "What every lesson must do", "Voice, in short" and "Lessons
from Capital and Phenomenology" apply in full (read Forsgren, Humble and Kim
for McConnell, and `acckit` for cckit).

## Read first, in this order

1. `AGENTS.md` §0, §7, §8 (**never read `site/`**, never open
   `release/contract*.json`), and `content/AGENTS.md`.
2. `docs/accelerate/PLAN.md` in full.
3. `docs/enterprise-patterns/PLAN.md` §E.3 (quoting), §E.4 (the author's
   checklist) and §F (voice) — search for the headings, read those sections
   only. This Subject adopts them.
4. For a lab: `docs/accelerate/kit-report.md` (every cfg field, input format,
   tile id, with examples). It is written while you draft; if it is absent,
   draft the prose first (phase A below).
5. One finished course as the shape reference:
   `content/domain_driven_design/c2_building_blocks/__init__.py` and its
   `part_a.py`. Same fields, ranges and enforcement
   (`scripts/preview_subject.py` EXACT/RANGES: 3 concepts, 3 mistakes, 4–5
   steps, 3–4 quiz, 3–8 key lines of at most 46 columns, 7–18 body blocks).

## The text

Private extraction of the operator's copy, outside the repository:
`/tmp/claude-0/-home-claude/5c90b399-20f2-5d19-9db3-f3c6934b2289/scratchpad/book/acc.txt`
(one form feed per PDF page; the footer numbers equal PDF pages). Helpers in
`/tmp/claude-0/-home-claude/5c90b399-20f2-5d19-9db3-f3c6934b2289/scratchpad/tools/` (run them from that directory):

- `python3 book.py '<regex>' [-C n]` — search; prints the PDF page.
- `python3 page.py N [M]` — print PDF pages N..M.
- `python3 quotes.py FILE` — lines `tag|pdfpage|quote` → OK / LOOSE / MISS, with word counts.
- `python3 overlap.py <dir> 8` — every run of ≥ 8 words your course's string literals share with the book.

Read the sections behind every claim before you write "the authors found";
read each of your lessons' sections in full (PLAN §C gives PDF pages; they
are approximate, check the outline with `book.py`). Never read the file
whole. Every number the book reports that you state (a percentage, a "times
as likely", a year, a sample size) is checked against the page and stated
with the year and the sample it belongs to.

Copyright rules are PLAN §E: one opening quotation ≤ 40 words, ≤ 60 words of
quotation a lesson, exact, with `# PDF p. N of the operator's copy` beside the
dict; never the book's tables, figures, survey items or example data; cite by
chapter and section in prose. Never copy any stretch of the text into the
repository, the project files or a report.

## Where you write

- `content/accelerate/cN_<name>/__init__.py` (the COURSE dict, replacing
  `COURSE = None`), `part_a.py`, and `part_b.py` past five lessons. The
  course `how_to` carries the attribution: a read-along of Nicole Forsgren,
  Jez Humble and Gene Kim, *Accelerate: The Science of Lean Software and
  DevOps* (IT Revolution, 2018), with samples and data written for these
  lessons (course 8 adds: Chapter 16 is by Steve Bell and Karen Whitley Bell).
- **Course 1's author only** also completes `PATH` in
  `content/accelerate/__init__.py` (tagline, description, key,
  sequence_intro, why_order, prerequisites, material, footer_lead) from PLAN
  §A, mirroring `content/domain_driven_design/__init__.py` field for field,
  with 8 courses and 46 lessons (fix the numbers if the final count differs —
  check `grep -c '"slug"' content/accelerate/c*/part_*.py` at the end).
- `content/spoken/accelerate.py`: spoken forms the read-out cannot settle.
  Others write to it at the same time: re-read it just before each edit, add
  only a block headed `# <Your course title>`, never touch another.
- Nothing else. Do not touch `scripts/`, `tests/`, `site/`, other courses or
  the kit. If the kit cannot show something, write the lesson with what it
  can show and list the gap in your report.
- Do not commit or push, and run no git command that changes the index or the
  working tree; other authors share this checkout.

## Two phases

**Phase A (while the kit is being built):** read your chapters, then write
every lesson in full — prose, concepts, steps, mistakes, quiz, key lines,
worked example — with a `lab` dict drafted from PLAN §D (mode, view, your
sample as presets with `expect: {}`). You cannot render until `acckit` is
registered; check with `grep -c '"acckit"' scripts/mathpath/labs/__init__.py`
(non-zero once it is) and for `docs/accelerate/kit-report.md`. Run
`quotes.py` and `overlap.py` in phase A. If the kit is not ready, stop and
report "phase A done" with a list of what remains; you will be told when to
continue.

**Phase B (when the kit report exists and acckit is registered):** correct
every lab cfg against `kit-report.md`, then run the loop below.

## The loop

Render your course only:
`python3 scripts/preview_subject.py accelerate --course <course-slug> --out <dir>`
with `<dir>` a new folder under `/tmp/claude-0/-home-claude/5c90b399-20f2-5d19-9db3-f3c6934b2289/scratchpad/preview/`.
`acckit` is a gated kit: every preset needs an `expect`. Write `expect: {}`
first, run `node scripts/labcheck.js --observe <dir>/site/<course>/<lesson>/index.html`,
and pin each tile string only after checking it against your own computation
by hand. Open each lesson once in Playwright (`require('playwright')`,
`chromium.launch()`), load each preset, try the exercise. Re-run
`preview_subject.py` until it prints OK; run
`/usr/bin/python3 scripts/speechcheck.py` (and `--list accelerate` for this
Subject's worklist; it may need the path wired, in which case note it) and fix
every unspoken run. Run `quotes.py` on every quotation and `overlap.py` on
your course directory until every run it prints is a title, a section or
capability name, an answer option, or a counted quotation. Try to argue for
every wrong quiz answer; if you can, rewrite it.

If the package fails to import because another course is mid-edit, wait a
minute and retry.

## Report

End with a short report (under 400 words): lessons written; every §C
deviation and why; any kit gap; renderer or read-out problems; each quotation
with its `quotes.py` result; `overlap.py` final state; the preview command's
final output line; spoken forms added.
