# Authoring an Enterprise Application Patterns course: the brief every author works from

This is the hand-off for writing one course of the read-along of Fowler et
al., *Patterns of Enterprise Application Architecture* (Addison-Wesley, 2002).
The design authority is `docs/enterprise-patterns/PLAN.md`; where this file
and the plan differ, the plan wins, and you say so in your report. The Subject
is built the way Code Complete was, and `docs/code-complete/AUTHORING.md` is
the model: its sections "The loop for each lesson", "What every lesson must
do", "Voice, in short" and "Lessons from Capital and Phenomenology" apply here
in full, reading Fowler (and the contributing author of a pattern) for
McConnell, `eakit` or `cckit` for the kit, and this Subject's paths below.

The renderer's `code` block and the code read-out dialect are in place (PATH
`"speech": "code"`). The kit is built and checked.

## Read first, in this order

1. `AGENTS.md` §0, §7, §8 (not all of it; **never read `site/`**, never open
   `release/contract*.json`), and `content/AGENTS.md`.
2. `docs/enterprise-patterns/PLAN.md` §0, §A, §B, your course's entries in
   §C, §D.0, your lessons' entries in §D.4 and §D.5, §E, §F, §G, §S and §R
   (all of it: §R records what the spec review changed, and §R.1 the kit
   changes). §F is the voice.
3. `docs/enterprise-patterns/kit-report.md`: every eakit cfg field, input and
   tile id with example strings, and the deviations from §D you must follow.
   For a cckit lab, `docs/code-complete/kit-report.md`; cckit's
   `code/complexity` takes `"book": "other"` on this Subject (always set it).
   Where a kit report and §D differ, the kit report wins.
4. `docs/enterprise-patterns/presets.py` holds every lesson's lab instances
   and every snippet constant, exactly; `python3
   docs/enterprise-patterns/earef.py --cc` prints every figure. Copy snippets
   and instances from there exactly.
5. One finished course as the shape reference:
   `content/code_complete/c2_high_quality_code/__init__.py` and its
   `part_a.py`. Same fields, ranges and enforcement (PLAN §E.1).

## The text

Private extraction of the operator's copy, outside the repository:
`/tmp/claude-0/-home-claude/d46a89a5-ae93-5f9f-84a3-4e1ae07e83c0/scratchpad/book/poeaa.txt`
(one form feed per PDF page; PDF page = the copy's own contents page; the copy
has no printed page numbers). Helpers in `…/scratchpad/tools/`:
`python3 eabook.py '<regex>' [-C n]`, `python3 eapage.py N [M]`, and
`python3 ea_quotes.py FILE` (lines `tag|pdfpage|quote` → OK/LOOSE/MISS).
Read the section around every claim before you write "Fowler argues"; never
read the file whole.

Copyright rules are PLAN §E.3: one opening quotation (§C's **Quote**) of at
most 40 words, at most 60 words of quotation a lesson, copied character for
character with `# PDF p. N of the operator's copy` beside the dict; never the
book's listings, tables, figures, sketches or example domains; cite by
chapter, section and pattern, never by page, in prose. Never copy any stretch
of the text into the repository, the project files or a report. Credit a
pattern to its contributing author where PLAN §F rule 6 says so.

## Where you write

- `content/enterprise_patterns/cN_<name>/__init__.py` (the COURSE dict,
  replacing `COURSE = None`), `part_a.py`, and `part_b.py` where PLAN §B
  splits the course. The course `how_to` carries the attribution: a
  read-along of Fowler et al., *Patterns of Enterprise Application
  Architecture* (Addison-Wesley, 2002), with code written for these lessons.
- **Course 1's author only** also completes `PATH` in
  `content/enterprise_patterns/__init__.py` from PLAN §A, mirroring
  `content/code_complete/__init__.py` field for field.
- `content/spoken/enterprise_patterns.py`: spoken forms the read-out cannot
  settle. Other authors write to it at the same time: re-read it just before
  each edit, add only a block headed `# <Your course title>`, never touch
  another course's block. (Course 1 also adds PATH key lines' readings.)
- `docs/enterprise-patterns/PLAN.md`: only §C corrections your course forces,
  in your course's entries, and §S.2 rows the book settles.
- Nothing else. Do not touch `scripts/`, `tests/`, `site/`, other courses or
  the kits. If a kit cannot show something, write the lesson with what it can
  show and list the gap in your report.
- Do not commit or push, and run no git command that changes the index or the
  working tree; other authors share this checkout.

## The loop, with this Subject's commands

Render your course only:
`python3 scripts/preview_subject.py enterprise_patterns --course <course-slug> --out <dir>`
with `<dir>` a new folder under
`/tmp/claude-0/-home-claude/d46a89a5-ae93-5f9f-84a3-4e1ae07e83c0/scratchpad/`.
Write presets with `expect: {}` first, then
`node scripts/labcheck.js --observe <dir>/site/<path>/index.html`, and pin
each tile string only after checking it against §C/earef and your own count.
Every preset needs an `expect` (eakit and cckit are both gated kits). Open each
lesson once in Playwright (`require('playwright')`, `chromium.launch()`),
load each preset, try the exercise. Re-run `preview_subject.py` without
`--no-labcheck` until it prints OK; run `/usr/bin/python3 scripts/speechcheck.py`
and fix every unspoken run. Run `ea_quotes.py` on every quotation. Try to
argue for every wrong quiz answer; if you can, rewrite it (PLAN §E.4 item 5).

If the package fails to import because another course is mid-edit, wait a
minute and retry.

## Report

End with a short report: lessons written; every §C deviation and why; any kit
gap; renderer or read-out problems; pages or figures corrected against the
text; each quotation with its `ea_quotes.py` result; the preview command's
final output line; spoken forms added.

## Overlap scan (added after the first reviews)

`python3 /tmp/claude-0/-home-claude/d46a89a5-ae93-5f9f-84a3-4e1ae07e83c0/scratchpad/tools/overlap.py content/enterprise_patterns/<course dir> 8` prints
every run of 8 or more consecutive words your course shares with the book, with
its PDF page. Every run it prints must be one of: a chapter, section or pattern
title or a list of titles; one of the lesson's counted quotations (in quotation
marks, within the 40/60-word limits, checked with `ea_quotes.py`); or a code
token sequence. Anything else, including a pattern's one-line intent, is
reworded in your own words. Run it until it prints nothing else.
