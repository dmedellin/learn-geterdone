---
format: long
lesson: enterprise-patterns-objects-and-tables/unit-of-work
title: Unit of Work: write it all at commit, once per object
thumb: Six writes become two
---

@chapter Saving as you go
@title text="Unit of Work" sub="Patterns of Enterprise Application Architecture, Chapters 3 and 11" art=thumb
You've probably written a save that runs as it goes. Load the order, change its status, write it. Add a line, write it. Change your mind about the line, delete it. Each step is correct, and the database sees every one of them.

@art scattered-writes
Fowler's argument starts there. People talk about object relational mapping as structure, how tables relate to objects. But the harder part is behaviour. Once you've loaded a number of objects and changed some, you must know which ones to write back. With a couple of records, that's easy. With many, some new, it becomes an exercise.

@chapter The idea
@art ledger
His answer is an object that does the remembering. A Unit of Work keeps track of the objects read, and the objects created, changed or deleted. At commit, it works out the database work itself. It starts a transaction, runs any concurrency check, and writes the changes out.

@quote text="Instead of the application programmer invoking explicit save methods, the programmer tells the unit of work to commit." cite="Fowler, Patterns of Enterprise Application Architecture, Chapter 3"
That's the whole pattern. Instead of the application programmer invoking explicit save methods, the programmer tells the unit of work to commit.

@chapter How it learns
@art three-registrations
How does it learn of a change? With caller registration, the code that changes an object must remember to register it, and anything forgotten is silently not written. With object registration, the object's own setters do it. Or a controller keeps a copy of each object it reads, and compares at commit.

@chapter The code
@code block=1 lines=1-20 label=Java focus="4@one map|5-10@mark decides|7@keeps its mark|8@becomes GONE|11-19@The commit"
Here's one written for the lesson. It holds one map from object to mark. And mark decides what a new mark does to the old one. A new or removed object keeps its mark. A new object that's then removed becomes GONE. The commit walks the map once, writing an insert, an update or a delete. GONE writes nothing.

@chapter The count
@words text="load order7 · change order7 · new line1 · new line2" sub="change order7 · delete line2 · load customer3 · change line1"
The lab runs a script. Load order seven and change it. Create line one and line two. Change order seven again, delete line two, load customer three, and change line one.

@math heading="edit-an-order" items="at once: 6 writes@at once;;at commit: INSERT line1; UPDATE order7@at commit;;saved: 4 of 6 = 2/3 ≈ 66.7%@saving four;;customer3: left clean@customer three"
Written at once, that's six writes. At commit, it's two: insert line one, and update order seven. That's saving four, two thirds of them. And customer three, loaded and never changed, is left clean.

@art created-deleted
That's Fowler's argument as a number. The line that was added and deleted never reaches the database at all. Order seven, changed twice, is written once in its final state. And line one is one insert, however often it changed after it was made.

@math heading="delete-loaded" items="at once: 3 writes@three writes;;at commit: UPDATE a1; DELETE a2@update a one;;saved: 1/3 ≈ 33.3%@a third"
But deleting a loaded object still costs. Load a one and a two, change a one, delete a two, and change a one again. That's three writes at once, and two at commit: update a one, delete a two. Saving one, a third. Only a row that never existed costs nothing.

@art commit-once
The alternatives are saving each object whenever you alter it, keeping changed objects in variables, or a dirty flag on each one, which is hard to find across a network of objects. The pattern's great strength, Fowler concludes, is that it keeps all this in one place.

@chapter Where people slip
@list heading="Common slips" items="It's a database transaction@The first|Saving at once is safer@The second|The commit orders writes for the keys@And the third"
The first slip is taking a Unit of Work for a database transaction. It's a record of changes in memory, which becomes a short transaction at commit. The second is thinking saving each change at once is safer. Nothing is lost by waiting. And the third is expecting the commit to order the writes for the database's keys.

@art key-order
It doesn't. A line written before its order can break a foreign key. The Unit of Work is the obvious home for that ordering, and a later lesson counts how.

@chapter Try it
@words text="invoice4 · payment1 · account2 · note1"
Your turn. Load invoice four, create payment one, change invoice four twice. Load account two and change it. Create note one, delete it, and change payment one. Count the writes at once, list the statements at commit, inserts first, and give the share saved.

@end text="Run a script yourself"
You can type a script of changes and watch the commit shrink it, on Learn. That's learn dot get er done dot I O.
