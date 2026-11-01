# Review (accuracy and teaching): Domain-Driven Design, Course 3 — The Life Cycle of a Domain Object

Course: `ddd-life-cycle` (`content/domain_driven_design/c3_life_cycle/`, `__init__.py`,
`part_a.py`, `part_b.py`), six lessons. Built to `docs/domain-driven-design/PLAN.md` §C
Course 3, §D, §E, §F and `docs/domain-driven-design/AUTHORING.md`. Reviewed 2026-11-01
against the private extraction of the operator's copy (PDF page = the tools' page), reading
PDF pp. 70–114 (all of Chapters 6 and 7) behind every sentence that says what Evans
argues, with `page.py` and `book.py`. I did not read the file whole and did not read `site/`.

**Scope.** I wrote only this file; each finding is a recommendation.

## Gates

- **Preview:** `python3 scripts/preview_subject.py domain_driven_design --course ddd-life-cycle --out …/scratchpad/rev/ddd-life-cycle`
  rendered 7 pages; labcheck 6 executed, 6 with pinned figures, 0 failing; **OK**.
- **`quotes.py`: 6 quotations, all OK.** 3.1 p. 72 (18 words), 3.2 p. 72 (15), 3.3 p. 80
  (23), 3.4 p. 86 (20), 3.5 p. 96 (23), 3.6 p. 108 (26). One quotation a lesson, so every
  lesson is under 40 and under 60. Each dict comment gives the PDF page.
- **`overlap.py <course dir> 8`:** 8 runs. Six are the counted quotations. Two (p. 70,
  8 words) are the chapter title "The Life Cycle of a Domain Object" followed by "the".
  None is anything else.
- **Browser (Playwright, chromium, `file://`).** All six lessons at 375 px and 1280 px:
  scrollWidth equals clientWidth everywhere, with no page errors and no console errors.
  I loaded all 16 presets at 1280 px. Every tile matches the body prose, the worked
  lines and the pinned `expect`, for example `object-locks` 14 over 12, `aggregate-lock`
  12, `fleet` b101 and b102, `first-draft` 5 / 2, and `two-packagings` 5/14 against 9/14.
- **Exercises, typed into the lab.** Each agrees with its quiz `why` and with my own count:
  library 5 / 2, deleting Member removes 3 and leaves 2 dangling (Loan → Member, Desk → Card);
  guided walk: object locks give kim, lee / 16, broken, and the aggregate lock gives kim / 15,
  holds; `request`: 2 of 4 true, clause 2 germination first, false germination and moisture;
  b201 selected, b202 fails on status, b203 on km; bakery 4 / 1 (OrderLine → Tray),
  removes Order and OrderLine, 1 dangling (Dispatch → Order); seed bank 2/8 = 1/4 and 6/8 = 3/4.
- **Hand counts.** I re-derived every figure by hand, including all 14 and 16
  dependencies. All are right. No lab uses a book domain: clinic, cookery class, seed bank, bike-share, theatre box
  office, library, guided walk, bakery. No book code, diagram or dialogue is reproduced.
  Cross-references (Pessimistic and Coarse-Grained Locks; Metadata Mapping, Query Object
  and Repository; Associations; Modules and Modeling Paradigms; Breakthrough) all exist.

## MUST-FIX

1. **`part_a.py:722` — the quiz `why` names the wrong options.** The question is lesson
   3.2, item 4. The correct answer is the third option. The two that reverse Evans's facts
   are the first ("Orders change less often than parts", which reverses fact 2) and the
   second ("A price change must reach every order at once", which reverses fact 3). The
   book's three facts are on p. 77. Replace with: "The first and second options reverse two
   of them; the last contradicts the first."

2. **`part_a.py:834–838` — the Factories boxed statement is paraphrased too closely.**
   The boxed statement is on p. 80. The lesson keeps its three sentences in order. "does
   not make the client name the concrete classes" is a 7-word near-run of the box (two
   words swapped), and "with its invariants enforced" mirrors its last clause. Replace the
   sentence after "Stated as the reader would apply it, the pattern says:" with: "when
   building an object or a whole aggregate is complicated, or would expose its insides,
   make building it the job of a separate element; let clients ask that element for what
   they want in their own terms, never naming the classes it puts together; and have it
   hand back each aggregate complete, its rules already checked."

3. **`part_a.py:1146–1152` — the Repositories boxed statement is paraphrased too
   closely.** The boxed statement is on p. 89. The lesson follows it clause by clause and
   has several near-runs:
   - "for each type that really needs global access";
   - "collection in memory of every object of that type";
   - "behind a well-known interface";
   - "methods to add and remove" (an exact 5-word run);
   - "aggregate roots that need direct access".

   Replace from "for each type…" to "…need direct access." with: "when clients must look up
   objects of some type by their attributes, give that type one object that clients can
   treat as if it simply held every such object in memory. Clients put objects in and take
   them out through it, and ask it for the ones matching a condition, getting whole objects
   back; it alone talks to the store. Only aggregate roots get one, and only those that
   clients cannot reach by following references."

4. **`part_b.py:153–154` — the book's example is misdescribed.** The lesson says each
   entity has "an identity scheme found by asking the experts". In the book (p. 99) only the
   Customer ID and the Handling Event key come from a domain expert. The cargo's tracking ID
   is industry practice, the Carrier Movement code comes from a shipping schedule, and
   Location gets an arbitrary internal identifier. Replace with: "each with its own
   identity scheme, two of them (the customer's and the handling event's) settled by
   asking a domain expert;".

## SHOULD-FIX

1. **`part_a.py:795` — Factory concept.** "A program element whose responsibility is" is
   a 6-word exact run of the book's defining sentence (p. 80). Use instead: "An element
   of the design whose one job is building other objects."
2. **`part_a.py:186–188`, `255–257` — the Aggregate definition and two rules are close to
   the book.** They track p. 72's definition and two of p. 74's rules:
   - "associated objects that … treat(s) as one unit";
   - "removes everything inside the boundary at once";
   - "invariant of the whole aggregate".

   Suggested replacements:
   - Concept: "Objects bound together so that any change to their data is made to the
     group as a whole. It has a root and a boundary, and its rules are kept for the group,
     not object by object."
   - Rule 5: "Deleting the root takes everything inside the boundary with it."
   - Rule 6: "After any committed change inside, all of the aggregate's rules are true."
3. **`part_a.py:1097` — key line "the client leaves commit to itself" does not parse.**
   Use "the client, not it, commits" (Implementing a Repository, p. 92).
4. **`part_b.py:529–532` — a claim the lab does not count.** "so nearly every change to
   the business crosses modules" is about changes, but the lesson runs only `cohesion`, not
   `change`. Replace with: "so most dependencies, 9 of the 14, run between modules."
5. **`part_b.py:437–438` — Anticorruption Layer concept.** "Here it is one service" does
   not match the book or the lesson's own quiz `why` at line 652. Evans (p. 111) defines a
   Service for each allocation function and implements them with one class. Use: "Here it
   is one class, named for its job, implementing a service for each function the feature
   needs."
6. **`part_b.py:636` — a distractor a careful reader can argue for.** After the
   refactoring Evans says the Delivery History has "no real need" to be kept and can be
   derived (p. 107). So "He removes the cargo's delivery history from the model" is half
   right. The `why` answers it, but the option invites the argument. Replace it with: "He
   has the cargo cache its latest handling event."

## NOTE

1. **`part_a.py:1334`.** "brought a production system down" is stronger than the book
   (p. 90), where the system kept running out of memory after a few hours during roll-out.
   "kept running out of memory in production" is exact.
2. **`part_a.py:1171–1172`.** The EJB Home is cited as an affinity, but Evans also warns
   that dressing it up as a Repository "could lead to other problems" (p. 92). A clause
   saying so would keep the lesson fair.
3. **`part_b.py:167–168`.** "chosen from the requirements, not from the roots": Evans
   first limits the candidates to the five roots, then lets the requirements pick among
   them (p. 102). "chosen among the roots by the requirements" is closer. Quiz item 3 and
   its `why` already state it this way.
4. **Lab and book differ on the order lock.** In the book (p. 76) the order lock leads to
   Amanda's save being refused until she fixes the total. The lab instead refuses the second
   editor on taking the lock. The lesson's note covers this; no change is needed.
5. **Teaching holds up.** Every lesson closes its note on what the count leaves to
   judgement. The costs Evans names are all stated:
   - the aggregate lock's cost on large orders;
   - "a constructor is all you need" and factories being underused;
   - the collection's speed on an object database;
   - the cached segment's upkeep.

   Every lab count is the consequence the argument is about. No other wrong answer is
   arguable.

**Verdict:** accurate and well taught. Make the one wrong quiz `why`, the two boxed-statement
paraphrases and the identity-scheme sentence right, and the course is ready.
