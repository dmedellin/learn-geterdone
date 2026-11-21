---
format: long
lesson: gof-document-editor/spelling-and-hyphenation
title: Iterator and Visitor in Lexi: new analyses, untouched classes
thumb: Separate the walk from the work
---

@chapter Many analyses
@title text="Spelling Checking and Hyphenation" sub="Design Patterns, Sections 2.8 and 2.9" art=thumb
The last of Lexi's problems is analysis. Spelling checking and hyphenation are two, but the authors expect many more: searching, counting words, adding up a table, checking grammar. And they don't want to change Glyph and all its subclasses for each one.

@art access-and-analysis
So they split the problem in two. First, reaching the information scattered through the structure. Second, doing the analysis itself.

@chapter Reaching the parts
@art traversal-orders
Reaching it is harder than it looks. Children may sit in arrays, lists, or something stranger. And analyses walk in different orders: forward, backward for a reverse search, or in order for an expression.

@list heading="Traversal on Glyph?" items="A new order changes the interface@a new order|Can't reuse it for other structures@cannot be reused|One traversal at a time@one traversal"
A first fix puts traversal operations on Glyph itself, with a parameter naming the order. But a new order means changing that parameter or adding operations, the mechanism cannot be reused for other structures, and only one traversal can be under way at a time.

@art iterator-stack
So the authors encapsulate the concept that varies once more, in an Iterator hierarchy. Each glyph creates an iterator over its own children. A leaf makes a null iterator, done at once. And a preorder iterator keeps a stack of them, so each walk holds its own place.

@chapter Doing the analysis
@words text="Not in the iterator · not in the glyphs"
Where does the analysis go? Not in the iterators, which would tie each analysis to one walk. And not in the glyph classes, which would mean editing every one for each new analysis, burying the glyph's real interface. So the analysis becomes an object the iterator carries to each glyph.

@art double-dispatch
It still has to tell a letter from a picture, and the authors refuse to do that with type tests and casts. Instead each glyph gets one operation that calls back the analyser's method for its own class. Call the analyser a visitor, and that operation accept, and a new analysis is just a new visitor subclass.

@code block=1 lines=2-16 focus="2-6@a visit method|7@accept|9@calls back|11-15@shopping list"
In the recipe book, the visitor has a visit method for each kind of part: section, recipe and photo. Every part has an accept. A recipe's accept calls back visit recipe, with itself. And a shopping list is a new analysis: it collects ingredients from recipes, and ignores the rest.

@chapter Which hierarchy changes?
@list heading="Visitor's trade" items="New operations: easy@adding an operation|Related behaviour gathered@gathered|New kinds of element: hard@a new kind of element|Elements expose state@expose state"
The catalog names the price beside the gain. Adding an operation is easy, and related behaviour is gathered in one class. But adding a new kind of element is hard, because every visitor gains a method for it, and visitors often need elements to expose state.

@quote text="An important question to ask yourself before applying the Visitor pattern is, Which class hierarchies change most often?" cite="Gamma, Helm, Johnson and Vlissides, Design Patterns, Section 2.8"
So the section ends on a question. An important question to ask yourself before applying the Visitor pattern is, which class hierarchies change most often? For Lexi, new analyses are far likelier than new kinds of glyph.

@chapter Count it
@math heading="10 nodes · 3 kinds · 2 visitors" items="10 × 2 = 20 accept calls + 20 visit calls@ten times two;;Visitor: 3 × 2 + 3 = 9 methods@nine methods;;on the elements: 3 × 2 = 6@six"
Back to the recipe book: ten nodes of three kinds, and two visitors, a timer and a costing. Every node accepts each visitor once: ten times two, twenty accept calls, and twenty visit calls. As visitors, the analyses take nine methods. As operations on the elements, six.

@math heading="Which change is cheap?" items="new analysis: Visitor 1 added, 0 changed · elements: 4 changed@a third analysis;;new kind: Visitor 3 changed · elements: 0 changed@a wine pairing"
Add a third analysis, the shopping list. With Visitor, one class is added and none changed. Without it, four classes change. Now add a new kind of part, a wine pairing, and the counts swap. With Visitor, three classes change. Without it, nothing else changes.

@art new-kind-cost
Neither design is cheaper in general. The count says which change each makes cheap, and the authors' question decides between them.

@art eight-patterns
That ends the case study, and its eight patterns: Composite, Strategy, Decorator, Abstract Factory, Bridge, Command, Iterator and Visitor. And none of these problems belongs to editors alone.

@chapter Where people slip
@list heading="Common slips" items="An operation on every class per analysis@The first|Type tests in the analysis@The second|Visitor without asking what changes@And the third"
The first slip is adding an operation to every element class for each new analysis. The second is telling kinds apart with type tests. And the third is adopting Visitor without asking which hierarchy changes more often.

@chapter Try it
@words text="The mixtape, three analyses" sub="duration · artists · playcount"
Your turn. Take the mixtape from the first lesson, with three analyses: duration, artists and play count. Count the accept calls, the methods with Visitor and without, and the classes a new kind of node changes under each design.

@end text="Visit the whole tree"
Then type it into the lab and check, on Learn. That's learn dot get er done dot I O.
