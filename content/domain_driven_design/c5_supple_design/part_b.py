"""Supple Design, lessons 6-7 -- Chapter 10.

Eric Evans, Domain-Driven Design (Addison-Wesley, 2004), Chapter 10, Supple
Design: Declarative Design, Domain-Specific Languages, A Declarative Style of
Design, Extending Specifications in a Declarative Style; and Angles of Attack,
with its Shares Math example. Pages in the comments are PDF pages of the
operator's copy; the lessons cite by chapter, section and pattern. Every
quotation is copied from that copy and checked with quotes.py. The code and the
lab models are written for these lessons: the book's warehouse, loan and share
examples are summarised in prose only. The design is
docs/domain-driven-design/PLAN.md, section C, Course 5.
"""

from .part_a import MODULE, _DDD_INTRO, _lines


# ---------------------------------------------------------------- snippets

# 5.6 Declarative Design: presets tightened, loosened, with-or; exercise.
SPEC_COMBINATORS = """// Java 8: a specification whose and, or and not are closed under Spec.
interface Spec<T> {
    boolean isSatisfiedBy(T candidate);

    default Spec<T> and(Spec<T> other) {
        return c -> isSatisfiedBy(c) && other.isSatisfiedBy(c);
    }
    default Spec<T> or(Spec<T> other) {
        return c -> isSatisfiedBy(c) || other.isSatisfiedBy(c);
    }
    default Spec<T> not() {
        return c -> !isSatisfiedBy(c);
    }
}"""

STORAGE_RULES = """old rule:  moisture <= 8 and temp <= -10
new rule:  moisture <= 6 and temp <= -18 and sealed = yes"""

OLD_RULE = "moisture <= 8 and temp <= -10"
NEW_RULE = "moisture <= 6 and temp <= -18 and sealed = yes"
OR_RULE = "(moisture <= 6 and sealed = yes) or temp <= -25"

SEED_LOTS = [
    ["lotA", "moisture=5", "temp=-20", "sealed=yes"],
    ["lotB", "moisture=7", "temp=-20", "sealed=yes"],
    ["lotC", "moisture=5", "temp=-12", "sealed=yes"],
    ["lotD", "moisture=5", "temp=-20", "sealed=no"],
    ["lotE", "moisture=9", "temp=-20", "sealed=yes"],
]

CONCESSION_EXERCISE = """loyalMember:     visits >= 10 and member = yes
regularVisitor:  visits >= 6"""


# 5.7 Angles of Attack: presets tangled-and-carved; exercise.
QUANTITY = """// The carved-off arithmetic: an amount in a unit, closed under plus.
final class Quantity {
    private final long amount;
    private final Unit unit;
    Quantity(long amount, Unit unit) {
        this.amount = amount;
        this.unit = unit;
    }
    Quantity plus(Quantity other) {
        long same = Conversion.convert(other.amount, other.unit, unit);
        return new Quantity(amount + same, unit);
    }
    Quantity times(int batches) {
        return new Quantity(amount * batches, unit);
    }
}"""

BATCH_CLIENT = """// In BatchPlan: the flour for a day's bake, read as a definition.
Quantity flour = recipe.flourPerBatch().times(batches)
        .plus(starter.flourToFeed());"""

BAKERY_ELEMENTS = [
    # element, tangled packaging, carved packaging
    ["Order", "orders", "orders"],
    ["OrderLine", "orders", "orders"],
    ["Product", "orders", "orders"],
    ["Customer", "orders", "orders"],
    ["Recipe", "production", "production"],
    ["Ingredient", "production", "production"],
    ["BatchPlan", "production", "production"],
    ["Oven", "production", "production"],
    ["Quantity", "orders", "quantities"],
    ["Conversion", "orders", "quantities"],
    ["Unit", "production", "quantities"],
]

BAKERY_DEPS = [
    ["Order", "OrderLine"], ["Order", "Customer"], ["OrderLine", "Product"],
    ["OrderLine", "Quantity"], ["Recipe", "Product"], ["Recipe", "Ingredient"],
    ["Ingredient", "Quantity"], ["BatchPlan", "OrderLine"], ["BatchPlan", "Recipe"],
    ["BatchPlan", "Oven"], ["BatchPlan", "Quantity"], ["Quantity", "Unit"],
    ["Quantity", "Conversion"], ["Conversion", "Unit"],
]

CLINIC_EXERCISE = """Appointment -> Patient, Clinician, TimeSlot
Rota        -> Clinician, TimeSlot
TimeSlot    -> Duration
Clinician   -> Duration
tangled:  booking = Appointment, Patient, TimeSlot
          staff   = Clinician, Rota, Duration
carved:   booking = Appointment, Patient
          staff   = Clinician, Rota
          time    = TimeSlot, Duration"""


LESSONS = [
    # ---------------------------------------------------------------- 06
    # Chapter 10, Declarative Design (PDF pp. 166-167 of the operator's copy),
    # Domain-Specific Languages (p. 167), A Declarative Style of Design (p. 168),
    # Extending Specifications in a Declarative Style (pp. 168-174): logical
    # operators (pp. 168-170), "only AND" (p. 170), the alternative
    # implementation (p. 171), subsumption (pp. 171-173), Socrates (p. 174).
    # Quotes: PDF p. 168, 18 words, and PDF p. 170, 13 words; quotes.py OK.
    # Lesson total: 31 words. Course 5's modern aside: Java 8's Predicate.
    {
        "slug": "declarative-design",
        "title": "Declarative Design",
        "module": MODULE,
        "one_line": "Let a precise description of a rule control the software, and see how far the chapter's patterns take a specification toward it: combined with and, or and not, and compared by subsumption.",
        "summary": (
            "Declarative design promises a program that is its own specification, and "
            "Evans has seen many attempts at it trap the model in the limits of a "
            "framework. Read his account of its pitfalls, "
            "of domain-specific languages, and of the declarative style a supple design "
            "makes possible; then ask whether one storage rule subsumes another, and find "
            "the candidates that separate them."
        ),
        "key": [
            "a declaration that controls the software",
            "frameworks that trap the model: a risk",
            "and, or, not are closed under specs",
            "implement only and, if that is enough",
            "subsumes: every match of it matches the other",
            "or and not make subsumption hard",
        ],
        "key_label": "Declarative Design in six lines",
        "concepts_intro": (
            "Three terms carry the lesson. The first two are Evans's, the third the lab's."
        ),
        "concepts": [
            ("Declarative design",
             "Writing a program, or part of one, as a kind of executable specification: a "
             "precise description of properties that actually controls the software, "
             "through reflection or code generation, so that the declaration can be taken "
             "at face value."),
            ("Subsumption",
             "A more stringent specification subsumes a less stringent one: anything that "
             "satisfies it satisfies the other too, so it could take the other's place "
             "without dropping a requirement. Viewed as predicates, it is logical "
             "implication."),
            ("A separating candidate",
             "A candidate that satisfies one specification and not the other. The lab "
             "checks the candidates it is given; one separating candidate disproves "
             "subsumption, and none among those given proves nothing on its own."),
        ],
        "read_title": "The promise, its pitfalls, then two rules compared",
        "read_intro": (
            "Read the sections Declarative Design, Domain-Specific Languages, A "
            "Declarative Style of Design and Extending Specifications in a Declarative "
            "Style in Chapter 10 first. The lesson reads them as an argument, then "
            "compares two specifications on a set of candidates."
        ),
        "body": [
            ("p", "&ldquo;A supple design can make it possible for the client code to use a "
                  "declarative style of design.&rdquo; That is from A Declarative Style of "
                  "Design, in Chapter 10. This lesson reads it with the sections around it, "
                  "from Declarative Design to Extending Specifications in a Declarative "
                  "Style. Read them in your own copy first; the Specification lesson of the "
                  "course Breakthroughs and Implicit Concepts set out the pattern they "
                  "extend."),
            ("p", "Evans begins with what the other patterns cannot do. Assertions help, "
                  "but handwritten code can always have a side effect nobody excluded, "
                  "and much code is boilerplate that adds no meaning and buries the model. "
                  "Declarative design answers with a precise description that actually "
                  "controls the software, through reflection or through code generated "
                  "from the declaration, so that another developer can take it at face "
                  "value. He calls generating a running program from the model's properties "
                  "a kind of Holy Grail, and names two problems he has met more than once: "
                  "a declaration language that cannot say everything needed inside a "
                  "framework that makes it hard to go beyond it, and code generation that "
                  "mixes generated and handwritten code so that regenerating destroys work. "
                  "The common result, he says, is a model dumbed down to fit the tool."),
            ("p", "Rule engines are declarative in principle, but control predicates added "
                  "for performance bring side effects back, so that reordering rules can "
                  "change results. Many declarative approaches fail when developers go "
                  "round them. The greatest value he has seen comes from a narrowly scoped "
                  "framework that automates one tedious, error-prone part of a design, "
                  "object-relational mapping for one, and leaves the rest free. "
                  "Domain-specific languages make the strongest link to the Ubiquitous "
                  "Language, but refining the model then means changing a language, which "
                  "takes skills a team, and the team after it, may lack; he notes that in a "
                  "functional language such as Scheme the style comes without splitting the "
                  "system in two."),
            ("p", "Then the turn. A design with intention-revealing interfaces, functions "
                  "and assertions is already edging into declarative territory: its "
                  "elements say what they mean and have known effects or none. The book "
                  "shows it on Specification, which is an adaptation of the predicate. "
                  "Predicates combine with and, or and not, and those operations are closed "
                  "under predicates, so combined specifications show Closure of Operations. "
                  "Below is the idea in Java 8, written for this lesson: each combinator "
                  "returns a new `Spec` and changes nothing."),
            ("code", _lines(SPEC_COMBINATORS)),
            ("p", "Evans is careful about cost. His own implementation is meant to explain, "
                  "and on one project a more elaborate version made millions of small "
                  "objects that slowed an object database, so he shows another that encodes "
                  "the expression and interprets it. Often the full set is not needed, and "
                  "and is used far more than the others: "
                  "&ldquo;Don't be afraid to implement only AND, if that is all you "
                  "need.&rdquo; Java 8 itself now gives `java.util.function.Predicate` the "
                  "methods `and`, `or` and `negate`, so the combinators come free; the next "
                  "operation does not."),
            ("p", "Subsumption, which Evans says is seldom needed and hard to implement, "
                  "compares two specifications. His case is a regulation that tightens: the "
                  "users want the kinds of goods whose handling became more stringent, and "
                  "validating today's stock will miss any kind not now in stock. A stricter "
                  "specification subsumes a looser one if everything satisfying it satisfies "
                  "the other. Proving it in general is hard; special cases are easy. A "
                  "threshold specification compares thresholds, and with and alone one "
                  "conjunction subsumes another when its clauses include all of the other's. "
                  "With or and not the proofs become much harder, and he advises choosing: "
                  "forgo some operators or forgo subsumption."),
            ("p", "The lab's model is a seed bank written for this lesson, whose storage "
                  "rule has been tightened, and five stored lots, `lotA` to `lotE`. One "
                  "warning before you run it. The lab never says subsumes, because the word "
                  "runs both ways: its rules note that logicians say the looser rule "
                  "subsumes the stricter, while Evans says the stricter subsumes the looser. "
                  "Its tiles ask one plain question: does A accept every candidate B "
                  "accepts? A yes means, in Evans's words, that B subsumes A. So to ask "
                  "Evans's question, whether the new rule subsumes the old, enter the old "
                  "rule as A and the new one as B. The lab's counter-examples are the separating "
                  "candidates of this lesson: they satisfy B and fail A."),
            ("code", _lines(STORAGE_RULES)),
            ("p", "On the preset <code>tightened</code>, A is the old rule and B the new. "
                  "Only `lotA` satisfies B, while 4 lots, `lotA` to `lotD`, satisfy A; "
                  "`lotA` satisfies both, so there are 0 counter-examples. Both rules are "
                  "conjunctions of comparisons, so the lab also gives the logical answer, "
                  "yes, for every candidate and not only these five: a moisture of at most "
                  "6 is at most 8, a temperature at most −18 is at most −10, and the old "
                  "rule asks nothing about sealing. In Evans's terms, the new rule subsumes "
                  "the old."),
            ("p", "On the preset <code>loosened</code> the rules swap places, which asks "
                  "whether the old rule subsumes the new. No: 3 counter-examples, `lotB`, "
                  "`lotC` and `lotD`, satisfy the old rule and fail the new, each for a "
                  "different clause, and the logical answer says the old rule allows a "
                  "moisture that fails the new rule's clause `moisture <= 6`. `lotE` satisfies neither. Those three "
                  "are the lots whose storage the tightening affects, the partial report "
                  "Evans describes; the logical answer holds whatever happens to be in "
                  "stock."),
            ("p", "On the preset <code>with-or</code>, B is a rule with an or, "
                  "`(moisture <= 6 and sealed = yes) or temp <= -25`. Of the five lots, "
                  "`lotA` and `lotC` satisfy it, and both satisfy the old rule, so there are "
                  "0 counter-examples among them; but B is not a pure conjunction, and the "
                  "lab says the logical answer is not decidable by it. The answer is in fact "
                  "no: a sealed lot at moisture 4 kept at 0 degrees satisfies B and fails "
                  "the old rule. Add it as `lotF` and the lab finds it."),
            ("h3", "Exercise"),
            ("code", _lines(CONCESSION_EXERCISE)),
            ("p", "Two rules for a theatre's loyalty discount. Say which rule subsumes the "
                  "other in Evans's sense, and give one candidate that satisfies one rule "
                  "and not the other. Then enter the rules and a few candidates in the lab, "
                  "including yours, minding which rule goes in as A. Separate candidates "
                  "with semicolons, as in `ann, visits=12, member=yes; bo, visits=3, "
                  "member=no`."),
            ("p", "The specification became declarative by drawing on a formalism, logic. "
                  "The last lesson of the chapter, Angles of Attack, makes that a strategy."),
        ],
        "lab": ("dddkit", {
            "mode": "spec",
            "view": "subsume",
            "candidates": SEED_LOTS,
            "preset": "tightened",
            "presets": [
                {"id": "tightened",
                 "label": "A old, B new: does the new rule subsume the old?",
                 "spec": OLD_RULE, "other": NEW_RULE,
                 "expect": {"dspSatB": "1: lotA", "dspSatA": "4: lotA, lotB, lotC, lotD",
                            "dspCounter": "0: none",
                            "dspLogical": "yes: every clause of A follows from B’s clauses"}},
                {"id": "loosened",
                 "label": "A new, B old: does the old rule subsume the new?",
                 "spec": NEW_RULE, "other": OLD_RULE,
                 "expect": {"dspSatB": "4: lotA, lotB, lotC, lotD", "dspSatA": "1: lotA",
                            "dspOnCands": "no: 3 of the 4 that satisfy B fail A",
                            "dspCounter": "3: lotB, lotC, lotD"}},
                {"id": "with-or",
                 "label": "A old, B a rule with an or",
                 "spec": OLD_RULE, "other": OR_RULE,
                 "expect": {"dspSatB": "2: lotA, lotC", "dspCounter": "0: none",
                            "dspLogical": "not decidable by the lab: B uses or, and the lab "
                                          "decides only clauses joined by and"}},
            ],
            "panel_title": "Whether one specification subsumes another",
            "panel_intro": _DDD_INTRO,
        }),
        "steps_title": "Comparing two specifications",
        "steps_intro": "Four steps, the last of them on rules of your own.",
        "steps": [
            ("Write both as clauses",
             "Write each rule as clauses joined by and, or and not, each clause an "
             "attribute, a comparison and a value."),
            ("Compare clause by clause",
             "For two conjunctions, check that every clause of the looser rule is implied "
             "by some clause of the stricter one on the same attribute."),
            ("Look for a separating candidate",
             "Write a candidate that satisfies one rule and fails the other, choosing each "
             "attribute at the edge of a clause."),
            ("Do it on rules of your own",
             "Find a rule in a system you know that was tightened, write the old and the "
             "new as specifications, and say whether the new one subsumes the old. Give the "
             "candidate that shows it if it does not."),
        ],
        "worked": {
            "title": "The new rule against the old",
            "intro": [
                "Decide <code>tightened</code> clause by clause, then on the lots.",
            ],
            "lines": [
                "moisture <= 6 implies moisture <= 8",
                "temp <= -18 implies temp <= -10",
                "sealed = yes: the old rule has no clause",
                "every old clause implied: subsumes",
                "lots satisfying new: lotA",
                "lotA satisfies old: no counter-example",
            ],
            "after": [
                "The clause-by-clause comparison is Evans's special case for conjunctions, "
                "extended to compare thresholds. It answers for every possible lot, not "
                "only the five in store.",
            ],
        },
        "quiz_title": "Declarative design and subsumption",
        "quiz": [
            {"q": "In the exercise, which rule subsumes the other in Evans's sense, and "
                  "which candidate separates them?",
             "a": ["loyalMember subsumes regularVisitor; a member with 8 visits satisfies "
                   "only regularVisitor",
                   "regularVisitor subsumes loyalMember; a member with 8 visits satisfies "
                   "only regularVisitor",
                   "loyalMember subsumes regularVisitor; a member with 11 visits satisfies "
                   "only loyalMember",
                   "Neither; a non-member with 12 visits satisfies neither"],
             "c": 0,
             "why": "Anyone satisfying loyalMember has at least 10 visits, so at least 6, "
                    "and satisfies regularVisitor: loyalMember is the stricter rule and, in "
                    "Evans's sense, subsumes regularVisitor. A member with 8 visits "
                    "satisfies regularVisitor only, and so does a non-member with 12. "
                    "Nobody satisfies loyalMember and not regularVisitor. In the lab, enter "
                    "regularVisitor, the looser rule, as A and loyalMember as B; the "
                    "logical answer is yes."},
            {"q": "In Evans's sense, what does it mean that a new specification subsumes "
                  "an old one?",
             "a": ["Every candidate that satisfies the old one satisfies the new one",
                   "Every candidate that satisfies the new one satisfies the old one",
                   "The two select exactly the same candidates",
                   "The new one has fewer clauses than the old"],
             "c": 1,
             "why": "A more stringent specification subsumes a less stringent one: any "
                    "candidate that would satisfy the new one would also satisfy the old, "
                    "so the new could replace the old without dropping a requirement. "
                    "Equal selections are a special case, and clause counts settle nothing."},
            {"q": "For specifications built with and alone, what simple test does Evans "
                  "give for subsumption?",
             "a": ["The subsuming specification's leaves include all the other's leaves",
                   "The subsumed specification's leaves include all the other's",
                   "Both have the same number of leaves",
                   "Every leaf of one is the negation of a leaf of the other"],
             "c": 0,
             "why": "A and B implies A, so a conjunction subsumes another when its leaf "
                    "specifications are a superset of the other's. The lab's clause-by-"
                    "clause comparison extends this to thresholds on one attribute, as his "
                    "parameterised minimum-age example does."},
            {"q": "Which two problems does Evans say he has met more than once with "
                  "attempts at declarative design?",
             "a": ["Programs too slow to run, and declarations too long to read",
                   "A declaration language that cannot say everything needed, in a framework "
                   "hard to extend; and generated code merged with handwritten code so that "
                   "regenerating destroys work",
                   "Domain experts who cannot read the declarations, and developers who "
                   "refuse to write them",
                   "Specifications that cannot be combined, and rules that cannot be ordered"],
             "c": 1,
             "why": "These are the two he lists in Declarative Design, followed by the "
                    "dumbing-down of the model they cause. Performance appears in the rule "
                    "engine's control predicates and in his own composite specification, "
                    "not in that list."},
        ],
        "mistakes": [
            ("Taking declarative design to mean generating the whole program from declarations",
             "Evans calls that a Holy Grail with pitfalls he has met repeatedly, and says "
             "the greatest value he has seen is a narrow framework that automates one "
             "tedious part, such as object-relational mapping. The declarative style he "
             "recommends comes from the chapter's own patterns, as specifications combined "
             "with and, or and not."),
            ("Building every operator because the pattern describes it",
             "Evans says that and is used far more than the others and is simpler to "
             "implement, that one need not be afraid to implement only and, and that using "
             "a pattern does not mean building features you do not need. Subsumption, "
             "especially with or and not, he advises against unless the benefit justifies "
             "the difficulty."),
            ("Reading no separating candidate as proof of subsumption",
             "The lab checks the candidates it is given. On the lesson's illustration, the "
             "rule with an or has no separating candidate among the five lots and still "
             "does not subsume the old rule; a sixth lot shows it. Only for pure "
             "conjunctions does the lab give a logical answer."),
        ],
        "standard": (
            "Finish when you can decide subsumption for two conjunctions and find a "
            "separating candidate.",
            "Given two specifications, say in Evans's sense whether one subsumes the "
            "other, by clauses where both are conjunctions, and give a candidate that "
            "satisfies one and not the other when neither subsumes."
        ),
        "note": (
            "The lab compares two specifications on the candidates given, and decides "
            "subsumption logically only for conjunctions of comparisons and word "
            "equalities. It cannot say whether a declarative framework will serve a "
            "project or trap it; Evans's warnings on that are about teams and tools, "
            "which no count reaches."
        ),
    },
    # ---------------------------------------------------------------- 07
    # Chapter 10, Angles of Attack (PDF pp. 174-180 of the operator's copy): Carve
    # Off Subdomains (p. 174), Draw on Established Formalisms (p. 174), Shares Math
    # (pp. 174-180), the closing paragraphs (p. 180).
    # Quote: PDF p. 174 of the operator's copy, 26 words, quotes.py OK.
    # Lesson total: 26 words.
    {
        "slug": "angles-of-attack",
        "title": "Angles of Attack",
        "module": MODULE,
        "one_line": "You cannot make a whole system supple at once: carve off a subdomain, draw on a formalism people already know, and make one area really supple.",
        "summary": (
            "The chapter ends with how to start. Read Evans's two angles of attack, carving "
            "off subdomains and drawing on established formalisms, and his Shares Math "
            "example, summarised; then count the dependencies inside and across modules of "
            "a bakery's model before and after its quantity arithmetic is carved off."
        ),
        "key": [
            "choose targets; do not spread effort thin",
            "carve off a subdomain, such as its math",
            "what is left is smaller and clearer",
            "draw on a formalism people know",
            "a carved module depends on nothing",
        ],
        "key_label": "Angles of Attack in five lines",
        "concepts_intro": (
            "Three terms carry the lesson. The first two are Evans's angles of attack, the "
            "third the lab's."
        ),
        "concepts": [
            ("Carving off a subdomain",
             "Separating one aspect of a system, such as a piece of specialised arithmetic "
             "or a set of rules about state changes, into a module of its own, worked over "
             "until it is clean. The part left behind is smaller and partly declarative."),
            ("An established formalism",
             "A conceptual system long refined in some field, such as accounting or "
             "mathematics, adapted as part of the model. Evans's favourite is mathematics, "
             "which he finds clean, combinable by clear rules and easy to understand."),
            ("A module-level cycle",
             "In the lab, two or more modules that depend on each other, directly or round "
             "a loop, through the dependencies of their elements. The lab lists every cycle "
             "for each packaging."),
        ],
        "read_title": "Two angles, an example, then a carve counted",
        "read_intro": (
            "Read Angles of Attack, at the end of Chapter 10, first, with its Shares Math "
            "example. The lesson reads the two approaches, summarises the example, and "
            "then counts one model packaged before and after a carve."
        ),
        "body": [
            ("p", "&ldquo;It is more useful to make a big impact on one area, making a part "
                  "of the design really supple, than to spread your efforts thin.&rdquo; That "
                  "is from Carve Off Subdomains, in Angles of Attack, the last section of "
                  "Chapter 10. Read it in your own copy first."),
            ("p", "The chapter has offered a set of techniques, and Evans admits that the "
                  "design they aim at is difficult. Nobody can look at a large system and "
                  "decide to make it supple; targets have to be chosen. He gives two broad "
                  "approaches and then an extended example that brings the chapter's "
                  "patterns together."),
            ("p", "The first is to carve off subdomains. The whole design cannot be taken on "
                  "at once, so pick at it: some part may be viewed as specialised "
                  "mathematics, and can be separated; rules that restrict state changes can "
                  "be pulled into a separate model or a small framework in which they are "
                  "declared. Each step leaves a clean new module and a smaller, clearer "
                  "remainder, part of which is now written declaratively in the terms of the "
                  "carved module. Chapter 15, on distillation, takes up how to choose and "
                  "manage subdomains."),
            ("p", "The second is to draw on established formalisms when you can. A tight "
                  "conceptual framework cannot be invented every day, but many fields have "
                  "systems refined over long periods. Accounting is one that many business "
                  "applications already involve. Evans's favourite is mathematics: many "
                  "domains have a little arithmetic in them somewhere, and he urges the "
                  "reader to look for it and dig it out."),
            ("p", "The example, Integrating the Patterns: Shares Math, returns to the "
                  "syndicated loan system whose breakthrough Chapter 8 told. A payment had "
                  "to be divided among the lenders by their shares, and the first design "
                  "calculated the division and changed the loan in one method. Evans "
                  "separates the query from the command, then finds the missing concept, "
                  "the shares as parts of one whole, first as an object inside the loan's "
                  "aggregate and then as a value object with addition and subtraction closed "
                  "under it and a proration that takes an amount. The loan's methods "
                  "shrink to lines that read like definitions of the business transactions, "
                  "and new transactions are easy to declare."),
            ("p", "He lists what made the design supple: complex logic in immutable values "
                  "whose operations are functions, so they can be combined freely and used "
                  "for analysis as well as for the real transaction; simple commands "
                  "characterised by assertions; concepts decoupled, the value depending "
                  "closely on one other class; and a familiar formalism. An invented "
                  "protocol for shares could have been supple too, he says, but it would "
                  "have had to be invented, which is hard and uncertain, and learnt by "
                  "everyone who met it; arithmetic is already known, and a design kept "
                  "consistent with its rules does not mislead."),
            ("p", "Now a model written for this lesson, a bakery's orders and production. "
                  "Quantities of flour, butter and loaves, their units and the conversions "
                  "between them grew up wherever they were first needed: `Quantity` and "
                  "`Conversion` beside the orders, `Unit` beside production. The carve "
                  "moves those three into a module `quantities` of their own, with the "
                  "arithmetic below, closed under `plus`, and the production code can then "
                  "say what it means."),
            ("code", _lines(QUANTITY)),
            ("code", _lines(BATCH_CLIENT)),
            ("p", "On the preset <code>tangled-and-carved</code> the lab counts both "
                  "packagings of the same 14 dependencies. Tangled, in two modules: 8 "
                  "inside a module, 6 across, a share inside of 4/7, and one module-level "
                  "cycle, `orders` and `production`, because each side holds part of the "
                  "arithmetic the other uses. Carved, in three modules: 9 inside, 5 across, "
                  "a share inside of 9/14, and no cycle. The most coupled pair of modules "
                  "falls from `orders` and `production` with 6 dependencies between them to "
                  "a tie at 2, which the lab gives to the same pair, alphabetically first, "
                  "over `production` and `quantities`. `quantities` depends on no other "
                  "module; three of the 5 dependencies across modules point into it, and the"
                  " other two run from production to orders."),
            ("p", "The share inside rose by one dependency, and that is not what the carve "
                  "was for. What changed is shape: a cycle gone, and a module every other "
                  "one uses and none of whose concepts reach out. Whether it is clean in "
                  "Evans's sense, combinable by clear rules that the bakers would recognise, "
                  "is a question about the arithmetic, which the count cannot ask."),
            ("h3", "Exercise"),
            ("code", _lines(CLINIC_EXERCISE)),
            ("p", "A clinic's model, written for this exercise, with its time arithmetic "
                  "tangled and then carved off. For each packaging give the dependencies "
                  "inside modules, those across, and the module-level cycles. Then enter "
                  "the elements, both packagings and the dependencies in the lab to check, "
                  "separating records with semicolons: elements as `Appointment, booking, "
                  "booking; Patient, booking, booking; …` and dependencies as "
                  "`Appointment, Patient; Appointment, Clinician; …`."),
            ("p", "That ends Part III's chapter on supple design. The next course, Analysis "
                  "Patterns, Design Patterns and Refactoring, opens with Applying Analysis "
                  "Patterns, where the established formalism is Fowler's accounting."),
        ],
        "lab": ("dddkit", {
            "mode": "modules",
            "view": "cohesion",
            "packagings": 2,
            "names": ["tangled", "carved"],
            "preset": "tangled-and-carved",
            "presets": [
                {"id": "tangled-and-carved",
                 "label": "The bakery's model, tangled and with quantities carved off",
                 "elements": BAKERY_ELEMENTS,
                 "deps": BAKERY_DEPS,
                 "expect": {"dmoModules": "2", "dmoInside": "8", "dmoAcross": "6",
                            "dmoShare": "4/7 ≈ 57.1%", "dmoCycles": "1: (orders, production)",
                            "dmoPair": "orders and production: 6",
                            "dmoModules2": "3", "dmoInside2": "9", "dmoAcross2": "5",
                            "dmoShare2": "9/14 ≈ 64.3%", "dmoCycles2": "0: none",
                            "dmoPair2": "orders and production: 2"}},
            ],
            "panel_title": "Dependencies inside and across modules, before and after a carve",
            "panel_intro": _DDD_INTRO,
        }),
        "steps_title": "Choosing a subdomain to carve off",
        "steps_intro": "Four steps, the last of them on a model of your own.",
        "steps": [
            ("Look for the formalism",
             "Find the part of the model that is arithmetic, logic, accounting or another "
             "system with rules people already know."),
            ("Draw its edge",
             "List the elements that belong to it and check that none of them depends on "
             "the rest of the model; where one does, ask whether that dependency is basic."),
            ("Count both packagings",
             "Count dependencies inside and across modules and the module-level cycles, "
             "before and after the carve, and say which way the dependencies across point."),
            ("Do it on a model of your own",
             "Name one piece of a system you know that could be carved off as a formalism, "
             "list its elements, and count the dependencies that would cross into it and "
             "out of it."),
        ],
        "worked": {
            "title": "Five dependencies that cross, carved",
            "intro": [
                "Sort the carved packaging's dependencies across modules by direction.",
            ],
            "lines": [
                "OrderLine to Quantity: orders to quantities",
                "Ingredient to Quantity: production to quantities",
                "BatchPlan to Quantity: production to quantities",
                "Recipe to Product: production to orders",
                "BatchPlan to OrderLine: production to orders",
                "from quantities outward: none",
            ],
            "after": [
                "Three point into `quantities` and two into `orders`, and nothing points "
                "from orders back to production, so no loop. That is the shape Evans "
                "describes: a clean module, and a remainder that uses it.",
            ],
        },
        "quiz_title": "Angles of attack and a carve counted",
        "quiz": [
            {"q": "In the exercise, what are the dependencies inside and across modules, "
                  "and the cycles, tangled and carved?",
             "a": ["Tangled 4 inside, 3 across, one cycle booking and staff; carved 3 inside, "
                   "4 across, no cycle",
                   "Tangled 4 inside, 3 across, no cycle; carved 3 inside, 4 across, no cycle",
                   "Tangled 3 inside, 4 across, one cycle; carved 4 inside, 3 across, no cycle",
                   "Tangled 5 inside, 2 across, one cycle; carved 3 inside, 4 across, one cycle"],
             "c": 0,
             "why": "Tangled: inside are Appointment to Patient and to TimeSlot, Rota to "
                    "Clinician, and Clinician to Duration (4); across are Appointment to "
                    "Clinician and TimeSlot to Duration (booking to staff) and Rota to "
                    "TimeSlot (staff to booking), 3, which make a cycle. Carved: inside are "
                    "Appointment to Patient, Rota to Clinician and TimeSlot to Duration (3); "
                    "the other 4 cross, all toward staff or time, and time depends on "
                    "nothing, so there is no cycle. The share inside falls, and the cycle "
                    "goes."},
            {"q": "On the preset <code>tangled-and-carved</code>, why is there a cycle "
                  "between orders and production in the tangled packaging?",
             "a": ["Because BatchPlan depends on OrderLine",
                   "Because Recipe depends on Product",
                   "Because production uses Quantity, kept in orders, and Quantity and "
                   "Conversion use Unit, kept in production",
                   "Because every packaging with two modules has a cycle"],
             "c": 2,
             "why": "Production depends on orders through Recipe, Ingredient and BatchPlan, "
                    "and orders depends on production only through `Quantity` and "
                    "`Conversion` using `Unit`. The arithmetic split across both sides "
                    "closes the loop; moving all three into one module removes it. "
                    "BatchPlan's and Recipe's dependencies point one way only."},
            {"q": "Where does Evans say effort on supple design is better spent?",
             "a": ["Spread evenly, so that no part of the system is left rigid",
                   "On the framework first, and then on each subdomain in turn",
                   "On one area, made thoroughly supple, rather than on many",
                   "On the parts of the system that change least"],
             "c": 2,
             "why": "In Carve Off Subdomains he says a big impact on one area is more useful "
                    "than effort spread thin, and he points to Chapter 15 for choosing and "
                    "managing subdomains."},
            {"q": "Which disadvantages does Evans give for a wholly original protocol for "
                  "shares, against the arithmetic he used?",
             "a": ["It could not have been made supple, and it would have been slower",
                   "It would have had to be invented, a hard and uncertain task, and learnt "
                   "by each person who met it",
                   "It would have needed a domain-specific language and a code generator",
                   "It would have tied the loan to one database"],
             "c": 1,
             "why": "He grants that an invented protocol could in principle have been made "
                    "supple, and gives exactly two disadvantages: it must be invented, and "
                    "it must be learnt by everyone who deals with it. Arithmetic is already "
                    "known, and kept consistent with its rules it does not mislead."},
        ],
        "mistakes": [
            ("Trying to make the whole design supple at once",
             "Evans says you cannot look at an enormous system and decide to make it supple; "
             "you choose targets and pick away at them, and a big impact on one area is "
             "worth more than effort spread thin. He also says he has never seen a large "
             "program supple throughout."),
            ("Inventing a protocol when an established formalism fits",
             "In Shares Math Evans weighs an invented protocol of financial terms against "
             "arithmetic. It might have been supple, but it would have had to be invented "
             "and then learnt by everyone. A formalism people already know, kept "
             "consistent with its rules, is easy to grasp and does not mislead."),
            ("Reading a higher share of dependencies inside modules as the measure of a carve",
             "On the lesson's illustration the share inside rises only from 8 to 9 of 14, "
             "and in the exercise it falls. What the carve changed is the shape of the "
             "dependencies, a cycle removed and a module that depends on nothing, and "
             "Evans's aim, a clean and combinable module, is a quality of its concepts that "
             "the count does not see."),
        ],
        "standard": (
            "Finish when you can count a model before and after a subdomain is carved off.",
            "Given a model's dependencies and two packagings, give the dependencies inside "
            "and across modules and the module-level cycles of each, and say which way the "
            "dependencies into the carved module point."
        ),
        "note": (
            "The lab counts dependencies by module for the packagings the lesson states. "
            "It cannot say which subdomain is worth carving, or whether a formalism fits "
            "the domain and will be recognised by the people who use it; Evans leaves "
            "that choice to the team, and Chapter 15 returns to it."
        ),
    },
]
