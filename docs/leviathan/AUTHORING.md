# Authoring a Leviathan course: the brief every author works from

The hand-off for writing one course of the read-along of Thomas Hobbes,
*Leviathan* (1651). The design authority is `docs/leviathan/PLAN.md`; where
this file and the plan differ, the plan wins, and you say so in your report.
The Subject is built the way Capital was: `docs/capital/AUTHORING.md`
sections "The loop for each lesson", "Voice, in short", "Lessons from the
Course 1 review" and "Lessons from the Course 1 second review" apply in full
(read Hobbes for Marx, and `levkit`, `argkit` or `choicekit` for capkit).

## Read first, in this order

1. `AGENTS.md` §0, §7, §8 (**never read `site/`**, never open
   `release/contract*.json`), and `content/AGENTS.md`.
2. `docs/leviathan/PLAN.md` in full.
3. `docs/capital/PLAN.md` §E.3 (quoting) and §F (voice) — search for the
   headings, read those sections only; read §F's exemplary paragraph twice.
4. For a `levkit` lab: `docs/leviathan/kit-report.md` (every cfg field, input
   format, tile id, with examples). It is written while you draft; if it is
   absent, draft the prose first (phase A below).
   For an `argkit` or `choicekit` lab: `docs/philosophy/PLAN.md` §D.0 and the
   mode's entry in §D.1/§D.2, the kit module's docstring for that mode, and
   one Philosophy lesson that uses the same mode as a working cfg
   (`grep -rn '"mode": "<mode>"' content/philosophy/ content/phenomenology/`).
   Those kits are finished and registered: you can render those lessons now.
5. One finished course as the shape reference:
   `content/capital/c01_commodities/__init__.py` and its `part_a.py`. Same
   fields, ranges and enforcement (`scripts/preview_subject.py` EXACT/RANGES:
   3 concepts, 3 mistakes, 4–5 steps, 3–4 quiz, 3–8 key lines of at most 46
   columns, 7–18 body blocks). Also read the Philosophy lesson "Hobbes and the
   State of Nature" (`content/philosophy/c5_games/part_b.py`) so you do not
   repeat it.

## The text

Private OCR of the operator's copy (Tuck's Cambridge edition, 1996), outside
the repository:
`/tmp/claude-0/-home-claude/38cc3589-e9c2-59a8-8621-efe796c7d5fc/scratchpad/book/lev.txt`
(one form feed per PDF page; Hobbes's text is PDF pages 97–589; every other
page is blanked because it is Tuck's apparatus, in copyright). Helpers in
`/tmp/claude-0/-home-claude/38cc3589-e9c2-59a8-8621-efe796c7d5fc/scratchpad/tools/`
(run them from that directory):

- `python3 book.py '<regex>' [-C n] [-i]` — search; prints the PDF page and chapter.
- `python3 page.py N [M] [--png]` — print PDF pages N..M; `--png` also renders
  the page image to `../pages/pN.png`, which you can Read to see the printed
  page. **The OCR is of a low-resolution scan and has errors** ("Hosses" for
  "Hobbes", `|` for `I`, dropped italics, marginal notes run into the text,
  page numbers like `(62)` or `[23]` in the stream). The image is the
  authority for every quotation.
- `python3 quotes.py FILE` — lines `tag|pdfpage|quote` → OK / LOOSE / NEAR r /
  MISS, with word counts. LOOSE and NEAR mean: open the page image and check
  character by character; an OCR error is fine, a misquote is not.

Chapter start pages (PDF): Epistle 99, Introduction 105, ch. 1 109, 2 111,
3 116, 4 120, 5 127, 6 133, 7 143, 8 146, 9 156, 10 158, 11 165, 12 171,
13 182, 14 187, 15 196, 16 207, 17 213, 18 217, 19 225, 20 234, 21 241,
22 251, 23 262, 24 266, 25 272, 26 279, 27 297, 28 310, 29 317, 30 327,
31 341, 32 351, 33 356, 34 365, 35 376, 36 383, 37 396, 38 402, 39 416,
40 418, 41 428, 42 434, 43 498, 44 513, 45 536, 46 554, 47 570, Review and
Conclusion 579–589.

Read each of your lessons' chapters in full before you write (`page.py`), not
only the passage. Every claim of the form "Hobbes argues/says/defines" is
checked against the page. Hobbes's marginal notes (the short headings Tuck
prints beside the text) are Hobbes's and may be quoted. Tuck's footnotes, if
any appear at a page foot, are not: never quote or paraphrase them.

Copyright: Hobbes's text is public domain. Never quote, paraphrase or copy
anything from Tuck's introduction, notes or index (they are blanked in the
file; do not look for them in the PDF).

## Quoting (PLAN §E)

The first `body` block is a `p`: `<strong>Chapter 13.</strong> &ldquo;…&rdquo;`,
at most 120 words, exactly as printed (1651 spelling, capitals, punctuation;
drop italics; render a long s as s; keep `&` as `&amp;`). Beside the lesson
dict: `# Leviathan ch. N, 1651 p. M; PDF p. K of the operator's copy` (the
1651 page is the bracketed marginal number; omit it if you cannot see it).
Every phrase inside `&ldquo;…&rdquo;` anywhere in a lesson must be in the
text and must pass `quotes.py` (or be confirmed on the image). The lesson's own
prose uses modern spelling. A Scripture quotation inside Hobbes's text is
quoted as Hobbes prints it.

## Where you write

- `content/leviathan/cN_<name>/__init__.py` (the COURSE dict, replacing
  `COURSE = None`), `part_a.py`, and `part_b.py` past five lessons (split at
  the midpoint). The course `how_to` carries the attribution once: a
  read-along of Thomas Hobbes, *Leviathan* (1651), with "Quotations are from
  Hobbes's text of 1651, in its original spelling," and examples written for
  these lessons.
- **Course 1's author only** also completes `PATH` in
  `content/leviathan/__init__.py` (tagline, description, key, sequence_intro,
  why_order, prerequisites, footer_lead; `material` is fixed by the plan) from
  PLAN §A, mirroring `content/capital/__init__.py` field for field, with nine
  courses and 55 lessons (fix the numbers if the final count differs — check
  `grep -c '"slug"' content/leviathan/c*/part_*.py` at the end).
- `content/spoken/leviathan.py`: spoken forms the read-out cannot settle.
  Others write to it at the same time: re-read it just before each edit, add
  only a block headed `# <Your course title>`, never touch another.
- Nothing else. Do not touch `scripts/`, `tests/`, `site/`, other courses or
  the kits. If a kit cannot show something, write the lesson with what it can
  show and list the gap in your report.
- Do not commit or push, and run no git command that changes the index or the
  working tree; other authors share this checkout.

## Two phases

**Phase A (while `levkit` is being built):** read your chapters, then write
every lesson in full — prose, concepts, steps, mistakes, quiz, key lines,
worked example — with a `lab` dict. Lessons on `argkit`/`choicekit` can be
finished, rendered and pinned now. For `levkit` lessons draft the cfg from
PLAN §D.1 with `expect: {}`. You cannot render a `levkit` lesson until the kit
is registered; check with `grep -c '"levkit"' scripts/mathpath/labs/__init__.py`
(non-zero once it is) and for `docs/leviathan/kit-report.md`. A course whose
`levkit` lesson cannot render yet makes the whole course fail to preview:
while you wait, temporarily give that lesson's lab a placeholder you will
replace, or preview with only your other lessons by keeping the levkit lesson
dicts in a separate list you add back later. Run `quotes.py` in phase A. If
the kit is not ready when everything else is done, stop and report "phase A
done" with a list of what remains; you will be told when to continue.

**Phase B (when the kit report exists and levkit is registered):** correct
every `levkit` cfg against `kit-report.md`, then run the loop.

## The loop

Render your course only:
`python3 scripts/preview_subject.py leviathan --course <course-slug> --out <dir>`
with `<dir>` a new folder under
`/tmp/claude-0/-home-claude/38cc3589-e9c2-59a8-8621-efe796c7d5fc/scratchpad/preview/`.
All three kits are gated: every preset needs an `expect`. Write `expect: {}`
first, run `node scripts/labcheck.js --observe <dir>/site/<course>/<lesson>/index.html`,
and pin each tile string only after checking it against your own computation
by hand. Every preset id appears in a body paragraph with the figure it shows.
Re-run `preview_subject.py` until it prints OK; run
`/usr/bin/python3 scripts/speechcheck.py` if it accepts an unwired path
(otherwise rely on the preview's read-out list) and fix every unspoken run.
Run `quotes.py` on every quotation. Try to argue for every wrong quiz answer;
if you can, rewrite it. Vary which position holds the right quiz answer
across your course.

If the package fails to import because another course is mid-edit, wait a
minute and retry.

## Report

End with a short report (under 400 words): lessons written; every §C
deviation and why; any kit gap; renderer or read-out problems; each opening
quotation with its `quotes.py` result (and "checked on image" where you did);
the preview command's final output line; spoken forms added.
