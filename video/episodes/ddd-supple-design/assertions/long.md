---
format: long
lesson: ddd-supple-design/assertions
title: Assertions: use a command without tracing it
thumb: Trust the guarantee
---

@chapter Commands still hide things
@title text="Assertions" sub="Domain-Driven Design, Chapter 10" art=thumb
Side effect free functions cut the problem down, but they leave commands on the entities. Anyone calling those commands still has to understand their consequences.

@art nested-commands
A command with no complex computation can be read by inspection. But in a design built from smaller parts, a command calls other commands, and the caller has to understand each of them. That defeats encapsulation.

@art two-implementations
And an interface doesn't restrict side effects. Two classes implementing it can change different things, which defeats the point of abstraction and polymorphism. When effects are defined only by the code, the only way to understand the program is to trace execution along its branches.

@chapter Design by contract
@list heading="After Meyer, 1988" items="Post-condition: the guaranteed outcome@A post condition|Precondition: what must hold first@A precondition|Invariant: true after every operation@an invariant"
Evans turns to design by contract, from Bertrand Meyer's book of nineteen eighty eight. A post condition describes the guaranteed outcome of a call, side effects included. A precondition is what must hold for that guarantee. And an invariant is true of an object whenever any operation finishes. It can even cover a whole Aggregate.

@quote text="If you trust the guarantee of a post-condition, you don't have to worry about how a method works." cite="Evans, Domain-Driven Design, Chapter 10"
All of these describe state, not procedure, which is why they're easier to analyse. The effects of delegation are already folded in. If you trust the guarantee of a post condition, you don't have to worry about how a method works.

@art test-shape
Where the language can't express assertions, check them with automated tests. Because they're about state, the tests are easy to write. Set up the preconditions, run the operation, check the post conditions.

@chapter A bike share
@code block=1 lines=1-9 focus="1-3@two docks together|4@Every dock|5@precondition|6-8@the method"
Here's a command written for the lesson, from a bike share scheme that moves bikes between docks. The comment states the post condition: the two docks together hold as many bikes as before. Every dock holds between zero and its capacity. And the precondition says n fits in both. Then the method itself, two lines.

@code block=2 lines=1-6 focus="2-3@capacity twelve|4@sends three|5-6@a holds five"
The test does exactly what Evans describes. Dock a has capacity twelve, holding eight. Dock b has capacity ten, holding five. A sends three bikes to b. Then a holds five and b holds eight.

@chapter Checking clause by clause
@code block=3 lines=1-1 focus="1@one specification"
The lab writes the assertions as one specification. Removed is three, added is three, a's bikes are at least zero, and b's spaces are at least zero. The first two are the post condition. The last two are the invariants that could break.

@math heading="a.sendBikesTo(b, 3)" items="transfer-kept: 4 of 4 hold@every clause holds;;transfer-overfull: toSpaces = −1, first false: toSpaces ≥ 0@only two spaces;;transfer-one-sided: removed = 0, first false: removed = 3@forgot the first line"
In transfer kept, every clause holds, four of four. In transfer overfull, b started with only two spaces, so its spaces end at minus one, and the invariant is broken. In transfer one sided, an implementation forgot the first line, so removed is zero. Bikes have been created out of nothing.

@art whose-fault
Look at the overfull case. The operation did what it promised. The caller broke the precondition that n fit in b. That's the fine print doing its work: it says whose fault the broken invariant is. And in the one sided case, only the stated post condition notices. Nothing in the method's name would have.

@chapter When an assertion looks odd
@art paint-split
The book's example returns to paint. Mixing one paint into another adds the second's volume and leaves the second unchanged, which fits nobody's idea of paint. Emptying it breaks a requirement. So Evans reads the awkwardness as a missing concept, and splits the class until the assertions become common sense.

@words text="Seek assertions people could guess"
His caution is about people. Any consistent set of assertions would serve a compiler. But developers extrapolate from the concepts of the model, so look for a model whose assertions they could have guessed.

@chapter Where people slip
@list heading="Common slips" items="Needing a language that checks them@The first|Bending the code to match intuition@The second|Reading satisfied assertions as proof@And the third"
The first slip is thinking assertions need a language that checks them. Unit tests stand in. The second is fixing an awkward post condition by bending the code to match intuition, which in the paint case broke a requirement. And the third is reading satisfied assertions as proof. A transfer that also cleared a dock's maintenance flag would pass all four clauses.

@chapter Try it
@code block=4 lines=1-6 focus="2@post condition|3@invariant|4-6@three states"
Your turn. A seed bank's vault holds a hundred packets and must be flagged for reordering whenever fewer than thirty are left. After withdrawing eighty, here's the post condition and the invariant, and three states. For each one, say whether the assertions hold, and if not, the first false clause.

@end text="State it, then check it"
Type the three states into the lab to check, on Learn. That's learn dot get er done dot I O.
