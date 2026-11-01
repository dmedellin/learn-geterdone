# Review (accuracy and teaching): Design Patterns, Course 4 — Structural Patterns

Course: `gof-structural` (`content/design_patterns/c4_structural/`, `__init__.py`,
`part_a.py`, `part_b.py`), eight lessons, plus the `# Structural Patterns` block of
`content/spoken/design_patterns.py`. Built to `docs/design-patterns/PLAN.md` §C
Course 4 and `docs/design-patterns/AUTHORING.md`. Reviewed 2026-11-01 against the
private extraction of the operator's copy (PDF page = printed page + 20). I checked every claim against its pages with `book.py`/`page.py`; I read neither the
book whole nor `site/`, and wrote only this file.

## Gates

- **Preview:** `python3 scripts/preview_subject.py design_patterns --course gof-structural --out …/scratchpad/rev/gof-structural`
  rendered 9 pages. Labcheck: 8 executed, 8 with pinned figures, 0 failing. **OK**.
- **`quotes.py`: 8 quotations, all OK**, each with its PDF page right: Adapter p. 157
  (15 words), Bridge p. 171 (13), Composite p. 183 (11), Decorator p. 195 (10), Facade
  p. 205 (12), Flyweight p. 215 (10), Proxy p. 227 (13), Discussion p. 239 (16). The one
  other quoted word, "adorners" in Decorator, is on p. 199 (ELSEWHERE only because the
  lesson's dict cites p. 195). No lesson goes over 40 words or 60.
- **`overlap.py … 8`:** the only runs are the book's title (in the attribution) and the
  eight counted quotations. Clean.
- **Browser (Playwright, chromium, `file://`).** All eight lessons at 375 px and 1280 px:
  scrollWidth equals clientWidth everywhere, with no page or console errors. I loaded
  every preset (19) and every tile matches the body prose, the worked lines and the pins.
  I also typed in all eight exercises, and in each the lab agrees with the quiz `why`.
- **Spoken forms.** The block has **32** entries, not 33. Every key is a whole
  worked or key line. None is a key in another Subject's spoken file, and none
  appears as a line on another Subject's pages. The bare sums inside them (`3 × 3 = 9`,
  `3 × 2 = 6`, `9 + 1 = 10`) do appear elsewhere, but the keys are the whole lines with
  their labels, so nothing collides. `speechcheck.py` reports 0 unresolved for
  design-patterns. The readings are right except the Flyweight formula (MUST-FIX 2).

## MUST-FIX

1. **`part_a.py:1016` and `:1021–1022`, Composite quiz 1.** The `why` says "28.3 leaves
   out the cookies packed straight into the order", but 32.5 − 6.5 = 26. The figure 28.3
   is 32.5 − 4.2, which leaves out the rye. The explanation of the distractor is false.
   Replace the fourth option with `"7 calls, depth 2, 26 kg"` and the last sentence of
   the `why` with: "Six is the forwarded calls without the client's; 26 leaves out the
   cookies packed straight into the order."

2. **`part_b.py:155` (Flyweight key line) and `content/spoken/design_patterns.py:132`.**
   The key line `saving: N × (I + X) less F × I + N × X` leaves out the reference per
   object that the lab, the body, the steps and the worked lines all count. On
   `plants-stored` the line gives 1,937,408 where the lab prints 1,933,608. On
   `name-tags` it gives 0 where the lab prints −12, and that negative result is the
   lesson's own counter-example. The spoken form, "less F times I plus N times X", is
   also ambiguous: it can be heard as (N(I+X) − F·I) + N·X. Replace the key line with
   `saved: N(I + X) − (F·I + N·X + N·R)` (37 columns). Replace the spoken entry with
   `"saved: N(I + X) − (F·I + N·X + N·R)": "saved, N times the sum of I and X, minus the sum of F times I, N times X and N times R"`.

3. **`part_a.py:1437–1440`, `:1469–1472`, `:1599–1602`, Facade: the Sample Code's
   "warning" is overstated.** The lesson says "every extra parameter the facade takes to
   be flexible works against its purpose", and the first mistake says "Each parameter
   added for flexibility works against the facade's purpose, the authors warn". The
   Sample Code (PDF p. 209) *proposes* a CodeGenerator parameter for the Compiler
   constructor as reasonable when there is more than one target. It adds only that
   parameterizing the other participants as well "adds flexibility" but detracts from the
   mission of simplifying the common case. Replace the clause at 1438–1440 with: "and
   ends by weighing a parameter for the code generator, sensible if there is more than
   one target, against parameterizing every participant, which adds flexibility but
   works against the facade's purpose of simplifying the common case." At 1600–1602, use:
   "A parameter or two can earn its place, as the code generator does in the authors'
   Sample Code; parameterizing every participant, they note, detracts from the facade's
   purpose, which is to make the common case simple. A client that needs the options can
   use the subsystem's classes directly." At 1471–1472, change "which is the Sample
   Code's warning" to "which is the trade-off the Sample Code ends on".

## SHOULD-FIX

1. **Near-runs on Intent and Applicability (PLAN §5).** These are 5–7-word stretches
   that follow the book closely in the sections the plan protects most. Reword them:
   - `part_a.py:1403–1404`, Facade Intent, second sentence: "a higher-level one that
     makes the subsystem easier to use". This is close to verbatim, next to the counted
     first sentence. Suggest: "the second says the facade works a level above those
     interfaces, so the subsystem is simpler to work with."
   - `part_b.py:197–202`, Flyweight Applicability: "their sheer number makes storage
     expensive" and "many groups of objects can be replaced by relatively few shared
     ones". The second is nearly the bullet itself. Suggest: "storing them all is costly
     simply because there are so many; … once it is, a few shared objects can stand in
     for large groups of them".
   - `part_b.py:462–464`, Proxy Applicability, "a local representative for an object in
     another address space" (7-word run), and the Protection proxy concept at `:440–441`,
     "should have different access rights for different callers". Suggest "a stand-in on
     this side for an object that lives in another address space" and "for objects whose
     callers are allowed different things".
   - `part_a.py:611–612`, Bridge Applicability: "should not have to be recompiled" and "you
     want to hide the implementation from clients". `part_a.py:888–889`, Composite: "be
     able to ignore the difference between". Each is milder, but each is a bullet's
     phrasing. Recast them in the lesson's own words.

2. **`part_b.py:201–202`, Flyweight's identity condition.** "since a shared object is
   identical to itself in every context where it appears" is circular, and it misses the
   book's point (p. 217): identity tests return true for objects that are conceptually
   distinct. Suggest: "since two occurrences that share a flyweight are one object, and
   an identity test cannot tell them apart."

3. **`part_a.py:300–301`, the chapter introduction.** "the class form of Adapter is the
   chapter's example" is not quite the book's order. The introduction's first example is
   multiple inheritance mixing classes into one, and the class adapter is "another
   example" (p. 157). Suggest: "multiple inheritance is the first example, and the class
   form of Adapter the second".

4. **`part_b.py:766–769`, the Discussion lab.** "read the same records as Adapter if the
   renderers were a library you found later and wrapped. The lab cannot tell the
   difference, because there is none in the classes." Under the Adapter reading, the
   concrete renderers are adapters over library classes that the count leaves out. Say
   so, or the claim reads stronger than the count: "…wrapped; the two concrete renderers
   are then adapters, the library's own classes sit outside the count, and the viewer's
   classes are the same seven."

## NOTE

1. The class-adapter sketch names its class `JetPrinter` (`part_a.py:67`), while the lab's
   class adapter for the same vendor class is `JetAdapter`, which is also the object
   adapter's name in the first sketch. Readers can follow it, but naming the sketch
   `JetClassAdapter` would line it up with the records.
2. Java sketches: all eight show the right participants with the reference in the right
   direction, and in my reading they compile as Java 8, given the undeclared domain types.
3. Proxy Known Uses (`part_b.py:492`) say "the editor's image proxy". The book (p. 236)
   attributes the Motivation's virtual proxy to ET++'s text building-block classes, so
   "ET++'s image proxy, the Motivation's source" would be more exact.
4. Proxy's archive scans are images loaded on demand, which is close to the Motivation's
   idea, but the domain (a library archive, not a document editor) is the lesson's own,
   so PLAN §C is met. No lab uses a book example's data.
5. A 6-word run, "extrinsic state is computed or stored" (`part_b.py:216–217`), is a
   technical phrase below the scanner's limit.
6. Teaching: every lesson states liabilities beside benefits. Examples: the class and
   object adapters' opposite costs, Bridge's degenerate case, Composite's
   over-generality, Decorator's identity and many-objects liabilities, Facade's
   parameter creep, Flyweight's run-time cost, Proxy's indirection. Every lesson closes
   on the gap between the count and the decision. Each lab's count is tied to the
   pattern's consequence and is not decoration. Apart from MUST-FIX 1's explanation, I
   could not make a case for any wrong quiz answer.
7. Every other claim I checked against its pages is supported, including each pattern's
   Applicability, Consequences, Implementation issues, Known Uses and Related Patterns as
   the lessons summarise them.

**Verdict:** accurate, well-taught and clean on the gates; fix the three MUST-FIXes
(a false distractor explanation, a key-line formula that disagrees with the lab, and an
overstated Facade warning) before release.
