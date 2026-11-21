---
format: long
lesson: gof-document-editor/embellishing-the-interface
title: Decorator in Lexi: borders and scroll bars without subclasses
thumb: Wrap it, don't subclass it
---

@chapter Borders and scroll bars
@title text="Embellishing the User Interface" sub="Design Patterns, Section 2.4" art=thumb
Lexi's page needs a border and scroll bars. The authors want them easy to add and remove, even while the program runs, and invisible to the rest of the interface. That turns out to be a design problem.

@art subclass-combinations
Inheritance fails both tests. A bordered composition is a subclass. A scrollable one is another, and one with both is a third. Carry on, and there's a class for every combination, growing out of hand, and none of them can be rearranged at run time.

@art who-holds-whom
Object composition is the alternative, which leaves one question: who holds whom? If the glyph held its border, every glyph class would have to know about borders. If the border holds the glyph, the drawing of borders stays in one class.

@chapter Transparent enclosure
@words text="A border is a glyph" sub="clients shouldn't care whether there is one"
Then comes the step that makes it work. A border has an appearance, so it can be a glyph. More to the point, clients shouldn't care whether a glyph has a border. If Border is a subclass of Glyph, a client tells a bordered glyph to draw, exactly as it told the plain one.

@quote text="All this leads us to the concept of transparent enclosure, which combines the notions of (1) single-child (or single-component) composition and (2) compatible interfaces." cite="Gamma, Helm, Johnson and Vlissides, Design Patterns, Section 2.4"
The authors name the idea. All this leads us to the concept of transparent enclosure, which combines the notions of single child composition, and compatible interfaces.

@art forward-then-add
Lexi gathers this in MonoGlyph, an abstract glyph that holds one component and forwards every request to it. A border's draw forwards first, so the component draws itself, and then draws the border. It extends the forwarded operation, rather than replacing it.

@chapter Order and limits
@art border-scroller-order
Lexi's page puts the composition inside a scroller, and the scroller inside a border. Reverse that, and the border scrolls with the text, which a designer may or may not want. So the order of wrapping is a design choice.

@words text="One component, never several" sub="grouping is the job of rows and columns"
And an embellishment encloses one glyph, never several. Grouping is already the job of rows and columns, and mixing it into embellishment would duplicate it.

@list heading="Decorator's costs" items="Not the same object@not the same object|Many small look-alikes@many small"
The pattern is Decorator, where embellishment means any added responsibility, not just a visual one. The catalog is fair about its costs. A decorated object is not the same object as the one inside it, so identity checks can be fooled. And many small, similar decorators can be easy to configure, but hard to learn and debug.

@chapter An audio guide
@art audio-guide
Now a design of the lesson's own. A museum rents audio guides. The guide costs six, and three options wrap it: headphones add two, a family rate multiplies by three, and a donation adds one point five.

@code block=1 lines=2-16 focus="2-4@one question|5-9@forwards|12-14@multiplies|16@three decorators"
A charge answers one question, its amount. The abstract decorator holds one charge and forwards to it. The family decorator forwards, then multiplies the result by three. And here three decorators wrap the guide.

@math heading="Innermost first" items="guide: 6@the guide is six;;headphones: 6 + 2 = 8@headphones;;family: 8 × 3 = 24@family;;donation: 24 + 1.5 = 25.5@donation"
The request goes in through donation, family and headphones to the guide, and comes back out the other way. The guide is six. Headphones add two, making eight. Family multiplies by three, making twenty four. And the donation adds one point five, for twenty five point five.

@math heading="Change the order" items="reversed: (6 + 1.5) × 3 + 2 = 24.5@reversed;;family first: 6 × 3 + 2 + 1.5 = 21.5@family innermost;;two adds: 9.5 either way@two additions"
Reversed, with the donation innermost, it's twenty four point five. With family innermost, twenty one point five. Drop the family rate, and both orders give nine point five, because two additions commute. Order changes the result only when the operations don't.

@art decorator-growth
And the classes? Three options as subclasses take eight: the plain guide and seven combinations. Decorator takes six. A fourth option adds eight subclasses, against one decorator. That growth, two to the n against n plus three, is the authors' argument, along with rearranging at run time.

@chapter Where people slip
@list heading="Common slips" items="Every option as a subclass@The first|Assuming order never matters@The second|One decorator around several@And the third"
The first slip is adding each optional feature as a subclass. The second is assuming the order of decorators never matters. And the third is making one decorator enclose several components. Then it isn't transparent any more. It's a composite with something added.

@chapter Try it
@words text="A theatre ticket at 40" sub="booking fee + 2.5 · member × 0.8"
Your turn. A theatre ticket at forty, with a booking fee that adds two point five and a member rate that multiplies by nought point eight, booking fee innermost. Give the result as listed, and in the reverse order, and the call order a request follows.

@end text="Wrap the charge yourself"
Then check it in the lab, on Learn. That's learn dot get er done dot I O.
