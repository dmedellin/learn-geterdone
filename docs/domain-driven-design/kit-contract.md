# dddkit: the contract between family A (`dddkit.py`) and family B (`dddkit_b.py`)

Written by family A's engineer for family B's. PLAN §D is the spec; this file
fixes only the seam between the two modules. If anything here changes, the
change is announced at the top of this file with a time.

**Change, 2026-11-01 (after the first version):** section 3's table corrected —
`dddValue` returns `{kind: 'num', r}` / `{kind: 'word', w}` (not `{num}` /
`{word}`), `dddValText` prints decimals as typed; `dddDec` and `dddListed`
added. Nothing else changed.

## 0. Id prefixes (decided at the start, 2026-11-01)

Grepped `scripts/mathpath/labs/*.py` and `scripts/*.js` for every PLAN prefix
as an identifier start (`\b<prefix>[A-Z0-9_]`):

- **`dag` collides** (`dagRelax`, `dagSchedule`, `dagCriticalPath`, `dagE`,
  `dagT` exist in other kits). The aggregate mode uses **`dgr`** instead
  (`dgrCompute`, `DGR_VIEW`, `dgrInObjects`, `dgrPreset`). This is the only
  change.
- Free and used as the PLAN gives them: family A `dln das did dsp` (+ `dgr`),
  family B `dmo dcx dds dle`, shared helpers `ddd` / `DDD_`.

Every id, JS function and JS variable of a mode begins with its prefix
(`dmoCompute`, `DMO_VIEW`, `dmoInElements`, `dmoPreset`, `dmoShareInside`);
shared helpers begin `ddd` / `DDD_`, and only `dddkit.py` defines those.
Family B must not define names beginning `ddd`/`DDD_`.

## 1. What `dddkit_b.py` exposes

```python
# scripts/mathpath/labs/dddkit_b.py
from . import eakit_core as ea
from .dddkit import mode_lab          # see section 2; safe at module top

DMO_JS = r"""..."""                   # the mode's base block (defines dmoCompute)
DMO_VIEW_JS = {}
DMO_VIEW_JS["cohesion"] = r"""..."""   # one block per view

MODULES = {                           # one spec dict per mode (section 2)
    "prefix": "dmo", "fn": "dmoCompute", "title": "Modules", "js": DMO_JS,
    "views": {
        "cohesion": {"fields": [...], "tiles": [...], "check": _check_cohesion,
                     "subtitle": "...", "rules": "...", "js": DMO_VIEW_JS["cohesion"]},
    },
}

MODES = {"modules": lambda cfg: mode_lab(cfg, "modules", MODULES),
         "context": ..., "distill": ..., "ledger": ...}
```

**The builder signature is `builder(cfg: dict) -> common.Lab`.** `cfg` is the
lesson's lab cfg exactly as the author wrote it (`cfg["mode"]` equals the key
the builder is registered under). The builder chooses the view
(`cfg.get("view")`, default the mode's first view), validates everything, and
raises `ValueError` with a message beginning `dddkit/<mode>/<view>: ` on
anything wrong. Calling `mode_lab` does all of that for you; you only write
the spec dict.

`dddkit.dddkit_lab(cfg)` dispatches: family A's modes (`lang`, `assoc`,
`identity`, `aggregate`, `spec`) from its own table, any other mode through
`dddkit_b.MODES[mode](cfg)`. An unknown mode raises naming all of them.
Family B never edits `dddkit.py`, `labs/__init__.py` or `build_paths.py`.

**The stub.** So that `dddkit` can be registered before family B lands,
family A created `scripts/mathpath/labs/dddkit_b.py` as a stub holding only
`MODES = {}` (and a docstring). **Family B replaces that file wholesale**; it
is yours. Keep the name `MODES`.

`dddkit.py` imports `dddkit_b` with a plain `from . import dddkit_b` at the
BOTTOM of the module (after `mode_lab` is defined) and reads `dddkit_b.MODES`
only inside `dddkit_lab`. So `from .dddkit import mode_lab` at the top of
`dddkit_b.py` works whichever module is imported first. Do not read anything
from `dddkit` at import time other than the names defined above that bottom
import: `mode_lab`, `DDD_CORE_JS`, `KIT`, `family_intro`, `CAUTION`,
`vrec`, `expr`.

## 2. `mode_lab(cfg, mode, spec)`

Exactly itakit's shape. `spec` keys:

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
| `fields` | `[(key, field_spec, default)]` in display order, field specs from `eakit_core` (`ea.field(...)`, `ea.rec(...)`, `ea.choice(...)`, a `list` dict) or dddkit's own two kinds (section 4). `default` None means required |
| `tiles` | `[(label, tile_id)]`; every tile id starts with the prefix |
| `check` | `check(parsed_inputs, fixed)` raising `ValueError(sentence)` on whatever the JS refuses beyond the field parser; or None |
| `subtitle` | short subtitle |
| `rules` | the "How the lab counts." sentence(s), always printed: what is counted, how ties and orders go |
| `js` | the view's JS block |
| `options` | optional `options(cfg, kit, tiles) -> (fixed, extra_cfg_keys, tiles)` for lesson-level cfg keys; default `({}, [], tiles)` |

There is no `family` key: every dddkit view is a count over the model the
lesson states.

`mode_lab` builds through dddkit's own `_build_lab`, a thin copy of
`eakit_core.build_lab` (it reuses eakit_core's parser, printers, markup
helpers and wiring unchanged) that adds two field kinds (section 4). A page
ships, in this order: RATIONAL_JS, EA_CORE_JS, **DDD_CORE_JS**, your `js`,
your view's `js`, then eakit's wiring with its one `eaRead(SPEC, raw)` call
replaced by `dddRead(SPEC, raw)`.

**Panel intro**, set by `mode_lab` unless the lesson's cfg sets
`panel_intro`: "A count over the small model the lesson states. The lab counts
one consequence of one modelling choice; the choice itself is weighed in the
book, against the domain, the team and the project." A `panel_intro` in the
cfg replaces all but the first sentence (which is prepended if missing).

## 3. JS conventions (both families)

- One pure function `<prefix>Compute(view, inst, opts)` per mode returning
  `{tiles: {id: text}, status: text, table: {caption, head, rows} | null}` or
  `{refuse: sentence}`. Use eakit's pattern:
  `var DMO_VIEW = {}; function dmoCompute(view, inst, opts) { return eaRun(DMO_VIEW[view], inst, opts); }`
  and `eaRefuse(sentence)` inside a view.
- **The status line ends with the caution.** Build it with
  `dddStatus(text)`, which strips a final full stop and appends
  `"; the count is of the model stated."` (Python: `dddkit.CAUTION` is that
  phrase.) Every view of both families does this.
- `scripts/mathcheck.js` extracts every block with the regex
  `NAME = r"""..."""`, so declare each block exactly that way
  (`DMO_VIEW_JS["cohesion"] = r"""`), no other string prefix.
- Numbers: exact BigInt rationals (RATIONAL_JS: `R`, `Radd`, `Rmul`, `Rcmp`,
  `Rparse`, …) and eakit_core's printers (`eaInt`, `eaNum`, `eaPct`,
  `eaTimes`, `eaCount`, `eaNames`, …).

**DDD_CORE_JS** (in `dddkit.py`, shipped on every dddkit page) provides:

| function | does |
|---|---|
| `dddStatus(s)` | the status line with the caution appended (above) |
| `dddRead(spec, raw)` | eakit's `eaRead`, plus the two kinds of section 4 |
| `dddValue(text, what)` | an attribute value: `{kind: 'num', r: R}` for a decimal (eakit's number syntax, at most 6 places, size at most 10,000,000), else `{kind: 'word', w: s}` for a word beginning with a letter; throws a sentence otherwise |
| `dddValText(v)` | a value back as text, as typed: `3`, `0.25`, `−1.5`, `rye` (no grouping) |
| `dddDec(r)` | a rational with a finite decimal, ungrouped: `106`, `−3.5` |
| `dddListed(n, parts, sep)` | `"2: a; b"` (sep default `, `), `"0: none"` |
| `dddValEq(a, b)` | equal kind and equal value (numbers exactly, words exactly) |
| `dddKey(s)` | a name folded for comparison ignoring letter case (`lower-case`) |
| `dddQ(r)` | a rational as a bare exact fraction (`3`, `−1/2`, `1,024/3`) |

## 4. Field formats both families use

From eakit_core, unchanged: records `a, 1; b, 2` (`ea.rec`), lists separated
by spaces or commas (`{"kind": "list", ...}`), whole numbers (`ea.whole`),
decimals with at most 6 places (`ea.num`; fractions like 1/3 are not
accepted), words (`ea.choice`), a name or `-` (`ea.PARENT`). A record list or
long list may set `"control": "area"` to get a textarea. eakit refuses
`< > & "` in every shipped value of these kinds.

dddkit adds two kinds (Python constructors in `dddkit.py`):

- `vrec(what, sub, rest, rest_what, lo_rest, hi_rest, unique=..., lo=, hi=)`:
  records whose first cells follow `sub` (as `ea.rec`) and whose remaining
  cells, `lo_rest` to `hi_rest` of them, each follow `rest` — another scalar
  spec, or `{"kind": "kv"}` for a `key=value` cell (key a name, value a
  decimal or a name, keys unique within a record). Family A uses it for
  glossary rows (`loan, loan, Loan, loan_record`) and for objects and
  candidates with attributes (`c1, pages=320, genre=crime`).
- `expr(what)`: a one-expression box (the `spec` mode's specification),
  at most 300 characters, read by the view's own parser; it may hold `<`
  and `>`, so like cckit's condition box it is EMPTY in the markup and filled
  by script from the preset.

## 5. The report and mathcheck

- `docs/domain-driven-design/kit-report.md`: family A owns the top and the
  "Conventions (both families)" section and family A's modes; family B
  appends its section `## Family B (dddkit_b.py)` at the end, same per-mode
  shape as family A's (every cfg field, input format with an example string,
  tile id, label and an example value, refusals, behaviour the tiles do not
  show).
- `scripts/mathcheck.js`: family A's block is
  `// ---- dddkit (Domain-Driven Design), family A ----` …
  `// ---- end dddkit family A ----`, placed before THE VERDICT. Family B adds
  `// ---- dddkit (Domain-Driven Design), family B ----` … `// ---- end dddkit family B ----`
  immediately after family A's end marker. Re-read the file immediately before
  each edit; both of us are editing it. Copy family A's harness (it loads
  RATIONAL_JS, EA_CORE_JS and DDD_CORE_JS and reads inputs with `dddRead`).
- Example domains are the lesson's own, never the book's (PLAN §C): library,
  clinic, bakery, bike-share, theatre, seed bank, school timetable.

## Family B notes

- The seam works as written; `dddkit_b.py` replaces the stub and imports
  `mode_lab, vrec` from `dddkit`. distill's parts use `vrec` (an optional
  fifth `option` cell). No `ddd`/`DDD_` names are defined in family B.
- `docs/domain-driven-design/kit-report.md` did not exist when course authors
  needed family B's section, so family B created the file with only
  `## Family B (dddkit_b.py)` in it. Family A: put your top and "Conventions
  (both families)" ABOVE that heading (insert, do not overwrite the file).
- mathcheck: family B's block sits directly after family A's end marker.
