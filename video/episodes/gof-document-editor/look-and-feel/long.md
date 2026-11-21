---
format: long
lesson: gof-document-editor/look-and-feel
title: Abstract Factory in Lexi: one look and feel, never a mix
thumb: Ask the factory, not the class
---

@chapter Many standards
@title text="Supporting Multiple Look-and-Feel Standards" sub="Design Patterns, Section 2.5" art=thumb
A look and feel standard is a style guide for how an application's controls look and respond. In the early nineties every platform had its own: Motif on Unix workstations, Presentation Manager on O S two, and the Macintosh's.

@art widget-layers
They differ in detail, not in kind. But a program that runs on several has to follow each one where it runs, take new ones easily, and ideally change style while running. Lexi assumes two layers of widget classes: an abstract class per kind of widget, like a scroll bar or a button, and under each, a concrete class for each standard.

@chapter The trouble with constructors
@art scattered-constructors
The obstacle is construction. Code that creates a widget with a constructor names one standard's class. That fixes the style when the program is compiled, and scatters the choice over every place a widget is made. Porting means finding them all.

@quote text="Littering our code with constructor calls to specific look-and-feel classes yields a maintenance nightmare—miss just one, and you could end up with a Motif menu in the middle of your Mac application." cite="Gamma, Helm, Johnson and Vlissides, Design Patterns, Section 2.5"
The authors put it vividly. Littering our code with constructor calls to specific look and feel classes yields a maintenance nightmare. Miss just one, and you could end up with a Motif menu in the middle of your Mac application.

@art wrong-menu
One missed call, and the application mixes two families, a widget that looks and behaves like another platform's, sitting among the rest.

@chapter Abstract creation
@art factory-family
Their answer is to abstract creation itself. Instead of constructing a Motif scroll bar, Lexi asks a factory object for a scroll bar, and a Motif factory returns a Motif one. Nothing in the calling code names Motif. Each standard has a concrete factory, and the widgets one factory makes belong together: a product family.

@list heading="Setting the factory" items="After the style is known@after the style is known|Before the first widget@before the first widget|A registry of names to factories@a registry"
Where does the factory live? Anywhere convenient: a global, a static member, or a Singleton. What matters is that it's set after the style is known, and before the first widget is made. And a registry from names to factories lets new ones be added without editing that choice.

@words text="Kinds settled, families vary"
The pattern is Abstract Factory. The section says it suits a design whose kinds of product are settled, while its families vary. And the catalog states the other side plainly: a new kind of product is hard, because the factory's interface fixes the set of products.

@chapter A map viewer
@art map-styles
The lesson's own design is a map viewer with three styles: street, satellite and terrain. Each style is a family of three kinds of product, drawn to match: tiles, labels and markers.

@code block=1 lines=2-18 focus="2-6@one creation operation|7-11@terrain style|13@chosen once|16-17@matches the tiles"
The factory declares one creation operation for each kind of product. The terrain style makes the terrain versions. The viewer's style is chosen once, at start up, so every marker matches the tiles.

@math heading="3 styles × 3 kinds" items="3 × 3 = 9 concrete products@times three kinds;;1 + 3 + 3 + 9 = 16 classes@sixteen;;classes that create: 1 + 3 = 4@four"
Three styles times three kinds is nine concrete products. The design has one abstract factory, three concrete factories, three abstract products and the nine: sixteen classes. And the classes that create are one plus three, four.

@math heading="Two kinds of change" items="new style: +4 classes, 0 edited@a fourth style;;new kind: +4 classes, 4 edited@a compass rose"
Add a fourth style, and that's four classes, one factory and its three products, and no existing class is edited. Add a fourth kind of product instead, a compass rose: four classes again, but now four existing classes are edited, the abstract factory and each of its three concrete factories.

@art asymmetry
Same number added, different number changed. That's the asymmetry the pattern lives with. A viewer with ten styles would edit eleven factory classes for one new kind of product.

@chapter Where people slip
@list heading="Common slips" items="A constructor and a flag@The first|Expecting new kinds to be cheap@The second|Choosing the factory in many places@And the third"
The first slip is creating each product with a constructor and a flag, so the style is fixed wherever the code is written. The second is expecting new kinds of product to be cheap. And the third is choosing a factory at each creation site, which brings back the scattered decision the pattern removed.

@chapter Try it
@words text="A quiz app" sub="families: kids, adult · kinds: question, timer · new kind: hint"
Your turn. A quiz app with a kids mode and an adult mode, each a family of questions and timers. Count the classes under Abstract Factory. Then add a new kind, hints, and count the classes it adds and the existing classes it edits.

@end text="Count families and kinds"
Then check your counts in the lab, on Learn. That's learn dot get er done dot I O.
