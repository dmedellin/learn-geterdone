"""Creational Patterns, lessons 1-5 -- Chapter 3.

Gamma, Helm, Johnson and Vlissides, Design Patterns: Elements of Reusable
Object-Oriented Software (Addison-Wesley, 1995), Chapter 3, Creational
Patterns: the chapter's introduction (its maze example summarised in prose
only), Abstract Factory, Builder, Factory Method, Prototype and Singleton.
Pages in the comments are PDF pages of the operator's copy; the lessons cite
by chapter, section and pattern. Every quotation is copied from that copy and
checked with quotes.py. The designs and Java sketches are written for these
lessons: none of the book's code, diagrams or example data is reproduced, and
no lab uses the book's domains (no maze rooms, walls or doors, no widget
families). The design is docs/design-patterns/PLAN.md, section C, Course 3.
"""


def _lines(text):
    """A snippet constant as a code block's list of lines."""
    return text.split("\n")


_GOF_INTRO = (
    "The lab counts one consequence of applying a pattern or not; whether the "
    "pattern fits is weighed in the book, against what in the design is expected "
    "to vary."
)


# ---------------------------------------------------------------- 3.1 design

# A map tile viewer: four styles (families), each supplying three kinds of
# part. Written for the lesson; not the book's widget toolkit.
MAP_FAMILIES = "street satellite night terrain"
MAP_KINDS = "tile marker label"

MAP_STYLE_JAVA = """// One map style makes every part a map view draws.
interface MapStyle {
    Tile makeTile(int x, int y);
    Marker makeMarker(Place place);
    Label makeLabel(String text);
}
final class NightStyle implements MapStyle {
    public Tile makeTile(int x, int y) { return new NightTile(x, y); }
    public Marker makeMarker(Place p) { return new GlowMarker(p); }
    public Label makeLabel(String text) { return new PaleLabel(text); }
}
abstract class MapView {
    private final MapStyle style;
    MapView(MapStyle style) { this.style = style; }
    abstract void draw(Object part);
    void show(Place p) {
        draw(style.makeTile(p.x(), p.y()));
        draw(style.makeMarker(p));
        draw(style.makeLabel(p.name()));
    }
}"""


# ---------------------------------------------------------------- 3.2 design

# A recipe book: three sources read by directors, four representations made
# by builders.
RECIPE_ASPECTS = ("reader, markup, form, scan; "
                  "builder, page, shopping-list, narration, card")
RECIPE_ONE_SOURCE = "reader, markup; builder, page, shopping-list, narration, card"

RECIPE_BUILDER_JAVA = """// Every part a recipe can have; the defaults do nothing.
interface RecipeBuilder {
    default void title(String text) { }
    default void ingredient(String name, String amount) { }
    default void step(String text) { }
}

// A builder that keeps only what a shopping trip needs.
final class ShoppingListBuilder implements RecipeBuilder {
    private final List<String> items = new ArrayList<>();

    @Override
    public void ingredient(String name, String amount) {
        items.add(amount + " " + name);
    }

    List<String> result() { return items; }
}"""

MARKUP_READER_JAVA = """// The director knows the markup, and nothing of what is built from it.
final class MarkupReader {
    void read(List<String> lines, RecipeBuilder builder) {
        for (String line : lines) {
            if (line.startsWith("# ")) {
                builder.title(line.substring(2));
            } else if (line.startsWith("- ")) {
                String[] parts = line.substring(2).split(":", 2);
                builder.ingredient(parts[0].trim(), parts[1].trim());
            } else if (line.length() > 0) {
                builder.step(line);
            }
        }
    }
}"""


# ---------------------------------------------------------------- 3.3 design

# A garden irrigation controller: an abstract Zone whose factory method makes
# the zone's watering schedule.
ZONE_FAMILIES = "lawn bed greenhouse"
ZONE_KINDS = "schedule"

ZONE_JAVA = """// The controller knows when a zone needs a schedule, not which one.
abstract class Zone {
    protected abstract Schedule createSchedule();   // the factory method

    abstract List<Valve> valves();

    final void runCycle(Weather today) {
        Schedule schedule = createSchedule();
        for (Valve valve : valves()) {
            valve.open(schedule.minutesFor(today));
        }
    }
}

final class LawnZone extends Zone {
    private final List<Valve> sprinklers = new ArrayList<>();

    @Override protected Schedule createSchedule() { return new LawnSchedule(); }
    @Override List<Valve> valves() { return sprinklers; }
}"""

ZONE_SUPPLIER_JAVA = """// Composition instead of a subclass per product: pass the constructor.
final class PlainZone extends Zone {
    private final Supplier<Schedule> schedules;
    private final List<Valve> valves;

    PlainZone(Supplier<Schedule> schedules, List<Valve> valves) {
        this.schedules = schedules;
        this.valves = valves;
    }

    @Override protected Schedule createSchedule() { return schedules.get(); }

    @Override List<Valve> valves() { return valves; }
}

// new PlainZone(DripSchedule::new, potLines) needs no PotZone class."""


# ---------------------------------------------------------------- 3.4 design

# A music playlist app: a workout template cloned for three runners. Shallow
# clones share the template's track list; deep clones have their own.
SHALLOW_HOLDERS = "template, tracks-w; ana-run, tracks-w; ben-run, tracks-w; cy-run, tracks-w"
DEEP_HOLDERS = "template, tracks-t; ana-run, tracks-a; ben-run, tracks-b; cy-run, tracks-c"

PLAYLIST_JAVA = """// A playlist template and its two ways of being copied.
final class Playlist {
    private final String name;
    private final List<Track> tracks;      // a part that can change

    Playlist(String name, List<Track> tracks) {
        this.name = name;
        this.tracks = tracks;
    }

    Playlist shallowCopy(String newName) {
        return new Playlist(newName, tracks);                    // shares it
    }

    Playlist deepCopy(String newName) {
        return new Playlist(newName, new ArrayList<>(tracks));   // owns one
    }

    void add(Track track) { tracks.add(track); }
}"""

TEMPLATES_JAVA = """// A prototype manager: templates by key, copied on request.
final class Templates {
    private final Map<String, Playlist> byKey = new HashMap<>();

    void register(String key, Playlist prototype) { byKey.put(key, prototype); }

    void unregister(String key) { byKey.remove(key); }

    Playlist create(String key, String newName) {
        Playlist prototype = byKey.get(key);
        if (prototype == null) {
            throw new IllegalArgumentException("no template " + key);
        }
        return prototype.deepCopy(newName);
    }
}"""


# ---------------------------------------------------------------- 3.5 design

# A parcel locker network: a registry of locker banks (cost 50 to load) and an
# audit log (cost 20 to open); five requests, all for the registry.
LOCKER_SUBJECTS = "registry, 50; audit-log, 20"
LOCKER_REQUESTS = ("kiosk, registry; app, registry; courier, registry; "
                   "kiosk, registry; night-job, registry")

REGISTRY_JAVA = """// One registry of lockers, made on first use and shared.
final class LockerRegistry {
    private static LockerRegistry instance;   // none until asked for

    private LockerRegistry() {                // no client can call new
        loadBanksFromDisk();                  // the cost, paid once
    }

    static synchronized LockerRegistry instance() {
        if (instance == null) {
            instance = new LockerRegistry();
        }
        return instance;
    }

    private void loadBanksFromDisk() {
        // read every bank's doors and sizes
    }
}"""


LESSONS = [
    # ---------------------------------------------------------------- 01
    # Chapter 3 introduction (PDF pp. 101-105 of the operator's copy; the maze
    # example pp. 102-105, summarised in prose only) and Abstract Factory
    # (pp. 107-115).
    # Quote: PDF p. 101 of the operator's copy, 7 words, quotes.py OK.
    # Lesson total: 7 words.
    {
        "slug": "abstract-factory",
        "title": "Abstract Factory",
        "module": "Chapter 3 · Creational Patterns",
        "one_line": "One object that creates every member of a family of related products, so the code that uses them never names a concrete class.",
        "summary": (
            "Chapter 3 opens with what the five creational patterns have in common, "
            "and with the maze the authors build five ways. Read the introduction and "
            "Abstract Factory, then count the classes a map viewer's styles need and "
            "what a new style and a new kind of part each add, and edit."
        ),
        "key": [
            "creational patterns hide which class is made",
            "a factory makes one whole family",
            "clients see only abstract interfaces",
            "a concrete factory is named once",
            "a new family edits no class",
            "a new kind edits every factory",
        ],
        "key_label": "Abstract Factory in six lines",
        "concepts_intro": (
            "Three terms carry the lesson. The first is the chapter's, the other two "
            "the pattern's."
        ),
        "concepts": [
            ("Creational pattern",
             "A pattern that takes the decision of which concrete class to "
             "instantiate out of the code that needs the object. A class creational "
             "pattern varies that class by inheritance; an object creational pattern "
             "hands the work to another object. Either way the rest of the system "
             "knows its objects by their abstract interfaces."),
            ("Product family",
             "A set of objects of different kinds that are designed to be used "
             "together and that vary together: one map style's tiles, markers and "
             "labels. Abstract Factory makes sure a client gets a matching set, never "
             "one style's markers on another style's tiles."),
            ("Abstract and concrete factory",
             "The abstract factory declares one creation operation per kind of "
             "product; each concrete factory implements all of them for one family. "
             "The client holds only the abstract factory and the abstract products, "
             "and the one line that names a concrete factory picks the family."),
        ],
        "read_title": "The chapter's argument first, then the pattern, then the count",
        "read_intro": (
            "Read the introduction to Chapter 3 and Abstract Factory in your own copy "
            "first. The lesson reads the introduction as an argument and the pattern "
            "as a tool, and then counts the classes of a small design."
        ),
        "body": [
            ("p", "&ldquo;Creational design patterns abstract the instantiation "
                  "process.&rdquo; The authors open Chapter 3, Creational Patterns, with "
                  "that sentence, and this lesson reads the chapter's introduction and its "
                  "first pattern, Abstract Factory. Read both in your own copy first. The "
                  "lesson reads the introduction as an argument and the pattern as a tool, "
                  "and then counts the classes a design built on families needs, and what "
                  "each kind of growth costs it."),
            ("p", "The introduction's case runs like this. As a system comes to rely more "
                  "on composing objects than on inheriting from classes, its behaviour is "
                  "assembled from a few basic pieces, and making an object that behaves "
                  "the right way takes more than a call to one constructor. The creational "
                  "patterns take that work over. All five share two habits: they keep the "
                  "knowledge of which concrete classes are in use in one place, and they "
                  "hide how instances are made and wired together, so the rest of the "
                  "program sees only abstract interfaces. A class creational pattern does "
                  "it by inheritance; an object creational pattern delegates the making to "
                  "another object. The authors add that the five sometimes compete, "
                  "Prototype and Abstract Factory each serving the same design, and "
                  "sometimes cooperate, as when a Builder uses another of them to pick its "
                  "parts."),
            ("p", "To compare the five, the chapter keeps one example running through all "
                  "of them: building the maze for a computer game, a set of rooms whose "
                  "sides are walls or doors. Its first version is one routine that makes "
                  "every room, wall and door by naming its class, and the authors' "
                  "complaint is not its length but its rigidity: a new game with enchanted "
                  "rooms and doors that open only to a spell cannot reuse the layout "
                  "without rewriting the routine. The introduction then sketches one way "
                  "out per pattern: overridable creation operations (Factory Method), an "
                  "object passed in that makes the parts (Abstract Factory), an object "
                  "passed in that builds a whole maze step by step (Builder), sample parts "
                  "to copy (Prototype), and Singleton to keep the game to one maze that "
                  "everything can reach. The maze stays in the book; the labs here use "
                  "designs of their own."),
            ("p", "Abstract Factory, an object creational pattern also known as Kit, gives "
                  "a client one interface through which it creates each member of a family "
                  "of related objects, so that the client never names their concrete "
                  "classes. The book's motivating example is a user interface toolkit that "
                  "must support more than one look-and-feel standard, Motif and "
                  "Presentation Manager in 1995. An abstract widget factory declares an "
                  "operation for each kind of widget; each standard has a concrete factory "
                  "that returns its own widgets; the application asks the factory and "
                  "never learns which classes it got, and because one factory makes the "
                  "whole set, widgets of two standards cannot end up side by side. The "
                  "case study's lesson Supporting Multiple Look-and-Feel Standards met this design "
                  "inside the Lexi editor; this lesson reads the pattern itself."),
            ("p", "The pattern applies, in the authors' list, when a system should be "
                  "insulated from the way its products are made and put together, when it must be "
                  "configured with one of several families, when the members of a family "
                  "must be used together and that rule should be enforced, and when a "
                  "library should publish its products' interfaces and keep their "
                  "implementations hidden. The participants are the AbstractFactory, with "
                  "an operation per kind of product; a ConcreteFactory per family, which "
                  "implements them; an AbstractProduct per kind; the ConcreteProducts, one "
                  "per family and kind; and the Client, which uses only the abstract "
                  "classes. At run time there is normally one concrete factory instance, "
                  "and the abstract factory leaves the actual making to it."),
            ("code", _lines(MAP_STYLE_JAVA)),
            ("p", "The authors list four consequences, three benefits and a liability. "
                  "The pattern isolates concrete classes: product class names live inside "
                  "the concrete factories and never appear in client code. It makes "
                  "exchanging families easy, since a concrete factory's class appears in "
                  "one place, where it is instantiated, and changing that one name changes "
                  "the whole family at once. It promotes consistency, because a client "
                  "that gets everything from one factory uses one family at a time. And "
                  "supporting new kinds of product is hard: the abstract factory's "
                  "interface fixes the set of kinds it can make, so a new kind means "
                  "changing the abstract factory and every one of its subclasses."),
            ("p", "Three implementation notes follow. An application usually needs one "
                  "concrete factory per family, so a factory is often a Singleton, the "
                  "fifth lesson's pattern. The products are most often made by one factory "
                  "method each, the third lesson's pattern, which is simple but costs a "
                  "concrete factory class for every family, even families that differ "
                  "only a little; where many families are possible, a factory can instead "
                  "be given a prototype of each product to clone, the fourth lesson's "
                  "pattern, and a new family then needs no new class. And a factory can be "
                  "made extensible by replacing its many operations with one make "
                  "operation that takes the kind as a parameter. That is more flexible and "
                  "less safe: in a statically typed language every product comes back "
                  "under one shared interface, and a client that needs a kind's own "
                  "operations must cast down, which can fail. The authors present it as "
                  "the usual price of a very open interface, easier to pay in Smalltalk "
                  "than in C++."),
            ("p", "The Sample Code applies the pattern to the maze: a maze factory with "
                  "one creation operation per part, passed to the maze-building routine, "
                  "and subclasses for enchanted and bombed mazes that override only the "
                  "parts that differ; the base factory is a concrete class, so it serves "
                  "as both the abstract and a concrete factory, and a Smalltalk version "
                  "keeps a catalogue of part classes keyed by name. Read it in the book; "
                  "its code is C++ and Smalltalk, and this course's sketches are Java. The "
                  "known uses are InterViews, whose classes named with a Kit suffix are "
                  "abstract factories, and ET++, which used the pattern to run on several "
                  "window systems. The related patterns are the two the implementation "
                  "leans on, Factory Method and Prototype, and Singleton for the factory "
                  "itself."),
            ("p", "Now the lab, on a map tile viewer rather than a widget toolkit. The "
                  "viewer draws three kinds of part, a tile, a marker and a label, in four "
                  "styles: street, satellite, night and terrain. On the preset "
                  "<code>map-styles</code> there are 4 × 3 = 12 concrete products. The "
                  "classes add up in the table's order, 1 abstract factory, 4 concrete "
                  "factories, 3 abstract products and 12 concrete products, so 1 + 4 + 3 + "
                  "12 = 20, and 1 + 4 = 5 of them create anything. The prototype "
                  "configuration tile reads none, because under this scheme the factory "
                  "classes themselves fix what is made. The lab counts each concrete "
                  "product as a class of its own, as if every style's marker behaved "
                  "differently; where styles differ only in colours, fewer classes would "
                  "do, which is the Prototype lesson's subject."),
            ("p", "The two change presets are the fourth consequence in numbers. On "
                  "<code>map-new-style</code> a fifth style, for public transport, adds 4 "
                  "classes, 1 concrete factory and its 3 products, taking the design from "
                  "20 to 24, and edits none: the abstract factory already says what a "
                  "style must supply. On <code>map-new-kind</code> a fourth kind of part, "
                  "a route line, adds 5 classes, 1 abstract product and one concrete "
                  "product per style, from 20 to 25, and edits 5, the abstract factory "
                  "and all 4 concrete factories, each given an operation to make the new "
                  "kind. The two growths cost about the same in new classes; only one of "
                  "them reaches back into code already written. On the lesson's "
                  "illustration that is the difference the authors mean, and no count "
                  "tells you which growth a design will meet."),
            ("h3", "Exercise"),
            ("ul", [
                "A quiz app has two families of look, `kids` and `adult`, and four kinds "
                "of part that every family supplies: `question`, `hint`, `score-card` "
                "and `timer`.",
                "It is built with Abstract Factory, one concrete factory per family.",
            ]),
            ("p", "By hand, count the concrete products and the classes in the design, then "
                  "what a new family adds and edits, and what a new kind adds and edits. "
                  "Then type the families and kinds into the lab, choose each change, and "
                  "check."),
            ("p", "Abstract Factory hands back each product at once, whole. The next "
                  "lesson, Builder, reads the pattern that assembles one complex product "
                  "a step at a time."),
        ],
        "lab": ("gofkit", {
            "mode": "classes",
            "view": "factory",
            "families": MAP_FAMILIES,
            "kinds": MAP_KINDS,
            "scheme": "abstract-factory",
            "preset": "map-styles",
            "presets": [
                {"id": "map-styles",
                 "label": "A map viewer: four styles, three kinds of part",
                 "change": "none",
                 "expect": {"gclProducts": "4 × 3 = 12", "gclClasses": "1 + 4 + 3 + 12 = 20", "gclFactories": "1 + 4 = 5", "gclConfigs": "none: the factory classes themselves fix what is made", "gclAdded": "no change chosen"}},
                {"id": "map-new-style",
                 "label": "The same viewer gaining a fifth style",
                 "change": "family",
                 "expect": {"gclAdded": "4 (20 → 24): 1 concrete factory, 3 concrete products", "gclChanged": "0"}},
                {"id": "map-new-kind",
                 "label": "The same viewer gaining a fourth kind of part",
                 "change": "kind",
                 "expect": {"gclAdded": "5 (20 → 25): 1 abstract product, 4 concrete products", "gclChanged": "5: the abstract factory and 4 concrete factories, each given an operation to make the new kind"}},
            ],
            "panel_title": "Families, kinds and the classes a factory design needs",
            "panel_intro": _GOF_INTRO,
        }),
        "steps_title": "Pricing a family-based design",
        "steps_intro": "Four steps, the last of them on a design of your own.",
        "steps": [
            ("Name the families and the kinds",
             "Write down what varies together, the families, and what every family "
             "must supply, the kinds. A concrete product is one family's version of "
             "one kind."),
            ("Count the classes",
             "Add 1 abstract factory, a concrete factory per family, an abstract "
             "product per kind and a concrete product per family and kind."),
            ("Price each growth",
             "A new family adds a factory and its products and edits nothing. A new "
             "kind adds an abstract product and one product per family, and edits the "
             "abstract factory and every concrete factory."),
            ("Do it on your own code",
             "Find a place in a system you know where objects come in matching sets: "
             "themes, regions, storage vendors, test and live. Type its families and "
             "kinds into the lab, and note which of the two growths the last year "
             "actually brought."),
        ],
        "worked": {
            "title": "Four styles, three kinds",
            "intro": [
                "Count <code>map-styles</code>, then both changes.",
            ],
            "lines": [
                "map products: 4 styles × 3 kinds = 12",
                "map classes: 1 + 4 + 3 + 12 = 20",
                "a new style adds 1 factory and 3 parts",
                "a new style edits none; 20 → 24",
                "a new kind adds 1 + 4 = 5; 20 → 25",
                "a new kind edits 1 + 4 = 5 factories",
            ],
            "after": [
                "The two additions are close in size. What separates them is the edits: "
                "a new style touches no class that exists, and a new kind touches every "
                "factory.",
            ],
        },
        "quiz_title": "Families, kinds and the authors' claims",
        "quiz": [
            {"q": "In the exercise (2 families, 4 kinds, Abstract Factory), how many "
                  "classes does the design have, and what does a new kind add and edit?",
             "a": ["15 classes; a new kind adds 3 and edits 3",
                   "15 classes; a new kind adds 3 and edits 0",
                   "14 classes; a new kind adds 3 and edits 2",
                   "15 classes; a new kind adds 5 and edits 0"],
             "c": 0,
             "why": "1 abstract factory + 2 concrete factories + 4 abstract products + 2 × "
                    "4 = 8 concrete products = 15. A new kind adds 1 abstract product and "
                    "2 concrete ones, 3 in all, and edits the abstract factory and both "
                    "concrete factories, 3 classes, each gaining an operation. Adding 5 "
                    "and editing none is what a new family costs, 1 factory and its 4 "
                    "products; 14 classes and 2 edits leave out the abstract factory."},
            {"q": "Which consequence do the authors list as Abstract Factory's liability?",
             "a": ["Clients come to depend on the concrete product classes",
                   "Supporting new kinds of product is difficult",
                   "Exchanging one product family for another is difficult",
                   "Products of two families get mixed"],
             "c": 1,
             "why": "The abstract factory's interface fixes the kinds it can make, so a new "
                    "kind changes it and all its subclasses. The other three are the "
                    "opposites of the benefits the authors list: the pattern isolates "
                    "concrete classes, makes exchanging families easy and promotes "
                    "consistency among products."},
            {"q": "In the extensible-factory variant the abstract factory offers just one "
                  "make operation, with a parameter naming the kind of product. What do "
                  "the authors say it costs?",
             "a": ["A new concrete factory class for every family",
                   "Every product comes back under one abstract interface, so a client "
                   "needing a kind's own operations must cast down",
                   "Changing the abstract factory and every concrete factory for each new "
                   "kind",
                   "Giving up prototype-based factories"],
             "c": 1,
             "why": "The parameter removes the fixed list of kinds, and with it the "
                    "edits a new kind would cause, but every product is returned as the "
                    "same abstract type, and a downcast can fail. A factory class per "
                    "family is the cost of the factory-method implementation, not of this "
                    "variant; and the prototype- and class-based factories are exactly "
                    "where the authors say this technique is used."},
            {"q": "In the chapter introduction's maze example, what do the authors name as "
                  "the real problem with the routine that builds the maze?",
             "a": ["It is long for what it does",
                   "It hard-codes the classes it instantiates, so the layout cannot be "
                   "reused with new kinds of room or door",
                   "It creates walls the game never uses",
                   "It cannot build a maze of more than two rooms"],
             "c": 1,
             "why": "The authors grant the routine is complicated for two rooms, but say "
                    "that shortening it only moves code elsewhere; the barrier to change "
                    "is the class names written into it. The routine builds the small "
                    "maze it is asked for, and nothing in the example turns on unused "
                    "walls or on size."},
        ],
        "mistakes": [
            ("Expecting Abstract Factory to make new kinds of product easy",
             "It makes new families easy and new kinds hard. The abstract factory's "
             "interface lists the kinds, so adding one changes that interface and every "
             "concrete factory; on the lesson's illustration the lab counts 5 classes "
             "edited for the map viewer's new kind against none for a new style. The "
             "authors' way round, a make operation with a parameter, costs type safety."),
            ("Writing a concrete factory class for every small variation",
             "Where many families are possible, the authors suggest a factory given "
             "prototypes of its products, which needs no new class per family. One "
             "factory method per product is the common implementation, not the only "
             "one."),
            ("Letting clients reach past the factory for a product",
             "Concrete classes stay isolated only while their names stay inside the "
             "concrete factories. A client that constructs one product directly can "
             "pair one family's marker with another's tile, and the consistency the "
             "pattern promised is gone."),
        ],
        "standard": (
            "Finish when you can price a new family and a new kind under Abstract Factory.",
            "Given the families and kinds of a design, state its products and classes, "
            "what a new family and a new kind each add and edit, and the authors' remedy "
            "for the new-kind problem with its cost."
        ),
        "note": (
            "The lab counts classes from the families and kinds you state, as if every "
            "product were a class of its own. It cannot tell whether your products really "
            "form families, which growth your design will meet, or whether the families "
            "differ enough to need classes at all; those are what the authors weigh in "
            "Consequences and Implementation."
        ),
    },
    # ---------------------------------------------------------------- 02
    # Builder (PDF pp. 117-126 of the operator's copy).
    # Quote: PDF p. 117 of the operator's copy, 20 words, quotes.py OK.
    # Lesson total: 20 words.
    {
        "slug": "builder",
        "title": "Builder",
        "module": "Chapter 3 · Creational Patterns",
        "one_line": "A director that knows how a complex object is put together, driving a builder that decides what each part becomes, so one process yields many representations.",
        "summary": (
            "Builder separates the steps that construct a complex object from the "
            "representation those steps produce. Read the pattern, then count the "
            "classes a recipe book needs when every source and output pairing is a "
            "class of its own, and when sources are directors and outputs are "
            "builders."
        ),
        "key": [
            "a director knows the steps",
            "a builder knows the representation",
            "one process, many representations",
            "take the product from the builder",
            "empty defaults: override what you need",
            "a new output is one builder",
        ],
        "key_label": "Builder in six lines",
        "concepts_intro": "Three roles carry the lesson, all of them the pattern's.",
        "concepts": [
            ("Builder",
             "An object with an operation for each part a complex product can have. A "
             "concrete builder decides how each part is represented, and keeps the "
             "product it is assembling until it is asked for it."),
            ("Director",
             "The object that knows the construction process: it walks its input and "
             "tells the builder, step by step, which part comes next. It never learns "
             "what the builder makes of those calls."),
            ("Representation",
             "What the construction produces: a page, a shopping list, a spoken "
             "walkthrough. Different builders give different representations of the "
             "same input, and their products need not share a parent class."),
        ],
        "read_title": "The pattern first, then the count",
        "read_intro": (
            "Read Builder in your own copy first. The lesson reads it as a tool, section "
            "by section, and then counts the classes of a small design two ways."
        ),
        "body": [
            ("p", "&ldquo;Separate the construction of a complex object from its "
                  "representation so that the same construction process can create "
                  "different representations.&rdquo; That is the intent of Builder, the "
                  "second pattern of Chapter 3, Creational Patterns, and an object "
                  "creational pattern. Read it in your own copy first. The lesson reads "
                  "it as a tool, then counts the classes a design needs when every "
                  "pairing of a construction process with a representation is a class of "
                  "its own, and when the two are split into directors and builders."),
            ("p", "The book's motivating example is a reader for RTF, the Rich Text "
                  "Format, which must convert documents into an open-ended number of "
                  "other formats: plain ASCII text, TeX, an editable text widget. The "
                  "answer is to give the reader a converter object. As the reader parses, "
                  "it hands each token it recognises, plain text or a control word, to "
                  "the converter, and each converter subclass decides what that token "
                  "becomes in its own format; the ASCII converter, for one, ignores all "
                  "but plain text. In the pattern's terms the converters are builders and "
                  "the reader is the director, and the parsing is written once for every "
                  "output there will ever be."),
            ("p", "Builder applies, the authors say, when the algorithm that makes a "
                  "complex object should not depend on its parts or on how they are put "
                  "together, and when one construction process "
                  "has to yield more than one representation. Its participants are the Builder, an abstract "
                  "interface with an operation per part; the ConcreteBuilders, each of "
                  "which assembles its own representation, keeps track of it and offers a "
                  "way to retrieve it; the Director, which constructs through the Builder "
                  "interface; and the Product. The collaboration is a short script: the "
                  "client makes a director and gives it the builder it wants, the "
                  "director calls the builder whenever a part should be built, the "
                  "builder adds the part, and the client takes the finished product from "
                  "the builder, not from the director."),
            ("code", _lines(RECIPE_BUILDER_JAVA)),
            ("code", _lines(MARKUP_READER_JAVA)),
            ("p", "The authors give three consequences. A product's internal "
                  "representation can vary, because the director sees only the abstract "
                  "builder: a new representation is a new builder. Construction and "
                  "representation are kept in separate code, each concrete builder "
                  "holding everything needed to make one kind of product, so different "
                  "directors can reuse the same builders; the book imagines a reader for "
                  "SGML driving the very converters written for RTF. And construction is "
                  "under finer control, since the product is made a step at a time under "
                  "the director and collected only when finished, so the builder's "
                  "interface follows the construction process more closely than the "
                  "other creational patterns' interfaces do."),
            ("p", "Implementation adds three points. The builder's interface must be "
                  "general enough for every concrete builder, and the key question is how "
                  "parts are assembled: usually appending each result to the product is "
                  "enough, but sometimes a builder must reach parts it made earlier, as "
                  "when a parse tree is built from the leaves up and the builder returns "
                  "child nodes to the director, which passes them back for their parent. "
                  "Products often get no common abstract class, because representations "
                  "as unlike as plain text and an interactive widget have little to "
                  "share, and the client, which chose the builder, knows what it will get. "
                  "And in C++ the build operations are left as empty methods rather than "
                  "pure virtual ones, so a builder overrides only the parts it cares "
                  "about; the sketch does the same with Java 8's default methods."),
            ("p", "The Sample Code turns the maze routine into a builder interface that "
                  "can make a maze, numbered rooms and doors between them, a standard "
                  "builder that makes real mazes, and a counting builder that makes "
                  "nothing at all and only tallies the parts it would have made; read it "
                  "in the book. The known uses are the RTF converter of ET++; three "
                  "builders in Smalltalk-80, the compiler's parser driving a program-node "
                  "builder, the class builder, and the byte-code stream that assembles a "
                  "compiled method; and the Service Configurator of the Adaptive "
                  "Communications Environment, whose configuration-language parser is "
                  "the director. The related patterns: Abstract Factory also makes "
                  "complex objects, but it is about families and returns each product at "
                  "once, where Builder assembles one product in steps and returns it at "
                  "the end; and what a builder builds is often a Composite."),
            ("p", "Now the lab, on a recipe book rather than a text converter. The app "
                  "reads recipes from three sources, a markup file, a web form and a "
                  "scanned card, and makes four representations of each: a printed page, "
                  "a shopping list, a spoken walkthrough for the kitchen and an index "
                  "card. If every pairing of a source with an output were its own class, "
                  "MarkupToPage, FormToShoppingList and so on, the preset "
                  "<code>recipe-formats</code> counts 3 × 4 = 12 combinations and 12 + 1 "
                  "= 13 classes with their abstract base. Split into an abstract reader "
                  "with 3 directors and an abstract builder with 4 concrete builders, it "
                  "is (3 + 1) + (4 + 1) = 9 classes, a ratio of 13/9, about 1.4 times. "
                  "Each reader holds 1 reference, to its builder. The lab counts readers "
                  "and builders only; the products, a page or a list of strings, are the "
                  "same in either design."),
            ("p", "The same preset adds one output, a nutrition card. As pairings it costs "
                  "3 new classes, one per source, taking the design from 13 to 16; as a "
                  "builder it costs 1, from 9 to 10. The preset "
                  "<code>recipe-new-source</code> adds a source instead, an import from "
                  "a website, which costs 4 pairings, 13 to 17, against 1 new director, 9 "
                  "to 10: the second consequence in numbers, a new director reusing every "
                  "builder already written. The preset <code>recipe-one-source</code> is "
                  "the fair counterweight. With a single markup reader and the four "
                  "outputs there are 4 combinations, 4 + 1 = 5 classes as pairings and (1 "
                  "+ 1) + (4 + 1) = 7 split, a ratio of 5/7: when only one side varies, "
                  "the split adds classes, and what it buys is room for the other side to "
                  "vary later."),
            ("h3", "Exercise"),
            ("ul", [
                "A quiz app exports its quizzes. It reads them from two sources, `sheet` "
                "and `editor`, and builds three representations: `web-page`, "
                "`print-sheet` and `answer-key`.",
                "Next term it must also build `audio`, a read-aloud version.",
            ]),
            ("p", "By hand, count the combinations, the classes with one class per pairing "
                  "and with directors and builders, and the classes <code>audio</code> "
                  "adds to each design. Then check in the lab, with the aspects in the "
                  "order reader, builder."),
            ("p", "A builder is an object handed to the director. The next lesson, Factory "
                  "Method, reads the chapter's one class creational pattern, in which a "
                  "class leaves the choice of what to create to its own subclasses."),
        ],
        "lab": ("gofkit", {
            "mode": "classes",
            "view": "explosion",
            "preset": "recipe-formats",
            "presets": [
                {"id": "recipe-formats",
                 "label": "A recipe book: three sources, four outputs, one more output",
                 "aspects": RECIPE_ASPECTS,
                 "added": "builder",
                 "expect": {"gclCombos": "3 × 4 = 12", "gclSubclass": "12 + 1 = 13", "gclCompose": "(3 + 1) + (4 + 1) = 9", "gclRatio": "13/9 ≈ 1.4×", "gclRefs": "1: builder", "gclAddSubclass": "3 (13 → 16)", "gclAddCompose": "1 (9 → 10)"}},
                {"id": "recipe-new-source",
                 "label": "The same recipe book gaining a fourth source",
                 "aspects": RECIPE_ASPECTS,
                 "added": "reader",
                 "expect": {"gclAddSubclass": "4 (13 → 17)", "gclAddCompose": "1 (9 → 10)"}},
                {"id": "recipe-one-source",
                 "label": "One source, four outputs",
                 "aspects": RECIPE_ONE_SOURCE,
                 "added": "-",
                 "expect": {"gclCombos": "1 × 4 = 4", "gclSubclass": "4 + 1 = 5", "gclCompose": "(1 + 1) + (4 + 1) = 7", "gclRatio": "5/7 ≈ 0.7×"}},
            ],
            "panel_title": "Pairings against directors and builders",
            "panel_intro": _GOF_INTRO,
        }),
        "steps_title": "Splitting a process from its outputs",
        "steps_intro": "Four steps, the last of them on code of your own.",
        "steps": [
            ("Find the construction process",
             "Name the code that walks an input or a plan and decides which part comes "
             "next. That is a director, and there may be several."),
            ("List the parts and the representations",
             "Write one builder operation per part the process can announce, and name "
             "each representation you need. An output that ignores most parts "
             "overrides few operations."),
            ("Count both designs",
             "Pairings give directors × builders + 1 classes; the split gives (directors "
             "+ 1) + (builders + 1). Add one of each side and see which design grows by "
             "a product and which by one class."),
            ("Do it on your own code",
             "Find an exporter, a report generator or a parser in a system you know. "
             "Count its inputs and its outputs, type them into the lab as reader and "
             "builder, and say whether its code today is written per pairing or split."),
        ],
        "worked": {
            "title": "Three sources, four outputs",
            "intro": [
                "Count <code>recipe-formats</code> and the nutrition card it adds.",
            ],
            "lines": [
                "recipe pairings: 3 sources × 4 outputs = 12",
                "as one class each: 12 + 1 base = 13",
                "split: (3 + 1) + (4 + 1) = 9 classes",
                "ratio 13/9, about 1.4",
                "a nutrition card as pairings: 3 classes",
                "as a builder: 1 class, 9 → 10",
            ],
            "after": [
                "Neither design edits an existing class for the new output, as the rules "
                "say; the difference is how many new classes repeat the parsing of each "
                "source.",
            ],
        },
        "quiz_title": "Directors, builders and the authors' claims",
        "quiz": [
            {"q": "In the exercise, how many classes does the quiz app need with one class "
                  "per pairing and with directors and builders, and how many does "
                  "<code>audio</code> add to each?",
             "a": ["7 and 7; audio adds 2 and 1",
                   "7 and 5; audio adds 2 and 1",
                   "6 and 7; audio adds 3 and 1",
                   "7 and 7; audio adds 1 and 1"],
             "c": 0,
             "why": "2 × 3 = 6 pairings plus the abstract base is 7; split, (2 + 1) + (3 + "
                    "1) = 7. As pairings, audio needs one class per source, 2; as a "
                    "builder it is 1. 5 leaves out the two abstract classes, and 6 the "
                    "base. The two designs are the same size today; they differ on the "
                    "next output."},
            {"q": "In Builder's collaborations, where does the client get the finished "
                  "product?",
             "a": ["From the director, when construction ends",
                   "From the builder, which the client asks for its product",
                   "From the abstract product's constructor",
                   "It assembles the parts the director returns to it"],
             "c": 1,
             "why": "The director only tells the builder which part comes next. The client "
                    "chose the builder and asks it for the result, which is why products "
                    "need no common parent class."},
            {"q": "How do the authors tell Builder from Abstract Factory in Related "
                  "Patterns?",
             "a": ["Builder makes families of products; Abstract Factory makes one product",
                   "Builder assembles one complex product step by step and returns it at "
                   "the end; Abstract Factory is about families and returns each product "
                   "at once",
                   "Builder needs a Singleton; Abstract Factory does not",
                   "Builder can only build Composite structures"],
             "c": 1,
             "why": "Both can make complex objects; the difference is the step-by-step "
                    "construction and when the product is handed over. The first option "
                    "swaps the two patterns. A builder often builds a Composite, but "
                    "nothing limits it to one."},
            {"q": "Why do the authors say a Builder's products often have no common "
                  "abstract class?",
             "a": ["Because C++ cannot give two unrelated classes a parent",
                   "Because the representations differ so much there is little to share, "
                   "and the client that chose the builder knows what it gets",
                   "Because all the products are made by one concrete builder",
                   "Because each product is made by cloning"],
             "c": 1,
             "why": "Plain text and an interactive widget have little in common, and since "
                    "the client configured the director with a particular builder, it can "
                    "handle that builder's product directly. Each concrete builder makes "
                    "its own kind of product, and cloning is Prototype's method."},
        ],
        "mistakes": [
            ("Putting the construction process inside the builder",
             "If each builder walks the input itself, every new output repeats the "
             "parsing, which is the one-class-per-pairing design under another name; on "
             "the recipe book the lab counts 3 new classes for one output that way "
             "against 1. The director owns the process and the builder only answers its "
             "calls, which is what lets the book's SGML reader reuse the RTF converters."),
            ("Expecting every builder to implement every part",
             "The abstract builder's operations do nothing by default, so a builder "
             "overrides only the parts it represents; the book's ASCII converter, like "
             "the shopping list here, ignores most of what the director announces."),
            ("Asking the director for the result",
             "The director knows the steps, not the product's type. The client chose "
             "the builder, so the client asks the builder for what it built, and "
             "different builders may return wholly unrelated types."),
        ],
        "standard": (
            "Finish when you can split a construction process from its representations and count both designs.",
            "Given the sources and outputs of a design, state the classes with one class "
            "per pairing and with directors and builders, what a new source and a new "
            "output each add, and the three consequences the authors list."
        ),
        "note": (
            "The lab counts directors and builders from the sources and outputs you "
            "state, and leaves the products out. It cannot tell whether your outputs "
            "really come from one construction process, or whether a second source will "
            "ever arrive; with a single source the split costs classes, and the case for "
            "it rests on what is expected to vary."
        ),
    },
    # ---------------------------------------------------------------- 03
    # Factory Method (PDF pp. 127-136 of the operator's copy); the Discussion's
    # remark on when a factory method is unnecessary, p. 156.
    # Quote: PDF p. 127 of the operator's copy, 15 words, quotes.py OK.
    # Lesson total: 15 words.
    {
        "slug": "factory-method",
        "title": "Factory Method",
        "module": "Chapter 3 · Creational Patterns",
        "one_line": "An overridable operation that creates an object, so a class can say when one is needed and leave which class it is to its subclasses.",
        "summary": (
            "Factory Method is the chapter's one class creational pattern: a class "
            "declares an operation that makes an object, and its subclasses decide what "
            "it makes. Read the pattern, then count the creator and product classes an "
            "irrigation controller needs, and what a new zone type adds."
        ),
        "key": [
            "subclasses decide what to instantiate",
            "the creator knows when, not which class",
            "a factory method is a hook",
            "creators run parallel to products",
            "a new product: a creator and a product",
            "pass an identifier for many products",
        ],
        "key_label": "Factory Method in six lines",
        "concepts_intro": "Three terms carry the lesson, all of them the pattern's.",
        "concepts": [
            ("Factory method",
             "An operation, declared in a class, whose job is to create and return an "
             "object of some product type. Subclasses override it to choose the "
             "concrete product; the class that declares it calls it without knowing "
             "which class it gets."),
            ("Creator and product hierarchies",
             "The Creator declares the factory method and usually calls it; each "
             "ConcreteCreator overrides it. When each creator subclass makes its own "
             "product subclass the two hierarchies run in parallel, and the factory "
             "method records which classes go together."),
            ("Parameterized factory method",
             "A factory method that takes an identifier of the kind to create, so one "
             "operation can make several products. A subclass can override it for a few "
             "identifiers and pass the rest back to its parent."),
        ],
        "read_title": "The pattern first, then the count",
        "read_intro": (
            "Read Factory Method in your own copy first. The lesson reads it as a tool, "
            "section by section, and then counts the classes of a small design."
        ),
        "body": [
            ("p", "&ldquo;Define an interface for creating an object, but let subclasses "
                  "decide which class to instantiate.&rdquo; So begins the intent of "
                  "Factory Method, also known as Virtual Constructor, the third pattern "
                  "of Chapter 3 and its only class creational one: it works by "
                  "inheritance, where the others hand creation to an object. Read the "
                  "pattern in your own copy first. The lesson reads it as a tool, then "
                  "counts the classes a creator hierarchy and its products need, and what "
                  "a new product costs."),
            ("p", "The motivating example is a framework for applications that manage "
                  "several documents. Its two central classes, Application and Document, "
                  "are both abstract, and a drawing program subclasses both. The "
                  "framework knows when a new document is needed, when the user chooses "
                  "Open or New, but not which document class to make, and it cannot "
                  "instantiate an abstract class. So Application declares an abstract "
                  "operation that creates a document, each application subclass overrides "
                  "it to return its own document class, and the framework calls it. That "
                  "operation is the factory method: it carries one piece of knowledge, "
                  "which class, out of the framework and into the subclass."),
            ("p", "The pattern applies when a class cannot know in advance which class "
                  "its objects must be, when a class would rather its subclasses chose, and when "
                  "a class passes work to a helper whose subclass varies, and the choice "
                  "of subclass should be made in one place. The participants "
                  "are the Product interface, the ConcreteProducts, the Creator, which "
                  "declares the factory method, may give it a default and calls it, and "
                  "the ConcreteCreators, which override it. The one collaboration is that "
                  "the Creator relies on its subclasses for the right product."),
            ("code", _lines(ZONE_JAVA)),
            ("p", "The central consequence is that factory methods keep "
                  "application-specific classes out of the code that uses them: the "
                  "framework deals with the Product interface and so works with any "
                  "concrete product a user defines. The potential disadvantage, the "
                  "authors say, is that a client may have to subclass the Creator just to "
                  "make a particular product, which is harmless when it was subclassing "
                  "anyway and otherwise one more thing that can change. Two more "
                  "consequences follow. A factory method is a hook for subclasses, and it "
                  "can have a sensible default, as a document's operation for making its "
                  "file dialog might. And factory methods connect parallel class "
                  "hierarchies. In the book's example, figures that can be dragged and "
                  "stretched hand the interaction to separate manipulator objects, each "
                  "figure class needing its own kind; a factory method on the figure "
                  "makes the matching manipulator, and so records which classes belong "
                  "together, while figures that inherit a default manipulator leave the "
                  "hierarchies only partly parallel."),
            ("p", "Implementation names five issues. There are two main varieties, an "
                  "abstract Creator with no default, which forces each subclass to "
                  "decide, and a concrete Creator with a default, which uses the factory "
                  "method so that a subclass can change what its parent makes. A "
                  "parameterized factory method takes an identifier and makes one of "
                  "several products; the Unidraw framework used one to rebuild objects "
                  "read back from disk by their class identifiers. Languages differ: "
                  "Smalltalk can return the class to instantiate, and in C++ a factory "
                  "method must not be called from the Creator's constructor, before the "
                  "subclass's override is in place, which an accessor that creates the "
                  "product on first use avoids. A C++ template subclass of Creator, "
                  "parameterized by the product class, saves writing a creator subclass "
                  "per product. And a naming convention, such as the common prefix "
                  "MacApp gives its factory methods, shows a reader where they are."),
            ("p", "In Java 8 the nearest thing to that template is to pass the product's "
                  "constructor as a value, a <code>Supplier&lt;Schedule&gt;</code> such "
                  "as <code>DripSchedule::new</code>. That is composition rather than "
                  "subclassing, and it brings the design close to the next lesson's "
                  "Prototype and to Abstract Factory, which is the chapter's closing "
                  "argument in miniature. In Java, unlike C++, an override called from a "
                  "constructor does run, before the subclass's own fields are set, which "
                  "is a hazard of its own."),
            ("code", _lines(ZONE_SUPPLIER_JAVA)),
            ("p", "The Sample Code gives the maze game a factory method for the maze and "
                  "each kind of part, rewrites the maze routine to call them, and "
                  "overrides a few of them in bombed and enchanted game subclasses; read "
                  "it in the book. The known uses are many, since factory methods are "
                  "everywhere in toolkits and frameworks: the document example in MacApp "
                  "and ET++, Unidraw's manipulators, the Smalltalk-80 view whose default "
                  "controller's class is the real factory method, a class choosing the "
                  "parser for its own source code, and the Orbix broker choosing a proxy "
                  "for a remote object. The related patterns: Abstract Factory is often "
                  "built from factory methods; factory methods are usually called inside "
                  "Template Methods; and Prototype needs no Creator subclass, though it "
                  "often needs an initialising operation on the product, which Factory "
                  "Method does not."),
            ("p", "Now the lab, on a garden irrigation controller rather than a document "
                  "framework. The controller's abstract Zone runs a watering cycle and "
                  "asks its factory method for a schedule; three concrete zones, lawn, "
                  "bed and greenhouse, each make their own schedule class. In the lab's "
                  "terms that is 3 families and 1 kind of product. On the preset "
                  "<code>zones</code> there are 3 × 1 = 3 concrete products, and the "
                  "classes add up as 1 abstract creator, 3 concrete creators, 1 abstract "
                  "product and 3 concrete products, 1 + 3 + 1 + 3 = 8, of which 1 + 3 = 4 "
                  "create. The prototype configuration tile reads none: only Prototype "
                  "configures instances."),
            ("p", "On <code>zones-new-zone</code> a fourth zone type, a row of pots on "
                  "drip lines, adds 2 classes, 1 concrete creator and 1 concrete product, "
                  "taking the design from 8 to 10, and edits none. Nothing written "
                  "changes, and since a pot zone also supplies its own valves, its creator "
                  "subclass is the harmless case the authors name, one the client needed "
                  "anyway; had zones differed only in schedules, it would exist just to "
                  "make one product. The preset <code>zones-new-kind</code> asks for a "
                  "second kind of product, a moisture sensor per zone. The lab counts the "
                  "book's own shape, the one its maze game has: the abstract Zone declares "
                  "a second factory method and every zone overrides it. That adds 4 "
                  "classes, 1 abstract sensor and 3 concrete ones, 8 to 12, and edits 4, "
                  "the abstract creator and its 3 concrete creators. Those are exactly the "
                  "Abstract Factory lesson's counts, because the two patterns have the "
                  "same shape here: an abstract factory is often a set of factory methods. "
                  "What differs is where the choice is made, in a subclass of the class "
                  "that uses the products or in a separate object handed to it."),
            ("h3", "Exercise"),
            ("ul", [
                "A vending machine framework has an abstract `Slot` whose factory method "
                "creates the slot's dispenser.",
                "Four slot types, `can`, `bottle`, `snack` and `hot-drink`, each "
                "override it to make their own dispenser class.",
            ]),
            ("p", "By hand, count the concrete products, the classes in the design, the "
                  "classes that create, and what a fifth slot type adds and edits. Then "
                  "type it into the lab as four families and one kind under the "
                  "factory-method scheme, and check."),
            ("p", "A creator subclass for every product is the cost this lesson counted. "
                  "The next lesson, Prototype, reads the pattern that does without the "
                  "creator hierarchy by copying an instance instead."),
        ],
        "lab": ("gofkit", {
            "mode": "classes",
            "view": "factory",
            "families": ZONE_FAMILIES,
            "kinds": ZONE_KINDS,
            "scheme": "factory-method",
            "preset": "zones",
            "presets": [
                {"id": "zones",
                 "label": "An irrigation controller: three zone types, one schedule each",
                 "change": "none",
                 "expect": {"gclProducts": "3 × 1 = 3", "gclClasses": "1 + 3 + 1 + 3 = 8", "gclFactories": "1 + 3 = 4", "gclConfigs": "none: the factory classes themselves fix what is made"}},
                {"id": "zones-new-zone",
                 "label": "The same controller gaining a fourth zone type",
                 "change": "family",
                 "expect": {"gclAdded": "2 (8 → 10): 1 concrete creator, 1 concrete product", "gclChanged": "0"}},
                {"id": "zones-new-kind",
                 "label": "The same controller gaining a second kind of product",
                 "change": "kind",
                 "expect": {"gclAdded": "4 (8 → 12): 1 abstract product, 3 concrete products", "gclChanged": "4: the abstract creator and 3 concrete creators, each given a factory method for the new kind"}},
            ],
            "panel_title": "Creators, products and what a new product costs",
            "panel_intro": _GOF_INTRO,
        }),
        "steps_title": "Introducing a factory method",
        "steps_intro": "Four steps, the last of them on code of your own.",
        "steps": [
            ("Find the line that names a class",
             "Look for the place where a general class constructs a specific one. The "
             "general class knows when the object is needed; the specific class is "
             "what varies."),
            ("Move the construction into an operation",
             "Replace the constructor call with a call to a protected factory method "
             "that returns the product interface, abstract or with a default."),
            ("Count the creators",
             "Each concrete product needs a creator subclass that overrides the factory "
             "method, unless a default or a passed-in constructor serves. Count "
             "creators against products."),
            ("Do it on your own code",
             "Find a hook in a system you know that subclasses override to supply an "
             "object, such as a test base class or a plug-in point. Count its creator "
             "subclasses and products in the lab, and note how many creators exist only "
             "to make one product."),
        ],
        "worked": {
            "title": "Three zones, one product each",
            "intro": [
                "Count <code>zones</code> and <code>zones-new-zone</code>.",
            ],
            "lines": [
                "zone products: 3 zones × 1 kind = 3",
                "zone classes: 1 + 3 + 1 + 3 = 8",
                "classes that create: 1 + 3 = 4",
                "pots add 1 zone class and 1 schedule",
                "a sensor kind adds 1 + 3 = 4, edits 4",
                "edits none; the design goes 8 → 10",
            ],
            "after": [
                "Each zone subclass also supplies its valves, the harmless case; one that "
                "existed only to pick a schedule would be the disadvantage, and a template "
                "or a prototype the way round it.",
            ],
        },
        "quiz_title": "Creators, products and the authors' claims",
        "quiz": [
            {"q": "In the exercise (four slot types, Factory Method), how many classes does "
                  "the design have, how many create, and what does a fifth slot type add "
                  "and edit?",
             "a": ["10 classes, 5 create; a fifth adds 2 and edits 0",
                   "9 classes, 5 create; a fifth adds 2 and edits 0",
                   "10 classes, 5 create; a fifth adds 1 and edits 0",
                   "10 classes, 4 create; a fifth adds 2 and edits 1"],
             "c": 0,
             "why": "1 abstract Slot + 4 slot subclasses + 1 abstract dispenser + 4 "
                    "concrete dispensers = 10, of which the 1 + 4 = 5 creator classes "
                    "create. A fifth type adds its slot subclass and its dispenser, 2, and "
                    "edits nothing, since the abstract Slot already declares the factory "
                    "method. 9 leaves out the abstract product; adding only 1 forgets the "
                    "creator subclass."},
            {"q": "What potential disadvantage do the authors name for Factory Method?",
             "a": ["The client must know every concrete product class",
                   "A client may have to subclass the Creator just to make a particular "
                   "product",
                   "The Creator's interface fixes the set of kinds of product",
                   "Every product must implement a clone operation"],
             "c": 1,
             "why": "The first is what the pattern removes. A fixed set of kinds is "
                    "Abstract Factory's liability, and a clone operation on every class "
                    "is Prototype's."},
            {"q": "Why do the authors warn against calling a factory method from the "
                  "Creator's constructor in C++?",
             "a": ["The concrete creator's override is not yet in effect there",
                   "A constructor cannot return an object",
                   "It would create a second Creator",
                   "A factory method must be a static member function"],
             "c": 0,
             "why": "While the Creator part of an object is being constructed, C++ calls "
                    "the Creator's own version, so the subclass's choice is not made. The "
                    "authors' remedy is an accessor that creates the product on first "
                    "use. A factory method is an ordinary overridable operation, never "
                    "static."},
            {"q": "In the book's figure-and-manipulator example, what does the factory "
                  "method do?",
             "a": ["It lets each figure create the manipulator that matches it, "
                   "connecting two parallel hierarchies",
                   "It lets the framework create documents of the application's class",
                   "It copies a prototypical manipulator",
                   "It makes sure there is only one manipulator"],
             "c": 0,
             "why": "Each figure class overrides an operation that returns its own kind of "
                    "manipulator, so the factory method records which classes belong "
                    "together. Documents are the Motivation's separate example; copying "
                    "and a sole instance are Prototype and Singleton."},
        ],
        "mistakes": [
            ("Thinking Factory Method needs no extra classes",
             "The factory method is one operation, but each concrete product usually "
             "needs a creator subclass to return it, 4 creating classes for 3 products on "
             "the irrigation controller. Where the subclass exists anyway, as each zone "
             "does for its valves, that costs nothing; where it exists only to pick a "
             "product, the authors call it the pattern's potential disadvantage, and offer "
             "a template, and later Prototype, as ways round it."),
            ("Putting a factory method behind every constructor call",
             "The Discussion of Creational Patterns says factory methods are not needed "
             "when the class instantiated never changes, or when the making already "
             "happens in an operation subclasses can override. A factory method is a "
             "hook for what varies."),
            ("Calling the factory method from the creator's constructor",
             "In C++ the subclass's override is not yet in effect there; in Java it runs "
             "before the subclass's fields are set. The authors' remedy is an accessor "
             "that creates the product on first use."),
        ],
        "standard": (
            "Finish when you can count a creator hierarchy and the product hierarchy it parallels.",
            "Given the products of a design under Factory Method, state its classes and "
            "creators, what a new product adds and edits, the pattern's disadvantage, and "
            "the two further consequences the authors list."
        ),
        "note": (
            "The lab counts one concrete creator per family, from the zones and kinds "
            "you state. A creator with a sensible default, a parameterized factory "
            "method or a passed-in constructor needs fewer, and whether the subclasses "
            "would exist anyway, which decides whether the cost is real, is for you to "
            "judge."
        ),
    },
    # ---------------------------------------------------------------- 04
    # Prototype (PDF pp. 137-146 of the operator's copy); shallow versus deep
    # copy, p. 141.
    # Quotes: PDF p. 137 of the operator's copy, 19 words, quotes.py OK;
    # PDF p. 141, 11 words, quotes.py OK.
    # Lesson total: 30 words.
    {
        "slug": "prototype",
        "title": "Prototype",
        "module": "Chapter 3 · Creational Patterns",
        "one_line": "New objects made by copying a sample instance, which forces the question of what a copy shares with the sample it was made from.",
        "summary": (
            "Prototype makes new objects by asking a sample instance to copy itself, "
            "which removes the factory classes and brings what the authors call its "
            "hardest part, implementing the copy correctly, and with it the question of "
            "what a clone shares. Read the pattern, then count who sees a "
            "change made through one clone of a playlist, under shallow and deep "
            "copies."
        ),
        "key": [
            "copy a sample instead of naming a class",
            "register prototypes while running",
            "variants by value, not by subclass",
            "a shallow copy shares every part",
            "a deep copy owns its parts",
            "share only what cannot change",
        ],
        "key_label": "Prototype in six lines",
        "concepts_intro": "Three terms carry the lesson, all of them the pattern's.",
        "concepts": [
            ("Prototype",
             "An instance kept as a sample of what to create. A client makes new objects "
             "by asking it to copy itself, so the client needs neither the product's "
             "class nor a factory class for it."),
            ("Prototype manager",
             "A registry that stores prototypes under keys, so that clients can "
             "register, look up, replace and remove them while the program runs, and "
             "clone by name."),
            ("Shallow and deep copy",
             "A shallow copy duplicates the object and shares everything it refers to "
             "with the original; a deep copy duplicates those parts as well, so original "
             "and clone are independent. Cloning makes you choose, part by part, what "
             "is shared."),
        ],
        "read_title": "The pattern first, then the count",
        "read_intro": (
            "Read Prototype in your own copy first. The lesson reads it as a tool, "
            "section by section, and then counts who shares what after cloning."
        ),
        "body": [
            ("p", "&ldquo;Specify the kinds of objects to create using a prototypical "
                  "instance, and create new objects by copying this prototype.&rdquo; "
                  "That is the intent of Prototype, the fourth pattern of Chapter 3 and "
                  "an object creational pattern. Read it in your own copy first. The "
                  "lesson reads it as a tool, then turns to what the authors call "
                  "the pattern's hardest part, implementing the clone operation "
                  "correctly, and to the question inside it of what a clone shares with "
                  "its prototype, and counts who sees a change made through one clone."),
            ("p", "The book's example is a music score editor built by customising a "
                  "general framework for graphical editors. The framework supplies a tool "
                  "class that creates a graphic and adds it to the document, but it "
                  "cannot know the application's note and staff classes, and a subclass "
                  "of the tool for every kind of note would multiply classes that differ "
                  "only in what they make. So each palette tool is an instance of the one "
                  "tool class, given a different prototype graphic to clone. The authors "
                  "then go further: whole notes and half notes need not be classes at "
                  "all, but instances of one note class with different images and "
                  "durations, each installed as a prototype."),
            ("p", "Prototype applies when a system should not care how its products "
                  "are made and, besides, when the classes to create are known "
                  "only at run time, loaded dynamically for instance; when you want "
                  "no factory classes shadowing the product classes one for one; "
                  "or when a class's instances come in only a few combinations of state, "
                  "so that keeping one prototype per combination is simpler than setting "
                  "the state by hand each time. The participants are the Prototype, which "
                  "declares the operation that copies it; the ConcretePrototypes, "
                  "which implement it; and the Client, which asks a prototype for a copy "
                  "of itself whenever it needs a new object."),
            ("code", _lines(PLAYLIST_JAVA)),
            ("p", "Prototype shares the main consequences of Abstract Factory and Builder: "
                  "it keeps the concrete product classes out of the client's sight, so "
                  "the client knows fewer names, and lets a client work with application-specific "
                  "classes unchanged. The authors add five of its own. Products can be "
                  "added and removed while the program runs, by registering a prototype. "
                  "New kinds of object can be specified by values rather than new "
                  "classes, which lets users define something close to new classes "
                  "without programming. New objects can be specified by structure, as "
                  "when a circuit editor offers a user's subcircuit as a palette item, "
                  "provided the clone is deep. Subclassing is reduced, since no Creator "
                  "hierarchy is needed, a gain mostly in C++ and other languages in "
                  "which a class is not an object. And an application can be configured with "
                  "classes loaded while it runs. The main liability is that every "
                  "prototype class must implement cloning, which is hard to add to "
                  "classes that already exist, and hard when they hold objects that "
                  "cannot be copied or that refer to each other in a cycle."),
            ("p", "&ldquo;Cloning forces you to decide what if anything will be "
                  "shared.&rdquo; That sentence closes the authors' discussion of shallow "
                  "and deep copying, the second of three implementation issues. A shallow "
                  "copy, Smalltalk's default and what C++'s default memberwise copy gives, "
                  "shares every referenced part between original and clone; it is simple "
                  "and often enough. A prototype with structure usually needs a deep "
                  "copy, so that the clone's parts are clones of the prototype's parts, "
                  "and saving an object and loading it straight back is one way to get "
                  "one. The first issue is the prototype manager, a store keyed by name "
                  "with operations to register and unregister, which clients can change "
                  "and browse at run time. The third is initialising clones: a uniform "
                  "clone operation cannot take arguments, so clients reset state after "
                  "cloning, through existing setters or a separate initialise operation. "
                  "Java's own <code>Object.clone</code> copies fields one for one, a "
                  "shallow copy, which is why the sketch writes both copies out."),
            ("code", _lines(TEMPLATES_JAVA)),
            ("p", "The Sample Code makes a maze factory that is given a prototype maze, "
                  "room, wall and door and clones them, so a new kind of maze is a new "
                  "set of prototypes rather than a new factory subclass; a cloned door is "
                  "then given its rooms by an initialise operation, and a Smalltalk "
                  "version keeps a dictionary of prototypes. Read it in the book. The "
                  "known uses reach back to Ivan Sutherland's Sketchpad and to ThingLab; "
                  "Goldberg and Robson name prototypes as a pattern and Coplien "
                  "describes C++ idioms for them; the etgdb debugger front end clones the "
                  "debugger adaptor an environment variable names; Mode Composer keeps "
                  "interaction techniques as prototypes; and the music editor is based on "
                  "Unidraw. The related patterns: Prototype competes with Abstract Factory "
                  "in some designs, the subject of the chapter's discussion, and can serve "
                  "it, a factory holding prototypes to clone; and designs heavy with "
                  "Composite and Decorator often gain from it."),
            ("p", "Now the lab, on a music playlist app rather than a score editor. A "
                  "template playlist, a workout mix, is the prototype, and three runners "
                  "clone it. The lab's sharing view asks who holds which track list and "
                  "what a change made through one holder reaches; its panel speaks of a "
                  "model, a value and holders, which here are the design, the track list "
                  "and the template with its clones. On the preset "
                  "<code>shallow-clones</code> the copies are shallow, so the template "
                  "and all three clones hold the one list <code>tracks-w</code>. Ben adds "
                  "a track through his copy: the lab counts 4 holders, 4 that see the "
                  "change, 3 surprised, the template, Ana and Cy, who saw a change they "
                  "did not make, and 0 new values. The template is among the surprised, "
                  "so every clone made from it later starts with Ben's track."),
            ("p", "On <code>deep-clones</code> each copy has its own list, and Ben's "
                  "change to <code>tracks-b</code> reaches 1 holder, himself, with none "
                  "surprised: the clones are independent, at the price of a list copied "
                  "for every clone, which this view does not count. The preset "
                  "<code>shallow-immutable</code> shares one list again, but an immutable "
                  "one: a change made through Ben gives him a new list, "
                  "<code>tracks-w′</code> in the lab, so 1 holder sees it, none are "
                  "surprised, and 1 new value is made. A shallow copy is safe for any "
                  "part that cannot change, which is why the decision the authors "
                  "describe is made part by part."),
            ("h3", "Exercise"),
            ("ul", [
                "A quiz app keeps a multiple-choice template, `mc-template`, and clones "
                "it for four questions. Three clones, `q1`, `q2` and `q4`, are shallow "
                "and share the template's options list `opts`; `q3` was deep-copied and "
                "holds `opts-3`.",
                "Through `q2`, an option in `opts` is reworded.",
            ]),
            ("p", "Count, for a mutable and then an immutable options list, the holders of "
                  "<code>opts</code>, the holders that see the change, the holders "
                  "surprised and the new values made. Then type the holders into the lab "
                  "and check."),
            ("p", "A prototype manager is one object that every client must reach. The "
                  "next lesson, Singleton, reads the pattern for a class that has exactly "
                  "one instance."),
        ],
        "lab": ("dddkit", {
            "mode": "identity",
            "view": "sharing",
            "preset": "shallow-clones",
            "presets": [
                {"id": "shallow-clones",
                 "label": "Three shallow clones of a playlist template",
                 "holders": SHALLOW_HOLDERS,
                 "value": "tracks-w",
                 "change": "ben-run",
                 "kind": "mutable",
                 "expect": {"didHolders": "4: template, ana-run, ben-run, cy-run", "didSee": "4: template, ana-run, ben-run, cy-run", "didSurprised": "3: template, ana-run, cy-run", "didNew": "0"}},
                {"id": "deep-clones",
                 "label": "Three deep clones of the same template",
                 "holders": DEEP_HOLDERS,
                 "value": "tracks-b",
                 "change": "ben-run",
                 "kind": "mutable",
                 "expect": {"didHolders": "1: ben-run", "didSee": "1: ben-run", "didSurprised": "0: none", "didNew": "0"}},
                {"id": "shallow-immutable",
                 "label": "Shallow clones sharing an immutable track list",
                 "holders": SHALLOW_HOLDERS,
                 "value": "tracks-w",
                 "change": "ben-run",
                 "kind": "immutable",
                 "expect": {"didSee": "1: ben-run", "didSurprised": "0: none", "didNew": "1: tracks-w′, now held by ben-run"}},
            ],
            "panel_title": "Who sees a change made through one clone",
            "panel_intro": (
                "The lab counts one consequence of how a prototype is copied; how to "
                "copy each part is weighed in the book, against what in the design is "
                "expected to change."
            ),
        }),
        "steps_title": "Making new objects by copying",
        "steps_intro": "Four steps, the last of them on code of your own.",
        "steps": [
            ("Find the classes that differ only in values",
             "Look for subclasses, or factory subclasses, whose only job is to set "
             "different values. Each could be one class with a prototype per variant."),
            ("Decide part by part what a clone shares",
             "For each field of the prototype, ask whether it can change after cloning. "
             "Share what cannot; copy what can."),
            ("Register the prototypes",
             "Keep the prototypes in a manager keyed by name, so that a new variant is "
             "registered while the program runs instead of written as a class."),
            ("Do it on your own code",
             "Find an object in a system you know that is copied to make new ones: a "
             "template, a default configuration, a test fixture. List who holds its "
             "changeable parts after copying, type them into the lab, and count the "
             "holders one change surprises."),
        ],
        "worked": {
            "title": "One template, three runners",
            "intro": [
                "Count <code>shallow-clones</code>, then <code>deep-clones</code>.",
            ],
            "lines": [
                "shallow: template, Ana, Ben, Cy share one list",
                "Ben adds a track: 4 holders see it",
                "surprised: template, Ana and Cy, so 3",
                "deep: Ben's list is his alone",
                "Ben's change: 1 sees it, none surprised",
            ],
            "after": [
                "The template counted among the surprised is the costly one: every runner "
                "who clones it next starts with Ben's track.",
            ],
        },
        "quiz_title": "Clones, sharing and the authors' claims",
        "quiz": [
            {"q": "In the exercise, the change is made through q2 to opts. What are the "
                  "holders that see it and the holders surprised, first for a mutable "
                  "list and then for an immutable one?",
             "a": ["Mutable: 4 see it, 3 surprised. Immutable: 1 sees it, 0 surprised",
                   "Mutable: 5 see it, 4 surprised. Immutable: 1 sees it, 0 surprised",
                   "Mutable: 4 see it, 4 surprised. Immutable: 1 sees it, 0 surprised",
                   "Mutable: 3 see it, 2 surprised. Immutable: 1 sees it, 0 surprised"],
             "c": 0,
             "why": "opts is held by mc-template, q1, q2 and q4: 4 holders, all of whom "
                    "see a change made in place, and the three that did not make it, the "
                    "template, q1 and q4, are surprised. q3 holds its own opts-3 and is "
                    "not counted, which rules out 5; the template holds opts too, which "
                    "rules out 3. Immutable: q2 is given a new list, 1 new value, so 1 "
                    "sees the change and 0 are surprised."},
            {"q": "What do the authors give as Prototype's main liability?",
             "a": ["Every prototype class must implement cloning, which can be hard",
                   "A new kind of product means changing every factory",
                   "It needs a creator hierarchy parallel to the products",
                   "Clients must know the concrete product classes"],
             "c": 0,
             "why": "Cloning is hard to add to classes that exist, and hard for objects "
                    "that cannot be copied or that refer to each other in cycles. Editing "
                    "every factory is Abstract Factory's liability; the creator hierarchy "
                    "is what Prototype removes; and hiding concrete classes is one of its "
                    "benefits."},
            {"q": "In the music editor, how does the framework's one tool class come to "
                  "create notes it knows nothing of?",
             "a": ["Each palette tool is an instance of it, given a different prototype "
                   "graphic to clone",
                   "The application subclasses the tool class once per kind of note",
                   "The tool reads each note's class name from a file",
                   "Each note class registers itself as a Singleton"],
             "c": 0,
             "why": "The tool is parameterized by an instance, not by a subclass. A "
                    "subclass per kind of note is the design the authors set aside as "
                    "producing many classes that differ only in what they make."},
            {"q": "What does a shallow copy of a prototype share with the original?",
             "a": ["Nothing; it duplicates every part",
                   "Every object the original refers to",
                   "Only the parts that are immutable",
                   "Only its class"],
             "c": 1,
             "why": "A shallow copy duplicates the object and shares every referenced part, "
                    "changeable or not. Sharing only the immutable parts is a choice a "
                    "hand-written copy makes, part by part; duplicating every part is a "
                    "deep copy."},
        ],
        "mistakes": [
            ("Assuming a copy is independent of its prototype",
             "A shallow copy shares every part the prototype refers to. On the playlist "
             "the lab counts 3 holders surprised by one runner's change, the template "
             "among them, so every later clone inherits it. The authors put it plainly: "
             "cloning makes you decide what is shared."),
            ("Deep-copying everything to be safe",
             "A deep copy costs an object per part for every clone, and is wrong for "
             "parts meant to be shared, such as a connection to a service. A part that "
             "cannot change can be shared by a shallow copy, as the immutable preset "
             "shows."),
            ("Passing initial values through the clone operation",
             "Prototypes of different classes need different values, so a clone "
             "operation with parameters cannot be uniform. The authors reset state after "
             "cloning, through setters or an initialise operation."),
        ],
        "standard": (
            "Finish when you can say what a clone shares and count who sees a change.",
            "Given a prototype, its clones and the parts each holds, state who sees a "
            "change made through one clone under shallow and deep copying, and the "
            "consequences and the liability the authors list."
        ),
        "note": (
            "The lab counts who holds a shared part and who sees a change to it. It "
            "cannot tell which parts of your prototype will change after cloning, what a "
            "deep copy costs, or whether a part is meant to be shared; those decide, part "
            "by part, how a clone should be made."
        ),
    },
    # ---------------------------------------------------------------- 05
    # Singleton (PDF pp. 147-154 of the operator's copy).
    # Quote: PDF p. 147 of the operator's copy, 16 words, quotes.py OK.
    # Lesson total: 16 words. The course's one modern aside is in this lesson.
    {
        "slug": "singleton",
        "title": "Singleton",
        "module": "Chapter 3 · Creational Patterns",
        "one_line": "A class that keeps its one instance itself and gives every client a single, well-known way to reach it.",
        "summary": (
            "Singleton makes a class responsible for having exactly one instance and for "
            "handing it out. Read the pattern, its five benefits and the costs its "
            "implementation section admits, then count the instances and the cost a "
            "parcel locker network's requests run up when each makes its own registry, "
            "when one is made on first use, and when all are made at start-up."
        ),
        "key": [
            "exactly one instance, one access point",
            "the class keeps its sole instance",
            "hide the constructor",
            "create it on first use",
            "only the access operation must change",
            "a registry chooses the subclass",
        ],
        "key_label": "Singleton in six lines",
        "concepts_intro": (
            "Three terms carry the lesson. The first is the pattern; the other two come "
            "from its implementation section."
        ),
        "concepts": [
            ("Singleton",
             "A class that makes sure it has one instance and gives every client one "
             "well-known way to reach it, through a class operation rather than a "
             "global variable."),
            ("Lazy initialisation",
             "Creating the instance the first time it is asked for, not when the program "
             "starts. The instance is made only if it is used, and with whatever the "
             "program knows by then."),
            ("Registry of singletons",
             "A well-known table in which singleton classes register their instance by "
             "name, so the access operation can hand out the one chosen at run time "
             "without listing every possible subclass."),
        ],
        "read_title": "The pattern first, then the count",
        "read_intro": (
            "Read Singleton in your own copy first. The lesson reads it as a tool, sets "
            "its benefits beside its costs, and then counts instances and cost."
        ),
        "body": [
            ("p", "&ldquo;Ensure a class only has one instance, and provide a global "
                  "point of access to it.&rdquo; That is the intent of Singleton, the "
                  "last pattern of Chapter 3 and an object creational pattern. Read it in "
                  "your own copy first. The lesson reads it as a tool, sets its benefits "
                  "beside the costs its implementation section admits, and counts the "
                  "instances and the cost a run of requests adds up to with one shared "
                  "instance and without."),
            ("p", "The motivation is a short list of things a system should have only "
                  "one of: one printer spooler however many printers, one file system, "
                  "one window manager, one company served by an accounting system. A "
                  "global variable makes an object easy to reach but does nothing to stop "
                  "a second one being made. The authors' answer is to make the class "
                  "itself responsible: it keeps track of its sole instance, intercepts "
                  "requests to create new ones, and offers a way to get the one it has."),
            ("p", "Singleton fits, in the authors' list, when a second instance would "
                  "be an error and every client needs one known place to find the first, "
                  "and when that one object may later belong to a subclass, chosen "
                  "without touching the clients' code. There is one participant, the Singleton class, with an "
                  "Instance operation that is a class operation, a static method in Java "
                  "as in C++, and that may create the instance itself. Clients reach the "
                  "instance only through that operation."),
            ("code", _lines(REGISTRY_JAVA)),
            ("p", "The authors list five benefits. Access to the sole instance is "
                  "controlled, because the class holds it. The name space is reduced, an "
                  "improvement on global variables that would each hold a sole instance. "
                  "Operations and representation can be refined, by subclassing the "
                  "Singleton and configuring the application with the subclass's "
                  "instance. A variable number of instances is easy, since only the "
                  "access operation changes if you later want two, or a fixed pool. And "
                  "the pattern is more flexible than class operations, static methods, "
                  "which make that change hard and which in C++ are never virtual, so a "
                  "subclass cannot override them."),
            ("p", "The costs are in the implementation section. To ensure a unique "
                  "instance the constructor is hidden, protected in the book's C++ and "
                  "private here, and the class operation creates the instance lazily, on "
                  "first access. The authors explain why a C++ global or static object "
                  "will not do: nothing stops a second one being declared, the values it "
                  "needs may not be known when static objects are initialised, and C++ "
                  "fixes no order of initialisation across files, so singletons that "
                  "depend on each other fail; and a static object forces every singleton "
                  "to be made whether used or not. Subclassing is harder still. Choosing "
                  "the subclass inside the access operation with conditionals hard-wires "
                  "the set of subclasses; choosing at link time fixes it before the "
                  "program runs; a registry, in which each singleton registers itself by "
                  "name, frees the access operation from knowing the subclasses, but only "
                  "if every candidate is created so that it can register. The section "
                  "does not discuss threads; in Java the lazy check must be safe for "
                  "them, which is why the sketch's method is synchronized."),
            ("p", "The Sample Code makes the maze factory of the Abstract Factory lesson a "
                  "singleton, first with no subclasses and then choosing the bombed or "
                  "enchanted subclass from an environment variable inside the access "
                  "operation, and the authors point out that the operation must then be "
                  "edited for every new subclass, which a registry would avoid. Read it "
                  "in the book. The known uses are Smalltalk-80's current change set; the "
                  "metaclasses of Smalltalk, each the class of one class and with exactly "
                  "one instance; and InterViews's Session and WidgetKit, the second an "
                  "abstract factory whose subclass is chosen from an environment "
                  "variable. Related Patterns says only that many patterns can be built "
                  "with Singleton, naming Abstract Factory, Builder and Prototype."),
            ("p", "Singleton is also the pattern in the catalog most argued over since. A "
                  "common later view holds that a singleton reached through a static "
                  "operation is global state under another name: every class that calls "
                  "it depends on it without saying so, and a test cannot easily put a "
                  "different instance in its place, so many designs now create the one "
                  "instance at start-up and pass it to the objects that need it. The "
                  "authors' text meets part of this, in the registry and in the benefit "
                  "that only the access operation must change to allow more instances; "
                  "it does not discuss testing. Read both, and weigh them against the "
                  "design in front of you."),
            ("p", "Now the lab, on a parcel locker network rather than a printer spooler. "
                  "Its registry of locker banks costs 50 to load from disk and its audit "
                  "log costs 20 to open; five requests reach the registry in turn, from a "
                  "kiosk, the app, a courier, the kiosk again and a night job, and none "
                  "reaches the log. The access view counts the requests, the instances "
                  "created, the cost at the start, the cost in all, the subjects never "
                  "requested, the instances alive at the end and the first request's "
                  "cost. On <code>registry-fresh</code>, where every request constructs "
                  "its own registry, there are 5 requests, 5 instances created and still "
                  "alive, a cost of 250, and the log is the 1 subject never requested."),
            ("p", "On <code>registry-lazy</code>, the sketch above, the first request "
                  "creates the registry and the other four reuse it: 1 instance, a cost "
                  "of 50, nothing paid at the start, and the first request pays the 50. "
                  "On <code>registry-eager</code>, the static-object approach the authors "
                  "argue against, both objects are made before any request: 2 instances, "
                  "70 paid at the start and 70 in all, the first request's cost 0, and "
                  "the log made though no one asks for it, the small liability the "
                  "authors name. The comparison tile sets the three schemes side by side: "
                  "eager 70, lazy 50, fresh 250. The count of requests refused belongs to "
                  "the Proxy lesson in the next course and is 0 here, since no access "
                  "rights are stated."),
            ("h3", "Exercise"),
            ("ul", [
                "A thermostat app has two shared objects: `settings`, which costs 12 to "
                "load, and `sensor-bus`, which costs 40 to open.",
                "The requests, in order: `screen, settings; scheduler, settings; screen, "
                "sensor-bus; app, settings; scheduler, sensor-bus; screen, settings`.",
            ]),
            ("p", "By hand, count the instances created and the cost in all when every "
                  "request makes a new object, and when each object is a singleton made "
                  "on first use. Then type the subjects and requests into the lab and "
                  "check both schemes."),
            ("p", "That completes the chapter's five patterns. The next lesson, Discussion "
                  "of Creational Patterns, reads the authors' comparison of them and "
                  "counts one design three ways."),
        ],
        "lab": ("gofkit", {
            "mode": "proxy",
            "view": "access",
            "subjects": LOCKER_SUBJECTS,
            "requests": LOCKER_REQUESTS,
            "preset": "registry-fresh",
            "presets": [
                {"id": "registry-fresh",
                 "label": "A locker registry made afresh for every request",
                 "scheme": "fresh",
                 "expect": {"gpxRequests": "5", "gpxCreations": "5", "gpxStart": "0", "gpxTotal": "250", "gpxNever": "1: audit-log", "gpxAlive": "5", "gpxFirst": "50", "gpxCompare": "eager 70, lazy 50, fresh 250"}},
                {"id": "registry-lazy",
                 "label": "The registry as a singleton made on first use",
                 "scheme": "lazy",
                 "expect": {"gpxCreations": "1", "gpxStart": "0", "gpxTotal": "50", "gpxAlive": "1", "gpxFirst": "50", "gpxRefused": "0: none"}},
                {"id": "registry-eager",
                 "label": "Every shared object made at start-up",
                 "scheme": "eager",
                 "expect": {"gpxCreations": "2", "gpxStart": "70", "gpxTotal": "70", "gpxNever": "1: audit-log", "gpxFirst": "0"}},
            ],
            "panel_title": "Instances and cost, with one shared instance and without",
            "panel_intro": _GOF_INTRO,
        }),
        "steps_title": "Making a class keep its one instance",
        "steps_intro": "Four steps, the last of them on code of your own.",
        "steps": [
            ("Ask whether one is a fact or a convenience",
             "A single instance is a fact when two would be an error, as two spoolers "
             "would; it is a convenience when one simply suffices. Only the first needs "
             "the class to forbid a second."),
            ("Hide the constructor",
             "Make the constructor private and give the class one static operation that "
             "returns the instance."),
            ("Choose when it is made",
             "Create it on first use when it is costly or needs values known only later, "
             "and make the check safe if threads share it."),
            ("Do it on your own code",
             "Find a shared object in a system you know: a configuration, a connection "
             "pool, a cache. Type its cost and a day's requests into the lab, count "
             "instances and cost under fresh and lazy, and note how a test would replace "
             "it."),
        ],
        "worked": {
            "title": "Five requests for one registry",
            "intro": [
                "Count <code>registry-fresh</code>, <code>registry-lazy</code> and "
                "<code>registry-eager</code>.",
            ],
            "lines": [
                "fresh: 5 requests, 5 registries made",
                "fresh cost: 5 × 50 = 250",
                "lazy: 1 registry, made on request 1",
                "lazy cost: 50, nothing at the start",
                "eager: 50 + 20 = 70 before any request",
            ],
            "after": [
                "Eager and lazy both keep one registry. They differ on the log, made under "
                "eager though no one asks for it, and on who pays: the program at "
                "start-up, or the first request.",
            ],
        },
        "quiz_title": "Instances, cost and the authors' claims",
        "quiz": [
            {"q": "In the exercise, how many instances are created and what is the cost in "
                  "all, first when every request makes a new object and then with "
                  "singletons made on first use?",
             "a": ["Fresh: 6 instances, 128. Lazy: 2 instances, 52",
                   "Fresh: 6 instances, 128. Lazy: 1 instance, 12",
                   "Fresh: 4 instances, 48. Lazy: 2 instances, 52",
                   "Fresh: 5 instances, 116. Lazy: 2 instances, 52"],
             "c": 0,
             "why": "settings is asked for four times and sensor-bus twice. Fresh: 6 "
                    "objects, 4 × 12 + 2 × 40 = 48 + 80 = 128. Lazy: each object is made "
                    "once, on its first request, so 2 instances and 12 + 40 = 52. One "
                    "instance forgets the bus; 4 and 48 count only settings; 5 and 116 "
                    "miss one of the four requests for settings."},
            {"q": "Which of these do the authors list among Singleton's consequences?",
             "a": ["It permits a variable number of instances, since only the access "
                   "operation changes",
                   "It makes the class easier to replace in tests",
                   "It makes initialisation safe for threads",
                   "It removes the need for a constructor"],
             "c": 0,
             "why": "The five are controlled access, a reduced name space, refinement by "
                    "subclassing, a variable number of instances, and more flexibility "
                    "than class operations. The chapter says nothing of tests or threads, "
                    "and the constructor is hidden, not removed."},
            {"q": "Why do the authors reject a C++ global or static object as the way to "
                  "make a singleton?",
             "a": ["Nothing prevents a second one, its values may not be known at static "
                   "initialisation, and the order of initialisation across files is "
                   "undefined",
                   "A static object cannot have operations",
                   "A static object is always created lazily",
                   "A static object cannot be an abstract factory"],
             "c": 0,
             "why": "Those are the three reasons the implementation section gives, with "
                    "the small added liability that every such singleton is made whether "
                    "used or not. A static object is made before it is used, which is the "
                    "opposite of lazy."},
            {"q": "In the Sample Code's second version, the access operation picks the "
                  "maze factory's subclass from an environment variable. What drawback do "
                  "the authors point out?",
             "a": ["The operation must be edited whenever a new subclass is defined",
                   "Two factories are always created",
                   "Clients must read the environment variable themselves",
                   "The factory can no longer be subclassed"],
             "c": 0,
             "why": "The conditionals list the subclasses, so each new one edits the "
                    "operation, which the authors say may matter for factories in a "
                    "framework; a registry is their remedy. Exactly one factory is "
                    "created, and clients still just call the access operation."},
        ],
        "mistakes": [
            ("Treating a global variable as a singleton",
             "A global variable makes an object reachable, but nothing stops a second "
             "one being made, and every sole instance it holds adds a name to the global "
             "space. The pattern makes the class keep its own instance; on the lab's "
             "fresh preset five clients each making a registry pay 250 where one shared "
             "registry costs 50."),
            ("Creating every singleton at start-up",
             "The static-object approach makes each singleton whether used or not, "
             "possibly before the values it needs are known, and in C++ in no defined "
             "order. Lazy creation in the access operation avoids all three; the lab's "
             "eager preset pays 20 for a log nobody asks for."),
            ("Choosing the subclass with conditionals in the access operation",
             "It works, but the operation must be edited for every new subclass, which "
             "the authors say may matter for a framework's factories. Their registry of "
             "singletons removes the list, at the cost that every candidate must be "
             "created in order to register."),
        ],
        "standard": (
            "Finish when you can count instances and cost with one shared instance and without.",
            "Given a resource's cost and a run of requests, state the instances created "
            "and the cost under fresh, lazy and eager creation, the five benefits the "
            "authors list, and the costs their implementation section admits."
        ),
        "note": (
            "The lab counts instances and cost for the requests you state, and frees "
            "nothing. It cannot tell whether a second instance would be an error in your "
            "design or merely wasteful, how threads reach the instance, or how a test "
            "would replace it; those decide whether a Singleton or one instance passed "
            "around fits better."
        ),
    },
]
