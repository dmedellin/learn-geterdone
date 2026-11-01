"""Breakthroughs and Implicit Concepts, lessons 1-5 -- Chapters 8 and 9.

Eric Evans, Domain-Driven Design: Tackling Complexity in the Heart of Software
(Addison-Wesley, 2004): Chapter 8, Breakthrough; Chapter 9, Making Implicit
Concepts Explicit (Digging Out Concepts; How to Model Less Obvious Kinds of
Concepts; Specification; Applying and Implementing Specification). Pages in
the comments are PDF pages of the operator's copy; the lessons cite by
chapter, section and pattern. Every quotation is copied from that copy and
checked with quotes.py. The models and code are written for these lessons:
none of the book's listings, diagrams, dialogues or example domains is
reproduced, and each lab works a domain of its own (a shared kitchen, a
public library, a theatre, a seed bank). Each snippet is one constant below,
used both by the lesson's code block and, for the cckit lesson, by the lab
preset that counts it, so the line numbers the prose names are the lab's. The
design is docs/domain-driven-design/PLAN.md, section C, Course 4.
"""


def _lines(text):
    """A snippet constant as a code block's list of lines."""
    return text.split("\n")


# ---------------------------------------------------------------- snippets

# 4.1 Breakthrough: body only.
SHARE_PIE = """// One concept for every split: a pie of shares that allocates exactly.
final class SharePie {
    private final Map<String, Long> shares;   // member -> whole share
    long[] allocate(long cents) {
        long total = 0;
        for (long s : shares.values()) { total = total + s; }
        long[] out = new long[shares.size()];
        long given = 0;
        int i = 0;
        for (long s : shares.values()) {
            out[i] = cents * s / total;          // rounded down
            given = given + out[i];
            i = i + 1;
        }
        for (int k = 0; given < cents; k = k + 1, given = given + 1) {
            out[k] = out[k] + 1;                 // leftover, from the first
        }
        return out;
    }
}"""

# 4.3 Constraints and processes: presets inline-limit, factored-caller,
# factored-constraint; exercise.
INLINE_LIMIT = """// The sales limit, written inline where seats are sold.
class Performance {
    private int capacity;
    private int sold;
    private int accessHeld;
    private boolean preview;

    boolean sell(int seats, Patron patron) {
        int limit = capacity - accessHeld;
        if (preview && !patron.isMember()) {
            limit = limit - capacity / 10;
        }
        if (seats > 0 && sold + seats <= limit) {
            sold = sold + seats;
            return true;
        }
        return false;
    }
}"""

FACTORED_CALLER = """// The caller, once the rule has a name of its own.
class Performance {
    private int sold;
    private SalesLimit limit;

    boolean sell(int seats, Patron patron) {
        if (!limit.allows(sold, seats, patron)) {
            return false;
        }
        sold = sold + seats;
        return true;
    }
}"""

FACTORED_CONSTRAINT = """// The constraint as an object: a named thing the team can discuss.
class SalesLimit {
    private int capacity;
    private int accessHeld;
    private boolean preview;

    boolean allows(int sold, int seats, Patron patron) {
        int limit = capacity - accessHeld;
        if (preview && !patron.isMember()) {
            limit = limit - capacity / 10;
        }
        return seats > 0 && sold + seats <= limit;
    }
}"""

CLINIC_BOOKING = """// A clinic books follow-up visits; the rule sits inside book().
class Clinician {
    private List<Visit> diary;
    private int dailyCap;
    Visit book(Patient p, LocalDate day, boolean urgent) {
        int booked = 0;
        for (Visit v : diary) {
            if (v.day().equals(day)) {
                booked = booked + 1;
            }
        }
        boolean saturday = day.getDayOfWeek() == SATURDAY;
        if (!urgent && (booked >= dailyCap || saturday)) {
            throw new IllegalStateException("no room that day");
        }
        Visit visit = new Visit(p, day);
        diary.add(visit);
        return visit;
    }
}"""

# 4.4 Specification: body only.
DISTRIBUTABLE_LOT = """interface LotSpecification { boolean isSatisfiedBy(SeedLot lot); }
// The seed bank's rule for sending a lot to growers, as a value object.
final class DistributableLot implements LotSpecification {
    private final int minGermination;   // percent of seeds that sprout
    private final int maxMoisture;      // percent water by weight
    private final int maxAgeYears;

    DistributableLot(int minGermination, int maxMoisture, int maxAgeYears) {
        this.minGermination = minGermination;
        this.maxMoisture = maxMoisture;
        this.maxAgeYears = maxAgeYears;
    }

    public boolean isSatisfiedBy(SeedLot lot) {
        return lot.germination() >= minGermination
            && lot.moisture() <= maxMoisture
            && lot.ageYears() <= maxAgeYears
            && !lot.inQuarantine();
    }
}"""

# 4.5 Applying Specification: body only.
THREE_USES = """// Validation: one lot, one answer.
boolean ok = distributable.isSatisfiedBy(lot);

// Selection: the repository takes the rule; the rule stays in the domain.
interface SeedLotRepository {
    List<SeedLot> satisfying(LotSpecification spec);
}

// Building to order: the assembler is told what, not how,
// and its result is checked against the same specification.
interface PacketAssembler {
    Packet assemble(LotSpecification wanted, int varieties);
}
Packet packet = assembler.assemble(schoolGarden, 5);
for (SeedLot each : packet.lots()) {
    if (!schoolGarden.isSatisfiedBy(each)) {
        throw new IllegalStateException(each.id() + " breaks the request");
    }
}"""


# ---------------------------------------------------------------- lab data

# The seed bank's lots, shared by 4.4 (one at a time) and 4.5 (all seven).
_LOTS = (
    "lot-01, germination=93, moisture=6, age=2, quarantine=no, kind=vegetable; "
    "lot-02, germination=88, moisture=9, age=5, quarantine=no, kind=herb; "
    "lot-03, germination=81, moisture=7, age=3, quarantine=no, kind=vegetable; "
    "lot-04, germination=95, moisture=5, age=14, quarantine=no, kind=flower; "
    "lot-05, germination=90, moisture=8, age=6, quarantine=yes, kind=vegetable; "
    "lot-06, germination=86, moisture=7, age=9, quarantine=no, kind=herb; "
    "lot-07, germination=72, moisture=10, age=11, quarantine=no, kind=vegetable"
)

_DISTRIBUTABLE = "germination >= 85 and moisture <= 8 and age <= 10 and quarantine = no"

_COMPLEXITY_INTRO = (
    "The lab counts decision points by a stated rule: one, plus one for each if, "
    "while, for and case, and for each conditional and and conditional or. The "
    "bands beside the count are McConnell's, from Code Complete; Evans gives no "
    "count. The listings are the lesson's."
)


LESSONS = [
    # ---------------------------------------------------------------- 01
    # Chapter 8, Breakthrough: opening (PDF p. 115 of the operator's copy);
    # Story of a Breakthrough, A Decent Model and Yet, The Breakthrough
    # (pp. 116-118); A Deeper Model (pp. 119-120); A Sobering Decision
    # (p. 120); The Payoff, Opportunities, Focus on Basics, Epilogue
    # (pp. 121-122).
    # Quote: PDF p. 115 of the operator's copy, 12 words, quotes.py OK.
    # Lesson total: 12 words.
    {
        "slug": "breakthrough",
        "title": "Breakthrough",
        "module": "Chapter 8 · Breakthrough",
        "one_line": "Months of small refactorings can suddenly open onto a much deeper model; Evans tells the story of one, and of the hard decision to take it.",
        "summary": (
            "Chapter 8 is a story from Evans's own work: a model refactored all "
            "winter, a sudden insight that shares are a concept of their own, and a "
            "decision to rebuild under a deadline. Read how the breakthrough came, "
            "what the deeper model removed, and why Evans tells you not to chase one, "
            "then split two bills by two kinds of share and count the cents each "
            "rounding rule loses."
        ),
        "key": [
            "returns from refactoring are not linear",
            "small steps prepare the way",
            "a breakthrough is an event, not a technique",
            "deciding to take it is the hard part",
            "shares became a concept of their own",
            "focus on basics; watch for the moment",
        ],
        "key_label": "Breakthrough in six lines",
        "concepts_intro": (
            "Three terms carry the lesson. The first two are the chapter's, the third "
            "the lab's."
        ),
        "concepts": [
            ("Breakthrough",
             "A sudden change to a much deeper model, after which the design is "
             "simpler and says more about the business. Evans presents it as "
             "something that happens to a team, after many small refactorings, and "
             "not as a step anyone can schedule."),
            ("Deep model",
             "A model whose concepts match how the domain experts actually think about "
             "their work, so that scenarios which once needed special cases become "
             "ordinary uses of the model. Chapter 1 introduced the term; this chapter "
             "shows one arriving."),
            ("A share pie",
             "In the lab, a set of whole-number shares that one object uses to split "
             "any amount, giving out the leftover cents itself so the parts always add "
             "up. It stands in for the concept the chapter's story discovers, on a "
             "domain written for the lesson."),
        ],
        "read_title": "The story first, then what it teaches, then the count",
        "read_intro": (
            "Read Chapter 8 in your own copy first. It is short, and it is a story; "
            "the lesson reads it as one, then states what Evans draws from it, and "
            "ends with a split bill counted two ways."
        ),
        "body": [
            ("p", "&ldquo;This sort of breakthrough is not a technique; it is an "
                  "event.&rdquo; Evans writes that in the opening of Chapter 8, "
                  "Breakthrough, the first chapter of Part III, Refactoring Toward "
                  "Deeper Insight. The chapter is short, and almost all of it is a story "
                  "told so that you will recognise the shape of the thing when it "
                  "happens on your own project. Read it in your own copy first."),
            ("p", "The opening sets the frame. Refactoring, Evans says, usually pays a "
                  "little for a little: a responsibility moved here, an association "
                  "adjusted there, and the small gains accumulate and keep a code base "
                  "from hardening. But the returns are not linear. Each refinement "
                  "gives the developers a clearer view, and that clarity is what makes "
                  "a sudden, larger insight possible, after which the model is both "
                  "more powerful and simpler. What the team can control is the "
                  "steady work beforehand; the challenge when the moment comes is "
                  "to see it for what it is and decide what to do."),
            ("p", "The story, in Story of a Breakthrough, is from a project Evans worked "
                  "on for an investment bank, and it is summarised here, not reworked. "
                  "After a winter of refactoring the team had a working model in which "
                  "each lender's part of a loan followed its fixed share of the "
                  "agreement behind it. Exceptions kept arriving: lenders who put in "
                  "more or less than their share on a given draw, handled by adding "
                  "adjustment objects. Complexity grew, and rounding discrepancies "
                  "would not go away however clever the algorithms became. Then, one "
                  "week, the team saw that the two sets of shares could change "
                  "independently, and that shares of any divisible value were one "
                  "concept. Evans drew a small abstract model of shares, a "
                  "&ldquo;Share Pie&rdquo;, and the special cases fell away."),
            ("p", "A Deeper Model lists what that bought, and two of its points are worth "
                  "carrying away. The new model removed a constraint that was not true "
                  "of the business, and it kept the true ones, such as the totals. And "
                  "one of the old classes turned out not to be a banking term at all: "
                  "the experts had said several times that they did not understand it, "
                  "and had deferred to the developers. A concept the experts never "
                  "recognised had been invented by a team that had not yet understood "
                  "the domain. The new model worked very well, and Evans records that "
                  "the whole team felt sick."),
            ("p", "That is A Sobering Decision. The project was already late, there "
                  "were no automated tests, and the change could not be made in small "
                  "steps that kept everything working. The project manager asked four "
                  "questions, in substance: how long to get back to where they were, "
                  "whether the problems could be solved without the change, whether "
                  "the next release would suffer without it, and whether it was the "
                  "right thing to do. The answers were about three weeks; probably, but "
                  "with no way to be sure; yes, and the change would only get harder; "
                  "and yes, lower risk in the long run. He let them go ahead, and it "
                  "took three weeks. In The Payoff, the surprising requirement changes "
                  "stopped, the rounding settled down, and the Share Pie became part of "
                  "the language that developers, experts and even the marketing people used."),
            ("p", "Then Evans turns the story into advice, and the advice is modest. "
                  "Opportunities warns that the chance of a breakthrough is often "
                  "frightening, with more opportunity and more risk than an ordinary "
                  "refactoring, and may come at a bad time. Focus on Basics tells you "
                  "not to sit waiting for one: keep crunching knowledge, keep the "
                  "Ubiquitous Language sharp, make implicit concepts explicit, make the "
                  "design suppler and distil the model, which are Chapters 9, 10 and "
                  "15, and do not hold back from small improvements. The Epilogue "
                  "adds that one breakthrough made the next visible: weeks later the "
                  "team noticed rules crammed into the methods of the two central "
                  "objects, and a word in their conversations, transaction in the "
                  "financial sense, that named no object; a second deeper model "
                  "followed."),
            ("p", "Now a model of the lesson's own, far from banking. Three caterers "
                  "share a commercial kitchen. They own its equipment in the "
                  "proportions they paid for it, 50, 30 and 20, and they use it for "
                  "different hours each month. The lease is split by ownership; the gas "
                  "bill by hours used, 9, 7 and 5 this month. A first design splits each "
                  "bill where it is paid, multiplying and rounding each caterer's "
                  "part. The lab splits an amount in cents by ratios under a rounding "
                  "rule and reports the shares, their total, and the total less the "
                  "amount."),
            ("p", "On the preset <code>lease-nearest</code> the lease of 9,999 cents is "
                  "split 50, 30, 20 with each part rounded to the nearest cent: exact "
                  "parts of 4,999.5, 2,999.7 and 1,999.8 cents become 5,000, 3,000 and "
                  "2,000, a total of 10,000, one cent more than the bill. On "
                  "<code>gas-nearest</code> the gas bill of 4,000 cents split 9, 7, 5 "
                  "comes to 1,714, 1,333 and 952, a total of 3,999, a cent short. Each "
                  "part was rounded without knowing what the others did, and neither "
                  "error is anyone's fault in particular. That is the kind of "
                  "discrepancy the story's team kept trying to fix with ever cleverer "
                  "code."),
            ("p", "The presets <code>lease-allocated</code> and <code>gas-allocated</code> "
                  "give the split to one concept. A share pie rounds every part down and "
                  "hands out the cents left over, one each from the first member. The "
                  "lease becomes 5,000, 3,000 and 1,999, the gas 1,715, 1,333 and 952, "
                  "and both totals equal their bills, 0 off. "
                  "The lab also prints the exact parts and the largest gap between a "
                  "part and its exact value: half a cent on the lease under nearest, "
                  "4/5 of a cent under the pie, where the third caterer, who gets none "
                  "of the leftover cents, falls 0.8 short of the exact part. Exact totals are bought with slightly less even parts. The class below is that "
                  "concept as a sketch. The two pies are different objects that change "
                  "independently: a caterer who buys a new oven changes the ownership "
                  "pie and leaves the hours alone. The same allocation applied to two "
                  "splits is the lesson's version of the story's point. If you have "
                  "read the Money lesson of Enterprise Application Patterns, the "
                  "allocator is the same one; Fowler asks how to divide a sum without "
                  "losing a penny, and Evans asks what concept in the domain the "
                  "division belongs to."),
            ("code", _lines(SHARE_PIE)),
            ("p", "Keep the count in proportion. A cent is not why Evans's team changed "
                  "its model; the rounding was a symptom, and the change was the "
                  "discovery that shares were a concept and that one supposed rule "
                  "of the business was false. The lab shows one consequence of making "
                  "the concept explicit, an exact total, on a domain the lesson "
                  "invented. Whether your own model is due for such a change, and "
                  "whether to make it this month, is the project manager's four "
                  "questions, and no count answers them."),
            ("h3", "Exercise"),
            ("ul", [
                "Amount: 10,000 cents, the kitchen's cleaning contract.",
                "Ratios: 3 3 1, the floor space each caterer's storage takes.",
                "Rules: nearest, then the share pie's allocation.",
            ]),
            ("p", "Work each exact part, then each caterer's part, the total and the "
                  "total less the amount under both rules, by hand. Then set the lab to "
                  "the same amount, ratios and rule to check."),
            ("p", "A breakthrough comes after concepts have been made explicit one by "
                  "one. The next lesson, Digging Out Concepts, reads the five places "
                  "Evans looks for them."),
        ],
        "lab": ("eakit", {
            "mode": "money",
            "view": "allocate",
            "preset": "lease-nearest",
            "presets": [
                {"id": "lease-nearest",
                 "label": "The lease, 9,999 cents by ownership 50 30 20, each part to nearest",
                 "amount": "9999", "ratios": "50 30 20", "rule": "nearest",
                 "expect": {"mnShares": "5,000, 3,000, 2,000", "mnTotal": "10,000", "mnDiff": "+1",
                            "mnFurthest": "1/2 = 0.50"}},
                {"id": "lease-allocated",
                 "label": "The lease by the ownership pie, leftover cents from the first",
                 "amount": "9999", "ratios": "50 30 20", "rule": "allocator",
                 "expect": {"mnShares": "5,000, 3,000, 1,999", "mnTotal": "9,999", "mnDiff": "0",
                            "mnFurthest": "4/5 = 0.80"}},
                {"id": "gas-nearest",
                 "label": "The gas bill, 4,000 cents by hours 9 7 5, each part to nearest",
                 "amount": "4000", "ratios": "9 7 5", "rule": "nearest",
                 "expect": {"mnShares": "1,714, 1,333, 952", "mnTotal": "3,999", "mnDiff": "−1"}},
                {"id": "gas-allocated",
                 "label": "The gas bill by the hours pie, leftover cents from the first",
                 "amount": "4000", "ratios": "9 7 5", "rule": "allocator",
                 "expect": {"mnShares": "1,715, 1,333, 952", "mnTotal": "4,000", "mnDiff": "0"}},
            ],
            "panel_title": "Two bills, two pies of shares",
            "panel_intro": (
                "Give an amount in cents, the shares and a rule. Each exact part is the "
                "amount times its share over the sum of the shares. The allocator, the "
                "lesson's share pie, rounds every part down, then gives the cents left "
                "over one each to the members in order from the first."
            ),
            "source": "the lesson's illustration, a shared kitchen's bills, not the book's",
        }),
        "steps_title": "Splitting a bill by a pie of shares",
        "steps_intro": "Four steps, the last of them on a system of your own.",
        "steps": [
            ("Work the exact parts",
             "Multiply the amount by each share and divide by the sum of the shares. "
             "Keep the fractions."),
            ("Round each part on its own",
             "Round each exact part to the nearest cent, add them, and compare the "
             "total with the amount."),
            ("Let the pie allocate",
             "Round every part down, count the cents left over, and give them one each "
             "from the first member. Check that the total equals the amount."),
            ("Do it on your own code",
             "Find a place in a system you know where an amount is divided among "
             "several parties. Count how many places do the dividing, write the figure "
             "down, and say in one sentence what concept in the domain the division "
             "belongs to."),
        ],
        "worked": {
            "title": "The lease, 9,999 cents, 50 30 20",
            "intro": [
                "Work <code>lease-nearest</code>, then <code>lease-allocated</code>.",
            ],
            "lines": [
                "exact: 4,999.5, 2,999.7, 1,999.8",
                "to nearest: 5,000, 3,000, 2,000",
                "total 10,000: a cent gained, +1",
                "down: 4,999, 2,999, 1,999, total 9,997",
                "2 cents left: one each to the first two",
                "pie: 5,000, 3,000, 1,999, total 9,999",
            ],
            "after": [
                "Rounding each part to nearest gains a cent here and loses one on the gas "
                "bill. The pie rounds every part the same way and then gives out "
                "exactly what is left, so its total cannot drift. Which member should "
                "receive a leftover cent is a business rule, and the lesson's choice, "
                "from the first, is only one of several the experts might want.",
            ],
        },
        "quiz_title": "Breakthroughs, decisions and shares",
        "quiz": [
            {"q": "In the exercise, 10,000 cents split 3, 3, 1: what are the parts and "
                  "the total under nearest, and under the share pie's allocation "
                  "(round down, leftover cents one each from the first)?",
             "a": ["nearest 4,286, 4,286, 1,429, total 10,001; pie 4,286, 4,286, 1,428, total 10,000",
                   "nearest 4,286, 4,286, 1,428, total 10,000; pie the same",
                   "nearest 4,285, 4,285, 1,428, total 9,998; pie 4,286, 4,286, 1,428, total 10,000",
                   "nearest 4,286, 4,286, 1,429, total 10,001; pie 4,285, 4,286, 1,429, total 10,000"],
             "c": 0,
             "why": "The exact parts are 30,000/7 ≈ 4,285.71 twice and 10,000/7 ≈ "
                    "1,428.57. Each rounds up to nearest, 4,286, 4,286 and 1,429, a total "
                    "of 10,001, a cent over. Rounded down they are 4,285, 4,285 and "
                    "1,428, a total of 9,998, which is the third option's figure for "
                    "rounding down, not for nearest. The pie gives the 2 cents left over "
                    "to the first two members: 4,286, 4,286 and 1,428, exactly 10,000. "
                    "The last option gives the leftover to the wrong members."},
            {"q": "In A Deeper Model, what does Evans say the new model did, besides "
                  "making shares a concept of their own?",
             "a": ["It removed a constraint the business did not have, and kept the valid ones",
                   "It removed every constraint on the shares, totals included",
                   "It added a new class for each kind of adjustment",
                   "It moved the rounding into the database"],
             "c": 0,
             "why": "The old model tied one set of shares to the other, which was not true "
                    "of the business; the new one let them vary independently while "
                    "keeping the real constraints, such as totals, in place. The "
                    "adjustment objects disappeared rather than multiplying."},
            {"q": "What does Focus on Basics advise a team that hopes for a breakthrough?",
             "a": ["Set aside time each iteration to look for one",
                   "Keep making modest improvements and knowledge crunching, and watch for the chance",
                   "Avoid small refactorings, which lock in the current model",
                   "Wait until the release is out before any refactoring"],
             "c": 1,
             "why": "Evans tells you not to be paralysed by trying to bring a "
                    "breakthrough about: push on the predictable levers, the Ubiquitous "
                    "Language, explicit concepts, supple design and distillation, keep "
                    "making small improvements, and be watchful. A breakthrough cannot be "
                    "scheduled, which is the chapter's point about it being an event."},
            {"q": "On the preset <code>gas-nearest</code>, the rule is changed to the share "
                  "pie's allocation. What does the lab report?",
             "a": ["1,714, 1,333, 952, total 3,999, as before",
                   "1,714, 1,333, 953, total 4,000",
                   "1,715, 1,333, 952, total 4,000",
                   "1,715, 1,334, 953, total 4,002"],
             "c": 2,
             "why": "Rounded down the parts are 1,714, 1,333 and 952, 3,999 in all, so one "
                    "cent is left, and it goes to the first member: 1,715. The second "
                    "option gives it to the member with the largest remainder, 952.38, "
                    "which is a reasonable rule but not the lab's. That is <code>gas-allocated</code>."},
        ],
        "mistakes": [
            ("Treating a breakthrough as a technique a team can plan for",
             "The chapter's opening calls it an event, and Focus on Basics tells you not "
             "to be paralysed trying to produce one. What a team can plan is the steady "
             "work that makes one possible: knowledge crunching, a sharp language, "
             "explicit concepts, supple design. The breakthrough itself came, in Evans's "
             "story, in one week after a winter of small steps."),
            ("Thinking a deeper model should be taken the moment it is seen",
             "Evans's team was frightened, and with reason: the project was late, there "
             "were no automated tests, and there were few stable stopping points. The "
             "decision rested on the manager's questions, how long, whether it could be "
             "done without, what not doing it would cost later, and whether it was "
             "right, and Opportunities says plainly that the timing may be bad. Taking "
             "it was a judgement about that project, not a rule."),
            ("Reading the rounding as the reason for the change",
             "The pennies were a symptom the team could not cure, and the lab counts "
             "them because they can be counted. The change was the insight that shares "
             "were one concept and that a rule tying two sets of shares together was "
             "false; exact rounding followed from that. On the lesson's illustration "
             "the pie fixes the totals, but a team that only fixed the totals would "
             "still have had the wrong model."),
        ],
        "standard": (
            "Finish when you can retell the breakthrough and split a bill exactly.",
            "Given an amount and shares, give each part under rounding to nearest and "
            "under the share pie's allocation, state each total, and name the questions "
            "Evans's manager asked before taking the change."
        ),
        "note": (
            "The lab does arithmetic on the shares the lesson states. It cannot tell "
            "you whether a concept in your model is false to the business, whether a "
            "deeper one is waiting, or whether this is the month to change; Evans's "
            "story turns on all three, and they are judgements about a domain, a "
            "team and a deadline."
        ),
    },
    # ---------------------------------------------------------------- 02
    # Chapter 9, Making Implicit Concepts Explicit: opening (PDF p. 123 of the
    # operator's copy); Digging Out Concepts, Listen to Language (pp. 123-126),
    # with its shipping example (pp. 124-126); Scrutinize Awkwardness
    # (pp. 126-130), with its interest example; Contemplate Contradictions
    # (pp. 130-131); Read the Book (pp. 131-132); Try, Try Again (p. 132).
    # Quote: PDF p. 124 of the operator's copy, 19 words, quotes.py OK.
    # Lesson total: 19 words.
    {
        "slug": "digging-out-concepts",
        "title": "Digging Out Concepts",
        "module": "Chapter 9 · Making Implicit Concepts Explicit",
        "one_line": "Five places to look for a concept the model is missing: the team's language, the awkward code, the experts' contradictions, the field's books, and many quick experiments.",
        "summary": (
            "Chapter 9 asks how a deep model is actually reached, and answers that it "
            "starts when a concept hinted at in conversation or buried in the design "
            "is made explicit. Read Evans's five ways of digging one out, then lay a "
            "library's vocabulary out for its experts, its developers and its code, "
            "and find the words the code has no name for."
        ),
        "key": [
            "deep models start with explicit concepts",
            "listen to the language of the team",
            "dig where the design is awkward",
            "a contradiction can hide a concept",
            "read the field's own literature",
            "try many leads; keep few",
        ],
        "key_label": "Digging out concepts in six lines",
        "concepts_intro": (
            "Three terms carry the lesson. The first is the chapter's, the second "
            "Chapter 2's, the third the lab's."
        ),
        "concepts": [
            ("Implicit concept",
             "Something the domain experts or the code rely on without the model "
             "naming it: a word used in meetings that matches no class, or a rule "
             "spread through several methods that no object owns."),
            ("Ubiquitous Language",
             "The vocabulary built on the model and used by everyone on the team, in "
             "speech, documents, diagrams and code, so that a word means the same thing "
             "wherever it appears. A term missing from it is, for Evans, an opening "
             "to improve the model."),
            ("A translation",
             "In the lab, a pair of audiences that use different names for the same "
             "concept, so that someone must convert one name to the other whenever "
             "they talk. The lab counts one for each such pair."),
        ],
        "read_title": "The five ways first, then the vocabulary laid out",
        "read_intro": (
            "Read the opening of Chapter 9 and Digging Out Concepts in your own copy "
            "first. The lesson reads the five ways as tools, with the book's examples "
            "summarised, and then counts one of them on a glossary."
        ),
        "body": [
            ("p", "&ldquo;When the users or domain experts use vocabulary that is "
                  "nowhere in the design, that is a warning sign.&rdquo; The sentence "
                  "is from Listen to Language, the first of the ways to find a concept "
                  "that Chapter 9, Making Implicit Concepts Explicit, sets out. Read "
                  "the chapter's opening and Digging Out Concepts in your own copy "
                  "first."),
            ("p", "The chapter begins where the last one left off. A deep model, Evans "
                  "says, gets its power from concepts that state the users' knowledge "
                  "compactly, and the work starts with getting the essential concepts "
                  "into the model at all, however crudely; refining them takes many "
                  "rounds after that. Most of the changes he cares about happen when "
                  "developers notice something the conversation keeps suggesting "
                  "or the design quietly depends on, and then give it an object or a "
                  "relationship. Now and then that step is itself a breakthrough. "
                  "More often the breakthrough comes later, once several such "
                  "concepts are in place and have been reshaped a few times."),
            ("p", "Listen to Language is the first tool. Notice the terms the experts "
                  "use that say something complicated in a word, the times they gently "
                  "correct your choice of word, and the phrase that makes their "
                  "puzzled looks go away. Evans is careful to say this is not the old "
                  "rule that every noun becomes an object: a new word is a lead, to be "
                  "followed up in conversation until a clean concept is carved out. And "
                  "he raises the stakes in one sentence: if the developers and the "
                  "experts are both using a term the design does not contain, the "
                  "warning is twice as strong. The book's example, from its shipping "
                  "domain, is a conversation in which a word on a printed report "
                  "turned out to name the object that connected two applications, and "
                  "giving it a class simplified a service's interface, removed "
                  "duplicated logic and took domain rules out of the report."),
            ("p", "Scrutinize Awkwardness is for when the concept is not in anyone's "
                  "mouth. Dig in the most awkward part of the design, where the procedures "
                  "are hard to explain and each new "
                  "requirement adds complexity, and bring the experts into the search, "
                  "using them at least as judges of the ideas you bring. The book's "
                  "example is an investment application whose interest calculation "
                  "was growing out of control; a conversation with an expert about "
                  "how the business actually records earnings turned up a term the "
                  "model lacked, and separating it from payments made fees and "
                  "interest the same kind of thing."),
            ("p", "Contemplate Contradictions takes seriously what two experts say "
                  "when it cannot all be true, or what one expert says on two days. "
                  "Much of it is loose wording or misunderstanding, but what is left "
                  "can point to a deeper model, as Evans illustrates with Galileo's "
                  "thought experiment of a ball dropped from a moving horse. Not every "
                  "contradiction should be resolved, he adds, and Chapter 14 is about "
                  "how to manage those that stay; but asking how both statements could "
                  "be true of the same world is revealing even then."),
            ("p", "Read the Book means the literature of the field. Many domains have "
                  "books that set out their fundamental concepts, and a developer "
                  "with an unhelpful expert can start from them; Evans retells his "
                  "interest example with a developer who learns the missing term from "
                  "an introductory accounting book, and notes that she then asked "
                  "better questions, which changed how the expert treated her. Books "
                  "by other software developers who have modelled the domain, such as "
                  "Fowler's <em>Analysis Patterns</em>, are a second source; Chapter "
                  "11 returns to them. Try, Try Again is the honest end of the list: "
                  "Evans may follow half a dozen leads before one is worth trying, "
                  "and will replace that one later. Experiments are how a team learns, "
                  "and a modeller cannot afford to be attached to an idea."),
            ("p", "Now a model of the lesson's own: a public library. The lab takes a "
                  "glossary with one name per audience for each concept, the "
                  "librarians, the developers and the code, and a dash where an "
                  "audience has no name; it compares names ignoring letter case, so the "
                  "glossary writes the code's `PickupWindow` as pickup-window. It reports the concepts, those every audience "
                  "names alike, the translations a conversation needs (for each "
                  "concept, each pair of audiences whose names differ), the names "
                  "each audience is missing, and any name one audience uses for two "
                  "concepts."),
            ("p", "On the preset <code>library-before</code> there are 8 concepts and "
                  "only one, the loan, is named alike by all three audiences, and a "
                  "conversation that touches each concept once needs 12 translations. "
                  "The code "
                  "has no name for 2 of them: the recall, when a librarian asks for a "
                  "book back early because someone else is waiting, and the pickup "
                  "window, the days a held book waits on the shelf. Look at the row for "
                  "recall: the librarians and the developers both say it, and the code "
                  "has nothing. That is Evans's doubly strong warning, and it is "
                  "worth more than the count. The lab also finds one name doing two "
                  "jobs: the developers say reservation both for a hold on a book and "
                  "for a study-room booking, which the code keeps apart."),
            ("p", "The preset <code>library-after</code> is the glossary once the team "
                  "has listened. Recall and pickup window are classes; the developers "
                  "say hold and booking, as the librarians do; the code's renewal and "
                  "fine use the librarians' words. Every concept is named, and only one "
                  "concept still needs translating, at 2 pairs: the code says user where everyone else "
                  "says patron, because the class is shared with the login system. "
                  "Whether that last rename is worth making is the kind of question "
                  "the lab cannot answer; it only shows that the translation is still "
                  "there."),
            ("h3", "Exercise"),
            ("ul", [
                "appointment: appointment, appointment, appointment",
                "did-not-attend: did-not-attend, no-show, no-show",
                "triage: triage, -, -",
                "care-episode: episode, case, -",
                "referral: referral, referral, referral",
                "clinician: clinician, doctor, user",
            ]),
            ("p", "A clinic's glossary, one concept a line, in the order experts, "
                  "developers, code. Find the concepts the code cannot name, and among "
                  "them the one Evans would call a doubly strong warning. Count the "
                  "translations for the concepts every audience names. Then type the "
                  "glossary into the lab to check."),
            ("p", "Some of what the experts talk about is not a thing at all but a "
                  "rule or a procedure. The next lesson, Explicit Constraints and "
                  "Processes as Domain Objects, reads how to model those."),
        ],
        "lab": ("dddkit", {
            "mode": "lang",
            "view": "glossary",
            "audiences": "experts developers code",
            "preset": "library-before",
            "presets": [
                {"id": "library-before",
                 "label": "A library's vocabulary before the team listened",
                 "terms": (
                     "loan, loan, loan, loan; "
                     "patron, patron, user, user; "
                     "hold, hold, reservation, reservation; "
                     "room-booking, booking, reservation, room-booking; "
                     "recall, recall, recall, -; "
                     "pickup-window, pickup-window, pickup-deadline, -; "
                     "renewal, renewal, extension, extension; "
                     "fine, fine, fine, penalty"
                 ),
                 "expect": {"dlnConcepts": "8", "dlnAlike": "1: loan", "dlnTranslations": "12",
                            "dlnMissing": "2: recall, pickup-window (code)",
                            "dlnAmbiguous": "1: reservation (developers: hold, room-booking)"}},
                {"id": "library-after",
                 "label": "The same library once the language is shared",
                 "terms": (
                     "loan, loan, loan, loan; "
                     "patron, patron, patron, user; "
                     "hold, hold, hold, hold; "
                     "room-booking, booking, booking, booking; "
                     "recall, recall, recall, recall; "
                     "pickup-window, pickup-window, pickup-window, pickup-window; "
                     "renewal, renewal, renewal, renewal; "
                     "fine, fine, fine, fine"
                 ),
                 "expect": {"dlnTranslations": "2", "dlnMissing": "0: none", "dlnAmbiguous": "0: none"}},
            ],
            "panel_title": "The words the code cannot say",
        }),
        "steps_title": "Finding the words the design lacks",
        "steps_intro": "Four steps, the last of them on a system of your own.",
        "steps": [
            ("Write the glossary",
             "For each concept, write the name the experts use, the name the "
             "developers use and the class or field in the code, with a dash where "
             "there is none."),
            ("Mark the missing names",
             "List the concepts with a dash in the code column, and mark those that the "
             "experts and the developers both name: the doubly strong warnings."),
            ("Count the translations",
             "For each concept, count the pairs of audiences whose names differ, and "
             "note any name one audience uses for two concepts."),
            ("Do it on your own code",
             "Write down six words the experts on a system you know use in meetings. "
             "Count how many name no class or field in the code, write the figure "
             "down, and pick the one you would follow up first."),
        ],
        "worked": {
            "title": "The library before the team listened",
            "intro": [
                "Read <code>library-before</code> row by row.",
            ],
            "lines": [
                "loan: one name everywhere, alike",
                "patron, user, user: 2 pairs differ",
                "recall: said by two, no class: a warning",
                "pickup window: no class either",
                "reservation: two concepts, one word",
                "code missing 2: recall, pickup-window",
            ],
            "after": [
                "Of the two concepts with no class, recall is the stronger lead, because "
                "the developers already say the word. Whether to make it a class, a state "
                "of a loan or an event is the knowledge crunching Evans describes, and "
                "the glossary does not decide it.",
            ],
        },
        "quiz_title": "Listening, digging and the glossary",
        "quiz": [
            {"q": "In the exercise's clinic glossary (experts, developers, code), which "
                  "concept does the code have no name for at all, although the experts and "
                  "the developers both name it? That is the lesson's reading of Evans's "
                  "doubly strong warning.",
             "a": ["triage",
                   "care-episode",
                   "did-not-attend",
                   "clinician"],
             "c": 1,
             "why": "The code cannot name triage or care-episode. Only the experts say "
                    "triage, so it is a warning; the experts say episode and the "
                    "developers say case, so both use a term for care-episode and the "
                    "code has none, the doubly strong case, even though their two "
                    "words differ. Did-not-attend and clinician have names in the "
                    "code; they cost translations, 2 and 3 pairs, not missing names. "
                    "Among the four concepts all three audiences name, the "
                    "translations are 0 + 2 + 0 + 3 = 5; the lab's total, 6, adds the "
                    "episode and case pair of care-episode. Read word by word, Evans's "
                    "warning also touches clinician: neither clinician nor doctor is in "
                    "the code, which says user. The lab counts that as 3 translations, "
                    "not as a missing name."},
            {"q": "In Listen to Language, how does Evans distinguish his advice from "
                  "making every noun an object?",
             "a": ["He does not: each new noun is a candidate class",
                   "A new word is a lead to follow up in conversation until a clean concept emerges",
                   "Only nouns the developers use should become objects",
                   "Verbs, not nouns, should become objects"],
             "c": 1,
             "why": "He says explicitly that this is not the old idea that nouns are "
                    "objects: hearing a word produces a lead, which knowledge crunching "
                    "turns, or does not turn, into a useful concept."},
            {"q": "According to Scrutinize Awkwardness, where should you dig for a "
                  "concept nobody has named?",
             "a": ["In the part of the design that is most awkward, where each new requirement adds complexity",
                   "In the newest code, which has had least refactoring",
                   "In the database schema, which shows what is stored",
                   "In the user interface, where the users see the model"],
             "c": 0,
             "why": "Evans names the most awkward part of the design: procedures whose "
                    "work is hard to explain, where every requirement "
                    "seems to add complexity. He adds that you need the experts there, at "
                    "least as validators of your ideas."},
            {"q": "What does Contemplate Contradictions say about contradictions that "
                  "remain after the misunderstandings are cleared away?",
             "a": ["They must all be resolved before the model is sound",
                   "They are always differences of wording",
                   "Not all should be reconciled, but asking how both could be true can still reveal something",
                   "They show that one of the experts is wrong"],
             "c": 2,
             "why": "Evans says it is not practical, perhaps not even desirable, to "
                    "reconcile every contradiction, and points to Chapter 14 for how to "
                    "manage those that stay; contemplating how both statements could "
                    "describe one reality is revealing even then."},
        ],
        "mistakes": [
            ("Waiting for the missing concept to be handed to you",
             "Evans's five ways are active: listen for the words, dig in the awkward "
             "code, take contradictions seriously, read the field's books, and run many "
             "small experiments. His second accrual story shows a developer whose "
             "expert would not help, who found the concept in an accounting book and "
             "won the expert's attention by asking better questions."),
            ("Turning every term the experts use into a class",
             "Listen to Language says outright that this is not the nouns-are-objects "
             "rule. A word is a lead to follow up; the result may be a class, a "
             "relationship, a rule or nothing. On the lesson's illustration the "
             "glossary lists what is missing, not what to build."),
            ("Expecting the first good idea to last",
             "Try, Try Again describes following half a dozen leads before one is "
             "worth trying, and replacing that one later. Evans does not count the "
             "changes of direction as waste: each leaves deeper insight in the model and "
             "a design easier to change the next time."),
        ],
        "standard": (
            "Finish when you can name the five ways and find a missing term.",
            "Given a glossary for experts, developers and code, list the concepts the "
            "code cannot name, mark the doubly strong warnings, and count the "
            "translations a conversation needs."
        ),
        "note": (
            "The lab compares names in a glossary you type. It cannot hear a "
            "conversation, tell a real concept from a passing word, or say whether a "
            "missing name should become a class, a rule or nothing; that is the "
            "knowledge crunching the chapter describes, done with the experts."
        ),
    },
    # ---------------------------------------------------------------- 03
    # Chapter 9, How to Model Less Obvious Kinds of Concepts (PDF p. 132 of the
    # operator's copy); Explicit Constraints (pp. 132-134), with its warning
    # signs (p. 134) and the overbooking review (p. 134); Processes as Domain
    # Objects (pp. 134-135).
    # Quotes: PDF p. 132, 10 words, quotes.py OK; PDF p. 135, 20 words,
    # quotes.py OK. Lesson total: 30 words.
    {
        "slug": "constraints-and-processes",
        "title": "Explicit Constraints and Processes as Domain Objects",
        "module": "Chapter 9 · Making Implicit Concepts Explicit",
        "one_line": "Two kinds of concept an object model does not suggest by itself: a rule that limits what objects may do, and a procedure the business itself talks about.",
        "summary": (
            "Things and their actions are what objects make easy to see; Chapter 9 "
            "names other kinds of concept that deserve a place in the model. Read "
            "Evans on constraints, his three signs that one is distorting its host, and "
            "his test for which processes belong in the model, then count where a "
            "theatre's sales limit puts its decisions before and after it is given a "
            "name."
        ),
        "key": [
            "objects suggest things, not rules",
            "a constraint can be a named method",
            "or an object, when it outgrows its host",
            "three signs a host is distorted",
            "a process the experts discuss is a concept",
            "the test: experts, or mechanism?",
        ],
        "key_label": "Constraints and processes in six lines",
        "concepts_intro": (
            "Three terms carry the lesson. The first two are the chapter's, the third "
            "the lab's."
        ),
        "concepts": [
            ("Constraint",
             "A rule that limits the states objects may be in or the changes they may "
             "make, such as a total that may not pass a limit. Evans counts constraints "
             "among the most important model concepts, and among the most often left "
             "implicit."),
            ("Process as a domain object",
             "A procedure that the business itself recognises, such as routing, "
             "represented in the model as a Service or, where it can be "
             "carried out in several ways, as interchangeable objects, one for each way."),
            ("Decision points",
             "The lab's count: one, plus one for each if, while, for and case, and for "
             "each conditional and and conditional or. It is McConnell's measure, from "
             "Code Complete, used here to see where a rule's decisions sit."),
        ],
        "read_title": "The argument first, then the rule moved, then the count",
        "read_intro": (
            "Read How to Model Less Obvious Kinds of Concepts, through Processes as "
            "Domain Objects, in your own copy first. The lesson reads the section as an "
            "argument, then moves a rule out of its host and counts what moved."
        ),
        "body": [
            ("p", "&ldquo;Constraints make up a particularly important category of model "
                  "concepts.&rdquo; Evans opens Explicit Constraints with that sentence, "
                  "in the part of Chapter 9 called How to Model Less Obvious Kinds of "
                  "Concepts. Read it, and Processes as Domain Objects after it, in your "
                  "own copy first."),
            ("p", "The section starts from what objects make easy. Object-oriented design "
                  "leads you to look for things, even abstract ones, and the actions they "
                  "take, the nouns and verbs of the introductory books. Evans names three "
                  "further kinds of concept that were not obvious to him when he started "
                  "with objects, and that made his designs sharper as he learned each: "
                  "constraints, processes, and Specification, which has a lesson of its "
                  "own after this one."),
            ("p", "A constraint sometimes has a natural home. An object whose contents "
                  "may not exceed a capacity can enforce that with a conditional in each "
                  "operation that changes the contents, and while the rule is that "
                  "simple, it is plain to see. Evans's move is to factor the rule into a "
                  "method of its own with a name that states what the constraint means. "
                  "The behaviour is the same; what changes is that the rule is now a "
                  "named thing the team can discuss, its link to the model is visible, "
                  "and it has room to grow, so that a more complicated rule can become "
                  "longer than the method that calls it without burying that method."),
            ("p", "Sometimes a method is not enough, and Evans gives three warning signs "
                  "that a rule is distorting the object that holds it. Checking "
                  "the rule needs data that does not otherwise belong in the object. "
                  "Rules of the same kind turn up in several classes, so they are "
                  "copied, or classes that share nothing else are made to inherit from "
                  "each other. Or the "
                  "design and requirements conversations keep returning to the rule "
                  "while in the code it is hidden in procedural logic. Then the "
                  "constraint can become an explicit object, or even a small set of "
                  "objects and relationships. His example is a review of Chapter 1's "
                  "overbooking policy, which was made a class of its own; the Object "
                  "Constraint Language of Warmer and Kleppe is his pointer for a fuller, "
                  "semiformal treatment."),
            ("p", "Processes as Domain Objects begins with a caution: procedures should "
                  "not become a prominent part of the model, since objects exist to "
                  "encapsulate them. What Evans means are processes that exist in the "
                  "domain itself. A Service is one way to make such a process explicit "
                  "while hiding a complicated algorithm, and where the process can "
                  "be carried out in several ways, each way can be an object, a "
                  "Strategy, which Chapter 12 develops. His test for which processes to "
                  "model is short: &ldquo;Is this something the domain experts talk "
                  "about, or is it just part of the mechanism of the computer "
                  "program?&rdquo;"),
            ("p", "Now a model of the lesson's own: a theatre's box office. A performance "
                  "may not sell more seats than its capacity less the seats held back "
                  "for wheelchair users and their companions, and on a preview night a "
                  "tenth of the house is kept for members, so a non-member's purchase "
                  "has a lower limit. The first listing writes that rule inline, in the "
                  "method that sells seats. On the preset <code>inline-limit</code> the "
                  "lab counts 5 decision points, the starting one, 2 ifs and 2 "
                  "conditional ands, all of them in `sell`."),
            ("code", _lines(INLINE_LIMIT)),
            ("p", "The second design names the rule `SalesLimit` and asks it. The caller, "
                  "preset <code>factored-caller</code>, now counts 2, the starting one and one "
                  "if: one question and its two outcomes. The constraint, preset "
                  "<code>factored-constraint</code>, counts 4, the starting one, an if and 2 "
                  "conditional ands. Look at what the counts say together. The decisions themselves, the "
                  "ifs and the conditional ands, number 4 in the inline listing and 1 + "
                  "3 = 4 across the two classes: factoring removed no decision. It moved "
                  "three of them to an object whose name says what they are, and left "
                  "the seller with one. The 6 of the two listings against the 5 of "
                  "one is only the rule's starting one, counted once for each routine. The deepest "
                  "nesting the lab reports, 3 in the inline listing, is the "
                  "class, the method and an if (the lab's first line at that depth, 11, "
                  "is the preview reduction)."),
            ("code", _lines(FACTORED_CALLER)),
            ("code", _lines(FACTORED_CONSTRAINT)),
            ("p", "Read the inline listing against Evans's warning signs. The members' "
                  "tenth on preview nights and a patron's membership are needed only "
                  "by the limit, not by selling as such, which is the nearest thing "
                  "here to the first sign; a matinee discount or a group booking limit "
                  "would put related rules beside it, which is the second; and if the box "
                  "office manager talks about the preview allocation every week, the "
                  "third applies too. The process test applies the same way: allocating "
                  "the best seats to a party is something the box office discusses, and "
                  "would earn a place in the model, while the loop that walks the "
                  "seating plan to do it would not. None of this is in the count."),
            ("h3", "Exercise"),
            ("code", _lines(CLINIC_BOOKING)),
            ("p", "A clinician's diary with a booking rule inside `book`. Count the "
                  "decision points by the lab's rule, with the breakdown. Then say which "
                  "of Evans's three warning signs the rule shows, and sketch the named "
                  "constraint you would move it to. Paste the listing into the lab to "
                  "check the count; the design is yours."),
            ("p", "Specification is the third kind of concept, narrower than these two "
                  "and very common. The next lesson, Specification, reads it."),
        ],
        "lab": ("cckit", {
            "mode": "code",
            "view": "complexity",
            "bands": [5, 10],
            "book": "other",
            "preset": "inline-limit",
            "presets": [
                {"id": "inline-limit",
                 "label": "The sales limit written inline in sell()",
                 "code": INLINE_LIMIT,
                 "expect": {"coDecisions": "5", "coBreakdown": "1 + if 2 + && 2", "coDepth": "3"}},
                {"id": "factored-caller",
                 "label": "The seller, once the limit has a name",
                 "code": FACTORED_CALLER,
                 "expect": {"coDecisions": "2", "coBreakdown": "1 + if 1"}},
                {"id": "factored-constraint",
                 "label": "The limit as an object of its own",
                 "code": FACTORED_CONSTRAINT,
                 "expect": {"coDecisions": "4", "coBreakdown": "1 + if 1 + && 2"}},
            ],
            "panel_title": "Where a constraint's decisions sit",
            "panel_intro": _COMPLEXITY_INTRO,
        }),
        "steps_title": "Giving a constraint a name and a home",
        "steps_intro": "Four steps, the last of them on code of your own.",
        "steps": [
            ("Find the rule",
             "In the method, mark every line that exists only to enforce the "
             "constraint, and count its decision points."),
            ("Check the warning signs",
             "Ask whether the rule needs data the object does not otherwise need, "
             "whether related rules appear elsewhere, and whether the team discusses it "
             "more than the code shows it."),
            ("Name it and move it",
             "Factor the rule into a method or object whose name says what the "
             "constraint means. Count the caller and the constraint separately, and "
             "check that the decisions add up to the same number."),
            ("Do it on your own code",
             "Find a method in a system you know that enforces a rule the business "
             "talks about. Count its decision points, write the figure down, and write "
             "the name you would give the rule."),
        ],
        "worked": {
            "title": "The theatre's limit, inline and named",
            "intro": [
                "Count <code>inline-limit</code>, then the two factored presets.",
            ],
            "lines": [
                "inline: 1, if 2, conditional and 2: 5",
                "caller: 1, if 1: 2",
                "constraint: 1, if 1, conditional and 2: 4",
                "decisions: 4 inline, 1 + 3 factored",
                "the extra 1: a second routine's start",
            ],
            "after": [
                "Factoring changed where the rule lives and what it is called, not how "
                "much deciding it takes. That is Evans's claim for it: the constraint "
                "becomes visible and has room to grow, and the seller stays focused on "
                "selling.",
            ],
        },
        "quiz_title": "Constraints, processes and their decisions",
        "quiz": [
            {"q": "By the lab's rule (one, plus one for each if, while, for, case, "
                  "conditional and, and conditional or), how many decision points does "
                  "the exercise's `book` method have, and with what breakdown?",
             "a": ["5: 1 + if 2 + for 1 + || 1",
                   "6: 1 + if 2 + for 1 + && 1 + || 1",
                   "7: 1 + if 2 + for 1 + && 1 + || 1 + ! 1",
                   "4: 1 + if 2 + for 1"],
             "c": 1,
             "why": "One, plus the `for` over the diary, the `if` on the day, the `if` on "
                    "the booking rule, the conditional and after `!urgent` and the "
                    "conditional or inside the brackets: 6. A negation is not a decision "
                    "point by the rule, and the `==` that sets `saturday` is a comparison, "
                    "not a branch. Which warning sign the rule shows is a judgement: the "
                    "Saturday closure and the urgent exemption are clinic policy sitting "
                    "in a clinician's diary, and if scheduling meetings keep returning to "
                    "them while the code hides them in one condition, that is Evans's "
                    "third sign."},
            {"q": "Which of these is not one of Evans's three warning signs that a "
                  "constraint is distorting its host object?",
             "a": ["Checking it needs data the object does not otherwise need",
                   "Rules of the same kind recur in several classes, copied or shared by inheritance",
                   "The team discusses it often, but the code hides it in procedural logic",
                   "Its method has more decision points than its caller"],
             "c": 3,
             "why": "The first three are the book's list. A constraint method longer than "
                    "its caller is something Evans says factoring allows, giving the rule "
                    "room to grow, not a sign of trouble."},
            {"q": "What test does Processes as Domain Objects give for whether a process "
                  "belongs in the model?",
             "a": ["Whether it has more than one implementation",
                   "Whether it takes longer than one transaction",
                   "Whether the domain experts talk about it, or it is only part of the program's mechanism",
                   "Whether it can be written as a Service"],
             "c": 2,
             "why": "Evans calls the test simple: is it something the experts talk about, "
                    "or just part of how the program works? More than one way to carry it "
                    "out is his reason for making each way a Strategy, and a Service is one "
                    "way of expressing a process once it qualifies."},
            {"q": "On the lesson's presets, the inline listing counts 5 and the two factored "
                  "listings count 2 and 4. What does that show?",
             "a": ["Factoring added a decision to the rule",
                   "The same 4 decisions, 1 left in the seller and 3 moved to the constraint; the 6 counts each routine's starting one",
                   "Factoring removed one decision from the seller and none from the rule",
                   "The factored design is more complex and should be reverted"],
             "c": 1,
             "why": "The ifs and conditional ands are 2 + 2 inline and 1 + (1 + 2) "
                    "factored: 4 either way. Each listing's count starts at one, so two "
                    "listings start at two. The count is a reason to look, not a verdict; "
                    "the last option turns it into one."},
        ],
        "mistakes": [
            ("Leaving a rule inline because it works",
             "Both of Evans's versions of his capacity example enforce the rule; his "
             "point is that the factored one has a clearer relation to the model and "
             "room to grow. When a rule needs data its host does not, recurs across "
             "objects, or fills the conversations while hiding in the code, it is "
             "distorting the host, and working is not the question."),
            ("Expecting factoring a constraint out to reduce the decisions",
             "On the lesson's illustration the decisions number 4 before and after. "
             "Factoring moves them, names them and gives them room; it does not make the "
             "rule simpler than it is. A smaller count in the caller is a consequence of "
             "where the rule now lives."),
            ("Modelling every procedure as a domain object",
             "Evans begins the section by agreeing that procedures should not be a "
             "prominent part of the model. Only processes that exist in the domain, "
             "that the experts talk about, belong there; the loop that carries one out "
             "is mechanism."),
        ],
        "standard": (
            "Finish when you can move a constraint out and say where its decisions went.",
            "Given a method that enforces a rule inline, count its decision points, "
            "name the warning signs it shows, and count the caller and the named "
            "constraint after factoring."
        ),
        "note": (
            "The lab counts decision points by a rule. It cannot tell a business "
            "constraint from a technical check, or a process the experts discuss from "
            "the mechanism behind it; Evans's test is a question for the experts, and "
            "the count only shows where the decisions sit."
        ),
    },
    # ---------------------------------------------------------------- 04
    # Chapter 9, Specification (PDF pp. 135-137 of the operator's copy):
    # Boolean test methods and the delinquent invoice (p. 135); logic
    # programming's predicates (pp. 135-136); the pattern statement (p. 136);
    # combining, deferred to Chapter 10 (p. 136); Factory configuration and the
    # built-in date (p. 137); a pattern is not a cookbook (p. 137). Developed
    # with Fowler (Evans and Fowler 1997, p. 135).
    # Quote: PDF p. 135 of the operator's copy, 16 words, quotes.py OK.
    # Lesson total: 16 words.
    {
        "slug": "specification",
        "title": "Specification",
        "module": "Chapter 9 · Making Implicit Concepts Explicit",
        "one_line": "A rule that has outgrown a test method becomes a small value object of its own, which says whether a given object satisfies it.",
        "summary": (
            "A test method on an object is often a little rule, and some rules grow "
            "until they swamp the object they test. Read Evans's case for keeping such "
            "rules in the domain layer as predicate-like value objects, the pattern he "
            "developed with Martin Fowler, then check seed lots against a seed bank's "
            "distribution rule, clause by clause."
        ),
        "key": [
            "a test method is often a little rule",
            "rules can swamp the object they test",
            "moving them out of the domain is worse",
            "borrow the idea of a predicate",
            "a specification: a value object rule",
            "it answers: does this object satisfy it?",
        ],
        "key_label": "Specification in six lines",
        "concepts_intro": (
            "Three terms carry the lesson. The first is logic programming's, the second "
            "the pattern's, the third the lab's."
        ),
        "concepts": [
            ("Predicate",
             "A function that returns true or false and can be combined with others "
             "by and and or to state a more complicated rule. Evans borrows the idea "
             "from logic programming without adopting the whole paradigm."),
            ("Specification",
             "A value object whose one job is to say whether another object meets "
             "some criteria. It keeps a business rule in the domain layer without "
             "loading it onto the object being tested."),
            ("A clause",
             "In the lab, one comparison in a specification, such as moisture at most "
             "8. The lab evaluates each clause on the candidate and reports which are "
             "true and which is the first, in the order written, that is false."),
        ],
        "read_title": "The problem first, then the pattern, then a lot checked",
        "read_intro": (
            "Read Specification in Chapter 9, up to Applying and Implementing "
            "Specification, in your own copy first. The lesson reads the pattern as a "
            "tool, then checks single candidates against one."
        ),
        "body": [
            ("p", "&ldquo;In all kinds of applications, Boolean test methods appear that "
                  "are really parts of little rules.&rdquo; That is how Evans opens "
                  "Specification, the narrowest of the three kinds of concept Chapter 9 "
                  "names and, he says, a common one. He developed the pattern with Martin "
                  "Fowler. Read the pattern in your own copy first, up to Applying and "
                  "Implementing Specification, which is the next lesson."),
            ("p", "The problem is a test method that grows. A method that asks whether a "
                  "bill is past its due date is a one-line rule, and it belongs on the "
                  "bill. A method that asks whether the bill is delinquent starts the "
                  "same way, then needs a grace period that depends on the customer's "
                  "account, the payment history, policy for different product lines, "
                  "and the difference between a bill due a second notice and one due "
                  "for a collection agency. The object's plain meaning, a request for "
                  "payment, disappears under the rules, and it picks up dependencies on "
                  "classes and subsystems that have nothing to do with that meaning."),
            ("p", "The usual rescue, Evans says, is worse. Developers move the rules out "
                  "to the application layer, which leaves the domain object a bundle of "
                  "data that no longer expresses the rules of the business, while the "
                  "rules sit in code that is not about the model. The rules belong "
                  "in the domain layer, and they do not fit in the object being tested."),
            ("p", "Logic programming has an answer: rules written as predicates, "
                  "functions that return true or false and combine with and and or. "
                  "Evans notes that people have tried to build full logic programming "
                  "out of objects, with mixed results, and that a full implementation is "
                  "a major undertaking, general enough that it says little about intent. "
                  "His proposal is narrower. Most rules fall into a few special cases, "
                  "so borrow only the concept: a specialised object that evaluates to a "
                  "Boolean, a little truth test factored out as a Value Object, which "
                  "can be asked about another object. That object is a Specification. "
                  "It says what another object's state must be, and its most basic "
                  "use is to test whether a given object satisfies the criteria."),
            ("p", "Three details follow. Many specifications are simple tests like the "
                  "delinquency rule; when rules are complicated, specifications can be "
                  "combined as predicates are, which Chapter 10 develops. Because the "
                  "rule is a full object, a Factory can build it from information found "
                  "elsewhere, such as an account or a policy table, without coupling "
                  "the object being tested to those sources. And a specification can "
                  "carry what it needs: Evans's delinquency rule had its evaluation date "
                  "built in, because each instance was created, used on some bills and "
                  "discarded. He ends by calling a pattern a starting point, not a "
                  "cookbook, and suggests skimming the implementation detail until you "
                  "need it."),
            ("p", "Now a model of the lesson's own: a seed bank that sends lots of seed "
                  "to growers. A lot may go out when at least 85 percent of a test "
                  "sample sprouts, its moisture is at most 8 percent, it is at most 10 "
                  "years old, and it is not in quarantine. The listing writes that rule "
                  "as a specification; the lot itself knows its measurements and "
                  "nothing about the policy, and a Factory could read the thresholds "
                  "from the bank's policy table."),
            ("code", _lines(DISTRIBUTABLE_LOT)),
            ("p", "The lab takes the same rule as a list of clauses joined by and, and "
                  "one candidate, and reports whether the candidate satisfies the rule, "
                  "which clauses are true, the first false one in the order written, "
                  "and every false one. On the preset <code>lot-01</code> all 4 clauses "
                  "are true and the lot may go out. On <code>lot-02</code>, germination "
                  "88, moisture 9, age 5, not quarantined, 3 clauses are true and the "
                  "one false clause is moisture at most 8: the lot needs drying, not "
                  "discarding. On <code>lot-07</code>, germination 72, moisture 10, age "
                  "11, three clauses are false, and the first is germination at least 85."),
            ("p", "The order matters only for the first false clause, and the lab reports "
                  "every false one as well, because a seed bank deciding whether to dry "
                  "a lot, retest it or compost it needs all of them. That is a small "
                  "version of Evans's argument: once the rule is an object, the "
                  "question can be asked of any lot by any part of the system, and the "
                  "answer comes with its reasons. The lab cannot say whether 85 percent "
                  "is the right threshold; the bank's curators can."),
            ("h3", "Exercise"),
            ("ul", [
                "Rule: germination >= 85 and moisture <= 8 and age <= 10 and quarantine = no.",
                "Candidate lot-08: germination 85, moisture 8, age 11, quarantine yes.",
            ]),
            ("p", "Evaluate each clause on lot-08 by hand. Say whether the lot satisfies "
                  "the rule, which clauses are false, and which is the first false clause "
                  "in the order written. Then add lot-08 to the lab's candidates, "
                  "choose it, and check."),
            ("p", "A specification tests one object here. The next lesson, Applying and "
                  "Implementing Specification, uses the same rule to choose from a "
                  "collection and to say what should be built."),
        ],
        "lab": ("dddkit", {
            "mode": "spec",
            "view": "validate",
            "candidates": _LOTS,
            "spec": _DISTRIBUTABLE,
            "preset": "lot-01",
            "presets": [
                {"id": "lot-01",
                 "label": "lot-01: germination 93, moisture 6, age 2, not quarantined",
                 "candidate": "lot-01",
                 "expect": {"dspSatisfied": "yes", "dspTrue": "4 of 4", "dspFalse": "0: none"}},
                {"id": "lot-02",
                 "label": "lot-02: germination 88, moisture 9, age 5, not quarantined",
                 "candidate": "lot-02",
                 "expect": {"dspSatisfied": "no", "dspTrue": "3 of 4",
                            "dspFirstFalse": "clause 2, moisture <= 8: moisture is 9"}},
                {"id": "lot-07",
                 "label": "lot-07: germination 72, moisture 10, age 11, not quarantined",
                 "candidate": "lot-07",
                 "expect": {"dspSatisfied": "no", "dspTrue": "1 of 4",
                            "dspFirstFalse": "clause 1, germination >= 85: germination is 72",
                            "dspFalse": "3: germination >= 85, moisture <= 8, age <= 10"}},
            ],
            "panel_title": "One seed lot against the distribution rule",
        }),
        "steps_title": "Checking one object against a specification",
        "steps_intro": "Four steps, the last of them on a system of your own.",
        "steps": [
            ("Write the rule as clauses",
             "State the rule as comparisons joined by and, each naming one attribute, "
             "an operator and a value."),
            ("Evaluate each clause",
             "For the candidate, write true or false beside each clause, watching the "
             "boundaries: at least 85 admits 85, at most 10 refuses 11."),
            ("Give the verdict and its reasons",
             "The candidate satisfies the rule only if every clause is true. Name the "
             "first false clause and every false one."),
            ("Do it on your own code",
             "Find a Boolean method in a system you know that has grown past three "
             "conditions. Count its conditions, write the figure down, and write the "
             "name the specification would have."),
        ],
        "worked": {
            "title": "lot-07 against the rule",
            "intro": [
                "Evaluate <code>lot-07</code> clause by clause.",
            ],
            "lines": [
                "germination 72 at least 85: false",
                "moisture 10 at most 8: false",
                "age 11 at most 10: false",
                "quarantine no equals no: true",
                "1 clause true; not satisfied",
                "first false: germination at least 85",
            ],
            "after": [
                "Every false clause is a reason, and the first one is only the first "
                "written. A lot that fails on germination alone might be retested; one "
                "that fails on three counts is probably not worth the effort. That is "
                "the bank's judgement, which the specification informs.",
            ],
        },
        "quiz_title": "Rules, predicates and a lot checked",
        "quiz": [
            {"q": "In the exercise, lot-08 has germination 85, moisture 8, age 11 and is in "
                  "quarantine. Against the rule (germination >= 85 and moisture <= 8 and "
                  "age <= 10 and quarantine = no), what is the verdict?",
             "a": ["Satisfied: every threshold is met exactly",
                   "Not satisfied; false clauses germination and moisture, the first germination",
                   "Not satisfied; false clauses age and quarantine, the first age <= 10",
                   "Not satisfied; one false clause, quarantine = no"],
             "c": 2,
             "why": "85 is at least 85 and 8 is at most 8, so the first two clauses are "
                    "true; reading at least and at most as strict comparisons gives the "
                    "second option. Age 11 is more than 10, and the lot is quarantined, so "
                    "two clauses are false, and age <= 10 comes first in the order "
                    "written."},
            {"q": "Why does Evans reject moving a growing rule from the domain object into "
                  "the application layer?",
             "a": ["It makes the rule slower to evaluate",
                   "It leaves the domain object as data that no longer expresses the business rules",
                   "The application layer cannot reach the database",
                   "It breaks the object's identity"],
             "c": 1,
             "why": "The rules leave the domain layer entirely, and the object they were "
                    "about is left holding data that expresses none of them; the rules belong in the domain layer, "
                    "just not inside the object being tested."},
            {"q": "What does Evans take from logic programming for Specification?",
             "a": ["The whole paradigm, implemented in objects",
                   "Only the concept of a predicate, as specialised objects that evaluate to a Boolean",
                   "A rule engine that evaluates rules at run time",
                   "Nothing: Specification is unrelated to predicates"],
             "c": 1,
             "why": "He notes that building all of logic programming out of objects is a "
                    "large undertaking and too general to show intent, and borrows just the "
                    "concept: little truth tests factored out as value objects."},
        ],
        "mistakes": [
            ("Putting every rule about an object on the object",
             "A one-line test such as being past due belongs there. Evans's case is "
             "for rules that grow, that need an account's grace period, a policy table "
             "and a payment history: on the object they bury its meaning and drag in "
             "dependencies, and a Specification keeps them in the domain layer without "
             "that cost."),
            ("Thinking Specification means building a rule engine",
             "Evans warns that full logic programming in objects is a major undertaking "
             "and says too little about intent. The pattern borrows only the predicate: "
             "a small, special-purpose value object, often a simple test, combinable "
             "later when the rules require it."),
            ("Reading only the first false clause",
             "The first false clause depends on the order the rule was written in. On "
             "the lesson's illustration lot-07 fails three clauses, and a curator "
             "deciding what to do with it needs all three; the lab lists them for that "
             "reason."),
        ],
        "standard": (
            "Finish when you can state a rule as a specification and check one object.",
            "Given a rule as clauses and one candidate, evaluate each clause, give the "
            "verdict, and name the first false clause and every false one."
        ),
        "note": (
            "The lab evaluates the clauses as typed. It cannot say whether a threshold "
            "is right, whether a rule belongs in a specification or on the object, or "
            "whether two rules are the same rule written twice; those are questions "
            "about the domain, put to the people who know it."
        ),
    },
    # ---------------------------------------------------------------- 05
    # Chapter 9, Applying and Implementing Specification (PDF pp. 137-146 of
    # the operator's copy): the three uses (p. 137); Validation (p. 138);
    # Selection (Querying), in memory, SQL in the specification, the leak, the
    # repository's specialised query and double dispatch, the intermediate
    # solution, stored procedures, Mee and Hieatt (pp. 138-142); Building to
    # Order (Generating) and its four advantages (p. 142); the warehouse
    # examples and the working prototype example (pp. 143-146).
    # Quote: PDF p. 137 of the operator's copy, 16 words, quotes.py OK.
    # Lesson total: 16 words.
    {
        "slug": "applying-specification",
        "title": "Applying and Implementing Specification",
        "module": "Chapter 9 · Making Implicit Concepts Explicit",
        "one_line": "One rule, three jobs: test an object, choose from a collection, and say what must be built; the model stays one even when the implementations differ.",
        "summary": (
            "A specification can validate an object, select objects from a collection, "
            "or state what a generator must produce. Read Evans on why these are one "
            "concept, what each use costs to implement against a database or a "
            "generator, and how the same rule can test what was built, then select seed "
            "lots for a school garden and see why each of the rest is refused."
        ),
        "key": [
            "validate, select, build to order",
            "the same concept, different code",
            "a repository takes the specification",
            "keep table details out of the domain",
            "a generator told what, not how",
            "the request also tests the result",
        ],
        "key_label": "Applying Specification in six lines",
        "concepts_intro": (
            "Three terms carry the lesson. The first two are the section's, the third "
            "the lab's."
        ),
        "concepts": [
            ("Selection",
             "Using a specification to pick from a collection the objects that satisfy "
             "it, typically by passing it to a Repository, which may evaluate it in "
             "memory or translate it into a database query."),
            ("Building to order",
             "Using a specification to describe objects that do not exist yet, so that "
             "a generator's interface states what it must produce rather than how. The "
             "same specification can then check the result."),
            ("The first false clause",
             "In the lab, for each candidate a specification refuses, the first clause "
             "in the order written that the candidate fails: one reason, read in the "
             "rule's own terms."),
        ],
        "read_title": "The three uses first, then their costs, then a selection",
        "read_intro": (
            "Read Applying and Implementing Specification in Chapter 9 in your own copy "
            "first. The lesson reads the section as an argument for one concept with "
            "three implementations, then selects from a collection."
        ),
        "body": [
            ("p", "&ldquo;These three uses&mdash;validation, selection, and building to "
                  "order&mdash;are the same on a conceptual level.&rdquo; That is the "
                  "claim at the head of Applying and Implementing Specification, the "
                  "last section of Chapter 9. Read it in your own copy first; Evans "
                  "himself suggests skimming its detail until you need it, and this "
                  "lesson reads it for the argument."),
            ("p", "The three uses are to check whether an object is fit for some "
                  "purpose, to choose objects from a collection, and to say what a new "
                  "object must be like. Without a pattern, Evans says, one rule tends to "
                  "appear in all three places in different forms, which can come to "
                  "contradict each other, and the fact that it is one rule is lost. "
                  "With a specification the model stays one, even where the three "
                  "implementations have to differ."),
            ("p", "Validation is the plain case, and the last lesson's. Selection is "
                  "where the implementation gets interesting. If the objects are few "
                  "and already in memory, a Repository can take any specification and "
                  "return the objects that satisfy it, and the client's single line of "
                  "code states the concept. Usually they are in a relational database, "
                  "and Evans walks through the options. The specification can produce "
                  "its own SQL, which keeps the rule in one place but leaks the table "
                  "structure into the domain layer. Some mapping frameworks let a query "
                  "be stated in terms of the model's objects instead. Failing that, the "
                  "Repository can offer a specialised query that is not itself a rule, "
                  "and the specification chooses which to call, by double dispatch."),
            ("p", "He adds an intermediate design: a more generic query on the "
                  "Repository, with the specification filtering the results in memory. "
                  "It reads more clearly and costs some performance, and whether that "
                  "trade is acceptable, he says, depends entirely on circumstances; a "
                  "stored procedure, used for speed or for security, limits the "
                  "specification to the parameters the procedure accepts. None of these "
                  "choices changes the model. For the technical detail he points to Mee "
                  "and Hieatt's Repository in Fowler's book, read in the Repository "
                  "lesson of Enterprise Application Patterns; Fowler asks how the query "
                  "reaches the tables, and Evans asks that the rule it applies stay a "
                  "concept of the domain."),
            ("p", "Building to Order turns the specification around: it describes "
                  "objects that are not there yet, as a buyer's requirements describe "
                  "an aircraft no one has designed. A generator written as a procedure "
                  "defines its behaviour only implicitly, and the only ways to predict "
                  "it are to run it or read every line. A generator whose interface "
                  "takes a specification separates what is wanted from how it is "
                  "produced, states its rules where callers can read them, leaves the "
                  "request in the caller's hands, and is easier to test, because the "
                  "same specification can check the result, an Assertion in Chapter "
                  "10's terms."),
            ("p", "The book's long example packs a warehouse, and it is worth reading "
                  "for how it proceeds: validation first, to make the rules explicit "
                  "and to have a test for the packer, then a Service interface stated "
                  "in terms of the specifications, and then a deliberately naive "
                  "prototype behind that interface, so that the application team and "
                  "the optimisation team could each work against something real. Its "
                  "second example, a working prototype, makes the general point: once "
                  "interface and implementation are separate, any implementation that "
                  "honours the interface unblocks the people waiting on it."),
            ("code", _lines(THREE_USES)),
            ("p", "Now the seed bank again, with all seven lots and the lab's select "
                  "view, which reports the candidates, the names of those satisfying the "
                  "specification, and each failing candidate with its first false "
                  "clause. On the preset <code>distributable</code>, the last lesson's "
                  "rule selects 2 of 7, lot-01 and lot-06. Of the 5 refused, lot-03 and "
                  "lot-07 fail first on germination, lot-02 on moisture, lot-04 on age "
                  "and lot-05 on quarantine: one reason each, in the rule's own terms."),
            ("p", "A school asks for vegetable seed for its garden: germination at least "
                  "80 and at most 6 years old. On the preset <code>school-garden</code>, "
                  "written as just that, 3 lots are selected, lot-01, lot-03 and lot-05. "
                  "But lot-05 is in quarantine. The request was written as a new rule, "
                  "and it left out a clause the bank's own rule always carries. The "
                  "preset <code>school-garden-safe</code> adds it and selects 2, lot-01 "
                  "and lot-03, with lot-05 refused first at quarantine. That is a "
                  "cousin of Evans's warning: the bank's rule turned up again in a new "
                  "guise and lost a clause on the way, on the lesson's illustration; Chapter 10 shows how to build the request "
                  "from the bank's rule rather than retyping it."),
            ("h3", "Exercise"),
            ("ul", [
                "Lots: the seven of the presets.",
                "Rule: moisture <= 7 and (kind = herb or age <= 3).",
            ]),
            ("p", "By hand, find the lots the rule selects and, for each lot refused on "
                  "moisture, say so. Then type the rule into the lab to check, and read "
                  "the clause it blames for each lot refused for another reason."),
            ("p", "Chapter 9 ends with the rule as an object. The next course, Supple "
                  "Design, opens Chapter 10, on design that is a pleasure to change, "
                  "and combines specifications with and, or and not."),
        ],
        "lab": ("dddkit", {
            "mode": "spec",
            "view": "select",
            "candidates": _LOTS,
            "preset": "distributable",
            "presets": [
                {"id": "distributable",
                 "label": "The seven lots against the bank's distribution rule",
                 "spec": _DISTRIBUTABLE,
                 "expect": {"dspCandidates": "7", "dspSatisfying": "2: lot-01, lot-06"}},
                {"id": "school-garden",
                 "label": "A school's request, written as a new rule",
                 "spec": "kind = vegetable and germination >= 80 and age <= 6",
                 "expect": {"dspSatisfying": "3: lot-01, lot-03, lot-05"}},
                {"id": "school-garden-safe",
                 "label": "The same request, with the bank's quarantine clause",
                 "spec": "kind = vegetable and germination >= 80 and age <= 6 and quarantine = no",
                 "expect": {"dspSatisfying": "2: lot-01, lot-03"}},
            ],
            "panel_title": "Seed lots selected by a specification",
        }),
        "steps_title": "Selecting with a specification",
        "steps_intro": "Five steps, the last of them on a system of your own.",
        "steps": [
            ("List the candidates",
             "Write each candidate with its attributes, one per line."),
            ("Evaluate the rule on each",
             "For each candidate, evaluate the clauses in order and note the first "
             "false one, or that all are true."),
            ("Split the collection",
             "Write the names that satisfy the rule, and beside each of the rest its "
             "first false clause."),
            ("Compare a request with the standing rule",
             "When a new request is written, check it against the rule the business "
             "already applies, and add any clause it left out."),
            ("Do it on your own code",
             "Find a rule in a system you know that is checked on a form, filtered in "
             "a query and enforced when something is created. Count the places it is "
             "written, write the figure down, and say whether they agree."),
        ],
        "worked": {
            "title": "The school's request on seven lots",
            "intro": [
                "Work <code>school-garden</code>, then <code>school-garden-safe</code>.",
            ],
            "lines": [
                "lot-01: vegetable, 93, age 2: selected",
                "lot-02, lot-06: herbs, refused on kind",
                "lot-03: vegetable, 81, age 3: selected",
                "lot-04: a flower, refused on kind",
                "lot-05: vegetable, 90, age 6: selected",
                "lot-07: 72, refused on germination",
            ],
            "after": [
                "Three lots, one of them quarantined. Adding the bank's clause refuses "
                "lot-05 and leaves lot-01 and lot-03. The lab shows the difference; that "
                "the request should have carried the clause is a rule of the seed bank, "
                "which the lesson states.",
            ],
        },
        "quiz_title": "Three uses, one rule",
        "quiz": [
            {"q": "In the exercise, which of the seven lots does the rule moisture <= 7 "
                  "and (kind = herb or age <= 3) select?",
             "a": ["lot-01, lot-03 and lot-06",
                   "lot-01 and lot-03",
                   "lot-01, lot-03, lot-04 and lot-06",
                   "lot-01, lot-02, lot-03 and lot-06"],
             "c": 0,
             "why": "lot-02 (moisture 9), lot-05 (8) and lot-07 (10) fail on moisture. Of "
                    "the rest, lot-01 and lot-03 are 2 and 3 years old, lot-06 is a herb, "
                    "and lot-04, a 14-year-old flower, meets neither half of the or. "
                    "Leaving out lot-06 forgets the herb clause; adding lot-04 counts its "
                    "low moisture as enough; lot-02 is a herb but too damp."},
            {"q": "What does Evans say is wrong with a specification that produces its "
                  "own SQL?",
             "a": ["SQL cannot express the rule",
                   "Details of the table structure leak into the domain layer",
                   "It cannot be used for validation as well",
                   "It is always slower than filtering in memory"],
             "c": 1,
             "why": "It keeps the rule in one place, but the table layout now lives in a "
                    "domain object, so a mapping change must be tracked in more than one "
                    "place. The rule itself is easily stated in SQL, which is why Evans "
                    "calls SQL a natural way to write specifications."},
            {"q": "Which of these does Evans give as an advantage of a generator whose "
                  "interface takes a specification?",
             "a": ["The generator always finds the optimal result",
                   "The specification can also validate the generator's output",
                   "No implementation of the generator is needed until the end",
                   "The generator no longer needs a Service"],
             "c": 1,
             "why": "The four advantages are a decoupled implementation, rules stated in "
                    "the interface, flexibility for the caller, and easier testing, "
                    "because the same specification checks what was built. The "
                    "warehouse prototype in the book is deliberately far from optimal."},
            {"q": "On the preset <code>school-garden</code>, three lots are selected, one "
                  "of them quarantined. What does the lesson draw from that?",
             "a": ["The lab's evaluation of the and is wrong",
                   "Quarantine should not be a clause",
                   "A rule rewritten for a new use dropped a clause the standing rule carries",
                   "Selection and validation need different rules"],
             "c": 2,
             "why": "The request was typed as a fresh rule and omitted the bank's "
                    "quarantine clause, so it admitted lot-05; adding the clause, preset "
                    "<code>school-garden-safe</code>, refuses it. Evans's point is that "
                    "validation, selection and building to order should share one rule, "
                    "not that they need different ones."},
        ],
        "mistakes": [
            ("Writing a separate rule for each use",
             "A form's check, a report's filter and a generator's procedure can each "
             "state the same rule differently until they disagree. Evans's claim is that "
             "the three uses are one concept; on the lesson's illustration a request "
             "retyped as a new rule admitted a quarantined lot."),
            ("Thinking a specification must be evaluated in memory",
             "Evans walks through SQL in the specification, a query stated in model terms "
             "by a framework, a Repository query chosen by double dispatch, a generic "
             "query filtered in memory, and stored procedures. The model is the same in "
             "all of them; the implementation is chosen for the platform and the "
             "volumes, and he says the trade depends on circumstances."),
            ("Treating building to order as a different pattern",
             "A specification for objects not yet present is the same concept used the "
             "other way round. Its value, in Evans's list, is that the interface states "
             "the rules and that the same specification then tests the result."),
        ],
        "standard": (
            "Finish when you can use one rule to validate, select and build.",
            "Given a rule and a collection, select the candidates that satisfy it with "
            "each refusal's first false clause, and say how the same rule would check a "
            "generator's output."
        ),
        "note": (
            "The lab evaluates a rule on candidates you type. It runs no query and no "
            "generator, so it cannot show the performance trade Evans describes, or "
            "whether a rule retyped for a new use still means what the business means; "
            "it can show only that two rules select different lots."
        ),
    },
]
