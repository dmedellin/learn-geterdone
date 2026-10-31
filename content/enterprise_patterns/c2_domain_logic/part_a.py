"""Organizing Domain Logic, lessons 1-4 -- Chapters 2 and 9.

Fowler et al., Patterns of Enterprise Application Architecture (Addison-Wesley,
2002): Chapter 2, Organizing Domain Logic; Chapter 9, Domain Logic Patterns
(Transaction Script, Domain Model, Table Module, and Randy Stafford's Service
Layer); with Chapter 18's Record Set and Chapter 8's Starting with the Domain
Layer. Pages in the comments are PDF pages of the operator's copy, which has
no printed page numbers; the lessons cite by chapter, section and pattern.
Every quotation is copied from that copy and checked with ea_quotes.py. The
code is written for these lessons: none of the book's listings or example
domains is reproduced. Each snippet is one constant below, used both by the
lesson's code block and by the lab preset that counts it, so the line numbers
the prose names are the lab's. The design is docs/enterprise-patterns/PLAN.md,
section C, Course 2.
"""


def _lines(text):
    """A snippet constant as a code block's list of lines."""
    return text.split("\n")


# ---------------------------------------------------------------- snippets

# 2.1 Transaction Script: presets two-scripts, shared-subroutine; exercise (PLAN section D.4 and presets.py, verbatim).
TWO_SCRIPTS = """// Script for "place order".
void placeOrder(Order o) {
    long total = o.subtotal();
    if (o.customer().isMember()) {
        total = total - total / 10;
    }
    db.insertOrder(o.id(), total);
}

// Script for "quote price": the same discount, copied.
long quotePrice(Order o) {
    long total = o.subtotal();
    if (o.customer().isMember()) {
        total = total - total / 10;
    }
    return total;
}"""

SHARED_SUBROUTINE = """// The discount, once, as a subroutine both scripts call.
long memberPrice(Order o) {
    long total = o.subtotal();
    if (o.customer().isMember()) {
        total = total - total / 10;
    }
    return total;
}

void placeOrder(Order o) {
    db.insertOrder(o.id(), memberPrice(o));
}

long quotePrice(Order o) {
    return memberPrice(o);
}"""

SHIPPING_TWICE = """// Script for "check out".
void checkOut(Cart cart) {
    long cents = cart.totalCents();
    long shipping = 499;
    if (cents >= 5000) {
        shipping = 0;
    }
    db.insertOrder(cart.id(), cents + shipping);
}

// Script for "show basket".
void showBasket(Cart cart, Page page) {
    long cents = cart.totalCents();
    long shipping = 499;
    if (cents >= 5000) {
        shipping = 0;
    }
    page.write(cents, shipping);
}"""


# 2.2 Domain Model: presets price-by-kind, price-delegated; exercise (PLAN section D.4 and presets.py, verbatim).
PRICE_BY_KIND = """// One routine prices every kind of product.
long price(Product p, int qty) {
    long cents = p.unitCents() * qty;
    if (p.kind() == Kind.BOOK) {
        cents = cents - cents / 20;
    } else if (p.kind() == Kind.ALCOHOL) {
        cents = cents + cents / 5;
    } else if (p.kind() == Kind.FOOD && qty > 10) {
        cents = cents - cents / 10;
    }
    return cents;
}"""

PRICE_DELEGATED = """// Each kind of product carries its own rule; Product is the default.
class Product {
    long unitCents;
    long adjust(long cents, int qty) { return cents; }
    long price(int qty) { return adjust(unitCents * qty, qty); }
}
class Book extends Product {
    long adjust(long cents, int qty) { return cents - cents / 20; }
}
class Alcohol extends Product {
    long adjust(long cents, int qty) { return cents + cents / 5; }
}
class Food extends Product {
    long adjust(long cents, int qty) {
        if (qty > 10) { return cents - cents / 10; }
        return cents;
    }
}"""

SHIPPING_BY_METHOD = """// Shipping cost in cents, by method and weight.
long shippingCents(Parcel p) {
    if (p.method() == Method.POST) {
        return 300 + 50 * p.kilos();
    } else if (p.method() == Method.COURIER && p.kilos() > 20) {
        return 2500;
    } else if (p.method() == Method.COURIER) {
        return 1200;
    } else if (p.method() == Method.COLLECT || p.isStaff()) {
        return 0;
    }
    return 999;
}"""


# 2.3 Table Module: body only (PLAN section D.4 and presets.py, verbatim).
TABLE_MODULE = """// One object for the whole invoice-line table, not one per row.
class InvoiceLines {
    private final RecordSet rows;

    InvoiceLines(RecordSet rows) {
        this.rows = rows;
    }

    long totalCents(long invoiceId) {
        long total = 0;
        for (Record r : rows.where("invoice_id", invoiceId)) {
            total = total + r.getLong("cents");
        }
        return total;
    }
}"""


# 2.4 Service Layer: presets orders-twice, orders-served; exercise (PLAN section D.4 and presets.py, verbatim).
ORDERS_TWICE = """// The web page and the nightly import both place orders.
void webPlace(Request req) {
    Order order = orders.fromForm(req);
    db.begin();
    inventory.reserve(order);
    order.confirm();
    db.commit();
    mailer.sendConfirmation(order);
}

void importPlace(Row row) {
    Order order = orders.fromRow(row);
    db.begin();
    inventory.reserve(order);
    order.confirm();
    db.commit();
    mailer.sendConfirmation(order);
}"""

ORDERS_SERVED = """// Each client builds its order, then asks the service to place it.
void webPlace(Request req) {
    service.placeOrder(orders.fromForm(req));
}

void importPlace(Row row) {
    service.placeOrder(orders.fromRow(row));
}

// In OrderService: the application logic, in one place.
void placeOrder(Order order) {
    db.begin();
    inventory.reserve(order);
    order.confirm();
    db.commit();
    mailer.sendConfirmation(order);
}"""

CANCEL_TWICE = """void webCancel(Request req) {
    Order order = orders.find(req.param("id"));
    db.begin();
    inventory.release(order);
    order.cancel();
    db.commit();
    mailer.sendCancellation(order);
}

void phoneCancel(ApiCall call) {
    audit.record(call);
    Order order = orders.find(call.field("order"));
    db.begin();
    inventory.release(order);
    order.cancel();
    db.commit();
    mailer.sendCancellation(order);
}"""


_DUPES_INTRO = (
    "The lab compares statement lines as text, with white space collapsed and "
    "comments left out, and reports every run of two or more lines that occurs "
    "again. A closing brace alone is not a statement line. It matches text, so a "
    "copy with renamed variables is one it cannot see. The listings are the "
    "lesson's."
)

_COMPLEXITY_INTRO = (
    "The lab counts decision points by a stated rule: one, plus one for each if, "
    "while, for and case, and for each conditional and and conditional or. The bands beside the count are McConnell's, from "
    "Code Complete; Fowler gives no count. The listings are the lesson's."
)


LESSONS = [
    # ---------------------------------------------------------------- 01
    # Chapter 2, opening (PDF pp. 39-41 of the operator's copy); Chapter 9,
    # Transaction Script (pp. 112-117); Making a Choice (pp. 42-43); Chapter 8,
    # Down to the Data Source Layer (p. 102).
    # Quote: PDF p. 113 of the operator's copy, 35 words, ea_quotes.py OK.
    # Lesson total: 35 words.
    {
        "slug": "transaction-script",
        "title": "Transaction Script",
        "module": "Chapter 9 · Domain Logic Patterns",
        "one_line": "One procedure for each thing a user asks the system to do: simple, natural for little logic, and prone to copying its rules as the logic grows.",
        "summary": (
            "Chapter 2 introduces three ways to organise domain logic, and Chapter 9 "
            "sets out the simplest: a Transaction Script, one procedure for each "
            "action a user takes. Read Fowler's case for its simplicity and his "
            "warning about duplication, then count the lines two scripts share and "
            "watch a subroutine remove them."
        ),
        "key": [
            "a procedure for each user action",
            "simple, and natural for little logic",
            "its failing: rules copied across scripts",
            "first remedy: a shared subroutine",
            "the database behind a gateway",
        ],
        "key_label": "Transaction Script in five lines",
        "concepts_intro": (
            "Three terms carry the lesson. The first is Chapter 2's, the second "
            "Chapter 9's, the third the lab's."
        ),
        "concepts": [
            ("Domain logic",
             "The part of an application that does the work the business needs: the "
             "validations, calculations and rules, as distinct from showing things to "
             "the user and from storing them. Fowler also calls it business logic."),
            ("Transaction Script",
             "A procedure that takes a request from the presentation, does its "
             "checks and calculations, reads and writes the database, and replies. "
             "There is one for each action, and usually one for each database "
             "transaction, which is where the name comes from."),
            ("A repeated block",
             "A run of statement lines that appears twice, word for word. The lab "
             "finds runs of at least two. It is the duplication Fowler names as the "
             "pattern's failing, in the one form a text match can see."),
        ],
        "read_title": "The chapter's argument first, then the pattern, then the count",
        "read_intro": (
            "Read the opening of Chapter 2 and the Transaction Script pattern in "
            "Chapter 9 in your own copy first. The lesson reads the narrative as an "
            "argument and the pattern as a tool, and then counts what two scripts "
            "share."
        ),
        "body": [
            ("p", "&ldquo;The glory of Transaction Script is its simplicity. Organizing "
                  "logic this way is natural for applications with only a small amount of "
                  "logic, and it involves very little overhead either in performance or in "
                  "understanding.&rdquo; That is the first paragraph of the pattern's When "
                  "to Use It, in Chapter 9. This lesson reads the opening of Chapter 2, "
                  "Organizing Domain Logic, where Fowler sets out three ways to organise "
                  "the middle layer, and then Transaction Script itself. Read both in your "
                  "own copy first."),
            ("p", "Chapter 2 is an argument, and it starts with the simplest of the three. "
                  "A Transaction Script, Fowler says, is essentially a procedure: it takes "
                  "the input from the presentation, validates it, calculates, stores data, "
                  "calls any other systems it needs, and replies. Its organising principle "
                  "is one procedure for each action a user might want to do, so a shop "
                  "would have one script for checking out and another for showing what is "
                  "in the basket. Pieces can be split into subroutines, and scripts can "
                  "share them, but the shape is still a procedure per action."),
            ("p", "He gives it three advantages: most developers already know the "
                  "procedural style; it sits easily on a simple data source layer, a "
                  "Row Data Gateway or a Table Data Gateway; and the transaction boundary "
                  "is obvious, opened at the start of the script and closed at its end. "
                  "Its disadvantages appear as the domain logic grows. Several "
                  "transactions do much the same work, so code is duplicated; some of "
                  "that can be factored into common subroutines, but much of it, he says, "
                  "is hard to remove and harder still to notice, and the application can "
                  "end up a tangle of routines with no clear structure."),
            ("p", "Chapter 9 gives the pattern as a tool. A Transaction Script organises "
                  "the logic of a request as a single procedure, calling the database "
                  "directly or through a thin wrapper. Fowler's preference is to keep "
                  "scripts apart from the rest: in their own subroutines at least, better "
                  "in classes separate from presentation and data source, and never "
                  "calling presentation logic, so that they are easy to change and to "
                  "test. He describes two ways of putting scripts into classes. The common "
                  "one, which suits most designs, is several related scripts to a "
                  "class. The other is a class for each script, after the Command pattern, "
                  "with a supertype that declares an execute method; he has rarely seen "
                  "the need."),
            ("p", "When to Use It continues past the quotation. As the logic gets more "
                  "complicated it gets harder to keep the scripts well designed, and the "
                  "particular problem to watch is duplication between transactions: the "
                  "whole point of a script is to handle one transaction, so code that two "
                  "of them need tends to be written twice. Careful factoring helps, but "
                  "more complex domains need a Domain Model. The cutover is hard to "
                  "quantify, and Fowler ends with a caution against his own enthusiasm: "
                  "however devoted to objects you become, the world is full of simple "
                  "problems, and a simple solution gets you running faster."),
            ("p", "Now the code. The listing below holds two scripts, one that places an "
                  "order and one that quotes its price, and each works out the member "
                  "discount for itself. The lab looks for runs of at least two statement "
                  "lines that occur twice. On the preset <code>two-scripts</code> it finds "
                  "one repeated block, 6 lines in all the copies, at lines 3–5 and lines "
                  "12–14: the subtotal, the test for a member and the discount, three "
                  "lines in two copies."),
            ("code", _lines(TWO_SCRIPTS)),
            ("p", "The count is a reason to look, and what it points at is a rule held "
                  "in two places. If the member discount changes, both copies must change, "
                  "and nothing in either script says the other exists. Notice too what the "
                  "scripts do not hold: no SQL. Placing the order calls `db.insertOrder`, "
                  "a gateway's method, which is how Fowler writes even the simplest "
                  "scripts."),
            ("p", "The preset <code>shared-subroutine</code> applies Fowler's first "
                  "remedy. The discount is written once, as `memberPrice`, and both "
                  "scripts call it: 0 repeated blocks, 0 lines, and the lab's where tile "
                  "says none. Each script is now one line, and the rule has one home. The "
                  "lab's limit is the chapter's warning in another form. It matches text, "
                  "so if the second copy had named its variable `price` instead of "
                  "`total`, the two blocks would share only the line that tests for a "
                  "member, and the lab would report nothing, though the rule would still "
                  "be written twice. That is the duplication Fowler calls harder to notice."),
            ("code", _lines(SHARED_SUBROUTINE)),
            ("h3", "Exercise"),
            ("code", _lines(SHIPPING_TWICE)),
            ("p", "Two more scripts, one that checks out a cart and one that shows the "
                  "basket. By the lab's rule, runs of two or more identical statement "
                  "lines with a lone closing brace not counted, mark the lines the two "
                  "scripts repeat, give their numbers and the lines in all the copies, "
                  "and write the subroutine both would call: its signature and its body. "
                  "Then paste the listing into the lab to check your count."),
            ("p", "A Transaction Script holds a rule where the action is. The next "
                  "lesson, Domain Model, reads the other end of Chapter 2's range: each "
                  "rule held by the object it concerns."),
        ],
        "lab": ("cckit", {
            "mode": "code",
            "view": "dupes",
            "min_run": 2,
            "preset": "two-scripts",
            "presets": [
                {"id": "two-scripts",
                 "label": "Two scripts, each working out the member discount",
                 "code": TWO_SCRIPTS,
                 "expect": {"coDupBlocks": "1", "coDupLines": "6",
                            "coDupWhere": "lines 3–5 and lines 12–14"}},
                {"id": "shared-subroutine",
                 "label": "The discount once, as a subroutine both scripts call",
                 "code": SHARED_SUBROUTINE,
                 "expect": {"coDupBlocks": "0", "coDupLines": "0", "coDupWhere": "none"}},
            ],
            "panel_title": "The lines two Transaction Scripts repeat",
            "panel_intro": _DUPES_INTRO,
        }),
        "steps_title": "Finding what two scripts share",
        "steps_intro": "Four steps, the last of them on code of your own.",
        "steps": [
            ("Put the scripts side by side",
             "Number every line of both scripts, blank and comment lines included, as "
             "the lab does."),
            ("Mark the identical runs",
             "Find each run of two or more statement lines that appears in both, word "
             "for word. A closing brace on its own is not a statement line."),
            ("Write the subroutine",
             "Give the repeated run a name that says what it computes, the inputs it "
             "reads as parameters and its result as the return value, and replace each "
             "copy with a call."),
            ("Do it on your own code",
             "Find two handlers in a system you know that compute the same thing, such "
             "as a total or a discount. Count the lines they share, write the figure "
             "down, and say in one sentence where the shared rule should live."),
        ],
        "worked": {
            "title": "Two scripts, one discount",
            "intro": [
                "Find the repeated block in <code>two-scripts</code>.",
            ],
            "lines": [
                "line 3 and line 12: the subtotal",
                "line 4 and line 13: the test for a member",
                "line 5 and line 14: the discount itself",
                "lines 6 and 15: a lone brace, not counted",
                "lines 7 and 16 differ: insert, or return",
                "one block, three lines in two copies: 6",
            ],
            "after": [
                "The run starts where the scripts start to agree and stops at the first "
                "statement where they differ. Writing it once as `memberPrice` is the "
                "subroutine Fowler recommends; whether every repetition can be removed "
                "that way is the question his chapter leaves open.",
            ],
        },
        "quiz_title": "Scripts, duplication and Fowler's claims",
        "quiz": [
            {"q": "In the exercise, which lines do the two scripts repeat by the lab's rule "
                  "(runs of two or more identical statement lines, a lone closing brace "
                  "not counted), and how many lines are in all the copies?",
             "a": ["lines 3–6 and lines 13–16, 8 lines",
                   "lines 3–7 and lines 13–17, 10 lines",
                   "lines 2–6 and lines 12–16, 10 lines",
                   "lines 3–5 and lines 13–15, 6 lines"],
             "c": 0,
             "why": "Lines 3 to 6 (the total, the shipping of 499, the test against 5000 "
                    "and the free shipping) match lines 13 to 16 word for word: one block, "
                    "four lines in two copies, 8. Lines 7 and 17 are lone braces, which are "
                    "not statement lines, and lines 2 and 12 are the two different "
                    "headers. Line 6 is in the run: `shipping = 0;` is identical in both. "
                    "A subroutine `long shippingFor(long cents)` holding lines 4 to 6 and "
                    "returning the shipping is what both scripts would call. Each script "
                    "keeps line 3, since both still need `cents`: one adds it to the "
                    "order, the other writes it to the page. The lab then finds no "
                    "repeated run, because one identical line is shorter than the "
                    "minimum."},
            {"q": "According to Chapter 9's When to Use It, what is the particular problem "
                  "to watch for as a Transaction Script design grows?",
             "a": ["Transactions that run too long and hold their locks",
                   "Duplication of logic between transactions",
                   "Scripts that call the presentation",
                   "Too many classes, one for each script"],
             "c": 1,
             "why": "Because each script handles one transaction, code that two of them "
                    "need tends to be written twice. Calls into the presentation are "
                    "something How It Works advises against, and a class for each script "
                    "is an option Fowler describes, not the problem he warns of."},
            {"q": "In Chapter 8, Down to the Data Source Layer, what does Fowler say about "
                  "a Transaction Script that holds its own SQL?",
             "a": ["It is the normal form of the pattern",
                   "He keeps the database apart even in the plainest scripts, with a gateway",
                   "It is acceptable only with a Domain Model beside it",
                   "It is required, since the script is the transaction"],
             "c": 1,
             "why": "The simplest scripts contain their own database logic, he says, but "
                    "he keeps the database apart even in the plainest scripts, with a "
                    "Row Data Gateway or a Table Data Gateway. The lesson's scripts "
                    "call `db.insertOrder` for that reason."},
            {"q": "On the preset <code>two-scripts</code>, the second script's variable is "
                  "renamed from `total` to `price` throughout. What does the lab report?",
             "a": ["1 block, 6 lines, as before",
                   "1 block, 4 lines: the subtotal and the test",
                   "2 blocks, one for each renamed line",
                   "0 blocks: only the test for a member still matches, and one line is "
                   "not a run"],
             "c": 3,
             "why": "After the rename, lines 12 and 14 no longer match lines 3 and 5. "
                    "Only the `if` line still matches, a run of one, shorter than the "
                    "minimum of two. The rule is still written twice; the lab matches text "
                    "and cannot see it."},
        ],
        "mistakes": [
            ("Taking Transaction Script for a beginner's pattern that a serious system grows out of",
             "Chapter 9's own When to Use It calls it natural for applications with little "
             "logic, with very little overhead, and tells the reader not to rule it out. "
             "Making a Choice qualifies this without withdrawing it: the better the team, "
             "the more Fowler leans to a Domain Model; he sees no reason for scripts on "
             ".NET, where Table Module is better supported; and a team that starts with "
             "scripts should not hesitate to refactor toward a Domain Model. The three "
             "patterns can also be mixed in one application. What costs a script design "
             "is the duplication as its logic grows, which the lab counts on the lesson's "
             "illustration."),
            ("Thinking a Transaction Script must contain its own SQL",
             "The simplest ones do, but Fowler keeps the database apart even in the plainest "
             "(Chapter 8, Down to the Data Source Layer), putting a Row Data Gateway or a "
             "Table Data Gateway between the script and the database, because the two "
             "make sense as separate parts. The lesson's scripts call `db.insertOrder` "
             "and hold no SQL."),
            ("Expecting subroutines to end the duplication",
             "Factoring out common subroutines is Fowler's first remedy, and on the "
             "lesson's illustration it takes the count to zero. Chapter 2 is careful "
             "about how far it goes: much of the duplication, he says, is hard to "
             "remove and harder still to notice. The lab sees only identical lines, so a copy "
             "with one variable renamed is invisible to it, and so is a rule written two "
             "different ways."),
        ],
        "standard": (
            "Finish when you can find what two scripts share and remove it.",
            "Given two scripts, mark their repeated lines by number, state the lines in "
            "all the copies, and write the subroutine both would call."
        ),
        "note": (
            "The lab finds lines that are identical as text. It cannot find a rule "
            "written twice in different words, and it cannot say whether a repeated "
            "block is one rule or a coincidence; that is a reading of the domain. Nor "
            "does it say when a script design should become a Domain Model. Fowler "
            "says that cutover is hard to quantify."
        ),
    },
    # ---------------------------------------------------------------- 02
    # Chapter 2 on Domain Model (PDF pp. 39-41 of the operator's copy); Chapter 9,
    # Domain Model (pp. 118-125): simple and rich styles (p. 118), coupling and
    # scope (p. 119), bloat (p. 119), When to Use It (p. 120), Evans in
    # preparation (p. 121; References p. 453).
    # Quote: PDF p. 39 of the operator's copy, 24 words, ea_quotes.py OK.
    # Lesson total: 24 words. Course 2's modern aside (PLAN section F.3): Evans.
    {
        "slug": "domain-model",
        "title": "Domain Model",
        "module": "Chapter 9 · Domain Logic Patterns",
        "one_line": "Objects that carry both the data and the rules of the business, each taking the part of the logic that concerns it.",
        "summary": (
            "Chapter 2's second pattern, and Chapter 9's account of it: a model of the "
            "domain in which each object takes the part of the logic relevant to it, "
            "simple when it mirrors the tables and rich when it does not. Count the "
            "decision points in a routine that prices every kind of product, then see "
            "where they go when each kind carries its own rule."
        ),
        "key": [
            "objects with both data and behaviour",
            "each object takes its part of the logic",
            "simple model: close to the tables",
            "rich model: inheritance, strategies",
            "a type switch becomes subclasses",
            "decisions move; they do not vanish",
        ],
        "key_label": "Domain Model in six lines",
        "concepts_intro": (
            "Three ideas from Chapter 9, the last of them the lab's count."
        ),
        "concepts": [
            ("Domain Model",
             "A model of the business made of objects, each holding its data and the behaviour that uses it. "
             "Its objects stand for meaningful things, as large as a company or as small "
             "as one line on an order, and the rules sit beside the data they use."),
            ("Simple and rich",
             "Fowler's two styles. A simple Domain Model looks much like the database, "
             "mostly one class to a table. A rich one can look quite different, with "
             "inheritance, strategies and webs of small objects, and is harder to map to "
             "the database."),
            ("Polymorphism",
             "Calling one method on objects of different classes and letting each class "
             "decide what it does. A chain of tests on a type code can become one call, "
             "with the branches moved into the classes."),
        ],
        "read_title": "The chapter's argument first, then the pattern, then the count",
        "read_intro": (
            "Read the pages on Domain Model in Chapter 2, and the Domain Model pattern "
            "in Chapter 9, in your own copy first. The lesson then counts the decisions "
            "in one routine and in the classes that replace it."
        ),
        "body": [
            ("p", "&ldquo;Rather than one routine having all the logic for a user action, "
                  "each object takes a part of the logic that's relevant to it.&rdquo; That "
                  "is Chapter 2's description of what object-oriented people mean by the "
                  "paradigm shift. This lesson reads Chapter 2 on Domain Model, as "
                  "argument, and the pattern in Chapter 9, as a tool. Read both in your "
                  "own copy first."),
            ("p", "Fowler's case begins where the last lesson's ended: objects are his "
                  "answer to complicated logic. A Domain Model is organised, to a first "
                  "approximation, around the nouns of the domain, with a class for each "
                  "thing the business talks about, and the validations and calculations "
                  "go into those classes. A procedure for some action may still exist, but "
                  "it quickly hands the work to the model. He admits the cost to a "
                  "newcomer: you hunt from one object to the next for the behaviour you "
                  "want."),
            ("p", "Its value, the chapter argues, is that once you are used to it there "
                  "are techniques for handling ever more complex logic in an organised "
                  "way. When a new rule arrives, a Domain Model adds a new object, such as "
                  "a new strategy, where a Transaction Script adds another condition to "
                  "its conditional logic. Its costs are the effort of learning it, which "
                  "can take months and which, he says, a significant minority of "
                  "developers seem unable to make, and the database mapping: the richer the model, "
                  "the more complex the mapping, usually a Data Mapper. Fowler, who calls "
                  "himself an object bigot, says that once the shift is made it "
                  "usually lasts a lifetime."),
            ("p", "Chapter 9 gives the pattern. A Domain Model adds a layer of objects "
                  "that stand for the business area, mingling data and process, with "
                  "multivalued attributes, a web of associations and inheritance. Fowler "
                  "sees two styles in practice. In the simple one the model mirrors the "
                  "database design, mostly one object for each table, and can use Active "
                  "Record. A rich one can look different, with inheritance, strategies and "
                  "other design patterns, and needs a Data Mapper. Because business rules "
                  "change so often, he wants the model easy to modify, build and test, "
                  "with as few dependencies on the other layers as possible."),
            ("p", "He takes up a common worry: bloated domain objects, an order class "
                  "swollen with behaviour that only one screen needs. Moving such behaviour "
                  "into a class for the use case, he answers, leads to duplication, "
                  "because behaviour kept apart from the order is easy to miss, so it gets "
                  "written a second time. In his experience bloat happens much less often than "
                  "predicted and is easy to see and fix, so his advice is to put behaviour "
                  "in the object that is its natural fit and deal with bloat only if and "
                  "when it becomes a problem. When to Use It turns on the complexity of "
                  "the behaviour: complicated, ever-changing rules of validation, "
                  "calculation and derivation want an object model; a few checks for "
                  "missing values and some totals are better as a Transaction Script."),
            ("p", "Now the count. The lab counts decision points by a stated rule: one, "
                  "plus one for each `if`, `while`, `for`, `case`, `&&` and `||`, with "
                  "`else` adding nothing. It also prints a band, the deepest nesting and "
                  "the first line at that depth. The bands, 0–5, 6–10 and 10+, are "
                  "McConnell's, from <em>Code Complete</em>; Fowler gives no count. On "
                  "<code>price-by-kind</code>, one routine that prices every kind of "
                  "product, it counts 5, broken down as 1 + if 3 + && 1, in the band "
                  "0–5, with the deepest nesting 1, first reached at line 5."),
            ("code", _lines(PRICE_BY_KIND)),
            ("p", "On <code>price-delegated</code> each kind of product carries its own "
                  "rule. `Product` is the default, which changes nothing, and `Book`, "
                  "`Alcohol` and `Food` override `adjust`. The listing has no routine at "
                  "its top, only classes, so the lab counts the whole listing: 2, broken "
                  "down as 1 + if 1, band 0–5. The deepest nesting is 2, first at line 15, "
                  "because the lab counts braces from the top of the listing and that "
                  "line sits inside a method inside a class. Every price the switch gave "
                  "is still given, so the fall from 5 to 2 loses no behaviour."),
            ("code", _lines(PRICE_DELEGATED)),
            ("p", "What moved, and what did not? The one decision left lives in `Food`, "
                  "the only kind with a rule about quantity, and it is the decision Food "
                  "needs. The three tests on `p.kind()` are gone from the listing, but "
                  "the question they asked, which kind of product this is, is now "
                  "answered once, when the object is made as a `Book` or a `Food`, by "
                  "whatever builds it. That is Fowler's point about adding rules: a new "
                  "kind is a new class, not a new branch in every routine that asks. The "
                  "count shows where the decisions sit; it does not say the classes are "
                  "better."),
            ("p", "One later view belongs here. The book's references list Eric Evans's "
                  "book on building domain models as in preparation; it appeared as "
                  "<em>Domain-Driven Design</em> (Addison-Wesley, 2003) and carried the "
                  "pattern a long way further: a model built with the domain's experts in "
                  "one shared language, aggregates that are changed as a unit through a "
                  "single root, and bounded contexts that let a large system hold more "
                  "than one model. Many teams now mean Evans's practice when they say "
                  "domain model. Fowler's chapter is the earlier and narrower pattern, a "
                  "way of organising logic in one layer, and the two are best read side "
                  "by side."),
            ("h3", "Exercise"),
            ("code", _lines(SHIPPING_BY_METHOD)),
            ("p", "Count this routine's decision points by the lab's rule, with the "
                  "breakdown. Then say which classes its branches would move to if each "
                  "shipping method carried its own rule, keeping every price the routine "
                  "gives for every parcel, staff parcels included. Paste it into the lab "
                  "to check the count; the classes are yours."),
            ("p", "A Domain Model gives each thing the business tracks an object of its own. "
                  "The next lesson, Table Module, and Making a Choice, reads the pattern "
                  "that gives a whole table one object, and Fowler's advice on choosing "
                  "among the three."),
        ],
        "lab": ("cckit", {
            "mode": "code",
            "view": "complexity",
            "bands": [5, 10],
            "book": "other",
            "preset": "price-by-kind",
            "presets": [
                {"id": "price-by-kind",
                 "label": "One routine prices every kind of product",
                 "code": PRICE_BY_KIND,
                 "expect": {"coDecisions": "5", "coBreakdown": "1 + if 3 + && 1"}},
                {"id": "price-delegated",
                 "label": "Each kind of product carries its own rule",
                 "code": PRICE_DELEGATED,
                 "expect": {"coDecisions": "2", "coBreakdown": "1 + if 1"}},
            ],
            "panel_title": "Where the decisions go in a Domain Model",
            "panel_intro": _COMPLEXITY_INTRO,
        }),
        "steps_title": "Moving a type switch into classes",
        "steps_intro": "Four steps, the last of them on code of your own.",
        "steps": [
            ("Count the decisions",
             "Count one, plus one for each `if`, `while`, `for`, `case`, `&&` and `||`. "
             "An `else` adds nothing."),
            ("Group the branches by kind",
             "For each branch, write which kind of thing it tests for. Tests on the same "
             "kind belong together, and so do tests on a value that only one kind has."),
            ("Write one class a kind, and a default",
             "Give each kind a class whose method holds its branch, and give the base "
             "class the behaviour of the final `return`, for every kind with no rule of "
             "its own. Check that every input still gets the price it got before."),
            ("Do it on your own code",
             "Find one `switch` or `if` chain on a type code in a system you know. "
             "Count its branches, write the figure down, and name the class each branch "
             "would move to."),
        ],
        "worked": {
            "title": "One routine, five decisions",
            "intro": [
                "Count <code>price-by-kind</code> by the lab's rule.",
            ],
            "lines": [
                "start at 1",
                "line 4: if, the test for a book: 2",
                "line 6: if, the test for alcohol: 3",
                "line 8: if, the test for food: 4",
                "line 8: the && on quantity: 5",
                "else adds nothing: 5 in all",
            ],
            "after": [
                "All five are in one routine, and every new kind of product would add "
                "another. In <code>price-delegated</code> four of them go: three became "
                "classes, and one, the test on quantity, moved into `Food` as its only "
                "`if`, which with the starting one makes 2.",
            ],
        },
        "quiz_title": "Decisions, classes and Fowler's two styles",
        "quiz": [
            {"q": "Count the exercise's decision points (one, plus one for each `if`, "
                  "`while`, `for`, `case`, `&&` and `||`). Which classes keep every "
                  "price it gives?",
             "a": ["8; `Post`, `Courier` with its weight test, and a default class that "
                   "charges 0 for `COLLECT` or a staff parcel and 999 otherwise",
                   "6; `Post`, `Courier` with its weight test, and a default class that "
                   "charges 0 for `COLLECT` or a staff parcel and 999 otherwise",
                   "7; `Post`, `Courier` with its weight test, `Collect` charging 0, and "
                   "a default charging 999",
                   "7; `Post`, `Courier` with its weight test, and a default class that "
                   "charges 0 for `COLLECT` or a staff parcel and 999 otherwise"],
             "c": 3,
             "why": "1 + if 4 + && 1 + || 1 = 7: four `if`s, the `&&` on the courier's "
                    "weight and the `||` for staff; the three `else`s add nothing, and six "
                    "forgets the `||`. A `Collect` class alone changes a price: in the "
                    "routine a staff parcel sent by any method but post or courier pays "
                    "nothing, so a staff parcel with no class of its own would pay 999. "
                    "The staff rule belongs in the default class. `COLLECT` can sit beside it "
                    "there, or have a `Collect` class of its own charging 0, as long as the "
                    "default still charges a staff parcel nothing."},
            {"q": "On <code>price-delegated</code>, by the same rule, how many decision "
                  "points does the lab count?",
             "a": ["1", "2", "4", "5"],
             "c": 1,
             "why": "One to start, plus the one `if` in `Food`. Methods and classes are "
                    "not decisions, and the overriding `adjust` methods hold no tests, so "
                    "the listing counts 2. Five is the routine before the change."},
            {"q": "Which mapping does Chapter 9 pair with each style of Domain Model?",
             "a": ["Simple with Data Mapper, rich with Active Record",
                   "Simple with Active Record, rich with Data Mapper",
                   "Both with Table Data Gateway",
                   "Simple with Record Set, rich with Data Mapper"],
             "c": 1,
             "why": "A simple Domain Model, close to the tables, can use Active Record; a "
                    "rich one, which can look quite different from the database, requires "
                    "a Data Mapper."},
            {"q": "What is Fowler's advice on behaviour that only one use case needs?",
             "a": ["Move it into a class for that use case from the start",
                   "Put it in the presentation, near the screen that uses it",
                   "Put it in the object that is its natural fit, and deal with bloat if "
                   "and when it appears",
                   "Split the domain class once it has more than a fixed number of "
                   "methods"],
             "c": 2,
             "why": "Separating usage-specific behaviour, he argues, leads to "
                    "duplication, because people do not find it and write it again; bloat "
                    "occurs less often than predicted and is easy to fix. He gives no "
                    "method count."},
        ],
        "mistakes": [
            ("Thinking a Domain Model is a set of classes that mirror the tables",
             "Fowler's distinction between a simple Domain Model, close to the tables, "
             "and a rich one, with inheritance, strategies and webs of small objects, is "
             "exactly that it need not mirror them. What makes it a domain model is that "
             "the objects carry the behaviour: each takes the part of the logic that "
             "concerns it. A set of classes that only hold the columns is data, whatever "
             "it is called."),
            ("Thinking polymorphism removes the decisions",
             "It moves each one to the class it concerns. On the lesson's illustration "
             "one `if` remains, in `Food`, because Food really does depend on quantity, "
             "and the question of which kind a product is moves to wherever the object "
             "is made. The count falls because the decision is asked once, not because "
             "it went away."),
            ("Splitting every use case's behaviour out of the domain objects",
             "It looks like a cure for bloated classes. Fowler argues it causes the "
             "worse problem: behaviour kept away from the object it concerns is harder "
             "to find, so it gets written again. His advice is to put it in the natural "
             "object and deal with bloat only if it appears."),
        ],
        "standard": (
            "Finish when you can see where a type switch's decisions go in a Domain Model.",
            "Given a routine that switches on a kind, count its decision points with the "
            "breakdown, and write the subclass method that takes one of its branches."
        ),
        "note": (
            "The lab counts decision points in the listing it is given. It cannot see the "
            "decision that moves to where an object is made, and it cannot say whether a "
            "model is simple or rich, or whether the classes are the right ones; Fowler "
            "says the choice turns on the complexity of the behaviour, which no count "
            "settles. The bands are McConnell's guidance for routines, not Fowler's."
        ),
    },
    # ---------------------------------------------------------------- 03
    # Chapter 9, Table Module (PDF pp. 126-132 of the operator's copy); Chapter 18,
    # Record Set (pp. 449-451); Chapter 2, Making a Choice (pp. 42-43); Chapter 8,
    # Starting with the Domain Layer (p. 101).
    # Quote: PDF p. 42 of the operator's copy, 15 words, ea_quotes.py OK.
    # F8, PDF p. 42 of the operator's copy: domain complexity cannot be
    # measured, says Making a Choice. Lesson total: 15 words.
    {
        "slug": "table-module-and-making-a-choice",
        "title": "Table Module, and Making a Choice",
        "module": "Chapter 9 · Domain Logic Patterns",
        "one_line": "One object for all the rows of a table, working on a Record Set; and Fowler's advice on choosing among the three patterns, which no count can settle.",
        "summary": (
            "Chapter 9's third pattern holds the logic for a whole table in one object "
            "that works on a Record Set, Chapter 18's in-memory table. Count the objects "
            "each organisation would hold for the same tables, then read Making a "
            "Choice, where Fowler admits that the quantity his choice turns on cannot "
            "be measured."
        ),
        "key": [
            "one object for all the rows of a table",
            "pass the key to act on one row",
            "built to work on a Record Set",
            "fits platforms with record set tools",
            "no measure of domain complexity",
            "the choice is a judgement call",
        ],
        "key_label": "Table Module and the choice in six lines",
        "concepts_intro": (
            "Two patterns and one admission."
        ),
        "concepts": [
            ("Table Module",
             "One object that carries the business logic for a whole table or view. It has no object for each row, so to act on one row you "
             "pass the module that row's key."),
            ("Record Set",
             "Tabular data held in memory in the shape a query returns, which other "
             "code can also create and edit. It usually the platform's own, such as a data set or a row "
             "set."),
            ("Identity",
             "What makes one object a particular thing, so that holding a reference to "
             "it means holding that employee or that order. A Domain Model's objects "
             "have it, one per row; a Table Module's rows do not."),
        ],
        "read_title": "The pattern first, then Record Set, then the choice",
        "read_intro": (
            "Read Table Module in Chapter 9, Record Set in Chapter 18, Making a Choice "
            "in Chapter 2 and Starting with the Domain Layer in Chapter 8 in your own "
            "copy first. The lesson counts objects between the patterns and the choice."
        ),
        "body": [
            ("p", "&ldquo;The bad news is that nobody knows how to measure the complexity "
                  "of domain logic.&rdquo; That is from Making a Choice, the section of "
                  "Chapter 2 that follows the three patterns and comes before Service "
                  "Layer, which this lesson reads last. First come Chapter 9's Table "
                  "Module and the Record Set it works on, from Chapter 18, both read as "
                  "tools; then the choice among the three patterns, read as Fowler's "
                  "argument. Read them in your own copy first."),
            ("p", "A Table Module gives each table one class, and one instance of it "
                  "carries every operation on that table's data. The main difference "
                  "from a Domain Model, Fowler says, is this: with many orders, a Domain Model has an object "
                  "for each order, and a Table Module has one object for all of them. So "
                  "the module has no notion of identity for the rows it works with. To ask "
                  "about one row you call a method on the module and pass the row's key, "
                  "usually the database's primary key."),
            ("p", "It is usually backed by tabular data, the result of a SQL query held "
                  "in a Record Set, and several Table Modules can work on one Record Set. "
                  "The module can be an instance, which can be set up with an existing "
                  "Record Set and can use inheritance, or a collection of static methods. "
                  "It can run its own queries or take them from a Table Data Gateway. The "
                  "flow Fowler describes is a round trip: a gateway fills a Record Set, a "
                  "module works on it, table-aware widgets show and edit it, and the "
                  "module validates it again before it is saved. A module can be tested "
                  "on a Record Set built in memory. When to Use It names the cost: no "
                  "direct links between instances, and polymorphism does not work well, "
                  "so for complicated logic a Domain Model is the better choice."),
            ("p", "Record Set, in Chapter 18, is the structure that makes the module "
                  "worth having. It has the shape of a query's result, so "
                  "it can go straight to a data-aware screen, and it can be built or "
                  "changed by domain code. It is usually the vendor's, and Fowler's 2002 "
                  "examples are ADO.NET's data set and JDBC's row set. Most have an "
                  "implicit interface, a column asked for by name as a string, which "
                  "Fowler generally frowns on; he minds it less here, because a Record "
                  "Set usually carries its legal columns and the query that made it names "
                  "them. His advice: where the "
                  "environment relies on Record Sets, organise the domain logic with a "
                  "Table Module."),
            ("p", "The listing below is a Table Module in small: one `InvoiceLines` "
                  "object for the whole invoice-line table, given a Record Set when it is "
                  "made. To total one invoice the caller passes its key, and the module "
                  "walks the rows with that key. `RecordSet` and `Record` stand for the "
                  "platform's types, and `r.getLong(\"cents\")` is the implicit interface "
                  "Fowler frowns on: the column named by a string. There are no lab "
                  "figures for this listing; the lab counts objects."),
            ("code", _lines(TABLE_MODULE)),
            ("p", "The lab takes tables and their row counts and prints five tiles: the "
                  "tables, the rows, the objects at one a row, as a Domain Model or a Row "
                  "Data Gateway holds them, the objects at one a table, as a Table Module "
                  "holds them, and the largest table with its rows, which is the most "
                  "rows one module's Record Set carries. On <code>small-shop</code>, four "
                  "tables of 200 customers, 1,500 orders, 120 products and 6,000 lines, "
                  "it prints 4 tables, 7,820 rows, 7,820 objects one a row, 4 objects one "
                  "a table, and line 6,000. Its banner says what the count is not: "
                  "objects, not memory, and every row loaded, which neither pattern "
                  "requires."),
            ("p", "On <code>one-big-table</code>, 250,000 meter readings and 400 meters, "
                  "it prints 2 tables, 250,400 rows, 250,400 objects one a row, 2 one a "
                  "table, and reading 250,000. Read the banner with it. A Domain Model "
                  "would not load a quarter of a million readings; Chapter 9 says a "
                  "session pulls in only the objects it needs. What the count shows is "
                  "the difference in kind: one object per reading, each with its own "
                  "identity and its own methods, against one module that is handed the "
                  "readings and a key. Which you want depends on the logic, and the "
                  "count is silent on that."),
            ("p", "Making a Choice asks how to choose, and answers that it depends very "
                  "much on how complex the domain logic is. Fowler draws a sketch of "
                  "effort against complexity for the three patterns and disowns it in "
                  "advance, as one of the unquantified graphs that irritate him in slides. "
                  "With simple logic a Domain Model costs more than it pays back; as the "
                  "logic grows, the other two hit a wall. He then names a threshold to "
                  "two decimal places, and takes it back in the sentence quoted above. "
                  "All you can do, he says, is find experienced people to analyse the "
                  "requirements and make a judgement call."),
            ("p", "Some factors shift the curves. A team that knows Domain Model lowers "
                  "its starting cost, though not to the others' level because of the "
                  "database mapping, and the better the team the more he leans to it. "
                  "Table Module depends on the Record Set tools around it: with them, as "
                  "on .NET, it is much more attractive, and without them he would not "
                  "bother. The decision can be changed, with difficulty: from scripts, do "
                  "not hesitate to refactor toward a Domain Model; the other way is "
                  "usually less worth it, unless it lets you simplify the data source "
                  "layer. And the three can be mixed. Chapter 8, Starting with "
                  "the Domain Layer, makes the same choice again with the database in "
                  "view, calls it the central choice, and adds that the tools you have "
                  "shape the architecture: of the three, Table Module gains most when the "
                  "tools suit it."),
            ("h3", "Exercise"),
            ("ul", [
                "`patient`: 900 rows",
                "`visit`: 5,400 rows",
                "`doctor`: 30 rows",
                "`ward`: 12 rows",
            ]),
            ("p", "For these four tables of a small clinic, give by hand the objects a "
                  "Domain Model would hold with every row loaded, the objects a Table "
                  "Module would hold, and the largest Record Set one module would work "
                  "on. Then type the tables into the lab, as `patient, 900; visit, "
                  "5400` and so on, to check."),
            ("p", "Whichever pattern holds the domain logic, some code must call it, "
                  "begin and end its transactions, and tell other people what happened. "
                  "The next lesson, Service Layer, reads where that code goes."),
        ],
        "lab": ("eakit", {
            "mode": "load",
            "view": "instances",
            "preset": "small-shop",
            "presets": [
                {"id": "small-shop",
                 "label": "A small shop: customers, orders, products and lines (illustrative)",
                 "tables": "customer, 200; orders, 1500; product, 120; line, 6000",
                 "expect": {"ldRowObjects": "7,820", "ldTableObjects": "4",
                            "ldLargest": "line 6,000"}},
                {"id": "one-big-table",
                 "label": "Meter readings: one table far larger than the rest (illustrative)",
                 "tables": "reading, 250000; meter, 400",
                 "expect": {"ldRowObjects": "250,400", "ldTableObjects": "2",
                            "ldLargest": "reading 250,000"}},
            ],
            "panel_title": "Objects a row against objects a table",
            "panel_intro": (
                "Each record is a table and its rows. The lab counts the objects a Domain Model or Row Data "
                "Gateway would hold, one a row, and a Table Module would hold, one a "
                "table, with every row loaded. The tables are illustrative."
            ),
        }),
        "steps_title": "Counting objects under two organisations",
        "steps_intro": "Four steps, the last of them on a system of your own.",
        "steps": [
            ("List the tables",
             "Write each table with its number of rows. Their number is the count of "
             "table modules."),
            ("Add the rows",
             "Add the row counts. With every row loaded, that is the number of objects a "
             "Domain Model would hold, one a row."),
            ("Find the largest table",
             "The table with the most rows is the largest Record Set one module works "
             "on; on a tie, take the first."),
            ("Do it on your own system",
             "Take the three largest tables in a system you know, write their row "
             "counts and the two object counts, and say in one sentence which of the "
             "three domain patterns its code is closest to, and why."),
        ],
        "worked": {
            "title": "A small shop, counted two ways",
            "intro": [
                "Count <code>small-shop</code>: customer 200, orders 1,500, product 120, "
                "line 6,000.",
            ],
            "lines": [
                "tables: 4",
                "rows: 200 + 1500 + 120 + 6000, so 7820",
                "one object a row: 7820",
                "one object a table: 4",
                "largest table: line, with 6000 rows",
            ],
            "after": [
                "A Domain Model with everything loaded would hold 7,820 objects, each with "
                "an identity; four table modules would hold the same rows in Record Sets, "
                "the largest of them 6,000 rows long. Neither pattern needs everything "
                "loaded, and the count does not say which to choose.",
            ],
        },
        "quiz_title": "Objects, identity and the choice",
        "quiz": [
            {"q": "For the exercise's tables (patient 900, visit 5,400, doctor 30, ward "
                  "12), how many objects at one a row, how many table modules, and what "
                  "is the largest Record Set?",
             "a": ["6,342 against 4; visit, 5,400 rows",
                   "6,342 against 4; patient, 900 rows",
                   "6,330 against 4; visit, 5,400 rows",
                   "6,342 against 6,342; visit, 5,400 rows"],
             "c": 0,
             "why": "900 + 5,400 + 30 + 12 = 6,342 objects at one a row, against 4 "
                    "modules, one a table. The largest table is `visit`, so the largest "
                    "Record Set one module works on holds 5,400 rows. `patient` is only "
                    "the first table listed, and 6,330 leaves out the ward."},
            {"q": "In a Table Module, how do you act on one particular row?",
             "a": ["Call a method on that row's own object",
                   "Use a Domain Model object for that row only",
                   "Ask the Record Set to create an object for the row",
                   "Call a method on the module and pass the row's key"],
             "c": 3,
             "why": "The module has no notion of identity for the rows it works on, so "
                    "every operation on one row takes some identity reference, usually "
                    "the primary key."},
            {"q": "What does Making a Choice say about where an application lies on its "
                  "sketch's complexity axis?",
             "a": ["Count the classes the domain needs",
                   "Count the use cases, and choose a Domain Model above a threshold",
                   "Nobody knows how to measure it, so experienced people make a "
                   "judgement call",
                   "Measure the effort of a prototype in each pattern"],
             "c": 2,
             "why": "The sketch's axes are unquantified, and Fowler says so; the "
                    "threshold he names is a joke he takes back at once. The complexity "
                    "of domain logic cannot be measured, so the decision is a judgement "
                    "by people with experience."},
            {"q": "What does Fowler say about Table Module in an environment with no "
                  "special tooling for Record Sets?",
             "a": ["It is the best choice there, since it needs no framework",
                   "He would not bother with it",
                   "It should be combined with a Data Mapper",
                   "It is preferable to Transaction Script there"],
             "c": 1,
             "why": "Its attractiveness depends very much on support for a common Record "
                    "Set in the environment; without such tooling, he says, he would not "
                    "bother with Table Module."},
        ],
        "mistakes": [
            ("Thinking Table Module is a Domain Model with fewer objects",
             "A Table Module has no object for each row, so it has no identity for each "
             "row, and the logic for one row runs on the module given that row's key. "
             "Fowler sets the two patterns apart on exactly this. It also gives up what "
             "identity buys: direct links from one instance to another, and the "
             "polymorphism a rich Domain Model relies on. The lab's count of 7,820 "
             "against 4 is the size of that difference on the lesson's illustration, not "
             "a saving."),
            ("Reading Making a Choice as a threshold",
             "The chapter's sketch has no units on either axis, and Fowler says so; the "
             "precise figure he offers is a joke he withdraws in the next sentence, "
             "because nobody can measure the complexity of domain logic. The threshold "
             "is a judgement by experienced people, and this lesson does not pretend to "
             "compute it."),
            ("Choosing Table Module without the tools it needs",
             "Table Module's strength is how it fits the rest of an architecture built "
             "around Record Sets: queries, screens and validation all passing the same "
             "structure. Without that tooling, Fowler says, he would not bother with "
             "it, and if the objects and tables are much alike he suggests a Domain "
             "Model with Active Record instead."),
        ],
        "standard": (
            "Finish when you can count the objects each organisation holds.",
            "Given tables and their row counts, state how many objects a Domain Model "
            "and a Table Module hold with every row loaded, and the most rows one module "
            "object's Record Set carries."
        ),
        "note": (
            "The lab counts objects, not memory, and it assumes every row is loaded, "
            "which neither pattern requires. It cannot place a system on Fowler's "
            "complexity axis, because, as Making a Choice says, nobody knows how to "
            "measure that; the choice among the three patterns is a judgement the "
            "count only informs."
        ),
    },
    # ---------------------------------------------------------------- 04
    # Chapter 2, Service Layer (PDF p. 44 of the operator's copy); Chapter 9,
    # Service Layer, by Randy Stafford (pp. 133-139): Kinds of "Business Logic"
    # (p. 134), Implementation Variations (p. 134), To Remote or Not to Remote
    # (p. 134), Identifying Services and Operations (p. 135), Session Facade
    # (p. 135), When to Use It (p. 136).
    # Quote: PDF p. 136 of the operator's copy, 31 words, ea_quotes.py OK; the
    # words are Stafford's. Lesson total: 31 words.
    {
        "slug": "service-layer",
        "title": "Service Layer",
        "module": "Chapter 9 · Domain Logic Patterns",
        "one_line": "Randy Stafford's boundary of application operations, which holds the transactions and notifications each kind of client would otherwise repeat.",
        "summary": (
            "Chapter 2's account of a layer of services over the domain, and Randy "
            "Stafford's pattern in Chapter 9: a boundary that defines the operations "
            "clients see and coordinates the response to each. Count the application "
            "logic two kinds of client repeat, then move it into one service "
            "operation."
        ),
        "key": [
            "a boundary of application operations",
            "domain logic: about the problem",
            "application logic: notify, transact",
            "a second kind of client: add the layer",
            "Fowler: as thin as you can, if any",
            "Stafford: a rich layer serves well",
        ],
        "key_label": "Service Layer in six lines",
        "concepts_intro": (
            "Stafford's pattern rests on a distinction between two kinds of business "
            "logic, and offers two ways to build the layer."
        ),
        "concepts": [
            ("Domain logic and application logic",
             "Stafford's two kinds of business logic. Domain logic is about the problem "
             "itself, such as how an order is priced. Application logic is about the "
             "application's responsibilities, such as telling people and other systems "
             "that something happened, and running the work in one transaction."),
            ("Domain facade",
             "A Service Layer of thin classes in front of a Domain Model. They hold "
             "no business logic; they set the boundary and the operations, and the "
             "model does the rest."),
            ("Operation script",
             "A Service Layer made of thicker classes that carry out the application "
             "logic themselves and hand the domain logic to domain objects. Each class "
             "groups related operations and is usually named something Service."),
        ],
        "read_title": "Two authors on one layer, then the count",
        "read_intro": (
            "Read the Service Layer section of Chapter 2, which is Fowler's, and the "
            "Service Layer pattern in Chapter 9, which is Randy Stafford's, in your own "
            "copy first. The lesson then counts what two clients repeat."
        ),
        "body": [
            ("p", "&ldquo;But as soon as you envision a second kind of client, or a second "
                  "transactional resource in use case responses, it pays to design in a "
                  "Service Layer from the beginning.&rdquo; The words are Randy Stafford's, "
                  "from his Service Layer pattern in Chapter 9 of Fowler's book. This "
                  "lesson reads Chapter 2's section on the layer, which is Fowler's "
                  "argument, and then Stafford's pattern. Read both in your own copy "
                  "first."),
            ("p", "Chapter 2 describes a common approach: split the domain layer in two "
                  "and put a Service Layer over a Domain Model or a Table Module, so that "
                  "the presentation talks to the domain only through it, as an API for "
                  "the application. It is also a good place for transaction control and "
                  "security. The key decision, Fowler says, is how much behaviour it "
                  "holds. At one extreme it is a facade that forwards every call to the "
                  "objects below; at the other, most of the business logic is in "
                  "Transaction Scripts inside it, over simple domain objects. Between them "
                  "is the controller-entity style, which he has never liked much: its "
                  "use-case controllers invite duplicate code, as scripts do."),
            ("p", "His own preference is as thin a Service Layer as possible, and none "
                  "if he can manage without one; he assumes he does not and adds it when the "
                  "application seems to need it. Then he concedes the point at once. Many "
                  "good designers, he says, always use a Service Layer with a good deal "
                  "of logic, and Stafford has done well with a rich layer, "
                  "which is why Fowler asked him to write the pattern. So the book holds "
                  "two answers to how thick the layer should be, and says so."),
            ("p", "Stafford's pattern defines the layer as an application's boundary: a "
                  "set of available operations, seen from the clients' side, each of which "
                  "coordinates the application's response. His motivation is that "
                  "enterprise applications have several kinds of interface, such as data "
                  "loaders, user interfaces and integration gateways, which need the same "
                  "interactions with the application, and coding them again in each "
                  "interface duplicates them. His section "
                  "Kinds of &ldquo;Business Logic&rdquo; then divides the logic into "
                  "domain logic, about the problem domain, and application logic, about "
                  "the application's responsibilities, such as notifying administrators "
                  "and integrated systems. Putting the second kind in domain classes "
                  "makes them less reusable across applications, and harder to move into "
                  "a workflow tool."),
            ("p", "He gives two ways to build the layer: a domain facade, thin classes "
                  "over a Domain Model that does all the business logic, and an operation "
                  "script, thicker classes that carry out the application logic and "
                  "delegate the domain logic. The operations come from the use cases and "
                  "the screens; many are plain create, read, update and delete, but what "
                  "the application must do around them, notifying people and other "
                  "systems, is often far from dull, and the operation coordinates it "
                  "and makes it atomic. Its interface is coarse-grained, so it could be "
                  "called remotely, but his advice is to start with a local layer and add "
                  "a Remote Facade only if you need one. When to Use It turns the "
                  "quotation round: with one kind of client and no response that spans "
                  "several transactional resources, you probably do not need the "
                  "layer."),
            ("p", "Now the code. In the listing below a web page and a nightly import "
                  "both place orders, and each does the whole response itself. On the "
                  "preset <code>orders-twice</code> the lab finds 1 repeated block, 10 "
                  "lines in all the copies, at lines 4–8 and lines 13–17: five lines in "
                  "each client, from `db.begin()` to the confirmation mail. Only the line "
                  "that builds the order differs, from the form in one and from the "
                  "imported row in the other."),
            ("code", _lines(ORDERS_TWICE)),
            ("p", "Read what repeats with Stafford's distinction. The transaction and "
                  "the mail are application logic. Inside them are two domain calls, "
                  "reserving the stock and `order.confirm()`, each already in one place "
                  "on its own object. What each client has had to write for itself is "
                  "the response that coordinates them, and a third kind of client would "
                  "write it a third time."),
            ("p", "On <code>orders-served</code> the response is one operation, "
                  "`placeOrder` in an `OrderService`, and each client builds its order "
                  "and calls it: 0 repeated blocks, 0 lines, none. This is Stafford's "
                  "operation script in small. The five lines did not disappear; they "
                  "exist once, and the transaction and the mail now have a home. The lab "
                  "cannot tell application logic from domain logic; that sorting is "
                  "yours."),
            ("code", _lines(ORDERS_SERVED)),
            ("h3", "Exercise"),
            ("code", _lines(CANCEL_TWICE)),
            ("p", "A web page and a phone client both cancel orders. Mark the lines they "
                  "repeat by the lab's rule and the lines in all the copies, write the "
                  "service operation both would call, and say which line stays in its "
                  "own client and why."),
            ("p", "A Service Layer is built from the domain's objects. The next lesson, "
                  "Value Object, starts Chapter 18's small objects with the smallest: one "
                  "whose equality is its value."),
        ],
        "lab": ("cckit", {
            "mode": "code",
            "view": "dupes",
            "min_run": 2,
            "preset": "orders-twice",
            "presets": [
                {"id": "orders-twice",
                 "label": "A web page and a nightly import each place an order",
                 "code": ORDERS_TWICE,
                 "expect": {"coDupBlocks": "1", "coDupLines": "10",
                            "coDupWhere": "lines 4–8 and lines 13–17"}},
                {"id": "orders-served",
                 "label": "Both clients call one service operation",
                 "code": ORDERS_SERVED,
                 "expect": {"coDupBlocks": "0", "coDupLines": "0", "coDupWhere": "none"}},
            ],
            "panel_title": "The application logic two clients repeat",
            "panel_intro": _DUPES_INTRO,
        }),
        "steps_title": "Finding the response each client repeats",
        "steps_intro": "Four steps, the last of them on a system of your own.",
        "steps": [
            ("List the clients",
             "Find every client that runs the same use case: pages, jobs, APIs, "
             "imports."),
            ("Mark what each repeats",
             "Mark the identical runs of statement lines, and sort each line into "
             "domain logic, about the problem, and application logic, such as "
             "transactions and notifications."),
            ("Write one operation",
             "Move the repeated response into one service operation that takes what "
             "the clients build, and leave in each client only what is about its own "
             "request."),
            ("Do it on your own system",
             "Take the clients of one domain operation in a system you know. Count the "
             "lines of transaction, notification and integration code each repeats, "
             "and write the figure down."),
        ],
        "worked": {
            "title": "Two clients, one response",
            "intro": [
                "Find the repeated block in <code>orders-twice</code>.",
            ],
            "lines": [
                "line 3 and line 12 differ: form, or row",
                "lines 4 and 13: db.begin()",
                "lines 5 and 14: reserve the stock",
                "lines 6 and 15: order.confirm()",
                "lines 7 and 16: db.commit()",
                "lines 8 and 17: send the confirmation",
                "one block, five lines in two copies: 10",
            ],
            "after": [
                "Three of the five repeated lines are plainly application logic: the "
                "transaction's begin and commit, and the mail. Two are calls into the "
                "domain, `inventory.reserve` and `order.confirm()`, which the response "
                "must run together inside the transaction. Stafford's operation script "
                "takes all five, because together they are the use case's response; "
                "the rules themselves stay in `reserve` and `confirm`.",
            ],
        },
        "quiz_title": "Clients, logic and the two answers",
        "quiz": [
            {"q": "In the exercise, which lines do the two clients repeat by the lab's rule "
                  "(runs of two or more identical statement lines), and what does the "
                  "phone client keep?",
             "a": ["lines 3–7 and lines 13–17, 10 lines; `audit.record` moves into the "
                   "service",
                   "lines 2–7 and lines 12–17, 12 lines; it keeps `audit.record`",
                   "lines 3–7 and lines 13–17, 10 lines; it keeps `audit.record`",
                   "lines 4–8 and lines 14–18, 10 lines; it keeps `audit.record`"],
             "c": 2,
             "why": "Lines 3 to 7 of the web client (begin, release, cancel, commit, "
                    "mail) match lines 13 to 17 of the phone client: one block, 10 lines. "
                    "Lines 2 and 12 differ, since each finds the order from its own "
                    "request. One `cancelOrder(Order order)` in the service replaces both "
                    "blocks. The phone client keeps `audit.record(call)`: it records the "
                    "API call, which is about that request, and the web page has no "
                    "such step, so moving it into the operation would change what the web "
                    "page does."},
            {"q": "By Stafford's Kinds of &ldquo;Business Logic&rdquo;, which of these is "
                  "application logic?",
             "a": ["The rule for an order's discount",
                   "Working out the tax on an order's lines",
                   "Sending the customer a confirmation mail once the order is placed",
                   "The strategy for recognising revenue on a contract"],
             "c": 2,
             "why": "Application logic is about the application's responsibilities, such "
                    "as notifying people and integrated systems; the others are rules of "
                    "the problem domain. Revenue recognition strategies are Stafford's own "
                    "example of domain logic."},
            {"q": "When does Stafford say you probably do not need a Service Layer?",
             "a": ["When the application is not distributed",
                   "With one kind of client and no use case response that involves "
                   "several transactional resources",
                   "Whenever the domain uses Transaction Scripts",
                   "When the domain model has fewer than a couple of dozen classes"],
             "c": 1,
             "why": "With one kind of client, such as a user interface, and responses "
                    "that touch one transactional resource, the page controllers can "
                    "control the transactions themselves. Once a further kind of client or "
                    "a further transactional resource appears, he says it pays to "
                    "design the layer in, even in an undistributed architecture."},
            {"q": "What is Fowler's own preference in Chapter 2, and what does he concede?",
             "a": ["A rich layer always; he concedes it costs more to build",
                   "As thin a layer as possible, if any; he concedes many good "
                   "designers always use a rich one",
                   "The controller-entity style; he concedes it can duplicate code",
                   "No layer ever; he concedes Stafford disagrees"],
             "c": 1,
             "why": "He prefers as thin a Service Layer as possible, if one is needed at all, and "
                    "says many good designers, Stafford among them, use one with a good "
                    "deal of logic. The controller-entity style is the one he has never "
                    "liked much."},
        ],
        "mistakes": [
            ("Thinking domain logic and application logic are the same, so it does not matter which layer holds a rule",
             "Stafford divides them in Kinds of &ldquo;Business Logic&rdquo;: domain logic "
             "is about the problem domain, application logic about the application's "
             "responsibilities, such as notifying people and integrated systems. Putting "
             "the second in domain classes makes them harder to reuse in another "
             "application. How thick the service should be is a separate question, and "
             "the book gives two answers: Fowler prefers it thin, and says plainly that "
             "good designers, Stafford among them, make it rich. On the lesson's "
             "illustration the repeated lines are mostly the second kind."),
            ("Thinking every application needs a Service Layer",
             "Stafford says not: with one kind of client and no response spanning "
             "several transactional resources, page controllers can manage the "
             "transactions. The condition in the lesson's opening quotation, another "
             "kind of client or another transactional resource, is the reason to "
             "have one."),
            ("Taking a Service Layer for a remote interface",
             "Its interface is coarse-grained, so it can be called remotely, and the J2EE "
             "Session Facade looks similar. Stafford separates them: Session Facade was "
             "motivated by the cost of remote calls to entity beans, Service Layer by "
             "factoring responsibility to avoid duplication. His advice is to start with "
             "a local layer and add remote access only if it is needed."),
        ],
        "standard": (
            "Finish when you can move a repeated response into one operation.",
            "Given two clients that each run the same response to a use case, mark the "
            "repeated lines, and write the service operation both would call."
        ),
        "note": (
            "The lab finds the lines two clients repeat; it cannot tell application logic "
            "from domain logic, and it cannot say how thick a Service Layer should be. "
            "The book itself gives two answers to that, Fowler's thin layer and "
            "Stafford's rich one, and both are presented here."
        ),
    },
]
