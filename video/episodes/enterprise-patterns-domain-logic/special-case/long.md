---
format: long
lesson: enterprise-patterns-domain-logic/special-case
title: Special Case: stop returning null
thumb: Return a guest, not null
---

@chapter The trouble with null
@title text="Special Case" sub="Patterns of Enterprise Application Architecture, Chapter 18" art=thumb
You ask for a customer, and there isn't one, so you get null. Fowler's Special Case pattern is about what to return instead, and why it saves you writing the same check over and over.

@art null-hole
His starting point is that nulls defeat polymorphism. Normally you can call a method on a variable without caring which subclass it holds. But if it can be null, the call fails at run time, and, as he notes, you get a stack trace for your trouble.

@art repeated-checks
So every caller that might see a null has to test for it. And since the right response is often the same in many places, the same test gets written in many places. That's duplication, and Fowler counts it a sin.

@chapter The pattern
@quote text="Instead of returning null, or some odd value, return a Special Case that has the same interface as what the caller expects." cite="Fowler, Patterns of Enterprise Application Architecture, Chapter 18"
Here's the pattern in one sentence. Instead of returning null, or some odd value, return a Special Case that has the same interface as what the caller expects.

@art stand-in
How it works is short. Make a subclass for the special case. Override all its methods to give harmless behaviour. And put an instance of it wherever a null would have been.

@art shared-flyweight
There's usually no reason to tell one instance from another, so a special case can often be a flyweight, one shared instance, unless it gathers state of its own. And its methods often return other special cases, so what an unknown customer owes is itself unknown.

@chapter The count
@code block=1 lines=1-11 label=Java focus="3@missing customer|7@or plan"
Here's a greeting that copes with a missing customer, and with a customer whose name or plan is missing, by guarding every call.

@math heading="null-checks" items="1 + if 2 + && 2 = 5@one, plus two;;nesting 1, from line 4@deepest nesting"
The lab counts its decision points: one, plus two ifs, plus two ands. That's five. The deepest nesting is one, first reached at line four. Each and is there only so the call after it doesn't land on a null.

@code block=2 lines=1-9 label=Java focus="2-5@GuestCustomer|7-9@asks its questions"
Now the finder returns a GuestCustomer instead of null. Its name is friend, and its plan is the basic one. The greeting just asks its questions directly. The count falls to one, and the greeting never names GuestCustomer.

@art finder-gate
Only one place now decides there's no customer: the finder that returns the guest. The decision left every caller, because the answer was the same wherever the question was asked.

@chapter Be honest about it
@art two-specials
There's a catch. The rewrite assumes a real customer always has a name and a plan. The original also guarded against a known customer with no name, and GuestCustomer doesn't cover that. That's Fowler's point that a null can mean different things, like no customer at all, or one nobody has identified. He suggests separate special cases for each.

@chapter When to use it
@words text="IEEE 754: ∞ and NaN" sub="special values instead of an exception"
Fowler finds a good example outside business code: IEEE floating point. Its infinities and not a number are special values that a division by zero can return instead of raising an exception, and they then take part in arithmetic like any other number.

@words text="Same response, many places"
Use a Special Case wherever several places respond alike once a test has found one particular instance, or a null. Fowler files Bobby Woolf's Null Object as a special case of Special Case, pardoning the pun. And a caller that does need to know can still ask, with an isNull method.

@chapter Where people slip
@list heading="Common slips" items="It hides errors@The first|Every caller must know about it@The second|One null object for every meaning@And the third"
The first slip is thinking a Special Case hides errors. A null that means a bug should still fail loudly. That's not this pattern's case. The second is thinking every caller has to know about it. Only the finder does. And the third is using one null object for every meaning of null.

@chapter Try it
@code block=3 lines=1-11 label=Java focus="4@city|7@postcode"
Your turn. This label routine copes with a missing address, its city and its postcode. Count its decision points with the breakdown. Then write a special case for the missing address, and the routine as it would read once the finder returns it.

@end text="Give it a guest yourself"
You can paste a routine into the lab and watch its null checks disappear, on Learn. That's learn dot get er done dot I O.
