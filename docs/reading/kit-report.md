# readkit (Reading Faster): kit report

Lesson authors work from this report. It records what the kit does as built.
Where it differs from docs/reading/PLAN.md §D, the "Deviations" section gives
the reason. PLAN §D.3 (the amendments from the pre-authoring reviews) is
implemented. Where D.3 and D.0–D.2 disagree, D.3 wins.

## Files (nothing committed)

- `scripts/mathpath/labs/readkit.py`: the entry point `readkit_lab(cfg)` and the modes drill, eye, flash and scan. It dispatches triage, text, recall and log to `readkit_b.readkit_b_lab` through a lazy import, and raises on an unknown mode or view.
- `scripts/mathpath/labs/readkit_b.py`: the modes triage, text, recall and log.
- `scripts/mathpath/labs/readkit_core.py`: the shared parts.
  - The JS blocks: `RD_CORE_JS` (printing and parsing), `RD_TEXT_JS` (word, sentence and syllable rules), `RD_LOG_JS` (the log and the due banner), and `RD_WIRE_JS` (preset menu, inputs, redraw).
  - The Python mirror of the text rules, passage validation, `slot()` and `build_lab()`.
  - It imports `attr`, `field_text`, `kpis_html`, `select_html` and `text_html` from `capkit_core`, read-only.
- `scripts/mathpath/labs/readkit_drill.py`: the drill engine, browser only.
  - `RD_DRILL_JS` is the core.
  - `RD_TIMED_JS` (pacer, mask, RSVP, phrases), `RD_RECALL_JS` (reread, free recall) and `RD_FIND_JS` (scan, coverage) ship only on pages that use them.
- `scripts/mathpath/labs/__init__.py`: one import (`readkit,`) and one registry line (`"readkit": readkit.readkit_lab,`). readkit is NOT added to `KITS_WITH_EXPECTATIONS`, which is left to wiring (D.0).
- `scripts/mathcheck.js`: one self-contained block, `// ---- readkit (Reading Faster) ----` … `// ---- end readkit ----`, just before "THE VERDICT". It runs in its own vm context with RATIONAL_JS, RD_CORE_JS, RD_TEXT_JS and the eight modes' pure blocks, and has 147 cases.

The kit never imports `content/`. Passages arrive in the cfg as dicts. The real bank (`content.reading.passages`) was imported only from a scratch script, to check that every bank passage validates: 79 of 82 build a drill, and the other 3 (B01, S01, S02) have no questions by design.

## Conventions as implemented

**Entry point and cfg.**
- `readkit_lab(cfg)` takes `cfg["mode"]` and `cfg["view"]`; the view defaults to the mode's first.
- These keys are common to every view:
  - `mode`, `view`, `presets` (required, non-empty), `preset` (the preset shown first; default the first);
  - `title`, `panel_title`, `panel_intro`;
  - `lesson` (the slug written into log entries; default the last segment of the page's path);
  - `warmup` and `warmup_kind` (see Warm-up).
- A cfg key that a view does not take raises, naming the keys it does take.

**Ids.**
- Prefixes are `dr ey fl sc tr tx re lg`.
- Inputs are text boxes `<prefix>In<Key>`, for example `drInSeconds`, `drInWordsA` or `lgInTests`.
- Other controls:
  - the preset menu is `<prefix>Preset`;
  - the status banner is `<prefix>Status`;
  - the table is `<prefix>Table`;
  - an extra area (chart, Schulte grid, triage buttons) is `<prefix>Extra`.
- Drill elements are `rd<Name><slot>`. The slot is `''` for one drill, `A`/`B` for a compare, `1`..`4` for runs, and `W` for the warm-up. The elements are:
  - `rdBox`, `rdMsg`, `rdStart`, `rdDone`, `rdReset`, `rdText`, `rdWork` and `rdOut`;
  - `rdNext` (sections; scan "Skip this one") and `rdAlt` (aloud fallback).
- The due-test banner is `rdDue`, on every readkit page.

**Presets.** Each preset is `{id, label, <input keys>, expect?, note?}`.
- The `id` is lowercase letters, digits and hyphens.
- A key that is not an input of the view raises, naming the inputs.
- An input with no default must be given.
- `expect` is `{tile id: exact text}`, and labcheck checks it.
- List-valued inputs:
  - `entries` are written as a list of `(rate, right, asked)` triples;
  - `nums` are a list of numbers;
  - `strings` are a list of strings;
  - `rec` (records) is a list of dicts.

**Hostile input.** Every text box survives `''`, `banana`, `0`, `-1`, `1/0` and `A>B`. The status banner turns red with a sentence, and the tiles blank to `—`. labcheck sweeps every page.

**Two sources, one computation.** Tiles are computed only from the text inputs.
- A preset writes the inputs.
- A drill writes the same inputs when it ends: through `rdWrite`, after Score (or at the end of find, coverage, flash or Schulte).
- Measured time is `performance.now()` rounded to whole milliseconds, written as exact seconds (`96.042`).

**Nothing starts by itself.**
- No timer, animation or flash starts at load or on `change`/`input`.
- Only `rdStart*`, `rdDone*`, `flStart` and the in-drill buttons start anything.
- Loading a page reads the log, which only fills boxes and the banner.

**Number format** (`rdFig`, `rdUnit`, `rdShare`, `rdSigned`).
- Whole numbers are grouped: `1,825,000`, `250 wpm`.
- A value exact in two decimals prints exactly: `191.25 ms`, `230.4 wpm`, `1.64 s`, `12.75 characters`.
- Anything else prints `≈` and one decimal, rounded half away from zero on the exact rational: `≈ 266.7 wpm`, `≈ 96.1 s`.
- The minus sign is U+2212: `−48 wpm`. A signed value reads `+16 wpm` or `≈ +16.7 points`.
- A share prints the reduced fraction and the percent: `4/5 = 80%`, `7/12 ≈ 58.3%`, `1/16 = 6.25%`, `1 = 100%`, `0 = 0%`. When the numerator or the denominator has more than 4 digits, only the percent prints: `≈ 22.7%`.
- Arithmetic is exact BigInt rationals (RATIONAL_JS). Floats appear only in SVG pixel coordinates.

**Text rules** (JS `RD_TEXT_JS`, mirrored in Python `readkit_core`).
- A word is a whitespace token containing a letter or digit (`A–Z a–z 0–9 À–ɏ`).
- `|` (phrase mark) and a leading `## ` (heading) are markup, not words.
- A sentence ends at a run of `.`, `!` or `?`, then optional closing quotes or brackets, then a space or the end.
- Syllables: count the vowel groups (`a e i o u y`), take one off for a final `e` that is not `le`, with a minimum of 1 per word.
- `chars` is the length of the normalized text, with each whitespace run counted as one space.
- Readability counts body paragraphs only (headings excluded). Drill word counts include headings.

**Passages** (validated at build time; a bad passage raises, naming it).
- Shape: `{id, title, paragraphs, band?, kind?, phrases?, questions?, ideas?, sections?, targets?}`. Any other key raises, and so does a passage given twice.
- `id` matches `[A-Z][A-Z0-9]{1,5}`.
- `band` is one of easy, standard, hard or mixed.
- `kind` is one of narrative, expository, procedural, argument or document.
- `paragraphs` is a non-empty list of strings. A heading starts with `## ` and may not carry phrase marks. `phrases: True` if and only if some paragraph carries `|`.
- `questions` is 4 to 6 items; the bank gives six, three gist and three detail. Each is `{q, a: 4 distinct options, c: 0–3, kind: "gist"|"detail"}`.
- `ideas` is 8 to 14 strings.
- `sections` is `j`, `[j]` or `[0, j]` with `0 < j < len(paragraphs)`: the paragraph where section 2 starts.
- `targets` (for scan/find) is a list of `{q, answer, nth?}` (the answer's words are matched without regard to case or punctuation; `nth` is 1-based) or `{q, at: [i, j]}` (token indices).
- A page ships only the passages its cfg gives, with only `id`, `title`, `paragraphs` and `questions`. `ideas` ships only when a free-recall drill ticks them.

**The drill flow.**
1. Start shows the passage and starts the clock.
2. Done hides it and stops the clock. RSVP, phrases, pacer, mask, gist and a time-limited inspect end by themselves.
3. A tick follows, if the slot has one.
4. The questions come one at a time, four buttons each, with no going back. The passage is hidden (`rdText` empty and `display:none`) the whole time.
5. Score writes the inputs, redraws, shows which answers were right in `rdOut` (with the tick, for example `(My attention left the text at some point: yes.)`), and appends a log entry.
6. Start again re-runs the drill. Reset abandons it without logging.

**Displays** (a drill's `display`; a compare side carries its own).
- `normal`.
- `aloud`: normal, plus a button "I can’t read aloud here" (D.3.13). It writes the published figure into the side's boxes instead of a reading: words = `published` (default 183), seconds = 60, right = asked = 0. It labels this in `rdOut`, hides Start, and logs nothing. Reset brings the drill back.
- `pacer`: the highlight moves line by line. Lines come from layout at Start (word spans grouped by `offsetTop`), and each line takes its words × 60,000 / target ms. The highlight is a background plus an underline, not colour alone. It ends by itself.
- `mask`: the pacer, with the lines above the highlight hidden.
- `rsvp`: `chunk` words at a time, each for 60,000 × chunk / target ms, in a centred box. It ends by itself.
- `phrases`: one marked phrase at a time, for its words × 60,000 / target ms. It ends by itself.
- `gist`: headings and first sentences for `limit` seconds. It ends by itself, and only the gist questions are asked.
- `preview`: headings plus the first and last paragraphs for `limit` seconds, then the whole passage. The clock runs through both.
- A drill refuses RSVP and phrase targets above 600 wpm with a sentence; presets may state any rate (D.3.12).
- RSVP and phrases carry the photosensitivity sentence in their slot intro.
- There is no CSS animation anywhere, so reduced motion needs nothing more: every timed display moves in discrete steps.

**Keyboard.**
- Every control is a button.
- In the click-the-word drills (scan/find, text/coverage) each word is `tabindex=0 role=button`. Tab or the arrow keys move between words, and Enter or Space hits one.
- The question and flash-answer buttons take Enter.

**The log** (`localStorage` key `learn-reading-log`; every read and write is in try/catch).
- With storage blocked, every drill runs and the slot's message says once: "This browser is not keeping data for this page, so your results will not be kept. Every drill still runs."
- A drill entry is:
  `{v: 1, at, lesson, mode, view, side, passage, display, words, chars, ms, correct, total, kind, extra: {gist, gistTotal, detail, detailTotal, target, split, order, kept, lapse}}`
- Other entries:
  - reread (recall/delayed A): `words` = 2 × the passage, `due`, `url`;
  - free recall: `extra {units, recalled, summaryWords}`, plus `due` and `url` on the delayed view;
  - scan/find: `extra {wrong}`;
  - coverage: `extra {unknown}`;
  - flash/span: `extra {len, ms, cues, measured}`;
  - Schulte: `ms`, `extra {errors, seed}`;
  - delayed test: view `delayed-test`, `extra {delA, delB}`;
  - notes: view `note`, `extra {text}`;
  - a saved plan: view `plan`, `extra {text}`;
  - warm-up: mode and view `warmup`.
- `kind` is required: baseline, test, practice, condition or other (D.3.2).

**Warm-up** (any view; D.3.5).
- `cfg["warmup"]` is a passage dict or a list. `cfg["warmup_kind"]` defaults to practice.
- It renders slot `W` ("Warm-up reading") above the view.
- Start serves the first listed passage whose id is not in the log. When every one is logged, it says so and does not start.
- It fills none of the view's boxes.
- When a delayed test is due elsewhere, the `rdDue` banner shows and the warm-up box is hidden.

**Verdict wording** (`drVerdictB`, `lgVerdict`; D.3.3). Exactly these strings:
- `inside the baseline range`
- `above the baseline range once — a fourth reading does this about one time in four`
- `above the baseline range on the median of the last three tests`
- `below the baseline range` and `below the baseline range on the median of the last three tests`
- `no baseline readings yet` (compare, when there is no range)
- `needs a reading after the three baselines` (history, with fewer than 4 sessions)
- `no baseline range given` (profile)

The tier rule (`lgTiers`): with three or more tests, the median of the last three is compared first. If it is inside the range, the latest test decides between `once` and `inside`. With fewer than three tests, the latest test is compared on its own.

## Modes and views

For each view below, "cfg" lists the view-specific keys, "inputs" the text boxes (key: kind, default; `—` means no default, so a preset must give it), and "tiles" the tile ids with an example as printed. Input kinds:
- `count`: a whole number, 1 or more.
- `nncount`: a whole number, 0 or more.
- `pos`: more than 0.
- `nn`: 0 or more.
- `share`: from 0 to 1.
- `opt`: empty, or more than 0.
- `name`: text.

The examples come from the demo build (labcheck-pinned) or from scripts/mathcheck.js.

### drill (`dr`)

Every drill reading's side cfg (`cfg` itself for single and practice; `cfg["a"]`/`cfg["b"]` for compare) takes:
- `display` (default `normal`);
- `questions` (bool, default True);
- `target` (wpm; required for pacer, mask, rsvp and phrases);
- `chunk` (1–5, default 1);
- `limit` (seconds, 5–1800; required for gist and preview);
- `kind` (log kind);
- `suppress` (bool, default False: adds the counting instruction and the tick "I kept counting the whole way", stored as `extra.kept`);
- `published` (aloud fallback figure, default 183);
- `label` (compare only).

The drill-wide cfg `lineWords` (default 12) states the line length for `drPacerLineMs`.

**single**
- cfg: `passage` (or a one-item `passages`) and the side keys. kind defaults to condition.
- Inputs: `words` (count, the passage's words), `chars` (count, the passage's chars), `seconds` (pos, —), `correct` and `total` (nncount; 0 when questions are off, else —).
  - With pacer or mask: `target` (pos, cfg target).
  - With rsvp: `target` and `chunk` (count, cfg chunk).
  - With phrases: `target` and `phrases` (count, the passage's phrases).
  - With gist: `shown` (nncount, the words in headings and first sentences).
- Tiles:
  - `drWords` `400 words`; `drTime` `96 s` or `≈ 96.1 s`; `drWpm` `250 wpm`; `drStdWpm` `275 standard wpm` (chars / 6 × 60 / seconds); `drComp` `2/3 ≈ 66.7%` or `no questions`; `drErr` `≈ 166.7 wpm` or `no questions`.
  - With pacer or mask: `drPacerLineMs` `2,880 ms` (lineWords × 60,000 / target).
  - With rsvp: `drWordMs` `240 ms` (requested, 60,000 × chunk / target) and `drWordMsSeen` `240 ms` (measured, seconds × 1,000 × chunk / words).
  - With phrases: `drPhraseMs` `960 ms` (words × 60,000 / (target × phrases)).
  - **With gist** (D.3.7): `drWords`, `drTime`, `drShown` `1/5 = 20%`, `drComp` (gist questions only) `3/4 = 75%`, and `drGistPerMin` `4.5 gist answers a minute`. There is no `drWpm`, `drStdWpm` or `drErr`.

**practice** (D.3.4)
- cfg: `pool` (a list of passage dicts; `passages` also works), `target` (default 250), `display` (`normal` or `pacer` only), `hold` (default 2/3), `kind` (default practice), and the side keys.
- Page controls:
  - `rdPool`, which names the next unread passage;
  - the checkbox `rdPacer` "Read with the pacer at the target rate in the panel";
  - the checkbox `rdTest` "This is a test reading (natural pace, no pacer)", which logs `test` with the normal display;
  - a collapsed `rdPaste` textarea for the reader's own text. Paragraphs are split on blank lines; it has no questions, total 0, and is logged as `practice` with passage `pasted`.
- After Done comes the tick "My attention left the text at some point" (`extra.lapse`).
- Inputs: `words`, `seconds`, `correct` (nncount, 0), `total` (nncount, 0), `target` (pos, cfg target), `pacerLog` (entries, default empty: target/right/asked of the reader's pacer practice readings with questions, oldest first), `sinceTest` (nncount, 0: practice drill readings logged since the last `test` entry).
  - At load and after each Score, the page fills `pacerLog` and `sinceTest` from the log.
- Tiles: `drWords`, `drTime`, `drWpm` `300 wpm`, `drComp`, `drErr`, and:
  - `drHold` `300 wpm` or `not yet`: the fastest target whose last three pacer readings at it all scored at least `hold`.
  - `drNextTarget` `315 wpm`, `285 wpm`, or `no pacer readings yet`. T is the last reading's target. Three holds in a row at T give T × 21/20; two misses in a row at T give T × 19/20; otherwise T.
  - `drTestDue`: `after 2 more practice sessions` or `due now: make the next reading a test`. A test is due after 4 practice sessions.
- A pool page may weigh up to 67 KB gzipped. Measured with the real bank's Q01–Q30 (see Page weight): 20 passages give 64.4 KB, and all 30 give 78.6 KB.

**compare**
- cfg: `passages` (two: A, then B), `a` and `b` (side cfgs; kind defaults to condition; `label` defaults to "Reading A"/"Reading B"), `kinds` (bool, default False: gist and detail inputs instead of right/asked), `ratioOf` (`err`, the default, or `wpm`), and `order` (`AB`, `BA` or `alternate`, the default; D.3.11).
  - With `alternate`, the order comes from the parity of the log's length at load: even gives AB, odd gives BA.
  - With BA, box B is moved above box A. `rdOrder` says the order, and every entry records `extra.order`.
- Inputs, per side s = A or B:
  - `words<s>`, `seconds<s>`, and `correct<s>`/`total<s>`; with `kinds`, `gist<s>`, `gistTotal<s>`, `detail<s>` and `detailTotal<s>`.
  - Display extras as in single: `target<s>`, `chunk<s>`, `phrases<s>`, `shown<s>`.
  - Then `baseLo` and `baseHi` (opt, empty).
  - When both range boxes are empty at load and the log holds baseline entries, the range is filled from the first three. The button `rdUseBase` "Use my baseline range" does the same on demand, and `rdBaseNote` says what happened.
- Tiles:
  - `drWpmA`, `drWpmB` (`240 wpm`, `480 wpm`); `drCompA`, `drCompB`; `drErrA`, `drErrB` (`192 wpm`).
  - `drErrDiff` `−48 wpm`, `+16 wpm`, or `needs questions on both`.
  - `drRatio` `4/5 = 80%` (of the effective rate, or of the rate when `ratioOf` is `wpm`, as in `238/183 ≈ 130.1%`).
  - `drVerdictB` (rate B against the range): one of the verdict strings above.
  - With `kinds`: `drGistA`, `drDetailA`, `drGistB`, `drDetailB` (`1/3 ≈ 33.3%`).
  - Where a side has the display: `drPacerLineMs`, `drWordMs` and `drWordMsSeen`, `drPhraseMs`.
- The panel intro prints "One question is ≈ 16.7 points; a one-question difference is not a result." (computed from the passages' question count; D.3.1).

**ladder**
- cfg: `passages` (three), `targets` (three, default `[250, 300, 375]`), `display` (`pacer` (default), `mask` or `normal`), `hold` (default 2/3; D.3.6), `kind`.
- Inputs, for i = 1..3: `t<i>` (pos, the target), `words<i>`, `seconds<i>`, `correct<i>`, `total<i>`.
- Tiles:
  - `drWpm1..3`, `drErr1..3`;
  - `drBestTarget` `288 wpm`, or `none at 2/3 or better`: the fastest target whose comprehension is at least `hold`;
  - `drBestErr` `230.4 wpm`: its effective rate;
  - `drTopErr` `240 wpm (target 240 wpm)`: the highest effective rate, with ties going to the slower target.
- The panel prints the one-question note.

**repeat**
- cfg: `passages` (two: readings 1–3 on the first, reading 4 on the second), `questions` (four bools, default `[False, False, True, True]`), `kind`.
- Inputs, for i = 1..4: `words<i>`, `seconds<i>`, `correct<i>`, `total<i>`.
- Tiles: `drWpm1..4` `248 wpm`; `drRepeatGain` `+100 wpm` (reading 3 − reading 1); `drTransferGain` `+8 wpm` (reading 4 − reading 1).
- The panel prints the one-question note.

**sections**
- cfg: `passage` (with `sections`), `questions` (bool), `kind`.
- Flow: Start, read section 1, then Next section (`rdNext`), read section 2, Done. Then the attention tick, then the questions.
- Inputs: `words1`, `seconds1`, `words2`, `seconds2`, `correct`, `total`.
- Tiles: `drRateS1` `≈ 310.3 wpm`; `drRateS2` `≈ 189.5 wpm`; `drWpm`; `drComp`; `drErr` `≈ 94.1 wpm`.

### eye (`ey`)

**budget**
- cfg: `split` (bool).
- Inputs: `fix` (pos, —), `sac` (nn, —), `step` (pos, —), `reg` (share, —; or, with split, `regNeed` and `regRepair`), `cpw` (pos, 6).
- Tiles: `eyFixPerWord` `15/17 ≈ 0.9 fixations` (or `3/4 = 0.75 fixations`); `eyMsPerWord` `225 ms`; `eyWpm` `≈ 266.7 wpm`; with split, `eySaved` `≈ 31.4 wpm`.
- A regression share of 1 or more is refused.
- The panel says the model understates a regression's cost.

**required**
- cfg: `claim` (bool), `identify` (default 8), `perceptual` (default 15).
- Inputs: `target` (pos, —); or, with claim, `words` (pos), `seconds` (pos) and `comp` (share, 1). Then `fix` (225), `sac` (30), `cpw` (6), `reg` (0).
- Tiles:
  - `eyNeeded` `25.5 characters`, `≈ 28.3 characters`;
  - `eyVerdict`: `at these settings, within the word-identification span`, `at these settings, beyond the word-identification span but within the perceptual span`, or `at these settings, beyond the perceptual span`;
  - with claim, `eyClaimWpm` `1,500 wpm` and `eyClaimErr` `750 wpm`.

**lines**
- Inputs: `cpl` (pos, —), `lines` (count, —), `step` (8), `fix` (225), `sac` (30), `sweep` (nn, —).
- Tiles:
  - `eyFixPerLine` `5 fixations`, or `45/4 = 11.25 fixations` (cpl / step);
  - `eySweepShare` `1/5 = 20%`: sweeps / (forward saccades + sweeps), where a line of f fixations has f − 1 forward saccades and 1 sweep, so the share is 1/f;
  - `eyMsPerLine` `1,545 ms` (f × fix + (f − 1) × sac + sweep);
  - `eySweepTime` `20/103 ≈ 19.4%`;
  - `eyTotal` `30.9 s`.

### flash (`fl`)

**span**: partial report (D.3.8).
- cfg: `len` (odd, 3–21, default 15: positions −7..+7), `ms` (17–2000, default 150), `n` (trials, 1–20, default 10), `cues` (2–3, default 3), `kind` (default practice).
- Drill steps: a + for 700 ms; the string for `ms` (requested); a mask of `#` for 300 ms; then the cued positions one at a time. A row marks the asked position `?`, and the reader picks from four letter buttons or "not seen".
- After `n` trials it writes `targets` and `typed`, prints the measured display times ("Requested 150 ms; measured on this screen: 150 to 167 ms…"), and logs.
- Inputs:
  - `targets`: letters, `;`-separated, one odd length.
  - `typed`: the answers by position. `.` is a position not asked, `-` (or `?` or `_`) is asked and not seen, and a letter is the answer. A whole-report preset simply has no `.`.
- Tiles:
  - `flCentre` `1 = 100%`, or `not asked`;
  - `flEdge` `1/4 = 25%`: both outermost positions pooled, right / asked;
  - `flSpan` `left 2, right 1`: the outermost asked position on each side with accuracy at least 1/2.
- The tile labels name the flash: "Letters identified at the centre, 150 ms flash". The panel gives the saccade latency as about 175–200 ms and the photosensitivity sentence.

**schulte**
- cfg: `kind`.
- Drill: a fresh random seed, a live 5×5 table, and 1..25 clicked in order. Wrong clicks are counted.
- Inputs: `seconds` (pos, —), `errors` (nncount, 0), `seed` (nncount, —).
- Tiles: `flTime` `62 s`; `flPerCell` `1.64 s`; `flErrors` `1`.
- A preset's seed draws its table in `flExtra` with the stated generator. Seed 12345 gives 5, 23, 1, 4, 3, 13, …

### scan (`sc`)

**find**
- cfg: `passage`, `targets` (or the passage's own `targets`), `limit` (optional seconds), `kind` (default other).
- Drill: a prompt per target. Clicking (or Enter on) a word inside the target's token range counts as found; any other word counts a wrong click. `rdNext` skips a target.
- Inputs: `found` (nncount), `wrong` (0), `targets` (count, the number of targets), `seconds`, `words` (the passage's words).
- Tiles: `scFound` `5 of 5`; `scPerTarget` `19 s` (seconds / found), or `none found`; `scWordsPerSec` `≈ 6.3 words a second`; `scWrong` `1`.

**inspect**
- cfg: `passage` (with questions), `limit` (default 300), `kind`.
- Drill: a time-limited look, then the passage's questions.
- Inputs: `found` (questions right), `targets` (questions), `seconds`, `words`.
- Tiles: `scFound` `4 of 5`; `scPerTarget` `75 s` (per right answer); `scWordsPerSec`.

### triage (`tr`)

**plan**
- Inputs: `items` (1–12 records `{title, words, value, choice: read|skim|skip}`), `read` (250), `skim` (750), `coverage` (share, 1/2), `budget` (pos, —).
- Each item gets read/skim/skip buttons in `trExtra`, which rewrite the items box.
- Tiles: `trMinutes` `28 min`; `trCovered` `3/4 = 75%`; `trFits` `fits, 12 min to spare` or `over the budget by 8 min`.

### text (`tx`)

**readability**
- cfg: `passage` or `passages`, the texts a preset may name.
- Inputs: `words`, `sentences`, `syllables` (count, default 1).
- A preset gives either all three counts or `"passage": "<id>"`. In the second case the kit counts the passage, shows it in `txPassage`, and writes the counts.
- A collapsed `txOwn` textarea with a `txCount` button counts the reader's own text.
- Tiles: `txWords` `139`; `txSentences` `11`; `txSyllables` `190 (by the rule)`; `txFre` `≈ 78.4`; `txGrade` `≈ 5.5` or `8.73`.

**coverage**
- cfg: `passage`, `kind` (default other).
- Drill: click (or Enter or Space on) every unknown word; a second hit unmarks. The Done button reads "Count my marks".
- Inputs: `tokens` (count, the passage's words), `unknown` (nncount, —).
- Tiles: `txCoverage` `49/50 = 98%`; `txOneIn` `one unknown in every 50 tokens` or `no unknown words` (D.3.16).

**volume**
- Inputs: `minutes` (nn), `wpm` (pos), `days` (365), `bookWords` (90000).
- Tiles: `txWordsYear` `1,825,000 words`; `txBooksYear` `≈ 20.3 books`.

### recall (`re`)

**free**
- cfg: `passage` (with ideas), `summary` (bool: ask for a three-sentence summary instead of everything remembered), `kind` (default condition).
- Drill:
  1. Read, then Done.
  2. With the passage hidden, write in a textarea, then press Finished writing.
  3. The idea units are shown, and the reader ticks the ones the writing contains. The kit never scores the writing itself.
  4. Score.
- Inputs: `units` (count, the passage's ideas), `recalled` (nncount, —), `words`, `seconds`, `summaryWords` (nncount, 0).
- Tiles: `reRecall` `7/12 ≈ 58.3%`; `reRate` `140 wpm` (rate × recall); `reWordsPerUnit` `≈ 6.7 words`.

**delayed** (D.3.9)
- cfg: `passages` (two with the same number of questions; the second needs ideas), `days` (1–60, default 2), `kind` (default condition).
- Side A, "Read twice": read, Done, then "Read it again", Done. There is no test. It is logged with `due` and `url`.
- Side B, "Read once, then recall": free recall with ticked idea units. It is logged with `due` and `url`.
- When both sides are logged, `reDelayed` shows "due on <date>". Once due, it shows a "Take the delayed test" button: both passages' questions with no passage shown. That test writes `delA`, `delB` and `total` and logs `delayed-test`. It is not offered again.
- Every readkit page shows `rdDue` with a link while the test is due.
- Inputs: `delA`, `delB` (nncount, —), `total` (count, the question count), `units` (count, B's ideas), `recalled` (nncount, —).
- A preset may carry published percentages as `total: 100`.
- Tiles: `reDelayedA` `1/3 ≈ 33.3%`; `reDelayedB` `1/2 = 50%`; `reDelayedDiff` `≈ +16.7 points` (B − A, in percentage points); `reRecallB` `5/8 = 62.5%`.
- With 6 or fewer questions, the status prints the one-question note.

**schedule**
- Inputs: `first` (1), `mult` (nn, 2), `reviews` (count, 5, at most 12), `minutes` (nn, 10).
- Tiles: `reDays` `1, 3, 7, 15, 31`; `reLastDay` `day 31`; `reMinutes` `50 min`.

### log (`lg`)

Each view has a button `lgMine` and a message `lgMsg`. Noise, history and profile compute over `baseline` and `test` entries only (D.3.2).

**noise**
- Inputs: `base` (2–10 numbers, —), `tests` (1–20 numbers, oldest first, —).
- "Use my baselines" fills the first three baseline rates and up to 20 test rates.
- Tiles:
  - `lgMean` `≈ 244.7 wpm`; `lgRange` `13 wpm`;
  - `lgTestMedian` `270 wpm`, or `275 wpm (of 2)`;
  - `lgVerdict` (the tier rule);
  - `lgBeyond` `39 wpm above the top (3 ranges)` or `inside`.

**gears**
- cfg: `gears` (up to 8 `(name, wpm)` pairs; default scanning 600, skimming 450, rauding 300, learning 200, memorising 138), `average` (default 238).
- Inputs: `wpm` (pos, —), `stdwpm` (opt, empty).
- "Use my baseline median" fills both. `stdwpm` is filled from the logged `chars`.
- Tiles:
  - `lgNearest` `rauding, 300 wpm` or `above every gear`. It is computed from `stdwpm` when given, else from `wpm`; ties go to the slower gear.
  - `lgVsAverage` `160/119 ≈ 134.5%`, always from `wpm` (D.3.15).

**history**
- Inputs: `entries` (rate/right/asked, 0–200), `practice` (the same, default empty).
- At load, and on "Show my log", the page fills both from the log and lists every entry in `lgLog`, with uncounted entries greyed. The other controls:
  - `lgExport` writes CSV text into the read-only textarea `lgCsv`;
  - `lgNote` with `lgNoteAdd` adds a note entry;
  - `lgClearAsk` then `lgClearYes` (or `lgClearNo`) clears the log after an in-page confirmation.
- Tiles: `lgSessions` `3`; `lgBaseMedian` `240 wpm`; `lgRecentMedian` `270 wpm`, or `after 6 sessions`; `lgLatestErr` `251 wpm`; `lgVerdict`. The first three sessions are the baselines and the rest are tests.
- The SVG chart in `lgExtra` draws baselines and tests as the line, and practice as a lighter dashed series (D.3.2).

**plan**
- Inputs: `rows` (1–10 records `{drill, sessions, minutes}`), `test` (name, `test reading`), `budget` (pos, —).
- "Save this plan to my log" logs it.
- Tiles: `lgWeekMinutes` `160 min`; `lgTestShare` `1/16 = 6.25%` or `no test in the week`; `lgFits` `fits, 20 min to spare`.

**profile**
- Inputs: `errThen`, `errNow` (pos); `baseLo`, `baseHi` (opt); `gistThen`, `gistNow` (share); `scanThen`, `scanNow` (pos, seconds per target); `recallThen`, `recallNow` (share).
- "Fill from my log" takes the first and last baseline or test entries of each kind. For the skim, scan and recall rows to fill, those lessons must log their drills with kind `baseline` (the first) and `test` (later).
- Tiles: `lgErrThen` `244 wpm`; `lgErrNow` `268 wpm`; `lgVerdict` (the latest against the range); `lgGist` `3/4 = 75% → 1 = 100%`; `lgScan` `8 s → 6 s`; `lgRecall` `7/12 ≈ 58.3% → 2/3 ≈ 66.7%`.

## Deviations from PLAN §D, with reasons

1. **Number format.**
   - Values exact in two decimals print exactly (`191.25 ms`, `1.64 s`, `12.75 characters`), not as `≈` with one decimal. The reason: a reader can check an exact figure by hand, and printing `≈ 191.3` for an exact 191.25 would misstate it.
   - Rounding is half away from zero, which is the same as half up for every positive tile.
   - A share whose fraction has more than 4 digits prints the percent only.
2. **eyFixPerWord** prints the fraction with its decimal (`15/17 ≈ 0.9 fixations`), so the model's arithmetic shows.
3. **drVerdictB** compares rate B, not effective rate B, with the baseline range, because the range is built from baseline rates. It reads the range from the boxes, from the log at load when the boxes are empty, or from the `rdUseBase` button.
4. **compare** has no `chars` inputs and no standard-word tile, to stay within the page budget. `baseLo` and `baseHi` are inputs.
5. **ladder** follows D.3.6, and `drTopErr` names the target in brackets.
6. **eye/required** has a claim variant (`claim: True`: words, seconds and comprehension instead of a target) for the "a novel an hour" lessons. eye/lines adds `eySweepTime` and `eyTotal`. The budget split and lines views are kept, although D.3.10 drops them from §C.
7. **flash/span** is partial report as D.3.8 asks. The `typed` notation (`.` for not asked) keeps one input for both whole and partial report, and `flEdge` pools both outermost positions. `flErrors` is added to Schulte.
8. **scan.**
   - find has a `targets` input and a `scWrong` tile.
   - "Structural targets" for inspect are the passage's questions after a time-limited look.
   - scan and coverage log as `other` by default.
9. **triage** rates (read, skim, coverage) are inputs, not cfg, so a lesson can show the effect of a faster skim.
10. **text.**
    - Readability counts body paragraphs only (headings are not sentences).
    - The sentence rule allows closing quotes or brackets after the end mark.
    - `txSyllables` carries "(by the rule)".
11. **recall/delayed** has no `immA`/`immB` inputs, because D.3.9 removes the immediate test. Its tiles are `reDelayedA`, `reDelayedB`, `reDelayedDiff` and `reRecallB`, and `days` is a cfg key.
12. **log/noise** keeps `lgMean` and `lgBeyond` beside D.3.3's `lgRange`, `lgTestMedian` and `lgVerdict`. `lgBeyond` is about the latest test.
13. **The log** also records `mode`, `side`, `chars`, `due` and `url`. The lesson slug is `cfg["lesson"]`, or the page path's last segment. D.0 says only log views and delayed recall read the log; under D.3 the practice pool, `sinceTest`/`pacerLog`, the warm-up pool, the compare baseline range and order, and the due banner on every page also read it at load. None of them starts anything.
14. **Aloud fallback** (D.3.13) writes the published figure (side cfg `published`, default 183) into the boxes, labelled and not logged. "Brysbaert 2019" is named in the label.
15. **The attention tick** is a single box, "My attention left the text at some point" (`extra.lapse`, true or false), rather than a lapse count.
16. **practice.**
    - `drNextTarget` is defined on the run of readings at the latest target (see practice above).
    - `drTestDue` needs an input (`sinceTest`), because tiles come from inputs only. The page fills it from the log.
17. **Questions per passage** are 4 to 6. The bank gives 6. Nothing counts on 5 or 6: every count comes from the passage.
18. **Passage `band`** also accepts `mixed`, and `kind` also accepts `document`, for the scanning and inspection texts.
19. **Pages carry no `<style>` element.** Styles are inline, using the site's tokens (`--line-strong`, `--cyan`).

## Proposed PLAN edits (not made)

- D.0 Number format: state the rule as implemented (exact to two decimals, else `≈` and one decimal; the long-fraction share prints the percent only).
- D.0 The log: list every reader of the log (item 13 above) and the entry fields as implemented.
- D.1 recall/delayed: drop `immA` and `immB`; name the tiles `reDelayedA`, `reDelayedB`, `reDelayedDiff` and `reRecallB`.
- D.1 scan/find: add the `targets` input and `scWrong`; say that inspect asks the passage's questions.
- D.3.4 Pool size: the 30-passage pool gives a 78.6 KB page against the 67 KB ceiling. A page fits about 20 pool passages (64.4 KB). Either split the Daily Drill pool across two lessons (Q01–Q15 and Q16–Q30), or ship 20 per page.
- D.3.5 Warm-up and budget: a warm-up adds about 1.8 KB gzipped per passage. A ladder (≈ 44 KB with bank-length passages) plus a warm-up reaches about 45.9 KB, so say "no warm-up on a ladder or three-passage page".
- D.3.4: define `drNextTarget` as implemented, and state the 4-session rule for `drTestDue`.
- D.3.13: add Brysbaert (2019), 183 wpm aloud, to §S if it is not there; the label cites it.
- D.3.2 / profile: say that the skim, scan and recall drills whose figures feed `log/profile` must be logged as `baseline`/`test`.

## Verification

**labcheck.** The demo package is outside the repo, at /tmp/claude-0/-home-claude/291ed4a3-3972-5b4f-bb6a-9013cbbfacc9/scratchpad/kitdemo/readdemo. It has 42 lessons, one per view and display, including warm-up, order, partial report, stdwpm and noise tiers, with hand-computed expectations. It was rendered with `preview_subject.py` and checked with `node scripts/labcheck.js --expect`: 42 pages executed and swept, 42 with pinned figures, 0 failing.

**Page weight** (gzip -9 of the whole rendered page).
- Demo pages: median 36.0 KB, maximum 40.5 KB (compare-rsvp).
- With bank-length passages (480 words, six questions): median 39.1 KB; compare 43.2 KB; ladder 44.0 KB (the heaviest under 45 KB); practice with an 8-passage pool 50.3 KB.
- With the real pool: 20 passages give 64.4 KB, and all 30 give 78.6 KB.
- Only the active mode's JS ships. The timed, recall and find engines ship only where a slot uses them, and `ideas` only for free recall.

**mathcheck.** `node scripts/mathcheck.js` passes in full ("every arithmetic assertion passes"). The readkit block has 147 cases, one per formula and edge, including the eye/budget figure from the brief: (225, 30, 8, 3/20, 6) gives 15/17 fixations per word, 225 ms per word and ≈ 266.7 wpm.

**Break on purpose.** Each formula line was broken once, by 116 single-line mutations of the kit source (wrong operand, wrong comparison, an off-by-one slice, a dropped term). After each mutation the readkit block was run and the source restored and hash-checked. Every one of the 116 made a case fail. A first run found 11 survivors, and a case was added for each:
- syllables with y;
- a ladder exact tie;
- `drHoldOf` using the first three readings rather than the last three;
- `drHoldOf` keeping the first passing target rather than the fastest;
- 8 characters exactly;
- a wrong typed letter;
- an accuracy of exactly 1/2;
- found < targets;
- reMinutes;
- a test row with 2 sessions;
- the word-character class.

After the D.3 changes, three more survivors got cases: accuracy over asked rather than over all strings, the median of the last three tests rather than of all, and history's three baselines.

The scripts are in /tmp/claude-0/-home-claude/291ed4a3-3972-5b4f-bb6a-9013cbbfacc9/scratchpad/mutate: mutate.py, and the log in mutation-log.txt.

**Real browser.** Playwright with Chromium, against the served demo site, using Playwright's clock so the timed drills run on a controlled clock. The script is /tmp/claude-0/-home-claude/291ed4a3-3972-5b4f-bb6a-9013cbbfacc9/scratchpad/pw/drills.js. All 521 checks pass. They cover:
- **every display and drill view:** Start, Done, questions, Score, with the passage hidden during every question, the tiles filled and one log entry with its kind;
- **displays that end by themselves:** RSVP, phrases, pacer, mask, gist and inspect; the pacer lights a line and the mask hides lines;
- **timing:** the preview clock runs through both parts; a target above 600 wpm is refused for RSVP;
- **compare:** order BA moves box B up and is recorded; the baseline range is filled from the log; the aloud fallback writes 183 wpm and logs nothing; the suppression and attention ticks are stored;
- **sections:** the split is logged;
- **practice:** the pool serves unread passages; `drHold`, `drNextTarget` and `drTestDue` fill; the pool-exhausted message shows; pasted text and the test tick work;
- **warm-up:** it serves its list in order and is replaced by a due test;
- **flash and Schulte:** partial report by mouse and keyboard, with the measured time printed; Schulte with a wrong click;
- **scan and coverage:** scan by mouse, Enter and an arrow key; coverage marking and unmarking by mouse, Enter and Space;
- **text:** counting the reader's own text;
- **triage:** the choice buttons;
- **recall:** free recall; the delayed reread and recall sides, then the not-yet-due message, the due banner on another page, the 12-question delayed test, and no second offer;
- **log history:** baseline and test entries only, practice in the lighter series, notes, CSV export, clear after confirmation;
- **every page:** no console errors or page errors; no horizontal overflow at 360 px, on all 42 pages and while RSVP, mask and Schulte run.

**Unit tests.** `python3 -m unittest tests.test_canvas_contract tests.test_browser_source` reports `Ran 5 tests … OK`.
