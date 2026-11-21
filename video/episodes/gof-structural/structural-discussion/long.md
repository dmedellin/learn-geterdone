---
format: long
lesson: gof-structural/structural-discussion
title: Adapter, Bridge, Decorator, Proxy: same shape, different patterns
thumb: Same shape, different intent
---

@chapter Why they look alike
@title text="Discussion of Structural Patterns" sub="Design Patterns, end of chapter 4" art=thumb
By now you've probably noticed something. Adapter, Bridge, Decorator and Proxy all hold another object and forward to it. So how are they different patterns at all? The two pages that close chapter four answer exactly that.

@art same-shape
The authors admit it up front. The structural patterns have similar participants and collaborations, because they're built from the same few mechanisms: inheritance for the class patterns, composition for the object ones. Those similarities, they say, hide different intents.

@chapter Adapter versus Bridge
@quote text="The Adapter pattern makes things work after they're designed; Bridge makes them work before they are." cite="Gamma, Helm, Johnson and Vlissides, Design Patterns, Chapter 4"
That's the centre of the section. The Adapter pattern makes things work after they're designed. Bridge makes them work before they are.

@art after-before
Both put an extra step between a client and another object. But Adapter resolves a mismatch between two interfaces that already exist, a coupling nobody foresaw. Bridge is planned from the start, when you know an abstraction will have several implementations.

@words text="Adapter is not the lesser pattern"
And the authors add at once: that doesn't make Adapter the lesser pattern. The two simply solve different problems. Nor is a facade an adapter for many objects. A facade invents an interface of its own, where an adapter serves one that already exists.

@chapter Composite, Decorator, Proxy
@art decorator-vs-composite
Composite and Decorator both use recursive composition, so it's tempting to call a decorator a composite with one child. That misses the point. Decorator adds responsibilities without subclassing. Composite is about representation, letting many related objects be treated as one.

@art used-together
The two are often used together, under one abstract class. To Decorator, a composite is a concrete component. To Composite, a decorator is a leaf.

@art proxy-gate
And Proxy keeps a reference and forwards too, with the subject's own interface. But its subject supplies the functionality, and the proxy grants or refuses access to it. A decorator supplies part of the functionality itself. And a proxy's one relationship can be fixed when you compile, while a decorator's stack can't be known in advance.

@chapter One shape in code
@code block=1 lines=1-18 label=Java focus="1-5@vendor tiles|6-13@cached tiles|14-18@grid overlay"
Here's the lesson's map tile viewer. Three classes, one shape. Vendor tiles is an adapter, because the vendor's class existed with an interface of its own. Cached tiles is a proxy, because it stands in for a remote source and controls when it's reached. Grid overlay is a decorator, because it adds a responsibility, and could be stacked.

@words text="Nothing in the structure says which is which"
Each one implements the same interface, holds another object, and forwards. Swap the reasons, and the code could stay the same.

@chapter Count it
@math heading="Views, renderers, frames" items="3 views × 2 renderers = 6 pairings → 7 classes@three views;;(3 + 1) + (2 + 1) = 7@two hierarchies;;add frames: 3 × 2 × 3 = 18 → 19 classes@add a frame;;(3 + 1) + (2 + 1) + (3 + 1) = 11@three hierarchies"
Three views of the map, street, satellite and terrain, drawn by two renderers. That's six pairings, seven classes with a subclass each. And two hierarchies make seven too, so at this size the split saves nothing. Now add a frame round each tile, plain, shadow or border. Eighteen pairings, nineteen classes, against eleven for three hierarchies.

@words text="A fourth frame: +6 vs +1" sub="3 views × 2 renderers"
And a fourth frame adds six subclasses, three views times two renderers, against just one class when the frames have a hierarchy of their own.

@art three-aspects
Here's the point. Read the split as Bridge, if the renderers were planned. Read it as Adapter, if they were a library you found later. The counts are the same seven. Hold the frame as an object and it's a strategy. Wrap it round the view and it's a decorator. The count records the design, but doesn't make the choice.

@chapter Where people slip
@list heading="Common slips" items="Identifying a pattern by structure@The first|Ranking Adapter below Bridge@The second|Calling a decorator a degenerate composite@And the third"
So, three slips. The first is identifying a pattern by its structure. The second is ranking Adapter below Bridge, as if fitting one later were a failure to plan. And the third is calling a decorator a degenerate composite.

@chapter Try it
@words text="Add a fourth view: transit" sub="4 views · 2 renderers · 3 frames"
Your turn. The viewer gains a fourth view, transit. By hand, give the pairings, the classes as subclasses and as three hierarchies, and what one more view would add to each.

@end text="Read one design three ways"
Then check your counts in the lab, on Learn. That's learn dot get er done dot I O.
