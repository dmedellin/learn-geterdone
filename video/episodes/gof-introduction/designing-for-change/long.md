---
format: long
lesson: gof-introduction/designing-for-change
title: Designing for change: eight causes of redesign
thumb: One kind of change, not all
---

@chapter Why change matters
@title text="Designing for Change" sub="Design Patterns, Section 1.6" art=thumb
Getting the most out of a design depends on seeing change coming. Ignore it, and you risk a major redesign later: classes redefined and rebuilt, clients modified, and everything tested again.

@quote text="Each design pattern lets some aspect of system structure vary independently of other aspects, thereby making a system more robust to a particular kind of change." cite="Gamma, Helm, Johnson and Vlissides, Design Patterns, Section 1.6"
Here's how the authors put the role of patterns. Each design pattern lets some aspect of system structure vary independently of other aspects, thereby making a system more robust to a particular kind of change.

@words text="“particular”" sub="one kind of change, not change itself"
The word that matters there is particular. A pattern protects against one kind of change, not against change in general. Keep that in mind, because the count at the end shows it.

@chapter Eight causes
@list heading="Causes of redesign, one to four" items="Naming a class to create an object@naming its class|Depending on one operation@one particular operation|Depending on a platform@a platform|Knowing how an object is stored@how an object is stored"
The section lists eight common causes of redesign. One: creating an object by naming its class, which commits you to an implementation. Abstract Factory, Factory Method and Prototype create objects indirectly. Two: depending on one particular operation. Chain of Responsibility and Command avoid that. Three: depending on a platform. And four: clients that know how an object is stored, laid out or built.

@list heading="Causes five to eight" items="Depending on an algorithm@an algorithm|Tight coupling@tight coupling|Extending by subclassing@subclassing|A class you can't alter@can't conveniently alter"
Five: depending on an algorithm that will be extended or replaced. Strategy, Iterator and Visitor isolate it. Six: tight coupling, until the system is one dense mass. Seven: extending by subclassing, which can multiply classes. And eight: a class you can't conveniently alter, because you lack its source. Adapter, Decorator and Visitor work around it.

@art dense-mass
Read the list as a tool. When a design hurts, ask which of the eight it is, and the section tells you which patterns to look at.

@chapter What you're building
@art three-kinds
How much flexibility you need depends on what you're building. In an application, like a document editor, the priorities are internal reuse, maintainability and extension. A toolkit, a library of general classes, is called by applications it can't foresee, so it mustn't make assumptions that limit where it's used.

@code block=1 lines=2-12 focus="3-8@written once|9-10@supplies"
A framework is hardest of all. It's a reusable design for one kind of software, and an application customises it by subclassing. Here the framework's job class owns the loop, written once. The application only supplies the hooks: when to run, and what work to do.

@art inversion-of-control
That inverts the usual relationship. With a toolkit, your code is in charge and calls the library. With a framework, the framework's code is in charge and calls yours. And because applications built on it are exposed to every change in its interfaces, loose coupling matters most here.

@words text="More abstract · smaller · less specialised" sub="patterns, compared with frameworks"
Patterns and frameworks differ in three ways. Patterns are more abstract: they have to be implemented each time. They're smaller: a framework contains several. And they're less specialised: a framework serves one domain, while the patterns fit nearly any.

@chapter A weather service
@art spread-calls
Now the count. A garden irrigation controller reads a commercial weather service. In the spread design, four classes in three modules call the service's web interface themselves. That's causes three and four at once.

@math heading="Spread" items="new provider: 3 modules@new provider;;hourly forecast: 2@hourly forecast;;3 + 2 + 1 + 1 = 7 module touches@seven;;2 of 4 changes confined@two of the four"
Four change requests come in. A new provider touches three modules, and an hourly forecast touches two. A frost threshold and a new valve touch one each. That's seven module touches, and two of the four changes stay inside one module.

@code block=2 lines=2-19 focus="2-4@an interface of its own|7@one class|16-19@web interface"
In the encapsulated design, the controller has an interface of its own, WeatherSource. One class, in a new weather module, knows the vendor's web interface and its units.

@math heading="Encapsulated" items="new provider: 1 module@changing vendors;;hourly forecast: 3 modules@three modules;;1 + 3 + 1 + 1 = 6@six"
Now changing vendors touches one module, so three changes are confined and the total falls to six. But an hourly forecast changes what the interface offers. It reaches the weather module and every module that uses the new forecast: three modules, one more than before.

@art interface-boundary
That's the word particular, as a number. The interface makes the design robust to a new vendor, not to a new kind of forecast.

@chapter Where people slip
@list heading="Common slips" items="Expecting robustness to every change@The first|Treating frameworks and patterns as the same@The second|Giving everything the same flexibility@And the third"
The first slip is expecting a pattern to make a design robust to every change. The second is treating frameworks and patterns as the same thing. And the third is giving every kind of software the same amount of flexibility, when a framework needs far more than an application.

@chapter Try it
@words text="A vending machine" sub="payment behind an interface, card reader added"
Your turn. A vending machine has three change requests: card payments, a new coin and a restock alert. Count the modules each touches before and after payment goes behind an interface, and name the cause of redesign the interface addresses.

@end text="Count the module touches"
Then check your counts in the lab, on Learn. That's learn dot get er done dot I O.
