---
format: long
lesson: gof-creational/abstract-factory
title: Abstract Factory: one object makes the whole family
thumb: New families easy, new kinds hard
---

@chapter Creational patterns
@title text="Abstract Factory" sub="Design Patterns, Chapter 3" art=thumb
Chapter three opens the catalog with five creational patterns. Here's what they share, the maze the authors build five ways, and the first of them, Abstract Factory.

@quote text="Creational design patterns abstract the instantiation process." cite="Gamma, Helm, Johnson and Vlissides, Design Patterns, Chapter 3"
The chapter's first sentence: creational design patterns abstract the instantiation process.

@art composed-behaviour
As a system relies more on composing objects than on inheriting, its behaviour is assembled from a few basic pieces, and making the right object takes more than one constructor call. All five patterns keep the knowledge of which concrete classes are used in one place, and hide how instances are made, so the rest of the program sees only abstract interfaces.

@chapter The maze
@art maze-rooms
The running example is a maze for a computer game: rooms whose sides are walls or doors. Its first version is one routine that makes every room, wall and door by naming its class. The complaint isn't its length but its rigidity. A game with enchanted rooms can't reuse the layout without rewriting the routine.

@list heading="One way out per pattern" items="Overridable creation operations@overridable|An object that makes the parts@makes the parts|An object that builds the whole maze@builds a whole maze|Sample parts to copy@sample parts|One maze everyone can reach@one maze"
The introduction sketches one way out per pattern: overridable creation operations, an object passed in that makes the parts, an object that builds a whole maze step by step, sample parts to copy, and Singleton, to keep the game to one maze everything can reach.

@chapter The pattern
@art factory-family
Abstract Factory, also known as Kit, gives a client one interface through which it creates each member of a family of related objects, without naming their classes. The book's example is a toolkit with more than one look and feel. Each standard has a concrete factory, and because one factory makes the whole set, widgets of two standards can't end up side by side.

@list heading="Participants" items="AbstractFactory@the abstract factory|ConcreteFactory, one per family@a concrete factory|AbstractProduct, one per kind@an abstract product|ConcreteProduct@the concrete products|Client@and the client"
The participants are the abstract factory, with an operation per kind of product. A concrete factory per family. An abstract product per kind. The concrete products, one per family and kind. And the client, which uses only the abstract classes.

@code block=1 lines=2-20 focus="2-6@an operation per kind|7-11@night style|13@holds one style|16-19@asks the style"
Here's the lesson's map viewer. The map style declares an operation per kind: tile, marker and label. The night style makes the night versions. A map view holds one style, and to show a place it asks the style for each part, and never learns which classes it got.

@chapter Consequences
@list heading="Four consequences" items="Isolates concrete classes@isolates|Exchanging families is easy@exchanging|Promotes consistency@consistency|New kinds of product are hard@new kinds"
The authors list three benefits and a liability. It isolates concrete classes. It makes exchanging families easy, since the factory's class is named in one place. It promotes consistency, one family at a time. And supporting new kinds of product is hard, because the abstract factory's interface fixes the set of kinds.

@words text="Singleton · Factory Method · Prototype" sub="how a factory is usually built"
Three implementation notes lean on the other patterns. A factory is often a Singleton. Each product is usually made by a factory method, which costs a class per family. Or the factory can be given prototypes to clone, and a new family needs no new class.

@art one-make-operation
A factory can also replace its many operations with one make operation that takes the kind as a parameter. That's more flexible and less safe. Every product comes back under one shared interface, and a client that needs a kind's own operations must cast down, which can fail.

@chapter Count it
@art map-styles
Now the lab, on a map tile viewer. It draws three kinds of part, a tile, a marker and a label, in four styles: street, satellite, night and terrain.

@math heading="4 styles × 3 kinds" items="4 × 3 = 12 concrete products@four times three;;1 + 4 + 3 + 12 = 20 classes@twenty;;5 create anything@five of them"
Four times three is twelve concrete products. One abstract factory, four concrete factories, three abstract products and twelve products make twenty classes, and five of them create anything.

@math heading="Two kinds of growth" items="new style: +4 classes, 20 → 24, edits 0@public transport;;new kind: +5 classes, 20 → 25, edits 5@a route line"
A fifth style, for public transport, adds four classes, twenty to twenty four, and edits none. A fourth kind of part, a route line, adds five, twenty to twenty five, and edits five: the abstract factory and all four concrete factories.

@art growth-edits
The two growths cost about the same in new classes. Only one of them reaches back into code already written. And no count tells you which growth your design will meet.

@chapter Where people slip
@list heading="Common slips" items="Expecting new kinds to be easy@The first|A factory class for every small variation@The second|Reaching past the factory@And the third"
The first slip is expecting new kinds of product to be easy. The second is writing a concrete factory class for every small variation, when prototypes would do. And the third is letting a client construct a product directly, which can pair one style's marker with another style's tile.

@chapter Try it
@words text="A quiz app" sub="families: kids, adult · kinds: question, hint, score-card, timer"
Your turn. A quiz app has two families of look, kids and adult, and four kinds of part: question, hint, score card and timer. Count the products and the classes, then what a new family adds and edits, and what a new kind adds and edits.

@end text="Count families and kinds"
Then check it in the lab, on Learn. That's learn dot get er done dot I O.
