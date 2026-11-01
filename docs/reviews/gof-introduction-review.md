# Review (accuracy and teaching): Design Patterns, Course 1 — What Design Patterns Are

Course: `gof-introduction` (`content/design_patterns/c1_introduction/`, `__init__.py`,
`part_a.py`, `part_b.py`), six lessons, plus the PATH fields in
`content/design_patterns/__init__.py`. Built to `docs/design-patterns/PLAN.md` §A, §C
Course 1, §E, §F and `docs/design-patterns/AUTHORING.md`. Reviewed 2026-11-01 against
the private extraction of the operator's copy (PDF page = printed page + 20). I read the
pages behind every sentence that says what the authors argue, with `book.py` and
`page.py` (PDF pp. 19, 22–51). I did not read the book file whole, and I did not read `site/`.

**Scope.** I wrote only this file. Each finding is a recommendation, with replacement text.

## Gates

- **Preview:** `python3 scripts/preview_subject.py design_patterns --course gof-introduction --out …/scratchpad/rev/gof-introduction`
  rendered 7 pages; labcheck 6 executed, 6 with pinned figures, 0 failing; **OK**.
- **`quotes.py`: 10 quotations, all OK**, each on the page its comment gives: 1.1 p. 23
  (25 words) + "Inheritance" p. 24 (1); 1.2 p. 26 (18); 1.3 p. 38 (7 + 21); 1.4 p. 40
  (6 + 22); 1.5 p. 44 (26, with "particular" re-quoted: 31 in the lesson); 1.6 p. 51 (15 + 7).
  Every opening quotation is 40 words or fewer, and every lesson has 60 or fewer.
- **`overlap.py <course dir> 8`:** every run is a section title, the book's title or a
  counted quotation. On the PATH fields (scanned separately), the runs are the authors'
  names, the book's title and a course title.
- **Browser (Playwright, chromium, `file://`).** All six lessons at 375 px and 1280 px:
  scrollWidth equals clientWidth, with no page or console errors. I checked every preset's
  tiles against the prose and the worked lines and they match. These are the tiles the
  prose does not quote: `fourth-view` redundant 4, and `interface-plus-post` 15 pairs at
  `1/3 ≈ 33.3%`. I typed in all six exercises (two designs each for 1.3 and 1.5). The lab
  matched every quiz key: 6/24/16/8; bridge and interpreter; TileView 4→2 with TileSource
  fan-in 4; 19/11/6/1; 5→4 with 2 of 3 confined; search-ranking and hold-queue, with
  ebook-loans failing `months <= 12`.
- **Example domains (PLAN §C):** dock, quiz board, locker, tile viewer, player,
  irrigation, vending machine, bakery and library. None of them is the book's.

## MUST-FIX

1. **`part_a.py:1617–1618` and `part_a.py:1737–1738`: hourly-forecast does not reach
   "every user" of the weather module.** In `encapsulated`, `WeeklyReport` (reports) is a
   user of `WeatherSource`, because it is the fourth class `new-provider` touched in
   `spread`. The hourly-forecast change does not touch it, and the lab counts 3 modules,
   not 4. The prose and the keyed quiz answer both say "every" user changes, which is
   false on the lesson's own data. A careful reader will reject the "correct" answer.
   - Body, replace "reaches the weather module and every user of it, 3 modules" with
     "reaches the weather module and every module whose classes use the new forecast,
     scheduling and alerts: 3 modules".
   - Quiz option 1, replace with "Because it changes the WeatherSource interface itself,
     so the weather module changes along with every module that uses the new forecast".
2. **`__init__.py:21`: "Chapter 1 of the catalog".** The book calls Chapters 3–5 the
   catalog, and Chapters 1–2 are the part before it (Guide to Readers, PDF p. 19). Replace
   with "Chapter 1 of the book, the Introduction, read section by section."

## SHOULD-FIX

1. **`part_b.py:144`: "usually bought".** The book says "Often" (p. 51). Replace with "often
   bought".
2. **`part_a.py:1254`: "a parent usually fixes part of its children's representation".**
   The book says "often" (p. 39). Replace with "often".
3. **`part_b.py:161–163`: the payment provider "points to Table 1.2 … a platform, Bridge or
   Abstract Factory".** Table 1.2 (p. 50) has no "platform" entry. Platform dependence is
   cause of redesign 3 in §1.6, where the book lists Abstract Factory and Bridge (p. 44).
   Replace with "the payment provider is a platform dependence, for which §1.6's list of
   causes gives Abstract Factory and Bridge (in Table 1.2, Bridge lets an object's
   implementation vary)".
4. **`part_a.py:668–670`: "and pattern names are capitalised".** §1.4 states only the
   page-number convention (p. 28). Small capitals for names are described in the notes to
   the index (p. 403), not in this section. Replace with "every pattern is named with the
   page it starts on in parentheses, a convention the authors say they follow throughout
   the book."
5. **Near-runs of the book's wording (copyright item 5).**
   - `part_a.py:1128–1129` repeats the book's definition of dynamic binding word for word
     but one (pp. 34, 380). Replace with "What does Section 1.6 call the choice, made while
     the program runs, of which object's operation answers a request?"
   - `part_a.py:811–812` follows the template's own question for Implementation (p. 27).
     Replace with "Which section of the template is about building the pattern: its traps
     and the techniques that help?"
   - `part_b.py:305–307` (the quiz `why`) tracks the p. 51 sentence. Replace with "The
     authors say the flexibility usually comes from an extra layer of indirection, which can
     make a design harder to follow and slower; …"
   - `part_a.py:1429–1430` tracks p. 41 closely. Replace with "Because so much is decided by
     which objects are connected at run time, the design is harder to follow than one fixed
     in code, and there is some run-time cost."
6. **`part_b.py:39`: the comment "the thirteenth is free" is wrong for `items / 12`.** With
   that code, 12 items earn one free unit, so the twelfth is free. Either divide by 13, or
   change the comment to "one unit free per dozen".

## NOTE

1. **Accuracy otherwise holds up.** I checked these against the pages:
   - §1.1: the four elements, names "among the hardest parts", the level between a hash
     table and an application, and the effect of language choice, including CLOS
     multi-methods and Visitor.
   - §1.2: Observer, Composite and Strategy as MVC's main relationships, with Factory
     Method and Decorator.
   - §1.3–1.5: the thirteen headings, at least two known uses from different domains,
     purpose and scope with every one of the eight pattern attributes, Adapter in both
     scopes, Prototype as an alternative to Abstract Factory, and Composite with Iterator or
     Visitor.
   - §1.6:
     - Strategy and State as late-found objects.
     - The granularity patterns.
     - Memento's two interfaces, and the matching interfaces of Decorator and Proxy.
     - Inheritance in C++/Eiffel against Smalltalk.
     - Inheritance's two disadvantages and the abstract-class remedy.
     - Composition's "more objects (if fewer classes)", which sits in the same paragraph.
     - The rectangle example of delegation, its cost, and State, Strategy and Visitor.
     - The three sort options.
     - Aggregation's identical lifetimes.
     - The patterns that make run-time structure readable.
     - **All eight causes of redesign, with exactly the book's pattern lists.**
     - Toolkits, frameworks, inversion of control, and the three differences between
       patterns and frameworks.
   - §1.7–1.8: the six approaches, the opposition between the last two, the six Table 1.2
     entries cited, and the seven steps in order.
   - PATH: the eight patterns of the case study, Chapter 5's eleven patterns, the catalog as
     both reference and read-through (Guide to Readers, p. 19), and the restraint warning.
     These are accurate, and 6 courses / 40 lessons matches the package.
2. **Java.** All seven sketches read as valid Java 8, given the obvious imports. The roles
   point the right way: `Dock`→`DockView`, `LockerApp`→`Notifier`, and `Player` composed of
   `TrackSource` and `PlayOrder`. `PushSender.notify(String, String)` (`part_a.py:138`) is a
   legal overload of `Object.notify()`. It is confusing, though, and `push.send(...)` reads
   better.
3. **Teaching.**
   - Every note closes on the material clause's gap.
   - Every lesson sets a cost beside the benefit:
     - 1.1: one more update per view.
     - 1.3: an interface with one implementation.
     - 1.4: behaviour spread over objects.
     - 1.5: the forecast change now spreads further.
     - 1.6: indirection.
   - The course ends on §1.8's warning, as §F asks.
   - Every distractor I tried to argue for failed on the book or on the lab's count.
4. **Alexander's definition** (`part_a.py:361–364`) is a close paraphrase of the famous
   quotation the authors cite. It is under the scanner's threshold and not an Intent, so it
   can stay. Loosening "without ever being built the same way twice" would be safer.
5. The course `blurb` names five of the six lab designs; the bakery is missing.

**Verdict:** accurate and well taught. Fix the two MUST-FIX items (a keyed quiz answer that
contradicts the lab's data, and "Chapter 1 of the catalog") and the course is ready.
