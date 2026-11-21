---
format: long
lesson: gof-document-editor/formatting
title: Strategy in Lexi: the line breaker becomes an object
thumb: Swap the algorithm, keep the page
---

@chapter Representing isn't formatting
@title text="Formatting" sub="Design Patterns, Section 2.3" art=thumb
Lexi's document is now a tree of glyphs. But a tree says how a formatted document is held, not how you get from a stream of letters and pictures to the right lines and columns. That's formatting, and it's the second problem.

@art stream-to-lines
The authors narrow it to line breaking. Breaking lines into columns, and columns into pages, works the same way. And it's hard to do well, because there's no one right algorithm.

@list heading="No one right algorithm" items="Quality against speed@quality of its lines|Slower typing for better pages@slower typing|Memory for speed@caching"
An interactive editor trades the quality of its lines against the speed of its response. A user might accept slower typing for better pages. And caching more can buy speed with memory. Not all of that can be decided when the program is compiled.

@chapter Two independences
@art two-independences
So the authors want two kinds of independence. A new kind of glyph shouldn't need to know about the formatting algorithm. And a new algorithm shouldn't need any edits to the existing glyphs.

@quote text="We can isolate the algorithm and make it easily replaceable at the same time by encapsulating it in an object." cite="Gamma, Helm, Johnson and Vlissides, Design Patterns, Section 2.3"
Their move fits in one sentence. We can isolate the algorithm and make it easily replaceable at the same time by encapsulating it in an object.

@chapter Compositor and Composition
@art compositor-composition
The algorithm lives in a class called Compositor. A Composition, a special glyph, holds the unformatted content and a compositor. Whenever the document changes, it asks the compositor to compose, and the compositor walks the children and inserts the row and column glyphs the lines need.

@words text="A quick pass · Knuth's TeX" sub="setCompositor: change it while Lexi runs"
One subclass might make a quick pass. Another might run Knuth's TeX algorithm, which weighs how evenly the text is spread, and takes longer. Add one operation to set the compositor, and the algorithm can be changed while Lexi runs.

@chapter Strategy
@list heading="Strategy" items="Strategy: the compositor@the strategy|Context: the composition@its context|Interfaces general enough@general enough"
The pattern is Strategy. The compositor is the strategy, and the composition is its context. The authors put the weight on one point: both interfaces have to be general enough for any algorithm in the family.

@words text="Costs" sub="know the strategies apart · extra data passed · more objects"
The catalog adds the costs. A client has to know how the strategies differ to choose one. The context and strategy may pass each other more than a given algorithm uses. And there are more objects.

@chapter A playlist app
@art playlist-orderings
Now a design of the lesson's own, a playlist app. Kinds of playlist play the part of compositions, and ordering algorithms, like shuffle or by tempo, play the part of compositors.

@code block=1 lines=2-17 focus="2-4@an interface|5-11@by tempo|14-16@holds an ordering|17@play order"
The lesson's sketch has the same shape. An ordering is an interface. Sorting by tempo is one ordering. A playlist holds an ordering, and can be handed a new one at run time. Its play order just asks the ordering to arrange the tracks.

@math heading="3 playlists, 4 orderings" items="3 × 4 = 12 → 12 + 1 = 13 classes@three times four;;(3 + 1) + (4 + 1) = 9@three plus one;;13/9 ≈ 1.4×@thirteen ninths;;fifth ordering: 13 → 16 vs 9 → 10@a fifth ordering"
Compare it with the design Section two point three avoids, a subclass for each pairing. Three times four is twelve, plus the base, thirteen classes. Two hierarchies need three plus one, plus four plus one: nine. That's thirteen ninths, about one point four times. A fifth ordering adds three subclasses, against one class.

@art pairings-grid
See the shape of it. Subclassing grows as a product of the two counts, so the grid fills in. Composition grows as their sum, one short column on each side.

@math heading="A new kind of playlist" items="subclassing: 13 → 17@seventeen;;composition: 9 → 10@nine to ten"
Add a kind of playlist instead. Under subclassing, that's four new classes, thirteen to seventeen. Under composition it's one, nine to ten, and no ordering is touched. Those are the two independences, as counts.

@art runtime-switch
What the count leaves out is the run time switch. A combined subclass can't change its algorithm without becoming a different object. A playlist that holds an ordering is simply handed a new one.

@chapter Where people slip
@list heading="Common slips" items="Putting the algorithm in the document classes@The first|Treating Strategy as free@The second|Shaping the interface around one algorithm@And the third"
The first slip is putting the formatting algorithm inside the document classes, which gives neither independence. The second is treating Strategy as free. At small sizes the class count may not fall at all. And the third is designing the strategy interface around the first algorithm, so it has to change for the next.

@chapter Try it
@words text="A recipe-card printer" sub="cards: index, full-page · layouts: compact, spacious, two-column"
Your turn. A recipe card printer has two kinds of card and three layout algorithms. Count the classes under each design, and the classes a fourth layout adds to each. Then say what the ratio shows.

@end text="Count both designs"
Type the aspects into the lab and check, on Learn. That's learn dot get er done dot I O.
