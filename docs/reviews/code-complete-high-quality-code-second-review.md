# Second review (accuracy): Code Complete, Course 2 — Creating High-Quality Code

Course: `code-complete-high-quality-code` (`content/code_complete/c2_high_quality_code/`,
`__init__.py`, `part_a.py`, `part_b.py`), nine lessons. Brief:
`docs/code-complete/SECOND-REVIEW.md`. Reviewed 2026-10-25 against the private
extraction of the second edition (printed page = PDF page − 37), reading the
passages behind every sentence that says what McConnell argues, reports or
recommends, with `ccbook.py` and a narrow page-window reader, never the file whole.

**Scope note.** The orchestrator told this reviewer to write only this file and not
to edit lessons, so nothing in the course or in PLAN §C was changed. Every finding
below is a recommendation, with the replacement text where the fix is mechanical.

## Gates

- **Preview:** `python3 scripts/preview_subject.py code_complete --course code-complete-high-quality-code`
  → 10 pages; labcheck 9 executed, 9 with pinned figures, 0 failing; **OK**.
- **`labcheck.js --observe`:** every preset's tiles match the body prose, the worked
  lines, §C and my hand count: `everything-talks` 5 / 20 / 10 / 1 = 100% / fan-in
  billing 4 (five-way tie, named in the banner); `layered` 7 / 7/10 = 70% / fan-out
  billing 2 / fan-in db 3; `strict-layers` 5 / 1/2 = 50% / ui 2 / db 2; `exposed` 5
  direct, 6 reached; `hidden` 1, 7; `public-fields` 5, 5, 2, 2; `private-fields` 5, 0,
  4, 3; `kitchen-sink` 9, 2, 6, 6; `shallow` 2, Circle, 4, 3; `deep` 7,
  ChristmasHolidaySavings, 8, 2; `copied` 1 / 6 / lines 3–5 and 7–9; `extracted` and
  `two-names` 0; `nine-parameters` 10 / 9 / 8 / 1 / 0 / 9 / 1/8 = 12.5%;
  `parameter-objects` 6 / 5 / 4 / 1 / 0 / 3 / 1/4 = 25%; `correct`, `never-fires`,
  `always-fires` as the body states; `mixed`, `barricaded`, `checks-everywhere` as the
  body states; `free-slot` 5 / 7 / line 14 / 3 lines under line 8; `complete` 5 / 8 /
  none.
- **Browser (Playwright, served locally), every exercise typed in as the body asks:**
  six all-talking modules 6 / 30 / 15 / 1 = 100%; layered 6 / 2/5 = 40%, fan-in
  `stock` 2; the date exercise as records 3 direct before, 1 (`parseDate`) after;
  `Point` 3 fields, 2 public; the `MAX`/`name`/`age` class 3, 1; the `Puppy` hierarchy
  5 at Puppy; `C, B; …` 4 at F; `printSummary` 1 block, 4 lines, lines 4–5 and 8–9;
  `schedule` 8 parameters; `score >= 0 || score <= 100` (valid, 0–100) disagrees on
  −1 and below, 101 and above, exposed −1, 101; `qty > 0 && qty < 99` (valid, 1–99)
  disagrees on 99; the barricade quiz records 1: c / 1: a / 0 / 1: b; the nine
  exercise values with the answer's handling, all four lists 0: none;
  `expireSessions` 4 steps, empty line 10; the three-comment quiz routine 3 steps,
  1 empty. Every one agrees with its quiz `why`. Each exercise's answer appears on
  the page only in the quiz (options and `why`), never in body prose.
- **Snippets against §D.4 / `presets.py`:** `FREE_SLOT`, `PRIVATE_FIELDS`,
  `KITCHEN_SINK`, `PRINT_SUMMARY_EXERCISE`, `EXPIRE_SESSIONS_EXERCISE` are
  byte-identical to §D.4; `PUBLIC_FIELDS`, `COPIED`, `EXTRACTED`, `TWO_NAMES`,
  `NINE_PARAMETERS`, `PARAMETER_OBJECTS` are verbatim in `presets.py`. `COMPLETE` is
  `FREE_SLOT` plus the one line §C names. Every preset's code is the same constant as
  a body `code` block.
- **`# F` comments: 4** — F6 (pp. 143–144, Abstract Data Types), F7 (p. 147,
  Inheritance), F8 (pp. 173–174) and F9 (p. 178), both Routine Length. Each checked on
  its page; no book figure in the course lacks one. (The 39 percent interface-error
  figure on p. 174 is not used, rightly: it is not in §S.2.)
- **`cc_quotes.py`: 17 quotations, all OK.** L1 p. 123 (17) + "No Silver Bullets"
  p. 77 (3) = 20; L2 p. 123 (17) + Brooks p. 92 (10) = 27; L3 p. 160 (15); L4 p. 160
  (13) + Bloch p. 144 (8) + "grossly optimistic" p. 147 (2) = 23; L5 p. 186 (20) +
  "illogical cohesion" p. 170 (2) = 22; L6 p. 186 (23); L7 p. 213 (19) + "Garbage in,
  garbage out" p. 188 (4) = 23; L8 p. 205 (24) + "Dog Breath" p. 210 (2) = 26; L9
  p. 234 (28) + "Just One More Compile" p. 231 (4) = 32. Every opening quotation is
  §C's **Quote**; all within 40 and 60. The extra phrases are short identifying
  phrases or quotations-within-the-book attributed to their authors (Brooks, Bloch),
  each with its page in the dict comment.
- **`speechcheck.py`:** code-complete 0 unresolved. The read-out of every code line,
  backtick run, key line and worked line was generated with `speech.say_code` /
  `say_code_block` and read: every `&&` and `||` is said "and" and "or"; there is no
  prefix `!` in the course; `%` in code is "mod"; code-block lines are announced by
  number, and the flagged line 14 / line 15 is announced "flagged". No negation is
  dropped. One kit fault found (finding 7).

## Findings

Ranked **must-fix** (a claim about the book or the code that is wrong),
**should-fix**, **consider**.

### Must-fix

1. **Routine Length and Parameters — the studies of routine length are misreported,
   and the reason for "care past 200" is wrong.** The body says the studies "do not
   say what you might expect: several found larger routines no more error-prone than
   small ones, and some found them cheaper", and that past about 200 lines you should
   be careful "because none of the studies looked beyond it"; quiz item 3's `why`
   repeats "because the studies the book cites did not distinguish sizes beyond it".
   On p. 174 the book's reason is narrower: none of the studies *that reported lower
   cost or lower error rates with larger routines* distinguished sizes above 200. One
   study it cites did look beyond: the IBM study (Jones 1986a, the very citation the
   lesson names as the end of its range) found routines over 500 lines the most
   error-prone, with errors rising with size past 500. As written, the lesson both
   drops the one finding against long routines and invents a gap in the evidence.
   (§S.2 F8 is right; the prose is not.) Replace the body sentences with:

   > Section 7.4 reviews the studies, which the book cites from Basili and Perricone
   > (1984) to Jones (1986a), and most do not say what you might expect: several
   > found larger routines no more error-prone per line than small ones, and some
   > found them cheaper to develop; one, at IBM, found routines over 500 lines the
   > most error-prone. The book's conclusion is that a routine with a complex
   > algorithm may be allowed to grow organically up to 100 to 200 lines, a line
   > being one that is neither a comment nor blank, and that past about 200 you
   > should be careful: none of the studies that favoured longer routines
   > distinguished sizes beyond 200, and somewhere past it a routine becomes hard to
   > understand.

   and the quiz-3 `why` with: "Up to 100 to 200 lines, a line being neither a comment
   nor blank (pp. 173–174), with care past 200, because none of the studies that
   found longer routines cheaper or less error-prone distinguished sizes beyond it.
   One screen is the traditional figure the section reports and does not adopt." The
   `note`'s "the evidence it reviewed did not find small routines less error-prone" is
   defensible for 100–200 lines (the book says routines of that length are no more
   error-prone than shorter ones) but should say so: "did not find routines of 100 to
   200 lines more error-prone than shorter ones".

2. **Assertions and Error Handling — `mistakes[2]` misdescribes its own preset.**
   "Testing only values inside the range": "A check that accepts 5 and rejects 50 can
   still be wrong at either end. On the lesson's illustration, `never-fires` looks
   fine on any valid month and fails only on 0 and 13, the values just outside." Both
   halves are wrong about `never-fires`: it rejects nothing (it is never true, so 50
   passes as valid), and it is wrong on every invalid integer — the lab's own tile on
   the same page prints "0 and below, 13 and above", and the worked example says
   "every invalid month passes". Any out-of-range value, 50 included, exposes it, so it
   is exactly the bug that does *not* need a boundary test. The refutation needs a
   check that is wrong only at an end. I typed `month < 1 || month > 13` into the lab
   (range 1–12, true means invalid): it disagrees on 13 alone, and only the boundary
   test 13 exposes it. Replace the body of `mistakes[2]` with:

   > A check that flags 0 and 50 can still be wrong at an end. Type
   > `month < 1 || month > 13` into the lab: it flags 0 and 50 correctly, lets 13
   > through, and only the boundary test 13 shows it. The boundary tests exist to
   > try exactly the values next to each end.

   (The quiz-3 item, `qty > 0 && qty < 99`, is the same kind of bug and is right.)

### Should-fix

3. **Design Heuristics and Information Hiding — "two amounts of design are wrong every
   time" is section 5.5 (p. 119), not 5.4.** The body puts it in the §5.4 paragraph
   ("How much design is enough? A judgement call, it says, but two amounts are wrong
   every time … Section 5.5 adds that dogmatic adherence …"), and quiz item 3's stem
   asks "According to section 5.4". Section 5.4's "How Much Design Is Enough?"
   (p. 115) is the table of factors; the "every last detail / nothing at all" sentence
   and Plauger's line on dogma are both on p. 119, inside §5.5 (which begins p. 118).
   Fix: the stem "According to section 5.5, which two amounts of design are wrong every
   time?"; in the body, end the §5.4 sentence at "capture the design cheaply, in
   comments, on a wiki, in photographs of a whiteboard", and make the last two
   sentences: "Section 5.5, on methodologies, comes back to how much design is
   enough: a judgement call, it says, but two amounts are wrong every time, designing
   every last detail and designing nothing at all, and dogmatic adherence to any one
   method hurts."

4. **Design Heuristics and Information Hiding — "complex data structures" is not on
   §5.3's list of areas likely to change.** The list on pp. 98–99 is business rules,
   hardware dependencies, input and output, nonstandard language features, difficult
   design and construction areas, status variables and data-size constraints.
   "Complex data types" is on a different list, §6.4's reasons to create a class
   (p. 153). Fix: "Business rules, hardware dependencies, input and output, status
   variables and data-size constraints are on its list of the usual suspects."

5. **Design Heuristics and Information Hiding — "and says plainly that its items
   overlap" is not on the page.** I searched §5.3 (pp. 87–110) for overlap, related,
   distinct, exclusive, redundant and similar wording; the nearest is p. 108, that
   modularity is related to information hiding and encapsulation, which is not a
   statement about the list. Fix: delete the clause ("Section 5.3 gives a list: find
   real-world objects; …").

6. **Assertions and Error Handling — key line "a check needs both ends joined by &&"
   is false for the lesson's own correct check.** The `correct` preset,
   `month < 1 || month > 12`, joins its ends with `||` and is right; the `steps` say
   so ("a check that it is outside joins them with `||`"). The key line states half the
   rule as the whole. Fix: `inside a range: join both ends with &&` (38 characters;
   read "inside a range, join both ends with and").

7. **Read-out (kit fault, `scripts/mathpath/speech.py`, the string branch of
   `say_code`): a string literal of only spaces or punctuation is read "the empty
   string".** `" "` (one space) and `": "` both collapse to nothing and are spoken
   "the empty string", and `"%,.2f"` is spoken "of,.2f". In this course:
   Reasons to Create a Routine, `copied` lines 5 and 9, `extracted` line 9,
   `two-names` lines 5 and 9 ("print line A dot city plus the empty string plus A dot
   postcode"), `printSummary` lines 4, 5, 8 and 9; Routine Length, `nine-parameters`
   lines 8 and 9 and `parameter-objects` line 5. A listener is told the label prints
   city and postcode run together, which is not what the code does. It is not a
   dropped negation, but it misreads code. Kit fix: speak a literal whose text has no
   speakable characters by its characters ("a space", "colon space"), and a format
   string by its characters. Course workaround until then: `say_code_block` takes
   overrides keyed by the exact line, so a Course 2 block in
   `content/spoken/code_complete.py` can give these eight distinct lines a spoken
   form (e.g. `    System.out.println(a.city() + " " + a.postcode());` → "print line
   a dot city, plus a space, plus a dot postcode").

8. **Design Challenges and Complexity — Brooks's essay is "No Silver Bullet",
   singular.** The body puts "No Silver Bullets" in quotation marks as the essay's
   title. That is how the book's citation prints it (p. 77, so `cc_quotes.py` passes),
   but the essay's title is singular, and §S.1 lists it so ("No silver bullet:
   essence and accidents of software engineering", *Computer* 20(4), 1987). A title
   is a fact about Brooks, not a quotation of McConnell. Fix: "Fred Brooks's essay
   <em>No Silver Bullet</em> (1987)", and drop the three words from the dict
   comment's quotation count (lesson total 17).

### Consider

9. **Inheritance, Containment and Members — §6.3's summary is compressed past what
   it says.** "Contain when classes share data, inherit when they share behaviour and
   an interface" makes containment the rule for shared data, but p. 149 says to
   inherit when classes share data *and* behaviour; containment is for shared data
   without behaviour (which quiz item 4 gets right). Suggest: "contain when classes
   share only data; inherit when they share behaviour, or when the base class should
   control the interface."

10. **Routine Length and Parameters — §7.6's "strict sense" is the purists'.** "A
    function, in the strict sense, takes input and returns one value through its
    name" is the position p. 181 gives to purists before it qualifies it. Suggest:
    "Purists, the section says, would have a function take only input and return one
    value through its name, as `sin` or `screenHeight` do."

11. **Abstract Data Types and Interfaces — a hedge dropped.** "A class, he says, is an
    abstract data type plus inheritance and polymorphism": p. 133 offers it as one way
    of thinking of a class. Suggest "One way to think of a class, he says, is as …".

12. **Reasons to Create a Routine — exercise items 4 and 5 track the book's own
    examples.** Item 5 (name, then date, in the order the form shows them) is the
    shape of the book's procedural example (p. 170: name, address, phone in the order
    of the input screen), and item 4 is close to its temporal `Startup()` example
    (p. 169). §C replaced items 1 and 3 for exactly this reason. Not a copyright
    problem (one-line descriptions, no listing), but a reader with the book open can
    look the answers up. Suggest an item 5 of the lesson's own, e.g. "prints a
    shipping label and then writes a line to the dispatch log, in the order the
    warehouse procedure lists them, with nothing passed between the two."

13. **Reasons to Create a Routine — quiz item 1's reason against "coincidental".**
    "These three are at least all documents" argues from what the operations are; the
    chapter's mark of logical cohesion is that a flag passed in selects the operation
    (p. 170), which the book says ties otherwise unrelated operations together. Suggest:
    "Coincidental cohesion has no tie at all; here a flag passed in picks the
    operation, which is what makes it logical (p. 170)."

14. **Design Challenges and Complexity — `strict-layers` is not strictly layered.**
    The label and body say each module uses only the layer below, but `billing, db`
    skips `stock`'s layer (`orders` and `billing` sit above `stock`). The figures are
    right; the description is not. Suggest the label "Strict layers: each module uses
    fewer modules, all below it" and in the body "each module talks only to modules
    below it, and to fewer of them".

15. **Exceptions and Barricades — `mixed`'s `taxRate, inside` against the exercise's
    configuration tax rate, outside.** The pedagogy review ranks this must-fix; I would
    rank it should-fix (no claim about the book is wrong, but a reader sees two
    placements of a "tax rate" on one page with nothing saying they are different
    values). Its option (a), renaming to `taxDue` in all three presets and re-pinning
    `checks-everywhere` to "3: lineTotal, customerId, taxDue", is the cleaner fix.

16. **Abstract Data Types and Interfaces — `mistakes[0]` gives away part of exercise
    (a).** It says, after Riel, that a `Point` with get and set routines encapsulates
    its representation, which is most of the answer to "what would a caller need if
    `x` and `y` were made private". It is the book's own concession and §C asks for it;
    if it stays, the exercise prompt could ask for the routines a caller needs *and
    which of them it should not get* (a setter the callers do not use), so the quiz
    still tests something.

17. **Read-out (kit): records lose their semicolons.** `ui, api; api, orders; …` is
    spoken "ui, api api, orders …", so a listener cannot tell where one record ends.
    Affects every records backtick run in lessons 1, 2, 4 and 8. Kit: read `;` between
    records as a pause word ("then") or a full stop.

18. **Inheritance — private inheritance is C++.** Agreeing with the pedagogy review's
    item 9: one clause that Java has no private inheritance (§F.6).

### Checked and right

- Lesson 1: Rittel and Webber's definition (p. 74); Tacoma Narrows, 1940, aerodynamics
  (p. 74); school problems rarely wicked, professional work the everyday reality
  (p. 75); three designers, three acceptable designs (p. 76); 5.1's headings —
  sloppy, nondeterministic, heuristic, emergent (pp. 75–76); Brooks after Aristotle,
  accidental difficulties addressed long ago (p. 77); the root of the essential
  difficulties is complexity, and projects that fail technically fail from
  uncontrolled complexity (p. 78); Dijkstra's skull (p. 79); the two prongs; fan-in and
  fan-out definitions (p. 80); six subsystems, the hoses, need-to-know, restrict early
  (pp. 83–84); acyclic system diagram (p. 85). Every count, and "thirteen of the twenty
  uses and three of the ten pairs".
- Lesson 2: the heuristic list (headings, pp. 87–108 and the summary p. 108); Brooks's
  retraction in the 20th-anniversary edition and Boehm on rework in high-change
  environments (p. 92); the barriers, including indirection as premature (pp. 95–96);
  wiki and digital-camera capture (pp. 117–118); top-down and bottom-up as not
  competing (p. 113).
- Lesson 3: the font example (pp. 126–128); "carrying cases for loosely related data"
  for `mistakes[2]` (p. 126); Riel's `Point` (p. 139); semantic violations and
  "programming through the interface" (pp. 141–142); F6 including the high and low end
  of 7±2 (pp. 143–144). Quiz 2's `static final` field: the lab prints 3 fields, 1
  public, as the `why` says.
- Lesson 4: containment as the workhorse, inheritance trickier "not because it's
  better" (p. 143); private inheritance as a last resort (p. 143); LSP after Liskov,
  Hunt and Thomas's summary, the `InterestRate()` sign example (pp. 144–145); F7 and
  the 7±2-for-subclasses remark in quiz 3's `why` (p. 147); "heavy bias against
  inheritance" and the summary (p. 149); Demeter after Lieberherr and Holland
  (p. 150); Java packages (p. 157). The `Square` traces: both overrides give 25; one
  override gives 20, as the `why` says.
- Lesson 5: routine as the greatest invention after the computer (p. 163, no hedge in
  the book); the undergraduate textbook (p. 163); "the single most important reason"
  (p. 164); the eight-line abstraction example (p. 164); "To ensure all routines are
  small? No" (p. 166); the dozen-place conversion (pp. 166–167); "the most popular
  reason" for avoiding duplication; cohesion as the workhorse heuristic at the
  routine level after Stevens, Myers and Constantine (p. 168); the kinds and the
  event-handler exception (pp. 168–170); "learn the ideas" (p. 171).
- Lesson 6: the Pilgrims (p. 173); F8, with the complex-algorithm qualifier and the
  line definition (p. 174); interfaces as among the most error-prone areas (p. 174);
  F9 after Miller (p. 178); the status-returning function accepted if used
  consistently, McConnell preferring the explicit status variable (p. 181); the §F.4
  aside, in the `note`, both positions at strength and unsettled. Java claims (no
  in/out keywords; `final` on a parameter) correct. `NINE_PARAMETERS` and
  `PARAMETER_OBJECTS` compile as fragments.
- Lesson 7: defensive driving (p. 187); garbage in (p. 188); the three ways to handle
  garbage, and not inserting errors (p. 188); the §8.2 rule (p. 191); design by
  contract after Meyer 1997 (p. 192); assert and handle anyway, for large,
  long-lasting systems (p. 193); the 8.3 techniques, the video game and the X-ray
  and radiation machine (pp. 194–197); robustness and correctness, safety-critical
  and consumer (p. 197). Java's `assert` and `-ea` correct. All three presets' tiles
  and the worked lines.
- Lesson 8: exceptions that cannot be ignored and weaken encapsulation (p. 199); the
  guidelines including the `GetTaxId()` / end-of-file example (pp. 199–203); hull
  compartments, firewalls, the operating room, converting input (pp. 203–204); bad
  data inside is an error in the program (p. 205); offensive programming after Howard
  and LeBlanc (p. 206); the §8.7 list and Pathfinder's debug code left in by design
  (pp. 209–210); "Dog Breath" (p. 210); fat and slow, and defensive code not immune
  to defects (p. 210). Java checked exceptions correctly stated.
- Lesson 9: "my favorite" (p. 217); the class and routine figures (pp. 216–217);
  pseudocode guidelines and benefits (pp. 218–220); "nothing is ever right just
  because it seems to work" (p. 230); compile once convinced, "Just One More Compile"
  (p. 231); the four alternatives with Beck 2003, Fowler 1999, Meyer 1997, and
  forgetting part of a routine hardly ever happening with the PPP (p. 233). The
  `expireSessions` `why`: on an `ArrayList`, removing inside an enhanced `for` throws
  `ConcurrentModificationException` on the next `next()`, except that removing the
  second-to-last element makes `hasNext()` false and silently skips the last — both
  as stated. `free-slot`'s counts by hand: steps at 3, 5, 8, 14, 15; statement lines
  4, 6, 7, 9, 10, 11, 16; three under line 8.
- Voice: three scene openings of nine (lessons 3, 6, 9); one modern aside, in the
  lesson §F.4 names; no language wars; every count presented as a reason to look;
  every misconception refuted from the chapter, lab runs introduced as the lesson's
  illustration. No verdict for or against McConnell in the lesson's voice.

## Claims not settled against the page

- "Says plainly that its items overlap" (lesson 2): not found; searched §5.3,
  pp. 87–110, for overlap / related / distinct / exclusive / redundant / similar /
  cousin / one another (finding 5 recommends deleting it).
- Brooks's title: settled from §S.1 and the bibliography form the PLAN records, not
  from a fetch of the original paper (finding 8).
- "It also makes poor comments, since it repeats the code" (lesson 9, `mistakes[1]`):
  p. 218–219 say language-level pseudocode loses the benefit of design at a higher
  level and that good pseudocode makes good comments; the "repeats the code" reason is
  a fair inference, not a sentence on the page. Left as it is.

## Disagreement with the pedagogy assessment

Written after my findings above, then compared with
`docs/reviews/code-complete-high-quality-code-pedagogy-review.md`.

- **"Nothing here is a must-fix in the sense of a lesson that misteaches."** I
  disagree on two counts. Routine Length misreports the evidence §7.4 reviews and
  gives a wrong reason for care past 200 (finding 1), and Assertions and Error
  Handling's `mistakes[2]` says `never-fires` fails "only on 0 and 13" while its own
  lab prints "0 and below, 13 and above" (finding 2). The assessment praised the
  `cond/range` presets and the worked example, rightly, but did not read the third
  misconception against them.
- **"The two positions always wrong (p. 119)" checked as stated.** The words are
  right; the lesson's attribution to section 5.4, in the body and in a quiz stem, is
  not (finding 3).
- **Its must-fix 1 (`taxRate`).** Agreed that it should change, and its option (a) is
  the right one; I rank it should-fix, since nothing the page says about the book is
  wrong (finding 15).
- **Its must-fix 2 (quiz pins the `kitchen-sink` grouping).** Partly agreed. §C makes
  "three classes" the exercise's **Answer** and §B requires a quiz item that asks for
  it, so the item is not a stray verdict; but a reader who keeps the audit log with
  ticketing has a defensible reading. Its proposed `why` sentence ("by the names
  alone; … a design decision, not a counting error") fixes it without dropping the
  grouping from the quiz.
- **Its should-fix 3 (the article "a" read as the letter).** Agreed, and the same
  kit function has a worse fault it did not report: string literals of spaces or
  punctuation read as "the empty string" (finding 7).
- **Its should-fix 5 (the parcel item could be functional).** Agreed, and it is an
  accuracy point as well: by p. 168's definition, a routine whose steps together make
  one complete function (choose a box) is functional, so the item as written has two
  defensible answers.
- **Its consider 9 (private inheritance is C++).** Agreed (finding 18).

## Summary of must-fix findings

1. **Routine Length and Parameters:** the body and quiz-3 `why` say none of the
   studies looked past 200 lines and omit the IBM study (Jones 1986a) that found
   routines over 500 lines the most error-prone; p. 174 says only the studies favouring
   longer routines did not distinguish sizes above 200. Replacement text above.
2. **Assertions and Error Handling:** `mistakes[2]` says `never-fires` fails only on 0
   and 13 and pairs it with a check that "rejects 50"; it rejects nothing and is wrong
   on every invalid integer, as its own lab shows. Use `month < 1 || month > 13`,
   which the lab shows is wrong on 13 alone.

Should-fix in brief: §5.5 not §5.4 for "two amounts always wrong" (body and quiz
stem); "complex data structures" is not on §5.3's list; delete "says plainly that its
items overlap"; the `&&` key line; the kit reads `" "` and `": "` as "the empty
string"; Brooks's title is singular.

## Author's response

All findings were applied except 7 and 17, which are kit faults left to the renderer engineer, and 16, which is kept as it is (reason below). The preview re-ran OK: 9 pages with pinned figures, 0 failing.

**Must-fix**

1. **Done.**
   - The §7.4 paragraph now uses the reviewer's text. It names the IBM study (routines over 500 lines most error-prone) and gives the narrower reason for care past 200.
   - The quiz-3 `why` was replaced as proposed.
   - The `note` now says "did not find routines of 100 to 200 lines more error-prone than shorter ones".
2. **Done.**
   - `mistakes[2]` uses the reviewer's body, with the title changed to "Testing only values far from the ends".
   - Checked in the lesson's own lab configuration (range 1–12, true means invalid): `month < 1 || month > 13` gives `cdDisagree` 13 and `cdExposed` 13.

**Should-fix**

3. **Done.** The body now ends the §5.4 paragraph at the whiteboard. The "two amounts" sentence now sits with §5.5, as proposed. The quiz stem reads "According to section 5.5". The dict's source comment is corrected too.
4. **Done.** The list now reads: business rules, hardware dependencies, input and output, status variables and data-size constraints.
5. **Done.** The clause is deleted.
6. **Done.** The key line is now "inside a range: join both ends with &&", read "inside a range, join both ends with and".
7. **Left to the renderer engineer**, at the coordinator's direction (the `say_code` string branch). No course-level override was added, so there will be no override to remove once the kit is fixed.
8. **Done.** The body now reads "<em>No Silver Bullet</em> (1987)". The dict comment no longer counts the title as a quotation, and the lesson total is now 17 words.

**Consider**

9. **Done.** The body now says: contain when classes share only data; inherit when they share behaviour, or when the base class should control the interface.
10. **Done.** The body now says: "Purists, the section says, would have a function take only input and return one value through its name…".
11. **Done.** The body now says: "One way to think of a class, he says, is as an abstract data type plus…".
12. **Done, for both items.**
    - Item 5 is now the shipping-label and dispatch-log routine, as suggested.
    - Item 4 is now the lesson's own temporal example: a nightly routine that archives the day's orders, empties the shopping baskets and rotates the logs.
    - The quiz-1 `why` and PLAN §C 2.5 were updated to match. The answers are unchanged: temporal, then procedural.
13. **Done.** The quiz-1 `why` now uses the reviewer's sentence about the flag (p. 170).
14. **Done.**
    - The label is now "Strict layers: each module uses fewer modules, all below it".
    - The body now says "each module talks only to modules below it, and to fewer of them".
    - The figures are unchanged.
15. **Already done in the pedagogy round.** `taxRate` was renamed to `taxDue` in all three presets, and `checks-everywhere` was re-pinned.
16. **Kept.** §C asks for Riel's concession in this misconception. Exercise (a) still tests what the misconception does not give away: which fields are public, and what the callers actually do with them. The quiz item's right answer keeps "or whatever the callers do with them".
17. **Kit.** Records losing their `;` in the read-out is passed to the renderer engineer with finding 7. The course text was not changed for it.
18. **Already done in the pedagogy round.** One clause now says that Java has no private inheritance.

**On the disagreement over the quiz verdict** (the pedagogy review's must-fix 2):

- I kept the pedagogy route taken in the first round:
  - Quiz item 1's stem asks only about `Point`.
  - Its `why` still gives the exercise's three-class answer for the kiosk, which §C requires.
  - The `why` also adds the pedagogy review's sentence: "by the names alone … a design decision, not a counting error".
- This review agrees that this sentence fixes the item without dropping the grouping, and nothing in its argument suggests going further.
