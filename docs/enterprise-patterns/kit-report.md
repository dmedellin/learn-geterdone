# eakit (Enterprise Patterns, Read Along): kit report

Lesson authors configure a lab from this report alone. It records the kit as
built to `docs/enterprise-patterns/PLAN.md` §D (D.0 to D.3), as revised after
the spec review's MF-5 (the pessimistic lock). Every example tile string below
was read off a rendered page with `node scripts/labcheck.js --observe`; none
was copied from the code. Where the kit differs from §D, the "Deviations"
section says how and why. Where it differs from the reference model `earef.py`
(§D.4), the "Model disagreements" section says which one is right.

The kit was last checked against the final PLAN.md (16:48:22), item by item against §R.1, earef.py at
16:28:01 and presets.py at 16:35:46 (2026-10-31). If any of the three changes,
rebuild the harness and re-run the checks under "Verification": the harness
reads presets.py and earef.py directly, so a changed figure shows up as a
failing tile.

## Files (nothing committed)

- `scripts/mathpath/labs/eakit_core.py` (32,762 bytes): the shared parts.
  - `EA_CORE_JS` ships on every page. It holds the printing (eaInt, eaFrac, eaFixed, eaNum, eaPct, eaTimes, eaSigned, eaNames, eaCount, eaPlural, eaSci), the reading (eaScalar, eaRecords, eaPairs, eaList, eaField, eaRead), eaRefuse and eaRun, and eaTableHtml.
  - `EA_WIRE_JS` is the page wiring (eaEl, eaRed, eaRedraw, eaFill). It sets `window.redrawLab`.
  - The Python side mirrors the field parser (`parse`, `parse_scalar`, with the same sentences), turns preset values into text (`to_text`), and holds `presets`, the HTML helpers and `build_lab`.
- `scripts/mathpath/labs/eakit.py` (45,312 bytes): the entry point `eakit_lab(cfg)` and the modes perf, remote, load and uow. Each mode has a base block (`PZ_JS`, `RR_JS`, `LD_JS`, `UW_JS`) and one block per view (`PZ_VIEW_JS[view]`, …), with the Python checks of D.3. `view_lab` is shared with eakit_b.
- `scripts/mathpath/labs/eakit_b.py` (30,558 bytes): the modes inherit, lock, session and money (`IH_JS`, `OL_JS`, `SN_JS`, `MN_JS` and their view blocks).
- `scripts/mathpath/labs/__init__.py`: one import (`eakit,`) and one registry line (`"eakit": eakit.eakit_lab,`). eakit is **not** in `KITS_WITH_EXPECTATIONS`; wiring adds it, last (§H.3).
- `scripts/mathcheck.js`: one block, `// ---- eakit (Enterprise Patterns) ----` … `// ---- end eakit ----`, after the cckit block and before THE VERDICT (414 lines). It holds 248 assertions in one vm context per mode, plus an EA_WIRE_JS run on a fake DOM.
- The §H.1 cckit change: `scripts/mathpath/labs/cckit.py` (45,720 bytes) gains the `book` key on `code/complexity`. The cckit block of mathcheck gains 4 assertions, and `docs/code-complete/kit-report.md` records the key. See "The cckit change (§H.1)".

There is no `content/enterprise_patterns/`: no tooling needed a stub. Nothing in the renderer was edited, and the kit needs nothing more from it.

## Conventions as implemented

**Entry point and cfg.**
- `eakit_lab(cfg)` reads `cfg["mode"]` (perf, remote, load, uow, inherit, lock, session or money) and `cfg["view"]`. The view defaults to the mode's first. An unknown mode or view raises, listing the valid ones.
- Keys common to every view: `mode`, `view`, `presets` (required, non-empty), `preset` (the one shown first; default the first), `title`, `panel_title`, `panel_intro`.
- **A cfg key named like one of the view's inputs** supplies that input to every preset that does not set it. A lesson that compares one timeline under three schemes states the timeline once, as cfg `events`.
- **Lesson-level keys** come from the cfg and never from a preset:
  - `unit` (perf/scale; one lower-case word, a–z, at most 20 letters, default `server`). It goes into the pzEfficiency values ("20 a node") and the crossover ("5 nodes", "1 node"), and into four tile labels: "Throughput a node, first measurement", "Throughput added a node", "Nodes needed", "Projected throughput at the node count given".
  - `fine_label` and `coarse_label` (remote/calls; plain text of at most 40 characters, defaults "fine-grained calls" and "coarse-grained calls"). They go into the six tile labels only, never the values. Lesson 3.6 passes "statements" and "batches".
  - `source` (every family 2 view, optional). When given, the panel intro ends " Figures: <source>.", even after a custom `panel_intro`.
- Any other cfg key raises, naming the keys the view takes.
- **Families.** Every panel intro begins with its family's sentence, even when `panel_intro` overrides the rest. Family 1 (remote/boundary, load/instances, identity, graph and tree, both uow views, inherit, both lock views): "A count over the situation the lesson states. The lab counts; it runs nothing, and no count is a verdict." Family 2 (perf, remote/calls, remote/payload, load/finds, session, money): "The arithmetic of the figures the lesson states (marked with their source). Every figure is the lesson's; the lab does the arithmetic and measures nothing."

**Ids.**
- Prefixes: `pz` perf, `rr` remote, `ld` load, `uw` uow, `ih` inherit, `ol` lock, `sn` session, `mn` money.
- An input's id is `<prefix>In<Key>`, with the key's first letter capitalised: `pzInPoints`, `rrInRemoteUs`, `ldInLatencyMs`, `olInCheckReads`, `uwInAs`.
- Each page ships a preset menu `<prefix>Preset`, a banner `<prefix>Status` and a table `<prefix>Table`.
- Every JS function and variable and every element id (157 names, 144 of them prefixed) was grepped across `scripts/mathpath/labs/*.py`: none is used by another kit. The Python module constants `MODES`, `VIEWS`, `TITLES`, `FAMILY`, `KIT` and `COMMON_CFG` share names with other kits' modules, which is harmless (module scope). The mathcheck block runs in its own vm contexts.

**Inputs.**
- Record inputs are `<textarea>`s (3 rows, 4 for events; they wrap; monospace). Scalars are text boxes. `scheme`, `checkReads` and `rule` are selects. Every control holds its preset's text in the markup, and the preset menu rewrites them.
- Records are `a, 1, 2; b, 3, 4`: fields separated by commas, records by semicolons. A wrong field count is refused as "Calls: record 2 has 2 fields; this list needs 3 (caller, callee, count)".
- Pairs (`nodes`, `groups`) are `a=b; c=d`, optional. Lists (`as`, `ratios`) are space- or comma-separated.
- Names are letters, digits, `.`, `_` and `-`. A parent field takes a name or `-` (none).
- Words (op, action, read, change, needed, concrete, scheme, rule) must be on their list; anything else is refused, naming the list.
- At most 60 records an input. A whole number is at most 10,000,000 (servers at most 10,000; own fields at most 1,000; a ratio at most 1,000,000). A number is a decimal with at most 6 places (`3`, `0.25`, `.5`); fractions and exponents are refused.

**Number format (D.0).**
- Whole numbers: `7,820`, `−1` (U+2212). A signed difference: `+1`, `−1`, `0`.
- A non-whole number prints its reduced fraction, both parts grouped, then two decimals rounded half away from zero on the exact value, with `=` only when those decimals are exact: `125/2 = 62.50`, `51,033/500 ≈ 102.07`.
- Shares: `4/5 = 80%`, `2/3 ≈ 66.7%`, `1 = 100%`, `7,000/7,001 ≈ 100.0%`; `=` when the share is exact at one place (`1/8 = 12.5%`).
- Ratios: `10×` when whole, else the fraction and one place, always with `≈`: `125/37 ≈ 3.4×`, `17/5 ≈ 3.4×`, `9/2 ≈ 4.5×`.
- Lists: `a, b` or `none`. A count with its list: `2: david, martin`, or `0: none`.
- A figure past 30 digits prints `≈ 1.80 × 10^308`.
- Per-system tiles join systems with `; `: `swordfish 20 a server; camel 40 a server`.

**Zero denominators.** A tile with nothing to divide by prints `—` and the banner says why: pzPerUser and pzRatio with one measurement (`a —`), pzMarginal and pzAt for a one-measurement system in scale, uwSaved with no writes (`0 (—)`), olPeakLocks under a scheme with no locks, uwBroken with no `as`. These are never red. Divisor inputs must be positive and are refused naming the field.

**Hostile input.** Every box survives `''`, `banana`, `0`, `-1`, `1/0`, `A>B` and the others in hostile.js. A refused value paints a red one-sentence banner and blanks every tile and the table. `hostile.js` ran every box × value × preset on all 42 harness pages: 5,930 runs, 5,526 refused, none threw, every refusal blanked every tile, and no accepted value printed NaN, undefined or Infinity.

**Build-time refusals (D.3).** A Python mirror reads every preset and raises ValueError, naming the preset and the record, on anything the page would refuse. `parity.py` compared mirror and page on 21,750 fuzzed inputs: 13,274 refused by both, 8,476 accepted by both, none differs. Beyond the field rules above, the build refuses:
- an unknown mode, view or cfg key; a preset key that is not an input; a lesson-level key in a preset; a bad `unit`, label or `source`;
- a duplicate preset id, an `expect` naming a tile the view does not show, an empty `expect`, markup (`< > & "`) in any value;
- perf: a system measured twice at one load or server count;
- remote/boundary: `nodes` naming a class no call has;
- load/finds: a broad query returning fewer rows than wanted;
- load/tree and inherit: no root, two roots, an unknown parent, a cycle (named "a → b → a");
- uow/commit: an op on an object the script has neither loaded nor created, a load of a created object, a second new, anything after a delete;
- uow/order: a key listed twice, a table that refers to itself (with the book's reason), a cycle, an `as` that misses or adds a table;
- inherit: `load`, `find` or `alter` not a class; `load` not concrete;
- lock/timeline: decreasing minutes, a commit with a record or an edit without one, a session acting after its commit, `groups` naming a record no event touches;
- session/objects: time between requests below the service time;
- money: every ratio 0.

**Page weight.**
- A page ships RATIONAL_JS, EA_CORE_JS, EA_WIRE_JS, its mode's base block and its own view's block, nothing more.
- The lab alone (script and markup) is 4.8 to 6.8 KB gzipped, median 5.4 KB; lock/timeline is the heaviest.
- On the harness (a Phenomenology lesson's prose with an eakit lab), the whole lesson is 31.4 to 33.9 KB gzipped, median 32.1 KB, under PLAN's 40 KB budget and well under the 67 KB ceiling. A lesson with code listings adds `theme.CODE_CSS` and its snippets; Code Complete's heaviest such lessons came to 38.9 KB with a heavier lab, so eakit lessons have a few KB more margin.

**Layout.** Checked in Playwright (chromium) on all 42 pages at 375 px and 1280 px: no page scrolls sideways (scrollWidth equals clientWidth), no page error, no request leaves the page. At 375 px the panel stacks under the lab, and a wide table (lock/timeline's six columns) scrolls inside its own `.table-wrap`. At 1280 px the banner, table and "How the lab counts" rules sit in lab-main with the controls and tiles in the side panel.

## Modes, views, fields, tiles

Each field is listed as `key` (kind, default), with its input id and label; — means the field is required. Tiles are listed as id, label, then the value observed on the page named.

### perf (`pz`, family 2)

- **load.** Family 2. Fields:
  - `points` (records of system (name), users (whole 1–10,000,000), ms (number > 0, ≤ 10,000,000); 1–60, —), id `pzInPoints`, labelled "Measurements (system, users, response time in ms)";
  - `users` (whole 1–10,000,000, —), id `pzInUsers`, labelled "Load to read it at (users)";

  Tiles, with their values on §C lesson 1.2, preset `system-a-and-b`:
  - pzPerUser, Change in response time a user, `a 0 ms a user; b 180 ms a user`;
  - pzRatio, Last response time over first, `a 1×; b 10×`;
  - pzAt, Response time at the load given, `a 500 ms; b 1,100 ms`;

- **scale.** Family 2. cfg `unit`. Fields:
  - `points` (records of system (name), servers (whole 1–10,000), tps (number ≥ 0, ≤ 10,000,000); 1–60, —), id `pzInPoints`, labelled "Measurements (system, servers, throughput in tps)";
  - `need` (number > 0, ≤ 10,000,000, —), id `pzInNeed`, labelled "Throughput needed (tps)";
  - `at` (whole 1–10,000, —), id `pzInAt`, labelled "Servers to project at";

  Tiles, with their values on §C lesson 1.3, preset `swordfish-and-camel`:
  - pzEfficiency, Throughput a server, first measurement, `swordfish 20 a server; camel 40 a server`;
  - pzMarginal, Throughput added a server, `swordfish 15; camel 10`;
  - pzCrossover, Where the projections meet or cross, `5 servers (both 80)`;
  - pzNeed, Servers needed, `swordfish 3; camel 1`;
  - pzAt, Projected throughput at the server count given, `swordfish 80; camel 80`;

### remote (`rr`, family 1/2)

- **boundary.** Family 1. Fields:
  - `calls` (records of caller (name), callee (name), count (whole 0–10,000,000); 1–60, —), id `rrInCalls`, labelled "Calls (caller, callee, how many)";
  - `nodes` (pairs `class=node; …`, optional, empty), id `rrInNodes`, labelled "Nodes (class=node; a class not listed runs on main)";
  - `remoteUs` (number > 0, ≤ 10,000,000, —), id `rrInRemoteUs`, labelled "Time of a remote call (µs)";
  - `localUs` (number > 0, ≤ 10,000,000, —), id `rrInLocalUs`, labelled "Time of a local call (µs)";

  Tiles, with their values on §C lesson 7.1, preset `by-class`:
  - rrCalls, Calls, `75`;
  - rrRemote, Remote calls, `75`;
  - rrTime, Time (µs), `75,000`;
  - rrShare, Share of the time in remote calls, `1 = 100%`;
  - rrOneNode, Time with every class on one node (µs), `75`;
  - rrRatio, Time against one node, `1,000×`;

- **calls.** Family 2. cfg `fine_label`, `coarse_label`. Fields:
  - `ops` (records of operation (name), fine (whole 1–10,000,000); 1–60, unique by the first, —), id `rrInOps`, labelled "Coarse-grained calls (operation, fine-grained calls it replaces)";
  - `latencyMs` (number > 0, ≤ 10,000,000, —), id `rrInLatencyMs`, labelled "Latency of a round trip (ms)";
  - `workMs` (number ≥ 0, ≤ 10,000,000, —), id `rrInWorkMs`, labelled "Work in a fine-grained call (ms)";

  Tiles, with their values on §C lesson 3.6, preset `save-an-order`:
  - rrFineTrips, Round trips, fine-grained calls, `25`;
  - rrCoarseTrips, Round trips, coarse-grained calls, `3`;
  - rrFineMs, Time, fine-grained calls (ms), `125/2 = 62.50`;
  - rrCoarseMs, Time, coarse-grained calls (ms), `37/2 = 18.50`;
  - rrLatencyShare, Share of the time of the fine-grained calls spent waiting, `4/5 = 80%`;
  - rrSpeedup, Time of the fine-grained calls over the coarse-grained calls, `125/37 ≈ 3.4×`;

- **payload.** Family 2. Fields:
  - `fields` (records of field (name), bytes (whole 0–10,000,000), needed (`yes` / `no`); 1–60, unique by the first, —), id `rrInFields`, labelled "Fields (field, bytes, needed: yes or no)";
  - `latencyMs` (number > 0, ≤ 10,000,000, —), id `rrInLatencyMs`, labelled "Latency of a round trip (ms)";
  - `bytesPerMs` (number > 0, ≤ 10,000,000, —), id `rrInBytesPerMs`, labelled "Bytes sent a millisecond";
  - `factor` (number > 0, ≤ 10,000,000, —), id `rrInFactor`, labelled "Encoding factor (encoded size over raw)";

  Tiles, with their values on §C lesson 7.3, preset `order-screen`:
  - rrGetterCalls, Calls, one getter a needed field, `5`;
  - rrGetterMs, Time, the getters (ms), `51,033/500 ≈ 102.07`;
  - rrDtoBytes, Bytes in the DTO, `6,066`;
  - rrDtoMs, Time, one DTO (ms), `13,033/500 ≈ 26.07`;
  - rrExtraBytes, Bytes the DTO carries that are not needed, `4,000`;
  - rrSpare, Bytes the saved round trips could have carried, `80,000`;

### load (`ld`, family 1/2)

- **instances.** Family 1. Fields:
  - `tables` (records of table (name), rows (whole 0–10,000,000); 1–60, unique by the first, —), id `ldInTables`, labelled "Tables (table, rows)";

  Tiles, with their values on §C lesson 2.3, preset `small-shop`:
  - ldTables, Tables, `4`;
  - ldRows, Rows, `7,820`;
  - ldRowObjects, Objects, one a row, `7,820`;
  - ldTableObjects, Objects, one a table, `4`;
  - ldLargest, Largest table, and its rows, `line 6,000`;

- **finds.** Family 2. Fields:
  - `wanted` (whole 1–10,000,000, —), id `ldInWanted`, labelled "Rows wanted";
  - `broad` (whole 1–10,000,000, —), id `ldInBroad`, labelled "Rows the broad query returns";
  - `batch` (whole 1–10,000,000, —), id `ldInBatch`, labelled "Rows in a batch";
  - `latencyMs` (number > 0, ≤ 10,000,000, —), id `ldInLatencyMs`, labelled "Latency of a statement (ms)";
  - `rowMs` (number ≥ 0, ≤ 10,000,000, —), id `ldInRowMs`, labelled "Time a row (ms)";

  Tiles, with their values on §C lesson 3.2, preset `fifty-or-one`:
  - ldKeyedStatements, Statements, one find a row, `50`;
  - ldKeyedMs, Time, one find a row (ms), `255`;
  - ldBroadRows, Rows, one broad query, `200`;
  - ldBroadMs, Time, one broad query (ms), `25`;
  - ldBatchStatements, Statements, finds in batches, `5`;
  - ldBatchMs, Time, finds in batches (ms), `30`;
  - ldUnneeded, Rows the broad query returns that are not wanted, `150`;

- **identity.** Family 1. Fields:
  - `finds` (records of class (name), id (name); 1–60, —), id `ldInFinds`, labelled "Finds, in order (class, id)";

  Tiles, with their values on §C lesson 4.2, preset `one-session`:
  - ldFinds, Finds, `7`;
  - ldDistinct, Distinct objects, `4`;
  - ldDuplicates, Finds of an object already found, `3`;
  - ldShared, Found more than once, `customer 7 ×3, product 5 ×2`;

- **graph.** Family 1. Fields:
  - `parents` (records of parent (name), children (whole 0–10,000,000), used (`yes` / `no`); 1–60, unique by the first, —), id `ldInParents`, labelled "Parents (parent, children, used: yes or no)";
  - `batch` (whole 1–10,000,000, —), id `ldInBatch`, labelled "Parents in a batch";

  Tiles, with their values on §C lesson 4.3, preset `orders-and-lines`:
  - ldLazy, Lazy load, a query a used parent, `4 statements, 17 rows`;
  - ldBatched, Lazy load in batches, `3 statements, 17 rows`;
  - ldTwoQueries, Two queries, the parents then every child, `2 statements, 19 rows`;
  - ldJoin, One join, `1 statement, 15 rows`;

- **tree.** Family 1. Fields:
  - `nodes` (records of node (name), parent (name or `-`); 1–60, unique by the first, —), id `ldInNodes`, labelled "Nodes (node, parent; - for the root)";

  Tiles, with their values on §C lesson 4.5, preset `departments`:
  - ldNodes, Nodes, `8`;
  - ldDepth, Depth (the root is 1), `4`;
  - ldPerNode, Queries, one a node's children, `9`;
  - ldPerLevel, Queries, one a level, `5`;
  - ldLob, Queries, the tree in one column, `1`;

### uow (`uw`, family 1)

- **commit.** Family 1. Fields:
  - `script` (records of op (`load` / `new` / `change` / `delete`), object (name); 1–60, —), id `uwInScript`, labelled "Script (op: load, new, change or delete; object)";

  Tiles, with their values on §C lesson 4.1, preset `edit-an-order`:
  - uwImmediate, Writes, each written at once, `6`;
  - uwCommit, Writes at commit, `2`;
  - uwSaved, Writes saved, `4 (2/3 ≈ 66.7%)`;
  - uwWrites, The writes at commit, `INSERT line1; UPDATE order7`;
  - uwClean, Loaded and never changed, `1: customer3`;

- **order.** Family 1. Fields:
  - `keys` (records of child (name), parent (name); 1–60, —), id `uwInKeys`, labelled "Foreign keys (child table, parent table)";
  - `as` (tables, 0–60, name, empty), id `uwInAs`, labelled "An order to check (tables, space-separated; optional)";

  Tiles, with their values on §C lesson 4.4, preset `order-schema`:
  - uwInsertOrder, Insert order, parents first, `customer, orders, payment, product, line`;
  - uwDeleteOrder, Delete order, children first, `line, product, payment, orders, customer`;
  - uwBroken, Keys the order given breaks, `3: orders before customer, line before orders, line before product`;

### inherit (`ih`, family 1)

- **tables.** Family 1. Fields:
  - `classes` (records of class (name), parent (name or `-`), fields (whole 0–1,000), concrete (`yes` / `no`); 1–60, unique by the first, —), id `ihInClasses`, labelled "Classes (class, parent or -, own fields, concrete: yes or no)";
  - `load` (name, —), id `ihInLoad`, labelled "Class to load (a concrete one)";
  - `find` (name, —), id `ihInFind`, labelled "Class to find, with its subclasses";
  - `alter` (name, —), id `ihInAlter`, labelled "Class to add a field to";

  Tiles, with their values on §C lesson 4.6, preset `staff`:
  - ihTables, Tables (single, class, concrete), `1, 4, 3`;
  - ihColumns, Columns (single, class, concrete), `11, 13, 20`;
  - ihEmpty, Empty columns in a row of the class loaded, single table, `2`;
  - ihLoad, Tables read to load one object (single, class, concrete), `1, 3, 1`;
  - ihFind, Tables read to find every instance (single, class, concrete), `1, 4, 3`;
  - ihAlter, Tables altered to add a field (single, class, concrete), `1, 1, 3`;

### lock (`ol`, family 1)

- **reads.** Family 1. Fields:
  - `items` (records of item (name), before (whole 0–10,000,000), after (whole 0–10,000,000), read (`before` / `after`), change (`insert` / `update`); 1–60, unique by the first, —), id `olInItems`, labelled "Items (item, before, after, read: before or after, change: insert or update)";

  Tiles, with their values on §C lesson 6.1, preset `martin-and-david`:
  - olSeen, Total the reader saw, `15`;
  - olBefore, Total before the commit, `12`;
  - olAfter, Total after the commit, `17`;
  - olConsistent, Matches a state of the data, `no: 15 is neither 12 nor 17`;
  - olLevel, Isolation level, `repeatable read allows it (a phantom); serializable prevents it`;

- **timeline.** Family 1. Fields:
  - `events` (records of minute (whole 0–10,000,000), session (name), action (`read` / `edit` / `commit`), record (name or `-`); 1–60, —), id `olInEvents`, labelled "Events (minute, session, action: read, edit or commit, record; - for a commit)";
  - `scheme` (`none` / `optimistic` / `pessimistic`, —), id `olInScheme`, labelled "Scheme";
  - `groups` (pairs `record=group; …`, optional, empty), id `olInGroups`, labelled "Groups (record=group; a record not listed is its own; optional)";
  - `checkReads` (`no` / `yes`, `no`), id `olInCheckReads`, labelled "Check the records only read (optimistic)";

  Tiles, with their values on §C lesson 6.2, preset `no-control`:
  - olCommitted, Committed, `2: david, martin`;
  - olConflicts, Conflicts at commit, `0: none`;
  - olRefused, Refused a lock, `0: none`;
  - olLostUpdates, Lost updates, `1`;
  - olRedo, Minutes of work redone, `0`;
  - olPeakLocks, Most locks held at once, `—`;

### session (`sn`, family 2)

- **objects.** Family 2. Fields:
  - `users` (whole 1–10,000,000, —), id `snInUsers`, labelled "Users";
  - `serviceMs` (number > 0, ≤ 10,000,000, —), id `snInServiceMs`, labelled "Service time of a request (ms)";
  - `thinkMs` (number > 0, ≤ 10,000,000, —), id `snInThinkMs`, labelled "Time between a user's requests (ms)";

  Tiles, with their values on §C lesson 6.6, preset `hundred-users`:
  - snStateful, Objects, one a user (stateful), `100`;
  - snStateless, Objects busy on average (stateless), `10`;
  - snIdle, Share of the time a stateful object is idle, `9/10 = 90%`;
  - snPerObject, Users a stateless object serves, `10`;

- **state.** Family 2. Fields:
  - `users` (whole 1–10,000,000, —), id `snInUsers`, labelled "Users";
  - `stateBytes` (whole 1–10,000,000, —), id `snInStateBytes`, labelled "Session state (bytes)";
  - `requests` (whole 1–10,000,000, —), id `snInRequests`, labelled "Requests in a session";
  - `idBytes` (whole 0–10,000,000, —), id `snInIdBytes`, labelled "Session id (bytes)";

  Tiles, with their values on §C lesson 6.7, preset `a-megabyte`:
  - snWire, Bytes on the wire a request, client state, `2,000,000`;
  - snSessionWire, Bytes on the wire a session, client state, `40,000,000`;
  - snIdOnly, Bytes on the wire a request, server or database state, `32`;
  - snMemory, Bytes held in memory, server state, `100,000,000`;
  - snDatabase, Bytes read and written a request, database state, `2,000,000`;

### money (`mn`, family 2)

- **allocate.** Family 2. Fields:
  - `amount` (whole 0–10,000,000, —), id `mnInAmount`, labelled "Amount (cents)";
  - `ratios` (ratios, 2–20, whole 0–1,000,000, —), id `mnInRatios`, labelled "Ratios (whole numbers, space-separated)";
  - `rule` (`nearest` / `down` / `up` / `last` / `allocator`, —), id `mnInRule`, labelled "Rounding rule";

  Tiles, with their values on §C lesson 2.6, preset `nearest`:
  - mnShares, Shares (cents), `4, 2`;
  - mnTotal, Total of the shares, `6`;
  - mnDiff, Total less the amount, `+1`;
  - mnExact, Exact shares, `7/2 = 3.50, 3/2 = 1.50`;
  - mnFurthest, Largest gap from an exact share, `1/2 = 0.50`;

### Behaviour the tiles do not show

- **perf/load** reads a response time on the straight line between the two measurements either side of the load given. Outside a system's measured loads the tile says `outside its measured loads` and the lab does not extrapolate. With one measurement, pzPerUser and pzRatio print `a —`.
- **perf/scale** projects with the measured value where n was measured, else the line through the first and last measurements. The crossover is computed for exactly two systems (`—: the crossover compares two systems` otherwise; `—: each system needs two measurements`; `none` when the lines never meet within 10,000). pzNeed prints `never at this rate` for a rate ≤ 0 that falls short, `more than 10,000` when the need lies past the search, and `not measured: one measurement gives no rate`. Observed on an edge page with `unit: "node"`: `3 nodes (both 30)`, `1 node (both 1)`, `a never at this rate; b 6`.
- **remote/boundary**: a class with no node runs on `main`. A self-call is local.
- **load/instances**: the largest table is the first with the most rows (`a 5` on a tie of a and b).
- **load/tree**: one query a level is depth + 1, the last finding the empty level below the leaves.
- **uow/commit**: INSERTs, then UPDATEs, then DELETEs, each in the order the script first names the object. Observed: `INSERT n; UPDATE d; DELETE c`; a created and deleted object writes nothing (`3 (1 = 100%)` saved).
- **uow/order**: ties go alphabetically. With no `as`, uwBroken prints `—`.
- **lock/reads**: olConsistent says `no, though 8 equals the total after the commit` when a mixed read happens to equal a state.
- **lock/timeline**, as revised for MF-5. Every group has a version from 0; a commit adds one to each group the session edited. Under pessimistic, a session takes the lock at its first read or edit of a group it edits anywhere in the timeline; a read of a group it never edits takes none. This is the exclusive write lock, the first of Pessimistic Offline Lock's three, taken when the record is first loaded for editing, and the banner and rules say so. Taking a lock another session holds is refused, which can now happen at a `read`: that session is listed in olRefused, its locks are released and its later events are skipped (the table says `skipped`). On 6.2 `pessimistic`: `1: martin`, `0: none`, `1: david`, `0`, `0`, `1`. Optimistic with `checkReads` `yes` also checks the groups a session only read. Redo is the minutes from a failed session's first event to its failure, the refused event included (`10` on 6.2 `optimistic`, `0` on 6.2 `pessimistic`, where david is refused at his first read).
- **money/allocate**: `last` gives the last share what is left, possibly negative. `allocator` floors each share and gives the leftover cents one each from the first (`34, 33, 33`).

## The cckit change (§H.1)

- New lesson-level key `book` on `code/complexity` only: `"code-complete"` (the default) or `"other"`. Any other value raises. Another view given `book` raises, as for any unknown key.
- With `"other"`, a small block `CO_BOOK_OTHER_JS` ships after the complexity view and wraps it. It rewrites three phrases of the banner and nothing else: "McConnell's guidance on what" becomes "McConnell's guidance in Code Complete on what", "The book prints its bands" becomes "McConnell prints his bands", and the `?:` note's "the kit's choice, not the book's." becomes "the kit's choice, not McConnell's.". No tile changes. The banner is plain text, so "Code Complete" is not italic.
- With the default, nothing ships: every Code Complete page is byte-identical, and `python3 scripts/build_paths.py --check` says every published page matches (1,147 pages).
- mathcheck's cckit block gains 4 assertions: the three phrases appear and "book" does not; the default still has all three originals; "other" differs only in those phrases; no tile changes. Breaking one rewrite failed 2 of them; the kit was restored.
- The basis view's `?:` note still says "not the book's". §H.1 names only complexity, and no Enterprise Patterns lesson uses basis.
- Lessons 1.1, 2.2, 2.7, 5.2 and 5.4 can now set `"book": "other"`.

## Verification

- **Harness.** It is all in `/tmp/claude-0/-home-claude/d46a89a5-ae93-5f9f-84a3-4e1ae07e83c0/scratchpad/eakit/`. `build.py` renders every §C preset in `presets.py` into a lesson page through `render.lesson_page_with_lab`, with each tile's expectation computed by `earef.py`. `build.py --extra` adds 18 edge-case pages from `extra.py`.
- **labcheck.** `node scripts/labcheck.js --expect h/scripts/manifest.json`: 42 pages executed and swept, 42 pinned, 0 failing. The 24 §C pages pin 85 presets and 446 tiles, every one equal to earef's figure (with the exceptions under "Model disagreements", none of which a §C preset reaches). The 18 edge pages pin 60 presets and 296 tiles. `--observe` ran on every page (`observe.json`).
- **Hostile sweep.** `hostile.js`: 5,930 runs, 5,526 refused, 0 failing.
- **Parity.** `parity.py`: 21,750 fuzzed inputs through the Python mirror and the page's JS, 0 differ; the slowest compute took 46 ms.
- **mathcheck.** `node scripts/mathcheck.js` passes in full ("every arithmetic assertion passes"). The eakit block holds 248 assertions: the printing and reading rules, every §C preset (generated from earef), the edge cases, the refusals, the MF-5 lock cases and the wiring on a fake DOM. Every view has at least one case.
- **Mutation testing.** `mutate.py` broke 57 lines of the kit, one at a time, covering every Compute function, the printing, the parser and the wiring, and ran the eakit block against each. 55 were killed. The two survivors are equivalent: #13 interpolates at a segment's right end, where the line and the measurement give the same value; #45 counts lost updates for every scheme, but a committed optimistic or pessimistic session never has a changed edited group. The kit files were checked restored by md5.
- **Layout.** Playwright, as under "Layout".
- **build_paths.** `python3 scripts/build_paths.py --check`: every published page matches content/ (1,147 pages).
- **tests.** `python3 -m unittest tests.test_site_invariants -k Lab`: 10 tests, all OK. The `code_complete`/`cckit` tests: 3, all OK.

## Deviations from §D, each decided and implemented

1. **Grouped fractions.** Both parts of a fraction are grouped (`51,033/500 ≈ 102.07`), as earef and §C print them. cckit does not group them.
2. **Ratios always say ≈.** eaTimes prints `≈` for any ratio that is not whole (`11/5 ≈ 2.2×`), as D.0 and §C do, where cckit's ccTimes prints `=` when one place is exact.
3. **Shares say = when exact at one place** (`1/8 = 12.5%`), following cckit's D.0 rule. earef prints `≈`. No §C preset reaches it.
4. **One measurement.** pzPerUser and pzRatio print `a —` (no rate from one point). earef prints `a — ms a user` and `a 1×`.
5. **Past the search.** pzNeed prints `more than 10,000` when the rate is positive but the need lies beyond the 10,000 searched; `never at this rate` only when the rate is not positive. earef prints `never at this rate` for both.
6. **The crossover uses `unit`** and pluralises (`1 node`, `5 nodes`). earef hard-codes `servers`.
7. **Bounds.** A whole number is at most 10,000,000 and a decimal has at most 6 places; §D gives no bound for numbers.
8. **Refusals beyond §D.1**: `nodes` or `groups` naming nothing in the instance, a duplicate key in uow/order. A self-call in remote/boundary is allowed and local.
9. **uwSaved** prints `0 (—)` when there are no writes at once.
10. **uwBroken** prints `—` when no `as` is given.
11. **`source`** is appended even after a custom `panel_intro`, so a book figure is always marked.
12. **Record inputs are textareas**, wrapping, with the preset text in the markup.
13. **The rules paragraph** ("How the lab counts.") is always on the page, under the table, not in a `<details>`.
14. **cfg `fine_label`/`coarse_label`.** §C lesson 3.6 says cfg `labels`; the kit implements D.0's two keys. Lesson 3.6 must pass `"fine_label": "statements", "coarse_label": "batches"`.
15. **The basis view** (cckit) still says "the book's"; see §H.1 above.
16. *(Withdrawn: the uow/commit banner now says "the order view is lesson 4.4's", as §R.1 item 4 sets.)*
17. **Field ids** `rrInRemoteUs` and `rrInLocalUs` follow the field keys `remoteUs` and `localUs`.

## §R.1, checked item by item

1. lock/timeline, pessimistic lock at first read or edit of a group the session edits anywhere: in the kit; the rules add "not when the edit begins". 6.2 `pessimistic` gives `1: martin`, `1: david`, redo `0`, peak `1`; `exercise-pessimistic` gives `1: ann`, `1: bo`, redo `0`.
2. load/tree, ldPerLevel = depth + 1: in the kit; the rules end "Both counts include the queries that come back empty." `departments` gives `5`.
3. load/instances, ldRatio removed, ldLargest added (first on a tie): in the kit. `small-shop` gives `line 6,000`.
4. Banners: uow/commit says "… the order view is lesson 4.4's."; remote/calls says "The lab assumes the work is the same either way; what the coarse calls remove is the waits."

remote/boundary is unchanged; 7.4's exercise (`nodes` "app=phone") gives 3 remote calls and 150,054 µs, matching earef.

## Model disagreements (earef.py, §D.4)

The kit is right in each case; none affects a §C figure.
- **Shares exact at one place** (deviation 3): earef prints `≈ 12.5%`, D.0's rule gives `=`.
- **One measurement in perf** (deviation 4): earef's `a — ms a user` puts a unit after a dash, and its `a 1×` claims a ratio of a point to itself.
- **pzNeed past the search** (deviation 5): earef says `never at this rate` for a positive rate, which is false.
- **The crossover's unit** (deviation 6): earef ignores cfg `unit`.

Earlier revisions of earef changed under the kit three times (ldLargest replacing ldRatio, ldPerLevel = depth + 1, the MF-5 pessimistic lock, then new or changed presets for 2.6, 4.3 and 7.4); the kit follows the current version in each.

## For wiring

- Add `eakit` to `build_paths.KITS_WITH_EXPECTATIONS`, last (§H.3). Every preset needs an `expect` with at least one tile; take the figures from earef or `labcheck.js --observe`, never from memory.
- Set cfg `unit` on perf/scale lessons that do not count servers; set `fine_label`/`coarse_label` on 3.6; set `source` on every family 2 lesson whose figures are the book's.
- For a three-scheme lock lesson, state `events` (and `groups`) once in the cfg and give each preset only its `scheme`.
- The mathcheck §C cases are generated by `gen_mathcheck.py` from presets.py and earef, and `assemble.py` re-inserts the block. If presets change before wiring, re-run `build.py --extra`, labcheck `--expect`, `assemble.py` and mathcheck.
- Lessons 1.1, 2.2, 2.7, 5.2 and 5.4 set `"book": "other"` on their cckit complexity labs.
