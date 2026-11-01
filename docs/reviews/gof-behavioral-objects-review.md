# Review (accuracy and teaching): Design Patterns, Course 6 — Behavioral Patterns II: Notification, State and Algorithms, and the Conclusion

Course: `gof-behavioral-objects` (`content/design_patterns/c6_behavioral_objects/`,
`__init__.py`, `part_a.py`, `part_b.py`), seven lessons, and its 31 spoken forms in
`content/spoken/design_patterns.py`. Built to `docs/design-patterns/PLAN.md` §C
Course 6, §E, §F and `docs/design-patterns/AUTHORING.md`. Reviewed 2026-11-01
against the private extraction of the operator's copy (PDF page = printed page + 20).
I read the pages behind every sentence that says what the authors argue, using `book.py`
and `page.py`: Observer pp. 313–323, State pp. 325–333, Strategy pp. 335–343, Template
Method pp. 345–350, Visitor pp. 351–364, the Discussion pp. 365–369 and Chapter 6
pp. 371–378. I did not read the book file whole and did not read `site/`.

**Scope.** I wrote only this file. Each finding is a recommendation, with replacement
text where the fix is mechanical.

## Gates

- **Preview:** `python3 scripts/preview_subject.py design_patterns --course gof-behavioral-objects --out …/scratchpad/rev/gof-behavioral-objects`
  rendered 8 pages. Labcheck: 7 executed, 7 with pinned figures, 0 failing. **OK**.
- **`quotes.py`: 8 quotations, all OK.** 6.1 p. 316 (19 words), 6.2 p. 325 (20), 6.3
  p. 338 (14), 6.4 p. 345 (14) plus the Hollywood phrase p. 347 (6; lesson 20), 6.5
  p. 351 (18), 6.6 p. 366 (15), 6.7 p. 375 (8). Every opening is under 40 words and every
  lesson under 60. Each dict has its PDF page in a comment.
- **`overlap.py … 8`:** the only runs are the book's title, the section title "6.1 What
  to Expect from Design Patterns", and the counted quotations. At 6 words the runs are
  section and pattern names or stock phrases, apart from the Applicability near-runs
  under S2.
- **Browser (Playwright, chromium, `file://`).** All seven lessons at 375 px and
  1280 px: no sideways scroll (scrollWidth equals clientWidth), no page or console
  errors. I loaded every preset (15 in all), and every tile matches the prose and the
  worked lines by my own count. Examples: box office 8 / 21 / 13 / 8, per observer
  7, 8, 1, 5 and then 4, 4, 1, 4; library copy final state lost, 2 ignored, 14 branches /
  7 classes, and with repair 18 / 8, never entered overdue and lost; print shop 8
  (`1 + if 3 + case 3 + && 1`, line 4) → 3 (line 7); tiles 21 / 12 → 13, TerrainTile
  lacks style; playlist 16 / 9 / 6, adding an operation gives 0 added, 4 changed, and
  adding a kind gives 3 changed; desk 10 / 4 against 5 / 1, and with eight devices
  28 / 7, 3.5×; bakery 9 (confined 1) → 6 (confined 2). I typed all seven exercises in
  (strategy before and after, conclusion before and after), and each lab result
  matches its quiz `why`: 13 and 6; ready, 2 ignored, 11 / 6; 6 → 3; Cortado, 12 / 7;
  15, 12 / 9, 4 changed; 21 / 6 against 7 / 1; 6 / 1 → 4 / 2.
- **Spoken forms:** all 31 keys occur in the course text. `speechcheck.py --list
  design-patterns` returns `[]`. No key collides with another Subject's spoken file.
  For two keys shared within this Subject, see N1.
- **Java:** all seven sketches read as valid Java 8, given the usual imports and the
  domain types they name (enum states that override interface default methods,
  `final` template method, double-dispatch `accept`). Each shows the pattern's
  participants with references running the right way.

## MUST-FIX

1. **`part_b.py:183–184` — "often" overstates.** The Discussion says *sometimes* the
   observer of one subject is a subject of another observer (p. 366). Replace
   "often with one subject's observer being another's subject" with "sometimes with
   one subject's observer being another's subject".

2. **`part_b.py:364–367` — the mistake misdescribes the Discussion's argument.** The
   book's one exception to "a new object that encapsulates the aspect, used by existing
   objects" is Chain of Responsibility (p. 365). It brings in objects passed as arguments
   (Visitor, Command, Memento) as a different point, about communication that is not
   fixed between classes. These objects still encapsulate something: a command is a
   request, a memento a state (p. 366). The mistake as written presents them as patterns
   that do not wrap anything. Replace the pair with:
   `("Thinking every behavioral pattern splits a new object from the ones that use it",
   "Most do, and are named for the new object. Chain of Responsibility works instead over
   any number of objects that may already exist, with communication left open-ended; and
   Visitor, Command and Memento wrap an operation, a request or a state in objects that
   travel as arguments rather than being kept by their users.")`

3. **`part_a.py:1516` — "only" overstates.** The book gives a complex traversal that
   depends on the operation's results as the *main* reason to put traversal in the
   visitor, not the only one (p. 359). The lesson's own quiz `why` (line 1665) says
   "main reason". Replace "the last only for an irregular traversal" with "the last
   mainly for an irregular traversal".

## SHOULD-FIX

1. **`part_a.py:828`, `why` 831–834 — a distractor that adds up to the right number.**
   "One for each of the 9 transitions and the 5 events not ignored" gives 14 by
   arithmetic, and the `why` never answers it. The figure 5 matches no count in the
   design: 7 events, 6 distinct events in the input that are followed, 8 followed steps.
   Add to the `why`: "The input plays no part: the branches are a count of the code, so
   which events a trace happens to ignore does not change them."

2. **Applicability summaries track the bullets too closely (copyright, REVIEW §5).**
   No run reaches 8 words. But four lessons compress the Applicability bullet by bullet,
   in the book's order and with 5–6-word near-runs:
   - Observer, `part_a.py:340–344`: "when an abstraction has two aspects …, … cannot say
     how many, … without assuming anything about who they are".
   - State, `641–644`: "large conditionals … enumerated constants … State puts each
     branch in a class of its own".
   - Strategy, `929–932`: "related classes differ only in behaviour … variants of an
     algorithm".
   - Visitor, `1488–1491`: "many classes with differing interfaces … classes rarely
     change but the operations often do".

   Recast each as one sentence in the lesson's own terms, and stop following the
   bullets one for one. For example, for Observer: "The Applicability's cases come
   down to one: some objects must follow another's state, and the one that changes
   should not have to know who they are or how many."

3. **`part_b.py:468` — "help most".** The book says patterns are "especially useful" in
   getting from an analysis model to an implementation model (p. 373), not that this
   is where they help most. Replace "They help most in getting from" with "They are
   especially useful in getting from".

4. **`part_b.py:209–210` — "a prototype made of it".** The Summary says the composition
   might be *treated as* a Prototype by another part of the system (p. 369). Replace
   "a builder that made it and a prototype made of it" with "a builder that made it,
   and other parts of the system treating it as a prototype".

5. **Strategy's own Related Patterns go unnamed (`part_a.py:964–967`).** The section
   lists only Flyweight (p. 343). The lesson's "two neighbours" are Template Method
   (taken from Template Method's Related Patterns) and the DDD lesson. Flyweight
   appears earlier, but only as a remedy for a liability. Add before "Two neighbours":
   "Strategy's Related Patterns name only Flyweight, since stateless strategies make
   good flyweights."

## NOTE

1. Two spoken keys, "with Visitor: 3 × 2 + 3 = 9 methods" and "on the elements:
   3 × 2 = 6 methods", are also worked lines in course 2's Visitor lesson
   (`c2_document_editor/part_b.py:588–589`). The reading suits both, so nothing breaks.
   But if course 2's author keys them too, the dict will hold the key twice. The two
   Visitor labs also share the same shape (3 kinds × 2 visitors). That is acceptable,
   but a reader doing both courses will see the same figures.
2. The Discussion lab's status line says "contexts", "published language" and "the
   count is of the model stated", the dddkit wording. The lesson body and
   `panel_intro` both say how to read these terms. This is a kit gap, not a course
   fault.
3. The managed scheme in the Observer lab also merges repeated changes to *one*
   subject within an operation (the exchange, the shower). The book's DAG manager is
   framed around changes to several subjects (p. 319). The opening of issue 8, which
   waits until "all the subjects have been modified", supports the per-operation
   reading. Fine as it stands.
4. `part_b.py:511`: "which the book quotes in full" adds nothing; the passage is an
   excerpt from *A Pattern Language*. Consider "which the book quotes".
5. Teaching holds up. Every lesson states liabilities beside benefits, each lab counts
   a consequence the book names, each lesson ends on what the count leaves open, and
   no lab uses a book domain (PLAN §C). I could not argue for any other wrong quiz
   answer.

**Verdict:** accurate, well-gated and well-taught. Three small overstatements or
misframings to fix, one quiz `why` to complete, and the Applicability summaries to
loosen.
