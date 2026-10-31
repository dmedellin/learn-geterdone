"""Course 6 -- Concurrency and Session State: Chapters 5, 6, 16 and 17.

Seven lessons: part_a reads Chapter 5, Concurrency (by Martin Fowler and David
Rice); part_b reads Chapter 16's offline locks (David Rice's, Coarse-Grained
Lock with Matt Foemmel), Chapter 6, Session State, and Chapter 17's three
session state patterns. Fowler et al., Patterns of Enterprise Application
Architecture (Addison-Wesley, 2002). The design is
docs/enterprise-patterns/PLAN.md, section C, Course 6.
"""

from . import part_a, part_b

COURSE = {
    "slug": "enterprise-patterns-concurrency-and-session-state",
    "title": "Concurrency and Session State",
    "level": "Intermediate",
    "summary": (
        "Chapter 5, Concurrency, by Martin Fowler and David Rice; Chapter 16, Offline "
        "Concurrency Patterns, whose Optimistic Offline Lock, Pessimistic Offline Lock and "
        "Implicit Lock are Rice's and whose Coarse-Grained Lock is Rice's and Matt Foemmel's; "
        "Chapter 6, Session State; and Chapter 17, Session State Patterns. What goes wrong when "
        "two people work on the same data, how transactions and locks prevent or detect it, "
        "and where a session's state lives between requests. Each lesson sets out the "
        "argument and counts its trade-off on a stated situation: what a reader saw across a "
        "commit, who commits and who is refused or conflicts on a timeline, the minutes of "
        "work a failure discards, the server objects a load needs, and the bytes each place "
        "for session state moves and holds."
    ),
    "blurb": (
        "Read Fowler's and Rice's chapter on concurrency and the offline locks that follow "
        "from it, then Fowler's two chapters on session state. Replay timelines of sessions "
        "under no control, optimistic and pessimistic locking, name the read error a commit "
        "causes and the isolation level that stops it, and count the objects and bytes that "
        "stateless servers and each place for session state cost."
    ),
    "key": [
        "lost update and inconsistent read",
        "optimistic detects; pessimistic prevents",
        "a stale update is an unrepeatable read",
        "a version in the WHERE, a row count back",
        "lock before loading; refuse, never wait",
        "stateless objects: users × service / think",
        "client state crosses the wire both ways",
    ],
    "assumes_short": "Layers and Performance",
    "assumes_long": (
        "Layers and Performance, for the three layers and the vocabulary of performance, and "
        "enough of the two database courses to know what a row, an UPDATE and a commit are; "
        "the code is short Java, with JDBC calls explained where they appear"
    ),
    "outcomes_intro": (
        "By the end you can do, on a stated situation, the counts these chapters make in "
        "words, and say in their terms what each count shows and what it leaves to your own "
        "system."
    ),
    "outcomes": [
        ("Say what a reader saw across a commit",
         "Given items read on either side of one commit, compute the total seen and both "
         "states, say whether they match, and name the read error and the weakest isolation "
         "level that prevents it."),
        ("Replay a timeline under each scheme",
         "Given a timeline of reads, edits and commits, state who commits, who conflicts and "
         "who is refused under no control, optimistic and pessimistic locking, and how many "
         "minutes of work each failure discards."),
        ("Use a version check and a coarse lock",
         "Read a save that checks a version in its WHERE, say what a row count of zero means, "
         "what checking reads adds, and what one lock for a group changes against a lock per "
         "record."),
        ("Count the objects a load needs",
         "Compute the stateful and stateless server objects for a number of users, a service "
         "time and a time between requests, and the share of the time a stateful object is "
         "idle."),
        ("Price the places for session state",
         "Compute the bytes client session state puts on the wire, what server session state "
         "holds in memory and what database session state moves, and say which of Fowler's "
         "considerations the bytes leave out."),
    ],
    "syllabus_intro": (
        "Seven lessons in the narratives' order: three on Chapter 5, the problems, the two "
        "forms of control, and transactions; two on Chapter 16's offline locks, the "
        "optimistic one, and the pessimistic one with its coarse-grained and implicit "
        "companions; one on Chapter 6's case for statelessness; and one on session state, "
        "read with Chapter 17's three patterns."
    ),
    "how_to": [
        "Read the chapter before the lesson. This is a read-along of Fowler et al., "
        "<em>Patterns of Enterprise Application Architecture</em> (Addison-Wesley, 2002), with "
        "code written for these lessons. Chapter 5 is by Martin Fowler and David Rice; three of "
        "Chapter 16's patterns are Rice's and the fourth Rice's and Matt Foemmel's, and the "
        "lessons name them. Each lesson cites the book by chapter, section and pattern, opens "
        "with at most one short quotation, and sets out the argument in its own words. The "
        "book's own examples are better read in the book.",
        "Expect timelines, not running code. The concurrency labs replay a timeline of "
        "sessions that the lesson states, minute by minute, and count what each scheme "
        "commits, refuses and loses. Real concurrency bugs cannot be reproduced on demand, "
        "which is the chapter's own reason for preferring designs that avoid them: isolation, "
        "immutability, and transactions that the database manages for you.",
        "Treat each count as a model of the situation. The figures come from what the "
        "lesson states: who reads and writes when, how long a request takes, how big a "
        "session is. How often your sessions really collide, and how long your users really "
        "wait between requests, are figures only your own system can give, and they are the "
        "ones Fowler's choices depend on.",
        "Try your own timeline. Every lab takes what you type, and every lesson ends by "
        "sending you to a record, a report or a session of your own. Nothing you type leaves "
        "your browser.",
    ],
    "not_covered": [
        "Explicit thread programming and the internals of database locking. Application "
        "Server Concurrency's policy is read, to avoid explicit synchronisation where you "
        "can, and the database's own locks and isolation are named as Chapter 5 names them; "
        "neither is taught.",
        "The book's examples and listings: the lock managers, mappers and session code of "
        "Chapters 16 and 17, and Table 5.1. They are named in the lessons, and the table's "
        "content is stated in the lesson's own words.",
        "Exclusive read locks, read/write locks, deadlock detection and lock timeouts. The "
        "lessons describe them as the book does; the lab models one exclusive write lock "
        "that is refused at once, never waited for.",
        "Merging conflicting business data, which Rice calls a pattern of its own and leaves "
        "aside, and the temporal reads Chapter 5 mentions.",
        "What has changed since 2002, except one development: snapshot isolation in "
        "multiversion databases, set beside Chapter 5's four levels in Transactions and "
        "Isolation. The platform advice of Chapter 17 (HTTP sessions, stateful session beans, "
        ".NET's session state) is named, not taught.",
    ],
    "footer_lead": (
        "Every figure in this course is computed in your browser from what a lesson states: "
        "a total from the values read on each side of a commit, who commits and who fails "
        "by replaying the timeline the lesson gives, server objects from users and timings, "
        "and bytes from a session's size. The code is written for these lessons; figures "
        "the book gives are marked as the book's illustrations. A count models the "
        "situation; it is not a measurement of your system."
    ),
    "lessons": part_a.LESSONS + part_b.LESSONS,
}
