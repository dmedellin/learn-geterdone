---
format: long
lesson: code-complete-high-quality-code/inheritance-containment-and-members
title: Contain before you inherit, and keep the tree shallow
thumb: Has a, before is a
---

@chapter The question
@title text="Inheritance, Containment and Members" sub="Code Complete, chapter 6" art=thumb
Once a class has an interface, how do you build what's behind it? Do you hold other classes, or extend them? Chapter six has a clear lean.

@quote text="Containment is usually preferable to inheritance unless you’re modeling an ‘is a’ relationship." cite="McConnell, Code Complete, 2nd ed., Chapter 6, p. 160"
Here's the key point. Containment is usually preferable to inheritance, unless you're modeling an is a relationship.

@chapter Has a
@art containment
Containment is a class holding another as a field. An employee has a name, has an address. The book calls it the workhorse. More gets written about inheritance, McConnell says, because inheritance is trickier and more error prone, not because it's better.

@chapter Is a
@art inheritance-tree
Inheritance means is a. The new class is a more specialised version of the old one, and it must keep the contract the old one sets.

@quote text="Design and document for inheritance, or prohibit it." cite="Joshua Bloch, as quoted in Code Complete, Section 6.3"
The book quotes Joshua Bloch. Design and document for inheritance, or prohibit it. In Java, the prohibition is the word final.

@words text="Usable through the parent, unnoticed" sub="Liskov, 1988"
Then comes the principle with a person behind it. In nineteen eighty eight, Barbara Liskov argued that a class should inherit from another only if it truly is a more specific version of it. A subclass must be usable through its parent's interface, without the caller knowing the difference.

@art flipped-sign
The book's example is an account whose interest routine returns a rate with the opposite sign from its parent's. It compiles. But every caller would now have to know which kind of account it held.

@chapter Keep it shallow
@list heading="More rules" items="Move common things as high as you can@as high|Suspect a base with one child@one derived class|Suspect an override that does nothing@does nothing|Keep hierarchies shallow@shallow"
More rules follow. Move common interface, data and behaviour as high as abstraction allows. Be suspicious of a base class with only one derived class, and of an override that does nothing. And keep hierarchies shallow.

@words text="Two or three levels" sub="Riel's six: “grossly optimistic”"
How shallow? Riel suggests a limit of six levels. McConnell calls that grossly optimistic. Most people have trouble juggling more than two or three, and deep trees have been associated with higher fault rates.

@art chainsaw
If inheritance is a chain saw, he adds, multiple inheritance is a nineteen fifties chain saw with no blade guard. His summary is a heavy bias against inheritance. Contain when classes share only data. Inherit when they share behaviour.

@chapter Measure a hierarchy
@art shallow-tree
The lesson's lab measures a hierarchy's depth, with the root at level one. A shallow tree, Circle, Square and Triangle under Shape, has depth two. Four classes, and three leaves, classes nothing extends.

@art deep-chain
Now take a chain of accounts, from Record at the top down to Christmas Holiday Savings, with Checking Account off to one side.

@math heading="The deep preset" items="Record 1 · Account 2 · DepositAccount 3@Record is one;;SavingsAccount 4 · CheckingAccount 4@Savings Account;;BonusSavings 5 · HolidayBonusSavings 6@Bonus Savings;;ChristmasHolidaySavings 7: the depth@Christmas"
Record is one, Account two, Deposit Account three. Savings Account and Checking Account are both four. Bonus Savings is five, Holiday Bonus Savings six. And Christmas Holiday Savings is seven, the depth. Eight classes, two leaves.

@words text="7 places to look for one call"
Read seven against McConnell's two or three, not Riel's six. To know what one call on the deepest class does, you may have to open all seven, because any level above could define or override it.

@chapter Members and classes
@list heading="Members and constructors" items="Keep routines few@small|The Law of Demeter@Demeter|Initialise everything in every constructor@every constructor|Prefer deep copies@deep copies"
On members, keep the number of routines small. Follow the Law of Demeter: call routines on the objects you hold, not on the objects they return. Initialise all member data in every constructor. And prefer deep copies to shallow ones, until shown otherwise. And why create a class at all? The single most important reason is to reduce complexity.

@chapter Where people slip
@list heading="Common slips" items="Inheriting just to reuse code@The first|Thinking a subclass that compiles can stand in@The second|Allowing deep trees because each level is small@the third"
The first slip is treating inheritance as the main way to reuse code. That's what containment is for. The second is thinking a subclass that compiles can stand in for its parent. The compiler checks names, not meaning. And the third is allowing deep trees because each level is small.

@chapter Try it
@code block=1 lines=1-18 label=Java focus="4-6@width and a height|10-13@sets both sides|14-17@height"
Your turn. Here's a Rectangle with a width and a height, and a Square that extends it. Its set width sets both sides, and so does its set height. Can Square stand in for Rectangle? Name a caller of Rectangle it would break, and say what that caller gets.

@end text="Measure your own hierarchy"
You can type a hierarchy into the lab and measure its depth, on Learn. That's learn dot get er done dot I O.
