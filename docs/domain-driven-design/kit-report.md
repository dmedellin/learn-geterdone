# dddkit (Domain-Driven Design, Read Along): kit report

Lesson authors configure a lab from this report alone. It records the kit as
built to `docs/domain-driven-design/PLAN.md` §0 and §D. Family A (lang,
assoc, identity, aggregate, spec) is `dddkit.py` and is reported here first;
family B's section (modules, context, distill, ledger) follows at the end.
The seam between the two modules is `docs/domain-driven-design/kit-contract.md`.
Every example tile string in family A's section was read off a rendered
scratch page with `node scripts/labcheck.js --observe`; none was copied from
the code. "Deviations from PLAN §D (family A)" says where family A differs
from §D and why.

**Change, 2026-11-01:** spec/subsume's tile labels now state the relation in
plain words ("every one B accepts, A accepts too") instead of "A subsumes
B", because Evans uses "subsumes" the other way round from the logicians
(see "Which way subsumes runs" under spec). **Tile ids are unchanged.** One
tile string changed: the vacuous logical answer now reads `yes, vacuously: B
can select nothing (no value of pages meets all its clauses)`. The field
`spec` is labelled "Specification A" (was "Specification A (the more
general)").

## Files

- `scripts/mathpath/labs/dddkit.py`: the entry point `dddkit_lab(cfg)`,
  `mode_lab(cfg, mode, spec)` (shared with family B), `DDD_CORE_JS` (shipped
  on every dddkit page: `dddStatus`, `dddRead`, `dddValue`, `dddValText`,
  `dddValEq`, `dddKey`, `dddDec`, `dddQ`, `dddListed`), dddkit's two field
  kinds (`vrec`, `expr`) and their Python mirror, a thin copy of
  `eakit_core.build_lab` that reads them, and family A's five modes: a base
  block (`DLN_JS`, `DAS_JS`, `DID_JS`, `DGR_JS`, `DSP_JS`) and one block per
  view (`DLN_VIEW_JS["glossary"]`, …), with the Python `check` of every view
  and `parse_spec`, the mirror of the specification parser. It imports
  `dddkit_b` with a plain import at its end and dispatches family B's modes
  through `dddkit_b.MODES`.
- `scripts/mathpath/labs/eakit_core.py`: used unchanged (imported as `ea`).
- `scripts/mathpath/labs/__init__.py`: one import (`dddkit,`) and one
  registry line (`"dddkit": dddkit.dddkit_lab,`).
- `scripts/build_paths.py`: `"dddkit"` added to `KITS_WITH_EXPECTATIONS`.
  No published page uses the kit yet; once lessons do, every dddkit preset
  menu must pin at least one tile on every option.
- `scripts/mathcheck.js`: the block `// ---- dddkit (Domain-Driven Design),
  family A ----` … `// ---- end dddkit family A ----`, before THE VERDICT and
  before family B's block: 51 assertions, one vm context per mode.

## Conventions (both families)

**Entry point and cfg.** A lesson's lab is `("dddkit", cfg)`, with
`cfg["mode"]` (lang, assoc, identity, aggregate, spec, or one of family B's:
modules, context, distill, ledger) and `cfg["view"]` (default: the mode's
first view, listed first below). An unknown mode or view raises, listing the
valid ones. Keys common to every view: `mode`, `view`, `presets` (required,
non-empty), `preset` (the one shown first; default the first), `title`,
`panel_title`, `panel_intro`. A cfg key named like one of the view's inputs
supplies it to every preset that does not set it (a spec lesson states its
`candidates` once and varies the specification per preset). Any other key
raises, naming the keys the view takes. Family A has no lesson-level keys
beyond these.

**Panel intro.** Every dddkit panel intro begins "A count over the small model
the lesson states." and by default continues "The lab counts one consequence
of one modelling choice; the choice itself is weighed in the book, against
the domain, the team and the project." (PLAN §D). A `panel_intro` in the cfg
replaces all but the first sentence, which is put back in front if missing.

**The caution.** Every status line, in every view of both families, ends
"; the count is of the model stated." (`dddStatus`). Under the tiles each
view prints "How the lab counts." with its rules sentence: what is counted,
and how ties and orders go. The rules are quoted per view below.

**Presets.** Each preset is `{"id": "lower-case-hyphens", "label": "plain
text", <inputs>..., "expect": {tile_id: "exact text"}}`. A label names the
instance; every outcome goes in `expect` (scripts/mathpath/AGENTS.md, "a
preset's two claims"). Every preset must pin at least one tile, because
dddkit is in `KITS_WITH_EXPECTATIONS`. Read the strings off the built page
with `node scripts/labcheck.js --observe <page>` (or `preview_subject.py`'s
pages), never out of the code. A preset the page would refuse fails the
build, naming the preset and the reason. **Instances are the lesson's own,
never the book's** (no cargo, voyages, PCB nets, syndicated loans, purchase
orders with approval limits, paint, payroll; PLAN §C): a library, clinic,
bakery, bike-share, theatre, seed bank, school timetable.

**Ids.** Family A: `dln` lang, `das` assoc, `did` identity, **`dgr`
aggregate** (PLAN's `dag` is used by other kits: `dagRelax`,
`dagSchedule`), `dsp` spec. Family B: `dmo`, `dcx`, `dds`, `dle`. Shared
helpers `ddd`/`DDD_`. An input's id is `<prefix>In<Key>`, the key's first
letter capitalised (`dlnInTerms`, `dgrInDelete`, `dspInOther`). Each page
has `<prefix>Preset` (the worked-example menu, which is the menu `expect`
pins), `<prefix>Status` and `<prefix>Table`. Every prefix was grepped across
`scripts/mathpath/labs/*.py` and `scripts/*.js` before use.

**Input formats.** eakit_core's parser, unchanged, for:
- a name: letters, digits, `.`, `_`, `-` (`loan1`, `P-100`, `book_loan`);
  "name or `-`" fields take `-` for none;
- a number: a decimal with at most 6 places, `3`, `0.25`, `-1.5`;
  fractions such as `1/3` and exponents are refused;
- a whole number: `12` (no commas, no decimals);
- a list (audiences): names separated by spaces or commas,
  `experts developers code`;
- records: fields by commas, records by semicolons,
  `loan1, loan, yes; line1, loan, no`; in a preset a string or a Python list
  of lists;
- a choice: one of the listed words, exactly (`mutable`, `n-n`, `a-b`).

and dddkit's own two kinds (kit-contract.md §4):
- **records with a tail** (`vrec`): the fixed cells, then a variable number
  of cells. In lang/glossary the tail is one name per audience
  (`loan, loan, checkout, Loan`); in identity/equality and spec the tail is
  `attribute=value` cells: `b1, pages=320, genre=crime`. An attribute name is
  a word beginning with a letter; a value is a number (as above, at most
  10,000,000 in size) or a word beginning with a letter (`crime`, `B1`,
  `rye-sour`); an attribute may appear once per record. `3.` and `-` are
  neither and are refused.
- **a specification** (`expr`): one expression of at most 300 characters,
  20 clauses and 8 levels of parentheses, read by the kit's own lexer and
  parser; nothing typed is evaluated. Its box is empty in the page's markup
  and filled by script from the preset (it may hold `<` and `>`).
- A wrong value paints one red sentence in the banner and blanks every tile
  and the table: "Candidates (name, then attribute=value cells), record 2:
  attribute 1: "pages" should be name=value, such as pages=320 or
  genre=crime, the name beginning with a letter."

**Comparing names.** lang compares terms, names and meanings ignoring letter
case (Loan = loan) and nothing else (`loan_record` ≠ `loan`), and prints the
first spelling met. Everywhere else names, ids and word values compare
exactly, letter case counted.

**Number and list format.**
- Counts grouped `1,024`; a list tile is `n: a, b` or `0: none`; a list of
  structured entries separates them with `; `
  (`2: bike (rental: vehicle, maintenance: frame); trip (…)`).
- Attribute values and lock values print as typed decimals, ungrouped,
  minus U+2212: `412`, `4`, `−3.5`, `106`.
- Pairs print `(x, y)`, references `from → to`, associations `a–b`, and a
  difference after − before is signed: `−4`, `0`, `+1`.

**Exactness.** Every figure is a count, a list, or an exact BigInt rational
(lock's sums, spec's comparisons: `4 = 4.0`, `320 <= 320` holds). Nothing is
approximated.

**Refusals.** Beyond the field rules above, each view's Python `check`
mirrors every refusal its JS makes, with the same sentence, so a preset the
page would refuse fails the build. A parity run of 68 targeted inputs over
family A (both sides of every limit and every refusal below) gave the same
verdict and the same sentence on both sides.

**Page weight.** A page ships RATIONAL_JS, EA_CORE_JS, DDD_CORE_JS, the
wiring, its mode's base block and its own view's block, nothing more.
Family A's lab is 7.0 to 9.9 KB gzipped (spec/subsume the heaviest); a
scratch lesson page (an Introduction to Algorithms lesson's prose with each
lab) is 34.2 to 37.4 KB gzipped, 129 to 140 KB raw.

## Family A (dddkit.py): modes, views, fields, tiles

Each field is listed as `key` (kind, default), with its input id and label;
— means required. Tiles are listed as id, label, then the value observed on
the sample preset named. Below each mode: the rules sentence (printed on the
page), what it refuses, and behaviour the tiles do not show.

### lang (`dln`)

- **glossary.** One concept, several audiences, how many names. Fields:
  - `audiences` (list of 2–4 names, default `experts developers code`), id `dlnInAudiences`, labelled "Audiences (2 to 4 names, in order)";
  - `terms` (records of concept (name), then 1–4 name cells (name or `-`); 1–60, —), id `dlnInTerms`, labelled "Terms (concept, then one name per audience; - for none)";

  Tiles, with their values on the sample preset `library` (audiences="experts developers code", terms="loan, loan, checkout, Loan; member, member, member, Member; copy, copy, item, Item; hold, hold, reservation, -; fine, fine, item, Fine"):
  - dlnConcepts, Concepts, `5`;
  - dlnAlike, Named alike by every audience, `1: member`;
  - dlnTranslations, Translations a conversation needs, `7`;
  - dlnMissing, Names missing (concept, audience), `1: hold (code)`;
  - dlnAmbiguous, Ambiguous names (one name, two or more concepts), `1: item (developers: copy, fine)`;

  Status: "5 concepts across 3 audiences: a conversation that touches each concept once needs 7 translations, 1 name is missing and 1 name stands for more than one concept; the count is of the model stated."

  Rules: "Each record names one concept and then gives one name for it per
  audience, in the order of the audiences; - means that audience has no name
  for it. Names compare ignoring letter case and nothing else (Loan = loan;
  loan_record ≠ loan). A translation is one pair of audiences whose names for
  one concept differ, counted once per pair and per concept; a pair where
  either name is missing is not a translation but a name missing. A concept
  is named alike when every audience names it and all the names agree. A
  name is ambiguous when one audience uses it for two or more concepts.
  Lists follow the order of the records and of the audiences."

  Refuses: a record whose number of names is not the number of audiences
  ("Terms, record 1 (loan) gives 2 names; there are 3 audiences (experts,
  developers, code), so each record needs 3 names, - where an audience has
  none"); a concept named twice; fewer than 2 or more than 4 audiences.
  `audiences` defaults to `experts developers code`; a cfg or preset may set
  it (`"audiences": "clinicians developers"`). With k audiences a concept
  needs at most k(k − 1)/2 translations (4 names all different: 6).
  The table shows each concept per audience (— for missing) and the pairs
  whose names differ (`experts↔developers, developers↔code`).

  Further figures: `the same library, one language` (every name the same, up
  to case) gives dlnTranslations `0`, dlnAlike `5: loan, member, copy, hold,
  fine`; a clinic with two audiences (`appointment, appointment, booking;
  patient, patient, user; visit, visit, booking`) gives `3` and dlnAmbiguous
  `1: booking (developers: appointment, visit)`.

- **cognates.** The same word in different bounded contexts. Fields:
  - `contexts` (records of context (name), term (name), meaning (name); 2–60, —), id `dlnInContexts`, labelled "Terms by context (context, term, meaning)";

  Tiles, with their values on the sample preset `bike-share` (contexts="rental, bike, vehicle; rental, dock, station; rental, trip, ride; maintenance, bike, frame; maintenance, dock, station; maintenance, job, repair; billing, trip, charge; billing, rider, customer; billing, journey, ride"):
  - dlnContexts, Contexts, `3: rental, maintenance, billing`;
  - dlnTerms, Terms, `6`;
  - dlnShared, Shared terms (in two or more contexts), `3: bike, dock, trip`;
  - dlnFalse, False cognates (one term, different meanings), `2: bike (rental: vehicle, maintenance: frame); trip (rental: ride, billing: charge)`;
  - dlnDuplicate, Duplicate concepts (one meaning, different terms), `1: ride: trip (rental), journey (billing)`;
  - dlnSafe, Terms safe to share, `1: dock`;

  Status: "6 terms in 3 contexts: 3 shared, of which 2 are false cognates and 1 safe to share; 1 concept carries more than one term; the count is of the model stated."

  Rules: "Each record says what one term means in one context, the meaning a
  short name of the concept. Terms and meanings compare ignoring letter case.
  A shared term appears in two or more contexts; it is a false cognate when
  its meanings there are not all the same, and safe to share when they are
  (a term in one context is neither). A duplicate concept is one meaning
  carried by two or more different terms, in any contexts. A context may give
  a term once. Lists follow the order in which contexts, terms and meanings
  first appear."

  Refuses: a context giving the same term twice ("Terms by context, record
  2: a gives the term t twice; give each term one meaning in each context");
  records all in one context. The table shows each term's meaning in each
  context and its verdict (`false cognate`, `safe to share`, `in one
  context`). A duplicate concept may sit in one context (two terms for one
  meaning there) or across several.

### assoc (`das`)

- **simplify.** A direction, a qualifier, a dropped association. Fields:
  - `assocs` (records of a (name), b (name), ends (choice: `1-1`, `1-n`, `n-1`, `n-n`), direction (choice: `both`, `a-b`, `b-a`), qualified (choice: `yes`, `no`); 1–60, —), id `dasInAssocs`, labelled "Associations before (a, b, ends, direction, qualified)";
  - `after` (records of a (name), b (name), ends (choice: `1-1`, `1-n`, `n-1`, `n-n`), direction (choice: `both`, `a-b`, `b-a`), qualified (choice: `yes`, `no`); 0–60, default empty), id `dasInAfter`, labelled "Associations after (same shape; empty for none)";

  Tiles, with their values on the sample preset `library` (assocs="member, loan, 1-n, both, no; book, author, n-n, both, no; branch, copy, 1-n, both, no; loan, copy, n-1, both, no", after="member, loan, 1-n, a-b, no; book, author, n-n, a-b, no; branch, copy, 1-n, a-b, yes; loan, copy, n-1, a-b, no"):
  - dasAssocs, Associations, `4 → 4`;
  - dasDirections, Navigable directions, `8 → 4`;
  - dasTwoWay, Two-way (two references to keep in step per link), `4 → 0`;
  - dasManyMany, Many-to-many, `1 → 1`;
  - dasManyEnds, Many ends, `5 → 4`;
  - dasChange, The change, after − before, `0 associations, −4 navigable directions, −4 two-way, 0 many-to-many, −1 many ends`;

  Status: "Before: 8 navigable directions and 4 associations to keep in step both ways; after: 4 and 0; the count is of the model stated."

  Rules: "Each record is one association between classes a and b: ends 1-n
  means one a to many b; direction both, a-b (only a navigates to b) or b-a.
  A two-way association gives 2 navigable directions and 2 references to
  keep in step whenever one link changes; a one-way association gives 1 of
  each. A qualifier (qualified yes) reduces one many end to one: the end
  navigated to (b for a-b, a for b-a; for both, b if it is many, else a); a
  qualifier on an end that is already one is refused. Every count is after
  qualifiers. The after list, when given, is counted the same way, each tile
  reads before → after, and the change is after − before."

  Refuses: a qualifier on a one end ("before, record 1 (a–b): a qualifier
  reduces the many end it navigates to, and the b end of n-1 a-b is already
  one"). With `after` empty every tile shows the before figure alone and
  dasChange reads `no after list given`. The lab does not match before and
  after records to each other; it compares the two lists' totals, so an
  author can drop, add or rewrite associations freely. The table lists every
  association of both lists with its ends as written and after the
  qualifier, its navigation (`member→loan`, `book↔author`), directions and
  many ends.

  Further figures: `books and authors, qualified` (`book, author, n-n, both,
  no` → `book, author, n-n, a-b, yes`): dasDirections `2 → 1`, dasManyMany
  `1 → 0`, dasManyEnds `2 → 1`.

### identity (`did`)

- **equality.** The same by identity, or the same by value. Fields:
  - `objects` (records of name (name), id (name or `-`), then 0–12 attribute cells (name=value); 1–60, —), id `didInObjects`, labelled "Objects (name, id or -, then attribute=value cells)";
  - `pairs` (records of x (name), y (name); 0–60, default empty), id `didInPairs`, labelled "Pairs to compare (x, y; empty for every pair)";

  Tiles, with their values on the sample preset `clinic` (objects="p1, P-100, name=Ana, born=1990; p1b, P-100, name=Ana, born=1990, phone=5550101; p2, P-200, name=Ana, born=1990; a1, -, street=Elm, number=4; a2, -, street=Elm, number=4.0", pairs=""):
  - didPairs, Pairs compared, `10`;
  - didIdentity, Same by identity, `1: (p1, p1b)`;
  - didAttrs, Same by attributes, `2: (p1, p2), (a1, a2)`;
  - didChanged, Same thing, attributes changed, `1: (p1, p1b): phone`;
  - didLookalike, Different things, same attributes (look-alikes), `1: (p1, p2)`;

  Status: "10 pairs compared: identity and attributes disagree on 2 (1 changed, 1 look-alike); the count is of the model stated."

  Rules: "Two objects are the same by identity when both carry an id and the
  ids are equal (ids compare exactly; - means the object has no identity, a
  value object, and is never the same by identity). They are the same by
  attributes when they have the same attribute names and every value is
  equal (numbers exactly, so 2 = 2.0; words exactly, letter case counted). A
  changed pair is the same thing with different attributes; a look-alike pair
  is two things, both with ids and the ids different, with the same
  attributes. With no pairs given, every pair is compared in record order (at
  most 12 objects)."

  Refuses: more than 12 objects with no pairs given; a pair naming an unknown
  object, an object with itself, or the same pair twice (either order). An
  attribute present on one object and absent on the other is a difference
  (didChanged lists the differing attribute names, in the first object's
  order then the second's). Two value objects (`-` ids) with the same
  attributes are "equal values" in the table, not look-alikes.

  Further figures: `library copies, two pairs` (pairs `c1, c1x; c1, c2`):
  didChanged `1: (c1, c1x): shelf`, didLookalike `1: (c1, c2)`.

- **sharing.** A change through one holder of a shared value. Fields:
  - `holders` (records of holder (name), value (name); 1–60, —), id `didInHolders`, labelled "Holders (holder, the value it refers to)";
  - `value` (name, —), id `didInValue`, labelled "The shared value";
  - `change` (name, —), id `didInChange`, labelled "The holder that makes the change";
  - `kind` (choice: `mutable`, `immutable`, —), id `didInKind`, labelled "The value is";

  Tiles, with their values on the sample preset `mutable` (holders="ana, addr1; ben, addr1; cy, addr1; dee, addr2", value="addr1", change="ana", kind="mutable"):
  - didHolders, Holders of the value, `3: ana, ben, cy`;
  - didSee, Holders that see the change, `3: ana, ben, cy`;
  - didSurprised, Holders surprised (saw a change they did not make), `2: ben, cy`;
  - didNew, New values created, `0`;

  Status: "A change to the mutable value addr1 through ana is seen by 3 holders, 2 of whom did not make it; the count is of the model stated."

  Rules: "Each record says which value a holder refers to; several holders
  may share one. A change is made through one holder. If the value is mutable
  it changes in place, so every holder of it sees the change; if it is
  immutable the changing holder gets a new value (named with ′) and every
  other holder keeps the old one. A holder is surprised when it sees a change
  it did not make. Lists follow the record order."

  Refuses: a value no holder holds; a change through a name that is not a
  holder; a change through a holder of another value ("dee holds addr2, not
  addr1; the change must be made through a holder of addr1"). Under
  `immutable`: didSee `1: ana`, didSurprised `0: none`, didNew `1: addr1′,
  now held by ana`. A lesson pinning both kinds can state `holders`,
  `value` and `change` once in the cfg and vary `kind` per preset.

### aggregate (`dgr`)

- **boundary.** Who may hold a reference into an aggregate. Fields:
  - `objects` (records of object (name), aggregate (name), root (choice: `yes`, `no`); 1–60, —), id `dgrInObjects`, labelled "Objects (object, aggregate, root yes or no)";
  - `refs` (records of from (name), to (name); 0–60, default empty), id `dgrInRefs`, labelled "References (from, to; from may be an outside holder)";
  - `delete` (name or `-`, default `-`), id `dgrInDelete`, labelled "Delete this object (- for none)";

  Tiles, with their values on the sample preset `delete-root` (objects="loan1, loan, yes; line1, loan, no; line2, loan, no; member1, member, yes; card1, member, no", refs="member1, loan1; desk, line2; line1, card1; loan1, line1; card1, member1; report, loan1", delete="loan1"):
  - dgrAggregates, Aggregates, `2: loan, member`;
  - dgrObjects, Objects, `5`;
  - dgrCrossing, References crossing a boundary, `4`;
  - dgrViolations, Of those, to a non-root (violations), `2: desk → line2, line1 → card1`;
  - dgrRemoves, Objects the delete removes, `3: loan1, line1, line2`;
  - dgrDangling, References left dangling, `3: member1 → loan1, desk → line2, report → loan1`;

  Status: "6 references, 4 crossing a boundary, 2 of them to non-roots; deleting loan1 removes 3 objects and leaves 3 dangling; the count is of the model stated."

  Rules: "Each object belongs to one aggregate, and each aggregate has
  exactly one root. A reference crosses a boundary when it comes from outside
  the aggregate it points into: from another aggregate's object, or from a
  name that is not an object (an outside holder). A crossing reference may
  hold only the root; one to any other object is a violation. Deleting a root
  removes its whole aggregate; deleting a non-root is refused, naming the
  root to go through. A reference left dangling runs from a surviving object
  or outside holder to a removed object. Lists follow the order of the
  records."

  Refuses: an aggregate with no root or with two; a reference to a name that
  is not an object (a non-object name may only hold references); a delete of
  an unknown name. A delete of a non-root is NOT a page refusal: it shows in
  the tiles (dgrRemoves `refused: line2 is not the root of loan; delete it
  through loan1`, dgrDangling `none: the delete is refused`). With `delete`
  `-` both tiles read `no delete given`. A reference from inside an
  aggregate to its own non-root objects is "inside" and never a violation;
  references held by the deleted objects are removed with them.

- **lock.** Concurrent edits, an invariant that spans objects. Fields:
  - `items` (records of item (name), value (number, −10,000,000 to 10,000,000); 1–20, —), id `dgrInItems`, labelled "Items of one aggregate (item, value)";
  - `limit` (number, −10,000,000 to 10,000,000, —), id `dgrInLimit`, labelled "The invariant: sum of the values at most";
  - `edits` (records of minute (whole 1–1,440), user (name), item (name), value (number, −10,000,000 to 10,000,000); 1–60, —), id `dgrInEdits`, labelled "Edits (minute, user, item, new value)";
  - `scheme` (choice: `object`, `aggregate`, default `object`), id `dgrInScheme`, labelled "Locking scheme";

  Tiles, with their values on the sample preset `object` (items="bread, 40; cake, 30; pies, 20", limit="100", edits="1, ana, bread, 48; 2, ben, cake, 38; 4, ana, pies, 20", scheme="object"):
  - dgrCommitted, Users who commit, `2: ana, ben`;
  - dgrRefused, Users refused, `0: none`;
  - dgrFinal, Final values, `bread = 48, cake = 38, pies = 20`;
  - dgrSum, Final sum, `106`;
  - dgrHolds, Invariant holds, `no: sum 106 over limit 100`;
  - dgrLost, Edits lost (overwritten by a later commit), `0: none`;

  Status: "Under object locks, 2 users commit and 0 are refused; the invariant (sum ≤ 100) is broken after the last commit; the count is of the model stated."

  Rules: "Every user reads the aggregate at minute 0, edits items at the
  minutes given (an edit sets the item's new value) and commits at their last
  edit's minute. Locks are pessimistic, taken at an edit and held to the end
  of the user's commit minute. Object scheme: an edit locks only its item, so
  two users conflict only on the same item. Aggregate scheme: an edit locks
  the whole aggregate. An edit of what another user holds refuses its user
  outright: all their edits are discarded and their locks released. Edits are
  taken in minute order, ties in record order; commits apply in
  commit-minute order, ties in order of first appearance. An edit lost is a
  committed value overwritten by a later commit. The invariant is that the
  sum of the values is at most the limit."

  Refuses: an edit of an unknown item; minutes outside 1–1,440; more than
  20 items. The table shows each user's edits, **the sum that user saw**
  (the minute-0 values plus their own edits — the figure each user would
  have checked the invariant against) and the outcome (`committed at minute
  4`, `refused: bread held by ana at minute 2`). Users are listed in order of
  first appearance. A lock is free again the minute after its holder's
  commit, so under the aggregate scheme a later user can take it once the
  first has committed (the PLAN's "first user takes the aggregate" holds
  while that user is working).

  Further figures (items `bread, 40; cake, 30; pies, 20`, limit `100`):
  the same edits under `aggregate`: dgrCommitted `1: ana`, dgrRefused
  `1: ben (the aggregate held by ana at minute 2)`, dgrHolds `yes: sum 98
  within limit 100`. `1, ana, bread, 45; 2, ben, bread, 50` under `object`:
  ana commits at 1, ben locks bread at 2, dgrLost `1: bread (ana’s)`, dgrSum
  `100`. `1, ana, bread, 45; 2, ben, bread, 50; 3, ana, cake, 30`: dgrRefused
  `1: ben (bread held by ana at minute 2)`.

### spec (`dsp`)

All three views share the candidates field and the grammar. The rules
sentence of each begins: "A specification is clauses attribute op value,
with op one of = != < <= > >=, joined by and, or, not and parentheses (not
binds tightest, then and, then or); a value is a number or a word beginning
with a letter. Numbers compare exactly; a word compares only by = and != (an
ordering op on a word is refused), and words compare exactly, letter case
counted. A clause on an attribute the candidate lacks is false whatever its
op, so not of it is true; an ordering clause on a word value is false."

Keywords `and`, `or`, `not` are lower case; spaces are optional around
operators and parentheses (`pages<=320` reads). A clause prints as
`attr op value` with single spaces in every tile. `!=` on a number is true
for a word value (`x != 3` holds for x = rye) but false for a missing one.

Refusals (every one names the box, "The specification", "Specification A"
or "Specification B"): a character it cannot read (`!`, `$`, `==` reads as
`=` then `=`: refused as a missing value); an operator, keyword, number or
parenthesis where an attribute should be; no operator after an attribute;
no value after an operator; an ordering op on a word ("The specification:
genre >= crime orders a word; a word compares only by = and !="); an
unclosed or stray parenthesis; text after the end; more than 20 clauses,
8 levels of parentheses or 300 characters; a value with more than 6
decimals or over 10,000,000 in size.

- **validate.** One candidate against one rule. Fields:
  - `candidates` (records of name (name), then 1–12 attribute cells (name=value); 1–40, —), id `dspInCandidates`, labelled "Candidates (name, then attribute=value cells)";
  - `candidate` (name, —), id `dspInCandidate`, labelled "The candidate to validate";
  - `spec` (specification, at most 300 characters, —), id `dspInSpec`, labelled "The specification";

  Tiles, with their values on the sample preset `b2` (candidates="b1, pages=320, genre=crime, year=2001; b2, pages=412, genre=crime, year=1998; b3, pages=150, genre=poetry, year=2015; b4, pages=280, year=2010; b5, pages=300, genre=crime, year=2020", candidate="b2", spec="genre = crime and pages <= 300 and year >= 2000"):
  - dspSatisfied, Satisfied, `no`;
  - dspTrue, Clauses true, `1 of 3`;
  - dspFirstFalse, The first false clause, in the order written, `clause 2, pages <= 300: pages is 412`;
  - dspFalse, Every false clause, `2: pages <= 300, year >= 2000`;

  Status: "b2 does not satisfy the specification; 1 of its 3 clauses is true; the count is of the model stated."

  The view's rules add: "Clauses are numbered in the order written; the first
  false clause is the first in that order, whether or not the whole is
  satisfied." Refuses a candidate name not among the candidates. The table
  lists each clause with the candidate's value (`412`, `missing`, `rye, not a
  number`) and true/false. Under `or` or `not` the first false clause need
  not be why the candidate fails (or the candidate may be satisfied with
  false clauses): preset `b4`, `not (genre = crime) or pages < 100` on a book
  with no genre, gives dspSatisfied `yes`, dspTrue `0 of 2`, dspFirstFalse
  `clause 1, genre = crime: genre missing`.

- **select.** A rule as a query over candidates. Fields:
  - `candidates` (records of name (name), then 1–12 attribute cells (name=value); 1–40, —), id `dspInCandidates`, labelled "Candidates (name, then attribute=value cells)";
  - `spec` (specification, at most 300 characters, —), id `dspInSpec`, labelled "The specification";

  Tiles, with their values on the sample preset `short-crime` (candidates="b1, pages=320, genre=crime, year=2001; b2, pages=412, genre=crime, year=1998; b3, pages=150, genre=poetry, year=2015; b4, pages=280, year=2010; b5, pages=300, genre=crime, year=2020", spec="genre = crime and pages <= 320"):
  - dspCandidates, Candidates, `5`;
  - dspSatisfying, Satisfying, `2: b1, b5`;
  - dspFailing, Failing, each with the clause that rejects it, `3: b2 (pages <= 320: pages is 412); b3 (genre = crime: genre is poetry); b4 (genre = crime: genre missing)`;

  Status: "The specification selects 2 of 5 candidates; the count is of the model stated."

  The view's rules add: "Candidates are listed in record order. A failing
  candidate is shown with the clause that rejects it, found from the left: a
  false and is blamed on its first false part, a true or on its first true
  part, and under a not a clause rejects by being true (for clauses joined
  only by and, this is the first false clause in the order written)."
  Further figures: `not (genre = poetry) and (year > 2000 or pages < 200)`
  selects `3: b1, b4, b5` and dspFailing reads `2: b2 (year > 2000: year is
  1998); b3 (genre = poetry, true under not: genre is poetry)`.

- **subsume.** Does every candidate one rule accepts pass the other. Fields:
  - `candidates` (records of name (name), then 1–12 attribute cells (name=value); 1–40, —), id `dspInCandidates`, labelled "Candidates (name, then attribute=value cells)";
  - `spec` (specification, at most 300 characters, —), id `dspInSpec`, labelled "Specification A";
  - `other` (specification, at most 300 characters, —), id `dspInOther`, labelled "Specification B";

  Tiles, with their values on the sample preset `follows` (candidates="b1, pages=320, genre=crime, year=2001; b2, pages=412, genre=crime, year=1998; b3, pages=150, genre=poetry, year=2015; b4, pages=280, year=2010; b5, pages=300, genre=crime, year=2020", spec="pages <= 400 and genre = crime", other="pages <= 320 and pages > 100 and genre = crime and year >= 2000"):
  - dspSatB, Satisfying B, `2: b1, b5`;
  - dspSatA, Satisfying A, `2: b1, b5`;
  - dspOnCands, On these candidates: every one B accepts, A accepts too, `yes: all 2 that satisfy B satisfy A`;
  - dspCounter, Counter-examples (B accepts, A rejects), `0: none`;
  - dspLogical, For every possible candidate: every one B accepts, A accepts too, `yes: every clause of A follows from B’s clauses`;

  Status: "On these 5 candidates, every one B accepts, A accepts too; for every possible candidate, yes; the count is of the model stated."

  **Which way "subsumes" runs.** The tiles never use the word, because it
  is used both ways round: in the logicians' sense the looser rule (A, when
  the answer is yes) subsumes the stricter (B); in Evans's sense (Chapter 10,
  "Subsumption") the stricter specification subsumes the looser, so a yes
  here means **B subsumes A in Evans's words**. A lesson quoting Evans
  should say "B subsumes A" for a yes, or better, the plain relation the
  tile states. (Check the direction against your copy when you quote it.)

  The view's rules add: "The question is one relation, in plain words: does
  A accept every candidate B accepts? The word subsumes is used both ways
  round: in the logicians' sense the looser rule, A, subsumes B; in Evans's
  sense (Chapter 10) the stricter rule, B, subsumes A. The tiles avoid the
  word. On the candidates the relation is checked one by one. For every
  possible candidate the answer is exact when both are clauses joined only
  by and: B's clauses on each attribute give the values it allows (an
  interval of numbers less excluded points, and words), and A accepts all B
  accepts when B allows nothing or every clause of A holds for everything B
  allows, an attribute B never mentions being allowed missing. With or or
  not in either, the lab says it cannot decide."

  dspLogical reads one of: `yes: every clause of A follows from B’s
  clauses`; `yes, vacuously: B can select nothing (no value of pages meets
  all its clauses)`; `no: B says nothing of pages, so a
  candidate missing it can satisfy B and fail A’s clause pages <= 320`;
  `no: B allows a value of pages that fails A’s clause pages < 320`;
  `not decidable by the lab: A uses or, and the lab decides only clauses
  joined by and`. dspOnCands reads `yes: all 2 that satisfy B satisfy A`,
  `yes: the one candidate that satisfies B satisfies A`, `yes, vacuously: no
  candidate satisfies B` or `no: 1 of the 2 that satisfy B fails A`. **The
  two can disagree, and that is the lesson's point**: preset `unmentioned`
  (A `pages <= 320 and genre = crime`, B `genre = crime and year >= 2000`)
  is `yes` on the five books and `no` logically. Parentheses around a pure
  conjunction are allowed (`(a = 1 and b = 2) and c = 3` is decided).

### A sample preset (spec/subsume)

```python
"lab": ("dddkit", {
    "mode": "spec", "view": "subsume",
    "candidates": "b1, pages=320, genre=crime, year=2001; b2, pages=412, genre=crime, year=1998; "
                  "b3, pages=150, genre=poetry, year=2015; b4, pages=280, year=2010; "
                  "b5, pages=300, genre=crime, year=2020",
    "presets": [
        {"id": "follows", "label": "a narrower crime shelf",
         "spec": "pages <= 400 and genre = crime",
         "other": "pages <= 320 and pages > 100 and genre = crime and year >= 2000",
         "expect": {"dspSatB": "2: b1, b5",
                    "dspLogical": "yes: every clause of A follows from B’s clauses"}},
        {"id": "unmentioned", "label": "the candidates agree, the rules do not",
         "spec": "pages <= 320 and genre = crime", "other": "genre = crime and year >= 2000",
         "expect": {"dspOnCands": "yes: all 2 that satisfy B satisfy A",
                    "dspLogical": "no: B says nothing of pages, so a candidate missing it can satisfy B and fail A’s clause pages <= 320"}},
    ],
}),
```

Note the typographic apostrophe `’` in `B’s` and `A’s` (also in
dgrLost's `ana’s`): an `expect` string must use it.

### Verification (family A)

- `node scripts/mathcheck.js`: passes; family A's block holds 51
  assertions (the helpers; every sample preset above and the further
  figures; refusals; lock's minute boundary and same-minute tie; spec's
  precedence, missing and word semantics; 18 hand-worked logical subsumption
  pairs: open and closed ends, an excluded endpoint, a point, word
  exclusions, three kinds of empty B, an unmentioned attribute). The figures
  were counted by hand on the stated model, never read from the kit (one
  hand count, a two-way qualifier case, was wrong and corrected after
  checking by hand again).
- Every compute function was broken on purpose, once a line, in a scratch
  copy of `scripts/` (34 mutations: dddDec, dddValEq's case, the caution,
  glossary's missing-pair rule, case folding and ambiguity threshold,
  cognates' false-cognate and duplicate tests and its two-context refusal,
  assoc's directions, qualifier end and change sign, equality's identity
  rule, numeric equality and look-alike rule, sharing's immutable case,
  boundary's outside-holder rule, root test and dangling rule, lock's
  release minute, tie order, aggregate scope, lost detection and invariant
  comparison, the parser's precedence, missing-attribute semantics, `<=`,
  the not-blame, and subsume's closed-end merge, excluded endpoints, word
  `!=`, vacuous test, unmentioned attribute and open-end test). Every one fails a case. Six were first missed (a two-way qualifier on 1-n, two different numbers on one attribute, a sum equal to the limit, != on a missing attribute, blame through a not of an and, equal lower bounds merged); a case was added for each and each was then seen to fail.
- `node scripts/labcheck.js --expect` on 10 scratch pages (every family A
  view, 27 presets): every page executes and survives the sweep of every
  control; every pinned tile matches (and a deliberately wrong expectation
  was seen to fail the page).
- Python mirror against the page: 68 targeted inputs, same verdict and same
  sentence.
- `python3 scripts/build_paths.py --check` passes (no published page uses
  the kit) and the lab tests of `tests/test_site_invariants.py` pass.

### Deviations from PLAN §D (family A)

- **`dag` → `dgr`.** The aggregate prefix `dag` is used by other kits.
- **dddkit has its own `_build_lab`** (a thin copy of eakit_core's, reusing
  its parser, printers, markup and wiring unchanged) because eakit_core has
  no field kind for variable-length records with `k=v` cells nor for an
  expression containing `<`/`>` (which eakit refuses in every shipped
  value). eakit_core itself is untouched.
- **Attributes are `k=v` cells separated by commas**, not `k=v; …`: the
  semicolon already separates records. Values beginning with a digit are
  numbers; words must begin with a letter.
- **assoc/simplify** has no separate "references to keep consistent" tile:
  summed over the associations it equals the navigable directions exactly
  (2 for both ways, 1 for one way), so the kit shows the two-way count
  (dasTwoWay) instead, and the rules sentence states the equality. The
  qualifier's end is fixed by a stated rule; a qualifier on a one end is
  refused.
- **select** names, for each failing candidate, the clause that rejects it
  (not the first false clause in source order, which under `not` or `or` can
  be a clause irrelevant to the failure). For and-only specifications the two
  are the same. validate keeps the PLAN's literal first false clause.
- **identity/equality** counts a disagreement only between objects that
  both carry ids; value objects (`-`) are compared by attributes alone.
- **aggregate/lock** frees a lock after its holder commits (stated in the
  rules), so the aggregate scheme refuses only users who edit while another
  holds it. The table adds the sum each user saw.
- **lang** compares names ignoring letter case (`Loan` = `loan`), stated in
  both rules sentences.

## Family B (dddkit_b.py)

Four modes: modules, context, distill, ledger. Every example tile string below
was read off a rendered scratch page with `node scripts/labcheck.js --observe`.
Every view prints its counting rules under the tiles ("How the lab counts."),
and every status line ends "; the count is of the model stated." (`dddStatus`).
"Deviations from PLAN §D (family B)" at the end says where the kit differs.

### Conventions (family B)

- **Ids.** Prefixes `dmo` modules, `dcx` context, `dds` distill, `dle` ledger.
  Inputs are `<prefix>In<Key>` (`dmoInElements`, `dcxInRels`, `ddsInParts`,
  `dleInEntries`); each page has `<prefix>Preset`, `<prefix>Status`,
  `<prefix>Table`.
- **Records** are `a, b; c, d` (comma between cells, semicolon between
  records), at most 60 per box (posting rules at most 20). Names are letters,
  digits, `.`, `_`, `-`. A cfg key named like an input supplies it to every
  preset that does not set it (a map lesson can state `contexts` once).
- **Order and ties.** Lists of modules are alphabetical; lists of changes,
  contexts, accounts and transactions follow the order the lesson gives them.
  A "largest"/"most" tile breaks a tie as its rules sentence says (pairs:
  alphabetically first; changes: first given) and the status line names the
  others.
- **Exactness.** Shares are exact fractions (`1/3 ≈ 33.3%`, `1/2 = 50%`);
  ratios `2×`, `3/2 ≈ 1.5×`; money to the cent, `−` (U+2212) for minus.

### modules (`dmo`)

Lesson-level cfg for **cohesion** and **change** only: `packagings` (1 or 2,
default 1) and, with 2, optional `names` (two plain labels ≤ 30 characters,
default `["first packaging", "second packaging"]`), which suffix the tile
labels and head the table columns. With `packagings: 2` the elements box takes
a third column, `module2`, and every tile of packaging 2 has the id of
packaging 1's plus `2` (`dmoShare2`). `dmoChanges` is printed once.

- **cohesion**. Fields `elements` (records `element, module` — or
  `element, module, module2` — element names unique; id `dmoInElements`), `deps`
  (records `from, to`: from depends on to; `dmoInDeps`). Example (two
  packagings, names `by pattern`/`by concept`): elements `Book, entities,
  catalog; Copy, entities, catalog; Loan, entities, lending; Isbn, values,
  catalog; DueDate, values, lending; LoanService, services, lending`, deps
  `Copy, Book; Book, Isbn; Loan, Copy; Loan, DueDate; LoanService, Loan;
  LoanService, Copy`. Tiles:
  - `dmoModules` Modules: `3` (packaging 2: `2`);
  - `dmoInside` Dependencies inside a module: `2` (`4`);
  - `dmoAcross` Dependencies across modules: `4` (`2`);
  - `dmoShare` Share inside: `1/3 ≈ 33.3%` (`2/3 ≈ 66.7%`);
  - `dmoCycles` Module cycles: `0: none`; a seed bank (`intake`, `storage`,
    `testing`, two two-way pairs) gives `1: (intake, storage, testing)`; two
    separate cycles print `2: (m1, m2), (m3, m4)`;
  - `dmoPair` Most coupled pair: `entities and services: 2` (tied with
    entities and values; the status names it), `none` when nothing crosses.
  A cycle is a strongly connected group of ≥ 2 modules (each reaches every
  other along across-module dependencies), modules alphabetical inside a
  group, groups by first module. Table: (packaging,) module, elements, inside,
  out to others, in from others.
- **change**. Fields `elements` (as above), `changes` (records `change,
  element`, one per element the change touches; `dmoInChanges`). Example:
  elements `Appointment, scheduling; Slot, scheduling; Patient, records; Note,
  records; Invoice, billing`, changes `telehealth, Appointment; telehealth,
  Slot; consent, Patient; consent, Note; consent, Appointment; fee, Invoice`:
  - `dmoChanges` Changes: `3`;
  - `dmoPer` Modules touched per change: `telehealth 1, consent 2, fee 1`;
  - `dmoTotal` Total module touches: `4`;
  - `dmoConfined` Changes confined to one module: `2 of 3: telehealth, fee`
    (`0 of 3` when none);
  - `dmoLargest` The largest change: `consent, 2 modules` (tie: first given).
  A module counts once per change however many of its elements the change
  lists. Two packagings (theatre, `by concept`/`by tier`) print e.g.
  `dmoTotal` `4` and `dmoTotal2` `7`. Table: change, elements, modules per
  packaging.
- **layers**. Fields `layers` (names top to bottom, 2–12, `dmoInLayers`, e.g.
  `ui app domain infra`), `elements` (records `element, layer`), `deps`. Example:
  elements `LoanForm, ui; LendingService, app; Loan, domain; LoanRepo, infra;
  Database, infra`, deps `LoanForm, LendingService; LoanForm, Loan; LoanForm,
  Database; LendingService, Loan; Loan, LoanRepo; LoanRepo, Database; Loan,
  LendingService`:
  - `dmoDeps` Dependencies: `7`;
  - `dmoDown` Downward: `5` (ALL downward ones, skips included);
  - `dmoWithin` Within a layer: `1`;
  - `dmoUp` Upward (violations): `1: Loan → LendingService` (order given);
  - `dmoSkip` Downward, skipping a layer: `2` (a subset of downward);
  - `dmoEmpty` Layers with no element: `0: none` (`1: commitment`).
  Downward + within + upward = all. Responsibility layers work the same:
  `policy commitment decision operations potential`. Table: from (layer), to
  (layer), direction (`down`, `down, skipping 2 layers`, `within app`,
  `UP, 1 layer (a violation)`).

Refusals (all three): an element named in deps or changes that is not in
elements (`Dependencies, record 1: c is not one of the elements`); a
dependency on itself; a dependency given twice; a change listing an element
twice (`Changes, record 2: x already touches a`); a layer not in the list.

### context (`dcx`)

- **map**. Fields `contexts` (names, 2–30, `dcxInContexts`), `rels` (records
  `upstream, downstream, kind`, kind one of `shared-kernel`,
  `customer-supplier`, `conformist`, `acl`, `ohs`, `published-language`,
  `separate-ways`; `dcxInRels`), `changed` (a context; `dcxInChanged`).
  Example: contexts `catalog lending fines holds search reports`, rels
  `catalog, lending, conformist; lending, fines, customer-supplier; catalog,
  search, acl; catalog, holds, ohs; catalog, reports, published-language;
  fines, reports, separate-ways; lending, holds, shared-kernel`, changed
  `catalog`:
  - `dcxRels` Relationships: `7`;
  - `dcxModels` Other models that must change: `3: lending, fines, holds`;
  - `dcxTranslators` Translators to update: `2: search’s ACL from catalog,
    catalog’s protocol`;
  - `dcxReached` Contexts reached: `4: lending, fines, holds, search`;
  - `dcxUntouched` Contexts untouched: `1: reports`.
  Same map with `catalog, lending, acl`: `0: none` / `3: lending’s ACL from
  catalog, search’s ACL from catalog, catalog’s protocol`. Same map, changed
  `holds`: `2: lending, fines` / `0: none` (a shared kernel carries the change
  to lending, which carries it down to fines; nothing travels up to catalog).
  Propagation: a model change crosses a shared kernel both ways and goes down
  conformist and customer-supplier edges, and travels on only from a model
  that changed; never upstream. `acl` stops it at the downstream's ACL
  (one translator per acl edge, its owner counted as reached); `ohs` and
  `published-language` stop it at the upstream's protocol (ONE per upstream,
  however many consumers; the consumers are untouched); `separate-ways` does
  nothing. Translators are counted on every edge whose upstream model changed,
  not only at the first hop. Table: each relationship and what the change
  does there. Refusals: a context not listed; a context related to itself; a
  second relationship between the same two contexts (either order); the
  changed context not listed; any other kind word.
- **protocol**. Fields `contexts` (one whole number 2–60, or 2–60 names;
  `dcxInContexts`, e.g. `5` or `clinic pharmacy lab billing`), `scheme`
  (select `pairwise`/`published`, default pairwise; `dcxInScheme`).
  Lesson-level cfg `directed`: `"no"` (default, two-way translators) or
  `"yes"` (one-way). Tiles, n = 5 pairwise, two-way:
  - `dcxN` Contexts n: `5`;
  - `dcxBuild` Translators to build: `10` (published: `5`);
  - `dcxChange` Translators to change when one model changes: `4` (published `1`);
  - `dcxOther` The other scheme: `published: 5 to build, 1 to change`;
  - `dcxBuildRatio` Pairwise ÷ published, to build: `2×`;
  - `dcxChangeRatio` Pairwise ÷ published, to change: `4×`.
  Directed n = 4: `12`, `6`, `published: 8 to build, 2 to change`,
  `3/2 ≈ 1.5×`, `3×`. Refusals: a number outside 2–60; a single name.

### distill (`dds`)

- **effort**. Field `parts` (records `part, kind, weeks, strong`, optionally a
  fifth cell `option`; `ddsInParts`): kind `core`/`supporting`/`generic`,
  weeks whole 0–100,000 developer-weeks, strong whole 0–1,000 (the team's
  strongest developers on it), option `build` (= none), `buy`, `published`,
  `outsource`. Records may mix four and five cells. Example: `booking, core,
  20, 3; rota, supporting, 10, 1; billing, generic, 8, 1; auth, generic, 6, 0,
  buy`:
  - `ddsWeeks` Developer-weeks built in house: `38`;
  - `ddsCore` Share on the core: `10/19 ≈ 52.6%`;
  - `ddsSupporting` Share on supporting parts: `5/19 ≈ 26.3%`;
  - `ddsGeneric` Share on generic parts: `4/19 ≈ 21.1%`;
  - `ddsStrong` Strongest developers on the core: `3 of 5, 3/5 = 60%`
    (`0 of 0` when none named);
  - `ddsBuilt` Generic parts built in house: `1: billing`;
  - `ddsFree` Weeks buying or publishing would free: `8` (weeks of generic
    parts still built).
  Only built parts count weeks; the status line reports the weeks not counted.
  Refusals: an option other than build on a core or supporting part; strong
  > 0 on a part not built; no built weeks at all. For "share of the model a
  newcomer must read" (course 8 lesson 3), state model elements as the
  `weeks` figure and say so in the lesson; the tile labels stay.

### ledger (`dle`)

Amounts are signed decimals, at most 2 places (whole cents), up to
10,000,000 in size.

- **balance**. Field `entries` (records `txn, account, amount`;
  `dleInEntries`). Example `sale1, till, 12.50; sale1, sales, -12.50; sale2,
  till, 3.00; sale2, sales, -2.99`:
  - `dleAccounts` Accounts: `2`;
  - `dleBalances` Balances: `till 15.50, sales −15.49` (first appearance);
  - `dleTxns` Transactions: `2`;
  - `dleUnbalanced` Unbalanced transactions (net): `1: sale2 +0.01` (`0: none`);
  - `dleTotal` Total of all entries: `0.01` (`0.00`).
  Refusal: `Entries, record 1: 12.505 is not a whole number of cents; give at
  most 2 decimal places`.
- **post**. Fields `entries`, `rules` (records `rule, from, to, share`, share
  0–1 with ≤ 6 places, rule names unique, ≤ 20; `dleInRules`). Example
  entries `t1, sales, -10.05; t1, till, 10.05; t2, sales, -3.33; t2, till,
  3.33`, rules `vat, sales, vat, 0.2; tip, till, tips, 0.125`:
  - `dleGiven` Entries given: `4`;
  - `dleDerived` Entries derived: `8` (two per firing);
  - `dleBalances` Balances after: `sales −10.70, vat −2.68, till 11.70, tips 1.68`;
  - `dleList` Derived postings: `vat on t1: −2.01 to vat; tip on t1: 1.26 to
    tips; vat on t2: −0.67 to vat; tip on t2: 0.42 to tips` (first 12, then
    "and N more");
  - `dleLeft` Rounding left (exact − rounded, summed): `−0.0035` (exact
    decimal; `0` when none; `+0.005` for −0.05 × 0.5 → −0.03).
  Each rule fires once on every GIVEN entry to its from account (any sign),
  rules in order given; it posts round(share × amount) to `to` and the
  negation to `from`, in the entry's transaction, rounded half away from zero
  (also when 0.00). Derived entries never fire a rule (`reserve, vat, ...`
  stays idle). Balances after follow the journal order: each given entry then
  what it derives. Status: "2 of 2 rules fire, 4 times in all, on 4 given
  entries, …". Refusals: cents as above; a rule whose from equals its to.

### Deviations from PLAN §D (family B)

- **modules: the second packaging is a cfg switch** (`packagings: 2`), not a
  column the reader may add, because the tile set is fixed at build time.
- **layers: "downward" counts every downward dependency; "skipping a layer"
  is the subset** that passes over ≥ 1 layer.
- **map: ohs/published-language edges from one upstream share ONE protocol
  translator**, counted once (consistent with protocol's "published: 1 to
  change"); an acl is one translator per edge. Translators are counted on
  every edge whose upstream changed, beyond the first hop when a conformist
  chain carries the change on. A downstream's own ACL is not counted as
  changing when only its own model changes.
- **protocol: directed doubles the published figures too** (2n to build, 2 to
  change), so both schemes count the same unit and the ratios do not depend
  on `directed`. Contexts are one box (a number or names).
- **distill: weeks of a part not built are not counted; such a part may have
  no strongest developers** (refused), and only a generic part may be bought,
  published or outsourced.
- **ledger/post: a firing that rounds to 0.00 still derives its two entries.**

### Family B: verification

- `scripts/mathcheck.js`, block `// ---- dddkit (Domain-Driven Design),
  family B ----`: 47 assertions, every view and every refusal, on models
  counted by hand (the library packaged two ways, a seed-bank cycle, a clinic's
  changes, four and five layers, a six-context library map three ways,
  n = 4 and 5 protocols both units, a clinic's effort with a bought part, a
  bakery's till, VAT and tips to the cent).
- **Mutation testing.** 40 single breaks of `dddkit_b.py` (tie rules, the
  cycle test, the share's denominator, module counting once per change,
  skip and direction, each propagating kind, the shared protocol, the ACL
  owner, each formula, weeks of bought parts, the core's strongest, the
  rounding rule and its sign, the derived counter-entry, derived entries
  firing rules, every refusal), each run against the block: all 40 fail it.
  Two first survived (a negative transaction net; a 2-place rounding-left)
  and a case was added for each. The file was restored and checked by md5.
- **Parity.** 2,005 fuzzed inputs over all eight views through the Python
  checks and the page's JS: the same verdict and the same refusal sentence
  every time; no tile printed NaN, undefined or Infinity.
- 12 scratch pages (every view; both packagings; directed protocol; options)
  rendered as `scripts/preview_subject.py` renders, outside the repository:
  `node scripts/labcheck.js` executes and sweeps all 12, and `--expect`
  matches all 21 presets' pinned tiles; a deliberately wrong pin is reported.
  Pages are 33–35 KB gzipped.
