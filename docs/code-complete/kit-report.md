# cckit (Code Complete, Read Along): kit report

Lesson authors configure a lab from this report alone. It records the kit as
built to `docs/code-complete/PLAN.md` §D (D.0 to D.3). Every example tile
string below was read off a rendered page with
`node scripts/labcheck.js --observe`; none was copied from the code. Where the
kit differs from §D, the "Deviations" section says how and why. Where it
differs from the reference model `ccref.py` (§D.4), the "Model disagreements"
section says which one is right.

## Files (nothing committed)

- `scripts/mathpath/labs/cckit_core.py` (57 KB): the shared parts.
  - `CC_CORE_JS` ships on every page. It holds the printing (ccInt, ccNum, ccPct, ccRange, ccTimes, ccTimesRange, ccNames, ccCount), the parsing (ccRead and the field kinds), ccTableHtml, and the listing with its gutter (ccListing, ccFlag).
  - `CC_LEX_JS` ships only in `code` mode: the tokenizer, brace depths, the header finder and the statement reader (ccLex, ccDepths, ccShape, ccHeader, ccEvents, ccReadCode).
  - `CC_WIRE_JS` is the page wiring.
  - The Python side mirrors the field parser (`parse`, `to_text`), the tokenizer (`lex`, `header`) and the condition parser (`cond_vars`). It also has `presets` and `build_lab`.
- `scripts/mathpath/labs/cckit.py` (44 KB): the entry point `cckit_lab(cfg)` and the `code` mode, with its 12 views.
  - `CO_JS` is the base block. `CO_DECIDE_JS` ships only for complexity and basis. `CO_VIEW_JS[view]` holds one block per view.
  - Any other mode is dispatched to `cckit_b.mode_lab` through a lazy import.
- `scripts/mathpath/labs/cckit_b.py` (73 KB): the seven other modes. Each has a base block (`DG_JS`, `CD_JS`, `SE_JS`, `LP_JS`, `DF_JS`, `PF_JS`, `PJ_JS`) and one block per view (`DG_VIEW_JS[view]`, …).
- `scripts/mathpath/labs/__init__.py`: one import (`cckit,`) and one registry line (`"cckit": cckit.cckit_lab,`). cckit is **not** in `KITS_WITH_EXPECTATIONS`; wiring adds it.
- `scripts/mathcheck.js`: one block, `// ---- cckit (Code Complete) ----` … `// ---- end cckit ----`, just before THE VERDICT. It holds 191 assertions (187, plus 4 for the `book` key) in one vm context per mode, plus a CC_WIRE_JS run on a fake DOM.

There is no `content/code_complete/`: no tooling needed a stub. Nothing in the renderer was edited, and the kit needs nothing more from it (see "What the kit needs from the renderer").

## Conventions as implemented

**Entry point and cfg.**
- `cckit_lab(cfg)` reads `cfg["mode"]` (code, deps, cond, search, run, defects, profile or project) and `cfg["view"]`. The view defaults to the mode's first. An unknown mode or view raises, listing the valid ones.
- Keys common to every view: `mode`, `view`, `presets` (required, non-empty), `preset` (the one shown first; default the first), `title`, `panel_title`, `panel_intro`.
- **A cfg key named like one of the view's fields** supplies that field's value to every preset that does not set it. This is how a lesson states its fixed instance once: the build graph (`edges`), the late-fee table (`steps`), the valid range (`lo`, `hi`, `means`), the nominal effort, the injected defects, a shared listing for `extract`.
- **Lesson-level keys** come from the cfg and never from a preset:
  - `min_run` (dupes, 2–10, default 2);
  - `min` (names, 1–40, default 8);
  - `bands` (complexity, two whole numbers 0 < a < b, default `[5, 10]`);
  - `book` (complexity, `"code-complete"`, the default, or `"other"`; added for the Enterprise Patterns path, its PLAN §H.1). With `"other"`, `CO_BOOK_OTHER_JS` ships after the complexity block and rewrites three phrases of the banner: "McConnell's guidance on what" becomes "McConnell's guidance in Code Complete on what", "The book prints its bands" becomes "McConnell prints his bands", and the `?:` note's "not the book's" becomes "not McConnell's". No tile changes. With the default nothing ships and every page is byte-identical to before. Any other value raises. The basis view's `?:` note still says "the book's", since no lesson outside Code Complete uses basis;
  - `indent` (layout, 1–8, default 4);
  - `table` (defects/cost, required);
  - `target` (profile, a share above 0 and at most 1, default 4/5);
  - `unit` (profile, plain text, added to the time and total tile labels);
  - `tag` (profile/shares, one lower-case letter, default `c`) and `tag_label` (default `tagged`);
  - `source` (every family 3 view, optional). When given, the panel intro ends "Figures: <source>."
- Any other cfg key raises, naming the keys the view does take.
- **Families.** Every panel intro begins with its family's sentence, even when `panel_intro` overrides the rest: "A count over code, by the rules stated below the listing." (code), "A count over the structure the lesson states." (deps, cond, search, run), or "The arithmetic of figures the lesson quotes (marked with their source)." (defects, profile, project).

**Ids.**
- Prefixes: `co` code, `dg` deps, `cd` cond, `se` search, `lp` run (`nu` for arith's tiles), `df` defects, `pf` profile, `pj` project.
- An input's id is `<prefix>In<Field>`: `coInCode`, `dgInEdges`, `cdInCond`, `lpInStep`, `pjInPerWeek`, `pjInDensityLow`. `run/arith`'s inputs are `lpIn*` too.
- Each page ships a preset menu `<prefix>Preset`, a banner `<prefix>Status` and a table `<prefix>Table`. `code` views also ship the listing `coListing`.
- Every JS function and variable and every element id was grepped across `scripts/mathpath/labs/*.py`. Two names are shared with another kit, and the two never meet on one page: `lpCompute` (dekit_b.py has one) and the tile id `seValue` (argkit has one). The mathcheck blocks run in separate vm contexts.

**Inputs.**
- Every input is a text box, except code and conditions.
- Records are `a, 1, 2; b, 3, 4`. A record field is separated by commas and a record by semicolons. Lists are space- or comma-separated.
- Names (`name`) are letters, digits, `.`, `_` and `-`. Labels (`label`, used for cases, stages, entries and factors) may hold spaces but not `, ; : = < > &` or quotes.
- Words (`cmp`, `rule`, `means`, `type`, `op`, `fn`, `side`, `handling`, `access`, stages) are typed. Anything not on the list is refused, naming the list.
- **Code and conditions** go in `<textarea>`s: `coInCode` (16 rows, `wrap="off"`, monospace) and `cdInA`, `cdInB`, `cdInCond` (3 rows). These are empty in the markup and filled from the preset table at load and on a preset change, so no shipped attribute or text holds code.
- **The listing.** Beside `coInCode` the lab draws the listing in `<pre id="coListing">`.
  - The gutter of line numbers is drawn by script and is `user-select: none`, so copying the listing copies no numbers.
  - Lines count from 1, blank and comment lines included.
  - A flagged line gets a `▸` glyph and a visually hidden word in the gutter: `repeated`, `in the block`, `empty step`, `used before set`, `set twice`, `set, never used` or `mis-indented`. It is also bold, so colour is never the only signal.
  - The box and the listing are two `flex: 1 1 19.5em` columns. Below about 40em they stack. Each scrolls in its own box (the listing at most 30em high), and the page never scrolls sideways.
  - A `<details>` "How the lab reads Java" under every code view states the subset the lab reads and the view's own rule.

**Number format (D.0).**
- Whole numbers: `2,692,537`, `−1` (U+2212).
- A non-whole number prints its reduced fraction, then two decimals rounded half away from zero on the exact value, with `=` only when those decimals are exact: `7/2 = 3.50`, `28/3 ≈ 9.33`, `−29/15 ≈ −1.93`.
- Shares: `33/50 = 66%`, `31/60 ≈ 51.7%`, `1 = 100%`, `0 = 0%`.
- Ranges: `425–800`, collapsing to `35` when the ends are equal, and `2/5 = 0.40 to 5` when an end is not whole.
- Times: `85/7 ≈ 12.1× to 160/7 ≈ 22.9×`, collapsing to `1×`.
- Lists: `a, b` or `none`. A count with its list: `5: audit, backup, export, invoice, report`, or `0: none`.
- A figure past 30 digits prints `≈ 1.80 × 10^308`.
- The one exception is `nuJava`, which prints what Java prints.

**Zero denominators and divisors.**
- A tile whose denominator is zero prints `—`, and the banner says why in one sentence: coDensity, coAvgSpan, coAvgLen, dfRatio, dfPerDefect. These are never red.
- An input that is a divisor must be positive, and a zero or negative one is refused with the field named: `ratio`, `prodLow`, `prodHigh`, `perWeek`, `manual`, `nominal`, `kloc`, `size`, `factor`, `multiplier`, `injected`.
- A total used as a divisor that comes to 0 is refused with a sentence: the chain's frequencies, the shares' amounts, the speedup's times.
- `run/arith` models Java: `int` and `long` division by zero prints `ArithmeticException`. A `double` division (or `%`) by zero is refused with "Division by zero: Java would print Infinity or NaN; this lab does not model it".

**Hostile input.**
- Every box and textarea survives `''`, `banana`, `0`, `-1`, `1/0` and `A>B`.
- A refused value paints a red one-sentence banner and blanks every tile to `—`.
- `hostile.js` ran every box × value × preset on all 37 harness pages: 2,550 runs, 2,107 refused. None threw, every refusal blanked every tile, and no accepted value printed NaN, undefined or Infinity.
- Many of these values are valid input, legitimately: `0` as a count, `-1` as a loop bound, `banana` as a name or a Java listing (one statement line).

**Build-time refusals.** Each raises ValueError, naming the preset where there is one. `refusals.py` saw all 27 of these raise:
- an unknown mode or view, or an unknown cfg key;
- a preset key that is not an input of its view, or a lesson-level key set in a preset;
- a size limit exceeded: 200 lines or 120 characters a line of code, 60 edges, 40 classes, 20 records, 13 stages, 17 factors, 5 loop sizes, 5 condition variables;
- a listing the tokenizer mirror cannot read, or a `}` that closes nothing;
- `ppp` without a routine header;
- an `extract` range outside the listing;
- `span` naming a variable the listing does not contain;
- a `range` check over two variables, or a condition the mirror cannot parse;
- `truth` over more than 5 variables;
- markup (`< > &`) in any value but code and conditions;
- a word off its list;
- a missing or malformed `table`: a stage's own cell missing, or one with two values;
- a `target` outside (0, 1];
- a duplicate preset id, an expectation naming a tile the view does not show, markup in `title`, a missing required field, or a zero divisor.

**Preset values.** A value may be a string (taken as typed, so code keeps its indentation), an int, a Fraction, a float, or a list. A record field takes a list of records, each a list of parts or a string. A list field takes a list.

**Preset conventions.**
- A preset is `{id, label, <field values>, expect}`.
- The label names the instance ("Declared at the top", "MAX + 1").
- `expect` maps tile ids to the exact text printed. labcheck's gate needs at least one tile per preset, and the build refuses a tile the view does not show.
- Code presets should use the lesson's own snippet constant (§D.4, "one source for each snippet").

**Page weight.**
- A page ships RATIONAL_JS, CC_CORE_JS, CC_LEX_JS (code only), its mode's base block and its own view's block, nothing more.
- On the harness (a Phenomenology lesson's prose with a cckit lab), the lab alone is 5.3 to 11.4 KB gzipped. Code views are 10.4 to 11.4 KB, arith 8.4 KB, and the rest 5.3 to 7.6 KB.
- The whole lesson is 31.7 to 38.0 KB gzipped.
- With two code listings added to the lesson body (so `theme.CODE_CSS` ships too), the heaviest lessons (complexity, layout) are 38.0 / 38.7 / 38.9 KB (min / median / max over four donor lessons).
- That is under PLAN's 40 KB budget and well under the 67 KB ceiling. The margin is about 1 KB, so a code lesson whose prose runs much longer than a Phenomenology lesson should be measured.

## Modes, views, fields, tiles

Each field is listed as `key` (kind, default), where — means the field is required. Kinds:
- `count` is a whole number ≥ 1, and `nncount` one ≥ 0.
- `whole` is any whole number, `num` any number, `nn` one ≥ 0, `pos` one > 0, and `share` a number from 0 to 1.
- `name`, `label` and `word` are as above.
- `rec` is records, and `list` a list.

Tiles are listed as id, label, then an example.

### code (`co`, family 1)

Every view has one field, `code` (the Java listing, —), drawn as the numbered listing. The rules the lab reads by are stated under it (PLAN D.1 "the subset"). A listing that the tokenizer cannot read is refused, naming the line: an unclosed string, a character outside the subset, or a `}` that closes nothing.

- **size.** Tiles:
  - coLines, Lines, `10`;
  - coCode, Code lines (braces included), `9`;
  - coStatements, Statement lines, `8`;
  - coComment, Comment lines, `1`;
  - coBlank, Blank lines, `0`;
  - coParams, Parameters, `9` (a fragment: `none (a fragment)`);
  - coDensity, Comment lines per statement line, `1/8 = 12.5%` (`—` with no statement lines).

  The empty listing gives 0, 0, 0, 0, 0, `none (a fragment)`, `—` and is not refused.
- **class.** Tiles:
  - coFields, Fields, `5`;
  - coPublicFields, Public fields (not final), `5`;
  - coRoutines, Routines, `2`;
  - coPublicRoutines, Public routines, `2`.

  On class-private: 5, 0, 4, 3.
- **dupes.** cfg `min_run`. Tiles:
  - coDupBlocks, Repeated blocks, `1`;
  - coDupLines, Lines in all the copies, `6`;
  - coDupWhere, Where, `lines 3–5 and lines 7–9` (or `none`).

  The copies are flagged `repeated`.
- **extract.** Fields `code`, `from` (count ≤ 200, —) and `to` (count ≤ 200, —). Ids `coInFrom` and `coInTo`. Tiles:
  - coIn, In, `account, balance, fees`;
  - coOut, Out, `balance, fees`;
  - coParams, Parameters the routine needs, `3`;
  - coOutside, Read but set nowhere, `none`.

  Lines 11–12 of the same listing give `fees, balance`, `none`, `2`, `none`. The block's lines are flagged `in the block`. A range past the listing is refused.
- **ppp.** Tiles:
  - coSteps, Pseudocode steps, `5`;
  - coCode, Statement lines in the body, `7`;
  - coEmpty, Empty steps, `line 14` (or `none`);
  - coMaxUnder, Most code under one step, `3 lines, under line 8`.

  Empty steps are flagged. A fragment prints `none (a fragment)`.
- **dataflow.** Tiles:
  - coAnomalies, Anomalies, `3`;
  - coUsedBeforeSet, Used before set, `count (line 6)`;
  - coSetTwice, Set twice, `total (lines 2, 4), count (lines 3, 5)`;
  - coUnused, Set, never used, `average (line 6)`;
  - coDeps, Dependencies (line → line), `1→4, 1→5, 3→5, 4→5, 5→8, 6→8`.

  Each anomaly's lines are flagged.
- **span.** Fields `code` and `vars` (Java names separated by spaces, at most 12, default empty, meaning every name that is set). Id `coInVars`. Tiles:
  - coAvgSpan, Average span (lines), `16/3 ≈ 5.33`;
  - coAvgLive, Average live time (lines), `41/3 ≈ 13.67`;
  - coLongest, Longest live time, `heaviestKg: 16`.

  On span-near: `7/3 ≈ 2.33`, `23/3 ≈ 7.67`, `heaviestKg: 9`. A name the listing lacks is refused.
- **names.** cfg `min`. Tiles:
  - coNames, Declared names, `7`;
  - coAvgLen, Mean length of the counted names, `4/3 ≈ 1.33`;
  - coShort, Shorter than the lesson's minimum, `a, n, r, t, x, tmp`.

  Loop indexes are listed in the table but not counted.
- **literals.** Tiles:
  - coMagic, Magic numbers, `5`;
  - coDistinct, Distinct, `3`;
  - coMagicList, Each, with its lines, `0.0725 (line 2), 12 (lines 2, 3), 360 (lines 4, 5)`.
- **complexity.** cfg `bands` and `book`. Tiles:
  - coDecisions, Decision points, `9`;
  - coBreakdown, Breakdown, `1 + if 5 + for 1 + && 1 + || 1`;
  - coBand, Band, `6–10` (the bands print `0–5`, `6–10`, `10+`);
  - coDepth, Deepest nesting, `5`;
  - coDeepest, First line at that depth, `line 14`.

  On refund-guards: `3`, `1 + if 2`, `0–5`, `1`, `line 3`. The banner says whose guidance the bands are. `?:` adds nothing, and the banner says so when one appears.
- **basis.** Tiles:
  - coBasis, Basis test cases, `6`;
  - coNoDefault, switch with no default, `1`;
  - coPoints, Decision points, in line order, `case line 4, case line 7, case line 10, if line 14`.
- **layout.** cfg `indent`. Tiles:
  - coMisIndented, Mis-indented lines, `2`;
  - coLines, Which, `5, 6` (or `none`).

  On clamp: `1`, `6`. Mis-indented lines are flagged.

### deps (`dg`, family 2)

Edges are records of two names. A self-edge is refused. In a "largest" tile a tie goes to the alphabetically first name, and the banner names every tied one.

- **coupling.** Field `edges` (records `user, used`, 1–60, —). Id `dgInEdges`. Tiles:
  - dgModules, Modules, `5`;
  - dgEdges, Distinct uses, `7`;
  - dgPairs, Possible pairs, `10`;
  - dgConnected, Pairs connected either way, `7/10 = 70%`;
  - dgFanOut, Largest fan-out, `billing 2`;
  - dgFanIn, Largest fan-in, `db 3`.

  On everything-talks: `billing 4` for both, and the banner names all five tied modules.
- **ripple.** Fields `edges` (records `dependent, dependency`, —) and `changed` (name, —). Ids `dgInEdges` and `dgInChanged`. Tiles:
  - dgDirect, Depend on it directly, `1: store`;
  - dgAffected, Reached in all, `7: audit, backup, export, invoice, report, store, ui`.

  The table gives each reached name's distance in edges. A `changed` that no edge names is refused.
- **tree.** Field `edges` (records `child, parent`, 1–40, —). Tiles:
  - dgDepth, Deepest level (a root is 1), `7`;
  - dgDeepest, Deepest class, `ChristmasHolidaySavings`;
  - dgClasses, Classes, `8`;
  - dgLeaves, Leaves, `2`.

  On shallow: `2`, `Circle` (banner: "Circle, Square, Triangle"), `4`, `3`. Two parents, or a cycle, are refused.
- **shared.** Fields `uses` (records `routine, access, global`, with access `r`, `w` or `rw`, 1–60, —) and `owners` (`global=routine; …`, optional, default empty). Ids `dgInUses` and `dgInOwners`. Tiles:
  - dgGlobals, Globals, `3`;
  - dgRoutines, Routines, `6`;
  - dgCoupled, Coupled pairs of routines, `9` (the banner gives "of the 15 possible pairs");
  - dgMostShared, Most shared global, `current, 5 routines`;
  - dgDirectAccess, Places that touch a global directly, `10` (with owners: `3`);
  - dgWriters, Who writes each global, `current: readInput, reset; errors: reset, validate; total: addLine` (with owners: `current: currentRecord; errors: errorLog; total: runningTotal`).

  With owners the banner says access routines move the coupling behind one name and do not remove it. An owner of an unknown global is refused.
- **integrate.** Fields `edges` (records `caller, callee`, —) and `order` (names separated by spaces, every component exactly once, —). Id `dgInOrder`. Tiles:
  - dgStubs, Stubs needed, `3: db, ui, widgets`;
  - dgDrivers, Drivers needed, `2: orders, pricing`.

  The table shows each step. An order that misses a component, or names one no edge has, is refused.

### cond (`cd`, family 2)

The lab's own parser handles identifiers, `true`, `false`, `!`, `&&`, `||` and parentheses, with Java precedence. In `range` it also takes the comparisons `< <= > >= == !=` between the variable and a whole number, on either side. Nothing is evaluated as script.

- **truth.** Fields `a` and `b` (conditions, —), in textareas `cdInA` and `cdInB`. Tiles:
  - cdAtoms, Variables, `2`;
  - cdRows, Rows, `4`;
  - cdTrueA, Rows where A is true, `1`;
  - cdTrueB, Rows where B is true, `3`;
  - cdEquivalent, Equivalent, `no, on 2 of 4 rows` (or `yes`);
  - cdFirstDiff, First row that differs, `done = T, error = F` (or `none`).

  The table has every row, T before F, the first variable most significant, with an "agree / differ" column. More than 5 variables are refused.
- **range.** Fields:
  - `cond` (the check, —; textarea `cdInCond`);
  - `lo` and `hi` (whole numbers within int, —);
  - `means` (`valid` or `invalid`: what a true check says, —).

  These are often given once in the cfg. Tiles:
  - cdDisagree, Where check and range disagree, `0 and below, 13 and above`, `1 to 12`, `99`, `−1 and below, 101 and above` (or `none`);
  - cdTests, Boundary tests, `0, 1, 2, 11, 12, 13`;
  - cdExposed, Tests that expose a difference, `0, 13` (or `none`).

  The table gives each boundary test. Refused: two variables, `!` before a bare comparison (Java rejects `!x < 5`), a literal outside int, and lo > hi.
- **barricade.** Field `values` (records `value, side, handling`, with side `outside` or `inside` and handling `validate`, `assert` or `none`; 1–20, unique, —). Id `cdInValues`. Tiles:
  - cdValues, Values, `6`;
  - cdOutsideUnchecked, Outside, unchecked, `1: uploadName`;
  - cdOutsideAsserted, Outside, only asserted, `1: feedPrice`;
  - cdInsideUnchecked, Inside, unchecked, `1: customerId`;
  - cdInsideValidated, Inside, validated, `0: none` (checks-everywhere: `3: lineTotal, customerId, taxRate`).

  Names are in record order. The banner states the chapter's rule and that the tiles are not a verdict.

### search (`se`, family 2)

- **chain.** Field `cases` (records `case, frequency`, with case a label and frequency ≥ 0; 1–20, unique, —). A last case named `else` is the final else. Id `seInCases`. Tiles:
  - seExpected, Expected tests as written, `7/2 = 3.50`;
  - seBest, Expected tests, best order, `3/2 = 1.50`;
  - seSaved, Saved per case, `2`.

  On else-is-common: `14/5 = 2.80`, `13/5 = 2.60`, `1/5 = 0.20`. The banner names the best order and says that reordering is valid only for mutually exclusive conditions. An `else` that is not last is refused, and so are frequencies that total 0.
- **stairs.** Fields:
  - `steps` (records `bound, value`, with value a label; 1–60; bounds strictly rising; —);
  - `key` (number, —);
  - `rule` (`below` or `atmost`, default `below`).

  Ids `seInSteps`, `seInKey` and `seInRule`. Tiles:
  - seValue, Value, `5`, `70%` (or `above the table`);
  - seLinear, Tests, linear search, `3`;
  - seBinary, Tests, binary search, `2`.

  The table marks the linear tests and each binary probe.
- **bisect.** Fields `n` and `k` (counts up to 10^12, with k ≤ n, —). Tiles:
  - seSteps, Steps to find it, `10`;
  - seWorst, Most steps any position takes, `10`.

  The table lists each interval: `1–1,000`, `501–1,000`, … `636–637`.

### run (`lp`, and `nu` for arith; family 2)

- **loop.** Fields `start`, `bound` and `step` (whole numbers within int, —; the step's label reads "a negative step counts down", and a step of 0 is refused) and `cmp` (`lt le ne gt ge`, —). Tiles:
  - lpIterations, Iterations, `11`, `never ends`, `never ends without overflow`, or `overflows int after 2,147,483,648 iterations`;
  - lpLast, Last value of i in the body, `10` (`—` when the body never runs);
  - lpAfter, i after the loop, if declared before it, `11`, `−1`.

  The banner prints the loop (`for (int i = 0; i <= 10; i += 1)`). The panel says the header's index does not exist after the loop and that the book advises against relying on it.
- **nested.** Field `sizes` (a list of 1–5 counts, each ≤ 1,000,000, —). Tiles:
  - lpBody, Body runs, `500`;
  - lpIterations, Passes, as given, `600`;
  - lpBest, Passes, smallest outside, `505`;
  - lpSaved, Saved, `19/120 ≈ 15.8%`.
- **recursion.** Fields `fn` (`factorial` or `fibonacci`, —) and `n` (0–90, and factorial past 20 is refused with the reason, —). Tiles:
  - lpCalls, Calls, `2,692,537`;
  - lpDepth, Deepest call, `30`;
  - lpValue, Value, `832,040`;
  - lpLoop, Iterations of a loop, `29`.
- **arith.** Fields:
  - `type` (`int`, `long` or `double`, —);
  - `start` and `operand` (Java literals, —). An int literal must fit int; a long may end in `L`; a double is decimal or `e` form, with an optional `d`;
  - `op` (`+ - * / %`, —);
  - `times` (1–1,000, default 1).

  Tiles:
  - nuJava, Java prints, `-2147483648`, `0.9999999999999999`, `1.0E-5`, `1.0E7`, `-0.0`, `ArithmeticException`;
  - nuExact, Exact arithmetic, `2,147,483,648`, `7/2 = 3.50`, `1`;
  - nuEqual, The same?, `no` (or `yes`);
  - nuStored, The value stored, exactly, `9007199254740991/9007199254740992 ≈ 1.00`, `−2,147,483,648`.

  The panel says Java prints a double as JDK 19 and later do.

### defects (`df`, family 3)

- **cost.** cfg `table` (required). It maps a pair `(introduced, found)`, or `"req post"`, to a positive multiplier: one number, a `(low, high)` pair, or `"10-100"`. The stages are `req arch cons test post`. Each stage that introduces defects needs its own one-figure cell, the baseline. Field `defects` (records `introduced, detected, count`, 1–20, —). Id `dfInDefects`. Tiles:
  - dfCost, Cost to fix, `425–800`;
  - dfEarly, Cost had each been found where it was introduced, `35`;
  - dfRatio, How many times more, `85/7 ≈ 12.1× to 160/7 ≈ 22.9×` (found-early `1×`; with no defects `—`).

  A pair the table lacks is refused.
- **removal.** Fields `injected` (count, —) and `stages` (records `stage, rate`, with rate a share; 1–13, unique, —). Tiles:
  - dfFound, Found, `47543/50 = 950.86`;
  - dfRemaining, Remaining, `2457/50 = 49.14`;
  - dfCombined, Combined removal, `47543/50000 ≈ 95.1%`.
- **pipeline.** As removal, with a third record part `hours` (≥ 0). Tiles are as removal, plus:
  - dfHours, Hours spent, `674`;
  - dfPerDefect, Hours per defect found, `1685/208 ≈ 8.10` (`—` when nothing is found).

### profile (`pf`, family 3)

- **shares.** cfg `tag`, `tag_label`, `target` and `unit`. Field `entries` (records `name, amount` plus an optional third part equal to `tag`; 1–20, unique, —). Id `pfInEntries`. Tiles:
  - pfTotal, Total (hours), `1,000`;
  - pfTagged, Share that is construction, `33/50 = 66%`;
  - pfTop, Largest entry, `coding and debugging, 8/25 = 32%`;
  - pfPareto, Entries reaching 4/5 of the total, `6 of 8`.

  The banner reads "6 of 8 entries reach 4/5 of the total, taken largest first". A zero total is refused.
- **speedup.** cfg `target` and `unit`. Field `routines` (records `name, time, factor`, with factor ≥ 1/1000 and 1 meaning unchanged; 1–20, unique, —). Tiles:
  - pfBefore, Time before (ms), `1,000`;
  - pfAfter, Time after (ms), `17003/20 = 850.15`;
  - pfSpeedup, Speedup, `20000/17003 ≈ 1.18`;
  - pfSaved, Saved, `2997/20000 ≈ 15.0%`;
  - pfPareto, Routines reaching 4/5 of the time, `2 of 4`.

### project (`pj`, family 3)

- **language.** Fields `size` and `ratio` (pos, —). Tile pjEquivalent, Statements of the language, `5000/3 ≈ 1,666.67`. The banner says the ratio measures statements, not time, defects or experience.
- **scale.** Fields `people` (count), `kloc` (pos), `densityLow` and `densityHigh` (≥ 0), and `prodLow` and `prodHigh` (pos), all —. A reversed range is refused. Tiles:
  - pjPaths, Communication paths, `1,225`;
  - pjDefects, Defects, `4,000–100,000`;
  - pjStaffYears, Staff-years, `100 to 10000/7 ≈ 1,428.57`;
  - pjSpread, Spread of the productivity range, `100/7 ≈ 14.29`.
- **effort.** Fields `nominal` (pos, —) and `factors` (records `factor, multiplier`, with multiplier pos; 1–17, unique, —). Tiles:
  - pjProduct, Product of the multipliers, `1035213/250000 ≈ 4.14`;
  - pjEffort, Adjusted effort, `1035213/2500 ≈ 414.09`.
- **breakeven.** Fields `build` (hours, pos), `manual` (minutes, pos), `auto` (minutes, ≥ 0) and `perWeek` (pos, a fraction allowed), all —. A manual time not above auto is refused. Tiles:
  - pjRuns, Runs to pay back, `35`;
  - pjWeeks, Weeks to pay back, `7/2 = 3.50`;
  - pjYear, Hours saved in the first year, `340/3 ≈ 113.33` (rare-task `−29/15 ≈ −1.93`).

## What the kit needs from the renderer

Nothing beyond what is already there:
- `labcheck.js` already sweeps `<textarea>`s with the hostile values and counts them when it decides what a preset menu rewrites. Those hostile inputs are tested.
- The kit styles its listing inline, so it does not depend on `theme.CODE_CSS`. That stylesheet ships only when the lesson body has a `code` block.
- The page uses the existing `.visually-hidden` and `.tone-red` classes.

## Verification

- **Harness.** It is all in `/tmp/claude-0/-home-claude/3b1d3502-1b81-5554-ace3-d7f9f019031f/scratchpad/cckit/`.
  - `cfgs.py` holds every §C preset of every cckit lesson on 37 pages. The listings are taken from `presets.py`. It adds edge cases: an empty listing, the int overflow of `i <= MAX`, `-0.0`, `1e23`, a subnormal, finds-none, above the table, and a check that differs only at its literal.
  - Expectations were written by hand from §C and the model's output in D.0's format.
  - `build.py` renders each page through `render.lesson_page_with_lab`, borrowing a Phenomenology lesson, and writes `h/manifest.json`.
- **labcheck.** `node scripts/labcheck.js --expect …/h/manifest.json`: 37 pages executed and swept, 37 pinned, 0 failing. Plain `labcheck.js` on the pages: 0 failing. `--observe` ran on every page (`observe.json`).
  - Three of my hand expectations were wrong on the first run, and in each case the kit was right:
    - binary probes above the table: 2, not 3;
    - `19001/200 ≈ 95.01`: it is not exact;
    - layout-switch had no pin yet.
- **Other checks.**
  - `hostile.js`: every box × value × preset, 0 failing.
  - `status.js` printed every preset's banner, and each was read.
  - `refusals.py`: 27 of 27 build refusals raise.
  - `dbl.js` compared nuShort with JavaScript's shortest round-trip digits on 30,000 random normal doubles. Every one read back exactly, had the same digits, and switched to the `E` form at the right thresholds.
  - `perf.js`: the worst arith runs (1,000 steps) take 4–31 ms.
- **mathcheck.** `node scripts/mathcheck.js` passes in full, with 191 cckit assertions (4 of them for the `book` key, seen to fail when its rewrite was broken), every view at least once, and §C's figures as the cases.
- **Mutation testing.** `mutate.py` broke 133 lines, one at a time, in a scratch copy of the kit, covering every Compute function, the printing, the parser, the tokenizer and the wiring. The cckit block was run against each.
  - 119 were killed on the first pass. I added cases for 12 survivors: block comments, a final public field, a field initialised by a call, a name set first in a block, a code line with a comment, a name at the minimum, a band's top, a line's depth after its leading braces, the cycle's message, a loop that never starts with a negative step, a table with a baseline other than 1, and a share that reaches the target exactly. All 12 were then killed.
  - Two survivors were equivalent:
    - Evaluating at each literal c itself, besides c ± 1. The single-value gap between c − 1 and c + 1 is sampled anyway, so D.1's requirement holds either way. The line stays.
    - JDK 19's "length 1 or 2" rule. It can only matter when a normal double's rounding interval holds two different short decimals, which it is too narrow to do. Subnormals are refused, so the code was removed.
  - Final run: 131 mutants, 131 killed. The full-file run was also checked to fail on a mutation.
- **build_paths.** `python3 scripts/build_paths.py --check`: every published page matches content/ (1,098 pages).
- **tests.** `python3 -m unittest tests.test_site_invariants -k Lab`: 10 tests, all OK.

## Deviations from §D, each decided and implemented

1. **Two decimals everywhere (D.0) over §C's prose.** §C sometimes prints more or fewer places. The kit follows D.0:
   - `pjProduct` is `1349/2500 ≈ 0.54`, not `= 0.5396`;
   - `pjWeeks` is `7/2 = 3.50`;
   - `pjSpread` is `25/2 = 12.50`;
   - `pjStaffYears` is `2/5 = 0.40 to 5`.

   A small figure therefore reads `1/500 ≈ 0.00` (arith's nuExact for 0.002). The fraction carries the value.
2. **Collapsed ranges.** found-early's dfRatio prints `1×` and its dfCost `35`, where §C writes "1× to 1×" and "35, 35". D.0's collapse rule is applied to every range.
3. **Units go in labels, not tiles.** pfTotal prints `1,000` and its label reads "Total (hours)", from cfg `unit`. §C's "1,000 hours" would break D.0's number format.
4. **pfTop ties go to the first entry listed** (the record order), and the banner names the tied ones. D.1's alphabetical rule is written for `deps` only.
5. **`run/loop`: the final step can overflow.** D.1 maps `le` to `lt` with bound + 1. For `i <= 2147483647` that bound lies outside int, and the last `i += step` wraps to a value that still passes. The kit prints lpIterations `overflows int after 2,147,483,648 iterations`, lpLast the last value, and lpAfter `—`. The banner says where i wraps to and that the loop does not stop there. D.1 has no sentence for this case.
6. **nuStored is shown for every type.** For int and long it is the stored integer (`−2,147,483,648`), which is what is stored. D.1 lists it for double only.
7. **The double printer.** It is the shortest decimal in the rounding interval, the closest to the value, in Java's format: `.0` always, and the `E` form below 10⁻³ and from 10⁷. JDK 19's extra weighing of two-digit decimals is not implemented, because no normal double can be affected (see Verification).
   - `%` on doubles is modelled exactly (fmod), with the dividend's sign. A double `%` by zero is refused with the same sentence as division.
   - Signed zero is tracked: `0 * -1` prints `-0.0`.
   - The exact track stops past 400 digits a side. nuExact and nuEqual then print `—` and the banner says why.
8. **Refusals that D.1 does not list but D.0's rules imply.**
   - A zero total of frequencies, amounts or times (D.0's divisor rule).
   - A self-edge, an unknown `changed`, an owner of an unknown global, and an integration order that misses or adds a component.
   - Two parents, or a cycle (D.1 lists these).
   - Bounds that do not rise.
   - k > n.
   - A loop step of 0 (D.1 says non-zero).
   - lo > hi.
   - A reversed density or productivity range.
   - manual ≤ auto (D.1's manual > auto).
   - `!` before a bare comparison in `range`, which Java would reject.
9. **`source`, `tag`, `unit`** are optional cfg keys that D.1 does not name. `source` marks family 3's figures in the panel intro. `tag` lets a lesson use a letter other than `c`.
10. **`stairs.rule`** is an input (default `below`), because §C's presets vary it. **`range.means`, `lo` and `hi`** are inputs that the cfg can fix once (§C sets `means` in the cfg).
11. **The code subset, as built.** These were decided while building the reader, and each is stated in the listing's rules block:
    - The header is the first statement at depth 0 shaped `type name(params)`, where the model checks only the first statement.
    - Several declarators in one declaration each set or declare a name.
    - A capitalised name is a constant or type: listed in `names` and producing no events.
    - An enhanced `for` reads its collection, then sets its variable.
    - A one-line `if (c) x = 1;` is read as a condition and a statement.
    - `dupes` compares statement lines as text with white space collapsed, where the model compared tokens. The result is the same on every preset.
    - `class` reads members as statements at brace depth 1.
    - `layout` checks only the first line of a statement that runs over several lines.
    - `coDeepest` is the first statement line at the greatest depth, and depth 0 counts.
    - A `?` in generics is not a `?:`.

## Model disagreements (ccref.py, §D.4)

All §C figures agree, except the following, where the spec was right:

- **count-passing, dataflow.** The model gives 0 anomalies. The kit gives `1` with coUnused `maxScore (line 2)`. D.1 sets parameters on the header's line, so a parameter never read has a set as its last event. §C's own answer for this exercise names "the parameter maxScore (line 2) is never used". The model skipped parameters.
- **Exact `%` in arith.** The model's exact track uses Python's floor `%`, which is wrong for a negative operand. Java's `%` (and the kit's exact track) truncates: `-7 % 2` gives `-1` and exact `−1`. No §C preset has a negative `%`.
- **Double formatting.** The model prints Python's `repr` (`1e-05`). The kit prints Java's `1.0E-5`, as §D.4 anticipates.
- **dgDeepest.** The model prints every tied class (`Circle, Square, Triangle`). The kit prints `Circle` and the banner names all three, as D.1 and §C say.

## For wiring

- Add `"cckit"` to `KITS_WITH_EXPECTATIONS` last, as D.0 says.
- `code` presets should use the lesson's snippet constants.
- cfgs like those in `cfgs.py` above can be copied into the content package. `cfgs.py` holds each §C preset with its observed expectations.
