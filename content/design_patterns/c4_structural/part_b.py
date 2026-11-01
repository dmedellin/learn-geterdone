"""Structural Patterns, lessons 6-8 -- Chapter 4: Flyweight, Proxy, and the
Discussion of Structural Patterns.

Gamma, Helm, Johnson and Vlissides, Design Patterns: Elements of Reusable
Object-Oriented Software (Addison-Wesley, 1995), Chapter 4. Pages in the
comments are PDF pages of the operator's copy; the lessons cite by chapter,
section and pattern. Every quotation is copied from that copy and checked with
quotes.py. The designs, records and Java are written for these lessons: none
of the book's code, diagrams or example data is reproduced, and no lab uses
the book's example domains. The design is docs/design-patterns/PLAN.md,
section C, Course 4.
"""

from .part_a import MODULE, _lines


# ---------------------------------------------------------------- 4.6 Flyweight

# A garden planner draws every plant on the plot; each species' sprite and
# growth table is the intrinsic state, a plant's position the extrinsic.
PLANTS = "tomato, 120; basil, 300; lettuce, 450; marigold, 80"
NAME_TAGS = "tag-anna, 1; tag-ben, 1; tag-cara, 1"

FLYWEIGHT_JAVA = """// The flyweight: what every tomato on the plan has in common.
final class PlantKind {
    private final byte[] sprite;                 // about 2 KB, shared
    PlantKind(byte[] sprite) { this.sprite = sprite; }
    void draw(Canvas c, int x, int y) {          // extrinsic state passed in
        c.blit(sprite, x, y);
    }
}
// The flyweight factory: one PlantKind per species, made on first request.
final class PlantKinds {
    private final Map<String, PlantKind> pool = new HashMap<>();
    private final SpriteStore sprites;
    PlantKinds(SpriteStore sprites) { this.sprites = sprites; }
    PlantKind get(String species) {
        return pool.computeIfAbsent(species,
                s -> new PlantKind(sprites.load(s)));
    }
}"""

DOCKS_EXERCISE = """objects:   dock-full, 40; dock-empty, 25; dock-some, 135
intrinsic: 1024 bytes   extrinsic: 16 bytes (stored)
reference: 4 bytes"""


# ---------------------------------------------------------------- 4.7 Proxy

# A library's digitised archive: scanned items with the cost of loading each.
SCANS = "map1850, 300; letters, 120; ledger, 80; diary, 150; atlas, 400; census, 250"
READS = ("ana, letters; ben, map1850; ana, letters; cara, diary; guest, atlas; "
         "ben, letters; ana, ledger")
RIGHTS = "ana, letters, ledger; ben, map1850, letters; cara, diary"

VIRTUAL_PROXY_JAVA = """interface Scan {                                  // the Subject
    Image page(int n);
}

// A virtual proxy: loads the real scan on first use, then forwards.
final class ScanProxy implements Scan {
    private final String archiveId;
    private Scan real;                            // null until first needed
    ScanProxy(String archiveId) { this.archiveId = archiveId; }

    public Image page(int n) {
        if (real == null) {
            real = ScanStore.load(archiveId);     // the costly step
        }
        return real.page(n);
    }
}"""

PROTECTION_PROXY_JAVA = """// A protection proxy: the same interface, and a check before forwarding.
final class GuardedScan implements Scan {
    private final Scan inner;
    private final Reader reader;
    private final Rights rights;
    GuardedScan(Scan inner, Reader reader, Rights rights) {
        this.inner = inner; this.reader = reader; this.rights = rights;
    }

    public Image page(int n) {
        if (!rights.allows(reader, inner)) {
            throw new SecurityException(reader + " may not read this item");
        }
        return inner.page(n);
    }
}"""

READS_EXERCISE = """requests: ben, census; ana, letters; ben, census;
          cara, atlas; ana, diary
costs:    the archive's six scans, as in the presets"""


# ---------------------------------------------------------------- 4.8 Discussion

# A map tile viewer: views of the map, renderers, and frames round a tile.
VIEWER_TWO = "view, street, satellite, terrain; renderer, screen, print"
VIEWER_THREE = ("view, street, satellite, terrain; renderer, screen, print; "
                "frame, plain, shadow, border")
VIEWER_FRAME_FIRST = ("frame, plain, shadow, border; view, street, satellite, terrain; "
                      "renderer, screen, print")

ONE_SHAPE_JAVA = """final class VendorTiles implements TileSource {       // Adapter
    private final GeoKit kit;                          // a vendor class
    VendorTiles(GeoKit kit) { this.kit = kit; }
    public Tile tile(TileKey k) { return kit.fetch(k.z, k.x, k.y).toTile(); }
}
final class CachedTiles implements TileSource {       // Proxy
    private final TileSource remote;
    private final Map<TileKey, Tile> seen = new HashMap<>();
    CachedTiles(TileSource remote) { this.remote = remote; }
    public Tile tile(TileKey k) {
        return seen.computeIfAbsent(k, remote::tile);   // fetch once
    }
}
final class GridOverlay implements TileSource {       // Decorator
    private final TileSource inner;
    GridOverlay(TileSource inner) { this.inner = inner; }
    public Tile tile(TileKey k) { return inner.tile(k).withGrid(); }
}"""

VIEWER_EXERCISE = """view, street, satellite, terrain, transit;
renderer, screen, print;
frame, plain, shadow, border"""


LESSONS = [
    # ---------------------------------------------------------------- 06
    # Flyweight (PDF pp. 215-226 of the operator's copy): Intent and Motivation
    # pp. 215-217, Applicability p. 217, Participants and Collaborations
    # pp. 218-219, Consequences pp. 219-220, Implementation p. 220, Known Uses
    # pp. 225-226 (the 180,000 characters and 480 objects are Doc's, from
    # InterViews, as the book reports them), Related Patterns p. 226.
    # Quote: PDF p. 215 of the operator's copy, 10 words (the Intent), quotes.py OK.
    # Lesson total: 10 words.
    {
        "slug": "flyweight",
        "title": "Flyweight",
        "module": MODULE,
        "one_line": "Many fine-grained objects made affordable by sharing the state they have in common and passing in the state that varies.",
        "summary": (
            "Flyweight shares one object among every context that needs the same "
            "context-free state, and has clients pass in the rest. Read the pattern and its "
            "demanding list of conditions, then count the bytes a garden planner's 950 "
            "plants take with an object each and with four shared species, with positions "
            "stored and computed, and a case where sharing costs more than it saves."
        ),
        "key": [
            "share what does not depend on context",
            "intrinsic: stored in the flyweight",
            "extrinsic: passed in by the client",
            "clients get flyweights from a factory",
            "saved: N(I + X) − (F·I + N·X + N·R)",
            "computing extrinsic state saves more",
            "no identity: shared means the same object",
        ],
        "key_label": "Flyweight in seven lines",
        "concepts_intro": (
            "Three terms carry the lesson: the distinction the pattern rests on, and the "
            "object that makes sharing safe."
        ),
        "concepts": [
            ("Intrinsic state",
             "What a flyweight stores because it is the same wherever the object appears: a "
             "species' drawing, a character's code. Being independent of context, it can be "
             "shared."),
            ("Extrinsic state",
             "What depends on the context and varies with it, such as a position. The "
             "flyweight does not keep it; the client stores it or computes it and passes it "
             "in each time it asks the flyweight to act."),
            ("FlyweightFactory",
             "The object that creates and manages flyweights, handing out an existing one for "
             "a key or making it the first time. Clients get flyweights only from it, which "
             "is what guarantees they are shared."),
        ],
        "read_title": "The pattern, section by section, then the count",
        "read_intro": (
            "Read Flyweight in your own copy first. The lesson summarises its document "
            "editor example, reads the conditions and consequences, and then counts the "
            "storage of a design of its own."
        ),
        "body": [
            ("p", "&ldquo;Use sharing to support large numbers of fine-grained objects "
                  "efficiently.&rdquo; That is the whole of Flyweight's intent. Its "
                  "Motivation is a document editor that would like an object for every "
                  "character, for the uniformity and flexibility that would bring, and "
                  "cannot afford hundreds of thousands of them. The answer is one shared "
                  "object per character code: the code is intrinsic, stored in the shared "
                  "object; the character's position and style are extrinsic, worked out by "
                  "the layout as it goes and handed to the shared object when it draws. "
                  "Logically there is an object at every occurrence; physically there is one "
                  "per letter. A footnote in Chapter 2's case study notes that its glyphs "
                  "could be shared this way, and leaves that as an exercise."),
            ("p", "Applicability is unusually strict: the authors say to apply the pattern "
                  "only when <em>all</em> of five things hold. There are a great many "
                  "objects; storing them all is costly simply because there are so many; most "
                  "of an object's state can be made extrinsic; once it is, a few shared "
                  "objects can stand in for large groups of them; and the "
                  "application does not depend on object identity, since two occurrences "
                  "that share a flyweight are one object, and an identity test cannot tell "
                  "them apart."),
            ("p", "The participants are the Flyweight interface, through which flyweights "
                  "receive extrinsic state; the ConcreteFlyweight, which stores only "
                  "intrinsic state and must be shareable; the UnsharedConcreteFlyweight, for "
                  "objects such as rows and columns that use the interface without being "
                  "shared; the FlyweightFactory; and the Client, which keeps references to "
                  "flyweights and computes or stores their extrinsic state. Two rules make "
                  "the collaboration work: every piece of state is classed as one or the "
                  "other, and clients never create concrete flyweights themselves."),
            ("code", _lines(FLYWEIGHT_JAVA)),
            ("p", "The Consequences are about storage and its price. Finding, passing or "
                  "computing extrinsic state costs time, especially if it used to be stored "
                  "inside the object; space savings offset it, and they depend on three "
                  "things: how far sharing reduces the number of instances, how much "
                  "intrinsic state each object has, and whether the extrinsic state is "
                  "computed or stored. The most is saved when objects have a great deal of "
                  "both kinds and the extrinsic kind can be computed, since then sharing "
                  "cuts the first and computation replaces the second. Combined with "
                  "Composite, shared leaves can no longer keep a parent reference; the "
                  "parent has to be passed in as extrinsic state too."),
            ("p", "Two implementation issues follow. Removing extrinsic state is what decides "
                  "whether the pattern applies at all: if there are as many different "
                  "extrinsic states as objects, nothing is gained, and ideally the extrinsic "
                  "state is computed from a much smaller separate structure, as the editor "
                  "keeps a map of runs of characters in the same style. And shared objects "
                  "must be managed, typically by a factory keyed by the intrinsic state; "
                  "reclaiming them needs reference counting or garbage collection, unless "
                  "there are few and they are kept for good. Known Uses report the "
                  "InterViews document editor Doc, where, as the book gives the figures, a "
                  "document of 180,000 characters needed only 480 character objects; and "
                  "ET++, whose layout objects for each widget are flyweights, as strategies "
                  "often can be."),
            ("p", "Now the lab, on a garden planner that draws every plant on a plot. Each "
                  "record is an intrinsic state and how many objects have it: 120 tomatoes, "
                  "300 basil, 450 lettuces and 80 marigolds. A species' sprite and growth "
                  "table take 2,048 bytes; a plant's position, 8; a reference to a shared "
                  "flyweight, 4. On the preset <code>plants-stored</code> the lab counts "
                  "950 objects and 4 flyweights. Without sharing every plant carries both "
                  "kinds of state: 950 × (2,048 + 8) = 1,953,200 bytes. With flyweights "
                  "there are four sprites, 950 stored positions and 950 references: "
                  "4 × 2,048 + 950 × 8 + 950 × 4 = 19,592 bytes. The saving is 1,933,608 "
                  "bytes, about 99%. The most objects on one flyweight are the lettuces, "
                  "450; the fewest, the marigolds, 80."),
            ("p", "On the preset <code>plants-computed</code> the planner works out each "
                  "plant's position from its row and the spacing, so no position is stored: "
                  "4 × 2,048 + 950 × 4 = 11,992 bytes, and about 99.4% saved. That is the "
                  "authors' second kind of saving, extrinsic state traded for computation. "
                  "The preset <code>name-tags</code> breaks the conditions: three name tags, "
                  "each with its own text, so three flyweights for three objects. Unshared "
                  "they take 3 × (64 + 8) = 216 bytes; shared, 3 × 64 + 3 × 8 + 3 × 4 = 228, "
                  "and the lab reports a saving of −12. When there are as many intrinsic "
                  "states as objects, the factory and the references are all cost."),
            ("h3", "Exercise"),
            ("code", _lines(DOCKS_EXERCISE)),
            ("p", "A bike-share map draws 200 dock icons in three states. By hand, give the "
                  "bytes without sharing, the bytes with flyweights (the position stored), "
                  "and the saving. Type the figures into the lab to check."),
            ("p", "Flyweight puts many contexts in front of one object. The next lesson, "
                  "Proxy, puts one stand-in in front of one object, to control how it is "
                  "reached."),
        ],
        "lab": ("gofkit", {
            "mode": "share",
            "view": "flyweight",
            "preset": "plants-stored",
            "presets": [
                {"id": "plants-stored",
                 "label": "A garden plan's 950 plants of four species, positions stored",
                 "objects": PLANTS, "intrinsic": "2048", "extrinsic": "8",
                 "stored": "yes", "ref": "4",
                 "expect": {"gshObjects": "950", "gshFlyweights": "4", "gshWithout": "1,953,200", "gshWith": "19,592", "gshSaved": "1,933,608", "gshShare": "241,701/244,150 ≈ 99.0%", "gshLargest": "lettuce, 450 objects", "gshSmallest": "marigold, 80 objects"}},
                {"id": "plants-computed",
                 "label": "The same plants, positions computed from row and spacing",
                 "objects": PLANTS, "intrinsic": "2048", "extrinsic": "8",
                 "stored": "no", "ref": "4",
                 "expect": {"gshObjects": "950", "gshFlyweights": "4", "gshWithout": "1,953,200", "gshWith": "11,992", "gshSaved": "1,941,208", "gshShare": "242,651/244,150 ≈ 99.4%", "gshLargest": "lettuce, 450 objects", "gshSmallest": "marigold, 80 objects"}},
                {"id": "name-tags",
                 "label": "Three name tags, each with its own text",
                 "objects": NAME_TAGS, "intrinsic": "64", "extrinsic": "8",
                 "stored": "yes", "ref": "4",
                 "expect": {"gshObjects": "3", "gshFlyweights": "3", "gshWithout": "216", "gshWith": "228", "gshSaved": "−12", "gshShare": "−1/18 ≈ −5.6%", "gshLargest": "tag-anna, 1 object", "gshSmallest": "tag-anna, 1 object"}},
            ],
            "panel_title": "Storage with an object each, and with shared flyweights",
        }),
        "steps_title": "Deciding whether sharing pays",
        "steps_intro": "Four steps, the last of them on a design of your own.",
        "steps": [
            ("Split the state",
             "For one object, list what it would hold and mark each part intrinsic, the same "
             "in every context, or extrinsic, depending on where the object is."),
            ("Count the distinct intrinsic states",
             "Those are the flyweights. If there are nearly as many as objects, stop: the "
             "pattern's conditions are not met."),
            ("Compute both storage figures",
             "Without sharing, objects × (intrinsic + extrinsic). With it, flyweights × "
             "intrinsic, plus objects × extrinsic if stored, plus a reference per object."),
            ("Do it on a design of your own",
             "Take a collection in your code with many small objects of few kinds (map "
             "markers, cells, particles, tokens) and estimate the bytes each way. Say whether "
             "the extrinsic part could be computed, and whether anything compares the objects "
             "by identity."),
        ],
        "worked": {
            "title": "Bytes for the garden plan",
            "intro": [
                "Compute the two storage figures on <code>plants-stored</code>.",
            ],
            "lines": [
                "plants: 120 + 300 + 450 + 80 = 950",
                "without sharing: 950 × (2048 + 8) = 1953200",
                "sprites: 4 × 2048 = 8192",
                "positions: 950 × 8 = 7600",
                "references: 950 × 4 = 3800",
                "with sharing: 8192 + 7600 + 3800 = 19592",
            ],
            "after": [
                "The sprites, which were most of the cost, are paid for four times instead of "
                "950. What remains per plant, a position and a reference, is what sharing "
                "cannot remove unless the position is computed.",
            ],
        },
        "quiz_title": "Storage, sharing and the conditions",
        "quiz": [
            {"q": "In the exercise, 200 dock icons of three states: what are the bytes "
                  "without sharing, with flyweights, and the saving?",
             "a": ["208,000; 7,072; 200,928", "208,000; 6,272; 201,728",
                   "204,800; 7,072; 197,728", "208,000; 3,872; 204,128"],
             "c": 0,
             "why": "There are 40 + 25 + 135 = 200 objects. Unshared, each holds 1,024 + 16 "
                    "bytes: 200 × 1,040 = 208,000. Shared, 3 × 1,024 = 3,072 for the "
                    "flyweights, 200 × 16 = 3,200 for the stored positions and 200 × 4 = 800 "
                    "for the references: 7,072, a saving of 200,928. Leaving out the "
                    "references gives 6,272; leaving out the positions, as if computed, "
                    "3,872."},
            {"q": "On <code>name-tags</code>, why does the lab report a negative saving?",
             "a": ["Because the extrinsic state is stored",
                   "Because every object has its own intrinsic state, so nothing is shared and "
                   "the references are extra",
                   "Because 64 bytes is too little intrinsic state to share",
                   "Because the factory itself is counted"],
             "c": 1,
             "why": "Three objects, three distinct intrinsic states, three flyweights: the "
                    "shared design stores the same 192 bytes of text plus 12 bytes of "
                    "references, 228 against 216. The positions are stored in both designs, "
                    "and the lab does not count a factory."},
            {"q": "Which is one of the conditions the authors require, all together, before "
                  "applying Flyweight?",
             "a": ["The objects form a part-whole hierarchy",
                   "Extrinsic state is always computed, never stored",
                   "The application does not depend on object identity",
                   "Each flyweight has a parent reference"],
             "c": 2,
             "why": "The five conditions are many objects, high storage cost from their "
                    "number, most state extrinsic, few shared objects once it is removed, and "
                    "no reliance on identity. Computing extrinsic state increases the saving "
                    "but is not required, and shared leaves cannot keep a parent reference at "
                    "all."},
            {"q": "On <code>plants-computed</code>, what does computing the positions save "
                  "beyond <code>plants-stored</code>?",
             "a": ["7,600 bytes, the stored positions", "3,800 bytes, the references",
                   "8,192 bytes, the sprites", "Nothing: the positions still exist"],
             "c": 0,
             "why": "With positions stored the shared design takes 19,592 bytes; computed, "
                    "11,992. The difference is 950 × 8 = 7,600, the positions no longer kept. "
                    "The references and the four sprites are still there."},
        ],
        "mistakes": [
            ("Applying Flyweight wherever there are many objects",
             "The authors require five conditions together, and the decisive one is that "
             "most of the state can be made extrinsic and what remains takes few distinct "
             "values. On the lesson's illustration three name tags with their own text "
             "cost 12 bytes more shared than not."),
            ("Leaving context in the flyweight",
             "A shared object that stores anything about where it is used is no longer "
             "context-free, and every context sees the last one's value. The position, the "
             "parent and the style go outside, passed in when the flyweight is asked to act."),
            ("Comparing flyweights by identity",
             "Two plants of the same species are the same object. Code that tells "
             "occurrences apart by identity will find them equal; the authors list "
             "independence from identity as a condition for that reason."),
        ],
        "standard": (
            "Finish when you can compute what sharing saves for a design.",
            "Given counts per intrinsic state and the bytes of each kind of state, state the "
            "storage without and with flyweights, stored and computed, and name the "
            "conditions under which the authors say the pattern applies."
        ),
        "note": (
            "The lab counts bytes from the sizes you give it. It does not count the time "
            "spent passing or computing extrinsic state, which the authors name as the "
            "pattern's cost, and it cannot tell whether your state really splits cleanly "
            "into a shared part and a contextual one."
        ),
    },
    # ---------------------------------------------------------------- 07
    # Proxy (PDF pp. 227-237 of the operator's copy): Intent and Motivation
    # pp. 227-228, Applicability pp. 228-229, Participants pp. 229-230,
    # Consequences pp. 230-231, Implementation pp. 231-233, Known Uses p. 236,
    # Related Patterns pp. 236-237.
    # Quote: PDF p. 227 of the operator's copy, 13 words (the Intent), quotes.py OK.
    # Lesson total: 13 words.
    {
        "slug": "proxy",
        "title": "Proxy",
        "module": MODULE,
        "one_line": "A stand-in with the same interface as the object it represents, which controls when and by whom that object is reached.",
        "summary": (
            "Proxy puts an object with the subject's own interface in front of it, to "
            "control access: to reach it in another address space, create it only when "
            "needed, check who is asking, or do housekeeping on each use. Read the pattern, "
            "then count what a library archive's readers cost when every scan is loaded at "
            "the start, when each is loaded behind a virtual proxy, and when a protection "
            "proxy turns a request away."
        ),
        "key": [
            "a surrogate with the same interface",
            "remote, virtual, protection, smart",
            "virtual: create on the first request",
            "eager: pay for every subject at start",
            "protection: refuse whoever lacks rights",
            "a level of indirection, used four ways",
        ],
        "key_label": "Proxy in six lines",
        "concepts_intro": (
            "Three terms carry the lesson: the roles, and the two kinds of proxy the lab "
            "counts."
        ),
        "concepts": [
            ("Subject, RealSubject and Proxy",
             "The Subject is the interface the RealSubject and the Proxy share, so a proxy "
             "can be used wherever the real object is expected. The Proxy keeps a reference "
             "that lets it reach the real subject, decides who reaches it and when, and may create "
             "and delete it."),
            ("Virtual proxy",
             "A proxy that creates a costly object only when it is first really needed, and "
             "forwards to it from then on. It may keep a little information about the "
             "subject, such as its size, to answer some requests without creating it."),
            ("Protection proxy",
             "A proxy that checks whether the caller may make a request before forwarding "
             "it, for objects whose callers are allowed different things."),
        ],
        "read_title": "The pattern, section by section, then the count",
        "read_intro": (
            "Read Proxy in your own copy first. The lesson summarises its image example, "
            "reads the four kinds of proxy and the consequences, and then counts the "
            "creations and costs of a design of its own under three schemes."
        ),
        "body": [
            ("p", "&ldquo;Provide a surrogate or placeholder for another object to control "
                  "access to it.&rdquo; That is Proxy's intent; Surrogate is its other name. "
                  "The Motivation is a document editor whose documents may embed large "
                  "images that are slow to load. Opening a document should be quick, and "
                  "most of its images are not on screen at once anyway, so each should be "
                  "created only when it is first shown. What sits in the document in the "
                  "meantime is an image proxy: it acts like the image, creates the real one "
                  "when asked to draw it, and forwards every later request. It keeps the "
                  "file name to find the image and the image's size, so the layout can ask "
                  "how big it is without loading it."),
            ("p", "Applicability is a list of the kinds of proxy, for whenever a plain "
                  "reference to an object is not enough. A <em>remote proxy</em> is a stand-in "
                  "on this side for an object that lives in another address space; NeXTSTEP had one, "
                  "and Coplien calls it an Ambassador. A <em>virtual proxy</em> creates "
                  "costly objects on demand, as the image proxy does. A <em>protection "
                  "proxy</em> controls access when different callers are "
                  "allowed different things. A <em>smart reference</em> does extra work whenever "
                  "an object is reached: counting references so the object can be freed, "
                  "loading a persistent object the first time it is referred to, or checking "
                  "that it is locked before use."),
            ("p", "The participants are the Proxy, the Subject interface it shares with the "
                  "RealSubject, and the RealSubject itself; the proxy forwards requests to "
                  "the real subject when appropriate, depending on its kind. The "
                  "Consequences follow from one fact, that a proxy adds a level of "
                  "indirection: a remote proxy hides where the object lives, a virtual proxy "
                  "can create it on demand, and protection proxies and smart references can "
                  "do housekeeping on each access. The authors add a fourth use the proxy can "
                  "hide from the client, copy-on-write: copying a large object is put off, "
                  "with the subject reference-counted, until someone actually modifies the "
                  "copy, and if nobody does, the copy is never paid for."),
            ("code", _lines(VIRTUAL_PROXY_JAVA)),
            ("p", "The Implementation section is about language features, and is the most "
                  "1995 part of the chapter. In C++ a proxy can overload the member access "
                  "operator so that every dereference passes through it, though that cannot "
                  "tell which operation is being called, which the image proxy needs. In "
                  "Smalltalk a proxy can catch every message it does not understand and "
                  "forward it, at a cost in speed and with identity comparisons that bypass "
                  "it. A proxy that deals with its subject only through the abstract "
                  "interface need not know the concrete class, unless, like a virtual proxy, "
                  "it must create the subject. Java later gained dynamic proxy classes, "
                  "which forward through one handler much as the Smalltalk technique does. "
                  "Known Uses are ET++'s image proxy, the Motivation's source, NeXTSTEP's proxies for "
                  "distributed objects, and earlier Smalltalk work on remote access and "
                  "access control."),
            ("code", _lines(PROTECTION_PROXY_JAVA)),
            ("p", "Now the lab, on a library's digitised archive, not the book's images. Six "
                  "scans have loading costs: map1850 300, letters 120, ledger 80, diary 150, "
                  "atlas 400 and census 250. Seven requests arrive, each a reader and a scan. "
                  "On the preset <code>eager</code> every scan is loaded when the archive "
                  "opens: 6 instances created, a cost of 1,300 at the start and 1,300 in all, "
                  "a first request that costs nothing more, and census, which nobody asked "
                  "for, loaded anyway. On the preset <code>virtual-proxy</code> each scan sits "
                  "behind a proxy that loads it on its first request and reuses it: 5 "
                  "creations, nothing at the start, 1,050 in all, and the first request pays "
                  "letters' 120. The lab's comparison tile adds a third scheme: loading afresh "
                  "on every request costs 1,290, since letters is asked for three times."),
            ("p", "The preset <code>protected</code> keeps the virtual proxies and puts a "
                  "protection proxy in front of each, with rights per reader: ana may read "
                  "letters and the ledger, ben the map and letters, cara the diary, and the "
                  "guest nothing. The lab refuses 1 request, the guest's for the atlas, the "
                  "fifth. The atlas is then never loaded: 4 creations and 650 in all. A "
                  "refused request does not count as asking for its subject, so the lab lists "
                  "two scans never requested, atlas and census. In the lab nothing is ever "
                  "unloaded, so the instances alive at the end equal those created."),
            ("p", "The counts depend on the requests. If every scan were read early, the "
                  "virtual proxy would save nothing over eager loading and would add a check "
                  "on every call; the proxy pays where many subjects are costly and few are "
                  "used, which is the Motivation's situation."),
            ("h3", "Exercise"),
            ("code", _lines(READS_EXERCISE)),
            ("p", "A different morning at the archive, with no rights checked. By hand, give "
                  "the creations and the cost in all under eager loading, behind virtual "
                  "proxies, and loading afresh each time. Type the requests into the lab and "
                  "switch the scheme to check."),
            ("p", "Proxy completes the chapter's seven patterns. The next lesson, the "
                  "Discussion of Structural Patterns, compares the ones whose structures look "
                  "alike."),
        ],
        "lab": ("gofkit", {
            "mode": "proxy",
            "view": "access",
            "preset": "virtual-proxy",
            "subjects": SCANS,
            "requests": READS,
            "presets": [
                {"id": "eager",
                 "label": "Every scan loaded when the archive opens",
                 "scheme": "eager",
                 "expect": {"gpxRequests": "7", "gpxRefused": "0: none", "gpxCreations": "6", "gpxStart": "1,300", "gpxTotal": "1,300", "gpxNever": "1: census", "gpxAlive": "6", "gpxFirst": "0", "gpxCompare": "eager 1,300, lazy 1,050, fresh 1,290"}},
                {"id": "virtual-proxy",
                 "label": "Each scan behind a virtual proxy, loaded on first request",
                 "scheme": "lazy",
                 "expect": {"gpxRequests": "7", "gpxRefused": "0: none", "gpxCreations": "5", "gpxStart": "0", "gpxTotal": "1,050", "gpxNever": "1: census", "gpxAlive": "5", "gpxFirst": "120", "gpxCompare": "eager 1,300, lazy 1,050, fresh 1,290"}},
                {"id": "protected",
                 "label": "Virtual proxies with a protection proxy checking each reader",
                 "scheme": "lazy",
                 "rights": RIGHTS,
                 "expect": {"gpxRequests": "7", "gpxRefused": "1: guest → atlas (5)", "gpxCreations": "4", "gpxStart": "0", "gpxTotal": "650", "gpxNever": "2: atlas, census", "gpxAlive": "4", "gpxFirst": "120", "gpxCompare": "eager 1,300, lazy 650, fresh 890"}},
            ],
            "panel_title": "Requests to costly subjects, with and without proxies",
        }),
        "steps_title": "Counting what a proxy controls",
        "steps_intro": "Four steps, the last of them on a design of your own.",
        "steps": [
            ("Name the kind of proxy",
             "Say what the proxy controls: where the subject lives, when it is created, who "
             "may reach it, or what happens on each access. The kind decides what to count."),
            ("Count the creations",
             "Eager: every subject at the start. Behind a virtual proxy: each subject on its "
             "first request. Afresh: one per request."),
            ("Apply the rights",
             "Under a protection proxy, strike every request whose reader lacks the right to "
             "its subject before counting creations; a refused request creates nothing."),
            ("Do it on a design of your own",
             "Take something costly your code loads at start-up (a configuration, a model, a "
             "connection) and list who uses it, in order. Count the cost eagerly and behind a "
             "virtual proxy, and say what the first user would wait for."),
        ],
        "worked": {
            "title": "Seven requests behind virtual proxies",
            "intro": [
                "Count the creations and the cost on <code>virtual-proxy</code>.",
            ],
            "lines": [
                "letters: created, 120",
                "map1850: created, 300",
                "letters: reused",
                "diary: created, 150",
                "atlas: created, 400",
                "letters: reused; ledger: created, 80",
                "scans loaded, in all: 120 + 300 + 150 + 400 + 80 = 1050",
            ],
            "after": [
                "Five scans are loaded, each once, and census never is. Eager loading pays for "
                "all six, 1,300, before the first reader arrives.",
            ],
        },
        "quiz_title": "Creations, costs and the kinds of proxy",
        "quiz": [
            {"q": "In the exercise, what are the creations and the cost in all under eager "
                  "loading, virtual proxies, and loading afresh?",
             "a": ["eager 6 and 1,300; virtual 4 and 920; afresh 5 and 1,170",
                   "eager 6 and 1,300; virtual 4 and 920; afresh 4 and 920",
                   "eager 4 and 920; virtual 4 and 920; afresh 5 and 1,170",
                   "eager 6 and 1,300; virtual 5 and 1,170; afresh 5 and 1,170"],
             "c": 0,
             "why": "Eager loads all six scans at the start, 1,300. Behind virtual proxies, "
                    "census, letters, atlas and diary are each loaded once: 250 + 120 + 400 + "
                    "150 = 920, and ben's second census is reused. Loading afresh pays for "
                    "every one of the five requests: 250 + 120 + 250 + 400 + 150 = 1,170."},
            {"q": "On <code>protected</code>, why is the atlas never loaded?",
             "a": ["Because the virtual proxy loads only the first three subjects",
                   "Because the only request for it, the guest's, is refused",
                   "Because the atlas costs more than any reader's limit",
                   "Because eager loading skipped it"],
             "c": 1,
             "why": "The guest has no rights, so the protection proxy refuses the fifth "
                    "request, and no one else asks for the atlas. A refused request creates "
                    "nothing and does not count as a request for its subject. The preset is "
                    "lazy, not eager, and the lab has no cost limits."},
            {"q": "Which kind of proxy do the authors describe as counting references so "
                  "that an object can be freed when none remain?",
             "a": ["A remote proxy", "A virtual proxy", "A protection proxy",
                   "A smart reference"],
             "c": 3,
             "why": "A smart reference replaces a bare pointer and does extra work when an "
                    "object is reached: counting references, loading a persistent object on "
                    "first reference, or checking a lock. A remote proxy stands for an object "
                    "elsewhere, a virtual one creates on demand, and a protection one checks "
                    "rights."},
            {"q": "On <code>eager</code>, what does the first request cost?",
             "a": ["120, the letters", "Nothing beyond what was paid at the start",
                   "1,300, every scan", "300, the most costly scan requested"],
             "c": 1,
             "why": "Under eager loading every scan, 1,300 in all, is loaded when the archive "
                    "opens, so the first reader finds letters already there. Behind a virtual "
                    "proxy the first request pays letters' 120."},
        ],
        "mistakes": [
            ("Thinking a proxy always saves work",
             "A virtual proxy saves only the subjects that are never requested, and adds a "
             "check to every call. On the lesson's illustration it saves 250 over eager "
             "loading because one scan of six is never read; read all six and it saves "
             "nothing."),
            ("Treating every proxy as a lazy loader",
             "Virtual proxies are one of four kinds. A remote proxy hides where the subject "
             "is, a protection proxy checks rights, and a smart reference does housekeeping "
             "such as reference counting; the structure is the same and the purpose differs."),
            ("Giving the proxy a different interface",
             "A proxy provides the subject's own interface, so it can stand wherever the "
             "subject can. A class that changes the interface is an adapter; the authors "
             "allow only that a protection proxy may refuse some operations, so its "
             "interface is in effect a subset."),
        ],
        "standard": (
            "Finish when you can count what a sequence of requests costs behind proxies.",
            "Given subjects with costs, requests and optional rights, state the creations, "
            "the cost at the start and in all under each scheme and the requests refused, "
            "and name the four kinds of proxy."
        ),
        "note": (
            "The lab counts creations and costs for the requests you list. It cannot "
            "measure the delay a first request feels behind a virtual proxy, the price of "
            "the indirection on every call, or whether your rights are the right ones; and "
            "it frees nothing, so a smart reference's counting is outside it."
        ),
    },
    # ---------------------------------------------------------------- 08
    # Discussion of Structural Patterns (PDF pp. 239-240 of the operator's copy):
    # the opening, Adapter versus Bridge (p. 239), Composite versus Decorator
    # versus Proxy (pp. 239-240).
    # Quote: PDF p. 239 of the operator's copy, 16 words, quotes.py OK.
    # Lesson total: 16 words.
    {
        "slug": "structural-discussion",
        "title": "Discussion of Structural Patterns",
        "module": MODULE,
        "one_line": "Why patterns built from the same few mechanisms are still different patterns: each answers a different problem at a different point in a design's life.",
        "summary": (
            "The chapter closes by comparing the structural patterns that look most alike: "
            "Adapter against Bridge, and Composite, Decorator and Proxy against each other. "
            "Read the comparison, then count the classes of a map tile viewer's design three "
            "ways and see that the counts are the same whichever pattern you have in mind, "
            "which is the authors' point: the difference is in the intent."
        ),
        "key": [
            "same mechanisms, different intents",
            "Adapter: two existing interfaces meet",
            "Bridge: planned for many implementations",
            "Decorator: responsibilities, stacked",
            "Composite: many treated as one",
            "Proxy: one surrogate, access controlled",
            "the class count cannot tell them apart",
        ],
        "key_label": "The comparison in seven lines",
        "concepts_intro": (
            "Three terms carry the lesson: what the patterns share, and the two ways the "
            "authors tell them apart."
        ),
        "concepts": [
            ("Shared mechanisms",
             "Inheritance, single or multiple, for the class patterns, and object composition "
             "for the object patterns. The structural patterns use the same few, which is why "
             "their participants and collaborations look so alike."),
            ("Intent",
             "What a pattern is for: the problem it addresses. The authors' comparisons all "
             "turn on it, since the structures alone do not separate Adapter from Bridge or "
             "Decorator from Proxy."),
            ("Point in the life cycle",
             "When in a design's life a pattern is applied. An adapter is usually fitted "
             "after two classes turn out to need each other; a bridge is planned before "
             "either hierarchy grows."),
        ],
        "read_title": "The comparison, pair by pair, then the count",
        "read_intro": (
            "Read the Discussion of Structural Patterns at the end of Chapter 4 in your own "
            "copy first. It is two pages; the lesson reads its two comparisons and then "
            "counts one design that each pattern could describe."
        ),
        "body": [
            ("p", "&ldquo;The Adapter pattern makes things work after they're designed; Bridge "
                  "makes them work before they are.&rdquo; That sentence is the centre of the "
                  "Discussion of Structural Patterns, the two pages that close Chapter 4. The "
                  "section begins by admitting what a reader has probably noticed by now: "
                  "the structural patterns have similar participants and collaborations, "
                  "because they are built from the same few mechanisms, inheritance for the "
                  "class patterns and composition for the object ones. The similarities, the "
                  "authors say, hide different intents, and the rest of the section "
                  "compares two groups to show them."),
            ("p", "Adapter versus Bridge first. Both put an extra step between a client "
                  "and another object, and both forward requests to it from an interface that is not "
                  "its own. Adapter is about resolving a mismatch between two interfaces that "
                  "already exist; it is not concerned with how they are implemented or how "
                  "they might change. Bridge joins an abstraction to its possibly many "
                  "implementations, keeps the clients' interface steady while those vary, "
                  "and makes room for new ones. So they come at different times: an adapter "
                  "when you find that two independently designed classes ought to work "
                  "together, a coupling nobody foresaw; a bridge when you know from the start "
                  "that an abstraction will have several implementations. The authors add at "
                  "once that this does not make Adapter the lesser pattern; the two simply "
                  "solve different problems. And a facade is not an adapter for many "
                  "objects, since a facade invents an interface of its own where an adapter "
                  "serves one that already exists."),
            ("p", "Composite, Decorator and Proxy next. Composite and Decorator both rely on "
                  "recursive composition, and their structures look alike, so it is tempting "
                  "to call a decorator a composite with one child. That misses Decorator's "
                  "intent, which is adding responsibilities without subclassing, so as to "
                  "avoid a subclass for every combination; Composite's is representation, "
                  "letting many related objects be treated as one. The intents complement "
                  "each other, and the two are often used together, under one abstract class: "
                  "to Decorator a composite is a ConcreteComponent, and to Composite a "
                  "decorator is a Leaf. Proxy also keeps a reference and forwards, with the "
                  "subject's own interface, but it does not attach or remove properties and "
                  "is not built for recursive composition. Its subject supplies the "
                  "functionality and the proxy grants or refuses access to it, where a "
                  "decorator supplies part of the functionality itself; and a proxy's one "
                  "relationship can be fixed at compile time, while a decorator's stack "
                  "cannot be known in advance. Hybrids are possible, the authors allow, "
                  "though they admit to having no real examples."),
            ("code", _lines(ONE_SHAPE_JAVA)),
            ("p", "The sketch makes the section's point in code. The three classes have one "
                  "shape: each implements <code>TileSource</code>, holds another object, and "
                  "forwards. Nothing in the structure says which is which. "
                  "<code>VendorTiles</code> is an adapter because <code>GeoKit</code> "
                  "existed with an interface of its own; <code>CachedTiles</code> is a proxy "
                  "because it stands in for a remote source and controls when it is "
                  "reached; <code>GridOverlay</code> is a decorator because it adds a "
                  "responsibility and could be stacked with others. Swap the reasons and the "
                  "code could stay the same."),
            ("p", "Now the lab, on a map tile viewer. Three views of the map (street, "
                  "satellite, terrain) are drawn by two renderers (screen and print). On the "
                  "preset <code>bridge-split</code> the lab counts 3 × 2 = 6 pairings, 6 + 1 = "
                  "7 classes with one subclass for each, and (3 + 1) + (2 + 1) = 7 with a "
                  "view hierarchy holding a renderer: a ratio of 1, so at this size the "
                  "second hierarchy saves nothing. A third renderer adds 3 classes under "
                  "subclassing and 1 under the split. Read the split as Bridge if the "
                  "renderers were planned; read the same records as Adapter if the renderers "
                  "were a library you found later and wrapped; the two concrete renderers "
                  "are then adapters, the library's own classes sit outside the count, and "
                  "the viewer's classes are the same seven."),
            ("p", "The preset <code>plus-frames</code> adds a third aspect, a frame round each "
                  "tile: plain, a shadow or a border. Now there are 3 × 2 × 3 = 18 pairings, "
                  "19 classes as subclasses against (3 + 1) + (2 + 1) + (3 + 1) = 11, a ratio "
                  "of about 1.7, and each view holds 2 references, to a renderer and a frame. "
                  "A fourth frame adds 6 subclasses against 1. Held as an object the view "
                  "delegates to, the frame is a strategy, the guts; wrapped round the view "
                  "and stacked, it would be a decorator, the skin, and the Decorator lesson's count "
                  "would apply instead. The preset <code>frame-held</code> lists the frame "
                  "first, so that the client holds a frame and the frame holds a view and a "
                  "renderer: the class counts are identical, 19 and 11; only the references "
                  "change, and a new renderer now adds 9 subclasses, one per frame and view. "
                  "Which object the client holds is a design decision the count records but "
                  "does not make."),
            ("p", "That is the section's lesson in one number: the class counts are the same "
                  "under every reading. The structure follows from the mechanisms; the "
                  "choice between patterns follows from what the design is for, and when."),
            ("h3", "Exercise"),
            ("code", _lines(VIEWER_EXERCISE)),
            ("p", "The viewer gains a fourth view, transit. By hand, give the pairings, the "
                  "classes as subclasses and as three hierarchies, and what one more view "
                  "would add to each. Type the records into the lab, with the view as the "
                  "aspect that gains a variant, to check."),
            ("p", "That ends the structural patterns. The next course, Behavioral Patterns I: "
                  "Requests, Languages and Traversal, begins Chapter 5 with Chain of "
                  "Responsibility."),
        ],
        "lab": ("gofkit", {
            "mode": "classes",
            "view": "explosion",
            "preset": "bridge-split",
            "presets": [
                {"id": "bridge-split",
                 "label": "Three map views on two renderers; a third renderer arrives",
                 "aspects": VIEWER_TWO,
                 "added": "renderer",
                 "expect": {"gclCombos": "3 × 2 = 6", "gclSubclass": "6 + 1 = 7", "gclCompose": "(3 + 1) + (2 + 1) = 7", "gclRatio": "1×", "gclRefs": "1: renderer", "gclAddSubclass": "3 (7 → 10)", "gclAddCompose": "1 (7 → 8)"}},
                {"id": "plus-frames",
                 "label": "The same with three frames round a tile; a fourth frame arrives",
                 "aspects": VIEWER_THREE,
                 "added": "frame",
                 "expect": {"gclCombos": "3 × 2 × 3 = 18", "gclSubclass": "18 + 1 = 19", "gclCompose": "(3 + 1) + (2 + 1) + (3 + 1) = 11", "gclRatio": "19/11 ≈ 1.7×", "gclRefs": "2: renderer, frame", "gclAddSubclass": "3 × 2 = 6 (19 → 25)", "gclAddCompose": "1 (11 → 12)"}},
                {"id": "frame-held",
                 "label": "The same three aspects with the frame held first; a renderer arrives",
                 "aspects": VIEWER_FRAME_FIRST,
                 "added": "renderer",
                 "expect": {"gclCombos": "3 × 3 × 2 = 18", "gclSubclass": "18 + 1 = 19", "gclCompose": "(3 + 1) + (3 + 1) + (2 + 1) = 11", "gclRatio": "19/11 ≈ 1.7×", "gclRefs": "2: view, renderer", "gclAddSubclass": "3 × 3 = 9 (19 → 28)", "gclAddCompose": "1 (11 → 12)"}},
            ],
            "panel_title": "One design's classes, read three ways",
        }),
        "steps_title": "Telling look-alike patterns apart",
        "steps_intro": "Four steps, the last of them on a design of your own.",
        "steps": [
            ("Describe the structure",
             "Write down what holds a reference to what and which interfaces match. That is "
             "what the patterns share, and it will not settle the question."),
            ("Ask when the second class appeared",
             "If the class being forwarded to existed first with its own interface, the "
             "wrapper is fitting it, Adapter's case; if both sides were planned to vary, "
             "Bridge's."),
            ("Ask what the wrapper adds",
             "Responsibilities that stack, Decorator; control over reaching an object that "
             "does the real work, Proxy; many children treated as one, Composite."),
            ("Do it on a design of your own",
             "Find a class in your code that holds another and forwards to it. Say which "
             "pattern's intent it serves, count the classes with and without it, and say "
             "whether the count would change if its intent were another pattern's."),
        ],
        "worked": {
            "title": "Three aspects, two designs",
            "intro": [
                "Count the classes on <code>plus-frames</code>.",
            ],
            "lines": [
                "views × renderers × frames: 3 × 2 × 3 = 18",
                "a subclass per view, renderer and frame: 18 + 1 = 19",
                "view, renderer and frame hierarchies: (3 + 1) + (2 + 1) + (3 + 1) = 11",
                "a fourth frame, subclassing: 3 × 2 = 6",
                "a fourth frame, hierarchies: 1",
            ],
            "after": [
                "Listing the frame first, as <code>frame-held</code> does, changes which object "
                "the client holds and nothing in these lines.",
            ],
        },
        "quiz_title": "Intents, life cycles and the counts",
        "quiz": [
            {"q": "In the exercise, with four views, two renderers and three frames: what "
                  "are the classes as subclasses and as three hierarchies, and what does one "
                  "more view add to each?",
             "a": ["25 and 12; 6 and 1", "24 and 12; 6 and 1",
                   "25 and 12; 4 and 1", "25 and 13; 6 and 2"],
             "c": 0,
             "why": "There are 4 × 2 × 3 = 24 pairings, so 24 + 1 = 25 classes with one "
                    "abstract base. The hierarchies are (4 + 1) + (2 + 1) + (3 + 1) = 12. One "
                    "more view needs a subclass for each renderer and frame pairing, 2 × 3 = 6, "
                    "against one view class."},
            {"q": "According to the Discussion, how do Adapter and Bridge differ?",
             "a": ["Adapter uses inheritance and Bridge uses composition",
                   "Adapter reconciles two existing interfaces, usually after the design; "
                   "Bridge is planned up front for several implementations",
                   "Bridge defines a new interface and Adapter reuses an old one",
                   "Adapter is the weaker pattern and is replaced by Bridge as a design matures"],
             "c": 1,
             "why": "The authors put the difference in intent and in timing: an adapter makes "
                    "independently designed classes work together once the need is found, and "
                    "a bridge is designed in when an abstraction is known to need several "
                    "implementations. Both can be built with composition; a new interface is "
                    "how they distinguish a facade from an adapter; and they say explicitly "
                    "that Adapter is not inferior."},
            {"q": "From Composite's point of view, what is a decorator, when the two are used "
                  "together?",
             "a": ["A Composite with one child", "A Leaf", "A ConcreteComponent",
                   "A Proxy"],
             "c": 1,
             "why": "Used together under one abstract class, a decorator is a Leaf to the "
                    "Composite pattern and a composite is a ConcreteComponent to the Decorator "
                    "pattern. Calling a decorator a composite with one child is the reading "
                    "the authors say misses its point."},
            {"q": "On <code>frame-held</code>, what changes compared with "
                  "<code>plus-frames</code>?",
             "a": ["The classes as subclasses", "The classes as three hierarchies",
                   "The pairings", "Which aspects each object of the first aspect refers to"],
             "c": 3,
             "why": "The same three aspects with the same variants give the same 18 pairings, "
                    "19 classes as subclasses and 11 as hierarchies. Listing the frame first "
                    "makes the frame the object the client holds, so its objects refer to a "
                    "view and a renderer; the added renderer also costs a different number of "
                    "subclasses than the added frame did."},
        ],
        "mistakes": [
            ("Identifying a pattern by its structure",
             "The structural patterns share their mechanisms, so a class that holds another "
             "and forwards may be an adapter, a bridge, a decorator or a proxy. On the "
             "lesson's illustration the class counts are identical however the design is "
             "read; the authors separate the patterns by intent."),
            ("Ranking Adapter below Bridge",
             "Fitting an adapter later is not a failure to plan a bridge. The authors say so "
             "directly: each addresses a different problem, one found after design and one "
             "foreseen before it."),
            ("Calling a decorator a degenerate composite",
             "The structures are alike, and the authors grant the temptation. But a decorator "
             "adds responsibilities and a composite represents a whole made of parts; used "
             "together, each sees the other as a component of its own kind."),
        ],
        "standard": (
            "Finish when you can say which look-alike pattern a design is applying, and why.",
            "Given a class that holds and forwards to another, state its structure, the "
            "classes it saves or costs, and which pattern's intent and point in the life "
            "cycle it matches, in the terms of the Discussion."
        ),
        "note": (
            "The lab counts classes, and the same classes serve several patterns. It cannot "
            "see intent, or when in a design's life a class was added, which is what the "
            "authors use to tell the patterns apart; that judgement stays with you."
        ),
    },
]
