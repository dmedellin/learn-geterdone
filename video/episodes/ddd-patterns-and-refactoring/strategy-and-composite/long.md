---
format: long
lesson: ddd-patterns-and-refactoring/strategy-and-composite
title: Strategy and Composite: design patterns that name domain concepts
thumb: A pattern on two levels
---

@chapter Two levels at once
@title text="Strategy and Composite in the Model" sub="Domain-Driven Design, Chapter 12" art=thumb
Chapter twelve asks when a design pattern can also be a domain pattern. Most published patterns are technical: objects and classes that communicate, tailored to a recurring design problem. Some of them, not all, match concepts that turn up in many domains.

@art two-levels
To use one that way, you read it twice at once. As a technical pattern in the code, and as a conceptual pattern in the model.

@chapter Strategy, or Policy
@art tangled-alternatives
Domain processes often have more than one legitimate form. Once the alternatives are written into the process, choosing among them tangles with the alternatives themselves, and the real options disappear into the rest of the behaviour.

@art policy-objects
Evans's remedy is to make the variable part an object of the model, kept apart from the process it steers, with one object for each way the process can go. The design pattern stresses swapping one algorithm for another. The domain pattern stresses expressing a concept, most often a policy.

@words text="Quickest, or least costly?" sub="a policy that scores each leg"
His example is a shipping route service, tuned to find the quickest or the least costly route, with that choice tested inside every computation. Pass in a policy that scores each leg, and the service treats every request the same way. New policies need no change to it.

@chapter Counting the decisions
@code block=1 lines=1-20 focus="3@member and the ride|6@member|9@student|16@member or student"
Now a bike share's ride pricing. Two methods, the fare and the deposit, each testing the rider's plan. Is the rider a member and the ride short? A member? A student? And for the deposit, a member or student?

@math heading="plan-tests" items="1 + if 4 + && 1 + || 1 = 7@seven;;5 of 6 decisions ask about the plan@Five of the six"
The lab counts decision points: one, plus one for each if, loop, case, and, and or. Here that's seven. Five of the six decisions ask which plan the rider is on. The and on line three asks about the ride. And a new plan would add a test to both methods.

@code block=2 lines=1-20 focus="2-5@pricing policy|6-9@casual|10-13@student|14-20@member"
Now the same prices as interchangeable policies. One pricing policy interface, with a fare and a deposit. A casual policy, a student policy, and a member policy. Every plan still gets the same prices.

@math heading="pricing-policies" items="1 + if 1 = 2@two;;the test left: 45 free minutes@forty five free minutes"
The lab counts two. The one test left is the member's forty five free minutes, a rule within that policy, and of the domain.

@art choice-moved
But the question of which plan a rider is on hasn't vanished. It's answered once, where a ride is given its policy, in code outside the listing. What makes this a domain pattern is that a pricing plan is something riders and staff already talk about.

@chapter Composite
@art nested-programme
Composite is the second. Some domains nest things inside things of the same kind. When the model doesn't say so, behaviour is copied at each level, clients use a different interface for each one, and adding up across the hierarchy gets complicated.

@code block=3 lines=1-18 focus="2-4@one shared type|5-9@an act|10-17@a programme"
So give whole and part one shared type. Here's the lesson's festival programme. An act answers minutes from itself. A programme answers by adding up its parts, and a programme may hold programmes. A client asks the same question at any size.

@words text="Same behaviour at every level"
Designers often stop at the structure, Evans notes, when the power is the same behaviour at every level. And in his route example, before segments were needed, the plain model did fine. A design pattern earns its place when the need arrives.

@chapter Why not Flyweight?
@art flyweight-tiles
Flyweight shares a few values that are used many times. It's an implementation option for value objects, not entities, and it says nothing about the domain. Composite applies to the model and the implementation alike.

@quote text="The only requirement is that the pattern should say something about the conceptual domain, not just be a technical solution to a technical problem." cite="Evans, Domain-Driven Design, Chapter 12"
Evans won't list which design patterns qualify. He can't think of a domain use for Interpreter, and won't say there is none. The only requirement is that the pattern should say something about the conceptual domain, not just be a technical solution to a technical problem.

@chapter Where people slip
@list heading="Common slips" items="Using a pattern because it's convenient@The first|Thinking Strategy removes the decision@The second|Composite before the domain needs it@And the third"
The first slip is using a design pattern in the domain because it's convenient in code. The second is thinking a Strategy removes the decision. It moves it. And the third is adding a Composite before the domain needs one.

@chapter Try it
@code block=4 lines=1-17 focus="2-13@prices seats|15-16@refunds"
Your turn. A theatre prices seats and refunds by the booking's scheme: standard, concession or group. Count the decision points by the lab's rule, with the breakdown. Then sketch three scheme policies that give every booking the same price and refund, and count again.

@end text="Does it say something about the domain?"
Paste each into the lab to check, on Learn. That's learn dot get er done dot I O.
