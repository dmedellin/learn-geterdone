"""A Case Study: Designing a Document Editor, lessons 1-5 -- Chapter 2, sections 2.1-2.6.

Gamma, Helm, Johnson and Vlissides, Design Patterns: Elements of Reusable
Object-Oriented Software (Addison-Wesley, 1995), Chapter 2: 2.1 Design
Problems and 2.2 Document Structure (Composite), 2.3 Formatting (Strategy),
2.4 Embellishing the User Interface (Decorator), 2.5 Supporting Multiple
Look-and-Feel Standards (Abstract Factory) and 2.6 Supporting Multiple Window
Systems (Bridge). Pages in the comments are PDF pages of the operator's copy;
the lessons cite by chapter, section and pattern. Every quotation is copied
from that copy and checked with quotes.py. Lexi's design is summarised in
prose; the designs, records and code the labs and sketches use are written
for these lessons (a recipe book, a playlist app, an audio-guide rental, a
map viewer, a library's notices), and none of the book's code, diagrams,
tables or example data is reproduced. The design is
docs/design-patterns/PLAN.md, section C, Course 2.
"""


def _lines(text):
    """A snippet or record constant as a code block's list of lines."""
    return text.split("\n")


def _records(text):
    """Records written one to a line, as the single string a lab field takes."""
    return " ".join(line.strip() for line in text.split("\n") if line.strip())


# ---------------------------------------------------------------- 2.2 records

# A recipe book as a tree of parts. Sections are composites; recipes and the
# cover photo are leaves, valued in minutes of cooking time (the photo, 0).
RECIPE_BOOK = """book, -, Section, -;
cover, book, Photo, 0;
breads, book, Section, -;
focaccia, breads, Recipe, 95;
pitta, breads, Recipe, 40;
cakes, book, Section, -;
layer, cakes, Section, -;
sponge, layer, Recipe, 55;
gateau, layer, Recipe, 120;
flapjack, cakes, Recipe, 35"""

# A talk's slide outline in minutes: parts are composites; slides and a clip
# are leaves.
TALK_OUTLINE = """talk, -, Part, -;
intro, talk, Slide, 2;
method, talk, Part, -;
setup, method, Slide, 4.5;
results, method, Slide, 6;
demo, method, Clip, 3.5;
close, talk, Slide, 1.5"""

# Exercise: a mixtape in minutes.
MIXTAPE = """mix, -, List, -;
side-a, mix, List, -;
t1, side-a, Track, 3.5;
t2, side-a, Track, 4.25;
side-b, mix, List, -;
t3, side-b, Track, 5;
encore, side-b, List, -;
t4, encore, Track, 2.75;
t5, mix, Track, 6"""

BOOK_PART_JAVA = """// Every part of the recipe book answers one question: how long?
interface BookPart {
    int minutes();
}
final class Recipe implements BookPart {
    private final int minutes;
    Recipe(int minutes) { this.minutes = minutes; }
    public int minutes() { return minutes; }
}
final class Section implements BookPart {
    private final List<BookPart> parts = new ArrayList<>();
    void add(BookPart part) { parts.add(part); }   // on Section only
    public int minutes() {
        int sum = 0;
        for (BookPart part : parts) {
            sum += part.minutes();   // a recipe or a whole section
        }
        return sum;
    }
}"""


# ---------------------------------------------------------------- 2.3 records

PLAYLIST_ASPECTS = "playlist, album, mix, radio; ordering, shuffle, by-artist, by-tempo, in-order"

# Exercise: a recipe-card printer.
CARD_ASPECTS = "card, index, full-page; layout, compact, spacious, two-column"

ORDERING_JAVA = """// The ordering algorithm is an object the playlist holds.
interface Ordering {
    List<Track> arrange(List<Track> tracks);
}
final class ByTempo implements Ordering {
    public List<Track> arrange(List<Track> tracks) {
        List<Track> out = new ArrayList<>(tracks);
        Collections.sort(out, Track.BY_BPM);
        return out;
    }
}
abstract class Playlist {
    private final List<Track> tracks = new ArrayList<>();
    private Ordering ordering;
    Playlist(Ordering ordering) { this.ordering = ordering; }
    void setOrdering(Ordering o) { this.ordering = o; }   // at run time
    List<Track> playOrder() { return ordering.arrange(tracks); }
}"""


# ---------------------------------------------------------------- 2.4 records

GUIDE_CORE = "guide, 6"
GUIDE_LAYERS = "headphones, add, 2; family, times, 3; donation, add, 1.5"
GUIDE_TWO_ADDS = "headphones, add, 2; donation, add, 1.5"

# Exercise: a theatre ticket.
TICKET_EXERCISE = """core:   ticket, 40
layers: booking-fee, add, 2.5; member, times, 0.8
        (innermost first)"""

CHARGE_JAVA = """// A charge, and decorators that enclose one charge each.
interface Charge {
    BigDecimal amount();
}
abstract class ChargeDecorator implements Charge {
    private final Charge inner;
    ChargeDecorator(Charge inner) { this.inner = inner; }
    public BigDecimal amount() { return inner.amount(); }   // forward
}
final class Family extends ChargeDecorator {
    Family(Charge inner) { super(inner); }
    public BigDecimal amount() {
        return super.amount().multiply(new BigDecimal("3"));   // after
    }
}
// new Donation(new Family(new Headphones(new GuideRental())))"""


# ---------------------------------------------------------------- 2.5 records

MAP_STYLES = "street satellite terrain"
MAP_KINDS = "tile label marker"

# Exercise: a quiz app's two modes.
QUIZ_EXERCISE = """families: kids adult
kinds:    question timer
a new kind of product: hint"""

MAP_FACTORY_JAVA = """// One factory per map style; the viewer never names a style's classes.
interface MapStyle {
    Tile createTile(int x, int y);
    Label createLabel(String text);
    Marker createMarker(Place p);
}
final class TerrainStyle implements MapStyle {
    public Tile createTile(int x, int y) { return new TerrainTile(x, y); }
    public Label createLabel(String t) { return new TerrainLabel(t); }
    public Marker createMarker(Place p) { return new TerrainMarker(p); }
}
final class MapViewer {
    private final MapStyle style;   // chosen once, at start-up
    MapViewer(MapStyle style) { this.style = style; }
    void show(Place p) {
        Marker m = style.createMarker(p);   // matches the tiles
        m.drawOn(style.createTile(p.tileX(), p.tileY()));
    }
}"""


# ---------------------------------------------------------------- 2.6 records

NOTICE_ASPECTS = "notice, overdue, hold-ready, renewal; channel, email, sms, app-push"
NOTICE_FOUR_CHANNELS = "notice, overdue, hold-ready, renewal; channel, email, sms, app-push, letter"

# Exercise: a shop's printing.
PRINT_ASPECTS = "document, receipt, label; printer, thermal, laser, inkjet, pdf"

NOTICE_BRIDGE_JAVA = """// The abstraction the library's code uses...
abstract class Notice {
    private final Channel channel;   // ...holds its implementation
    Notice(Channel channel) { this.channel = channel; }
    protected void deliver(String subject, String body) {
        channel.send(subject, body);
    }
    abstract void issue(Member m);
}
final class Overdue extends Notice {
    Overdue(Channel c) { super(c); }
    void issue(Member m) {
        deliver("Overdue", m.name() + ", please return " + m.oldestLoan());
    }
}
// ...which caters to the delivery services, not to the library.
interface Channel {
    void send(String subject, String body);
}"""


LESSONS = [
    # ---------------------------------------------------------------- 01
    # 2.1 Design Problems (PDF pp. 53-55 of the operator's copy) and 2.2
    # Document Structure (pp. 55-60): the seven problems, goals and
    # constraints, recursive composition, glyphs, Composite. Composite's
    # safety-transparency trade-off is from the pattern's Implementation
    # (p. 187).
    # Quote: PDF p. 56 of the operator's copy, 25 words, quotes.py OK.
    # Lesson total: 25 words.
    {
        "slug": "document-structure",
        "title": "Design Problems and Document Structure",
        "module": "Chapter 2 · A Case Study: Designing a Document Editor",
        "one_line": "Seven design problems in one editor, and the first of them solved by building the document from parts that can be treated the same as the whole.",
        "summary": (
            "Chapter 2 sets out seven design problems in Lexi, a WYSIWYG editor, and "
            "solves the first, how to represent a document, by recursive composition. "
            "Read why the authors want one interface for a single element and a group "
            "of them, then send one operation down a recipe book's tree and count the "
            "calls it makes and what it totals."
        ),
        "key": [
            "seven problems, one design",
            "build the complex out of the simple",
            "a part and a group share one interface",
            "draw, know your bounds, know your children",
            "a call on the root reaches every node",
            "where to declare add: safety or uniformity",
        ],
        "key_label": "Document structure in six lines",
        "concepts_intro": (
            "Three terms carry the lesson: the chapter's technique, its class, and "
            "the pattern the technique becomes."
        ),
        "concepts": [
            ("Recursive composition",
             "Building complex elements out of simpler ones, and those out of simpler "
             "ones again: a line out of letters and pictures, a column out of lines, a "
             "page out of columns. Each level is made of parts of the same general "
             "sort as itself."),
            ("Glyph",
             "Lexi's abstract class for anything that can appear in a document, from a "
             "single letter to a whole column. Every glyph can draw itself, report the "
             "space it occupies and whether a point falls inside it, and give access to "
             "its children and its parent."),
            ("Composite",
             "The pattern that recursive composition becomes: a common Component "
             "interface shared by Leaf objects and by Composite objects that hold other "
             "components, so that a client treats one part and a whole structure of "
             "parts in the same way. It has a lesson of its own, Composite, in "
             "Structural Patterns."),
        ],
        "read_title": "The seven problems, then the first of them",
        "read_intro": (
            "Read the opening of Chapter 2, section 2.1, Design Problems, and 2.2, "
            "Document Structure, in your own copy first. The lesson summarises Lexi's "
            "design in prose and counts the same shape on a recipe book."
        ),
        "body": [
            # PDF p. 56 of the operator's copy
            ("p", "&ldquo;A common way to represent hierarchically structured information "
                  "is through a technique called recursive composition, which entails "
                  "building increasingly complex elements out of simpler ones.&rdquo; That "
                  "is the technique Section 2.2 of Chapter 2, A Case Study: Designing a "
                  "Document Editor, settles on for its first problem. The chapter follows "
                  "one design, an editor called Lexi, from problem to pattern, and shows "
                  "eight of the catalog's patterns at work in it before the catalog "
                  "begins. Read sections 2.1 and 2.2 in your own copy first."),
            ("p", "Lexi is a WYSIWYG editor, showing the page as it will print and mixing text and pictures "
                  "freely, and the authors credit its design to Doc, an editor Calder "
                  "built. Section 2.1 lists seven problems the design has to solve: how "
                  "to represent the document; how to format it into lines and columns; "
                  "how to add and remove decorations such as borders and scroll bars; how "
                  "to support more than one look-and-feel standard; how to run on more "
                  "than one window system; how to give menus and buttons a single way to "
                  "reach scattered operations and undo them; and how to add analyses "
                  "such as spelling checking while changing as few classes as possible. "
                  "Each of the following sections, and each lesson of this course, takes "
                  "one problem: its goals and constraints first, then a design, then the "
                  "pattern the design is an instance of."),
            ("p", "The first problem touches everything else, because editing, "
                  "formatting, display and analysis all walk the document's "
                  "representation. The authors want the representation to match the "
                  "document's physical structure, the way its text and pictures are laid out "
                  "into lines, columns and tables, so that a user can treat a table or a "
                  "diagram as one thing. It has to hold that structure, draw it, and map "
                  "a point on the screen back to the element under it. Two constraints "
                  "follow. Text and graphics should be handled alike, with no second set "
                  "of mechanisms for either; and a single element and a group of "
                  "elements should be handled alike, so that the tenth thing in a line "
                  "may be one letter or an elaborate diagram without the line caring. "
                  "Against the second, the authors note at once, some analyses do care: "
                  "nobody checks the spelling of a polygon. That tension returns in the "
                  "last lesson."),
            ("p", "Recursive composition meets both constraints. Letters and pictures "
                  "are tiled into a line, lines stacked into a column, columns into a "
                  "page, and every element, visible or structural, is an object. That "
                  "has two implications the authors draw out: the objects need classes, "
                  "and the classes need compatible interfaces, which in C++ means a "
                  "common base class. A footnote adds a caution worth keeping: most "
                  "editors of the time did not use an object per character, presumably "
                  "for efficiency, and the authors point to Flyweight as the way to share "
                  "such objects, a lesson in Structural Patterns."),
            ("p", "The base class is Glyph. A glyph has three responsibilities: it draws "
                  "itself in a window; it knows the rectangle it occupies and whether a "
                  "point falls inside it, which is how a click finds its target; and it "
                  "knows its children and its parent, with operations to insert, remove "
                  "and fetch a child. A glyph that has children is asked to reach them "
                  "through its own child operation rather than through the list or array "
                  "that holds them, so that the container can change without touching "
                  "the operations that loop over it. The section closes by naming the "
                  "pattern, Composite, and sending the reader to it."),
            ("p", "Read as a tool, Composite has three roles: a Component interface, Leaf "
                  "classes with no children, and Composite classes that hold components "
                  "and pass an operation on to each one. The catalog lists the benefits, "
                  "a simple client and new kinds of component that work with existing "
                  "structures, and the cost: a design so general that the type system "
                  "can no longer restrict what goes inside a composite. Its "
                  "Implementation section adds a choice the lab counts. Declare the "
                  "child operations on every component, as Lexi's Glyph does, and every "
                  "part is treated alike, but a client can ask a leaf for a child it "
                  "cannot have; declare them on the composite only, and the compiler "
                  "catches that mistake, at the price of two interfaces. The authors "
                  "call these transparency and safety. The sketch below, a recipe book "
                  "in Java, takes the safe side."),
            ("code", _lines(BOOK_PART_JAVA)),
            ("p", "Now the count, on the recipe book rather than Lexi's pages. The preset "
                  "<code>recipe-book</code> has 10 nodes: 4 sections, which are the "
                  "composites, and 6 leaves, five recipes valued in minutes and a cover "
                  "photo valued at 0. One operation on the book, asking how long "
                  "everything takes, makes 10 calls: 1 from the client and 9 forwarded "
                  "by sections to their parts. It totals 345 minutes, and the table "
                  "gives each section's subtotal: breads 135, cakes 210, and the layer "
                  "cakes inside cakes 175. The depth is 3, from the book through cakes "
                  "and layer to a recipe. The photo answers the question too, with 0, "
                  "which is the uniform treatment of text and graphics in a number. The "
                  "preset also asks pitta and layer to add a child: layer does, and under "
                  "the safe declaration pitta's call does not compile."),
            ("p", "The preset <code>talk-outline</code> is a talk's slides, 7 nodes with "
                  "2 parts as composites and 5 leaves, one of them a video clip: 7 calls, "
                  "17.5 minutes, depth 2. It is set to the transparent declaration, and "
                  "asks the slide close and the part method to add a child. Method does; "
                  "close's call is accepted by the interface, and the slide must either "
                  "ignore it or fail at run time. Switch the declaration to safe and the "
                  "same request becomes a compile error. Which you want is the trade-off "
                  "the catalog leaves to you."),
            ("h3", "Exercise"),
            ("code", _lines(MIXTAPE)),
            ("p", "A mixtape, in the lab's record form: node, parent, kind, minutes. By "
                  "hand, count the calls one operation on <code>mix</code> makes and the "
                  "total it returns, and give the subtotal of <code>side-b</code>. Then "
                  "type the records into the lab to check."),
            ("p", "The structure is in place, but nothing yet says how a stream of parts "
                  "is broken into lines. The next lesson, Formatting, reads Section 2.3, "
                  "where the line-breaking algorithm becomes an object of its own."),
        ],
        "lab": ("gofkit", {
            "mode": "tree",
            "view": "compose",
            "preset": "recipe-book",
            "presets": [
                {"id": "recipe-book",
                 "label": "A recipe book in minutes, safe declaration",
                 "nodes": _records(RECIPE_BOOK),
                 "asks": "pitta layer",
                 "declare": "safe",
                 "expect": {"gtrNodes": "10",
                   "gtrLeaves": "6",
                   "gtrComposites": "4",
                   "gtrDepth": "3",
                   "gtrCalls": "10: 1 from the client + 9 forwarded by composites",
                   "gtrTotal": "345",
                   "gtrAskLeaves": "1: pitta (refused by the compiler: add is declared only on composites)",
                   "gtrAskTaken": "1: layer"}},
                {"id": "talk-outline",
                 "label": "A talk's slide outline, transparent declaration",
                 "nodes": _records(TALK_OUTLINE),
                 "asks": "close method",
                 "declare": "transparent",
                 "expect": {"gtrNodes": "7",
                   "gtrLeaves": "5",
                   "gtrComposites": "2",
                   "gtrDepth": "2",
                   "gtrCalls": "7: 1 from the client + 6 forwarded by composites",
                   "gtrTotal": "17.5",
                   "gtrAskLeaves": "1: close (accepted by the interface: each ignores it or fails at run time)",
                   "gtrAskTaken": "1: method"}},
            ],
            "panel_title": "One operation over a whole and its parts",
        }),
        "steps_title": "Counting one operation over a tree of parts",
        "steps_intro": "Four steps, the last of them on a structure of your own.",
        "steps": [
            ("Sort the nodes into leaves and composites",
             "A node with a value is a leaf; a node that holds others is a composite. "
             "Write each composite's children in the order given."),
            ("Count the calls",
             "One call from the client reaches the root; each composite then makes one "
             "call per child. The total is one call per node, whatever the shape."),
            ("Add the leaves",
             "The operation's result at the root is the sum of the leaf values, and "
             "each composite's subtotal is the sum of the leaves below it. A leaf worth "
             "0 still answers."),
            ("Do it on a structure of your own",
             "Take a folder tree, an organisation chart or a bill of materials you know "
             "and write five to ten of its parts as node, parent, kind, value. Count the "
             "calls and the total, and say which child operations you would declare on "
             "every part and which on the groups only."),
        ],
        "worked": {
            "title": "One question asked of a recipe book",
            "intro": [
                "Count the calls and the total on the preset <code>recipe-book</code>.",
            ],
            "lines": [
                "client → book: 1 call",
                "book → cover, breads, cakes: 3 calls",
                "breads → focaccia, pitta: 2 calls",
                "cakes → layer, flapjack: 2 calls",
                "layer → sponge, gateau: 2 calls",
                "calls: 1 + 3 + 2 + 2 + 2 = 10",
                "minutes: 0 + 95 + 40 + 55 + 120 + 35 = 345",
            ],
            "after": [
                "Every node receives exactly one call, so the count is the number of "
                "nodes. The client made one of them; it never needed to know that cakes "
                "holds a section inside it.",
            ],
        },
        "quiz_title": "Parts, wholes and the first design problem",
        "quiz": [
            {"q": "In the exercise, how many calls does one operation on <code>mix</code> "
                  "make, and what does it total?",
             "a": ["5 calls, totalling 21.5",
                   "8 calls, totalling 21.5",
                   "9 calls, totalling 21.5",
                   "9 calls, totalling 15.5"],
             "c": 2,
             "why": "There are 9 nodes, and each receives one call: 1 from the client to "
                    "mix and 8 forwarded by the four lists. The leaves are 3.5 + 4.25 + 5 "
                    "+ 2.75 + 6 = 21.5, and side-b's subtotal is 5 + 2.75 = 7.75. Five is "
                    "the number of tracks, eight leaves out the client's call, and 15.5 "
                    "forgets t5, the track that sits directly under mix."},
            {"q": "What three responsibilities does Section 2.2 give every glyph?",
             "a": ["Drawing itself, formatting its children into lines, and checking its "
                   "own spelling",
                   "Drawing itself, knowing the space it occupies, and knowing its "
                   "children and parent",
                   "Storing its character code, its font and its position on the page",
                   "Creating its children, decorating them, and undoing changes to them"],
             "c": 1,
             "why": "A glyph draws itself, knows its bounds (and whether a point falls "
                    "inside them), and knows its children and parent. Formatting is "
                    "given to a separate object in Section 2.3 and spelling checking to "
                    "another in 2.8, precisely to keep them out of the glyph classes; "
                    "character codes belong to the Character subclass alone."},
            {"q": "On the preset <code>recipe-book</code>, under the safe declaration, "
                  "pitta and layer are each asked to add a child. What happens?",
             "a": ["Both calls compile; pitta ignores its request",
                   "Neither call compiles, because add is declared only on the book",
                   "Layer adds the child; pitta's call does not compile",
                   "Both calls compile; pitta fails at run time"],
             "c": 2,
             "why": "Under the safe declaration add exists only on the composite class, "
                    "so layer, a section, takes the child and the call on pitta, a "
                    "recipe, is caught by the compiler. Compiling and then ignoring or "
                    "failing is what the transparent declaration allows, as on the "
                    "<code>talk-outline</code> preset. Every section, not just the root, "
                    "has add."},
            {"q": "Which constraint do the authors say pulls against treating single "
                  "elements and groups uniformly?",
             "a": ["Some analyses depend on the kind of element, such as checking "
                   "spelling",
                   "Graphics must be treated as a special case of text",
                   "Lines must never contain pictures",
                   "Each element must store its position on the page"],
             "c": 0,
             "why": "Section 2.2 notes that an analysis such as spelling checking or "
                    "hyphenation needs to tell a letter from a polygon, which the "
                    "uniform interface hides; Section 2.8 resolves it with Visitor. The "
                    "authors want text and graphics treated alike, not one as a case of "
                    "the other, and pictures in lines are exactly what recursive "
                    "composition allows."},
        ],
        "mistakes": [
            ("Writing one case for a single element and another for a group",
             "That is the design the second constraint of Section 2.2 rules out: the "
             "tenth element of a line may be a letter or a whole diagram, and the line "
             "should not have to ask. With one interface for leaves and composites, the "
             "client's single call reaches every part, as the lab's 10 calls on the "
             "recipe book show; with two, every client grows a type test."),
            ("Taking an object per character as the book's advice for any editor",
             "The authors note in a footnote that most editors of their day did not do "
             "it, presumably for efficiency, that Calder showed it could be done, and "
             "that Flyweight is the way to share such objects. Lexi's design is chosen "
             "for flexibility in an example; its cost is a question the reader still has "
             "to weigh."),
            ("Thinking uniform treatment means no operation may tell kinds apart",
             "Section 2.2 names the opposing constraint itself: spelling and hyphenation "
             "care whether a part is a letter. The chapter does not drop uniformity to "
             "meet it; Section 2.8 lets an analysis distinguish kinds without type "
             "tests, through Visitor."),
        ],
        "standard": (
            "Finish when you can count one operation over a tree of parts by hand.",
            "Given a tree as node, parent, kind and value, state its leaves, composites "
            "and depth, the calls one operation on the root makes and its total, and say "
            "what the safe and transparent declarations do with a leaf asked to add a "
            "child."
        ),
        "note": (
            "The lab counts calls and adds leaf values on the tree as stated; it does not "
            "add the children it is asked to add. It cannot say whether your structure "
            "should be a tree of objects at all, or whether one object per smallest part "
            "is affordable, which the authors themselves leave open."
        ),
    },
    # ---------------------------------------------------------------- 02
    # 2.3 Formatting (PDF pp. 60-63 of the operator's copy): representation
    # versus formatting, encapsulating the algorithm, Compositor and
    # Composition, Strategy. Strategy's consequences are from the pattern
    # (pp. 337-338).
    # Quote: PDF p. 61 of the operator's copy, 20 words, quotes.py OK.
    # Lesson total: 20 words.
    {
        "slug": "formatting",
        "title": "Formatting",
        "module": "Chapter 2 · A Case Study: Designing a Document Editor",
        "one_line": "The line-breaking algorithm taken out of the document classes and made an object, so that structures and algorithms can each be added without the other.",
        "summary": (
            "Section 2.3 separates how a document is represented from how it is broken "
            "into lines, and puts the algorithm in an object of its own: Compositor, "
            "held by a Composition. Read why, then count the classes a playlist app "
            "needs when every playlist and ordering pair is a subclass, against a "
            "playlist that holds its ordering."
        ),
        "key": [
            "representing is not formatting",
            "isolate the algorithm in an object",
            "a context holds its strategy",
            "new structures, old algorithms",
            "a product of subclasses, a sum of classes",
            "switch the algorithm while running",
        ],
        "key_label": "Formatting in six lines",
        "concepts_intro": (
            "Two terms are Lexi's; the third is the pattern they are an instance of."
        ),
        "concepts": [
            ("Compositor",
             "Lexi's class for an object that holds one line-breaking algorithm. It is "
             "told which glyphs to format and when, and each subclass breaks them into "
             "lines its own way: a quick pass, or a slower one that weighs how evenly "
             "text and space are spread."),
            ("Composition",
             "The glyph that holds a document's visible content and a compositor. When "
             "the content changes it asks its compositor to compose it, and the "
             "compositor inserts the row and column glyphs that make up the lines."),
            ("Strategy",
             "The pattern: several algorithms for one job, each in a "
             "ConcreteStrategy class behind one Strategy interface, used by a Context "
             "that holds one of them. It has a lesson of its own, Strategy, in "
             "Behavioral Patterns II."),
        ],
        "read_title": "Why formatting gets its own object",
        "read_intro": (
            "Read Section 2.3, Formatting, in your own copy first. The lesson follows "
            "its argument, then counts the classes the alternative would need on a "
            "playlist app of its own."
        ),
        "body": [
            # PDF p. 61 of the operator's copy
            ("p", "&ldquo;We can isolate the algorithm and make it easily replaceable at "
                  "the same time by encapsulating it in an object.&rdquo; That is the move "
                  "Section 2.3, Formatting, makes for Lexi's second problem. Read the "
                  "section in your own copy first; it is four pages, and the shortest "
                  "route in the chapter from a problem to a pattern."),
            ("p", "The section begins by separating two things. Recursive composition "
                  "says how a formatted document is held, but not how to get from a "
                  "stream of letters and pictures to the right lines and columns. That "
                  "is formatting, which the authors narrow for the section to line "
                  "breaking, noting that breaking lines into columns and columns into "
                  "pages works the same way. It is hard to do well, and there is no one "
                  "right algorithm: an interactive editor trades the quality of its "
                  "lines against the speed of its response, a user may accept slower "
                  "typing for better pages, and caching more can buy speed with memory. "
                  "Not all of that can be decided when the program is compiled."),
            ("p", "So the authors want two kinds of independence. A new kind of glyph "
                  "should not have to know about the formatting algorithm, and a new "
                  "algorithm should not require editing the existing glyphs. Their answer "
                  "is a separate class hierarchy for algorithms. Compositor's interface "
                  "says what to format and when; a Composition, a special glyph, holds "
                  "the unformatted content and a compositor, and asks it to compose "
                  "whenever the document changes. The compositor walks the composition's "
                  "children and inserts the row and column glyphs the lines need. One "
                  "subclass might make a quick pass; another might run Knuth's TeX "
                  "algorithm, which weighs the evenness of the text's colour and takes "
                  "longer. Add a single operation to set the compositor, and the "
                  "algorithm can be changed while Lexi runs."),
            ("p", "The pattern is Strategy: the compositor is the strategy, the "
                  "composition its context. The authors put the weight on one point, "
                  "that the two interfaces must be general enough for any algorithm in "
                  "the family; here the glyph's child operations already let any "
                  "compositor rebuild the lines, and the compositor's interface gives "
                  "the composition all it needs to ask. The pattern's own consequences, "
                  "in the catalog, add the costs: a client must know how the strategies "
                  "differ in order to choose one, the context and strategy may pass "
                  "each other more than a given algorithm uses, and there are more "
                  "objects. Strategy reappears as a concept of the domain in the "
                  "Domain-Driven Design lesson Strategy and Composite in the Model."),
            ("code", _lines(ORDERING_JAVA)),
            ("p", "The sketch is a playlist app with the same shape: kinds of playlist, "
                  "like kinds of composition, and ordering algorithms, like compositors. "
                  "The lab compares it with the design Section 2.3 avoids, where each "
                  "pairing is its own subclass. On the preset "
                  "<code>playlist-orderings</code>, 3 kinds of playlist and 4 orderings "
                  "make 3 × 4 = 12 combinations, so one subclass per combination needs "
                  "12 + 1 = 13 classes with the abstract base. Two hierarchies joined by "
                  "a reference need (3 + 1) + (4 + 1) = 9: an abstract class and its "
                  "concrete classes on each side. The ratio tile reads 13/9 ≈ 1.4×, and "
                  "the references tile says each playlist holds one reference, to its "
                  "ordering. The preset adds a fifth ordering: 3 more subclasses, one for "
                  "each kind of playlist (13 → 16), against 1 more class (9 → 10)."),
            ("p", "The preset <code>new-playlist-kind</code> adds a kind of playlist "
                  "instead. Under subclassing that is 4 new classes, one per ordering "
                  "(13 → 17); under composition, 1 (9 → 10), and no ordering is touched. "
                  "That is the section's two independences as counts: a new structure "
                  "without regard to the algorithms, and the other way round. What the "
                  "count leaves out is the run-time switch. A combined subclass cannot "
                  "change its algorithm without becoming a different object; a playlist "
                  "that holds an ordering is handed a new one."),
            ("h3", "Exercise"),
            ("code", [CARD_ASPECTS]),
            ("p", "A recipe-card printer, as the lab's aspects: two kinds of card and three "
                  "layout algorithms. By hand, count the classes under each design and "
                  "the classes a fourth layout adds to each, and say what the ratio "
                  "shows. Then type the line into the lab, with layout as the aspect that "
                  "gains a variant."),
            ("p", "A playlist holds one ordering. The next lesson, Embellishing the User "
                  "Interface, reads Section 2.4, where an object holds another of its own "
                  "kind and adds to what it does."),
        ],
        "lab": ("gofkit", {
            "mode": "classes",
            "view": "explosion",
            "preset": "playlist-orderings",
            "presets": [
                {"id": "playlist-orderings",
                 "label": "A playlist app: three playlists, four orderings, a fifth ordering",
                 "aspects": PLAYLIST_ASPECTS,
                 "added": "ordering",
                 "expect": {"gclCombos": "3 × 4 = 12",
                   "gclSubclass": "12 + 1 = 13",
                   "gclCompose": "(3 + 1) + (4 + 1) = 9",
                   "gclRatio": "13/9 ≈ 1.4×",
                   "gclRefs": "1: ordering",
                   "gclAddSubclass": "3 (13 → 16)",
                   "gclAddCompose": "1 (9 → 10)"}},
                {"id": "new-playlist-kind",
                 "label": "The same app, adding a kind of playlist",
                 "aspects": PLAYLIST_ASPECTS,
                 "added": "playlist",
                 "expect": {"gclCombos": "3 × 4 = 12",
                   "gclSubclass": "12 + 1 = 13",
                   "gclCompose": "(3 + 1) + (4 + 1) = 9",
                   "gclRatio": "13/9 ≈ 1.4×",
                   "gclRefs": "1: ordering",
                   "gclAddSubclass": "4 (13 → 17)",
                   "gclAddCompose": "1 (9 → 10)"}},
            ],
            "panel_title": "Structures and algorithms: subclasses against a held strategy",
        }),
        "steps_title": "Counting the classes an algorithm costs",
        "steps_intro": "Four steps, the last of them on a design of your own.",
        "steps": [
            ("Name the two things that vary",
             "Write the structure that does the work (the context) and the algorithm it "
             "uses, each with its variants."),
            ("Count one subclass per pairing",
             "Multiply the variant counts and add 1 for the abstract base. That is the "
             "design in which each structure is hard-wired to one algorithm."),
            ("Count two hierarchies",
             "Add the variant counts, and 1 abstract class for each side. A new variant "
             "on either side adds 1 class; under subclassing it adds one per variant of "
             "the other side."),
            ("Do it on a design of your own",
             "Find a class in your own code that chooses an algorithm by a flag or by "
             "being subclassed: a sort order, a pricing rule, a retry policy. Write its "
             "aspects, count both designs, and say whether the algorithm ever needs to "
             "change on a live object."),
        ],
        "worked": {
            "title": "Three playlists, four orderings",
            "intro": [
                "Count both designs on the preset <code>playlist-orderings</code>.",
            ],
            "lines": [
                "pairings: 3 × 4 = 12",
                "subclassing: 12 + 1 = 13 classes",
                "composition: (3 + 1) + (4 + 1) = 9 classes",
                "a fifth ordering, subclassing: +3 (13 → 16)",
                "a fifth ordering, composition: +1 (9 → 10)",
            ],
            "after": [
                "The subclass count is a product and the composed one a sum, so the gap "
                "grows with each variant. The playlist classes are untouched by the new "
                "ordering under either design; what differs is how many classes it takes "
                "to offer it.",
            ],
        },
        "quiz_title": "Compositors, compositions and the classes they save",
        "quiz": [
            {"q": "In the exercise, two kinds of card and three layouts: how many classes "
                  "does each design need, and how many does a fourth layout add to each?",
             "a": ["7 and 7; a fourth layout adds 2 under subclassing and 1 under "
                   "composition",
                   "6 and 5; a fourth layout adds 2 and 1",
                   "7 and 7; a fourth layout adds 1 to each",
                   "7 and 5; a fourth layout adds 3 and 1"],
             "c": 0,
             "why": "Subclassing needs 2 × 3 = 6 combinations plus 1 base, 7; composition "
                    "needs (2 + 1) + (3 + 1) = 7, so the ratio is exactly 1×. A fourth "
                    "layout adds one subclass per kind of card, 2 (7 → 9), against 1 "
                    "(7 → 8). Six forgets the abstract base and five the abstract class "
                    "on each side. At this size the designs cost the same; the difference "
                    "shows in each addition and in switching layouts at run time."},
            {"q": "According to Section 2.3, which object inserts the rows and columns "
                  "into a Composition?",
             "a": ["The Composition itself, in its draw operation",
                   "Its Compositor, when the Composition asks it to compose",
                   "Each glyph, when it is inserted into the document",
                   "The window, when it redraws the page"],
             "c": 1,
             "why": "An unformatted composition holds only the visible glyphs; when it "
                    "needs formatting it calls its compositor, which walks the children "
                    "and inserts the row and column glyphs by its own algorithm. Keeping "
                    "that work out of the composition and the glyphs is the point of the "
                    "split."},
            {"q": "On the preset <code>new-playlist-kind</code>, a fourth kind of "
                  "playlist is added. What does the lab count?",
             "a": ["3 classes added under subclassing, 1 under composition",
                   "4 classes added under subclassing, 4 under composition",
                   "4 classes added under subclassing, 1 under composition",
                   "1 class added under each design"],
             "c": 2,
             "why": "Under subclassing a new kind of playlist needs one class per ordering, "
                    "4 (13 → 17). Under composition it is one new playlist class (9 → 10), "
                    "which uses the existing orderings. Three is what a new ordering adds, "
                    "one per kind of playlist, on the other preset."},
            {"q": "Which of these does the catalog list as a drawback of Strategy?",
             "a": ["A client must understand how the strategies differ to choose one",
                   "The algorithm can no longer be changed at run time",
                   "Each new algorithm requires editing the context class",
                   "The context must test the type of its strategy"],
             "c": 0,
             "why": "Strategy's consequences include that clients must be aware of the "
                    "strategies, a possible communication overhead between strategy and "
                    "context, and more objects. Changing the algorithm at run time, adding "
                    "one without editing the context, and avoiding type tests are among "
                    "its benefits."},
        ],
        "mistakes": [
            ("Putting the formatting algorithm inside the document classes",
             "Section 2.3 wants a new glyph to need no knowledge of formatting and a new "
             "algorithm to need no change to the glyphs; an algorithm written into the "
             "structure classes gives neither. On the lesson's playlist app the lab "
             "counts what it costs when each pairing is a subclass instead: 13 classes "
             "against 9, and 3 more for every new ordering against 1."),
            ("Treating Strategy as free",
             "The catalog lists its costs beside its benefits: the client has to know the "
             "strategies apart to pick one, a general interface may pass data a simple "
             "algorithm never uses, and there are more objects. With two kinds and three "
             "algorithms, as in the exercise, the class count does not fall at all."),
            ("Designing the strategy interface around the first algorithm",
             "The authors put the key to Strategy in interfaces general enough for the "
             "whole family, so that a new algorithm changes neither the strategy's nor "
             "the context's interface. Lexi's compositors can rebuild the lines because "
             "the glyph's child operations are general; an interface shaped by one "
             "algorithm would have to change for the next."),
        ],
        "standard": (
            "Finish when you can count what an algorithm costs as subclasses and as an object.",
            "Given a structure and an algorithm that vary, state the classes under one "
            "subclass per pairing and under two hierarchies, what one new variant of "
            "either adds, and what Strategy's catalog entry lists as its costs."
        ),
        "note": (
            "The lab counts classes on the aspects as stated, as if every pairing "
            "differs. It cannot say whether your algorithm will ever vary, or whether "
            "switching it at run time matters; the authors' case rests on what in Lexi "
            "is expected to change."
        ),
    },
    # ---------------------------------------------------------------- 03
    # 2.4 Embellishing the User Interface (PDF pp. 63-67 of the operator's
    # copy): transparent enclosure, MonoGlyph, Border and Scroller, the order
    # of composition, Decorator. Decorator's consequences are from the
    # pattern (p. 198).
    # Quote: PDF p. 64 of the operator's copy, 24 words, quotes.py OK.
    # Lesson total: 24 words.
    {
        "slug": "embellishing-the-interface",
        "title": "Embellishing the User Interface",
        "module": "Chapter 2 · A Case Study: Designing a Document Editor",
        "one_line": "Borders and scroll bars added by wrapping an object in another with the same interface, so they can be stacked, reordered and removed without subclasses.",
        "summary": (
            "Section 2.4 adds a border and scroll bars to Lexi's page without a subclass "
            "for each combination, by enclosing one glyph in another that looks the same "
            "to its clients. Read the idea of transparent enclosure, then wrap an audio "
            "guide's rental charge in decorators and count the call order, the result, "
            "and what changes when the order does."
        ),
        "key": [
            "enclose one component, same interface",
            "work before or after forwarding",
            "clients cannot tell the enclosure",
            "order of wrapping is a design choice",
            "2ⁿ subclasses, or n + 3 classes",
            "many little objects that look alike",
        ],
        "key_label": "Embellishment in six lines",
        "concepts_intro": (
            "The section's idea, Lexi's class for it, and the pattern it leads to."
        ),
        "concepts": [
            ("Transparent enclosure",
             "Two ideas together: an object that encloses exactly one component, and an "
             "interface identical to that component's. Clients cannot tell the two apart; "
             "the enclosure forwards each request and may do work of its own before or "
             "after, or hold state the component lacks."),
            ("MonoGlyph",
             "Lexi's abstract class for embellishing glyphs. It holds one component glyph "
             "and forwards every operation to it, so that a subclass such as a border or "
             "a scroller overrides only what it adds to."),
            ("Decorator",
             "The pattern: a Decorator conforms to the Component interface, holds one "
             "component, and adds responsibilities around the requests it forwards; "
             "ConcreteDecorators can be stacked in any order. It has a lesson of its "
             "own, Decorator, in Structural Patterns."),
        ],
        "read_title": "Embellishment without a subclass for every combination",
        "read_intro": (
            "Read Section 2.4, Embellishing the User Interface, in your own copy first. "
            "The lesson follows its argument and then counts a stack of decorators on a "
            "rental charge."
        ),
        "body": [
            # PDF p. 64 of the operator's copy
            ("p", "&ldquo;All this leads us to the concept of transparent enclosure, which "
                  "combines the notions of (1) single-child (or single-component) "
                  "composition and (2) compatible interfaces.&rdquo; Section 2.4, "
                  "Embellishing the User Interface, arrives at that concept by asking "
                  "how to put a border and scroll bars around Lexi's page. Read the "
                  "section in your own copy first."),
            ("p", "The authors want the embellishments easy to add and remove, even "
                  "while the program runs, and invisible to the rest of the interface. "
                  "Inheritance fails both tests. A bordered composition is a subclass, a "
                  "scrollable one another, and one with both a third; carry that on and "
                  "there is a class for every combination of embellishments, which grows "
                  "out of hand as embellishments are added, and none of them can be "
                  "rearranged at run time. Object composition is the alternative, which "
                  "leaves the question of who holds whom. If the glyph held its border, "
                  "every glyph class would have to know about borders; if the border "
                  "holds the glyph, the drawing of borders stays in one class."),
            ("p", "Then comes the step that makes it transparent. A border has an "
                  "appearance, so it can be a glyph; more to the point, clients should "
                  "not care whether a glyph has a border. If Border is a subclass of "
                  "Glyph, a client tells a bordered glyph to draw exactly as it told the "
                  "plain one. The enclosure can forward everything, or add work before or "
                  "after forwarding, or keep state of its own. Lexi gathers this in "
                  "MonoGlyph, an abstract glyph holding one component and forwarding "
                  "every request to it. A border's draw operation forwards first, so "
                  "the component draws itself, and then draws the border: it extends the "
                  "forwarded operation rather than replacing it. A scroller draws its "
                  "component offset by the scroll bars' positions and clipped to its "
                  "bounds."),
            ("p", "Lexi's page puts the composition inside a scroller and the scroller "
                  "inside a border. The authors point out that the order can be reversed: "
                  "put the border inside the scroller, and the border scrolls with the "
                  "text, which a designer may or may not want. They also insist that an "
                  "embellishment encloses one glyph, never several; grouping is already "
                  "the job of rows and columns, and mixing it into embellishment would "
                  "duplicate it. The pattern is Decorator, in which embellishment means "
                  "any added responsibility, not only a visual one. Its catalog entry is "
                  "fair about the costs: a decorated object is not the same object as the "
                  "one inside it, so code that compares identities can be fooled, and a "
                  "design built of many small, similar decorators can be easy to "
                  "configure and hard to learn and debug."),
            ("code", _lines(CHARGE_JAVA)),
            ("p", "The lab works a rental charge at a museum's audio-guide desk instead of "
                  "a page. On the preset <code>guide-rental</code> the component is a "
                  "guide at 6, and three decorators wrap it, innermost first: headphones "
                  "adds 2, family multiplies by 3, and a donation adds 1.5. A request "
                  "goes in through donation, family and headphones to the guide and comes "
                  "back out the other way, and each decorator does its work on the way "
                  "out, as Lexi's border draws after its component: (6 + 2) × 3 + 1.5 = "
                  "25.5. Reversed, with the donation innermost, it is (6 + 1.5) × 3 + 2 "
                  "= 24.5, so the order matters. Every combination of three options as "
                  "its own subclass would be 8 classes, the plain guide and 7 "
                  "combinations; with Decorator, 6: the interface, the guide, the "
                  "abstract decorator and 3 decorators. A fourth option would add 8 "
                  "subclasses against 1 decorator."),
            ("p", "The preset <code>family-first</code> keeps the same three decorators and "
                  "compares another order, family innermost: 6 × 3 + 2 + 1.5 = 21.5. The "
                  "preset <code>two-adds</code> drops the family rate, and both orders "
                  "give 9.5, because two additions commute; the order of decorators "
                  "changes a result only when their operations do not. The class counts "
                  "become 4 against 5, so with two options Decorator costs a class more "
                  "than the subclasses, since the subclass design needs no separate "
                  "interface; it is the growth, 2ⁿ against n + 3, and the "
                  "freedom to rearrange at run time that the authors argue from."),
            ("h3", "Exercise"),
            ("code", _lines(TICKET_EXERCISE)),
            ("p", "A theatre ticket, as the lab's core and layers. By hand, give the result "
                  "with the layers as listed and in the reverse order, and the call order "
                  "a request follows. Then type the two fields into the lab to check."),
            ("p", "Every embellishment so far is one of Lexi's own classes. The next "
                  "lesson, Supporting Multiple Look-and-Feel Standards, reads Section 2.5, "
                  "where whole sets of classes must be swapped at once."),
        ],
        "lab": ("gofkit", {
            "mode": "route",
            "view": "wrap",
            "preset": "guide-rental",
            "core": GUIDE_CORE,
            "presets": [
                {"id": "guide-rental",
                 "label": "An audio-guide rental: headphones, a family rate, a donation",
                 "layers": GUIDE_LAYERS,
                 "expect": {"grtLayers": "3",
                   "grtCalls": "in: donation, family, headphones; core: guide; out: headphones, family, donation",
                   "grtResult": "25.5",
                   "grtOther": "24.5",
                   "grtMatters": "yes",
                   "grtSubclass": "8 (the component + 7 combinations)",
                   "grtDecorator": "6 (interface, component, abstract decorator + 3)",
                   "grtAddOne": "subclassing +8, Decorator +1"}},
                {"id": "family-first",
                 "label": "The same rental, compared with the family rate innermost",
                 "layers": GUIDE_LAYERS,
                 "order": "family headphones donation",
                 "expect": {"grtLayers": "3",
                   "grtCalls": "in: donation, family, headphones; core: guide; out: headphones, family, donation",
                   "grtResult": "25.5",
                   "grtOther": "21.5",
                   "grtMatters": "yes",
                   "grtSubclass": "8 (the component + 7 combinations)",
                   "grtDecorator": "6 (interface, component, abstract decorator + 3)",
                   "grtAddOne": "subclassing +8, Decorator +1"}},
                {"id": "two-adds",
                 "label": "Headphones and a donation only, where order does not matter",
                 "layers": GUIDE_TWO_ADDS,
                 "expect": {"grtLayers": "2",
                   "grtCalls": "in: donation, headphones; core: guide; out: headphones, donation",
                   "grtResult": "9.5",
                   "grtOther": "9.5",
                   "grtMatters": "no",
                   "grtSubclass": "4 (the component + 3 combinations)",
                   "grtDecorator": "5 (interface, component, abstract decorator + 2)",
                   "grtAddOne": "subclassing +4, Decorator +1"}},
            ],
            "panel_title": "A component wrapped in decorators",
        }),
        "steps_title": "Reading a stack of decorators",
        "steps_intro": "Four steps, the last of them on a design of your own.",
        "steps": [
            ("List the layers innermost first",
             "Write the component, then each decorator in the order it wraps: the first "
             "one listed encloses the component directly."),
            ("Trace the call in and out",
             "A request enters at the outermost decorator and passes inward to the "
             "component; the results come back out in the reverse order, each decorator "
             "applying its work as the result passes."),
            ("Swap the order and compare",
             "Apply the same layers in another order. If every operation is an addition, "
             "nothing changes; mix a multiplication in and the result moves."),
            ("Do it on a design of your own",
             "Find a feature in your own code that is switched on by options: logging, "
             "caching, retries, compression around a stream. Count the classes if each "
             "combination were a subclass (2ⁿ with n options), against n + 3 with "
             "Decorator, and say which orders of the options would behave differently."),
        ],
        "worked": {
            "title": "Three decorators on an audio-guide rental",
            "intro": [
                "Trace the preset <code>guide-rental</code>.",
            ],
            "lines": [
                "in: donation → family → headphones → guide",
                "guide: 6",
                "headphones: 6 + 2 = 8",
                "family: 8 × 3 = 24",
                "donation: 24 + 1.5 = 25.5",
                "reversed: (6 + 1.5) × 3 + 2 = 24.5",
            ],
            "after": [
                "Each decorator sees only the charge inside it and the same interface on "
                "both sides. The client holds the outermost one and asks it the same "
                "question it would ask a plain guide.",
            ],
        },
        "quiz_title": "Enclosures, their order and their cost",
        "quiz": [
            {"q": "In the exercise, what does the ticket cost with the layers as listed, "
                  "and in the reverse order?",
             "a": ["34 as listed, 34.5 reversed",
                   "34.5 as listed, 34 reversed",
                   "34 both ways",
                   "42.5 as listed, 32 reversed"],
             "c": 0,
             "why": "As listed the booking fee is innermost: (40 + 2.5) × 0.8 = 34. "
                    "Reversed, the member rate applies to the ticket alone and the fee "
                    "is added after: 40 × 0.8 + 2.5 = 34.5. The request enters at member "
                    "and reaches the ticket through booking-fee. 42.5 and 32 are each "
                    "layer applied alone; the swapped answer reads the list outermost "
                    "first."},
            {"q": "In Section 2.4, why do the authors make Border a subclass of Glyph?",
             "a": ["So that a border can hold several glyphs at once",
                   "So that clients treat a bordered glyph exactly as a plain one",
                   "So that every glyph class can draw its own border",
                   "So that the border can be chosen when the program is compiled"],
             "c": 1,
             "why": "The compelling reason they give is that clients should not care "
                    "whether a glyph has a border, which requires the border's interface "
                    "to match the glyph's. They insist an embellishment encloses one "
                    "glyph, keep the drawing of borders out of the other glyph classes, "
                    "and want borders added and removed at run time."},
            {"q": "On the preset <code>two-adds</code>, how many classes does each design "
                  "need, and does the order change the result?",
             "a": ["4 with subclasses, 5 with Decorator; the order does not change it",
                   "3 with subclasses, 4 with Decorator; the order does not change it",
                   "4 with subclasses, 5 with Decorator; the order changes it",
                   "4 with subclasses, 4 with Decorator; the order does not change it"],
             "c": 0,
             "why": "Two on-off options give 2² = 4 classes as subclasses: the plain "
                    "component and 3 combinations. Decorator needs 2 + 3 = 5: the "
                    "interface, the component, the abstract decorator and 2 decorators. "
                    "Both layers add, so either order gives 6 + 2 + 1.5 = 9.5. Three "
                    "leaves out the plain component; four for Decorator leaves out the "
                    "interface."},
            {"q": "Which liability does Decorator's catalog entry name?",
             "a": ["A decorator cannot be removed once attached",
                   "Each new decorator requires changing the component class",
                   "A decorated object is not identical to the object inside it",
                   "Decorators can only be stacked one deep"],
             "c": 2,
             "why": "The catalog warns that object identity cannot be relied on, since "
                    "the decorator and its component are different objects, and that "
                    "many small decorators can be hard to learn and debug. Attaching and "
                    "detaching at run time, adding decorators without touching the "
                    "component, and stacking them, even the same one twice, are its "
                    "benefits."},
        ],
        "mistakes": [
            ("Adding each optional feature as a subclass",
             "Section 2.4 shows where that goes: a bordered class, a scrollable class, a "
             "bordered scrollable class, one for every combination, none rearrangeable "
             "at run time. On the lesson's rental the lab counts 8 classes for three "
             "options and 16 for four, against 6 and 7 with Decorator."),
            ("Assuming the order of decorators never matters",
             "The authors point out that a border inside the scroller scrolls with the "
             "text and one outside it does not. On the lab's rental the same three "
             "decorators give 25.5, 24.5 or 21.5 depending on the order; only "
             "operations that commute, like the two additions, make the order "
             "irrelevant."),
            ("Making one decorator enclose several components",
             "The authors keep embellishment to a single component, because grouping is "
             "already done by rows and columns and mixing the two would duplicate it. A "
             "decorator that holds several objects is no longer transparent: it is a "
             "composite with something added."),
        ],
        "standard": (
            "Finish when you can trace a stack of decorators and count its classes.",
            "Given a component and its decorators innermost first, state the call order, "
            "the result in that order and another, whether the order matters, and the "
            "classes as subclasses against Decorator."
        ),
        "note": (
            "The lab applies each decorator's operation as the result passes outward and "
            "counts classes by the formulas it states. It cannot say whether a reordering "
            "is a fault or a feature, as the authors leave the scrolling border to taste, "
            "nor whether many small objects will be easy for your team to follow."
        ),
    },
    # ---------------------------------------------------------------- 04
    # 2.5 Supporting Multiple Look-and-Feel Standards (PDF pp. 67-71 of the
    # operator's copy): abstracting object creation, factories and product
    # classes, where the factory comes from, Abstract Factory. Abstract
    # Factory's consequences are from the pattern (pp. 109-110).
    # Quote: PDF p. 68 of the operator's copy, 32 words, quotes.py OK.
    # Lesson total: 32 words.
    {
        "slug": "look-and-feel",
        "title": "Supporting Multiple Look-and-Feel Standards",
        "module": "Chapter 2 · A Case Study: Designing a Document Editor",
        "one_line": "Every product of one family made by one factory object, so that the code never names a family's classes and a whole family can be swapped at once.",
        "summary": (
            "Section 2.5 makes Lexi follow more than one look-and-feel standard by "
            "creating every widget through a factory object instead of a constructor. "
            "Read why direct construction fails, then count the classes a map viewer's "
            "styles need under Abstract Factory, and what a new style and a new kind of "
            "product each add and change."
        ),
        "key": [
            "never name a concrete class to create",
            "a factory makes a family of products",
            "choose the factory once, at start-up",
            "swap a family by swapping the factory",
            "a new family edits nothing",
            "a new kind edits every factory",
        ],
        "key_label": "Abstract Factory in six lines",
        "concepts_intro": (
            "Two terms are the section's; the third is the pattern."
        ),
        "concepts": [
            ("Factory",
             "An object whose job is to create other objects. Lexi asks a factory for a "
             "scroll bar or a button instead of calling a constructor, and the factory "
             "returns one of the right style without the caller naming that style."),
            ("Product family",
             "A set of related products made to be used together, such as every widget "
             "of one look and feel. Each kind of product has an abstract class, and each "
             "family a concrete class for every kind."),
            ("Abstract Factory",
             "The pattern: an AbstractFactory declares one creation operation per kind of "
             "AbstractProduct, each ConcreteFactory makes one family's ConcreteProducts, "
             "and the client uses only the abstract interfaces. It has a lesson of its "
             "own, Abstract Factory, in Creational Patterns."),
        ],
        "read_title": "Abstracting how objects are made",
        "read_intro": (
            "Read Section 2.5, Supporting Multiple Look-and-Feel Standards, in your own "
            "copy first. The lesson follows its argument and counts the same shape on a "
            "map viewer's styles."
        ),
        "body": [
            # PDF p. 68 of the operator's copy
            ("p", "&ldquo;Littering our code with constructor calls to specific "
                  "look-and-feel classes yields a maintenance nightmare—miss just one, and "
                  "you could end up with a Motif menu in the middle of your Mac "
                  "application.&rdquo; Section 2.5, Supporting Multiple Look-and-Feel "
                  "Standards, is the authors' way out of that nightmare. Read it in your "
                  "own copy first."),
            ("p", "A look-and-feel standard is a style guide for how an application's "
                  "controls look and respond, and each platform of the early 1990s had "
                  "its own: Motif on Unix workstations, Presentation Manager on OS/2, the "
                  "Macintosh's. The standards differ in detail rather than in kind, but a "
                  "program that runs on several must follow each one where it runs, "
                  "should take new ones easily, and ideally could change style while "
                  "running. Lexi assumes two layers of widget classes: an abstract class "
                  "per kind of widget, such as a scroll bar or a button, and under "
                  "each a concrete class for each standard."),
            ("p", "The obstacle is construction. Code that creates a widget with a "
                  "constructor names one standard's class, which fixes the style when the "
                  "program is compiled and scatters that choice over every place a "
                  "widget is made; porting means finding them all. The authors' answer "
                  "is to abstract creation itself. Instead of constructing a Motif scroll "
                  "bar, Lexi asks a factory object for a scroll bar, and a Motif factory "
                  "returns a Motif one. Nothing in the calling code names Motif. The "
                  "factory's abstract class declares one creation operation for each "
                  "kind of widget, and each standard has a concrete factory that "
                  "implements all of them; the widgets one factory makes belong together, "
                  "which is what the authors mean by a product family."),
            ("p", "Where does the factory come from? Anywhere convenient, the authors "
                  "say: a global, a static member, a local variable, or a Singleton, a "
                  "pattern for well-known single objects that has a lesson in Creational "
                  "Patterns. What matters is that it is set after the style is known and "
                  "before the first widget is made, by assignment if the style is fixed "
                  "at compile time, or from a name given at start-up. A registry from "
                  "names to factories lets new factories be added without editing that "
                  "choice, and spares linking a factory for a platform that cannot run "
                  "it. Once set, the factory fixes the look and feel; to change it, the "
                  "program installs another factory and rebuilds its interface."),
            ("p", "The pattern is Abstract Factory, which the section says suits a design "
                  "whose kinds of product are settled while its families vary. Its "
                  "catalog entry states the other side plainly: supporting a new kind of "
                  "product is hard, because the abstract factory's interface fixes the "
                  "set of products, and adding one means changing that class and every "
                  "concrete factory. The lab counts both kinds of change."),
            ("code", _lines(MAP_FACTORY_JAVA)),
            ("p", "The sketch is a map viewer with three styles, street, satellite and "
                  "terrain, each a family of three kinds of product: tiles, labels and "
                  "markers drawn to match. On the preset <code>map-styles</code> there "
                  "are 3 × 3 = 9 concrete products, and the design has 1 + 3 + 3 + 9 = "
                  "16 classes: the abstract factory, a concrete factory per style, an "
                  "abstract class per kind and the nine concrete products. The classes "
                  "that create are 1 + 3 = 4. The preset <code>new-style</code> adds a "
                  "fourth style: 4 classes, one factory and its three products (16 → "
                  "20), and no existing class is edited. The preset "
                  "<code>new-kind</code> adds a fourth kind of product instead, a "
                  "compass rose: 4 classes again, one abstract product and one product "
                  "per style, but now 4 existing classes are edited, the abstract "
                  "factory and each of its 3 concrete factories, each given an "
                  "operation to make the new kind. Same number added, different "
                  "number changed: that is the asymmetry the pattern lives with. The "
                  "scheme menu also offers Factory Method and Prototype, and the "
                  "configuration tiles count Prototype's sets of instances; both "
                  "schemes are counted in Creational Patterns, and on this lesson only "
                  "Abstract Factory is Lexi's."),
            ("h3", "Exercise"),
            ("code", _lines(QUIZ_EXERCISE)),
            ("p", "A quiz app with a kids' mode and an adult mode, each a family of "
                  "questions and timers. By hand, count the classes under Abstract "
                  "Factory, then the classes a new kind of product, hints, adds and the "
                  "existing classes it edits. Then type the families and kinds into the "
                  "lab with the change set to a new kind."),
            ("p", "Abstract Factory assumes the products' classes are yours to write. The "
                  "next lesson, Supporting Multiple Window Systems, reads Section 2.6, "
                  "where they are not."),
        ],
        "lab": ("gofkit", {
            "mode": "classes",
            "view": "factory",
            "preset": "map-styles",
            "families": MAP_STYLES,
            "kinds": MAP_KINDS,
            "scheme": "abstract-factory",
            "presets": [
                {"id": "map-styles",
                 "label": "A map viewer: three styles, three kinds of product",
                 "change": "none",
                 "expect": {"gclProducts": "3 × 3 = 9",
                   "gclClasses": "1 + 3 + 3 + 9 = 16",
                   "gclFactories": "1 + 3 = 4",
                   "gclConfigs": "none: the factory classes themselves fix what is made",
                   "gclAdded": "no change chosen",
                   "gclChanged": "no change chosen",
                   "gclConfigChange": "no change chosen"}},
                {"id": "new-style",
                 "label": "The map viewer gains a fourth style",
                 "change": "family",
                 "expect": {"gclProducts": "3 × 3 = 9",
                   "gclClasses": "1 + 3 + 3 + 9 = 16",
                   "gclFactories": "1 + 3 = 4",
                   "gclConfigs": "none: the factory classes themselves fix what is made",
                   "gclAdded": "4 (16 → 20): 1 concrete factory, 3 concrete products",
                   "gclChanged": "0",
                   "gclConfigChange": "none: this scheme configures no prototypes"}},
                {"id": "new-kind",
                 "label": "The map viewer gains a fourth kind of product",
                 "change": "kind",
                 "expect": {"gclProducts": "3 × 3 = 9",
                   "gclClasses": "1 + 3 + 3 + 9 = 16",
                   "gclFactories": "1 + 3 = 4",
                   "gclConfigs": "none: the factory classes themselves fix what is made",
                   "gclAdded": "4 (16 → 20): 1 abstract product, 3 concrete products",
                   "gclChanged": "4: the abstract factory and 3 concrete factories, each given an operation to make the new kind",
                   "gclConfigChange": "none: this scheme configures no prototypes"}},
            ],
            "panel_title": "Families and kinds of product, under Abstract Factory",
        }),
        "steps_title": "Counting a family of factories",
        "steps_intro": "Four steps, the last of them on a design of your own.",
        "steps": [
            ("Name the families and the kinds",
             "A family is a set of products that must be used together; a kind is one "
             "slot every family fills. Write F families and K kinds."),
            ("Count the classes",
             "1 abstract factory, F concrete factories, K abstract products and F × K "
             "concrete products: 1 + F + K + F × K."),
            ("Count each change",
             "A new family adds 1 factory and K products and edits nothing. A new kind "
             "adds 1 abstract product and F products and edits the abstract factory and "
             "all F concrete ones."),
            ("Do it on a design of your own",
             "Find a place in your own code that chooses between sets of related classes: "
             "storage back ends, payment providers, themes, test doubles. Write its "
             "families and kinds, count the classes, and say which is likelier to grow, "
             "the families or the kinds."),
        ],
        "worked": {
            "title": "A map viewer gains a kind of product",
            "intro": [
                "Count the preset <code>new-kind</code>.",
            ],
            "lines": [
                "products: 3 styles × 3 kinds = 9",
                "classes: 1 + 3 + 3 + 9 = 16",
                "a new kind adds: 1 + 3 = 4 classes (16 → 20)",
                "it edits: 1 + 3 = 4 factory classes",
                "a new style would add 1 + 3 = 4 and edit 0",
            ],
            "after": [
                "Both changes add four classes here, because the design is square. The "
                "difference is in the classes edited, and it grows with the number of "
                "families: a viewer with ten styles would edit eleven factory classes for "
                "one new kind of product.",
            ],
        },
        "quiz_title": "Factories, families and kinds",
        "quiz": [
            {"q": "In the exercise, two modes and two kinds of product: how many classes "
                  "does the design have, and what does a new kind, hints, add and edit?",
             "a": ["9 classes; it adds 3 and edits 3",
                   "9 classes; it adds 3 and edits 0",
                   "8 classes; it adds 2 and edits 3",
                   "9 classes; it adds 2 and edits 2"],
             "c": 0,
             "why": "1 + 2 + 2 + 2 × 2 = 9 classes. A new kind adds 1 abstract product "
                    "and one product per mode, 3 (9 → 12), and edits the abstract factory "
                    "and both concrete factories, 3, each gaining an operation to make "
                    "hints. Editing nothing is what a new family does; 8 forgets the "
                    "abstract factory; 2 edits forgets that the abstract factory itself "
                    "declares the new operation."},
            {"q": "Why does Section 2.5 reject creating widgets with constructor calls?",
             "a": ["Constructors are slower than factory operations",
                   "A constructor names one standard's class, fixing the style and "
                   "scattering the choice through the code",
                   "Each constructor call makes a fresh widget where one shared widget "
                   "would do",
                   "Widgets must be created before the program starts"],
             "c": 1,
             "why": "A constructor call names a concrete class, so the style cannot be "
                    "chosen at run time, and porting means finding every such call; miss "
                    "one and the wrong style appears. The section says nothing about "
                    "speed or sharing, and the factory is set at start-up, before widgets are made, "
                    "not the widgets themselves."},
            {"q": "On the preset <code>new-style</code>, a fourth map style is added. "
                  "What does the lab count?",
             "a": ["4 classes added, 4 existing classes edited",
                   "3 classes added, 0 edited",
                   "4 classes added, 0 edited",
                   "1 class added, 0 edited"],
             "c": 2,
             "why": "A new family is one concrete factory and one product of each of the "
                    "3 kinds, 4 classes (16 → 20), and no existing class changes: the "
                    "abstract factory already declares every operation the new factory "
                    "implements. Four edits is the count for a new kind; 3 forgets the "
                    "factory; 1 forgets the products."},
            {"q": "Which liability does Abstract Factory's catalog entry name?",
             "a": ["Supporting a new kind of product means changing the abstract factory "
                   "and all its subclasses",
                   "Products of different families get mixed in one application",
                   "Client code must name the concrete product classes",
                   "A new product family requires editing every existing factory"],
             "c": 0,
             "why": "The entry lists isolating concrete classes, easy exchange of "
                    "families and consistency among products as benefits, and the "
                    "difficulty of new kinds of product as the liability, because the "
                    "factory interface fixes the set of products. Mixed families and "
                    "named classes are what the pattern prevents, and a new family edits "
                    "nothing."},
        ],
        "mistakes": [
            ("Creating each product with a constructor and a flag",
             "Section 2.5 shows what that costs: the style is fixed where the code is "
             "written, and every creation site must be found to port it; one missed is a "
             "widget of the wrong style. With a factory chosen once, the calling code "
             "names no style at all."),
            ("Expecting Abstract Factory to absorb new kinds of product cheaply",
             "The catalog says plainly that new kinds are hard: the abstract factory's "
             "interface lists the products, so a new kind edits it and every concrete "
             "factory. On the lesson's map viewer the lab counts 4 classes edited for a "
             "new kind against 0 for a new style; the authors recommend the pattern where "
             "the kinds stay put and the families vary."),
            ("Making the factory choice in many places",
             "The authors leave where the factory lives to convenience, a global, a "
             "static member or a Singleton, but insist that it is set after the style "
             "is known and before any product is made, and that the code which makes "
             "products never chooses it. Choosing a factory at each "
             "creation site brings back the scattered decision the pattern removed."),
        ],
        "standard": (
            "Finish when you can count a family of factories and what each change costs.",
            "Given families and kinds of product, state the classes under Abstract "
            "Factory, and what a new family and a new kind each add and edit, and say "
            "which of the two the catalog calls difficult."
        ),
        "note": (
            "The lab counts classes as if every concrete product differs in behaviour, "
            "and does not count the client. It cannot say which of your families and "
            "kinds will grow, which is the question the pattern's fit turns on."
        ),
    },
    # ---------------------------------------------------------------- 05
    # 2.6 Supporting Multiple Window Systems (PDF pp. 71-78 of the operator's
    # copy): why Abstract Factory does not fit, the Window class, the two
    # rejected alternatives, WindowImp, configuring through an abstract
    # factory, Bridge. Bridge's consequences are from the pattern (p. 174).
    # Quote: PDF p. 78 of the operator's copy, 18 words, quotes.py OK.
    # Lesson total: 18 words.
    {
        "slug": "window-systems",
        "title": "Supporting Multiple Window Systems",
        "module": "Chapter 2 · A Case Study: Designing a Document Editor",
        "one_line": "An abstraction and its platform implementations kept in two class hierarchies joined by a reference, so that each can grow without the other.",
        "summary": (
            "Section 2.6 makes Lexi run on several window systems whose interfaces it "
            "does not control, by giving every window an implementation object behind a "
            "stable interface. Read why Abstract Factory alone will not do, then count "
            "the classes a library's notices need when each notice and channel pair is "
            "a subclass, against two hierarchies joined by a reference."
        ),
        "key": [
            "vendor interfaces share no base class",
            "neither intersection nor union",
            "encapsulate the concept that varies",
            "a window holds its implementation",
            "abstraction and implementation grow apart",
            "a factory picks the implementation",
        ],
        "key_label": "Window systems in six lines",
        "concepts_intro": (
            "Lexi's two classes, and the pattern their relationship is."
        ),
        "concepts": [
            ("Window",
             "Lexi's abstract class for a window as the application sees it: operations "
             "to draw shapes and text, to raise, lower, iconify and redraw. Its "
             "subclasses are kinds of window, such as an application window, an icon or "
             "a dialog, and none of them depends on a particular window system."),
            ("WindowImp",
             "The abstract class for an object that hides one window system's own "
             "interface. Each window holds one, and forwards its drawing and window "
             "management to it; a subclass per window system translates those requests "
             "into that system's calls."),
            ("Bridge",
             "The pattern: an Abstraction holds a reference to an Implementor, "
             "RefinedAbstractions extend the abstraction, and ConcreteImplementors "
             "implement the implementor's interface, so that either hierarchy can gain "
             "classes without touching the other. It has a lesson of its own, Bridge, in Structural "
             "Patterns."),
        ],
        "read_title": "Two hierarchies instead of one",
        "read_intro": (
            "Read Section 2.6, Supporting Multiple Window Systems, in your own copy "
            "first. The lesson follows its argument and counts the same shape on a "
            "library's notices and the channels that deliver them."
        ),
        "body": [
            # PDF p. 78 of the operator's copy
            ("p", "&ldquo;The intent behind Bridge is to allow separate class hierarchies "
                  "to work together even as they evolve independently.&rdquo; Section 2.6, "
                  "Supporting Multiple Window Systems, reaches Bridge after first asking "
                  "whether the previous section's pattern would do. Read the section in "
                  "your own copy first."),
            ("p", "The problem looks like the last one. A window system manages "
                  "overlapping windows on the screen and routes keyboard and mouse input "
                  "to them, and in 1995 there were several, Macintosh, Presentation "
                  "Manager, Windows and X, with largely incompatible programming "
                  "interfaces. Why not a factory per window system? Because Abstract "
                  "Factory worked for widgets only because the authors wrote the widget "
                  "classes themselves, deriving each standard's scroll bar from a common "
                  "abstract one. Hierarchies from different vendors share no such base, "
                  "and Lexi cannot write its own window system to supply one. What it can "
                  "do is notice that window systems all do broadly the same things, and "
                  "slide each one under a common interface."),
            ("p", "That interface is the Window class Section 2.2 already used for "
                  "drawing. How much should it offer? The authors reject both extremes. "
                  "Offer only what every window system has, and Lexi is as weak as the "
                  "weakest; offer everything any of them has, and the interface is huge, "
                  "incoherent and changes with every vendor's release. They settle "
                  "between: the popular windowing operations, plus the graphics "
                  "operations glyphs need to draw themselves. Subclasses of Window are "
                  "kinds of window, an application window, an icon, a dialog, each "
                  "behaving a little differently."),
            ("p", "Where does the platform code go? Two ways are dismissed. One is a "
                  "separate version of Window and its subclasses for each platform, "
                  "chosen when Lexi is built, with several classes of the same name to "
                  "keep in step. The other is a platform subclass of every kind of "
                  "window, which the authors call another subclass explosion, like the "
                  "one embellishment would have caused. Neither lets the window system "
                  "change after compiling. Their third way is the chapter's refrain, to "
                  "encapsulate the concept that varies: put each window system's "
                  "functionality in an object, a WindowImp, and implement Window in terms "
                  "of it. A window's request to draw a rectangle becomes a call on its "
                  "implementation, and the X subclass and the Presentation Manager "
                  "subclass carry it out in their very different ways."),
            ("p", "Which implementation does a window get? The section uses the previous "
                  "lesson's pattern after all: an abstract factory for window-system "
                  "resources, one concrete factory per window system, asked by Window's "
                  "constructor for its implementation. The relationship between the two "
                  "hierarchies is Bridge. Window's interface serves the application "
                  "programmer; WindowImp's serves the window systems and may follow "
                  "them, warts and all. The catalog lists the consequences: the "
                  "implementation can be chosen at run time and changed without "
                  "recompiling clients, each hierarchy can be extended on its own, and "
                  "clients do not see implementation details. The catalog names no "
                  "liability. The costs are visible in the section itself: a second "
                  "hierarchy to maintain, a call through the implementation object for "
                  "every drawing request, and an implementation interface that must be "
                  "made to fit systems that do the same things differently."),
            ("code", _lines(NOTICE_BRIDGE_JAVA)),
            ("p", "The lab's design is a library that sends notices, overdue, hold ready "
                  "and renewal, through channels it does not control, email, SMS and app "
                  "push, each with its own provider's interface. On the preset "
                  "<code>library-notices</code> there are 3 × 3 = 9 combinations, so a "
                  "platform subclass of every kind of notice needs 9 + 1 = 10 classes. "
                  "Two hierarchies need (3 + 1) + (3 + 1) = 8, and the references tile "
                  "says each notice holds one reference, to its channel, which is "
                  "Window's reference to its WindowImp. A fourth channel adds 3 classes "
                  "under subclassing, one per kind of notice (10 → 13), against 1 "
                  "(8 → 9), and no notice class is touched."),
            ("p", "The preset <code>four-channels</code> adds a letter channel and then a "
                  "new kind of notice: 3 × 4 = 12 combinations, 13 classes against 9, "
                  "and the new notice costs 4 subclasses (13 → 17) against 1 (9 → 10). "
                  "The ratio tile reads 5/4 ≈ 1.3× on the first preset and 13/9 ≈ 1.4× on "
                  "this one. It is not large here; what the "
                  "authors argue from is that the subclass count multiplies and the other "
                  "adds, and that only the reference lets a notice be given a different "
                  "channel while the program runs."),
            ("h3", "Exercise"),
            ("code", [PRINT_ASPECTS]),
            ("p", "A shop prints two kinds of document on four kinds of printer, each "
                  "with its own driver. By hand, count the classes under each design and "
                  "what a fifth printer adds to each. Then type the line into the lab, "
                  "with printer as the aspect that gains a variant."),
            ("p", "The design now reaches the screen on any platform. The next lesson, "
                  "User Operations, reads Section 2.7, where the problem moves from "
                  "drawing to doing: how menus and buttons reach Lexi's operations, and "
                  "how those operations are undone."),
        ],
        "lab": ("gofkit", {
            "mode": "classes",
            "view": "explosion",
            "preset": "library-notices",
            "presets": [
                {"id": "library-notices",
                 "label": "A library's notices on three channels, a fourth channel",
                 "aspects": NOTICE_ASPECTS,
                 "added": "channel",
                 "expect": {"gclCombos": "3 × 3 = 9",
                   "gclSubclass": "9 + 1 = 10",
                   "gclCompose": "(3 + 1) + (3 + 1) = 8",
                   "gclRatio": "5/4 ≈ 1.3×",
                   "gclRefs": "1: channel",
                   "gclAddSubclass": "3 (10 → 13)",
                   "gclAddCompose": "1 (8 → 9)"}},
                {"id": "four-channels",
                 "label": "Four channels, and a new kind of notice",
                 "aspects": NOTICE_FOUR_CHANNELS,
                 "added": "notice",
                 "expect": {"gclCombos": "3 × 4 = 12",
                   "gclSubclass": "12 + 1 = 13",
                   "gclCompose": "(3 + 1) + (4 + 1) = 9",
                   "gclRatio": "13/9 ≈ 1.4×",
                   "gclRefs": "1: channel",
                   "gclAddSubclass": "4 (13 → 17)",
                   "gclAddCompose": "1 (9 → 10)"}},
            ],
            "panel_title": "Abstractions and platforms: subclasses against a bridge",
        }),
        "steps_title": "Counting a bridge",
        "steps_intro": "Four steps, the last of them on a design of your own.",
        "steps": [
            ("Separate the abstraction from the platform",
             "Write the kinds of thing the application uses (the abstraction) first, and "
             "the platforms that carry them out (the implementations) second."),
            ("Count a platform subclass of every kind",
             "Multiply the two counts and add 1 for the base: one class per kind of "
             "thing on each platform."),
            ("Count the bridge",
             "Add the two counts and 1 abstract class for each side. Each object of the "
             "abstraction holds one reference to an implementation."),
            ("Do it on a design of your own",
             "Find code of your own that runs one idea on several platforms or vendors: "
             "storage, messaging, payment, rendering. Write the abstraction and the "
             "platforms, count both designs, and say whether the platform's interface is "
             "yours to change or a vendor's."),
        ],
        "worked": {
            "title": "Three notices on three channels",
            "intro": [
                "Count the preset <code>library-notices</code>.",
            ],
            "lines": [
                "combinations: 3 notices × 3 channels = 9",
                "subclassing: 9 + 1 = 10 classes",
                "bridge: (3 + 1) + (3 + 1) = 8 classes",
                "a fourth channel, subclassing: +3 (10 → 13)",
                "a fourth channel, bridge: +1 (8 → 9)",
            ],
            "after": [
                "Under the bridge the new channel is one class that implements the "
                "channel interface; every kind of notice can use it through the "
                "reference it already holds.",
            ],
        },
        "quiz_title": "Windows, implementations and the bridge",
        "quiz": [
            {"q": "In the exercise, two documents on four printers: how many classes does "
                  "each design need, and what does a fifth printer add to each?",
             "a": ["9 and 8; a fifth printer adds 2 and 1",
                   "8 and 6; a fifth printer adds 2 and 1",
                   "9 and 8; a fifth printer adds 4 and 1",
                   "9 and 8; a fifth printer adds 1 and 1"],
             "c": 0,
             "why": "Subclassing: 2 × 4 = 8 combinations plus the base, 9. The bridge: "
                    "(2 + 1) + (4 + 1) = 8. A fifth printer needs a subclass for each "
                    "kind of document, 2 (9 → 11), against 1 printer class (8 → 9). "
                    "Eight and six forget the abstract classes; 4 is what a new kind of "
                    "document would add under subclassing, one per printer."},
            {"q": "Why, according to Section 2.6, does Abstract Factory alone not solve "
                  "window-system portability?",
             "a": ["Abstract Factory cannot create objects at run time",
                   "The vendors' window-system classes share no common abstract classes, "
                   "and Lexi cannot write its own window system",
                   "There are too many window systems for one factory",
                   "Window systems have no product families"],
             "c": 1,
             "why": "Abstract Factory needs an abstract product class for each kind of "
                    "product; for widgets the authors wrote those themselves, but "
                    "different vendors' hierarchies are incompatible and a home-made "
                    "window system is out of the question. The section still uses an "
                    "abstract factory afterwards, to choose each window's implementation."},
            {"q": "What does the references tile report on the preset "
                  "<code>library-notices</code>, and what is it in Lexi's design?",
             "a": ["1: channel; a window's reference to its WindowImp",
                   "3: overdue, hold-ready, renewal; a window's subclasses",
                   "1: notice; a WindowImp's reference to its window",
                   "2: notice, channel; a window's parent and child"],
             "c": 0,
             "why": "The client holds the first aspect, the notice, and each notice holds "
                    "one reference per other aspect, here 1, to its channel. In Lexi each "
                    "Window holds its WindowImp, not the other way round; the three notice "
                    "kinds are the abstraction's refinements, not references."},
            {"q": "Which two approaches to the Window interface do the authors reject?",
             "a": ["Abstract classes and concrete classes",
                   "Offering only what all window systems share, and offering everything "
                   "any of them has",
                   "Compile-time and run-time configuration",
                   "Inheritance and composition"],
             "c": 1,
             "why": "The intersection of functionality makes Lexi as weak as the weakest "
                    "system; the union makes a huge, incoherent interface that changes "
                    "with every vendor. The design falls between them. Window is an "
                    "abstract class with concrete subclasses, and the section favours "
                    "composition and run-time configuration rather than rejecting them."},
        ],
        "mistakes": [
            ("Applying Abstract Factory because the problem looks the same",
             "Section 2.6 opens by asking exactly that and answering no: the pattern needs "
             "abstract product classes the vendors do not share. The window systems' "
             "interfaces had to be hidden behind one Lexi defines, and only then could a "
             "factory pick an implementation."),
            ("Adding a platform subclass to every class in a hierarchy",
             "The authors call it another subclass explosion, and note that it fixes the "
             "platform at compile time. On the lesson's notices the lab counts 10 classes "
             "against 8, with each new channel costing 3 subclasses against 1; and no "
             "subclass can switch channel on a live notice."),
            ("Making the implementation interface mirror the abstraction",
             "Bridge's point is that the two interfaces serve different readers: Window's "
             "the application programmer, WindowImp's the window systems, warts and all. "
             "The catalog notes the implementor usually offers primitives from which the "
             "abstraction builds higher-level operations."),
        ],
        "standard": (
            "Finish when you can count a bridge against a subclass per platform.",
            "Given an abstraction and its platforms, state the classes under each design, "
            "what a new platform and a new kind of abstraction each add, and why Section "
            "2.6 does not use Abstract Factory alone."
        ),
        "note": (
            "The lab counts classes on the aspects as stated. It cannot tell you whether "
            "your platforms' interfaces are close enough to slide under one, which the "
            "authors take as given for window systems, nor where between intersection "
            "and union your interface should fall."
        ),
    },
]
