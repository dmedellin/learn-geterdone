---
format: long
lesson: gof-introduction/describing-and-organizing-the-catalog
title: How the Gang of Four catalog is written and organised
thumb: Thirteen sections, two criteria
---

@chapter Why a template
@title text="Describing and Organizing the Catalog" sub="Design Patterns, Sections 1.3 to 1.5" art=thumb
Twenty three patterns, and every one is written the same way. That's a choice, and these three sections explain it, then sort the whole catalog on two simple criteria.

@art diagram-not-enough
Start with why. A diagram isn't enough to describe a pattern. It shows the classes and objects a design ended up with, but not the choices made on the way, the options turned down, and what each one cost. And those are exactly what someone reusing the design needs.

@quote text="The template lends a uniform structure to the information, making design patterns easier to learn, compare, and use." cite="Gamma, Helm, Johnson and Vlissides, Design Patterns, Section 1.3"
So each pattern follows a fixed template. In the authors' words, the template lends a uniform structure to the information, making design patterns easier to learn, compare, and use.

@chapter Thirteen sections
@code block=1 lines=1-13 focus="1-3@the name|4-5@motivation|6-8@structure|9-13@consequences"
There are thirteen sections, and they fall into four groups. The name, its classification, the intent and any other names say what the pattern is. Motivation and applicability say when to use it. Structure, participants and collaborations say what it's made of. And consequences, implementation, sample code, known uses and related patterns say what using it involves.

@art four-groups
That last group carries a lot. The trade offs, the pitfalls of building it, code in C plus plus or Smalltalk, at least two uses in real systems from different domains, and its neighbours in the catalog. The pattern lessons on this path follow the same order.

@words text="Abstract Factory … Visitor" sub="Section 1.4: 23 names, each with its intent"
Section one point four is the table of contents: all twenty three names in alphabetical order, each with its intent, from Abstract Factory to Visitor. Read it through once now. You'll come back to it.

@chapter Purpose and scope
@list heading="Purpose" items="Creational: making objects@creational|Structural: composing them@structural|Behavioral: how they interact@behavioral"
Section one point five sorts the patterns by two criteria. The first is purpose, what a pattern does. Creational patterns are about making objects. Structural ones are about composing classes or objects. And behavioral ones are about how they interact and share out the work.

@art class-vs-object
The second is scope. Class patterns are about relationships between classes and their subclasses. They're set by inheritance, so they're fixed at compile time. Object patterns are about relationships between objects, which can change while the program runs.

@words text="Most of the catalog has object scope"
Almost every pattern uses inheritance somewhere, the authors note. So only the ones whose point is a class relationship count as class patterns, and most of the catalog has object scope.

@art purpose-scope-grid
Cross the two, and each cell says something. A creational class pattern, like Factory Method, leaves making an object to a subclass. A creational object pattern, like Abstract Factory or Singleton, leaves it to another object. Template Method and Interpreter are behavioral class patterns, while Observer and Strategy are behavioral object patterns.

@chapter Other maps
@art catalog-map
Purpose and scope aren't the only map. Some patterns are used together, like Composite with Iterator. Some are alternatives, like Prototype instead of Abstract Factory. Some, like Composite and Decorator, have similar diagrams for different intents. And the cross references make a map of the whole catalog, Figure one point one.

@chapter Select from eight
@math heading="Selecting by specification" items="scope = class → factory-method, template-method@scope equals class;;purpose = behavioral and scope = object → observer, strategy@behavioral and scope equals object;;purpose = creational or scope = class → 4@creational or"
The lab takes eight candidates. Ask for scope equals class, and it selects two: Factory Method and Template Method. Ask for purpose behavioral and scope equals object, and you get Observer and Strategy. Ask for purpose creational or scope class, and it selects four: the three creational patterns and Template Method.

@art failing-clause
For each pattern it rejects, the lab shows the clause that failed. In the second search, five fail on purpose, and Template Method fails on scope, because it's behavioral but a class pattern.

@words text="Only as good as the records" sub="the lab checks the records against nothing"
One caution. A selection is only as good as the attributes typed in. The lab checks the specification against the records, and the records against nothing.

@chapter Where people slip
@list heading="Common slips" items="Reading only the structure diagram@The first|Thinking object patterns don't inherit@The second|Treating the table as the only map@And the third"
The first slip is reading only the structure diagram, which loses applicability and consequences. The second is thinking object patterns don't use inheritance. Observer and Strategy do, and they're still object patterns. And the third is treating the classification as the only map of the catalog.

@chapter Try it
@words text="scope = class or purpose = structural" sub="Builder · Bridge · Interpreter · Iterator"
Your turn. Four more patterns: Builder and Bridge have object scope, Interpreter is a behavioral class pattern, and Iterator a behavioral object pattern. For the specification scope class or purpose structural, say which are selected, and which clause each of the others fails.

@end text="Select from the catalog"
Add them to the lab and check, on Learn. That's learn dot get er done dot I O.
