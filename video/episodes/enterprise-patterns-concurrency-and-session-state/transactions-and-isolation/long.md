---
format: long
lesson: enterprise-patterns-concurrency-and-session-state/transactions-and-isolation
title: Transactions and isolation levels: what each one lets through
thumb: Each level lets one more through
---

@chapter The promise
@title text="Transactions and Isolation" sub="Patterns of Enterprise Application Architecture, Chapter 5" art=thumb
What does a transaction actually promise you? And what do the weaker isolation levels give away, for the sake of speed?

@quote text="To be sure of correctness you should always use the serializable isolation level." cite="Fowler and Rice, Patterns of Enterprise Application Architecture, Chapter 5"
Here's a sentence from the chapter. To be sure of correctness you should always use the serializable isolation level. Keep reading, though, because the next sentence gives its cost.

@art all-or-nothing
A transaction is a bounded piece of work. It leaves everything it touches in a consistent state, and it happens all or not at all. The book says database for any transactional resource, message queues and printers included.

@list heading="ACID" items="Atomicity: all or nothing@Atomicity|Consistency: sound at start and end@consistency|Isolation: unseen until commit@isolation|Durability: survives a crash@and durability"
The promise is ACID. Atomicity: every step completes, or all roll back. Then consistency: sound at the start and the end. Then isolation: nobody else sees the result until it commits. And durability: a committed result survives a crash.

@chapter Keep it short
@art request-transaction
Transaction systems want transactions short, so don't let one span several requests. The simple model is the request transaction, opened when a request begins and closed when it ends. A late transaction reads outside, and opens only to write, which leaves the reads unprotected.

@chapter Four levels
@words text="Serializable" sub="as if run one after another"
Transactions are serializable when running them together gives the result of some order of running them one after another. So Martin, counting under serializable, gets twelve or seventeen. Which one isn't promised. But it's a correct one.

@art isolation-ladder
The SQL standard defines four levels, and in the chapter's retelling, each step down lets one more kind of read error through.

@list heading="Each step down" items="Repeatable read: phantoms@Repeatable read|Read committed: + unrepeatable reads@Read committed|Read uncommitted: + dirty reads@Read uncommitted"
Repeatable read allows phantoms: rows inserted while you read, seen in some reads and not others. That's Martin's case, since David added files. Read committed also allows unrepeatable reads: a value updated under you. Read uncommitted also allows dirty reads, of data that may yet roll back.

@words text="Serializable costs liveness" sub="choose a level for each transaction"
And the cost? Straight after that opening sentence, the authors say serializable damages liveness so much that you often have to step down for throughput. You decide which risks to take, and each transaction can have its own level.

@chapter In code
@code block=1 lines=1-8 label=Java focus="3@stops the driver|4@serializable|5@both counts|6@commit"
Here's the first lesson's routine, made safe. Turning off auto commit stops the driver committing after each statement. Then it asks for serializable, runs both counts, and calls commit. Now it returns twelve or seventeen, never fifteen. Or it throws, if the database aborts it to keep the promise.

@chapter Name the error
@math heading="quarter-totals" items="Jan 400 · Feb 300 → 350 (update), read before@February;;Mar 0 → 120 (insert), read after@March;;seen 820 · before 700 · after 870@eight hundred and twenty;;unrepeatable read: repeatable read prevents it@unrepeatable"
In the lab, the stale item decides. January is four hundred and unchanged. February goes from three hundred to three hundred and fifty, read before. March goes from zero to one hundred and twenty, read after. The reader sees eight hundred and twenty: not seven hundred, not eight hundred and seventy. February's change was an update, so it's an unrepeatable read.

@art phantom-row
Load Martin's preset, though, and the stale read is locking, where David's change was new files, an insert. That's a phantom, which repeatable read allows, and only serializable prevents.

@words text="Snapshot isolation" sub="a development since the book"
One thing has changed since the book. Many databases give each transaction a snapshot, which the four levels don't name. It shows none of the three errors, but allows write skew. And it ships under different names, so the name alone no longer tells you which errors you're choosing.

@chapter Business transactions
@art business-vs-system
The user's business transaction, choosing an account, setting up payments and pressing OK, should be ACID too. If the database isn't under heavy load, run it as one long system transaction. Otherwise, it's a run of short ones, and isolation is the hard part. That's where Optimistic Offline Lock, the authors' first choice, comes in.

@art threads-processes
Inside the server, the authors keep explicit synchronisation out of application code. It behaves ninety nine percent of the time, and fails at random for the rest. Create fresh objects for each request, and keep them out of statics and singletons.

@chapter Where people slip
@list heading="Common slips" items="Serializable everywhere@The first|Isolation levels are about writes@The second|Long transactions, never@And the third"
The first slip is using serializable everywhere. It costs liveness. The second is thinking isolation levels are about writes. They decide how consistent your reads are. And the third is ruling out long transactions on principle. With little contention, one long transaction may be the better course.

@chapter Try it
@code block=2 lines=1-3 label=Records focus="1@north|2@south|3@east"
Your turn. Three regions around one commit. North stays at twelve, read before. South goes from eight to eleven by an insert, read before. East goes from five to seven by an update, read after. Find the totals, the stale item, the read error, and the weakest level that prevents it.

@end text="Name the read error"
You can replay a commit and name the error it causes, on Learn. That's learn dot get er done dot I O.
