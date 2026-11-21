---
format: long
lesson: enterprise-patterns-layers-and-performance/layer-supertype-and-separated-interface
title: Separated Interface: how to reverse a dependency
thumb: Interface here, code there
---

@chapter Two base patterns
@title text="Layer Supertype and Separated Interface" sub="Patterns of Enterprise Application Architecture, Chapter 18" art=thumb
The layering rule says the domain must not depend on the layers that would get in its way. But what if a domain object needs to call its mapper? Two small base patterns from Chapter eighteen make the rule workable.

@chapter Layer Supertype
@art supertype-tree
The first is Layer Supertype, and Fowler calls it a small idea, so a short pattern. When every object in a layer needs the same methods, put them in a superclass for that layer. His example is a domain object superclass that holds the storage and handling of every object's ID.

@words text="Only what they all share"
A mapper superclass can do the same for every mapper. A layer with more than one kind of object may want more than one supertype. When to use it? When the objects in a layer have common features. Fowler says he often does it without thinking.

@chapter The problem
@art package-boxes
Separated Interface starts with packages. You reduce coupling by grouping classes into packages and controlling which may depend on which. But sometimes a class has to call something the rules put out of its reach.

@quote text="use Separated Interface to define an interface in one package but implement it in another." cite="Fowler, Patterns of Enterprise Application Architecture, Chapter 18"
Fowler's advice: use Separated Interface to define an interface in one package, but implement it in another.

@art reversed-arrow
It works because an implementation depends on its interface, and not the other way round. The caller sees only the interface. And the implementation's package now depends on the caller's. The arrow has turned around.

@chapter The code
@code block=1 lines=1-19 label=Java focus="2-4@OrderFinder|7-11@Order holds|14-19@OrderMapper"
Here's the lesson's version. OrderFinder is the interface, in the domain package. Order holds only an OrderFinder, and loads through it. And OrderMapper lives in the mapper package, knows the SQL, and implements the interface. So the dependency runs from the mapper to the domain.

@art wiring-box
Something still has to call set finder with a real mapper when the application starts. Fowler's simpler choice is a package that knows both and wires them together. The alternative is a factory, bound by Plugin.

@chapter Where it goes
@list heading="Where the interface lives" items="In the client's package@one client|In a third package@several clients"
Where does the interface go? If there's one client package, put it there, so the client's developers define what they need. If there are several clients, or the implementers own the definition, put it in a third package.

@chapter What a change reaches
@art ripple-reach
The lesson's lab counts what a change to the database library reaches, following dependents of dependents.

@math heading="jdbc changes" items="mapper in domain: direct 1, in all 3@calls its mapper directly;;mapper, order, screen@order and screen;;separated: direct 1, in all 2@With the interface;;main, mapper@just main"
When the domain calls its mapper directly, one class depends on jdbc, but the change reaches three in all: the mapper, order and screen. With the interface in place, it's still one directly, but only two in all, just main and the mapper. No domain class is reached.

@words text="It reverses one dependency" sub="it doesn't remove them all"
That doesn't prove the second design is better. It says what the dependencies let a database change touch. And note what the pattern doesn't do. The mapper still depends on order, so a change to order still reaches it.

@chapter When to use it
@art plug-socket
When should you use it? Fowler gives three occasions. A framework that has to call application code. A layer that must reach one it shouldn't see, like a domain object that needs its Data Mapper. And code that has to call another team's work without depending on its API.

@words text="Not one for every class"
He also says when not to bother. Some developers write a separate interface for every class, which he thinks is excessive. For applications, he recommends one only to break a dependency, or to allow several independent implementations. And separating them later is a simple refactoring.

@chapter Where people slip
@list heading="Common slips" items="Only worth it with two implementations@The first|A supertype that does everything@The second|It removes every dependency@And the third"
Three slips. The first is thinking an interface is only worth it with two implementations. One is enough, if it breaks a dependency. The second is a supertype that does everything, when it should hold only what every object shares. And the third is thinking the pattern removes every dependency. It reverses one.

@chapter Try it
@words text="report → invoice → pdfwriter → fontlib" sub="fontlib changes"
Your turn. Report depends on invoice, invoice on pdfwriter, and pdfwriter on fontlib, and fontlib changes. List what it reaches. Then add a Separated Interface that keeps invoice out of reach, add the class that wires the two, and list again.

@end text="Trace a change yourself"
You can type in dependencies and watch a change spread, on Learn. That's learn dot get er done dot I O.
