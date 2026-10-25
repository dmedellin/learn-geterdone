# phenkit, the Phenomenology of Perception kit: report

Built to `docs/phenomenology/PLAN.md` §D (D.0, D.1, D.3), on the model of capkit
(`docs/capital/kit-a-report.md`). An author configures a lesson's lab from this
report alone. Every example string below was read off a rendered page with
`node scripts/labcheck.js --observe`, never copied from the code.

## Files changed (nothing committed)

- `scripts/mathpath/labs/phenkit_core.py` (new, 39 KB). It holds the shared JS:
  - `PH_CORE_JS`: phNum, phQty, phDeg, phFixed, phApprox, phPct, phAngle, phAngleText, phDir, phRead, phNames, phTable, phRefuse and phSvg;
  - `PH_WIRE_JS`: the page wiring.

  It also holds the Python build-time mirror of the parser (`parse`, `to_text`), `presets` and `mode_lab`.
- `scripts/mathpath/labs/phenkit.py` (new, 83 KB). Fifteen modes. Each has a field table, a view table and one pure `<xx>Compute(view, inst, opts)`. The entry point is `phenkit_lab(cfg)`. It is under 150 KB, so it is not split.
- `scripts/mathpath/labs/__init__.py`: `phenkit` is in the import list, and `"phenkit": phenkit.phenkit_lab` is in REGISTRY. It is **not** in `KITS_WITH_EXPECTATIONS`.
- `scripts/mathcheck.js`: a new block `// ---- phenkit ----` … `// ---- end phenkit ----` sits just before THE VERDICT. It has its own vm context: RATIONAL_JS, PH_CORE_JS and all fifteen mode blocks. It holds 182 assertions, including a PH_WIRE_JS run on a fake DOM.

## Conventions as implemented

- **cfg keys (every view).**
  - The common keys: `mode`, `view` (default: the mode's first view), `presets`, `preset` (default: the first), `title`, `panel_title`, `panel_intro` and `model`.
  - `model` names the model the view computes. It is printed in the status sentence and in the default `panel_intro`.
  - The defaults by family:
    - family 1 names its model ("the constancy hypothesis …");
    - family 2 says "the lesson's coding";
    - family 3, and `perspective/own`, say "the lesson's model".
  - Mode-specific keys: `unit` (schema habitual, tool and obstacle; depth; motion), `allowed` (perspective/own), `accounts` and `pair` (cases), `step` and `cue_text` (cues/sequence), `period` (level), `vertex` (triangle).
  - **Any other cfg key is refused at build time.**
- **Inputs.** Each input is a text box with id `<prefix>In<CamelField>`, for example `szInStandardDistance`. Records are written `a, 1, 2; b, 3, 4`. Lists are comma- or space-separated; a list of names is comma-separated only. No name may contain `, ; : = < > &` or quotes.
- **Shipped elements.** The preset menu is `<prefix>Preset`, the banner `<prefix>Status` and the table `<prefix>Table`. Views that draw have `<prefix>Figure`: grouping, necker, level, triangle, time/diagram and time/ekstasis.
- **Redraw-only controls.** There are four. A preset never sets one, and the preset menu's change handler never touches one (the mathcheck wiring case checks this).

  | control | id | values | shipped from |
  | --- | --- | --- | --- |
  | range | `cuStep` | 1 to the longest cue list in the lesson's presets (computed at build time) | cfg `step`, default that maximum |
  | select | `caPair` | `0-1`, `0-2`, `1-2`: the cfg's account pairs, one option with two accounts | cfg `pair` (two account names), default the first two |
  | range | `lePeriod` | 1 to 10 | cfg `period`, default 1 |
  | select | `trVertex` | A, B, C | cfg `vertex`, default C |

- **Exact.** Every tile is a reduced rational over BigInt, with the minus sign U+2212.
  - A decimal beside an exact figure is marked `≈`, or `=` when the decimal is exact: `13/100 = 0.1300 rad`, `13/120 ≈ 0.1083 rad`. A whole number prints alone: `0 rad`.
  - A percentage has one decimal: `47/51 ≈ 92.2%`, `1 = 100%`, `0 = 0%`.
  - The Pythagorean angles are D.0's list, with their printed degree figures stored as D.0 gives them: `3-4-5: cos 4/5, ≈ 36.87°`.
  - Floats appear only in SVG pixels, and in szDegrees, a π conversion marked `≈`.
- **Hostile input.** Every box survives `''`, `banana`, `0`, `-1`, `1/0` and `A>B`. A refused value paints a red banner and blanks every tile to `—`. A script checked every box × value on all 43 harness labs and found no throw, and every refusal was red with blank tiles.

  Some of those values are valid input and are computed rather than refused:
  - `0` or `-1` as a magnitude, reported difference, tilt, observer position, offset or reach;
  - `banana` as a word list or a letter pattern;
  - `''` in an optional field: context, assumed, a tool's objects, openings.
- **Build-time refusals.** Each raises ValueError naming the preset. 28 of them were each seen to raise:
  - an unknown mode or view, or an unknown cfg key;
  - a preset key that is not an input of its view;
  - a preset that sets a redraw-only or lesson-level key (`accounts`, `period`, `vertex`, `step`, `unit`, `model`, …);
  - a size limit exceeded (16 dots, 40 words, 8 candidates, 6 cues, 6 views, 10 variants, 10 observations, 6 objects, 8 rocks, 12 samples, 6 surfaces, 9 parcels or moments);
  - any malformed value: a view direction of non-whole length, an angle off the list, a cell other than y/n/-, the wrong number of cells, a lightness above 10, `<` or `>` in a value;
  - `accounts` that are not 2 or 3 names, or a bad `pair`;
  - `step` or `period` out of range, a bad `vertex` or `unit`;
  - an `own` preset view outside cfg `allowed`;
  - a duplicate preset id, a missing required field, or markup in `model`, `title`, `panel_title` or `panel_intro`.
- **Preset values** may be strings (taken as typed), numbers, Fractions or lists. A list record may be a list of parts, and a part that is itself a list is joined by spaces.
- **Page weight.** Only the active mode's JS is emitted. On the harness pages (a Capital lesson's prose with a phenkit lab) a lesson is 34.6 / 35.2 / 37.7 KB gzipped (min / median / max; the max is the perspective lesson). The lab alone is 8.5 to 11.4 KB gzipped; capkit's is 7.6 KB. The budget is 40 KB.

## Modes, views, fields, tiles

Each field is listed as `key` (kind, default), with — meaning the field is required. Each example tile is from a rendered page.

**stimulus** (`st`, family 1, default model "the model named above")
- `illusion`. Fields: `a` (≥ 0, —), `b` (≥ 0, —), `unit` (mm|cm|m|km, cm), `reported` (signed, —). Tiles:
  - stPredicted = a − b, `0 cm`;
  - stReported, `2 cm`;
  - stGap = reported − predicted, `2 cm` (`−3 cm` when negative).

**grouping** (`gr`, 1, "the Gestalt proximity rule (Wertheimer, 1923)")
- `proximity`. Fields: `points` (2–16 numbers, —), `ratio` (> 0, 2). Tiles: grGaps `1, 3, 1, 3, 1`, grGroups `{0, 1} {4, 5} {8, 9}`, grCount `3`. The shift preset gives `{0, 1} {4} {6} {8, 9}` and `4`. Draws a strip of dots coloured by group. Refuses two dots at one position.

**cues** (`cu`, 1)
- `pattern`. Fields:
  - `words` (1–40, `word` or `word:tag`, unique, —);
  - `pattern` (letters and `_`, —);
  - `context` (a tag or empty, "").

  Tiles: cuCount `2`, cuCandidates `house, horse` (list order), cuContext `door`, or `—` when there is no context. Refuses a context no word carries.
- `sequence`. Fields: `candidates` (1–8 records `name, cue1 cue2 …`, —), `cues` (1–6 ids, —). It also takes cfg `cue_text` {id: sentence}, shown in the table, and the `cuStep` range. Tiles:
  - cuCount `2`;
  - cuCandidates `trees at the forest’s edge, masts and funnel of a ship`;
  - cuRemoved `none` / `trees at the forest’s edge`.

  A step past the instance's cues is clamped. The banner then begins "Step 3 is past this instance's 2 cues, so the lab shows step 2." Refuses a cue that no candidate lists.

**size** (`sz`, 1, "geometric optics")
- `angle`. Fields: `size` (> 0), `distance` (> 0), `unit` (cm). Tiles: szRatio `1737/192200 ≈ 0.0090 rad`, szDegrees `≈ 0.52°`. A 7 mm disc at 770 mm gives `1/110 ≈ 0.0091 rad`.
- `constancy`. Fields: `size`, `distance`, `standard_distance` (> 0), `assumed` (empty = the true distance), `reported` (≥ 0), `unit`. Tiles:
  - szRetinal `85/2 cm`;
  - szInferred `170 cm`, or `85 cm` when 4 m is assumed;
  - szBrunswik `47/51 ≈ 92.2%`, `0 = 0%` or `1 = 100%`.

  Refused at run time when distance = standard distance.

**perspective** (`pe`)
- `faces` (family 1, "parallel projection"). Fields:
  - `object`: `cube` or `box W D H` (width, depth, height); default cube. It only names the object, since the tiles do not depend on it.
  - `views`: 1–6 records `direction[, name[, reported faces]]`. A direction is front, back, right, left, above, below, or `x y z` of whole length with each component ≤ 20. A name defaults to the direction text.

  Faces print in the order front, back, right, left, above, below. Tiles:
  - peVisible `front-right-above: front 2/3, right 1/3, above 2/3; back-left-above: back 2/3, left 2/3, above 1/3; front: front 1`;
  - peUnion `5 of 6`;
  - peMax `3`;
  - peCover `east, west (2 views)`;
  - peConsistent `yes`, `no: front-right-above (below)`, or `—` when no view reports.

  Refuses two views of one name, or a report that is not a face.
- `own` (family 3, "the lesson's model"). Fields as `faces`, plus cfg `allowed` (a list of directions; it is enforced at build time and run time when given). Tiles: peUnion `4 of 6`, peUnseen `back, below` (`none` when every face is seen).
- `necker` (family 1). Fields:
  - `object`: `wire cube`, `wire box W D H`, `solid cube` or `solid box W D H`; required.
  - `offset` k: a rational in [−2, 2], default `1/2`.

  Tiles: peEdges `12` (the solid cube gives `9`), peReadings `2` / `1`, peSame `identical drawings` / `different drawings`. Draws A's and B's drawings side by side.

**variation** (`vr`, family 2, "the lesson's coding")
- `core`. Fields: `variants`, 1–10 records `name, yes|no, prop1 prop2 …`; properties are space-separated words, hyphenated when they have several words. Tiles:
  - vrCore `letter-shapes, stroke-order, rhythm`, or `none`;
  - vrVary `fingers, arm, left-hand, leg`;
  - vrBreak `tracing lacks rhythm`, `smile in pleasure lacks none of the core`, or `no variant is marked no`.

  Refuses a set with no yes variant.

**cases** (`ca`, 2)
- `table`. cfg `accounts` holds 2 or 3 names (required) and cfg `pair` holds two of them. Field: `observations`, 1–10 records `name, cell, cell[, cell]`, one cell per account, each `y`, `n` or `-`. Tiles:
  - caRecord `empiricism: absorbs 1 of 4, fails 3, silent 0; intellectualism: absorbs 1 of 4, fails 3, silent 0`;
  - caSurvivors `none`, or `the physiological explanation`;
  - caSplit: observations where the pair is y against n, in list order, e.g. `the misprinted word, the ship on the beach`, or `none`.

  The table colours the cells y, n and -.

**schema** (`sc`, family 3)
- `coordinates`. Fields: `body` (one record `x, y, facing`; the facing is an angle name or east/north/west/south), `objects` (1–6 records `name, x, y[, body|objective]`). Tiles:
  - scRoom `cup (2, 1)`;
  - scBody `cup ahead 2, left 1` (or `ahead 1, right 2`, `behind 2, right 1`);
  - scFrame `nose: given as a position in objective space: converted to ahead 1/10, left 0` and `handkerchief: given in the body's situation: no conversion`, or `no object has a given frame`.

  Several objects are joined by `; `. The banner prints the facing as `north (90): cos 0, 90°`.
- `habitual`. Fields: `habitual_reach` and `present_reach` (`70`, or `left 70, right 0`), `objects` (1–8 `name, left|right, distance`). It takes cfg `unit`. Tiles: scHabitual `cup`, scPresent `none`, scAppeal `cup`. A reach includes its own distance.
- `tool`. Fields: `reach` (—), `tool` (0), `height` (0), `clearance` (0), `objects` (0–8 `name, distance`, ""), `openings` (0–4 numbers, ""), and cfg `unit`. Tiles:
  - scReach `170 cm`;
  - scWithin `kerb`;
  - scClears `clears by 5 cm`, `does not clear by 10 cm`, `200 cm: clears by 20 cm; 170 cm: does not clear by 10 cm` for several openings, or `no opening`.
- `obstacle`. Fields: `rocks` (1–8 heights), `project` (climb|pass|none), `capacity`, `general_level`, and cfg `unit`. Tiles: scProject `3 m` (always `none` unless the project is climb), scLevel `3 m`. Strictly taller.

**sorting** (`so`, 3)
- `sort`. Fields: `samples` (2–12 `name, hue, lightness 0–10`), `start` (a sample's name). Tiles:
  - soCategorical `red: pale red, mid red, dark red; green: pale green, mid green; brown: brown, dark brown`;
  - soChain `pale red → pale green → mid red → mid green → dark red → brown → dark brown`;
  - soPart `pale green`, or `none`.

  Refuses an unknown start.

**level** (`le`, 3)
- `tilt`. Fields: `image` (degrees in [−180, 180], −180 is read as 180), `level` (0), `rule` (switch|share), `at` (whole, 2), `share` (0–1, 1/2), and the `lePeriod` range. Tiles:
  - lePerceived (image − level, normalised to (−180, 180], at the period shown) `45°`;
  - leLevel `0°`;
  - leSeries `45°, 45°, 0°, 0°, 0°`; Stratton gives `180°, 90°, 45°, 45/2°, 45/4°`.

  Draws the room as imaged, with the level dashed. Refuses `at` below 2 under switch.

**depth** (`de`, 1, "the classical theory of depth from signs")
- `binocular`. Fields: `iod`, `near`, `far` (> 0), and cfg `unit`. Tiles: deConvergence `50 cm: 13/100 = 0.1300 rad; 60 cm: 13/120 ≈ 0.1083 rad`, deDisparity `13/600 ≈ 0.0217 rad` (`13/51000 ≈ 0.0003 rad`, `0 rad`). Refuses near > far.

**motion** (`mo`, 1, "Wertheimer's bands, as later textbooks report them")
- `phi`. Fields: `separation`, `interval` (ms), `simultaneous` (30), `succession` (200), and cfg `unit`. Tiles: moSpeed `1/12 cm per ms`, moBand `seen together` | `motion` | `seen in succession`. Both thresholds count as motion. Refuses simultaneous > succession.

**light** (`li`, 1)
- `ratio`. Fields: `surfaces` (1–6 `name, reflectance 0–1, illumination`), `surround` (a surface name). Tiles:
  - liLuminance `white paper 4/5, black disc 1/20, wall 1/2`;
  - liRatio `white paper 8/5, black disc 1/10, wall 1`, or `black disc 1/16, paper in the beam 1`;
  - liBrightest `white paper, black disc` (ties in list order).

  Refuses an unknown surround, or one with luminance 0.

**triangle** (`tr`, 3)
- `parallel`. Fields: `a`, `b` (degrees), and the `trVertex` select. Tiles:
  - trC `50°`;
  - trAlternate `60° and 70°` at C, `70° and 50°` at A, `60° and 50°` at B;
  - trStraight `60° + 50° + 70° = 180°`, with the sum computed.

  Refused at run time unless 0 < a, 0 < b and a + b < 180. The `refuse` preset pins `trC: "—"`. Draws the triangle and the parallel.

**time** (`ti`, 3)
- `river`. Fields: `parcels` (1–9 `name, position`), `observer` (a number or `none`), `standpoint` (bank|current, default bank). Tiles: tiWorld `w1 at 1, w2 at 2, …`, tiPast `w5, w6, w7`, tiFuture `w1, w2, w3`; with no observer, both are `none`.
- `diagram`. Fields: `moments` (1–9 names), `present`, `protention` (0). Tiles: tiRetained `A at depth 2, B at depth 1`, tiProtended `D, E`, tiColumn `C, B′, A′′`. Draws the line of nows, the obliques and the vertical.
- `ekstasis`. Fields: `moments`, `presents` (distinct moments). Tiles:
  - tiColumns `B: A 1; C: A 2, B 1; D: A 3, B 2, C 1`;
  - tiDepths `A: 1, 2, 3; B: 1, 2; C: 1`;
  - tiOrder `the order A, B, C is the same in every column`.

## Verification

- **Harness.** All of it is in `/tmp/claude-0/-home-claude/077dbf62-e1a1-5aba-b15b-1df7e091edab/scratchpad/phenkit/`.
  - `cfgs.py` holds every §C instance of every phenkit lesson (42 pages, with all ten `cases` tables) plus one three-account table, each with expectations written by hand from §C's Worked lines.
  - `build.py` renders each through `render.lesson_page_with_lab`, borrowing a Capital lesson's prose.
  - `labcheck.js --expect`: 43 pages swept, 43 pinned, 0 failing. Plain `labcheck.js`: 0 failing. `--observe` ran on every page.
  - The only hand expectation that disagreed was my own wrong one for the three-account pair.
- **Other checks.**
  - `hostile.js` runs every box × every hostile value.
  - `status.js` prints every preset's banner.
  - `refusals.py` checks 28 of 28 build refusals.
  - `svgs.js` / `raster.py` check that no figure has NaN, and give a montage of the figures (looked at).
- **mathcheck.** The file passes in full, with 182 phenkit assertions.
- **Mutation testing.** `mutate.py` plus `mutate2.py` broke 137 distinct lines, covering every Compute function, every helper, the parser, the angle table and the wiring.
  - 126 were killed on the first pass. I added cases for nine survivors: pos refusing 0, nn refusing a negative, the box dimension order, the reported sign, both habitual-reach edges, the cost of a hue change, chain from the last pick, and no observer. All nine were then killed.
  - Two survivors are equivalent mutants, unobservable in output:
    - `>` vs `>=` on solid faces: an edge-on face only arises at offset 0, where its edges are degenerate or coincide with drawn ones;
    - trStraight printing a literal `= 180°`: the computed sum is always 180 for any triangle the lab accepts.
  - Every restore was hash-checked. Logs: `mutation-log.txt`, `mutation-log-2.txt`.
- **Tests.** `python3 -m unittest tests.test_site_invariants -k Lab` runs 7 tests, all OK. The full `python3 -m unittest discover -s tests -p test_site_invariants.py` runs 101 tests, all OK.

## Deviations from §D, each decided and implemented

1. **cuCandidates.** D.1's example `horse, house` contradicts its own rule "in list order". With §C's list (house first), the kit prints `house, horse`.
2. **`unit`.** It is an input box for stimulus and size, because size/angle's presets change unit: km for the moon, mm for the disc. It is restricted to mm, cm, m and km so that `banana` reddens. Elsewhere it is a cfg key, default cm.
3. **`=` and `≈`.** `≈` is printed only when the decimal is inexact: `0 = 0%`, `1 = 100%`, `13/100 = 0.1300 rad`.
4. **variation records.** They are `name, yes|no, props`, because D.1's `name: p1 …; kind yes` collides with `;` as the record separator.
5. **perspective views.** They are `direction[, name[, reports]]`, with the direction first so that the optional parts trail. One canonical face order is used, since §C lists faces in varying orders. Box dimensions are W D H. peUnion prints only the count; the banner names the faces.
6. **own.** `own` is family 3 and takes the optional cfg `allowed`, which implements "restricted to the list the lesson gives".
7. **necker.**
   - It also accepts `solid box`.
   - The offset is limited to [−2, 2] for drawing.
   - Edges are counted as distinct non-degenerate projected segments, so a wire cube at offset 0 gives `4`.
8. **cases.** The observation names may not contain commas (two §C-style names in the harness needed rewording). cfg `pair` takes account names.
9. **cues/sequence.** A cue that no candidate lists is refused, as a typo guard. §C's "pins the count at steps 2 and 3" is met through the clamp: the shipped step is 3, ship clamps to 2, and hull shows 3.
10. **level.**
    - `at` ≥ 2, since D.1 says period 1 is the starting level.
    - `share` moves along the normalised difference, the short way round.
    - §C's "pins at periods 1 and 3" cannot be met with one shipped period (AGENTS rule 6), so pin leSeries.
11. **schema.**
    - Facing takes compass words besides the angle names.
    - scFrame without frames prints `no object has a given frame`.
    - tool objects are named.
    - `openings` is a list, and each opening is reported when there is more than one.
12. **time/diagram.** Protended moments come from the moments listed, and the banner says when the list runs out. §C's `span` therefore lists A–E.
13. **time/ekstasis.** tiOrder compares each column with the longest one. Under this model no column can break the order; the breaking branch is reachable through `tiOrderOf` and is tested there.
14. **Run-time refusals.** size/constancy's equal distances and triangle's impossible angles are refused when the page runs, not at build time, so that a preset can show the refusal, as §C's `refuse` preset needs.
15. **New cfg keys.** `model` (every view), `cue_text`, `allowed` and `pair` are new. D.1 names no key for these values.
