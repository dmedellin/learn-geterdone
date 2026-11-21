---
format: long
lesson: gof-creational/creational-discussion
title: Comparing the creational patterns: subclass or pass an object?
thumb: Start simple, evolve
---

@chapter Two ways
@title text="Discussion of Creational Patterns" sub="Design Patterns, Chapter 3" art=thumb
Chapter three closes by setting its five patterns side by side. The comparison is short, and it boils down to one choice.

@quote text="There are two common ways to parameterize a system by the classes of objects it creates." cite="Gamma, Helm, Johnson and Vlissides, Design Patterns, Chapter 3"
Here's how it opens. There are two common ways to parameterize a system by the classes of objects it creates.

@art subclass-the-creator
The first is to subclass the class that does the creating. That's Factory Method. Its drawback is that changing the product's class can take a new subclass, and the need can cascade. If the creator is itself made by a factory method, its own creator has to be overridden too.

@art pass-a-factory
The second leans on composition. Define an object whose job is to know the product classes, and hand it to the system. Abstract Factory, Builder and Prototype all do this, each with its own kind of factory object.

@list heading="Three factory objects" items="Makes objects of several classes@several classes|Builds a product step by step@step by step|Copies itself@copies itself"
One that makes objects of several classes. One that builds a complex product step by step. And one that copies itself, so in Prototype the factory object and the sample of the product are one and the same.

@chapter The drawing editor
@art editor-palette
The authors return to the graphical editor from Prototype, whose tool must be parameterized by the class of graphic it adds, and try each pattern. Factory Method gives a tool subclass per graphic. Abstract Factory gives a factory class per graphic. Prototype gives each tool a prototype to clone.

@list heading="Their verdict for that framework" items="Factory Method: easiest, many small subclasses@easiest at first|Abstract Factory: an equally large hierarchy@little improvement|Prototype: probably the best fit@probably fits best"
Their judgement: Factory Method is easiest at first, but multiplies small subclasses that do little. Abstract Factory offers little improvement, because its factory hierarchy is just as large. And Prototype probably fits best, since it needs only a clone operation on each graphic class, which also serves a duplicate command.

@chapter The general lesson
@words text="Not needed if the class never changes"
Factory Method makes a design more customisable at little extra cost. But it isn't needed when the instantiated class never changes, or when creation already happens in an operation subclasses can override. The other three are more flexible still, and more complex.

@art evolve-arrow
So start simple.

@quote text="Often, designs start out using Factory Method and evolve toward the other creational patterns as the designer discovers where more flexibility is needed." cite="Gamma, Helm, Johnson and Vlissides, Design Patterns, Chapter 3"
Here's the line to remember. Often, designs start out using Factory Method and evolve toward the other creational patterns as the designer discovers where more flexibility is needed.

@art same-shape
Notice two things. The verdict is for one framework, and the authors say the best choice turns on many factors. And it isn't a comparison of class counts. Factory Method and Abstract Factory have the same shape. What separates them is where the choice is made: in a subclass, or in an object passed in.

@chapter A quiz palette
@code block=1 lines=2-17 comments=keep focus="2-5@a tool subclass|7-12@a factory|14-17@a prototype"
Here are all three on a quiz builder's palette. Factory Method: each question type gets a tool subclass that overrides new question. Abstract Factory: one tool class, handed a factory. Prototype: one tool class, handed a prototype to copy.

@math heading="4 question types, 1 kind each" items="Factory Method: 1 + 4 + 1 + 4 = 10@factory method;;Abstract Factory: 1 + 4 + 1 + 4 = 10@abstract factory;;Prototype: 1 + 1 + 4 = 6@prototype"
Four types: multiple choice, true or false, short answer and matching. Under factory method, the lab counts ten classes. Under abstract factory, ten again, the equally large hierarchy the authors describe. Under prototype, a manager, an abstract question and four question classes: six.

@math heading="Add ordering" items="Factory Method: 10 → 12@twelve;;Abstract Factory: 10 → 12@so does Abstract Factory;;Prototype: 6 → 7, plus 1 configuration@seven"
Add a fifth type, ordering. Factory Method goes from ten to twelve, and so does Abstract Factory. Prototype goes from six to seven, with one configuration that registers its prototype. None edits an existing class.

@art values-not-classes
And if the types differed only in values, Prototype could make them instances of one class, like the whole and half notes, and its count would fall further.

@chapter Where people slip
@list heading="Common slips" items="Reading the verdict as a ranking@The first|Starting with the most flexible@The second|Thinking composition needs no classes@And the third"
The first slip is reading the drawing editor verdict as a ranking of the patterns. The second is starting with the most flexible pattern. And the third is thinking composition needs no new classes. Abstract Factory still needs a factory per family. The classes move. They don't all disappear.

@chapter Try it
@words text="Two products per type" sub="question + rubric · choice, truefalse, short, match"
Your turn. Each question type now needs two products, a question and a rubric that marks it. Using the lab's formulas, count the classes under Abstract Factory, Factory Method and Prototype, and what a fifth type adds under each.

@end text="One design, three patterns"
Then switch the scheme in the lab and check, on Learn. That's learn dot get er done dot I O.
