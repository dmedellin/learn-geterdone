---
format: long
lesson: gof-introduction/inheritance-versus-composition
title: Favor composition over inheritance: what the Gang of Four meant
thumb: Favor, not replace
---

@chapter Two ways to reuse
@title text="Inheritance Versus Composition" sub="Design Patterns, Section 1.6" art=thumb
You've written a class that does something useful, and now you want to reuse it. There are two ways, and the Gang of Four's second principle says which to prefer, and why.

@art white-box-black-box
You can inherit from it, defining the new class in terms of the old one's implementation. The authors call that white box reuse, because the parent's insides are often visible to the child. Or you can hold an object of it and send it requests. That's black box reuse: you only see its interface.

@quote text="Favor object composition over class inheritance." cite="Gamma, Helm, Johnson and Vlissides, Design Patterns, Section 1.6"
The principle is short. Favor object composition over class inheritance.

@quote text="designers overuse inheritance as a reuse technique, and designs are often made more reusable (and simpler) by depending more on object composition." cite="Design Patterns, Section 1.6"
And the reason is their experience. Designers overuse inheritance as a reuse technique, and designs are often made more reusable, and simpler, by depending more on object composition.

@chapter Weighing them
@list heading="Inheritance" items="Supported directly, easy to use@supports it directly|Can't change at run time@can't be swapped|Breaks encapsulation@the worse of the two"
Inheritance has real advantages. The language supports it directly, it's easy to use, and overriding a few operations can change what the inherited ones do. But what a class inherits can't be swapped while the program runs. And the worse of the two: a parent often fixes part of its children's representation, so when the parent changes, the child must too.

@art composition-swap
Composition is set up while the program runs, by objects getting references to other objects. It needs carefully designed interfaces, but no encapsulation is broken, any object can be replaced by another of the same type, and classes stay small.

@words text="Cost: more objects" sub="behaviour lives in the connections"
Its cost, stated in the same paragraph, is more objects, if fewer classes, and behaviour that lives in how the objects are connected, not in one place you can read. And in the end the two work together. The components on hand are never quite enough, and inheritance makes new ones easy to write.

@chapter Delegation
@art window-delegates
Delegation is the strong form of composition. An object forwards a request to a delegate, and passes itself along, so the delegate can refer back. The book's example is a window that holds a rectangle and forwards its area to it, so it can become a circle while the program runs, just by swapping that object.

@words text="Only when it removes more than it adds" sub="State · Strategy · Visitor"
The price is that software this dynamic is harder to understand. So delegation is a good choice only when it removes more complexity than it adds, and it works best in the stylized forms patterns give it, as in State, Strategy and Visitor.

@chapter Two structures
@art compile-vs-run
Section one point six ends on a contrast. The code is frozen when it's compiled, classes in fixed relationships. The running program is a changing network of objects. Owning another object and merely knowing it usually look the same in the code, a reference, so the code won't show everything about how a system runs.

@chapter A music player
@code block=1 lines=2-17 focus="3-4@a track source|11-13@changed while|16@delegated"
Here's the lesson's music player. It's composed of a track source and a play order, each behind an interface. The order can be changed while the player runs, and asking for the next track is delegated, not inherited.

@art player-parts
It varies in two ways: where tracks come from, a local library, a stream, a radio station or a podcast feed, and the order they play in, in order, shuffled or repeated.

@math heading="Two aspects: 4 sources, 3 orders" items="subclasses: 4 × 3 = 12 combinations → 13 classes@four times three;;composition: (4 + 1) + (3 + 1) = 9@four plus one;;13/9 ≈ 1.4×@thirteen ninths;;new order: 4 subclasses vs 1 class@a new order"
One subclass per combination is four times three, twelve combinations, and thirteen classes with the abstract player. One hierarchy per aspect is four plus one, plus three plus one: nine. That's thirteen ninths, about one point four times. And a new order adds four subclasses, against one class.

@math heading="Add an output: speaker or headphones" items="24 combinations → 25 classes@twenty four;;composition: 12@twelve;;25/12 ≈ 2.1× · new order: 8 vs 1@two point one"
Add a third aspect, the output. Combinations double to twenty four, and subclassing needs twenty five classes, while composition needs twelve. The ratio grows to about two point one, and a new order adds eight subclasses against one. That's an explosion of classes.

@art class-explosion
But the count is one consequence. It doesn't show the cost the authors put beside it: the composed player's behaviour is spread over three objects.

@chapter Where people slip
@list heading="Common slips" items="Reading it as never inherit@The first|Thinking the case is the class count@The second|Expecting code to show owning and knowing@And the third"
The first slip is reading the principle as never inherit. It says favor, not replace. The second is thinking the case against inheritance is the class count. The real reasons are that inheritance can't change at run time, and binds a child to its parent. And the third is expecting the code to show owning versus knowing.

@chapter Try it
@words text="trigger · zone · valve" sub="3 triggers · 3 zones · 2 valves"
Your turn. A garden irrigation controller varies in its trigger, timer, moisture or weather, its zone, lawn, beds or pots, and its valve, solenoid or drip. Count the combinations, the classes each way, and what a new trigger adds under each.

@end text="Count the classes"
Then type the aspects into the lab and check, on Learn. That's learn dot get er done dot I O.
