# Domain-Driven Design, Read Along — the build specification

The curriculum, lab and authoring contract for the sixteenth Subject: a
read-along of Eric Evans, *Domain-Driven Design: Tackling Complexity in the
Heart of Software* (Boston: Addison-Wesley, 2004; ISBN 0-321-12521-5), its
seventeen chapters and conclusion in the book's own order, one lesson per
pattern or per group of sections. The operator asked for it "the same way as
the previous ones", all the way to live.

It is built the way *Code Complete* (`docs/code-complete/PLAN.md`),
*Patterns of Enterprise Application Architecture*
(`docs/enterprise-patterns/PLAN.md`) and *Introduction to Algorithms*
(`docs/intro-algorithms/PLAN.md`) were, and adopts their conventions by
reference wherever this one is silent: Enterprise Patterns' §E (package,
quoting, author's checklist), §F (voice) and §R lessons. Read before this:
`AGENTS.md` §0, §1, §1a, §7, §8; `content/AGENTS.md`;
`docs/enterprise-patterns/AUTHORING.md`.

**This Subject is the closest neighbour of Enterprise Application Patterns.**
Evans and Fowler share vocabulary — Entity, Value Object, Service, Repository,
Layered Architecture, Specification — and Fowler's book is in the library. A
lesson that meets a pattern Enterprise Patterns already teaches (Layered
Architecture, Value Object, Service Layer, Repository, Domain Model) names that
lesson by title once, says in a sentence where Evans's emphasis differs (Evans
asks what the concept *means in the domain*; Fowler asks how it *maps to the
database and the layers*), and never repeats its prose. The labs reuse
`cckit` and `eakit` modes where they fit (§C names them) and one new kit,
`dddkit` (§D), counts what the others cannot.

Contents: §0 the one question · §A PATH · §B courses · §C every lesson ·
§D the new kit · §E package, text, quoting · §F voice · §G left out

---

## §0 The one question: what does the reader compute?

Evans's book is a book of judgements, not of formulas, and it would be easy to
answer "nothing". But every one of his judgements is about something a reader
can count on a small model written down in front of them, and the book itself
argues by pointing at exactly those things:

1. **Words.** How many translations a conversation needs between the experts'
   terms, the developers' terms and the names in the code; which word means two
   things; which concept has two names; which term in one Bounded Context is a
   false cognate of the same term in another (Chapters 2, 9, 14).
2. **References and boundaries.** Which associations must be traversed both
   ways and which can be one-way; which outside references bypass an aggregate
   root; what a delete removes; which concurrent edits break an invariant that
   spans objects, under object locks and under aggregate locks (Chapters 5, 6).
3. **Equality and sharing.** Which pairs of objects are "the same" by identity
   and which by value, where the two disagree; how many holders see a change
   made through a shared mutable value (Chapter 5, Chapter 10).
4. **Rules as objects.** Which candidates a SPECIFICATION selects and which
   clause rejects the rest; whether one specification subsumes another
   (Chapters 9, 10).
5. **Dependencies and change.** How many modules a change touches when the
   modules follow the concepts and when they follow something else; which
   dependencies run up a layering; how far a change in an upstream context
   reaches down a context map, and how many translators it costs (Chapters 4,
   5, 10, 14, 15, 16).
6. **Effort.** What share of the effort and of the strongest developers goes
   to the CORE DOMAIN and what share to GENERIC SUBDOMAINS (Chapter 15).
7. **Money that must balance.** Balances from entries, transactions that do not
   balance, and the entries a posting rule derives (Chapter 11's analysis
   patterns).

**What the lab never does** is score a design. Every count is of the small
model the lesson states, and a count shows one consequence of one choice; it
is not a verdict on the choice, which the book makes by weighing the domain,
the team and the project. The material clause (§A) says so, and every lesson
closes on that gap.

## §A PATH fields (`content/domain_driven_design/__init__.py`)

```
"slug": "domain-driven-design",
"title": "Domain-Driven Design, Read Along",
"level": "Intermediate",
"level_note": "you can read a short Java class and have worked on a program someone else will change",
"speech": "code",
```

Catalog: `short_title` `"Domain-Driven Design"`, `"kind": "Read along"`, last
in the computing group (after Introduction to Algorithms), card: "Eric
Evans&rsquo;s <em>Domain-Driven Design</em>, pattern by pattern, with each
modelling choice counted on a small model: translations, references,
conflicts, modules touched and effort shared." Extend the computing group's
note with Domain-Driven Design beside Code Complete and Enterprise Application
Patterns ("assume only that you can read a short routine"). Course slug prefix
`ddd-`; check-id prefix `ddd`; package `domain_driven_design` → slug
`domain-driven-design` needs no `PACKAGE_OF_SLUG` entry. `"speech": "code"`
(backtick runs and code blocks read by the code dialect, as on Code Complete
and Enterprise Patterns).

**material** (unique; required by `TestGeneratedPathIsCurrent`):
"every figure on this path is counted in your browser from the small model a
lesson states &mdash; its terms, objects, references, edits, modules and
contexts &mdash; and a count shows one consequence of one modelling choice; it
is not a verdict on the choice, which depends on the domain, the team and the
project."

tagline / description: written by course 1's author from the final counts
(`test_the_tagline_and_description_state_the_real_counts`). The tagline names
the book with `<em>`, says each pattern's consequence is counted on a small
model, and ends "Nine courses and N lessons are available."

## §B The nine courses

| # | slug | title | Part, chapters | lessons | module dir |
|---|---|---|---|---|---|
| 1 | `ddd-putting-the-model-to-work` | Putting the Domain Model to Work | I, 1–3 | 5 | `c1_model_to_work` |
| 2 | `ddd-building-blocks` | The Building Blocks of a Model-Driven Design | II, 4–5 | 7 | `c2_building_blocks` |
| 3 | `ddd-life-cycle` | The Life Cycle of a Domain Object | II, 6–7 | 6 | `c3_life_cycle` |
| 4 | `ddd-implicit-concepts` | Breakthroughs and Implicit Concepts | III, 8–9 | 5 | `c4_implicit_concepts` |
| 5 | `ddd-supple-design` | Supple Design | III, 10 | 7 | `c5_supple_design` |
| 6 | `ddd-patterns-and-refactoring` | Analysis Patterns, Design Patterns and Refactoring | III, 11–13 | 4 | `c6_patterns_and_refactoring` |
| 7 | `ddd-model-integrity` | Maintaining Model Integrity | IV, 14 | 8 | `c7_model_integrity` |
| 8 | `ddd-distillation` | Distillation | IV, 15 | 5 | `c8_distillation` |
| 9 | `ddd-large-scale-structure` | Large-Scale Structure and Strategy | IV, 16–17, Conclusion | 6 | `c9_large_scale_structure` |

53 lessons. Part II and Part III are split because each holds more than one
course's worth: Part II's building blocks (4–5) and life cycle with its
extended example (6–7); Part III's breakthrough and implicit concepts (8–9),
supple design (10), and the three short chapters 11–13. Part IV's three large
chapters are a course each, with Chapter 17 and the Conclusion closing the
last. The operator's copy has no Preface and no Part introductions (§E); the
Part names are the book's.

Modules (the `module` field) are the book's chapter titles, e.g.
`"Chapter 6 · The Life Cycle of a Domain Object"`.

## §C Every lesson

Format: slug — Title — chapter and sections (PDF pages of the operator's copy)
— lab `kit/mode` view — focus. Instances are the lesson's own: **never the
book's example domains as lab data** (no PCB nets, no cargo and voyages, no
syndicated loans and shares, no paint mixing, no chemical warehouse, no
purchase-order approval limit, no payroll and pension). The book's examples are
summarised in prose, where the chapter's argument runs through them, and named
by section; each lab works a different domain written for the lesson (a
library, a clinic, a bakery's orders, a bike-share, a theatre box office, a
seed bank, a school timetable, a freight-free one of your own).

A lesson may switch to a different existing view if the one named cannot show
its focus; it says so in the author's report.

### Course 1 — Putting the Domain Model to Work (Part I, Chapters 1–3)
1. `crunching-knowledge` — Crunching Knowledge — Ch 1: opening story, Ingredients of Effective Modeling, Knowledge Crunching, Continuous Learning (2–8) — `dddkit/lang` view `glossary` — the five ingredients; knowledge crunching as a team activity with feedback, against the one-way waterfall hand-off; the lab: experts' and developers' first vocabularies for one domain, the synonyms a model consolidates, the translations left.
2. `knowledge-rich-design-and-deep-models` — Knowledge-Rich Design and Deep Models — Ch 1: Knowledge-Rich Design, Deep Models (8–11) — `dddkit/spec` view `validate` — a business rule buried in a method versus the same rule made an explicit object of the model (the book's overbooking example summarised); the lab: a booking policy as an explicit specification, which requests it admits and which clause refuses the rest.
3. `ubiquitous-language` — The Ubiquitous Language — Ch 2: Ubiquitous Language, Modeling Out Loud, One Team, One Language (12–19) — `dddkit/lang` view `glossary` — the cost of translation; the language as the model's vocabulary used in speech, writing and code; changes to the language as changes to the model; the lab: three audiences (experts, developers, code), translations a conversation needs, ambiguous terms.
4. `documents-and-explanatory-models` — Documents, Diagrams and Explanatory Models — Ch 2: Documents and Diagrams, Written Design Documents, Explanatory Models (19–25) — `dddkit/lang` view `glossary` — diagrams as anchors for conversation, not the model; documents that complement code and speech, and the test that a document still earns its keep; the lab: a design document's terms against the code's names, the stale ones.
5. `model-driven-design-and-hands-on-modelers` — Model-Driven Design and Hands-On Modelers — Ch 3: Model-Driven Design, Modeling Paradigms and Tool Support, Letting the Bones Show, Hands-On Modelers (25–35) — `dddkit/modules` view `change` — one model for analysis and design; the code as an expression of the model; why the modeler must code; the lab: model concepts mapped to code modules, the modules each model change reaches with the model in the code and with a separate analysis model.

### Course 2 — The Building Blocks of a Model-Driven Design (Part II, Chapters 4–5)
1. `layered-architecture` — Layered Architecture — Ch 4: Layered Architecture, Relating the Layers, Architectural Frameworks, The Domain Layer Is Where the Model Lives (36–41) — `dddkit/modules` view `layers` — the four layers; a layer depends only downward; upward communication through callbacks or OBSERVER; the lab: classes assigned to layers, the dependencies that run upward. Names *Enterprise Patterns*' Layering lesson.
2. `the-smart-ui-anti-pattern` — The Smart UI "Anti-Pattern" — Ch 4: The Smart UI "Anti-Pattern", Other Kinds of Isolation (41–43) — `dddkit/modules` view `change` — when Smart UI is the right choice and why it excludes model-driven design; the lab: a rule copied into three screens against the same rule in one domain class, the places each rule change touches.
3. `associations` — Associations — Ch 5: Associations (45–49) — `dddkit/assoc` view `simplify` — imposing a traversal direction, adding a qualifier, eliminating nonessential associations; the lab: the references to maintain before and after the three moves.
4. `entities` — Entities — Ch 5: Entities (a.k.a. Reference Objects), Modeling Entities, Designing the Identity Operation (49–54) — `dddkit/identity` view `equality` — an object defined by its continuity and identity rather than its attributes; the lab: pairs that are the same thing and pairs that only look alike, where attribute equality and identity disagree.
5. `value-objects` — Value Objects — Ch 5: Value Objects, Designing Value Objects, Designing Associations That Involve Value Objects (54–59) — `dddkit/identity` view `sharing` — immutability, sharing and copying; the lab: holders sharing one value, how many see a change made through one of them when the value is mutable and when it is replaced. Names *Enterprise Patterns*' Value Object lesson.
6. `services` — Services — Ch 5: Services, Services and the Isolated Domain Layer, Granularity, Access to Services (59–62) — `cckit/deps` view `coupling` — the three marks of a good service; application, domain and infrastructure services; the lab: an operation forced onto an entity against the same operation as a domain service, the uses and fan-in each design has. Names *Enterprise Patterns*' Service Layer lesson.
7. `modules-and-modeling-paradigms` — Modules and Modeling Paradigms — Ch 5: Modules (a.k.a. Packages), Agile Modules, The Pitfalls of Infrastructure-Driven Packaging, Modeling Paradigms (62–69) — `dddkit/modules` view `cohesion` — modules as part of the model, low coupling and high cohesion of concepts; the lab: one model packaged two ways, dependencies inside and across modules.

### Course 3 — The Life Cycle of a Domain Object (Part II, Chapters 6–7)
1. `aggregates` — Aggregates — Ch 6: Aggregates (71–79), the rules — `dddkit/aggregate` view `boundary` — root, boundary, the rules: outside objects hold references only to the root, the root checks invariants, a delete removes the whole; the lab: objects, roots and references, the references that bypass a root, what a delete removes.
2. `aggregate-invariants-and-locking` — Aggregate Invariants and Concurrent Change — Ch 6: Aggregates, the invariant-spanning example and its locking discussion (71–79) — `dddkit/aggregate` view `lock` — why locking single objects lets two edits together break a rule that spans the aggregate; the lab: concurrent edits under object locks and under aggregate locks, commits, refusals and whether the invariant holds after. Names *Enterprise Patterns*' Coarse-Grained Lock lesson.
3. `factories` — Factories — Ch 6: Factories, Choosing Factories and Their Sites, Designing the Interface, Where Does Invariant Logic Go?, Entity Factories Versus Value Object Factories, Reconstituting Stored Objects (79–86) — `dddkit/spec` view `validate` — creation as a separate responsibility; atomic creation of a whole aggregate; a factory that refuses an invalid object; the lab: requests to create an object, which the factory's invariants admit and which clause refuses.
4. `repositories` — Repositories and Relational Databases — Ch 6: Repositories, Querying a Repository, Client Code Ignores Repository Implementation, Implementing a Repository, Working Within Your Frameworks, The Relationship with Factories, Designing Objects for Relational Databases (86–95) — `dddkit/spec` view `select` — the illusion of an in-memory collection of aggregate roots; specification-based queries; the lab: a repository asked for the roots that satisfy a specification. Names *Enterprise Patterns*' Repository lesson.
5. `an-extended-example` — Using the Language: An Extended Example — Ch 7: Introducing the System, Isolating the Domain, Entities and Values, Associations, Aggregate Boundaries, Selecting Repositories, Walking Through Scenarios, Object Creation (96–106) — `dddkit/aggregate` view `boundary` — how the building blocks are chosen one after another on one model (the book's shipping example, summarised); the lab: the same decisions taken on a model written for the lesson.
6. `refactoring-the-example-and-modules` — Refactoring the Example, Modules and a New Feature — Ch 7: Pause for Refactoring, Modules in the Model, Introducing a New Feature, A Final Look (106–114) — `dddkit/modules` view `cohesion` — the alternative aggregate design; packaging by concept rather than by pattern; a new feature integrated through a translating service; the lab: one model packaged by pattern (entities, values, services) and by concept.

### Course 4 — Breakthroughs and Implicit Concepts (Part III, Chapters 8–9)
1. `breakthrough` — Breakthrough — Ch 8: Story of a Breakthrough, Opportunities, Focus on Basics, Epilogue (115–122) — `eakit/money` view `allocate` — continuous refactoring preparing for a breakthrough; the decision to take it; the deeper model's concept of shares, summarised; the lab: an amount divided by shares under different rounding rules, what a share concept makes explicit (a domain of the lesson's own).
2. `digging-out-concepts` — Digging Out Concepts — Ch 9: Listen to Language, Scrutinize Awkwardness, Contemplate Contradictions, Read the Book, Try, Try Again (123–132) — `dddkit/lang` view `glossary` — the five ways of finding a concept the model is missing; the lab: the terms the experts use that name no class in the code.
3. `constraints-and-processes` — Explicit Constraints and Processes as Domain Objects — Ch 9: How to Model Less Obvious Kinds of Concepts — Explicit Constraints, Processes as Domain Objects (132–137) — `cckit/code` view `complexity` — a constraint buried in a method against the same constraint factored into its own method or object; a process the experts talk about as a domain object; the lab: the decision points of a Java method with the constraint inline and factored out.
4. `specification` — Specification — Ch 9: Specification (137–141) — `dddkit/spec` view `validate` — a predicate-like value object that states whether an object satisfies criteria; the lab: one object checked against a specification, clause by clause.
5. `applying-specification` — Applying and Implementing Specification — Ch 9: Applying and Implementing Specification: Validation, Selection (Querying), Generation (Building to Order) (141–146) — `dddkit/spec` view `select` — the three uses; selection from a repository; building to order; the lab: a set of candidates, which a specification selects and why each of the rest fails.

### Course 5 — Supple Design (Part III, Chapter 10)
1. `intention-revealing-interfaces` — Intention-Revealing Interfaces — Ch 10: opening, Intention-Revealing Interfaces (147–152) — `cckit/code` view `names` — names that state effect and purpose, not means; the lab: a Java class's declared names read against what they reveal.
2. `side-effect-free-functions` — Side-Effect-Free Functions — Ch 10: Side-Effect-Free Functions (152–156) — `dddkit/identity` view `sharing` — commands and queries separated; logic moved into value objects; the lab: a change made through a shared value, mutable and immutable.
3. `assertions` — Assertions — Ch 10: Assertions (156–159) — `dddkit/spec` view `validate` — post-conditions and invariants stated so that a reader need not trace the implementation; the lab: an operation's post-condition and an invariant checked as a specification.
4. `conceptual-contours` — Conceptual Contours — Ch 10: Conceptual Contours (159–163) — `dddkit/modules` view `change` — decomposing along the domain's own lines so that changes stay local; the lab: change requests against two decompositions, modules each change touches.
5. `standalone-classes-and-closure` — Standalone Classes and Closure of Operations — Ch 10: Standalone Classes, Closure of Operations (163–166) — `cckit/deps` view `ripple` — concepts a reader must hold to understand a class; operations whose result type is their argument type; the lab: what a class depends on, directly and in all.
6. `declarative-design` — Declarative Design — Ch 10: Declarative Design, Domain-Specific Languages, A Declarative Style of Design, Extending Specifications in a Declarative Style (166–174) — `dddkit/spec` view `subsume` — combining specifications with and, or and not; subsumption; the lab: two specifications, whether one subsumes the other, and the candidates that separate them.
7. `angles-of-attack` — Angles of Attack — Ch 10: Angles of Attack — Carve Off Subdomains, Draw on Established Formalisms, When You Can (174–180) — `dddkit/modules` view `cohesion` — carving off a subdomain; a formalism such as arithmetic of shares; the lab: a tangled model and the same model with a subdomain carved off.

### Course 6 — Analysis Patterns, Design Patterns and Refactoring (Part III, Chapters 11–13)
1. `analysis-patterns` — Applying Analysis Patterns — Ch 11: opening, Example: Earning Interest with Accounts (181–186) — `dddkit/ledger` view `balance` — an analysis pattern as a model to draw on; Fowler's accounts and entries; the lab: entries posted to accounts, balances, and transactions that do not balance (a domain of the lesson's own).
2. `posting-rules` — Posting Rules and the Nightly Batch — Ch 11: Example: Insight into the Nightly Batch, Analysis Patterns Are Knowledge to Draw On (186–190) — `dddkit/ledger` view `post` — posting rules that derive entries; the batch understood through the model; the lab: rules that fire on entries and the entries they derive.
3. `strategy-and-composite` — Strategy and Composite in the Model — Ch 12: Strategy (a.k.a. Policy), Composite, Why Not Flyweight? (191–200) — `cckit/code` view `complexity` — a design pattern used as a domain pattern when it names a domain concept; the lab: the decision points of a conditional policy against the same choice as interchangeable policies.
4. `refactoring-toward-deeper-insight` — Refactoring Toward Deeper Insight — Ch 13: Initiation, Exploration Teams, Prior Art, A Design for Developers, Timing, Crisis as Opportunity (201–204) — `dddkit/modules` view `change` — refactoring driven by domain insight rather than code smells; when to refactor; the lab: change requests before and after a refactoring that makes a concept explicit.

### Course 7 — Maintaining Model Integrity (Part IV, Chapter 14)
1. `bounded-context` — Bounded Context — Ch 14: opening, Bounded Context, Recognizing Splinters Within a Bounded Context (205–211) — `dddkit/lang` view `cognates` — one model per context, with an explicit boundary; duplicate concepts and false cognates; the lab: two teams' glossaries, the concepts with two names and the names with two meanings.
2. `continuous-integration` — Continuous Integration — Ch 14: Continuous Integration (211–213) — `dddkit/lang` view `cognates` — integration of code and of concepts within one context; the lab: one context's glossary as two halves of a team drift apart, the splinters a merge shows.
3. `context-map` — Context Map — Ch 14: Context Map, Testing at the Context Boundaries, Organizing and Documenting Context Maps (213–219) — `dddkit/context` view `map` — naming every context and the relationships between them; the lab: contexts and their relationships, what a change in one reaches.
4. `shared-kernel-and-customer-supplier` — Shared Kernel and Customer/Supplier Teams — Ch 14: Relationships Between Bounded Contexts, Shared Kernel, Customer/Supplier Development Teams (219–224) — `dddkit/context` view `map` — a shared subset changed only by agreement; upstream and downstream teams with acceptance tests; the lab: a change in the upstream context and the downstream contexts that must change with each relationship.
5. `conformist-and-anticorruption-layer` — Conformist and Anticorruption Layer — Ch 14: Conformist, Anticorruption Layer (224–230) — `dddkit/context` view `map` — adopting the upstream model wholesale versus translating at a boundary; facade, adapter, translator; the lab: one upstream change, the models that change when downstream conforms, and the translators that change when it does not.
6. `separate-ways-open-host-and-published-language` — Separate Ways, Open Host Service and Published Language — Ch 14: Separate Ways, Open Host Service, Published Language (230–234) — `dddkit/context` view `protocol` — no integration at all; one protocol for many consumers; a shared, documented language; the lab: n contexts integrating point to point against through one published language, translators to build and to change.
7. `unifying-an-elephant` — Unifying an Elephant and Choosing a Strategy — Ch 14: Unifying an Elephant, Choosing Your Model Context Strategy (234–242) — `dddkit/lang` view `cognates` — partial models of one thing and what unifying them takes; team decisions, the external systems, the system under design; the lab: four glossaries of one thing, the overlaps and the conflicts.
8. `transformations` — Transformations — Ch 14: Transformations — Merging Contexts, Separate Ways → Shared Kernel, Shared Kernel → Continuous Integration, Phasing Out a Legacy System, Open Host Service → Published Language (242–246) — `dddkit/context` view `map` — moving a relationship along the spectrum; the lab: one map before and after a transformation, what a change reaches in each.

### Course 8 — Distillation (Part IV, Chapter 15)
1. `core-domain` — Core Domain — Ch 15: opening, Core Domain, Choosing the Core, Who Does the Work?, An Escalation of Distillations (247–252) — `dddkit/distill` view `effort` — the part of the model that distinguishes the system and justifies building it; putting the best developers there; the lab: subdomains with their kind and effort, the share of effort and of the strongest developers on the core.
2. `generic-subdomains` — Generic Subdomains — Ch 15: Generic Subdomains, Generic Doesn't Mean Reusable, Project Risk Management (252–257) — `dddkit/distill` view `effort` — the four options (off the shelf, published model, outsourced, in house); the lab: the same subdomains with the generic ones bought or published, effort moved.
3. `domain-vision-statement-and-highlighted-core` — Domain Vision Statement and Highlighted Core — Ch 15: Domain Vision Statement, Highlighted Core, The Distillation Document, The Flagged Core, The Distillation Document as Process Tool (257–261) — `dddkit/distill` view `effort` — a one-page statement of the core's value; making the core visible in the model; the lab: model elements flagged core, the share of the model a newcomer must read.
4. `cohesive-mechanisms` — Cohesive Mechanisms — Ch 15: Cohesive Mechanisms, Generic Subdomain Versus Cohesive Mechanism, When a Mechanism Is Part of the Core Domain (261–264) — `dddkit/modules` view `change` — a complicated computation separated behind an intention-revealing interface; the lab: changes to the computation and to the domain rules, modules each touches with the mechanism tangled and separated.
5. `segregated-and-abstract-core` — Segregated Core, Abstract Core and Refactoring Targets — Ch 15: Distilling to a Declarative Style, Segregated Core, The Costs of Creating a Segregated Core, Abstract Core, Deep Models Distill, Choosing Refactoring Targets (264–272) — `dddkit/modules` view `cohesion` — refactoring the core into its own module; abstract interfaces at the core; the lab: the core's classes mixed with supporting ones and segregated, dependencies across the core's boundary.

### Course 9 — Large-Scale Structure and Strategy (Part IV, Chapters 16–17, Conclusion)
1. `evolving-order-and-system-metaphor` — Evolving Order and System Metaphor — Ch 16: opening, Evolving Order, System Metaphor (272–277) — `dddkit/modules` view `change` — structure that evolves with the system rather than being fixed up front; a metaphor's benefits and risks; the lab: changes against a structure imposed up front and one evolved with them.
2. `responsibility-layers` — Responsibility Layers — Ch 16: Responsibility Layers, Choosing Appropriate Layers (277–288) — `dddkit/modules` view `layers` — layers of responsibility (potential, operations, decision support, policy, commitment); the lab: classes assigned to responsibility layers, dependencies that run the wrong way.
3. `knowledge-level` — Knowledge Level — Ch 16: Knowledge Level (288–294) — `dddkit/modules` view `change` — a group of objects that describes how another group should behave; the lab: new types added as subclasses and as knowledge-level data, modules each addition touches.
4. `pluggable-component-framework` — Pluggable Component Framework and Fitting Structure — Ch 16: Pluggable Component Framework, How Restrictive Should a Structure Be?, Refactoring Toward a Fitting Structure, Minimalism, Communication and Self-Discipline, Restructuring Yields Supple Design, Distillation Lightens the Load (294–300) — `dddkit/context` view `protocol` — components that plug into an abstract core through one interface; the lab: n components integrating pairwise against through one framework interface.
5. `bringing-the-strategy-together` — Bringing the Strategy Together — Ch 17: Combining Large-Scale Structures and Bounded Contexts, Combining Large-Scale Structures and Distillation, Assessment First (301–305) — `dddkit/distill` view `effort` — structure across contexts; the core within the structure; assessing first; the lab: a team's effort across contexts and subdomains.
6. `who-sets-the-strategy` — Who Sets the Strategy, and a Conclusion — Ch 17: Who Sets the Strategy?, Six Essentials for Strategic Design Decision Making; Conclusion: Epilogues, Looking Forward (305–314) — `dddkit/context` view `map` — emergent structure from the team and an architecture team close to development; the six essentials; the book's epilogues; the lab: one context map read by the reader's own project.

## §D The new kit: `dddkit`

Built on `eakit_core` exactly as `itakit` is (copy its `mode_lab` pattern:
import `eakit_core` as `ea`; one pure JS `<prefix>Compute(view, inst, opts)`
per mode returning `{tiles, status, table}` or `{refuse}`; a Python `check` per
view mirroring every JS refusal; presets with `expect`; listed in
`build_paths.KITS_WITH_EXPECTATIONS`; mathcheck cases in `scripts/mathcheck.js`,
each seen to fail when its function is broken). Two modules: `dddkit.py`
(entry point + family A) and `dddkit_b.py` (family B), with a seam contract
`docs/domain-driven-design/kit-contract.md` in the shape of
`docs/intro-algorithms/kit-contract.md`. Report for authors:
`docs/domain-driven-design/kit-report.md`, same shape as
`docs/intro-algorithms/kit-report.md`.

Id prefixes: three letters beginning `d`, as listed below; family A's engineer
greps `scripts/mathpath/labs/*.py` for every one before starting and changes
any that collide, announcing the change at the top of the contract. Shared
helpers begin `ddd` / `DDD_`.

Everything is exact counting and exact rational arithmetic (`RATIONAL_JS`);
nothing typed is evaluated as script; names are `ea.NAME`-shaped (letters,
digits, `.`, `_`, `-`). Each view's rules sentence says what is counted and
how ties and orders go. Every lab ends its status line with the same caution
in a few words: the count is of the model stated.

The panel intro, unless a lesson overrides it: "A count over the small model
the lesson states. The lab counts one consequence of one modelling choice; the
choice itself is weighed in the book, against the domain, the team and the
project."

**Family A (`dddkit.py`)**: words, objects and rules.

| mode (prefix) | views | input | tiles (at least) |
|---|---|---|---|
| `lang` (dln) | `glossary` | `audiences` (2–4 names, from cfg or preset, e.g. `experts developers code`); `terms`: records `concept, name₁, …, nameₖ` one name per audience (`-` = that audience has no name for it) | concepts; concepts named alike by every audience; translations a conversation needs (for each concept, each pair of audiences whose names differ, counted once per pair); names missing (audience: concepts it cannot name); ambiguous names (a name one audience uses for two or more concepts); the table: concept × audience with "differs" marks |
|  | `cognates` | two or more glossaries (`contexts`: records `context, term, meaning`, meaning a short name of the concept) | contexts; terms; shared terms; false cognates (same term, different meanings, with the contexts); duplicate concepts (one meaning, different terms, with the terms); terms safe to share (same term, same meaning in every context that has it) |
| `assoc` (das) | `simplify` | `assocs`: records `a, b, ends, direction, qualified` with ends `1-1`, `1-n`, `n-1`, `n-n`; direction `both`, `a-b` (only a navigates to b) or `b-a`; qualified `yes`/`no` (a qualifier reduces the many end to one) — and a second list `after` with the same shape or omitted | for before and after: associations; navigable directions (2 for both, 1 otherwise); references to keep consistent when one link changes (2 for both ways, 1 for one way); many-to-many associations; many ends; the reductions (before − after) |
| `identity` (did) | `equality` | `objects`: records `name, id, attrs` (attrs `k=v; …` or a single text token list); `pairs` to compare (records `x, y`; optional: every pair if omitted, n ≤ 12) | pairs compared; same by identity; same by attributes; where they disagree (two lists: same thing, different attributes — "changed"; different things, same attributes — "look-alikes") |
|  | `sharing` | `holders`: records `holder, value`; `value`: the shared value's name; `change` (holder through which it is changed); `kind` `mutable`/`immutable` | holders of the value; holders that see the change (mutable: all holders of that value; immutable: the one whose reference was replaced); holders surprised (saw a change they did not make); new values created |
| `aggregate` (dag) | `boundary` | `objects`: records `object, aggregate, root` (root `yes` for exactly one per aggregate); `refs`: records `from, to` (`from` may be an outside name not in objects: an outside holder); `delete` (an object, optional) | aggregates; objects; references that cross a boundary; of those, references to a non-root (violations, listed); objects a delete of the root removes (the whole aggregate); a delete of a non-root refused with reason; dangling references a delete would leave |
|  | `lock` | `items`: records `item, value` in one aggregate; `limit` (the invariant: sum of item values ≤ limit), `edits`: records `minute, user, item, new value` (each user reads at minute 0 and commits at their last minute); `scheme` `object`/`aggregate` | committed users; refused users; final values; final sum; invariant holds (yes / no: sum S over limit L); edits lost. Object scheme: each user locks only items edited; conflicts only on the same item. Aggregate scheme: the first user to edit takes the whole aggregate; others refused. |
| `spec` (dsp) | `validate`, `select`, `subsume` | `fields` declared per record (`candidates`: records `name, k=v; …` with numeric or word values); `spec` (and a second `other` for subsume): an expression over clauses `attr op value` with op `= != < <= > >=`, combined with `and`, `or`, `not` and parentheses (the kit's own parser; nothing evaluated as script) | validate (one candidate): satisfied yes/no, clauses true, the first false clause (in source order), every false clause; select: candidates, satisfying (names), failing (each with its first false clause); subsume: on the candidates, A ⊇ B (every candidate satisfying B satisfies A) yes/no with the counter-examples; for pure conjunctions of numeric comparisons and word equalities, the exact logical answer as well (interval containment per attribute), "not decidable by the lab" otherwise |

**Family B (`dddkit_b.py`)**: dependencies, contexts, effort and money.

| mode (prefix) | views | input | tiles (at least) |
|---|---|---|---|
| `modules` (dmo) | `cohesion` | `elements`: records `element, module` (one or two assignments: `module` and optional `module2` column, so one view compares two packagings); `deps`: records `from, to` | for each packaging: modules; dependencies inside modules; across modules; the share inside; module-level cycles (listed); the most coupled pair of modules |
|  | `change` | `elements` as above (one or two packagings); `changes`: records `change, element` (a change touches each element listed) | for each packaging: changes; modules touched per change (listed); total module touches; changes confined to one module; the largest |
|  | `layers` | `layers`: names top to bottom (cfg or preset); `elements`: records `element, layer`; `deps`: records `from, to` | dependencies; downward; within a layer; upward (violations, listed); skipping a layer (allowed, counted); layers with no element |
| `context` (dcx) | `map` | `contexts`: names; `rels`: records `upstream, downstream, kind` with kind `shared-kernel`, `customer-supplier`, `conformist`, `acl`, `ohs`, `published-language`, `separate-ways` (only the book's kinds; any other word refused; `separate-ways` has no edge effect); `changed` (a context whose model changes) | relationships; downstream contexts reached (transitively along edges whose kind propagates); models that must change (shared-kernel both ways, conformist and customer-supplier downstream propagate; acl and ohs/published-language stop at the translator); translators to update (acl and ohs edges at the first hop); contexts untouched; the table: each relationship, what the change does there |
|  | `protocol` | `n` contexts (whole 2–60) or a list of names; `scheme` `pairwise`/`published` | translators to build (pairwise: n·(n − 1) one-way, or n·(n − 1)/2 two-way, per cfg `directed` yes/no; published: n, one per context to and from the language); translators to change when one context's model changes (pairwise: 2·(n − 1) or n − 1; published: 1); the ratio |
| `distill` (dds) | `effort` | `parts`: records `part, kind, weeks, strong` with kind `core`/`supporting`/`generic`, weeks a whole number of developer-weeks, strong the number of the team's strongest developers on it; optional `option` column for generic parts (`build`/`buy`/`published`/`outsource`; only `build` counts weeks) | total weeks; share on core; share on generic; strongest developers on core / in all; generic parts built in house; weeks a decision to buy or publish would free; the table |
| `ledger` (dle) | `balance` | `entries`: records `txn, account, amount` (signed decimals, cents exact) | accounts; balances (account: amount, in record order); transactions; unbalanced transactions (txn: net); total of all entries |
|  | `post` | `entries` as above; `rules`: records `rule, from, to, share` (share a decimal 0–1: when an entry posts to `from`, the rule posts share × amount to `to` and the negative back to `from`, rounded to cents half away from zero, once — rules do not fire on derived entries) | entries given; entries derived; balances after; derived entries listed; rounding left (exact share − rounded, summed) |

**Never**: score or grade a design; carry a book example as data; run typed
text as script; print a figure the inputs do not determine.

## §E Package, text, quoting

Package `content/domain_driven_design/`, one directory per course (§B), each
with `__init__.py` (COURSE dict, same fields as
`content/enterprise_patterns/c2_domain_logic/__init__.py`) and `part_a.py`
(and `part_b.py` past five lessons). Spoken forms in
`content/spoken/domain_driven_design.py`, one block per course.

**The text** is the operator's copy, extracted privately outside the
repository (see `docs/domain-driven-design/AUTHORING.md`). It is a 324-page
PDF with no Preface and no Part introductions; cite by chapter, section and
pattern name in prose, never by page; source comments give the PDF page of the
operator's copy (`# PDF p. N of the operator's copy`). The book is in
copyright: never copy any stretch of it into the repository, the project files
or a report.

**Quoting** (Enterprise Patterns §E.3): one opening quotation of at most 40
words, at most 60 words of quotation per lesson, character for character. Never
reproduce the book's code listings, diagrams, dialogues, tables or examples'
data; a pattern's boxed statement (the bold problem/solution paragraphs) is
paraphrased, never copied, except as the lesson's counted quotation. Pattern
names are the book's (in the book they are in small capitals; write them in
title case in prose, e.g. Bounded Context, Anticorruption Layer).

**Overlap scan**: no run of 8+ consecutive words shared with the book except
titles, pattern names, section titles and counted quotations. The scanner is
in AUTHORING.md.

## §F Voice

The read-along for a working programmer reading the book. Each lesson: which
sections, what problem the chapter sets out, the argument in the lesson's own
words, the pattern stated as the reader would apply it, the book's example
summarised in two or three sentences when the argument runs through it, then
the lab on a model written for the lesson, a worked example by hand, and a quiz
whose distractors are each arguable-for and wrong. Credit the book to "Evans";
where a section is drawn from another author (Chapter 11's analysis patterns
are Fowler's; Chapter 12 cites the Gang of Four), say so. Code is Java 8, at
most twenty lines a block, written for the lesson. Be fair to the book's
judgements: Evans says when a pattern is not worth its cost (Smart UI, a
Segregated Core's costs, Separate Ways), and the lesson says it too.

## §G What is left out, and why

- The Preface and the Part introductions: not in the operator's copy; their
  substance is restated in the chapters.
- The Appendix (The Use of Patterns in This Book), Glossary and References:
  pointed to, not taught. The Glossary may be cited for a definition.
- The book's diagrams, dialogues, code and example data (copyright, §E).
- Photo credits.
