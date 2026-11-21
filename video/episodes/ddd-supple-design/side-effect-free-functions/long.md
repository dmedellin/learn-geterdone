---
format: long
lesson: ddd-supple-design/side-effect-free-functions
title: Side-Effect-Free Functions: calculate without changing anything
thumb: Return a new value
---

@chapter Commands and queries
@title text="Side-Effect-Free Functions" sub="Domain-Driven Design, Chapter 10" art=thumb
Evans starts with a division. Queries get information from the system, by reading a variable or computing from it. Commands, also called modifiers, change the system. Every operation is one or the other, or, too often, both.

@words text="Side effect" sub="a change that later operations will feel"
In computing, a side effect is any effect on state. Evans narrows it to a change that will affect operations that come later. Why borrow a word for unintended consequences? Because operations call operations, which call others, and a client can't foresee what the second and third tiers do.

@art call-tiers
So their effects become side effects in the everyday sense too. Once rules and calculations combine, the developer calling an operation has to understand its implementation and everything it delegates to. The interface's abstraction is worth very little.

@chapter Functions lower risk
@quote text="Place as much of the logic of the program as possible into functions, operations that return results with no observable side effects." cite="Evans, Domain-Driven Design, Chapter 10"
Here's the pattern's first sentence. Place as much of the logic of the program as possible into functions, operations that return results with no observable side effects.

@list heading="What a function gives you" items="The same answer every time@same value|Nesting to any depth@any depth|Easy testing@easier to test"
Called again, a function returns the same value. It can call other functions at any depth without worry. And it's far easier to test. So functions lower risk.

@chapter Two mitigations
@art split-command-query
Commands can't be avoided, so Evans offers two moves. First, after Bertrand Meyer, keep commands and queries in separate operations. A method that changes state returns no domain data, and is as simple as it can be. Every calculation happens in methods with no observable effect.

@art new-value
Second, look for a model where nothing existing needs to change at all, and answer with a new Value Object holding the result. A value can be made in answer to a question, handed on and forgotten. An entity can't, because its life cycle is closely controlled.

@chapter A shared dose
@code block=1 lines=1-15 focus="5@scale by|13@times"
Here's a clinic's dose, written two ways. The mutable one has scale by, which multiplies its milligrams in place. The value has times, which returns a new dose and changes nothing.

@art shared-dose
In the lab, four prescriptions hold doses. Anna, Ben and Cara share one value, five milligrams. Dev holds ten milligrams. The doctor doubles Ben's dose.

@math heading="Double Ben's dose" items="mutable: 3 holders · 3 see it · 2 surprised · 0 new@In place;;immutable: 3 holders · 1 sees it · 0 surprised · 1 new@as a value"
In place, with scale by: three holders of five milligrams, all three see the change, and two are surprised. Anna and Cara's doses doubled though nobody touched their prescriptions. No new values. Done as a value: three holders, one sees the change, nobody is surprised, and one new value is created, held by Ben.

@art twice-the-dose
Nothing that existed before was changed. Ben's prescription simply refers to a different value. The figures are the lesson's model, but in a real clinic, the surprise in the first case is a patient given twice the dose.

@chapter Splitting the entity
@code block=2 lines=1-9 focus="2-5@did both jobs|8@doubled|9@change dose to"
Evans sets an order of work. On an entity, first split the operation that both calculates and changes state, a refactoring from Fowler. Double and report did both jobs. Split, doubled is a function you can call as often as you like, to show the doctor what the new dose would be. And change dose to is a one line command that returns nothing.

@art paint-mix
After that, consider a second refactoring that moves the calculation into a value, which often removes the side effect altogether. In the book's paint example, colour becomes an immutable value, mixing returns a new colour, and the entity's command shrinks to a few lines.

@chapter Where people slip
@list heading="Common slips" items="A design of functions alone@The first|Separation is the whole pattern@The second|Making entities immutable too@And the third"
The first slip is believing a design can be made of functions alone. Evans says commands can't be avoided. The second is thinking that separating commands from queries is the whole pattern. Moving the calculation into a value is what took the surprised holders from two to zero. And the third is making entities immutable too. The prescription keeps its identity. Its dose is the value.

@chapter Try it
@code block=3 lines=1-8 focus="1-2@morning and noon|3-7@Five orders|8@extended in place"
Your turn. A bakery with pickup windows, morning and noon. Five orders hold them, and order b's window is extended in place. Find the holders of the changed value, how many see the change, and how many are surprised. Then make Window immutable, give b alone an extended window, and count again, with the new values.

@end text="Change one, surprise none"
Type both versions into the lab to check, on Learn. That's learn dot get er done dot I O.
