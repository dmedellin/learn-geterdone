"""Talking to the Database, lessons 1-6 -- Chapter 3's first half and Chapter 10.

Fowler et al., Patterns of Enterprise Application Architecture (Addison-Wesley,
2002): Chapter 3, Mapping to Relational Databases (Architectural Patterns,
Reading in Data, Building the Mapping, Database Connections, Some
Miscellaneous Points); Chapter 10, Data Source Architectural Patterns; and
Chapter 18's Gateway, Mapper and Registry. The book is cited by chapter,
section and pattern; the PDF page of the operator's copy is in the comment
beside each lesson. Every quotation was checked with ea_quotes.py, and every
figure attributed to the book carries its PLAN section S.2 id. The code is
written for these lessons and none of the book's listings is reproduced. Each
snippet is one constant below, copied from docs/enterprise-patterns/presets.py,
used by the lesson's code block and, for a cckit code lab, by its preset.
"""


def _lines(text):
    """A snippet constant as a code block's list of lines."""
    return text.split("\n")


# ---------------------------------------------------------------- snippets

PRICE_GATEWAY = """// All the SQL for the price table, in one class.
class PriceGateway {
    private final Connection db;

    PriceGateway(Connection db) {
        this.db = db;
    }

    long findCents(String sku) throws SQLException {
        PreparedStatement s = db.prepareStatement(
            "SELECT cents FROM price WHERE sku = ?");
        s.setString(1, sku);
        ResultSet rs = s.executeQuery();
        return rs.next() ? rs.getLong(1) : -1;
    }
}"""

ORDER_ROW = """// A gateway for one row of the orders table, and its finder.
class OrderRow {
    final long id;
    String status;

    OrderRow(long id, String status) {
        this.id = id;
        this.status = status;
    }

    static OrderRow find(Connection db, long id) throws SQLException {
        PreparedStatement s = db.prepareStatement(
            "SELECT status FROM orders WHERE id = ?");
        s.setLong(1, id);
        ResultSet rs = s.executeQuery();
        return rs.next() ? new OrderRow(id, rs.getString(1)) : null;
    }
}"""

ACCOUNT_RECORD = """// An Active Record: a row's data, its SQL and its domain logic.
class Account {
    private long id;
    private long balance;
    private long overdraft;

    static Account find(Connection db, long id) throws SQLException {
        // SELECT balance, overdraft FROM account WHERE id = ?
        return new Account();
    }

    void update(Connection db) throws SQLException {
        // UPDATE account SET balance = ? WHERE id = ?
    }

    public boolean canWithdraw(long cents) {
        return balance + overdraft >= cents;
    }
}"""

ACCOUNT_ROW = """// A Row Data Gateway: the same row, with no domain logic.
class AccountRow {
    private long id;
    private long balance;
    private long overdraft;

    static AccountRow find(Connection db, long id) throws SQLException {
        // SELECT balance, overdraft FROM account WHERE id = ?
        return new AccountRow();
    }

    void update(Connection db) throws SQLException {
        // UPDATE account SET balance = ? WHERE id = ?
    }
}"""

MEMBER_RECORD = """class Member {
    private long id;
    public String email;
    private int points;
    public final String joined = "2024-01-01";

    static Member find(Connection db, long id) throws SQLException {
        return new Member();
    }

    public void insert(Connection db) throws SQLException {
        // INSERT INTO member (email, points) VALUES (?, ?)
    }

    public int level() {
        return points / 1000;
    }
}"""

ACCOUNT_MAPPER = """// The mapper knows the table and the class; Account knows neither.
class AccountMapper {
    private final Connection db;

    AccountMapper(Connection db) {
        this.db = db;
    }

    Account find(long id) throws SQLException {
        PreparedStatement s = db.prepareStatement(
            "SELECT balance, overdraft FROM account WHERE id = ?");
        s.setLong(1, id);
        ResultSet rs = s.executeQuery();
        rs.next();
        return new Account(id, rs.getLong(1), rs.getLong(2));
    }
}"""

TWO_SOURCES = """// The same customer arrives from a table and from a message.
Customer fromRow(ResultSet rs) throws SQLException {
    String name = rs.getString("name");
    String postcode = rs.getString("postcode");
    long limit = rs.getLong("credit_limit");
    Customer c = new Customer(name.trim(), postcode.toUpperCase());
    c.setCreditLimit(limit);
    return c;
}

Customer fromMessage(Element msg) {
    String name = msg.getAttribute("name");
    String postcode = msg.getAttribute("post_code");
    long limit = Long.parseLong(msg.getAttribute("limit"));
    Customer c = new Customer(name.trim(), postcode.toUpperCase());
    c.setCreditLimit(limit);
    return c;
}"""

TWO_STEP = """// Step one, per source, holds the differences: to a logical record.
CustomerData fromRow(ResultSet rs) throws SQLException {
    return new CustomerData(rs.getString("name"),
        rs.getString("postcode"), rs.getLong("credit_limit"));
}

CustomerData fromMessage(Element msg) {
    return new CustomerData(msg.getAttribute("name"),
        msg.getAttribute("post_code"),
        Long.parseLong(msg.getAttribute("limit")));
}

// Step two, once, holds what they share: the record to the object.
Customer toCustomer(CustomerData d) {
    Customer c = new Customer(d.name.trim(), d.postcode.toUpperCase());
    c.setCreditLimit(d.limit);
    return c;
}"""

SHIPMENT_TWICE = """void toTable(Shipment s, PreparedStatement st) throws SQLException {
    String ref = s.ref().toUpperCase();
    long grams = Math.round(s.kilos() * 1000);
    String to = s.postcode().replace(" ", "");
    st.setString(1, ref);
    st.setLong(2, grams);
    st.setString(3, to);
    st.executeUpdate();
}

void toMessage(Shipment s, Element msg) {
    String ref = s.ref().toUpperCase();
    long grams = Math.round(s.kilos() * 1000);
    String to = s.postcode().replace(" ", "");
    msg.setAttribute("ref", ref);
    msg.setAttribute("grams", Long.toString(grams));
    msg.setAttribute("to", to);
}"""

SAVE_LINES_BATCH = """// Sends every line of an order to the database in one call.
void saveLines(Connection db, long orderId, List<Line> lines)
        throws SQLException {
    PreparedStatement s = db.prepareStatement(
        "INSERT INTO line (order_id, sku, qty) VALUES (?, ?, ?)");
    for (Line line : lines) {
        s.setLong(1, orderId);
        s.setString(2, line.sku());
        s.setInt(3, line.qty());
        s.addBatch();
    }
    s.executeBatch();
}"""



LESSONS = [
    # ---------------------------------------------------------------- 01
    # Chapter 3, Architectural Patterns: PDF pp. 46-49 of the operator's copy.
    # Chapter 18, Gateway: PDF pp. 413-417. Chapter 10, Table Data Gateway:
    # PDF pp. 141-147 (the Alur et al. note, p. 142). Mapper is named, p. 418.
    # Quote: PDF p. 46, 23 words, ea_quotes.py OK. Lesson total: 23 words.
    # F10, PDF p. 49 of the operator's copy: mapping to a relational database
    # around a third of programming effort, by anecdotal observation.
    {
        "slug": "gateways",
        "title": "Gateways",
        "module": "Chapter 10 · Data Source Architectural Patterns",
        "one_line": "Put all the SQL for a table in one class, a gateway, so the rest of the application knows nothing about SQL and a schema change is edited in one place.",
        "summary": (
            "Chapter 3 opens its architectural patterns with the case for taking SQL out of "
            "the domain logic and putting it in a Gateway, one class per table. Read that "
            "case with Chapter 18's Gateway and Chapter 10's Table Data Gateway, then count "
            "the classes a column rename is edited in when four classes hold SQL against a "
            "table, and when one gateway does."
        ),
        "key": [
            "keep SQL out of the domain logic",
            "a gateway wraps an awkward resource",
            "table data gateway: an object a table",
            "a rename is edited where the SQL is",
            "direct dependents: the classes to edit",
            "reached in all: an upper bound",
        ],
        "key_label": "Architectural Patterns and Gateway in six lines",
        "concepts_intro": (
            "Three terms carry the lesson. The first is a base pattern the rest of the "
            "course builds on."
        ),
        "concepts": [
            ("Gateway",
             "An object that wraps access to something outside the program, such as a "
             "database table, behind an interface that looks like an ordinary object's. "
             "Chapter 18 says to keep it as small as it can be: it adapts the resource and "
             "gives a place to substitute a stand-in for tests."),
            ("Table Data Gateway",
             "A gateway with one instance for a whole table: it holds every SELECT, INSERT, "
             "UPDATE and DELETE for that table, and other code calls its methods for all "
             "access to it. It is usually stateless, pushing data back and forth."),
            ("Record Set",
             "A generic in-memory structure of tables and rows that mimics the database's "
             "own shape. Many environments of the time provided one, and user-interface "
             "controls worked with it directly; a Table Data Gateway's finders can return "
             "one."),
        ],
        "read_title": "The narrative's case, the pattern, then the count",
        "read_intro": (
            "Read Chapter 3, Architectural Patterns, then Chapter 18, Gateway, and Chapter "
            "10, Table Data Gateway, in your own copy first. The lesson sets out the "
            "narrative's argument, reads the two patterns as tools, and counts where a "
            "schema change is edited in two versions of one small design."
        ),
        "body": [
            ("p", "&ldquo;The rest of the application needs to know nothing about SQL, and "
                  "all the SQL that accesses the database is easy to find.&rdquo; That "
                  "sentence, from Chapter 3's section Architectural Patterns, is the promise "
                  "of every pattern in this course. This lesson reads that section as an "
                  "argument, and then Chapter 18's Gateway and Chapter 10's Table Data "
                  "Gateway as tools. Read them in your own copy first."),
            ("p", "Fowler's case begins with SQL itself. It is everywhere in enterprise "
                  "software, he says, and still a trap: many application developers do not "
                  "know it well and write poor queries; every way of embedding it in a "
                  "programming language is somewhat awkward; and database administrators "
                  "want to find the SQL that touches a table, so as to tune it and arrange "
                  "its indexes. So separate the SQL from the domain logic and put it in "
                  "classes of its own, one for each table, each a Gateway to its table. He "
                  "adds that he does this even in small scripts of his own, because he finds "
                  "the separation that helpful."),
            ("p", "He then lays out the choice the rest of the course reads. A gateway can "
                  "have one instance per row, a Row Data Gateway, or one per table, a Table "
                  "Data Gateway, which returns a Record Set and is the obvious partner for "
                  "Table Module. A simple Domain Model whose classes match the tables can let "
                  "each object load and save itself, an Active Record; a rich one wants a "
                  "Data Mapper, a layer that keeps the objects and the tables apart. He calls "
                  "the choice far-reaching and hard to refactor, and strongly affected by how "
                  "you built the domain logic, which is why the previous course came first."),
            # F10, PDF p. 49 of the operator's copy.
            ("p", "The section closes on what all this costs. Weighing object databases, "
                  "which need no mapping, Fowler reports that anecdotal observations put "
                  "the effort of mapping to a relational database at around a third of "
                  "programming effort, a cost that goes on through maintenance. He says "
                  "himself that he knows of no controlled tests; it is a figure from "
                  "projects he has seen, not a measurement, and your own records can test "
                  "it."),
            ("p", "Gateway, in Chapter 18, is the general tool. Wrap the special API of an "
                  "external resource, JDBC and SQL for a database, in a class whose interface "
                  "looks like any other object's, and let everything else go through it. "
                  "Keep it minimal: adapt the resource, give tests a place to substitute a "
                  "stand-in, and leave any cleverer logic to its callers. Its chief benefit, "
                  "the pattern says, is that a change of resource alters only the gateway "
                  "and does not ripple through the rest of the system."),
            ("p", "Table Data Gateway, in Chapter 10, is that tool for one table: finds, "
                  "inserts, updates and deletes, each mapping its parameters into SQL. Its "
                  "trickiest question is what a query returns. A map works, but Fowler calls "
                  "it bad form, because it defeats compile-time checking; a Data Transfer "
                  "Object is better, at the cost of another class; the Record Set itself is "
                  "conceptually messy but very effective where tools are built around it; "
                  "and with a Domain Model the gateway can return domain objects, which he is "
                  "reluctant to do, because each side then depends on the other. The book "
                  "notes that Alur, Crupi and Malks's Data Access Object is this pattern "
                  "under another name."),
            ("p", "The lesson's snippet is a small Table Data Gateway for a `price` table. "
                  "In JDBC, `prepareStatement` compiles a SQL statement with a question "
                  "mark as its placeholder, `setString` fills the placeholder, and `executeQuery` runs "
                  "the statement and returns a `ResultSet`, whose `next` moves to the first "
                  "row if there is one. A caller asks for `findCents` and never sees a "
                  "column name."),
            ("code", _lines(PRICE_GATEWAY)),
            ("p", "Now the count. The lab reads a design as records `dependent, "
                  "dependency`, one for each class that uses another, and you name what "
                  "changes. Its first tile lists what depends on the changed name directly; "
                  "its second lists everything the change reaches by following the "
                  "dependencies back. In <code>sql-everywhere</code> four classes, `cart`, "
                  "`checkout`, `report` and `admin`, each hold their own SQL against "
                  "`price-table`. Change the table and the lab prints 4: admin, cart, "
                  "checkout, report for both tiles: a column rename is edited in four "
                  "classes, and found by searching for it."),
            ("p", "In <code>one-gateway</code> each of the four depends on `pricegateway` "
                  "instead, and only the gateway depends on the table. The direct tile "
                  "falls to 1: pricegateway, the one class a rename is edited in. The second "
                  "tile prints 5: admin, cart, checkout, pricegateway, report, and that "
                  "figure is an upper bound: it is what the change would reach if it got "
                  "past the gateway's interface, if `findCents` itself had to change. A "
                  "rename the gateway absorbs stops at the gateway, which is the "
                  "quotation's claim. Whether a given change is absorbed is the question the "
                  "count leaves to you."),
            ("h3", "Exercise"),
            ("ul", [
                "Four classes and a table: `signup, member-table; profile, member-table; "
                "mailer, member-table; profile, mailer`, with `member-table` the name that "
                "changes.",
                "The same classes redrawn so that each depends on a `membergateway`, which "
                "alone depends on `member-table`; `profile` still uses `mailer`.",
            ]),
            ("p", "For each design, list by hand the classes a column rename must be edited "
                  "in, and then what the change would reach if the gateway's interface had "
                  "to change too. Mind `profile`, which reaches the table two ways. Type "
                  "the records into the lab afterwards to check."),
            ("p", "Fowler's first gateway has one instance per table. The next lesson, Row "
                  "Data Gateway, and Reading in Data, reads the one with an instance per "
                  "row, and what Chapter 3 says about the finders that load it."),
        ],
        "lab": ("cckit", {
            "mode": "deps",
            "view": "ripple",
            "preset": "sql-everywhere",
            "presets": [
                {"id": "sql-everywhere",
                 "label": "SQL everywhere: four classes query the price table",
                 "edges": "cart, price-table; checkout, price-table; report, price-table; "
                          "admin, price-table",
                 "changed": "price-table",
                 "expect": {"dgDirect": "4: admin, cart, checkout, report"}},
                {"id": "one-gateway",
                 "label": "One gateway: the four classes go through pricegateway",
                 "edges": "cart, pricegateway; checkout, pricegateway; report, pricegateway; "
                          "admin, pricegateway; pricegateway, price-table",
                 "changed": "price-table",
                 "expect": {"dgDirect": "1: pricegateway"}},
            ],
            "panel_title": "Where a schema change is edited",
            "panel_intro": (
                "Each record is one dependency, written dependent, dependency. Name the "
                "class or table that changes. The first tile lists the classes that "
                "depend on it directly, the ones a column rename is edited in; the "
                "second lists everything the change reaches, an upper bound that holds "
                "only if the change gets past a gateway's interface. The designs are the "
                "lesson's."
            ),
        }),
        "steps_title": "Finding where a schema change is edited",
        "steps_intro": "Four steps, the last of them on a table of your own.",
        "steps": [
            ("Find the SQL",
             "Search the code for the table's name and list every class that holds SQL "
             "against it, whatever else the class does."),
            ("Write the dependencies",
             "Write one record for each, `class, table`, and one for each class that uses "
             "another. The classes that depend on the table directly are the ones a column "
             "rename is edited in."),
            ("Redraw it through a gateway",
             "Make every class depend on one gateway, and the gateway alone on the table. "
             "Count the direct dependents again, and note what the change would reach if "
             "the gateway's interface had to change."),
            ("Count it in a system you know",
             "Take one table in a system you know, search the code for its name, and count "
             "the files that hold SQL against it. Write the figure, and say in one sentence "
             "whether a single gateway holds all of them."),
        ],
        "worked": {
            "title": "Four classes, then one gateway",
            "intro": [
                "Count <code>sql-everywhere</code> and <code>one-gateway</code> for a column "
                "rename in the price table.",
            ],
            "lines": [
                "without: cart, checkout, report, admin",
                "each holds SQL against the price table",
                "a rename is edited in 4 classes",
                "with: each of the 4 uses pricegateway",
                "a rename is edited in pricegateway: 1",
                "if its interface changed: 5 reached",
            ],
            "after": [
                "The gateway is one more class, and it is the only one a rename touches. The "
                "five classes reached are what would follow if `findCents` had to change; a "
                "rename it absorbs never reaches them.",
            ],
        },
        "quiz_title": "Gateways, counted and read",
        "quiz": [
            {"q": "Take the exercise: `signup`, `profile` and `mailer` hold SQL against "
                  "`member-table`, and `profile` also uses `mailer`. How many classes must a "
                  "column rename be edited in without a gateway, and with `membergateway`?",
             "a": ["3 without (mailer, profile, signup); 1 with (membergateway)",
                   "2 without (mailer, signup); 1 with (membergateway)",
                   "3 without; 4 with (mailer, membergateway, profile, signup)",
                   "4 without, counting profile twice; 1 with"],
             "c": 0,
             "why": "Without the gateway three classes hold SQL against the table, so the "
                    "lab's direct tile prints 3: mailer, profile, signup, and its second tile "
                    "prints the same 3, since `profile` is reached directly as well as "
                    "through `mailer` and is counted once. With the gateway only "
                    "`membergateway` depends on the table: 1: membergateway. The second tile "
                    "then prints 4: mailer, membergateway, profile, signup, which is the "
                    "upper bound if the gateway's interface had to change, not the classes a "
                    "rename is edited in."},
            {"q": "Of the four things a Table Data Gateway's finder can return, which does "
                  "Chapter 10 call bad form?",
             "a": ["A map", "A Data Transfer Object", "A Record Set", "Domain objects"],
             "c": 0,
             "why": "A map, because it defeats compile-time checking and is not an explicit "
                    "interface, so a misspelt key becomes a bug. A Data Transfer Object is "
                    "another class but a better choice; a Record Set is conceptually messy "
                    "and very effective where tools use it; returning domain objects makes "
                    "each side depend on the other, which Fowler is reluctant to do but does "
                    "not call bad form."},
            {"q": "On <code>one-gateway</code> the lab's second tile prints 5: admin, cart, "
                  "checkout, pricegateway, report. What do those five classes count?",
             "a": ["The classes a column rename must be edited in",
                   "The classes holding SQL against the price table",
                   "Everything the change would reach if it got past the gateway's "
                   "interface",
                   "The classes plus the table itself"],
             "c": 2,
             "why": "The tile follows every dependency back from the changed table, as if "
                    "nothing absorbed the change. Only `pricegateway` holds SQL, so a rename "
                    "is edited there alone, which the first tile prints. The changed name "
                    "never appears in the list."},
            {"q": "Which of these is one of Architectural Patterns' reasons for taking SQL "
                  "out of the domain logic?",
             "a": ["Embedded SQL cannot use a connection pool",
                   "Database administrators want to find the SQL that accesses a table, to "
                   "tune it and arrange its indexes",
                   "SQL in a domain class cannot be precompiled",
                   "A relational database cannot be reached from a domain class"],
             "c": 1,
             "why": "The section gives three reasons: many application developers do not "
                    "know SQL well, every way of embedding it is somewhat awkward, and "
                    "database administrators want to find it. Pooling and precompiling "
                    "are discussed elsewhere in Chapter 3 and have nothing to do with where "
                    "the SQL is written."},
        ],
        "mistakes": [
            ("Thinking a gateway is one more class, so a schema change costs more",
             "A gateway does add a class, and on the lesson's illustration that class is the "
             "whole point: a column rename is edited in four classes without it and in one "
             "with it. The quotation's claim is not that the code gets smaller but that the "
             "SQL becomes easy to find and the rest of the application stops knowing it. "
             "The five classes the lab reaches through the gateway are reached only if its "
             "interface changes too."),
            ("Expecting a gateway to hide that there is a database",
             "That is Data Mapper's promise, not Gateway's. A Table Data Gateway that returns "
             "a Record Set hands its callers the table's own shape, and a Row Data Gateway "
             "mirrors one row field for field. A gateway hides the SQL and the API; the "
             "domain code still thinks in tables. Chapter 3 says that is too little "
             "indirection for a rich Domain Model, and does not recommend a gateway as a "
             "Domain Model's primary persistence."),
            ("Choosing the data-source pattern first",
             "Architectural Patterns says the choice is strongly affected by how you design "
             "the domain logic. Table Data Gateway is the obvious choice with a Table Module, "
             "a gateway of either kind suits a Transaction Script, and a Domain Model wants "
             "an Active Record or a Data Mapper. Picking the gateway before the domain "
             "pattern decides the harder question by accident."),
        ],
        "standard": (
            "Finish when you can say where a schema change is edited.",
            "Given classes that hold SQL against one table, list the classes a column rename "
            "must be edited in, then redraw them through a gateway and list them again, "
            "saying what the change would reach if the gateway's interface changed."
        ),
        "note": (
            "The lab follows the dependencies you state; it cannot find SQL in code, and it "
            "cannot tell whether a change stops at a gateway's interface, which is why its "
            "second tile is an upper bound. The figure of a third of programming effort is "
            "Fowler's report of anecdotal observation, as he says himself, not a measured "
            "rate."
        ),
    },
    # ---------------------------------------------------------------- 02
    # Chapter 10, Row Data Gateway: PDF pp. 148-153 of the operator's copy
    # (the finders, p. 148; the crux and code generation, p. 149; When to Use
    # It, pp. 149-150). Chapter 3, Reading in Data: PDF p. 52.
    # Quote: PDF p. 52, 18 words, ea_quotes.py OK. Lesson total: 18 words.
    # F11, PDF p. 52 of the operator's copy: one query that brings back
    # unnecessary rows over 50 individual ones (50 wanted of 200); joins up
    # to three or four a query. The latency, row time and batch size are
    # illustrative, and the batched strategy is the lab's, not the book's.
    {
        "slug": "row-data-gateway-and-finders",
        "title": "Row Data Gateway, and Reading in Data",
        "module": "Chapter 10 · Data Source Architectural Patterns",
        "one_line": "A Row Data Gateway is an object per row, loaded by finders; Chapter 3’s rule for finders is to bring back many rows in one query, because every query pays the wait.",
        "summary": (
            "Chapter 10's Row Data Gateway gives each row an object that holds its fields "
            "and its SQL, loaded by finders. Chapter 3's Reading in Data says where the "
            "finders go and how they should read: rather one query with rows you do not "
            "need than fifty that each fetch one. Time fifty keyed finds against one broad "
            "query and a batched one, on a slow link and on a fast one."
        ),
        "key": [
            "a row data gateway: an object a row",
            "a finder wraps one SELECT in a method",
            "keyed: wanted·(latency + row time)",
            "broad: latency + broad·(row time)",
            "batched: batches·latency + wanted·(row time)",
            "profile with your own database",
        ],
        "key_label": "Row Data Gateway and Reading in Data in six lines",
        "concepts_intro": (
            "Three terms. The first is the pattern, the second where its loading lives, and "
            "the third the quantity the lab turns on."
        ),
        "concepts": [
            ("Row Data Gateway",
             "An object that mimics one record exactly, with one field for each column, and "
             "holds the SQL to read and write it. It does any simple type conversion and "
             "nothing else: no business rules."),
            ("Finder",
             "A method that wraps a SELECT in an ordinary method call, such as `find(id)` or "
             "a find for every order of a customer. Reading in Data prefers finders on "
             "objects of their own to static methods on the row class."),
            ("Latency",
             "The wait a statement pays to reach the database and come back, whatever it "
             "returns. In the lab it is a fixed time a statement, added to a time for each "
             "row; both are the lesson's figures, not a measured network."),
        ],
        "read_title": "The pattern, the narrative's rules of thumb, then the arithmetic",
        "read_intro": (
            "Read Chapter 10, Row Data Gateway, and then Chapter 3, Reading in Data, in your "
            "own copy first. The lesson reads the pattern as a tool and the section as an "
            "argument, and then times three ways of loading fifty rows."
        ),
        "body": [
            ("p", "&ldquo;It's usually better to use one query that brings back unnecessary "
                  "rows than to issue 50 individual queries.&rdquo; That is Chapter 3's "
                  "advice in Reading in Data, and the lab in this lesson puts numbers on it. "
                  "First, though, the pattern whose objects those queries load: Chapter "
                  "10's Row Data Gateway. Read both in your own copy first."),
            ("p", "Row Data Gateway, read as a tool, is an object that looks exactly like one "
                  "record: each column becomes a field, the gateway converts the database's "
                  "types to the language's, and every detail of reaching the database is "
                  "behind its interface. Fowler uses it most with a Transaction Script, "
                  "where it factors the database code out so that several scripts can share "
                  "it. With a Domain Model he does not: a simple mapping wants an Active "
                  "Record, which does the same job with one layer fewer, and a complex one a "
                  "Data Mapper. A gateway under a Domain Model on a large scale gives three "
                  "representations of the data, in the domain, the gateway and the "
                  "database, and that, he says, is one too many."),
            ("p", "Its open question is where the finders go, and Chapter 10 and Reading in "
                  "Data give one answer. A table-based class can hold its finders beside its "
                  "inserts and updates; a row-based one cannot, since there is no row "
                  "object until the find has run. Static finders on the row class work, but "
                  "a static method cannot be swapped for another, so a test cannot replace "
                  "the database with a stand-in, a Service Stub. So Fowler prefers separate "
                  "finder objects, one finder class for each table beside its gateway class, "
                  "each method wrapping one SELECT and returning row objects."),
            ("p", "The lesson's snippet keeps the finder static for brevity, which is the "
                  "choice Reading in Data warns against; a finder object would hold the same "
                  "method without `static`. `OrderRow` holds an order's id and status, and "
                  "`find` runs one keyed SELECT and builds the row, or returns `null` when "
                  "there is none."),
            ("code", _lines(ORDER_ROW)),
            ("p", "Reading in Data adds a warning that is easy to miss: a finder reads the "
                  "database, not what is in memory. Add a member to a club in memory, run a "
                  "query for the club's members, and the new one is not in the result. "
                  "Fowler's advice is to do queries at the beginning. Then come his rules of "
                  "thumb on speed. Pull back many rows at once; never query one table "
                  "repeatedly to get several rows; it is almost always better to bring back "
                  "too much than too little, though too many rows locked under pessimistic "
                  "concurrency is a cost of its own."),
            # F11, PDF p. 52 of the operator's copy.
            ("p", "His illustration is the quotation's. You need 50 people you can name by "
                  "primary key, but the only query you can write brings back 200, from which "
                  "further logic picks the 50; that one query is usually better than 50. "
                  "Joins help the same way, pulling several tables back in one query, "
                  "though he notes that databases are optimised for up to three or four "
                  "joins a query and suffer beyond that. And he ends the section with his "
                  "own caveat: profile with your own database and data, because for every "
                  "rule of thumb he has heard of surprising exceptions."),
            ("p", "Now the arithmetic. The lab takes the rows wanted, the rows the broad query "
                  "returns, a batch size, a latency a statement and a time a row. Keyed finds "
                  "are one statement a row wanted, each paying the latency and its row; the "
                  "broad query is one statement paying the latency once and every row it "
                  "returns; finds in batches send the keys `batch` at a time, each batch one "
                  "statement. That third strategy is the lab's, not the book's. Its seven "
                  "tiles are the keyed statements and time, the broad query's rows and "
                  "time, the batched statements and time, and the rows the broad query "
                  "returns that nobody wanted."),
            ("p", "In <code>fifty-or-one</code> the 50 and the 200 are the book's; the 5 ms "
                  "latency, 0.1 ms a row and batches of 10 are illustrative. Keyed finds make "
                  "50 statements and take 255 ms. The broad query returns 200 rows, 150 of "
                  "them unneeded, in 25 ms. Batched finds make 5 statements and take 30 ms. "
                  "Fifty keyed finds take ten times as long as one query that returns four "
                  "times the rows, because forty-nine of their fifty waits are the cost."),
            ("p", "In <code>local-database</code> the latency falls to 0.2 ms, as if the "
                  "database sat on the same machine, and the advice reverses on its own "
                  "figures: keyed finds take 15 ms, the broad query 101/5 = 20.20 ms, and "
                  "batches 6 ms. With a short wait, the 150 rows nobody wanted cost more "
                  "than the 49 extra statements. That is Fowler's point about measuring, "
                  "made by the lab: the rule of thumb is a rule about latency, and it holds "
                  "where a statement's wait is large against a row's cost."),
            ("h3", "Exercise"),
            ("ul", [
                "Rows wanted: 30. Rows the broad query returns: 600.",
                "Batches of 15 keys. Latency 4 ms a statement; 0.05 ms a row.",
            ]),
            ("p", "Compute by hand the statements and the time of keyed finds, of the broad "
                  "query and of finds in batches, and the rows the broad query returns that "
                  "are not wanted. Say which is fastest here, and whether the broad query "
                  "still beats keyed finds. Check your figures in the lab afterwards."),
            ("p", "A Row Data Gateway holds no business rules. The next lesson, Active "
                  "Record, adds them, and reads the one sentence Chapter 10 uses to tell the "
                  "two apart."),
        ],
        "lab": ("eakit", {
            "mode": "load",
            "view": "finds",
            "preset": "fifty-or-one",
            "presets": [
                {"id": "fifty-or-one",
                 "label": "Fifty of two hundred, 5 ms a statement",
                 "wanted": "50", "broad": "200", "batch": "10",
                 "latencyMs": "5", "rowMs": "0.1",
                 "expect": {"ldKeyedMs": "255", "ldBroadMs": "25", "ldBatchMs": "30"}},
                {"id": "local-database",
                 "label": "The same rows, 0.2 ms a statement",
                 "wanted": "50", "broad": "200", "batch": "10",
                 "latencyMs": "0.2", "rowMs": "0.1",
                 "expect": {"ldKeyedMs": "15", "ldBroadMs": "101/5 = 20.20", "ldBatchMs": "6"}},
            ],
            "panel_title": "Fifty keyed finds, one broad query, or batches",
            "panel_intro": (
                "Keyed finds are one statement a row wanted; the broad query is one "
                "statement returning every row it returns; finds in batches send the keys "
                "a batch at a time, a strategy the lab adds and the book does not discuss. "
                "Each statement pays the latency, and each row its time."
            ),
            "source": (
                "50 rows wanted of 200 returned are the book's illustration in Chapter 3, "
                "Reading in Data; the latency, row time and batch size are illustrative"
            ),
        }),
        "steps_title": "Timing three ways to read rows",
        "steps_intro": "Four steps, the last of them on a page of your own.",
        "steps": [
            ("Time the keyed finds",
             "Multiply the rows wanted by the latency plus one row's time. That many "
             "statements, each paying the wait."),
            ("Time the broad query",
             "Add the latency once to the rows it returns times a row's time, and subtract "
             "the rows wanted from the rows returned for the rows nobody needs."),
            ("Time the batches",
             "Divide the rows wanted by the batch size, rounding up, for the statements; "
             "multiply by the latency and add the rows wanted times a row's time."),
            ("Count it on a page you know",
             "Take one page in a system you know that loads a list. From a log or a "
             "profiler, count the queries it issues and the rows each returns, and write "
             "whether it reads the list in one query or one row at a time."),
        ],
        "worked": {
            "title": "Fifty keyed finds against one query",
            "intro": [
                "Work <code>fifty-or-one</code>: 50 rows wanted, 200 returned, batches of 10, "
                "5 ms a statement and 0.1 ms a row.",
            ],
            "lines": [
                "keyed: 50 statements of 5 + 0.1 ms",
                "keyed: 50 × 5.1, which is 255 ms",
                "broad: 5 + 200 × 0.1, which is 25 ms",
                "batches: 50 / 10, which is 5 statements",
                "batched: 5 × 5 + 50 × 0.1, which is 30 ms",
                "unneeded rows: 200 − 50, which is 150",
            ],
            "after": [
                "Of the keyed finds' 255 ms, 250 are waiting. The broad query waits once and "
                "pays for 150 rows nobody needs, which at 0.1 ms each costs 15 ms: far less "
                "than 49 more waits.",
            ],
        },
        "quiz_title": "Finders and their arithmetic",
        "quiz": [
            {"q": "Take the exercise: 30 rows wanted, a broad query of 600 rows, batches of "
                  "15, 4 ms a statement and 0.05 ms a row. What are the three times?",
             "a": ["keyed 121.50 ms, broad 34 ms, batched 9.50 ms",
                   "keyed 120 ms, broad 34 ms, batched 9.50 ms",
                   "keyed 121.50 ms, broad 30 ms, batched 9.50 ms",
                   "keyed 121.50 ms, broad 34 ms, batched 8 ms"],
             "c": 0,
             "why": "Keyed: 30 statements of 4 + 0.05 ms, 30 × 4.05 = 243/2 = 121.50 ms. "
                    "Broad: 4 + 600 × 0.05 = 34 ms, with 570 rows unneeded. Batched: 30 / 15 "
                    "= 2 statements, 2 × 4 + 30 × 0.05 = 19/2 = 9.50 ms. Batching wins here, "
                    "and the broad query still beats keyed finds. 120 ms leaves out the "
                    "keyed rows' time, 30 ms the broad query's wait, and 8 ms the batched "
                    "rows' time."},
            {"q": "Reading in Data names one cost of making a row-based class's finders "
                  "static. What is it?",
             "a": ["A static finder issues one query for every row",
                   "A static finder cannot be substituted, so a test cannot replace the "
                   "database with a Service Stub",
                   "A static finder reads the objects in memory instead of the database",
                   "A static finder cannot take a parameter"],
             "c": 1,
             "why": "The section's point is substitutability: a static method cannot be "
                    "swapped for another, which is why Fowler prefers finder objects. How "
                    "many queries a finder issues depends on its SQL, not on `static`, and "
                    "every finder reads the database."},
            {"q": "You add a member to a club in memory and then run a finder for the club's "
                  "members. What does Reading in Data warn?",
             "a": ["The new member is returned twice",
                   "The finder fails until the change is committed",
                   "The new member is not in the result, because finders work on the "
                   "database's state",
                   "The new member is returned, because the gateway holds it"],
             "c": 2,
             "why": "Finders query the database, so an object added only in memory is not "
                    "picked up. Fowler's advice is to do queries at the beginning."},
            {"q": "On <code>local-database</code> (50 wanted of 200, batches of 10, 0.2 ms a "
                  "statement, 0.1 ms a row), which order does the lab put the three times "
                  "in, fastest first?",
             "a": ["broad, batched, keyed",
                   "batched, keyed, broad",
                   "keyed, batched, broad",
                   "batched, broad, keyed"],
             "c": 1,
             "why": "Batched 5 × 0.2 + 50 × 0.1 = 6 ms; keyed 50 × 0.3 = 15 ms; broad 0.2 + "
                    "200 × 0.1 = 101/5 = 20.20 ms. With a short wait the broad query's 150 "
                    "extra rows cost more than the extra statements, which is why the rule "
                    "of thumb is a rule about latency."},
        ],
        "mistakes": [
            ("Thinking that fetching only the rows you need is always cheaper",
             "Every statement pays the latency, whatever it returns. On the lesson's first "
             "preset, fifty keyed finds take 255 ms and one query that returns four times "
             "the rows takes 25 ms, ten times less: the extra 150 rows cost 15 ms, and the "
             "49 extra waits 245. Reading in Data's advice, to pull back too much rather "
             "than too little, is that arithmetic in words."),
            ("Thinking a static finder is as good as a finder object",
             "It finds the same rows, but Reading in Data's point is substitutability: a "
             "static method cannot be replaced, so a test cannot swap the database for a "
             "Service Stub. The lesson's snippet uses a static finder only for brevity. "
             "Moving the method onto an object of its own, one finder class a table, is "
             "what the section recommends."),
            ("Taking the rule of thumb for a measurement",
             "The second preset reverses the advice on its own figures: at 0.2 ms a "
             "statement, keyed finds beat the broad query. Fowler says as much at the end "
             "of the section: profile your application with your own database and data, "
             "because every rule of thumb has its surprising exceptions."),
        ],
        "standard": (
            "Finish when you can time three ways of reading rows by hand.",
            "Given the rows wanted, the rows a broad query returns, a batch size, a latency "
            "and a time a row, compute the keyed, broad and batched times and the unneeded "
            "rows, and say which way the figures point."
        ),
        "note": (
            "The lab's model is a fixed wait a statement plus a fixed time a row. A real "
            "database also caches, locks and plans, and a broad query's extra rows can cost "
            "more than their transfer; none of that is in the figures. The 50 and the 200 "
            "are the book's illustration; the timings are the lesson's."
        ),
    },
    # ---------------------------------------------------------------- 03
    # Chapter 10, Active Record: PDF pp. 154-158 of the operator's copy (How
    # It Works, pp. 154-155; When to Use It, p. 155). Row Data Gateway's
    # crux, p. 149, and the turn to Active Record, p. 150. Chapter 3,
    # Architectural Patterns, on Active Record, p. 47.
    # Quote: PDF p. 149, 14 words, ea_quotes.py OK. Lesson total: 14 words.
    # F22, PDF p. 102 of the operator's copy: a couple of dozen classes close
    # to the database (Chapter 8, Down to the Data Source Layer).
    {
        "slug": "active-record",
        "title": "Active Record",
        "module": "Chapter 10 · Data Source Architectural Patterns",
        "one_line": "An Active Record is a row object that also carries the domain logic on its data; a Row Data Gateway is the same shape with none.",
        "summary": (
            "Chapter 10's Active Record wraps a row, holds its SQL and adds the domain logic "
            "that acts on its data. It has the shape of a Row Data Gateway, and Chapter 10 "
            "tells the two apart by one thing. Count the routines of two classes over one "
            "account row, sort them into database access and domain logic, and name each "
            "pattern."
        ),
        "key": [
            "an Active Record: row, SQL, domain logic",
            "a row data gateway: row and SQL only",
            "tables match classes: isomorphic",
            "simple logic, close tables: Active Record",
            "the kit counts routines; you sort them",
        ],
        "key_label": "Active Record in five lines",
        "concepts_intro": (
            "Three ideas. The second is the one the pattern depends on, and the third is the "
            "line the lesson draws."
        ),
        "concepts": [
            ("Active Record",
             "An object that wraps a row of a table or view, does its own database access, "
             "and adds domain logic on that data. Chapter 10 calls its essence a Domain "
             "Model whose classes match the database's records very closely."),
            ("Isomorphic schema",
             "A schema with the same shape as the classes: one class for each table, one "
             "field for each column. Active Record works well only on such a schema, the "
             "pattern says."),
            ("Database access and domain logic",
             "Database access reads and writes rows: finds, inserts, updates. Domain logic "
             "is a rule of the business, such as whether an account may pay a sum. A row "
             "object with any of the second kind is an Active Record."),
        ],
        "read_title": "The pattern, its neighbour, then the count",
        "read_intro": (
            "Read Chapter 10, Active Record, and the paragraph of Row Data Gateway that "
            "compares the two, in your own copy first. The lesson reads the pattern as a "
            "tool, and then counts and sorts the routines of two classes over one row."
        ),
        "body": [
            ("p", "&ldquo;A Row Data Gateway should contain only database access logic and "
                  "no domain logic.&rdquo; Chapter 10 says it is often hard to tell a Row "
                  "Data Gateway from an Active Record, and this sentence is its test. This "
                  "lesson reads Active Record as a tool, with that test beside it. Read "
                  "the pattern in your own copy first."),
            ("p", "Active Record puts data access in the domain object, so that each object "
                  "knows how to read and write its own data. Its structure should match the "
                  "table exactly, one field for each column, typed as the SQL interface gives "
                  "the data. The pattern lists what such a class typically does: build "
                  "itself from a result-set row, build a new instance for later insertion, "
                  "offer static finders that wrap common queries, insert and update its row, "
                  "get and set its fields, and implement some pieces of business logic. That "
                  "last item is the difference."),
            ("p", "Fowler puts the difference plainly in both places: a Row Data Gateway "
                  "holds only database access, an Active Record both database access and "
                  "domain logic, and he grants that the line between them, like most in "
                  "software, is not terribly sharp, but useful. Chapter 3 gives the same "
                  "relation as a route: start with a Row Data Gateway and add domain logic "
                  "to it, particularly when you see the same code repeated in several "
                  "Transaction Scripts. Row Data Gateway's own pages say that moving such "
                  "logic in gradually turns the gateway into an Active Record, and that this "
                  "is often good, since it reduces duplication."),
            # F22, PDF p. 102 of the operator's copy.
            ("p", "When to use it: for domain logic that is not too complex, such as creates, "
                  "reads, updates and deletes, and derivations and validations on one record. "
                  "Its primary advantage is simplicity. Its primary problem is that it works "
                  "well only when the objects correspond directly to the tables; once the "
                  "logic wants collections, inheritance and direct relationships, adding "
                  "them piecemeal gets messy, and that leads to a Data Mapper. It also "
                  "couples the object design to the database design, so each is harder to "
                  "refactor. Chapter 8 puts a size on simple: a Domain Model of a couple of "
                  "dozen classes close to the database, the book's illustration, is where an "
                  "Active Record makes sense."),
            ("p", "The lesson's two classes cover one `account` row with three fields. Each "
                  "routine that talks to the database shows its SQL as a comment, so you "
                  "can see what it would run; the bodies are left out because the lesson is "
                  "about which routines are which. The first, `Account`, is an Active "
                  "Record."),
            ("code", _lines(ACCOUNT_RECORD)),
            ("p", "The second, `AccountRow`, is the same row with the same two database "
                  "routines and nothing else: a Row Data Gateway."),
            ("code", _lines(ACCOUNT_ROW)),
            ("p", "Now the count. The lab reads a class and prints four tiles: its fields, "
                  "its public fields that are not final, its routines with constructors "
                  "included, and its public routines. On <code>active-record</code> it "
                  "prints 3 fields, 0 public, 3 routines and 1 public; on "
                  "<code>row-gateway</code>, 3, 0, 2 and 0. The kit counts routines and "
                  "cannot tell database access from domain logic, so the sorting is yours: "
                  "`find` and `update` run SQL in both classes, and the one routine the "
                  "second class lacks, `canWithdraw`, decides whether the balance and the "
                  "overdraft cover a sum. That rule of the business is what makes the first "
                  "class an Active Record."),
            ("p", "The same sorting shows where the database coupling sits. `canWithdraw` "
                  "reads two fields and touches no connection, so it can be tested on an "
                  "`Account` built in memory. The coupling is in `find` and `update`. Chapter "
                  "10 notes that static finders are more common with this pattern because of "
                  "its closeness to the database, and that moving them to a separate class, "
                  "as with Row Data Gateway, is better for testing."),
            ("h3", "Exercise"),
            ("code", _lines(MEMBER_RECORD)),
            ("p", "For this `Member`, count the fields, the public fields that are not final "
                  "and the routines. Then sort the routines into database access and domain "
                  "logic, and say which of the two patterns the class is. Paste it into the "
                  "lab afterwards to check the counts; the sorting is yours."),
            ("p", "Active Record breaks down as the domain gets richer. The next lesson, Data "
                  "Mapper, reads the pattern Fowler turns to then, and counts what it "
                  "changes about who depends on whom."),
        ],
        "lab": ("cckit", {
            "mode": "code",
            "view": "class",
            "preset": "active-record",
            "presets": [
                {"id": "active-record",
                 "label": "Account: a row's data, its SQL and a business rule",
                 "code": ACCOUNT_RECORD,
                 "expect": {"coRoutines": "3"}},
                {"id": "row-gateway",
                 "label": "AccountRow: the same row with no domain logic",
                 "code": ACCOUNT_ROW,
                 "expect": {"coRoutines": "2"}},
            ],
            "panel_title": "Count a row object's routines",
            "panel_intro": (
                "Paste a Java class. The lab counts its fields, its public fields that are "
                "not final, its routines with constructors included, and its public "
                "routines. It cannot tell a routine that reaches the database from one that "
                "applies a business rule: that sorting is yours, and it decides the pattern."
            ),
        }),
        "steps_title": "Telling an Active Record from a gateway",
        "steps_intro": "Four steps, the last of them on a class of your own.",
        "steps": [
            ("List the routines",
             "List every routine of the class over one row, constructors included."),
            ("Mark the database access",
             "Mark each routine that reads or writes the database: finds, inserts, updates, "
             "deletes, and the code that builds the object from a result row."),
            ("Mark the domain logic",
             "Mark each routine that applies a rule of the business to the row's data: a "
             "derivation, a validation, a decision. If any is marked, the class is an Active "
             "Record; if none, a Row Data Gateway."),
            ("Sort a class you know",
             "Take one class in a system you know that both saves itself and carries a "
             "business rule. List its methods in two columns, database access and domain "
             "logic, and write how many fall in each."),
        ],
        "worked": {
            "title": "Three routines, one rule",
            "intro": [
                "Count and sort <code>active-record</code>.",
            ],
            "lines": [
                "fields: id, balance, overdraft, private",
                "routines: find, update, canWithdraw",
                "find runs SELECT: database access",
                "update runs UPDATE: database access",
                "canWithdraw: a rule, domain logic",
                "domain logic present: Active Record",
            ],
            "after": [
                "Take `canWithdraw` away and the class is <code>row-gateway</code>: three "
                "fields, two routines, both database access, and no domain logic.",
            ],
        },
        "quiz_title": "Active Record, counted and sorted",
        "quiz": [
            {"q": "Take the exercise's `Member`. How many fields, public fields that are not "
                  "final and routines does it have, and which pattern is it?",
             "a": ["4 fields, 1 public and not final, 3 routines; an Active Record",
                   "4 fields, 2 public and not final, 3 routines; an Active Record",
                   "4 fields, 1 public and not final, 3 routines; a Row Data Gateway",
                   "3 fields, 1 public and not final, 3 routines; an Active Record"],
             "c": 0,
             "why": "`id`, `email`, `points` and `joined` are 4 fields; `email` is public and "
                    "not final, while `joined` is public but final, so 1. The routines are "
                    "`find`, `insert` and `level`, 3 (the lab also prints 2 public: `insert` "
                    "and `level`). `find` and `insert` are database access; `level` derives a "
                    "member's level from their points, which is domain logic, so the class "
                    "is an Active Record. Leaving out `joined` gives 3 fields; counting it as "
                    "public data gives 2."},
            {"q": "By what one thing does Chapter 10 tell a Row Data Gateway from an Active "
                  "Record?",
             "a": ["Whether its finders are static",
                   "Whether it maps one table or several",
                   "Whether its fields are public",
                   "Whether it contains any domain logic"],
             "c": 3,
             "why": "The crux, Row Data Gateway's pages say, is whether any domain logic is "
                    "present; if it is, the class is an Active Record. Static finders appear "
                    "with both, and both map one row of one table."},
            {"q": "What does Active Record's When to Use It give as the pattern's primary "
                  "problem?",
             "a": ["It cannot hold business logic",
                   "It works well only when the objects correspond directly to the tables",
                   "It cannot be used with views",
                   "It needs a separate finder class"],
             "c": 1,
             "why": "It works well only on an isomorphic schema; collections, inheritance and "
                    "direct relationships do not map easily onto it. It holds business logic "
                    "by definition, it can be used with views (updates through them are "
                    "harder), and a separate finder class is an option, better for testing."},
            {"q": "The lab prints 3 routines for <code>active-record</code> and 2 for "
                  "<code>row-gateway</code>. Which routine makes the difference, and what "
                  "kind is it?",
             "a": ["`canWithdraw`, domain logic",
                   "`update`, database access",
                   "`find`, database access",
                   "a constructor, which the kit counts"],
             "c": 0,
             "why": "Both classes have `find` and `update`, which run SQL; neither declares a "
                    "constructor. Only `Account` has `canWithdraw`, a business rule on the "
                    "balance and overdraft."},
        ],
        "mistakes": [
            ("Thinking Active Record and Row Data Gateway are two names for one pattern",
             "They have the same shape, one object a row holding its own SQL, and Chapter 10 "
             "grants they are often hard to tell apart. Its test is the quotation: a Row "
             "Data Gateway holds only database access, and any domain logic makes the class "
             "an Active Record. On the lesson's illustration the two classes differ by one "
             "routine, `canWithdraw`, and that routine is the difference."),
            ("Thinking an Active Record cannot be tested without a database",
             "Its domain methods can be, when they do not call the SQL: `canWithdraw` reads "
             "two fields and can be tested on an `Account` built in memory. The coupling "
             "is in the find and save routines, and Chapter 10 adds that moving the finders "
             "into a class of their own is better for testing."),
            ("Placing Active Record outside the Domain Model",
             "It is tempting to read the four patterns as gateways on one side and the "
             "Domain Model on the other. Chapter 10 says the essence of an Active Record is "
             "a Domain Model whose classes match the database's records closely. It is one "
             "way to build a simple Domain Model, and Data Mapper the way for a rich one."),
        ],
        "standard": (
            "Finish when you can name a row object's pattern from its routines.",
            "Given a class over one row, sort its routines into database access and domain "
            "logic, and say whether it is a Row Data Gateway or an Active Record."
        ),
        "note": (
            "The lab counts fields and routines by the rules beside its listing. It cannot "
            "tell a routine that runs SQL from one that applies a rule, and that is the "
            "pattern's whole test, so the sorting is yours. The SQL in the snippets is in "
            "comments so that the routines stay short."
        ),
    },
    # ---------------------------------------------------------------- 04
    # Chapter 10, Data Mapper: PDF pp. 159-172 of the operator's copy (the
    # problem, p. 159; How It Works, pp. 159-162; When to Use It, p. 162; the
    # examples from p. 163 are pointed to, not read). Chapter 18, Mapper:
    # PDF pp. 418-419. Chapter 3 on O/R mapping tools, p. 49; Chapter 8, Down
    # to the Data Source Layer, on a mapping tool, p. 103 (the course's one
    # modern aside, PLAN section F.3, builds on these).
    # Quote: PDF p. 159, 14 words, ea_quotes.py OK. Lesson total: 14 words.
    {
        "slug": "data-mapper",
        "title": "Data Mapper",
        "module": "Chapter 10 · Data Source Architectural Patterns",
        "one_line": "A Data Mapper moves data between the objects and the database and keeps each ignorant of the other; it reverses a dependency and adds one.",
        "summary": (
            "Chapter 10's Data Mapper is a layer that moves data between a rich domain "
            "model and the database while keeping them independent of each other and of the "
            "mapper. Read it with Chapter 18's Mapper, then trace what a change to the "
            "database library and a change to the domain class reach with an Active Record "
            "and with a mapper."
        ),
        "key": [
            "a mapper: objects and tables kept apart",
            "the domain no longer depends on the SQL",
            "the mapper depends on both sides",
            "a third party wires the mapper in",
            "its price: one more layer",
        ],
        "key_label": "Data Mapper in five lines",
        "concepts_intro": (
            "Three ideas: the pattern, the base pattern it is a case of, and the condition "
            "that calls for it."
        ),
        "concepts": [
            ("Data Mapper",
             "A layer of mappers that loads and saves domain objects, so that the objects "
             "hold no SQL and know nothing of the schema, and the domain layer does not even "
             "know the mapper is there."),
            ("Mapper",
             "Chapter 18's general form: an object that sets up communication between two "
             "subsystems that stay ignorant of each other and of it. Since neither may call "
             "it, something else has to invoke it."),
            ("Variant schemas",
             "An object schema and a relational schema that do not match, because the "
             "objects use collections and inheritance, which a relational database lacks. "
             "That mismatch is what makes the mapper's work a complexity of its own."),
        ],
        "read_title": "The pattern, its base pattern, then the count",
        "read_intro": (
            "Read Chapter 10, Data Mapper, as far as its examples, and Chapter 18, Mapper, "
            "in your own copy first. The lesson reads both as tools, and then traces two "
            "changes through the same small design with and without a mapper."
        ),
        "body": [
            ("p", "&ldquo;With Data Mapper the in-memory objects needn't know even that "
                  "there's a database present&rdquo;, Chapter 10 says, and goes on: no SQL "
                  "interface code in them, and no knowledge of the schema. This lesson reads "
                  "Data Mapper and the base pattern behind it, Chapter 18's Mapper, as "
                  "tools. Read them in your own copy first; the pattern's examples are "
                  "worth reading in the book."),
            ("p", "The problem comes first. Objects have collections and inheritance, and "
                  "relational databases do not, so a model with a lot of business logic "
                  "ends up with a schema of its own that does not match the tables. Data "
                  "must still move between the two, and if the objects know the database's "
                  "structure, a change on one side tends to ripple to the other. The mapper "
                  "is a layer that does the moving and keeps the two apart. The schema was "
                  "always ignorant of the objects; now the objects are ignorant of the "
                  "schema, and, since a Data Mapper is a kind of Mapper, of the mapper too."),
            ("p", "Mapper, in Chapter 18, says what that costs in design. A mapper sits "
                  "between two subsystems neither of which knows it, so the hard part is how "
                  "to invoke it: a third subsystem drives it, or it listens to events on one "
                  "side. Gateway is by far the more common choice, because it is simpler to "
                  "write and to use; a Mapper is for when neither side may depend on the "
                  "interaction, which in enterprise applications mostly means the database."),
            ("p", "How it works, in brief: a client asks the mapper to find an object, the "
                  "mapper checks an Identity Map for it and loads it if it is not there, and "
                  "a save pulls the data out of the object and shuttles it to the database. "
                  "Knowing what changed, what is new and what is gone is a Unit of Work's "
                  "job; how much of a graph of objects to load at once is the mapper's "
                  "design, with Lazy Load to stop it pulling back the whole database. The "
                  "next course reads those three patterns. The whole layer can be "
                  "substituted, for testing or for another database."),
            ("p", "The pattern does not claim the objects can be wholly unaware. They may "
                  "need to call a finder, and Fowler would rather they did not depend on "
                  "the mapper to do it, so the finders they need go in an interface placed "
                  "in the domain package, a Separated Interface. Its When to Use It is "
                  "plain: use a Data Mapper when the schema and the object model must evolve "
                  "independently, most often with a Domain Model; its price is the extra "
                  "layer Active Record does not have, and he would not choose one without a "
                  "Domain Model. A simple model over tables its own team controls can use "
                  "Active Record instead."),
            ("p", "The lesson's snippet is the mapper for the `Account` of the last lesson, "
                  "which now has a constructor and no SQL. `find` runs the SELECT, moves to "
                  "the one row with `next`, and builds the account from its columns. "
                  "`Account` knows neither the table nor `AccountMapper`."),
            ("code", _lines(ACCOUNT_MAPPER)),
            ("p", "Now the count, with the lab of the first lesson: records `dependent, "
                  "dependency`, the name that changes, what depends on it directly, and what "
                  "it reaches in all. In <code>active-record</code> a screen and a report "
                  "use `account`, and `account` uses `jdbc`. Change `jdbc` and the lab "
                  "prints 1: account directly and 3: account, report, screen in all: the "
                  "database library's change reaches the screen and the report through the "
                  "domain class."),
            ("p", "In <code>mapper</code> the screen and the report still use `account`, but "
                  "`account` uses nothing; `mapper` uses `account` and `jdbc`, and `main` "
                  "uses `mapper`. Change `jdbc` and the lab prints 1: mapper and 2: main, "
                  "mapper. `main` is Mapper's third subsystem, the code that wires the "
                  "mapper in; no screen, no report and no domain class is reached."),
            ("p", "Now change the domain class instead. In "
                  "<code>active-record-domain-change</code> `account` changes in the first "
                  "design and the lab prints 2: report, screen for both tiles. In "
                  "<code>mapper-domain-change</code> it changes in the mapper design and the "
                  "lab prints 3: mapper, report, screen directly and 4: main, mapper, report, "
                  "screen in all. The mapper has not removed a dependency: it has reversed "
                  "the one between the domain and the database, and added one, its own on "
                  "the domain. That is the price When to Use It names, counted."),
            ("p", "Fowler did not expect most readers to write this layer by hand. Chapter "
                  "3 says that anyone with a Domain Model should seriously consider buying "
                  "an O/R mapping tool, and Chapter 8 strongly suggests one unless the team "
                  "is strong or the mapping can be simplified. Since 2002 that advice has "
                  "become the usual practice: the object-relational frameworks most "
                  "platforms now provide implement Data Mapper, with Unit of Work and "
                  "Identity Map, for you. This is a continuation of the chapter rather than "
                  "a view against it. Fowler's own caveat still applies: a tool makes a big "
                  "dent in the effort, and using and tuning it is still a small but real "
                  "piece of work, which these patterns help you choose among."),
            ("h3", "Exercise"),
            ("ul", [
                "`web, invoice; invoice, customer; invoicemapper, invoice; invoicemapper, "
                "jdbc; customermapper, customer; customermapper, jdbc; main, invoicemapper; "
                "main, customermapper`",
                "The name that changes: `jdbc`.",
            ]),
            ("p", "List by hand what depends on `jdbc` directly and what the change reaches "
                  "in all, and say whether either domain class or `web` is reached. Type the "
                  "records into the lab afterwards to check."),
            ("p", "Which of the four patterns to use depends on the schema you have and the "
                  "model you want. The next lesson, Building the Mapping, reads Chapter 3's "
                  "three situations, and what to do when one kind of data has two sources."),
        ],
        "lab": ("cckit", {
            "mode": "deps",
            "view": "ripple",
            "preset": "active-record",
            "presets": [
                {"id": "active-record",
                 "label": "Active Record: the account holds its own SQL",
                 "edges": "screen, account; report, account; account, jdbc",
                 "changed": "jdbc",
                 "expect": {"dgDirect": "1: account",
                            "dgAffected": "3: account, report, screen"}},
                {"id": "active-record-domain-change",
                 "label": "Active Record, with the account class changed",
                 "edges": "screen, account; report, account; account, jdbc",
                 "changed": "account",
                 "expect": {"dgDirect": "2: report, screen",
                            "dgAffected": "2: report, screen"}},
                {"id": "mapper",
                 "label": "Data Mapper: the mapper holds it, and main wires the mapper",
                 "edges": "screen, account; report, account; mapper, account; "
                          "mapper, jdbc; main, mapper",
                 "changed": "jdbc",
                 "expect": {"dgDirect": "1: mapper", "dgAffected": "2: main, mapper"}},
                {"id": "mapper-domain-change",
                 "label": "The same design, with the account class changed",
                 "edges": "screen, account; report, account; mapper, account; "
                          "mapper, jdbc; main, mapper",
                 "changed": "account",
                 "expect": {"dgDirect": "3: mapper, report, screen",
                            "dgAffected": "4: main, mapper, report, screen"}},
            ],
            "panel_title": "What a change reaches, with and without a mapper",
            "panel_intro": (
                "Each record is one dependency, written dependent, dependency. Name the "
                "class that changes; the lab lists what depends on it directly and "
                "everything the change reaches. The designs are the lesson's."
            ),
        }),
        "steps_title": "Tracing a change through a mapper",
        "steps_intro": "Four steps, the last of them on a domain class of your own.",
        "steps": [
            ("Write both designs",
             "Write the Active Record design and the mapper design as `dependent, "
             "dependency` records, including whatever creates the mapper."),
            ("Change the database side",
             "Name the database library as changed and list what depends on it directly "
             "and what it reaches, in each design."),
            ("Change the domain side",
             "Name the domain class as changed and list the same two things. The mapper "
             "now appears among its dependents."),
            ("Place a class you know",
             "Take one domain class in a system you know. Write down whether it, or "
             "something else, holds its SQL, and which of the four patterns that makes it."),
        ],
        "worked": {
            "title": "The database library changes, behind a mapper",
            "intro": [
                "Trace <code>mapper</code>: a change to `jdbc`.",
            ],
            "lines": [
                "screen and report use account",
                "mapper uses account and jdbc",
                "main uses mapper",
                "jdbc changes: mapper uses it, 1",
                "mapper is used by main: 2 reached",
                "account, screen, report: untouched",
            ],
            "after": [
                "With an Active Record the same change reached the screen and the report "
                "through `account`. Behind the mapper it stops at the mapper and the code "
                "that creates it.",
            ],
        },
        "quiz_title": "Mappers, traced",
        "quiz": [
            {"q": "Take the exercise's eight records, with `jdbc` changed. What depends on it "
                  "directly, and what does the change reach in all?",
             "a": ["2 directly (customermapper, invoicemapper); 3 in all, adding main",
                   "2 directly; 5 in all, adding main, invoice and customer",
                   "2 directly; 4 in all, adding main and web",
                   "3 directly (customermapper, invoicemapper, main); 3 in all"],
             "c": 0,
             "why": "Only the two mappers use `jdbc`, so the lab prints 2: customermapper, "
                    "invoicemapper, and the only thing that uses a mapper is `main`, so 3: "
                    "customermapper, invoicemapper, main in all. The mappers use `invoice` "
                    "and `customer`, but a change travels to what depends on the changed "
                    "name, not to what it depends on, so neither domain class is reached, "
                    "and `web` uses only `invoice`. `main` is reached through the mappers, "
                    "not directly."},
            {"q": "In <code>mapper-domain-change</code> the `account` class changes. What "
                  "does the lab print, against Active Record's 2: report, screen?",
             "a": ["2: report, screen and 2 in all, as with Active Record",
                   "3: mapper, report, screen directly and 4 in all, adding main",
                   "1: mapper directly and 2 in all",
                   "3: mapper, report, screen directly and 3 in all"],
             "c": 1,
             "why": "The mapper depends on the domain class, so it is one more direct "
                    "dependent, and `main`, which uses the mapper, is reached through it: 4: "
                    "main, mapper, report, screen. The mapper reverses the dependency "
                    "between domain and database and adds its own on the domain."},
            {"q": "What does Data Mapper's When to Use It give as the primary occasion for "
                  "the pattern?",
             "a": ["Whenever an application uses a relational database",
                   "When the domain logic is mostly creates, reads, updates and deletes",
                   "When the database schema and the object model must evolve independently",
                   "When the classes match the tables one to one"],
             "c": 2,
             "why": "Independent evolution, most often with a Domain Model. Simple CRUD logic "
                    "over tables that match the classes is Active Record's case, and Fowler "
                    "says he would not choose a Data Mapper without a Domain Model."},
            {"q": "Chapter 18's Mapper names one part of using a mapper as the complicated "
                  "one. Which?",
             "a": ["Deciding how to invoke it, since neither subsystem it separates may "
                   "call it",
                   "Writing its SQL",
                   "Moving the data, once it is invoked",
                   "Keeping the two subsystems in one package"],
             "c": 0,
             "why": "Once it is activated the shuffling of data is fairly easy to follow, the "
                    "pattern says; the complicated part is invoking it, which a third "
                    "subsystem does, or an observer of one side. In the lab that third "
                    "party is `main`."},
        ],
        "mistakes": [
            ("Thinking a Data Mapper removes dependencies",
             "It reverses them. The domain no longer depends on the database, and the mapper "
             "depends on both. On the lesson's illustration a change to `jdbc` stops at the "
             "mapper and `main`, but a change to `account` now has one more direct dependent, "
             "the mapper, and reaches two more classes in all, the mapper and the `main` that "
             "wires it."),
            ("Using a Data Mapper for every application",
             "Fowler ties it to a rich Domain Model. Its price is an extra layer, he would "
             "not choose it without a Domain Model, and for a simple model over tables its "
             "team controls an Active Record is less work. Chapter 8 makes the same "
             "pairing: Active Record for a simple Domain Model, Data Mapper as it grows "
             "complicated."),
            ("Expecting the domain to be wholly ignorant of the mapping",
             "The quotation says the objects need not know there is a database. The "
             "pattern's own pages add that they cannot be entirely ignorant of the mapping "
             "layer: with Lazy Load and finders they may need to know a few of its "
             "mechanisms. The remedy is a Separated Interface in the domain package for the "
             "finders they call, so that the dependency points the right way."),
        ],
        "standard": (
            "Finish when you can trace a change through a mapper.",
            "Given an Active Record design and a mapper design as dependencies, list what a "
            "change to the database library reaches in each, and what a change to the "
            "domain class reaches with the mapper."
        ),
        "note": (
            "The lab follows dependencies you state and treats each one alike; it cannot see "
            "how much of the mapper a domain change touches, or how often the domain changes "
            "against the database. The designs are the lesson's, and the frameworks the "
            "late paragraph names are the lesson's account, not the book's."
        ),
    },
    # ---------------------------------------------------------------- 05
    # Chapter 3, Building the Mapping: PDF pp. 58-59 of the operator's copy
    # (the three situations and the model-first advice, p. 58; Double
    # Mapping, pp. 58-59). Chapter 8, Down to the Data Source Layer: PDF
    # pp. 102-103.
    # Quote: PDF p. 58, 21 words, ea_quotes.py OK. Lesson total: 21 words.
    # F12, PDF p. 58 of the operator's copy: iterations of no more than six
    # weeks, preferably fewer (and six months database-free called highly
    # risky). F22, PDF p. 102: a couple of dozen classes close to the
    # database.
    # The snippet TWO_STEP reads data in, so its comments number the
    # per-source step first; Fowler numbers the steps from the in-memory
    # schema outward, so his second step is the per-source one. The body
    # says so.
    {
        "slug": "building-the-mapping",
        "title": "Building the Mapping",
        "module": "Chapter 3 · Mapping to Relational Databases",
        "one_line": "Build a Domain Model first only within short iterations, and when one kind of data has two sources, map it in two steps so the shared conversions are written once.",
        "summary": (
            "Chapter 3's Building the Mapping names three situations, a schema you choose, "
            "one you cannot change and one you can negotiate, and says what to build in "
            "each. It ends with double mapping, one kind of data from two sources. Find "
            "the conversions two mappings of one customer repeat, and see a two-step "
            "mapping write them once."
        ),
        "key": [
            "own schema, simple logic: tables first",
            "Domain Model: the model first, in short cycles",
            "existing schema: build the model gradually",
            "two sources: a mapping layer for each",
            "or two steps through a logical schema",
        ],
        "key_label": "Building the Mapping in five lines",
        "concepts_intro": (
            "Three ideas: the situations the section sorts by, the problem its second half "
            "names, and the remedy it offers."
        ),
        "concepts": [
            ("The three situations",
             "You choose the schema yourself; you map to an existing schema that cannot "
             "change; or you map to an existing one whose changes are negotiable. Which you "
             "are in, with the domain pattern, decides what to build."),
            ("Double mapping",
             "The same kind of data pulled from more than one source: two databases whose "
             "schemas differ a little, or a database and a stream of messages. Each source "
             "needs its own mapping."),
            ("Logical data store schema",
             "A schema designed to make the sources look as alike as they can. Mapping "
             "through it takes two steps: one between the objects and the logical schema, "
             "written once, and one between the logical schema and each real store, which "
             "holds the differences."),
        ],
        "read_title": "The narrative's three situations, then the count",
        "read_intro": (
            "Read Chapter 3, Building the Mapping, and Chapter 8's Down to the Data Source "
            "Layer, in your own copy first. The lesson sets out the section's argument, and "
            "then counts what two mappings of one customer repeat, before and after a "
            "two-step mapping."
        ),
        "body": [
            ("p", "&ldquo;Although building the model first is a reasonable way of thinking "
                  "about it, this advice only applies within short iterative cycles.&rdquo; "
                  "Chapter 3's Building the Mapping gives that advice and its limit in one "
                  "sentence. This lesson reads the section as an argument, with the part of "
                  "Chapter 8 that sums it up. Read both in your own copy first."),
            ("p", "Fowler sorts the work into three situations: you choose the schema; you "
                  "map to an existing schema that cannot change; or you map to an existing "
                  "one whose changes are negotiable. The simplest is the first with little "
                  "to moderate domain logic, a Transaction Script or a Table Module. Then "
                  "design the tables around the data by classic database design, and pull "
                  "the SQL away from the domain logic with a Row or a Table Data Gateway."),
            # F12, PDF p. 58 of the operator's copy.
            ("p", "With a Domain Model the advice turns round. Beware a model that looks like "
                  "a database design: build the model without regard to the database, so as "
                  "to make the domain logic as simple as it can be, and treat the database "
                  "as the way its data persists. A Data Mapper gives the most room for "
                  "that; an Active Record suits a database shaped like the model. Then the "
                  "quotation's limit. Spending six months on a model with no database and "
                  "persisting it at the end is, he says, highly risky, because the design "
                  "may have crippling performance problems that take too much refactoring "
                  "to fix. Build the database up with each iteration instead, of no more than "
                  "six weeks and preferably fewer, the book's figure, so that you learn early "
                  "how the database interactions work in practice."),
            # F22, PDF p. 102 of the operator's copy.
            ("p", "When the schema is already there, the choices are the same and the process "
                  "differs: with simple logic, gateways that mimic the database and domain "
                  "logic layered on them; with complex logic, a Domain Model, which is very "
                  "unlikely to match the existing tables, built up gradually with Data "
                  "Mappers to persist it. Chapter 8's Down to the Data Source Layer pairs the "
                  "patterns the same way: a Row or Table Data Gateway for a Transaction "
                  "Script, a Table Data Gateway for a Table Module, and for a Domain Model an "
                  "Active Record while it is a couple of dozen classes close to the database, "
                  "the book's illustration of simple, then a Data Mapper as it grows."),
            ("p", "The section's second half is double mapping: one kind of data from more "
                  "than one source. There may be several databases holding the same data "
                  "with small schema differences left by copy-and-paste reuse; Fowler "
                  "observes that the smaller the difference, the more it annoys. "
                  "Or the data may arrive sometimes from tables and sometimes in messages. "
                  "The simplest answer is a mapping layer for each source, which duplicates "
                  "a lot when the data is similar. The other is a two-step mapping. Fowler's "
                  "first step converts the in-memory objects to a logical schema designed "
                  "to make the sources look alike; his second maps the logical schema to "
                  "each physical store, and holds the differences. He adds that the extra "
                  "step pays for itself only when there are many commonalities, and that the "
                  "second step can be treated as a Gateway."),
            ("p", "The lesson's first snippet maps one customer from two sources: a row of a "
                  "table, read through JDBC's `ResultSet`, and an XML message, read through "
                  "the attributes of a DOM `Element`. Each reads three values and then "
                  "converts them the same way."),
            ("code", _lines(TWO_SOURCES)),
            ("p", "Now the count. The lab looks for runs of at least two identical lines and "
                  "prints three tiles: the repeated blocks, the lines in all the copies, and "
                  "where they are. On <code>two-sources</code> it prints 1 block, 6 lines, "
                  "lines 6–8 and lines 15–17: the constructor with its trimming and upper "
                  "casing, the credit limit and the return, written in both mappings. The kit "
                  "finds only identical lines. Lines 3–5 and 12–14 repeat in shape and "
                  "differ in their source calls and column names, so they are not counted; "
                  "those differences are exactly what a per-source step is for."),
            ("p", "The second snippet maps in two steps. Because it reads data in, its "
                  "comments number the steps from the source: its step one, a routine for "
                  "each source that fills a `CustomerData`, is the step Fowler numbers "
                  "second, the one between the logical schema and a physical store, which "
                  "holds the differences. Its step two, `toCustomer`, written once, is "
                  "Fowler's first."),
            ("code", _lines(TWO_STEP)),
            ("p", "On <code>two-step</code> the lab prints 0, 0 and none: the conversions are "
                  "in `toCustomer` once. The count does not show what the change cost, a "
                  "`CustomerData` class and a second call on every read, and that cost is "
                  "why Fowler keeps the two-step scheme for sources alike in most things "
                  "and irritatingly unlike in a few. With one source, or two that share little, a "
                  "layer for each is simpler."),
            ("h3", "Exercise"),
            ("code", _lines(SHIPMENT_TWICE)),
            ("p", "This writes one shipment to two sinks, a table and a message. Mark by hand "
                  "the lines the two routines repeat. Then write the logical record that "
                  "would carry the converted values, and say what the shared step and each "
                  "sink's step would hold. Paste it into the lab afterwards to check the "
                  "lines."),
            ("p", "Every one of these mappings runs over a connection. The next lesson, "
                  "Database Connections and Registry, reads how a connection is found, kept "
                  "and closed, and counts what batching statements saves."),
        ],
        "lab": ("cckit", {
            "mode": "code",
            "view": "dupes",
            "min_run": 2,
            "preset": "two-sources",
            "presets": [
                {"id": "two-sources",
                 "label": "One customer mapped from a table and from a message",
                 "code": TWO_SOURCES,
                 "expect": {"coDupBlocks": "1", "coDupLines": "6",
                            "coDupWhere": "lines 6–8 and lines 15–17"}},
                {"id": "two-step",
                 "label": "The same, through a logical record and one shared step",
                 "code": TWO_STEP,
                 "expect": {"coDupBlocks": "0", "coDupLines": "0", "coDupWhere": "none"}},
            ],
            "panel_title": "What two mappings repeat",
            "panel_intro": (
                "Paste Java. The lab finds runs of at least two identical lines, after "
                "collapsing white space, and lists where each copy is. Lines that repeat in "
                "shape with different names are not counted, so the duplication double "
                "mapping causes is wider than the count. The listings are the lesson's."
            ),
        }),
        "steps_title": "Finding what a second source repeats",
        "steps_intro": "Four steps, the last of them on data of your own.",
        "steps": [
            ("Name the situation",
             "Say whether you choose the schema, map to one that cannot change, or map to "
             "one whose changes are negotiable, and which domain pattern you use."),
            ("Mark the repeats",
             "Put the two mappings side by side and mark the lines that are the same in "
             "both, and the lines that differ only in the source's calls and names."),
            ("Write the logical record",
             "Write a record with one field for each value the sources share. The "
             "identical lines go in one step between that record and the objects; each "
             "source's own calls go in its own step."),
            ("Count it on data you know",
             "Take one kind of data in a system you know that arrives or leaves by two "
             "routes, a table and an API, a file and a queue. Count the conversions "
             "written in both, and write whether a shared step would hold them."),
        ],
        "worked": {
            "title": "One customer, two sources",
            "intro": [
                "Read the lab's figures for <code>two-sources</code>.",
            ],
            "lines": [
                "lines 6 to 8: construct, set limit, return",
                "lines 15 to 17: the same three lines",
                "1 block, 3 lines a copy, 6 lines in all",
                "lines 3 to 5 and 12 to 14: same shape",
                "they differ in the source calls",
                "identical lines only: not counted",
            ],
            "after": [
                "The six counted lines are the conversion both sources share: what "
                "`toCustomer` holds in <code>two-step</code>. The six uncounted ones are "
                "where the sources differ, and they stay, one routine a source.",
            ],
        },
        "quiz_title": "The mapping's situations and its repeats",
        "quiz": [
            {"q": "Take the exercise's `toTable` and `toMessage`. Which lines does the lab "
                  "mark, and what goes in the shared step?",
             "a": ["Lines 2–4 and 12–14, 6 lines: the reference, grams and postcode "
                   "conversions, which a ShipmentData filled once would carry to a step "
                   "for each sink",
                   "Lines 5–7 and 15–17, 6 lines: the three writes, which a shared step "
                   "would make once",
                   "Lines 2–8 and 12–17, 13 lines: everything but the headers",
                   "None: the routines write to different sinks, so nothing repeats"],
             "c": 0,
             "why": "Lines 2–4 and 12–14 are identical: the upper-cased reference, the "
                    "weight in grams and the postcode without spaces (1 repeated block, "
                    "6 lines in all). The writes differ, `setString` and `setLong` against "
                    "`setAttribute`, and `executeUpdate` has no partner, so they are not "
                    "counted. A `ShipmentData` filled once from the shipment holds the "
                    "conversions, and each sink's own step writes its fields."},
            {"q": "In Building the Mapping's advice to build up the database with each "
                  "iteration, how long may an iteration be?",
             "a": ["No more than six months",
                   "No more than two weeks",
                   "No more than six weeks, and preferably fewer",
                   "As long as the domain model takes to finish"],
             "c": 2,
             "why": "No more than six weeks, preferably fewer, the book's figure. Six months "
                    "is the length of the database-free model the section calls highly "
                    "risky, and finishing the model before persisting it is what the advice "
                    "rules out."},
            {"q": "In Fowler's two-step mapping, which step holds the differences between "
                  "the sources?",
             "a": ["The step from the in-memory objects to the logical schema",
                   "The step from the logical schema to each physical store",
                   "Neither: the logical schema removes them",
                   "Both, equally"],
             "c": 1,
             "why": "His second step, from the logical data store schema to each physical "
                    "one, contains the differences, and he suggests treating it as a "
                    "Gateway. The lesson's `TWO_STEP` reads data in, so its comments call "
                    "that per-source step &ldquo;step one&rdquo;: the numbering runs from "
                    "the other end."},
            {"q": "You choose the schema yourself and use a Transaction Script. What does "
                  "Building the Mapping advise?",
             "a": ["Build the domain model first, without regard to the database",
                   "Design the tables around the data, and pull the SQL out with a Row or "
                   "Table Data Gateway",
                   "Use a Data Mapper, which gives the most flexibility",
                   "Map in two steps through a logical schema"],
             "c": 1,
             "why": "That is the simplest situation: classic database design and a gateway. "
                    "Model first, and a Data Mapper, are the advice for a Domain Model, and "
                    "two steps are for one kind of data from several sources."},
        ],
        "mistakes": [
            ("Designing the database first, then the objects to fit",
             "For a Domain Model, Building the Mapping says the reverse: build the model "
             "without regard to the database and treat the database as its persistence, "
             "beware a model that looks like a database design, and do it within short "
             "iterations, building the database up as you go. Designing the tables around "
             "the data is its advice for a Transaction Script or a Table Module."),
            ("Thinking double mapping means mapping twice to the same database",
             "It means one kind of data fed from two sources: two databases with small "
             "differences in schema, or a database and a feed of messages. On the lesson's "
             "illustration the second source is an XML message, and the repeated lines are "
             "the conversions both sources share."),
            ("Adding the logical step whenever there are two sources",
             "Fowler says the extra step pays for itself only when there are many "
             "commonalities, and keeps it for stores alike in most things and "
             "irritatingly unlike in a few. The lab's 0 repeated lines on <code>two-step</code> leave out what "
             "the step costs: a logical record class and a second call on every read."),
        ],
        "standard": (
            "Finish when you can find and split what two mappings repeat.",
            "Given mapping code for one kind of data from two sources, mark the repeated "
            "lines, and write the logical record and the shared step that would hold them "
            "once."
        ),
        "note": (
            "The lab finds identical lines only. Mappings that repeat a conversion with "
            "different names, or in a different order, are not counted, so the duplication "
            "two sources cause is usually wider than the count; and the lab cannot weigh "
            "the cost of the extra step, which is the section's own condition for taking it."
        ),
    },
    # ---------------------------------------------------------------- 06
    # Chapter 3, Database Connections: PDF pp. 61-62 of the operator's copy;
    # Some Miscellaneous Points: PDF p. 63. Chapter 18, Registry: PDF
    # pp. 424-428 (scopes, pp. 424-425; When to Use It, pp. 425-426; the
    # thread-safe example by Matt Foemmel and Fowler, p. 427).
    # Quote: PDF p. 63, 16 words, ea_quotes.py OK. "guilty until proven
    # innocent": PDF p. 426, 4 words, ea_quotes.py OK. Lesson total: 20 words.
    # F13, PDF p. 425 of the operator's copy: a parameter not needed 90
    # percent of the time is what leads Fowler to a Registry.
    # The lab holds the work of each statement the same either way; that is
    # the lab's assumption (PLAN section R.4, N-8), and the body says so.
    {
        "slug": "database-connections",
        "title": "Database Connections and Registry",
        "module": "Chapter 3 · Mapping to Relational Databases",
        "one_line": "A connection is opened, tied to a transaction and closed; it is found by a parameter or a thread-scoped Registry; and statements batched into one call share one wait.",
        "summary": (
            "Chapter 3's Database Connections says how a connection is opened, pooled, tied "
            "to a transaction and closed, and Some Miscellaneous Points adds three habits, "
            "the last of them batching. Chapter 18's Registry is how code finds a connection "
            "it was not handed. Work out what batching the statements of one save removes, "
            "on a network and on one machine."
        ),
        "key": [
            "tie the connection to the transaction",
            "pass it, or look it up in the Registry",
            "one at a time: n·(latency + work)",
            "batched: m·latency + n·work",
            "a batch removes waits, not work",
        ],
        "key_label": "Connections and batching in five lines",
        "concepts_intro": (
            "Three ideas: how connections are shared, how code finds one, and what the lab "
            "counts."
        ),
        "concepts": [
            ("Connection pool",
             "A set of open connections that code borrows and returns instead of opening and "
             "closing its own. Most platforms provide one behind an interface that looks "
             "like opening a new connection, so the choice to pool stays hidden."),
            ("Registry",
             "A well-known object, usually reached through static methods, that code uses to "
             "find common objects and services such as a connection or a finder. Its data "
             "can be scoped to the process, a thread or a session; a connection is "
             "thread-scoped."),
            ("Statement batch",
             "Several SQL statements sent to the database in one call. Each call pays the "
             "round trip's wait once, however many statements it carries."),
        ],
        "read_title": "The narrative, the pattern, then the arithmetic",
        "read_intro": (
            "Read Chapter 3, Database Connections and Some Miscellaneous Points, then "
            "Chapter 18, Registry, in your own copy first. The lesson sets out the sections' "
            "argument and the pattern, and its lab counts one of the points, batching."
        ),
        "body": [
            ("p", "&ldquo;Many environments give you the ability to batch multiple SQL "
                  "queries into a single database call.&rdquo; That sentence is from Chapter "
                  "3's Some Miscellaneous Points, and Fowler adds that his examples do not do "
                  "it but production code should. This lesson reads the connection that "
                  "every statement goes through, the Registry that finds it, and then counts "
                  "what batching saves. Read the sections in your own copy first."),
            ("p", "Database Connections starts from what a connection is: the link between "
                  "the code and the database, opened before any command runs and held open "
                  "while the command, and any transaction it belongs to, takes place. "
                  "Connections are often expensive to create, so environments pool them, "
                  "and Fowler notes that most platforms now do the pooling for you; if you "
                  "must do it yourself, check first that it helps, since creating a new "
                  "connection keeps getting cheaper. A pool behind an interface that looks "
                  "like opening a fresh connection is, he says, a good thing: the choice to "
                  "pool is properly encapsulated."),
            ("p", "Then the management. Close a connection as soon as you are done, and keep "
                  "every command of one transaction on the same connection. That raises two "
                  "problems: having the connection wherever it is needed, and not forgetting "
                  "to close it. Passing it as a parameter adds it to all sorts of calls whose "
                  "only use for it is to hand it on, which is where a thread-scoped Registry "
                  "comes in. Closing by hand is easy to forget, he admits of himself, and "
                  "the garbage collector closes too late to rely on, though it makes a "
                  "backup. His preference is to tie the connection to the transaction: open "
                  "it when the transaction begins and close it at commit or rollback, a job "
                  "a Unit of Work fits naturally."),
            ("p", "Some Miscellaneous Points adds three habits. Do not use `SELECT *` with "
                  "positional column indices, since a reordered column then breaks the code; "
                  "column names are clearer, if perhaps slower, and as usual he says to "
                  "measure. Prefer static SQL that can be precompiled, and avoid putting "
                  "queries together by string concatenation. And batch statements into one "
                  "call where the platform allows it, which is the quotation and the one "
                  "point this lesson's lab counts."),
            # F13, PDF p. 425; "guilty until proven innocent", PDF p. 426.
            ("p", "Registry, in Chapter 18, is read as a tool: a well-known object that "
                  "others use to find common objects and services. Fowler prefers static "
                  "methods as its interface and does not let that make its data static: the "
                  "data may be global to the process, to a thread or to a session, and a "
                  "connection is thread data, held in thread-local storage behind the same "
                  "static method. The book's thread-safe example is Matt Foemmel's and "
                  "Fowler's. He is uncomfortable with it all the same, because a Registry is "
                  "still global data: pass the object as a parameter if you can, and he "
                  "turns to a Registry when the parameter would not be needed 90 percent of "
                  "the time by the calls it passes through, the book's figure. Any global "
                  "data, he ends, is &ldquo;guilty until proven innocent&rdquo;."),
            ("p", "The lesson's snippet takes its connection as a parameter, the choice "
                  "Fowler prefers. It prepares one INSERT, and for each line of an order it "
                  "sets the three placeholders and calls `addBatch`, which queues the "
                  "statement instead of sending it; `executeBatch` then sends every queued "
                  "statement in one call."),
            ("code", _lines(SAVE_LINES_BATCH)),
            ("p", "Now the arithmetic. The lab treats the database as the far end of a "
                  "round trip. Each record is one batch and the statements it carries; "
                  "sent one at a time, every statement pays the latency and its work, n·"
                  "(latency + work); batched, each batch pays the latency once and the "
                  "work is the same, m·latency + n·work. Its six tiles are the round trips "
                  "each way, the two times, the share of the one-at-a-time time spent "
                  "waiting, and the ratio of the two times. The panel and banner use the "
                  "path's word for remote calls, calling a batch a coarse-grained call and a "
                  "statement a fine-grained one; the tile labels say statements and batches. Holding the work the same is the lab's "
                  "assumption: a real driver may also save some parsing and commit work."),
            ("p", "In <code>save-an-order</code> a save makes 1 insert for the order, 12 for "
                  "its lines and 12 stock updates, with an illustrative 2 ms latency and 0.5 "
                  "ms of work a statement. One at a time that is 25 round trips and 125/2 = "
                  "62.50 ms, of which 4/5 = 80% is waiting; in 3 batches it is 37/2 = 18.50 "
                  "ms, 125/37 ≈ 3.4× faster. In <code>same-machine</code> the latency is 0.1 "
                  "ms: 15 ms against 64/5 = 12.80 ms, waiting only 1/6 ≈ 16.7% of the first, "
                  "and 75/64 ≈ 1.2×. Batching removes waits; where the waits are short it "
                  "has little to remove, and only your own measurement says which case you "
                  "are in."),
            ("h3", "Exercise"),
            ("ul", [
                "A save: `insert-invoice, 1; insert-items, 40`, one batch for the invoice "
                "and one for its items.",
                "Latency 3 ms; work 0.2 ms a statement.",
            ]),
            ("p", "Compute by hand the statements, the time one at a time and in batches, "
                  "the share of the first spent waiting, and how many times faster the "
                  "batches are. Check your figures in the lab afterwards."),
            ("p", "This ends the course on how the domain talks to the database. The next "
                  "course, Objects and Tables, begins with Chapter 3's behavioral problem "
                  "and the Unit of Work that answers it."),
        ],
        "lab": ("eakit", {
            "mode": "remote",
            "view": "calls",
            "fine_label": "statements",
            "coarse_label": "batches",
            "preset": "save-an-order",
            "presets": [
                {"id": "save-an-order",
                 "label": "Saving an order with 12 lines, 2 ms a round trip",
                 "ops": "insert-order, 1; insert-lines, 12; update-stock, 12",
                 "latencyMs": "2", "workMs": "0.5",
                 "expect": {"rrFineMs": "125/2 = 62.50", "rrCoarseMs": "37/2 = 18.50",
                            "rrSpeedup": "125/37 ≈ 3.4×"}},
                {"id": "same-machine",
                 "label": "The same save, 0.1 ms a round trip",
                 "ops": "insert-order, 1; insert-lines, 12; update-stock, 12",
                 "latencyMs": "0.1", "workMs": "0.5",
                 "expect": {"rrFineMs": "15", "rrCoarseMs": "64/5 = 12.80",
                            "rrSpeedup": "75/64 ≈ 1.2×"}},
            ],
            "panel_title": "What batching statements saves",
            "panel_intro": (
                "The database is the far end of the round trip. Each record is one batch, a "
                "coarse-grained call, and the statements it carries, each a fine-grained "
                "call. Sent one at a time every statement pays the latency; batched, each "
                "batch pays it once."
            ),
            "source": "every figure is illustrative",
        }),
        "steps_title": "Working out what batching saves",
        "steps_intro": "Four steps, the last of them on a save of your own.",
        "steps": [
            ("Count the statements",
             "Add up the statements of the save, n, and the batches they would go in, m."),
            ("Time them one at a time",
             "Multiply n by the latency plus one statement's work. Then multiply n by the "
             "latency alone, and divide by the first figure for the share spent waiting."),
            ("Time the batches",
             "Multiply m by the latency and add n times the work, then divide the first time "
             "by this one for how many times faster the batches are."),
            ("Count a save you know",
             "Take one save in a system you know that writes many rows. Count its "
             "statements, and find out from its log or its driver's settings whether they "
             "are sent one at a time or in batches; write both down."),
        ],
        "worked": {
            "title": "Saving an order with twelve lines",
            "intro": [
                "Work <code>save-an-order</code>: 25 statements in 3 batches, 2 ms a round "
                "trip and 0.5 ms of work each.",
            ],
            "lines": [
                "statements: 1 + 12 + 12, which is 25",
                "one at a time: 25 × (2 + 0.5), 62.5 ms",
                "batched: 3 × 2 + 25 × 0.5, 18.5 ms",
                "waiting, one at a time: 25 × 2, 50 ms",
                "share waiting: 50 / 62.5, 80 per cent",
                "62.5 / 18.5: about 3.4 times",
            ],
            "after": [
                "The work, 12.5 ms, is in both times. Batching took away 22 of the 25 waits, "
                "44 ms, and that is the whole difference.",
            ],
        },
        "quiz_title": "Connections, Registry and batches",
        "quiz": [
            {"q": "Take the exercise: 41 statements in 2 batches, 3 ms a round trip and 0.2 "
                  "ms of work a statement. What are the two times and the ratio?",
             "a": ["131.20 ms one at a time, 14.20 ms batched, about 9.2× faster",
                   "123 ms one at a time, 14.20 ms batched, about 8.7× faster",
                   "131.20 ms one at a time, 6.40 ms batched, about 20.5× faster",
                   "131.20 ms one at a time, 8.20 ms batched, 16× faster"],
             "c": 0,
             "why": "One at a time: 41 × (3 + 0.2) = 656/5 = 131.20 ms. Batched: 2 × 3 + 41 "
                    "× 0.2 = 71/5 = 14.20 ms. Waiting is 41 × 3 = 123 ms, 15/16 ≈ 93.8% of "
                    "the first time, and 656/71 ≈ 9.2×. 123 ms leaves out the work, 6.40 ms "
                    "pays the work once a batch instead of once a statement, and 8.20 ms "
                    "leaves out the batches' waits."},
            {"q": "When does Registry's When to Use It say Fowler turns to a Registry "
                  "instead of a parameter?",
             "a": ["Whenever an object is needed in more than one layer",
                   "Never, since a Registry is global data",
                   "When the object is immutable",
                   "When the parameter would not be needed 90 percent of the time by the "
                   "calls it passes through"],
             "c": 3,
             "why": "The book's figure: a parameter not needed 90 percent of the time is "
                    "what leads him to a Registry, though he calls it a last resort and "
                    "global data guilty until proven innocent. Immutable data is what makes "
                    "a process-wide singleton safe, which is a question of the Registry's "
                    "scope, not of whether to have one."},
            {"q": "What scope does Chapter 3 give the Registry that holds a database "
                  "connection, and why?",
             "a": ["Process scope, so that every thread shares one connection",
                   "Thread scope, because you do not want several threads using the same "
                   "connection",
                   "Session scope, so that a user keeps one connection between requests",
                   "No scope: the connection is a static field"],
             "c": 1,
             "why": "Database Connections asks for a thread-scoped Registry for exactly that "
                    "reason, and Registry shows it held in thread-local storage behind a "
                    "static method. A connection held across a user's requests would sit "
                    "open while they think, the opposite of closing it as soon as you are "
                    "done."},
            {"q": "What does Database Connections recommend tying a connection to?",
             "a": ["The garbage collector, which closes it once nothing refers to it",
                   "Each command, closing it after every statement",
                   "A transaction: open it when the transaction begins and close it at "
                   "commit or rollback",
                   "The connection pool's lifetime"],
             "c": 2,
             "why": "A transaction's end is visible, so it is easy to remember and to spot "
                    "when forgotten, and a Unit of Work fits it. The garbage collector "
                    "closes too late and is only a backup; closing after every command "
                    "would usually roll a transaction back."},
        ],
        "mistakes": [
            ("Thinking batching is faster because the database does less work",
             "The lab holds the work the same, 25 × 0.5 ms, and batching is still 125/37 ≈ "
             "3.4× faster on the lesson's first preset: it removes 22 of the 25 waits. Holding "
             "the work fixed is the lab's assumption, and a real driver may also save some "
             "parsing and commit work; but the saving the quotation points to is the round "
             "trips."),
            ("Thinking a Registry is a global variable, so it is always wrong",
             "Fowler's position is narrower. He is uncomfortable with any global data and "
             "calls a Registry a last resort: pass the object if you can. But he uses one "
             "when passing it would thread a parameter through calls that do not use it most "
             "of the time, and he scopes it to the thread or session, so that it is less "
             "global than it looks."),
            ("Building a connection pool as a matter of course",
             "Database Connections says most platforms already pool, behind an interface "
             "that looks like opening a connection, and that if you must pool yourself you "
             "should first check that it helps performance, since new connections keep "
             "getting cheaper to create."),
        ],
        "standard": (
            "Finish when you can work out what batching saves.",
            "Given groups of statements, a latency and a work time each, compute the "
            "one-at-a-time and batched times and the latency's share of the first."
        ),
        "note": (
            "The lab counts batching and nothing else in the lesson: where a connection "
            "lives, how it is pooled and whether a Registry holds it are read without a "
            "count. Its figures are illustrative, and it assumes each statement's work is "
            "the same whether or not it is batched."
        ),
    },
]
