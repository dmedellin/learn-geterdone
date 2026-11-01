# Review (accuracy and teaching): Design Patterns, Course 5 — Behavioral Patterns I: Requests, Languages and Traversal

Course: `gof-behavioral-requests` (`content/design_patterns/c5_behavioral_requests/`,
`__init__.py`, `part_a.py`, `part_b.py`), six lessons. Built to
`docs/design-patterns/PLAN.md` §C Course 5, §D, §E, §F and `docs/design-patterns/AUTHORING.md`.
Reviewed 2026-11-01 against the private extraction of the operator's copy (PDF page = printed
+ 20). I read the pages behind every sentence about what the authors argue with `book.py` and
`page.py` (PDF pp. 241–311). I did not read the book whole or `site/`, and wrote only
this file.

## Gates

- **Preview:** `python3 scripts/preview_subject.py design_patterns --course gof-behavioral-requests --out …/scratchpad/rev/gof-behavioral-requests`
  printed 7 pages; labcheck 6 executed, 6 with pinned figures, 0 failing; **OK**.
- **`quotes.py`: 6 quotations, all OK.** 5.1 p. 243 (22 words), 5.2 p. 255 (7), 5.3 p. 275
  (24), 5.4 p. 277 (27), 5.5 p. 297 (12), 5.6 p. 303 (21). Each lesson has one quotation, so
  each is under 40 and 60. The PDF pages in the dict comments are right, and so are the
  section names (the Interpreter line is in Known Uses, the Mediator line is consequence 5).
- **`overlap.py … 8`:** the only runs are the book's title and the six counted quotations. At
  5 words the scanner finds near-runs that matter in Mediator and Memento (MF-2, MF-3).
- **Browser (Playwright, chromium, `file://`).** All six pages at 375 px and 1280 px: no
  sideways scroll, no page or console errors. I loaded all 16 presets. Each matches the prose,
  the worked lines and my own count by hand (e.g. `library` 11 hops, `garden` north 15, south
  15 with 2 discarded, `quiz-score` 345/4, q4 at 8, 5, 10, `cake-form-bigger` 28/7, `tiles`
  1 against 15). With `questions` set to 0 the lab refuses, naming the division.
- **Exercises typed in**, each matching its quiz `why`: bakery 7 hops, refund (5); thermostat
  22 / warm, warm / warm; museum 35, 9 nodes; catalogue s1 at 6, 4, 7; studio 21/6 against 7/1;
  locker 1 against 12.

## MUST-FIX

1. **`part_a.py:723–724` and the `why` at `part_a.py:808–809` — the Command exercise's last
   question has the wrong answer if you read it literally.** The script is `warm warm eco undo
   warm redo undo`. Read literally, "the second `warm`" is the second word. If you remove it,
   the run still has a `warm` after the undo, so the redo is still refused, not "set the target
   back to 16". The author means the `warm` that runs after the undo, which is the third.
   Replace with: "…and say what the redo would have done had the <code>warm</code> after the
   undo not run." In the `why`: "Had the warm after the undo not run, the redo would have
   re-run eco and set the target to 16." (Also split the 100-plus-column source line at 808.)
2. **`part_a.py:1498–1502` — Mediator's Applicability is close to the book's wording.** The
   first situation repeats the first bullet (p. 296) word for word except for an added "that".
   The scanner catches 7 words of it. The other two situations follow the bullets clause by
   clause. Replace with: "The authors give three situations: objects whose dealings with one
   another are clearly defined but tangled; an object that is hard to use elsewhere because it
   is wired to so many others; and behaviour shared among several classes that you want to
   change without a subclass of each."
3. **`part_b.py:141–148` and `156–158` — Memento's Participants, Collaborations and
   Applicability are close paraphrase.** The Applicability sentence repeats both bullets
   (p. 305) with near-runs of 7 and 6 words. "Mementos are passive; only the originator
   that…" is a 7-word run from Collaborations (p. 306). "…of the Originator's internal state
   as…" follows the Memento participant's wording. Replace 156–158 with: "The pattern fits when
   two things hold together: an object must be put back to an earlier state, so part of that
   state has to be kept somewhere, and handing the state out through ordinary getters would
   show other objects how the object is built." Replace 141–148 with: "The participants, as
   you would apply them. The Memento holds whatever part of the Originator's state the
   originator decides to put in it, and lets no one else at it. The Originator makes a memento
   of where it stands now and later resets itself from one. The Caretaker keeps the memento and
   never looks inside. The collaboration is short: the caretaker asks for a memento, holds it a
   while and hands it back, or never does if no undo comes. A memento does nothing by itself;
   only the originator that made it writes or reads what it holds."
4. **`part_a.py:1467–1470` with quiz items at `1634` and `1669` — the Mediator quiz has
   distractors that can be defended.** The concept defines a connection as "a reference by
   which one object can ask another", and a reference runs one way. On that definition, ten
   colleagues that call each other need 90 references, so answer "90" to item 4 can be argued
   for. The lab counts two-way translators, one per pair. Replace the concept with: "A two-way
   link by which two objects can ask each other for something, counted once per pair. Pairwise,
   every pair that interacts needs one; through a mediator, each colleague needs one, to the
   mediator." In items 1 and 4, add "counting one two-way connection per pair" to the question.
   In the `why`s, say that 42 and 90 count each pair from both ends.

## SHOULD-FIX

1. **The Command lab repeats Course 2's design** (`part_a.py:84–141` against
   `c2_document_editor/part_b.py:17–60`). User Operations already runs a garden irrigation
   controller with two zones, add/set commands and the same view. Its Java has the same
   `SetMinutes` with a `before` field and the same `History` with `done`/`undone` deques. A
   reader who takes the courses in order gets the same exercise twice. Move Command to another
   domain from PLAN §C's list (a bike-share dock, a theatre box office) and give its sketch
   something Course 2's lacks, such as a macro command or an invoker that holds a command.
2. **`part_b.py:178–180` — wrong source for the cursor point.** Memento's Related Patterns
   (p. 311) says only that mementos can be used for iteration, pointing back to Dylan's state
   objects. The point that a cursor is a simple memento is in Iterator's Implementation
   footnote (p. 281). Replace with: "Related Patterns: Command, which can keep undo state in
   mementos, and Iterator, since a memento can hold an iteration's state, as Dylan's collections
   do; Iterator's own Implementation calls its cursor a simple memento."
3. **`part_a.py:663–669` — Command's five uses keep the bullets' wording** ("parameterizes an
   object by an action", "a system … around high-level operations made of primitive ones";
   p. 255–256). Reword, for example: "A command lets you configure an object with what it
   should do… And a system's large operations can be composed of small ones, the way
   transactions are."
4. **`part_a.py:1229–1233` — Iterator's Applicability follows the three bullets (p. 279)
   phrase by phrase.** For example: "The pattern applies when clients should get at what an
   aggregate holds without learning how it holds it, when one aggregate must be walked in
   several ways or by several walks at once, and when different kinds of aggregate should be
   walked through one interface, which the book calls polymorphic iteration."
5. **`part_a.py:934–936` — Interpreter's motivation sentence follows the book's opening
   (p. 263)** clause by clause. For example: "The motivation: when the same sort of problem
   keeps coming back, describing each case in a small language and evaluating the descriptions
   can beat writing a fresh algorithm each time."

## NOTE

- Accuracy is otherwise good. Every intent, participant list, consequence (the three of Chain
  of Responsibility, the four of Command and Interpreter, the three of Iterator, the five of
  Mediator and Memento), implementation issue, sample code, known use and related pattern I
  checked is supported by the pages.
- Every lesson states its liabilities beside its benefits, ties its count to a stated
  consequence and ends on the gap the material clause names. Command and Iterator list no
  liabilities in their Consequences, and the lessons rightly take the costs from
  Implementation.
- Java 8: every sketch compiles as I read it, given the implied `Request`, `Zone`, `Part` and
  `Field` subclasses and the imports. `Request` must be a class, since Java 8 has no records.
  The roles and the direction of reference are right in each. In the Interpreter sketch, a
  `Div` built on `BigDecimal.divide` would throw on a quotient that does not terminate. A
  comment could say that the lab works in exact fractions.
- `DeskHandler` and `changed(Field source)` have the shape the pattern dictates; neither
  copies the book's code.
- The Mediator lab borrows dddkit's protocol view. Its status line says "contexts",
  "translators" and "the count is of the model stated". The panel intro explains this, and so
  does the PLAN. It is a kit gap, not a lesson fault.
- The cake order form's dependent fields are the same kind of example as the book's dialog,
  but not the font dialog PLAN §C bans.

**Verdict:** accurate and well taught, with labs that check out to the digit. Fix the
ambiguous Command exercise question, the defensible Mediator distractors and the close
paraphrases in Mediator and Memento before release.
