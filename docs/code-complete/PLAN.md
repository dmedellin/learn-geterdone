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

**Status: specification, reviewed and reconciled; blocked on one thing.**
The book's text is in hand (the operator's copy, §E.2): every page reference
and section title in §C was checked against it, every figure in §S.2 is
settled, and each lesson's opening quotation is chosen and counted (§C,
**Quote**). Both pre-authoring reviews are reconciled (§R). What still blocks
authoring is renderer support for code (§H.1, a `chrome-renderer` task): the
lesson schema has no code block today, and the read-out mangles code
operators. The kit (§D) can be built in parallel; its reference model is in
§D.4.

Contents

- §0 The one question, answered for this Subject
- §A PATH fields
- §B The seven courses, and the module names
- §C Every lesson: 41 entries
- §D The lab kit: `cckit` (8 modes, 36 views)
- §E Package layout, the source text, quoting, and the author's checklist
- §F Voice: the read-along, for a working programmer
- §G What is left out, and why
- §S Sources, and the register of figures
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
4. **The chapter comes first, mostly in paraphrase.** The earlier
   read-alongs quote at length. This book is in copyright, so a lesson opens
   with one short quotation (§C's **Quote**, at most 40 words) and then sets
   out the chapter's argument in its own words, pointing to the section by
   number and page; it quotes at most 60 words in all (§E.3), and no lesson's
   argument depends on a quotation.
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

**Title: decided by the owner** — `"Code Complete, Read Along"`, with the
catalog's `short_title` `"Code Complete"`. It follows the precedent (`"Capital,
Read Along"`, `"Phenomenology of Perception, Read Along"`, with `short_title`
dropping the suffix on the home card, B-22), and it keeps a breadcrumb or
`<title>` from presenting a page of this library as the book itself, which
belongs to McConnell and Microsoft Press. The Subject's catalog entry goes
last in the computing group, with the note proposed in §H.3. **Language:
decided by the owner** — Java (§D.0).

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
   section by number and page, and quotes at most a sentence or two. The code is
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
| 1 | `code-complete-laying-the-foundation` | Laying the Foundation | Part I, Chapters 1–4 | 3 | Beginner |
| 2 | `code-complete-high-quality-code` | Creating High-Quality Code | Part II, Chapters 5–9 | 9 | Beginner |
| 3 | `code-complete-variables` | Variables | Part III, Chapters 10–13 | 6 | Intermediate |
| 4 | `code-complete-statements` | Statements | Part IV, Chapters 14–19 | 7 | Intermediate |
| 5 | `code-complete-code-improvements` | Code Improvements | Part V, Chapters 20–26 | 8 | Intermediate |
| 6 | `code-complete-system-considerations` | System Considerations | Part VI, Chapters 27–30 | 4 | Intermediate |
| 7 | `code-complete-software-craftsmanship` | Software Craftsmanship | Part VII, Chapters 31–35 | 4 | Intermediate |

Total 41. Against the orchestrator's starting proposal two splits changed in
review (§R, pedagogy #20–#21): Chapter 8 is split, because assertions and
exceptions are two mechanisms with two different labs, and Chapters 1 and 2
share Course 1's first lesson, because neither chapter has a count of its own
and both are short (pp. 3–21 together). Chapter 22 is split into Structured
Basis Testing and Boundaries and Bad Data, and Chapters 34 and 35 share the
last lesson. Course titles are the book's Part titles, as printed; the slugs
carry the `code-complete-` prefix, so the generic titles "Variables" and
"Statements" collide with nothing in the flat course namespace.

**Chapter splits** (one hard idea per lesson), checked against the contents
pages; §C gives each lesson's pages and sections. Chapter 5 (§§5.1–5.2,
pp. 73–86; §§5.3–5.5, pp. 87–123), Chapter 6 (§§6.1–6.2, pp. 125–142;
§§6.3–6.6, pp. 143–160), Chapter 7 (§§7.1–7.3, pp. 161–172; §§7.4–7.7,
pp. 173–186), Chapter 8 (§§8.1–8.3, pp. 187–197, invalid input, assertions
and error handling; §§8.4–8.8, pp. 198–213, exceptions, barricades,
debugging aids and how much to leave in production), Chapter 10 (§§10.1–10.3,
pp. 237–243; §§10.4–10.8, pp. 244–258), Chapter 12 (§§12.1–12.3, pp. 291–296;
§§12.4–12.9, pp. 297–318), Chapter 19 (§§19.1–19.3, pp. 431–444; §§19.4–19.6,
pp. 445–460), Chapter 22 (§22.1, §22.2 and §22.3 to the end of structured
basis testing, pp. 499–509; data-flow testing on p. 509 to the end of §22.3,
and §§22.4–22.7, pp. 509–533).

**Part files.** A course with more than six lessons splits into `part_a.py`
and `part_b.py`: Course 2 (lessons 1–4 Chapters 5–6, 5–9 Chapters 7–9),
Course 4 (1–4 Chapters 14–17, 5–7 Chapters 18–19), Course 5 (1–4 Chapters
20–22, 5–8 Chapters 23–26). The rest are one `part_a.py`.

**Check ids** take the form `cc-course7-lesson-<lesson-slug>` (18 characters
before the slug). Every lesson slug in §C is at most 40 characters, so every
check id is at most 58, inside the 72-character cap; the longest is
`cc-course2-lesson-design-heuristics-and-information-hiding` (58).

**Module names.** Each chapter is one module, named `Chapter N · short form`
from the table below (at most 60 characters; never cut), except that
Chapters 1 and 2 share one module and Chapters 34 and 35 another. A lesson's
`module` is its chapter's name. The short forms are the spec's; the course
`summary` gives each chapter's full title as the edition prints it. The full
titles below were checked against the contents pages and the chapter
openings.

| chapter | module name | full title (as printed) |
| --- | --- | --- |
| 1–2 | `Chapters 1–2 · Construction and Metaphors` | Welcome to Software Construction; Metaphors for a Richer Understanding of Software Development |
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
without the lab, and at least one quiz item asks about the snippet. Its
answer, computed by the reference model (§D.4) and given in §C as
**Answer**, goes in that quiz item's `why` and nowhere else on the page, so
the reader commits to an answer before seeing it. The exercise's instance is
never a preset's (the worked example works a preset; the exercise is the
reader's). The lab may be used to check the answer afterwards; the body says
so in one sentence.

**Every lesson ends by sending the reader to their own code.** The last of
the `steps` is the act §C's **Own:** line names, applied to a routine (or a
record, a schedule, a team) of the reader's own, pasted into the lab where
the view takes code. It is phrased as an instruction with an observable
result ("paste…, note the count, and write one sentence on…"), never as
"reflect on".

---

## §C Every lesson

Format:

- **slug** — Title — *module* — minutes (an estimate for the author; there is
  no minutes field)
- **Read:** the sections the lesson covers, with the printed pages of the
  second edition, and what the argument is, in paraphrase.
- **Quote:** the one opening quotation (§E.3), its page and its word count,
  checked character for character against the text. The lesson may open
  without it; it may not open with another without recording it here.
- **Do:** the observable objective; **Standard:** the act that shows it,
  without the lab, and its pass level.
- **Lab:** mode/view (§D); presets with their exact instances; the tile
  values the reference model computes, in §D.0's formats. The exact strings are
  read with `labcheck.js --observe` at authoring and pinned (rule 3).
- **Misconception:** the wrong model `mistakes[0]` names and refutes. **Also**
  (where given): a second wrong model for `mistakes[1]`.
- **Worked:** the single worked example, in one line. It works a preset's
  instance, never the exercise's.
- **Exercise:** the applied task. **Answer:** its answer, which goes in the
  `why` of one quiz item (§E.4 item 4) and nowhere else on the page.
- **Own:** what the last of the `steps` sends the reader to do with their own
  work, and the input it uses.
- **Sources:** the book's sections and the works it cites; every figure here
  marked *F<n>* is in §S.2, settled against the text.

**Read lines are paraphrase.** This document quotes the book only in the
**Quote** lines, each within §E.3's limits. Its other quotation marks enclose a
misconception's wording, a preset's label, a lab's tile or a code string.
Section numbers, titles and pages were checked against the operator's copy
(printed page = PDF page − 37).

Preset ids are suggestions; **the instances are not optional**. Every figure
below was computed by the reference model in §D.4 from the instance given, and
an author who changes an instance recomputes it and records it here in the
same commit. Snippets are Java, four-space indent, at most 20 lines unless an
entry says otherwise. Line numbers count every line of the snippet from 1,
blank and comment lines included (§D.0).

**Misconceptions.** A misconception is a reading of the chapter someone could
hold, or the view the chapter argues against stated at its strongest — never a
jibe at a language or a methodology. Where it is a position someone holds, the
lesson names its holder or its school. **A misconception is never the later
view named as the course's §F.4 aside**: that view goes in the `note` or a late
`p`, stated at strength and not settled. **A misconception is refuted by the
chapter's argument; a lab run on an illustrative instance illustrates the
refutation and is said to** ("on the lesson's illustration, …"), never "the
lab proves".

### Course 1 — Laying the Foundation (`code-complete-laying-the-foundation`, 3)

Part I, Chapters 1–4. What construction is and which picture of it to work
with, what must be settled upstream, and the decisions taken at the start of
construction. Its `how_to` says the course has the least code of any, because
the book's first Part is about the work around the code; its `not_covered`
says requirements engineering and architecture are named, not taught.

1. **construction-and-its-metaphors** — Construction and Its Metaphors — *Chapters 1–2 · Construction and Metaphors* — 15 min
   - **Read:** Chapter 1, pp. 3–8: §1.1 (p. 3), the activities the book calls
     construction (detailed design, coding and debugging, integration,
     developer testing, and the rest of its list) set against problem
     definition, requirements, architecture, system testing and maintenance;
     §1.2 (p. 6), why construction matters (30 to 80 percent of a project's
     time, *F1*; the one activity sure to happen; the source code often the
     only accurate description of the software); §1.3 (p. 8). Chapter 2,
     pp. 9–21: §2.1–2.2 (pp. 9–13), a metaphor is a heuristic, not an
     algorithm; §2.3 (p. 13), the metaphors themselves — McConnell rejects
     the writing metaphor for anything beyond a small project and calls the
     farming one weak, and prefers accretion (the oyster) and building
     (planning grows with the size of what is built; changing the
     foundation late is expensive), with the toolbox and combinations.
   - **Quote:** p. 8, 21 words — “Software construction is the central
     activity in software development; construction is the only activity
     that’s guaranteed to happen on every project.”
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
     coding and debugging, 8/25 = 32%, `pfPareto` "6 of 8 entries reach 4/5
     of the total"), `large-project` (1,400; 1,100; 1,300 c; 2,700 c;
     1,000 c; 1,200 c; 2,100; 1,200 → 12,000 hours, `pfTagged` 31/60 ≈ 51.7%,
     `pfTop` 9/40 = 22.5%, `pfPareto` "6 of 8"). Pins `pfTagged`, `pfTotal`.
     The body says that both shares sit inside the book's 30–80 percent
     range only because the lesson chose the hours so.
   - **Misconception:** "Writing software is like writing a letter: sit
     down, write it, and if it is wrong, throw it away and start again." The
     chapter's own target (§2.3): it calls the writing metaphor adequate
     only for small projects, and the building and accretion metaphors are
     its answer. **Also:** "Construction is just typing in a design someone
     else finished" — refuted by §1.1's list; on the lesson's illustration
     the construction activities are two-thirds of the hours.
   - **Worked:** 120 + 320 + 130 + 90 = 660 of 1,000 hours: 66%.
   - **Exercise:** requirements 40, detailed design 30, coding 90, code
     review 20, unit testing 40, system testing 50, user-interface design 30
     (changed from user documentation after the course's review: §1.1 names
     user-interface design as outside construction and says nothing of
     documentation). **Answer:** construction is detailed design, coding,
     code review and unit testing, 180 of 300 hours, 3/5 = 60%.
   - **Own:** last week's calendar, each block marked construction or not by
     §1.1's list, pasted into the lab as `name, hours, c` records.
   - **Sources:** McConnell §§1.1–1.3, 2.1–2.3; *F1*.
   - **Other quotations** (as authored): p. 14, Brooks's line as the book
     quotes it, 8 words; p. 12, "an algorithm in a clown suit", 6 words.
     Lesson total 35 words.

2. **upstream-prerequisites** — Upstream Prerequisites — *Chapter 3 · Upstream Prerequisites* — 15 min
   - **Read:** pp. 23–60. §3.1 (p. 24), why prerequisites matter, and the
     appeal to the cost of fixing a defect late (Table 3-1, p. 29, *F3*);
     §3.2 (p. 31), the kind of software (business systems, mission-critical,
     embedded life-critical) and iterative against sequential approaches
     (Tables 3-3 and 3-4, pp. 33–34: the cost table holds for iterative
     projects too, and an iterative project pays it in smaller pieces);
     §3.3–3.5 (pp. 36–55), problem definition, requirements, architecture;
     §3.6 (p. 55), how much time to spend upstream (*F30*).
   - **Quote:** p. 59, 21 words — “The overarching goal of preparing for
     construction is risk reduction. Be sure your preparation activities are
     reducing risks, not increasing them.”
   - **Do:** compute the relative cost of a set of defects from the phase each
     was introduced in and the phase it was found in, against finding each in
     the phase it was made.
   - **Standard:** given short descriptions of defects and the phase each
     was found in, place each by §§3.3–3.5, then compute the total cost range
     by the cost table and the ratio to finding them early (changed after
     the course's review, with the exercise below).
   - **Lab:** `defects/cost`, family 3. `cfg["table"]` is Table 3-1 as the
     lesson gives it (*F3*): introduced in requirements and found in
     requirements 1, architecture 3, construction 5–10, system test 10, after
     release 10–100; introduced in architecture and found in architecture 1,
     construction 10, system test 15, after release 25–100; introduced in
     construction and found in construction 1, system test 10, after release
     10–25. Records `introduced, detected, count` with stages `req arch cons
     test post`. Presets `found-late` (`req, test, 10; arch, post, 5; cons,
     test, 20` → `dfCost` 425–800, `dfEarly` 35, `dfRatio` 85/7 ≈ 12.1× to
     160/7 ≈ 22.9×), `found-early` (`req, req, 10; arch, arch, 5; cons, cons,
     20` → 35, 35, 1× to 1×), `requirements-late` (`req, post, 10` →
     100–1,000, 10, 10× to 100×). Pins `dfCost`, `dfRatio`.
   - **Misconception:** "The cost table says every project should finish its
     requirements before any coding starts." §3.2 argues the opposite for
     most kinds of project: the table is an argument for finding defects
     early, which an iterative project does by doing a little of each
     activity at a time. The later agile view — that much of what the
     chapter settles upstream is better discovered by building — is this
     course's §F.4 aside, in the `note`, at strength and unsettled.
   - **Worked:** 10 × 10 + 5 × (25 to 100) + 20 × 10 = 425 to 800 units,
     against 35 if each defect is caught where it was made.
   - **Exercise** (changed after the course's review, so that the reader
     places defects by phase, the act the lab cannot do, rather than
     repeating `requirements-late`): three defects found after release, given
     as descriptions: a rounding rule the specification got wrong (half up
     where the contracts require half to even); tax computed in both the
     order screen and the invoice service, disagreeing on a boundary date;
     a loop that totals a basket and skips its last line. **Answer:**
     requirements (10–100), architecture (25–100), construction (10–25):
     45 to 225 units against 3, a ratio of 15× to 75× (lab: `req, post, 1;
     arch, post, 1; cons, post, 1`).
   - **Own:** the last five defects in the reader's tracker, each with the
     phase it was introduced in and the phase it was found in, as records.
   - **Sources:** McConnell §§3.1–3.6; Table 3-1 and its sources (*F3*);
     §3.6's effort and schedule shares (*F30*); Boehm and Turner 2004 for the
     iterative discussion as the book cites it.
   - **Other quotations** (as authored): p. 26, "Why Isn’t Sam Coding
     Anything?", 5 words. Lesson total 26 words.

3. **key-construction-decisions** — Key Construction Decisions — *Chapter 4 · Key Construction Decisions* — 12 min
   - **Read:** pp. 61–70. §4.1 (p. 61), the choice of language, Table 4-1's
     statements equivalent to one statement of C (p. 62, *F4*) and the value
     of experience with a language (*F5*); §4.2 (p. 66), programming
     conventions; §4.3 (p. 66), your location on the technology wave and
     *programming into a language* rather than in it — the chapter's own
     example is a convention adopted to give a language a separation it
     lacked; §4.4 (p. 69), the major construction practices to select.
   - **Quote:** p. 70, 32 words — “Ask yourself whether the programming
     practices you’re using are a response to the programming language
     you’re using or controlled by it. Remember to program into the language,
     rather than programming in it.”
   - **Do:** convert a size in C statements to another language by the
     table's ratio, and supply by convention a facility a language lacks.
   - **Standard:** given a size in C statements and a ratio, state the
     equivalent statements and what the ratio does not measure; given a
     missing facility, write the convention that supplies it.
   - **Lab:** `project/language`, family 3, one tile. Inputs `size` (C
     statements) and `ratio` (from Table 4-1, *F4*). Presets `java` (10,000;
     2.5 → `pjEquivalent` 4,000), `python` (10,000; 6 → 5000/3 ≈ 1,666.67),
     `visual-basic` (10,000; 4.5 → 20000/9 ≈ 2,222.22). Pins `pjEquivalent`.
     The panel says once that the ratio measures statements, not time,
     defects or the team's experience.
   - **Misconception:** "A practice your language has no keyword for is
     unavailable to you." §4.3 is the refutation: programmers who program
     *into* a language supply what it lacks by convention.
   - **Worked:** 10,000 / 2.5 = 4,000 Java statements for the same function.
   - **Exercise:** three languages, each lacking one facility: no assertion
     statement (Java before 1.4), no enumerated types (Java before 5), no
     access control (a language where every member is public). **Answer:**
     a routine `check(boolean condition, String message)` that throws when the
     condition is false, called where an assertion would be; a class with a
     private constructor and a fixed set of `public static final` instances;
     a naming convention (a leading underscore marks a member nobody outside
     the class may use) enforced by review.
   - **Own:** one facility the reader's own language or framework lacks, and
     the convention their team uses (or should use) to supply it.
   - **Sources:** McConnell §§4.1–4.4; Table 4-1 and its sources (*F4*);
     *F5*.
   - **Body snippet** (new, written for the lesson; no lab figures):
     `SEND_WITH_DEFAULT`, 16 lines: Java has no default arguments, so
     `send(message)` on line 6 forwards `DEFAULT_RETRIES` (line 3) to the
     full `send(message, retries)` on lines 9–16.
   - **Other quotations** (as authored): p. 63, "disguised Fortran", 2
     words. Lesson total 34 words.

### Course 2 — Creating High-Quality Code (`code-complete-high-quality-code`, 9)

Part II, Chapters 5–9. Design, classes, routines, defensive programming and the
pseudocode programming process. Its `how_to` names the course's one idea —
managing complexity is software's primary technical imperative (p. 78) — and
says that every count in the course is a way of seeing complexity. `part_a.py`
is Chapters 5–6 (lessons 1–4), `part_b.py` Chapters 7–9 (lessons 5–9).

1. **design-challenges-and-complexity** — Design Challenges and Complexity — *Chapter 5 · Design in Construction* — 15 min
   - **Read:** pp. 73–86. §5.1 (p. 74), design as a wicked problem (after
     Rittel and Webber 1973, as the book cites them), sloppy, about
     trade-offs and restrictions, non-deterministic, heuristic and emergent;
     §5.2 (p. 77), accidental and essential difficulties (after Brooks 1987),
     managing complexity as the primary technical imperative, the desirable
     characteristics of a design (minimal complexity, loose coupling, high
     fan-in, low-to-medium fan-out, stratification …), and the levels of
     design from system to routine.
   - **Quote:** p. 123, 17 words — “Software’s Primary Technical Imperative
     is managing complexity. This is greatly aided by a design focus on
     simplicity.”
   - **Do:** count the dependencies among a design's parts, the pairs that
     could interact, and the fan-in and fan-out, and say how layering changes
     them.
   - **Standard:** for five or six modules and their dependencies, compute
     the possible pairs, the connected pairs as a share, and the largest
     fan-in.
   - **Lab:** `deps/coupling`, family 2. Presets (illustrative):
     `everything-talks` (each of `ui orders billing stock db` uses every
     other: 20 edges → `dgModules` 5, `dgEdges` 20, `dgPairs` 10,
     `dgConnected` 1 = 100%, `dgFanIn` "billing 4" — all five tie at 4; the
     alphabetical rule picks `billing` and the banner names all five),
     `layered` (`ui, orders; ui, billing; orders, stock; billing, stock;
     orders, db; billing, db; stock, db` → 7, 10, 7/10 = 70%, `dgFanIn` "db
     3"), `strict-layers` (`ui, orders; orders, stock; stock, db; ui,
     billing; billing, db` → 5, 10, 1/2 = 50%, `dgFanIn` "db 2"). Pins
     `dgEdges`, `dgConnected`, `dgFanIn`.
   - **Misconception:** "Design is a phase that ends when coding begins."
     §5.1 refutes it directly: design is sloppy, iterative and emergent, and
     much of it happens during construction. The lab's layering is one
     design decision redrawn three times.
   - **Worked:** five modules give 5·4/2 = 10 pairs; `layered`'s seven
     dependencies touch 7 of them.
   - **Exercise:** six modules `ui api orders billing stock db`, first where
     every pair talks, then layered as `ui, api; api, orders; api, billing;
     orders, stock; billing, stock; stock, db`. **Answer:** all talking:
     6·5/2 = 15 pairs, all 15 connected (30 edges); layered: 6 edges, 6 of
     15 pairs = 2/5 = 40%, largest fan-in `stock` 2.
   - **Own:** the modules of one package of the reader's and who imports
     whom, pasted as `a, b` records.
   - **Sources:** McConnell §§5.1–5.2; Rittel and Webber 1973 and Brooks
     1987, as the book cites them.

2. **design-heuristics-and-information-hiding** — Design Heuristics and Information Hiding — *Chapter 5 · Design in Construction* — 15 min
   - **Read:** pp. 87–123. §5.3 (p. 87), the heuristics: find real-world
     objects, form consistent abstractions, encapsulate implementation
     details, inherit when it simplifies, hide secrets (after Parnas 1972),
     identify areas likely to change, keep coupling loose, look for common
     patterns; §5.4 (p. 110), design practices (iterate, divide and conquer,
     top-down and bottom-up, prototyping, collaborative design, how much
     design is enough, capturing the work); §5.5 (p. 118), comments on
     popular methodologies.
   - **Quote:** p. 123, 17 words — “Information hiding is a particularly
     valuable concept. Asking “What should I hide?” settles many difficult
     design issues.” (The inner quotation marks are the book's; the lesson
     prints them as `&lsquo;…&rsquo;` inside the outer pair.)
   - **Do:** name the secret a design should hide and count the components
     whose code knows it, with the detail exposed and hidden.
   - **Standard:** given a dependency list, name the secret, the modules
     that know it, and the one module that should.
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
     `substring(0, 4)`, `substring(4, 6)` and `substring(6, 8)` on it.
     **Answer:** the secret is the `yyyyMMdd` layout; one routine (a
     `parseDate`) should know it; when the format becomes `yyyy-MM-dd`, 3
     routines change before, 1 after.
   - **Own:** one detail of the reader's code that several modules know (a
     file format, a table's columns, a URL scheme), with the modules that
     know it as `a, b` records.
   - **Sources:** McConnell §§5.3–5.5; Parnas 1972.

3. **abstract-data-types-and-interfaces** — Abstract Data Types and Interfaces — *Chapter 6 · Working Classes* — 15 min
   - **Read:** pp. 125–142. §6.1 (p. 126), the abstract data type and the
     benefits the chapter lists (hide implementation details, limit the
     effect of changes, make the interface more informative, work with
     real-world entities); §6.2 (p. 133), good class interfaces: a
     consistent level of abstraction, and encapsulation — no public data, no
     exposed implementation, no assumptions about the users of the class.
   - **Quote:** p. 160, 15 words — “Class interfaces should provide a
     consistent abstraction. Many problems arise from violating this single
     principle.”
   - **Do:** count a class's fields, its public data and its routines by
     visibility, and group its public routines by the abstraction each
     serves.
   - **Standard:** for a class listing, state the field count, the public
     non-constant fields and the routines a caller can reach, and name the
     abstractions its public routines serve.
   - **Lab:** `code/class`, family 1. Presets (snippets in §D.4):
     `public-fields` (an `Employee` with five public fields, a constructor
     and one method → `coFields` 5, `coPublicFields` 5, `coRoutines` 2,
     `coPublicRoutines` 2), `private-fields` (the same data private, with a
     constructor, two public readers and one private helper, 20 lines → 5,
     0, 4, 3), `kitchen-sink` (the abstract `Kiosk` class, 18 lines → 9, 2,
     6, 6). Pins `coFields`, `coPublicFields`, `coPublicRoutines`.
   - **Misconception:** "A getter and setter for every field is
     encapsulation." The chapter's test is the abstraction the interface
     presents: `kitchen-sink` exposes two fields and six public routines that
     serve three unrelated abstractions — tickets, the weather forecast and
     an audit log — in one class; no accessor discipline fixes that.
     (Corrected at authoring: the book, after Riel, does call a `Point` with
     get and set routines perfect encapsulation of its representation,
     p. 139; the lesson grants that and refutes the misconception as "makes
     a good interface". Because the grouping is exercise (b)'s answer, the
     lesson's `mistakes[0]` does not name the three abstractions.)
   - **Worked:** `public-fields` exposes all five fields: any change to how
     salary is stored reaches every caller.
   - **Exercise:** (a) `public class Point { public double x; public double
     y; private String label; public double distanceTo(Point other) {…} }`;
     (b) `kitchen-sink`'s six public routines. **Answer:** (a) 3 fields, 2
     public; made private, a caller needs `x()` and `y()` (or whatever the
     callers actually do with them); (b) three classes: `issueTicket` and
     `refundTicket`; `fetchForecast` and `showForecast`; `openAuditLog` and
     `closeAuditLog`.
   - **Own:** the reader's largest class pasted into the lab, and its public
     routines grouped by the abstraction each serves.
   - **Sources:** McConnell §§6.1–6.2; the number of data members (*F6*).

4. **inheritance-containment-and-members** — Inheritance, Containment and Members — *Chapter 6 · Working Classes* — 15 min
   - **Read:** pp. 143–160. §6.3 (p. 143), containment ("has a") before
     inheritance ("is a"), the Liskov substitution principle (pp. 144–145,
     Liskov 1988), overridable routines, keeping hierarchies shallow
     (*F7*), member functions and data, constructors; §6.4 (p. 152), reasons
     to create a class (and classes to avoid); §6.5 (p. 156),
     language-specific issues; §6.6 (p. 156), packages.
   - **Quote:** p. 160, 13 words — “Containment is usually preferable to
     inheritance unless you’re modeling an “is a” relationship.” (Inner marks
     as `&lsquo;…&rsquo;`.)
   - **Do:** compute the depth of an inheritance hierarchy and say whether a
     subclass can stand in for its parent, and why.
   - **Standard:** for a hierarchy given as child–parent pairs, state the
     depth and the deepest class; for a stated subclass, say whether it
     substitutes for its parent, naming the caller it would break.
   - **Lab:** `deps/tree`, family 2. Presets: `shallow` (`Circle, Shape;
     Square, Shape; Triangle, Shape` → `dgDepth` 2, `dgClasses` 4,
     `dgLeaves` 3, `dgDeepest` "Circle" — a three-way tie, banner names
     `Circle, Square, Triangle`), `deep` (`Account, Record; DepositAccount,
     Account; SavingsAccount, DepositAccount; BonusSavings, SavingsAccount;
     HolidayBonusSavings, BonusSavings; ChristmasHolidaySavings,
     HolidayBonusSavings; CheckingAccount, DepositAccount` → 7,
     `dgDeepest` ChristmasHolidaySavings, 8 classes, 2 leaves). Pins
     `dgDepth`, `dgDeepest`. The body reads `deep`'s 7 against McConnell's
     own figure (most people manage two or three levels; he calls Riel's six
     "optimistic" in stronger words, p. 147), not against Riel's.
   - **Misconception:** "Inheritance is the main way to reuse code." The
     chapter prefers containment and treats inheritance as a tool with costs;
     the depth tile counts one of them.
   - **Worked:** Record ← Account ← DepositAccount ← SavingsAccount ←
     BonusSavings ← HolidayBonusSavings ← ChristmasHolidaySavings: seven.
   - **Exercise:** (a) `Dog, Mammal; Cat, Mammal; Mammal, Animal; Animal,
     LivingThing; Puppy, Dog`; (b) a `Square` that extends `Rectangle` and
     overrides both `setWidth` and `setHeight` so that each sets both sides.
     **Answer:** (a) depth 5 at `Puppy`; (b) it does not substitute: a caller
     that sets the width to 4, then the height to 5, and expects an area of
     20 gets 25. (A `Square` that overrides only `setWidth` passes this
     caller — the height set last wins — which is why the exercise names
     both.)
   - **Own:** one inheritance chain from the reader's codebase, as
     child–parent pairs, and for its deepest class the one caller of its
     parent it could break.
   - **Sources:** McConnell §§6.3–6.6; Liskov 1988; *F7* (Riel 1996; Basili,
     Briand and Melo 1996, as the book cites them).

5. **reasons-to-create-a-routine** — Reasons to Create a Routine — *Chapter 7 · High-Quality Routines* — 15 min
   - **Read:** pp. 161–172. §7.1 (p. 164), the valid reasons (reduce
     complexity, introduce an intermediate abstraction, avoid duplicate code,
     support subclassing, hide sequences, improve portability, simplify
     tests, and more), and the point that even a two-line routine can be
     worth it; §7.2 (p. 168), cohesion, from functional (the one to aim for)
     through sequential, communicational and temporal to procedural, logical
     and coincidental (after Stevens, Myers and Constantine 1974); §7.3
     (p. 171), good routine names.
   - **Quote:** p. 186, 20 words — “You can classify routines into various
     kinds of cohesion, but you can make most routines functionally cohesive,
     which is best.”
   - **Do:** name a routine's cohesion by the chapter's kinds, and find the
     duplicated lines a routine would remove, with its name and parameters.
   - **Standard:** for six one-line routine descriptions, name each one's
     cohesion and rewrite the weakest as separate routines; in a listing, mark the
     repeated block and write the header of the routine that replaces it.
   - **Lab:** `code/dupes`, family 1 (`cfg["min_run"] = 2`). Presets, in this
     order: `copied` (the label printer reusing one variable `a` → 1 block,
     `coDupLines` 6, `coDupWhere` "lines 3–5 and lines 7–9"), `extracted`
     (the printer calling `printAddress` twice → 0), `two-names` (the label
     printer with `ship` and `bill` variables → `coDupBlocks` 0). Pins
     `coDupBlocks`, `coDupLines`. The body says of `two-names`, in these
     words or near them: "the lab cannot see this copy; you can" — it
     matches text, and a copy with renamed variables is one it cannot see.
   - **Misconception:** "Routines exist to avoid duplication, so code that is
     not repeated needs no routine." The chapter's first reason is reducing
     complexity, and its cohesion scale has nothing to do with repetition.
   - **Worked:** in `copied`, lines 3–5 equal lines 7–9: one block, two
     copies, six lines; `printAddress(Address a)` replaces them.
   - **Exercise:** (a) six routines (replaced at authoring: the first and
     third descriptions were the book's own examples of sequential and
     communicational cohesion, pp. 168–169, and the first had two answers
     depending on whether the age feeds the retirement date; the fourth and
     fifth replaced after the accuracy review, as close to the book's
     temporal and procedural examples, pp. 169–170): "returns the
     sales tax on an amount"; "works out a parcel's volume and then, from that volume,
     its box size, and returns both"; "from an order's list of items, adds up
     the total weight and, separately, counts the distinct suppliers"; "at
     the end of each night, archives the day's orders, empties the shopping
     baskets and rotates the logs"; "prints a shipping label and then writes
     a line to the dispatch log, in the order the warehouse procedure lists
     them, with nothing passed between the two";
     "formats an invoice, a receipt or a refund note, depending on a flag
     passed in". (b) `printSummary` in §D.4.
     **Answer:** (a) functional; sequential; communicational; temporal;
     procedural; logical — the weakest, split into `formatInvoice`,
     `formatReceipt` and `formatRefundNote` with no flag.
     (b) The lab finds 1 block, `coDupLines` 4, "lines 4–5 and lines 8–9";
     `printMoney(String label, double amount)` replaces it, and
     `printSummary` becomes two calls.
   - **Own:** the reader's longest routine, its cohesion named, pasted into
     the lab to look for a repeated block.
   - **Sources:** McConnell §§7.1–7.3; Stevens, Myers and Constantine 1974,
     as the book cites them.

6. **routine-length-and-parameters** — Routine Length and Parameters — *Chapter 7 · High-Quality Routines* — 15 min
   - **Read:** pp. 173–186. §7.4 (p. 173), how long a routine can be, with
     the studies the book reviews (*F8*: allow growth to 100–200 lines,
     counted as non-comment, non-blank lines; care past 200); §7.5 (p. 174),
     parameters: order, using all of them, not using them as working
     variables, limiting their number (*F9*), passing what the routine's
     abstraction needs; §7.6 (p. 181), functions versus procedures — a
     function returns the value its name describes and nothing else; §7.7
     (p. 182), macros and inline routines (named, not taught, §G).
   - **Quote:** p. 186, 23 words — “Functions should be used only when the
     primary purpose of the function is to return the specific value
     described by the function’s name.”
   - **Do:** count a routine's lines and parameters, and regroup parameters
     that travel together into an object.
   - **Standard:** for a routine header and body, state its code lines and
     parameter count, and propose a header with fewer parameters that keeps
     the abstraction.
   - **Lab:** `code/size`, family 1. Presets: `nine-parameters` (an invoice
     line printer whose header spans three lines → `coParams` 9, `coCode` 9,
     `coLines` 10), `parameter-objects` (the same printer taking an
     `InvoiceLine`, a `TaxRule` and a `Format` → 3, 5, 6). Pins `coParams`,
     `coCode`. (Corrected at authoring: `coCode` counts lines that are
     neither blank nor comment, which is exactly the book's line, p. 174,
     braces included; `coStatements` is the count without brace-only lines.
     The body says so.)
   - **Misconception:** "A routine that returns a value can also change
     state on the way; the caller will read the code." §7.6 is firm: a
     function's job is the value its name describes. The short-function
     school — that most routines should be a few lines long, a view later
     than and more demanding than §7.4's — is this course's §F.4 aside, in
     the `note`: the book's figures (*F8*) stated at strength, the later
     view stated fairly, neither settled.
   - **Worked:** nine parameters, seven of which describe the line or its
     tax (`sku`, `description`, `quantity`, `unitPriceCents`,
     `discountPercent`, `taxable`, `taxRatePermille`), become two objects and
     a format.
   - **Exercise:** `void schedule(String name, int year, int month, int day,
     int hour, int minute, int durationMinutes, String room)`. **Answer:** 8
     parameters; the five time fields become one `LocalDateTime` and the
     header has 4.
   - **Own:** the routine in the reader's code with the most parameters,
     pasted into the lab, and the object its travelling-together parameters
     belong in.
   - **Sources:** McConnell §§7.4–7.7; *F8*, *F9*.

7. **assertions-and-error-handling** — Assertions and Error Handling — *Chapter 8 · Defensive Programming* — 15 min
   - **Read:** pp. 187–197. §8.1 (p. 188), protecting the program from
     invalid inputs (check data from external sources, check input
     parameters, decide how to handle bad inputs); §8.2 (p. 189), assertions,
     and the rule that settles most of the chapter: error-handling code for
     conditions you expect to occur, assertions for conditions that should
     never occur (p. 191); §8.3 (p. 194), error-handling techniques (neutral
     value, next valid data, previous answer, closest legal value, logging,
     error codes, a central handler, shutting down) and robustness against
     correctness.
   - **Quote:** p. 213, 19 words — “The decision about how to handle bad
     inputs is a key error-handling decision and a key high-level design
     decision.”
   - **Do:** compare an input check with its specification over every
     integer and say where it is wrong, including the `&&`/`||` confusion
     that makes a check never or always fire.
   - **Standard:** given a valid interval and a check, name the integers the
     check gets wrong, by hand, from its comparisons and its connective.
   - **Lab:** `cond/range`, family 2. Spec: a month is valid from 1 to 12;
     the check flags *invalid* (`cfg["means"] = "invalid"`). Presets:
     `correct` (`month < 1 || month > 12` → `cdDisagree` none, `cdTests` 0,
     1, 2, 11, 12, 13, `cdExposed` none), `never-fires` (`month < 1 && month
     > 12` → `cdDisagree` "0 and below, 13 and above", `cdExposed` 0, 13),
     `always-fires` (`month >= 1 || month <= 12` → "1 to 12", exposed 1, 2,
     11, 12). Pins `cdDisagree`, `cdExposed`.
   - **Misconception:** "An assertion is a way of handling bad input." §8.2:
     input from a user or a file is a condition you expect to occur, and
     gets error handling; an assertion states what can never happen if the
     program is right, and may be compiled out.
   - **Worked:** in `never-fires`, no integer is both below 1 and above 12,
     so the check never flags anything: every invalid month passes.
   - **Exercise:** scores are valid from 0 to 100; the check
     `score >= 0 || score <= 100` means *valid*. **Answer:** every `int`
     satisfies it, so it disagrees on −1 and below and on 101 and above; the
     boundary tests −1 and 101 expose it; the connective should be `&&`.
   - **Own:** one input check from the reader's code, with its documented
     range, typed into the lab.
   - **Sources:** McConnell §§8.1–8.3.

8. **exceptions-and-barricades** — Exceptions and Barricades — *Chapter 8 · Defensive Programming* — 15 min
   - **Read:** pp. 198–213. §8.4 (p. 198), exceptions: use them for what
     should never be ignored, throw at the right level of abstraction, avoid
     empty `catch` blocks, consider the alternatives; §8.5 (p. 203), the
     barricade — classes at the boundary validate and sanitise external
     data, classes inside may assume it clean, and so the boundary decides
     between error handling outside and assertions inside (Figure 8-2,
     p. 204, named and not reproduced; the rule, p. 205); §8.6 (p. 205),
     debugging aids and offensive programming; §8.7–8.8 (pp. 209–210), how
     much defensive code to leave in production, and being defensive about
     defensive programming.
   - **Quote:** p. 205, 24 words — “Routines inside the barricade should use
     assertions, because the data passed to them is supposed to be sanitized
     before it’s passed across the barricade.”
   - **Do:** classify each value in a design by where it comes from, and say
     what the chapter's rule asks of it.
   - **Standard:** for nine values, mark each *validate*, *assert* or
     *neither* by the barricade rule, and give the reason for each.
   - **Lab:** `cond/barricade`, family 2, records `value, side, handling`
     (`side` `outside` or `inside`; `handling` `validate`, `assert` or
     `none`). Presets (illustrative): `mixed` (`quantityField, outside,
     validate; uploadName, outside, none; feedPrice, outside, assert;
     lineTotal, inside, assert; customerId, inside, none; taxDue, inside,
     assert` → `cdValues` 6, `cdOutsideUnchecked` "1: uploadName",
     `cdOutsideAsserted` "1: feedPrice", `cdInsideUnchecked` "1:
     customerId", `cdInsideValidated` "0: none"), `barricaded` (the three
     outside values validated, the three inside asserted → all four tiles
     "0: none"), `checks-everywhere` (all six validated → `cdInsideValidated`
     "3: lineTotal, customerId, taxDue", the rest "0: none"). Pins the four
     tiles. The panel says the counts are the chapter's rule applied to the
     records, not a verdict: §8.8 allows judgement. (`taxDue` was `taxRate`
     until the pedagogy review: the exercise argues that a tax rate read
     from a configuration file is outside, so the preset names a computed
     value.)
   - **Misconception:** "Defensive programming means checking everything
     everywhere." `checks-everywhere` is that program: §8.5 puts the checks at
     the barricade and assertions inside it, and §8.8 warns that too much
     defensive code is itself a source of defects and slowness.
   - **Worked:** in `mixed`, `feedPrice` arrives from a real-time feed —
     outside — and is only asserted, so a bad price stops the program (or,
     with assertions off, passes) instead of being handled.
   - **Exercise:** nine values in an order system: a quantity typed in a
     form; a file name from an upload; a price from a supplier's feed; a line
     total the routine computed itself; an index into the routine's own
     array; a customer id passed from the validated order class; a tax rate
     read from a configuration file; a discount the pricing class computed
     after validation; a date parsed from an e-mail. **Answer:** validate the
     form quantity, the upload name, the feed price, the configuration tax
     rate and the e-mailed date (outside); assert the line total, the array
     index, the customer id and the computed discount (inside). The tax rate
     is the one to argue about: configuration is written by the team, but it
     is read from outside the program, and §8.1 treats a file as an external
     source.
   - **Own:** one boundary in the reader's system (an API handler, a file
     reader), and the values that cross it, as records.
   - **Sources:** McConnell §§8.4–8.8.

9. **the-pseudocode-programming-process** — The Pseudocode Programming Process — *Chapter 9 · The Pseudocode Programming Process* — 15 min
   - **Read:** pp. 215–234. §9.1 (p. 216), the steps in building classes and
     routines; §9.2 (p. 218), pseudocode for professionals (English, at the
     level of intent, not of the language); §9.3 (p. 220), the process:
     design the routine, write pseudocode, turn it into comments, fill in code
     beneath each, check, clean up, repeat; §9.4 (p. 232), alternatives
     (test-first, refactoring, design by contract, hacking).
   - **Quote:** p. 234, 28 words — “The Pseudocode Programming Process is a
     useful tool for detailed design and makes coding easy. Pseudocode
     translates directly into comments, ensuring that the comments are
     accurate and useful.”
   - **Do:** check that every pseudocode comment in a routine has the code
     it promised beneath it, and that the code is right for the language.
   - **Standard:** for a routine written by the process, list its steps,
     find any step with no code, and name the code that is missing.
   - **Lab:** `code/ppp`, family 1. Preset `free-slot` (a routine with five
     pseudocode comments, one of which, "if no slot is free, log the
     overflow", has nothing beneath it → `coSteps` 5, `coCode` 7, `coEmpty`
     "line 14", `coMaxUnder` "3 lines, under line 8"); preset `complete` (the
     same routine with `log.warn("table full");` added under line 14 →
     `coSteps` 5, `coCode` 8, `coEmpty` none). Pins `coSteps`, `coEmpty`.
     The body names a second point in `free-slot`: its last step, "return
     -1", is pseudocode at the level of the language, which §9.2 says to
     avoid.
   - **Misconception:** "Pseudocode is a draft you delete once the code
     works." The process keeps it as the routine's comments, which is why a
     step with no code beneath it is a defect the reader can see.
   - **Worked:** five steps, seven code lines; the step at line 14 is empty.
   - **Exercise:** the `expireSessions` listing in §D.4; find the empty
     step, then say whether the obvious one-line fix is right in Java.
     **Answer:** 4 steps; "remove it from the live list" (line 10) has no
     code, so expired sessions stay live. The obvious fix,
     `sessions.remove(s);` inside the enhanced `for`, throws
     `ConcurrentModificationException` on the next iteration in the standard
     `List`s (and, when it removes the second-to-last element of an
     `ArrayList`, silently skips the last instead); the step needs an
     explicit `Iterator` and `it.remove()`
     (or a loop over a copy). Writing the pseudocode first is what lets the
     reader see the step needs a different loop.
   - **Own:** a routine the reader is about to write, as five pseudocode
     comments first, pasted into the lab once the code is under them.
   - **Sources:** McConnell §§9.1–9.4.

### Course 3 — Variables (`code-complete-variables`, 6)

Part III, Chapters 10–13. Declaring, initialising, scoping and naming
variables, and the data types. Its `how_to` says that four of the six labs
read code (`run/arith` and `deps/shared` do not; corrected at authoring), and
that the reader should paste a routine of their own into each code lab.

1. **declaring-and-initializing-variables** — Declaring and Initializing Variables — *Chapter 10 · Using Variables* — 15 min
   - **Read:** pp. 237–244 (§10.3's last guideline, on input parameters, is
     on p. 244). §10.1 (p. 238), data literacy; §10.2 (p. 239),
     making declarations easy and the danger of implicit declarations; §10.3
     (p. 240), guidelines for initialising: initialise each variable as it is
     declared, or close to where it is first used, use `final` where
     possible, reset counters and accumulators, check input parameters. The
     data-flow anomalies the lab reports are named in §22.3 (p. 509) and the
     body says so.
   - **Quote:** p. 258, 24 words — “Data initialization is prone to errors,
     so use the initialization techniques described in this chapter to avoid
     the problems caused by unexpected initial values.”
   - **Do:** find each variable read before it is set, set twice with no use
     between, or set and never used, reading the listing top to bottom, and
     say which of them Java's compiler catches.
   - **Standard:** for a short routine, list every such anomaly with its line,
     and say which `javac` rejects.
   - **Lab:** `code/dataflow`, family 1. Presets: `count-unset` (an average
     routine declaring `int count;` and incrementing it → `coAnomalies` 1,
     `coUsedBeforeSet` "count (line 6)"; `javac` rejects it), `initialized`
     (the same routine with `int count = 0;` beside `total` → 0), `set-twice`
     (`total` and `count` initialised then overwritten, and an `average`
     computed and not used → 3: `coSetTwice` "total (lines 2, 4), count
     (lines 3, 5)", `coUnused` "average (line 6)"; `javac` accepts it). Pins
     `coAnomalies`, `coUsedBeforeSet`, `coSetTwice`.
   - **Misconception:** "If it compiles, every variable holds the value you
     meant." `set-twice` compiles and throws two initial values away; and a
     field (`int count;` in a class) defaults silently to 0, which `javac`
     never questions. What Java's compiler does catch — a local read before
     it is definitely assigned, on any path — is real, and the body says so:
     it is stronger than this lab on locals.
   - **Worked:** in `count-unset`, line 6 reads `count` in `count = count +
     1` and nothing before it set `count`.
   - **Exercise:** `String result; if (first.length() > 0) { result =
     first.substring(0, 1); } result = result + last.substring(0, 1);`.
     **Answer:** the lab reports nothing, because it reads lines in order and
     line 4 sets `result` before line 6 reads it; on the path where the `if`
     is false, line 6 reads an unset variable. `javac` rejects the routine
     ("variable result might not have been initialized"); a C or C++
     compiler accepts its equivalent. The lab reads top to bottom; the `note`
     names that limit without naming the exercise.
   - **Own:** a routine of the reader's pasted into the lab, and each
     anomaly it reports checked against what the compiler said.
   - **Sources:** McConnell §§10.1–10.3, and §22.3 for the anomaly names.

2. **scope-span-and-live-time** — Scope, Span and Live Time — *Chapter 10 · Using Variables* — 15 min
   - **Read:** pp. 244–258. §10.4 (p. 244), scope: localise references
     (span), keep variables live for as short a time as possible (live time),
     the measures and the book's worked examples (pp. 245–248; its example
     averages 54 lines of live time against 7 after the rewrite, *F10*);
     §10.5 (p. 251), persistence; §10.6 (p. 252), binding time; §10.7
     (p. 254), data types and control structures; §10.8 (p. 255), one
     purpose per variable.
   - **Quote:** p. 258, 24 words — “Minimize the scope of each variable.
     Keep references to a variable close together. Keep it local to a
     routine or class. Avoid global data.”
     Also quoted in the lesson: “window of vulnerability” (p. 245, 3 words)
     and “moonlighting as a boolean” (p. 257, 4 words); lesson total 31.
   - **Do:** compute each variable's spans and live time and the averages,
     and move declarations to shrink them.
   - **Standard:** given the lines on which two variables are referenced,
     compute every span, the average span and each live time.
   - **Lab:** `code/span`, family 1, `vars` = `scanned heaviestKg
     overLimit`, the `auditShipments` routine (§D.4). Presets:
     `declared-at-top` (all three declared on lines 2–4 → `scanned` lines 2,
     9, 11, spans 6, 1, live 10; `heaviestKg` 3, 13, 18, spans 9, 4, live 16;
     `overLimit` 4, 15, 18, spans 10, 2, live 15; `coAvgSpan` 16/3 ≈ 5.33,
     `coAvgLive` 41/3 ≈ 13.67, `coLongest` "heaviestKg: 16"),
     `declared-near-use` (each declared just before its loop → `scanned` 4,
     7, 9; `heaviestKg` 10, 13, 18; `overLimit` 11, 15, 18; `coAvgSpan` 7/3 ≈
     2.33, `coAvgLive` 23/3 ≈ 7.67, `coLongest` "heaviestKg: 9"). Pins
     `coAvgSpan`, `coAvgLive`. The body says two things about the
     measures: the book counts statements and the lab counts listing lines;
     and the lab's pooled average span over several variables is its own
     extension of the book's per-variable average.
   - **Misconception:** "Declaring every variable at the top makes them easy
     to find." The chapter's measure says what it costs; on the lesson's
     illustration, an average live time of 41/3 ≈ 13.7 lines against 23/3 ≈
     7.7 for the same statements.
   - **Worked:** `heaviestKg` on lines 3, 13 and 18: spans 9 and 4; live time
     18 − 3 + 1 = 16.
   - **Exercise:** in another routine, `total` is referenced on lines 2, 9,
     12 and `count` on 3, 10, 12; then both declarations move below four
     `print…` calls on lines 2–5, to lines 6 and 7. **Answer:** before: spans
     6, 2 and 6, 1, average 15/4 = 3.75, live times 11 and 10; after: `total`
     on 6, 9, 12 and `count` on 7, 10, 12, spans 2, 2 and 2, 1, average 7/4 =
     1.75, live times 7 and 6. (As authored: `reportSales`, 13 lines; the
     lab with `vars` `total count` prints `coAvgSpan` 15/4 = 3.75 and
     `coAvgLive` 21/2 = 10.50 before, 7/4 = 1.75 and 13/2 = 6.50 after.)
   - **Own:** a routine of the reader's pasted into the lab with `vars`
     empty, and the variable with the longest live time moved.
   - **Sources:** McConnell §§10.4–10.8; *F10*.

3. **the-power-of-variable-names** — The Power of Variable Names — *Chapter 11 · Variable Names* — 15 min
   - **Read:** pp. 259–289. §11.1 (p. 259), choosing a good name (the
     problem, not the solution; optimum length, *F11*; scope and name length;
     computed-value qualifiers; common opposites); §11.2 (p. 264), naming
     specific types (loop indexes, status variables, temporaries, booleans,
     enums, constants); §11.3–11.4 (pp. 270–272), the power of naming
     conventions and informal conventions; §11.5 (p. 279), standardized
     prefixes; §11.6 (p. 282), creating short names that are readable; §11.7
     (p. 285), kinds of names to avoid.
   - **Quote:** p. 289, 23 words — “Code is read far more times than it is
     written. Be sure that the names you choose favor read-time convenience
     over write-time convenience.”
   - **Do:** compute the average length of a routine's names, leaving out
     loop indexes, and rename the short ones for the problem they describe.
   - **Standard:** for a routine, list its declared names with lengths,
     compute the average without loop indexes, and propose names for those
     under eight characters.
   - **Lab:** `code/names`, family 1, `cfg["min"] = 8` (the lesson's
     threshold, after the study the book cites, *F11*). Presets:
     `short-names` (`calc(double[] a, int n, double r)` with `t`, `x`, `tmp`
     → `coNames` 7, `coAvgLen` 4/3 ≈ 1.33, `coShort` "a, n, r, t, x, tmp";
     loop index `i` not counted), `problem-names` (`averageNetPrice(double[]
     grossPrices, int priceCount, double netFactor)` with `netTotal`,
     `netPrice`, `averageNet` → 7, 28/3 ≈ 9.33, none). Pins `coAvgLen`,
     `coShort`. The body says the study's figure is an average over a
     program, and the per-name `coShort` list is the lab's reading of it.
   - **Misconception:** "Longer names are always better." The study the book
     reports found a range, not a direction (*F11*), and the chapter keeps
     short names for loop indexes. The modern aside of this course lives
     here (prefix conventions and today's editors, §F.4), in the `note`.
   - **Worked:** 11 + 10 + 9 + 8 + 8 + 10 = 56 characters over 6 names: 28/3
     ≈ 9.33.
   - **Exercise:** `double f(double p, int n, double r)` with `m` and `t`.
     **Answer:** average 1; renamed `totalInterest(double principal, int
     months, double annualRate)` with `monthlyInterest`, `totalInterest` →
     53/5 = 10.6, and only `months` is under eight. (As authored: the routine
     is `simpleInterest`, so that no local shares the routine's name; the
     lab counts neither, so the figures are unchanged, checked in the lab:
     `coAvgLen` 1, then `53/5 = 10.60`, `coShort` "months".)
   - **Own:** a routine of the reader's pasted into the lab, its short names
     renamed for the problem.
   - **Sources:** McConnell §§11.1–11.7; *F11*.

4. **integers-and-floating-point** — Integers and Floating Point — *Chapter 12 · Fundamental Data Types* — 15 min
   - **Read:** pp. 291–296. §12.1 (p. 292), numbers in general (avoid magic
     numbers, with the rule of thumb that the only literals in a program's
     body should be 0 and 1, *F12*; anticipate divide-by-zero; make
     conversions obvious; avoid mixed-type comparisons); §12.2 (p. 293),
     integers (integer division, overflow, overflow in intermediate
     results); §12.3 (p. 295), floating point (adding numbers of very
     different size, equality comparisons — the book's own example is 0.1
     added ten times — rounding, decimal types).
   - **Quote:** p. 295, 29 words — “Floating-point numbers that should be
     equal are not always equal. The main problem is that two different
     paths to the same number don’t always lead to the same number.” (A
     margin epigraph sits beside it on the page; the quotation is the body
     text only.)
   - **Do:** compute what Java's `int`, `long` and `double` give for an
     operation repeated, against the exact result, and say why they differ.
   - **Standard:** for an `int` product or sum, say whether it overflows and
     in which direction, and name the fix (`long`, or a `long` literal); for
     a decimal fraction added ten times as `double`, say whether the result
     equals the exact one and why.
   - **Lab:** `run/arith`, family 2. Presets: `int-max-plus-one` (`int`,
     2147483647 + 1, once → `nuJava` `-2147483648`, `nuExact` 2,147,483,648,
     `nuEqual` no), `square-overflow` (`int`, 46341 × 46341 → `-2147479015`
     against 2,147,488,281), `long-square` (the same in `long` →
     `2147488281`, yes), `int-division` (`int`, 7 / 2 → `3` against
     `nuExact` "7/2 = 3.50"), `tenth-ten-times` (`double`, 0 + 0.1, ten times
     → `nuJava` `0.9999999999999999`, `nuExact` 1, `nuEqual` no, `nuStored`
     9007199254740991/9007199254740992 — the book's own example, p. 295),
     `cents` (`int`, 0 + 10, ten times → `100`, yes). Pins `nuJava`,
     `nuEqual`. `nuJava` prints as Java prints, ASCII minus and no grouping.
   - **Misconception:** "A `double` holds 0.1." It holds the nearest binary
     fraction, and the lab prints it exactly; ten of them make
     0.9999999999999999. Counting money in whole cents (`cents`) is the
     chapter's remedy.
   - **Worked:** 46341² = 2,147,488,281, which is 2³¹ + 4,633; the `int`
     wraps to −2,147,479,015.
   - **Exercise:** `int total = 0;` and then `total += 3000000;` a thousand
     times (start 0, `+`, 3000000, 1,000 times in the lab). **Answer:** the
     exact value 3,000,000,000 exceeds `Integer.MAX_VALUE`; Java prints
     `-1294967296`; declared `long`, it prints `3000000000`. The body adds a
     second case in prose, `int msPerYear = 365 * 24 * 60 * 60 * 1000;`,
     which prints `1471228928` against 31,536,000,000 and is fixed by
     writing `1000L`.
   - **Own:** one counter or product in the reader's code, its largest
     plausible value, and whether its type holds it.
   - **Sources:** McConnell §§12.1–12.3; *F12*.

5. **named-constants-and-other-types** — Named Constants and Other Types — *Chapter 12 · Fundamental Data Types* — 15 min
   - **Read:** pp. 297–318. §12.4 (p. 297), characters and strings (magic
     characters and strings); §12.5 (p. 301), boolean variables used to
     document a test; §12.6 (p. 303), enumerated types; §12.7 (p. 307), named
     constants — use them in declarations, avoid literals "even safe ones",
     use them consistently (pp. 308–309), and the rule of §12.1 (*F12*);
     §12.8 (p. 310), arrays; §12.9 (p. 311), creating your own types.
   - **Quote:** p. 309, 22 words — “Even if you think a literal is safe, use
     named constants instead. Be a fanatic about rooting out literals in your
     code.”
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
   - **Misconception:** "A literal used only once is harmless." The
     chapter's reasons are readability and a single point of change, and it
     asks for constants even for "safe" literals; `12` appearing twice with
     one meaning is the case the lab catches, and a single `0.0725` still
     does not say it is an annual rate.
   - **Worked:** `0.0725 / 12` becomes `ANNUAL_RATE / MONTHS_PER_YEAR`.
   - **Exercise:** a monitoring loop with `38.5`, `3` and `900`. **Answer:**
     3 magic numbers, 3 distinct (`FEVER_CELSIUS`, `URGENT_PRIORITY`,
     `CHECK_INTERVAL_SECONDS`). (As authored: `watchWard`, 10 lines, the
     literals on lines 4, 5 and 8; the lab prints `coMagicList` "38.5
     (line 4), 3 (line 5), 900 (line 8)".)
   - **Own:** a routine of the reader's pasted into the lab, and a constant
     declared for each literal it lists.
   - **Sources:** McConnell §§12.4–12.9; *F12*.

6. **structures-pointers-and-global-data** — Structures, Pointers and Global Data — *Chapter 13 · Unusual Data Types* — 15 min
   - **Read:** pp. 319–344. §13.1 (p. 319), structures; §13.2 (p. 323),
     pointers (where errors come from, general tips; the C++ and C detail is
     named, not taught — §G); §13.3 (p. 335), global data: its problems,
     reasons to use it, and access routines — each global given one owner,
     a single point of change and a place to check its value (Table 13-1 is
     named, not reproduced).
   - **Quote:** p. 344, 24 words — “If you can’t avoid global variables, work
     with them through access routines. Access routines give you everything
     that global variables give you, and more.”
   - **Do:** count the routines coupled to one another through global
     variables, and the places that touch each global's representation,
     with and without access routines.
   - **Standard:** for a table of routines and the globals each reads and
     writes, count the coupled pairs (two routines that share a global one
     of them writes) and say what access routines change and what they do
     not.
   - **Lab:** `deps/shared`, family 2, records `routine, access, global` with
     access `r`, `w` or `rw`, and an optional `owners` input (`global =
     access routine`). The records are the same in both presets:
     `readInput, w, current; validate, r, current; validate, w, errors;
     report, r, errors; report, r, current; reset, w, errors; reset, w,
     current; addLine, r, current; addLine, rw, total; printTotals, r,
     total`. Presets: `globals` (no owners → `dgGlobals` 3, `dgRoutines` 6,
     `dgCoupled` 9 of 15 pairs, `dgMostShared` "current, 5 routines",
     `dgDirectAccess` 10, `dgWriters` "current: readInput, reset; errors:
     reset, validate; total: addLine"), `access-routines` (owners `current =
     currentRecord; errors = errorLog; total = runningTotal` → `dgCoupled`
     still 9, `dgDirectAccess` 3, `dgWriters` "current: currentRecord;
     errors: errorLog; total: runningTotal"). Pins `dgCoupled`,
     `dgDirectAccess`.
   - **Misconception:** "Global data is fine as long as it is only read." A
     reader is coupled to every writer, and `globals` has two writers of
     `current`. **Also:** "Access routines remove the coupling." They do not:
     `dgCoupled` stays 9, because the six routines still share the data;
     what changes is that each global's representation is touched in one
     place instead of ten, which is what §13.3 claims for them.
   - **Worked:** `current` has writers `readInput` and `reset` and readers
     `validate`, `report`, `addLine`: 7 coupled pairs; `errors` adds
     `validate`–`report`; `total` adds `addLine`–`printTotals`: 9.
   - **Exercise:** `load, w, config; render, r, config; save, r, config;
     render, w, cache; save, r, cache`. **Answer:** 2 globals, 3 routines,
     all 3 pairs coupled; 5 places touch the globals directly, 2 with an
     access routine for each.
   - **Own:** one global (or singleton, or static field) in the reader's
     code and every routine that reads or writes it, as records.
   - **Sources:** McConnell §§13.1–13.3.

### Course 4 — Statements (`code-complete-statements`, 7)

Part IV, Chapters 14–19. Straight-line code, conditionals, loops, unusual
control structures, tables and the general issues of control. Its `how_to` says
the course's last lesson, Nesting and Complexity, gathers the counts of the
others into one. `part_a.py` is Chapters 14–17, `part_b.py` 18–19.

1. **organizing-straight-line-code** — Organizing Straight-Line Code — *Chapter 14 · Straight-Line Code* — 12 min
   - **Read:** pp. 347–353. §14.1 (p. 347), statements that must be in a
     specific order: make the dependencies obvious through names,
     parameters and comments; §14.2 (p. 351), statements whose order does not
     matter: read top to bottom, group related statements.
   - **Quote:** p. 353, 10 words — “The strongest principle for organizing
     straight-line code is ordering dependencies.”
   - **Do:** list the order dependencies between statements (which line reads
     what another line wrote), and find the statement that reads a value
     before it is computed.
   - **Standard:** for six statements, list each dependency as *i → j* and
     reorder them so that none points backwards.
   - **Lab:** `code/dataflow`, family 1 (the `coDeps` tile). Presets, on a
     parcel quote (§D.4): `total-first` (`total` summed on line 2 from
     `base`, `surcharge` and `insurance`, which lines 3–5 then compute →
     `coAnomalies` 6, `coUsedBeforeSet` "base (line 2), surcharge (line 2),
     insurance (line 2)", `coDeps` "1→3, 1→4, 1→5, 2→6"), `in-order` (the
     same statements reordered → 0, `coDeps` "1→2, 1→3, 1→4, 2→5, 3→5, 4→5,
     5→6"), `hidden` (`quote.loadRates(); quote.addSurcharges();
     quote.addInsurance(); quote.print();` → 0, `coDeps` "1→2, 1→3, 1→4,
     1→5"). Pins `coAnomalies`, `coDeps`.
   - **Misconception:** "If the code compiles, its order is right." `javac`
     rejects `total-first` ("cannot find symbol") because the dependency is
     visible; `hidden` compiles in any order, and the lab sees no dependency
     between its calls, because they pass nothing.
   - **Worked:** in `in-order`, line 5 reads what lines 2, 3 and 4 wrote.
   - **Exercise:** rewrite `hidden` so each call takes the result of the
     previous one (§D.4, `printQuote` with parameters). **Answer:** `coDeps`
     "1→2, 1→3, 1→4, 1→5, 2→3, 3→4, 4→5": the chain 2→3→4→5 is the order,
     now in the parameters, which is §14.1's remedy and why the lab can see
     it.
   - **Own:** a routine of the reader's with calls that must happen in
     order, pasted into the lab, and the dependency it does not show.
   - **Sources:** McConnell §§14.1–14.2.

2. **using-conditionals** — Using Conditionals — *Chapter 15 · Conditionals* — 12 min
   - **Read:** pp. 355–366. §15.1 (p. 355), `if` statements: the nominal path
     first, the normal case after the `if`, the `else` considered, chains of
     `if-then-else` tests in order of frequency, all cases covered, the last
     `else` catching errors; §15.2 (p. 361), `case` statements: ordering
     cases, tips (simple actions, the default for errors, fall-through in
     C-family languages).
   - **Quote:** p. 366, 21 words — “To trap errors, use the default clause in
     a case statement or the last else in a chain of if-then-else
     statements.”
   - **Do:** compute the average number of tests an `if-else-if` chain makes
     from the frequencies of its cases, reorder it, and find the input a
     chain without a final `else` lets through.
   - **Standard:** given a chain's cases in order with frequencies, compute
     the expected tests, and the expected tests with the cases in order of
     frequency; for a chain, name an input no branch catches.
   - **Lab:** `search/chain`, family 2, records `case, frequency` in chain
     order; a final `else` costs as many tests as there are conditions.
     Presets (illustrative frequencies for classifying HTTP responses):
     `as-written` (`server error, 5; client error, 10; redirect, 15;
     success, 70` → `seExpected` 7/2 = 3.50, `seBest` 3/2 = 1.50, `seSaved`
     2), `common-first` (`success, 70; redirect, 15; client error, 10; else,
     5` → 29/20 = 1.45, 29/20 = 1.45, 0), `else-is-common` (`server error,
     5; client error, 10; redirect, 15; else, 70` → 14/5 = 2.80, 13/5 = 2.60,
     1/5 = 0.20). Pins `seExpected`, `seBest`.
   - **Misconception:** "The order of mutually exclusive tests does not
     matter." It does not matter to the result; it matters to the cost, and
     to the reader, and the chapter weighs both.
   - **Worked:** (1·5 + 2·10 + 3·15 + 4·70)/100 = 3.5 tests; success first,
     1.5.
   - **Exercise:** (a) a request router testing `DELETE` (5%), `POST`
     (15%), `GET` (80%) in that order; (b) a chain `if GET … else if POST …
     else if PUT … else if DELETE …` with no final `else`. **Answer:**
     (a) 11/4 = 2.75 tests on average; reversed, 5/4 = 1.25; (b) any other
     method (`PATCH`, `HEAD`, a misspelling) falls through silently; a final
     `else` that rejects it is §15.1's error trap.
   - **Own:** an `if-else-if` chain from the reader's code, with
     frequencies from a log or a guess (and the sentence that says which),
     typed into the lab.
   - **Sources:** McConnell §§15.1–15.2.
   - **Recorded at second review:** a second quotation, p. 365, 19 words (the Pontiac Aztek line on fall-through; lesson total 40). New snippets: `classify` (12 lines; the HTTP classifier the `chain` presets price) and `route` (11 lines; the exercise's chain with no final `else`).

3. **controlling-loops** — Controlling Loops — *Chapter 16 · Loops* — 15 min
   - **Read:** pp. 367–389. §16.1 (p. 367), selecting the kind of loop;
     §16.2 (p. 373), controlling it: entering, the body, exit, endpoints
     (off-by-one errors), loop variables — including the advice not to write
     code that depends on the index's value after the loop (p. 377) — and
     length and nesting (*F13*); §16.3 (p. 385), creating a loop from the
     inside out; §16.4 (p. 387), the correspondence between loops and arrays.
   - **Quote:** p. 389, 20 words — “Think through the loop carefully to
     verify that it operates normally under each case and terminates under
     all possible conditions.”
   - **Do:** compute how many times a loop runs, the last value its index
     takes in the body and the value it would hold after the loop, from the
     header alone.
   - **Standard:** for four headers, state iterations, last value and value
     after, and say which never ends.
   - **Lab:** `run/loop`, family 2, inputs `start`, `cmp` (`lt le ne gt ge`,
     printed as the operator), `bound`, `step`. Presets: `fencepost` (0, le,
     10, 1 → `lpIterations` 11, `lpLast` 10, `lpAfter` 11), `half-open` (0,
     lt, 10, 1 → 10, 9, 10), `counting-down` (10, ge, 0, −1 → 11, 0, −1),
     `skips-the-bound` (0, ne, 9, 2 → `lpIterations` "never ends": every
     value of `i` is even, wrap-around included). Pins all three tiles
     (`lpIterations` only on `skips-the-bound`). The panel says that in Java
     an index declared in the `for` header does not exist after the loop;
     `lpAfter` is the value it would hold if declared before it, which the
     book advises against relying on (p. 377).
   - **Misconception:** "`<=` and `<` differ by one only at the end." They
     differ in the count, the last value and the value after, and `!=` with a
     step that jumps the bound never stops. **Also:** "after the loop, `i` is
     the last value it had in the body" — `lpAfter` is one step past it.
   - **Worked:** `for (int i = 0; i <= 10; i++)` runs 11 times; an `i`
     declared before the loop is 11 after it.
   - **Exercise:** `for (int i = 10; i > 0; i -= 3)`. **Answer:** 4
     iterations (10, 7, 4, 1); last value 1; −2 after.
   - **Own:** four loop headers from the reader's code, typed into the lab.
   - **Sources:** McConnell §§16.1–16.4; *F13*.
   - **Recorded at second review:** new snippets `hourly` (4 lines; `fencepost`'s header, `hourly[10]` throws) and the exercise's `for (int i = 10; i > 0; i -= 3)` (3 lines).

4. **unusual-control-structures** — Unusual Control Structures — *Chapter 17 · Unusual Control Structures* — 15 min
   - **Read:** pp. 391–410. §17.1 (p. 391), multiple returns from a routine,
     and guard clauses — early returns that take the error cases out of the
     way of the nominal path; §17.2 (p. 393), recursion: tips, and the book's
     warning not to use it for factorials or Fibonacci numbers (p. 397);
     §17.3 (p. 398), `goto`: the arguments for and against, with the
     history; §17.4 (p. 408), perspective.
   - **Quote:** p. 410, 22 words — “Multiple returns can enhance a routine’s
     readability and maintainability, and they help prevent deeply nested
     logic. They should, nevertheless, be used carefully.”
   - **Do:** rewrite nested conditions as guard clauses; compute the calls,
     depth and loop iterations of a recursive routine against its iterative
     version.
   - **Standard:** for a routine with two nested `if`s and a single return,
     write the guard-clause version and say what changes in its nesting and
     what does not in its decision points; for naive recursive Fibonacci at
     n, state the calls (2·F(n + 1) − 1) and the loop's iterations.
   - **Lab:** `run/recursion`, family 2, `fn` `factorial` (n ≤ 20, so the
     value fits a Java `long`) or `fibonacci` (n ≤ 90). Presets:
     `factorial-10` (→ `lpCalls` 10, `lpDepth` 10, `lpValue` 3,628,800,
     `lpLoop` 9), `fibonacci-30` (→ 2,692,537, 30, 832,040, 29),
     `fibonacci-40` (→ 331,160,281, 40, 102,334,155, 39). Pins `lpCalls`,
     `lpLoop`.
   - **Misconception:** "Recursion is the natural way to compute Fibonacci
     numbers." The definition is recursive; the computation need not be, and
     the book says not to. The history aside (Dijkstra's 1968 letter, Knuth's
     1974 reply, and languages since that have no `goto`) is this course's
     §F.4 aside, in a late `p`.
   - **Worked:** F(31) = 1,346,269, so `fibonacci(30)` makes 2·1,346,269 − 1 =
     2,692,537 calls; the loop makes 29 additions.
   - **Exercise:** the `refundAmount` routine in §D.4 (nested). **Answer:**
     the guard-clause version returns `0.0` early when the order is not paid
     and when more than 30 days have passed, then returns `order.total()`;
     the lab's `code/complexity` view (or a count by hand) gives 3 decision
     points before and after, and depth 2 before, 1 after — which Nesting
     and Complexity counts again on a larger routine.
   - **Own:** one routine of the reader's with an `if` nested inside
     another, rewritten with guard clauses.
   - **Added at authoring** (pedagogy review of Course 4, finding 1): a
     demonstration snippet `firstLine(File)` with two guard clauses, shown
     before the exercise; `code/complexity` gives 3 decision points
     (1 + if 2), depth 1. Not a preset.
   - **Sources:** McConnell §§17.1–17.4; Dijkstra 1968; Knuth 1974.
   - **Recorded at second review:** new snippets, recursive `fibonacci` (6 lines) and its loop (13 lines; i from 2 to n, n − 1 passes), the two the `recursion` presets model.

5. **table-driven-methods** — Table-Driven Methods — *Chapter 18 · Table-Driven Methods* — 15 min
   - **Read:** pp. 411–430. §18.1 (p. 411), general considerations (how to
     look an entry up, what to store); §18.2 (p. 413), direct access; §18.3
     (p. 425), indexed access; §18.4 (p. 426), stair-step access, with its
     care over endpoints and the choice of linear or binary search; §18.5
     (p. 429), other examples.
   - **Quote:** p. 430, 27 words — “One key consideration in using a table is
     deciding how to access the table. You can access tables by using direct
     access, indexed access, or stair-step access.”
   - **Do:** look a key up in a stair-step table and count the comparisons
     a linear scan and a binary search make.
   - **Standard:** for a five-step table and a key, state the value and
     both comparison counts, and say which endpoint rule the table uses.
   - **Lab:** `search/stairs`, family 2, records `upper bound, value` and a
     `rule` (`below`: the key is in the first step whose bound it is below;
     `atmost`: at or below). Instance (a library's late fee by days
     overdue): `7, 0; 14, 2; 30, 5; 60, 10; 365, 20`. Presets: `days-20`
     (below → `seValue` 5, `seLinear` 3, `seBinary` 2), `days-60-below` (→
     20, 5, 3), `days-60-atmost` (→ 10, 4, 3), and `brackets` (sixteen tax
     brackets `1000, 0%; 2000, 5%; … 16000, 75%` in steps of 1,000 and 5%,
     key 14,500 → 70%, 15, 4). Pins `seValue`, `seLinear`, `seBinary`.
   - **Misconception:** "A table is just a faster `if` chain." The chapter's
     case is that a table moves the logic into data, and the two `days-60`
     presets show where the remaining logic sits: in the endpoint rule.
   - **Worked:** 20 is not below 7 or 14 and is below 30: fee 5, after 3
     comparisons; binary search tests 30, then 14: 2.
   - **Exercise:** shipping rates `1, 5; 5, 9; 20, 15; 70, 40` (kilograms,
     price), a 5 kg parcel. **Answer:** with `below` it costs 15 (3
     comparisons linear, 2 binary); with `atmost`, 9 (2 linear, 3 binary).
     Which the business means is a question for the business, and the table
     must say.
   - **Own:** one lookup in the reader's code written as a chain of `if`s,
     and the table that would replace it, with its endpoint rule stated.
   - **Sources:** McConnell §§18.1–18.5.
   - **Recorded at second review:** new snippets, `lateFee` (11 lines, the instance as two arrays and a `<` loop; above 365 it returns the top fee, where the lab says "above the table") and the exercise's two arrays (3 lines). The lab's binary search counts n + 1 places (the steps and "above the table"): `brackets` keys below 2,000 take 5 probes, the rest 4.

6. **boolean-expressions** — Boolean Expressions — *Chapter 19 · General Control Issues* — 15 min
   - **Read:** pp. 431–445 (§19.3 runs onto p. 445, where §19.4 begins; corrected at authoring). §19.1 (p. 431), boolean expressions: `true` and
     `false` rather than 1 and 0, simplifying with well-named boolean
     variables or functions, forming them positively, DeMorgan's theorems
     (Table 19-1, named), parentheses, short-circuit evaluation, number-line
     order, comparisons to 0; §19.2 (p. 443), compound statements; §19.3
     (p. 444), null statements.
   - **Quote:** p. 460, 14 words — “Making boolean expressions simple and
     readable contributes substantially to the quality of your code.”
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
   - **Exercise:** simplify `!(isAdmin || !isOwner)`. **Answer:** `!isAdmin
     && isOwner`; the lab confirms equivalence on all 4 rows.
   - **Own:** one negated compound condition from the reader's code,
     rewritten positively and checked in the lab.
   - **Sources:** McConnell §§19.1–19.3.
   - **Recorded at second review:** new snippets `drain` (11 lines; the guard on line 4 and the test on line 7 are `demorgan`'s A and B) and the exercise's three-line `if`.

7. **nesting-and-complexity** — Nesting and Complexity — *Chapter 19 · General Control Issues* — 15 min
   - **Read:** pp. 445–460. §19.4 (p. 445), taming deep nesting (*F15*;
     retest part of the condition, break out early, convert to `if-else-if`
     or `case`, factor into routines, use polymorphism); §19.5 (p. 454),
     structured programming (sequence, selection, iteration; Böhm and
     Jacopini 1966); §19.6 (p. 456), control structures and complexity: the
     decision-point count after McCabe 1976 (Table 19-2, p. 458, *F14*), the
     book's bands for reading it, and its remark that moving part of a
     routine into another does not reduce the program's overall complexity
     (p. 458).
   - **Quote:** p. 460, 15 words — “Deep nesting makes a routine hard to
     understand. Fortunately, you can avoid it relatively easily.”
   - **Do:** count a routine's decision points by the chapter's rule and its
     nesting depth, and flatten it with guard clauses.
   - **Standard:** for a 15-to-22-line routine, state the decision points
     with their breakdown and the deepest nesting, by hand, by the rule as
     the lesson states it.
   - **Lab:** `code/complexity`, family 1. Presets: `nested-shipping` (a
     shipping-cost routine nested five deep → `coDecisions` 9,
     `coBreakdown` "1 + if 5 + for 1 + && 1 + || 1", `coBand` "6–10",
     `coDepth` 5, `coDeepest` line 14), `guard-clauses` (the same rules as
     guard clauses, the international branch moved into a routine of its own
     → 6, "1 + if 3 + && 1 + || 1", "6–10", 1). Pins `coDecisions`,
     `coDepth`. `nested-shipping`'s `return -1.0;` is an error sentinel, a
     technique Chapter 8 lists with its costs; the body says so in a clause.
   - **Misconception:** "Flattening the code reduces its complexity." It
     reduces the nesting a reader holds at once (5 to 1); the decision points
     fall from 9 to 6 only because three moved into `internationalCost`,
     where they are still to be read — which is the book's own point
     (p. 458). **Also:** "A count of 11 means the routine is bad." The band
     is the book's guidance for where to look (*F14*), and the material
     clause says so.
   - **Worked:** 1 + five `if`s + one `for` + one `&&` + one `||` = 9.
   - **Exercise:** the `discountPercent` routine in §D.4. **Answer:** 7
     decision points (1 + if 3 + for 1 + && 1 + || 1), depth 2.
   - **Own:** the reader's most-nested routine pasted into the lab.
   - **Sources:** McConnell §§19.4–19.6; McCabe 1976; Böhm and Jacopini 1966;
     *F14*, *F15*.
   - **Recorded at second review:** two phrases quoted besides the opening, "structured goofing off" (p. 454, 3 words) and "or their equivalents" (p. 458, 3 words); lesson total 21.

### Course 5 — Code Improvements (`code-complete-code-improvements`, 8)

Part V, Chapters 20–26. Quality, collaboration, testing, debugging,
refactoring and tuning. Its `how_to` says the defect-removal figures are
averages from many organisations' projects, quoted by the book from Capers
Jones and others, and every lab that uses them says so. `part_a.py` is
Chapters 20–22, `part_b.py` 23–26.

1. **the-software-quality-landscape** — The Software-Quality Landscape — *Chapter 20 · The Software-Quality Landscape* — 15 min
   - **Read:** pp. 463–477. §20.1 (p. 463), external and internal
     characteristics of quality; §20.2 (p. 466), techniques for improving
     quality; §20.3 (p. 469), the relative effectiveness of the techniques,
     Table 20-2's defect-detection rates (p. 470, *F16*), the argument for
     combining unlike techniques (*F17*), and Table 20-3 (p. 472), where the
     book itself multiplies rates to estimate what Extreme Programming's
     practices catch; §20.4 (p. 473), when to do quality assurance; §20.5
     (p. 474), the general principle of software quality — improving
     quality reduces cost.
   - **Quote:** p. 477, 19 words — “No single defect-detection technique is
     completely effective by itself. Testing by itself is not optimally
     effective at removing errors.”
   - **Do:** compute the share of defects a sequence of removal stages
     catches, and the number left, from each stage's rate, and say what the
     product assumes.
   - **Standard:** for three stages with stated rates and 1,000 defects,
     compute the found, the remaining and the combined rate, and state the
     independence assumption.
   - **Lab:** `defects/removal`, family 3, rates as the lesson gives them
     from Table 20-2's modal values (*F16*; at most five of its thirteen
     rows in the lesson, never set out as a table). Presets: `testing-only`
     (1,000 defects; unit test 30%, integration test 35%, system test 40% →
     `dfFound` 727, `dfRemaining` 273, `dfCombined` 727/1000 = 72.7%),
     `inspections-too` (design inspection 55%, code inspection 60%, then the
     three tests → 47543/50 = 950.86, 2457/50 = 49.14, 47543/50000 ≈
     95.1%), `one-stage` (unit test only → 300, 700, 30%). Pins
     `dfCombined`, `dfRemaining`.
   - **Misconception:** "Testing is how you get quality." The chapter's
     argument (*F17*): no single technique's modal rate is above 75% and the
     average is about 40%, so no single stage reaches the levels the book
     reports for leading organisations; on the lesson's illustration even
     three test stages leave a quarter behind. The `note` says what the lab
     cannot show: the product assumes each stage's misses are independent of
     the last, so it gives the same answer for two *like* stages as for two
     *unlike* ones — the "unlike" part is the chapter's claim from Jones's
     data, which a product cannot test; and the book reports that real
     combinations of testing alone often catch less than 60 percent (p. 471,
     after Jones), so 72.7% is an upper bound, not a forecast.
   - **Worked:** 1,000 × 0.70 × 0.65 × 0.60 = 273 left; 72.7% caught.
   - **Exercise:** two stages at 40% and 50%; three at 30%. **Answer:**
     1 − 0.6 × 0.5 = 70%; 1 − 0.7³ = 1 − 0.343 = 65.7%.
   - **Own:** the reader's team's actual stages, with the book's modal rate
     for each and the sentence that the rates are averages from other
     people's projects.
   - **Sources:** McConnell §§20.1–20.5; *F16*, *F17*.

2. **collaborative-construction** — Collaborative Construction — *Chapter 21 · Collaborative Construction* — 15 min
   - **Read:** pp. 479–497. §21.1 (p. 480), an overview of collaborative
     practices and why they find different defects from testing; §21.2
     (p. 483), pair programming; §21.3 (p. 485), formal inspections (roles,
     stages, checklists, egos); §21.4 (p. 492), other kinds (walk-throughs,
     code reading, dog-and-pony shows) and the comparison of techniques; the
     hours per defect the book reports (*F18*).
   - **Quote:** p. 497, 30 words — “Collaborative development practices tend
     to find different kinds of errors than testing does, implying that you
     need to use both reviews and testing to ensure the quality of your
     software.”
   - **Do:** read a short routine as an inspector would and list what to
     raise; compute defects found, defects left and hours by a pipeline of
     stages with rates and hours per defect found.
   - **Standard:** for a ten-line routine with planted defects, list each
     with its line; for an inspection followed by two tests, compute the
     hours per defect found and the defects left, against testing alone.
   - **Lab:** `defects/pipeline`, family 3, records `stage, rate, hours per
     defect found, as the book reports them` (*F16*, *F18*). Presets:
     `test-only` (100 defects; unit test 30%, 20 h; system test 40%, 20 h →
     `dfFound` 58, `dfRemaining` 42, `dfHours` 1,160, `dfPerDefect` 20),
     `inspect-first` (code inspection 60%, 3.5 h, then the same tests →
     416/5 = 83.2, 84/5 = 16.8, 674, 1685/208 ≈ 8.10), `three-and-twelve`
     (inspection 3 h, tests 12 h, rates as `inspect-first` → 83.2, 16.8,
     2292/5 = 458.4, 573/104 ≈ 5.51). Pins `dfRemaining`, `dfHours`,
     `dfPerDefect`. The 20 h test figure is illustrative, inside the IBM
     range the book reports.
   - **Misconception:** "Reviews cost time that testing would not." The
     refutation leans on the book's reported figures (*F18*): 3.5 hours to
     find a defect by inspection against 15–25 by testing (Kaplan, as the
     book cites him), 3 hours against 12 to find and fix (Moore). The `note`
     names the model's assumption: testing's hours scale with the defects
     that reach it, whereas a real test suite costs its running time whether
     it finds anything or not; the pipeline's totals hold only under that
     assumption.
   - **Worked:** 60 found at 3.5 h = 210 h; 12 at 20 h = 240 h; 11.2 at 20 h =
     224 h; 674 h for 83.2 defects.
   - **Exercise:** the `countPassing` routine in §D.4, read as the
     inspection's reader role would. **Answer:** line 3 starts `count` at 1
     instead of 0; line 5 tests `>` where the comment promises "at or
     above"; the parameter `maxScore` (line 2) is never used. Each is the
     kind of point a team's inspection checklist would hold; the book's own
     checklists elsewhere ask whether counters and accumulators are
     initialised (Chapter 10, p. 257) and warn of `>=` written for `>`
     (p. 513). Chapter 21's checklists are about running the practice
     (pp. 484, 491–492); its point is that a team builds its inspection
     checklist from the errors its inspections find (p. 489).
   - **Own:** the last change the reader reviewed (or had reviewed), and
     what each reviewer found that tests had not.
   - **Sources:** McConnell §§21.1–21.4; Fagan 1976; *F18*.

3. **structured-basis-testing** — Structured Basis Testing — *Chapter 22 · Developer Testing* — 15 min
   - **Read:** pp. 499–509. §22.1 (p. 500), developer testing's role in
     quality, and testing during construction; §22.2 (p. 503), the
     recommended approach, and test-first, which McConnell calls one of the
     most beneficial practices of the decade before the book (p. 504); §22.3
     (p. 505), the bag of tricks up to the end of structured basis testing
     (pp. 505–509): the minimum number of test cases, counted from the
     routine's decision points, plus one for a `case` statement with no
     default (p. 506).
   - **Quote:** p. 533, 27 words — “Writing test cases before the code takes
     the same amount of time and effort as writing the test cases after the
     code, but it shortens defect-detection-debug-correction cycles.”
   - **Do:** count the basis test cases a routine needs and write one test
     per decision point.
   - **Standard:** for a routine with a `while`, an `&&` and two `if`s, state
     the count and one input per case.
   - **Lab:** `code/basis`, family 1. Presets: `overtime` (a payroll loop →
     `coBasis` 5, `coPoints` "while line 4, && line 4, if line 6, if line
     8"), `switch-without-default` (a three-case `switch` and an `if` → 6,
     `coNoDefault` 1). Pins `coBasis`, `coNoDefault`.
   - **Misconception:** "Full statement coverage means the routine is
     tested." Basis testing asks for each decision's outcomes; a test suite
     can run every line of `overtime` without the case where `staff[i]` is
     `null`. The modern aside of this course lives here: test-first as the
     book endorses it (p. 504) and what it became in test-driven development
     — the practice the book recommends, carried further, not a view against
     it (§F.4).
   - **Worked:** 1 + `while` + `&&` + `if` + `else if` = 5 cases.
   - **Exercise:** the `archiveOld` routine in §D.4 (a `for`, an `if` with
     `||`). **Answer:** 4 cases; one input each: an empty inbox, an old
     message, a spam message, a new non-spam message.
   - **Own:** one routine of the reader's pasted into the lab, against the
     tests that exist for it.
   - **Sources:** McConnell §§22.1–22.3.

4. **boundaries-and-bad-data** — Boundaries and Bad Data — *Chapter 22 · Developer Testing* — 15 min
   - **Read:** pp. 509–533. The rest of §22.3: data-flow testing (p. 509),
     equivalence partitioning (p. 512), error guessing, boundary analysis
     (p. 513) and compound boundaries, classes of bad data and of good data;
     §22.4 (p. 517), typical errors (where they cluster, the classification,
     how many to expect, *F19*, and construction's share of all defects,
     *F2*); §22.5 (p. 523), test-support tools; §22.6 (p. 528), improving the
     testing; §22.7 (p. 529), keeping test records.
   - **Quote:** p. 533, 24 words — “You can generate many test cases
     deterministically by using basis testing, data-flow analysis, boundary
     analysis, classes of bad data, and classes of good data.”
   - **Do:** list the boundary test values for a range and find which of them
     exposes a wrong check.
   - **Standard:** for a valid range and a check, write the six boundary
     values and name each that the check gets wrong.
   - **Lab:** `cond/range`, family 2. Spec: an order of 1 to 99 items is
     valid; the check says *valid*. Presets: `correct` (`qty >= 1 && qty <=
     99` → `cdDisagree` none, `cdTests` 0, 1, 2, 98, 99, 100, `cdExposed`
     none), `strict-top` (`qty > 0 && qty < 99` → 99, exposed 99),
     `no-lower-check` (`qty <= 99` → `cdDisagree` "0 and below",
     `cdExposed` 0). Pins `cdDisagree`, `cdExposed`.
   - **Misconception:** "One typical value per case is enough." A nominal 50
     passes all three checks; only the boundary values tell them apart.
   - **Worked:** `qty < 99` rejects 99, the largest valid order; the test 99
     catches it, 50 does not.
   - **Exercise:** passwords of 8 to 64 characters, check `len > 8 && len <=
     64`. **Answer:** tests 7, 8, 9, 63, 64, 65; the check is wrong at 8
     only, and only the test 8 exposes it. (As authored, the check is set
     in a five-line routine written for the lesson, `validLength`; not a
     preset. The built lab, `cond/range` with lo 8, hi 64, prints
     `cdDisagree` 8, `cdTests` 7, 8, 9, 63, 64, 65, `cdExposed` 8.)
   - **Own:** one validation in the reader's code, its documented range,
     and the six boundary tests — which of them exist.
   - **Sources:** McConnell §§22.3–22.7; Myers 1979; *F2*, *F19*.

5. **debugging-as-science** — Debugging as Science — *Chapter 23 · Debugging* — 15 min
   - **Read:** pp. 535–562. §23.1 (p. 535), overview: the variation among
     programmers in finding defects (*F20*), defects as opportunities, an
     ineffective approach; §23.2 (p. 540), finding a defect by the scientific
     method (stabilise, locate, fix, test, look for similar), with its tips —
     narrow the suspicious region, binary search, brute force with a time
     limit; §23.3 (p. 550), fixing; §23.4 (p. 554), psychological
     considerations; §23.5 (p. 556), tools.
   - **Quote:** p. 562, 30 words — “A systematic approach to finding and
     fixing errors is critical to success. Focus your debugging so that each
     test moves you a step forward. Use the Scientific Method of Debugging.”
     Also quoted: the section title “The Devil’s Guide to Debugging”
     (p. 539, 5 words).
   - **Do:** state a hypothesis about a failure, name the test that halves the
     suspects, and compute the steps a binary search takes among n suspects.
   - **Standard:** for a failing input and a routine, state the hypothesis,
     the one test that decides it and the line; for 1,000 suspect commits and
     the defect at a given one, list the halving intervals and count the
     steps.
   - **Lab:** `search/bisect`, family 2, inputs `n`, `k` (the defect's
     position). Presets: `commit-637` (1,000, 637 → `seSteps` 10, `seWorst`
     10; intervals 1–1000, 501–1000, 501–750, 626–750, 626–688, 626–657,
     626–641, 634–641, 634–637, 636–637), `commit-63` (1,000, 63 → 9, 10),
     `sixty-four` (64, 1 → 6, 6). Pins `seSteps`, `seWorst`.
   - **Misconception:** "Debugging is reading the code until the defect shows
     itself." The chapter's method is experiment: a hypothesis, a test that
     halves the suspects, repeat; on the lesson's illustration ten tests
     settle a thousand commits.
   - **Worked:** ⌈log₂ 1,000⌉ = 10; 2¹⁰ = 1,024 ≥ 1,000.
   - **Exercise:** the `overtime` routine from Structured Basis Testing
     fails with `ArrayIndexOutOfBoundsException` when called with four
     employees and `count` 5. **Answer:** hypothesis: the loop reads past the
     array because nothing ties `count` to `staff.length`; the test that
     decides it: call it with four non-null employees and `count` 4 (passes)
     and 5 (fails); the line is 4, where `staff[i]` is read with `i == 4`.
     The fix tests the length before the element:
     `i < count && i < staff.length && staff[i] != null` (or drop `count`
     and loop to `staff.length`). The
     five basis tests of the earlier lesson did not include it, which is
     Boundaries and Bad Data's point.
   - **Own:** the reader's last bisection (of commits, input or code): how
     many steps it took against ⌈log₂ n⌉.
   - **Sources:** McConnell §§23.1–23.5; *F20*.

6. **refactoring-safely** — Refactoring Safely — *Chapter 24 · Refactoring* — 15 min
   - **Read:** pp. 563–585. §24.1 (p. 564), kinds of software evolution;
     §24.2 (p. 565), introduction to refactoring and the reasons to refactor
     (duplicate code, long routines, long parameter lists, and the rest of
     the book's list); §24.3 (p. 571), specific refactorings at data,
     statement, routine, class and system level; §24.4 (p. 579), refactoring
     safely (small steps, one at a time, a list, tests, reviews, and the
     evidence on small changes, *F21*); §24.5 (p. 582), strategies.
   - **Quote:** p. 585, 24 words — “Software can either improve or degrade
     as it’s changed. The Cardinal Rule of Software Evolution is that
     internal quality should improve with code evolution.”
     Also quoted: “factoring” (p. 565, 1 word) and “parking lot” (p. 580,
     2 words).
   - **Do:** compute the inputs and outputs of a block before extracting it
     into a routine, and decide whether it extracts cleanly.
   - **Standard:** for a block in a routine, list the variables it reads that
     were set before it (parameters) and those it sets that are read after it
     (results); say what to do when there are two results.
   - **Lab:** `code/extract`, family 1, inputs `from`, `to`. Instance: the
     `printStatement` routine (§D.4) that totals transactions, charges an
     overdraft fee and prints. Presets: `print-lines` (lines 11–12 → `coIn`
     "fees, balance", `coOut` none, `coParams` 2), `fee-loop` (4–9 → `coIn`
     "account, balance, fees", `coOut` "balance, fees", 3), `from-the-top`
     (2–10 → "account", "balance, fees", 1). Pins `coIn`, `coOut`.
   - **Misconception:** "Extract Routine is always safe." It is safe when
     the block has at most one result; `fee-loop` has two, and a Java method
     returns one value, so the refactoring needs a small class or two
     routines first.
   - **Worked:** lines 11–12 read `fees` and `balance` and set nothing used
     later: `printTotals(fees, balance)`.
   - **Exercise:** the `printInvoice` routine in §D.4. **Answer:** lines 2–5
     extract cleanly as `subtotalOf(inv)` (in `inv`, out `subtotal`); lines
     7–9 as `printTotals(subtotal, tax)` (in `subtotal, tax`, out none).
   - **Own:** a block of the reader's that they would like to extract,
     pasted with its routine into the lab, and its In and Out read before
     they start.
   - **Sources:** McConnell §§24.1–24.5; Fowler 1999; *F21*.

7. **code-tuning-strategies** — Code-Tuning Strategies — *Chapter 25 · Code-Tuning Strategies* — 15 min
   - **Read:** pp. 587–608. §25.1 (p. 588), performance overview (quality
     characteristics and performance; efficiency through requirements,
     design, class and routine design, OS, compiler, hardware, and code
     tuning last); §25.2 (p. 591), introduction to tuning: the Pareto
     principle (p. 592, *F22*), old wives' tales, when to tune; §25.3
     (p. 597), kinds of fat and molasses; §25.4 (p. 603), measurement; §25.5
     (p. 605), iteration; §25.6 (p. 606), the approach.
   - **Quote:** p. 608, 25 words — “Most programs spend most of their time in
     a small fraction of their code. You won’t know which code that is until
     you measure it.”
   - **Do:** compute the overall speedup a change to one routine gives, from
     a profile, and find the few routines that hold most of the time.
   - **Standard:** for a four-routine profile and a speed factor on one
     routine, compute the new total, the speedup and the share saved, and how
     many routines reach four-fifths of the time.
   - **Lab:** `profile/speedup`, family 3, records `routine, ms, factor`
     (illustrative profile: parse 600, compute 250, format 100, write 50).
     Presets: `tune-format` (format ×10 → `pfBefore` 1,000, `pfAfter` 910,
     `pfSpeedup` 100/91 ≈ 1.10, `pfSaved` 9/100 = 9%, `pfPareto` "2 of 4
     routines reach 4/5 of the time"), `tune-parse` (parse ×2 → 700, 10/7 ≈
     1.43, 30%), `tune-the-small-ones` (format and write ×1,000 → 17003/20 =
     850.15, 20000/17003 ≈ 1.18, 2997/20000 ≈ 15.0%). Pins `pfAfter`,
     `pfSpeedup`, `pfPareto`.
   - **Misconception:** "A tenfold speedup of a routine makes the program
     much faster." `tune-format` makes a routine ten times faster and the
     program 9% faster; `tune-parse` makes the hot routine twice as fast and
     saves 30%.
   - **Worked:** 1,000 − 100 + 100/10 = 910 ms; 1,000/910 ≈ 1.10.
   - **Exercise:** a program spending 95% of its time in one routine and 5%
     elsewhere. **Answer:** making the 5% a thousand times faster saves
     999/20000 ≈ 5.0%; halving the 95% saves 19/40 = 47.5%.
   - **Own:** a profile the reader has taken (or takes now) of their own
     program, its top four entries typed into the lab.
   - **Sources:** McConnell §§25.1–25.6; Knuth 1971; Boehm 1987b; *F22*.

8. **code-tuning-techniques** — Code-Tuning Techniques — *Chapter 26 · Code-Tuning Techniques* — 15 min
   - **Read:** pp. 609–645. §26.1 (p. 610), logic (stop testing when you know
     the answer, order tests by frequency, tables, lazy evaluation); §26.2
     (p. 616), loops (unswitching, jamming, unrolling, minimising the work
     inside, sentinel values, the busiest loop inside — the book's own
     example and measurements, p. 623, *F23* — strength reduction); §26.3
     (p. 624), data transformations; §26.4 (p. 630), expressions; §26.5
     (p. 639), routines; §26.6 (p. 640), recoding in a lower-level language;
     §26.7 (p. 643), the more things change.
   - **Quote:** p. 645, 28 words — “Results of optimizations vary widely with
     different languages, compilers, and environments. Without measuring
     each specific optimization, you’ll have no idea whether it will help or
     hurt your program.”
   - **Do:** count the loop iterations of a nest in two orders, and move
     loop-invariant work out of a loop, stating the work saved.
   - **Standard:** for a nest with given iteration counts, compute body
     executions, total iterations in each order, and the share saved; for a
     loop with an invariant call, write the moved version and state the
     calls before and after.
   - **Lab:** `run/nested`, family 2, input `sizes` outer to inner. Presets:
     `busiest-outside` (`100 5` → `lpBody` 500, `lpIterations` 600, `lpBest`
     505, `lpSaved` 19/120 ≈ 15.8% — the book's own example, p. 623, *F23*),
     `busiest-inside` (`5 100` → 500, 505, 505, 0), `three-levels` (`50 10
     2` → 1,000, 1,550, 1,022, 264/775 ≈ 34.1%; the lesson's own). Pins
     `lpIterations`, `lpBest`, `lpSaved`.
   - **Misconception:** "A technique that saves 16% of iterations saves 16% of
     time." The lab counts loop iterations, not time; the book's own
     measurements of this change on p. 623 range from a third of the time in
     two languages to almost nothing in another (*F23*), and the chapter's
     lesson is to measure each change.
   - **Worked:** 100 + 100·5 = 600 against 5 + 5·100 = 505.
   - **Exercise:** `for (int i = 0; i < n; i++) { double rate =
     config.taxRate(); gross[i] = net[i] * (1 + rate); }` with n = 1,000.
     **Answer:** `double rate = config.taxRate();` moves before the loop; the
     body still runs 1,000 times; `taxRate()` is called once instead of
     1,000 times — a saving only if the call costs something, which only a
     measurement says.
   - **Own:** one loop nest of the reader's, its sizes typed into the lab,
     and one invariant computation moved out of it.
   - **Sources:** McConnell §§26.1–26.7; *F23*.

### Course 6 — System Considerations (`code-complete-system-considerations`, 4)

Part VI, Chapters 27–30. Program size, managing construction, integration and
tools. Its `how_to` says the course is for anyone who works on a team, and that
its figures are the book's quotations of industry averages.

*As authored:* every instance and figure below stands; the pinned strings follow
§D.0's two decimals (`pjStaffYears` "2/5 = 0.40 to 5", `pjSpread` "25/2 = 12.50",
`pjProduct` "1349/2500 ≈ 0.54", "4757/2500 ≈ 1.90"). The exercises of lessons 3
and 4 are given as code the reader reads the records off: four Java classes whose
calls are the exercise's pairs, and the build's three makefile dependency lines.
Lesson 2's `hard-product` glosses time and storage constraint as the program's
own run time and memory, as Table 28-1 defines them, not the schedule.
Short quotations beyond each lesson's **Quote**, all checked with `cc_quotes.py`:
lesson 1 "right-weight" (p. 658; total 22 words); lesson 2 "religious" (p. 683;
total 36); lesson 3 "big bang integration" (p. 691), "dump truck full of stubs"
(p. 696) and "smokes" (p. 702; total 30); lesson 4 "Tool Fantasyland" (p. 722,
the section title) and "too much of a good thing" (p. 706; total 22). Lesson 2
names van Genuchten 1991 (p. 675) as the book cites it.

1. **how-program-size-affects-construction** — How Program Size Affects Construction — *Chapter 27 · Program Size* — 15 min
   - **Read:** pp. 649–659. §27.1 (p. 650), communication and size (the paths
     among n people, n(n − 1)/2); §27.2 (p. 651), the range of project sizes;
     §27.3 (p. 651), the effect of size on errors (Table 27-1, p. 652, *F24*;
     construction's share of the errors, *F2*); §27.4 (p. 653), on
     productivity (Table 27-2, p. 653, *F25*); §27.5 (p. 654), on development
     activities, and construction's falling share (*F1*).
   - **Quote:** p. 659, 21 words — “All other things being equal, a large
     project will have more errors per thousand lines of code than a small
     one.”
   - **Do:** compute a team's communication paths, and the ranges of
     defects and staff-years the book's tables give for a size, and how wide
     those ranges are.
   - **Standard:** for a team size and a size in thousands of lines, compute
     the paths, the defect range and the staff-year range from the stated
     table rows, and the ratio of the range's ends.
   - **Lab:** `project/scale`, family 3, inputs `people`, `kloc`,
     `densityLow`, `densityHigh` (defects per thousand lines), `prodLow`,
     `prodHigh` (lines per staff-year), the last four from the book's rows
     (*F24*, *F25*). Presets: `small-team` (3; 10; 0–40; 2,000–25,000 →
     `pjPaths` 3, `pjDefects` 0–400, `pjStaffYears` 2/5 = 0.4 to 5,
     `pjSpread` 25/2 = 12.5), `medium` (10; 100; 2–70; 1,000–20,000 → 45,
     200–7,000, 5–100, 20), `large-team` (50; 1,000; 4–100; 700–10,000 →
     1,225, 4,000–100,000, 100 to 10000/7 ≈ 1,428.57, 100/7 ≈ 14.29). Pins
     `pjPaths`, `pjDefects`, `pjStaffYears`, `pjSpread`. The body says the
     spread is the honest result: the book's productivity ranges are an
     order of magnitude wide at every size.
   - **Misconception:** "A ten-times-larger program is ten times the work of
     a small one." The chapter's argument: productivity falls and error
     density rises with size (Tables 27-1 and 27-2), and communication paths
     grow with the square of the team; on the lesson's illustration, 3 paths
     become 1,225.
   - **Worked:** 50·49/2 = 1,225 paths; 1,000 × 4 to 1,000 × 100 defects.
   - **Exercise:** a team growing from 6 to 12 people. **Answer:** 15 paths
     to 66.
   - **Own:** the reader's team size, the paths it implies, and the
     project's size against the book's rows.
   - **Sources:** McConnell §§27.1–27.5; Brooks 1995; *F1*, *F2*, *F24*,
     *F25*.

2. **managing-construction** — Managing Construction — *Chapter 28 · Managing Construction* — 15 min
   - **Read:** pp. 661–688. §28.1 (p. 662), encouraging good coding; §28.2
     (p. 664), configuration management; §28.3 (p. 671), estimating a
     construction schedule (approaches, influences on schedule, Table 28-1's
     factors, p. 674, *F26*, estimation against control, what to do if you
     are behind — Brooks's law, as the book qualifies it: adding people can
     help if the tasks are partitionable, p. 676); §28.4 (p. 677),
     measurement; §28.5 (p. 680), treating programmers as people, with
     individual variation (p. 682, *F29*); §28.6 (p. 686), managing your
     manager.
   - **Quote:** p. 688, 35 words — “Good software estimation is a significant
     challenge. Keys to success are using multiple approaches, tightening
     down your estimates as you work your way into the project, and making
     use of data to create the estimates.”
   - **Do:** adjust a nominal effort estimate by a set of multipliers and
     state the range the factors span.
   - **Standard:** given a nominal estimate and three multipliers, compute
     their product and the adjusted effort.
   - **Lab:** `project/effort`, family 3, records `factor, multiplier`, the
     book's factor names and the multipliers its percentages give (*F26*;
     at most seven of the table's factors, never set out as a table).
     Presets (nominal 100 staff-months): `strong-team` (programmer
     capability 0.76, requirements analyst capability 0.71 → `pjProduct`
     1349/2500 = 0.5396, `pjEffort` 1349/25 = 53.96), `weak-team` (1.34,
     1.42 → 4757/2500 = 1.9028, 4757/25 = 190.28), `hard-product` (product
     complexity 1.74, time constraint 1.63, storage constraint 1.46 →
     1035213/250000 = 4.140852, ≈ 414.09). Pins `pjProduct`, `pjEffort`.
   - **Misconception:** "An estimate is a number." The product's range is
     the refutation: two factors alone move the same nominal estimate from
     0.54 to 1.90 times, and §28.3 asks for several approaches and an
     estimate tightened as the project goes. **Also:** "Adding people to a
     late project brings it in earlier" — Brooks's law (Brooks 1995), which
     the book states and qualifies (p. 676); in prose only, since the lab has
     no input for team size.
   - **Worked:** 0.76 × 0.71 = 0.5396; 100 × 0.5396 = 53.96 staff-months.
   - **Exercise:** nominal 50 staff-months, weak programmers (programmer
     capability 1.34) with good tools (use of software tools 0.78).
     **Answer:** 1.34 × 0.78 = 1.0452; 52.26 staff-months.
   - **Own:** the reader's last estimate, the two factors they would apply
     to it now, and the adjusted figure.
   - **Sources:** McConnell §§28.1–28.6; Boehm et al. 2000; Brooks 1995;
     *F26*, *F29*.

3. **integration-order** — Integration Order — *Chapter 29 · Integration* — 15 min
   - **Read:** pp. 689–708. §29.1 (p. 689), the importance of the integration
     approach; §29.2 (p. 691), phased ("big bang") against incremental
     integration; §29.3 (p. 694), incremental strategies: top-down (stubs),
     bottom-up (drivers), sandwich, risk-oriented, feature-oriented,
     T-shaped; §29.4 (p. 702), the daily build and smoke test.
   - **Quote:** p. 708, 21 words — “Incremental integration comes in several
     varieties, and, unless the project is trivial, any one of them is better
     than phased integration.”
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
   - **Misconception:** "Integration is a phase at the end of construction."
     That is phased integration, which §29.2 argues against; the stubs and
     drivers the lab counts are the price of integrating incrementally,
     which is the trade the chapter accepts, and `risk-first` shows the
     hardest-part-first order paying in both.
   - **Worked:** top-down integrates `main` first, so `ui` and `orders` are
     stubs until they arrive; five stubs, no drivers.
   - **Exercise:** `app, ui; app, core; core, store; ui, core` integrated
     `app ui core store`. **Answer:** stubs `core`, `store`, `ui` (3), no
     drivers.
   - **Own:** the call graph of one feature of the reader's, and the order
     they would integrate it in, typed into the lab.
   - **Sources:** McConnell §§29.1–29.4.

4. **programming-tools** — Programming Tools — *Chapter 30 · Programming Tools* — 12 min
   - **Read:** pp. 709–725. §30.1 (p. 710), design tools; §30.2 (p. 710),
     source-code tools (editing, analysing quality, refactoring, version
     control, data dictionaries); §30.3 (p. 716), executable-code tools
     (compilers, linkers, build tools such as `make`, libraries, code
     generation, preprocessors, debuggers, testing tools, tuning tools);
     §30.4 (p. 720), tool-oriented environments; §30.5 (p. 721), building
     your own tools; §30.6 (p. 722), tool fantasyland.
   - **Quote:** p. 725, 14 words — “Programmers sometimes overlook some of the
     most powerful tools for years before discovering them.”
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
     §F.4).
   - **Misconception:** "A build tool rebuilds what you edited." It rebuilds
     what depends on it, transitively; a header reaches every object that
     includes it.
   - **Worked:** `util.h` → `main.o`, `util.o` → `app`: three targets.
   - **Exercise:** `util.c` changes. **Answer:** `util.o` and `app` (2).
   - **Own:** one build target of the reader's, its prerequisites as
     records, and what a change to the most-included file rebuilds.
   - **Sources:** McConnell §§30.1–30.6.

### Course 7 — Software Craftsmanship (`code-complete-software-craftsmanship`, 4)

Part VII, Chapters 31–35. Layout, self-documenting code, character, and the
book's themes. Its `how_to` says the course can be read alone.

1. **layout-and-style** — Layout and Style — *Chapter 31 · Layout and Style* — 15 min
   - **Read:** pp. 729–775. §31.1 (p. 730), layout fundamentals (the
     Fundamental Theorem of Formatting, p. 732: good visual layout shows the
     logical structure; the objectives of good layout); §31.2 (p. 736),
     techniques (white space and the indentation study, p. 737, *F27*;
     parentheses); §31.3 (p. 738), layout styles (pure blocks, emulating pure
     blocks, begin-end pairs, endline layout); §31.4–31.8 (pp. 745–773),
     control structures, individual statements, comments, routines,
     classes.
   - **Quote:** p. 775, 15 words — “The first priority of visual layout is to
     illuminate the logical organization of the code.”
   - **Do:** find each line whose indentation disagrees with the structure the
     compiler reads, and say in words what the compiler does.
   - **Standard:** for a listing with unbraced `if`s, mark every line whose
     indentation misstates its structure and say what the compiler does.
   - **Lab:** `code/layout`, family 1, `cfg["indent"] = 4`. Presets:
     `dangling-else` (`notifyUser`: an `else` indented under the outer `if`
     that Java binds to the inner → `coMisIndented` 2, `coLines` "5, 6"),
     `two-statements` (an unbraced `if` followed by two indented statements
     → 1, "4"), `braced` (the first preset with braces → 0, none). Pins
     `coMisIndented`, `coLines`. The listing marks a flagged line in the
     gutter, not by colour alone.
   - **Misconception:** "Indentation is cosmetic: the compiler ignores it, so
     it cannot cause a defect." `dangling-else` shows a layout that tells the
     reader the opposite of what the code does, and the exercise is a defect
     the layout hid. (The chapter concedes that much of layout is a matter of
     taste — brace placement is one of its "religious issues" — and the
     lesson does not argue with that.)
   - **Worked:** the `else` on line 5 belongs to the `if` on line 3, whatever
     the indentation says, so it should sit at that `if`'s depth (8 spaces)
     and `sendLetter` at 12. The body states this structure in words, for a
     listener who cannot see the indentation; the `note` says the listing's
     evidence is visual.
   - **Exercise:** the `clamp` routine in §D.4. **Answer:** the lab flags
     line 6 (`coMisIndented` 1, `coLines` "6"); `return high;` is
     unconditional, so every value not below `low` returns `high`; and
     `javac` rejects line 7 as unreachable — here the compiler catches what
     the layout hid, and with any statement other than a `return` on line 6
     nothing would.
   - **Own:** a routine of the reader's pasted into the lab, widened to four
     spaces by search-and-replace (never by an editor's re-indent, which
     would remove what the lab checks; the lab's indent is a lesson-level
     cfg key, not a reader input).
   - **Sources:** McConnell §§31.1–31.8; *F27*.

2. **self-documenting-code** — Self-Documenting Code — *Chapter 32 · Self-Documenting Code* — 15 min
   - **Read:** pp. 777–817. §32.1 (p. 777), external documentation; §32.2
     (p. 778), programming style as documentation; §32.3 (p. 781), to comment
     or not to comment (the book's dialogue, whose voices are not all
     McConnell's); §32.4 (p. 785), keys to effective comments (kinds of
     comments; the optimum number, p. 792, *F28*); §32.5 (p. 792), commenting
     techniques; §32.6 (p. 813), IEEE standards.
   - **Quote:** p. 817, 22 words — “Comments should say things about the code
     that the code can’t say about itself—at the summary level or the intent
     level.”
   - **Do:** compute a routine's comment density per statement and classify
     each comment as repeating the code, explaining it, or stating intent.
   - **Standard:** for a routine, count statement and comment lines, compute
     the density, and mark each comment by kind.
   - **Lab:** `code/size`, family 1 (`coDensity` = comment lines over
     statement lines). Presets: `comments-repeat` (an average routine with a
     comment over every statement → `coStatements` 5, `coComment` 5,
     `coDensity` 1 = 100%), `comments-intent` (`mean` with one header comment
     stating its precondition → 5, 1, 1/5 = 20%). Pins `coComment`,
     `coDensity`.
   - **Misconception:** "More comments make code better documented." The
     density on `comments-repeat` is five times the other's and every one of
     its comments repeats the code; the chapter's kinds are the test, not the
     count — and a routine can match that density with every comment
     useful, which the count cannot tell apart (the lesson does not say
     which case the exercise is: its answer stays in the quiz). The modern
     aside of this course lives here (the comment debate
     since, §F.4).
   - **Worked:** 5 comment lines over 5 statement lines: 100%; one in five:
     20%.
   - **Exercise:** `isLeapYear` in §D.4. **Answer:** 2 comment lines, 2
     statement lines, `coDensity` 100%, the same as `comments-repeat`; both
     comments state intent (what a leap year is; the rule in words) and
     neither repeats the code.
   - **Own:** a routine of the reader's pasted into the lab, and each of its
     comments marked by kind.
   - **Sources:** McConnell §§32.1–32.6; *F28*.

3. **personal-character** — Personal Character — *Chapter 33 · Personal Character* — 12 min
   - **Read:** pp. 819–835. §33.1 (p. 820), is personal character off-topic?
     (with the differences among programmers, *F29*); §33.2 (p. 821),
     intelligence and humility; §33.3 (p. 822), curiosity; §33.4 (p. 826),
     intellectual honesty; §33.5 (p. 828), communication and cooperation;
     §33.6 (p. 829), creativity and discipline; §33.7 (p. 830), laziness (three
     kinds: deferring a task is "true laziness", doing it at once is the
     enlightened kind, and writing a tool to do it is "long-term laziness",
     the most productive kind provided the tool saves time — corrected from
     the text at authoring); §33.8
     (p. 830), characteristics that matter less than you think; §33.9
     (p. 833), habits.
   - **Quote:** p. 835, 23 words — “The characteristics of a superior
     programmer have almost nothing to do with talent and everything to do
     with a commitment to personal development.”
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
     a week). **Answer:** 24 runs, 24/5 = 4.8 weeks, 59/3 ≈ 19.67 hours saved
     in the first year.
   - **Own:** one task the reader repeats weekly, with an honest estimate of
     the tool's build time.
   - **Sources:** McConnell §§33.1–33.9; *F29*.

4. **themes-of-craftsmanship** — Themes of Craftsmanship — *Chapters 34–35 · Themes and Further Reading* — 15 min
   - **Read:** Chapter 34, pp. 837–853, the book's themes: conquer complexity
     (§34.1); pick your process; write programs for people first, computers
     second; program into your language, not in it; focus your attention
     with conventions; program in terms of the problem domain; watch for
     falling rocks; iterate, repeatedly, again and again; separate software
     and religion (§34.9, p. 851). Chapter 35, pp. 855–862, where to find
     more: the reading plan, named and pointed to, not reproduced (§G).
   - **Quote:** p. 853, 27 words — “Dogmatic methodologies and high-quality
     software development don’t mix. Fill your intellectual toolbox with
     programming alternatives, and improve your skill at choosing the right
     tool for the job.”
   - **Do:** apply the course's counts to one routine and say which themes
     each count serves.
   - **Standard:** for a 16-line routine, state its decision points and
     depth, name two improvements and the theme each serves.
   - **Lab:** `code/complexity`, family 1. Presets: `retry-delay` (a
     retry-backoff routine, 16 lines → `coDecisions` 7, `coBreakdown` "1 + if
     3 + for 1 + && 1 + || 1", `coBand` "6–10", `coDepth` 2),
     `nested-shipping` (from Nesting and Complexity → 9, depth 5). Pins
     `coDecisions`, `coDepth`.
   - **Misconception:** "Craftsmanship is a set of rules to follow."
     Chapter 34's last theme argues against treating any method as a
     religion; the counts are tools for judgement, which is the material
     clause.
   - **Worked:** 1 + `if` ×3 + `for` + `&&` + `||` = 7.
   - **Exercise:** the reader's own routine, pasted in. **Answer:** none
     fixed; the quiz item that carries the exercise asks about a changed
     `retry-delay` (line 7 becomes `delay = Math.min(delay * 2, 10000);` and
     lines 8–10 go: 6 decision points, depth 1), so that it has a fixed
     answer the page does not print; the preset's own 7 and depth 2 are in
     the body (pedagogy review of Course 7, finding 2). The `standard` uses
     the preset, worked without the lab.
   - **Own:** the exercise is the own-code step: the reader's routine, its
     decision points, its depth, and one sentence per theme it touches.
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
called done. Eight modes and 36 views would not fit if every page shipped
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
listing that way, comment line included (§10.4, pp. 245–248; F10). A view
that flags lines (`layout`, `dataflow`, `ppp`) marks each flagged line in the
gutter with a glyph and a visually hidden word, never by colour alone. At a
narrow width (below 40em) the listing stacks under the textarea rather than
beside it, and neither scrolls the page sideways: the listing scrolls in its
own box, and the textarea wraps off (`wrap="off"`) inside its own.

**Zero denominators.** A tile whose denominator is zero prints `—` and the
banner says why in one sentence ("no statement lines, so no density"); it is
never a red refusal, because an empty listing is a legitimate input. An
*input* that is a divisor (a ratio, a productivity, a rate, a factor, a
frequency total) must be positive, and a zero or negative one is refused with
the field named. `run/arith` is the exception that models Java: `int` and
`long` division by zero prints `ArithmeticException`; `double` division by
zero is refused with the sentence "Java would print Infinity or NaN; this lab
does not model it".

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
  `do` (its `while` counts), `?:`, `catch` and `try` add nothing. The book's
  rule (Table 19-2, p. 458) counts `if`, `while`, `repeat`, `for`, `and` and
  `or` *or their equivalents*, and `?:` is arguably an equivalent of `if`; leaving it
  out is **the kit's choice**, and where `?` appears the banner says so in
  those words ("`?:` is not counted: the kit's choice, not the book's").
  `case` labels count one each, as the book counts each case.
- **Depth** of a statement line is its brace depth below the routine's own
  braces (a fragment's lines start at 0). Unbraced bodies add nothing to it;
  the `layout` view is where they are checked. This is the kit's convention:
  a statement directly in the routine's body is at depth 0, so "three levels
  of nested `if`" (F15) is depth 3 for the innermost `if`'s statements. The
  `complexity` banner states it.

Views (each takes `code`, a textarea, plus what is listed):

- `size`: tiles `coLines`, `coCode` (code lines, braces included),
  `coStatements` (statement lines: code lines that are not only braces and
  semicolons), `coComment` (comment lines), `coBlank`, `coParams` (a count,
  or "none (a fragment)"), `coDensity` (comment lines / statement lines, a
  share; `—` when there are no statement lines). Density is over statements
  because the study the book cites counts comments per statement (§32.4,
  F28). The banner says the book's routine-length line is non-comment,
  non-blank (F8), which is `coCode`; `coStatements` leaves out brace-only
  lines too.
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
  `coBand` (cfg `bands`, default `[5, 10]`: "0–5", "6–10", "10+", the
  book's labels from §19.6, p. 458), `coDepth`, `coDeepest` (the first line
  at that depth). The book's bands overlap at 10 (it prints "6–10" and
  "10+"); the kit puts 10 in "6–10", and the banner says so in one sentence.
  The banner also names the bands as McConnell's guidance — what to think
  about doing, not a grade.
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
- `shared`: records `routine, access, global`, access `r`, `w` or `rw`;
  input `owners` (optional, `global=routine; …`: the access routine through
  which every use of that global goes). Tiles `dgGlobals`, `dgRoutines`,
  `dgCoupled` (unordered pairs of distinct routines that touch a common
  global which at least one of them writes; the banner gives it out of
  n·(n − 1)/2), `dgMostShared` ("current, 5 routines"; ties to the
  alphabetically first global), `dgDirectAccess` (the places that touch a
  global's representation directly: for an owned global 1, otherwise the
  number of routines that use it, summed over globals), `dgWriters` (per
  global in alphabetical order, its owner if it has one, else the routines
  that write it, or `none`: "current: readInput, reset; errors: log").
  Owners do not change `dgCoupled`: the banner says access routines move the
  coupling behind one name, they do not remove it (§13.3).
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
  in `cdDisagree`). The evaluation points are each literal c itself as
  well as c ± 1 (a check `x != 7` differs from the range only at 7); a
  literal outside `int`, or a point outside it, is refused or dropped, never
  wrapped.
- `barricade`: records `value, side, handling`, `side` `outside` or
  `inside` (of the barricade, §8.5), `handling` `validate`, `assert` or
  `none`. The chapter's rule: data outside is validated by error handling;
  data inside may be asserted (§8.5, p. 205). Tiles `cdValues` (records),
  `cdOutsideUnchecked`, `cdOutsideAsserted`, `cdInsideUnchecked`,
  `cdInsideValidated`, each "count: names" in record order, or "0: none".
  The banner says the tiles apply the chapter's rule to the records the
  lesson states and are not a verdict: §8.8 allows judgement, and validating
  inside is a cost, not a defect.

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
  integers); the loop `for (int i = start; i cmp bound; i += step)` over
  Java `int`. Computed in closed form, never by running it. `le` is `lt` with
  bound + 1 and `ge` is `gt` with bound − 1. `lt`: 0 iterations when start ≥
  bound; ⌈(bound − start)/step⌉ when step > 0; when step < 0, "never ends
  without overflow" (in Java `i` wraps past the bottom of `int` and the loop
  then stops, which is a defect, not an ending). `gt` mirrors it. `ne`: 0
  when start = bound; (bound − start)/step when that is a positive whole
  number; otherwise "never ends" when (bound − start) is not a multiple of
  gcd(step, 2³²) (no value of `i`, wrap-around included, ever equals the
  bound), else "never ends without overflow". Tiles `lpIterations` (a count
  or one of the two sentences), `lpLast` (`—` when it never runs), `lpAfter`
  (the value an `i` declared *before* the loop would hold after it). The
  panel says that an index declared in the `for` header does not exist after
  the loop in Java, and that the book advises against relying on its value
  (p. 377). The `step` field's hint reads "a negative step counts down".
- `nested`: input `sizes` (outer to inner, 1 to 5 positive whole numbers).
  Tiles `lpBody` (the product), `lpIterations` (Σ over levels of the product
  of the sizes down to that level), `lpBest` (the same with the sizes
  ascending), `lpSaved` ((iterations − best)/iterations).
- `recursion`: inputs `fn` (`factorial` | `fibonacci`), `n` (0 to 90 for
  `fibonacci`, 0 to 20 for `factorial`, so that every `lpValue` fits a Java
  `long`; a larger `n` is refused with that reason).
  `factorial(n) = n ≤ 1 ? 1 : n·factorial(n − 1)`; `fibonacci(n) = n < 2 ? n :
  fibonacci(n − 1) + fibonacci(n − 2)`. Tiles `lpCalls` (max(n, 1);
  2·F(n + 1) − 1), `lpDepth` (max(n, 1)), `lpValue`, `lpLoop` (max(n − 1, 0),
  the iterations of the loop version).
- `arith`: inputs `type` (`int` | `long` | `double`), `start`, `op` (`+ - * /
  %`), `operand`, `times` (1 to 1,000): `acc = start; repeat times: acc = acc
  op operand`, each step in the type's arithmetic — `int`/`long` wrap at 32/64
  bits, `/` truncates toward zero, `%` takes the dividend's sign, division by
  zero prints `ArithmeticException`; `double` rounds every literal and every
  result to the nearest binary64, ties to even. Zero is a valid `double`
  (`0.0`) and is never refused as a value. What is refused, with a sentence
  naming the reason: `double` division by zero ("Java would print Infinity or
  NaN; this lab does not model it"); a result whose magnitude overflows
  binary64 (the same sentence, Infinity); a non-zero result below the
  smallest normal double (subnormals are not modelled). Tiles `nuJava`
  (what Java prints: for `int` and `long` the plain integer, ASCII `-`, no
  grouping; for `double`, what `Double.toString` prints **as JDK 19 or later
  prints it** — the shortest decimal that reads back to the same binary64,
  always with a `.` ("1.0", not "1"), and in Java's scientific form `1.0E-5`
  below 10⁻³ and from 10⁷; earlier JDKs print longer strings for some
  values, and the panel says so), `nuExact` (the same operations on exact
  rationals, in §D.0's format: `7/2 = 3.50`, `10/3 ≈ 3.33`), `nuEqual`
  (yes/no), and for `double` `nuStored` (the binary64 result as an exact
  fraction).

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
  `pfPareto` ("6 of 8": the fewest entries, largest first, whose amounts
  reach `target` of the total, out of all entries; the banner spells it out,
  "6 of 8 entries reach 4/5 of the total").
- `speedup`: records `name, time, factor` (factor ≥ 1/1000, 1 = unchanged).
  Tiles `pfBefore`, `pfAfter` (Σ time/factor), `pfSpeedup`
  (before/after), `pfSaved` ((before − after)/before), `pfPareto` (as in
  `shares`, over the times before tuning, target 4/5).

#### project (`pj`) — family 3

- `language`: inputs `size` (statements of C), `ratio` (the book's
  statements of C equivalent to one statement of the language, Table 4-1;
  positive). One tile, `pjEquivalent` (size / ratio: the statements of the
  language that do the same work).
  The earlier `rate` input and its two day tiles are gone: they turned a
  ratio of expressiveness into a schedule, which the book does not do.
- `scale`: inputs `people`, `kloc`, `densityLow`, `densityHigh`, `prodLow`,
  `prodHigh` (productivities positive). Tiles `pjPaths` (people·(people −
  1)/2), `pjDefects` (kloc × density range), `pjStaffYears` (1,000·kloc /
  prodHigh to 1,000·kloc / prodLow), `pjSpread` (prodHigh / prodLow: how
  many times the slowest estimate exceeds the fastest).
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

The figures in §C were computed by a Python reference model of every view,
`ccref.py`, run over every lesson's instances by `presets.py`, in
`/tmp/claude-0/-home-claude/3b1d3502-1b81-5554-ace3-d7f9f019031f/scratchpad/`
(not committed; the orchestrator copies both to the kit engineer). This is
revision 2, after the reviews; `ccref_v1.py` and `presets_v1.py` beside them
are the first revision, kept only for the record. `presets.py` prints every
preset's tiles, lesson by lesson in §C's numbering (1.1 to 7.4); every figure
in §C is its output. Revision 2 changed the model in these places, each
mirrored in §D.1: `size` gains `coStatements` and computes `coDensity` over it
(`—` at zero); `complexity`'s top band is "10+"; `shared` takes `owners` and
gains `dgDirectAccess` and `dgWriters`, with ties broken alphabetically; the
new `cond/barricade`; `range` evaluates at each literal itself; `loop`'s edge
cases and `ne` against wrap-around; `recursion` caps `factorial` at 20;
`arith` refuses `double` division by zero with the stated sentence;
`speedup` gains `pfPareto`; `language` is one tile; `scale` gains `pjSpread`.

The model is not the kit: the kit is JavaScript, and its figures are read
from the page by `labcheck.js --observe`. Where the two disagree, the kit
engineer finds out which is wrong and records it in the kit report. One known
difference is deliberate: the model prints a `double` with Python's `repr`,
which agrees with Java's `Double.toString` (JDK 19 or later) on every value
in §C but not in form in general (`1e-05` against `1.0E-5`); the kit prints
Java's form (§D.1, `run/arith`).

**One source for each snippet.** In the content package a snippet is one
Python string constant, used both by the lesson's `code` block and by the
preset's cfg, so the listing the reader reads and the listing the lab counts
cannot drift; a test asserts, for every `code` lab, that its preset's code is
one of the lesson's `code` blocks or a named exercise constant (§E.4).

The snippets below are the lessons' instances, verbatim, generated from
`presets.py`; an author may improve wording but recomputes and records any
change. All are at most 20 lines except `nested-shipping` (22 lines: the
nesting is the lesson). The remaining presets' snippets (`public-fields`, the
label printers, `nine-parameters`, `parameter-objects`, `short-names`,
`problem-names`, `magic`, `named`, `switch-without-default`,
`comments-repeat`, `comments-intent`, `retry-delay`) are in `presets.py` with
their figures; the author copies them from there.

**Lesson snippets.**

`free-slot` (`presets.py` `ppp`; The Pseudocode Programming Process; `ppp-complete` adds `log.warn("table full");` after line 14):

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

`count-unset` (`presets.py` `init-bad`; Declaring and Initializing Variables; `initialized` is `init-good` in `presets.py`, `int count = 0;` on line 3):

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

`set-twice` (`presets.py` `init-twice`; Declaring and Initializing Variables):

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

`declared-at-top` (`presets.py` `span-top`; Scope, Span and Live Time; revised in review):

```java
void auditShipments(Shipment[] shipments, int limitKg) {
    int scanned = 0;
    int heaviestKg = 0;
    int overLimit = 0;
    printTitle();
    printLegend();
    for (Shipment s : shipments) {
        s.verify();
        scanned = scanned + 1;
    }
    printCount(scanned);
    for (Shipment s : shipments) {
        heaviestKg = Math.max(heaviestKg, s.weightKg());
        if (s.weightKg() > limitKg) {
            overLimit = overLimit + 1;
        }
    }
    printSummary(heaviestKg, overLimit);
}
```

`declared-near-use` (`presets.py` `span-near`; the same statements, each variable declared just before its loop):

```java
void auditShipments(Shipment[] shipments, int limitKg) {
    printTitle();
    printLegend();
    int scanned = 0;
    for (Shipment s : shipments) {
        s.verify();
        scanned = scanned + 1;
    }
    printCount(scanned);
    int heaviestKg = 0;
    int overLimit = 0;
    for (Shipment s : shipments) {
        heaviestKg = Math.max(heaviestKg, s.weightKg());
        if (s.weightKg() > limitKg) {
            overLimit = overLimit + 1;
        }
    }
    printSummary(heaviestKg, overLimit);
}
```

`total-first` (`presets.py` `order-wrong`; Organizing Straight-Line Code; revised in review (a parcel quote)):

```java
double shippingQuote(Parcel parcel) {
    double total = base + surcharge + insurance;
    double base = parcel.baseRate();
    double surcharge = parcel.fuelSurcharge();
    double insurance = parcel.insuranceFee();
    return total;
}
```

`in-order` (`presets.py` `order-right`):

```java
double shippingQuote(Parcel parcel) {
    double base = parcel.baseRate();
    double surcharge = parcel.fuelSurcharge();
    double insurance = parcel.insuranceFee();
    double total = base + surcharge + insurance;
    return total;
}
```

`hidden` (`presets.py` `order-hidden`):

```java
void printQuote(Quote quote) {
    quote.loadRates();
    quote.addSurcharges();
    quote.addInsurance();
    quote.print();
}
```

printQuote with parameters (`presets.py` `order-visible`; the exercise's answer):

```java
void printQuote(Quote quote) {
    Rates rates = quote.loadRates();
    Rates withFuel = quote.addSurcharges(rates);
    Rates insured = quote.addInsurance(withFuel);
    quote.print(insured);
}
```

`nested-shipping` (`presets.py` `nested`; Nesting and Complexity; Themes of Craftsmanship):

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

`guard-clauses` (`presets.py` `flat`):

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

`overtime` (`presets.py` `basis`; Structured Basis Testing; Debugging as Science; revised in review: the comment on line 6 states the rule the code must keep):

```java
double overtimePay(Employee[] staff, int count) {
    double pay = 0.0;
    int i = 0;
    while (i < count && staff[i] != null) {
        Employee e = staff[i];
        if (e.isExempt()) {
            // exempt staff earn no overtime
        } else if (e.hours() > 40) {
            pay = pay + (e.hours() - 40) * e.rate() * 1.5;
        }
        i = i + 1;
    }
    return pay;
}
```

`printStatement` (`presets.py` `extract`; Refactoring Safely):

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

`dangling-else` (`presets.py` `layout-dangling`; Layout and Style; renamed `notifyUser` in review: `notify(User)` overloads `Object.notify()` legally, but a reader stops at it; `braced` is `layout-good`):

```java
void notifyUser(User user) {
    if (user.isActive())
        if (user.wantsEmail())
            sendEmail(user);
    else
        sendLetter(user);
    log(user);
}
```

`two-statements` (`presets.py` `layout-two`):

```java
void close(Account account) {
    if (account.balance() == 0)
        account.markClosed();
        archive(account);
    log(account);
}
```

`private-fields` (`presets.py` `class-private`; Abstract Data Types and Interfaces; revised in review to 20 lines):

```java
public class Employee {
    private String name;
    private Address address;
    private PhoneNumber phone;
    private Money salary;
    private int vacationDays;
    public Employee(String name, Money salary) {
        this.name = name;
        this.salary = salary;
    }
    public String name() {
        return name;
    }
    public Money monthlyPay() {
        return salary.dividedBy(12);
    }
    private boolean isEligibleForBonus() {
        return vacationDays < 5;
    }
}
```

`kitchen-sink` (`presets.py` `class-sink`; Abstract Data Types and Interfaces; revised in review: an abstract `Kiosk`, 18 lines, replacing the 35-line class):

```java
public abstract class Kiosk {
    public String location;
    public Printer printer;
    private int ticketsIssued;
    private int refundsToday;
    private Forecast forecast;
    private String forecastCity;
    private Writer auditLog;
    private int auditLines;
    private boolean maintenanceMode;

    public abstract Ticket issueTicket(Fare fare);
    public abstract void refundTicket(Ticket ticket);
    public abstract Forecast fetchForecast(String city);
    public abstract void showForecast();
    public abstract void openAuditLog();
    public abstract void closeAuditLog();
}
```

`printSummary` (`presets.py` `dupes-summary`; Reasons to Create a Routine, exercise (b); new in review):

```java
void printSummary(Totals totals) {
    double amount = totals.sales();
    String label = "Sales";
    System.out.print(label + ": ");
    System.out.println(String.format("%,.2f", amount));
    amount = totals.refunds();
    label = "Refunds";
    System.out.print(label + ": ");
    System.out.println(String.format("%,.2f", amount));
}
```

**Exercise snippets.**

`discountPercent` (`presets.py` `discount`; Nesting and Complexity: 7 decision points, depth 2; basis count 7):

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

refundAmount, nested (`presets.py` `refund-nested`; Unusual Control Structures, exercise; new in review):

```java
double refundAmount(Order order) {
    double refund = 0.0;
    if (order.isPaid()) {
        if (order.daysSinceDelivery() <= 30) {
            refund = order.total();
        }
    }
    return refund;
}
```

refundAmount, with guard clauses (`presets.py` `refund-guards`; its answer: 3 decision points as before, depth 2 → 1):

```java
double refundAmount(Order order) {
    if (!order.isPaid()) {
        return 0.0;
    }
    if (order.daysSinceDelivery() > 30) {
        return 0.0;
    }
    return order.total();
}
```

`archiveOld` (`presets.py` `archive-old`; Structured Basis Testing: 4):

```java
void archiveOld(Message[] inbox, int days) {
    for (int i = 0; i < inbox.length; i++) {
        if (inbox[i].ageInDays() > days || inbox[i].isSpam()) {
            inbox[i].archive();
        }
    }
}
```

`countPassing` (`presets.py` `count-passing`; Collaborative Construction, read as an inspection; new in review):

```java
// Returns how many scores are at or above the pass mark.
int countPassing(int[] scores, int passMark, int maxScore) {
    int count = 1;
    for (int i = 0; i < scores.length; i++) {
        if (scores[i] > passMark) {
            count = count + 1;
        }
    }
    return count;
}
```

`expireSessions` (`presets.py` `expire-sessions`; The Pseudocode Programming Process: 4 steps, line 10 empty; the answer notes that `sessions.remove(s)` inside the enhanced `for` throws `ConcurrentModificationException`, so the fix uses an `Iterator`):

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

`printInvoice` (`presets.py` `print-invoice`; Refactoring Safely: 2–5 → in `inv`, out `subtotal`; 7–9 → in `subtotal, tax`, out none):

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

`clamp` (`presets.py` `clamp`; Layout and Style: line 6 mis-indented):

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

`isLeapYear` (`presets.py` `leap-year`; Self-Documenting Code; new in review):

```java
// True if the year has 366 days in the Gregorian calendar.
boolean isLeapYear(int year) {
    // divisible by 4, except centuries, except every fourth century
    return (year % 4 == 0 && year % 100 != 0) || year % 400 == 0;
}
```

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
Microsoft Press, 2004)**, copyright 2004 by Steven C. McConnell. The
operator's copy is a PDF of that edition; its text was extracted privately
(`pdftotext -layout`, one form feed per PDF page) to
`/tmp/claude-0/-home-claude/3b1d3502-1b81-5554-ace3-d7f9f019031f/scratchpad/book/cc2.txt`,
**outside the repository, never committed, never copied in**. Printed page =
PDF page − 37 (front matter, roman-numbered, comes first). Every page in this
document is a printed page, as the book's index and cross-references give it.

Two helpers sit beside it, in `…/scratchpad/tools/`, and print only short
matches, never stretches of the text:

- `ccbook.py <regex>` prints each matching line as `printed page | line`
  (truncated at 150 characters). An author greps the text with it; **nobody
  reads the extraction whole, and nothing from it enters the repository
  beyond the quotations §E.3 allows.**
- `cc_quotes.py <file>` checks lines `tag|page|quote` against that page and
  the next (joining lines, allowing for end-of-line hyphenation) and prints
  OK, LOOSE or MISSING with the word count. All 41 opening quotations in §C
  were checked with it: 40 are OK; one (§C 3.4's, p. 295) is LOOSE only
  because a margin note sits beside it in the extraction, and it was checked
  by eye.

What the text settled: every page and section title in §B and §C; every
figure in §S.2 (each now with its page; no `# verify` remains); the sources
in §S.1; and the opening quotation of every lesson. If the orchestrator moves
the extraction, it records the new route in `docs/code-complete/AUTHORING.md`;
the route never goes in a lesson.

### E.3 Quoting

*Code Complete* is in copyright (Steve McConnell, 2004). The Subject is
commentary, and keeps quotation smaller than the earlier read-alongs, because
a practical handbook's value is in its formulations:

- A lesson may open with **one quotation of at most 40 words**, cited by page,
  and only where the sentence is the chapter's own summary of its argument.
  §C's **Quote** line gives each lesson's, with its page and word count; an
  author who uses another records it there and checks it with `cc_quotes.py`.
  A lesson's quotations total at most **60 words**, the opening one
  included. No lesson's argument depends on a quotation.
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
- This specification quotes the book only in §C's **Quote** lines (41
  quotations, 10 to 35 words each) and in a handful of phrases of two to
  five words in §C and §S.2 that identify a claim ("grossly optimistic").
  Nothing else here is the book's wording.

### E.4 The author's checklist

The per-lesson procedure of `docs/philosophy/PLAN.md` §E, with
`python3 scripts/preview_subject.py code-complete --course <slug> --out <dir>`
to render, and these additions:

1. Open with §C's **Quote** (or none), set as the first body block with its
   page in a comment beside the dict; then the chapter's argument in the
   lesson's own words. Every figure attributed to the book carries its §S.2
   id and page in a comment beside the dict (`# F17, p. 470`).
2. Every code block is one of §D.4's snippets or a new one written for the
   lesson; never the book's. A snippet is **one Python constant** in the
   course module, used by the lesson's `code` block and by the preset's cfg;
   the test `test_code_complete_presets_use_the_lessons_snippets` asserts
   that each `code` lab preset's code is the text of a `code` block on the
   same page or a named exercise constant. A new snippet is run through the
   reference model (or the built lab) and its figures recorded in §C.
3. Every preset id appears in a body `p` with the figures it shows; every tile
   a view prints is explained in prose at least once in the course.
4. The exercise (§B) is an `h3` "Exercise", a `code` block (or a small
   table), and a `p` that says what to find. Its answer, §C's **Answer**, is
   the `why` of one quiz item that asks for it, and appears nowhere else on
   the page; `worked` works a preset, never the exercise.
5. **Quiz items** (3–4 per lesson). Each item's options differ by a fact the
   reader can check: a row of a truth table, an integer, a line number, a
   section's claim. Never quiz a verdict ("is this routine too complex?");
   when an item turns on a rule (the decision-point rule, the barricade
   rule), the stem states the rule or names the section. A figure from the
   book is asked only as §S.2 settles it, with its source in the `why`.
   Distractors are the misconceptions of §C, or the off-by-one of the
   correct answer, never a joke option.
6. The last of the `steps` is §C's **Own:** line: an instruction with an
   observable result, applied to the reader's own code or records.
7. **Length.** `body` stays within 7–18 blocks (a `code` block counts as
   one); a lesson whose chapter span needs more is split in this document
   first, never padded or crammed. As a guide, one `p` per two sections the
   lesson covers, plus the quotation, the lab's paragraphs and the exercise.
   §C's minutes are the author's estimate of reading time at that length,
   and a lesson that would read past 20 minutes is shortened.
8. Inline code in prose is a backtick run and stays short: an identifier, a
   condition, a call. A statement longer than about 40 characters goes in a
   `code` block.
9. `/usr/bin/python3 scripts/speechcheck.py` with the code dialect on (§H.1),
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
   its sections in order, with their pages. §C's opening quotation, at most
   40 words, precedes the paraphrase where it is used (§E.3).
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
   without `goto`); Structured Basis Testing (test-first, which McConnell
   calls one of the most beneficial practices of its decade, §22.2, p. 504,
   and what it became in test-driven development: a continuation of the
   book's advice, not a view against it); Programming Tools (continuous
   integration, build systems); Self-Documenting Code (the comment debate).
   Never "this advice is outdated" or "modern developers know better" in the
   lesson's voice. The view named here is never a lesson's `mistakes[0]`
   (§C, "Misconceptions").
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

> You have probably written a routine like `auditShipments`: three
> declarations at the top, set to zero, and then the work, a screen further
> down. It looks tidy, and McConnell's measure says what it costs. A variable
> is live from the first line that mentions it to the last, and every line in
> between is a line on which a reader has to remember what it holds. Count it
> for `heaviestKg`: declared on line 3, used on lines 13 and 18, so it is live
> for 18 − 3 + 1 = 16 lines, and the nine lines between its declaration and
> its first use have nothing to do with it. Move each declaration down to the
> loop that uses it and the lab's average live time over the three variables
> falls from 41/3, about 13.7 lines, to 23/3, about 7.7, with not a statement
> changed. Nothing about the program's behaviour is different; what is
> different is how much of it you have to hold in your head at once, which is
> the complexity Chapter 5 said was the thing to manage.

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

## §S Sources, and the register of figures

### S.1 Sources the lessons may cite

Cited by author and year in prose; never quoted at length. Every work here
except the first is cited **as the book cites it**: the lesson says "the book
cites Fagan 1976", not "Fagan found". Each was checked against the book's
text and bibliography (pp. 863–884) with `ccbook.py`: every work below is
cited by the book under the year given, except where a note says otherwise.
Titles are given where the bibliography gives them and they were confirmed;
a lesson needs only author and year.

- McConnell, S. (2004). *Code Complete: A Practical Handbook of Software
  Construction*, 2nd ed. Microsoft Press. The source of every lesson.
- Basili, V. R., Briand, L. C. and Melo, W. L. (1996). A validation of
  object-oriented design metrics as quality indicators. *IEEE Transactions on
  Software Engineering* 22(10).
- Basili, V. R. and Perricone, B. T. (1984). Software errors and complexity:
  an empirical investigation. *Communications of the ACM* 27(1).
- Beck, K. (2003). *Test-Driven Development: By Example*. Addison-Wesley.
- Boehm, B. W. (1981). *Software Engineering Economics*. Prentice Hall.
- Boehm, B. W. (1987b). Industrial software metrics top 10 list. *IEEE
  Software* 4(5). The book's "1987b".
- Boehm, B. W. et al. (2000). *Software Cost Estimation with COCOMO II*.
  Prentice Hall.
- Boehm, B. and Turner, R. (2004). *Balancing Agility and Discipline*.
  Addison-Wesley.
- Böhm, C. and Jacopini, G. (1966). Flow diagrams, Turing machines and
  languages with only two formation rules. *Communications of the ACM* 9(5).
- Brooks, F. P. (1995). *The Mythical Man-Month*, anniversary edition.
  Addison-Wesley. The book cites the 1995 edition for Brooks's law (p. 676).
- Brooks, F. P. (1987). No silver bullet: essence and accidents of software
  engineering. *Computer* 20(4).
- Card, D. N., Church, V. E. and Agresti, W. W. (1986). An empirical study of
  software design practices. *IEEE Transactions on Software Engineering*
  12(2).
- Card, D. N. and Glass, R. L. (1990). *Measuring Software Design Quality*.
  Prentice Hall.
- Cobb, R. H. and Mills, H. D. (1990), as the book cites them (F19).
- Cusumano, M. et al. (2003), as the book cites them (F25).
- Dijkstra, E. W. (1968). Go To statement considered harmful (letter).
  *Communications of the ACM* 11(3).
- Dunn, R. H. (1984). *Software Defect Removal*. McGraw-Hill.
- Fagan, M. E. (1976). Design and code inspections to reduce errors in
  program development. *IBM Systems Journal* 15(3).
- Fowler, M. (1999). *Refactoring: Improving the Design of Existing Code*.
  Addison-Wesley.
- Freedman, D. P. and Weinberg, G. M. (1982), as the text cites them on
  p. 581 (F21); the bibliography lists the 1990 edition of their *Handbook of
  Walkthroughs, Inspections, and Technical Reviews*.
- Gorla, N., Benander, A. C. and Benander, B. A. (1990). Debugging effort
  estimation using software metrics. *IEEE Transactions on Software
  Engineering* 16(2).
- Gould, J. D. (1975). Some psychological evidence on how people debug
  computer programs. *International Journal of Man-Machine Studies* 7.
- Jones, C. (1977), as the book cites him (F24).
- Jones, C. (1986a). *Programming Productivity*. McGraw-Hill.
- Jones, C. (1996). Software defect-removal efficiency. *Computer* 29(4).
- Jones, C. (1998). *Estimating Software Costs*. McGraw-Hill.
- Jones, C. (2000). *Software Assessments, Benchmarks, and Best Practices*.
  Addison-Wesley.
- Kaplan (1995) and Moore (1992): cited in the text (pp. 472–473, 521) and
  absent from the bibliography; cite them "as the book cites them", with no
  title.
- Knuth, D. E. (1971). An empirical study of FORTRAN programs. *Software:
  Practice and Experience* 1(2).
- Knuth, D. E. (1974). Structured programming with go to statements.
  *Computing Surveys* 6(4).
- Ledgard, H. and Tauer, J. (1987a). *C With Excellence: Programming
  Proverbs*. Hayden.
- Liskov, B. (1988). Data abstraction and hierarchy. *SIGPLAN Notices*
  23(5). Confirmed (p. 144 and the bibliography).
- Marca, D. (1981). Some Pascal style guidelines. *SIGPLAN Notices* 16(4).
- McCabe, T. J. (1976). A complexity measure. *IEEE Transactions on Software
  Engineering* SE-2(4).
- Miara, R. J., Musselman, J. A., Navarro, J. A. and Shneiderman, B. (1983).
  Program indentation and comprehensibility. *Communications of the ACM*
  26(11). The book spells the first author "Miaria" (p. 737 and the
  bibliography); the lessons use the correct spelling and say nothing of it.
- Miller, G. A. (1956). The magical number seven, plus or minus two.
  *Psychological Review* 63(2).
- Myers, G. J. (1976). *Software Reliability*. Wiley.
- Myers, G. J. (1978b), as the book cites him (F17).
- Myers, G. J. (1979). *The Art of Software Testing*. Wiley.
- Parnas, D. L. (1972). On the criteria to be used in decomposing systems
  into modules. *Communications of the ACM* 15(12).
- Putnam, L. H. and Myers, W. (1992). *Measures for Excellence*. Yourdon
  Press; and (1997) *Industrial Strength Software*. IEEE Computer Society
  Press. The book spells the second author "Meyers" in its citations.
- Riel, A. J. (1996). *Object-Oriented Design Heuristics*. Addison-Wesley.
- Rittel, H. and Webber, M. (1973). Dilemmas in a general theory of
  planning. *Policy Sciences* 4. Wicked problems, as the book cites them
  (p. 74).
- Sackman, H., Erikson, W. J. and Grant, E. E. (1968). Exploratory
  experimental studies comparing online and offline programming performance.
  *Communications of the ACM* 11(1).
- Shen, V. Y. et al. (1985), as the book cites them (F8).
- Shull, F. et al. (2002). What we have learned about fighting defects.
  *Proceedings of the 8th International Software Metrics Symposium*.
- Stevens, W. P., Myers, G. J. and Constantine, L. L. (1974). Structured
  design. *IBM Systems Journal* 13(2).
- Weinberg, G. M. (1983), as the book cites him (F21).
- Yourdon, E. (1986a). *Managing the Structured Techniques*. Yourdon Press;
  and (1986b) *Nations at Risk*. Yourdon Press.

Added for Software Craftsmanship (Course 7), each as the book cites it on
the page given: Chase, W. G. and Simon, H. A. (1973), "Perception in chess"
(p. 733); Shneiderman, B. (1976), "Exploratory experiments in programmer
behavior" (p. 734); Fjelstad, R. K. and Hamlen, W. T. (1979), the IBM
maintenance study (p. 788). Two works outside the book, named only in Self-
Documenting Code's §F.4 aside and not cited by the book: Martin, R. C.
(2008), *Clean Code*, Prentice Hall; Ousterhout, J. (2018), *A Philosophy of
Software Design*, Yaknyam Press.

Dropped in review, because the book does not cite them: Feldman 1979 (`make`)
and Goldberg 1991 (floating point). Simon 1996 is cited in Chapter 5 for
another point and is not the source of "wicked problems".

### S.2 The register of figures

Every figure a lesson attributes to the book is listed here with the value
the book gives, its printed page and the sources the book names. Each was
settled against the text (the accuracy review's §S.2 table, then the text
itself). A lesson prints the figure with a comment `# F<n>, p. <page>` beside
the dict; there is no `# verify` marker left to grep for. A figure not in
this table is not attributed to the book.

| id | claim as the lesson uses it | the book's value | where (printed page) | sources the book names |
| --- | --- | --- | --- | --- |
| F1 | share of a project's time construction takes | 30 to 80 percent of the total time, depending on size; as much as 65% on small projects, about 50% on medium | §1.2, p. 7; §27.5, p. 654 | the book's synthesis |
| F2 | construction errors as a share of all errors | at least 35% of all defects regardless of size; 45–75% even on the largest projects (Figure 22-2); about 75% on small projects, about 50% on larger | §22.4, pp. 520–521; §27.3, p. 652 | Grady 1987 and others as cited there |
| F3 | relative cost of fixing a defect by phase introduced × phase detected | requirements: 1, 3, 5–10, 10, 10–100; architecture: 1, 10, 15, 25–100; construction: 1, 10, 10–25 (detected at requirements, architecture, construction, system test, post-release); the table's example, an architecture defect costing $1,000 at architecture and $15,000 in system test; on smaller projects the post-release multiplier for a requirements error is closer to 5–10 than 100 | §3.1, Table 3-1, p. 29; §3.4, p. 39 for smaller projects | Fagan 1976; Humphrey, Snyder and Willis 1991; Leffingwell 1997; Willis et al. 1998; Grady 1999; Shull et al. 2002; Boehm and Turner 2004; Dunn 1984 |
| F4 | statements equivalent to one C statement | C 1, C++ 2.5, Fortran 95 2, Java 2.5, Perl 6, Python 6, Smalltalk 6, Visual Basic 4.5 | §4.1, Table 4-1, p. 62 | Jones 1998; Boehm 2000; Prechelt 2000 |
| F5 | productivity with experience in the language | about 30% higher with three or more years | §4.1, p. 62 | Boehm et al. 2000 (Cocomo II) |
| F6 | a class's data members | consider decomposing above about seven | §6.3, pp. 143–144 | Miller 1956; Riel 1996 |
| F7 | depth of inheritance | Riel suggests six levels; McConnell calls that "grossly optimistic" — most people manage two or three; deep trees significantly associated with fault rates | §6.3, p. 147 | Riel 1996; Basili, Briand and Melo 1996 |
| F8 | routine length | allow growth up to 100–200 lines (a line being non-comment, non-blank); take care past 200 | §7.4, pp. 173–174 | Basili and Perricone 1984; Shen et al. 1985; Card, Church and Agresti 1986; Card and Glass 1990; Selby and Basili 1991; Lind and Vairavan 1989; Jones 1986a |
| F9 | number of parameters | limit to about seven | §7.5, p. 178 | Miller 1956 |
| F10 | span and live time | span = lines between references; average span = mean of the spans; live time = first through last reference, inclusive; the listing's numbering includes the comment line | §10.4, pp. 245–248 | the book's own; the lab's pooled average over several variables is the lab's extension |
| F11 | variable-name length | debugging effort lowest when names average 10–16 characters; 8–20 almost as good. A program-wide average, not a per-name rule | §11.1, p. 262 | Gorla, Benander and Benander 1990 |
| F12 | literals in a program's body | only 0 and 1 | §12.1, p. 292 | the book's own |
| F13 | loop length and nesting | one screen or one page; rarely longer than 15 or 20 lines; limit nesting to three levels | §16.2, p. 385 | Yourdon 1986a |
| F14 | decision points and what to make of them | 1 + if, while, repeat, for, and, or (or their equivalents) + each case; 0–5 probably fine, 6–10 start to think about simplifying, 10+ break part of the routine out | §19.6, Table 19-2, p. 458 | McCabe 1976 |
| F15 | depth of nesting a reader can follow | few people understand more than three levels of nested `if`s; many recommend no more than three or four | §19.4, p. 445 | Yourdon 1986a (after Chomsky and Weinberg); Myers 1976; Marca 1981; Ledgard and Tauer 1987a |
| F16 | defect-detection rates (lowest, modal, highest) | informal design reviews 25/35/40; formal design inspections 45/55/65; informal code reviews 20/25/35; formal code inspections 45/60/70; modelling or prototyping 35/65/80; personal desk-checking 20/40/60; unit test 15/30/50; new-function test 20/30/35; integration test 25/35/40; regression test 15/25/30; system test 25/40/55; low-volume beta 25/35/40; high-volume beta 60/75/85 | §20.3, Table 20-2, p. 470 | Jones 1986a, 1996; Shull et al. 2002 |
| F17 | combining techniques | modal rate never above 75%, average about 40%; unit, functional and system testing together often under 60%; test-heavy organisations about 85%, leading ones 95% or more; Table 20-3 multiplies the rates for Extreme Programming's practices to about 74/90/97% | §20.3, pp. 470–472, Table 20-3 p. 472 | Jones 2000; Myers 1978b |
| F18 | hours per defect, inspection against testing | IBM: 3.5 staff-hours to *find* a defect by inspection against 15–25 by testing; Microsoft: about 3 hours to *find and fix* by inspection against 12 by testing | §20.3, pp. 472–473 | Kaplan 1995; Moore 1992 (as the book cites them) |
| F19 | errors to expect | industry average 1–25 per thousand lines delivered; Microsoft 10–20 in-house, 0.5 released; cleanroom 3 in-house, 0.1 released; 80% of errors in 20% of classes or routines; 50% in 5% | §22.4, pp. 517, 521 | Moore 1992; Cobb and Mills 1990; Endres 1975; Gremillion 1984; Boehm 1987b; Shull et al. 2002; Jones 2000 |
| F20 | variation among programmers in debugging | fastest against slowest: 5.0 against 14.1 minutes; defects not found 0.7 against 1.7; defects made while correcting 3.0 against 7.7 | §23.1, p. 537 | Gould 1975 |
| F21 | small changes and errors | the chance of a bad change rises from one to five lines, then falls: small changes are more error-prone than larger ones; reviewing one-line changes cut their error rate from 55% to 2%; a first attempt at a change is wrong more than half the time | §24.4, pp. 580–581, Figure 24-1 | Weinberg 1983; Freedman and Weinberg 1982; Yourdon 1986b |
| F22 | the Pareto principle in performance | 20% of routines take 80% of the time; under 4% of a program accounts for more than 50% of its run time | §25.2, p. 592 | Boehm 1987b; Knuth 1971 |
| F23 | measured effect of a tuning technique | the busiest-loop example: outer 100 and inner 5 against the reverse, 600 against 505 iterations (about 16%), measured savings 33% C++, 34% Java, 12% PHP, 4% Python; other techniques' per-language timings through Chapter 26 | §26.2, p. 623; §§26.1–26.7 | the book's own measurements |
| F24 | defect density by project size | under 2K lines 0–25 per KLOC; 2K–16K 0–40; 16K–64K 0.5–50; 64K–512K 2–70; 512K or more 4–100 | §27.3, Table 27-1, p. 652 | Jones 1977; Jones 1998 |
| F25 | productivity by project size (lines per staff-year) | 1K: 2,500–25,000; 10K: 2,000–25,000; 100K: 1,000–20,000; 1M: 700–10,000; 10M: 300–5,000 (Cocomo II nominal 4,000 / 3,200 / 2,600 / 2,000 / 1,600) | §27.4, Table 27-2, p. 653 | Putnam and Myers 1992, 1997 (the source line under the table misprints "Meyers"; the bibliography, pp. 878–879, gives Ware Myers); Boehm et al. 2000; Cusumano et al. 2003 |
| F26 | effort factors | Table 28-1 prints percentages: programmer capability −24%/+34%; requirements analyst capability −29%/+42%; product complexity −27%/+74%; time constraint 0/+63%; storage constraint 0/+46%; use of software tools −22%/+17%; personnel continuity −19%/+29%. As multipliers: 0.76–1.34, 0.71–1.42, 0.73–1.74, 1.00–1.63, 1.00–1.46, 0.78–1.17, 0.81–1.29 | §28.3, Table 28-1, p. 674 | Boehm et al. 2000 |
| F27 | indentation | subjects scored 20–30% higher on comprehension with two-to-four-space indentation than with none; six spaces scored second lowest | §31.2, p. 737 | Miara et al. 1983 |
| F28 | comment density | about one comment per ten statements gave the highest clarity; both fewer and more reduced understandability | §32.4, p. 792 | IBM studies, via Jones 2000 |
| F29 | differences among programmers | about 10 to 1 in productivity among programmers with the same experience | §28.5, p. 682; §33.1, p. 820 | Sackman, Erikson and Grant 1968 and later studies as the book cites them |
| F30 | time spent upstream | a well-run project devotes about 10 to 20 percent of its effort and about 20 to 30 percent of its schedule to requirements, architecture and up-front planning | §3.6, p. 55 | McConnell 1998; Kruchten 2000 |

Where a lesson uses a figure whose original is better known than the book's
citation of it (a COCOMO II multiplier, Jones's rates), the lesson uses the
book's figure (it is a read-along); where the original differs, the `note`
may say so, citing the original by author and year.

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
  The block may carry an optional set of marked lines, drawn in the gutter
  with a glyph and a visually hidden word ("flagged"), never by colour alone
  (the layout lesson marks its mis-indented lines; pedagogy #31).
- **R2 — a code dialect for the read-out.** `speech.say_code(line)`: `&&`
  "and", `||` "or", a prefix `!` "not", `==` "equals", `!=` "is not equal
  to", `=` "is set to" (in a statement), `+=` "is increased by", `++` "is
  incremented", `--` "is decremented", `[i]` "at index i", braces and
  semicolons silent, a string literal read as its text; everything else
  through `speech.say`. Added in review (pedagogy #30), before the dialect
  is built:
  - **line numbers spoken**: a `code` block is read line by line, each
    announced by its number ("line 14: …"), as the `math` table block
    announces a table, because every lesson's prose names lines by number
    and the visible numbers are a CSS counter the read-out cannot see;
    blank lines are skipped and their numbers not announced;
  - `%` "mod" (not "percent"); `[]` in a type, "array of" (`double[]
    prices` → "array of double prices"); `.` between identifiers "dot";
  - a negative literal "minus" (`-1.0` → "minus one point zero"), and a
    binary `-` "minus";
  - `System.out.println` "print line" (and `System.out.print` "print");
  - camelCase and `UPPER_SNAKE` identifiers split into words (`isDomestic`
    → "is domestic", `MAX_RETRIES` → "max retries");
  - Java keywords and primitive types read as words from a fixed list
    (`int` "int", `for` "for", `new` "new", `void` "void", `char` "char",
    `boolean` "boolean", `static` "static", `final` "final"), so that a
    three-letter word at the head of a line is never spelt out.

  Applied to every line of a `code` block, and — on a
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
  58 characters (§B; unchanged by the review's re-split, since the longest
  slug is still `design-heuristics-and-information-hiding`, 40).
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
- A new test, `test_code_complete_presets_use_the_lessons_snippets` (with
  the Subject's other content tests): for every `cckit` lab of mode `code`,
  each preset's `code` equals the joined lines of a `code` block on the same
  lesson or a named exercise constant of the course module (§D.4, §E.4
  item 2).
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
  The review's re-split (Chapter 8 into two, Chapters 1 and 2 into one) kept
  the total at 41, so no count below changed.
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

The specification was reviewed before authoring by two models independently:
a pedagogy review (the `pedagogical-expert` brief;
`docs/reviews/code-complete-spec-pedagogy-review.md`, findings #1–#34) and
an accuracy review that checked every claim about the book, every §S.2 figure
and every pinned tile against the text and a recomputation
(`docs/reviews/code-complete-spec-accuracy-review.md`: MF-1 to MF-6, SF-1 to
SF-13, C-1 to C-13). Both were reconciled in one pass, with the book's text
in hand, which also settled every page, section title, §S.2 figure and
opening quotation. Each course is reviewed again after authoring
(`docs/code-complete/SECOND-REVIEW.md`).

**Owner decisions recorded with the reconciliation:** title "Code Complete,
Read Along" (§A); Java (§D.0); catalog placement last in the computing group
with the note in §H.3.

**Lesson count after review: 41**, unchanged. Chapter 8 is split in two and
Chapters 1 and 2 share one lesson (pedagogy #20, #21 option (a)); Course 1
has 3 lessons and Course 2 has 9. §A's sentences, §B's table and part files,
the check ids (longest still 58) and §H.3's counts are consistent with it.

### R.1 Pedagogy review

| # | finding | what was done |
| --- | --- | --- |
| 1 | must-fix: `reasons-to-create-a-routine`'s exercise repeats the worked example; cohesion untaught | Done. The exercise is a cohesion classification of six routine descriptions, with the weakest split in two; a second exercise on a fresh `printSummary` snippet (§D.4); presets reordered so `two-names`, the lab's limit, comes last, with "the lab cannot see this copy; you can". |
| 2 | must-fix: `access-routines` reaches 0 coupled pairs by deleting the callers | Done. The preset keeps all six routines and adds `owners`; `dgCoupled` stays 9, and the new `dgDirectAccess` (10 → 3) and `dgWriters` show what moves. "Access routines remove the coupling" is the lesson's `mistakes[1]`. |
| 3 | must-fix: the own-code step is promised for 41 lessons, specified for 18 | Done. Every §C entry has an **Own:** line; §B and §E.4 item 6 make it the last `step`, phrased as an act with an observable result. |
| 4 | should-fix: review and debugging lessons have exercises where nothing is done | Done. Collaborative Construction's exercise is `countPassing` read as an inspection (three planted defects); Debugging as Science's is `overtime`'s out-of-bounds read when `count` exceeds `staff.length`, worked by hypothesis and halving. |
| 5 | should-fix: exercises without a determinate answer | Done. Every exercise has an **Answer** computed by the reference model, including the layered design, the moved declarations and the parameter-passing rewrite of `printQuote`. |
| 6 | should-fix: the overflow exercise cannot be checked in the lab | Done. The exercise adds 3,000,000 a thousand times in an `int` (Java prints `-1294967296`); the Standard asks for direction and fix, not a wrapped value by hand; `msPerYear` stays as prose. |
| 7 | should-fix: `expireSessions`'s obvious fix throws | Done. The exercise's second half asks whether the one-line fix is right; the answer names `ConcurrentModificationException` and the `Iterator`. |
| 8 | should-fix: exercises that are arithmetic where the chapter has an act | Done for all four: programming *into* a language (Key Construction Decisions), a guard-clause rewrite of `refundAmount` (Unusual Control Structures), hoisting a loop-invariant call (Code-Tuning Techniques), the chain with no final `else` (Using Conditionals). |
| 9 | should-fix: `language`'s `rate` makes a decorative tile | Done. `rate`, `pjDays` and `pjDaysC` removed; one tile, `pjEquivalent`; the caveat is prose. |
| 10 | should-fix: the removal product cannot show "unlike techniques" | Done. The refutation says what the product shows (no single stage at modal rates reaches the target); the `note` says "unlike" is the chapter's claim from Jones's data, which independence cannot test. |
| 11 | should-fix: the pipeline makes inspection cheap by construction | Done. The `note` names the hours-per-defect-found assumption; preset labels say "as the book reports them"; the refutation leans on F18. |
| 12 | should-fix: `coDensity`'s denominator is not the study's | Done. `coStatements` added; density is comment lines over statement lines (§D.1); figures recomputed (`comments-repeat` 100%, `comments-intent` 20%, `isLeapYear` 100%). |
| 13 | should-fix: the speedup view lacks the Pareto tile | Done. `speedup` gains `pfPareto` ("2 of 4" on the lesson's profile). |
| 14 | consider: labs that count the obvious | Partly taken. `pjSpread` added to `scale`; the class exercise groups the `Kiosk`'s six public routines; Course 1's ripple lab is said to test the metaphor's prediction only. Kept as they are: `deps/tree` depth, the parameter count and `breakeven`, which the review itself rated acceptable. |
| 15 | must-fix: the §F.4 aside sits in `mistakes[0]` | Done. Upstream Prerequisites' misconception is the misreading of the cost table §3.2 refutes; Routine Length's is the §7.6 function-with-side-effects error; the later views go in the `note`. §C's preamble and §F.4 state the rule. |
| 16 | must-fix: "the compiler catches uninitialised variables" is true in Java | Done. The misconception is "if it compiles, every variable holds the value you meant", refuted by `set-twice` and by a field read before any set; the exercise says `javac` rejects its path-sensitive case and the lab, like C, reads top to bottom. |
| 17 | should-fix: straw men and holders | Done for all six: the writing metaphor; "a practice your language has no keyword for is unavailable"; "design is a phase that ends when coding begins"; "indentation is cosmetic"; "integration is a phase at the end"; "an estimate is a number", with Brooks's law as `mistakes[1]`. |
| 18 | should-fix: refutations leaning on illustrative instances | Done. §C's preamble rule; the entries say "on the lesson's illustration". |
| 19 | consider: misconceptions readers arrive with | Partly taken: "a count of 11 means the routine is bad" (Nesting and Complexity) and "`i` after the loop is its last value" (Controlling Loops) are `mistakes[1]`. **Declined:** the named-constants over-application ("even the `2` in `/ 2`") as a misconception, because the book itself says to replace even "safe" literals with named constants (pp. 308–309) and calls for being a fanatic about it; refuting it would refute the book. The lesson may say that this is where readers disagree with McConnell. |
| 20 | should-fix: Chapter 8 carries two ideas | Done, with one deviation. Split into `assertions-and-error-handling` (§§8.1–8.3; `cond/range` with never-fires / always-fires presets) and `exceptions-and-barricades` (§§8.4–8.8; the new `cond/barricade` and the nine-value classification). The review put the barricade lab in the first lesson; it goes in the second, because the barricade and its assertion rule are §8.5 (pp. 203–205), which the second lesson reads. |
| 21 | consider: where to find the 42nd slot | Taken, option (a): Chapters 1 and 2 share `construction-and-its-metaphors`; total stays 41. |
| 22 | should-fix: guard clauses taught in the wrong lesson | Done (with #8): Unusual Control Structures' exercise is the `refundAmount` rewrite; Nesting and Complexity counts the transformation again. |
| 23 | consider: `cond/range` used twice for one skill | Taken: resolved by #20; the first use is the `&&`/`||` confusion, the second boundary analysis. |
| 24 | consider: minutes | Taken as a rule (§E.4 item 7): one `p` per two sections as a guide; minutes are the author's estimate, and a lesson past 20 minutes is shortened. |
| 25 | consider: the body-block ceiling | Taken: 7–18 kept, not raised; a chapter that needs more is split in this document first (§E.4 item 7). The split of Chapter 8 removes the heaviest case. |
| 26 | should-fix: distractors that are also true | Done: §E.4 item 5 (distractors differ on a truth-table row or an integer; never quiz a verdict; state the rule in the stem; figures only as §S.2 settles them). |
| 27 | should-fix: line numbers depend on identical snippets | Done: one Python constant per snippet, used by body and preset, and a test (§D.4, §E.4 item 2). |
| 28 | the voice contract; four places lean | Done: (a) per #15, #18; (b) "the lab cannot see this; you can" in both places; (c) per #11; (d) `footer_lead` keeps "a count says where to look"; `coBand` prints "10+". |
| 29 | consider: snippets that teach a habit silently | Taken: `overtime`'s no-op replaced by `// exempt staff earn no overtime` (basis count still 5); the shipping lesson may say a clause on `-1.0` as a sentinel; the free-slot lesson may name the "// return -1" step as pseudocode at the level of the language. |
| 30 | should-fix: R2 reads a listing without its line numbers | Done: §H.1 R2 additions (line numbers spoken, `%`, `[]`, `.`, negative literals, `println`, camelCase, keywords as words). Filed for the renderer task. |
| 31 | should-fix: the layout lesson is invisible to a listener | Done: the body states the binding in words, the `note` says the evidence is visual; flagged lines carry a gutter marker, not colour alone (§D.0, §H.1 R1). |
| 32 | consider: two listings on a phone; two depth conventions | Taken: the listing stacks under the textarea below 40em and scrolls in its own box; the depth convention is stated in §D.0 and in the `complexity` banner. |
| 33 | should-fix: "answer never on the same screen" is unenforceable | Done: the answer is the `why` of one quiz item, and `worked` works a preset (§B, §C format, §E.4 item 4). |
| 34 | consider: Standards that measure the count rather than the act | Taken: the Standards of `inheritance-containment-and-members` and `design-heuristics-and-information-hiding` measure the act (whether the subclass substitutes and why; the secret named). |

### R.2 Accuracy review

| id | finding | what was done |
| --- | --- | --- |
| MF-1 | four instances adapt the book's own examples | Done: `auditShipments` replaces the live-time listing; an abstract `Kiosk` replaces the `Program` class; a parcel quote (`shippingQuote`, `printQuote`) replaces the expense ordering; a late-fee table (`7, 0; 14, 2; 30, 5; 60, 10; 365, 20`) replaces the grade breakpoints. All recomputed. |
| MF-2 | `testing-only`'s 72.7% contradicts the book's "less than 60 percent" | Done: the lesson sets the book's figure (p. 471, again p. 500) beside the product, and says the product of modal rates is not what the book reports for testing alone. F17 extended. |
| MF-3 | the Square/Rectangle exercise does not break | Done: `Square` overrides both setters, and the caller expecting 20 gets 25. |
| MF-4 | `kitchen-sink`'s misconception contradicts its tile | Done: rewritten against the `Kiosk` figures (2 public fields, 6 public routines). |
| MF-5 | two class snippets exceed the line limit | Done: `private-fields` 20 lines, `kitchen-sink` 18. |
| MF-6 | `arith` refuses zero, and its own preset | Done: zero is a valid `double`; only division by zero, overflow to infinity and subnormal results are refused, with the stated sentence (§D.1). |
| SF-1 | Chapter 11 section numbers | Done: §§11.1–11.7 as printed. |
| SF-2 | the 0-and-1 rule is §12.1 | Done (F12). |
| SF-3 | F29 is in §28.5 and §33.1 | Done. |
| SF-4 | Routine Length's worked line miscounts | Done: "seven of which describe the line or its tax". |
| SF-5 | `expireSessions`'s obvious fix | Done (pedagogy #7). |
| SF-6 | `loop`'s closed form at the edges and against Java | Done: start = bound gives 0; a wrong-way step "never ends without overflow"; `ne` decided against wrap-around by gcd(step, 2³²) (§D.1). |
| SF-7 | `nuJava` formatting contradicts §D.0 | Done: `nuJava` is ASCII, ungrouped, as Java prints; `nuExact` follows §D.0. |
| SF-8 | zero denominators unspecified | Done: §D.0 "Zero denominators". |
| SF-9 | three pinned tiles without values | Done: `total-first`'s `coDeps` (recomputed on the new snippet), `everything-talks`' `dgFanIn` "billing 4" and `shallow`'s `dgDeepest` "Circle", ties named in the banner. |
| SF-10 | `range` must evaluate each literal itself | Done (§D.1, `ccref.py`). |
| SF-11 | register corrections | Done: F2, F3, F7, F8, F16, F17, F18, F21, F25, F26, F28 as the review gives them (§S.2). |
| SF-12 | the busiest-loop preset is the book's example | Done: labelled the book's example (F23, p. 623), not illustrative; `three-levels` and the exercise are the lesson's own. |
| SF-13 | sources the book does not cite | Done: Feldman 1979 and Goldberg 1991 dropped; Brooks 1995; Boehm 1987b; Miara's spelling noted; Rittel and Webber 1973 for wicked problems; the listed works added; Kaplan 1995 and Moore 1992 "as the book cites them" (§S.1). |
| C-1 | the ternary operator | Taken: the kit's choice not to count `?:`, worded as the kit's choice in the banner (§D.1). |
| C-2 | band boundary at 10 | Taken: "10+" printed; 10 in "6–10", said in the banner. |
| C-3 | the book's own point for the nesting misconception | Taken: cited (p. 458). |
| C-4 | test-first is endorsed | Taken: §F.4 and Structured Basis Testing frame TDD as a continuation. |
| C-5 | compile errors the lessons can use | Taken in Declaring and Initializing and Organizing Straight-Line Code. |
| C-6 | data-flow anomalies come from §22.3 | Taken: cited where `dataflow` is introduced. |
| C-7 | metaphors: McConnell rejects writing and farming | Taken in the merged Course 1 lesson's Read line. |
| C-8 | lesser overlaps (character classes; overtime) | Taken: `search/chain` classifies HTTP responses; `overtime` kept, as the review allows. |
| C-9 | `access-routines` drops the callers | Taken (pedagogy #2). |
| C-10 | `nuJava` for `double` and JDK versions | Taken: "as JDK 19 or later prints it", Java's form named (§D.1). |
| C-11 | `factorial` beyond `long` | Taken: `factorial` capped at 20. |
| C-12 | Bentley's square-root case | **Declined as an exercise:** it is the book's own example (p. 592), and MF-1's principle keeps the book's examples out of the exercises; the lesson may cite it in prose with its figures. The exercise uses the lesson's own profile. |
| C-13 | the effort misconception asserts what the lab cannot compute | Taken: "an estimate is a number", refuted by the product's range; Brooks in `mistakes[1]` in prose. |

### R.3 Settled from the text

Beyond the reviews: every page and section title in §B and §C; F1–F29
settled and F30 added (§3.6, p. 55); the Key Points page of each chapter
(the source of most opening quotations); p. 377's advice against relying on
the loop index after the loop (Controlling Loops); p. 295's 0.1-added-ten-times
example, which the `tenth-ten-times` preset therefore labels as the book's
example; basis testing on pp. 505–509 and data-flow testing from p. 509 (the
Chapter 22 split); and Freedman and Weinberg cited as 1982 in the text and
1990 in the bibliography.
