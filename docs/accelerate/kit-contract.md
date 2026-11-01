# acckit: the contract between family A (`acckit.py`) and family B (`acckit_b.py`)

Written by family A's engineer for family B's. PLAN §D is the spec; this file
fixes only the seam between the two modules. If anything here changes, the
change is announced at the top of this file with a time.

**Change, 2026-11-01 (tile wording):** `aktUnit`, `aktTwo`, `aktTimes` added
to AKT_CORE_JS (section 3a); `aktPp` prints `+1 point` for exactly one;
family B's groups/likely uses `aktTimes`/`aktTwo`. Python: `num_text`,
`unit_text` mirror `eaNum`/`aktUnit`.

**No prefix changes.** Every PLAN §D prefix is used as given (section 0).

**Change, 2026-11-01 (after the first version), additive only:** `CLOCK`
added (section 4), a time cell that takes only `day.hh:mm`; `aktScalar`
refuses a bare number in a cell whose spec has `clock: true`. `CLOCK` may be
imported with the other names. Nothing family B uses changed.

## 0. Id prefixes (decided at the start, 2026-11-01)

Grepped `scripts/mathpath/labs/*.py` and `scripts/*.js` for every PLAN prefix
as an identifier start (`\b<prefix>[A-Z0-9_]`, lower-case and upper-case
forms) on branch `feat/accelerate-subject` (364991a):

- Free: family A `ade afl atb arl acm awk`, family B `alk ast avd agr asn
  acp`, shared helpers `akt` / `AKT_`.
- The only hit is `AGR` followed by a capital in English words in comments
  and test labels (`AGREE`, `AGREEMENT` in `mathcheck.js`, `avail.py`,
  `birthdeath.py`). No identifier begins `AGR_` or `agr`, so `agr` stands;
  family B: name your view table `AGR_VIEW`, never `AGREE…`.
- The Design Patterns branch (`gofkit`) is not in this checkout (no local or
  remote branch for it), so it could not be grepped. Its PLAN prefixes begin
  `g`, so no `a…` prefix can meet it.

Every id, JS function and JS variable of a mode begins with its prefix
(`alkCompute`, `ALK_VIEW`, `alkInAnswers`, `alkPreset`); shared helpers begin
`akt` / `AKT_`, and only `acckit.py` defines those. Family B must not define
names beginning `akt`/`AKT_`.

## 1. What `acckit_b.py` exposes

```python
# scripts/mathpath/labs/acckit_b.py
from . import eakit_core as ea
from .acckit import mode_lab, arec, alist, rat, TIME   # safe at module top

ALK_JS = r"""..."""                   # the mode's base block (defines alkCompute)
ALK_VIEW_JS = {}
ALK_VIEW_JS["score"] = r"""..."""      # one block per view

LIKERT = {                            # one spec dict per mode (section 2)
    "prefix": "alk", "fn": "alkCompute", "title": "Likert-type items", "js": ALK_JS,
    "views": {
        "score": {"fields": [...], "tiles": [...], "check": _check_score,
                  "subtitle": "...", "rules": "...", "js": ALK_VIEW_JS["score"]},
    },
}

MODES = {"likert": lambda cfg: mode_lab(cfg, "likert", LIKERT),
         "stats": ..., "validity": ..., "groups": ..., "sample": ..., "capability": ...}
```

**The builder signature is `builder(cfg: dict) -> common.Lab`.** `cfg` is the
lesson's lab cfg exactly as the author wrote it (`cfg["mode"]` equals the key
the builder is registered under). The builder chooses the view
(`cfg.get("view")`, default the mode's first view), validates everything, and
raises `ValueError` with a message beginning `acckit/<mode>/<view>: ` on
anything wrong. Calling `mode_lab` does all of that for you; you only write
the spec dict.

`acckit.acckit_lab(cfg)` dispatches family A's modes (`delivery`, `flow`,
`branches`, `release`, `change`, `work`) from its own table, and any other
mode through `acckit_b.MODES[mode](cfg)`. An unknown mode raises naming all of
them. Family B never edits `acckit.py`, `labs/__init__.py` or
`build_paths.py`.

**No stub.** `acckit.py` imports `acckit_b` lazily, INSIDE `acckit_lab`, the
first time a mode outside family A is asked for. If `acckit_b.py` does not
exist yet, family B's modes are simply absent (the unknown-mode error lists
only family A's); any other import error inside `acckit_b` is raised, not
swallowed. So `from .acckit import ...` at the top of `acckit_b.py` always
works, and `acckit_b.py` is entirely yours to create. Keep the name `MODES`.

Names you may import from `acckit` (Python): `mode_lab`, `family_intro`,
`KIT`, `CAUTION`, `FAMILY_SENTENCE`, `AKT_CORE_JS`, the field constructors
`arec`, `alist`, `rat`, `TIME`, `CLOCK`, and the exact helpers of section 3b
(`sqrt_fixed`, `root_signed`, `sqrt_exact`, `parse_dec`, `parse_rat`,
`dec_text`, `median`, `pp_text`, `parse_field`, `to_text`).

## 2. `mode_lab(cfg, mode, spec)`

Exactly dddkit's shape. `spec` keys:

| key | meaning |
|---|---|
| `prefix` | the mode's id prefix (section 0) |
| `fn` | the JS compute function's name, `<prefix>Compute` |
| `title` | the lab title shown on the page |
| `js` | the mode's base JS block (defines `<prefix>Compute(view, inst, opts)`) |
| `views` | ordered dict view -> view spec; the first is the default view |

view spec keys:

| key | meaning |
|---|---|
| `fields` | `[(key, field_spec, default)]` in display order, field specs from `eakit_core` (`ea.field(...)`, `ea.rec(...)`, `ea.choice(...)`, a `list` dict) or acckit's own kinds (section 4). `default` None means required |
| `tiles` | `[(label, tile_id)]`; every tile id starts with the prefix |
| `check` | `check(parsed_inputs, fixed)` raising `ValueError(sentence)` on whatever the JS refuses beyond the field parser; or None |
| `subtitle` | short subtitle |
| `rules` | the "How the lab counts." sentence(s), always printed: what is computed, the formula in words, how ties and orders go |
| `js` | the view's JS block |
| `options` | optional `options(cfg, kit, tiles) -> (fixed, extra_cfg_keys, tiles)` for lesson-level cfg keys; default `({}, [], tiles)` |

`mode_lab` builds through acckit's own `_build_lab`, a thin copy of
`eakit_core.build_lab` (dddkit's, with acckit's field kinds). A page ships, in
this order: RATIONAL_JS, EA_CORE_JS, **AKT_CORE_JS**, your `js`, your view's
`js`, then eakit's wiring with its one `eaRead(SPEC, raw)` call replaced by
`aktRead(SPEC, raw)`.

**Panel intro**, set by `mode_lab` unless the lesson's cfg sets
`panel_intro`: "A figure computed from the small sample the lesson states. It
shows what one measure says about that sample; the book's findings are its
survey's, and a correlation is not a cause." A `panel_intro` in the cfg
replaces all but the first sentence (which is prepended if missing).

## 3. JS conventions (both families)

- One pure function `<prefix>Compute(view, inst, opts)` per mode returning
  `{tiles: {id: text}, status: text, table: {caption, head, rows} | null}` or
  `{refuse: sentence}`. Use eakit's pattern:
  `var ALK_VIEW = {}; function alkCompute(view, inst, opts) { return eaRun(ALK_VIEW[view], inst, opts); }`
  and `eaRefuse(sentence)` inside a view.
- **Refusals and messages.** A refusal is one sentence for the reader, with
  no final full stop (the page adds it), naming the record and the value
  (`'Changes, record 3: deployed 2.10:00 is before committed 2.11:30'`). The
  Python `check` raises `ValueError` with **the same sentence**, so a preset
  the page would refuse fails the build. A build error is prefixed
  `acckit/<mode>/<view>: ` by `mode_lab` (and `... preset 'id': ` for a
  preset). Nothing typed is ever evaluated as script.
- **The status line ends with the caution.** Build it with
  `aktStatus(text)`, which strips a final full stop and appends
  `"; the figure is of the sample stated."` (Python: `acckit.CAUTION` is that
  phrase.) Every view of both families does this.
- `scripts/mathcheck.js` extracts every block with the regex
  `NAME = r"""..."""`, so declare each block exactly that way
  (`ALK_VIEW_JS["score"] = r"""`), no other string prefix.
- Numbers: exact BigInt rationals (RATIONAL_JS: `R`, `Radd`, `Rsub`, `Rmul`,
  `Rdiv`, `Rcmp`, `Rparse`, …) and eakit_core's printers (`eaInt`, `eaNum`,
  `eaPct`, `eaFixed`, `eaTimes`, `eaCount`, `eaNames`, `eaPlural`, `eaSum`).
  **Never** `Math.sqrt`, `Number` division or `toFixed` for a printed figure.

### 3a. AKT_CORE_JS (in `acckit.py`, shipped on every acckit page)

| function | does |
|---|---|
| `aktStatus(s)` | the status line with the caution appended (above) |
| `aktRead(spec, raw)` | eakit's `eaRead`, plus acckit's kinds (section 4) |
| `aktIsqrt(n)` | ⌊√n⌋ for a BigInt n ≥ 0, exactly (Newton on BigInt) |
| `aktSqrtFixed(r, places)` | √r for a rational r ≥ 0, printed to exactly `places` decimals, **rounded half up on the exact value**: m = ⌊(⌊√⌊4·r·10^(2·places)⌋⌋ + 1)/2⌋, then the digits of m with the point placed; whole part grouped (`0.707`, `1.000`, `12,345.679`). The digits are a function of r alone |
| `aktRootSigned(sign, sq, places)` | a signed root: `sign` (−1, 0, 1) times √sq, printed as `aktSqrtFixed` with U+2212 for a minus (`−0.866`, `0.000`). For Pearson's r: sign of Sxy, sq = Sxy²/(Sxx·Syy) |
| `aktSqrtExact(r)` | √r as a rational when r is the square of one (`R(3n, 4n)` for 9/16), else `null` |
| `aktParseDec(s, what)` | an exact rational from a decimal typed as text (`0.62`, `-1.5`, `.5`, at most 6 places); THROWS `what + ' should be a number such as 3 or 0.25 …'` otherwise. Fractions are refused |
| `aktParseRat(s, what)` | an exact rational from a decimal (as above) OR a fraction of whole numbers `p/q` (`1/2`, `-3/4`, q > 0); THROWS a sentence otherwise |
| `aktDec(r)` | a rational with a finite decimal, ungrouped, as typed: `106`, `−3.5`, `0.375` (an unending one is cut at 12 places with `…`) |
| `aktMedian(list)` | the median of a non-empty list of rationals: the middle one after sorting, or the mean of the two middle ones (exact) |
| `aktMean(list)` | the exact mean of a non-empty list of rationals |
| `aktPp(r)` | a difference of two shares as signed percentage points: `+20 points`, `+12.5 points` (exact at one place), `≈ −13.3 points` (one place, half away from zero, `≈` when not exact), `0 points` |
| `aktUnit(r, word)` | `eaNum(r)` and a unit, singular (final `s` dropped) when r is exactly ±1: `1 hour`, `3/2 = 1.50 days` |
| `aktTwo(r)` / `aktTimes(r)` | the kit's one rule for ratios: always two places, `≈ ` in front when not exact: `2.00`, `≈ 3.14`; `aktTimes` adds `×` |
| `aktListed(n, parts, sep)` | `"2: a; b"` (sep default `, `), `"0: none"` |
| `aktTime(s, what)` | a time from the period's start: `day.hh:mm` (day 1 is the first day, so `1.09:30` is 9.5 h, `2.00:00` is 24 h) or decimal hours (`37.5`); returns hours as a rational. THROWS a sentence otherwise |
| `aktTimeText(h)` | hours back as `day.hh:mm` when they are whole minutes (`2.10:00`), else the exact hours `aktDec(h) + ' h'` |
| `aktDur(h)` | a duration in hours as `2 d 3 h 15 min`, `45 min`, `0 min`; past whole minutes, `+ 30 s`; past whole seconds the exact hours (`eaNum(h) + ' h'`) |

### 3b. Python helpers (in `acckit.py`), the mirrors

| function | does |
|---|---|
| `sqrt_fixed(fr, places)` | `aktSqrtFixed` on a `Fraction` ≥ 0, the same text |
| `root_signed(sign, sq, places)` | `aktRootSigned` |
| `sqrt_exact(fr)` | `aktSqrtExact`: a `Fraction` or `None` |
| `parse_dec(text, what)` / `parse_rat(text, what)` | `aktParseDec` / `aktParseRat`, raising `ValueError` with the same sentence |
| `dec_text(fr)` | `aktDec` |
| `median(list)` | `aktMedian` on `Fraction`s |
| `pp_text(fr)` | `aktPp` |
| `parse_field(where, f, text)` / `to_text(where, f, value)` | eakit's, reading acckit's kinds too |

## 4. Field formats both families use

From eakit_core, unchanged: records `a, 1; b, 2` (`ea.rec`), lists separated
by spaces or commas (`{"kind": "list", ...}`), whole numbers (`ea.whole`),
decimals with at most 6 places (`ea.num`; fractions like 1/3 are not
accepted), words (`ea.choice`, `ea.word`, `ea.YESNO`), a name or `-`
(`ea.PARENT`). A record list or long list may set `"control": "area"` to get a
textarea. eakit refuses `< > & "` in every shipped value.

acckit adds (Python constructors in `acckit.py`, read by `aktRead`):

- `rat(gt=None, lo=None, hi=ea.LIMIT, dash=False)`: a **rational cell**: a
  decimal (at most 6 places) or a fraction `p/q` of whole numbers
  (`1/2`, `0.25`, `7/3`); bounds as `ea.num`; with `dash=True`, `-` is
  accepted and comes back as the string `'-'`. Use it inside records and
  lists, or alone with `ea.field(what, rat(...))`.
- `TIME`: a **time cell**, `day.hh:mm` or decimal hours (see `aktTime`); with
  `dict(TIME, dash=True)`, `-` for none. Returned as hours (a rational). `CLOCK` is `TIME` with
  `clock: True`: only `day.hh:mm` (a bare number is refused with the reason).
- `arec(what, sub, rest=None, rest_what="value", lo_rest=0, hi_rest=0,
  unique=False, rows=3, lo=1, hi=ea.MAX_RECORDS)`: **records** whose first
  cells follow `sub` (as `ea.rec`, but each cell may be any scalar kind
  including `rat` and `TIME`) and whose remaining cells, `lo_rest` to
  `hi_rest` of them, each follow `rest`. With `rest=None` it is a fixed
  record exactly like `ea.rec`. The parsed record holds the sub-cells by key
  and the tail as a list under `rest` (always present; `[]` when none).
  Family B: Likert answers are `arec("Answers (respondent, then one answer
  per item)", [("respondent", ea.NAME)], ea.whole(1, 7), "answer", 2, 40,
  unique=True)`.
- `alist(what, each, lo=1, hi=ea.MAX_RECORDS, things="values", control="text")`:
  a list separated by spaces or commas whose entries follow any scalar kind
  (`rat`, `TIME`, `ea.whole`, `ea.num`, names; names must be unique).

Record and list sizes are refused in eakit's words ("this lab needs at least
3 records, and there are 2").

## 5. The report and mathcheck

- `docs/accelerate/kit-report.md`: family A owns the top, the "Conventions
  (both families)" section and family A's modes; family B appends its section
  `## Family B (acckit_b.py)` at the end, same per-mode shape as family A's
  (every cfg field, input format with an example string, tile id, label and
  an example value read off a rendered page, refusals, behaviour the tiles do
  not show). If the file does not exist when you need it, create it holding
  only your heading; family A inserts above it. Re-read before every edit.
- `scripts/mathcheck.js`: family A's block is
  `// ---- acckit (Accelerate), family A ----` …
  `// ---- end acckit family A ----`, placed before THE VERDICT (after the
  dddkit blocks). Family B adds
  `// ---- acckit (Accelerate), family B ----` … `// ---- end acckit family B ----`
  immediately after family A's end marker. Re-read the file immediately before
  each edit; both of us are editing it. Copy family A's harness (it loads
  RATIONAL_JS, EA_CORE_JS and AKT_CORE_JS and reads inputs with `aktRead`).
  Family A's block also tests `aktSqrtFixed`, `aktRootSigned`,
  `aktParseDec`/`aktParseRat` and `aktMedian`, so family B need not.
- Example samples are the lesson's own, never the book's (PLAN §C): no row of
  Tables 2.2/2.3 or B.1, no figure's bars, no ING teams.
- The lab never grades a team; a tile states what one measure says about the
  sample, and the status line's caution says so.
