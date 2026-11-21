---
format: long
lesson: enterprise-patterns-data-source/data-mapper
title: Data Mapper: objects that don't know the database exists
thumb: Reverse one, add one
---

@chapter The mismatch
@title text="Data Mapper" sub="Patterns of Enterprise Application Architecture, Chapters 10 and 18" art=thumb
Active Record ties each object to its row. That works while the objects and the tables look alike. Fowler's Data Mapper is for when they don't.

@art mismatch
Here's the problem. Objects have collections and inheritance. Relational databases don't. So a model rich in business rules ends up with a shape of its own that doesn't match the tables. Data still has to move between the two, and if the objects know the database's structure, a change on one side tends to ripple to the other.

@chapter The layer
@art mapper-between
The mapper is a layer that does the moving, and keeps the two apart. The schema was always ignorant of the objects. Now the objects are ignorant of the schema, and of the mapper too.

@quote text="With Data Mapper the in-memory objects needn't know even that there's a database present" cite="Fowler, Patterns of Enterprise Application Architecture, Chapter 10"
As Chapter ten puts it, with Data Mapper the in memory objects needn't know even that there's a database present. No SQL interface code in them, and no knowledge of the schema.

@art third-party
Chapter eighteen's Mapper says what that costs. A mapper sits between two subsystems that don't know it, so how do you invoke it? A third subsystem drives it. That's why Gateway is far more common. It's simpler to write and to use.

@chapter How it works
@art identity-check
A client asks the mapper to find an object. The mapper checks an Identity Map for it, and loads it if it isn't there. A save reads the object's values and writes them to its rows. Knowing what changed is a Unit of Work's job, and Lazy Load stops it pulling back the whole database.

@code block=1 lines=1-17 label=Java focus="2@AccountMapper|10-11@runs the SELECT|14@one row|15@builds the account"
Here's the mapper for the Account from the last lesson, which now has a constructor and no SQL. Find runs the SELECT, moves to the one row, and builds the account from its columns. Account knows neither the table, nor AccountMapper.

@chapter What a change reaches
@math heading="jdbc changes" items="active record: direct 1, in all 3@With Active Record;;account, report, screen@the screen and the report;;mapper: direct 1, in all 2@With the mapper;;main, mapper@main and the mapper"
Let's trace a change. With Active Record, a screen and a report use account, and account uses jdbc. Change jdbc, and it can reach three classes: account, and through it, the screen and the report. With the mapper, the same change reaches just two: main and the mapper. No domain class is reached.

@math heading="account changes" items="active record: 2, report and screen@In the first design;;mapper: direct 3, in all 4@in the mapper design;;main, mapper, report, screen@main, the mapper"
Now change the domain class instead. In the first design, it reaches two: the report and the screen. In the mapper design, three depend on it directly, and four are reached in all: main, the mapper, the report and the screen.

@art dependency-arrows
So the mapper hasn't removed a dependency. It has reversed the one between the domain and the database, and added one: its own, on the domain. That's the price, counted.

@chapter When to use it
@words text="Schema and model evolve independently"
Use a Data Mapper when the schema and the object model must evolve independently, most often with a Domain Model. Its price is the extra layer, and Fowler wouldn't choose one without a Domain Model. A simple model over tables its own team controls can use Active Record.

@art tool-box
He didn't expect most readers to write this layer by hand. He tells anyone with a Domain Model to think hard about buying a tool. Since then, that's become usual practice. But choosing and tuning a tool is still a job, and these patterns are the vocabulary for its options.

@chapter Where people slip
@list heading="Common slips" items="It removes dependencies@The first|Use it everywhere@The second|The domain is wholly ignorant@And the third"
The first slip is thinking a Data Mapper removes dependencies. It reverses them. The second is using one for every application. And the third is expecting the domain to be wholly ignorant. It may need finders, so put them in a Separated Interface in the domain package.

@chapter Try it
@words text="web, invoice, customer · two mappers · main" sub="jdbc changes"
Your turn. Web uses invoice, invoice uses customer, and each has its own mapper that uses jdbc, with main wiring both mappers. Change jdbc. What depends on it directly, what does it reach in all, and is either domain class reached?

@end text="Trace the change yourself"
You can type in a design and see what a change reaches, on Learn. That's learn dot get er done dot I O.
