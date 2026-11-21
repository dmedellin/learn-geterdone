---
format: long
lesson: enterprise-patterns-domain-logic/table-module-and-making-a-choice
title: Table Module, and how Fowler says to choose
thumb: One object, every row
---

@chapter The third way
@title text="Table Module, and Making a Choice" sub="Patterns of Enterprise Application Architecture, Chapters 2, 9 and 18" art=thumb
Fowler's third way of organising domain logic sits between the other two. Then he tackles the question everyone wants answered: which one should you use? His answer starts with bad news.

@chapter One object, many rows
@art one-per-row
A Table Module gives each table one class, and one instance of it carries every operation on that table's data. Here's the main difference from a Domain Model. With many orders, a Domain Model has an object for each order. A Table Module has one object for all of them.

@art key-lookup
So the module has no notion of identity for the rows it works with. To ask about one row, you call a method on the module and pass the row's key, usually the database's primary key.

@code block=1 lines=1-16 label=Java focus="2-3@whole invoice line table|9@passes its key|11-13@walks the rows"
Here's one in small. One InvoiceLines object for the whole invoice line table, given a Record Set when it's made. To total one invoice, the caller passes its key, and the module walks the rows with that key.

@chapter The Record Set
@art record-grid
A Table Module is usually backed by a Record Set, the result of a query held in memory, in the shape the query returned. Domain code can build one or change it too.

@art round-trip
The flow Fowler describes is a round trip. A gateway fills a Record Set, a module works on it, table aware widgets show and edit it, and the module validates it again before it's saved.

@words text='r.getLong("cents")' sub="a column named by a string"
Most Record Sets ask for a column by name, as a string. Fowler generally frowns on that. He minds it less here, because a Record Set usually carries its legal columns. His advice: where the environment relies on Record Sets, organise the domain logic with a Table Module.

@chapter Counting objects
@math heading="small-shop" items="200 + 1,500 + 120 + 6,000 = 7,820 rows@two hundred customers;;one a row: 7,820 objects@One object a row;;one a table: 4 objects@one a table"
The lab counts objects. A small shop has two hundred customers, fifteen hundred orders, a hundred and twenty products, and six thousand lines. That's seven thousand eight hundred and twenty rows. One object a row gives seven thousand eight hundred and twenty objects. One a table gives four.

@words text="Objects, not memory" sub="a difference in kind, not a saving"
But read the banner. It counts objects, not memory, with every row loaded, which neither pattern requires. A Domain Model only pulls in the objects a session needs. What the count shows is a difference in kind: objects with their own identity, against one module handed the rows and a key.

@chapter Making a choice
@quote text="The bad news is that nobody knows how to measure the complexity of domain logic." cite="Fowler, Patterns of Enterprise Application Architecture, Chapter 2"
So how do you choose? It depends very much on how complex the domain logic is. And then the bad news. Nobody knows how to measure the complexity of domain logic.

@art effort-curves
Fowler sketches effort against complexity for the three patterns, and disowns it in advance, as an unquantified graph. With simple logic, a Domain Model costs more than it pays back. As the logic grows, the other two hit a wall. All you can do is find experienced people, and make a judgement call.

@art judgement-scale
Some factors shift the curves. The better the team, the more he leans to a Domain Model. Table Module depends on its tools, and without them, he wouldn't bother. From scripts, don't hesitate to refactor toward a Domain Model. And the three can be mixed.

@chapter Where people slip
@list heading="Common slips" items="Table Module is a Domain Model with fewer objects@The first|Making a Choice gives a threshold@The second|Table Module without its tools@And the third"
The first slip is thinking a Table Module is a Domain Model with fewer objects. It gives up identity, direct links between instances, and polymorphism. The second is reading Making a Choice as a threshold. It's a judgement. And the third is choosing a Table Module without the Record Set tools it depends on.

@chapter Try it
@words text="patient 900 · visit 5,400 · doctor 30 · ward 12"
Your turn. A small clinic has nine hundred patients, fifty four hundred visits, thirty doctors and twelve wards. How many objects would a Domain Model hold with every row loaded? How many would a Table Module hold? And what's the largest Record Set one module would work on?

@end text="Count the objects yourself"
You can type in tables and compare the two counts, on Learn. That's learn dot get er done dot I O.
