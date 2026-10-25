# Code Complete, Read Along — the build specification

This is the curriculum, lab and authoring contract for the thirteenth Subject:
a read-along of Steve McConnell, *Code Complete: A Practical Handbook of
Software Construction*, second edition (Redmond: Microsoft Press, 2004), the
whole book in its own order — its seven Parts and thirty-five chapters — one
lesson per chapter, or per half-chapter where a chapter carries two hard ideas.
The operator asked for it "built the same way as the earlier read-along
Subjects" and taken all the way to live. Because the book is a practical
handbook, every lesson is applied: the reader reads the chapter's argument and
then measures it on a short piece of code.

Everything an author, a kit engineer or a reviewer needs is here. Where it says
"exactly", a test or a gate enforces it. Where it says "never", a published
page somewhere in this library has already been wrong for that reason.

It is built the way *Capital* and *Phenomenology of Perception* were built
(`docs/capital/PLAN.md`, `docs/phenomenology/PLAN.md`) and adopts their
conventions by reference wherever this one is silent. Read before this:
`AGENTS.md` §0, §1, §1a, §2 and the page-weight note; `content/AGENTS.md` (all
of it); `scripts/mathpath/AGENTS.md` ("a preset's two claims");
`docs/philosophy/PLAN.md` §D.0 and §E; `docs/phenomenology/PLAN.md` §E.3.

**Status: specification, blocked on two things.** (1) The book's text: the
operator has been asked to upload his copy. Until it arrives every page
reference in this document is `TBD`, no lesson carries a quotation, and every
figure attributed to McConnell is marked *verify against the book* (§S.2).
(2) Renderer support for code (§H.1, a `chrome-renderer` task): the lesson
schema has no code block today, and the read-out mangles code operators. The
kit (§D) can be built in parallel with both.

Contents

- §0 The one question, answered for this Subject
- §A PATH fields
- §B The seven courses, and the module names
- §C Every lesson: 41 entries
- §D The lab kit: `cckit` (8 modes, 35 views)
- §E Package layout, the source text, quoting, and the author's checklist
- §F Voice: the read-along, for a working programmer
- §G What is left out, and why
- §S Sources, and the register of figures to verify
- §H Wiring notes for the orchestrator, and the renderer work
- §R Review record

---

## §0 The one question

`docs/FUTURE-SUBJECTS.md` asks of every proposed Subject: **what does the reader
compute?** For *Code Complete* the answer is direct, and it is the book's own
method: McConnell measures code. He counts the decision points in a routine to
decide whether to split it, counts the lines between two references to a
variable to decide where to declare it, counts the basis test cases a routine
needs, multiplies defect-removal rates to say what a set of practices will
catch, multiplies the cost of a defect by the phase it is found in, counts the
communication paths in a team, and times a routine before and after a tuning
change. Every one of those is arithmetic the reader can do on a piece of code
in front of them, and the lab does it with them.

The honest answer comes in three families, and every view's `panel_intro` says
which one it is in:

1. **A count over code.** The lab reads a short Java routine (the lesson's, or
   one the reader pastes) and counts what the chapter says to count: decision
   points, nesting depth, basis test cases, references and live times, a
   variable read before it is set, magic numbers, comment lines, duplicated
   lines, the inputs and outputs of a block to be extracted, lines whose
   indentation disagrees with their structure. The rules of each count are
   stated in the panel (§D.1, `code`). The kit **reads** code; it never runs
   it.
2. **A count over a structure the lesson states.** A dependency list (who uses
   whom, who inherits from whom, who calls whom, which file a target is built
   from), a boolean condition, a validation check against its specification,
   a chain of `if` tests with their frequencies, a lookup table, a loop
   header. The lab computes what the structure implies: what a change
   ripples to, how deep a hierarchy is, which stubs an integration order
   needs, whether two conditions agree on every row, which integers a check
   gets wrong, how many tests a chain makes on average, how many times a loop
   runs, what Java's arithmetic gives.
3. **The arithmetic of a stated figure.** McConnell's tables — defect-removal
   rates, the cost of a defect by the phase it is found in, language
   statement ratios, defect density and productivity by project size, effort
   multipliers — and the lesson's own illustrative inputs (a profile of
   runtimes, a team size, a tool's cost). The lab does the arithmetic the
   chapter does with them. The figures come from the lesson, never from the
   kit, and each is marked with its source: *the book, after Jones*, or
   *illustrative*.

**What the lab never does** is call a count a verdict. Nine decision points do
not make a routine bad; a comment density of one in seven does not make it
documented; a combined removal rate of 95% is what the averages multiply to,
not what your project will see. McConnell says the same of his own numbers —
they are reasons to look — and that is the material clause.

**Deliberate deviations from the library's conventions:**

1. **The lab reads code.** Every other kit computes from numbers or records.
   The `code` mode takes a Java listing in a `<textarea>` and tokenises it by
   a stated subset of the language (§D.1). The rules are part of the lesson:
   a reader who disagrees with what the kit counts can see why.
2. **Code appears in the lesson body.** That needs a new body block kind and a
   way for the read-out to speak code (§H.1). Until those land no lesson
   with code is authored.
3. **One language, Java**, for every snippet (§D.0, "Why Java").
4. **The chapter comes first, in paraphrase.** The earlier read-alongs open
   each lesson with a quoted passage. This book is in copyright and its text
   is not yet in hand, so a lesson opens with the chapter's argument in the
   lesson's own words, pointing to the section by number; a short opening
   quotation may be added once the text arrives (§E.3), and no lesson
   depends on one.
5. **Cross-references to the book are by chapter and section number**
   ("Section 19.6"), which is how the book numbers itself. Lessons on this
   path are cross-referenced by title.

---

## §A PATH fields (`content/code_complete/__init__.py`)

```
"slug": "code-complete",
"title": "Code Complete, Read Along",
"level": "Beginner → Intermediate",
"level_note": "you can read a short routine in Java, C# or C++; the arithmetic is counting",
```

**Title: a recommended change to the decided design.** The orchestrator
decided `"title": "Code Complete"`. This specification proposes `"Code
Complete, Read Along"`, with the catalog's `short_title` `"Code Complete"`
unchanged, for two reasons: it is the precedent (`"Capital, Read Along"`,
`"Phenomenology of Perception, Read Along"`, with `short_title` dropping the
suffix on the home card, B-22), and a breadcrumb or `<title>` that reads
only "Code Complete" presents a page of this library as the book itself, which
belongs to McConnell and Microsoft Press. If the orchestrator keeps the bare
title, nothing else in this document changes. The title feeds every
breadcrumb and the test inventory, so it is settled before the first build.

**tagline** (counts re-verified at wiring by
`test_the_tagline_and_description_state_the_real_counts`):

> Steve McConnell&rsquo;s <em>Code Complete</em>, read chapter by chapter from
> the foundations of construction to the habits of the craft &mdash; with each
> chapter&rsquo;s guidance measured on short pieces of code: decision points,
> live times, basis tests, defect-removal rates and the cost of a late fix.
> Seven courses and 41 lessons are available.

**description**:

> The Code Complete Subject: a read-along of the second edition (2004) in its
> own order, seven courses that follow the book&rsquo;s seven Parts. Each
> lesson sets out a chapter&rsquo;s argument and then applies it to code
> &mdash; counting the decision points in a routine, the lines a variable
> stays live, the test cases a routine needs, the defects a set of practices
> leaves behind, the stubs an integration order needs &mdash; and ends with a
> piece of code to fix or to measure. All seven courses and 41 lessons are
> available.

**key** (each line ≤ 46 characters, measured):

```
points = 1 + each if, for, while, case, &&, ||      (46)
span = lines between two references                  (35)
live time = last line − first line + 1               (38)
paths in a team of n = n·(n − 1)/2                   (34)
left = N·(1 − e₁)·(1 − e₂)·…                         (28)
speedup = old time / new time                        (29)
a count is a reason to look, not a verdict           (42)
```

(The parenthesised lengths are not part of the lines.) The first line reads
correctly only after the speech dialect of §H.1 lands; until then `&&` is read
"and and".

**material** (must differ from every existing clause; proposed
`CC_DISCLAIMER_RE = r"a reason to look at it, not a verdict"`, checked against
the eleven existing patterns in `tests/test_site_invariants.py`):

> every figure on this path is computed in your browser from the code or the
> quantities a lesson states, and a count over code is a reason to look at it,
> not a verdict on it &mdash; the rates and costs quoted from the book are
> averages from other people&rsquo;s projects, which your own records can test
> and the lab cannot.

**prerequisites** (paragraphs):

1. You can read a short routine in a C-family language. Every snippet is
   Java, kept under twenty lines, and uses nothing past what a first course
   teaches: `if`, loops, methods, arrays, a class with fields. A reader who
   knows C#, C++, JavaScript or Python reads it without trouble; where Java
   behaves in a way another language does not (integer overflow, integer
   division, `switch` fall-through), the lesson says so.
2. No other Subject. Boolean algebra is taught where the book uses it, in
   Boolean Expressions; Logic and Proof on the Discrete Mathematics path goes
   further and is optional. The arithmetic is counting, a product and a
   share; the labs do it, and what is asked of you is to say what each count
   is evidence of.
3. A copy of the book is strongly recommended. The book is in copyright, so a
   lesson states each chapter's argument in its own words, points to the
   section by number, and quotes at most a sentence or two. The code is
   written for these lessons; none of the book's listings or checklists is
   reproduced, and the book's own versions are better read in the book.
4. Some code of your own. Every `code` lab takes a routine you paste in, and
   the most useful thing a lesson can do is send you back to your own work
   with a number to look at.

**why_order** (paragraphs):

1. The order is the book's, and it runs from outside the code inwards and out
   again. Laying the Foundation says what construction is and what must be
   settled before it starts; Creating High-Quality Code builds classes and
   routines; Variables and Statements go down to the line; Code Improvements
   tests, inspects, debugs, refactors and tunes what was built; System
   Considerations widens the view to the project; Software Craftsmanship
   closes on layout, documentation and the programmer.
2. Design comes before variables and statements because the book's one
   organising idea, that managing complexity is software's primary technical
   imperative, is argued in Chapter 5 and used in every later chapter. A
   reader who meets the decision-point count before the argument for it sees
   a metric; a reader who meets it after sees the argument applied.
3. Quality comes after construction because its chapters measure the code the
   earlier ones taught you to write: the basis tests of Structured Basis
   Testing are counted on the same routines whose decision points Nesting and
   Complexity counted.
4. The Parts can be read separately. Variables and Statements assume only the
   first two courses; System Considerations can be read by a lead who has read
   Laying the Foundation; Software Craftsmanship's lessons stand alone.

**sequence_intro**:

> Each course assumes the ones before it and nothing else. Creating
> High-Quality Code uses the prerequisites and the cost of a late fix from
> Laying the Foundation; Variables and Statements apply the complexity
> argument line by line; Code Improvements measures the code they produce;
> System Considerations and Software Craftsmanship widen the view to the
> project and the programmer.

**footer_lead**:

> <strong>Educational course material.</strong> Every figure on this path is
> computed in your browser from what the lesson states: a decision-point count
> is one plus the branches a stated rule finds, a live time is a difference of
> line numbers, a combined removal rate is a product of the stages&rsquo;
> misses. The code is written for this course; the labs read it and never run
> it, and nothing you paste is sent anywhere. Figures quoted from the book are
> marked with their source. What the labs cannot do is tell you whether a
> routine is good &mdash; a count says where to look.

---

## §B The seven courses

| # | slug | title | the book | lessons | level |
| --- | --- | --- | --- | --- | --- |
| 1 | `code-complete-laying-the-foundation` | Laying the Foundation | Part I, Chapters 1–4 | 4 | Beginner |
| 2 | `code-complete-high-quality-code` | Creating High-Quality Code | Part II, Chapters 5–9 | 8 | Beginner |
| 3 | `code-complete-variables` | Variables | Part III, Chapters 10–13 | 6 | Intermediate |
| 4 | `code-complete-statements` | Statements | Part IV, Chapters 14–19 | 7 | Intermediate |
| 5 | `code-complete-code-improvements` | Code Improvements | Part V, Chapters 20–26 | 8 | Intermediate |
| 6 | `code-complete-system-considerations` | System Considerations | Part VI, Chapters 27–30 | 4 | Intermediate |
| 7 | `code-complete-software-craftsmanship` | Software Craftsmanship | Part VII, Chapters 31–35 | 4 | Intermediate |

Total 41, as the orchestrator's starting proposal, with one change of split
inside a course: Chapter 22 is split into Structured Basis Testing and
Boundaries and Bad Data (the proposal's "ch22 ×2"), and Chapters 34 and 35 share
the last lesson. Course titles are the book's Part titles; the slugs carry the
`code-complete-` prefix, so the generic titles "Variables" and "Statements"
collide with nothing in the flat course namespace.

**Chapter splits** (one hard idea per lesson): Chapter 5 (two: design's
challenges and the complexity argument, §§5.1–5.2; heuristics and information
hiding, §§5.3–5.5), Chapter 6 (two: abstract data types and interfaces,
§§6.1–6.2; implementation, inheritance and members, §§6.3–6.6), Chapter 7
(two: reasons for a routine, cohesion and names, §§7.1–7.3; length,
parameters and functions, §§7.4–7.7), Chapter 10 (two: declaration and
initialisation, §§10.1–10.3; scope, span, live time and one purpose,
§§10.4–10.8), Chapter 12 (two: numbers, §§12.1–12.3; the other types and named
constants, §§12.4–12.9), Chapter 19 (two: boolean expressions, compound and
null statements, §§19.1–19.3; nesting, structured programming and complexity,
§§19.4–19.6), Chapter 22 (two: structured basis testing with the testing
landscape, §§22.1–22.3 to the end of basis testing; data-flow and boundary
testing, bad data, typical errors and the rest of the chapter). Section
numbers are the edition's as remembered; every split is checked against the
contents page when the book arrives (§E.2) and moved if a section falls the
other side.

**Part files.** A course with more than six lessons splits into `part_a.py`
and `part_b.py`: Course 2 (lessons 1–4 Chapters 5–6, 5–8 Chapters 7–9),
Course 4 (1–4 Chapters 14–17, 5–7 Chapters 18–19), Course 5 (1–4 Chapters
20–22, 5–8 Chapters 23–26). The rest are one `part_a.py`.

**Check ids** take the form `cc-course7-lesson-<lesson-slug>` (18 characters
before the slug). Every lesson slug in §C is at most 40 characters, so every
check id is at most 58, inside the 72-character cap; the longest is
`cc-course2-lesson-design-heuristics-and-information-hiding` (58).

**Module names.** Each chapter is one module, named `Chapter N · short form`
from the table below (at most 60 characters; never cut). A lesson's `module`
is its chapter's name. The short forms are the spec's; the course `summary`
gives each chapter's full title as the edition prints it, copied from the
contents page when it arrives (the full titles below are as remembered and are
checked then).

| chapter | module name | full title (to be checked) |
| --- | --- | --- |
| 1 | `Chapter 1 · Welcome to Software Construction` | Welcome to Software Construction |
| 2 | `Chapter 2 · Metaphors` | Metaphors for a Richer Understanding of Software Development |
| 3 | `Chapter 3 · Upstream Prerequisites` | Measure Twice, Cut Once: Upstream Prerequisites |
| 4 | `Chapter 4 · Key Construction Decisions` | Key Construction Decisions |
| 5 | `Chapter 5 · Design in Construction` | Design in Construction |
| 6 | `Chapter 6 · Working Classes` | Working Classes |
| 7 | `Chapter 7 · High-Quality Routines` | High-Quality Routines |
| 8 | `Chapter 8 · Defensive Programming` | Defensive Programming |
| 9 | `Chapter 9 · The Pseudocode Programming Process` | The Pseudocode Programming Process |
| 10 | `Chapter 10 · Using Variables` | General Issues in Using Variables |
| 11 | `Chapter 11 · Variable Names` | The Power of Variable Names |
| 12 | `Chapter 12 · Fundamental Data Types` | Fundamental Data Types |
| 13 | `Chapter 13 · Unusual Data Types` | Unusual Data Types |
| 14 | `Chapter 14 · Straight-Line Code` | Organizing Straight-Line Code |
| 15 | `Chapter 15 · Conditionals` | Using Conditionals |
| 16 | `Chapter 16 · Loops` | Controlling Loops |
| 17 | `Chapter 17 · Unusual Control Structures` | Unusual Control Structures |
| 18 | `Chapter 18 · Table-Driven Methods` | Table-Driven Methods |
| 19 | `Chapter 19 · General Control Issues` | General Control Issues |
| 20 | `Chapter 20 · The Software-Quality Landscape` | The Software-Quality Landscape |
| 21 | `Chapter 21 · Collaborative Construction` | Collaborative Construction |
| 22 | `Chapter 22 · Developer Testing` | Developer Testing |
| 23 | `Chapter 23 · Debugging` | Debugging |
| 24 | `Chapter 24 · Refactoring` | Refactoring |
| 25 | `Chapter 25 · Code-Tuning Strategies` | Code-Tuning Strategies |
| 26 | `Chapter 26 · Code-Tuning Techniques` | Code-Tuning Techniques |
| 27 | `Chapter 27 · Program Size` | How Program Size Affects Construction |
| 28 | `Chapter 28 · Managing Construction` | Managing Construction |
| 29 | `Chapter 29 · Integration` | Integration |
| 30 | `Chapter 30 · Programming Tools` | Programming Tools |
| 31 | `Chapter 31 · Layout and Style` | Layout and Style |
| 32 | `Chapter 32 · Self-Documenting Code` | Self-Documenting Code |
| 33 | `Chapter 33 · Personal Character` | Personal Character |
| 34–35 | `Chapters 34–35 · Themes and Further Reading` | Themes in Software Craftsmanship; Where to Find More Information |

**Every lesson has an exercise.** §C's **Exercise** is a piece of code (or a
small table) the reader fixes or measures by hand. It is a `code` block under
an `h3` near the end of the body; the `standard` asks for exactly that act
without the lab, and at least one quiz item asks about the snippet. Its answer
is in §C, computed by the reference model (§D.4). The lab may be used to check
the answer afterwards; the body says so in one sentence.

**Every lesson ends by sending the reader to their own code.** The last of
the `steps` is the same act applied to a routine of the reader's own,
pasted into the lab where the view takes code.

---

## §C Every lesson

Format:

- **slug** — Title — *module* — minutes (an estimate for the author; there is
  no minutes field)
- **Read:** the sections the lesson covers, by number, and what the argument is,
  in paraphrase. Pages `TBD`.
- **Do:** the observable objective; **Standard:** the act that shows it,
  without the lab, and its pass level.
- **Lab:** mode/view (§D); presets with their exact instances; the tile
  values the reference model computes, in §D.0's formats. The exact strings are
  read with `labcheck.js --observe` at authoring and pinned (rule 3).
- **Misconception:** the wrong model `mistakes[0]` names and refutes.
- **Worked:** the single worked example, in one line.
- **Exercise:** the applied task, with its answer.
- **Sources:** §S keys; every figure here marked *(verify)* is in §S.2.

**Read lines are paraphrase, never quotation.** This document quotes nothing
from the book. Its quotation marks enclose a misconception's wording, a
preset's label, a lab's tile or a code string. A section number marked *(check)*
is one the accuracy review was not sure of.

Preset ids are suggestions; **the instances are not optional**. Every figure
below was computed by the reference model in §D.4 from the instance given, and
an author who changes an instance recomputes it and records it here in the
same commit. Snippets are Java, four-space indent, at most 20 lines unless an
entry says otherwise. Line numbers count every line of the snippet from 1,
blank and comment lines included (§D.0).

Misconceptions are a reading of the chapter someone could hold, or the view the
chapter argues against stated at its strongest — never a jibe at a language or
a methodology. Where a misconception is a position someone holds (the
"real programmers write code first" school, the cowboy coder McConnell names,
a later author who disagrees), the lesson names its holder or its school.

### Course 1 — Laying the Foundation (`code-complete-laying-the-foundation`, 4)

Part I, Chapters 1–4. What construction is, which picture of software to work
with, what must be settled upstream, and the decisions taken at the start of
construction. Its `how_to` says the course has the least code of any, because
the book's first Part is about the work around the code; its `not_covered`
says requirements engineering and architecture are named, not taught.

1. **what-software-construction-is** — What Software Construction Is — *Chapter 1 · Welcome to Software Construction* — 12 min
   - **Read:** §1.1, the activities the book calls construction (detailed
     design, coding and debugging, unit and integration testing of your own
     code, reviewing others' code and having yours reviewed, polishing,
     tuning) set against problem definition, requirements, architecture,
     system testing and maintenance; §1.2, why construction matters (a large
     share of the project, the one activity sure to happen, the source code
     often the only accurate description of the software); §1.3, how to
     read the book.
   - **Do:** classify a project's activities as construction or not, by the
     chapter's list, and compute construction's share of the hours.
   - **Standard:** given seven activities with hours, mark the construction
     ones and state their share as a fraction and a percentage.
   - **Lab:** `profile/shares`, family 3, records `name, hours, c` (the third
     field marks construction; `cfg["tag_label"] = "construction"`).
     Presets (illustrative, labelled so): `small-project` (requirements 80;
     architecture 50; detailed design 120, c; coding and debugging 320, c;
     unit testing 130, c; integration 90, c; system testing 110; planning and
     management 100 → `pfTotal` 1,000 hours, `pfTagged` 33/50 = 66%, `pfTop`
     coding and debugging, 8/25 = 32%), `large-project` (1,400; 1,100;
     1,300 c; 2,700 c; 1,000 c; 1,200 c; 2,100; 1,200 → 12,000 hours,
     `pfTagged` 31/60 ≈ 51.7%, `pfTop` 9/40 = 22.5%). Pins `pfTagged`,
     `pfTotal`.
   - **Misconception:** "Construction is just typing in a design someone else
     finished." Refuted by the chapter's own list: detailed design, debugging,
     unit testing and integration are construction, and on the presets they
     are most of it.
   - **Worked:** 120 + 320 + 130 + 90 = 660 of 1,000 hours: 66%.
   - **Exercise:** requirements 40, detailed design 30, coding 90, code
     review 20, unit testing 40, system testing 50, user documentation 30 →
     construction is detailed design, coding, code review and unit testing,
     180 of 300 hours, 3/5 = 60%.
   - **Sources:** McConnell §§1.1–1.2; the share of a project construction
     takes *(verify, §S.2 F1)*.

2. **metaphors-for-software** — Metaphors for Software — *Chapter 2 · Metaphors* — 12 min
   - **Read:** §2.1, why metaphors matter (a model is a heuristic, not an
     algorithm, and better models have changed sciences); §2.2, how to use
     them; §2.3, writing (a single author, a first draft thrown away), farming
     (growing a system), accretion (the oyster: build a little at a time, a
     working system at every step), building (planning grows with the size of
     what is built, and changing the foundation late is expensive), and the
     toolbox; combining metaphors.
   - **Do:** compute what rests on a component in a dependency structure, and
     say what the building metaphor predicts about the cost of changing it.
   - **Standard:** given five dependencies, list everything that rests on a
     named component, directly and in all.
   - **Lab:** `deps/ripple`, family 2, edges `a, b` meaning *a rests on b*.
     Instance (the lesson's illustration): `ui, orders; orders, db; reports,
     db; db, schema; billing, orders; billing, db`. Presets `foundation`
     (changed `schema` → `dgDirect` "1: db", `dgAffected` "5: billing, db,
     orders, reports, ui"), `middle` (`orders` → "2: billing, ui" both),
     `paint` (`ui` → "0: none" both). Pins `dgDirect`, `dgAffected`.
   - **Misconception:** "Software is soft, so nothing about it is expensive to
     change." The building metaphor says the opposite about foundations, and
     the lab counts it: the schema carries five components, the user interface
     none.
   - **Worked:** `schema` ← `db` ← {`orders`, `reports`, `billing`};
     `orders` ← {`ui`, `billing`}: five in all.
   - **Exercise:** `logging, config; db, config; api, db; api, logging; web,
     api` — changing `config` reaches `db` and `logging` directly and four
     components in all (`api`, `db`, `logging`, `web`).
   - **Sources:** McConnell §§2.1–2.3.

3. **upstream-prerequisites** — Upstream Prerequisites — *Chapter 3 · Upstream Prerequisites* — 15 min
   - **Read:** §3.1, why prerequisites matter, and the appeal to the cost of
     fixing a defect late (the book's table of costs by phase introduced and
     phase detected); §3.2, the kind of software (business systems,
     mission-critical, embedded life-critical) and iterative against
     sequential approaches; §3.3–3.5, problem definition, requirements,
     architecture; §3.6, how much time to spend upstream.
   - **Do:** compute the relative cost of a set of defects from the phase each
     was introduced in and the phase it was found in, against finding each in
     the phase it was made.
   - **Standard:** given defects by introduced and detected phase and the
     cost table, compute the total cost range and the ratio to finding them
     early.
   - **Lab:** `defects/cost`, family 3. `cfg["table"]` is the book's table as
     the lesson gives it *(verify, §S.2 F3)*: introduced in requirements and
     found in requirements 1, architecture 3, construction 5–10, system test
     10, after release 10–100; introduced in architecture and found in
     architecture 1, construction 10, system test 15, after release 25–100;
     introduced in construction and found in construction 1, system test 10,
     after release 10–25. Records `introduced, detected, count` with stages
     `req arch cons test post`. Presets `found-late` (`req, test, 10; arch,
     post, 5; cons, test, 20` → `dfCost` 425–800, `dfEarly` 35, `dfRatio`
     85/7 ≈ 12.1× to 160/7 ≈ 22.9×), `found-early` (`req, req, 10; arch,
     arch, 5; cons, cons, 20` → 35, 35, 1× to 1×), `requirements-late`
     (`req, post, 10` → 100–1,000, 10, 10× to 100×). Pins `dfCost`,
     `dfRatio`.
   - **Misconception:** "Prerequisites belong to waterfall; an iterative team
     can skip them." The chapter argues the cost table applies to iterative
     projects too, and that the question is how much and when, not whether;
     the modern aside of this course lives here (§F.1).
   - **Worked:** 10 × 10 + 5 × (25 to 100) + 20 × 10 = 425 to 800 units,
     against 35 if each defect is caught where it was made.
   - **Exercise:** eight requirements defects found after release cost
     8 × (10 to 100) = 80 to 800 units against 8 caught in requirements.
   - **Sources:** McConnell §§3.1–3.6; the table's sources *(verify, §S.2
     F3)*; Boehm and Turner 2004 for the iterative discussion.

4. **key-construction-decisions** — Key Construction Decisions — *Chapter 4 · Key Construction Decisions* — 12 min
   - **Read:** §4.1, the choice of language and the book's table of
     statements in each language equivalent to one statement of C; §4.2,
     programming conventions; §4.3, your location on the technology wave and
     *programming into a language* rather than in it; §4.4, the major
     construction practices to select.
   - **Do:** convert a size in C statements to another language by the
     table's ratio, and the days it would take at a stated rate.
   - **Standard:** given a size in C statements, a ratio and a rate, compute
     the statements and the days, and say what the ratio does not measure.
   - **Lab:** `project/language`, family 3. Inputs `size` (C statements),
     `ratio` (from the table, *verify, §S.2 F4*), `rate` (statements a day,
     illustrative). Presets `java` (10,000; 2.5; 50 → `pjEquivalent`
     4,000, `pjDays` 80, `pjDaysC` 200), `python` (10,000; 6; 50 → 5000/3 ≈
     1,666.67, 100/3 ≈ 33.33, 200), `visual-basic` (10,000; 4.5; 50 →
     20000/9 ≈ 2,222.22, 400/9 ≈ 44.44, 200). Pins `pjEquivalent`, `pjDays`.
   - **Misconception:** "Choose the language that needs the fewest
     statements." The ratio is one input; the chapter also weighs the team's
     experience with the language, the kind of program, and conventions. The
     lab's rate is an assumption the lesson states, not a law.
   - **Worked:** 10,000 / 2.5 = 4,000 Java statements; at 50 a day, 80 days.
   - **Exercise:** 30,000 C statements in Java: 12,000 statements; at 60 a
     day, 200 days against 500 in C.
   - **Sources:** McConnell §§4.1–4.4; the ratio table and its sources
     *(verify, §S.2 F4)*; experience with a language *(verify, F5)*.

### Course 2 — Creating High-Quality Code (`code-complete-high-quality-code`, 8)

Part II, Chapters 5–9. Design, classes, routines, defensive programming and the
pseudocode programming process. Its `how_to` names the course's one idea —
managing complexity is software's primary technical imperative — and says that
every count in the course is a way of seeing complexity. `part_a.py` is
Chapters 5–6, `part_b.py` Chapters 7–9.

1. **design-challenges-and-complexity** — Design Challenges and Complexity — *Chapter 5 · Design in Construction* — 15 min
   - **Read:** §5.1, design as a wicked problem, sloppy, about trade-offs and
     restrictions, non-deterministic, heuristic and emergent; §5.2,
     accidental and essential difficulties (after Brooks), managing
     complexity as the primary technical imperative, the desirable
     characteristics of a design (minimal complexity, loose coupling, high
     fan-in, low-to-medium fan-out, stratification …), and the levels of
     design from system to routine.
   - **Do:** count the dependencies among a design's parts, the pairs that
     could interact, and the fan-in and fan-out, and say how layering changes
     them.
   - **Standard:** for five modules and their dependencies, compute the
     possible pairs, the connected pairs as a share, and the largest fan-in.
   - **Lab:** `deps/coupling`, family 2. Presets (illustrative):
     `everything-talks` (each of `ui orders billing stock db` uses every
     other: 20 edges → `dgModules` 5, `dgEdges` 20, `dgPairs` 10,
     `dgConnected` 1 = 100%), `layered` (`ui, orders; ui, billing; orders,
     stock; billing, stock; orders, db; billing, db; stock, db` → 7, 10,
     7/10 = 70%, `dgFanIn` db 3), `strict-layers` (`ui, orders; orders,
     stock; stock, db; ui, billing; billing, db` → 5, 10, 1/2 = 50%,
     `dgFanIn` db 2). Pins `dgEdges`, `dgConnected`, `dgFanIn`.
   - **Misconception:** "A good design is one that captures every
     relationship in the domain." The chapter's criterion is the reverse:
     minimal interaction, so that a programmer can hold one part in mind
     at a time.
   - **Worked:** five modules give 5·4/2 = 10 pairs; seven dependencies touch
     7 of them.
   - **Exercise:** six modules where every pair talks: 6·5/2 = 15 pairs, all
     connected; redraw as three layers and count again.
   - **Sources:** McConnell §§5.1–5.2; Brooks 1987; Simon 1996 and Rittel on
     wicked problems as the book cites them *(check)*.

2. **design-heuristics-and-information-hiding** — Design Heuristics and Information Hiding — *Chapter 5 · Design in Construction* — 15 min
   - **Read:** §5.3, the heuristics: find real-world objects, form consistent
     abstractions, encapsulate implementation details, inherit when it
     simplifies, hide secrets (after Parnas), identify areas likely to change,
     keep coupling loose, look for common patterns; §5.4, design practices
     (iterate, divide and conquer, top-down and bottom-up, prototyping,
     collaborative design, how much design is enough, capturing the work);
     §5.5, comments on popular methodologies.
   - **Do:** count the components that must change when a hidden detail
     changes, with the detail exposed and with it hidden behind one module.
   - **Standard:** given a dependency list, name the secret, count the
     modules that know it, and propose the one module that should.
   - **Lab:** `deps/ripple`, family 2. Presets: `exposed` (`invoice,
     csvformat; report, csvformat; export, csvformat; audit, csvformat;
     backup, csvformat; ui, report`, changed `csvformat` → `dgDirect` "5:
     audit, backup, export, invoice, report", `dgAffected` "6: audit, backup,
     export, invoice, report, ui"), `hidden` (`store, csvformat; invoice,
     store; report, store; export, store; audit, store; backup, store; ui,
     report` → `dgDirect` "1: store", `dgAffected` "7: audit, backup,
     export, invoice, report, store, ui"). Pins `dgDirect` on both,
     `dgAffected` on `hidden`.
   - **Misconception:** "Information hiding means fewer dependencies." On
     `hidden` the transitive count rises from 6 to 7; what falls is the number
     of modules whose code knows the format, from 5 to 1. The body explains the
     difference between the two tiles: one counts who must be edited, the
     other who a build would recompile (Programming Tools uses the second).
   - **Worked:** five modules parse the CSV format themselves; behind `store`
     only `store` does.
   - **Exercise:** three routines each take a date string and call
     `substring(0, 4)`, `substring(4, 6)` and `substring(6, 8)` on it; name
     the secret (the `yyyyMMdd` layout) and the one routine that should know
     it; changes when the format becomes `yyyy-MM-dd`: 3 before, 1 after.
   - **Sources:** McConnell §§5.3–5.5; Parnas 1972.

3. **abstract-data-types-and-interfaces** — Abstract Data Types and Interfaces — *Chapter 6 · Working Classes* — 15 min
   - **Read:** §6.1, the abstract data type and the benefits the chapter lists
     (hide implementation details, limit the effect of changes, make the
     interface more informative, work with real-world entities); §6.2, good
     class interfaces: a consistent level of abstraction, and encapsulation —
     no public data, no exposed implementation, no assumptions about the
     users of the class.
   - **Do:** count a class's fields, its public data and its routines by
     visibility, and say which public members break encapsulation.
   - **Standard:** for a class listing, state the field count, the public
     non-constant fields, and the routines a caller can reach.
   - **Lab:** `code/class`, family 1. Presets (snippets in §D.4):
     `public-fields` (an `Employee` with five public fields, a constructor
     and one method → `coFields` 5, `coPublicFields` 5, `coRoutines` 2,
     `coPublicRoutines` 2), `private-fields` (the same data private, with a
     constructor, two public readers and one private helper → 5, 0, 4, 3),
     `kitchen-sink` (a `Program` class mixing a command stack, a report, a
     printer and global data → 9, 2, 6, 6). Pins `coFields`,
     `coPublicFields`, `coPublicRoutines`.
   - **Misconception:** "A getter and setter for every field is
     encapsulation." The chapter's test is the abstraction the interface
     presents; `kitchen-sink`'s routines have no fields in public but six
     unrelated abstractions in one class.
   - **Worked:** `public-fields` exposes all five fields: any change to how
     salary is stored reaches every caller.
   - **Exercise:** `public class Point { public double x; public double y;
     private String label; public double distanceTo(Point other) {…} }` →
     3 fields, 2 public; make them private and name the routines a caller now
     needs.
   - **Sources:** McConnell §§6.1–6.2; the guidance on the number of data
     members *(verify, §S.2 F6)*.

4. **inheritance-containment-and-members** — Inheritance, Containment and Members — *Chapter 6 · Working Classes* — 15 min
   - **Read:** §6.3, containment ("has a") before inheritance ("is a"), the
     Liskov substitution principle, overridable routines, keeping hierarchies
     shallow, member functions and data, constructors; §6.4, reasons to
     create a class (and classes to avoid); §6.5, language-specific issues;
     §6.6, packages.
   - **Do:** compute the depth of an inheritance hierarchy and the number of
     leaf classes, and test a subclass against substitution.
   - **Standard:** for a hierarchy given as child–parent pairs, state the
     depth and the deepest class, and say whether a stated subclass can be
     used everywhere its parent is.
   - **Lab:** `deps/tree`, family 2. Presets: `shallow` (`Circle, Shape;
     Square, Shape; Triangle, Shape` → `dgDepth` 2, `dgClasses` 4,
     `dgLeaves` 3), `deep` (`Account, Record; DepositAccount, Account;
     SavingsAccount, DepositAccount; BonusSavings, SavingsAccount;
     HolidayBonusSavings, BonusSavings; ChristmasHolidaySavings,
     HolidayBonusSavings; CheckingAccount, DepositAccount` → 7,
     `dgDeepest` ChristmasHolidaySavings, 8 classes, 2 leaves). Pins
     `dgDepth`, `dgDeepest`.
   - **Misconception:** "Inheritance is the main way to reuse code." The
     chapter prefers containment and treats inheritance as a tool with costs;
     the depth tile counts one of them.
   - **Worked:** Record ← Account ← DepositAccount ← SavingsAccount ←
     BonusSavings ← HolidayBonusSavings ← ChristmasHolidaySavings: seven.
   - **Exercise:** `Dog, Mammal; Cat, Mammal; Mammal, Animal; Animal,
     LivingThing; Puppy, Dog` → depth 5 at `Puppy`. Then a substitution
     question in prose: a `Square` that extends `Rectangle` and overrides
     `setWidth` to set the height too breaks a caller that sets the width to
     4 and the height to 5 and expects an area of 20.
   - **Sources:** McConnell §§6.3–6.6; Liskov 1988 *(check year as cited)*;
     the hierarchy-depth guidance and its sources *(verify, §S.2 F7)*.

5. **reasons-to-create-a-routine** — Reasons to Create a Routine — *Chapter 7 · High-Quality Routines* — 15 min
   - **Read:** §7.1, the valid reasons (reduce complexity, introduce an
     intermediate abstraction, avoid duplicate code, support subclassing,
     hide sequences, improve portability, simplify tests, and more), and the
     point that even a two-line routine can be worth it; §7.2, cohesion,
     from functional (the one to aim for) through sequential, communicational
     and temporal to procedural, logical and coincidental; §7.3, good routine
     names.
   - **Do:** find the duplicated lines in a routine and say what routine
     would remove them, with its name and its one parameter.
   - **Standard:** in a listing, mark every repeated block, count the lines in
     all its copies, and write the header of the routine that replaces them.
   - **Lab:** `code/dupes`, family 1 (`cfg["min_run"] = 2`). Presets:
     `two-names` (the label printer with `ship` and `bill` variables →
     `coDupBlocks` 0: the kit matches text, and a copy with renamed variables
     is a copy it cannot see — the body says so), `copied` (the same printer
     reusing one variable `a` → 1 block, `coDupLines` 6, `coDupWhere` "lines
     3–5 and lines 7–9"), `extracted` (the printer calling `printAddress`
     twice → 0). Pins `coDupBlocks`, `coDupLines`.
   - **Misconception:** "Routines exist to avoid duplication, so code that is
     not repeated needs no routine." The chapter's first reason is reducing
     complexity, and `two-names` shows duplication a text match misses.
   - **Worked:** lines 3–5 equal lines 7–9: one block, two copies, six lines;
     `printAddress(Address a)` replaces them.
   - **Exercise:** the `copied` listing — name the routine (`printAddress`),
     its parameter, and the lines that remain (two calls).
   - **Sources:** McConnell §§7.1–7.3; cohesion after Stevens, Myers and
     Constantine 1974 as the book cites it *(check)*.

6. **routine-length-and-parameters** — Routine Length and Parameters — *Chapter 7 · High-Quality Routines* — 15 min
   - **Read:** §7.4, how long a routine can be, with the studies the book
     reviews; §7.5, parameters: order, using all of them, not using them as
     working variables, limiting their number, passing what the routine's
     abstraction needs; §7.6, functions versus procedures; §7.7, macros and
     inline routines.
   - **Do:** count a routine's lines and parameters, and regroup parameters
     that travel together into an object.
   - **Standard:** for a routine header and body, state its code lines and
     parameter count, and propose a header with fewer parameters that keeps
     the abstraction.
   - **Lab:** `code/size`, family 1. Presets: `nine-parameters` (an invoice
     line printer whose header spans three lines → `coParams` 9, `coCode` 9,
     `coLines` 10), `parameter-objects` (the same printer taking an
     `InvoiceLine`, a `TaxRule` and a `Format` → 3, 5, 6). Pins `coParams`,
     `coCode`.
   - **Misconception:** "Shorter is always better." The book's position on
     length is more tolerant than much later advice *(verify the figures,
     §S.2 F8)*; the modern aside of this course lives here (§F.1). Parameters
     are where the book is firm *(verify, F9)*.
   - **Worked:** nine parameters, six of which describe the line or its tax,
     become two objects and a format.
   - **Exercise:** `void schedule(String name, int year, int month, int day,
     int hour, int minute, int durationMinutes, String room)` — 8 parameters;
     the five time fields become one `LocalDateTime` and the header has 4.
   - **Sources:** McConnell §§7.4–7.7 *(verify, §S.2 F8, F9)*.

7. **defensive-programming** — Defensive Programming — *Chapter 8 · Defensive Programming* — 15 min
   - **Read:** §8.1, protecting the program from invalid inputs; §8.2,
     assertions; §8.3, error-handling techniques (neutral value, next valid
     data, closest legal value, logging, error codes, shutting down) and
     robustness against correctness; §8.4, exceptions; §8.5, barricades;
     §8.6, debugging aids and offensive programming; §8.7–8.8, how much to
     leave in production, and being defensive about defensive programming.
   - **Do:** compare a validation check with its specification over every
     integer and list where they disagree.
   - **Standard:** given a specification interval and a check, name the
     integers the check gets wrong, by hand, from its comparisons.
   - **Lab:** `cond/range`, family 2. Spec: a month is valid from 1 to 12;
     the check flags *invalid* (`cfg["means"] = "invalid"`). Presets:
     `correct` (`month < 1 || month > 12` → `cdDisagree` none, `cdTests` 0,
     1, 2, 11, 12, 13, `cdExposed` none), `off-by-one` (`month < 0 || month >
     12` → `cdDisagree` 0, `cdExposed` 0), `wrong-operators` (`month <= 1 ||
     month >= 12` → 1, 12). Pins `cdDisagree`, `cdExposed`.
   - **Misconception:** "Defensive programming means checking everything
     everywhere." The chapter puts checks at a barricade and assertions
     inside it, and warns against too much; the lab's point is that a check
     written once at the barricade must be right at its ends.
   - **Worked:** `month < 0` lets 0 through: the only disagreement is the
     integer 0.
   - **Exercise:** `if (age < 0 && age > 120) reject();` with ages 0 to 120
     valid — the `&&` can never be true; the check accepts every age, and
     disagrees on −1 and below and 121 and above; the boundary tests −1 and
     121 expose it.
   - **Sources:** McConnell §§8.1–8.8.

8. **the-pseudocode-programming-process** — The Pseudocode Programming Process — *Chapter 9 · The Pseudocode Programming Process* — 15 min
   - **Read:** §9.1, the steps in building classes and routines; §9.2,
     pseudocode for professionals (English, at the level of intent, not of
     the language); §9.3, the process: design the routine, write pseudocode,
     turn it into comments, fill in code beneath each, check, clean up,
     repeat; §9.4, alternatives (test-first, refactoring, design by contract,
     hacking).
   - **Do:** check that every pseudocode comment in a routine has the code
     it promised beneath it.
   - **Standard:** for a routine written by the process, list its steps,
     find any step with no code, and name the code that is missing.
   - **Lab:** `code/ppp`, family 1. Preset `free-slot` (a routine with five
     pseudocode comments, one of which, "if no slot is free, log the
     overflow", has nothing beneath it → `coSteps` 5, `coCode` 7, `coEmpty`
     "line 14", `coMaxUnder` "3 lines, under line 8"); preset `complete` (the
     same routine with `log.warn("table full");` added under line 14 →
     `coSteps` 5, `coCode` 8, `coEmpty` none). Pins `coSteps`, `coEmpty`.
     (The `complete` figures are the model's arithmetic on the stated edit;
     the author confirms with `--observe`.)
   - **Misconception:** "Pseudocode is a draft you delete once the code
     works." The process keeps it as the routine's comments, which is why a
     step with no code beneath it is a defect the reader can see.
   - **Worked:** five steps, seven code lines; the step at line 14 is empty.
   - **Exercise:** the `expireSessions` listing in §D.4 — 4 steps; the step
     "remove it from the live list" (line 10) has no code, so expired sessions
     stay live.
   - **Sources:** McConnell §§9.1–9.4.

### Course 3 — Variables (`code-complete-variables`, 6)

Part III, Chapters 10–13. Declaring, initialising, scoping and naming
variables, and the data types. Its `how_to` says every lab here reads code, and
that the reader should paste a routine of their own into each.

1. **declaring-and-initializing-variables** — Declaring and Initializing Variables — *Chapter 10 · Using Variables* — 15 min
   - **Read:** §10.1, data literacy; §10.2, making declarations easy and the
     danger of implicit declarations; §10.3, guidelines for initialising:
     initialise each variable as it is declared, or close to where it is first
     used, use `final` where possible, reset counters and accumulators, check
     input parameters.
   - **Do:** find each variable read before it is set, set twice with no use
     between, or set and never used, reading the listing top to bottom.
   - **Standard:** for a short routine, list every such anomaly with its line,
     and say which the compiler would catch.
   - **Lab:** `code/dataflow`, family 1. Presets: `count-unset` (an average
     routine declaring `int count;` and incrementing it → `coAnomalies` 1,
     `coUsedBeforeSet` "count (line 6)"), `initialized` (the same routine with
     `int count = 0;` beside `total` → 0), `set-twice` (`total` and `count`
     initialised then overwritten, and an `average` computed and not used →
     3: `coSetTwice` "total (lines 2, 4), count (lines 3, 5)", `coUnused`
     "average (line 6)"). Pins `coAnomalies`, `coUsedBeforeSet`, `coSetTwice`.
   - **Misconception:** "The compiler catches uninitialised variables." Java's
     does, for locals, which `count-unset` shows by refusing to compile; C and
     C++ do not, fields default silently, and the exercise is one the lab's
     top-to-bottom reading misses.
   - **Worked:** line 6 reads `count` in `count = count + 1` and nothing
     before it set `count`.
   - **Exercise:** `String result; if (first.length() > 0) { result =
     first.substring(0, 1); } result = result + last.substring(0, 1);` — the
     lab reports nothing, because it reads lines in order and line 4 sets
     `result` before line 6 reads it; on the path where the `if` is false,
     line 6 reads an unset variable. The lesson's `note` says this is the
     lab's limit.
   - **Sources:** McConnell §§10.1–10.3.

2. **scope-span-and-live-time** — Scope, Span and Live Time — *Chapter 10 · Using Variables* — 15 min
   - **Read:** §10.4, scope: localise references (span), keep variables live
     for as short a time as possible (live time), the measures and the book's
     worked examples; §10.5, persistence; §10.6, binding time; §10.7, data
     types and control structures; §10.8, one purpose per variable.
   - **Do:** compute each variable's spans and live time and the averages,
     and move declarations to shrink them.
   - **Standard:** given the lines on which two variables are referenced,
     compute every span, the average span and each live time.
   - **Lab:** `code/span`, family 1, `vars` = `index total done`. Presets:
     `declared-at-top` (all three initialised under a comment at the top →
     `index` lines 3, 8, 9, 10; `total` 4, 14, 15, 17; `done` 5, 13, 15;
     `coAvgSpan` 11/4 = 2.75, `coAvgLive` 11, `coLongest` "total: 14"),
     `declared-near-use` (each declared just before its loop → spans 0, 0, 0;
     2, 0, 1; 0, 1; `coAvgSpan` 1/2 = 0.50, `coAvgLive` 5, `coLongest` "total:
     7"). Pins `coAvgSpan`, `coAvgLive`.
   - **Misconception:** "Declaring every variable at the top makes them easy
     to find." The chapter's measure says what it costs: an average live time
     of 11 lines against 5 for the same code.
   - **Worked:** `total` on lines 4, 14, 15 and 17: spans 9, 0, 1; live time
     17 − 4 + 1 = 14.
   - **Exercise:** `total` referenced on lines 2, 9, 12 and `count` on 3, 10,
     12 → spans 6, 2 and 6, 1, average 15/4 = 3.75; live times 11 and 10.
     Move both declarations below the four `print…` calls and recompute.
   - **Sources:** McConnell §§10.4–10.8; the definitions of span and live
     time and the book's example figures *(verify, §S.2 F10)*.

3. **the-power-of-variable-names** — The Power of Variable Names — *Chapter 11 · Variable Names* — 15 min
   - **Read:** §11.1, choosing a good name (the problem, not the solution;
     optimum length; scope and name length; computed-value qualifiers; common
     opposites); §11.2, naming specific types (loop indexes, status
     variables, temporaries, booleans, enums, constants); §11.3–11.4, naming
     conventions, informal and standardised (prefixes); §11.5, short names;
     §11.6, kinds of names to avoid.
   - **Do:** compute the average length of a routine's names, leaving out
     loop indexes, and rename the short ones for the problem they describe.
   - **Standard:** for a routine, list its declared names with lengths,
     compute the average without loop indexes, and propose names for those
     under eight characters.
   - **Lab:** `code/names`, family 1, `cfg["min"] = 8` (the lesson's
     threshold, after the study the book cites, §S.2 F11). Presets:
     `short-names` (`calc(double[] a, int n, double r)` with `t`, `x`, `tmp`
     → `coNames` 7, `coAvgLen` 4/3 ≈ 1.33, `coShort` "a, n, r, t, x, tmp";
     loop index `i` not counted), `problem-names` (`averageNetPrice(double[]
     grossPrices, int priceCount, double netFactor)` with `netTotal`,
     `netPrice`, `averageNet` → 7, 28/3 ≈ 9.33, none). Pins `coAvgLen`,
     `coShort`.
   - **Misconception:** "Longer names are always better." The study the book
     reports found a range, not a direction *(verify, F11)*, and the chapter
     keeps short names for loop indexes; the modern aside of this course lives
     here (prefix conventions and today's editors, §F.1).
   - **Worked:** 11 + 10 + 9 + 8 + 8 + 10 = 56 characters over 6 names: 28/3
     ≈ 9.33.
   - **Exercise:** `double f(double p, int n, double r)` with `m` and `t` →
     average 1; renamed `totalInterest(double principal, int months, double
     annualRate)` with `monthlyInterest`, `totalInterest` → 53/5 = 10.6, and
     only `months` is under eight.
   - **Sources:** McConnell §§11.1–11.6 *(verify, §S.2 F11)*.

4. **integers-and-floating-point** — Integers and Floating Point — *Chapter 12 · Fundamental Data Types* — 15 min
   - **Read:** §12.1, numbers in general (avoid magic numbers, anticipate
     divide-by-zero, make conversions obvious, avoid mixed-type comparisons);
     §12.2, integers (integer division, overflow, overflow in intermediate
     results); §12.3, floating point (adding numbers of very different size,
     equality comparisons, rounding, decimal types).
   - **Do:** compute what Java's `int`, `long` and `double` give for an
     operation repeated, against the exact result, and say why they differ.
   - **Standard:** for an `int` product that overflows, compute the wrapped
     value; for a decimal fraction added ten times as `double`, say whether
     the result equals the exact one.
   - **Lab:** `run/arith`, family 2. Presets: `int-max-plus-one` (`int`,
     2147483647 + 1, once → `nuJava` −2147483648, `nuExact` 2,147,483,648,
     `nuEqual` no), `square-overflow` (`int`, 46341 × 46341 → −2147479015
     against 2,147,488,281), `long-square` (the same in `long` → 2147488281,
     yes), `int-division` (`int`, 7 / 2 → 3 against 7/2), `tenth-ten-times`
     (`double`, 0 + 0.1, ten times → `nuJava` 0.9999999999999999, `nuExact`
     1, `nuEqual` no, `nuStored` 9007199254740991/9007199254740992), `cents`
     (`int`, 0 + 10, ten times → 100, yes). Pins `nuJava`, `nuEqual`.
   - **Misconception:** "A `double` holds 0.1." It holds the nearest binary
     fraction, and the lab prints it exactly; ten of them make
     0.9999999999999999. Counting money in whole cents (`cents`) is the
     chapter's remedy.
   - **Worked:** 46341² = 2,147,488,281, which is 2³¹ + 4,633; the `int`
     wraps to −2,147,479,015.
   - **Exercise:** `int msPerYear = 365 * 24 * 60 * 60 * 1000;` — the exact
     value 31,536,000,000 does not fit in an `int`; Java gives 1471228928;
     writing `1000L` makes the product `long` and correct.
   - **Sources:** McConnell §§12.1–12.3; Goldberg 1991 for the
     floating-point background if the book cites it *(check)*.

5. **named-constants-and-other-types** — Named Constants and Other Types — *Chapter 12 · Fundamental Data Types* — 15 min
   - **Read:** §12.4, characters and strings; §12.5, boolean variables used to
     document a test; §12.6, enumerated types; §12.7, named constants, with
     the rule that the only literals in a routine's body should be 0 and 1
     *(verify, §S.2 F12)*; §12.8, arrays; §12.9, creating your own types.
   - **Do:** list a routine's magic numbers, count them, and replace them
     with named constants.
   - **Standard:** for a routine, list every literal other than 0 and 1 with
     its lines, and write the constant declarations that replace them.
   - **Lab:** `code/literals`, family 1. Presets: `magic` (a mortgage
     payment routine with 0.0725, 12 twice and 360 twice → `coMagic` 5,
     `coDistinct` 3, `coMagicList` "0.0725 (line 2), 12 (lines 2, 3), 360
     (lines 4, 5)"), `named` (the same with `ANNUAL_RATE`,
     `MONTHS_PER_YEAR`, `MAX_TERM_MONTHS` declared `static final` → 0). Pins
     `coMagic`, `coMagicList`.
   - **Misconception:** "A literal used only once is harmless." The chapter's
     reasons are readability and a single point of change; `12` appearing
     twice with one meaning is the case the lab catches, and a single `0.0725`
     still does not say it is an annual rate.
   - **Worked:** `0.0725 / 12` becomes `ANNUAL_RATE / MONTHS_PER_YEAR`.
   - **Exercise:** a monitoring loop with `38.5`, `3` and `900` → 3 magic
     numbers, 3 distinct (`FEVER_CELSIUS`, `URGENT_PRIORITY`,
     `CHECK_INTERVAL_SECONDS`).
   - **Sources:** McConnell §§12.4–12.9 *(verify, §S.2 F12)*.

6. **structures-pointers-and-global-data** — Structures, Pointers and Global Data — *Chapter 13 · Unusual Data Types* — 15 min
   - **Read:** §13.1, structures; §13.2, pointers (where errors come from,
     general tips; the C++ and C detail is named, not taught — §G); §13.3,
     global data: its problems, reasons to use it, using access routines
     instead.
   - **Do:** count the routines coupled to one another through global
     variables, and how access routines change the count.
   - **Standard:** for a table of routines and the globals each reads and
     writes, count the coupled pairs (two routines that share a global one
     of them writes).
   - **Lab:** `deps/shared`, family 2, records `routine, access, global` with
     access `r`, `w` or `rw`. Presets: `globals` (`readInput, w, current;
     validate, r, current; validate, w, errors; report, r, errors; report, r,
     current; reset, w, errors; reset, w, current; addLine, r, current;
     addLine, rw, total; printTotals, r, total` → `dgGlobals` 3,
     `dgRoutines` 6, `dgCoupled` 9 of 15 pairs, `dgMostShared` "current, 5
     routines"), `access-routines` (`currentRecord, rw, current; errorLog, rw,
     errors; runningTotal, rw, total` → 3, 3, 0). Pins `dgCoupled`,
     `dgMostShared`.
   - **Misconception:** "Global data is fine as long as it is only read." A
     reader is coupled to every writer, and `globals` has two writers of
     `current`; the access routines leave each global with one owner.
   - **Worked:** `current` has writers `readInput` and `reset` and readers
     `validate`, `report`, `addLine`: 7 coupled pairs; `errors` adds
     `validate`–`report`; `total` adds `addLine`–`printTotals`: 9.
   - **Exercise:** `load, w, config; render, r, config; save, r, config;
     render, w, cache; save, r, cache` → 2 globals, 3 routines, all 3 pairs
     coupled.
   - **Sources:** McConnell §§13.1–13.3.

### Course 4 — Statements (`code-complete-statements`, 7)

Part IV, Chapters 14–19. Straight-line code, conditionals, loops, unusual
control structures, tables and the general issues of control. Its `how_to` says
the course's last lesson, Nesting and Complexity, gathers the counts of the
others into one. `part_a.py` is Chapters 14–17, `part_b.py` 18–19.

1. **organizing-straight-line-code** — Organizing Straight-Line Code — *Chapter 14 · Straight-Line Code* — 12 min
   - **Read:** §14.1, statements that must be in a specific order: make the
     dependencies obvious through names, parameters and comments; §14.2,
     statements whose order does not matter: read top to bottom, group related
     statements.
   - **Do:** list the order dependencies between statements (which line reads
     what another line wrote), and find the statement that reads a value
     before it is computed.
   - **Standard:** for six statements, list each dependency as *i → j* and
     reorder them so that none points backwards.
   - **Lab:** `code/dataflow`, family 1 (the `coDeps` tile). Presets:
     `total-first` (`total` summed on line 2 from `marketing`, `sales` and
     `travel`, which lines 3–5 then compute → `coAnomalies` 6,
     `coUsedBeforeSet` "marketing (line 2), sales (line 2), travel (line
     2)"), `in-order` (the same statements reordered → 0, `coDeps` "1→2, 1→3,
     1→4, 2→5, 3→5, 4→5, 5→6"), `hidden` (`ledger.computeMarketing();
     ledger.computeSales(); ledger.computeTravel(); ledger.printReport();` →
     0, `coDeps` "1→2, 1→3, 1→4, 1→5"). Pins `coAnomalies`, `coDeps`.
   - **Misconception:** "If the code compiles, its order is right." `hidden`
     compiles in any order, and the lab sees no dependency between its
     calls, because they pass nothing; the chapter's remedy is to make the
     order visible in the parameters.
   - **Worked:** in `in-order`, line 5 reads what lines 2, 3 and 4 wrote.
   - **Exercise:** rewrite `hidden` so each call takes the result of the
     previous one, and list the dependencies the lab then finds.
   - **Sources:** McConnell §§14.1–14.2.

2. **using-conditionals** — Using Conditionals — *Chapter 15 · Conditionals* — 12 min
   - **Read:** §15.1, `if` statements: the nominal path first, the normal
     case after the `if`, the `else` considered, chains of `if-then-else`
     tests in order of frequency, all cases covered, the last `else` catching
     errors; §15.2, `case` statements: ordering cases, tips (simple actions,
     the default for errors, fall-through in C-family languages).
   - **Do:** compute the average number of tests an `if-else-if` chain makes
     from the frequencies of its cases, and reorder it.
   - **Standard:** given a chain's cases in order with frequencies, compute
     the expected tests, and the expected tests with the cases in order of
     frequency.
   - **Lab:** `search/chain`, family 2, records `case, frequency` in chain
     order; a final `else` costs as many tests as there are conditions.
     Presets (illustrative frequencies for classifying characters):
     `as-written` (`digit, 5; punctuation, 10; space, 15; letter, 70` →
     `seExpected` 7/2 = 3.50, `seBest` 3/2 = 1.50, `seSaved` 2),
     `letters-first` (`letter, 70; space, 15; punctuation, 10; else, 5` →
     29/20 = 1.45, 29/20 = 1.45, 0), `else-is-common` (`digit, 5;
     punctuation, 10; space, 15; else, 70` → 14/5 = 2.80, 13/5 = 2.60,
     1/5 = 0.20). Pins `seExpected`, `seBest`.
   - **Misconception:** "The order of mutually exclusive tests does not
     matter." It does not matter to the result; it matters to the cost, and
     to the reader, and the chapter weighs both.
   - **Worked:** (1·5 + 2·10 + 3·15 + 4·70)/100 = 3.5 tests; letters first,
     1.5.
   - **Exercise:** a request router testing `DELETE` (5%), `POST` (15%),
     `GET` (80%) in that order → 11/4 = 2.75 tests on average; reversed,
     5/4 = 1.25.
   - **Sources:** McConnell §§15.1–15.2.

3. **controlling-loops** — Controlling Loops — *Chapter 16 · Loops* — 15 min
   - **Read:** §16.1, selecting the kind of loop; §16.2, controlling it:
     entering, the body, exit, endpoints (off-by-one errors), loop variables,
     length and nesting; §16.3, creating a loop from the inside out; §16.4,
     the correspondence between loops and arrays.
   - **Do:** compute how many times a loop runs, the last value its index
     takes in the body and its value after the loop, from the header alone.
   - **Standard:** for four headers, state iterations, last value and value
     after, and say which never ends.
   - **Lab:** `run/loop`, family 2, inputs `start`, `cmp` (`lt le ne gt
     ge`, printed as the operator), `bound`, `step`. Presets: `fencepost`
     (0, le, 10, 1 → `lpIterations` 11, `lpLast` 10, `lpAfter` 11),
     `half-open` (0, lt, 10, 1 → 10, 9, 10), `counting-down` (10, ge, 0, −1 →
     11, 0, −1), `skips-the-bound` (0, ne, 9, 2 → `lpIterations` "never
     ends"). Pins all three tiles (`lpIterations` only on `skips-the-bound`).
   - **Misconception:** "`<=` and `<` differ by one only at the end." They
     differ in the count, the last value and the value after, and `!=` with a
     step that jumps the bound never stops.
   - **Worked:** `for (int i = 0; i <= 10; i++)` runs 11 times; `i` is 11
     after.
   - **Exercise:** `for (int i = 10; i > 0; i -= 3)` → 4 iterations (10, 7, 4,
     1), `i` is −2 after.
   - **Sources:** McConnell §§16.1–16.4; the guidance on loop length and
     nesting *(verify, §S.2 F13)*.

4. **unusual-control-structures** — Unusual Control Structures — *Chapter 17 · Unusual Control Structures* — 15 min
   - **Read:** §17.1, multiple returns from a routine (guard clauses);
     §17.2, recursion: tips, and the book's warning against recursion for
     factorials and Fibonacci numbers; §17.3, `goto`: the arguments for and
     against, with the history; §17.4, perspective.
   - **Do:** compute the calls, depth and loop iterations of a recursive
     routine against its iterative version.
   - **Standard:** for naive recursive Fibonacci at n, compute the number of
     calls (2·F(n + 1) − 1) and the iterations of the loop version.
   - **Lab:** `run/recursion`, family 2. Presets: `factorial-10` (→
     `lpCalls` 10, `lpDepth` 10, `lpValue` 3,628,800, `lpLoop` 9),
     `fibonacci-30` (→ 2,692,537, 30, 832,040, 29), `fibonacci-40` (→
     331,160,281, 40, 102,334,155, 39). Pins `lpCalls`, `lpLoop`.
   - **Misconception:** "Recursion is the natural way to compute Fibonacci
     numbers." The definition is recursive; the computation need not be. The
     history aside (Dijkstra's 1968 letter, Knuth's 1974 reply) is the modern
     aside of this course (§F.1).
   - **Worked:** F(31) = 1,346,269, so `fibonacci(30)` makes 2·1,346,269 − 1 =
     2,692,537 calls; the loop makes 29 additions.
   - **Exercise:** `fibonacci(20)` → 21,891 calls, depth 20, value 6,765; 19
     loop additions.
   - **Sources:** McConnell §§17.1–17.4; Dijkstra 1968; Knuth 1974.

5. **table-driven-methods** — Table-Driven Methods — *Chapter 18 · Table-Driven Methods* — 15 min
   - **Read:** §18.1, general considerations (how to look an entry up, what to
     store); §18.2, direct access (days in a month); §18.3, indexed access;
     §18.4, stair-step access (grades, rates), with its care over endpoints
     and the choice of linear or binary search; §18.5, other examples.
   - **Do:** look a key up in a stair-step table and count the comparisons
     a linear scan and a binary search make.
   - **Standard:** for a five-step grade table and a key, state the grade and
     both comparison counts, and say which endpoint rule the table uses.
   - **Lab:** `search/stairs`, family 2, records `upper bound, value` and a
     `rule` (`below`: the key is in the first step whose bound it is below;
     `atmost`: at or below). Instance `50, F; 65, D; 75, C; 90, B; 101, A`.
     Presets: `grade-72` (below → `seValue` C, `seLinear` 3, `seBinary` 2),
     `grade-90-below` (→ A, 5, 3), `grade-90-atmost` (→ B, 4, 3), and
     `brackets` (sixteen tax brackets `1000, 0%; 2000, 5%; … 16000, 75%` in
     steps of 1,000 and 5%, key 14,500 → 70%, 15, 4). Pins `seValue`,
     `seLinear`, `seBinary`.
   - **Misconception:** "A table is just a faster `if` chain." The chapter's
     case is that a table moves the logic into data, and the two 90 presets
     show where the remaining logic sits: in the endpoint rule.
   - **Worked:** 72 is not below 50 or 65 and is below 75: C, after 3
     comparisons; binary search tests 75, then 65: 2.
   - **Exercise:** shipping rates `1, 5; 5, 9; 20, 15; 70, 40` (kilograms,
     price): 5 kg with `below` costs 15 (3 comparisons linear), with `atmost`
     9 (2). Which does the business mean?
   - **Sources:** McConnell §§18.1–18.5.

6. **boolean-expressions** — Boolean Expressions — *Chapter 19 · General Control Issues* — 15 min
   - **Read:** §19.1, boolean expressions: `true` and `false` rather than 1
     and 0, simplifying with well-named boolean variables or functions,
     forming them positively, DeMorgan's theorems, parentheses, short-circuit
     evaluation, number-line order, comparisons to 0; §19.2, compound
     statements; §19.3, null statements.
   - **Do:** decide by truth table whether two conditions agree on every
     row, and rewrite a negated condition by DeMorgan.
   - **Standard:** for two conditions over two variables, write the four rows
     and say whether they are equivalent; apply DeMorgan to `!(a || b)`.
   - **Lab:** `cond/truth`, family 2. Presets: `demorgan` (`!(done ||
     error)` against `!done && !error` → `cdEquivalent` yes), `half-demorgan`
     (against `!done || !error` → "no, on 2 of 4 rows", `cdFirstDiff` "done =
     T, error = F"), `redundant` (`(found && valid) || (found && !valid)`
     against `found` → yes), `double-negative` (`!(!ready || !loaded)` against
     `ready && loaded` → yes). Pins `cdEquivalent`, `cdFirstDiff`.
   - **Misconception:** "To negate a condition, negate each part." That is
     `half-demorgan`, and it is wrong on two rows; the `||` must also become
     `&&`.
   - **Worked:** `!(done || error)` is true only when both are false;
     `!done && !error` likewise; `!done || !error` is also true when exactly
     one is.
   - **Exercise:** `!(isAdmin || !isOwner)` simplifies to `!isAdmin &&
     isOwner`; the lab confirms equivalence on all 4 rows.
   - **Sources:** McConnell §§19.1–19.3; De Morgan as the book names him.

7. **nesting-and-complexity** — Nesting and Complexity — *Chapter 19 · General Control Issues* — 15 min
   - **Read:** §19.4, taming deep nesting (retest part of the condition,
     break out early, convert to `if-else-if` or `case`, factor into routines,
     use polymorphism); §19.5, structured programming (sequence, selection,
     iteration); §19.6, control structures and complexity: the decision-point
     count after McCabe, and the book's guidance for reading it.
   - **Do:** count a routine's decision points by the chapter's rule and its
     nesting depth, and flatten it with guard clauses.
   - **Standard:** for a 20-line routine, state the decision points with
     their breakdown and the deepest nesting, by hand.
   - **Lab:** `code/complexity`, family 1. Presets: `nested-shipping` (a
     shipping-cost routine nested five deep → `coDecisions` 9,
     `coBreakdown` "1 + if 5 + for 1 + && 1 + || 1", `coBand` "6–10",
     `coDepth` 5, `coDeepest` line 14), `guard-clauses` (the same rules as
     guard clauses, the international branch moved into a routine of its own
     → 6, "1 + if 3 + && 1 + || 1", "6–10", 1). Pins `coDecisions`,
     `coDepth`.
   - **Misconception:** "Flattening the code reduces its complexity." It
     reduces the nesting a reader holds at once (5 to 1); the decision points
     fall from 9 to 6 only because three moved into `internationalCost`, where
     they are still to be read. The band tile reads the book's guidance
     *(verify, §S.2 F14)*; it is a reason to look.
   - **Worked:** 1 + five `if`s + one `for` + one `&&` + one `||` = 9.
   - **Exercise:** the `discountPercent` routine in §D.4 → 7 decision points
     (1 + if 3 + for 1 + && 1 + || 1), depth 2.
   - **Sources:** McConnell §§19.4–19.6; McCabe 1976; Böhm and Jacopini 1966;
     nesting guidance *(verify, F15)*.

### Course 5 — Code Improvements (`code-complete-code-improvements`, 8)

Part V, Chapters 20–26. Quality, collaboration, testing, debugging,
refactoring and tuning. Its `how_to` says the defect-removal figures are
averages from many organisations' projects, quoted by the book from Capers
Jones and others, and every lab that uses them says so. `part_a.py` is
Chapters 20–22, `part_b.py` 23–26.

1. **the-software-quality-landscape** — The Software-Quality Landscape — *Chapter 20 · The Software-Quality Landscape* — 15 min
   - **Read:** §20.1, external and internal characteristics of quality;
     §20.2, techniques for improving quality; §20.3, the relative
     effectiveness of the techniques, with the book's table of defect-detection
     rates and the argument for combining techniques; §20.4, when to do
     quality assurance; §20.5, the general principle of software quality —
     improving quality reduces cost.
   - **Do:** compute the share of defects a sequence of removal stages
     catches, and the number left, from each stage's rate.
   - **Standard:** for three stages with stated rates and 1,000 defects,
     compute the found, the remaining and the combined rate.
   - **Lab:** `defects/removal`, family 3, rates as the lesson gives them
     from the book's table (modal values) *(verify, §S.2 F16)*. Presets:
     `testing-only` (1,000 defects; unit test 30%, integration test 35%,
     system test 40% → `dfFound` 727, `dfRemaining` 273, `dfCombined`
     727/1000 = 72.7%), `inspections-too` (design inspection 55%, code
     inspection 60%, then the three tests → 47543/50 = 950.86, 2457/50 =
     49.14, 47543/50000 ≈ 95.1%), `one-stage` (unit test only → 300, 700,
     30%). Pins `dfCombined`, `dfRemaining`.
   - **Misconception:** "Testing is how you get quality." The chapter's table
     puts no single technique much above the middle, and the lab's product
     shows why combining unlike techniques is the argument. The model assumes
     each stage catches its share of what is left, independently, and the
     `note` says so.
   - **Worked:** 1,000 × 0.70 × 0.65 × 0.60 = 273 left; 72.7% caught.
   - **Exercise:** two stages at 40% and 50% → 1 − 0.6 × 0.5 = 70%; three at
     30% → 1 − 0.343 = 65.7%.
   - **Sources:** McConnell §§20.1–20.5; Jones 1996, 2000 *(verify, §S.2
     F16, F17)*.

2. **collaborative-construction** — Collaborative Construction — *Chapter 21 · Collaborative Construction* — 15 min
   - **Read:** §21.1, an overview of collaborative practices and why they
     work alongside testing; §21.2, pair programming; §21.3, formal
     inspections (roles, stages, egos); §21.4, other kinds (walk-throughs,
     code reading, dog-and-pony shows); the comparison of techniques.
   - **Do:** compute defects found, defects left and hours spent by a
     pipeline of stages with rates and hours per defect found.
   - **Standard:** for an inspection followed by two tests, compute the hours
     per defect found and the defects left, against testing alone.
   - **Lab:** `defects/pipeline`, family 3, records `stage, rate, hours per
     defect` *(rates and hours: verify, §S.2 F16, F18)*. Presets: `test-only`
     (100 defects; unit test 30%, 20 h; system test 40%, 20 h → `dfFound` 58,
     `dfRemaining` 42, `dfHours` 1,160, `dfPerDefect` 20), `inspect-first`
     (code inspection 60%, 3.5 h, then the same tests → 416/5 = 83.2, 84/5 =
     16.8, 674, 1685/208 ≈ 8.10), `three-and-twelve` (inspection 3 h, tests 12
     h, rates as `inspect-first` → 83.2, 16.8, 2292/5 = 458.4, 573/104 ≈
     5.51). Pins `dfRemaining`, `dfHours`, `dfPerDefect`.
   - **Misconception:** "Reviews cost time that testing would not." The
     pipeline counts the hours: the inspection's defects are the cheap ones,
     and fewer reach the expensive stages.
   - **Worked:** 60 found at 3.5 h = 210 h; 12 at 20 h = 240 h; 11.2 at 20 h =
     224 h; 674 h for 83.2 defects.
   - **Exercise:** 50 defects, code review 50% at 3 h, testing 50% at 12 h →
     37.5 found, 12.5 left, 225 hours, 6 hours per defect.
   - **Sources:** McConnell §§21.1–21.4; Fagan 1976 *(verify, §S.2 F18)*.

3. **structured-basis-testing** — Structured Basis Testing — *Chapter 22 · Developer Testing* — 15 min
   - **Read:** §22.1, developer testing's role in quality, and testing during
     construction; §22.2, recommended approach and test-first; §22.3, the bag
     of tricks up to and including structured basis testing: the minimum
     number of test cases, counted from the routine's decision points, plus
     one for a `case` statement with no default.
   - **Do:** count the basis test cases a routine needs and write one test
     per decision point.
   - **Standard:** for a routine with a `while`, an `&&` and two `if`s, state
     the count and one input per case.
   - **Lab:** `code/basis`, family 1. Presets: `overtime` (a payroll loop →
     `coBasis` 5, `coPoints` "while line 4, && line 4, if line 6, if line 8"),
     `switch-without-default` (a three-case `switch` and an `if` → 6,
     `coNoDefault` 1). Pins `coBasis`, `coNoDefault`.
   - **Misconception:** "Full statement coverage means the routine is
     tested." Basis testing asks for each decision's outcomes; a test suite
     can run every line of `overtime` without the case where `staff[i]` is
     `null`. The modern aside of this course lives here: the book's §22.2
     discussion of test-first, set beside test-driven development as later
     practised (§F.1).
   - **Worked:** 1 + `while` + `&&` + `if` + `else if` = 5 cases.
   - **Exercise:** the `archiveOld` routine in §D.4 (a `for`, an `if` with
     `||`) → 4 cases; one input each: an empty inbox, an old message, a spam
     message, a new non-spam message.
   - **Sources:** McConnell §§22.1–22.3 *(check that basis testing falls in
     the first half)*.

4. **boundaries-and-bad-data** — Boundaries and Bad Data — *Chapter 22 · Developer Testing* — 15 min
   - **Read:** the rest of §22.3: data-flow testing, equivalence partitioning,
     error guessing, boundary analysis and compound boundaries, classes of bad
     data and of good data; §22.4, typical errors (where they cluster, the
     classification, how many to expect *(verify, §S.2 F19)*); §22.5, test
     support tools; §22.6, improving the testing; §22.7, keeping test records.
   - **Do:** list the boundary test values for a range and find which of them
     exposes a wrong check.
   - **Standard:** for a valid range and a check, write the six boundary
     values and name each that the check gets wrong.
   - **Lab:** `cond/range`, family 2. Spec: an order of 1 to 99 items is
     valid; the check says *valid*. Presets: `correct` (`qty >= 1 && qty <=
     99` → `cdDisagree` none, `cdTests` 0, 1, 2, 98, 99, 100, `cdExposed`
     none), `strict-top` (`qty > 0 && qty < 99` → 99, exposed 99),
     `no-lower-check` (`qty <= 99` → `cdDisagree` "0 and below",
     `cdExposed` 0). Pins `cdDisagree`,
     `cdExposed`.
   - **Misconception:** "One typical value per case is enough." A nominal 50
     passes all three checks; only the boundary values tell them apart.
   - **Worked:** `qty < 99` rejects 99, the largest valid order; the test 99
     catches it, 50 does not.
   - **Exercise:** passwords of 8 to 64 characters, check `len > 8 && len <=
     64` → tests 7, 8, 9, 63, 64, 65; the check is wrong at 8 only.
   - **Sources:** McConnell §§22.3–22.7 *(verify, §S.2 F19)*; Myers 1979.

5. **debugging-as-science** — Debugging as Science — *Chapter 23 · Debugging* — 15 min
   - **Read:** §23.1, overview: the variation among programmers in finding
     defects *(verify, §S.2 F20)*, defects as opportunities, an ineffective
     approach; §23.2, finding a defect by the scientific method (stabilise,
     locate, fix, test, look for similar), with its tips — narrow the
     suspicious region, binary search, brute force with a time limit;
     §23.3, fixing; §23.4, psychological considerations; §23.5, tools.
   - **Do:** compute the steps a binary search takes to locate a defect among
     n suspects, and the worst case.
   - **Standard:** for 1,000 suspect commits and the defect at a given one,
     list the halving intervals and count the steps; state the worst case for
     a million.
   - **Lab:** `search/bisect`, family 2, inputs `n`, `k` (the defect's
     position). Presets: `commit-637` (1,000, 637 → `seSteps` 10, `seWorst`
     10; intervals 1–1000, 501–1000, 501–750, 626–750, 626–688, 626–657,
     626–641, 634–641, 634–637, 636–637), `commit-63` (1,000, 63 → 9, 10),
     `sixty-four` (64, 1 → 6, 6). Pins `seSteps`, `seWorst`.
   - **Misconception:** "Debugging is reading the code until the defect shows
     itself." The chapter's method is experiment: a hypothesis, a test that
     halves the suspects, repeat; ten tests settle a thousand commits.
   - **Worked:** ⌈log₂ 1,000⌉ = 10; 2¹⁰ = 1,024 ≥ 1,000.
   - **Exercise:** a defect somewhere in 1,048,576 lines of a generated input
     file: at most 20 halvings; among 100 commits, at most 7.
   - **Sources:** McConnell §§23.1–23.5 *(verify, §S.2 F20)*.

6. **refactoring-safely** — Refactoring Safely — *Chapter 24 · Refactoring* — 15 min
   - **Read:** §24.1, kinds of software evolution; §24.2, introduction to
     refactoring and the reasons to refactor (duplicate code, long routines,
     long parameter lists, and the rest of the book's list); §24.3, specific
     refactorings at data, statement, routine, class and system level;
     §24.4, refactoring safely (small steps, one at a time, a list, tests,
     reviews, and the warning about small changes *(verify, §S.2 F21)*);
     §24.5, strategies.
   - **Do:** compute the inputs and outputs of a block before extracting it
     into a routine, and decide whether it extracts cleanly.
   - **Standard:** for a block in a routine, list the variables it reads that
     were set before it (parameters) and those it sets that are read after it
     (results); say what to do when there are two results.
   - **Lab:** `code/extract`, family 1, inputs `from`, `to`. Instance: a
     `printStatement` routine that totals transactions, charges an overdraft
     fee and prints. Presets: `print-lines` (lines 11–12 → `coIn` "fees,
     balance", `coOut` none, `coParams` 2), `fee-loop` (4–9 → `coIn`
     "account, balance, fees", `coOut` "balance, fees", 3), `from-the-top`
     (2–10 → "account", "balance, fees", 1). Pins `coIn`, `coOut`.
   - **Misconception:** "Extract Routine is always safe." It is safe when
     the block has at most one result; `fee-loop` has two, and Java returns
     one value, so the refactoring needs a small class or two routines first.
   - **Worked:** lines 11–12 read `fees` and `balance` and set nothing used
     later: `printTotals(fees, balance)`.
   - **Exercise:** the `printInvoice` routine in §D.4 — lines 2–5 extract
     cleanly as `subtotalOf(inv)` (in `inv`, out `subtotal`); lines 7–9 as
     `printTotals(subtotal, tax)`.
   - **Sources:** McConnell §§24.1–24.5; Fowler 1999.

7. **code-tuning-strategies** — Code-Tuning Strategies — *Chapter 25 · Code-Tuning Strategies* — 15 min
   - **Read:** §25.1, performance overview (quality characteristics and
     performance; efficiency through requirements, design, class and
     routine design, OS, compiler, hardware, and code tuning last); §25.2,
     introduction to tuning: the Pareto principle, old wives' tales, when to
     tune *(verify, §S.2 F22)*; §25.3, kinds of fat and molasses; §25.4,
     measurement; §25.5, iteration; §25.6, the approach.
   - **Do:** compute the overall speedup a change to one routine gives, from
     a profile, and say which routine is worth tuning.
   - **Standard:** for a four-routine profile and a speed factor on one
     routine, compute the new total, the speedup and the share saved.
   - **Lab:** `profile/speedup`, family 3, records `routine, ms, factor`
     (illustrative profile: parse 600, compute 250, format 100, write 50).
     Presets: `tune-format` (format ×10 → `pfBefore` 1,000, `pfAfter` 910,
     `pfSpeedup` 100/91 ≈ 1.10, `pfSaved` 9/100 = 9%), `tune-parse` (parse ×2
     → 700, 10/7 ≈ 1.43, 30%), `tune-the-small-ones` (format and write ×1,000
     → 17003/20 = 850.15, 20000/17003 ≈ 1.18, 2997/20000 ≈ 15.0%). Pins
     `pfAfter`, `pfSpeedup`.
   - **Misconception:** "A tenfold speedup of a routine makes the program
     much faster." `tune-format` makes a routine ten times faster and the
     program 9% faster; `tune-parse` makes the hot routine twice as fast and
     saves 30%.
   - **Worked:** 1,000 − 100 + 100/10 = 910 ms; 1,000/910 ≈ 1.10.
   - **Exercise:** a program spending 95% of its time in one routine and 5%
     elsewhere: making the 5% a thousand times faster saves 999/20000 ≈ 5.0%;
     halving the 95% saves 19/40 = 47.5%.
   - **Sources:** McConnell §§25.1–25.6; Knuth 1971; Boehm 1987 *(verify,
     §S.2 F22)*.

8. **code-tuning-techniques** — Code-Tuning Techniques — *Chapter 26 · Code-Tuning Techniques* — 15 min
   - **Read:** §26.1, logic (stop testing when you know the answer, order
     tests by frequency, tables, lazy evaluation); §26.2, loops (unswitching,
     jamming, unrolling, minimising the work inside, sentinel values, the
     busiest loop inside, strength reduction); §26.3, data
     transformations; §26.4, expressions; §26.5, routines; §26.6, recoding
     in a lower-level language; §26.7, the more things change. The book's
     measured timings per language *(verify, §S.2 F23)*.
   - **Do:** count the loop iterations of a nest in two orders and compute
     the share saved by putting the busiest loop inside.
   - **Standard:** for a nest with given iteration counts, compute body
     executions, total iterations in each order, and the share saved.
   - **Lab:** `run/nested`, family 2, input `sizes` outer to inner. Presets:
     `busiest-outside` (`100 5` → `lpBody` 500, `lpIterations` 600, `lpBest`
     505, `lpSaved` 19/120 ≈ 15.8%), `busiest-inside` (`5 100` → 500, 505,
     505, 0), `three-levels` (`50 10 2` → 1,000, 1,550, 1,022, 264/775 ≈
     34.1%). Pins `lpIterations`, `lpBest`, `lpSaved`.
   - **Misconception:** "A technique that saves 16% of iterations saves 16% of
     time." The lab counts loop iterations, not time; the chapter's own
     timings vary by language and compiler, and the book's lesson is to
     measure each change.
   - **Worked:** 100 + 100·5 = 600 against 5 + 5·100 = 505.
   - **Exercise:** `1000 3` → 4,000 iterations; `3 1000` → 3,003; the body
     still runs 3,000 times in both.
   - **Sources:** McConnell §§26.1–26.7 *(verify, §S.2 F23)*.

### Course 6 — System Considerations (`code-complete-system-considerations`, 4)

Part VI, Chapters 27–30. Program size, managing construction, integration and
tools. Its `how_to` says the course is for anyone who works on a team, and that
its figures are the book's quotations of industry averages.

1. **how-program-size-affects-construction** — How Program Size Affects Construction — *Chapter 27 · Program Size* — 15 min
   - **Read:** §27.1, communication and size (the paths among n people);
     §27.2, the range of project sizes; §27.3, the effect of size on errors
     (the book's table of defect density by size); §27.4, on productivity
     (the table of lines per staff-year by size); §27.5, on development
     activities, and the shift away from construction as projects grow.
   - **Do:** compute a team's communication paths, and the ranges of
     defects and staff-years the book's tables give for a size.
   - **Standard:** for a team size and a size in thousands of lines, compute
     the paths, the defect range and the staff-year range from the stated
     table rows.
   - **Lab:** `project/scale`, family 3, inputs `people`, `kloc`, `densityLow`,
     `densityHigh` (defects per thousand lines), `prodLow`, `prodHigh` (lines
     per staff-year), the last four from the book's rows *(verify, §S.2 F24,
     F25)*. Presets: `small-team` (3; 10; 0–40; 2,000–25,000 → `pjPaths` 3,
     `pjDefects` 0–400, `pjStaffYears` 2/5 = 0.4 to 5), `medium` (10; 100;
     2–70; 1,000–20,000 → 45, 200–7,000, 5–100), `large-team` (50; 1,000;
     4–100; 700–10,000 → 1,225, 4,000–100,000, 100 to 10000/7 ≈ 1,428.57).
     Pins `pjPaths`, `pjDefects`, `pjStaffYears`.
   - **Misconception:** "A ten-times-larger program is ten times the work of
     a small one." The tables' ranges grow faster than the size, and the
     paths grow with the square of the team.
   - **Worked:** 50·49/2 = 1,225 paths; 1,000 × 4 to 1,000 × 100 defects.
   - **Exercise:** a team growing from 6 to 12 people: 15 paths to 66.
   - **Sources:** McConnell §§27.1–27.5; Brooks 1975; Jones 1998 *(verify,
     §S.2 F24, F25)*.

2. **managing-construction** — Managing Construction — *Chapter 28 · Managing Construction* — 15 min
   - **Read:** §28.1, encouraging good coding; §28.2, configuration
     management; §28.3, estimating a construction schedule (approaches,
     influences on schedule, the book's table of factors *(verify, §S.2
     F26)*, estimation against control, what to do if you are behind —
     Brooks's law); §28.4, measurement; §28.5, treating programmers as
     people; §28.6, managing your manager.
   - **Do:** adjust a nominal effort estimate by a set of multipliers and
     state the range the factors span.
   - **Standard:** given a nominal estimate and three multipliers, compute
     their product and the adjusted effort.
   - **Lab:** `project/effort`, family 3, records `factor, multiplier`
     (COCOMO II values as the lesson gives them *(verify, F26)*). Presets
     (nominal 100 staff-months): `strong-team` (programmer capability 0.76,
     analyst capability 0.71 → `pjProduct` 1349/2500 = 0.5396, `pjEffort`
     1349/25 = 53.96), `weak-team` (1.34, 1.42 → 1.9028, 190.28),
     `hard-product` (product complexity 1.74, time constraint 1.63, storage
     constraint 1.46 → 1035213/250000 = 4.140852, ≈ 414.09). Pins
     `pjProduct`, `pjEffort`.
   - **Misconception:** "Adding people to a late project brings it in
     earlier." The chapter quotes Brooks and qualifies him; the effort
     factors show that who is on the team moves the estimate by more than
     how many.
   - **Worked:** 0.76 × 0.71 = 0.5396; 100 × 0.5396 = 53.96 staff-months.
   - **Exercise:** nominal 50 staff-months, weak programmers (1.34) with good
     tools (0.78) → 1.0452, 52.26 staff-months.
   - **Sources:** McConnell §§28.1–28.6; Boehm et al. 2000; Brooks 1975.

3. **integration-order** — Integration Order — *Chapter 29 · Integration* — 15 min
   - **Read:** §29.1, the importance of the integration approach; §29.2,
     phased against incremental integration; §29.3, incremental strategies:
     top-down (stubs), bottom-up (drivers), sandwich, risk-oriented,
     feature-oriented, T-shaped; §29.4, the daily build and smoke test.
   - **Do:** count the stubs and drivers an integration order requires from a
     call graph.
   - **Standard:** for six components, their calls and an order, list the
     stubs (called before integrated) and the drivers (integrated before any
     caller).
   - **Lab:** `deps/integrate`, family 2, edges `caller, callee` and an
     `order`. Instance: `main, ui; main, orders; ui, widgets; orders,
     pricing; orders, db; pricing, db`. Presets: `top-down` (`main ui orders
     widgets pricing db` → `dgStubs` "5: db, orders, pricing, ui, widgets",
     `dgDrivers` "0: none"), `bottom-up` (`db widgets pricing orders ui main`
     → 0, "5: db, orders, pricing, ui, widgets"), `risk-first` (`pricing db
     orders main ui widgets` → "3: db, ui, widgets", "2: orders, pricing").
     Pins `dgStubs`, `dgDrivers`.
   - **Misconception:** "Top-down and bottom-up are the only orders." The
     chapter's risk-oriented integration takes the hardest part first and
     pays in both stubs and drivers, which the third preset counts.
   - **Worked:** top-down integrates `main` first, so `ui` and `orders` are
     stubs until they arrive; five stubs, no drivers.
   - **Exercise:** `app, ui; app, core; core, store; ui, core` integrated
     `app ui core store` → stubs `core`, `store`, `ui` (3), no drivers.
   - **Sources:** McConnell §§29.1–29.4.

4. **programming-tools** — Programming Tools — *Chapter 30 · Programming Tools* — 12 min
   - **Read:** §30.1, design tools; §30.2, source-code tools (editing,
     analysing quality, refactoring, version control, data dictionaries);
     §30.3, executable-code tools (compilers, linkers, build tools such as
     make, libraries, code generation, preprocessors, debuggers, testing
     tools, tuning tools); §30.4, tool-oriented environments; §30.5, building
     your own tools; §30.6, tool fantasyland.
   - **Do:** compute which build targets a change to one file makes stale,
     as a build tool does.
   - **Standard:** for a make-style dependency list and a changed file, list
     the targets rebuilt.
   - **Lab:** `deps/ripple`, family 2, edges `target, prerequisite`.
     Instance: `app, main.o; app, util.o; main.o, main.c; main.o, util.h;
     util.o, util.c; util.o, util.h`. Presets: `header` (`util.h` →
     `dgDirect` "2: main.o, util.o", `dgAffected` "3: app, main.o,
     util.o"), `source` (`main.c` → "1: main.o", "2: app, main.o"). Pins
     `dgAffected`. The modern aside of this course lives here (continuous
     integration and today's build systems doing the same computation,
     §F.1).
   - **Misconception:** "A build tool rebuilds what you edited." It rebuilds
     what depends on it, transitively; a header reaches every object that
     includes it.
   - **Worked:** `util.h` → `main.o`, `util.o` → `app`: three targets.
   - **Exercise:** `util.c` changes → `util.o` and `app`.
   - **Sources:** McConnell §§30.1–30.6; Feldman 1979 for make *(check that
     the book cites it)*.

### Course 7 — Software Craftsmanship (`code-complete-software-craftsmanship`, 4)

Part VII, Chapters 31–35. Layout, self-documenting code, character, and the
book's themes. Its `how_to` says the course can be read alone.

1. **layout-and-style** — Layout and Style — *Chapter 31 · Layout and Style* — 15 min
   - **Read:** §31.1, layout fundamentals (the fundamental theorem of
     formatting: good visual layout shows the logical structure; the
     objectives of good layout); §31.2, techniques (white space,
     parentheses); §31.3, layout styles (pure blocks, emulating pure blocks,
     begin-end pairs, endline layout); §31.4–31.8, control structures,
     individual statements, comments, routines, classes; the study of
     indentation *(verify, §S.2 F27)*.
   - **Do:** find each line whose indentation disagrees with the structure the
     compiler reads.
   - **Standard:** for a listing with unbraced `if`s, mark every line whose
     indentation misstates its structure and say what the compiler does.
   - **Lab:** `code/layout`, family 1, `cfg["indent"] = 4`. Presets:
     `dangling-else` (an `else` indented under the outer `if` that Java binds
     to the inner → `coMisIndented` 2, `coLines` "5, 6"), `two-statements`
     (an unbraced `if` followed by two indented statements → 1, "4"), `braced`
     (the first preset with braces → 0, none). Pins `coMisIndented`,
     `coLines`.
   - **Misconception:** "Layout is a matter of taste." The fundamental
     theorem is the chapter's test, and `dangling-else` shows a layout that
     tells the reader the opposite of what the code does.
   - **Worked:** the `else` on line 5 belongs to the `if` on line 3, so it
     should sit at its depth (8 spaces); `sendLetter` at 12.
   - **Exercise:** the `clamp` routine in §D.4: `log("clamped");` and
     `return high;` both indented under an unbraced `if` → the lab flags
     line 6 (`coMisIndented` 1, `coLines` "6"). The reader explains that
     `return high;` is unconditional, so every value not below `low` returns
     `high`, and that `javac` rejects line 7 as unreachable: here the
     compiler catches what the layout hid, and with any statement other
     than a `return` on line 6 nothing would.
   - **Sources:** McConnell §§31.1–31.8 *(verify, §S.2 F27)*.

2. **self-documenting-code** — Self-Documenting Code — *Chapter 32 · Self-Documenting Code* — 15 min
   - **Read:** §32.1, external documentation; §32.2, programming style as
     documentation; §32.3, to comment or not to comment (the book's
     dialogue); §32.4, keys to effective comments (kinds of comments; the
     density figure *(verify, §S.2 F28)*); §32.5, commenting techniques;
     §32.6, IEEE standards.
   - **Do:** compute a routine's comment density and classify each comment
     as repeating the code, explaining it, or stating intent.
   - **Standard:** for a routine, count code and comment lines, compute the
     density, and mark each comment by kind.
   - **Lab:** `code/size`, family 1 (`coDensity`). Presets: `comments-repeat`
     (an average routine with a comment over every line → `coCode` 7,
     `coComment` 5, `coDensity` 5/7 ≈ 71.4%), `comments-intent` (`mean`
     with one header comment stating its precondition → 7, 1, 1/7 ≈ 14.3%).
     Pins `coComment`, `coDensity`.
   - **Misconception:** "More comments make code better documented." The
     density on `comments-repeat` is five times the other's and every one of
     its comments repeats the code; the chapter's kinds are the test, not the
     count. The modern aside of this course lives here (§F.1).
   - **Worked:** 5 comment lines over 7 code lines: 5/7 ≈ 71.4%.
   - **Exercise:** `isLeapYear` with a header comment and one comment stating
     the rule → 2 comment lines, 3 code lines, 2/3; both comments state
     intent, neither repeats the code.
   - **Sources:** McConnell §§32.1–32.6 *(verify, §S.2 F28)*.

3. **personal-character** — Personal Character — *Chapter 33 · Personal Character* — 12 min
   - **Read:** §33.1, is personal character off-topic?; §33.2, intelligence
     and humility; §33.3, curiosity; §33.4, intellectual honesty; §33.5,
     communication and cooperation; §33.6, creativity and discipline;
     §33.7, laziness (the enlightened kind: writing a tool to do an
     unpleasant job); §33.8, characteristics that matter less than you
     think; §33.9, habits. The differences among programmers *(verify, §S.2
     F29)*.
   - **Do:** compute when a tool that automates a repeated task pays for
     itself, and what it saves in a year.
   - **Standard:** given the hours to build a tool, the minutes a task takes
     by hand and with the tool, and how often it runs, compute the break-even
     runs and weeks.
   - **Lab:** `project/breakeven`, family 3 (the lesson's model; the chapter
     gives no formula). Inputs `build` (hours), `manual`, `auto` (minutes per
     run), `perWeek`. Presets: `weekly-report` (8; 15; 1; 10 →
     `pjRuns` 35, `pjWeeks` 7/2 = 3.5, `pjYear` 340/3 ≈ 113.33 hours saved
     in the first year), `rare-task` (8; 30; 2; 1/4 → 18, 72, −29/15 ≈
     −1.93), `big-tool` (40; 10; 1; 5 → 267, 267/5 = 53.4, −1). Pins
     `pjRuns`, `pjWeeks`, `pjYear`.
   - **Misconception:** "Automating a task always saves time." `rare-task`
     takes 72 weeks to pay back; the chapter's virtue is laziness with
     judgement.
   - **Worked:** 8 h = 480 min; 480/14 ≈ 34.3, so 35 runs; at 10 a week, 3.5
     weeks.
   - **Exercise:** a 2-hour script that saves 5 minutes a working day (5 runs
     a week) → 24 runs, 24/5 = 4.8 weeks, 59/3 ≈ 19.67 hours saved in the
     first year.
   - **Sources:** McConnell §§33.1–33.9 *(verify, §S.2 F29)*.

4. **themes-of-craftsmanship** — Themes of Craftsmanship — *Chapters 34–35 · Themes and Further Reading* — 15 min
   - **Read:** Chapter 34, the book's themes: conquer complexity; pick your
     process; write programs for people first, computers second; program
     into your language, not in it; focus your attention with conventions;
     program in terms of the problem domain; watch for falling rocks;
     iterate, repeatedly, again and again; separate software and religion.
     Chapter 35, where to find more: the reading plan, named and pointed
     to, not reproduced (§G).
   - **Do:** apply the course's counts to one routine and say which themes
     each count serves.
   - **Standard:** for a 16-line routine, state its decision points and
     depth, name two improvements and the theme each serves.
   - **Lab:** `code/complexity`, family 1. Presets: `retry-delay` (a
     retry-backoff routine → `coDecisions` 7, `coBreakdown` "1 + if 3 + for
     1 + && 1 + || 1", `coBand` "6–10", `coDepth` 2), `nested-shipping` (from
     Nesting and Complexity → 9, depth 5). Pins `coDecisions`, `coDepth`.
   - **Misconception:** "Craftsmanship is a set of rules to follow."
     Chapter 34's last theme argues against treating any method as a
     religion; the counts are tools for judgement, which is the material
     clause.
   - **Worked:** 1 + `if` ×3 + `for` + `&&` + `||` = 7.
   - **Exercise:** the reader's own routine, pasted in: the decision points,
     the depth, and one sentence per theme it touches. (The `standard`
     uses `retry-delay` so that it has an answer.)
   - **Sources:** McConnell Chapters 34–35.

---

## §D The lab kit: `cckit`

### D.0 Conventions

Everything in `docs/philosophy/PLAN.md` §D.0 and the phenkit conventions as
implemented (`docs/phenomenology/kit-report.md`, `phenkit_core.py`) holds unless
this section says otherwise: one function `cckit_lab(cfg)` registered under the
key `"cckit"` in `scripts/mathpath/labs/__init__.py`; cfg keys `mode`, `view`,
`presets`, `preset`, `title`, `panel_title`, `panel_intro`; text inputs with id
`<prefix>In<Field>`; records `a, 1, 2; b, 3, 4`; a preset menu
`<prefix>Preset`, a banner `<prefix>Status`, a table `<prefix>Table`; every
text input survives `''`, `banana`, `0`, `-1`, `1/0`, `A>B` with a red banner
and tiles blanked to `—`; build-time refusals for a preset key that is not an
input of its view, a size limit exceeded, an unknown view. Each mode has one
pure `<xx>Compute(view, inst, opts)` that `scripts/mathcheck.js` calls in its
own block, each case seen to fail when its line is broken on purpose. `cckit`
joins `KITS_WITH_EXPECTATIONS` at wiring, last.

**Files.** `scripts/mathpath/labs/cckit_core.py` (shared JS: printing,
parsing, the preset menu, the code tokenizer and statement reader),
`cckit.py` (the `code` mode), `cckit_b.py` (the other seven modes). Like
`phenkit`, the entry point dispatches on `cfg["mode"]` and raises on an
unknown mode or view.

**Page weight.** A page ships `RATIONAL_JS`, `CC_CORE_JS`, the tokenizer only
when the mode is `code`, and the active view's block only. Budget: ≤ 40 KB
gzipped per lesson, measured with the snippet in `AGENTS.md` before the kit is
called done. Eight modes and 35 views would not fit if every page shipped
every view; emitting only the active view is a requirement, not an
optimisation.

**Prefixes.** `co` code, `dg` deps, `cd` cond, `se` search, `lp` run, `nu`
(the `run/arith` view's tiles), `df` defects, `pf` profile, `pj` project.
Before the kit is called done, grep `scripts/mathpath/labs/*.py` for every JS
function name and element id it defines, as phenkit's docstring records.

**Why Java.** The book's examples are in C++, Java and Visual Basic. Java is
one of its two main languages, so the book's own discussion carries over
without translation; it has the C-family syntax the book's layout, `case`
and decision-point chapters are written about (braces, `switch` with
fall-through, `&&` and `||`, `++`); its integers are fixed-width and
overflow, which Chapter 12 needs and Python hides; and the decision-point rule
maps onto its keywords one for one. Python would read more easily, and the
prerequisites say a Python reader can follow, but the kit's counts would have
to be redefined for indentation-delimited blocks, `elif`, and arbitrary-
precision integers, and the layout chapter's subject would disappear.
Snippets use plain Java 8 or later: no records, no `var`, no lambdas, no
streams, no annotations.

**Code inputs are `<textarea>`s, filled by script.** A view that takes code
or a condition (`code/*`, `cond/*`) has a `<textarea id="<prefix>InCode">` (and
`cdInA`, `cdInB`, `cdInCond`), monospace, at least 12 rows for code, filled
from the preset table at load and on a preset change, never from markup: no
`value=` attribute or text content carries code, so no shipped attribute holds
`>` or `&`. `labcheck.js` must learn to sweep `<textarea>`s and to count them
when deciding what a preset menu rewrites (§H.2); until it does, their hostile
inputs are untested, and the kit is not called done.

**The listing.** Beside every code input the view draws the code as a
numbered listing (`<pre>` with a line-number gutter generated by script,
non-selectable), and every tile and banner that names a line uses those
numbers. Line numbers count every line from 1, blank and comment lines
included, because the book's own live-time examples number the lines of the
listing that way *(verify, §S.2 F10)*.

**Number format.** Whole numbers group thousands with a comma (`2,692,537`)
and print a negative with U+2212 (`−1`). A non-whole figure prints its
reduced fraction and its decimal: `11/4 = 2.75`, `28/3 ≈ 9.33` (two places,
rounded half away from zero from the exact value; `=` when the decimal is
exact). A share prints the fraction and a percentage with one decimal where it
is not whole: `33/50 = 66%`, `31/60 ≈ 51.7%`. A range prints `low–high` with an
en dash (`425–800`), collapsing to one figure when equal. A list is
comma-separated in the order stated per tile, or `none`; a count with a list
prints `5: audit, backup, export, invoice, report`. The one exception is
`nuJava`, which prints exactly what Java's `System.out.println` prints for the
value: ASCII `-`, no grouping, and for a `double` the shortest decimal that
reads back to the same double (§D.1, `run/arith`).

**Exact.** Every tile is a rational over BigInt, or a count, or a list.
`run/arith` simulates `int` and `long` with BigInt and wraps them explicitly,
and simulates `double` by rounding each exact rational result to the nearest
binary64 (ties to even) with BigInt; no tile is computed in JavaScript
floating point.

**The figures are the lesson's.** No figure from the book is a constant of
the kit. Cost tables, removal rates, ratios, densities, productivities and
multipliers arrive in the cfg or the preset, so that the accuracy review and
the book correct them in `content/` without touching the kit, and so that the
kit never states something only the book can vouch for.

**Families.** Every view's `panel_intro` names its family (§0): "A count over
code, by the rules stated below the listing", "A count over the structure the
lesson states", or "The arithmetic of figures the lesson quotes (marked with
their source)".

### D.1 Modes (prefix, views, inputs, tiles)

#### code (`co`) — family 1

**The subset the kit reads** (stated in a `details` block under every code
listing, in these words or near them):

- Comments `//` to the end of the line and `/* … */` (which may span lines);
  string and character literals (`"…"` with `\"` escapes, `'x'`) are opaque.
- A line is **blank** (whitespace only), a **comment line** (it carries a
  comment, alone or after code), and/or a **code line** (it has code outside
  comments). A **statement line** is a code line that is not only braces and
  semicolons.
- The **routine** is the first statement at brace depth 0 that ends in `{`
  and has the shape *type name(parameters)* — joined across lines up to its
  `{`, and not beginning with a control keyword. Without one, the listing is
  a **fragment** and routine-level tiles say so. Its **parameters** are the
  comma-separated items between its parentheses.
- A **variable** is an identifier that begins with a lower-case letter or
  `_`, is not a Java keyword, is not followed by `(` (a call) and is not
  preceded by `.` (a member). Names that begin with a capital are types or
  constants.
- A **declaration** is a statement (after any of `public private protected
  static final abstract`) that begins with a type — a primitive, or a
  capitalised name, with optional `<…>` and `[]` — followed by a name and then
  `=`, `;`, `,` or `:` (the enhanced `for`). With `=` (or `:`) it **sets** the
  name; without, it only declares it. Parameters are set at the header line.
- A statement `name op expr` with `op` one of `= += -= *= /= %=` **reads**
  the variables in `expr` (and `name` too unless `op` is `=`) and then
  **sets** `name`. `x++`, `x--`, `++x`, `--x` read and then set `x`.
  Assigning to an element or a field (`a[i] = v`, `p.x = v`) only reads the
  variables in it: the kit does not track the contents of arrays or objects.
  Every other statement reads every variable in it. A `for` header is read as
  its three parts in order.
- The kit **reads the lines top to bottom and does not follow branches or
  loops.** It is exact for straight-line code and an approximation
  otherwise, and every view whose tile depends on order says so in its
  banner.
- **Decision points**, the chapter's rule as applied to Java: 1, plus one for
  each `if`, `while`, `for`, `case`, `&&` and `||`. `else`, `default`,
  `do` (its `while` counts), `?:`, `catch` and `try` add nothing; where `?`
  appears, the banner says it was not counted. *(The rule is the book's;
  whether the book counts the conditional operator: verify, §S.2 F14.)*
- **Depth** of a statement line is its brace depth below the routine's own
  braces (a fragment's lines start at 0). Unbraced bodies add nothing to it;
  the `layout` view is where they are checked.

Views (each takes `code`, a textarea, plus what is listed):

- `size`: tiles `coLines`, `coCode` (code lines, braces included),
  `coComment` (comment lines), `coBlank`, `coParams` (a count, or "none (a
  fragment)"), `coDensity` (comment lines / code lines, a share).
- `class`: the listing is one class. A **field** is a statement at depth 1
  ending in `;` whose first `(` (if any) comes after its `=`; a **routine** is
  a line at depth 1 with `(` before any `=` ending in `{` or `;`. Visibility
  is the first of `public private protected`, else package. Tiles `coFields`,
  `coPublicFields` (public and not `final`), `coRoutines`,
  `coPublicRoutines`.
- `dupes`: cfg `min_run` (default 2). Statement lines are compared after
  collapsing white space; a **repeated block** is a run of at least
  `min_run` consecutive statement lines that occurs again, not overlapping,
  maximal (not extendable backwards). Tiles `coDupBlocks` (distinct blocks),
  `coDupLines` (lines in all copies), `coDupWhere` ("lines 3–5 and lines 7–9";
  blocks separated by `; `).
- `extract`: inputs `from`, `to` (line numbers). **In**: variables whose
  first event inside the block is a read and that were set or declared
  before it. **Out**: variables set inside the block and read after it.
  Variables read but declared nowhere in the listing are listed as
  "outside". Tiles `coIn`, `coOut` (each in order of first reference inside
  the block, or `none`), `coParams` (the In count), `coOutside`. When Out has
  more than one name the banner says a Java method returns one value.
- `ppp`: steps are the comment-only lines inside the routine's body. Tiles
  `coSteps`, `coCode` (statement lines in the body), `coEmpty` (steps with no
  statement line before the next step or the body's end: "line 14", or
  `none`), `coMaxUnder` ("3 lines, under line 8"; the first on a tie).
- `dataflow`: for each variable set or declared in the listing (parameters
  included), its events in line order. Anomalies: **used before set** (a
  read with no earlier set — reported once per variable, at its first
  read); **set twice** (a set by `=` followed by another set with no read
  between); **set, never used** (the variable's last event is a set). Tiles
  `coAnomalies` (their total), `coUsedBeforeSet`, `coSetTwice`, `coUnused`
  ("count (line 6)", "total (lines 2, 4)", comma-separated in line order),
  `coDeps` (each pair *i → j*, i < j, such that line j reads a variable whose
  latest earlier set is on line i: "1→2, 2→5", sorted).
- `span`: input `vars` (space-separated names; empty means every variable the
  listing sets or declares). A variable's **references** are the lines on which
  it appears; a **span** is the number of lines strictly between two
  consecutive references; its **live time** is last − first + 1. Tiles
  `coAvgSpan` (all spans of the chosen variables pooled), `coAvgLive` (mean
  over the variables), `coLongest` ("total: 14"), and a table: variable,
  references, spans, live time.
- `names`: cfg `min` (default 8). Declared names (parameters, declarations,
  enhanced-`for` variables) in order of declaration; **loop indexes** (declared
  in a `for` header) are listed but not counted. Tiles `coNames` (all
  declared), `coAvgLen` (mean length of the counted names), `coShort` (counted
  names shorter than `min`, or `none`).
- `literals`: numeric literals in code lines, except those whose value is 0
  or 1 and except on a line containing `final`. Tiles `coMagic` (occurrences),
  `coDistinct`, `coMagicList` ("12 (lines 2, 3)", in order of first
  appearance).
- `complexity`: tiles `coDecisions`, `coBreakdown` ("1 + if 5 + for 1 + && 1 +
  || 1", in the order if, while, for, case, &&, ||, zero terms left out),
  `coBand` (cfg `bands`, default `[5, 10]`: "0–5", "6–10", "above 10" —
  the book's guidance as the lesson states it, verify §S.2 F14), `coDepth`,
  `coDeepest` (the first line at that depth).
- `basis`: tiles `coBasis` (decision points + one for each `switch` with no
  `default`), `coNoDefault`, `coPoints` ("while line 4, && line 4, …", in line
  order).
- `layout`: cfg `indent` (default 4; a tab counts as `indent` spaces). For
  each code line the kit computes the depth the compiler's structure gives it
  — braces, plus one for the single statement after an unbraced `if`,
  `else`, `for` or `while` header; an `else` takes the depth of the `if` it
  binds to (the nearest unmatched one, as Java binds it); a `case`/`default`
  label at the switch's depth and its statements one deeper; a line of only
  `{` after an unbraced header at the header's depth — and compares it with
  the line's leading spaces / `indent`. Comment-only lines are not checked.
  Tiles `coMisIndented`, `coLines` (line numbers, or `none`).

Limits: 200 lines, 120 characters a line; more is refused with a sentence.

#### deps (`dg`) — family 2

Records `a, b` (names: letters, digits, `.`, `_`, `-`). Ties in a "largest"
tile go to the alphabetically first name, and the banner names every tied one.

- `coupling`: *a uses b*. Tiles `dgModules`, `dgEdges` (distinct ordered
  pairs), `dgPairs` (n·(n − 1)/2), `dgConnected` (unordered pairs with an edge
  either way, as a share of `dgPairs`), `dgFanOut`, `dgFanIn` ("db 3").
- `ripple`: input `changed`. *a depends on b*. Tiles `dgDirect` (names with an
  edge to `changed`), `dgAffected` (names that reach it by edges), both
  "count: names" alphabetical.
- `tree`: *child, parent*; a child with two parents or a cycle is refused.
  Depth of a root is 1. Tiles `dgDepth`, `dgDeepest`, `dgClasses`,
  `dgLeaves`.
- `shared`: records `routine, access, global`, access `r`, `w` or `rw`.
  Tiles `dgGlobals`, `dgRoutines`, `dgCoupled` (unordered pairs of distinct
  routines that touch a common global which at least one of them writes;
  the banner gives it out of n·(n − 1)/2), `dgMostShared` ("current, 5
  routines").
- `integrate`: *caller, callee*, and input `order` (space-separated, every
  name once). A **stub** is needed for a component that some integrated
  component calls before it is itself integrated; a **driver** for a
  component that has callers, none of them integrated when it is. Tiles
  `dgStubs`, `dgDrivers` ("count: names").

#### cond (`cd`) — family 2

A condition is Java: identifiers, `true`, `false`, `!`, `&&`, `||`,
parentheses, and (in `range`) the comparisons `< <= > >= == !=` between the
variable and an integer literal. The kit parses it with its own parser; it
never evaluates text as script.

- `truth`: textareas `a`, `b` (boolean variables only). Atoms in order of
  first appearance in `a` then `b`, at most 5; rows T before F, the first atom
  most significant. Tiles `cdAtoms`, `cdRows`, `cdTrueA`, `cdTrueB`,
  `cdEquivalent` ("yes", or "no, on 2 of 4 rows"), `cdFirstDiff` ("done = T,
  error = F", or `none`); a table of all rows.
- `range`: textarea `cond` over one integer variable; inputs `lo`, `hi` (the
  valid range, inclusive) and `means` (`valid` or `invalid`: what a true
  condition says). The domain is Java's `int`. The kit evaluates at every
  literal c ± 1, lo ± 1, hi ± 1, the ends of `int`, and one point inside each
  gap between them, which decides every integer exactly. Tiles `cdDisagree`
  (maximal intervals where the check and the range differ: "0", "1, 12",
  "−1 and below", "121 and above", "5 to 9", or `none`), `cdTests` (lo − 1,
  lo, lo + 1, hi − 1, hi, hi + 1, sorted, distinct), `cdExposed` (those tests
  in `cdDisagree`).

#### search (`se`) — family 2

- `chain`: records `case, frequency` in the chain's order; a last case named
  `else` is the final `else`. Reaching condition i costs i tests; the `else`
  costs as many as there are conditions. Tiles `seExpected`, `seBest` (the
  conditions in descending frequency, ties in the given order, the `else`
  last), `seSaved`. The banner says reordering is valid only if the
  conditions are mutually exclusive.
- `stairs`: records `upper bound, value` strictly ascending; inputs `key`,
  `rule` (`below` | `atmost`). Linear: test steps from the first until one
  passes (`key < bound`, or `≤`), counting tests; none passing is "above the
  table". Binary: `lo = 0, hi = n; while lo < hi: mid = ⌊(lo + hi)/2⌋; one
  test; pass → hi = mid, else lo = mid + 1`. Tiles `seValue`, `seLinear`,
  `seBinary`.
- `bisect`: inputs `n`, `k`. `lo = 1, hi = n; while lo < hi: mid =
  ⌊(lo + hi)/2⌋; one test "is it in lo..mid?"`. Tiles `seSteps`, `seWorst`
  (⌈log₂ n⌉, computed as the bit length of n − 1), and the table of
  intervals.

#### run (`lp`, and `nu` for `arith`) — family 2

- `loop`: inputs `start`, `cmp` (`lt le ne gt ge`), `bound`, `step` (non-zero
  integers); the loop `for (i = start; i cmp bound; i += step)`. Computed in
  closed form, never by running it: `lt` with start < bound runs ⌈(bound −
  start)/step⌉ times when step > 0 and never ends when step ≤ 0; `le` is `lt`
  with bound + 1; `gt`, `ge` mirror; `ne` ends only when (bound − start) is a
  positive multiple of step. Overflow of `int` is not modelled, and the
  banner says so. Tiles `lpIterations` (a count or "never ends"), `lpLast`
  (`—` when it never runs), `lpAfter`.
- `nested`: input `sizes` (outer to inner, 1 to 5 positive whole numbers).
  Tiles `lpBody` (the product), `lpIterations` (Σ over levels of the product
  of the sizes down to that level), `lpBest` (the same with the sizes
  ascending), `lpSaved` ((iterations − best)/iterations).
- `recursion`: inputs `fn` (`factorial` | `fibonacci`), `n` (0 to 90).
  `factorial(n) = n ≤ 1 ? 1 : n·factorial(n − 1)`; `fibonacci(n) = n < 2 ? n :
  fibonacci(n − 1) + fibonacci(n − 2)`. Tiles `lpCalls` (max(n, 1);
  2·F(n + 1) − 1), `lpDepth` (max(n, 1)), `lpValue`, `lpLoop` (max(n − 1, 0),
  the iterations of the loop version).
- `arith`: inputs `type` (`int` | `long` | `double`), `start`, `op` (`+ - * /
  %`), `operand`, `times` (1 to 1,000): `acc = start; repeat times: acc = acc
  op operand`, each step in the type's arithmetic — `int`/`long` wrap at 32/64
  bits, `/` truncates toward zero, `%` takes the dividend's sign, division by
  zero prints "ArithmeticException"; `double` rounds every literal and every
  result to the nearest binary64, ties to even, and refuses division by zero
  and results outside the normal range with a sentence. Tiles `nuJava`
  (Java's printed value; for `double`, the shortest decimal of 1 to 17
  significant digits that rounds back to the same binary64, in Java's form),
  `nuExact` (the same operations on exact rationals), `nuEqual` (yes/no), and
  for `double` `nuStored` (the binary64 result as an exact fraction).

#### defects (`df`) — family 3

- `cost`: cfg `table` (stage pairs → `low–high` multipliers; stages `req arch
  cons test post`); records `introduced, detected, count`. A pair missing
  from the table is refused. Tiles `dfCost` (range), `dfEarly` (each count
  times the cost of finding it in the stage it was introduced), `dfRatio`
  ("85/7 ≈ 12.1× to 160/7 ≈ 22.9×").
- `removal`: input `injected`; records `stage, rate` (a share). Each stage
  finds its rate of what is left. Tiles `dfFound`, `dfRemaining`,
  `dfCombined`; table per stage.
- `pipeline`: as `removal` with a third part, hours per defect found. Tiles
  as `removal` plus `dfHours`, `dfPerDefect`.

#### profile (`pf`) — family 3

- `shares`: records `name, amount` with an optional third part `c` marking
  the entries `cfg["tag_label"]` names; cfg `target` (default 4/5). Tiles
  `pfTotal`, `pfTagged`, `pfTop` ("coding and debugging, 8/25 = 32%"),
  `pfPareto` ("6 of 8 entries reach 4/5 of the total").
- `speedup`: records `name, time, factor` (factor ≥ 1/1000, 1 = unchanged).
  Tiles `pfBefore`, `pfAfter` (Σ time/factor), `pfSpeedup`
  (before/after), `pfSaved` ((before − after)/before).

#### project (`pj`) — family 3

- `language`: inputs `size`, `ratio`, `rate`. Tiles `pjEquivalent`
  (size/ratio), `pjDays` (equivalent/rate), `pjDaysC` (size/rate).
- `scale`: inputs `people`, `kloc`, `densityLow`, `densityHigh`, `prodLow`,
  `prodHigh`. Tiles `pjPaths` (people·(people − 1)/2), `pjDefects`
  (kloc × density range), `pjStaffYears` (1,000·kloc / prodHigh to
  1,000·kloc / prodLow).
- `effort`: input `nominal`; records `factor, multiplier`. Tiles
  `pjProduct`, `pjEffort`.
- `breakeven`: inputs `build` (hours), `manual`, `auto` (minutes; manual >
  auto), `perWeek` (> 0, a fraction allowed). Tiles `pjRuns`
  (⌈60·build/(manual − auto)⌉), `pjWeeks` (runs/perWeek), `pjYear`
  ((manual − auto)·perWeek·52/60 − build, hours, signed).

### D.2 What the kit must never do

- **Run the reader's code**, or evaluate any text as script (`eval`,
  `Function`, `setTimeout` with a string). The kit tokenises and counts; the
  conditions have their own parser. The site's CSP forbids it anyway, and a
  kit that relied on it would fail in production and pass locally.
- **Print a verdict on code.** No tile or banner says "good", "bad", "too
  complex" or "fails"; `coBand` prints the band's figures and the banner
  says whose guidance it is.
- **Carry a figure from the book as a constant.** Every rate, ratio, cost and
  multiplier is lesson data (§D.0).
- **Send or store the reader's code.** Nothing leaves the page; nothing is
  written to storage.
- **Claim more than its reading.** Every order-dependent view says it reads
  top to bottom and does not follow branches; `dupes` says it matches text;
  `extract` says it does not track objects.
- **Derive a tile from a float**, or from a drawing.
- Show a tile, or offer a control, whose meaning depends on comparing
  presets.

### D.3 Build-time checks

The kit tokenises every preset's code at build time with a Python mirror of
the tokenizer (as `phenkit_core.parse` mirrors `phRead`) and raises, naming
the preset, on a listing it cannot read, a header it cannot find where the
view needs a routine, a line range outside the listing, or a condition with
more than one variable in `range`. `scripts/mathcheck.js` gets one block per
mode, with at least one case per view and the reference values of §C as its
cases.

### D.4 The reference model, and the snippets

The figures in §C were computed by a Python reference model of every view
(`/tmp/claude-0/-home-claude/3b1d3502-1b81-5554-ace3-d7f9f019031f/scratchpad/ccref.py`
and `presets.py`, not committed; the orchestrator copies them to the kit
engineer). The model is not the kit: the kit is JavaScript, and its figures
are read from the page by `labcheck.js --observe`. Where the two disagree, the
kit engineer finds out which is wrong and records it in the kit report.

The snippets below are the lessons' instances, verbatim; an author may
improve wording but recomputes and records any change. Snippets used only as
exercises are given here too.

`free-slot` (The Pseudocode Programming Process):

```java
// Returns the index of the first free slot, or -1 if the table is full.
int findFreeSlot(Slot[] table) {
    // start at the slot after the one used last
    int start = (lastUsed + 1) % table.length;
    // look at each slot once, wrapping around the end
    for (int step = 0; step < table.length; step++) {
        int i = (start + step) % table.length;
        // if the slot is free, remember it and return it
        if (table[i].isFree()) {
            lastUsed = i;
            return i;
        }
    }
    // if no slot is free, log the overflow
    // return -1
    return -1;
}
```

`count-unset` (Declaring and Initializing Variables; `initialized` moves
`int count = 0;` to line 3 after `double total = 0.0;`):

```java
double averagePrice(double[] prices) {
    int count;
    double total = 0.0;
    for (int i = 0; i < prices.length; i++) {
        total = total + prices[i];
        count = count + 1;
    }
    return total / count;
}
```

`set-twice`:

```java
double averagePrice(double[] prices) {
    double total = 0.0;
    int count = 0;
    total = prices[0];
    count = prices.length;
    double average = total / count;
    return total / count;
}
```

`declared-at-top` (Scope, Span and Live Time; `declared-near-use` declares
`index` just before the first `while` and `total`, `done` just before the
second, after `printRule();`):

```java
void summarize(Record[] records) {
    // initialize all variables
    int index = 0;
    double total = 0.0;
    boolean done = false;
    printHeader();
    printColumns();
    while (index < records.length) {
        records[index].check();
        index = index + 1;
    }
    printRule();
    while (!done) {
        total = total + nextAmount();
        done = total > 1000;
    }
    printTotal(total);
}
```

`nested-shipping` (Nesting and Complexity; Themes of Craftsmanship):

```java
double shippingCost(Order order) {
    double cost = 0.0;
    if (order != null) {
        if (order.weight() > 0) {
            if (order.isDomestic()) {
                if (order.weight() < 2 && !order.isExpress()) {
                    cost = 5.0;
                } else {
                    cost = 9.0 + order.weight();
                }
            } else {
                for (Item item : order.items()) {
                    if (item.isRestricted() || item.weight() > 30) {
                        return -1.0;
                    }
                }
                cost = 25.0 + 2 * order.weight();
            }
        }
    }
    return cost;
}
```

(22 lines: the one snippet allowed past 20, because the nesting is the
lesson.) `guard-clauses`:

```java
double shippingCost(Order order) {
    if (order == null || order.weight() <= 0) {
        return 0.0;
    }
    if (!order.isDomestic()) {
        return internationalCost(order);
    }
    if (order.weight() < 2 && !order.isExpress()) {
        return 5.0;
    }
    return 9.0 + order.weight();
}
```

`overtime` (Structured Basis Testing):

```java
double overtimePay(Employee[] staff, int count) {
    double pay = 0.0;
    int i = 0;
    while (i < count && staff[i] != null) {
        Employee e = staff[i];
        if (e.isExempt()) {
            pay = pay + 0.0;
        } else if (e.hours() > 40) {
            pay = pay + (e.hours() - 40) * e.rate() * 1.5;
        }
        i = i + 1;
    }
    return pay;
}
```

`printStatement` (Refactoring Safely):

```java
void printStatement(Account account) {
    double balance = account.openingBalance();
    double fees = 0.0;
    for (Transaction t : account.transactions()) {
        balance = balance + t.amount();
        if (t.amount() < 0 && balance < 0) {
            fees = fees + 25.0;
        }
    }
    balance = balance - fees;
    System.out.println("Fees: " + fees);
    System.out.println("Closing balance: " + balance);
}
```

`dangling-else` (Layout and Style; `braced` is the same logic with braces
and the `else` on the inner `if`):

```java
void notify(User user) {
    if (user.isActive())
        if (user.wantsEmail())
            sendEmail(user);
    else
        sendLetter(user);
    log(user);
}
```

`two-statements`:

```java
void close(Account account) {
    if (account.balance() == 0)
        account.markClosed();
        archive(account);
    log(account);
}
```

Exercise snippets. `discountPercent` (Nesting and Complexity: 7 decision
points, depth 2; basis count 7):

```java
int discountPercent(Customer c, Order o) {
    int pct = 0;
    if (c.isMember()) {
        pct = 5;
    }
    if (o.total() > 100 || c.years() > 3) {
        pct = pct + 5;
    }
    for (Coupon k : o.coupons()) {
        if (k.isValid() && !k.isUsed()) {
            pct = pct + k.percent();
        }
    }
    return pct;
}
```

`archiveOld` (Structured Basis Testing: 4):

```java
void archiveOld(Message[] inbox, int days) {
    for (int i = 0; i < inbox.length; i++) {
        if (inbox[i].ageInDays() > days || inbox[i].isSpam()) {
            inbox[i].archive();
        }
    }
}
```

`expireSessions` (The Pseudocode Programming Process: 4 steps, line 10
empty):

```java
// Moves every expired session to the archive.
void expireSessions(List<Session> sessions, Clock clock) {
    // read the current time once
    long now = clock.millis();
    // for each session older than the limit
    for (Session s : sessions) {
        if (now - s.lastSeen() > LIMIT) {
            // move it to the archive
            archive.add(s);
            // remove it from the live list
        }
    }
}
```

`printInvoice` (Refactoring Safely: 2–5 → in `inv`, out `subtotal`; 7–9 → in
`subtotal, tax`, out none):

```java
void printInvoice(Invoice inv) {
    double subtotal = 0.0;
    for (Line line : inv.lines()) {
        subtotal = subtotal + line.amount();
    }
    double tax = subtotal * inv.taxRate();
    System.out.println("Subtotal: " + subtotal);
    System.out.println("Tax: " + tax);
    System.out.println("Total: " + (subtotal + tax));
}
```

`clamp` (Layout and Style: line 6 mis-indented):

```java
int clamp(int value, int low, int high) {
    if (value < low)
        return low;
    if (value > high)
        log("clamped");
        return high;
    return value;
}
```

The remaining presets' snippets (`public-fields`, `private-fields`,
`kitchen-sink`, the label printers, `nine-parameters`, `parameter-objects`,
`short-names`, `problem-names`, `magic`, `named`, `total-first`, `in-order`,
`hidden`, `switch-without-default`, `comments-repeat`, `comments-intent`,
`retry-delay`, and the exercises of Course 3) are in `presets.py` with the
figures above; the author copies them from there into the lesson and the
cfg.

---

## §E Package layout, the source text, quoting, and the author's checklist

### E.1 Layout

```
content/code_complete/
  __init__.py                       PATH, COURSES (filter COURSE = None), numbering loop
  c1_foundation/__init__.py         COURSE; lessons = part_a.LESSONS
  c1_foundation/part_a.py
  c2_high_quality_code/             part_a.py (Chapters 5–6), part_b.py (7–9)
  c3_variables/
  c4_statements/                    part_a.py (14–17), part_b.py (18–19)
  c5_code_improvements/             part_a.py (20–22), part_b.py (23–26)
  c6_system_considerations/
  c7_craftsmanship/
content/spoken/code_complete.py     SPOKEN = {}
```

Mirror `content/phenomenology/__init__.py` for the package `__init__` and
`content/phenomenology/c1_preface/__init__.py` for a course. Course and lesson
fields are exactly those of `docs/philosophy/PLAN.md` §E, with `body` 7–18
blocks (a `code` block counts as one).

### E.2 The source text

The Subject's single source is **Steve McConnell, *Code Complete: A Practical
Handbook of Software Construction*, 2nd edition (Redmond, Washington:
Microsoft Press, 2004)**. Printings differ in their errata, not their
pagination, as far as this document knows *(check against the copyright
page)*. Until the operator's copy is available:

- every page reference is `TBD`, in §C and in the lesson's comment;
- section numbers and titles in §B and §C are as remembered, marked
  *(check)* where the review was unsure, and are corrected from the contents
  page when it arrives;
- every figure attributed to the book is marked in §S.2 and printed in the
  lesson as "the book reports …, after Jones" with the comment `# verify`
  beside it, so that a grep finds every one;
- no lesson carries a quotation.

When the copy arrives, the orchestrator records its route (a private
extraction outside the repository, as for Phenomenology) in
`docs/code-complete/AUTHORING.md`, and one pass per course fills the pages,
resolves every *verify* and *(check)*, and adds opening quotations where they
earn their place.

### E.3 Quoting

*Code Complete* is in copyright (Steve McConnell, 2004). The Subject is
commentary, and keeps quotation smaller than the earlier read-alongs, because
a practical handbook's value is in its formulations:

- A lesson may open with **one quotation of at most 40 words**, cited by page,
  only once the text is in hand, and only where the sentence is the chapter's
  own summary of its argument. A lesson's quotations total at most **60
  words**. No lesson depends on a quotation; every lesson is written first
  without one.
- **Never reproduce the book's code listings, checklists, tables or figures.**
  Not retyped, not "adapted" line by line. The code in every lesson is written
  for it (§D.4). A table's *figures* may be used, a few at a time, as facts
  with their source ("the book's table, after Jones, gives 30% for unit
  testing"); the table itself is not reproduced. A lesson may name a
  checklist and paraphrase two or three of its points; never more.
- Every quoted phrase is copied from the source text, character for
  character, with its page in a comment beside the lesson dict. Never from
  memory, a secondary source, a blog or this document, which quotes nothing.
- The book's famous lines that are someone else's (Knuth on premature
  optimisation, Brooks's law, Dijkstra's title) are attributed to their
  author and, if quoted, quoted from the book's citation, counted against the
  same limits.

### E.4 The author's checklist

The per-lesson procedure of `docs/philosophy/PLAN.md` §E, with
`python3 scripts/preview_subject.py code-complete --course <slug> --out <dir>`
to render, and these additions:

1. Write the body without a quotation (§E.2). Mark every figure attributed to
   the book with `# verify` in a comment beside the dict and with its §S.2 id.
2. Every code block is one of §D.4's snippets or a new one written for the
   lesson; never the book's. A new snippet is run through the reference model
   (or the built lab) and its figures recorded in §C.
3. Every preset id appears in a body `p` with the figures it shows; every tile
   a view prints is explained in prose at least once in the course.
4. The exercise (§B) is an `h3` "Exercise", a `code` block, and a `p` that
   says what to find; the answer goes in `worked` or the quiz's `why`, never
   on the same screen as the question.
5. Inline code in prose is a backtick run and stays short: an identifier, a
   condition, a call. A statement longer than about 40 characters goes in a
   `code` block.
6. `/usr/bin/python3 scripts/speechcheck.py` with the code dialect on (§H.1),
   and listen to one lesson per course with the read-out.

---

## §F Voice: the read-along, for a working programmer

`docs/capital/PLAN.md` §F and `docs/phenomenology/PLAN.md` §F hold where this
section is silent: the chapter first, then line by line; "you", warmly; the
history of an idea as a story with people in it, at most once a lesson; at
most one light remark, preferably pointing at the author's own (McConnell has
many: the oyster, the wicked problem, the tool fantasyland); the `note` names
the lesson's one limit; the last `p` points to the next lesson by title; no
slang, no first-person anecdotes, no "let's"; presented, not endorsed.

What is different for this book:

1. **The reader is a working programmer, or becoming one.** Open with the
   reader's own code where the chapter is about something already in it —
   a routine that has grown, a variable declared at the top, a bug found by
   bisecting — and reach the chapter's argument within the paragraph. That is
   most chapters, so ration it as Phenomenology does: open with a scene in at
   most half of a course's lessons, and with the chapter's own question in the
   rest.
2. **The chapter's argument comes first, in paraphrase.** Where the earlier
   read-alongs read a passage, this one sets out what the chapter argues and
   why, in two or three sentences that say whose claim it is ("McConnell
   argues …", "the chapter's table, after Jones, gives …"), then goes through
   its sections in order. Once the text is in hand, a 40-word opening
   quotation may precede the paraphrase (§E.3).
3. **Then the code.** Every lesson turns from the argument to a snippet in
   its second half, does the chapter's count on it with the lab, and ends
   with the exercise. The count is never the point; what it shows about the
   code is.
4. **McConnell is presented, not endorsed.** The book is a synthesis of
   research and practice to 2004, and much of it is now common ground; some
   of it is disputed. Where later practice disagrees — the tolerance for long
   routines, comment density, prefix naming conventions, how much to settle
   upstream, test-first — the lesson states the book's position at strength
   and the later view fairly, and does not settle it. A lesson may do this
   **at most once per course**, in the `note` or a late `p`, in the lesson
   named as that course's home: Upstream Prerequisites (iterative and agile
   practice); Routine Length and Parameters (the short-function school);
   The Power of Variable Names (prefixes and today's editors); Unusual Control
   Structures (the `goto` history: Dijkstra 1968, Knuth 1974, languages
   without `goto`); Structured Basis Testing (test-first in §22.2 beside
   test-driven development); Programming Tools (continuous integration, build
   systems); Self-Documenting Code (the comment debate). Never "this advice is
   outdated" or "modern developers know better" in the lesson's voice.
5. **The numbers are other people's.** Every rate, cost and ratio the book
   quotes is an average over projects the reader did not work on, collected
   by Jones, Boehm and others, mostly before 2004. A lesson says once, where
   it leans on one, whose figure it is and that it is an average; it never
   says "studies show" without the study.
6. **No language wars.** Java is the lessons' language for the reasons in
   §D.0; no lesson says one language is better. Where Java differs from
   C or Python on the point at hand, the lesson says so in a sentence.

**One exemplary paragraph** (a `p` block for “Scope, Span and Live Time”, after
the chapter's argument):

> You have probably written a routine like the one in the lab: a comment that
> says "initialize all variables", three declarations under it, and then the
> work, a screen further down. It looks tidy, and McConnell's measure says
> what it costs. A variable is live from the first line that mentions it to
> the last, and every line in between is a line on which a reader has to
> remember what it holds. Count it for `total`: declared on line 4, used on
> lines 14, 15 and 17, so it is live for 17 − 4 + 1 = 14 lines, and nine of
> them have nothing to do with it. Move each declaration down to the loop that
> uses it and the lab's average live time falls from 11 lines to 5, with not a
> statement changed. Nothing about the program's behaviour is different; what
> is different is how much of it you have to hold in your head at once, which
> is the complexity Chapter 5 said was the thing to manage.

---

## §G What is left out, and why

- **The book's checklists, code listings, tables and figures.** Copyright
  (§E.3), and a checklist reproduced is a checklist not read. Lessons point to
  them by chapter.
- **Language-specific sections** — C++ pointers and memory management in
  detail (§13.2), Visual Basic specifics, C macros (§7.7), the C++ class
  details of §6.5. Named in the lesson that meets them, with one sentence of
  what the section covers; not taught, because the lessons use one language.
- **Chapter 35's reading list.** Named and pointed to in Themes of
  Craftsmanship; not reproduced, because it is the book's and because a 2004
  reading list needs the reader's own judgement about what has been
  superseded.
- **What has happened since 2004.** Version-control workflows past §28.2's
  configuration management, continuous delivery, code-review tooling, static
  analysers, language features (lambdas, records, null-safety), and AI
  assistants. A lesson may say in one sentence what is different now, under
  §F.4's rule; the Subject does not teach them.
- **Running code.** The kit reads code and never executes it (§D.2). A
  reader who wants to run a snippet runs it in their own environment; no
  lesson depends on it.
- **Process methodologies** (Scrum, XP as a whole, the Rational Unified
  Process). The book names them; the lessons name them where the book does.
- **Estimation as a discipline.** McConnell's later book on estimation is a
  separate work; Managing Construction does only Chapter 28's arithmetic.
- **The companion web site.** Its addresses are not linked: the site's
  reviewed link origins do not include it, and the book's own references are
  enough.

---

## §S Sources, and the register of figures to verify

### S.1 Sources the lessons may cite

Cited by author and year in prose; never quoted at length. Every work here
except the first is cited **as the book cites it**: the lesson says "the book
cites Fagan 1976", not "Fagan found", until the accuracy review has checked
the original. Years and titles are as remembered and are checked against the
book's bibliography *(verify all)*.

- McConnell, S. (2004). *Code Complete: A Practical Handbook of Software
  Construction*, 2nd ed. Microsoft Press. The source of every lesson.
- Basili, V. R., Briand, L. C. and Melo, W. L. (1996). A validation of
  object-oriented design metrics as quality indicators. *IEEE Transactions on
  Software Engineering* 22(10).
- Basili, V. R. and Perricone, B. T. (1984). Software errors and complexity:
  an empirical investigation. *Communications of the ACM* 27(1).
- Beck, K. (2003). *Test-Driven Development: By Example*. Addison-Wesley.
- Boehm, B. W. (1981). *Software Engineering Economics*. Prentice Hall.
- Boehm, B. W. (1987). Industrial software metrics top 10 list. *IEEE
  Software* 4(5).
- Boehm, B. W. et al. (2000). *Software Cost Estimation with COCOMO II*.
  Prentice Hall.
- Boehm, B. and Turner, R. (2004). *Balancing Agility and Discipline*.
  Addison-Wesley.
- Böhm, C. and Jacopini, G. (1966). Flow diagrams, Turing machines and
  languages with only two formation rules. *Communications of the ACM* 9(5).
- Brooks, F. P. (1975; anniversary edition 1995). *The Mythical Man-Month*.
  Addison-Wesley.
- Brooks, F. P. (1987). No silver bullet: essence and accidents of software
  engineering. *Computer* 20(4).
- Card, D. N., Church, V. E. and Agresti, W. W. (1986). An empirical study of
  software design practices. *IEEE Transactions on Software Engineering*
  12(2).
- Dijkstra, E. W. (1968). Go To statement considered harmful (letter).
  *Communications of the ACM* 11(3).
- Fagan, M. E. (1976). Design and code inspections to reduce errors in
  program development. *IBM Systems Journal* 15(3).
- Feldman, S. I. (1979). Make — a program for maintaining computer programs.
  *Software: Practice and Experience* 9(4). *(check that the book cites it)*
- Fowler, M. (1999). *Refactoring: Improving the Design of Existing Code*.
  Addison-Wesley.
- Gorla, N., Benander, A. C. and Benander, B. A. (1990). Debugging effort
  estimation using software metrics. *IEEE Transactions on Software
  Engineering* 16(2).
- Gould, J. D. (1975). Some psychological evidence on how people debug
  computer programs. *International Journal of Man-Machine Studies* 7.
- Jones, C. (1996). Software defect-removal efficiency. *Computer* 29(4).
- Jones, C. (1998). *Estimating Software Costs*. McGraw-Hill.
- Jones, C. (2000). *Software Assessments, Benchmarks, and Best Practices*.
  Addison-Wesley.
- Knuth, D. E. (1971). An empirical study of FORTRAN programs. *Software:
  Practice and Experience* 1(2).
- Knuth, D. E. (1974). Structured programming with go to statements.
  *Computing Surveys* 6(4).
- Liskov, B. (1988). Data abstraction and hierarchy. *SIGPLAN Notices*
  23(5). *(check the year the book cites)*
- McCabe, T. J. (1976). A complexity measure. *IEEE Transactions on Software
  Engineering* SE-2(4).
- Miara, R. J., Musselman, J. A., Navarro, J. A. and Shneiderman, B. (1983).
  Program indentation and comprehensibility. *Communications of the ACM*
  26(11).
- Miller, G. A. (1956). The magical number seven, plus or minus two.
  *Psychological Review* 63(2).
- Myers, G. J. (1979). *The Art of Software Testing*. Wiley.
- Parnas, D. L. (1972). On the criteria to be used in decomposing systems
  into modules. *Communications of the ACM* 15(12).
- Sackman, H., Erikson, W. J. and Grant, E. E. (1968). Exploratory
  experimental studies comparing online and offline programming performance.
  *Communications of the ACM* 11(1).
- Shull, F. et al. (2002). What we have learned about fighting defects.
  *Proceedings of the 8th International Software Metrics Symposium*.
- Stevens, W. P., Myers, G. J. and Constantine, L. L. (1974). Structured
  design. *IBM Systems Journal* 13(2).

### S.2 The register of figures to verify

Every figure a lesson attributes to the book is listed here with the value
this specification believes the book gives, where it is believed to be, and
its original source where known. **Every one is "verify against the book"**:
the accuracy review checks each against what it can reach, and the book
settles it. A lesson prints the figure with `# verify F<n>` beside it until
the book has been checked, and the reviewer of each course greps for the
marker.

| id | claim as the lesson would use it | value believed | where | original source (as the book cites it) |
| --- | --- | --- | --- | --- |
| F1 | share of a project's time that construction takes | 30% to 80%, depending on size | §1.2 | — (the book's synthesis; see Chapter 27) |
| F2 | construction errors as a share of all errors on some projects | a large share (the book gives a range) | §1.2 | *(verify whether the book gives one; the lessons do not use it until checked)* |
| F3 | relative cost of fixing a defect by phase introduced × phase detected | requirements: 1, 3, 5–10, 10, 10–100; architecture: 1, 10, 15, 25–100; construction: 1, 10, 10–25 (detected at requirements, architecture, construction, system test, post-release) | §3.1, Table 3-1 *(check number)* | Fagan 1976; Humphrey, Snyder and Willis 1991; Leffingwell 1997; Willis et al. 1998; Grady 1999; Shull et al. 2002; Boehm and Turner 2004 |
| F4 | statements equivalent to one C statement | C 1, C++ 2.5, Fortran 95 2, Java 2.5, Perl 6, Python 6, Smalltalk 6, Visual Basic 4.5 | §4.1, Table 4-1 | Jones 1998; Prechelt 2000 *(check)* |
| F5 | productivity of programmers experienced in a language against novices | about 30% higher with three or more years' experience | §4.1 | Boehm et al. 2000 |
| F6 | a class's data members | consider decomposing above about seven (7 ± 2) | §6.3 | Miller 1956 |
| F7 | depth of inheritance | keep shallow; deep trees associated with more faults; a limit of about six levels is cited | §6.3 | Basili, Briand and Melo 1996; Riel 1996 |
| F8 | routine length | the studies reviewed tolerate up to about 100–200 lines; small routines not shown cheaper | §7.4 | Basili and Perricone 1984; Card, Church and Agresti 1986; Selby and Basili 1991; Lind and Vairavan 1989; Jones 1986 |
| F9 | number of parameters | limit to about seven | §7.5 | Miller 1956 |
| F10 | span and live time | definitions (lines between references; last − first + 1) and the book's worked example figures | §10.4 | the book's own |
| F11 | variable-name length | debugging effort lowest for names averaging 10–16 characters; 8–20 almost as good | §11.1 | Gorla, Benander and Benander 1990 |
| F12 | literals in a routine's body | only 0 and 1 | §12.1 / §12.7 | the book's own |
| F13 | loop length and nesting | keep a loop short enough to see whole; limit nesting to about three levels | §16.2 | Yourdon 1986 *(check)* |
| F14 | decision points and what to make of them | rule: 1 + if, while, repeat, for, and, or, + each case; 0–5 probably fine, 6–10 start to simplify, 10+ split part of the routine off | §19.6 | McCabe 1976; the bands are the book's guidance |
| F15 | depth of nesting a reader can follow | few people understand more than three levels of nested `if`s | §19.4 | Yourdon 1986; Chomsky and Weinberg as cited *(check)* |
| F16 | defect-detection rates (lowest, modal, highest) | informal design reviews 25/35/40; formal design inspections 45/55/65; informal code reviews 20/25/35; formal code inspections 45/60/70; modelling or prototyping 35/65/80; personal desk-checking 20/40/60; unit test 15/30/50; new-function test 20/30/35; integration test 25/35/40; regression test 15/25/30; system test 25/40/55; low-volume beta 25/35/40; high-volume beta 60/75/85 | §20.3, Table 20-2 *(check number)* | Jones 1996, 2000; Shull et al. 2002 |
| F17 | combining techniques | no single technique exceeds about 75%, the modal average is about 40%, and a combination of unlike techniques is needed for 95% or more | §20.3 | Jones |
| F18 | hours per defect found, inspection against testing | 3.5 staff-hours by inspection against 15–25 by testing (IBM); about 3 against 12 (Microsoft) | §20.3 or §21.3 *(check)* | Kaplan 1995; Moore 1992 *(check both)* |
| F19 | errors to expect | industry average about 1–25 per thousand lines of delivered code; Microsoft 10–20 in-house, 0.5 released; cleanroom 3 in-house, 0.1 released; errors cluster in a few classes (80/20) | §22.4 | Jones 1998; Moore 1992; Cobb and Mills 1990; Endres 1975, Gremillion 1984, Boehm 1987 |
| F20 | variation among programmers in debugging | experienced programmers: the fastest found defects in about a third of the time of the slowest, inserting fewer new ones | §23.1 | Gould 1975 |
| F21 | small changes and errors | one-line changes have a high error rate | §24.4 | Weinberg 1983 |
| F22 | the Pareto principle in performance | 20% of routines take 80% of time; under 4% of a program accounts for more than 50% of its run time | §25.2 | Boehm 1987; Knuth 1971 |
| F23 | measured effect of each tuning technique | the book's per-language timings | §26.1–26.6 | the book's own measurements |
| F24 | defect density by project size | under 2K lines 0–25 per KLOC; 2K–16K 0–40; 16K–64K 0.5–50; 64K–512K 2–70; 512K or more 4–100 | §27.3, Table 27-1 | Jones 1998 |
| F25 | productivity by project size (lines per staff-year) | 1K: 2,500–25,000; 10K: 2,000–25,000; 100K: 1,000–20,000; 1M: 700–10,000; 10M: 300–5,000 | §27.4, Table 27-2 | Jones 1998; Boehm et al. 2000; Putnam and Meyers 1992 |
| F26 | effort multipliers | the COCOMO II range of each factor, e.g. programmer capability 0.76–1.34, analyst capability 0.71–1.42, product complexity 0.73–1.74, time constraint 1.00–1.63, storage constraint 1.00–1.46, use of tools 0.78–1.17, personnel continuity 0.81–1.29 | §28.3 *(check that the book gives a table)* | Boehm et al. 2000 |
| F27 | indentation | two to four spaces gave the best comprehension | §31.2 *(check)* | Miara et al. 1983 |
| F28 | comment density | clarity peaked at about one comment per ten statements | §32.4 *(check)* | an IBM study as the book cites it |
| F29 | differences among programmers | about 10 to 1 in productivity among programmers with the same experience | §33.x *(check; may be Chapter 28)* | Sackman, Erikson and Grant 1968 and later studies |

Where a lesson uses a COCOMO II multiplier, Jones's rate or another figure
whose original is better known than the book's citation of it, the accuracy
review checks the original too; where the book and the original differ, the
lesson uses the book's figure (it is a read-along) and the `note` says the
original's.

---

## §H Wiring notes for the orchestrator, and the renderer work

### H.1 Renderer work (`chrome-renderer` tier), blocking authoring

The lesson schema has no way to show code. Today a body block is one of `p
h3 math ul ol def thm example proof` (`scripts/mathpath/render.py` `_block`
raises on anything else), and the only monospace display is the `math` block,
which is spoken by `speech.say_block` as mathematics. Measured on the read-out
as it stands (`speech.say`):

| run | spoken |
| --- | --- |
| `a && b` | "A and and b" |
| `a \|\| b` | "A the absolute value of, b" |
| `!done` | "done" — **the negation is dropped** |
| `int[] a = new int[n];` | "int at A equals new int at n" |
| `x != y` | "x is not equal to y" (correct) |

A lesson on DeMorgan read aloud as "not done" → "done" teaches the opposite
of the page. So:

- **R1 — a `code` body block.** `("code", ["line", …])`: a list of lines (a
  bare string raises, as `_mathblock` does); rendered as `<pre
  class="codeblock"><code>` with each line escaped and wrapped in a span
  whose number is drawn by a CSS counter (so copying the code copies no
  numbers); monospace, `white-space: pre`, `overflow-x: auto` inside the
  block so a 72-character line scrolls within the block at 360 px and the
  page does not; no syntax colouring; both themes; passes
  `tests/browser_contrast.js`. Limits enforced by
  `TestLessonDataMatchesTheRenderer`: at most 30 lines, at most 80 characters
  a line, no tab characters. The test's allowed-kinds list gains `code`.
- **R2 — a code dialect for the read-out.** `speech.say_code(line)`: `&&`
  "and", `||` "or", a prefix `!` "not", `==` "equals", `!=` "is not equal
  to", `=` "is set to" (in a statement), `+=` "is increased by", `++` "is
  incremented", `--` "is decremented", `[i]` "at index i", braces and
  semicolons silent, a string literal read as its text; everything else
  through `speech.say`. Applied to every line of a `code` block, and — on a
  path whose PATH dict carries `"speech": "code"` — to every backtick run,
  `key` line and `worked` line, so that `` `!done` `` in prose reads "not
  done". Global rules are not changed: `||` is scheduling notation in
  Operations Research and `!` is a factorial elsewhere. `speechcheck.py`
  and `tests/test_speech.py` learn the dialect; on this path a run with `&&`,
  `||` or a prefix `!` that reaches plain `say` is a failure.
- **R3 — the `x` shorthand stays the only inline markup.** Inline code is a
  backtick run, rendered as the existing math span (monospace); no new inline
  syntax.

R1 and R2 land, with their tests, before the first lesson with a code block
is written. The kit does not wait for them.

### H.2 Lab-infrastructure work (`lab-arithmetic` tier)

- `scripts/labcheck.js`: sweep `<textarea>` controls with the same hostile
  strings as text inputs, read their initial value from the DOM after the
  page's scripts run (they are filled by script, §D.0), and include
  `TEXTAREA` when deciding whether a `<select>` rewrites another control
  (`presetSelects` filters `INPUT` and `SELECT` today). Readkit's textareas
  are not swept either; this change will sweep them, so run its pages too.
- `scripts/mathcheck.js`: one block per `cckit` mode, the §C figures as cases.

### H.3 Wiring

As `docs/phenomenology/PLAN.md` §H and every declaration site in `AGENTS.md`
§0, with these values:

- Package `code_complete`; path slug `code-complete`. The slug is the
  package name with `-` for `_`, so **no** `build_paths.PACKAGE_OF_SLUG`
  entry is needed (the default rule finds it).
- Check-id prefix `cc`; check ids `cc-course7-lesson-<lesson-slug>`, longest
  58 characters (§B).
- `CC_DISCLAIMER_RE = r"a reason to look at it, not a verdict"`, in
  `tests/test_site_invariants.py` beside the eleven others, with its path-page
  constant and its entry in `PATH_MATERIAL_DISCLAIMER`.
- `content/spoken/code_complete.py` (ONE file, named for the package);
  `code_complete_semantic_copy` in `tests/test_public_copy.py`, derived from
  the rendered page.
- `scripts/build_paths.py`: import and add to `GENERATED_PATHS` at the start
  of the branch with every `COURSE = None`; add `"cckit"` to
  `KITS_WITH_EXPECTATIONS` last. `scripts/generated-pages.txt` and
  `scripts/generated-expectations.json` are rewritten by the build.
- `scripts/smoke.py`, `scripts/canvas_sources.js`.
- `release/contract.json` and `release/contract.example.json` (both),
  `release/contract.schema.json` (each new check id pinned by name, and
  `minItems` equal to the pin count).
- `Containerfile.release` and `.github/workflows/ci.yml` enumerations:
  backslash-continued lists, no comment inside them, `bash -n` every `run:`
  block, and never read either through a width-truncating pipe.
- `tests/test_site_invariants.py` (slug tuples, course-home constants,
  `REQUIRED_PAGES`, and the `TestGeneratedPathIsCurrent`,
  `TestLessonDataMatchesTheRenderer` and `TestEveryLabBuilds` import lists),
  `tests/content_preservation.json` (every `.py` in the package, generated with
  `/usr/bin/python3` via the test module's own fingerprint function — the
  moment the package joins `GENERATED_PATHS`), `tests/test_review_remediation.py`,
  `tests/test_public_copy.py`, `tests/test_course_ui.py`,
  `tests/test_canvas_contract.py`, `tests/test_browser_source.py`,
  `tests/test_responsive_ui.py`, `tests/test_generation4.py`,
  `tests/test_generation5_catalog.py`, `tests/browser_acceptance.js`,
  `tests/browser_contrast.js`, `tests/browser_interactions.js`.
- `scripts/catalog.py`, one entry, last in the `computing` group (after
  Operations Research):

  ```
  {
      "slug": "code-complete",
      "group": "computing",
      "short_title": "Code Complete",
      "kind": "Read along",
      "card": "Steve McConnell&rsquo;s <em>Code Complete</em>, chapter by "
              "chapter, with each chapter&rsquo;s guidance measured on short "
              "pieces of code.",
  },
  ```

  No `builds_on`: the Subject assumes no other. **Placement, argued by
  dependency:** the catalog's rule orders a group by dependency, so a Subject
  that assumes nothing may stand anywhere in it; nothing places it after
  Algorithms, since it uses none of Algorithms. It goes last because that is
  the precedent for a read-along (in Philosophy and close reading, the two
  read-alongs follow the topical Subject), because the three Subjects already
  in the group share a dependency on Discrete Mathematics that this one does
  not, and keeping them together keeps the group note one sentence. The
  group note becomes:

  > "Algorithms, System Design and Operations Research build on Discrete
  > Mathematics, the last two on Algebra as well; Code Complete assumes only
  > that you can read a short routine."

  (Checked against the copy rules in `catalog.py`'s docstring: no "path", no
  "N subjects", no "course N", no "take these in order".) Then re-run
  `scripts/build_index.py` and `scripts/build_auth_pages.py`; never edit
  `site/index.html`'s generated region by hand.
- The PATH's tagline and description say "Seven courses and 41 lessons"; the
  counts test reads the PATH, so §B's total and both sentences move together.
- Counts after wiring: **thirteen Subjects**; 120 courses; 1,141 lessons;
  49 new pages (41 lessons, 7 course homes, 1 path page), so 1,230 pages
  become 1,279; 168 lab modes registered (8 added); 24 kits in
  `KITS_WITH_EXPECTATIONS`. Every "twelve Subjects", "113 courses",
  "1,100 lessons" and "1,230 pages" in `AGENTS.md` §0 and §1, `README.md`'s URL
  layout and the tests is updated in the wiring commit, from the numbers the
  build reports rather than from this list.
- `AGENTS.md` §0's table gains the row; the check-id prefix list gains
  `cc`; the page-weight note gains a re-measurement paragraph.

---

## §R Review record

The specification is reviewed before authoring by two models independently —
a pedagogy review (the `pedagogical-expert` brief) and an accuracy review
that checks every claim about the book and every §S.2 figure against what it
can reach, marking each CERTAIN, LIKELY or CHECK-AGAINST-TEXT — and each course
again after authoring (`docs/code-complete/SECOND-REVIEW.md`). A third pass,
once the book is in hand, resolves every *verify* and *(check)*. Findings and
their resolutions are appended here.

(No reviews yet.)
