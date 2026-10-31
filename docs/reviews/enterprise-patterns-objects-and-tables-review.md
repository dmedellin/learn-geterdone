# Review: Course 4, Objects and Tables (`enterprise-patterns-objects-and-tables`)

Read against the operator's text (private extraction, `eabook.py`,
`eapage.py`, `ea_quotes.py`), PLAN §C Course 4, §D.0, §D.1 (`load`, `uow`,
`inherit`), §D.4 4.1–4.8, §D.5, §E, §F, §S.2 and §R, `AUTHORING.md`, the
eakit and cckit kit reports, and the rendered preview. Every lesson page was
opened in Playwright (chromium) at 375 px and 1280 px. Each preset was loaded
from the menu and each exercise was typed into its lab. Every pinned tile and
every exercise answer was worked out again by hand. Every line number the prose
cites was checked against the listing as rendered.

Files reviewed: `content/enterprise_patterns/c4_objects_and_tables/__init__.py`,
`part_a.py` (4.1–4.4), `part_b.py` (4.5–4.8), and the `# Objects and Tables`
block of `content/spoken/enterprise_patterns.py`.

Preview: `python3 scripts/preview_subject.py enterprise_patterns --course
enterprise-patterns-objects-and-tables --out …/scratchpad/rev4/out` → 9 pages
rendered; 8 executed and swept, 8 with pinned figures, 0 failing, **OK**.
`speechcheck.py`: enterprise-patterns 0 unresolved. Playwright: no page
errors or console errors; `scrollWidth == clientWidth` on every page at both
widths. Code blocks scroll inside their own box at 375 px, as in every other
course.

**Counts: 3 MUST-FIX, 9 SHOULD-FIX, 10 NOTE.**

---

## What was checked and holds

- **Quotations.** `ea_quotes.py` gives all ten as **OK** and on their stated
  pages: 4.1 p. 50 (18 w), 4.2 p. 183 (16), 4.3 p. 187 (24), 4.4 p. 53 (11)
  and "a rare stand on the side of meaninglessness" p. 201 (8), 4.5 p. 55
  (20), 4.6 p. 57 (13), 4.7 p. 262 (21) and "a heinous crime" p. 278 (3),
  4.8 p. 60 (25). Each one is character-exact with the file text, em dash and
  straight apostrophes included. No lesson goes over 40 words for its
  opening quotation or 60 in total, even after counting 4.4's repeat (N-1).
- **Snippets.** All eleven constants are identical to `presets.py`'s `S[...]`.
  **`UNIT_OF_WORK`** no longer follows Rice's listing. Rice has three lists, four
  `register*` methods with assertions, and a commit that calls insertNew,
  updateDirty and deleteRemoved. The rewrite has one `LinkedHashMap<Entity,
  Mark>`, a three-line rule for a new mark, and one loop with a `switch`, so
  its structure is different. **`LAZY_LINES`** no longer follows the book's
  Supplier/products lazy initialization (a null test with a static finder).
  The rewrite has an injected mapper, a separate `linesLoaded` flag and `addAll`
  into a final list. `IDENTITY_MAP` is a find-then-load guard in an explicit
  mapper, not the book's static `addPerson`/`getPerson` registry methods.
  (`LOB_TEXT` is the exception; see MF-1.)
- **Line numbers.** Every number cited in body, quiz and worked text is right:
  `UNIT_OF_WORK` 4, 5–10, 7, 8, 9, 11–19, 13–17; `IDENTITY_MAP` 3–4, 6–13, 7,
  8, 9, 10, 12, 15–18; `LAZY_LINES` 5, 6, 13, 14, 15, 17; `SAVE_NEW_ORDER`
  3, 4, 7; `EMBEDDED_TERM` 3–5, 6; `LOB_TEXT` 4, 5–7; `SINGLE_TABLE_LOAD` 3,
  4–5, 6–12; `CLASS_TABLE_FIND` 3, 5, 6, 7; `HAND_MAPPING` 2, 3–5, 7–8, 12,
  13–15, 17–18; `METADATA_FIND` 2–3, 8–11, 12, 13–16; `INVOICE_FINDERS` 3–5,
  11, 13, 14–16.
- **Counts, by hand and in the browser.**
  - 4.1 `edit-an-order`: immediate 2 news + 3 changes + 1 delete = 6; commit
    INSERT line1, UPDATE order7; 4 saved, 4/6 = 2/3. `delete-loaded`: 3, 2,
    1/3. Exercise: 7, 3, 4/7 ≈ 57.1%.
  - 4.2 `one-session`: 7, 4, 3. Exercise: 7, 4, 3, "room 12 ×2, guest 3 ×3".
  - 4.3 `orders-and-lines`: N 5, t 3, C_u 12, C 14, so 4/17, 3/17, 2/19, 1/15.
    `every-order-used`: 6/19, 4/19, 2/19, 1/15. Exercise: 4/25, 2/25, 2/28,
    1/23.
  - 4.4: alphabetical topological order and three broken keys. Exercise: one
    broken key, "guest, hotel, room, booking, charge".
  - 4.5 `departments`: 8, 4, 9, 5, 1. `flat`: 4, 2, 5, 3, 1. Exercise: 6, 5, 7,
    6, 1.
  - 4.6 `staff`: tables 1/4/3, columns 11/13/20 (concrete 6 + 8 + 6), empty 2.
    `load-an-employee`: empty 4, find 1/3/2, alter 1/1/1. Exercise: 16, 7
    empty, 18 in 4, 25 in 3.
  - 4.7 both presets, and the exercise 1/3/1, 1/3/2, 1/1/3.
  - 4.8: 1 block of 6 lines at "lines 3–5 and lines 13–15". The exercise in the
    browser gives "lines 3–5 and lines 14–16", which matches the quiz `why`.

  Each prose figure matches its tile, and the models are honest. A lazy query
  for a used parent with no children is still counted. The join counts the
  unused o4's lines. Per-level counts the empty level. The class-table find is
  "joins up, unions down".
- **Exercise answers** appear only in the correct option and the `why` of
  their quiz item.
- **Structure** (§E.1): bodies have 12–14 blocks, every lesson has 3 concepts,
  4 steps and 3 mistakes, and quizzes have 3–4 items. Every preset id is named
  in a body `p` with its figures. The `inherit` tile order is named the first
  time it is used (4.6). The last step of each lesson is §C's **Own** line.
  The one modern aside is in 4.5, in a late `p`, and stated without settling
  the question. The attribution `how_to` is present. Repository is credited to
  Hieatt and Mee wherever it appears in the body, concepts and quiz, and the
  Identity Field example to Foemmel and Fowler.
- **Book claims verified at strength** (a selection): caller registration
  "more confusion than worthwhile" and the explicit copy (p. 175); the
  controller's selective update (p. 176); deferral first, "no good reason not
  to" (pp. 55, 177); fixed table order against deadlocks (p. 177); *F14* (p.
  178); explicit maps preferred, one map per inheritance tree, Unit of Work
  "by far the best place" (p. 184); the Data Mapper double check (p. 164);
  Lazy Load's four forms, Beck, the Gang of Four, the proxy identity problem,
  ripple loading "cripple", two degrees of laziness, "usually pointless" in
  the same row, Fowler's preference not to use it until needed (pp. 187–189);
  *F11* (p. 52); meaningful keys, the hedge, long integer, database-unique
  keys allowing one map (pp. 201–202); the GUID's costs and the key table in
  its own transaction (p. 203); Embedded Value as a special case of Dependent
  Mapping, reference objects mostly one-to-one, SQL query as its advantage
  (pp. 246–247); BLOB/CLOB, versioning, duplication and the snapshot
  exception, single-owner reachability, "considered less often than it might
  be" (pp. 249–250); the inheritance trade-off, compression, Fowler's first
  choice, DBAs (p. 57); single-table strengths and weaknesses (p. 255);
  class-table joins and outer joins (pp. 261–262); concrete-table keys,
  references to abstract classes, superclass finds (pp. 269–271);
  Inheritance Mappers (pp. 277–278); reflection, generation and
  "unsophisticated", the 90 percent warning, Layer Supertype, refactoring
  (pp. 280–281); Query Object's When to Use It (p. 290); Repository (pp.
  294–295).

---

## MUST-FIX

### MF-1. 4.5 Embedded Value and Serialized LOB: `LOB_TEXT` and the `departments` preset reuse the book's Serialized LOB example domain and the shape of its listing

**What is wrong.** §E.3 says the book's example domains are not used for
code, and neither is the shape of its listings, which are not "the listing
with the names changed". Serialized LOB's own example (Chapter 12, PDF pp.
250–252) is **a department hierarchy**. A `Department` with a name and a list
of subsidiary departments has a recursive `toXmlElement()`: make an element
holding the name, iterate the children, and add each child's serialization.
The book's sample output is a department tree of regions. `LOB_TEXT` is the
same domain ("Writes a whole department tree into one text column", `Dept`,
`d.name()`, `d.children()`) and the same structure: emit the name, loop over
the children, append the recursive call, close. Only S-expressions stand in
for XML. The lab presets carry the domain into the counts too: `departments`
(company, sales, north, south, it, support…) and `flat`, with the prose
calling it "a company with sales and IT, sales with two regions", and the
lesson's own link line ("A tree of departments is one kind of hierarchy").
The spec review (MF-1 to MF-4) caught the same fault in four other snippets
and missed this one, so it is in §D.4 too.

**Evidence.** `part_b.py` lines 35–44 (`LOB_TEXT`), 239–241, 243–250,
280–290, 271; book pp. 250–252 (example heading, `Department` class,
recursive `toXmlElement`).

**Fix.** Pick a domain the book does not use for this pattern, such as a
discussion thread (post and replies), a product category tree or a folder
tree. Do not use org charts or bills of materials, which Chapter 3 names.
Write the serializer in a different structure. For example, a preorder walk
with an explicit stack that writes one `depth name` line per node, or a
writer that emits each node as `id parent name` triples. Either is a CLOB
with no recursive element builder. Rename the presets (`thread` / `flat` or
similar) and change their node names, the body's description, the worked
lines and the 4.5 → 4.6 link sentence to match. The figures can keep the
same shape: 8 nodes, depth 4, 9 / 5 / 1, and 4, 2, 5 / 3 / 1. Update
`presets.py` and PLAN §C 4.5 / §D.4 in the same pass, and record it in §R.
Re-run `ea_quotes.py` and the preview after the edit.

### MF-2. 4.8 Metadata Mapping, Query Object and Repository: the `note` credits Fowler with advice about Repository that the book does not give

**What is wrong.** The note says the lab "does not count Query Object or
Repository at all, which Fowler himself advises most hand-built projects to
do without or to buy." For Query Object this holds: "most projects don't use
them if they have a handbuilt data source layer", and "you're almost always
better off buying a tool" (p. 290). For **Repository** it is a verdict the
book does not give. Repository is Hieatt and Mee's pattern, not Fowler's
(§F rule 6). Its When to Use It recommends it for large systems with many
domain types and queries, and especially for multiple data sources and
in-memory testing (pp. 295–296). Nowhere does it say to do without it or to
buy it. A reader of the `note`, the lesson's single stated limit, comes away
with the opposite of the pattern's own advice, and with it attached to the
wrong author.

**Evidence.** `part_b.py` lines 1189–1195; book p. 290 (Query Object, When to
Use It), pp. 294–296 (Repository, by Edward Hieatt and Rob Mee).

**Fix.** Limit the claim to Query Object, for example: "…and it does not count
Query Object or Repository at all. Of Query Object, Fowler says most
hand-built data source layers do without one and that buying a tool is
almost always better; Repository, Hieatt and Mee's, is worth most in a large
system with many queries or more than one data source."

### MF-3. Unmarked verbatim runs of 9–16 words from the book, in four lessons

**What is wrong.** §E.3 and AUTHORING.md require every phrase copied from the
text to be marked as a quotation, given a PDF-page comment and counted
against the lesson's 60 words. Never copy a stretch of the text otherwise. A
7-gram comparison of every learner-facing string against the extraction
(labs excluded) found these runs inside unquoted prose:

| lesson | where | run (words) | page |
| --- | --- | --- | --- |
| 4.2 | quiz 2 stem + `why` | "the primary purpose of an Identity Map … is to maintain correct identities, not to boost performance" (6 + 9) | 50 |
| 4.2 | concept "Session scope" | "more work than any sane developer wants" (7) | 184 |
| 4.3 | concept "Lazy Load" | "An object that does not contain all the data you need but knows how to get it" (the pattern's intent sentence, 16 with one word changed) | 187 |
| 4.5 | body p2 | "no sane person would want a table of money values" (10) | 246 |
| 4.5 | mistakes[0] | "turns the database into little more than a transactional file system" (opening quotation repeated without marks) | 55 |
| 4.7 | body p2 | "the relationship between the domain model and the database is very straightforward" (12) | 262 |
| 4.7 | body p2 | "joins of more than three or four tables tend to be slow" (11, one word changed) | 261 |
| 4.8 | body p4 | "a useful alternative is to override the generic code with" (10) | 281 |
| 4.8 | body p4, quiz 2 `why`, mistakes[0] | "a simple metadata scheme often works well 90 percent of the time" (11, three times) | 281 |
| 4.1 | mistakes[0] | "a transaction open for the whole interaction, which is impractical" (10) | 174 |

4.6's body p3–p4 and quiz 2 are close paraphrases of Chapter 3's p. 57 in
nearly the book's own order: "its great advantage … puts everything in one
place, which makes [modification] easier and avoids joins", which the
lesson even introduces as "in Chapter 3's words", and "first choice tends to
be Single Table Inheritance, as … easy to do and resilient to many
refactorings … the other two as needed … irrelevant and wasted columns".

**Fix.** For each run, either reword it in the lesson's own sentence, or set
it in quotation marks with its `# PDF p. N` comment and add it to the
lesson's total. Even with every run quoted, each total stays under 60: 4.2
at most 38, 4.3 40, 4.5 at most 42, 4.7 at most 47, 4.8 at most 46. Rewording is better for the definitional
ones (4.3's concept, 4.8's 90 percent sentence, which is *F15* and needs only
the figure). Quote, do not paraphrase, where the prose already says "in
Chapter 3's words" (4.6), or reword and drop that phrase. Re-run the
n-gram check (`ea_quotes.py` for anything newly quoted).

---

## SHOULD-FIX

### SF-1. 4.1 Unit of Work: the example's author is not named

§F rule 6 lists "the Unit of Work example is Rice's (p. 178)" among the
credits a lesson must give, and §C 4.1's Sources say so. The credit is only
in the source comment (`part_a.py` line 110); nothing a reader sees names
David Rice. 4.4 does credit Foemmel and Fowler for its example. **Fix:** add a
clause to body p4 or p5: "The pattern's worked example, with object
registration, is David Rice's, and is better read in the book."

### SF-2. 4.2 Identity Map: "Fowler allows one exception" miscounts the book

Body p4 says "Fowler allows one exception: objects that can never be
changed…". The concept and mistakes[1] say the same ("read-only objects are
the exception"). The book (pp. 184–185) says "there are a couple of
exceptions. The biggest one" is an object database used as a transactional
cache, which Fowler says is worth a look. "The other exception" is read-only
objects, and it is extended to objects updated so rarely that flushing the
process-wide map is acceptable. **Fix:** "Fowler names two exceptions: an
object database used as a transactional cache, which he thinks worth a look,
and objects that are never (or very rarely) changed, which may be held for
the whole process in a read-only map beside the session's updatable one."
The concept can keep one exception if it says "the main exception for a
plain map".

### SF-3. 4.3 Lazy Load: the reason given for the flag misreads the book's null warning

Body p6 says: "The flag, rather than a null list, is the marker, because an
order with no lines has a legitimately empty list, the case Chapter 11 warns
about when null is a legal value." An empty list is not null. A null-test
marker would load the lines and leave a non-null empty list, which works.
Chapter 11's warning (pp. 187–188) is about a field whose *loaded value* can
legally be null, so a null test would reload every time. A careful reader
will spot the non sequitur. **Fix:** "The flag is the marker because the list
is created empty and stays a real list (line 5), so there is no null to test.
It is also the shape Chapter 11 recommends wherever null is a legal loaded
value, when a null test would go back to the database on every call."

### SF-4. 4.4 Identity Field and Foreign Keys: "Fowler's own suggestion is a separate key table" overstates and leaves out the database counter

Body p4 runs auto-generated field, then GUID, then "Fowler's own suggestion
is a separate key table". The book's three choices (p. 203) are
auto-generate, GUID and rolling your own. Under auto-generate, Fowler calls a
database counter such as an Oracle sequence "perfect for our needs, but …
nonstandard". The key table is called "a better approach" than a `max()`
scan, within rolling your own. It is not his recommendation over every other
scheme. **Fix:** "A database counter, such as a sequence, avoids that
problem, and Fowler calls it perfect where you have one, but it is
nonstandard. A GUID … If you roll your own, he prefers a separate key table
to scanning for the largest key: a row per table…"

### SF-5. 4.5: the worked example's depth line names a path that is not in the tree

Worked lines 1–2: "depth: company 1, sales 2, north 3, desk 4: depth 4".
`desk` is under `support` under `it`, not under `north`. North is a leaf at
level 3. As written, the line reads as a path from root to deepest node, and
that path does not exist. **Fix:** "depth: company, it, support, desk: depth
4". After MF-1, use the new tree's deepest path.

### SF-6. 4.6 Single Table Inheritance: `SINGLE_TABLE_LOAD` drops a manager's inherited salary

In the lesson's own hierarchy, manager is under employee, which declares the
salary. 4.7's `CLASS_TABLE_FIND` selects `e.salary` for a manager. But
`SINGLE_TABLE_LOAD` line 7 builds `new Manager(id, name,
rs.getInt("reports"))` and reads `salary` only in the default Employee
branch. A manager loaded this way has no salary, which contradicts both the
hierarchy the lab counts ("a manager uses 7 of the 9 fields") and 4.7's
listing. The prose ("each branch reading the column its class adds")
matches the code, so the fault is in the code. **Fix:** at its indent, the
one-line call `return new Manager(id, name, rs.getLong("salary"),
rs.getInt("reports"));` is 81 characters, which breaks §D.4's 72-character
limit. Either split it over two lines, which moves the later line numbers
the body cites ("lines 6 to 12" becomes 6 to 13) and makes the listing 14
lines, or read `long salary = rs.getLong("salary");` once on a new line 6
beside `id` and `name` and pass `salary` to both Manager and Employee. The
second is closer to how the single table works: every row has the column.
Then change the body sentence to say what a manager reads, update the cited
line numbers, `presets.py` and §D.4, and recompile.

### SF-7. 4.7 Class and Concrete Table Inheritance: the exercise is the staff hierarchy renamed, so each answer can be read off a preset

`account, -, 3, no; saving, account, 2, yes; isa, saving, 1, yes; current,
account, 2, yes` has the same shape as `_STAFF`. Map account to person, saving
to employee, isa to manager and current to contractor: the field counts
match too (3, 2, 1 vs 2, 2). The three questions are the same as the preset
questions: load the depth-3 class, find the middle concrete class, alter the
root. So the answer, load 1, 3, 1; find 1, 3, 2; alter 1, 1, 3, is exactly
`staff-find-person`'s load and alter and `staff-find-employee`'s find, all
printed in the body. A reader can match the pattern and never apply the
rules. **Fix:** change the shape. Make `saving` abstract (`saving, account, 2,
no`), or add a second concrete class under `current`, and give find and
alter targets whose subtrees differ from the presets'. For example: abstract
saving, `isa` and `bond` under it, find `saving` → class 4, concrete 2;
alter `saving` → concrete 2. Recompute and update §C 4.7, the quiz and the
`why`.

### SF-8. 4.7: quiz 4's `why` gives a wrong reason for the absent type code

"There is no type code in a class-table schema here, since each class has its
own table." Class Table Inheritance often does use a code. Fowler's
alternative to outer joins is to "read the root table first and then use a
code to figure out what tables to read next" (p. 262), and the lesson's own
body p2 says so. The quiz answer is still right; the reason is not. **Fix:**
"…Line 7's `WHERE` picks the manager. This query needs no type code because
it already knows the class; a query for people of mixed classes might read a
code in the root table to choose its joins."

### SF-9. 4.4: the lesson's word total is misrecorded

The source comment (`part_a.py` lines 964–965) gives "Lesson total: 19 words".
"a rare stand on the side of meaninglessness" is quoted twice, in body p3 and
mistakes[0], so the total is 11 + 8 + 8 = 27. That is within 60, but §E.3
counts every quotation. **Fix:** correct the comment to 27, or reword the
mistakes item ("Fowler sides with meaningless keys") and keep 19. Either way,
PLAN §E.3's sentence on that phrase ("for a total of 19") should match.

---

## NOTE

### N-1. 4.1: `UNIT_OF_WORK` can write a GONE object again if it is marked after removal

`mark` keeps NEW and REMOVED but not GONE. So `mark(e, NEW)`, `mark(e,
REMOVED)`, `mark(e, DIRTY)` leaves DIRTY, and the commit issues an UPDATE
for a row that was never inserted. That contradicts the header comment
"GONE: never written". The lab refuses any record after a delete, and the
lesson never describes this path, so no figure is wrong. **Fix (optional):**
add `|| now == Mark.GONE` to line 7, and say "a NEW, REMOVED or GONE object
keeps its mark".

### N-2. 4.1: the closing paragraph points two ways

"A Unit of Work writes each row once, but it may still write a row before
another row it depends on. The next lesson, Identity Map, deals first with
the other half…" sets up the ordering problem and then moves away from it.
"deals first" reads as if Identity Map will solve it. **Fix:** "Ordering
those writes is lesson 4.4's. The next lesson, Identity Map, takes the other
half of the behavioral problem: loading the same row twice."

### N-3. 4.1 quiz 2 / body p5: *F14* is close to verbatim

"three database calls rather than one call with its final state" against the
book's "three calls rather than one call in its final state". It is short and
marked as the book's illustration, but MF-3's pass is a good time to reword
it ("three writes where one, of its final state, would do").

### N-4. 4.3 quiz 1: the `why` does not account for one distractor

"Lazy 7 statements, 28 rows; batches 3, 28…" treats every parent as used.
The `why`'s last sentence lists only "forget the parents' rows, forget b's
join row, or round the batches wrongly". **Fix:** add "or count every parent
as used".

### N-5. 4.3: two small hardenings

Mistakes[2] says databases "handle only three or four joins in a query
well"; the book says they are "optimized to handle up to three or four joins
per query" (p. 52). Mistakes[1] and body p4 present "different loaders for
different use cases" as a cure for ripple loading. The book offers it for
choosing the right subgraph per use case (p. 189). Its ripple-loading cure is
the lazy collection (p. 188). **Fix:** "optimized for up to three or four";
"a related remedy, from the pattern's discussion of use cases, is…".

### N-6. 4.5 quiz 1: "The other answers drop one of the empty queries"

"6, 5 and 1" drops both. **Fix:** "drop one or both of the empty queries".

### N-7. 4.5: `LOB_TEXT` line 4 does not write "the name in brackets"

Line 4 writes the opening bracket and the name; line 8 closes the bracket.
This becomes moot if MF-1 rewrites the snippet. Otherwise, write "opens a
bracket with the department's name (line 4), writes each child inside it
(lines 5 to 7), and closes it (line 8)".

### N-8. 4.7 concept: shared keys are stated as the only scheme

The concept says "The rows of one object share a key across the tables".
The book gives that as "a possible solution", with own keys plus foreign
keys into the superclass table as the alternative (p. 261). The body is
right ("can share"). **Fix:** "usually share one key value".

### N-9. 4.8: "That ends the database half of the book"

Chapters 14 onward are not all non-database. Chapter 16's offline locks
(Course 6) are database patterns, and Chapter 5 is the concurrency
narrative. **Fix:** "That ends the book's object-relational patterns, Chapters
10 to 13. The next course…"

### N-10. Worked lines use a hyphen-minus for subtraction

"duplicates: 7 - 4, which is 3" (4.2) and "empty in its row: 9 - 7, so 2"
(4.6). The quiz `why`s use U+2212 ("7 − 4"). The read-out passes either way.
Use U+2212 in the worked lines for consistency with §D.0's number format.

---

## Teaching, overall

The course does what §C asks. Each lab count models its situation honestly,
and each body says what the count leaves out: row width in 4.3, deferral in
4.4, compression in 4.6, and key and reference problems in 4.7. No wrong quiz
answer could be defended once SF-8's reason is corrected. Every pinned figure
and every exercise answer re-derives by hand and in the browser. The voice
follows §F. Argument and tool are each named. Fowler's hedges are kept: "no
clearcut winner", "profile", "evaluate the trade-offs yourself". There is one
light remark (the "unsophisticated" aside in 4.8) and one modern aside (4.5).
No lesson ranks a platform or calls a pattern outdated. The must-fixes are
about provenance and attribution, not arithmetic: one example domain carried
over from the book (MF-1), one advice sentence given to the wrong author and
pattern (MF-2), and unmarked verbatim runs (MF-3).
