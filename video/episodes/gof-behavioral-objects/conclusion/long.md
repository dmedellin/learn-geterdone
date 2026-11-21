---
format: long
lesson: gof-behavioral-objects/conclusion
title: What the Gang of Four expected patterns to do, and what they didn't claim
thumb: Targets for refactoring
---

@chapter The case against the book
@title text="What to Expect from Design Patterns" sub="Design Patterns, chapter 6" art=thumb
The last chapter of Design Patterns is short, and it's the authors' own account of what the catalog is for. It's also honest about what it isn't. Let's read it as an argument.

@words text="No new algorithm · no method · no theory"
The chapter opens by stating the case against the book. It offers no new algorithm or technique, no rigorous method, and no theory of design. Only existing designs, written down. Their reply: naming gives techniques standard definitions, and what isn't studied can't be improved.

@chapter Four things to expect
@art vocabulary
First, a common design vocabulary. Patterns name structures larger than syntax, so designers can talk above the level of code. You'll hear yourself proposing an Observer here, or a Strategy there.

@list heading="What to expect" items="A common vocabulary@vocabulary|A documentation and learning aid@learning aid|An adjunct to existing methods@adjunct|A target for refactoring@target"
So, four things. A common vocabulary. A documentation and learning aid, since much of what makes a large system hard to follow is patterns the reader doesn't recognise. An adjunct to existing methods, recording why a design is as it is. And a target for refactoring.

@quote text="Design patterns thus provide targets for your refactorings." cite="Gamma, Helm, Johnson and Vlissides, Design Patterns, Chapter 6"
That last one closes its section. Design patterns thus provide targets for your refactorings.

@chapter The life cycle
@art life-cycle
It rests on a life cycle Brian Foote described. In prototyping, software is built fast, its classes mirror the problem, and reuse is by inheritance. In expansion, new requirements pile on classes until the software grows stiff. In consolidation, it's refactored: classes split, interfaces are rationalized, frameworks emerge.

@art white-to-black
And in consolidation, composition replaces inheritance: black box reuse in place of white box. Expansion and consolidation repeat. Used early, patterns spare later refactorings. Found late, they show what to refactor toward.

@chapter History and Alexander
@art history-grow
The history is a nice story. The catalog began in Erich Gamma's thesis. Wrapper became Decorator, Glue became Facade, Solitaire became Singleton, and Walker became Visitor. Their main lesson: spotting a pattern is easy, describing one so newcomers see why it matters is hard. Patterns grew from under two pages each to over ten.

@art alexander
Then they set the book beside Christopher Alexander's work on buildings. Alexander orders his patterns, they don't. His stress the problem, theirs the solution. And he claims his generate whole buildings, while they claim no such thing for programs. Their catalog, they say, is a collection of related patterns, not a pattern language.

@chapter Count it
@art change-ripple
The lab tries the life cycle at small scale: a bakery's till, after its expansion. Each kind of discount was added as a subclass of the order, and the till, the receipt and the daily report all test the order's class.

@math heading="Modules each request touches, before" items="senior discount: 4@a senior discount;;staff cap: 2@the staff discount;;loyalty stamps: 2@loyalty stamps;;receipt logo: 1@a new logo;;4 + 2 + 2 + 1 = 9 · confined: 1@nine"
Four change requests. A senior discount touches four modules. A cap on the staff discount, two. Loyalty stamps on discounted orders, two. A new logo on the receipt, one. That's nine module touches, with one change confined to a single module.

@code block=1 lines=1-16 label=Java focus="2-4@a discount interface|11-15@the order"
Now consolidate, with the discounts as a Strategy. There's a discount interface, and each discount is a class. The order is given a discount, by composition, instead of being one.

@math heading="After the consolidation" items="2 + 1 + 2 + 1 = 6@six;;confined: 2@two changes confined"
The same four requests now touch two, one, two and one modules. That's six, with two changes confined. The logo was never about discounts, and stays at one.

@words text="For these four requests only"
But those are the figures for these four requests. The book's point is that the pattern gave the refactoring a target. Whether this one was worth it depends on which requests come next.

@chapter An invitation
@list heading="The invitation" items="Use patterns@use patterns|Be a critical consumer@critical consumer|Write down your own@write down"
The book ends with an invitation. Use patterns, and build your vocabulary. Be a critical consumer: a pattern states its trade offs, so you can argue with it. And write down the patterns you use, with someone to help you improve them.

@chapter Try it
@words text="A garden controller's modes" sub="frost · holiday · alarm, before and after State"
Your turn. A garden irrigation controller, before and after its modes become State classes in a module of their own. Give the modules each change touches in each design, the total, and the changes confined to one module.

@end text="Look for the patterns"
Then check both designs in the lab, on Learn. That's learn dot get er done dot I O.
