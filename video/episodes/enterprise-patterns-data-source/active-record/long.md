---
format: long
lesson: enterprise-patterns-data-source/active-record
title: Active Record vs Row Data Gateway: the one difference
thumb: One rule makes the difference
---

@chapter Same shape
@title text="Active Record" sub="Patterns of Enterprise Application Architecture, Chapter 10" art=thumb
Two patterns in Chapter ten look almost identical. Both are an object for one row that holds its own SQL. Fowler admits they're often hard to tell apart, and then gives you a one line test.

@art row-plus-rule
Active Record puts data access in the domain object, so each object knows how to read and write its own data. Its fields mirror the table's columns. And the pattern's own list of what such a class does runs through building itself from a row, finders, inserts, updates and accessors, to one last item: some of the business logic.

@quote text="A Row Data Gateway should contain only database access logic and no domain logic." cite="Fowler, Patterns of Enterprise Application Architecture, Chapter 10"
That last item is the difference. A Row Data Gateway should contain only database access logic, and no domain logic. Fowler calls the line blurred, and still worth drawing.

@chapter Two classes
@code block=1 lines=1-19 label=Java focus="3-5@three fields|7-10@find|12-14@update|16-18@canWithdraw"
Here's an Account over one account row, with three fields. Find and update run SQL, shown as comments, with the bodies left out, because the lesson is about which routines are which. And canWithdraw decides whether the balance plus the overdraft covers a sum.

@code block=2 lines=1-15 label=Java focus="7-10@same two|12-14@nothing else"
And here's AccountRow. The same row, the same three fields, the same two database routines, and nothing else. So which is which?

@math heading="The lab's count" items="Account: 3 fields, 0 public · 3 routines, 1 public@On active record;;AccountRow: 3 fields, 0 public · 2 routines, 0 public@on row gateway"
The lab counts them. On active record, three fields, none public, three routines, one public. On row gateway, three fields, none public, two routines, none public.

@art row-only
But the count can't tell database access from domain logic. That sorting is yours. Find and update run SQL in both classes. The one routine the second lacks, canWithdraw, is a rule of the business. That's what makes the first an Active Record.

@chapter From one to the other
@art gateway-grows
Chapter three gives the relation as a route. Start with a Row Data Gateway, and add domain logic to it, particularly when you see the same code repeated in several Transaction Scripts. Move logic in gradually, and the gateway turns into an Active Record. That's often good, because it reduces duplication.

@chapter When it fits
@words text="Logic close to one record"
Fowler recommends Active Record for logic that stays close to one record: the ordinary create, read, update and delete work, and rules computed from a single row. Its appeal is that it's simple. Chapter eight puts a size on simple: a couple of dozen classes, close to the database.

@words text="Isomorphic schema" sub="one class a table, one field a column"
It works well only on an isomorphic schema, one with the same shape as the classes: one class for each table, and one field for each column.

@art parting-ways
It stops working once the classes and the tables part ways. Collections, inheritance and links between objects don't fit it, and that's when you need a Data Mapper.

@art tied-designs
And because it ties the class design to the table design, neither can be refactored without the other.

@chapter Testing
@art tests-in-memory
Where's the database coupling? canWithdraw reads two fields and touches no connection, so you can test it on an Account built in memory. The coupling is in find and update. Static finders are more common with this pattern, because of its closeness to the database. But Fowler says moving the finders into a class of their own is better for testing.

@chapter Where people slip
@list heading="Common slips" items="Two names for one pattern@The first|Can't be tested without a database@The second|It's outside the Domain Model@And the third"
The first slip is thinking they're two names for one pattern. Domain logic is the difference. The second is thinking an Active Record can't be tested without a database. Its rules can. And the third is placing it outside the Domain Model. At heart, it's a Domain Model shaped like its tables.

@chapter Try it
@code block=3 lines=1-18 label=Java focus="6-9@find|11-13@insert|15-17@level"
Your turn. Here's a Member, with find, insert and level. List its routines, sort them into database access and domain logic, and say which of the two patterns it is. Then paste it into the lab to check the count.

@end text="Sort the routines yourself"
You can paste a class into the lab and count its routines, on Learn. That's learn dot get er done dot I O.
