"""Objects and Tables, lessons 5-8 -- embedded values, inheritance, metadata.

Fowler et al., Patterns of Enterprise Application Architecture
(Addison-Wesley, 2002): Chapter 3, Structural Mapping Patterns (the
paragraphs on Embedded Value and Serialized LOB, and Inheritance) and Using
Metadata; Chapter 12, Embedded Value, Serialized LOB, Single Table, Class
Table and Concrete Table Inheritance, and Inheritance Mappers; Chapter 13,
Metadata Mapping, Query Object and Repository. The lessons cite the book by
chapter, section and pattern; the PDF page of the operator's copy is given
only in the comments beside each lesson. Every quotation is copied from that
copy and checked with ea_quotes.py; every figure attributed to the book
carries its PLAN section S.2 id. The code is written for these lessons, and
none of the book's listings or example domains is reproduced. Each snippet is
one constant below, verbatim from docs/enterprise-patterns/presets.py, used
by the lesson's code block and, in lesson 8, by the lab preset that counts it.
"""


def _lines(text):
    """A snippet constant as a code block's list of lines."""
    return text.split("\n")


# ---------------------------------------------------------------- snippets

EMBEDDED_TERM = """\
// The lease's term has no table of its own: it is two columns.
Lease load(ResultSet rs) throws SQLException {
    DateRange term = new DateRange(
        rs.getDate("term_start").toLocalDate(),
        rs.getDate("term_end").toLocalDate());
    return new Lease(rs.getLong("id"), term);
}"""

THREAD_TEXT = """\
// Writes a reply thread into one text column, a line per post.
String toText(Post first) {
    StringBuilder out = new StringBuilder();
    Deque<Post> todo = new ArrayDeque<Post>();
    Deque<Integer> depths = new ArrayDeque<Integer>();
    todo.push(first);
    depths.push(0);
    while (!todo.isEmpty()) {
        Post p = todo.pop();
        int depth = depths.pop();
        out.append(depth).append(' ').append(p.id()).append('\\n');
        List<Post> replies = p.replies();
        for (int i = replies.size() - 1; i >= 0; i--) {
            todo.push(replies.get(i));
            depths.push(depth + 1);
        }
    }
    return out.toString();
}"""

SINGLE_TABLE_LOAD = """\
// One table for every kind of staff; a type column says which.
Staff load(ResultSet rs) throws SQLException {
    String type = rs.getString("type");
    long id = rs.getLong("id");
    String name = rs.getString("name");
    if (type.equals("C")) {
        return new Contractor(id, name, rs.getLong("day_rate"));
    }
    long salary = rs.getLong("salary");
    if (type.equals("M")) {
        return new Manager(id, name, salary, rs.getInt("reports"));
    }
    return new Employee(id, name, salary);
}"""

CLASS_TABLE_FIND = """\
// A manager's fields live in three tables, one per class.
static final String FIND_MANAGER =
    "SELECT p.name, e.salary, m.reports"
    + " FROM person p"
    + " JOIN employee e ON e.id = p.id"
    + " JOIN manager m ON m.id = p.id"
    + " WHERE p.id = ?";"""

HAND_MAPPING = """\
Member findMember(long id) throws SQLException {
    PreparedStatement s = db.prepareStatement(MEMBER_BY_ID);
    s.setLong(1, id);
    ResultSet rs = s.executeQuery();
    rs.next();
    Member m = new Member(id);
    m.email = rs.getString("email");
    m.city = rs.getString("city");
    return m;
}
Shop findShop(long id) throws SQLException {
    PreparedStatement s = db.prepareStatement(SHOP_BY_ID);
    s.setLong(1, id);
    ResultSet rs = s.executeQuery();
    rs.next();
    Shop p = new Shop(id);
    p.name = rs.getString("name");
    p.city = rs.getString("city");
    return p;
}"""

METADATA_FIND = """\
// The mapping held as data: each column and the field it fills.
static final String[][] MEMBER_MAP = {{"email", "email"},
                                      {"city", "city"}};

// One finder for every mapped class, which reads the map.
<T> T find(Class<T> type, String sql, String[][] map, long id)
        throws Exception {
    PreparedStatement s = db.prepareStatement(sql);
    s.setLong(1, id);
    ResultSet rs = s.executeQuery();
    rs.next();
    T obj = type.getDeclaredConstructor(long.class).newInstance(id);
    for (String[] column : map) {
        Object value = rs.getObject(column[0]);
        type.getDeclaredField(column[1]).set(obj, value);
    }
    return obj;
}"""

# Exercise snippet (not a preset: the exercise is the reader's).
INVOICE_FINDERS = """\
Invoice findInvoice(long id) throws SQLException {
    PreparedStatement s = db.prepareStatement(INVOICE_BY_ID);
    s.setLong(1, id);
    ResultSet rs = s.executeQuery();
    rs.next();
    Invoice i = new Invoice(id);
    i.total = rs.getLong("total");
    i.due = rs.getDate("due");
    return i;
}

Receipt findReceipt(long id) throws SQLException {
    PreparedStatement s = db.prepareStatement(RECEIPT_BY_ID);
    s.setLong(1, id);
    ResultSet rs = s.executeQuery();
    rs.next();
    Receipt r = new Receipt(id);
    r.paid = rs.getLong("paid");
    return r;
}"""

# The staff hierarchy of lessons 6 and 7, stated once.
_STAFF = ("person, -, 3, no; employee, person, 2, yes; manager, employee, 2, yes; "
          "contractor, person, 2, yes")


LESSONS = [
    # ---------------------------------------------------------------- 05
    # Chapter 3, Structural Mapping Patterns (PDF p. 55 of the operator's
    # copy): small Value Objects embedded, Serialized LOB for hierarchic
    # structures, SQL not aware of it. Chapter 12, Embedded Value (PDF pp.
    # 246-248; When to Use It pp. 246-247) and Serialized LOB (pp. 249-253;
    # BLOB and CLOB pp. 249-250, identity problems p. 250, When to Use It p.
    # 250). The book's own example (a department hierarchy, from p. 250) is
    # pointed to, not reused: the lesson's tree is a reply thread, and its
    # serializer an explicit-stack walk, not a recursive element builder.
    # Quote: PDF p. 55, 20 words, ea_quotes.py OK. Lesson total: 20 words.
    # The course's one modern aside (PLAN section F rule 3) is the late p on
    # databases that query inside a document column.
    {
        "slug": "embedded-value-and-serialized-lob",
        "title": "Embedded Value and Serialized LOB",
        "module": "Chapter 12 · Object-Relational Structural Patterns",
        "one_line": "A small value goes into its owner's row as columns; a whole tree of objects can go into one column, read at once and invisible to SQL.",
        "summary": (
            "Some objects are not worth a table of their own. Chapter 12's Embedded Value "
            "stores a small Value Object, a date range or an amount, as columns in its owner's "
            "row; its Serialized LOB stores a whole graph of objects, a tree, in one large "
            "column. Count the queries that read a tree one node at a time, one level at a "
            "time, and from one column."
        ),
        "key": [
            "a small value: columns in the owner row",
            "an embedded value has no key of its own",
            "a whole graph: one large column",
            "read in one query, but opaque to SQL",
            "node by node: 1 + nodes queries",
            "level by level: depth + 1 queries",
        ],
        "key_label": "Two ways to skip a table, in six lines",
        "concepts_intro": (
            "Two patterns from Chapter 12 carry the lesson, and one term the second depends "
            "on."
        ),
        "concepts": [
            ("Embedded Value",
             "An object mapped into several fields of its owner's table. The owner loads and "
             "saves it, and it has no persistence of its own; Fowler calls it a special case of "
             "Dependent Mapping with a single dependent."),
            ("Serialized LOB",
             "A graph of objects serialized into one large object and stored in one database "
             "field. It reads a whole structure in one go, and SQL cannot see inside it."),
            ("BLOB and CLOB",
             "The two forms of a large object: binary, compact and impenetrable to anyone "
             "browsing the table; or character text, readable and larger, which XML makes easy "
             "to parse and more verbose still."),
        ],
        "read_title": "Two patterns for objects without tables",
        "read_intro": (
            "Read the paragraphs on small values and on large objects in Chapter 3's "
            "Structural Mapping Patterns, then Embedded Value and Serialized LOB in Chapter "
            "12, in your own copy first. The lesson reads both patterns as tools, then counts "
            "the queries a tree takes to read."
        ),
        "body": [
            ("p", "&ldquo;If you use it too much, it ends up turning your database into "
                  "little more than a transactional file system.&rdquo; That is Chapter 3's "
                  "caution about Serialized LOB, in Structural Mapping Patterns, and this "
                  "lesson reads it with the companion pattern, Embedded Value, both in "
                  "Chapter 12. Read them in your own copy first."),
            ("p", "The chapter's question is which objects deserve a table. Its first answer "
                  "is about small values. A date range or an amount of money is a Value "
                  "Object, Course 2's pattern: it has no identity, only a value, so nobody "
                  "needs to find it by key, and Chapter 12's Embedded Value thinks a table "
                  "of nothing but amounts absurd. Its fields go into the owner's "
                  "row instead, and the owner loads and saves them. Because a value has no "
                  "identity it needs no Identity Map either: you can make a new one on every "
                  "read."),
            ("p", "Embedded Value's grey area is the reference object, a shipping record "
                  "on an order, say. The questions Fowler asks are whether it means anything "
                  "outside the order, whether it is always loaded with it, and whether "
                  "anyone queries it separately through SQL. He uses the pattern for a "
                  "reference object mostly where the link is one-to-one. Its great advantage "
                  "over a LOB, he says, is that SQL can still query the embedded values."),
            ("p", "Here is an embedded value written for this lesson. A lease's term is a "
                  "`DateRange`, built on lines 3 to 5 from two columns of the lease's own "
                  "row, `term_start` and `term_end`. The range has no key and no table; line "
                  "6 hands it to the lease with the lease's own key."),
            ("code", _lines(EMBEDDED_TERM)),
            ("p", "Serialized LOB is the same move on a larger scale: take a cluster of "
                  "objects and save it as a single column. Chapter 3 names the use for it, "
                  "hierarchic structures such as an organization chart or a bill of "
                  "materials, which a relational schema reads with many small calls and a "
                  "LOB reads in one. Chapter 12 gives the two forms. A binary LOB is simple "
                  "where the platform serializes for you and takes the least space, but "
                  "nobody can read the field without the program, and a changed class may "
                  "not read its own old serializations. A text LOB can be read by a person "
                  "browsing the table; XML spares you writing a parser, at the cost of more "
                  "space."),
            ("p", "Its warnings are about what the column hides. SQL cannot query inside it, "
                  "so the pattern suits a group of objects nobody will want to query from "
                  "outside the application. It invites duplication: put a customer's details "
                  "in a LOB on every order and each update must find them all, unless a "
                  "snapshot of the customer at the time of the order is exactly what you "
                  "want. And it works poorly when objects outside the LOB must refer to "
                  "objects inside it. Fowler also thinks it is considered less often than it "
                  "might be. Here is a text serialization written for this lesson, for a "
                  "discussion thread whose posts answer one another. It walks the thread "
                  "with an explicit stack of posts and a matching stack of depths (lines 4 "
                  "to 7), and writes one line per post, its depth, a space and its id (line "
                  "11). The replies are pushed last first (lines 13 to 16), so they come off "
                  "the stack in order. A first post with one reply that has its own reply "
                  "becomes three lines, `0 start`, `1 ann` and `2 bo`."),
            ("code", _lines(THREAD_TEXT)),
            ("p", "Now the count. The lab reads a tree as records `node, parent`, with a dash "
                  "for the root, and prints five tiles: the nodes; the depth, counting the "
                  "root as 1; the queries to read the tree one node at a time, one for the "
                  "root and then one for each node's children; the queries one level at a "
                  "time; and the queries for a LOB, always 1. In <code>thread</code>, a "
                  "first post `start` with two replies, `ann` and `dee`; `bo` and `cy` "
                  "answering `ann`; `eli` answering `dee`; and `fay` and `gus` answering "
                  "`eli`, there are 8 posts, depth 4, 9 queries post by post, 5 level by "
                  "level and 1 from the column."),
            ("p", "Both multi-query counts include the queries that come back empty: each "
                  "leaf's query for children it does not have, and the query for the level "
                  "below the deepest, which is how a program reading level by level finds "
                  "that it has finished. The preset <code>flat-thread</code>, a first post "
                  "with three replies and nothing below them, has 4 nodes and depth 2: 5 "
                  "queries node by node, 3 level by level, 1 as a LOB. The column always wins "
                  "on queries, and the tiles cannot show what it costs: every query you might "
                  "have run against the posts, such as all of one person's replies, is gone."),
            ("p", "That cost is the one part of the chapter that time has moved. Fowler "
                  "already expected XML query extensions to SQL to soften it, while noting "
                  "that they were largely nonstandard. Many databases now store a JSON or XML "
                  "document in a column and can index and query inside it, which takes away "
                  "part of the reason not to use a LOB. The other reasons, duplication, "
                  "references into the blob, and other programs that read the tables, are "
                  "untouched by that, and whether a queryable document column is a LOB or a "
                  "small database of its own is still argued."),
            ("h3", "Exercise"),
            ("p", "A tree has the records `root, -; a, root; b, a; c, b; d, c; e, root`. By "
                  "hand, give its nodes and depth, and the queries to read it node by node, "
                  "level by level and as a Serialized LOB. Then type it into the lab."),
            ("p", "A reply thread is one kind of hierarchy. The next lesson, Single "
                  "Table Inheritance, reads the other kind Chapter 3 names, a hierarchy of "
                  "classes, and the first of three ways to map it."),
        ],
        "lab": ("eakit", {
            "mode": "load",
            "view": "tree",
            "preset": "thread",
            "presets": [
                {"id": "thread",
                 "label": "A reply thread: a first post and seven replies, four levels deep",
                 "nodes": "start, -; ann, start; bo, ann; cy, ann; "
                          "dee, start; eli, dee; fay, eli; gus, eli",
                 "expect": {"ldNodes": "8", "ldDepth": "4", "ldPerNode": "9",
                            "ldPerLevel": "5", "ldLob": "1"}},
                {"id": "flat-thread",
                 "label": "A flat thread: a first post with three replies",
                 "nodes": "start, -; ann, start; bo, start; cy, start",
                 "expect": {"ldNodes": "4", "ldDepth": "2", "ldPerNode": "5",
                            "ldPerLevel": "3", "ldLob": "1"}},
            ],
            "panel_title": "Queries to read a tree",
            "panel_intro": (
                "Each record is one node and its parent, with - for the root. The lab counts "
                "the queries to read the tree a node at a time, a level at a time, and from one "
                "column. The trees are the lesson's, and illustrative."
            ),
        }),
        "steps_title": "Counting the queries a tree needs",
        "steps_intro": "Four steps, the last of them on a schema of your own.",
        "steps": [
            ("Count the nodes and the depth",
             "Count every node, and find the longest path from the root down, counting the "
             "root as level 1."),
            ("Count node by node",
             "One query reads the root, and each node then needs one query for its children, "
             "leaves included, whose queries return nothing: 1 + the nodes."),
            ("Count level by level and as a LOB",
             "One query per level, plus the one that finds the level below the deepest empty: "
             "the depth + 1. Read from one column, the whole tree is 1 query."),
            ("Do it on a column of your own",
             "Find one column in a schema you know that holds JSON, XML or another serialized "
             "structure, and write down one query someone might want that the column now "
             "prevents or makes harder."),
        ],
        "worked": {
            "title": "Reading the thread",
            "intro": [
                "Take the preset thread and count by each rule.",
            ],
            "lines": [
                "nodes: 8",
                "deepest: start, dee, eli, fay: depth 4",
                "node by node: 1 for start + 8, so 9",
                "level by level: 4 levels + 1 empty, so 5",
                "from one column: 1",
            ],
            "after": [
                "The node-by-node count grows with the size of the tree and the level count "
                "with its depth; the LOB stays at one. What the one query gives up is every "
                "query SQL could have run on the rows.",
            ],
        },
        "quiz_title": "Trees, queries and the chapter's warnings",
        "quiz": [
            {"q": "The exercise's tree is `root, -; a, root; b, a; c, b; d, c; e, root`. How "
                  "many queries does it take node by node, level by level and as a LOB?",
             "a": ["6, 5 and 1",
                   "7, 5 and 1",
                   "7, 6 and 1",
                   "6, 6 and 1"],
             "c": 2,
             "why": "There are 6 nodes, and the path root, a, b, c, d gives depth 5. Node by "
                    "node is 1 + 6 = 7, counting the leaves' empty queries; level by level is "
                    "5 + 1 = 6, counting the empty level below d; a LOB is always 1. The other "
                    "answers drop one or both of the empty queries."},
            {"q": "Why does Chapter 12 say Embedded Value suits a Value Object such as a date "
                  "range?",
             "a": ["It is always too large to fit beside the owner's other columns",
                   "It has no identity, so it needs no key, no table and no Identity Map",
                   "Its fields cannot be queried, so they may as well be embedded",
                   "It needs a key of its own, which the owner's row supplies to it"],
             "c": 1,
             "why": "A Value Object is equal to any other with the same value, so nothing ever "
                    "finds it by key; it is saved as columns of its owner's row and created "
                    "afresh on each read. The embedded columns can still be queried, which is "
                    "the pattern's advantage over a LOB. The owner's key is the owner's, not "
                    "the value's."},
            {"q": "Serialized LOB's discussion warns against putting a customer's details in a "
                  "LOB on every order. Why?",
             "a": ["A LOB cannot hold more than one customer, so each order needs its own",
                   "A LOB on an order cannot be read in the same query as the order",
                   "Orders cannot have large columns beside their own small ones",
                   "The customer data is copied on every order, so an update must reach "
                   "them all"],
             "c": 3,
             "why": "The details would be duplicated in every order, which makes updates a "
                    "problem. Fowler notes the exception: when a snapshot of the customer as "
                    "it was when the order was placed is what you want, the copy is the point. "
                    "Otherwise put the LOB in a customer table and let orders refer to it."},
            {"q": "A first post with five replies and nothing below them. How many queries "
                  "does the lab count level by level?",
             "a": ["3",
                   "2",
                   "6",
                   "7"],
             "c": 0,
             "why": "The tree has depth 2, the first post and its replies, and level by level "
                    "is the depth + 1: a query for each level and one that finds nothing below "
                    "the replies. Node by node it would be 1 + 6 = 7."},
        ],
        "mistakes": [
            ("Preferring a Serialized LOB because it is fast",
             "On this view one query beats nine, so the LOB is the better design. It is one "
             "read, and on the lesson's illustration, <code>thread</code>, one against 9 "
             "node by node; but nothing else can query inside it, and Fowler's caution is the "
             "opening quotation: lean on it everywhere and the database is reduced to storing "
             "files with transactions. He recommends it for a fairly self-contained group of "
             "objects nobody will query from outside the application."),
            ("Giving an Embedded Value a key of its own",
             "An embedded value seems to need an id like any other object. It has none: it is "
             "part of its owner's row and is loaded and saved with it, which is exactly why "
             "it suits a Value Object, whose identity is its value."),
            ("Copying shared data into many LOBs",
             "A LOB is easy to write, so it is tempting to serialize whatever an object holds, "
             "a customer's details on each order, say. The data is then duplicated, and an "
             "update must find every copy. Chapter 12's rule is that what a LOB holds should "
             "be reachable only through the one object that owns it."),
        ],
        "standard": (
            "Finish when you can count a tree's queries under three choices by hand.",
            "Given a tree as node, parent records, state its depth and the queries to read it "
            "one node at a time, one level at a time, and from one column."
        ),
        "note": (
            "The lab counts queries, not their cost or what they return, so it shows the "
            "LOB's one read and nothing of what it gives up: the queries SQL can no longer "
            "run, the duplication, the old serializations a changed class cannot read. "
            "Whether your database can query inside a document column is a fact about your "
            "database that the count cannot know."
        ),
    },
    # ---------------------------------------------------------------- 06
    # Chapter 3, Inheritance (PDF pp. 55-57 of the operator's copy): the three
    # options p. 55; the trade-offs, compression, Fowler's first choice and
    # mixing p. 57. Chapter 12, Single Table Inheritance (PDF pp. 254-260;
    # How It Works p. 254, strengths and weaknesses p. 255).
    # Quote: PDF p. 57, 13 words, ea_quotes.py OK. Lesson total: 13 words.
    {
        "slug": "single-table-inheritance",
        "title": "Single Table Inheritance",
        "module": "Chapter 12 · Object-Relational Structural Patterns",
        "one_line": "Map a whole class hierarchy to one table with a type code: no joins and one place to change, at the price of empty columns and one large table.",
        "summary": (
            "Chapter 3 gives three ways to map a class hierarchy to tables and says the "
            "trade-off is between duplicated structure and speed of access. Chapter 12's "
            "Single Table Inheritance is the first: every class in one table, with a type "
            "code. Count the tables, columns, empty columns and tables touched for a staff "
            "hierarchy under all three mappings, and read the single-table figures."
        ),
        "key": [
            "every class in one table, with a type",
            "columns: key + type + every field",
            "empty: fields the class of a row lacks",
            "loading touches one table, no joins",
            "adding a field alters one table",
            "costs: empty columns and one big table",
        ],
        "key_label": "Single Table Inheritance in six lines",
        "concepts_intro": (
            "Three ideas carry the lesson: the three mappings, the type code, and the chain "
            "of classes a row must hold."
        ),
        "concepts": [
            ("The three inheritance mappings",
             "Chapter 3's options for a class hierarchy: one table for all the classes "
             "(Single Table Inheritance), one table for each class (Class Table Inheritance), "
             "or one table for each concrete class, holding its inherited fields too "
             "(Concrete Table Inheritance)."),
            ("Type code",
             "A column in the single table that says which class each row is, a code or a "
             "class name. The loader reads it first to choose the class; a code needs a table "
             "in the program that must grow with the hierarchy."),
            ("A class's chain",
             "The class and its ancestors. A row of a class holds its chain's fields; in a "
             "single table every other field's column is empty in that row."),
        ],
        "read_title": "The three options first, then the first of them",
        "read_intro": (
            "Read Inheritance in Chapter 3's Structural Mapping Patterns, then Single Table "
            "Inheritance in Chapter 12, in your own copy first. The lesson reads the "
            "chapter's trade-off as an argument, then the pattern as a tool, and counts one "
            "hierarchy under all three mappings."
        ),
        "body": [
            ("p", "&ldquo;The trade-offs are all between duplication of data structure and "
                  "speed of access.&rdquo; Chapter 3 says it of the three ways to map a class "
                  "hierarchy, in the Inheritance part of Structural Mapping Patterns. This "
                  "lesson reads that argument and the first of the three patterns, Single "
                  "Table Inheritance, in Chapter 12; the next lesson reads the other two. "
                  "Read the section and the pattern in your own copy first."),
            ("p", "The chapter's question is how to store inheritance in a database that has "
                  "none. There are, Fowler says, basically three options. One table for every "
                  "class in the hierarchy is Single Table Inheritance. One table for each "
                  "class, each holding only the fields that class declares, is Class Table "
                  "Inheritance, the simplest correspondence between classes and tables, at "
                  "the cost of joins to load one object. One table for each concrete class, "
                  "holding all its inherited fields as well, is Concrete Table Inheritance, "
                  "with no joins to load but brittle when a superclass changes."),
            ("p", "Single Table Inheritance has its own costs. Every row has columns for all "
                  "the fields of every class, and a row uses only its own class's, so the rest "
                  "are empty: wasted space, though Fowler notes that many databases compress "
                  "it well. The one table can grow large, with many indexes and frequent "
                  "locking, and become a bottleneck. What it buys, as Chapter 3 weighs it, is "
                  "a single home for the whole hierarchy: a change has one table to touch, "
                  "and no load ever needs a join."),
            ("p", "Chapter 3 then declines to name a winner, and says what Fowler himself "
                  "usually does: start with the single table, because it is simple to build "
                  "and survives most reshuffling of the classes, and reach for the other two "
                  "when particular subclasses bring too many columns nobody else uses. The "
                  "three may be combined in one hierarchy, which adds complexity, and he "
                  "suggests asking the database administrators which access patterns suit "
                  "their database."),
            ("p", "Chapter 12 adds the pattern's working parts. The table needs a column that "
                  "says which class each row is: a class name, which takes space and ties "
                  "the schema to the class names, or a code, which some code must translate "
                  "and which grows with the hierarchy. On load the code is read first to "
                  "choose the class. Among the pattern's strengths, a field pushed up or down "
                  "the hierarchy needs no change to the database; among its weaknesses, the "
                  "columns share one namespace, so two classes cannot use one name for "
                  "different fields."),
            ("p", "Here is a single-table load written for this lesson. It reads the type "
                  "code on line 3 and the columns every person has on lines 4 and 5. A "
                  "contractor adds only `day_rate` (lines 6 to 8). Everyone else is an "
                  "employee, so line 9 reads `salary` once; a manager adds `reports` as well "
                  "(lines 10 to 12), and line 13 builds a plain employee. Every one of those "
                  "columns is in every row, and in each row the ones its class does not use "
                  "are empty."),
            ("code", _lines(SINGLE_TABLE_LOAD)),
            ("p", "Now the count. The lab reads a hierarchy as records of a class, its parent "
                  "(a dash for the root), how many fields it declares itself, and whether it is "
                  "concrete, with a class to load, one to find and one to add a field to. Each "
                  "three-part tile is single table, class table, concrete table, in that "
                  "order. Every table has a key column, and the single table a type column "
                  "too. In <code>staff</code>, a person with 3 fields, not concrete; an "
                  "employee with 2; a manager, under employee, with 2; and a contractor, under "
                  "person, with 2: the tables are `1, 4, 3` and the columns `11, 13, 20`."),
            ("p", "The single table's 11 columns are a key, a type and 3 + 2 + 2 + 2 = 9 "
                  "field columns. The `ihEmpty` tile is single-table only: the columns empty "
                  "in a row of the class loaded. A manager's row uses its chain's 3 + 2 + 2 = "
                  "7 fields, so 2 of the 9 are empty, the contractor's two. Loading a manager "
                  "touches `1, 3, 1` tables: one under single table, three joined under class "
                  "table, one under concrete. The preset <code>load-an-employee</code> loads "
                  "an employee instead, whose row uses 5 fields and leaves 4 empty, and whose "
                  "load touches `1, 2, 1`."),
            ("p", "The other two tiles are the next lesson's, and the single table's figure in "
                  "each is always 1. Finding every person, subclasses included, reads `1, 4, "
                  "3` tables in <code>staff</code>; adding a field to person alters `1, 1, "
                  "3`. However the hierarchy changes, there is one table to read and one to "
                  "alter. That is the single place Fowler's advantage names, and the empty "
                  "columns are what it costs."),
            ("h3", "Exercise"),
            ("p", "A fleet hierarchy has the records `vehicle, -, 4, no; car, vehicle, 2, yes; "
                  "van, vehicle, 3, yes; truck, vehicle, 5, yes`, and you load a van. By hand, "
                  "give the single table's columns and the columns empty in a van's row, then "
                  "the columns and tables of the other two mappings. Check them in the lab."),
            ("p", "The single table pays in empty columns; the other two pay in tables. The "
                  "next lesson, Class and Concrete Table Inheritance, counts what loading, "
                  "finding and altering touch under each."),
        ],
        "lab": ("eakit", {
            "mode": "inherit",
            "view": "tables",
            "preset": "staff",
            "classes": _STAFF,
            "presets": [
                {"id": "staff",
                 "label": "Staff: load a manager, find every person, add a field to person",
                 "load": "manager", "find": "person", "alter": "person",
                 "expect": {"ihTables": "1, 4, 3", "ihColumns": "11, 13, 20",
                            "ihEmpty": "2", "ihLoad": "1, 3, 1",
                            "ihFind": "1, 4, 3", "ihAlter": "1, 1, 3"}},
                {"id": "load-an-employee",
                 "label": "Staff: load an employee, find employees, add a field to manager",
                 "load": "employee", "find": "employee", "alter": "manager",
                 "expect": {"ihEmpty": "4", "ihLoad": "1, 2, 1",
                            "ihFind": "1, 3, 2", "ihAlter": "1, 1, 1"}},
            ],
            "panel_title": "One hierarchy under three mappings",
            "panel_intro": (
                "Each record is a class, its parent, the fields it declares itself, and whether "
                "it is concrete. Every three-part tile is single table, class table, concrete "
                "table, in that order. The hierarchies are the lesson's, and illustrative."
            ),
        }),
        "steps_title": "Counting a single table",
        "steps_intro": "Four steps, the last of them on a hierarchy of your own.",
        "steps": [
            ("Total the fields",
             "Add up the fields every class declares itself. The single table has that many "
             "field columns, plus a key and a type."),
            ("Find the loaded class's chain",
             "List the class and its ancestors, and add up their fields: those are the columns "
             "a row of that class uses."),
            ("Count the empty columns",
             "Subtract the chain's fields from the total. That many columns are empty in "
             "every row of the class."),
            ("Do it on a hierarchy of your own",
             "Take one class hierarchy in a system you know, write which of the three mappings "
             "it uses, and count the columns a row of its largest subclass leaves empty under "
             "a single table."),
        ],
        "worked": {
            "title": "A manager in the staff table",
            "intro": [
                "Take the preset staff and count the single table, then a manager's row.",
            ],
            "lines": [
                "fields: 3 + 2 + 2 + 2, so 9",
                "columns: key + type + 9, so 11",
                "chain of a manager: person, employee,",
                "  manager",
                "its fields: 3 + 2 + 2, so 7",
                "empty in its row: 9 − 7, so 2",
            ],
            "after": [
                "The two empty columns are the contractor's. Every manager row carries them, "
                "and every contractor row carries the employee's and the manager's four.",
            ],
        },
        "quiz_title": "Columns, empty columns and the chapter's claims",
        "quiz": [
            {"q": "The exercise's hierarchy is `vehicle, -, 4, no; car, vehicle, 2, yes; van, "
                  "vehicle, 3, yes; truck, vehicle, 5, yes`, loading a van. What are the single "
                  "table's columns and a van row's empty columns, and the other two mappings' "
                  "columns?",
             "a": ["Single 14, 7 empty; class table 14 in 4 tables; concrete 21 in 3",
                   "Single 16, 7 empty; class table 18 in 4 tables; concrete 25 in 3",
                   "Single 16, 9 empty; class table 18 in 4 tables; concrete 25 in 3",
                   "Single 16, 7 empty; class table 18 in 3 tables; concrete 25 in 4"],
             "c": 1,
             "why": "The fields are 4 + 2 + 3 + 5 = 14, so the single table has 2 + 14 = 16 "
                    "columns; a van uses 4 + 3 = 7, leaving 7 empty. Class table: a table a "
                    "class, each with a key, 5 + 3 + 4 + 6 = 18 columns in 4 tables. Concrete "
                    "table: one for each of car, van and truck, each a key and its chain's "
                    "fields, 7 + 8 + 10 = 25 in 3. Fourteen forgets the key and type; 9 empty "
                    "counts only the van's own fields as used."},
            {"q": "What does Chapter 3 name as Single Table Inheritance's great advantage?",
             "a": ["No wasted space, since every column in the table is used by every row",
                   "The simplest correspondence between classes and tables, one for one",
                   "Each table is read only when its own class is, spreading the load",
                   "One table for the hierarchy: changes touch one place and loads never join"],
             "c": 3,
             "why": "Chapter 3 credits the single table with keeping the whole hierarchy in "
                    "one place, so that a change touches one table and no load joins. The simplest correspondence is Class "
                    "Table Inheritance's strength, and spreading access across tables is "
                    "Concrete Table Inheritance's; wasted space is the single table's best-known "
                    "cost."},
            {"q": "In the staff hierarchy, a contractor declares 2 fields and person 3. How "
                  "many columns are empty in a contractor's row of the single table?",
             "a": ["4",
                   "2",
                   "5",
                   "6"],
             "c": 0,
             "why": "The single table has 9 field columns. A contractor's chain is contractor "
                    "and person, 2 + 3 = 5 fields, so 9 − 5 = 4 are empty: the employee's 2 "
                    "and the manager's 2."},
        ],
        "mistakes": [
            ("Calling Single Table Inheritance the beginner's mapping",
             "On this view one table for a hierarchy is the naive design that a careful one "
             "outgrows. Fowler credits it with keeping the hierarchy in one place with no "
             "joins, and says he usually starts with it, turning to the other two when "
             "needed; its costs are the empty columns and the size of the one table. The "
             "chapter's trade-off is between duplication and speed, and no mapping wins it "
             "everywhere."),
            ("Thinking the empty columns waste most of the table",
             "Every row carries every class's columns, so the waste looks enormous. Fowler "
             "notes that many databases compress empty columns very well; on the lesson's "
             "illustration a manager's row leaves 2 of its 9 field columns empty. How much "
             "the space matters depends on the database and the data."),
            ("Forgetting the type column has to be kept",
             "The type code looks like a detail of the table. It is part of the program too: "
             "a code must be translated into a class, and that translation must grow every "
             "time a class is added. Storing the class name instead avoids the table but ties "
             "the schema to the names of the classes."),
        ],
        "standard": (
            "Finish when you can count a single table and its empty columns by hand.",
            "Given a hierarchy with each class's own field count, state the single table's "
            "tables and columns, and the columns empty in a given class's row."
        ),
        "note": (
            "The lab counts columns, not bytes: it cannot say how well your database "
            "compresses empty columns, which Fowler says decides how much they matter. Nor "
            "does it count the locking and index contention on one large table, the "
            "pattern's other cost, because that depends on the load and not on the schema."
        ),
    },
    # ---------------------------------------------------------------- 07
    # Chapter 12, Class Table Inheritance (PDF pp. 261-268 of the operator's
    # copy; How It Works pp. 261-262, When to Use It p. 262), Concrete Table
    # Inheritance (pp. 269-276; keys p. 269, referential integrity and finds p.
    # 270, When to Use It pp. 270-271), Inheritance Mappers (pp. 277-278; the
    # "heinous crime" p. 278). Chapter 3, Inheritance, PDF p. 57 (mixing).
    # Quote: PDF p. 262, 21 words, ea_quotes.py OK; "a heinous crime", p.
    # 278, 3 words. Lesson total: 24 words.
    {
        "slug": "class-and-concrete-table-inheritance",
        "title": "Class and Concrete Table Inheritance",
        "module": "Chapter 12 · Object-Relational Structural Patterns",
        "one_line": "A table per class joins to load and changes least; a table per concrete class loads from one table and changes everywhere a superclass does.",
        "summary": (
            "Chapter 12's other two inheritance mappings make opposite trade-offs. Class Table "
            "Inheritance gives each class its own table and joins them to load an object; "
            "Concrete Table Inheritance gives each concrete class one table holding every "
            "inherited field. Count what loading, finding and altering touch under each, and "
            "read how Inheritance Mappers organizes the code for all three."
        ),
        "key": [
            "class table: a table per class",
            "loading joins every ancestor table",
            "concrete table: one per concrete class",
            "loading reads one table, no joins",
            "a superclass find unions every table",
            "a superclass change alters every table",
        ],
        "key_label": "The other two mappings in six lines",
        "concepts_intro": (
            "Two mappings and one structure carry the lesson."
        ),
        "concepts": [
            ("Class Table Inheritance",
             "One table for each class in the hierarchy, holding the fields that class "
             "declares. The rows of one object usually share one key value across the tables, and loading it "
             "joins the tables of its class and its ancestors."),
            ("Concrete Table Inheritance",
             "One table for each concrete class, holding all its fields, inherited ones "
             "included. Loading needs no join, but superclass fields are duplicated in every "
             "table, and keys must be unique across all of them."),
            ("Inheritance Mappers",
             "A structure of mapper classes for any of the three mappings: one mapper per "
             "domain class, each loading its own class's fields and calling its superclass "
             "mapper for the rest, with a mapper for the abstract class that delegates to the "
             "right concrete one."),
        ],
        "read_title": "Two patterns, read against each other",
        "read_intro": (
            "Read Class Table Inheritance, Concrete Table Inheritance and Inheritance Mappers "
            "in Chapter 12, and the end of Chapter 3's Inheritance, in your own copy first. "
            "The lesson reads the two patterns as tools with opposite costs and counts what "
            "each touches on the staff hierarchy of the last lesson."
        ),
        "body": [
            ("p", "&ldquo;You need to touch multiple tables to load an object, which means a "
                  "join or multiple queries and sewing in memory.&rdquo; That is the first "
                  "weakness Chapter 12 lists for Class Table Inheritance, and the lesson reads "
                  "it against its opposite, Concrete Table Inheritance, and the structure "
                  "both share, Inheritance Mappers. Read the three patterns in your own copy "
                  "first."),
            ("p", "Class Table Inheritance gives every class a table of the fields it "
                  "declares. Its strengths, as the pattern lists them, are that no row "
                  "carries a column it does not use, so nothing is wasted, and that classes "
                  "and tables correspond one to one, which makes the mapping easy to follow. "
                  "The rows of one object can share one key value across the tables, or each "
                  "table can have its own key and a foreign key into the superclass table. "
                  "The cost is the quotation: loading an object reads several tables, and a "
                  "join across more than three or four of them is slow on most databases. "
                  "Worse, a query for a group of "
                  "objects of mixed classes does not know which tables to join, so it needs "
                  "outer joins or a first read of the root table followed by more queries. "
                  "Moving a field up or down the hierarchy changes the database, and the "
                  "superclass tables, read on every access, can become a bottleneck."),
            ("p", "Concrete Table Inheritance makes the opposite trade. Each concrete class "
                  "gets one self-contained table with all its fields, so loading an object "
                  "of a known class reads one table, and each table is touched only when its "
                  "class is. But superclass fields are duplicated across the tables, so a "
                  "superclass change alters every table that holds the field, and a find on "
                  "the superclass must look in all of them. Keys must be unique across the "
                  "tables, not just within each, or one key could name two rows; and the "
                  "database cannot enforce a reference to the abstract class, because it has "
                  "no table."),
            ("p", "Inheritance Mappers is the structure behind all three. Each domain class "
                  "has a mapper that loads and saves its own fields and calls its superclass's "
                  "mapper for the rest, and a mapper for the abstract class works out which "
                  "concrete mapper should handle a request and delegates to it. Fowler finds "
                  "it hard to think of a good alternative; duplicating the superclass's "
                  "mapping code in every concrete mapper is, in his phrase, &ldquo;a heinous "
                  "crime&rdquo;. And Chapter 3 reminds you that the three mappings can be "
                  "mixed in one hierarchy, at the cost of more complexity."),
            ("p", "Here is the query a class-table load needs, written for this lesson. A "
                  "manager's name is in `person`, its salary in `employee` and its reports in "
                  "`manager`, so the `SELECT` on line 3 names a column from each, and lines 5 "
                  "and 6 `JOIN` the three tables on the shared key. Under concrete table the "
                  "same object would be one row of one table."),
            ("code", _lines(CLASS_TABLE_FIND)),
            ("p", "Now the count, on the last lesson's staff hierarchy, single table, class "
                  "table, concrete table in each tile. In <code>staff-find-person</code> the "
                  "lab loads a manager: `1, 3, 1` tables, a class-table load joining person, "
                  "employee and manager. Finding every person, subclasses included, reads "
                  "`1, 4, 3`: under class table the find joins the class's ancestors and "
                  "unions its descendants, here all four tables, and under concrete table it "
                  "unions the concrete tables below person, employee, manager and contractor. "
                  "Adding a field to person alters `1, 1, 3`: one table for single and class "
                  "table, all three concrete tables."),
            ("p", "The preset <code>staff-find-employee</code> moves down the hierarchy. "
                  "Loading a contractor touches `1, 2, 1`, person and contractor under class "
                  "table. Finding every employee reads `1, 3, 2`: class table joins person "
                  "above and unions manager below, and concrete table unions employee and "
                  "manager. Adding a field to employee alters `1, 1, 2`. The lower the class, "
                  "the more a class-table load joins and the fewer tables a concrete-table "
                  "change or find touches."),
            ("p", "Read the two patterns against those figures. Class Table Inheritance pays "
                  "on every load, more the deeper the class, and never alters more than one "
                  "table to add a field. Concrete Table Inheritance pays nothing to load a "
                  "class it knows, and pays in every concrete table below the class it finds "
                  "or alters. Which costs more depends on whether the system mostly loads "
                  "objects it can name or mostly searches and changes the hierarchy, and the "
                  "count does not know that."),
            ("h3", "Exercise"),
            ("p", "A bank's hierarchy has the records `account, -, 3, no; saving, account, 2, "
                  "no; isa, saving, 1, yes; bond, saving, 2, yes; current, account, 2, yes`: "
                  "a saving account is abstract, with two concrete kinds below it. You load a "
                  "`bond`, find every saving account and add a field to saving. By hand, give "
                  "the tables each touches under the three mappings, then check them in the "
                  "lab."),
            ("p", "Every mapping so far has been written by hand. The next lesson, Metadata "
                  "Mapping, Query Object and Repository, reads Chapter 13's way of holding "
                  "the mapping as data instead."),
        ],
        "lab": ("eakit", {
            "mode": "inherit",
            "view": "tables",
            "preset": "staff-find-person",
            "classes": _STAFF,
            "presets": [
                {"id": "staff-find-person",
                 "label": "Staff: load a manager, find every person, add a field to person",
                 "load": "manager", "find": "person", "alter": "person",
                 "expect": {"ihLoad": "1, 3, 1", "ihFind": "1, 4, 3",
                            "ihAlter": "1, 1, 3"}},
                {"id": "staff-find-employee",
                 "label": "Staff: load a contractor, find employees, add a field to employee",
                 "load": "contractor", "find": "employee", "alter": "employee",
                 "expect": {"ihLoad": "1, 2, 1", "ihFind": "1, 3, 2",
                            "ihAlter": "1, 1, 2"}},
            ],
            "panel_title": "What loading, finding and altering touch",
            "panel_intro": (
                "Each record is a class, its parent, the fields it declares itself, and whether "
                "it is concrete. Every three-part tile is single table, class table, concrete "
                "table, in that order. A class-table find joins the class's ancestors and "
                "unions its descendants; a concrete-table find unions the concrete tables "
                "below it. The hierarchies are the lesson's, and illustrative."
            ),
        }),
        "steps_title": "Counting the tables an operation touches",
        "steps_intro": "Four steps, the last of them on a hierarchy of your own.",
        "steps": [
            ("Count a load",
             "Under class table, a load reads the class and each of its ancestors. Under "
             "single and concrete table it reads one table."),
            ("Count a find",
             "Under class table, a find of a class reads its ancestors and every class below "
             "it. Under concrete table it reads each concrete class at or below it. Single "
             "table reads one."),
            ("Count an alteration",
             "Adding a field alters one table under single and class table. Under concrete "
             "table it alters every concrete class at or below the class changed."),
            ("Do it on a hierarchy of your own",
             "Take the hierarchy from the last lesson's final step, and count the tables a "
             "query for every instance of its root touches under each of the three "
             "mappings. Write the three numbers down."),
        ],
        "worked": {
            "title": "A manager, three ways",
            "intro": [
                "Take the preset staff-find-person and follow one manager through each mapping.",
            ],
            "lines": [
                "single: one row of the one table",
                "class: person + employee + manager rows,",
                "  3 tables joined on one key",
                "concrete: one row of the manager table",
                "manager table: key + 3 + 2 + 2, so 8",
            ],
            "after": [
                "The concrete manager table repeats person's 3 columns and employee's 2, "
                "which is why adding a field to person alters all 3 concrete tables.",
            ],
        },
        "quiz_title": "Loads, finds and alterations",
        "quiz": [
            {"q": "The exercise's hierarchy: `account, -, 3, no; saving, account, 2, no; isa, "
                  "saving, 1, yes; bond, saving, 2, yes; current, account, 2, yes`. Load a "
                  "`bond`, find every saving account, add a field to saving. What are the "
                  "three tiles, single, class, concrete?",
             "a": ["Load 1, 3, 1; find 1, 3, 2; alter 1, 1, 2",
                   "Load 1, 3, 1; find 1, 4, 3; alter 1, 1, 3",
                   "Load 1, 2, 1; find 1, 4, 2; alter 1, 1, 2",
                   "Load 1, 3, 1; find 1, 4, 2; alter 1, 1, 2"],
             "c": 3,
             "why": "A bond's chain is bond, saving and account: 3 tables to load under class "
                    "table. Finding every saving account joins account above and unions isa "
                    "and bond below, account, saving, isa and bond, 4 tables; under concrete "
                    "table it unions the isa and bond tables, 2, because saving is abstract "
                    "and has no concrete table. Adding a field to saving alters those same 2 "
                    "concrete tables, and one table otherwise. Leaving out the join up to "
                    "account gives 3 for the find; treating saving as concrete gives 3 "
                    "concrete tables; forgetting account in the chain gives a load of 2."},
            {"q": "Under Class Table Inheritance, how many tables does loading one contractor "
                  "touch in the staff hierarchy, against one manager?",
             "a": ["2 against 3",
                   "4 against 4",
                   "1 against 1",
                   "3 against 3"],
             "c": 0,
             "why": "A class-table load joins the class and its ancestors. A contractor's "
                    "chain is contractor and person, 2 tables; a manager's is manager, "
                    "employee and person, 3. The hierarchy's four tables are what a find on "
                    "person reads, not what a load reads."},
            {"q": "Which weakness does Chapter 12 give Concrete Table Inheritance and not "
                  "Class Table Inheritance?",
             "a": ["Loading one object needs a join",
                   "Some columns are irrelevant to some rows",
                   "A superclass field change alters every table that has the field",
                   "The superclass tables are read on every access and can become a "
                   "bottleneck"],
             "c": 2,
             "why": "Superclass fields are duplicated across the concrete tables, so changing "
                    "one means changing each table. Joins to load and busy supertype tables "
                    "are Class Table Inheritance's weaknesses, and columns irrelevant to a "
                    "row are the single table's; a concrete table has no supertype table and "
                    "no irrelevant columns."},
            {"q": "In the lesson's `FIND_MANAGER`, which lines join the tables, and on what?",
             "a": ["Lines 3 and 4, on the name the tables share",
                   "Lines 5 and 6, each on the key `id` the rows share",
                   "Line 7 alone, on `p.id` in its WHERE clause",
                   "Lines 5 and 6, on a type code in the root table"],
             "c": 1,
             "why": "Line 5 joins `employee` and line 6 joins `manager`, each `ON` its id "
                    "equal to the person's id: the rows of one object share a key. Line 7's "
                    "`WHERE` picks the manager. This query needs no type code because it "
                    "already knows the class; a query for people of mixed classes might read "
                    "a code in the root table to choose its joins."},
        ],
        "mistakes": [
            ("Choosing Concrete Table Inheritance as the fast one",
             "On this view the mapping that loads from one table must be the best. It does "
             "load from one table, but a find on the superclass touches every concrete table, "
             "and altering the superclass alters all of them: on the lesson's illustration, "
             "<code>staff-find-person</code>, 3 tables each time. It also makes keys and "
             "references to the abstract class awkward. Chapter 3's trade-off between "
             "duplication and speed is still a trade-off."),
            ("Expecting every load to join every table",
             "Class Table Inheritance can sound as if every load joins every table. It joins "
             "one table per class in the loaded object's chain: a contractor touches 2 tables, "
             "a manager 3. The whole hierarchy is read only by a find on the root, which must "
             "also cover every class below it."),
            ("Copying the superclass's mapping into each mapper",
             "With one table per concrete class, it is tempting to write each mapper whole, "
             "superclass fields included. Inheritance Mappers' answer is a mapper per class "
             "that maps its own fields and calls its superclass's mapper for the rest; Fowler "
             "calls the duplication a heinous crime, and it is the code-level twin of the "
             "duplicated columns."),
        ],
        "standard": (
            "Finish when you can count the tables each operation touches under each mapping.",
            "Given a hierarchy, a class to load, a class to find all instances of and a class "
            "to alter, state the tables each touches under each of the three mappings."
        ),
        "note": (
            "The lab counts tables touched, not the cost of a join or a union, which depends "
            "on the rows and the database. It also cannot show the concrete-table problems "
            "that are about keys rather than tables: keeping keys unique across tables and "
            "referring to an abstract class that has no table."
        ),
    },
    # ---------------------------------------------------------------- 08
    # Chapter 3, Using Metadata (PDF p. 60 of the operator's copy). Chapter 13:
    # Metadata Mapping (PDF pp. 280-288; code generation and reflection p.
    # 280, Fowler preferring generation p. 281, the 90 percent warning p. 281,
    # When to Use It pp. 281-282); Query Object (pp. 289-293; When to Use It
    # p. 290); Repository, by Edward Hieatt and Rob Mee (pp. 294-298).
    # Quote: PDF p. 60, 25 words, ea_quotes.py OK. Lesson total: 25 words.
    # F15, PDF p. 281 of the operator's copy: a simple metadata scheme works
    # well 90 percent of the time (paraphrased, not quoted).
    {
        "slug": "metadata-query-object-repository",
        "title": "Metadata Mapping, Query Object and Repository",
        "module": "Chapter 13 · Object-Relational Metadata Mapping Patterns",
        "one_line": "Hand-written mapping is simple and repetitive; hold the mapping as data, read by one finder, and build queries and collections on top of it.",
        "summary": (
            "Chapter 3's Using Metadata says that hand-written mapping is simple and "
            "repetitive, and that repetitive code is a sign of a design problem. Chapter 13's "
            "Metadata Mapping holds the mapping as data; Query Object and Repository, the "
            "latter by Edward Hieatt and Rob Mee, build on it. Find the lines two hand-written "
            "finders repeat, and write the metadata a single finder would read instead."
        ),
        "key": [
            "hand mapping: simple and repetitive",
            "metadata: each column and its field",
            "one generic finder reads the metadata",
            "generated code, or reflection",
            "simple metadata covers most cases",
            "repository: a collection of objects",
        ],
        "key_label": "Mapping by metadata in six lines",
        "concepts_intro": (
            "Three patterns from Chapter 13 carry the lesson, each built on the one before."
        ),
        "concepts": [
            ("Metadata Mapping",
             "The details of the object-relational mapping held as data, such as which column "
             "fills which field, and processed by generic code: either a generator that writes "
             "the mapping classes at build time, or a reflective routine that reads the data "
             "as it runs."),
            ("Query Object",
             "A query built as an object from criteria in terms of classes and fields, which "
             "turns itself into SQL. It needs metadata to translate fields into columns, and "
             "Fowler says most projects with a hand-built data source layer do without one."),
            ("Repository",
             "Edward Hieatt and Rob Mee's pattern in Fowler's book: an interface that looks "
             "like a collection of domain objects. Domain code asks it for the objects that "
             "match some criteria, and the queries and mapping sit behind it."),
        ],
        "read_title": "The chapter's diagnosis first, then the three patterns",
        "read_intro": (
            "Read Using Metadata in Chapter 3, then Metadata Mapping, Query Object and "
            "Repository in Chapter 13, in your own copy first. The lesson reads the "
            "diagnosis as an argument and the patterns as tools, and counts the repetition "
            "in two hand-written finders."
        ),
        "body": [
            ("p", "&ldquo;With simple and repetitive mapping this can lead to code that's "
                  "simple and repetitive—and repetitive code is a sign of something wrong "
                  "with the design.&rdquo; Chapter 3's Using Metadata says it of the book's "
                  "own hand-written examples, and this lesson reads it with Chapter 13's "
                  "three patterns: Metadata Mapping, Query Object and Repository. Read the "
                  "section and the patterns in your own copy first."),
            ("p", "You have probably written the same finder twice: prepare a statement, "
                  "bind the key, run it, step to the row, make the object, copy each column "
                  "into a field, return it. Chapter 3's diagnosis is that the repetition is a "
                  "design problem. Some of it can be factored out with inheritance and "
                  "delegation, honest object-oriented practice; the more sophisticated answer "
                  "is to boil the mapping down to metadata, a statement of which column maps "
                  "to which field, and let code generation or reflection do the rest. That, "
                  "Fowler notes, is why commercial mapping tools use metadata, and why the "
                  "book still teaches the hand-written versions first: they are easier to "
                  "understand."),
            ("p", "Metadata Mapping's first decision is how the metadata becomes running "
                  "code. A generator reads it and writes mapper classes during the build, "
                  "classes nobody edits by hand; a reflective program reads field names from "
                  "the metadata and sets the fields as it runs. Fowler usually counsels "
                  "against reflection, as slow and hard to debug, but finds it quite "
                  "appropriate here, and the slowness small beside the database call it sits "
                  "in. Even so, generated code is easier to follow in a debugger, so he "
                  "usually prefers generation, which he says makes him unsophisticated."),
            ("p", "Its warning is about the cases left over. By the pattern's rough guide, "
                  "plain metadata covers about 90 percent of a mapping, and the odd cases "
                  "that remain can make the generic code much harder to follow. For those, "
                  "Fowler suggests hand-written subclasses that take over from it. "
                  "Metadata can also interfere with refactoring, since a field renamed in the "
                  "code is still named in the data. And a good Layer Supertype, Fowler adds, "
                  "can reduce hand-coding a long way before metadata is needed at all."),
            ("p", "Query Object and Repository build on the metadata. A Query Object is an "
                  "interpreter of criteria written in terms of classes and fields, which can "
                  "turn itself into SQL; it needs the metadata to know which column a field "
                  "is. Its own When to Use It is cautious: most projects with a hand-built "
                  "data source layer do without one, it is really needed only with a Domain "
                  "Model and a Data Mapper, and serious use needs Metadata Mapping as well. "
                  "That is why the lab does not count one. Repository, Edward Hieatt and Rob "
                  "Mee's pattern, sits above the mappers and looks like a collection of "
                  "domain objects: the client builds criteria and asks for the matching "
                  "objects, never for a query to be run."),
            ("p", "Now the count. Here are two hand-written finders, written for this lesson. "
                  "Each prepares its statement, binds the key, executes, steps to the row, "
                  "builds its object and copies two columns into fields."),
            ("code", _lines(HAND_MAPPING)),
            ("p", "The lab finds repeated runs of identical lines, two or more long, and "
                  "prints three tiles: the repeated blocks, the lines in all the copies, and "
                  "where they are. In <code>hand-mapping</code> it finds 1 block of 6 lines, "
                  "`lines 3–5 and lines 13–15`: the bind, the execute and the `next`, three "
                  "lines twice. The prepare on lines 2 and 12 names different statements, and "
                  "the field copies on lines 7, 8, 17 and 18 differ in their names, so the "
                  "kit does not count them. They repeat in shape, and that shape is exactly "
                  "what the metadata holds: the repetition the pattern removes is wider than "
                  "the count."),
            ("p", "In <code>metadata-find</code> the mapping is data. `MEMBER_MAP` on lines 2 "
                  "and 3 pairs each column with the field it fills, and one generic `find` "
                  "prepares, binds and runs the statement once (lines 8 to 11), makes the "
                  "object by reflection (line 12), and copies each mapped column into its "
                  "field (lines 13 to 16). The lab finds 0 repeated blocks, 0 lines, `none`. "
                  "A shop needs only its own map and its own statement."),
            ("code", _lines(METADATA_FIND)),
            ("h3", "Exercise"),
            ("code", _lines(INVOICE_FINDERS)),
            ("p", "Mark by hand the lines these two finders repeat exactly, by their line "
                  "numbers. Then write the metadata, column and field pairs, that the single "
                  "metadata finder would read for each class. You can paste the listing into "
                  "the lab to check the first part."),
            ("p", "That ends the book's object-relational patterns, Chapters 10 to 13. "
                  "The next course, Web "
                  "Presentation, puts a front on the system these patterns have mapped to its "
                  "tables, beginning with Model View Controller."),
        ],
        "lab": ("cckit", {
            "mode": "code",
            "view": "dupes",
            "min_run": 2,
            "preset": "hand-mapping",
            "presets": [
                {"id": "hand-mapping",
                 "label": "Hand mapping: a member and a shop, each found by its own code",
                 "code": HAND_MAPPING,
                 "expect": {"coDupBlocks": "1", "coDupLines": "6",
                            "coDupWhere": "lines 3–5 and lines 13–15"}},
                {"id": "metadata-find",
                 "label": "Metadata: one finder that reads a map of columns and fields",
                 "code": METADATA_FIND,
                 "expect": {"coDupBlocks": "0", "coDupLines": "0",
                            "coDupWhere": "none"}},
            ],
            "panel_title": "The repetition a metadata mapping removes",
            "panel_intro": (
                "The lab finds runs of two or more identical lines, after collapsing white "
                "space, and counts the copies. Lines that repeat in shape with different "
                "names are not counted. The listings are the lesson's."
            ),
        }),
        "steps_title": "Finding the mapping that repeats",
        "steps_intro": "Four steps, the last of them on code of your own.",
        "steps": [
            ("Mark the identical lines",
             "Read the finders side by side and mark each run of two or more lines that is "
             "the same in both, character for character apart from spacing."),
            ("Mark the lines that repeat in shape",
             "Mark the lines that do the same thing with different names: the statement each "
             "prepares, the object each builds, the columns each copies."),
            ("Write the metadata",
             "For each class, list each column it reads with the field it fills. Those pairs, "
             "with the statement, are all a single metadata finder needs."),
            ("Do it on finders of your own",
             "Take the finders of one class in a system you know, count them, and count the "
             "lines each shares with the others exactly and in shape. Write both numbers."),
        ],
        "worked": {
            "title": "Two hand-written finders",
            "intro": [
                "Take the preset hand-mapping and compare the two finders line by line.",
            ],
            "lines": [
                "lines 1 and 11: different names",
                "lines 2 and 12: different statements",
                "lines 3 to 5 and 13 to 15: identical",
                "lines 6 to 8 and 16 to 18: shape only",
                "lab: 1 block, 6 lines",
            ],
            "after": [
                "Six identical lines is the kit's count. The two finders share far more in "
                "shape, and the metadata finder removes both kinds at once, because what "
                "differs between them is exactly what the map holds.",
            ],
        },
        "quiz_title": "Repetition, metadata and the chapter's claims",
        "quiz": [
            {"q": "In the exercise's listing, which lines repeat exactly, and what metadata "
                  "would a single finder read?",
             "a": ["Lines 3–5 and 13–15; total and due for the invoice, paid for the "
                   "receipt",
                   "Lines 2–5 and 13–16; total, due and paid for each of the two",
                   "Lines 3–5 and 14–16; total and due for the invoice, paid for the "
                   "receipt",
                   "Lines 3–9 and 14–19; total and due for the invoice, paid for the "
                   "receipt"],
             "c": 2,
             "why": "Line 11 is blank, so the receipt's finder starts at line 12, and the "
                    "bind, execute and `next` are lines 3 to 5 and 14 to 16: 1 block, 6 lines. "
                    "Lines 2 and 13 prepare different statements. The metadata is "
                    "`{\"total\", \"total\"}, {\"due\", \"due\"}` for the invoice and "
                    "`{\"paid\", \"paid\"}` for the receipt, and both finders become calls to "
                    "the one metadata finder."},
            {"q": "How often, by Metadata Mapping's own warning, does a simple metadata scheme "
                  "work well?",
             "a": ["Always, once the metadata covers every field of every class",
                   "About half the time, the rest needing code written by hand",
                   "Only with code generation, never when it is read by reflection",
                   "About 90 percent of the time, with the rest adding much complexity"],
             "c": 3,
             "why": "The pattern's guide is that plain metadata handles about nine cases in "
                    "ten, and that the rest can make the generic code much more complex; for "
                    "those it suggests hand-written subclasses in its place. The figure is a "
                    "rough guide, not a measurement."},
            {"q": "By Query Object's When to Use It, when do you really need one?",
             "a": ["In any project that builds its own data source layer by hand",
                   "With a Domain Model and a Data Mapper, and Metadata Mapping for "
                   "serious use",
                   "Whenever the developers on the project do not know SQL well",
                   "With a Table Module and a Record Set, for queries built at run time"],
             "c": 1,
             "why": "Fowler says most projects with a hand-built data source layer do without "
                    "one, that you only really need it with a Domain Model and a Data Mapper, "
                    "and that serious use needs Metadata Mapping. Even then many developers "
                    "are comfortable with SQL, and most people who use one get it from a tool."},
            {"q": "What does a Repository offer domain code, in Hieatt and Mee's pattern?",
             "a": ["A collection-like interface: ask for the objects matching some "
                   "criteria",
                   "A mapper class for each table, renamed and moved to the domain",
                   "A cache of loaded objects shared between every session",
                   "The SQL for each of its queries, written by hand by the caller"],
             "c": 0,
             "why": "A Repository mediates between the domain and the mapping layers and acts "
                    "like an in-memory collection of domain objects; the client builds criteria "
                    "and asks for the matches, and the queries and mapping sit behind it. It "
                    "sits above the mappers rather than replacing one."},
        ],
        "mistakes": [
            ("Thinking metadata mapping removes the mapping work",
             "On this view, once the mapping is data the work is gone. It moves: into the "
             "metadata, and into the generic code that reads it, which must handle every "
             "case. Metadata Mapping's own warning is that plain metadata covers about 90 "
             "percent of a mapping, and the remainder can tangle it; Fowler's advice is "
             "hand-written overrides for the special cases, and he notes the setup work and "
             "the trouble metadata makes for refactoring."),
            ("Taking a Repository for a Data Mapper renamed",
             "Both sit between the domain and the database, so they can look alike. A "
             "Repository sits above the mappers and offers a collection, so that domain code "
             "asks for objects by criteria without knowing about queries; it combines "
             "Metadata Mapping with a Query Object underneath, and its source need not be a "
             "database at all."),
            ("Trusting the duplicate count as the whole repetition",
             "The lab finds 6 identical lines in two finders that are alike almost "
             "throughout. Lines that do the same thing with different names, the field "
             "copies above all, are not counted; they are the repetition the metadata holds. "
             "A low count of identical lines does not mean the mapping is not repetitive."),
        ],
        "standard": (
            "Finish when you can mark a pair of finders' repetition and write its metadata.",
            "Given two hand-written finders for two classes, mark the lines they repeat, and "
            "write the metadata, column and field, that a single finder would read."
        ),
        "note": (
            "The lab finds identical lines only, so it understates repetition that differs "
            "by a name, which is most of what a metadata mapping removes. It cannot weigh "
            "what the metadata costs in setup, special cases and refactoring, and it does not "
            "count Query Object or Repository at all. Of Query Object, Fowler says most "
            "hand-built data source layers do without one and that buying a tool is almost "
            "always better; Repository, Hieatt and Mee's, is worth most in a large system "
            "with many queries or more than one data source."
        ),
    },
]
