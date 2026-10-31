"""Concurrency and Session State, lessons 1-3 -- Chapter 5, Concurrency.

Fowler et al., Patterns of Enterprise Application Architecture (Addison-Wesley,
2002), Chapter 5, by Martin Fowler and David Rice. Pages in the comments are
PDF pages of the operator's copy, which has no printed page numbers; the
lessons cite the book by chapter and section only. Every quotation is copied
from that copy and checked with ea_quotes.py; every figure attributed to the
book carries its PLAN section S.2 id. The code is written for these lessons
(PLAN section D.4, verbatim): none of the book's listings is reproduced.
"""


def _lines(text):
    """A snippet constant as a code block's list of lines."""
    return text.split("\n")


# ---------------------------------------------------------------- snippets
# PLAN section D.4 and docs/enterprise-patterns/presets.py, verbatim.

COUNT_FILES = """\
// Two reads, and another session may commit between them.
int countFiles(Connection db) throws SQLException {
    int a = count(db, "locking");
    int b = count(db, "multiphase");
    return a + b;
}"""

TWO_CONTROLS = """\
class FileStore {
    private final Map<String, Integer> versions = new HashMap<>();
    private final Map<String, String> lockedBy = new HashMap<>();
    // Optimistic: detect a conflict when the session commits.
    boolean canCommit(String file, int versionWhenRead) {
        return versions.getOrDefault(file, 0) == versionWhenRead;
    }

    // Pessimistic: lock a file the session will edit before it is
    // loaded, so the session works on the latest version or not at all.
    boolean tryLoadForEdit(String file, String session) {
        String holder = lockedBy.get(file);
        if (holder != null && !holder.equals(session)) {
            return false;
        }
        lockedBy.put(file, session);
        return true;
    }
}"""

COUNT_SERIALIZABLE = """\
// Both counts inside one serializable transaction.
int countFiles(Connection db) throws SQLException {
    db.setAutoCommit(false);
    db.setTransactionIsolation(Connection.TRANSACTION_SERIALIZABLE);
    int total = count(db, "locking") + count(db, "multiphase");
    db.commit();
    return total;
}"""

# ---------------------------------------------------------------- exercises
# Each exercise's instance is PLAN section C's, never a preset's; its answer
# is in one quiz item's `why` only. One record a line, with the semicolons
# the lab's input uses, so the reader can paste it.

EXERCISE_TRANSFER = [
    "cash, 400, 300, after, update;",
    "savings, 600, 700, before, update",
]

EXERCISE_PLAN = [
    "0, ann, read, plan;",
    "2, bo, read, plan;",
    "3, ann, edit, plan;",
    "4, bo, edit, plan;",
    "9, bo, commit, -;",
    "12, ann, commit, -",
]

EXERCISE_REGIONS = [
    "north, 12, 12, before, update;",
    "south, 8, 11, before, insert;",
    "east, 5, 7, after, update",
]

# 6.2: one timeline, stated once in the cfg (F16's situation; the minutes are
# illustrative).
_DESIGN = ("0, martin, read, design; 1, david, read, design; 5, david, edit, design; "
           "6, martin, edit, design; 8, david, commit, -; 10, martin, commit, -")


LESSONS = [
    # ---------------------------------------------------------------- 6.1
    # Chapter 5 (Fowler and Rice), opening, PDF p. 72; Concurrency Problems,
    # p. 73; Execution Contexts, p. 74; Isolation and Immutability, p. 75.
    # Quote: PDF p. 73 of the operator's copy, 8 words, ea_quotes.py OK.
    # Lesson total: 8 words.
    # F16, PDF p. 73 of the operator's copy: locking 7 then 9, multiphase 5
    # then 8; Martin counts 15, the answer was 12 before and 17 after.
    {
        "slug": "concurrency-problems",
        "title": "Concurrency Problems",
        "module": "Chapter 5 · Concurrency",
        "one_line": "Two sessions on the same data can lose an update, or hand a reader a total that no state of the data ever had.",
        "summary": (
            "Chapter 5 opens with the two essential problems of concurrency, the lost update and "
            "the inconsistent read, and with the trade between correctness and liveness that "
            "every remedy makes. Replay Martin counting classes while David adds to them, and "
            "see a total built from two correct reads that matches neither state of the data."
        ),
        "key": [
            "lost update: a write over unseen work",
            "inconsistent read: right parts, wrong time",
            "stale read: before a commit that changed it",
            "consistent: no stale reads, or no fresh ones",
            "correctness against liveness",
            "avoid it: isolate, or make it immutable",
        ],
        "key_label": "Chapter 5's first sections in six lines",
        "concepts_intro": (
            "Three terms carry the chapter's opening, and the rest of the course uses all three."
        ),
        "concepts": [
            ("Lost update",
             "One session writes over a change another session made after the first one read "
             "the data. Each write is correct on its own; the second simply never saw the "
             "first, and the first change is gone without anyone being told."),
            ("Inconsistent read",
             "A reader reads several pieces of data, each correct when it is read, but not "
             "correct at the same time, because someone committed a change between the reads. "
             "It needs only one writer."),
            ("Correctness and liveness",
             "Correctness (the chapter also says safety) is getting the right answer. Liveness "
             "is how much concurrent activity can go on. Letting one person at a time near the "
             "data buys the first by spending the second."),
        ],
        "read_title": "The chapter's argument first, then the count",
        "read_intro": (
            "Read the opening of Chapter 5, Concurrency, and its sections Concurrency Problems, "
            "Execution Contexts, and Isolation and Immutability in your own copy first. The "
            "lesson sets out the argument in its own words and then replays the chapter's "
            "inconsistent read in the lab."
        ),
        "body": [
            ("p", "&ldquo;Sadly, fifteen classes was never the right answer.&rdquo; The sentence "
                  "ends the first story of Chapter 5, Concurrency, which Fowler wrote with David "
                  "Rice, and the lesson builds to it. It reads the chapter's opening and its first "
                  "three sections, Concurrency Problems, Execution Contexts, and Isolation and "
                  "Immutability. This is a narrative, read as an argument; read it in your own "
                  "copy first."),
            ("p", "The chapter begins by admitting the difficulty. Concurrency is hard to think "
                  "about, because the ways into trouble are hard to list, and hard to test, which "
                  "worries authors who rely on automated tests. Enterprise developers, the authors "
                  "note with some irony, depend on concurrency as heavily as anyone and think "
                  "about it rarely, and they get away with it because of transaction managers: do your work inside "
                  "a database transaction and little goes badly wrong. The trouble is the work "
                  "that cannot be fitted into one. A user who edits an order across several "
                  "screens spans several database transactions, and controlling concurrency for "
                  "data handled across multiple transactions is what the book calls <em>offline "
                  "concurrency</em>. It is the book's main concern. The other concern, many "
                  "threads in one application server, gets less space because it is simpler, and "
                  "this course's third lesson reads it."),
            ("p", "Concurrency Problems names the two essentials, with source code control as "
                  "the running example. A <em>lost update</em>: Martin spends a few minutes "
                  "changing one method of a file, David changes another method of the same file "
                  "and finishes first, and when Martin saves, his copy, read before David's "
                  "change, writes over it. An <em>inconsistent read</em>: Martin counts the "
                  "classes in a package with two subpackages, locking and multiphase. He sees "
                  "seven in locking, takes a phone call, and while he talks David adds two "
                  "classes to locking and three to the five in multiphase. Martin comes back, "
                  "sees eight in multiphase, and arrives at fifteen. The answer was twelve before "
                  "David's change and seventeen after it. Each of those was a true count at some "
                  "moment; fifteen was true at none."),
            ("p", "Both problems are failures of correctness, and the chapter's next point is "
                  "that correctness alone would be easy: let only one person work on the data at "
                  "a time. That destroys <em>liveness</em>, how much concurrent activity can go "
                  "on, and the essential problem of concurrent programming, the authors say, is "
                  "that you must worry about both. People often give up some correctness to gain "
                  "liveness, depending on how serious and how likely the failures are. The "
                  "remedies bring problems of their own, smaller ones; and if you can tolerate "
                  "the basic problems you can do without control at all, which is rare."),
            ("p", "Execution Contexts fixes the vocabulary the later chapters use. A "
                  "<em>request</em> is one call from outside, which the server works on while the "
                  "client waits. A <em>session</em> is a long interaction, usually a run of "
                  "requests that the user regards as one logical sequence. A server sees both "
                  "from two sides, as the server to its clients and as a client of its databases. "
                  "Processes isolate their data; threads share memory, which is efficient and is "
                  "where concurrency problems come from. And a <em>transaction</em> gathers "
                  "several requests that should be treated as one: a <em>system "
                  "transaction</em> from the application to the database, a <em>business "
                  "transaction</em> from the user to the application."),
            ("p", "Isolation and Immutability then names the two ways to avoid the problems "
                  "altogether. <em>Isolation</em> partitions the data so that only one active "
                  "agent can reach each piece of it, as an operating system gives each process "
                  "its own memory. Good concurrency design, on this account, finds ways to create "
                  "isolated zones and does as much of the programming as possible inside them. "
                  "<em>Immutability</em> starts from the fact that only data that can change "
                  "causes trouble: identify what is immutable, or nearly so, and share it freely, "
                  "or give applications that only read their own copied data."),
            ("p", "Here is the inconsistent read in code. The routine counts two packages with "
                  "two separate queries; `count` stands for some routine that runs one "
                  "`SELECT COUNT` against the database. Nothing ties the two queries together, so "
                  "another session can commit between line 3 and line 4, and neither query is "
                  "wrong."),
            ("code", _lines(COUNT_FILES)),
            ("p", "The lab replays one commit against one reader. Each record is an item, its "
                  "value before and after the commit, the side of the commit the reader read it "
                  "on, and whether the commit inserted rows into it or updated it. A read before "
                  "the commit of an item the commit changes is <em>stale</em>; a read after it of "
                  "a changed item is <em>fresh</em>. The tiles give the total the reader saw, the "
                  "totals before and after the commit, and whether the total matches a state of "
                  "the data: it does when no read is stale, or when none is fresh. The preset "
                  "<code>martin-and-david</code> is the chapter's own illustration: locking 7 "
                  "then 9, read before David's commit; multiphase 5 then 8, read after. The lab "
                  "prints a total of 15, 12 before and 17 after, and &ldquo;no: 15 is neither 12 "
                  "nor 17&rdquo;. The change column says insert, because David added classes; "
                  "the isolation tile it feeds is lesson 3's."),
            ("p", "Now move the reads. In <code>both-after</code> Martin reads both packages "
                  "after the commit: 17, &ldquo;yes: the state after the commit&rdquo;. In "
                  "<code>both-before</code> he reads both before it: 12, &ldquo;yes: the state "
                  "before the commit&rdquo;. Only the timing of the reads changed. Should a mixed "
                  "read happen to land on one of the two totals, the tile says &ldquo;no, "
                  "though&rdquo; the number equals it, because a coincidence is still not a read "
                  "of either state."),
            ("p", "What does this show? Every number Martin read was true when he read it, so a "
                  "check of each read against the database at that moment would pass. The fault "
                  "is in the sum, which belongs to no state the database was ever in, and it took "
                  "only one person writing. On the lesson's illustration, the remedy is not to "
                  "read more carefully but to arrange that both reads see one state, which is "
                  "what the rest of the chapter is about."),
            ("h3", "Exercise"),
            ("code", EXERCISE_TRANSFER),
            ("p", "A transfer of 100 between two accounts commits while a report reads them: "
                  "cash is read after the commit and savings before it. Find by hand the total "
                  "the report saw, the totals before and after the commit, and whether the "
                  "report's total matches either state. Then name the stale read. You can check "
                  "your answer by pasting the two records into the lab."),
            ("p", "Fowler and Rice name two families of remedy, one that detects a conflict and "
                  "one that prevents it. The next lesson, Optimistic and Pessimistic Control, "
                  "replays one timeline under each."),
        ],
        "lab": ("eakit", {
            "mode": "lock",
            "view": "reads",
            "preset": "martin-and-david",
            "presets": [
                # F16, PDF p. 73 of the operator's copy.
                {"id": "martin-and-david",
                 "label": "Martin and David: locking read before the commit, multiphase after (the book's illustration)",
                 "items": "locking, 7, 9, before, insert; multiphase, 5, 8, after, insert",
                 "expect": {"olSeen": "15", "olConsistent": "no: 15 is neither 12 nor 17"}},
                {"id": "both-after",
                 "label": "Both packages read after David's commit",
                 "items": "locking, 7, 9, after, insert; multiphase, 5, 8, after, insert",
                 "expect": {"olSeen": "17", "olConsistent": "yes: the state after the commit"}},
                {"id": "both-before",
                 "label": "Both packages read before David's commit",
                 "items": "locking, 7, 9, before, insert; multiphase, 5, 8, before, insert",
                 "expect": {"olSeen": "12", "olConsistent": "yes: the state before the commit"}},
            ],
            "panel_title": "What a reader sees across one commit",
            "panel_intro": (
                "Each record is one item: its value before and after one writer's commit, the "
                "side of the commit the reader read it on, and whether the commit inserted rows "
                "or updated them. The lab adds up what was read and compares the sum with the "
                "two states of the data."
            ),
        }),
        "steps_title": "Checking what a reader saw",
        "steps_intro": "Four steps, the last of them on a system of your own.",
        "steps": [
            ("Write down both states",
             "For each item, write its value before the commit and after it, and add each "
             "column. Those two totals are the only correct answers there are."),
            ("Mark each read stale or fresh",
             "An item that the commit changed and that was read before it is stale; one that "
             "was changed and read after it is fresh. An unchanged item is neither."),
            ("Add up what was read and compare",
             "Sum the values as read. The total is a state of the data only when no read is "
             "stale or no read is fresh; a mixed read that equals a total does so by "
             "coincidence."),
            ("Do it on a report of your own",
             "Take one report in a system you know that reads several tables while other "
             "sessions write to them. List its reads in order, name one commit that could fall "
             "between two of them, and write down the total the report would then print."),
        ],
        "worked": {
            "title": "Martin's fifteen classes",
            "intro": [
                "The preset martin-and-david, worked by hand: two packages, one commit by David "
                "between Martin's two reads.",
            ],
            "lines": [
                "before the commit: 7 + 5 is 12",
                "after the commit: 9 + 8 is 17",
                "locking, read before the commit: 7",
                "multiphase, read after the commit: 8",
                "Martin sees 7 + 8, which is 15",
                "15 is neither 12 nor 17",
            ],
            "after": [
                "Locking is the stale read: David changed it and Martin read it first. "
                "Multiphase is the fresh one. With one of each, the total cannot be either "
                "state, whatever the numbers are.",
            ],
        },
        "quiz_title": "Reads across a commit",
        "quiz": [
            {"q": "Work the exercise: cash goes from 400 to 300 and is read after the commit; "
                  "savings goes from 600 to 700 and is read before it. What total does the "
                  "report see, and does it match a state of the data?",
             "a": ["900; it matches no state, since the total is 1,000 both before and after",
                   "1,000; a transfer only moves money, so the total seen is unchanged",
                   "1,100; it matches no state, since the reads straddle the commit",
                   "900; it matches the state after the commit, when cash had moved"],
             "c": 0,
             "why": "The report read 300 + 600 = 900. Before the commit the accounts held "
                    "400 + 600 = 1,000, and after it 300 + 700 = 1,000, so the lab prints "
                    "&ldquo;no: 900 is not 1,000, before or after&rdquo;. Savings is the stale "
                    "read. 1,000 is what either state holds, which a mixed read cannot see here; "
                    "1,100 is the other mixed read, cash before and savings after."},
            {"q": "Martin reads both packages after David's commit, which took locking from 7 "
                  "to 9 and multiphase from 5 to 8. What total does he see, and is it a state "
                  "of the data?",
             "a": ["15; no", "17; yes, the state after the commit",
                   "12; yes, the state before the commit", "17; no, because the commit fell "
                   "between his reads"],
             "c": 1,
             "why": "Both reads are fresh, so he sees 9 + 8 = 17, the state after the commit "
                    "(the preset both-after). No commit falls between two of his reads; 15 is "
                    "the total of one stale read and one fresh one."},
            {"q": "By Chapter 5's account, what is the least an inconsistent read needs?",
             "a": ["Two sessions that both write the same data",
                   "Two sessions that both only read the same data",
                   "One session reading the same item twice, with nobody writing",
                   "One session that writes and another that reads"],
             "c": 3,
             "why": "In the chapter's story only David writes; Martin only reads. A lost update "
                    "needs two writers, but an inconsistent read needs one writer whose commit "
                    "falls between another session's reads. With nobody writing, every read "
                    "sees the same state."},
            {"q": "Which of these does Isolation and Immutability give as a way to avoid "
                  "concurrency problems altogether?",
             "a": ["Detect conflicts at commit with a version number",
                   "Run every request in a serializable transaction",
                   "Partition the data so that only one agent can reach each piece",
                   "Refuse a second session's lock at once"],
             "c": 2,
             "why": "The section's two ways are isolation, partitioning the data so that one "
                    "active agent reaches each piece, and immutability, sharing only data that "
                    "does not change. Version checks, serializable transactions and refused "
                    "locks control concurrency where it cannot be avoided; they come later in "
                    "the chapter."},
        ],
        "mistakes": [
            ("Thinking that correct reads give a correct result",
             "If every value read is right, the total should be right. Chapter 5's inconsistent "
             "read is the counterexample: Martin's seven and eight were each correct when he "
             "read them, and fifteen was never the number of classes, which was twelve and then "
             "seventeen. On the lesson's illustration the lab shows the same: a stale read and "
             "a fresh one give a total that matches neither state. Correctness belongs to the "
             "set of reads, not to each one."),
            ("Thinking concurrency needs two writers",
             "A lost update does need two people changing the same data. An inconsistent read "
             "needs only one: David writes, Martin only reads, and Martin is the one with the "
             "wrong answer. A report that writes nothing can still be wrong because of a commit "
             "that falls between its queries."),
            ("Treating correctness as the only goal",
             "The way to make every read and write correct is to let one person at a time near "
             "the data, and the chapter says plainly that this costs liveness, the concurrent "
             "activity the system exists to allow. Its question is how much correctness to buy "
             "at what cost in liveness, depending on how serious and how likely the failures "
             "are, and the rest of the course is about that trade."),
        ],
        "standard": (
            "Finish when you can say what a reader saw across a commit.",
            "Given items with their values before and after one commit and the side of it each "
            "was read on, compute the total seen and both totals by hand, and say whether the "
            "total matches either state of the data."
        ),
        "note": (
            "The lab replays one commit and one reader, and you tell it which side of the "
            "commit each read fell on. A real report does not know that, and real data sees "
            "many commits; nor does the lab model reading data another session has not yet "
            "committed. It shows what one straddled commit does to a total, not how often "
            "that happens in your system."
        ),
    },
    # ---------------------------------------------------------------- 6.2
    # Chapter 5 (Fowler and Rice), Optimistic and Pessimistic Concurrency
    # Control, with Preventing Inconsistent Reads and Deadlocks, PDF pp. 76-78.
    # Quote: PDF p. 76 of the operator's copy, 24 words, ea_quotes.py OK.
    # Lesson total: 24 words.
    # The timeline is F16's situation (PDF p. 73 of the operator's copy);
    # its minutes are illustrative.
    {
        "slug": "optimistic-and-pessimistic-control",
        "title": "Optimistic and Pessimistic Control",
        "module": "Chapter 5 · Concurrency",
        "one_line": "An optimistic lock lets both sessions work and detects the clash at commit; a pessimistic lock lets only one work, and prevents it.",
        "summary": (
            "Chapter 5's two forms of concurrency control, and how to choose between them by "
            "how often conflicts happen and how much one costs. Replay one timeline of two "
            "sessions with no control, optimistically and pessimistically, and count who "
            "commits, who is refused or conflicts, and how much work is lost."
        ),
        "key": [
            "optimistic: detect the conflict at commit",
            "pessimistic: prevent it, one editor at a time",
            "choose by how often, and how much it hurts",
            "version marker: compare, then increment",
            "deadlock: simple, conservative schemes",
        ],
        "key_label": "The section in five lines",
        "concepts_intro": (
            "The section turns on two kinds of lock and on one hazard of the second."
        ),
        "concepts": [
            ("Optimistic lock",
             "Every session may work on the data. When a session commits, the system checks "
             "whether anyone else committed a change to that data since the session read it, "
             "and refuses the commit if so. It detects a conflict; it does not stop one."),
            ("Pessimistic lock",
             "The first session to take the data for editing locks it, and nobody else may edit "
             "it until that session finishes. It prevents a conflict by making the second "
             "session wait or give up before it starts."),
            ("Deadlock",
             "Two sessions each hold a lock the other needs, so neither can go on. It is a "
             "hazard of pessimistic locking, and Chapter 5 prefers very simple, conservative "
             "schemes, even at the cost of unnecessary victims."),
        ],
        "read_title": "The section's argument first, then the replay",
        "read_intro": (
            "Read Chapter 5's section Optimistic and Pessimistic Concurrency Control, with its "
            "parts Preventing Inconsistent Reads and Deadlocks, in your own copy first. The "
            "lesson sets out the argument and then replays one timeline under each scheme."
        ),
        "body": [
            ("p", "&ldquo;A good way of thinking about this is that an optimistic lock is about "
                  "conflict detection while a pessimistic lock is about conflict "
                  "prevention.&rdquo; The sentence is Fowler's and Rice's, from Chapter 5's "
                  "section Optimistic and Pessimistic Concurrency Control, which this lesson "
                  "reads with its two parts, Preventing Inconsistent Reads and Deadlocks. It is "
                  "a narrative, read as an argument; read it in your own copy first."),
            ("p", "The section's question is what to do with data that can change and cannot be "
                  "isolated, and it answers with two forms of control, on the source code "
                  "example again. Martin and David both want to edit one file. With "
                  "<em>optimistic</em> locking each takes a copy and edits freely; David checks "
                  "in first without trouble, and when Martin tries to commit, the system detects "
                  "the conflict, rejects his commit and leaves it to him to sort out. With "
                  "<em>pessimistic</em> locking whoever checks the file out first stops anyone "
                  "else editing it, so David cannot work on the file until Martin has committed. "
                  "The authors grant, in an aside, that optimistic locking is arguably not "
                  "locking at all, and keep the word because it is convenient and widespread."),
            ("p", "Each has its cost. A pessimistic lock reduces concurrency: while Martin holds "
                  "the file everyone else waits, and with enterprise data, the authors add, "
                  "someone editing can stop others even reading. An optimistic lock is held only "
                  "during the commit, so people make better progress, but a conflict means that "
                  "everyone after the first commit must take the new version and merge. Source "
                  "code merges easily, often automatically; business data usually does not, and "
                  "often the only course is to throw the work away and start again. So the "
                  "choice turns on the frequency and severity of conflicts: if they are rare or "
                  "cheap, the section says you should usually pick optimistic locks, which give "
                  "better concurrency and are usually easier to build; if a conflict is painful "
                  "for users, you need a pessimistic technique."),
            ("p", "Preventing Inconsistent Reads returns to the problem of the last lesson. "
                  "Martin edits a class that calls another, David changes the other's interface "
                  "and checks in first, and the shared build breaks although nobody overwrote "
                  "anybody. Pessimistic schemes prevent this with read (shared) and write "
                  "(exclusive) locks: many readers, or one writer. Optimistic schemes keep a "
                  "<em>version marker</em>, a timestamp or a counter, on the data: an update is "
                  "allowed only if the marker is unchanged, and then the marker moves on. "
                  "Catching an inconsistent read means checking the markers of what was read "
                  "too, and checking everything costs conflicts on data that hardly matters, so "
                  "the section asks you to separate data you used from data you merely glanced "
                  "at, which takes thought about what each is for. Temporal reads, which ask for "
                  "data as of a time, are the third remedy, and few databases offer them."),
            ("p", "Deadlocks are the hazard of the pessimistic side: Martin holds one file and "
                  "wants David's, and David holds that one and wants Martin's. You can detect a "
                  "deadlock and pick a victim, who loses his work and locks; give every lock a "
                  "time limit; make everyone take all their locks at the start; take locks in a "
                  "fixed order, such as alphabetical; or make anyone who asks for a lock already "
                  "held a victim at once. Because it is easy to think a scheme is deadlock-proof "
                  "and then meet a chain of events nobody considered, the authors prefer very "
                  "simple, conservative schemes, even at the price of unnecessary victims."),
            ("p", "The snippet holds both controls in one class. `canCommit` is the optimistic "
                  "check: the session remembers the version it read, and the commit may go "
                  "ahead only if the stored version is still that one. `tryLoadForEdit` is the "
                  "pessimistic one: the session asks for the file before it loads it, and is "
                  "turned away at once if another session holds it. The class leaves out moving "
                  "the version on after a commit and releasing the lock, which a real store "
                  "must do, and it does not serialize access to its maps, so two threads could "
                  "both find a file free; a real lock manager must."),
            ("code", _lines(TWO_CONTROLS)),
            ("p", "The lab replays a timeline of events, each a minute, a session, an action "
                  "(read, edit or commit) and a record. Every record has a version that starts "
                  "at 0, a commit adds one to each record the session edited, and a session "
                  "remembers the version it first saw. The tiles count the sessions that "
                  "committed, those whose commit conflicted, and those refused a lock, each with "
                  "their names; the lost updates; the minutes of work redone, from a failed "
                  "session's first event to its failure; and the most locks held at once. The "
                  "one timeline here is the chapter's situation with minutes added: Martin reads "
                  "the design at minute 0 and David at 1; David edits at 5 and Martin at 6; "
                  "David commits at 8 and Martin at 10."),
            ("p", "With <code>no-control</code> the lab prints &ldquo;2: david, martin&rdquo; "
                  "committed, 1 lost update and 0 minutes redone. Both commits succeed, and "
                  "Martin's, made from the version he read at minute 0, writes over David's "
                  "change. Nobody is told; the lost update is in the count and nowhere else. "
                  "With <code>optimistic</code> the lab prints &ldquo;1: david&rdquo; committed "
                  "and &ldquo;1: martin&rdquo; in conflict, with 10 minutes redone: David moved "
                  "the version to 1 at minute 8, Martin's commit at minute 10 finds it changed, "
                  "and everything since minute 0 must be done again."),
            ("p", "With <code>pessimistic</code> the lab prints &ldquo;1: martin&rdquo; "
                  "committed, &ldquo;1: david&rdquo; refused, 0 minutes redone and at most 1 "
                  "lock held. Martin loads the design for editing at minute 0 and takes the lock "
                  "then, because a pessimistic lock is taken before the data is loaded, not when "
                  "the editing starts. David is refused at minute 1, before he has done any "
                  "work, and the lab skips his later events. His read is refused because he "
                  "goes on to edit the design: the lab's lock is the exclusive write lock, taken "
                  "when a session loads a record it means to edit, as `tryLoadForEdit` asks for "
                  "it. A session that only read the design would be let through. What no tile shows is his wait: he "
                  "cannot work on the design until Martin commits at minute 10."),
            ("p", "So which is safer? On this timeline the two sessions do collide, and the "
                  "schemes only choose who pays: ten minutes of Martin's work, or David kept "
                  "out for nine. Now delete Martin's commit from the timeline, as if he had "
                  "walked away without saving, so that there is no collision at all. "
                  "Pessimistically David is still refused at minute 1; optimistically he "
                  "commits and nobody loses anything. That is why the section makes the choice "
                  "turn on how often conflicts happen and how much each one costs."),
            ("h3", "Exercise"),
            ("code", EXERCISE_PLAN),
            ("p", "Replay this timeline by hand, first under optimistic locking and then under "
                  "pessimistic locking. For each, say who commits, who fails and at which "
                  "minute, and how many minutes of work the failure discards."),
            ("p", "The lab's reads are on one side of a commit or the other because nothing "
                  "else ties them together. The next lesson, Transactions and Isolation, reads "
                  "the tool that does: the database transaction, and how much of its protection "
                  "systems give up for speed."),
        ],
        "lab": ("eakit", {
            "mode": "lock",
            "view": "timeline",
            "preset": "no-control",
            # F16's situation, PDF p. 73 of the operator's copy; minutes illustrative.
            "events": _DESIGN,
            "presets": [
                {"id": "no-control",
                 "label": "Martin and David edit the design, with no control",
                 "scheme": "none",
                 "expect": {"olCommitted": "2: david, martin", "olLostUpdates": "1", "olRedo": "0"}},
                {"id": "optimistic",
                 "label": "The same timeline, optimistic",
                 "scheme": "optimistic",
                 "expect": {"olCommitted": "1: david", "olConflicts": "1: martin",
                            "olLostUpdates": "0", "olRedo": "10"}},
                {"id": "pessimistic",
                 "label": "The same timeline, pessimistic",
                 "scheme": "pessimistic",
                 "expect": {"olCommitted": "1: martin", "olRefused": "1: david",
                            "olLostUpdates": "0", "olRedo": "0", "olPeakLocks": "1"}},
            ],
            "panel_title": "One timeline under three schemes",
            "panel_intro": (
                "Each event is a minute, a session, an action and a record. The lab replays the "
                "events under the scheme chosen and counts who commits, who conflicts at commit, "
                "who is refused a lock, the updates lost, the minutes of work redone and the "
                "most locks held at once. The timeline is the chapter's situation; its minutes "
                "are illustrative."
            ),
        }),
        "steps_title": "Replaying a timeline",
        "steps_intro": "Four steps, the last of them on a record of your own.",
        "steps": [
            ("Note the version each session saw",
             "Every record starts at version 0. For each session, write the version of each "
             "record at its first read or edit, and add one to a record's version at each "
             "successful commit that edited it."),
            ("Replay it optimistically",
             "At each commit, compare the versions the session saw with the current ones for "
             "the records it edited. If any has moved, the commit conflicts; its redo is the "
             "minutes from the session's first event to that commit."),
            ("Replay it pessimistically",
             "Give a session the lock on a record at its first read or edit of a record it "
             "will edit. A session that asks for a lock another holds is refused there and "
             "then, and its later events never happen; a commit releases its locks."),
            ("Do it on a record of your own",
             "Pick one record in a system you know that two people edit. Write down which "
             "scheme protects it, if any, and what the second editor sees when the first has "
             "already saved."),
        ],
        "worked": {
            "title": "Martin and David, three ways",
            "intro": [
                "The lab's one timeline, replayed by hand under each scheme.",
            ],
            "lines": [
                "no control: both commit at 8 and 10",
                "Martin saw version 0; it was 1 at 10",
                "no control: 1 lost update, nobody told",
                "optimistic: Martin conflicts at minute 10",
                "optimistic: 10 minutes redone, 0 to 10",
                "pessimistic: Martin locks at minute 0",
                "pessimistic: David refused at minute 1",
            ],
            "after": [
                "Pessimistically nobody redoes anything, and David is kept from the design "
                "from minute 1 to minute 10. Optimistically David is never kept out, and "
                "Martin pays ten minutes. Neither figure is the scheme's verdict; each is what "
                "this timeline costs under it.",
            ],
        },
        "quiz_title": "Detection, prevention and their costs",
        "quiz": [
            {"q": "Work the exercise under optimistic locking: ann reads the plan at 0 and "
                  "edits at 3, bo reads at 2 and edits at 4, bo commits at 9 and ann at 12. "
                  "What happens?",
             "a": ["bo commits; ann's commit conflicts at minute 12, and 12 minutes of work "
                   "are redone",
                   "ann commits; bo's commit conflicts at minute 9, and 7 minutes are redone",
                   "Both commit, and ann's commit writes over bo's change",
                   "bo commits; ann's commit conflicts, and 9 minutes are redone"],
             "c": 0,
             "why": "bo commits first, at minute 9, and moves the plan to version 1. ann saw "
                    "version 0 at minute 0, so her commit at 12 conflicts, and her redo runs "
                    "from her first event to the failure, 12 − 0 = 12 minutes. Nine minutes "
                    "would start the count at her edit instead of her read. Both committing is "
                    "what happens with no control."},
            {"q": "Under the lab's pessimistic rule, a session takes the lock at its first "
                  "read or edit of a record it edits anywhere in the timeline, and a session "
                  "refused a lock ends there. On the exercise's timeline, what happens to bo?",
             "a": ["He is refused at minute 4, when he starts to edit",
                   "He is refused at minute 2, when he loads the plan, and redoes nothing",
                   "He commits at minute 9, because ann has not edited yet",
                   "He waits until ann commits at minute 12, then edits"],
             "c": 1,
             "why": "ann reads the plan at minute 0 and edits it later, so she takes the lock "
                    "at minute 0. bo's read at minute 2 is his load of a record he means to "
                    "edit, and it is refused; his redo is 2 − 2 = 0. The lock is taken at load, "
                    "not at the edit, and a refused session ends rather than waits."},
            {"q": "What does the section say the choice between optimistic and pessimistic "
                  "locking turns on?",
             "a": ["How many users the system has, and how many edit at once",
                   "Whether the database supports transactions across requests",
                   "Nothing: prevention is always safer, so choose pessimistic",
                   "How often conflicts happen and how severe each one is"],
             "c": 3,
             "why": "The essence of the choice, in the section's terms, is the frequency and "
                    "severity of conflicts: optimistic when they are rare or cheap, pessimistic "
                    "when a conflict is painful for users. Prevention has its own cost, the "
                    "concurrency lost while others wait."},
        ],
        "mistakes": [
            ("Thinking pessimistic locking is safer, so better",
             "Prevention sounds safer than detection, and a pessimistic lock does turn a "
             "conflict away before any work is done. It also keeps the second session out when "
             "the two would never have collided, and it holds everyone else back while one "
             "session works. Chapter 5's choice turns on how often conflicts happen and what "
             "one costs. On the lesson's illustration the schemes only move the cost: ten "
             "minutes of Martin's work optimistically, David kept out for nine "
             "pessimistically."),
            ("Thinking optimistic locking loses no work",
             "It does stop the lost update: Martin's commit is refused, David's change "
             "survives, and the lab counts 0 lost updates. But it stops it by throwing away "
             "the second session's work, not by saving it. Unless Martin can merge, everything "
             "he did is gone, and the section warns that business data is seldom easy to "
             "merge. On the lesson's timeline Martin redoes ten minutes."),
            ("Checking only what you write",
             "A version check on the records a session writes catches lost updates, and misses "
             "the inconsistent read: work built on something another session changed "
             "meanwhile. Preventing Inconsistent Reads asks for the versions of what was read "
             "to be checked too, for the data that matters, which takes knowing what each "
             "piece is used for."),
        ],
        "standard": (
            "Finish when you can replay a timeline under each scheme.",
            "Given a timeline of reads, edits and commits by two sessions, state under no "
            "control, optimistic and pessimistic locking who commits and who fails, at which "
            "minute, and how many minutes of work the failure discards."
        ),
        "note": (
            "The lab's pessimistic lock is the simplest kind, one editor at a time, refused at "
            "once rather than kept waiting, so it never deadlocks; read locks, waiting and "
            "timeouts are not in it. Nor can it say how often your sessions collide, which is "
            "the figure the chapter's choice depends on: that has to come from your own "
            "system."
        ),
    },
    # ---------------------------------------------------------------- 6.3
    # Chapter 5 (Fowler and Rice), Transactions, PDF pp. 79-83 (Table 5.1 is
    # on p. 81 and is stated in the lesson's own sentences, never reproduced);
    # Patterns for Offline Concurrency Control, p. 83; Application Server
    # Concurrency, pp. 84-85.
    # Quote: PDF p. 81 of the operator's copy, 13 words, ea_quotes.py OK.
    # The word "database" for any transactional resource, p. 79, 1 word.
    # Lesson total: 14 words.
    # F16, PDF pp. 80-81 of the operator's copy: the files retold, the insert
    # case a phantom and the totals case an unrepeatable read.
    # F17, PDF p. 84 of the operator's copy: 99 percent of the time.
    # The course's one modern aside (PLAN section F.3): snapshot isolation.
    {
        "slug": "transactions-and-isolation",
        "title": "Transactions and Isolation",
        "module": "Chapter 5 · Concurrency",
        "one_line": "A transaction can promise a reader one state of the data, and the weaker isolation levels trade parts of that promise for throughput.",
        "summary": (
            "Chapter 5 on transactions: ACID, how long a transaction should be, the four "
            "isolation levels and the read error each lets through, business against system "
            "transactions, the map of the offline patterns, and threads in the application "
            "server. Name the read error a straddled commit causes and the weakest level that "
            "prevents it."
        ),
        "key": [
            "ACID: atomic, consistent, isolated, durable",
            "serializable: as if one after another",
            "repeatable read allows phantoms",
            "read committed allows unrepeatable reads",
            "stale update: unrepeatable; insert: phantom",
            "business transaction across many systems",
        ],
        "key_label": "The section in six lines",
        "concepts_intro": (
            "Three terms from the section on transactions, each one the lab uses."
        ),
        "concepts": [
            ("Isolation level",
             "How much of other transactions' work a transaction may see while it runs. The SQL "
             "standard defines four, from serializable, the strongest, down to read "
             "uncommitted, and each step down lets one more kind of inconsistent read through."),
            ("Phantom and unrepeatable read",
             "A phantom is a row another transaction inserted that a reader sees in some of its "
             "reads and not others. An unrepeatable read is a value another transaction "
             "updated, so that reading it again would give a different answer."),
            ("Business and system transaction",
             "A system transaction is the database's, a group of SQL statements begun and "
             "ended together. A business transaction is the user's, such as setting up bill "
             "payments over several screens and pressing OK, and it usually spans several "
             "system transactions."),
        ],
        "read_title": "The section's argument first, then the levels",
        "read_intro": (
            "Read Chapter 5's sections Transactions, Patterns for Offline Concurrency Control "
            "and Application Server Concurrency in your own copy first. The lesson sets out the "
            "argument and then names, in the lab, the read error a straddled commit makes."
        ),
        "body": [
            ("p", "&ldquo;To be sure of correctness you should always use the serializable "
                  "isolation level.&rdquo; Read on, because the next sentence in Chapter 5 "
                  "gives its cost. This lesson reads three sections of the chapter, "
                  "Transactions, Patterns for Offline Concurrency Control and Application "
                  "Server Concurrency. They are narrative, read as an argument; read them in "
                  "your own copy first."),
            ("p", "The section's question is what the transaction, the main tool for "
                  "concurrency in enterprise applications, actually promises. A transaction is "
                  "a bounded piece of work that leaves everything it touches in a consistent "
                  "state and happens all or not at all, and software states the promise as "
                  "ACID: <em>atomicity</em>, every step completes or all roll back; "
                  "<em>consistency</em>, the resources are sound at the start and the end; "
                  "<em>isolation</em>, no other open transaction sees the result until it "
                  "commits; and <em>durability</em>, a committed result survives a crash. The "
                  "book says &ldquo;database&rdquo; for any transactional resource, message "
                  "queues and printers included."),
            ("p", "Transaction systems want transactions short, so the general advice is never "
                  "to let one span several requests, which would make it a <em>long "
                  "transaction</em>. The simple model is the <em>request transaction</em>, opened "
                  "when a request begins and closed when it ends. A <em>late transaction</em> "
                  "does its reads outside and opens only to write, which shortens it and leaves "
                  "the reads unprotected. The section also warns about lock escalation: a "
                  "transaction that locks many rows can have the database lock the whole table "
                  "instead, which is one reason not to keep every domain object in one table."),
            ("p", "Then the levels. A set of transactions is <em>serializable</em> when running "
                  "them together gives the result of some order of running them one after "
                  "another, so Martin, counting under serializable, gets twelve or seventeen; "
                  "which one is not promised, but it is a correct one. The SQL standard defines "
                  "four levels, and in the chapter's retelling each step down admits one more "
                  "kind of read error. <em>Repeatable read</em> allows phantoms: rows inserted "
                  "while you read, seen in some reads and not others, which is Martin's case, "
                  "since David added files. <em>Read committed</em> allows unrepeatable reads "
                  "as well: if Martin reads stored totals rather than files, his seven for "
                  "locking could not be read again after David's commit. <em>Read "
                  "uncommitted</em> allows dirty reads too, of data another transaction has not "
                  "committed and may roll back. The chapter sums this up in a table, and the "
                  "table is better read in the book."),
            ("p", "Which brings back the opening sentence. Straight after it the authors say "
                  "that serializable damages a system's liveness so much that you often have to "
                  "reduce it to get throughput, that you must decide which risks to take, and "
                  "that each transaction can have its own level. Business and System "
                  "Transactions then raises the harder case. The user's business transaction, "
                  "logging in, choosing an account, setting up payments and pressing OK, should "
                  "be ACID too, and running it as one long system transaction would make it so. "
                  "Where the database is not under heavy concurrent load, the authors advise "
                  "doing exactly that; otherwise the database becomes a bottleneck, and you are left with a run of "
                  "short system transactions and the glue between them. Atomicity and "
                  "durability come from doing the final save in one system transaction; "
                  "isolation is the hard part."),
            ("p", "Patterns for Offline Concurrency Control maps the patterns the next two "
                  "lessons read, and it begins by saying to avoid them if you can: fit the "
                  "business transaction in one request, or accept a long transaction and give "
                  "up scalability. Otherwise the authors' first choice is Optimistic Offline "
                  "Lock, easier to program and best for liveness, whose limit is finding out "
                  "only at commit; Pessimistic Offline Lock finds out early, at the price of "
                  "harder code and less liveness; Coarse-Grained Lock and Implicit Lock make "
                  "either easier to live with. The choice affects the whole user experience, "
                  "so it is not a technical detail to settle after the requirements, and since "
                  "concurrency bugs are hard to reproduce, the authors advise experienced help."),
            ("p", "Application Server Concurrency, the last section, is about threads inside "
                  "the server. Explicit locks and synchronisation are easy to get wrong in ways "
                  "that are almost impossible to reproduce, and the result, in the book's figure, "
                  "behaves for 99 percent of the time and fails at random for the rest; so the "
                  "authors set out to keep explicit synchronisation out of application code. "
                  "Process-per-session isolates completely and costs most; pooled "
                  "process-per-request is nearly as isolated and much cheaper; thread-per-request "
                  "is cheaper still and isolates nothing, so the authors see a lot to be said for "
                  "process-per-request, as just as scalable and more robust. With threads, create fresh objects for each request, keep them out "
                  "of statics and singletons, and synchronise only the explicit pools, such as "
                  "database connections."),
            ("p", "The snippet is the first lesson's routine with the two counts inside one "
                  "transaction. `setAutoCommit(false)` stops the driver committing after each "
                  "statement, `setTransactionIsolation` asks for serializable, and `commit` "
                  "ends the transaction. Under that level the two counts see one state, and the "
                  "routine returns 12 or 17, never 15, or throws if the database aborts the "
                  "transaction to keep that promise."),
            ("code", _lines(COUNT_SERIALIZABLE)),
            ("p", "The lab is the first lesson's, now with its last tile. When reads straddle a "
                  "commit, the stale item decides the error: if its change was an update, it is "
                  "an unrepeatable read, which read committed allows and repeatable read "
                  "prevents; if every stale item's change was an insert, it is a phantom, which "
                  "repeatable read allows and only serializable prevents. The preset "
                  "<code>quarter-totals</code> reads January, unchanged at 400, and February, "
                  "300 updated to 350, before a commit, and March, 0 with 120 inserted, after "
                  "it. The lab prints 820 seen, &ldquo;no: 820 is neither 700 nor 870&rdquo;, "
                  "and &ldquo;read committed allows it (an unrepeatable read); repeatable read "
                  "prevents it&rdquo;, because February's stale value was an update."),
            ("p", "Take February out and the preset <code>only-a-new-row</code> reads January "
                  "before and March after: 520, &ldquo;yes: the state after the commit&rdquo;, "
                  "and &ldquo;none needed: no read straddles the commit&rdquo;, because January "
                  "did not change and no stale read is left. Load "
                  "<code>martin-and-david</code>, the first lesson's preset, and the tile "
                  "reads &ldquo;repeatable read allows it (a phantom); serializable prevents "
                  "it&rdquo;: the stale read is locking, and David's change to it was new "
                  "files, an insert. The panel adds that a database's own implementation of a "
                  "level can be stronger than the standard asks."),
            ("p", "One development since the book changes what those level names mean on many "
                  "databases. Multiversion databases commonly give each transaction a snapshot "
                  "of the data as it stood when the transaction began, a level called snapshot "
                  "isolation that the chapter's four do not name. A snapshot shows none of the "
                  "three read errors as the chapter describes them, yet it allows an anomaly of "
                  "its own, write skew: two transactions each check a rule against the same "
                  "snapshot, each change a different row, and together break the rule. Some "
                  "databases ship this under the name repeatable read and some under "
                  "serializable, and some have since added a stricter serializable. Chapter "
                  "5's advice to choose the level for each transaction stands either way; "
                  "what changes is that the name alone no longer tells you which errors you "
                  "are choosing."),
            ("h3", "Exercise"),
            ("code", EXERCISE_REGIONS),
            ("p", "Three regions are read around one commit. Find the total seen and the totals "
                  "before and after, say which item is stale and whether its change was an "
                  "insert or an update, and name the read error and the weakest isolation level "
                  "that prevents it."),
            ("p", "The patterns that hold a business transaction together across system "
                  "transactions start with the authors' first choice. The next lesson, "
                  "Optimistic Offline Lock, reads it."),
        ],
        "lab": ("eakit", {
            "mode": "lock",
            "view": "reads",
            "preset": "quarter-totals",
            "presets": [
                {"id": "quarter-totals",
                 "label": "Quarter totals: February updated and read stale, March inserted",
                 "items": "january, 400, 400, before, update; february, 300, 350, before, update; "
                          "march, 0, 120, after, insert",
                 "expect": {"olSeen": "820", "olConsistent": "no: 820 is neither 700 nor 870",
                            "olLevel": "read committed allows it (an unrepeatable read); "
                                       "repeatable read prevents it"}},
                {"id": "only-a-new-row",
                 "label": "Only a new row: January unchanged, March inserted and read after",
                 "items": "january, 400, 400, before, update; march, 0, 120, after, insert",
                 "expect": {"olSeen": "520", "olConsistent": "yes: the state after the commit",
                            "olLevel": "none needed: no read straddles the commit"}},
                # F16, PDF pp. 73 and 80 of the operator's copy.
                {"id": "martin-and-david",
                 "label": "Martin and David again: new files, read across the commit (the book's illustration)",
                 "items": "locking, 7, 9, before, insert; multiphase, 5, 8, after, insert",
                 "expect": {"olConsistent": "no: 15 is neither 12 nor 17",
                            "olLevel": "repeatable read allows it (a phantom); serializable prevents it"}},
            ],
            "panel_title": "The read error, and the level that prevents it",
            "panel_intro": (
                "Each record is one item: its value before and after one commit, the side of "
                "the commit it was read on, and whether the commit inserted rows or updated "
                "them. The levels are the four standard ones Chapter 5 describes; the last "
                "tile names the read error and the weakest level that prevents it."
            ),
        }),
        "steps_title": "Naming a read error",
        "steps_intro": "Four steps, the last of them on your own database.",
        "steps": [
            ("Find the stale reads",
             "Mark every item that the commit changed and that was read before it. If there "
             "is none, or no fresh read either, the reads are of one state and no level is "
             "needed."),
            ("Look at how each stale item changed",
             "An updated value read stale is an unrepeatable read. Rows inserted after the "
             "read are a phantom. If any stale item was updated, the error is the "
             "unrepeatable read."),
            ("Name the weakest level that prevents it",
             "Repeatable read prevents an unrepeatable read; only serializable prevents a "
             "phantom. Read committed allows both, and read uncommitted allows dirty reads "
             "besides."),
            ("Do it on your own database",
             "Look up the isolation level your database runs at by default, and what its "
             "documentation says that level does. Write down which of the three read errors "
             "it allows, and whether it is really snapshot isolation under another name."),
        ],
        "worked": {
            "title": "Quarter totals",
            "intro": [
                "The preset quarter-totals, worked by hand.",
            ],
            "lines": [
                "before: 400 + 300 + 0 is 700",
                "after: 400 + 350 + 120 is 870",
                "seen: 400 + 300 + 120 is 820",
                "January: unchanged, so neither",
                "February: read before, updated: stale",
                "March: read after, inserted: fresh",
                "stale update: an unrepeatable read",
            ],
            "after": [
                "Read committed lets February's old value through; repeatable read would have "
                "held February steady for the whole transaction. If February had only gained "
                "rows, the error would be a phantom, and only serializable would stop it.",
            ],
        },
        "quiz_title": "Levels, errors and the section's claims",
        "quiz": [
            {"q": "Work the exercise: north 12 then 12, read before; south 8 then 11, rows "
                  "inserted, read before; east 5 then 7, updated, read after. The stale item "
                  "decides: an update is an unrepeatable read, an insert a phantom. What is "
                  "the error, and the weakest level that prevents it?",
             "a": ["A phantom, from south's inserted rows; only serializable prevents it",
                   "An unrepeatable read, from east's update; repeatable read prevents it",
                   "None: the total of 27 lies between 25 and 30",
                   "A dirty read; read committed prevents it"],
             "c": 0,
             "why": "The reader saw 12 + 8 + 7 = 27, against 12 + 8 + 5 = 25 before and "
                    "12 + 11 + 7 = 30 after, so it matches neither state. North did not "
                    "change. East was read after its update, so it is fresh, not stale. South "
                    "is the only stale item, and its change was an insert: a phantom, which "
                    "repeatable read allows and serializable prevents. Lying between the two "
                    "totals is not being one of them."},
            {"q": "Martin runs the serializable version of the count while David commits his "
                  "new files. By Chapter 5's definition of serializable, which totals can the "
                  "routine return?",
             "a": ["Only 12: serializable runs transactions in the order they began",
                   "12 or 17, without a promise which",
                   "Always 17, because David's commit is the later one",
                   "12, 15 or 17"],
             "c": 1,
             "why": "Serializable promises the result of some order of running the transactions "
                    "one after another: Martin entirely before David (12) or entirely after "
                    "(17). Chapter 5 says it cannot promise which, only that it is a correct "
                    "one. Fifteen is the straddled read serializable rules out."},
            {"q": "What does Chapter 5 say straight after advising serializable for correctness?",
             "a": ["That every transaction should therefore run at it, whatever it costs",
                   "That it is needed only for business transactions, not system ones",
                   "That it costs so much liveness that you often lower it for throughput",
                   "That read committed is the right default level for every system"],
             "c": 2,
             "why": "The advice comes with its price in the very next sentence: serializable "
                    "hurts liveness badly enough that systems commonly step down a level to get "
                    "the throughput they need, and you weigh errors against performance "
                    "transaction by transaction. The chapter names no default."},
            {"q": "What policy does Application Server Concurrency state on explicit locks and "
                  "synchronisation in application code?",
             "a": ["Use them in every class that two threads might share",
                   "Replace them with deadlock detection and timeouts",
                   "Pool every object and synchronise access to the pools",
                   "Arrange things so that application code seldom needs them"],
             "c": 3,
             "why": "Because such bugs can hardly ever be reproduced, the authors aim to keep "
                    "locks and synchronisation out of application code wherever they can, and "
                    "to isolate each request's objects instead. They synchronise only "
                    "explicit pools of expensive things, such as connections, and recommend "
                    "fresh objects over pooled ones."},
        ],
        "mistakes": [
            ("Using serializable for every transaction",
             "Serializable prevents every read error the standard names, so it looks like the "
             "safe default. Chapter 5 gives the advice and its cost in consecutive sentences: "
             "serializable costs so much liveness that systems often step down a level for "
             "throughput, and each transaction can be given its own level. The point "
             "of knowing the levels is knowing which errors a weaker one lets through, as the "
             "lab names them on the lesson's illustrations."),
            ("Thinking isolation levels are about writes",
             "They govern what a transaction can read of others' work: uncommitted data, a "
             "value that changes under it, rows that appear while it reads. The "
             "database's own write locks stop two transactions changing one row at the same "
             "instant at every level, but that does not make every write safe: a transaction "
             "that reads a value and writes back a result can still lose another's update at "
             "a weak level. The levels, as the chapter states them, decide how consistent a "
             "transaction's reads are."),
            ("Ruling out long transactions on principle",
             "The general advice is to keep transactions short, and long transactions do not "
             "scale. But the chapter also says that a database with little contention may "
             "cope with a business transaction run as one long transaction, and that where it "
             "does, that is the better course, since it sidesteps many of the offline "
             "problems. The offline patterns are for when you cannot."),
        ],
        "standard": (
            "Finish when you can name a read error and the level that stops it.",
            "Given reads on both sides of a commit and whether each stale item was updated or "
            "had rows inserted, name the read error and the weakest of the four standard "
            "isolation levels that prevents it."
        ),
        "note": (
            "The lab names levels by the standard's definitions, as Chapter 5 does. Your "
            "database may implement a level more strongly, or offer snapshot isolation, which "
            "the four names do not describe, and only its documentation can say which errors "
            "it allows. The lab also has one commit and no rollback, so it cannot show a dirty "
            "read."
        ),
    },
]
