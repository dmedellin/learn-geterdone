"""What Design Patterns Are, lesson 6 -- Chapter 1, Sections 1.7 and 1.8.

Gamma, Helm, Johnson and Vlissides, Design Patterns: Elements of Reusable
Object-Oriented Software (Addison-Wesley, 1995), Chapter 1: 1.7 How to Select a
Design Pattern and 1.8 How to Use a Design Pattern, with Table 1.2 described in
the lesson's own words. Pages in the comments are PDF pages of the operator's
copy; the lesson cites by chapter and section. Every quotation is copied from
that copy and checked with quotes.py. The design, records and Java sketch are
written for this lesson. The design is docs/design-patterns/PLAN.md, section C,
Course 1.
"""

from .part_a import _lines, _records


# A bakery's order system and the changes its team can foresee: what kind of
# thing would vary (aspect), whether the team thinks it likely, and in how many
# months they expect it.
BAKERY_CHANGES = """discount-rules, aspect=algorithm, likely=yes, months=3;
payment-provider, aspect=platform, likely=yes, months=6;
oven-schedule, aspect=algorithm, likely=no, months=24;
loyalty-alerts, aspect=dependents, likely=yes, months=9;
order-states, aspect=states, likely=yes, months=18;
receipt-layout, aspect=representation, likely=no, months=36;
new-branch, aspect=families, likely=no, months=48"""

DISCOUNT_JAVA = """// The participant's name, Strategy, kept inside the application's names.
interface DiscountStrategy {
    long discountCents(Order order);
}

final class NoDiscountStrategy implements DiscountStrategy {
    public long discountCents(Order order) { return 0; }
}

final class DozenDiscountStrategy implements DiscountStrategy {
    public long discountCents(Order order) {
        int dozens = order.items() / 12;
        return dozens * order.unitCents();   // one unit free per dozen
    }
}"""

LIBRARY_EXERCISE = """search-ranking, aspect=algorithm, likely=yes, months=4;
ebook-loans, aspect=platform, likely=yes, months=14;
hold-queue, aspect=dependents, likely=yes, months=8;
fine-rules, aspect=algorithm, likely=no, months=6
specification: likely = yes and months <= 12"""


LESSONS = [
    # ---------------------------------------------------------------- 06
    # 1.7 How to Select a Design Pattern (PDF pp. 48-49 of the operator's copy;
    # Table 1.2 p. 50), 1.8 How to Use a Design Pattern (pp. 49, 51).
    # Quotes: PDF p. 51 of the operator's copy, 7 + 15 = 22 words, quotes.py
    # OK. Lesson total: 22 words.
    {
        "slug": "selecting-and-using-a-pattern",
        "title": "Selecting and Using a Design Pattern",
        "module": "Chapter 1 · Introduction",
        "one_line": "Six ways to find the pattern for a problem, seven steps to apply it, and the warning that a pattern's flexibility is worth its cost only where it is needed.",
        "summary": (
            "The last two sections of Chapter 1 give six ways to find a pattern, seven "
            "steps for applying one, and a warning against applying them where their "
            "flexibility is not needed. Read them, then list the changes a design's team "
            "can foresee and let a specification of what should vary select the ones "
            "worth a pattern, and say which clause rejects the rest."
        ),
        "key": [
            "six ways to find a pattern",
            "encapsulate the concept that varies",
            "read Applicability and Consequences first",
            "keep the participant name in your names",
            "patterns add indirection",
            "apply one only where flexibility is needed",
        ],
        "key_label": "Selecting and using in six lines",
        "concepts_intro": (
            "Three ideas carry the lesson: the two sections' procedures, and the "
            "theme the authors find in many patterns."
        ),
        "concepts": [
            ("Six ways to select",
             "Consider how patterns solve design problems (Section 1.6); scan the "
             "intents (Section 1.4); study how patterns refer to each other (Figure "
             "1.1); read the catalog chapter for the right purpose; look for a cause of "
             "redesign; and ask what in your design should vary."),
            ("Encapsulate what varies",
             "The opposite of examining a cause of redesign: instead of asking what "
             "might force a change, ask what you would like to be free to change without "
             "redesign, and put that behind an interface of its own. Table 1.2 lists, "
             "for each pattern, the aspect it lets vary."),
            ("Seven steps of use",
             "Read the pattern for an overview, attending to Applicability and "
             "Consequences; study Structure, Participants and Collaborations; look at "
             "the Sample Code; name the participants for your application; define the "
             "classes; name the operations; implement them."),
        ],
        "read_title": "The two sections first, then a selection, then the warning",
        "read_intro": (
            "Read Sections 1.7 and 1.8 and Table 1.2 in your own copy first. The lesson "
            "reads them as a procedure, counts one selection made with it, and ends on "
            "the warning that closes the chapter."
        ),
        "body": [
            ("p", "&ldquo;A design pattern should only be applied when the flexibility it "
                  "affords is actually needed.&rdquo; That sentence is near the end of "
                  "Section 1.8, How to Use a Design Pattern, the last section of Chapter "
                  "1. This lesson reads it and Section 1.7, How to Select a Design "
                  "Pattern. Read both in your own copy first."),
            ("p", "Section 1.7 begins from the reader's position: more than twenty "
                  "patterns, a problem in front of you, and a catalog you do not yet "
                  "know. It gives six ways in. Go back to Section 1.6 and its list of how "
                  "patterns solve design problems. Read through the intents of Section "
                  "1.4, narrowing by the purpose and scope of Table 1.1. Follow the "
                  "cross-references of Figure 1.1 from a pattern you know. Read the "
                  "catalog chapter for the right purpose, each of which opens with an "
                  "introduction and closes with a comparison of its patterns. Look for "
                  "your problem among the causes of redesign. Or ask what in your design "
                  "ought to vary."),
            ("p", "The last two are, the authors say, opposites. A cause of redesign asks "
                  "what might force a change on you; the last approach asks what you want "
                  "to be free to change without redesigning, and puts that concept behind "
                  "an interface of its own, which they call a theme of many patterns. "
                  "Table 1.2 supports it: for each pattern, the aspect it lets vary. In "
                  "the lesson's words, a few of its entries: Strategy lets an algorithm "
                  "vary, State the states of an object, Observer how many objects depend "
                  "on another and how they keep up, Abstract Factory the families of "
                  "product objects, Bridge an object's implementation, and Builder how a "
                  "composite object is put together."),
            ("p", "Section 1.8 then gives seven steps for applying a pattern once chosen. "
                  "Read it through once, paying most attention to Applicability and "
                  "Consequences, to be sure it fits. Study its Structure, Participants and "
                  "Collaborations until the classes and their relations are clear. Look at "
                  "its Sample Code. Choose names for the participants that mean something "
                  "in your application, keeping the participant's name inside them so the "
                  "pattern stays visible, as the sketch below does. Define the classes, "
                  "their interfaces, inheritance and references, and change the existing "
                  "classes the pattern touches. Name the operations, consistently. Then "
                  "implement them, with the Implementation section's hints. These are a "
                  "start, the authors add; readers will develop ways of their own."),
            ("code", _lines(DISCOUNT_JAVA)),
            ("p", "Then the warning, which this course ends on. &ldquo;Design patterns "
                  "should not be applied indiscriminately.&rdquo; Their flexibility is "
                  "often bought with extra levels of indirection, the authors explain, "
                  "and indirection can complicate a design and cost some performance; the "
                  "Consequences sections are where the benefits and liabilities are "
                  "weighed. It is the same point the last three lessons made in their own "
                  "terms: an interface with one implementation, a composed object whose "
                  "behaviour is spread over three, an interface that confines one kind of "
                  "change and spreads another."),
            ("p", "Now the lab, on a bakery's order system of the lesson's own. Its team "
                  "has listed seven changes it can foresee, each with the aspect that "
                  "would vary, whether they think it likely, and how many months away. "
                  "The preset <code>needed</code> writes the team's rule for what should "
                  "vary, likely and within a year, as <code>likely = yes and months &lt;= "
                  "12</code>. It selects 3 of the 7 candidates: discount-rules, "
                  "payment-provider and loyalty-alerts. The failing list gives each "
                  "rejection's clause: oven-schedule, receipt-layout and new-branch fail "
                  "<code>likely = yes</code>, and order-states fails <code>months &lt;= "
                  "12</code> at 18 months."),
            ("p", "Each selected change points to a pattern: the discount rules are an "
                  "algorithm, which Table 1.2 gives to Strategy, as in the sketch; the "
                  "payment provider is a platform dependence, for which Section 1.6's list "
                  "of causes gives Abstract Factory and Bridge (in Table 1.2, Bridge lets "
                  "an object's implementation vary); the loyalty alerts are objects "
                  "that depend on an order, Observer. The preset <code>algorithms</code> "
                  "adds <code>aspect = algorithm</code> and selects only discount-rules, "
                  "the narrowing Section 1.7 suggests once the purpose is known. The "
                  "preset <code>everything</code> asks for anything within four years, "
                  "<code>months &lt;= 48</code>, and selects all 7, failing none: a "
                  "pattern for every change the team can imagine, each with its "
                  "indirection, which is the indiscriminate use Section 1.8 warns "
                  "against."),
            ("p", "The rule is the team's, and so are the attributes. The lab shows "
                  "what a rule selects and which clause turns each candidate away; it "
                  "cannot say whether a change rated unlikely will come anyway, or "
                  "whether eighteen months is near enough to prepare for now. Those are "
                  "the judgements the Consequences sections exist to inform."),
            ("h3", "Exercise"),
            ("code", _lines(LIBRARY_EXERCISE)),
            ("p", "A library catalogue's foreseeable changes, with the same rule. By hand, "
                  "say which candidates the specification selects and which clause rejects "
                  "each of the others, and name a pattern from Table 1.2 for each one "
                  "selected. Then type the candidates into the lab to check."),
            ("p", "That ends Chapter 1, and its last word is the one to carry into the "
                  "rest of the book: a pattern buys flexibility with indirection, and is "
                  "worth applying only where that flexibility is needed. The next course, "
                  "A Case Study: Designing a Document Editor, watches the authors make "
                  "exactly those choices, one design problem at a time, beginning with "
                  "Design Problems and Document Structure."),
        ],
        "lab": ("dddkit", {
            "mode": "spec",
            "view": "select",
            "candidates": _records(BAKERY_CHANGES),
            "preset": "needed",
            "presets": [
                {"id": "needed",
                 "label": "A bakery's foreseeable changes: likely, within a year",
                 "spec": "likely = yes and months <= 12",
                 "expect": {"dspCandidates": "7",
                            "dspSatisfying": "3: discount-rules, payment-provider, "
                                             "loyalty-alerts"}},
                {"id": "algorithms",
                 "label": "The same rule, for algorithms only",
                 "spec": "likely = yes and months <= 12 and aspect = algorithm",
                 "expect": {"dspSatisfying": "1: discount-rules"}},
                {"id": "everything",
                 "label": "Every change within four years",
                 "spec": "months <= 48",
                 "expect": {"dspSatisfying": "7: discount-rules, payment-provider, "
                                             "oven-schedule, loyalty-alerts, "
                                             "order-states, receipt-layout, new-branch",
                            "dspFailing": "0: none"}},
            ],
            "panel_title": "The changes a rule for what should vary selects",
            "panel_intro": (
                "The lab counts one consequence of a rule for what should vary; whether "
                "a change is likely, and whether a pattern is worth its indirection, is "
                "weighed in the book's Consequences sections and by the team."
            ),
        }),
        "steps_title": "Selecting a pattern for what should vary",
        "steps_intro": "Five steps, the last of them on a design of your own.",
        "steps": [
            ("List the changes you can foresee",
             "Write each change the design might meet, with the aspect that would vary, "
             "whether it is likely, and how soon."),
            ("Write the rule",
             "Write, as clauses joined by and, what makes a change worth preparing for "
             "now. Agree it before looking at which changes it selects."),
            ("Select and read the rejections",
             "Evaluate the rule on each change. For each one rejected, note the clause "
             "that rejects it; that is the reason not to add a pattern for it yet."),
            ("Find the pattern",
             "For each selected change, find the aspect in Table 1.2, read that "
             "pattern's Applicability and Consequences, and check it fits before going "
             "further."),
            ("Do it on a design of your own",
             "List five changes your own system might meet and apply the rule. For the "
             "one change it selects that matters most, name a pattern, its participants "
             "with your application's names, and the extra indirection it adds."),
        ],
        "worked": {
            "title": "The bakery's rule, change by change",
            "intro": [
                "Evaluate <code>likely = yes and months &lt;= 12</code> on the seven changes.",
            ],
            "lines": [
                "discount rules: likely, 3 months: selected",
                "payment provider: likely, 6 months: selected",
                "oven schedule: likely is no: rejected",
                "loyalty alerts: likely, 9 months: selected",
                "order states: 18 months: rejected",
                "receipt layout, new branch: likely is no",
                "selected: 3 of the 7 changes",
            ],
            "after": [
                "Three changes are worth a pattern now by the team's rule. Order-states "
                "is likely and fails only on time; if the rule's year were eighteen "
                "months, State would join the list.",
            ],
        },
        "quiz_title": "Selecting, using, and when not to",
        "quiz": [
            {"q": "In the exercise, which candidates does <code>likely = yes and months "
                  "&lt;= 12</code> select, and which clause rejects ebook-loans?",
             "a": ["search-ranking and hold-queue; ebook-loans fails months &lt;= 12",
                   "search-ranking, hold-queue and fine-rules; ebook-loans fails months "
                   "&lt;= 12",
                   "search-ranking and hold-queue; ebook-loans fails likely = yes",
                   "search-ranking only; ebook-loans fails months &lt;= 12"],
             "c": 0,
             "why": "Search-ranking (likely, 4 months) and hold-queue (likely, 8 months) "
                    "pass both clauses. Ebook-loans is likely, so it passes the first "
                    "clause and fails the second at 14 months. Fine-rules is within a year "
                    "but not likely, so it fails the first clause. A pattern for the "
                    "selected two: Strategy for the ranking, an algorithm; Observer for the "
                    "hold queue, whose members depend on a copy coming back."},
            {"q": "Which of Section 1.7's approaches do the authors call the opposite of "
                  "examining a cause of redesign?",
             "a": ["Scanning the Intent sections",
                   "Reading the catalog chapter for the problem's purpose",
                   "Asking what in your design should vary",
                   "Studying how patterns interrelate"],
             "c": 2,
             "why": "A cause of redesign asks what might force a change; the last "
                    "approach asks what you would like to be free to change without redesign, "
                    "and encapsulates it. The other three are separate ways in, by "
                    "intent, by catalog chapter and by Figure 1.1."},
            {"q": "In Section 1.8's steps, what comes right after studying the Structure, "
                  "Participants and Collaborations?",
             "a": ["Reading the Applicability and Consequences",
                   "Looking at the Sample Code",
                   "Choosing names for the participants",
                   "Defining the classes"],
             "c": 1,
             "why": "The order is: read for an overview with attention to Applicability "
                    "and Consequences; study Structure, Participants and Collaborations; "
                    "look at the Sample Code; then name the participants, define the "
                    "classes, name the operations and implement them."},
            {"q": "According to Section 1.8, what do patterns often introduce to gain "
                  "their flexibility?",
             "a": ["Global variables", "Additional levels of indirection",
                   "Duplicated code in each subclass", "Checks at compile time"],
             "c": 1,
             "why": "The authors say the flexibility usually comes from an extra layer "
                    "of indirection, which can make a design harder to follow and slower; that is why a pattern should be applied only when its "
                    "flexibility is actually needed."},
        ],
        "mistakes": [
            ("Applying every pattern that could fit",
             "The chapter's closing warning is against exactly that: patterns should not "
             "be applied indiscriminately, because their flexibility comes from "
             "indirection that complicates a design and can cost performance. On the "
             "lesson's illustration, a rule that admits every imaginable change selects "
             "all seven, and each would add its indirection."),
            ("Treating the six ways of selecting as one method",
             "Section 1.7 offers several ways in, and says two of them are opposites: "
             "examining what might force a change, and considering what you want to be "
             "free to change. They can lead to different patterns for the same "
             "design, and reading one problem both ways is part of the point."),
            ("Copying the participants' names into the code",
             "Step four says the book's participant names are usually too abstract to "
             "use as they are. Choose names that mean something in the application, and "
             "keep the participant's name inside them, as "
             "<code>DozenDiscountStrategy</code> keeps Strategy, so the pattern stays "
             "visible."),
        ],
        "standard": (
            "Finish when you can select a pattern by what should vary, and say when not to apply one.",
            "Given a design's foreseeable changes and a rule for what should vary, "
            "state which changes the rule selects and which clause rejects each other "
            "one, name a pattern for each selected change from Table 1.2, list "
            "Section 1.8's steps, and give the chapter's reason for restraint."
        ),
        "note": (
            "The lab applies the rule to the attributes typed in. Whether a change is "
            "likely, how soon it will come, and whether a pattern's indirection is worth "
            "it are judgements no count makes; the authors' answer is to apply a pattern "
            "only where its flexibility is actually needed, and to read its "
            "Consequences first."
        ),
    },
]
