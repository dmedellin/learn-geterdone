# Review (accuracy and teaching): Design Patterns, Course 2 — A Case Study: Designing a Document Editor

Course: `gof-document-editor` (`content/design_patterns/c2_document_editor/`,
`__init__.py`, `part_a.py`, `part_b.py`), seven lessons. Built to
`docs/design-patterns/PLAN.md` §C Course 2 and `docs/design-patterns/AUTHORING.md`.
Reviewed 2026-11-01 against the private extraction of the operator's copy
(PDF page = printed page + 20). I read all of Chapter 2 (PDF pp. 53–97) with `page.py`,
and the catalog passages the lessons cite (Composite pp. 186–189, Decorator p. 198,
Abstract Factory p. 110, Bridge p. 174, Command pp. 258–259, Strategy p. 338,
Visitor pp. 355–357, each Intent). I did not read the book file whole and did not
read `site/`. This is the only file I wrote.

## Gates

- **Preview:** `python3 scripts/preview_subject.py design_patterns --course gof-document-editor --out …/scratchpad/rev/gof-document-editor`:
  8 pages; labcheck 7 executed, 7 with pinned figures, 0 failing; **OK**.
- **`quotes.py`: 7 quotations, all OK.** 2.1 p. 56 (25 words), 2.2 p. 61 (20), 2.3 p. 64 (24),
  2.4 p. 68 (32), 2.5 p. 78 (18), 2.6 p. 80 (16), 2.7 p. 96 (18). One quotation per lesson,
  each under 40 words, PDF page in the dict comment.
- **`overlap.py … 8`:** every run is the book's title, author list, chapter or section title,
  or a counted quotation. Nothing else.
- **Browser (Playwright, chromium, `file://`).** All seven lessons at 375 px and 1280 px: no
  sideways scroll (scrollWidth = clientWidth), no page or console errors. Every preset loaded;
  every tile matches the prose, the worked lines and my own count (recipe book 10 / 6 / 4 / depth 3 /
  345, subtotals 135 / 210 / 175; talk 7 / 17.5; playlist 13 / 9 / +3 / +4; guide 25.5 / 24.5 /
  21.5 / 9.5, 8 vs 6, 4 vs 5; map 16, +4/0 and +4/4; notices 10 / 8 / 5/4, 13 / 9; garden-week
  front 30 back 25, undo [boost, trim], redo [summer], 1 discarded, 1 vs 6; nothing-to-undo
  refusals 1 and 2; visitor 20 / 20 / 9 / 6, 0+4 and 1+3). I typed every exercise in: mixtape
  9 calls, 21.5, side-b 7.75; cards 7 / 7 / 1× / +2 / +1; ticket 34 and 34.5; quiz app 9, +3,
  edits 3; printers 9 / 8 / +2 / +1; garden script front 0 back 30, undo [rain], redo [trim],
  1 discarded, redo 1 refused; mixtape visitors 27 / 8 / 4 changed. Each agrees with its quiz
  `why`.
- **Lab data:** no book example domain anywhere (recipe book, playlist, audio guide, map viewer,
  library notices, printers, irrigation controller, mixtape).

## MUST-FIX

1. **`part_a.py:1311` — arguable distractor.** Q "Why does Section 2.5 reject creating widgets
   with constructor calls?" offers "C++ constructors cannot return a subclass". That is true, and
   it is *why* a constructor call fixes the class: a reader can argue for it. The book's reason
   (p. 68) is that the call hard-codes one style, so the style can't be chosen at run time, and
   every call has to be found to port. Replace the option with
   `"Each constructor call makes a fresh widget where one shared widget would do"` and change the
   `why` sentence "The section says nothing about speed" to "The section says nothing about speed
   or sharing".

2. **`part_a.py:1357–1361` — overstatement.** "insist it is set once, after the style is known
   and before any product is made". The book (p. 69) asks only that the factory be set before it
   is first used and after the look and feel is known. On p. 71 it says the program can reset it
   to another factory and rebuild the interface, and the lesson's own body (l. 1174–1175) says so
   too. Replace with: "but insist that it is set after the style is known and before any product
   is made, and that the code which makes products never chooses it."

3. **`part_b.py:328–329` — garbled, and wrong as written.** The `why` ends "A menu item is a glyph
   and can hold state; it is a command object that gains Unexecute." Read straight, "it" is the
   menu item, but a MenuItem *holds* a Command (p. 80) and only Command gains Unexecute
   (p. 82). The sentence also leaves the fourth option unanswered. Replace with: "A menu item is a
   glyph and can hold state; undo comes from the Command it holds, which gains Unexecute; and
   MenuItem is itself a subclass of Glyph."

## SHOULD-FIX

1. **Bridge's liabilities (`part_a.py:1475–1478`).** The lesson lists the three consequences, all
   of them benefits, which is accurate: the catalog (p. 174) names no liability. PLAN §F still asks
   for costs beside benefits. Add: "The catalog names no liability. The costs are visible in the
   section itself: a second hierarchy to maintain, a call through the implementation object
   for every drawing request, and an implementation interface that must be found to fit
   systems that do the same things differently."

2. **Command's costs and the sketch (`part_b.py:176–179`, `31–63`).** Nothing names a cost of
   Command. Its Implementation (pp. 258–259) gives two: a command whose state changes when it runs
   must be copied before it goes on the history, and repeated undo and redo can pile up errors
   (hysteresis). The `SetMinutes` sketch has the first problem. It stores `before` in a field, and
   `History.run` pushes the same instance, so running one `SetMinutes` object twice overwrites the
   value that the first undo needs. Add to the paragraph: "It also warns that a command whose
   state changes when it runs must be copied before it goes on the history, and that errors can
   pile up over many undos and redos." In `HISTORY_JAVA` add the comment
   `// c is a fresh command per request; a reused one would be copied first`.

3. **Visitor's other liability (`part_b.py:480–483`).** Only "new elements are hard" is given.
   The catalog (p. 357) also names breaking encapsulation: elements often have to make public
   operations that expose their internal state. Add after "every visitor gains a method for it":
   "and visitors often need elements to expose state through public operations, which the
   catalog counts as a cost to encapsulation."

4. **Visitor sketch is missing the Element role (`part_b.py:68–84`).** `Recipe implements BookPart`
   with an `accept`, but `BookPart` as lesson 1 declares it has no `accept`, so the Element
   participant is never shown. Replace the `Recipe` block's first line with
   `interface BookPart { void accept(BookVisitor v); }` followed by the `Recipe` class (still
   under 20 lines if `// ...` is dropped).

5. **Near-runs on Intents.** Strategy's concept (`part_a.py:562`) "a family of interchangeable
   algorithms" echoes the Intent's opening clause and its "interchangeable". Replace with "several
   algorithms for one job, each in a ConcreteStrategy class…". Bridge's concept
   (`part_a.py:1420–1421`) "so the two hierarchies vary independently" echoes the Intent's ending.
   Replace with "so that either hierarchy can gain classes without touching the other".

6. **`part_b.py:126`** "reverses the command just before the marker and moves it back": "it" reads
   as the command. Change to "and moves the marker back one place".

## NOTE

1. Section comments are off by one: `part_a.py:87, 114, 143, 174` say 2.2–2.5 for the records of
   2.3–2.6, and `part_b.py:17, 66` say 2.6 and 2.7 for 2.7 and 2.8. They are not shown to the
   reader. Renumber them.
2. The Decorator count counts the interface on the Decorator side (n + 3) but not on the
   subclassing side (2ⁿ). The lesson states both formulas, and at n = 2 it says honestly that
   Decorator costs one class more, so this is defensible. It is worth one clause: "the subclass
   design needs no separate interface".
3. The Composite concept (`part_a.py:248–253`) restates the second sentence of Composite's Intent
   in different words, with no run longer than two words. That is acceptable paraphrase.
4. Teaching is strong. Each lab's count is the section's own argument: Section 2.4's subclass
   explosion, Section 2.5's new-kind asymmetry, Section 2.8's question of which hierarchy
   changes. Each `note` closes on what the count cannot settle. Composite, Strategy, Decorator,
   Abstract Factory and Visitor each state their catalog liabilities. Every other wrong quiz
   answer, which I tried to argue for, is wrong on the book or on the count.
5. Java sketches: in my reading all seven compile as Java 8, given the elided imports and the
   domain types. Each shows its pattern's participants with references pointing the right way:
   decorator → component, Notice → Channel, MapViewer → MapStyle, Playlist → Ordering.

**Verdict:** accurate and well-taught, with clean gates. Fix one arguable distractor, one
overstatement about the factory being set once, and one garbled quiz explanation, then add the
missing Bridge, Command and Visitor costs.
