"""Concurrency and Session State, lessons 4-7 -- offline locks and session state.

Fowler et al., Patterns of Enterprise Application Architecture (Addison-Wesley,
2002): Chapter 16, Offline Concurrency Patterns (Optimistic Offline Lock,
Pessimistic Offline Lock and Implicit Lock by David Rice, Coarse-Grained Lock
by Rice and Matt Foemmel); Chapter 6, Session State; and Chapter 17, Session
State Patterns. Pages in the comments are PDF pages of the operator's copy,
which has no printed page numbers; the lessons cite the book by chapter,
section and pattern only. Every quotation is copied from that copy and checked
with ea_quotes.py; every figure attributed to the book carries its PLAN
section S.2 id. The code is written for these lessons (PLAN section D.4,
verbatim): none of the book's listings is reproduced.
"""


def _lines(text):
    """A snippet constant as a code block's list of lines."""
    return text.split("\n")


# ---------------------------------------------------------------- snippets
# PLAN section D.4 and docs/enterprise-patterns/presets.py, verbatim.

OPTIMISTIC_SAVE = """\
// Saves only if nobody has changed the row since it was read; false
// tells the caller to reload the invoice and let the user try again.
boolean trySave(Connection db, Invoice inv) throws SQLException {
    PreparedStatement s = db.prepareStatement(
        "UPDATE invoice SET total = ?, version = version + 1"
        + " WHERE id = ? AND version = ?");
    s.setLong(1, inv.total());
    s.setLong(2, inv.id());
    s.setInt(3, inv.version());
    return s.executeUpdate() == 1;
}"""

GROUP_LOCK = """\
// Locks the order, not the line: one lock covers the group.
boolean tryEdit(Line line, String session) {
    String key = "order:" + line.orderId();
    String holder = owners.get(key);
    if (holder != null && !holder.equals(session)) {
        return false;
    }
    owners.put(key, session);
    return true;
}"""

STATELESS_HANDLER = """\
// Stateless: what a request needs arrives with it or is read
// from the database, so any server object can serve it.
class CartHandler {
    private final CartStore store;

    CartHandler(CartStore store) {
        this.store = store;
    }

    String handle(String cartId, String sku) {
        Cart cart = store.load(cartId);
        cart.add(sku);
        store.save(cart);
        return cart.summary();
    }
}"""

SERVER_SESSION = """\
// Server Session State: carts stay in server memory, keyed by
// the id the browser sends back with every request.
class Carts {
    private final Map<String, Cart> byId = new HashMap<String, Cart>();

    Cart forSession(String id) {
        Cart cart = byId.get(id);
        if (cart == null) {
            cart = new Cart();
            byId.put(id, cart);
        }
        return cart;
    }
}"""

# ---------------------------------------------------------------- exercises
# Each exercise's instance is PLAN section C's, never a preset's; its answer
# is in one quiz item's `why` only.

EXERCISE_POLICY = [
    "0, ana, read, budget;",
    "1, ben, read, budget;",
    "2, ana, edit, budget;",
    "5, ana, commit, -;",
    "6, ben, edit, budget;",
    "30, ben, commit, -;",
    "31, cy, read, budget;",
    "32, cy, edit, budget;",
    "40, cy, commit, -",
]

EXERCISE_ROOMS = [
    "0, ann, edit, room1;",
    "1, bo, edit, room2;",
    "2, cy, edit, room3;",
    "3, ann, commit, -;",
    "7, bo, commit, -;",
    "8, cy, commit, -",
]

_QUOTE_DISCOUNT = ("0, kim, read, discount; 0, kim, edit, quote; 1, lee, edit, discount; "
                 "2, lee, commit, -; 6, kim, commit, -")
_TWO_LINES = "0, kim, edit, line1; 1, lee, edit, line2; 4, kim, commit, -; 5, lee, commit, -"


LESSONS = [
    # ---------------------------------------------------------------- 6.4
    # Chapter 16, Optimistic Offline Lock, by David Rice, PDF pp. 374-381:
    # the pattern's opening, p. 374; How It Works, pp. 375-377; When to Use
    # It, p. 377. The examples (pp. 377-381) are pointed to, not used.
    # Quote: PDF p. 377 of the operator's copy, 17 words, ea_quotes.py OK;
    # Rice's words, in his pattern. Lesson total: 17 words.
    {
        "slug": "optimistic-offline-lock",
        "title": "Optimistic Offline Lock",
        "module": "Chapter 16 · Offline Concurrency Patterns",
        "one_line": "A version number in every row, checked and moved on by the update itself, turns a lost update into a failed save the caller can see.",
        "summary": (
            "David Rice's Optimistic Offline Lock, in Fowler's book: a version in each row, "
            "checked in the update's WHERE and incremented by it, so that a row count of zero "
            "means someone else committed first. Replay two clerks on one invoice, then a "
            "quote built from a discount someone else changed, and count the conflicts and the "
            "minutes of work each one discards."
        ),
        "key": [
            "a version in every row",
            "UPDATE only where the version still matches",
            "one row: committed; zero: someone was first",
            "check what was read, not only what was written",
            "suits a low chance of conflict",
            "failure is late, so the work is lost",
        ],
        "key_label": "The pattern in six lines",
        "concepts_intro": (
            "Three ideas make up the pattern as Rice describes it."
        ),
        "concepts": [
            ("Business transaction across system transactions",
             "A user's piece of work, such as editing an invoice over several screens, runs as "
             "several short database transactions. Between them the database cannot keep one "
             "session from overwriting another's work, so the application has to."),
            ("Version number",
             "A counter in each row, read with the row and kept in the session. The save "
             "updates the row only if the counter still has the value read, and adds one to it "
             "in the same statement."),
            ("Checking a read",
             "A session whose result depends on a record it only read can check that record's "
             "version at commit too. Without that, a change to the record it read goes "
             "unnoticed: an inconsistent read."),
        ],
        "read_title": "The pattern first, then the replay",
        "read_intro": (
            "Read Optimistic Offline Lock in Chapter 16, its opening, How It Works and When to "
            "Use It, in your own copy first; its examples are best read in the book. The lesson "
            "sets out the pattern and then replays it in the lab."
        ),
        "body": [
            ("p", "&ldquo;Optimistic concurrency management is appropriate when the chance of "
                  "conflict between any two business transactions is low.&rdquo; The words are "
                  "David Rice's, from When to Use It in his Optimistic Offline Lock, the first "
                  "pattern of Chapter 16 in Fowler's book. A pattern is a tool to look up "
                  "rather than an argument to follow, and this lesson reads it that way: the "
                  "problem, how it works, and when to use it. Read it in your own copy first."),
            ("p", "You have probably written a save that writes whatever the form sent back: "
                  "an `UPDATE` that sets the new total on the row with the invoice's id. Two clerks "
                  "open the invoice, both change it, and the second save wins without anyone "
                  "learning that the first one happened. That is Chapter 5's lost update, now "
                  "spread across requests. Rice's opening states the problem: once a business "
                  "transaction runs across a series of system transactions, the database alone "
                  "cannot keep the record data consistent, and lost updates and inconsistent "
                  "reads become likely."),
            ("p", "The pattern validates, before committing, that a session's changes do not "
                  "conflict with another session's. Rice likens a check that passes to obtaining "
                  "a lock, one that holds only within the system transaction that makes the "
                  "changes. The usual way is a version number in each record. The session keeps "
                  "the version it loaded with the rest of its state, and at commit compares it "
                  "with the version in the database; if they match, the changes and an "
                  "increment of the version are committed together, and any session still "
                  "holding the old number can no longer get the lock."),
            ("p", "With a relational database the comparison goes into the criteria of every "
                  "`UPDATE` and `DELETE`, so one statement both takes the lock and changes the "
                  "row. The session then reads the row count: 1 means success, 0 means someone "
                  "changed or deleted the record first, so the session rolls back its system "
                  "transaction and then gives up or resolves the conflict and tries again. Rice "
                  "also suggests recording who changed a record and when, so that the user can "
                  "be told; but he warns against checking with the modification time instead of "
                  "a version count, since the clocks of different machines cannot be trusted to "
                  "agree. A `WHERE` that compares every field is an alternative where no "
                  "version column can be added."),
            ("p", "Most implementations stop at the version in `UPDATE` and `DELETE`, Rice says, "
                  "and that misses the inconsistent read. His illustration is a session that "
                  "computes a charge from a value held in another record while a second session "
                  "changes that record; the first session wrote nothing there, so no check "
                  "fires. The remedy is to check the version of what was read as well, by adding "
                  "it to the change set or keeping a separate list of records to check. Rereading "
                  "a version works only at repeatable read or stronger; below that the version "
                  "must be incremented. Sometimes checking a condition rather than a version is "
                  "enough, and sometimes a Coarse-Grained Lock or a long transaction is the "
                  "simpler answer."),
            ("p", "Two further points close How It Works. Whether a changed record really is a "
                  "conflict is a business question as much as a technical one, and two sessions "
                  "adding to one collection may break a rule that the usual version check does not "
                  "see. And a "
                  "good merge makes the pattern far stronger, as source code control shows, "
                  "though a business system may need hundreds of kinds of merge. When to Use It "
                  "then gives the quotation's condition: when conflicts are likely, announcing "
                  "one only as the user finishes drives users away, and Pessimistic Offline Lock "
                  "suits. Rice still makes the optimistic lock the default, and asks you to look "
                  "for where it alone is not enough."),
            ("p", "The snippet is a save with the check built in. The `UPDATE` on lines 5 and 6 "
                  "sets the new total and moves the version on, but only for the row whose id "
                  "and version both match. The three `set` calls fill the three question marks "
                  "in order, and `executeUpdate` returns the number of rows changed. Line 10 "
                  "turns that count into the answer: true for one row, false for none, and "
                  "false is the caller's signal to reload the invoice and let the user try "
                  "again. The snippet leaves the system transaction around it, closing the statement and "
                  "moving its own copy of the version on after a save, to its caller."),
            ("code", _lines(OPTIMISTIC_SAVE)),
            ("p", "The lab is the timeline of lesson 2 with the scheme set to optimistic. In "
                  "<code>two-clerks</code> Kim reads the invoice at minute 0, at version 0. Lee "
                  "reads it at 1, edits at 2 and commits at 3, moving it to version 1. Kim edits "
                  "at 4 and saves at 20, and her update matches no row. The lab prints "
                  "&ldquo;1: lee&rdquo; committed, &ldquo;1: kim&rdquo; in conflict, and 20 "
                  "minutes redone, from her read at minute 0 to the failed save. The table's "
                  "version on each read or edit row is the record's version at that minute; "
                  "what the session holds is the version at its first read or edit, which is "
                  "why Kim's edit row shows 1 while she still holds the 0 she read."),
            ("p", "The other two presets share a timeline: Kim reads a discount and edits a quote "
                  "computed from it at minute 0, Lee edits the discount at 1 and commits at 2, and "
                  "Kim commits at 6. The last control, which checks the records only read, "
                  "makes the difference. In <code>inconsistent-read</code> it is set to no: the "
                  "lab prints &ldquo;2: lee, kim&rdquo; committed, &ldquo;0: none&rdquo; in "
                  "conflict and 0 minutes redone. Both saves succeed, and Kim's quote is "
                  "built on a discount that no longer exists. In <code>check-the-read</code> it is "
                  "set to yes: &ldquo;1: lee&rdquo; committed, &ldquo;1: kim&rdquo; in conflict, "
                  "6 minutes redone."),
            ("p", "Both of the pattern's limits are in those figures. A version check on what a "
                  "session writes catches the clerks' collision and misses the discount, which only "
                  "a check on reads finds. And the check finds a conflict at the last possible "
                  "moment: on the lesson's illustration Kim loses twenty minutes in one case and "
                  "six in the other. The pattern is cheap to build and costs nothing while "
                  "conflicts are rare; each conflict is paid for in someone's lost work, which "
                  "is why Rice makes the chance of conflict the condition for using it."),
            ("h3", "Exercise"),
            ("code", EXERCISE_POLICY),
            ("p", "Three users edit one budget, and the scheme is optimistic. Replay it by hand: "
                  "for each user, write the version seen and the version at commit, say who "
                  "commits and whose save fails, and how many minutes of work the failure "
                  "discards."),
            ("p", "Rice's other answer finds out early instead of late, by refusing the second "
                  "session at the start. The next lesson, Pessimistic and Coarse-Grained Locks, "
                  "reads it with the lock that covers a group of records at once."),
        ],
        "lab": ("eakit", {
            "mode": "lock",
            "view": "timeline",
            "preset": "two-clerks",
            "scheme": "optimistic",
            "presets": [
                {"id": "two-clerks",
                 "label": "Two clerks save one invoice",
                 "events": "0, kim, read, invoice; 1, lee, read, invoice; 2, lee, edit, invoice; "
                           "3, lee, commit, -; 4, kim, edit, invoice; 20, kim, commit, -",
                 "expect": {"olCommitted": "1: lee", "olConflicts": "1: kim", "olRedo": "20"}},
                {"id": "inconsistent-read",
                 "label": "A quote built from a discount Lee changes, reads not checked",
                 "events": _QUOTE_DISCOUNT,
                 "checkReads": "no",
                 "expect": {"olCommitted": "2: lee, kim", "olConflicts": "0: none", "olRedo": "0"}},
                {"id": "check-the-read",
                 "label": "The same, with the discount's version checked at commit",
                 "events": _QUOTE_DISCOUNT,
                 "checkReads": "yes",
                 "expect": {"olCommitted": "1: lee", "olConflicts": "1: kim", "olRedo": "6"}},
            ],
            "panel_title": "Version checks at commit",
            "panel_intro": (
                "Each event is a minute, a session, an action and a record. Every record has a "
                "version from 0, and each commit moves on the versions of what it edited. A "
                "commit conflicts when something it edited has moved since the session saw it, "
                "and, with reads checked, something it only read. The timelines are "
                "illustrative."
            ),
        }),
        "steps_title": "Replaying an optimistic lock",
        "steps_intro": "Four steps, the last of them on a table of your own.",
        "steps": [
            ("Record the version at first sight",
             "For each session, write the version of each record at its first read or edit. "
             "Every record starts at 0."),
            ("Move the version on at each commit",
             "When a commit succeeds, add one to the version of every record the session "
             "edited. A failed commit moves nothing."),
            ("Check each commit",
             "A commit fails if a record it edited, or with reads checked a record it read, is "
             "no longer at the version the session saw. Its redo is the minutes from the "
             "session's first event to the failed commit."),
            ("Do it on a table of your own",
             "Pick one table in a system you know that two users update. Check whether it has "
             "a version column and whether its update's WHERE uses it, and write down what the "
             "second of two simultaneous saves does."),
        ],
        "worked": {
            "title": "Two clerks, one invoice",
            "intro": [
                "The preset two-clerks, worked by hand.",
            ],
            "lines": [
                "minute 0: Kim reads, sees version 0",
                "minute 1: Lee reads, sees version 0",
                "minute 3: Lee saves; version 0 matches",
                "the invoice moves to version 1",
                "minute 20: Kim saves with version 0",
                "no row has version 0: zero rows",
                "Kim redoes 20 − 0, which is 20 minutes",
            ],
            "after": [
                "In the snippet's terms, Lee's executeUpdate returned 1 and Kim's returned 0, so "
                "trySave told Kim's caller false. What the caller does next, reload and let Kim "
                "redo the work, is the twenty minutes.",
            ],
        },
        "quiz_title": "Versions, conflicts and the pattern's limits",
        "quiz": [
            {"q": "Work the exercise, optimistic: ana reads the budget at 0, edits at 2 and "
                  "commits at 5; ben reads at 1, edits at 6 and commits at 30; cy reads at 31, "
                  "edits at 32 and commits at 40. What happens?",
             "a": ["ana and cy commit; ben conflicts at minute 30 and redoes 29 minutes",
                   "ana and cy commit; ben conflicts at minute 30 and redoes 24 minutes",
                   "ana commits; ben and cy both conflict",
                   "All three commit, each in turn"],
             "c": 0,
             "why": "ben saw version 0 at minute 1; ana's commit at 5 moved the budget to 1, so "
                    "ben's save at 30 fails, and his redo runs from his first event, 30 − 1 = 29 "
                    "minutes, not from his edit at 6. cy first reads at 31, after ana's commit, "
                    "and sees version 1; ben's failed save moved nothing, so cy's commit at 40 "
                    "succeeds. All three committing is what happens with no control at all."},
            {"q": "Lee has saved the invoice, moving it to version 1. Kim's session still holds "
                  "version 0 and calls trySave. What does executeUpdate return, and what does "
                  "trySave return?",
             "a": ["1, and true, so Kim's total replaces Lee's",
                   "It throws an exception, so trySave never returns",
                   "0, and true, since the statement itself ran without error",
                   "0, and false, so the caller must reload the invoice"],
             "c": 3,
             "why": "The WHERE asks for the row whose id matches and whose version is 0, and "
                    "no such row exists any more, so the update changes no rows and returns 0. "
                    "Line 10 compares that with 1 and returns false. A row count of zero is the "
                    "signal, not an error: nothing is thrown."},
            {"q": "In inconsistent-read, Kim's quote depends on a discount that Lee changes and "
                  "commits while Kim works. Kim checks only the records she edited. What "
                  "happens at her commit?",
             "a": ["It conflicts, because the discount's version moved",
                   "It is refused a lock on the discount",
                   "It succeeds, and the quote is built on the old discount",
                   "It waits for Lee's commit, then rereads the discount"],
             "c": 2,
             "why": "Kim edited only the quote, whose version nobody changed, so the check "
                    "passes and both sessions commit (&ldquo;2: lee, kim&rdquo;). Only checking "
                    "the version of the discount she read, as in check-the-read, turns this into a "
                    "conflict. There are no locks to refuse under an optimistic scheme, and no "
                    "waiting."},
            {"q": "Why does Rice advise against using the modification time instead of a "
                  "version count for the check?",
             "a": ["A timestamp cannot appear in the WHERE clause of an UPDATE",
                   "Clocks cannot be trusted, least of all on several servers",
                   "Timestamps take more space in each row than counters do",
                   "The database reorders rows that carry equal timestamps"],
             "c": 1,
             "why": "How It Works rules out the modification time for the check because "
                    "machine clocks cannot be relied on, and on several servers they will not "
                    "agree. Recording who changed a "
                    "record and when is still useful, for telling the user."},
        ],
        "mistakes": [
            ("Thinking a version check catches every conflict",
             "It catches a conflict on what the session writes. Rice's point is that most "
             "implementations stop there and miss the inconsistent read: a session whose result "
             "depends on a record it only read. On the lesson's illustration Kim's quote is "
             "computed from a discount Lee changed, and the check passes unless the discount's version "
             "is checked too; with the read checked, Kim's save fails."),
            ("Thinking optimistic locking costs nothing",
             "It costs nothing while nobody conflicts, and then it costs the whole of the "
             "failed session's work, discovered at the end. On two-clerks Kim loses twenty "
             "minutes. That is why Rice makes a low chance of conflict the condition for the "
             "pattern, and points to Pessimistic Offline Lock when a conflict is likely or too "
             "expensive."),
            ("Treating a zero row count as a database error",
             "An update that changes no rows looks like a failure to log and move past. In this "
             "pattern it is the lock refusing: another session committed first, and the "
             "business transaction must roll back its system transaction and then abort or "
             "resolve the conflict and retry. Code that ignores the count has a version column "
             "and still loses updates."),
        ],
        "standard": (
            "Finish when you can replay an optimistic lock by hand.",
            "Given a timeline, state which commits fail their version check, how many minutes "
            "of work each failure discards, and what checking the records only read would "
            "change."
        ),
        "note": (
            "The lab checks whole records, as a version column does, and it cannot see a "
            "conflict that is only a business rule, such as two sessions each adding to one "
            "collection, which Rice notes the usual version check does not prevent. It does not model merging, "
            "which would turn a conflict into less lost work. Whether a changed record is a "
            "real conflict is a question about your domain."
        ),
    },
    # ---------------------------------------------------------------- 6.5
    # Chapter 16: Pessimistic Offline Lock, by David Rice, PDF pp. 382-390
    # (How It Works pp. 383-385, the lock taken before loading p. 384, When
    # to Use It p. 385); Coarse-Grained Lock, by Rice and Matt Foemmel,
    # pp. 391-399 (When to Use It p. 393); Implicit Lock, by Rice,
    # pp. 400-403. Examples pointed to, not used.
    # Quote: PDF p. 382 of the operator's copy, 9 words, ea_quotes.py OK;
    # Rice's words, in his pattern. Implicit Lock's sentence on locking an
    # item everywhere: PDF p. 400, 12 words, ea_quotes.py OK. Lesson total:
    # 21 words.
    # F18, PDF p. 385 of the operator's copy: a business transaction might
    # take 20 minutes.
    {
        "slug": "pessimistic-and-coarse-grained-locks",
        "title": "Pessimistic and Coarse-Grained Locks",
        "module": "Chapter 16 · Offline Concurrency Patterns",
        "one_line": "Lock before you load, refuse rather than wait, and lock a group with one lock when the group is what the business edits.",
        "summary": (
            "David Rice's Pessimistic Offline Lock, his Coarse-Grained Lock with Matt Foemmel, "
            "and his Implicit Lock, in Fowler's book: lock before loading, refuse at once "
            "rather than wait, cover a group with one lock, and let the framework take the "
            "locks nobody may forget. Replay two edits to the lines of one order with a lock "
            "per line and with one lock for the order."
        ),
        "key": [
            "lock before you load the data",
            "refused: abort at once, never wait",
            "one lock for the group, on its root",
            "coarser: fewer locks, less concurrency",
            "let the framework take the locks",
        ],
        "key_label": "The three patterns in five lines",
        "concepts_intro": (
            "Three terms from the three patterns."
        ),
        "concepts": [
            ("Lock manager",
             "The one place that grants or refuses locks: little more than a table from each "
             "locked item to its owner, the session. It may be in memory or a database table, "
             "and business transactions talk only to it."),
            ("Coarse-grained lock",
             "One lock that covers a group of objects edited together, such as an order and its "
             "lines. It is taken on a version the members share, or on the group's root, so a "
             "session locks the group without finding and locking every member."),
            ("Implicit lock",
             "Locking that the framework or a layer supertype does for the developer, so that "
             "no business transaction can forget a lock it must take. A layer supertype is a "
             "class every class of a layer inherits from."),
        ],
        "read_title": "The patterns first, then the replay",
        "read_intro": (
            "Read Pessimistic Offline Lock, Coarse-Grained Lock and Implicit Lock in Chapter 16, "
            "their How It Works and When to Use It, in your own copy first; the examples are "
            "best read in the book. The lesson sets out the three patterns and then replays "
            "locks on an order's lines."
        ),
        "body": [
            ("p", "&ldquo;Pessimistic Offline Lock prevents conflicts by avoiding them "
                  "altogether.&rdquo; The words are David Rice's, from his Pessimistic Offline "
                  "Lock in Chapter 16 of Fowler's book. This lesson reads it with the two "
                  "patterns that make it easier to live with, Coarse-Grained Lock, by Rice and "
                  "Matt Foemmel, and Implicit Lock, by Rice. They are tools, read as tools: what "
                  "each does and when to reach for it. Read them in your own copy first."),
            ("p", "Why prevent rather than detect? With an optimistic lock, Rice says, when "
                  "several people work on the same data one commits and the others fail, and "
                  "they find out only at the end, after doing all the work. On long business "
                  "transactions that soon makes a system unpopular. A pessimistic lock makes the "
                  "business transaction lock the data before touching it, and in return a session "
                  "that has started can usually expect to finish."),
            ("p", "How It Works has three parts. First, the kind of lock. An <em>exclusive "
                  "write lock</em> is needed only to edit, and ignores reading. An "
                  "<em>exclusive read lock</em> is needed even to load the record, for when a "
                  "transaction must always have the latest data, and it restricts concurrency "
                  "severely. A <em>read/write lock</em> combines them: many readers or one "
                  "writer. Rice asks you to weigh concurrency, the business's needs and the "
                  "complexity of the code, and to choose a scheme the domain's analysts can "
                  "understand; a poor choice, such as locking every record, can leave a "
                  "multi-user system behaving much like a single-user one. Second, the <em>lock manager</em>: a "
                  "table from locks to owners, in memory or in the database, exactly one of it, "
                  "and, once the servers are clustered, probably in the database, since a table "
                  "in one server's memory works only if it is pinned to that server."),
            ("p", "Third, the protocol. Take the lock before loading the data, since a lock is "
                  "of little use without the assurance that you have the latest version, and "
                  "lock the record's id, which lets you lock before you load. Release locks when "
                  "the business transaction completes. If a lock cannot be had, abort; the user "
                  "should accept that, because it happens early, and the earlier the better, "
                  "ideally before any work begins. Do not wait for a lock: a business "
                  "transaction might take twenty minutes, in the book's example, so the lock "
                  "manager should refuse at once, which also takes deadlock off the table. "
                  "Give abandoned sessions a timeout. Use the pattern where conflicts are likely "
                  "or too costly, as a complement to Optimistic Offline Lock rather than on every "
                  "record, and weigh a long transaction too, which may do no more harm and be "
                  "easier to program; load test before choosing."),
            ("p", "Coarse-Grained Lock answers the cost of many locks. Locking each object of a "
                  "group means finding and perhaps loading every member, and with pessimistic "
                  "locks a large lock set crowds the lock table. One lock for the group removes "
                  "both. With optimistic locks the members share one version, the same version "
                  "and not merely an equal one, so that moving it on locks them all; with "
                  "pessimistic locks they share a lockable token. For an aggregate, a cluster "
                  "treated as a unit for changes in Evans and Siegel's sense, the authors offer "
                  "a root lock: lock the root, and every member is locked. The first reason to "
                  "use it, they say, is the business's requirement that the group be edited as "
                  "one; cheaper locking is a second, and they warn against inventing unnatural "
                  "relationships to get it."),
            ("p", "Implicit Lock starts from the fact that a locking scheme with one gap is no "
                  "scheme: forget one line that takes a lock and the whole scheme is useless, "
                  "and such a mistake is hard to find by testing. In Rice's words, &ldquo;if an "
                  "item might be locked anywhere it must be locked everywhere.&rdquo; So the "
                  "framework or a "
                  "layer supertype takes the locks nobody may forget: versions for an "
                  "optimistic scheme, the locks needed to load data for a pessimistic one. The "
                  "write locks are the exception, because an implicit point to take them gives "
                  "no promise of failing early; the framework instead checks at commit that the "
                  "lock was taken, and throws if not. He recommends the pattern for all but the "
                  "simplest applications."),
            ("p", "The snippet is a root lock in miniature. `tryEdit` does not lock the line it "
                  "is given: line 3 builds a key from the line's order, so every line of one "
                  "order asks for the same lock. `owners` stands for the lock manager's table, a "
                  "map from key to session declared elsewhere. A key another session holds "
                  "refuses the edit at once, on line 6; there is no waiting. A real lock manager "
                  "must also serialize access to that table, as Rice requires, so that two "
                  "sessions cannot both find the key free; the snippet leaves that, like "
                  "releasing the lock at commit, to the code around it."),
            ("code", _lines(GROUP_LOCK)),
            ("p", "The lab is the timeline again, with the scheme set to pessimistic and one "
                  "more input, the groups: a list of `record=group` pairs, where a record not "
                  "listed is its own group and the lock is taken on the group. These timelines "
                  "have no reads, so each lock is taken at the edit, which is also the load. In "
                  "<code>line-locks</code> Kim edits line1 at minute 0 and Lee edits line2 at "
                  "1, and they commit at 4 and 5. With a lock per line the lab prints &ldquo;2: "
                  "kim, lee&rdquo; committed, &ldquo;0: none&rdquo; refused, and at most 2 "
                  "locks held at once."),
            ("p", "In <code>order-lock</code> both lines belong to one order, `line1=order9` and "
                  "`line2=order9`. Now the lab prints &ldquo;1: kim&rdquo; committed, &ldquo;1: "
                  "lee&rdquo; refused, and at most 1 lock: Lee's edit at minute 1 asks for the "
                  "order that Kim's session holds. Lee is refused although the two lines are "
                  "different rows. That is the coarse lock's cost. It is also its point, if the "
                  "order has a rule that spans its lines, such as a total or a credit limit: "
                  "with a lock per line, two sessions can each make a change that keeps the rule "
                  "and together break it."),
            ("p", "The preset <code>optimistic-groups</code> keeps the groups and switches the "
                  "scheme, which makes the order a shared version. The lab prints &ldquo;1: "
                  "kim&rdquo; committed and &ldquo;1: lee&rdquo; in conflict, with 4 minutes "
                  "redone: Lee works from minute 1 and learns at her commit at minute 5 that "
                  "Kim's commit moved the order's version. The grouping protects the order "
                  "either way; the scheme decides whether Lee is told at the start or at the "
                  "end."),
            ("h3", "Exercise"),
            ("code", EXERCISE_ROOMS),
            ("p", "Three people edit three rooms, with pessimistic locks on floors: "
                  "`room1=floor1; room2=floor1; room3=floor2`. Replay it by hand: say who "
                  "commits, who is refused and at which minute, how many minutes of work the "
                  "refusal discards, and the most locks held at once."),
            ("p", "Every lock in this lesson protects the record data; the next question is "
                  "where the data a session has not yet committed should live. The next lesson, "
                  "The Value of Statelessness, opens Chapter 6 with it."),
        ],
        "lab": ("eakit", {
            "mode": "lock",
            "view": "timeline",
            "preset": "line-locks",
            "events": _TWO_LINES,
            "presets": [
                {"id": "line-locks",
                 "label": "Kim and Lee edit two lines of one order, a lock per line",
                 "scheme": "pessimistic",
                 "expect": {"olCommitted": "2: kim, lee", "olRefused": "0: none", "olPeakLocks": "2"}},
                {"id": "order-lock",
                 "label": "The same edits, one lock for the order",
                 "scheme": "pessimistic",
                 "groups": "line1=order9; line2=order9",
                 "expect": {"olCommitted": "1: kim", "olRefused": "1: lee", "olPeakLocks": "1"}},
                {"id": "optimistic-groups",
                 "label": "The same edits, one shared version for the order",
                 "scheme": "optimistic",
                 "groups": "line1=order9; line2=order9",
                 "expect": {"olCommitted": "1: kim", "olConflicts": "1: lee", "olRedo": "4"}},
            ],
            "panel_title": "A lock per record, or one for the group",
            "panel_intro": (
                "Each event is a minute, a session, an action and a record; the groups map "
                "records to the group their lock or version belongs to. A pessimistic lock is "
                "refused at once, never waited for. The timelines are illustrative."
            ),
        }),
        "steps_title": "Replaying a pessimistic lock",
        "steps_intro": "Four steps, the last of them on an aggregate of your own.",
        "steps": [
            ("Map each record to its group",
             "Write down the group for every record the timeline touches. A record not listed "
             "is a group of its own, and the lock or version belongs to the group."),
            ("Take each lock at the load",
             "Walk the events in order. A session takes its group's lock at its first read or "
             "edit of a group it will edit; if another session holds that lock, the session "
             "is refused there, and its later events never happen."),
            ("Release at commit and count",
             "A commit releases the session's locks. Count the sessions that committed and "
             "were refused, the most locks held at any moment, and the minutes from each "
             "refused session's first event to its refusal."),
            ("Do it on an aggregate of your own",
             "Pick one aggregate in a system you know, such as an order and its lines or a "
             "document and its sections. Write down what is locked when one part is edited, "
             "and one rule that spans the parts."),
        ],
        "worked": {
            "title": "Two lines, one order",
            "intro": [
                "The preset order-lock, worked by hand.",
            ],
            "lines": [
                "groups: line1 and line2 are order9",
                "minute 0: Kim edits line1, locks order9",
                "minute 1: Lee edits line2, asks for order9",
                "order9 is held by Kim: Lee is refused",
                "Lee redoes 1 − 1, which is 0 minutes",
                "minute 4: Kim commits, releases order9",
                "most locks held at once: 1",
            ],
            "after": [
                "With a lock per line, line-locks, both commit and two locks are held at minute "
                "1. The coarse lock trades that concurrency for protection of anything that "
                "depends on both lines together.",
            ],
        },
        "quiz_title": "Locks, groups and the patterns' rules",
        "quiz": [
            {"q": "Work the exercise, pessimistic, with groups room1=floor1, room2=floor1 and "
                  "room3=floor2: ann edits room1 at 0, bo room2 at 1, cy room3 at 2; they commit "
                  "at 3, 7 and 8. What happens?",
             "a": ["All three commit, since each edits a different room; at most 3 locks",
                   "ann commits; bo and cy are refused while floor1 is held; at most 1 lock",
                   "ann and cy commit; bo is refused at minute 1, losing nothing; at most 2 locks",
                   "ann and cy commit; bo is refused at minute 7, when he commits; at most 2"],
             "c": 2,
             "why": "ann's edit at minute 0 locks floor1. bo's edit at 1 asks for floor1 too, "
                    "and is refused there, at his first event, so he loses 1 − 1 = 0 minutes. "
                    "cy's room3 is on floor2, which nobody holds, so at minute 2 two locks are "
                    "held, floor1 and floor2, the most at any moment. All three would commit "
                    "with a lock per room. A refusal happens when the lock is asked for, not at "
                    "commit."},
            {"q": "Why does Rice's lock manager refuse a lock at once instead of making the "
                  "session wait?",
             "a": ["Because a refused session can retry at once and usually wins the second time",
                   "Because waiting cannot be programmed across several system transactions",
                   "Because the database already refuses every lock at once, so it must too",
                   "Because a lock may be held for twenty minutes, and waiting invites deadlock"],
             "c": 3,
             "why": "Across system transactions, Rice argues, nobody wants to wait for a lock "
                    "that a business transaction might hold for 20 minutes, in the book's "
                    "example; a wait needs timeouts and soon turns complicated; and failing "
                    "straight away means deadlock never has to be handled. Waiting is possible, "
                    "as SELECT FOR UPDATE shows; it is a bad idea here."},
            {"q": "Under Pessimistic Offline Lock, when does Rice say a business transaction "
                  "should generally acquire its lock?",
             "a": ["Before loading the data",
                   "When it first changes a field",
                   "Just before it commits",
                   "After loading the data, once it is sure it will edit"],
             "c": 0,
             "why": "There is little point, Rice says, in a lock without the assurance that you "
                    "have the latest version of what it locks, so generally acquire it before "
                    "loading the data; locking the id rather than the object makes that "
                    "possible. Taking it at the first change or at commit leaves the session "
                    "working on data that may already be stale."},
            {"q": "Which locks does Implicit Lock say the framework should not take implicitly?",
             "a": ["The locks needed to load data, which a developer might forget",
                   "The version checks of an optimistic scheme, kept in the SQL",
                   "The locks needed only to edit, checked for at commit instead",
                   "The release of every lock when the business transaction ends"],
             "c": 2,
             "why": "Rice lists loading locks, versions and releasing locks as mandatory tasks "
                    "the framework should do. Write locks are the exception: an implicit point to "
                    "take them, such as registering a changed object, cannot promise to fail "
                    "early, and they limit concurrency most. The framework should instead ensure "
                    "at commit that the lock was taken, and throw a concurrency exception if not."},
        ],
        "mistakes": [
            ("Thinking a finer lock is always better",
             "A lock per row allows the most concurrency, and that sounds like the whole story. "
             "It also protects the least: two sessions can each change one line of an order "
             "whose rule spans both lines, and each change passes on its own. On the lesson's "
             "illustration the lock per line lets Kim and Lee both commit; one lock for the "
             "order refuses Lee. Coarse-Grained Lock makes the business's grouping the reason "
             "to choose."),
            ("Making pessimistic locks wait",
             "A database lock usually waits, so an offline lock might as well. Rice's lock "
             "manager refuses at once and the business transaction aborts, because another "
             "session may hold the lock for twenty minutes, and because waiting brings timeouts "
             "and deadlock with it. Failing early is the pattern's promise to the user."),
            ("Leaving each lock to the developer who needs it",
             "Every business transaction could take its own locks. Implicit Lock's point is "
             "that one forgotten lock makes the whole scheme useless, and that the mistake is "
             "hard to find by testing. A record that some code locks has to be locked by all "
             "code that touches it, so the framework takes the locks that cannot be skipped."),
        ],
        "standard": (
            "Finish when you can replay a pessimistic lock on groups.",
            "Given a timeline and a grouping of records, state who is refused and when, the "
            "most locks held at once, and what the grouping changes against a lock per record."
        ),
        "note": (
            "The lab's lock is the exclusive write lock alone, taken at the first read or edit "
            "of a record the session will edit; it does not model exclusive read or read/write "
            "locks, timeouts for abandoned sessions, or a lock manager that is itself a "
            "bottleneck. Which records form a group is a question about your domain, which the "
            "groups input only states."
        ),
    },
    # ---------------------------------------------------------------- 6.6
    # Chapter 6, Session State (Fowler), opening, PDF p. 87; The Value of
    # Statelessness, p. 88.
    # Quote: PDF p. 88 of the operator's copy, 20 words, ea_quotes.py OK.
    # Lesson total: 20 words.
    # F19, PDF p. 88 of the operator's copy: a hundred users, a request of one
    # second every ten seconds; a hundred stateful objects, 90 percent idle,
    # against ten stateless ones fully employed.
    {
        "slug": "the-value-of-statelessness",
        "title": "The Value of Statelessness",
        "module": "Chapter 6 · Session State",
        "one_line": "A server object that keeps nothing between requests can serve anyone, so a few of them can do the work of one each for many idle users.",
        "summary": (
            "Chapter 6 opens with what a stateless server is, why it needs fewer objects, and "
            "why many sessions are stateful anyway. Work the book's thought experiment of a "
            "hundred users and see how the saving shrinks as users wait less between requests."
        ),
        "key": [
            "stateless: nothing kept between requests",
            "stateful objects: one a user",
            "stateless busy: users × service / think",
            "idle share: 1 − service / think",
            "a stateful session can use stateless servers",
        ],
        "key_label": "The section in five lines",
        "concepts_intro": (
            "Three terms the section uses, and the next lesson builds on."
        ),
        "concepts": [
            ("Stateless server object",
             "An object that keeps nothing between one request and the next. It may have fields "
             "and use them while it handles a request, but their values mean nothing when the "
             "next request arrives, so any such object can handle any request."),
            ("Stateful server object",
             "An object that keeps a client's data between requests, so every request of that "
             "client must reach that object, and the object waits, holding the data, while "
             "the user thinks."),
            ("Pooling",
             "Keeping a few interchangeable objects and handing each request to whichever is "
             "free. It works only for stateless objects, and it is where statelessness saves."),
        ],
        "read_title": "The section's argument first, then the arithmetic",
        "read_intro": (
            "Read the opening of Chapter 6, Session State, and its section The Value of "
            "Statelessness in your own copy first. The lesson sets out the argument and then "
            "does the section's arithmetic in the lab."
        ),
        "body": [
            ("p", "&ldquo;The shift from stateless to stateful is much more than three or four "
                  "letters at the end of the word.&rdquo; The sentence is from The Value of "
                  "Statelessness, the first section of Chapter 6, Session State, which Fowler "
                  "wrote alone. This lesson reads the chapter's short opening and that section; "
                  "it is a narrative, read as an argument. Read it in your own copy first."),
            ("p", "You may have written a handler that keeps something in a field between "
                  "calls: the last few pages a user looked at, a half-filled form, a cart. It "
                  "works until there are two servers, or a thousand users, and then the field "
                  "is the problem. Chapter 6 opens by tying this to the last chapter. The "
                  "difference between business and system transactions, Fowler says, also "
                  "decides where to keep the data a business transaction uses but has not yet "
                  "committed, and the stateless-against-stateful debate often hides the real "
                  "issue: some sessions are stateful by nature, and the question is what to do "
                  "with their state."),
            ("p", "What is a stateless server? Not an object with no fields; such objects are "
                  "rare, and arguably a bad design, since an object combines data and behaviour. "
                  "What people mean is an object that keeps no state between requests. It may "
                  "fill its fields while building one page, say a product's details looked up "
                  "from the database, and then those values are useless; the next request starts "
                  "afresh. Make it remember every product a client has viewed, a list that "
                  "must outlive the request, and it is stateful."),
            ("p", "Many people, Fowler says, regard stateful servers as a disaster, and he "
                  "explains why: the main issue is resources. He makes the case with a "
                  "thought experiment he calls completely unrealistic but helpful. A hundred "
                  "people want to know about books; handling a request takes one second; each "
                  "person sends one request every ten seconds, perfectly balanced. With a "
                  "stateful object per user, a hundred objects are needed and 90 percent of the "
                  "time they sit idle. With stateless objects, ten can do all the work, busy all "
                  "the time. Without state between calls it does not matter which object serves "
                  "a request, so they can be pooled; the more idle users, the more statelessness "
                  "is worth, and it fits the web, whose protocol is stateless."),
            ("p", "So should everything be stateless? Fowler's answer is that it should where "
                  "it can, and that many interactions are stateful by nature. The shopping cart must "
                  "be remembered for the whole session; that is a stateful business transaction, "
                  "so the session is stateful. A visitor who only browses has a stateless "
                  "session; one who buys has a stateful one, and the only way to avoid the "
                  "state, Fowler remarks, is to stay poor. The good news, he says, is that a stateless server "
                  "can carry a stateful session; and he adds that we may not want it to, which "
                  "the next lesson takes up."),
            ("p", "The snippet is a stateless handler for a stateful session. `CartHandler` has "
                  "a field, `store`, set once when it is built, and nothing else: each call to "
                  "`handle` loads the cart its id names, adds the item, saves the cart and "
                  "returns a summary. Between two calls the handler holds no cart, so any "
                  "handler in a pool can take the next request. The session's state has not "
                  "gone; it lives wherever `CartStore` keeps it, which is the next lesson's "
                  "subject."),
            ("code", _lines(STATELESS_HANDLER)),
            ("p", "The lab does the section's arithmetic. Its inputs are the users, the service "
                  "time of one request, and the time from one request of a user's to the next. "
                  "Its tiles are the stateful objects, one a user; the stateless objects busy "
                  "on average, users × service time / time between requests; the share of the "
                  "time a stateful object is idle, 1 − service / time between; and the users "
                  "one stateless object serves, time between / service. The preset "
                  "<code>hundred-users</code> is the book's thought experiment in "
                  "milliseconds, 100 users, 1,000 and 10,000: 100 stateful objects, 10 "
                  "stateless ones, &ldquo;9/10 = 90%&rdquo; idle, and 10 users to each "
                  "stateless object."),
            ("p", "In <code>busier</code> the same users ask every 2,000 ms instead. The "
                  "stateful count stays at 100, but now 50 stateless objects are busy on "
                  "average, the stateful ones are idle &ldquo;1/2 = 50%&rdquo; of the time, and "
                  "each stateless object serves 2 users. The saving is the idle time, and when "
                  "users wait less it shrinks, which is Fowler's point about idle users the "
                  "other way round. The experiment also assumes perfectly balanced "
                  "requests, and real ones bunch; the banner adds that the stateless figure is "
                  "an average, so a pool sized to it is too small at a peak."),
            ("p", "What the figures do not say is that the application kept less. The cart in "
                  "the snippet is the same size whether the handler is stateful or not. "
                  "Statelessness moves the state out of the server object, to the client or "
                  "the database, and the saving in objects is paid for in moving it, which is "
                  "what the next lesson counts."),
            ("h3", "Exercise"),
            ("ul", [
                "250 users.",
                "A request takes 400 ms to serve.",
                "Each user sends a request every 20 s, that is 20,000 ms.",
            ]),
            ("p", "Compute by hand the stateful objects needed, the stateless objects busy on "
                  "average, the share of the time a stateful object is idle, and the users one "
                  "stateless object serves."),
            ("p", "Statelessness leaves the question of where the cart lives. The next lesson, "
                  "Session State, reads Fowler's three answers and counts what each one moves "
                  "and holds."),
        ],
        "lab": ("eakit", {
            "mode": "session",
            "view": "objects",
            "preset": "hundred-users",
            "source": ("the book's thought experiment in Chapter 6, The Value of Statelessness, "
                       "for hundred-users; busier is illustrative"),
            "presets": [
                # F19, PDF p. 88 of the operator's copy.
                {"id": "hundred-users",
                 "label": "A hundred users, a one-second request every ten seconds (the book's illustration)",
                 "users": "100", "serviceMs": "1000", "thinkMs": "10000",
                 "expect": {"snStateful": "100", "snStateless": "10", "snIdle": "9/10 = 90%",
                            "snPerObject": "10"}},
                {"id": "busier",
                 "label": "The same users, a request every two seconds",
                 "users": "100", "serviceMs": "1000", "thinkMs": "2000",
                 "expect": {"snStateful": "100", "snStateless": "50", "snIdle": "1/2 = 50%",
                            "snPerObject": "2"}},
            ],
            "panel_title": "Stateful against stateless server objects",
            "panel_intro": (
                "Give the users, the time one request takes to serve, and the time from one of a "
                "user's requests to the next. The lab counts the objects a stateful design "
                "needs, the stateless objects busy on average, how idle a stateful object is, "
                "and how many users one stateless object serves."
            ),
        }),
        "steps_title": "Counting server objects",
        "steps_intro": "Four steps, the last of them on a service of your own.",
        "steps": [
            ("Count the stateful objects",
             "A stateful design needs one object a user, whatever the timings, because each "
             "user's requests must reach the object holding that user's state."),
            ("Find the share of time each is busy",
             "Divide the service time by the time between a user's requests. A stateful object "
             "is busy for that share and idle for the rest, 1 minus it."),
            ("Count the stateless objects",
             "Multiply the users by that busy share: that many stateless objects are busy on "
             "average. Its inverse, time between requests over service time, is the users one "
             "pooled object serves."),
            ("Do it on a service of your own",
             "Pick one service in a system you know. Write down what it keeps in memory between "
             "a user's requests, if anything, and where that state would go if the service "
             "kept none."),
        ],
        "worked": {
            "title": "A hundred users",
            "intro": [
                "The book's thought experiment, the preset hundred-users, worked by hand.",
            ],
            "lines": [
                "stateful: one object a user, 100",
                "busy share: 1,000 / 10,000 is 1/10",
                "idle share: 1 − 1/10 is 9/10",
                "stateless: 100 × 1/10 is 10 objects",
                "users an object serves: 10,000 / 1,000",
                "so each stateless object serves 10",
            ],
            "after": [
                "Ten objects is an average over perfectly balanced requests. In practice "
                "requests bunch, and a pool needs room above the average; the lab's figure is "
                "where to start the sizing, not where to end it.",
            ],
        },
        "quiz_title": "Objects, idle time and the section's claims",
        "quiz": [
            {"q": "Work the exercise: 250 users, a 400 ms request, a request from each user "
                  "every 20,000 ms. How many objects does each design need, how idle is a "
                  "stateful object, and how many users does a stateless object serve?",
             "a": ["250 stateful, 5 stateless, 98% idle, 50 users each",
                   "250 stateful, 5 stateless, 2% idle, 50 users each",
                   "250 stateful, 50 stateless, 98% idle, 5 users each",
                   "5 stateful, 250 stateless, 98% idle, 50 users each"],
             "c": 0,
             "why": "A stateful design needs one object a user, 250. The busy share is "
                    "400 / 20,000 = 1/50, so 250 × 1/50 = 5 stateless objects are busy on "
                    "average, a stateful object is idle 1 − 1/50 = 49/50 = 98% of the time, and "
                    "each stateless object serves 20,000 / 400 = 50 users. Two per cent is the "
                    "busy share; fifty is the users an object serves, not the objects."},
            {"q": "In Fowler's sense, is CartHandler, which has the field store, a stateless "
                  "server object?",
             "a": ["No: a stateless object has no fields",
                   "No: it saves the cart, so it keeps state",
                   "No: it keeps the cart between requests, in itself",
                   "Yes: it keeps nothing between requests"],
             "c": 3,
             "why": "The section says that a stateless server, as people use the term, is an "
                    "object that keeps no state between requests; it may well have fields. "
                    "CartHandler's store is set once and holds no client's data; the cart is "
                    "loaded and saved on each request. Saving the cart elsewhere is how the "
                    "session keeps its state while the handler keeps none."},
            {"q": "Does a stateless server mean a stateless session, by the section's account?",
             "a": ["Yes: with stateless servers there is nowhere to keep a cart",
                   "No: the state can be kept outside the server",
                   "Yes: HTTP is stateless, so every session on it is",
                   "No: a stateless server always has a stateful session"],
             "c": 1,
             "why": "Fowler's good news is that a stateless server can implement a stateful "
                    "session; the cart is still remembered, outside the server object. A session "
                    "that only browses is stateless whatever the server, and one that buys is "
                    "stateful whatever the server."},
            {"q": "On hundred-users, ten stateless objects are busy on average. Why might a pool "
                  "of exactly ten be too small?",
             "a": ["Because each stateless object can serve only one user at a time",
                   "Because requests bunch, so at a peak more than ten arrive at once",
                   "Because the stateful figure, 100, is the real requirement for this load",
                   "Because a stateless object is busy only 10% of the time, so more are needed"],
             "c": 1,
             "why": "Ten is users × service / time between requests, an average that assumes "
                    "requests evenly spread, as Fowler's experiment does. Requests bunch, and at a peak more than ten are in progress at once. "
                    "Each stateless object serves ten users on average, and is busy all the "
                    "time in the experiment."},
        ],
        "mistakes": [
            ("Thinking stateless means the application keeps no state",
             "The word suggests the state is gone. Fowler's stateless server keeps none between "
             "requests in the server object; the session can be as stateful as a full shopping "
             "cart, and the state goes to the client or the database, which is the next "
             "lesson. On the lesson's illustration the snippet's handler holds nothing between "
             "calls, and the cart survives in its store."),
            ("Thinking stateful is always worse",
             "The arithmetic favours stateless objects when users are idle, and Fowler reports "
             "that many people regard stateful servers as a disaster. But the "
             "cart has to live somewhere, and moving it out of the server object has its own "
             "costs, which the next lesson counts; and the saving itself depends on idle time: "
             "on busier the stateless pool is 50 objects against 100, not 10. The question the chapter asks is where the state should live, not "
             "whether to have it."),
            ("Thinking a stateless object has no fields",
             "A true stateless object, with no fields at all, is rare, and the section suggests "
             "it is usually a bad design. A stateless server object may fill fields while it "
             "handles a request; what makes it stateless is that their values mean nothing to "
             "the next request."),
        ],
        "standard": (
            "Finish when you can count the objects a load needs.",
            "Given users, a service time and the time between a user's requests, compute the "
            "stateful objects, the stateless objects busy on average and the share of the time "
            "a stateful object is idle."
        ),
        "note": (
            "The lab's stateless figure is an average over requests that arrive evenly, as in "
            "Fowler's experiment; it says nothing about peaks, queueing or how long a user "
            "waits, and it counts objects, not the memory or connections each holds. Sizing a "
            "real pool takes measurements of the real load."
        ),
    },
    # ---------------------------------------------------------------- 6.7
    # Chapter 6 (Fowler), Session State and Ways to Store Session State, PDF
    # pp. 89-91; Chapter 17: Client Session State, pp. 405-406; Server Session
    # State, pp. 407-409; Database Session State, pp. 410-411.
    # Quote: PDF p. 89 of the operator's copy, 10 words, ea_quotes.py OK.
    # Phrase "three Shakespeare plays worth": PDF p. 90, 4 words, ea_quotes.py
    # OK. Lesson total: 14 words.
    # F20, PDF p. 90 of the operator's copy: about a megabyte, sent as XML.
    # F21, PDF p. 408 of the operator's copy: twelve segments, rotated every
    # two hours; a session active for twenty-four hours is dropped.
    {
        "slug": "session-state",
        "title": "Session State",
        "module": "Chapter 17 · Session State Patterns",
        "one_line": "A session's state can live on the client, on the server or in the database, and each place moves or holds a different number of bytes.",
        "summary": (
            "Chapter 6 on what session state is and the three places to keep it, read with "
            "Chapter 17's three patterns: Client, Server and Database Session State. Count the "
            "bytes each one moves on every request and holds in memory, for the book's "
            "megabyte session and for a small cart."
        ),
        "key": [
            "client state: all of it, both ways, each time",
            "server or database: an id on the wire",
            "server memory: users × state",
            "database: read and write it each request",
            "an id always lives on the client",
        ],
        "key_label": "The three patterns in five lines",
        "concepts_intro": (
            "Three distinctions carry Chapter 6's second section and Chapter 17."
        ),
        "concepts": [
            ("Session state and record data",
             "Session state is the data of a business transaction still in progress, such as a "
             "cart, seen by that session only. Record data is the long-term data in the "
             "database, seen by every session. Session state becomes record data when it is "
             "committed."),
            ("Server affinity and session migration",
             "With affinity, every request of a session goes to the server that holds its "
             "state. With migration, any server can take any request, which balances the load "
             "and requires every server to reach the state."),
            ("Pending data",
             "Session state written into the database before it is committed, marked by a "
             "session id in the row or kept in separate pending tables, so that queries for "
             "record data do not see it."),
        ],
        "read_title": "The chapter's argument first, then the bytes",
        "read_intro": (
            "Read Chapter 6's section Session State, with Ways to Store Session State, and then "
            "Chapter 17's Client Session State, Server Session State and Database Session State, "
            "in your own copy first. The lesson sets out the argument and the patterns, then "
            "counts bytes in the lab."
        ),
        "body": [
            ("p", "&ldquo;Session state needs to be committed to become record data.&rdquo; The "
                  "sentence is from Chapter 6's second section, Session State, and it is the "
                  "distinction the rest of the chapter, and Chapter 17's three patterns, turn on. "
                  "This lesson reads the section as an argument and the patterns as tools. Read "
                  "them in your own copy first."),
            ("p", "The cart is <em>session state</em>: data that matters only to one session, "
                  "inside a business transaction, apart from other sessions. <em>Record "
                  "data</em> is the long-term data in the database that every session sees. "
                  "Because session state lives inside a business transaction, Fowler says, it "
                  "has the transaction's properties, with consequences people miss. It need not "
                  "be valid while it is being worked on; a half-filled form may break the "
                  "rules until it is committed. It must be isolated, with the inconsistent read "
                  "of Chapter 5 as the danger. And a cache is not session state, since losing a "
                  "cache loses only speed."),
            ("p", "Fowler divides the places to keep it into three, with blurred edges. "
                  "<em>Client Session State</em> keeps it on the client: in the URL, a cookie, a "
                  "hidden field of a form, or objects of a rich client. <em>Server Session "
                  "State</em> keeps it on the server, in memory or serialized somewhere more "
                  "durable, perhaps a table keyed by session id. <em>Database Session "
                  "State</em> breaks it into tables and fields in the database, like record "
                  "data. Then he weighs them. Client state crosses the wire with every request; "
                  "a few fields are no burden, but in one application of his it came to about a "
                  "megabyte, &ldquo;three Shakespeare plays worth&rdquo;, as one of the team put "
                  "it, admittedly as XML. Data sent to a client can also be edited by a "
                  "malicious user unless it is encrypted."),
            ("p", "The other questions follow. Database Session State must work hard to keep "
                  "pending data apart from record data. A cluster raises migration against "
                  "affinity, and Server Session State is awkward to migrate, since often only "
                  "the server that holds it can find it; affinity by IP address can tie every "
                  "user behind one proxy to one server. Speed differs, with a retail site's many "
                  "idle, small sessions suiting the database and a leasing system's heavy ones "
                  "the server. When a user walks away, client state is easily forgotten and the "
                  "others need timeouts; when something crashes, Database Session State copes "
                  "best. Server Session State is usually the least work to build. Whatever else "
                  "you use, at least a session id lives on the client. Fowler's preference is "
                  "Server Session State, with its memento stored remotely to survive a crash, "
                  "and Client Session State for ids and very small data."),
            ("p", "Chapter 17 gives each pattern its page. Client Session State sends the whole "
                  "state with each request and gets it back with each response, often as a Data "
                  "Transfer Object, which lets the server be completely stateless. URL "
                  "parameters suit a couple of items; hidden fields can be read in the page "
                  "source; cookies are limited in size, can be turned off and stay within one "
                  "domain. For a rich client, Fowler would rather drink Budweiser than keep the "
                  "state in the fields of the interface. The pattern supports clustering and "
                  "failover well; its costs grow with the data; and anything that comes back "
                  "must be validated again, since it may have been altered. A random session id "
                  "makes stealing another's session harder."),
            ("p", "Server Session State, in its simplest form, is a map in memory from session id "
                  "to session object, and it assumes enough memory, one server, and that losing "
                  "a session when the server fails is acceptable. Lifting those assumptions means "
                  "serializing the state to a memento, binary or text, kept locally or on a "
                  "shared store, perhaps a session table in the database holding a Serialized "
                  "LOB, the point where the boundary with Database Session State is, Fowler "
                  "admits, arbitrary. Deleting expired rows with a daemon can cause heavy "
                  "contention for that table; Kai Yu described to Fowler a scheme "
                  "that split the session table into twelve segments and cleared the oldest "
                  "every two hours, which dropped any session active for twenty-four hours, "
                  "rarely enough not to matter. Its appeal is simplicity; its cost comes with "
                  "clustering and failover."),
            ("p", "Database Session State pulls what a request needs from the database, does the "
                  "work and saves it back, with at least an id kept on the client. Its problem "
                  "is keeping pending data out of everyone else's queries, such as a "
                  "sales report: a session id in each row, which every query must then filter, or "
                  "pending tables cloned from the real ones. Integrity and validation rules often "
                  "differ for pending data, abandoned sessions need a cleanup, and rolling back "
                  "updates to existing records is awkward. It gains stateless servers, pooling "
                  "and easy clustering, and pays for reading and writing the data on every "
                  "request; caching saves the reads, not the writes."),
            ("p", "The snippet is Server Session State at its simplest: a map in memory from the "
                  "id the browser sends to the session's cart, creating a cart the first time "
                  "an id is seen. Only this server can find these carts, and a crash loses them: "
                  "two of the three assumptions Chapter 17 names. In a thread-per-request server "
                  "the map is also shared between threads, which Chapter 5 says must be "
                  "synchronised. Chapter 17 names the platform support of its day, the HTTP "
                  "session and stateful session beans in Java and the built-in session state of "
                  ".NET, which does this for you."),
            ("code", _lines(SERVER_SESSION)),
            ("p", "The lab counts bytes. Its inputs are the users, the size of one session's "
                  "state, the requests in a session and the size of a session id. Its tiles are "
                  "the bytes client state puts on the wire for one request, twice the state "
                  "because it goes out and comes back, and for a whole session; the bytes a "
                  "request carries with server or database state, the id alone; the bytes "
                  "server state holds in memory, users × state; and the bytes database state "
                  "reads and writes a request, twice the state. The preset "
                  "<code>a-megabyte</code> takes the book's session of about a megabyte, for "
                  "100 users, 20 requests and a 32-byte id: 2,000,000 bytes a request, "
                  "40,000,000 a session, 32 with the id, 100,000,000 in memory and 2,000,000 "
                  "through the database a request. The table below the tiles is one user's "
                  "request; the memory tile multiplies by the users."),
            ("p", "In <code>a-small-cart</code> the state is 2,000 bytes: 4,000 a request, 80,000 "
                  "a session, still 32 with the id, 200,000 in memory and 4,000 through the "
                  "database. Every figure but the id scales with the state, which is why Fowler "
                  "keeps client state for small data. The database's figure is the same as the "
                  "client's, but it travels between server and database rather than over the "
                  "user's connection. The panel adds that compression, partial loading and "
                  "caching change every figure."),
            ("p", "Two readings fail on these numbers. Client session state is not free because "
                  "the server stores nothing: on the first preset it sends forty million bytes "
                  "over one session. And server session state is simple only until there are "
                  "two servers, when the hundred megabytes in one server's memory must be "
                  "reachable from whichever server takes the request, or each user must be "
                  "pinned to one server, which is Fowler's clustering problem."),
            ("h3", "Exercise"),
            ("ul", [
                "5,000 users.",
                "40,000 bytes of session state each.",
                "12 requests in a session.",
                "A session id of 32 bytes.",
            ]),
            ("p", "Compute by hand the bytes on the wire a request and a session with client "
                  "state, what a request carries with server or database state, the memory "
                  "server state holds, and the bytes database state moves a request."),
            ("p", "That ends Concurrency and Session State. The next course, Distribution and "
                  "Putting It Together, asks what should run on another machine, beginning "
                  "with Distribution Strategies."),
        ],
        "lab": ("eakit", {
            "mode": "session",
            "view": "state",
            "preset": "a-megabyte",
            "source": ("the book's illustration in Chapter 6, Session State, for the megabyte "
                       "session; the users, requests and id, and a-small-cart, are illustrative"),
            "presets": [
                # F20, PDF p. 90 of the operator's copy.
                {"id": "a-megabyte",
                 "label": "A megabyte of session state (the book's illustration), 100 users",
                 "users": "100", "stateBytes": "1000000", "requests": "20", "idBytes": "32",
                 "expect": {"snWire": "2,000,000", "snSessionWire": "40,000,000",
                            "snIdOnly": "32", "snMemory": "100,000,000",
                            "snDatabase": "2,000,000"}},
                {"id": "a-small-cart",
                 "label": "A small cart of 2,000 bytes, 100 users",
                 "users": "100", "stateBytes": "2000", "requests": "20", "idBytes": "32",
                 "expect": {"snWire": "4,000", "snSessionWire": "80,000", "snIdOnly": "32",
                            "snMemory": "200,000", "snDatabase": "4,000"}},
            ],
            "panel_title": "Where session state lives, in bytes",
            "panel_intro": (
                "Give the users, one session's state in bytes, the requests in a session and "
                "the session id's size. The lab counts what client state puts on the wire, what "
                "a request carries with server or database state, what server state holds in "
                "memory and what database state reads and writes."
            ),
        }),
        "steps_title": "Counting a session's bytes",
        "steps_intro": "Four steps, the last of them on a session of your own.",
        "steps": [
            ("Price client state",
             "Client state goes to the browser and comes back with every request: twice the "
             "state a request, and that times the requests for a session."),
            ("Price server state",
             "A request carries only the id. The server holds every active user's state at "
             "once, users times the state, in memory or wherever it serializes it."),
            ("Price database state",
             "A request carries only the id, and the server reads the state from the database "
             "and writes it back: twice the state a request, between server and database."),
            ("Do it on a session of your own",
             "Pick one session in a system you know. Find where its state is kept, estimate "
             "its size in bytes, and write down what the other two places would move or hold "
             "for the same session."),
        ],
        "worked": {
            "title": "A megabyte session",
            "intro": [
                "The preset a-megabyte, worked by hand.",
            ],
            "lines": [
                "client, a request: 2 × 1,000,000",
                "so 2,000,000 bytes on the wire",
                "client, a session: 2,000,000 × 20",
                "so 40,000,000 bytes on the wire",
                "server, a request: the id, 32 bytes",
                "server memory: 100 × 1,000,000",
                "database, a request: 2,000,000 bytes",
            ],
            "after": [
                "Server state holds a hundred megabytes and sends 32 bytes a request; client "
                "state holds nothing and sends forty megabytes a session. Neither figure is "
                "small, which is why the chapter weighs failover, clustering and effort before "
                "choosing.",
            ],
        },
        "quiz_title": "Bytes, places and the chapter's claims",
        "quiz": [
            {"q": "Work the exercise: 5,000 users, 40,000 bytes of state, 12 requests in a "
                  "session, a 32-byte id. What does client state put on the wire a request and "
                  "a session, what does server state hold in memory, and what does database "
                  "state read and write a request?",
             "a": ["80,000 and 960,000 bytes; 200,000,000 in memory; 80,000 a request",
                   "40,000 and 480,000 bytes; 200,000,000 in memory; 40,000 a request",
                   "80,000 and 960,000 bytes; 2,400,000,000 in memory; 80,000 a request",
                   "80,000 and 960,000 bytes; 200,000,000 in memory; 32 a request"],
             "c": 0,
             "why": "Client state goes both ways: 2 × 40,000 = 80,000 bytes a request, and "
                    "80,000 × 12 = 960,000 a session. Server state holds 5,000 × 40,000 = "
                    "200,000,000 bytes, once each, not once each request. Database state "
                    "carries the 32-byte id over the wire but reads and writes the state, "
                    "2 × 40,000 = 80,000 bytes, between server and database each request. "
                    "40,000 counts one direction only."},
            {"q": "Which way of storing session state does Fowler say he prefers?",
             "a": ["Database Session State, for its failover",
                   "Server Session State, ideally with its memento kept off the server",
                   "Client Session State, for everything a session holds",
                   "None: he declines to choose between the three"],
             "c": 1,
             "why": "Chapter 6 ends with his preference for Server Session State, best of all "
                    "with the serialized state kept away from the server so that a crash does "
                    "not lose it; he likes "
                    "Client Session State for session ids and very small data, and Database "
                    "Session State only when failover and clustering require it."},
            {"q": "With Server or Database Session State, what must still be kept on the "
                  "client?",
             "a": ["Nothing at all, since the server holds everything",
                   "A copy of the state, kept there for failover",
                   "The pending rows, until the session commits",
                   "At least the id that names the session"],
             "c": 3,
             "why": "Whatever else you use, Fowler says, the client still carries the session's "
                    "id as Client Session State, so that the server can find the "
                    "session's state; the lab's 32 bytes a request are that id."},
            {"q": "Why does Database Session State need a pending field or pending tables?",
             "a": ["To keep uncommitted session data out of queries on record data",
                   "To make the database's queries on record data faster",
                   "To let the client read its own state back from the tables",
                   "To encrypt the session's data before it is committed"],
             "c": 0,
             "why": "Session data should not affect the rest of the system until the session "
                    "commits, so a pending order must not show up in reports such as "
                    "the day's sales. A session id field, or separate pending "
                    "tables, keeps it apart, at the cost of invasiveness or extra mapping code."},
        ],
        "mistakes": [
            ("Thinking client session state is free",
             "The server stores nothing, so it looks like no cost at all. Chapter 6 says the "
             "opposite: client state crosses the wire with every request, so it must be small, "
             "and it must be protected and revalidated, since a user can change it. On the "
             "lesson's first preset, the book's megabyte session, it sends forty million bytes "
             "over one session of twenty requests."),
            ("Thinking server session state is the simple choice",
             "It is the simplest to build, and Fowler prefers it. It stays simple while there is "
             "one server with enough memory and losing a session in a crash is acceptable. "
             "With two servers the session must be reachable from either, or each user pinned to one, which is the "
             "clustering and failover problem the chapter and the pattern both name."),
            ("Treating a cache as session state",
             "A server may keep data between requests only to be faster. Fowler separates that "
             "from session state: a cache can be lost without losing correct behaviour, and "
             "session state cannot. Counting a cache as session state makes a server look "
             "stateful when it is not."),
        ],
        "standard": (
            "Finish when you can price the three places for session state.",
            "Given users, a session's size, the requests in a session and an id's size, "
            "compute the bytes on the wire a request and a session with client state, the id "
            "alone with server state, the memory server state holds, and the bytes database "
            "state moves a request."
        ),
        "note": (
            "The lab counts bytes on a simple model: the whole state each way for the client, "
            "the whole state read and written for the database, and every user's state in "
            "memory at once for the server. Compression, sending only what changed, caching "
            "and sessions that end early change every figure, and none of them is a measure of "
            "speed, security or the effort of building each one."
        ),
    },
]
