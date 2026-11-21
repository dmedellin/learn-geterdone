---
format: long
lesson: gof-introduction/objects-interfaces-and-implementations
title: Program to an interface, not an implementation
thumb: Know it by what it accepts
---

@chapter The principle
@title text="Objects, Interfaces and Implementations" sub="Design Patterns, Section 1.6" art=thumb
The first principle of the Gang of Four's book gets a line of its own. Program to an interface, not an implementation. Here's the argument that leads to it, and what it does to a real piece of code.

@quote text="Don't declare variables to be instances of particular concrete classes. Instead, commit only to an interface defined by an abstract class." cite="Gamma, Helm, Johnson and Vlissides, Design Patterns, Section 1.6"
And the authors explain it straight away. Don't declare variables to be instances of particular concrete classes. Instead, commit only to an interface defined by an abstract class.

@chapter Finding objects
@art requests-only
Start with what an object is. It packages data with the operations on it, and a client can only send it requests. That restriction is what keeps its state encapsulated.

@art objects-not-in-world
Deciding what the objects should be is the hard part. Many classes come from analysis of the real world. But a design that only copies today's world isn't ready for tomorrow's, and some of the most useful objects have no counterpart in it, like an algorithm made into an object, which is Strategy, or each state of something made into an object, which is State.

@words text="From a character to a subsystem" sub="Facade · Flyweight · Abstract Factory · Builder"
Objects can also be any size, as small as a character or as large as a subsystem. Facade makes a whole subsystem one object, and Flyweight supports huge numbers of tiny ones. Abstract Factory and Builder make objects whose only job is to make other objects.

@chapter Interfaces and types
@list heading="Words that matter" items="Signature: name, parameters, result@a signature|Interface: every signature@its interface|Type: a name for an interface@a type"
Every operation has a signature: its name, its parameters and its result. The set of all an object's signatures is its interface, every request it'll accept. And a type is just a name for an interface.

@art dynamic-binding
Objects are known only through their interfaces, which say nothing about how a request is carried out. Which operation runs depends on the request and on the object that gets it, decided while the program runs. That's dynamic binding. And the freedom to swap one object for another of the same type is polymorphism.

@chapter Class versus type
@words text="Class: how it's built" sub="Type: what it can be asked"
Now the key distinction. An object's class is how it's built. Its type is only what it can be asked. Class inheritance reuses code and representation. Interface inheritance says what may stand in for what.

@art subtypes
When every subclass of an abstract class keeps its interface, they're all subtypes, and a client can use any of them. Clients that deal only with that interface don't need to know which classes implement it, and the dependencies between parts of a system shrink.

@chapter A parcel locker
@code block=1 lines=2-16 focus="3-5@three implementations|9-15@chooses among them"
Here's a parcel locker's app, written to three implementations. It names a text sender, a mail sender and a push sender, and chooses among them itself.

@math heading="Concrete senders" items="4 classes · 3 uses@four classes;;3 of 6 pairs = 1/2 = 50%@three of the six;;fan-out: LockerApp 3@fan out"
The lab counts four classes and three uses. Three of the six possible pairs are connected, which is one half, fifty percent. And the largest fan out, the most classes one class uses, is the locker app, with three.

@code block=2 lines=2-15 focus="2-4@one type|9-11@the caller chooses|14@notifier"
Now write it to an interface. The app depends on one type, Notifier, and each sender implements it. The caller chooses the class and hands it in. The app just calls send on its notifier.

@math heading="One interface" items="5 classes · 4 uses@five classes;;4 of 10 pairs = 2/5 = 40%@four of ten;;fan-in: Notifier 4 · fan-out: 1@fan in"
Now there are five classes and four uses, connecting four of ten pairs, two fifths, forty percent. And the figures turn round. The largest fan in is Notifier, with four, and no class uses more than one other.

@art dependency-fan
So in the first design, one class fans out to three. In the second, three senders fan in to one type, and the client fans out to just that one.

@art fourth-sender
The real test is a fourth sender, for post. With concrete senders, the app gains a use, its fan out becomes four, and the client is edited. Through the interface, the new use runs from the post sender to Notifier, and the app is untouched.

@chapter Where people slip
@list heading="Common slips" items="Taking class and type for the same thing@The first|Expecting the world to supply every object@The second|Thinking concrete classes disappear@And the third"
The first slip is taking class and type for the same thing. Three unrelated sender classes all share the type Notifier. The second is expecting the real world to supply every object. And the third is thinking an interface removes concrete classes. They still have to be created somewhere, and the creational patterns say where.

@chapter Try it
@words text="TileView · three tile sources" sub="before and after one interface"
Your turn. A map viewer's tile view uses three tile sources and a renderer. Then the sources go behind one interface. Give the fan out of the tile view and each class's fan in, before and after, and say which class a fourth source would make you edit.

@end text="Count the dependencies"
Check your counts in the lab, on Learn. That's learn dot get er done dot I O.
