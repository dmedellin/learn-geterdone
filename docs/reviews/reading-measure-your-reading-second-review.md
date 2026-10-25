# Second review — Measure Your Reading (Reading Faster, course 1)

Independent second read of `content/reading/c1_measure/` (`__init__.py`,
`part_a.py`) against `docs/reading/PLAN.md` (§0, §B, Course 1 in §C, §D.3,
§F, §G, §S, §R), `docs/reviews/reading-spec-accuracy-review.md`,
`docs/reading/AUTHORING.md` and `docs/reading/kit-report.md`, following
`docs/reading/SECOND-REVIEW.md`. The findings below were written before the
pedagogy assessment (`docs/pedagogy/reading-measure-your-reading.md`) was
read; the disagreements are at the end.

## Method

- Every lesson dict read in full; every passage the course uses (`P01`–`P05`,
  `P09`, `P10`) has its questions read, with the passage text consulted for the
  doubtful ones. Word counts as the kit counts them: 491, 460, 427, 498, 461,
  494, 486, all standard band.
- Rendered with `python3 scripts/preview_subject.py reading --course
  reading-measure-your-reading --out <scratch>/sr-reading-measure-your-reading`;
  every preset's tiles read with `node scripts/labcheck.js --observe` on all
  five pages.
- Every figure in prose, worked lines, quiz answers, `why`s and standards
  recomputed by hand.
- The whole course done in Chromium (Playwright, controlled clock) in one
  browser profile, as a reader who starts with an empty log would: the `P01`
  drill, the `P02`/`P03` compare, both warm-ups of lesson 3 then "Use my
  baselines", the `P09` warm-up then "Use my baseline median", the `P10`
  warm-up and the reader's own history. The passage was hidden during every
  question; every reading wrote exactly one entry with the kind §C gives
  (`baseline`, `condition`, `baseline`, `baseline`, `test`, `practice`,
  `practice`); no console or page error.
- Research claims checked against §S and the accuracy review. Rayner et al.
  (2016) additionally against its published abstract (Washington University
  profile; APS press release). Jackson and McClelland (1979) could not be
  reached online; the claim is checked against §S only.

## Arithmetic (all correct)

| Where | Figure | Check |
| --- | --- | --- |
| 1 body | 491 × 60 / 120 = 245.5; 2,652 / 6 = 442; 442 × 60 / 120 = 221; 2,652 / 491 ≈ 5.4 | ✓ (drill tile printed `245.5 wpm`, `221 standard wpm`) |
| 1 presets | 400 × 60 / 96 = 250; 2,640 / 6 = 440; 440 × 60 / 96 = 275; 160 s → 150 and 165 | ✓ |
| 1 mistake | 250 × 5.4 / 6 = 225 | ✓ |
| 1 quiz | 600 × 60 / 150 = 240; 600 / 1.5 = 400; 3,300 / 6 × 60 / 150 = 220; 3,300 / 600 = 5.5 | ✓ |
| 1 standard | 520 × 60 / 130 = 240; 2,880 / 6 × 60 / 130 ≈ 221.5 → 222 | ✓ |
| 2 presets | 240/240, 480/160, −80, 2/3; 320 × 5/6 ≈ 266.7, ≈ +26.7, 10/9 | ✓ |
| 2 worked | 480 × 4/6 = 320 | ✓ |
| 2 quiz / standard | 300 × 4/6 = 200; 480 / 6 = 80; 450 in 90 s and 135 s → 300 / 250 and 200 / 200 | ✓ |
| 3 presets | mean 734/3 ≈ 244.7; ranges 13 and 56; 262 − 251 = 11; median 262 | ✓ |
| 3 note | median of three tests above three baselines ⇔ the top two of six are tests: 3/15 = 1/5 | ✓ |
| 3 quiz / standard | 230–252 (22); 255 once; median(249, 258, 262) = 258; 236–249, median 251, 247 inside | ✓ |
| 4 presets | 238 × 6.6 / 6 = 261.8 (38.2 / 61.8); 238 × 5.4 / 6 = 214.2; 190 × 6.6 / 6 = 209; 95/119 ≈ 79.8%; 500/119 ≈ 420.2% | ✓ |
| 4 body | 250 × 6 / 5.4 ≈ 277.8 ("about 278") | ✓ |
| 4 quiz / standard | 250 × 5.4 / 6 = 225; 3,300 / 500 = 6.6; 260 × 6.6 / 6 = 286 (14 from 300) | ✓ |
| 5 presets | 301.2 × 5/6 = 251, 294 × 5/6 = 245; 306, 262, 324, 319.2 → 255, 262, 270, 266, median 266; 288, 354, 488 → 240, 236, 244, median 240 | ✓ |
| 5 standard | 236–247; median(250, 245, 252) = 250 | ✓ |

## Findings

### 1. Comprehension and the Effective Rate: the baseline was taken after the sprint (fixed)

The compare used `order: "alternate"`, which the kit sets from the parity of
the log's length at load. A reader following the course arrives with exactly
one entry (lesson 1's baseline), so the order is BA for essentially every
reader: confirmed in the browser ("Read B first, then A"). The natural-pace
reading, logged as a **baseline**, was therefore taken straight after a reading
"as fast as you can" — the very after-effect Sprints Above Comfort sets out to
test — and the body's own exemplary paragraph ("If the second was faster…")
assumed the fast reading came second. The alternation was not alternating, and
it contaminated one of the three baselines every later verdict uses.

*Changed:* `order: "AB"`; the first `p`, the confounds `p`, the third concept
and the `note` now say the natural-pace reading always comes first and why
(so the warm-up and fatigue fall on the fast reading). §C 1.2's Lab line
records `order: AB` and the reason. Re-checked in the browser with a
one-entry log: "Read A first, then B."

### 2. Comprehension and the Effective Rate: the verdict tile on a deliberately fast reading (fixed in text; kit recommendation)

`drVerdictB` sets rate B — here the as-fast-as-you-can reading — against the
baseline range, and on a revisit (three baselines logged) it prints "above
the baseline range once — a fourth reading does this about one time in four".
For a reading the reader pushed on purpose that chance wording is wrong.
*Changed:* the paragraph that introduces the tile now says the chance wording
is written for natural-pace tests and does not apply to a pushed reading.
*Recommend (kit):* a compare cfg switch that drops `drVerdictB` when B is a
`condition` side, as it already is for paced sides.

### 3. Comprehension and the Effective Rate: "a guess from general knowledge fails" (fixed)

The body said the questions "were written so that a guess from general
knowledge fails". Several cannot meet that for every reader: `P03` Q5 (the
horn "every two minutes … as the rules required" — the fog-signal interval
any sailor knows), `P02` Q5 (glutenin, for a baker) and Q2 (a slow cold rise
for flavour). *Changed:* "written to be answered from the passage, not from
general knowledge, though a reader who happens to know a topic may still get
one without it."

### 4. Keeping a Practice Log: the verdict the reader actually sees (fixed)

Doing the course with natural-looking numbers (test `P05` at 276.6 wpm with
4 of 6), lesson 3 said "above the baseline range once" and this lesson said
**"below the baseline range"** (effective 184.4 against 204.6–259.8). The body
prepared the reader for "above in words, inside in understood words" only.
*Changed:* "inside, or even below, it in understood words".

### 5. Research claims (no change needed)

- Brysbaert (2019): 238 nonfiction, 260 fiction, 183 aloud, words not
  standard words, 300 an overestimate — as §S and the accuracy review.
- Carver (1990) gears, college students, standard-length words; Carver (1992)
  constancy and deliberate shifting — at the accuracy review's strength; the
  "flexible reader" misattribution is absent.
- Rayner et al. (2016), "published after Rayner's death in 2015" — correct
  (he died in January 2015). The point attributed to them (a test passable
  without reading says nothing about the reading) is consistent with the
  review's discussion of speed-reading claims; not verifiable from the
  abstract alone.
- *Recommend (low):* Jackson and McClelland (1979) "used this product … to
  compare readers who traded speed against understanding in different
  amounts". They used effective reading speed to rank readers' ability
  (fast against average readers). "to rank readers, so that speed bought
  with understanding did not count as skill" is closer.

### 6. Smaller points (recommendations)

- **One Reading Is One Measurement, steps:** "Your range is the lowest and
  highest of your first three natural-pace readings" while the note says "this
  lab uses all your baselines for the range", and the kit does. Harmless while
  the course takes exactly three; "of your baseline readings" would agree with
  the kit.
- **One Reading Is One Measurement, mistake 1:** "even the tight reader's 13
  is wider than the difference most comparisons in this Subject will show" is
  a forecast the lesson cannot support and mixes rates with effective rates;
  suggest "wider than many of the differences later comparisons show".
- **Keeping a Practice Log:** with fewer than six sessions the kit's
  `lgRecentMedian` prints "after 6 sessions" beside a verdict that is already
  "below the baseline range"; the reader may read that as contradictory. A kit
  wording point ("needs three tests").
- **Exchangeability:** the one-in-four and one-in-five figures assume the four
  (six) readings are interchangeable; the body says passages vary (Carver
  1990) and the note calls the rule a rule of thumb. Fair as written.

## Quiz and passages

Every quiz question has one defensible answer; every distractor was argued
for and fails (lesson 3 Q3's "inside the range, because 249 is inside" is the
intended trap; lesson 4 Q3's "Brysbaert converted Carver's figures" is false).
Option length gives no cue: across the fifteen passages this course and
Guided Practice use, the correct option is the longest in 19 of 90 questions,
and the four answer positions are used 22, 23, 23, 22 times.

Passage questions answerable without reading (report only; passages not
edited): `P03` Q5 (fog-horn interval, from the collision rules), `P02` Q5
(glutenin) for a baker, `P05` Q3 (why lights have characteristics) and Q5
(why lights are kept running) by reasoning alone. None has two defensible
answers on my reading.

## Voice (§F)

Warm, practical and about the reader's own numbers ("If you took exactly two
minutes…"); no promises; no "your reading speed" except as the thing a
measurement is not; the speed-reading tradition does not appear in this
course, so §F's "stated at its strongest" does not bite. No changes.

## Preview after the changes

`python3 scripts/preview_subject.py reading --course reading-measure-your-reading`:
`5 page(s) executed and swept, 5 with pinned figures, 0 failing` — `OK`.

## Where I disagree with the pedagogy assessment

(Read after the findings above were written.)

- **The compare order of lesson 2.** The assessment saw that "the page put
  the fast reading first, since the log had one entry" and treated it as a
  matter of telling the reader in advance. I think it is a measurement defect
  (finding 1): the alternation is deterministic for a course-following reader,
  so it never alternates, and it puts a sprint immediately before one of the
  three baselines that every later verdict in the Subject depends on. It also
  contradicted §F's exemplary paragraph, which the assessment praises as being
  "word for word, in the place §F put it" — that paragraph assumes the fast
  reading came second. Changed to `order: AB`.
- **"Questions written to fail a guess."** The assessment lists lesson 2's
  Rayner sentence ("the questions were written so that a guess from general
  knowledge fails") under good use of history. The sentence claimed more than
  the passages deliver (finding 3); softened.
- **The two verdicts on one test.** The assessment's run reports the test
  becoming "inside" at 184.4 understood words a minute. With the baselines a
  run of that shape logs (effective 204.6 to 259.8), 184.4 is *below* the
  range, and the kit said "below the baseline range" in my run with the same
  figures. The lesson's added sentence covered only "inside"; it now says
  "inside, or even below".
- **`mistakes[0]` of One Reading Is One Measurement.** The assessment
  rewrote "13 is still more than many claimed gains" to "wider than the
  difference most comparisons in this Subject will show", citing differences
  of 8 and 48. Half of those examples exceed 13, so "most" is not shown; I
  recommend "wider than many of the differences later comparisons show"
  (not changed: taste).
- **`P05` Q1.** Agree that it stands. I add `P05` Q3 and Q5 and `P03` Q5 as
  answerable without the passage, which the assessment, having read all
  forty-two questions, did not flag.
- Agreed: the arithmetic, the drill-first discipline, the kinds, the voice,
  the kit's "is is approximately" panel sentence, and the recommendation for a
  fourth baseline somewhere later.
