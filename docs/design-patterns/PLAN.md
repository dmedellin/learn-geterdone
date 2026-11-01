# Design Patterns, Read Along — the build specification

The curriculum, lab and authoring contract for the seventeenth Subject: a
read-along of Erich Gamma, Richard Helm, Ralph Johnson and John Vlissides,
*Design Patterns: Elements of Reusable Object-Oriented Software* (Reading,
Mass.: Addison-Wesley, 1995) — "the Gang of Four" — in the book's own order:
the introduction, the Lexi case study, and the twenty-three patterns of the
catalog, one lesson per pattern. The operator asked for it the same way as the
previous ones ("Next in line"), all the way to live.

It is built the way *Domain-Driven Design* (`docs/domain-driven-design/PLAN.md`)
and *Patterns of Enterprise Application Architecture*
(`docs/enterprise-patterns/PLAN.md`) were, and adopts their conventions by
reference wherever this one is silent: Enterprise Patterns' §E (package,
quoting, author's checklist), §F (voice) and §R lessons; Domain-Driven
Design's §E–§F. Read before this: `AGENTS.md` §0, §1, §1a, §7, §8;
`content/AGENTS.md`; `docs/domain-driven-design/AUTHORING.md`.

**Neighbours.** Three Subjects already in the library meet this book.
*Domain-Driven Design* has a lesson "Strategy and Composite in the Model"
(`ddd-patterns-and-refactoring/strategy-and-composite`); *Enterprise
Application Patterns* uses Gang of Four patterns throughout; *Code Complete*
teaches the inheritance and coupling heuristics Chapter 1 leans on. A lesson
here that meets one of them names that lesson by title once and does not
repeat its prose. This Subject is the source those books cite: it teaches the
pattern itself, at the scale of a few classes.

Contents: §0 the one question · §A PATH · §B courses · §C every lesson ·
§D the new kit · §E package, text, quoting · §F voice · §G left out

---

## §0 The one question: what does the reader compute?

The book is a catalog of designs, and every pattern's "Consequences" section
argues by pointing at something a reader can count on a small design written
down in front of them:

1. **Classes.** How many classes a design needs when every combination of two
   or three varying things is a subclass, and how many when each varying thing
   is its own hierarchy joined by composition (Bridge, Decorator, Strategy,
   the Introduction's inheritance versus composition); how many classes, and
   how many existing classes changed, when a new product family or a new kind
   of product is added under Abstract Factory, Factory Method and Prototype.
2. **Object structures.** On a tree of parts, how many calls one operation
   makes, what it totals, the order an iterator visits (Composite, Iterator);
   under Visitor, the accept and visit calls, and the classes to change when a
   new operation or a new kind of element is added; an expression's value and
   its node count under Interpreter.
3. **Requests in motion.** Which handler in a chain takes each request and
   how many it passes on the way (Chain of Responsibility); the order a stack
   of wrappers runs in and what it returns (Decorator); the steps a template
   method runs for each subclass and the hooks it overrides (Template
   Method).
4. **Notifications and history.** The updates a change sends to observers,
   and the redundant ones a change manager saves (Observer); the undo and redo
   stacks after a sequence of commands, and the state stored as inverse
   commands against snapshots (Command, Memento).
5. **States and access.** A state machine's trace over a sequence of events,
   and the branches a single conditional needs against the classes of State;
   the objects created and the cost spent under eager creation, lazy creation
   behind a proxy, and a single shared instance (Proxy, Singleton); the
   storage a pool of shared flyweights saves (Flyweight).
6. **Couplings.** How many classes a client depends on with and without a
   facade or a mediator; how many modules a change reaches (Facade, Mediator,
   designing for change).

**What the lab never does** is judge a design. Every count is of the small
design the lesson states, and a count shows one consequence of applying a
pattern or not; it is not a verdict on the pattern, whose fit depends on what
in the design is expected to vary — which is how the book itself frames every
choice. The material clause (§A) says so, and every lesson closes on that gap.

## §A PATH fields (`content/design_patterns/__init__.py`)

```
"slug": "design-patterns",
"title": "Design Patterns, Read Along",
"level": "Intermediate",
"level_note": "you can read a short Java class and know what an interface and a subclass are",
"speech": "code",
```

Catalog: `short_title` `"Design Patterns"`, `"kind": "Read along"`, last in
the computing group (after Domain-Driven Design), card: "The Gang of
Four&rsquo;s <em>Design Patterns</em>, pattern by pattern, with each
pattern&rsquo;s consequences counted on a small design: classes, calls,
notifications, undo stacks and objects shared." Extend the computing group's
note with Design Patterns beside the other read-alongs ("assume only that you
can read a short routine" or the note's current wording). Course slug prefix
`gof-`; check-id prefix `gof`; package `design_patterns` → slug
`design-patterns` needs no `PACKAGE_OF_SLUG` entry. `"speech": "code"`.

**material** (unique; required by `TestGeneratedPathIsCurrent`):
"every figure on this path is counted in your browser from the small design a
lesson states &mdash; its classes, objects, requests, events and changes
&mdash; and a count shows one consequence of applying a pattern or not; it is
not a verdict on the pattern, whose fit depends on what in the design is
expected to vary."

tagline / description: written by course 1's author from the final counts
(`test_the_tagline_and_description_state_the_real_counts`). The tagline names
the book with `<em>`, says each pattern's consequences are counted on a small
design, and ends "Six courses and N lessons are available."

## §B The six courses

| # | slug | title | chapters | lessons | module dir |
|---|---|---|---|---|---|
| 1 | `gof-introduction` | What Design Patterns Are | 1 | 6 | `c1_introduction` |
| 2 | `gof-document-editor` | A Case Study: Designing a Document Editor | 2 | 7 | `c2_document_editor` |
| 3 | `gof-creational` | Creational Patterns | 3 | 6 | `c3_creational` |
| 4 | `gof-structural` | Structural Patterns | 4 | 8 | `c4_structural` |
| 5 | `gof-behavioral-requests` | Behavioral Patterns I: Requests, Languages and Traversal | 5 (first six) | 6 | `c5_behavioral_requests` |
| 6 | `gof-behavioral-objects` | Behavioral Patterns II: Notification, State and Algorithms, and the Conclusion | 5 (last five, discussion), 6 | 7 | `c6_behavioral_objects` |

40 lessons. Chapter 5 holds eleven patterns, more than one course's worth; it
is split after Memento, in the book's alphabetical order, and the second half
takes the chapter's discussion and Chapter 6, the Conclusion. Modules (the
`module` field) are the book's chapter titles, e.g. `"Chapter 4 · Structural
Patterns"`. Lessons past five go in `part_b.py`.

## §C Every lesson

Format: slug — Title — chapter and sections (book pages from the contents;
the PDF page of the operator's copy is found with `book.py`) — lab
`kit/mode` view — focus. Instances are the lesson's own: **never the book's
example data as lab data** — no Lexi glyphs, rows and characters as a lab's
model, no maze rooms and doors, no WidgetFactory/Motif/Presentation Manager
families, no TCPConnection states, no ET++ or InterViews class names, no
DrawingEditor shapes, no equipment pricing (Composite/Visitor sample), no
boolean-expression grammar or regular-expression grammar for Interpreter, no
help-handler widgets for Chain of Responsibility, no font dialog for
Mediator, no spreadsheet/bar-chart for Observer. The book's examples are
summarised in prose, where the pattern's argument runs through them, and
named by section; each lab works a design written for the lesson (a coffee
order, a print shop, a ticket desk, a recipe book, a music playlist, a parcel
locker, a museum audio guide, a garden irrigation controller, a bike-share
dock, a theatre box office, a bakery's orders, a library catalogue, a
thermostat, a vending machine, a quiz app, a map tile viewer).

Every pattern lesson covers, in the lesson's own words: the pattern's intent
(paraphrased; the book's intent sentence may be the counted quotation), the
motivating problem, applicability, the participants and collaborations named
in prose, the consequences (benefits and liabilities, both), the main
implementation issues, a short Java 8 sketch written for the lesson (at most
twenty lines a block), the book's sample code and known uses named but not
reproduced, and related patterns.

A lesson may switch to a different existing view if the one named cannot show
its focus; it says so in the author's report.

### Course 1 — What Design Patterns Are (Chapter 1, Introduction)
1. `what-is-a-design-pattern` — What Is a Design Pattern? — 1.1 What Is a Design Pattern?, 1.2 Design Patterns in Smalltalk MVC — `gofkit/notify` view `observer` — Alexander's definition carried to objects; the four essential elements (name, problem, solution, consequences); MVC read as Observer, Composite and Strategy; the lab: one model, three views, the updates each change sends.
2. `describing-and-organizing-the-catalog` — Describing and Organizing the Catalog — 1.3 Describing Design Patterns, 1.4 The Catalog of Design Patterns, 1.5 Organizing the Catalog — `dddkit/spec` view `select` — the template's sections and what each is for; purpose (creational, structural, behavioral) and scope (class, object); patterns used together and as alternatives; the lab: a handful of patterns as candidates with `purpose` and `scope` attributes the reader assigns from the lesson's prose (at most eight; not a copy of the book's table), selected by a specification.
3. `objects-interfaces-and-implementations` — Objects, Interfaces and Implementations — 1.6 How Design Patterns Solve Design Problems: Finding Appropriate Objects, Determining Object Granularity, Specifying Object Interfaces, Specifying Object Implementations (class versus interface inheritance; programming to an interface, not an implementation) — `cckit/deps` view `coupling` — types, signatures, dynamic binding and polymorphism; the principle "program to an interface"; the lab: a client depending on three concrete classes against the same client depending on one interface, its fan-out and the classes a new variant reaches.
4. `inheritance-versus-composition` — Inheritance Versus Composition — 1.6: Putting Reuse Mechanisms to Work (inheritance versus composition, delegation, inheritance versus parameterized types), Relating Run-Time and Compile-Time Structures — `gofkit/classes` view `explosion` — white-box and black-box reuse; "favor object composition over class inheritance"; delegation and its cost; aggregation versus acquaintance; the lab: two or three varying aspects, classes as one subclass per combination against one hierarchy per aspect, and the classes a new variant adds.
5. `designing-for-change` — Designing for Change — 1.6: Designing for Change (the common causes of redesign; application programs, toolkits and frameworks) — `dddkit/modules` view `change` — the eight causes of redesign, each with the patterns that address it, in the lesson's words; frameworks and inversion of control; the lab: change requests against a design where a varying thing is spread through the code and one where it is encapsulated, modules each change touches.
6. `selecting-and-using-a-pattern` — Selecting and Using a Design Pattern — 1.7 How to Select a Design Pattern, 1.8 How to Use a Design Pattern — `dddkit/spec` view `select` — the six approaches to selecting (how patterns solve problems, intents, interrelationships, purpose, causes of redesign, what should be variable); the steps of using one; the warning that patterns buy flexibility at the cost of complexity and should be applied only where the flexibility is needed; the lab: a design's anticipated changes as candidates, which a specification of "what should vary" selects and which clause rejects the rest.

### Course 2 — A Case Study: Designing a Document Editor (Chapter 2)
Every lesson summarises Lexi's problem and the book's solution in prose; the
lab works a different editor-free design of the lesson's own that has the same
shape (a recipe book, a slide outline, a playlist, a museum guide).
1. `document-structure` — Design Problems and Document Structure — 2.1 Design Problems, 2.2 Document Structure — `gofkit/tree` view `compose` — the seven design problems; recursive composition; the Glyph interface's three responsibilities, summarised; Composite as the pattern; the lab: a tree of parts, the calls one operation makes and what it totals.
2. `formatting` — Formatting — 2.3 Formatting — `gofkit/classes` view `explosion` — encapsulating the formatting algorithm; Compositor and Composition; Strategy; the lab: structures × algorithms as subclasses against a structure that holds an algorithm object.
3. `embellishing-the-interface` — Embellishing the User Interface — 2.4 Embellishing the User Interface — `gofkit/route` view `wrap` — transparent enclosure; MonoGlyph; Decorator; the lab: a component wrapped in decorators, the order they run in and what the stack returns, and how the order changes it.
4. `look-and-feel` — Supporting Multiple Look-and-Feel Standards — 2.5 — `gofkit/classes` view `factory` — abstracting object creation; factories and product classes; Abstract Factory; the lab: families × kinds of product, classes in the design, and what a new family and a new kind each add and change.
5. `window-systems` — Supporting Multiple Window Systems — 2.6 — `gofkit/classes` view `explosion` — why Abstract Factory does not fit here; encapsulating implementation dependencies; Window and WindowImp; Bridge; the lab: abstractions × platforms as subclasses against two hierarchies joined by a reference.
6. `user-operations` — User Operations — 2.7 User Operations — `gofkit/history` view `undo` — encapsulating a request; Command and its subclasses; undoability; the command history and the present line; the lab: a sequence of commands, undos and redos on a small state, the two stacks and the state after each step.
7. `spelling-and-hyphenation` — Spelling Checking and Hyphenation — 2.8 Spelling Checking and Hyphenation, 2.9 Summary — `gofkit/tree` view `visit` — accessing scattered information (Iterator and its subclasses), traversal versus actions on traversal, encapsulating the analysis (Visitor); the eight patterns of the chapter, summarised; the lab: an operation over a tree as a visitor, the accept and visit calls, and the classes a new operation and a new element kind each change.

### Course 3 — Creational Patterns (Chapter 3)
1. `abstract-factory` — Abstract Factory — Chapter 3 introduction (the maze example summarised), Abstract Factory — `gofkit/classes` view `factory` — the creational problem; families of related products; consequences: isolates concrete classes, makes exchanging families easy, promotes consistency, makes new kinds of product hard; factories as singletons; the lab: families × kinds, a new family against a new kind.
2. `builder` — Builder — Builder — `gofkit/classes` view `explosion` — separating construction from representation; Director and Builder; consequences: varying the internal representation, isolating construction code, finer control; Builder against Abstract Factory; the lab: construction processes × representations as one class per pair against directors and builders.
3. `factory-method` — Factory Method — Factory Method — `gofkit/classes` view `factory` (scheme `factory-method`) — letting subclasses decide which class to instantiate; hooks for subclasses; connecting parallel class hierarchies; parameterized factory methods; the cost that a creator subclass may be needed just to make one product; the lab: a creator hierarchy and a product hierarchy, the classes a new product adds.
4. `prototype` — Prototype — Prototype — `dddkit/identity` view `sharing` — creating by copying a prototypical instance; a prototype manager; shallow versus deep copy; the lab: clones of a prototype that share a mutable part (shallow) against clones with their own (deep), how many see a change made through one.
5. `singleton` — Singleton — Singleton — `gofkit/proxy` view `access` (schemes `fresh` and `lazy`) — one instance and a global point of access; consequences: controlled access, reduced name space, refinement by subclassing, a variable number of instances, more flexible than class operations; the lab: a sequence of requests for a shared resource, instances created when each request makes a new one and when one instance is created lazily and reused.
6. `creational-discussion` — Discussion of Creational Patterns — Discussion of Creational Patterns — `gofkit/classes` view `factory` (all three schemes) — the two ways to parameterize a system by the classes it creates (subclass the creator; compose with an object that knows the classes); the book's comparison on its drawing-editor example, summarised; the lab: one design under Factory Method, Abstract Factory and Prototype, the classes each needs and each change adds.

### Course 4 — Structural Patterns (Chapter 4)
1. `adapter` — Adapter — Chapter 4 introduction, Adapter — `gofkit/classes` view `explosion` (or `cckit/deps` `coupling`, author's choice) — converting an interface clients expect; class adapter versus object adapter and their trade-offs (a class adapter cannot adapt a class and all its subclasses; an object adapter can, but overriding adaptee behaviour is harder); pluggable and two-way adapters; the lab: adaptees with subclasses, adapter classes under each scheme.
2. `bridge` — Bridge — Bridge — `gofkit/classes` view `explosion` — decoupling an abstraction from its implementation so the two vary independently; the "proliferation of classes" the motivation shows; consequences; the lab: abstractions × implementations, subclasses per combination against the bridge, and what one new implementation adds.
3. `composite` — Composite — Composite — `gofkit/tree` view `compose` — part–whole hierarchies treated uniformly; transparency versus safety in declaring child operations; explicit parent references; caching; the lab: a tree of parts and an aggregate operation, calls and total, and the leaves asked to add a child.
4. `decorator` — Decorator — Decorator — `gofkit/route` view `wrap` — attaching responsibilities dynamically; a flexible alternative to subclassing; "lots of little objects"; a decorator and its component are not identical; changing the skin versus the guts (Decorator against Strategy); the lab: a component in a stack of decorators, the call order and result, and the classes the same options need as subclasses.
5. `facade` — Facade — Facade — `cckit/deps` view `coupling` — a unified interface to a subsystem; shielding clients, weak coupling, and not preventing direct use; the lab: clients depending on a subsystem's classes directly and through a facade, the dependencies across the boundary.
6. `flyweight` — Flyweight — Flyweight — `gofkit/share` view `flyweight` — sharing to support many fine-grained objects; intrinsic versus extrinsic state; the flyweight factory; the storage saving as a function of the number of flyweights, the intrinsic state per object, and whether extrinsic state is computed or stored; the lab: objects, distinct intrinsic states, storage without sharing and with.
7. `proxy` — Proxy — Proxy — `gofkit/proxy` view `access` — a surrogate that controls access: remote, virtual, protection proxies and smart references; copy-on-write; the lab: requests to costly subjects under eager creation and through virtual proxies, and a protection proxy's refusals.
8. `structural-discussion` — Discussion of Structural Patterns — Discussion of Structural Patterns: Adapter versus Bridge, Composite versus Decorator versus Proxy — `gofkit/classes` view `explosion` — patterns that look alike in structure and differ in intent; when each is applied in a design's life; the lab: one varying design read three ways, classes under each.

### Course 5 — Behavioral Patterns I: Requests, Languages and Traversal (Chapter 5, first six)
1. `chain-of-responsibility` — Chain of Responsibility — Chapter 5 introduction, Chain of Responsibility — `gofkit/route` view `chain` — decoupling sender and receiver; reduced coupling, added flexibility, and receipt not guaranteed; representing requests; the lab: an ordered chain of handlers and a stream of requests, the handler that takes each, the hops, and the requests no one handles.
2. `command` — Command — Command — `gofkit/history` view `undo` — a request as an object: parameterizing, queuing, logging, undoing; the receiver, invoker and client; how intelligent a command should be; undo, redo and hysteresis; macro commands; the lab: commands, undos and redos, the stacks and the state, and the redo history a new command discards.
3. `interpreter` — Interpreter — Interpreter — `gofkit/expr` view `interpret` — a class per grammar rule; abstract syntax trees; easy to change and extend, hard to maintain for complex grammars; the lab: a small arithmetic language of the lesson's own, an expression's tree, its value in a context, nodes by class and interpret calls.
4. `iterator` — Iterator — Iterator — `gofkit/tree` view `traverse` — sequential access without exposing representation; external versus internal iterators; who defines the traversal; robust iterators; the lab: one tree, its pre-order, post-order and level-order traversals.
5. `mediator` — Mediator — Mediator — `dddkit/context` view `protocol` — encapsulating how objects interact; consequences: limits subclassing, decouples colleagues, simplifies object protocols, abstracts cooperation, centralizes control (and the mediator itself can become a monolith); the lab: n colleagues connected pairwise against through one mediator, connections to build and to change. The lesson's prose says the protocol view's words "context" and "translator" read as "colleague" and "connection".
6. `memento` — Memento — Memento — `gofkit/history` view `undo` (scheme `snapshot` against `inverse`) — capturing internal state without violating encapsulation; narrow and wide interfaces; the cost of mementos; storing incremental changes; the lab: one sequence of commands, the state stored as full snapshots against inverse operations.

### Course 6 — Behavioral Patterns II: Notification, State and Algorithms, and the Conclusion (Chapter 5, last five; Chapter 6)
1. `observer` — Observer — Observer — `gofkit/notify` view `observer` — a one-to-many dependency; abstract coupling, broadcast, unexpected updates; who triggers the update; push versus pull; specifying modifications of interest; the change manager; the lab: subjects, observers and the operations that change them, updates sent directly and through a change manager, and the redundant updates it saves.
2. `state` — State — State — `gofkit/machine` view `states` — behaviour that changes with internal state; localizing state-specific behaviour, explicit transitions, sharable state objects; who defines transitions; the lab: a machine of the lesson's own (a vending machine, a parcel locker), the trace over a sequence of events, and the branches a single conditional needs against the classes of State.
3. `strategy` — Strategy — Strategy — `cckit/code` view `complexity` (or `gofkit/classes` `explosion`) — a family of interchangeable algorithms; an alternative to subclassing; eliminating conditional statements; clients must know the strategies; communication overhead; optional strategies. Names *Domain-Driven Design*'s "Strategy and Composite in the Model" lesson. The lab: the decision points of a method choosing an algorithm by a flag, against the same method calling a strategy.
4. `template-method` — Template Method — Template Method — `gofkit/route` view `template` — an algorithm's skeleton in an operation, steps deferred to subclasses; the "Hollywood principle"; primitive operations versus hooks; minimizing primitives; the lab: a template's steps, the subclasses' overrides, the sequence each subclass runs and the primitive operations each must supply.
5. `visitor` — Visitor — Visitor — `gofkit/tree` view `visit` — operations on an object structure without changing its classes; double dispatch; adding operations is easy, adding element classes is hard; accumulating state; breaking encapsulation; who is responsible for traversal; the lab: a structure, two visitors, the calls, and the classes each kind of addition changes.
6. `behavioral-discussion` — Discussion of Behavioral Patterns — Discussion of Behavioral Patterns: encapsulating variation, objects as arguments, should communication be encapsulated or distributed?, decoupling senders and receivers, summary — `dddkit/context` view `protocol` (or `gofkit/notify`, author's choice) — what each behavioral pattern encapsulates; Observer against Mediator; senders and receivers decoupled four ways (Command, Observer, Mediator, Chain of Responsibility); the lab: one interaction designed as a distributed protocol against a centralized one.
7. `conclusion` — What to Expect from Design Patterns — Chapter 6: What to Expect from Design Patterns (a common design vocabulary, a documentation and learning aid, an adjunct to existing methods, a target for refactoring), A Brief History, The Pattern Community, An Invitation, A Parting Thought — `dddkit/modules` view `change` — the refactoring life cycle (prototyping, expansionary and consolidating phases); patterns as targets for refactoring; the lab: a design before and after a consolidation that introduces one pattern, the modules each change touches.

## §D The new kit: `gofkit`

Built the way `dddkit` was (`docs/domain-driven-design/kit-contract.md`), on
`eakit_core`; it may import and reuse `dddkit.mode_lab`, `vrec`, `expr` and
`DDD_CORE_JS` rather than copy them, if the panel intro, status caution and
error prefix can be set per kit; otherwise copy the minimum. One pure JS
`<prefix>Compute(view, inst, opts)` per mode returning `{tiles, status,
table}` or `{refuse}`; a Python `check` per view mirroring every JS refusal;
presets with `expect`; listed in `build_paths.KITS_WITH_EXPECTATIONS`;
mathcheck cases in `scripts/mathcheck.js`, each seen to fail when its function
is broken. Two modules: `gofkit.py` (entry point + family A) and
`gofkit_b.py` (family B), with a seam contract
`docs/design-patterns/kit-contract.md` (family A writes it first) and a report
for authors `docs/design-patterns/kit-report.md`, both in the shape of
dddkit's.

Id prefixes: three letters beginning `g`, as listed below; family A's
engineer greps `scripts/mathpath/labs/*.py` and `scripts/*.js` for every one
before starting and changes any that collide, announcing the change at the top
of the contract. Shared helpers begin `gof` / `GOF_`.

Everything is exact counting and exact rational arithmetic (`RATIONAL_JS`);
nothing typed is evaluated as script; names are letters, digits, `.`, `_`,
`-`. Each view's rules sentence says what is counted and how ties and orders
go. Every status line ends with the same caution in a few words: "the count
is of the design stated".

The panel intro, unless a lesson overrides it: "A count over the small design
the lesson states. The lab counts one consequence of applying a pattern or
not; whether the pattern fits is weighed in the book, against what in the
design is expected to vary."

**Family A (`gofkit.py`)**: classes and structures.

| mode (prefix) | views | input | tiles (at least) |
|---|---|---|---|
| `classes` (gcl) | `explosion` | `aspects`: records `aspect, variant₁, …, variantₖ` (2–4 aspects, 1–8 variants each); `added` (optional: an aspect that gains one variant) | combinations (product of the variant counts); classes with one subclass per combination (product + 1 abstract base); classes with one hierarchy per aspect joined by composition (sum of variant counts + one abstract class per aspect; the first aspect's hierarchy is the one the client holds); the ratio; with `added`: classes the new variant adds under each design (product of the other aspects' counts against 1); the table: aspect, variants, classes it contributes under each design |
|  | `factory` | `families` (names), `kinds` (names of product kinds); `scheme` `abstract-factory`/`factory-method`/`prototype`; `change` `family`/`kind`/none | concrete products (families × kinds); classes in the design: abstract-factory = 1 abstract factory + families concrete factories + kinds abstract products + families × kinds concrete products; factory-method = 1 abstract creator + one creator subclass per concrete product + kinds abstract products + concrete products; prototype = 1 prototype manager (or client) + kinds abstract products + concrete products (no factory classes; a family is a configuration of instances); for `change`: classes added and existing classes changed (abstract-factory, new kind: kinds-wide — 1 abstract product + families concrete products added; 1 + families factory classes changed; new family: 1 factory + kinds products added, 0 changed; factory-method: per new product 1 product + 1 creator subclass; prototype: products added, 0 factory classes, 1 configuration changed); the rules sentence states every formula |
| `tree` (gtr) | `compose` | `nodes`: records `node, parent, kind, value` (parent `-` for the root, exactly one root; kind a class name; value a decimal for leaves, `-` for composites); `asks` (optional: nodes asked to add a child) | nodes; leaves; composites; depth; calls the operation makes (one per node: each composite forwards to each child); the total (sum of leaf values, exact); per composite subtotal (table); child operations asked of leaves (refused under the "safety" declaration, a no-op or an error under "transparency"; `declare` cfg `safe`/`transparent`) |
|  | `traverse` | `nodes` as above (children in record order) | pre-order; post-order; level-order (breadth-first); nodes; the position of a named `find` node in each order (optional) |
|  | `visit` | `nodes` as above; `visitors` (names of operations, 1–4); `adding` `operation`/`kind`/none | accept calls (one per node per visitor); visit calls (one per node per visitor, by kind: table kind × visitor); element classes; visitor classes; methods in all (kinds × visitors visit methods + kinds accept); for `adding`: classes changed with Visitor (new operation: 1 class added, 0 changed; new kind: 1 class added and every visitor changed) against operations on the elements (new operation: every element class changed; new kind: 1 class added, 0 changed) |
| `expr` (gex) | `interpret` | `expr`: an arithmetic expression of the lesson's own grammar — integers and decimals, variables (names), `+ - * /`, unary minus, parentheses, standard precedence, left-associative (the kit's own parser; nothing evaluated as script); `context`: records `name, value` | value (exact rational; division by zero refused with the subexpression); nodes; nodes by class (Number, Variable, Add, Subtract, Multiply, Divide, Negate — the lab's own class names); interpret calls (one per node); depth; variables used; unbound variables refused by name; the table: each node in post-order with its value |

**Family B (`gofkit_b.py`)**: requests, notifications, history, states, sharing.

| mode (prefix) | views | input | tiles (at least) |
|---|---|---|---|
| `route` (grt) | `chain` | `handlers`: records `handler, topic₁, …` in chain order (topics the handler takes; a handler with `*` takes everything; with `-` none); `requests`: list of topics | requests; handled (per handler count, table); hops in all (a request handled by the k-th handler passed k − 1 times); unhandled requests (listed); the busiest handler; per-request trace in the table |
|  | `wrap` | `core`: records `name, value` (one component and its base value); `layers`: records `decorator, op, amount` innermost first, op `add`/`times`/`then` (`then` appends a word to a text result instead — choose one result kind per instance: numeric ops or text ops, not mixed); `order` optional reorder | call order (enter outer … core … exit outer, as a list); result (exact); layers; the result with the layers in reverse order and whether order matters here; subclasses needed for every combination of the options as subclasses (2ⁿ − 1 with n options, plus the base) against n + 2 classes with Decorator (component interface, concrete component, abstract decorator… state the formula used in the rules sentence) |
|  | `template` | `steps`: records `step, kind` in order, kind `fixed`/`primitive`/`hook`; `subclasses`: records `subclass, step₁, …` (the steps it overrides) | per subclass: the sequence it runs (each step as `base` or `own`); primitive operations each subclass must supply and which are missing (refused as "abstract" with the names); hooks overridden; steps written once in the base; lines of the algorithm duplicated if each subclass wrote it whole (steps × subclasses) against with the template |
| `notify` (gno) | `observer` | `subjects` (names); `observers`: records `observer, subject₁, …` (the subjects it observes); `operations`: records `operation, subject₁, …` (the subjects one operation changes, in order); `scheme` `direct`/`managed` | changes; notifications sent (direct: one per change per observer of that subject; managed: one per observer per operation that changed any subject it observes); updates per observer (table: operation × observer); redundant updates (direct minus managed); observers never notified |
| `history` (ghi) | `undo` | `state`: records `cell, value` (the initial state: named whole numbers); `commands`: records `command, op, cell, amount` with op `set`/`add`; `script`: a list of `do:<command>`, `undo`, `redo`; `scheme` `inverse`/`snapshot` | the state after each step (table); undo stack and redo stack at the end (names); undos refused (nothing to undo) and redos refused; redo entries discarded by a new command; stored values: inverse (one old value per `set`, 0 for `add`, which is undone by subtracting) against snapshot (all cells per executed command); final state |
| `machine` (gsm) | `states` | `states` (names; first is the start); `events` (names); `transitions`: records `state, event, next` (at most one per state and event); `input`: a list of events | final state; the trace (state, event, next; table); events ignored (no transition from the current state); transitions defined; branches a single conditional needs (states × events it distinguishes: one per defined transition plus one default per state, stated in the rules) against classes with State (one per state + the context + the abstract state); states never reached |
| `share` (gsh) | `flyweight` | `objects`: records `object, key` (key the intrinsic state's name; objects sharing a key can share one flyweight); `intrinsic` bytes per object (whole), `extrinsic` bytes per object (whole); `extrinsic_stored` yes/no | objects; flyweights (distinct keys); storage without sharing (objects × (intrinsic + extrinsic)); storage with sharing (flyweights × intrinsic + objects × extrinsic if stored, else flyweights × intrinsic only); saved; the share saved (exact percent); objects per flyweight (largest, smallest) |
| `proxy` (gpx) | `access` | `subjects`: records `subject, cost` (whole cost to create or load); `requests`: records `client, subject` in order; `scheme` `eager`/`lazy`/`fresh` (eager: create every subject at start; lazy: create a subject on its first request and reuse it; fresh: create on every request); optional `rights`: records `client, subject₁, …` (a protection proxy refuses any other request) | requests; refused (protection); creations; cost at start; cost in all; subjects never requested (created anyway under eager); instances alive at the end; the first request's cost |

**Never**: judge or grade a design; carry a book example as data; run typed
text as script; print a figure the inputs do not determine.

## §E Package, text, quoting

Package `content/design_patterns/`, one directory per course (§B), each with
`__init__.py` (COURSE dict, same fields as
`content/domain_driven_design/c1_model_to_work/__init__.py`) and `part_a.py`
(and `part_b.py` past five lessons). Spoken forms in
`content/spoken/design_patterns.py`, one block per course.

**The text** is the operator's copy, extracted privately outside the
repository (see `docs/design-patterns/AUTHORING.md`). Cite by chapter,
section and pattern name in prose, never by page; source comments give the
PDF page of the operator's copy (`# PDF p. N of the operator's copy`). The
book is in copyright: never copy any stretch of it into the repository, the
project files or a report.

**Quoting**: one opening quotation of at most 40 words, at most 60 words of
quotation per lesson, character for character. Never reproduce the book's
code (C++ or Smalltalk), structure diagrams, interaction diagrams, tables or
examples' data. A pattern's Intent is paraphrased, never copied, except as the
lesson's counted quotation. Pattern names are the book's, in title case
(Abstract Factory, Chain of Responsibility, Template Method); participant
names are the book's generic ones (Subject, Observer, ConcreteObserver,
Component, Decorator) where the lesson names roles, which is not copying.

**Overlap scan**: no run of 8+ consecutive words shared with the book except
titles, pattern names, section titles and counted quotations.

## §F Voice

The read-along for a working programmer reading the book. Each lesson: which
sections, what problem the pattern solves, the argument in the lesson's own
words, the pattern stated as the reader would apply it, the book's motivating
example summarised in two or three sentences, then the lab on a design written
for the lesson, a worked example by hand, and a quiz whose distractors are
each arguable-for and wrong. Credit the book to "the authors" or "Gamma,
Helm, Johnson and Vlissides" (the "Gang of Four" may be used as the book's
well-known nickname). The book's code is C++ and Smalltalk; the lessons' code
is Java 8, at most twenty lines a block, written for the lesson, and a lesson
says once (course 1) that the book's own samples are C++ and Smalltalk. Be
fair to the book's judgements: each pattern's liabilities are stated beside
its benefits (Singleton's, Visitor's, Abstract Factory's new-kinds problem,
Decorator's many little objects, Mediator's monolith), and the warning of
§1.8 that a pattern should not be applied indiscriminately is the closing
note of course 1 and recurs where it bites. Where the book is of its time
(1995: C++ without templates in common use, Smalltalk, no Java), say so in a
sentence when a reader would otherwise be puzzled; do not editorialize
against the book.

## §G What is left out, and why

- The Preface, Foreword and Guide to Readers: pointed to, not taught.
- Appendix A (Glossary), B (Guide to Notation), C (Foundation Classes) and the
  Bibliography: pointed to. The Glossary may be cited for a definition; the
  notation (OMT) is described in words where a lesson needs it.
- The book's diagrams, code, sample code and example data (copyright, §E).
