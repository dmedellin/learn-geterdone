---
format: long
lesson: gof-behavioral-objects/behavioral-discussion
title: The behavioral patterns, side by side
thumb: Observer or Mediator?
---

@chapter Eleven patterns, compared
@title text="Discussion of Behavioral Patterns" sub="Design Patterns, end of chapter 5" art=thumb
Chapter five has eleven patterns, and at its end the authors set them side by side. It's a short discussion in four parts, and it answers a question you've probably had: when should I use Observer, and when Mediator?

@quote text="We've found it easier to make reusable Observers and Subjects than to make reusable Mediators." cite="Gamma, Helm, Johnson and Vlissides, Design Patterns, Chapter 5"
That's the authors weighing two of their own patterns. We've found it easier to make reusable Observers and Subjects than to make reusable Mediators. Hold on to that. We'll come back to it.

@chapter Encapsulating variation
@art wrap-variation
The first theme. When some aspect of a program changes often, many behavioral patterns give it an object, and the pattern takes the object's name. A strategy wraps an algorithm. A state, behaviour that depends on a state. A mediator, the protocol between objects. An iterator, the way an aggregate is traversed.

@words text="The exception: Chain of Responsibility"
Chain of Responsibility is the exception. It works over any number of objects that may already exist, and its communication is open ended, rather than fixed between classes.

@chapter Objects as arguments
@art tokens-passed
The second theme. A visitor is always an argument, to the accept operation of what it visits, and never part of those objects. Command and Memento make tokens, passed around and used later. A command stands for a request, a memento for an object's state at one moment.

@words text="Command: polymorphic · Memento: a value"
They differ in one respect. Executing a command is polymorphic. A memento's interface is so narrow that it's passed only as a value.

@chapter Distributed or encapsulated
@art distributed-vs-central
The third part calls Mediator and Observer competitors. Observer distributes communication: no single object holds the constraint, subjects and observers maintain it together. Mediator puts the constraint in one place, the mediator.

@list heading="Two measures" items="Reuse: Observer@easier to reuse|A flow you can follow: Mediator@easier to follow"
And here's their verdict. Observer gives finer grained classes that are easier to reuse. But the flow of communication is easier to follow through a mediator, because observers are usually connected just after they're made, and the connections are hard to see later. Smalltalk tips the balance toward Observer.

@chapter Four ways to decouple
@art four-decouplers
The fourth part is decoupling senders and receivers. Command puts the binding in an object, at the cost of a subclass per connection. Observer's binding is looser, and suits data dependencies best. Mediator routes colleagues through it. And Chain of Responsibility passes a request along possible receivers.

@words text="Mediator and Chain: a home-made dispatch" sub="at a cost in type safety"
Those last two share a drawback. Their fixed interface may force a home made dispatching scheme, which weakens type safety. Every way of decoupling costs something, and the discussion states each cost beside the benefit.

@art patterns-together
The summary says the patterns mostly reinforce one another. A handler in a chain probably uses a template method. The chain may carry commands. And a visitor may act on what an iterator reaches. Well designed systems, the authors say, are full of patterns.

@chapter Count it
@art desk-devices
The lab takes one comparison from the third part, on a ticket desk with five devices: the till, the ticket printer, the scanner, the customer display and the queue screen. They must keep each other informed.

@math heading="Pairwise or through a mediator" items="pairwise: 5 · 4 ÷ 2 = 10 to build@five times four;;one changes: 5 − 1 = 4@five minus one;;mediator: 5 to build, 1 to change@through one mediator;;8 devices: 28 and 7 vs 8 and 1@add a door"
Each talking to each, that's five times four, over two, ten connections to build. When one device changes, five minus one, four. Through one mediator, five to build, and one to change. Add a door, an alarm and a phone, and it's twenty eight and seven, against eight and one.

@words text="The counts bound it, they don't settle it"
Two cautions. Observer isn't the pairwise extreme, since a subject links only to its own observers. And the one connection that changes under the mediator sits inside it, which is how it grows into a monolith. The authors' two measures aren't counted at all.

@chapter Try it
@words text="A garden controller: 7 devices" sub="sensor · valve · pump · panel · phone · timer · weather"
Your turn. A garden controller's seven devices. Count the connections to build and to change, with each talking to each, and with one mediator.

@end text="Count both designs"
Then type them into the lab and switch the scheme to check, on Learn. That's learn dot get er done dot I O.
