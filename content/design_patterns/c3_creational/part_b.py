"""Creational Patterns, lesson 6 -- Discussion of Creational Patterns.

Gamma, Helm, Johnson and Vlissides, Design Patterns (Addison-Wesley, 1995),
Chapter 3, the closing Discussion of Creational Patterns. Pages in the
comments are PDF pages of the operator's copy; the lesson cites by chapter
and section. Its quotations are copied from that copy and checked with
quotes.py. The book's drawing-editor comparison is summarised in prose; the
lab works a quiz builder's palette written for the lesson. The design is
docs/design-patterns/PLAN.md, section C, Course 3.
"""

from .part_a import _GOF_INTRO, _lines

# A quiz builder's palette: one tool per question type, each creating its own
# kind of question. Four families of one kind each.
PALETTE_FAMILIES = "choice truefalse short match"
PALETTE_KINDS = "question"

THREE_TOOLS_JAVA = """// Three ways to give a palette tool the class it creates.
abstract class Tool {                                   // Factory Method
    protected abstract Question newQuestion();
    final void click(Quiz quiz) { quiz.add(newQuestion()); }
}

interface QuestionFactory { Question make(); }          // Abstract Factory
final class FactoryTool {
    private final QuestionFactory factory;
    FactoryTool(QuestionFactory factory) { this.factory = factory; }
    void click(Quiz quiz) { quiz.add(factory.make()); }
}

final class CloningTool {                               // Prototype
    private final Question prototype;
    CloningTool(Question prototype) { this.prototype = prototype; }
    void click(Quiz quiz) { quiz.add(prototype.copy()); }
}"""


LESSONS = [
    # ---------------------------------------------------------------- 06
    # Discussion of Creational Patterns (PDF pp. 155-156 of the operator's
    # copy), with the drawing editor of the Prototype pattern (p. 137).
    # Quotes: PDF p. 155 of the operator's copy, 16 words, quotes.py OK;
    # PDF p. 156, 23 words, quotes.py OK.
    # Lesson total: 39 words.
    {
        "slug": "creational-discussion",
        "title": "Discussion of Creational Patterns",
        "module": "Chapter 3 · Creational Patterns",
        "one_line": "Two ways to vary the classes a system creates, by subclassing the creator or by passing in an object that knows them, and how the five patterns divide between them.",
        "summary": (
            "The chapter closes by setting its patterns side by side: Factory Method "
            "against the three that pass in a factory object, compared on the drawing "
            "editor of the Prototype pattern. Read the discussion, then count one quiz "
            "builder's palette under Factory Method, Abstract Factory and Prototype, "
            "and what a new question type adds under each."
        ),
        "key": [
            "subclass the creator: Factory Method",
            "pass in a factory object: composition",
            "one product per family: no gain",
            "prototypes drop the creator classes",
            "start simple, add flexibility as needed",
        ],
        "key_label": "The discussion in five lines",
        "concepts_intro": (
            "Three ideas carry the lesson, all of them from the chapter's closing "
            "section."
        ),
        "concepts": [
            ("Parameterizing by subclassing",
             "Varying the class a system creates by subclassing the class that creates "
             "it: Factory Method. Simple, but a new product can need a new creator "
             "subclass, and the change can cascade to whatever creates the creator."),
            ("Parameterizing by composition",
             "Varying it by giving the system an object that knows which classes to "
             "create: Abstract Factory's factory, Builder's builder, Prototype's "
             "prototype. The factory object is a parameter, and replacing it changes "
             "what is made."),
            ("Evolving toward flexibility",
             "The authors' observation that designs often begin with Factory Method and "
             "move to the other creational patterns where more flexibility turns out to "
             "be needed, accepting their extra complexity there and only there."),
        ],
        "read_title": "The discussion's argument first, then the count",
        "read_intro": (
            "Read the Discussion of Creational Patterns at the end of Chapter 3 in your "
            "own copy first. It is two pages; the lesson reads it as an argument and "
            "then counts one design three ways."
        ),
        "body": [
            ("p", "&ldquo;There are two common ways to parameterize a system by the "
                  "classes of objects it creates.&rdquo; The authors close Chapter 3 with "
                  "that sentence and a short Discussion of Creational Patterns, and this "
                  "lesson reads it. Read it in your own copy first. The lesson reads it "
                  "as an argument, then counts one small design three ways."),
            ("p", "The first way is to subclass the class that does the creating, which is "
                  "Factory Method. Its drawback is that changing the product's class can "
                  "take a new subclass, and the need can cascade: if the creator is itself "
                  "made by a factory method, its own creator must be overridden as well. "
                  "The second way leans on composition: define an object whose job is to "
                  "know the product classes, and hand it to the system. Abstract Factory, "
                  "Builder and Prototype all do this, each with its own kind of factory "
                  "object: one that makes objects of several classes, one that builds a "
                  "complex product step by step through a matching protocol, and one "
                  "that copies itself, so that in Prototype the factory object and the "
                  "sample of the product are one and the same."),
            ("p", "The authors then return to the graphical editor framework of the "
                  "Prototype pattern, whose tool must be parameterized by the class of "
                  "graphic it adds, and try each pattern on it. Factory Method gives a "
                  "tool subclass per graphic class. Abstract Factory gives a factory class "
                  "per graphic class, each making a single product, and hands the tool "
                  "the right factory. Prototype has each graphic class implement cloning "
                  "and gives each tool a prototype to clone. Their judgement for that "
                  "framework is that Factory Method is easiest at first but multiplies "
                  "small subclasses that do little; that Abstract Factory offers little "
                  "improvement, because its factory hierarchy is as large, and is worth it only where "
                  "such a hierarchy already exists, provided by the language as in "
                  "Smalltalk or needed elsewhere in the system; and that Prototype "
                  "probably fits best, since it needs only a clone operation on each "
                  "graphic class, and cloning also serves a Duplicate command."),
            ("p", "The general lessons follow. Factory Method makes a design more "
                  "customisable at little extra complexity, and needs a new operation "
                  "where the others need new classes; people use it by default for making "
                  "objects, but it is not needed when the instantiated class "
                  "never changes, or when creation already happens in an operation "
                  "subclasses can override. Designs built on Abstract Factory, Prototype "
                  "or Builder are more flexible still, and more complex. &ldquo;Often, "
                  "designs start out using Factory Method and evolve toward the other "
                  "creational patterns as the designer discovers where more flexibility "
                  "is needed.&rdquo; Knowing the patterns, the authors end, gives a "
                  "designer more choices when one criterion has to be traded against "
                  "another."),
            ("p", "Two things are worth noticing about the comparison. It is made for one "
                  "framework, with one kind of product per tool, and the authors say "
                  "plainly that the best choice turns on many factors. And the comparison "
                  "is not one of class counts. Factory Method and Abstract Factory have "
                  "the same shape, a creator or factory per variant with one operation "
                  "per kind of product, which is why an abstract factory is often built "
                  "from factory methods; with two kinds per family they still count the "
                  "same. What separates them in the authors' argument is where the choice "
                  "is made, in a subclass of the class that needs the products or in an "
                  "object passed to it. Prototype is the one that reduces subclassing, "
                  "since it needs no creator or factory classes at all."),
            ("code", _lines(THREE_TOOLS_JAVA)),
            ("p", "Now the lab, on a quiz builder rather than a drawing editor. Its editor "
                  "has a palette with one tool per question type, multiple choice, true "
                  "or false, short answer and matching, and each tool must create its "
                  "own kind of question: 4 families of 1 kind each, stated once for all "
                  "three presets. On <code>palette-fm</code>, Factory Method, the design "
                  "has 1 abstract tool, 4 tool subclasses, 1 abstract question and 4 "
                  "question classes, 1 + 4 + 1 + 4 = 10 classes, 5 of which create. On "
                  "<code>palette-af</code>, Abstract Factory, the 5 creators are 1 "
                  "abstract factory and 4 concrete factories, and the total is again 1 + "
                  "4 + 1 + 4 = 10: the equally large hierarchy the authors describe, 5 "
                  "factory classes against 5 tool classes. The lab counts the tool only "
                  "under Factory Method, where it is the creator; under the other two it "
                  "is the client and left out, so the sketch's own classes come to 10, 11 "
                  "and 6."),
            ("p", "On <code>palette-proto</code>, Prototype, there is 1 prototype manager, "
                  "which the sketch does without since each tool holds its own "
                  "prototype, 1 abstract question and 4 question classes, 1 + 1 + 4 = 6 "
                  "classes, and "
                  "the configuration tile counts 4 configurations of 1 prototype each, "
                  "one per tool. Each preset also adds a fifth question type, ordering. "
                  "Factory Method adds 2 classes, a concrete tool and a question class, "
                  "10 to 12; Abstract Factory adds 2, a factory and a question class, 10 "
                  "to 12; Prototype adds 1, the question class, 6 to 7, and 1 "
                  "configuration that registers its prototype. None edits an existing "
                  "class. The lab counts each question type as a class of its own; if "
                  "the types differed only in values, Prototype could make them instances "
                  "of one class, the authors' argument about whole and half notes, and "
                  "its count would fall further."),
            ("h3", "Exercise"),
            ("ul", [
                "Each of the quiz builder's question types now needs two products, a "
                "`question` and a `rubric` that marks it.",
                "The families are the same four: `choice`, `truefalse`, `short` and "
                "`match`.",
            ]),
            ("p", "By hand, using the formulas of the lab's rules sentence, count the "
                  "classes in the design under Abstract Factory, Factory Method and "
                  "Prototype, and what a fifth question type adds under each. Then set "
                  "the kinds in the lab to <code>question rubric</code> and check each "
                  "scheme."),
            ("p", "Chapter 3 ends here. The next course, Structural Patterns, reads "
                  "Chapter 4, on how classes and objects are composed into larger "
                  "structures, beginning with Adapter."),
        ],
        "lab": ("gofkit", {
            "mode": "classes",
            "view": "factory",
            "families": PALETTE_FAMILIES,
            "kinds": PALETTE_KINDS,
            "change": "family",
            "preset": "palette-fm",
            "presets": [
                {"id": "palette-fm",
                 "label": "A quiz palette under Factory Method, a fifth question type",
                 "scheme": "factory-method",
                 "expect": {"gclClasses": "1 + 4 + 1 + 4 = 10", "gclFactories": "1 + 4 = 5", "gclAdded": "2 (10 → 12): 1 concrete creator, 1 concrete product", "gclChanged": "0"}},
                {"id": "palette-af",
                 "label": "The same palette under Abstract Factory",
                 "scheme": "abstract-factory",
                 "expect": {"gclClasses": "1 + 4 + 1 + 4 = 10", "gclFactories": "1 + 4 = 5", "gclAdded": "2 (10 → 12): 1 concrete factory, 1 concrete product", "gclChanged": "0"}},
                {"id": "palette-proto",
                 "label": "The same palette under Prototype",
                 "scheme": "prototype",
                 "expect": {"gclClasses": "1 + 1 + 4 = 6", "gclFactories": "1", "gclConfigs": "4 configurations of 1 prototype (4 instances)", "gclAdded": "1 (6 → 7): 1 concrete product", "gclConfigChange": "1 added, registering 1 prototype"}},
            ],
            "panel_title": "One design under three creational patterns",
            "panel_intro": _GOF_INTRO,
        }),
        "steps_title": "Choosing how to parameterize what is created",
        "steps_intro": "Four steps, the last of them on a design of your own.",
        "steps": [
            ("Ask whether the class created changes at all",
             "If it never does, a plain constructor call is enough, as the Discussion "
             "says of Factory Method itself."),
            ("Count the families and kinds",
             "Factory Method and Abstract Factory count the same for any number of kinds; "
             "only Prototype drops the creator classes. Decide by where the choice "
             "should be made."),
            ("Count all three schemes",
             "Type the families and kinds into the lab once and switch the scheme, "
             "reading the classes and what a new family adds under each."),
            ("Do it on your own design",
             "Take a place in a system you know where the class created varies. Count "
             "it under the three schemes, then write down which one it uses today and "
             "where the next change would land."),
        ],
        "worked": {
            "title": "One palette, three patterns",
            "intro": [
                "Count <code>palette-fm</code>, <code>palette-af</code> and "
                "<code>palette-proto</code>.",
            ],
            "lines": [
                "palette, Factory Method: 1 + 4 + 1 + 4 = 10",
                "palette, Abstract Factory: 1 + 4 + 1 + 4 = 10",
                "palette, Prototype: 1 + 1 + 4 = 6",
                "ordering: 2 under each factory scheme",
                "ordering under Prototype: 1, and a config",
            ],
            "after": [
                "The first two lines are the authors' remark that Abstract Factory's "
                "hierarchy is as large as Factory Method's. Neither scheme uses a family "
                "of more than one product here, so neither gains from it.",
            ],
        },
        "quiz_title": "Three patterns and the authors' comparison",
        "quiz": [
            {"q": "In the exercise (4 question types, 2 kinds each), how many classes does "
                  "the lab count under each scheme, by its rules sentence's formulas?",
             "a": ["Abstract Factory 15, Factory Method 15, Prototype 11",
                   "Abstract Factory 15, Factory Method 20, Prototype 11",
                   "Abstract Factory 13, Factory Method 15, Prototype 11",
                   "Abstract Factory 15, Factory Method 15, Prototype 10"],
             "c": 0,
             "why": "Abstract Factory: 1 + 4 + 2 + 8 = 15. Factory Method, 1 abstract "
                    "creator with a factory method per kind and 1 concrete creator per "
                    "type: 1 + 4 + 2 + 8 = 15, the same shape. Prototype: 1 + 2 + 8 = 11. "
                    "A fifth type adds 3, 3 and 2 classes, and edits none. 20 would give "
                    "every kind its own creator hierarchy, which neither the book nor the "
                    "lab does; 13 leaves out the abstract products, and 10 the manager."},
            {"q": "What drawback do the authors give for parameterizing a system by "
                  "subclassing the creator?",
             "a": ["Changing the product's class can take a new subclass, and such "
                   "changes can cascade",
                   "A factory object must be passed to the system",
                   "Every factory must change when a new kind of product is added",
                   "Every product must implement cloning"],
             "c": 0,
             "why": "If the creator is itself made by a factory method, its creator must "
                    "be overridden too. Passing a factory object is the other way; "
                    "changing every factory is Abstract Factory's new-kind liability; "
                    "cloning is Prototype's requirement."},
            {"q": "In the drawing-editor comparison, why does Abstract Factory offer little "
                  "over Factory Method?",
             "a": ["It needs a factory hierarchy as large as the tool subclasses it "
                   "replaces",
                   "It cannot create graphics at all",
                   "It requires a clone operation on each graphic class",
                   "It forces every graphic to be a singleton"],
             "c": 0,
             "why": "Each factory makes one product, so there is a factory class per "
                    "graphic class, as many as Factory Method's tool subclasses. The "
                    "authors would prefer it only where such a hierarchy already exists. "
                    "A clone operation is what Prototype needs."},
            {"q": "According to the Discussion, when is a factory method unnecessary?",
             "a": ["When the class instantiated never changes, or creation already happens "
                   "in an operation subclasses can override",
                   "Whenever the design is a framework",
                   "When there is more than one kind of product",
                   "When the product's class may change in a later release"],
             "c": 0,
             "why": "Those are the two cases the authors name. Frameworks are where "
                    "factory methods are most used, and a class that may change later is "
                    "exactly the case a factory method serves."},
        ],
        "mistakes": [
            ("Reading the drawing-editor verdict as a ranking of the patterns",
             "The authors choose Prototype for one framework with one product per tool, "
             "and say the best choice depends on many factors. On the lab's palette "
             "Abstract Factory and Factory Method both count 10 classes, and with two "
             "kinds per type both count 15; the difference the authors draw is "
             "subclassing the creator against passing in a factory object."),
            ("Starting with the most flexible pattern",
             "The authors observe designs that begin with Factory Method and move to "
             "Abstract Factory, Prototype or Builder where flexibility proves to be "
             "needed. The composed patterns are more flexible and more complex, and the "
             "extra complexity pays only where the variation arrives."),
            ("Thinking composition needs no new classes",
             "Abstract Factory needs a factory class per family; only Prototype does "
             "without factory classes, and then every product class must implement "
             "cloning, its own liability. The classes move; they do not all disappear."),
        ],
        "standard": (
            "Finish when you can count one design under three creational patterns and say what the counts leave out.",
            "Given the families and kinds of a design, state the classes under Factory "
            "Method, Abstract Factory and Prototype and what a new family adds under "
            "each, and give the authors' two ways of parameterizing a system and their "
            "comparison on the drawing editor."
        ),
        "note": (
            "The lab counts classes by three stated formulas, each product a class. It "
            "cannot weigh what the authors weigh: whether a factory hierarchy already "
            "exists, whether products differ only in values, whether cloning is hard for "
            "your classes, or where flexibility will be needed. The Discussion says the "
            "choice turns on many factors, and no count settles it."
        ),
    },
]
