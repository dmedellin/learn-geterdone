# Review (accuracy and teaching): Domain-Driven Design, Course 2 — The Building Blocks of a Model-Driven Design

Course `ddd-building-blocks` (`content/domain_driven_design/c2_building_blocks/`), seven
lessons. Reviewed 2026-11-01 per `docs/domain-driven-design/REVIEW.md`. Every claim about
Evans was checked with `book.py`/`page.py` (PDF pp. 36–69). I did not read the book whole
or `site/`, and I wrote only this file.

## Gates

- **Preview:** `preview_subject.py domain_driven_design --course ddd-building-blocks --out …/scratchpad/rev/ddd-building-blocks`:
  8 pages, labcheck 7 executed, 7 with pinned figures, 0 failing; **OK**.
- **`quotes.py`: 7 quotations, all OK, one per lesson.** 1 p. 37 (27 words), 2 p. 41
  (19), 3 p. 45 (22), 4 p. 51 (12), 5 p. 56 (25), 6 p. 59 (6), 7 p. 63 (11). Every
  lesson is under 40 words and under 60, and each dict comment gives the PDF page.
- **`overlap.py … 8`: 10 runs.** All are counted quotations or section titles (The
  Domain Layer Is Where the Model Lives; Sticking with Model-Driven Design When
  Mixing Paradigms). None is anything else.
- **Browser (Playwright, chromium, `file://`).** All seven lessons at 375 and 1280 px:
  no sideways scroll, no page or console errors. Every preset's tiles match the prose
  and worked lines by my own count. Every exercise typed in agrees with its quiz `why`:
  clinic 2 up and 1 skip; gym 8 and 4; bike-share 10→4 and 6→3; members 2/3/1/2;
  term dates 4/3, then 1/0/1; bakery 2/7 and 4/7 with a cycle. The lab-tested quiz
  items 1.4, 2.4 and 6.4 also match.
- **Data.** No lab uses a book example domain from PLAN §C's list. No book code,
  diagram, table or dialogue is reproduced.

## MUST-FIX

1. **Boxed pattern statements paraphrased clause by clause, with 5–7-word
   near-runs** (PLAN §E: a boxed statement is paraphrased, never copied). The
   scanner at 5 words shows these runs. Each passage follows the box's sentence
   order one clause at a time. Rewrite each one as a rule in the lesson's own
   order and words:
   - `part_a.py:357–362` (Layered Architecture, p. 38): "a complex program into
     layers", "only on the layers below", "isolated from the user interface, the
     application and the infrastructure", "Freed from displaying and storing
     themselves". Replace with: "Put as a rule to apply: split a complex program by
     concern, let each part lean only on what lies under it, and give the model a
     layer of its own that screens, task coordination and plumbing stay out of.
     Objects that need not draw or save themselves can be about the business
     alone."
   - `part_a.py:686–690` (Smart UI, p. 41): "the application into small
     functions", "use a relational database as", "the most automated …
     tools available". Replace with: "Evans's prescription, for those
     circumstances only: let each screen be a small application that carries its
     own rules, keep the shared data in a relational store, and build the screens
     with whatever tools generate them fastest."
   - `part_a.py:1296–1302` and `1493–1496` (Entities, p. 51): "in the model, keep
     the class", "whatever its form or history", "requirements that match objects
     by attributes", "a unique result for each object". Replace with: "Put as a
     rule to apply: if an object matters for who it is, let identity lead its
     definition, keep the class about remaining the same thing over its life, give
     it a way to be told apart that survives any change of storage or shape, and
     distrust any requirement to match such objects on their fields. The identity
     is an operation that never gives two objects the same answer, …". In the
     mistake: "…asks for an identification that survives any change of shape or
     storage, and distrusts requirements to match on fields;…"
   - `part_a.py:1613–1616` (Value Objects, p. 56): "when you care only about",
     "treat it as immutable", "should form a conceptual whole". Replace with: "Put
     as a rule to apply: if nobody cares which instance they hold, only what it
     says, make it a value; let it carry the meaning and operations of what it
     describes, never change it in place, and give it no identity. Its parts should
     belong together as one idea, Ward Cunningham's Whole Value:…"
   - `part_b.py:527–536` and quiz answer `724–725` (Modules, p. 63): "a cohesive
     set of concepts", "overlooked concept that would bring the elements
     together", "is not an alternative to technical measures". Replace with: "Put
     as a rule to apply: let each module be a chapter of the domain's story, its
     concepts belonging together. Low coupling often follows; when it does not,
     change the model so the concepts separate, or find a missing concept that can
     anchor a module of its own. … Thinking in concepts does not replace the
     technical measures; it works at another level of the same problem;…". Quiz
     answer: "Change the model so the concepts separate, or find a missing concept
     that can anchor a module of its own".

2. **`part_a.py:422–424` misdescribes Evans.** The lesson says "a project that has no
   application layer at all, which Evans says some do". Evans says (p. 38) that
   some projects do not make a sharp distinction between the user interface and
   application layers, and that others have several infrastructure layers. Replace
   with: "a project that folds the application layer into the user interface, as
   Evans says some do, would show 1 there and break no rule."

3. **Associations, "counted as one": the quiz stem makes a wrong answer arguable,
   and the worked lines contradict each other.**
   - The concept (`part_a.py:967–968`) and quiz 1's stem (`1147`) say a qualified many
     end counts "as one". Read literally, that is one many end, which makes the
     distractor "4 directions and 4 many ends" (`1149`) correct. The lab counts it
     as 0 (the bike-share's after-model gives 3).
   - Worked line `1132` says "its many end is 1", and the next line sums it as 0.
   - Replace the concept's sentence with "the lab counts a qualified many end as a
     one end, so it is no longer a many end". Replace the stem's phrase with
     "counting a qualified many end as no longer many". Replace line 1132 with
     "room to course qualified: no many end".

## SHOULD-FIX

1. **`part_b.py:604–607`:** "give the association a direction" does not fit here.
   The added dependency `AccessionLogic, ShipmentLogic` already runs one way, and
   its direction is what closes the cycle. Turned round (shipments know their
   accession), it gives no cycle. Suggest: "…turn it round, so that a shipment
   names its accession, as the Associations lesson did with its links, or find the
   concept that would hold it."
2. **Value Objects quiz 2, distractor "It must be copied whenever it is read"
   (`part_a.py:1768`).** This can be argued for. The lesson's own safe preset is
   copy-per-holder, and Evans (p. 56) gives passing a copy as a cure. Replace it
   with "It must be declared final in the language".
3. **Services exercise (`part_b.py:283–287`)** maps one to one onto Evans's banking
   cases on pp. 60–61: export, transfer between two accounts, notification and the
   balance threshold. The `why` says so. The reader can answer by analogy without
   applying the test. Vary at least two items, for example a domain operation that
   involves one entity, or an application service that does apply a rule.
4. **Entities lab (`part_a.py:189–200`, 1331–1341):** two systems that exchange
   patient records under a shared patient ID echo Evans's aside on p. 53–54
   (hospitals exchanging medical records). The clinic is a PLAN-approved domain
   and the aside is brief, so this is not a MUST. Consider the library members
   (already the exercise) or the box office as the preset, and the clinic as the
   exercise.
5. **`part_a.py:1311–1313`:** "recorded by different people on different dates"
   is a 7-word run from p. 51. Use "entered by different people on different
   days".
6. **`part_b.py:554–555`:** "developers stopped creating or changing modules"
   overstates p. 65 (they "tended to avoid" making many and "hardly ever" changed
   one). Use "developers avoided making modules and hardly ever changed one".

## NOTE

- The book's examples are summarised briefly and correctly (banking transfer, presidents, brokerage, stadium, four-tier project, object database). Smart UI gets a fair hearing.
- `part_b.py:199`: "Evans's service is smaller" than Service Layer; the book says medium-grained and makes no such comparison. "Narrower in scope" is safer.
- `part_b.py:160`, `394`: 6-word runs from p. 60's characteristics and box; consider rewording.
- Every lab count is tied to the pattern's argument, and every lesson's `note` says what the count cannot decide.

**Verdict:** accurate and well-taught, and the gates and labs are clean. Before
release, fix the boxed-statement paraphrases, the application-layer
misattribution and the ambiguous "qualified as one" wording.
