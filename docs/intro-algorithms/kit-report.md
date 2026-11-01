# itakit (Introduction to Algorithms, Read Along): kit report

Lesson authors configure a lab from this report alone. It records the kit as
built to `docs/intro-algorithms/PLAN.md` §D. Family A (growth, sorting,
recurrence, maxsub, hiring, workspan, lup, fft) is `itakit.py` and is
reported here first; family B's section follows at the end. The seam between
the two modules is `docs/intro-algorithms/kit-contract.md`. Every example tile
string in family A's section was read off a rendered page with
`node scripts/labcheck.js --observe`; none was copied from the code. The
"Deviations" section says where family A differs from §D and why.

## Files

- `scripts/mathpath/labs/itakit.py`: the entry point `itakit_lab(cfg)`,
  `mode_lab(cfg, mode, spec)` (shared with family B), `ITA_CORE_JS` (shipped
  on every itakit page: `itaQ`, `itaList`, `itaApprox`, `itaLg`, `itaLgCmp`,
  `itaLgMid`), and family A's eight modes: a base block (`GRI_JS`, `STI_JS`,
  `RCI_JS`, `MSI_JS`, `HRI_JS`, `WSI_JS`, `LUI_JS`, `FTI_JS`) and one block
  per view (`GRI_VIEW_JS["race"]`, …), with the Python `check` of every view
  that refuses anything beyond the field parser. It imports `itakit_b` with a
  plain import at its end and dispatches family B's modes through
  `itakit_b.MODES`.
- `scripts/mathpath/labs/eakit_core.py`: used unchanged (imported as `ea`).
- `scripts/mathpath/labs/__init__.py`: one import (`itakit,`) and one registry
  line (`"itakit": itakit.itakit_lab,`).
- `scripts/build_paths.py`: `"itakit"` added to `KITS_WITH_EXPECTATIONS`
  (the Subject's 61 lessons are its published pages). Every itakit preset
  menu must pin at least one tile on every option.
- `scripts/mathcheck.js`: the block `// ---- itakit (Introduction to
  Algorithms), family A ----` … `// ---- end itakit family A ----`, before
  THE VERDICT: 49 assertions, one vm context per mode.

## Conventions (both families)

**Entry point and cfg.** A lesson's lab is `("itakit", cfg)`, with
`cfg["mode"]` (growth, sorting, recurrence, maxsub, hiring, workspan, lup,
fft, or one of family B's) and `cfg["view"]` (default: the mode's first view,
listed first below). An unknown mode or view raises, listing the valid ones.
Keys common to every view: `mode`, `view`, `presets` (required, non-empty),
`preset` (the one shown first; default the first), `title`, `panel_title`,
`panel_intro`. A cfg key named like one of the view's inputs supplies it to
every preset that does not set it (a lesson comparing several arrays on one
recurrence can state `a`, `b`, `k` once). Any other key raises, naming the
keys the view takes. Family A has no lesson-level keys beyond these.

**Panel intro.** Every itakit panel intro begins "A count over the situation
the lesson states. The lab runs the algorithm on the instance and counts; a
count on one instance is evidence about that instance, and only the book's
proof bounds every input." A `panel_intro` in the cfg replaces all but the
first sentence.

**Presets.** Each preset is `{"id": "lower-case-hyphens", "label": "plain
text", <inputs>..., "expect": {tile_id: "exact text"}}`. A label names the
instance; every outcome goes in `expect` (scripts/mathpath/AGENTS.md, "a
preset's two claims"). Every preset must pin at least one tile, because
itakit is in `KITS_WITH_EXPECTATIONS`. Read the strings off the built page
with `node scripts/labcheck.js --observe <page>` (or `preview_subject.py`'s
pages), never out of the code. A preset the page would refuse fails the
build, naming the preset and the reason. Instances are the lesson's own,
never the book's figures' arrays, matrices or graphs (PLAN §C, §E).

**Ids.** The PLAN's two-letter prefixes are taken by other kits, so every id,
JS function and JS variable uses the PLAN prefix followed by `i`
(kit-contract.md §0): `gri` growth, `sti` sorting, `rci` recurrence, `msi`
maxsub, `hri` hiring, `wsi` workspan, `lui` lup, `fti` fft (family B: `rdi`,
`lci`, `obi`, `ami`, `rbi`, `bti`, `fhi`, `vbi`, `bfi`). An input's id is
`<prefix>In<Key>`, the key's first letter capitalised (`stiInList`,
`griInFnA`, `rciInT1`). Each page has `<prefix>Preset` (the worked-example
menu, which is the menu `expect` pins), `<prefix>Status` and
`<prefix>Table`. All 113 top-level JS names and tile ids of family A, and
every `gri…`/`sti…`/… identifier, were grepped across
`scripts/mathpath/labs/*.py`: none is used by another kit, nor by itakit_b.

**Input formats** (eakit_core's parser, unchanged):
- a whole number: `12`, `-3` (no commas, no decimals);
- a number: a decimal with at most 6 places, `3`, `0.25`, `-1.5`, `.5`;
  **fractions such as `1/3` and exponents are refused** (write `0.25`, or
  scale the instance);
- a list (arrays, ranks, coefficients, matrix entries): numbers separated by
  spaces, commas or newlines, `5 2 4 7 1 3 2 6`; in a preset a string or a
  Python list `[5, 2, 4]`;
- records (terms, strands, edges): fields by commas, records by semicolons,
  `0.25, n^2; -5, n`; in a preset a string or a list of lists;
- a name (strands): letters, digits, `.`, `_`, `-`;
- a choice: one of the listed words, exactly (`n lg n`, `p-fib`, `Theta`).
- A wrong value paints one red sentence in the banner and blanks every tile
  and the table: "Array A (whole numbers, up to 40), entry 3 should be a
  whole number, and "x" is not one."

**Number format.**
- Whole numbers grouped `1,024`; minus is U+2212: `−3`.
- A non-whole exact figure: its reduced fraction, both parts grouped, then
  two places, `=` only when exact at two places: `25/12 ≈ 2.08`,
  `33/2 = 16.50`. Past 30 digits: `≈ 3.33 × 10^39`.
- A bare exact fraction, in matrices, pivots, solutions and lists: `1/2`,
  `−2/11`. Matrices print row by row, rows separated by `; `:
  `1, 0; 1/3, 1`. Lists: `5, 8, 12`.
- Ratios: `10×`, `3/2 ≈ 1.5×`, and `≈ 25.1×` when the ratio is built from a
  rounded figure.
- A rounded figure (it contains lg n of a number that is not a power of 2):
  `≈ 79.73`. growth/race prints a time below 0.01 s in powers of ten, with
  its exact fraction when it has one: `1/125 ≈ 8.00 × 10^−3 s`,
  `≈ 3.99 × 10^−8 s`.

**Exactness.** Every figure is an exact BigInt rational except: (1) a value
containing lg n, which prints rounded while every comparison involving lg n
(crossover, witness, faster) is decided exactly by bracketing lg n on
integers (`itaLgCmp`); (2) the exponent in `rciCritical` when log_b a is
irrational (`n^(log_2 7) ≈ n^2.807`), while the case is decided on integers;
(3) fft, which works in doubles, rounds, and compares with the exact
schoolbook product (`ftiAgree`); its rounding distance is not below 10^−9
for large coefficients (see "fft" below). Never pin `ftiError`: its value is a
floating-point residue and may differ between browsers.

**Refusals.** Beyond the field rules above, each view's Python `check`
mirrors every refusal its JS makes, with the same sentence, so a preset the
page would refuse fails the build. A parity run of 122 targeted inputs
(both sides of every limit below) gave the same verdict and the same
sentence on both sides.

**Page weight.** A page ships RATIONAL_JS, EA_CORE_JS, ITA_CORE_JS, the
wiring, its mode's base block and its own view's block, nothing more. Family
A's lab alone is 6.4 to 8.2 KB gzipped (growth/bounds the heaviest); a
scratch lesson page (an Enterprise Patterns lesson's prose with each lab) is
33.3 to 35.3 KB gzipped, 125 to 132 KB raw, far under the 67 KB ceiling.

## Family A (itakit.py): modes, views, fields, tiles

Each field is listed as `key` (kind, default), with its input id and label;
— means required. Tiles are listed as id, label, then the value observed on
the sample preset named. All family A views are family 1 (eakit_core's
FAMILY sentence 1). Below each mode: what it refuses, and further observed
figures.

### growth (`gri`)

- **race.** Two programs on two machines. Fields:
  - `fnA` (choice: `lg n`, `n`, `n lg n`, `n^2`, `n^3`, `2^n`, —), id `griInFnA`, labelled "Program A's cost (instructions)";
  - `costA` (number > 0, ≤ 10,000,000, —), id `griInCostA`, labelled "A's constant (instructions = constant × cost)";
  - `speedA` (number > 0, ≤ 1,000,000,000,000,000, —), id `griInSpeedA`, labelled "Machine A's speed (instructions a second)";
  - `fnB` (choice: `lg n`, `n`, `n lg n`, `n^2`, `n^3`, `2^n`, —), id `griInFnB`, labelled "Program B's cost (instructions)";
  - `costB` (number > 0, ≤ 10,000,000, —), id `griInCostB`, labelled "B's constant";
  - `speedB` (number > 0, ≤ 1,000,000,000,000,000, —), id `griInSpeedB`, labelled "Machine B's speed (instructions a second)";
  - `n` (whole 1–1,000,000,000,000, —), id `griInN`, labelled "Input size n";

  Tiles, with their values on the sample preset `two-machines` (fnA="n^2", costA="2", speedA="1000000000", fnB="n lg n", costB="40", speedB="10000000", n="1000000"):
  - griCross, Where the better order of growth wins for good, `n = 29,719: from there on B (n lg n) is always faster`;
  - griTimeA, A's time at n, `2,000 s`;
  - griTimeB, B's time at n, `≈ 79.73 s`;
  - griFaster, Faster at n, `B, ≈ 25.1× faster`;

- **bounds.** Checking a claimed witness c and n₀. Fields:
  - `f` (records of coef (number ≥ -10,000,000, ≤ 10,000,000), fn (choice: `1`, `lg* n`, `lg n`, `n`, `n lg n`, `n^2`, `n^3`, `F(n)`, `2^n`, `n!`); 1–4, —), id `griInF`, labelled "f(n) (coefficient, function; up to 4 terms)";
  - `g` (records of coef (number ≥ -10,000,000, ≤ 10,000,000), fn (choice: `1`, `lg* n`, `lg n`, `n`, `n lg n`, `n^2`, `n^3`, `F(n)`, `2^n`, `n!`); 1–4, —), id `griInG`, labelled "g(n) (coefficient, function; up to 4 terms)";
  - `relation` (choice: `O`, `Omega`, `Theta`, —), id `griInRelation`, labelled "Claim: f(n) = ? (g(n))";
  - `c1` (number > 0, ≤ 10,000,000, default `1`), id `griInC1`, labelled "c₁, the lower constant (Ω and Θ)";
  - `c2` (number > 0, ≤ 10,000,000, default `1`), id `griInC2`, labelled "c₂, the upper constant (O and Θ)";
  - `n0` (whole 1–1,000,000, —), id `griInN0`, labelled "n₀";

  Tiles, with their values on the sample preset `theta-quadratic` (f="0.25, n^2; -5, n", g="1, n^2", relation="Theta", c1="0.1", c2="0.25", n0="34"):
  - griHolds, Witness holds from n₀ to n₀ + 10,000, `yes, at all 10,001 values of n from 34 to 10,034`;
  - griFirstFail, First n where it fails, `none from 34 to 10,034`;
  - griAtN0, At n₀, `f(34) = 119, c₁g(34) = 578/5 = 115.60, c₂g(34) = 289`;
  - griOrder, Order of growth (by the leading terms), `f = Θ(g): both lead with n^2`;
  - griClaim, The claim, for some witness, `true: some c and n₀ work`;

### sorting (`sti`)

- **insertion.** INSERTION-SORT pass by pass, with its loop invariant. Fields:
  - `list` (list of 1–40 numbers, each whole -10,000,000–10,000,000, —), id `stiInList`, labelled "Array A (whole numbers, up to 40)";

  Tiles, with their values on the sample preset `eight` (list="31 12 47 5 26 12 40 8"):
  - stiComparisons, Key comparisons, `21`;
  - stiShifts, Shifts, `16`;
  - stiInvariant, Loop invariant, `holds at all 8 checks, j = 2 to 9`;
  - stiSorted, Sorted, `5, 8, 12, 12, 26, 31, 40, 47`;

- **cost.** The line-cost sum with t_j. Fields:
  - `list` (list of 1–40 numbers, each whole -10,000,000–10,000,000, —), id `stiInList`, labelled "Array A (whole numbers, up to 40)";

  Tiles, with their values on the sample preset `eight` (list="31 12 47 5 26 12 40 8"):
  - stiTj, t_j for j = 2 to n, `2, 1, 4, 3, 4, 2, 7`;
  - stiSumTj, Σ t_j, `23`;
  - stiComparisons, Key comparisons, `21`;
  - stiShifts, Shifts (= inversions), `16`;
  - stiBest, Best-case comparisons, `n − 1 = 7`;
  - stiWorst, Worst-case comparisons, `n(n − 1)/2 = 28`;
  - stiLines, Lines executed, every c_i = 1, `84 (best 5n − 4 = 36, worst (3n² + 7n − 8)/2 = 120)`;

- **merge.** MERGE-SORT's comparisons, level by level. Fields:
  - `list` (list of 1–40 numbers, each whole -10,000,000–10,000,000, —), id `stiInList`, labelled "Array A (whole numbers, up to 40)";

  Tiles, with their values on the sample preset `eight` (list="31 12 47 5 26 12 40 8"):
  - stiLevels, Merge levels, `3 (⌈lg n⌉ = 3)`;
  - stiPerLevel, Comparisons by level, `level 1: 7; level 2: 6; level 3: 4`;
  - stiMergeTotal, Comparisons in all, `17`;
  - stiMergeBound, Worst case for this n, `n⌈lg n⌉ − 2^⌈lg n⌉ + 1 = 17`;
  - stiSentinel, Comparisons with sentinels, `24`;
  - stiSorted, Sorted, `5, 8, 12, 12, 26, 31, 40, 47`;

### recurrence (`rci`)

- **master.** The exact T(n) beside the master method. Fields:
  - `a` (whole 1–1,000, —), id `rciInA`, labelled "a (subproblems)";
  - `b` (whole 2–1,000, —), id `rciInB`, labelled "b (each of size n/b)";
  - `c` (number > 0, ≤ 10,000,000, default `1`), id `rciInC`, labelled "c in f(n) = c·n^k·lg^p n";
  - `k` (number ≥ 0, ≤ 8, —), id `rciInK`, labelled "k (at most 8; b^k must be whole)";
  - `p` (whole -3–3, default `0`), id `rciInP`, labelled "p (−3 to 3; p ≠ 0 needs b a power of 2)";
  - `t1` (number ≥ 0, ≤ 10,000,000, default `1`), id `rciInT1`, labelled "T(1)";
  - `j` (whole 1–30, —), id `rciInJ`, labelled "Largest j (n = b^j)";

  Tiles, with their values on the sample preset `merge-sort` (a="2", b="2", k="1", j="10"):
  - rciCritical, n^(log_b a), `n`;
  - rciCase, Master method, `case 2: f(n) = Θ(n^(log_b a))`;
  - rciSolution, Solution, `Θ(n lg n)`;
  - rciLast, T(n) at the largest n, `T(1,024) = 11,264`;
  - rciRatio, T(n) over the predicted growth there, `11/10 = 1.10`;

- **tree.** The recursion tree, level by level. Fields:
  - `a` (whole 1–1,000, —), id `rciInA`, labelled "a (subproblems)";
  - `b` (whole 2–1,000, —), id `rciInB`, labelled "b (each of size n/b)";
  - `c` (number > 0, ≤ 10,000,000, default `1`), id `rciInC`, labelled "c in f(n) = c·n^k·lg^p n";
  - `k` (number ≥ 0, ≤ 8, —), id `rciInK`, labelled "k (at most 8; b^k must be whole)";
  - `p` (whole -3–3, default `0`), id `rciInP`, labelled "p (−3 to 3; p ≠ 0 needs b a power of 2)";
  - `t1` (number ≥ 0, ≤ 10,000,000, default `1`), id `rciInT1`, labelled "T(1)";
  - `j` (whole 1–30, —), id `rciInJ`, labelled "Largest j (n = b^j)";

  Tiles, with their values on the sample preset `three-quarters` (a="3", b="4", k="2", j="4"):
  - rciLevelSums, Level sums, root first, `65,536, 12,288, 2,304, 432`;
  - rciLeaves, Leaves, `81 × T(1) = 81`;
  - rciTreeTotal, Sum of the tree, `80,641`;
  - rciLast, T(n) by the recurrence, `T(256) = 80,641`;
  - rciTrend, From level to level, `each level 3/16 × the one above: decreasing, the root dominates`;
  - rciCase, Master method, `case 3: f(n) = Ω(n^(log_b a + ε)), and a·f(n/b) ≤ (3/16)·f(n)`;

### maxsub (`msi`)

- **compare.** Brute force, divide-and-conquer and one pass. Fields:
  - `list` (list of 1–60 numbers, each whole -10,000,000–10,000,000, —), id `msiInList`, labelled "Array A (whole numbers, up to 60)";

  Tiles, with their values on the sample preset `twelve` (list="4 -9 6 -2 7 -11 3 5 -1 8 -6 2"):
  - msiBrute, Brute force, `A[3..10], sum 15`;
  - msiDc, Divide-and-conquer, `A[7..10], sum 15`;
  - msiLinear, One pass, `A[7..10], sum 15`;
  - msiBruteSteps, Brute force, steps, `78 sums (n(n + 1)/2)`;
  - msiDcSteps, Divide-and-conquer, steps, `23 calls, 44 elements scanned across the middle`;
  - msiLinearSteps, One pass, steps, `12 elements, one pass`;
  - msiAgree, Do the three agree, `yes: all three find sum 15, by tie-breaking not all the same subarray`;

### hiring (`hri`)

- **order.** Hires on one order, and on average. Fields:
  - `order` (list of 1–40 candidates, each whole 1–40, —), id `hriInOrder`, labelled "Candidates' ranks in interview order (a permutation of 1 to n; higher is better)";
  - `ci` (number ≥ 0, ≤ 10,000,000, default `1`), id `hriInCi`, labelled "Cost of an interview, c_i";
  - `ch` (number ≥ 0, ≤ 10,000,000, default `10`), id `hriInCh`, labelled "Cost of a hire, c_h";

  Tiles, with their values on the sample preset `four` (order="2 1 4 3"):
  - hriHires, Hires on this order, `2: candidates 1, 3`;
  - hriCost, Cost on this order, `24`;
  - hriAverage, Average hires over every order, `25/12 ≈ 2.08 over 24 orders`;
  - hriHarmonic, H_n, `25/12 ≈ 2.08`;
  - hriAgree, Average equals H_n, `yes: the average is H_4`;
  - hriExpectedCost, Expected cost, c_i·n + c_h·H_n, `149/6 ≈ 24.83`;

### workspan (`wsi`)

- **dag.** A computation DAG's work and span. Fields:
  - `strands` (records of strand (name), cost (whole 1–1,000,000); 1–40, —), id `wsiInStrands`, labelled "Strands (strand, cost)";
  - `edges` (records of from (name), to (name); 0–60, default ``), id `wsiInEdges`, labelled "Edges (from, to)";
  - `p` (whole 1–1,000,000, —), id `wsiInP`, labelled "Processors P";

  Tiles, with their values on the sample preset `fork-join` (strands="start, 1; left, 4; mid, 2; right, 3; join, 1", edges="start, left; start, mid; start, right; left, join; mid, join; right, join", p="2"):
  - wsiWork, Work T₁, `11`;
  - wsiSpan, Span T∞, `6`;
  - wsiParallelism, Parallelism T₁/T∞, `11/6 ≈ 1.83`;
  - wsiBound, Greedy bound T₁/P + T∞, `23/2 = 11.50`;
  - wsiLower, Lower bound max(T₁/P, T∞), `6`;
  - wsiCritical, Critical path, `start → left → join`;

- **recurrence.** P-FIB and MERGE-SORT′ as recurrences. Fields:
  - `program` (choice: `p-fib`, `merge-sort`, —), id `wsiInProgram`, labelled "Program";
  - `n` (whole 0–1,000,000, —), id `wsiInN`, labelled "n";
  - `p` (whole 1–1,000,000, —), id `wsiInP`, labelled "Processors P";

  Tiles, with their values on the sample preset `pfib-4` (program="p-fib", n="4", p="2"):
  - wsiWork, Work T₁, `17`;
  - wsiSpan, Span T∞, `8`;
  - wsiParallelism, Parallelism T₁/T∞, `17/8 ≈ 2.13`;
  - wsiBound, Greedy bound T₁/P + T∞, `33/2 = 16.50`;
  - wsiLower, Lower bound max(T₁/P, T∞), `17/2 = 8.50`;
  - wsiCritical, Critical path, `P-FIB(4) → P-FIB(3) → P-FIB(2) → P-FIB(0)`;

### lup (`lui`)

- **decompose.** PA = LU, exactly, and LUP-SOLVE. Fields:
  - `matrix` (list of 1–25 entries, each number ≥ -10,000,000, ≤ 10,000,000, —), id `luiInMatrix`, labelled "Matrix A, row by row (1, 4, 9, 16 or 25 numbers)";
  - `b` (list of 0–5 entries, each number ≥ -10,000,000, ≤ 10,000,000, default ``), id `luiInB`, labelled "b (optional; one number a row)";

  Tiles, with their values on the sample preset `three` (matrix="2 0 1\n4 1 3\n-2 5 2", b="5 13 9"):
  - luiPerm, Permutation, `π = 2, 3, 1`;
  - luiPivots, Pivots, `4, 11/2, −2/11`;
  - luiL, L, `1, 0, 0; −1/2, 1, 0; 1/2, −1/11, 1`;
  - luiU, U, `4, 1, 3; 0, 11/2, 7/2; 0, 0, −2/11`;
  - luiDet, det A, `−4`;
  - luiX, Solution, `x = 9/4, 5/2, 1/2`;
  - luiCheck, Checked, `yes: A·x = b exactly`;

### fft (`fti`)

- **multiply.** The schoolbook product against evaluate, multiply, interpolate. Fields:
  - `a` (list of 1–16 coefficients, each whole -1,000,000–1,000,000, —), id `ftiInA`, labelled "A(x)'s coefficients, constant first (up to 16)";
  - `b` (list of 1–16 coefficients, each whole -1,000,000–1,000,000, —), id `ftiInB`, labelled "B(x)'s coefficients, constant first (up to 16)";

  Tiles, with their values on the sample preset `two-linear` (a="1 2", b="3 4"):
  - ftiN, n, padded to a power of 2, `4 (product degree 2)`;
  - ftiSchool, Schoolbook product, `3, 10, 8`;
  - ftiSchoolMults, Schoolbook multiplications, `4 (2 × 2)`;
  - ftiFft, FFT product, rounded, `3, 10, 8`;
  - ftiButterflies, FFT butterflies, `12 (3 transforms × (n/2) lg n = 3 × 4), and 4 pointwise products`;
  - ftiAgree, Agree, `yes`;
  - ftiError, Largest distance from an integer before rounding, `below 10^−9`;

### What the tiles mean, and further observed figures

**growth/race.** The crossover is the least n from which the program whose
cost grows more slowly is strictly faster at every larger n (n = 1 to 64 one
by one, then bisection up to 10^15, or 4,096 when either costs `2^n`; past
the cap: `beyond n = 1,000,000,000,000,000, where the search stops`). Equal
orders never cross: `never: the same order of growth, so A always takes 3/2
≈ 1.5× B's time`; the ratio is always stated from the slower program, so it
is never under 1 (A's constant 1 and B's 41 on one machine: `never: the
same order of growth, so B always takes 41× A's time`). An exact tie is not "faster": n² against 8n crosses at
`n = 9: …` and `griFaster` at n = 8 is `neither: the same time`. Other
observed: n³ against 2^n on one machine at 10^6 a second, n = 20:
`griCross` `n = 10: from there on A (n^3) is always faster`, `griTimeA`
`1/125 ≈ 8.00 × 10^−3 s`, `griFaster` `A, 16,384/125 ≈ 131.1× faster`.
Refused: a program costing `2^n` with n > 4,096 ("Program A costs 2^n, and
2^n seconds past n = 4,096 is too large to print; choose n of at most
4,096"). The table lists both times at n = 1, 10, …, 10^7.

**growth/bounds.** `griHolds` checks every n from n₀ to n₀ + 10,000; it is
evidence, not a proof, and the banner says so. `griOrder` and `griClaim`
compare leading terms by the menu's ranking (each function is o() of the
next), so they hold for every n: `griClaim` is `true: some c and n₀ work` or
`false: no c and n₀ work`, or `false: no witness exists` when f or g has a
negative leading coefficient. A witness can fail while the claim is true —
the lesson's point. Observed: the same f, g and constants from n₀ = 20:
`griHolds` `no`, `griFirstFail` `n = 20: f(n) < c₁·g(n)`; 2^n against n³
with c₂ = 1,000: `griFirstFail` `n = 24: f(n) > c₂·g(n)`, `griOrder`
`f = ω(g): 2^n grows faster than n^3`, `griClaim` `false: no c and n₀ work`.
`griAtN0` lists only the constants the relation uses (`f(1) = 0, c₂g(1) =
1` for O). `c1` is ignored for O and `c2` for Ω. Refused: n₀ > 1,000 with
F(n), 2^n or n! in f or g. No table.

**sorting.** A key comparison is one test A[i] > key; when i reaches 0 the
loop stops without one, so comparisons = shifts + (passes that stop on a
comparison). t_j = shifts + 1. Shifts equal the inversions. Observed:
reversed 10 9 … 1: `stiComparisons` `45`, `stiShifts` `45`, `stiInvariant`
`holds at all 10 checks, j = 2 to 11`; cost on 1 2 3 4 5 6: `stiComparisons`
`5`, `stiLines` `26 (best 5n − 4 = 26, worst (3n² + 7n − 8)/2 = 71)`. merge
on 9 3 7 1 8 2 6 4 5 0 10: `stiLevels` `4 (⌈lg n⌉ = 4)`, `stiMergeTotal`
`29`, `stiSentinel` `39`; a sorted array of 11 makes 22 against the bound
29. With n = 1: `stiTj` and `stiPerLevel` read `none (n = 1)`. Tables: one
row a pass (insertion, cost), one row a level (merge). Refuses nothing
beyond the field (1–40 whole numbers).

**recurrence.** T(1) = `t1`, T(b^j) = a·T(b^(j−1)) + c·(b^k)^j·(j·lg b)^p,
exactly, for j up to `j`. The case compares b^k with a: smaller case 1,
larger case 3, equal with p = 0 case 2, equal with p ≠ 0 a gap
(`falls in the gap between cases 2 and 3` for p > 0, `… between cases 1 and
2` for p < 0). `rciRatio` divides T(n) by n^(log_b a) (case 1),
n^(log_b a)·log_b n (case 2), f(n) (case 3), n^(log_b a)·log_b^(p+1) n (gap,
p > 0) or n^(log_b a) (gap, p < 0). Observed on master: 7T(n/2) + n², j = 8:
`rciCritical` `n^(log_2 7) ≈ n^2.807`, `rciCase` `case 1: f(n) =
O(n^(log_b a − ε))`, `rciSolution` `Θ(n^(log_2 7))`; 2T(n/2) + n lg n, j =
10: `rciSolution` `no case applies (Exercise 4.6-2 extends case 2: Θ(n lg^2
n))`, `rciRatio` `14/25 = 0.56`; 3T(n/4) + n², j = 8: `rciCase` `case 3:
f(n) = Ω(n^(log_b a + ε)), and a·f(n/b) ≤ (3/16)·f(n)`, `rciRatio`
`5,286,112,081/4,294,967,296 ≈ 1.23`. On tree, T(n/2) + 1 (k = 0), j = 6:
`rciLevelSums` `1, 1, 1, 1, 1, 1`, `rciTrend` `each level 1 × the one above:
every level the same`, `rciLast` `T(64) = 7`. More than six levels print
the first three, `…`, and the last; the table has every level. Refused: b^k
not whole ("b^k = 2^1/2 is not a whole number, so f(b^j) is not exact;
choose k with b^k whole"); p ≠ 0 with b not a power of 2 ("With p ≠ 0, b
must be a power of 2, so that lg n is a whole number at every n = b^j").

**maxsub.** Indices are one-based; a subarray is never empty (an
all-negative array's answer is its largest element: on −5 −2 −8 −3,
`msiLinear` `A[2..2], sum −2`). Ties: brute force keeps the first best (least
i, then least j); divide-and-conquer prefers left, then right, then
crossing; one pass extends while the running sum is positive. So the three
may name different subarrays of the same sum, and `msiAgree` says so (`yes:
all three find sum 15, by tie-breaking not all the same subarray`) or `…,
the same subarray`. Divide-and-conquer always makes 2n − 1 calls. Refuses
nothing beyond the field (1–60 whole numbers).

**hiring.** Higher rank is better; the first candidate is always hired. The
average runs the hiring loop on every order of 1..n by Heap's algorithm, up
to n = 9 (362,880 orders), and its table counts orders by hires. For n > 9:
`hriAverage` `not run: n > 9 (12! orders)`, `hriAgree` `—`, no table, and
`hriHarmonic` is still exact (`86,021/27,720 ≈ 3.10` at n = 12). Observed on
1 2 … 8: `hriHires` `8: candidates 1, 2, 3, 4, 5, 6, 7, 8`, `hriCost` `88`,
`hriAverage` `761/280 ≈ 2.72 over 40,320 orders`. Refused: not a
permutation ("The order gives rank 2 twice; it is a permutation of 1 to 3";
"The order ranks 3 candidates, so each rank is from 1 to 3, and entry 3 is
4").

**workspan.** dag: work is the sum of strand costs; span the costliest path
(strand costs added); the critical path breaks ties toward the earlier
strand in the list. recurrence: `p-fib` counts unit strands, three a call
for n ≥ 2 and one for n ≤ 1 (so P-FIB(4) is 17 and 8), n ≤ 40;
`merge-sort` is MERGE-SORT′ (halves spawned, serial merge; a merge of m
elements costs m, a call on one element 1). Observed: MERGE-SORT′ on 1,024
with P = 8: `wsiWork` `11,264`, `wsiSpan` `2,047`, `wsiCritical` `sizes
1,024 → 512 → … → 1`. Tables: per strand (dag), per k (p-fib), per size
down the critical path (merge-sort). Refused: an edge naming an unknown
strand, a self edge, a duplicate edge, a cycle ("The edges form a cycle
through a, b; a computation DAG has none"); p-fib with n > 40;
merge-sort with n = 0.

**lup.** Partial pivoting by largest absolute value, the first on a tie, as
LUP-DECOMPOSITION does. π lists, for each row of PA, the row of A it came
from. Without `b`, `luiX` reads `— (no b given)` and `luiCheck` `—`.
Observed on the 2 × 2 `2 1 / 6 4`: `luiPerm` `π = 2, 1`, `luiL` `1, 0; 1/3,
1`, `luiU` `6, 4; 0, −1/3`, `luiDet` `2`. Refused: an entry count that is not
1, 4, 9, 16 or 25; b of the wrong length; singular ("The matrix is
singular: column 2 has no nonzero pivot on or below the diagonal").

**fft.** Coefficients are listed constant term first. n is the least power
of 2 at least the product's length; butterflies are 3 × (n/2) lg n (two
forward transforms and one inverse) plus n pointwise products. `ftiSchool`
and `ftiFft` print their coefficients without thousands separators, so every
comma separates two coefficients: `−1000000000000, 3000000, −2`. `ftiError`
is `below 10^−9` only for small coefficients; it grows with their size, and
near a million it is not: the `large` preset (`1000000 −999999 1000000` times
`999999 1000000 −1000000`) prints about `1.8 × 10^−4`, and sixteen
coefficients of 1,000,000 squared about `3.9 × 10^−3`. Every input the kit
accepts stays far under the 1/2 at which rounding could land on the wrong
integer (20,000 random inputs at the limits: largest distance 1.2 × 10^−3,
none wrong). `ftiAgree` does not rely on that margin: it compares every
rounded coefficient, padding included, with the exact BigInt schoolbook
product, so it reads `yes` only when the FFT's answer is exactly right. Do
not pin `ftiError`. Refuses nothing beyond the fields (1–16 whole numbers from
−1,000,000 to 1,000,000).

### A sample preset (sorting/merge)

```python
"lab": ("itakit", {
    "mode": "sorting", "view": "merge",
    "presets": [
        {"id": "eight", "label": "eight numbers",
         "list": "31 12 47 5 26 12 40 8",
         "expect": {"stiPerLevel": "level 1: 7; level 2: 6; level 3: 4",
                    "stiMergeTotal": "17",
                    "stiMergeBound": "n⌈lg n⌉ − 2^⌈lg n⌉ + 1 = 17"}},
        {"id": "eleven", "label": "eleven numbers",
         "list": [9, 3, 7, 1, 8, 2, 6, 4, 5, 0, 10],
         "expect": {"stiLevels": "4 (⌈lg n⌉ = 4)", "stiMergeTotal": "29",
                    "stiSentinel": "39"}},
    ],
}),
```

A recurrence lesson stating the recurrence once and varying the size:
`{"mode": "recurrence", "view": "master", "a": "2", "b": "2", "k": "1",
"presets": [{"id": "to-1024", "label": "up to n = 1,024", "j": "10",
"expect": {"rciCase": "case 2: f(n) = Θ(n^(log_b a))", "rciLast": "T(1,024)
= 11,264"}}]}` (`c`, `p` and `t1` take their defaults 1, 0 and 1).

### Verification (family A)

- `node scripts/mathcheck.js`: passes; family A's block holds 49 assertions,
  one per key figure in PLAN §D's tile column or more (insertion on a
  reversed array = n(n − 1)/2; merge comparisons per level; 2T(n/2) + n is
  case 2 with T(2^j) = 2^j(j + 1) for every j from 0 to 30; the three
  maximum-subarray routes against a direct scan on 300 seeded arrays; the
  hiring average over all orders of 4 = H_4 = 25/12 and of 9 = H_9; P-FIB(4)
  work 17, span 8, and P-FIB(30) = 4F(31) − 3; LUP solving two 3 × 3
  systems exactly; (1 + 2x)(3 + 4x) by FFT; lg n decided exactly at 1,024
  and 1,025). The figures were computed independently (by hand and in a
  separate Python model), never read from the kit.
- Every compute function was broken on purpose, once a line, in a scratch
  copy of `scripts/` (26 mutations: the lg bracket, the lg comparison, the
  crossover's tie rule, the race times, each bounds inequality, insertion
  comparisons, the line sum, merge comparisons, the master case and the
  recurrence, the tree levels, each maxsub route, Heap's enumeration, H_n,
  P-FIB work and span, MERGE-SORT′ span, the DAG span, the LU pivot rule,
  the Schur update, back substitution, the FFT's inverse roots and the
  butterfly count). Every one fails a case. The crossover tie rule was first
  missed, so the two exact-tie cases were added.
- `node scripts/labcheck.js` on 13 scratch pages (every family A view, 31
  presets): every page executes and survives the sweep of every control;
  with the expectations manifest, every pinned tile matches.
- Python mirror against the page: 122 targeted inputs, same verdict and same
  sentence.
- `python3 scripts/build_paths.py --check` passes (no published page
  changes) and `python3 -m unittest tests.test_site_invariants -k Lab`
  passes.

### Deviations from PLAN §D (family A)

- **Id prefixes** are the PLAN's two letters plus `i` (`gri`, not `gr`),
  because every two-letter prefix is already used by another kit
  (`grCompute`, `hrPreset`, `ftStatus` exist).
- **Fractions are not typeable.** lup takes integer or decimal entries (at
  most 6 places), because eakit_core's parser, which this kit must not
  change, reads no fractions. Every intermediate and result is still an
  exact fraction.
- **hiring averages every order up to n = 9**, not 8 (PLAN's input column
  says 9, its tile column 8; 9 runs in well under a second).
- **recurrence** restricts f to what can be evaluated exactly at n = b^j:
  b^k must be whole, and p ≠ 0 needs b a power of 2. The master-method
  ratio uses log_b n where the book writes lg n (a constant factor).
- **sorting/merge** counts the comparisons of a merge that stops when one
  half runs out (so the PLAN's bound n⌈lg n⌉ − 2^⌈lg n⌉ + 1 applies), and
  prints CLRS's sentinel count beside it (`stiSentinel`).
- **growth/race** adds a crossover cap (10^15; 4,096 with 2^n) and growth/
  bounds a cap on n₀ (1,000) when F(n), 2^n or n! appears, both stated.

## Family B (itakit_b.py)

Nine modes: rod, lcs, obst, amortized, rbtree, btree, fibheap, veb, bfs. Every
example tile string below was read off a rendered scratch page with
`node scripts/labcheck.js --observe`; none was copied from the code. Every
view prints its counting rules under the tiles ("How the lab counts."), so a
reader can recount by hand; this section summarises them, and "Deviations
(family B)" says where the kit differs from PLAN §D and why.

### Files (family B; nothing committed)

- `scripts/mathpath/labs/itakit_b.py`: the nine modes, each a base block
  (`RDI_JS`, `LCI_JS`, `OBI_JS`, `AMI_JS`, `RBI_JS`, `BTI_JS`, `FHI_JS`,
  `VBI_JS`, `BFI_JS`) defining `<prefix>Compute(view, inst, opts)`, one block
  per view (`AMI_VIEW_JS["stack"]`, …), the Python `check` of every view that
  refuses anything beyond the field parser, and one spec dict per mode
  (`ROD`, `LCS`, … in `SPECS`). It exposes `MODES = {mode: builder}`, each
  builder `builder(cfg) -> Lab` through `itakit.mode_lab` (kit-contract.md).
- `scripts/mathcheck.js`: the block `// ---- itakit (Introduction to
  Algorithms), family B ----` … `// ---- end itakit family B ----`, straight
  after family A's: 69 assertions, one vm context per mode.
- Nothing else: `itakit.py`, `labs/__init__.py` and `build_paths.py` are
  family A's.

### Conventions (family B)

- **All views are family 1** (the Subject's panel sentence). No lesson-level
  cfg keys beyond the common ones; a cfg key named like an input supplies it
  to every preset that does not set it (a btree lesson can state `t` once).
- **Ids.** Prefixes `rdi` rod, `lci` lcs, `obi` obst, `ami` amortized, `rbi`
  rbtree, `bti` btree, `fhi` fibheap, `vbi` veb, `bfi` bfs. Inputs are
  `<prefix>In<Key>` (`rdiInPrices`, `obiInScale`, `fhiInOps`, `bfiInGraph`);
  each page has `<prefix>Preset`, `<prefix>Status`, `<prefix>Table`.
- **Operation lists** (amortized stack and table, fibheap, veb) are one text
  area of words and whole numbers separated by spaces or commas, read left to
  right: `insert 5, insert 3, extract, decrease 5 1`. In a preset give a
  string. A word the view does not know, a number that follows nothing, or a
  word missing its number is refused, naming the entry: `Operations, entry 3:
  "pusj" should be push, pop or multipop`.
- **Keys** are whole numbers 0–1,000,000 and distinct wherever they name a
  node (rbtree, btree, fibheap); vEB elements are 0 to u − 1.
- **Exactness.** Every figure is exact. The only printed approximations are
  rbtree's 2 lg(n + 1) and btree's log_t((n + 1)/2), to two places, rounded
  half up by exact integer comparison, `=` only when exact (`2 lg 8 = 6`,
  `log_2 5.5 ≈ 2.46`, `2 lg 11 ≈ 6.92`). fibheap's D(n) = ⌊log_φ n⌋ is exact.
- **Tables.** Every view prints a table under the tiles (lcs only when both
  strings have at most 15 characters); per-operation tables show at most the
  first 60 operations and say so. Tables wider than their box repaint
  compact (eakit_core's wiring).

### rod (`rdi`)

- **cut** (15.1). Field `prices` (list of 1–20 numbers ≥ 0, decimals allowed;
  —), id `rdiInPrices`, "Prices p_1 to p_n, for pieces of length 1 to n"; n
  is the number of prices. Tiles, on prices `1 5 8 9`:
  - `rdiRevenue` Best revenue r_n: `10`;
  - `rdiCuts` Pieces: `2 + 2` (sold whole: `3 (no cut)`);
  - `rdiNaive` CUT-ROD calls, 2^n: `16` (T(n) = 2^n, computed, never run; n = 20 gives `1,048,576`);
  - `rdiWays` Ways to cut, 2^(n−1): `8`;
  - `rdiMemo` MEMOIZED-CUT-ROD-AUX calls: `11` (counted as run, first call included, = 1 + n(n+1)/2);
  - `rdiInner` BOTTOM-UP inner-loop runs: `10` (n(n+1)/2).
  Ties keep the smallest first piece (the book's strict `<`): prices `2 4`
  give `1 + 1`. Decimal prices print exactly: `0.5 1.25` gives `5/4 = 1.25`.
  Table: j, p_j, r_j, s_j, cut as. Refusals: the field parser's only.

### lcs (`lci`)

- **table** (15.4). Fields `x`, `y` (one word each: letters, digits, `.`,
  `_`, `-`; at most 30 characters; —), ids `lciInX`, `lciInY`; case matters.
  Tiles, on `ABAB` and `BABA`:
  - `lciLength` LCS length: `3`;
  - `lciLcs` One LCS (PRINT-LCS): `ABA` (`(empty)` when there is none);
  - `lciCells` Cells filled, m × n: `4 × 4 = 16`;
  - `lciArrows` Arrows in the b table: `↖ 8, ↑ 6, ← 2`.
  A tie goes up (c[i−1, j] ≥ c[i, j−1]), as LCS-LENGTH does, which is why
  this pair prints ABA and not BAB. The c/b table has a row per i and a
  column per j (row and column 0 included), cells `2↖`, PRINT-LCS's path in
  brackets `[2↖]`. Refused: a string over 30 characters.

### obst (`obi`)

- **table** (15.5). Fields `p` (list of 1–8 numbers ≥ 0; —), `q` (list of
  2–9 numbers ≥ 0; —), `scale` (whole ≥ 1, default `1`), ids `obiInP`,
  `obiInQ`, `obiInScale`. Every entry is divided by `scale`; the parser
  refuses `1/16`, so give exact fractions as whole weights over a common
  denominator: `"p": "4 2 1", "q": "2 2 2 3", "scale": 16`. Tiles, on `p`
  `0.3 0.2`, `q` `0.1 0.2 0.2`:
  - `obiCost` Expected search cost e[1, n]: `21/10 = 2.10`;
  - `obiTree` The optimal tree: `k1(d0 k2(d1 d2))` (k_r(left right), dummy leaves d_i);
  - `obiRoots` root[i, j], row i, j = i to n: `1: 1 1; 2: 2`;
  - `obiBrute` Brute force over every tree: `2 trees; least 21/10 = 2.10 (2 trees); agrees`
    (n = 8: `not run at n = 8 (the lab enumerates trees up to n = 7)`).
  The two trees tie here, and the smaller root is kept (OPTIMAL-BST's
  strict `<`). Cost = Σ (depth + 1) × probability over keys and dummies, the
  root at depth 0. The brute force builds every BST (Catalan many: 429 at
  n = 7) and costs each from its own depths. Weights over 16 above give
  `39/16 ≈ 2.44` and `k2(k1(d0 d1) k3(d2 d3))`. Table: every (i, j), shortest
  first, with w, e, root. Refused: `q` not one longer than `p` ("There are 3
  keys, so there are 4 dummy probabilities q0 to q3, and 2 are given"); the
  divided entries not summing to exactly 1 ("The probabilities sum to 19/20
  = 0.95, not 1").

### amortized (`ami`)

Common tiles: `amiActual` Actual cost, total; `amiBound` Aggregate bound;
`amiCredit` Credit left (accounting); `amiPhi` Potential before and after;
`amiAmortized` Amortized cost, total (potential); `amiMax` Largest amortized
cost of one operation.

- **counter** (17.1–17.3). Fields `bits` (whole 1–20; —), `increments`
  (whole 1–1,000; —), `start` (whole, default `0`, less than 2^bits), ids
  `amiInBits`, `amiInIncrements`, `amiInStart`. Cost = bits flipped (an
  increment of all 1s resets them and sets nothing: the counter wraps).
  Accounting charges 2 to set a bit and 0 to reset, credit starting at 0; Φ
  = number of 1 bits. Tiles, on bits 3, increments 8: `amiActual` `14`;
  `amiPerBit` Flips of each bit `bit 0: 8, bit 1: 4, bit 2: 2`; `amiBound`
  `2n = 16`; `amiCredit` `0 (least 0)`; `amiPhi` `Φ0 = 0, Φn = 0`;
  `amiAmortized` `14`; `amiMax` `2`; `amiValue` Counter after `0 (000)`.
  From start 6 (110), 3 increments: `amiCredit` `−1 (least −2)`, `amiPhi`
  `Φ0 = 2, Φn = 1` (the accounting assumes a start at 0; the banner gives
  the potential bound 2n − Φn + Φ0). Refused: start ≥ 2^bits.
- **stack** (17.1–17.3). Field `ops` (`push`, `pop`, `multipop k`; a number
  after push or pop repeats it; at most 1,000 operations), id `amiInOps`.
  PUSH and POP cost 1, MULTIPOP k costs min(s, k) (0 on an empty stack);
  charge 2 a push; Φ = stack size. Tiles, on `push 4 pop multipop 2 push 3
  multipop 9`: `amiActual` `14`; `amiBound` `2 × 7 pushes = 14`; `amiCredit`
  `0`; `amiPhi` `Φ0 = 0, Φn = 0`; `amiAmortized` `14`; `amiMax` `2`;
  `amiOpCount` Operations run `10`. Refused: POP of an empty stack
  ("Operation 3 pops an empty stack"); multipop with no k.
- **table** (17.4). Field `ops` (`insert`, `delete`; a number after either
  repeats it), id `amiInOps`. Insert into no slots allocates 1 (cost 1);
  into a full table doubles and moves (cost num + 1); delete costs 1, and
  when it leaves the table under ¼ full halves it and moves the rest (cost
  num + 1); num 0 frees the table (size 0). Φ is equation 17.6. Tiles, on
  `insert 9 delete 7`: `amiActual` `34`; `amiBound` `3 × 9 + 2 × 7 = 41`
  (the book's amortized bounds, 3 an insert and 2 a delete); `amiPhi`
  `Φ0 = 0, Φn = 2`; `amiAmortized` `36`; `amiMax` `insert 3, delete 2`;
  `amiCredit` Amortized less actual, total `2`; `amiSize` Items and slots
  after `num 2, size 8, load 1/4 = 0.25`; `amiResize` `expansions 4,
  contractions 1, items moved 18`. A delete from a full table has amortized
  cost −1 (`insert 8 delete 2 insert`: `amiMax` `insert 3, delete −1`).
  Refused: a delete from an empty table.

### rbtree (`rbi`)

Shared tiles: `rbiBh` Black-height of the root (bh counts the NIL leaf, not
the node); `rbiHeight` Height (edges from the root down to its deepest NIL
leaf, so a lone node has height 1); `rbiBound` Lemma 13.1 bound.

- **check** (13.1–13.2). Field `nodes` (records `key, color, parent`: key a
  whole number, color `red` or `black`, parent a key or `-` for the root;
  1–60; —), id `rbiInNodes`, a text area. A child smaller than its parent is
  its left child. Preset text: `"4, black, -; 2, red, 4; 6, red, 4; 1, black,
  2; 3, black, 2; 5, black, 6; 7, black, 6"`. Tiles on it: `rbiVerdict` A
  red-black tree `yes`; `rbiP1` … `rbiP5` the five properties, each `holds`;
  `rbiBst` Search-tree order `holds`; `rbiNodes` `7`; `rbiBh` `2`;
  `rbiHeight` `3`; `rbiBound` `2 lg 8 = 6`. On `4, red, -; 2, red, 4; 6,
  black, 4`: `rbiVerdict` `no: property 2, 4, 5 fail`; `rbiP2` `fails: the
  root 4 is red`; `rbiP4` `fails at 4: red, with red child 2` (first in
  preorder); `rbiP5` `fails at 4: 1 black node down its left side, 2 down its
  right` (first in postorder); `rbiBh` `— (property 5 fails)`. A BST-order
  failure reads `fails: 6 comes before 5 in the inorder walk`. Properties 1
  and 3 always hold (every record names a color; NIL leaves are black).
  Refused: a key twice, a parent that is not a key, a node its own parent,
  two left (or right) children ("5 has two left children, 3 and 1 (a child
  smaller than its parent is its left child)"), no root, two roots, a cycle.
- **insert** (13.3). Field `keys` (list of 1–31 distinct whole numbers; —),
  id `rbiInKeys`. Tiles, on `1 2 3 4 5 6 7`: `rbiCases` Fix-up cases, in all
  `case 1′ ×2, case 3′ ×3` (′ marks the mirror case, z's parent a right
  child); `rbiRecolor` `14`; `rbiRotate` `3`; `rbiMostRot` Most rotations in
  one insertion `1`; `rbiFinal` Final tree `2B(1B 4R(3B 6B(5R 7R)))` (key and
  R/B, then both subtrees in parentheses, `-` for a NIL child: `2B(1B(0R -)
  3B)`); `rbiBh` `2`; `rbiHeight` `4`; `rbiBound` `2 lg 8 = 6`. On `10 1 5`:
  `case 2 ×1, case 3 ×1`, rotations 2. A recoloring is a color assignment
  that changes a color: case 1 makes 3, case 3 makes 2, and the final root
  := black counts 1 when the root was red (so the first key always costs 1).
  Table: per key, its cases, recolorings, rotations, root, black-height,
  height. Refused: a key twice.

### btree (`bti`)

- **insert** (18.2). Fields `t` (whole 2–5; —), `keys` (list of 1–60
  distinct whole numbers; —), ids `btiInT`, `btiInKeys`. Tiles, on t 2, keys
  `1 2 3 4 5 6 7 8 9 10`: `btiHeight` Height h `2` (edges root to leaf; a
  lone root is 0); `btiNodes` `8`; `btiSplits` `5`; `btiReads` DISK-READs
  `9`; `btiWrites` DISK-WRITEs `25`; `btiBound` `log_2 5.5 ≈ 2.46` (15 keys:
  `log_2 8 = 3`); `btiLevels` The tree by level, root first `[4] / [2] [6 8]
  / [1] [3] [5] [7] [9 10]`. Counting is B-TREE-INSERT's: 1 write when the
  key goes into a leaf; 1 read for each child the walk descends to (never the
  root, which stays in memory, and never the new right half after a split
  below the root, which was just written); 3 writes for each split (both halves and the
  parent); a full root is split first under a new root. Right after a root
  split, B-TREE-INSERT calls B-TREE-INSERT-NONFULL on the new root, which
  reads the child it descends to: one DISK-READ is counted on the half the
  walk enters, though that half was just written, because the book's
  procedure calls DISK-READ there. B-TREE-CREATE's one write is not in the
  totals. Table: per key, splits, reads, writes, height.
  Refused: a key twice.

### fibheap (`fhi`)

Field (both views) `ops`: `insert k`, `min`, `extract`, `decrease k v`,
`delete k` (at most 120 operations), id `fhiInOps`. Actual cost in steps:
INSERT 1; MIN 1; EXTRACT-MIN 1 + one for each child moved to the root list
+ one for each root CONSOLIDATE takes (links are part of taking a root);
DECREASE-KEY 1 + one per cut (its own and the cascading ones); DELETE the
sum of its DECREASE-KEY to minus infinity and its EXTRACT-MIN. Φ = t(H) +
2m(H); amortized = actual + ΔΦ. Root list: a new root (INSERT or a cut) goes
just left of H.min; INSERT updates H.min, a cut does not (DECREASE-KEY does,
after its cuts); EXTRACT-MIN puts the children where the minimum was and
CONSOLIDATE starts at the old minimum's right neighbour, linking the larger
key under the smaller, then rebuilds the list by degree. Extract children
keep their marks (as the book's procedure does); a link clears the linked
root's mark.

- **ops** (19.1–19.2). Tiles, on `insert 5, insert 3, insert 8, insert 1,
  insert 9, extract`: `fhiActual` `10`; `fhiAmortized` `11`; `fhiPhi` Potential
  now `t(H) + 2m(H) = 1 + 2 × 0 = 1`; `fhiMostAm` Largest amortized cost, by
  operation `insert 2, extract-min 1`; `fhiRoots` Root list from H.min
  `3 (min)`; `fhiDegree` Degree against D(n) `max degree 2; ⌊log_φ 4⌋ = 2`;
  `fhiN` Nodes n `4`. With 9 inserts, an extract and `delete 4`: `fhiMostAm`
  `insert 2, extract-min 1, delete 7`, `fhiRoots` `2 (min), 5`.
- **cascade** (19.3–19.4). Tiles, on 9 inserts (1 to 9), `extract, decrease 7
  1, decrease 8 0`: `fhiCuts` `3`; `fhiCascades` Cascading cuts among them
  `1`; `fhiCalls` Calls to CASCADING-CUT `3`; `fhiMarked` Marked now `0:
  none` (elsewhere `2: 6, 8`); `fhiMostDec` Largest amortized DECREASE-KEY
  `5`; `fhiLemma` size(x) ≥ F(degree + 2) `holds at all 8; closest 0: degree
  1, size 2, F(3) = 2`; `fhiDegree` `max degree 2; ⌊log_φ 8⌋ = 4`;
  `fhiRoots` `0 (min), 6, 1, 2`.
- Refused (both): inserting a key present; min or extract of an empty heap
  ("Operation 3 (extract): the heap is empty"); decreasing or deleting an
  absent key; a new key greater than the old; a new key already present.

### veb (`vbi`)

- **ops** (20.2–20.3). Fields `k` (whole 1–4, u = 2^(2^k) = 4, 16, 256 or
  65,536; —), `ops` (`insert x`, `member x`, `successor x`, `delete x`;
  0 ≤ x < u; at most 60), ids `vbiInK`, `vbiInOps`. Both structures run
  every operation. Tiles, on k 2, `insert 2, insert 3, insert 7, insert 14,
  member 7, successor 4, delete 2, successor 0`: `vbiU` Universe `u = 16,
  √u = 4, lg lg u = 2`; `vbiProto` proto-vEB calls, total `48`; `vbiVeb` vEB
  calls, total `19`; `vbiMost` Most calls in one operation `proto-vEB 7, vEB
  5`; `vbiAnswers` `member 7: yes; successor 4: 7; successor 0: 3` (`none
  asked` without queries; `successor x: none` past the last member);
  `vbiMembers` Members after `3: 3, 7, 14`; `vbiTop` vEB top level `min 3,
  max 14; summary: 1, 3; cluster 1: 3 (7); cluster 3: 2 (14)` (a cluster
  lists its low parts, each element in parentheses; the vEB min is held
  apart). On k 4, `insert 5, member 5, member 6`: proto `41` (an insert is
  31 calls, T(u) = 2T(√u) + 1; a member 5), vEB `7`. A call is one call of a
  structure procedure, the top call included: proto counts MEMBER, MINIMUM,
  SUCCESSOR, INSERT and DELETE; vEB counts MEMBER, SUCCESSOR, INSERT and
  DELETE (MINIMUM, MAXIMUM and EMPTY-TREE-INSERT read or set fields and are
  not counted). Refused: inserting a member, deleting a non-member (the
  book's procedures assume neither), x ≥ u.

### bfs (`bfi`)

- **search** (22.2). Fields `edges` (records `from, to`, names; 0–60; —),
  `graph` (choice `undirected` or `directed`; —), `source` (a name; —),
  `vertices` (optional list of names, default empty: fixes the vertex order
  and adds vertices no edge names), ids `bfiInEdges`, `bfiInGraph`,
  `bfiInSource`, `bfiInVertices`. Adjacency lists follow the edges' order (an
  undirected edge u, v puts v on u's list and u on v's). Tiles, on `s, a; s,
  b; a, c; b, c; c, d`, undirected, source s: `bfiDist` Distance d from s
  `s 0, a 1, b 1, c 2, d 3` (`∞` if unreached); `bfiParent` `a ← s, b ← s,
  c ← a, d ← c` (in dequeue order); `bfiLayers` `0: s; 1: a b; 2: c; 3: d`;
  `bfiEnqueued` `5 of 5 vertices`; `bfiScanned` Adjacency entries examined
  `10 of 10 (2E)` (directed: `5 of 5 (E)`); `bfiUnreached` `0: none`. On
  `a, b; c, d`, directed, source a, vertices `a b c d e`: `bfiUnreached`
  `3: c, d, e`, `bfiEnqueued` `2 of 5 vertices`, `bfiScanned` `1 of 2 (E)`.
  Swapping the first two edges (`s, b; s, a; …`) gives `c ← b`. The graph
  select only redraws; it is not a preset menu. Refused: an undirected
  self-loop, an edge given twice ("Edges, record 2: the edge b, a is given
  twice"), a source that is not a vertex, more than 30 vertices.

### A sample preset (rbtree/insert)

```python
"lab": ("itakit", {
    "mode": "rbtree", "view": "insert",
    "presets": [
        {"id": "ascending", "label": "1 to 7 in order", "keys": "1 2 3 4 5 6 7",
         "expect": {"rbiRecolor": "14", "rbiRotate": "3",
                    "rbiFinal": "2B(1B 4R(3B 6B(5R 7R)))"}},
        {"id": "zigzag", "label": "10, 1, 5", "keys": [10, 1, 5],
         "expect": {"rbiCases": "case 2 ×1, case 3 ×1", "rbiMostRot": "2"}},
    ],
}),
```

An operation list: `{"mode": "fibheap", "view": "cascade", "presets": [{"id":
"cascade", "label": "nine keys, two decreases", "ops": "insert 1, insert 2,
insert 3, insert 4, insert 5, insert 6, insert 7, insert 8, insert 9, extract,
decrease 7 1, decrease 8 0", "expect": {"fhiCuts": "3", "fhiCascades": "1"}}]}`.
Fractions in obst: `{"p": "4 2 1", "q": "2 2 2 3", "scale": 16}`.

### Verification (family B)

- `node scripts/mathcheck.js` passes in full. Family B's block holds 69
  assertions, at least one per compute function and per view, on figures
  worked by hand from the book's procedures: rod r_4 = 10 on prices 1 5 8 9
  with 16 / 11 / 10 calls; LCS ABAB/BABA = ABA under the tie rule; an obst
  tie at 21/10 and a 429-tree brute force; the 3-bit counter's 14 flips over
  8 increments; the multipop stack; the table's 34 elementary operations;
  RB insertion of 1..7 (case 3′ at keys 3, 5 and 7, case 1′ at 4 and 6, 14
  recolorings, 3 rotations, black-height 2, height 4); B-tree t = 2 on 1..10
  (5 splits, 9 reads, 25 writes, height 2); Fibonacci heap extract after 5
  inserts (actual 10, amortized 11) and a cascading cut; vEB u = 16 (proto
  48 calls, vEB 19, traced call by call) and u = 65,536; BFS distances,
  2E/E counts and input-order parents; and every refusal.
- **Mutation testing.** 38 single-line breaks of `itakit_b.py`, at least one
  in every compute function (tie rules, counted calls, the w recurrence, the
  brute force depth, the counter wrap, the accounting charge, MULTIPOP's
  cost, contraction at ¼, Φ's two branches, each RB fix-up case and its
  recolorings, height and black-height, properties 4 and 5, B-tree reads,
  split writes and the full-root test, the log rounding, the link's mark
  clearing, CONSOLIDATE's start, cascading cuts, D(n), proto and vEB
  procedures, BFS's queue, d and directedness), each run against family B's
  block. All 38 fail it. Five first survived (left-hand case 1, a red right
  child, the mark cleared by a link, CONSOLIDATE's starting root, vEB
  member at the min), and a case was added for each. The kit file was
  restored and checked by md5.
- **Parity.** 16,500 fuzzed inputs across all eleven views that refuse
  beyond the parser, through the Python mirror and the page's JS: same
  verdict every time, no tile printing NaN, undefined or Infinity. The fuzz
  found the one real bug the harness missed (a cycle check that never ended
  when a node led into a cycle it was not on), fixed in both mirrors.
- `node scripts/labcheck.js --expect` on 13 scratch pages (every family B
  view, 24 presets): every page executes and survives the sweep of every
  control, and every pinned tile matches; a deliberately wrong pin is
  reported. Each scratch page is 33–35 KB gzipped with an Enterprise
  Patterns lesson's prose.
- Every element id and JS name family B defines (95 ids, 214 names) was
  grepped against `scripts/mathpath/labs/*.py`: none is used by another kit.
- `python3 scripts/build_paths.py --check` passes (1,199 pages, unchanged).

### Deviations from PLAN §D (family B)

- **Id prefixes** are the PLAN's two letters plus `i` (kit-contract.md §0).
- **rbtree/check reads records, not a parenthesized tree.** eakit_core's
  parser, which the kit must not change, has no tree syntax, so a tree is
  given as `key, color, parent` records. The insert view prints its final
  tree in a parenthesized form (`rbiFinal`).
- **obst takes decimals or whole weights with a divisor** (`scale`), since
  the parser reads no fractions; the arithmetic is exact either way.
- **Keys are distinct** in rbtree, btree and fibheap (keys name nodes in the
  input and output); the book's RB-INSERT and B-TREE-INSERT would accept a
  duplicate. vEB refuses inserting a member and deleting a non-member, which
  the book's procedures assume never happen; fibheap refuses min and extract
  on an empty heap.
- **Choices the book leaves open are the lab's, and stated in each rules
  text:** where a Fibonacci heap's new roots and extracted children go in the
  root list, and the step unit of actual cost; proto-vEB deletion (Exercise
  20.2-2); B-TREE-CREATE's write left out of the totals; heights counted in
  edges (to the NIL leaves for red-black trees).
- **rod** prints both 2^n (CUT-ROD's calls, §D) and 2^(n−1) (the ways to cut,
  which §C's lesson line names) as separate tiles.
- **amortized/table**'s aggregate tile is the book's amortized bound (3 an
  insert, 2 a delete), and its credit tile is amortized less actual (= Φn),
  because the book gives an accounting scheme only for expansion.
- **veb** offers member, successor, insert and delete (no minimum, maximum
  or predecessor operations) and k from 1, so u ≥ 4.
