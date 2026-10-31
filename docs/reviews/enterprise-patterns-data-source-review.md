# Course review: Enterprise Application Patterns, Course 3 — Talking to the Database

Course: `enterprise-patterns-data-source`
(`content/enterprise_patterns/c3_data_source/__init__.py`, `part_a.py`, and its
block in `content/spoken/enterprise_patterns.py`), six lessons. Built to
`docs/enterprise-patterns/PLAN.md` §C Course 3, §D.5, §E, §F and §R, and
`docs/enterprise-patterns/AUTHORING.md`. Reviewed 2026-10-31.

**Method.** The book was read only through `eabook.py` and `eapage.py`, at
every page the lessons cite: pp. 46–49, 52, 58–59, 61–63, 102–103, 141–143,
148–150, 154–155, 159–162, 413–415, 418–419 and 424–427. Book text is cited
below by page and by a few words at most. Every quotation went through
`ea_quotes.py`. Every preset and exercise was worked by hand, then read off
the rendered page in Playwright. Every snippet was compiled. A script also
compared every lesson string, outside its quotations, with the book in runs
of six words or more, to find unquoted copying. No course file was edited.

Labels: **MUST-FIX** means a breach of the copyright rules or of PLAN, or a
claim about the book that is wrong. **SHOULD-FIX** means a claim stated
stronger or looser than the book, a page that says something untrue about
itself, or a lab that teaches the wrong thing. **NOTE** is a smaller point.

## Gates

- **Preview.** `preview_subject.py enterprise_patterns --course enterprise-patterns-data-source`
  rendered 7 pages. labcheck: 6 pages executed, 6 with pinned figures,
  0 failing. Result **OK**.
- **`labcheck.js --observe`.** Every tile of every preset matches the body
  prose, the worked lines, §C and my own count:
  - 3.1: `4: admin, cart, checkout, report` for both tiles, then
    `1: pricegateway` and
    `5: admin, cart, checkout, pricegateway, report`.
  - 3.2: 50 / 255 / 200 / 25 / 5 / 30 / 150, then 15, `101/5 = 20.20` and 6.
  - 3.3: 3 / 0 / 3 / 1, then 3 / 0 / 2 / 0.
  - 3.4: all four presets as §D.5 gives them.
  - 3.5: 1, 6, `lines 6–8 and lines 15–17`, then 0, 0, `none`.
  - 3.6: 25 / 3 / `125/2 = 62.50` / `37/2 = 18.50` / `4/5 = 80%` / `125/37 ≈ 3.4×`,
    then 15, `64/5 = 12.80`, `1/6 ≈ 16.7%` and `75/64 ≈ 1.2×`.

  The prose counts of tiles are also right: seven tiles in 3.2 and six in 3.6.
- **Browser (Playwright, Chromium, at 375 px and 1280 px).** No page error or
  console error, and no horizontal page scroll on any of the 7 pages. Code
  blocks scroll inside their own box and number their lines from the comment
  line, as the lab's listing does. I loaded each preset and typed in each
  exercise:
  - 3.1: `3: mailer, profile, signup` twice; redrawn, `1: membergateway` and
    `4: mailer, membergateway, profile, signup`.
  - 3.2: 30 statements, `243/2 = 121.50`, 600 rows, 34, 2 statements,
    `19/2 = 9.50`, 570 unneeded.
  - 3.3: `Member` gives 4 / 1 / 3 / 2.
  - 3.4: `2: customermapper, invoicemapper` and
    `3: customermapper, invoicemapper, main`.
  - 3.5: `SHIPMENT_TWICE` gives 1, 6 and `lines 2–4 and lines 12–14`.
  - 3.6: 41 / 2 / `656/5 = 131.20` / `71/5 = 14.20` / `15/16 ≈ 93.8%` /
    `656/71 ≈ 9.2×`.

  Every result agrees with §C's **Answer** and with the quiz `why`.
- **Exercise answers.** In the rendered text, each answer appears only in its
  quiz item: in the options and the `why`. The exercise paragraphs give the
  instance and nothing more. 3.1's "Mind `profile`, which reaches the table two
  ways" is a hint, not the answer.
- **`ea_quotes.py`:** 7 quotations, all **OK** on the stated page.

  | lesson | page | words | result |
  | --- | --- | --- | --- |
  | 3.1 | p. 46 | 23 | OK |
  | 3.2 | p. 52 | 18 | OK |
  | 3.3 | p. 149 | 14 | OK |
  | 3.4 | p. 159 | 14 | OK |
  | 3.5 | p. 58 | 21 | OK |
  | 3.6 | p. 63 | 16 | OK |
  | 3.6, "guilty until proven innocent" | p. 426 | 4 | OK |

  Every lesson is within 40 words for its opening quotation and within 60 in
  all. 3.6's total is 20 words.
- **Figures.** Every book figure has its `# F` comment, on the right page:
  - F10, p. 49;
  - F11, p. 52;
  - F12, p. 58;
  - F13, p. 425;
  - F22, p. 102, which both 3.3 and 3.5 use.

  Each is called the book's illustration or the book's figure where it is
  used. The 5 ms, 0.1 ms, 2 ms and 0.5 ms timings are marked as the lesson's.
- **Snippets.** All ten constants are character-identical to `presets.S`, and
  the line counts match §C (16, 18, 19, 15, 18, 17, 18, 18, 18, 13). No line
  is longer than 72 characters. All ten compile with `javac --release 8`,
  given stub domain types (`Customer`, `CustomerData`, `Shipment`, `Line`).
  Each cckit preset uses the same constant as its code block. The one place
  that cites line numbers is 3.5 (lines 3–5, 6–8, 12–14, 15–17; and 2–4 and
  12–14 in the exercise), and every one is right.
- **Read-out.** `speechcheck.py` gives `enterprise-patterns 0 unresolved`.
  The course's spoken block is headed `# Talking to the Database`, and covers
  the hyphenated table names, the exercise records, `SELECT *` and the key and
  worked lines with `·` and "ms".
- **Structure (§E.1).** Each lesson has 13 to 15 body blocks, 3 concepts,
  4 steps, 3 mistakes and 4 quiz items. Every last `p` names the next lesson
  by title. The last step of each lesson is §C's **Own:** line.
- **Attribution (§F rule 6).** 3.6 names Foemmel and Fowler for the Registry
  example (p. 427 confirmed). The course uses no other contributor's pattern.
- **§R's cckit fixes.**
  - 3.1 pins only `dgDirect`, and the panel and body call `dgAffected` an
    upper bound.
  - 3.3 pins only `coRoutines`, and the body says the reader does the
    sorting.
  - 3.5 is now double mapping, `TWO_SOURCES` against `TWO_STEP`, and its body
    explains the step numbering.

  All three fixes hold in the lab. Two weaknesses remain in how the lessons
  use them: in 3.3's exercise and quiz (SF-5), and in 3.4's reading of the
  ripple tile that 3.1 fixed (SF-4).

The arithmetic, the tiles, the snippets and the attributions are clean. The
findings are of two kinds. First, wording copied from the book without
quotation marks, which is serious in two places. Second, a few claims, about
the book or about the course itself, stated more strongly than the source
supports.

## MUST-FIX

### MF-1 — Gateways (3.1): F10 copied from the book, unquoted

- **What.** The body paragraph "The section closes on what all this costs"
  reproduces 18 consecutive words of Architectural Patterns word for word,
  without quotation marks. The run starts at "anecdotal observations put" and
  ends at "programming effort". It then follows the rest of the same sentence
  closely ("a cost that goes on through maintenance"). Without quotation
  marks or a page comment for a quotation, the book's sentence is presented
  as the lesson's own; this is the "stretch of the text" that §E.3 and
  AUTHORING forbid. The same paragraph also
  adds a gloss the book does not give: "a figure from projects he has seen".
  The book says only "anecdotal observations", and does not say whose.
- **Evidence.** PDF p. 49. My n-gram check gives a 21-token match. The
  sentence is the one that sets out F10 in §S.2.
- **Fix.** Restate the figure in the lesson's own words and drop the gloss.
  For example: "Weighing object databases, which need no mapping, Fowler puts
  the cost of the alternative at about a third of all programming effort,
  carried on into maintenance. He says that this rests on anecdote, and that
  he knows of no controlled test. Treat it as an estimate, which your own
  records can check." Keep the `# F10` comment. Then re-run the n-gram check
  until no run of six or more words remains. The other route is to quote the
  18 words exactly, with the page in a comment: that makes 41 words of
  quotation, within the 60. The rewrite is better, because the lesson
  already opens on a quotation.

### MF-2 — Active Record (3.3): When to Use It copied from the book, unquoted

- **What.** The body paragraph that begins "When to use it:" opens with a
  14-word run copied from the book: the description of the domain logic
  Active Record suits, with its list of creates, reads, updates and deletes.
  The rest of the paragraph follows the section sentence by sentence:
  - the derivations and validations on one record;
  - the "primary advantage" of simplicity;
  - the "primary problem", which it states almost word for word;
  - adding relationships "piecemeal gets messy";
  - the coupling of "the object design to the database design", an 8-word
    run.

  Quiz item 3's correct option repeats the "primary problem" sentence almost
  word for word.
- **Evidence.** PDF p. 155, When to Use It. My n-gram check gives runs of 15
  and 8 tokens.
- **Fix.** Rewrite the paragraph in the lesson's own words and order.
  For example: "Chapter 10 recommends Active Record for logic that stays
  close to one record: the ordinary create, read, update and delete work, and
  rules computed from a single row. It is simple. It stops working once the
  classes and tables part ways, because collections, inheritance and links
  between objects do not fit it, and that is when a Data Mapper is needed.
  Because it ties the class design to the table design, neither can be
  refactored without the other." Reword quiz 3's correct option in the same
  way, for example "It fits only a schema shaped like the classes".

## SHOULD-FIX

### SF-1 — Gateways (3.1): "Its chief benefit" overstates Gateway's When to Use It

- **What.** The body says that Gateway's "chief benefit" is that a change of
  resource alters only the gateway. The book calls this "a clear benefit". It
  says this flexibility is often what the debate focuses on. It then tells
  the reader not to forget simplicity and testability, which hold even if the
  resource never changes. The paragraph also copies a 9-word run of the
  sentence about the change not rippling through the system.
- **Evidence.** PDF p. 414.
- **Fix.** Write: "One clear benefit, the pattern says, is that swapping the
  resource means changing only the gateway, and nothing beyond it. It adds
  that the simplicity and the place for a test stand-in are worth having even
  if the resource never changes."

### SF-2 — Course `not_covered`: stored procedures are not named in any lesson

- **What.** The first `not_covered` item says Fowler names stored procedures
  where they bear on a pattern, "and the lessons name them there". No lesson
  mentions stored procedures; a search of `part_a.py` finds none. The page
  says something untrue about itself, and PLAN §C's `not_covered` wording
  assumes that the naming happens.
- **Evidence.** Architectural Patterns, p. 47: a set of stored procedures can
  be thought of as a Table Data Gateway, and Fowler would still wrap them in
  an in-memory one. Table Data Gateway, p. 142, says stored procedures
  themselves are often organized as Table Data Gateways.
- **Fix.** Add one sentence to 3.1's Table Data Gateway paragraph: "Where a
  team does all its access through stored procedures, Fowler treats the set
  of procedures for a table as its Table Data Gateway, and would still wrap
  the calls in an in-memory one." Alternatively, change the `not_covered`
  item to "…and the lessons do not teach them."

### SF-3 — Course `not_covered`: "the four calls the snippets use"

- **What.** The course says it covers no JDBC "beyond the four calls the
  snippets use". The snippets use eleven JDBC methods:
  - `prepareStatement`;
  - `setString`, `setLong` and `setInt`;
  - `executeQuery`, `next`, `getLong` and `getString`;
  - `executeUpdate`, `addBatch` and `executeBatch`.

  They also use the DOM's `getAttribute` and `setAttribute`.
- **Fix.** Write "JDBC beyond the few calls the snippets use, each explained
  where it first appears". 3.1 explains `prepareStatement`, `setString`,
  `executeQuery` and `next`, and 3.6 explains `addBatch` and `executeBatch`,
  so this wording is true.

### SF-4 — Data Mapper (3.4): "Reached in all" read as certain, against 3.1's upper bound

- **What.** 3.1 teaches that the second tile is an upper bound: what a change
  reaches only if it passes through each interface. 3.4 reads the same tile
  as a fact. The `active-record` paragraph says the database library's change
  "reaches the screen and the report through the domain class". The
  `mapper-domain-change` paragraph and the first mistake count "two more
  classes" reached as a definite cost. A reader who took 3.1's lesson to
  heart will find the two lessons contradict each other. The comparison
  itself is fair, because both designs are measured with the same rule.
- **Fix.** Add one clause the first time the tile is read in 3.4: "in all,
  at most: as in the first lesson, this is what the change reaches if each
  class's interface passes it on". Use "can reach" in place of "reaches" in
  the `active-record` sentence, and "can reach two more classes" in the first
  mistake. No figure changes.

### SF-5 — Active Record (3.3): the exercise and quiz 1 test field counts, not the pattern

- **What.** §R SF-18 narrowed this lab to `coRoutines`, because the field
  tiles are Code Complete's encapsulation counts, not Fowler's distinction.
  The exercise still asks for "the fields, the public fields that are not
  final and the routines". Quiz 1's distractors differ by the field count and
  by whether `joined` (public, final) counts as public data. Only one
  distractor differs by the pattern. A reader who sorts the routines
  correctly can still miss the item over `final`, which the lesson never
  teaches. `MEMBER_RECORD`'s `public final String joined = "2024-01-01"`
  exists only to set that trap. It also contradicts the lesson's own account
  of the pattern, one field for each column read from the row, because
  `insert` never writes `joined` and `find` never reads it. §C's **Answer**
  prescribes the field counts, so this needs a §C correction.
- **Fix.** Ask for the routines and their sorting only. Rewrite quiz 1's
  options so that they differ by the sorting:
  - "3 routines; `find` and `insert` database access, `level` domain logic;
    an Active Record";
  - "3 routines; `level` only converts a type; a Row Data Gateway";
  - "2 routines, `find` and `insert`; a Row Data Gateway";
  - "4 routines, counting the field initialiser; an Active Record".

  The `why` can still mention the lab's other tiles. If the snippet changes,
  drop `joined` from `MEMBER_RECORD` (and from `presets.S`), and correct §C
  3.3's **Answer**.

### SF-6 — Close paraphrase and unquoted runs, below MF-1 and MF-2

None of these runs is long on its own. Each reproduces a sentence of the
book, or one of its lists, nearly word for word, without quotation marks.
Taken together, several lessons follow the book's sentences in order more
closely than §E.3 ("the argument in its own words") allows. Each needs a
reword, not a quotation:

- **3.1, Table Data Gateway paragraph and quiz 2's `why`.** "bad form,
  because it defeats compile-time checking", with "is not a very explicit
  interface" (p. 141, 9 words). Keep "bad form", because that is the fact
  quiz 2 turns on; give the reason in other words ("it gives up type checks
  at compile time, and a mistyped key is found only when it fails").
- **3.1, concept "Table Data Gateway".** This tracks the pattern's opening
  sentences and its How It Works (p. 141): it holds the selects, inserts,
  updates and deletes, other code calls it "for all" access, it is "usually
  stateless", and it "pushes data back and forth". Rewrite it as a definition
  in the lesson's own words.
- **3.3, body paragraph 2.** This restates Active Record's bulleted list of
  typical methods item by item, in the book's order. The last item,
  "implement some pieces of business logic", is copied verbatim (pp.
  154–155). §E.3 forbids reproducing the book's lists in this way. Summarise
  instead: "The pattern's own list of what such a class does runs from
  building itself out of a result row, through finders, inserts, updates and
  accessors, to one last item: some of the business logic."
- **3.3, body paragraph 3.** "like most in software, is not terribly sharp,
  but useful" is the book's sentence on p. 155 with two words dropped. Either
  quote it exactly (it is about 17 words, which keeps the lesson under 60) or
  write "a line he admits is blurred, and still worth drawing".
- **3.3, concept 1 and the third mistake.** "the essence of an Active Record
  is a Domain Model whose classes match…" (p. 154, a 10-word run). Write
  "Chapter 10 describes an Active Record as, at heart, a Domain Model shaped
  like its tables".
- **3.4, body paragraph on tools.** "makes a big dent" with "using and tuning
  it is still a small but real piece of work". This is p. 49's last sentence
  with one word changed. Either quote the four words "It makes a big dent"
  (3.4 has 14 words of quotation, so it has room), or write "a tool removes
  much of the work, but choosing and tuning it is still a job of its own".
- **3.5, body paragraph 3.** "crippling performance problems that take too
  much refactoring to fix" (p. 58, an 11-word run). "build up the database
  with each iteration … of no more than six weeks … preferably fewer" follows
  the next sentence of p. 58 in order. The paragraph after it, "When the
  schema is already there…", follows that one in the same way. Write, for
  example: "…is highly risky, he says: by then the design may be too slow in
  ways that would take more rework than anyone can afford. Grow the database
  with the model instead, in iterations of six weeks at most, the book's
  figure."
- **3.6, quiz 2's `why`.** "not needed 90 percent of the time is what leads"
  (p. 425, 10 words). Write "The book's figure: when the parameter would sit
  unused in nine calls out of ten, he takes a Registry instead."

After the rewrites, re-run a six-word shingle comparison of each lesson's
strings, quotations excluded, against the book. A run of up to five words is
acceptable for a pattern name or a technical phrase ("Down to the Data
Source Layer", "behind an interface that looks like").

## NOTE

### N-1 — Course `summary`, docstring and `not_covered`: "first half" and "second half" of Chapter 3

The course says it reads "Chapter 3's first half", and that the structural
and behavioral patterns are "the rest of Chapter 3's second half". In the
book, Building the Mapping (p. 58) and Database Connections and Some
Miscellaneous Points (pp. 61–63) come after The Behavioral Problem (p. 50),
Structural Mapping Patterns (p. 53) and Inheritance (p. 55), which Course 4
reads. The wording comes from PLAN §C, and the rendered page would mislead a
reader who looks for the halves in their copy. Write "the sections of Chapter
3 on the architectural patterns, reading data, building the mapping and
connections", and in `not_covered`, "the rest of Chapter 3 (the behavioral
problem, structural mapping, inheritance and metadata) is the next course's".

### N-2 — Row Data Gateway and Reading in Data (3.2): the club example is the book's

The body ("Add a member to a club in memory…") and quiz 3 retell Reading in
Data's own illustration of finders working on database state (p. 52: people
added to a club). This is a narrative example, not a listing, and the rule
it illustrates is fair to state. But §E.3 keeps the book's examples in the
book, and §S.2 does not register this one. Use the lesson's own domain: "Add
a line to an order in memory, then run a finder for the order's lines, and
the new line is not among them."

### N-3 — Row Data Gateway and Reading in Data (3.2): whose point is "a rule about latency"

"That is Fowler's point about measuring, made by the lab: the rule of thumb
is a rule about latency" can be read as attributing the latency claim to
Fowler. His point is to profile with your own database and data (p. 52), and
his rule of thumb carries a caveat of its own, about locking too many rows.
The reading in terms of latency belongs to the lab. Write: "Fowler's advice
is to measure, and the lab shows why: on these figures, the rule of thumb
holds only where a statement's wait is large against a row's cost." Quiz 4's
`why` can keep "which is why".

### N-4 — Row Data Gateway and Reading in Data (3.2): "ten times less"

The first mistake says "25 ms, ten times less". 255/25 is 10.2, and "ten
times less" reads awkwardly. Write "about a tenth of the time". The body's
"ten times as long" is fine as an approximation; "about ten times" would be
exact.

### N-5 — Active Record (3.3): `MEMBER_RECORD`'s `find` shows no SQL

The body says "each routine that talks to the database shows its SQL as a
comment". `Member.find` has no such comment, so the reader has to classify it
by its name alone. Add `// SELECT email, points FROM member WHERE id = ?`,
which makes 19 lines (and update `presets.S`), or fold this into SF-5's
rewrite.

### N-6 — Data Mapper (3.4): the `note` refers to frameworks the lesson does not name

The `note` says "the frameworks the late paragraph names are the lesson's
account". The paragraph names no framework. Write "the late paragraph's
account of the frameworks since 2002 is the lesson's, not the book's." The
modern aside itself meets §F.3: there is one, in the lesson §F.3 names, it is
framed as a continuation of the chapter, and it is not `mistakes[0]`.

### N-7 — Database Connections (3.6): `executeBatch` and round trips

"`executeBatch` then sends every queued statement in one call" is true of the
JDBC call. Whether the driver sends the batch in one network round trip
depends on the driver and its settings, and the lab equates a batch with a
round trip. The book says how batching is done "varies with the platform"
(p. 63), and the lesson's Own step asks the reader to check their own
driver. Add: "…in one call to the driver, which a batching driver sends as
one round trip; the last step asks you to check yours."

### N-8 — The snippets never close what they open

`PRICE_GATEWAY`, `ORDER_ROW`, `ACCOUNT_MAPPER` and `SAVE_LINES_BATCH` never
close their `PreparedStatement` or `ResultSet`. `ACCOUNT_MAPPER` also ignores
the result of `next()`, so a missing row ends in an `SQLException` instead of
a null. This is reasonable at 13 to 18 lines, but 3.6 tells the reader to
close resources as soon as they are done. One clause in 3.6's snippet
paragraph would cover it: "like every snippet in the course, it leaves out
the try-with-resources that would close the statement".

### N-9 — Gateways (3.1): the `note` names two limits

§F says the `note` names the lesson's one limit. 3.1's note names two: the
lab's upper bound and the anecdotal F10. The second is already in the body.
Drop it from the note, or keep it, since this is minor.

### N-10 — Checked and clean

These checks found no problem:
- Fowler's reasons for separating SQL (p. 46).
- Gateway against Mapper: Gateway is the commoner choice, and a Mapper is
  hard to invoke (p. 418).
- What a Table Data Gateway returns, and Fowler's reluctance to return domain
  objects (pp. 141–142).
- The Alur et al. Data Access Object (p. 142).
- Static finders and Service Stub (p. 52).
- The three representations and "one too many" (p. 149).
- The crux that tells a Row Data Gateway from an Active Record (p. 149).
- Row Data Gateway turning into an Active Record (p. 150).
- Data Mapper's How It Works, Separated Interface and When to Use It,
  including "I wouldn't choose Data Mapper without Domain Model"
  (pp. 159–162).
- Chapter 8's pairings and its strong advice to buy a tool (pp. 102–103).
- The three situations, double mapping, and the order of the two steps
  (pp. 58–59).
- Connections, pooling, tying a connection to a transaction, the garbage
  collector as a backup, and closing on every command rolling a transaction
  back (pp. 61–62).
- The three miscellaneous points (p. 63).
- Registry's scopes, its static interface without static data, the last
  resort, 90 percent, and guilty until proven innocent (pp. 424–426).
- The pattern and chapter names, and the module labels.
- The read-along framing: each lesson says whether it reads an argument or a
  tool.

No quiz distractor survived my attempt to argue for it. The closest was 3.3
quiz 1's "Row Data Gateway" option: one could argue that `level()` is mere
type conversion. But When to Use It lists derivations as Active Record's
business, so the option stays wrong; SF-5 would make it the item's real test.

## Counts

MUST-FIX 2, SHOULD-FIX 6, NOTE 10.
