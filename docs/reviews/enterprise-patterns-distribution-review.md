# Review: Enterprise Application Patterns, Course 7 — Distribution and Putting It Together

Course: `enterprise-patterns-distribution` (`content/enterprise_patterns/c7_distribution/__init__.py`,
`part_a.py`, and the `# Distribution and Putting It Together` block of
`content/spoken/enterprise_patterns.py`). Five lessons: Chapter 7, Chapter 15's Remote Facade and
Data Transfer Object, Chapter 8 with Other Layering Schemes, and Chapter 18's Plugin and Service
Stub. Built to `docs/enterprise-patterns/PLAN.md` §C Course 7, §E, §F, §R and
`docs/enterprise-patterns/AUTHORING.md`. Reviewed 2026-10-31 against the private extraction of the
operator's copy, reading every section each lesson cites (PDF pp. 92–109, 352–355, 363–366, 441–446,
and p. 90 for *F20*) with `eapage.py` / `eabook.py`.

**Scope.** This reviewer wrote only this file. Nothing in the course, the spoken file or PLAN was
changed. Every finding is a recommendation, with the fix where it is mechanical. No book text
beyond identifying phrases of a few words appears below.

## Gates

- **Preview:** `python3 scripts/preview_subject.py enterprise_patterns --course enterprise-patterns-distribution --out …/scratchpad/rev7/out`
  → 6 pages; labcheck 5 executed, 5 with pinned figures, 0 failing; **OK**.
- **`labcheck.js --observe`**, every preset, against the body prose, the worked lines, §C and a
  hand count. All agree:
  - 7.1 `by-class` 75 / 75 / 75,000 / "1 = 100%" / 75 / "1,000×"; `one-process` 75 / 0 / 75 /
    "0 = 0%" / 75 / "1×".
  - 7.2 `move-house` 11 / 2 / "451/2 = 225.50" / "91/2 = 45.50" / "40/41 ≈ 97.6%" /
    "451/91 ≈ 5.0×"; `on-a-fast-network` "33/2 = 16.50" / "15/2 = 7.50" / "2/3 ≈ 66.7%" /
    "11/5 ≈ 2.2×".
  - 7.3 `order-screen` 5 / "51,033/500 ≈ 102.07" / 6,066 / "13,033/500 ≈ 26.07" / 4,000 /
    80,000; `as-xml` "53,099/500 ≈ 106.20" / 18,198 / "19,099/500 ≈ 38.20" / 12,000 / 80,000.
  - 7.4 `web-and-database` 7 / 14,067 / "14,067/74 ≈ 190.1×"; `service-split-off` 9 / 18,065;
    `domain-split-off` 47 / 94,027.
  - 7.5 `real-service` "1: postoffice" / "3: postoffice, signup, signuptest"; `plugin-and-stub`
    "1: postofficecheck" / "2: main, postofficecheck".
- **Browser** (Playwright, chromium, `file://`, 375 px and 1280 px). No console errors. No
  horizontal page scroll at 375 px (`scrollWidth` = 375 on every page; code blocks and the lab
  tables scroll inside their own boxes). Each preset loaded from the menu. Each exercise typed as
  the body states it:
  - 7.1 → 44 / 20 / 16,048 / "1,000/1,003 ≈ 99.7%" / 88 / "2,006/11 ≈ 182.4×". 7.1 quiz 2's
    `customer=orders` → 65 / 65,010.
  - 7.2 → 20 / 3 / 320 / 65 / "15/16 ≈ 93.8%" / "64/13 ≈ 4.9×".
  - 7.3 → 2 / "4,007/200 ≈ 20.04" / 69,070 / "8,907/200 ≈ 44.54" / 69,000 / 20,000. With only
    the two needed fields → "2,007/200 ≈ 10.04".
  - 7.4 → 57 / 3 / 150,054 / "50,018/19 ≈ 2,632.5×". With `app, facade, 1` → 50,054.
  - 7.5 → "1: ratesfeed" / "3: invoice, invoicetest, ratesfeed". The redesign's records, as the
    `why` gives them → "1: httprates" / "2: httprates, main". 7.5 quiz 4 (`signup, main` added) →
    4, by hand.

  Every figure in a quiz `why` matches the page. Every exercise answer appears only in its quiz
  `why`; I grepped `part_a.py` for each answer figure. Every tile is explained in prose somewhere
  in the course (rrShare and rrOneNode in 7.1).
- **Code.** All five snippets equal their `presets.py` constants. Each is ≤ 20 lines of ≤ 72
  characters, and each compiles with `javac`, given minimal stand-in types. Every line number the
  prose cites is right: 7.1 lines 3–5; 7.2 lines 9–15; 7.3 lines 3–7; 7.4 lines 4, 5, 6, 7–8, 9;
  7.5 lines 2–4, 5–9, 12–20.
- **Quotations**, `ea_quotes.py`: 7 quotations, all **OK**, each on the stated page.
  - 7.1: p. 95 (15 words) and p. 97 "fight like a cornered rat" (5): 20 words.
  - 7.2: p. 355 (13) and p. 354 "Remote Facade has no domain logic." (6): 19 words.
  - 7.3: p. 363 (26, the book's "its" kept as printed).
  - 7.4: p. 100 (17).
  - 7.5: p. 446 (18, credited to David Rice).

  Each lesson is within the 40-word opening limit and the 60-word lesson limit. Each is recorded in
  the comment beside the dict.
- **Attribution (§F.6).** Stafford's Service Layer is credited in 7.2 and 7.4. Plugin is credited to
  Rice and Foemmel and Service Stub to Rice (7.5, course `how_to`), and 7.5's quotation is given as
  Rice's. Session Facade is credited "after Alur, Crupi and Malks", and the layering schemes to
  Brown, Kirtland, Marinescu and Nilsson, as the book cites them.
- **Copyright.** None of the book's listings, figures or tables is reproduced. Other Layering
  Schemes' tables are stated in the lesson's own sentences, which §E.3 allows. No snippet uses the
  book's example domains (album, ID generator, sales tax). The domains are customer/address,
  order screen, cart/checkout and post-office address check. An n-gram scan of every string in the
  course against the text found no unquoted run longer than 12 words. Four runs of 9–12 words are
  near-verbatim (SF-5).
- **Read-out.** `speechcheck.py` has no row for this Subject yet. I checked the read-out from the
  rendered `data-say` attributes instead. Two errors are must-fixes (MF-1, MF-2).

## Findings

Ranked: **MUST-FIX** (a wrong claim about the book, or a read-out that states the wrong thing),
**SHOULD-FIX**, **NOTE**.

### MUST-FIX

**MF-1. Remote Facade (7.2): the read-out says "is set to" for `=` and "mod" for `%`.**
- *Where:* body, the `move-house` and `on-a-fast-network` paragraphs. The renderer makes each run
  "451/2 = 225.50 ms, 40/41 ≈ 97.6%" and "33/2 = 16.50 ms, 2/3 ≈ 66.7%" one code island.
- *What is wrong:* the code dialect reads them as "451 divided by 2 is set to 225.50 ms, 40
  divided by 41 is approximately 97.6 mod" (and the same for 33/2). "Mod" is modulo, so the
  listener hears the wrong operation. "Is set to" turns a result into an assignment.
- *Evidence:* the `data-say` attributes in the rendered `remote-facade/index.html`. The ratio
  islands next to them ("451/91 ≈ 5.0×") read correctly, as "over … approximately … times".
- *Fix:* break each island so that no single run holds both `=` and `%`, for example "11 round
  trips taking 225.50 ms (451/2), 97.6% of it (40/41) waiting". Or add the two runs to the course's
  `SPOKEN` block, e.g. "451 over 2, which is 225.50 milliseconds, 40 over 41, about 97.6 percent",
  and the same for 33/2 and 2/3. Then re-check the `data-say` attributes.

**MF-2. Data Transfer Object (7.3): the read-out splits grouped thousands.**
- *Where:* six runs. "51,033/500 ≈ 102.07 ms" and "13,033/500 ≈ 26.07 ms" appear in the
  `order-screen` paragraph and again in `mistakes[0]`. "53,099/500 ≈ 106.20 ms" and "19,099/500 ≈
  38.20 ms" appear in the `as-xml` paragraph.
- *What is wrong:* each is read as "51, 033 divided by 500 …". The comma becomes a pause and the
  number is spoken as fifty-one, then zero-three-three, which is not the figure on the page. (Lesson
  4's "14,067/74" reads correctly as "14067 over 74".)
- *Evidence:* the `data-say` attributes in the rendered `data-transfer-object/index.html`.
- *Fix:* add the four runs to the course's `SPOKEN` block, e.g. "51,033/500 ≈ 102.07 ms" →
  "51033 over 500, about 102.07 milliseconds". Or write the prose as "about 102.07 ms
  (51,033/500)" and confirm that the island then reads cleanly.

### SHOULD-FIX

**SF-1. Data Transfer Object (7.3): "no behaviour" is stronger than the book.**
- *Where:* the claim appears four times:
  - the `one_line` ("An object with no behaviour …");
  - concept 1 ("fields, getters and setters, no behaviour");
  - `mistakes[1]` ("a transfer object has no behaviour");
  - 7.2 quiz 2's `why`.
- *What is wrong:* Serializing the Data Transfer Object says that, besides its accessors, the DTO
  is usually responsible for serializing itself (PDF p. 364). The Remote Facade example says the
  same of its DTOs (p. 356). The book's point is that a DTO has no *domain* behaviour, not no
  behaviour at all.
- *Fix:* write "no domain behaviour" in each place. In concept 1, add "beyond its accessors and,
  usually, its own serialization".

**SF-2. Plugin and Service Stub (7.5): the concept says a new configuration needs no rebuild, and
the snippet needs one.**
- *Where:* concept 2 ("so that a new configuration needs no rebuild"); the snippet paragraph;
  `mistakes[1]`.
- *What is wrong:* Plugin's opening problem (p. 441) is that a new deployment configuration means
  editing conditionals, rebuilding and redeploying. How It Works says the linking must happen at
  run time "so that reconfiguration won't require a rebuild" (p. 441). The book's fallback without
  reflection (p. 442) keeps the linking rules in a text file and uses a conditional only to map
  each configured name to a class.
- `ADDRESS_STUB`'s `switch` puts the choice of implementation for each environment in compiled
  code. A new environment (a staging setup that uses the stub, say) is a code change and a rebuild.
  The snippet solves the scattering problem but not the rebuild problem. A reader who compares
  concept 2 with lines 12–20 will find the contradiction.
- *Fix:* the smallest fix is one sentence in the snippet paragraph or in `mistakes[1]`: the
  `switch` gives one place to choose, but a new environment still means a rebuild, which a
  configuration file read at startup, or reflection, removes. The fuller fix, in `presets.py`, is to
  switch on an implementation name read from configuration (`case "stub"`, `case "postoffice"`), so
  that the environment's choice lives outside the code, as the p. 442 fallback does.

**SF-3. Putting It All Together (7.4): "the two boundaries Chapter 7 says you cannot avoid"
hardens a hedge.**
- *Where:*
  - the body's `web-and-database` paragraph;
  - the worked title ("The two boundaries you cannot avoid");
  - the `standard` and course outcome 4 ("say which boundaries Chapter 7 says you cannot avoid");
  - step 2 ("the nodes you cannot avoid first, the client and the database").
- *What is wrong:* Where You Have to Distribute (p. 97) says you will not eliminate all the
  boundaries, but not that any particular one is unavoidable. It says outright that you do not have
  to separate the application server from the database: you can run everything in the database
  process, though that is often impractical. It lists the web/application-server split and vendor
  packages alongside. §F.2 asks for Fowler's hedges to be kept. 7.1's own body states this one
  correctly ("unless everything runs inside the database").
- *Fix:* "the two boundaries Chapter 7 expects most systems to keep, client and server, and
  application and database" (the standard and outcome likewise: "say which boundaries Chapter 7
  says you will usually have to keep"). Retitle the worked example "The two boundaries most systems
  keep".

**SF-4. Remote Facade (7.2): the lab's illustration is given as Fowler's point.**
- *Where:* body, `on-a-fast-network` paragraph: "even a fast network leaves two thirds of the
  fine-grained time in waiting, which is Fowler's point about processes on one machine."
- *What is wrong:* the two-thirds figure follows only from the lesson's chosen numbers (1 ms
  latency against 0.5 ms work). It is not evidence for When to Use It's claim that a call between
  processes on one box costs enough to need a coarse interface (p. 355). The preset is also labelled
  a fast *network*, not one machine. §F.4: the lesson never turns an illustration into a benchmark.
- *Fix:* "On the lesson's illustration the saving shrinks as the latency falls, but does not
  vanish. When to Use It goes further and says that even two processes on one machine pay enough
  per call to need the facade."

**SF-5. Four near-verbatim runs without quotation marks.**
- *What is wrong:* each is a single sentence closely following the book. Together they go beyond
  "in the lesson's own words" (§E.3, AUTHORING). Each lesson has room in its 60-word budget either
  to quote the run or to reword it.
  - **7.1 body, paragraph 2.** The opening design's list of remote objects follows a 10-word run of
    p. 93. The sentence on transparency and performance mirrors pp. 93–94's sentence in structure
    and words.
  - **7.1 body, "Hence the law".** The clustering sentence follows a 9-word run of p. 95. Quiz 3's
    right option repeats it.
  - **7.1 body, Interfaces for Distribution.** Fowler's attitude to XML web services is a 10-word
    run of p. 99.
  - **7.2 quiz 4 `why`.** The same-box sentence is a 12-word run of p. 355. `mistakes[2]` rewords
    the same sentence but keeps its last six words.
- *Fix:* recast each in the lesson's words. For example, for p. 99: "Fowler would reach for XML web
  services only when nothing more direct will do". For p. 355: "even two processes on one machine,
  the section says, pay enough per call to need a coarse-grained interface".

**SF-6. Data Transfer Object (7.3): the standard says "one saved round trip", and the tile counts
all of them.**
- *Where:* the `standard` ("the bytes one saved round trip would have carried"); course outcome 3
  ("what a saved round trip could have carried").
- *What is wrong:* `rrSpare` is (getter calls − 1) × latency × bandwidth. It is 80,000 bytes for
  the four trips `order-screen` saves. Step 3 and the lab paragraph say "the saved round trips". The
  exercise has only one saved trip, so it does not show the mismatch, but the preset does.
- *Fix:* "the bytes the saved round trips could have carried", in both places.

**SF-7. Remote Facade (7.2) quiz 3: the `why` muddles the answer it should settle.**
- *Where:* "With no work the speed-up is just the number of round trips saved over one".
- *What is wrong:* four round trips are saved, and 4× is a distractor. "The number of round trips
  saved over one" can be read as 4/1. The speed-up is the ratio of round trips, 5 to 1.
- *Fix:* "With no work the speed-up is the ratio of round trips, 5 to 1. 4× counts the trips saved,
  not the ratio, and work would bring the speed-up down."

**SF-8. Distribution Strategies (7.1): `class=node` is read as "class is set to node".**
- *Where:* the lab paragraph ("a list of nodes written `class=node`").
- *Fix:* a `SPOKEN` entry, "class=node" → "class equals node". Or write "pairs like `order=orders`,
  a class and its node".

### NOTE

**N-1. 7.1: a hedge dropped from the clustering sentence.** Remote and Local Interfaces says
clustering is the way to go "in most cases" (p. 95). The body ("To use several processors, Fowler
says, put all the classes in a single process …") and quiz 3's stem drop the hedge. Add "in most
cases" to the body.

**N-2. 7.1: the fifth boundary is called "rare".** For the fifth boundary the book says only that
such cases do come up, and that you should go to great lengths to avoid them (p. 97). "Rarely" (in
the body and in quiz 4's `why`) is a fair gloss, but it is the lesson's word, not the book's.

**N-3. 7.4: the three practices are hedged in the book.** Fowler asks the reader to "consider
seriously" continuous integration, test-driven development and refactoring, even if they dislike
the rest of extreme programming, and says the practices will not be a panacea (p. 100). "He
recommends three practices" loses both hedges. Write "he asks you to consider seriously three
practices … which will not be a panacea".

**N-4. 7.3: "the client" where the book says "the server".** On p. 363 the book says you don't
want the domain classes "on the server". From context this is evidently a slip for the client.
The lesson's reading ("you would not want the domain classes on the client") and quiz 2 are right.
Recorded so that a later reviewer who checks against the text does not "correct" them.

**N-5. 7.3: binary serialization is not fragile as such.** Concept 2 and the serialization
paragraph call binary forms fragile. The book's fragility is that of a *pure* or *direct* binary
serialization. It names a tolerant binary alternative, serializing through a dictionary (p. 365).
Write "a direct binary form" in concept 2.

**N-6. 7.3: `order-screen` is not quite the snippet's object.** The body calls `order-screen` "the
snippet's screen", but `OrderDto` has no `notes` field. The preset is the snippet's five fields
plus a 4,000-byte field an assembler copied without need. Write "the snippet's five fields, with a
4,000-byte `notes` field added, as if …".

**N-7. 7.2: "five local calls" undercounts the snippet.** `moveHouse` also calls `c.address()`
three times (lines 11–13), so a reader counting calls in the snippet gets eight, not five. Write
"five calls on the domain, besides fetching the address", or hoist `Address a = c.address();` in
`presets.py` (the method then runs to 8 lines, so the cited range becomes 9–16).

**N-8. 7.5 exercise: "as in the snippet's design".** The invoice and its test are said to be "as in
the snippet's design", but the snippet has no signup or test. The design meant is the preset
`plugin-and-stub`. Write "as in the preset plugin-and-stub".

**N-9. 7.5: wiring at `main` is the lesson's choice, not the book's.** The paragraph that adds
`signup, main` recommends reading the configuration once, at the edge, "as the lesson's `main`
does". That is sound and is marked as the lesson's. But the book's own Service Stub example has
the interface itself obtain its implementation from the plugin factory (p. 446). A reader who
opens the book will see the dependency the lesson warns against, made harmless by reflection. One
clause would help: "the book's examples call the factory from the interface, which reflection makes
harmless".

**N-10. §F.1, the reading mode.** 7.1, 7.2 and 7.4 say whether they read an argument or a pattern.
7.3 and 7.5, both pattern lessons, do not. A clause in each first paragraph would do, e.g. "a
pattern, read as a tool".

**N-11. Narrative figures not in §S.2.** "Two or three times a year" (p. 93), "an order or two"
more for another machine (p. 95) and "perhaps one [facade] for a moderate application" (p. 353)
are the book's figures but are not registered. They are narrative, not data, and each is stated
at the book's strength. If §S.2's rule is to hold strictly, register them, or reword them as
"several times a year" and "a single facade even for a moderate application". The last is the
book's claim, not a figure.

**N-12. 7.5: the key-generator illustration.** The Plugin paragraph describes the pattern's
motivation with the book's own illustration, an in-memory counter for tests and a database
sequence in production (p. 441). It is prose about the book's argument, not code, so it does not
break §E.3. But the course's `not_covered` lists "the identity generator of Plugin" as staying in
the book. A different example would avoid the apparent contradiction, e.g. a file store on disk for
tests and an object store in production.

**N-13. 7.4: the kit's tile label says "class".** `rrOneNode` reads "Time with every class on one
node (µs)" on a lab of layers. This is a kit label and cannot be changed in content. The
`panel_intro` could add "(here, every layer)".

**N-14. 7.4 quiz 1: "about 50,054 µs" is exact.** The `why` says one facade call would take
"about 50,054 µs". The lab gives exactly 50,054. Drop "about", or say "about 50 ms".

**N-15. Read-out: "ms" is read inconsistently.** 7.2's worked lines are read "milliseconds" in
their first two lines (from the `SPOKEN` entries) and "ms" as letters in the next three (the speed-up line has no unit). 7.3's
worked lines and every prose island say "ms". The course's `SPOKEN` comment lists µs but not ms. Add
entries for the remaining 7.2 and 7.3 worked lines, so that each lesson reads the unit one way.

## Counts

MUST-FIX 2 · SHOULD-FIX 8 · NOTE 15.
