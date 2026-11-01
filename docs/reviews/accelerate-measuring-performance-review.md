# Review (accuracy and teaching): Accelerate, Course 1 — Accelerate and Measuring Performance

Course: `accelerate-measuring-performance` (`content/accelerate/c1_measuring_performance/`,
`__init__.py`, `part_a.py`), five lessons, plus `PATH` in `content/accelerate/__init__.py`.
Built to `docs/accelerate/PLAN.md` §A, §C Course 1, §D, §E, §F and `docs/accelerate/AUTHORING.md`.
Reviewed 2026-11-01 against the private extraction of the operator's copy (PDF page =
footer page), reading the pages behind every claim with `book.py` and `page.py`: the
foreword (pp. 14–16), Quick Reference (20–22), Preface (23–31), Chapter 1 (36–43),
Chapter 2 (44–62), the Chapter 12 box (181) and Appendix C, Tests for Classification
(272). I did not read the file whole and did not read `site/`. I wrote only this file.

## Gates

- **Preview: FAILS.** `preview_subject.py accelerate --course accelerate-measuring-performance`
  rendered 6 pages; labcheck executed all 5 labs with no error, but **1 page fails pinned
  figures** (`capabilities-not-maturity`, three pins: see MF-1). The kit's capability
  view changed after the pins were taken (kit-report: `acpLevel` now reads `Atlas 1 (level 1
  of 3)`, `acpFewest` names at most 3 ties). The other four lessons pass.
- **`quotes.py`: 6 quotations, all OK.** 1.1 p. 38 (18 words); 1.2 p. 46 (9); 1.3 p. 47
  (15); 1.4 p. 53 (20); 1.5 p. 58 (15) and p. 62 (9), 24 in the lesson. All openings ≤ 40,
  all lessons ≤ 60, each with its PDF page in the dict comment.
- **`overlap.py … 8`.** Every run is a section title, a capability or category name, the
  four measures' names, an answer option or a counted quotation, **except two quiz
  options**: `part_a.py:1377` (8 words from the Surprise! box) and `part_a.py:1660`
  (8 words from the Driving Change spoiler). See SF-5.
- **Browser (Playwright, chromium, `file://`).** All five lessons at 375 px and 1280 px:
  scrollWidth = clientWidth, no errors. Every preset's tiles match the prose except
  MF-2. Each exercise, typed in, agrees with its quiz `why` (Cove level 2 hiding
  monitoring; 24 h; 100 % refused; 2 h and 25 %; 1/2, 1, 99/4 then 0, 2/3, 95/6; 2×,
  +45, 11).
- **My own arithmetic.** Ward's merges recomputed exactly: 1/2, 5/6, 1, 3/2, 5/3, 5/3,
  23/6, 25/2, 63; totals 11 and 47/2; all group medians, both logs' lead times and
  restores, and every profile and level are right.
- **PATH.** 5+4+7+5+7+7+6+5 = 46 lessons, eight courses, as the tagline and description
  say; `material` is PLAN §A's word for word; `test_the_tagline_and_description_state_the_real_counts`
  and `TestGeneratedPathIsCurrent` pass.

## MUST-FIX

1. **`part_a.py:370`, `:380`, `:382` — stale pins; the gate fails.** Replace with the
   strings the page prints (checked against my own counts):
   - `:370` `"acpLevel": "Atlas 1 (level 1 of 3)"`
   - `:380` `"acpLevel": "Atlas 1 (level 1 of 3); Brook 2 (level 2 of 3)"`
   - `:382` `"acpFewest": "0 of 2 teams: loosely-coupled-architecture, value-stream, team-experimentation and 3 more (the table lists all)"`

2. **`part_a.py:342` — prose says the tile lists all six; it now names three.** "with two
   teams it lists the 6 that neither has, from loosely coupled architecture to
   transformational leadership" → "with two teams it names three of the 6 that neither
   team has and counts the rest, and the table lists all six, from loosely coupled
   architecture to transformational leadership; so it is only a pointer."

3. **`part_a.py:995–996` — change fail rate misdefined in the steps.** "the share of
   deployments that failed" is not the book's measure, which is the percentage of
   *changes* to production that fail (p. 50–51), nor the lab's (failed / changes
   deployed). On `batched` the two differ: 2/7 changes against 1/3 deployments. Replace
   with "the share of the changes deployed that failed".

4. **`part_a.py:1513` — the fear passage is credited to the authors, and reworded.** On
   p. 62 the book quotes Humble, Molesky and O'Reilly, *Lean Enterprise* (2014), and
   Deming's line is inside that quotation; the passage's subject is pathological and
   bureaucratic cultures, not "where fear rules". Replace "Where fear rules, they say,
   numbers become a tool of control and information that challenges the rules is hidden,
   and as Deming said," with "In pathological and bureaucratic cultures, runs a passage
   the authors quote from Humble and colleagues' *Lean Enterprise* (2014), measurement
   becomes a means of control and people keep back what would unsettle those in charge;
   and, in Deming's words as that passage gives them,". Mistake 2 (`:1676–1678`) may
   keep "fear" but should say "in a pathological or bureaucratic culture".

## SHOULD-FIX

1. **`part_a.py:917–918`.** "over a weekend and an overnight wait": the log has no
   weekdays, and if days 6–7 are the weekend, c03 (day 3→4) and c07 (day 10→11) are both
   overnight. → "two waits overnight".
2. **`part_a.py:1488`.** "a measure for noncommercial organizations": the 2017 measure is
   of noncommercial *goals*, which the book applies "whether you're trying to generate
   profits or not" (p. 58). → "a measure of noncommercial goals, which any organization
   has".
3. **`part_a.py:1642` (quiz).** "Productivity" can be argued for: the noncommercial goals
   include operating efficiency (p. 59), and the Preface calls the noncommercial outcomes
   "effectiveness, efficiency, and customer satisfaction" (p. 23). Replace with "Revenue
   growth" (p. 58 says the measure goes beyond profit and revenue) and add it to the `why`.
4. **`part_a.py:1536–1537`.** "two groups drawn by the clustering in one survey": the
   book's figure is "analysis over several years" (p. 58). → "in each year's survey".
5. **Quiz options that are 8-word book runs.** `:1377` → "Medium performers had a worse
   change fail rate than the low group"; `:1660` → "Their correlation with both tempo and
   stability is negative".
6. **Close paraphrases (5–7-word near-runs in definitions).**
   - `:1163–1173`, cluster analysis: follows p. 51 clause by clause ("Each measurement is
     put on … dimension", "no understanding of the …", "what counts as a good or a bad
     response on any measure"). Suggest: "They use cluster analysis, which sorts responses
     into groups whose members resemble one another more than they resemble anyone outside.
     The four answers are four axes; the method sees only how far apart responses lie, and
     cannot know that one answer is better than another. That, they say, lets the industry's
     groups emerge without a prior view of what good looks like." The concept at `:1140–1144`
     and the `why` at `:1362` are fine once this changes.
   - `:272–275`, Fowler: "surveys that capture subjective perceptions … how well the sample
     reflects the IT world … when other teams, using other approaches, confirm the
     reasoning" tracks p. 16 phrase by phrase. → "The answers are people's perceptions, he
     notes; he is unsure how representative the respondents are; and he wants independent
     work by other methods to confirm the results."
   - `:604–606`, slack: "no spare capacity, or slack, remains to absorb unplanned work,
     changes of plan or improvement work" (p. 46) → "nothing is left over for the unplanned,
     for a change of plan or for improving the work".
   - `:897–900`, change fail rate: keep the definition, drop the run of four remedies →
     "that degrade service or have to be remedied".
7. **`part_a.py:337`.** "strong in four categories and ahead on culture" overstates 1 of 2
   and 2 of 4. → "a team with something in place in every category, and 4 of 5 in culture".
8. **`content/accelerate/__init__.py`, prerequisites, third item.** "*System Design, Read
   Along*" is not that path's title; it is *System Design* (`content/system_design/__init__.py:49`).
9. **`part_a.py:1458–1461` and key `:1444`.** The book never says how "twice as likely" was
   computed (pp. 58–59, 253). The body says so at `:1533`; the concept should too: add "The
   book does not give its computation; this is the plain reading of the phrase."

## NOTE

1. **Table 2.3 in prose (`:1187–1196`).** The paragraph gives 7 of the table's 12 cells and
   its footnote. PLAN §C allows the tables "described in prose", and it is fairly done; two
   or three cells would be enough to carry the argument.
2. **The footnote to an appendix (`:1182`).** Chapter 2's footnote 3 (p. 62) points to
   Appendix B, while the method is in Appendix C (p. 272). "an appendix" is a careful
   hedge; it is right.
3. **Coding and distance are the lab's (`:1228–1235`).** The book does not say how answers
   were coded for clustering or which distance was used (p. 272). One clause, "this coding
   is the lesson's; the book does not give its own", would keep a reader from crediting it
   to the authors.
4. **Fairness to the book's own claim.** The lessons give Fowler's cautions well. The
   authors also say outright that their findings will apply to the teams in your
   organization (p. 43); lesson 1 or its third mistake could say so and set Fowler's
   caution against it, which is fairer than leaving only the caution.
5. **Supported by the pages.** Every other figure and claim: the Preface's counts and years,
   the four reasons, the three non-predictors, 46 / 440 / 170 / a fifth (2017), the options,
   the clustering criteria, the Surprise! box, the organizational measures, arrows as
   prediction, the CAB spoiler. No finding is stated as a cause; every lesson closes on the
   material clause's gap; no other wrong quiz answer can be argued for; no lab uses the
   book's data.

**Verdict:** accurate and well taught, but not shippable until MF-1 (the preview gate) and
MF-2–MF-4 are fixed; the SHOULD-FIX items are short wording changes.
