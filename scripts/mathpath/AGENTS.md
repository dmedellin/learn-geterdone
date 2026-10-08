# scripts/mathpath — the shared renderer, and the arithmetic

Root `AGENTS.md` applies. This adds what is specific to this directory.

**There is no local change here.** One edit to `chrome.py`, `theme.py`,
`render.py`, `progress.py` or `feedback.py` lands on all 762 lessons, and it
reaches the hand-written trading pages too, because
`scripts/add_progress_marks.py` takes its CSS and scripts from `progress.py` and
`feedback.py`. Check both families before calling anything done.

Model: this is the **frontier tier** (`gpt-5.6-sol`, or `codex -p deep`). Small
diffs here are not small changes.

## Chrome mistakes that have shipped, all passing every check at the time

- A container query cannot style its own container. Put `container-type` on the
  child, never on the element you want to size.
- `[hidden]` is `display: none` at USER-AGENT precedence, so any author class
  that sets `display` silently defeats it — `.btn` sets `inline-flex`.
- `topbar()` escapes a mark that is not already markup, so a bare `&#10003;`
  reaches the reader as the literal text `&#10003;`.
- A `<style>` inside `<noscript>` applies only when scripting is OFF.
- `justify-content: space-between` spreads CHILDREN, so a new control must join
  an existing grouped child or it is stranded in open space.

Chrome is the one area the tests cannot answer. Render it and look:
`python3 -m http.server --directory site` then `google-chrome --headless
--screenshot`. Both themes; both light paths are real.

## labs/ — the arithmetic

`node scripts/mathcheck.js` is the check that matters. It executes the shipped
JavaScript extracted from these modules, so it tests what readers run rather
than a reimplementation. **Nothing else in the repository can tell you the
arithmetic is wrong**: a lab reporting the wrong roots renders correctly, passes
HTML validation and passes `labcheck.js`.

When you add arithmetic, add a case to `mathcheck.js`, then break the code on
purpose and confirm the case fails. A test that has never failed has not been
shown to test anything.

`algebra_systems.py` is 264 KB — about 66,000 tokens. Read the function you are
changing, never the module.

## labs/ — a preset's two claims

A preset carries a `label` (what the reader picks out of the `<select>`) and in
most kits a `note`. Both are prose about an outcome and **no check here can read
either.** A sweep of fifteen kits found **57** of those strings false about the
lab they described; every check in the repository passed on all 57. Rendering
does not help: `dpkit.py` prints its selected preset's note into the status
banner and had 5–6 of 36 wrong, against `graphkit.py`'s 1–3 of 45 with no note
rendered at all — and `dpkit`'s `memo/canonical` note said "into nineteen" in
the same banner line where the page printed 50 and 18.

So a preset also carries `expect`: `{kpi element id: the exact text the page
prints}`, one to three tiles. `scripts/build_paths.py` writes it to
`scripts/generated-expectations.json`; `scripts/labcheck.js` selects the option
on the built page, dispatches the control's own `change` handler, reads
`getElementById(id).textContent` and compares. It is the page's output that is
checked, never the source that produced it.

**The rule, for anyone adding or editing a preset.**

1. **A `label` names the instance; an outcome goes in `expect`.** "three items,
   capacity 50" and "the trace FIFO gets worse on" are labels. "greedy gets a
   fiftieth of the optimum" is a figure, and a figure belongs in a tile where it
   is checked.
2. **A new preset ships with `expect` or its page fails** — every option of every
   declared preset `<select>` must pin at least one tile. That is a gate, not a
   convention. A *second* preset menu cannot be smuggled past it either:
   `labcheck.js` decides what a preset menu is by behaviour, not by name — a
   `<select>` whose change handler rewrites another control's value is one, and
   it must be declared. A menu that only redraws (the greedy rule, the cache
   policy) is not.
3. **Read the figures by running the kit**, never out of the code that computes
   them: `node scripts/labcheck.js --observe site/<course>/<lesson>/index.html`
   prints every option's tiles as the page prints them. A figure copied from the
   source only proves the source agrees with itself.
4. **Pin the tiles that say why the preset exists.** `knapsack/halfway` exists to
   show density greedy at a fiftieth of the optimum, so it pins `ksGreedy`,
   `ksOpt` and `ksRatio`. Pinning `ksFrac` there would pass and prove nothing.
5. **Exact strings, format included**: `"1/50 = 0.020"`, not `"1/50"`. A tile that
   is reformatted must break this check loudly, because every sentence in the
   repository quoting the old format has just become wrong.
6. **A claim only visible with another control moved cannot be pinned.** Tiles are
   read with every other control at the value the markup ships — the
   earliest-finish rule, the density rule, LRU. `intervals/shortestfails` is a
   counterexample to *shortest-first*, and under the shipped rule the page prints
   the optimum; it pins `ivN` and `ivOpt` and says so in a comment rather than
   pinning something weaker and calling the claim checked.
7. **`KITS_WITH_EXPECTATIONS` in `scripts/build_paths.py` is the last step of a
   conversion, not the first.** Add the kit's key after its presets carry
   expectations; adding it before is what makes its pages fail.

`greedy.py` is the converted kit — 28 presets, all seven modes — and it is the
worked example to copy.

## After any change here

    python3 scripts/build_paths.py             # pages AND the two manifests
    python3 scripts/add_progress_marks.py     # idempotent; second run rewrites nothing
    node scripts/mathcheck.js && node scripts/labcheck.js --generated
    node scripts/progresscheck.js && node scripts/feedbackcheck.js
    python3 -m unittest discover -s tests
