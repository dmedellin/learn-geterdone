# acckit (Accelerate, Read Along): kit report

Lesson authors configure a lab from this report alone. It records the kit as
built to `docs/accelerate/PLAN.md` §0 and §D. Family A (delivery, flow,
branches, release, change, work) is `acckit.py` and is reported here first;
family B's section (likert, stats, validity, groups, sample, capability)
follows at the end under its own heading. The seam between the two modules is
`docs/accelerate/kit-contract.md`. Every example tile string in family A's
section was read off a rendered scratch page with
`node scripts/labcheck.js --observe`; none was copied from the code.

**Change, 2026-11-01 (tile wording, after review).** Tile ids unchanged;
these strings changed, and every pinned `expect` in `content/accelerate/` was
re-pinned: ratios always print two places (`2×` → `2.00×`, `22/7 ≈ 3.1×` →
`≈ 3.14×`, `1/2 ≈ 0.5×` → `0.50×`), the odds ratio likewise (`3` → `3.00`);
a figure of exactly 1 takes a singular unit (`1 hours` → `1 hour`, `1 items a
day` → `1 item a day`, `+1 points` → `+1 point`); arlCoord and arlAfterCoord
count groups in words (`1: shop + money for {…}` → `1 group spans more than
one team: shop + money for {…}`; `0: none` → `none: every release group
belongs to one team`; no teams: `no teams given`); groups/likely's table
share column prints the share whole (`3/10 = 30%`, was `= 30%`); stats'
compare tile reads `no sign to compare, since one r is 0` (was `one of them
0`).

**Field names that differ from, or add to, PLAN §D (family A).** Read these
before drafting a lab cfg:

- delivery/metrics: §D's "optional `period2` second set" is two fields,
  **`changes2`** and **`incidents2`** (same record shapes as `changes` and
  `incidents`, empty by default), over the same `days`.
- delivery/cluster: "cfg says which end is better" is the field **`better`**,
  `1` (default: code 1 is the book's first option) or `6`.
- flow/utilization and flow/batch take a **`unit`** (a word, default `hours`
  / `days`); utilization's single service time is **`service`**.
- flow/wip: the board log is **`items`** with **`days`** (the window);
  `throughput` is `-` when a log is given.
- branches/trunk: the thresholds are **`max_active`** (default `2`: at
  most two, the book's "fewer than three active branches"), **`life_hours`**
  (default `24`: lifetimes of **less than** a day; a lifetime of exactly the
  limit fails) and **`freeze_max`** (default `0`). There is no `max_life`.
  **Branch times must be `day.hh:mm`** (`3.14:30`), not day numbers: a bare
  number is refused with the reason, because a day number cannot tell a
  branch that lived an hour from one that lived a day and a half, so "less
  than a day" could not be tested. (§D said "day numbers"; this is the
  deviation.)
- release/independent: `components` is a list of names
  (`web cart pay ledger`); teams, when given, are a separate field
  **`teams`**, records `component, team` (every component needs one, or
  none does); `remove` is one record `a, b`.
- work/split: an entry may carry a third cell, its **stage**
  (`security, 36, test`), summed in the tile awkStages.
- change/approval: the two named routes are **`compare`** (`cab peer`; empty
  compares the first two routes met).
- work/split: **`kinds`** (the kinds, in order), **`new`** (which kind is new
  work), **`entries`**, **`scale`** (one record `kind, factor`) and
  **`move`** (`yes`: freed hours go to new work; `no`: the total falls).

**Drafted family A labs that do not build yet (checked 2026-11-01).** Every
other family A lab in `content/accelerate/` built:

- `the-impact-of-continuous-delivery` (work/split): an entry of kind `other`;
  set `"kinds": "new unplanned rework other"`.
- `trunk-based-development` (branches/trunk): `max_life` is not a field
  (use `life_hours`, default 24, or leave it out), and the branch records
  use day numbers, which the view refuses; write them as `day.hh:mm`
  (`b1, 1.09:00, 1.15:00`). `max_active: "2"` is right as it stands.

## Files

- `scripts/mathpath/labs/acckit.py`: the entry point `acckit_lab(cfg)`,
  `mode_lab(cfg, mode, spec)` (shared with family B), `AKT_CORE_JS` (shipped on
  every acckit page: `aktStatus`, `aktRead`, `aktIsqrt`, `aktSqrtFixed`,
  `aktRootSigned`, `aktSqrtExact`, `aktParseDec`, `aktParseRat`, `aktTime`,
  `aktTimeText`, `aktDur`, `aktMedian`, `aktMean`, `aktPp`, `aktDec`,
  `aktListed`), acckit's field kinds (`rat`, `TIME`, `arec`, `alist`) and
  their Python mirror (with `sqrt_fixed`, `root_signed`, `parse_rat`, …), a
  thin copy of `eakit_core.build_lab` that reads them, and family A's six
  modes: a base block (`ADE_JS`, `AFL_JS`, `ATB_JS`, `ARL_JS`, `ACM_JS`,
  `AWK_JS`) and one block per view, with the Python `check` of every view.
  It imports `acckit_b` lazily inside `acckit_lab`.
- `scripts/mathpath/labs/eakit_core.py`: used unchanged (imported as `ea`).
- `scripts/mathpath/labs/__init__.py`: one import (`acckit,`) and one
  registry line (`"acckit": acckit.acckit_lab,`).
- `scripts/build_paths.py`: `"acckit"` added to `KITS_WITH_EXPECTATIONS`, so
  every acckit preset menu must pin at least one tile on every option.
- `scripts/mathcheck.js`: the block `// ---- acckit (Accelerate), family A
  ----` … `// ---- end acckit family A ----`, after the dddkit blocks and
  before THE VERDICT: 64 assertions, one vm context per mode, plus the shared
  helpers.

## Conventions (both families)

**Entry point and cfg.** A lesson's lab is `("acckit", cfg)`, with
`cfg["mode"]` (delivery, flow, branches, release, change, work, or one of
family B's) and `cfg["view"]` (default: the mode's first view, listed first
below). An unknown mode or view raises, listing the valid ones. Keys common
to every view: `mode`, `view`, `presets` (required, non-empty), `preset` (the
one shown first; default the first), `title`, `panel_title`, `panel_intro`.
A cfg key named like one of the view's inputs supplies it to every preset
that does not set it (a cluster lesson states its `teams` once and varies
`k` per preset). Any other key raises, naming the keys the view takes.

**Panel intro.** Every acckit panel intro begins "A figure computed from the
small sample the lesson states." and by default continues "It shows what one
measure says about that sample; the book's findings are its survey's, and a
correlation is not a cause." (PLAN §D). A `panel_intro` in the cfg replaces
all but the first sentence, which is put back in front if missing.

**The caution.** Every status line, in every view of both families, ends
"; the figure is of the sample stated." (`aktStatus`). Under the tiles each
view prints "How the lab counts." with its rules sentence: what is computed,
the formula in words, and how ties, boundaries and orders go. The rules are
quoted or summarised per view below. No view grades a team: a tile says
what a measure is on the sample, and a threshold tile says whether the
sample meets the threshold the lesson states.

**Presets.** Each preset is `{"id": "lower-case-hyphens", "label": "plain
text", <inputs>..., "expect": {tile_id: "exact text"}}`. A label names the
instance; every outcome goes in `expect`. Every preset must pin at least one
tile (acckit is in `KITS_WITH_EXPECTATIONS`). Read the strings off the built
page with `node scripts/labcheck.js --observe <page>` (or
`scripts/preview_subject.py accelerate --course <slug>`), never out of the
code. A preset the page would refuse fails the build, naming the preset and
the reason. **Samples are the lesson's own, never the book's** (PLAN §C): no
row of Tables 2.2/2.3 or B.1, no figure's bars, no ING teams. The book's
answer options and thresholds are facts the kit uses; cite them in prose.

**Ids.** Family A: `ade` delivery, `afl` flow, `atb` branches, `arl`
release, `acm` change, `awk` work. Family B: `alk`, `ast`, `avd`, `agr`,
`asn`, `acp`. Shared helpers `akt`/`AKT_`. No prefix changed from PLAN §D.
An input's id is `<prefix>In<Key>`, the key's first letter capitalised
(`adeInChanges`, `atbInLife_hours`, `awkInNew`). Each page has
`<prefix>Preset` (the worked-example menu, which `expect` pins),
`<prefix>Status` and `<prefix>Table`.

**Input formats.** eakit_core's parser for names (letters, digits, `.`,
`_`, `-`), whole numbers (`12`), decimals (`3`, `0.25`, at most 6 places),
words (`yes`, `no`), and records (fields by commas, records by semicolons:
`c1, 1.09:00, 1.15:00, no; c2, …`; in a preset a string or a Python list of
lists). acckit adds:

- **a rational** (`rat`): a decimal or a fraction of whole numbers, `1/2`,
  `0.25`, `7/3` (at most 8 digits above and below the line; `1/0` is
  refused). Where a field says so, `-` means none.
- **a time** (`TIME`): `day.hh:mm` from the period's start, day 1 being the
  first day (`1.09:30` is day 1 at 09:30, which is 9.5 hours in; `2.00:00`
  is 24 hours in), or decimal hours from the start (`33.5`). `9:00` and
  `0.09:00` are refused with the reason. Times print back as `day.hh:mm`.
  branches/trunk takes only the `day.hh:mm` form (`CLOCK`).
- **lists** of any of these, separated by spaces or commas (`50 80 90`,
  `12 6`, `cab peer`).
- A wrong value paints one red sentence in the banner and blanks every tile
  and the table: "Changes (change, committed, deployed or -, failed yes or
  no), record 1: committed "9:00" should be a time: day.hh:mm (1.09:30 is
  day 1 at 09:30) or hours from the start (37.5)."

**Number and duration format.**
- Counts grouped `1,024`; a list tile is `n: a, b` or `0: none`.
- A rational is `eaNum`: `2/7 ≈ 0.29`, `1/2 = 0.50`, `4`; a share is
  `eaPct`: `1/5 = 20%`, `1/3 ≈ 33.3%`; a difference of shares `aktPp`:
  `≈ +8.3 points`, `+1 point`.
- **Ratios, both families (`aktTimes`):** always exactly two decimal
  places, `≈` in front only when two places are not exact: `2.00×`,
  `1.50×`, `50.00×`, `≈ 3.14×`, `0.50×`. No fraction is printed before a
  ratio. The odds ratio (groups/likely) follows the same rule without the
  `×`: `3.00`, `≈ 2.43`.
- **A figure with a unit (`aktUnit`)** takes the singular when the figure is
  exactly 1: `1 hour`, `1 day`, `1 item a day`, `3/2 = 1.50 days`. A lesson's
  own `unit` word is singularised by dropping a final `s` (`days` → `day`),
  so give units as plain plurals.
- A duration in hours prints `1 d 2 h 30 min`, `45 min`, `0 min`, with `30 s`
  when a median falls on a half minute.
- A square root (family B: r, standard deviation, √AVE) is printed to the
  stated places from the exact rational under the root by an integer square
  root, half up; a threshold on a root is tested on the squares.

**Exactness.** Every figure is a count, a list, or an exact BigInt rational,
including Ward's fusion coefficients. Nothing is approximated before it is
printed, and nothing typed is evaluated as script.

**Refusals.** Beyond the field rules, each view's Python `check` mirrors
every refusal its JS makes, with the same sentence, so a preset the page
would refuse fails the build. A parity run of 50 targeted inputs over
family A (both sides of every limit and every refusal) gave the same verdict
on both sides and the same sentence for every refusal a `check` makes.

**Page weight.** A page ships RATIONAL_JS, EA_CORE_JS, AKT_CORE_JS, the
wiring, its mode's base block and its own view's block, nothing more.

## Family A (acckit.py): modes, views, fields, tiles

Each field is listed as `key` (kind, default) with its label; — means
required. Tiles are listed as id, label, then the value observed on the
sample preset named.

### delivery (`ade`)

- **metrics.** The four measures from a log of changes and incidents.
  Fields:
  - `days` (whole 1–366, `14`), "Days in the period";
  - `changes` (records `change, committed, deployed or -, failed yes/no`;
    0–60, —), names unique;
  - `incidents` (records `incident, start, restored`; 0–60, empty);
  - `changes2`, `incidents2` (the same shapes; empty: one period).

  Tiles on preset `two-weeks` (changes `c1, 1.09:00, 1.15:00, no; c2,
  1.10:00, 1.15:00, no; c3, 2.09:00, 3.11:00, yes; c4, 4.09:00, 4.09:40, no;
  c5, 5.10:00, -, no; c6, 6.09:00, 8.09:00, no`, incidents `i1, 3.11:30,
  3.14:00; i2, 9.08:00, 9.08:45`, days 14):
  - adeDeploys, Deployments, `4` (c1 and c2 deploy together);
  - adeChanges, Changes deployed, `5 of 6`;
  - adePerDay, Deployments per day, `2/7 ≈ 0.29`;
  - adePerWeek, Deployments per week, `2`;
  - adeFreq, Deployment frequency, as the book's answer option, `between once per day and once per week`;
  - adeLead, Median lead time (commit to deploy), `6 h`;
  - adeLeadOpt, Lead time, as the book's answer option, `less than one day`;
  - adeFail, Change fail rate (failed / deployed), `1/5 = 20%`;
  - adeFailBand, Change fail rate band, `16–30%`;
  - adeRestore, Median time to restore service, `1 h 37 min 30 s`;
  - adeRestoreOpt, Time to restore, as the book's answer option, `less than one day`.

  Status: "Over 14 days: 4 deployments (2/7 ≈ 0.29 a day), median lead time
  6 h, change fail rate 1/5 = 20%, median time to restore 1 h 37 min 30 s;
  the figure is of the sample stated." Table: each change (committed,
  deployed, lead time, failed) and each incident (start, restored, time to
  restore); with two periods, a period column.

  With `changes2`/`incidents2`, every tile reads `period 1 → period 2`:
  preset `two-periods` (days 7, changes `a, 1.09:00, 1.10:00, no`, changes2
  `a, 1.09:00, 1.09:30, no; b, 2.09:00, 2.09:20, yes`) gives adeDeploys
  `1 → 2`, adeLead `1 h → 25 min`, adeLeadOpt `less than one day → less than
  one hour`, adeFail `0 = 0% → 1/2 = 50%`.

  **How a value is placed on the book's options (and boundaries).** Lead
  time and time to restore: less than one hour (< 1 h), less than one day
  (< 24 h), between one day and one week (< 7 d), between one week and one
  month (< 30 d), between one month and six months (< 180 d), more than six
  months; **a value exactly on a boundary goes to the longer option** (one
  hour exactly is "less than one day"), because the book's words are "less
  than". Deployment frequency, by deployments per day over the period: the
  book's first two options overlap ("multiple deploys per day" is also
  "between once per hour and once per day"), so the lab states its rule:
  **two or more a day** is on demand (multiple deploys per day); **at least
  one but fewer than two** a day is between once per hour and once per day;
  at least one a week, between once per day and once per week; at least one
  in 30 days, between once per week and once per month; at least one in 180
  days, between once per month and once every six months; fewer, fewer than
  once every six months; **a rate exactly on a boundary goes to the more
  frequent option** (one a day exactly is "between once per hour and once
  per day"). No deployment prints "none: no deployment in the period".
  Change fail rate bands: 0–15%, 16–30%, 31–45%, 46–60% (the book's), then
  the lab's own 61–75%, 76–100%; a rate goes in the first band whose top it
  does not pass (15% is 0–15%; 3/19 ≈ 15.8% is 16–30%).

  Other rules: changes deployed at the same moment are one deployment; lead
  time is deployed − committed; time to restore is restored − start; a median
  of an even count is the mean of the two middle values; change fail rate is
  failed changes over changes deployed (an undeployed change is in neither).
  No change deployed prints "no change deployed"; no incident prints "no
  incident in the period" (no figure is invented).

  Refuses: a time after the period's end ("Changes, record 1 (c1): deployed
  3.00:30 is after the end of the 2-day period"); deployed before committed;
  restored before start; an undeployed change marked failed ("Changes,
  record 1 (c1): failed is yes, but the change was never deployed (deployed
  -)"). Period 2's records are named "Changes, period 2" and "Incidents,
  period 2".

- **cluster.** Ward's hierarchical clustering of coded answers. Fields:
  - `teams` (records `team, deploy, lead, restore, fail`, each code a whole
    1–6; 3–30, —), names unique;
  - `k` (whole 2–5, `3`), "Groups to stop at";
  - `better` (choice `1` or `6`, `1`): which code is the book's first option
    (on demand, less than one hour, 0–15%). It only decodes the medians; the
    clustering ignores it.

  Tiles on preset `three` (teams `a, 1, 1, 1, 1; b, 1, 2, 1, 1; c, 2, 1, 2,
  1; d, 4, 4, 3, 2; e, 4, 5, 4, 3; f, 5, 4, 4, 2; g, 6, 6, 5, 4; h, 6, 6, 6,
  4`, k 3):
  - adeTeams, Teams, `8`;
  - adeGroups, The k groups, `G1: a, b, c; G2: d, e, f; G3: g, h`;
  - adeMedDeploy, Median deployment frequency per group, `G1: 1, on demand (multiple deploys per day); G2: 4, between once per week and once per month; G3: 6, fewer than once every six months`;
  - adeMedLead, Median lead time per group, `G1: 1, less than one hour; G2: 4, between one week and one month; G3: 6, more than six months`;
  - adeMedRestore, Median time to restore per group, `G1: 1, less than one hour; G2: 4, between one week and one month; G3: 5.5, between one month and six months / more than six months`;
  - adeMedFail, Median change fail rate per group, `G1: 1, 0–15%; G2: 2, 16–30%; G3: 4, 46–60%`;
  - adeWithin, Total within-group sum of squares at k, `31/6 ≈ 5.17`;
  - adeLastCoef, Fusion coefficient of the last merge made, `5/3 ≈ 1.67 ({d, f} + {e})`;
  - adeNextCoef, Fusion coefficient of the next merge (to k − 1), `421/30 ≈ 14.03 ({d, e, f} + {g, h})`.

  Table: every merge down to one group (merge, groups joined, fusion
  coefficient, groups left with `(k)` marking k, running total within-group
  sum of squares). On these teams the coefficients are 1/2, 1/2, 1, 3/2,
  5/3, 421/30, 1,511/20: the jump from 5/3 to 421/30 is the gap a
  classification lesson points at. With k 2 the same teams give
  `G1: a, b, c; G2: d, e, f, g, h`.

  Rules: squared Euclidean distance on the four codes; at each step merge
  the two groups whose merge adds least to the total within-group sum of
  squares; that increase, nA·nB/(nA + nB) × the squared distance between
  the group means, is the fusion coefficient, an exact fraction. **Tie-break:**
  groups are kept in the order of their earliest team in the input; a tie
  between merges goes to the pair whose first group comes earliest, then
  whose second does (above, {a}+{b} and {g}+{h} both cost 1/2; {a}+{b} goes
  first). Groups are named G1, G2, … in that order. A group's median is the
  middle code or the mean of the two middle codes; a half code prints both
  neighbouring options. Refuses k not fewer than the teams ("k is 3, and
  there are 3 teams; k must be fewer than the teams").

### flow (`afl`)

- **utilization.** Lead time as utilization nears 100 percent. Fields:
  `levels` (list of 1–12 decimals 0–100, —), "Utilization levels, percent
  (below 100)"; `service` (rational > 0, `1`); `unit` (name, `hours`).

  Tiles on preset `rising` (levels `50 80 90 95 99`): aflLevels, Levels,
  `5: 50%, 80%, 90%, 95%, 99%`; aflMultiples, Queueing multiple u/(1 − u) at
  each level, `50%: 1; 80%: 4; 90%: 9; 95%: 19; 99%: 99`; aflLeads, Lead time
  at each level, `50%: 2 hours; 80%: 5 hours; 90%: 10 hours; 95%: 20 hours;
  99%: 100 hours`; aflHigh, Lead time at the highest level, `99%: 100.00× the
  service time`; aflRatio, Highest level's lead time over the lowest's,
  `50.00× (50% to 99%)`. Preset `half-day` (levels `60 25`, service `1/2`, unit
  `days`): aflLeads `60%: 5/4 = 1.25 days; 25%: 2/3 ≈ 0.67 days`.

  Rules: the single-server queue with random arrivals and service (M/M/1),
  named in the rules sentence as a simplification; wait u/(1 − u) service
  times, lead time service/(1 − u). Levels in the order given. Refuses 100:
  "Utilization levels, entry 2 is 100%: there u/(1 − u) divides by zero,
  because work arrives as fast as it can be done, so in this model the queue
  and the wait grow without bound and no lead time exists". A System Design
  or Operations Research lesson teaches the queue; name it by title.

- **batch.** What a smaller batch does to the wait for feedback. Fields:
  `work` (whole 1–1000, —); `batch` (list of 1–2 wholes, —; two compare);
  `per_item` (rational > 0, `1`); `release_cost` (rational ≥ 0, `0`); `unit`
  (name, `days`).

  Tiles on preset `slices` (work 20, batch `20 5`, per_item 1,
  release_cost 2): aflBatches, Batches, `1 of 20 → 4 of 5`; aflFirst, Time
  to first feedback (first batch released), `22 days → 7 days`; aflLast,
  Time to last release, `22 days → 28 days`; aflWait, Average wait per item
  (start to release), `22 days → 35/2 = 17.50 days`; aflOverhead, Total
  release overhead, `2 days → 8 days`; aflRatio, First feedback, first size
  over second, `≈ 3.14×`. A short last batch: work 10, batch 4,
  per_item `1/2`, release_cost 1 gives aflBatches `3: 2 of 4, the last of 2`.

  Rules: one worker, items one after another; batch i is released at (items
  done through batch i) × per_item + i × release_cost; the next batch starts
  after the release. Refuses a batch larger than the work. The table lists
  each batch's release (the first 40).

- **wip.** Little's law. Fields: `throughput` (rational > 0 or `-`, `-`),
  items a day; `wip` (list of 0–2 rationals > 0, empty); `days` (whole
  1–366, `10`), the log's window; `items` (records `item, start, done or -`,
  decimal days from the window's start, 0–366; 0–60, empty).

  Give either a throughput with one or two WIP values, or a board log (and
  optionally WIP values to apply its throughput to). Preset `limit`
  (throughput `3/2`, wip `12 6`): aflThru, Throughput, `3/2 = 1.50 items a
  day`; aflAvgWip, Average work in process (from the log), `no board log`;
  aflAvgLead, Average lead time of items done (from the log), `no board
  log`; aflLittle, Little's law on the log, `no board log`; aflLeadAt, Lead
  time at each work in process, `WIP 12: 8 days; WIP 6: 4 days`; aflChange,
  Second lead time over the first, `0.50× the lead time (8 → 4 days)`.
  Preset `board` (items `w1, 0, 3; w2, 0, 4; w3, 1, 6; w4, 2, 9; w5, 5, -;
  w6, 7, 10`, wip 4): aflThru `1/2 = 0.50 items a day`, aflAvgWip
  `27/10 = 2.70 items`, aflAvgLead `22/5 = 4.40 days`, aflLittle `differs:
  average WIP 27/10 = 2.70, throughput × average lead time 11/5 = 2.20,
  because 1 item is still open at the end (w5)`, aflLeadAt `WIP 4: 8 days`.
  With no item open the tile reads `holds: average WIP 3/2 = 1.50 =
  throughput × average lead time`.

  Refuses: neither a throughput nor a log; no WIP and no log; both a
  throughput and a log; a start or done after the window; done before
  start; WIP values with a log in which nothing is done (throughput 0).

### branches (`atb`)

- **trunk.** Active branches, lifetimes and freezes against the thresholds.
  Fields: `days` (whole 1–92, `30`); `branches` (records `branch, created,
  merged or -`, each a `day.hh:mm` time; 1–60, —); `freezes` (list of day
  numbers, empty); `max_active` (whole 0–60, `2`); `life_hours` (rational
  > 0, `24`); `freeze_max` (whole, `0`). Example record:
  `f1, 1.09:00, 1.16:00; f6, 5.14:00, -`.

  Tiles on preset `week` (days 7, branches `f1, 1.09:00, 1.16:00; f2,
  1.10:00, 2.11:00; f3, 2.09:00, 2.12:00; f4, 2.10:00, 2.11:00; f5, 3.09:00,
  7.17:00; f6, 5.14:00, -; f7, 7.09:00, -`, freezes `6`):
  - atbBranches, Branches, `7`;
  - atbMaxActive, Most branches open at once, `3, first at 2.10:00`;
  - atbMeanLife, Mean lifetime of merged branches, `1 d 4 h`;
  - atbOver, Branches living the limit or longer, `3: f2 (1 d 1 h); f5 (4 d 8 h); f6 (open, at least 2 d 10 h)`;
  - atbOpen, Open at the end, `2: f6, f7`;
  - atbFreeze, Freeze days, `1: day 6`;
  - atbMetActive, Active branches threshold met, `no: 3 at once, and the threshold is at most 2 (fewer than three)`;
  - atbMetLife, Lifetime threshold met, `no: 3 branches lived 1 d or longer`;
  - atbMetFreeze, Freeze threshold met, `no: 1 freeze day, and the threshold is at most 0`.

  Table: each day, the branches that exist at some moment of it, and freeze
  days. Rules: a branch is open on [created, merged); a merge at the same
  moment as a creation ends first; the most open at once is over every
  moment. A lifetime (or an open branch's age at the period's end) equal to
  the limit fails "less than"; an open branch younger than the limit is
  **not yet determined** (`not yet determined: 1 branch is open and younger
  than 1 d`), never counted as a pass. Exactly `max_active` open at once
  meets it (`yes: at most 1 at once, and the threshold is at most 1`).
  Refuses: a bare day number ("Branches (…), record 1: created "1" should
  be a time day.hh:mm, such as 3.14:30; this view takes no bare numbers,
  because a day number alone cannot tell a lifetime of an hour from one of
  a day and a half"), a time after the period, merged before created, a
  freeze day after the period or given twice.

### release (`arl`)

- **independent.** Release groups from "must release together" ties.
  Fields: `components` (list of 1–60 names, —); `teams` (records
  `component, team`; empty for none; every component or none); `ties`
  (records `a, b`; empty); `remove` (one record `a, b`, a tie to remove;
  empty).

  Tiles on preset `shop` (components `web cart pay ledger search mail`,
  teams `web, shop; cart, shop; pay, money; ledger, money; search, find;
  mail, ops`, ties `web, cart; cart, pay; pay, ledger`, remove `cart,
  pay`):
  - arlGroups, Release groups, `3: {web, cart, pay, ledger}, {search}, {mail}`;
  - arlLargest, Largest group, `4: web, cart, pay, ledger`;
  - arlAlone, Deployable alone, `2: search, mail`;
  - arlCoord, Teams that must coordinate a release, `1 group spans more than one team: shop + money for {web, cart, pay, ledger}` (the count is of groups; with two, `2 groups span more than one team: x + y for {a, b}; x + z for {c, d}`);
  - arlRemoved, The tie removed, `removing cart–pay splits a group: 3 → 4 release groups`;
  - arlAfterGroups, Release groups after, `4: {web, cart}, {pay, ledger}, {search}, {mail}`;
  - arlAfterAlone, Deployable alone after, `2: search, mail`;
  - arlAfterCoord, Teams that must coordinate after, `none: every release group belongs to one team`.

  Without teams arlCoord reads `no teams given`; without `remove` the
  after tiles read `no tie removed`. A tie inside a cycle changes nothing:
  `removing c–a changes no group: c and a are still tied through others`.
  Groups are connected components, listed by their first component in the
  input. Refuses: a tie to an unknown component, a tie to itself, a tie
  given twice (either order), a tie to remove that is not a tie, a team
  record for an unknown component, teams on some components only ("Give a
  team for every component or for none; b has none").

- **scaling.** Deploys per developer per day as organizations grow.
  Fields: `orgs` (records `org, developers, deploys`; 2–30, —); `days`
  (whole 1–366, `30`).

  Tiles on preset `three-orgs` (orgs `big, 400, 9600; small, 10, 150; mid,
  80, 2000`, days 30): arlOrgs, Organizations, `3`; arlRates, Deploys per
  developer per day, by size, `small (10 developers): 1/2 = 0.500; mid (80
  developers): 5/6 ≈ 0.833; big (400 developers): 4/5 = 0.800`; arlSmall,
  Smallest, `small (10 developers): 1/2 = 0.500`; arlBig, Largest, `big (400
  developers): 4/5 = 0.800`; arlTrend, As size grows, `from small to big,
  the rate rises and falls: no single direction`. Other trend words: `rises
  at every step`, `falls at every step`, `holds: the same at every size`,
  `rises or holds, never falls`, `falls or holds, never rises`. Rates print
  to three places. Refuses two organizations with the same number of
  developers.

### change (`acm`)

- **approval.** What each approval route adds to lead time, and its fail
  rate. Fields: `changes` (records `change, route, wait, failed`, wait in
  hours, a rational ≥ 0; 1–60, —); `compare` (list of 0 or 2 route names,
  empty).

  Tiles on preset `routes` (changes `c1, none, 0, no; c2, peer, 2, no; c3,
  peer, 3.5, yes; c4, cab, 72, no; c5, cab, 120, yes; c6, peer, 1, no; c7,
  cab, 48, no; c8, none, 0.25, no; c9, peer, 4, no; c10, none, 0, yes`):
  acmChanges, Changes, `10`; acmRoutes, Changes by route, `3: none (3), peer
  (4), cab (3)`; acmMeanWait, Mean wait each route adds, `none 5 min; peer
  2 h 37 min 30 s; cab 3 d 8 h`; acmMedianWait, Median wait each route adds,
  `none 0 min; peer 2 h 45 min; cab 3 d`; acmFail, Change fail rate by
  route, `none 1/3 ≈ 33.3%; peer 1/4 = 25%; cab 1/3 ≈ 33.3%`; acmOverall,
  Change fail rate overall, `3/10 = 30%`; acmDiff, Difference in fail rate
  between two routes, `none 1/3 ≈ 33.3% against peer 1/4 = 25%: ≈ +8.3
  points`. With compare `cab peer`: `cab 1/3 ≈ 33.3% against peer 1/4 =
  25%: ≈ +8.3 points`. The status says a difference in a sample says nothing
  of what causes it. Refuses one route named, or a named route no change
  uses.

### work (`awk`)

- **split.** Hours by kind of work, and what a scaling frees. Fields:
  `kinds` (list of 2–10 names, `new unplanned rework`); `new` (a name, `new`);
  `entries` (records `kind, hours` or `kind, hours, stage`, hours a rational
  > 0; a kind may repeat and is summed; 1–60, —); `scale` (one record `kind, factor`, factor a
  rational 0–10 such as `1/2`; empty); `move` (choice `yes`/`no`, `yes`).

  Tiles on preset `month` (entries `new, 60; unplanned, 30; rework, 40; new,
  30`): awkTotal, Total, `160 hours`; awkHours, Hours by kind, `new 90;
  unplanned 30; rework 40`; awkShares, Share by kind, `new 9/16 ≈ 56.3%;
  unplanned 3/16 ≈ 18.8%; rework 1/4 = 25%`; awkNew, New work's share,
  `9/16 ≈ 56.3%`; awkFreed, Hours freed by the scaling, `no scaling given`;
  awkAfter, Shares after the scaling, `no scaling given`; awkNewAfter, New
  work's share after, `no scaling given`; awkStages, Hours by stage (entries
  that give one), `no stages given`. With scale `rework, 1/2`: awkFreed
  `20 hours (rework 40 → 20), to new`, awkNewAfter `11/16 ≈ 68.8%`; with move
  `no` as well: awkFreed `20 hours (rework 40 → 20), total 140`, awkNewAfter
  `9/14 ≈ 64.3%`. For the security lesson: kinds `new security`, entries
  `new, 800; security, 4, build; security, 36, test; security, 320,
  release` give awkStages `build 4; test 36; release 320`. "What finding
  them earlier would save" is two presets (late and early hours) compared in
  prose, or a scale of the security kind; the kit holds no cost model of
  its own.

  Refuses: `new` not among the kinds; an entry of an unknown kind; scaling
  an unknown kind; scaling the new-work kind while freed hours go to it; a
  factor above 1 that would take more hours than new work has.

### A sample preset (delivery/cluster)

```python
"lab": ("acckit", {
    "mode": "delivery", "view": "cluster",
    "teams": "a, 1, 1, 1, 1; b, 1, 2, 1, 1; c, 2, 1, 2, 1; d, 4, 4, 3, 2; "
             "e, 4, 5, 4, 3; f, 5, 4, 4, 2; g, 6, 6, 5, 4; h, 6, 6, 6, 4",
    "presets": [
        {"id": "three", "label": "Eight invented teams, three groups", "k": 3,
         "expect": {"adeGroups": "G1: a, b, c; G2: d, e, f; G3: g, h",
                    "adeNextCoef": "421/30 ≈ 14.03 ({d, e, f} + {g, h})"}},
        {"id": "two", "label": "The same teams, two groups", "k": 2,
         "expect": {"adeGroups": "G1: a, b, c; G2: d, e, f, g, h"}},
    ],
}),
```

prints, for `three`, the nine tiles listed under cluster above.

### Verification (family A)

- `node scripts/mathcheck.js`: family A's block passes (64 assertions:
  the shared helpers' roots, parsers and durations, and every view). Ward's
  fusion coefficients were checked against an independent Fraction
  computation of the within-group sums of squares before and after each
  merge. A mutation run broke 50 lines on purpose (the root's rounding, the
  option boundaries in both directions, the deployment de-duplication,
  Ward's denominator and tie-break, the batch release times, Little's law,
  the branch sweep order and limits, the union of ties, the scaling rate and
  order, the per-route fail rate, the scaling of work): every mutant made at
  least one assertion fail.
- One scratch lesson per view (ten pages, rendered with
  `scripts/preview_subject.py` from a scratch package outside the
  repository): `labcheck.js` executed and swept every page, 0 failing, and
  every pinned preset figure matched. At 375 px wide in Playwright no page
  scrolls sideways under any preset, and no page error was thrown.

## Family B (acckit_b.py)

Six modes: likert, stats, validity, groups, sample, capability. Every example
tile string below was read off a rendered scratch page with
`node scripts/labcheck.js --observe` (and every one was also worked by hand;
see "Family B: verification"). Every view prints its rules under the tiles
("How the lab counts."), and every status line ends "; the figure is of the
sample stated." (`aktStatus`). No view grades a team, a construct or a leader,
and none prints a p-value.

### Deviations from PLAN §D (family B)

- **likert/westrum: `cuts` is a required input with no kit default** (the book
  gives no cut-points). State it once at cfg level (`"cuts": "3.5 5.5"`) to
  supply every preset. The items box is score's (`item, construct, reverse`)
  and must name exactly one construct.
- **likert/alpha: `items` is a list of names** (`q1 q2 q3`), not records, and
  the view takes `points` (to check the answers' range). Answers are used as
  given: reverse a reverse-coded item before entering it. Threshold cfg key
  `alpha_min` (default `"0.7"`).
- **likert/score: `line` defaults to 4** (the middle of 7 points); set it for
  a 5-point scale. Respondents exactly on the line are counted "at" it.
- **stats/describe and groups/enps: "a list, or records `name, value`" is a
  cfg switch**, `"named": "yes"` (default `"no"`), because the box's shape is
  fixed at build time.
- **stats/pearson: strength cut-offs are the cfg key `strength`**, two
  decimal strings, default `["0.3", "0.7"]`: a convention the lab states, not
  the book's.
- **stats/spurious: `t` is a whole number, strictly increasing; n ≥ 4.**
- **stats/confound: the pooled within-group r uses every group**, those under
  3 rows included (their sums are added; only their own r is not printed).
- **validity/matrix: at most 11 items** (55 pairs within the 60-record box);
  means use the signed r.
- **validity/ave: threshold cfg keys `ave_min` (0.5, passed when AVE is
  above), `cr_min` (0.7, at least), `loading_min` (0.6, above), `r_max`
  (0.85, below).** "r < 0.85" is tested on |r| (as r² < 0.85²).
- **groups/likely: the groups compared are two required inputs, `first` and
  `second`** (state them once at cfg level).
- **groups/enps: "the answers that would raise it by moving one band" are the
  answers at 6 and at 8**, one point from the next band up; the tile counts
  them and gives the rise per answer moved (100 ÷ n points).
- **capability/profile: teams are "has" lists only** (`t1, vc, ta, la`: the
  team, then the capabilities in place), not yes/no columns; **the second date
  is the input `teams2`** (the same shape), not `team2`/`date2`. A capability
  belongs to at most one maturity level.
- **Names are one word.** Every name in every box (items, constructs,
  respondents, groups, capabilities, levels, people) is letters, digits, `.`,
  `_`, `-`: **no spaces**. Write the book's multiword capabilities with
  hyphens: `trunk-based-development`, `version-control`,
  `test-data-management`. (Spaces cannot be accepted without a new
  shared field kind in acckit.py; the comma already ends a cell.)

### Conventions (family B)

- **Ids.** Prefixes `alk` likert, `ast` stats, `avd` validity, `agr` groups,
  `asn` sample, `acp` capability. Inputs are `<prefix>In<Key>` (`alkInAnswers`,
  `astInPairs`, `avdInLoadings`, `agrInRows`, `asnInPeople`, `acpInTeams`);
  each page has `<prefix>Preset`, `<prefix>Status`, `<prefix>Table`.
- **Records** are `a, b; c, d`, at most 60 per box. Likert answers are
  `respondent, then one whole answer per item` in the items' order
  (`r1, 6, 5, 2, 7, 1`); a record with too few or too many answers is refused,
  naming the record. Lists are separated by spaces or commas.
- **Numbers.** Values, x, y, loadings, r and cut-points are decimals with at
  most 6 places (`0.62`, `-1.5`); counts and answers are whole numbers.
- **Printing.** An exact decimal prints as itself (`5.25`, `0.4325`);
  otherwise the exact fraction and 3 places (`14/3 ≈ 4.667`). Shares print
  `9 of 12 = 75%` / `1 of 3 ≈ 33.3%`; differences of shares `+40 points`,
  `≈ −33.3 points`. A square root (r, a standard deviation, √AVE) prints to 3
  places by the exact method (integer square root of the scaled rational,
  half up), with `≈` in front unless the root is exact (`1`, `0.6`, `−1`).
  Minus is U+2212.
- **Order and ties.** Constructs, items, groups, seeds, categories and
  capabilities go in the order first given. Modes (stats) go in increasing
  order. Every tie rule is in the view's rules sentence.
- **Optional boxes** (`answers2`, `between`, `levels`, `teams2`) may be empty;
  `drop` is `-` for none. Their tiles then say so (`no second survey given`,
  `no maturity model given`, `no seed dropped`).

### likert (`alk`)

Fields common to score and westrum: `points` (select `5`/`7`, default `7`;
`alkInPoints`), `items` (records `item, construct, reverse` with reverse
`yes`/`no`, item names unique, ≤ 40; `alkInItems`), `answers` (records
`respondent, a1 … ak`, respondents unique, each answer a whole 1–7 and at most
`points`; `alkInAnswers`).

- **score**. Extra field `line` (a decimal on the scale, default `4`;
  `alkInLine`). Example: items `c1, culture, no; c2, culture, no; c3, culture,
  yes; l1, learning, no; l2, learning, yes`, answers `r1, 6, 5, 2, 7, 1; r2, 4,
  4, 4, 5, 3; r3, 7, 6, 1, 6, 2; r4, 2, 3, 6, 3, 5`, line `4`:
  - `alkN` Respondents: `4`
  - `alkConstructs` Construct means, reverse-coded items reversed: `culture 14/3 ≈ 4.667; learning 5.25`
  - `alkItems` Item means, as scored: `c1 4.75; c2 4.5; c3 4.75; l1 5.25; l2 5.25`
  - `alkLine` Respondents above, at and below the line: `culture: 2 above, 1 at, 1 below; learning: 3 above, 0 at, 1 below`
  - `alkReversed` Reverse-coded items: `2: c3, l2`
  - `alkUnreversed` Construct means if nothing were reversed (the error): `culture 25/6 ≈ 4.167; learning 4`
  A reverse-coded answer scores points + 1 − answer. Table: each respondent's
  mean per construct. Refusals: answer count ≠ items
  (`Answers, record 1 (r1) gives 4 answers; there are 5 items (c1, c2, c3, l1, l2), so each record needs 5`),
  an answer above `points`, a line off the scale.
- **westrum**. Extra fields `cuts` (two decimals, low then high, the lesson's
  own, **required**; `alkInCuts`) and `answers2` (a second survey, same shape,
  default empty; `alkInAnswers2`). Bands: mean < first cut pathological; first
  cut ≤ mean < second bureaucratic; ≥ second generative. Example (cfg
  `"cuts": "3.5 5.5"`), items `w1, culture, no; w2, culture, no; w3, culture,
  no; w4, culture, yes`, answers `a, 6, 7, 6, 2; b, 5, 5, 4, 3; c, 2, 3, 3, 6;
  d, 6, 6, 7, 1`, answers2 `a, 7, 7, 6, 1; b, 6, 6, 5, 2; c, 4, 4, 3, 4; f, 5,
  5, 5, 3`:
  - `alkN` Respondents: `4`
  - `alkTeam` Team mean and band: `5, bureaucratic`
  - `alkBands` Respondents by band: `pathological 1, bureaucratic 1, generative 2`
  - `alkTeam2` Second survey: team mean and band: `5.3125, bureaucratic`
  - `alkBands2` Second survey: by band: `pathological 0, bureaucratic 2, generative 2`
  - `alkChange` Change in the team mean: `+0.3125 (bureaucratic to bureaucratic)`
  - `alkEach` Change per respondent in both surveys: `3: a +0.5, b +1, c +1.25`
  With no second survey the last four read `no second survey given`.
  Respondents only in one survey count in that survey's mean, not in
  `alkEach`. Refusals: items naming two constructs, not two cuts, a cut off
  the scale, cuts not low-then-high (`The cuts go low then high, and 4 is not below 4`).
- **alpha**. Fields `points`, `items` (2–20 names; `alkInItems`), `answers`
  (≥ 3 respondents, ≥ 2 answers each). cfg `alpha_min` (default `"0.7"`).
  Example: points `5`, items `q1 q2 q3`, answers `r1, 4, 5, 4; r2, 2, 3, 3;
  r3, 5, 5, 4; r4, 3, 2, 2; r5, 1, 2, 1`:
  - `alkK` Items k: `3`; `alkN` Respondents n: `5`
  - `alkVars` Item variances: `q1 2; q2 1.84; q3 1.36` (population, ÷ n)
  - `alkTotal` Variance of the total score: `14.16`
  - `alkAlpha` Cronbach's alpha: `56/59 ≈ 0.949`
  - `alkDeleted` Alpha with each item removed: `q1 0.961; q2 0.909; q3 0.909`
    (`not computed (one item would be left)` when k = 2)
  - `alkMeets` At or above the threshold: `yes: 0.949 ≥ 0.7`
    (`alpha_min: "0.95"` gives `no: 0.949 < 0.95`)
  Alpha may be negative (`−108` for two items that disagree). Refused when
  every respondent's total is the same (the total varies by nothing).

### stats (`ast`)

- **describe**. Field `values` (≥ 2 decimals; `astInValues`), or with cfg
  `"named": "yes"` records `name, value`. Example `3 7 7 2 9 4`:
  `astN` n `6`; `astMean` Mean `16/3 ≈ 5.333`; `astMedian` Median `5.5`;
  `astMode` Mode(s) `7 (2 times)` (`1, 2 (2 times each)`; `none: every value
  occurs once` when all occur equally often); `astMin` `2`; `astMax` `9`;
  `astRange` `7`; `astPopSd` Population standard deviation (÷ n)
  `≈ 2.494 (variance 56/9 ≈ 6.222)`; `astSampleSd` Sample standard deviation
  (÷ (n − 1)) `≈ 2.733 (variance 112/15 ≈ 7.467)`. Table: values in order,
  deviation and its square.
- **pearson**. Field `pairs` (records `name, x, y`, ≥ 3, names unique;
  `astInPairs`). cfg `strength` (default `["0.3", "0.7"]`). Example `a, 1, 2;
  b, 2, 4; c, 3, 5; d, 4, 4; e, 5, 5`: `astN` `5`; `astMeans` Means
  `x̄ = 3, ȳ = 4`; `astR` Pearson's r `≈ 0.775`; `astR2` r² (shared
  variation) `3/5 = 60%`; `astLine` Least-squares line `y = 2.2 + 0.6·x`;
  `astWords` Sign and strength `positive, strong` (`positive, moderate` with
  `strength: ["0.3", "0.8"]`; `none: r = 0` when r is 0). Refused when every x
  or every y is the same.
- **spurious**. Field `series` (records `t, x, y`, t whole and increasing,
  ≥ 4; `astInSeries`). Example `1, 10, 5; 2, 12, 7; 3, 15, 8; 4, 17, 10; 5,
  20, 11; 6, 22, 13`: `astN` Time points `6`; `astRLevels` r of the levels
  `≈ 0.989`; `astRDiffs` r of the first differences `−1`; `astCompare` The
  differences' r against the levels' `larger in size, the opposite sign`. A
  straight-line trend gives `not defined: every x is the same` for the
  differences and `cannot be compared: one r is not defined`.
- **confound**. Field `rows` (records `name, x, y, z`, z a group name, ≥ 3;
  `astInRows`). Example `a, 1, 5, small; b, 2, 4, small; c, 3, 3, small; d,
  6, 10, large; e, 7, 9, large; f, 8, 8, large`: `astN` `6`; `astGroups`
  Groups of z `2: small, large`; `astR` r over all rows `≈ 0.807`;
  `astWithin` r within each group `small −1 (n = 3); large −1 (n = 3)` (a group
  under 3 rows: `not computed: fewer than 3 rows (n = 2)`); `astPooled` Pooled
  within-group r `−1`; `astCompare` Pooled against overall `larger in size,
  the opposite sign`. Table: per group n, means, Sxx, Syy, Sxy, r.

### validity (`avd`)

- **matrix**. Fields `items` (records `item, construct`, 3–11, ≥ 2
  constructs; `avdInItems`), `corr` (records `item, item, r`, r from −1 to 1,
  **every pair of different items exactly once**, either order;
  `avdInCorr`). Example: items `s1, speed; s2, speed; s3, speed; k1, care; k2,
  care`, corr `s1, s2, 0.6; s1, s3, 0.5; s2, s3, 0.4; s1, k1, 0.2; s1, k2,
  0.1; s2, k1, 0.3; s2, k2, 0.2; s3, k1, 0.55; s3, k2, 0.5; k1, k2, 0.7`:
  `avdItems` `5 items in 2 constructs`; `avdWithin` Mean correlation within
  each construct `speed 0.5; care 0.7`; `avdCross` across constructs
  `37/120 ≈ 0.308`; `avdFlagged` Items closer to another construct than to
  their own `1: s3 (own 0.45; with care 0.525)` (strictly greater; an item
  alone in its construct is not tested). Refusals: a missing pair
  (`Correlations: the pair k1, k2 is missing; give every pair of different items once, 10 pairs for 5 items`),
  a pair twice, an item paired with itself, an unknown item, one construct.
- **ave**. Fields `loadings` (records `item, construct, loading`, 0–1, items
  unique; `avdInLoadings`), `between` (records `construct, construct, r`,
  each pair once, may be empty; `avdInBetween`). cfg `ave_min`, `cr_min`,
  `loading_min`, `r_max` (decimal strings). Example `s1, speed, 0.8; s2,
  speed, 0.7; s3, speed, 0.9; c1, care, 0.75; c2, care, 0.55`, between
  `speed, care, 0.6`:
  - `avdAve` AVE (mean squared loading): `speed 97/150 ≈ 0.647; care 0.4325`
  - `avdCr` Composite reliability: `speed 288/341 ≈ 0.845; care 338/565 ≈ 0.598`
  - `avdRoot` √AVE: `speed ≈ 0.804; care ≈ 0.658`
  - `avdLow` Items loading at or below the threshold: `1: c2 0.55`
  - `avdPairs` Each pair of constructs: `speed, care |r| 0.6: √AVE speed above it yes, √AVE care above it yes, below 0.85 yes`
  - `avdTests` Tests passed: `9 of 12 pass; not passed: care AVE, care CR, c2 loading`
  Tests: per construct AVE and CR, per item its loading, per pair three.
  Values equal to a strict threshold fail (AVE exactly 0.5; a loading of
  0.6; √AVE equal to |r|). With cfg `ave_min "0.4"`, `cr_min "0.5"`,
  `loading_min "0.5"` the example gives `12 of 12 pass`.

### groups (`agr`)

- **likely**. Fields `rows` (records `group, n, met`, ≥ 2 groups, met ≤ n;
  `agrInRows`), `first`, `second` (group names, required, different;
  `agrInFirst`, `agrInSecond`). Example rows `high, 30, 18; low, 40, 8`, first
  `high`, second `low`: `agrShares` Share meeting the outcome `high 18 of 30 =
  60%; low 8 of 40 = 20%`; `agrRatio` Times as likely (share ÷ share) `3.00×`
  (always 2 places: `≈ 1.93×`, `0.50×`); `agrDiff` Difference in
  percentage points `+40 points`; `agrOdds` Odds ratio (a different figure)
  `6.00`. The table's share column reads `3/5 = 60%`. When the second share is 0: `not defined: no one in low met it`; when
  everyone in the first met it the odds ratio reads `not defined: everyone in
  high met it`.
- **enps**. Field `answers` (whole 0–10, ≥ 1; `agrInAnswers`), or with
  `"named": "yes"` records `name, answer`. Example `10 9 9 8 8 7 6 6 3 10`:
  `agrN` `10`; `agrPromoters` Promoters (9 or 10) `4 of 10 = 40%`;
  `agrPassives` `3 of 10 = 30%`; `agrDetractors` `3 of 10 = 30%`; `agrEnps`
  eNPS `+10` (`≈ −33.3`, `+12.5`, `0`); `agrNear` Answers one point below a
  higher band `4: 2 at 6 (a detractor one point from passive), 2 at 8 (a
  passive one point from promoter); each one moved raises eNPS by 10 points`
  (`0: no answer is at 6 or 8`).
- **bias**. Fields `table` (records `category, early, late`, ≥ 2 categories;
  `agrInTable`), `critical` (the lesson's critical value for its df and
  level, > 0; `agrInCritical`). Example table `yes, 30, 20; no, 10, 15;
  unsure, 5, 2`, critical `5.991`: `agrN` Respondents `early 45, late 37, all
  82`; `agrChi` χ² `41,246/11,655 ≈ 3.539`; `agrDf` Degrees of freedom `2`;
  `agrExceeds` χ² above the critical value `no: 3.539 is not above 5.991, the
  critical value stated`; `agrSmall` Cells with an expected count below 5
  `2: unsure early (expected 315/82 ≈ 3.841), unsure late (expected 259/82 ≈
  3.159)`. Table: observed and expected per cell and each category's part of
  χ². Refusals: a category with no respondents; a column with none.

### sample (`asn`)

- **snowball**. Fields `people` (records `person, referred_by, group`,
  referred_by `-` for a seed; `asnInPeople`), `drop` (a seed, `-` for none,
  default `-`; `asnInDrop`). Example `s1, -, eng; s2, -, ops; a, s1, eng; b,
  s1, eng; c, a, ops; d, b, eng; e, s2, ops; f, e, eng; g, c, eng`, drop `s2`:
  `asnSeeds` `2: s1, s2`; `asnWaves` `wave 0: 2; wave 1: 3; wave 2: 3; wave 3:
  1`; `asnSize` Sample size `9`; `asnTrees` Share from each seed's tree `s1 6
  of 9 ≈ 66.7%; s2 3 of 9 ≈ 33.3%`; `asnGroups` Share per group `eng 6 of 9 ≈
  66.7%; ops 3 of 9 ≈ 33.3%`; `asnLost` Lost with the dropped seed `3: s2, e,
  f`; `asnAfter` Share per group without it `eng 5 of 6 ≈ 83.3%; ops 1 of 6 ≈
  16.7%` (both `no seed dropped` when drop is `-`). People may be listed before
  their referrer. Refusals: self-referral, an unknown referrer, a referral loop
  that reaches no seed (`People: a, b, c refer one another in a loop that
  reaches no seed`), a drop that is not a seed.

### capability (`acp`)

- **profile**. Fields `capabilities` (records `capability, category`,
  unique; `acpInCapabilities`; the book's 24 names and 5 categories are facts
  a preset may carry, hyphenated), `teams` (records `team, capability …`, the
  capabilities in place, possibly none; `acpInTeams`), `levels` (optional:
  `level, capability …`, lowest level first, each capability in at most one
  level; `acpInLevels`), `teams2` (optional: the same teams at a second date;
  `acpInTeams2`). State `capabilities` once at cfg level. Example
  capabilities `vc, delivery; ta, delivery; tbd, delivery; la, architecture;
  wip, lean; viz, lean; ci, delivery; mon, lean`, teams `t1, vc, ta, la; t2,
  vc, tbd, ta, wip`, levels `L1, vc; L2, ta, tbd; L3, la, wip`, teams2 `t1,
  vc, ta, tbd, la`:
  - `acpTeams` Teams: `2: t1, t2`
  - `acpOverall` In place, of all capabilities: `t1 3 of 8; t2 4 of 8`
  - `acpCategories` In place by category: `t1: delivery 2 of 4, architecture 1 of 1, lean 0 of 3; t2: …`
  - `acpLevel` Maturity level reached: `t1 L1 (level 1 of 3); t2 L2 (level 2 of 3)`
    (`t3 none (level 1 of 2, L1, not met)`; `no maturity model given`)
  - `acpHidden` In place above that level (what the level hides): `t1 2: ta, la; t2 1: wip`
  - `acpAdded` Added (and dropped) by the second date: `t1 +1 (tbd)` (`t2 +1 (viz), −3 (ta, tbd, wip)`; `no second date given`)
  - `acpFewest` The capability fewest teams have: `0 of 2 teams: viz, ci, mon`;
    **at most 3 ties are named**, the rest counted: `0 of 2 teams: ta, tbd, la
    and 2 more (the table lists all)`.
  A level is reached only when it and every lower level are met. Table: each
  capability, its category (and level), and `yes` per team that has it.
  Refusals: an unknown capability, one named twice in a record, a capability
  in two levels, a `teams2` team not in `teams`.

### Family B: verification

- `scripts/mathcheck.js`, block `// ---- acckit (Accelerate), family B ----`
  (directly after family A's): 81 assertions over all 14 views, every refusal
  kind and every boundary (equal cuts, AVE exactly 0.5, √AVE equal to |r|,
  |r| equal to 0.85, CR equal to its threshold, expected exactly 5, alpha
  equal to its threshold). Figures worked by hand (alpha 56/59, r = 6/√60,
  √(56/9), χ² 41,246/11,655 checked with Python `Fraction`, AVE/CR of every
  example).
- **Mutation testing.** 59 single breaks of the JS in acckit_b.py (reverse
  coding, band edges, alpha's k/(k − 1) and total, r's denominator and sign,
  n − 1, slope, strength on squares, first differences, pooled sums, AVE,
  CR, every strict/non-strict threshold, ratio vs odds, eNPS bands and
  denominator, χ² and df, waves, trees, drop, level ordering, hidden,
  dropped capabilities, tie listing, every refusal): every one fails the
  block. Seven first survived; a boundary case was added for each.
- **Parity.** 3,832 fuzzed inputs (every view; the targeted refusals plus
  random mutations) through the Python checks and the page's JS on the real
  field specs: same verdict and same refusal sentence every time; no tile
  printed NaN, undefined or Infinity.
- 19 scratch lesson pages (every view, both `named` shapes, every cfg
  threshold) rendered with `scripts/preview_subject.py` outside the
  repository: `labcheck.js` executes and sweeps all, `--expect` matches every
  preset's pinned tiles, and a deliberately wrong pin is reported. At 375 px
  (Playwright, chromium) no page scrolls sideways. Pages are 34–37 KB
  gzipped.
- Note for family A: `aktPp` prints `+12.5 points` for an exact one-place
  value (no `=`), unlike the contract's table (`= +12.5 points`); family B's
  strings follow the code.
