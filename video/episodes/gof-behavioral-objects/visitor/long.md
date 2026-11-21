---
format: long
lesson: gof-behavioral-objects/visitor
title: Visitor: new operations are cheap, new classes are dear
thumb: Which will change more?
---

@chapter Too many operations
@title text="Visitor" sub="Design Patterns, chapter 5" art=thumb
Visitor is the last pattern in the catalog, and it has a reputation for being confusing. It isn't, once you see the one question it turns on: which will change more often, your operations or your classes?

@quote text="Visitor lets you define a new operation without changing the classes of the elements on which it operates." cite="Gamma, Helm, Johnson and Vlissides, Design Patterns, Chapter 5"
That's the second sentence of the intent. Visitor lets you define a new operation without changing the classes of the elements on which it operates. The first says what a visitor is: an operation, made into an object of its own.

@art compiler-tree
The book's example is a compiler holding programs as syntax trees. It needs type checking, code generation, optimization, pretty printing, each treating assignments, variables and expressions differently. Put every operation in every node class, and they become a hard to follow mixture, all recompiled for one new operation.

@art two-hierarchies
So each operation goes into a visitor, which is passed to the nodes. Now there are two hierarchies, the elements and the visitors, and a new operation is a new visitor subclass.

@chapter Double dispatch
@code block=1 lines=1-20 label=Java focus="1-5@one visit|10-13@a folder|18@a track"
Here's the lesson's playlist. The visitor declares one visit per kind of entry: folder, track and episode. Each entry declares accept. A folder passes the visitor to its entries, then visits itself. And a track just calls visit track, passing itself.

@art double-dispatch
That trick has a name: double dispatch. The method that runs depends on both classes, the element's and the visitor's. Accept is chosen by the element. The visit it calls is chosen by the visitor. Languages with multiple dispatch need the pattern less.

@art visitor-walks
And who traverses? In the sketch, the structure does. It could also be an iterator, or the visitor itself, mainly for an irregular traversal that depends on the results, at the cost of repeating it in each visitor.

@chapter The trade
@list heading="Consequences" items="Adding an operation is easy@easy|Related behaviour sits together@sits together|Adding an element class is hard@hard|Visits unrelated classes@no common parent|Accumulates state@accumulate|Breaks encapsulation@encapsulation"
Adding an operation is easy. Related behaviour sits together in one visitor. But adding an element class is hard: every visitor gains an operation. Visitors can visit objects with no common parent, unlike an iterator. They can accumulate state. And the last liability is encapsulation: visitors need public access to what elements hold.

@chapter Count it
@math heading="Eight entries, two visitors" items="accepts: 8 × 2 = 16 · visits: 16@eight times two;;with Visitor: 3 × 2 + 3 = 9 methods@three times two plus three;;on the elements: 3 × 2 = 6 methods@three times two"
In the lab's playlist, there are eight entries of three kinds, and two visitors: one totals the minutes, one exports the list. That's eight times two, sixteen accept calls, and as many visits. With Visitor, three times two plus three, nine methods. With each operation on the element classes, three times two, six.

@words text="The 3 extra methods are the accepts"
The three extra methods are the accepts, the price of double dispatch. In return, the six visit methods sit in two visitors, instead of across three element classes.

@art new-operation
Now add a third operation. With Visitor, it's one new visitor, and nothing changes. Without it, you edit the abstract element and all three element classes.

@art new-kind
But add a new kind of entry, say an audiobook chapter. With Visitor, that's one new class and three changed, the abstract visitor and both visitors. With operations on the elements, it's one new class and nothing changed.

@words text="Which will you add more often?" sub="operations or element classes"
That's the book's key question, as counts. If the classes will change more, keep the operations in them. Which addition your playlist will see more often isn't in the counts.

@chapter Where people slip
@list heading="Common slips" items="Using it when new kinds keep arriving@The first|Expecting elements to stay encapsulated@The second|Taking a visitor for an iterator@And the third"
The first slip is choosing Visitor where new kinds of element keep arriving. The second is expecting the elements to stay fully encapsulated. And the third is taking a visitor for an iterator. An iterator calls the elements' operations. A visitor carries an operation to them, and picks its code by their class.

@chapter Try it
@words text="A museum floor plan" sub="2 wings · vase, mask · film · 3 visitors"
Your turn. A museum with an east wing holding a vase and a mask, and a film screen, with three visitors. Count the accept calls, the methods each way, and the classes a new shop kind changes under each.

@end text="Count both additions"
Then enter it into the lab and check, on Learn. That's learn dot get er done dot I O.
