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

> Read faster in the ways that work, and find out for yourself which ones do
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
2. A quiet ten to twenty minutes per lesson, and a keyboard or a touchscreen.
   Every drill is timed; a drill run while you are interrupted measures the
   interruption.
3. The arithmetic is a division and a product. The labs do it; what is asked of
   you is to read each number for what it is a measurement of.
4. A willingness to be measured honestly. The comprehension questions are
   there so that a fast time with nothing understood shows up as what it is.

**why_order** (paragraphs):

1. Measurement comes first because every later claim — that a pacer helps, that
   a flashed stream is faster, that skimming loses detail — is a comparison of
   two measurements, and a comparison means nothing until you know how much one
   measurement varies on its own.
2. The eye comes second because it sets the limits. Once you have computed what
   a fixation costs and how far a glance reaches, you can test any speed claim
   in a line of arithmetic, and the rest of the Subject does.
3. Guided practice and the inner voice come next: the techniques the
   speed-reading tradition teaches, each tried as a drill with a control
   condition, so you see what it does to your rate and to your comprehension.
4. Skimming, difficulty and memory come after because they are where the real
   time is saved or lost: by not reading what you do not need, by knowing more
   words and more about the subject, and by remembering what you read the first
   time. The training plan comes last and uses all of it.

**sequence_intro**:

> Each course assumes the ones before it and nothing else. Measure Your Reading
> gives every later drill its scoring; How the Eyes Read gives the limits every
> technique is tested against; Guided Practice and The Inner Voice and Flashing
> Words try the classic techniques against a control; Skimming, Scanning and
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
| 2 | `reading-how-the-eyes-read` | How the Eyes Read | 6 | Beginner |
| 3 | `reading-guided-practice` | Guided Practice | 6 | Intermediate |
| 4 | `reading-inner-voice-and-flashing-words` | The Inner Voice and Flashing Words | 5 | Intermediate |
| 5 | `reading-skim-scan-and-preview` | Skimming, Scanning and Previewing | 7 | Intermediate |
| 6 | `reading-words-knowledge-and-difficulty` | Words, Knowledge and Difficulty | 5 | Intermediate |
| 7 | `reading-remembering-what-you-read` | Remembering What You Read | 4 | Intermediate |
| 8 | `reading-your-training-plan` | Your Training Plan | 4 | Intermediate |

Total 42. Course 5 has more than six lessons and splits into `part_a.py`
(lessons 1–4) and `part_b.py` (5–7); every other course is one `part_a.py`.

The `reading-` prefix keeps course slugs from colliding with other Subjects'.
Check ids take the form `read-course8-lesson-<lesson-slug>` (20 characters
before the slug); every lesson slug in §C is at most 40 characters, so every
check id is at most 60, inside the 72-character cap.

**Module names.** Each course has two or three modules, named in its §C
header; every lesson's `module` is one of them, plain text, at most 40
characters.

**Every lesson's lab is a drill or computes on one** (§D). "The drill" in §C
means the lab's interactive run on the named passage(s); "the presets" are the
deterministic instances `labcheck.js` checks. A preset is always a plausible
reader's result written out in numbers (e.g. "a reader who took 96 seconds over
400 words and answered 4 of 5"), never "you".

---

## §C Every lesson

Format:

- **slug** — Title — *module*
- **Drill:** what the reader does in the lab, on which passages (§P ids).
- **Do:** the observable objective; `standard` measures it.
- **Lab:** mode/view; presets and their instances; pinned tiles.
- **Misconception:** the wrong model `mistakes[0]` names and refutes.
- **Worked:** the single worked example, in one line.
- **Sources:** what the explanation rests on (§S keys).

Preset ids are suggestions; the INSTANCES are not optional. Where an entry
gives only an id and a description, the author designs the numbers so that
the figures come out as stated, records them here in the same commit, and a
reviewer rejects a lesson whose entry still carries a bare id.

Every passage id named in §C must exist in the bank (§P) with the stated band;
an author who needs to change one changes it here.

### Course 1 — Measure Your Reading (`reading-measure-your-reading`, 5)

Modules: `Rate and comprehension`, `Reading your numbers`.

The course gives every later drill its scoring and makes the reader take three
baseline readings. Its `how_to` says: do every drill the first time you open
the lesson, before reading the explanation, and do not practise on a passage
you have already read in a drill.

1. **words-per-minute** — Words per Minute — *Rate and comprehension*
   - **Drill:** a timed reading of `P01` (standard, ~400 words), no questions
     scored yet; the lab counts the words and computes the rate. The body's
     first `p` sends the reader to the drill before explaining anything.
   - **Do:** compute a reading rate from a word count and a time, in words and
     in standard words (six characters including the space), and say which
     count a published figure uses.
   - **Lab:** `drill/single`, display `normal`, questions off. Presets:
     `steady` (400 words in 96 s → 250 wpm), `slow` (400 in 160 s → 150),
     `long-words` (the same 400 words with 2,640 characters → 440 standard
     words; 440 in 96 s → 275 standard wpm). Pins `drWpm`, `drStdWpm`.
   - **Misconception:** "A rate counted in words is comparable across texts."
     Long words and short words make the same count differ; this is why
     Carver counts six-character standard words and why the Subject's
     references say which count they use.
   - **Worked:** 400 words × 60 / 96 s = 250 wpm; 2,640 characters / 6 = 440
     standard words; 440 × 60 / 96 = 275.
   - **Sources:** Carver 1990; Brysbaert 2019.

2. **comprehension-and-effective-rate** — Comprehension and the Effective Rate — *Rate and comprehension*
   - **Drill:** a timed reading of `P02` (standard) followed by its five
     questions; then the same at "as fast as you can" on `P03`.
   - **Do:** compute comprehension and effective rate for two readings and say
     which reading delivered more understood words per minute.
   - **Lab:** `drill/compare`, side A "your usual pace" on `P02`, side B "as
     fast as you can" on `P03`, both `normal`. Presets: `pushed-too-far`
     (A: 400 words, 100 s, 5/5 → 240 wpm, effective 240; B: 400, 50 s, 2/5 →
     480 wpm, effective 192), `worth-it` (A as before; B 400, 75 s, 4/5 → 320,
     effective 256). Pins `drWpmA`, `drWpmB`, `drErrA`, `drErrB`.
   - **Misconception:** "The faster reading is the better reading." Effective
     rate makes the trade visible; Jackson and McClelland used this measure in
     1979, and it is why the Subject never reports a rate without the
     comprehension beside it.
   - **Worked:** 480 wpm × 2/5 = 192 effective wpm < 240 × 5/5 = 240.
   - **Sources:** Jackson and McClelland 1979; Rayner et al. 2016.

3. **one-reading-is-one-measurement** — One Reading Is One Measurement — *Reading your numbers*
   - **Drill:** two more timed readings with questions, `P04` and `P05`
     (both standard), on the same sitting, at the usual pace. With
     `words-per-minute`'s these are the reader's three baselines.
   - **Do:** compute the spread of three baseline rates and decide whether a
     later change is larger than the spread.
   - **Lab:** `log/noise`. Presets: `tight` (rates 238, 251, 245 → mean 734/3
     ≈ 244.7, range 13), `wide` (rates 212, 268, 240 → range 56), `real-gain`
     (baseline 238, 251, 245; later 290 → 290 − 251 = 39 above the best
     baseline, 3 ranges), `no-gain` (baseline 212, 268, 240; later 262 —
     inside the range). Pins `lgMean`, `lgRange`, `lgVerdict` (the sentence
     "outside the baseline range" / "inside the baseline range").
   - **Misconception:** "My rate on one test is my reading speed." The same
     reader on two passages of the same band, minutes apart, can differ by
     tens of words per minute; a change inside that spread is not evidence.
   - **Worked:** baseline 212, 268, 240 → range 268 − 212 = 56; a later 262 is
     inside it.
   - **Sources:** Carver 1990 (rate varies with passage); the log is the
     reader's own.

4. **typical-rates-and-reading-gears** — Typical Rates and Reading Gears — *Reading your numbers*
   - **Drill:** the reader's own median baseline (from the log, or typed)
     compared with Brysbaert's averages and with Carver's five gears.
   - **Do:** place a measured rate against the published averages for silent
     reading and against the five gears, and name the purpose each gear
     serves.
   - **Lab:** `log/gears`. Input: one rate. Presets (gear table from §S Carver, verified
     by the accuracy review): `median-reader` (238 → nearest gear learning,
     200, since 38 < 62), `fast-reader` (320 → rauding), `claim` (1,000 →
     "above every gear"). Pins
     `lgNearest`, `lgVsAverage` (rate / 238 as a fraction and ≈ percent).
   - **Misconception:** "There is one right speed and faster is always
     better." Carver's gears are five processes with different goals; the
     same reader should use several, and the Subject teaches the shift.
   - **Worked:** 320 / 238 = 160/119 ≈ 134% of the nonfiction average.
   - **Sources:** Brysbaert 2019; Carver 1990, 1992.

5. **keeping-a-practice-log** — Keeping a Practice Log — *Reading your numbers*
   - **Drill:** the log itself: the reader reads their first entries in
     `log/history`, adds a note, and exports the log as text.
   - **Do:** read a practice log: sessions, baseline median, latest effective
     rate, and the change measured against the baseline range.
   - **Lab:** `log/history`. Presets are three example logs (shown when the
     reader's own log is empty, and labelled "example"): `starting`
     (3 baselines), `six-weeks` (3 baselines and 12 sessions trending up),
     `speed-only` (rate up, comprehension down: effective rate flat). Pins
     `lgSessions`, `lgBaseMedian`, `lgLatestErr`.
   - **Misconception:** "Practice that feels faster is faster." Felt speed and
     measured speed diverge; only the log, with comprehension in it, says
     whether the week's practice worked.
   - **Worked:** baselines 240, 238, 251 → median 240; latest effective 264 →
     change 24, inside or outside the range as computed.
   - **Sources:** —

### Course 2 — How the Eyes Read (`reading-how-the-eyes-read`, 6)

Modules: `Fixations and saccades`, `The limits`.

1. **fixations-and-saccades** — Fixations and Saccades — *Fixations and saccades*
   - **Drill:** the reader reads `P06` with the pacer off and then watches a
     replay of a typical eye-movement record of its first line (the kit
     draws fixation dots at the model's spacing; illustrative, labelled so).
   - **Do:** compute the time a reader spends per word from fixation duration,
     saccade duration and characters advanced per fixation.
   - **Lab:** `eye/budget`. Inputs: fixation ms, saccade ms, characters per
     forward saccade, regression share, characters per word (with the
     space). Presets: `typical` (225, 30, 8, 3/20, 6 → wpm ≈ 266.7; the
     author verifies against the formula in §D), `no-regressions` (same, 0 →
     60,000 / 191.25 ≈ 313.7), `long-fixations` (300, 30, 8, 3/20, 6). Pins `eyWpm`,
     `eyFixPerWord`.
   - **Misconception:** "The eyes glide smoothly along the line." Javal's 1879
     observation and every eye-tracking study since: the eyes jump and stop,
     and nearly all the reading happens in the stops.
   - **Worked:** fixations per word = 6 / (8 × 17/20) = 15/17; time per word
     = 15/17 × 255 ms = 225 ms; 60,000 / 225 = 266⅔ wpm.
   - **Sources:** Javal 1879 (via Huey 1908); Rayner 1998, 2009.

2. **the-perceptual-span** — The Perceptual Span — *Fixations and saccades*
   - **Drill:** `flash/span`: strings of letters flashed around a fixation
     mark for 150 ms (shorter than the time it takes to start a saccade), the
     reader types what they saw; scored by position, left and right of
     centre.
   - **Do:** compute accuracy by distance from fixation and say how far to
     each side letters are identified.
   - **Lab:** `flash/span`. Presets are typed results for given flashed
     strings: `typical` (9-letter strings, accuracy falling from 10/10 at
     centre to 3/10 at ±4), `wide-claim` (a reader who claims to see a whole
     line: the 21-letter flash scored position by position). Pins `flCentre`,
     `flEdge`, `flSpan` (positions with accuracy ≥ 1/2).
   - **Misconception:** "With training you can take in a whole line, or a
     page, in one glance." The span is asymmetric, about 3–4 characters left
     and 14–15 right in English, and words are identified only in about the
     first 7–8 characters to the right; acuity, not habit, sets it.
   - **Worked:** 7 of 10 correct at +3, 3 of 10 at +5: the identification span
     ends between them.
   - **Sources:** McConkie and Rayner 1975; Rayner 1998.

3. **looking-back** — Looking Back — *Fixations and saccades*
   - **Drill:** `drill/compare`: `P07` read normally; `P08` read with the
     `mask` display (text before the current line hidden as the pacer
     passes), both at the same target rate, five questions each.
   - **Do:** compute what blocking regressions did to comprehension at a
     fixed rate, and say what a regression is for.
   - **Lab:** `drill/compare`. Presets: `masked-costs` (A normal 300 wpm 5/5;
     B masked 300 wpm 3/5 → effective 300 vs 180), `masked-free` (A and B
     4/5). Pins `drErrA`, `drErrB`, `drErrDiff`.
   - **Misconception:** "Regressions are a bad habit to eliminate." Regressions
     are about 10–15% of saccades in skilled readers, and when Schotter,
     Tran and Rayner prevented them, comprehension fell; many are the eye
     going back to repair a misreading.
   - **Worked:** 300 × 3/5 = 180 against 300 × 5/5 = 300.
   - **Sources:** Rayner 1998; Schotter, Tran and Rayner 2014.

4. **the-speed-ceiling** — The Speed Ceiling — *The limits*
   - **Drill:** `eye/required`: the reader enters a claimed speed (their own
     goal, or an advertisement's) and the lab computes the characters per
     fixation it would need.
   - **Do:** compute the characters a fixation must cover for a claimed rate,
     compare it with the perceptual span, and classify the claim as reading,
     skimming or impossible as reading.
   - **Lab:** `eye/required`. Inputs: target wpm, fixation ms, saccade ms,
     characters per word, regression share (0 in every preset). Presets: `double` (500 wpm → ≈ 12.75 characters,
     inside the right span but beyond the identification span), `thousand`
     (1,000 → 25.5), `twenty-five-thousand` (25,000 → 637.5, about eight
     lines per fixation). Pins `eyNeeded`, `eyVerdict`.
   - **Misconception:** "Reading at 1,000 words a minute with full
     comprehension is a matter of technique." At 255 ms a fixation it needs
     25 characters identified per glance; what is done at such rates is
     skimming, which the Subject teaches as skimming.
   - **Worked:** 1,000 wpm × 6 chars × 255 ms / 60,000 = 25.5 characters per
     fixation.
   - **Sources:** Rayner et al. 2016; Just, Carpenter and Masson 1982.

5. **lines-and-return-sweeps** — Lines and Return Sweeps — *The limits*
   - **Drill:** `drill/compare` on `P09`/`P10` displayed in a narrow column
     (about 40 characters) and a wide one (about 90), same rate target.
   - **Do:** compute fixations per line and the share of time spent on return
     sweeps for two line lengths.
   - **Lab:** `eye/lines`. Inputs: characters per line, lines, characters per
     forward saccade, fixation and saccade ms, return-sweep ms (with its
     corrective fixation). Presets: `narrow` (40 chars), `wide` (90 chars),
     `newspaper` (30 chars). Pins `eyFixPerLine`, `eySweepShare`.
   - **Misconception:** "Narrow columns are faster because you read them
     straight down the middle." The eyes still fixate along a narrow line;
     what narrow columns change is the number of return sweeps, and the
     evidence on line length and speed is mixed (§S Dyson).
   - **Worked:** 40 / 8 = 5 fixations a line, plus one sweep: 1 in 6 eye
     movements is a sweep.
   - **Sources:** Rayner 1998; Dyson 2004.

6. **training-the-periphery** — Training the Periphery — *The limits*
   - **Drill:** `flash/schulte`: a 5×5 table of numbers to find in order while
     keeping the eyes on the centre; timed, three tables. Then the reader's
     next timed reading (`P11`) to see whether the table time and the
     reading rate move together across sessions (the log does this over
     weeks).
   - **Do:** compute a Schulte table time per cell and state what a faster
     table would and would not show about reading.
   - **Lab:** `flash/schulte`. Presets: `first` (25 cells in 62 s), `third`
     (25 in 41 s), each with a seeded table. Pins `flTime`, `flPerCell`.
   - **Misconception:** "Getting faster at eye exercises makes reading
     faster." Practice improves the practised task; transfer to reading
     rate is the claim to test, and the Subject's log is how the reader
     tests it.
   - **Worked:** 41 s / 25 = 1.64 s per cell, against 62 / 25 = 2.48.
   - **Sources:** Rayner et al. 2016 (training the visual span).

### Course 3 — Guided Practice (`reading-guided-practice`, 6)

Modules: `The pacer`, `Pushing the pace`.

1. **reading-with-a-pacer** — Reading with a Pacer — *The pacer*
   - **Drill:** `drill/compare`: `P12` at the reader's own pace; `P13` with the
     `pacer` display (a highlight moving line by line) at the reader's
     baseline rate.
   - **Do:** compute the pacer's time per line from a target rate and compare
     comprehension and effective rate with and without it.
   - **Lab:** `drill/compare`, B display `pacer` at 250 wpm. Presets:
     `steadier` (A 240 wpm 4/5; B 250 wpm 5/5), `no-difference` (both 4/5).
     Pins `drErrA`, `drErrB`, `drPacerLineMs` (ms per line of 12 words at
     250 wpm = 2,880).
   - **Misconception:** "A pacer works by forcing the eyes to move faster than
     they can." A pacer sets a steady pace and discourages drifting and
     re-reading for no reason; it does not widen what a fixation takes in.
   - **Worked:** 12 words × 60,000 / 250 = 2,880 ms per line.
   - **Sources:** Rayner et al. 2016; Wood (as the tradition's source).

2. **choosing-a-target-pace** — Choosing a Target Pace — *The pacer*
   - **Drill:** three pacer readings at baseline × 1, × 6/5 and × 3/2 on
     `P14`, `P15`, `P16`, five questions each.
   - **Do:** find the fastest pacer setting at which comprehension holds at
     4/5 or better, from three runs.
   - **Lab:** `drill/ladder` (three runs, each with its own target). Presets:
     `holds-at-120` (240 → 240/288/360 with 5/5, 4/5, 2/5 → best effective
     at 288), `holds-at-150`. Pins `drBestTarget`, `drBestErr`.
   - **Misconception:** "Set the pacer as fast as you can follow it." The
     setting to practise at is the fastest at which you still understand;
     beyond it, effective rate falls.
   - **Worked:** 288 × 4/5 = 230.4 > 360 × 2/5 = 144.
   - **Sources:** —

3. **sprints-above-comfort** — Sprints Above Comfort — *Pushing the pace*
   - **Drill:** the classic overload drill: a 1-minute sprint at about twice
     the reader's rate on `P17` with no questions (just keep moving), then a
     normal timed reading with questions on `P18`.
   - **Do:** compute the rate of a reading after a sprint and decide, from the
     baseline range, whether it is a change or noise.
   - **Lab:** `drill/compare`, A sprint (`pacer`, 2 × baseline, questions off),
     B `normal` with questions. Presets: `after-sprint` (B 268 wpm, 4/5 vs
     baseline range 238–251), `no-effect` (B 247). Pins `drWpmB`, `drErrB`,
     `drVerdictB` (against the baseline range typed in the panel).
   - **Misconception:** "After a sprint you read faster for good." The
     after-effect, where there is one, is a reading of a single passage; only
     a log over weeks tests whether the base rate moved.
   - **Worked:** 268 − 251 = 17 above the best baseline; the baseline range
     is 13, so it is outside — once.
   - **Sources:** —

4. **reading-in-phrases** — Reading in Phrases — *Pushing the pace*
   - **Drill:** `drill/compare`: `P19` normal; `P20` displayed in phrase
     chunks (one meaningful phrase at a time, centred, at the reader's rate).
   - **Do:** compute the chunk display's time per phrase and compare
     comprehension with normal reading at the same rate.
   - **Lab:** `drill/compare`, B display `phrases`. Presets: `chunks-help`
     and `chunks-hurt` (author designs). Pins `drErrA`, `drErrB`,
     `drPhraseMs` (mean ms per phrase).
   - **Misconception:** "Phrase reading means seeing several words in one
     fixation." Chunking groups words by meaning; the eyes still fixate most
     content words. What may help is the grouping, not a wider glance.
   - **Worked:** a 4-word phrase at 250 wpm: 4 × 60,000 / 250 = 960 ms.
   - **Sources:** Rayner et al. 2016.

5. **fewer-needless-regressions** — Fewer Needless Regressions — *Pushing the pace*
   - **Drill:** the masked pacer on `P21` at the reader's rate, then the
     unmasked pacer on `P22`; a self-count afterwards ("how many times did you
     want to look back?").
   - **Do:** separate needless re-reading (from drifting attention) from
     repair regressions, and compute the time a reader saves by cutting the
     first kind only.
   - **Lab:** `eye/budget` with regressions split: needless share and repair
     share. Presets: `drifting` (needless 1/10, repair 1/20), `focused`
     (needless 1/50, repair 1/20). Pins `eyWpm`, `eySaved`.
   - **Misconception:** "Every look back is wasted time." The cut that helps
     is to the regressions caused by inattention; the repair regressions
     carry comprehension (Looking Back).
   - **Worked:** from 3/20 total to 7/100 total: the formula in §D gives the
     rate before and after.
   - **Sources:** Schotter, Tran and Rayner 2014; Rayner et al. 2016.

6. **repeated-reading-and-transfer** — Repeated Reading and Transfer — *Pushing the pace*
   - **Drill:** `drill/repeat`: `P23` three times in a row, then the new
     passage `P24` once, all timed with questions on the last two.
   - **Do:** compute the gain on a repeated passage and the gain on a new one,
     and say which one is evidence of a faster reader.
   - **Lab:** `drill/repeat`. Presets: `practice-effect` (P23: 240, 300, 340;
     P24: 248), `transfer` (P24: 275). Pins `drRepeatGain`,
     `drTransferGain`.
   - **Misconception:** "The third reading shows my new speed." It shows that
     you know the passage; only the new passage tests the reader. Repeated
     reading is a fluency method for developing readers (Samuels 1979);
     for a skilled adult its gains are largely specific to the passage.
   - **Worked:** 340 − 240 = 100 on the repeated passage; 248 − 240 = 8 on
     the new one.
   - **Sources:** Samuels 1979; Therrien 2004.

### Course 4 — The Inner Voice and Flashing Words (`reading-inner-voice-and-flashing-words`, 5)

Modules: `The inner voice`, `Flashing words`.

1. **the-inner-voice** — The Inner Voice — *The inner voice*
   - **Drill:** `drill/compare`: `P25` read aloud (timed), `P26` read
     silently.
   - **Do:** compute oral and silent rates and the ratio between them, and
     explain why silent reading can exceed speaking rate even with an inner
     voice.
   - **Lab:** `drill/compare`, A `aloud` (no questions; the reader presses
     Done when they finish speaking), B `normal`. Presets: `typical` (A 183,
     B 238: Brysbaert's averages), `fast-silent` (A 180, B 320). Pins
     `drWpmA`, `drWpmB`, `drRatio`.
   - **Misconception:** "The inner voice limits you to speaking speed, so it
     must go." Silent reading is already faster than oral reading on
     average; inner speech is not full articulation.
   - **Worked:** 238 / 183 ≈ 1.30.
   - **Sources:** Brysbaert 2019; Rayner et al. 2016.

2. **silencing-the-inner-voice** — Silencing the Inner Voice — *The inner voice*
   - **Drill:** `drill/compare`: `P27` read normally; `P28` read while
     repeating "one-two-three" under the breath (articulatory suppression),
     both with questions. The pair is matched in band and length.
   - **Do:** compute the change in rate and comprehension under suppression
     and say what it implies for the advice to eliminate subvocalisation.
   - **Lab:** `drill/compare`. Presets: `typical` (A 245, 5/5; B 262, 3/5),
     `easy-text` (small drop). Pins `drErrA`, `drErrB`, `drErrDiff`.
   - **Misconception:** "Eliminating subvocalisation is the key to speed
     reading." When inner speech is suppressed, comprehension of anything
     but easy text suffers; the inner voice carries the sentence while it is
     being understood.
   - **Worked:** 245 × 5/5 = 245 vs 262 × 3/5 = 157.2.
   - **Sources:** Hardyck and Petrinovich 1970; Slowiaczek and Clifton 1980;
     Rayner et al. 2016.

3. **one-word-at-a-time** — One Word at a Time — *Flashing words*
   - **Drill:** `drill/single` with the `rsvp` display: `P29` flashed one word at
     a time at the reader's baseline rate, then questions.
   - **Do:** compute the time each word is shown at a given rate, and the
     total, and compare comprehension with the reader's normal baseline.
   - **Lab:** `drill/single`, display `rsvp`. Presets: `at-baseline` (250 wpm
     → 240 ms per word), `at-500` (120 ms), `at-1000` (60 ms). Pins
     `drWordMs`, `drWpm`, `drErr`.
   - **Misconception:** "Removing eye movements removes the time they take, so
     a flashed stream is free speed." The eye's travel was a small part of
     the time; identification and integration take the rest, and the stream
     gives no time back for either.
   - **Worked:** 60,000 / 250 = 240 ms per word.
   - **Sources:** Potter 1984; Rayner et al. 2016; Benedetto et al. 2015.

4. **rsvp-without-looking-back** — Flashing Words Without Looking Back — *Flashing words*
   - **Drill:** `drill/compare` at the same rate: `P30` `normal` (paced),
     `P31` `rsvp`. Both texts carry one garden-path sentence each, which a
     question targets.
   - **Do:** compute comprehension in both displays at one rate and connect
     the garden-path question's result to regressions.
   - **Lab:** `drill/compare`. Presets: `stream-loses` (A 5/5, B 3/5),
     `even` (A 4/5, B 4/5). Pins `drErrA`, `drErrB`.
   - **Misconception:** "RSVP is reading with the waste removed." The stream
     removes regressions too; Schotter, Tran and Rayner's ambiguous
     sentences are where that costs.
   - **Worked:** same 300 wpm: 300 × 5/5 vs 300 × 3/5.
   - **Sources:** Schotter, Tran and Rayner 2014; Acklin and Papesh 2017.

5. **testing-a-speed-claim** — Testing a Speed Claim — *Flashing words*
   - **Drill:** the reader takes an advertised claim (presets carry three
     typical ones, worded as claims and attributed to no product) and runs
     it through the eye budget and the effective rate; then does a 1-minute
     reading at the claimed pace to feel it.
   - **Do:** test a speed-reading claim with three computations — characters
     per fixation, effective rate at a plausible comprehension, and the
     book-length time it implies — and state what evidence would settle it.
   - **Lab:** `eye/required` with a claim panel. Presets: `triple-speed`
     (750), `a-novel-an-hour` (90,000 words in 60 minutes → 1,500 wpm),
     `whole-page` (a page of 350 words per 2-second glance). Pins
     `eyNeeded`, `eyVerdict`.
   - **Misconception:** "A claim with a testimonial is a measured claim." The
     Just, Carpenter and Masson comparison of trained speed readers, normal
     readers and skimmers is the model of a test; the lesson tells that
     story (and Woody Allen's line about *War and Peace*, at most once).
   - **Worked:** 90,000 words / 60 min = 1,500 wpm → 1,500 × 6 × 255 / 60,000
     = 38.25 characters per fixation.
   - **Sources:** Just, Carpenter and Masson 1982; Carver 1985; Rayner et al.
     2016.

### Course 5 — Skimming, Scanning and Previewing (`reading-skim-scan-and-preview`, 7)

Modules: `Scanning and skimming`, `Reading strategically`.

1. **scanning-for-a-target** — Scanning for a Target — *Scanning and skimming*
   - **Drill:** `scan/find`: a long text (`S01`, a schedule-like or
     index-like document, ~600 words) and five targets ("the date the second
     ferry leaves"); the reader clicks the word that answers each; timed per
     target.
   - **Do:** compute seconds per target and words passed over per second, and
     say why scanning is fast.
   - **Lab:** `scan/find`. Presets: `quick` (5 found in 40 s), `slow-reader`
     (5 in 95 s, 1 wrong). Pins `scFound`, `scPerTarget`, `scWordsPerSec`.
   - **Misconception:** "Scanning is fast reading." Scanning is a search for
     a known form — a number, a name — and not reading at all; its speed
     says nothing about reading rate.
   - **Worked:** 600 words / 40 s = 15 words per second = 900 words per
     minute passed over.
   - **Sources:** Carver 1990 (scanning gear).

2. **skimming-for-gist** — Skimming for Gist — *Scanning and skimming*
   - **Drill:** `drill/single` with the `gist` display: `P32` shown as first
     sentences of each paragraph plus headings, for a limit of one third of
     its full reading time; then gist questions (main points, not details).
   - **Do:** compute the share of the text a skim shows and the gist score
     per minute, and compare with the full reading's.
   - **Lab:** `drill/single`, display `gist`. Presets: `first-sentences`
     (words shown 112 of 560 → 1/5; 3 of 4 gist questions in 40 s),
     `full-read` (560 words in 140 s, 4/4). Pins `drShown`, `drErr`.
   - **Misconception:** "First sentences always carry the point." They often
     do in exposition written to a plan, and the passages show where they
     do not; skimming is a bet on the text's structure.
   - **Worked:** 112 / 560 = 1/5 of the words.
   - **Sources:** Masson 1982; Duggan and Payne 2009.

3. **what-skimming-costs** — What Skimming Costs — *Scanning and skimming*
   - **Drill:** `drill/compare`: `P33` skimmed with a time limit, `P34` read
     in full; each with five questions, two gist and three detail.
   - **Do:** compute gist and detail comprehension separately for a skim and
     a full reading, and choose between them for a stated purpose.
   - **Lab:** `drill/compare` with question types. Presets: `typical` (skim:
     2/2 gist, 1/3 detail; read: 2/2, 3/3). Pins `drGistA`, `drDetailA`,
     `drGistB`, `drDetailB`.
   - **Misconception:** "A skim is a fast read with a little less
     understanding." It is a different reading: gist holds, detail goes.
   - **Worked:** detail 1/3 vs 3/3; gist 2/2 both.
   - **Sources:** Masson 1982; Just, Carpenter and Masson 1982; Duggan and
     Payne 2009.

4. **previewing-before-reading** — Previewing Before Reading — *Scanning and skimming*
   - **Drill:** `drill/compare`: `P35` read cold; `P36` previewed for 30
     seconds (headings, first and last paragraph) then read, both timed in
     total with questions.
   - **Do:** compute the effective rate including preview time and decide
     whether the preview paid for itself.
   - **Lab:** `drill/compare`, B display `preview`. Presets: `pays`, `does-not`
     (author designs; the total time includes the 30 s). Pins `drErrA`,
     `drErrB`.
   - **Misconception:** "A preview is free." It costs time; it pays only when
     it raises comprehension or lets you skip a section.
   - **Worked:** (preview 30 s + read 110 s) for 480 words → 480 × 60 / 140
     ≈ 205.7 wpm, × 5/5.
   - **Sources:** Robinson 1946 (SQ3R); Adler and Van Doren 1972.

5. **inspectional-reading** — Inspectional Reading — *Reading strategically*
   - **Drill:** a book-shaped document (`B01`: title page, contents, preface
     and index of an imaginary book, written for the course) inspected in a
     time limit, then questions about what the book is and where things are.
   - **Do:** answer, from a 5-minute inspection, what a book is about, how it
     is organised, and where a named topic is treated.
   - **Lab:** `scan/inspect`. Presets: `five-minutes`. Pins `scFound`,
     `scPerTarget`.
   - **Misconception:** "Reading a book means reading it from the first page."
     Adler's inspectional reading comes first, and decides whether the book
     needs a whole reading at all.
   - **Worked:** 4 of 5 structural questions answered in 300 s.
   - **Sources:** Adler and Van Doren 1972.

6. **triaging-a-reading-list** — Triaging a Reading List — *Reading strategically*
   - **Drill:** `triage/plan`: a stack of eight documents with word counts and
     a stated purpose; the reader assigns read, skim or skip to each and the
     lab computes the time and the share of the value covered.
   - **Do:** plan a reading session under a time budget and compute the time
     and coverage of the plan.
   - **Lab:** `triage/plan`. Presets: `read-everything` (over budget),
     `skim-the-rest` (fits), `skip-wrong` (fits, misses the important one).
     Pins `trMinutes`, `trCovered`, `trFits`.
   - **Misconception:** "The fastest way through a pile is to read faster."
     Choosing what not to read saves more time than any rate gain.
   - **Worked:** 12,000 words at 250 wpm = 48 min; skimming three of them at
     750 wpm (shown words 1/5) saves the difference.
   - **Sources:** Carver 1990; Duggan and Payne 2009.

7. **shifting-gears** — Shifting Gears — *Reading strategically*
   - **Drill:** one document (`P37`, a long passage with an easy narrative
     section and a dense technical section), read with the instruction to
     change speed by section; the drill records time per section.
   - **Do:** compute the rate for each section and say whether the reader
     shifted gear to match difficulty and purpose.
   - **Lab:** `drill/sections`. Presets: `flexible` (narrative 310, dense
     190), `rigid` (250, 245 with 2/5 on the dense questions). Pins
     `drRateS1`, `drRateS2`, `drErr`.
   - **Misconception:** "A good reader holds one fast speed." Skilled readers
     slow down for difficulty and speed up for familiarity; Carver called
     the capacity to shift gears the mark of a flexible reader.
   - **Worked:** 300 words in 58 s ≈ 310 wpm; 300 words in 95 s ≈ 189.5.
   - **Sources:** Carver 1990.

### Course 6 — Words, Knowledge and Difficulty (`reading-words-knowledge-and-difficulty`, 5)

Modules: `Difficulty`, `Knowledge`.

1. **measuring-difficulty** — Measuring Difficulty — *Difficulty*
   - **Drill:** `text/readability` on three passages of the bank (an easy, a
     standard and a hard one), then the reader's own rates on them from the
     log, if they have them.
   - **Do:** compute Flesch Reading Ease and Flesch–Kincaid grade from counts
     of words, sentences and syllables, and say what the formulas cannot
     see.
   - **Lab:** `text/readability`. Presets are three bank passages (one per
     band); the kit counts words and sentences and syllables by the stated
     rule (§D). Pins `txWords`, `txSentences`, `txFre`, `txGrade`.
   - **Misconception:** "A readability score measures how hard a text is to
     understand." It measures sentence length and word length; a short-word
     text of unfamiliar ideas scores easy.
   - **Worked:** 100 words, 5 sentences, 140 syllables → 206.835 − 1.015 × 20
     − 84.6 × 1.4 = 68.095.
   - **Sources:** Flesch 1948; Kincaid et al. 1975.

2. **your-rate-on-hard-text** — Your Rate on Hard Text — *Difficulty*
   - **Drill:** `drill/compare`: `P38` (easy band) and `P39` (hard band),
     each timed with questions.
   - **Do:** compute the change in rate and effective rate between an easy and
     a hard text and decide which number a speed claim should be measured
     on.
   - **Lab:** `drill/compare`. Presets: `typical` (easy 290, 5/5; hard 170,
     4/5). Pins `drWpmA`, `drWpmB`, `drRatio`.
   - **Misconception:** "My reading speed is one number." It is a number per
     kind of text; a speed claim measured on easy text says little about a
     contract or a textbook.
   - **Worked:** 170 / 290 = 17/29 ≈ 59%.
   - **Sources:** Carver 1990; Rayner et al. 2016.

3. **unknown-words-and-coverage** — Unknown Words and Coverage — *Knowledge*
   - **Drill:** `text/coverage`: the reader marks the words they do not know
     in `P40` (a hard-band passage), and the lab computes coverage.
   - **Do:** compute lexical coverage and the run of known words between
     unknown ones, and compare with the 98% threshold.
   - **Lab:** `text/coverage`. Inputs: tokens, unknown tokens. Presets:
     `ninety-eight` (500 tokens, 10 unknown → 98%, one in 50), `ninety-five`
     (25 unknown → one in 20), `ninety` (50). Pins `txCoverage`, `txRun`.
   - **Misconception:** "One unknown word in twenty is fine; you get it from
     context." At 95% coverage most readers do not understand a text
     adequately; Hu and Nation put the threshold for unassisted reading near
     98%.
   - **Worked:** 490 / 500 = 49/50 = 98%; one unknown word every 50 tokens.
   - **Sources:** Hu and Nation 2000; Nation 2006.

4. **what-you-already-know** — What You Already Know — *Knowledge*
   - **Drill:** `drill/compare`: `P41` on a topic the reader is likely to know
     (everyday life) and `P42` on an unfamiliar specialist topic, matched for
     readability score.
   - **Do:** compute the effect of topic familiarity on rate and
     comprehension with readability held equal.
   - **Lab:** `drill/compare`. Presets: `typical`, `expert` (reader expert in
     B's topic; author designs). Pins `drErrA`, `drErrB`, `drRatio`.
   - **Misconception:** "Speed is a skill independent of what you know."
     Background knowledge is one of the strongest predictors of
     comprehension (Recht and Leslie's baseball study); fast readers of a
     field are mostly readers who know the field.
   - **Worked:** effective 260 vs 150: ratio 15/26 ≈ 58%.
   - **Sources:** Recht and Leslie 1988; Rayner et al. 2016.

5. **how-much-you-read** — How Much You Read — *Knowledge*
   - **Drill:** `text/volume`: the reader enters minutes per day and their
     rate; the lab computes words and books a year and the new words met.
   - **Do:** compute annual reading volume from minutes a day and a rate, and
     compare what a rate gain and a time gain each add.
   - **Lab:** `text/volume`. Presets: `twenty-minutes` (20 min × 250 wpm ×
     365 = 1,825,000 words ≈ 20 books of 90,000), `faster` (20 min × 300),
     `longer` (30 min × 250). Pins `txWordsYear`, `txBooksYear`.
   - **Misconception:** "The way to read more is to read faster." Ten more
     minutes a day adds more than any plausible rate gain, and the volume is
     itself what grows vocabulary and knowledge.
   - **Worked:** 30 × 250 × 365 = 2,737,500 vs 20 × 300 × 365 = 2,190,000.
   - **Sources:** Anderson, Wilson and Fielding 1988; Nagy and Herman 1987.

### Course 7 — Remembering What You Read (`reading-remembering-what-you-read`, 4)

Modules: `Recall`, `Keeping it`.

1. **free-recall** — Free Recall — *Recall*
   - **Drill:** `recall/free`: `P43` timed, then the passage hides and the
     reader writes everything they remember; then the lab shows the
     passage's idea units and the reader ticks the ones they recalled.
   - **Do:** compute the share of idea units recalled and a recall-adjusted
     rate, and compare with multiple-choice comprehension.
   - **Lab:** `recall/free`. Presets: `typical` (12 idea units, 7 recalled;
     400 words in 100 s → 240 × 7/12 = 140). Pins `reRecall`, `reRate`.
   - **Misconception:** "Recognising the right answer is remembering."
     Multiple choice measures recognition; free recall is harder and closer
     to what you can use later.
   - **Worked:** 7/12 of 240 = 140 recalled-idea words per minute.
   - **Sources:** Roediger and Karpicke 2006 (method).

2. **retrieval-beats-rereading** — Retrieval Beats Rereading — *Recall*
   - **Drill:** `recall/delayed`: two passages, `P44` read twice, `P45` read
     once and then recalled; the lab stores both and asks the questions
     again when the reader returns two or more days later (the log keeps the
     due date).
   - **Do:** compute immediate and delayed scores for rereading and for
     retrieval, and the percentage of each kept.
   - **Lab:** `recall/delayed`. Presets: `typical-delay` (reread: 5/5 then 2/5;
     retrieve: 4/5 then 3/5 — the shape of Roediger and Karpicke's result, in
     the lesson's own numbers, labelled illustrative). Pins `reKeptA`,
     `reKeptB`.
   - **Misconception:** "Reading it again is the best way to remember it."
     Rereading wins on the immediate test and loses on the delayed one.
   - **Worked:** reread 2/5 ÷ 5/5 = 40% kept; retrieval 3/5 ÷ 4/5 = 75% kept.
   - **Sources:** Roediger and Karpicke 2006.

3. **spacing-your-reviews** — Spacing Your Reviews — *Keeping it*
   - **Drill:** `recall/schedule`: the reader plans reviews of a chapter's
     notes; the lab computes dates, total reviews and the minutes they cost.
   - **Do:** compute an expanding review schedule and its total time, and
     compare it with massed review.
   - **Lab:** `recall/schedule`. Inputs: first gap in days, multiplier,
     reviews, minutes each. Presets: `expanding` (1, ×2, 5 reviews → days 1,
     3, 7, 15, 31), `massed` (5 reviews on day 1). Pins `reLastDay`,
     `reMinutes`.
   - **Misconception:** "Cramming and spacing cost the same, so it doesn't
     matter when." Same minutes, different retention; Cepeda and colleagues'
     meta-analysis is the evidence.
   - **Worked:** gaps 1, 2, 4, 8, 16 → review days 1, 3, 7, 15, 31.
   - **Sources:** Ebbinghaus 1885; Cepeda et al. 2006.

4. **notes-in-your-own-words** — Notes in Your Own Words — *Keeping it*
   - **Drill:** `recall/free` on `P46`, this time writing a three-sentence
     summary instead of free recall, then ticking idea units covered.
   - **Do:** compute the idea units a short summary covers and the words per
     idea unit, and say what a good summary leaves out.
   - **Lab:** `recall/free`, summary variant. Presets: `tight` (40 words, 6
     units), `copied` (90 words, 4 units). Pins `reRecall`, `reWordsPerUnit`.
   - **Misconception:** "Highlighting is note-taking." Highlighting selects
     without transforming; summarising forces retrieval and selection
     (Dunlosky and colleagues rate highlighting low and summarising
     moderate).
   - **Worked:** 40 / 6 ≈ 6.7 words per unit vs 90 / 4 = 22.5.
   - **Sources:** Dunlosky et al. 2013.

### Course 8 — Your Training Plan (`reading-your-training-plan`, 4)

Modules: `The plan`, `The test`.

1. **a-practice-week** — A Practice Week — *The plan*
   - **Drill:** `log/plan`: the reader builds a week from the Subject's drills
     (minutes per session, sessions per drill type) and commits to it; the
     lab computes the week's minutes and the share per kind of practice.
   - **Do:** design a week of practice under a time budget, with a test
     reading on fresh text at its end.
   - **Lab:** `log/plan`. Presets: `twenty-a-day`, `weekend-only`,
     `all-sprints` (the unbalanced plan). Pins `lgWeekMinutes`,
     `lgTestShare`.
   - **Misconception:** "More drills means more progress." The test that
     matters is a fresh passage with questions; a week without one has not
     measured anything.
   - **Worked:** 5 × 20 + 2 × 30 = 160 minutes; the test is 10 of them.
   - **Sources:** —

2. **reading-your-curve** — Reading Your Curve — *The plan*
   - **Drill:** `log/history` on the reader's own log (or the example logs).
   - **Do:** decide from a log whether effective rate has changed, using the
     baseline range and the last three sessions' median.
   - **Lab:** `log/history` with the trend view. Presets: `real-gain`,
     `noise`, `rate-only` (rate up, comprehension down). Pins
     `lgBaseMedian`, `lgRecentMedian`, `lgVerdict`.
   - **Misconception:** "My best session is my new level." The median of the
     last three against the baseline range is the honest comparison; the
     best session is selected for being high.
   - **Worked:** baseline 238–251 (median 245), recent 262, 270, 281 →
     median 270; 270 − 251 = 19 above the top of the range.
   - **Sources:** —

3. **plateaus-and-transfer** — Plateaus and Transfer — *The test*
   - **Drill:** a transfer test: one passage of a kind the reader never
     practised on (`P47`, a dense argument), timed with questions.
   - **Do:** compute the gain on practised passages and on a new kind, and
     say what a plateau in each would mean.
   - **Lab:** `drill/compare`, A practised band, B new kind. Presets:
     `transfers`, `does-not`. Pins `drErrA`, `drErrB`, `drRatio`.
   - **Misconception:** "A plateau means I have reached my limit." It often
     means the practice has stopped asking for more, or that the gains so
     far were specific to the practice material; a new kind of text tells
     which.
   - **Worked:** gain 30 on practised, 4 on new: specific, not general.
   - **Sources:** Ericsson, Krampe and Tesch-Römer 1993 (deliberate
     practice); Rayner et al. 2016.

4. **the-full-battery** — The Full Battery — *The test*
   - **Drill:** the capstone: a fresh standard passage (`P48`) at the usual
     pace with questions, a skim of `P49`, a scan of `S02`, and a free recall
     of `P48` — all logged — then the log's comparison with the reader's
     first baselines.
   - **Do:** compute a profile — effective rate, skim gist score, scan time per
     target, recall share — and compare each with the first measurement.
   - **Lab:** `log/profile`. Presets: `starting-profile`, `after-practice`.
     Pins `lgErrNow`, `lgErrThen`, `lgVerdict`.
   - **Misconception:** "One number sums up a reader." A reader is a profile:
     rate on a kind of text, comprehension, the choice of when not to read
     everything, and what is kept.
   - **Worked:** effective 244 → 268, inside or outside the baseline range.
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
  "questions": [               # exactly 5 (4 for gist-only passages)
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
4. **Questions** cannot be answered from general knowledge: before a question
   is kept, its author answers it without the passage, and if the right
   option is guessable, it is rewritten (Rayner et al. 2016 make this point
   about speed-reading tests). Exactly one defensible answer; distractors
   are plausible and appear in or near the text. At least two `gist` and two
   `detail` questions per passage. The correct index is rotated.
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

`measuring-difficulty` reuses one passage per band from the bank for counting
only (no drill), which is the one exception to rule 5.

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

A lesson's lab cfg names passages by id (`"passage": "P01"`, `"passages":
["P07", "P08"]`); the kit resolves them from `content.reading.passages` at
build time and embeds only those. Course fields and lesson fields are exactly
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
  only where it explains something: Javal watching eyes jump in 1879; Huey's
  1908 book; Evelyn Wood's courses from 1959 and the claims made for them;
  Woody Allen's line about *War and Peace*; the 2014 apps; Rayner and his
  colleagues' 2016 review.
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
> most people told to go as fast as they can, it is, often by half again —
> look next at the questions. The usual result is a rate that went up and a
> score that went down, and the question that matters is what happened to
> their product. Four hundred words at 480 words a minute with two questions
> in five right is, in understood words per minute, worse than the same
> length at 240 with all five: 192 against 240. That product is the effective
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
  learning techniques. *Psychological Science in the Public Interest* 14(1).
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
