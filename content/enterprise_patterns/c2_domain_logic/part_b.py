"""Organizing Domain Logic, lessons 5-7 -- Chapter 18's base patterns.

Fowler et al., Patterns of Enterprise Application Architecture (Addison-Wesley,
2002), Chapter 18, Base Patterns: Value Object, Money (whose allocation
conundrum is Matt Foemmel's, and whose example is Foemmel's and Fowler's) and
Special Case. Pages in the comments are PDF pages of the operator's copy, which
has no printed page numbers; the lessons cite by chapter and pattern. Every
quotation is copied from that copy and checked with ea_quotes.py; the one
figure attributed to the book carries its PLAN section S.2 id. The code is
written for these lessons: none of the book's listings or example domains is
reproduced, and the allocator rule is stated as the lab's rule, not as a
listing. Each snippet is one constant below, used both by the lesson's code
block and by the lab preset that counts it.
"""


def _lines(text):
    """A snippet constant as a code block's list of lines."""
    return text.split("\n")


# ---------------------------------------------------------------- snippets

# 2.5 Value Object: presets mutable-range, value-range; exercise (PLAN section D.4 and presets.py, verbatim).
DATE_RANGE_MUTABLE = """class DateRange {
    public LocalDate start;
    public LocalDate end;

    public void setEnd(LocalDate end) {
        this.end = end;
    }

    public boolean includes(LocalDate d) {
        return !d.isBefore(start) && !d.isAfter(end);
    }
}"""

DATE_RANGE_VALUE = """final class DateRange {
    private final LocalDate start;
    private final LocalDate end;

    DateRange(LocalDate start, LocalDate end) {
        this.start = start;
        this.end = end;
    }

    public boolean equals(Object o) {
        if (!(o instanceof DateRange)) { return false; }
        DateRange r = (DateRange) o;
        return start.equals(r.start) && end.equals(r.end);
    }

    public int hashCode() {
        return 31 * start.hashCode() + end.hashCode();
    }
}"""

QUANTITY_MUTABLE = """class Quantity {
    public int amount;
    public String unit;
    private final int max = 1000;

    public void add(int n) {
        amount = amount + n;
    }

    public String toString() {
        return amount + " " + unit;
    }

    int room() {
        return max - amount;
    }
}"""


# 2.6 Money: body only (PLAN section D.4 and presets.py, verbatim).
REFUND_SPLIT = """// Refunds an order across the payments that paid for it, in
// proportion to each; Money does the splitting, this checks it.
List<Refund> refund(Money total, List<Payment> paid) {
    long[] weights = new long[paid.size()];
    for (int i = 0; i < weights.length; i++) {
        weights[i] = paid.get(i).amount().cents();
    }
    Money[] parts = total.splitBy(weights);
    Money sum = Money.zero(total.currency());
    List<Refund> out = new ArrayList<Refund>();
    for (int i = 0; i < parts.length; i++) {
        sum = sum.plus(parts[i]);
        out.add(new Refund(paid.get(i), parts[i]));
    }
    if (!sum.equals(total)) {
        throw new IllegalStateException("refund parts do not add up");
    }
    return out;
}"""


# 2.7 Special Case: presets null-checks, guest-customer; exercise (PLAN section D.4 and presets.py, verbatim).
NULL_CHECKS = """String greeting(Customer c) {
    String name = "friend";
    if (c != null && c.name() != null) {
        name = c.name();
    }
    String plan = "basic";
    if (c != null && c.plan() != null) {
        plan = c.plan().title();
    }
    return "Dear " + name + ", your plan: " + plan;
}"""

GUEST_CUSTOMER = """// The finder returns a GuestCustomer instead of null.
class GuestCustomer extends Customer {
    String name() { return "friend"; }
    Plan plan() { return Plan.BASIC; }
}

String greeting(Customer c) {
    return "Dear " + c.name() + ", your plan: " + c.plan().title();
}"""

NULL_ADDRESS = """String label(Order o) {
    Address a = o.address();
    String city = "unknown";
    if (a != null && a.city() != null) {
        city = a.city();
    }
    if (a == null || a.postcode() == null) {
        return city;
    }
    return city + " " + a.postcode();
}"""


_COMPLEXITY_INTRO = (
    "The lab counts decision points by a stated rule: one, plus one for each if, "
    "while, for and case, and for each conditional and and conditional or. The bands beside the count are McConnell's, from "
    "Code Complete; Fowler gives no count. The listings are the lesson's."
)


LESSONS = [
    # ---------------------------------------------------------------- 05
    # Chapter 18, Value Object (PDF pp. 429-430 of the operator's copy):
    # equality (p. 429), immutability and aliasing (p. 429), Embedded Value
    # (p. 429), the J2EE name collision (p. 430).
    # Quote: PDF p. 429 of the operator's copy, 17 words, ea_quotes.py OK.
    # Lesson total: 17 words.
    {
        "slug": "value-object",
        "title": "Value Object",
        "module": "Chapter 18 · Base Patterns",
        "one_line": "A small object, like a date range or an amount, that is equal to another when its values are equal, and that nobody can change once it is made.",
        "summary": (
            "Chapter 18's Value Object is a small object whose equality rests on its "
            "values, not its identity, and Fowler advises making it immutable so that "
            "two owners can share it safely. Count the public mutable fields in a date "
            "range, then in its value version, and read what the count cannot see."
        ),
        "key": [
            "equal when the values are equal",
            "a reference object: equal by identity",
            "make it immutable: no field changes",
            "the reason: aliasing bugs",
            "stored inside the row of its owner",
        ],
        "key_label": "Value Object in five lines",
        "concepts_intro": (
            "Three terms from the pattern, the last of them the bug it exists to "
            "prevent."
        ),
        "concepts": [
            ("Reference object",
             "An object whose equality is its identity: the same object in memory, or "
             "the same key in the database. Two customers with the same name are still "
             "two customers."),
            ("Value Object",
             "An object whose equality is based on the values of its fields, so two date "
             "ranges with the same start and end are the same range. It does not matter "
             "how many copies exist."),
            ("Aliasing bug",
             "What happens when two owners share one mutable object and one of them "
             "changes it: the other owner's value changes too, though nobody touched it. "
             "An immutable object cannot be changed, so it can be shared."),
        ],
        "read_title": "The pattern first, then two versions of a class",
        "read_intro": (
            "Read Value Object in Chapter 18 in your own copy first. It is two pages "
            "long. The lesson reads it as a tool and counts what two versions of one "
            "class expose."
        ),
        "body": [
            ("p", "&ldquo;it's a very good idea to make them immutable—that is, once "
                  "created none of their fields change.&rdquo; That is the advice at the "
                  "centre of Value Object, one of the base patterns of Chapter 18, and "
                  "the reason for it is the whole pattern. This lesson reads it as a tool. "
                  "Read it in your own copy first; it is short."),
            ("p", "Fowler distinguishes reference objects from Value Objects. A handy "
                  "definition, he says, is by size: values are small, like an amount of "
                  "money or a date, and references large, like an order or a customer. "
                  "But the real difference is equality. A reference object's equality is "
                  "its identity, either the language's own object identity or an ID such "
                  "as a primary key. A Value Object's equality is its field values: two "
                  "dates are equal when they name the same day of the same month and year. So values are "
                  "passed around freely, and you do not care how many objects for the "
                  "same date exist or whether two owners share one."),
            ("p", "That freedom is where the quotation comes in. Few languages treat "
                  "values specially, so Fowler advises making them immutable, "
                  "and the reason he gives is aliasing bugs. If two owners share one date "
                  "and one of them changes a field in it, the other's date changes too. "
                  "His point is less that this is wrong than that nobody expects it: "
                  "people expect to change a date by replacing the object with a new one. "
                  "An immutable value meets that expectation, and can then be shared "
                  "without anyone asking who else holds it."),
            ("p", "The rest of the pattern is brief. A Value Object should not be stored "
                  "as a record of its own: Embedded Value, read in the Objects and Tables "
                  "course, keeps its fields in the owner's row, which also lets SQL query "
                  "them, and Serialized LOB is the other option. .NET gives values "
                  "first-class treatment as structs, which the pattern names as a "
                  "platform note. When to Use It is a single test: use the pattern for a "
                  "thing whose equality rests on something other than identity, "
                  "and consider it for any small object that is easy to create. Fowler "
                  "ends on a name clash: some J2EE writing of the time used value object "
                  "for what the book calls a Data Transfer Object, read in the last "
                  "course, and later renamed it transfer object."),
            ("p", "Now the count. The lab reads one class and prints four tiles: its "
                  "fields, its public fields that are not final, its routines with "
                  "constructors included, and its public routines. On "
                  "<code>mutable-range</code>, the date range below, it counts 2 fields, "
                  "2 public and not final, 2 routines and 2 public. Both `start` and `end` "
                  "are open to every caller, and `setEnd` changes the range in place."),
            ("code", _lines(DATE_RANGE_MUTABLE)),
            ("p", "Here is the aliasing bug on this class. Two bookings are given the "
                  "same `DateRange` object, because they cover the same week. One booking "
                  "is extended, and its code calls `setEnd` on its range. The other "
                  "booking is now extended too, though nothing touched it, and the "
                  "condition in `includes`, `!d.isBefore(start) && !d.isAfter(end)`, "
                  "answers yes for days it never covered."),
            ("p", "On <code>value-range</code> the fields are private and final, set "
                  "once by the constructor, and `equals` and `hashCode` compare the two "
                  "dates: 2 fields, 0 public and not final, 3 routines, 2 public. The lab "
                  "pins only the public fields, because the routine count rose with "
                  "`equals`, which is not what makes the class a value. Two limits are "
                  "worth knowing. The kit counts `public` and not `final`, so a private "
                  "field with a public setter counts 0 though it can still change; and "
                  "it cannot see whether `equals` compares values, which you check by "
                  "reading line 13. The lesson adds two points of its own: the class is "
                  "`final`, so no subclass can add a field that changes, and the "
                  "`LocalDate`s it holds are immutable themselves."),
            ("code", _lines(DATE_RANGE_VALUE)),
            ("h3", "Exercise"),
            ("code", _lines(QUANTITY_MUTABLE)),
            ("p", "Count this `Quantity` by the lab's four tiles: fields, public fields "
                  "that are not final, routines with constructors included, and public "
                  "routines. Then write the fields, the constructor and the `add` method "
                  "of its value version, and say what `equals` should compare. Paste the "
                  "class into the lab to check the counts."),
            ("p", "The pattern points to its best-known example. The next lesson, Money, "
                  "reads it: an amount with its currency, and the penny that rounding "
                  "loses."),
        ],
        "lab": ("cckit", {
            "mode": "code",
            "view": "class",
            "preset": "mutable-range",
            "presets": [
                {"id": "mutable-range",
                 "label": "A date range with public fields and a setter",
                 "code": DATE_RANGE_MUTABLE,
                 "expect": {"coPublicFields": "2"}},
                {"id": "value-range",
                 "label": "The same range as a value: private, final, equal by its dates",
                 "code": DATE_RANGE_VALUE,
                 "expect": {"coPublicFields": "0"}},
            ],
            "panel_title": "The public mutable fields that make aliasing possible",
            "panel_intro": (
                "Paste a Java class. The lab counts its fields, its public fields that "
                "are not final, its routines with constructors included, and its public "
                "routines. Whether equals compares values is for you to read. The "
                "classes are the lesson's."
            ),
        }),
        "steps_title": "Checking a class for the two properties",
        "steps_intro": "Four steps, the last of them on a class of your own.",
        "steps": [
            ("Count what can change",
             "List the fields that are public and not final, and the methods that "
             "assign a field after the constructor has run."),
            ("Check the equality",
             "Read `equals` and `hashCode`. A value compares its fields; with neither "
             "method, Java compares identity."),
            ("Write the value version",
             "Make every field private and final, set them all in one constructor, turn "
             "each mutator into a method that returns a new object, and compare every "
             "field in `equals` and `hashCode`."),
            ("Do it on your own code",
             "Find one small class in a system you know that represents an amount, a "
             "range or a code. Count its setters and public mutable fields, write the "
             "figure down, and say whether two owners ever share one instance."),
        ],
        "worked": {
            "title": "A range anyone can change",
            "intro": [
                "Count <code>mutable-range</code> and name what makes aliasing possible.",
            ],
            "lines": [
                "fields: start and end, 2",
                "public and not final: both, 2",
                "routines: setEnd and includes, 2",
                "public routines: 2",
                "ways to change a shared range: 3",
            ],
            "after": [
                "The three ways are assigning `start`, assigning `end`, and calling "
                "`setEnd`. Any one of them, through any holder of the range, changes it "
                "for every holder. The value version closes all three, and the lab's "
                "public-field count, 0, sees two of them.",
            ],
        },
        "quiz_title": "Values, identity and what the lab sees",
        "quiz": [
            {"q": "Count the exercise's `Quantity` by the lab's rules (a public field that "
                  "is not final counts as public; constructors count as routines). What "
                  "are its four counts?",
             "a": ["2 fields, 2 public and not final, 3 routines, 2 public",
                   "3 fields, 3 public and not final, 3 routines, 2 public",
                   "3 fields, 2 public and not final, 3 routines, 2 public",
                   "3 fields, 2 public and not final, 3 routines, 3 public"],
             "c": 2,
             "why": "`amount`, `unit` and `max` are fields; `max` is private and final, so "
                    "2 are public and not final. `add`, `toString` and `room` are routines, "
                    "and `room` is package-private, so 2 are public. As a value object, "
                    "`amount` and `unit` become private and final, set by one constructor; "
                    "`add` returns a new `Quantity`; and `equals` and `hashCode` compare "
                    "both fields."},
            {"q": "Two `DateRange` objects are created separately, each from 1 to 7 March. "
                  "Which is true?",
             "a": ["As Value Objects they are equal; as reference objects they are not",
                   "As Value Objects they are not equal, since they are two objects",
                   "They are equal either way, since their fields match",
                   "Neither, until both are saved with the same key"],
             "c": 0,
             "why": "A Value Object's equality is its field values, so the two ranges are "
                    "equal. A reference object's equality is its identity, the object "
                    "itself or its key, and these are two objects."},
            {"q": "What reason does Fowler give for making Value Objects immutable?",
             "a": ["Immutable objects are faster to create",
                   "To avoid aliasing bugs, where one owner changes a value another "
                   "shares",
                   "So that they can be stored as records of their own",
                   "Because the J2EE specification requires it"],
             "c": 1,
             "why": "Aliasing bugs: two objects share one value, one changes it, and the "
                    "other's changes too. People expect to change a value by replacing it, "
                    "and immutability meets that."},
            {"q": "How does the pattern say a Value Object should usually be stored?",
             "a": ["As a complete record in a table of its own",
                   "As an Embedded Value, its fields in the owner's row",
                   "Only in memory, never in the database",
                   "As a Data Transfer Object"],
             "c": 1,
             "why": "Not as complete records: Embedded Value, or Serialized LOB, and "
                    "Embedded Value is usually best since SQL can still query the fields. "
                    "Data Transfer Object is the other meaning of value object in the "
                    "name clash."},
        ],
        "mistakes": [
            ("Thinking a Value Object is any object without an ID field",
             "Its defining property is equality by value, which Fowler sets against "
             "equality by identity. An entity with no key field is still an entity if "
             "two with the same fields are different things: two customers with the same "
             "name, two orders for the same goods. A missing ID says how something is "
             "stored, not how it is compared."),
            ("Thinking immutability is a performance trick",
             "Fowler's reason is aliasing bugs: one owner changes a value another owner "
             "shares. On the lesson's illustration, `setEnd` on a shared `DateRange` "
             "extends two bookings at once. Immutability makes sharing safe; any saving "
             "in copies follows from that."),
            ("Taking private fields for an immutable class",
             "Private fields stop callers assigning them directly, but a public setter "
             "still changes the object in place, and so does any method that assigns a "
             "field. The lab's public-field count would be 0 for such a class. What "
             "makes a value is fields set once, in the constructor, and methods that "
             "return new objects."),
        ],
        "standard": (
            "Finish when you can check a small class for value equality and for any way to change it.",
            "Given a class, count its public non-final fields and its mutators, and write "
            "the immutable version's fields and constructor."
        ),
        "note": (
            "The lab counts public fields that are not final; it cannot see a private "
            "field changed by a setter, and it cannot tell whether `equals` compares "
            "values or identity. Reading the class settles both, and only the domain "
            "settles whether a thing is a value at all."
        ),
    },
    # ---------------------------------------------------------------- 06
    # Chapter 18, Money (PDF pp. 431-437 of the operator's copy): the type
    # (p. 431), the conundrum and its solutions (p. 432), When to Use It
    # (p. 433), the example by Matt Foemmel and Martin Fowler (pp. 433-437).
    # Quote: PDF p. 432 of the operator's copy, 18 words, ea_quotes.py OK.
    # Lesson total: 18 words.
    # F9, PDF p. 432 of the operator's copy: 5 cents split 70% and 30%
    # (Foemmel's conundrum); presets nearest, round-down, rest-to-last and
    # allocator use it.
    {
        "slug": "money",
        "title": "Money",
        "module": "Chapter 18 · Base Patterns",
        "one_line": "An amount with its currency, held as whole cents, and a way of splitting a sum that neither loses nor gains a penny.",
        "summary": (
            "Chapter 18's Money is an amount and a currency in one Value Object, never "
            "a floating point number, with arithmetic that knows its currency. Its hard "
            "part is splitting a sum: work Matt Foemmel's five cents split 70 to 30 "
            "under four rounding rules, and see which lose a penny, which gain one, and "
            "where the pennies go."
        ),
        "key": [
            "an amount and its currency, together",
            "whole cents, never floating point",
            "adding two currencies is an error",
            "rounding each share can lose a penny",
            "allocate: floor, then hand out the rest",
        ],
        "key_label": "Money in five lines",
        "concepts_intro": (
            "Three ideas from the pattern, the last of them the one the lab works."
        ),
        "concepts": [
            ("Money",
             "A Value Object holding an amount and a currency. The amount is a whole "
             "number of the smallest unit, cents, or a fixed decimal, and adding or "
             "subtracting checks that the currencies match."),
            ("Allocation",
             "Splitting a sum of money between several places by given ratios, as "
             "opposed to multiplying it by a rate, such as a tax. The shares must add "
             "back to the sum exactly."),
            ("An allocator",
             "A method on Money that takes the ratios and returns the shares, with no "
             "penny dropped or added. The lab's allocator rounds every share down and "
             "then gives the cents left over one each to the shares in order, from the "
             "first."),
        ],
        "read_title": "The pattern first, then the conundrum worked",
        "read_intro": (
            "Read Money in Chapter 18 in your own copy first, including its example. "
            "The lesson reads the pattern as a tool and works its rounding problem "
            "under four rules."
        ),
        "body": [
            ("p", "&ldquo;There's no general rounding scheme I can apply to both that will "
                  "avoid losing or gaining a penny.&rdquo; That is the end of Matt "
                  "Foemmel's conundrum, as Fowler tells it in the Money pattern of Chapter "
                  "18, and this lesson works it. Read the pattern in your own copy first; "
                  "its example class is by Foemmel and Fowler, and is better read there."),
            ("p", "Fowler is puzzled that money is not a first-class type in any "
                  "mainstream language, because its absence causes two kinds of trouble. "
                  "The obvious one is currencies: adding dollars to yen. The subtle one is "
                  "rounding: amounts are usually rounded to the smallest unit, and it is "
                  "easy to lose pennies doing it. His answer is a Money class with an "
                  "amount and a currency. The amount is an integral type or a fixed "
                  "decimal, and he says to avoid any floating point type absolutely, "
                  "because it brings back the rounding problems Money exists to avoid. "
                  "The book's example shows the effect; the reason, in one sentence of "
                  "this lesson's own: binary floating "
                  "point cannot hold most decimal fractions exactly, so ten cents is "
                  "stored as a number very near ten cents, and the error shows in "
                  "totals."),
            ("p", "Money is a Value Object, so its equality and hash code rest on the "
                  "amount and the currency. Its arithmetic is currency-aware: adding two "
                  "currencies is, most simply, an error, and Ward Cunningham's money bag, "
                  "an object holding several currencies at once, is the more elaborate "
                  "answer. Multiplying by a rate is ordinary. Converting between "
                  "currencies goes through a convertor object, because some conversion "
                  "rules, like the fixed euro rates, round in their own way. Comparison is "
                  "currency-aware too, and Money can print and parse itself. When to Use "
                  "It is broad: Fowler reaches for Money in nearly every calculation an "
                  "object-oriented program does, chiefly to keep the rounding in one "
                  "place."),
            ("p", "Then the conundrum, which the book credits to Matt Foemmel. A rule "
                  "says a sum must be split 70% to one account and 30% to another, and "
                  "the sum is 5 cents. The exact shares are 3.5 and 1.5 cents. Rounding "
                  "both to nearest gives 4 and 2, a penny gained; rounding both down "
                  "gives 4 cents in all, a penny lost; rounding both up gives 6. Fowler "
                  "lists the ways out he has seen: ignore it, which worries "
                  "accountants; give the last share whatever is left, which keeps the total "
                  "but can pile pennies onto the last share; let the caller choose a "
                  "rounding for each share, which gets complicated across ten accounts; "
                  "and his favourite, an allocator that takes the ratios and returns "
                  "shares with no penny dropped. Its faults, he says, are that you must "
                  "remember to use it, and that it is hard to guarantee which share gets "
                  "each spare penny."),
            ("p", "The lab works the split exactly. It takes an amount in cents, the "
                  "ratios and a rule, computes each exact share as the amount times its "
                  "ratio over the sum of the ratios, and prints five tiles: the shares, "
                  "their total, the total less the amount, the exact shares, and the "
                  "largest gap between a share and its exact value. Its `allocator` "
                  "rounds every share down and gives the cents left over one each to the "
                  "shares in order from the first, which is what the Foemmel and Fowler "
                  "example does; the panel says the book allows other ways of placing "
                  "them. On Foemmel's 5 cents at 70 30, the book's illustration, "
                  "<code>nearest</code> prints 4, 2, a total of 6, +1, exact shares 7/2 = "
                  "3.50 and 3/2 = 1.50, and a largest gap of 1/2 = 0.50. "
                  "<code>round-down</code> prints 3, 1, a total of 4, −1."),
            ("p", "The two rules that keep the total agree here. <code>rest-to-last</code> "
                  "rounds the first share to nearest and gives the last what is left: 4, "
                  "1, a total of 5, 0. <code>allocator</code> floors both to 3 and 1, then "
                  "gives the one cent left to the first share: 4, 1, 5, 0. With two "
                  "shares there is nowhere else for a penny to go, so the difference "
                  "between the rules needs more shares to show."),
            ("p", "On <code>three-ways</code> a dollar is split equally three ways by "
                  "nearest: 33, 33, 33, a total of 99, −1, a cent lost. On "
                  "<code>three-ways-allocated</code> the allocator gives 34, 33, 33, a "
                  "total of 100, 0, with the largest gap 2/3 ≈ 0.67. On "
                  "<code>pennies-to-last</code> a dollar is split seven ways with the "
                  "last share taking what is left: 14 six times and then 16, a total of "
                  "100, 0, but a largest gap of 12/7 ≈ 1.71. The total is kept and the "
                  "last share takes two cents more than the others, which is the fault "
                  "the book names. The allocator keeps every share within a cent of its "
                  "exact value, because it rounds down and adds at most one."),
            ("p", "The listing is the caller's side: a refund shared across the payments "
                  "that made up an order, in proportion to each. It leaves the splitting "
                  "to `Money` and then checks that the parts add back up, throwing if they "
                  "do not. Under a rule that rounds each share to nearest, that check can "
                  "fail; under an allocator it cannot. There are no lab figures for this "
                  "listing: the lab works the rule, and the exercise asks you to work it "
                  "by hand."),
            ("code", _lines(REFUND_SPLIT)),
            ("h3", "Exercise"),
            ("ul", [
                "Amount: 100 cents.",
                "Ratios: six equal shares, 1 1 1 1 1 1.",
                "Rules: nearest, then the allocator.",
            ]),
            ("p", "Work each share, the total and the total less the amount under both "
                  "rules, and the exact share, by hand. Then set the lab to the same "
                  "amount, ratios and rule to check."),
            ("p", "A Money object stands in for a number. The next lesson, Special Case, "
                  "reads the object that stands in for a missing one."),
        ],
        "lab": ("eakit", {
            "mode": "money",
            "view": "allocate",
            "preset": "nearest",
            "presets": [
                {"id": "nearest",
                 "label": "5 cents at 70 30, each share to nearest (the book's illustration)",
                 "amount": "5", "ratios": "70 30", "rule": "nearest",
                 "expect": {"mnShares": "4, 2", "mnTotal": "6", "mnDiff": "+1"}},
                {"id": "round-down",
                 "label": "5 cents at 70 30, each share down (the book's illustration)",
                 "amount": "5", "ratios": "70 30", "rule": "down",
                 "expect": {"mnShares": "3, 1", "mnTotal": "4", "mnDiff": "−1"}},
                {"id": "rest-to-last",
                 "label": "5 cents at 70 30, the last share takes the rest (the book's illustration)",
                 "amount": "5", "ratios": "70 30", "rule": "last",
                 "expect": {"mnShares": "4, 1", "mnTotal": "5", "mnDiff": "0"}},
                {"id": "allocator",
                 "label": "5 cents at 70 30, by the allocator (the book's illustration)",
                 "amount": "5", "ratios": "70 30", "rule": "allocator",
                 "expect": {"mnShares": "4, 1", "mnTotal": "5", "mnDiff": "0"}},
                {"id": "three-ways",
                 "label": "A dollar in three equal shares, to nearest (illustrative)",
                 "amount": "100", "ratios": "1 1 1", "rule": "nearest",
                 "expect": {"mnShares": "33, 33, 33", "mnTotal": "99", "mnDiff": "−1"}},
                {"id": "three-ways-allocated",
                 "label": "A dollar in three equal shares, by the allocator (illustrative)",
                 "amount": "100", "ratios": "1 1 1", "rule": "allocator",
                 "expect": {"mnShares": "34, 33, 33", "mnTotal": "100", "mnDiff": "0"}},
                {"id": "pennies-to-last",
                 "label": "A dollar in seven shares, the last taking the rest (illustrative)",
                 "amount": "100", "ratios": "1 1 1 1 1 1 1", "rule": "last",
                 "expect": {"mnShares": "14, 14, 14, 14, 14, 14, 16", "mnTotal": "100",
                            "mnDiff": "0"}},
            ],
            "panel_title": "Splitting a sum by ratios",
            "panel_intro": (
                "Give an amount in cents, the ratios and a rule. Each exact share is "
                "the amount times its ratio over the sum of the ratios. The allocator "
                "rounds every share down, then gives the cents left over one each to "
                "the shares in order from the first; Fowler's Money allows other ways "
                "of placing them, and this is the one his and Foemmel's example uses."
            ),
            "source": (
                "the book's illustration in Chapter 18, Money (Matt Foemmel's five "
                "cents split 70 to 30) for the first four presets; the rest "
                "illustrative"
            ),
        }),
        "steps_title": "Splitting a sum without losing a penny",
        "steps_intro": "Four steps, the last of them on a system of your own.",
        "steps": [
            ("Work the exact shares",
             "Multiply the amount by each ratio and divide by the sum of the ratios. "
             "Keep the fractions."),
            ("Round by the rule",
             "Round each exact share by the rule in use: to nearest, down, up, or the "
             "last share taking what is left."),
            ("Total and compare",
             "Add the shares and subtract the amount. A non-zero difference is a penny "
             "gained or lost; a zero with one share far from its exact value is a "
             "penny moved."),
            ("Do it on your own system",
             "Find one place a system you know splits an amount, such as tax, a "
             "discount across order lines or instalments. Write which rule it uses and "
             "what happens to the remainder."),
        ],
        "worked": {
            "title": "Five cents, 70 to 30",
            "intro": [
                "Work <code>nearest</code>, the book's illustration.",
            ],
            "lines": [
                "exact: 5 × 70/100, which is 3.5 cents",
                "exact: 5 × 30/100, which is 1.5 cents",
                "to nearest, half up: 4 and 2",
                "total 6, a penny gained: +1",
                "each share half a cent from exact",
            ],
            "after": [
                "Rounding down instead gives 3 and 1, a penny lost. Both rules fail for "
                "the same reason: each share is rounded without knowing what the others "
                "did. The allocator rounds all of them down first and then hands out "
                "what was lost, so its shares, 4 and 1, add up to 5.",
            ],
        },
        "quiz_title": "Pennies, rules and the book's reasons",
        "quiz": [
            {"q": "Split 100 cents into six equal shares. What do nearest rounding and the "
                  "allocator (round every share down, then give the cents left over one "
                  "each from the first share) give?",
             "a": ["Nearest 17 each, total 102, +2; allocator 17, 17, 17, 17, 17, 15, "
                   "total 100",
                   "Nearest 17 each, total 102, +2; allocator 16, 16, 17, 17, 17, 17, "
                   "total 100",
                   "Nearest 16 each, total 96, −4; allocator 17, 17, 17, 17, 16, 16, "
                   "total 100",
                   "Nearest 17 each, total 102, +2; allocator 17, 17, 17, 17, 16, 16, "
                   "total 100"],
             "c": 3,
             "why": "Each exact share is 100/6 = 50/3 ≈ 16.67 cents. To nearest, every "
                    "share is 17, and six of them are 102, two cents gained. The allocator "
                    "floors each to 16, a total of 96, and gives the 4 cents left one each "
                    "to the first four shares: 17, 17, 17, 17, 16, 16, which is 100. "
                    "Sixteen each is rounding down, and 15 for the last is a rule that "
                    "puts the remainder on one share."},
            {"q": "In Foemmel's conundrum, 5 cents split 70% and 30%, what does rounding "
                  "both shares up give?",
             "a": ["5 cents, the right total", "4 cents, a penny lost",
                   "6 cents, a penny gained", "7 cents, two pennies gained"],
             "c": 2,
             "why": "The exact shares are 3.5 and 1.5, so rounding up gives 4 and 2, "
                    "which is 6. Rounding to nearest, half up, gives the same here; "
                    "rounding down gives 3 and 1, which is 4."},
            {"q": "Why does the pattern say to avoid floating point types for the amount?",
             "a": ["They are slower than integers",
                   "They cannot hold a currency",
                   "Databases cannot store them",
                   "They introduce the rounding problems Money is meant to avoid"],
             "c": 3,
             "why": "The book's reason is that floating point brings back the rounding "
                    "problems Money exists to solve. That binary floating point cannot "
                    "hold most decimal fractions exactly is the lesson's explanation of "
                    "why."},
            {"q": "Split 10 cents by the ratios 1 1 1 with the allocator (round every "
                  "share down, then give the cents left over one each from the first). "
                  "What are the shares?",
             "a": ["3, 3, 4", "4, 3, 3", "3, 3, 3", "4, 4, 2"],
             "c": 1,
             "why": "Each exact share is 10/3 ≈ 3.33, so each floors to 3, a total of 9. "
                    "The one cent left goes to the first share: 4, 3, 3. Giving it to "
                    "the last is the other rule, and 3, 3, 3 loses the cent."},
        ],
        "mistakes": [
            ("Thinking that rounding each share to the nearest cent keeps the total",
             "On the book's own example it gains a cent: 3.5 and 1.5 become 4 and 2, "
             "which is 6 from 5. On a three-way split of a dollar it loses one, 33 three "
             "times for 99. Each share is rounded without regard to the others, so the "
             "errors do not cancel; Fowler's point is that no rounding scheme applied to "
             "every share can promise they will."),
            ("Using a double and rounding at the end",
             "The book's reason against it is that floating point brings back the "
             "rounding problems Money exists to avoid; it says to avoid any floating "
             "point type absolutely. The lesson adds, as its own explanation, that binary "
             "floating point cannot hold most decimal fractions exactly, so a sum of "
             "amounts drifts before any rounding is applied. Whole cents, or a fixed "
             "decimal, have no such drift."),
            ("Thinking the last share taking the rest solves the problem",
             "It keeps the total, and on two shares it looks as good as an allocator. "
             "Fowler names its fault: pennies can pile up on the last allocation. On "
             "<code>pennies-to-last</code>, a dollar split seven ways, the last share is "
             "16 against 14 for the rest, nearly two cents from its exact value."),
        ],
        "standard": (
            "Finish when you can split an amount by ratios and say what each rule does to the total.",
            "Given an amount in cents and ratios, compute each share exactly, then under "
            "nearest, down and allocator rounding, and state each rule's total."
        ),
        "note": (
            "The lab does the arithmetic of the amounts and ratios it is given, exactly, "
            "and its allocator is one rule among those the book allows. Which rule is "
            "right, and which share should take a spare cent, is a business decision the "
            "lab cannot make; Fowler says the allocator cannot easily guarantee where "
            "the spare pennies land."
        ),
    },
    # ---------------------------------------------------------------- 07
    # Chapter 18, Special Case (PDF pp. 438-440 of the operator's copy): nulls and
    # duplication (p. 438), How It Works and flyweight (pp. 438-439), missing and
    # unknown (p. 439), IEEE 754 (p. 439), When to Use It (p. 439), Woolf's Null
    # Object and the pun (p. 439), the explicit test (p. 440).
    # Quote: PDF p. 438 of the operator's copy, 22 words, ea_quotes.py OK.
    # Lesson total: 22 words.
    {
        "slug": "special-case",
        "title": "Special Case",
        "module": "Chapter 18 · Base Patterns",
        "one_line": "Instead of returning null and making every caller check, return an object with the expected interface and harmless behaviour.",
        "summary": (
            "Chapter 18's Special Case replaces a null, or an odd value, with a "
            "subclass that answers the caller's questions sensibly, so the null checks "
            "that every caller would repeat are written once. Count the decision points "
            "a greeting spends on a missing customer, then give it a guest."
        ),
        "key": [
            "nulls defeat polymorphism",
            "the same check, repeated in every caller",
            "return a subclass with harmless answers",
            "missing and unknown: two special cases",
            "the caller asks; nothing branches",
        ],
        "key_label": "Special Case in five lines",
        "concepts_intro": (
            "Three terms from the pattern and the patterns it names."
        ),
        "concepts": [
            ("Special Case",
             "A subclass that stands in for one particular situation, such as "
             "a customer who is missing, returned in place of null so that callers can "
             "call the usual methods on it."),
            ("Null Object",
             "The special case of Special Case for null, written up as a pattern by "
             "Bobby Woolf, whom the book cites. Its methods do nothing harmful and "
             "return harmless values."),
            ("Flyweight",
             "A single shared instance used wherever one is needed, after the Design "
             "Patterns book of Gamma and his co-authors. A special case with no state of "
             "its own can be one."),
        ],
        "read_title": "The pattern first, then one caller counted",
        "read_intro": (
            "Read Special Case in Chapter 18 in your own copy first; it is three pages "
            "long. The lesson reads it as a tool and counts what a caller spends on "
            "nulls."
        ),
        "body": [
            ("p", "&ldquo;Instead of returning null, or some odd value, return a Special "
                  "Case that has the same interface as what the caller expects.&rdquo; "
                  "That is the pattern in one sentence, from Chapter 18's Special Case, "
                  "which this lesson reads as a tool. Read it in your own copy first."),
            ("p", "Fowler's starting point is that nulls defeat polymorphism. You can "
                  "normally call a method on a variable without caring which subclass it "
                  "holds, and a typed language checks the call for you, but if the "
                  "variable can be null the call fails at run time, and, as he notes, "
                  "you get a stack trace for your trouble. So every caller that might see a null must "
                  "test for it, and since the right response is often the same in many "
                  "places, the same test is written in many places, which is duplication, "
                  "and Fowler counts it a sin. Nulls are the common case; infinity in arithmetic and a "
                  "customer only partly known are others."),
            ("p", "How It Works is short. Make a subclass for the special case, override "
                  "all the methods to give harmless behaviour, and put an instance of it "
                  "wherever a null would have been. There is usually no reason to tell one "
                  "instance from another, so a special case can often be a flyweight, one "
                  "shared instance, though not when it gathers state of its own. A null "
                  "can also mean different things, such as no customer at all or a "
                  "customer nobody has identified, and Fowler suggests separate special "
                  "cases for each. A special case's methods often return other special "
                  "cases, so what an unknown customer owes is itself unknown."),
            ("p", "He finds a good example outside business code: IEEE 754 floating "
                  "point, whose infinities and not-a-number are special values a "
                  "division by zero can return instead of raising an exception, and "
                  "which then take part in arithmetic like any other number. When to Use "
                  "It is a single test: use a Special Case wherever several places in the "
                  "system respond alike once a test has found one particular instance, "
                  "or found a null. The book cites Bobby Woolf's Null "
                  "Object and, pardoning what Fowler calls the pun, files Null Object "
                  "as a special case of Special Case. A caller that does need to know can "
                  "still ask: the example gives the class an `isNull` method, or a marker "
                  "interface to test for."),
            ("p", "Now the count. The greeting below must cope with a missing customer "
                  "and with a customer whose name or plan is missing, and it guards every "
                  "call. On <code>null-checks</code> the lab counts 5 decision points, 1 "
                  "+ if 2 + && 2, band 0–5, deepest nesting 1, first at line 4. Each `&&` "
                  "is there only so that the call after it does not land on a null."),
            ("code", _lines(NULL_CHECKS)),
            ("p", "On <code>guest-customer</code> the finder returns a `GuestCustomer` "
                  "instead of null, whose name is &ldquo;friend&rdquo; and whose plan is "
                  "the basic one, and the greeting asks its questions directly: 1 "
                  "decision point, breakdown 1, band 0–5, deepest nesting 0, first at "
                  "line 3. The lab finds a routine header here, `greeting` on line 7, so "
                  "it measures depth from inside a routine, as it did on the Domain "
                  "Model lesson's first preset, and the class's one-line methods above "
                  "it read as 0. The listing is a class and a routine, and the lab counts the "
                  "whole listing; neither holds a test. Unlike the Domain Model lesson, "
                  "where each branch moved into the class it concerned, here the guarded "
                  "answers all move into one class and the decision moves to one place, "
                  "the finder that returns the guest. It leaves every caller, because "
                  "the answer was the same wherever the question was asked."),
            ("code", _lines(GUEST_CUSTOMER)),
            ("p", "The rewrite assumes something the original did not: that a real "
                  "customer always has a name and a plan. `NULL_CHECKS` also guarded "
                  "against a known customer with no name, and `GuestCustomer` does not "
                  "cover that case. A customer with a missing name is a different "
                  "special case from a missing customer, which is Fowler's point about "
                  "a null meaning different things; the count fell to 1 on the "
                  "lesson's illustration because the lesson decided those cases away, "
                  "and your code may not be able to."),
            ("h3", "Exercise"),
            ("code", _lines(NULL_ADDRESS)),
            ("p", "Count this routine's decision points by the lab's rule, with the "
                  "breakdown. Then write a special case for the missing address, with "
                  "the city and postcode it should report, and the routine as it would "
                  "read once the finder returns it. Paste the listing into the lab to "
                  "check the count."),
            ("p", "This course has built the domain layer: its organisation, its service "
                  "boundary and its small objects. The next course, Talking to the "
                  "Database, connects it to the tables, and its choice of data-source "
                  "pattern turns on the domain pattern chosen here."),
        ],
        "lab": ("cckit", {
            "mode": "code",
            "view": "complexity",
            "bands": [5, 10],
            "book": "other",
            "preset": "null-checks",
            "presets": [
                {"id": "null-checks",
                 "label": "A greeting that checks for a missing customer twice",
                 "code": NULL_CHECKS,
                 "expect": {"coDecisions": "5", "coBreakdown": "1 + if 2 + && 2"}},
                {"id": "guest-customer",
                 "label": "The same greeting, given a GuestCustomer",
                 "code": GUEST_CUSTOMER,
                 "expect": {"coDecisions": "1", "coBreakdown": "1"}},
            ],
            "panel_title": "The null checks a Special Case removes",
            "panel_intro": _COMPLEXITY_INTRO,
        }),
        "steps_title": "Replacing null checks with a Special Case",
        "steps_intro": "Four steps, the last of them on code of your own.",
        "steps": [
            ("Count the guards",
             "Count the routine's decision points, and mark each `if`, `&&` and `||` "
             "that exists only to keep a call off a null."),
            ("Name what null means",
             "Write what each null stands for: nothing there at all, or something there "
             "that nobody knows. Each meaning is its own special case."),
            ("Write the subclass",
             "Subclass the expected type and override each method the callers use "
             "with the answer the guarded code gave, then have the finder return it "
             "instead of null."),
            ("Do it on your own code",
             "Find one method in a system you know that returns null. Count the null "
             "checks its callers make, write the figure down, and say whether they all "
             "do the same thing afterwards."),
        ],
        "worked": {
            "title": "A greeting with five decisions",
            "intro": [
                "Count <code>null-checks</code>, then <code>guest-customer</code>.",
            ],
            "lines": [
                "start at 1",
                "line 3: if, and && on the name: 3",
                "line 7: if, and && on the plan: 5",
                "with a GuestCustomer: no tests, 1",
            ],
            "after": [
                "Four of the five decisions guard calls against null. The finder now "
                "makes that decision once, by returning a guest, and every caller that "
                "greets a customer is spared it.",
            ],
        },
        "quiz_title": "Nulls, guards and the book's test",
        "quiz": [
            {"q": "Count the exercise's decision points (one, plus one for each `if`, "
                  "`while`, `for`, `case`, `&&` and `||`). What does the routine become "
                  "with a special case for the missing address?",
             "a": ["3; one line, with an `UnknownAddress` whose `city()` is "
                   "&ldquo;unknown&rdquo; and whose `postcode()` is empty",
                   "4; one line, with an `UnknownAddress` whose `city()` is "
                   "&ldquo;unknown&rdquo; and whose `postcode()` is empty",
                   "6; one line, with an `UnknownAddress` whose `city()` is "
                   "&ldquo;unknown&rdquo; and whose `postcode()` is empty",
                   "5; one line, with an `UnknownAddress` whose `city()` is "
                   "&ldquo;unknown&rdquo; and whose `postcode()` is empty"],
             "c": 3,
             "why": "1 + if 2 + && 1 + || 1 = 5: the two `if`s, the `&&` on line 4 and "
                    "the `||` on line 7. Four forgets the `||`; three counts only the "
                    "`if`s. With an `UnknownAddress` returned instead of null, whose "
                    "`city()` is &ldquo;unknown&rdquo; and whose `postcode()` is empty, "
                    "the routine is one line returning the city, a space and the "
                    "postcode. Check the edge: that line ends in a space when the postcode "
                    "is empty, where the original returned the city alone."},
            {"q": "What is the pattern's When to Use It test?",
             "a": ["Whenever a method can return null",
                   "Wherever several places do the same thing after a check for a "
                   "particular instance or for null",
                   "Only for errors that should not stop the program",
                   "Whenever a class has a subclass already"],
             "c": 1,
             "why": "The test is repetition: multiple places with the same behaviour "
                    "after the same conditional or null check. A null that each caller "
                    "handles differently is not that case."},
            {"q": "What example of Special Case does the book find in IEEE 754 floating "
                  "point?",
             "a": ["Rounding to the nearest even digit",
                   "Infinity and not-a-number, returned where an exception might "
                   "have been raised, which then take part in arithmetic",
                   "Signed zero, which compares equal to zero",
                   "The exponent field, which marks a special number"],
             "c": 1,
             "why": "Positive and negative infinity and NaN: a division by zero returns "
                    "a special value instead of an exception, and the value goes on "
                    "taking part in arithmetic like any other number."},
            {"q": "On <code>guest-customer</code>, how many decision points does the lab "
                  "count, by the same rule?",
             "a": ["0", "1", "3", "5"],
             "c": 1,
             "why": "The count starts at one, and neither the `GuestCustomer` class nor "
                    "the greeting holds an `if`, `&&` or `||`, so it stays 1. Five is the "
                    "greeting with its null checks; no listing counts 0 by this rule."},
        ],
        "mistakes": [
            ("Thinking a Special Case hides errors",
             "It is for a case that has the same behaviour wherever it turns up (When to "
             "Use It), and it hides nothing a caller needs: the book's own example can "
             "still be tested for explicitly, with an `isNull` method or a marker "
             "interface. Even a failure can be a special case, as the book's IEEE "
             "example shows: a division by zero returns a special value instead of "
             "throwing. What should still fail loudly is a null that means a bug, and "
             "that is not this pattern's case."),
            ("Thinking every caller still has to know about the Special Case",
             "The finder returns it; callers call the same methods they call on a real "
             "customer. On the lesson's illustration the greeting has no test at all "
             "and never names `GuestCustomer`. Only the code that decides there is no "
             "customer knows the special case exists."),
            ("Using one null object for every meaning of null",
             "A null can mean no customer at all, or a customer nobody has identified, "
             "and these may need different answers. The book's own case is a utility "
             "customer nobody has identified, whose charges must still be kept apart. "
             "Fowler suggests separate "
             "special cases for missing and unknown, and keeps those with state of "
             "their own apart rather than sharing one instance."),
        ],
        "standard": (
            "Finish when you can count the null checks a Special Case removes.",
            "Given a caller with null checks, count its decision points with the "
            "breakdown, and write the Special Case class that removes them."
        ),
        "note": (
            "The lab counts the decisions left in the listing; it cannot tell a check "
            "that guards against a missing object from one that tests a real rule, and "
            "it cannot say whether every null in a system means the same thing. The "
            "bands are McConnell's guidance for routines, not Fowler's, who gives no "
            "count."
        ),
    },
]
