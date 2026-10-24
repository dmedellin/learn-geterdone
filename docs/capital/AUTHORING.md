# Authoring a Capital course: the brief every author works from

This is the hand-off for writing one course of the Capital Subject. The design
authority is `docs/capital/PLAN.md`; where this file and the plan differ, the
plan wins, and you say so in your report.

## Read first, in this order

1. `AGENTS.md` §0, §7, §8 (not all of it; never read `site/`), and
   `content/AGENTS.md` (how prose, math runs and spoken forms are written).
2. `docs/capital/PLAN.md` §0, §B, your course's entries in §C, §E, §F, §G.
   §F is the voice. Read the exemplary paragraph twice.
3. The kit you will configure. Do not read §D cover to cover; read the
   kit reports, which list every cfg field per mode and view and every tile id
   with an example string, and the deviations from §D that you must follow:
   - Volume I modes (value, form, money, circuit, surplus, workday, machine,
     wages, accumulate): `docs/capital/kit-a-report.md`
   - Volumes II and III modes (turnover, schemes, profit, prices, tendency,
     interest, rent, revenue): `docs/capital/kit-b-report.md`
   The code is `scripts/mathpath/labs/capkit.py` and `capkit_b.py`; the lab key
   is always `"capkit"`.
4. One finished course as a shape reference:
   `content/philosophy/c1_arguments/__init__.py` and its `part_a.py`. The
   field table is `docs/philosophy/PLAN.md` §E ("Course fields" and the lesson
   field table); same ranges, same enforcement.
5. If Course 1 (`content/capital/c01_commodities/`) is already written, read
   two of its lessons as the voice reference for this Subject.

## The text

Plain-text Kerr editions are at
`/mnt/project-files/capital-texts/volume-{1,2,3}-kerr.txt` (read-only; never
write to that folder). Before writing a lesson, find its chapter with
`grep -n` and read the whole chapter, not only the passage. Quote by copying
from the file, character for character, under 120 words, and put the line
number in a comment beside the lesson dict (`# Kerr vol. 1, l. 1234`). Never
quote from memory or from any other translation. If a figure in §C differs
from the text, the text wins: correct the §C entry in `docs/capital/PLAN.md`
in the same change and say so in your report.

## Where you write

- `content/capital/cNN_<name>/__init__.py` (the COURSE dict, replacing
  `COURSE = None`), `part_a.py`, and `part_b.py` if the course has more than
  six lessons (split at the midpoint).
- `content/spoken/capital.py`: spoken forms for math runs the read-out cannot
  settle. Other authors write to this file at the same time: re-read it just
  before each edit, add only a block headed `# <Your course title>`, and
  never touch another course's block.
- `docs/capital/PLAN.md`: only §C corrections the text forces, in your
  course's entries.
- Nothing else. Do not touch `scripts/`, `tests/`, `site/`, other courses,
  or the kit. If the kit cannot show something a lesson needs, write the
  lesson with what it can show and list the gap in your report.
- Do not commit or push. The orchestrator reviews and commits.

## The loop for each lesson

1. Write the dict from the §C entry; §C's misconception is `mistakes[0]`.
2. Write the lab cfg and presets with `expect: {}`.
3. Render your course only:
   `python3 scripts/preview_subject.py capital --course <course-slug> --out <dir>`
   (use a directory under your scratch space; the tool prints where it wrote).
4. `node scripts/labcheck.js --observe <dir>/site/<course>/<lesson>/index.html`
   and copy the tile strings each preset exists to show into `expect`. Check
   each against your own arithmetic and against Marx's figures in the text
   before you pin it. A pinned string you did not verify is worse than none.
5. Re-run `preview_subject.py` for your course without `--no-labcheck` until it
   prints OK, and fix every unspoken run it lists.
6. Try to argue for every wrong quiz answer. If you can, rewrite it.

## Voice, in short (PLAN §F is the authority)

The voice comes from three recorded lectures Dave admires: the teacher reads the
text whole, then goes through it line by line; tells the history of ideas as a
story with people in it; reaches for an everyday example when the idea is
abstract; talks to the listener as "you"; is warm and lets one light remark
through. Do not force any of this. A lesson that sounds like a person who has
read the chapter many times and wants you to see it is the target; a lesson that
performs friendliness is a failure. No slang, no first-person anecdotes, no
"let's dive in". Marx is presented, not endorsed: state what the chapter
argues, at strength, and where it is contested, say who contests it and why, at
strength too. The `note` says what the lesson's arithmetic cannot settle. The
last `p` of the body points to the next lesson (at a course's end, to the next
course).

## Report

End with a short report: lessons written, every §C deviation and why, any kit
gap, the preview command's final output line, and any spoken forms added.

## Lessons from the Course 1 review

- Every phrase inside `&ldquo;…&rdquo;` counts as a quotation and must be in
  the Kerr text. The pilot had one phrase written from memory and attributed
  to Marx; it was not in the chapter. Run the quotation checker over every
  quoted span, not only the opening block.
- Every preset id must appear in a body paragraph with the figure it shows.
- A three-letter word at the head of a key line or after `=` (`due`, `out`,
  `use`, `tax`, `net`) is spelt out letter by letter by the read-out. Reword
  (`payable`, `bullion out = …` → put the word mid-phrase) or rephrase.
- Abbreviations such as `cwt.` read badly; write `hundredweight`.
- Name the standard objection to a step in the lesson that takes the step,
  and vary the closing sentence that says the Subject does not settle it.
