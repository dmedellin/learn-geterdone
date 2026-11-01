# Review (accuracy and teaching): Accelerate, Course 2 — Measuring and Changing Culture

Course: `accelerate-culture` (`content/accelerate/c2_culture/`, `__init__.py`,
`part_a.py`), four lessons. Built to `docs/accelerate/PLAN.md` §C Course 2, §D,
§E, §F and `docs/accelerate/AUTHORING.md`. Reviewed 2026-11-01 against the
private extraction of the operator's copy (PDF page = footer page). I read
Chapter 3 in full (pp. 63–75), Fowler's foreword (pp. 14–16), the Preface's
research paragraph (p. 24) and Chapter 12's Likert box and inferential section
(pp. 172, 177–178) with `page.py`/`book.py`. I did not read the file whole and
did not read `site/`.

**Scope.** I wrote only this file. Nothing in the course or in PLAN was changed.

## Gates

- **Preview:** `python3 scripts/preview_subject.py accelerate --course accelerate-culture --out …/scratchpad/rev/accelerate-culture`
  rendered 5 pages; labcheck 4 executed, 4 with pinned figures, 0 failing; **OK**.
- **`quotes.py`: 5 quotations, all OK.** 3.1 p. 65 (16 words); 3.2 p. 67 (19);
  3.3 p. 73 (20, opening) and p. 73 (10), lesson total 30; 3.4 p. 74 (25).
  Every opening is ≤ 40 words and every lesson ≤ 60. Each dict carries its PDF
  page comment.
- **`overlap.py c2_culture 8`:** the four quotations; "lead time release
  frequency and time to restore" five times (the measures' names, allowed by
  §E). Nothing else. At 6 words the scan also shows the near-runs listed under
  SF-5.
- **Browser (Playwright, chromium, `file://`).** All four lessons at 375 px and
  1280 px: scrollWidth = clientWidth, no page or console errors. Every preset
  loaded; every tile matches the prose and the worked lines, and I re-derived
  each by hand:
  - `mixed` totals 34, 28, 17, 34, 22, 14, 28 = 177/42 = 59/14 ≈ 4.214;
    bands 2/3/2. `even` totals 25 ×5, 26 ×2 = 177; bands 0/7/0. Median of the
    `mixed` means is 4.667 (quiz 3's distractor note is right).
  - `reversed` 5.75, 5, 3, 6.5, 5.5, 2 → 4.625; items 28/6 ×3, blame 27/6 =
    4.5; line 4/0/2. `forgotten` 4.75, 4.5, 4, 5, 4.5, 3.5 → 4.375; blame 3.5;
    line 4/1/1.
  - `eight` Sxy 10.625, Sxx 10.5, Syy 12.46875, r ≈ 0.929, r² 7,225/8,379 ≈
    86.2%, line −41/84 + 85/84·x. `moved` r ≈ 0.374, 14.0%.
  - `adopted` 126/36 → 149/36, +23/36; per person +1.5, +2/3, +2/3, −1/6,
    +7/6, 0; s1 the only band change. `unchanged` 131/36, +5/36, no band change.
- **Exercises typed in (L3 and L4 were hand-computed by the author; both hold).**
  - 3.1 platform team: 7/3, 13/3, 19/3, 19/6, 29/6; team 4.2; bands 1/3/1 — matches the `why`.
  - 3.2: reversed 6.75, 4, 2.25; unreversed (after editing `blame` to `no`)
    5.25, 4, 3.25 — q1 changes 1.5, q3 1.0, q2 0 — matches.
  - **3.3**: r = 0.9, r² 81/100 = 81%, line −0.5 + 0.9·x; w raised to 4.0 gives
    r ≈ 0.971 (r² 49/52) — matches "about 0.97". But see SF-3 on "onto the line".
  - **3.4**: before 10/3, 29/6, 13/6, team 31/9 ≈ 3.444; after 23/6, 5.5, 2,
    team 34/9 ≈ 3.778; change +1/3; only x2 changes band (to generative) — matches.
- **Book data.** No row of Table 3.1, no Figure 3.1 statement, no footnote
  percentage is used as lab data; the six aspects are named only. The 2016
  31/48/21 split is stated in prose with its year (p. 75 fn 1), correctly.

## MUST-FIX

1. **`part_a.py:863–864` — the 23,000 figure is credited to Chapter 1.** It is
   in the Preface, section "The Research" (p. 24); Chapter 1 begins at p. 35.
   Replace "across its years, as Chapter 1 reports." with "across its years, as
   the Preface reports."

2. **`part_a.py:406–409` — mistake 2 says "the chapter says a team of any kind
   of organization can land anywhere on the scale".** The chapter says no such
   thing. It says only that the authors have worked with US federal government
   teams they would call generative and with startups that are clearly
   pathological (p. 70). The general claim is the lesson's inference, presented
   as the book's. Replace "The type describes where the rules rank against the
   mission, and the chapter says a team of any kind of organization can land
   anywhere on the scale." with "The type describes where the rules rank
   against the mission, and the authors add that they have met generative
   teams in the US federal government and pathological startups."

## SHOULD-FIX

1. **`part_a.py:220–223` and `:392–393` — "so the type is not a matter of an
   organization's size, age or sector" / "so neither size nor age settles the
   type."** These go further than the book's two examples (p. 70), which show
   only that a stereotype can be wrong. Replace them with "so the type cannot be
   read off the kind of organization" and "so the kind of organization does not
   settle the type."

2. **`part_a.py:837` — "The section ends on failure, where the types differ
   most."** The book calls how organizations handle failure "particularly
   instructive" (p. 73). It does not rank the aspects. Replace with "The
   section ends on failure, which the authors single out as telling."

3. **`part_a.py:954–956` — quiz 3.3 `why`: "Raising w's delivery score to 4.0
   moves that team onto the line".** It does not. The old line gives 3.1 at
   x = 4 and the new one (0.9 + 0.7x) gives 3.7, and the other four points are
   not collinear either. Replace with "Raising w's delivery score to 4.0 brings
   it closer to the rising pattern of the other four, and r rises to about
   0.97."

4. **3.2 exercise (`part_a.py:574–578`) and concept (`:482`): the lab cannot
   show each respondent's score "without" the reversal unless the reader edits
   the items box.** `alkUnreversed` prints only the construct mean (25/6 ≈
   4.167), and the table shows reversed scores only. Add to the exercise text:
   "For the scores without reversing, change `blame, flow, yes` to `blame, flow,
   no` in the items box." At `:482` replace "The lab shows the score both ways."
   with "The lab shows the construct mean both ways."

5. **Close paraphrase (copyright, 5–7-word near-runs in definitions).**
   - `:510–524` follows pp. 67–68 sentence by sentence, keeping their order and
     most of their words. The runs include "from several people, often dozens or
     hundreds", "whether, taken together, they measure organizational culture",
     "If several statistical tests confirm both, … called a construct",
     "the items are read and interpreted alike" (7-word run) and "come before any
     test of correlation or prediction".
   - `:527–530` "calculate the mean across all the questions" (6-word run) and
     the next sentence.
   - `:180–189` (Schein): "formed over time as a group makes sense of", "talk
     about the culture of a team" (7-word run), "discuss and even argue over".
   - `:840` "accidents are almost never the fault of" (7-word run).

   Recast each passage in the lesson's own order and words, for example at
   `:510–524`: "The chapter's next step is statistical. With answers from many
   people, the authors test whether respondents read the statements the same
   way and whether the statements belong together; only a set that passes is
   called a construct. Three kinds of test are named: discriminant and
   convergent validity, and reliability (internal consistency). Chapter 13 and
   Appendix C take them up, and this course leaves them there."

6. **`part_a.py:249` — "The Martin Fowler&rsquo;s foreword"** is a typo on the
   rendered page. Replace it with "Martin Fowler&rsquo;s foreword".

## NOTE

- `part_a.py:236` — the prose gives "177 over 42" and the lab prints "59/14 ≈
  4.214". The value is the same, but a reader comparing them may stumble; add
  "(59 over 14 in lowest terms, as the lab prints it)".
- `part_a.py:658` — "8 minus twice the answer, over 4" is negative for q3
  (−1.0). Write "the size of 8 minus twice the answer, over 4".
- `part_a.py:948` — the distractor "r = 0.450 and r squared = 0.200" contradicts
  itself (0.45² = 0.2025), so a reader can rule it out without computing
  anything. "r = 0.900 and r squared = 0.949" would be a better wrong pairing
  (it takes √r for r²).
- `part_a.py:758` — the key line "how a team interacts matters most" is stronger
  than Google's "matters less than" (p. 73). "how a team works beats who is on
  it" is closer.
- `part_a.py:1104` — "Lean management, with … continuous delivery, do affect
  culture": "does" reads better in the lesson's own sentence.
- `part_a.py:200–203` and concept `:147–152` paraphrase Westrum's three
  characteristics of good information (p. 65). They are in the lesson's own
  words and allowed; keep them as they are.
- Teaching: each lesson closes on the material clause's gap (3.1 note on
  perceptions and sample, 3.2 on validity, 3.3 on direction of cause, 3.4 on
  why a score moved). 3.3 is fair to the book's "inferential predictive"
  framing (p. 75 fn 2; pp. 177–178). 3.4 says plainly that a before-and-after
  comparison is not the book's method, and the `unchanged` control is a good
  touch. I could not argue for any wrong quiz answer. Every lab figure is tied
  to the chapter's step (the mean of the items, p. 69; a culture–delivery
  relationship, p. 71), not decoration.

**Verdict:** accurate and well taught, with exact labs and exercises (the L3
and L4 answers check in the lab). Fix the Preface misattribution and the
unsupported "the chapter says" in 3.1 mistake 2, then tighten the close
paraphrase in 3.2.
