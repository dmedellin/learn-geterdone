# Authoring a Design Patterns course: the brief every author works from

The hand-off for writing one course of the read-along of Gamma, Helm, Johnson
and Vlissides, *Design Patterns: Elements of Reusable Object-Oriented
Software* (Addison-Wesley, 1995). The design authority is
`docs/design-patterns/PLAN.md`; where this file and the plan differ, the plan
wins, and you say so in your report. The Subject is built the way
Domain-Driven Design, Code Complete and Enterprise Application Patterns were:
`docs/code-complete/AUTHORING.md` sections "The loop for each lesson", "What
every lesson must do", "Voice, in short" and "Lessons from Capital and
Phenomenology" apply in full (read the Gang of Four for McConnell, and the
kit named in PLAN §C for cckit).

## Read first, in this order

1. `AGENTS.md` §0, §7, §8 (**never read `site/`**, never open
   `release/contract*.json`), and `content/AGENTS.md`.
2. `docs/design-patterns/PLAN.md` in full.
3. `docs/enterprise-patterns/PLAN.md` §E.3 (quoting), §E.4 (the author's
   checklist) and §F (voice) — search for the headings, read those sections
   only. This Subject adopts them.
4. For a lab:
   - `gofkit`: `docs/design-patterns/kit-report.md` (every cfg field, input
     format, tile id, with examples). It may still be being written while you
     draft; if it is absent, draft the prose first (phase A below).
   - `dddkit`: `docs/domain-driven-design/kit-report.md` and a finished lesson
     that uses the same view (`grep -rn '"view": "<view>"' content/domain_driven_design`).
   - `cckit`: `docs/code-complete/kit-report.md`, and a finished lesson that
     uses the same view (`grep -rn '"view": "<view>"' content/domain_driven_design content/enterprise_patterns content/code_complete`);
     `code/complexity` takes `"book": "other"` on this Subject (always set it).
5. One finished course as the shape reference:
   `content/domain_driven_design/c6_patterns_and_refactoring/__init__.py` and
   its `part_a.py`. Same fields, ranges and enforcement
   (`scripts/preview_subject.py` EXACT/RANGES: 3 concepts, 3 mistakes, 4–5
   steps, 3–4 quiz, 3–8 key lines of at most 46 columns, 7–18 body blocks).

## The text

Private extraction of the operator's copy, outside the repository:
`/tmp/claude-0/-home-claude/9da44922-ed07-5577-833b-95ab59ddd870/scratchpad/book/gof.txt`
(one form feed per PDF page; printed page numbers are not PDF pages — use the
tools' PDF page). The copy is a 416-page scan with a text layer: **PDF page = printed page + 20** (the catalog's "Abstract Factory (87)" is PDF p. 107). Anchors: Chapter 1 PDF p. 21 (1.6 at p. 31), Chapter 2 p. 53, Chapter 3 p. 101, Chapter 4 p. 157, Chapter 5 p. 241, Chapter 6 p. 371; the discussions of creational, structural and behavioral patterns at pp. 155, 239, 365. OCR slips exist (e.g. "ADAPTED" for ADAPTER in a header); a quotation must match the text file, so check it with `quotes.py`. Helpers in
`/tmp/claude-0/-home-claude/9da44922-ed07-5577-833b-95ab59ddd870/scratchpad/tools/`:

- `python3 book.py '<regex>' [-C n]` — search; prints the PDF page.
- `python3 page.py N [M]` — print PDF pages N..M.
- `python3 quotes.py FILE` — lines `tag|pdfpage|quote` → OK / LOOSE / ELSEWHERE / MISS.
- `python3 overlap.py <dir> 8` — every run of ≥ 8 words your course shares
  with the book.

Read the sections behind every claim before you write "the authors argue";
read each of your lessons' patterns in full (Intent, Motivation,
Applicability, Structure, Participants, Collaborations, Consequences,
Implementation, Sample Code, Known Uses, Related Patterns). Never read the
file whole.

Copyright rules are PLAN §E: one opening quotation ≤ 40 words, ≤ 60 words of
quotation a lesson, exact, with `# PDF p. N of the operator's copy` beside the
dict; never the book's code, diagrams, tables or examples' data, and never its
example domains as lab data (PLAN §C lists them); cite by chapter, section and
pattern in prose. Never copy any stretch of the text into the repository, the
project files or a report.

## Where you write

- `content/design_patterns/cN_<name>/__init__.py` (the COURSE dict,
  replacing `COURSE = None`), `part_a.py`, and `part_b.py` past five lessons.
  The course `how_to` carries the attribution: a read-along of Gamma, Helm,
  Johnson and Vlissides, *Design Patterns: Elements of Reusable
  Object-Oriented Software* (Addison-Wesley, 1995), with designs and code
  written for these lessons.
- **Course 1's author only** also completes `PATH` in
  `content/design_patterns/__init__.py` (tagline, description, key,
  sequence_intro, why_order, prerequisites, material, footer_lead) from PLAN
  §A, mirroring `content/domain_driven_design/__init__.py` field for field,
  with 6 courses and 40 lessons (fix the numbers if the final count differs).
- `content/spoken/design_patterns.py`: spoken forms the read-out cannot
  settle. Others write to it at the same time: re-read it just before each
  edit, add only a block headed `# <Your course title>`, never touch another.
- Nothing else. Do not touch `scripts/`, `tests/`, `site/`, other courses or
  the kits. If a kit cannot show something, write the lesson with what it can
  show and list the gap in your report.
- Do not commit or push, and run no git command that changes the index or the
  working tree; other authors share this checkout.

## Two phases

**Phase A (while the kit is being built):** read your chapter's sections,
then write every lesson in full — prose, concepts, steps, mistakes, quiz, key
lines, worked example — with a `lab` dict drafted from PLAN §C/§D (mode,
view, your instance as presets with `expect: {}`). Check whether `gofkit` is
registered with `grep -c '"gofkit"' scripts/mathpath/labs/__init__.py`
(non-zero once it is) and whether `docs/design-patterns/kit-report.md` covers
your views. Run `quotes.py` and `overlap.py` in phase A.

**Phase B (when the kit report covers your views and gofkit is registered):**
correct every lab cfg against `kit-report.md`, then run the loop below. If
the kit is not ready after your phase A, wait (re-check every few minutes)
rather than stopping; if it is still not ready after about 40 minutes, stop
and report "phase A done" with a list of what remains.

## The loop

Render your course only:
`python3 scripts/preview_subject.py design_patterns --course <course-slug> --out <dir>`
with `<dir>` a new folder under
`/tmp/claude-0/-home-claude/9da44922-ed07-5577-833b-95ab59ddd870/scratchpad/preview/`.
`gofkit`, `dddkit` and `cckit` are gated kits: every preset needs an `expect`.
Write `expect: {}` first, run
`node scripts/labcheck.js --observe <dir>/site/<course>/<lesson>/index.html`,
and pin each tile string only after checking it against your own count by
hand. Open each lesson once in Playwright (`require('playwright')`,
`chromium.launch()`), load each preset, try the exercise. Re-run
`preview_subject.py` until it prints OK; run
`/usr/bin/python3 scripts/speechcheck.py` (and `--list design-patterns` for
this Subject's worklist; it may need the path wired, in which case note it)
and fix every unspoken run. **Spoken forms are merged across Subjects at
render time**: never add a key for a generic run (such as `1 + 2 = 3`) that
another Subject's page also contains; make your worked lines specific to your
lesson. Run `quotes.py` on every quotation and `overlap.py` on your course
directory until every run it prints is a title, a pattern or section name, or
a counted quotation. Try to argue for every wrong quiz answer; if you can,
rewrite it.

If the package fails to import because another course is mid-edit, wait a
minute and retry.

## Report

End with a short report (under 400 words): lessons written; every §C
deviation and why; any kit gap; renderer or read-out problems; each quotation
with its `quotes.py` result; `overlap.py` final state; the preview command's
final output line; spoken forms added.
