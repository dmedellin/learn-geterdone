# levkit (Leviathan, Read Along): kit report

**Ready (2026-11-14, UTC).** Family A: `reckon/names`, `deliberate/will`,
`worth/price`, `equality/coalition`, `covenant/perform`, `covenant/fool` are
built, registered and verified. Family B: see its section at the end.

Lesson authors configure a lab from this report alone. It records the kit as
built to `docs/leviathan/PLAN.md` §0 and §D. Family A (reckon, deliberate,
worth, equality, covenant) is `levkit.py` and is reported here first; family
B's section (assembly, succession, tax, law, canon) follows at the end under
its own heading. The seam between the two modules is
`docs/leviathan/kit-contract.md`. Every example tile string in family A's
section was read off a rendered scratch page with
`node scripts/labcheck.js --observe` and was also worked by hand.

**Field names and readings that differ from, or add to, PLAN §D (family A).**
Read these before drafting a lab cfg:

- deliberate/will: PLAN's `options` ("the action deliberated") is the field
  **`action`**; `end` takes **`as-last`** (the default: the action follows the
  last motion), `done`, `omitted` or `impossible`. `done`/`omitted` that
  contradict the last motion are **refused** (on Hobbes's definition the will
  is the last motion, so they cannot disagree).
- reckon/names: **a name defined twice is refused** ("a name of inconstant
  signification cannot be reckoned with, so keep one definition"). To show
  Chapter 4's name defined two ways, give two presets, one per definition,
  and pin the verdicts that change. A name may not be both simple and
  defined. A defined name whose parts reach a name that is neither simple
  nor defined is not refused: it adds up to nothing, and every claim using it
  is insignificant.
- reckon/names: the subject and the predicate of a claim may each be
  **several names separated by spaces, read as their sum** (`round
  quadrangle` is round + quadrangle). A single name of several words takes
  hyphens (`round-quadrangle`), and is then one name that must itself be
  simple or defined.
- worth/price: needs are rationals (`1/2`, `0.25`, at most 1,000); amounts
  are whole numbers. `dignity` is for every person or for none.
- covenant/perform: the tie rule is the input **`tie`** (`keep`, default, or
  `break`), so it can be set once at cfg level or per preset.

## Files

- `scripts/mathpath/labs/levkit.py`: the entry point `levkit_lab(cfg)`,
  `mode_lab(cfg, mode, spec)` (shared with family B), `LVK_CORE_JS` (shipped
  on every levkit page: `lvkStatus`, `lvkRead`, `lvkParseRat`, `lvkPct`,
  `lvkDec`, `lvkListed`, `lvkNameSeq`), levkit's field kinds (`rat`, `NAMES`,
  `NAMES_DASH`, `lrec`, `llist`) and their Python mirror, a thin copy of
  acckit's `_build_lab` that reads them, and family A's five modes: a base
  block (`LRK_JS`, `LDE_JS`, `LWO_JS`, `LEQ_JS`, `LCV_JS`) and one block per
  view, with the Python `check` of every view. It imports `levkit_b` lazily
  inside `levkit_lab`.
- `scripts/mathpath/labs/eakit_core.py`: used unchanged (imported as `ea`).
- `scripts/mathpath/labs/__init__.py`: one import (`levkit,`) and one
  registry line (`"levkit": levkit.levkit_lab,`).
- `scripts/build_paths.py`: `"levkit"` added to `KITS_WITH_EXPECTATIONS`
  (nothing added to `GENERATED_PATHS`; the Subject is wired later).
- `scripts/mathcheck.js`: the block `// ---- levkit (Leviathan), family A
  ----` … `// ---- end levkit family A ----`, after acckit family B and
  before levkit family B's block and THE VERDICT.

## Conventions (both families)

**Entry point and cfg.** A lesson's lab is `("levkit", cfg)`, with
`cfg["mode"]` and `cfg["view"]` (default: the mode's first view). An unknown
mode or view raises, listing the valid ones. Keys common to every view:
`mode`, `view`, `presets` (required, non-empty), `preset` (the one shown
first; default the first), `title`, `panel_title`, `panel_intro`. **A cfg key
named like one of the view's inputs supplies it to every preset that does
not set it** (a reckon lesson states its `simple`, `defs` and `opposed` once
and varies `claims` per preset). Any other key raises, naming the keys the
view takes.

**Panel intro.** By default: "A figure computed from what the lesson states.
It shows what follows on Hobbes’s definitions as written here; whether they
describe men and commonwealths is what the book argues." A `panel_intro` in
the cfg replaces it; its first sentence is put back in front if missing.

**The caution.** Every status line, in every view of both families, ends
"; the figure follows from what the lesson states, on Hobbes’s definitions as
stated." (`lvkStatus`). Under the tiles each view prints "How the lab
counts." with its rules sentence, quoted per view below.

**Presets.** Each preset is `{"id": "lower-case-hyphens", "label": "plain
text", <inputs>..., "expect": {tile_id: "exact text"}}`. **Every preset must
pin at least one tile** (levkit is in `KITS_WITH_EXPECTATIONS`). Read the
strings off your own rendered page with `node scripts/labcheck.js --observe
<page>` (render with `python3 scripts/preview_subject.py leviathan --course
<slug> --out <dir>`), never out of this report without checking. A preset the
page would refuse fails the build, naming the preset and the reason
(`levkit/reckon/names preset 'cycle': The definitions go round in a circle:
…`). Labels name the instance; outcomes go in `expect`. The other selects on
a page (`ldeInEnd`, `leqInRule`, `lcvInTie`) are inputs, not preset menus,
and need no expectations.

**Ids.** Family A: `lrk` reckon, `lde` deliberate, `lwo` worth, `leq`
equality, `lcv` covenant. Family B: `las`, `lsu`, `ltx`, `llw`, `lcn`.
Shared helpers `lvk`/`LVK_`. No prefix changed from PLAN §D. An input's id is
`<prefix>In<Key>`, the key's first letter capitalised (`lrkInClaims`,
`lcvInCost1`). Each page has `<prefix>Preset` (the worked-example menu that
`expect` pins), `<prefix>Status` and `<prefix>Table`.

**Input formats.**
- **Names**: letters, digits, `.`, `_`, `-`; no spaces. **A name of several
  words is written with hyphens: `round-quadrangle`, `natural-philosophy`,
  `body-politic`.** Names are compared exactly as typed: `Body` and `body`
  are two names, and so are `round-quadrangle` and `round_quadrangle` (use
  hyphens throughout). Names print as typed.
- **A cell of names** (reckon's parts, subject and predicate; family B's
  lists inside a record): names separated by spaces inside one
  comma-separated cell: `man, animal rational`. A name twice in one cell is
  refused.
- **Records**: cells separated by commas, records by semicolons: `a, 2; b,
  3`. In a preset, a string, or a Python list of records, each a list of
  cells (a cell that is itself a list is joined by spaces): `[["man",
  ["animal", "rational"]], ["animal", "body animated"]]`.
- **Lists**: separated by spaces or commas: `strength eloquence riches`,
  `1/10 1/4 0.5`.
- **A rational** (`rat`): a decimal with at most 6 places or a fraction of
  whole numbers with at most 8 digits above and below: `3`, `0.25`, `1/3`,
  `7/2`. `1/0` is refused. A chance or certainty is a rational from 0 to 1.
- Whole numbers (`12`), and words from a select (`yes`, `exceed`).
- A wrong value paints one red sentence and blanks every tile and the table
  (`Claims (claim, subject, predicate: subject is predicate), record 2:
  subject "round!" should be letters, digits, dots, hyphens or underscores (a
  name of several words takes hyphens: round-quadrangle)`).

**Number format.** A whole number prints grouped (`1,024`); any other
rational is `eaNum`: the fraction and two places, `=` when exact and `≈`
otherwise (`32/3 ≈ 10.67`, `9/5 = 1.80`, `−39/5 = −7.80`); minus is U+2212.
**Chances and shares are `lvkPct`**: the fraction and its percentage to at
most two decimals, trailing zeros dropped, `=` when exact: `1/4 = 25%`,
`1/8 = 12.5%`, `1/3 ≈ 33.33%`, `1 = 100%`, `0 = 0%`. A listed tile is `n:
a, b` or `0: none`.

**Exactness.** Every figure is a count, a list of names, or an exact BigInt
rational. Nothing is rounded before it is printed, and nothing typed is
evaluated as script.

## Family A (levkit.py): modes, views, fields, tiles

Each field is `key` (kind, default; — means required), with its label.
Tiles are id, label, then the value observed on the preset named.

### reckon (`lrk`)

- **names.** Names as sums of names; each claim true, false, absurd or
  insignificant by the definitions. Fields:
  - `simple` (list of 1–40 names, —), "Simple names (admitted with no
    definition)": the bottom of the reckoning;
  - `defs` (records `name, parts`, parts a cell of names; 0–40, empty),
    "Definitions (name, then its parts separated by spaces)";
  - `opposed` (records `a, b`, two distinct simple names; 0–20, empty),
    "Names that cannot be added (two simple names)";
  - `claims` (records `claim, subject, predicate`, subject and predicate each
    a cell of one or more names; 1–30, —; claim ids unique), "Claims (claim,
    subject, predicate: subject is predicate)".

  Preset `vocabulary` (simple `body animated rational round quadrangle
  figure incorporeal`; defs `animal, body animated; man, animal rational;
  circle, figure round; square, figure quadrangle`; opposed `round,
  quadrangle; body, incorporeal`; claims `c1, man, animal; c2, animal, man;
  c3, round quadrangle, figure; c4, man, incorporeal; c5, man, centaur; c6,
  circle, figure`):
  - lrkNames, Names, `7 simple, 4 defined`;
  - lrkExpand, Each defined name, added up, `animal = animated + body; man =
    animated + body + rational; circle = figure + round; square = figure +
    quadrangle` (definitions in input order, each expansion alphabetical);
  - lrkVerdicts, Each claim, `c1 true; c2 false; c3 absurd; c4 absurd; c5
    insignificant; c6 true`;
  - lrkCounts, Verdicts, `2 true, 1 false, 2 absurd, 1 insignificant`;
  - lrkTrue, True, `2: c1, c6`; lrkFalse, False, `1: c2`; lrkAbsurd, Absurd,
    `2: c3, c4`; lrkEmpty, Insignificant, `1: c5`.

  Status: "6 claims: 2 true, 1 false, 2 absurd, 1 insignificant; a claim is
  true when every simple name of the predicate is in the subject; the figure
  follows …". Table (claim, subject, adds up to, predicate, adds up to,
  verdict, why); the reasons on this preset: c1 `every part of the predicate
  is in the subject`; c2 `the subject lacks rational`; c3 `round and
  quadrangle cannot be added (in the subject)`; c4 `body and incorporeal
  cannot be added (subject and predicate together)`; c5 `centaur stands for
  nothing`.

  Preset `empty` (the same simple names and opposed pairs; defs `animal,
  body animated; man, animal rational; spirit, incorporeal substance`; claims
  `c1, spirit, incorporeal; c2, man, body; c3, round-quadrangle, figure`):
  lrkExpand `animal = animated + body; man = animated + body + rational;
  spirit = nothing (substance stands for nothing)`; lrkVerdicts `c1
  insignificant; c2 true; c3 insignificant`. c1's reason is `spirit is
  defined through substance, which stands for nothing`; c3's is
  `round-quadrangle stands for nothing`, because the hyphenated name is one
  name and is not defined, while `round quadrangle` with a space is the sum,
  and absurd.

  **Verdict precedence: insignificant > absurd > true/false.** The rules
  sentence: "A defined name is the sum of its parts, and a part may itself be
  defined; adding up every part down to the simple names gives the name's
  expansion (listed in alphabetical order). A claim 'subject is predicate'
  may give several names on either side, read as their sum. Its verdict, in
  this order of precedence: insignificant, when a name in it, or a name it is
  defined through, is neither simple nor defined, so stands for nothing; else
  absurd, when the subject, the predicate, or the two together contain a pair
  of names that cannot be added; else true, when every simple name of the
  predicate is in the subject's expansion; else false. A name defined through
  itself, directly or through others, is refused, naming the circle." The
  reason given is the first found: names in the claim in order (subject, then
  predicate); for absurdity the subject first, then the predicate, then the
  two together, with the opposed pairs in input order. A false claim's reason
  lists every missing simple name, alphabetically.

  Refuses, in this order: `Definitions define x twice (records 1 and 3); a
  name of inconstant signification cannot be reckoned with, so keep one
  definition`; `b is both a simple name and defined (Definitions, record 1);
  a name is one or the other`; `Opposed pairs, record 1: x is not one of the
  simple names`; `Opposed pairs, record 1 pairs a with itself`; **a definition
  cycle, named from where it closes**: `The definitions go round in a circle:
  x → y → z → x; a name cannot be defined through itself` (definitions are
  searched in input order and parts in order; `x, a x` gives `x → x`).

  For Hobbes's own examples: "incorporeal substance" is a claim subject
  `incorporeal substance` (two names, summed), with `opposed` `body,
  incorporeal` and `substance` defined to include `body`; the schoolmen's
  empty terms are names left out of both `simple` and `defs`.

### deliberate (`lde`)

- **will.** The will as the last appetite or aversion. Fields:
  - `action` (name, —), "The action deliberated (one name)";
  - `steps` (records `step, motion, toward`; motion `appetite`, `aversion`,
    `hope` or `fear`; toward `do` or `omit`; 1–30, —; step names unique),
    "Steps (step, motion, toward: do or omit)";
  - `end` (select `as-last`, `done`, `omitted`, `impossible`; `as-last`),
    "How the deliberation ends".

  Preset `five-steps` (action `fight`, steps `s1, appetite, do; s2, fear,
  do; s3, hope, do; s4, aversion, do; s5, appetite, do`):
  - ldeSteps, Steps, `5`;
  - ldeAlternations, Changes of direction, `4`;
  - ldeLean, Steps inclining each way, `3 toward doing, 2 toward omitting`;
  - ldeWill, The will (the last motion), `to do (s5: appetite toward doing)`;
  - ldeOutcome, Outcome, `fight done`;
  - ldeWills, The will had it ended at each step, `s1 do, s2 omit, s3 do, s4
    omit, s5 do`;
  - ldeOpposite, Earlier stops that give the opposite will, `2 of 4: s2, s4`.

  Preset `omitted` (the same, s5 `fear, do`, end `omitted`): ldeWill `to omit
  (s5: fear toward doing, an aversion)`, ldeOutcome `fight omitted`,
  ldeOpposite `2 of 4: s1, s3`. Preset `impossible` (steps `s1, appetite, do;
  s2, aversion, omit`, end `impossible`): ldeWill `to do (s2: aversion toward
  omitting)`, ldeOutcome `fight not done: thought impossible`, ldeOpposite `0
  of 1`. A single step prints ldeOpposite `no earlier step`.

  Status: "The will is the last appetite or aversion, s5, so the will is to
  do and fight is done; stopped earlier, 2 of 4 steps would have given the
  opposite will; the figure follows …". Table: step, motion, toward,
  inclines to, will if it ended here (`the same` / `the opposite`).

  Rules: "Each step is an appetite or an aversion toward doing or toward
  omitting the action; hope counts as an appetite and fear as an aversion. A
  step inclines to doing when it is an appetite toward doing or an aversion
  toward omitting, and otherwise to omitting. The will is the last step,
  whatever the earlier ones were and however many lean the other way; had
  deliberation ended at an earlier step, that step would have been the will.
  A change of direction is a step that inclines the other way from the one
  before. The end as-last means the action follows the will; done or omitted
  must agree with the last step, or the inputs are refused; impossible means
  the action is not done because it was thought impossible."

  Refuses: `The deliberation ends with the action done, but its last motion
  (s1) inclines to omit it; on Hobbes’s definition the will is that last
  motion, so an action done follows a last appetite to do it`, and the like
  for `omitted` after a last motion toward doing.

### worth (`lwo`)

- **price.** A person's powers priced by buyers with different needs.
  Fields:
  - `powers` (list of 2–6 names, —), "Powers (2 to 6 names, in order)";
  - `persons` (records `person, amount…`, one whole amount ≥ 0 per power in
    the order of `powers`; 2–12, —; names unique), "Persons (person, then an
    amount of each power)";
  - `buyers` (records `buyer, need…`, one rational need 0–1,000 per power;
    1–6, —; names unique), "Buyers (buyer, then a need for each power)";
  - `dignity` (records `person, value`, value a rational ≥ 0; empty, or one
    for every person), "Dignity set by the commonwealth (person, value; empty
    for none)".

  Preset `three-buyers` (powers `strength eloquence riches`; persons `a, 5,
  1, 2; b, 2, 4, 1; c, 1, 1, 6; d, 3, 3, 3`; buyers `general, 3, 0, 1;
  lawyer, 0, 3, 1; merchant, 1, 1, 2`):
  - lwoPrices, Each person’s price to each buyer, `general: a 17, b 7, c 9, d
    12; lawyer: a 5, b 13, c 9, d 12; merchant: a 10, b 8, c 14, d 12`;
  - lwoRanks, Each buyer’s ranking, `general: a > d > c > b; lawyer: b > d >
    c > a; merchant: c > d > a > b`;
  - lwoTop, The person each buyer would pay most for, `general: a; lawyer: b;
    merchant: c`;
  - lwoSame, Does every buyer rank them the same?, `no: on a and b, general
    ranks a above b and lawyer ranks b above a`;
  - lwoDignity, Dignity against each buyer’s price, `no dignity given`;
  - lwoApart, Dignity apart from every buyer’s price, `no dignity given`.

  Preset `dignity` (the same, dignity `a, 12; b, 13; c, 10; d, 12`):
  lwoDignity `a 12: below general, above lawyer, above merchant; b 13: above
  general, equal to lawyer, above merchant; c 10: above general, above
  lawyer, below merchant; d 12: equal to general, equal to lawyer, equal to
  merchant` (read: a's dignity, 12, is below the general's price); lwoApart
  `2: a, c`. Preset `one-buyer` (buyers `even, 1, 1, 1`): lwoRanks `even: d >
  a = c > b`, lwoSame `one buyer only: nothing to compare`. With ties and
  agreement: lwoRanks `x: a = b = c > d; …`, lwoTop `x: a, b, c (tied); …`,
  lwoSame `yes: every buyer ranks a = b = c > d`.

  Status: "4 persons priced by 3 buyers; the same ranking for every buyer:
  no; a price is what a buyer would give, so it depends on the buyer; the
  figure follows …". Table: person, one price column per buyer, dignity.

  Rules: "A person's price to a buyer is the sum, over the powers, of the
  buyer's need for that power times the person's amount of it, exact. Each
  buyer ranks the persons by price, highest first; equal prices share a
  place (written =) and are listed in input order. The rankings agree when,
  for every pair of persons, every buyer puts them in the same order or ties
  them alike; otherwise the first pair in input order on which a buyer
  differs from the first buyer is named. A dignity is the public worth the
  commonwealth sets, compared with each buyer's price as above, equal to or
  below it; it is given for every person or for none." A tie for one buyer
  against an order for another is a disagreement (`x ranks a equal to b and
  y ranks a above b`).

  Refuses: `Persons, record 2 (b) gives 2 amounts, and there are 3 powers`;
  `Buyers, record 1 (x) gives 3 needs, and there are 2 powers`; `Dignity,
  record 2: q is not one of the persons`; `Dignity names a twice`; `Dignity
  is given for 1 of the 2 persons; give it for every person, or for none`.

### equality (`leq`)

- **coalition.** Who can be overcome, and by how few. Fields:
  - `persons` (records `person, strength`, strength a whole number ≥ 1; 2–10,
    —; names unique), "Persons (person, strength: a whole number from 1)";
  - `machination` (rational 1–1,000, `1`), "Factor for secret machination (1
    for none)": multiplies the attackers' summed strength (secret
    machination, or the victim asleep);
  - `rule` (select `exceed` or `match`, `exceed`), "To overcome is to".

  Preset `six-men` (persons `a, 2; b, 3; c, 4; d, 5; e, 6; f, 9`):
  - leqStrongest, The strongest, `f (9)` (ties list every one: `a, b (3)`);
  - leqWeakest, The weakest, `a (2)`;
  - leqFewest, Fewest others who overcome each, `a: 1 (f); b: 1 (f); c: 1
    (f); d: 1 (f); e: 1 (f); f: 2 (e + d)`;
  - leqBeyond, Beyond every coalition, `0: none`;
  - leqWeakAlone, The weakest alone against the strongest, `no: a, 2, does
    not exceed f, 9`;
  - leqByTwo, Overcome by two or fewer, `6 of 6`.

  Preset `asleep` (the same, machination `5`): leqFewest `…; f: 1 (e)`,
  leqWeakAlone `yes: a, 2 × 5 = 10, exceeds f, 9`. Preset `two-equal`
  (persons `a, 3; b, 3; c, 6`): leqFewest `a: 1 (c); b: 1 (c); c: no
  coalition`, leqBeyond `1: c`, leqByTwo `2 of 3`. Preset `two-equal-match`
  (the same, rule `match`): leqFewest `a: 1 (c); b: 1 (c); c: 2 (a + b)`,
  leqWeakAlone `no: a, 3, falls short of c, 6`. A fractional factor prints
  as a fraction: `11 × 3/2 = 33/2 = 16.50` in the table's force column.

  Status: "The strongest, f, can be overcome by 2 others (e + d); 6 of 6 can
  be overcome by two or fewer; the weakest alone does not exceed the
  strongest; the figure follows …". Table: person, strength, fewest others,
  coalition, their force.

  **Coalition selection rule** (the rules sentence): "A coalition's force is
  the sum of its members' strengths times the factor (secret machination, or
  the victim asleep; 1 for none). It overcomes a person when its force
  exceeds his strength (rule exceed) or at least equals it (rule match). For
  each person, the others are taken from the strongest down, ties in input
  order, until their force overcomes him; that is the fewest who can, and
  the coalition shown. A person whom all the others together cannot overcome
  is beyond every coalition. The strongest is the first of the greatest
  strength in input order, the weakest the first of the least strength other
  than him; the weakest alone has the factor too." Taking the strongest
  first gives the true least number. No refusals beyond the fields.

### covenant (`lcv`)

- **perform.** Whether the second party does better to keep, and whether to
  perform first. Fields:
  - `first` (name, `first`), "The party who performs first";
  - `second` (name, `second`), "The party trusted to perform after";
  - `cost1`, `gain1`, `cost2`, `gain2` (rationals ≥ 0, —): what the first
    gives up by performing, what the first gets when the second performs,
    what the second gives up by performing, what the second gets from the
    first;
  - `sanction` (rational ≥ 0, `0`), "Sanction on the second's breach (0 for
    none)";
  - `certainty` (rational 0–1, `1`), "Certainty the sanction is applied (0 to
    1)";
  - `tie` (select `keep` or `break`, `keep`), "When keeping and breaking pay
    the same, the second".

  Preset `mere-nature` (first `buyer`, second `seller`, cost1 `10`, gain1
  `14`, cost2 `8`, gain2 `10`, no sanction):
  - lcvCondition, Condition, `mere nature: no sanction`;
  - lcvKeep, Second's payoff if it keeps, `2`;
  - lcvBreak, Second's payoff if it breaks, `10`;
  - lcvExpected, Expected sanction, `0`;
  - lcvChoice, What the second does, `seller breaks: 10 against 2`;
  - lcvFirst, First's payoff from performing first, `−10, since seller
    breaks`;
  - lcvReasonable, Is performing first reasonable?, `no: −10 against 0 for
    not performing`;
  - lcvLeast, Least sanction that makes keeping at least as good, `8 (cost2
    ÷ certainty)`.

  Preset `sword` (the same, sanction `12`, certainty `3/4`): lcvCondition `a
  common power: sanction 12 at certainty 3/4 = 75%`, lcvBreak `1`,
  lcvExpected `9`, lcvChoice `seller keeps: 2 against 1`, lcvFirst `4, since
  seller keeps`, lcvReasonable `yes: 4 against 0 for not performing`,
  lcvLeast `32/3 ≈ 10.67 (cost2 ÷ certainty)`. Preset `exact` (sanction `8`):
  lcvChoice `seller keeps: 2 against 2 (equal; the tie rule keeps)`; with
  tie `break`, `seller breaks: 2 against 2 (equal; the tie rule breaks)`.
  Preset `never` (sanction `12`, certainty `0`): lcvCondition `a sanction
  never applied (certainty 0)`, lcvLeast `none: at certainty 0 no sanction
  is ever applied`. With cost2 `0`: lcvLeast `0: keeping costs seller
  nothing`. A first payoff of exactly 0: lcvReasonable `no better: 0 against
  0 for not performing`.

  Status, mere nature: "In the condition of mere nature (no sanction), seller
  does better to break, so buyer performing first gets −10; performing first
  is not reasonable; the figure follows …"; with a sanction: "Under a
  sanction of 12 applied with certainty 3/4 = 75%, seller does better to
  keep, so buyer performing first gets 4; performing first is reasonable;
  …". Table: who, does, payoff, note (`chosen` / `what follows`).

  **Tie rule** and the rest (the rules sentence): "The first performs first.
  The second then keeps, getting gain2 − cost2, or breaks, getting gain2 −
  certainty × sanction (the expected sanction). The second keeps when keeping
  pays more, and when the two are equal it does as the tie rule says (keep by
  default). The first gets gain1 − cost1 if the second keeps and −cost1 if it
  breaks; not performing gets 0, and performing first is reasonable only when
  it gets more than 0. The least sanction that makes keeping at least as good
  is cost2 ÷ certainty; there is none at certainty 0 (unless keeping costs
  nothing). With no sanction this is the condition of mere nature." Under
  `tie: break` the least sanction printed is still the one at which keeping
  is as good; keeping is chosen only above it.

  Refuses: `The two parties are both named buyer; name them apart`.

- **fool.** The Fool's calculation. Fields:
  - `gain` (rational ≥ 0, —), "What breaking now gains";
  - `loss` (rational > 0, —), "What being cast out of the confederacy costs";
  - `chances` (list of 1–8 rationals 0–1, —), "Chances of being found out and
    cast out (0 to 1, up to 8)".

  Preset `four-chances` (gain `3`, loss `12`, chances `1/10 1/4 1/2 0.9`):
  - lcvThreshold, Threshold chance (gain ÷ loss), `1/4 = 25%`;
  - lcvValues, Expected value of breaking at each chance, `1/10 = 10%: 9/5 =
    1.80; 1/4 = 25%: 0; 1/2 = 50%: −3; 9/10 = 90%: −39/5 = −7.80`;
  - lcvBreakAt, Chances at which breaking pays, `1: 1/10 = 10%`;
  - lcvKeepAt, Chances at which keeping pays, `2: 1/2 = 50%; 9/10 = 90%`.

  Preset `above` (gain `5`, loss `4`, chances `0.5 1`): lcvThreshold `5/4 =
  125%, above certainty: breaking pays at every chance`, lcvKeepAt `0: none`.
  A chance exactly at the threshold is in neither list.

  Status: "Breaking pays the Fool when the chance of being cast out is below
  gain ÷ loss = 1/4 = 25%; it does at 1 of the 4 chances given; Hobbes’s
  reply is that no one can reasonably count on the errors of others, which
  this calculation assumes; the figure follows …". Table: chance, expected
  value of breaking, keeping (0), the calculation favours (`breaking`,
  `keeping`, `neither (equal)`).

  Rules: "Breaking gains the gain now and, with the chance given, costs the
  loss of being cast out: its expected value is gain − chance × loss, exact,
  against 0 for keeping. The threshold chance gain ÷ loss is where the two
  are equal; below it the calculation favours breaking, above it keeping,
  and at it neither. Chances are listed in the order given. The calculation
  is the Fool's; Hobbes's reply is that no one can reasonably count on the
  errors of others." Refuses (field): `loss must be more than 0`.

### A worked preset that renders (reckon/names)

```python
"lab": ("levkit", {
    "mode": "reckon", "view": "names",
    "simple": "body animated rational round quadrangle figure incorporeal",
    "defs": "animal, body animated; man, animal rational; circle, figure round",
    "opposed": "round, quadrangle; body, incorporeal",
    "presets": [
        {"id": "men-and-figures", "label": "Men, animals and figures",
         "claims": "c1, man, animal; c2, animal, man; c3, round quadrangle, figure; c5, man, centaur",
         "expect": {"lrkVerdicts": "c1 true; c2 false; c3 absurd; c5 insignificant"}},
    ],
}),
```

The first preset of every other view above, with its observed tiles as
`expect`, rendered and passed `labcheck.js` (sweep included) on a scratch
page.

### Verification (family A)

- `node scripts/mathcheck.js`: family A's block passes (the core helpers and
  every view: verdict precedence, cycles, empty names, tie rules,
  thresholds, every refusal). A mutation run broke 56 lines on purpose (the
  percentage printer, the parser's limits, the name cell, the cycle search
  and its path, every reckon refusal, empty-name propagation, each place of
  absurdity, the missing-part test, the hope/fear reading, alternations, the
  will, the price sum, tie printing, rank agreement, dignity comparison, the
  coalition order, factor and rule, the expected sanction, the tie rule, the
  least sanction, the Fool's value and threshold): 53 made an assertion fail;
  the 3 that did not are equivalent (a guard the inner loop repeats, a loop
  bound that can only add the last step, which always agrees with the will,
  and a tie-break the stable sort already gives).
- Parity: 1,800 fuzzed inputs over the six views through the Python checks
  and the page's JS: the same verdict every time and the same sentence for
  every view refusal (243 view refusals, 542 field refusals); no tile printed
  NaN, undefined or Infinity.
- Six scratch lesson pages (one per view, 18 presets) rendered with
  `scripts/preview_subject.py` from a package outside `content/`:
  `labcheck.js` executed and swept every page, 0 failing, and every pinned
  figure matched; a deliberately wrong pin was reported.
- `tests.test_site_invariants.TestEveryLabBuilds` passes with `levkit`
  registered. No test enumerates `KITS_WITH_EXPECTATIONS`.

## Family B (levkit_b.py)

Five modes, nine views: `assembly` (voices, ties), `succession` (heir), `tax`
(impose, shares), `law` (silence, deter), `canon` (date, benefit). Every
example tile string below was read off a rendered scratch page with
`node scripts/labcheck.js --observe`, and every one was also worked by hand.
Every view prints its rules under the tiles ("How the lab counts."), and every
status line ends "; the figure follows from what the lesson states, on
Hobbes’s definitions as stated." (`lvkStatus`). No view says who is right.

`levkit` is in `KITS_WITH_EXPECTATIONS`: **every preset needs an `expect`**
mapping some of its view's tile ids to the exact text printed. Read them off
your own scratch page with `--observe`; never type them from this report
without checking.

### Deviations from PLAN §D.1 (family B), and readings the kit makes

- **assembly/voices: `liable` is a select input** (`no`/`yes`, default `no`),
  not only a cfg flag, so a reader can switch it. Abstainers are excused with
  those who voted no. "Mute" is decided the same way on both rules: the yes
  and no voices equal (including none at all). On `absolute`, a motion with
  more yes than no but not more than half of all members **fails** (it is not
  mute). An extra tile `lasNeeded` gives the yes voices needed.
- **assembly/ties: a size given twice is refused** (`Sizes: 4 is given
  twice`).
- **succession/heir.** `born` is one birth order across the whole family
  (whole numbers, smaller is elder; a year works): no two people may share
  it, and a child must be born after its parent. People need not have a
  single root; anyone with no ancestor in common with the monarch is "not of
  the blood". **Ancestors count among the blood** (a living father is 1 step,
  so he precedes a brother, 2 steps): PLAN's "fewest steps through the
  nearest common ancestor" read literally; if a lesson does not want that,
  mark ancestors dead or leave them out. After a testament the line continues
  by custom or presumption with the named successor removed. Male-line
  custom: the candidate is male, everyone between him and the nearest common
  ancestor is male, that ancestor is male (unless it is the monarch), and
  everyone between the monarch and that ancestor is male.
- **law/deter: certainty 0 does not refuse the view.** Only the
  least-penalty tile says `none: at certainty 0 ...`; the rest still prints
  (the case "hope of impunity" is the point of Chapter 27). Deterring means
  the expected penalty is **more than** the gain (equal does not), so the
  tile `llwLeast` reads `more than <gain ÷ certainty>`. `penalty` and
  `prescribed` are separate inputs: the price test compares the prescribed
  penalty with the gain.
- **tax/shares: a party may be both set apart a portion and given a share**
  (its portion in the table is the two added). Set-aside fractions add to at
  most 1.
- **canon/date: a mention in the very year of the author's death does not
  rule the author out** ("in the year of ... death"); only a later one does.
- **law/silence: `reason` is words separated by spaces** (the NAMES cell),
  printed joined by spaces; no commas or punctuation other than `. _ -`.

### Conventions (family B)

- **Ids.** Prefixes `las` assembly, `lsu` succession, `ltx` tax, `llw` law,
  `lcn` canon. Inputs are `<prefix>In<Key>` (`lasInMembers`, `lasInRule`,
  `lsuInPeople`, `lsuInCustom`, `ltxInSetaside`, `llwInInalienable`,
  `lcnInMentions`); each page has `<prefix>Preset`, `<prefix>Status`,
  `<prefix>Table`.
- **Names** are one word: letters, digits, `.`, `_`, `-`; a name of several
  words is hyphenated (`accuse-oneself`, `kings-of-edom`). Compared exactly.
- **Records** are `a, b; c, d`. A NAMES cell inside a record holds names
  separated by spaces (`fight pray`), or `-` for none where the field says so.
- **Numbers.** Whole cells (`riches`, `born`, years) are whole numbers;
  rational cells (`revenue`, `total`, `weight`, `fraction`, `gain`,
  `penalty`, `certainty`, `prescribed`, `inflicted`) take a decimal (at most 6
  places) or a fraction `p/q` (`1/10`, `3/4`). Years may be negative.
- **Printing.** Amounts print `eaNum`-style: `10`, `15/2 = 7.50`,
  `80/3 ≈ 26.67`. Chances, rates and shares of a whole print with `lvkPct`:
  `1/4 = 25%`, `2/7 ≈ 28.57%`. **tax/shares never rounds**: `108/7`, and the
  decimal only when exact within six places (`75/2 = 37.5`). Years print
  ungrouped with U+2212 (`−1050`). Minus is U+2212 everywhere.
- **Order.** Members, sizes, persons, parties, actions, books go in the order
  given; every tie rule is in the view's rules sentence.

### assembly (`las`)

- **voices.** Fields: `members` (records `member, voice`, voice `yes`/`no`/
  `abstain`, 1–60, unique; `lasInMembers`), `rule` (select `greater`/
  `absolute`, default `greater`; `lasInRule`), `liable` (select `no`/`yes`,
  default `no`; `lasInLiable`). Example `ann, yes; ben, yes; cal, no; dee,
  abstain; eve, yes; fay, no; gil, abstain`, liable `yes`:
  - `lasYes` Yes `3`; `lasNo` No `2`; `lasAbstain` Abstain `2`
  - `lasDecision` The decision: `passes: 3 to 2 by the greater number of voices given`
    (rule `absolute`: `fails: 3 of 7 members say yes, not more than half`;
    six members three to three: `mute: 3 to 3, an even split of the voices`;
    all abstain: `mute: no voice is given (every member abstains)`)
  - `lasMargin` Margin (yes less no): `+1` (`0`, `−1`)
  - `lasNeeded` Yes voices needed to pass: `3 yes voices (more than the 2 no)`
    (absolute: `4 yes voices (more than half of 7 members)`)
  - `lasLiable` Answerable for the decree: `3: ann, ben, eve`
    (`none: no decree was made`; liable `no`: `not shown (liable is no)`)
  - `lasExcused` Excused: `4: cal, dee, fay, gil` (`everyone: no decree was made`)
  Table: member, voice (and "answerable"/"excused"). No refusals beyond the
  parser. Rules: "Each member gives one voice: yes, no or abstain. On the
  rule greater, the motion passes when the yes voices are more than the no
  voices given; on the rule absolute, when the yes voices are more than half
  of all the members, abstainers counted. On either rule, when the yes and no
  voices are equal (none at all included) the assembly is mute and nothing
  is decreed (Chapter 16). With answerable shown, a decree that passes binds as
  its authors only the members who voted yes; those who voted no or abstained
  are excused (Chapter 22). Members go in the order given."
- **ties.** Field `sizes` (list of whole numbers 1–60, up to 8, no repeats;
  `lasInSizes`). Example `2 3 4 5 6 7`:
  - `lasChances` Chance of an even split, for each size: `2: 1/2 = 50%; 3: 0 = 0%; 4: 3/8 = 37.5%; 5: 0 = 0%; 6: 5/16 = 31.25%; 7: 0 = 0%`
  - `lasOdd` Odd sizes: never mute: `3: 3, 5, 7`
  - `lasMost` The even size most often mute: `2 members: 1/2 = 50%`
  - `lasLeast` The even size least often mute: `6 members: 5/16 = 31.25%`
    (`10 20 21 60`: `60 members: 7,391,536,347,803,839/72,057,594,037,927,936 ≈ 10.26%`;
    all odd: `none: every size given is odd`)
  Table: size, C(n, n/2), 2^n, chance. Rules: "The model is stated, not
  Hobbes's: each member says yes or no with equal chance, independently of
  the others, and no one abstains. Of the 2^n ways n members can vote,
  C(n, n/2) split evenly, so the chance of a mute assembly is C(n, n/2) ÷
  2^n, exact, and 0 for an odd n. ..." Refusal: a repeated size.

### succession (`lsu`)

- **heir.** Fields: `people` (records `person, parent, sex, born, alive`;
  parent a person or `-`, sex `m`/`f`, born a whole number, alive `yes`/`no`;
  2–20, unique; `lsuInPeople`), `monarch` (a person; `lsuInMonarch`),
  `named` (a person or `-`, default `-`; `lsuInNamed`), `custom` (select
  `none`/`male-line`, default `none`; `lsuInCustom`). State `people` and
  `monarch` once at cfg level. Worked example, people `king, -, m, 1, no;
  henry, king, m, 2, yes; arthur, henry, m, 3, no; margaret, henry, f, 4,
  yes; harry, henry, m, 5, yes; mary, henry, f, 6, yes; catherine, arthur, f,
  7, yes; james, margaret, m, 8, yes; edward, harry, m, 9, yes; uncle, king,
  m, 10, yes`, monarch `henry`:
  - `lsuSuccessor` The successor: `catherine` (named `mary`: `mary`; custom
    `male-line`: `harry`; monarch `edward`: `harry`)
  - `lsuRule` By what right: `presumption: the monarch's own issue`
    (`testament: named by express words`; `custom (male-line): the first male
    of the blood through males`; `presumption: no living issue, so the
    nearest in blood`; `none: no living person of the blood qualifies`)
  - `lsuLine` The line of succession (first 6): `1 catherine; 2 harry; 3 edward; 4 margaret; 5 james; 6 mary; and 1 more (the table lists all)`
    (male-line: `1 harry; 2 edward; 3 uncle`; monarch `edward`: `1 harry; 2
    henry; 3 margaret; 4 mary; 5 james; 6 uncle; and 1 more (the table lists all)`)
  - `lsuWithout` Without the testament: `catherine (there is no testament)`
    (named `mary`: `catherine`)
  - `lsuPresumption` By presumption alone: `catherine`
  - `lsuIssue` The monarch's living issue: `6: catherine, harry, edward, margaret, james, mary`
  - `lsuNear` The successor's nearness in blood: `catherine: issue, 2 generations down`
    (`harry: 1 step up (an ancestor)`; `henry: 3 steps through king` shape for collaterals)
  "What changes when the eldest son dies": set his `alive` to `no`; his issue
  then stand in his place (here catherine), and with none the next son
  succeeds. Table: the line in order, then everyone passed over with the
  reason (`dead`, `not of the blood`, `not of the male line: female` /
  `through a female (margaret)`). Refusals, in this order: `People, record 1
  (a) is named as their own parent`; `People, record 1 (a): the parent z is
  not one of the people`; `People: a, b, c are one another's ancestors in a
  loop`; `People, record 2 (b) is born 1, as a is: born gives the order of
  birth, so no two people share it`; `People, record 2 (b) is born 3, not
  after the parent a (born 5)`; `The monarch, zed, is not one of the people`;
  `The successor named, zed, is not one of the people`; `The successor named,
  henry, is the monarch`; `The successor named, arthur, is dead (alive is
  no), and the dead cannot succeed`. Rules (in full on the page): a successor
  named by express words or testament first, then custom, then the
  presumption; "The kit reads the presumption so, which is its reading and
  not Hobbes's words: the monarch's own issue before all others; among the
  issue each child in turn, male before female and then elder before
  younger, followed by that child's own issue in the same order, so that a
  dead child's issue stand in its place before the next child; with no
  living issue, the nearer in blood before the remoter, counting the steps up
  from the monarch to the nearest common ancestor and down from it to the
  person (a parent is 1, a brother 2, a nephew 3), and among the equally
  near, male before female and elder before younger." The status repeats
  that the order is the kit's reading of Chapter 19.

### tax (`ltx`)

- **impose.** Fields: `persons` (records `person, riches, consumption`, whole
  amounts, unique; `ltxInPersons`), `revenue` (rational > 0;
  `ltxInRevenue`). Example `ann, 100, 10; ben, 50, 20; cal, 10, 30; dee, 20,
  5; eve, 20, 15`, revenue `20`:
  - `ltxRateRiches` Rate on riches: `1/10 = 10%`
  - `ltxRateConsumption` Rate on consumption: `1/4 = 25%`
  - `ltxOnRiches` Each person's tax on riches: `ann 10; ben 5; cal 1; dee 2; eve 2`
  - `ltxOnConsumption` Each person's tax on consumption: `ann 5/2 = 2.50; ben 5; cal 15/2 = 7.50; dee 5/4 = 1.25; eve 15/4 = 3.75`
  - `ltxDifference` Difference (on consumption less on riches): `ann −15/2 = −7.50; ben 0; cal +13/2 = 6.50; dee −3/4 = −0.75; eve +7/4 = 1.75`
  - `ltxMore` Who pays more on consumption: `2: cal, eve`
  - `ltxBurdenRiches` Tax on riches, as a share of what each consumes: `ann 1 = 100%; ben 1/4 = 25%; cal 1/30 ≈ 3.33%; dee 2/5 = 40%; eve 2/15 ≈ 13.33%`
  - `ltxBurdenConsumption` Tax on consumption, as a share of what each consumes: `ann 1/4 = 25%; ...` (every one equal)
  A person consuming 0 shows `no consumption` in the two share tiles.
  Refusals: `Persons: every person's riches are 0, so no rate on riches can
  raise the revenue` (and the same for consumption).
- **shares.** Fields: `total` (rational > 0; `ltxInTotal`), `parties`
  (records `party, weight`, weight rational > 0; `ltxInParties`),
  `setaside` (records `party, fraction`, 0 < fraction ≤ 1, may be empty,
  default empty; `ltxInSetaside`). Example total `120`, parties `reuben, 1;
  simeon, 2; gad, 4`, setaside `levi, 1/10`:
  - `ltxSetAside` Set apart first: `levi 1/10 = 0.1 of the total: 12` (`none set apart`)
  - `ltxRemainder` The remainder: `108`
  - `ltxWeight` Weights in all: `7`
  - `ltxShares` Each party's share of the remainder: `reuben 108/7; simeon 216/7; gad 432/7`
    (weights `1; 2; 3`: `reuben 18; simeon 36; gad 54`)
  - `ltxNotWhole` Shares that are not whole: `3: reuben, simeon, gad`
  - `ltxSum` Every portion added up: `120, the whole total`
  Refusal: `Set apart: the fractions add to 7/6, more than the whole`.

### law (`llw`)

- **silence.** Fields: `actions` (list of names, up to 12; `llwInActions`),
  `laws` (records `law, commands, forbids`, each a NAMES cell or `-`;
  `llwInLaws`), `inalienable` (records `action, reason`, the reason words
  separated by spaces, may be empty; `llwInInalienable`). Example actions
  `steal kill fight pray trade marry accuse-oneself`, laws `l1, fight pray,
  steal kill; l2, -, pray; l3, trade, -`:
  - `llwCommanded` Commanded: `3: fight, pray, trade`
  - `llwForbidden` Forbidden: `3: steal, kill, pray`
  - `llwFree` Free, in the silence of the law: `2: marry, accuse-oneself`
  - `llwBoth` Both commanded and forbidden (a contradiction): `1: pray (commanded by l1, forbidden by l2)` (`0: none`)
  - `llwRefusable` Commands a subject may still refuse: `no inalienable liberty is stated`;
    with laws `l1, fight pray, steal kill; l2, accuse-oneself, -; l3, trade, -`
    and inalienable `accuse-oneself, no man is bound to accuse himself; fight,
    natural timorousness`: `2: fight (natural timorousness), accuse-oneself (no man is bound to accuse himself)`
  - `llwShareFree` Share of actions left free: `2 of 7: 2/7 ≈ 28.57%`
  An inalienable liberty of an action no law commands is shown only in the
  table. Refusals: `Laws, record 1 (l1): it commands fly, which is not one of
  the actions` (and `it forbids`), `Inalienable, record 1: fly is not one of
  the actions`.
- **deter.** Fields: `gain`, `penalty` (rationals ≥ 0), `certainty`
  (rational 0–1, `1/2` or `0.5`), `prescribed`, `inflicted` (rationals ≥ 0
  or `-`, default `-`); ids `llwInGain` … `llwInInflicted`. Example gain
  `20`, penalty `40`, certainty `3/4`, prescribed `10`, inflicted `40`:
  - `llwExpected` Expected penalty: `30`
  - `llwNet` Gain less expected penalty: `−10` (penalty 30 at 1/2: `+5`)
  - `llwDeters` Does the expected penalty exceed the gain?: `yes: 30 is more than the gain 20`
    (`no: 15 is less than the gain 20`; `no: 15 equals the gain, and does not exceed it`)
  - `llwLeast` Penalty it must exceed to deter at this certainty: `more than 80/3 ≈ 26.67`
    (certainty 0: `none: at certainty 0 the penalty is never inflicted, so no penalty deters`)
  - `llwHostility` Inflicted beyond the prescribed: hostility?: `yes: the excess, 30, is not punishment but an act of hostility`
    (`no: the inflicted 15 is within the prescribed 15`; `needs both the prescribed and the inflicted penalty`)
  - `llwPrice` Prescribed below the gain: a price, not a punishment?: `yes: the prescribed 10 is less than the gain 20, rather the price of the crime than a punishment`
    (`no prescribed penalty is given`)
  No table, no refusals beyond the parser. The status says the hope of
  impunity makes the crime pay only when the certainty is below 1; at
  certainty 1 with a penalty not above the gain it says the penalty is
  "rather the price of the crime".

### canon (`lcn`)

- **date.** Fields: `books` (records `book, author, author_death`, the year
  whole and possibly negative, unique, up to 30; `lcnInBooks`), `mentions`
  (records `book, event, year`, may be empty; `lcnInMentions`). Example
  books `first, aaron, 40; second, bezalel, 90; third, caleb, 150`, mentions
  `first, well-dug, 30; first, kings-reign, 120; second, city-built, 90;
  second, flood, -20`:
  - `lcnLatest` The latest thing each book mentions: `first: kings-reign (120); second: city-built (90); third: no test`
    (ties: `gen: edom and y (−1050)`)
  - `lcnAfter` Written after the author's death: `1: first`
  - `lcnGap` Latest mention against the author's death: `first 80 years after aaron's death; second in the year of bezalel's death; third no test`
    (`gen 1 year before moses's death`)
  - `lcnPossible` Not ruled out by this test: `1: second`
  - `lcnNoTest` No mention, no test: `1: third`
  Refusal: `Mentions, record 1: the book b is not one of the books`. State the
  year scale in the lesson (e.g. years from the Exodus).
- **benefit.** Fields: `parties` (list of names, up to 20; `lcnInParties`),
  `doctrines` (records `doctrine, benefits`, a NAMES cell or `-`;
  `lcnInDoctrines`). Example parties `pope clergy king people`, doctrines
  `purgatory, pope clergy; infallibility, pope; celibacy, clergy pope;
  tithes, clergy; obedience, -`:
  - `lcnCounts` Doctrines benefiting each party: `pope 3; clergy 3; king 0; people 0`
  - `lcnMost` The party served by the most: `pope and clergy, 3 of 5 doctrines each (a tie)`
    (`pope, 2 of 2 doctrines`; `none: no doctrine benefits any party`)
  - `lcnNoOne` Doctrines that benefit no one named: `1: obedience`
  - `lcnUnserved` Parties served by none: `2: king, people`
  Refusal: `Doctrines, record 1 (d1): r is not one of the parties`.

### A sample preset (succession/heir)

```python
"lab": ("levkit", {
    "mode": "succession", "view": "heir",
    "people": "king, -, m, 1, no; henry, king, m, 2, yes; arthur, henry, m, 3, no; "
              "margaret, henry, f, 4, yes; harry, henry, m, 5, yes; mary, henry, f, 6, yes; "
              "catherine, arthur, f, 7, yes; james, margaret, m, 8, yes; edward, harry, m, 9, yes; "
              "uncle, king, m, 10, yes",
    "monarch": "henry",
    "presets": [
        {"id": "presume", "label": "No testament: by presumption",
         "expect": {"lsuSuccessor": "catherine", "lsuRule": "presumption: the monarch's own issue"}},
        {"id": "testament", "label": "Mary named by testament", "named": "mary",
         "expect": {"lsuSuccessor": "mary", "lsuWithout": "catherine"}},
        {"id": "male", "label": "A male-line custom", "custom": "male-line",
         "expect": {"lsuLine": "1 harry; 2 edward; 3 uncle"}},
    ],
}),
```

The names here are the kit's test family, not the book's; a lesson uses its
own.

### Family B: verification

- `scripts/mathcheck.js`, block `// ---- levkit (Leviathan), family B ----`
  (directly after family A's): 70 assertions over all nine views, every
  refusal and every boundary (exactly half of all members, an even split on
  both rules, all abstaining, equal expected penalty and gain, inflicted
  equal to prescribed, prescribed equal to gain, a mention in the year of the
  death, set-asides of exactly the whole, C(60, 30)/2^60 exact).
- **Mutation testing.** 48 single breaks of the JS (C(n, k), 2^n, odd/even,
  most/least direction, mute, both rules' thresholds, liability, male before
  female, elder before younger, representation of a dead child, steps,
  nearness ordering, both halves of the male-line rule, testament first,
  every refusal, both rates, burden, set-aside bound, remainder, shares,
  exact printing, contradiction, free, refusable, deterrence's strictness,
  gain ÷ certainty, hostility, price, latest year, strictness of "after",
  most, no one, unknown names): 46 fail the block; the other two are
  unreachable (a tie is caught as mute before the greater rule; a child born
  in its parent's year is caught as a shared birth order).
- **Parity.** 880 inputs (20 targeted refusals plus random mutations of
  every view's presets) through the Python checks and the page's JS on the
  real field specs: same verdict and same refusal sentence every time; no
  tile printed NaN, undefined or Infinity.
- Nine scratch lesson pages (one per view, 21 presets) rendered outside the
  repository: `labcheck.js` executes and sweeps all nine, `--expect` matches
  every pinned tile, and a deliberately wrong pin is reported.
