---
format: long
lesson: gof-document-editor/document-structure
title: Composite in the Gang of Four's document editor
thumb: A part or the whole, one call
---

@chapter Seven problems
@title text="Design Problems and Document Structure" sub="Design Patterns, Sections 2.1 and 2.2" art=thumb
Before the catalog begins, the Gang of Four design one program: an editor called Lexi, which shows the page as it will print. Its design turns up eight of the catalog's patterns.

@list heading="Lexi's seven problems" items="Document structure@represent the document|Formatting@format it|Embellishment@decorations|Look and feel@look and feel|Window systems@window system|User operations@menus and buttons|Spelling and hyphenation@spelling"
Section two point one lists seven problems. How to represent the document. How to format it into lines and columns. How to add decorations, like borders and scroll bars. How to support more than one look and feel. How to run on more than one window system. How to give menus and buttons one way to reach operations and undo them. And how to add analyses like spelling checking.

@chapter Two constraints
@art page-structure
The first problem touches everything, because editing, formatting, display and analysis all walk the document. So the representation should match the page's physical structure, text and pictures laid out into lines, columns and tables, so a user can treat a table or a diagram as one thing.

@list heading="Two constraints" items="Text and graphics alike@text and graphics|One element and a group alike@a group"
Two constraints follow. Text and graphics should be handled alike, with no second set of mechanisms. And a single element and a group should be handled alike, so the tenth thing in a line can be one letter or a whole diagram, and the line doesn't care.

@art polygon-spelling
Against that second one, the authors note straight away, some analyses do care. Nobody checks the spelling of a polygon. That tension comes back in the last lesson.

@chapter Recursive composition
@quote text="A common way to represent hierarchically structured information is through a technique called recursive composition, which entails building increasingly complex elements out of simpler ones." cite="Gamma, Helm, Johnson and Vlissides, Design Patterns, Section 2.2"
Here's the technique they settle on. A common way to represent hierarchically structured information is through a technique called recursive composition, which entails building increasingly complex elements out of simpler ones.

@art glyph-tree
Letters and pictures are tiled into a line, lines stacked into a column, and columns into a page. Every element, visible or structural, is an object. So the objects need classes, and the classes need compatible interfaces: a common base class, called Glyph.

@list heading="Every glyph" items="Draws itself@draws itself|Knows its bounds@the rectangle|Knows its children and parent@its children"
A glyph has three responsibilities. It draws itself in a window. It knows the rectangle it occupies, and whether a point falls inside it, which is how a click finds its target. And it knows its children and its parent.

@chapter Composite
@art composite-roles
The pattern is Composite. A component interface, leaf classes with no children, and composite classes that hold components and pass an operation on to each one. The benefit is a simple client. The cost is a design so general that the type system can't restrict what goes inside a composite.

@words text="Transparency or safety?" sub="declare add on every part, or on composites only"
There's a choice in where to declare the child operations. On every component, as Lexi's Glyph does, and every part is treated alike, but a client can ask a leaf for a child it can't have. On the composite only, and the compiler catches that, at the price of two interfaces. The authors call these transparency and safety.

@code block=1 lines=2-19 focus="2-4@one question|12@on the section only|15-17@a recipe or a whole section"
Here's the lesson's recipe book in Java, on the safe side. Every part answers one question: how long? Add is on the section only. And a section's answer just asks each of its parts, whether that's a recipe or a whole section.

@chapter Count the calls
@art recipe-book
Now the count, on the recipe book rather than Lexi's pages. Sections hold recipes, and sections hold other sections, like the layer cakes inside cakes.

@math heading="One question, the whole book" items="10 nodes: 4 sections, 6 leaves@ten nodes;;1 + 3 + 2 + 2 + 2 = 10 calls@ten calls;;0 + 95 + 40 + 55 + 120 + 35 = 345 minutes@three hundred and forty five"
The book has ten nodes: four sections and six leaves, five recipes and a cover photo worth zero. Asking the book how long everything takes makes ten calls, one from the client and nine forwarded by sections. It totals three hundred and forty five minutes.

@words text="breads 135 · cakes 210 · layer 175" sub="depth 3 · the photo answers 0"
Breads takes one hundred and thirty five, cakes two hundred and ten, and the layer cakes inside cakes take one hundred and seventy five. The photo answers too, with zero: text and graphics treated alike.

@art safe-vs-transparent
Now ask pitta, a recipe, and layer, a section, to add a child. Under the safe declaration, layer does, and pitta's call doesn't compile. In the talk outline preset, set to transparent, the same mistake compiles, and the slide has to ignore it or fail at run time.

@chapter Where people slip
@list heading="Common slips" items="One case for an element, another for a group@The first|An object per character as universal advice@The second|Thinking no operation may tell kinds apart@And the third"
The first slip is writing one case for a single element, and another for a group. Every client then grows a type test. The second is taking an object per character as advice for any editor. The authors point to Flyweight for that cost. And the third is thinking uniform treatment means no operation may tell kinds apart.

@chapter Try it
@words text="A mixtape" sub="mix → side-a, side-b, t5 · side-b → t3, encore"
Your turn. A mixtape, with two sides, an encore inside side b, and a track directly under the mix. Count the calls one operation on the mix makes, the total it returns, and side b's subtotal.

@end text="Ask the whole tree"
Then type the records into the lab and check, on Learn. That's learn dot get er done dot I O.
