# Pedagogy review: Course 5, Code Improvements (`code-complete-code-improvements`)

Reviewed against `docs/code-complete/PLAN.md` (§0, §B, §C Course 5, §E.4, §F),
`docs/code-complete/AUTHORING.md`, and the pre-authoring review
`docs/reviews/code-complete-spec-pedagogy-review.md`. Every lesson in
`content/code_complete/c5_code_improvements/part_a.py` and `part_b.py` was read
in full; the course was rendered with `preview_subject.py` (final line `OK`,
8 pages executed, 8 with pinned figures, 0 failing) and opened in Playwright at
390 px and 1280 px; each exercise was typed into its lab; the key lines, worked
lines and every backtick run were passed through `speech.say_code`.

## Verdict

The course teaches. Each of the eight lessons sets out the chapter's argument
section by section, in the voice §F asks for, and then makes the reader do one
thing the chapter does: multiply misses, read a routine as an inspector, count
basis tests, list boundary tests, state a hypothesis and halve suspects, measure
a block's In and Out, compute a speedup, count loop passes. Every exercise is
applied and has a determinate answer in exactly one quiz `why`, every last step
sends the reader to their own code or records with an observable result, and
the pre-authoring findings that named this course (3, 4, 8, 10, 11, 13, 23, 29)
have all been taken: `countPassing` and the out-of-bounds `overtime` are the
exercises the earlier review asked for, the `note`s say what the removal product
and the pipeline assume, `pfPareto` is on the speedup view, the no-op line in
`overtime` is a comment, and the Own step is an act in all eight lessons.

One defect must be fixed before the course ships, and it is not in any lesson's
prose: **every one of the 32 quiz items has its correct answer in position 0,
and the renderer does not shuffle choices.** A reader who notices after the
second lesson stops reading the options. The other findings are improvements to
distractors, to one exercise's wording, and to two lessons that ask the reader
to perform an act (inspect; hypothesise) that the lesson never demonstrates
before the exercise.

## Rendering, labs and read-out

- **Phone (390 px) and desktop (1280 px):** no page scrolls horizontally. Code
  blocks and lab tables are wider than the viewport on a phone but scroll inside
  their own box; line numbers stay in the gutter and the "in the block" flags
  of the extract view are readable. The preset `<select>` label is clipped on a
  phone ("Testing only: unit 30, integration 35, syste…"), which is the
  renderer's, not the course's; noted for the renderer owner.
- **Labs, exercised as the exercises ask:** 5.1 `a, 40/100; b, 50/100` gives
  `7/10 = 70%` and three stages at `3/10` give `657/1000 = 65.7%`; 5.3
  `archiveOld` pasted gives Basis 4, points `for line 2, if line 3, || line 3`;
  5.4 `len > 8 && len <= 64` with lo 8, hi 64 gives Disagree 8, Tests
  `7, 8, 9, 63, 64, 65`, Exposed 8, and the corrected `>=` gives none; 5.6
  `printInvoice` lines 2–5 give In `inv`, Out `subtotal`, lines 7–9 In
  `subtotal, tax`, Out none; 5.7 `hot, 95, 1; rest, 5, 1000` gives Saved
  `999/20000 ≈ 5.0%` and `hot, 95, 2; rest, 5, 1` gives `19/40 = 47.5%`; 5.5
  and 5.8 presets print the figures the prose names. Every answer in the quiz
  `why`s matches what the lab prints. Two things a reader will meet: 5.1
  refuses `40%` ("should be a number such as 3, 1/2 or 0.25") though the lesson
  says "percent" throughout (finding 7), and 5.4 refuses
  `password.length() > 8` with "The check has '.', which this lab cannot read"
  (the exercise's `len` works, and the refusal explains itself).
- **Read-out:** every key line, worked line and backtick run reads correctly
  with the code dialect: `&&` as "and", `||` as "or", `i <= scores.length` as
  "i is at most scores dot length", `count++` as "count is incremented",
  `staff[i]` as "staff at index i", `printTotals(fees, balance)` as "print
  totals of fees, balance". No `=` is read "is set to", no thousands comma, no
  `%` in a spoken line. Two identifiers are left to the synthesiser: `IBM`
  (5.2 key line) and `qty` (5.4 key line); see finding 11.
- **Quiz, as rendered:** 5.3's first item shows its choices as `4, 3, 2, 5`,
  i.e. in source order; the quiz script (`render()` in the page) builds the
  buttons from `q.a` in order and compares the click index to `q.c`. Course 1
  sets `c` to 1, 2 or 3 in nine of its twelve items; Courses 2–4 spread it
  42/27/14/5 across the four positions; this course sets it to 0 in all 32.

## Findings

### Must-fix

**1. The correct answer is always the first option, in all 32 items.**
*Where:* every `"c": 0` in `part_a.py` and `part_b.py`; the renderer presents
`a` in source order. *What is wrong:* retrieval practice that can be passed
without retrieval teaches nothing and, worse, teaches the reader that the quiz
is decorative. The `why`s are good, and they are only read after a choice.
*Change:* permute the options of each item so that the correct answer sits in
each of the four positions roughly equally across the course, and set `c` to
match. A permutation that keeps each item's own logic (the off-by-one next to
the answer, the misconception last) is below; the `why` text does not change,
since each `why` names the wrong figures rather than their letters.

| lesson | item 1 | item 2 | item 3 | item 4 |
| --- | --- | --- | --- | --- |
| 5.1 | c = 2 (`A 20%, B 2.7%`, `A 90%, B 90%`, **`A 70%, B 65.7%`**, `A 70%, B 90%`) | c = 1 | c = 3 | c = 0 |
| 5.2 | c = 1 | c = 2 | c = 3 (`30`, `28`, `18`, **`12`**) | c = 0 |
| 5.3 | c = 3 (`3`, `2`, `5`, **`4`**) | c = 0 | c = 2 (`5`, `4`, **`6`**, `7`) | c = 1 |
| 5.4 | c = 1 (`8 and 64`, **`8 only`**, `64 only`, `7 and 65`) | c = 3 | c = 0 | c = 2 |
| 5.5 | c = 2 (`Line 5, with i == 4`, `Line 4, with i == 5`, **`Line 4, with i == 4`**, `Line 9, with i == 3`) | c = 1 | c = 0 | c = 3 |
| 5.6 | c = 3 | c = 0 | c = 1 | c = 2 (`Changing the fee from 25.0 to 30.0`, `Charging the fee only once per statement`, **`Replacing the literal 25.0 with a named constant OVERDRAFT_FEE`**, `Printing the number of overdrafts as well`) |
| 5.7 | c = 1 | c = 3 (`900 ms`, `100 ms`, `990 ms`, **`910 ms`**) | c = 2 | c = 0 |
| 5.8 | c = 0 | c = 2 (`1,000`, `1,022`, **`1,550`**, `62`) | c = 1 | c = 3 |

The bracketed lists show the four items where the order of the distractors
matters to the reading (the off-by-one beside the answer); the rest are a plain
rotation. Add one sentence to `AUTHORING.md`'s loop step 7 for the remaining
courses: "spread `c` over the four positions; the renderer shows the options in
source order."

### Should-fix

**2. 5.2, quiz item 1: the correct option is the long one.** *Where:*
`collaborative-construction`, quiz 1. *What is wrong:* the answer lists three
defects in a 30-word option; the three distractors are two-item or one-item
lists, each with one false claim. A reader who knows nothing picks the longest
and most specific option and is right. Each option should be a three-item list
with exactly one item wrong, so that the reader has to check each line.
*Replacement options* (correct first; then apply finding 1):

- "Line 3 starts `count` at 1; line 5 uses `>` where the comment promises at
  or above; the parameter `maxScore` on line 2 is never used"
- "Line 3 starts `count` at 1; line 4 should loop while `i <= scores.length`;
  the parameter `maxScore` on line 2 is never used"
- "Line 3 starts `count` at 1; line 5 uses `>` where the comment promises at
  or above; line 6 should be `count++`"
- "Line 2 should take `scores.length` as a parameter; line 5 uses `>` where
  the comment promises at or above; the parameter `maxScore` is never used"

*`why` addition*, after "and `count = count + 1` and `count++` do the same":
"and an array carries its own length in Java, so a length parameter would be a
fourth parameter nobody needs, not a fix."

**3. 5.6: the exercise has more right answers than its quiz accepts.**
*Where:* `refactoring-safely`, exercise `p` ("Find two blocks of
`printInvoice` that extract cleanly") and quiz 1. *What is wrong:* lines 2–5
and 7–9 are the intended pair, but lines 3–5 (In `inv, subtotal`, Out
`subtotal`: `subtotal = addLines(inv, subtotal)`) and lines 6–9 (In
`subtotal, inv`, Out none: `printTotals(inv, subtotal)`) also extract cleanly,
and the lab confirms both. A reader who finds 6–9 has done the lesson's act
correctly and is then marked wrong by an item that asks only about 2–5 and 7–9.
*Change:* make the exercise name the two candidate blocks and add the judgment
the lesson is actually about, so the answer is determinate and the reader still
decides something:

> "Two extractions are proposed for `printInvoice`: lines 2 to 5 as a routine
> that totals the lines, and lines 7 to 9 as a routine that prints. For each,
> give its In, its Out and the call that would replace it. Then say whether
> lines 2 to 6, the total and the tax together, would extract as cleanly, and
> why. To check, paste the routine into the lab and set From and To."

*Quiz 1 stem* stays; *`why` addition*: "Lines 2 to 6 would not: they set both
`subtotal` and `tax`, and both are read on lines 7 to 9, so a Java method could
return only one of them. Lines 6 to 9 together would extract cleanly too, as
`printTotals(inv, subtotal)` computing the tax inside; the lesson's pair keeps
the tax where the caller can see it."

**4. 5.8, quiz item 4 has a joke distractor.** *Where:*
`code-tuning-techniques`, quiz 4, option "They are refactorings that happen to
run backwards in time". §E.4 item 5 forbids it, and it also makes the item a
three-option item. *Replacement:* "They make the code faster without changing
its internal structure" (wrong on the row the stem is about: the chapter's
definition is that the structure gets worse). Option C, "They undo the
refactorings of Chapter 24 one by one", is arguable as a reading of the prefix
"anti-"; keep it, since the `why` answers it ("degrade it in exchange for
performance, by definition").

**5. 5.5 asks for a hypothesis and a deciding test without ever showing one
made on code.** *Where:* `debugging-as-science`. The worked example is the
halving arithmetic (`commit-637`), the steps name the act, and the exercise
asks for a hypothesis, the deciding test and the line on `overtimePay`. The
reader goes from a description of the method to performing it with no
demonstration between. *Change:* one `p` after the "Most of Section 23.2 is
tips" paragraph, worked on a snippet the reader has already met:

> "Watch the method on something small. `shippingLabel`, from Structured Basis
> Testing, is reported to return an empty label for some orders. The data: it
> happens for a few zones and never with `express` set either way. A hypothesis
> that accounts for it: the zone is one the `switch` does not name, so `label`
> keeps its starting value. The experiment that decides it: call with zone 4,
> which should fail, and zone 3, which should pass; if zone 3 also fails, the
> hypothesis is wrong and the `switch` is cleared as a suspect. One call
> each way settles it, and the line is 2, where the empty string is set. That
> is the whole method, and the only difference at scale is how many suspects
> each test clears."

This keeps the body at 14 blocks, under the ceiling.

**6. 5.2's step 2 is the exercise's answer key, and the only demonstration of
inspecting.** *Where:* `collaborative-construction`, steps 1–2 ("For each
variable, ask where it is set first and whether that value is right; for each
comparison, whether it should include its boundary; for each parameter, whether
it is used"). *What is wrong:* the three questions are the three planted
defects in order; a reader who reads the steps before the exercise (they are on
the same page) has only to apply them one to one. The scaffold should be a
checklist a reader could use on any routine, so that choosing which questions
bite on `countPassing` is still the reader's work. *Replacement step 2:*

> ("Ask the checklist's questions", "The chapter's checklist asks, among other
> things: for each variable, where it is first set and whether that is the
> right start; for each comparison, whether the boundary belongs inside or
> outside; for each loop, whether it ends and where its index is when it does;
> for each parameter, whether it is used and whether the caller could pass a
> value the routine does not expect; for the return value, whether every path
> sets it. Ask all of them, and keep only the ones that bite.")

### Consider

**7. 5.1's exercise says "percent" and the lab refuses `40%`.** Add to the
exercise `p`: "…type each pipeline into the lab's stages box, with any stage
names and the rates as fractions or decimals (`40/100` or `0.4`), to check your
figures."

**8. 5.3, quiz item 1 `why` explains 3 and 2 but not 5.** Add: "Five adds one
for the `i++` in the loop header or for the array index, neither of which is a
decision."

**9. 5.7, quiz item 4 stem is not a question.** "The chapter's approach to
code tuning (Section 25.6) says what to do with a change that does not make the
measured time fall?" → "By the chapter's approach to code tuning (Section
25.6), what do you do with a change that does not make the measured time
fall?"

**10. 5.1 says "averages from other people's projects" four times** (body
§20.3 paragraph, `mistakes[2]`, step 5, `note`). §F.5 asks for it once where
the lesson leans on a figure. Keep the body sentence and the `note`; cut the
clause from step 5 ("Then write one sentence saying the rates are averages from
other people's projects, and" → "Then") and shorten `mistakes[2]` to its last
two sentences.

**11. Two key lines depend on the synthesiser.** `IBM: 3.5 hours by
inspection, 15–25 testing` is read "ibm"; `qty < 99 is wrong at 99 only` is
read "qty". If the operator's voice spells neither, write "at IBM" as "at I B
M" in the spoken override file, and change the key line to `quantity < 99 is
wrong at 99 only` (the lab's variable stays `qty`; the key line is prose).

**12. 5.1, quiz item 4: option B is close to the answer.** "The three stages
find different kinds of defect from one another" is what a reader who absorbed
the `note` might reasonably call the independence assumption. The `why` does
separate them ("like stages multiply exactly as unlike ones do"), so the item
is fair; if it is kept, the stem could say "Which assumption does the
*arithmetic* rest on?" to point at the product rather than the chapter.

**13. The `math` block as an exercise.** 5.1 and 5.7 lay out the exercise's
figures in a `math` block (the worked-lines style). §E.4 item 4 says "a `code`
block (or a small table)" and the Course 1 notes allow a `ul`. It renders well
and reads well; record it as a third accepted shape in §E.4 rather than change
it.

## What the course does well, and should not be changed

- The exercises are the chapter's acts, not the lab's arithmetic again:
  inspection (5.2), the out-of-bounds hypothesis (5.5), the hoisted call (5.8).
  The earlier review asked for exactly these and the author delivered them.
- The `note`s are honest about what each model cannot show: the independence
  of misses (5.1), hours that scale with defects found (5.2), case labels that
  fall through (5.3), one integer variable (5.4), tests that decide cleanly
  (5.5), calls not followed (5.6), times that simply add (5.7), passes not
  time (5.8). Nothing in the course calls a count a verdict.
- The scene openings are rationed to four of eight (5.3, 5.5, 5.6, 5.7), the
  modern aside is in 5.3 only and stated as a continuation, the one history per
  lesson has people in it (Weinberg and Schulman, Fagan, Gould, Constantine,
  Knuth), and the light remarks are McConnell's own (weighing yourself more
  often; the hairy name; Jackson's rules).
- 5.3's "coverage tool's verdict" paragraph is the best misconception handling
  in the course: a concrete call, full statement coverage, two of five outcomes
  untried, and the reader can check it against the listing.
- The quiz `why`s address the specific wrong figure in every item.

## Summary of must-fix findings

1. Every quiz item in the course has its correct answer first and the renderer
   does not shuffle; rotate `c` across the four positions as the table in
   finding 1 gives, and tell the remaining authors.

Should-fix 2–6 (the long-option tell in 5.2, the under-determined exercise in
5.6, the joke distractor in 5.8, a demonstration of the hypothesis step in 5.5,
and a checklist rather than an answer key in 5.2's steps) can be taken in the
same revision; none changes a snippet, a preset or a pinned figure.
