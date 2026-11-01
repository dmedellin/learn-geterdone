# Review (accuracy and teaching): Accelerate, Course 4 — Security, Lean Management and Product Development

Course: `accelerate-lean-management` (`content/accelerate/c4_lean_management/`,
`__init__.py`, `part_a.py`), five lessons. Built to `docs/accelerate/PLAN.md` §C
Course 4, §D, §E, §F and `docs/accelerate/AUTHORING.md`. Reviewed 2026-11-01
against the private extraction of the operator's copy, reading Chapter 6 (PDF
pp. 105–110), Chapter 7 (111–117), Chapter 8 (118–124) and the preface's
research years (27–30) with `page.py`/`book.py`. I did not read the file whole
or `site/`. I wrote only this file; every finding is a recommendation for the
author. Line numbers are `part_a.py` unless stated.

## Gates

- **Preview:** `python3 scripts/preview_subject.py accelerate --course accelerate-lean-management --out …/scratchpad/rev/accelerate-lean-management`:
  6 pages, labcheck 5 executed, 5 with pinned figures, 0 failing; **OK**.
- **`quotes.py`:** 1.1 p. 106, 19 words, OK. 2.1 p. 113, 11, OK. 3.1 p. 115,
  21, LOOSE (case: the lesson capitalizes "Approval"; see S-1). 3.2
  "negatively correlated" p. 115, 2, OK. 3.3 "risk management theater"
  p. 117, 3, OK. 4.1 p. 120, 12, LOOSE (only the comma inside the closing
  quotation mark). 5.1 p. 122, 27, OK. Each lesson has one opening quotation
  of 40 words or fewer and a total of 60 or fewer (lesson 3: 26).
- **`overlap.py … 8`:** every run is a chapter or section title or a counted
  quotation except two. (a) line 242, 10 words, the DevSecOps coiners' names
  and employers: facts, acceptable (N-1). (b) **line 1272, 9 words, the book's
  definition of an MVP in a quiz answer** (M-3).
- **Browser** (Playwright, chromium, `file://`): every preset loaded at
  1280 px; no page or console errors; at 375 px scrollWidth equals
  clientWidth on all five pages. Every tile on every preset (`late`,
  `early`, `quarter`, `limit`, `board`, `one-failure`, `two-failures`,
  `by-hand`, `automated`, `lean-first`, `delivery-first`) matches the
  prose, the worked lines and my own arithmetic (e.g. 360/1,400 = 9/35;
  18/8 ÷ 6/8 = 3; waits 12.5 and 8.75; Sxy 7, Sxx 12, Syy 8, r = 0.714,
  lines 5/3 + 7/12·x and 0.5 + 0.875·x).
- **Exercises typed in**, each agreeing with its quiz `why`: security 282 /
  105 / 177; board 7/3, 1, 7/3, holds; routes cab 60 h, peer 1 h 45 min,
  58.25 h, medians 60 and 1.5, 1/4 each; batches 13 → 5, 13 → 25, 3 → 15;
  teams r = 0.8, 16/25 = 64%, unchanged when swapped.

## MUST-FIX

1. **Line 156, key line "high performers fixed less, in less time".** The book
   reports only time: high performers spent 50% less time remediating
   security issues than low performers (p. 108). Nothing says they fixed
   fewer issues. Replace with: `"high performers: half the time fixing"`.

2. **Lines 373–375, quiz 1.1 `why`, the account of the second option.** "282
   and 105, freeing 387" does not come from adding "the other work's 150
   hours". The other work is 750 hours, and 282 + 150 − 105 = 327. 387 is
   282 + 105. Replace from "The second option…" with: `"The second option
   gives the sum of the two totals as the hours freed; the third compares
   only the after-release rows; the fourth takes the sum as the late figure
   and the early total as the hours freed."`

3. **Line 1272, quiz 4.4 correct answer.** "validated learning about the
   product and its business model" is a 9-word run of the book's MVP
   definition (p. 120). It is not counted as a quotation and is outside the
   overlap allowance. Replace with: `"A prototype with only the features
   needed to learn, by testing it, whether the product and its business
   model are sound"`. That is the lesson's own concept wording (line 1070).

4. **Lines 1154–1162 and 1289–1294: reasoning credited to the chapter.** "The
   numbers show a cost as well as a gain, and the chapter does not hide it:
   small batches finish later in total…" Chapter 8 says nothing about small
   batches finishing later or about release overhead (pp. 118–124). "This is
   why the authors link small batches to the technical practices… they cut
   the price of a release" is the lesson's mechanism, not the authors'. What
   the book does report is weaker: an experimental approach is "highly
   correlated" with the technical practices of continuous delivery
   (pp. 121, 124), and better delivery capability "enables" small batches
   (p. 123).
   - Line 1154, replace with: `"The numbers show a cost as well as a gain,
     which the chapter does not discuss: small batches finish later in total
     when each release is costly."`
   - Lines 1160–1162, replace with: `"The authors report that an
     experimental approach to product development is highly correlated with
     the technical practices of continuous delivery; the arithmetic shows
     one way the two could fit together, since a cheaper release makes small
     batches affordable."`
   - Mistake 2 (1292–1294), replace with: `"…and it depends on the release
     being cheap, which the lab shows and the chapter does not argue; the
     authors report only that the experimental approach is highly correlated
     with continuous delivery's practices."`

5. **Lines 1397–1399: close paraphrase.** "Lean product management practices
   positively impacted software delivery performance, stimulated a
   generative culture and decreased burnout" is the p. 122 sentence with only
   the tenses changed. That is nine-plus words, and the scanner misses it
   only because of the inflections. Replace with: `"In the first model,
   Lean product management practices predicted better delivery performance,
   a more generative culture and less burnout."` This also states the claim
   at the strength the lesson argues for at line 1404.

## SHOULD-FIX

1. **Line 815: the quotation is not character for character.** The book has
   lowercase "approval" mid-sentence ("In short, approval by…", p. 115).
   Write `&ldquo;[A]pproval by an external body…` or start the quotation
   lowercase after "they conclude that".
2. **Line 211: "from design through operations".** Chapter 6 says "from
   development through operations" (p. 106). Design comes in as something the
   experts contribute to. Write "from development through operations".
3. **Line 1386 and lines 1554–1556 (5.4 `why`).** The book says team
   experimentation "is an important factor in predicting organizational
   performance" (p. 122).
   - Line 1386: "matters for organizational performance" drops *predicting*.
     Write "predicts organizational performance".
   - The `why`'s "when combined with the other capabilities" turns the
     authors' advice ("To be effective, experimentation should be
     combined…") into a condition on the finding. Drop the clause, or write
     "and the authors advise combining it with the other capabilities".
4. **Near-runs and close paraphrases in descriptions.** Five to seven words
   each, in the book's order. Recast each in the lesson's own words, at the
   level of the central idea:
   - Line 497 and lines 725–727, "how broadly it is shared, and how easy it
     is to reach" (p. 113).
   - Lines 536–540, "much stronger positive effect on software delivery
     performance" and the overburdened / longer lead times / obstacles to
     flow sentence (p. 113).
   - Lines 546–550: the four things asked about visual displays. This is a
     description of survey items, item by item. Reduce it to "what is shown,
     to whom, and how easily".
   - Lines 852–853, "practices known to improve stability, quality and speed"
     (p. 117).
   - Lines 1105–1112, the four capability descriptions. Keep the names and
     shorten the clauses.
   - Lines 1133–1136, the three feedback practices (p. 121).
   - Lines 1378–1382, "do not delight customers or deliver the expected
     results… capacity to innovate is sharply reduced" (p. 121).

## NOTE

1. Line 242, the names "Topo Pal of Capital One and Shannon Lietz of Intuit":
   facts, acceptable.
2. Line 750: the comment counts lesson 3 at 24 words. With "negatively
   correlated" (2 words, line 823) the total is 26, which is still under 60.
   Update the comment.
3. Lines 1341–1342, the key lines "2016: product practice predicts delivery" and
   "2017: …". The book says the analysis covered "two years, from 2016-2017",
   with a first model and a flipped model "the following year" (pp. 122–123).
   The years are a fair inference, not the book's wording.
4. Lines 1089–1092: the book places the three signs of faux Agile "in larger
   companies" (p. 118). Add the qualifier.
5. Lines 805–809 paraphrase the book's four approval scenarios, which are
   survey answer options. They are close to names and the lab uses only
   `none`/`peer`/`cab`, so this is acceptable, but keep it at that level.
6. Kit wording, not this course's: the tiles print "1 items a day" and "1
   days each" (afl wip and batch status). Report this to the kit owner.
7. Teaching: every lesson closes on the gap (figure of the stated sample,
   not a cause); lessons 1 and 4 say their costs are the lesson's own,
   lesson 3's equal fail rates are labelled "built to match", lesson 5
   separates r's symmetry from the two-year design. I could argue for no
   wrong quiz answer; 5.1's "0.5, and 25 percent" is merely weak. No book
   table, figure or example data is used as lab data.

**Verdict:** accurate and well built, with every lab matching its prose. Make
the five MUST-FIXes before release: two attribution or wording errors about
the book's findings, one wrong quiz explanation, and two copyright overlaps.
