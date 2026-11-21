---
format: long
lesson: gof-behavioral-objects/template-method
title: Template Method: the parent writes the order, the subclass fills the gaps
thumb: Don't call us
---

@chapter A skeleton
@title text="Template Method" sub="Design Patterns, chapter 5" art=thumb
This is one of the shortest patterns in the book, and one of the most used. Almost every abstract class you've written has one hiding in it. Let's see what it fixes, and what it leaves for subclasses.

@quote text="Define the skeleton of an algorithm in an operation, deferring some steps to subclasses." cite="Gamma, Helm, Johnson and Vlissides, Design Patterns, Chapter 5"
That's the first sentence of the intent. Define the skeleton of an algorithm in an operation, deferring some steps to subclasses. Subclasses may redefine some steps, but the algorithm's structure stays as the parent wrote it.

@art open-document
The book's example is an application framework that opens a document in a fixed series of steps: check it can be opened, create the right kind of document, add it to the open documents, and read it in. A drawing program or a spreadsheet supplies the check, the creation and the reading.

@words text="Class scope: done with inheritance"
Of the patterns in this course, it's the one with class scope, done with inheritance rather than objects. The abstract class implements the template method, and each concrete class writes the steps that vary.

@chapter Primitives and hooks
@code block=1 lines=1-17 label=Java focus="2@final|10-11@abstract|12-13@do nothing|14-16@private"
Here's the lesson's map tile, in Java. Render is final, so no subclass can reorder the steps. Decode and style are abstract: the primitives, which every subclass must write. Label and shade do nothing unless overridden: the hooks. And the fixed steps are private.

@art skeleton
So there are three kinds of step. Fixed steps the parent writes. Primitive operations every subclass must supply. And hooks, with a default, often empty, that a subclass overrides only if it cares. The book asks a template method to make clear which is which.

@chapter Don't call us
@quote text="Don't call us, we'll call you" cite="Design Patterns, Chapter 5, crediting Richard Sweet"
The book says template methods invert control, by what's called the Hollywood principle. Don't call us, we'll call you. The parent calls the subclass, never the other way round.

@art hook-vs-super
Hooks also cure a common slip. A subclass that extends an operation by overriding it and calling the parent's version can forget the call. If the parent calls an empty hook instead, the subclass overrides the hook, and can't forget anything.

@list heading="Implementation" items="Control access@access|Keep primitives few@few|Name them so they stand out@stand out"
Three implementation issues. Control access, so primitives are protected and the template method can't be overridden. Keep the primitives few, since each is one more method every subclass writer must supply. And name them so they stand out. MacApp prefixed its with Do.

@chapter Count it
@art three-subclasses
In the lab, the tile has seven steps: three fixed, two primitives, two hooks. Road tiles write decode, style and the label hook. Satellite tiles write decode and style. Terrain tiles write decode, and the shading hook.

@art missing-primitive
Spot the problem? Terrain tiles lack style. That subclass is left abstract, so the Java won't compile until that primitive is written.

@math heading="Step bodies" items="whole: 7 × 3 = 21@seven steps;;base: 3 fixed + 2 hook defaults = 5@the base;;overrides: 3 + 2 + 2 = 7@the overrides;;with the template: 5 + 7 = 12@twelve"
Now count the step bodies. Written whole in each subclass, it's seven steps, three times: twenty one. With the template, the base writes five, its fixed steps and its two hook defaults. The overrides are three, two and two, seven. So five plus seven, twelve.

@words text="Fix terrain: 13 vs 21"
Give terrain tiles their style, and no subclass is abstract. The count rises to thirteen, against twenty one. The gap is the duplication the template removes. It isn't a measure of whether the steps were cut in the right places.

@chapter Where people slip
@list heading="Common slips" items="Overriding and calling the parent@The first|Not saying what may be overridden@The second|Making every step a primitive@And the third"
The first slip is extending an operation by overriding it and calling the parent. The second is leaving unclear which operations may be overridden. And the third is making every step a primitive for flexibility. Each one is a method every subclass must write.

@chapter Try it
@words text="A coffee bar's order" sub="take · brew · milk · serve"
Your turn. Take and serve are fixed, brew is a primitive, milk is a hook. Espresso writes brew, latte writes brew and milk, and cortado writes milk. Which subclass is left abstract? And how many step bodies, with and without the template?

@end text="Count what each subclass writes"
Then enter it into the lab and check, on Learn. That's learn dot get er done dot I O.
