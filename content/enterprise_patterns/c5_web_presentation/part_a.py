"""Web Presentation, lessons 1-6 -- Chapters 4 and 14.

Fowler et al., Patterns of Enterprise Application Architecture (Addison-Wesley,
2002): Chapter 4, Web Presentation (PDF pp. 65-71 of the operator's copy), read
with the seven patterns of Chapter 14, Web Presentation Patterns (pp. 299-350).
The operator's copy has no printed page numbers, so every page below is a PDF
page of that copy, in a comment only; the lessons cite the book by chapter,
section and pattern. Every quotation is copied from that copy and checked with
ea_quotes.py. The code is written for these lessons: none of the book's
listings or example domains is used. Each snippet is one constant below, used
both by the lesson's code block and by the lab preset that counts it, so the
line numbers the prose names are the lab's. The design is
docs/enterprise-patterns/PLAN.md, section C, Course 5.
"""


def _lines(text):
    """A snippet constant as a code block's list of lines."""
    return text.split("\n")


# ---------------------------------------------------------------- snippets
# Verbatim from docs/enterprise-patterns/presets.py (PLAN section D.4).

# 5.1 Model View Controller (body).
CONCERT_MODEL = """\
// The model knows nothing of pages; the view asks the model.
class Concert {
    private final String act;
    private final String venue;
    Concert(String act, String venue) {
        this.act = act;
        this.venue = venue;
    }
    String act() { return act; }
    String venue() { return venue; }
}

class ConcertView {
    String render(Concert c) {
        return "<h1>" + escape(c.act()) + " at " + escape(c.venue())
            + "</h1>";
    }
}"""

# 5.2 Page Controller: presets concert-page, concert-page-split; exercise.
CONCERT_PAGE = """\
// The page controller for one page: read input, choose a view.
void doGet(Request req, Response res) throws IOException {
    Concert c = concerts.find(req.param("id"));
    if (c == null) {
        res.forward("missing.jsp", null);
    } else if (c.isSoldOut()) {
        res.forward("waitlist.jsp", c);
    } else if (c.isSeated() && c.hasSeatMap()) {
        res.forward("seats.jsp", c);
    } else {
        res.forward("tickets.jsp", c);
    }
}"""

CONCERT_PAGE_SPLIT = """\
// The decisions move to a presentation helper; the model keeps its
// own predicates, and the controller only forwards.
void doGet(Request req, Response res) throws IOException {
    Concert c = concerts.find(req.param("id"));
    res.forward(helper.viewFor(c), c);
}"""

BOOKING_PAGE = """\
void doPost(Request req, Response res) throws IOException {
    Booking b = bookings.find(req.param("id"));
    String seats = req.param("seats");
    if (b == null || seats == null) {
        res.forward("error.jsp", null);
        return;
    }
    int n = Integer.parseInt(seats);
    if (n < 1 || n > 8) {
        res.forward("booking.jsp", b);
    } else if (b.isPaid() && !b.isRefundable()) {
        res.forward("locked.jsp", b);
    } else {
        b.setSeats(n);
        res.forward("confirm.jsp", b);
    }
}"""

# 5.3 Front Controller: presets pages-repeat, page-superclass,
# front-handler; exercise.
PAGES_REPEAT = """\
void orderPage(Request req, Response res) throws IOException {
    User u = sessions.user(req);
    if (u == null) { res.redirect("/login"); return; }
    audit.log(u, req.path());
    res.forward("order.jsp", orders.find(req.param("id")));
}

void invoicePage(Request req, Response res) throws IOException {
    User u = sessions.user(req);
    if (u == null) { res.redirect("/login"); return; }
    audit.log(u, req.path());
    res.forward("invoice.jsp", invoices.find(req.param("id")));
}"""

PAGES_SUPERCLASS = """\
// A Layer Supertype runs the shared steps; each page adds its own.
abstract class SecurePage {
    void doGet(Request req, Response res) throws IOException {
        User u = sessions.user(req);
        if (u == null) { res.redirect("/login"); return; }
        audit.log(u, req.path());
        show(req, res);
    }
    abstract void show(Request req, Response res) throws IOException;
}
class OrderPage extends SecurePage {
    void show(Request req, Response res) throws IOException {
        res.forward("order.jsp", orders.find(req.param("id")));
    }
}
class InvoicePage extends SecurePage {
    void show(Request req, Response res) throws IOException {
        res.forward("invoice.jsp", invoices.find(req.param("id")));
    }
}"""

FRONT_HANDLER = """\
// One handler for every request; a command does each page's part.
void handle(Request req, Response res) throws IOException {
    Command c = commands.get(req.path());
    User u = sessions.user(req);
    if (u == null && c.needsLogin()) { res.redirect("/login"); return; }
    audit.log(u, req.path());
    c.run(req, res);
}"""

REPORTS_REPEAT = """\
void salesReport(Request req, Response res) throws IOException {
    res.setHeader("Cache-Control", "no-store");
    Locale locale = locales.forRequest(req);
    Report r = reports.sales(req.param("month"));
    res.forward("sales.jsp", r.in(locale));
}

void stockReport(Request req, Response res) throws IOException {
    res.setHeader("Cache-Control", "no-store");
    Locale locale = locales.forRequest(req);
    Report r = reports.stock(req.param("depot"));
    res.forward("stock.jsp", r.in(locale));
}"""

# 5.4 Template View and Transform View: presets ticket-row, ticket-helper;
# exercise.
TICKET_ROW = """\
// A row of the page, with its decisions inline.
String row(Ticket t) {
    String html = "<tr><td>" + escape(t.section()) + "</td>";
    if (t.seatsLeft() < 10 || t.isLastRelease()) {
        html = html + "<td class=\\"few\\">";
    } else {
        html = html + "<td>";
    }
    if (t.isResale() && !t.isLastRelease()) {
        html = html + "resale ";
    }
    return html + t.seatsLeft() + "</td></tr>";
}"""

TICKET_HELPER = """\
// The helper decides; the template only prints what it is given.
class TicketHelper {
    private final Ticket t;
    TicketHelper(Ticket t) { this.t = t; }
    boolean isFew() {
        return t.seatsLeft() < 10 || t.isLastRelease();
    }
    boolean showResale() {
        return t.isResale() && !t.isLastRelease();
    }
}"""

PRICE_CELL = """\
String cell(Item item, Locale locale) {
    String html = "<td>";
    if (item.onSale() && item.saleCents() < item.cents()) {
        html = html + "<s>" + money(item.cents(), locale) + "</s> ";
        html = html + money(item.saleCents(), locale);
    } else {
        html = html + money(item.cents(), locale);
    }
    if (item.stock() == 0 || item.isWithdrawn() || item.isRecalled()) {
        html = html + " (unavailable)";
    }
    return html + "</td>";
}"""

# 5.5 Two Step View (body).
SECOND_STAGE = """\
// Stage one builds a logical screen; stage two turns it into HTML.
class Field {
    final String label;
    final String value;
    Field(String label, String value) {
        this.label = label;
        this.value = value;
    }
}

class HtmlRenderer {
    String render(List<Field> screen) {
        StringBuilder out = new StringBuilder("<dl>");
        for (Field f : screen) {
            out.append("<dt>").append(escape(f.label)).append("</dt>")
               .append("<dd>").append(escape(f.value)).append("</dd>");
        }
        return out.append("</dl>").toString();
    }
}"""

# 5.6 Application Controller: presets flow-repeat, next-screen; exercise.
FLOW_REPEAT = """\
void afterAddress(Order o, Response res) throws IOException {
    if (o.needsCustomsForm()) { res.redirect("/customs"); return; }
    if (o.total() > LIMIT) { res.redirect("/approval"); return; }
    res.redirect("/payment");
}

void afterCart(Order o, Response res) throws IOException {
    if (!o.hasAddress()) { res.redirect("/address"); return; }
    if (o.needsCustomsForm()) { res.redirect("/customs"); return; }
    if (o.total() > LIMIT) { res.redirect("/approval"); return; }
    res.redirect("/payment");
}"""

NEXT_SCREEN = """\
// The flow in one place: which screen comes next.
String nextScreen(Order o) {
    if (!o.hasAddress()) { return "/address"; }
    if (o.needsCustomsForm()) { return "/customs"; }
    if (o.total() > LIMIT) { return "/approval"; }
    return "/payment";
}"""

CLAIM_FLOW = """\
void afterDetails(Claim c, Response res) throws IOException {
    if (c.amount() > 10000) { res.redirect("/assessor"); return; }
    if (c.hasInjury()) { res.redirect("/medical"); return; }
    res.redirect("/bank");
}

void afterPhotos(Claim c, Response res) throws IOException {
    if (c.photos() == 0) { res.redirect("/photos"); return; }
    if (c.photosTooLarge()) { res.redirect("/resize"); return; }
    if (c.amount() > 10000) { res.redirect("/assessor"); return; }
    if (c.hasInjury()) { res.redirect("/medical"); return; }
    res.redirect("/bank");
}"""

# Dependency records the exercises list (not presets: the exercise is the
# reader's). One record a line, each ending in the lab's separator.
CHECKOUT_DEPS = """\
basket, widgets;
checkoutpage, basket;
basketapi, basket;
checkoutpage, widgets"""

SCREEN_DEPS = """\
home, screen;
search, screen;
account, screen;
renderer, screen;
renderer, look;
printrenderer, screen;
printrenderer, printlook"""


# ---------------------------------------------------------------- 01
# Chapter 4's opening, PDF pp. 65-66 of the operator's copy; Chapter 14,
# Model View Controller, pp. 300-301.
# Quote: PDF p. 301 of the operator's copy, 16 words, ea_quotes.py OK.
# Lesson total: 16 words.
# Reenskaug and Smalltalk, late 1970s (p. 300); the two separations and the
# direction of the dependencies (pp. 300-301); "input controller" (p. 65);
# the request's round from controller to model to view (p. 66).
MODEL_VIEW_CONTROLLER = {
    "slug": "model-view-controller",
    "title": "Model View Controller",
    "module": "Chapter 14 · Web Presentation Patterns",
    "one_line": "Model View Controller makes two separations, and the one that matters most is that the presentation depends on the model while the model knows nothing of the presentation.",
    "summary": (
        "Chapter 4 opens the book's web presentation with scripts, server pages and the "
        "input controller, and Chapter 14's Model View Controller names the two separations "
        "underneath: presentation from model, which Fowler ranks among the most important "
        "principles in software, and view from controller, which matters much less. Count "
        "what a change to an HTML library reaches when the model knows about HTML, and when "
        "it does not."
    ),
    "key": [
        "presentation depends on the model",
        "the model never depends on the page",
        "view from controller matters less",
        "input controller: reads the request",
        "direct: who uses the changed class",
        "reached: who uses those, and so on",
    ],
    "key_label": "Model View Controller in six lines",
    "concepts_intro": (
        "Three terms carry the chapter's opening and the pattern. Fowler uses the first in "
        "place of a word he finds overloaded."
    ),
    "concepts": [
        ("Model, view and controller",
         "The three roles of Model View Controller. The model is a nonvisual object holding "
         "the domain's data and behaviour. The view displays the model and does nothing else. "
         "The controller takes the user's input, works on the model and has the view "
         "updated. View and controller together are the user interface."),
        ("Input controller",
         "Fowler's name, in Chapter 4, for the controller of Model View Controller on the "
         "web: the object that receives a request, pulls information off it, hands the work "
         "to the model and picks the view. He uses the longer name because the word "
         "controller is used for other things, among them the Application Controller of the "
         "last lesson in this course."),
        ("The direction of a dependency",
         "Class A depends on class B when A uses B, so that a change to B can force a change "
         "to A. Model View Controller asks for the dependency in one direction only: the "
         "presentation depends on the model, and the model does not depend on the "
         "presentation."),
    ],
    "read_title": "The chapter's opening and the pattern, then the count",
    "read_intro": (
        "Read the opening of Chapter 4, Web Presentation, and then Model View Controller "
        "in Chapter 14, in your own copy first. The lesson reads the first as an argument "
        "and the second as a pattern, and then counts what a change reaches in two small "
        "designs."
    ),
    "body": [
        ("p", "&ldquo;the separation of presentation and model is one of the most important "
              "design principles in software&rdquo;: that is Fowler's verdict in Model View "
              "Controller's When to Use It, in Chapter 14, and the only exception he allows is "
              "a very simple system whose model has no real behaviour in it. This lesson "
              "reads the opening of Chapter 4, Web Presentation, as the argument that leads "
              "there, and then the pattern itself. Read both in your own copy first."),
        ("p", "Chapter 4 starts from the web server. A server is configured to hand each URL "
              "to a program, and Fowler finds two ways to write that program. A script, such "
              "as a CGI script or a Java servlet, reads the request and writes the response "
              "as a stream of text. A server page, as in PHP, ASP or JSP, is written as the "
              "HTML page it returns, with small pieces of code, called scriptlets, inserted "
              "where something has to be computed. Scripts, he observes, are best at "
              "interpreting a request and server pages at formatting a response, so the "
              "obvious move is to use one for each. That move, he says, is an old idea, and "
              "its name is Model View Controller."),
        ("p", "He then warns about a word. Before web applications, he says, most "
              "presentations of the pattern he sat through got it wrong, largely because "
              "controller means several things, so he calls this one the input controller. "
              "His picture of a request is a round trip: the input controller pulls "
              "information off the request and hands the business logic to a model object; "
              "the model talks to the data source and gathers what the response needs; "
              "then the input controller gets control back, reads what came of it, picks "
              "a view and hands it the data. The first and most important reason for all "
              "this, Chapter 4 says, is that the models are kept entirely apart from the "
              "web presentation, which makes the presentation easier to "
              "change, a second presentation easier to add, and the domain logic easier to "
              "test."),
        ("p", "Model View Controller, in Chapter 14, is read as a pattern: a tool with its "
              "own description, to look up. Its history is short and has one name in it. "
              "Trygve Reenskaug built it as a framework for Smalltalk in the late 1970s, and "
              "it has shaped most user-interface frameworks since. The pattern has three "
              "roles: a model that is nonvisual and holds everything but the user interface, "
              "a view that only displays, and a controller that takes input, works on the "
              "model and has the view updated. Fowler sees two principal separations in it: "
              "presentation from model, and controller from view."),
        ("p", "The first, he argues, matters for three reasons. Presentation and model are "
              "different concerns, written with different libraries and often by people "
              "who prefer one side. Users want the same model shown in different ways, in a "
              "desktop program, a web page, a service other programs call, or a terminal, "
              "and the separation "
              "lets all of them share the model's code. And nonvisual objects are easier to "
              "test. The key point, he says, is which way the dependencies run: the "
              "presentation uses the model, and the model never uses the presentation, so the people writing the model need not know which "
              "presentation is in use, and the presentation can change freely."),
        ("p", "The second separation, of view from controller, Fowler calls less important. "
              "The irony he points out is that almost every version of Smalltalk did not "
              "make it. Most systems have one controller for each view, so the separation is "
              "usually skipped in rich clients; it came back on the web, where the input "
              "controller is a separate object, and most of Chapter 14's patterns are built "
              "on it. He adds that the controller is often misplaced between the model and "
              "the view, which is where an Application Controller sits, and that this is a "
              "very different thing."),
        ("p", "Now the code. The listing below is the lesson's, not the book's: a `Concert` "
              "with an act and a venue, and a `ConcertView` that renders it as a heading. "
              "`escape` stands for some routine of the HTML library that makes text safe to "
              "put in a page. Read the imports the listing would need: `ConcertView` needs "
              "the HTML library and `Concert`; `Concert` needs neither."),
        ("code", _lines(CONCERT_MODEL)),
        ("p", "The lab reads a design as dependency records, written `dependent, dependency`, "
              "and a class that changes. It lists the classes that depend on the changed "
              "class directly, then every class the change reaches by following those "
              "records backwards, step after step; the changed class itself is never in "
              "either list. In the preset <code>model-knows-html</code>, `concert` has been "
              "given a method that formats itself with the HTML library, so the records are "
              "`concert, html`, `concertpage, concert` and `concertreport, concert`. Change "
              "`html` and the lab prints 1: concert directly and 3: concert, concertpage, "
              "concertreport in all. The report, which has nothing to do with HTML, is "
              "reached only because the model knew about HTML."),
        ("p", "In <code>separated</code> the design is the listing's (`concertpage` is the "
              "listing's `ConcertView`): `concertpage` uses "
              "`concert` and `html`, and `concertreport` uses `concert`. The same change "
              "prints 1: concertpage directly and 1: concertpage in all. Only the class that "
              "renders HTML is reached, which is Fowler's direction of dependencies as a "
              "count. Being reached does not mean being edited: it means the class must at "
              "least be looked at, rebuilt and tested again. The count says where to look."),
        ("p", "The count says nothing about whether a dependency is needed. Fowler's "
              "separation is a design rule, not a measurement: he applies it as soon as a "
              "model has any nonvisual logic, and the lab cannot tell you that yours does. "
              "What it can show is the shape the rule produces. A change below the "
              "presentation stops at the presentation."),
        ("h3", "Exercise"),
        ("code", _lines(CHECKOUT_DEPS)),
        ("p", "Each line is one dependency of a small shop, `dependent, dependency`. The "
              "`widgets` library draws form controls. Say by hand which classes a change to "
              "`widgets` reaches directly and which it reaches in all. Then remove the first "
              "record, so that `basket` no longer knows about widgets, and count again. You "
              "can paste the records into the lab afterwards to check."),
        ("p", "Chapter 4 has two ways to write the input controller. The next lesson, Page "
              "Controller, reads the first of them, one controller for each page."),
    ],
    "lab": ("cckit", {
        "mode": "deps",
        "view": "ripple",
        "preset": "model-knows-html",
        "presets": [
            {"id": "model-knows-html",
             "label": "The model formats itself with the HTML library (illustrative)",
             "edges": "concert, html; concertpage, concert; concertreport, concert",
             "changed": "html",
             "expect": {"dgDirect": "1: concert",
                        "dgAffected": "3: concert, concertpage, concertreport"}},
            {"id": "separated",
             "label": "Only the page uses the HTML library",
             "edges": "concertpage, concert; concertpage, html; concertreport, concert",
             "changed": "html",
             "expect": {"dgDirect": "1: concertpage", "dgAffected": "1: concertpage"}},
        ],
        "panel_title": "What a change to the HTML library reaches",
        "panel_intro": (
            "Each record is one dependency, written dependent, dependency. Name the class "
            "that changes; the lab lists what depends on it directly and everything the "
            "change reaches. The designs are the lesson's."
        ),
    }),
    "steps_title": "Tracing what a presentation change reaches",
    "steps_intro": "Four steps, the last of them on a class of your own.",
    "steps": [
        ("Write the dependencies down",
         "For each class, write one record for each class it uses, dependent first. A model "
         "that calls an HTML routine gets a record for the HTML library."),
        ("Find the direct dependents",
         "Name the class that changes and list every class with a record pointing at it. "
         "Those are reached directly."),
        ("Follow the records backwards",
         "For each class reached, list the classes that depend on it, and repeat until "
         "nothing new appears. Do not count the changed class itself."),
        ("Check a model of your own",
         "Take one model class in a system you know and read its imports. Write down "
         "anything from the presentation layer it uses, such as an HTML, template or "
         "widget library, and name the one class that should hold that use instead."),
    ],
    "worked": {
        "title": "The separated design, by hand",
        "intro": [
            "Take the preset <code>separated</code> and change `html`.",
        ],
        "lines": [
            "records: concertpage uses concert and html",
            "records: concertreport uses concert",
            "who uses html? concertpage only",
            "direct: 1, concertpage",
            "who uses concertpage? nobody",
            "reached in all: 1, concertpage",
        ],
        "after": [
            "The model and the report are untouched because neither uses the library. "
            "Add the record `concert, html` and both come into the count, which is what "
            "<code>model-knows-html</code> shows.",
        ],
    },
    "quiz_title": "Dependencies and the chapter's claims",
    "quiz": [
        {"q": "Take the exercise's four records and change `widgets`. What does a change to "
              "`widgets` reach directly, and in all?",
         "a": ["Directly 1: basket; in all 3: basket, basketapi, checkoutpage",
               "Directly 2: basket, checkoutpage; in all 2: basket, checkoutpage",
               "Directly 2: basket, checkoutpage; in all 4: basket, basketapi, checkoutpage, widgets",
               "Directly 2: basket, checkoutpage; in all 3: basket, basketapi, checkoutpage"],
         "c": 3,
         "why": "`basket` and `checkoutpage` each have a record pointing at `widgets`, so 2 "
                "directly. `basketapi` uses `basket`, so the change reaches it through the "
                "model: 3 in all. The changed class is never in the list. Remove `basket, "
                "widgets` and only `checkoutpage` is reached, 1: checkoutpage both ways; "
                "the API that has nothing to do with form controls drops out."},
        {"q": "Which dependency does Model View Controller, as Chapter 14 describes it, rule "
              "out?",
         "a": ["The model depending on the presentation above it",
               "The view depending on the model it displays",
               "The controller depending on the model it updates",
               "The controller depending on the view it updates"],
         "c": 0,
         "why": "Fowler's key point is the direction: the presentation, view and controller, "
                "depends on the model, and the model does not depend on the presentation. "
                "The other three are dependencies the pattern expects."},
        {"q": "What does Chapter 14 say about separating the view from the controller?",
         "a": ["It is the more important of the two separations Fowler finds in MVC",
               "Every version of Smalltalk made it, and later web frameworks dropped it",
               "It is less important, rarely done in rich clients, common on the web",
               "It is the separation the Application Controller pattern describes in full"],
         "c": 2,
         "why": "Fowler calls it less important and notes that almost every version of "
                "Smalltalk did not make it; it came back with web front ends, which give the "
                "controller an object of its own. An Application Controller, Fowler says, is a "
                "different thing from an MVC controller."},
        {"q": "Records `a, b` and `b, c`, with `c` changed. What does the lab print?",
         "a": ["Directly 1: b; in all 1: b",
               "Directly 1: b; in all 2: a, b",
               "Directly 2: a, b; in all 2: a, b",
               "Directly 1: b; in all 3: a, b, c"],
         "c": 1,
         "why": "Only `b` has a record pointing at `c`, so 1 directly. `a` uses `b`, so "
                "following the records backwards reaches it: 2 in all. The changed class "
                "itself is never listed."},
    ],
    "mistakes": [
        ("Taking Model View Controller to be three folders",
         "On this reading the pattern is satisfied once the code is filed as models, views "
         "and controllers. Fowler's point is which way the dependencies run: the "
         "presentation uses the model, and the model never uses the presentation. A "
         "model in the models folder that calls an HTML routine breaks the pattern however "
         "it is filed. On the lesson's illustration, the report, which has nothing to do "
         "with HTML, is reached by an HTML change only because the model knew about HTML: "
         "3 classes reached instead of 1."),
        ("Putting the business logic in the controller",
         "The controller is the part people write first, so the rules end up there. In "
         "Chapter 4's round trip the input controller handles the request, hands the "
         "business logic to the model and picks the view; where the decisions get "
         "complicated, Fowler gives them to helper objects. The logic belongs in the model, "
         "a Domain Model or a Transaction Script, so that it can be tested and shared by "
         "every presentation."),
        ("Thinking the view-controller split is the point",
         "It is the separation people notice, because web frameworks make it. Fowler ranks "
         "it second and calls it less important; the separation he will not give up, "
         "except in a very simple system, is the model's from the presentation."),
    ],
    "standard": (
        "Finish when you can trace what a presentation change reaches.",
        "Given the dependencies of a model, two presentations and an HTML library, list "
        "what a change to the library reaches directly and in all; then redraw the design "
        "with the model independent of the library and list it again."
    ),
    "note": (
        "The lab follows the dependencies you state; it cannot find them in code, and it "
        "counts a class reached through one call the same as one reached through forty. "
        "It does not model the rich-client case Fowler raises, where several views of one "
        "model must refresh together and an observer keeps the model free of them. Whether "
        "a dependency belongs is the design question; the count shows how far a change "
        "travels if it does."
    ),
}

# ---------------------------------------------------------------- 02
# Chapter 4, Input Controller Patterns, PDF p. 70 of the operator's copy;
# Chapter 14, Page Controller, pp. 302-311 (examples from p. 303, pointed
# to). Quote: PDF p. 65 of the operator's copy (Chapter 4's opening), 26
# words, ea_quotes.py OK. Lesson total: 26 words.
# One controller per action (p. 70; p. 302); the two responsibilities and
# the helper (p. 70; p. 302); the three responsibilities, model data with no
# connection to the request (p. 303); mixing pages and scripts (p. 303);
# When to Use It (p. 303).
PAGE_CONTROLLER = {
    "slug": "page-controller",
    "title": "Page Controller",
    "module": "Chapter 14 · Web Presentation Patterns",
    "one_line": "A Page Controller handles the request for one page or action, and the decisions it makes about which view to show can move to a helper where they are tested without a web server.",
    "summary": (
        "Chapter 4's Input Controller Patterns and Chapter 14's Page Controller: one input "
        "controller for each page, or more precisely for each action, which decodes the "
        "request, asks the model and picks the view. Count the decision points in a page "
        "controller, and see where they go when the choice of view moves to a helper and "
        "the model keeps only its own predicates."
    ),
    "key": [
        "one input controller per action",
        "decode, ask the model, pick a view",
        "the model never sees the request",
        "decision points: 1, plus each branch",
        "a helper decides; a page forwards",
    ],
    "key_label": "Page Controller in five lines",
    "concepts_intro": (
        "Three ideas carry the section and the pattern. The second is the one the rest of "
        "the course keeps returning to."
    ),
    "concepts": [
        ("An action",
         "A button or a link the user can press. Fowler's more precise version of Page "
         "Controller has a controller for each action rather than each page, because one "
         "link may lead to different pages depending on some condition."),
        ("A helper object",
         "An ordinary class that a page or controller calls to do its logic, so that the "
         "page itself holds none. Chapter 14 uses helpers for the controller's decisions "
         "here and for the template's in Template View."),
        ("A decision point",
         "A place where the code can go one of two ways. The lab counts them by a stated "
         "rule taken from Code Complete: one, plus one for each if, while, for, case and "
         "each `&&` and `||`. Fowler gives no count; the rule is a way of seeing where the "
         "controller's choices are."),
    ],
    "read_title": "The section and the pattern, then the count",
    "read_intro": (
        "Read Input Controller Patterns in Chapter 4 and Page Controller in Chapter 14 in "
        "your own copy first. The lesson sets out the section's argument, describes the "
        "pattern, and then counts the decisions in a page controller before and after its "
        "choice of view moves to a helper."
    ),
    "body": [
        ("p", "&ldquo;Things get a lot more messy when you have to make decisions based on "
              "the input, such as different display formats for classical and jazz "
              "albums.&rdquo; Fowler writes that of server pages in Chapter 4's opening, and "
              "you may have seen it happen to a controller of your own: it began by finding "
              "one record and showing it, and grew a branch for every case the page had to "
              "handle. This lesson reads Input Controller Patterns in Chapter 4 and Page "
              "Controller in Chapter 14. Read them in your own copy first."),
        ("p", "Input Controller Patterns is a short section with one argument. The most "
              "common design, Fowler says, gives every page on the site its own input "
              "controller. In the simplest case that controller is the server page itself, "
              "playing view and controller at once; often it is easier to split it out as a "
              "separate object that creates the models and picks the view. The match is not "
              "quite one controller to one page, though. The more precise thought, he says, "
              "is a controller for each action, a button or a link, because a link can lead "
              "to different pages depending on some condition."),
        ("p", "Any input controller, the section goes on, does two things: it deals with the "
              "HTTP request, and it decides what should happen as a result. It often makes sense to "
              "separate them, with a server page handling the request and a helper object "
              "deciding. Front Controller, the next lesson, takes that separation further."),
        ("p", "Page Controller, in Chapter 14, is read as a pattern. It starts from the "
              "simplest model of the web, one path leading to one file, and gives each "
              "logical page of the site its own controller, either a script or a server "
              "page. A server page that is also the controller works well as a view and "
              "less well as a controller: once there is logic in reading the request or "
              "choosing the view, the page fills with awkward scriptlets. Fowler's two ways "
              "out are a helper object that the page calls first to handle the logic, and a "
              "script that is the controller and forwards to a server page for the view."),
        ("p", "The pattern gives the controller three jobs. It decodes the URL and any form "
              "data. It creates and calls the model objects, passing them all the data they "
              "need from the request so that the model needs no connection to the request "
              "itself. And it decides which view shows the result and forwards the model's "
              "information to it. A controller need not be one class; helpers are a good "
              "place for code several controllers would otherwise repeat. Fowler also sees "
              "no reason to handle every URL the same way: a URL with little logic is best "
              "a server page, one with more a script, and teams that insist on one or the "
              "other end up, he says, with scriptlet-laden pages or with many trivial "
              "pass-through scripts."),
        ("p", "When to use it is set against Front Controller. Page Controller is the more "
              "familiar of the two and gives a natural structure, one action to one page or "
              "script, and it works particularly well where most of the controller logic is "
              "simple; there, Fowler says, a Front Controller adds a lot of overhead. The "
              "two mix without much trouble, and a site being moved from one to the other "
              "often has both. The pattern's three examples, a servlet controller with a JSP "
              "view, a JSP as the handler, and a C# page handler with a code-behind, are "
              "worth reading in the book."),
        ("p", "Now the code, written for the lesson. `Request` and `Response` stand for a "
              "servlet-like API: `req.param` reads a parameter and `res.forward` hands the "
              "response to a view with the object it should show. The controller below "
              "finds a concert on line 3 and spends lines 4 to 12 choosing one of four "
              "views."),
        ("code", _lines(CONCERT_PAGE)),
        ("p", "The lab counts decision points by a stated rule: one, plus one for each "
              "`if`, `while`, `for` and `case`, and one for each `&&` and `||`. An `else` "
              "adds nothing; an `else if` is an `if`. On the preset "
              "<code>concert-page</code> it prints 5, broken down as `1 + if 3 + && 1`. Its "
              "other tiles are a band, 0–5, which is McConnell's from Code Complete and not "
              "Fowler's (Fowler gives no count); the deepest nesting, 1, counting the blocks "
              "inside the routine's own braces; and the first line at that depth, line 5."),
        ("p", "Leave aside the 1 every routine starts with. Of the four decisions, the test "
              "`c == null` on line 4 is about the request: was there such a concert? "
              "`isSoldOut`, `isSeated` and `hasSeatMap` are questions the concert answers; "
              "and using their answers to pick one of four pages is presentation: which "
              "view to show. Move that choice "
              "to a helper on the presentation side and the controller becomes the "
              "listing below."),
        ("code", _lines(CONCERT_PAGE_SPLIT)),
        ("p", "On <code>concert-page-split</code> the lab prints 1, broken down as 1, with "
              "a deepest nesting of 0, first reached on line 4. The four branches have not "
              "disappeared. They have moved to `ConcertPageHelper.viewFor`, a helper on the "
              "presentation side, which holds the same tests and returns the page's name. "
              "The model keeps only its domain predicates and never names a page, as the "
              "last lesson requires. What the move buys is a place to test the decisions: "
              "call `viewFor` with a sold-out concert and check the name it returns, with "
              "no request and no web server."),
        ("h3", "Exercise"),
        ("code", _lines(BOOKING_PAGE)),
        ("p", "This controller changes the number of seats on a booking. Count its decision "
              "points by the lab's rule, with the breakdown. Then sort them: which are about "
              "the request, which are rules about a booking that the `Booking` class should "
              "answer as predicates, and which choose the page. Write the helper method "
              "that would choose the page."),
        ("p", "A page controller repeats what every page must do first. The next lesson, "
              "Front Controller, reads the pattern that puts those things in one handler."),
    ],
    "lab": ("cckit", {
        "mode": "code",
        "view": "complexity",
        "bands": [5, 10],
        "book": "other",
        "preset": "concert-page",
        "presets": [
            {"id": "concert-page",
             "label": "A page controller choosing among four views",
             "code": CONCERT_PAGE,
             "expect": {"coDecisions": "5", "coBreakdown": "1 + if 3 + && 1"}},
            {"id": "concert-page-split",
             "label": "The same controller, with the choice of view in a helper",
             "code": CONCERT_PAGE_SPLIT,
             "expect": {"coDecisions": "1", "coBreakdown": "1"}},
        ],
        "panel_title": "The decisions a page controller holds",
        "panel_intro": (
            "The lab counts decision points by a stated rule: one, plus one for each if, "
            "while, for and case, and for each conditional-and or conditional-or "
            "operator. The bands beside the count are McConnell's, from "
            "Code Complete; Fowler gives no count. The listings are the lesson's."
        ),
    }),
    "steps_title": "Counting a controller's decisions",
    "steps_intro": "Four steps, the last of them on a controller of your own.",
    "steps": [
        ("Count by the rule",
         "Start at one. Add one for each if, while, for and case, and one for each `&&` "
         "and `||`. An `else` adds nothing."),
        ("Sort each decision",
         "Mark each test as about the request (is the input there, is it well formed), "
         "about the domain (a rule the model should answer) or about the view (which page "
         "to show)."),
        ("Move the view's decisions",
         "Write a helper method that takes the model object and returns the view's name, "
         "and leave the controller one call to it. Give each domain rule to the model as a "
         "predicate."),
        ("Count a controller of your own",
         "Take one controller in a system you know and count its decision points by the "
         "rule. Write the figure, and mark each decision that is about the domain rather "
         "than the request."),
    ],
    "worked": {
        "title": "The concert page, by the rule",
        "intro": [
            "Take the preset <code>concert-page</code> and count line by line.",
        ],
        "lines": [
            "start: 1",
            "line 4, if the concert is missing: 2",
            "line 6, else if it is sold out: 3",
            "line 8, else if it is seated: 4",
            "line 8, and it has a seat map: 5",
            "line 10, else: adds nothing, still 5",
        ],
        "after": [
            "The breakdown is `1 + if 3 + && 1`. Of the four decisions, one is about the "
            "request; the other three ask the model's predicates, and using the answers "
            "to pick a page is the helper's work, which is why <code>concert-page-split</code> prints 1.",
        ],
    },
    "quiz_title": "Decisions and the section's claims",
    "quiz": [
        {"q": "Count the exercise's booking controller by the lab's rule: one, plus one for "
              "each `if`, `while`, `for`, `case`, `&&` and `||`. How many decision points, and what is "
              "the breakdown?",
         "a": ["6: if 3 + && 1 + || 2",
               "7: 1 + if 3 + && 1 + || 2",
               "8: 1 + if 3 + && 1 + || 2 + else 1",
               "5: 1 + if 3 + && 1"],
         "c": 1,
         "why": "Start at 1. Line 4 is an `if` with one `||`, line 9 an `if` with one `||`, "
                "and line 11 an `else if` with one `&&`: 1 + 3 + 1 + 2 = 7. The rule starts at one, and "
                "else adds nothing; the `!` is not a connective. Sorted, the null checks "
                "on line 4 are about the request; the seat range (the limit of eight seats is a "
                "rule about bookings, not about the form) and the rule that a paid, "
                "non-refundable booking is locked belong to `Booking` as predicates; and "
                "the choice among booking, locked and confirm pages belongs to the helper."},
        {"q": "By the same rule, how many decision points does a routine hold whose only "
              "branches are `if (p && q)`, then `else if (r)`, then a final `else`?",
         "a": ["3: if 2 + && 1",
               "5: 1 + if 2 + && 1 + else 1",
               "6: 1 + if 3 + && 1 + else 1",
               "4: 1 + if 2 + && 1"],
         "c": 3,
         "why": "1 to start, plus 2 for the if and the else if, plus 1 for the `&&`: 4. The "
                "final else adds nothing."},
        {"q": "What does Chapter 4 call the more precise version of one Page Controller per "
              "page?",
         "a": ["One for each action, such as a button or a link the user presses",
               "One for each view the site can show to a user",
               "One for each server page file deployed on the site",
               "One for each domain object the page displays"],
         "c": 0,
         "why": "Most actions correspond to pages, but a link may lead to different pages "
                "depending on a condition, so Fowler's more precise thought is a controller "
                "for each action."},
        {"q": "Page Controller passes the model all the data it needs from the request. Why, "
              "by the pattern's account?",
         "a": ["So that the request can be cached between the model's calls",
               "So that the view does not have to call the model itself",
               "So that the model needs no connection to the request",
               "So that the model can choose which view shows the result"],
         "c": 2,
         "why": "Chapter 14 lists it as the controller's second job: create and invoke the "
                "model objects with all the relevant data, so that they need no connection "
                "to the request. Choosing the view is the controller's third job, not the "
                "model's."},
    ],
    "mistakes": [
        ("Taking a page controller to be a page",
         "The name suggests one controller for each page, and most of the time that is "
         "what you get. Fowler's more precise version is one controller for each action, a "
         "button or a link, because one link may lead to two or more pages, chosen by "
         "a condition. The concert page's controller is an example: one "
         "action, four pages."),
        ("Thinking that moving a decision out removes it",
         "<code>concert-page-split</code> prints 1, and it is tempting to read that as four "
         "decisions gone. They are in `ConcertPageHelper.viewFor`, which the lab is not "
         "shown. What moved is where they can be tested: a helper takes a concert and "
         "returns a page's name, with no request and no web server."),
        ("Handling every URL the same way",
         "Consistency looks like a virtue, so some teams make every URL a server page or "
         "every URL a script. Fowler says the advantage is usually offset by the cost: "
         "server pages full of scriptlets, or many trivial scripts that only pass the "
         "request through. His advice is a server page where there is little controller "
         "logic and a script where there is more."),
    ],
    "standard": (
        "Finish when you can count and place a controller's decisions.",
        "Given a page controller, count its decision points by the rule, with the "
        "breakdown, and write the helper method that picks the view from the model's "
        "predicates."
    ),
    "note": (
        "The lab counts the listing it is given; the helper the split controller calls is "
        "not in it, so the drop from 5 to 1 is a move and not a saving. The rule and the "
        "bands are McConnell's, not Fowler's, and a count does not say whether a "
        "controller is too complicated. Sorting the decisions into request, domain and "
        "view is the reader's work; the lab cannot tell a domain rule from a page choice."
    ),
}

# ---------------------------------------------------------------- 03
# Chapter 4, Input Controller Patterns, PDF p. 70 of the operator's copy;
# Chapter 14, Front Controller, pp. 312-317 (example from p. 314, pointed
# to). Quote: PDF p. 314 of the operator's copy, 21 words, ea_quotes.py OK.
# Lesson total: 21 words.
# The common behaviour and the two parts (p. 312); static and dynamic
# dispatch, Intercepting Filter as the book cites Alur, Crupi and Malks,
# Rob Mee's two-stage handler, commands choose the view (p. 313); the four
# advantages and the superclass answer (p. 314).
FRONT_CONTROLLER = {
    "slug": "front-controller",
    "title": "Front Controller",
    "module": "Chapter 14 · Web Presentation Patterns",
    "one_line": "A Front Controller sends every request through one handler that does the common work and passes the rest to a command, and Fowler holds that it needs real advantages to be worth its extra complexity.",
    "summary": (
        "Chapter 14's Front Controller, read with Chapter 4's Input Controller Patterns: "
        "one web handler for every request, which does what all requests share and "
        "dispatches to a command for each action. Count the lines two page controllers "
        "repeat, then remove them twice, with a superclass and with one handler, and see "
        "why the count cannot choose between the two."
    ),
    "key": [
        "one handler; a command per action",
        "handler: the common work, then dispatch",
        "commands choose the view",
        "a superclass removes the copies too",
        "repeated: identical lines, two or more",
    ],
    "key_label": "Front Controller in five lines",
    "concepts_intro": (
        "Three terms carry the pattern. The third is the book's citation of another "
        "catalogue, and Fowler recommends it alongside."
    ),
    "concepts": [
        ("Web handler",
         "The one object the web server hands every request to. It reads just enough of the "
         "URL and the request to decide which action is wanted, and then passes the request "
         "to a command. It renders no page itself: once it has chosen the command, the "
         "command chooses the view."),
        ("Command",
         "An object for one kind of request, with a method that carries the action out. The "
         "commands are part of the controller and choose the view; the handler only chooses "
         "the command. The handler can pick it statically, by conditional logic on the URL, "
         "or dynamically, by creating a command class named in the URL or a configuration "
         "file."),
        ("Intercepting Filter",
         "A decorator, an object that wraps another and adds behaviour before or after it, "
         "placed around the handler. Filters chain, so authentication, logging and locale "
         "can each be one filter set up at configuration time. The book cites the pattern "
         "from Alur, Crupi and Malks's Core J2EE Patterns (2001)."),
    ],
    "read_title": "The pattern and its reasons, then the count",
    "read_intro": (
        "Read Front Controller in Chapter 14, with Chapter 4's Input Controller Patterns "
        "beside it, in your own copy first. The lesson describes the pattern, sets out "
        "Fowler's reasons for and against it, and then counts the lines two page "
        "controllers share in three designs."
    ),
    "body": [
        ("p", "&ldquo;Only one Front Controller has to be configured into the Web server; "
              "the Web handler does the rest of the dispatching.&rdquo; That is the first "
              "advantage Fowler lists for Front Controller in Chapter 14, and he lists them "
              "because he thinks the pattern needs them: it is a more complicated design "
              "than Page Controller. Where should the code that every request needs live, "
              "if not in every page? This lesson reads his answer. Read Front Controller in "
              "your own copy first, with Input Controller Patterns from Chapter 4."),
        ("p", "Chapter 4's argument was that an input controller has two jobs: dealing with "
              "the request, and deciding what should come of it. Front Controller, it says, "
              "pulls the two further apart: a single object receives every request, reads "
              "the URL to tell which kind it is, and makes another object to carry it out. "
              "All the HTTP handling is then in one place, and the web server "
              "need not be reconfigured whenever the site's set of actions changes."),
        ("p", "The pattern, read as a tool, begins with a problem. A complex site does "
              "similar things on every request, such as security, internationalisation and "
              "particular views for certain users, and if input-controller behaviour is "
              "spread across many objects, much of it ends up duplicated and is hard to "
              "change at run time. Front Controller puts every request through one handler "
              "object, which does the common work and then dispatches to a command for "
              "the part particular to the request. The handler is a class, not a server "
              "page, because it renders no page of its own; the commands need not know about the "
              "web at all, though they are often passed the request."),
        ("p", "The handler can choose its command statically, by parsing the URL with "
              "conditional logic, which makes the logic plain to read, lets the compiler "
              "check the dispatch and leaves the URLs free in their shape; or dynamically, by taking part "
              "of the URL and creating a command class from it, which lets you add commands "
              "without changing the handler. A useful companion, Fowler says, is Intercepting "
              "Filter, as the book cites Alur, Crupi and Malks: decorators wrapped round the "
              "handler in a chain, for authentication, logging and locale. He also tells of "
              "a variation Rob Mee showed him, a handler split in two, a thin web part that "
              "pulls the data out of the request and a dispatcher that knows nothing of the "
              "web server, so that tests can drive the dispatcher directly. Whichever way it "
              "is built, the commands choose the view; once the handler has chosen the "
              "command, it plays no further part in the request."),
        ("p", "Fowler's case for using it is a list of four advantages. Only one handler is "
              "configured into the web server, which helps where the server is awkward to "
              "configure and eases porting; with dynamic commands, new ones are added "
              "without changing anything. A new command object is created for each request, "
              "so the command classes need not be thread-safe, though you must still make sure "
              "they share no other objects, such as the model objects. And because there is "
              "one controller, decorators can be added to it at run time. The advantage "
              "most often claimed, factoring out the code page controllers duplicate, he "
              "treats more coolly: much of that, he says to be fair, a superclass Page "
              "Controller can do."),
        ("p", "That claim can be counted. The lab finds repeated code by a stated rule: it "
              "compares statement lines as text, with spacing collapsed, and reports every "
              "run of two or more consecutive lines that appears more than once. Its tiles "
              "are the repeated blocks, the lines in all the copies, and where they are. "
              "The preset <code>pages-repeat</code> is two page controllers written for the "
              "lesson, and the lab prints 1 block, 6 lines, at lines 2–4 and lines 9–11: "
              "each page reads the session's user, redirects to the login page if there is "
              "none, and writes an audit record, before it does its own work."),
        ("code", _lines(PAGES_REPEAT)),
        ("p", "In <code>page-superclass</code> the three lines run once, in `SecurePage`, a "
              "Layer Supertype from the first course: an abstract superclass that does the "
              "shared steps and then calls `show`, which each page overrides. The lab reads "
              "the whole listing, all three classes, and prints 0 blocks, 0 lines, none."),
        ("code", _lines(PAGES_SUPERCLASS)),
        ("p", "In <code>front-handler</code> one handler looks the request's path up in a "
              "table of commands, sends a visitor with no session to the login page unless "
              "the command is public, writes the audit record, and runs the command; each "
              "page's part would be a command's `run`. Again 0, 0, none. The pages under "
              "`SecurePage` never needed that exemption, because the login page simply does "
              "not extend it; a handler that sees every request has to be told which ones "
              "are open."),
        ("code", _lines(FRONT_HANDLER)),
        ("p", "The count cannot choose between the second and third designs: both reach 0. "
              "The handler's listing is a single routine with its commands left out, so its "
              "0 is certain; the commands, each one page's `forward`, differ as the pages' "
              "last lines did. Removing duplicated lines is a weak reason on its own to "
              "prefer a Front Controller, because a superclass can do much of it too; the "
              "reasons Fowler gives for one handler are the one configuration, the dynamic "
              "commands, the fresh command for each request, and the decorators, and none "
              "of them is something a count of repeated lines can see. The pattern's own "
              "example, a simple display with dynamic commands, is worth reading in the "
              "book."),
        ("h3", "Exercise"),
        ("code", _lines(REPORTS_REPEAT)),
        ("p", "Two report pages, written for the lesson. Mark by hand the lines that repeat, "
              "by the lab's rule, and give their line numbers and how many lines the copies "
              "hold. Then say what a superclass or a front handler would do with them."),
        ("p", "Controllers decide which view to show. The next lesson, Template View and "
              "Transform View, reads the two ways to write the view."),
    ],
    "lab": ("cckit", {
        "mode": "code",
        "view": "dupes",
        "min_run": 2,
        "preset": "pages-repeat",
        "presets": [
            {"id": "pages-repeat",
             "label": "Two page controllers that check the session and audit",
             "code": PAGES_REPEAT,
             "expect": {"coDupBlocks": "1", "coDupLines": "6",
                        "coDupWhere": "lines 2–4 and lines 9–11"}},
            {"id": "page-superclass",
             "label": "The same pages under a SecurePage superclass",
             "code": PAGES_SUPERCLASS,
             "expect": {"coDupBlocks": "0", "coDupLines": "0", "coDupWhere": "none"}},
            {"id": "front-handler",
             "label": "One handler for every request, dispatching to a command",
             "code": FRONT_HANDLER,
             "expect": {"coDupBlocks": "0", "coDupLines": "0", "coDupWhere": "none"}},
        ],
        "panel_title": "What page controllers repeat",
        "panel_intro": (
            "The lab compares statement lines as text, with spacing collapsed, and reports "
            "each run of two or more lines that appears more than once. Lines that differ "
            "only in a name are not the same text, so the lab does not see them. The "
            "listings are the lesson's."
        ),
    }),
    "steps_title": "Finding what controllers repeat",
    "steps_intro": "Four steps, the last of them on controllers of your own.",
    "steps": [
        ("Line the controllers up",
         "Put the controllers one under another and read their first lines side by side. "
         "The common work usually comes before each page's own."),
        ("Mark identical runs",
         "Mark every run of two or more lines that is the same text in both, spacing "
         "aside. A line that differs only in a variable's name is not identical."),
        ("Remove them once",
         "Write the superclass whose method runs the marked lines and then calls the "
         "page's own step. Then ask whether one handler adds anything you need: a single "
         "configuration, commands added without changes, a fresh command per request, "
         "decorators."),
        ("Count controllers of your own",
         "Take the first lines of three controllers in a system you know. Count the lines "
         "they share, write the figure, and say in one sentence where those lines could "
         "run once."),
    ],
    "worked": {
        "title": "Two page controllers, line by line",
        "intro": [
            "Take the preset <code>pages-repeat</code> and compare the two routines.",
        ],
        "lines": [
            "lines 2 and 9: read the user from the session",
            "lines 3 and 10: no user, so go to the login page",
            "lines 4 and 11: write the audit record",
            "lines 5 and 12: differ, an order and an invoice",
            "one block of 3 lines, in 2 copies: 6 lines",
        ],
        "after": [
            "The session check, the login redirect and the audit are three lines in each "
            "page. A third page would make them nine, and a change to the audit would be "
            "three edits. <code>page-superclass</code> and <code>front-handler</code> "
            "both bring them to one copy.",
        ],
    },
    "quiz_title": "Repeated lines and the pattern's reasons",
    "quiz": [
        {"q": "In the exercise's two report pages, which lines repeat by the lab's rule "
              "(identical statement lines, in runs of two or more), and how many lines do "
              "the copies hold?",
         "a": ["Lines 2–4 and lines 9–11: 6 lines in the two copies",
               "Lines 2–3 and lines 9–10: 2 lines, one copy counted",
               "Lines 2–3 and lines 9–10: 4 lines in the copies",
               "Lines 1–3 and lines 8–10: 6 lines, headers included"],
         "c": 2,
         "why": "Lines 2 and 3, the Cache-Control header and the locale, are the same text as "
                "lines 9 and 10: one block of 2 lines in 2 copies, 4 lines. Line 4 differs "
                "from line 11 (`sales` against `stock`), and the headers on lines 1 and 8 "
                "name different routines. A superclass or a front handler would set the "
                "header and the locale once."},
        {"q": "Which of these does Fowler give as an advantage of Front Controller?",
         "a": ["It is a simpler design than Page Controller, with less to configure",
               "A fresh command per request, so commands need not be thread-safe",
               "It is the only way to remove the code page controllers duplicate",
               "The handler chooses the view for every request it receives"],
         "c": 1,
         "why": "Chapter 14 lists one configured handler, dynamic commands, a fresh command "
                "per request (no thread-safety worries for the commands), and decorators. "
                "Fowler calls the pattern more complicated than Page Controller, grants that "
                "a superclass Page Controller removes much of the duplication, and gives "
                "the choice of view to the commands."},
        {"q": "What does a static choice of command offer that a dynamic one does not, by "
              "Chapter 14's account?",
         "a": ["Adding commands without changing the handler",
               "A properties file binding URLs to command classes",
               "A new command object for each request",
               "Compile-time checking of which command each URL reaches"],
         "c": 3,
         "why": "The static version parses the URL with conditional logic, which keeps "
                "the logic in plain view, lets the compiler check the dispatch, and leaves "
                "the URLs free in their shape. Adding commands without changing the handler, with or without a "
                "properties file, is the dynamic version's; a fresh command per request "
                "holds either way."},
        {"q": "The first routine opens with `User u = sessions.user(req);` and a null "
              "check on `u`; the second opens with the same two lines but calls the "
              "variable `user`. What does the lab report for those opening lines?",
         "a": ["Nothing: the lines are not the same text at all",
               "1 block, 4 lines: the two opening lines in each routine",
               "1 block, 2 lines: the null checks, once in each routine",
               "2 blocks, 4 lines: one block for each opening line"],
         "c": 0,
         "why": "The lab compares lines as text, with only spacing collapsed. `User u` and "
                "`User user` differ, so the lines do not match, and the repetition is wider "
                "than the count."},
    ],
    "mistakes": [
        ("Taking a Front Controller for one huge controller",
         "A single object for every request sounds like everything in one place. Fowler's "
         "Front Controller is one handler and many small commands. The handler does only "
         "the work common to requests and then chooses a command; the command does the "
         "action and chooses the view. In <code>front-handler</code> the handler's body is "
         "five statements, and the login check is skipped for a command that is public."),
        ("Thinking only a Front Controller removes what pages repeat",
         "Duplicated code is the reason most often given for the pattern. Fowler grants "
         "that a superclass Page Controller does much of that too, and the "
         "<code>page-superclass</code> preset brings the repeated lines to 0, as the front "
         "handler does. His reasons for one handler are the single configuration, dynamic "
         "commands, a fresh command for each request, and decorators."),
        ("Letting the handler pick the view",
         "If the handler sees every request, it seems the natural place to choose every "
         "response. Chapter 14 says the opposite: the commands are part of the controller "
         "and choose the view, and once the handler has chosen the command it plays no "
         "further part in the request."),
    ],
    "standard": (
        "Finish when you can find and remove what controllers repeat.",
        "Given two page controllers, mark the repeated lines and give their line numbers, "
        "write the superclass that runs them once, and name what a front handler offers "
        "beyond that."
    ),
    "note": (
        "The lab sees identical lines only, so a repetition with different names is not "
        "counted, and it cannot tell code that should be shared from code that merely "
        "looks alike. Two of the three designs reach 0, and the count has nothing to say "
        "about the choice between them; Fowler's four reasons are about configuration, "
        "run time and threads, which no listing shows."
    ),
}

# ---------------------------------------------------------------- 04
# Chapter 4, View Patterns, PDF pp. 67-69 of the operator's copy; Chapter 14,
# Template View, pp. 318-326, and Transform View, pp. 327-330 (examples
# pointed to). Quote: PDF p. 67 of the operator's copy, 21 words,
# ea_quotes.py OK. Lesson total: 21 words.
# Markers, scriptlets, the helper object, conditional display, iteration
# (pp. 318-320); the two weaknesses (p. 321); Transform View's element by
# element walk, any language, XSLT (p. 327); When to Use It (p. 328).
# This course's one modern aside (PLAN section F.3) is in the note.
TEMPLATE_AND_TRANSFORM_VIEW = {
    "slug": "template-and-transform-view",
    "title": "Template View and Transform View",
    "module": "Chapter 14 · Web Presentation Patterns",
    "one_line": "Template View writes the page and marks where data goes, Transform View walks the data and writes the page, and in either the logic belongs in code outside the page.",
    "summary": (
        "Chapter 4's View Patterns and Chapter 14's two single-stage views: Template View, "
        "markers in the page's own structure with a helper holding the logic, and "
        "Transform View, a program that walks the domain data element by element. Count "
        "the decisions in a piece of HTML-building code, and see what is left when a "
        "helper takes them and the template only asks."
    ),
    "key": [
        "template: the page, with markers in it",
        "transform: walk the data, write the page",
        "a helper holds the logic of the page",
        "a condition: one Boolean of the helper",
        "moved decisions still count somewhere",
    ],
    "key_label": "The two views in five lines",
    "concepts_intro": (
        "Three terms carry the section and the two patterns. The first two are the "
        "patterns' own; the third is how Fowler keeps the first one clean."
    ),
    "concepts": [
        ("Marker",
         "A tag or a piece of special text in an HTML page that the template engine "
         "replaces with a computed value when the page is served. A Template View is a page "
         "written as HTML with markers in it."),
        ("Scriptlet",
         "Program code embedded in a server page, as ASP, JSP and PHP allow. Fowler calls "
         "the feature a big problem: a page full of scriptlets cannot be edited by a "
         "designer, is a poor module for a program, and makes it easy to put domain logic "
         "in the page."),
        ("Transform",
         "A routine for one kind of input element that writes the HTML for it. A Transform "
         "View is a set of such transforms and a loop that walks the domain data, finds the "
         "transform for each element and calls it. XSLT is the usual language, but not the "
         "only one."),
    ],
    "read_title": "The section and the two patterns, then the count",
    "read_intro": (
        "Read View Patterns in Chapter 4, then Template View and Transform View in "
        "Chapter 14, in your own copy first. The lesson sets out the section's two "
        "choices, describes each pattern and its trade-offs, and then counts the "
        "decisions in a row of HTML before and after a helper takes them."
    ),
    "body": [
        ("p", "&ldquo;This clearly provides a lot of power and flexibility; sadly, it also "
              "leads to very messy code that's difficult to maintain.&rdquo; Fowler is "
              "writing in Chapter 4 about server pages, which let a page hold a complete "
              "programming language. You may know the result from a template of your own "
              "that began as HTML with a few markers and now has a condition for every "
              "special case. This lesson reads View Patterns in Chapter 4, and Template "
              "View and Transform View in Chapter 14. Read them in your own copy first."),
        ("p", "View Patterns sets out the choices. There are three view patterns, Fowler "
              "says, and they give two decisions: Template View or Transform View, and "
              "either one in a single stage or as a Two Step View, which is the next "
              "lesson. Template View lays the presentation out as the page itself, with "
              "markers where the changing content goes; Transform View uses a "
              "transform style of program, usually XSLT, applied by the input controller to "
              "XML taken from the model. A procedural script can be written in either style "
              "or a mix of the two. If you use server pages, the section warns, it takes "
              "real discipline to keep the program out of the page, often with a "
              "helper object."),
        ("p", "Template View, read as a pattern, starts from the difficulty of writing a "
              "program that produces a page of HTML, and the ease of writing a static page "
              "in an editor. So write the page as a static page, with markers that are "
              "replaced by computed results when it is served. The page can then be laid "
              "out, often in a visual editor, by people who are not programmers. Server "
              "pages go further and allow scriptlets, and in Fowler's view that is a big "
              "problem: designers can no longer edit the page, a page is a poor module for "
              "a program, and domain logic creeps in and gets duplicated across pages. The "
              "worst code he had seen in recent years, he says, was server page code."),
        ("p", "His answer is a helper object for each page, a regular class that holds all "
              "the real programming logic, so that the page holds only calls to it. Two "
              "cases are hard. Conditional display tempts you towards a general conditional "
              "tag, which turns the template into a programming language; Fowler calls "
              "purely conditional tags a bad smell. The helper can return an empty string "
              "when there is nothing to show, or generate the markup itself, which takes "
              "the choice of markup away from the designer; where the designer must keep "
              "it, he prefers a focused tag, and in every case a condition that asks the "
              "helper one true-or-false question. Iteration over a collection is the "
              "other hard case, and a general loop tag is hard to avoid but usually fits "
              "well enough."),
        ("p", "Template View's strength, he says, is that you compose the page by looking at "
              "its structure, which most people find easier, and which lets a graphic "
              "designer lay out the page while a programmer writes the helper. Its two "
              "weaknesses are that the usual tools make it all too easy to let complicated "
              "logic into the page, and that it is hard to test outside a web "
              "server."),
        ("p", "Transform View is organised the other way round. Where a template is "
              "organised around the output, a transform view is organised around the "
              "input: a program walks the domain data and, as it recognises each kind of "
              "element, writes out the HTML for it, and the order in which its rules are "
              "written makes no difference to the page. It can be written in any language; the "
              "dominant choice when the book was written was XSLT, a functional language "
              "with an awkward XML syntax. The choice between the two, Fowler says, comes "
              "down mostly to what the team prefers and the tools it has. A transform is "
              "easier to keep focused on rendering and easy to test without a web server; "
              "a change to the whole site's appearance can mean changing many transforms, "
              "which is where Two Step View comes in. The examples, a JSP as a view with a "
              "separate controller, an ASP.NET server page, and a simple transform, are "
              "worth reading in the book."),
        ("p", "Now the code, written for the lesson. The routine below builds one row of a "
              "concert's ticket table, and decides inline whether to mark the seats as few "
              "and whether to label them as resale. The lab reads Java, so the row stands "
              "in for a server page whose scriptlets make the same two decisions."),
        ("code", _lines(TICKET_ROW)),
        ("p", "On the preset <code>ticket-row</code> the lab prints 5 decision points, "
              "broken down as `1 + if 2 + && 1 + || 1`, by the same rule as the last two "
              "lessons. The band is 0–5, the deepest nesting 1 and the first line at that "
              "depth line 5. Both conditions sit inside the code that builds the HTML, so "
              "nobody can change the row's markup without reading them, and nobody can "
              "test them without building a row."),
        ("code", _lines(TICKET_HELPER)),
        ("p", "<code>ticket-helper</code> gives the two conditions to `TicketHelper`, as the "
              "methods `isFew` and `showResale`, and the lab prints 3, broken down as "
              "`1 + && 1 + || 1`. The `if`s are gone because each method returns its condition "
              "instead of branching on it; the two connectives are still there. The lab "
              "counts the whole listing as one, starting at one, so 3 is not a figure for "
              "either method. A class has no routine header, so the lab counts depth from "
              "the top of the listing: inside the class and inside a method, line 6 is at "
              "depth 2. The template that uses the helper would hold two markers that ask "
              "a single Boolean each, which is Fowler's rule, and no condition of its own."),
        ("p", "So the count fell from 5 to 3, and that is not the point. The decisions moved "
              "to a class that can be tested by constructing a ticket and asking it, with no "
              "web server, and the row's markup moved to a page that a designer can edit. "
              "The template itself is not Java, and the lab cannot count it."),
        ("h3", "Exercise"),
        ("code", _lines(PRICE_CELL)),
        ("p", "A price cell, built inline. Count its decision points by the lab's rule, with "
              "the breakdown. Then name the helper methods a template would call instead, "
              "one for each condition, and say what each returns."),
        ("p", "A site-wide change of look can still mean editing every template. The next "
              "lesson, Two Step View, reads the variation that puts the look in one place."),
    ],
    "lab": ("cckit", {
        "mode": "code",
        "view": "complexity",
        "bands": [5, 10],
        "book": "other",
        "preset": "ticket-row",
        "presets": [
            {"id": "ticket-row",
             "label": "A ticket row with its decisions inline",
             "code": TICKET_ROW,
             "expect": {"coDecisions": "5", "coBreakdown": "1 + if 2 + && 1 + || 1"}},
            {"id": "ticket-helper",
             "label": "The helper that holds the row's two conditions",
             "code": TICKET_HELPER,
             "expect": {"coDecisions": "3", "coBreakdown": "1 + && 1 + || 1"}},
        ],
        "panel_title": "The logic in a page, and in its helper",
        "panel_intro": (
            "The lab counts decision points by a stated rule: one, plus one for each if, "
            "while, for and case, and for each conditional-and or conditional-or "
            "operator. A class is counted as one listing. The bands "
            "beside the count are McConnell's, from Code Complete; Fowler gives no count. "
            "The listings are the lesson's."
        ),
    }),
    "steps_title": "Taking the logic out of a page",
    "steps_intro": "Four steps, the last of them on a template of your own.",
    "steps": [
        ("Find the conditions",
         "Read the page or the code that builds it and mark every if, loop and connective "
         "that decides what is shown."),
        ("Name each one",
         "Give each condition a name that says what it means for the page, such as "
         "isFew or showResale, not how it is computed."),
        ("Move them to a helper",
         "Write a helper class with one Boolean method for each name, and leave the page "
         "one marker for each that asks it. Loops over a collection can stay as the "
         "template's iteration."),
        ("Count a template of your own",
         "Take one template in a system you know and count the conditionals in it. Write "
         "the figure, and mark the ones that test more than one value."),
    ],
    "worked": {
        "title": "The ticket row, by the rule",
        "intro": [
            "Take the preset <code>ticket-row</code> and count line by line.",
        ],
        "lines": [
            "start: 1",
            "line 4, if the seats are few: 2",
            "line 4, or it is the last release: 3",
            "line 6, else: adds nothing, still 3",
            "line 9, if it is a resale: 4",
            "line 9, and not the last release: 5",
        ],
        "after": [
            "One, two `if`s, one `||` and one `&&`, which the lab prints as "
            "`1 + if 2 + && 1 + || 1`. In "
            "<code>ticket-helper</code> the two ifs become two returned conditions, and "
            "the count of the listing is 3.",
        ],
    },
    "quiz_title": "Views, helpers and decisions",
    "quiz": [
        {"q": "Count the exercise's price cell by the lab's rule: one, plus one for each if, "
              "while, for, case, `&&` and `||`. How many decision points, with the breakdown?",
         "a": ["6: 1 + if 2 + && 1 + || 2",
               "5: 1 + if 2 + && 1 + || 1",
               "7: 1 + if 2 + && 1 + || 2 + else 1",
               "5: if 2 + && 1 + || 2"],
         "c": 0,
         "why": "Start at 1. Line 3 is an `if` with one `&&`, line 9 an `if` with two `||`, "
                "and the else on line 6 adds nothing: 1 + 2 + 1 + 2 = 6. A helper would "
                "hold two Boolean methods, such as `showWasPrice()` for the sale price below "
                "the full price, and `isUnavailable()` for no stock, a withdrawn item or a "
                "recalled one, and the template would ask each one."},
        {"q": "Where Template View must show something only under a condition, what does "
              "Chapter 14 recommend the condition be based on?",
         "a": ["A general IF tag holding the whole expression",
               "A scriptlet placed in the page at that point",
               "One true-or-false method of the page's helper",
               "A separate page for each case of the condition"],
         "c": 2,
         "why": "Fowler calls purely conditional tags a bad smell, because they turn the "
                "template into a programming language, and scriptlets a big problem. "
                "Whatever tag is used, the condition should ask the helper one true-or-false "
                "question; a more complex expression puts the logic in the page."},
        {"q": "What is the key difference Chapter 14 draws between Template View and "
              "Transform View?",
         "a": ["Template View needs a web server to run, and Transform View needs XSLT",
               "Template View follows the output, and Transform View the input's elements",
               "Template View is for static pages, and Transform View for dynamic ones",
               "Template View holds no logic at all, and Transform View holds all of it"],
         "c": 1,
         "why": "A template is the page with markers in it; a transform view has a "
                "transform for each kind of input element and a loop that walks the data. "
                "Transform View can be written in any language, and both views serve "
                "dynamic pages."},
        {"q": "Which of these is one of the two weaknesses Fowler names in Template View?",
         "a": ["It cannot display anything conditionally",
               "It cannot be edited in a visual HTML editor",
               "It must be written in XSLT to be tested",
               "It is harder to test than Transform View, outside a web server"],
         "c": 3,
         "why": "The two weaknesses are that the usual implementations let complicated "
                "logic into the page too easily, and that most implementations are "
                "hard or impossible to test outside a web server. Conditional display is "
                "one of its hard cases, met with a helper, and editing in a visual editor "
                "is one of its strengths."},
    ],
    "mistakes": [
        ("Thinking a template with no code cannot show anything conditional",
         "If the page may hold no logic, it seems it can only show what is always there. "
         "Template View's hard cases are exactly conditional display and iteration, and "
         "Fowler's answer is a helper that decides and a marker that asks it, one Boolean "
         "property at a time. On the lesson's illustration the row's two conditions become "
         "`isFew` and `showResale`, and the template holds none."),
        ("Thinking Transform View needs XSLT",
         "The book's examples of Transform View are XSLT, and XSLT was the dominant choice "
         "when it was written. But the pattern is a transformation organised around the "
         "input, element by element, and Fowler says it can be written in any language: a "
         "method that renders a concert and loops over its ticket sections, calling a "
         "method that renders a section, is one."),
        ("Thinking the two views differ only in syntax",
         "Both produce HTML, so the choice can look like a matter of notation. Fowler's "
         "difference is organisation, the output's structure against the input's, and it "
         "has consequences: a template lets a designer lay out the page, while a transform "
         "is easier to keep free of other logic and to test without a web server."),
    ],
    "standard": (
        "Finish when you can take the logic out of a page fragment.",
        "Given a page fragment with its logic inline, count its decision points by the "
        "rule, with the breakdown, and write the helper methods a template would call, "
        "one Boolean for each condition."
    ),
    "note": (
        "The lab counts Java, so it cannot read a template, and the drop from 5 to 3 is a "
        "move, not a saving. The book was written for pages built on the server. Much of "
        "today's presentation is built in the browser, where the same separation, a "
        "component that renders and the data it is given, is argued afresh: some hold that "
        "putting markup and logic in one component is the right unit, others that it brings "
        "back the scriptlet. That argument is not settled here."
    ),
}

# ---------------------------------------------------------------- 05
# Chapter 4, View Patterns, PDF pp. 67-69 of the operator's copy (the second
# stage, pp. 68-69); Chapter 14, Two Step View, pp. 331-343 (examples from
# p. 337, pointed to). Quote: PDF p. 333 of the operator's copy, 22 words,
# ea_quotes.py OK. Lesson total: 22 words.
# The logical screen (p. 331); the two stages and the ways to build them
# (p. 332); single- and multiappearance (p. 333); ten screens and three
# appearances (p. 336); the costs and devices (p. 337).
# F24, PDF p. 336 of the operator's copy: ten screens and three appearances,
# thirty single-stage views against ten first stages and three second.
TWO_STEP_VIEW = {
    "slug": "two-step-view",
    "title": "Two Step View",
    "module": "Chapter 14 · Web Presentation Patterns",
    "one_line": "Two Step View builds a logical screen for each page and turns every logical screen into HTML in one place, so a change of look is made once, at the price of fitting every page to the logical screen.",
    "summary": (
        "Chapter 4's View Patterns and Chapter 14's Two Step View: a first stage for each "
        "page that turns domain data into a logical screen with no formatting, and one "
        "second stage for the site that turns logical screens into HTML. Count what a "
        "change of look reaches with one stage and with two, and see which change becomes "
        "the expensive one."
    ),
    "key": [
        "first stage: data to a logical screen",
        "second stage: logical screen to HTML",
        "a first stage per page; one second stage",
        "a change of look: the second stage",
        "a change of screen: every stage",
    ],
    "key_label": "Two Step View in five lines",
    "concepts_intro": (
        "Three terms carry the section and the pattern. The first is the one everything "
        "else depends on."
    ),
    "concepts": [
        ("Logical screen",
         "A structure that describes what a screen shows, fields, headers, tables, choices, "
         "without saying how it looks: it contains no HTML. Fowler also calls it the "
         "presentation-oriented structure. Every page on the site has to be expressible "
         "in it."),
        ("First stage and second stage",
         "The first stage is code written for one screen: it reads the domain data and "
         "builds that screen's logical screen. The second stage turns any logical screen "
         "into HTML, and there is one for the whole site, or one for each look."),
        ("Single- and multiappearance",
         "A single-appearance site has one look throughout. A multiappearance site offers "
         "the same function under several looks, for several organisations or devices, "
         "each with its own second stage."),
    ],
    "read_title": "The section and the pattern, then the count",
    "read_intro": (
        "Read the second half of View Patterns in Chapter 4 and Two Step View in Chapter "
        "14 in your own copy first. The lesson sets out what the second stage buys and "
        "costs, and then counts what a change reaches in a site with one stage and with "
        "two."
    ),
    "body": [
        ("p", "&ldquo;Two Step View's key value comes from the separation of first and "
              "second stages, allowing you to make global changes more easily.&rdquo; That "
              "is how When to Use It opens, in Chapter 14. If you have changed a site's "
              "look, a new header or a different style of table, and found the change "
              "waiting in every page's template, you have met the problem it answers. This "
              "lesson reads the second half of View Patterns in Chapter 4 and Two Step View "
              "in Chapter 14. Read them in your own copy first."),
        ("p", "Chapter 4 sets the two shapes side by side. In a single-stage view there is, "
              "for the most part, one view component per screen, which turns the domain's "
              "data straight into HTML. A two-stage view breaks that into a logical screen produced from "
              "the domain data and then rendered in HTML, with one first stage for each "
              "screen and only one second stage for the application. The advantage, Fowler "
              "says, is that the decision about which HTML to use is in one place, so a "
              "global change to the HTML is one object to alter. He qualifies it at once: "
              "the gain lasts only as long as every screen keeps to one logical layout, "
              "so it works best where screens share a basic layout, and highly "
              "design-intensive sites will not find a good logical screen."),
        ("p", "The section adds the case where the pattern works even better: one service "
              "fronted by several customers, his example being several airlines in front of "
              "one reservation system, each with its own look through its own second "
              "stage; and, in the same way, separate second stages for different devices. "
              "The limit is the same each time. Every look must fit one logical screen, and "
              "very different interfaces may not."),
        ("p", "Two Step View, read as a pattern, makes the logical screen concrete. Its "
              "elements might be fields, headers, footers, tables and choices: "
              "presentation-oriented, and forcing the screens into a definite style, but "
              "with no HTML. The first stage, written for each screen, reads a "
              "domain-oriented model, extracts what the screen needs, and puts it into the "
              "structure. The second stage knows each kind of element and how to show it "
              "as HTML, so all the formatting decisions are made in one place. It can be "
              "built as two XSLT stylesheets, as classes for the elements rendered by "
              "themselves or by a separate renderer, or as templates written in logical "
              "tags."),
        ("p", "When to Use It does the arithmetic in words. A single-stage site has one view "
              "module for each page; a two-step site has one first stage for each page and "
              "one second stage for the site, so a change to the site's appearance is one "
              "change. With several appearances the saving compounds. Fowler's own figures: "
              "ten screens and three appearances need thirty single-stage view modules, "
              "where two stages need thirteen, ten for the screens and three for the looks. "
              "The saving, he says, grows with both numbers."),
        ("p", "The costs are as plain. The pattern depends on making the logical screen "
              "serve the look, and a site built on visual design, whose every page is to "
              "look unlike the others, is constrained by it, too much for many sites. Designers who lay "
              "out pages in visual editors cannot write a renderer, so programmers are "
              "involved in every design change. And it is a harder programming model to "
              "learn, Fowler concedes, though not difficult once you are used to it, and "
              "it may cut repetitive code. Its examples, a two-stage XSLT and JSP with "
              "custom tags, are worth reading in the book."),
        ("p", "Now the code, written for the lesson. A `Field` is the smallest logical "
              "screen there is, a label and a value. `HtmlRenderer` is a second stage: it "
              "takes any list of fields and writes them as a definition list. A first stage "
              "for a concert page would build the concert's list of fields and hand it over; "
              "so would the stages for a venue page and a tour page. To show every field on "
              "the site as a table instead, you would change `render` and nothing else."),
        ("code", _lines(SECOND_STAGE)),
        ("p", "The lab is the ripple view of the first lesson: records `dependent, "
              "dependency`, a changed class, and what the change reaches directly and in "
              "all. In <code>one-step</code> three pages each format their own HTML, so "
              "each depends on `look`, the site's style decisions, and two of them depend "
              "on their models too. Change `look` and the lab prints 3: concertpage, "
              "tourpage, venuepage directly, and the same three in all. The model records "
              "make no difference to a change of look."),
        ("p", "In <code>two-step</code> the pages depend on `screen`, the logical screen, "
              "and only `renderer` depends on both `screen` and `look`. The same change "
              "prints 1: renderer directly and 1: renderer in all. That is the "
              "quotation's global change, made in one class."),
        ("p", "Being reached is not the same as being edited, and here the difference "
              "matters. In <code>one-step</code> each page holds its own HTML, so a page "
              "reached by a change of look is a page to edit; in <code>two-step</code> "
              "only the renderer holds any. The count says where to look. It also shows "
              "where the cost went, because the logical screen is now something everything "
              "depends on, and the exercise asks what that costs."),
        ("h3", "Exercise"),
        ("code", _lines(SCREEN_DEPS)),
        ("p", "A site with three pages, a renderer for the browser and a second renderer for "
              "printing, each with its own look. Change `screen`, the logical screen, and "
              "say by hand what the change reaches directly and in all. Then compare it "
              "with a change to `look`."),
        ("p", "Views and controllers decide what one page shows. The next lesson, "
              "Application Controller, reads the pattern that decides which page comes "
              "next."),
    ],
    "lab": ("cckit", {
        "mode": "deps",
        "view": "ripple",
        "preset": "one-step",
        "presets": [
            {"id": "one-step",
             "label": "One stage: each page formats its own HTML (illustrative)",
             "edges": "concertpage, look; venuepage, look; tourpage, look; "
                      "concertpage, concert; venuepage, venue",
             "changed": "look",
             "expect": {"dgDirect": "3: concertpage, tourpage, venuepage",
                        "dgAffected": "3: concertpage, tourpage, venuepage"}},
            {"id": "two-step",
             "label": "Two stages: pages build a logical screen, one renderer formats it",
             "edges": "concertpage, screen; venuepage, screen; tourpage, screen; "
                      "renderer, screen; renderer, look; "
                      "concertpage, concert; venuepage, venue",
             "changed": "look",
             "expect": {"dgDirect": "1: renderer", "dgAffected": "1: renderer"}},
        ],
        "panel_title": "What a change of look reaches",
        "panel_intro": (
            "Each record is one dependency, written dependent, dependency. Name the class "
            "that changes; the lab lists what depends on it directly and everything the "
            "change reaches. The sites are the lesson's."
        ),
    }),
    "steps_title": "Counting what a change of look reaches",
    "steps_intro": "Four steps, the last of them on a change you have made.",
    "steps": [
        ("Write down who formats",
         "For each page, write a record for every class it uses, and a record for the "
         "look if the page makes its own decisions about HTML."),
        ("Count the reach of a look change",
         "Change the look and list what depends on it, directly and in all. With one stage "
         "that is every page that formats."),
        ("Redraw with a logical screen",
         "Make every page depend on the logical screen instead, and give one renderer the "
         "records for the screen and the look. Count again, and then count a change to the "
         "screen."),
        ("Count a change of your own",
         "Take one site-wide change of look you have made, or one you would make. Count "
         "the files it touched, write the figure, and say which of them held their own "
         "HTML."),
    ],
    "worked": {
        "title": "A change of look, with two stages",
        "intro": [
            "Take the preset <code>two-step</code> and change `look`.",
        ],
        "lines": [
            "who uses look? renderer only",
            "direct: 1, renderer",
            "who uses renderer? nobody",
            "reached in all: 1, renderer",
            "the pages use screen, not look: not reached",
        ],
        "after": [
            "With one stage the same change reaches all three pages, each of which holds "
            "its own HTML. With two, the one class that holds HTML is the one class "
            "reached.",
        ],
    },
    "quiz_title": "Stages, screens and reach",
    "quiz": [
        {"q": "Take the exercise's seven records and change `screen`. What does the change "
              "reach directly, and in all?",
         "a": ["Directly 2: printrenderer, renderer; in all 2, the same two renderers",
               "Directly 5, the pages and renderers; in all 7, adding look and printlook",
               "Directly 3: account, home, search; in all 5, adding both renderers",
               "Directly 5: account, home, printrenderer, renderer, search; in all 5"],
         "c": 3,
         "why": "Five records point at `screen`: the three pages and both renderers. Nothing "
                "depends on any of the five, so the change reaches the same 5 in all: "
                "account, home, printrenderer, renderer, search. `look` and `printlook` are "
                "what the renderers use, not what uses them. A change to `look` reaches 1, "
                "the renderer; a change to the logical screen reaches every first and "
                "second stage."},
        {"q": "Fowler's illustration in Two Step View: ten screens and three appearances. "
              "How many view modules does a single-stage design need, and how many first "
              "and second stages does a Two Step View need?",
         "a": ["Thirty; thirteen",
               "Thirty; thirty, one view for each pairing",
               "Thirteen; thirty",
               "Ten; three, one for each screen and look"],
         "c": 0,
         "why": "Single-stage needs a view for every pairing of a screen with a look, "
                "10 × 3 = 30. Two Step View needs a first stage for each screen and a second "
                "stage for each appearance, 10 + 3 = 13. The figures are the book's "
                "illustration, not a measurement."},
        {"q": "Which kind of site does Chapter 14 say Two Step View does not suit?",
         "a": ["A site with one look throughout all of its pages",
               "A site offered under several organisations' own looks",
               "A design-led site whose every page looks different",
               "A site whose screens all share one basic layout"],
         "c": 2,
         "why": "It is hard to find a simple enough logical screen for a site whose pages "
                "are all different, and the design is constrained by it. Single-appearance "
                "sites are the common case and gain from one second stage, "
                "multiappearance sites gain most, and screens "
                "that share a basic layout are what the pattern needs."},
        {"q": "What does a first stage produce?",
         "a": ["The finished HTML of the page, ready to send",
               "A logical screen of fields and tables, with no HTML in it",
               "An XSLT stylesheet for the second stage to apply",
               "The domain-oriented XML the model produced"],
         "c": 1,
         "why": "The first stage reads the domain-oriented model and fills a "
                "presentation-oriented structure, fields, tables and the like, with no "
                "HTML; the second stage turns it into HTML. Stylesheets are one way to "
                "build either stage."},
    ],
    "mistakes": [
        ("Taking Two Step View for two templates per page",
         "The name suggests each page now has two views. It is one first stage for each "
         "page and one second stage for the whole site, or one for each look. On the "
         "lesson's illustration three pages need three first stages and one renderer, and "
         "a change of look reaches only the renderer."),
        ("Thinking a second stage makes every change cheaper",
         "It makes a change of look cheaper by putting all the HTML in one place. A change "
         "to the logical screen itself, a new kind of element or a changed field, is the "
         "expensive one; the exercise counts it."),
        ("Expecting the pattern to suit every site",
         "If one place for the HTML is good, it seems every site should have it. Fowler "
         "says a design-intensive site, where each page is meant to look different, will "
         "not find a good logical screen and is constrained by one, and that a two-step "
         "site needs programmers for every design change."),
    ],
    "standard": (
        "Finish when you can count what a change of look reaches.",
        "Given pages that each format their own HTML, list what a change of look reaches; "
        "then redraw the site with a logical screen and a renderer, and list what a change "
        "of look and a change of the logical screen each reach."
    ),
    "note": (
        "The lab follows the records it is given, so it cannot see whether your pages "
        "really share a layout, which is the condition the whole pattern rests on. It "
        "counts classes reached, not lines changed: a renderer reached by a change of "
        "look may need one line or a rewrite. Fowler's thirty against thirteen is an "
        "illustration of how the saving grows, not a figure for any site."
    ),
}

# ---------------------------------------------------------------- 06
# Chapter 4's opening, PDF p. 66 of the operator's copy (Application
# Controller and the test of who controls the flow), and Further Reading,
# p. 71 (the terminology from Knight and Dai); Chapter 14, Application
# Controller, pp. 344-350 (example from p. 346, pointed to); Chapter 8,
# Other Layering Schemes, p. 107 (read in lesson 7.4).
# Quote: PDF p. 346 of the operator's copy, 28 words, ea_quotes.py OK.
# Lesson total: 28 words.
# The duplication across input controllers (p. 344); two responsibilities
# and two collections (pp. 344-345); no links to the UI machinery, several
# controllers, state machines (p. 345); domain logic and the smoker's
# screen (pp. 345-346); When to Use It and Knight and Dai (p. 346).
APPLICATION_CONTROLLER = {
    "slug": "application-controller",
    "title": "Application Controller",
    "module": "Chapter 14 · Web Presentation Patterns",
    "one_line": "An Application Controller holds an application's rules about which screen comes next in one place, so that the input controllers stop repeating them.",
    "summary": (
        "Chapter 4's opening and Chapter 14's Application Controller: a central point for "
        "screen navigation and flow, which input controllers ask for the command to run "
        "and the view to show next. Count the flow decisions two controllers repeat, move "
        "them to one method, and read Fowler's test for when the pattern earns its place."
    ),
    "key": [
        "flow: which screen comes next",
        "input controllers ask; it decides",
        "it picks a command and a view",
        "machine leads the flow: use one",
        "user leads the flow: you need none",
    ],
    "key_label": "Application Controller in five lines",
    "concepts_intro": (
        "Three ideas carry the pattern. The second is the word Fowler has been careful "
        "about since the first lesson."
    ),
    "concepts": [
        ("Screen flow",
         "The order in which an application shows its screens, and the rules that decide "
         "it: a wizard that leads through steps, a screen shown only under a condition, a "
         "choice of screen that depends on earlier input."),
        ("Application controller",
         "An object that holds those rules in one place. Input controllers ask it which "
         "domain command to run and which view to show next. It is a different thing from "
         "the controller of Model View Controller, which handles one request."),
        ("Mediating layer",
         "A layer between two others that both talk to, so that neither needs to know the "
         "other. An Application Controller with no links to the user-interface machinery "
         "can be thought of as one, between the presentation and the domain; Chapter 8 "
         "places it so, in the last course."),
    ],
    "read_title": "The chapter's test and the pattern, then the count",
    "read_intro": (
        "Read the opening of Chapter 4 again for Application Controller, and the pattern "
        "in Chapter 14, in your own copy first. The lesson sets out when Fowler thinks an "
        "application needs one, describes the pattern, and then counts the flow rules two "
        "controllers repeat."
    ),
    "body": [
        ("p", "&ldquo;A good signal to use an Application Controller is if you find yourself "
              "having to make similar changes in lots of different places when your "
              "application's flow changes.&rdquo; That is the whole of the signal Fowler "
              "gives in Chapter 14. Who decides which screen comes next, and where is that "
              "decision written down? This lesson reads his answer, in the opening of "
              "Chapter 4 and in the last pattern of Chapter 14. Read them in your own copy "
              "first."),
        ("p", "Chapter 4's opening introduced the pattern as a second use of the word "
              "controller. Many user-interface designs, Fowler says, put a layer of "
              "Application Controller objects between the presentation and the domain, to "
              "handle the flow of the application, deciding which screens appear in which "
              "order. It can be part of the presentation or a separate layer that mediates "
              "between presentation and domain, and written independently of any one "
              "presentation it can be reused across several, though different "
              "presentations are often best given different flows."),
        ("p", "Not every system needs one, the chapter goes on. It earns its place where much "
              "of the code is about which screen follows which, or where pages do not line "
              "up simply with actions on the domain; where a user may open the screens in "
              "nearly any order, there is little for it to do. Fowler's test fits in a "
              "line: when the application decides which screen the user sees next, you "
              "want an Application Controller; when the user decides, you do not."),
        ("p", "Application Controller, read as a pattern, starts from the wizard: the user "
              "led through screens in a set order, screens shown only under conditions, a "
              "choice of screen that depends on earlier input. Input controllers can make "
              "those decisions, but as the application grows, several of them come to need "
              "the same knowledge, and the code is duplicated. The pattern puts all the "
              "flow logic in one object, which the input controllers ask for the command to "
              "run against the model and the view to show. It has two jobs, choosing the "
              "domain logic to run and choosing the view for the response, and typically "
              "holds two collections of references, one of domain commands and one of "
              "views: command objects, references to functions, names for reflection, or "
              "server page names."),
        ("p", "Fowler's preference is for an Application Controller with no links to the "
              "user-interface machinery: it neither reads the HTTP session, nor forwards to "
              "a server page, nor calls a rich-client class. That makes it testable without "
              "the interface and reusable across presentations, and it is why many people "
              "think of it as an intermediate layer. Chapter 8's Other Layering Schemes, "
              "read in the last course, gives it exactly that place in one of the layering "
              "schemes it compares. An application may have several, one for each broad "
              "area of the interface, and a flow often thought of as a state machine can "
              "be held as metadata."),
        ("p", "He comes down hard, he says, against putting domain logic in it, and then "
              "admits the boundary is murky. His case is an insurance application that "
              "shows an extra screen of questions only to smokers: is that application "
              "logic or domain logic? A few such cases can live in the Application "
              "Controller; if they occur in many places, the Domain Model should be "
              "designed to drive them. The pattern's ideas, he writes, came mostly from "
              "Knight and Dai, as the book cites them (IEEE Software, 2002), whose "
              "explanations he found unusually clear; Chapter 4's Further Reading credits them "
              "with the vocabulary that separates input controllers from application "
              "controllers. The pattern's example, a controller driven by a state model, "
              "is worth reading in the book."),
        ("p", "Now the code, written for the lesson. Two input controllers of a checkout each "
              "decide where to send the customer after their step: after the address, and "
              "after the cart."),
        ("code", _lines(FLOW_REPEAT)),
        ("p", "The lab is the repeated-lines view of Front Controller, with the same rule: "
              "identical statement lines, spacing collapsed, in runs of two or more. On "
              "<code>flow-repeat</code> it prints 1 block, 6 lines, at lines 2–4 and lines "
              "9–11: the customs form, the approval and the payment, written in both "
              "controllers in the same order. That is Fowler's signal as a count. Add a "
              "screen to the flow, a gift message before payment, say, and the change must "
              "be made in both places, and in every other controller that knows the order."),
        ("p", "<code>next-screen</code> holds the flow in one method, and the lab prints 0 "
              "blocks, 0 lines, none. Each input controller would call `nextScreen` and "
              "redirect to what it returns. The method returns a path rather than "
              "redirecting, so it has no link to the request or the response, Fowler's "
              "preference, and a test can call it with an order and check the answer."),
        ("code", _lines(NEXT_SCREEN)),
        ("p", "One check is needed before the move is safe. The two controllers were not "
              "identical: `afterCart` first sends a customer with no address to the "
              "address screen, and `afterAddress` does not, because its step has just "
              "taken the address. `nextScreen` asks the address question every time, which "
              "gives the same answer after the address step, since `hasAddress` is then "
              "true. The conditions themselves, `needsCustomsForm` and the total against a "
              "limit, are questions the order answers; the order in which they are asked is "
              "the flow, and that is what moved."),
        ("h3", "Exercise"),
        ("code", _lines(CLAIM_FLOW)),
        ("p", "Two input controllers of an insurance claim form. Mark by hand the lines that "
              "repeat, by the lab's rule, with their line numbers and how many lines the "
              "copies hold. Then write the one method that replaces them, `nextStep(Claim "
              "c)`, returning the path of the next screen."),
        ("p", "This ends the course. The next course, Concurrency and Session State, reads "
              "what happens when many people use these pages at once."),
    ],
    "lab": ("cckit", {
        "mode": "code",
        "view": "dupes",
        "min_run": 2,
        "preset": "flow-repeat",
        "presets": [
            {"id": "flow-repeat",
             "label": "Two checkout controllers, each deciding the next screen",
             "code": FLOW_REPEAT,
             "expect": {"coDupBlocks": "1", "coDupLines": "6",
                        "coDupWhere": "lines 2–4 and lines 9–11"}},
            {"id": "next-screen",
             "label": "The checkout's flow in one method",
             "code": NEXT_SCREEN,
             "expect": {"coDupBlocks": "0", "coDupLines": "0", "coDupWhere": "none"}},
        ],
        "panel_title": "Flow written in more than one place",
        "panel_intro": (
            "The lab compares statement lines as text, with spacing collapsed, and reports "
            "each run of two or more lines that appears more than once. Lines that differ "
            "only in a name are not the same text, so the lab does not see them. The "
            "listings are the lesson's."
        ),
    }),
    "steps_title": "Finding the flow and putting it in one place",
    "steps_intro": "Four steps, the last of them on a flow of your own.",
    "steps": [
        ("Ask who controls the flow",
         "If the user can open the screens in nearly any order, stop: there are no "
         "rules for an Application Controller to hold. If the application leads, go on."),
        ("Mark the repeated rules",
         "Line up the input controllers and mark every run of lines that decides the next "
         "screen in the same way in more than one of them."),
        ("Write one method",
         "Write a method that takes the domain object and returns the next screen, asking "
         "the questions in the flow's order, and check that it gives each controller's old "
         "answer."),
        ("Count a flow of your own",
         "Take one wizard or checkout in a system you know. Count the places its order of "
         "screens is written down, write the figure, and say which one should hold it."),
    ],
    "worked": {
        "title": "Two checkout controllers, compared",
        "intro": [
            "Take the preset <code>flow-repeat</code> and compare the two routines.",
        ],
        "lines": [
            "lines 2 and 9: the customs form",
            "lines 3 and 10: the approval",
            "lines 4 and 11: the payment",
            "line 8: the address check, after the cart only",
            "one block of 3 lines, in 2 copies: 6 lines",
        ],
        "after": [
            "The flow is written twice, in the same order. <code>next-screen</code> writes "
            "it once, with the address check first, and the lab finds nothing repeated.",
        ],
    },
    "quiz_title": "Flow, signals and the pattern",
    "quiz": [
        {"q": "In the exercise's two claim controllers, which lines repeat by the lab's rule "
              "(identical statement lines, in runs of two or more), and how many lines do "
              "the copies hold?",
         "a": ["Lines 2–4 and lines 9–11: 6 lines, as in the checkout",
               "Lines 2–4 and lines 10–12: 6 lines, in two copies",
               "Lines 2–3 and lines 10–11: 4 lines, without the bank",
               "Lines 2–4 and lines 10–12: 3 lines, one copy counted"],
         "c": 1,
         "why": "The assessor check, the medical check and the redirect to the bank details "
                "are the same text on lines 2 to 4 and 10 to 12: one block of 3 lines in 2 "
                "copies, 6 lines. Lines 8 and 9, the photo checks, are in one controller "
                "only, and the routine headers differ. One `nextStep(Claim c)` asking about "
                "the photos, then the assessor, then the medical screen, and otherwise the "
                "bank, replaces them, with one difference to decide: a claim with no photos "
                "leaving the details step now goes to `/photos`, where the old controller "
                "sent it on. If the details step can come before the photos, that is a "
                "change in the flow, and possibly the fix it needed; if it cannot, the "
                "answers are the same."},
        {"q": "What is Chapter 4's test for whether a system needs an Application "
              "Controller?",
         "a": ["Whether it has more than one input controller handling pages",
               "Whether it already sends every request through a Front Controller",
               "Whether it serves more than one presentation of the same model",
               "Whether the machine or the user is the one controlling the flow"],
         "c": 3,
         "why": "When the application decides the order of screens, it needs one; when the "
                "user decides, it does not. Several input controllers, a Front Controller or several "
                "presentations do not by themselves make flow rules."},
        {"q": "What are an Application Controller's two responsibilities, as Chapter 14 "
              "gives them?",
         "a": ["Choosing the domain logic to run and the view to show next",
               "Handling the HTTP request and rendering the full response",
               "Validating the user's input and saving the changed model",
               "Choosing the command and configuring the web server for it"],
         "c": 0,
         "why": "It decides which domain logic to run and which view displays the response, "
                "and holds a collection of references for each. Handling the request is the "
                "input controller's job, and the commands do the domain work."},
        {"q": "Which design for an Application Controller does Fowler prefer?",
         "a": ["One that reads the HTTP session directly for its state",
               "One that forwards to the server pages itself when done",
               "One with no links at all to the user-interface machinery",
               "One that holds the domain logic for each request"],
         "c": 2,
         "why": "With no links to the interface machinery it can be tested independently and "
                "used with several presentations. He comes down hard against domain logic "
                "in it, while granting that the boundary is murky."},
    ],
    "mistakes": [
        ("Thinking every web application needs an Application Controller",
         "Any application has an order of screens, so it seems any application needs "
         "something to hold it. Fowler's signal is the quotation: similar changes in many "
         "places when the flow changes. Where a user may open the screens in nearly any "
         "order there are no rules for it to hold, and it adds little; if the user is in "
         "control of the flow, you do not need one."),
        ("Thinking the application controller does the work",
         "It sits in the middle of every request, so it looks like the place for the "
         "work. It decides what comes next: which command to run and which view to show. "
         "The domain commands do the work, and Fowler comes down hard against putting "
         "domain logic in it."),
        ("Sharing one flow across every presentation",
         "An Application Controller free of the interface can serve a browser, a desktop "
         "program and a handheld device at once, and that seems the point of making it "
         "free. Fowler says not to be too eager: different interfaces often need different "
         "flows to be usable, though one shared controller may be worth a more awkward "
         "interface for the effort it saves."),
    ],
    "standard": (
        "Finish when you can find a flow written twice and write it once.",
        "Given two input controllers, mark the repeated flow lines with their line "
        "numbers, and write the application controller's method that returns the next "
        "screen."
    ),
    "note": (
        "The lab sees identical lines only, so a flow rule written two ways is not "
        "counted, and it cannot check that one method gives the answers each controller "
        "gave; that check is the reader's, done above for the address step. Nor can it say "
        "whether a rule is flow or domain logic, which Fowler admits is murky."
    ),
}

LESSONS = [
    MODEL_VIEW_CONTROLLER,
    PAGE_CONTROLLER,
    FRONT_CONTROLLER,
    TEMPLATE_AND_TRANSFORM_VIEW,
    TWO_STEP_VIEW,
    APPLICATION_CONTROLLER,
]
