# Review (accuracy and teaching): Domain-Driven Design, Course 7 — Maintaining Model Integrity

Course `ddd-model-integrity` (`content/domain_driven_design/c7_model_integrity/`), eight
lessons on Chapter 14, reviewed 2026-11-01 to `docs/domain-driven-design/REVIEW.md`
against PDF pp. 205–246 of the private extraction. I wrote only this file.

## Gates

- **Preview:** `preview_subject.py domain_driven_design --course ddd-model-integrity`
  rendered 9 pages; labcheck 8 executed, 8 with pinned figures, 0 failing; **OK**.
- **`quotes.py`: 8 quotations, all OK**, one a lesson, each the lesson's whole quoted
  total: 7.1 p. 208 (27 words), 7.2 p. 211 (23), 7.3 p. 213 (8), 7.4 p. 220 (17),
  7.5 p. 225 (17), 7.6 p. 230 (9), 7.7 p. 236 (10), 7.8 p. 242 (22).; source-comment pages
  right.
- **`overlap.py … 8`:** 8 runs, each one of the counted quotations. **Clean.** At 5
  words the scan shows near-runs in six boxed pattern statements (MF-5).
- **Browser (Playwright, chromium, `file://`):** at 1280 px and 375 px, no page scrolls
  sideways and none logs an error. Every preset's tiles match its `expect`, the prose
  and the worked lines. I typed every exercise in (and quiz 3.4's variant); each
  result matches its quiz `why`.
- **Data:** no book example domain is lab data; `ACL_JAVA` is 20 lines, the course's own.

## MUST-FIX

1. **part_a.py:860–863 (Context Map).** "…means changing the Venue and Box Office
   models and two translators" drops marketing; the preset and the paragraph above
   count 3 models. Replace with: "…means changing the Venue, Box
   Office and Marketing models and two translators, and that a change at Payments
   means one translator."

2. **part_b.py:217–219 and 288–297 (Separate Ways / OHS / PL).** The prose and the
   worked example give the one-way figures "30 and 10 against 12 and 2" (worked lines
   30 and 10). The lab cannot print them, because the lesson sets `"directed": "no"`
   at cfg level. The worked intro also says "Count the three presets"; there are two.
   Replace 217–219 with: "Counted one way, by hand, each figure doubles, 30 and 10
   against 12 and 2, and the ratios stay the same; this lab counts two-way translators
   only." Change the worked title to "Six theatres, two schemes" and the intro to
   "Count the two presets by hand, with n = 6, and the one-way figures beside them,
   which the lab does not show."

3. **part_b.py:193–194 (the DB2/Btrieve story).** "moving a client's product from one
   database to a lighter one" gets the example wrong. The client wanted to ship to
   users without a DB2 licence, so Evans built a Btrieve interface beside DB2 and did
   not replace it (p. 233). Replace with: "Evans tells of letting a client's product run
   on a lighter database as well as its original one, by building his component on…"

4. **part_b.py:880–883 (quiz 8.2 `why`).** "The core comes later, in the next
   transformation" is wrong. In the Separate Ways → Shared Kernel plan itself, later
   iterations may take on Core Domain subdomains once the process has firmed up
   (p. 243). Replace with: "The core comes later, once the process has firmed up and
   the teams are confident, and subdomains tailored to different jargons are deferred
   until a deep model can replace both."

5. **Close paraphrase of boxed pattern statements (5–7-word near-runs, §E).** The
   8-word scanner misses these, but each one follows the bold statement nearly word
   for word:
   - part_b.py:133–135, the Open Host Service concept ("a protocol that gives access
     to a subsystem as a set of Services, open…"). It matches 13 of the statement's
     first 14 words (p. 232). Replace with: "One interface of Services that a
     subsystem in demand offers to every context that integrates with it, grown for
     common needs, while a lone team's unusual needs get a translator of their own."
   - part_b.py:177–180 has the same in the body ("define a protocol that gives access
     to the subsystem as Services…"). Replace with: "So: describe the subsystem as
     Services behind one protocol any integrating team may use; grow it for common
     needs, and serve one team's unusual needs with its own translator, keeping what
     everyone shares simple."
   - part_b.py:129–131, the Separate Ways concept ("declared to have no connection to
     the others … find simple, specialised solutions"), is a 7-word run (p. 230), and
     part_b.py:160–161 echoes it. Replace the concept with: "A Bounded Context cut
     loose from all the others: no shared logic, little or no data passed through
     translation, and its developers free to solve its narrow problem as simply as
     they can." Replace the body clause with: "So cut the context loose and let its
     developers solve its narrow problem as simply as they can".
   - part_a.py:1047–1048 and 1085–1086, Shared Kernel ("subset of the domain model …
     that the two teams agree to share", a 7-word run, p. 220). Replace with "a part of
     the domain model, with the code and schema behind it, that two teams hold in
     common by explicit agreement".
   - part_a.py:243–244 and quiz 1.4 answer 445–446 (Bounded Context: "usage within parts
     of the application, and physical forms such as code bases and schemas", p. 208).
     Replace the quiz answer with "Who owns the model, which parts of the application
     use it, and the code and schema it lives in". In the concept, change "its physical
     forms such as a code base and a schema" to "the code and schema it lives in".
   - part_a.py:1322 (ACL concept, "talks to that system through its existing
     interface", p. 227). Replace with "reaches that system by the interface it already
     has".
   - part_a.py:810–811 (Context Map, "Identify each model in play, including the
     implicit models of", p. 213). Replace with "List every model the project really
     uses, counting the unstated models inside subsystems that are not
     object-oriented,".

## SHOULD-FIX

1. **part_a.py:796–797.** "the last line of the Context Map pattern" is wrong: it is
   the last line of the pattern's boxed statement, and the pattern runs on for three
   pages. Read "the last line of the Context Map pattern's statement".
2. **part_a.py:596–599.** "the merge removed a term" sits beside a list of two terms
   given up. The till half gave up `customer`, `reduced-rate` and its snack sense of
   `concession`, and `kiosk-sale` was added, so the net is 7 → 6. Read: "Notice who
   gave way: the till half gave up `customer`, `reduced-rate` and its snack sense of
   `concession`, now `kiosk-sale`; the web half nothing."
3. **part_a.py:1121–1122 and 1199.** The body says a kernel "has no downstream", but
   the worked `after` says "no upstream". Use "neither side is upstream of the other"
   in both.
4. **part_a.py:1403–1405.** "its 3 models change because they are the old model" is
   true only of the box office and marketing. Finance is the box office's customer.
   Read: "…because the box office takes the old model as it is, and marketing and
   finance build on the box office's."
5. **The downstream's own layer is never counted** (kit-report, family B
   deviations). In `change-programming` (L3) the box office's model changes, but its
   layer for payments is not listed. The same happens in `before`/`after` (L8) with
   marketing's layer for membership. Evans's layer translates both ways (p. 227), so
   its own side may need changing. Add to the L3 note: "Nor does it count a
   downstream's own layer when that downstream's model changes: the box office's layer
   for payments may need its box-office side rewritten."
6. **part_b.py:226.** "the XML schemas the chapter is excited about". Evans gives the
   excitement to "the world of e-commerce" and himself calls XML's schemas a valuable
   feature (p. 232). Read "the XML schemas the chapter points to".
7. **part_a.py:1079–1082.** The sentence makes limited functional integration one of
   three alternative causes. In the book it is the condition, and skill, politics or
   size make it worse (p. 220). Read: "Shared Kernel starts where functional
   integration is limited and Continuous Integration costs more than it returns,
   especially when the team is too big or lacks the skill or the political
   organisation…"

## NOTE

- **Accuracy otherwise holds.** Every other claim I checked matches its pages: the
  charge story, the Modules sidebar, the two levels of Continuous Integration, the
  map's "dragon", the Customer/Supplier example, Conformist's sidebar, the layer's
  parts, the Great Wall, the insurance project, CML, the elephant, the strategy
  guidelines and the four game plans.
- **Fairness.** The course is fair where Evans is. Conformist's case ("chosen less often
  than it should be", "dragged into a better design"), the cost of Separate Ways, the
  Great Wall's cost and "integration is always expensive" are all stated.
- **Quizzes.** I tried to argue for every wrong answer and could not. The closest is
  3.2's "repair the splinter before going on", which the book's "finish describing
  everything" rules out.
- **Labs are tied to the argument**, and each lesson closes on the gap in its `note`.
- **Kit (not the author's to fix):** the status line forms the possessive as
  "payments’s" and "tickets’s".
- part_a.py:286–287: "not in the code" slightly overstates p. 208; acceptable.

**Verdict:** accurate, well taught and gate-clean. Fix the Context Map omission, the
one-way figures the lab cannot show, the DB2 story, quiz 8.2's `why` and the
boxed-statement paraphrases before publishing.
