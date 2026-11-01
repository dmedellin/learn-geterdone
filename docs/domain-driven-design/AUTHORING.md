# Authoring a Domain-Driven Design course: the brief every author works from

The hand-off for writing one course of the read-along of Eric Evans,
*Domain-Driven Design: Tackling Complexity in the Heart of Software*
(Addison-Wesley, 2004). The design authority is
`docs/domain-driven-design/PLAN.md`; where this file and the plan differ, the
plan wins, and you say so in your report. The Subject is built the way Code
Complete and Enterprise Application Patterns were:
`docs/code-complete/AUTHORING.md` sections "The loop for each lesson", "What
every lesson must do", "Voice, in short" and "Lessons from Capital and
Phenomenology" apply in full (read Evans for McConnell, and the kit named in
PLAN §C for cckit).

## Read first, in this order

1. `AGENTS.md` §0, §7, §8 (**never read `site/`**, never open
   `release/contract*.json`), and `content/AGENTS.md`.
2. `docs/domain-driven-design/PLAN.md` in full (it is short).
3. `docs/enterprise-patterns/PLAN.md` §E.3 (quoting), §E.4 (the author's
   checklist) and §F (voice) — search for the headings, read those sections
   only. This Subject adopts them.
4. For a lab:
   - `dddkit`: `docs/domain-driven-design/kit-report.md` (every cfg field,
     input format, tile id, with examples). It is written while you draft;
     if it is absent, draft the prose first (phase A below).
   - `cckit`: `docs/code-complete/kit-report.md`, and a finished lesson that
     uses the same view (`grep -rn '"view": "<view>"' content/enterprise_patterns content/code_complete`);
     `code/complexity` takes `"book": "other"` on this Subject (always set it).
   - `eakit`: `docs/enterprise-patterns/kit-report.md` and the lesson that uses
     the mode in `content/enterprise_patterns/`.
5. One finished course as the shape reference:
   `content/enterprise_patterns/c2_domain_logic/__init__.py` and its
   `part_a.py`. Same fields, ranges and enforcement
   (`scripts/preview_subject.py` EXACT/RANGES: 3 concepts, 3 mistakes, 4–5
   steps, 3–4 quiz, 3–8 key lines of at most 46 columns, 7–18 body blocks).

## The text

Private extraction of the operator's copy, outside the repository:
`/tmp/claude-0/-home-claude/7540f9d1-06bc-59b3-bf0e-d0303b4bcb74/scratchpad/book/ddd.txt`
(one form feed per PDF page; the running-header numbers are NOT PDF pages —
use the tools' PDF page). Helpers in
`/tmp/claude-0/-home-claude/7540f9d1-06bc-59b3-bf0e-d0303b4bcb74/scratchpad/tools/`:

- `python3 book.py '<regex>' [-C n]` — search; prints the PDF page.
- `python3 page.py N [M]` — print PDF pages N..M.
- `python3 quotes.py FILE` — lines `tag|pdfpage|quote` → OK / LOOSE / MISS.
- `python3 overlap.py <dir> 8` — every run of ≥ 8 words your course shares
  with the book.

Read the sections behind every claim before you write "Evans argues"; read
each of your lessons' sections in full (PLAN §C gives PDF pages; they are
approximate, check the outline with `book.py`). Never read the file whole.

Copyright rules are PLAN §E: one opening quotation ≤ 40 words, ≤ 60 words of
quotation a lesson, exact, with `# PDF p. N of the operator's copy` beside the
dict; never the book's code, diagrams, dialogues, tables or examples' data, and
never its example domains as lab data; cite by chapter, section and pattern in
prose. Never copy any stretch of the text into the repository, the project
files or a report.

## Where you write

- `content/domain_driven_design/cN_<name>/__init__.py` (the COURSE dict,
  replacing `COURSE = None`), `part_a.py`, and `part_b.py` past five lessons.
  The course `how_to` carries the attribution: a read-along of Eric Evans,
  *Domain-Driven Design: Tackling Complexity in the Heart of Software*
  (Addison-Wesley, 2004), with models and code written for these lessons.
- **Course 1's author only** also completes `PATH` in
  `content/domain_driven_design/__init__.py` (tagline, description, key,
  sequence_intro, why_order, prerequisites, material, footer_lead) from PLAN §A,
  mirroring `content/enterprise_patterns/__init__.py` field for field, with 9
  courses and 53 lessons (fix the numbers if the final count differs).
- `content/spoken/domain_driven_design.py`: spoken forms the read-out cannot
  settle. Others write to it at the same time: re-read it just before each
  edit, add only a block headed `# <Your course title>`, never touch another.
- Nothing else. Do not touch `scripts/`, `tests/`, `site/`, other courses or
  the kits. If a kit cannot show something, write the lesson with what it can
  show and list the gap in your report.
- Do not commit or push, and run no git command that changes the index or the
  working tree; other authors share this checkout.

## Two phases

**Phase A (while the kit is being built):** read your chapters, then write every
lesson in full — prose, concepts, steps, mistakes, quiz, key lines, worked
example — with a `lab` dict drafted from PLAN §D (mode, view, your instance as
presets with `expect: {}`). You cannot render yet if `dddkit` is not
registered; check with
`grep -c '"dddkit"' scripts/mathpath/labs/__init__.py` (non-zero once it is). Run `quotes.py`
and `overlap.py` in phase A. If the kit is not ready, stop and report
"phase A done" with a list of what remains.

**Phase B (when the kit report exists and dddkit is registered):** correct
every lab cfg against `kit-report.md`, then run the loop below.

## The loop

Render your course only:
`python3 scripts/preview_subject.py domain_driven_design --course <course-slug> --out <dir>`
with `<dir>` a new folder under
`/tmp/claude-0/-home-claude/7540f9d1-06bc-59b3-bf0e-d0303b4bcb74/scratchpad/preview/`.
`dddkit`, `cckit` and `eakit` are gated kits: every preset needs an `expect`.
Write `expect: {}` first, run
`node scripts/labcheck.js --observe <dir>/site/<course>/<lesson>/index.html`,
and pin each tile string only after checking it against your own count by
hand. Open each lesson once in Playwright (`require('playwright')`,
`chromium.launch()`), load each preset, try the exercise. Re-run
`preview_subject.py` until it prints OK; run
`/usr/bin/python3 scripts/speechcheck.py` (and `--list domain-driven-design`
for this Subject's worklist; it may need the path wired, in which case note it) and fix every unspoken run. Run `quotes.py` on every quotation and
`overlap.py` on your course directory until every run it prints is a title, a
pattern or section name, or a counted quotation. Try to argue for every wrong
quiz answer; if you can, rewrite it.

If the package fails to import because another course is mid-edit, wait a
minute and retry.

## Report

End with a short report (under 400 words): lessons written; every §C deviation
and why; any kit gap; renderer or read-out problems; each quotation with its
`quotes.py` result; `overlap.py` final state; the preview command's final
output line; spoken forms added.
