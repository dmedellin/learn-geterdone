---
format: long
lesson: enterprise-patterns-domain-logic/domain-model
title: Domain Model: let each object carry its own rules
thumb: Each object takes its part
---

@chapter The shift
@title text="Domain Model" sub="Patterns of Enterprise Application Architecture, Chapters 2 and 9" art=thumb
A Transaction Script puts all the logic for an action in one procedure. Fowler's second way of organising domain logic turns that inside out, and he calls himself an object bigot for preferring it.

@quote text="Rather than one routine having all the logic for a user action, each object takes a part of the logic that's relevant to it." cite="Fowler, Patterns of Enterprise Application Architecture, Chapter 2"
Here's his description of the paradigm shift. Rather than one routine having all the logic for a user action, each object takes a part of the logic that's relevant to it.

@chapter The idea
@art nouns-objects
A Domain Model is organised, roughly, around the nouns of the domain, with a class for each thing the business talks about. The validations and calculations go into those classes, beside the data they use. A procedure for an action may still exist, but it quickly hands the work to the model.

@art hunt-objects
Fowler admits the cost to a newcomer. You hunt from one object to the next to find the behaviour you want. And learning the style can take months.

@chapter Why bother
@art new-class
The payoff comes as logic grows. When a new rule arrives, a Domain Model adds a new object, such as a new strategy. A Transaction Script adds another condition to its conditional logic. Once you're used to it, there are techniques for handling ever more complex logic in an organised way.

@chapter Simple and rich
@list heading="Two styles" items="Simple: mirrors the tables · Active Record@In the simple|Rich: inheritance, strategies · Data Mapper@A rich one"
Fowler sees two styles. In the simple one, the model mirrors the database, mostly one object to a table, and can use Active Record. A rich one can look quite different, with inheritance, strategies and other patterns, and it needs a Data Mapper. The richer the model, the more complex the mapping.

@chapter The count
@code block=1 lines=1-12 label=Java focus="4-5@book|6-7@alcohol|8-9@food"
Here's one routine that prices every kind of product. A book gets five percent off. Alcohol costs twenty percent more. And food gets ten percent off, when you buy more than ten.

@math heading="price-by-kind" items="1 + if 3 + && 1 = 5@one, plus three;;nesting 1, from line 5@deepest nesting"
Count decision points the same way as before: one, plus one for each if, and, and or. That's one, plus three ifs, plus one and, which makes five. The deepest nesting is one, first reached at line five.

@code block=2 lines=1-18 label=Java focus="2-6@Product is the default|7-12@Book and Alcohol|13-18@Food"
Now give each kind of product its own rule. Product is the default, and changes nothing. Book and Alcohol override adjust. And Food keeps the one decision it really needs, about quantity.

@math heading="price-delegated" items="1 + if 1 = 2@one, plus one;;every price unchanged@every price"
Counted over the whole listing, that's one, plus one if: two. And every price the switch gave is still given. So the fall from five to two loses no behaviour.

@chapter Decisions move
@art subclasses
So where did the three tests on the kind go? The question they asked, which kind of product is this, is now answered once, when the object is made as a Book or a Food. That's Fowler's point. A new kind is a new class, not a new branch in every routine that asks.

@chapter Bloat
@art bloated-object
A common worry is bloat: an order class swollen with behaviour only one screen needs. Moving it into a use case class, Fowler answers, leads to duplication, because behaviour kept apart from the order is easy to miss. In his experience, bloat is rarer than predicted, and easy to fix.

@chapter Where people slip
@list heading="Common slips" items="A Domain Model mirrors the tables@The first|Polymorphism removes the decisions@The second|Split every use case out@And the third"
The first slip is thinking a Domain Model is classes that mirror the tables. Classes that only hold columns are data. The second is thinking polymorphism removes the decisions. It moves them. And the third is splitting every use case out of the domain objects. Put behaviour in its natural object, and deal with bloat if it appears.

@chapter Try it
@code block=3 lines=1-13 label=Java focus="3-4@post|5-8@courier|9-10@collect"
Your turn. Here's a shipping cost by method and weight: post, courier, and collect, with staff parcels free. Count its decision points with the breakdown. Then say which classes each branch would move to, keeping every price the same.

@end text="Move the decisions yourself"
You can paste a routine into the lab and watch its decision points, on Learn. That's learn dot get er done dot I O.
