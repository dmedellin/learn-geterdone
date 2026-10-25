# Pedagogy review: Course 6, System Considerations (`code-complete-system-considerations`)

Reviewed against `docs/code-complete/PLAN.md` (§0, §B, §C Course 6, §E.4, §F),
`docs/code-complete/AUTHORING.md`, the pre-authoring review
(`docs/reviews/code-complete-spec-pedagogy-review.md`, items 11, 15 and the
"what is right" list), and the author notes from Course 1. Source read:
`content/code_complete/c6_system_considerations/__init__.py` and `part_a.py`,
all four lessons in full.

Method: rendered with `python3 scripts/preview_subject.py code_complete
--course code-complete-system-considerations --out …/pedagogy-c6`, whose last
lines were `4 page(s) executed and swept, 4 with pinned figures, 0 failing`
and `OK`. Opened every page in Playwright (chromium) at 390 px and 1280 px:
no page errors, no horizontal page scroll at either width. Drove every lab
through its presets, through each lesson's exercise, through each quiz item
that can be checked in it, and through malformed input. Ran
`speech.say_code` over every key line, worked line, code line and inline run,
and read the `data-say` attributes the rendered pages carry.

## Verdict

The course does what §C asks and does it honestly. Each lesson states an act
a working programmer can perform (count paths, adjust an estimate, list an
order's stubs and drivers, trace a change through a build), demonstrates it on
a preset, hands it to the reader in an exercise whose answer is withheld until
the quiz, and ends by sending the reader to their own team, estimate, call
graph or build with an observable result. Every pinned figure matched the
lab; every exercise is answerable by hand and checks in the lab as the body
says it will; the misconceptions are the ones the chapters argue against and
the refutations lean on the lesson's illustration and say so. The material
clause holds throughout: no tile or sentence calls a number a verdict, and
each lesson's `note` says what its lab cannot settle.

Three things must be fixed before it ships: a read-out defect that reads the
course's one formula as "n times, open bracket, n negative" on every page; a
quiz distractor in lesson 1 whose stated derivation does not produce it; and
a distractor in lesson 1 that is a joke option. The rest is should-fix
polish on instructions and phone-width legibility, and a few things to
consider.

## Lesson by lesson

### 1. how-program-size-affects-construction

**Teaches:** yes. The reader leaves able to compute paths, a defect range,
a staff-year range and the spread, and the Standard asks the right extra
thing: say which of the four is a count and which are the book's averages.
The `pjSpread` tile, added after the pre-authoring review, is used as that
review hoped: the body says to "read the spread before anything else" and
treats the order-of-magnitude width as the result, not a failure.

**Exercise:** a team of 6 growing to 12, with the ratio of the two counts
asked for. Answerable by hand; the lab's People box checks it (15, then 66);
the answer appears only in quiz item 1's `why`. It is thin, as the
pre-authoring review warned arithmetic-on-a-figure exercises would be, but
the ratio (4.4) carries the chapter's point and the Own step carries the
applied work.

**Quiz distractors:**
- Item 1 (paths 6 → 12): 12/24 counts people, 30/132 counts ordered pairs,
  36/144 is n². Each is a named error; good.
- Item 2 (200K lines, 2–70 per KLOC): 2–70 is the density; 100–10,000 is the
  16K–64K row; 800–20,000 the 512K-or-more row. Checked against Table 27-1
  (p. 652): all three rows are as the `why` states. Good.
- Item 3 (100K lines, 1,000–20,000 per staff-year): "95 times" is the
  difference, good; "100 to 2,000" multiplies by the spread, good; but
  **"0.05 to 1 staff-year" is not what the `why` says it is.** Dividing the
  size in thousands (100) by the rates gives 100/20,000 = 0.005 and
  100/1,000 = 0.1, not 0.05 and 1. A reader who makes exactly the error the
  `why` names will not find their answer among the options. See MF-2.
- Item 4 (construction's share): "It falls to nothing past 512K lines" is
  McConnell's job-protection joke turned into an option, which §E.4 item 5
  forbids. See MF-3.

**Voice and load:** the opening is the chapter's own question, the one light
remark is McConnell's own (the chart cut off to protect his job, p. 654,
checked), the figures are each marked with their source the first time. The
body is 16 blocks, within range, but the six-section walk plus four tiles is
the heaviest lesson of the four; the "Read the spread before anything else"
paragraph is what keeps it from being a wall of arithmetic. Fine.

**Read-out:** the key block and worked lines have spoken forms and read
well ("paths equal n times n minus 1, divided by 2"; "paths, 50 times 49,
divided by 2, is 1225"). The body prose does not: see MF-1.

**Lab:** the exercise's numbers and both quiz-2 and quiz-3 instances check
in the lab; a non-integer or zero team size is refused with a clear message.
One kit nit: the banner says "1 people have 0 possible communication paths"
(consider, kit).

### 2. managing-construction

**Teaches:** yes. Turning a percentage into a multiplier, multiplying rather
than adding, and reporting the range both ends span is a thing readers get
wrong and the lesson shows them doing it right. The Own step ("take an
estimate you gave recently … write down the adjusted effort beside what the
work actually took") is the best in the course.

**Exercise:** nominal 50, +34 percent and −22 percent. By hand: 1.34 × 0.78
= 1.0452, 52.26 staff-months; in the lab, with the two records typed in, the
tiles print `2613/2500 ≈ 1.05` and `2613/50 = 52.26`. The answer appears
only in quiz item 1's `why`. But the body's instruction ("each as a name, a
comma and its multiplier") does not say that the records are separated by a
semicolon; a reader who types them on two lines, which is the natural thing
in a box that already holds a long line, gets "Entry 1 … has 3 parts". See
SF-1.

**Quiz distractors:**
- Item 1: 56 adds the percentages, 67 drops the tools, 106 adds the
  multipliers. All three are errors a reader makes; the first is the one the
  steps warn about. Good.
- Item 2: 0.29 is the reduction, 1.29 flips the sign, 0.971 takes 2.9
  percent. Good.
- Item 3 (Brooks's law qualified): "never" is the law unqualified; "more
  capable" and "less than half finished" are plausible folk qualifications
  the book does not make (p. 676 checked: partitionable tasks). Good.
- Item 4: each distractor is the opposite of one of the section's
  recommendations. Good.

**Misconceptions:** `mistakes[0]` is "an estimate is a number", refuted by the
range two factors span, as the pre-authoring review asked (item 15); Brooks
is `mistakes[1]` in prose, and the `note` says the lab has no input for team
size. Correct.

**Voice:** two light remarks in one lesson, the woolly mammoth (McConnell's,
p. 662) and the nine women (Brooks's, which the book quotes on p. 676). The
second is an argument as much as a joke, so this is a consider, not a
defect (C-2).

### 3. integration-order

**Teaches:** yes, and this is the lesson where the lab computes something the
reader could not see without it: `risk-first` costs both kinds of
scaffolding, and the body says that is the trade the chapter accepts rather
than a mark against the order. `mistakes[2]` ("the best order is the one with
the least scaffolding") heads off the one misuse the lab invites. The
step-by-step table the kit prints under the tiles ("Stubbed after this
step") is exactly the trace the worked example narrates.

**Exercise:** four Java classes whose calls are the pairs. By hand: app
calls ui and core before either is in (two stubs), core calls store (a
third), no drivers. The lab, with the pairs typed into Calls and `app ui core
store` into the order, prints `3: core, store, ui` and `0: none`, and its
table shows the trace. The body's "in lower case" is needed and present
(`App Ui Core Store` is refused as leaving out every component). But at
phone width lines 9 and 13, the one-line methods, are cut at `Core.` and
`Store`: the very calls the reader is told to read off are hidden behind a
horizontal scroll inside the block. See SF-2.

**Quiz distractors:**
- Item 1 (the exercise): "core, store" forgets ui is called before it
  arrives; "drivers: core, store, ui" is the bottom-up pattern; "stubs:
  store; drivers: core" mixes the two. The `why` names each. Good.
- Item 2 (db integrated first): stub/driver confusion, "nothing" because db
  calls nothing, "both". Each is a distinct wrong model. Good.
- Item 3 (pure top-down's disadvantage): the three distractors are
  top-down's advantages and bottom-up's cost; p. 695 checked. Good.
- Item 4 (when phased might be best): p. 692 checked ("if you're lucky").
  "Any program built daily" is the weakest option in the course: nobody
  holds it. Consider C-3.

**Voice:** the stadium is told as a story with a place in it, the
"dump truck full of stubs" is McConnell's phrase (p. 696, checked), and the
section on the orders is frank that the names are heuristics. Good.

### 4. programming-tools

**Teaches:** yes, within the honest limits the `note` states (the lab follows
the list you type; a real tool compares timestamps). Direct and transitive
dependence are glossed; the worked example's "after" paragraph says the
right thing about why three targets for one header is not waste.

**Exercise:** three makefile lines, `util.c` changes. By hand: util.o, then
app; not main.o. The lab prints `1: util.o` and `2: app, util.o`. The answer
is in quiz item 1's `why` only. Good. Quiz item 2 extends the build by a
line the reader has to write themselves (`test: util.o test.o`) and the lab
confirms `4: app, main.o, test, util.o`; this is the course's best retrieval
item, because it asks the reader to apply the rule to a case not on the page.

**Quiz distractors:**
- Item 1: "util.o only" stops at the direct dependent; "app, main.o and
  util.o" is the header's answer; "util.c and util.o" treats the source as a
  target. Good.
- Item 2: each option adds or drops one target; test.o is the trap and the
  `why` explains why it is not reached. Good.
- Items 3 and 4: Fortran (p. 722) and the five-character rule (p. 722)
  checked. "Only a job that takes longer than writing the script" is a
  real break-even belief; the `why` says the book states no such rule. Good.

**Modern aside:** one paragraph, in the lesson §F.4 names, stating the
book's position with its page (p. 706, "too much of a good thing", checked)
and the later view without settling it. It ties the later practice back to
the lab ("the lab's computation done on every commit"). Correct and well
placed.

### Course home

Outcomes are observable acts; `how_to` carries the attribution and the
"numbers are other people's" sentence; `not_covered` is honest. The course
key line "paths among n people: n·(n − 1)/2" has a spoken form and reads
well. `outcomes[0]` and `footer_lead` do not: see MF-1.

## Findings

### Must-fix

**MF-1. The formula n·(n − 1)/2 is read aloud as "n times, open bracket, n
negative" in prose, then "1)/2" as plain text.** The read-out's island
detection stops at the spaced minus, so the inline run becomes `n·(n −` with
`data-say="n times, open bracket, n negative"`, and the rest of the formula
is left to the browser's voice. Confirmed in the rendered HTML: four such
spans on lesson 1 (concepts[0], the `def` block, the lab paragraph) and one
on every other page of the course, from `footer_lead`; the course page's
`outcomes[0]` has the same run. The key lines are safe because
`content/spoken/code_complete.py` gives them spoken forms, but a spoken form
cannot fix the prose, because the island the renderer looks up is `n·(n −`,
not the whole formula.

*Fix:* keep the formula in the key lines, where it is spoken correctly, and
write it in words everywhere it appears in running prose:

- concepts[0]: "Among n people there are n·(n − 1)/2 of them" → "Among n
  people there are n times n minus one, halved".
- the `def` block: "so the team has n·(n − 1)/2 paths" → "so the team has n
  times n minus one, halved: ten people have 10 times 9, halved, 45".
- lab paragraph: "Communication paths is n·(n − 1)/2." → "Communication paths
  is the team size times one less, halved."
- `__init__.py` `outcomes[0]`: "Compute the paths among n people as
  n·(n − 1)/2" → "Compute the paths among n people as n times n minus one,
  halved".
- `__init__.py` `footer_lead`: "communication paths as n·(n − 1)/2" →
  "communication paths as the team size times one less, halved".

If the kit engineer would rather fix `speech.islands` so that a spaced minus
inside brackets does not end an island, that is the better long-term fix,
but this course should not wait on it.

**MF-2. Lesson 1, quiz item 3: the distractor "0.05 to 1 staff-year; 20
times" is not produced by the error its `why` names.** "Divides the size in
thousands, not in lines" gives 100/20,000 = 0.005 and 100/1,000 = 0.1. A
reader who makes that error finds no matching option, and a reader who
checks the `why` finds it false. Either figure can be fixed; the simplest is
to make the option what the error gives.

*Fix:* option → "0.005 to 0.1 staff-years; 20 times"; `why` unchanged except
"0.005 to 0.1 divides the size in thousands, not in lines".

**MF-3. Lesson 1, quiz item 4: "It falls to nothing past 512K lines" is a
joke option.** It exists only to let the `why` explain McConnell's
job-protection remark, and §E.4 item 5 forbids distractors that are jokes.
The `why` already names a real misconception the option could carry instead:
that construction's share falling means construction itself shrinks.

*Fix:* option → "It falls, and so does the amount of coding and unit
testing"; `why` → "The book gives as much as 65 percent on small projects
and about 50 on medium ones, falling further on large ones (F1, p. 654),
because other activities grow faster than construction. Construction's own
work grows with the lines; only its share falls. Cutting the chart off at
512K is McConnell's joke about protecting his job, not a claim about the
share." (The last sentence can stay as colour or go.)

### Should-fix

**SF-1. Lesson 2's exercise instruction does not say how to separate the
two records.** "put 50 in the Nominal effort box and the two factors in the
Factors box, each as a name, a comma and its multiplier" is right for one
record; the reader has to infer the semicolon from the preset's text, and the
box shows only the first thirty characters of it at desktop width. Typing
the two on separate lines is refused ("Entry 1 … has 3 parts"), and so is
typing the percentages ("+34%" is not a number), which the exercise's own
wording invites since it states them as percentages.

*Fix:* "… then put 50 in the Nominal effort box and the two factors in the
Factors box, each as a name, a comma and its multiplier, with a semicolon
between the two, as the preset's line shows, to check."

**SF-2. Lesson 3's exercise code is clipped at phone width where the calls
are.** At 390 px the block shows `static void show() { Core.` and
`static void load() { Store` and the rest is behind a horizontal scroll
inside the block. The exercise says "read the calls off the four classes";
the calls on lines 9 and 13 are the ones hidden. Lesson 4's three-line
makefile fits.

*Fix:* put each body on its own line. Without the blank lines between
classes the constant is 21 lines, within the renderer's 30:

```
class App {
    void start() {
        Ui.show();
        Core.load();
    }
}
class Ui {
    static void show() {
        Core.load();
    }
}
class Core {
    static void load() {
        Store.read();
    }
}
class Store {
    static void read() {
    }
}
```

The read-out then says each call on its own numbered line, which is also
clearer than "line 9, static void show core dot load". The comment above
the constant and the pairs it names do not change.

**SF-3. Lesson 1's Own step needs the book's tables, and does not say so.**
"Type your team's size and your project's size … with the book's rows for
that size" assumes the reader has Tables 27-1 and 27-2 to hand. The lesson
quotes three rows of each; a reader with a 30K-line project needs the
16K–64K row (0.5 to 50), which appears on the page only inside a quiz
`why`. Lesson 2's Own step has the same dependence on Table 28-1, but that
lesson quotes five of its factors with both ends, which is enough to start.

*Fix:* steps[4] → "With your copy open at Tables 27-1 and 27-2 (pp. 652–653),
type your team's size, your project's size in thousands of lines and the two
rows for that size into the lab. Note the paths, the defect range and the
staff-year range, and write one sentence comparing the staff-years with what
your project actually took." And steps[1] "Find the rows" could add "both
tables are on pp. 652–653".

**SF-4. Lesson 2, quiz item 1's stem repeats the exercise's instance and
the exercise names the tools factor by percentage; the `why` gives 0.78
without showing where it comes from.** A reader who got 56 (added the
percentages) is told the multipliers are 1.34 and 0.78 but not that 0.78 is
1 − 0.22, which is the step they skipped.

*Fix:* `why` → "The multipliers are 1 + 0.34 = 1.34 and 1 − 0.22 = 0.78, and
1.34 × 0.78 = 1.0452, so …" (and write "is" for "=" if these whys are ever
read aloud; see C-1).

### Consider

**C-1. "=" in quiz `why` text.** The author notes say to write "is" in key
and worked lines because the code reader says "is set to". The quiz whys use
"=" freely ("6 × 5 / 2 = 15 and 12 × 11 / 2 = 66"; "1.34 × 0.78 = 1.0452").
The rendered quiz carries no `data-say`, so these are not read by the
read-out today; if the quiz is ever read aloud they will be read as
"is set to". Low priority; note for whoever wires that up.

**C-2. Two light remarks in lesson 2** (the woolly mammoth, p. 662; the nine
women, p. 676). §F allows one per lesson. The nine-women line is Brooks's
argument as much as his joke and the book quotes it, so it can stay; if one
goes, cut the mammoth, since the point of §28.1 survives without it.

**C-3. Lesson 3, quiz item 4's fourth option** ("Any program built daily")
is not a view anyone holds. A better fourth: "A program whose classes were
each unit-tested first", which is the premise of phased integration and the
one the chapter says is not enough.

**C-4. Lesson 1's exercise could carry one more line of the chapter's
point.** Adding "and how many paths each person has before and after"
(5, then 11) shows that each person's load grows in proportion while the
total grows with the square, which is the sentence the chapter's figure is
drawn to make. It would need a fifth option set or a second quiz item, so
only if the author has room.

**C-5. Table 27-2's nominal figure.** The book prints a nominal productivity
in parentheses beside each range (3,200 at 10K, 2,600 at 100K, 2,000 at
1,000K). The lesson uses only the range ends. A sentence naming the nominal
for one size would give the reader a point inside the order-of-magnitude
range to compare their own record to. Not required; §C does not ask for it.

**C-6. Kit and chrome nits, not the author's:** the scale view's banner
says "1 people have 0 possible communication paths"; the key block wraps at
phone width even for 32-character lines; the integration table's fourth
column is cut at phone width and needs the table's own scroll. None blocks
the lesson.

## What should not be changed

- The `pjSpread` tile and the "read the spread before anything else"
  paragraph: the honest result of the chapter, made the computed thing.
- Lesson 2's `mistakes[0]` and `note`, exactly as the pre-authoring review
  asked: an estimate is a number, refuted by the range, Brooks in prose.
- Lesson 3's `risk-first` preset and `mistakes[2]`: the one place the lab
  shows something a reader could not see unaided, and the warning against
  minimising the count.
- Lesson 4's quiz item 2, which extends the build off the page.
- Every Own step, each phrased as an instruction with a result to write
  down.
- The modern aside, in the lesson §F.4 names, at the book's strength.

## Summary of must-fix items

1. **MF-1:** n·(n − 1)/2 in running prose is read as "n times, open bracket,
   n negative" on every page of the course. Write it in words in lesson 1's
   concepts[0], `def` and lab paragraph, and in the course's `outcomes[0]`
   and `footer_lead`; keep the formula in the key lines, which have spoken
   forms.
2. **MF-2:** lesson 1, quiz 3: the distractor "0.05 to 1 staff-year" is not
   what its `why` says it is; make it "0.005 to 0.1 staff-years; 20 times".
3. **MF-3:** lesson 1, quiz 4: "It falls to nothing past 512K lines" is a
   joke option; replace with "It falls, and so does the amount of coding and
   unit testing" and let the `why` correct it.
