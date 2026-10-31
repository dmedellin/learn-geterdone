# Patterns of Enterprise Application Architecture, Read Along — the build specification

This is the curriculum, lab and authoring contract for the fourteenth Subject:
a read-along of Martin Fowler, with David Rice, Matthew Foemmel, Edward
Hieatt, Robert Mee and Randy Stafford, *Patterns of Enterprise Application
Architecture* (Boston: Addison-Wesley, 2002; ISBN 0-321-12742-0). The book is in
two parts: eight narrative chapters (Part 1) that set out the problems of
building an enterprise application, and ten chapters of patterns (Part 2) that
the narratives point to. The Subject reads them together: each lesson pairs a
narrative chapter, or a section of one, with the Part 2 patterns it introduces,
so the reader meets the problem and the pattern on the same page. It has seven
courses and 44 lessons.

Every lesson is applied. The reader reads the argument in paraphrase, reads a
short Java snippet written for the lesson, works the lab on the situation the
lesson states, and ends with an exercise done by hand.

Everything an author, a kit engineer or a reviewer needs is here. Where it says
"exactly", a test or a gate enforces it. Where it says "never", a published
page somewhere in this library has already been wrong for that reason.

It is built the way *Code Complete* was built (`docs/code-complete/PLAN.md`),
and it adopts that plan's conventions by reference wherever this one is
silent. Read these first:

- `AGENTS.md` §0, §1, §1a, §2 and the page-weight note;
- `content/AGENTS.md`, all of it;
- `scripts/mathpath/AGENTS.md` ("a preset's two claims");
- `docs/code-complete/PLAN.md` §D.0, §E and §F;
- `docs/code-complete/kit-report.md` (cckit as built, which §D.5 reuses).

**Status: specification, reviewed and reconciled (§R).** The book's text is
in hand (the operator's copy, §E.2):

- every chapter, section and pattern name in §B and §C, and every page, was
  checked against it;
- every figure in §S.2 was settled against the page it is on;
- every lesson's opening quotation was chosen, counted and checked character
  by character with `ea_quotes.py`, and re-located on its stated page alone
  after the review (44 of 44 OK);
- every lab figure in §C is the output of the reference model
  (`docs/enterprise-patterns/earef.py`, §D.4). The cckit lessons' figures were
  computed by the shipped cckit JavaScript itself;
- every Java snippet in §D.4 (74 of them) was compiled with `javac --release 8`
  (JDK 21) against stub declarations, and all 74 compile.

The review's findings are reconciled in §R; the changes to §D made after the
kit was started are listed in §R.1. One small cckit change blocks five
lessons (§H.1), and the owner has accepted it. The kit, `eakit` (§D), is
being built.

Contents

- §0 The one question, answered for this Subject
- §A PATH fields
- §B The seven courses, and the module names
- §C Every lesson: 44 entries
- §D The lab kit: `eakit` (8 modes, 18 views), and the cckit views reused
- §E Package layout, the source text, quoting, and the author's checklist
- §F Voice: the read-along, for a working programmer
- §G What is left out, and why
- §S Sources, and the register of figures
- §H Wiring notes for the orchestrator, and the kit work
- §R Review record

---

## §0 The one question

`docs/FUTURE-SUBJECTS.md` asks of every proposed Subject: **what does the reader
compute?**

Fowler mostly does not compute. He weighs, and he says so: there is no way to
measure the complexity of domain logic (Chapter 2, Making a Choice), and advice
about performance is not a fact until it is measured on your own configuration
(Introduction, Thinking About Performance). What he weighs, though, is almost
always a count over a situation. Examples:

- how many round trips a fine-grained interface makes across a process
  boundary;
- how many SQL statements a lazy collection issues as it is walked;
- how many writes a Unit of Work saves by waiting until commit;
- how many tables a class hierarchy needs under each inheritance mapping, and
  how many of them a query or an `ALTER TABLE` touches;
- how many server objects a hundred users need with stateful and with
  stateless sessions;
- which commits an optimistic lock refuses, and how much work the refused
  session loses;
- how many pennies a rounding scheme loses or gains when it splits a sum.

He does that arithmetic himself in the narratives, with the numbers left out,
and the lab puts the numbers back.

The labs fall into three families. Every view's `panel_intro` says which one
it is in:

1. **A count over the situation the lesson states.** The lesson gives a
   structure: tables and their rows, a script of loads and changes, a class
   hierarchy, a timeline of sessions, calls between classes placed on nodes.
   The lab counts what the chapter says to count: statements, rows, writes,
   tables touched, conflicts, remote calls. (eakit modes `uow`, `inherit`
   and `lock`, the `load` views other than `finds`, and `remote/boundary`.)
2. **The arithmetic of the figures the lesson states.** The lesson gives
   response times at two loads, throughput per server, a latency and a work
   time per call, a session's size, an amount and its ratios. The lab does the
   arithmetic the chapter does in words. The figures come from the lesson,
   never from the kit. Each is marked with its source: *the book's
   illustration* (with its §S.2 id) or *illustrative*. (eakit modes `perf`,
   `session` and `money`, and the `remote/calls`, `remote/payload` and
   `load/finds` views.)
3. **A count over code**, reused from cckit (§D.5). Twenty lessons count
   something in a short Java snippet or a dependency list with the Code
   Complete kit, unchanged but for one sentence (§H.1). That count is
   duplicated lines (the Transaction Script that copies its rule), decision
   points (the conditional a Special Case removes), public fields (a mutable
   Value Object), or what a change ripples to (a domain that imports its
   mapper).

**What the lab never does** is call a count a measurement of the reader's
system. Twenty-five statements against three round trips is what the lesson's
latency gives; on the reader's network the ratio is different, and Fowler's
own rule is to measure it there. That is the material clause (§A).

**Deliberate deviations from the library's conventions** (as in Code Complete
unless noted):

1. **Two parts read together.** The book's own order is all the narratives,
   then all the patterns. A lesson here pairs a narrative section with its
   patterns (§B), so the courses follow the narratives' order and pull each
   pattern forward to the narrative that introduces it. The reading order is
   given in every lesson's **Read** line.
2. **The book is cited by chapter, section and pattern, never by page.** The
   operator's copy has no printed page numbers. Lessons say "Chapter 11, Unit
   of Work" or "Chapter 3, Reading in Data". The PDF page of the operator's
   copy goes only in source comments beside the lesson dict
   (`# PDF p. 174 of the operator's copy`), and in this document. The book's
   own cross-references, such as "Unit of Work (184)", are printed pages of
   another printing and do not match this copy (§E.2). They are never quoted
   or used.
3. **Code appears in every lesson body**, through the `code` block and the
   code read-out dialect that Code Complete added (`render.py`'s code block,
   `speech.say_code`, PATH `"speech": "code"`). No renderer work is needed.
4. **One language, Java**, as in Code Complete: Java 8, no records, no `var`,
   no lambdas, no streams, no annotations. The book's own examples are Java
   and C#. A snippet is at most 20 lines of at most 72 characters (tighter
   than the 30 × 80 the block allows, so that the listing never scrolls at
   phone width beside the lab).
5. **The chapter comes first, in paraphrase**, with at most 40 words of
   opening quotation and 60 in all (§E.3), as in Code Complete.
6. **A second kit is reused.** Twenty of the 44 lessons use cckit views
   (§D.5); 24 use the new eakit. Each reuse is justified in §D.5.

**Deviations from the brief that commissioned this plan** (each argued where it
falls):

- 44 lessons, not about 42: inheritance takes two lessons (4.6, 4.7), because
  single-table and the two multi-table mappings make different trade-offs and
  the lab compares all three in each.
- Registry is read with Database Connections (3.6), not with the base patterns
  of course 2, because Fowler introduces it as the way to find a connection or
  a finder. Record Set is read with Table Module (2.3), its only client.
- The book's own example domains (revenue recognition, the
  footballer/cricketer/bowler hierarchy, the album, artist and track pages,
  the sales-tax service) are not reused as code, and no snippet follows the
  shape of one of the book's listings. Every snippet uses its own domain
  (§E.3), so no listing can be mistaken for an adaptation of the book's.
- The money lab's `allocator` rule is stated outright (floor every share, then
  give the remaining cents one each to the first shares in order). Money (Chapter
  18) says the pennies may be scattered in other ways; the lab's rule is the
  one the book's own example (Matt Foemmel's and Fowler's) uses, and the panel
  says so (§D.1).
- cckit's `complexity` banner names McConnell's book as "the book". On this
  path that is wrong, so the five lessons that reuse the view wait for a small
  cckit change (§H.1).

---

## §A PATH fields (`content/enterprise_patterns/__init__.py`)

```
"slug": "enterprise-patterns",
"title": "Patterns of Enterprise Application Architecture, Read Along",
"speech": "code",
"level": "Intermediate",
"level_note": "you can read a short Java class and know what a table, a row and a SQL query are",
```

**Title: decided** — `"Patterns of Enterprise Application Architecture, Read
Along"`, with the catalog's `short_title` `"Enterprise Application Patterns"`.
It follows the read-along precedent (`"Code Complete, Read Along"`, `"Capital,
Read Along"`), and the suffix keeps a breadcrumb or `<title>` from presenting a
page of this library as the book, which belongs to Fowler and Addison-Wesley.
The short title drops "Read Along" as Code Complete's does. It is not the
book's title shortened to an acronym, because the acronym is not a name a
reader searches for. **Short title: decided by the owner** (§H.4) —
"Enterprise Application Patterns". The alternative, "Enterprise Patterns",
matched the slug but read as a different book.

**Check-id prefix: decided** — `eaa`. **Catalog group: decided** —
`computing`, after Code Complete (§H.3).

**tagline** (the counts are re-verified at wiring by
`test_the_tagline_and_description_state_the_real_counts`):

> Martin Fowler&rsquo;s <em>Patterns of Enterprise Application
> Architecture</em>, read narrative by narrative with the patterns each one
> introduces &mdash; and each pattern&rsquo;s trade-off counted on a stated
> situation: round trips, SQL statements, writes saved, tables touched,
> conflicts refused, pennies lost. Seven courses and 44 lessons are available.

**description**:

> The Enterprise Application Patterns Subject: a read-along of the 2002 book
> that follows its eight narrative chapters and reads each with the patterns it
> introduces. Seven courses take the reader from layering and domain logic
> through the database, object-relational mapping, web presentation,
> concurrency and session state to distribution. Each lesson sets out a
> chapter&rsquo;s argument, shows the pattern in a short piece of Java, and
> counts its trade-off in the lab &mdash; the statements a lazy collection
> issues, the writes a unit of work saves, the remote calls a facade removes
> &mdash; and ends with a situation to work by hand. All seven courses and 44
> lessons are available.

**key** (each line at most 46 characters, measured):

```
fine-grained time = n·(latency + work)        (38)
coarse-grained time = m·latency + n·work      (40)
lazy load = 1 + one query per parent used     (41)
unit of work: one write per object, at commit (45)
stateless objects = users·service/think       (39)
a count models the situation, not your system (45)
```

(The parenthesised lengths are not part of the lines.)

**material** (required, unique: it must differ from every existing clause).
The proposed pattern is
`EAA_DISCLAIMER_RE = re.compile(r"(?i)not a measurement of your system")`. It
was checked against the thirteen patterns in `tests/test_site_invariants.py`,
lines 2018–2093, and matches none of their clauses. It reflects Fowler's own
rule that performance advice is not fact until it is measured on your
configuration (Introduction, Thinking About Performance; PDF p. 27):

> every figure on this path is computed in your browser from the situation a
> lesson states &mdash; its rows, calls, sessions and timings &mdash; and a count
> models that situation; it is not a measurement of your system, which only
> measuring your own configuration can give.

**prerequisites** (paragraphs):

1. You can read a short Java class. Every snippet is Java 8, at most twenty
   lines, using classes, interfaces, fields, `if`, loops, `List` and `Map`.
   Where a snippet uses JDBC (`Connection`, `PreparedStatement`,
   `ResultSet`), the lesson says in a sentence what each call does. A reader
   who knows C#, Kotlin or TypeScript reads it without trouble.
2. You know what a relational table, a row, a primary key and a `SELECT` are.
   You do not need to write SQL beyond a one-table query; the lessons that
   need a join show it.
3. No other Subject. *Code Complete, Read Along* is a good companion, and its
   decision-point and duplication counts are reused here (§D.5), but every
   rule is restated where it is used. The arithmetic is products, sums and
   shares, and the labs do it.
4. A copy of the book is strongly recommended. The book is in copyright, so a
   lesson states each chapter's argument in its own words, points to the
   chapter, section and pattern by name, and quotes at most a sentence or two.
   The code is written for these lessons, and none of the book's listings is
   reproduced. The book's own examples, worked in full in Part 2, are better
   read in the book.
5. Some system of your own, or one you know. Every lesson's last step sends
   you to a design you work on, with a count to make.

**why_order** (paragraphs):

1. The order is the narratives', and it runs from the outside in and out
   again. Layers and Performance sets out what an enterprise application is,
   the vocabulary of performance, and the three layers. Organizing Domain Logic
   chooses how the middle layer is built. Talking to the Database and Objects
   and Tables connect it to the database. Web Presentation puts a front on it.
   Concurrency and Session State let many people use it at once. Distribution
   and Putting It Together decides what, if anything, runs on another machine,
   and closes with the book's own summary.
2. Domain logic comes before the database because Fowler's choice of
   data-source pattern depends on the domain pattern chosen. A Table Module
   wants a Table Data Gateway; a rich Domain Model wants a Data Mapper. A
   reader who meets the mappers before the domain patterns cannot see why
   there are four of them.
3. Each pattern is read where the narrative introduces it, not in Part 2's
   order. Unit of Work is read with Chapter 3's behavioral problem, not after
   all the data-source patterns, so that the reader meets the problem first.
4. The courses can be read separately. Web Presentation assumes only the
   first course. Concurrency and Session State assumes the first and enough
   of the database courses to know what a row and a commit are.

**sequence_intro**:

> Each course assumes the ones before it and nothing else. The layers and the
> performance terms of the first course are used everywhere. The domain-logic
> choice of the second decides which data-source patterns the third and fourth
> use. Web presentation, concurrency and distribution then build on a system
> that already has all three layers.

**footer_lead**:

> <strong>Educational course material.</strong> Every figure on this path is
> computed in your browser from what the lesson states: a round-trip time is
> a product of the calls and the latency the lesson gives, a write count is a
> count over the script of changes it lists, a table count is a count over the
> hierarchy it draws. The code is written for this course; the labs read it
> and never run it, and nothing you type is sent anywhere. Figures the book
> gives are marked as the book&rsquo;s illustrations. What the labs cannot do
> is measure your system &mdash; Fowler&rsquo;s advice is to measure it
> yourself.

---

## §B The seven courses

| # | slug | title | the book | lessons | level |
| --- | --- | --- | --- | --- | --- |
| 1 | `enterprise-patterns-layers-and-performance` | Layers and Performance | Preface; Introduction; Chapter 1; Layer Supertype and Separated Interface (Chapter 18) | 5 | Intermediate |
| 2 | `enterprise-patterns-domain-logic` | Organizing Domain Logic | Chapters 2 and 9; Record Set, Value Object, Money and Special Case (Chapter 18) | 7 | Intermediate |
| 3 | `enterprise-patterns-data-source` | Talking to the Database | Chapter 3 (Architectural Patterns, Reading in Data, Building the Mapping, Database Connections, Some Miscellaneous Points); Chapter 10; Gateway, Mapper and Registry (Chapter 18) | 6 | Intermediate |
| 4 | `enterprise-patterns-objects-and-tables` | Objects and Tables | Chapter 3 (The Behavioral Problem, Structural Mapping Patterns, Using Metadata); Chapters 11–13 | 8 | Intermediate |
| 5 | `enterprise-patterns-web-presentation` | Web Presentation | Chapters 4 and 14 | 6 | Intermediate |
| 6 | `enterprise-patterns-concurrency-and-session-state` | Concurrency and Session State | Chapters 5, 6, 16 and 17 | 7 | Intermediate |
| 7 | `enterprise-patterns-distribution` | Distribution and Putting It Together | Chapters 7, 8 and 15; Plugin and Service Stub (Chapter 18) | 5 | Intermediate |

Total 44. Every pattern in Part 2 is read in some lesson; §C's **Read** lines
name each one. Course titles are this plan's, not the book's (the book has no
Part titles beyond "The Narratives" and "The Patterns"). They take their words
from the chapter titles where they can. Slugs carry the `enterprise-patterns-`
prefix, so the generic "Web Presentation" collides with nothing in the flat
course namespace.

**Part files.** A course with more than six lessons splits into `part_a.py`
and `part_b.py`:

- Course 2: lessons 1–4 in `part_a.py` (Chapters 2 and 9), 5–7 in `part_b.py`
  (the Chapter 18 patterns);
- Course 4: lessons 1–4 in `part_a.py` (Chapter 11 and keys), 5–8 in
  `part_b.py` (embedded values, inheritance, metadata);
- Course 6: lessons 1–3 in `part_a.py` (Chapter 5), 4–7 in `part_b.py`
  (offline locks and session state).

The rest are one `part_a.py`.

**Check ids** take the form `eaa-course7-lesson-<lesson-slug>`, 19 characters
before the slug. Every lesson slug in §C is at most 39 characters, so every
check id is at most 58, inside the 72-character cap. The longest is
`eaa-course1-lesson-layer-supertype-and-separated-interface` (58). Course homes
are `eaa-course1-home` … `eaa-course7-home`; the path page is `eaa-path`.

**Module names.** A lesson's `module` is the Part 2 chapter its patterns come
from, as `Chapter N · title`. A lesson that reads no Part 2 pattern takes its
narrative chapter (`Introduction`, `Chapter 1 · Layering`,
`Chapter 3 · Mapping to Relational Databases`, `Chapter 5 · Concurrency`,
`Chapter 6 · Session State`, `Chapter 7 · Distribution Strategies`,
`Chapter 8 · Putting It All Together`). One exception is stated: 3.6 reads
Chapter 18's Registry beside Chapter 3's Database Connections and Some
Miscellaneous Points, and keeps `Chapter 3 · Mapping to Relational
Databases`, because its lab and most of its reading are Chapter 3's and
Registry is the secondary read. Every name is at most 60 characters and is
never cut. The course `summary` names each chapter in full.

| module name | lessons | the book's title, as in the contents |
| --- | --- | --- |
| `Introduction` | 1.1–1.3 | Preface; Introduction |
| `Chapter 1 · Layering` | 1.4 | Layering |
| `Chapter 18 · Base Patterns` | 1.5, 2.5–2.7, 7.5 | Base Patterns |
| `Chapter 9 · Domain Logic Patterns` | 2.1–2.4 | Organizing Domain Logic (Chapter 2); Domain Logic Patterns (Chapter 9) |
| `Chapter 10 · Data Source Architectural Patterns` | 3.1–3.4 | Data Source Architectural Patterns |
| `Chapter 3 · Mapping to Relational Databases` | 3.5–3.6 | Mapping to Relational Databases |
| `Chapter 11 · Object-Relational Behavioral Patterns` | 4.1–4.3 | Object-Relational Behavioral Patterns |
| `Chapter 12 · Object-Relational Structural Patterns` | 4.4–4.7 | Object-Relational Structural Patterns |
| `Chapter 13 · Object-Relational Metadata Mapping Patterns` | 4.8 | Object-Relational Metadata Mapping Patterns |
| `Chapter 14 · Web Presentation Patterns` | 5.1–5.6 | Web Presentation (Chapter 4); Web Presentation Patterns (Chapter 14) |
| `Chapter 5 · Concurrency` | 6.1–6.3 | Concurrency |
| `Chapter 16 · Offline Concurrency Patterns` | 6.4–6.5 | Offline Concurrency Patterns |
| `Chapter 6 · Session State` | 6.6 | Session State |
| `Chapter 17 · Session State Patterns` | 6.7 | Session State Patterns |
| `Chapter 7 · Distribution Strategies` | 7.1 | Distribution Strategies |
| `Chapter 15 · Distribution Patterns` | 7.2–7.3 | Distribution Patterns |
| `Chapter 8 · Putting It All Together` | 7.4 | Putting It All Together |

(The longest, Chapter 13's, is 56 characters.)

**Every lesson has an exercise**, as in Code Complete §B. It is a situation (a
table of rows, a script of changes, a timeline, a hierarchy) or a piece of code
to measure by hand. It goes in a `code` block or a small table under an `h3`
"Exercise" near the end of the body, and the `standard` asks for exactly that
act without the lab. Its answer, computed by the reference model and given in
§C as **Answer**, goes in the `why` of one quiz item and nowhere else on the
page. The exercise's instance is never a preset's.

**Every lesson ends by sending the reader to their own system.** The last of
the `steps` is the act §C's **Own:** line names, with an observable result
("count…, write the figure, and say in one sentence…"), never "reflect on".

---

## §C Every lesson

Format, as Code Complete §C, with these differences:

- **slug** — Title — *module* — minutes (an estimate for the author; there is
  no minutes field).
- **Read:** the chapter, sections and patterns the lesson covers, in reading
  order, with the PDF pages of the operator's copy (for source comments only;
  the lesson cites by chapter, section and pattern), and the argument in
  paraphrase.
- **Quote:** the one opening quotation (§E.3), its PDF page and its word count,
  checked with `ea_quotes.py`. The lesson may open without it; it may not open
  with another without recording it here.
- **Do:** the observable objective. **Standard:** the act that shows it,
  without the lab, and its pass level.
- **Lab:** kit, mode/view (§D); presets with their exact instances; the tile
  values the reference model computes, in §D.0's formats. The exact strings
  are read with `labcheck.js --observe` at authoring and pinned.
- **Misconception:** the wrong model `mistakes[0]` names and refutes. **Also**:
  a second, for `mistakes[1]`.
- **Worked:** the single worked example, in one line. It works a preset,
  never the exercise.
- **Exercise:** the applied task. **Answer:** its answer, which goes in the
  `why` of one quiz item and nowhere else on the page.
- **Own:** what the last of the `steps` sends the reader to do.
- **Snippet:** the lesson's Java, by its §D.4 name (the constant's name in the
  course module). In a cckit `code` lab the snippet *is* the preset's code.
- **Sources:** the chapters and patterns, and every figure marked *F<n>* in
  §S.2.

**Read lines are paraphrase.** This document quotes the book only in the
**Quote** lines, each within §E.3's limits, and in a few phrases of two to
eight words in §C and §S.2 that identify a claim. Its other quotation marks enclose a
misconception's wording, a preset's label, a tile or a code string.

Preset ids are suggestions; **the instances are not optional.** Every figure
below was computed by `earef.py` (eakit) or by the shipped cckit JavaScript
through `ccrun.js` (cckit) from the instance given, and an author who changes
an instance recomputes it and records it here in the same commit. Every
instance is illustrative unless it carries an *F* id.

**Misconceptions.** As Code Complete §C: a reading of the chapter someone could
hold, or the view the chapter argues against at its strongest, never a jibe at
a technology. A misconception is never the later view named as the course's
§F.4 aside. It is refuted by the chapter's argument; a lab run on an
illustrative instance illustrates the refutation and is said to ("on the
lesson's illustration, …").

### Course 1 — Layers and Performance (`enterprise-patterns-layers-and-performance`, 5)

The Preface, the Introduction and Chapter 1, with the two base patterns that
layering needs. What an enterprise application is, the words Fowler uses for
performance, and the three layers. Its `how_to` says the course has the least
pattern of any, because it sets up the vocabulary the patterns are argued in.
Its `not_covered` says the Introduction's survey of architecture definitions is
named, not taught.

1. **enterprise-applications** — Enterprise Applications — *Introduction* — 15 min
   - **Read:** Preface (PDF pp. 15–20): who the book is for, and its two
     parts, the narratives to read through and the patterns to look up.
     Introduction (pp. 21–31):
     - Architecture (p. 22): two common elements, the highest-level breakdown
       of a system and the decisions that are hard to change.
     - Enterprise Applications (p. 23): persistent data, lots of it (*F1*),
       accessed concurrently by many people, through many screens, integrated
       with other systems that disagree about what the data means, and
       governed by business rules that do not follow from any principle.
     - Kinds of Enterprise Application (p. 25): three points on a large plane
       — a business-to-customer retailer (many users, simple logic), a
       leasing system (few users, *F2*, complex logic) and a small expense
       tracker (simple everything, but it must be built quickly). Fowler is
       wary of anyone who says "always do this".
     - Patterns (p. 29): Alexander's definition as Fowler quotes it, a pattern
       as a chunk of advice rooted in practice, and the form each Part 2 pattern
       takes (how it works, when to use it, examples).
   - **Quote:** PDF p. 24, 18 words — “I find this a curious term because there
     are few things that are less logical than business logic.”
   - **Do:** count the special cases in a business rule and see what each
     costs a reader.
   - **Standard:** given a routine encoding a business rule, list its special
     cases and count its decision points by the stated rule.
   - **Lab:** cckit `code/complexity` (§D.5). Presets `due-day` (`DUE_DAY`:
     `coDecisions` 9, `coBreakdown` "1 + if 5 + && 2 + || 1", `coBand` "6–10",
     `coDepth` 2, `coDeepest` "line 12") and `due-day-plain` (`DUE_DAY_PLAIN`:
     1, "1", "0–5", 0, "line 3"). Pins `coDecisions`, `coBreakdown`. The body
     says the rule's eight exceptions are invented, and that the bands are
     McConnell's, from *Code Complete*, not Fowler's: Fowler gives no count.
   - **Misconception:** "Business logic is logic: find the principle and the
     special cases disappear." Fowler's point on p. 24 is that they do not;
     the rules were agreed one negotiation at a time, and the program has to
     carry them. On the lesson's illustration, eight decision points come from
     agreements nobody can derive.
   - **Also:** "An enterprise application is a big application." Enterprise
     Applications (p. 24) says not all of them are large, and Kinds of
     Enterprise Application gives a small expense tracker as one; what makes
     it enterprise is persistent, shared, integrated data, not its size.
   - **Worked:** `due-day`: 1 + 5 `if` + 2 `&&` + 1 `||` = 9.
   - **Exercise:** `LATE_FEE` (§D.4). Count its decision points and name the
     agreement each one encodes. **Answer:** 8 (1 + if 4 + && 2 + || 1):
     after ten days, after thirty or flagged, the charity exemption under
     sixty days, half for a new account with no payments.
   - **Own:** one rule in a system you know that someone outside engineering
     agreed; write its exceptions as a list and count them.
   - **Snippet:** `DUE_DAY`, 19 lines; `DUE_DAY_PLAIN`, 4.
   - **Sources:** Preface; Introduction (Architecture, Enterprise
     Applications, Kinds of Enterprise Application, Patterns); *F1*, *F2*.

2. **performance-terms** — Thinking About Performance — *Introduction* — 15 min
   - **Read:** Introduction, Thinking About Performance (PDF p. 27, and p. 28
     for load, load sensitivity and the illustration). Fowler's caution first: much architecture is about performance,
     and performance advice is not fact until it is measured on your own
     configuration. Then the terms, in his order: response time;
     responsiveness (acknowledging a request, which can be fast while the
     response is slow); latency (the minimum time for any response, which a
     remote call pays); throughput (bytes or transactions per second); load
     (how much stress the system is under, for example how many users); load
     sensitivity (how response time varies with load); efficiency
     (performance divided by resources). His illustration of load
     sensitivity (*F3*): one system answers in 0.5 s from 10 to 20 users,
     another in 0.2 s at 10 users rising to 2 s at 20.
   - **Quote:** PDF p. 27, 16 words — “any advice about performance should not
     be treated as fact until it's measured on your configuration.”
   - **Do:** compute load sensitivity from two measurements, and say which
     system is better at which load.
   - **Standard:** given response times at two loads for two systems, compute
     each system's change per user and ratio, and the response time between
     them by straight-line interpolation, stating that it is interpolation.
   - **Lab:** eakit `perf/load` (§D.1). Presets `system-a-and-b` (the book's
     illustration, *F3*, in ms: `a, 10, 500; a, 20, 500; b, 10, 200; b, 20,
     2000`, users 15 → `pzPerUser` "a 0 ms a user; b 180 ms a user", `pzRatio`
     "a 1×; b 10×", `pzAt` "a 500 ms; b 1,100 ms") and `at-ten-users` (users
     10 → `pzAt` "a 500 ms; b 200 ms"). Pins `pzPerUser`, `pzRatio`, `pzAt`.
     The body says the interpolation at 15 users is the lab's assumption, not
     the book's: Fowler gives only the two ends.
   - **Misconception:** "The system with the lower response time at one load
     is faster at every load." On the book's illustration B is faster at 10
     users and A from about 12 users up; which is better depends on the load,
     which is why Fowler separates response time from load sensitivity.
   - **Also:** "Responsiveness and response time are the same thing." Fowler
     distinguishes them: a system that shows a progress bar at once is
     responsive while its response time is long.
   - **Worked:** B rises (2,000 − 200)/(20 − 10) = 180 ms a user, a ratio of
     2,000/200 = 10×; A's ratio is 1×.
   - **Exercise:** `north, 5, 400; north, 25, 1400; south, 5, 900; south, 25,
     1000`, at 20 users. **Answer:** north 50 ms a user, 3.5×, 1,150 ms at
     20; south 5 ms a user, 10/9 ≈ 1.1×, 975 ms at 20: south is faster at 20
     users, north at 5.
   - **Own:** one response time you have measured, and the load you measured it
     at; write which of Fowler's terms the figure is, and the load at which
     you have no figure at all.
   - **Snippet:** `RESPONSE_TIME`, 6 lines (no lab figures).
   - **Sources:** Introduction, Thinking About Performance; *F3*.

3. **capacity-and-scalability** — Capacity and Scalability — *Introduction* — 15 min
   - **Read:** Thinking About Performance, second half (PDF p. 28):
     efficiency, with the book's example (*F4*); capacity (the maximum
     effective throughput or load); scalability (how adding resources affects
     performance), vertical and horizontal; and the Swordfish and Camel
     illustration (*F5*), in which Camel has the higher capacity and
     Swordfish the better horizontal scalability, with Camel the more
     efficient below five servers. Fowler's closing point: buying hardware is
     often cheaper than making the software more efficient, so scalability
     is worth more than it looks.
   - **Quote:** PDF p. 28, 12 words — “Scalability is a measure of how adding
     resources (usually hardware) affects performance.”
   - **Do:** project throughput from measurements, find the crossover, and
     say how many servers a target needs.
   - **Standard:** given two systems' throughput measured at two server
     counts and a constant gain per server between and after them, compute
     each one's gain, the crossover and the servers needed for a target.
   - **Lab:** eakit `perf/scale`, cfg `unit` "server". Presets
     `swordfish-and-camel` (*F5*: `swordfish, 1, 20; swordfish, 2, 35; camel,
     1, 40; camel, 2, 50`, need 40, at 5 → `pzEfficiency` "swordfish 20 a
     server; camel 40 a server", `pzMarginal` "swordfish 15; camel 10",
     `pzCrossover` "5 servers (both 80)", `pzNeed` "swordfish 3; camel 1",
     `pzAt` "swordfish 80; camel 80") and `need-120` (need 120, at 10 →
     `pzNeed` "swordfish 8; camel 9", `pzAt` "swordfish 155; camel 130").
     Pins `pzMarginal`, `pzCrossover`, `pzNeed`. The panel says the lab
     projects at the measured rate past the last measurement, which is the
     book's own assumption ("we'll discover that…") and nothing more.
   - **Misconception:** "The system with the higher capacity scales better."
     Swordfish and Camel are Fowler's counterexample. On his figures Camel
     has twice the capacity on one server and Swordfish catches it at five.
   - **Also:** "Efficiency is throughput." Efficiency is throughput per unit of
     resource. In the book's example 30 tps on two CPUs (15 a CPU) is more
     efficient than 40 on four (10 a CPU), though 40 is the higher throughput.
   - **Worked:** Swordfish 20 + 15·(n − 1) and Camel 40 + 10·(n − 1) meet at
     n = 5: 80 tps each.
   - **Exercise:** `heron, 1, 30; heron, 3, 54; stork, 1, 45; stork, 3, 57`,
     need 60, at 6. **Answer:** heron gains 12 a server and stork 6; heron
     passes stork at 4 servers (66 against 63); both need 4 servers for 60;
     at 6, heron 90 and stork 75.
   - **Own:** the last time your team scaled a system, by hardware or by
     code; write whether it was scaling up, scaling out, or (if it was done
     by code) a gain in efficiency instead, and the figure that justified it.
     (Corrected at authoring: a change made in code is neither of Fowler's
     two scalabilities, which are both about adding hardware.)
   - **Snippet:** `SERVERS_NEEDED`, 13 lines: the loop that `pzNeed` does,
     run by hand in the exercise, with a guard for a system that gains
     nothing from another server (the loop would never end).
   - **Sources:** Introduction, Thinking About Performance; *F4*, *F5*.

4. **layering** — Layering — *Chapter 1 · Layering* — 18 min
   - **Read:** Chapter 1 (PDF pp. 33–38): the benefits and costs of layers as
     Fowler lists them on p. 33 (a layer can be understood and replaced on its
     own, and minimises dependencies; but layers do not encapsulate
     everything, so a new field ripples through all of them, and extra layers
     cost performance); The Evolution of Layers (p. 34), from client–server
     to three layers; The Three Principal Layers (p. 35), presentation,
     domain and data source, with the rule that the domain and data source
     never depend on the presentation, and the 10 percent example (*F6*):
     logic that colours a product red when its sales rose by more than 10%
     belongs in the domain, not the page; Choosing Where to Run Your Layers
     (p. 37), servers by default and the client only for responsiveness or
     disconnected use; the complexity boosters (p. 38, *F7*).
   - **Quote:** PDF p. 36, 12 words — “The domain and data source should never
     be dependent on the presentation.”
   - **Do:** find domain logic that has leaked into the presentation by the
     duplicate it forces when a second presentation is added.
   - **Standard:** given two presentations of the same data, mark the lines
     that are domain logic and write the domain method that replaces them.
   - **Lab:** cckit `code/dupes`, `min_run` 2. Presets `rising-twice`
     (`RISING_TWICE`: `coDupBlocks` 1, `coDupLines` 6, `coDupWhere` "lines 3–5
     and lines 11–13") and `rising-once` (`RISING_ONCE`: 0, 0, "none"). Pins
     all three. The body says the 10% rule is the book's illustration (*F6*)
     and the code is the lesson's.
   - **Misconception:** "Layers are tiers: three layers means three machines."
     Fowler separates logical layers from where they run (Choosing Where to Run
     Your Layers); the separation is worth having on one machine.
   - **Also:** "Putting the rule in the page is harmless while there is only
     one page." Fowler's test is to imagine adding a second presentation,
     such as a command line: everything that would be duplicated is domain
     logic. On the lesson's illustration that is three lines, copied.
   - **Worked:** `rising-twice`: lines 3–5 and 11–13 match, one block of 3
     lines in 2 copies, 6 lines.
   - **Exercise:** `OVERDUE_TWICE` (§D.4): mark the duplicated lines and write
     the method that removes them. **Answer:** lines 3–4 and 10–11 (`coDupBlocks`
     1, `coDupLines` 4); the rule becomes `boolean isOverdue()` on `Invoice`.
   - **Own:** one screen in a system you know; list each line of it that would
     be repeated if the same data were offered through an API, and count them.
   - **Snippet:** `RISING_TWICE`, 15 lines; `RISING_ONCE`, 14.
   - **Sources:** Chapter 1; *F6*, *F7*.

5. **layer-supertype-and-separated-interface** — Layer Supertype and Separated Interface — *Chapter 18 · Base Patterns* — 15 min
   - **Read:** Chapter 18, Layer Supertype (PDF p. 420), a superclass for every
     object in a layer, holding what they share (an ID, say); Separated
     Interface (pp. 421–423): define an interface in one package and implement
     it in another, so that a package that must not depend on another can
     still call it; who instantiates the implementation (a factory, a
     Plugin), and when not to bother.
   - **Quote:** PDF p. 421, 15 words — “use Separated Interface to define an
     interface in one package but implement it in another.”
   - **Do:** count what a change to the database library reaches, before and
     after the domain stops depending on its mapper.
   - **Standard:** given dependencies with a cycle through the domain, redraw
     them with a Separated Interface and list what a change to the database
     layer reaches in each.
   - **Lab:** cckit `deps/ripple`. Presets `mapper-in-domain` (edges `screen,
     order; order, mapper; mapper, order; mapper, jdbc`, changed `jdbc` →
     `dgDirect` "1: mapper", `dgAffected` "3: mapper, order, screen") and
     `separated` (`screen, order; order, finder; mapper, finder; mapper, order;
     mapper, jdbc; main, mapper` → "1: mapper", "2: main, mapper"). Pins both
     tiles. The lab follows the cycle in `mapper-in-domain` without looping
     (cckit's ripple is a breadth-first search, §D.5).
   - **Misconception:** "An interface is only worth having when there are two
     implementations." Separated Interface has one implementation; its point
     is the direction of the dependency, which Fowler argues from package
     dependencies, not from substitution.
   - **Also:** "A Layer Supertype is a God class." It holds only what every
     object in its layer shares; Fowler's example is the ID field.
   - **Worked:** in `separated`, `order` depends on `finder`, an interface in
     its own package; a change to `jdbc` reaches `mapper` and the `main` that
     wires it, and no domain class.
   - **Exercise:** `report, invoice; invoice, pdfwriter; pdfwriter, fontlib`,
     changed `fontlib`. List what it reaches, then put a Separated Interface
     where it would keep `invoice` out of reach. **Answer:** 3: invoice,
     pdfwriter, report (`dgDirect` "1: pdfwriter"). An interface
     `InvoiceRenderer` in the invoice package, implemented by `pdfwriter`,
     reverses the `invoice, pdfwriter` edge (`pdfwriter, invoice`, plus `main,
     pdfwriter` to wire it), and `fontlib` then reaches "2: main, pdfwriter".
   - **Own:** one place in your code where a domain class imports something
     from a lower layer; draw the edge, and write the interface that would
     reverse it.
   - **Snippet:** `SEPARATED_FINDER`, 19 lines.
   - **Sources:** Chapter 18, Layer Supertype, Separated Interface.

### Course 2 — Organizing Domain Logic (`enterprise-patterns-domain-logic`, 7)

Chapters 2 and 9, with the Chapter 18 patterns a domain layer is built from.
The three ways to organise domain logic, how to choose between them, the
Service Layer over them, and the small objects they are made of. Its `how_to`
says the lab counts what each organisation costs in code, and that the choice
between them is Fowler's judgement, which no count settles. Its `not_covered`
says Fowler's full revenue-recognition example is pointed to, not reworked.

1. **transaction-script** — Transaction Script — *Chapter 9 · Domain Logic Patterns* — 15 min
   - **Read:** Chapter 2's opening (PDF pp. 39–41) on Transaction Script, then
     Chapter 9, Transaction Script (pp. 112–117): one procedure per action the
     user takes, with the logic and (directly or through a gateway) the
     database calls in it; organising scripts as methods of a class or as
     command objects; its virtues, simplicity and a natural fit for a
     transactional boundary; its failing, that common logic is duplicated
     across scripts as the logic grows, which subroutines help with only so
     far.
   - **Quote:** PDF p. 113, 35 words — “The glory of Transaction Script is its
     simplicity. Organizing logic this way is natural for applications with
     only a small amount of logic, and it involves very little overhead either
     in performance or in understanding.”
   - **Do:** find the duplication that two scripts share and remove it with a
     subroutine.
   - **Standard:** given two scripts, mark their repeated lines and write the
     subroutine both would call.
   - **Lab:** cckit `code/dupes`, `min_run` 2. Presets `two-scripts`
     (`TWO_SCRIPTS`: 1, 6, "lines 3–5 and lines 12–14") and
     `shared-subroutine` (`SHARED_SUBROUTINE`: 0, 0, "none"). Pins all three.
   - **Misconception:** "Transaction Script is a beginner's pattern that a
     serious system grows out of." Its own When to Use It (the quotation)
     calls it natural for applications with little logic. Making a Choice
     qualifies this without withdrawing it: the better the team the more
     Fowler leans to Domain Model, he sees no reason for scripts on .NET, and
     a team that starts with scripts should not hesitate to refactor toward a
     Domain Model; its cost is the duplication as the logic grows.
   - **Also:** "A Transaction Script must contain its own SQL." Fowler
     separates it from the database with a gateway even in simple cases
     (Chapter 8, Down to the Data Source Layer, p. 102).
   - **Worked:** `two-scripts`: lines 3–5 and 12–14, three lines in two copies.
   - **Exercise:** `SHIPPING_TWICE`. **Answer:** lines 3–6 and 13–16
     (`coDupBlocks` 1, `coDupLines` 8): a subroutine `long shippingFor(long
     cents)` both scripts call.
   - **Own:** two handlers in a system you know that compute the same thing;
     count the lines they share.
   - **Snippet:** `TWO_SCRIPTS`, 17 lines; `SHARED_SUBROUTINE`, 16.
   - **Sources:** Chapter 2; Chapter 9, Transaction Script.

2. **domain-model** — Domain Model — *Chapter 9 · Domain Logic Patterns* — 18 min
   - **Read:** Chapter 2 on Domain Model (PDF pp. 39–41), then Chapter 9,
     Domain Model (pp. 118–125): an object model of the domain with both
     behaviour and data, in which each object takes the part of the logic
     relevant to it, and conditionals give way to polymorphism; simple and
     rich domain models, and the mapping each needs (Active Record for a
     simple one, Data Mapper for a rich one); keeping the domain model free of
     the database; the worry about bloated domain objects, which Fowler
     answers by putting each behaviour in the object it naturally fits and
     fixing bloat when, and if, it appears.
   - **Quote:** PDF p. 39, 24 words — “Rather than one routine having all the
     logic for a user action, each object takes a part of the logic that's
     relevant to it.”
   - **Do:** see where the decisions go when a type switch becomes
     polymorphism.
   - **Standard:** given a routine that switches on a kind, count its decision
     points, and write the subclass method that takes one branch.
   - **Lab:** cckit `code/complexity`, `bands` [5, 10]. Presets
     `price-by-kind` (`PRICE_BY_KIND`: 5, "1 + if 3 + && 1", "0–5", 1, "line
     5") and `price-delegated` (`PRICE_DELEGATED`: 2, "1 + if 1", "0–5", 2,
     "line 15"). Pins `coDecisions`, `coBreakdown`. The body says the listing
     `price-delegated` has no routine at its top (it is classes), so the kit
     counts the whole listing; that it keeps every kind the switch priced
     (books, alcohol, food, and `Product` itself as the default that changes
     nothing), so the fall from 5 to 2 loses no behaviour; and that the one
     decision left lives in `Food`, the only kind with a rule about quantity.
   - **Misconception:** "A Domain Model is a set of classes that mirror the
     tables." Fowler's distinction between a simple domain model (close to
     the tables) and a rich one (inheritance, strategies, behaviour) is
     exactly that it need not; the behaviour is what makes it a domain model.
   - **Also:** "Polymorphism removes the decisions." It moves each one to the
     class it concerns; on the lesson's illustration one `if` remains, in
     `Food`.
   - **Worked:** `price-by-kind`: 1 + 3 `if` + 1 `&&` = 5, all in one routine.
   - **Exercise:** `SHIPPING_BY_METHOD`. Count, then say which classes the
     branches would move to. **Answer:** 7 (1 + if 4 + && 1 + || 1); one class
     per method, `Post` and `Courier` (keeping its weight test), and a default
     class for every other method, which charges 0 for `COLLECT` or a staff
     parcel and 999 otherwise. The staff rule cannot go in a `Collect` class
     alone: in the routine a staff parcel sent by any method but post or
     courier pays nothing.
   - **Own:** one `switch` or `if` chain on a type code in a system you know;
     count its branches and name the class each would move to.
   - **Snippet:** `PRICE_BY_KIND`, 12 lines; `PRICE_DELEGATED`, 18.
   - **Sources:** Chapter 2; Chapter 9, Domain Model.

3. **table-module-and-making-a-choice** — Table Module, and Making a Choice — *Chapter 9 · Domain Logic Patterns* — 18 min
   - **Read:** Chapter 9, Table Module (PDF pp. 126–132): one object for all the
     rows of a table, working on a Record Set, which fits platforms with
     strong record-set tools; Chapter 18, Record Set (pp. 449–451), the
     in-memory tabular data such tools pass around. Then Chapter 2, Making a
     Choice (pp. 42–43): Fowler's sketch of effort against the complexity of
     the domain logic, with its admission that nobody can measure that
     complexity (*F8*); and Chapter 8, Starting with the Domain Layer (p.
     101), which makes the same choice again with the database in view.
   - **Quote:** PDF p. 42, 15 words — “The bad news is that nobody knows how to
     measure the complexity of domain logic.”
   - **Do:** count the objects in memory under each organisation for the same
     tables.
   - **Standard:** given tables and their row counts, state how many objects
     a Domain Model and a Table Module hold, and the most rows one module
     object's Record Set carries.
   - **Lab:** eakit `load/instances`. Presets `small-shop` (`customer, 200;
     orders, 1500; product, 120; line, 6000` → `ldTables` 4, `ldRows` 7,820,
     `ldRowObjects` 7,820, `ldTableObjects` 4, `ldLargest` "line 6,000") and
     `one-big-table` (`reading, 250000; meter, 400` → 2, 250,400, 250,400, 2,
     "reading 250,000"). Pins `ldRowObjects`, `ldTableObjects` and, as authored,
     `ldLargest`. The panel says the count
     is objects, not memory, and assumes every row is loaded, which neither
     pattern requires.
   - **Misconception:** "Table Module is a Domain Model with fewer objects."
     It has no object per row, so there is no identity per row, and the
     logic for an individual row runs on the module given an ID; Fowler sets
     the patterns apart on exactly that.
   - **Also:** "Making a Choice gives a threshold." The chapter's sketch has
     no units on either axis, and Fowler says so; the threshold is judgement,
     which this lesson does not pretend to compute.
   - **Worked:** `small-shop`: 200 + 1,500 + 120 + 6,000 = 7,820 row objects
     against 4 table modules, the largest of which, `line`, works on a Record
     Set of 6,000 rows.
   - **Exercise:** `patient, 900; visit, 5400; doctor, 30; ward, 12`.
     **Answer:** 6,342 row objects against 4 modules; the largest, `visit`,
     holds 5,400 rows.
   - **Own:** the three largest tables in a system you know; say which of the
     three domain patterns its code is closest to, and why.
   - **Snippet:** `TABLE_MODULE`, 16 lines.
   - **Sources:** Chapter 9, Table Module; Chapter 18, Record Set; Chapter 2,
     Making a Choice; Chapter 8, Starting with the Domain Layer; *F8*.

4. **service-layer** — Service Layer — *Chapter 9 · Domain Logic Patterns* — 15 min
   - **Read:** Chapter 2, Service Layer (PDF p. 44): the range from a thin
     facade to most of the logic in scripts inside the service, and Fowler's
     preference for the thinnest Service Layer you can have, if any, with his
     concession that many good designers use a rich one and that he asked
     Randy Stafford, who has, to write the pattern. Then Chapter 9, Service
     Layer, by Stafford (pp. 133–139): an application boundary that defines
     the operations its clients see and coordinates the response to each; the
     two kinds of business logic, domain logic and application logic
     (notifications, integration, transactions); domain facade against
     operation script; how to identify services from use cases; when it is
     not worth having (one kind of client, no transactional coordination).
   - **Quote:** PDF p. 136, 31 words — “But as soon as you envision a second
     kind of client, or a second transactional resource in use case
     responses, it pays to design in a Service Layer from the beginning.”
     The words are Randy Stafford's, in his pattern.
   - **Do:** find the application logic two kinds of client repeat, and move
     it to one service operation.
   - **Standard:** given two clients that each run the same response to a use
     case, mark the repeated lines, and write the service operation both
     would call.
   - **Lab:** cckit `code/dupes`, `min_run` 2. Presets `orders-twice`
     (`ORDERS_TWICE`: the web page and the nightly import each begin a
     transaction, reserve stock, confirm the order, commit and send the mail
     → `coDupBlocks` 1, `coDupLines` 10, `coDupWhere` "lines 4–8 and lines
     13–17") and `orders-served` (`ORDERS_SERVED`: 0, 0, "none"). Pins all
     three. The body says what repeats is application logic (the transaction
     and the mail) wrapped round one domain call (`confirm`), which is the
     part Stafford's operation script holds.
   - **Misconception:** "Domain logic and application logic are the same
     thing, so it does not matter which layer holds a rule." Stafford divides
     them (Kinds of "Business Logic"): domain logic is about the problem
     domain, application logic about the application's responsibilities,
     such as notifying people and integrated systems, and putting the second
     in domain classes makes them harder to reuse. How thick the service
     should be is a separate question, and the book gives two answers:
     Fowler prefers it thin, and says plainly that good designers, Stafford
     among them, make it rich.
   - **Also:** "Every application needs one." Fowler says not with one kind of
     client and no transactional coordination; the quotation's condition is
     the reason to have one.
   - **Worked:** `orders-twice`: five lines, from `db.begin()` to the mail,
     in each client; only the line that builds the order differs.
   - **Exercise:** `CANCEL_TWICE`. **Answer:** lines 3–7 and 13–17
     (`coDupBlocks` 1, `coDupLines` 10), the transaction, the release, the
     cancel and the mail; one `cancelOrder(Order order)` in the service
     replaces them, and the phone client keeps its own `audit.record`, which
     is about the request, not the use case.
   - **Own:** the clients of one domain operation in a system you know (pages,
     jobs, APIs); count the lines of transaction, notification and
     integration code each repeats.
   - **Snippet:** `ORDERS_TWICE`, 18 lines; `ORDERS_SERVED`, 17.
   - **Sources:** Chapter 2, Service Layer; Chapter 9, Service Layer (Randy
     Stafford).

5. **value-object** — Value Object — *Chapter 18 · Base Patterns* — 12 min
   - **Read:** Chapter 18, Value Object (PDF pp. 429–430): a small object, like
     money or a date range, whose equality is based on its values rather than
     its identity; why it should be immutable (aliasing: two owners sharing
     one mutable date and one changing it under the other); the name clash
     with the J2EE usage of "value object" for what the book calls a Data
     Transfer Object. Chapter 3's Embedded Value (read in 4.5) is how a value
     object is stored.
   - **Quote:** PDF p. 429, 17 words — “it's a very good idea to make them
     immutable—that is, once created none of their fields change.”
   - **Do:** check a small class for the two properties a Value Object needs:
     value equality and no way to change it.
   - **Standard:** given a class, count its public non-final fields and its
     mutators, and write the immutable version's fields and constructor.
   - **Lab:** cckit `code/class`. Presets `mutable-range` (`DATE_RANGE_MUTABLE`:
     `coFields` 2, `coPublicFields` 2, `coRoutines` 2, `coPublicRoutines` 2)
     and `value-range` (`DATE_RANGE_VALUE`: 2, 0, 3, 2). Pins
     `coPublicFields` only: the routine count changes with `equals`, which
     is not what makes the class a value. The body says the kit counts `public` and not `final`
     fields, and that it cannot see whether `equals` compares values; the
     reader reads that.
   - **Misconception:** "A Value Object is any object without an ID field." Its
     defining property is equality by value; an entity without a key field is
     still an entity if two with the same fields are different things.
   - **Also:** "Immutability is a performance trick." Fowler's reason is
     aliasing bugs.
   - **Worked:** `mutable-range`: both fields public and assignable, so any
     holder of the range can change it for every other holder.
   - **Exercise:** `QUANTITY_MUTABLE`. **Answer:** 3 fields, 2 public and
     not final (`amount`, `unit`; `max` is private and final), 3 routines, 2
     public; as a value object, `amount` and `unit` become private and final,
     `add` returns a new `Quantity`, and `equals` and `hashCode` compare both.
   - **Own:** one small class in a system you know that represents an amount,
     a range or a code; count its setters.
   - **Snippet:** `DATE_RANGE_MUTABLE`, 12 lines; `DATE_RANGE_VALUE`, 19.
   - **Sources:** Chapter 18, Value Object.

6. **money** — Money — *Chapter 18 · Base Patterns* — 15 min
   - **Read:** Chapter 18, Money (PDF pp. 431–437): an amount with its
     currency, held as an integral or fixed decimal type, never a floating
     point one; arithmetic that refuses mixed currencies;
     rounding, and the problem of allocation: splitting a sum by ratios in a
     way that neither loses nor gains a penny. The book's example (*F9*): 5
     cents to be split 70% and 30%, Matt Foemmel's conundrum; the ways of
     handling it, including giving the last share whatever is left, which
     piles the pennies onto it; and the book's answer, an allocation method
     that hands out the remainder. The example code is Foemmel's and
     Fowler's.
   - **Quote:** PDF p. 432, 18 words — “There's no general rounding scheme I can
     apply to both that will avoid losing or gaining a penny.”
   - **Do:** split an amount by ratios under four rounding rules, and find
     the ones that lose or gain.
   - **Standard:** given an amount in cents and ratios, compute each share
     exactly, then under nearest, down and allocator rounding, and state each
     rule's total.
   - **Lab:** eakit `money/allocate`. Presets on the book's example (*F9*,
     amount 5, ratios `70 30`): `nearest` (`mnShares` "4, 2", `mnTotal` 6,
     `mnDiff` "+1", `mnExact` "7/2 = 3.50, 3/2 = 1.50", `mnFurthest` "1/2 =
     0.50"), `round-down` ("3, 1", 4, "−1"), `rest-to-last` ("4, 1", 5, "0"),
     `allocator` ("4, 1", 5, "0"); and `three-ways` (100, `1 1 1`, nearest →
     "33, 33, 33", 99, "−1") and `three-ways-allocated` (allocator → "34, 33,
     33", 100, "0", `mnFurthest` "2/3 ≈ 0.67") and `pennies-to-last` (100,
     `1 1 1 1 1 1 1`, last → "14, 14, 14, 14, 14, 14, 16", 100, "0",
     `mnFurthest` "12/7 ≈ 1.71": the total is kept and the last share takes
     two cents more than the others, the fault the book names). Pins
     `mnShares`, `mnTotal`, `mnDiff`. The panel states the allocator rule in
     full (§D.1) and says the book allows other ways of placing the
     remainder.
   - **Misconception:** "Rounding each share to the nearest cent keeps the
     total." On the book's own example it gains a cent (4 + 2 = 6 from 5),
     and on a three-way split of a dollar it loses one.
   - **Also:** "Use a `double` and round at the end." The book's reason is
     that floating point brings back the rounding problems Money exists to
     avoid. The lesson adds, as its own explanation and in one sentence, that
     binary floating point cannot hold most decimal fractions exactly.
   - **Worked:** 5 × 70/100 = 3.5 and 5 × 30/100 = 1.5; nearest gives 4 and
     2, which is 6.
   - **Exercise:** 100 cents in six equal shares, by nearest and by allocator.
     **Answer:** nearest 17 each, 102 (+2); allocator 17, 17, 17, 17, 16, 16,
     100 (0); exact 50/3 ≈ 16.67 each.
   - **Own:** one place a system you know splits an amount (tax, a discount
     across lines, instalments); write which rule it uses and what happens to
     the remainder.
   - **Snippet:** `REFUND_SPLIT`, 19 lines: the caller's side, a refund
     shared across the payments that made it, which leaves the splitting to
     `Money` and checks that the parts add back up. The allocator rule itself
     is the panel's, run by hand in the exercise.
   - **Sources:** Chapter 18, Money (the conundrum and the example are Matt
     Foemmel's, the example with Fowler); *F9*.

7. **special-case** — Special Case — *Chapter 18 · Base Patterns* — 12 min
   - **Read:** Chapter 18, Special Case (PDF pp. 438–440): instead of returning
     null and making every caller check, return a subclass with the
     expected interface and harmless behaviour, with separate special cases
     where a null can mean different things (no customer, or a customer
     nobody knows); a special case can also be flyweight-shared when it
     has no state; its relation to the Null Object pattern; and the book's
     note that IEEE floating-point infinity and NaN are special cases of a
     kind.
   - **Quote:** PDF p. 438, 22 words — “Instead of returning null, or some odd
     value, return a Special Case that has the same interface as what the
     caller expects.”
   - **Do:** count the null checks that a Special Case removes from a caller.
   - **Standard:** given a caller with null checks, count its decision points,
     and write the Special Case class that removes them.
   - **Lab:** cckit `code/complexity`, `bands` [5, 10]. Presets `null-checks`
     (`NULL_CHECKS`: 5, "1 + if 2 + && 2", "0–5", 1, "line 4") and
     `guest-customer` (`GUEST_CUSTOMER`: 1, "1", "0–5", 0, "line 3"). Pins
     `coDecisions`, `coBreakdown`. As authored (2.2 too), `"book": "other"`,
     and the panel intro states the operators in words ("each conditional
     and and conditional or"), because cckit refuses `&` in panel text, so
     §D.5's example intro does not build.
   - **Misconception:** "A Special Case hides errors." It is for a case with
     the same behaviour wherever it turns up (When to Use It), and it hides
     nothing a caller needs: the book's own example can still be tested for
     explicitly, with an `isNull` method or a marker interface. Even a failure
     can be a special case, as the book's IEEE example shows: dividing by zero
     returns NaN instead of throwing.
   - **Also:** "Every caller still has to know about the Special Case." The
     finder returns it; callers call the same methods they call on a real
     customer.
   - **Worked:** `null-checks`: 1 + 2 `if` + 2 `&&` = 5; with
     `GuestCustomer`, 1.
   - **Exercise:** `NULL_ADDRESS`. **Answer:** 5 (1 + if 2 + && 1 + || 1);
     with an `UnknownAddress` whose `city()` is "unknown" and whose
     `postcode()` is empty, the caller is one line.
   - **Own:** one method in a system you know that returns null; count the
     null checks its callers make.
   - **Snippet:** `NULL_CHECKS`, 11 lines; `GUEST_CUSTOMER`, 9.
   - **Sources:** Chapter 18, Special Case.

### Course 3 — Talking to the Database (`enterprise-patterns-data-source`, 6)

Chapter 3's first half, Chapter 10, and the base patterns behind them. The four
ways for the domain to talk to the database, how finders read data, the three
situations of building a mapping, and the connection that every one of them
needs. Its `how_to` says each lesson counts what a design makes a change, a
query or a round trip cost, and that the database is the reader's to imagine,
since the labs run none; and that 3.6's lab counts only batching, one point
of Some Miscellaneous Points, while connections and Registry are read
without a count. Its `not_covered` says SQL tuning and stored
procedures are named where Fowler names them, not taught.

1. **gateways** — Gateways — *Chapter 10 · Data Source Architectural Patterns* — 15 min
   - **Read:** Chapter 3, Architectural Patterns (PDF pp. 46–49): why SQL is
     separated from domain logic (developers who know it poorly, awkward
     embedding, DBAs who want to find it), and a Gateway class per table as the
     way to do it; the anecdotal third of programming effort that mapping
     takes (*F10*). Then Chapter 18, Gateway (pp. 413–417), an object that
     wraps access to an external resource, and Chapter 10, Table Data Gateway
     (pp. 141–147), one instance for all the rows of a table, returning a
     Record Set, a map, a DTO or, with a Domain Model, domain objects (which
     Fowler is reluctant to do, for the two-way dependency). Mapper (Chapter 18, pp. 418–419) is named here and read in 3.4.
   - **Quote:** PDF p. 46, 23 words — “The rest of the application needs to
     know nothing about SQL, and all the SQL that accesses the database is
     easy to find.”
   - **Do:** count where a schema change has to be made, with and without a
     gateway.
   - **Standard:** given classes that hold SQL against one table, list the
     classes a column rename must be edited in, then redraw them through a
     gateway and list them again.
   - **Lab:** cckit `deps/ripple`. Presets `sql-everywhere` (`cart,
     price-table; checkout, price-table; report, price-table; admin,
     price-table`, changed `price-table` → `dgDirect` "4: admin, cart,
     checkout, report", `dgAffected` the same) and `one-gateway` (each of the
     four depends on `pricegateway`, and `pricegateway, price-table` →
     `dgDirect` "1: pricegateway", `dgAffected` "5: admin, cart, checkout,
     pricegateway, report"). Pins `dgDirect`, which is the lesson's count:
     the classes holding SQL against the table, the ones a column rename has
     to be edited in. The panel says `dgAffected` is an upper bound, what
     would be reached if the change got past the gateway's interface; a
     rename the gateway absorbs stops at the gateway, which is the
     quotation's claim.
   - **Misconception:** "A gateway is one more class, so a schema change
     costs more." On the lesson's illustration a column rename is edited in
     four classes without the gateway and in one with it; the extra class is
     where the SQL becomes easy to find.
   - **Worked:** `one-gateway`: one class to edit instead of four.
   - **Exercise:** `signup, member-table; profile, member-table; mailer,
     member-table; profile, mailer`, changed `member-table`. **Answer:** 3
     direct, `mailer, profile, signup`: three classes to edit; with a
     `membergateway`, one ("1: membergateway"). `dgAffected` "4: mailer,
     membergateway, profile, signup" is the upper bound, if the gateway's
     interface had to change too.
   - **Own:** one table in a system you know; grep for its name in the code
     and count the files that hold SQL against it.
   - **Snippet:** `PRICE_GATEWAY`, 16 lines.
   - **Sources:** Chapter 3, Architectural Patterns; Chapter 18, Gateway,
     Mapper; Chapter 10, Table Data Gateway; *F10*.

2. **row-data-gateway-and-finders** — Row Data Gateway, and Reading in Data — *Chapter 10 · Data Source Architectural Patterns* — 18 min
   - **Read:** Chapter 10, Row Data Gateway (PDF pp. 148–153): one object per
     row, holding the row's fields and its SQL, with finders that return it;
     where the finders go. Then Chapter 3, Reading in Data (pp. 52–53): finders
     as methods wrapping a select; static finders cannot be swapped for a
     Service Stub, so Fowler prefers finder objects; finders work on the
     database's state, not what is in memory; and the advice that is this
     lesson's quotation, with its figures (*F11*): one query that brings back
     unnecessary rows is usually better than 50 separate ones, and joins can
     really speed things up, though only up to three or four joins in a
     query.
   - **Quote:** PDF p. 52, 18 words — “It's usually better to use one query
     that brings back unnecessary rows than to issue 50 individual queries.”
   - **Do:** compare the time of fifty keyed finds with one broad query and a
     batched query, from a latency and a cost per row.
   - **Standard:** given rows wanted, rows a broad query returns, a batch size,
     a latency and a per-row cost, compute the three times and the unneeded
     rows.
   - **Lab:** eakit `load/finds`. Presets `fifty-or-one` (*F11*: wanted 50,
     broad 200, batch 10; latency 5 ms and 0.1 ms a row illustrative →
     `ldKeyedStatements` 50, `ldKeyedMs` 255, `ldBroadRows` 200, `ldBroadMs`
     25, `ldBatchStatements` 5, `ldBatchMs` 30, `ldUnneeded` 150; the batched
     strategy, keys sent `batch` at a time, is the lab's, not the book's) and
     `local-database` (latency 0.2 → `ldKeyedMs` 15, `ldBroadMs` "101/5 =
     20.20", `ldBatchMs` 6). Pins `ldKeyedMs`, `ldBroadMs`, `ldBatchMs`. The
     body says the second preset reverses the advice on its own figures, which
     is Fowler's point about measuring: the rule of thumb is a rule about
     latency.
   - **Misconception:** "Fetching only the rows you need is always cheaper."
     Each statement pays the latency; on the lesson's first preset fifty keyed
     finds take ten times as long as one query that returns four times the
     rows.
   - **Also:** "A static finder on the gateway is as good as a finder object."
     Reading in Data's point is substitutability: a static method cannot be
     replaced by a Service Stub in a test. The lesson's snippet uses a static
     finder for brevity and the body says so.
   - **Worked:** keyed 50 × (5 + 0.1) = 255 ms; broad 5 + 200 × 0.1 = 25 ms.
   - **Exercise:** wanted 30, broad 600, batch 15, latency 4 ms, 0.05 ms a row.
     **Answer:** keyed 243/2 = 121.50 ms (30 statements); broad 34 ms (570
     rows unneeded); batched 19/2 = 9.50 ms (2 statements): batching wins
     here, and the broad query beats keyed finds.
   - **Own:** one page in a system you know that loads a list; count the
     queries it issues (from a log or a profiler), and the rows each returns.
   - **Snippet:** `ORDER_ROW`, 18 lines.
   - **Sources:** Chapter 10, Row Data Gateway; Chapter 3, Reading in Data;
     *F11*.

3. **active-record** — Active Record — *Chapter 10 · Data Source Architectural Patterns* — 12 min
   - **Read:** Chapter 10, Active Record (PDF pp. 154–158): an object that
     wraps a row, holds its SQL and adds domain logic; it fits a domain model
     whose classes match the tables closely; its costs are the coupling of the
     object to the schema and the difficulty of anything the tables do not
     mirror (inheritance, collections). The contrast with Row Data Gateway
     (pp. 148–149), which has the same shape and no domain logic.
   - **Quote:** PDF p. 149, 14 words — “A Row Data Gateway should contain only
     database access logic and no domain logic.”
   - **Do:** tell an Active Record from a Row Data Gateway by what its routines
     do.
   - **Standard:** given a class over one row, sort its routines into database
     access and domain logic, and say which pattern it is.
   - **Lab:** cckit `code/class`. Presets `active-record` (`ACCOUNT_RECORD`:
     `coFields` 3, `coPublicFields` 0, `coRoutines` 3, `coPublicRoutines` 1)
     and `row-gateway` (`ACCOUNT_ROW`: 3, 0, 2, 0). Pins `coRoutines` only.
     The body says the kit counts routines and cannot tell database access
     from domain logic: the reader does the classifying, and the one routine
     the second class lacks, `canWithdraw`, is what makes the first an Active
     Record.
   - **Misconception:** "Active Record and Row Data Gateway are two names for
     one pattern." The quotation is the difference: domain logic.
   - **Also:** "Active Record cannot be tested without a database." Its
     domain methods can be, if they do not call the SQL; the coupling is in
     the find and save methods.
   - **Worked:** `active-record`: three routines, two of them SQL and one,
     `canWithdraw`, a business rule.
   - **Exercise:** `MEMBER_RECORD`. **Answer:** 4 fields, 1 public and not
     final (`email`); 3 routines (`find` and `insert` are database access,
     `level` is domain logic), so it is an Active Record.
   - **Own:** one class in a system you know that both saves itself and
     carries a business rule; list its methods in the two columns.
   - **Snippet:** `ACCOUNT_RECORD`, 19 lines; `ACCOUNT_ROW`, 15.
   - **Sources:** Chapter 10, Active Record, Row Data Gateway.

4. **data-mapper** — Data Mapper — *Chapter 10 · Data Source Architectural Patterns* — 18 min
   - **Read:** Chapter 10, Data Mapper (PDF pp. 159–172; the examples from p.
     163 are pointed to, not read): a layer of mappers that moves data
     between objects and the database while keeping them independent of each
     other and of the mapper itself; how a mapper finds and creates objects,
     uses an Identity Map and works with a Unit of Work; the cost, an extra
     layer; when to use it (a rich Domain Model, a schema that must evolve
     separately). Chapter 18, Mapper (pp. 418–419), the general form.
   - **Quote:** PDF p. 159, 14 words — “With Data Mapper the in-memory objects
     needn't know even that there's a database present”
   - **Do:** count what a database change and a domain change reach, with an
     Active Record and with a mapper.
   - **Standard:** given both designs as dependencies, list what a change to
     the database library reaches in each, and what a change to the domain
     class reaches with the mapper.
   - **Lab:** cckit `deps/ripple`. Presets `active-record` (`screen, account;
     report, account; account, jdbc`, changed `jdbc` → `dgDirect` "1:
     account", `dgAffected` "3: account, report, screen"), `mapper` (`screen,
     account; report, account; mapper, account; mapper, jdbc; main, mapper` →
     "1: mapper", "2: main, mapper"), `active-record-domain-change` (the
     first design, changed `account` → "2: report, screen", "2: report,
     screen") and `mapper-domain-change` (the mapper design,
     changed `account` → "3: mapper, report, screen", "4: main, mapper,
     report, screen"). Pins both tiles. The body says the mapper costs a
     class and moves the dependency on the domain into it: a domain change now
     reaches the mapper too.
   - **Misconception:** "A Data Mapper removes dependencies." It reverses
     them: the domain no longer depends on the database, and the mapper
     depends on both. On the lesson's illustration a domain change now has
     one more direct dependent (the mapper), and reaches two more classes
     (the mapper and the `main` that wires it).
   - **Also:** "Use a Data Mapper for every application." Fowler ties it to a
     rich Domain Model; for a simple one an Active Record is less work.
   - **Worked:** `mapper`: `jdbc` reaches `mapper` and the `main` that wires
     it; no screen or report.
   - **Exercise:** `web, invoice; invoice, customer; invoicemapper, invoice;
     invoicemapper, jdbc; customermapper, customer; customermapper, jdbc; main,
     invoicemapper; main, customermapper`, changed `jdbc`. **Answer:** direct
     2 (`customermapper, invoicemapper`), affected 3 (`customermapper,
     invoicemapper, main`); neither domain class nor `web`.
   - **Own:** one domain class in a system you know; write whether it, or
     something else, holds its SQL, and which of the four patterns that is.
   - **Snippet:** `ACCOUNT_MAPPER`, 17 lines.
   - **Sources:** Chapter 10, Data Mapper; Chapter 18, Mapper.

5. **building-the-mapping** — Building the Mapping — *Chapter 3 · Mapping to Relational Databases* — 15 min
   - **Read:** Chapter 3, Building the Mapping (PDF pp. 58–59): three
     situations (you choose the schema; you map to an existing schema that
     cannot change; you map to one whose changes are negotiable); building the
     domain model first only within short iterations (*F12*), never by
     building it for months without a database; double mapping, when the
     same kind of data comes from more than one source (two databases, or a
     database and messages), and the two answers: one mapping layer per
     source, which duplicates a lot when the data is similar, or a two-step
     mapping through a logical schema, whose second step holds the
     differences. Then Chapter 8, Down to the Data Source Layer (pp.
     102–103), which pairs each domain pattern with its data-source
     patterns.
   - **Quote:** PDF p. 58, 21 words — “Although building the model first is a
     reasonable way of thinking about it, this advice only applies within
     short iterative cycles.”
   - **Do:** find what two mappings for two sources repeat, and split them
     into a step per source and a step they share.
   - **Standard:** given mapping code for one kind of data from two sources,
     mark the repeated lines, and write the logical record and the shared
     step that would hold them once.
   - **Lab:** cckit `code/dupes`, `min_run` 2. Presets `two-sources`
     (`TWO_SOURCES`: one customer read from a table and from a message, the
     same conversion written in both → `coDupBlocks` 1, `coDupLines` 6,
     `coDupWhere` "lines 6–8 and lines 15–17") and `two-step` (`TWO_STEP`:
     each source fills a `CustomerData`, and one `toCustomer` does the rest
     → 0, 0, "none"). Pins all three. The body says the kit finds only the
     identical lines; the reading lines differ in their source calls, which
     is what the per-source step is for. `TWO_STEP` reads data in, so its
     comments number the per-source step "step one"; Fowler numbers from the
     in-memory schema outward, and his second step is the per-source one,
     which holds the differences (PDF p. 58). The body says so (added at
     authoring).
   - **Misconception:** "Design the database first, then the objects to fit."
     Fowler's advice for a Domain Model is the reverse, within short
     iterations: the model first, the database as its persistence; for a
     Transaction Script or Table Module, design the tables around the data.
   - **Also:** "Double mapping means mapping twice to the same database." It
     means the same objects fed from two sources, such as a database and a
     message feed.
   - **Worked:** `two-sources`: the constructor with its trimming and upper
     casing, the credit limit and the return appear in both mappings.
   - **Exercise:** `SHIPMENT_TWICE`, one shipment written to a table and to a
     message. **Answer:** lines 2–4 and 12–14 (`coDupBlocks` 1, `coDupLines`
     6), the reference, grams and postcode conversions; a `ShipmentData`
     filled once from the shipment, then one step per sink that writes its
     own fields.
   - **Own:** one kind of data in a system you know that arrives or leaves
     by two routes (a table and an API, a file and a queue); count the
     conversions written in both.
   - **Snippet:** `TWO_SOURCES`, 18 lines; `TWO_STEP`, 18.
   - **Sources:** Chapter 3, Building the Mapping; Chapter 8, Down to the Data
     Source Layer; *F12*.

6. **database-connections** — Database Connections and Registry — *Chapter 3 · Mapping to Relational Databases* — 15 min
   - **Read:** Chapter 3, Database Connections (PDF pp. 61–62): opening and
     closing connections, pools and why pooling is often already done for you,
     tying a connection to a transaction, and closing it reliably; Some
     Miscellaneous Points (p. 63): avoid `select *` with positional column
     indices, prefer precompiled SQL to string concatenation, and batch
     several statements into one database call. Then Chapter 18, Registry (pp.
     424–428), a well-known object for finding common objects and services
     such as a connection or a finder, scoped per process, per thread or per
     session. Fowler treats it as global data, guilty until proven innocent,
     and prefers to pass the object as a parameter; he turns to a Registry
     when the parameter would be carried through calls that do not need it
     most of the time (*F13*).
   - **Quote:** PDF p. 63, 16 words — “Many environments give you the ability to
     batch multiple SQL queries into a single database call.”
   - **Do:** compute what batching saves from a latency, a cost per statement
     and the statements of a save.
   - **Standard:** given groups of statements, a latency and a work time each,
     compute the one-at-a-time and batched times and the latency's share.
   - **Lab:** eakit `remote/calls` (the database is the remote end). Presets
     `save-an-order` (`insert-order, 1; insert-lines, 12; update-stock, 12`,
     latency 2 ms, work 0.5 ms → `rrFineTrips` 25, `rrCoarseTrips` 3,
     `rrFineMs` "125/2 = 62.50", `rrCoarseMs` "37/2 = 18.50",
     `rrLatencyShare` "4/5 = 80%", `rrSpeedup` "125/37 ≈ 3.4×") and
     `same-machine` (latency 0.1 → 25, 3, 15, "64/5 = 12.80", "1/6 ≈ 16.7%",
     "75/64 ≈ 1.2×"). Pins `rrFineMs`, `rrCoarseMs`, `rrSpeedup`. The panel
     calls a batch a coarse call; the labels say "statements" and
     "batches" here (§D.0, cfg `fine_label` and `coarse_label`, as
     the kit report's deviation 14 implements them; corrected at authoring).
   - **Misconception:** "Batching is faster because the database does less
     work." The lab holds the work the same, 25 × 0.5 ms, and batching is
     still 3.4× faster: it removes 22 of the 25 waits. The body says that
     holding the work fixed is the lab's assumption, and that a real driver
     may save some parsing and commit work as well.
   - **Also:** "A Registry is a global variable, so it is always wrong."
     Fowler's position is narrower: pass the object if you can, and use a
     Registry scoped to the thread or session when passing it would thread a
     parameter through code that does not use it.
   - **Worked:** one at a time 25 × (2 + 0.5) = 62.5 ms; batched 3 × 2 + 25 ×
     0.5 = 18.5 ms.
   - **Exercise:** `insert-invoice, 1; insert-items, 40`, latency 3 ms, work
     0.2 ms. **Answer:** 41 statements, 656/5 = 131.20 ms one at a time,
     71/5 = 14.20 ms in 2 batches, latency 15/16 ≈ 93.8% of the first,
     ≈ 9.2× faster.
   - **Own:** one save in a system you know that writes many rows; count its
     statements, and find whether the driver is batching them.
   - **Snippet:** `SAVE_LINES_BATCH`, 13 lines.
   - **Sources:** Chapter 3, Database Connections, Some Miscellaneous Points;
     Chapter 18, Registry; *F13*.

### Course 4 — Objects and Tables (`enterprise-patterns-objects-and-tables`, 8)

Chapter 3's second half with Chapters 11, 12 and 13: keeping track of what
changed, loading objects once and only when needed, keys, embedded values,
inheritance, and mapping by metadata. Its `how_to` says every lesson counts
statements, rows, writes or tables on a stated schema, and that an O/R mapping
tool does most of this for you, which is why it is worth knowing what it is
doing. Its `not_covered` says the book's long mapping examples, and the
association-table and dependent mappings beyond a paragraph each, are pointed
to, not reworked.

1. **unit-of-work** — Unit of Work — *Chapter 11 · Object-Relational Behavioral Patterns* — 18 min
   - **Read:** Chapter 3, The Behavioral Problem (PDF pp. 50–51): loading
     objects, changing some and creating others, and keeping track of which
     must be written back; Unit of Work as the answer. Then Chapter 11, Unit of
     Work (pp. 174–182; the examples from p. 178, David Rice's, pointed to):
     register new, dirty and removed objects as they happen, and write them
     all at commit;
     caller registration against object registration against unit-of-work
     controller; ordering the writes for referential integrity (p. 177, read
     in 4.4); and the illustration that one object altered at three points
     gives three calls rather than one (*F14*).
   - **Quote:** PDF p. 50, 18 words — “Instead of the application programmer
     invoking explicit save methods, the programmer tells the unit of work to
     commit.”
   - **Do:** count the writes a script of changes makes immediately and at
     commit.
   - **Standard:** given a script of loads, creations, changes and deletions,
     list the statements a Unit of Work writes at commit, in its order, and
     the writes it saves.
   - **Lab:** eakit `uow/commit`. Presets `edit-an-order` (`load, order7;
     change, order7; new, line1; new, line2; change, order7; delete, line2;
     load, customer3; change, line1` → `uwImmediate` 6, `uwCommit` 2,
     `uwSaved` "4 (2/3 ≈ 66.7%)", `uwWrites` "INSERT line1; UPDATE order7",
     `uwClean` "1: customer3") and `delete-loaded` (`load, a1; load, a2;
     change, a1; delete, a2; change, a1` → 3, 2, "1 (1/3 ≈ 33.3%)", "UPDATE
     a1; DELETE a2", "0: none"). Pins `uwCommit`, `uwWrites`, `uwSaved`. The
     body says the lab lists the writes grouped by kind (inserts, updates,
     deletes) while the snippet's commit writes them in the order the
     objects were first marked; the same statements either way, and ordering
     them for the database's keys is lesson 4.4's.
   - **Misconception:** "A Unit of Work is a database transaction." It is an
     in-memory record of changes that becomes a short system transaction at
     commit; until then the loads have read the database, but nothing has
     been written to it.
   - **Also:** "Saving each change at once is safer." On the lesson's
     illustration it writes `line2` and then deletes it, and updates `order7`
     twice; the Unit of Work writes neither the insert nor the delete of
     `line2`.
   - **Worked:** `edit-an-order`: `line2` is new and deleted, so nothing;
     `line1` is new, so one INSERT however often it changes; `order7` changed
     twice, so one UPDATE.
   - **Exercise:** `load, invoice4; new, payment1; change, invoice4; change,
     invoice4; load, account2; change, account2; new, note1; delete, note1;
     change, payment1`. **Answer:** 7 immediate writes; at commit 3, "INSERT
     payment1; UPDATE invoice4; UPDATE account2", saving 4 (4/7 ≈ 57.1%).
   - **Own:** one request in a system you know that changes several rows; list
     the statements it issues, from a log, and mark those a Unit of Work
     would merge.
   - **Snippet:** `UNIT_OF_WORK`, 20 lines: one map from object to mark, a
     rule for what each new mark does to the old one, and a commit that walks
     the map once.
   - **Sources:** Chapter 3, The Behavioral Problem; Chapter 11, Unit of Work
     (the example is David Rice's); *F14*.

2. **identity-map** — Identity Map — *Chapter 11 · Object-Relational Behavioral Patterns* — 15 min
   - **Read:** Chapter 3, The Behavioral Problem (PDF p. 50; p. 51 is blank in
     the operator's copy, corrected at authoring) on loading the same
     row twice; Chapter 11, Identity Map (pp. 183–186): a map from key to
     loaded object, consulted before every load, so each row is one object
     per session; explicit or generic maps, one per class or one per session;
     its use as a cache (the second find needs no query) and its limits (it
     does not help a query for many rows, and it is not a cache shared between
     sessions, except for read-only data, which Fowler allows to be held for
     the whole process).
   - **Quote:** PDF p. 183, 16 words — “An old proverb says that a man with two
     watches never knows what time it is.”
   - **Do:** count the rows a session's finds load, and the duplicate objects
     an Identity Map prevents.
   - **Standard:** given a session's finds in order, count the distinct rows,
     the duplicates and which object is shared by whom.
   - **Lab:** eakit `load/identity`. Presets `one-session` (`customer, 7;
     order, 31; customer, 7; order, 32; customer, 7; product, 5; product, 5`
     → `ldFinds` 7, `ldDistinct` 4, `ldDuplicates` 3, `ldShared` "customer 7
     ×3, product 5 ×2") and `no-repeats` (`customer, 7; order, 31; product, 5`
     → 3, 3, 0, "none"). Pins all four.
   - **Misconception:** "An Identity Map is a performance cache." Fowler's
     first reason is correctness: without it two objects for one row can be
     changed separately and one change lost. Saving the query is the second.
   - **Also:** "One map for the whole server." It is per session (or per
     business transaction), so that two users do not share each other's
     uncommitted objects; the exception is objects nobody can change, whose
     map may be shared by the whole process.
   - **Worked:** `one-session`: seven finds load four rows; without the map,
     three objects duplicate one already loaded.
   - **Exercise:** `room, 12; guest, 3; room, 14; guest, 3; room, 12; guest,
     9; guest, 3`. **Answer:** 7 finds, 4 distinct, 3 duplicates: room 12 ×2,
     guest 3 ×3.
   - **Own:** one request in a system you know; count how often it loads the
     same row, from a query log.
   - **Snippet:** `IDENTITY_MAP`, 19 lines.
   - **Sources:** Chapter 3, The Behavioral Problem; Chapter 11, Identity Map.

3. **lazy-load** — Lazy Load — *Chapter 11 · Object-Relational Behavioral Patterns* — 18 min
   - **Read:** Chapter 11, Lazy Load (PDF pp. 187–199; the examples from p. 189
     pointed to): an object that does not hold all its data but knows how to
     get it; four ways, lazy initialization, virtual proxy, value holder and
     ghost; the danger of ripple loading, where a collection of lazy objects
     looked at one by one issues a query each, and the cures (load the whole
     collection at once, or design the lazy boundary round how the data is
     used). Chapter 3, Reading in Data (p. 52) on joins against separate
     queries (*F11*).
   - **Quote:** PDF p. 187, 24 words — “As many people know, if you're lazy
     about doing things you'll win when it turns out you don't need to do
     them at all.”
   - **Do:** count the statements and rows four loading strategies issue for
     the same parents and children.
   - **Standard:** given parents, their child counts and which parents'
     children are used, compute statements and rows lazily, lazily in
     batches, with two queries and with one join.
   - **Lab:** eakit `load/graph`. Presets `orders-and-lines` (`o1, 3, yes; o2,
     0, no; o3, 5, yes; o4, 2, no; o5, 4, yes`, batch 2 → `ldLazy` "4
     statements, 17 rows", `ldBatched` "3 statements, 17 rows",
     `ldTwoQueries` "2 statements, 19 rows", `ldJoin` "1 statement, 15 rows")
     and `every-order-used` (`o1, 3, yes; o2, 0, yes; o3, 5, yes; o4, 2, yes;
     o5, 4, yes`, every order used → "6 statements, 19 rows", "4 statements,
     19 rows", "2 statements, 19 rows", "1 statement, 15 rows"). Pins all
     four. The panel states each strategy's rule (§D.1), including that a
     join returns one row for a parent with no children, and that the lab
     counts rows, not their width: a join's rows each repeat the parent's
     columns, which no tile shows.
   - **Misconception:** "Lazy loading always loads less." When every child is
     used, lazy loading and two queries return the same 19 rows, and the
     lazy strategy takes 1 + 5 statements to do it where two queries take 2;
     it saves only what is not used.
   - **Worked:** `orders-and-lines`: the first query returns 5 orders; three
     are used, so 3 more statements returning 3 + 5 + 4 = 12 lines: 4
     statements, 17 rows.
   - **Exercise:** `a, 10, yes; b, 0, no; c, 2, no; d, 6, yes; e, 1, no; f, 3,
     yes`, batch 3. **Answer:** lazy 4 statements, 25 rows; batched 2, 25;
     two queries 2, 28; join 1, 23.
   - **Own:** one list page in a system you know; count its queries with the
     list at 10 rows and at 50, and say whether it ripple-loads.
   - **Snippet:** `LAZY_LINES`, 19 lines (lazy initialization, with a flag
     for whether the lines have been loaded).
   - **Sources:** Chapter 11, Lazy Load; Chapter 3, Reading in Data; *F11*.

4. **identity-field-and-foreign-keys** — Identity Field and Foreign Keys — *Chapter 12 · Object-Relational Structural Patterns* — 18 min
   - **Read:** Chapter 3, Structural Mapping Patterns, Mapping Relationships
     (PDF pp. 53–55): objects link by reference, tables by key; collections
     reverse the direction (an order holds its lines; the line row holds the
     order's key); referential integrity, where Fowler's first advice is to
     defer the checks to the end of the transaction if the database can, and
     only otherwise to order the updates, with a topological sort of the
     writes as one technique (p. 55, and Unit of Work p. 177). Then Chapter 12: Identity Field (pp. 201–217, examples pointed
     to), meaningful against meaningless keys, simple against compound, table-
     against database-unique, and how keys are generated (auto-generated
     fields, GUIDs, a key table); Foreign Key Mapping (pp. 218–228);
     Association Table Mapping (pp. 229–240) for many-to-many; Dependent
     Mapping (pp. 241–245) for objects that belong to one owner.
   - **Quote:** PDF p. 53, 11 words — “Relational databases handle links by
     forming a key into another table.”
   - **Do:** order inserts and deletes so that no row refers to a row that
     is not there.
   - **Standard:** given which tables hold foreign keys to which, write an
     insert order and a delete order, and find the broken pairs in a given
     order.
   - **Lab:** eakit `uow/order`. Presets `order-schema` (`orders, customer;
     line, orders; line, product; payment, orders`, as `line orders customer
     product payment` → `uwInsertOrder` "customer, orders, payment, product,
     line", `uwDeleteOrder` "line, product, payment, orders, customer",
     `uwBroken` "3: orders before customer, line before orders, line before
     product") and `schema-only` (no order given → the two orders). Pins all
     three. The panel says ties are broken alphabetically, so the insert
     order is one of several valid ones, and that the lab models a database
     that checks every statement: with the checks deferred to commit, the
     order would not matter.
   - **Misconception:** "Meaningful keys, such as an email address, save a
     column." Fowler takes "a rare stand on the side of meaninglessness": a
     meaningful key can change or be mistyped, and every foreign key holding
     it must change with it. He allows that small or very stable systems may
     get away with one.
   - **Also:** "The object should hold its children's keys." The table
     structure is the reverse of the object structure; the child holds the
     parent's key (Mapping Relationships).
   - **Worked:** `customer` and `product` depend on nothing; `orders` needs
     `customer`; `payment` needs `orders`; `line` needs both `orders` and
     `product`, so it goes last.
   - **Exercise:** `booking, guest; booking, room; room, hotel; charge,
     booking`, in the order `hotel guest booking room charge`. **Answer:** one
     broken pair, "booking before room"; a valid insert order is guest, hotel,
     room, booking, charge, and deletes go in reverse.
   - **Own:** one schema you know; write its tables in an order that inserts
     safely, and find one foreign key whose column holds a meaningful value.
   - **Snippet:** `SAVE_NEW_ORDER`, 9 lines.
   - **Sources:** Chapter 3, Mapping Relationships; Chapter 11, Unit of Work;
     Chapter 12, Identity Field, Foreign Key Mapping, Association Table
     Mapping, Dependent Mapping.

5. **embedded-value-and-serialized-lob** — Embedded Value and Serialized LOB — *Chapter 12 · Object-Relational Structural Patterns* — 15 min
   - **Read:** Chapter 3, Structural Mapping Patterns (PDF p. 55), on objects
     that are not worth a table of their own. Chapter 12, Embedded Value (pp.
     246–248): a small Value Object (a date range, a money amount) stored as
     fields in its owner's row; Serialized LOB (pp. 249–253): a graph of
     objects (a tree, say) serialized into one large column, binary or text,
     at the cost of being invisible to SQL and to anything that reads the
     database without the application.
   - **Quote:** PDF p. 55, 20 words — “If you use it too much, it ends up
     turning your database into little more than a transactional file
     system.”
   - **Do:** count the queries that read a tree under three storage choices.
   - **Standard:** given a tree as node, parent records, state its depth and
     the queries to read it one node at a time, one level at a time, and from
     one column.
   - **Lab:** eakit `load/tree`. Presets `departments` (`company, -; sales,
     company; north, sales; south, sales; it, company; support, it; desk,
     support; field, support` → `ldNodes` 8, `ldDepth` 4, `ldPerNode` 9,
     `ldPerLevel` 5, `ldLob` 1) and `flat` (`company, -; sales, company; it,
     company; legal, company` → 4, 2, 5, 3, 1). Pins `ldPerNode`,
     `ldPerLevel`. The panel states the three rules (§D.1), and that both
     counts include the queries that come back empty: a leaf's query for its
     children, and the query for the level below the deepest.
   - **Misconception:** "A Serialized LOB is the fast choice, so prefer it."
     It is one read, and nothing else can query inside it; Fowler's caution is
     the quotation.
   - **Also:** "An Embedded Value needs its own key." It has none: it is part of
     its owner's row, which is why it suits a Value Object.
   - **Worked:** `departments`: 1 + 8 = 9 queries node by node (one for the
     root, then one for each node's children), 4 + 1 = 5 level by level (the
     fifth finds nothing below the deepest level), 1 as a LOB.
   - **Exercise:** `root, -; a, root; b, a; c, b; d, c; e, root`. **Answer:** 6
     nodes, depth 5: 7 queries node by node, 6 level by level, 1 as a LOB.
   - **Own:** one column in a schema you know that holds JSON or XML; write
     one query someone might want that it now prevents.
   - **Snippet:** `EMBEDDED_TERM`, 7 lines; `LOB_TEXT`, 9.
   - **Sources:** Chapter 3, Structural Mapping Patterns; Chapter 12, Embedded
     Value, Serialized LOB.

6. **single-table-inheritance** — Single Table Inheritance — *Chapter 12 · Object-Relational Structural Patterns* — 15 min
   - **Read:** Chapter 3, Inheritance (PDF pp. 55–57): the three ways to map a
     hierarchy, and the trade-off between duplication of structure and speed
     of access. Chapter 12, Single Table Inheritance (pp. 254–260): every class
     in one table, with a type code; no joins, one place to change; but wasted
     space for the columns a row's class does not use, and one large table
     that every access contends for.
   - **Quote:** PDF p. 57, 13 words — “The trade-offs are all between
     duplication of data structure and speed of access.”
   - **Do:** count the tables, columns, empty columns and tables touched for a
     hierarchy under all three mappings.
   - **Standard:** given a hierarchy with each class's own field count, state
     single-table's tables and columns, and the columns empty in a given
     class's row.
   - **Lab:** eakit `inherit/tables`. Presets `staff` (`person, -, 3, no;
     employee, person, 2, yes; manager, employee, 2, yes; contractor, person,
     2, yes`, load `manager`, find `person`, alter `person` → `ihTables` "1,
     4, 3", `ihColumns` "11, 13, 20", `ihEmpty` 2, `ihLoad` "1, 3, 1",
     `ihFind` "1, 4, 3", `ihAlter` "1, 1, 3") and `load-an-employee` (load
     `employee`, find `employee`, alter `manager` → `ihEmpty` 4, `ihLoad` "1,
     2, 1", `ihFind` "1, 3, 2", `ihAlter` "1, 1, 1"). Each three-part tile is
     single, class, concrete, in that order. Pins `ihColumns`, `ihEmpty`,
     `ihLoad`. This lesson reads the single-table figure of each; 4.7 the
     other two.
   - **Misconception:** "Single Table Inheritance is the beginner's mapping."
     Fowler names its great advantage: everything in one place, with no
     joins; its costs are empty columns and size.
   - **Also:** "The empty columns waste most of the table." Fowler notes that
     many databases compress them; on the lesson's illustration a manager's
     row leaves 2 of 9 field columns empty.
   - **Worked:** `staff`: one table with a key, a type code and 3 + 2 + 2 + 2
     field columns, 11; a manager uses 7 of the 9 fields, so 2 are empty.
   - **Exercise:** `vehicle, -, 4, no; car, vehicle, 2, yes; van, vehicle, 3,
     yes; truck, vehicle, 5, yes`, load `van`. **Answer:** single table 16
     columns, 7 empty in a van's row; class table 18 columns in 4 tables;
     concrete 25 in 3.
   - **Own:** one hierarchy in a system you know; write which of the three
     mappings it uses and count the columns a row of its largest subclass
     leaves empty.
   - **Snippet:** `SINGLE_TABLE_LOAD`, 13 lines.
   - **Sources:** Chapter 3, Inheritance; Chapter 12, Single Table Inheritance.

7. **class-and-concrete-table-inheritance** — Class and Concrete Table Inheritance — *Chapter 12 · Object-Relational Structural Patterns* — 18 min
   - **Read:** Chapter 12, Class Table Inheritance (PDF pp. 261–268): a table
     per class, with a join (or several queries) to load one object, and the
     simplest correspondence between classes and tables; Concrete Table
     Inheritance (pp. 269–276): a table per concrete class holding all its
     inherited fields, no join to load, but brittle: a superclass change alters
     every table, and keys must be unique across them; Inheritance Mappers
     (pp. 277–278), the structure of mapper classes for all three. Chapter 3,
     Inheritance (p. 57), on mixing the three in one hierarchy.
   - **Quote:** PDF p. 262, 21 words — “You need to touch multiple tables to load
     an object, which means a join or multiple queries and sewing in memory.”
     The body also quotes Inheritance Mappers' “a heinous crime” (PDF p. 278,
     3 words; ea_quotes.py OK), for a lesson total of 24 (added at authoring).
   - **Do:** count what loading, finding and altering touch under class- and
     concrete-table mappings.
   - **Standard:** given a hierarchy, a class to load, a class to find all
     instances of and a class to alter, state the tables each touches under
     each mapping.
   - **Lab:** eakit `inherit/tables`, as 4.6. Presets `staff-find-person` (as
     4.6's `staff` → `ihLoad` "1, 3, 1", `ihFind` "1, 4, 3", `ihAlter` "1, 1,
     3") and `staff-find-employee` (load `contractor`, find `employee`, alter
     `employee` → `ihLoad` "1, 2, 1", `ihFind` "1, 3, 2", `ihAlter` "1, 1,
     2"). Pins `ihLoad`, `ihFind`, `ihAlter`. The panel states the rules
     (§D.1): a class-table find on a class joins its ancestors and unions its
     descendants; a concrete-table find unions the concrete tables below it.
   - **Misconception:** "Concrete Table Inheritance is the fast one, so it is
     the best." It loads from one table, but a find on the superclass
     touches every concrete table, and altering the superclass alters all
     of them: on the lesson's illustration 3 tables each time.
   - **Also:** "Class Table Inheritance needs one join per class in the
     hierarchy." It needs one per ancestor of the class loaded; a contractor
     touches 2 tables, a manager 3.
   - **Worked:** `staff-find-person`: a manager's row is split across person,
     employee and manager, 3 tables; under concrete table it is one table of
     1 + 3 + 2 + 2 = 8 columns.
   - **Exercise:** `account, -, 3, no; saving, account, 2, yes; isa, saving, 1,
     yes; current, account, 2, yes`, load `isa`, find `saving`, alter
     `account`. **Answer:** load 1, 3, 1; find `saving` 1, 3, 2 (class table
     joins account and unions isa); alter `account` 1, 1, 3.
   - **Own:** the hierarchy from 4.6's step; count the tables a query for all
     instances of its root touches under each mapping.
   - **Snippet:** `CLASS_TABLE_FIND`, 7 lines (a SQL string constant).
   - **Sources:** Chapter 12, Class Table Inheritance, Concrete Table
     Inheritance, Inheritance Mappers; Chapter 3, Inheritance.

8. **metadata-query-object-repository** — Metadata Mapping, Query Object and Repository — *Chapter 13 · Object-Relational Metadata Mapping Patterns* — 18 min
   - **Read:** Chapter 3, Using Metadata (PDF p. 60): handwritten mapping is
     simple and repetitive, which signals a design problem, and Metadata
     Mapping holds the mapping as data, used by code generation or
     reflection. Chapter 13: Metadata Mapping (pp. 280–288), with its warning
     that a simple scheme covers about 90 percent of cases and the rest is
     hard (*F15*); Query Object (pp. 289–293), a query built as an object
     from criteria in domain terms, which Fowler says most projects with a
     hand-built data source layer do without (p. 290); Repository, by Edward
     Hieatt and Rob Mee (pp. 294–298), a collection-like
     interface for finding domain objects, behind which queries and mapping
     sit.
   - **Quote:** PDF p. 60, 25 words — “With simple and repetitive mapping this
     can lead to code that's simple and repetitive—and repetitive code is a
     sign of something wrong with the design.”
   - **Do:** find the simple and repetitive mapping code that two
     hand-written finders share, and hold the mapping as data instead.
   - **Standard:** given two hand-written finders for two classes, mark the
     lines they repeat, and write the metadata (column and field) that a
     single finder would read.
   - **Lab:** cckit `code/dupes`, `min_run` 2. Presets `hand-mapping`
     (`HAND_MAPPING`: a member and a shop found by key, each with its own
     prepare, bind, execute and field copying → `coDupBlocks` 1,
     `coDupLines` 6, `coDupWhere` "lines 3–5 and lines 13–15") and
     `metadata-find` (`METADATA_FIND`: one finder that reads a table of
     columns and fields by reflection → 0, 0, "none"). Pins all three. The
     body says the kit finds only the identical lines; the field-copying
     lines differ only in their names, which is exactly what the metadata
     holds. It says Query Object, by Fowler's own When to Use It, is left out
     of most projects with a hand-built data source layer and is really
     needed only with a Domain Model, Data Mapper and Metadata Mapping
     together, which is why the lab does not count one.
   - **Misconception:** "Metadata mapping removes the mapping work." It moves
     it into the metadata and the code that reads it; Fowler's 90 percent
     warning is about the rest.
   - **Also:** "A Repository is a Data Mapper with a new name." It sits above
     the mappers and offers a collection, so that domain code asks for
     objects by criteria without knowing about the queries.
   - **Worked:** `hand-mapping`: lines 3–5 and 13–15, the bind, execute and
     `next`, three lines twice; the copying lines below them repeat in shape
     with different names.
   - **Exercise:** `INVOICE_FINDERS`. **Answer:** lines 3–5 and 14–16
     (`coDupBlocks` 1, `coDupLines` 6); the metadata is `{"total", "total"},
     {"due", "due"}` for the invoice and `{"paid", "paid"}` for the receipt,
     and both finders become calls to the one metadata finder.
   - **Own:** the finders of one class in a system you know; count them, and
     the lines each shares with the others.
   - **Snippet:** `HAND_MAPPING`, 20 lines; `METADATA_FIND`, 18.
   - **Sources:** Chapter 3, Using Metadata; Chapter 13, Metadata Mapping,
     Query Object, Repository (Edward Hieatt and Rob Mee); *F15*.

### Course 5 — Web Presentation (`enterprise-patterns-web-presentation`, 6)

Chapters 4 and 14. Model View Controller as the separation underneath, the two
input controllers, the two view patterns and the two-stage variation, and
Application Controller for flow. Every lab here reuses cckit, because what each
pattern changes is code: which lines repeat across pages, how many decisions a
page holds, and what a change to the look reaches. Its `how_to` says so. Its
`not_covered` says rich clients, JavaScript frameworks and the servlet and ASP.NET
specifics of the book's examples are named, not taught. The course's §F.4
aside is in Template View and Transform View.

1. **model-view-controller** — Model View Controller — *Chapter 14 · Web Presentation Patterns* — 15 min
   - **Read:** Chapter 4's opening (PDF pp. 65–66): scripts and server pages,
     and the input controller, model and view of a web request. Then Chapter
     14, Model View Controller (pp. 300–301): two separations, of presentation
     from model, which Fowler counts among the most important design
     principles, and of view from controller, which matters much less in rich
     clients and more on the web; the model never refers to the view.
   - **Quote:** PDF p. 301, 16 words — “the separation of presentation and
     model is one of the most important design principles in software”
   - **Do:** count what a change to the HTML library reaches when the model
     does, and does not, know about HTML.
   - **Standard:** given the dependencies of a model, two presentations and an
     HTML library, list what a change to the library reaches, then redraw
     with the model independent and list it again.
   - **Lab:** cckit `deps/ripple`. Presets `model-knows-html` (`concert,
     html; concertpage, concert; concertreport, concert`, changed `html` →
     `dgDirect` "1: concert", `dgAffected` "3: concert, concertpage,
     concertreport") and `separated` (`concertpage, concert; concertpage,
     html; concertreport, concert` → "1: concertpage", "1: concertpage").
     Pins both tiles.
   - **Misconception:** "MVC is three folders." Fowler's point is the
     direction of the dependencies; on the lesson's illustration the report,
     which has nothing to do with HTML, is reached by an HTML change only
     because the model knew about HTML.
   - **Also:** "The controller is where the business logic goes." On the web
     the controller handles the request and picks the view, with helper
     objects for the decisions; the logic is in the model (Chapter 4).
   - **Worked:** `separated`: only the page that renders HTML depends on it.
   - **Exercise:** `basket, widgets; checkoutpage, basket; basketapi, basket;
     checkoutpage, widgets`, changed `widgets`. **Answer:** direct 2 (`basket,
     checkoutpage`), affected 3 (`basket, basketapi, checkoutpage`); remove
     `basket, widgets` and only `checkoutpage` is reached ("1: checkoutpage").
   - **Own:** one model class in a system you know; grep its imports for
     anything from the presentation layer.
   - **Snippet:** `CONCERT_MODEL`, 18 lines.
   - **Sources:** Chapter 4; Chapter 14, Model View Controller.

2. **page-controller** — Page Controller — *Chapter 14 · Web Presentation Patterns* — 15 min
   - **Read:** Chapter 4, Input Controller Patterns (PDF p. 70): an input
     controller for each page, or more precisely for each action; the two
     jobs of handling the request and deciding what to do. Chapter 14, Page
     Controller (pp. 302–311; examples pointed to): a controller per page,
     as a server page or a separate object, which decodes the request, asks
     the model and picks the view; helpers for the decisions.
   - **Quote:** PDF p. 65, 26 words — “Things get a lot more messy when you have
     to make decisions based on the input, such as different display formats
     for classical and jazz albums.”
   - **Do:** count the decisions a page controller makes, and move the
     choice of view to a helper.
   - **Standard:** given a page controller, count its decision points, and
     write the helper method that picks the view from the model's
     predicates.
   - **Lab:** cckit `code/complexity`, `bands` [5, 10]. Presets `concert-page`
     (`CONCERT_PAGE`: 5, "1 + if 3 + && 1", "0–5", 1, "line 5") and
     `concert-page-split` (`CONCERT_PAGE_SPLIT`: 1, "1", "0–5", 0, "line 4").
     Pins `coDecisions`, `coBreakdown`. The body says the four branches have
     moved to a presentation-side helper, `ConcertPageHelper.viewFor`, not
     disappeared; the model keeps only its domain predicates (`isSoldOut`,
     `isSeated`, `hasSeatMap`) and never names a page, as 5.1 requires.
   - **Misconception:** "A page controller is a page." Fowler's more precise
     version is one controller per action, which is usually but not always one
     per page.
   - **Also:** "Moving the decision out removes it." It moves it to a place it
     can be tested without HTTP.
   - **Worked:** `concert-page`: 1 + 3 `if` + 1 `&&` = 5.
   - **Exercise:** `BOOKING_PAGE`. **Answer:** 7 (1 + if 3 + && 1 + || 2):
     the null checks, the seat range and the paid-and-not-refundable rule; the
     seat range and the refund rule belong to `Booking` as predicates, and
     the choice of page belongs to the helper.
   - **Own:** one controller in a system you know; count its decision points,
     and mark the ones that are about the domain, not the request.
   - **Snippet:** `CONCERT_PAGE`, 13 lines; `CONCERT_PAGE_SPLIT`, 6.
   - **Sources:** Chapter 4, Input Controller Patterns; Chapter 14, Page
     Controller.

3. **front-controller** — Front Controller — *Chapter 14 · Web Presentation Patterns* — 15 min
   - **Read:** Chapter 4, Input Controller Patterns (PDF p. 70; p. 71 is
     Further Reading, corrected at authoring) on Front
     Controller; Chapter 14, Front Controller (pp. 312–317): one handler for
     every request, which does the common work (security, logging,
     internationalisation) and dispatches to a command per action, chosen
     statically or dynamically; decorating it with filters (Intercepting
     Filter, as the book cites Alur, Crupi and Malks); Fowler's judgement that
     it is more complex than Page Controller and needs advantages to be worth
     it: one handler to configure, commands added without changes, a new
     command per request so no thread-safety worries, and decorators. He
     answers the commonly stated one, removing duplicated code, with a
     superclass Page Controller.
   - **Quote:** PDF p. 314, 21 words — “Only one Front Controller has to be
     configured into the Web server; the Web handler does the rest of the
     dispatching.”
   - **Do:** find the lines that page controllers repeat, and remove them two
     ways: a superclass, and one handler.
   - **Standard:** given two page controllers, mark the repeated lines, write
     the superclass that runs them once, and name what a front handler
     offers beyond that.
   - **Lab:** cckit `code/dupes`, `min_run` 2. Presets `pages-repeat`
     (`PAGES_REPEAT`: 1, 6, "lines 2–4 and lines 9–11"), `page-superclass`
     (`PAGES_SUPERCLASS`: the two pages extend a `SecurePage` Layer
     Supertype that runs the three lines → 0, 0, "none") and `front-handler`
     (`FRONT_HANDLER`: 0, 0, "none"). Pins all three. The body says the
     count cannot choose between the second and third presets, which both
     reach 0, and gives Fowler's four reasons for the Front Controller.
   - **Misconception:** "A Front Controller is one huge controller." It is one
     handler and many small commands; the handler does only what every
     request shares.
   - **Also:** "Front Controller is the only way to remove what page
     controllers repeat." A superclass Page Controller removes it too, as
     the `page-superclass` preset shows; Fowler's reasons for one handler
     are configuration, dynamic commands, thread safety and decorators.
   - **Worked:** `pages-repeat`: the session check, login redirect and audit,
     three lines in each page.
   - **Exercise:** `REPORTS_REPEAT`. **Answer:** lines 2–3 and 9–10 (4 lines),
     the cache header and the locale, which a superclass or a front handler
     sets once.
   - **Own:** the first lines of three controllers in a system you know; count
     the lines they share.
   - **Snippet:** `PAGES_REPEAT`, 13 lines; `PAGES_SUPERCLASS`, 20;
     `FRONT_HANDLER`, 8.
   - **Sources:** Chapter 4; Chapter 14, Front Controller; Alur, Crupi and
     Malks as the book cites them.

4. **template-and-transform-view** — Template View and Transform View — *Chapter 14 · Web Presentation Patterns* — 18 min
   - **Read:** Chapter 4, View Patterns (PDF pp. 67–69): the two single-stage
     choices; server pages allow full programming in the page, with the
     quotation's consequence, and the discipline of a helper object.
     Chapter 14, Template View (pp. 318–326): markers in the page's
     structure, a helper that holds the logic, and conditional display and
     iteration as the hard cases; Transform View (pp. 327–330): a program that
     walks the domain data element by element and transforms it, usually in
     XSLT, which keeps logic out of the page but is a different language to
     learn.
   - **Quote:** PDF p. 67, 21 words — “This clearly provides a lot of power and
     flexibility; sadly, it also leads to very messy code that's difficult to
     maintain.”
   - **Do:** count the decisions in a page fragment, and move them to a
     helper the template asks.
   - **Standard:** given a page fragment with its logic inline, count its
     decision points, and write the helper methods a template would call.
   - **Lab:** cckit `code/complexity`, `bands` [5, 10]. Presets `ticket-row`
     (`TICKET_ROW`: a concert's ticket row, its "few left" and resale marks
     decided inline → 5, "1 + if 2 + && 1 + || 1", "0–5", 1, "line 5") and
     `ticket-helper` (`TICKET_HELPER`: 3, "1 + && 1 + || 1", "0–5", 2, "line
     6"). Pins `coDecisions`, `coBreakdown`. The body says the helper keeps
     the two conditions as named methods, so the template has none.
   - **Misconception:** "A template with no code in it cannot show anything
     conditional." Template View's hard cases are exactly conditional display
     and iteration, and Fowler's answer is a helper that decides and a marker
     that asks it.
   - **Also:** "Transform View needs XSLT." Fowler's examples are XSLT, but
     the pattern is a transformation element by element, in any language.
   - **Worked:** `ticket-row`: 1 + 2 `if` + 1 `||` + 1 `&&` = 5, inside the
     HTML-building code.
   - **Exercise:** `PRICE_CELL`. **Answer:** 5 (1 + if 2 + && 1 + || 1); a
     helper with `showWasPrice()` and `isUnavailable()`.
   - **Own:** one template in a system you know; count the conditionals in
     it.
   - **Snippet:** `TICKET_ROW`, 13 lines; `TICKET_HELPER`, 11.
   - **Sources:** Chapter 4, View Patterns; Chapter 14, Template View,
     Transform View.
   - **§F.4 aside** (this course's one): the book was written for server-built
     pages; much of today's presentation is built in the browser, where the
     same separation (a component that renders, data it is given) is argued
     afresh. Stated in the `note`, at strength, unsettled.

5. **two-step-view** — Two Step View — *Chapter 14 · Web Presentation Patterns* — 15 min
   - **Read:** Chapter 4, View Patterns (PDF p. 69) on the second stage;
     Chapter 14, Two Step View (pp. 331–343; examples pointed to): the first
     stage turns domain data into a logical screen with no formatting, and the
     second turns logical screens into HTML, so a site-wide change of look is
     made in one place and a site can have several looks (ten screens and
     three appearances: thirty single-stage views against thirteen stages,
     *F24*, p. 336); its cost, that the logical screen has to be designed and
     every page fits it.
   - **Quote:** PDF p. 333, 22 words — “Two Step View's key value comes from the
     separation of first and second stages, allowing you to make global
     changes more easily.”
   - **Do:** count what a change to the site's look reaches with one stage
     and with two.
   - **Standard:** given pages that each format their own HTML, list what a
     change of look reaches; then redraw with a logical screen and a renderer
     and list it again.
   - **Lab:** cckit `deps/ripple`. Presets `one-step` (`concertpage, look;
     venuepage, look; tourpage, look; concertpage, concert; venuepage,
     venue`, changed `look` → `dgDirect` "3: concertpage, tourpage,
     venuepage", `dgAffected` the same) and `two-step` (the pages depend on
     `screen`; `renderer, screen; renderer, look` → "1: renderer", "1:
     renderer"). Pins both tiles.
   - **Misconception:** "Two Step View is two templates per page." It is one
     first stage per page and one second stage for the site.
   - **Also:** "It makes every change cheaper." A change to the logical screen
     reaches every page and every renderer; the exercise shows it.
   - **Worked:** `two-step`: a change of look reaches only `renderer`.
   - **Exercise:** `home, screen; search, screen; account, screen; renderer,
     screen; renderer, look; printrenderer, screen; printrenderer,
     printlook`, changed `screen`. **Answer:** 5 direct and 5 affected:
     account, home, printrenderer, renderer, search.
   - **Own:** one site-wide change you have made to a look; count the files it
     touched.
   - **Snippet:** `SECOND_STAGE`, 20 lines.
   - **Sources:** Chapter 4, View Patterns; Chapter 14, Two Step View.

6. **application-controller** — Application Controller — *Chapter 14 · Web Presentation Patterns* — 15 min
   - **Read:** Chapter 4's opening (PDF p. 66) on screen flow and the test
     of who controls it, and Further Reading (p. 71) for the terminology
     taken from Knight and Dai (corrected at authoring: Input Controller
     Patterns, p. 70, does not discuss flow); Chapter 14, Application Controller (pp. 344–350): a central point
     for screen navigation and flow, which input controllers ask for the
     domain command to run and the view to show next; it adds little when
     any screen can be visited in pretty much any order, and its strength is
     definite rules about the order of pages and views that depend on the
     state of objects; its ideas came, Fowler says, from Knight and Dai. Chapter 8's Other Layering
     Schemes (read in 7.4) places it as the mediating layer of the Brown
     model.
   - **Quote:** PDF p. 346, 28 words — “A good signal to use an Application
     Controller is if you find yourself having to make similar changes in lots
     of different places when your application's flow changes.”
   - **Do:** find flow decisions repeated across controllers and move them
     to one.
   - **Standard:** given two controllers, mark the repeated flow lines and
     write the application controller's method.
   - **Lab:** cckit `code/dupes`, `min_run` 2. Presets `flow-repeat`
     (`FLOW_REPEAT`: 1, 6, "lines 2–4 and lines 9–11") and `next-screen`
     (`NEXT_SCREEN`: 0, 0, "none"). Pins all three.
   - **Misconception:** "Every web application needs an Application
     Controller." Fowler's signal is the quotation; where any screen can be
     visited in any order there are no rules for it to hold, and it adds
     little.
   - **Also:** "The application controller does the work." It decides what
     comes next; the domain commands do the work.
   - **Worked:** `flow-repeat`: the customs, approval and payment lines
     appear in both controllers.
   - **Exercise:** `CLAIM_FLOW`. **Answer:** lines 2–4 and 9–11 (6 lines): the
     assessor, medical and bank steps; one `nextStep(Claim c)` replaces them.
   - **Own:** one wizard or checkout in a system you know; count the places
     its order of screens is written down.
   - **Snippet:** `FLOW_REPEAT`, 12 lines; `NEXT_SCREEN`, 7.
   - **Sources:** Chapter 4; Chapter 14, Application Controller; Chapter 8,
     Other Layering Schemes; Knight and Dai, as the book cites them.

### Course 6 — Concurrency and Session State (`enterprise-patterns-concurrency-and-session-state`, 7)

Chapters 5, 6, 16 and 17: what goes wrong when two people work on the same
data, how locks and transactions prevent or detect it, and where a session's
state lives between requests. Chapter 5 is by Fowler and David Rice, and
Chapter 16's patterns are Rice's (Coarse-Grained Lock with Matt Foemmel); the
lessons name them. Its `how_to` says the labs replay a stated
timeline of sessions, and that real concurrency bugs are not reproducible on
demand, which is Fowler's reason for preferring designs that avoid them. Its
`not_covered` says explicit thread programming and the internals of database
locking are named, not taught.

1. **concurrency-problems** — Concurrency Problems — *Chapter 5 · Concurrency* — 18 min
   - **Read:** Chapter 5's opening (PDF p. 72): offline concurrency, across
     several database transactions, as the book's concern. Concurrency
     Problems (p. 73): lost updates and inconsistent reads, with Martin counting the
     classes in two packages while David adds to both (*F16*), and the trade
     between correctness and liveness. Execution Contexts (p. 74): request, session, process and
     thread, and business against system transactions. Isolation and
     Immutability (p. 75): the two ways to avoid concurrency problems
     altogether.
   - **Quote:** PDF p. 73, 8 words — “Sadly, fifteen classes was never the right
     answer.”
   - **Do:** compute what a reader sees when a commit falls between two reads.
   - **Standard:** given items with values before and after a commit and
     which side of it each was read, compute the total seen and say whether it
     matches either state.
   - **Lab:** eakit `lock/reads`. Presets `martin-and-david` (*F16*: `locking,
     7, 9, before, insert; multiphase, 5, 8, after, insert` → `olSeen` 15,
     `olBefore` 12, `olAfter` 17, `olConsistent` "no: 15 is neither 12 nor
     17"), `both-after` (17; "yes: the state after the commit") and
     `both-before` (12; "yes: the state before the commit"). Pins `olSeen`,
     `olConsistent`. `olLevel` is read in 6.3.
   - **Misconception:** "If every read is of correct data, the result is
     correct." Each count Martin reads is correct when he reads it; the sum
     is of no state the database was ever in.
   - **Also:** "Concurrency problems need two people to write." An
     inconsistent read needs one writer and one reader.
   - **Worked:** 7 + 8 = 15, against 7 + 5 = 12 before David's commit and 9
     + 8 = 17 after.
   - **Exercise:** `cash, 400, 300, after, update; savings, 600, 700, before,
     update` (a transfer of 100). **Answer:** 900 seen against 1,000 both
     before and after: "no: 900 is not 1,000, before or after".
   - **Own:** one report in a system you know that reads several tables
     while others write; say which commit could fall between its reads.
   - **Snippet:** `COUNT_FILES`, 6 lines.
   - **Sources:** Chapter 5, Concurrency Problems, Execution Contexts,
     Isolation and Immutability; *F16*.

2. **optimistic-and-pessimistic-control** — Optimistic and Pessimistic Control — *Chapter 5 · Concurrency* — 18 min
   - **Read:** Chapter 5, Optimistic and Pessimistic Concurrency Control (PDF
     pp. 76–78): pessimistic locking prevents a conflict by letting one
     session edit at a time; optimistic locking lets both edit and detects
     the conflict when the second commits; choosing between them by how often
     conflicts happen and what one costs; preventing inconsistent reads (read
     locks, version markers, temporal reads); deadlocks, and the avoidance
     techniques Fowler and Rice prefer to detection (the chapter's "we",
     PDF p. 78; corrected at authoring from "Fowler").
   - **Quote:** PDF p. 76, 24 words — “A good way of thinking about this is that
     an optimistic lock is about conflict detection while a pessimistic lock is
     about conflict prevention.”
   - **Do:** replay one timeline under no control, optimistic and pessimistic
     control, and count what each commits, refuses and loses.
   - **Standard:** given a timeline of reads, edits and commits by two
     sessions, state under each scheme who commits, who fails, when, and how
     many minutes of work the failure discards.
   - **Lab:** eakit `lock/timeline`. One timeline (*F16*'s situation,
     minutes illustrative): `0, martin, read, design; 1, david, read, design;
     5, david, edit, design; 6, martin, edit, design; 8, david, commit, -;
     10, martin, commit, -`. Presets `no-control` (scheme none →
     `olCommitted` "2: david, martin", `olLostUpdates` 1, `olRedo` 0),
     `optimistic` (→ "1: david", `olConflicts` "1: martin", `olRedo` 10) and
     `pessimistic` (→ "1: martin", `olRefused` "1: david", `olRedo` 0,
     `olPeakLocks` 1: Martin takes the lock when he loads the design at
     minute 0, so David is refused at minute 1, before he has done any
     work). Pins `olCommitted`, `olLostUpdates`, `olRedo`. The panel says a
     refused or conflicted session's later events are skipped, and that the
     lock is taken when the record is loaded for editing (§D.1).
   - **Misconception:** "Pessimistic locking is safer, so it is better." It
     turns a conflict away before any work is done, and it also keeps the
     second session out when the two would never have collided; Fowler's
     choice turns on how often conflicts happen and what one costs.
   - **Also:** "Optimistic locking prevents lost updates." It detects them; the
     second session's work is still lost, and it must redo it.
   - **Worked:** with no control both commit and David's change is
     overwritten; optimistically Martin finds out at minute 10, ten minutes
     after he started; pessimistically David is turned away at minute 1 and
     loses nothing, but cannot work on the design until Martin commits.
   - **Exercise:** `0, ann, read, plan; 2, bo, read, plan; 3, ann, edit, plan;
     4, bo, edit, plan; 9, bo, commit, -; 12, ann, commit, -`, optimistic.
     **Answer:** bo commits; ann's commit conflicts, 12 minutes of work redone.
     Pessimistic: ann takes the lock when she loads the plan at minute 0, bo
     is refused at minute 2 and redoes nothing.
   - **Own:** one record in a system you know that two people edit; write
     which scheme it uses (if any) and what the second editor sees.
   - **Snippet:** `TWO_CONTROLS`, 19 lines.
   - **Sources:** Chapter 5, Optimistic and Pessimistic Concurrency Control;
     *F16*.

3. **transactions-and-isolation** — Transactions and Isolation — *Chapter 5 · Concurrency* — 18 min
   - **Read:** Chapter 5, Transactions (PDF pp. 79–83): ACID; transactional
     resources; long, request and late transactions; lock escalation;
     reducing isolation for liveness, with the four isolation levels and the
     read errors each allows (Table 5.1, p. 81, reproduced nowhere: the lesson
     states the levels in its own sentences); business and system
     transactions. Patterns for Offline Concurrency Control (pp. 83–84), the
     map of Chapter 16. Application Server Concurrency (pp. 84–86):
     process-per-session, process-per-request and thread-per-request, and
     Fowler's and Rice's policy of avoiding explicit synchronisation
     (*F17*; the chapter's "our policy", corrected at authoring from
     "Fowler's").
   - **Quote:** PDF p. 81, 13 words — “To be sure of correctness you should
     always use the serializable isolation level.”
   - **Do:** name the weakest isolation level that prevents a stated
     inconsistent read.
   - **Standard:** given reads on both sides of a commit and whether the stale
     item was updated or had rows inserted, name the read error and the
     weakest level that prevents it.
   - **Lab:** eakit `lock/reads` with the `olLevel` tile. Presets
     `quarter-totals` (`january, 400, 400, before, update; february, 300,
     350, before, update; march, 0, 120, after, insert` → `olSeen` 820,
     `olConsistent` "no: 820 is neither 700 nor 870", `olLevel` "read
     committed allows it (an unrepeatable read); repeatable read prevents
     it"), `only-a-new-row` (`january, 400, 400, before, update; march, 0,
     120, after, insert` → 520, "yes: the state after the commit", "none
     needed: no read straddles the commit") and 6.1's `martin-and-david`
     (`olLevel` "repeatable read allows it (a phantom); serializable prevents
     it"). Pins `olConsistent`, `olLevel`. The panel states the rule (§D.1):
     the stale item decides, an update being an unrepeatable read and an
     insert a phantom.
   - **Misconception:** "Serializable prevents every read error, so use it
     always." Fowler's quotation is followed at once by the cost:
     serializable damages a system's liveness so much that you often have to
     reduce it to get throughput, and this lesson is about knowing which
     errors the weaker level lets through.
   - **Also:** "Isolation levels are about writes." They are about what a
     transaction can read of others' work.
   - **Worked:** `quarter-totals`: February was read before its update and
     March after its insert; February's stale value is an unrepeatable read,
     which repeatable read would have blocked.
   - **Exercise:** `north, 12, 12, before, update; south, 8, 11, before, insert;
     east, 5, 7, after, update`. **Answer:** seen 27 against 25 and 30; south
     is the stale item and its change an insert, so a phantom, which only
     serializable prevents.
   - **Own:** the isolation level your database runs at by default; look it
     up, and write which of the three read errors it allows.
   - **Snippet:** `COUNT_SERIALIZABLE`, 8 lines.
   - **Sources:** Chapter 5, Transactions, Patterns for Offline Concurrency
     Control, Application Server Concurrency; *F17*.

4. **optimistic-offline-lock** — Optimistic Offline Lock — *Chapter 16 · Offline Concurrency Patterns* — 18 min
   - **Read:** Chapter 16, Optimistic Offline Lock, by David Rice (PDF pp.
     374–381; examples pointed to): a version number in each row, checked in the update's
     `WHERE` and incremented by it, so that a row count of zero means another
     session committed first; the business transaction that fails late and
     must be redone, which is why it suits low conflict; checking the versions
     of what was only read, to detect an inconsistent read (the book's
     billing-and-address example); merging as an alternative to failing.
   - **Quote:** PDF p. 377, 17 words — “Optimistic concurrency management is
     appropriate when the chance of conflict between any two business
     transactions is low.” The words are David Rice's, in his pattern.
   - **Do:** replay a timeline under optimistic locking, with and without
     checking reads, and count the conflicts and the work lost.
   - **Standard:** given a timeline, state which commits fail their version
     check, the work each discards, and what checking reads changes.
   - **Lab:** eakit `lock/timeline`, scheme optimistic. Presets `two-clerks`
     (`0, kim, read, invoice; 1, lee, read, invoice; 2, lee, edit, invoice; 3,
     lee, commit, -; 4, kim, edit, invoice; 20, kim, commit, -` →
     `olCommitted` "1: lee", `olConflicts` "1: kim", `olRedo` 20),
     `inconsistent-read` (`0, kim, read, rate; 0, kim, edit, invoice; 1, lee,
     edit, rate; 2, lee, commit, -; 6, kim, commit, -`, checkReads no → "2:
     lee, kim", "0: none", 0) and `check-the-read` (checkReads yes → "1: lee",
     "1: kim", 6). Pins `olCommitted`, `olConflicts`, `olRedo`.
   - **Misconception:** "A version check catches every conflict." It catches
     conflicts on what the session wrote; on the lesson's illustration Kim's
     invoice is computed from a rate Lee changed, and the check passes unless
     the read is checked too.
   - **Also:** "Optimistic locking costs nothing." It costs the work of
     every failed session; on `two-clerks` Kim loses 20 minutes.
   - **Worked:** `two-clerks`: Kim read version 0, Lee committed version 1 at
     minute 3, and Kim's update at minute 20 matches no row.
   - **Exercise:** `0, ana, read, policy; 1, ben, read, policy; 2, ana, edit,
     policy; 5, ana, commit, -; 6, ben, edit, policy; 30, ben, commit, -; 31,
     cy, read, policy; 32, cy, edit, policy; 40, cy, commit, -`. **Answer:**
     ana and cy commit; ben conflicts at minute 30 and redoes 29 minutes.
   - **Own:** one table in a system you know that two users update; check
     whether it has a version column, and what the second save does.
   - **Snippet:** `OPTIMISTIC_SAVE`, 11 lines: the version check in the
     `WHERE`, and a `false` the caller must act on.
   - **Sources:** Chapter 16, Optimistic Offline Lock (David Rice).

5. **pessimistic-and-coarse-grained-locks** — Pessimistic and Coarse-Grained Locks — *Chapter 16 · Offline Concurrency Patterns* — 18 min
   - **Read:** Chapter 16, Pessimistic Offline Lock, by David Rice (PDF pp.
     382–390): acquire the lock before loading the data, so the session is
     sure to have the latest version; exclusive write, exclusive read and
     read/write locks; a lock manager and lock table; no waiting, because a
     business transaction can take twenty minutes (*F18*), so a refused lock
     aborts the transaction, early; timeouts for abandoned sessions.
     Coarse-Grained Lock, by Rice and Matt Foemmel (pp. 391–399): one lock
     for a group of objects (an aggregate), through a shared version or a
     lock on the root. Implicit Lock, by Rice (pp. 400–403): the framework or
     a Layer Supertype acquires the locks, so that no developer can forget
     one.
   - **Quote:** PDF p. 382, 9 words — “Pessimistic Offline Lock prevents
     conflicts by avoiding them altogether.”
     The words are David Rice's, in his pattern.
   - **Do:** replay edits of two lines of one order with a lock per line and
     with one lock for the order.
   - **Standard:** given a timeline and a grouping of records, state who is
     refused, the peak number of locks held, and what the grouping changes.
   - **Lab:** eakit `lock/timeline`, scheme pessimistic. Presets `line-locks`
     (`0, kim, edit, line1; 1, lee, edit, line2; 4, kim, commit, -; 5, lee,
     commit, -` → `olCommitted` "2: kim, lee", `olRefused` "0: none",
     `olPeakLocks` 2), `order-lock` (groups `line1=order9; line2=order9` →
     "1: kim", "1: lee", 1) and `optimistic-groups` (the same groups,
     optimistic → "1: kim", `olConflicts` "1: lee", `olRedo` 4). Pins
     `olRefused`, `olPeakLocks`. These timelines have no reads, so each lock
     is taken at the edit, which is also the load. The body says the coarse
     lock refused Lee
     although the two lines are different rows, which is its cost, and that
     it is the point when the order's total depends on both.
   - **Misconception:** "A finer lock is always better." It allows more
     concurrency and protects less: two sessions can each change one line of
     an order whose rule spans both.
   - **Also:** "Pessimistic locks should wait for each other." Rice's lock
     manager refuses at once and the business transaction aborts, because
     another may hold the lock for twenty minutes.
   - **Worked:** `order-lock`: both lines map to `order9`, so Lee's edit at
     minute 1 is refused while Kim holds it.
   - **Exercise:** `0, ann, edit, room1; 1, bo, edit, room2; 2, cy, edit,
     room3; 3, ann, commit, -; 7, bo, commit, -; 8, cy, commit, -`,
     pessimistic, groups `room1=floor1; room2=floor1; room3=floor2`.
     **Answer:** ann and cy commit, bo is refused at minute 1 (0 minutes of
     work lost, `olRedo` 0); peak 2 locks.
   - **Own:** one aggregate in a system you know (an order and its lines, a
     document and its sections); write what is locked when one part is
     edited.
   - **Snippet:** `GROUP_LOCK`, 10 lines.
   - **Sources:** Chapter 16, Pessimistic Offline Lock (David Rice),
     Coarse-Grained Lock (Rice and Matt Foemmel), Implicit Lock (Rice);
     *F18*.

6. **the-value-of-statelessness** — The Value of Statelessness — *Chapter 6 · Session State* — 15 min
   - **Read:** Chapter 6, The Value of Statelessness (PDF p. 88): a stateless
     server object holds nothing between requests, so it can be pooled; the
     book's illustration (*F19*): a hundred users, each idle for most of the
     time between requests, need a hundred stateful objects but only about
     ten stateless ones, because 90 percent of the stateful objects are idle;
     why some state is unavoidable (a shopping cart), and that a stateless
     server does not mean a stateless session.
   - **Quote:** PDF p. 88, 20 words — “The shift from stateless to stateful is
     much more than three or four letters at the end of the word.”
   - **Do:** compute how many server objects a load needs, stateful and
     stateless.
   - **Standard:** given users, a service time and a time between requests,
     compute the stateful objects, the stateless objects busy on average and
     the stateful objects' idle share.
   - **Lab:** eakit `session/objects`. Presets `hundred-users` (*F19*'s
     figures in ms: users 100, service 1,000, think 10,000 → `snStateful`
     100, `snStateless` 10, `snIdle` "9/10 = 90%", `snPerObject` 10) and
     `busier` (think 2,000 → 100, 50, "1/2 = 50%", 2). Pins `snStateless`,
     `snIdle`. The panel says the stateless figure is an average, and that a
     pool sized to it is too small at peaks (§D.1); and that Fowler calls the
     illustration a completely unrealistic thought experiment, with
     perfectly balanced requests.
   - **Misconception:** "Stateless means the application keeps no state." It
     means the server object keeps none between requests; the state goes to
     the client or the database (6.7).
   - **Also:** "Stateful is always worse." The cart has to live somewhere;
     the question is where.
   - **Worked:** 100 × 1,000/10,000 = 10 objects busy on average; 1 −
     1,000/10,000 = 9/10 idle.
   - **Exercise:** users 250, service 400 ms, think 20 s. **Answer:** 250
     stateful against 5 stateless; 49/50 = 98% idle; each stateless object
     serves 50 users.
   - **Own:** one service in a system you know; write what it keeps in memory
     between a user's requests.
   - **Snippet:** `STATELESS_HANDLER`, 16 lines.
   - **Sources:** Chapter 6, The Value of Statelessness; *F19*.

7. **session-state** — Session State — *Chapter 17 · Session State Patterns* — 18 min
   - **Read:** Chapter 6, Session State (PDF pp. 89–91): session state against
     record data, and committing it to become record data; the three places it
     can live; the book's illustration of a large session (*F20*), about a
     megabyte. Chapter 17, Client Session State (pp. 405–406): URL, hidden
     fields or cookies, sent with every request, so it must be small, and it
     must be protected; Server Session State (pp. 407–409): in memory or
     serialized, kept by the server, with the clustering and failover
     problem, and the anecdote of a session table rotated in twelve
     segments (*F21*); Database Session State (pp. 410–411): pending rows in
     the database, kept apart from committed data.
   - **Quote:** PDF p. 89, 10 words — “Session state needs to be committed to
     become record data.”
   - **Do:** compute the bytes each place for session state moves and holds.
   - **Standard:** given users, a session's size, requests in a session and an
     id's size, compute the bytes on the wire per request and per session for
     client state, the id alone for server state, the memory a server holds,
     and the bytes a database session moves per request.
   - **Lab:** eakit `session/state`. Presets `a-megabyte` (*F20*'s size: users
     100, state 1,000,000 bytes, 20 requests, id 32 → `snWire` 2,000,000,
     `snSessionWire` 40,000,000, `snIdOnly` 32, `snMemory` 100,000,000,
     `snDatabase` 2,000,000) and `a-small-cart` (state 2,000 → 4,000, 80,000,
     32, 200,000, 4,000). Pins `snWire`, `snMemory`. The panel states the
     model (§D.1): client state goes both ways on every request; a database
     session reads and writes it once a request.
   - **Misconception:** "Client session state is free because the server
     stores nothing." It sends everything, both ways, every request: on the
     lesson's first preset forty million bytes for one session.
   - **Also:** "Server session state is the simple choice." It is until there
     are two servers; then the session must follow the user or be shared,
     which is Fowler's clustering problem.
   - **Worked:** 2 × 1,000,000 bytes a request, × 20 requests = 40,000,000;
     the server's alternative holds 100 × 1,000,000 = 100,000,000 in memory.
   - **Exercise:** users 5,000, state 40,000 bytes, 12 requests, id 32.
     **Answer:** client 80,000 bytes a request and 960,000 a session; server
     memory 200,000,000; database 80,000 a request.
   - **Own:** one session in a system you know; find where its state is kept
     and estimate its size.
   - **Snippet:** `SERVER_SESSION`, 14 lines.
   - **Sources:** Chapter 6, Session State; Chapter 17, Client, Server and
     Database Session State; *F20*, *F21*.

### Course 7 — Distribution and Putting It Together (`enterprise-patterns-distribution`, 5)

Chapters 7, 8 and 15, with the two base patterns that let a system be wired
from outside. When to cross a process boundary, how to do it when you must,
and Fowler's own summary of the book. Its `how_to` says four of its five labs
count calls across a boundary from a latency the lesson states, and the last
(7.5, cckit `deps/ripple`) counts what a change reaches. Its `not_covered`
says the web-services and messaging technologies of 2002 are named as the
book names them, not taught. The course's §F.4 aside is in Putting It All
Together.

1. **distribution-strategies** — Distribution Strategies — *Chapter 7 · Distribution Strategies* — 18 min
   - **Read:** Chapter 7 (PDF pp. 92–99): The Allure of Distributed Objects
     (p. 93), putting each kind of object on its own node, and why it fails;
     Remote and Local Interfaces (p. 95): a remote call costs orders of
     magnitude more than a local one, so a remote interface must be
     coarse-grained and a local one fine-grained, and the two cannot be the
     same; the First Law; clustering instead (copies of the whole application
     on many nodes); Where You Have to Distribute (p. 97): client and server,
     application server and database, web server and application server,
     vendor packages; Working with the Distribution Boundary (p. 98), which
     points to Remote Facade and Data Transfer Object; Interfaces for
     Distribution (p. 99).
   - **Quote:** PDF p. 95, 15 words — “Hence, we get to my First Law of
     Distributed Object Design: Don't distribute your objects!”
   - **Do:** compute the time a design's calls take with its classes on one
     node and spread across several.
   - **Standard:** given calls between classes and which node each class is
     on, compute the remote calls, the total time and the ratio to one node.
   - **Lab:** eakit `remote/boundary`. Presets `by-class` (`screen, order, 20;
     order, customer, 10; order, product, 30; order, pricing, 15`, each of
     order, customer, product and pricing on its own node, remote 1,000 µs,
     local 1 µs, illustrative → `rrCalls` 75, `rrRemote` 75, `rrTime` 75,000,
     `rrShare` "1 = 100%", `rrOneNode` 75, `rrRatio` "1,000×") and
     `one-process` (no nodes → 75, 0, 75, "0 = 0%", 75, "1×"). Pins `rrRemote`,
     `rrTime`, `rrRatio`. The panel says the times are in microseconds and
     the ratio of remote to local is the lesson's, not a measurement.
   - **Misconception:** "Distributing by class spreads the load." It
     multiplies the calls' cost by the remote ratio; Fowler's alternative,
     clustering, spreads load with every call still local.
   - **Also:** "A remote call is just a slower local call." It also needs a
     different interface, which is why Fowler says a class cannot be both.
   - **Worked:** `by-class`: every one of 75 calls crosses a node, 75 × 1,000
     µs = 75 ms against 75 µs.
   - **Exercise:** `web, cart, 12; cart, stock, 8; cart, tax, 8; tax, rates,
     16`, with `web` on a front node and `tax` and `rates` on a back node,
     remote 800 µs, local 2. **Answer:** 44 calls, 20 remote, 16,048 µs, the
     remote share 1,000/1,003 ≈ 99.7%, against 88 µs on one node (2,006/11 ≈
     182.4×); `tax, rates` stays local.
   - **Own:** one service boundary in a system you know; count the calls that
     cross it for one user action.
   - **Snippet:** `REMOTE_CUSTOMER`, 6 lines.
   - **Sources:** Chapter 7.

2. **remote-facade** — Remote Facade — *Chapter 15 · Distribution Patterns* — 15 min
   - **Read:** Chapter 15, Remote Facade (PDF pp. 352–362; examples pointed
     to): a coarse-grained facade over fine-grained objects, with no domain
     logic of its own, so the fine-grained model stays usable locally; one
     facade method doing the work of several calls; granularity, where
     Fowler prefers few facades with many methods each (perhaps one for a
     moderate application) to the one-per-use-case some prefer (PDF p. 353),
     each designed for one client's usage; stateful and stateless facades;
     security and transactions applied at the facade.
   - **Quote:** PDF p. 355, 13 words — “Use Remote Facade whenever you need
     remote access to a fine-grained object model.”
   - **Do:** compute the time fine-grained calls take across a network
     against the facade's coarse calls.
   - **Standard:** given facade methods and the fine-grained calls each
     replaces, a latency and a work time, compute both times and the
     speed-up.
   - **Lab:** eakit `remote/calls`. Presets `move-house` (`moveHouse, 5;
     showCustomer, 6`, latency 20 ms, work 0.5 ms → `rrFineTrips` 11,
     `rrCoarseTrips` 2, `rrFineMs` "451/2 = 225.50", `rrCoarseMs` "91/2 =
     45.50", `rrLatencyShare` "40/41 ≈ 97.6%", `rrSpeedup` "451/91 ≈ 5.0×")
     and `on-a-fast-network` (latency 1 → "33/2 = 16.50", "15/2 = 7.50", "2/3
     ≈ 66.7%", "11/5 ≈ 2.2×"). Pins `rrFineMs`, `rrCoarseMs`, `rrSpeedup`.
   - **Misconception:** "A Remote Facade is where the business logic goes."
     Fowler keeps it thin: it translates coarse calls to fine-grained ones;
     the logic stays in the objects behind it.
   - **Also:** "Make the domain objects coarse-grained so they can be called
     remotely." That gives up the fine-grained model locally, which is what
     the facade exists to keep.
   - **Worked:** fine 11 × 20.5 = 225.5 ms; coarse 2 × 20 + 11 × 0.5 = 45.5 ms.
   - **Exercise:** `bookTrip, 8; cancelTrip, 3; showTrip, 9`, latency 15 ms,
     work 1 ms. **Answer:** 20 fine calls, 320 ms, against 3 coarse, 65 ms,
     64/13 ≈ 4.9× faster; latency 15/16 ≈ 93.8% of the fine time.
   - **Own:** one screen in a system you know that calls a remote API; count
     its calls and say which could be one.
   - **Snippet:** `CUSTOMER_FACADE`, 16 lines.
   - **Sources:** Chapter 15, Remote Facade.

3. **data-transfer-object** — Data Transfer Object — *Chapter 15 · Distribution Patterns* — 15 min
   - **Read:** Chapter 15, Data Transfer Object (PDF pp. 363–372; examples
     pointed to): an object that carries data across a process boundary in
     one call, serializable, usually shaped for one screen and assembled from
     the domain by an assembler; the advice to err on the side of sending too
     much; serialization forms, binary and XML (the book notes XML's size,
     and Chapter 6 its megabyte, *F20*); not to be confused with the J2EE
     use of "value object" (read in 2.5).
   - **Quote:** PDF p. 363, 26 words — “Due to the latency costs of remote calls,
     its better to err on the side of sending too much data than have to make
     multiple calls.”
   - **Do:** compute the time of one getter call per field against one DTO
     carrying every field.
   - **Standard:** given fields with sizes and whether the screen needs them,
     a latency, a bandwidth and an encoding factor, compute both times, the
     unneeded bytes the DTO sends, and how many bytes one saved round trip
     would have carried.
   - **Lab:** eakit `remote/payload`. Presets `order-screen` (`id, 8, yes;
     customerName, 40, yes; status, 10, yes; totalCents, 8, yes; lines, 2000,
     yes; notes, 4000, no`, latency 20 ms, 1,000 bytes a ms, factor 1 →
     `rrGetterCalls` 5, `rrGetterMs` "51,033/500 ≈ 102.07", `rrDtoBytes`
     6,066, `rrDtoMs` "13,033/500 ≈ 26.07", `rrExtraBytes` 4,000, `rrSpare`
     80,000) and `as-xml` (factor 3 → 5, "53,099/500 ≈ 106.20", 18,198,
     "19,099/500 ≈ 38.20", 12,000, 80,000). Pins `rrGetterMs`, `rrDtoMs`,
     `rrExtraBytes`. The panel says the factor is the lesson's stand-in for an
     encoding's size and states the model (§D.1).
   - **Misconception:** "Fetch each value only when the screen asks for it."
     On the lesson's illustration that is five calls and 51,033/500 ≈ 102.07
     ms, against 13,033/500 ≈ 26.07 ms for one DTO that also carries 4,000
     bytes the screen never shows; the quotation is the reason. The
     exercise shows the limit of the advice: a DTO shaped for the screen,
     sent in one call, is faster still.
   - **Also:** "A DTO is a domain object with getters." It has no behaviour
     and is shaped by the call, not the domain; an assembler builds it.
   - **Worked:** five getters cost 5 × 20 ms plus 2,066 bytes; one DTO costs
     20 ms plus 6,066 bytes, at 1,000 a ms.
   - **Exercise:** `name, 30, yes; email, 40, yes; photo, 60000, no; history,
     9000, no`, latency 10 ms, 2,000 bytes a ms, factor 1. **Answer:** two
     getters 4,007/200 ≈ 20.04 ms; one DTO of 69,070 bytes 8,907/200 ≈ 44.54
     ms: here the DTO is slower, because it carries 69,000 unneeded bytes,
     more than the 20,000 a saved round trip would have carried. A DTO shaped
     for the screen (no photo, no history) takes 2,007/200 ≈ 10.04 ms.
   - **Own:** one API response in a system you know; weigh it, and count the
     fields its client uses.
   - **Snippet:** `ORDER_DTO`, 8 lines.
   - **Sources:** Chapter 15, Data Transfer Object; Chapter 6, Session State;
     *F20*.

4. **putting-it-all-together** — Putting It All Together — *Chapter 8 · Putting It All Together* — 18 min
   - **Read:** Chapter 8 (PDF pp. 100–106): Starting with the Domain Layer
     (p. 101), the three domain patterns again, now with the database's
     difficulty as a second force; Down to the Data Source Layer (pp.
     102–103), the data-source patterns for each, with the threshold of a
     couple of dozen classes for a simple Domain Model (*F22*); The
     Presentation Layer (p. 103); Some Technology-Specific Advice (pp.
     104–106), Java and J2EE, .NET, stored procedures and web services, which
     Fowler dates himself (*F23*). Then Other Layering Schemes (pp.
     107–109): Fowler compares his three layers with the Brown, Core J2EE,
     Microsoft DNA (Kirtland), Marinescu and Nilsson schemes, mapping their
     mediating layers onto patterns the reader has now met (Application
     Controller, Data Mapper, Service Layer, Data Transfer Object).
   - **Quote:** PDF p. 100, 17 words — “Use this advice to prod your thinking,
     but don't use it as a replacement for your thinking.”
   - **Do:** compute what one request's calls cost under three deployments of
     the same layers.
   - **Standard:** given the calls between layers for one request and which
     node each layer runs on, compute the remote calls and the time for each
     deployment, and say which boundary Fowler would keep.
   - **Lab:** eakit `remote/boundary`. Presets `web-and-database` (`browser,
     page, 1; page, service, 2; service, domain, 40; domain, mapper, 25;
     mapper, database, 6`, nodes `browser=client; database=db`, remote 2,000
     µs, local 1 → `rrRemote` 7, `rrTime` 14,067, `rrRatio` "14,067/74 ≈
     190.1×"), `service-split-off` (the service, domain and mappers on an
     `app` node → 9, 18,065, "18,065/74 ≈ 244.1×") and `domain-split-off`
     (the page and service apart from the domain → 47, 94,027, "94,027/74 ≈
     1,270.6×"). Pins `rrRemote`, `rrTime`. The body reads the three as
     Chapter 7's advice: the browser and the database boundaries are the ones
     you cannot avoid; a boundary above the Service Layer (between the page
     and the service) adds 2 calls, and one under it (between the service
     and the domain) adds 40. The panel says one `remoteUs` prices every
     remote hop alike, the browser's and the database's.
   - **Misconception:** "The chapter is a decision procedure." The quotation
     says otherwise, and so does Fowler's description of it as advice that
     depends on circumstance.
   - **Also:** "The technology advice is the chapter's point." Fowler dates it
     himself; the patterns are the point.
   - **Worked:** `web-and-database`: 1 + 6 remote calls, 7 × 2,000 + 67 × 1 =
     14,067 µs.
   - **Exercise:** `app, facade, 3; facade, domain, 30; domain, mapper, 20;
     mapper, db, 4`, nodes `app=phone` (the database is left on the server's
     node, so that the only slow hop is the phone's), remote 50,000 µs, local
     1. **Answer:** 57 calls, 3 remote, 150,054 µs, almost all of it the
     three phone calls (`rrRatio` 50,018/19 ≈ 2,632.5×); one Remote Facade
     method for the screen would make it one call, about 50,054 µs.
   - **Own:** the layers of one system you know, with the node each runs on;
     count the calls that cross a node for one request.
   - **Snippet:** `PLACE_ORDER_STACK`, 11 lines.
   - **Sources:** Chapter 8, Starting with the Domain Layer, Down to the Data
     Source Layer, The Presentation Layer, Some Technology-Specific Advice,
     Other Layering Schemes; *F22*, *F23*.
   - **§F.4 aside** (this course's one): what has happened to distribution
     since 2002 (services and microservices) is argued largely in the
     vocabulary of Chapter 7, and some of it against the First Law. Stated in
     the `note`, at strength, unsettled.

5. **plugin-and-service-stub** — Plugin and Service Stub — *Chapter 18 · Base Patterns* — 15 min
   - **Read:** Chapter 18, Plugin, by David Rice and Matt Foemmel (PDF pp.
     441–444): linking classes during configuration rather than
     compilation, so the implementation of a Separated Interface is chosen
     per environment; Service Stub, by Rice (pp. 445–448): a stand-in for a
     slow, unreliable or not-yet-available service during development and
     testing, as simple as it can be; both read back to Separated Interface
     (1.5).
   - **Quote:** PDF p. 446, 18 words — “Use Service Stub whenever you find that
     dependence on a particular service is hindering your development and
     testing.” The words are David Rice's, in his pattern.
   - **Do:** count what a network change reaches, and whether the tests
     depend on the network, with and without a plugin and a stub.
   - **Standard:** given dependencies including tests, list what a change to
     the network library reaches with a direct dependency and with a
     Separated Interface, a stub and a plugin.
   - **Lab:** cckit `deps/ripple`, on a signup that checks a postcode with
     an address service. Presets `real-service` (`signup, postoffice;
     postoffice, network; signuptest, signup`, changed `network` →
     `dgDirect` "1: postoffice", `dgAffected` "3: postoffice, signup,
     signuptest") and `plugin-and-stub` (`signup, addresscheck;
     postofficecheck, addresscheck; postofficecheck, network;
     addresscheckstub, addresscheck; signuptest, signup; signuptest,
     addresscheckstub; main, postofficecheck` → "1: postofficecheck", "2:
     main, postofficecheck"). Pins both tiles.
   - **Misconception:** "A stub tests the service." It tests the code that
     uses the service, without it; the service needs its own tests.
   - **Also:** "A plugin needs a framework." Rice and Foemmel's Plugin needs
     only one place, read at configuration time, that chooses the
     implementation for the environment; the snippet does it with one
     `switch`.
   - **Worked:** `plugin-and-stub`: the test depends on `signup` and
     `addresscheckstub`, neither of which reaches the network.
   - **Exercise:** `invoice, ratesfeed; ratesfeed, http; invoicetest,
     invoice`, an invoice priced from an exchange-rate feed, changed `http`.
     **Answer:** 1 direct (`ratesfeed`) and 3 affected (`invoice,
     invoicetest, ratesfeed`); with a `rates` interface, `httprates` and
     `ratesstub` implementing it and `main` wiring the real one, `http`
     reaches "2: httprates, main" and the test is no longer reached.
   - **Own:** one test in a system you know that calls a real external
     service; write the interface that would let it use a stub.
   - **Snippet:** `ADDRESS_STUB`, 20 lines.
   - **Sources:** Chapter 18, Plugin (David Rice and Matt Foemmel), Service
     Stub (Rice), Separated Interface.

---

## §D The lab kit: `eakit`

### D.0 Conventions

Everything in Code Complete's §D.0 and cckit as built
(`docs/code-complete/kit-report.md`, "Conventions as implemented") holds
unless this section says otherwise.

**Entry point and cfg.**

- One function `eakit_lab(cfg)`, registered under the key `"eakit"` in
  `scripts/mathpath/labs/__init__.py`. It dispatches on `cfg["mode"]` and
  `cfg["view"]` (the view defaults to the mode's first). An unknown mode or
  view raises, listing the valid ones.
- Keys common to every view: `mode`, `view`, `presets` (required, non-empty),
  `preset` (the one shown first; default the first), `title`, `panel_title`,
  `panel_intro`.
- A preset is `{"id", "label", <inputs>, "expect"}`. A preset key that is not
  an input of its view raises at build time, naming the view's inputs.
- **A cfg key named like one of the view's inputs** supplies that input to
  every preset that does not set it, as in cckit. A lesson that compares one
  timeline under three schemes states the timeline once, as cfg `events`.
- **Lesson-level keys**, from the cfg and never from a preset:
  - `unit` (`perf/scale`; one lower-case word, default `server`), used in
    `pzEfficiency` and the tile labels;
  - `fine_label` and `coarse_label` (`remote/calls`; plain text, defaults
    "fine-grained calls" and "coarse-grained calls"), used in tile labels
    only, never in tile values. Lesson 3.6 passes "statements" and
    "batches";
  - `source` (every family 2 view, optional). When given, the panel intro
    ends "Figures: <source>." Lessons whose presets carry book figures set
    it ("the book's illustration in the Introduction, Thinking About
    Performance; the rest illustrative").
- Any other cfg key raises, naming the keys the view takes.
- `eakit` joins `KITS_WITH_EXPECTATIONS` at wiring, last (§H.3).

**Files.**

- `scripts/mathpath/labs/eakit_core.py`: shared JS (`EA_CORE_JS`) for
  printing, records, names, the preset menu and the banner, with its Python
  mirror for build-time parsing.
- `eakit.py`: the `perf`, `remote`, `load` and `uow` modes.
- `eakit_b.py`: the `inherit`, `lock`, `session` and `money` modes.

Like cckit, each mode's JS is one `VIEW_JS` block per view, and a page ships
only its own.

**Page weight.** A page ships `RATIONAL_JS`, `EA_CORE_JS` and the active
view's block only. Budget: at most 40 KB gzipped per lesson page, measured
with the snippet in `AGENTS.md` before the kit is called done, against the
67 KB ceiling. A cckit lesson's weight is cckit's, unchanged.

**Prefixes.** Mode prefixes: `pz` perf, `rr` remote, `ld` load, `uw` uow, `ih`
inherit, `ol` lock, `sn` session, `mn` money. Shared helpers are prefixed `ea`.
Each prefix was checked against every `*.py` in `scripts/mathpath/labs/` and
none of them is in use (the taken ones nearby are `eu` dekit, `el` replica,
`ey` readkit, `lg`, `ln`, `ob`, `pt`, `gr`, `ss`, `st`). Before the kit is
called done, grep again for every JS function name and element id it defines.

**Ids.** An input's id is `<prefix>In<Field>`, with the field's name in
camel case: `pzInPoints`, `rrInLatencyMs`, `olInCheckReads`. Each page ships
a preset menu `<prefix>Preset`, a banner `<prefix>Status` and a table
`<prefix>Table`. A tile's id is the name §D.1 gives it, and a view's tiles are
exactly those.

**Inputs.**

- Record inputs are text boxes: records `a, 1, 2; b, 3, 4`, fields separated
  by commas, records by semicolons. A record with the wrong number of fields
  is refused with its position ("record 3 has 2 fields; this list needs 3").
- Names are letters, digits, `.`, `_` and `-`, as in cckit; a name may not be
  `-`, which marks "none" (a root, a commit's record).
- Words are typed and checked against their list (`yes`/`no`; `load`, `new`,
  `change`, `delete`; `read`, `edit`, `commit`; `before`/`after`;
  `insert`/`update`). Anything else is refused, naming the list.
- `scheme`, `checkReads` and `rule` are `<select>`s.
- Numbers are whole numbers or decimals (`0.1`), read exactly. A fraction, a
  sign other than a leading minus, or an exponent is refused. Each input
  states its range in §D.1, and a number outside it is refused, naming the
  field and the range.
- **Every text input survives** `''`, `banana`, `0`, `-1`, `1/0` and `A>B`
  with a red banner and every tile blanked to `—`. The exceptions are the
  optional inputs (`rrInNodes`, `olInGroups`, `uwInAs`): for these `''` is a
  legal empty value, which the view reads as "none" and states in its banner.
  Since `labcheck.js`'s sweep checks only that nothing throws, this needs no
  change to it.
- Limits: at most 60 records per input and 20 ratios. A whole-number field is
  at most 10,000,000. A view's projected search (`pzCrossover`, `pzNeed`)
  stops at 10,000 servers and says so.

**Number format.** Exactly Code Complete's §D.0: grouped thousands, U+2212
for a minus, `7/2 = 3.50` and `28/3 ≈ 9.33` (two places, rounded half away
from zero from the exact value), shares `9/10 = 90%` and `2/3 ≈ 66.7%`. Ratios
print `10×` when whole, else `125/37 ≈ 3.4×` (one place). A list is
comma-separated in the order each tile states, or `none`. A count with a
list prints `2: david, martin`. A per-system tile joins its entries with
`; ` in the order the systems first appear. A three-part `inherit` tile
prints `single, class, concrete`, in that order.

**Exact.** Every tile is a rational over BigInt (`RATIONAL_JS`), a count or a
list. No tile is computed in JavaScript floating point, and no tile is read
off a drawing.

**The figures are the lesson's.** No figure from the book is a constant of the
kit: response times, throughputs, latencies, row counts, session sizes and the
amount to allocate all arrive in a preset. The kit never states something only
the book can vouch for.

**Families.** Every panel intro begins with its family's sentence, even when
`panel_intro` overrides the rest:

- `load/instances`, `identity`, `graph` and `tree`, `uow/*`, `inherit/*`,
  `lock/*` and `remote/boundary`: "A count over the situation the lesson
  states."
- `perf/*`, `remote/calls`, `remote/payload`, `load/finds`, `session/*` and
  `money/*`: "The arithmetic of the figures the lesson states (marked with
  their source)."

**Zero denominators** print `—` with a one-sentence reason in the banner, as
in Code Complete. A *divisor* input (a latency in a ratio, a bandwidth, a time
between requests, a ratio total) must be positive, and zero or a negative is
refused with the field named.

### D.1 Modes (prefix, views, inputs, tiles)

Each view lists its inputs (field, type, range), its rules and its tiles in
order. Where a rule is a modelling choice, the panel says it in the words
given here, or near them.

#### perf (`pz`) — family 2

- `load`. Inputs `points` (records `system, users, ms`: name; whole 1–10⁷;
  number > 0; a system's user counts distinct) and `users` (whole 1–10⁷).
  Rules: each system's points are sorted by users. Its change per user is
  (last ms − first ms)/(last users − first users). Its ratio is last ms /
  first ms. Its response at `users` is interpolated in a straight line
  between the two measured points either side. Outside the measured loads
  the tile says so, and is not extrapolated.
  Tiles:
  - `pzPerUser`: "a 0 ms a user; b 180 ms a user". A system with one
    measurement prints "—".
  - `pzRatio`: "a 1×; b 10×".
  - `pzAt`: "a 500 ms; b 1,100 ms", or "b outside its measured loads".

  Banner: "Between two measurements the lab draws a straight line; that is
  the lab's assumption, not a measurement, and Fowler's advice is to measure
  at the load you care about."

- `scale`. Inputs `points` (records `system, servers, tps`: name; whole
  1–10,000; number ≥ 0; a system's server counts distinct), `need` (number
  > 0) and `at` (whole 1–10,000); cfg `unit`.

  Rules: a system's rate is (tps at its last measurement − tps at its first)
  / (the difference in servers). Its projected throughput at n servers is
  the measured value where n was measured, and otherwise the straight line
  through its first and last measurements: tps_last + rate·(n − n_last).

  Tiles:
  - `pzEfficiency`: tps at the first measurement divided by its servers,
    "swordfish 20 a server; camel 40 a server".
  - `pzMarginal`: the rate, "swordfish 15; camel 10", or "—" with one
    measurement.
  - `pzCrossover`: only with exactly two systems. It is the first n from 1 up
    at which the two projections are equal or have changed order: "5 servers
    (both 80)" or "4 servers (heron 66, stork 63)". It prints "none" when
    there is no such n up to 10,000, "—: each system needs two measurements",
    or, with other than two systems, "—: the crossover compares two systems".
  - `pzNeed`: the least n with projection ≥ `need`, "swordfish 3; camel 1".
    It prints "never at this rate" (rate ≤ 0 and not yet reached) or "not
    measured: one measurement gives no rate".
  - `pzAt`: the projection at `at`, "swordfish 80; camel 80".

  Banner: "Past the last measurement the lab carries on at the measured rate,
  which is what the lesson's figures say and nothing more."

#### remote (`rr`)

- `boundary` (family 1). Inputs `calls` (records `caller, callee, count`:
  name; name; whole 0–10⁷), `nodes` (optional, `class=node; class=node`; a
  class not listed runs on node `main`), `remoteUs` (number > 0) and
  `localUs` (number > 0). A call is remote when its caller and callee are on
  different nodes.
  Tiles:
  - `rrCalls`: every call.
  - `rrRemote`: the remote calls.
  - `rrTime`: remote·remoteUs + local·localUs, in µs.
  - `rrShare`: the remote calls' share of `rrTime`.
  - `rrOneNode`: the time with every class on one node, calls·localUs.
  - `rrRatio`: `rrTime`/`rrOneNode`.

  Banner: "The times are the lesson's, in microseconds: a remote call's cost
  against a local one is what the lesson states, not a measurement."

- `calls` (family 2). Inputs `ops` (records `operation, fine`: name; whole
  1–10⁷), `latencyMs` (number > 0) and `workMs` (number ≥ 0); cfg
  `fine_label`, `coarse_label`. Each record is one coarse-grained call that
  does the work of `fine` fine-grained ones. With n = Σ fine and m = the
  number of records:
  - `rrFineTrips` n;
  - `rrCoarseTrips` m;
  - `rrFineMs` n·(latency + work);
  - `rrCoarseMs` m·latency + n·work;
  - `rrLatencyShare` n·latency / `rrFineMs`;
  - `rrSpeedup` `rrFineMs`/`rrCoarseMs`.

  Banner: "The lab assumes the work is the same either way; what the coarse
  calls remove is the waits."

- `payload` (family 2). Inputs `fields` (records `field, bytes, needed`:
  name; whole 0–10⁷; yes/no), `latencyMs` (number > 0), `bytesPerMs` (number
  > 0) and `factor` (number > 0, the encoding's size against the raw bytes).
  The getter design makes one call per needed field; the DTO is one call
  carrying every field. With k needed fields:
  - `rrGetterCalls` k;
  - `rrGetterMs` k·latency + needed bytes·factor/bytesPerMs;
  - `rrDtoBytes` all bytes·factor;
  - `rrDtoMs` latency + `rrDtoBytes`/bytesPerMs;
  - `rrExtraBytes` the unneeded bytes·factor;
  - `rrSpare` (k − 1)·latency·bytesPerMs, the bytes the saved round trips
    could have carried (0 when k ≤ 1).

  Banner: "The model sends data at a steady rate after a fixed latency; real
  networks are lumpier."

#### load (`ld`)

- `instances` (family 1). Input `tables` (records `table, rows`: name; whole
  0–10⁷). Tiles:
  - `ldTables`;
  - `ldRows` (Σ rows);
  - `ldRowObjects` (one per row, as a Domain Model or Row Data Gateway holds
    them);
  - `ldTableObjects` (one per table, as Table Module holds them);
  - `ldLargest` (the table with the most rows and its rows, "line 6,000";
    the first such table on a tie).

  Banner: "Objects, not memory, and every row loaded, which neither pattern
  requires."
- `finds` (family 2). Inputs `wanted` (whole 1–10⁷), `broad` (whole ≥
  `wanted`, refused otherwise: "the broad query returns at least the rows you
  want"), `batch` (whole 1–10⁷), `latencyMs` (number > 0) and `rowMs` (number
  ≥ 0). Tiles:
  - `ldKeyedStatements` (wanted);
  - `ldKeyedMs` (wanted·(latency + rowMs));
  - `ldBroadRows` (broad);
  - `ldBroadMs` (latency + broad·rowMs);
  - `ldBatchStatements` (⌈wanted/batch⌉);
  - `ldBatchMs` (⌈wanted/batch⌉·latency + wanted·rowMs);
  - `ldUnneeded` (broad − wanted).
- `identity` (family 1). Input `finds` (records `class, id`: name; name), in
  the order they happen. Tiles:
  - `ldFinds`;
  - `ldDistinct` (distinct class and id pairs);
  - `ldDuplicates` (finds − distinct);
  - `ldShared` (each pair found more than once, in order of its first find,
    "customer 7 ×3, product 5 ×2", or `none`).
- `graph` (family 1). Inputs `parents` (records `parent, children, used`:
  name; whole 0–10⁷; yes/no) and `batch` (whole 1–10⁷). With N parents, t of
  them used, the used parents' children C_u and all children C:
  - `ldLazy`: 1 + t statements, N + C_u rows. One query for the parents, then
    one for each used parent's children.
  - `ldBatched`: 1 + ⌈t/batch⌉ statements, N + C_u rows. The used parents'
    children, `batch` parents at a time.
  - `ldTwoQueries`: 2 statements, N + C rows. The parents, then every
    child.
  - `ldJoin`: 1 statement, Σ max(children, 1) rows. A left outer join, so a
    parent with no children is still one row.

  Each tile prints "4 statements, 17 rows" (singular "1 statement", "1 row").
  The panel states the four rules.
- `tree` (family 1). Input `nodes` (records `node, parent`; `-` for the
  root; exactly one root, every parent a node, no cycle, all refused
  otherwise). The depth of the root is 1. Tiles:
  - `ldNodes`;
  - `ldDepth`;
  - `ldPerNode` (1 + nodes: one query for the root, then one for each node's
    children);
  - `ldPerLevel` (depth + 1: one query per level, the last finding the
    level below the leaves empty, as `ldPerNode` counts the leaves' empty
    queries);
  - `ldLob` (1: the whole tree in one column).

#### uow (`uw`) — family 1

- `commit`. Input `script` (records `op, object`: one of load, new, change,
  delete; a name). Refused, naming the record:
  - change or delete of an object neither loaded nor created;
  - load of an object created in the script;
  - new of an object already loaded or created;
  - anything after an object's delete.

  Immediate writes are one per new, change and delete. At commit:
  - an object created and deleted writes nothing;
  - created, one INSERT;
  - loaded and deleted, one DELETE;
  - loaded and changed (any number of times), one UPDATE;
  - loaded only, nothing ("clean").

  Tiles:
  - `uwImmediate`;
  - `uwCommit`;
  - `uwSaved` (immediate − commit, with its share of immediate: "4 (2/3 ≈
    66.7%)");
  - `uwWrites` (INSERTs, then UPDATEs, then DELETEs, each in order of the
    object's first mention, joined "; ", or `none`);
  - `uwClean` ("1: customer3").

  Banner: "Writes in this order can still break a foreign key; the order view
  is lesson 4.4's."
- `order`. Inputs `keys` (records `child, parent`: the child's table holds a
  key to the parent's) and `as` (optional; space-separated, every table in
  `keys` exactly once, refused otherwise).
  - A cycle is refused, naming its tables.
  - A table that refers to itself is refused with the sentence "a table that
    refers to itself needs its rows ordered, which this lab does not do".

  Tiles:
  - `uwInsertOrder`: parents before children, taking the alphabetically
    first ready table at each step.
  - `uwDeleteOrder`: its reverse.
  - `uwBroken`: only with `as`. Every key whose child comes before its parent
    in `as`, in `keys` order: "3: orders before customer, line before orders,
    line before product".

  Banner: "Ties are broken alphabetically, so this is one valid order of
  several."

#### inherit (`ih`) — family 1

- `tables`. Inputs `classes` (records `class, parent, fields, concrete`:
  name; name or `-`; whole 0–1,000; yes/no; exactly one root, no cycle, every
  parent a class), `load` (a concrete class, refused otherwise), `find` and
  `alter` (classes).

  A class's chain is the class and its ancestors; its subtree is the class
  and its descendants. Every table has a key column, and the single table
  has a type column too. Each tile is "single, class, concrete":
  - `ihTables`: 1; the number of classes; the number of concrete classes.
  - `ihColumns`: 2 + Σ fields; Σ over classes of (1 + own fields); Σ over
    concrete classes of (1 + the chain's fields).
  - `ihEmpty`: one number, single-table only. Σ fields − the chain's fields
    of `load`: the columns empty in a row of that class.
  - `ihLoad`: 1; the size of `load`'s chain; 1.
  - `ihFind` (every instance of `find`, subclasses included): 1; the size of
    chain(find) ∪ subtree(find) (joins up, unions down); the number of
    concrete classes in the subtree.
  - `ihAlter` (add a field to `alter`): 1; 1; the number of concrete classes
    in the subtree.

  The panel states each rule.

#### lock (`ol`) — family 1

- `reads`. Input `items` (records `item, before, after, read, change`: name;
  whole 0–10⁷; whole; before/after; insert/update). One writer commits once;
  each item's value before and after that commit is given, and the reader
  reads each item on one side of it. A read before the commit of an item the
  commit changes (before ≠ after) is **stale**. A read after the commit of a
  changed item is **fresh**.
  Tiles:
  - `olSeen`: Σ of what was read.
  - `olBefore`, `olAfter`: the totals before and after.
  - `olConsistent`:
    - with no stale read, "yes: the state after the commit";
    - with no fresh read, "yes: the state before the commit";
    - otherwise "no: 15 is neither 12 nor 17", or "no: 900 is not 1,000,
      before or after" when the two totals are equal, or "no, though 520
      equals the total after the commit" when the sum agrees by coincidence.
  - `olLevel`:
    - with no stale read or no fresh one, "none needed: no read straddles the
      commit";
    - when every stale item's change is an insert, "repeatable read allows it
      (a phantom); serializable prevents it";
    - otherwise "read committed allows it (an unrepeatable read); repeatable
      read prevents it".

  The panel says the levels are the four standard ones Chapter 5 describes,
  and that a database's own implementation of each can be stronger.
- `timeline`. Inputs:
  - `events` (records `minute, session, action, record`: whole 0–10⁷,
    non-decreasing; name; read/edit/commit; a name, or `-` for a commit);
  - `scheme` (none, optimistic or pessimistic);
  - `groups` (optional, `record=group; …`; a record not listed is its own
    group);
  - `checkReads` (no or yes; read only when the scheme is optimistic).

  Rules:
  - Every group has a version, 0 at the start, and a successful commit adds
    one to the version of each group the session edited.
  - A session's first read or edit of a group records the version it saw.
  - **none**: every commit succeeds; a *lost update* is counted for each
    group a committing session edited whose version has changed since it
    saw it.
  - **optimistic**: a commit fails (a *conflict*) when any group the session
    edited has changed since it saw it. With `checkReads` yes, the groups it
    only read are checked too.
  - **pessimistic**: a session takes the lock on a group at its first read
    or edit of that group, provided it edits the group anywhere in the
    timeline: the lock is acquired when the data is loaded, not when the
    edit begins (Chapter 16, Pessimistic Offline Lock; PDF p. 384 of the
    operator's copy). A read of a group the session never edits takes no
    lock. Taking a lock another session holds is *refused*, at that event:
    the session ends at once and its locks are released. A commit releases
    the session's locks. This is the exclusive write lock, the first of
    Pessimistic Offline Lock's three. The panel says the lock is taken when
    the record is first loaded for editing.
  - A refused or conflicted session's later events are skipped, and the
    banner names them. An event by a session after its own commit is refused
    as a mistake in the input.
  - *Redo* is the minutes from a failed session's first event to its
    failure.

  Tiles:
  - `olCommitted`, `olConflicts`, `olRefused`: each "count: names", in the
    order of the commit or failure.
  - `olLostUpdates`.
  - `olRedo`: total minutes.
  - `olPeakLocks`: the most locks held at once; `—` unless pessimistic.

  Banner: names any session that neither committed nor failed.

#### session (`sn`) — family 2

- `objects`. Inputs `users` (whole 1–10⁷), `serviceMs` (number > 0) and
  `thinkMs` (number ≥ `serviceMs`, the time from one request of a user's to
  the next; refused otherwise). Tiles:
  - `snStateful` (users: one object per user);
  - `snStateless` (users·service/think: the objects busy on average);
  - `snIdle` (1 − service/think, a share);
  - `snPerObject` (think/service: users per stateless object).

  Banner: "An average: a pool sized to it is too small at a peak."
- `state`. Inputs `users`, `stateBytes`, `requests` (wholes 1–10⁷) and
  `idBytes` (whole 0–10⁷). Tiles:
  - `snWire` (2·state: client session state goes to the browser and back on
    every request);
  - `snSessionWire` (2·state·requests);
  - `snIdOnly` (idBytes: what a request carries with server or database
    session state);
  - `snMemory` (users·state: server session state held in memory);
  - `snDatabase` (2·state: database session state read and written once a
    request).

  The panel states the model and says that compression, partial loading and
  caching change every figure.

#### money (`mn`) — family 2

- `allocate`. Inputs `amount` (whole 0–10⁷, in the smallest unit: cents),
  `ratios` (2–20 wholes 0–10⁶, space-separated, at least one positive) and
  `rule`:
  - `nearest`: each exact share rounded half up;
  - `down`: each rounded down;
  - `up`: each rounded up;
  - `last`: nearest for all but the last share, which takes what is left
    (possibly negative, which the banner then says);
  - `allocator`: each rounded down, then the cents left over given one each
    to the shares in order from the first.

  The exact share is amount·ratio/Σ ratios. Tiles:
  - `mnShares` ("4, 2");
  - `mnTotal`;
  - `mnDiff` (total − amount, signed: "+1", "−1", "0");
  - `mnExact` (each exact share, "7/2 = 3.50, 3/2 = 1.50");
  - `mnFurthest` (the largest |share − exact share|).

  The panel says Fowler's Money allows other ways of placing the leftover
  cents, and that `allocator` is the one his example uses.

### D.2 What the kit must never do

- **Call a figure a measurement of the reader's system.** Every banner that
  turns on a timing says it is the lesson's figure.
- **Print a verdict.** No tile or banner says "best", "too slow", "safe" or
  "wrong"; `olConsistent` says whether a total matches a state, which is a
  fact about the instance.
- **Carry a figure from the book as a constant** (§D.0).
- **Run anything**, or evaluate text as script. The kit parses records.
- **Derive a tile from a float**, or from a drawing.
- **Show a tile or offer a control whose meaning depends on comparing
  presets.** A lesson compares presets in prose.
- **Send or store** anything the reader types.

### D.3 Build-time checks

- A Python mirror of `EA_CORE_JS`'s record parser reads every preset at build
  time. It raises, naming the preset and the record, on anything the view
  would refuse: a bad field count, a word not on its list, a cycle, an
  unknown parent, a `load` that is not concrete, an `as` that is not a
  permutation, a session acting after its commit, a non-decreasing minute
  broken.
- An `expect` key that is not one of the view's tiles raises.
- `scripts/mathcheck.js` gets a block `eakit`, one case per view at least, its
  cases the §C values. Each case was seen to fail when its line was broken on
  purpose.

### D.4 The reference model, and the snippets

The eakit figures in §C were computed by `docs/enterprise-patterns/earef.py`,
an exact Python model of every view (integers and `fractions.Fraction`, never a
float), run over every lesson's instances in `docs/enterprise-patterns/presets.py`:

```
python3 docs/enterprise-patterns/earef.py          # every eakit preset
python3 docs/enterprise-patterns/earef.py 4.1 6.2  # some lessons
python3 docs/enterprise-patterns/earef.py --cc     # and the cckit lessons
```

The cckit figures were computed by the shipped cckit JavaScript itself, not a
model of it. `docs/enterprise-patterns/ccrun.js` loads `RATIONAL_JS`,
`CC_CORE_JS`, `CC_LEX_JS`, `CO_JS`, `CO_DECIDE_JS`, the code views (`size`,
`class`, `dupes`, `complexity`, `basis`), `DG_JS` and the deps views
(`coupling`, `ripple`) from `scripts/mathpath/labs/` into a node `vm`, and
runs `coCompute` or `dgCompute` on each job in `presets.CC_JOBS`. Its figures
are cckit's own. If cckit changes, re-run it.

The model is not the kit. The kit is JavaScript, and its figures are read off
the page with `labcheck.js --observe`. Where the two disagree, the kit engineer
finds out which is wrong and records it in the kit report. The three files are
committed with this plan, as specification. They are not imported by the
build, and they are not under `scripts/`.

**One source for each snippet.** In the content package a snippet is one
Python string constant, named as below, used by the lesson's `code` block and,
for a cckit `code` lab, by the preset's `code`. The test of §H.3 asserts that
every cckit `code` preset's code is a `code` block on the same lesson or a
named exercise constant.

**Every snippet compiles.** Each was compiled with `javac --release 8` (JDK
21.0.12) inside a wrapper class, against stub declarations for the types it
uses (`Customer`, `Order`, and the like). All 74 compiled without error. The
harness and stubs are not part of the plan. An author who changes a snippet
compiles it again. Each snippet:

- is at most 20 lines of at most 72 characters, with no tabs;
- uses no records, `var`, lambdas, streams or annotations (not even
  `@Override`, so `equals` and `toString` overrides carry none);
- is new, written for this Subject. None is the book's, and none follows a
  listing of the book's line by line (§E.3).

Line numbers count every line from 1, blank and comment lines included, as
cckit's listing does.

**The snippets**, verbatim from `presets.py`, lesson by lesson. A cckit
preset's or exercise's figures are in its §C entry; "body" marks a snippet
with no lab figures, which the lesson reads and the exercise may use.

#### 1.1 Enterprise Applications

`DUE_DAY` (preset `due-day`; 19 lines):

```java
// Days from the start of the invoice month until payment is due.
int dueDay(Customer c, int invoiceDay) {
    int day = invoiceDay + 30;
    if (c.isGovernment()) {
        day = day + 15;
    }
    if (c.region() == Region.NORTH && c.years() > 5) {
        day = day + 10;
    }
    if (c.isRetail() || c.isOnline()) {
        if (invoiceDay > 25) {
            day = day + 5;
        }
    }
    if (day > 60 && !c.isGovernment()) {
        day = 60;
    }
    return day;
}
```

`DUE_DAY_PLAIN` (preset `due-day-plain`; 4 lines):

```java
// Days from the start of the invoice month until payment is due.
int dueDay(Customer c, int invoiceDay) {
    return invoiceDay + 30;
}
```

`LATE_FEE` (exercise; 17 lines):

```java
// Fee in cents for a late payment, with the agreed exceptions.
long lateFee(Account a, int daysLate) {
    long fee = 0;
    if (daysLate > 10) {
        fee = 500;
    }
    if (daysLate > 30 || a.isFlagged()) {
        fee = 2500;
    }
    if (a.isCharity() && daysLate < 60) {
        fee = 0;
    }
    if (a.isNew() && a.payments() == 0) {
        fee = fee / 2;
    }
    return fee;
}
```

#### 1.2 Thinking About Performance

`RESPONSE_TIME` (body; 6 lines):

```java
// Times one request. Run it at each load you care about.
long responseMillis(Service service, Request request) {
    long start = System.nanoTime();
    service.handle(request);
    return (System.nanoTime() - start) / 1000000;
}
```

#### 1.3 Capacity and Scalability

`SERVERS_NEEDED` (body; 13 lines):

```java
// Servers needed for a target load, from two measured rates.
int serversNeeded(int firstTps, int extraTps, int targetTps) {
    if (extraTps <= 0 && firstTps < targetTps) {
        throw new IllegalArgumentException("more servers add nothing");
    }
    int servers = 1;
    int tps = firstTps;
    while (tps < targetTps) {
        servers = servers + 1;
        tps = tps + extraTps;
    }
    return servers;
}
```

#### 1.4 Layering

`RISING_TWICE` (preset `rising-twice`; 15 lines):

```java
// Web page: show a product, red if sales rose more than 10%.
void showProduct(Product p, Page page) {
    long before = p.salesLastMonth();
    long now = p.salesThisMonth();
    boolean rising = now * 100 > before * 110;
    page.write(p.name(), now, rising);
}

// Command line: the same report, for a script.
void printProduct(Product p, PrintStream out) {
    long before = p.salesLastMonth();
    long now = p.salesThisMonth();
    boolean rising = now * 100 > before * 110;
    out.println(p.name() + " " + now + (rising ? " *" : ""));
}
```

`RISING_ONCE` (preset `rising-once`; 14 lines):

```java
// Domain layer: the rule, in one place.
boolean isRising(Product p) {
    return p.salesThisMonth() * 100 > p.salesLastMonth() * 110;
}

// Presentation: the web page and the command line both ask.
void showProduct(Product p, Page page) {
    page.write(p.name(), p.salesThisMonth(), isRising(p));
}

void printProduct(Product p, PrintStream out) {
    String mark = isRising(p) ? " *" : "";
    out.println(p.name() + " " + p.salesThisMonth() + mark);
}
```

`OVERDUE_TWICE` (exercise; 13 lines):

```java
// Report screen
void showInvoice(Invoice inv, Page page) {
    int days = inv.daysOpen();
    boolean overdue = days > 30 && !inv.isDisputed();
    page.write(inv.number(), overdue);
}

// Nightly export
void exportInvoice(Invoice inv, Writer csv) throws IOException {
    int days = inv.daysOpen();
    boolean overdue = days > 30 && !inv.isDisputed();
    csv.write(inv.number() + "," + overdue + "\n");
}
```

#### 1.5 Layer Supertype and Separated Interface

`SEPARATED_FINDER` (body; 19 lines):

```java
// Domain package: the interface the domain needs.
interface OrderFinder {
    Order find(long id);
}

// Domain package: Order uses only the interface.
class Order {
    private static OrderFinder finder;
    static void setFinder(OrderFinder f) { finder = f; }
    static Order load(long id) { return finder.find(id); }
}

// Mapper package: the implementation, which knows the SQL.
class OrderMapper implements OrderFinder {
    public Order find(long id) {
        // SELECT ... FROM orders WHERE id = ?
        return new Order();
    }
}
```

#### 2.1 Transaction Script

`TWO_SCRIPTS` (preset `two-scripts`; 17 lines):

```java
// Script for "place order".
void placeOrder(Order o) {
    long total = o.subtotal();
    if (o.customer().isMember()) {
        total = total - total / 10;
    }
    db.insertOrder(o.id(), total);
}

// Script for "quote price": the same discount, copied.
long quotePrice(Order o) {
    long total = o.subtotal();
    if (o.customer().isMember()) {
        total = total - total / 10;
    }
    return total;
}
```

`SHARED_SUBROUTINE` (preset `shared-subroutine`; 16 lines):

```java
// The discount, once, as a subroutine both scripts call.
long memberPrice(Order o) {
    long total = o.subtotal();
    if (o.customer().isMember()) {
        total = total - total / 10;
    }
    return total;
}

void placeOrder(Order o) {
    db.insertOrder(o.id(), memberPrice(o));
}

long quotePrice(Order o) {
    return memberPrice(o);
}
```

`SHIPPING_TWICE` (exercise; 19 lines):

```java
// Script for "check out".
void checkOut(Cart cart) {
    long cents = cart.totalCents();
    long shipping = 499;
    if (cents >= 5000) {
        shipping = 0;
    }
    db.insertOrder(cart.id(), cents + shipping);
}

// Script for "show basket".
void showBasket(Cart cart, Page page) {
    long cents = cart.totalCents();
    long shipping = 499;
    if (cents >= 5000) {
        shipping = 0;
    }
    page.write(cents, shipping);
}
```

#### 2.2 Domain Model

`PRICE_BY_KIND` (preset `price-by-kind`; 12 lines):

```java
// One routine prices every kind of product.
long price(Product p, int qty) {
    long cents = p.unitCents() * qty;
    if (p.kind() == Kind.BOOK) {
        cents = cents - cents / 20;
    } else if (p.kind() == Kind.ALCOHOL) {
        cents = cents + cents / 5;
    } else if (p.kind() == Kind.FOOD && qty > 10) {
        cents = cents - cents / 10;
    }
    return cents;
}
```

`PRICE_DELEGATED` (preset `price-delegated`; 18 lines):

```java
// Each kind of product carries its own rule; Product is the default.
class Product {
    long unitCents;
    long adjust(long cents, int qty) { return cents; }
    long price(int qty) { return adjust(unitCents * qty, qty); }
}
class Book extends Product {
    long adjust(long cents, int qty) { return cents - cents / 20; }
}
class Alcohol extends Product {
    long adjust(long cents, int qty) { return cents + cents / 5; }
}
class Food extends Product {
    long adjust(long cents, int qty) {
        if (qty > 10) { return cents - cents / 10; }
        return cents;
    }
}
```

`SHIPPING_BY_METHOD` (exercise; 13 lines):

```java
// Shipping cost in cents, by method and weight.
long shippingCents(Parcel p) {
    if (p.method() == Method.POST) {
        return 300 + 50 * p.kilos();
    } else if (p.method() == Method.COURIER && p.kilos() > 20) {
        return 2500;
    } else if (p.method() == Method.COURIER) {
        return 1200;
    } else if (p.method() == Method.COLLECT || p.isStaff()) {
        return 0;
    }
    return 999;
}
```

#### 2.3 Table Module, and Making a Choice

`TABLE_MODULE` (body; 16 lines):

```java
// One object for the whole invoice-line table, not one per row.
class InvoiceLines {
    private final RecordSet rows;

    InvoiceLines(RecordSet rows) {
        this.rows = rows;
    }

    long totalCents(long invoiceId) {
        long total = 0;
        for (Record r : rows.where("invoice_id", invoiceId)) {
            total = total + r.getLong("cents");
        }
        return total;
    }
}
```

#### 2.4 Service Layer

`ORDERS_TWICE` (preset `orders-twice`; 18 lines):

```java
// The web page and the nightly import both place orders.
void webPlace(Request req) {
    Order order = orders.fromForm(req);
    db.begin();
    inventory.reserve(order);
    order.confirm();
    db.commit();
    mailer.sendConfirmation(order);
}

void importPlace(Row row) {
    Order order = orders.fromRow(row);
    db.begin();
    inventory.reserve(order);
    order.confirm();
    db.commit();
    mailer.sendConfirmation(order);
}
```

`ORDERS_SERVED` (preset `orders-served`; 17 lines):

```java
// Each client builds its order, then asks the service to place it.
void webPlace(Request req) {
    service.placeOrder(orders.fromForm(req));
}

void importPlace(Row row) {
    service.placeOrder(orders.fromRow(row));
}

// In OrderService: the application logic, in one place.
void placeOrder(Order order) {
    db.begin();
    inventory.reserve(order);
    order.confirm();
    db.commit();
    mailer.sendConfirmation(order);
}
```

`CANCEL_TWICE` (exercise; 18 lines):

```java
void webCancel(Request req) {
    Order order = orders.find(req.param("id"));
    db.begin();
    inventory.release(order);
    order.cancel();
    db.commit();
    mailer.sendCancellation(order);
}

void phoneCancel(ApiCall call) {
    audit.record(call);
    Order order = orders.find(call.field("order"));
    db.begin();
    inventory.release(order);
    order.cancel();
    db.commit();
    mailer.sendCancellation(order);
}
```

#### 2.5 Value Object

`DATE_RANGE_MUTABLE` (preset `mutable-range`; 12 lines):

```java
class DateRange {
    public LocalDate start;
    public LocalDate end;

    public void setEnd(LocalDate end) {
        this.end = end;
    }

    public boolean includes(LocalDate d) {
        return !d.isBefore(start) && !d.isAfter(end);
    }
}
```

`DATE_RANGE_VALUE` (preset `value-range`; 19 lines):

```java
final class DateRange {
    private final LocalDate start;
    private final LocalDate end;

    DateRange(LocalDate start, LocalDate end) {
        this.start = start;
        this.end = end;
    }

    public boolean equals(Object o) {
        if (!(o instanceof DateRange)) { return false; }
        DateRange r = (DateRange) o;
        return start.equals(r.start) && end.equals(r.end);
    }

    public int hashCode() {
        return 31 * start.hashCode() + end.hashCode();
    }
}
```

`QUANTITY_MUTABLE` (exercise; 17 lines):

```java
class Quantity {
    public int amount;
    public String unit;
    private final int max = 1000;

    public void add(int n) {
        amount = amount + n;
    }

    public String toString() {
        return amount + " " + unit;
    }

    int room() {
        return max - amount;
    }
}
```

#### 2.6 Money

`REFUND_SPLIT` (body; 19 lines):

```java
// Refunds an order across the payments that paid for it, in
// proportion to each; Money does the splitting, this checks it.
List<Refund> refund(Money total, List<Payment> paid) {
    long[] weights = new long[paid.size()];
    for (int i = 0; i < weights.length; i++) {
        weights[i] = paid.get(i).amount().cents();
    }
    Money[] parts = total.splitBy(weights);
    Money sum = Money.zero(total.currency());
    List<Refund> out = new ArrayList<Refund>();
    for (int i = 0; i < parts.length; i++) {
        sum = sum.plus(parts[i]);
        out.add(new Refund(paid.get(i), parts[i]));
    }
    if (!sum.equals(total)) {
        throw new IllegalStateException("refund parts do not add up");
    }
    return out;
}
```

#### 2.7 Special Case

`NULL_CHECKS` (preset `null-checks`; 11 lines):

```java
String greeting(Customer c) {
    String name = "friend";
    if (c != null && c.name() != null) {
        name = c.name();
    }
    String plan = "basic";
    if (c != null && c.plan() != null) {
        plan = c.plan().title();
    }
    return "Dear " + name + ", your plan: " + plan;
}
```

`GUEST_CUSTOMER` (preset `guest-customer`; 9 lines):

```java
// The finder returns a GuestCustomer instead of null.
class GuestCustomer extends Customer {
    String name() { return "friend"; }
    Plan plan() { return Plan.BASIC; }
}

String greeting(Customer c) {
    return "Dear " + c.name() + ", your plan: " + c.plan().title();
}
```

`NULL_ADDRESS` (exercise; 11 lines):

```java
String label(Order o) {
    Address a = o.address();
    String city = "unknown";
    if (a != null && a.city() != null) {
        city = a.city();
    }
    if (a == null || a.postcode() == null) {
        return city;
    }
    return city + " " + a.postcode();
}
```

#### 3.1 Gateways

`PRICE_GATEWAY` (body; 16 lines):

```java
// All the SQL for the price table, in one class.
class PriceGateway {
    private final Connection db;

    PriceGateway(Connection db) {
        this.db = db;
    }

    long findCents(String sku) throws SQLException {
        PreparedStatement s = db.prepareStatement(
            "SELECT cents FROM price WHERE sku = ?");
        s.setString(1, sku);
        ResultSet rs = s.executeQuery();
        return rs.next() ? rs.getLong(1) : -1;
    }
}
```

#### 3.2 Row Data Gateway, and Reading in Data

`ORDER_ROW` (body; 18 lines):

```java
// A gateway for one row of the orders table, and its finder.
class OrderRow {
    final long id;
    String status;

    OrderRow(long id, String status) {
        this.id = id;
        this.status = status;
    }

    static OrderRow find(Connection db, long id) throws SQLException {
        PreparedStatement s = db.prepareStatement(
            "SELECT status FROM orders WHERE id = ?");
        s.setLong(1, id);
        ResultSet rs = s.executeQuery();
        return rs.next() ? new OrderRow(id, rs.getString(1)) : null;
    }
}
```

#### 3.3 Active Record

`ACCOUNT_RECORD` (preset `active-record`; 19 lines):

```java
// An Active Record: a row's data, its SQL and its domain logic.
class Account {
    private long id;
    private long balance;
    private long overdraft;

    static Account find(Connection db, long id) throws SQLException {
        // SELECT balance, overdraft FROM account WHERE id = ?
        return new Account();
    }

    void update(Connection db) throws SQLException {
        // UPDATE account SET balance = ? WHERE id = ?
    }

    public boolean canWithdraw(long cents) {
        return balance + overdraft >= cents;
    }
}
```

`ACCOUNT_ROW` (preset `row-gateway`; 15 lines):

```java
// A Row Data Gateway: the same row, with no domain logic.
class AccountRow {
    private long id;
    private long balance;
    private long overdraft;

    static AccountRow find(Connection db, long id) throws SQLException {
        // SELECT balance, overdraft FROM account WHERE id = ?
        return new AccountRow();
    }

    void update(Connection db) throws SQLException {
        // UPDATE account SET balance = ? WHERE id = ?
    }
}
```

`MEMBER_RECORD` (exercise; 18 lines):

```java
class Member {
    private long id;
    public String email;
    private int points;
    public final String joined = "2024-01-01";

    static Member find(Connection db, long id) throws SQLException {
        return new Member();
    }

    public void insert(Connection db) throws SQLException {
        // INSERT INTO member (email, points) VALUES (?, ?)
    }

    public int level() {
        return points / 1000;
    }
}
```

#### 3.4 Data Mapper

`ACCOUNT_MAPPER` (body; 17 lines):

```java
// The mapper knows the table and the class; Account knows neither.
class AccountMapper {
    private final Connection db;

    AccountMapper(Connection db) {
        this.db = db;
    }

    Account find(long id) throws SQLException {
        PreparedStatement s = db.prepareStatement(
            "SELECT balance, overdraft FROM account WHERE id = ?");
        s.setLong(1, id);
        ResultSet rs = s.executeQuery();
        rs.next();
        return new Account(id, rs.getLong(1), rs.getLong(2));
    }
}
```

#### 3.5 Building the Mapping

`TWO_SOURCES` (preset `two-sources`; 18 lines):

```java
// The same customer arrives from a table and from a message.
Customer fromRow(ResultSet rs) throws SQLException {
    String name = rs.getString("name");
    String postcode = rs.getString("postcode");
    long limit = rs.getLong("credit_limit");
    Customer c = new Customer(name.trim(), postcode.toUpperCase());
    c.setCreditLimit(limit);
    return c;
}

Customer fromMessage(Element msg) {
    String name = msg.getAttribute("name");
    String postcode = msg.getAttribute("post_code");
    long limit = Long.parseLong(msg.getAttribute("limit"));
    Customer c = new Customer(name.trim(), postcode.toUpperCase());
    c.setCreditLimit(limit);
    return c;
}
```

`TWO_STEP` (preset `two-step`; 18 lines):

```java
// Step one, per source, holds the differences: to a logical record.
CustomerData fromRow(ResultSet rs) throws SQLException {
    return new CustomerData(rs.getString("name"),
        rs.getString("postcode"), rs.getLong("credit_limit"));
}

CustomerData fromMessage(Element msg) {
    return new CustomerData(msg.getAttribute("name"),
        msg.getAttribute("post_code"),
        Long.parseLong(msg.getAttribute("limit")));
}

// Step two, once, holds what they share: the record to the object.
Customer toCustomer(CustomerData d) {
    Customer c = new Customer(d.name.trim(), d.postcode.toUpperCase());
    c.setCreditLimit(d.limit);
    return c;
}
```

`SHIPMENT_TWICE` (exercise; 18 lines):

```java
void toTable(Shipment s, PreparedStatement st) throws SQLException {
    String ref = s.ref().toUpperCase();
    long grams = Math.round(s.kilos() * 1000);
    String to = s.postcode().replace(" ", "");
    st.setString(1, ref);
    st.setLong(2, grams);
    st.setString(3, to);
    st.executeUpdate();
}

void toMessage(Shipment s, Element msg) {
    String ref = s.ref().toUpperCase();
    long grams = Math.round(s.kilos() * 1000);
    String to = s.postcode().replace(" ", "");
    msg.setAttribute("ref", ref);
    msg.setAttribute("grams", Long.toString(grams));
    msg.setAttribute("to", to);
}
```

#### 3.6 Database Connections and Registry

`SAVE_LINES_BATCH` (body; 13 lines):

```java
// Sends every line of an order to the database in one call.
void saveLines(Connection db, long orderId, List<Line> lines)
        throws SQLException {
    PreparedStatement s = db.prepareStatement(
        "INSERT INTO line (order_id, sku, qty) VALUES (?, ?, ?)");
    for (Line line : lines) {
        s.setLong(1, orderId);
        s.setString(2, line.sku());
        s.setInt(3, line.qty());
        s.addBatch();
    }
    s.executeBatch();
}
```

#### 4.1 Unit of Work

`UNIT_OF_WORK` (body; 20 lines):

```java
// Remembers what changed; writes it all at commit. GONE: never written.
class UnitOfWork {
    enum Mark { NEW, DIRTY, REMOVED, GONE }
    private final Map<Entity, Mark> pending = new LinkedHashMap<>();
    void mark(Entity e, Mark asked) {
        Mark now = pending.get(e);
        boolean kept = now == Mark.NEW || now == Mark.REMOVED;
        boolean undone = now == Mark.NEW && asked == Mark.REMOVED;
        pending.put(e, undone ? Mark.GONE : kept ? now : asked);
    }
    void commit(Mapper db) {
        for (Map.Entry<Entity, Mark> p : pending.entrySet()) {
            switch (p.getValue()) {
                case NEW: db.insert(p.getKey()); break;
                case DIRTY: db.update(p.getKey()); break;
                case REMOVED: db.delete(p.getKey()); break;
            }
        }
    }
}
```

#### 4.2 Identity Map

`IDENTITY_MAP` (body; 19 lines):

```java
// One object per row: a second find returns the same object.
class CustomerMapper {
    private final Map<Long, Customer> loaded =
        new HashMap<Long, Customer>();

    Customer find(long id) throws SQLException {
        Customer c = loaded.get(id);
        if (c == null) {
            c = load(id);
            loaded.put(id, c);
        }
        return c;
    }

    private Customer load(long id) throws SQLException {
        // SELECT ... FROM customer WHERE id = ?
        return new Customer(id);
    }
}
```

#### 4.3 Lazy Load

`LAZY_LINES` (body; 19 lines):

```java
// Loads an order's lines the first time something asks.
class Order {
    private final long id;
    private final LineMapper mapper;
    private final List<Line> lines = new ArrayList<>();
    private boolean linesLoaded = false;
    Order(long id, LineMapper mapper) {
        this.id = id;
        this.mapper = mapper;
    }

    List<Line> lines() throws SQLException {
        if (!linesLoaded) {
            lines.addAll(mapper.linesOf(id));
            linesLoaded = true;
        }
        return lines;
    }
}
```

#### 4.4 Identity Field and Foreign Keys

`SAVE_NEW_ORDER` (body; 9 lines):

```java
// Saves a new order and its lines: the parent row goes first.
void saveNew(Order order) throws SQLException {
    long orderId = keys.next("orders");
    insertOrder(orderId, order.customerId());
    for (Line line : order.lines()) {
        long lineId = keys.next("line");
        insertLine(lineId, orderId, line.sku(), line.qty());
    }
}
```

#### 4.5 Embedded Value and Serialized LOB

`EMBEDDED_TERM` (body; 7 lines):

```java
// The lease's term has no table of its own: it is two columns.
Lease load(ResultSet rs) throws SQLException {
    DateRange term = new DateRange(
        rs.getDate("term_start").toLocalDate(),
        rs.getDate("term_end").toLocalDate());
    return new Lease(rs.getLong("id"), term);
}
```

`LOB_TEXT` (body; 9 lines):

```java
// Writes a whole department tree into one text column.
String toText(Dept d) {
    StringBuilder out = new StringBuilder();
    out.append('(').append(d.name());
    for (Dept child : d.children()) {
        out.append(' ').append(toText(child));
    }
    return out.append(')').toString();
}
```

#### 4.6 Single Table Inheritance

`SINGLE_TABLE_LOAD` (body; 13 lines):

```java
// One table for every kind of staff; a type column says which.
Staff load(ResultSet rs) throws SQLException {
    String type = rs.getString("type");
    long id = rs.getLong("id");
    String name = rs.getString("name");
    if (type.equals("M")) {
        return new Manager(id, name, rs.getInt("reports"));
    }
    if (type.equals("C")) {
        return new Contractor(id, name, rs.getLong("day_rate"));
    }
    return new Employee(id, name, rs.getLong("salary"));
}
```

#### 4.7 Class and Concrete Table Inheritance

`CLASS_TABLE_FIND` (body; 7 lines):

```java
// A manager's fields live in three tables, one per class.
static final String FIND_MANAGER =
    "SELECT p.name, e.salary, m.reports"
    + " FROM person p"
    + " JOIN employee e ON e.id = p.id"
    + " JOIN manager m ON m.id = p.id"
    + " WHERE p.id = ?";
```

#### 4.8 Metadata Mapping, Query Object and Repository

`HAND_MAPPING` (preset `hand-mapping`; 20 lines):

```java
Member findMember(long id) throws SQLException {
    PreparedStatement s = db.prepareStatement(MEMBER_BY_ID);
    s.setLong(1, id);
    ResultSet rs = s.executeQuery();
    rs.next();
    Member m = new Member(id);
    m.email = rs.getString("email");
    m.city = rs.getString("city");
    return m;
}
Shop findShop(long id) throws SQLException {
    PreparedStatement s = db.prepareStatement(SHOP_BY_ID);
    s.setLong(1, id);
    ResultSet rs = s.executeQuery();
    rs.next();
    Shop p = new Shop(id);
    p.name = rs.getString("name");
    p.city = rs.getString("city");
    return p;
}
```

`METADATA_FIND` (preset `metadata-find`; 18 lines):

```java
// The mapping held as data: each column and the field it fills.
static final String[][] MEMBER_MAP = {{"email", "email"},
                                      {"city", "city"}};

// One finder for every mapped class, which reads the map.
<T> T find(Class<T> type, String sql, String[][] map, long id)
        throws Exception {
    PreparedStatement s = db.prepareStatement(sql);
    s.setLong(1, id);
    ResultSet rs = s.executeQuery();
    rs.next();
    T obj = type.getDeclaredConstructor(long.class).newInstance(id);
    for (String[] column : map) {
        Object value = rs.getObject(column[0]);
        type.getDeclaredField(column[1]).set(obj, value);
    }
    return obj;
}
```

`INVOICE_FINDERS` (exercise; 20 lines):

```java
Invoice findInvoice(long id) throws SQLException {
    PreparedStatement s = db.prepareStatement(INVOICE_BY_ID);
    s.setLong(1, id);
    ResultSet rs = s.executeQuery();
    rs.next();
    Invoice i = new Invoice(id);
    i.total = rs.getLong("total");
    i.due = rs.getDate("due");
    return i;
}

Receipt findReceipt(long id) throws SQLException {
    PreparedStatement s = db.prepareStatement(RECEIPT_BY_ID);
    s.setLong(1, id);
    ResultSet rs = s.executeQuery();
    rs.next();
    Receipt r = new Receipt(id);
    r.paid = rs.getLong("paid");
    return r;
}
```

#### 5.1 Model View Controller

`CONCERT_MODEL` (body; 18 lines):

```java
// The model knows nothing of pages; the view asks the model.
class Concert {
    private final String act;
    private final String venue;
    Concert(String act, String venue) {
        this.act = act;
        this.venue = venue;
    }
    String act() { return act; }
    String venue() { return venue; }
}

class ConcertView {
    String render(Concert c) {
        return "<h1>" + escape(c.act()) + " at " + escape(c.venue())
            + "</h1>";
    }
}
```

#### 5.2 Page Controller

`CONCERT_PAGE` (preset `concert-page`; 13 lines):

```java
// The page controller for one page: read input, choose a view.
void doGet(Request req, Response res) throws IOException {
    Concert c = concerts.find(req.param("id"));
    if (c == null) {
        res.forward("missing.jsp", null);
    } else if (c.isSoldOut()) {
        res.forward("waitlist.jsp", c);
    } else if (c.isSeated() && c.hasSeatMap()) {
        res.forward("seats.jsp", c);
    } else {
        res.forward("tickets.jsp", c);
    }
}
```

`CONCERT_PAGE_SPLIT` (preset `concert-page-split`; 6 lines):

```java
// The decisions move to a presentation helper; the model keeps its
// own predicates, and the controller only forwards.
void doGet(Request req, Response res) throws IOException {
    Concert c = concerts.find(req.param("id"));
    res.forward(helper.viewFor(c), c);
}
```

`BOOKING_PAGE` (exercise; 17 lines):

```java
void doPost(Request req, Response res) throws IOException {
    Booking b = bookings.find(req.param("id"));
    String seats = req.param("seats");
    if (b == null || seats == null) {
        res.forward("error.jsp", null);
        return;
    }
    int n = Integer.parseInt(seats);
    if (n < 1 || n > 8) {
        res.forward("booking.jsp", b);
    } else if (b.isPaid() && !b.isRefundable()) {
        res.forward("locked.jsp", b);
    } else {
        b.setSeats(n);
        res.forward("confirm.jsp", b);
    }
}
```

#### 5.3 Front Controller

`PAGES_REPEAT` (preset `pages-repeat`; 13 lines):

```java
void orderPage(Request req, Response res) throws IOException {
    User u = sessions.user(req);
    if (u == null) { res.redirect("/login"); return; }
    audit.log(u, req.path());
    res.forward("order.jsp", orders.find(req.param("id")));
}

void invoicePage(Request req, Response res) throws IOException {
    User u = sessions.user(req);
    if (u == null) { res.redirect("/login"); return; }
    audit.log(u, req.path());
    res.forward("invoice.jsp", invoices.find(req.param("id")));
}
```

`PAGES_SUPERCLASS` (preset `page-superclass`; 20 lines):

```java
// A Layer Supertype runs the shared steps; each page adds its own.
abstract class SecurePage {
    void doGet(Request req, Response res) throws IOException {
        User u = sessions.user(req);
        if (u == null) { res.redirect("/login"); return; }
        audit.log(u, req.path());
        show(req, res);
    }
    abstract void show(Request req, Response res) throws IOException;
}
class OrderPage extends SecurePage {
    void show(Request req, Response res) throws IOException {
        res.forward("order.jsp", orders.find(req.param("id")));
    }
}
class InvoicePage extends SecurePage {
    void show(Request req, Response res) throws IOException {
        res.forward("invoice.jsp", invoices.find(req.param("id")));
    }
}
```

`FRONT_HANDLER` (preset `front-handler`; 8 lines):

```java
// One handler for every request; a command does each page's part.
void handle(Request req, Response res) throws IOException {
    User u = sessions.user(req);
    if (u == null) { res.redirect("/login"); return; }
    audit.log(u, req.path());
    Command c = commands.get(req.path());
    c.run(req, res);
}
```

`REPORTS_REPEAT` (exercise; 13 lines):

```java
void salesReport(Request req, Response res) throws IOException {
    res.setHeader("Cache-Control", "no-store");
    Locale locale = locales.forRequest(req);
    Report r = reports.sales(req.param("month"));
    res.forward("sales.jsp", r.in(locale));
}

void stockReport(Request req, Response res) throws IOException {
    res.setHeader("Cache-Control", "no-store");
    Locale locale = locales.forRequest(req);
    Report r = reports.stock(req.param("depot"));
    res.forward("stock.jsp", r.in(locale));
}
```

#### 5.4 Template View and Transform View

`TICKET_ROW` (preset `ticket-row`; 13 lines):

```java
// A row of the page, with its decisions inline.
String row(Ticket t) {
    String html = "<tr><td>" + escape(t.section()) + "</td>";
    if (t.seatsLeft() < 10 || t.isLastRelease()) {
        html = html + "<td class=\"few\">";
    } else {
        html = html + "<td>";
    }
    if (t.isResale() && !t.isLastRelease()) {
        html = html + "resale ";
    }
    return html + t.seatsLeft() + "</td></tr>";
}
```

`TICKET_HELPER` (preset `ticket-helper`; 11 lines):

```java
// The helper decides; the template only prints what it is given.
class TicketHelper {
    private final Ticket t;
    TicketHelper(Ticket t) { this.t = t; }
    boolean isFew() {
        return t.seatsLeft() < 10 || t.isLastRelease();
    }
    boolean showResale() {
        return t.isResale() && !t.isLastRelease();
    }
}
```

`PRICE_CELL` (exercise; 13 lines):

```java
String cell(Item item, Locale locale) {
    String html = "<td>";
    if (item.onSale() && item.saleCents() < item.cents()) {
        html = html + "<s>" + money(item.cents(), locale) + "</s> ";
        html = html + money(item.saleCents(), locale);
    } else {
        html = html + money(item.cents(), locale);
    }
    if (item.stock() == 0 || item.isWithdrawn()) {
        html = html + " (unavailable)";
    }
    return html + "</td>";
}
```

#### 5.5 Two Step View

`SECOND_STAGE` (body; 20 lines):

```java
// Stage one builds a logical screen; stage two turns it into HTML.
class Field {
    final String label;
    final String value;
    Field(String label, String value) {
        this.label = label;
        this.value = value;
    }
}

class HtmlRenderer {
    String render(List<Field> screen) {
        StringBuilder out = new StringBuilder("<dl>");
        for (Field f : screen) {
            out.append("<dt>").append(escape(f.label)).append("</dt>")
               .append("<dd>").append(escape(f.value)).append("</dd>");
        }
        return out.append("</dl>").toString();
    }
}
```

#### 5.6 Application Controller

`FLOW_REPEAT` (preset `flow-repeat`; 12 lines):

```java
void afterAddress(Order o, Response res) throws IOException {
    if (o.needsCustomsForm()) { res.redirect("/customs"); return; }
    if (o.total() > LIMIT) { res.redirect("/approval"); return; }
    res.redirect("/payment");
}

void afterCart(Order o, Response res) throws IOException {
    if (!o.hasAddress()) { res.redirect("/address"); return; }
    if (o.needsCustomsForm()) { res.redirect("/customs"); return; }
    if (o.total() > LIMIT) { res.redirect("/approval"); return; }
    res.redirect("/payment");
}
```

`NEXT_SCREEN` (preset `next-screen`; 7 lines):

```java
// The flow in one place: which screen comes next.
String nextScreen(Order o) {
    if (!o.hasAddress()) { return "/address"; }
    if (o.needsCustomsForm()) { return "/customs"; }
    if (o.total() > LIMIT) { return "/approval"; }
    return "/payment";
}
```

`CLAIM_FLOW` (exercise; 12 lines):

```java
void afterDetails(Claim c, Response res) throws IOException {
    if (c.amount() > 10000) { res.redirect("/assessor"); return; }
    if (c.hasInjury()) { res.redirect("/medical"); return; }
    res.redirect("/bank");
}

void afterPhotos(Claim c, Response res) throws IOException {
    if (c.photos() == 0) { res.redirect("/photos"); return; }
    if (c.amount() > 10000) { res.redirect("/assessor"); return; }
    if (c.hasInjury()) { res.redirect("/medical"); return; }
    res.redirect("/bank");
}
```

#### 6.1 Concurrency Problems

`COUNT_FILES` (body; 6 lines):

```java
// Two reads, and another session may commit between them.
int countFiles(Connection db) throws SQLException {
    int a = count(db, "locking");
    int b = count(db, "multiphase");
    return a + b;
}
```

#### 6.2 Optimistic and Pessimistic Control

`TWO_CONTROLS` (body; 19 lines):

```java
class FileStore {
    private final Map<String, Integer> versions = new HashMap<>();
    private final Map<String, String> lockedBy = new HashMap<>();
    // Optimistic: detect a conflict when the session commits.
    boolean canCommit(String file, int versionWhenRead) {
        return versions.getOrDefault(file, 0) == versionWhenRead;
    }

    // Pessimistic: lock a file the session will edit before it is
    // loaded, so the session works on the latest version or not at all.
    boolean tryLoadForEdit(String file, String session) {
        String holder = lockedBy.get(file);
        if (holder != null && !holder.equals(session)) {
            return false;
        }
        lockedBy.put(file, session);
        return true;
    }
}
```

#### 6.3 Transactions and Isolation

`COUNT_SERIALIZABLE` (body; 8 lines):

```java
// Both counts inside one serializable transaction.
int countFiles(Connection db) throws SQLException {
    db.setAutoCommit(false);
    db.setTransactionIsolation(Connection.TRANSACTION_SERIALIZABLE);
    int total = count(db, "locking") + count(db, "multiphase");
    db.commit();
    return total;
}
```

#### 6.4 Optimistic Offline Lock

`OPTIMISTIC_SAVE` (body; 11 lines):

```java
// Saves only if nobody has changed the row since it was read; false
// tells the caller to reload the invoice and let the user try again.
boolean trySave(Connection db, Invoice inv) throws SQLException {
    PreparedStatement s = db.prepareStatement(
        "UPDATE invoice SET total = ?, version = version + 1"
        + " WHERE id = ? AND version = ?");
    s.setLong(1, inv.total());
    s.setLong(2, inv.id());
    s.setInt(3, inv.version());
    return s.executeUpdate() == 1;
}
```

#### 6.5 Pessimistic and Coarse-Grained Locks

`GROUP_LOCK` (body; 10 lines):

```java
// Locks the order, not the line: one lock covers the group.
boolean tryEdit(Line line, String session) {
    String key = "order:" + line.orderId();
    String holder = owners.get(key);
    if (holder != null && !holder.equals(session)) {
        return false;
    }
    owners.put(key, session);
    return true;
}
```

#### 6.6 The Value of Statelessness

`STATELESS_HANDLER` (body; 16 lines):

```java
// Stateless: what a request needs arrives with it or is read
// from the database, so any server object can serve it.
class CartHandler {
    private final CartStore store;

    CartHandler(CartStore store) {
        this.store = store;
    }

    String handle(String cartId, String sku) {
        Cart cart = store.load(cartId);
        cart.add(sku);
        store.save(cart);
        return cart.summary();
    }
}
```

#### 6.7 Session State

`SERVER_SESSION` (body; 14 lines):

```java
// Server Session State: carts stay in server memory, keyed by
// the id the browser sends back with every request.
class Carts {
    private final Map<String, Cart> byId = new HashMap<String, Cart>();

    Cart forSession(String id) {
        Cart cart = byId.get(id);
        if (cart == null) {
            cart = new Cart();
            byId.put(id, cart);
        }
        return cart;
    }
}
```

#### 7.1 Distribution Strategies

`REMOTE_CUSTOMER` (body; 6 lines):

```java
// Each call on this interface crosses the network.
interface RemoteCustomer extends Remote {
    String name() throws RemoteException;
    String city() throws RemoteException;
    long creditCents() throws RemoteException;
}
```

#### 7.2 Remote Facade

`CUSTOMER_FACADE` (body; 16 lines):

```java
// One remote call does the work of several local ones.
class CustomerFacade {
    private final CustomerRepository customers;

    CustomerFacade(CustomerRepository customers) {
        this.customers = customers;
    }

    void moveHouse(long id, String street, String city, String code) {
        Customer c = customers.find(id);
        c.address().setStreet(street);
        c.address().setCity(city);
        c.address().setPostcode(code);
        customers.save(c);
    }
}
```

#### 7.3 Data Transfer Object

`ORDER_DTO` (body; 8 lines):

```java
// Everything the order screen shows, in one serializable bundle.
class OrderDto implements Serializable {
    long id;
    String customerName;
    String status;
    long totalCents;
    List<String> lineSummaries = new ArrayList<String>();
}
```

#### 7.4 Putting It All Together

`PLACE_ORDER_STACK` (body; 11 lines):

```java
// One request through every layer: the service runs the domain
// logic inside a unit of work, and the mappers do the SQL.
String placeOrder(String cartId) throws SQLException {
    UnitOfWork uow = new UnitOfWork();
    Cart cart = carts.find(cartId);
    Order order = cart.checkOut();
    uow.markNew(order);
    uow.markChanged(cart);
    uow.commit(mapper);
    return "Order " + order.number() + " placed";
}
```

#### 7.5 Plugin and Service Stub

`ADDRESS_STUB` (body; 20 lines):

```java
// The interface the signup depends on, and a stub for its tests.
interface AddressCheck {
    boolean deliverable(String postcode);
}
class AddressCheckStub implements AddressCheck {
    public boolean deliverable(String postcode) {
        return !postcode.startsWith("ZZ");
    }
}

// The plugin: one switch on the environment, read once at startup.
class AddressChecks {
    static AddressCheck forEnvironment(String environment) {
        switch (environment) {
            case "test": return new AddressCheckStub();
            case "live": return new PostOfficeCheck();
            default: throw new IllegalArgumentException(environment);
        }
    }
}
```

### D.5 The cckit views reused, and why each fits

Twenty lessons use cckit, unchanged but for §H.1, with cfg exactly as
`docs/code-complete/kit-report.md` documents it. The rule for reuse was
strict: cckit is used only where the pattern's argument is about code that the
pattern changes, and where one of cckit's counts is the count the chapter
makes in words. That is duplication removed, a conditional removed, a mutable
field removed, or a dependency reversed. Where the argument is about rows,
calls, writes, locks or bytes, the lesson uses eakit, even if a cckit view
could be bent to it. No eakit view duplicates a cckit one. The review (§R)
found seven of the first draft's twenty bent to fit (2.4, 3.1, 3.3, 3.5, 4.8,
5.2, 5.3); each was rebuilt or narrowed, and the table says what each now
counts.

| lesson | cckit view | the chapter's count it makes |
| --- | --- | --- |
| 1.1 Enterprise Applications | `code/complexity` | the special cases in "illogical" business logic |
| 1.4 Layering | `code/dupes` | the domain logic a second presentation would duplicate (Fowler's own test) |
| 1.5 Layer Supertype and Separated Interface | `deps/ripple` | what a change below reaches once the domain no longer depends on it |
| 2.1 Transaction Script | `code/dupes` | the duplication Fowler names as the pattern's failing |
| 2.2 Domain Model | `code/complexity` | the conditional that polymorphism distributes |
| 2.4 Service Layer | `code/dupes` | the application logic (transaction, notification) each kind of client repeats without the layer, Stafford's argument |
| 2.5 Value Object | `code/class` | the public mutable fields that make aliasing possible |
| 2.7 Special Case | `code/complexity` | the null checks the pattern removes |
| 3.1 Gateways | `deps/ripple` | where a schema change is edited (`dgDirect`, the pinned tile); `dgAffected` is shown as the upper bound if the gateway's interface changed |
| 3.3 Active Record | `code/class` | the routines only (`coRoutines`); the reader sorts them into database access and domain logic, which the kit cannot |
| 3.4 Data Mapper | `deps/ripple` | the dependency the mapper reverses, and the one it adds |
| 3.5 Building the Mapping | `code/dupes` | the duplication double mapping causes with one mapping per source, which a two-step mapping removes |
| 4.8 Metadata Mapping, Query Object and Repository | `code/dupes` | "simple and repetitive" hand-written mapping, Chapter 3's own words, which Metadata Mapping holds as data |
| 5.1 Model View Controller | `deps/ripple` | what a presentation change reaches when the model knows the presentation |
| 5.2 Page Controller | `code/complexity` | the decisions an input controller holds, which move to a presentation helper |
| 5.3 Front Controller | `code/dupes` | the common behaviour page controllers repeat, which a superclass and a front handler both remove; the count does not choose between them, and the body says so |
| 5.4 Template View and Transform View | `code/complexity` | the logic in a page that a helper takes out |
| 5.5 Two Step View | `deps/ripple` | what a change of look reaches with one stage and with two |
| 5.6 Application Controller | `code/dupes` | flow repeated across controllers (the pattern's own signal) |
| 7.5 Plugin and Service Stub | `deps/ripple` | whether a test is reached by a change to the real service |

**cfg, exactly.** Keys: `mode`, `view`, `preset`, `presets` (each `id`,
`label`, `code` or `edges` and `changed`, `expect`), `panel_title`,
`panel_intro`. For `code/dupes` add `"min_run": 2`; for `code/complexity`
add `"bands": [5, 10]` and, once §H.1 lands, `"book": "other"`. Nothing else
is passed. Two complete examples, as lessons 2.7 and 3.4 give them:

```python
"lab": ("cckit", {
    "mode": "code",
    "view": "complexity",
    "bands": [5, 10],
    "book": "other",                      # once §H.1 lands
    "preset": "null-checks",
    "presets": [
        {"id": "null-checks",
         "label": "A greeting that checks for a missing customer twice",
         "code": NULL_CHECKS,
         "expect": {"coDecisions": "5", "coBreakdown": "1 + if 2 + && 2"}},
        {"id": "guest-customer",
         "label": "The same greeting, given a GuestCustomer",
         "code": GUEST_CUSTOMER,
         "expect": {"coDecisions": "1", "coBreakdown": "1"}},
    ],
    "panel_title": "The null checks a Special Case removes",
    "panel_intro": (
        "The lab counts decision points by a stated rule: one, plus one for each "
        "if, while, for, case, && and ||. The bands beside the count are "
        "McConnell's, from Code Complete; Fowler gives no count. The listings "
        "are the lesson's."
    ),
}),
```

```python
"lab": ("cckit", {
    "mode": "deps",
    "view": "ripple",
    "preset": "active-record",
    "presets": [
        {"id": "active-record",
         "label": "Active Record: the account holds its own SQL",
         "edges": "screen, account; report, account; account, jdbc",
         "changed": "jdbc",
         "expect": {"dgDirect": "1: account",
                    "dgAffected": "3: account, report, screen"}},
        {"id": "active-record-domain-change",
         "label": "Active Record, with the account class changed",
         "edges": "screen, account; report, account; account, jdbc",
         "changed": "account",
         "expect": {"dgDirect": "2: report, screen",
                    "dgAffected": "2: report, screen"}},
        {"id": "mapper",
         "label": "Data Mapper: the mapper holds it, and main wires the mapper",
         "edges": "screen, account; report, account; mapper, account; "
                  "mapper, jdbc; main, mapper",
         "changed": "jdbc",
         "expect": {"dgDirect": "1: mapper", "dgAffected": "2: main, mapper"}},
        {"id": "mapper-domain-change",
         "label": "The same design, with the account class changed",
         "edges": "screen, account; report, account; mapper, account; "
                  "mapper, jdbc; main, mapper",
         "changed": "account",
         "expect": {"dgDirect": "3: mapper, report, screen",
                    "dgAffected": "4: main, mapper, report, screen"}},
    ],
    "panel_title": "What a change reaches, with and without a mapper",
    "panel_intro": (
        "Each record is one dependency, written dependent, dependency. Name the "
        "class that changes; the lab lists what depends on it directly and "
        "everything the change reaches. The designs are the lesson's."
    ),
}),
```

The other eighteen follow the same shape, with the presets and expectations of
their §C entries. Two cckit facts every author needs:

- `deps/ripple` is a breadth-first search from `changed` along reversed
  edges, and it excludes `changed` itself. So it terminates on a cycle (1.5's
  `mapper-in-domain`), and `changed` never appears in `dgAffected`.
- The `code` views read a fragment as well as a routine. `PRICE_DELEGATED`,
  `GUEST_CUSTOMER`, `TICKET_HELPER` and `PAGES_SUPERCLASS` are classes, and
  the kit counts the whole listing. Each lesson's body says so where it
  matters.
- `code/dupes` finds identical lines only (after cckit's own
  normalisation). Lines that repeat in shape with different names, such as
  3.5's source reads and 4.8's field copies, are not counted, and those
  lessons' bodies say so: the repetition the pattern removes is wider than
  the count.

---

## §E Package layout, the source text, quoting, and the author's checklist

### E.1 Layout

```
content/enterprise_patterns/
  __init__.py                         PATH, COURSES (filter COURSE = None), numbering loop
  c1_layers_and_performance/          __init__.py (COURSE; lessons = part_a.LESSONS), part_a.py
  c2_domain_logic/                    part_a.py (Chapters 2, 9), part_b.py (Chapter 18)
  c3_data_source/                     part_a.py
  c4_objects_and_tables/              part_a.py (4.1–4.4), part_b.py (4.5–4.8)
  c5_web_presentation/                part_a.py
  c6_concurrency_and_session_state/   part_a.py (6.1–6.3), part_b.py (6.4–6.7)
  c7_distribution/                    part_a.py
content/spoken/enterprise_patterns.py SPOKEN = {}
```

Mirror `content/code_complete/__init__.py` for the package `__init__`, with
PATH `"speech": "code"`, and `content/code_complete/c2_high_quality_code/` for
a course with two part files. Course and lesson fields are exactly Code
Complete's. Lesson keys:

```
slug, title, module, one_line, summary, key, key_label, concepts_intro,
concepts, read_title, read_intro, body, lab, steps_title, steps_intro,
steps, worked {title, intro, lines, after}, quiz_title,
quiz [{q, a, c, why}], mistakes, standard, note
```

Each lesson has 3 concepts, 4 steps and 3 mistakes, and a `body` of 7–18
blocks (a `code` block counts as one). The snippets are module-level
constants in the part file that uses them, named as in §D.4.

### E.2 The source text

The Subject's single source is **Martin Fowler, with David Rice, Matthew
Foemmel, Edward Hieatt, Robert Mee and Randy Stafford, *Patterns of Enterprise
Application Architecture* (Boston: Addison-Wesley, 2002), ISBN
0-321-12742-0**, copyright 2003 by Pearson Education, Inc. The operator's copy
is a PDF without printed page numbers. Its text was extracted privately, one
form feed per PDF page, to
`/tmp/claude-0/-home-claude/d46a89a5-ae93-5f9f-84a3-4e1ae07e83c0/scratchpad/book/poeaa.txt`.
That file is **outside the repository, never committed, never copied in.**

**Pages.** In this copy, the PDF page equals the page number in the copy's
own table of contents (Unit of Work, PDF p. 174). Every page in this document
is a PDF page. The book's in-text cross-references, such as "Unit of Work
(184)" or "Class Table Inheritance (285)", are the printed pages of the
paper edition. They are offset from this copy by an amount that varies (Unit
of Work is 10 pages earlier here, Class Table Inheritance 24). So they are
never cited, never converted, and never quoted: no quotation in §C contains
one. A lesson cites the book by chapter, section and pattern ("Chapter 11, Unit
of Work"). The PDF page goes only in a source comment beside the lesson dict,
marked as the operator's copy (`# PDF p. 174 of the operator's copy`).

Three helpers sit beside the extraction, in `…/scratchpad/tools/`. They print
short matches only, never stretches of the text:

- `eabook.py <regex> [-C n]` prints each matching line as `pdfpage | line`.
  An author greps the text with it; **nobody reads the extraction whole, and
  nothing from it enters the repository beyond the quotations §E.3 allows.**
- `eapage.py` prints one page, for checking a section's place.
- `ea_quotes.py <file>` checks lines `tag|pdfpage|quote` against that page and
  the next, and prints OK, LOOSE or MISS with the word count. All 44 opening
  quotations in §C are OK. One (7.3's) keeps the book's own "its" for "it's",
  as printed.

What the text settled: every chapter, section and pattern title and page in
§B and §C; every figure in §S.2; the works in §S.1; and every opening
quotation. If the orchestrator moves the extraction, it records the new route
in `docs/enterprise-patterns/AUTHORING.md` (created at authoring, as Code
Complete's was). The route never goes in a lesson.

### E.3 Quoting

*Patterns of Enterprise Application Architecture* is in copyright. The rules
are Code Complete's §E.3, applied to this book:

- A lesson may open with **one quotation of at most 40 words**, and only where
  the sentence states the section's argument. §C's **Quote** line gives each
  lesson's, with its PDF page and word count (8 to 35 words). A lesson's
  quotations total at most **60 words**, the opening one included. No
  lesson's argument depends on a quotation.
- **Never reproduce the book's code listings, tables, figures or
  sketches.** They are not retyped and not "adapted" line by line, and that
  includes Table 5.1 and every UML sketch. A table's *content* may be stated
  in the lesson's own sentences, as 6.3 does with the isolation levels, and a
  figure the narrative gives (Swordfish's 20 tps) may be used as a fact with
  its source.
- **The book's example domains are not used for code, and neither is the
  shape of its listings.** The revenue recognition example, the players
  hierarchy, the album, artist and track pages, the sales-tax Service Stub,
  the utility's "occupant" and the other Part 2 examples stay in the book;
  every snippet here has its own domain. Where a snippet does what one of
  the book's listings does (a Unit of Work, an allocator, a lazy load, a
  version check), it is written in a different structure, not the listing
  with the names changed (§R records the three that were, and their
  replacements). A lab preset may use a narrative's illustrative figures (*F1*–*F23*),
  marked with their source.
- Every quoted phrase is copied from the source text, character for
  character, with its PDF page in a comment beside the lesson dict. It is
  never copied from memory, from a secondary source or from this document.
- Quotations the book makes of others (Alexander's definition of a pattern)
  are attributed to their author and, if quoted, taken from the book's
  citation and counted against the same limits.
- This document quotes the book only in §C's **Quote** lines and in a few
  phrases of two to eight words in §C and §S.2 that identify a claim ("a rare
  stand on the side of meaninglessness" is the longest, at 8 words, in 4.4's
  misconception; it counts against that lesson's 60, for a total of 19).

### E.4 The author's checklist

The per-lesson procedure of Code Complete §E.4, with
`python3 scripts/preview_subject.py enterprise_patterns --course <slug> --out <dir>`
to render, and these differences:

1. Open with §C's **Quote** (or none), set as the first body block with its
   PDF page in a comment. Then the section's argument in the lesson's own
   words, citing it by chapter, section and pattern, never by page. Every
   figure attributed to the book carries its §S.2 id and PDF page in a
   comment (`# F5, PDF p. 28 of the operator's copy`).
2. Every `code` block is one of §D.4's snippets, or a new one written for the
   lesson, compiled, and recorded here. For a cckit `code` lab the preset's
   `code` is the same constant.
3. Every preset id appears in a body `p` with the figures it shows. Every tile
   a view prints is explained in prose at least once in the course. The
   `inherit` tiles' three parts are named in order the first time.
4. The exercise (§B) is an `h3` "Exercise", a `code` block or a small table,
   and a `p` that says what to find. Its answer is the `why` of one quiz item,
   and nowhere else.
5. **Quiz items** (3–4 per lesson). Each item's options differ by a fact the
   reader can check: a count, a statement number, a table name, which
   session commits, the section's claim. Never quiz a verdict ("which pattern
   is best?"). Where an item turns on a rule (the Unit of Work's write
   rules, an isolation level), the stem states the rule or names the
   section. Distractors are §C's misconceptions or the off-by-one answer.
6. The last of the `steps` is §C's **Own:** line.
7. **Length.** The `body` stays within 7–18 blocks. A lesson whose reading
   needs more is split in this document first. §C's minutes are the
   author's estimate; a lesson past 20 minutes is shortened.
8. Inline code in prose stays short: an identifier, a call, a table name. A
   statement longer than about 40 characters goes in a `code` block. SQL in
   prose is upper-case keywords in a backtick run (`SELECT`, `WHERE`).
9. Run `/usr/bin/python3 scripts/speechcheck.py`, and listen to one lesson per
   course with the read-out (the code dialect is on through PATH `speech`).

---

## §F Voice: the read-along, for a working programmer

Code Complete's §F holds where this section is silent: the argument first,
then the code; "you", warmly; the history of an idea as a story with people
in it, at most once a lesson; at most one light remark, preferably pointing at
the author's own (Fowler has many: the cornered rat of Where You Have to
Distribute, the two watches of Identity Map, the "unresistable pun" of Special
Case); the `note` names the lesson's one limit; the last `p` points to the
next lesson by title; no slang, no first-person anecdotes, no "let's".

What is different for this book:

1. **Two kinds of reading.** The narratives are an argument, read through.
   The patterns are a reference, looked up. A lesson reads its narrative
   section as an argument ("Fowler's case is…") and its pattern as a tool
   ("Unit of Work keeps a record of what changed…"), and says which it is
   doing.
2. **Fowler is presented, not endorsed.** The book is a catalogue of practice
   to 2002, written, as Fowler says, in early 2002 (*F23*), and much of it is
   now the vocabulary of the field. A lesson states his position at strength,
   with his own hedges. He hedges often: "it depends", "measure", "use this
   advice to prod your thinking". The lesson does not harden them into rules.
3. **At most one modern aside per course**, in the `note` or a late `p` of
   the lesson named here, stating the later view at strength and not
   settling it:
   - Course 1, Layering: browser-built presentation, and where the layers
     run now (Choosing Where to Run Your Layers).
   - Course 2, Domain Model: Evans's *Domain-Driven Design*, which the book's
     references list as in preparation and which carried the Domain Model
     further.
   - Course 3, Data Mapper: the O/R mapping frameworks that now implement Data
     Mapper, Unit of Work and Identity Map for the reader, as a continuation
     of the chapter, not a view against it.
   - Course 4, Embedded Value and Serialized LOB: databases that can query
     inside a document column, which changes the LOB's cost Fowler names.
   - Course 5, Template View and Transform View: presentation built in the
     browser.
   - Course 6, Transactions and Isolation: snapshot isolation in multiversion
     databases, a level the chapter's four do not name, with its own anomaly.
   - Course 7, Putting It All Together: services and microservices, argued in
     Chapter 7's vocabulary and sometimes against its First Law.

   Never "outdated", "legacy" or "modern developers know better" in the
   lesson's voice. The view named here is never a lesson's `mistakes[0]`.
4. **The numbers are the lesson's.** Fowler gives few figures, and those he
   gives are illustrations (Swordfish and Camel are invented, and he says
   systems differ). A lesson says once, where it uses one, that it is the
   book's illustration. It never says "studies show", and it never turns an
   illustration into a benchmark.
5. **No platform wars.** The book's examples are Java and C#, and its
   technology advice is J2EE and .NET of 2002. No lesson says one platform
   is better. Where the book's advice is tied to a platform (Record Set tools,
   entity beans), the lesson says so in a sentence and moves on.
6. **Where the book names a pattern's author, the lesson names them.** The
   book is Fowler's, and eight of its patterns and several examples are by
   contributors, each named on the pattern's first page (and all thanked in
   the Preface, p. 18): Service Layer is Randy Stafford's (p. 133);
   Optimistic Offline Lock (p. 374), Pessimistic Offline Lock (p. 382),
   Implicit Lock (p. 400) and Service Stub (p. 445) are David Rice's;
   Coarse-Grained Lock (p. 391) and Plugin (p. 441) are Rice's and Matt
   Foemmel's; Repository is Edward Hieatt's and Rob Mee's (p. 294). Chapter
   5 is Fowler's and Rice's (p. 72); the Unit of Work example is Rice's (p.
   178); the Identity Field and Registry examples are Foemmel's and
   Fowler's (pp. 205, 427); Money's allocation conundrum is Foemmel's (p.
   432) and its example Foemmel's and Fowler's (p. 433). The lesson writes
   "Stafford's Service Layer, in Fowler's book" and quotes a contributor's
   pattern as the contributor's, never as Fowler's.

**One exemplary paragraph** (a `p` for Unit of Work, after the argument):

> You have probably written a save that runs as it goes: load the order,
> change its status, write it; add a line, write it; change your mind about
> the line, delete it. Each step is correct, and the database sees every one
> of them. Run the lesson's first preset and count: six writes issued as the
> script happens, against two at commit, an INSERT for the line that
> survived and one UPDATE for the order however often it changed. The line
> that was added and deleted never reaches the database at all. That is
> Fowler's whole argument in a number: if you let the Unit of Work remember
> what changed, the four writes in between were never needed, and a commit
> that writes two rows holds its locks for less time than one that writes
> six.

---

## §G What is left out, and why

- **The book's code listings, sketches, tables and worked examples.**
  Copyright (§E.3). The examples are where the book is at its best, and the
  lessons point to them by pattern.
- **Platform specifics**: the J2EE and .NET details of 2002 (entity beans,
  ADO.NET data sets, ASP.NET code-behind), and the book's Java and C#
  libraries. Named where the book names them; not taught.
- **Stored procedures and database tuning.** Named in Down to the Data Source
  Layer and Some Technology-Specific Advice; not taught. The lessons need
  only a one-table query and, once, a join.
- **Explicit multithreading.** Application Server Concurrency is read, and
  its policy (avoid explicit synchronisation) stated; the mechanics are not
  taught.
- **The "Further Reading" sections.** The works are listed in §S.1 where a
  lesson cites them; the reading lists are not reproduced.
- **What has happened since 2002**, beyond §F.3's seven asides: ORM
  frameworks in detail, REST and GraphQL, message brokers, cloud deployment,
  microservice patterns, browser frameworks. A lesson may say in one sentence
  what is different now, under §F.3's rule; the Subject does not teach them.
- **Running code.** The labs read records and code and never execute either
  (§D.2). The snippets compile (§D.4), and a reader may run them in their own
  environment; no lesson depends on it.

---

## §S Sources, and the register of figures

### S.1 Sources the lessons may cite

Cited by author and year in prose, and never quoted at length. Every work
except the first is cited **as the book cites it**: "the book cites Alur,
Crupi and Malks", not "Alur found". Each was checked against the book's
References (PDF pp. 452–455) with `eabook.py`.

- Fowler, M., with Rice, D., Foemmel, M., Hieatt, E., Mee, R. and Stafford,
  R. (2002). *Patterns of Enterprise Application Architecture*.
  Addison-Wesley. The source of every lesson.
- Alexander, C., et al. (1977). *A Pattern Language*. Oxford University
  Press. The definition of a pattern, as the Introduction quotes it (1.1).
- Alur, D., Crupi, J. and Malks, D. (2001). *Core J2EE Patterns*. Prentice
  Hall. Intercepting Filter (5.3); one of the layering schemes (7.4).
- Beck, K. (1997). *Smalltalk Best Practice Patterns*. Prentice Hall. Lazy
  initialization, as Lazy Load cites it (4.3).
- Brown, K., et al. (2001). *Enterprise Java Programming with IBM WebSphere*.
  Addison-Wesley. The Brown layers (7.4, and 5.6's mediating layer).
- Evans, E. *Domain Driven* [Design], listed by the book as in preparation.
  Course 2's aside only (§F.3), and then as published (Addison-Wesley,
  2003).
- Gamma, E., Helm, R., Johnson, R. and Vlissides, J. (1995). *Design
  Patterns*. Addison-Wesley. Virtual proxy (4.3), flyweight (2.7),
  singleton (3.6).
- Kirtland (1998). *Designing Component-Based Applications*. Microsoft
  Press. The Microsoft DNA layers (7.4); the book gives the surname only.
- Knight and Dai (2002). "Objects and the Web". *IEEE Software*,
  March/April; the book gives the surnames only. The source of Application Controller's ideas, as the book
  says (5.6).
- Marinescu, F. (2002). *EJB Design Patterns*. Wiley. A layering scheme
  (7.4).
- Nilsson, J. (2002). *.NET Enterprise Design with Visual Basic .NET and SQL
  Server 2000*. Sams. A layering scheme (7.4).
- Woolf, B. "Null Object", in *Pattern Languages of Program Design 3*.
  Special Case (2.7).

### S.2 The register of figures

Every figure a lesson attributes to the book is listed here with the value
the book gives and its PDF page. Each was settled against the text with
`eabook.py`. A lesson prints the figure with a comment `# F<n>, PDF p. <page>
of the operator's copy` beside the dict. A figure not in this table is not
attributed to the book, and every other figure in §C is illustrative.

| id | claim as the lesson uses it | the book's value | where (PDF page) |
| --- | --- | --- | --- |
| F1 | how much data a moderate enterprise system holds | over 1 GB, in tens of millions of records | Introduction, Enterprise Applications, p. 23 |
| F2 | the leasing system's users | no more than a hundred or so at one time | Introduction, Kinds of Enterprise Application, p. 25 |
| F3 | load sensitivity illustration | A: 0.5 s from 10 to 20 users; B: 0.2 s at 10 users rising to 2 s at 20 | Introduction, Thinking About Performance, p. 28 |
| F4 | efficiency illustration | 30 tps on two CPUs is more efficient than 40 tps on four identical CPUs | Thinking About Performance, p. 28 |
| F5 | Swordfish and Camel | Swordfish 20 tps, Camel 40 on one server; 35 and 50 on two; then 15 and 10 a server; Camel more efficient below five servers | Thinking About Performance, p. 28 |
| F6 | the layering example | products whose sales rose over 10 percent on last month, coloured red | Chapter 1, The Three Principal Layers, p. 36 |
| F7 | complexity boosters | among them extreme performance requirements, "more than 100 transactions per second" | Chapter 1, p. 38 |
| F8 | measuring domain complexity | nobody can, says the chapter (Making a Choice) | Chapter 2, p. 42 |
| F9 | the allocation example | 5 cents split 70% and 30% | Chapter 18, Money, p. 432 |
| F10 | the cost of O/R mapping | around a third of programming effort, by anecdotal observation, and continuing in maintenance | Chapter 3, Architectural Patterns, p. 49 |
| F11 | reading in data | one query that brings back unnecessary rows over 50 individual ones; a query up to three or four joins | Chapter 3, Reading in Data, p. 52 |
| F12 | iterations when building the model first | no more than six weeks, preferably fewer | Chapter 3, Building the Mapping, p. 58 |
| F13 | when Fowler uses a Registry | a parameter not needed 90 percent of the time | Chapter 18, Registry, p. 425 |
| F14 | the Unit of Work illustration | one object altered at three points: three calls rather than one | Chapter 11, Unit of Work, p. 178 |
| F15 | the limit of simple metadata | works well 90 percent of the time | Chapter 13, Metadata Mapping, p. 281 |
| F16 | Martin and David's packages | the locking package 7 classes, then 9; the multiphase package 5, then 8; Martin counts 15 where the answer was 12 before and 17 after. Retold with files on p. 80, where the insert case is a phantom and the totals case an unrepeatable read | Chapter 5, Concurrency Problems, p. 73; Transactions, pp. 80–81 |
| F17 | explicit multithreading | a system that works correctly 99 percent of the time but throws random fits | Chapter 5, Application Server Concurrency, p. 84 |
| F18 | the length of a business transaction | a business transaction might take 20 minutes | Chapter 16, Pessimistic Offline Lock, p. 385 |
| F19 | statelessness | one hundred users, one server object each when stateful; with a request every ten seconds taking one, about ten when stateless; 90 percent idle | Chapter 6, The Value of Statelessness, p. 88 |
| F20 | a large session | about a megabyte, "three Shakespeare plays worth", sent as XML | Chapter 6, Session State, p. 90 |
| F21 | expiring server sessions | a session table partitioned into twelve segments, rotated every two hours, so a session active for twenty-four hours is dropped | Chapter 17, Server Session State, p. 408 |
| F22 | a simple Domain Model | a couple of dozen classes close to the database | Chapter 8, Down to the Data Source Layer, p. 102 |
| F23 | the book's date | written in early 2002 | Chapter 8, Some Technology-Specific Advice, p. 104 |
| F24 | the multiappearance saving (5.5) | ten screens and three appearances need thirty single-stage view modules, against ten first stages and three second stages | Chapter 14, Two Step View, p. 336 |

---

## §H Wiring notes for the orchestrator, and the kit work

### H.1 cckit change (`lab-arithmetic` tier), blocking five lessons

cckit's `complexity` view hard-codes two sentences about "the book", meaning
*Code Complete* (`scripts/mathpath/labs/cckit.py`, the complexity banner,
lines 454–455), and its `?:` note says "not the book's" (line 90). On this
path "the book" is Fowler's, and both sentences would be wrong. Lessons 1.1,
2.2, 2.7, 5.2 and 5.4 wait for this change:

- a new lesson-level key `book`, for `complexity` only: `"code-complete"`,
  the default, or `"other"`;
- with `"other"`, the banner reads "The bands are McConnell's guidance in
  *Code Complete* on what to think about doing with a routine, not a grade"
  and "McConnell prints his bands as 0–5, 6–10 and 10+…";
- with `"other"`, the `?:` note reads "the kit's choice, not McConnell's";
- with the default, every string is unchanged, so no Code Complete page
  changes. Its `generated-expectations.json` entries and the
  `test_code_complete_*` tests prove it;
- one `mathcheck.js` case for `"other"`, and the kit report updated.

No other cckit view used here mentions a book (`dupes`, `class`, `coupling`,
`ripple` were read for it). Nothing in the renderer needs changing: the `code`
block and the code read-out landed with Code Complete.

### H.2 eakit (`lab-arithmetic` tier)

Build §D as specified. Its gates are Code Complete's:

- `mathcheck.js` block `eakit`;
- the hostile-input sweep;
- the page-weight measurement;
- the prefix grep.

It also needs a kit report at `docs/enterprise-patterns/kit-report.md`
recording the conventions as implemented and any disagreement with `earef.py`.

### H.3 Wiring

As Code Complete §H.3 and every declaration site in `AGENTS.md` §0, file by
file, with these values:

- **Package and slug.** Package `enterprise_patterns`; path slug
  `enterprise-patterns`. The slug is the package name with `-` for `_`, so
  **no** `build_paths.PACKAGE_OF_SLUG` entry is needed (`package_of`'s
  default rule finds it).
- **Check ids.** Prefix `eaa`; check ids `eaa-course7-lesson-<lesson-slug>`,
  the longest 58 characters (§B); course homes `eaa-courseN-home`; the path
  page `eaa-path`.
- **`content/enterprise_patterns/`** as §E.1; **`content/spoken/enterprise_patterns.py`**
  (ONE file, named for the package), `SPOKEN = {}`.
- **`tests/test_site_invariants.py`**:
  - `EAA_DISCLAIMER_RE = re.compile(r"(?i)not a measurement of your system")`
    beside the thirteen others, with a comment in their style ("Enterprise
    Application Patterns promises that every figure is computed from the
    situation a lesson states, and warns that a count models that situation
    and is not a measurement of the reader's system — Fowler's own rule.
    Stopping short of the em dash, for OR's reason.");
  - its path-page constant `EAA_PATH_PAGE`;
  - its `PATH_MATERIAL_DISCLAIMER` entry ("the not-a-measurement-of-your-system
    disclaimer");
  - the slug tuples, course-home constants, `REQUIRED_PAGES`, and the
    `TestGeneratedPathIsCurrent`, `TestLessonDataMatchesTheRenderer` and
    `TestEveryLabBuilds` import lists.
- **`scripts/build_paths.py`**: import the package and add it to
  `GENERATED_PATHS` (every `COURSE = None`); add `"eakit"` to
  `KITS_WITH_EXPECTATIONS` **last**, after `"cckit"`. `scripts/generated-pages.txt`
  and `scripts/generated-expectations.json` are rewritten by the build.
- **`scripts/mathpath/labs/__init__.py`**: register `"eakit": eakit_lab`.
- **`scripts/smoke.py`**, **`scripts/canvas_sources.js`**.
- **`release/contract.json`** and **`release/contract.example.json`** (both),
  **`release/contract.schema.json`**: each new check id pinned by name, and
  `minItems` equal to the pin count. (This plan's author did not open them;
  the orchestrator edits them as for Code Complete.)
- **`Containerfile.release`** and **`.github/workflows/ci.yml`** enumerations:
  backslash-continued lists, no comment inside them, `bash -n` every `run:`
  block, and never read either through a width-truncating pipe.
- **Content-preservation and the other tests:**
  - `tests/content_preservation.json`: every `.py` in the package, generated
    with `/usr/bin/python3` via the test module's own fingerprint function
    the moment the package joins `GENERATED_PATHS`;
  - `tests/test_review_remediation.py`, `tests/test_public_copy.py` (an
    `enterprise_patterns_semantic_copy`, derived from the rendered page),
    `tests/test_course_ui.py`, `tests/test_canvas_contract.py`,
    `tests/test_browser_source.py`, `tests/test_responsive_ui.py`,
    `tests/test_generation4.py`, `tests/test_generation5_catalog.py`;
  - `tests/browser_acceptance.js`, `tests/browser_contrast.js`,
    `tests/browser_interactions.js`.
- **A new test**, `test_enterprise_patterns_presets_use_the_lessons_snippets`:
  for every cckit lab of mode `code` on this path, each preset's `code` equals
  the joined lines of a `code` block on the same lesson or a named exercise
  constant of the course module.
- **`scripts/catalog.py`**, one entry, last in the `computing` group, after
  Code Complete:

  ```
  {
      "slug": "enterprise-patterns",
      "group": "computing",
      "short_title": "Enterprise Application Patterns",
      "kind": "Read along",
      "card": "Martin Fowler&rsquo;s <em>Patterns of Enterprise Application "
              "Architecture</em>, narrative by narrative, with each "
              "pattern&rsquo;s trade-off counted on a stated situation.",
  },
  ```

  **No `builds_on`.** The Subject assumes no other; Code Complete is a
  companion (§A prerequisites 3), not a prerequisite. The owner decided
  this (§H.4). Placement: last, after Code Complete, for Code
  Complete's own reason (a read-along follows the topical Subjects), and
  because this one reuses Code Complete's kit and reads naturally after it.
  The group note becomes:

  > "Algorithms, System Design and Operations Research build on Discrete
  > Mathematics, the last two on Algebra as well; Code Complete and
  > Enterprise Application Patterns assume only that you can read a short
  > routine."

  It was checked against the copy rules in `catalog.py`'s docstring: no
  "path", no "N subjects", no "course N", no "take these in order". Then
  re-run `scripts/build_index.py` and `scripts/build_auth_pages.py`; never
  edit the site index's generated region by hand.
- **Counts.** The PATH's tagline and description say "Seven courses and 44
  lessons"; the counts test reads the PATH, so §B's total and both sentences
  move together.
- **Counts after wiring** (from the numbers the build reports, not from this
  list):
  - fourteen Subjects;
  - 52 new pages (44 lessons, 7 course homes, 1 path page), so 1,279 pages
    become 1,331;
  - 176 lab modes registered (8 added);
  - 25 kits in `KITS_WITH_EXPECTATIONS`.

  Every "thirteen Subjects", "1,279 pages", "168 lab modes" and "twenty-four
  kits" in `AGENTS.md` §0 and §1, `README.md`'s URL layout and the tests is
  updated in the wiring commit. `AGENTS.md` §0's table gains the row. The
  check-id prefix list gains `eaa`, and the page-weight note gains a
  re-measurement paragraph. The pinned-pages sentence also needs updating:
  "Code Complete's `cckit` for all 41 of its" gains "and for 20 of
  Enterprise Application Patterns' 44, whose other 24 use `eakit`".

### H.4 The owner's decisions

The four questions this section put to the owner are settled:

1. **Short title:** "Enterprise Application Patterns".
2. **`builds_on`:** none. Code Complete is a companion, not a prerequisite.
3. **The share of cckit lessons:** cckit is reused where it genuinely fits.
   After the review (§R), 20 of 44 lessons still use it, but seven of them
   were rebuilt or narrowed so that each count is the one the chapter
   makes (§D.5's table).
4. **The cckit change of §H.1:** accepted; the kit engineer is implementing
   the `book` key.

---

## §R Review record

The specification was reviewed before authoring by an independent accuracy
and pedagogy review that checked every claim about the book, every §S.2
figure, every quotation and every pinned tile against the text, a
recomputation and the shipped cckit
(`docs/reviews/enterprise-patterns-spec-review.md`: MF-1 to MF-13, SF-1 to
SF-27, N-1 to N-14). It was reconciled in one pass with the book's text in
hand. After the edits:

- `earef.py --cc` was re-run, and every backtick tile value in §C was
  compared with its output (181 values, 0 differences);
- all 74 snippets were compiled again with `javac --release 8` (0 errors)
  and checked for at most 20 lines of at most 72 characters;
- all 44 opening quotations were re-located, this time requiring the whole
  quotation on the stated page and not on the page after (SF-3's point),
  and re-counted. Two more errors turned up that the old check had hidden:
  5.1's quotation is on PDF p. 301, not p. 300, and 3.5's new quotation is
  21 words, not 17. Both are corrected; 44 of 44 now pass the same-page
  check.

**Owner decisions recorded with the reconciliation:** short title
"Enterprise Application Patterns" (§A); no `builds_on` (§A); cckit reused
where it genuinely fits, with the seven uses the review called shoehorned
rebuilt or narrowed (§D.5); the §H.1 cckit `book` key accepted, and being
implemented (§H.4).

**Lesson count after review: 44**, unchanged, in the same order. The cckit
share is unchanged at 20 of 44.

### R.1 Changes to §D after the kit started

The kit engineer began building eakit from §D before this reconciliation.
These are the only changes to any eakit mode's rules, inputs, tiles,
refusals or banners. Everything else in §D.0–§D.3 is as it was.

1. **`lock/timeline`, scheme pessimistic: the lock is taken at load** (MF-5;
   Chapter 16, Pessimistic Offline Lock, PDF p. 384 of the operator's copy:
   acquire the lock before loading the data).
   - Before: an `edit` took the lock on its group; a `read` took none.
   - Now: before replaying, the kit collects, for each session, the groups
     it `edit`s anywhere in the timeline. A session's first `read` **or**
     `edit` of such a group takes the lock at that event. A `read` of a
     group the session never edits takes no lock (still the exclusive write
     lock). A session already holding the lock takes nothing new.
   - Refusal is unchanged in kind but can now happen at a `read`: taking a
     lock another session holds refuses the session at that event; it ends
     at once, its locks are released, and *redo* is the minutes from its
     first event to that event. `olPeakLocks` counts as before.
   - The panel adds one sentence: the lock is taken when the record is
     first loaded for editing, not when the edit begins.
   - No input, tile name or tile format changes. Optimistic and none are
     unchanged.
   - Figures that change: 6.2 `pessimistic` → `olCommitted` "1: martin",
     `olRefused` "1: david", `olRedo` 0, `olPeakLocks` 1 (was "1: david",
     "1: martin", 6, 1); 6.2 `exercise-pessimistic` → "1: ann", "1: bo",
     `olRedo` 0 (was 2). 6.5's presets have no reads and are unchanged.
2. **`load/tree`: `ldPerLevel` is depth + 1** (SF-22). The query that finds
   the level below the deepest empty is counted, as `ldPerNode` (1 + nodes)
   already counts each leaf's empty query. The panel's rule sentence says
   both counts include the queries that come back empty. Figures:
   `departments` 5 (was 4), `flat` 3 (was 2), exercise 6 (was 5).
3. **`load/instances`: `ldRatio` is removed and `ldLargest` added**
   (SF-20). `ldLargest` is the table with the most rows and its rows,
   printed "line 6,000" (the name, a space, the grouped count); on a tie,
   the first such table in input order. It is what one Table Module
   object's Record Set holds at most. Figures: `small-shop` "line 6,000",
   `one-big-table` "reading 250,000", exercise "visit 5,400". No other tile
   changes; the pins (`ldRowObjects`, `ldTableObjects`) are unchanged.
4. **Two banner strings** (SF-27, N-8):
   - `uow/commit`: "Writes in this order can still break a foreign key; the
     order view is lesson 4.4's." (was "… is the next lesson's.");
   - `remote/calls`: "The lab assumes the work is the same either way; what
     the coarse calls remove is the waits." (was "The work is the same
     either way; …").

`remote/boundary` is **not** changed (SF-26 was met by changing 7.4's
exercise instance to `nodes` "app=phone", so the database shares the
server's node; it now gives 3 remote calls, 150,054 µs). `presets.py` and
`earef.py` carry all four changes.

### R.2 MUST-FIX

| # | finding | what was done |
| --- | --- | --- |
| MF-1 | `UNIT_OF_WORK` tracks the book's listing | Done. Rewritten as one `Map<Entity, Mark>`, a rule for what each new mark does to the old (new then removed is never written), and a commit that walks the map once and switches on the mark. 4.1's body says the lab groups writes by kind while the snippet writes in first-marked order. |
| MF-2 | `SPLIT_CENTS` adapts the book's allocator | Done. Replaced by `REFUND_SPLIT`, a caller that shares a refund across payments through `Money` and checks the parts add back up. The allocator rule stays the panel's (§D.1), stated as the rule, not as a listing. |
| MF-3 | `TAX_STUB` is the book's Service Stub example | Done. Replaced by `ADDRESS_STUB`: an `AddressCheck` interface, a stub, and a plugin that is one `switch` on the environment name. 7.5's presets are a signup and a post office address check; the exercise is an exchange-rate feed. |
| MF-4 | Course 5 uses the album/artist/track domain | Done. `CONCERT_MODEL` (`Concert`, `ConcertView`); 5.1's nodes `concert`, `concertpage`, `concertreport`; 5.4's `TICKET_ROW` and `TICKET_HELPER`; 5.5's `concertpage`, `venuepage`, `tourpage`, `concert`, `venue`. The only album left is 5.2's quotation. |
| MF-5 | pessimistic lock taken at the edit, not at load | Done; the §D change is R.1 item 1. 6.2's preset, exercise, misconception, Worked line and `TWO_CONTROLS` (`tryLoadForEdit`) follow it; 6.5's Read says the lock is taken before loading. |
| MF-6 | 2.4 gives a verdict the book declines | Done. The misconception is now the domain-logic/application-logic confusion Stafford's Kinds of "Business Logic" refutes (PDF p. 134). Fowler's thin layer is stated as his preference with his concession (p. 44), and the pattern and quotation are Stafford's (pp. 133, 136). |
| MF-7 | 3.1 reads `dgAffected` against its own quotation | Done. `dgDirect` is the pinned count (4 → 1); the panel calls `dgAffected` an upper bound; the misconception is "a gateway is one more class, so a schema change costs more". |
| MF-8 | 3.1's "Also" contradicted by p. 142 | Done. Dropped; the Read now lists a Record Set, a map, a DTO or, with a Domain Model, domain objects, with Fowler's reluctance (p. 142). |
| MF-9 | 5.2 puts view selection in the model | Done. `CONCERT_PAGE_SPLIT` calls `helper.viewFor(c)`; the Standard asks for the helper method; the exercise answer splits the domain predicates (to `Booking`) from the choice of page (to the helper). |
| MF-10 | 5.3 presents the qualified advantage as the reason | Done. New preset `page-superclass` (`PAGES_SUPERCLASS`, a `SecurePage` Layer Supertype, 0 duplicates); the Read and body give Fowler's four reasons (p. 314); the "Also" is "Front Controller is the only way to remove what page controllers repeat". |
| MF-11 | 5.6 inverts When to Use It | Done. The Read and misconception now say it adds little when any screen can be visited in any order, and its strength is definite rules about page order (p. 346). |
| MF-12 | 4.3 `every-order-used` instance differs from §C | Done, the review's preferred way: `o2` keeps 0 children, so lazy and two queries both return 19 rows; §C gives the instance in full and the misconception uses the 6-against-2 statements. |
| MF-13 | 3.4's "one more class" | Done. New preset `active-record-domain-change` ("2: report, screen" for both tiles); the misconception says one more direct dependent and two more classes reached. |

### R.3 SHOULD-FIX

| # | finding | what was done |
| --- | --- | --- |
| SF-1 | co-authors' patterns attributed to Fowler | Done. §F rule 6 names every contributor's pattern and example with its page; 2.4, 2.6, 4.1, 4.8, 6.4, 6.5, 7.5 and Course 6's intro name them; "Fowler's lock manager" and "Fowler's Plugin" are corrected; the four contributor quotations say whose words they are. |
| SF-2 | F3 is on p. 28 | Done (§S.2, 1.2's Read). |
| SF-3 | 7.5's quotation is on p. 446 | Done, and every quotation re-located with a same-page check, which found 5.1's (p. 301, not 300). |
| SF-4 | Table 5.1 is on p. 81 | Done (6.3). |
| SF-5 | 2.1 cites Making a Choice for what it does not say | Done. The refutation cites Transaction Script's own When to Use It (p. 113) and gives Making a Choice's qualifications (pp. 42–43). |
| SF-6 | Money's floating-point reason | Done. "Integral or fixed decimal" (p. 431); the "Also" gives the book's reason and marks the binary explanation as the lesson's. |
| SF-7 | 2.7 overreaches | Done. Refuted with When to Use It (p. 439), the explicit null test (p. 440) and the IEEE NaN example (p. 439). |
| SF-8 | "occupant" and `MissingCustomer` | Done: `GuestCustomer`, "friend". |
| SF-9 | Identity Map scope | Done. The read-only exception (p. 185) is in the Read and the "Also". |
| SF-10 | 4.4 omits deferral | Done. Deferral first (p. 55); the panel says the lab models a database that checks every statement. |
| SF-11 | 3.5's quotation is an aside | Done. The new quotation (p. 58, 21 words) is the short-iterations advice *F12* uses. |
| SF-12 | 6.3's misconception | Done: "Serializable prevents every read error, so use it always", refuted by the liveness sentence that follows the quotation (p. 81). |
| SF-13 | 4.1's "nothing has touched the database" | Done: "nothing has been written to it". |
| SF-14 | 3.6's module | Done. The exception is stated in §B's module rule. |
| SF-15 | `LAZY_LINES`, `OPTIMISTIC_SAVE` track book lines | Done. `LAZY_LINES` keeps a `linesLoaded` flag and calls `linesOf`; `OPTIMISTIC_SAVE` is `trySave`, returning whether one row was updated, with no exception. |
| SF-16 | 3.5's lab does not illustrate the section | Done. The dupes lab is double mapping: one customer mapped from a table and from a message (`TWO_SOURCES`), then a two-step mapping (`TWO_STEP`); the exercise is a shipment written to two sinks. |
| SF-17 | 4.8 sells Query Object | Done. The lab is Metadata Mapping (`HAND_MAPPING` → `METADATA_FIND`); Query Object's conditions (p. 290) are stated in the Read and body. |
| SF-18 | 3.3's count shoehorned | Done, the review's first option: pin `coRoutines` only, and the reader classifies. |
| SF-19 | 2.4's `dgConnected` | Done, the review's better option: `code/dupes` on application logic copied into two clients (`ORDERS_TWICE` → `ORDERS_SERVED`, exercise `CANCEL_TWICE`). |
| SF-20 | 2.3's `ldRatio` | Done; R.1 item 3. |
| SF-21 | 4.3's join looks strictly best | Done without a new tile: the "Also" and its p. 52 citation are dropped, and the panel says the lab counts rows, not their width. A cells tile would have been a further §D change while the kit is being built. |
| SF-22 | 4.5's counts use different rules | Done; R.1 item 2. |
| SF-23 | 2.2's refactors not equivalent | Done. `PRICE_DELEGATED` keeps `Alcohol` and a default `Product`; the exercise answer puts the staff rule in the default class. |
| SF-24 | 7.3's misconception undercut | Done: "Fetch each value only when the screen asks for it"; the exercise stays as the advice's limit. |
| SF-25 | 1.2's misconception defensible | Done: "lower at one load is faster at every load". |
| SF-26 | 7.4 mislabels boundaries | Done. "Above the Service Layer" and "under it"; the panel says one `remoteUs` prices every hop; the exercise puts the database on the server's node so that the phone hop is the question. |
| SF-27 | 4.1 banner; §C line counts | Done (R.1 item 4); every §C line count now matches §D.4, checked by script. |

### R.4 NOTE

| # | note | what was done |
| --- | --- | --- |
| N-1 | example page starts | Done: Unit of Work examples p. 178, Lazy Load p. 189, Chapter 3's Inheritance p. 55. |
| N-2 | 1.1's "Also" | Done: Enterprise Applications, p. 24. |
| N-3 | 4.4's hedge | Done: small or very stable systems may get away with meaningful keys (p. 201). |
| N-4 | 3.2's batched strategy | Done: marked as the lab's; the Read says joins "can really speed things up" (p. 52). |
| N-5 | 6.6's thought experiment | Done: the panel says Fowler calls it completely unrealistic (p. 88). |
| N-6 | 2.6 hides the last-share fault | Done: preset `pennies-to-last` (100 in seven, "14, …, 16"). |
| N-7 | 3.6's lab covers one point | Done: Course 3's `how_to` says so. |
| N-8 | 3.6's "work is the same" | Done: marked as the lab's assumption, in the lesson and the banner. |
| N-9 | 1.3's Standard; `SERVERS_NEEDED` loop | Done: measurements at two server counts; the snippet guards a system that gains nothing. |
| N-10 | course order | Taken in part. Other Layering Schemes moves from 1.5 to 7.4, where every pattern its mappings name has been met. **Declined:** swapping 7.4 and 7.5, because the course follows the book's order, Chapter 8 (PDF pp. 100–109) before Chapter 18's Plugin and Service Stub (pp. 441–448), as every course does with its chapters; ending on two base patterns that read back to 1.5 is the book's own shape. |
| N-11 | `SELECT *` in three snippets | Moot: all three snippets were replaced (SF-16, SF-17), and no snippet now uses `SELECT *`. |
| N-12 | §S.1 lacks Kirtland, Knight and Dai | Done, by surname, as the book's References give them (p. 453). |
| N-13 | `TWO_CONTROLS` unboxing | Done: `getOrDefault`. |
| N-14 | cckit reuse case by case | Done: the seven shoehorned uses are rebuilt or narrowed (§D.5's table); 2.5 pins `coPublicFields` only. |

**Rejected outright:** none. One note was declined in part (N-10's swap),
and two should-fixes were met by the review's other option so as not to
change §D further while the kit is being built (SF-21, SF-26).
