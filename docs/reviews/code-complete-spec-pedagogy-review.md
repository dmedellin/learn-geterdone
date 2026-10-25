# Pre-authoring pedagogy review: Code Complete (`docs/code-complete/PLAN.md`)

Reviewed 2026-10-25 on branch `feat/code-complete-subject`, against the
`pedagogical-expert` brief (observable objectives, prerequisite order, cognitive
load, worked-example progression, retrieval practice, misconceptions), `AGENTS.md`
§0 and §1a, `content/AGENTS.md`, the enforced lesson shape in
`docs/philosophy/PLAN.md` §E (three concepts, 4–5 steps, 3–4 quiz items, three
mistakes, body 7–18 blocks), and the operator's brief for this Subject: a
read-along like Capital and Phenomenology, leaning on applied exercises because
the book is a practical handbook. Nothing has been authored; this judges the
specification. Written independently of the accuracy review. The book's text
reached the scratchpad during the review; where a finding below rests on what a
chapter says, it was checked against the page and says so, and nothing from the
text is reproduced here.

Every figure in §C that a finding depends on was recomputed by hand from the
§D.4 snippet or the stated instance: the span and live-time instance, the
decision points and depth of all four complexity/basis snippets, the
coupled-pair count of `globals`, the stairs and bisect traces, the chain,
pipeline, speedup and nested-loop arithmetic, and the layout depths. All of them
check. The findings are about what the lessons teach, not whether they add up.

## Verdict

This is a stronger specification than either earlier read-along was at the same
stage. §0 is honest about its three families of computation; the material clause
("a count is a reason to look, not a verdict") is right for the book and the kit
is forbidden to print a verdict; every lesson has a Do, a Standard and an
Exercise; the exemplary paragraph is the right register; the counting rule for
decision points is the book's own (checked: 1, plus each `if`, `while`, `for`,
`and`, `or`, and each `case`); and about half the lessons turn on a genuinely
non-obvious computed result (`scope-span-and-live-time`,
`design-heuristics-and-information-hiding`, `nesting-and-complexity`,
`refactoring-safely`, `layout-and-style`, `integration-order`,
`table-driven-methods`, `boolean-expressions`).

It is not yet the applied Subject the operator asked for. About a third of the
exercises are arithmetic on a stated figure (multiply three COCOMO factors,
divide 10,000 by 2.5, halve a thousand commits ten times) that no working
programmer does on their own code; one exercise is the lesson's own worked
example repeated; three have no answer; one cannot be checked in the lab the
lesson gives it. The two chapters most about practice, Collaborative
Construction and Debugging, have no exercise in which the reader reviews or
debugs anything. One lab manufactures its result by changing the population
between presets (`structures-pointers-and-global-data`). Two misconceptions are
the later, disputed view that §F.4 says must be presented and not settled, put in
the one slot that settles by construction; one misconception is true for the
language the lessons use. The own-code step that §B promises for every lesson
is specified only for the 18 lessons whose view takes code. Chapter 8 is one
15-minute lesson carrying eight sections and two hard ideas. And the read-out,
once R2 lands, will still read a listing without its line numbers to a listener
whose lesson says "line 14".

All of this is fixable in the specification without changing the shape of the
Subject. The recommendation is **revise before authoring**, with findings 1–7
must-fix.

## Findings

### A. Do the exercises build the skill?

**1. MUST-FIX — `reasons-to-create-a-routine`: the exercise is the worked
example, and the chapter's hardest idea has no exercise at all.** *Where:*
Course 2.5. *What is wrong:* the Exercise is "the `copied` listing — name the
routine (`printAddress`), its parameter, and the lines that remain", and the
Worked line two bullets above has already said "`printAddress(Address a)`
replaces them". The reader is asked to recall what the page just told them.
Meanwhile §7.2's cohesion (functional, sequential, communicational, temporal,
procedural, logical, coincidental — checked against the chapter's list) is the
one idea in Chapter 7 that a working programmer gets wrong daily and cannot see
by counting, and the lesson's Do does not mention it. *Change:* (a) the
Exercise becomes a classification: six one-line routine descriptions
(e.g. "computes age and retirement date from a birth date", "prints the report
and resets the totals", "handles every kind of input depending on a flag"),
and the reader names each one's cohesion kind and rewrites the header of the
weakest into two routines; the answer goes in a quiz `why`. (b) `code/dupes`
keeps its lab role, with a *fresh* duplicate-block snippet for a second,
shorter exercise (a `printSummary` that formats two totals the same way twice;
answer: one block, lines n–m, `printMoney(double amount, String label)`).
(c) Reorder the presets `copied`, `extracted`, `two-names`: the lab's limit (a
renamed copy it cannot see) is the last thing shown, not the first. *Priority:
must-fix.*

**2. MUST-FIX — `structures-pointers-and-global-data`: the `access-routines`
preset reaches 0 coupled pairs by deleting the six routines from the table.**
*Where:* Course 3.6; `deps/shared`. *What is wrong:* `globals` lists six
routines and three globals and counts 9 coupled pairs of 15. `access-routines`
lists only the three new access routines and counts 0 — but `readInput`,
`validate`, `report`, `reset`, `addLine` and `printTotals` still exist and now
call `currentRecord()`; the coupling the chapter is about has moved behind a
routine, not vanished. The lab prints the chapter's conclusion because the
preset changed what was counted. This is the Phenomenology finding-1 pattern
(a scoreboard on which the book's view wins because the lesson coded it so),
and it is the one place in this specification where a reader who thinks about
the result will catch the Subject cheating. *Change:* `access-routines` keeps
all six routines, each now accessing the global through its access routine
(records `readInput, w, current` become `readInput, w, current` *via*
`currentRecord`, or simpler: keep the records and add a cfg key `owners:
current=currentRecord; errors=errorLog; total=runningTotal`). The tile that
changes is a new `dgWriters` ("current: 2 routines" → "current: 1 routine,
currentRecord") and `dgCoupled` stays 9. The body then says what the chapter
says (checked, §13.3): access routines give each global one owner, a single
point of change and a place to check its value; they do not uncouple the
routines that use it. The misconception ("global data is fine as long as it
is only read") survives unchanged and is refuted by `globals`. *Priority:
must-fix.*

**3. MUST-FIX — the own-code step exists for 18 lessons and is promised for
41.** *Where:* §B "Every lesson ends by sending the reader to their own code…
pasted into the lab where the view takes code". *What is wrong:* 23 lessons
use a family-2 or family-3 view that takes names, records or figures, and the
specification says nothing about what their last `step` sends the reader to
do. An author will write "think about your own project" 23 times, which is not
an act. *Change:* add to each non-code entry a one-line **Own:** item, the act
and the input. Proposed: 1.1 last week's calendar, classified by the chapter's
list; 1.2 and 2.2 five dependencies from the reader's own build; 1.3 the last
five bugs in the reader's tracker, by where introduced and where found (the
lab's cost table on them); 1.4 the reader's own language's ratio and a day's
real output; 2.1 the modules of one package and who imports whom; 2.4 one
inheritance chain from the reader's codebase, child–parent pairs; 2.7 and 5.4
a validation check from the reader's code with its documented range; 4.2 an
`if-else-if` chain from the reader's code with frequencies from a log or a
guess, and the sentence that says which; 4.3 four loop headers from the
reader's code; 4.4 one recursive routine of the reader's, its depth bound; 4.5
one lookup table of the reader's, its endpoint rule; 4.6 a negated condition
from the reader's code; 5.1 and 5.2 the reader's team's actual stages, with the
book's modal rates and the sentence that they are averages; 5.5 the reader's
last bisection, how many steps it took against ⌈log₂ n⌉; 5.7 a profile the
reader has taken; 5.8 one loop nest of the reader's with its sizes; 6.1 the
reader's team size; 6.2 the reader's last estimate and which two factors they
would have applied; 6.3 the call graph of one feature; 6.4 one build target's
prerequisites; 7.3 one task the reader repeats weekly. *Priority: must-fix
(it is the Subject's own promise).*

**4. SHOULD-FIX — `collaborative-construction` and `debugging-as-science`:
the two chapters about doing something have exercises in which nothing is
done.** *Where:* Course 5.2 (Exercise: "50 defects, code review 50% at 3 h,
testing 50% at 12 h → … 6 hours per defect") and 5.5 (Exercise: "a defect in
1,048,576 lines: at most 20 halvings"). *What is wrong:* a programmer who has
done both exercises has reviewed no code and debugged nothing. The operator's
brief is applied exercises; these are the two places where "find the defect"
is the chapter's own subject. *Change:* keep each lab (the arithmetic is
legitimate family-3 work) and replace the exercise. 5.2: a 14-line snippet
written for the lesson with three planted defects of the kinds the chapter's
inspection checklist names (named, not reproduced: an uninitialised
accumulator, a `<` that should be `<=`, a parameter unused) and the
instruction "read it as the inspection's reader role would, and list what you
would raise"; the answer in a quiz `why` names the three lines. 5.5: a
12-line routine, a failing input, and the chapter's method as the steps —
"state the hypothesis, name the one test that halves the suspects, name the
line"; a good candidate is the `overtime` snippet itself, whose
`while (i < count && staff[i] != null)` throws when `count` exceeds
`staff.length` (a defect §D.4 does not mention, and which the second review
would otherwise find as a fault in a lesson that claims the snippet is wrong
in no other way). *Priority: should-fix.*

**5. SHOULD-FIX — exercises with no determinate answer, where §B says the
answer is in §C.** *Where:* `design-challenges-and-complexity` ("redraw as
three layers and count again"), `scope-span-and-live-time` ("move both
declarations below the four `print…` calls and recompute"),
`organizing-straight-line-code` ("rewrite `hidden` so each call takes the
result of the previous one, and list the dependencies the lab then finds"),
`themes-of-craftsmanship` (the reader's own routine; acceptable, because the
Standard uses `retry-delay`). *Change:* give each its answer. 2.1: the layered
instance is `ui, orders; ui, billing; orders, stock; billing, stock; stock, db`
→ 5 of 15 pairs, 1/3 ≈ 33.3%, `dgFanIn` stock 2 (or whatever the author
chooses; it must be written down). 3.2: declarations on lines 6 and 7 (after
four prints on 2–5) give `total` 6, 9, 12 and `count` 7, 10, 12 → spans 2, 2,
2, 1, average 7/4 = 1.75, live times 7 and 6. 4.1: the model rewrite is
`Marketing m = ledger.computeMarketing(); Sales s = ledger.computeSales(m);
Travel t = ledger.computeTravel(s); ledger.printReport(t);` → `coDeps`
"1→2, 2→3, 3→4" — and the body should say this is the chapter's own remedy
(make the order visible in the parameters), which is why the lab now sees it.
*Priority: should-fix.*

**6. SHOULD-FIX — `integers-and-floating-point`: the exercise cannot be
checked in the lab, and the Standard asks for arithmetic the lab exists to
do.** *Where:* Course 3.4; `run/arith` is `acc = start; repeat times: acc op
operand` with one operand. *What is wrong:* the exercise `365 * 24 * 60 * 60 *
1000` is a chain of four different multiplications; the view cannot express
it, so "the lab may be used to check the answer afterwards" (§B) is false
here. The Standard asks the reader to compute "the wrapped value" of an `int`
product by hand; 46341² mod 2³² by hand is not a 15-minute skill and is not
the chapter's point. *Change:* (a) the exercise becomes one the view can
show: `int total = 0; for 1,000 iterations total += 3000000;` → exact
3,000,000,000, Java `-1294967296` (start 0, `+`, 3000000, times 1000); keep
`msPerYear` as a second, prose-only example with the `1000L` fix. (b) The
Standard: "say whether the product overflows and in which direction, name the
fix (`long`, or a `long` literal), and for a decimal fraction added ten times
as `double` say whether the result equals the exact one and why". *Priority:
should-fix.*

**7. SHOULD-FIX — `the-pseudocode-programming-process`: the exercise's
obvious fix is itself a defect in Java.** *Where:* Course 2.8, `expireSessions`
(§D.4): the empty step is "remove it from the live list" inside
`for (Session s : sessions)`. *What is wrong:* the code a reader writes under
that comment — `sessions.remove(s);` — throws `ConcurrentModificationException`
on the next iteration in every standard `List`. A lesson that asks "name the
code that is missing" and accepts that answer teaches a bug; one that rejects
it without saying why is unfair. *Change:* either change the loop to iterate
over a copy (`for (Session s : new ArrayList<Session>(sessions))`) or over an
`Iterator` with `it.remove()`, or keep the snippet and make the Java gotcha
the second half of the exercise ("the one-line fix throws; what does the
step need?"), with the answer in the quiz `why`. The second is the better
lesson, and it is exactly the kind of language difference the prerequisites
promise to flag. *Priority: should-fix.*

**8. SHOULD-FIX — exercises that are arithmetic on a stated figure, where
the chapter has an act the reader could perform instead.** Not every lesson
can be applied — Chapters 1, 3, 20, 27 and 28 have no code in them — but
these four can be:
- `key-construction-decisions` (1.4): §4.3, programming *into* a language,
  is the chapter's one idea a programmer uses daily (checked: the chapter's
  own example is a convention adopted to give Visual Basic a separation it
  lacked). *Change:* keep `project/language` as the lab, and make the exercise
  a judgement: three short descriptions of a language lacking a facility
  (no assertions, no enumerated types, no access control) and the reader
  writes the one-line convention that supplies it; answer in the `why`.
- `unusual-control-structures` (4.4): the lab counts calls of naive
  Fibonacci, which the chapter does say not to write recursively (checked,
  §17.2), but §17.1's guard clauses are the technique the reader will use
  tomorrow, and the specification teaches them in 4.7 instead. *Change:* the
  exercise is a guard-clause rewrite — a 10-line routine with two nested
  `if`s and a `return` at the bottom, rewritten with early returns; answer the
  rewritten header and body, and the sentence that the decision points do
  not change, which 4.7 then counts.
- `code-tuning-techniques` (5.8): Chapter 26 is a catalogue of code
  transformations and the lab counts loop headers. *Change:* the exercise is
  one transformation: a loop with a loop-invariant call inside
  (`for (…) { double rate = config.taxRate(); … }`) or an `if` inside a loop
  that does not depend on the index (unswitching); the reader writes the
  moved version and states body executions before and after for n = 1,000.
- `using-conditionals` (4.2): the Exercise is the lab's arithmetic again.
  *Change:* add the chapter's other point (checked, §15.1: cover all cases;
  the final `else` for the error case): a four-branch chain classifying a
  request method with no final `else`; the reader names the input that falls
  through, and the branch that should catch it.
*Priority: should-fix.*

### B. Labs that compute something, and labs that restate the lesson

**9. SHOULD-FIX — `key-construction-decisions`: the `rate` input adds a
decorative tile.** *Where:* Course 1.4; `project/language` tiles `pjDays`,
`pjDaysC`. *What is wrong:* `pjDays / pjDaysC = 1 / ratio` identically: "80
days against 200" is the ratio 2.5 again, dressed as a schedule, computed from
a rate the lesson admits is "an assumption, not a law". A reader will take 80
days as a prediction. *Change:* drop `rate`, `pjDays` and `pjDaysC`; keep
`pjEquivalent` and add `pjNotMeasured` as a fixed sentence in the banner
("the ratio measures statements, not time, defects or the team's experience")
— or better, since a fixed string is not a computation, keep the view to one
tile and let the lesson's prose carry the caveat. *Priority: should-fix.*

**10. SHOULD-FIX — `the-software-quality-landscape`: the lab's model cannot
show the argument the misconception says it shows.** *Where:* Course 5.1;
`defects/removal`; Misconception: "the lab's product shows why combining
unlike techniques is the argument". *What is wrong:* the product of
independent rates is the same for two *like* techniques as for two *unlike*
ones — two 40% stages give 64% whichever they are. The chapter's claim (after
Jones; §S.2 F17) is that unlike techniques find different defects; the
independence model is exactly the assumption under which kind does not
matter. *Change:* the misconception's refutation says what the lab shows —
that no single stage at the book's modal rates reaches the chapter's target,
so a second is needed — and the `note` says the "unlike" part is the
chapter's claim, from Jones's data, which a product of independent rates
cannot test. *Priority: should-fix.*

**11. SHOULD-FIX — `collaborative-construction`: the pipeline's hidden
assumption makes inspections cheap by construction.** *Where:* Course 5.2;
`defects/pipeline`, hours *per defect found*. *What is wrong:* testing's
hours in the model scale with the defects that reach it, so inserting an
inspection first cuts testing's cost automatically. Test suites are not
costed that way: the suite runs whether or not it finds anything. The lesson
then says "the pipeline counts the hours", which it does only under that
assumption. *Change:* the `note` names the assumption in one sentence and
says what it leaves out; the preset labels say "hours per defect found, as
the book reports them"; and the misconception's refutation leans on the
book's reported hours (F18), not on the model's total. *Priority:
should-fix.*

**12. SHOULD-FIX — `self-documenting-code`: `coDensity`'s denominator is
not the study's.** *Where:* Course 7.2; `code/size` `coDensity` = comment
lines / code lines, where code lines include the header and every brace-only
line. *What is wrong:* the figure the lesson sets it against (F28, checked:
roughly one comment every ten *statements*) is per statement. On
`comments-repeat`, "a comment over every line" gives 5 comments over 5
statements — a density of 100% by the study's measure — and the tile prints
71.4% because two of the seven "code lines" are braces. The exercise's
`isLeapYear` "2/3" has a `}` in the denominator. *Change:* `coDensity` is
comment lines over *statement* lines (the kit already defines a statement
line); the lesson says so. *Priority: should-fix (a kit change, small).*

**13. SHOULD-FIX — `code-tuning-strategies` never shows the Pareto tile the
chapter is about.** *Where:* Course 5.7 uses `profile/speedup`; `pfPareto`
("6 of 8 entries reach 4/5 of the total") lives only in `profile/shares`, which
Course 1.1 uses for hours. *What is wrong:* §25.2's 80/20 (F22) is the
chapter's opening claim and the one tile that computes it appears in a
lesson about project hours. *Change:* give `speedup` the `pfPareto` tile too
(the records already carry the times): on the illustrative profile "1 of 4
routines reaches 3/5 of the time". *Priority: should-fix.*

**14. CONSIDER — labs that are counts of the obvious.** These are
acceptable because their chapters have no quantity, and the review records
them so that nobody mistakes them for the Subject's spine: `deps/tree` depth
(2.4; the LSP prose question is the real exercise), `code/size` parameters
(2.6; a parameter count is visible without a lab, and the exercise is the
lesson), `code/class` (2.3; the misconception itself says the count is not
the test — the exercise should add "group `kitchen-sink`'s six public
routines into the classes they belong to"), `project/scale` (6.1; the ranges
are so wide that a `pjSpread` tile, high/low, would make the width the
computed thing, which is the chapter's honest point), `project/breakeven`
(7.3; the lesson's own model, labelled so, and honest about `rare-task`).
`deps/ripple` is used three times (1.2, 2.2, 6.4); 2.2 is the one that earns
it (the transitive count *rises* while the direct count falls, which is a
real result). In 1.2 it is a stretch from the chapter: the lab tests the
building metaphor's prediction, which is fine if the body says that is all
it does.

### C. Misconceptions

**15. MUST-FIX — the disputed later view is in the slot that refutes.**
*Where:* `upstream-prerequisites` (1.3: "Prerequisites belong to waterfall;
an iterative team can skip them") and `routine-length-and-parameters` (2.6:
"Shorter is always better"), both marked as the course's §F.4 home. *What is
wrong:* §F.4 says the later view is stated at strength and "the lesson does
not settle it"; `mistakes[0]` is by contract the wrong model, named and
refuted. Putting the short-function school in `mistakes[0]` settles it
against them in the lesson's own voice, which is the thing Capital's second
review forbade. 2.6 also puts the modern aside in the misconception rather
than in the `note` or a late `p`, which §F.4 requires. *Change:* 1.3's
`mistakes[0]` becomes a misreading the chapter itself refutes — "the cost
table says every project should finish its requirements before coding"
(checked: §3.2 argues the opposite for iterative kinds) — and the agile view
goes in the `note`, at strength, unsettled. 2.6's `mistakes[0]` becomes one
the chapter is firm on: "parameters are whatever is convenient to pass, in
any order" or "a function that returns a value and also changes state is
fine" (§7.6); the short-function school goes in the `note`. Add a sentence
to §C's preamble: a misconception is never the view named as the course's
§F.4 aside. *Priority: must-fix (voice contract).*

**16. MUST-FIX — `declaring-and-initializing-variables`: the misconception
is true in Java.** *Where:* Course 3.1: "The compiler catches uninitialised
variables." *What is wrong:* for local variables, `javac` does — definite
assignment is path-sensitive, and it rejects the lesson's own exercise
(`result` not definitely assigned on the `false` path of the `if`), which the
entry presents as a case "the lab's top-to-bottom reading misses" as if the
reader alone catches it. A Java reader who holds the "misconception" is
right, and the Standard ("say which the compiler would catch") gets a
different answer from the one the entry implies. *Change:* `mistakes[0]`
becomes "If it compiles, every variable holds the value you meant", refuted
by `set-twice` (a value overwritten before it is read) and by fields, which
default silently (a short `Counter` class with `int count;` as a field, read
before any set — the lab reports it, `javac` does not). The exercise keeps
the path-sensitive case but says plainly that `javac` rejects it and C and
C++ do not, and that the lab, like C, reads top to bottom. The lesson's
`note` then names the lab's limit truthfully: it is weaker than Java's
compiler on locals and useful on fields and on the set-twice and never-used
anomalies. *Priority: must-fix (a false statement about the language).*

**17. SHOULD-FIX — straw men and holders.**
- `metaphors-for-software` (1.2): "Software is soft, so nothing about it is
  expensive to change" has no holder. The chapter's own target (checked,
  §2.3) is the writing metaphor — one author, a draft, throw it away —
  which it calls inadequate for anything beyond a small project. *Change:*
  "Writing software is like writing a letter: sit down, write it, and if it
  is wrong, throw it away and start again." Refuted by the chapter's
  building and accretion metaphors, with the lab's count of what rests on the
  schema as the illustration.
- `key-construction-decisions` (1.4): "Choose the language that needs the
  fewest statements" — nobody. *Change:* "A practice the language has no
  keyword for is unavailable to you" — refuted by §4.3 (finding 8).
- `design-challenges-and-complexity` (2.1): "A good design captures every
  relationship in the domain" is thin. *Change:* "Design is a phase that
  ends when coding begins", which §5.1 refutes directly (design as sloppy,
  iterative and emergent through construction) and which has real holders.
- `layout-and-style` (7.1): "Layout is a matter of taste" is close to what
  the chapter *concedes* (the religious wars over brace style), so refuting
  it misstates the book. *Change:* "Indentation is cosmetic: the compiler
  ignores it, so it cannot cause a defect" — refuted by `dangling-else` and
  by the `clamp` exercise, where it did.
- `integration-order` (6.3): "Top-down and bottom-up are the only orders" —
  nobody. *Change:* "Integration is a phase at the end of construction"
  (phased, "big bang" integration, which §29.2 argues against; checked). The
  lab's stubs and drivers are then the price of doing it incrementally,
  which is the trade the chapter accepts.
- `managing-construction` (6.2): the misconception is Brooks's law and the
  lab computes capability multipliers; the refutation claims "who is on the
  team moves the estimate by more than how many", but the lab has no
  how-many input, so the comparison is asserted, not computed. *Change:*
  either add `people` and a path count to the view, or make `mistakes[0]`
  "An estimate is a number" — refuted by the product's range (0.54 to 1.90
  on two factors alone) — and put Brooks in `mistakes[1]` in prose.
*Priority: should-fix.*

**18. SHOULD-FIX — refutations that lean on the lesson's own illustrative
instance.** *Where:* 1.1 ("on the presets they are most of it"), 1.2 ("the
lab counts it: the schema carries five components"), 2.1, 6.1. *What is
wrong:* the hours, the dependency graph and the team sizes are the lesson's
inventions; a count over an instance the author wrote cannot refute a
general claim, and the voice rule from Phenomenology (finding 13 there) is
that the text refutes and the lab illustrates. *Change:* add to §C's
preamble: "A misconception is refuted by the chapter's argument; a lab run
on an illustrative instance illustrates the refutation and is said to." Fix
the four entries' wording ("on the lesson's illustration, …"). *Priority:
should-fix.*

**19. CONSIDER — misconceptions the reader actually arrives with, not yet
named.** `named-constants-and-other-types`: the over-application ("every
literal must be a constant, even the `2` in `/ 2` and the `100` in a
percentage") is the junior's error after reading §12.7, and the chapter's
0-and-1 rule invites it; make it `mistakes[1]`. `nesting-and-complexity`:
"a count of 11 means the routine is bad" is the misreading the material
clause exists for; make it `mistakes[1]` and let `coBand`'s banner carry
whose guidance it is. `controlling-loops`: "`i` after the loop is the last
value it had in the body" is the mistake the `lpAfter` tile exists to
correct; the current misconception is near it but says it less directly.

### D. Sequence, load and granularity

**20. SHOULD-FIX — Chapter 8 is one lesson carrying two hard ideas and
eight sections.** *Where:* `defensive-programming`, 15 min, §§8.1–8.8. *What
is wrong:* the chapter's one rule a programmer must internalise (checked,
§8.2: anticipated off-nominal cases get error handling; cases that must
not happen get assertions) and its second (the barricade: validate
at the boundary, assert inside) are two ideas, and the lesson's lab
(`cond/range`, a boundary check) touches neither; the Misconception is about
barricades and the lab is about an off-by-one. Chapter 8 is also the chapter
most used by the reader on their own code tomorrow. *Change:* split it:
`assertions-and-error-handling` (§§8.1–8.3, 8.6–8.8) with a classification
exercise — nine values in a routine (a parameter from a form, a result of
the routine's own arithmetic, a value from another module inside the
barricade, a file that may be missing…) each marked *validate*, *assert* or
*neither*, answer in the `why`; and `exceptions-and-barricades` (§§8.4–8.5)
keeping `cond/range` with the lab's point stated as the entry already has it
("a check written once at the barricade must be right at its ends"). For the
first lesson's lab, a small family-2 view `cond/barricade` (records `value,
origin, check`; tiles: external values with no validation, internal values
with none, assertions on external values — the chapter's Figure 8-2 as a
count) is cheap to build and computes the chapter's own rule. If the kit
cannot grow, the first lesson may share `cond/range` with the second and the
course `how_to` says so. The count then needs finding 21. *Priority:
should-fix.*

**21. CONSIDER — 41 is the right order of granularity; where to find the
42nd slot if finding 20 is taken.** The chapter splits in §B are the right
ones (5, 6, 7, 10, 12, 19, 22 each carry two ideas; 34–35 together is
right). Two options keep 41: (a) merge Chapter 2 into Chapter 1's lesson
("What Construction Is, and the Metaphors for It" — Chapter 2 is short, its
lab is a stretch (finding 14), and the writing-metaphor misconception fits
Chapter 1's argument that construction is more than typing); Course 1 goes
to 3 lessons and Course 2 to 9 (part_a Chapters 5–6, four lessons; part_b
7–9, five). (b) Accept 42 and move the tagline, description, §B total and §H
counts together. (a) is cleaner; the Subject loses nothing a reader would
miss. Either way, the orchestrator's starting number should not decide it.

**22. SHOULD-FIX — guard clauses are taught in the wrong lesson.** *Where:*
`unusual-control-structures` (4.4) reads §17.1 "multiple returns from a
routine (guard clauses)" but its lab and exercise are recursion;
`nesting-and-complexity` (4.7) does the guard-clause rewrite
(`nested-shipping` → `guard-clauses`) as its presets. *What is wrong:* the
reader meets the technique as a preset in 4.7 without having practised it,
and 4.4's Do ("compute the calls, depth and loop iterations of a recursive
routine") is the chapter's least transferable content. *Change:* finding 8's
exercise for 4.4 (the rewrite), so that 4.7 counts a transformation the
reader has already made. The order of lessons does not change. *Priority:
should-fix.*

**23. CONSIDER — `cond/range` is used twice for nearly the same skill.**
2.7 and 5.4 both find where a range check is wrong at its ends, with presets
that differ only in which end. If finding 20 is taken this resolves itself
(2.7's second half keeps `range` with barricade framing, 5.4 keeps boundary
analysis). If not, make 2.7's presets the `&&`/`||` confusion (a check that
can never fire; one that always does — the exercise's `age < 0 && age > 120`
is the right shape and should be a preset) and leave off-by-one to 5.4.

**24. CONSIDER — minutes.** Every lesson is 12–15 min and most Read lines
cover five to eight sections plus a snippet, a lab, an exercise and a quiz.
Capital's lessons of the same shape run longer. Either the estimates are the
author's and nobody reads them (the format says so), or the body should
say which sections the lab touches and which are "read in the book" — the
second is the honest reading of a 15-minute lesson on Chapter 24 or 26.

**25. CONSIDER — the body-block ceiling.** A lesson here carries the
chapter's paraphrase (five to eight sections), a snippet `code` block, the
exercise (an `h3`, a `code` block and a `p` = 3 blocks) and the closing
pointer. Eighteen blocks will be tight for the eight-section chapters (8,
24, 26, 30, 33). Either state in §E.1 that authors keep the paraphrase to
one `p` per two sections, or ask the renderer task for a range of 7–20 on
this path. Decide before authoring, not at the first failure.

### E. Quiz and distractor risks

**26. SHOULD-FIX — a distractor that is also true (the `content/AGENTS.md`
failure), in the three lessons most exposed to it.**
- `boolean-expressions`, `defensive-programming`, `boundaries-and-bad-data`:
  any question whose answer is a condition has equivalent rewrites as
  natural distractors — `!isAdmin && isOwner` and `isOwner && !isAdmin` are
  the same condition; `qty >= 1 && qty <= 99` and `qty > 0 && qty < 100` are
  the same check over `int`. The rule for authors: every distractor must
  differ on at least one row of the truth table or one integer, and the
  `why` names it.
- `nesting-and-complexity`, `themes-of-craftsmanship`: a question of the
  form "is this routine too complex?" has no defensible single answer and
  contradicts the material clause. Quiz the count, the breakdown or the
  line; never the verdict.
- Decision-point questions must state the rule in the stem ("by the
  chapter's rule, 1 plus each …"), because `else if` counts (it is an `if`),
  `?:` does not (the kit's banner says so), and a reader who counts `else`
  gets a defensible different number.
- Any figure still marked *(verify)* in §S.2 (F8, F11, F14's bands, F16's
  rates, F18, F28) must not be a quiz answer until the third pass settles
  it; a quiz that pins "unit testing's modal rate is 30%" turns a figure the
  Subject admits it has not checked into an examined fact.
*Priority: should-fix (add to §E.4 as a rule).*

**27. SHOULD-FIX — line numbers in prose depend on the snippet being
byte-identical in the body and the preset.** Every lesson's prose says
"line 14"; the renderer's `code` block and the lab's listing both count from
1 including blank and comment lines, so they agree *if* the author pastes the
same text into both. `free-slot` has a header comment on line 1 above the
routine; drop it in one place and every line number in the lesson is off by
one with no test catching it. *Change:* §E.4 item 2 says the body's `code`
block and the preset's code are one Python constant referenced twice; a
test (or `preview_subject.py`) compares them. *Priority: should-fix.*

### F. Voice

**28. The contract is right; four places lean.** §F is the right voice for
this book and the exemplary paragraph is exactly it. (a) Findings 15 and 18
are the voice findings that matter. (b) `reasons-to-create-a-routine`'s
"`two-names` shows duplication a text match misses" and
`abstract-data-types-and-interfaces`' misconception both have the lab failing
to show the lesson's point, which is honest and should be said in those
words ("the lab cannot see this; you can"), not as if the lab showed it.
(c) `collaborative-construction`'s "the inspection's defects are the cheap
ones" states the model's assumption as a fact (finding 11). (d) The `how_to`
of Course 5 ("every lab that uses them says so") and the material clause do
the Subject's honesty well; keep the sentence "a count says where to look" in
`footer_lead`. One wording: `nesting-and-complexity`'s "it is a reason to
look" is right, and `coBand`'s third band should print "10+" as the book
does, not "above 10". *Priority: consider, except where a finding above
already ranks it.*

**29. CONSIDER — snippets that teach a habit silently.** `overtime`'s
`pay = pay + 0.0;` is a no-op written to give the exempt branch a statement.
A reader will copy the shape. Replace the line with a comment
(`// exempt staff earn no overtime`); the branch is still legal Java, `if`
still counts, and the basis count is unchanged at 5. `nested-shipping`'s
`return -1.0;` as an error sentinel is a technique Chapter 8 lists with its
costs; the lesson may say so in a clause. `free-slot`'s fifth step,
"// return -1", is pseudocode at the level of the language, which §9.2 says
to avoid — a free second teaching point for 2.8 if the body names it.

### G. Code on the page and in the ear

**30. SHOULD-FIX — R2 as specified still reads a listing to a listener
without the line numbers every lesson's prose refers to.** *Where:* §H.1
R1 ("number drawn by a CSS counter, so copying the code copies no numbers")
and R2. *What is wrong:* a CSS counter is invisible to the read-out; a
listener hears fourteen lines and then "the step at line 14 is empty". *Add
to R2:* the spoken form of a `code` block announces each line's number
("line 14: …"), as the `math` table block announces a table; the visible
counter stays CSS. *Also missing from the dialect:* `%` ("mod", not
"percent" — `(lastUsed + 1) % table.length` is on the page), `[]` in a
declaration (`double[] prices` — "array of double"; R2 covers only `[i]`),
`.` as "dot" between identifiers, a negative literal (`-1.0` is "minus one
point zero", not a dash), `System.out.println` (give it a spoken form,
"print line"), and camelCase split into words (`isDomestic` → "is domestic";
otherwise every identifier is one unpronounceable token). And the
three-letter-word rule AUTHORING already warns of (`int`, `for`, `new` at the
head of a line are spelt letter by letter): the dialect needs a word list of
Java keywords read as words. *Priority: should-fix (file with the R2 task
now, before the dialect is built).*

**31. SHOULD-FIX — the layout lesson's point is invisible to a listener,
and the lesson must say so in prose.** `layout-and-style` is about
indentation disagreeing with structure; braces are silent in R2 and
indentation is not spoken at all, so a listener gets nothing from the
listing. The body must state the structure in words ("the `else` on line 5
binds to the `if` on line 3, whatever the indentation says"), and the `note`
should say the listing's evidence is visual. The same holds, less severely,
for `nesting-and-complexity`'s depth. Also: `coLines` marks mis-indented
lines in the listing — if by colour alone, `browser_contrast.js` will not
catch it and a colour-blind reader loses it; use a marker in the gutter.
*Priority: should-fix.*

**32. CONSIDER — the two listings on a phone.** A textarea and a numbered
`<pre>` side by side do not fit at 360 px; stack them (textarea first), and
say in §D.0 that a 72-character line scrolls inside the listing, as R1 says
for the body block. `complexity` defines depth below the routine's braces
and `layout` counts the routine's braces; a reader comparing `coDepth` 5 with
a line indented 24 spaces will ask. Say in each view's `details` which
convention it uses, or unify them.

### H. Contract gaps

**33. SHOULD-FIX — "the answer never on the same screen as the question" is
unenforceable, and only one place on the page hides anything.** *Where:* §B
and §E.4 item 4 ("the answer goes in `worked` or the quiz's `why`"). *What is
wrong:* the page is one scroll; `worked` sits a screen below the exercise and
is read first by anyone who scrolls. The quiz `why` appears only after an
answer is chosen. *Change:* the rule is: every exercise's answer is the
`why` of one quiz item (which satisfies §B's "at least one quiz item asks
about the snippet" at the same time), and `worked` works a *different*
instance — the lab's preset, as the Worked lines in §C already do. *Priority:
should-fix.*

**34. CONSIDER — the Standard for the two lessons whose lab reads
structure the reader states.** `inheritance-containment-and-members`' LSP
question and `design-heuristics-and-information-hiding`'s secret-naming are
the best exercises in Course 2 and neither is a count; their Standards say
"state the depth" and "count the modules". Let the Standard measure the act
the exercise performs (name the secret; say whether the subclass substitutes
and why), and keep the count as the lab's part.

## What is right and should not be changed

- §0's three families and the material clause. "A count is a reason to look,
  not a verdict" is the right frame for this book and the kit's ban on
  verdict tiles enforces it.
- The decision-point rule and its bands, now checked against the chapter,
  and `nesting-and-complexity`'s misconception (flattening moves complexity;
  it does not remove it). Keep both exactly.
- `scope-span-and-live-time` as the model lesson and the exemplary paragraph
  as the model voice. The live-time rule (last − first + 1) matches the
  chapter's own example; the one thing to add is a sentence that the book
  counts statements and the lab counts listing lines.
- `design-heuristics-and-information-hiding`'s two tiles moving in opposite
  directions. It is the clearest computed result in the Subject.
- `refactoring-safely`'s In/Out computation and its "two results" preset,
  `layout-and-style`'s `clamp` exercise (the compiler catches it only because
  the mis-indented statement is a `return`), `table-driven-methods`' "which
  does the business mean?", `boolean-expressions`' `half-demorgan`,
  `integration-order`'s `risk-first`, `controlling-loops`' four headers.
- Every snippet written for the lesson, in one language, at most 24 lines,
  with the figures computed from the exact text and pinned.
- The ban on the kit carrying any figure from the book, and "the numbers are
  other people's" in §F.5.
- Capstone design: `themes-of-craftsmanship` on the reader's own routine with
  `retry-delay` for the Standard.
- The honesty of `two-names` (the lab cannot see a renamed copy) and the
  `exercise` of 3.1 (the lab reads top to bottom) — keep the honesty; fix the
  framing (findings 1 and 16).

## Summary of must-fix items

1. **`reasons-to-create-a-routine`**: the exercise is the worked example;
   replace it with a cohesion classification and a fresh duplicate-block
   snippet; reorder the presets so the lab's limit comes last (finding 1).
2. **`structures-pointers-and-global-data`**: `access-routines` reaches 0 by
   dropping the six routines from the table; keep them, add a writers/owner
   tile, and let `dgCoupled` stay 9 (finding 2).
3. **The own-code step** is specified for 18 lessons and promised for 41;
   add an **Own:** line to every non-code entry (finding 3).
4. **`upstream-prerequisites` and `routine-length-and-parameters`** put the
   disputed later view in `mistakes[0]`, which refutes by construction and
   breaks §F.4; move it to the `note` and choose a misconception the
   chapter itself refutes (finding 15).
5. **`declaring-and-initializing-variables`**: "the compiler catches
   uninitialised variables" is true for Java locals, including the lesson's
   own exercise; reword the misconception and say what `javac` catches
   (finding 16).

Should-fix findings 4–13, 17–18, 20, 22, 26–27, 30–31 and 33 can be taken in
the same revision; none changes the lesson count unless finding 20 is
adopted, in which case finding 21 says where the slot comes from.
