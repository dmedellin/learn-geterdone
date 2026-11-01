# gofkit (Design Patterns, Read Along): kit report

Lesson authors configure a lab from this report alone. It records the kit as
built to `docs/design-patterns/PLAN.md` §0 and §D. Family A (classes, tree,
expr) is `gofkit.py` and is reported here first; family B's section (route,
notify, history, machine, share, proxy) follows at the end. The seam between
the two modules is `docs/design-patterns/kit-contract.md`. Every example tile
string in family A's section was counted by hand and then read off a rendered
scratch page with `node scripts/labcheck.js --observe`; every one is pinned as
`expect` in `gofkit.SAMPLES` (one worked cfg per view, two or three presets
each; copy the shape, but use your lesson's own design). "Formulas and
deviations (family A)" says where family A chose a formula or differs from
§D, and why.

## Files

- `scripts/mathpath/labs/gofkit.py`: the entry point `gofkit_lab(cfg)`,
  `mode_lab(cfg, mode, spec)` (shared with family B), `GOF_CORE_JS` (shipped
  on every gofkit page after dddkit's `DDD_CORE_JS`: `gofStatus`, `gofCount`,
  `gofDec`, `gofNum`, `gofHas`), a thin copy of dddkit's lab builder (so the
  panel intro begins with gofkit's sentence, not dddkit's), family A's three
  modes (a base block `GCL_JS`, `GTR_JS`, `GEX_JS` and one block per view,
  `GCL_VIEW_JS["explosion"]`, …), each view's Python `check`, the Python
  mirror of the expression parser (`gex_parse`, `gex_value`), and `SAMPLES`.
  It re-exports dddkit's `vrec` and `expr`, imports `gofkit_b` with a plain
  import at its end, and dispatches family B's modes through `gofkit_b.MODES`.
- `scripts/mathpath/labs/dddkit.py`, `eakit_core.py`: used unchanged.
- `scripts/mathpath/labs/__init__.py`: one import (`gofkit,`) and one registry
  line (`"gofkit": gofkit.gofkit_lab,`).
- `scripts/build_paths.py`: `"gofkit"` added to `KITS_WITH_EXPECTATIONS`
  (the Subject is not in `GENERATED_PATHS`). Every gofkit preset menu must
  pin at least one tile on every option.
- `scripts/mathcheck.js`: the block `// ---- gofkit (Design Patterns), family
  A ----` … `// ---- end gofkit family A ----`, before THE VERDICT and before
  family B's block: 29 assertions, one vm context per mode.

## Conventions (both families)

**Entry point and cfg.** A lesson's lab is `("gofkit", cfg)`, with
`cfg["mode"]` (classes, tree, expr, or one of family B's: route, notify,
history, machine, share, proxy) and `cfg["view"]` (default: the mode's first
view, listed first below). An unknown mode or view raises, listing the valid
ones; every build error begins `gofkit/<mode>/<view>: `. Keys common to every
view: `mode`, `view`, `presets` (required, non-empty), `preset` (the one shown
first; default the first), `title`, `panel_title`, `panel_intro`. A cfg key
named like one of the view's inputs supplies it to every preset that does not
set it (the factory sample states `families` and `kinds` once and varies the
scheme per preset). Any other key raises, naming the keys the view takes.

**Panel intro.** Every gofkit panel intro begins "A count over the small
design the lesson states." and by default continues "The lab counts one
consequence of applying a pattern or not; whether the pattern fits is weighed
in the book, against what in the design is expected to vary." (PLAN §D). A
`panel_intro` in the cfg replaces all but the first sentence, which is put
back in front if missing.

**The caution.** Every status line, in every view of both families, ends
"; the count is of the design stated." (`gofStatus`). Under the tiles each
view prints "How the lab counts." with its rules sentence, quoted per view
below: what is counted, every formula, and how orders go.

**Presets.** `{"id": "lower-case-hyphens", "label": "plain text",
<inputs>..., "expect": {tile_id: "exact text"}}`. A label names the instance;
outcomes go in `expect`. Read the strings off the built page with `node
scripts/labcheck.js --observe <page>` (or `scripts/preview_subject.py`'s
pages), never out of the code. A preset the page would refuse fails the
build, naming the preset and the reason. **Instances are the lesson's own,
never the book's** (PLAN §C: no Lexi glyphs, maze rooms, widget families, TCP
states, drawing-editor shapes, equipment pricing, boolean or regular
expression grammars, …).

**Ids.** Family A's prefixes are `gcl` classes, `gtr` tree, `gex` expr. Inputs
are `<prefix>In<Key>` (`gclInAspects`, `gtrInNodes`, `gexInExpr`); each page
also has `<prefix>Preset`, `<prefix>Status`, `<prefix>Table`.

**Input formats.** Records are `a, b; c, d` (a trailing `;` is allowed);
lists are names separated by spaces or commas and may not repeat a name.
Names are letters, digits, `.`, `_`, `-` (`-` alone means none where a field
allows it). Decimals have at most 6 places and are at most 10,000,000 in
size; fractions and exponents are refused. `< > & "` are refused in every
shipped value (the expression box refuses `&` and `"`, and its lexer refuses
the rest). Nothing typed is evaluated as script.

## Family A (gofkit.py): modes, views, fields, tiles

### classes (`gcl`)

- **explosion.** Every combination a subclass, or one hierarchy per aspect.
  Fields:
  - `aspects` (records of aspect (name), then 1–8 variants (names); 2–4 records, —), id `gclInAspects`, labelled "Aspects (aspect, then its variants)";
  - `added` (name or `-`, default `-`), id `gclInAdded`, labelled "The aspect that gains one variant (- for none)".

  Tiles, on the sample preset `coffee` (aspects="size, small, medium, large; milk, whole, oat; cup, paper, ceramic", added="milk"):
  - gclCombos, Combinations, `3 × 2 × 2 = 12`;
  - gclSubclass, Classes, one subclass per combination, `12 + 1 = 13`;
  - gclCompose, Classes, one hierarchy per aspect, `(3 + 1) + (2 + 1) + (2 + 1) = 10`;
  - gclRatio, Subclassing against composition, `13/10 ≈ 1.3×` (a whole ratio prints `2×`);
  - gclRefs, References each object of the first aspect holds, `2: milk, cup`;
  - gclAddSubclass, A new variant: classes added by subclassing, `3 × 2 = 6 (13 → 19)`;
  - gclAddCompose, A new variant: classes added by composition, `1 (10 → 11)`.

  With `added` `-` both addition tiles read `no aspect gains a variant`.
  Status: "3 aspects with 7 variants: 13 classes as one subclass per
  combination, 10 as one hierarchy per aspect; the count is of the design
  stated." Table: each aspect, its variants, `× k` under subclassing and
  `k + 1 = …` under composition, then the abstract base (`+ 1`) and the totals.

  Rules: "Each record is one aspect that varies, then its variants (2 to 4
  aspects, 1 to 8 variants each); every name is a class and is used once.
  Combinations = the product of the variant counts. With one subclass per
  combination the design has that product + 1 classes (one abstract base).
  With one hierarchy per aspect, joined by composition, each aspect has 1
  abstract class + 1 concrete class per variant, so the design has the sum of
  the variant counts + the number of aspects; the client holds the first
  aspect's abstract class, and each of its objects holds one reference per
  other aspect. The ratio is the first count over the second. One new variant
  of the added aspect adds the product of the other aspects' counts under
  subclassing and 1 class under composition; neither design edits an existing
  class for it."

  Refuses: fewer than 2 or more than 4 aspects, an aspect with no variant or
  more than 8; a name used twice anywhere, aspect or variant ("Aspects: small
  is named twice; every aspect and every variant is a class, and each needs a
  name of its own"); an `added` that is not one of the aspects. Not shown by
  the tiles: which aspect comes first matters only to gclRefs. Further
  figures: `print-shop` (job with 4 variants, finish with 2, added finish):
  `4 × 2 = 8`, `8 + 1 = 9`, `(4 + 1) + (2 + 1) = 8`, `9/8 ≈ 1.1×`,
  gclAddSubclass `4 (9 → 13)`; `bike-dock` (four aspects of 2, 2, 2, 3):
  `2 × 2 × 2 × 3 = 24`, `24 + 1 = 25`, composition `… = 13`, `25/13 ≈ 1.9×`,
  gclRefs `3: motor, lock, rack`.

- **factory.** Families and kinds of product, and who makes them. Fields:
  - `families` (list of 1–8 names, —), id `gclInFamilies`, labelled "Families (1 to 8 names)";
  - `kinds` (list of 1–8 names, —), id `gclInKinds`, labelled "Kinds of product (1 to 8 names)";
  - `scheme` (choice `abstract-factory`, `factory-method`, `prototype`; default `abstract-factory`), id `gclInScheme`, labelled "The scheme";
  - `change` (choice `none`, `family`, `kind`; default `none`), id `gclInChange`, labelled "The change".

  Tiles, on the sample preset `af-kind` (families="rustic french vegan", kinds="loaf roll", scheme abstract-factory, change kind):
  - gclProducts, Concrete products (families × kinds), `3 × 2 = 6`;
  - gclClasses, Classes in the design, `1 + 3 + 2 + 6 = 12` (terms in the table's row order);
  - gclFactories, Classes that create (factories or creators), `1 + 3 = 4`;
  - gclConfigs, Prototype configurations, `none: the factory classes themselves fix what is made` (under prototype: `3 configurations of 2 prototypes (6 instances)`);
  - gclAdded, Classes the change adds, `4 (12 → 16): 1 abstract product, 3 concrete products`;
  - gclChanged, Existing classes the change edits, `4: the abstract factory and 3 concrete factories, each given an operation to make the new kind` (every other case `0`);
  - gclConfigChange, Configurations the change touches, `none: this scheme configures no prototypes` (under prototype: `1 added, registering 2 prototypes` for a family; `3 changed, each registering 1 more prototype` for a kind).

  With `change` `none` the three change tiles read `no change chosen`.
  Status: "abstract-factory: 3 × 2 products in 12 classes; a new kind of
  product adds 4 and edits 4; the count is of the design stated." Table: one
  row per class role the scheme has (abstract factory, concrete factories,
  abstract creators, creator subclasses, prototype manager, abstract
  products, concrete products) with its formula, its count now and, with a
  change, after (`3 (+1)`), then `in all`.

  Rules: "F families × K kinds of product. Every scheme has K abstract
  products and F × K concrete product classes, counted as if each concrete
  product differs in behaviour. Abstract Factory adds 1 abstract factory and 1
  concrete factory per family: 1 + F + K + F × K. Factory Method mirrors the
  products with creators, 1 abstract creator per kind and 1 creator subclass
  per concrete product: K + F × K + K + F × K. Prototype adds 1 prototype
  manager, a registry keyed by kind, and no factory subclasses: 1 + K + F × K;
  a family is a configuration of K prototype instances. A new family adds its
  K products and, under Abstract Factory, 1 concrete factory, under Factory
  Method K creator subclasses, under Prototype 1 configuration; it edits no
  existing class. A new kind adds 1 abstract product and F concrete products,
  and under Factory Method 1 abstract creator and F creator subclasses; under
  Abstract Factory it edits the abstract factory and every concrete factory
  (1 + F classes), each gaining an operation; under Prototype it edits no
  class, and each of the F configurations registers one more prototype. The
  client is not counted."

  Refuses only what the field parser refuses (an empty list, more than 8, a
  repeated name). A family may share a name with a kind. Further figures:
  `fm-family` (factory-method, family): gclClasses `2 + 6 + 2 + 6 = 16`,
  gclFactories `2 + 6 = 8`, gclAdded `4 (16 → 20): 2 creator subclasses, 2
  concrete products`, gclChanged `0`; `proto-kind` (prototype, kind):
  gclClasses `1 + 2 + 6 = 9`, gclFactories `1`, gclAdded `4 (9 → 13): 1
  abstract product, 3 concrete products`. The Discussion of Creational
  Patterns lesson can state `families` and `kinds` once in the cfg and give
  one preset per scheme.

### tree (`gtr`)

All three views read the same `nodes` field: records of node (name), parent
(name or `-`), kind (name), value (a decimal, or `-`); 1–60, node names
unique, required; id `gtrInNodes`, labelled "Nodes (node, parent, kind,
value)". Example: `hamper, -, Box, -; tray, hamper, Box, -; jam, hamper,
Item, 4.5; bread, tray, Item, 3.25; scone, tray, Item, 1.75; tin, hamper,
Box, -; tea, tin, Item, 6`. A node with a decimal value is a leaf; one with
`-` is a composite (and may have no children). Every tree view refuses: no
root, or more than one ("The tree has 2 roots (a, b); …"); a parent that is
not a node; a node that is its own parent; nodes not reached from the root
("Nodes b, c cannot be reached from the root a; their parents form a
cycle"); a value that is not a decimal; a leaf with children ("… has a value,
so it is a leaf, and a leaf has no children, but it has 1 (c); a composite
has the value -"); one kind used for both a leaf and a composite. Shared
rules: "Each record is one node: its name, its parent (- for the root;
exactly one root), its kind (a class name) and its value, a decimal for a
leaf and - for a composite. A leaf has no children; a composite may have
none. Children are taken in record order. A kind is either a leaf class or a
composite class, never both. Depth counts the edges on the longest path down
from the root (a root alone is at depth 0)." Each view's own sentence
follows.

- **compose.** One operation over a whole and its parts. Fields: `nodes`;
  `asks` (list of names, 0–60, default empty), id `gtrInAsks`, labelled "Nodes
  asked to add a child (names; empty for none)"; `declare` (choice `safe`,
  `transparent`; default `safe`), id `gtrInDeclare`, labelled "Child
  operations are declared".

  Tiles, on the sample preset `hamper` (the nodes above, asks="jam tin", declare safe):
  - gtrNodes, Nodes, `7`; gtrLeaves, Leaves, `4`; gtrComposites, Composites, `3`; gtrDepth, Depth, `2`;
  - gtrCalls, Calls one operation on the root makes, `7: 1 from the client + 6 forwarded by composites`;
  - gtrTotal, The total (the sum of the leaves), `15.5` (exact and grouped: `1,234.5`);
  - gtrAskLeaves, Leaves asked to add a child, `1: jam (refused by the compiler: add is declared only on composites)`; under transparent `1: jam (accepted by the interface: each ignores it or fails at run time)`; none asked `0: none`;
  - gtrAskTaken, Composites asked to add a child (they do), `1: tin`.

  Status: "One operation on hamper makes 7 calls and totals 15.5; the count is
  of the design stated." Table: each composite in record order with its
  kind, children, leaves below, subtotal and calls in its subtree (`hamper /
  Box / 3 / 4 / 15.5 / 7; tray / Box / 2 / 2 / 5 / 3; tin / Box / 1 / 1 / 6 /
  2`).

  Rules (after the shared ones): "One operation on the root makes one call per
  node: the client's call on the root, and one call from each composite to
  each of its children. The total is the sum of the leaf values, exactly; a
  composite's subtotal is the sum of the leaves below it, and its calls are
  the nodes in its subtree. A composite asked to add a child does. A leaf
  asked to: under the safe declaration (add declared only on the composite
  class) the call does not compile; under the transparent one (add declared
  on every component) it compiles, and the leaf ignores it or fails at run
  time."

  Refuses also: an asked name that is not a node. Not shown: an asked child is
  not added to the tree (every count is of the tree as stated). Further
  figures: `playlist` (transparent, no asks): gtrTotal `527.5`, gtrAskLeaves
  `0: none`.

- **traverse.** One tree, three orders. Fields: `nodes`; `find` (name or `-`,
  default `-`), id `gtrInFind`, labelled "A node to find (- for none)".

  Tiles, on the sample preset `hamper` (find="scone"):
  - gtrNodes, Nodes, `7`;
  - gtrPre, Pre-order, `hamper, tray, bread, scone, jam, tin, tea`;
  - gtrPost, Post-order, `bread, scone, tray, jam, tea, tin, hamper`;
  - gtrLevel, Level-order, `hamper, tray, jam, tin, bread, scone, tea`;
  - gtrFind, The node to find, by position, `pre-order 4, post-order 2, level-order 6 (of 7)`; with `-`: `no node to find`.

  Status: "Three orders over 7 nodes: pre-order starts at hamper, post-order
  at bread; the count is of the design stated." Table: each node, its parent,
  depth and position in each order.

  Rules (after the shared ones): "Pre-order visits a node, then each child's
  subtree in order; post-order visits each child's subtree in order, then the
  node; level-order visits the root, then every node at depth 1, then depth
  2, each level left to right in record order of the children. Positions
  count from 1." Refuses also: a `find` that is not a node. Further figures:
  `audio-guide`: gtrLevel `tour, hall1, hall2, garden, vase, mask, coin`.

- **visit.** Operations as visitors, or as methods of the elements. Fields:
  `nodes`; `visitors` (list of 1–4 names, —), id `gtrInVisitors`, labelled
  "Visitors, the operations (1 to 4 names)"; `adding` (choice `none`,
  `operation`, `kind`; default `none`), id `gtrInAdding`, labelled "The
  addition".

  Tiles, on the sample preset `hamper-kind` (visitors="price weigh", adding kind):
  - gtrAccepts, Accept calls, `14: 7 nodes × 2 visitors`;
  - gtrVisits, Visit calls, `14`;
  - gtrElements, Element classes, `1 + 2 = 3 (the abstract element; Box, Item)` (kinds in order of first appearance);
  - gtrVisitorClasses, Visitor classes, `1 + 2 = 3 (the abstract visitor; price, weigh)`;
  - gtrMethods, Methods written, with Visitor, `2 × 2 + 2 = 6`;
  - gtrMethodsPlain, Methods written, operations on the elements, `2 × 2 = 4`;
  - gtrAddVisitor, The addition, with Visitor, `1 added (the new element class), 3 changed (the abstract visitor and 2 visitors)`; for an operation `1 added (the new visitor), 0 changed`;
  - gtrAddPlain, The addition, operations on the elements, `1 added (the new element class), 0 changed`; for an operation `0 added, 3 changed (the abstract element and 2 element classes)`; with `none` both read `no addition chosen`.

  Status: "2 visitors over 7 nodes of 2 kinds: 14 accept calls and as many
  visit calls; the count is of the design stated." Table: visit calls by kind
  (rows) and visitor (columns), then `in all`.

  Rules (after the shared ones): "The structure asks every node to accept
  each visitor once, and each accept makes one visit call on the visitor's
  method for that node's kind: nodes × visitors of each. Element classes are
  1 abstract element + 1 per kind; visitor classes are 1 abstract visitor + 1
  per visitor. Methods written, counting implementations only: with Visitor,
  kinds × visitors visit methods + 1 accept per kind; with each operation a
  method of the element classes, kinds × visitors. A new operation is 1 new
  visitor and changes nothing, against a change to the abstract element and
  every element class; a new kind is 1 new element class that changes the
  abstract visitor and every visitor, against nothing changed."

  Values are read and checked but not used. Further figures:
  `guide-operation` (Stop and Exhibit kinds, visitors narrate time, adding
  operation): gtrAddVisitor `1 added (the new visitor), 0 changed`.

### expr (`gex`)

- **interpret.** A class per rule, an expression as a tree of objects.
  Fields:
  - `expr` (one expression, at most 300 characters, —), id `gexInExpr`, labelled "The expression"; like dddkit's spec box it is empty in the markup and filled by script;
  - `context` (records of name (name), value (decimal); 0–60, names unique, default empty), id `gexInContext`, labelled "Context (name, value; empty for none)".

  Tiles, on the sample preset `coffee-price` (expr="base + shots * 0.6 - discount", context="base, 3.2; shots, 2; discount, 0.5; tip, 1"):
  - gexValue, Value, `39/10 = 3.9` (whole values `42`; non-terminating `1/3 ≈ 0.33`);
  - gexNodes, Nodes, `7`;
  - gexByClass, Nodes by class, `Number 1, Variable 3, Add 1, Subtract 1, Multiply 1` (always in the order Number, Variable, Add, Subtract, Multiply, Divide, Negate; absent classes left out);
  - gexClasses, Classes used, `5 of the 7`;
  - gexCalls, Interpret calls, `7: 1 from the client + 6 from nodes to their operands`;
  - gexDepth, Depth, `3`;
  - gexVars, Variables used, `3: base, shots, discount` (distinct, in first appearance);
  - gexUnused, Context names not used, `1: tip`.

  Status: "The expression interprets to 39/10 = 3.9 in 7 interpret calls; the
  count is of the design stated." Table: each node in post-order: step,
  class, its subexpression as typed (`b * 2`, `a - b * 2`), value.

  Rules: "The language: numbers (at most 6 decimal places, at most
  10,000,000), variables (a letter, then letters, digits or underscores;
  letter case counts), + - * /, a minus in front, and parentheses. * and /
  bind tighter than + and -, a leading minus tighter than either, and each
  operator groups from the left (8 - 3 - 2 is (8 - 3) - 2). Each number,
  variable and operator is one node, of the class Number, Variable, Add,
  Subtract, Multiply, Divide or Negate; parentheses make no node, and -3 is a
  Negate of the Number 3. Interpreting the root makes one interpret call per
  node. Values are exact fractions; a variable takes its value from the
  context, and one the context does not give, or a divisor that is 0, is
  refused. Depth counts the edges on the longest path down from the root."

  Refuses, with the page's sentence: any other character ("The expression has
  "%" at character 3; it reads numbers, names, + - * / and parentheses"); a
  number with more than 6 places or over 10,000,000; a missing operand ("…
  ends where a number, a name, - or ( should be"; "… has + at character 1,
  where a number, a name, - or ( should be": there is no unary plus); an
  unclosed or stray parenthesis; two operands in a row (`2x`: "… has x at
  character 2, where an operator or the end should be"); variables the
  context does not give, all named ("The context gives no value for hours,
  x; add a record name, value for each"); division by zero, naming the
  divisor and the division ("Division by zero: the divisor b - 2 is 0 in a /
  (b - 2)"); a context name that cannot appear in an expression (one with
  `-` or `.`, or beginning with a digit). Not shown: unbound variables are
  refused before any division by zero is looked for. Further figures:
  `box-office` (`(adults * 12 + children * 7.5) * (1 - discount)`, adults 2,
  children 3, discount 0.1): `837/20 = 41.85`, 11 nodes, `Number 3, Variable
  3, Add 1, Subtract 1, Multiply 3`; `thermostat` (`(target - now) / step`,
  21, 18.5, 0.5): `5`, `Variable 3, Subtract 1, Divide 1`, depth `2`.

### Formulas and deviations (family A)

- **explosion**: subclassing = ∏kᵢ + 1; composition = Σkᵢ + (number of
  aspects), as §D. Added: the references tile (aspects − 1) and before → after
  totals on the addition tiles.
- **factory, Abstract Factory**: 1 + F + K + F·K, as §D; a new kind adds 1 + F
  and edits 1 + F; a new family adds K + 1 and edits 0.
- **factory, Factory Method: deviation.** §D has 1 abstract creator; the kit
  has **one abstract creator per kind** (the creator hierarchy parallels the
  product hierarchy, each abstract creator's factory method returning its
  kind's abstract product) and one creator subclass per concrete product:
  2(K + F·K). A new family adds 2K, a new kind 2(F + 1), and neither edits a
  class. A design whose single creator overrides K factory methods per family
  is not what this scheme counts; a lesson that means that one should say so
  in prose (its counts are Abstract Factory's).
- **factory, Prototype**: 1 + K + F·K, as §D. The manager is a registry keyed
  by kind, so a new kind edits no class; §D's "1 configuration changed"
  becomes 1 configuration added for a new family and F configurations
  changed for a new kind. Concrete product classes are counted as if each
  differs in behaviour; where families differ only in values Prototype could
  drop them, which the lab does not count (say so in prose if the lesson's
  design is like that).
- **compose**: `declare` is a select input, not a lesson-level cfg key, so the
  reader can switch it.
- **visit**: the abstract element and abstract visitor are counted, so a new
  kind changes V + 1 classes and a new operation (without Visitor) K + 1;
  §D's "every visitor" / "every element class" leave the abstract class out.
- **interpret**: names in expressions may not contain `.` or `-` (a `-` is
  minus); §D's general name rule holds in every other box.

### Verification (family A)

- `node scripts/mathcheck.js` passes (family A block: 29 assertions). Each
  case was seen to FAIL with its function broken on purpose, 34 breaks in
  all, then restored: the caution text; gofDec and gofNum places; each
  explosion formula and the duplicate-name refusal; each scheme's roles, the
  Abstract Factory edit count and Prototype's configuration count; every tree
  refusal, the subtotal and subtree sums, the pre/post walk and child order;
  each visit count; Subtract's operand order, precedence, Negate as a node,
  the zero-divisor and unbound refusals, the parenthesised span, depth, the
  stray-parenthesis message and repeated variables.
- Every view built through `gofkit_lab` for every preset of `SAMPLES`; a
  scratch Subject rendered with `scripts/preview_subject.py` ran clean under
  `labcheck.js` (every select swept, hostile strings in every box) and every
  pinned tile matched (6 pages, 0 failing); a deliberately wrong pin failed.

## Family B (gofkit_b.py)

Six modes: route, notify, history, machine, share, proxy. Every example tile
string below was read off a rendered scratch page with `node
scripts/labcheck.js --observe`, and every one is pinned as `expect` in the
worked cfgs `gofkit_b.SAMPLES` (one per view; copy them freely, but swap in
your lesson's own design). Every view prints its counting rules under the
tiles ("How the lab counts."), and every status line ends "; the count is of
the design stated." (`gofStatus`). "Formulas and deviations (family B)" at
the end says where the kit chose or differs from PLAN §D.

### Conventions (family B)

- **Ids.** Prefixes `grt` route, `gno` notify, `ghi` history, `gsm` machine,
  `gsh` share, `gpx` proxy (grepped free on 2026-11-01). Inputs are
  `<prefix>In<Key>` (`grtInHandlers`, `ghiInScript`, `gpxInRights`); each page
  has `<prefix>Preset`, `<prefix>Status`, `<prefix>Table`.
- **Records** are `a, b; c, d`. Some take a variable tail (dddkit's `vrec`):
  `handler, topic, topic, …`. Names are letters, digits, `.`, `_`, `-`.
  Event, request and script lists may repeat a name. A cfg key named like an
  input supplies it to every preset that does not set it.
- **Optional inputs** (`order`, `rights`) default to empty; `stored` defaults
  to `yes`, `ref` to `0`; schemes default to `direct`, `inverse`, `lazy`.
- **Order and ties.** Lists follow the order the lesson gives. A "busiest" /
  "largest" / "most" tile breaks a tie toward the first given (first in the
  chain); the chain view's status names the others.
- `-` means "none" where a tail allows it (a handler taking nothing, a
  subclass overriding nothing), and must stand alone.

### route (`grt`)

- **chain**. Fields `handlers` (records `handler, topic, …` in chain order, 1–12
  handlers, 1–12 topics each; `all` takes every topic, `-` none;
  `grtInHandlers`), `requests` (topics in the order sent, 1–60, repeats
  allowed; `grtInRequests`). Example: handlers `logger, -; bot, unlock,
  balance; agent, unlock, refund, damage; supervisor, refund, ban`, requests
  `unlock balance refund ban theft unlock damage theft`:
  - `grtRequests` Requests: `8`;
  - `grtHandled` Handled: `6 of 8`;
  - `grtHops` Times passed on, in all: `16`;
  - `grtUnhandled` Unhandled (position): `2: theft (5), theft (8)` (`0: none`);
  - `grtPer` Requests each handler takes: `logger 0, bot 3, agent 2, supervisor 1`;
  - `grtBusiest` The busiest handler: `bot, 3 requests` (`none` if nothing is handled).
  A box office `kiosk, collect; clerk, collect, exchange, refund; manager,
  all` on `refund collect comp exchange collect`: `5 of 5`, hops `4`,
  busiest `kiosk, 2 requests` (tied with clerk; the status names it). Table:
  request, topic, path (`logger → bot → agent → supervisor → off the end`),
  taken by, passed on. Refusals: `-` or `all` with other topics; a topic twice
  in one handler; `all` or `-` as a request.
- **wrap**. Fields `core` (one record `component, value`, the value a number
  or a word; `grtInCore`), `layers` (records `decorator, op, amount`
  innermost first, op `add`/`times`/`then`, 1–8, names unique;
  `grtInLayers`), `order` (optional: the decorator names in another order,
  innermost first; empty compares the reverse; `grtInOrder`). Example: core
  `flatwhite, 2.50`, layers `milk, add, 0.40; double, times, 2; syrup, add,
  0.35`:
  - `grtLayers` Decorators: `3`;
  - `grtCalls` Call order: `in: syrup, double, milk; core: flatwhite; out: milk, double, syrup`;
  - `grtResult` Result: `6.15` (exact decimal, as typed: no grouping, no trailing zero);
  - `grtOther` Result in the other order: `6.1`;
  - `grtMatters` Does the order change it?: `yes` (`no` for two adds);
  - `grtSubclass` Classes, one subclass per combination: `8 (the component + 7 combinations)`;
  - `grtDecorator` Classes with Decorator: `6 (interface, component, abstract decorator + 3)`;
  - `grtAddOne` Classes one more option adds: `subclassing +8, Decorator +1`.
  Words: core `ticket, Row-F`, layers `date, then, Sat-14; seat, then, F12;
  vip, then, VIP`, order `vip date seat`: `Row-F Sat-14 F12 VIP` against
  `Row-F VIP Sat-14 F12`. Table: position, decorator, does, value after.
  Refusals: a number with `then`, a word with `add`/`times`; a non-number
  amount for add/times; a value that is neither number nor word (`1e5`); a
  decorator named like the component; an other order that misses a decorator
  or names an unknown one.
- **template**. Fields `steps` (records `step, kind`, kind
  `fixed`/`primitive`/`hook`, in order, 1–12; `grtInSteps`), `subclasses`
  (records `subclass, step, …` the steps it overrides, or `-`, 1–8;
  `grtInSubclasses`). Example (bakery): steps `weigh, fixed; mix, primitive;
  proof, hook; bake, primitive; cool, fixed; glaze, hook`, subclasses
  `Sourdough, mix, bake, proof; Brioche, mix, bake, glaze; Flatbread, mix,
  proof`:
  - `grtSteps` Steps: `6: 2 fixed, 2 primitive, 2 hooks`;
  - `grtOwn` Steps each subclass writes: `Sourdough 3, Brioche 3, Flatbread 2`;
  - `grtAbstract` Subclasses left abstract: `1: Flatbread (lacks bake)` (`0: none`);
  - `grtHooks` Hooks each subclass overrides: `Sourdough 1, Brioche 1, Flatbread 1`;
  - `grtBase` Steps written once in the base: `4`;
  - `grtWhole` Step bodies, the algorithm written whole in each subclass: `18`;
  - `grtWith` Step bodies with the template: `12`.
  Table: subclass, runs (`weigh base, mix own, proof own, bake MISSING, cool
  base, glaze base default`), primitives supplied (`1 of 2`), hooks
  overridden. Refusals: overriding a fixed step, an unknown step, a step
  twice, `-` with steps. A missing primitive is NOT refused: it is shown.

### notify (`gno`)

- **observer**. Fields `subjects` (names, 1–12; `gnoInSubjects`), `observers`
  (records `observer, subject, …`, 1–20; `gnoInObservers`), `operations`
  (records `operation, subject, …` the subjects it changes in order, a subject
  may repeat; 1–20; `gnoInOperations`), `scheme` (`direct`/`managed`;
  `gnoInScheme`). Example (thermostat): subjects `temp humidity mode`,
  observers `display, temp, humidity, mode; logger, temp, humidity; fan, temp;
  app, mode`, operations `reading, temp, humidity; storm, temp, humidity,
  temp; switch, mode; calibrate, humidity`:
  - `gnoChanges` Changes: `7`;
  - `gnoSent` Updates sent: `17` (managed: `10`);
  - `gnoOther` Under the other scheme: `managed: 10` (`direct: 17`);
  - `gnoRedundant` Redundant updates a change manager saves: `7` (either scheme);
  - `gnoPer` Updates each observer receives: `display 7, logger 6, fan 3, app 1` (managed `display 4, logger 3, fan 2, app 1`);
  - `gnoNever` Observers never notified: `0: none` (`1: ticket`);
  - `gnoUnobserved` Subjects no one observes: `0: none` (`1: garden`).
  Table: operation × observer; under managed a cell reads `1 (of 3)` where
  direct would send more. Refusals: observing an unknown subject or one
  twice; an operation changing an unknown subject.

### history (`ghi`)

- **undo**. Fields `state` (records `cell, whole value`, 1–12; `ghiInState`),
  `commands` (records `command, op, cell, amount`, op `set`/`add`, whole
  amounts, 1–20; `ghiInCommands`), `script` (command names, `undo`, `redo`,
  1–60; `ghiInScript`), `scheme` (`inverse`/`snapshot`; `ghiInScheme`).
  Example: state `bikes, 10; fee, 2`, commands `rent, add, bikes, -1; ret,
  add, bikes, 1; price, set, fee, 3; free, set, fee, 0`, script `rent rent
  price undo undo redo free undo undo undo undo`:
  - `ghiFinal` Final state: `bikes 10, fee 2` (grouped: `flour 1,000`);
  - `ghiUndo` Undo stack, bottom to top: `0: none`;
  - `ghiRedo` Redo stack, bottom to top: `3: free, rent, rent`;
  - `ghiRefused` Refused: nothing to undo or redo: `undo 1, redo 0`;
  - `ghiDiscarded` Redo entries a new command discarded: `1`;
  - `ghiStored` Values the history holds at the end: `1` (snapshot: `6`);
  - `ghiOther` Under the other scheme: `snapshot: 6` (`inverse: 2`).
  Table: step, script, did (`ran free, discarding 1 redo`, `undid rent`,
  `redid rent`, `nothing to undo`), state after, both stacks. Refusals: a
  command named `undo`/`redo`; a command on an unknown cell; a script entry
  that is not a command, `undo` or `redo`. An empty-stack undo/redo is
  counted, not refused. The scheme never changes the states, only the count.

### machine (`gsm`)

- **states**. Fields `states` (names, first is the start, 1–12;
  `gsmInStates`), `events` (names, 1–12; `gsmInEvents`), `transitions`
  (records `state, event, next`; `gsmInTransitions`), `input` (events in
  order, 1–60; `gsmInInput`). Example (parcel locker): states `idle reserved
  loaded emptied jammed`, events `reserve load collect cancel timeout jam`,
  transitions `idle, reserve, reserved; reserved, load, loaded; reserved,
  cancel, idle; loaded, collect, emptied; loaded, timeout, reserved; emptied,
  reserve, reserved; loaded, jam, jammed; jammed, cancel, idle`, input `load
  reserve load timeout load collect cancel reserve`:
  - `gsmFinal` Final state: `reserved`;
  - `gsmIgnored` Events ignored (position): `2: load at idle (1), cancel at emptied (7)`;
  - `gsmDefined` Transitions defined: `8`;
  - `gsmBranches` Branches in one conditional: `13`;
  - `gsmClasses` Classes with State: `7`;
  - `gsmLargest` The largest state class: `loaded, 3 transitions`;
  - `gsmNever` States never entered: `1: jammed`.
  Table: step, state, event, next (`ignored: stays idle`). Refusals: an
  unknown state, event or input event; two transitions for one state and
  event.

### share (`gsh`)

- **flyweight**. Fields `objects` (records `state, how many objects`, the
  intrinsic state's name and a count 1–1,000,000, 1–60; `gshInObjects`),
  `intrinsic` (bytes, 1–1,000,000; `gshInIntrinsic`), `extrinsic` (bytes,
  0–1,000,000; `gshInExtrinsic`), `stored` (`yes`/`no`; `gshInStored`),
  `ref` (bytes for a reference, 0–64; `gshInRef`). Example (map tiles):
  objects `grass, 4000; water, 2500; road, 600; forest, 900`, intrinsic
  `4096`, extrinsic `8`:
  - `gshObjects` Objects: `8,000`;
  - `gshFlyweights` Flyweights: `4`;
  - `gshWithout` Bytes without sharing: `32,832,000`;
  - `gshWith` Bytes with flyweights: `80,384`;
  - `gshSaved` Bytes saved: `32,751,616` (negative when sharing costs more: `−16`);
  - `gshShare` Share saved: `63,968/64,125 ≈ 99.8%`;
  - `gshLargest` Most objects on one flyweight: `grass, 4,000 objects`;
  - `gshSmallest` Fewest objects on one flyweight: `road, 600 objects`.
  Seats computed in place (`stored` no, `ref` 2): `3,920` against `304`,
  `226/245 ≈ 92.2%`. Table: state, objects, bytes unshared, bytes shared.
  No refusals beyond the field reader.

### proxy (`gpx`)

- **access**. Fields `subjects` (records `subject, whole cost`, 1–20;
  `gpxInSubjects`), `requests` (records `client, subject` in order, 1–60;
  `gpxInRequests`), `scheme` (`eager`/`lazy`/`fresh`; `gpxInScheme`),
  `rights` (optional records `client, subject, …`; `gpxInRights`). Example
  (audio-guide tracks): subjects `intro, 40; egypt, 120; rome, 90; vault,
  200`, requests `ana, intro; ben, egypt; ana, egypt; guest, vault; ben,
  intro; cara, egypt`, rights `ana, intro, egypt, rome; ben, intro, egypt;
  cara, egypt`, lazy:
  - `gpxRequests` Requests: `6`;
  - `gpxRefused` Refused by the protection proxy: `1: guest → vault (4)`;
  - `gpxCreations` Instances created: `2` (eager `4`, fresh `5`);
  - `gpxStart` Cost at the start: `0` (eager `450`);
  - `gpxTotal` Cost in all: `160`;
  - `gpxNever` Subjects never requested: `2: rome, vault`;
  - `gpxAlive` Instances alive at the end: `2`;
  - `gpxFirst` The first request's cost: `40` (eager `0`; `none served`);
  - `gpxCompare` Cost in all, each scheme: `eager 450, lazy 160, fresh 440`.
  Singleton: one subject `catalogue, 30` asked four times, fresh: `4`
  instances, `120`; compare `eager 30, lazy 30, fresh 120`. Table: request,
  client, subject, outcome (`created`/`reused`/`refused`), cost. Refusals:
  an unknown subject in requests or rights; a subject twice in a rights
  record.

### Formulas and deviations (family B)

- Decorator: subclassing = 2ⁿ (the component + one per non-empty set of n
  on/off options); Decorator = n + 3 (interface, concrete component, abstract
  decorator, n decorators). PLAN said "n + 2"; the book's structure has three
  fixed classes. One more option: +2ⁿ against +1.
- Chain: an unhandled request is passed on n − 1 times. `*` is written `all`
  (the shared reader takes no `*`); `all` is therefore not a topic.
- Template: step bodies whole = steps × subclasses; with the template =
  fixed + hooks + every override. A missing primitive is shown as abstract
  rather than refused, so a lesson can show it.
- Observer: direct = Σ over changes of the subject's observers; managed = one
  per (operation, observer) pair where the operation changed something the
  observer observes; redundant = the difference.
- History: the script names commands directly (`do:` is not readable: `:` is
  not a name character). Stored values count what both stacks hold at the
  end: inverse = entries whose command is a `set`; snapshot = entries × cells.
- State: one conditional = transitions + states (a default per state);
  State = states + 2.
- Flyweight: objects are given as counts per intrinsic state (PLAN: one
  record per object), so a lesson can state thousands. Unshared = N(I + X);
  shared = F·I + N·(X if stored else 0) + N·ref.
- Proxy: nothing is freed, so alive = created; a refused request's subject
  does not count as requested.
- Shared-reader note (not family B's code): eakit's `eaRecords` and dddkit's
  `dddVrec` detect a repeated first cell with a plain `{}`, so a name
  `__proto__` given twice is not refused on the page, though Python refuses
  it at build. Family B's own tables use `Object.create(null)`.

### Family B: verification

`node scripts/mathcheck.js`, block "gofkit (Design Patterns), family B": 67
cases; each of 38 deliberate breaks (one per formula, order, tie rule and
refusal) made at least one case fail, and all pass restored. Every preset
in `SAMPLES` builds through `gofkit.gofkit_lab`; a scratch render passes
`labcheck.js --expect` (sweep included, every pinned tile matching). 2,800
fuzzed inputs agree between the Python checks and the JS on what is refused.
