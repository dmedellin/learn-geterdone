---
format: long
lesson: gof-creational/factory-method
title: Factory Method: know when to create, not which class
thumb: Let the subclass decide
---

@chapter The framework's problem
@title text="Factory Method" sub="Design Patterns, Chapter 3" art=thumb
Factory Method, also called Virtual Constructor, is the chapter's only class creational pattern. It works by inheritance, where the other four hand creation to an object.

@quote text="Define an interface for creating an object, but let subclasses decide which class to instantiate." cite="Gamma, Helm, Johnson and Vlissides, Design Patterns, Chapter 3"
Its intent begins: define an interface for creating an object, but let subclasses decide which class to instantiate.

@art app-document
The book's example is a framework for applications that manage documents. Application and Document are both abstract, and a drawing program subclasses both. The framework knows when a new document is needed, when the user chooses open or new, but not which class to make. And it can't instantiate an abstract class.

@words text="createDocument()" sub="declared by the framework · overridden by each application"
So Application declares an abstract operation that creates a document, and each application overrides it to return its own document class. That operation is the factory method. It carries one piece of knowledge, which class, out of the framework and into the subclass.

@chapter The roles
@list heading="Participants" items="Product@the product|ConcreteProduct@the concrete products|Creator: declares and calls it@the creator|ConcreteCreator: overrides it@the concrete creators"
The participants are the product interface, the concrete products, the creator, which declares the factory method and calls it, and the concrete creators, which override it. The one collaboration: the creator relies on its subclasses for the right product.

@code block=1 lines=2-19 focus="3@the factory method|7-11@runs a cycle|15-18@lawn zone"
Here's the lesson's irrigation controller. The abstract zone declares the factory method, create schedule. It knows when a zone needs a schedule: when it runs a cycle. It doesn't know which one. The lawn zone overrides it to make a lawn schedule, and supplies its own sprinklers.

@art creator-subclasses
So each concrete product usually comes with a creator subclass that returns it. The creators run parallel to the products.

@chapter Consequences
@words text="Keeps specific classes out of general code" sub="cost: a Creator subclass just to make a product"
The central consequence is that application specific classes stay out of the code that uses them. The potential disadvantage is that a client may have to subclass the creator just to make a particular product. That's harmless when it was subclassing anyway, and otherwise one more thing that can change.

@art parallel-hierarchies
Two more consequences. A factory method is a hook for subclasses, and it can have a sensible default. And factory methods connect parallel hierarchies. In the book, each figure that can be dragged makes its own matching manipulator, so the factory method records which classes belong together.

@list heading="Implementation" items="Abstract or with a default@two main varieties|A parameterized factory method@a parameterized|Not from the constructor@constructor|A naming convention@naming convention"
Implementation names a few issues. There are two main varieties, an abstract creator, or a concrete one with a default. A parameterized factory method takes an identifier and makes one of several products. In C plus plus, don't call it from the creator's constructor, before the override is in place. And a naming convention shows a reader where factory methods are.

@code block=2 lines=2-16 focus="3@a supplier|11@one plain zone calls it|16@needs no class of its own"
In Java eight you can pass the product's constructor as a value, a supplier. One plain zone calls it, and a zone of pots on drip lines needs no class of its own. That's composition rather than subclassing, and it brings the design close to Prototype and Abstract Factory.

@art supplier-passed
One class, handed the constructor it should call, instead of a subclass for every product.

@chapter Count it
@art zones-garden
The lab's controller has three zones: lawn, bed and greenhouse, each making its own schedule class. In the lab's terms that's three families, and one kind of product.

@math heading="3 zones, 1 kind" items="3 × 1 = 3 products@three times one;;1 + 3 + 1 + 3 = 8 classes@eight;;4 create@four"
Three times one is three concrete products. One abstract creator, three concrete creators, one abstract product and three schedules: eight classes, of which four create.

@math heading="Two kinds of change" items="pot zone: +2, 8 → 10, edits 0@a fourth zone type;;sensor kind: +4, 8 → 12, edits 4@a moisture sensor"
A fourth zone type, pots on drip lines, adds two classes, eight to ten, and edits none. A second kind of product, a moisture sensor per zone, means a second factory method that every zone overrides. That adds four classes, eight to twelve, and edits four.

@art same-shape
Those are exactly the Abstract Factory lesson's counts, because here the two patterns have the same shape: an abstract factory is often a set of factory methods. What differs is where the choice is made, in a subclass of the class that uses the products, or in a separate object handed to it.

@chapter Where people slip
@list heading="Common slips" items="Thinking it needs no extra classes@The first|A factory method behind every constructor@The second|Calling it from the constructor@And the third"
The first slip is thinking Factory Method needs no extra classes. Each product usually needs a creator subclass. The second is putting a factory method behind every constructor call, even where the class never changes. And the third is calling it from the creator's constructor.

@chapter Try it
@words text="A vending machine" sub="slots: can, bottle, snack, hot-drink"
Your turn. A vending machine framework has an abstract slot whose factory method creates its dispenser. Four slot types each make their own. Count the products, the classes, the classes that create, and what a fifth slot type adds and edits.

@end text="Count creators and products"
Then check it in the lab, on Learn. That's learn dot get er done dot I O.
