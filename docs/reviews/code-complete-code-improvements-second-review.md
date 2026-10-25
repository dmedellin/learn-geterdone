# Second review (accuracy): Code Complete, Course 5 — Code Improvements

Course: `code-complete-code-improvements` (`content/code_complete/c5_code_improvements/`),
eight lessons (Chapters 20–26). Brief: `docs/code-complete/SECOND-REVIEW.md`. Reviewed
2026-10-25 against the private extraction of the second edition (printed page = PDF
page − 37). I read the pages each lesson cites with `ccbook.py` and a page-window helper:
pp. 463–477, 479–497, 499–533 (by section), 535–562, 563–585, 587–608 and 609–645.

**Scope note.** The orchestrator told this reviewer to write only this file and not to
edit lessons, so nothing in the course or in PLAN §C was changed. Every finding below
is a recommendation. Where the fix is mechanical, the exact replacement text is given.

**Concurrent edits.** While this review was being written, another agent began applying
the pedagogy review to `part_a.py` and `part_b.py` (uncommitted changes against commit
56d9c96: the quiz options were reordered, 5.2's step 2 was broadened, and the wording
was changed in a few places). The review was made on the committed text. At the end I
re-checked the working tree:
- Every must-fix and every should-fix below is still present, except two.
- 5.2's step 2 now says "A review checklist asks", which settles disagreement 2.
- 5.5's `why` now says "The fix adds a second test, `i < staff.length`, to the loop
  condition". That is closer, but it still does not say that the new test must come
  before `staff[i] != null` (should-fix 6).
- Quiz positions cited below may have moved. The items are named by their content.

## Gates

- **Preview:** `python3 scripts/preview_subject.py code_complete --course code-complete-code-improvements`
  → 9 pages; labcheck 8 pages executed, 8 with pinned figures, 0 failing; **OK**.
- **`labcheck.js --observe`:** every preset's tiles match the body prose, the worked lines,
  §C and my count by hand.
  - testing-only: 727 / 273 / 727/1000 = 72.7%.
  - inspections-too: 47543/50 = 950.86 / 2457/50 = 49.14 / 47543/50000 ≈ 95.1%.
  - one-stage: 300 / 700 / 30%.
  - test-only: 58 / 42 / 1,160 h / 20.
  - inspect-first: 83.20 / 16.80 / 674 h / 1685/208 ≈ 8.10. Traced as 210 + 240 + 224.
  - three-and-twelve: 458.40 h / 573/104 ≈ 5.51. Traced as 180 + 144 + 134.4.
  - overtime: 5, with points while 4, && 4, if 6, if 8. switch-without-default: 6, with case 4, 7, 10 and if 14, no-default 1.
  - correct / strict-top / no-lower-check: none / 99 / "0 and below", with the same six tests.
  - commit-637: 10 / 10. I traced the ten intervals by hand with the lower midpoint, and they match the body.
  - commit-63: 9 / 10. sixty-four: 6 / 6.
  - print-lines: fees, balance / none / 2. fee-loop: account, balance, fees / balance, fees / 3. from-the-top: account / balance, fees / 1. Read but set nowhere is none in all three.
  - tune-format: 910, 100/91 ≈ 1.10, 9%. tune-parse: 700, 10/7 ≈ 1.43, 30%. tune-the-small-ones: 850.15, 20000/17003 ≈ 1.18, 2997/20000 ≈ 15.0%. Pareto is "2 of 4" in all three.
  - busiest-outside: 500 / 600 / 505 / 19/120. busiest-inside: 505 / 505 / "0 = 0%". three-levels: 1,000 / 1,550 / 1,022 / 264/775.
- **Browser** (Playwright, site served locally, desktop and 375 px). I typed in each exercise as the body says. Every result agrees with its quiz `why`:
  - L1: `a, 0.4; b, 0.5` → 70%; the three 0.3 stages → 657/1000 = 65.7%.
  - L3: `archiveOld` → 4, with points for 2, if 3, || 3.
  - L4: lo 8, hi 64, `len > 8 && len <= 64` → disagree 8, tests 7, 8, 9, 63, 64, 65, exposed 8. The lab accepts `len` as the variable.
  - L6: `printInvoice` lines 2–5 → in inv, out subtotal; lines 7–9 → in subtotal, tax, out none.
  - L7: the 95/5 profile → 999/20000 ≈ 5.0% and 19/40 = 47.5%.
  - No page scrolls sideways at 375 px.
  - Each `code` lab preset uses the same Python constant as the body's `code` block (`OVERTIME`, `SHIPPING_LABEL`, `PRINT_STATEMENT`).
  - No exercise answer appears in body prose. Each answer is only in its quiz `why` (and, unavoidably, in the options).
- **Code:** every snippet compiles with `javac` once it is wrapped with stub classes (`Employee`, `Message`, `Transaction`, `Account`, `Line`, `Invoice`, `Config`).
  - Each is byte-identical to PLAN §D.4 / `presets.py` (`overtime`, `basis-switch`, `archive-old`, `count-passing`, `extract`, `print-invoice`).
  - No excluded feature is used.
  - I ran the exercise of L5: `overtimePay(fourEmployees, 5)` throws `ArrayIndexOutOfBoundsException: Index 4 out of bounds for length 4` from the `while` condition, as the `why` says.
  - Every snippet does what its prose says. The planted defects in `countPassing` and `validLength` are exactly the stated ones.
- **`# F` comments:** **18** (`grep -n "# F[0-9]"`: part_a 10, part_b 8). Each lesson header also names its ids: F16/F17, F18, F19/F2, F20, F21, F22, F23. I checked every one on its page:
  - F16 p. 470; F17 pp. 470–471; F18 pp. 472–473; F19 pp. 517, 521; F2 pp. 520–521; F20 p. 537; F21 pp. 580–581; F22 p. 592; F23 p. 623.
  - Every attributed figure is at §S.2's strength and is named as someone's average or one study's figure.
  - No book figure outside §S.2 is used.
  - See consider-23 for figures in `key`, `concepts`, `mistakes` and `note` that only the dict-header comment covers.
- **`cc_quotes.py`:** all 8 opening quotations are **OK**, and each is §C's **Quote**:
  - L1 p. 477, 19 words; L2 p. 497, 30; L3 p. 533, 27; L4 p. 533, 24; L5 p. 562, 30; L6 p. 585, 24; L7 p. 608, 25; L8 p. 645, 28.
  - Three further quoted phrases are **OK**: "The Devil's Guide to Debugging" (p. 539, 5 words); "factoring" (p. 565, 1); "parking lot" (p. 580, 2).
  - Lesson totals: L5 35 words and L6 27, both within 60. §C does not record those three phrases (should-fix 11).
- **Read-out:** `/usr/bin/python3 scripts/speechcheck.py` → code-complete 0 unresolved. I read the rendered `data-say` text of every code block, key line, worked line and backtick run:
  - `&&` and `||` are said "and" and "or".
  - `!=` is said "is not equal to".
  - The course has no prefix `!` and no `%`.
  - Code lines are announced by number, and blank and brace-only lines are skipped with their numbers kept.
  - No negation is dropped. Two ambiguities are in should-fix 9.

## Findings

Ranked: **must-fix** (a claim about the book or a cited author that the page does not
support), **should-fix**, **consider**.

### Must-fix

1. **Debugging as Science, body p 2: "Chapter 23 calls that guessing."** The sentence follows "You could read the code until the defect shows itself." The chapter does not call reading code guessing.
   - Its "Find the defect by guessing" (the Devil's Guide, p. 539) is scattering print statements and changing things until something seems to work.
   - Reading code is part of the method it recommends. Step 2(c) of its procedure is to decide the hypothesis by testing the program or by examining the code (p. 541).
   - Its brute-force fallback includes a full code review (pp. 548–549).
   - Its opening says most defects are minor slips, found easily by reading the listing or stepping through it in a debugger (p. 535).

   Replace: "You could read the code until the defect shows itself. Chapter 23 calls that guessing, and opens (p. 535)…" → "You could read the code until the defect shows itself, or change things until the test passes. Chapter 23 opens (p. 535)…".

   The misconception (`mistakes[0]`, §C's) can stand as a reading someone could hold. Its text claims nothing about what the book calls reading, but it should not imply that the book opposes reading code. Add after "experiment instead": "; reading the code is one of the ways it decides a hypothesis, not a substitute for having one."

2. **Debugging as Science, body p 2: Gould's study as "the book's evidence that debugging is a skill rather than a talent."** The book draws no such conclusion. It uses Gould (1975) for two things:
   - that not everyone knows how to debug, so the variation is wide (p. 536);
   - as support for the General Principle of Software Quality, since the best debuggers were fastest and most accurate (p. 537).

   It says nothing about skill against talent. Replace the last sentence with: "That is one study, from 1975, and the book reads it two ways: not everyone knows how to debug, and, since the fastest were also the most accurate, quality and speed go together, the General Principle of Chapter 20 again."

3. **Collaborative Construction, quiz 1 `why` (and PLAN §C 5.2's Answer): "Two of the three are on the chapter's checklist kinds, initialisation and off-by-one comparisons."** Chapter 21's checklists are about running the practice, not about code:
   - "Effective Pair Programming", p. 484;
   - "Effective Inspections", pp. 491–492.

   Neither names initialisation, comparisons or parameters. The chapter's point is that an inspection's checklist is the team's own, built from the errors its inspections find (p. 489).

   The two kinds are on the book's checklists elsewhere. Chapter 10's checklist asks whether counters and accumulators are initialised properly (p. 257). Boundary analysis names writing `>=` for `>` as a common mistake (p. 513).

   Replace the sentence with: "Each is the kind of point a team's inspection checklist would hold. The book's own checklists elsewhere ask whether counters and accumulators are initialised properly (Chapter 10) and warn of `>=` written for `>` (Section 22.3, p. 513); Chapter 21's point is that a team builds its checklist from the errors its inspections find."

   PLAN §C 5.2's Answer carries the same misstatement ("on the chapter's own checklist kinds") and should be corrected with it.

4. **Boundaries and Bad Data, body p 2: "starts from the claim, which it credits to Boris Beizer, that data use is at least as error-prone as control flow."** On p. 509 the book states that idea as the basis of data-flow testing, in its own voice. What it credits to Beizer (1990) is a different claim: at least half of all code consists of data declarations and initializations.

   Replace: "Data-flow testing (p. 509) starts from the idea that data use is at least as error-prone as control flow; the book adds Boris Beizer's estimate that at least half of all code is data declarations and initialisations."

### Should-fix

5. **Boundaries and Bad Data, body p 2: "the tests add a case for each place a value is defined and then first used."** That is weaker than the book's rule. The book says the key is to exercise all possible defined-used paths. It calls "all definitions" the weak form, one that running every line gives you anyway, and asks for all defined-used combinations: every place a variable is defined paired with every place it is used (p. 510).

   Replace: "and the tests add a case for each pairing of a place a variable is set with a place that value is used, which running every line does not guarantee."

6. **Debugging as Science, quiz 1 `why` (and PLAN §C 5.5): "The fix is `i < count && i < staff.length`, or dropping `count`."**
   - Read literally, this replaces the loop condition and loses the null test.
   - Placed after `staff[i] != null`, it would still throw.
   - The fix depends on order, in exactly the short-circuit way the `why` has just explained.

   Replace with: "The fix is to test the length before the element: `i < count && i < staff.length && staff[i] != null`, or to drop `count` and loop to `staff.length`."

7. **Course `how_to` item 3: "Four labs read Java: they count basis tests, the inputs and outputs of a block, and the boundaries of a check."**
   - Three labs read code: Structured Basis Testing (`code/basis`), Refactoring Safely (`code/extract`) and Boundaries and Bad Data (`cond/range`, which reads a condition).
   - The sentence lists three things.

   Replace "Four labs read Java" with "Three labs read Java".

8. **Structured Basis Testing, body p 5: "It is the same count as the decision points of “Nesting and Complexity”, used here for a different purpose."**
   - The book says the procedure is *similar* (cross-reference, p. 506).
   - The two counts differ in the very case this lesson's second preset shows. Basis testing adds 1 for a `case` statement with no default (p. 506), but the §19.6 count does not (Table 19-2, p. 458; F14).
   - On `shippingLabel`, Nesting and Complexity's rule gives 5, not 6.

   Replace with: "It is the decision-point count of “Nesting and Complexity”, plus one for a missing default, which the complexity count does not add; the book calls the two procedures similar."

9. **Read-out: a colon between two numbers is dropped, and the numbers run together.**
   - Structured Basis Testing's worked lines are read "while, line 4 1. and in the while, line 4 1. if, line 6 1. else if, line 8 1." A listener hears "line 4 1" as "line forty-one".
   - Code-Tuning Techniques' key line "outer 100, inner 5: 600 passes" is read "outer 100, inner 5 600 passes".

   Reword so that a word separates the numbers:
   - worked lines: `"the while, line 4:  adds 1"`, `"the && in it, line 4:  adds 1"`, `"the if, line 6:  adds 1"`, `"the else if, line 8:  adds 1"`;
   - key line: `"outer 100, inner 5 make 600 passes"` (36 characters).

10. **Collaborative Construction, `three-and-twelve`.**
    - The body p ("uses Microsoft's pair, 3 hours by inspection and 12 by testing") puts Microsoft's *find-and-fix* hours (p. 473) into a field that the lesson's own definition makes hours per defect *found*.
    - The quiz `why` draws the distinction, but the body does not.
    - The preset label ("Microsoft's figures as the book reports them") hides it.

    Add after "12 by testing": ", which Microsoft measured for finding and fixing together, so this preset prices both".

11. **Quotations that §C does not record.** "The Devil's Guide to Debugging" (L5, p. 539), "factoring" (L6, p. 565) and "parking lot" (L6, p. 580) are in quotation marks. All three are OK in `cc_quotes.py` and inside the limits.
    - The first is a section title, and the lesson types it with a straight apostrophe, where the book prints `Devil’s`.
    - Either record the three in §C's Lesson 5 and 6 entries with their pages, or drop the quotation marks from the two single words.
    - Change `Devil's` to `Devil’s` inside the quotation (part_b.py line 118).

12. **Collaborative Construction, `mistakes[1]`: "Solutions debated in the meeting slow it down and turn it into an argument about style."**
    - On inspections the book says only "Don't discuss solutions during the meeting" and keeps the group on finding defects (p. 488).
    - The argument about style is the pair-programming section's warning (p. 483).

    Replace with: "Solutions debated in the meeting take it off its one job, finding defects."

### Consider

13. **Refactoring Safely, body p 5 and quiz 3 `why`: "The chance of a bad change rises from one line changed to five and then falls, because small changes are treated casually (Weinberg 1983)."** The figure is Weinberg's (Figure 24-1, p. 581). The explanation is McConnell's comment in the next paragraph, not part of the cited finding. Reword: "…and then falls (Weinberg 1983); McConnell's explanation is that programmers treat small changes casually."

14. **The Software-Quality Landscape, the `note`, the last body p and step 4: "the 72.7 is an upper bound on the illustration".**
    - The product is an upper bound only if the stages' misses are positively correlated.
    - The book's under-60-percent report (p. 471) says real testing combinations do worse, which is evidence that they are, not a bound.
    - Step 4 has it right ("an upper bound when two stages find the same kinds of defect").

    In the note and the p, consider "optimistic, as Jones's under-60-percent suggests, and not a forecast".

15. **The Software-Quality Landscape, body p 6: "Quality, the Key Points put it, is free in the end, but only after resources are moved upstream."** The Key Point (p. 477) is that quality is free in the end but requires a reallocation of resources, so that defects are prevented cheaply instead of fixed expensively. "Upstream" is the lesson's gloss. Reword: "…is free in the end, but only once resources are moved to preventing defects cheaply rather than fixing them expensively."

16. **Debugging as Science, body p 2: "one study's small sample".** The page does not give Gould's sample size. It says professional programmers with at least four years of experience, and a program with 12 defects (p. 537). Say that instead.

17. **Refactoring Safely, exercise: "Find two blocks of `printInvoice` that extract cleanly."**
    - The answer is not unique. Lines 6–9 also extract with no Out: In subtotal and inv (the lab confirms this).
    - So 2–5 with 6–9 is a defensible pair, though the quiz names 7–9.

    Narrow the prompt: "Find the block that computes the subtotal and the block that only prints, and for each give…".

18. **Structured Basis Testing: "two of the five outcomes the count asks for".** This appears in body p 7, the worked `after`, the quiz 2 `why` and `mistakes[0]`. The count asks for five *tests*. Four decisions have eight *outcomes*, and the single call leaves two of them (a null entry; 40 hours or under) untried.

    Either "two of the eight decision outcomes" or "two of the five basis cases" is exact. The present wording mixes the two.

19. **Refactoring Safely, `mistakes[0]`: "Extract Routine is the refactoring most programmers reach for first".** This is an unsupported generalisation in the lesson's own voice. Soften it to "a refactoring many programmers reach for first", or drop it.

20. **Collaborative Construction (optional).** On any input where exactly one score equals the pass mark, the two planted defects in `countPassing` cancel: `{50, 60, 40}` with mark 50 returns 2, the right answer, which I checked by running it.

    A sentence in the quiz `why` would sharpen the chapter's claim that reviews find what tests miss: "a test whose one borderline score equals the mark passes, because the two defects cancel".

21. **Kit / read-out (not this course's to fix).**
    - The spoken text upper-cases the article "a" as "A" in key and worked lines on every page. Examples are "keep A change only if it measures faster" and "one change at A time".
    - A comment line ending in a full stop is read with a double stop ("…characters long..").
    - Both come from the code dialect, not the lesson. Report them to the renderer owner.

22. **Debugging as Science, body p 4.** "Refine the test case until changing any part of it changes the failure" merges two pieces of advice:
    - the stabilising step's advice to simplify the test case until changing any aspect of it changes the error (p. 542);
    - the locating tip "Refine the test cases that produce the error" (p. 544), which is about varying one parameter further.

    It is harmless, but the first belongs to stabilising.

23. **`# F` coverage by field.** The dict-header comments cover these figures, but no inline comment does:
    - L1: the key line "unit test 30, code inspection 60" (F16), and `mistakes[0]` and the `note` (F16/F17).
    - L2: the key line "IBM: 3.5 hours…", the concept "Hours per defect found", `mistakes[0]` and the `note` (F18).
    - L4: `mistakes[2]` (F19).
    - L6: `mistakes[2]` (F21).
    - L7: the concept "The Pareto principle" and the `note` (F22).
    - L8: the key line "outer 100, inner 5…", `mistakes[0]`, the worked `after` and the `note` (F23).

    The header comments satisfy the letter of PLAN §E.4 item 1. An inline `# F16, p. 470` beside `mistakes` and `note` in L1, L2 and L8 would make the grep complete.

## Claims checked and found right (the riskier ones)

- **L1:**
  - the external/internal split and that users care only about external characteristics (p. 464);
  - correctness hurts robustness (p. 465; Figure 20-1, p. 466);
  - §20.2's list (pp. 466–468);
  - Weinberg and Schulman: five teams, four first and one second, none good on all (pp. 468–469);
  - Table 20-2's source, Jones 1986a and 1996 and Shull 2002 (p. 470);
  - the 85% and 95% figures (p. 470);
  - Myers 1978b: experienced programmers, one program, no method significantly better alone, any two together almost doubling (pp. 470–471);
  - Jones under 60%, "usually inadequate" (p. 471);
  - Table 20-3 multiplies XP's rates (pp. 471–472);
  - the General Principle and "debugging and correcting code" as the single biggest activity (p. 474).
- **L2:**
  - the blind-spots premise (p. 480);
  - unit 30, integration 35, design and code inspections 55 and 60 after Jones 1996 (p. 480);
  - Myers 1978 and Basili, Selby and Hutchens 1986 on different kinds of errors, and scrutiny when work will be read (p. 481);
  - the pair-programming keys (p. 483);
  - pairs and inspections roughly equal (pp. 496–497);
  - Fagan "for several years" before 1976 (p. 485);
  - the roles, management, and no use in appraisals (pp. 486–487);
  - the moderator chooses someone other than the author to read (p. 488);
  - report, rework, follow-up and the third-hour meeting (pp. 488–489);
  - the second-edition inspections (pp. 490–491);
  - walk-throughs significantly less effective after Jones 1996 (p. 493), a meeting worth holding is worth running as an inspection (p. 493), and code reading (p. 494);
  - Kaplan and Moore (pp. 472–473), and one-step against two-step (p. 472).
- **L3:**
  - "in many cases it's the only part… unfortunate" (p. 500);
  - weighing yourself (p. 501);
  - the recommended approach, test-first's four reasons, "one of the most beneficial", "no panacea", and Beck 2003 cited (pp. 503–504);
  - clean tests, optimistic coverage, statement against branch coverage (p. 504);
  - the name, address and phone example and "hairy name" (p. 505);
  - the counting rule (p. 506).
- **L4:**
  - "lowbrow name" (p. 513);
  - `>=` for `>` and the three cases at a boundary (p. 513);
  - compound boundaries, and the bad and good data classes (pp. 514–515);
  - hand-checks (p. 516);
  - 80/20 and 50/5 with their sources (p. 517);
  - the taxonomy disagreement (p. 518);
  - construction 35%, and 75% on a small project (p. 520);
  - test cases as error-prone as code (p. 522);
  - regression testing practical only when automated (p. 528);
  - "getting sicker or healthier" (p. 529).
- **L5:**
  - Gould's three figures (p. 537);
  - the Devil's Guide items (p. 539);
  - the scientific method and the five-step procedure (pp. 540–541);
  - the tips (pp. 544–549), with binary search on p. 546 and recent changes and old versions on p. 547;
  - fixing is the easy part and therefore error-prone, and special cases are unmaintainable (pp. 550–553).
- **L6:**
  - the myth and its reality (p. 563);
  - duct tape and superstition (p. 564);
  - Fowler's definition and Constantine's factoring (p. 565);
  - smells (p. 565) and the diluted term (p. 571);
  - the catalogue summarising Fowler (p. 571);
  - the precautions, parking lot included (pp. 579–580);
  - Yourdon 1986b, Weinberg 1983 and Freedman and Weinberg 1982 (pp. 580–581);
  - risk levels (p. 581);
  - hacking, and refactoring instead of rewriting (p. 582);
  - the strategies (pp. 582–583).
- **L7:**
  - the camera and card reader (p. 588);
  - the seven viewpoints and Boehm's TRW story (p. 589);
  - Boehm 20/80 and Knuth under 4% over half, with a line-count profiler (p. 592);
  - the four old wives' tales (pp. 593–595);
  - Jackson's rules in the margin (p. 596);
  - compilers favour straightforward code (p. 597);
  - relative costs changed since the first edition (p. 603);
  - the matrix story: no improvement at any size, and harder code as the only sure result (pp. 603–604);
  - iteration combining techniques (p. 605);
  - the approach and "more than half… negligible or degrade" (p. 606).
- **L8:**
  - anti-refactorings, "true by definition" (pp. 609–610);
  - "things to try" (p. 610);
  - the section contents of §§26.1–26.4;
  - the busiest-loop example, 600 against 505, ≈16%, and 33/34/12/4 (p. 623);
  - inlining saves 8% in C++ and costs 10% in Java (p. 640);
  - §26.7: tests rerun 1 million to 100 million times, irrelevant for many programs but not for embedded or real-time work, less predictable than ten years before, and the measurement rule (pp. 643–644).

## Claims I could not settle against the page

- **L3, the late p:** test-driven development as Kent Beck described it (one failing test, just enough code, tidy, repeat).
  - This is outside the book.
  - The book cites Beck 2003 on p. 503 only for the test-first-or-last question.
  - The description matches Beck's *Test-Driven Development: By Example* (2003) as I know it. I did not fetch a source.
  - It is stated as Beck's and fairly in both directions, so I raise nothing.
- **L8, body p 7:** that Java's just-in-time compiler "may reorder or simplify loops itself". It is hedged and plausible, but it is not in the book, and I did not verify it for loop interchange in particular. "may simplify loops itself" alone is safer.

## Where I disagree with the pedagogy assessment

Written after the findings above. I then read
`docs/reviews/code-complete-code-improvements-pedagogy-review.md`.

1. **Debugging as Science, the opening, which the assessment does not question.** The
   assessment treats the lesson's voice as sound. Its second paragraph contains the
   course's two clearest misstatements of the book (must-fix 1 and 2): reading code is
   said to be what Chapter 23 calls guessing, and Gould's study is said to show that
   debugging is a skill rather than a talent.
2. **Its should-fix 6 (5.2, step 2) would compound must-fix 3.** The proposed step opens
   "The chapter's checklist asks, among other things: for each variable, where it is
   first set…". Chapter 21's checklists ask nothing of the kind (pp. 484, 491–492). If
   the step is broadened as the assessment suggests, which is a good idea, it should
   read "An inspection checklist built from past errors might ask…", or credit the
   questions to the book's Chapter 10 and boundary-analysis advice, not to Chapter 21.
3. **Its should-fix 5 (a demonstration of the hypothesis step on `shippingLabel`) is
   wrong about the snippet as drafted.**
   - "It happens for a few zones and never with `express` set either way" is
     self-contradictory. With `express` true, an unnamed zone returns `" express"`,
     not an empty label, so the symptom appears only when `express` is false.
   - "The line is 2, where the empty string is set" locates the defect on the
     initialisation. The cause is the `switch` with no default (lines 3–13), and
     Structured Basis Testing itself says that whether an empty label is wrong is "a
     question for the specification".
   - If the paragraph is taken, it should read: "…for zones the switch does not name,
     and only when `express` is false… the experiment: zone 4 without express, which
     should give an empty label, and zone 3, which should not… the cause is the
     `switch`'s missing default, lines 3 to 13, if the specification says every zone
     needs a label."
4. **"The best misconception handling in the course" (5.3's coverage paragraph).** I
   agree it is strong, but its count is loosely worded ("two of five outcomes";
   consider-18): five is the number of tests and eight is the number of outcomes.
5. **Read-out "reads correctly" throughout.** Two worked/key lines run two numbers
   together once the colon is dropped ("line 4 1", "inner 5 600 passes"; should-fix 9).
   The article "a" is upper-cased in the spoken text on every page (consider-21).
6. **The `note`s "honest about what each model cannot show".** I agree, with one
   correction: 5.1's note and last body paragraph call 72.7% "an upper bound". That is
   stronger than either the product or Jones's figure shows (consider-14).
7. **Agreement, for the record.**
   - The assessment's finding 3 and my consider-17 find the same non-unique exercise
     in 5.6. It also finds lines 3–5 (in `inv, subtotal`, out `subtotal`), which I had
     not listed, and its replacement wording fixes both.
   - Its must-fix 1 (`c` always 0) is outside this review's remit but is real. I saw
     the same in the source: every item has `"c": 0`.
   - Its finding 4 (the joke distractor in 5.8 quiz 4) is right, and its replacement is
     accurate to pp. 609–610.

## Summary of must-fix findings

1. Debugging as Science says Chapter 23 calls reading the code "guessing". The book's
   guessing is print statements and trial changes, and its method decides hypotheses
   by testing *or examining the code* (pp. 539, 541). Remove the clause.
2. Debugging as Science says Gould's study is the book's evidence that "debugging is a
   skill rather than a talent". The book draws no such conclusion. It reads the study
   as wide variation and as support for the General Principle of Software Quality
   (pp. 536–537).
3. Collaborative Construction's quiz 1 `why` (and PLAN §C 5.2's Answer) says the planted
   defects are "on the chapter's checklist kinds". Chapter 21's checklists contain no
   code items. Credit the kinds to Chapter 10's checklist (p. 257) and to boundary
   analysis (p. 513).
4. Boundaries and Bad Data credits Beizer with "data use is at least as error-prone as
   control flow". That is the book's own premise. Beizer's claim is that at least half
   of code is data declarations and initialisations (p. 509).

Preview: OK (8 labs executed, 8 with pinned figures, 0 failing). `# F` comments: 18,
all checked on the page. `cc_quotes.py`: 8 opening quotations OK, plus 3 short quoted
phrases OK, none of them recorded in §C.

## Author's response

All four must-fixes and every should-fix are applied, along with every consider item except 21, which belongs to the renderer owner. After the changes, preview is **OK**: 9 pages, labcheck 8 executed, 8 with pinned figures, 0 failing.

**Must-fix**
1. Debugging as Science no longer says the book calls reading code guessing. It now reads "…shows itself, or change things until the test passes. Chapter 23 opens (p. 535)…". The misconception now says that a hypothesis is decided by a test *or a reading of the code*, and that reading is one way to decide a hypothesis, not a substitute for having one.
2. Gould's study is now read the book's two ways: wide variation, and quality going with speed (the General Principle). The paragraph also gives the subjects (programmers with at least four years' experience) and the program (12 known defects), so consider-16 is done too.
3. The `countPassing` quiz `why` and PLAN §C 5.2's Answer credit the defect kinds to Chapter 10's checklist (p. 257) and to Section 22.3 (p. 513). They now say that Chapter 21's own checklists are about running the practice and that a team builds its checklist from its errors. Consider-20, the cancelling defects on 50, 60, 40 with mark 50, is added to the same `why`.
4. Data-flow testing's premise is now the book's own, and the claim credited to Beizer is his estimate that at least half of all code is data declarations and initialisations.

**Should-fix**
- 5: data-flow tests now pair each place a variable is set with each place it is used.
- 6: the overtime `why` says `i < staff.length` goes after `i < count` and before the null test, or that `count` is dropped. PLAN §C 5.5 gives the full condition.
- 7: the course `how_to` now says "Three labs read Java".
- 8: Structured Basis Testing now says the count is the complexity count plus one for a missing default, and that the book calls the two procedures similar.
- 9: the worked lines now read "the while, line 4: adds 1" and similar, and the key line reads "outer 100, inner 5 make 600 passes". The read-out now separates the numbers, so nothing is left for the renderer here.
- 10: the `three-and-twelve` paragraph says Microsoft's hours are for finding and fixing together. The preset label is now "Microsoft's find-and-fix hours: 3 by inspection and 12 by test".
- 11: the three phrases are recorded in §C 5.5 and 5.6 with their pages, and "Devil’s" now has the book's apostrophe.
- 12: the inspection misconception now says that debating solutions takes the meeting off its one job, finding defects.

**Consider**
- 13: Weinberg's figure is now kept apart from McConnell's explanation, in both the body and the `why`.
- 14: the 72.7 is called "optimistic … and not a forecast" in the body and the note. Step 4 is unchanged.
- 15: the Key Points gloss now says resources are moved to preventing defects cheaply rather than fixing them expensively.
- 17: this was already settled by the pedagogy fix. The exercise names both blocks and asks about lines 2–6.
- 18: "two of the eight decision outcomes" is now used in all four places.
- 19: Extract Routine is now "a refactoring many programmers reach for first".
- 22: simplifying the test case has moved to the stabilising step, and the locating tip now reads "refine the test cases that produce the error".
- 23: inline `# F` comments now sit beside the `mistakes` and `note` of L1, L2 and L8.
- Unsettled L8 claim: the text now says only "may simplify loops itself".

**Disagreement 3 (`shippingLabel`)**
- I checked this against the snippet. With `express` true, an unnamed zone returns " express". Read literally, the lesson's symptom ("a label with no place name") covered both cases, but the paragraph wrongly placed the cause on line 2.
- It now gives both forms of the symptom. The experiment uses zones 4 and 3 with `express` false. The cause is the `switch` on lines 3 to 13 having no default, which is a defect only if the specification says every zone needs a label.
