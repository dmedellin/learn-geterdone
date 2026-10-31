"""Objects and Tables, lessons 1-4 -- Chapter 11 and keys.

Fowler et al., Patterns of Enterprise Application Architecture
(Addison-Wesley, 2002): Chapter 3, The Behavioral Problem and Mapping
Relationships; Chapter 11, Unit of Work, Identity Map and Lazy Load; Chapter
12, Identity Field, Foreign Key Mapping, Association Table Mapping and
Dependent Mapping. The lessons cite the book by chapter, section and pattern;
the PDF page of the operator's copy is given only in the comments beside each
lesson. Every quotation is copied from that copy and checked with
ea_quotes.py; every figure attributed to the book carries its PLAN section S.2
id. The code is written for these lessons, and none of the book's listings or
example domains is reproduced. Each snippet is one constant below, verbatim
from docs/enterprise-patterns/presets.py, used by the lesson's code block, so
the line numbers the prose names are the listing's.
"""


def _lines(text):
    """A snippet constant as a code block's list of lines."""
    return text.split("\n")


# ---------------------------------------------------------------- snippets

UNIT_OF_WORK = """\
// Remembers what changed; writes it all at commit. GONE: never written.
class UnitOfWork {
    enum Mark { NEW, DIRTY, REMOVED, GONE }
    private final Map<Entity, Mark> pending = new LinkedHashMap<>();
    void mark(Entity e, Mark asked) {
        Mark now = pending.get(e);
        boolean kept = now == Mark.NEW || now == Mark.REMOVED;
        boolean undone = now == Mark.NEW && asked == Mark.REMOVED;
        pending.put(e, undone ? Mark.GONE : kept ? now : asked);
    }
    void commit(Mapper db) {
        for (Map.Entry<Entity, Mark> p : pending.entrySet()) {
            switch (p.getValue()) {
                case NEW: db.insert(p.getKey()); break;
                case DIRTY: db.update(p.getKey()); break;
                case REMOVED: db.delete(p.getKey()); break;
            }
        }
    }
}"""

IDENTITY_MAP = """\
// One object per row: a second find returns the same object.
class CustomerMapper {
    private final Map<Long, Customer> loaded =
        new HashMap<Long, Customer>();

    Customer find(long id) throws SQLException {
        Customer c = loaded.get(id);
        if (c == null) {
            c = load(id);
            loaded.put(id, c);
        }
        return c;
    }

    private Customer load(long id) throws SQLException {
        // SELECT ... FROM customer WHERE id = ?
        return new Customer(id);
    }
}"""

LAZY_LINES = """\
// Loads an order's lines the first time something asks.
class Order {
    private final long id;
    private final LineMapper mapper;
    private final List<Line> lines = new ArrayList<>();
    private boolean linesLoaded = false;
    Order(long id, LineMapper mapper) {
        this.id = id;
        this.mapper = mapper;
    }

    List<Line> lines() throws SQLException {
        if (!linesLoaded) {
            lines.addAll(mapper.linesOf(id));
            linesLoaded = true;
        }
        return lines;
    }
}"""

SAVE_NEW_ORDER = """\
// Saves a new order and its lines: the parent row goes first.
void saveNew(Order order) throws SQLException {
    long orderId = keys.next("orders");
    insertOrder(orderId, order.customerId());
    for (Line line : order.lines()) {
        long lineId = keys.next("line");
        insertLine(lineId, orderId, line.sku(), line.qty());
    }
}"""

# Lesson 4.4's order schema, shared by both of its presets.
_ORDER_KEYS = "orders, customer; line, orders; line, product; payment, orders"


LESSONS = [
    # ---------------------------------------------------------------- 01
    # Chapter 3, The Behavioral Problem (PDF p. 50 of the operator's copy;
    # p. 51 is blank in that copy). Chapter 11, Unit of Work (PDF pp. 174-182):
    # caller and object registration p. 175, unit of work controller p. 176,
    # update order and referential integrity p. 177, batch updates p. 178,
    # When to Use It p. 178; the example, by David Rice, from p. 178.
    # Quote: PDF p. 50, 18 words, ea_quotes.py OK. Lesson total: 18 words.
    # F14, PDF p. 178 of the operator's copy: one object altered at three
    # points gives three calls rather than one (paraphrased, not quoted).
    {
        "slug": "unit-of-work",
        "title": "Unit of Work",
        "module": "Chapter 11 · Object-Relational Behavioral Patterns",
        "one_line": "Keep a record of what a business transaction created, changed and deleted, and write it all at commit, once per object.",
        "summary": (
            "Chapter 3's behavioral problem is keeping track of which loaded objects must be "
            "written back, and Unit of Work is its answer: register each new, changed and "
            "deleted object as it happens, and let one object decide at commit what to write. "
            "Count the writes a script of changes makes immediately and at commit, and which "
            "ones the commit never needs."
        ),
        "key": [
            "register each change as it happens",
            "write at commit, once per object",
            "created, then deleted: never written",
            "loaded and changed: one UPDATE",
            "created: one INSERT, however changed",
            "loaded only: clean, nothing written",
        ],
        "key_label": "Unit of Work in six lines",
        "concepts_intro": (
            "Three terms carry this lesson. The first is Chapter 3's, the other two are the "
            "pattern's."
        ),
        "concepts": [
            ("The behavioral problem",
             "Chapter 3's name for getting objects to load and save themselves: once you have "
             "loaded a number of objects and changed some of them, you must know which ones to "
             "write back, and in what order. Fowler finds it harder than the structural "
             "question of how tables and objects correspond."),
            ("Unit of Work",
             "An object that keeps a list of everything a business transaction has created, "
             "changed or deleted. At commit it opens a transaction, does any concurrency check, "
             "and writes the changes; the application never calls an update itself."),
            ("Caller and object registration",
             "Two ways the Unit of Work learns of a change. With caller registration the code "
             "that changes an object must remember to register it; with object registration "
             "the object's own setters do it. A third, the unit of work controller, takes a "
             "copy of each object as it is read and compares at commit."),
        ],
        "read_title": "The chapter's problem first, then the pattern",
        "read_intro": (
            "Read The Behavioral Problem in Chapter 3, then Unit of Work in Chapter 11, in "
            "your own copy first. The lesson sets out the problem as an argument, reads the "
            "pattern as a tool, and then counts the writes one script of changes needs."
        ),
        "body": [
            ("p", "&ldquo;Instead of the application programmer invoking explicit save "
                  "methods, the programmer tells the unit of work to commit.&rdquo; That "
                  "sentence is from Chapter 3, The Behavioral Problem, and it is the whole of "
                  "the pattern this lesson reads: Unit of Work, in Chapter 11. Read the "
                  "section and the pattern in your own copy first."),
            ("p", "You have probably written a save that runs as it goes: load the order, "
                  "change its status, write it; add a line, write it; change your mind about "
                  "the line, delete it. Each step is correct, and the database sees every one "
                  "of them. Chapter 3's argument starts there. When people talk about "
                  "object-relational mapping, Fowler says, they talk about structure, how "
                  "tables relate to objects, but the harder part is behavior: once you have "
                  "loaded a number of objects and changed some, you must know which ones to "
                  "write back. With a couple of records that is easy. With many, some of them "
                  "new, it becomes an exercise, because a new row's key may be needed before "
                  "the rows that refer to it can be written."),
            ("p", "His answer is an object that does the remembering. A Unit of Work keeps "
                  "track of the objects read and the objects created, changed or deleted, and "
                  "at commit it works out the database work itself: it starts a transaction, runs any "
                  "concurrency check (the offline locks of a later course), and writes the "
                  "changes out. Chapter 3 calls it the controller of the database mapping, "
                  "behavior that without it lives scattered through the domain layer."),
            ("p", "Unit of Work is a pattern to look up as well as an argument, and Chapter 11 "
                  "gives its choices. With <em>caller registration</em> the code that changes "
                  "an object must remember to register it, and an object nobody registered is "
                  "silently not written; Fowler thinks that causes more confusion than it is "
                  "worth. With <em>object registration</em> a load registers the object as "
                  "clean and its setters register it as dirty, which still leaves the "
                  "object's author a call to remember. The <em>unit of work controller</em> "
                  "handles every read, keeps a copy of each object, and compares at commit, "
                  "which costs time at commit but lets it update only the fields that "
                  "changed. The pattern also gives the commit a place to order the writes "
                  "for the database's keys, which is lesson 4.4's subject, and to send them "
                  "as one batch. The pattern's worked example, with object registration, is "
                  "David Rice's, and is better read in the book."),
            ("p", "Its When to Use It sets out the alternatives. The simplest is to save each "
                  "object whenever you alter it, and the book's illustration of what that "
                  "costs is one object altered at three points in a piece of work: three "
                  "writes where a single write of its last state would do. Keeping the "
                  "changed objects in variables works for a few, and works with a Transaction "
                  "Script, but soon becomes unmanageable; a dirty flag on each object works "
                  "if you can find all the dirty ones, which in a Domain Model's network of "
                  "objects is hard. The great strength of the pattern, Fowler concludes, is "
                  "that it keeps all this in one place."),
            ("p", "Here is a Unit of Work written for this lesson. It holds one map from "
                  "object to mark (line 4), and `mark` on lines 5 to 10 decides what a new "
                  "mark does to the old one: a NEW or REMOVED object keeps its mark (line 7), "
                  "a NEW object then removed becomes GONE (line 8), and anything else takes "
                  "the mark asked for. The commit on lines 11 to 19 walks the map once and "
                  "writes an INSERT, an UPDATE or a DELETE for each mark; GONE matches no "
                  "case and writes nothing. A loaded object never marked is not in the map at "
                  "all."),
            ("code", _lines(UNIT_OF_WORK)),
            ("p", "Now the count. The lab reads a script of `load`, `new`, `change` and "
                  "`delete` records, one object each, and prints five tiles: the writes made "
                  "if every new, change and delete is written at once; the writes at commit, "
                  "by the rules beside the lab; the writes saved, with their share of the "
                  "immediate ones; the statements at commit; and the objects loaded and never "
                  "changed, which the commit leaves alone. The preset "
                  "<code>edit-an-order</code> loads `order7`, changes it, creates `line1` and "
                  "`line2`, changes `order7` again, deletes `line2`, loads `customer3` and "
                  "changes `line1`. Written at once that is 6 writes; at commit it is 2, "
                  "`INSERT line1; UPDATE order7`, saving 4, 2/3 ≈ 66.7%, and `customer3` is "
                  "the 1 object left clean."),
            ("p", "That is Fowler's argument in a number. The line that was added and deleted "
                  "never reaches the database at all; `order7`, changed twice, is written "
                  "once in its final state; `line1` is one INSERT however often it changed "
                  "after it was made. The lab lists the writes grouped by kind, inserts, then "
                  "updates, then deletes, while the snippet's commit writes them in the order "
                  "the objects were first marked, so it would issue the UPDATE first. They are "
                  "the same statements either way. Neither order is chosen for the database's "
                  "keys, and the lab's banner says so."),
            ("p", "The second preset, <code>delete-loaded</code>, deletes an object that "
                  "came from the database: it loads `a1` and `a2`, changes `a1`, deletes `a2` "
                  "and changes `a1` again. That is 3 writes at once and 2 at commit, "
                  "`UPDATE a1; DELETE a2`, saving 1, 1/3 ≈ 33.3%, with nothing left clean. A "
                  "loaded object that is deleted still costs its DELETE; only a row that "
                  "never existed costs nothing."),
            ("h3", "Exercise"),
            ("p", "A business transaction runs this script: `load, invoice4; new, payment1; "
                  "change, invoice4; change, invoice4; load, account2; change, account2; new, "
                  "note1; delete, note1; change, payment1`. By hand, count the writes made at "
                  "once, list the statements a Unit of Work writes at commit, inserts first, "
                  "and give the writes saved as a share. Then type the script into the lab to "
                  "check."),
            ("p", "A Unit of Work writes each row once; putting those writes in an order the "
                  "keys allow is lesson 4.4's. The next lesson, Identity Map, takes the other "
                  "half of the behavioral problem: loading the same row twice."),
        ],
        "lab": ("eakit", {
            "mode": "uow",
            "view": "commit",
            "preset": "edit-an-order",
            "presets": [
                {"id": "edit-an-order",
                 "label": "Edit an order: two lines added, one deleted, the order changed twice",
                 "script": "load, order7; change, order7; new, line1; new, line2; "
                           "change, order7; delete, line2; load, customer3; change, line1",
                 "expect": {"uwImmediate": "6", "uwCommit": "2",
                            "uwSaved": "4 (2/3 ≈ 66.7%)",
                            "uwWrites": "INSERT line1; UPDATE order7",
                            "uwClean": "1: customer3"}},
                {"id": "delete-loaded",
                 "label": "Delete a loaded object, and change another twice",
                 "script": "load, a1; load, a2; change, a1; delete, a2; change, a1",
                 "expect": {"uwImmediate": "3", "uwCommit": "2",
                            "uwSaved": "1 (1/3 ≈ 33.3%)",
                            "uwWrites": "UPDATE a1; DELETE a2",
                            "uwClean": "0: none"}},
            ],
            "panel_title": "Writes at once against writes at commit",
            "panel_intro": (
                "Each record is one step of a business transaction: load, new, change or "
                "delete, and the object it acts on. The lab counts the writes if each step is "
                "written at once and the writes a Unit of Work makes at commit. The scripts "
                "are the lesson's, and illustrative."
            ),
        }),
        "steps_title": "Counting the writes a commit saves",
        "steps_intro": "Four steps, the last of them on a system of your own.",
        "steps": [
            ("Count the immediate writes",
             "Go through the script and count every new, change and delete. A load writes "
             "nothing. That count is what a save-as-you-go design sends to the database."),
            ("Give each object its final mark",
             "For each object, note whether it was loaded or created, and whether it was "
             "changed or deleted after that. Created and deleted is nothing; created is one "
             "INSERT; loaded and deleted is one DELETE; loaded and changed is one UPDATE; "
             "loaded only is clean."),
            ("List the statements at commit",
             "Write the INSERTs, then the UPDATEs, then the DELETEs, each in the order the "
             "script first names the object, and count them. The writes saved are the "
             "immediate count less this one."),
            ("Do it on a request of your own",
             "Take one request in a system you know that changes several rows, list the "
             "statements it issues from a database log, and mark those a Unit of Work would "
             "merge or drop. Write down both counts."),
        ],
        "worked": {
            "title": "Editing an order, object by object",
            "intro": [
                "Take the preset edit-an-order and give each object its final mark.",
            ],
            "lines": [
                "at once: 2 changes of order7, 2 news",
                "  + delete line2 + change line1: 6",
                "line2: new, then deleted: nothing",
                "line1: new, then changed: one INSERT",
                "order7: loaded, changed twice: one UPDATE",
                "customer3: loaded only: clean",
                "at commit: 2 writes, so 4 saved",
            ],
            "after": [
                "The two writes are the row that is new and the row that changed, each in "
                "its final state. Nothing about the database decided that; the script did, "
                "and a Unit of Work only had to remember it.",
            ],
        },
        "quiz_title": "Writes, marks and the chapter's claims",
        "quiz": [
            {"q": "Count the exercise's script with the lesson's rules: `load, invoice4; new, "
                  "payment1; change, invoice4; change, invoice4; load, account2; change, "
                  "account2; new, note1; delete, note1; change, payment1`. What does the Unit "
                  "of Work write at commit?",
             "a": ["4 statements: INSERT payment1; INSERT note1; UPDATE invoice4; UPDATE "
                   "account2, saving 3 of 7",
                   "4 statements: INSERT payment1; UPDATE payment1; UPDATE invoice4; "
                   "UPDATE account2, saving 3 of 7",
                   "3 statements: INSERT payment1; UPDATE invoice4; UPDATE account2, "
                   "saving 4 of 7",
                   "3 statements: INSERT payment1; UPDATE invoice4; UPDATE account2, "
                   "saving 6 of 9"],
             "c": 2,
             "why": "At once there are 7 writes: two news, four changes and a delete; the "
                    "two loads write nothing. At commit `note1` was created and deleted, so "
                    "it writes nothing; `payment1` was created, so one INSERT, however it "
                    "changed afterwards; `invoice4` and `account2` were loaded and changed, "
                    "so one UPDATE each. That is 3 statements, \"INSERT payment1; UPDATE "
                    "invoice4; UPDATE account2\", saving 4, 4/7 ≈ 57.1%. Nine counts the "
                    "loads as writes."},
            {"q": "The book's illustration in Unit of Work's When to Use It: one object is "
                  "altered at three points in a piece of work, and saved each time. How many "
                  "database calls does that make, against a Unit of Work?",
             "a": ["Three, against one: one write of its last state at commit",
                   "One, against one: the database merges the three saves into one",
                   "Three, against three: the Unit of Work only delays the same writes",
                   "Four, against one: the load and three saves, against one at commit"],
             "c": 0,
             "why": "The illustration is three writes where one, of the object as it ends "
                    "up, would do. A Unit of Work marks the object dirty once and writes "
                    "it once at commit; the load is a read, not a save."},
            {"q": "In the lesson's snippet, `mark` is called on one object with NEW and then "
                  "with REMOVED. What does the commit write for it?",
             "a": ["A DELETE: REMOVED is the last mark, so the switch deletes the row",
                   "An INSERT and then a DELETE, one for each mark in the order set",
                   "An INSERT: line 7 keeps a NEW object's mark whatever comes after",
                   "Nothing: the mark becomes GONE, which no case of the switch writes"],
             "c": 3,
             "why": "Line 8 makes `undone` true when the old mark is NEW and the new one "
                    "REMOVED, and line 9 then stores GONE. The switch on lines 13 to 17 has "
                    "cases for NEW, DIRTY and REMOVED only, so GONE writes nothing. Line 7's "
                    "rule that a NEW object keeps its mark applies to every other mark, such "
                    "as DIRTY."},
            {"q": "Which registration scheme does Chapter 11 argue causes more confusion than "
                  "its flexibility is worth?",
             "a": ["Object registration, where the object's setters register it",
                   "Caller registration, where the user of an object registers it",
                   "The unit of work controller, comparing copies taken at read time",
                   "None: Chapter 11 finds each scheme's flexibility worth its cost"],
             "c": 1,
             "why": "With caller registration the user of an object must remember to "
                    "register it, and an object nobody registered is not written on commit; "
                    "Fowler grants the flexibility, but would rather make an explicit copy for "
                    "changes that are not to be written. Object registration moves the call "
                    "into the object's setters, and the controller compares copies taken at "
                    "read time; neither does Fowler argue against."},
        ],
        "mistakes": [
            ("Taking a Unit of Work for a database transaction",
             "On this view the Unit of Work is the transaction, open from the first load to "
             "the commit. It is not. It is a record of changes held in memory, which becomes a "
             "short system transaction at commit; until then the loads have read the "
             "database, but nothing has been written to it. Chapter 11 makes the point "
             "against saving as you go: it would keep a database transaction running from "
             "the first change to the last, which cannot work when one business transaction "
             "stretches over several requests."),
            ("Thinking that saving each change at once is safer",
             "It can feel safer to write each change the moment it is made, so that nothing "
             "is lost. On the lesson's illustration, <code>edit-an-order</code>, saving at "
             "once inserts `line2` and then deletes it, and updates `order7` twice; the Unit "
             "of Work writes neither the insert nor the delete of `line2`, and updates "
             "`order7` once. Nothing is lost by waiting, because the commit writes the final "
             "state of every object it was told about."),
            ("Expecting the commit to order the writes for you",
             "The lab's commit, like the snippet's, writes each object once, but in an order "
             "set by the kind of write or by when the object was first marked, not by the "
             "database's keys. A line written before its order can break a foreign key. "
             "Chapter 11 makes the Unit of Work the obvious home for that ordering, and "
             "lesson 4.4 counts how."),
        ],
        "standard": (
            "Finish when you can list a commit's statements from a script by hand.",
            "Given a script of loads, creations, changes and deletions, count the immediate "
            "writes, list the statements a Unit of Work writes at commit in the lab's order, "
            "and give the writes it saves as a share."
        ),
        "note": (
            "The lab counts the statements a script implies; it does not time them, lock "
            "anything or check another session's changes, all of which the real commit does. "
            "It also cannot tell whether a change was registered: in the lab every step is "
            "seen, which is what object registration and the controller try to guarantee and "
            "caller registration does not."
        ),
    },
    # ---------------------------------------------------------------- 02
    # Chapter 3, The Behavioral Problem (PDF p. 50 of the operator's copy, on
    # loading the same row twice; PLAN section C says p. 51, which is blank in
    # this copy). Chapter 11, Identity Map (PDF pp. 183-186): explicit or
    # generic and Fowler's preference for explicit p. 184; how many maps p. 184;
    # where to put them and the read-only exception pp. 184-185; When to Use It
    # p. 185. The finder that cannot be sure of the map: Chapter 10, Data
    # Mapper, PDF p. 164.
    # Quote: PDF p. 183, 16 words, ea_quotes.py OK. Lesson total: 16 words.
    {
        "slug": "identity-map",
        "title": "Identity Map",
        "module": "Chapter 11 · Object-Relational Behavioral Patterns",
        "one_line": "Keep every object a session has loaded in a map by its key, and look there before every load, so that one row is one object.",
        "summary": (
            "Chapter 3 warns against loading the same row twice, and Chapter 11's Identity Map "
            "is the guard: a map from key to loaded object, consulted before every load, so "
            "that each row is one object in a session. Count the rows a session's finds load, "
            "the duplicate objects the map prevents, and which object each repeat shares."
        ),
        "key": [
            "a map from key to the loaded object",
            "look in the map before every load",
            "first reason: one row, one object",
            "second reason: a cache, saving a query",
            "scoped to a session, not the server",
            "duplicates: finds minus distinct rows",
        ],
        "key_label": "Identity Map in six lines",
        "concepts_intro": (
            "Three ideas carry the lesson: what the map is for, how it is keyed, and how far "
            "it reaches."
        ),
        "concepts": [
            ("Identity Map",
             "A record of every object read from the database in one business transaction, "
             "keyed by the row's key. Before loading, a finder looks in the map; if the object "
             "is there it returns that object, and otherwise it loads and adds it."),
            ("Explicit and generic maps",
             "An explicit map has a method per kind of object, such as a find for customers; a "
             "generic one takes the kind as a parameter. Fowler prefers explicit maps, for the "
             "compile-time checking and because the interface shows what maps there are."),
            ("Session scope",
             "Each session gets its own maps, isolated from every other session's, usually "
             "held by its Unit of Work. Sharing one map between sessions would need "
             "transactional protection, a burden Fowler advises against taking on; for a "
             "plain map, read-only objects are the main exception."),
        ],
        "read_title": "The chapter's warning first, then the map",
        "read_intro": (
            "Read the passage on loading an object twice in Chapter 3, The Behavioral Problem, "
            "and Identity Map in Chapter 11, in your own copy first. The lesson reads the "
            "warning, then the pattern, then counts the finds of one session."
        ),
        "body": [
            ("p", "&ldquo;An old proverb says that a man with two watches never knows what "
                  "time it is.&rdquo; Identity Map, in Chapter 11, opens with it, and the "
                  "proverb is the pattern's first reason in miniature. This lesson reads that "
                  "pattern with the passage in Chapter 3, The Behavioral Problem, that "
                  "introduces it. Read both in your own copy first."),
            ("p", "What goes wrong when a row is loaded twice? Chapter 3's answer is short. "
                  "Load the same row into two objects and change them both, and everything "
                  "gets very confusing: two in-memory objects claim to be one record, and "
                  "whichever is written last decides what the database holds. The cure is to "
                  "keep a record of every row read, check it before each read, and return a "
                  "second reference to the object already loaded. As a benefit the record "
                  "doubles as a cache, but Fowler's warning is explicit: the map is there "
                  "first so that each row has one object, and speed is a side benefit."),
            ("p", "Chapter 11 makes the record a pattern. Its How It Works keys the map on the "
                  "table's primary key, which works well if the key is one column and never "
                  "changes, so a surrogate key, a number with no meaning outside the database, "
                  "suits it. The map can be explicit, "
                  "with a method for each kind of object, or generic, taking the kind as a "
                  "parameter; Fowler prefers explicit, for compile-time checking and because "
                  "the interface shows what maps there are, at the cost of a method for each "
                  "new map. There can be one map per class or one for the session, and for "
                  "an inheritance hierarchy Fowler prefers one map for the whole tree."),
            ("p", "Where the maps live matters most. Each session needs its own, isolated "
                  "from every other session's, so they belong on a session object, and the "
                  "Unit of Work of the last lesson is by far the best place. A map shared "
                  "between sessions would need transactional protection of its own. Fowler "
                  "names two exceptions: an object database used as a transactional cache, "
                  "which he thinks worth a look, and objects that are never or very rarely "
                  "changed, which may be held for the whole process in a read-only map "
                  "beside the session's updatable one."),
            ("p", "There are also things the map does not do. It answers a find by key; a "
                  "query for many rows, such as everyone whose surname matches a pattern, "
                  "still has to go to the database, because nothing guarantees that all the "
                  "matches are already loaded (Data Mapper's example in Chapter 10 checks the "
                  "map a second time for exactly that reason). And it prevents conflicting "
                  "updates within one session only; conflicts between sessions are the "
                  "offline locks' work."),
            ("p", "Here is an explicit map written for this lesson. The map is the field on "
                  "lines 3 and 4. The `find` on lines 6 to 13 looks in it first (line 7), "
                  "and only when the key is missing (line 8) loads the row (line 9) and "
                  "records the new object (line 10) before returning it. A second find for "
                  "the same key returns the same object on line 12, without the query that "
                  "`load` on lines 15 to 18 stands for."),
            ("code", _lines(IDENTITY_MAP)),
            ("p", "Now the count. The lab reads a session's finds in order, each a class and "
                  "an id, and prints four tiles: the finds; the distinct objects, one per "
                  "class and id; the finds of an object already found, which without the map "
                  "would each make a second copy; and every object found more than once, with "
                  "how many times. In <code>one-session</code> the session finds customer 7, "
                  "order 31, customer 7, order 32, customer 7, product 5 and product 5: 7 "
                  "finds, 4 distinct objects and 3 duplicates, with the repeats "
                  "`customer 7 ×3, product 5 ×2`."),
            ("p", "Read those figures with both of Fowler's reasons. Without a map, the "
                  "session holds three objects for customer 7 and two for product 5, and a "
                  "change made through one of them is invisible to the others. With it, it "
                  "holds four objects, and three of the seven finds need no query. The preset "
                  "<code>no-repeats</code> finds customer 7, order 31 and product 5 once each: "
                  "3 finds, 3 distinct, 0 duplicates, `none` shared. There the map does "
                  "nothing for speed, and it still guarantees that a later find would return "
                  "the same object."),
            ("h3", "Exercise"),
            ("p", "A hotel session makes these finds, in order: `room, 12; guest, 3; room, 14; "
                  "guest, 3; room, 12; guest, 9; guest, 3`. By hand, count the finds, the "
                  "distinct rows and the duplicates, and say which objects are shared and how "
                  "often. Then check your count in the lab."),
            ("p", "The map stops a session loading a row twice. The next lesson, Lazy Load, "
                  "asks the opposite question: how to avoid loading rows the session never "
                  "uses."),
        ],
        "lab": ("eakit", {
            "mode": "load",
            "view": "identity",
            "preset": "one-session",
            "presets": [
                {"id": "one-session",
                 "label": "One session: a customer found three times, a product twice",
                 "finds": "customer, 7; order, 31; customer, 7; order, 32; customer, 7; "
                          "product, 5; product, 5",
                 "expect": {"ldFinds": "7", "ldDistinct": "4", "ldDuplicates": "3",
                            "ldShared": "customer 7 ×3, product 5 ×2"}},
                {"id": "no-repeats",
                 "label": "No repeats: three finds of three rows",
                 "finds": "customer, 7; order, 31; product, 5",
                 "expect": {"ldFinds": "3", "ldDistinct": "3", "ldDuplicates": "0",
                            "ldShared": "none"}},
            ],
            "panel_title": "Finds of an object already loaded",
            "panel_intro": (
                "Each record is one find in a session, a class and an id, in the order they "
                "happen. The lab counts the finds, the distinct objects and the duplicates an "
                "Identity Map prevents. The sessions are the lesson's, and illustrative."
            ),
        }),
        "steps_title": "Counting a session's duplicate loads",
        "steps_intro": "Four steps, the last of them on a system of your own.",
        "steps": [
            ("Count the finds",
             "Write down every find in the order it happens, as a class and a key. Their "
             "number is what a session without a map would load."),
            ("Count the distinct rows",
             "Count each class and key pair once, however often it is found. That is the "
             "number of objects the session holds with an Identity Map."),
            ("Name the repeats",
             "Subtract to get the duplicates, and list each pair found more than once with "
             "how many times, in the order it was first found. Each repeat is an object that "
             "would otherwise exist twice."),
            ("Do it on a request of your own",
             "Take one request in a system you know, read its queries from a log, and count "
             "how often it loads the same row by key. Write the finds, the distinct rows and "
             "the duplicates."),
        ],
        "worked": {
            "title": "One session's seven finds",
            "intro": [
                "Take the preset one-session and count its finds pair by pair.",
            ],
            "lines": [
                "finds: 7",
                "pairs: customer 7, order 31, order 32,",
                "  product 5: 4 distinct",
                "duplicates: 7 − 4, which is 3",
                "customer 7 found 3 times, product 5 twice",
            ],
            "after": [
                "Without the map the session would hold three objects for customer 7, and a "
                "change through one would not show in the other two. That, not the three "
                "saved queries, is the reason Fowler gives first.",
            ],
        },
        "quiz_title": "Finds, duplicates and the map's scope",
        "quiz": [
            {"q": "Count the exercise's finds: `room, 12; guest, 3; room, 14; guest, 3; room, "
                  "12; guest, 9; guest, 3`. How many distinct rows and duplicates are there, "
                  "and which objects are shared?",
             "a": ["5 distinct, 2 duplicates: room 12 ×2, guest 3 ×2",
                   "4 distinct, 3 duplicates: room 12 ×2, guest 3 ×3",
                   "4 distinct, 3 duplicates: guest 3 ×3, room 14 ×2",
                   "3 distinct, 4 duplicates: room 12 ×2, guest 3 ×3"],
             "c": 1,
             "why": "There are 7 finds of 4 distinct pairs, room 12, guest 3, room 14 and "
                    "guest 9, so 7 − 4 = 3 duplicates. Room 12 is found twice and guest 3 "
                    "three times; room 14 and guest 9 once each. Two duplicates of guest 3 "
                    "plus one of room 12 make the 3."},
            {"q": "Which reason does Chapter 3 put first for an Identity Map?",
             "a": ["Performance: a cache that saves a database read on each repeat find",
                   "Sharing: one set of loaded objects used by every session at once",
                   "Ordering: the writes at commit follow the order objects entered it",
                   "Correctness: one in-memory object for each row the session reads"],
             "c": 3,
             "why": "Chapter 3 says the map doubles as a cache, and then insists that keeping "
                    "one object per row comes first and speed second. "
                    "Sharing between sessions is what it avoids, and ordering writes belongs "
                    "to the Unit of Work."},
            {"q": "Where may a whole process share one Identity Map, by Chapter 11's How It "
                  "Works?",
             "a": ["For objects that can never be changed, held in a read-only map",
                   "For every object, once the server has enough memory to hold them",
                   "For objects whose keys are unique across the whole database",
                   "Nowhere: every map is per session, read-only data included"],
             "c": 0,
             "why": "Each session gets its own map, so that one user's uncommitted objects are "
                    "not another's. For a plain map the exception is read-only data, which may be loaded once "
                    "and held in a process-wide map beside the session's updatable one. "
                    "Database-unique keys allow one map for a session, not one for the "
                    "process."},
            {"q": "In the lesson's `CustomerMapper`, a session calls `find(7)` twice. How many "
                  "times does line 9, `c = load(id);`, run?",
             "a": ["Twice: line 9 runs on each call, and line 10 only records it",
                   "Never: the map is filled before the first call is made",
                   "Once: the second call finds the object at line 7 and skips it",
                   "Once for every session in the server, whatever its calls"],
             "c": 2,
             "why": "The first call finds nothing at line 7, so line 8's test is true and line "
                    "9 loads the row; line 10 puts it in the map. The second call finds the "
                    "object at line 7 and skips lines 9 and 10. The map is a field of one "
                    "mapper, so another session would need its own mapper and would load again."},
        ],
        "mistakes": [
            ("Thinking an Identity Map is a performance cache",
             "On this view the map exists to save queries, and a system with a fast database "
             "can do without it. Fowler's first reason is correctness: without the map, two "
             "objects for one row can be changed separately and one change lost, or written "
             "over the other. Saving the query is the second reason, and Chapter 3 says so in "
             "as many words. On the lesson's illustration, <code>no-repeats</code> saves no "
             "query at all and the map is still doing its job."),
            ("Putting one map on the whole server",
             "A map per server looks like a bigger cache. But it is per session, or per "
             "business transaction, so that two users never share each other's uncommitted "
             "objects; one shared map would need transactional protection of its own. The "
             "exception is objects nobody can change, whose map may be held by the whole "
             "process."),
            ("Expecting the map to answer every query",
             "The map answers a find by key. A query for a set of rows, everyone whose name "
             "matches a pattern, must still go to the database, because nothing says every "
             "match is already loaded; the finder then checks the map for each row it brings "
             "back, so as not to make a second object."),
        ],
        "standard": (
            "Finish when you can count a session's finds and duplicates by hand.",
            "Given a session's finds in order, count the distinct rows and the duplicates, "
            "and say which object is shared by which finds and how many times."
        ),
        "note": (
            "The lab counts finds by key in one session. It cannot show the failure the map "
            "exists to prevent, two copies changed differently, because it runs nothing; nor "
            "does it count the queries for many rows that the map cannot answer, or what "
            "happens between sessions, which the offline locks of Course 6 take up."
        ),
    },
    # ---------------------------------------------------------------- 03
    # Chapter 11, Lazy Load (PDF pp. 187-199 of the operator's copy): the four
    # ways and lazy initialization after Beck pp. 187-188; virtual proxy (after
    # the Gang of Four), value holder and ghost p. 188; ripple loading p. 188;
    # two degrees of laziness p. 189; When to Use It p. 189; examples from p.
    # 189, pointed to. Chapter 3, Reading in Data, PDF p. 52.
    # Quote: PDF p. 187, 24 words, ea_quotes.py OK. Lesson total: 24 words.
    # F11, PDF p. 52 of the operator's copy: one query bringing back
    # unnecessary rows over 50 individual ones; three or four joins a query.
    # The batched strategy is the lab's, not the book's.
    {
        "slug": "lazy-load",
        "title": "Lazy Load",
        "module": "Chapter 11 · Object-Relational Behavioral Patterns",
        "one_line": "Leave a marker where related data would go, and load it only when something asks, which saves what is never used and costs a query for each thing that is.",
        "summary": (
            "A Lazy Load stands in for data not yet read and fetches it on first use. "
            "Chapter 11 gives four ways to build one and warns of ripple loading, a query for "
            "each lazy object in a collection; Chapter 3's Reading in Data gives the rules of "
            "thumb on queries and joins. Count the statements and rows four loading "
            "strategies issue for the same orders and lines."
        ),
        "key": [
            "a marker that loads data when asked",
            "lazy: 1 + one query per parent used",
            "two queries: parents, then every child",
            "a join: one statement, one row a child",
            "saves only what is never used",
            "ripple loading: a query per object",
        ],
        "key_label": "Lazy Load in six lines",
        "concepts_intro": (
            "Three ideas carry the lesson: the pattern, its danger, and the rule of thumb it is "
            "weighed against."
        ),
        "concepts": [
            ("Lazy Load",
             "A stand-in for data not yet read, which fetches it the first time it is used. "
             "It leaves a marker in the object structure, and the data is loaded only when "
             "something follows the marker. Chapter 11 builds it four ways: lazy "
             "initialization, a virtual proxy, a value holder and a ghost."),
            ("Ripple loading",
             "Fowler's name for the danger of a collection of lazy objects looked at one at a "
             "time: each one goes to the database separately, where one query could have "
             "read them all. He has seen it cripple an application's performance."),
            ("A statement and a row",
             "The two things this lesson counts. A statement is one query sent to the "
             "database, and costs a round trip whatever it returns; a row is one record it "
             "returns. A lazy strategy trades rows not read for statements sent."),
        ],
        "read_title": "The pattern first, then the rule of thumb",
        "read_intro": (
            "Read Lazy Load in Chapter 11, and Reading in Data in Chapter 3, in your own copy "
            "first. The lesson reads the pattern as a tool, sets it beside the chapter's "
            "advice on queries, and then counts four ways of loading one set of orders."
        ),
        "body": [
            ("p", "&ldquo;As many people know, if you're lazy about doing things you'll win "
                  "when it turns out you don't need to do them at all.&rdquo; That is Lazy "
                  "Load's own summary of itself, in Chapter 11, and the lesson reads it with "
                  "Chapter 3's Reading in Data. Read both in your own copy first."),
            ("p", "You have probably seen a list page that is fast with ten rows and slow "
                  "with fifty, and found in the log one query for the list and then one more "
                  "for each row. Chapter 11 starts from the opposite habit. It is handy, it "
                  "says, to load an object's related objects with it, so that the developer "
                  "using it need not load them by hand; taken to its conclusion, loading one "
                  "object pulls a huge graph out of the database when only a few of its "
                  "objects are needed. A Lazy Load interrupts that, leaving a marker so that "
                  "the data is loaded only when it is used."),
            ("p", "The pattern gives four ways to leave the marker. <em>Lazy "
                  "initialization</em>, which the book takes from Kent Beck, checks a field "
                  "on every access and loads it the first time; it is the simplest, and ties "
                  "the object to the database, so it suits Active Record and the gateways. A "
                  "<em>virtual proxy</em>, from the Gang of Four's book, is an object that "
                  "looks like the real one and loads it when called, at the risk of several "
                  "proxies with different identities for one object. A <em>value holder</em> "
                  "wraps the object and hands it over on request; a <em>ghost</em> is the "
                  "real object holding only its key, which loads the rest on first touch. "
                  "Fowler adds that in practice two degrees of laziness are enough: a "
                  "complete load, and enough to identify each item in a list."),
            ("p", "Then the warning. Fill a collection with lazy objects and look at them one "
                  "by one, and each of them makes its own trip to the database where one trip "
                  "could have fetched them all: ripple loading. Fowler's cure is to make the "
                  "collection itself the lazy thing, and load all its contents when it is "
                  "first touched. A related remedy, from the pattern's discussion of use "
                  "cases, is to give different use cases different loaders, one that loads "
                  "the lines with the order and one that waits. When to Use It puts the decision plainly: "
                  "Lazy Load is worth considering when the data needs an extra call and is "
                  "not used whenever the main object is, and Fowler's own preference is not "
                  "to add it until he thinks he needs it."),
            ("p", "Chapter 3's Reading in Data sets the other side of the scale. Its rule of "
                  "thumb, the book's illustration, is that one query bringing back more rows "
                  "than you need is usually better than fifty separate ones, and that joins "
                  "can pull several tables back in one query, though databases are optimized "
                  "for up to three or four joins in a query. Fowler then tells you to profile "
                  "on your own database, because every rule of thumb has its surprising "
                  "exceptions."),
            ("p", "Here is lazy initialization written for this lesson. The `Order` keeps its "
                  "lines in a list (line 5) and a flag saying whether they have been loaded "
                  "(line 6). The first call of `lines()` finds the flag false on line 13, "
                  "asks the mapper for the lines on line 14, and sets the flag on line 15; "
                  "every later call skips straight to line 17. The flag is the marker because "
                  "the list is created empty and stays a real list (line 5), so there is no "
                  "null to test. It is also the shape Chapter 11 points to wherever null is a "
                  "legal loaded value, when a null test would go back to the database on every "
                  "call."),
            ("code", _lines(LAZY_LINES)),
            ("p", "Now the count. The lab reads parents as records of a name, how many "
                  "children each has and whether its children are used, with a batch size, "
                  "and prints one tile per strategy as statements and rows. <em>Lazy</em> is "
                  "one query for the parents and one for each used parent's children. "
                  "<em>Lazy in batches</em>, the lab's variant rather than one of the "
                  "book's, fetches the used parents' children a batch of parents at a time. "
                  "<em>Two queries</em> reads the parents and then every child. <em>One "
                  "join</em> is a left outer join: one statement, a row for each child, and "
                  "one row for a parent with none."),
            ("p", "In <code>orders-and-lines</code> five orders have 3, 0, 5, 2 and 4 lines, "
                  "and only the first, third and fifth are used, with a batch of 2. Lazy "
                  "loading issues `4 statements, 17 rows`; in batches, `3 statements, 17 "
                  "rows`; two queries, `2 statements, 19 rows`; the join, `1 statement, 15 "
                  "rows`. In <code>every-order-used</code> the same orders are all used: lazy "
                  "is now `6 statements, 19 rows`, batches `4 statements, 19 rows`, and two "
                  "queries and the join are unchanged, 2 and 19, 1 and 15. When everything is "
                  "used, laziness reads no fewer rows and sends three times the statements."),
            ("p", "Two things the tiles do not show. The join's 15 rows are fewer than two "
                  "queries' 19 because the orders are not read separately, but each of its "
                  "rows repeats the order's columns beside the line's, and the lab counts rows, "
                  "not their width. And a statement's cost depends on your network and "
                  "database, which no count here measures; Fowler's advice is to profile it."),
            ("h3", "Exercise"),
            ("p", "Six parents have `a, 10, yes; b, 0, no; c, 2, no; d, 6, yes; e, 1, no; f, "
                  "3, yes` (name, children, used), and the batch is 3. By hand, give the "
                  "statements and rows of each of the four strategies, then check them in the "
                  "lab."),
            ("p", "Loading an order's lines means finding the rows that hold the order's key. "
                  "The next lesson, Identity Field and Foreign Keys, reads how those keys are "
                  "chosen and in what order the rows that hold them can be written."),
        ],
        "lab": ("eakit", {
            "mode": "load",
            "view": "graph",
            "preset": "orders-and-lines",
            "presets": [
                {"id": "orders-and-lines",
                 "label": "Five orders, three of them used, batch of 2",
                 "parents": "o1, 3, yes; o2, 0, no; o3, 5, yes; o4, 2, no; o5, 4, yes",
                 "batch": "2",
                 "expect": {"ldLazy": "4 statements, 17 rows",
                            "ldBatched": "3 statements, 17 rows",
                            "ldTwoQueries": "2 statements, 19 rows",
                            "ldJoin": "1 statement, 15 rows"}},
                {"id": "every-order-used",
                 "label": "The same five orders, every one used",
                 "parents": "o1, 3, yes; o2, 0, yes; o3, 5, yes; o4, 2, yes; o5, 4, yes",
                 "batch": "2",
                 "expect": {"ldLazy": "6 statements, 19 rows",
                            "ldBatched": "4 statements, 19 rows",
                            "ldTwoQueries": "2 statements, 19 rows",
                            "ldJoin": "1 statement, 15 rows"}},
            ],
            "panel_title": "Statements and rows to load orders and their lines",
            "panel_intro": (
                "Each record is a parent, how many children it has, and whether its children "
                "are used. The lab counts the statements and rows four loading strategies "
                "issue; the batched strategy is the lab's, not the book's. It counts rows, not "
                "their width. The orders are the lesson's, and illustrative."
            ),
        }),
        "steps_title": "Counting four ways of loading",
        "steps_intro": "Four steps, the last of them on a system of your own.",
        "steps": [
            ("Total the parents and children",
             "Count the parents, those whose children are used, the children of the used "
             "parents, and all the children."),
            ("Count the lazy strategies",
             "Lazy is 1 + the used parents statements, returning the parents plus the used "
             "children. In batches it is 1 + the used parents divided by the batch, rounded "
             "up, with the same rows."),
            ("Count the eager strategies",
             "Two queries is always 2 statements, returning the parents plus every child. The "
             "join is 1 statement, one row a child, with one row for each parent that has no "
             "children."),
            ("Do it on a list page of your own",
             "Take one list page in a system you know, count its queries from a log with the "
             "list at 10 rows and at 50, and write in one sentence whether it ripple-loads."),
        ],
        "worked": {
            "title": "Five orders, three used",
            "intro": [
                "Take the preset orders-and-lines and count the lazy strategy, then the others.",
            ],
            "lines": [
                "first query: 5 orders, 5 rows",
                "used: o1, o3, o5, so 3 more statements",
                "their lines: 3 + 5 + 4, so 12 rows",
                "lazy: 4 statements, 17 rows",
                "batch of 2: two batches, 3 statements",
                "two queries: 2 statements, 5 + 14 rows",
                "join: 3 + 1 + 5 + 2 + 4, so 15 rows",
            ],
            "after": [
                "Laziness saved the 2 lines of the unused o4, and cost two more statements "
                "than two queries. Which matters more depends on what a statement costs on "
                "your connection, which the lesson does not know.",
            ],
        },
        "quiz_title": "Statements, rows and ripple loading",
        "quiz": [
            {"q": "Count the exercise: `a, 10, yes; b, 0, no; c, 2, no; d, 6, yes; e, 1, no; "
                  "f, 3, yes`, batch 3. What do lazy loading, lazy in batches, two queries and "
                  "the join issue?",
             "a": ["Lazy 4 statements, 19 rows; batches 2, 19; two queries 2, 22; join 1, "
                   "23",
                   "Lazy 7 statements, 28 rows; batches 3, 28; two queries 2, 28; join 1, "
                   "22",
                   "Lazy 4 statements, 25 rows; batches 3, 25; two queries 2, 28; join 1, "
                   "22",
                   "Lazy 4 statements, 25 rows; batches 2, 25; two queries 2, 28; join 1, "
                   "23"],
             "c": 3,
             "why": "Six parents, three used (a, d, f) with 10 + 6 + 3 = 19 children, and 22 "
                    "children in all. Lazy: 1 + 3 = 4 statements, 6 + 19 = 25 rows. Batches: "
                    "the 3 used parents fit one batch of 3, so 1 + 1 = 2 statements, 25 rows. "
                    "Two queries: 2 statements, 6 + 22 = 28 rows. The join: 10 + 1 + 2 + 6 + 1 "
                    "+ 3 = 23 rows, because b has no children and is still one row. The other "
                    "answers count every parent as used, forget the parents' rows, forget "
                    "b's join row, or round the batches wrongly."},
            {"q": "Four orders, every one used, with 2, 2, 2 and 2 lines. How many statements "
                  "does the lazy strategy issue, against two queries?",
             "a": ["4 against 2",
                   "5 against 5",
                   "5 against 2",
                   "8 against 2"],
             "c": 2,
             "why": "Lazy is one query for the orders and one for each used order's lines: 1 "
                    "+ 4 = 5. Two queries is always 2. Both return 4 + 8 = 12 rows, so here "
                    "laziness loads nothing less and sends more statements."},
            {"q": "What does Chapter 11 call the danger of a collection of lazy objects "
                  "examined one at a time?",
             "a": ["A ghost",
                   "Ripple loading",
                   "A virtual proxy",
                   "Lazy initialization"],
             "c": 1,
             "why": "Ripple loading is a separate trip to the database for each object where "
                    "one trip could have read them all. A ghost and a virtual proxy are two of the four "
                    "ways to build a Lazy Load, and lazy initialization is the simplest of "
                    "them."},
            {"q": "By Lazy Load's When to Use It, when is the pattern usually pointless?",
             "a": ["On a field kept in the object's own row, beside its other columns",
                   "On a collection whose items need an extra query to read",
                   "On data used only some of the times the object itself is used",
                   "On any object loaded through a Data Mapper rather than a record"],
             "c": 0,
             "why": "Fowler says it is usually pointless on a field in the same row, because "
                    "bringing back extra data in a call usually costs no more; it is worth "
                    "considering when the field needs an extra call and is not used whenever "
                    "the main object is. A Data Mapper needs a virtual proxy or similar rather "
                    "than lazy initialization, not no laziness."},
        ],
        "mistakes": [
            ("Believing lazy loading always loads less",
             "On this view a lazy design can only win, because it never reads more than is "
             "asked for. On the lesson's illustration, <code>every-order-used</code>, every "
             "order's lines are used: lazy loading and two queries return the same 19 rows, "
             "and the lazy strategy takes 1 + 5 = 6 statements where two queries take 2. "
             "Laziness saves only what is not used, and Fowler's When to Use It is about "
             "exactly that judgement."),
            ("Making each item of a collection lazy",
             "A collection of lazy objects, each loading itself, is the shape that ripple "
             "loads: one query per item as the list is walked. Fowler's cure is to make the "
             "collection the lazy thing and load all of it at once when first touched; a "
             "related remedy is to give the use case that walks the list a loader that reads "
             "it eagerly."),
            ("Reading the join's rows as its whole cost",
             "The join returns the fewest rows in both presets, 15 against 19, and one "
             "statement. But each of those rows carries the parent's columns as well as the "
             "child's, the lab counts rows and not their width, and Chapter 3 notes that "
             "databases are optimized for up to three or four joins in a query."),
        ],
        "standard": (
            "Finish when you can count four loading strategies by hand.",
            "Given parents, their child counts and which parents' children are used, compute "
            "the statements and rows lazily, lazily in batches, with two queries and with one "
            "join."
        ),
        "note": (
            "The lab counts statements and rows; it does not time them, so it cannot say "
            "whether four short queries cost more than one longer one on your network. It "
            "also counts every row alike, though a join's rows are wider, and its batched "
            "strategy is the lab's variant rather than one the chapter describes."
        ),
    },
    # ---------------------------------------------------------------- 04
    # Chapter 3, Structural Mapping Patterns, Mapping Relationships (PDF pp.
    # 53-55 of the operator's copy): keys and the reversal of collections p.
    # 53; association tables p. 54; deferring referential integrity and the
    # topological sort p. 55. Chapter 11, Unit of Work, PDF p. 177 (update
    # order). Chapter 12: Identity Field (pp. 201-217; meaningful keys p. 201,
    # key types and table- or database-unique p. 202, auto-generation, GUIDs
    # and key tables pp. 203-204; the examples, from p. 204, include one by
    # Matt Foemmel and Fowler at p. 205); Foreign Key Mapping (pp. 218-228;
    # When to Use It p. 221); Association Table Mapping (pp. 229-240); Dependent
    # Mapping (pp. 241-245).
    # Quote: PDF p. 53, 11 words, ea_quotes.py OK; "a rare stand on the side of
    # meaninglessness", PDF p. 201, 8 words, OK; it is quoted twice, in the
    # body and mistakes[0]. Lesson total: 11 + 8 + 8 = 27 words.
    {
        "slug": "identity-field-and-foreign-keys",
        "title": "Identity Field and Foreign Keys",
        "module": "Chapter 12 · Object-Relational Structural Patterns",
        "one_line": "Objects link by reference and tables by key, so each object keeps its row's key, and rows must be written parents first unless the database waits to check.",
        "summary": (
            "Chapter 3's Mapping Relationships sets out the mismatch: objects link by reference, "
            "tables by key, and a collection's direction is reversed in the tables. Chapter 12 "
            "answers with Identity Field and Foreign Key Mapping, with Association Table Mapping "
            "and Dependent Mapping for the harder cases. Order inserts and deletes so that no "
            "row refers to a row that is not there, and find the broken pairs in an order given."
        ),
        "key": [
            "objects link by reference, rows by key",
            "the child row holds the key of its parent",
            "defer the checks to commit if you can",
            "otherwise: parents first on insert",
            "and children first on delete",
            "prefer keys that mean nothing",
        ],
        "key_label": "Keys and their order in six lines",
        "concepts_intro": (
            "Three patterns from Chapter 12 carry the lesson, and two more are named for the "
            "cases they cover."
        ),
        "concepts": [
            ("Identity Field",
             "A field in an object that holds its row's primary key, so that the object can be "
             "written back to the right row. Fowler calls it mind-numbingly simple, and then "
             "spends pages on the choices: what kind of key, unique to what, and how to get a "
             "new one."),
            ("Foreign Key Mapping",
             "An object reference saved as a foreign key between tables. A single reference "
             "becomes a key in the referring row; a collection is reversed, so each child's "
             "row holds the key of its parent."),
            ("Referential integrity",
             "The database's guarantee that every foreign key names a row that exists. A "
             "database that checks it on every statement makes the order of writes matter; one "
             "that defers the check to commit does not."),
        ],
        "read_title": "The mismatch first, then the keys",
        "read_intro": (
            "Read Mapping Relationships in Chapter 3's Structural Mapping Patterns, then "
            "Identity Field and Foreign Key Mapping in Chapter 12, in your own copy first, "
            "and look through Association Table Mapping and Dependent Mapping. The lesson "
            "reads the mismatch as an argument and the patterns as tools, then counts write "
            "orders on a small schema."
        ),
        "body": [
            ("p", "&ldquo;Relational databases handle links by forming a key into another "
                  "table.&rdquo; Chapter 3's Mapping Relationships says it of the first of two "
                  "problems, and this lesson reads it with the four Chapter 12 patterns that "
                  "answer them: Identity Field, Foreign Key Mapping, Association Table Mapping "
                  "and Dependent Mapping. Read the section and the first two patterns in your "
                  "own copy first."),
            ("p", "The chapter's question is how an object's links survive a trip to the "
                  "database. Objects hold references, which mean something only in a running "
                  "program; rows hold keys. And objects hold collections, where a normalized "
                  "table cannot hold a many-valued field, so the structure is reversed: an "
                  "order holds its lines, but the line row holds the order's key, and the "
                  "order row knows nothing of its lines. Fowler's answer to the first problem "
                  "is to keep each object's key in the object, and to translate between "
                  "references and keys on every load and save, with the Identity Map of "
                  "lesson 4.2 as the lookup table."),
            ("p", "Identity Field is that key in the object, and it is a tool with choices. "
                  "Fowler's first concern is meaningful against meaningless keys. A "
                  "meaningful one, such as a national identity number, should be unique and "
                  "immutable, and human error makes it neither: mistype it and fix the "
                  "mistake, and every row that refers to it must change too. So he takes, in "
                  "his words, &ldquo;a rare stand on the side of meaninglessness&rdquo;, "
                  "allowing that small or very stable systems may get away with a meaningful "
                  "key. He then weighs simple against compound keys, a long integer as the "
                  "usual type, and keys unique to a table against keys unique across the "
                  "database, which allow a single Identity Map."),
            ("p", "Getting a new key is harder than it sounds. A field the database "
                  "auto-generates is the easiest, until you insert an order and its lines and "
                  "need the order's key for the lines' foreign keys before the transaction "
                  "commits. A GUID is unique without asking anyone, but long, hard to type and read, "
                  "and a possible strain on indexes. A database counter, such as a sequence, "
                  "avoids the auto-generated field's problem, and Fowler calls it perfect "
                  "where you have one, but it is nonstandard. If you roll your own, he "
                  "prefers a separate key table to scanning for the largest key: a row per "
                  "table with the next free value, read and updated in its own short "
                  "transaction so that it does not lock out everyone else who wants a key. The pattern's examples, "
                  "one of them by Matt Foemmel and Fowler, are in the book."),
            ("p", "Foreign Key Mapping turns a reference into a key, and reverses a "
                  "collection into keys held by the children; updating such a collection "
                  "means deciding which children were added and which removed. A many-to-many "
                  "link has no single-valued end to hold the key, so Association Table "
                  "Mapping adds a table whose rows are pairs of keys. And where the children "
                  "belong to one owner and nothing else refers to them, Dependent Mapping "
                  "lets the owner's mapper save them too, often by deleting and reinserting "
                  "them all. These two the lesson names and leaves to the book."),
            ("p", "Then the order of writes. Chapter 3 says that where the database can "
                  "defer its referential integrity checks to the end of the transaction, "
                  "there is no reason not to: the order then does not matter. Otherwise the "
                  "database checks every write, and the updates must go in the right order, "
                  "for which one technique is a topological sort of the writes, an ordering "
                  "that puts every table after the tables it depends on, and another "
                  "a fixed order coded by hand. Unit of Work's discussion, in Chapter 11, "
                  "makes the same point, and adds that a fixed order of tables also reduces "
                  "deadlocks."),
            ("p", "Here is a save written for this lesson, against a database that checks "
                  "every statement. It takes the order's key from a key table on line 3, "
                  "inserts the parent row on line 4, and only then, on line 7, inserts each "
                  "line with the order's key in it. Reverse lines 4 and 7 and the first line "
                  "row would name an order that is not there yet."),
            ("code", _lines(SAVE_NEW_ORDER)),
            ("p", "Now the count. The lab reads foreign keys as records `child, parent`, "
                  "meaning the child's table holds a key to the parent's, and an order to "
                  "check if you give one. Its three tiles are an insert order with every "
                  "parent first, taking the alphabetically first ready table at each step; "
                  "the delete order, its reverse; and the keys the order given breaks, each a "
                  "child placed before its parent. In <code>order-schema</code> the keys are "
                  "`orders, customer; line, orders; line, product; payment, orders`, and the "
                  "insert order is `customer, orders, payment, product, line`, the delete "
                  "order `line, product, payment, orders, customer`."),
            ("p", "The order to check in <code>order-schema</code> is "
                  "`line orders customer product payment`, the tables as someone happened to "
                  "list them, and it breaks `3: orders before customer, line before orders, "
                  "line before product`. The preset <code>schema-only</code> gives the same "
                  "keys with no order to check, and prints the same two orders, with a dash "
                  "for the broken keys, since there is no order to break them. Ties are "
                  "broken alphabetically, so the insert order is one valid order of several; "
                  "`product` could equally go first. And the lab models a database that "
                  "checks every statement: deferred to commit, none of these orders would "
                  "matter."),
            ("h3", "Exercise"),
            ("p", "A booking schema has the keys `booking, guest; booking, room; room, hotel; "
                  "charge, booking`. Someone proposes to insert in the order `hotel guest "
                  "booking room charge`. By hand, find the keys that order breaks, write a "
                  "valid insert order and a valid delete order, and check them in the lab."),
            ("p", "Keys link objects that have rows of their own. The next lesson, Embedded "
                  "Value and Serialized LOB, reads Chapter 12's two answers for objects that "
                  "are not worth a table."),
        ],
        "lab": ("eakit", {
            "mode": "uow",
            "view": "order",
            "preset": "order-schema",
            "presets": [
                {"id": "order-schema",
                 "label": "An order schema, with the tables in the order someone listed them",
                 "keys": _ORDER_KEYS,
                 "as": "line orders customer product payment",
                 "expect": {"uwInsertOrder": "customer, orders, payment, product, line",
                            "uwDeleteOrder": "line, product, payment, orders, customer",
                            "uwBroken": "3: orders before customer, line before orders, "
                                        "line before product"}},
                {"id": "schema-only",
                 "label": "The same schema, with no order to check",
                 "keys": _ORDER_KEYS,
                 "expect": {"uwInsertOrder": "customer, orders, payment, product, line",
                            "uwDeleteOrder": "line, product, payment, orders, customer"}},
            ],
            "panel_title": "The order foreign keys put writes in",
            "panel_intro": (
                "Each record is one foreign key, child table then parent table. The lab "
                "writes an insert order with every parent first and a delete order with every "
                "child first, and lists the keys an order you give breaks. It models a "
                "database that checks every statement; with the checks deferred to commit, the "
                "order would not matter. The schemas are the lesson's, and illustrative."
            ),
        }),
        "steps_title": "Ordering writes by their keys",
        "steps_intro": "Four steps, the last of them on a schema of your own.",
        "steps": [
            ("List what each table depends on",
             "For each table, write the tables its foreign keys refer to. A table that refers "
             "to nothing can be written first."),
            ("Write an insert order",
             "Repeatedly take a table whose parents are all already written, and write it "
             "down. When several are ready, any of them will do. Reverse the list for a "
             "delete order."),
            ("Check a proposed order",
             "For each key, see whether the child comes before its parent in the order given. "
             "Each such key is broken: its first insert would name a row not yet there."),
            ("Do it on a schema of your own",
             "Take one schema you know, write its tables in an order that inserts safely, "
             "and find one foreign key whose column holds a meaningful value, such as an "
             "email address or a code. Write both down."),
        ],
        "worked": {
            "title": "Ordering the order schema",
            "intro": [
                "Take the preset order-schema and place the tables one at a time.",
            ],
            "lines": [
                "customer, product: depend on nothing",
                "orders: needs customer",
                "payment: needs orders",
                "line: needs orders and product: last",
                "inserts: customer, orders, payment,",
                "  product, line, ties alphabetical",
                "deletes: the same list reversed",
            ],
            "after": [
                "`line` waits for two parents, so it goes last whatever else is chosen. "
                "`product` could have gone first; the lab breaks the tie alphabetically, and "
                "a database deferring its checks would not care at all.",
            ],
        },
        "quiz_title": "Keys, orders and the chapter's claims",
        "quiz": [
            {"q": "The exercise's keys are `booking, guest; booking, room; room, hotel; charge, "
                  "booking`, and the order proposed is `hotel guest booking room charge`. "
                  "Which keys does it break, and what is a valid insert order?",
             "a": ["One, booking before room; guest, hotel, room, booking, charge",
                   "Two, booking before room and booking before guest; guest, hotel, "
                   "room, booking, charge",
                   "One, booking before room; charge, booking, room, hotel, guest",
                   "None; hotel, guest, booking, room, charge already follows the keys"],
             "c": 0,
             "why": "In the order given, `hotel` precedes `room`, `guest` precedes `booking` "
                    "and `booking` precedes `charge`, but `booking` comes before `room`, which "
                    "it refers to: one broken pair. A valid insert order is guest, hotel, room, "
                    "booking, charge, as the lab prints it, and deletes go in the reverse, "
                    "charge, booking, room, hotel, guest. That reverse is the delete order, not "
                    "an insert order."},
            {"q": "By Chapter 3's Mapping Relationships, which row holds the foreign key "
                  "between an order and its lines?",
             "a": ["The order row holds a list of its lines' keys",
                   "Both rows hold each other's keys",
                   "Neither: a third table holds the pairs",
                   "Each line row holds the order's key"],
             "c": 3,
             "why": "A normalized table cannot hold a many-valued field, so the structure is "
                    "reversed: the order object holds a collection of lines, but each line "
                    "row holds the key of its order. A third table of pairs is Association "
                    "Table Mapping, needed for many-to-many links."},
            {"q": "Where the database can defer its referential integrity checks to the end "
                  "of the transaction, what does Chapter 3 advise?",
             "a": ["Keep them on every statement and order the writes",
                   "Turn them off and rely on the Unit of Work",
                   "Defer them: there is no reason not to",
                   "Defer them only for deletes"],
             "c": 2,
             "why": "Fowler's first advice is to use deferral if the database has it, and "
                    "only otherwise to order the writes, with a topological sort as one "
                    "technique. With the checks deferred, the order of writes inside the "
                    "transaction does not matter. The lab models the other case."},
            {"q": "Why does Identity Field's discussion distrust meaningful keys such as a "
                  "national identity number?",
             "a": ["They take more space than a long integer, which slows every join on "
                   "them",
                   "Mistakes make them neither unique nor immutable, and a fix reaches "
                   "every foreign key",
                   "Databases cannot index them, so every lookup by key scans the table",
                   "They cannot be used as foreign keys, so links need a second, "
                   "meaningless key"],
             "c": 1,
             "why": "Keys must be unique to work at all and immutable to work well; a "
                    "mistyped number is neither once it is corrected, and the correction "
                    "reaches every row that refers to it. Fowler allows that small or very "
                    "stable systems may get away with one, and otherwise prefers keys that "
                    "mean nothing to the business."},
        ],
        "mistakes": [
            ("Using a meaningful key to save a column",
             "An email address or an account code is already unique, so it looks wasteful to "
             "add a number. Fowler takes &ldquo;a rare stand on the side of "
             "meaninglessness&rdquo;: a meaningful key can change or be mistyped, and every "
             "foreign key holding it must change with it, where a meaningless key never needs "
             "to. He allows that small or very stable systems may get away with a meaningful "
             "one."),
            ("Expecting the object's structure in the tables",
             "In memory an order holds its lines, so it seems the order row should hold its "
             "lines' keys. The table structure is the reverse: the child holds the parent's "
             "key, because a row cannot hold a many-valued field. That reversal is what makes "
             "saving a collection awkward, and Foreign Key Mapping's update options deal with "
             "it."),
            ("Ordering writes when the database can wait",
             "A topological sort of the writes is a real technique, and the lab performs one. "
             "But Chapter 3's first advice is to defer the integrity checks to commit where "
             "the database allows it, and then no order is needed. Ordering is the answer "
             "only for a database that checks every statement."),
        ],
        "standard": (
            "Finish when you can order a schema's writes by hand.",
            "Given which tables hold foreign keys to which, write an insert order and a "
            "delete order, and find the broken pairs in an order given."
        ),
        "note": (
            "The lab orders whole tables. Real writes are rows, and a table that refers to "
            "itself, a manager column in a staff table, needs its rows ordered, which the lab "
            "refuses to attempt. It also cannot tell you whether your database defers its "
            "checks; if it does, the order it prints is one you no longer need."
        ),
    },
]
