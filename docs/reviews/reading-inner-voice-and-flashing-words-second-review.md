# Second review — The Inner Voice and Flashing Words (Reading Faster, course 4)

Independent second read of `content/reading/c4_inner_voice/` (`__init__.py`,
`part_a.py`) against `docs/reading/PLAN.md` (§0, §B, Course 4 in §C, §D.3,
§F, §G, §S, §R), `docs/reviews/reading-spec-accuracy-review.md`,
`docs/reading/AUTHORING.md` and `docs/reading/kit-report.md`, following
`docs/reading/SECOND-REVIEW.md`. Findings were written before the pedagogy
assessment (`docs/pedagogy/reading-inner-voice-and-flashing-words.md`) was
read; the disagreements are at the end.

## Method

- Every lesson dict read in full, and every passage the course uses counted
  with the kit's rule: `P25` 477 (easy), `P26` 453 (easy), `P27` 409 and `P28`
  402 (standard, FK grade 10.07 and 10.18), `P29` 403, `P19` 459, `P20` 438
  in 127 phrases of 2–5 words (23, 47, 34, 23), `P30` 391, `P31` 403, `Q20`
  423. `P30` and `P31` read in full with their questions.
- Rendered with `python3 scripts/preview_subject.py reading --course
  reading-inner-voice-and-flashing-words --out <scratch>/sr-reading-inner-voice-and-flashing-words`;
  every preset's tiles read with `node scripts/labcheck.js --observe`.
- Every figure recomputed by hand (below).
- Every drill done in Chromium (Playwright, controlled clock): aloud then
  silent, and the "I can't read aloud here" fallback; the suppression pair
  with the tick; the RSVP single with three baselines in the log, "Use my
  baseline median", the 600 felt-pace run with Reset at the questions, and
  650 refused; word against phrase streams; pacer against stream; the `Q20`
  warm-up; all pages at 360 px. No failures, no console or page errors.
- Research claims checked against §S and the accuracy review; Schotter, Tran
  and Rayner against the published abstract (see the Course 3 review); I
  tried and failed to reach Slowiaczek and Clifton's method section (finding
  2).

## Arithmetic (all correct)

183/60 → 183, 476/120 → 238, 238/183 ≈ 130.1%; 477/159 → 180, 453/84.9375 →
320, 16/9 ≈ 177.8%; quiz 200, 300, 1.5, 9/8, 2/3. Suppression: 409/98.16 →
250, 402/90 → 268, × 4/6 = 536/3 ≈ 178.7, −214/3 ≈ −71.3; 403/93 → 260,
399/90 → 266, × 5/6 ≈ 221.7, ≈ −38.3; quiz 208.3, 180, ≈ −28.3. RSVP:
403/96.72 → 250, 48.36 → 500, 40.3 → 600; 240, 120, 100 ms; 30/255 ≈ 11.8%;
150 ms, 6.7, 2.5; 250 ms seen ↔ 240 wpm. Phrases: 459/110.16 and 438/105.12
→ 250; 125, ≈ 208.3, ≈ +83.3; 438 × 60,000/(250 × 127) ≈ 827.7; 438/127 ≈
3.4; 960, 480, 600 ms. Pacer/stream: 391/78.2 and 403/80.6 → 300; 200; −100;
quiz 250 − 150. Claim: 19.125, 38.25 (= 2.55 × 15), 267.75; 375, 750, 5,250;
90,000/238 ≈ 378 min; 120, 60 min, ≈ 8.6 min; 1,500 inside 15 needs ≤ 100
ms; 1,000 → 25.5. The page tiles agree with all of these.

## Findings and changes

Changes are in `content/reading/c4_inner_voice/part_a.py` and the Course 4
lesson 2 entry of `docs/reading/PLAN.md` §C. No preset, `expect`, slug, mode,
view or passage changed by this review. After them: `7 page(s) rendered … 6
page(s) executed and swept, 6 with pinned figures, 0 failing … OK`.

1. **the-inner-voice — reading aloud stated as speaking.** "On average, adults
   read silently about 1.3 times as fast as they speak" (body), "as fast as
   they speak" (worked), "1.3 times the speed of speech" (`mistakes[0]`).
   Brysbaert's 183 is a rate of *reading aloud*, not of speech; the lesson's
   argument uses it as the proxy for speaking pace, which is fair, but the
   sentences state the published figure as something it is not. **Changed**
   all three to "read aloud" / "the pace of reading aloud". The reader's own
   ratio sentences ("faster than you can speak") are left: there the aloud
   reading is the reader's own speaking pace.
2. **silencing-the-inner-voice — "had readers count aloud, as in this
   drill".** The drill asks for counting *under the breath* ("mouthing the
   numbers without sound is enough"), so "aloud, as in this drill" is
   self-contradictory; and §S and the accuracy review say only "articulatory
   suppression (counting)", not that it was aloud. I could not reach the
   method section to settle it. **Changed** the body to "had readers count
   while they read, the method this drill copies" and `mistakes[0]` to
   "counting while reading impaired comprehension of passages", and the same
   in §C. If the study did count aloud, the lesson should add that the drill
   is a milder version (recommendation).
3. **testing-a-speed-claim — "well under half".** Bringing 1,500 wpm inside
   the perceptual span needs fixation + saccade ≤ 100 ms; the average
   fixation alone is 225, so 100 is 44%: under half, not "well under".
   **Changed** to "less than half" in the body and `mistakes[2]`, and
   `mistakes[2]` now says the 100 ms is "just to come within the perceptual
   span" (within the identification span it would be about 53 ms), so the
   figure is not read as what full reading would need.
4. **§C out of step with the lesson.** §C Course 4 lesson 2 still recorded
   the old `typical` instance (392 words in 96 s → 245; 393 in 90 s → 262 →
   ≈ 174.7; ≈ −70.3), which the pedagogy pass replaced with the passages'
   real counts. **Changed** §C to `P27`'s 409 words in 98.16 s → 250, `P28`'s
   402 in 90 s → 268, 4/6 → ≈ 178.7, ≈ −71.3, and the worked line to
   "268 × 4/6 ≈ 178.7 against 250"; recomputed and matching the pins.

## Passage problems (reported; passages not edited)

- **`P31` Q3 is answerable without resolving the garden path.** §C and §R say
  the later cues were removed, but two remain: "he would not be pulling an oar
  for a fortnight at least" (the paragraph before the sentence) and "Klara
  ran the ferry for the rest of the six weeks, with Emil sitting in the
  stern" (the last paragraph), and the right option is "Sitting in the boat
  and waving the red flag". A reader who took "The ferryman rowed across the
  river" as Emil rowing can still answer from either cue, which is exactly
  the repair the stream is supposed to make impossible. Proposed fix: make
  the injury sentence about the wrist only ("…his wrist was swollen and
  purple, and the doctor told him to rest it") and end the last paragraph
  "with Emil in the stern to give advice" → "with Emil giving advice that
  she mostly ignored"; no word count, answer index or question changes
  needed beyond a few words.
- **`P30` Q2** ("Who complained that the soup was cold?") can be reached by
  reasoning (whoever was served before the quarter-hour speech waited
  longest), less strongly than `P31`'s. Acceptable; noted.
- `P27`/`P28` are matched within 7 words and 0.1 grade; `P19`/`P20` within 21
  words and under one grade. No other question found guessable.

## Checked and sound

- Brysbaert 2019 (238, 260, 183; pooled adult English); Hardyck and
  Petrinovich by EMG feedback, difficult text down, easy held; Slowiaczek and
  Clifton's reading-not-listening contrast; the second-task confound stated
  in concepts, body, quiz and note; Potter's ~12 words a second for single
  sentences; Benedetto et al.'s lower literal comprehension and fatigue with
  reduced blinking; Acklin and Papesh's lower comprehension at speed;
  Schotter, Tran and Rayner's trailing mask with the cost on ordinary
  sentences; Carver 1985 (≈ 600; superior readers, not graduates); Just,
  Carpenter and Masson used for design only, as the `note` says; Woody Allen
  once, in the §S form; photoreading named once. No promise anywhere.
- The drills match their text: aloud has no questions and logs `other`; the
  fallback writes 183 in 60 s labelled "Brysbaert 2019" and logs nothing;
  the suppression tick reaches `extra.kept`; every streamed and paced reading
  logs `condition`; RSVP shows one word in the box and ends by itself, both
  ms tiles print; phrases shows a marked phrase ("bought in a pot"); the
  passage is hidden during every question; "Use my baseline median" fills
  every target box the body says it fills; 650 is refused with the sentence
  the lesson paraphrases; Reset at the questions logs nothing, so lesson 6's
  felt-pace instruction works.
- Quiz: one defensible answer in each of 23 items; every distractor argued
  for and rejected.

## Recommendations (not changed)

- **`the-inner-voice` logs an easy-band silent reading as `test`.** `P26` is
  easy (FK ≈ 6.2), and a `test` enters the median of the last three tests
  and the verdict tiles, where an easy story's rate flatters the curve. §C
  assigns `test` and Course 6's easy/hard compare does the same, so this is
  a Subject-level decision rather than a local fix; I recommend `condition`
  for both, or a sentence in the body saying an easy-text test will sit high.
- If Slowiaczek and Clifton's counting was overt, say the drill's
  under-the-breath counting is a milder suppression (finding 2).
- `the-inner-voice` `typical` preset's 476 words is not `P26`'s 453 (the
  pedagogy assessment's point; agreed — a clause saying the box will show 453
  is the lighter fix).
- `one-word-at-a-time` with `vsLog: True` (the pedagogy assessment's
  recommendation; agreed).

## Where I disagree with the pedagogy assessment

- It states that "`P31` has no later cue that gives the answer away". Two
  remain (above); the lesson's central question is answerable without the
  repair it is meant to test.
- It records lesson 1's logging as "exactly as §C assigns them, so the curve
  the Subject promises is not polluted". The silent reading is an easy-band
  passage logged `test`, which is the one entry in this course that does
  enter the curve; it is as §C assigns, but §C is the thing to question.
- It did not flag "count aloud, as in this drill" against a drill that
  counts under the breath, the reading-aloud/speaking conflation, or "well
  under half" (findings 1–3).
- It left the §C correction for lesson 2 to the orchestrator; this review's
  brief allows the course's own §C entries, so it is made here.
- Agreed with its repairs (the real-count `typical` preset, the verdict-tile
  clauses, the whole-page book time) and with its recommendations on
  `vsLog`, the 476-word preset and the `P21`/`Q20` twins.
