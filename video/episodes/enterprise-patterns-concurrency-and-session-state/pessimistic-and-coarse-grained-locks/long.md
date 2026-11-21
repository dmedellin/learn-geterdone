---
format: long
lesson: enterprise-patterns-concurrency-and-session-state/pessimistic-and-coarse-grained-locks
title: Pessimistic and coarse-grained locks: refuse early, lock the group
thumb: Lock the order, not the line
---

@chapter Why prevent
@title text="Pessimistic and Coarse-Grained Locks" sub="Patterns of Enterprise Application Architecture, Chapter 16" art=thumb
With an optimistic lock, when several people work on the same data, one commits and the others fail. And they find out only at the end, after all the work. On long business transactions, that soon makes a system unpopular.

@quote text="Pessimistic Offline Lock prevents conflicts by avoiding them altogether." cite="David Rice, in Fowler, Patterns of Enterprise Application Architecture, Chapter 16"
David Rice's answer is the other side. Pessimistic Offline Lock prevents conflicts by avoiding them altogether. The business transaction locks the data before touching it, so a session that has started can usually expect to finish.

@chapter Three choices
@list heading="Kinds of lock" items="Exclusive write: needed only to edit@exclusive write|Exclusive read: needed even to load@exclusive read|Read/write: many readers or one writer@read write"
First, the kind of lock. An exclusive write lock is needed only to edit. An exclusive read lock is needed even to load, and it restricts concurrency severely. A read write lock combines them: many readers, or one writer. Choose one the domain's analysts can understand.

@art lock-manager-table
Second, the lock manager: a table from locks to their owners, and exactly one of it. Once the servers are clustered, it probably belongs in the database, since a table in one server's memory only works if you're pinned to that server.

@art lock-before-load
Third, the protocol. Take the lock before you load the data, since a lock is little use without the latest version. Lock the record's id, so you can lock before you load. And release the locks when the business transaction completes.

@art refuse-not-wait
If a lock can't be had, abort, and the earlier the better. Don't wait. A business transaction might take twenty minutes, so the lock manager should refuse at once, which also takes deadlock off the table. And give abandoned sessions a timeout.

@chapter Lock the group
@art root-lock
Locking every object in a group means finding every member, and a large lock set crowds the table. Coarse Grained Lock, by Rice and Matt Foemmel, uses one lock for the group. Optimistically, the members share one version. Pessimistically, they share a token. For an aggregate, lock the root, and every member is locked.

@code block=1 lines=1-10 label=Java focus="3@builds a key|5-6@refuses the edit"
Here's a root lock in miniature. It doesn't lock the line it's given. It builds a key from the line's order, so every line of one order asks for the same lock. If another session holds that key, it refuses the edit at once. No waiting.

@chapter Replay it
@art line-locks
In the lab, Kim edits line one at minute zero, and Lee edits line two at one. They commit at four and five. With a lock per line, both commit, nobody is refused, and at most two locks are held.

@math heading="order-lock: both lines in order9" items="committed: kim@Kim commits;;refused: lee@Lee is refused;;most locks held: 1@one lock"
Now put both lines in one order. Kim commits, Lee is refused at minute one, and at most one lock is held. Lee is refused although the lines are different rows. That's the cost. It's also the point, if the order has a rule that spans its lines, like a credit limit.

@math heading="optimistic-groups" items="committed: kim@Kim commits;;conflict: lee@Lee conflicts;;minutes redone: 4@four minutes"
Switch the scheme to optimistic, and the order becomes a shared version. Kim commits, Lee conflicts at her commit at minute five, and four minutes are redone. The grouping protects the order either way. The scheme decides whether Lee hears at the start or the end.

@words text="The business's grouping comes first" sub="cheaper locking is a second reason"
The first reason to use a coarse lock, the authors say, is the business's need to edit the group as one. Cheaper locking is a second. And don't invent unnatural relationships just to get it.

@chapter Implicit Lock
@quote text="if an item might be locked anywhere it must be locked everywhere." cite="David Rice, in Fowler, Patterns of Enterprise Application Architecture, Chapter 16, Implicit Lock"
A locking scheme with one gap is no scheme. Forget one line that takes a lock, and the scheme is useless, and testing rarely finds it. In Rice's words: if an item might be locked anywhere, it must be locked everywhere.

@art implicit-lock
So the framework, or a layer supertype, takes the locks nobody may forget. Write locks are the exception: the framework checks at commit that the lock was taken, and throws if not.

@chapter Where people slip
@list heading="Common slips" items="A finer lock is always better@The first|Making pessimistic locks wait@The second|Leaving each lock to its developer@And the third"
The first slip is thinking a finer lock is always better. It protects the least. The second is making pessimistic locks wait. Refuse at once. And the third is leaving each lock to the developer who needs it. One forgotten lock breaks the scheme.

@chapter Try it
@code block=2 lines=1-6 label=Timeline focus="1-3@three rooms|4-6@commit"
Your turn. Ann, Bo and Cy edit three rooms. Rooms one and two are on floor one, and room three is on floor two, and the locks are on floors. They commit at three, seven and eight. Who commits, who's refused and when, how much work is lost, and what's the most locks held?

@end text="Lock the group yourself"
You can group records and replay the timeline in the lab, on Learn. That's learn dot get er done dot I O.
