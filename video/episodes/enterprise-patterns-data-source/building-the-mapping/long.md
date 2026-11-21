---
format: long
lesson: enterprise-patterns-data-source/building-the-mapping
title: Building the mapping: model first, but only in short cycles
thumb: Two sources, one conversion
---

@chapter Three situations
@title text="Building the Mapping" sub="Patterns of Enterprise Application Architecture, Chapters 3 and 8" art=thumb
Which comes first, the database or the objects? Fowler's answer depends on which of three situations you're in, and it comes with a firm limit.

@art three-situations
You choose the schema yourself. Or you map to an existing schema that can't change. Or you map to an existing one whose changes are negotiable. The simplest case is the first, with little to moderate domain logic, a Transaction Script or a Table Module. Then design the tables around the data in the usual way, and keep the SQL behind a gateway.

@chapter Model first
@art model-first-risk
With a Domain Model, the advice turns round. Build the model without regard to the database, to make the domain logic as simple as it can be, and treat the database as the way its data persists. Beware a model that looks like a database design. A Data Mapper gives you the most room for that.

@quote text="Although building the model first is a reasonable way of thinking about it, this advice only applies within short iterative cycles." cite="Fowler, Patterns of Enterprise Application Architecture, Chapter 3"
Then the limit. Although building the model first is a reasonable way of thinking about it, this advice only applies within short iterative cycles.

@art grow-together
A model built for months with no database, and only then persisted, is highly risky. By then, the design may be too slow in ways that take more rework than anyone can afford. So grow the database with the model, in iterations of six weeks at most, and shorter if you can.

@chapter An existing schema
@art old-schema-pieces
With a schema that already exists, the options don't change, but the order of work does. Simple logic sits on gateways shaped like the tables. Complex logic needs a Domain Model, which will almost never fit tables designed before it. So it grows a piece at a time, with Data Mappers writing it to the old schema.

@chapter Double mapping
@art two-sources
The section ends with double mapping: one kind of data with several origins. Maybe several databases hold the same data with small schema differences, left by copy and paste reuse. Fowler observes that the smaller the difference, the more it annoys. Or the data arrives sometimes from tables, and sometimes in messages.

@code block=1 lines=1-18 label=Java focus="3-5@reads three values|6-8@converts them|12-14@XML message|15-17@the same way"
Here's one customer from two sources. One mapping reads a row of a table, and the other an XML message. Each reads three values, then converts them the same way. The lab finds one repeated block, six lines in all: lines six to eight, and fifteen to seventeen.

@words text="Lines 3–5 and 12–14 differ" sub="those differences belong to each source"
Lines three to five and twelve to fourteen repeat in shape, but differ in their source calls and column names. So they aren't counted. And those differences are exactly what a per source step is for.

@chapter Two steps
@code block=2 lines=1-18 label=Java focus="2-11@each source|14-18@toCustomer"
So map in two steps. Each source fills a logical record, a CustomerData, and holds the differences. Then toCustomer, written once, turns the record into the object. The lab now finds zero repeated lines.

@art two-step
Note the numbering. This code reads data in, so it numbers the steps from the source. Fowler numbers them from the objects: his first step converts objects to a logical schema, designed to make the sources look alike. His second maps that schema to each real store.

@words text="Worth it only with many commonalities"
The count doesn't show what it cost: a CustomerData class, and a second call on every read. That's why Fowler keeps two steps for sources alike in most things, and irritatingly unlike in a few. With one source, or two that share little, a layer for each is simpler.

@chapter Where people slip
@list heading="Common slips" items="Database first, then the objects@The first|Double mapping is mapping twice@The second|Two sources always need two steps@And the third"
The first slip is designing the database first for a Domain Model. The second is thinking double mapping means mapping twice to the same database. It's one kind of data from two sources. And the third is adding the logical step whenever there are two sources.

@chapter Try it
@code block=3 lines=1-18 label=Java focus="1-9@a table|11-18@a message"
Your turn. This writes one shipment to two sinks, a table and a message. Mark the lines they repeat. Then write the logical record that would carry the converted values, and say what the shared step and each sink's step would hold.

@end text="Find the shared conversions"
You can paste two mappings into the lab and see what they share, on Learn. That's learn dot get er done dot I O.
