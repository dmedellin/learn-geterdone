# Second review: Course 4, Statements (`code-complete-statements`)

Brief: `docs/code-complete/SECOND-REVIEW.md`. Read against the book's text
(private extraction, `ccbook.py`, `cc_quotes.py`), PLAN §C 4.1–4.7, §D.4,
§E, §F and §S.2, the rendered preview, `labcheck.js --observe` on every page
and a Playwright session that typed each exercise into its lab. The
pedagogy review (`docs/reviews/code-complete-statements-pedagogy-review.md`)
was read only after the findings below were written.

Final preview: `python3 scripts/preview_subject.py code_complete --course
code-complete-statements` → 7 pages executed and swept, 7 with pinned
figures, 0 failing, **OK**. `speechcheck.py`: code-complete 0 unresolved.

## Must-fix (fixed)

1. **Table-Driven Methods: the binary-search probe count is wrong for some
   keys.** The kit's `stairs` search (`cckit_b.py`, `lo = 0, hi = n`)
   searches n + 1 places: the n steps and "above the table". For the
   16-step `brackets` table that is 17 places, and keys in the first two
   steps (below 2,000) take **5** probes. In the browser, `brackets` with key
   500 prints `seBinary` 5. The lesson said 4 probes "as it does for any key
   in a sixteen-step table", and quiz item 3 asked "how many probes for a key
   in it?" with the answer 4 and a `why` of "16, 8, 4, 2, 1 … whatever the
   key". The body, the quiz and the `note` also said the search "stops when
   one step is left". All the pinned figures (days-20 2, days-60 3 and 3,
   brackets 14,500 4, the exercise's 2 and 3, a key of 5 3) are correct under
   the n + 1 rule and were rechecked by hand.
   *Changed:* the body now says the search stops when one place is left and
   counts the place above the last bound (a five-step table has six); the
   brackets sentence says "takes 4, and no key in this table takes more than
   5 (those below 2,000 take 5)". Quiz 3 now asks for the most probes over
   17 places (answer 5; distractors 16, 17, 4), with the `why` "17, 9, 5,
   3, 2, 1". The `note` and the worked `after` ("for 14,500, it saves
   eleven") were changed to match. Recorded in §C 4.5.

2. **Controlling Loops, quiz item 2 `why`: the off-by-one is described the
   wrong way round.** It said "With `<` it would run 10 times, which is the
   off-by-one the lesson's `hourly` loop makes in the other direction". The
   `hourly` loop's mistake is running 11 times where 10 were meant, and 10 is
   the right count. *Changed to:* "With `<` it would run 10 times; running 11
   times where 10 were meant is the off-by-one the lesson's `hourly` loop
   makes."

## Should-fix (fixed)

3. **Using Conditionals and Nesting and Complexity: quotations that §C does
   not record.** All run through `cc_quotes.py` (below); all are OK and on
   their stated pages and within the limits. Using Conditionals quotes the
   Pontiac Aztek line (p. 365, 19 words; lesson total 40). Nesting and
   Complexity quotes "structured goofing off" (p. 454, 3) and "or their
   equivalents" (p. 458, 3; total 21). *Changed:* a "Recorded at second
   review" line in §C 4.2 and 4.7.

4. **Ten new snippets are not recorded in §C** (AUTHORING.md: a new snippet's
   figures go in the course's §C entry): `classify`, `route`, `hourly`, the
   `by-threes` header, recursive and loop `fibonacci`, `lateFee`, the shipping
   arrays, `drain` and the owner test. Each was traced by hand. They compile
   as the fragments the lessons present, and they do what the prose says. The
   line numbers named are right (drain: guard on line 4, test on line 7;
   `hourly[10]` throws `ArrayIndexOutOfBoundsException`; fib loop 29 passes
   for n = 30). *Changed:* §C 4.2–4.6 each gain a "Recorded at second
   review" line with the snippet and its figures.

5. **Organizing Straight-Line Code: "Keep the routine to five lines" can't be
   done.** `HIDDEN` is six lines with its brace, and so is the answer. If the
   reader's layout differs, the quiz's `4→5` stops matching. *Changed to:*
   "Keep each of the four statements on its own line, so that they are still
   lines 2 to 5" (the pedagogy review's wording, which is better than mine).

6. **Read-out: the article "a" is spoken as the variable "A" in key lines.**
   The rendered `data-say` gave "name A complicated test", "treat the loop
   body as A black box", "check the first, A middle and the last pass",
   "A step stores…", "A count says where to look" and, on the course page,
   "move the logic into A table … A count is A reason to look". No negation
   is dropped anywhere: every `!`, `&&` and `||` in code lines and backtick
   runs is spoken "not", "and" or "or". *Changed:* the key lines were reworded
   so that they contain no article: "name each complicated test", "treat loop
   bodies as black boxes", "check the first, middle and last passes", "each
   step stores the top of its range", "the count says where to look", "move
   the logic into tables" and "counts are reasons to look". After
   re-rendering, no key line says "A" for an article.

7. **Nesting and Complexity: the breakdowns in prose read badly.** "1 + if 5
   + for 1 + && 1 + || 1" was plain prose. The renderer wrapped only "1 + ||
   1" and left `&&` for the browser to read aloud, and the plain reader turns
   `|| 1` into "the absolute value of 1". *Changed:* both breakdowns are now
   backtick runs. They are spoken "1 plus if 5 plus for 1 plus and 1 plus or
   1".

8. **Unusual Control Structures: Dijkstra's observation was paraphrased from
   the book's own paraphrase.** The lesson said the letter observed "that the
   quality of code fell as the number of its gotos rose". That is the book's
   wording (p. 398). The letter (EWD215, checked by web search) speaks of the
   quality of *programmers* as a decreasing function of the *density* of go
   to statements in their programs. *Changed to:* "…observing that the
   quality of programmers fell as the density of `goto`s in their programs
   rose, which the book renders as the quality of code."

## Consider (fixed where a wording only)

9. **Using Conditionals, the lesson's own verdict.** "The chapter's first
   reason, the reader who looks for the usual case, is usually the stronger"
   ranked the reasons in the lesson's own voice. The book lists readability
   first and does not rank them (p. 359). *Changed to:* "the chapter gives
   its other reason, the reader who looks for the usual case, first."

10. **Using Conditionals: "the final `return` is the error trap the
    quotation asks for".** `return "unexpected"` hands the case back to the
    caller silently. §15.1 (p. 360) asks for an error message or an assertion
    meant for the programmer. *Changed to:* "is where the quotation's error
    trap goes; a full one would also report the unexpected status to the
    programmer, as Section 15.1 asks".

11. **Unusual Control Structures, the aside: "the dispute McConnell said had
    moved to multiple returns…"** On p. 398 the book says modern equivalents
    of the debate "still crop up" in debates over multiple returns, loop
    exits, error processing and exception handling. That is not a move.
    *Changed to:* "the debates in which McConnell saw the argument still
    cropping up, over multiple returns, loop exits and exception handling
    (p. 398), are argued in those terms today."

12. **Table-Driven Methods `mistakes[0]`: "Speed is one of the chapter's
    reasons, and not the main one."** On p. 411 the book gives three reasons
    without ranking them: simpler, easier to modify and more efficient.
    *Changed to:* "Speed is one of the chapter's reasons (p. 411), beside
    simplicity and ease of change."

13. **Not changed:**
    - The formula `2·F(n + 1) − 1` is spoken "2 times F of n plus 1 minus 1"
      in the key and the worked line.
    - In the `standard` the renderer wraps only "2·F(n +", which is a
      renderer fault.
    - "twice F(n + 1), less 1" is still read "F of n plus 1" in the code
      dialect, so no wording fixes it inside this course.
    - The `drain` snippet's `Queue` shares a name with `java.util.Queue`,
      which has no `hasFailed`. A reader may assume the JDK type. A name
      such as `JobQueue` would avoid that.

## Checked and correct

- **Book claims, section by section, against the page.** Checked:
  - §14.1 guidelines and their order (p. 350: first without dependencies,
    second obvious, then document), the status-variable costs (p. 350), the
    "terrible routine" remark (p. 349), the boxes test and the
    decomposition (p. 352).
  - §15.1 and §15.2 guidelines (pp. 355–365), including the phony-variable
    first-letter example and the default clause (p. 363).
  - The kinds of loop (p. 367), black box (p. 373), "prefer for" (p. 374),
    monkeying and the final value (p. 377), endpoints and the calculator
    (p. 381), three C++ compilers (p. 384), F13 (p. 385), APL and
    Fortran 90 and the Java loop (p. 387).
  - The twilight zone (p. 391), the guard-clause margin (p. 393), the
    recursion tips and "I'd hire someone else" (pp. 396–398), the goto
    arguments, Sheil and Knuth (pp. 398–399), nine out of ten (p. 407),
    strong skepticism (p. 408).
  - §18.1–18.5, including the OO pointer on p. 411, fudging keys (p. 424),
    the indexed-access advantages (pp. 425–426), the endpoints and the
    quasi-binary search (p. 428).
  - §19.1–19.3, including Homer Simpson, the margin note on p. 436, fully
    parenthesize (p. 438), Java `&`/`|` (p. 439), nested tests (p. 440),
    `equals` (p. 443), braces and `DoNothing()`.
  - §19.4–19.6: F15 (p. 445), the remedies and their summary (pp. 445–454),
    "good reason" (p. 453), Dijkstra 1969, one-in one-out and Böhm–Jacopini
    (pp. 454–456), Table 19-2 and the warning flag, the long case statement
    and "moves the decision points" (p. 458).
  - Key-point ordinals for all seven openings.
  - Every `not_covered` item: the VB case ranges (p. 361), the C++
    AND/OR/EQUALS macros (p. 442), the null-statement macro (p. 444) and
    comparisons to 0 (p. 441).
- **Figures.** `grep "# F[0-9]"` finds 3 comments: F13 (p. 385), F14
  (p. 458) and F15 (p. 445). All three match §S.2 and the page, at the
  page's strength. No other book figure appears in the course.
- **Arithmetic.** Every preset was recomputed by hand and with the lab:
  - dataflow: 6 anomalies, and 1→3, 1→4, 1→5, 2→6. The other two presets
    and the exercise's seven arrows are also right.
  - chain: 7/2, 3/2, 2; 29/20, 29/20, 0; 14/5, 13/5, 1/5. The exercise:
    11/4, 5/4.
  - loop: 11/10/11, 10/9/10, 11/0/−1, and "never ends" (even values,
    wrap-around included). The exercise: 4/1/−2.
  - recursion: 2·F(31) − 1 = 2,692,537; 2·F(41) − 1 = 331,160,281; the
    loop makes n − 1 passes; factorial(10) is 10 calls.
  - complexity: 9 (lines 3, 4, 5, 6 and 13; `for` 12; `&&` 6; `||` 13),
    depth 5 at line 14. The guard version is 6, depth 1 at line 3.
    `refundAmount` is 3 before and after, depth 2 → 1. `discountPercent`
    is 7, depth 2 at line 11.
  - truth: all four presets and the owner exercise.
- **Labs in the browser.** Every exercise typed in gave the quiz's answer,
  with no page errors. Each preset's code is the body's constant.
- **Copyright.** No listing, table or checklist is reproduced. Table 19-1 is
  named, not reproduced.

## `cc_quotes.py`

```
L1  p.353 OK 10   L2  p.366 OK 21   L2b p.365 OK 19 (Aztek)
L3  p.389 OK 20   L4  p.410 OK 22   L5  p.430 OK 27
L6  p.460 OK 14   L7  p.460 OK 15   L7b p.454 OK 3   L7c p.458 OK 3
```

## Not settled against the page

- "Large C programs still use a forward `goto` to a single cleanup label"
  (the aside) is the lesson's own present-tense claim. It is true of
  well-known code bases such as the Linux kernel, but the book does not
  make it. "Some large C programs" would hedge it.

## Where I differ from the pedagogy review

- It praises `table-driven-methods`' presets and did not catch the
  binary-search error (my #1). Its quiz-distractor pass accepts quiz 3's
  "4, whatever the key".
- It calls the read-out's only ambiguity the Fibonacci key (its #10). The
  article-as-"A" in five key lines and the course key (my #6), and `|| 1`
  read as an absolute value in prose (my #7), were missed.
- It counts the Aztek quotation as 17 words. `cc_quotes.py` gives 19. It
  does not note that §C does not record it.
- It misses the quiz 2 `why` in Controlling Loops (my #2).
- I agree with its #2 (adopted its wording) and #4. The `why` of
  `refundAmount`'s quiz should allow one `if` and one `||`; I left that and
  its #1, #3, #5, #7 and #8 to the course's author, because they are
  teaching changes rather than errors of fact. On #3, though, I agree
  that `how_to[3]`'s "a chain" is false of `nested-shipping`.
- On its #6 I disagree in part: as-written has no `else` case, and the
  listing's trailing `return` is reached by no illustrated status. The
  worked intro is accurate, but the clarifying sentence it proposes is fine.

## Summary of must-fix findings

1. Table-Driven Methods said the lab's binary search takes 4 probes for any
   key in a 16-step table (the body and quiz 3). The kit searches n + 1
   places, so keys below 2,000 take 5. The body, quiz, note and worked line
   are fixed.
2. Controlling Loops, quiz 2's `why` described the `hourly` off-by-one
   backwards. Fixed.

## Author's response

All the reviewer's fixes were re-read against the files after the pedagogy-round edits. None was overwritten. The final preview prints OK: 7 pages, 7 with pinned figures, 0 failing.

1. **Binary search over n + 1 places.** Accepted; this was my error. The fix is present in the body ("stops when one place is left … a five-step table has six"), in the brackets sentence ("no key in this table takes more than 5"), in quiz 3 (17 places, answer 5), in the `note` and in the worked `after`. I made one more change to match: `steps[2]` now says "until one place remains, counting the place above the top bound as one". It had still said "one step".
2. **Controlling Loops quiz 2.** Your corrected `why` was replaced by the pedagogy review's finding 5. Quiz 2 now uses a header not on the page, `for (int i = 1; i < 10; i += 3)`, with the answer "3 times; 10 after". Its `why` names 1, 4 and 7 and the step past, and no longer mentions the `hourly` loop.
3. **Quotations recorded in §C.** Present in §C 4.2 and 4.7.
4. **New snippets recorded in §C.** Present. One more was added in the pedagogy round: `firstLine(File)`, a guard-clause demonstration. It is recorded in §C 4.4 with 3 decision points and depth 1.
5. **"Five lines".** Present, with the pedagogy review's extra clause on matching line numbers.
6. **Article-free key lines.** Present. The Fibonacci key line had become "recursive Fibonacci: 2·F(n + 1) - 1 calls"; in the pedagogy round it is now "calls: twice F(n + 1), less one". As you note, the code dialect still reads "F of n plus 1". That is the renderer's to settle.
7. **Breakdowns in backticks.** Present in Nesting and Complexity.
8. **Dijkstra's wording.** Present.
9–12. **Consider items.** All four are present. Item 11's hedge, "some large C programs", is also in, applied in the pedagogy round.
13. **Not changed.** I took the `Queue` point: `drain` now takes a `JobQueue`. Its line numbers are unchanged; the guard is still on line 4 and the inner test on line 7.

On where the two reviews differ: I adopted the pedagogy review's #1, #3, #4, #6, #7 and #8. The binary-search finding was mine to fix, and it is fixed.
