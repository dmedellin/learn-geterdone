# Review (accuracy and teaching): Accelerate, Course 5 — Sustainable Work, Satisfaction and Leadership

Course: `accelerate-people` (`content/accelerate/c5_people/`), seven lessons, built to
`docs/accelerate/PLAN.md` §C Course 5 and `AUTHORING.md`. Reviewed 2026-11-01 against the
private extraction, with `book.py` and `page.py`. I read Ch. 9–11 (pp. 125–168), the Preface
(pp. 24, 30–31), Ch. 15 (pp. 212–215) and App. A (pp. 254–263). I did not read the file
whole or `site/`. I wrote only this file.

## Gates

- **Preview:** 8 pages; labcheck 7 executed, 7 with pinned figures, 0 failing; **OK**.
- **`quotes.py`:** 6 OK and 1 LOOSE (MF-2): p. 126 (20 words), 131 (20), 142 (14), 145 (28,
  LOOSE), 148 (11), 161 (11), 163 (14). Each lesson has one quotation, so each is under 40
  words and under 60.
- **`overlap.py … 8`:** the quotations, the authors' names, the section titles and the five
  dimension names are allowed. part_b.py:600 (the three culture constructs) is allowed as
  construct names. Two quiz options are not allowed (MF-3). One 8-word run is split by a page
  footer, so the scanner misses it (SF-8).
- **Browser (Playwright, `file://`):** all seven pages at 375 and 1280 px. None scrolls
  sideways, and there are no page or console errors. I checked every preset's tiles by hand:
  Sxy 260/120, Sxx 4,200, Syy 18/16; burnout 53/12 and 23/6; eNPS +10/+20/+10; Alder 5.25/5
  and Birch 3.25/5; dimension sums 73, 64, 57, 67, 36 (later 49); odds 40,800/16,800 ≈ 2.43
  and 169/49 ≈ 3.45; and the confounded split. All match.
- **Exercises, typed in:** each one agrees with its quiz `why`. Pain r² 121/140; burnout 3
  (29/9 with nothing reversed); eNPS −10; Cedar 16/3 and 23/6; diversity 1.50×, +10 points,
  odds ≈ 1.71; metrics 3×, +40 points, odds 6. Lesson 6's exercise gives totals only, so it
  cannot be typed in.

## Diversity in Tech: figures and years

I checked each of these against pp. 147–154 and p. 262, and each is right:

- Rock and Grant 2016, Deloitte 2013 and Hunt et al. 2015.
- "Few teams are diverse"; inclusion after Smith and Lindsay.
- Gender first asked in 2015; 5% / 6% / 6.5% for 2015–2017.
- 7% (2011) and 13% (2008) of systems administration; 27% (Diaz and King 2013).
- 33 / 56 / 81%. The book gives no year, and the lesson says so.
- 91 / 6 / 3% in 2017; why the survey began with binary gender.
- 77 / 12 / 11% (Figure 10.4, 2017); the reason for self-identification; disabilities not
  yet studied.
- Woolley and Malone; Leslie et al.; 45% (Quora 2017); the three resources.
- Over 23,000 responses (p. 24); the outreach to underrepresented groups' own lists (p. 214).

The topic is treated plainly and with respect. The lesson uses the book's own terms, and its
groups are abstract and invented, so nothing in it ranks a real group. The fixes below are
about precision and fairness.

## MUST-FIX

1. **part_a.py:1389, 1395, 1400, 1527, 1534 (and 1479, 1486 to match).** The prose says the
   lab reports "a ratio of 2.00" and "1.00"; the lab prints `2×` and `1×`. Write: "a ratio
   of 2× (Group A is twice as likely to answer)"; "the ratio is 1× and the gap 0 points";
   "The ratio, 2× in the first wave, …; the odds ratio, ≈ 2.43, is a different number".
   Quiz: "the lab reports a ratio of 1×"; why: "A ratio of shares is 1 when the shares are
   equal". Worked: "30/15 = 2"; after: "about 2.43, is not the ratio of shares, 2."
2. **part_a.py:1037.** The quotation opens "People", but p. 145 has "people" in mid-sentence,
   so `quotes.py` reports LOOSE. Write "&ldquo;[P]eople who feel supported…" and run
   `quotes.py` again.
3. **part_b.py:308, 610.** Both quiz options are 10-word runs of the book that are not counted
   as quotations (pp. 161, 163). Replace 308 with "They were no more likely, and possibly
   less likely, to be high performers than teams overall". Replace 610 with "The two are
   highly correlated".

## SHOULD-FIX

1. **part_a.py:1373–1382, fairness on sampling.** A reader can take the caution to mean that
   the low share of women is an artefact of sampling. The book does not say that. The authors
   treat the share as a real shortfall and were hoping for better numbers (p. 148). Chapter 15
   says the population cannot be identified (p. 213), so response rates are unknowable for
   the real survey. Add: "Nothing in the book says which way, if at all, its share differs
   from the field's. The authors read the low figure as a real shortfall, and the team figures
   (33, 56, 81 percent) point the same way. The field cannot be counted (Chapter 15), so the
   lab assumes a known field only to show the mechanism."
2. **part_a.py:1338–1346.** The lesson gives 6.5% for 2017 and then 6% in the 2017 breakdown
   without comment. The book does the same (pp. 148, 150, 262). Add: "The chapter gives 6.5
   percent for 2017 in one place and 6 percent in its 2017 breakdown, and does not reconcile
   them."
3. **part_a.py:1341.** "because they cite about 7 percent" reads as if the citing caused the
   surprise. Write: "lower than they expected, given outside figures of about 7 percent women
   in systems administration in 2011 (13 percent in 2008) and 27 percent in computer and
   information management (Diaz and King, 2013)."
4. **part_a.py:1366–1367.** The "innate brilliance" explanation comes from Leslie et al. 2015,
   but the lesson credits it to "the authors", and the wording is a near-run of the book.
   Write: "Citing Leslie and colleagues (2015), they suggest that a widespread belief in some
   men's innate gift for technical work may keep women and others out. A footnote says that
   study covered only women and African Americans."
5. **part_a.py:1409–1412, 1401.** "Type the rows in to check" comes after a question about Q's
   share of the answers, which the lab does not print. Write: "Type the rows in to check the
   shares, ratio and gap; the share of the answers is by hand." At 1401, the diversity
   sections never say "times as likely". Write: "what the book means by 'times as likely' (as
   in Chapter 10's loyalty finding)".
6. **Decimals worked by hand where the lab prints whole numbers.** These are confusing, not
   wrong. part_a.py:645/652 "3.00" (lab `3`); 1100, 1102, 1183, 1185, 1213 "5.00" (lab `5`);
   part_b.py:192, 276, 279, 334 "3.00" (lab `3`); 481, 571, 592, 596, 621 "1.00" (lab `1×`);
   578/584 "3.00", "6.00" (lab `3×`, `6`). Use the lab's forms.
7. **part_a.py:197.** "The text says *correlated* and *predicts*" is wrong. The section says
   "high correlation" (p. 128). Write: "The text calls the second a high correlation, and the
   lesson keeps to that word."
8. **Close paraphrase (5–8-word runs).**
   - Inclusion, part_a.py:1296–1297 and 1549: this follows Smith and Lindsay's definition and
     repeats "for diversity to take hold". Write: "an organization where every member is
     welcomed and belongs; the authors say diversity does not last without it."
   - part_a.py:1324 and 1524: "recruit and retain more women and underrepresented
     minorities" is 8 words of pp. 147–148, split by the footer. Write "hire and keep more
     women and members of underrepresented groups".
   - Burnout, part_a.py:446 and 470–472: the opening definition is paraphrased twice. Keep
     one, shorter.
   - part_b.py:152 "followers to identify with the organization and". Write "transformational
     leaders aim at followers' commitment to the organization's goals".
9. **part_a.py:1018, 1050–1052.** Together these paraphrase all six identity survey items,
   one by one (p. 143), which PLAN §E rules out. Write: "six statements adapted from
   Kankanhalli and colleagues (2005), on being glad to work there, sharing the
   organization's values and goals, and the like."
10. **part_a.py:1060, 1082.**
    - At 1060, "the more people identified…, the more it predicted" misstates p. 145, and
      "predicted a generative, performance-oriented culture and" is a near-run. Write:
      "Identity predicted both a generative culture and organizational performance
      (productivity, market share, profitability)."
    - At 1082, "in the authors' words" introduces "predict", but the book says "results in"
      (pp. 145–146). Drop "in the authors' words".

## NOTE

- **Kit:** three points.
  - The table's share column in groups/likely reads `= 30%`, with nothing before the
    equals sign.
  - Ratios print `2×` but `1.50×`.
  - No tile gives the sample composition, which is the diversity lesson's main point.
- part_a.py:200: the Bing figures of 38 and 75 percent are in the book's box. The box does
  not plainly attribute them to Almeida.
- part_a.py:484: "financial interest" softens the book's "fiduciary obligation".
- part_a.py:1198: the distractor 4.17 matches no slip a reader is likely to make.
- part_a.py:759: "answers that falls" should be "answers that fall".
- I tried to argue for each of the other wrong quiz answers and could not.

**Verdict:** the course is accurate and teaches well, and every diversity figure and year is
right. Before release, fix the three MUST-FIXes and add the sentence on sampling (SF-1).
