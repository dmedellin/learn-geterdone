---
format: long
lesson: enterprise-patterns-data-source/row-data-gateway-and-finders
title: One query or fifty? Row Data Gateway and finders
thumb: Every query pays the wait
---

@chapter An object per row
@title text="Row Data Gateway, and Reading in Data" sub="Patterns of Enterprise Application Architecture, Chapters 3 and 10" art=thumb
Should you fetch exactly the rows you need, one at a time, or grab more than you need in one go? Fowler has a rule of thumb, and then a warning about rules of thumb.

@art row-object
First, the pattern those queries load. A Row Data Gateway is an object that looks exactly like one record. Each column becomes a field, the gateway converts the database's types to the language's, and every detail of reaching the database is behind its interface. It holds no business rules.

@art three-representations
Fowler uses it most with a Transaction Script, so several scripts can share the database code. Not with a Domain Model. Put a gateway under a large Domain Model, and you have three representations of the data, in the domain, the gateway and the database. That, he says, is one too many.

@chapter Where finders go
@code block=1 lines=1-18 label=Java focus="3-4@id and status|11@static|12-13@one keyed SELECT|16@returns null"
Here's the lesson's version. OrderRow holds an order's id and status. Its finder is static, just for brevity, and runs one keyed SELECT, building the row, or it returns null when there's none.

@art finder-object
But a static method can't be swapped for another, so a test can't replace the database with a stand in, a Service Stub. So Fowler prefers separate finder objects, one finder class for each table, each method wrapping one SELECT and returning row objects.

@art memory-vs-db
There's a warning here that's easy to miss. A finder reads the database, not what's in memory. Add a line to an order in memory, then run a finder for its lines, and the new one isn't there. His advice: do queries at the beginning.

@chapter Many rows at once
@quote text="It's usually better to use one query that brings back unnecessary rows than to issue 50 individual queries." cite="Fowler, Patterns of Enterprise Application Architecture, Chapter 3"
Then his rules of thumb. Pull back many rows at once. Never query one table repeatedly to get several rows. As he puts it, it's usually better to use one query that brings back unnecessary rows than to issue fifty individual queries.

@art broad-query
His illustration: you need fifty people you can name by primary key, but the only query you can write brings back two hundred, and further logic picks out the fifty. That one query is usually better than fifty.

@chapter The arithmetic
@math heading="fifty-or-one · 5 ms a statement, 0.1 ms a row" items="keyed: 50 × (5 + 0.1) = 255 ms@fifty keyed finds;;broad: 5 + 200 × 0.1 = 25 ms@the broad query;;batched: 5 × 5 + 50 × 0.1 = 30 ms@batches of ten"
The fifty and two hundred are the book's. The timings are illustrative. Fifty keyed finds, each paying five milliseconds plus a tenth for its row, take two hundred and fifty five milliseconds. The broad query pays the wait once, plus two hundred rows: twenty five milliseconds. Finds in batches of ten, the lab's own strategy, take thirty.

@art many-trips
So fifty keyed finds take about ten times as long as one query that returns four times the rows. Forty nine of their fifty waits are the cost.

@math heading="local-database · 0.2 ms a statement" items="keyed: 15 ms@keyed finds;;broad: 20.20 ms@the broad query;;batched: 6 ms@batches"
Now put the database on the same machine, so the wait falls to a fifth of a millisecond. Keyed finds take fifteen milliseconds. The broad query takes twenty point two. Batches take six. The advice reverses on its own figures. With a short wait, the hundred and fifty unwanted rows cost more than the extra statements.

@words text="Profile with your own database"
That's why Fowler ends the section with his own caveat. Profile with your own database and data, because for every rule of thumb he's heard of surprising exceptions.

@chapter Where people slip
@list heading="Common slips" items="Fetching only what you need is cheaper@The first|A static finder is as good@The second|A rule of thumb is a measurement@And the third"
The first slip is thinking fetching only the rows you need is always cheaper. Every statement pays the wait. The second is thinking a static finder is as good as a finder object. A test can't replace it. And the third is taking the rule of thumb for a measurement.

@chapter Try it
@words text="30 wanted · 600 returned · batches of 15" sub="4 ms a statement · 0.05 ms a row"
Your turn. You want thirty rows, the broad query returns six hundred, and batches hold fifteen keys. Each statement waits four milliseconds, and each row costs five hundredths. Work out all three times, and say which is fastest.

@end text="Time the queries yourself"
You can change the wait and the row cost and watch the winner change, on Learn. That's learn dot get er done dot I O.
