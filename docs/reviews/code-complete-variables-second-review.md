# Second review (accuracy): Code Complete, Course 3 — Variables

Course: `code-complete-variables` (`content/code_complete/c3_variables/`), six
lessons in `part_a.py`. Brief: `docs/code-complete/SECOND-REVIEW.md`. Reviewed
2026-10-25 against the private extraction of the second edition (printed page =
PDF page − 37), reading the paragraphs behind every claim the lessons make about
pp. 237–258, 259–289, 291–318 and 319–344, and p. 509 for the data-flow
anomaly names, with `ccbook.py` and a narrow page-window helper.

**Scope note.** The orchestrator told this reviewer to write only this file and
not to edit lessons, so nothing in the course or in PLAN §C was changed. Every
finding below is a recommendation, with the replacement text where the fix is
mechanical.

## Gates

- **Preview:** `python3 scripts/preview_subject.py code_complete --course code-complete-variables`
  rendered 7 pages. labcheck: 6 pages executed, 6 with pinned figures,
  0 failing. Result: **OK**.
- **`labcheck.js --observe`:** every preset's tiles match the body prose, the
  worked lines, §C and my hand count:
  - Lesson 1: `count-unset` gives 1 and `count (line 6)`; `initialized` gives 0;
    `set-twice` gives 3, with `total (lines 2, 4), count (lines 3, 5)` and
    `average (line 6)`. Its Dependencies tile, `1→4, 1→5, 4→6, 4→7, 5→6, 5→7`,
    agrees with the body's `4→6` sentence.
  - Lesson 2: 16/3 ≈ 5.33, 41/3 ≈ 13.67 and `heaviestKg: 16`, then
    7/3 ≈ 2.33, 23/3 ≈ 7.67 and `heaviestKg: 9`. My hand count of the spans:
    6, 1, 9, 4, 10, 2, then 2, 1, 2, 4, 3, 2.
  - Lesson 3: 7, 4/3 and `a, n, r, t, x, tmp`, then 7, 28/3 and `none`.
  - Lesson 4: all six presets, including 46341² − 2³² = −2,147,479,015 and
    0.1 × 10 stored as 1 − 2⁻⁵³.
  - Lesson 5: 5, 3 and the list of literals, then 0.
  - Lesson 6: 3, 6, 9, `current, 5 routines`, 10 and the writers list, then
    9, 3 and the owners. My own pair-by-pair count also gives 9 of 15.
- **Browser (Playwright, served locally).** I entered each exercise as the body
  asks:
  - Lesson 1: `initials` gives 0 anomalies.
  - Lesson 2: `reportSales` with `total count` gives 15/4 = 3.75 and
    21/2 = 10.50. With the declarations moved it gives 7/4 = 1.75 and
    13/2 = 6.50.
  - Lesson 3: `f` gives a mean of 1. The renamed `simpleInterest` gives
    53/5 = 10.60 and `months`.
  - Lesson 4: `int` 0 + 3000000 × 1000 prints `-1294967296`, and `long`
    prints `3000000000`. `int` 31536000 × 1000 prints `1471228928`.
  - Lesson 5: `watchWard` gives 3, 3 and `38.5 (line 4), 3 (line 5), 900 (line 8)`.
    With three `static final` constants it gives 0.
  - Lesson 6: the five records give 2, 3, 3 of 3 and 5. With owners they give
    2 places, and the coupled pairs stay 3.

  Every result agrees with §C's **Answer** and with the quiz `why`. No page error.
- **`# F` comments: 4**: F10 (pp. 245–248), F11 (p. 262) and F12 (p. 292) twice.
  I checked each on its page. Book figures in the course:
  - 54 against 7 and the 1-to-25 example (F10, pp. 246, 248);
  - 10 to 16 and 8 to 20 (F11, p. 262);
  - only 0 and 1 (F12, p. 292).

  No book figure lacks a comment. Card, Church and Agresti (1986) is a finding
  with no figure. Its page is in the lesson 1 comment (p. 257). It is worded as
  the book cites it, and as a correlation.
- **`cc_quotes.py`:** 8 quotations.
  - L1 p. 258: OK, 24 words.
  - L2 p. 258: OK, 24 words. Lesson 2 also uses "window of vulnerability",
    p. 245 (OK, 3 words), and "moonlighting as a boolean" (4 words). That phrase
    is on **p. 257**. It passed when tested at p. 256 only because the checker
    also searches the following page. Lesson 2 total: 31 words.
  - L3 p. 289: OK, 23 words.
  - L4 p. 295: LOOSE, 29 words. I checked it by eye: the margin epigraph
    "1 is equal to 2…" is interleaved in the extraction, and the body text
    matches character for character.
  - L5 p. 309: OK, 22 words.
  - L6 p. 344: OK, 24 words.

  Every quotation is within 40 words, and every lesson is within 60. I checked
  the ordinals against the Key Points lists on pp. 258 and 344. "First" (L1),
  "second" (L2) and "last" (L6) are all correct. The `javac` message quoted in
  lesson 1 is the compiler's, not McConnell's.
- **Read-out:** `speechcheck.py` has no row for code-complete. I ran
  `speech.say_code_block` and `speech.say_code` over:
  - every `code` block (line numbers are announced, and marked lines are
    "flagged");
  - every backtick run, key line and worked line.

  Nothing is mangled. There is no `!`, `&&`, `||` or `%` in the course, so no
  negation can be dropped. `-2147483648` in a key line is read "minus". The
  worked line `13/2` is read "13 divided by 2".
- **Snippets against §D.4 / `presets.py`:** they are character-identical
  (`count-unset`, `initialized` with `count` on line 3, `set-twice`,
  `declared-at-top`, `declared-near-use`, `names-short`, `names-long`, `magic`
  and `named`). Each snippet is one constant, shared by the code block and the
  preset.
- **Java:** every snippet compiles as the fragment presented, given its
  domain types (`Shipment`, `Sale`, `Patient`, `Record`). The two deliberate
  faults behave as described:
  - `count-unset` and `initials` each give exactly one definite-assignment
    error.
  - `set-twice` compiles.

  No feature excluded by §D.0 is used. Where Java differs from C and Python, the
  lessons say so: definite assignment against C, field defaults, wrapping
  against C's undefined behaviour and Python's big integers, and integer
  division.

## Findings

Ranked: **must-fix** (a claim about the book that is wrong, or a rule of PLAN
broken), **should-fix**, **consider**. I found no misstatement of a figure, no
quotation off the page, no reproduced listing or checklist, and no snippet
that does other than the lesson says.

### Must-fix

1. **Declaring and Initializing Variables: the `note` gives away the
   exercise's answer.** The note says "Java's compiler checks every path, so
   for locals it is stronger than the lab, **and the exercise is a case only
   the compiler sees**". That clause tells the reader that the lab reports
   nothing and that `javac` rejects the routine, which is the whole answer
   that PLAN §B and §E.4 item 4 keep for the quiz's first `why`.
   **Fix:** delete the clause. The note should read:
   > "The lab reads the lines in order and never follows a branch or a loop;
   > Java's compiler checks every path, so for locals it is stronger than the
   > lab. The lab also cannot see …"

### Should-fix

2. **Scope, Span and Live Time: a conclusion the page does not draw.** The
   fourth body `p` says that McConnell's "own conclusion is that a program is
   read more than it is written." Pages 250–251 frame the two philosophies as
   "a difference in emphasis between writing programs and reading them." His
   conclusion there is different: a program in which any routine can use any
   variable is harder to understand, read, debug and modify, so each variable
   should be visible to the smallest part of the program that needs it.
   "Read far more times than it is written" is Chapter 11's Key Point (p. 289),
   not this passage's.
   **Fix:** replace the clause with:
   > "his own conclusion is that a program in which any routine can use any
   > variable is harder to understand, debug and modify, so each variable
   > should be visible to the smallest part of the program that needs it."

3. **The Power of Variable Names: the `note` misquotes Section 11.5's
   example.** The note says "as with the distinctions between first, last,
   limit and maximum". The book's list (p. 281) is min, first, last and max;
   "limit" is not in it. The same sentence says prefixes "can catch type
   mistakes a compiler cannot". The book says they let you check types "that
   your compiler can't necessarily check". That is weaker: it covers abstract
   types the compiler may not distinguish.
   **Fix:**
   > "as with the distinctions between minimum, first, last and maximum, and
   > can catch mixed-up abstract types that a compiler may not check."

4. **Scope, Span and Live Time: two quotations are not recorded.** The body
   quotes "window of vulnerability" (p. 245) and the `mistakes` quote
   "moonlighting as a boolean" (p. 257). Neither is in §C's entry or in a page
   comment beside the dict. Under the brief, a quotation other than §C's
   **Quote** that §C does not record is a finding. Both are short, both are
   attributed to the book, and the total of 31 words is within limits.
   **Fix:** add this to the lesson's comment:
   > `# Also quoted: "window of vulnerability", p. 245 (3 words); "moonlighting as a boolean", p. 257 (4 words); lesson total 31.`

   Add the same note to §C 3.2.

5. **Scope, Span and Live Time: "nine of which come before it is first
   used".** `heaviestKg` is live on lines 3–18. The lines before its first use
   on line 13 are lines 3–12, which is ten lines. Nine lie strictly between the
   declaration and the first use, and that is how §F's exemplary paragraph
   puts it.
   **Fix:**
   > "…and it is live for 18 − 3 + 1 = 16 lines, and the nine lines between its
   > declaration and its first use have nothing to do with it."

### Consider

6. **Structures, Pointers and Global Data: "and above all the damage to
   modularity".** Section 13.3 lists modularity last of its six problems and
   says it is "reason enough" (p. 338). It does not rank it above the others.
   **Fix:** write "and, last, the damage to modularity…", or drop "above all".
7. **Named Constants and Other Types: "two reasons".** `mistakes[0]` says "the
   chapter gives two reasons for constants, readability and a single point of
   change". The third quiz's `why` says "one of Section 12.7's two reasons".
   Section 12.1 (p. 292) lists three benefits: changes made more reliably,
   changes made more easily, and readability. Section 12.7 argues single-point
   control and readability. **Fix:** in `mistakes[0]`, write "The chapter's
   reasons for constants are readability and a single point of change". In the
   quiz `why`, write "one of Section 12.7's reasons".
8. **Declaring and Initializing Variables: page range.** The lesson says pages
   237 to 243, but Section 10.3 runs onto p. 244, where "Check input parameters
   for validity" is (the lesson cites that guideline). Say "pages 237 to 244"
   here and in §C 3.1. The overlap with lesson 2's p. 244 is harmless.
9. **Integers and Floating Point: `mistakes[1]` says "only integer division by
   zero throws".** `%` by zero also throws `ArithmeticException`.
   **Fix:** "only integer division or remainder by zero throws".
10. **Declaring and Initializing Variables: C's behaviour.** The body says that
    a C program "reads whatever was in memory", and the fourth quiz's `why`
    calls that "C's behaviour". In C, reading an uninitialised local is
    undefined behaviour; leftover memory is the usual result, not a guarantee.
    **Fix:** "the behaviour is undefined, and in practice the read usually gets
    whatever was in memory". This is a precision point, not a misstatement of
    the book.
11. **Structures, Pointers and Global Data: the type name `Record` in
    `ACCESS_ROUTINE`.** Since Java 16, `java.lang.Record` exists. The fragment
    compiles only because a user `Record` in the same package shadows it. The
    name is harmless, but a reader may wonder whether it is the language
    feature PLAN §D.0 excludes. Renaming it to `InputRecord` changes no figure:
    no lab reads this snippet, and no prose names the type.
12. **Scope, Span and Live Time: worked line "average span: 13/2, about 6.5".**
    The value is exact. Write "is 6.5".
13. **Kit (page `integers-and-floating-point`, preset `tenth-ten-times`).** The
    `nuStored` tile prints `9007199254740991/9007199254740992 ≈ 1.00`. The
    two-place decimal follows §D.0's rule, but here it reads as "1.00" right
    beside "The same? no". The body explains the fraction, so a reader is not
    misled. Still, the kit could print more places, or the fraction alone,
    when the rounded decimal would equal the comparison value. This is not a
    lesson fault.
14. **Named Constants and Other Types: the second "readers disagree"
    passage.** This lesson's body ("This is where many readers part company
    with McConnell…") and its `note` ("practice varies; the book's answer is
    yes") together come close to a second §F.4 aside in the course. The aside's
    home is The Power of Variable Names. §R.1 #19 explicitly allows this
    lesson to say where readers disagree, and both passages state the book's
    position at strength, so I leave them. If the note's sentence is cut, the
    body still carries the point.

## Claims checked and confirmed (no finding)

These are the claims a reader is most likely to doubt. Each matches the page:

- **Lesson 1:**
  - implicit declaration "one of the most hazardous features" and the
    two-mistakes argument (p. 240);
  - the made-up data-literacy terms and the "fraud" score band (p. 239);
  - initialisation errors as an unexpected initial value, in three cases
    (p. 240);
  - the loop built around far-off initialisations, and the Principle of
    Proximity (p. 242);
  - `final`, counters and accumulators, and compiler warnings (p. 243);
  - Defined-Defined "wasteful and error-prone, even if not actually wrong"
    (p. 509);
  - Card, Church and Agresti on unreferenced variables (p. 257).
- **Lesson 2:**
  - "celebrity status" (p. 244);
  - the 1/25 span and live-time example (p. 246);
  - 54 against 7, and no hard number from researchers (p. 248);
  - harder to narrow a scope than to widen it (p. 250);
  - the milk jug (p. 251);
  - binding times from coding time to just in time, with the window examples
    (p. 253), and flexibility against complexity (pp. 254, 258);
  - `pageCount` −1 as hybrid coupling (p. 257).
- **Lesson 3:**
  - Gorla et al. (p. 262), and the 32-character Olympic-team name (p. 262);
  - qualifiers at the end (p. 263);
  - loop indexes: long, nested, or used after the loop with `recordCount`
    (p. 265);
  - `flag` (p. 266) and `temp` (p. 267);
  - a convention's power coming from its existence (p. 271);
  - Hungarian "no longer in widespread use" (p. 279);
  - prefixes as no substitute for a name (p. 281);
  - short names as "a remnant of an earlier age" (p. 282);
  - not removing one character (p. 283);
  - Goal Donor and Gold Owner (p. 286).
- **Lesson 4:**
  - top programmers fix compiler warnings (p. 293);
  - 10 × (7/10) = 0 (p. 293);
  - the 1,000,000 × 1,000,000 / 1,000,000 = −727 Java example (pp. 294–295);
  - magnitudes (p. 295);
  - the 0.1-ten-times listing printing 0.9999999999999999 (p. 296);
  - BCD, integers for cents, and a `DollarsAndCents` class (p. 297).
- **Lesson 5:**
  - `ESCAPE`, and the translation, memory and cryptic reasons (p. 298);
  - Java strings are Unicode (p. 298);
  - "1 stands for red" (p. 303);
  - the Java enum margin note (p. 307);
  - single-point control (p. 308);
  - "Avoid literals, even 'safe' ones", the Monty Python bet, and searching
    for 2–9 (pp. 308–309);
  - containers, end points and cross-talk (pp. 310–311).
- **Lesson 6:**
  - a structure as public data with no public routines (p. 319);
  - pointers "one of the most error-prone areas" (p. 323), and the two-pronged
    strategy (p. 325);
  - riskier, but access from several routines useful (p. 335);
  - the six problems (pp. 336–338);
  - purists, the database and registry, and named constants as global data but
    not global variables (p. 338);
  - local first (p. 339);
  - the stack-overflow check and `PageFull()` (pp. 339–340);
  - `static`, and the "same barrel" (p. 340);
  - the "monster object" and "none of the benefits of true encapsulation"
    (p. 343).

## Claims not settled against the page

- **Section 12.6's "for parameters whose meaning is otherwise a guess"
  (lesson 5).** This is a reasonable paraphrase of the readability guideline.
  I did not read the whole of pp. 303–304 to confirm that parameters are the
  book's example. I searched "enumerated types for readability" and found it
  on p. 303.
- **"Java 5 added `enum` the same year" (lesson 5).** This is outside the
  book. J2SE 5.0 shipped in September 2004, the book's year of publication.
  I did not check this on the web; it is stated from general knowledge and
  matches the margin note's prediction.

## Disagreements with the pedagogy assessment

There is none yet. Neither `docs/reviews/code-complete-variables-pedagogy-review.md`
nor a `docs/pedagogy/` file for this course existed when this review was
finished, so I have nothing to compare with. I wrote my findings without
reading any pedagogy assessment of the course.

## Summary of must-fix

One: delete "and the exercise is a case only the compiler sees" from lesson 1's
`note`, because it gives away the exercise's answer. The should-fix items are:

- lesson 2's "read more than it is written" conclusion, which is not on
  pp. 250–251;
- lesson 3's note, "limit", which should be "minimum", and "cannot", which
  should be "may not";
- lesson 2's two unrecorded short quotations;
- lesson 2's "nine of which", which should be "nine lines between".

## Author's response

Applied from this review: must-fix 1 (the note's clause removed; the note now
names the lab's limits without the exercise); should-fix 2 (the p. 250–251
conclusion as given), 3 (minimum, first, last, maximum; "may not check"), 4
(both short quotations recorded beside the dict and in §C 3.2), 5 ("the nine
lines between its declaration and its first use"); consider 6 ("and, last"),
7 (no count of reasons), 8 (pages 237 to 244, here and in §C 3.1), 9
(division or remainder), 10 (undefined behaviour, usually leftover memory, in
the body and the quiz `why`), 11 (`InputRecord`), 12 ("which is 6.5").

Applied from the pedagogy review: must-fix 1 (the permutation table, options
moved and every `why` reworded where it named an option by position), 2 (the
tax table is a `static final` array, with the loader case explained in the
`why`), 3 (note and option text); should-fix 4 to 10; consider 12 (the enum
sentence in lesson 5's exercise `why`), 13 (lesson 4's fourth item is now the
intermediate overflow) and 14 ("when the loop body calls another routine").
Finding 8 split lesson 6's first item in two and dropped the "which pair is
not coupled" item, so lesson 6 keeps four items.

Declined or left:
- Consider 13 here (the kit's `nuStored` "≈ 1.00" beside "no"): a kit
  change, outside the course; the body explains the fraction.
- Consider 14 here: left as the reviewer recommends; §R.1 #19 allows the
  passage and both sides are stated at strength.
- Pedagogy consider 11 (merging lesson 3's §§11.5–11.7 paragraphs): declined;
  the prefix paragraph is what the `note`'s modern aside rests on, and the
  lesson is within the block and length limits.
- Pedagogy consider 15: checked, p. 239 names three made-up terms; no change.
- Pedagogy consider 16: the kit's table treatment; no lesson change.
- Pedagogy should-fix 6 took the prose route (`1000L`, "a long literal with an
  L after it"), so no spoken form was added to content/spoken/code_complete.py.
