# Pedagogy review: Course 3, Variables (`code-complete-variables`)

Reviewed 2026-10-25 on branch `feat/code-complete-subject`, commit `8311309`
("Code Complete course 3: Variables (6 lessons)"), against the
`pedagogical-expert` brief, `docs/code-complete/PLAN.md` (§0, §B, Course 3's
§C entries, §E.4, §F), `docs/code-complete/AUTHORING.md`, the author notes,
and the pre-authoring review `docs/reviews/code-complete-spec-pedagogy-review.md`.
All six lessons were read in full in `content/code_complete/c3_variables/part_a.py`.
The course was rendered with `preview_subject.py` (final line `OK`; six pages,
six with pinned figures, none failing) and opened in Playwright at 390 and
1280 pixels; every lab was driven with its presets, with each lesson's
exercise, and with inputs a reader would paste. Every figure the lessons
state was recomputed by hand and read off the live tiles. Book passages the
lessons paraphrase (pp. 238, 240, 242, 246, 251, 257, 262, 293–294, 309, 338,
343, 509) were checked against the text; nothing from it is reproduced here.

## Verdict

This is a good course and the best-shaped of the read-alongs so far: every
lesson teaches an act a working programmer can perform on a routine in front
of them, every exercise is applied and has one determinate answer, the lab
confirms each exercise's answer exactly, and the three must-fix items the
pre-authoring review raised for this course (findings 2, 6 and 16, and the
should-fix 5) have all been taken, correctly. The voice is the one §F asks
for; the read-out speaks listings with their line numbers and says "flagged"
on a marked line.

Two defects must be fixed before it ships, and both are in the quiz. Every
one of the 24 quiz items keys the correct answer as the first option, and the
renderer does not shuffle, so a reader learns by the second question that
the top button is always right; and one item's keyed answer is contradicted
by the lab's own rule on the very table the stem describes. A third defect,
the lesson 1 `note` giving away the exercise's answer, breaks the one
page-shape rule §E.4 is strict about.

Recommendation: **fix the three must-fix items and ship**; the should-fix
items can follow in the same change.

## What the course does well

- **Every lesson teaches an act, and the act is the chapter's.** Reading a
  routine for a read-before-set (10.3), counting spans and live times
  (10.4), averaging name lengths against the Gorla figure (11.1), predicting
  an `int` wrap and a `double` sum (12.2–12.3), listing literals by the
  0-and-1 rule (12.1, 12.7), counting the pairs a global couples (13.3).
  None is "understand"; each `standard` names the act without the lab.
- **Worked example → exercise → own code**, in every lesson, with the worked
  example on a preset and the exercise on a different instance (§E.4 item 4),
  and the last step an instruction with an observable result. The
  own-code steps for the two non-code labs (lesson 4: one counter's largest
  plausible value in its declared type; lesson 6: one static field and
  every routine that touches it, as records) are real acts, which the
  pre-authoring review's finding 3 asked for.
- **Every exercise checks in the lab**, confirmed live: lesson 1 reports 0
  anomalies on `initials`; lesson 2 prints `15/4 = 3.75` and `21/2 = 10.50`,
  then `7/4 = 1.75` and `13/2 = 6.50`, with the per-name table showing 11
  and 10, then 7 and 6; lesson 3 prints `1` then `53/5 = 10.60` with
  `months` short; lesson 4 prints `-1294967296` and, as `long`,
  `3000000000`, and `1471228928` for `31536000 * 1000`; lesson 5 prints
  `38.5 (line 4), 3 (line 5), 900 (line 8)` and `none` after constants are
  declared; lesson 6 prints 2, 3, 3 of 3, 5, and 2 with owners.
- **The misconceptions are the right ones**, and they are refuted by the
  chapter and illustrated by a preset, said as such ("on the lesson's
  illustration"). Lesson 1's is the corrected one ("if it compiles, every
  variable holds the value you meant") and the body says plainly what
  `javac` does catch. Lesson 6's second mistake ("access routines remove
  the coupling") is refuted by a lab in which `dgCoupled` stays 9, which is
  what the spec review's finding 2 asked for, and the lab's banner now says
  so in a sentence.
- **The material clause holds.** No lesson calls a count a verdict; the
  lesson 2 and 3 bodies each say what the lab's number is and is not (listing
  lines against statements; a pooled average; a length against a meaning).
- **The modern aside** sits where §F.4 puts it, in lesson 3's `note`, at
  strength on both sides and unsettled.
- **The read-out.** A `code` block is read as "line 1, double average price
  of array of double prices. … line 6, flagged, count is set to count plus
  1"; `&&`-free lessons, so nothing to mis-say; `-` and `/` in worked lines
  come out "minus" and "divided by"; key lines carry no three-letter word
  that would be spelt out. `-2147483648` is "minus 2147483648". One loss is
  noted under should-fix.
- **Layout.** At 390 pixels no page scrolls sideways; code blocks and the
  lab's listing scroll in their own boxes with the gutter outside the
  selection; the lab stacks under the listing; the quiz feedback appears
  under the options with the correct one outlined after a wrong pick.

## Findings

### Must-fix

**1. Every quiz item keys the correct answer as option 1, and the renderer
does not shuffle.** *Where:* all 24 items in `part_a.py` have `"c": 0`;
`scripts/mathpath/labs/common.py` `QUIZ_SCRIPT` renders `q.a` in order.
Course 1 varies its keys (`"c": 2`, `1`), so this is the author's habit, not
the Subject's. *Why it matters:* by the second item a reader has a rule that
scores 24/24 without reading an option, and the retrieval practice the quiz
exists for is gone. *Change:* re-key so that each lesson's four items land on
four different positions, moving the option text accordingly. A permutation
that keeps every distractor's `why` sentence true as written (none of the
`why` texts refer to options by position):

| lesson | item 1 | item 2 | item 3 | item 4 |
| --- | --- | --- | --- | --- |
| 1 | c=2 | c=0 | c=3 | c=1 |
| 2 | c=1 | c=3 | c=0 | c=2 |
| 3 | c=3 | c=1 | c=2 | c=0 |
| 4 | c=0 | c=2 | c=1 | c=3 |
| 5 | c=1 | c=0 | c=3 | c=2 |
| 6 | c=2 | c=3 | c=1 | c=0 |

The three items whose options are all one character or one number (4.4 `3`,
`3.5`, `4`, `3.0`; 5.3 `2 and 1` …; 2.2) are the ones where a position rule
does the most damage, so make sure none of them stays at 0.

**2. Lesson 6, quiz item 4 (the tax table): the keyed answer is contradicted
by the lab's rule, and a distractor is right by that rule.** *Where:*
`structures-pointers-and-global-data`, quiz item 4: "A table of tax rates is
loaded once at start-up and only read afterwards by four routines. Counting
coupling as the lab does, after start-up, how many pairs does it couple?"
Keyed: "None, since no routine writes it". *What is wrong:* the routine that
loads it writes it, and the lab, given `loadRates, w, rates; a, r, rates; …
d, r, rates`, prints `dgCoupled` 4 (checked live). "Counting as the lab does"
and "after start-up" pull in opposite directions; a reader who models the
table as the lab would picks "4, one for each reader" and is told it is
wrong. The `why` then leans on p. 338 (named constants are global data but
not global variables), which is about data no routine writes, not about a
loader that runs first. *Change:* make the table one that genuinely has no
writer, so the keyed answer and the lab agree:

> *q:* "A table of tax rates is a `static final` array filled in its
> declaration, and four routines read it. Counting coupling as the lab does,
> how many pairs of routines does it couple?"
> *a:* ["None: no routine writes it", "6, every pair of the four readers",
> "4, one for each reader", "3, each reader with the next"]
> *why:* "Coupling needs a writer, and a table filled in its declaration has
> none: it is a named constant, which Section 13.3 counts as global data but
> not a global variable (p. 338). Four readers make 6 pairs, but readers alone
> are not coupled. Had a routine loaded the table at start-up, that routine
> would be its writer and the lab would count 4 pairs, one with each reader."

That last sentence keeps the case the current stem was reaching for, as the
explanation of the 4 distractor rather than as a trap.

**3. Lesson 1's `note` and quiz option give the exercise's answer away.**
*Where:* `declaring-and-initializing-variables`. (a) The `note`: "… and the
exercise is a case only the compiler sees." That sentence is on the page
above the quiz and states the exercise's answer (the lab reports nothing,
`javac` rejects it), which §E.4 item 4 says appears in the quiz `why` and
nowhere else. (b) Quiz item 1's correct option is 99 characters and carries
its own justification ("… because when the if is false line 6 reads result
before anything sets it"); the three distractors are 50–53 characters and
two of them carry a reason too, but the correct one is the only one that
explains a path. An option that explains itself is picked on form. *Change:*
(a) `note`, replacing its first sentence:

> "The lab reads the lines in order and never follows a branch or a loop;
> Java's compiler checks every path, so for locals it is stronger than the
> lab. The lab also cannot see a value that has gone stale, or a variable
> that is set correctly and holds the wrong thing; and a field it flags as
> read before set is one Java silently starts at 0."

(b) Quiz item 1's options, same key after re-keying:

> ["Nothing; javac rejects it", "result used before set on line 6; javac
> rejects it", "Nothing; javac accepts it", "result set twice, on lines 4 and
> 6; javac accepts it"]

The `why` already carries the path argument. Step 4 of the method ("look
along every path through an `if`, which the line-by-line reading does not")
is a fair hint and can stay.

### Should-fix

**4. Lesson 2's own-code step sends the reader to move a declaration that
may be a parameter's.** *Where:* step 4, "Paste a routine of your own into the
lab with the Variables box empty, find the variable with the longest live
time, move its declaration down". With the box empty the lab measures every
name the routine sets or declares, parameters and loop variables included;
on the exercise's own `reportSales` the longest live time is `sales: 8`, the
parameter (checked live), whose declaration is the header and cannot move.
*Change:* "…find the local variable with the longest live time (the table
lists parameters and loop variables too; a parameter's live time is the
routine's), move its declaration down to just before its first use, paste
again, and note how far its live time fell."

**5. Lesson 1 names the field case and gives the reader nothing to do with
it, though the lab shows it.** *Where:* the "So what does Java's compiler
catch?" paragraph, `mistakes[0]`, quiz item 4 and the `note` all say a field
starts at 0 without a word from the compiler. Pasted into the lab, `class
Counter { int hits; int bump() { hits = hits + 1; return hits; } }` prints
`coUsedBeforeSet` "hits (line 4)" (checked live): it is the one case where
the lab is stronger than `javac`, which the pre-authoring review's finding
16 asked the lesson to use, and the body's "stronger than this lab's" leaves
a reader thinking the lab is the weaker tool in every case. *Change:* add
one sentence to the end of that paragraph: "Paste such a class into the lab
and it flags the read, `hits (line 4)`, which is the one case where the
lab's reading is the stricter of the two." The current `note` sentence "a
field's default" is corrected in finding 3(a).

**6. The read-out drops the `L` from `1000L`.** *Where:* lesson 4, the
`msPerYear` paragraph: `<code>1000L</code>` is read "1000", so a listener
hears the fix as the same number. *Change:* add to `content/spoken/
code_complete.py` under a `# Variables` block a spoken form for `1000L`
("1000 L, a long literal"), or write the sentence as "the last factor as
<code>1000L</code>, a `long` literal with an L after it". The second needs
no spoken form.

**7. Lesson 1, quiz item 3 is terminology recall.** *Where:* "A local
variable is set, then set again with no use between. Which of Section 22.3's
patterns is that?" with four pattern names. §E.4 allows an item on a
section's claim, but this one measures whether the reader remembers which
hyphenated label the book uses, not whether they can see the pattern. The
distractors are not arguable as right, which is good, but nothing is learnt
from getting it wrong. *Change:* ask the reader to classify a line pair:

> *q:* "Reading top to bottom, `int n = 0;` on line 2, `n = items.length;`
> on line 4, and nothing between them reads `n`. Which of Section 22.3's
> patterns is that, and what does the lab list it under?"
> *a:* ["Defined-defined; Set twice, n (lines 2, 4)", "Entered-used; Used
> before set, n (line 4)", "Defined-exited; Set, never used, n (line 2)",
> "Used-defined; nothing, because line 4 sets n"]
> *why:* as now, plus "the lab lists it under Set twice with both lines".

**8. Lesson 6, quiz item 1 asks four things in one stem and its options run
to 127 characters.** The item is answerable and correct, but on a phone the
four options are four paragraphs that differ in one clause each, and a
reader compares them by diffing rather than by counting. *Change:* split the
exercise's answer across two items: one for "globals, routines, coupled pairs
of possible pairs" (2, 3, 3 of 3; distractors 2 of 3 "because render and
save only read config", 1 of 3, 3 of 6) and one for "direct touches before
and after access routines" (5 and 2; distractors 5 and 5, 5 and 0, 3 and 2),
dropping the present item 2 (which pair is not coupled in `globals`) if the
lesson must stay at four.

**9. Lesson 3's exercise `why` hands over the renamed names the exercise
asked the reader to invent.** Unavoidable, since the stem has to name them
to make the lengths checkable; but the exercise `p` should say so, so that the
reader commits first: add "Write your names down before you open the quiz;
it names one set, and yours need not match it to be right, so long as each
says what the variable stands for."

**10. Lesson 4's body and `summary` disagree on the pages.** The body says
"pages 291 to 297" (the dict comment says the lesson runs to the top of
p. 297); the `summary`, §C and the lesson 5 body ("pages 297 to 318") say
291–296. Say "291 to 296" in the body, or "and the top of page 297".

### Consider

**11. Lesson 3 carries seven sections in six paragraphs before the code**,
the longest argument half in the course, and 11.5–11.7 (prefixes,
abbreviations, names to avoid) are each a paragraph though none bears on the
lab. Merging those three into one paragraph of four sentences would bring
the reader to the code a screen earlier without losing a section.

**12. Lesson 5's exercise has a second teaching point the lesson does not
use.** The `3` in `raiseAlert(patient, 3)` is a priority, which Section 12.6
would make an `enum`, not a `static final int`; the lesson's own concept 3
is the enumerated type. A fifth quiz item, or a sentence in the exercise's
`why` ("`URGENT_PRIORITY` names it; Section 12.6 would rather it were one
value of a `Priority` enum, so that a `4` cannot be passed by mistake"),
would connect the exercise to the section it otherwise skips.

**13. Lesson 4, quiz item 4 (`7 / 2`) is the lab's `int-division` preset
asked back.** It is correct and its distractors are the three plausible
wrong models (3.5, rounding, a double). A stronger item would be the one
the body explains and the lab cannot show, the intermediate overflow:
"`int seconds = 365 * 24 * 60 * 60; long ms = seconds * 1000;` — what is
`ms`?" (1471228928, because the multiplication is done in `int` before the
widening; fixed by `1000L`). It measures the lesson's own worked
paragraph rather than a preset.

**14. Lesson 3, quiz item 4's distractors "Always" and "Never" are absolutes
a test-wise reader strikes on form.** Replace one with a criterion the
section does not use but a reader might: "When the loop body calls another
routine". The `why` already says how many times a loop runs is not the
criterion; add that what the loop calls is not either.

**15. Lesson 1's "Three of the terms are made up"** (the Data Literacy Test,
p. 238) is a count the accuracy review should confirm against the list; the
pedagogy of the paragraph does not depend on it, but a reader with the book
open will count.

**16. Lesson 6 at phone width:** the lab's "Each global" table scrolls
sideways inside its own box, with the "Written by" and "Access routine"
columns off-screen until scrolled. The page itself does not scroll; it is
the kit's standard treatment, and it is mentioned only so that the author
knows the reader on a phone sees the readers before the writers.

## Checked against the pre-authoring review

- Finding 2 (access routines reaching 0 by dropping routines): taken. The
  records are the same in both presets, `owners` is the only change,
  `dgCoupled` stays 9 and `dgDirectAccess` falls 10 → 3; the body says what
  §13.3 claims and no more.
- Finding 5 (lesson 2's exercise had no answer): taken; answer in quiz
  item 1's `why`, confirmed in the lab.
- Finding 6 (lesson 4's exercise could not be checked in the lab; the
  Standard asked for a wrapped value by hand): taken; the exercise is the
  `+ 3000000` loop, the Standard asks for direction and fix, and `msPerYear`
  is prose with the `1000L` fix.
- Finding 16 (the misconception was true in Java): taken; `mistakes[0]` is
  "if it compiles…", refuted by `set-twice` and by fields, and the exercise
  says plainly that `javac` rejects it and C does not.
- Finding 3 (own-code steps for non-code labs): taken for lessons 4 and 6.
- Finding 33 (the exercise's answer only in a quiz `why`): taken in five
  lessons; lesson 1 leaks it in the `note` (must-fix 3).

## Summary of must-fix items

1. **Re-key the quiz.** All 24 items have `"c": 0` and the renderer renders
   options in order; use the permutation table in finding 1.
2. **Lesson 6, quiz item 4.** The keyed "None" contradicts the lab, which
   counts the loading routine as a writer (4 pairs); make the table a
   `static final` array filled in its declaration, as in finding 2.
3. **Lesson 1.** Remove "the exercise is a case only the compiler sees" from
   the `note` and strip the justification from quiz item 1's correct option,
   as in finding 3.
