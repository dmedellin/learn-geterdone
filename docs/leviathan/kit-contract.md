# levkit: the contract between family A (`levkit.py`) and family B (`levkit_b.py`)

Written by family A's engineer for family B's. PLAN §D is the spec; this file
fixes only the seam between the two modules. If anything here changes, the
change is announced at the top of this file with a time (UTC).

**No prefix changes.** Every PLAN §D prefix is used as given (section 0).

## 0. Id prefixes (decided at the start, 2026-11-14 02:30)

Grepped `scripts/mathpath/labs/*.py` and `scripts/*.js` for every PLAN prefix
as an identifier start (`\b<prefix>[A-Z0-9_]`, lower-case and upper-case
forms) on branch `feat/leviathan-subject`:

- Free: family A `lrk lde lwo leq lcv`, family B `las lsu ltx llw lcn`,
  shared helpers `lvk` / `LVK_`.
- The only hit is `LAS` followed by a capital: the English word `LAST` in
  comments (`algo_core.py`, `dpseq.py`, `estimate.py`, `or_core.py`,
  `replica.py`, `sortkit.py`, `mathcheck.js`). No identifier begins `LAS_` or
  `las`, so `las` stands; family B: name your view table `LAS_VIEW`, never
  `LAST…`.
- There is no other local or remote branch than `main` in this checkout.

Every id, JS function and JS variable of a mode begins with its prefix
(`lasCompute`, `LAS_VIEW`, `lasInMembers`, `lasPreset`); shared helpers begin
`lvk` / `LVK_`, and only `levkit.py` defines those. Family B must not define
names beginning `lvk`/`LVK_`.

## 1. What `levkit_b.py` exposes

```python
# scripts/mathpath/labs/levkit_b.py
from . import eakit_core as ea
from .levkit import mode_lab, lrec, llist, rat, NAMES, NAMES_DASH   # safe at module top

LAS_JS = r"""..."""                   # the mode's base block (defines lasCompute)
LAS_VIEW_JS = {}
LAS_VIEW_JS["voices"] = r"""..."""     # one block per view

ASSEMBLY = {                          # one spec dict per mode (section 2)
    "prefix": "las", "fn": "lasCompute", "title": "An assembly's voices", "js": LAS_JS,
    "views": {
        "voices": {"fields": [...], "tiles": [...], "check": _check_voices,
                   "subtitle": "...", "rules": "...", "js": LAS_VIEW_JS["voices"]},
        "ties": {...},
    },
}

MODES = {"assembly": lambda cfg: mode_lab(cfg, "assembly", ASSEMBLY),
         "succession": ..., "tax": ..., "law": ..., "canon": ...}
```

**The builder signature is `builder(cfg: dict) -> common.Lab`.** `cfg` is the
lesson's lab cfg exactly as the author wrote it (`cfg["mode"]` equals the key
the builder is registered under). The builder chooses the view
(`cfg.get("view")`, default the mode's first view), validates everything, and
raises `ValueError` with a message beginning `levkit/<mode>/<view>: ` on
anything wrong. Calling `mode_lab` does all of that for you; you only write
the spec dict.

`levkit.levkit_lab(cfg)` dispatches family A's modes (`reckon`, `deliberate`,
`worth`, `equality`, `covenant`) from its own table, and any other mode
through `levkit_b.MODES[mode](cfg)`. An unknown mode raises naming all of
them. Family B never edits `levkit.py`, `labs/__init__.py` or
`build_paths.py` (family A registers `"levkit"` in both).

**No stub.** `levkit.py` imports `levkit_b` lazily, INSIDE `levkit_lab`, the
first time a mode outside family A is asked for. If `levkit_b.py` does not
exist yet, family B's modes are simply absent (the unknown-mode error lists
only family A's); any other import error inside `levkit_b` is raised, not
swallowed. So `from .levkit import ...` at the top of `levkit_b.py` always
works, and `levkit_b.py` is entirely yours to create. Keep the name `MODES`.

Names you may import from `levkit` (Python): `mode_lab`, `family_intro`,
`KIT`, `CAUTION`, `FAMILY_SENTENCE`, `LVK_CORE_JS`, the field constructors
`lrec`, `llist`, `rat`, `NAMES`, `NAMES_DASH` (section 4), and the exact
helpers of section 3b (`parse_rat`, `dec_text`, `num_text`, `pct_text`,
`plural`, `quote`, `parse_field`, `to_text`, `MINUS`).

## 2. `mode_lab(cfg, mode, spec)`

acckit's shape exactly. `spec` keys:

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
| `fields` | `[(key, field_spec, default)]` in display order, field specs from `eakit_core` (`ea.field(...)`, `ea.rec(...)`, `ea.choice(...)`, a `list` dict) or levkit's own kinds (section 4). `default` None means required |
| `tiles` | `[(label, tile_id)]`; every tile id starts with the prefix |
| `check` | `check(parsed_inputs, fixed)` raising `ValueError(sentence)` on whatever the JS refuses beyond the field parser; or None |
| `subtitle` | short subtitle |
| `rules` | the "How the lab counts." sentence(s), always printed: what is computed, the rule in words, how ties and orders go |
| `js` | the view's JS block |
| `options` | optional `options(cfg, kit, tiles) -> (fixed, extra_cfg_keys, tiles)` for lesson-level cfg keys that are not inputs; default `({}, [], tiles)` |

`mode_lab` builds through levkit's own `_build_lab`, a thin copy of acckit's
(itself eakit_core's `build_lab` with extra field kinds). A page ships, in
this order: RATIONAL_JS, EA_CORE_JS, **LVK_CORE_JS**, your `js`, your view's
`js`, then eakit's wiring with its one `eaRead(SPEC, raw)` call replaced by
`lvkRead(SPEC, raw)`.

A cfg key named like one of the view's inputs supplies it to every preset
that does not set it (eakit's rule). Any other cfg key that is not common
(`mode view presets preset title panel_title panel_intro`) or declared by
`options` raises.

**Panel intro**, set by `mode_lab` unless the lesson's cfg sets
`panel_intro`: "A figure computed from what the lesson states. It shows what
follows on Hobbes’s definitions as written here; whether they describe men
and commonwealths is what the book argues." A `panel_intro` in the cfg
replaces it; its first sentence ("A figure computed from what the lesson
states.") is put back in front if missing.

## 3. JS conventions (both families)

- One pure function `<prefix>Compute(view, inst, opts)` per mode returning
  `{tiles: {id: text}, status: text, table: {caption, head, rows} | null}` or
  `{refuse: sentence}`. Use eakit's pattern:
  `var LAS_VIEW = {}; function lasCompute(view, inst, opts) { return eaRun(LAS_VIEW[view], inst, opts); }`
  and `eaRefuse(sentence)` inside a view.
- **Refusals and messages.** A refusal is one sentence for the reader, with
  no final full stop (the page adds it), naming the record and the value
  (`'Members, record 3: x is named twice'`). The Python `check` raises
  `ValueError` with **the same sentence**, so a preset the page would refuse
  fails the build. A build error is prefixed `levkit/<mode>/<view>: ` by
  `mode_lab` (and `... preset 'id': ` for a preset). Nothing typed is ever
  evaluated as script.
- **The status line ends with the caution.** Build it with
  `lvkStatus(text)`, which strips a final full stop and appends
  `"; the figure follows from what the lesson states, on Hobbes’s definitions as stated."`
  (Python: `levkit.CAUTION` is that phrase, without the `"; "` and the full
  stop; the apostrophe is U+2019.) Every view of both families does this.
- `scripts/mathcheck.js` extracts every block with the regex
  `NAME = r"""..."""`, so declare each block exactly that way
  (`LAS_VIEW_JS["voices"] = r"""`), no other string prefix.
- Numbers: exact BigInt rationals (RATIONAL_JS: `R`, `Radd`, `Rsub`, `Rmul`,
  `Rdiv`, `Rcmp`, `Rparse`, …) and eakit_core's printers (`eaInt`, `eaNum`,
  `eaFixed`, `eaCount`, `eaNames`, `eaPlural`, `eaSum`). **Never**
  `Math.sqrt`, `Number` division or `toFixed` for a printed figure.
- **Probabilities and shares print with `lvkPct`** (PLAN §D: "the fraction and
  its percentage to at most two decimals"), not `eaPct` (one place).

### 3a. LVK_CORE_JS (in `levkit.py`, shipped on every levkit page)

| function | does |
|---|---|
| `lvkStatus(s)` | the status line with the caution appended (above) |
| `lvkRead(spec, raw)` | eakit's `eaRead`, plus levkit's kinds (section 4) |
| `lvkParseRat(s, what)` | an exact rational from a decimal (`0.25`, `-1.5`, `.5`, at most 6 places) OR a fraction of whole numbers `p/q` (`1/3`, `-3/4`, at most 8 digits above and below, q > 0); THROWS a sentence otherwise (`what + ' "1/0" divides by zero'`, `what + ' should be a number such as 3, 0.25 or 1/2, and "x" is not one'`) |
| `lvkDec(r)` | a rational with a finite decimal, ungrouped, as typed: `106`, `−3.5`, `0.375` (an unending one is cut at 12 places with `…`) |
| `lvkPct(r)` | a chance or share: the fraction (or whole number) and its percentage to at most two decimals, trailing zeros dropped, `=` when that is exact and `≈` (rounded half away from zero at two places) when not: `1/4 = 25%`, `1/8 = 12.5%`, `1/3 ≈ 33.33%`, `2/3 ≈ 66.67%`, `0 = 0%`, `1 = 100%`, `1/400 = 0.25%`, `1/30000 ≈ 0%` |
| `lvkListed(n, parts, sep)` | `"2: a; b"` (sep default `, `), `"0: none"` |
| `lvkNameSeq(text, f, what)` | the NAMES cell (section 4): names separated by spaces, returned as an array of strings in the order typed |

### 3b. Python helpers (in `levkit.py`), the mirrors

| function | does |
|---|---|
| `parse_rat(text, what)` | `lvkParseRat`, raising `ValueError` with the same sentence |
| `dec_text(fr)` | `lvkDec` |
| `num_text(fr)` | `eaNum` for figures below 30 digits: `4`, `3/2 = 1.50`, `2/7 ≈ 0.29` |
| `pct_text(fr)` | `lvkPct` |
| `plural(n, one, many)` | `eaPlural` |
| `quote(s)` | `eaQuote` |
| `parse_field(where, f, text)` / `to_text(where, f, value)` | eakit's, reading levkit's kinds too |

## 4. Field formats both families use

From eakit_core, unchanged: records `a, 1; b, 2` (`ea.rec`), lists separated
by spaces or commas (`{"kind": "list", ...}`), whole numbers (`ea.whole`),
decimals with at most 6 places (`ea.num`), words (`ea.choice`, `ea.word`,
`ea.YESNO`), a name or `-` (`ea.PARENT`). eakit refuses `< > & "` in every
shipped value.

**Names (both families).** A name is eakit's `ea.NAME`: letters, digits,
`.`, `_`, `-`, no spaces. **A name of several words is written with
hyphens**: `round-quadrangle`, `natural-philosophy`, `body-politic`. Names
are compared exactly as typed (case and punctuation count: `Body` and `body`
are two names, and so are `round-quadrangle` and `round_quadrangle`). Print a
name as typed.

levkit adds (Python constructors in `levkit.py`, read by `lvkRead`):

- `rat(gt=None, lo=None, hi=ea.LIMIT, dash=False)`: a **rational cell**: a
  decimal (at most 6 places) or a fraction `p/q` of whole numbers
  (`1/2`, `0.25`, `7/3`); bounds `gt` (more than), `lo` (at least), `hi` (at
  most); with `dash=True`, `-` is accepted and comes back as the string
  `'-'`. A chance is `rat(lo=0, hi=1)`. Use it inside records and lists, or
  alone with `ea.field(what, rat(...))`.
- `NAMES`: a **cell of names separated by spaces** (inside a record cell,
  whose cells are separated by commas): `space-separated parts` such as
  `body animated rational`. One name or more; a name twice in one cell is
  refused (`... names "body" twice`). `NAMES_DASH`: the same, or `-` alone
  for none (comes back as `[]`). Returned as an array of strings. Alone as a
  field: `ea.field(what, NAMES)`.
- `lrec(what, sub, rest=None, rest_what="value", lo_rest=0, hi_rest=0,
  unique=False, rows=3, lo=1, hi=ea.MAX_RECORDS)`: **records** whose first
  cells follow `sub` (each cell any scalar kind including `rat` and `NAMES`)
  and whose remaining cells, `lo_rest` to `hi_rest` of them, each follow
  `rest`. With `rest=None` it is a fixed record like `ea.rec`. The parsed
  record holds the sub-cells by key and the tail as a list under `rest`
  (always present; `[]` when none). Refusal wording: `<what>, record 3 has 2
  fields; this list needs 3 (a, b, c)`, `<what>, record 3: cost1 should be a
  number such as 3, 0.25 or 1/2, and "x" is not one`, `<what> names "x"
  twice` (with `unique`).
- `llist(what, each, lo=1, hi=ea.MAX_RECORDS, things="values", control="text")`:
  a list separated by spaces or commas whose entries follow any scalar kind
  (`rat`, `ea.whole`, `ea.num`, names; names must be unique).

Record and list sizes are refused in eakit's words ("this lab needs at least
3 records, and there are 2").

## 5. The report and mathcheck

- `docs/leviathan/kit-report.md`: family A owns the top (the readiness note),
  the "Conventions (both families)" section and family A's modes; family B
  appends its section `## Family B (levkit_b.py)` at the end, same per-mode
  shape as family A's (every cfg field, input format with an example string,
  tile id, label and an example value read off a rendered page, refusals,
  rules sentence). If the file does not exist when you need it, create it
  holding only your heading; family A inserts above it. Re-read before every
  edit, and edit only your own section. Family B may add its views to the
  readiness note's line at the top (one line per family).
- `scripts/mathcheck.js`: family A's block is
  `// ---- levkit (Leviathan), family A ----` …
  `// ---- end levkit family A ----`, placed before THE VERDICT (after the
  acckit family B block). Family B adds
  `// ---- levkit (Leviathan), family B ----` … `// ---- end levkit family B ----`
  immediately after family A's end marker (if family A's block is not there
  yet, put yours immediately before THE VERDICT; family A will insert above
  it). Re-read the file immediately before each edit; both of us are editing
  it. Copy family A's harness (it loads RATIONAL_JS, EA_CORE_JS and
  LVK_CORE_JS and reads inputs with `lvkRead`). Family A's block also tests
  `lvkParseRat`, `lvkPct`, `lvkDec` and the NAMES cell, so family B need not.
- Lesson instances are the lesson's own (PLAN §C); Hobbes's own definitions
  and lists may be lab data with the chapter cited.
- The lab never decides whether Hobbes is right; the status line's caution
  says so.
