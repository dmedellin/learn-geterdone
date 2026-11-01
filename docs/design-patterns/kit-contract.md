# gofkit: the contract between family A (`gofkit.py`) and family B (`gofkit_b.py`)

Written by family A's engineer for family B's. PLAN §D is the spec; this file
fixes only the seam between the two modules. It follows
`docs/domain-driven-design/kit-contract.md` (dddkit's) wherever it is silent.
If anything here changes, the change is announced at the top of this file with
a time.

**Change, 2026-11-01 (after the first version):** section 3's GOF_CORE_JS
table gained `gofDec`, `gofNum` and `gofHas` (additions only). The exported
names and the seam are unchanged.

## 0. Id prefixes (decided at the start, 2026-11-01)

Grepped `scripts/mathpath/labs/*.py` and `scripts/*.js` for every PLAN prefix
as an identifier start (`\b<prefix>[A-Z0-9_]`, lower and upper case):

- All free as the PLAN gives them. Family A `gcl gtr gex`, family B
  `grt gno ghi gsm gsh gpx`, shared helpers `gof` / `GOF_`.
- The only hit was `GEXP`, a local variable inside `algebra_basics.py`; it is
  not a `gex` name and never ships on a gofkit page, so `gex` stands. No
  prefix is changed.

Every id, JS function and JS variable of a mode begins with its prefix
(`grtCompute`, `GRT_VIEW`, `grtInHandlers`, `grtPreset`); shared helpers begin
`gof` / `GOF_`, and only `gofkit.py` defines those. Family B must not define
names beginning `gof`/`GOF_`.

## 1. What `gofkit_b.py` exposes

```python
# scripts/mathpath/labs/gofkit_b.py
from . import eakit_core as ea
from .gofkit import mode_lab, vrec, expr        # safe at module top (section 2)
# and, if wanted: GOF_CORE_JS, KIT, CAUTION, family_intro

GRT_JS = r"""..."""                    # the mode's base block (defines grtCompute)
GRT_VIEW_JS = {}
GRT_VIEW_JS["chain"] = r"""..."""      # one block per view

ROUTE = {                              # one spec dict per mode (section 2)
    "prefix": "grt", "fn": "grtCompute", "title": "...", "js": GRT_JS,
    "views": {"chain": {"fields": [...], "tiles": [...], "check": _check_chain,
                        "subtitle": "...", "rules": "...", "js": GRT_VIEW_JS["chain"]}},
}

MODES = {"route": lambda cfg: mode_lab(cfg, "route", ROUTE),
         "notify": ..., "history": ..., "machine": ..., "share": ..., "proxy": ...}
```

**The builder signature is `builder(cfg: dict) -> common.Lab`**, exactly as
dddkit's. `mode_lab` chooses the view (`cfg.get("view")`, default the mode's
first), validates everything, and raises `ValueError` with a message beginning
`gofkit/<mode>/<view>: `.

`gofkit.gofkit_lab(cfg)` dispatches family A's modes (`classes`, `tree`,
`expr`) from its own table, any other mode through
`gofkit_b.MODES[mode](cfg)`. An unknown mode raises naming all of them.
Family B never edits `gofkit.py`, `labs/__init__.py` or `build_paths.py`.

**The file.** `gofkit_b.py` is family B's (they created it, a stub with
`MODES = {}` first). Family A never edits it. Keep the name `MODES`.

`gofkit.py` imports it with a plain `from . import gofkit_b` at the BOTTOM of
the module (after `mode_lab` is defined) and reads `gofkit_b.MODES` only inside
`gofkit_lab`. So `from .gofkit import ...` at the top of `gofkit_b.py` works
whichever module is imported first. **The names exported for family B, and
stable:** `mode_lab`, `vrec`, `expr`, `GOF_CORE_JS`, `KIT` (`"gofkit"`),
`CAUTION` (`"the count is of the design stated"`), `family_intro`. (`vrec` and
`expr` are dddkit's own, re-exported unchanged.)

## 2. `mode_lab(cfg, mode, spec)`

dddkit's spec-dict shape, unchanged (dddkit's contract §2): spec keys `prefix`,
`fn`, `title`, `js`, `views`; view keys `fields`, `tiles`, `check`,
`subtitle`, `rules`, `js`, optional `options(cfg, kit, tiles) -> (fixed,
extra_cfg_keys, tiles)`. Every tile id must begin with the prefix.

It builds through a thin copy of dddkit's `_build_lab` (dddkit's adds dddkit's
own first sentence to every panel intro, so it cannot be reused as is); the
copy reuses dddkit's preset reader, its two field kinds and its `dddRead`
wiring unchanged. A page ships, in this order: RATIONAL_JS, EA_CORE_JS,
DDD_CORE_JS, **GOF_CORE_JS**, the mode's `js`, the view's `js`, then the
wiring (which reads inputs with `dddRead(SPEC, raw)`).

**Panel intro**, set by `mode_lab` unless the lesson's cfg sets
`panel_intro`: "A count over the small design the lesson states. The lab
counts one consequence of applying a pattern or not; whether the pattern fits
is weighed in the book, against what in the design is expected to vary." A
`panel_intro` in the cfg replaces all but the first sentence (which is
prepended if missing).

## 3. JS conventions (both families)

- One pure function `<prefix>Compute(view, inst, opts)` per mode returning
  `{tiles, status, table}` or `{refuse}`, via eakit's pattern
  `var GRT_VIEW = {}; function grtCompute(view, inst, opts) { return eaRun(GRT_VIEW[view], inst, opts); }`
  and `eaRefuse(sentence)` inside a view.
- **The status line ends with the caution.** Build it with `gofStatus(text)`,
  which strips a final full stop and appends
  `"; the count is of the design stated."` Every view of both families does
  this (never `dddStatus`, whose caution says "model").
- Declare each JS block exactly `NAME = r"""` (mathcheck extracts them so).
- Numbers: exact BigInt rationals (RATIONAL_JS) and eakit's printers.
- Family B may call DDD_CORE_JS helpers (`dddValue`, `dddDec`, `dddListed`,
  `dddKey`, `dddQ`, `dddValText`, `dddValEq`): every gofkit page ships them.

**GOF_CORE_JS** (in `gofkit.py`, shipped on every gofkit page) provides:

| function | does |
|---|---|
| `gofStatus(s)` | the status line with the caution appended (above) |
| `gofCount(n, one, many)` | `"1 class"`, `"3 classes"` (grouped with `eaInt`; the same as `eaPlural`) |
| `gofDec(r)` | a rational with a finite decimal of at most 6 places, grouped: `15.5`, `1,234.567`; else `eaNum(r)` |
| `gofNum(r)` | an exact value: `12`, `7/8 = 0.875`, `2/3 ≈ 0.67`, very long ones `≈ 1.23 × 10^40` |
| `gofHas(o, k)` | own-property test (`Object.prototype.hasOwnProperty.call`) |

## 4. Field formats

dddkit's contract §4, unchanged: eakit's kinds (`ea.rec`, lists, `ea.whole`,
`ea.num`, `ea.choice`, `ea.PARENT`) and dddkit's `vrec` and `expr`
(re-exported from `gofkit`).

## 5. The report and mathcheck

- `docs/design-patterns/kit-report.md`: family A owns the top, the
  "Conventions (both families)" section and family A's modes; family B appends
  `## Family B (gofkit_b.py)` at the end, same per-mode shape. If family B
  creates the file first, family A inserts above that heading.
- `scripts/mathcheck.js`: family A's block is
  `// ---- gofkit (Design Patterns), family A ----` …
  `// ---- end gofkit family A ----`, placed before THE VERDICT. Family B adds
  `// ---- gofkit (Design Patterns), family B ----` …
  `// ---- end gofkit family B ----` immediately after family A's end marker.
  Re-read the file immediately before each edit; both of us edit it. Copy
  family A's harness (it loads RATIONAL_JS, EA_CORE_JS, DDD_CORE_JS and
  GOF_CORE_JS and reads inputs with `dddRead`).
- Example domains are the lesson's own, never the book's (PLAN §C lists what
  is forbidden).
