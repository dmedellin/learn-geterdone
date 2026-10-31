# itakit: the contract between family A (`itakit.py`) and family B (`itakit_b.py`)

Written by family A's engineer for family B's. PLAN §D is the spec; this file
fixes only the seam between the two modules. If anything here changes, the
change is announced at the top of this file with a time.

## 0. Id prefixes: the PLAN's two letters plus `i` (decided at the start)

The two-letter prefixes in PLAN §D are already taken by other kits
(`grCompute`, `hrPreset`, `ftStatus`, `rdAsk`, `obJobs`, `amCeil`, `btCap`,
`bfAgree`, `vbCons`, … all exist in `scripts/mathpath/labs/*.py`). So every
itakit id, JS function and JS variable uses the **PLAN prefix followed by a
lower-case `i`**: family A `gri sti rci msi hri wsi lui fti`, family B
`rdi lci obi ami rbi bti fhi vbi bfi` (grepped 2026-10-31: none of the
eighteen is used anywhere in `labs/*.py`). Examples: `rdiCompute`,
`RDI_VIEW`, `rdiInPrices`, `rdiPreset`, `rdiRevenue`. The ids still begin
with the PLAN's mode prefix. Shared helpers begin with `ita`/`ITA_`.

## 1. What `itakit_b.py` exposes

```python
# scripts/mathpath/labs/itakit_b.py
from . import eakit_core as ea
from .itakit import mode_lab          # see section 2; safe at module top

RDI_JS = r"""..."""                   # the mode's base block (defines rdiCompute)
RDI_VIEW_JS = {}
RDI_VIEW_JS["cut"] = r"""..."""        # one block per view

ROD = {                               # one spec dict per mode (section 2)
    "prefix": "rdi", "fn": "rdiCompute", "title": "Rod cutting", "js": RDI_JS,
    "views": {
        "cut": {"fields": [...], "tiles": [...], "check": _check_cut,
                "subtitle": "...", "rules": "...", "js": RDI_VIEW_JS["cut"]},
    },
}

def rod_lab(cfg):
    return mode_lab(cfg, "rod", ROD)

MODES = {"rod": rod_lab, "lcs": lcs_lab, "obst": obst_lab, "amortized": amortized_lab,
         "rbtree": rbtree_lab, "btree": btree_lab, "fibheap": fibheap_lab, "veb": veb_lab,
         "bfs": bfs_lab}
```

**The builder signature is `builder(cfg: dict) -> common.Lab`.** `cfg` is the
lesson's lab cfg exactly as the author wrote it (`cfg["mode"]` equals the key
the builder is registered under). The builder chooses the view
(`cfg.get("view")`, default the mode's first view), validates everything, and
raises `ValueError` with a message beginning `itakit/<mode>/<view>: ` on
anything wrong. It returns the `Lab` that `eakit_core.build_lab` returns.
Calling `mode_lab` does all of that for you; you only write the spec dict.

`itakit.itakit_lab(cfg)` dispatches: family A's modes from its own table, any
other mode through `itakit_b.MODES[mode](cfg)`. An unknown mode raises naming
all seventeen. Family B never edits `itakit.py`, `labs/__init__.py` or
`build_paths.py`.

`itakit.py` imports `itakit_b` with a plain `from . import itakit_b` at the
BOTTOM of the module (after `mode_lab` is defined), and reads
`itakit_b.MODES` only inside `itakit_lab`. So `from .itakit import mode_lab`
at the top of `itakit_b.py` works whichever module is imported first. Do not
read anything from `itakit` at import time other than names defined above that
bottom import (`mode_lab`, `ITA_CORE_JS`, `KIT`, `family_intro`).

## 2. `mode_lab(cfg, mode, spec)`

`spec` keys:

| key | meaning |
|---|---|
| `prefix` | the mode's id prefix, PLAN §D's two letters + `i` (section 0): rdi, lci, obi, ami, rbi, bti, fhi, vbi, bfi |
| `fn` | the JS compute function's name, `<prefix>Compute` (e.g. `rdiCompute`) |
| `title` | the lab title shown on the page |
| `js` | the mode's base JS block (defines `<prefix>Compute(view, inst, opts)`) |
| `views` | ordered dict view -> view spec; the first is the default view |

view spec keys:

| key | meaning |
|---|---|
| `fields` | `[(key, field_spec, default)]` in display order, field specs from `eakit_core` (`ea.field(...)`, `ea.rec(...)`, `ea.choice(...)`, a `list` dict). `default` None means required |
| `tiles` | `[(label, tile_id)]`; every tile id starts with the prefix |
| `check` | `check(parsed_inputs, fixed)` raising `ValueError(sentence)` on whatever the JS refuses beyond the field parser; or None |
| `subtitle` | short subtitle |
| `rules` | the "How the lab counts." sentence(s), always printed |
| `js` | the view's JS block |
| `options` | optional `options(cfg, kit, tiles) -> (fixed, extra_cfg_keys, tiles)` for lesson-level cfg keys; default `({}, [], tiles)` |
| `family` | optional, default 1 (eakit_core's FAMILY sentence 1) |

`mode_lab` ships, in this order: RATIONAL_JS, EA_CORE_JS, **ITA_CORE_JS**,
your `js`, your view's `js`, then the eakit wiring. It sets the panel intro to
`family_intro()` (the Subject's sentence: "A count over the situation the
lesson states. The lab runs the algorithm on the instance and counts; a count
on one instance is evidence about that instance, and only the book's proof
bounds every input.") unless the lesson's cfg sets `panel_intro`.

## 3. JS conventions (both families)

- One pure function `<prefix>Compute(view, inst, opts)` per mode returning
  `{tiles: {id: text}, status: text, table: {caption, head, rows} | null}` or
  `{refuse: sentence}`. Use eakit's pattern:
  `var RDI_VIEW = {}; function rdiCompute(view, inst, opts) { return eaRun(RDI_VIEW[view], inst, opts); }`
  and `eaRefuse(sentence)` inside a view.
- `scripts/mathcheck.js` extracts every block with the regex
  `NAME = r"""..."""`, so declare each block exactly that way
  (`RDI_VIEW_JS["cut"] = r"""`), no other string prefix.
- Every JS function, variable and element id begins with the mode's prefix
  (`rdi`, `RDI_`), except the shared helpers below which begin with `ita` /
  `ITA_`. Family B must not define names beginning `ita`/`ITA_`.
- Numbers: exact BigInt rationals (RATIONAL_JS: `R`, `Radd`, `Rmul`, …) and
  eakit_core's printers (`eaInt`, `eaNum`, `eaPct`, `eaTimes`, …).

**ITA_CORE_JS** (in `itakit.py`, shipped on every itakit page) provides:

| function | does |
|---|---|
| `itaQ(r)` | a rational as a bare exact fraction: `3`, `−1/2`, `1,024/3` (no decimals; for matrices and lists) |
| `itaList(a)` | a JS array of BigInt or numbers as `5, 2, 4, 7` |
| `itaLg(n)` | lg n for a BigInt n ≥ 1: `{exact: R}` when n is a power of 2, else `{lo: R, hi: R}` bracketing it within 2^−64 |
| `itaLgCmp(n, x)` | sign of lg n − x for BigInt n ≥ 1 and rational x, exact (interval refinement; lg n of a non-power of 2 is irrational) |
| `itaApprox(r, places)` | `≈ 1,162.67`: a rational rounded to `places` decimals, with `≈` (use for a figure built from an approximation) |

## 4. Field formats both families use

From eakit_core, unchanged: records `a, 1; b, 2` (`ea.rec`), lists separated
by spaces or commas (`{"kind": "list", ...}`), whole numbers (`ea.whole`),
decimals with at most 6 places (`ea.num`; **fractions like 1/3 are not
accepted by eakit_core's parser**: write 0.25, or scale to whole numbers),
words (`ea.choice`). A record list or long list may set `"control": "area"`
to get a textarea.

## 5. The report and mathcheck

- `docs/intro-algorithms/kit-report.md`: family A owns the top and the
  "Conventions (both families)" section; family B appends its section
  `## Family B (itakit_b.py)` at the end, same per-mode shape as family A's.
- `scripts/mathcheck.js`: family A's block is
  `// ---- itakit (Introduction to Algorithms), family A ----` …
  `// ---- end itakit family A ----`, placed before THE VERDICT. Family B adds
  `// ---- itakit (Introduction to Algorithms), family B ----` … `// ---- end itakit family B ----`
  immediately after family A's end marker. Re-read the file immediately before
  each edit; both of us are editing it.
