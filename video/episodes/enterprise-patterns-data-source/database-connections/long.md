---
format: long
lesson: enterprise-patterns-data-source/database-connections
title: Database connections, the Registry, and batching
thumb: One trip, many statements
---

@chapter The connection
@title text="Database Connections and Registry" sub="Patterns of Enterprise Application Architecture, Chapters 3 and 18" art=thumb
Every statement your mappers send goes through a connection. Fowler's short sections on connections say how to open one, how to find one, when to close one, and how to stop paying the same wait over and over.

@art connection-pipe
A connection is the link between your code and the database. It's opened before any command runs, and held open while the command, and any transaction it belongs to, takes place.

@art pool
Connections are often expensive to create, so environments pool them. Fowler notes that most platforms now do the pooling for you. A pool behind an interface that looks like opening a fresh connection is a good thing, because the choice to pool is properly encapsulated.

@chapter Keeping it, closing it
@art transaction-bracket
Close a connection as soon as you're done, and keep every command of one transaction on the same connection. Closing by hand is easy to forget, he admits of himself. So his preference is to tie the connection to the transaction: open it when the transaction begins, and close it at commit or rollback.

@art parameter-chain
The other problem is having the connection wherever it's needed. Passing it as a parameter adds it to all sorts of calls whose only use for it is to hand it on.

@chapter The Registry
@art registry-board
That's where a Registry comes in: a well known object others use to find common objects and services. Fowler prefers static methods as its interface, but doesn't let that make its data static. A connection is thread data, held in thread local storage behind the same static method.

@words text="Guilty until proven innocent" sub="Fowler, on any global data"
He's uncomfortable with it all the same, because a Registry is still global data. Pass the object as a parameter if you can. He takes a Registry when the parameter would sit unused in nine of every ten calls that carry it. Any global data, he says, is guilty until proven innocent.

@chapter Three habits
@list heading="Some miscellaneous points" items="No SELECT * with column positions@SELECT star|Static SQL, not concatenation@static SQL|Batch statements into one call@batch"
Chapter three adds three habits. Don't use SELECT star with positional column indices, since a reordered column then breaks the code. Prefer static SQL that can be precompiled, and avoid building queries by string concatenation. And batch statements into one call, where the platform allows it.

@quote text="Many environments give you the ability to batch multiple SQL queries into a single database call." cite="Fowler, Patterns of Enterprise Application Architecture, Chapter 3"
Many environments give you the ability to batch multiple SQL queries into a single database call. Fowler adds that his examples don't do it, but production code should.

@code block=1 lines=1-13 label=Java focus="4-5@prepares one INSERT|6-11@calls addBatch|12@executeBatch"
Here's how it looks in JDBC. The connection is a parameter, the choice Fowler prefers. It prepares one INSERT, and for each line of an order it sets the placeholders and calls addBatch, which queues the statement. Then executeBatch sends them all in one call.

@chapter The arithmetic
@math heading="save-an-order · 25 statements, 2 ms wait, 0.5 ms work" items="one at a time: 25 × (2 + 0.5) = 62.50 ms@one at a time;;waiting: 50 ÷ 62.5 = 80%@waiting;;3 batches: 3 × 2 + 25 × 0.5 = 18.50 ms@three batches;;125/37 ≈ 3.4× faster@times faster"
A save makes one insert for the order, twelve for its lines, and twelve stock updates, with illustrative timings. One at a time, that's twenty five round trips and sixty two and a half milliseconds, and eighty percent of it is waiting. In three batches, it's eighteen and a half milliseconds, about three point four times faster.

@art batch-trip
The lab holds the work the same, so the saving is all in the waits. Batching removes twenty two of the twenty five.

@math heading="same-machine · 0.1 ms wait" items="15 ms one at a time@fifteen milliseconds;;12.80 ms batched@twelve point eight;;75/64 ≈ 1.2×@one point two"
Now put the database on the same machine, with a tenth of a millisecond's wait. It's fifteen milliseconds against twelve point eight, about one point two times faster. Where the waits are short, batching has little to remove, and only your own measurement says which case you're in.

@chapter Where people slip
@list heading="Common slips" items="Batching makes the database do less@The first|A Registry is always wrong@The second|Build your own pool@And the third"
The first slip is thinking batching is faster because the database does less work. It removes waits. The second is thinking a Registry is always wrong. It's a last resort, scoped to a thread. And the third is building a connection pool as a matter of course, when most platforms already pool.

@chapter Try it
@words text="1 invoice + 40 items, two batches" sub="3 ms wait · 0.2 ms work a statement"
Your turn. A save inserts one invoice and forty items, in two batches. The wait is three milliseconds, and the work is a fifth of a millisecond a statement. Work out the time one at a time and in batches, the share spent waiting, and how many times faster the batches are.

@end text="Batch a save yourself"
You can change the wait and the batches and watch the saving, on Learn. That's learn dot get er done dot I O.
