---
format: long
lesson: gof-introduction/what-is-a-design-pattern
title: What is a design pattern? The Gang of Four's answer
thumb: Name, problem, solution, cost
---

@chapter The puzzle
@title text="What Is a Design Pattern?" sub="Design Patterns, Chapter 1" art=thumb
Reusable object oriented design is hard. Experienced designers say they rarely get it right the first time. And yet they do produce good designs, while newcomers, faced with too many options, fall back on old habits. So what do the experts know?

@art folklore-shapes
The book's answer is that experts don't start every problem from nothing. They reuse arrangements that worked before, so the same shapes of classes and communicating objects turn up in system after system. The authors set out to write those shapes down, each one named, explained and evaluated.

@words text="None of them is new" sub="each used more than once, in different systems"
And they stress that none of it is new. Every design in the catalog had been used more than once, in different systems. Most of them lived only in folklore, or inside successful programs.

@chapter The definition
@quote text="A design pattern names, abstracts, and identifies the key aspects of a common design structure that make it useful for creating a reusable object-oriented design." cite="Gamma, Helm, Johnson and Vlissides, Design Patterns, Section 1.1"
Here's how Section one point one puts it. A design pattern names, abstracts, and identifies the key aspects of a common design structure that make it useful for creating a reusable object oriented design.

@words text="A recurring problem + the core of its answer" sub="from Christopher Alexander: walls and doors → objects and interfaces"
They borrow the idea from the architect Christopher Alexander, whose patterns describe a problem that keeps coming back, and the core of a solution you can use countless times. Alexander meant buildings and towns. The authors keep the shape and change the material, from walls and doors to objects and interfaces.

@art size-scale
They also fix the size they mean. A linked list or a hash table, coded once and reused as it stands, is too small. The design of a whole application for one domain is too large. The book's patterns sit in between.

@chapter Four elements
@list heading="Every pattern has" items="Name@the name|Problem@the problem|Solution@the solution|Consequences@the consequences"
Every pattern has four essential elements. First, the name, a word or two that lets designers think and talk at a higher level. Second, the problem, which says when to apply it. Third, the solution, an abstract arrangement of roles, a template rather than one implementation. And fourth, the consequences, the results and trade offs.

@art four-elements
The authors insist on that last one. Designers often leave the costs unspoken, but the costs are what you need to choose between designs. Every later lesson is built around these four.

@chapter MVC, read three ways
@art mvc-three-views
Section one point two reads a familiar design: Smalltalk's Model View Controller. A model holds the data, and each view presents it. Whenever the model changes, it tells the views that depend on it, and each one updates itself. The book shows one set of figures drawn three ways at once.

@list heading="Inside MVC" items="Observer@that's Observer|Composite@that's Composite|Strategy@that's Strategy"
Read generally, letting one change reach any number of objects without knowing what they are: that's Observer. Views nest, and a group of views is used like a single view: that's Composite. And a view hands its response to input to a replaceable controller object: that's Strategy.

@art nested-views
MVC uses others in passing, Factory Method and Decorator, but those three are its main relationships. So one familiar design is really several patterns working together.

@chapter A bike dock
@code block=1 lines=2-20 focus="2-4@knows its views|11-12@each time|16-17@on every attached view"
Here's the protocol on the lesson's own example, a bike share dock. The dock knows its views only through this small interface. It names no screen. Each time its count of bikes changes, it calls update on every attached view.

@art dock-views
There are three views: the screen at the dock, the city map in a rider's app, and the operator's ledger. Four operations run: a rental, a drop off, a swap and a repair. The swap changes the dock twice.

@math heading="Count the updates" items="5 changes × 3 views = 15 updates@fifteen updates;;change manager: 12 updates · 3 redundant@twelve;;add an alerts view: 20 · 16@twenty"
So the lab counts five changes, and fifteen updates sent, five to each view. A change manager that sends each view one update per operation sends twelve, and the three redundant ones are the swap's second round. Attach a fourth, alerts view, and updates rise to twenty, or sixteen with the manager.

@words text="Dock isn't edited at all"
And the class Dock isn't edited at all. New views cost one more update for every change, and nothing in the model.

@chapter Where people slip
@list heading="Common slips" items="Taking a pattern for a reusable class@The first|Reading MVC as one pattern@The second|Treating the costs as optional@And the third"
The first slip is taking a pattern for a class you reuse as it stands. It's an arrangement of roles you build again, with your own names. The second is reading MVC as one pattern, when it's at least three. And the third is treating the consequences as an optional extra. They're one of the four elements.

@chapter Try it
@words text="A quiz scoreboard, four views" sub="podium · league table · host · phones"
Your turn. A quiz app's scoreboard is the model, with four views: the podium screen, the league table, the host's console, and each player's phone. Count the changes, the updates sent directly, and what a change manager would send. Then say where the redundant updates come from.

@end text="Count the updates yourself"
You can run the dock and the scoreboard in the lab, on Learn. That's learn dot get er done dot I O.
