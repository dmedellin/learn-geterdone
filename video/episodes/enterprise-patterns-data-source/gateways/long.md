---
format: long
lesson: enterprise-patterns-data-source/gateways
title: Gateways: put all the SQL for a table in one class
thumb: Rename it in one place
---

@chapter Where the SQL goes
@title text="Gateways" sub="Patterns of Enterprise Application Architecture, Chapters 3, 10 and 18" art=thumb
Your domain logic is built. Now it has to talk to the database. Fowler's first move in Chapter three is simple: get the SQL out of the domain logic, and put it somewhere you can find it.

@art sql-everywhere
His case begins with SQL itself. It's everywhere in enterprise software, and still a trap. Many application developers don't know it well. Every way of embedding it in a language is somewhat awkward. And database administrators want to find the SQL that touches a table, so they can tune it.

@art one-gateway
So separate the SQL from the domain logic, and put it in classes of its own, one for each table. Each is a Gateway to its table. Fowler does this even in his own small scripts, because he finds the separation that helpful.

@quote text="The rest of the application needs to know nothing about SQL, and all the SQL that accesses the database is easy to find." cite="Fowler, Patterns of Enterprise Application Architecture, Chapter 3"
And here's the promise. The rest of the application needs to know nothing about SQL, and all the SQL that accesses the database is easy to find.

@chapter The choice ahead
@art four-choices
Then he lays out the choice this course reads. A gateway can have one instance per row, a Row Data Gateway, or one per table, a Table Data Gateway. A simple Domain Model can let each object load and save itself, an Active Record. And a rich one wants a Data Mapper. The choice is far reaching, and shaped by your domain logic.

@art cost-third
Weighing object databases, which need no mapping, Fowler puts the cost of mapping at about a third of all programming effort. But he says it rests on anecdote, and he knows of no controlled test. So treat it as an estimate.

@chapter The Gateway
@art wrapped-resource
Gateway, in Chapter eighteen, is the general tool. Wrap the special API of an external resource, like JDBC and SQL, in a class whose interface looks like any other object's. Keep it minimal. It adapts the resource, and gives tests a place to substitute a stand in.

@code block=1 lines=1-16 label=Java focus="2@price table|9@findCents|10-11@question mark|12-14@fills the placeholder"
Here's a small Table Data Gateway for a price table. prepareStatement compiles the SQL, with a question mark as a placeholder. setString fills the placeholder, and executeQuery runs it. A caller asks for findCents and never sees a column name.

@words text="Map? DTO? Record Set?" sub="what should a query return"
The trickiest question is what a query returns. A map works, but Fowler calls it bad form, because a mistyped key is found only when it fails. A Data Transfer Object is better, at the cost of another class. A Record Set is very effective where tools are built around it.

@chapter Counting the edits
@math heading="Rename a column of price-table" items="sql-everywhere: direct 4@four classes;;admin, cart, checkout, report@cart, checkout;;one-gateway: direct 1, pricegateway@one gateway;;reached in all: 5, an upper bound@upper bound"
The lab counts what a column rename touches. When four classes, cart, checkout, report and admin, each hold their own SQL, the rename is edited in all four. With one gateway, only the gateway touches the table, so the rename is edited in one class. The lab says five are reached in all, but that's an upper bound.

@art test-standin
Those five are reached only if the change gets past the gateway's interface, if findCents itself has to change. A rename the gateway absorbs stops at the gateway. Whether a given change is absorbed is a question the count leaves to you.

@chapter Where people slip
@list heading="Common slips" items="A gateway is one more class to change@The first|A gateway hides the database@The second|Choosing the data source first@And the third"
The first slip is thinking a gateway is one more class, so a change costs more. It's the class that saves the other edits. The second is expecting a gateway to hide that there's a database. That's Data Mapper's promise. And the third is choosing the data source pattern before the domain pattern.

@chapter Try it
@words text="signup, profile, mailer → member-table" sub="then redraw with a membergateway"
Your turn. Signup, profile and mailer each use the member table, and profile also uses mailer. List the classes a column rename must be edited in. Then redraw it with a member gateway, and list them again. Mind profile, which reaches the table two ways.

@end text="Trace a rename yourself"
You can type in a design and watch what a rename reaches, on Learn. That's learn dot get er done dot I O.
