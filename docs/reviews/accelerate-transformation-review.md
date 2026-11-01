# Review (accuracy and teaching): Accelerate, Course 8 — Transformation

Course `accelerate-transformation` (`content/accelerate/c8_transformation/`), five
lessons, against PLAN §C Course 8 and AUTHORING. Reviewed 2026-11-01 against the
pages behind every claim (Ch. 16 pp. 217–240, Conclusion, App. A–B, and the pages
cited elsewhere), never the whole file and never `site/`. I wrote only this file.

## Gates

- **Preview:** `preview_subject.py accelerate --course accelerate-transformation`
  rendered 6 pages; labcheck 5 executed, 5 with pinned figures, 0 failing; **OK**.
- **`quotes.py`:** 8 quotations, 7 OK: L1 p. 220 (24 words); L2 p. 228 (11) and
  p. 228 (5); L3 p. 233 (16); L4 p. 242 (7) and p. 243 (4); L5 p. 252 (28). **L3
  p. 235 (11 words) is a MISS** (SHOULD-FIX 1). Every lesson is under 40 for its
  opening quotation and under 60 in total.
- **`overlap.py … 8`:** 9 runs. All are allowed: the counted quotations (lines 277, 621,
  935, 967, 1551), answer options ("between once per day and once per week", 678,
  736), and the five category names (1529, 1729).
- **Browser (Playwright, chromium, `file://`):** all five pages at 1280 and 375 px:
  no sideways scroll, no errors. Every preset's tiles match my own arithmetic
  (board 40/10 = 4, 8/10, 40/8 = 5; L2 medians 61 h and 19 h, 2/8 and 1/10, restores
  12 h and 3 h; Orchid 9, +4; 2× with odds 4, 1.50× with odds 3; six teams
  18/14/8/13/7/11, team-experimentation in none). Every exercise typed in agrees with
  its quiz `why` (6 and 4 days; 30 h and 20%, 27 h without x3; Pine product and
  process 3 of 4; 2× and odds 6; Willow 2 of 2 and 0 of 5).
- **Attribution and ING.** Chapter 16 is credited to Steve Bell and Karen Whitley
  Bell in `how_to`, the summary, L1–L3 and the L1 quiz. The p. 8 copyright line and
  the Part III intro (p. 217) bear this out. ING appears **only in prose**. All lab
  data are invented: squad items A–H, teams c/d/x, Orchid, Pine, the tree-named
  teams and the group counts. The capability labels are the lab's own. No figure or
  table of the book is used as data.

## MUST-FIX

1. **`part_a.py:1623–1633` (L5): figures the lab does not print.** The lab does not
   print "26 of 48 … 19 of 30", "71 of the 144", "three categories are below half"
   or "36.7 percent". `acpCategories` gives per-team counts only, and the table gives
   yes/no for each capability. The figures are right, but the paragraph presents
   them as the lab's output, and so does the panel title at 1678. Replace from "On
   the preset…" with: "On the preset <code>six-teams</code> the lab prints each
   team's total, 18, 14, 8, 13, 7 and 11 of the 24, and its count in each category.
   Add a category's six counts by hand and divide by its size times six: 26 of 48
   continuous delivery, 5 of 12 architecture, 10 of 24 product and process, 11 of
   30 lean management and monitoring, 19 of 30 cultural. Three are below half, lean
   management lowest at 36.7 percent. The lab's last tile shows team
   experimentation in place in none of the six." Retitle the panel "Six teams'
   capabilities, by category", or report an organization-wide tile to the kit as a
   gap.

2. **`part_a.py:416–419` (L1 step "Check the identity"): wrong reason.** With the
   step's own definitions, throughput is n/T, lead time is S/n and average WIP is S/T.
   The product (n/T)(S/n) = S/T holds for any closed log, so it cannot detect an
   item "started or finished outside your window". The kit refuses such items
   (kit-report, wip "Refuses"). The identity fails only when an item is still open
   at the end. Then the lab's `aflLittle` reads "differs … because 1 item is still
   open". Replace with: "Multiply throughput by lead time. On a log where every item
   is done you get the average work in process back exactly; if an item is still
   open at the end of the window, the two differ, and the lab says which item." In
   step 3 (412–415), add "of the items done" after "Divide the item-days".

3. **Close paraphrase of the Bells (copyright, PLAN §E).** These passages follow
   the source sentence by sentence, below the scanner's 8 words:
   - `610–616` follows the p. 227 routine step by step. Replace with: "The Bells
     describe a routine instead: a problem goes to whoever can help, climbs a level
     when it must, and stays on the board until the answer comes back down."
   - `653–665` follows the p. 232 approach clause by clause, and it is labelled
     "in the Bells' words" though the words are not theirs. Cut it to one sentence
     of your own and drop the label.
   - `945–953` follows the p. 234 coaches and the quarterly cycle closely. Use:
     "That leader hired coaches to challenge everyone, himself first, and his
     managers met each quarter to learn and spent the months between making it
     habit."
   - `997–998` is the p. 238 sentence with one word changed. Use: "Lead by example:
     a new culture is shown, not delegated."
   - `582–584` (L2 concept) repeats the counted quotation without quotation marks.
     Reword it or put it in quotation marks.

## SHOULD-FIX

1. **`part_a.py:936–937` (L3 quotation), MISS.** The book has double quotation marks
   around "implement". The lesson uses `&lsquo;…&rsquo;`, so the quotation is not
   character for character, though the comment at 883 says "quotes.py OK". Keep
   the book's marks or end the quotation before "You can't".
2. **`part_a.py:316–323` (L1).** p. 223 says the squads are "led (in case of IT)"
   by an IT-area lead and that "most" squads mix engineers and marketers. The product
   area lead is a role ING "plan[s] to call" by that name. It is not yet in place.
   Add "for IT" and "most", and say ING "had seen the need for" the role.
3. **`part_a.py:296–297` (L1).** "it closes by saying there is no checklist." That
   remark is in the last section (p. 235). The chapter closes with the mindset
   suggestions and good wishes (pp. 238–239). Change it to "its last section says
   there is no checklist".
4. **`part_a.py:987–988` and `1167–1168` (L3).** "the unstarred practices are not
   yet tested" and "the rest are untested" go beyond p. 236. The book says only that
   the starred practices correlate with high performance and hopes future research
   "will explore the full range". Change both to "the unstarred practices are not
   ones the research has shown to go with high performance".
5. **`part_a.py:1296–1298` and `1468–1469` (L4).** These present the lesson's gloss
   as the meaning of "unequivocal". The book does not define the word. Suggested:
   "The fairest reading of 'unequivocal' is that the survey's results were
   consistent over its years, on the relationships it tested…", and in the mistake,
   "Read fairly, the word is about…".
6. **`part_a.py:1616–1618` (L5).** The comparison is missing: "no more likely, and
   perhaps less, to be high performers". Add "than the survey's teams as a whole"
   (p. 261).
7. **`part_a.py:810` (L2 quiz `why`).** "A chapter lead says they experimented…" This
   is the Bells' narration about Jan Rijkhoff's chapter (p. 231), not his words.
   Change it to "The Bells report that a chapter experimented…".
8. **`part_a.py:372–375` (L1 exercise).** The default preset `board` carries a log,
   and the lab refuses a typed throughput beside a log. Begin with "Choose the preset
   <code>limit</code>, then type…".
9. **`part_a.py:1019` (L3).** The `quarter` preset does not print "Orchid has 13 of
   24". It prints the first date only, and the exercise text admits this for Pine.
   Add a preset `end` with `teams: _teams(orchid=ORCHID_END)` (pin `orchid 13 of 24`
   and the categories line). Alternatively, say "by hand" for the 13 as well.
10. **Unquoted near-runs.** "sustained effort, investment, focus and time" (1277,
    1426) is the p. 242 phrase verbatim. Line 1560 ("24 key capabilities that drive
    … software delivery performance … statistically significant") follows Appendix
    A's first sentence, which PLAN §E says never to quote. Reword both
    ("lasting effort and investment over time"; "24 capabilities that the analysis
    tied to better delivery performance").

## NOTE

- Every other factual claim checks out on its page. These include Ch. 16's
  particulars (pp. 221–235), the Conclusion, the p. 2 endorsement's "causal link",
  Fowler's cautions, and Ch. 12's account of inferential prediction and of causal
  analysis left out. They also include Ch. 15's snowball limit, Ch. 2's
  "consistently twice as likely" and the 2017 noncommercial result, and App. B's
  2014 follow-up (1,000+, 355 companies, 50%, not replicated). The three-measure
  construct, the women share (5/6/6.5%), the top-10% leadership result, and App. A's
  categories and chapter pointers are right too.
- Causal language is careful throughout, and each lesson closes on the sample's
  figure. I could not argue for any wrong quiz answer.
- The `part_a.py:14–16` docstring still says "PHASE A … expect is empty".
- The L2 title keeps PLAN's "Improvement Kata". The lesson says honestly that the
  chapter does not set out its steps.

**Verdict:** accurate, fairly attributed and well-taught. Fix MUST 1–3 (two
lab/prose mismatches and five close paraphrases of the Bells), then ship.
