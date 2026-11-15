# Lesson layout backlog: reading mode

A review of how lesson, course and Subject pages present their content, written
2026-11-15 in answer to "there is a lot of peripheral data around the main
topic". The review, with page maps drawn to scale, is the Lesson Layout Review
artifact. Dave answered "create the backlog and implement", so this file is the
plan and the record of what shipped, in the way
[SITE-STRUCTURE-BACKLOG.md](SITE-STRUCTURE-BACKLOG.md) is for the home page.

Direction chosen: **B, Reading mode**, shipped in two releases with the trim
(**A**) first. C (guided steps) was not chosen: it works against long
read-along passages, which are most of the library.

## What was measured

On the live templates, with Leviathan's "The War of Every Man Against Every
Man" and Algebra's "Order of Operations", at 390 px and 1366 px:

| finding | phone | laptop |
|---|---|---|
| distance to the first sentence of the reading | 2,951 px, 3.5 screens | 1,311 px, 1.5 screens |
| previews of the lesson before the lesson | 4 | 4 |
| characters per line of reading text | ~45 | ~150 (the comfortable range is 50 to 75; WCAG 1.4.8 caps it at 80) |
| course page: first lesson in the list | 3,531 px, 4.2 screens | 1,717 px |
| Subject page: first course in the list | 3,079 px, 3.6 screens | 1,504 px |

The four previews are the hero summary (80 to 170 words), the code-styled key
card beside it, the three "What this lesson establishes" cards, and the side
note next to the reading's heading. After the material every lesson also ends
with a feedback form (an editor's tool, not a reader's) and a footer whose two
lines state the same disclaimer twice. Every block is the same white card, so
nothing tells the eye that the reading is the main event.

Course and Subject pages have the same habit: the list a reader opened the page
for sits under a hero, a code card, stat tiles ("Format: Interactive" on every
course) and objective cards.

## Principles the items apply

- **Coherence and redundancy** (Mayer; Sweller): remove material that is not
  needed, and do not say the same thing four ways before the content.
- **Advance organizer** (Ausubel): one short preview helps, so the fix is one
  sentence, not none.
- **Signaling** (Mayer): one clear heading level and a visible "you are here";
  the reading should not look like every other card.
- **Measure**: 50 to 75 characters per line (Bringhurst; WCAG 1.4.8).
- **Progressive disclosure** (NN/g): keep the editor's form and the background
  one tap away.
- **Retrieval practice** (Roediger and Karpicke): the key ideas work better as
  something to recall at the end than as cards to read at the top.

## Constraints

- **No content rewrites and no URL changes.** Every authored field is reused in
  a new place. The few that are no longer shown are listed under "Fields no
  longer shown", and stay in the content so a later decision can bring them
  back.
- **The page-family contract** in `tests/test_course_ui.py` pins each family's
  `data-ui` regions and their order. Moving the lesson list above the overview
  is a deliberate change to that contract, made in the same commit.
- **Trading pages are hand-written** and take only the shared progress,
  feedback, read-out and `UI_CSS` blocks through `scripts/add_progress_marks.py`.
  Anything that changes those blocks reaches Trading too; anything in the
  generated renderer does not.

## Backlog

Priority: **P1** answers the complaint, **P2** is a clear improvement, **P3** is
polish. Effort: S (an hour or two), M (a session), L (several sessions).

### Release 1: trim (direction A)

| id | pri | item | effort | touches |
|---|---|---|---|---|
| L-1 | P1 | **One preview, not four.** The lesson hero shows a one-line kicker (Lesson · chapter), the title and the lesson's authored `one_line`. The pill styling, the code card and the long summary leave the hero; the summary and the key block move to the end of the lesson (L-9), so nothing authored disappears. | S | `render.py::lesson_page_with_lab`, theme |
| L-2 | P1 | **Drop the two jump buttons** ("Open the interactive lesson", "Practice"); they only scroll down the same page. Listen stays. | S | `render.py`, `readout.py` |
| L-3 | P1 | **Readable measure.** Reading text in a column of about 68 characters at 17 px with a 1.7 line height, without a card around it. Labs, tables and code keep the full width. | S | theme (generated pages only) |
| L-4 | P1 | **"In brief" instead of three cards.** The three key ideas become a short list under the title in Release 1, then move to the end in Release 2 (L-9). | S | `render.py` |
| L-5 | P2 | **Breadcrumb on a phone shows the course only**, as a back link. The full trail stays in the markup and on wider screens. | S | theme |
| L-6 | P2 | **Feedback form behind a disclosure** ("Suggest a change to this lesson"). It opens by itself when the lesson already has notes, so the editor's list is never hidden from the editor. Shared with Trading. | S | `feedback.py`, `add_progress_marks.py` run |
| L-7 | P2 | **Footer says its piece once** on lessons: the licence line and host, without the course lead that repeats the licence clause. The course lead stays on the course home. | S | `render.py` |
| C-1 | P1 | **Course page: lessons first.** Hero without the code card, with a one-line meta (lessons, level) in place of the three stat tiles; the lesson list right under it; objectives, background, practice suggestions and "not covered" behind "More about this course". Closes SITE-STRUCTURE B-18 ("Format: Interactive"). | M | `render.py::course_home`, contract test |
| S-1 | P1 | **Subject page: courses first.** Hero without the code card, the four facts as one meta line, the course list right under it as a single column in order, overview and background behind "More about this Subject". The single column is SITE-STRUCTURE B-17's desktop half. | M | `render.py::path_page`, contract test |

### Release 2: reading mode (direction B)

| id | pri | item | effort | touches |
|---|---|---|---|---|
| L-8 | P1 | **A slim lesson bar that stays on screen**: the course name as a link, where you are (Read, Try, Practise, Check) and Listen. It replaces the jump buttons and gives the "you are here" signal. | M | `render.py`, theme, `readout.py` |
| L-9 | P1 | **Recap at the end, as recall.** The three key ideas become "say it, then check" disclosures after the check, followed by the long summary and the key block ("In symbols"), next to Mark complete and the next lesson. | S | `render.py` |
| L-10 | P1 | **The lab inside the reading**, right after the first paragraph or list that mentions the lab; a lesson whose text never mentions it gets the lab after the reading. Measured on the current content: 1,079 of 1,387 lessons mention the lab, at a median 42% of the way through the text. A per-lesson override can come later if a placement reads badly. | M | `render.py` |
| L-11 | P2 | **Method, practice, mistakes and check without card chrome**: the method steps as a numbered list in the reading column, the mistakes and the check as plain sections. The quiz and the lab keep their panels because they are things to use. | S | `render.py`, theme |

### Later, only if asked

| id | pri | item | effort | notes |
|---|---|---|---|---|
| L-12 | P2 | **Trading lessons** get the same treatment. They are hand-authored with their own template, so this is a pass through `add_progress_marks.py` per course, not a renderer change. | L | Release 1 reaches them only through L-6. |
| L-13 | P3 | **Lab beside the text on wide screens.** The lab already lays its controls beside the figure; putting the whole lab in a margin column needs labs that fit 420 px. | M | |
| L-14 | P3 | **Per-lesson lab placement**, an optional `("lab",)` body block that overrides L-10's rule where it reads badly. | S | |
| L-15 | P3 | **Retire the fields no longer shown** below, or bring them back, once the new layout has been read for a while. | S | content packages, preservation fixtures |

## Fields no longer shown

`read_intro` (the side note beside the reading's heading) and `concepts_intro`
(the line above the three cards) were previews of previews. They stay in the
content and in the preservation fixtures; nothing renders them. Every other
field still reaches the page: `summary` and `key` in the recap, `one_line` under
the title, `concepts` in "In brief" and then the recap.

## Overlap with SITE-STRUCTURE-BACKLOG.md

- **B-18** ("Format: Interactive" on course homes) is done by C-1.
- **B-17** (show order inside a Subject) is half done by S-1: the course list is
  a single column in order. The per-card "builds on" line is still open.
- **B-20** ("In this Subject" strip on course homes) and **B-21** stay open;
  neither adds to the clutter this backlog removes, and both add a block.
