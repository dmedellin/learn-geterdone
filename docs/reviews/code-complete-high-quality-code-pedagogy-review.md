# Pedagogy review: Code Complete, Course 2 — Creating High-Quality Code

Reviewed 2026-10-25 on branch `feat/code-complete-subject`, against the
`pedagogical-expert` brief, PLAN §0, §B, §C (Course 2), §E.4 and §F,
AUTHORING.md, and the pre-authoring review
(`docs/reviews/code-complete-spec-pedagogy-review.md`). Source:
`content/code_complete/c2_high_quality_code/` (`__init__.py`, `part_a.py`,
`part_b.py`), all nine lessons read in full. The course was rendered with
`preview_subject.py` (final line `OK`; 9 pages, 9 with pinned figures, 0
failing), every lesson was opened in Playwright at 390 px and 1280 px, and
every exercise was typed or pasted into its lab and the tiles read. Every key
line and worked line, and every exercise snippet, was run through
`speech.say_code`. Six claims about the book that the lessons make in
McConnell's voice were checked against the page.

## Verdict

This course does what the Subject promised and the specification did not yet:
each lesson teaches an act a working programmer can perform tomorrow, the
exercises are applied and have one checkable answer each, the answer lives only
in a quiz `why`, and the labs confirm every exercise's count. The four
pre-authoring findings that bore on this course are taken: the cohesion
classification plus `printSummary` replaces the repeated worked example and the
presets run `copied`, `extracted`, `two-names` (finding 1); the own-code step is
an instruction with an observable result in all nine lessons (3); the
short-function school is in the `note` of Routine Length and Parameters, stated
at strength and unsettled, and `mistakes[0]` there is §7.6's function rule
(15); Chapter 8 is two lessons with the `cond/barricade` view, and the
`cond/range` presets are the `&&`/`||` confusion (20, 23); `expireSessions`
makes the Java gotcha the second half of the exercise (7); the Standards of
lessons 2 and 4 measure the act, not the count (34).

Nothing here is a must-fix in the sense of a lesson that misteaches. The two
findings ranked must-fix are a preset that contradicts the exercise's answer on
the same page, and a quiz item that pins a judgement the lesson itself says is
the reader's. The read-out findings are kit-level and shared with Course 1.

## Lesson by lesson: does it teach an act?

| lesson | the act | taught by | exercise answerable | lab confirms |
| --- | --- | --- | --- | --- |
| design-challenges-and-complexity | count pairs, connected share, fan-in | worked on `layered`, 4 steps | yes (6/15 = 40 %, `stock` 2) | `2/5 = 40%`, `stock 2` |
| design-heuristics-and-information-hiding | name the secret, its keeper, who must be edited | worked on `exposed`/`hidden` | yes (3 then 1) | `3: dueDate, joinDate, shipDate` |
| abstract-data-types-and-interfaces | count fields/public routines, group by abstraction | worked on `public-fields` | counts yes; grouping is a judgement (finding 2) | `3`, `2`, `1`, `1` |
| inheritance-containment-and-members | depth; substitution by naming a caller | worked on `deep`; steps 3–4 give the method | yes (5 at `Puppy`; 20 → 25) | `5`, `Puppy` |
| reasons-to-create-a-routine | name cohesion; mark a repeated block, write its header | worked on `copied` | yes | `1`, `4`, `lines 4–5 and lines 8–9` |
| routine-length-and-parameters | count lines/parameters; regroup | worked on `nine-parameters` | yes (8 → 4) | `coParams 8` |
| assertions-and-error-handling | test a check at its ends; read the connective | worked on `never-fires` | yes (−1, 101; `&&`) | `−1 and below, 101 and above`, exposed `−1, 101` |
| exceptions-and-barricades | place a value by the barricade rule | worked on `feedPrice` | yes (five validate; tax rate argued) | all four lists `0: none` on the answer |
| the-pseudocode-programming-process | find the empty step; judge the obvious fix | worked on `free-slot` | yes (line 10; `Iterator`) | `4`, `line 10` |

Worked-example progression holds in every lesson: the `worked` block works a
preset, the `steps` fade it into a procedure, and the exercise is a different
instance. The misconception slot names a real wrong model in all nine and
refutes it from the chapter, with the lab run introduced as "on the lesson's
illustration". The scene opening (§F.1) is used in three of nine lessons
(Abstract Data Types, Routine Length, the PPP), the rest open with the chapter's
own question. Each lesson has at most one light remark, all McConnell's own
(the hoses, the Pilgrims, the chain saw, Dog Breath). Body blocks run 11–17,
inside the 7–18 ceiling; Reasons to Create a Routine is at 17 and reads long
on a phone (the four paraphrase paragraphs before "Now the count" fill about
three screens) but nothing in it is padding.

Claims checked against the text and found as stated: the undergraduate
textbook (p. 163), "learn the ideas rather than the terminology" (p. 171), the
Pilgrims (p. 173), the §8.2 rule (p. 191), Mars Pathfinder and "Dog Breath"
(p. 210), "that hardly ever happens if you're using the PPP" (p. 233), "grossly
optimistic" (p. 147), private inheritance as a last resort (p. 143), school
problems rarely wicked (p. 75), the two positions always wrong (p. 119).

## Findings

### Must-fix

**1. `exceptions-and-barricades`: the `mixed` preset puts `taxRate` inside
the barricade; the exercise's answer, in the quiz `why` on the same page,
says the tax rate is outside and the one value to argue about.** *Where:*
`part_b.py`, preset `mixed` (`taxRate, inside, assert`), body paragraph
"Take them in turn", quiz item 1 `why` ("The tax rate is the one to argue
about … section 8.1 treats a file as an external source"). *What is wrong:*
a reader who does the exercise, answers the quiz, and then opens the lab sees
the lesson's own illustration place a `taxRate` on the side the quiz has just
told them is arguable at best. Nothing on the page says the two tax rates are
different values, and the `mixed` paragraph does not mention `taxRate` at all.
This is the one place in the course where the lab and the lesson disagree in
front of the reader. *Change (either):* (a) rename the preset value in all
three presets to one that is unambiguously computed inside, and keep the
rest of the record unchanged, so the pinned tiles move only in the name:

```
feedPrice, outside, assert; lineTotal, inside, assert;
customerId, inside, none; taxDue, inside, assert
```

with `checks-everywhere`'s expectation becoming
`"cdInsideValidated": "3: lineTotal, customerId, taxDue"`; or (b) keep the
name and add one sentence to the "Take them in turn" paragraph: "`taxRate`
here is the rate the pricing class holds, not a value read from a file; the
exercise has the other kind." (a) is cleaner, because the exercise then owns
the argument about configuration files outright.

**2. `abstract-data-types-and-interfaces`: quiz item 1 pins "three classes"
for `kitchen-sink`'s grouping, which the exercise's own text calls "yours"
and the `note` says the lab cannot tell.** *Where:* `part_a.py`, exercise
`p` ("the grouping is yours"), quiz item 1 (options "three classes" versus
"two classes"), `note` ("it cannot tell whether public routines belong
together, which is the chapter's main question"). *What is wrong:* §E.4
item 5 says never quiz a verdict, and this is one: a reader who groups the
audit log with ticketing (an audit log opened and closed around ticket
operations is a plausible part of the ticket abstraction) gets "two classes",
has a defensible reason, and is told they are wrong. The counts in the same
item (3 fields, 2 public) are checkable; the grouping is not. *Change:* make
item 1 ask only what is checkable and keep the grouping as the lesson's
answer in the `why`, where §B says the exercise's answer lives:

- stem: "In the exercise's `Point`, how many fields and public fields are
  there, and what does a caller need once `x` and `y` are private?"
- options: "3 fields, 2 public; a reader for each, `x()` and `y()`, or
  whatever the callers do with them" (correct); "3 fields, 3 public; nothing,
  since `label` is already private"; "2 fields, 2 public; a reader for each";
  "3 fields, 2 public; nothing, since `distanceTo` already reads them".
- `why`: keep the present text, which ends with the three abstractions
  (tickets, forecast, audit log) and says "so three classes" — and add
  "By the names alone; a reader who keeps the audit log with the tickets has
  made a design decision, not a counting error."

### Should-fix

**3. Read-out: the code dialect reads the article "a" as the letter A in
key lines and worked lines, across the course.** *Where:* every key line and
worked line goes through `speech.say_code`; `a secret: a decision likely to
change` is spoken "A secret A decision likely to change", `has a:
containment, the workhorse` "has A containment", `layered: 7 uses, each joins
a different pair` "each joins A different pair". Fourteen key lines and four
worked lines in this course carry a lone "a"; Course 1 has three (checked:
`fix a defect near where it was made`, `program into a language, not in it`,
`a ratio counts statements, not hours`). *What is wrong:* a listener hears the
letter, not the article, in the lines meant to be the lesson's summary. It is
a kit finding (`say_code` capitalises a single-letter token as an identifier),
not an authoring one, and should not be worked around by rewording every key
line. *Change:* in `say_code`, a lone `a` that is preceded by a word or a
punctuation mark and followed by a word is the article and is left lower
case; a lone `a` adjacent to an operator, a bracket or a dot is an identifier.
Until then, the three worked-example lines that read worst could be reworded
without loss: "each joins a different pair" → "each joins its own pair";
"has a: containment, the workhorse" → "has-a: containment, the workhorse"
(check the hyphen's reading first).

**4. `routine-length-and-parameters`: the exercise's closing sentence and
the quiz stem both leave a reader unsure what "the time fields" and "both
counts" are.** *Where:* exercise `p` ("You can paste the header into the lab
afterwards to check both counts"); quiz item 1 stem ("with its time fields
grouped"). *What is wrong:* the exercise asks only for the parameter count and
the regrouped header, so "both counts" has no second referent; and
`durationMinutes` is a time field, so a reader who groups it too (a
`Duration`, or a start–end interval) arrives at 3 and finds no option.
*Change:* the exercise `p` ends "You can paste the header into the lab
afterwards to check the parameter count." The stem reads "How many parameters
has the exercise's `schedule`, and how many once the five fields that name a
moment, `year` to `minute`, become one `LocalDateTime`?" The `why` then adds
one sentence: "`durationMinutes` could become a `Duration` as well; the header
would still have four parameters, and a single interval object would be a
further choice the stem does not ask about."

**5. `reasons-to-create-a-routine`: the second cohesion item is close enough
to functional that a reader can defend it, and the quiz has no option for
them.** *Where:* exercise `ol` item 2 ("works out a parcel's volume, then
uses that volume to choose a box size"); quiz item 1. *What is wrong:* "choose
a box size for a parcel" is one operation with one output; what makes the
book's own example sequential (age, then retirement date, p. 168) is that the
routine delivers both results. The item as written delivers one. A reader who
says "functional" meets four options that all say "sequential" and learns
nothing about why. *Change:* "works out a parcel's volume and then, from that
volume, its box size, and returns both" — two results, the second computed
from the first, which is the chapter's sequential case exactly; and add to the
`why` "it would be functional if it returned the box size alone".

**6. `exceptions-and-barricades`: "neither" is offered in the exercise and is
never the answer.** *Where:* exercise `p` ("Mark each validate, assert or
neither"), quiz `why` (five validate, four assert). *What is wrong:* a
three-way classification in which one way is never right is a two-way one
with a decoy, and the reader who takes "an index into the routine's own
array" as neither (it never crossed anything) is marked wrong by the `why`
without being told why an assertion is still the rule's answer. *Change:*
either drop "or neither" from the exercise and the Standard (§C's Standard
says "validate, assert or neither"; PLAN would change in the same commit), or
keep it and add to the `why`: "Nothing here is neither: the index is the
routine's own, and §8.2 asks for a precondition on it all the same, which is
what an assertion is for."

**7. `design-heuristics-and-information-hiding`: quiz item 4's distractors
are not positions anyone holds.** *Where:* "Public secrets and private
secrets"; "Secrets of the user interface, and secrets of the database". *What
is wrong:* §E.4 item 5 says distractors are the misconceptions of §C or the
off-by-one of the answer, never a joke option; these are neither, and the
item is answerable by elimination. *Change:* "Hiding data, and hiding
routines" (the reader who thinks hiding is about members, which
`mistakes[2]` refutes) and "Hiding from users, and hiding from other
programmers" (the reader who confuses information hiding with access
control). Both are wrong models a reader arrives with.

**8. `design-challenges-and-complexity`: quiz item 1's fourth distractor, "6
of 12 pairs, 50%", comes from nowhere.** *Where:* quiz item 1. *What is
wrong:* 15 and 30 each name a real slip (pairs versus uses); 12 names none,
so it is a throwaway. *Change:* "5 of 15 pairs, 33%; stock, with fan-in 2" —
the reader who missed one of the six records — and the `why` adds "six
records, six pairs: count the records before the pairs".

### Consider

**9. `inheritance-containment-and-members`: "private inheritance … a last
resort" needs the §F.6 sentence.** Java has no private inheritance; the
lesson says "In Java the prohibition is `final`" for Bloch's line but not
that the private-inheritance warning is C++'s. One clause: "(a C++ device;
Java has no private inheritance, so the question does not arise)".

**10. `the-pseudocode-programming-process`: the exercise's `coMaxUnder` is
"2 lines, under line 5", which the page never explains.** The tile is named
in the "Now the count" paragraph for `free-slot` ("the most code under one
step is 3 lines, under line 8") but a reader pasting `expireSessions` sees
"under line 5" for a step whose code is the `for` header and the `if`, and
may think the lab has miscounted. One sentence in the panel or the body: "a
step's code runs to the next comment, so the `for` and the `if` both belong
to the step above them."

**11. `assertions-and-error-handling`: `<code>-ea</code>` and
`<code>yyyy-MM-dd</code>` have no spoken form.** They are read raw; "-ea"
may be spoken "minus e a". A spoken-form entry in
`content/spoken/code_complete.py` for `-ea` ("dash e a, the switch that
enables assertions") and `yyyy-MM-dd` ("year, dash, month, dash, day")
would settle it; the author notes say the file is shared, so add a Course 2
block.

**12. `reasons-to-create-a-routine`: length on a phone.** At 390 px the four
paraphrase paragraphs before the first listing run about three screens, and
the exercise's `ol` and listing sit after four code blocks. It is within the
block ceiling and nothing is padding; if the course is trimmed anywhere, the
§7.3 paragraph could lose its last two clauses ("never tell routines apart by
a number … use opposites precisely"), which the exercise does not use.

**13. `exceptions-and-barricades` and `design-heuristics`: the lab checks
consistency, not the design.** Both lessons say so (the barricade lab "cannot
decide which side a value is on"; the ripple lab "cannot read code"), and the
exercise sentences "you can type your classification into the lab afterwards"
are honest. Worth keeping exactly; a later edit should not promise more.

## What is right and should not be changed

- The two tiles of Design Heuristics moving in opposite directions, and the
  paragraph that says which one the chapter cares about and which a build
  tool does. It is the clearest computed result in the course, as the
  pre-authoring review predicted.
- `two-names` last, with "the lab cannot see this copy; you can" in those
  words, and the `note` that cohesion is not measurable at all.
- The `Square` exercise overriding both setters, with the `why` explaining
  why one override would pass the caller. That is misconception handling
  done by construction.
- `expireSessions`: the empty step and the Java gotcha in one exercise, with
  the `why` naming both failure modes of `remove` inside an enhanced `for`.
- The `cond/range` presets as the `&&`/`||` confusion and the worked
  example evaluating `never-fires` at 0 and 13 by hand; the read-out speaks
  it as "0 is less than 1 is true, 0 is greater than 12 is false".
- The modern aside on routine length, in the `note`, both positions at
  strength, with "your own records of where defects were found can test
  either".
- The `how_to`'s one idea (complexity) and "a count is a reason to look"
  carried into every "What do the counts show?" paragraph.
- Phone layout: the textarea and the numbered listing stack, the listing
  scrolls inside its box, and no page scrolls horizontally at 390 px.

## Summary of must-fix findings

1. **`exceptions-and-barricades`**: the `mixed` preset's `taxRate, inside`
   contradicts the exercise answer on the same page; rename the value to a
   computed one (`taxDue`) in all three presets and the pinned string, or
   say in the body that it is not the configuration file's rate (finding 1).
2. **`abstract-data-types-and-interfaces`**: quiz item 1 pins the
   `kitchen-sink` grouping, a judgement the lesson calls the reader's; quiz
   the `Point` counts and what a caller needs, and keep the three
   abstractions as the answer in the `why` (finding 2).

Should-fix 3 (the article "a" in the code dialect) is a kit change that
benefits every course on the path; 4–8 are single-sentence edits to one
lesson each.
