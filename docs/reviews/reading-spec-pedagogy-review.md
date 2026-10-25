# Pre-authoring pedagogy review: Reading Faster (`docs/reading/PLAN.md`)

Reviewed 2026-10-24 on branch `feat/reading-subject`, against the
`pedagogical-expert` brief (observable objectives, prerequisite order, cognitive
load, worked-example progression, retrieval practice, misconceptions) and the
operator's one instruction for this Subject: "the most important thing is
exercising". Nothing has been authored; this judges the specification. Written
independently of the accuracy review; where a finding touches a figure it is
flagged for that review rather than settled here.

## Verdict

The specification is unusually well built as a set of **experiments**: every
compare lesson has a control condition, every figure is a reader's own
measurement, the effective rate is reported beside every rate, and Course 1
teaches the noise in a single reading before any technique is tried. That is a
better foundation than most published speed-reading material has. But it is
not yet a **training** Subject. Forty-nine passages are each assigned to one
lesson and may never be reread, so once the reader has done a lesson's drill
there is nothing fresh to practise on; about a dozen lessons' labs are
calculators with no timed reading at all (contradicting §0's "every lesson is
built around a drill"); the practice routine arrives in lesson 39 of 42; and the
log, which is meant to show whether practice worked, would mix sprints, masked
readings, RSVP at 1,000 wpm and articulatory suppression into the same curve as
natural readings. There are also two prerequisite breaks (the pacer and the
mask display are used in Course 2 but taught in Course 3), one tile whose
definition contradicts its lesson's objective (`drBestTarget`), one experiment
whose design defeats its own point (`retrieval-beats-rereading` gives the
reread condition an immediate test), and a decision rule in Course 1 ("outside
the baseline range") that fires by chance one time in four. All of these are
fixable in the specification, most without changing the lesson count. The
recommendation is **revise before authoring**, with findings 1–8 blocking.

## Findings

### A. Is practice central? Dosage, routine, fresh text

**1. There is no fresh text to practise on.** *Where:* §P rule 5 ("no passage
is used in two lessons' drills"), Course 1 `how_to` ("do not practise on a
passage you have already read"), §E per-lesson procedure 3 ("the `steps` are
the exercise protocol — what to do when you repeat the drill on another day").
*What is wrong:* every one of the 49 texts is consumed by its lesson's drill;
the `steps` tell the reader to repeat the drill on another day, and there is
nothing to repeat it on. The Subject can measure, but it cannot be trained on.
*Change:* add an unassigned **practice pool** to §P — `Q01`–`Q24` at least, 350–500
words, five (or six, see finding 14) questions each, about two thirds standard
band and one third hard, with `kind` spread across the four kinds — served in a
fixed order by a new `drill/practice` view that reads the log and offers the
first pool passage the reader has not logged. Twenty-four is a floor: at one
session a day it lasts five weeks. State the pool's size in the tagline's
neighbourhood only if the counts test tolerates it. *Priority: high.*

**2. The reader's own text should be a practice source.** *Where:* §D.1
`drill/single`; §G. *What is weak:* the only place a reader will go on reading
faster is their own material, and the kit cannot time it. *Change:* give
`drill/single` and `drill/practice` an `own text` option: a textarea the reader
pastes into, counted by the kit's word rule, displayed `normal` or `pacer`,
timed, logged with `total` 0 and `kind: practice`. It is self-contained (nothing
leaves the browser), costs nothing in passages, and is where transfer to real
reading is most likely. The panel says a reading without questions is a rate,
not an effective rate. *Priority: medium-high.*

**3. The routine arrives too late and is not specified.** *Where:*
`a-practice-week` (Course 8, lesson 39). *What is wrong:* a reader following
the Subject one lesson a day practises nothing between lessons for five weeks,
then is asked to design a week. The library's own order — worked example, faded
guidance, independent practice — puts independent practice after the pacer is
learned, not at the end. *Change:* (a) add a lesson **`the-daily-drill`** —
"The Daily Drill" — directly after `choosing-a-target-pace`, whose lab is
`drill/practice` and whose body hands the reader the routine the Subject wants
followed from then on; (b) every later lesson's last `step` says "then today's
Daily Drill" with the link; (c) `a-practice-week` keeps its planning lab but
becomes a review of the routine the reader has kept, not its introduction.
The routine itself, as the specification should state it so the author does
not invent one: ten to fifteen minutes a day; one pool passage with the pacer
at the reader's *hold* target (the fastest setting at which the last three
practice readings scored at least 4/5); every fifth session is a **test** —
a pool passage at the reader's natural pace, no pacer, questions on, logged as
`kind: test`; raise the target by about 5% when three practice readings in a
row hold, lower it by the same when two fail; never more than two timed
readings in a sitting after the first week's novelty wears off. The numbers are
the author's to adjust, but a rule for raising the target, a rule for testing,
and a session length must be in the lesson. *Priority: high.*

**4. The log cannot tell a natural reading from an experimental condition.**
*Where:* §D.0 "The log" (`kind?` is optional and undefined); `log/history`
(`lgRecentMedian` = last three entries); `reading-your-curve`; `the-full-battery`.
*What is wrong:* the last three sessions before the reader opens
`reading-your-curve` may be a skim, an RSVP run at 500 wpm and a suppression
reading. A curve of effective rate over those is noise by construction, and
the Subject's central promise — "what you learn about reading speed is
measured on your own reading" — rests on that curve. *Change:* make `kind`
required with values `baseline | test | practice | condition | other`, set by
the view's cfg (every compare side that is not `normal` at natural pace is
`condition`; `P03` "as fast as you can" is `condition`); `log/history`,
`log/noise` and `log/profile` compute medians and verdicts over `baseline` and
`test` only, draw `practice` as a lighter series, and leave `condition` out of
the chart (listed in the export). *Priority: high.*

**5. Twelve lessons have no timed reading, so "every lesson is built around a
drill" is false as specified.** *Where:* `typical-rates-and-reading-gears`,
`keeping-a-practice-log`, `fixations-and-saccades` (the reading is unscored
and the lab is a calculator), `the-speed-ceiling`, `lines-and-return-sweeps`,
`fewer-needless-regressions` (lab is `eye/budget`), `testing-a-speed-claim`,
`triaging-a-reading-list`, `measuring-difficulty`, `how-much-you-read`,
`spacing-your-reviews`, `a-practice-week`, `reading-your-curve`. *Change:*
within one lab per lesson, give the kit a cfg key `warmup: PASSAGES["Qnn"]`
(or a pool draw) that any calculator view may carry: a Start → Done → questions
→ Score reading, logged as `practice`, shown above the calculator panel. Then
every lesson does give the reader a reading, the pool (finding 1) supplies the
text, and §0's sentence becomes true. Where a lesson's calculator *is* the
point (gears, volume, schedule), the warm-up also gives the panel a live number
to compute on. *Priority: high.*

**6. Fatigue and session length are nowhere stated.** *Where:*
`choosing-a-target-pace` (three readings and fifteen questions),
`repeated-reading-and-transfer` (four readings), `the-full-battery` (four
tasks), Course 1 overall (five readings in three lessons). *Change:* each §C
entry states its expected minutes; the `how_to` of each course says the
longest lessons are to be done in one sitting but not after another drill; the
battery's body says it is a fifteen-minute sitting and should be done fresh.
*Priority: low.*

**7. Progressive difficulty is absent from practice.** *Where:* §P assignments
(every drill passage through Course 5 is `standard`); no lesson raises length or
band as training. *Change:* order the practice pool so that its second half is
`hard` band and 500–650 words, and have `drill/practice` say when the reader
crosses into it; `the-daily-drill`'s body says that a hold target should be
re-found on hard text (it will be lower), which also previews
`your-rate-on-hard-text`. *Priority: medium.*

### B. Objectives, misconceptions, worked examples

**8. `drBestTarget` contradicts its lesson's objective, and the preset's own
numbers show it.** *Where:* `choosing-a-target-pace`; §D.1 `ladder`. *What is
wrong:* the Do is "the fastest pacer setting at which comprehension holds at
4/5 or better"; the tile is defined as "the run with the highest effective
rate". Preset `holds-at-120` is 240 at 5/5 (effective 240), 288 at 4/5
(230.4), 360 at 2/5 (144): the highest effective rate is 240, so the tile
would name the baseline target while the preset's name and the worked line
("288 × 4/5 = 230.4 > 360 × 2/5 = 144") say 288. *Change:* define
`drBestTarget` as the fastest target whose comprehension is at least a cfg
threshold `hold` (4/5), printed with its effective rate; show the three
effective rates as tiles so the reader also sees the trade; keep the preset
numbers. This is also the rule the Daily Drill (finding 3) uses, so the two
must agree. *Priority: high.*

**9. The first baseline has no comprehension score, so the baseline median is
undefined.** *Where:* `words-per-minute` (questions off), `one-reading-is-one-measurement`
("with `words-per-minute`'s these are the reader's three baselines"),
`log/history` (`lgBaseMedian` = median of the first three *effective* rates).
*Change:* keep `words-per-minute`'s explanation about rate only, but score
`P01`'s questions too (the body simply does not discuss them until the next
lesson), and log it `baseline`; or define the three baselines as `P02`, `P04`,
`P05` and exclude `P03` by `kind`. The first is cleaner. *Priority: high.*

**10. "Outside the baseline range" is weak evidence and the Subject treats it
as the test.** *Where:* `one-reading-is-one-measurement` (`lgVerdict`),
`sprints-above-comfort` (`drVerdictB`), `the-full-battery`. *What is wrong:* a
fourth reading drawn from the same distribution as three baselines falls above
their maximum one time in four, by order statistics alone; a Subject whose
material clause is "one measurement is not your reading speed" should not
hand the reader a one-in-four false positive as its verdict sentence.
`reading-your-curve` already has the better rule (median of the last three
tests against the range). *Change:* in Course 1, state the one-in-four fact in
a sentence and make the verdict two-tiered: "outside the baseline range —
once; three tests in a row outside it would be evidence"; make the median-of-
three rule the Subject's rule from `keeping-a-practice-log` on, and have
`log/noise` accept more than three baselines (every `test` entry widens the
reference set over time). *Priority: high.*

**11. Bare preset ids the plan's own rule says a reviewer must reject.**
*Where:* `fixations-and-saccades` `long-fixations` (no result);
`lines-and-return-sweeps` all three; `choosing-a-target-pace` `holds-at-150`;
`reading-in-phrases` both; `fewer-needless-regressions` worked line ("the
formula in §D gives the rate before and after"); `previewing-before-reading`
both; `inspectional-reading` `five-minutes`; `what-you-already-know` both;
`plateaus-and-transfer` both; `the-full-battery` both. *Change:* write the
instances before authoring, as §C's preamble requires; the accuracy review
should then recompute them. For `fewer-needless-regressions`, the numbers are
immediate from §D: 3/20 → 7/100 at 225/30/8/6 gives 266⅔ → ≈ 289.7 wpm
(fixations per word 0.75 / 0.93), which the author should verify.
*Priority: medium (blocking for authoring of those lessons).*

**12. The §C format has no `Standard` line, so the thing that measures the
objective is unspecified.** *Where:* §C format; every entry. *What is wrong:*
the brief judges each Do "as measured by the standard"; the author will invent
42 standards without a contract. *Change:* add a one-line **Standard:** to the
format and each entry, naming the act and the pass level, e.g. for
`comprehension-and-effective-rate`: "given two readings' words, seconds and
scores, you compute both effective rates and name the one that delivered more
understood words per minute, without the lab". *Priority: medium.*

**13. Misconceptions that are not ones readers hold, or are the wrong one for
the slot.**
- `spacing-your-reviews`: "Cramming and spacing cost the same, so it doesn't
  matter when" — nobody says this. The real wrong model is that massed review
  *feels* more effective because performance during the session is higher
  (the fluency illusion). Reword.
- `words-per-minute`: "A rate counted in words is comparable across texts" is a
  specialist's point for lesson 1. Keep it in `mistakes[1]`, and make
  `mistakes[0]` the one readers arrive with: "Average adults read about 300
  wpm and I am slow" (Brysbaert's 238 nonfiction is the correction; the
  accuracy review confirms the figure).
- `fixations-and-saccades`: "The eyes glide smoothly along the line" is real
  and good, but the drill (watch a replay) gives the reader no way to
  discover it. Add the oldest demonstration there is: watch a partner's eyes
  while they read a line, or your own in a mirror — one `step`, no kit needed.
*Priority: medium.*

**14. Five questions give comprehension steps of 20 points, which is coarser
than most effects the compare lessons look for.** *Where:* §P rule 4
("exactly 5"), every `drill/compare` preset (`masked-costs` 5/5 vs 3/5,
`steadier` 4/5 vs 5/5). *What is wrong:* one guessed answer is a 20-point swing
and a 48-wpm swing in effective rate at 240; a difference of one question is
inside noise, and no view says so. *Change:* six questions per drill passage
(three gist, three detail; steps of 16⅔ and a clean 2/3 split for
`what-skimming-costs`), and in every compare panel a fixed sentence: "one
question is N points; a one-question difference is not a result". If six is
too costly to author, keep five and the sentence is mandatory.
*Priority: medium-high.*

**15. Worked examples are well chosen but two illustrate the wrong quantity.**
- `skimming-for-gist`: `drErr` for a gist display is ambiguous — 560 words in
  40 s is 840 "wpm", × 3/4 = 630, which would make a skim look like a
  triumph beside the full read's 240. Define a separate tile `drGistPerMin`
  (gist questions right per minute) and do not print `drErr` for `gist`.
- `the-full-battery`'s worked line "effective 244 → 268, inside or outside
  the baseline range" is a one-against-three comparison the Subject has just
  taught to distrust (finding 10). Work the median-of-three instead.
*Priority: medium.*

### C. Order and load

**16. Prerequisite break: the pacer and the mask are used before they are
taught.** *Where:* `looking-back` (Course 2.3: "both at the same target rate",
`mask` display) and `lines-and-return-sweeps` (2.5: "same rate target") use the
pacer; `reading-with-a-pacer` is Course 3.1. The reader meets a moving
highlight and a disappearing text for the first time in an experiment that
depends on their following it steadily. *Change:* see finding 17; failing that,
move `looking-back` to Course 3 after `reading-with-a-pacer` and before
`fewer-needless-regressions`. *Priority: high.*

**17. Swap Courses 2 and 3, so that practice begins at lesson 6.** *Where:*
§B, `why_order` 2–3. *What is wrong:* a Subject built on "try first, then
learn why" makes the reader sit through six lessons of eye-movement science
before the first technique; the pacer needs nothing from Course 2 (its
misconception, "a pacer forces the eyes faster than they can move", can be
stated in Course 2 and *shown* in Course 3), while Course 2's `looking-back`
needs the pacer. Proposed order: Course 2 **Guided Practice** —
`reading-with-a-pacer`, `choosing-a-target-pace`, `the-daily-drill` (new),
`sprints-above-comfort`, `repeated-reading-and-transfer` (5); Course 3 **How
the Eyes Read** — `fixations-and-saccades`, `the-perceptual-span`,
`looking-back`, `fewer-needless-regressions`, `the-speed-ceiling`,
`training-the-periphery` (6). `reading-in-phrases` moves to Course 4 (finding
19); `lines-and-return-sweeps` is cut (finding 18). The count stays 42. The
`why_order` paragraph then reads: measurement first; practice second, because
the routine should start early and the log needs weeks; the eye third, as the
limits against which the practice is read. *Priority: medium-high (the
prerequisite break in 16 is high either way).*

**18. Cut `lines-and-return-sweeps`.** *Where:* Course 2.5. *What is wrong:*
its drill (narrow versus wide column, two passages) and its lab (`eye/lines`,
a calculator) are disconnected — the reading result never enters the lab; the
plan's own misconception entry says the evidence is mixed; a 90-character
column cannot be shown on a phone, so half the readers cannot do the drill;
and the one teachable fact (the return sweep costs a fixation) fits in a `ul`
of `fixations-and-saccades`. Its passages `P09`/`P10` go to the pool.
*Priority: medium.*

**19. `reading-in-phrases` confounds grouping with no-looking-back, and
belongs in Course 4.** *Where:* Course 3.4; §D.0 `phrases` display ("`rsvp` by
the passage's marked phrase boundaries"). *What is wrong:* the B side is RSVP
by phrase, so the comparison with `normal` differs in two things at once — the
grouping, and the removal of regressions that Course 4 then shows is costly.
The clean control is word-RSVP against phrase-RSVP at the same rate, which the
reader cannot run before `one-word-at-a-time`. *Change:* move it to Course 4
after `one-word-at-a-time`, with A = `rsvp` (chunk 1) and B = `phrases`, both
at the reader's baseline; the misconception stays. Course 4 becomes six
lessons; Course 3 (now the eye course) stays at six after finding 17.
*Priority: medium.*

**20. Course 6 opens with a calculator; its own principle says try first.**
*Where:* `measuring-difficulty` (6.1) before `your-rate-on-hard-text` (6.2).
*Change:* swap them: the reader measures a 290 → 170 drop on their own
reading, then learns the formula that predicted the drop and what it cannot
see. `measuring-difficulty` then computes on the two passages the reader has
just read, which is better than three passages read for counting only.
*Priority: medium.*

**21. `plateaus-and-transfer`'s drill does not produce side A.** *Where:*
Course 8.3 (`drill/compare`, "A practised band, B new kind"; the drill is one
passage `P47`). *What is wrong:* the reader reads only B; A must come from the
log (the last `test` entry) and the entry does not say so; the Do ("compute the
gain on practised passages and on a new kind") needs two befores and two
afters, which the Subject never collected for the new kind. *Change:* make the
lab `drill/single` on `P47` with a panel that pulls the baseline median and the
recent test median from the log and prints the reader's rate on `P47` against
both, with the honest sentence that a first reading of a new kind has no
baseline of its own; move "gain on practised passages" to `reading-your-curve`.
*Priority: medium.*

**22. Missing for adult readers: attention lapses.** *Where:* nowhere, except
"drifting attention" inside `fewer-needless-regressions`. *What is weak:* the
largest everyday speed loss for a skilled adult is re-reading a paragraph they
did not attend to, and the Subject has no drill or measure for it. *Change:*
low cost — in `drill/sections` (`shifting-gears`) and in `drill/practice`,
one tick-box after Done, before the questions: "did your attention leave the
text at least once?", logged in `extra`; `the-daily-drill`'s body treats a
"yes" as the reason to shorten the session rather than slow the pacer. No new
lesson. *Priority: low-medium.*

**23. Padding to trim rather than cut.** `how-much-you-read` carries the
single most useful sentence in the Subject (ten more minutes a day beats any
plausible rate gain) in a lab that is one multiplication; with the warm-up
reading (finding 5) it earns its place. `spacing-your-reviews` is not about
reading and its drill is a date calculator; keep it only if Course 7 would
otherwise be three lessons, and make its warm-up the delayed test of
`retrieval-beats-rereading` when due (finding 25). *Priority: low.*

### D. The drills as experiences

**24. Every compare view shows a difference of two single readings and no
yardstick.** *Where:* §D.1 `compare` (`drErrDiff`, `drRatio`; `drVerdictB`
only "when the cfg gives a baseline range"); every compare lesson from
`looking-back` on. *What is wrong:* a reader who gets 4/5 against 5/5 on two
different passages will read it as the technique's effect; Course 1 taught
them not to, and then no later view reminds them. *Change:* `drVerdictB`
becomes universal: every compare, ladder and repeat view reads the reader's
baseline range (and, once present, the spread of `test` entries) from the log
and prints the difference against it, with the fixed sentence from finding 14
about one question. When the log is empty the panel says so and uses the
preset's range. *Priority: high.*

**25. `retrieval-beats-rereading` gives the reread condition an immediate
test, which is itself retrieval practice.** *Where:* Course 7.2 (presets
"reread: 5/5 then 2/5; retrieve: 4/5 then 3/5"; tiles `reKeptA`/`reKeptB` =
delayed ÷ immediate). *What is wrong:* in Roediger and Karpicke the reread
group did not take the immediate test; answering five questions on `P44` on day
one is retrieval, so both conditions get it and the delayed difference the
lesson exists to show shrinks or vanishes. Also: a lesson that cannot be
completed in one sitting is the only one of its kind in the library and needs
a return path. *Change:* reread side — read `P44` twice, no immediate test;
retrieve side — read `P45` once, free recall (the `recall/free` flow, idea
units ticked); both — the five questions when the log says two or more days
have passed, offered as the warm-up on whichever lesson the reader opens next
(finding 5's mechanism) and in `log/history`. Tiles become `reDelayedA`,
`reDelayedB` and the difference; the preset keeps the shape of the published
result, labelled illustrative. The lesson is complete on day one with the
immediate part and the published shape; the reader's own delayed figures fill
in when they return. *Priority: medium-high.*

**26. Reading aloud is unrealistic for many readers and settings.** *Where:*
`the-inner-voice` (A `aloud`). *What is wrong:* a reader on a train, in an
office, or who cannot speak cannot do side A, and the lesson's point survives
without it. *Change:* make the aloud side optional with a typed fallback
(Brysbaert's 183, labelled a published average), and let the body say that
whispering is enough; the ratio tile is then "your silent rate against your
oral rate, or against the average". *Priority: medium.*

**27. Articulatory suppression for a hundred seconds is hard to sustain and
the result is uninterpretable if the reader stopped.** *Where:*
`silencing-the-inner-voice`. *Change:* a tick-box after Done — "did you keep
counting the whole way?" — logged in `extra` and printed beside the tiles; the
note says a reading in which the counting lapsed measures the lapse. Also tell
the reader to count under the breath, not aloud, and that mouthing is enough.
*Priority: medium.*

**28. The span drill measures memory and typing as much as vision, and its
default string cannot show the asymmetry it teaches.** *Where:*
`the-perceptual-span` (`flash/span`, 9-letter strings, type what you saw).
*What is wrong:* typing nine letters on a phone keyboard takes ten seconds and
the report decays; nine letters reach only ±4, while the lesson's point is
3–4 left against 14–15 right. *Change:* partial report — after the mask, cue
two or three positions and ask for those letters only (buttons, not typing);
default 15-letter strings; the note says letters without context understate
the span for words. *Priority: medium.*

**29. `fewer-needless-regressions`: the drill's self-count never reaches the
lab.** *Where:* Course 3.5 (drill: masked then unmasked pacer and "how many
times did you want to look back?"; lab: `eye/budget` with typed shares).
*Change:* either make the self-count the input (`regNeed` = count ÷ the
passage's model fixations, which the kit can compute from words × 15/17) or
make the lab the compare of the two readings and keep `eye/budget`'s split as
the worked example only. As specified the reader does a drill and then types
preset numbers. *Priority: medium.*

**30. `training-the-periphery` promises a correlation no view computes.**
*Where:* Course 2.6 ("whether the table time and the reading rate move
together across sessions (the log does this over weeks)"). *Change:* either add
a `flash` series to `log/history` (table time per cell by session beside test
effective rate, two series, no correlation coefficient — the reader eyeballs
it) or drop the sentence and let the lesson's misconception carry the point.
*Priority: low-medium.*

**31. `testing-a-speed-claim`'s "1-minute reading at the claimed pace to feel
it" should be capped.** *Where:* Course 4.5. *What is wrong:* 1,500 wpm is 40 ms
per word, a 25 Hz flicker, which the photosensitivity sentence in §D.0 exists
to warn about, and nothing is learned past about 600 wpm that is not learned
at 600. *Change:* cap the felt reading at 600 wpm with the sentence "beyond
this the display is a flicker, and that is itself the finding"; RSVP tiles
print requested and measured ms per word, as `flash/span` already does.
*Priority: medium.*

**32. Phone and keyboard specifics the kit section should state.** *Where:*
§D.0 Accessibility. (a) `scan/find`, `scan/inspect` and `text/coverage` are
click-the-word drills: they need Tab/arrow navigation between words or a
typed answer fallback, or they are not keyboard-operable as promised. (b) The
pacer highlight must not rely on colour alone (an underline or a bar in the
margin). (c) On a phone a `pacer` line is six to eight words and the highlight
steps every ~1.5 s; `drPacerLineMs` is computed for a 12-word line and the
panel should say the number is for a stated line, not the one on screen (the
plan says this in §D.0; it should also be in the tile's label). (d) `S01` at
600 words scrolls on a phone and the scroll is inside the timing; say so.
(e) Say honestly in `prerequisites` that the drills are visual and timed and
that a reader using a screen reader can read the lessons but not do the
drills. *Priority: medium.*

**33. Order and passage confounds in every compare.** *Where:* §D.1 `compare`
(A always first, always the control). The second reading is warmer and the
first is fresher, and the pair differ by passage; the matched-pair rule bounds
the second but nothing bounds the first. *Change:* the cfg carries
`order: "AB" | "BA" | "alternate"`, defaulting to alternate by the parity of
the log's length, and the log records which was first; the `note` of each
compare lesson names both confounds in one sentence. *Priority: low-medium.*

**34. The page order spoils "try first" for the lessons that depend on it.**
*Where:* §0 deviation 4, §F "Try first, then explain"; the renderer puts
`one_line`, `summary` and the three `concepts` above the body and the lab
below it. A reader of `comprehension-and-effective-rate` will have read a
summary saying that pushing the pace lowers the score before they are sent to
find that out. *Change:* for the lessons §C marks as drill-first, the author
writes `summary` and `concepts` that state the question and the method, not
the expected result, and the review checks it. *Priority: low.*

### E. Voice and honesty

**35. The framing is honest; two places lean.** `§F` is the right contract and
the exemplary paragraph is the right register. (a) The tagline's "read faster
in the ways that work" is the one near-promise; "in the ways that can be
measured" is truer to the Subject and no less inviting. (b) The experimental
presets are named for the technique losing (`pushed-too-far`, `masked-costs`,
`stream-loses`, `chunks-hurt`) with a neutral alternate; name the alternates
for the technique helping where the evidence allows (`steadier` already does
this), and let the body say plainly, once per compare lesson, that a reader
whose result goes the other way has not refuted the study and the study has
not refuted them. (c) The Subject never states what gain an honest reader
should expect; it should not invent a number, but `the-daily-drill` and
`a-practice-week` should say in a sentence that the research finds modest rate
gains with comprehension held, and that the large savings are in Courses 5
and 6 — which `why_order` 4 already says and the practice lessons should
repeat. *Priority: low-medium.*

**36. Gears are in standard words for college students and the reader's rate
is in words.** *Where:* `typical-rates-and-reading-gears` (`log/gears` takes
"one rate"); `words-per-minute` teaches exactly this mismatch. *Change:* feed
`drStdWpm` (the kit has the characters) or state the mismatch in the panel; the
accuracy review confirms Carver's units. *Priority: medium (also for the
accuracy review).*

## What is right and should not be changed

- The three-baseline opening, the range as the first yardstick, and "one
  reading is one measurement" as the material clause. Keep the rule; sharpen
  it (finding 10).
- Effective rate beside every rate, from lesson 2 on, and the ban on calling
  any figure "your reading speed".
- Every technique tried against a control at the same target rate (`looking-back`,
  `rsvp-without-looking-back`, `silencing-the-inner-voice`, `previewing-before-reading`
  with preview time counted). This is the Subject's spine.
- `repeated-reading-and-transfer`'s design: three readings of one passage then
  one of a new one, with the misconception "the third reading shows my new
  speed". It is the clearest lesson in the plan.
- `sprints-above-comfort`: the tradition's drill, done as the tradition does it,
  and measured by the Subject's own yardstick.
- The questions rule in §P (answer it without the passage first; rotate the
  correct index; gist and detail kinds) and the garden-path passages for
  `rsvp-without-looking-back`.
- The passage-never-visible-during-questions rule, the no-timer-on-load rule,
  whole-millisecond timing, and the one-key log with try/catch.
- `inspectional-reading` on an imaginary book's front and back matter, and
  `triaging-a-reading-list`: the two lessons where most real time is saved.
- `how-much-you-read`'s misconception. Keep it even if the lesson shrinks.
- §F: "presented, not endorsed — both ways", no promises, the history as
  people, one light remark. Hold the author to it.
- The `note` as "what this measurement cannot settle", and `steps` as the
  protocol for repeating the drill — once there is something to repeat it on.
