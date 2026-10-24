# Authoring a Phenomenology course: the brief every author works from

This is the hand-off for writing one course of the Phenomenology of
Perception Subject. The design authority is `docs/phenomenology/PLAN.md`;
where this file and the plan differ, the plan wins, and you say so in your
report. The Subject is built the way Capital was (`docs/capital/AUTHORING.md`
is the model, and its two "Lessons from" sections apply here in full).

## Read first, in this order

1. `AGENTS.md` §0, §7, §8 (not all of it; never read `site/`), and
   `content/AGENTS.md` (how prose, math runs and spoken forms are written).
2. `docs/phenomenology/PLAN.md` §0, §B, your course's entries in §C, §E, §F,
   §G. §F is the voice; read the exemplary paragraph twice.
3. `docs/phenomenology/kit-report.md`: every cfg field per mode and view,
   every tile id with an example string, and the deviations from §D you must
   follow. The code is `scripts/mathpath/labs/phenkit.py`; the lab key is
   always `"phenkit"`. Lessons that use `argkit/validity` follow the
   Philosophy Subject's lessons that use it.
4. One finished course as a shape reference:
   `content/capital/c01_commodities/__init__.py` and its `part_a.py`. The
   field table is `docs/philosophy/PLAN.md` §E; same ranges, same enforcement.
5. If Course 1 (`content/phenomenology/c1_preface/`) is already written, read
   two of its lessons as the voice reference for this Subject.

## The text

The source edition is Colin Smith's translation, Routledge Classics
pagination (PLAN §E.2). A private plain-text extraction is at
`/tmp/claude-0/-home-claude/077dbf62-e1a1-5aba-b15b-1df7e091edab/scratchpad/pop/smith.txt` (read-only; never copy it, or any long stretch of it,
into the repository, the project files or a report). Pages are separated by
form feeds; the printed page number is in the running head at the top of each
page. `python3 -I /tmp/claude-0/-home-claude/077dbf62-e1a1-5aba-b15b-1df7e091edab/scratchpad/tools/smith_pages.py /tmp/claude-0/-home-claude/077dbf62-e1a1-5aba-b15b-1df7e091edab/scratchpad/pop/smith.txt <line>` prints the
printed page of a line (for the Preface, read the roman running head instead).

Before writing a lesson, find its pages with `grep -n` and read the whole
section, not only the passage. The book is in copyright, so:

- the opening passage is at most **70 words**; a lesson's quotations, the
  opening passage included, total at most **150 words**;
- every phrase inside `&ldquo;…&rdquo;` is a quotation, copied character
  for character (Smith's ligatures as plain letters, a word split by a
  line-break hyphen joined, footnote numerals dropped, Smith's single quote
  marks inside a quotation printed as `&lsquo;…&rsquo;`); nothing else changes;
- the page goes in a comment beside the lesson dict (`# Smith p. 52`) and in
  the opening `p`, which also invites the reader to read the whole section
  in their own copy first;
- never quote from memory, from Landes or from a secondary source;
- a sentence in an opponent's voice (Merleau-Ponty often states the view he
  is about to reject for a page) is never quoted as his; say whose voice it is.

Check every lesson with
`python3 -I /tmp/claude-0/-home-claude/077dbf62-e1a1-5aba-b15b-1df7e091edab/scratchpad/tools/phen_quotes.py <course-package>` from the repo root
(e.g. `c1_preface`); it lists each span not in the text and the word counts.
A miss it reports at a page break may be a false alarm: check by eye and say so.

Every `(check against text)` in your course's §C entries is yours to resolve
against Smith. If §C differs from the text, the text wins: correct the §C
entry in `docs/phenomenology/PLAN.md` in the same change and say so in your
report. Smith's vocabulary differs from the spec's in a few places (PLAN §E.2):
Smith's "body image" is the lessons' *body schema*, said once where it is
introduced.

## Where you write

- `content/phenomenology/cN_<name>/__init__.py` (the COURSE dict, replacing
  `COURSE = None`), `part_a.py`, and `part_b.py` if the course has more than
  six lessons (split at the midpoint). The course `how_to` carries the
  attribution line: quotations from Colin Smith's translation (Routledge
  Classics), short extracts quoted for commentary, page numbers that edition's.
- `content/spoken/phenomenology.py`: spoken forms for math runs the read-out
  cannot settle. Other authors write to this file at the same time: re-read it
  just before each edit, add only a block headed `# <Your course title>`, and
  never touch another course's block.
- `docs/phenomenology/PLAN.md`: only §C corrections the text forces, in your
  course's entries.
- Nothing else. Do not touch `scripts/`, `tests/`, `site/`, other courses,
  or the kit. If the kit cannot show something a lesson needs, write the
  lesson with what it can show and list the gap in your report.
- Do not run git commands that change the index or the working tree; other
  authors share this checkout. Do not commit or push.

## The loop for each lesson

1. Write the dict from the §C entry; §C's misconception is `mistakes[0]`.
2. Write the lab cfg and presets with `expect: {}`.
3. Render your course only:
   `python3 scripts/preview_subject.py phenomenology --course <course-slug> --out <dir>`
   with `<dir>` a folder of your own under `/tmp/claude-0/-home-claude/077dbf62-e1a1-5aba-b15b-1df7e091edab/scratchpad/`.
4. `node scripts/labcheck.js --observe <dir>/site/<path>/index.html` and copy
   the tile strings each preset exists to show into `expect`. Check each
   against your own arithmetic before you pin it. A pinned string you did not
   verify is worse than none.
5. Re-run `preview_subject.py` without `--no-labcheck` until it prints OK,
   and fix every unspoken run it lists.
6. Try to argue for every wrong quiz answer. If you can, rewrite it.
7. Run the quotation checker.

## Voice, in short (PLAN §F is the authority)

The voice comes from three recorded lectures Dave admires: the teacher reads the
text whole, then goes through it line by line; tells the history of ideas as a
story with people in it; reaches for an everyday example when the idea is
abstract; talks to the listener as "you"; is warm and lets one light remark
through. Do not force any of this. A lesson that sounds like a person who has
read the chapter many times and wants you to see it is the target; a lesson
that performs friendliness is a failure. No slang, no first-person anecdotes,
no "let's dive in". Open with an everyday scene in at most half of a course's
lessons. Merleau-Ponty is presented, not endorsed: state what the section
argues, at strength; state each opponent (Descartes, Kant, Husserl, Sartre,
Bergson, the empiricist and intellectualist psychologists) in their own terms
and at strength; where a reading of him is disputed, say so. The cases are
people: name them as the book does and with its respect. At most one modern
aside per course, in the lesson §F names. The `note` says what the lesson's
lab cannot settle. The last `p` of the body points to the next lesson (at a
course's end, to the next course).

## Lessons from Capital that apply here

- Do not give the author a verdict the text does not contain. Re-read every
  sentence that begins "Merleau-Ponty says", "argues", "replies" or
  paraphrases him, and find the page that supports it.
- When the lesson answers a critic, the answer must be the book's actual
  reply. Merleau-Ponty died in 1961 and answers nobody who wrote later; state a
  later view at strength, then say what in the chapter bears on it.
- First-word case inside a quotation must match the text; reword around it.
- Every preset id must appear in a body paragraph with the figure it shows.
- A three-letter word at the head of a key line or after `=` is spelt out
  letter by letter by the read-out. Reword.
- Do not praise one side in the lesson's own voice.

## Report

End with a short report: lessons written, every §C deviation and why, any kit
gap, the preview command's final output line, the quotation checker's final
line, and any spoken forms added.
