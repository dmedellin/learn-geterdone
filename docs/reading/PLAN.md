# Reading Faster — the build specification

This is the curriculum, lab and authoring contract for the twelfth Subject:
how to read faster, what the evidence says is and is not possible, and — above
all — **practice**. The operator asked for it in one sentence: explore the
techniques and add exercises, "in this one I think the most important thing is
exercising". Every lesson is therefore built around a drill the reader does in
the browser, timed and scored there, and logged so that progress across the
Subject can be read off the reader's own numbers.

Everything an author, a kit engineer or a reviewer needs is here. Where it says
"exactly", a test or a gate enforces it. Where it says "never", a published
page somewhere in this library has already been wrong for that reason.

It adopts the conventions of `docs/capital/PLAN.md` and
`docs/philosophy/PLAN.md` §D.0 and §E by reference wherever this one is silent.
Read before this: `AGENTS.md` §0, §1, §1a, §2 and the page-weight note;
`content/AGENTS.md` (all of it); `scripts/mathpath/AGENTS.md` ("a preset's two
claims"); `docs/philosophy/PLAN.md` §D.0 and §E.

**Status: specification.** Built on branch `feat/reading-subject`. The
Phenomenology Subject is being wired concurrently on its own branch and merges
first; this Subject wires as the twelfth, after rebasing on that merge (§H).

Contents

- §0 The one question, answered for this Subject
- §A PATH fields
- §B The eight courses
- §C Every lesson: 42 entries
- §D The lab kit: `readkit` (8 modes)
- §P The passage bank
- §E Package layout and the author's checklist
- §F Voice: a coach who has read the research
- §G What is left out, and why
- §S Sources the lessons may cite
- §H Wiring notes for the orchestrator
- §R Review record

---

## §0 The one question

`docs/FUTURE-SUBJECTS.md` asks of every proposed Subject: **what does the reader
compute?** For reading faster the answer is unusually direct: **the reader
measures themself.** Every drill times a reading in the browser, scores the
comprehension questions that follow it, and computes words per minute, the
share of questions answered correctly, and their product — the *effective
reading rate*. The lab then compares that with the reader's own earlier runs,
with a second condition (a pacer, a flashed word stream, a skim), or with what
a model of the eye says is possible.

So the claim this Subject makes is: **every figure is computed in your browser,
in exact arithmetic, either from what you did in a drill or from the quantities
a lesson states.** Three families, and every view's `panel_intro` names which
one it is in:

1. **Your measurement.** Words read, milliseconds taken, questions right, from
   a drill you just did (or, before you do one, from the preset instance the
   lesson describes). Words per minute, comprehension, effective rate, the
   difference between two conditions, a change across sessions.
2. **A stated model.** The eye-movement budget (fixation time, saccade time,
   characters advanced per fixation, share of regressions → words per minute
   possible); the characters per fixation a claimed speed would require; a
   readability formula; vocabulary coverage; a time budget over a reading list;
   a review schedule. The model is named, its source is cited, and the lab
   computes what it says, not whether it is true.
3. **A count over a text.** Words, sentences, syllables (by a stated rule),
   unknown words, the words a skim shows against the words in the passage.

**What the lab never does:** call one measurement "your reading speed". A
single timed reading of one passage on one day is one measurement, and the
first course teaches exactly how much two of them can differ with nothing
changed. That is the material clause.

**Deliberate deviations from the library's conventions:**

1. **Drills use the clock.** Every other kit computes from inputs; this one also
   *measures*, with `performance.now()`, and fills its own inputs from the
   measurement. The tiles are computed from those inputs exactly as from a
   preset, so `labcheck.js` checks the same arithmetic the drill uses (§D.0).
2. **The lab keeps a log.** A drill's result is appended to one
   `localStorage` key shared by every lesson of the Subject
   (`learn-reading-log`, §D.0), so that later lessons — and the whole of Your
   Training Plan — can read the reader's history. Nothing leaves the browser.
3. **Passages are written for the Subject** (§P). A timed drill needs a fresh
   text each time, of known length and difficulty, with questions that cannot
   be answered without reading it. The passages live in the content package,
   like any other lesson text.
4. **The body may send the reader to the drill first.** In lessons whose point
   is a measurement the reader has not yet made, the first `p` says so and
   names the drill; the explanation follows. This is the library's worked
   example → practice order, run in the order the research on testing
   suggests: try, then learn why (§F).

---

## §A PATH fields (`content/reading/__init__.py`)

```
"slug": "reading-faster",
"title": "Reading Faster",
"level": "Beginner → Intermediate",
"level_note": "any fluent adult reader; the arithmetic is a division",
```

**tagline** (counts re-verified at wiring by
`test_the_tagline_and_description_state_the_real_counts`):

> Read faster in the ways that can be measured, and find out for yourself which ones work for you
> &mdash; timed drills with comprehension checks in every lesson, a log of
> your own numbers, and the research on eye movements, the inner voice,
> skimming and memory. Eight courses and 42 lessons are available.

**description**:

> The Reading Faster Subject: eight courses of practice. Each lesson gives you a
> drill &mdash; a timed reading, a pacer, a flashed word stream, a skim, a
> scan, a recall test &mdash; scores it in your browser, and logs the result,
> so that what you learn about reading speed is measured on your own reading.
> The lessons explain what the eye can and cannot do, what the speed-reading
> courses promise and what the studies found, and how to choose a speed for a
> purpose. All eight courses and 42 lessons are available.

**key** (each line ≤ 46 characters, no second column):

```
rate = words × 60 / seconds
comprehension = correct / questions
effective rate = rate × comprehension
time per word = fixations × (fix + saccade)
coverage = known tokens / all tokens
one reading is one measurement
```

**material** (must differ from every existing clause; proposed
`READ_DISCLAIMER_RE = r"one measurement, not your reading speed"`):

> every figure on this path is computed in your browser from what you did in a
> drill or from the quantities a lesson states, and a rate measured on one
> passage on one day is one measurement, not your reading speed &mdash;
> whether a technique helps you is a question your log can answer and a single
> drill cannot.

**prerequisites** (paragraphs):

1. Fluent reading in English. This is a Subject for an adult who already reads
   well and wants to read more in less time; it does not teach reading. If
   English is not your first language, your rates will be lower than the
   reference figures, and the comparisons that matter are with yourself.
2. A quiet ten to twenty minutes per lesson, then ten to fifteen a day for the
   Daily Drill, and a keyboard or a touchscreen. Every drill is visual and
   timed; a drill run while you are interrupted measures the interruption, and
   a reader using a screen reader can read the lessons but not do the drills.
3. The arithmetic is a division and a product. The labs do it; what is asked of
   you is to read each number for what it is a measurement of.
4. A willingness to be measured honestly. The comprehension questions are
   there so that a fast time with nothing understood shows up as what it is.

**why_order** (paragraphs):

1. Measurement comes first because every later claim — that a pacer helps, that
   a flashed stream is faster, that skimming loses detail — is a comparison of
   two measurements, and a comparison means nothing until you know how much one
   measurement varies on its own.
2. Practice comes second, because the routine should start early and a log
   needs weeks to say anything: the pacer, the hold target and the Daily
   Drill, which the reader then keeps up through the rest of the Subject.
3. The eye comes third, as the limits the practice is read against. Once you
   have computed what a fixation costs and how far a glance reaches, you can
   test any speed claim in a line of arithmetic, and the inner voice and the
   flashed word stream are tested next the same way.
4. Skimming, difficulty and memory come after because they are where the real
   time is saved or lost: by not reading what you do not need, by knowing more
   words and more about the subject, and by remembering what you read the first
   time. The training plan comes last and uses all of it.

**sequence_intro**:

> Each course assumes the ones before it and nothing else. Measure Your Reading
> gives every later drill its scoring; Guided Practice starts the Daily Drill
> the rest of the Subject keeps going; How the Eyes Read gives the limits every
> technique is tested against; The Inner Voice and Flashing Words tries the
> tradition's other techniques against a control; Skimming, Scanning and
> Previewing and Words, Knowledge and Difficulty are where most of the time is
> saved; Remembering What You Read measures what is kept; Your Training Plan
> uses all of it on your own log.

**footer_lead**:

> <strong>Educational course material.</strong> Every figure on this path is
> computed in your browser from what you did in a drill or from what the lesson
> states: a rate is words over minutes, comprehension is questions right over
> questions asked, an eye-movement budget is fixations times their cost.
> Passages are written for this course. Your drill results stay in your
> browser and are never sent anywhere. What the labs cannot do is tell you
> what one reading means on its own &mdash; that takes a log.

---

## §B The eight courses

| # | slug | title | lessons | level |
| --- | --- | --- | --- | --- |
| 1 | `reading-measure-your-reading` | Measure Your Reading | 5 | Beginner |
| 2 | `reading-guided-practice` | Guided Practice | 5 | Beginner |
| 3 | `reading-how-the-eyes-read` | How the Eyes Read | 6 | Intermediate |
| 4 | `reading-inner-voice-and-flashing-words` | The Inner Voice and Flashing Words | 6 | Intermediate |
| 5 | `reading-skim-scan-and-preview` | Skimming, Scanning and Previewing | 7 | Intermediate |
| 6 | `reading-words-knowledge-and-difficulty` | Words, Knowledge and Difficulty | 5 | Intermediate |
| 7 | `reading-remembering-what-you-read` | Remembering What You Read | 4 | Intermediate |
| 8 | `reading-your-training-plan` | Your Training Plan | 4 | Intermediate |

Total 42. Course 5 has more than six lessons and splits into `part_a.py`
(lessons 1–4) and `part_b.py` (5–7); every other course is one `part_a.py`.

Practice starts in Course 2 and does not stop: its third lesson, The Daily
Drill, hands the reader the routine the Subject wants followed from then on
(ten to fifteen minutes a day on the practice pool, §P), and the last `step`
of every later lesson is "then today's Daily Drill". The eye course comes
third, as the limits against which the practice is read, after the reader has
a pacer and a log that is filling.

The `reading-` prefix keeps course slugs from colliding with other Subjects'.
Check ids take the form `read-course8-lesson-<lesson-slug>` (20 characters
before the slug); every lesson slug in §C is at most 40 characters, so every
check id is at most 60, inside the 72-character cap.

**Module names.** Each course has two modules, named in its §C header; every
lesson's `module` is one of them, plain text, at most 40 characters.

**Every lesson has a timed reading** (§0): either its lab is a drill, or its
calculator view carries a `warmup` reading (§D.0). "The drill" in §C means the
lab's interactive run; "the presets" are the deterministic instances
`labcheck.js` checks. A preset is always a plausible reader's result written
out in numbers ("a reader who took 96 seconds over 400 words and answered 5 of
6"), never "you". Every passage has six questions (§P), so one question is
1/6 ≈ 16.7 points of comprehension, and every compare panel says so.

**Drill-first lessons** (marked *drill first* in §C): the body's first `p`
sends the reader to the drill, and the `summary`, `one_line` and `concepts`
state the question and the method, never the expected result.

**Log kinds** (§D.0): every logged reading is `baseline`, `test`, `practice`,
`condition` or `other`. Medians, ranges and verdicts use `baseline` and `test`
only. §C says the kind of each reading.

**The Subject's rule for a real change** (taught in Course 1, used
everywhere): a single reading above the baseline range happens by chance about
one time in four (a fourth reading from the same reader is the highest of four
one time in four); a change is evidence when the **median of the last three
tests** is above the baseline range. The median rule is not proof either: with
nothing changed, three baselines and three tests from one reader put the median
of the tests above the top baseline about one time in five, because that
happens exactly when the two highest of the six readings are both tests, 3 of
the 15 equally likely pairs (3/15 = 1/5). It is a rule of thumb that one lucky
reading cannot meet, not a significance test.

---

## §C Every lesson

Format:

- **slug** — Title — *module* — minutes
- **Drill:** what the reader does, on which passages (§P ids), and each
  reading's log kind.
- **Do:** the observable objective.
- **Standard:** the act that shows it, without the lab, and its pass level.
- **Lab:** mode/view; presets and their instances; pinned tiles.
- **Misconception:** the wrong model `mistakes[0]` names and refutes.
- **Worked:** the single worked example, in one line.
- **Sources:** what the explanation rests on (§S keys).

Preset ids are suggestions; the INSTANCES are not optional. Every figure below
was recomputed by the accuracy review or at reconciliation; an author who
changes an instance recomputes it and records it here in the same commit.
Comprehension is out of six throughout.

Every compare lesson's `note` names the two confounds of a two-reading
comparison — different passages, and which came first (the kit alternates the
order, §D.0) — and its body says once that a reader whose result goes the
other way has not refuted the study, and the study has not refuted them.

### Course 1 — Measure Your Reading (`reading-measure-your-reading`, 5)

Modules: `Rate and comprehension`, `Reading your numbers`.

Gives every later drill its scoring and takes the reader's three baselines:
`P01`, `P02` and `P04`, at natural pace with questions, logged `baseline`;
`P05`, read the same way, is logged `test`, the first reading judged against
them. (The kit builds every range from all the baselines the log holds, so a
fourth baseline widens the range rather than being ignored.) Its `how_to` says: do every drill the first time you open the
lesson, before reading the explanation; never practise on a passage you have
already read; and its `not_covered` says a reader who finds reading effortful
should see a specialist, not a drill.

1. **words-per-minute** — Words per Minute — *Rate and comprehension* — 8 min — *drill first*
   - **Drill:** a timed reading of `P01` (491 words) at natural pace, six questions
     scored (the body does not discuss them until the next lesson);
     `baseline`.
   - **Do:** compute a reading rate from a word count and a time, in words and
     in standard-length words (six character spaces), and place it against
     the published average.
   - **Standard:** given words, characters and seconds, compute both rates
     to the nearest whole number and say which one Carver's figures use.
   - **Lab:** `drill/single`, display `normal`. Presets: `steady` (400 words,
     2,640 characters with spaces, 96 s, 5/6 → 250 wpm, 275 standard wpm),
     `slow` (400 words, 2,640 characters, 160 s, 6/6 → 150 wpm, 165 standard).
     Pins `drWpm`, `drStdWpm`.
   - **Misconception:** "Most adults read about 300 words a minute, so I am
     slow." The best current estimate for silent reading of English
     nonfiction is about 238 wpm (Brysbaert 2019), and the familiar 300 is an
     overestimate. `mistakes[1]`: a rate in words is not comparable across
     texts of different word length, which is why Carver counts six-character
     standard words.
   - **Worked:** 400 × 60 / 96 = 250 wpm; 2,640 / 6 = 440 standard words;
     440 × 60 / 96 = 275.
   - **Sources:** Brysbaert 2019; Carver 1990.

2. **comprehension-and-effective-rate** — Comprehension and the Effective Rate — *Rate and comprehension* — 10 min — *drill first*
   - **Drill:** `drill/compare`: side A `P02` at natural pace (`baseline`);
     side B `P03` "as fast as you can" (`condition`); six questions each.
   - **Do:** compute comprehension and effective rate for two readings and say
     which delivered more understood words per minute.
   - **Standard:** given two readings' words, seconds and scores, compute both
     effective rates and name the larger, without the lab.
   - **Lab:** `drill/compare`, `ratioOf: err`, `order: AB` (the natural-pace
     baseline first, so that it is not taken straight after the fast reading;
     with `alternate` the log's length after lesson 1 made every course-following
     reader read B first). Presets: `pushed-too-far` (A:
     400 words, 100 s, 6/6 → 240 wpm, effective 240; B: 400, 50 s, 2/6 → 480
     wpm, effective 160), `worth-it` (A as before; B 400, 75 s, 5/6 → 320 wpm,
     effective ≈ 266.7). Pins `drWpmA`, `drWpmB`, `drErrA`, `drErrB`,
     `drErrDiff` (−80, ≈ +26.7), `drRatio` (2/3 ≈ 66.7%, 10/9 ≈ 111.1%).
   - **Misconception:** "The faster reading is the better reading." Effective
     rate (Jackson and McClelland's effective reading speed) makes the trade
     visible.
   - **Worked:** 480 × 2/6 = 160 < 240 × 6/6 = 240.
   - **Sources:** Jackson and McClelland 1979; Rayner et al. 2016.

3. **one-reading-is-one-measurement** — One Reading Is One Measurement — *Reading your numbers* — 12 min
   - **Drill:** two more natural-pace readings with questions as the view's
     `warmup` list: `P04` (`baseline`, the third) then `P05` (`test`); then
     `log/noise` reads the baselines and tests from the log ("Use my
     baselines").
   - **Do:** compute the range of the baseline rates and decide whether a
     later reading, and the median of three later tests, is above it.
   - **Standard:** given three baselines and three later tests (the lesson's:
     236, 249, 243; tests 251, 254, 247), compute the range and the tests'
     median and say whether the change is evidence by the Subject's rule.
   - **Lab:** `log/noise` (effective rates). Presets: `tight` (baselines 238,
     251, 245 → 238–251, `lgRange` 13 wpm wide; one test 247 → inside),
     `wide` (212, 268, 240 → 56 wide; test 262 → inside), `one-high` (tight
     baselines; one test 262 → "above the baseline range once — a fourth
     reading does this about one time in four"), `three-high` (tight
     baselines; tests 262, 270, 258 → median 262, "above the baseline range on
     the median of the last three tests"). Pins `lgMean`, `lgRange`,
     `lgTestMedian`, `lgVerdict`.
   - **Misconception:** "My rate on one test is my reading speed." The same
     reader on two passages of one band, minutes apart, can differ by tens of
     words per minute, and one high reading is expected by chance.
   - **Worked:** baselines 212, 268, 240 → range 212–268, 56 wide; a later
     262 is inside it.
   - **Sources:** Carver 1990 (rate varies with passage).

4. **typical-rates-and-reading-gears** — Typical Rates and Reading Gears — *Reading your numbers* — 8 min
   - **Drill:** `warmup` `P09` (`practice`); the reader's baseline median in
     standard-length words is read from the log (or typed) and placed against
     Carver's five gears.
   - **Do:** place a measured rate, in the right unit, against Carver's gears
     and Brysbaert's averages, and name the purpose each gear serves.
   - **Standard:** given a rate in words and the characters read, convert to
     standard-length words and name the nearest gear and its purpose.
   - **Lab:** `log/gears`, inputs `stdwpm` and `wpm`. Gear table (standard
     words per minute, college students): scanning 600, skimming 450,
     rauding 300, learning 200, memorising 138. Presets: `average` (238 wpm,
     261.8 standard → nearest rauding, 300 − 261.8 = 38.2 < 61.8),
     `short-words` (238 wpm, 214.2 standard → learning), `slower` (190 wpm,
     209 standard → learning; 95/119 ≈ 79.8% of 238), `claim` (1,000 wpm,
     1,100 standard → "above every gear"). Pins `lgNearest`, `lgVsAverage`
     (wpm / 238).
   - **Misconception:** "There is one right speed, and faster is always
     better." Carver's gears are five processes with different goals. Carver
     also found that most readers seldom shift gear (his rauding rate is
     relatively constant), and he recommended shifting deliberately — which
     Shifting Gears practises.
   - **Worked:** 238 wpm on text averaging 6.6 characters a word with its
     space: 238 × 6.6 / 6 = 261.8 standard wpm.
   - **Sources:** Brysbaert 2019; Carver 1990, 1992.

5. **keeping-a-practice-log** — Keeping a Practice Log — *Reading your numbers* — 8 min
   - **Drill:** `warmup` `P10` (`practice`), then the reader's own log in
     `log/history`: kinds, the baseline range, export as text.
   - **Do:** read a practice log: which entries count, the baseline range, the
     median of the last three tests, and the verdict.
   - **Standard:** given a log of mixed kinds, pick the entries that count and
     state the verdict by the Subject's rule.
   - **Lab:** `log/history`. Example logs (shown when the reader's log is
     empty, labelled "example"; entries are rate/right/asked, effective rates
     given here): `starting` (3 baselines 238, 251, 245 only → "needs a
     reading after the three baselines"), `six-weeks` (the same baselines,
     median 245, then tests 255, 262, 270, 266 among eight practice entries →
     median of last three 266, above), `speed-only` (tests read at 288, 354,
     488 wpm with 5, 4, 3 right: effective 240, 236, 244 → median 240,
     inside). Pins `lgSessions`, `lgBaseMedian`, `lgRecentMedian`,
     `lgLatestErr`, `lgVerdict`.
   - **Misconception:** "Practice that feels faster is faster." Felt speed and
     measured effective rate diverge; only tests in the log say.
   - **Worked:** last three tests 262, 270, 266 → median 266 > 251.
   - **Sources:** —

### Course 2 — Guided Practice (`reading-guided-practice`, 5)

Modules: `The pacer`, `Pushing the pace`.

The tradition's techniques, done the way the tradition does them, each
measured. Its `how_to` attributes the evidence's conclusion to Rayner et al.
2016 at its own strength (doubling or tripling a rate with comprehension held
is unlikely; practice in reading and language is the way to read faster with
comprehension), and says that the large savings come in Skimming, Scanning and
Previewing and in Words, Knowledge and Difficulty.

1. **reading-with-a-pacer** — Reading with a Pacer — *The pacer* — 10 min — *drill first*
   - **Drill:** `drill/compare`: A `P12` at natural pace (`test`); B `P13`
     with the `pacer` display at the reader's baseline median rate
     (`condition`); order alternates.
   - **Do:** compute a pacer's time per line from a target rate and a line
     length, and compare effective rate with and without it.
   - **Standard:** given a target and words per line, compute ms per line;
     given two readings, say whether the difference exceeds one question.
   - **Lab:** `drill/compare`, B `pacer` at 250 (Use my baseline median
     refills it), `lineWords: 12`. Presets: `steadier` (A 442 words in 110.5 s
     → 240 wpm, 4/6 → 160; B 418 words in 100.32 s → 250 wpm, 5/6 → ≈ 208.3;
     ≈ +48.3), `no-difference` (A 240, 5/6 → 200; B 250, 5/6 → ≈ 208.3;
     ≈ +8.3). Pins `drErrA`, `drErrB`, `drErrDiff`, `drPacerLineMs` (12 ×
     60,000 / 250 = 2,880).
   - **Misconception:** "The pacer makes the eyes work faster than they
     can." It sets a steady pace and discourages drifting and needless
     re-reading; it does not widen what a fixation takes in (How the Eyes Read
     shows why).
   - **Worked:** 12 × 60,000 / 250 = 2,880 ms per line.
   - **Sources:** Rayner et al. 2016 (on the Evelyn Wood courses and the hand
     as pacer).

2. **choosing-a-target-pace** — Choosing a Target Pace — *The pacer* — 14 min
   - **Drill:** `drill/ladder`: three pacer readings at baseline × 1, × 6/5
     and × 3/2 on `P14`, `P15`, `P16` (`practice`), six questions each.
   - **Do:** find the hold target: the fastest pacer setting at which
     comprehension is at least 4/6.
   - **Standard:** given three targets and scores, name the hold target and
     the highest effective rate, and explain why they can differ.
   - **Lab:** `drill/ladder`, `hold: 4/6`. Presets (450-word readings at
     targets 240, 288, 360): `holds-at-288` (scores 6/6, 4/6, 2/6 → hold 288;
     effective 240, 192, 120; top effective 240 at target 240),
     `holds-at-360` (scores 5/6, 5/6, 4/6 → hold 360; effective 200, 240, 240;
     top 240 at target 288, the tie going to the slower). Pins
     `drBestTarget`, `drBestErr`, `drTopErr`.
   - **Misconception:** "Set the pacer as fast as you can follow it." Practise
     at the fastest setting at which you still understand; beyond it, effective
     rate falls.
   - **Worked:** 360 × 2/6 = 120 < 288 × 4/6 = 192; the hold is 288.
   - **Sources:** —

3. **the-daily-drill** — The Daily Drill — *The pacer* — 15 min, then daily
   - **Drill:** `drill/practice` on the practice pool (§P): the next unread
     pool passage with the pacer at the reader's hold target (`practice`), or
     at natural pace with no pacer when the session is a test (`test`); or
     the reader's own pasted text (`practice`, unscored). An attention tick
     after Done: "did your attention leave the text?".
   - **Do:** run a practice session by the routine and record it.
   - **Standard:** state the routine's four rules and apply them to a log
     excerpt (what is the next target; is today a test).
   - **The routine** (the body states it; the numbers are the Subject's):
     ten to fifteen minutes a day; one pool passage with the pacer at the hold
     target; every fifth session a test at natural pace; raise the target by
     about 5% after three holds in a row (4/6 or better), lower it by the same
     after two misses; at most two timed readings in a sitting; if attention
     left the text, shorten the session rather than slow the pacer. When the
     pool reaches hard texts, find the hold again: it will be lower.
   - **Lab:** `drill/practice`, pool `Q01`–`Q15` and `Q26`–`Q28` (18 passages,
     66.2 KB gzipped against the 67 KB ceiling; at 21 the page was 69.9 KB).
     `Q16` is the warm-up of Reading Your Curve and `Q19`–`Q24`, `Q29` and
     `Q30` are warm-ups elsewhere; `Q17`, `Q18` and `Q25` are unplaced.
     Presets (log excerpts, 432 words in 90 s): `three-holds` (pacer 288: 5/6,
     4/6, 5/6, three sessions since the last test → next target 302.4, test
     after 1 more session), `two-misses` (288: 3/6, 3/6, two since → 273.6),
     `test-due` (288: 4/6, 3/6, 5/6, 4/6, four since → "due now: make the
     next reading a test"). Pins `drHold`, `drNextTarget`, `drTestDue`.
   - **Misconception:** "Read as much as possible, as fast as possible." Short, regular sessions at a pace you still
     understand, with regular tests, are the routine; a session's length is
     limited by attention, not ambition.
   - **Worked:** 288 × 21/20 = 302.4.
   - **Sources:** Ericsson, Krampe and Tesch-Römer 1993 (deliberate practice,
     with its contested size); Rayner et al. 2016.

4. **sprints-above-comfort** — Sprints Above Comfort — *Pushing the pace* — 8 min
   - **Drill:** A: a one-minute sprint at twice the baseline rate on `P17`
     with the pacer (`fromBase: 2`), no questions (`condition`); B: a
     natural-pace reading with questions on `P18` (`test`). Order fixed (A
     first): the sprint is the treatment.
   - **Do:** compute the rate of a reading after a sprint and judge it by the
     Subject's rule.
   - **Standard:** given a baseline range and a post-sprint reading, give the
     verdict and what further readings would be needed.
   - **Lab:** `drill/compare`, `order: AB`, `ratio: false`. Presets:
     `after-sprint` (A 484 words in 60.5 s at target 480; B 469 words in 105 s
     → 268 wpm, 5/6 → effective ≈ 223.3; baseline range 238–251 in rate →
     "above the baseline range once"), `no-effect` (B 494 words in 120 s →
     247, 5/6 → ≈ 205.8 → inside). Pins `drWpmB`, `drErrB`, `drVerdictB`.
   - **Misconception:** "After a sprint you read faster for good." Any
     after-effect is one reading; only the median of later tests says whether
     the base rate moved.
   - **Worked:** 268 − 251 = 17 above the top of the range — once.
   - **Sources:** —

5. **repeated-reading-and-transfer** — Repeated Reading and Transfer — *Pushing the pace* — 14 min
   - **Drill:** `drill/repeat`: `P23` three times (`condition`), then the new
     passage `P24` once (`test`), questions on runs 3 and 4.
   - **Do:** compute the gain on a repeated passage and on a new one, and say
     which is evidence of a faster reader.
   - **Standard:** given four rates, compute both gains and name the one that
     measures the reader.
   - **Lab:** `drill/repeat`. Presets: `practice-effect` (runs 1–3, 442 words
     in 110.5, 88.4, 78 s: 240, 300, 340; run 4, 465 words in 112.5 s: 248),
     `transfer` (run 4, 451 words in 98.4 s: 275, +35). Pins `drWpm4`,
     `drRepeatGain`, `drTransferGain`.
   - **Misconception:** "The third reading shows my new speed." It shows you
     know the passage. Repeated reading is a fluency method from work with
     school-age readers, where it also improved new passages, less than the
     practised one (Therrien 2004); for a skilled adult, this drill's
     new-passage run is the test.
   - **Worked:** 340 − 240 = 100 on the repeated passage; 248 − 240 = 8 on the
     new one.
   - **Sources:** Samuels 1979; Therrien 2004.

### Course 3 — How the Eyes Read (`reading-how-the-eyes-read`, 6)

Modules: `Fixations and saccades`, `The limits`.

1. **fixations-and-saccades** — Fixations and Saccades — *Fixations and saccades* — 10 min
   - **Drill:** `warmup` `P06` (`practice`); a `step` asks the reader to watch
     a partner's eyes while they read a line, or their own in a mirror — the
     oldest demonstration there is; then `eye/budget`.
   - **Do:** compute the time per word, and the rate, from fixation duration,
     saccade duration, characters advanced per fixation and regression share.
   - **Standard:** given the five inputs, compute fixations per word and
     words per minute by hand.
   - **Lab:** `eye/budget`. Presets: `typical` (225, 30, 8, 3/20, 6 → 15/17
     fixations per word, 225 ms per word, ≈ 266.7 wpm), `no-regressions`
     (225, 30, 8, 0, 6 → 3/4, 191.25 ms, ≈ 313.7 wpm), `long-fixations`
     (300, 30, 8, 3/20, 6 → 15/17, ≈ 291.2 ms, ≈ 206.1 wpm). Pins `eyWpm`,
     `eyFixPerWord`. The panel says the model treats a regression as a
     fixation that does not advance, which understates its cost (the eyes
     must also come back), and that a return sweep costs about one more
     fixation per line (a `ul` in the body; no lab).
   - **Misconception:** "The eyes glide smoothly along the line." They jump
     and stop, and vision is suppressed during the jumps, so nearly all the
     reading happens in the stops. The jumps were described in Javal's
     laboratory around 1879 (by Lamare; Hering independently), and Javal's
     word "saccade" stuck.
   - **Worked:** 6 / (8 × 17/20) = 15/17 fixations; 15/17 × 255 = 225 ms;
     60,000 / 225 ≈ 266.7 wpm.
   - **Sources:** Wade and Tatler 2009; Huey 1908; Rayner 1998, 2009.

2. **the-perceptual-span** — The Perceptual Span — *Fixations and saccades* — 10 min
   - **Drill:** `flash/span`, partial report: a 15-letter random string
     flashed around a fixation mark for 150 ms (shorter than the 175–200 ms
     it takes to start a saccade), then a mask, then three positions cued
     (`cues: 3`); the reader picks those letters from buttons. Twenty trials
     (`n: 20`). Logged `other`.
   - **Do:** compute letter-identification accuracy by distance from fixation
     and say how this differs from the perceptual span in reading.
   - **Standard:** given accuracy by position, name the farthest position each
     side with accuracy ≥ 1/2, and say why the reading span is asymmetric
     while this one is not.
   - **Lab:** `flash/span`, `len: 15` (positions −7…+7). Presets, each ten
     trials written out in full (`targets`, `typed`): `typical` (accuracy
     10/10 at 0, 9/10 at ±1, 8/10 at ±2, 6/10 at ±3, 4/10 at ±4, 2/10 at ±5
     and beyond, symmetric → span "left 3, right 3", edge 1/5), `strong`
     (6/10 at ±4 → "left 4, right 4"). Pins `flCentre`, `flEdge`, `flSpan`.
   - **Misconception:** "With training you can take in a whole line, or a page,
     in one glance." In reading, the perceptual span is about 3–4 letters left
     and 14–15 right, and words are identified only within about 7–8 letters
     to the right; the asymmetry follows attention in the direction of
     reading (it reverses for readers of Hebrew). The span is smaller on hard
     text and somewhat larger in skilled readers, but there is no evidence
     that training widens it to a line. The drill measures a related but
     different span — letters with no context, which is roughly symmetric —
     and the lesson says so.
   - **Worked:** 6/10 at +3 and 4/10 at +4: the identification of random
     letters ends between them.
   - **Sources:** McConkie and Rayner 1975; Rayner 1998; Pollatsek et al. 1981;
     Rayner, Slattery and Bélanger 2010.

3. **looking-back** — Looking Back — *Fixations and saccades* — 12 min
   - **Drill:** `drill/compare` at the reader's hold target (both target
     boxes; 300 until the reader sets them): A `P07` with the `pacer`
     (`condition`); B `P08` with the `mask` display — lines above the
     highlight hidden as it passes (`condition`).
   - **Do:** compute what removing the text behind the eyes does to
     comprehension at a fixed rate, and say what regressions are for.
   - **Standard:** given two scores at one rate, compute both effective rates
     and say whether the difference exceeds one question.
   - **Lab:** `drill/compare`. Presets: `masked-costs` (A 447 words in 89.4 s
     → 300 wpm, 6/6 → 300; B 436 words in 87.2 s → 300 wpm, 4/6 → 200;
     −100), `no-cost` (A and B 5/6 → 250). Pins `drErrA`, `drErrB`,
     `drErrDiff`.
   - **Misconception:** "Regressions are a bad habit to eliminate." They are
     about 10–15% of saccades in skilled readers. When Schotter, Tran and
     Rayner made going back useless — each word turned to x's as the eyes left
     it — comprehension fell, for ordinary sentences as well as ambiguous
     ones; in normal reading, regressions happen when they are needed. The
     kit's mask hides whole lines, a coarser version of their method.
   - **Worked:** 300 × 4/6 = 200 against 300 × 6/6 = 300.
   - **Sources:** Rayner 1998; Schotter, Tran and Rayner 2014.

4. **fewer-needless-regressions** — Fewer Needless Regressions — *Fixations and saccades* — 12 min
   - **Drill:** `drill/compare`: A `P21` at natural pace without a pacer
     (`test`); B `P22` with the pacer at the hold target (`condition`); after
     each, a count box, "Times my attention left the text" (`lapses: true`,
     logged as `extra.lapses`).
   - **Do:** separate re-reading from lapses of attention from regressions that
     repair understanding, and compare a paced and an unpaced reading on
     effective rate and on self-reported lapses.
   - **Standard:** given two readings and their lapse counts, compute both
     effective rates and say which kind of regression a pacer can reduce.
   - **Lab:** `drill/compare`, `lapses: true`. Presets: `pacer-steadies` (A
     484 words in 121 s → 240 wpm, 5/6, 4 lapses → 200; B 457 words in
     103.864 s at target 264 → ≈ 264.0 wpm, 5/6, 1 lapse → ≈ 220.0),
     `no-change` (A 484 words in 116.16 s, B 457 in 109.68 s, both 250 wpm,
     5/6, 2 lapses → ≈ 208.3 each). Pins `drErrA`, `drErrB`, `drErrDiff`,
     `drWpmB`, `drLapsesA`, `drLapsesB`. The body works the eye-budget arithmetic of a
     smaller regression share as its example (illustrative shares, labelled
     so); the lapse count is a self-report, not a measure of regressions.
   - **Misconception:** "Every look back is wasted time." The ones worth
     cutting come from drifting attention; the repair regressions carry
     comprehension (Looking Back). The split is a teaching device, not a
     distinction the studies measured.
   - **Worked:** eye budget at 225/30/8/6 with regression share 3/20 → ≈ 266.7
     wpm; with 7/100 → 3/4 × 100/93 = 25/31 fixations per word, ≈ 205.6 ms,
     ≈ 291.8 wpm.
   - **Sources:** Schotter, Tran and Rayner 2014; Rayner et al. 2016.

5. **the-speed-ceiling** — The Speed Ceiling — *The limits* — 8 min
   - **Drill:** `warmup` `Q19` (`practice`); then `eye/required` on a claimed
     speed, with `fix` adjustable.
   - **Do:** compute the characters a fixation must advance for a claimed rate
     and classify the claim against the spans, at stated settings.
   - **Standard:** given a claimed rate and the settings, compute characters
     per fixation and state the verdict with its settings.
   - **Lab:** `eye/required` (reg 0 in every preset). Presets: `double` (500
     wpm, 225 + 30 ms, 6 → 12.75: "at these settings, beyond the
     word-identification span but within the perceptual span"), `thousand`
     (1,000 → 25.5: "at these settings, beyond the perceptual span"),
     `twenty-five-thousand` (25,000 → 637.5, the same). Pins `eyNeeded`,
     `eyVerdict`.
   - **Misconception:** "Reading at 1,000 words a minute with full
     comprehension is a matter of technique." At an average fixation it needs
     25 characters identified per glance. Skilled readers who reach 350–400
     wpm do it with shorter fixations and by skipping short words, which the
     settings let you try; what is done at 1,000 is skimming, which the
     Subject teaches as skimming. Carver (1985) found no tested reader
     comprehending above about 600 wpm.
   - **Worked:** 1,000 × 6 × 255 / 60,000 = 25.5 characters per fixation.
   - **Sources:** Rayner 1998; Rayner et al. 2016; Carver 1985.

6. **training-the-periphery** — Training the Periphery — *The limits* — 10 min
   - **Drill:** `flash/schulte`: three 5×5 tables, eyes on the centre, numbers
     found in order (`other`, logged with the table time); then `warmup`
     `P11` (`test`). `log/history` has no Schulte series, so the reader
     writes each table time in a log note beside the test's effective rate
     and compares the two over weeks.
   - **Do:** compute a table time per cell and state what a faster table would
     and would not show about reading.
   - **Standard:** given table times and test rates over sessions, say whether
     they support transfer, and what else could explain both.
   - **Lab:** `flash/schulte`. Presets: `first` (25 cells in 62 s, seed 12345
     → 2.48 s per cell), `third` (25 in 41 s, seed 2718 → 1.64); no errors.
     Pins `flTime`, `flPerCell`.
   - **Misconception:** "Getting faster at eye exercises makes reading faster."
     Practice improves the practised task; transfer to reading is the claim to
     test, and the evidence for it is weak (Rayner et al. 2016).
   - **Worked:** 41 / 25 = 1.64 s per cell, against 62 / 25 = 2.48.
   - **Sources:** Rayner et al. 2016.

### Course 4 — The Inner Voice and Flashing Words (`reading-inner-voice-and-flashing-words`, 6)

Modules: `The inner voice`, `Flashing words`.

1. **the-inner-voice** — The Inner Voice — *The inner voice* — 10 min
   - **Drill:** `drill/compare`: A `P25` read aloud — a whisper is enough —
     no questions (`other`); B `P26` silently with questions (`test`). A
     reader who cannot read aloud where they are uses the fallback: Brysbaert's
     oral average, 183, labelled a published figure.
   - **Do:** compute oral and silent rates and their ratio, and explain how
     silent reading can exceed speaking rate with an inner voice.
   - **Standard:** given both rates, compute the ratio and state what it
     implies for the advice to eliminate the inner voice.
   - **Lab:** `drill/compare`, A `aloud`, `ratioOf: wpm`. Presets: `typical`
     (A the fallback's 183 words in 60 s; B 476 words in 120 s → 238 →
     238/183 ≈ 130.1%), `fast-silent` (A 477 words in 159 s → 180; B 453
     words in 84.9375 s → 320 → 16/9 ≈ 177.8%). The ratio prints as a
     percentage. Pins `drWpmA`, `drWpmB`, `drRatio`.
   - **Misconception:** "The inner voice limits you to speaking speed, so it
     must go." Silent reading is already faster than oral reading on average;
     inner speech is not full articulation.
   - **Worked:** 238 / 183 ≈ 1.3 (≈ 130.1%).
   - **Sources:** Brysbaert 2019; Rayner et al. 2016.

2. **silencing-the-inner-voice** — Silencing the Inner Voice — *The inner voice* — 12 min
   - **Drill:** `drill/compare`, matched pair: A `P27` normally; B `P28` while
     counting "one-two-three" under the breath (articulatory suppression, as
     Slowiaczek and Clifton did; mouthing is enough), both `condition`, with
     questions; after B, the tick "I kept counting the whole way".
   - **Do:** compute the change in rate and comprehension under suppression and
     say what it implies.
   - **Standard:** given both readings, compute both effective rates and the
     difference, and say why a reading where the counting lapsed does not
     count.
   - **Lab:** `drill/compare`, B `suppress: true`. Presets: `typical` (A `P27`'s
     409 words in 98.16 s → 250, 6/6 → 250; B `P28`'s 402 words in 90 s →
     268, 4/6 → ≈ 178.7; ≈ −71.3), `easy-text` (A 403 in 93 s → 260, 6/6; B 399 in 90 s
     → 266, 5/6 → ≈ 221.7; ≈ −38.3). Pins `drErrA`, `drErrB`, `drErrDiff`.
   - **Misconception:** "Eliminating subvocalisation is the key to speed
     reading." In studies that suppressed inner speech, comprehension of
     difficult text fell while easy text held up (Hardyck and Petrinovich, by
     muscle feedback); counting while reading impaired passage comprehension
     (Slowiaczek and Clifton). The studies are few and small, and suppression
     also adds a second task.
   - **Worked:** 268 × 4/6 ≈ 178.7 against 250.
   - **Sources:** Hardyck and Petrinovich 1970; Slowiaczek and Clifton 1980;
     Rayner et al. 2016.

3. **one-word-at-a-time** — One Word at a Time — *Flashing words* — 8 min — *drill first*
   - **Drill:** `drill/single` with the `rsvp` display: `P29`, one word at a
     time at the reader's baseline median rate (`condition`), then questions.
   - **Do:** compute the time each word is shown at a rate and compare
     comprehension with the reader's baselines.
   - **Standard:** given a rate, compute ms per word; explain why removing
     eye movements saves so little time.
   - **Lab:** `drill/single`, `rsvp`. Presets (`P29`'s 403 words):
     `at-baseline` (96.72 s → 250 wpm, 240 ms per word, 5/6 → ≈ 208.3),
     `at-500` (48.36 s, 120 ms, 3/6 → 250), `at-600` (40.3 s, 100 ms, the cap
     for a drill, §D.0; 2/6 → 200). Pins `drWordMs`, `drWpm`, `drErr`.
   - **Misconception:** "Removing eye movements removes their time, so a
     flashed stream is free speed." Saccades are about a tenth of reading time
     (30 of 255 ms in the model). Single sentences can be understood in RSVP at
     about twelve words a second (Potter 1984); the costs come with passages,
     with memory and with no way back — lower literal comprehension and more
     visual fatigue for Spritz (Benedetto et al. 2015), lower comprehension at
     speed for the apps (Acklin and Papesh 2017).
   - **Worked:** 60,000 / 250 = 240 ms per word; 30 / 255 ≈ 11.8% of the
     model's time is saccades.
   - **Sources:** Potter 1984; Benedetto et al. 2015; Acklin and Papesh 2017.

4. **reading-in-phrases** — Reading in Phrases — *Flashing words* — 10 min
   - **Drill:** `drill/compare` at the reader's baseline rate: A `P19` in
     word-by-word RSVP; B `P20` in phrase RSVP (one meaningful phrase at a
     time), both `condition`. Both remove regressions, so the comparison
     isolates the grouping.
   - **Do:** compute the phrase display's time per phrase and compare
     comprehension of grouped and ungrouped streams at one rate.
   - **Standard:** compute ms per phrase from its words and the rate; say what
     the comparison does and does not isolate.
   - **Lab:** `drill/compare`, A `rsvp`, B `phrases`, both at 250. Presets:
     `grouping-helps` (A 459 words in 110.16 s → 250 wpm, 3/6 → 125; B 438
     words in 105.12 s → 250, 5/6 → ≈ 208.3), `no-difference` (both 4/6 →
     ≈ 166.7). Pins `drErrA`, `drErrB`, `drErrDiff`, `drPhraseMs` (mean ms per
     phrase for `P20`'s 127 phrases: 438 × 60,000 / (250 × 127) ≈ 827.7).
   - **Misconception:** "Phrase reading means seeing several words in one
     fixation." Chunking groups words by meaning; in normal reading the eyes
     still fixate most content words. What may help is the grouping.
   - **Worked:** a 4-word phrase at 250 wpm: 4 × 60,000 / 250 = 960 ms; the
     mean phrase of `P20` ≈ 827.7 ms.
   - **Sources:** Rayner et al. 2016.

5. **rsvp-without-looking-back** — Flashing Words Without Looking Back — *Flashing words* — 12 min
   - **Drill:** `drill/compare` at one rate: A `P30` with the pacer; B `P31` in
     RSVP; both `condition`. Each carries one garden-path sentence and one
     question on it.
   - **Do:** compute comprehension in both displays at one rate and connect the
     garden-path question's result to regressions.
   - **Standard:** say what the garden-path question tests and why the stream
     cannot let you repair it.
   - **Lab:** `drill/compare`, both at 300. Presets: `stream-costs` (A 391
     words in 78.2 s → 300, 6/6 → 300; B 403 words in 80.6 s → 300, 4/6 →
     200; −100), `even` (both 5/6 → 250). Pins `drErrA`, `drErrB`,
     `drErrDiff`. `P31`'s garden path ("The ferryman rowed across the river
     waved a red flag …") carries its question (Q3) with no later cue that
     gives the answer away.
   - **Misconception:** "RSVP is reading with the waste removed." The stream
     removes regressions too, and Schotter, Tran and Rayner found going back
     mattered for ordinary sentences, not only ambiguous ones; the garden path
     is just where you can feel it.
   - **Worked:** 300 × 4/6 = 200 against 300.
   - **Sources:** Schotter, Tran and Rayner 2014; Acklin and Papesh 2017.

6. **testing-a-speed-claim** — Testing a Speed Claim — *Flashing words* — 10 min
   - **Drill:** `warmup` `Q20` (`practice`); then `eye/required` with the
     claim panel. The kit cannot put a stream beside `eye/required`, so the
     felt reading of a claimed pace is in the body: go back to One Word at a
     Time, set 600 (the cap; beyond it the display is a flicker, and that is
     itself the finding), and press Reset at the questions.
   - **Do:** test a claim with three computations — characters per fixation,
     effective rate at a plausible comprehension, and the time a book would
     take — and state what evidence would settle it.
   - **Standard:** given a claim, do the three computations and name the test
     that would settle it (a fresh passage, questions written by someone else,
     a control reader).
   - **Lab:** `eye/required`, claim view, comprehension 1/2 in every preset.
     Presets: `triple-speed` (750 words in 60 s → 750 wpm → 19.125, printed
     ≈ 19.1; effective 375), `a-novel-an-hour` (90,000 words in 3,600 s →
     1,500 wpm → 38.25; 750), `whole-page` (350 words in a 2-second glance →
     10,500 wpm → 267.75; 5,250); every verdict "at these settings, beyond the
     perceptual span". Pins `eyClaimWpm`, `eyNeeded`, `eyVerdict`,
     `eyClaimErr`.
   - **Misconception:** "A claim with a testimonial is a measured claim." The
     Just, Carpenter and Masson comparison of trained speed readers, normal
     readers and skimmers is the model of a test; Carver (1985) is the other.
     Photoreading and "mental photography" are named once as claims that
     make no testable prediction beyond ordinary comprehension questions.
     Woody Allen's line ("I took a speed-reading course and read *War and
     Peace* in twenty minutes. It involves Russia.") at most once.
   - **Worked:** 90,000 / 60 = 1,500 wpm → 1,500 × 6 × 255 / 60,000 = 38.25.
   - **Sources:** Just, Carpenter and Masson 1982 (figures checked against
     Rayner et al. 2016 before use); Carver 1985; Rayner et al. 2016.

### Course 5 — Skimming, Scanning and Previewing (`reading-skim-scan-and-preview`, 7)

Modules: `Scanning and skimming`, `Reading strategically`.

1. **scanning-for-a-target** — Scanning for a Target — *Scanning and skimming* — 8 min
   - **Drill:** `scan/find` on `S01` (613 words; then `S02`, 590, on a second visit, first
     unread served): five targets, the reader selects the answering word by
     click or keyboard; timed per target (`test`, so that The Full Battery's
     profile reads the first and latest scan; a scan is not a reading and never
     enters the rate curve). On a phone the scroll is
     inside the timing, and the panel says so.
   - **Do:** compute seconds per target and words passed over per second, and
     say why scanning is not reading.
   - **Standard:** given targets found and the time, compute both figures.
   - **Lab:** `scan/find`. Presets (`S01`'s 613 words): `quick` (5 found, 40 s
     → 8 s per target, ≈ 15.3 words a second), `slow` (4 found, 1 wrong, 95 s
     → 23.75 s, ≈ 6.5). Pins `scFound`, `scPerTarget`, `scWordsPerSec`,
     `scWrong`.
   - **Misconception:** "Scanning is fast reading." It is a search for a known
     form — a number, a name — and not reading for meaning; Carver counts it a
     gear of its own, whose goal is finding. Its speed says nothing about
     reading rate.
   - **Worked:** 613 / 40 ≈ 15.3 words per second; 613 × 60 / 40 = 919.5 a
     minute passed over.
   - **Sources:** Carver 1990.

2. **skimming-for-gist** — Skimming for Gist — *Scanning and skimming* — 8 min — *drill first*
   - **Drill:** `drill/single` with the `gist` display on `P32` (594 words):
     headings and first sentences only (141 words), for 40 s (`limit: 40`),
     under a third of a full reading at 240 (148.5 s); then four gist
     questions (`test`, for the profile's skim row; a gist display never
     enters the rate curve).
   - **Do:** compute the share of the text a skim shows and gist questions
     right per minute.
   - **Standard:** given words shown, words in all and the time, compute the
     share and the gist rate; say when first sentences fail.
   - **Lab:** `drill/single`, `gist`. Presets: `first-sentences` (141 of 594
     words shown → 47/198 ≈ 23.7%; 3/4 gist in 40 s → 4.5 gist answers a
     minute), `slower-skim` (4/4 in 80 s → 3). Pins `drShown`, `drComp`,
     `drGistPerMin`. No effective rate is printed for a skim.
   - **Misconception:** "First sentences always carry the point." Often in
     exposition written to a plan; the passage shows a paragraph where they do
     not. A skim is a bet on the text's structure.
   - **Worked:** 141 / 594 = 47/198 ≈ 23.7%; 3 × 60 / 40 = 4.5.
   - **Sources:** Masson 1982; Duggan and Payne 2009.

3. **what-skimming-costs** — What Skimming Costs — *Scanning and skimming* — 12 min
   - **Drill:** `drill/compare`: A `P33` (410 words) skimmed, the passage
     disappearing at 40 s (normal display, `limit: 40`; `condition`); B `P34`
     (387 words) read in full (`test`); each with six questions, three gist and
     three detail.
   - **Do:** compute gist and detail comprehension separately and choose
     between a skim and a reading for a stated purpose.
   - **Standard:** given both scores by kind and a purpose, choose and justify.
   - **Lab:** `drill/compare`, `kinds: true`. Presets: `typical` (skim 40 s →
     615 wpm, 2/3 gist, 1/3 detail → effective 307.5; read 90 s → 258 wpm,
     3/3, 3/3), `good-skimmer` (skim 3/3, 2/3 → 512.5). Pins `drGistA`,
     `drDetailA`, `drGistB`, `drDetailB`, `drWpmA`, `drWpmB`, `drErrA`,
     `drErrB`; the body says why the effective rate is the wrong basis for
     the choice.
   - **Misconception:** "A skim is a fast read with a little less
     understanding." Gist suffers less than detail (Masson 1982); skimmers who
     choose where to look, given time for half a text, remember more of its
     important ideas than readers who read half of it, but no more of its
     details (Duggan and Payne 2009; they had no untimed full-reading
     condition).
   - **Worked:** detail 1/3 against 3/3; gist 2/3 against 3/3.
   - **Sources:** Masson 1982; Duggan and Payne 2009.

4. **previewing-before-reading** — Previewing Before Reading — *Scanning and skimming* — 12 min
   - **Drill:** `drill/compare`: A `P35` read cold (`test`); B `P36` previewed
     for 30 seconds (headings, first and last paragraph) then read, total time
     counted (`condition`).
   - **Do:** compute the effective rate including the preview and decide
     whether it paid for itself.
   - **Standard:** given times and scores, compute both effective rates with
     the preview counted.
   - **Lab:** `drill/compare`, B `preview`, `limit: 30`. Presets: `pays` (A
     `P35`'s 451 words in 110 s → 246 wpm, 4/6 → 164; B `P36`'s 433 words in
     150 s with the preview counted → 173.2, 6/6 → 173.2; +9.2), `does-not`
     (A 5/6 → 205; B 5/6 → ≈ 144.3; ≈ −60.7). Pins `drWpmA`, `drWpmB`,
     `drErrA`, `drErrB`, `drErrDiff`.
   - **Misconception:** "A preview is free." It costs time; it pays when it
     raises comprehension or lets you skip a section.
   - **Worked:** 433 × 60 / 150 = 173.2 wpm, × 6/6, against 246 × 4/6 = 164.
   - **Sources:** Robinson 1946; Adler and Van Doren 1972.

5. **inspectional-reading** — Inspectional Reading — *Reading strategically* — 10 min
   - **Drill:** `scan/inspect` on `B01` (586 words of front and back matter
     of an imaginary book), `limit: 300`, five structural targets from
     `B01`'s own `targets`, each answered by clicking the word that answers
     it (`other`).
   - **Do:** answer, from a timed inspection, what a book is about, how it is
     organised and where a topic is treated.
   - **Standard:** given a book's contents and index, answer five structural
     questions within the limit.
   - **Lab:** `scan/inspect`. Presets: `five-minutes` (4 of 5 in 300 s → 75 s
     per target found), `thorough` (5 of 5 in 210 s → 42 s). Pins `scFound`,
     `scPerTarget`.
   - **Misconception:** "Reading a book means starting at page one." Adler and
     Van Doren's inspectional reading comes first, and decides whether the
     book needs a whole reading.
   - **Worked:** 300 / 4 = 75 s per target found.
   - **Sources:** Adler and Van Doren 1972.

6. **triaging-a-reading-list** — Triaging a Reading List — *Reading strategically* — 10 min
   - **Drill:** `warmup` `Q21` (`practice`); then `triage/plan` on a stack of
     eight documents with word counts and values for a stated purpose.
   - **Do:** plan a session under a time budget and compute its time and the
     share of the value covered.
   - **Standard:** given the stack, a budget and rates, produce a plan that
     fits and covers more value than reading in order.
   - **Lab:** `triage/plan` (read 250 wpm; skim 750 wpm covering 1/2 of a
     document's value; budget 45 minutes; eight documents totalling 15,000
     words and 36 value points). The rows (words, value): neighbourhood
     newsletter 1,800, 1; minutes of last month's meeting 1,500, 3;
     landlord's lease proposal 3,000, 10; parking study 2,100, 3; staff survey
     results 2,400, 6; history of the building 2,100, 1; facilities
     manager's summary 1,200, 8; removal firm's quote 900, 4. Presets:
     `read-everything` (60 min, 1 = 100%, over by 15), `skim-the-rest` (read
     the lease, survey, summary and quote, skim the rest: 30 + 10 = 40 min,
     8/9 ≈ 88.9%, 5 to spare), `skip-wrong` (read in the order they came until
     time runs out, skipping the last three, the summary among them: 43.2 min,
     23/36 ≈ 63.9%, 1.8 to spare). Pins `trMinutes`, `trCovered`, `trFits`.
   - **Misconception:** "The fastest way through a pile is to read faster."
     Choosing what not to read saves more time than any rate gain.
   - **Worked:** 15,000 / 250 = 60 minutes, over a 45-minute budget.
   - **Sources:** Duggan and Payne 2009.

7. **shifting-gears** — Shifting Gears — *Reading strategically* — 12 min
   - **Drill:** `drill/sections` on `P37` (578 words: an easy narrative
     section of 292, then a dense report of 286), the instruction to change
     speed by section; time per section; six questions on the whole (`test`;
     the kit has no per-section score); the attention tick.
   - **Do:** compute the rate for each section and say whether the reader
     shifted gear to match difficulty and purpose.
   - **Standard:** given section times and scores, compute both rates and say
     whether the shift was a choice or a collapse.
   - **Lab:** `drill/sections`. Presets: `flexible` (292 in 60 s = 292; 286 in
     104 s = 165; 5/6 → whole ≈ 211.5, effective ≈ 176.2), `rigid` (292 in
     73 s = 240; 286 in 72 s ≈ 238.3; 4/6 → ≈ 159.4). Pins `drRateS1`,
     `drRateS2`, `drWpm`, `drErr`.
   - **Misconception:** "A good reader holds one fast speed." Carver found
     most readers hold a nearly constant rate across ordinary texts and seldom
     shift gear; he recommended shifting deliberately, slowing for what must
     be learned and speeding up for what need only be skimmed.
   - **Worked:** 292 × 60 / 60 = 292; 286 × 60 / 104 = 165.
   - **Sources:** Carver 1990, 1992.

### Course 6 — Words, Knowledge and Difficulty (`reading-words-knowledge-and-difficulty`, 5)

Modules: `Difficulty`, `Knowledge`.

1. **your-rate-on-hard-text** — Your Rate on Hard Text — *Difficulty* — 12 min — *drill first*
   - **Drill:** `drill/compare`: A `P38` (easy) and B `P39` (hard), each at
     natural pace with questions (`test`).
   - **Do:** compute the change in rate and effective rate between an easy and a
     hard text and decide which a speed claim should be measured on.
   - **Standard:** given both readings, compute both ratios and say what a
     claim measured on easy text tells you about a hard one.
   - **Lab:** `drill/compare`, `ratioOf: wpm`. Presets: `big-drop` (easy 395
     words in 79 s → 300, 6/6; hard 391 words in 138 s → 170, 5/6 → ≈ 141.7;
     rate ratio 17/30 ≈ 56.7%), `held-rate` (easy 250 in 94.8 s, 6/6; hard
     240 in 97.75 s, 3/6 → 120; ratio 24/25 = 96% — rate held, comprehension
     fell). Pins `drWpmA`, `drWpmB`, `drRatio`, `drErrB`.
   - **Misconception:** "My reading speed is one number." Carver found readers
     keep a nearly constant rate across texts within their level and lose
     comprehension instead; on text well above it they drop into a slower
     gear, and the eye data show longer fixations and more regressions. Either
     way a rate means a rate on a kind of text.
   - **Worked:** 170 / 300 = 17/30 ≈ 56.7%.
   - **Sources:** Carver 1990; Rayner 1998.

2. **measuring-difficulty** — Measuring Difficulty — *Difficulty* — 8 min
   - **Drill:** `warmup` `Q22` (`practice`); then `text/readability` on `P38`
     and `P39` (just read) and `P01` (standard, read in Course 1), counted by
     the kit.
   - **Do:** compute Flesch Reading Ease and Flesch–Kincaid grade from counts
     of words, sentences and syllables, and say what the formulas cannot see.
   - **Standard:** given counts, compute both scores by hand to one decimal.
   - **Lab:** `text/readability`. Presets: `octopus` (`P38`: 395 words, 21
     sentences → FRE ≈ 79.8, grade ≈ 6.8), `church-clock` (`P01`: 491, 21 →
     ≈ 70.2, ≈ 9.3), `continents` (`P39`: 391, 16 → ≈ 14.3, ≈ 17.3), `by-hand`
     (100, 5, 140 → ≈ 68.1, 8.73). Pins `txWords`, `txSentences`, `txFre`,
     `txGrade`.
   - **Misconception:** "A readability score measures how hard a text is to
     understand." It measures sentence length and syllables per word; short
     words about unfamiliar ideas score easy.
   - **Worked:** 100 words, 5 sentences, 140 syllables → FRE 206.835 −
     1.015 × 20 − 84.6 × 1.4 = 68.095; grade 0.39 × 20 + 11.8 × 1.4 − 15.59
     = 8.73.
   - **Sources:** Flesch 1948; Kincaid et al. 1975.

3. **unknown-words-and-coverage** — Unknown Words and Coverage — *Knowledge* — 12 min
   - **Drill:** `text/coverage`: the reader reads `P40` (hard band, 380
     words; untimed, logged `other`), selecting the words they do not know;
     the lab computes coverage.
   - **Do:** compute lexical coverage and the density of unknown words, and
     compare with the published estimates.
   - **Standard:** given tokens and unknown tokens, compute coverage and "one
     unknown in every N".
   - **Lab:** `text/coverage`. Presets: `ninety-eight` (500 tokens, 10 unknown →
     98%, one in 50), `ninety-five` (25 → one in 20), `ninety` (50 → one in 10).
     Pins `txCoverage`, `txOneIn`.
   - **Misconception:** "One unknown word in twenty is fine; context will
     supply it." In Hu and Nation's study of learners of English reading a
     story, most did not understand it adequately at 95% coverage; they
     estimated about 98% for unassisted reading. Others put 95% as a minimum
     and 98% as optimal, or find no threshold at all; for a fluent native
     reader it is an extrapolation.
   - **Worked:** 490 / 500 = 49/50 = 98%; one unknown in every 50 tokens.
   - **Sources:** Hu and Nation 2000; Nation 2006; Laufer and
     Ravenhorst-Kalovski 2010; Schmitt, Jiang and Grabe 2011.

4. **what-you-already-know** — What You Already Know — *Knowledge* — 12 min
   - **Drill:** `drill/compare`: A `P41` (familiar everyday topic) and B `P42`
     (unfamiliar specialist procedure), matched within one grade (`test`).
   - **Do:** compute the effect of topic familiarity on rate and comprehension
     with readability held close.
   - **Standard:** given both readings, compute both effective rates and the
     ratio, and say why readability did not predict it.
   - **Lab:** `drill/compare`, `ratioOf: err`. Presets: `typical` (A 385 words
     in 96.25 s → 240, 6/6 → 240; B 375 words in 100 s → 225, 4/6 → 150 →
     ratio 5/8 = 62.5%), `expert` (a reader who knows B's field: A 240, 6/6;
     B 375 in 90 s → 250, 6/6 → 25/24 ≈ 104.2%). Pins `drErrA`, `drErrB`,
     `drRatio`.
   - **Misconception:** "Speed is a skill independent of what you know."
     Recht and Leslie found junior-high readers' knowledge of baseball
     mattered more than their reading ability for what they recalled of a
     baseball passage; background knowledge is among the strongest
     influences on comprehension.
   - **Worked:** 150 / 240 = 5/8 = 62.5%.
   - **Sources:** Recht and Leslie 1988; Rayner et al. 2016.

5. **how-much-you-read** — How Much You Read — *Knowledge* — 8 min
   - **Drill:** `warmup` `[Q23, Q30]` (`practice`); then `text/volume` with the
     reader's minutes a day and rate.
   - **Do:** compute annual reading volume and compare what a rate gain and a
     time gain each add.
   - **Standard:** given minutes and rates, compute both volumes and the rate
     gain equal to a time gain.
   - **Lab:** `text/volume` (365 days, 90,000-word books). Presets:
     `twenty-minutes` (20 × 250 × 365 = 1,825,000 words ≈ 20.3 books),
     `faster` (20 × 300 → 2,190,000, ≈ 24.3), `longer` (30 × 250 → 2,737,500,
     ≈ 30.4), `rate-to-match` (20 × 375 → 2,737,500). Pins `txWordsYear`,
     `txBooksYear`.
   - **Misconception:** "The way to read more is to read faster." Ten more
     minutes a day at 250 adds as much as a rate gain from 250 to 375, which no
     technique reliably delivers; and reading volume is strongly associated
     with vocabulary and knowledge growth (correlational evidence).
   - **Worked:** 30 × 250 × 365 = 2,737,500 against 20 × 300 × 365 =
     2,190,000.
   - **Sources:** Anderson, Wilson and Fielding 1988; Nagy and Herman 1987.

### Course 7 — Remembering What You Read (`reading-remembering-what-you-read`, 4)

Modules: `Recall`, `Keeping it`.

1. **free-recall** — Free Recall — *Recall* — 12 min
   - **Drill:** `recall/free`: `P43` timed (`test`), then the passage hides and
     the reader writes what they remember; then the twelve idea units appear
     and the reader ticks the ones they recalled; then the six questions.
   - **Do:** compute the share of idea units recalled and a recall-adjusted
     rate, and compare with multiple-choice comprehension.
   - **Standard:** given units recalled and the reading, compute both and say
     why recall is lower than recognition.
   - **Lab:** `recall/free`, `questions: true`. Presets: `typical` (12 units, 7
     recalled; 383 words in 95.75 s → 240 × 7/12 = 140; questions 5/6),
     `strong` (10 of 12 → 200; 6/6). Pins `reRecall`, `reRate`, `reComp`.
   - **Misconception:** "Recognising the right answer is remembering."
     Multiple choice measures recognition; free recall is harder and closer to
     what you can use later.
   - **Worked:** 383 × 60 / 95.75 = 240; 240 × 7/12 = 140.
   - **Sources:** Roediger and Karpicke 2006 (free recall as the measure).

2. **retrieval-beats-rereading** — Retrieval Beats Rereading — *Recall* — 15 min, then 5 min after two days
   - **Drill:** `recall/delayed`: reread side — `P44` read twice, no test
     (`condition`); retrieve side — `P45` read once, then free recall with
     idea units ticked (`condition`). Two or more days later, any Subject page
     offers both passages' six questions as a due test. The lesson is complete
     on day one with the published shape; the reader's own delayed figures
     fill in on return.
   - **Do:** compute the delayed scores for rereading and for retrieval and the
     difference.
   - **Standard:** given delayed scores, compute both and explain why the
     immediate result favoured rereading.
   - **Lab:** `recall/delayed`, `days: 2`. Presets: `reader-example` (shown
     first; delayed 2/6 reread, 4/6 retrieved → ≈ +33.3 points; 7 of `P45`'s
     11 idea units → 7/11 ≈ 63.6%; illustrative) and `published-shape`
     (Roediger and Karpicke 2006, Experiment 1, rounded and labelled, as
     scores out of 100: 54 restudy and 68 test at two days → +14 points;
     recall 70/100, the tested group's initial free recall (20.9 of 30 idea
     units); the five-minute 81% and 75% are in the body). Pins
     `reDelayedA`, `reDelayedB`, `reDelayedDiff`, `reRecallB`.
   - **Misconception:** "Reading it again is the best way to remember it."
     Rereading wins on an immediate test and loses on a delayed one. Their test
     was free recall without feedback; the drill's delayed test is multiple
     choice, which tends to show a smaller effect.
   - **Worked:** 4/6 − 2/6 = 1/3 ≈ 33.3 points.
   - **Sources:** Roediger and Karpicke 2006.

3. **spacing-your-reviews** — Spacing Your Reviews — *Keeping it* — 8 min
   - **Drill:** the due test from Retrieval Beats Rereading if it is due, else
     `warmup` `[Q24, Q29]` (`practice`); then `recall/schedule`.
   - **Do:** compute a review schedule and its total time, and compare spaced
     with massed review.
   - **Standard:** given a first gap, a multiplier and a count, list the review
     days and the minutes.
   - **Lab:** `recall/schedule`. Presets: `expanding` (first gap 1, × 2, 5
     reviews of 10 minutes → days 1, 3, 7, 15, 31; 50 minutes), `equal` (gap 6,
     × 1 → 6, 12, 18, 24, 30), `massed` (gap 1, × 0 → all five on day 1,
     the same 50 minutes). Pins
     `reLastDay`, `reMinutes`, `reDays`.
   - **Misconception:** "Massed review works better, because it feels better."
     Review crammed into one sitting feels fluent and produces high scores
     during the session; spaced review is retained better at a delay (Cepeda
     et al. 2006). Expanding gaps are one reasonable schedule; equal gaps do
     as well or better in some studies (Karpicke and Roediger 2007).
   - **Worked:** gaps 1, 2, 4, 8, 16 → days 1, 3, 7, 15, 31.
   - **Sources:** Ebbinghaus 1885; Cepeda et al. 2006; Karpicke and Roediger
     2007.

4. **notes-in-your-own-words** — Notes in Your Own Words — *Keeping it* — 12 min
   - **Drill:** `recall/free`, summary variant: `P46` timed (377 words; logged
     `other`, so a summary does not enter the recall row of the profile), then
     a three-sentence summary from memory, then idea units ticked.
   - **Do:** compute the idea units a short summary covers and its words per
     unit, and say what a good summary leaves out.
   - **Standard:** given two summaries' lengths and units, compute and choose.
   - **Lab:** `recall/free`, `summary: true`. Presets (10 idea units; 94.25 s
     → 240 wpm): `tight` (40 words, 6 units → 3/5 = 60%, ≈ 6.7 words per
     unit, 144 wpm recalled), `copied` (90 words, 4 units → 2/5 = 40%, 22.5,
     96). Pins `reRecall`, `reWordsPerUnit`, `reRate`.
   - **Misconception:** "Highlighting is studying." Dunlosky and colleagues
     rated highlighting, rereading and summarisation all of low utility, and
     practice testing high; a summary written from memory is retrieval, which
     is what this drill makes it.
   - **Worked:** 40 / 6 ≈ 6.7 against 90 / 4 = 22.5.
   - **Sources:** Dunlosky et al. 2013.

### Course 8 — Your Training Plan (`reading-your-training-plan`, 4)

Modules: `The plan`, `The test`.

1. **a-practice-week** — A Practice Week — *The plan* — 10 min
   - **Drill:** `warmup` `P49` (`test`); then `log/plan`: the reader reviews the
     routine kept since The Daily Drill and plans the next week.
   - **Do:** plan a week of practice under a time budget, with tests.
   - **Standard:** given a budget, produce a week that meets the routine's
     rules, and find the rule an unbalanced plan breaks.
   - **Lab:** `log/plan`, budget 120 minutes. Presets: `fifteen-a-day` (5 × 15
     pacer practice + 2 × 15 test session = 105 minutes; test share 2/7
     ≈ 28.6%; fits, 15 to spare), `weekend-only` (1 × 60 test + 1 × 60 long
     practice = 120; 1/2 = 50%; fits, 0 to spare), `all-sprints` (7 × 15 =
     105, "no test in the week"). Pins `lgWeekMinutes`, `lgTestShare`,
     `lgFits`.
   - **Misconception:** "More drills means more progress." A week without a
     test reading has not measured anything, and sessions longer than
     attention lasts practise drifting.
   - **Worked:** 5 × 15 + 2 × 15 = 105 minutes; 30 / 105 = 2/7; 120 − 105 =
     15 to spare.
   - **Sources:** Ericsson, Krampe and Tesch-Römer 1993.

2. **reading-your-curve** — Reading Your Curve — *The plan* — 8 min
   - **Drill:** `warmup` `Q16` (standard band, `test`: a hard-band warm-up
     would drag the test median down); then `log/history` on the reader's
     log.
   - **Do:** decide from a log whether effective rate has changed.
   - **Standard:** given a log, state the verdict by the Subject's rule and
     name the entries that do not count.
   - **Lab:** `log/history`, trend view. Example logs (effective rates; every
     one with baselines 238, 245, 251, median 245): `real-gain` (tests 262,
     270, 281 → median 270, above; four practice entries drawn lighter),
     `noise` (tests 244, 262, 239 → 244, inside), `rate-only` (tests read at
     354, 360, 357 wpm with 4/6: effective 236, 240, 238 → 238, inside). Pins
     `lgSessions`, `lgBaseMedian`, `lgRecentMedian`, `lgLatestErr`,
     `lgVerdict`.
   - **Misconception:** "My best session is my new level." The best session is
     selected for being high; the median of the last three tests against the
     baseline range is the honest comparison.
   - **Worked:** median of 262, 270, 281 = 270; 270 − 251 = 19 above the top.
   - **Sources:** —

3. **plateaus-and-transfer** — Plateaus and Transfer — *The test* — 10 min
   - **Drill:** `drill/single` on `P47` (389 words, a dense argument, a kind
     the reader has not practised; logged `other`, because a first reading of
     a kind with no baseline would pull down the median of tests on standard
     passages); `vsLog: true` prints the reader's effective rate on it beside
     the baseline range and the recent test median from the log.
   - **Do:** compare a first reading of a new kind of text with the practised
     kind and say what a plateau in each would mean.
   - **Standard:** given the three figures, say whether the practice
     transferred and why one reading of a new kind has no baseline of its own.
   - **Lab:** `drill/single` with the log comparison. Presets (range 238–251,
     recent 270): `transfers` (97.25 s → 240 wpm, 6/6 → 240: inside, −30
     against recent), `does-not` (77.8 s → 300 wpm, the practised rate, 4/6 →
     200: below the range, −70). Pins `drWpm`, `drComp`, `drErr`, `drVsBase`,
     `drVsRecent`.
   - **Misconception:** "A plateau means I have reached my limit." It often
     means the practice has stopped asking for more, or that the gains were
     specific to the practice material; readings of a new kind of text help
     tell which.
   - **Worked:** 270 on practised text, 200 on the argument (300 × 4/6): the
     gain did not carry.
   - **Sources:** Ericsson, Krampe and Tesch-Römer 1993; Rayner et al. 2016.

4. **the-full-battery** — The Full Battery — *The test* — 15 min, done fresh
   - **Drill:** `log/profile` with `warmup` `P48` as a test (`test`; a
     warm-up cannot do free recall, so none follows); "Fill from my log" reads
     the baseline median and the latest test, and the first and latest skim,
     scan and free-recall entries, warm-ups included.
   - **Do:** compute a profile — effective rate (median of last three tests),
     gist rate, scan time per target, recall share — and compare each with the
     first measurement.
   - **Standard:** given two profiles, say which measures changed by the
     Subject's rule and which have too few readings to say.
   - **Lab:** `log/profile`. Presets: `after-practice` (effective then 245,
     the baseline median; now 266, the latest test; range 238–251, no `tests`
     list, so the tile judges 266 alone: "above the baseline range once" — the
     body works the median of the last three, 262, 270, 266 → 266, as the
     rule's evidence; gist 2/3 → 1; scan 12 s → 8 s; recall 5/12 → 7/12),
     `rate-flat` (245 → 244, inside; gist 2/3 → 2/3; scan 12 s → 7 s; recall
     flat). Pins `lgErrThen`, `lgErrNow`, `lgVerdict`, `lgGist`, `lgScan`,
     `lgRecall`.
   - **Misconception:** "One number sums up a reader." A reader is a profile:
     rate on a kind of text, comprehension, the choice of when not to read
     everything, and what is kept.
   - **Worked:** median of 262, 270, 266 = 266 against a baseline range
     topping at 251.
   - **Sources:** —

---

## §D The lab kit: `readkit`

### D.0 Conventions

Everything in `docs/philosophy/PLAN.md` §D.0 and the capkit conventions as
implemented (`docs/capital/kit-a-report.md`, "Conventions as implemented")
holds unless this section says otherwise: one function `readkit_lab(cfg)`;
cfg keys `mode`, `view`, `presets`, `preset`, `title`, `panel_title`,
`panel_intro`; inputs are text boxes with id `<prefix>In<Field>`; a preset menu
`<prefix>Preset`, a banner `<prefix>Status`; every text box survives `''`,
`banana`, `0`, `-1`, `1/0`, `A>B` with a red banner and tiles blanked to `—`;
build-time refusals for a preset key that is not an input of its view, a size
limit exceeded, an unknown view, an unknown passage id. Exact rationals over
BigInt (reuse `RATIONAL_JS` from the existing core). Each mode has one pure
`<xx>Compute(view, inst)` that `scripts/mathcheck.js` calls in its own block,
each case seen to fail when its line is broken on purpose. `readkit` joins
`KITS_WITH_EXPECTATIONS` at wiring.

**Page weight.** `readkit_lab` emits the JavaScript of the active mode only,
plus the shared rational, banner, drill and log helpers, and only the passages
the lesson's cfg names. Budget: ≤ 45 KB gzipped per lesson, measured.

**Number format.** A rate, a time, a share: when the reduced fraction's
denominator is 1 it prints as a whole number (`250 wpm`); otherwise it prints
`≈` and one decimal, rounded half up from the exact rational, never from a
float (`≈ 266.7 wpm`). A share prints the reduced fraction and the percent:
`4/5 = 80%`, `7/12 ≈ 58.3%`. Times print in seconds with at most one decimal
(`96 s`, `≈ 97.3 s`). Grouped thousands with a comma (`1,825,000`).

**Two sources of inputs, one computation.** Every view's tiles are computed
from its text inputs and nothing else. A preset writes the inputs; a drill
writes the inputs when it ends (words from the passage, milliseconds from
`performance.now()` rounded to whole ms, correct from the reader's answers).
So the arithmetic `labcheck.js` checks on presets is exactly the arithmetic a
drill uses. The drill's controls are buttons; no drill starts on a `change`
or `input` event, and no timer is created at load (the labcheck shim's
`setTimeout` fires immediately and it has no `setInterval`).

**Drill flow** (views that have a passage): *Start* shows the passage and
starts the clock → *Done* hides it and stops the clock → the questions appear
one at a time, four options each, no going back → *Score* fills the inputs,
redraws, shows which answers were right, and appends a log entry. A drill can
be abandoned (*Reset*) without logging. The passage is never visible while
questions are shown. The reader can choose to skip questions only where §C
says questions are off.

**Displays** (a drill's `display` cfg; a compare side carries its own):

- `normal` — the passage as paragraphs.
- `pacer` — the passage with a highlight that moves line by line at
  `target` wpm; the line grouping is read from layout at runtime (word spans
  by `offsetTop`), and the time per line is that line's words × 60,000 /
  target. The tile `drPacerLineMs` is computed for a stated line length
  (`lineWords` cfg), not from layout.
- `mask` — `pacer`, with every line above the highlight hidden.
- `rsvp` — one word (or `chunk` words) at a time, centred, `60,000 × chunk /
  target` ms each; the total time is fixed by the rate and the drill ends by
  itself.
- `phrases` — `rsvp` by the passage's marked phrase boundaries (§P), each
  phrase shown for its words × 60,000 / target ms.
- `gist` — only the headings and first sentence of each paragraph, for a
  `limit` of seconds; ends by itself.
- `preview` — headings, first and last paragraph for `limit` seconds, then
  the whole passage; the clock runs through both.
- `aloud` — `normal`, with the instruction to read aloud.

**The log.** One `localStorage` key, `learn-reading-log`, holding a JSON array
of entries `{v: 1, at: ISO date, lesson: slug, view, passage, display, words,
ms, correct, total, kind?, extra?}`. Reads and writes are wrapped in
try/catch; a page with storage blocked runs every drill and says, once, that
results will not be kept. Only `log/*` views and the delayed recall read it.
`log/history` can export the log as CSV text in a read-only textarea and can
clear it after a confirmation inside the page (no `confirm()` dialog). The key
contains no "theme" (the site's theme test reads every storage key).

**Randomness.** Presets are deterministic. A Schulte table or a flash string
in a drill may use `Math.random`; in a preset, it uses the preset's seed with
a stated linear congruential generator, so `labcheck` sees the same table.

**Accessibility.** Every drill is operable by keyboard; the timed displays
respect `prefers-reduced-motion` by replacing animation with discrete steps
(the pacer still moves line by line). The flash and RSVP displays carry a
sentence in the panel that they are not suitable for readers with
photosensitive conditions and can be skipped without losing the lesson.

### D.1 Modes (prefix, views, inputs, tiles)

#### drill (`dr`)

- `single`: inputs `words`, `chars`, `seconds`, `correct`, `total`
  (`total` 0 when questions are off). Tiles: `drWords`, `drTime`, `drWpm`
  (words × 60 / seconds), `drStdWpm` (chars / 6 × 60 / seconds), `drComp`
  (correct / total), `drErr` (wpm × comp); with display `rsvp`, `drWordMs`
  (60,000 × chunk / target); with `gist`, `drShown` (words shown / words).
- `compare`: the same inputs suffixed `A` and `B`; tiles `drWpmA`, `drWpmB`,
  `drCompA`, `drCompB`, `drErrA`, `drErrB`, `drErrDiff` (B − A), `drRatio`
  (B / A, of the rate or the effective rate as the cfg's `ratioOf` says),
  `drVerdictB` (when the cfg gives a baseline range: "outside the baseline
  range" or "inside"); with question kinds, `drGistA/B`, `drDetailA/B`;
  `drPacerLineMs`, `drPhraseMs` where the display has them.
- `ladder`: three runs with targets `t1 t2 t3`; tiles per run and
  `drBestTarget`, `drBestErr` (the run with the highest effective rate; ties
  go to the slower target).
- `repeat`: four runs, the first three on one passage; tiles
  `drRepeatGain` (run 3 − run 1 wpm), `drTransferGain` (run 4 − run 1).
- `sections`: one passage with two marked sections, time per section;
  tiles `drRateS1`, `drRateS2`, `drErr`.

#### eye (`ey`)

- `budget`: inputs `fix` (ms), `sac` (ms), `step` (characters per forward
  saccade), `reg` (regression share of fixations, a fraction < 1), `cpw`
  (characters per word, space included). Model: forward fixations per word
  = cpw / step; total fixations per word = (cpw / step) / (1 − reg); time per
  word = total fixations × (fix + sac); wpm = 60,000 / time per word.
  Tiles `eyFixPerWord`, `eyMsPerWord`, `eyWpm`. Variant with `regNeed` and
  `regRepair` (reg = their sum) adds `eySaved` (wpm with `regNeed` = 0 minus
  wpm as given).
- `required`: inputs `target` (wpm), `fix`, `sac`, `cpw`, `reg`. Characters a
  forward fixation must advance = target × cpw × (fix + sac) / (60,000 ×
  (1 − reg)). Tiles `eyNeeded`, `eyVerdict`: "within the word-identification
  span" (≤ 8), "within the perceptual span but beyond identification" (≤ 15),
  "beyond the perceptual span" (> 15). The thresholds are cfg values cited in
  the panel (§S Rayner 1998).
- `lines`: inputs `cpl` (characters per line), `lines`, `step`, `fix`, `sac`,
  `sweep` (ms of a return sweep with its corrective fixation). Tiles
  `eyFixPerLine` (cpl / step), `eySweepShare` (sweeps / all eye movements),
  `eyMsPerLine`.

#### flash (`fl`)

- `span`: drill: a fixation mark, then a string of `len` letters (odd, centred)
  for `ms` milliseconds, then a mask; the reader types what they saw; `n`
  trials. Inputs for presets: `targets` and `typed` as `;`-separated strings.
  Scoring is by position from centre. Tiles `flCentre` (accuracy at 0),
  `flEdge` (at the outermost positions), `flSpan` (outermost position each
  side with accuracy ≥ 1/2, printed `left 3, right 4`). The panel says the
  display time is requested, not guaranteed, and prints the measured time.
- `schulte`: drill: a 5×5 table of 1–25, click in order; inputs `seconds`,
  `errors`, `seed`. Tiles `flTime`, `flPerCell`.

#### scan (`sc`)

- `find`: a text and `targets` (prompt + the answer's word index range); the
  reader clicks the answer; inputs `found`, `wrong`, `seconds`, `words`.
  Tiles `scFound`, `scPerTarget`, `scWordsPerSec`.
- `inspect`: as `find`, with a time limit and structural targets.

#### triage (`tr`)

- `plan`: items `title, words, value, choice` (`read`, `skim`, `skip`), cfg
  rates (read wpm, skim wpm, skim coverage fraction), budget minutes. Tiles
  `trMinutes`, `trCovered` (Σ value × coverage / Σ value, read = 1, skim =
  the cfg coverage, skip = 0), `trFits`.

#### text (`tx`)

- `readability`: a bank passage (counted) or typed counts. Words as §P;
  sentences end at `.`, `!` or `?` followed by space or end (the bank avoids
  abbreviations); syllables by the stated rule: count vowel groups (a e i o u
  y), subtract a final silent `e` (not `le`), minimum 1 per word — the panel
  says it is an approximation and the tiles say "by the rule". Tiles
  `txWords`, `txSentences`, `txSyllables`, `txFre` (206.835 − 1.015 × words /
  sentences − 84.6 × syllables / words), `txGrade` (0.39 × words / sentences
  + 11.8 × syllables / words − 15.59).
- `coverage`: inputs `tokens`, `unknown`; drill: the reader clicks unknown
  words in the passage. Tiles `txCoverage`, `txRun` (tokens / unknown).
- `volume`: inputs `minutes`, `wpm`, `days`, `bookWords`. Tiles `txWordsYear`,
  `txBooksYear`.

#### recall (`re`)

- `free`: drill: read, then a textarea, then the idea-unit checklist; inputs
  `units`, `recalled`, `words`, `seconds`, `summaryWords`. Tiles `reRecall`,
  `reRate` (wpm × recall), `reWordsPerUnit`.
- `delayed`: two passages, conditions `reread` and `retrieve`; inputs
  `immA`, `delA`, `immB`, `delB`, `total`. Tiles `reKeptA`, `reKeptB`. The
  drill stores a due date in the log and offers the delayed test when it is
  due.
- `schedule`: inputs `first`, `mult`, `reviews`, `minutes`. Tiles
  `reLastDay`, `reMinutes`, `reDays` (the list).

#### log (`lg`)

- `noise`: inputs `base` (rates, comma-separated), `later`. Tiles `lgMean`,
  `lgRange`, `lgVerdict`.
- `gears`: input `wpm`; the reference table is cfg (§S). Tiles `lgNearest`,
  `lgVsAverage`.
- `history`: the reader's log, or a preset example log when it is empty.
  Inputs (for presets) `entries` as `wpm/correct/total` triples. Tiles
  `lgSessions`, `lgBaseMedian` (median of the first three effective rates),
  `lgRecentMedian` (last three), `lgLatestErr`, `lgVerdict`. A small SVG chart
  of effective rate by session (pixels may be float; tiles are not).
- `plan`: rows `drill, sessions, minutes`. Tiles `lgWeekMinutes`,
  `lgTestShare`.
- `profile`: four measures now and then. Tiles `lgErrNow`, `lgErrThen`,
  `lgVerdict`.

### D.2 What the kit must never do

- Print a measurement as "your reading speed" or "your level".
- Start a timer, an animation or a flash on load or on a `change`/`input`
  event.
- Show the passage while its questions are on screen.
- Send anything anywhere, or read storage outside its one key (and the
  site's own keys, which it does not touch).
- Score a free recall by itself: the reader ticks the idea units.
- Print a tile derived from layout or from a floating-point timer value
  other than whole milliseconds.

---

### D.3 Amendments from the pre-authoring reviews (these win over D.0–D.2)

Where `docs/reading/kit-report.md` records a deviation from D.0–D.3, the
report describes what the kit does and wins; authors work from it. A ladder
carries no warm-up (page weight).

1. **Six questions** per passage (three gist, three detail); one question is
   1/6 of comprehension, and every compare, ladder and repeat panel prints
   "one question is ≈ 16.7 points; a one-question difference is not a
   result".
2. **Log kinds.** Every entry carries a required `kind`: `baseline`, `test`,
   `practice`, `condition` or `other`, set by the cfg (per side in a compare;
   default `condition` for compare sides, `practice` for practice and warm-up
   readings). `log/history`, `log/noise` and `log/profile` compute over
   `baseline` and `test` only; `practice` is drawn as a lighter series;
   `condition` and `other` are listed but not charted. Entries also record the
   display, the order a compare ran in, and `extra` (the attention tick, a
   lapse count, the suppression tick, a Schulte time).
3. **Verdicts** have three tiers, everywhere (`lgVerdict`, `drVerdictB`):
   "inside the baseline range"; "above the baseline range once — a fourth
   reading does this about one time in four"; "above the baseline range on
   the median of the last three tests". `drVerdictB` is in every compare
   view and reads the range from the reader's `baseline` entries when the cfg
   gives none; with no baselines it says so. `log/noise` takes any number of
   baselines and tests (tiles `lgRange`, `lgTestMedian`, `lgVerdict`).
4. **`drill/practice`** (new view): cfg `pool` (a list of passage dicts); it
   serves the first pool passage whose id is not in the log, with display
   `pacer` at the reader's target or `normal` when the reader ticks "this is a
   test" (logged `test`); "paste your own text" (counted by the kit's rule,
   unscored, `practice`). Tiles `drHold` (the fastest pacer target at which the
   reader's last three practice readings at that target all scored ≥ 4/6, or
   "not yet"), `drNextTarget` (hold × 21/20 after three holds in a row, × 19/20
   after two misses), `drTestDue` (a test is due when four practice sessions
   have passed since the last test). A page with a pool may weigh up to 67 KB
   gzipped (the library ceiling).
5. **`warmup`** (any view): a passage dict or a list; renders a compact timed
   reading with questions above the view's panel and serves the first passage
   in the list not yet logged; logged with the kind the cfg gives (default
   `practice`). This keeps one lab per lesson while every lesson has a timed
   reading. A due delayed test (item 9) takes the warm-up's place when one is
   due.
6. **`drill/ladder`**: `drBestTarget` is the fastest target whose
   comprehension is at least cfg `hold` (default 4/6), with `drBestErr` its
   effective rate; `drTopErr` is the highest effective rate of the three.
7. **Gist display**: tile `drGistPerMin` (gist questions right per minute); no
   effective rate is printed for a skim.
8. **`flash/span`** is partial report: a `len`-letter string (default 15,
   positions −7…+7), a mask, then two or three cued positions answered by
   buttons. Tiles name what is measured: "letters identified by position in a
   150 ms flash". The panel gives saccade latency as about 175–200 ms and
   prints the measured display time.
9. **`recall/delayed`**: the reread side reads twice with no immediate test;
   the retrieve side reads once and does free recall with idea units ticked;
   both are offered their six questions as a due test after two days (a
   banner on any readkit page). Tiles `reDelayedA`, `reDelayedB`,
   `reDelayedDiff`; a preset may carry the published percentages directly.
10. **`eye/budget`** with a regression split is dropped from §C (the body works
    it as an example); `eye/lines` is not used by any lesson and may be
    removed. `eye/required` verdicts say "at these settings", and the view lets
    `fix` and `sac` be changed.
11. **Order** in a compare: cfg `order` `AB`, `BA` or `alternate` (default:
    alternate by the parity of the log's length); the entry records it.
12. **RSVP cap.** A drill's RSVP or phrase display refuses targets above 600
    wpm with a sentence (beyond it the display is a flicker); presets may state
    any rate. RSVP tiles print requested and measured ms per word.
13. **Fallbacks and ticks.** `aloud` offers "I can't read aloud here", which
    makes the side a typed published figure (183, labelled). The suppression
    side asks "I kept counting the whole way". `drill/practice` and
    `drill/sections` ask "did your attention leave the text?". All go in
    `extra` and print beside the tiles.
14. **Keyboard.** Click-the-word drills (`scan`, `text/coverage`) are operable
    by Tab/arrow keys with Enter; the pacer highlight is not colour alone (a
    margin bar or underline as well).
15. **`log/gears`** takes `stdwpm` (standard-length words) as well as `wpm`;
    the gear comparison uses `stdwpm`, the average comparison uses `wpm`
    (Brysbaert's 238 is in words).
16. **`text/coverage`** tile `txOneIn` ("one unknown in every N tokens")
    replaces `txRun`.

## §P The passage bank

Passages live in `content/reading/passages/` as data
(`PASSAGES = {id: {...}}`), written for this Subject by one author and reviewed
for accuracy, band and question quality before any lesson uses them.

**Shape of a passage:**

```
"P01": {
  "title": "…",                # plain text
  "band": "standard",          # easy | standard | hard
  "kind": "narrative",         # narrative | expository | procedural | argument
  "paragraphs": ["…", …],      # plain text; a "## " paragraph is a heading
  "phrases": True/False,       # whether "|" marks phrase boundaries (only P20)
  "id": "P01",                 # equal to its key
  "questions": [               # exactly 6: 3 gist, 3 detail (P32: 4 gist)
    {"q": "…", "a": ["…","…","…","…"], "c": 2, "kind": "detail" | "gist"},
  ],
  "ideas": ["…", …],           # 8–14 idea units (only passages used in recall)
  "sections": [i, j],          # paragraph index where section 2 starts (P37)
}
```

**Rules.**

1. **Original.** Written for the Subject; no passage paraphrases a published
   text. Fiction may be in any period; expository passages state only
   well-established facts that a reviewer can check, and the bank's review
   checks every one.
2. **Length.** 350–500 words for standard drills; 550–650 for `P37`, `P32`
   and the scanning texts; counted by the kit's rule (a word is a
   whitespace-separated token containing a letter or a digit).
3. **Bands** by Flesch–Kincaid grade computed with the kit's rule: easy 5–7,
   standard 8–11, hard 13 and above. A matched pair (§C says which) differs
   by at most 30 words and one grade.
4. **Questions** (six; three gist and three detail, except `P32`'s four gist)
   cannot be answered from general knowledge: before a question
   is kept, its author answers it without the passage, and if the right
   option is guessable, it is rewritten (Rayner et al. 2016 make this point
   about speed-reading tests). Exactly one defensible answer; distractors
   are plausible and appear in or near the text. The correct index is
   rotated.
5. **No passage is used in two lessons' drills.** Each lesson's `how_to`
   reminds the reader that rereading a passage measures memory.
6. **Garden paths.** `P30` and `P31` each contain exactly one temporarily
   ambiguous sentence (of the "the horse raced past the barn fell" kind, but
   original) with a question that depends on resolving it.
7. **Topic familiarity.** `P41` is everyday (a household or travel scene);
   `P42` is a specialist topic (e.g. a procedure in a field most readers do
   not know), within one Flesch–Kincaid grade of `P41`.

**Assignments** (band; kind; use):

| id | band | kind | lesson |
| --- | --- | --- | --- |
| P01 | standard | narrative | words-per-minute |
| P02, P03 | standard | expository, narrative | comprehension-and-effective-rate |
| P04, P05 | standard | narrative, expository | one-reading-is-one-measurement |
| P06 | standard | expository | fixations-and-saccades |
| P07, P08 | standard | matched pair | looking-back |
| P09, P10 | standard | matched pair | lines-and-return-sweeps |
| P11 | standard | narrative | training-the-periphery |
| P12, P13 | standard | matched pair | reading-with-a-pacer |
| P14, P15, P16 | standard | matched triple | choosing-a-target-pace |
| P17, P18 | standard | narrative, expository | sprints-above-comfort |
| P19, P20 | standard | matched pair (P20 phrase-marked) | reading-in-phrases |
| P21, P22 | standard | matched pair | fewer-needless-regressions |
| P23, P24 | standard | matched pair | repeated-reading-and-transfer |
| P25, P26 | easy | narrative pair | the-inner-voice |
| P27, P28 | standard | matched pair | silencing-the-inner-voice |
| P29 | standard | narrative | one-word-at-a-time |
| P30, P31 | standard | matched pair, one garden path each | rsvp-without-looking-back |
| P32 | standard | expository with headings, 560–600 | skimming-for-gist |
| P33, P34 | standard | expository with headings, matched | what-skimming-costs |
| P35, P36 | standard | expository with headings, matched | previewing-before-reading |
| P37 | mixed | narrative section + dense section | shifting-gears |
| P38, P39 | easy, hard | expository | your-rate-on-hard-text |
| P40 | hard | expository | unknown-words-and-coverage |
| P41, P42 | standard | familiar, unfamiliar | what-you-already-know |
| P43 | standard | expository, 12 ideas | free-recall |
| P44, P45 | standard | matched, ideas | retrieval-beats-rereading |
| P46 | standard | expository, ideas | notes-in-your-own-words |
| P47 | hard | argument | plateaus-and-transfer |
| P48, P49 | standard | expository (P48 ideas; P49 headings) | the-full-battery |
| S01 | — | ferry timetable notice with prose | scanning-for-a-target |
| S02 | — | a museum's visitor guide | the-full-battery |
| B01 | — | front and back matter of an imaginary book | inspectional-reading |

`P09` and `P10` are the warm-ups of `typical-rates-and-reading-gears` and
`keeping-a-practice-log`; `P06`, `P11` and `P49` are warm-ups too (§C).
`measuring-difficulty` counts `P38`, `P39` and one standard passage (no drill),
the one exception to rule 5. `S02` is the second scanning text, served on a
second visit.

**The practice pool** (`content/reading/passages/pool.py`, `Q01`–`Q30`): the
Daily Drill's texts, served in order, never assigned to one lesson except the
warm-ups `Q16`, `Q19`–`Q24`, `Q29` and `Q30` (§C); the Daily Drill page carries `Q01`–`Q15`
and `Q26`–`Q28` (18, for page weight), and `Q17`, `Q18` and `Q25` are unplaced. Q01–Q08
easy, Q09–Q22 standard rising, Q23–Q30 hard; 380–480 words; six questions;
kinds mixed. After the pool, the reader practises on their own pasted text.

---

## §E Package layout and the author's checklist

```
content/reading/
  __init__.py                       PATH, COURSES, numbering loop
  passages/__init__.py              PASSAGES = {**bank_a.PASSAGES, **bank_b.PASSAGES}
  passages/bank_a.py                P01–P24
  passages/bank_b.py                P25–P49, S01, S02, B01
  c1_measure/__init__.py            COURSE; lessons = part_a.LESSONS
  c1_measure/part_a.py
  c2_eyes/ c3_guided/ c4_inner_voice/ c5_skim_scan/ (part_a, part_b)
  c6_difficulty/ c7_remembering/ c8_training_plan/
content/spoken/reading.py           SPOKEN = {}
```

A lesson module imports the bank (`from reading.passages import PASSAGES`)
and puts the passage dicts themselves into its lab cfg (`"passage":
PASSAGES["P01"]`, `"passages": [PASSAGES["P07"], PASSAGES["P08"]]`), each
dict carrying its own `id`. The kit never imports `content/`; it validates
the dict's shape at build time and embeds only what it is given. Course fields and lesson fields are exactly
those of `docs/philosophy/PLAN.md` §E (the field table and its ranges), with
`body` 7–16 blocks.

**Per-lesson procedure** — `docs/philosophy/PLAN.md` §E's, with
`python3 scripts/preview_subject.py reading --course <slug> --out <dir>` to
render, and these additions:

1. Do the drill yourself in a real browser before writing the body (the
   orchestrator gives a Playwright snippet that opens the page); a drill
   that is confusing to do is a lesson defect.
2. Every preset's figures appear in a body `p` with the preset's name, and
   every figure in prose is recomputed.
3. The `steps` are the exercise protocol — what to do, in order, when you
   repeat the drill on another day — not a summary of the body.

---

## §F Voice: a coach who has read the research

The library's voice for this Subject is closer to the read-alongs' warmth than
to the mathematics paths' austerity, because the operator asked for practice,
and practice is coached. It keeps every hard rule of correctness.

- **"You", warmly, and about the reader's own numbers.** "Your three baselines
  were 238, 251 and 245" is the target sentence; "studies show readers…" is
  the fallback.
- **Try first, then explain.** Where §C says the body sends the reader to the
  drill first, the first `p` does so in one or two sentences, and the second
  starts from what they probably found.
- **The history as a story with people in it**, at most once a lesson and
  only where it explains something: the jumps described in Javal's laboratory
  around 1879, and his word "saccade"; Huey's 1908 book; Evelyn Wood's courses from 1959 and the claims made for them;
  Woody Allen's line about *War and Peace*; the 2014 apps; the 2016 review by
  Rayner's colleagues, published after his death in 2015.
- **Presented, not endorsed — both ways.** The speed-reading tradition's claims
  are stated at their strongest, with what its practitioners say they
  experience, before the evidence; the research is cited with its limits
  (small samples, lab tasks, college students). Never "speed reading is a
  scam" in the lesson's voice; never "science proves". A technique that
  helps some readers in some conditions is described that way.
- **No promises.** No lesson says the reader will double or triple their
  speed. What the Subject promises is that the reader will know what their
  numbers are and what moved them.
- **One light remark** at most, and never at the reader's expense.
- **No slang, no first-person anecdotes, no "let's dive in".**
- The `note` says what the lesson's measurement cannot settle (one passage,
  one day; a lab task, not your reading life). The last `p` of the body
  points to the next lesson by title (at a course's end, to the next course).

**One exemplary paragraph** (a `p` for “Comprehension and the Effective
Rate”, after the drill):

> Look at your two readings side by side. If the second was faster — and for
> most people told to go as fast as they can, it is, often by a lot —
> look next at the questions. The usual result is a rate that went up and a
> score that went down, and the question that matters is what happened to
> their product. Four hundred words at 480 words a minute with two questions
> in six right is, in understood words per minute, worse than the same
> length at 240 with all six: 160 against 240. That product is the effective
> reading rate, and it is the number every drill in this Subject reports
> beside your rate, because a rate on its own cannot tell a fast reader from
> a fast page-turner.

---

## §G What is left out, and why

- **Reading instruction** for children or for developing readers, and
  dyslexia. Repeated reading is mentioned as a method from that field, not
  taught. The Subject says, in Measure Your Reading's `not_covered`, that a
  reader who finds reading effortful should see a specialist, not a drill.
- **Reading in another language** beyond the note on coverage.
- **Screen versus paper**, fonts and typography beyond line length: the
  evidence is large and mixed, and none of it is a drill.
- **Photoreading, "mental photography" and subliminal methods**: named once in
  Testing a Speed Claim as claims that make no testable prediction short of
  ordinary comprehension questions, and tested by the same three
  computations.
- **Brain-training games**: the general literature on transfer is summarised
  in a sentence in Training the Periphery and Plateaus and Transfer.
- **Eye-tracking hardware.** The kit draws illustrative fixation patterns from
  the model; it never claims to track the reader's eyes.

---

## §S Sources the lessons may cite

Cited by author and year in prose; never quoted at length. The accuracy review
checks every figure the lessons take from these before authoring.

- Acklin, D. and Papesh, M. H. (2017). Modern speed-reading apps do not
  foster reading comprehension. *American Journal of Psychology* 130(2).
- Adler, M. J. and Van Doren, C. (1972). *How to Read a Book*, revised edition
  (first edition Adler 1940). Levels of reading; inspectional reading.
- Anderson, R. C., Wilson, P. T. and Fielding, L. G. (1988). Growth in reading
  and how children spend their time outside of school. *Reading Research
  Quarterly* 23(3).
- Benedetto, S. et al. (2015). Rapid serial visual presentation in reading:
  the case of Spritz. *Computers in Human Behavior* 45.
- Brysbaert, M. (2019). How many words do we read per minute? A review and
  meta-analysis of reading rate. *Journal of Memory and Language* 109.
  Silent reading of English: about 238 wpm nonfiction, 260 fiction; oral
  about 183.
- Carver, R. P. (1985). How good are some of the world's best readers?
  *Reading Research Quarterly* 20(4).
- Carver, R. P. (1990). *Reading Rate: A Review of Research and Theory*.
  Academic Press. The five gears (scanning ~600, skimming ~450, rauding
  ~300, learning ~200, memorising ~138 standard-length words per minute for
  college students); standard-length words of six characters.
- Cepeda, N. J. et al. (2006). Distributed practice in verbal recall tasks.
  *Psychological Bulletin* 132(3).
- Duggan, G. B. and Payne, S. J. (2009). Text skimming: the process and
  effectiveness of foraging through text under time pressure. *Journal of
  Experimental Psychology: Applied* 15(3).
- Dunlosky, J. et al. (2013). Improving students' learning with effective
  learning techniques. *Psychological Science in the Public Interest* 14(1). Rated
  highlighting, rereading and summarisation low utility; practice testing and
  distributed practice high.
- Dyson, M. C. (2004). How physical text layout affects reading from screen.
  *Behaviour & Information Technology* 23(6).
- Ebbinghaus, H. (1885). *Über das Gedächtnis*.
- Ericsson, K. A., Krampe, R. T. and Tesch-Römer, C. (1993). The role of
  deliberate practice in the acquisition of expert performance.
  *Psychological Review* 100(3).
- Flesch, R. (1948). A new readability yardstick. *Journal of Applied
  Psychology* 32(3).
- Hardyck, C. D. and Petrinovich, L. F. (1970). Subvocal speech and
  comprehension level as a function of the difficulty level of reading
  material. *Journal of Verbal Learning and Verbal Behavior* 9.
- Hu, M. and Nation, I. S. P. (2000). Unknown vocabulary density and reading
  comprehension. *Reading in a Foreign Language* 13(1).
- Huey, E. B. (1908). *The Psychology and Pedagogy of Reading*.
- Jackson, M. D. and McClelland, J. L. (1979). Processing determinants of
  reading speed. *Journal of Experimental Psychology: General* 108(2).
  Effective reading speed = rate × comprehension.
- Just, M. A., Carpenter, P. A. and Masson, M. E. J. (1982). What eye
  fixations tell us about speed reading and skimming. Eye-Lab technical
  report, Carnegie-Mellon University.
- Kincaid, J. P. et al. (1975). Derivation of new readability formulas for
  Navy enlisted personnel. Research Branch Report 8-75.
- Masson, M. E. J. (1982). Cognitive processes in skimming stories. *Journal
  of Experimental Psychology: Learning, Memory, and Cognition* 8(5).
- McConkie, G. W. and Rayner, K. (1975). The span of the effective stimulus
  during a fixation in reading. *Perception & Psychophysics* 17(6).
- Nagy, W. E. and Herman, P. A. (1987). Breadth and depth of vocabulary
  knowledge. In McKeown and Curtis (eds.), *The Nature of Vocabulary
  Acquisition*.
- Nation, I. S. P. (2006). How large a vocabulary is needed for reading and
  listening? *Canadian Modern Language Review* 63(1).
- Potter, M. C. (1984). Rapid serial visual presentation (RSVP): a method for
  studying language processing. In Kieras and Just (eds.), *New Methods in
  Reading Comprehension Research*.
- Rayner, K. (1998). Eye movements in reading and information processing: 20
  years of research. *Psychological Bulletin* 124(3). Fixations ~200–250 ms
  in silent reading; saccades ~7–9 letter spaces; regressions ~10–15%;
  perceptual span ~3–4 letters left, ~14–15 right.
- Rayner, K. (2009). Eye movements and attention in reading, scene
  perception, and visual search. *Quarterly Journal of Experimental
  Psychology* 62(8).
- Rayner, K., Schotter, E. R., Masson, M. E. J., Potter, M. C. and Treiman, R.
  (2016). So much to read, so little time: how do we read, and can speed
  reading help? *Psychological Science in the Public Interest* 17(1).
- Recht, D. R. and Leslie, L. (1988). Effect of prior knowledge on good and
  poor readers' memory of text. *Journal of Educational Psychology* 80(1).
- Robinson, F. P. (1946). *Effective Study*. SQ3R.
- Roediger, H. L. and Karpicke, J. D. (2006). Test-enhanced learning: taking
  memory tests improves long-term retention. *Psychological Science* 17(3).
- Samuels, S. J. (1979). The method of repeated readings. *The Reading
  Teacher* 32(4).
- Schotter, E. R., Tran, R. and Rayner, K. (2014). Don't believe what you read
  (only once): comprehension is supported by regressions during reading.
  *Psychological Science* 25(6).
- Slowiaczek, M. L. and Clifton, C. (1980). Subvocalization and reading for
  meaning. *Journal of Verbal Learning and Verbal Behavior* 19.
- Therrien, W. J. (2004). Fluency and comprehension gains as a result of
  repeated reading: a meta-analysis. *Remedial and Special Education* 25(4).

- Carver, R. P. (1992). Reading rate: theory, research, and practical
  implications. *Journal of Reading* 36(2). Most readers hold a relatively
  constant rauding rate and seldom shift gear; recommends shifting
  deliberately.
- Karpicke, J. D. and Roediger, H. L. (2007). Expanding retrieval practice
  promotes short-term retention, but equally spaced retrieval enhances
  long-term retention. *JEP: Learning, Memory, and Cognition* 33(4).
- Laufer, B. and Ravenhorst-Kalovski, G. C. (2010). Lexical threshold
  revisited. *Reading in a Foreign Language* 22(1). 95% minimal, 98% optimal.
- Pollatsek, A., Bolozky, S., Well, A. D. and Rayner, K. (1981). Asymmetries in
  the perceptual span for Israeli readers. *Brain and Language* 14.
- Rayner, K., Slattery, T. J. and Bélanger, N. N. (2010). Eye movements, the
  perceptual span, and reading speed. *Psychonomic Bulletin & Review* 17(6).
- Schmitt, N., Jiang, X. and Grabe, W. (2011). The percentage of words known
  in a text and reading comprehension. *Modern Language Journal* 95(1).
- Wade, N. J. and Tatler, B. W. (2009). Did Javal measure eye movements during
  reading? *Journal of Eye Movement Research* 2(5). The jumps were observed by
  Lamare in Javal's laboratory (and by Hering independently); Javal named
  them saccades.
- The Evelyn Wood Reading Dynamics courses (from 1959) and Woody Allen's line
  are cited through Rayner et al. 2016.

---

## §H Wiring notes for the orchestrator

As `docs/capital/PLAN.md` §H and AGENTS.md §0's list, with these values:

- Package `reading`; path slug `reading-faster`; check-id prefix `read`.
  Check ids `read-course8-lesson-<lesson-slug>`, at most 60 characters.
- `READ_DISCLAIMER_RE = r"one measurement, not your reading speed"`.
- `content/spoken/reading.py`; `reading_semantic_copy` in `test_public_copy`.
- Wire only after the Phenomenology Subject's PR has merged; rebase on main
  first. Twelve Subjects after wiring; every count is updated in the wiring
  commit, counting Phenomenology's pages as already there.
- The PATH's tagline and description say "Eight courses and 42 lessons"; they
  move with §B.
- `readkit` joins `KITS_WITH_EXPECTATIONS` last.
- The drills need browser verification the shim cannot give: a Playwright
  script under the scratchpad (not committed) opens one page per display and
  runs a drill end to end before the PR.

---

## §R Review record

The specification is reviewed before authoring by two models independently —
a pedagogy review (Fable, the `pedagogical-expert` brief) and an accuracy
review (Opus) that checks every claim about the research against §S — and each
course again after authoring, as for *Capital*. Findings and their
resolutions are appended here.

### Pre-authoring review, 2026-10-24

Two independent reviews: `docs/reviews/reading-spec-pedagogy-review.md`
(Fable) and `docs/reviews/reading-spec-accuracy-review.md` (Opus, with web
search on the doubtful claims). Resolution:

- **Practice made central** (pedagogy 1–7): a practice pool `Q01`–`Q30` and the
  `drill/practice` view with own-text pasting; a new lesson, The Daily Drill,
  in Guided Practice, stating the routine; every later lesson ends with it; a
  `warmup` reading on every calculator lesson, so every lesson has a timed
  reading; log `kind`s so curves use baselines and tests only.
- **Order** (pedagogy 16–20): Guided Practice moved to Course 2 and How the Eyes
  Read to Course 3, fixing the pacer-before-taught break; Lines and Return
  Sweeps cut (its fact is a `ul` in Fixations and Saccades); Reading in
  Phrases moved to Course 4 with word-RSVP against phrase-RSVP as the
  control; Course 6 opens with the reader's own easy/hard drill. Count stays
  42.
- **Measurement honesty** (pedagogy 8–10, 14, 24): six questions per passage;
  `P01` scored; four baselines; the three-tier verdict and the
  median-of-three-tests rule; `drBestTarget` defined by the hold threshold;
  the one-question sentence in every compare panel; compare order alternated.
- **Drill design** (pedagogy 25–33): retrieval-beats-rereading redesigned (no
  immediate test on the reread side); aloud fallback; suppression tick; span
  drill as partial report on 15-letter strings; RSVP capped at 600 wpm in
  drills; keyboard operation; `fewer-needless-regressions` compares paced and
  unpaced readings with self-reported lapses; `plateaus-and-transfer` reads
  its comparison from the log.
- **Accuracy** (accuracy 1–24): Dunlosky's ratings (summarisation low);
  Carver's constancy law and his recommendation to shift deliberately;
  Schotter, Tran and Rayner's trailing mask and its cost on ordinary sentences;
  units in the gears lesson (standard-length words); the span drill measures
  letters without context, and the reading span's asymmetry follows
  attention; Javal via Wade and Tatler; inner-voice studies (difficult text;
  EMG feedback against articulatory suppression); RSVP (Potter's sentences,
  Benedetto's fatigue); "gist suffers less than detail"; Therrien's transfer;
  Hu and Nation's learners and the contested threshold; Recht and Leslie's
  recall measure; spacing against expanding schedules; reading volume as
  correlational; the eye-budget model's understatement of a regression's
  cost; verdicts "at these settings"; every blank preset filled and every
  figure recomputed.

### Reconciliation with the authored lessons, 2026-10-25

- §C brought into agreement with the lessons as written (`content/reading/c*/part_*.py`)
  and docs/reading/kit-report.md: preset instances and figures, passage word counts,
  log kinds (Course 1 takes three baselines and logs `P05` as `test`; `P40`, `P46` and
  `P47` log `other`), pins, and the reworded misconceptions; §B gains the median rule's
  1-in-5 false-positive rate under pure noise (3/15, checked by enumeration).
- Passages: the guessable or doubly-answerable questions P03 Q2, P05 Q1, P12 Q4, P13 Q6
  and P14 Q6 rewritten; P31's later cues ("with his good hand", Klara "pulling the oars",
  "out of breath") removed so its garden-path question depends on that sentence. No word
  count or correct-answer index changed.
- Reading Your Curve's test warm-up moved from the hard-band `Q25` to the standard-band
  `Q16`.
