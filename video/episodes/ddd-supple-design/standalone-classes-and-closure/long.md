---
format: long
lesson: ddd-supple-design/standalone-classes-and-closure
title: Standalone Classes and Closure of Operations
thumb: Depend on nothing extra
---

@chapter What a dependency costs
@title text="Standalone Classes and Closure" sub="Domain-Driven Design, Chapter 10" art=thumb
Evans counts the cost of a dependency in what a reader has to think about. Every association is one. So is the type of every argument, and every return value.

@art growing-web
With one dependency, you think about two classes and their relationship. With two, it's three classes, two relationships, and whatever relates the other two. And the things depended on have dependencies of their own. Modules and Aggregates help limit the web, but the difficulty grows quickly with each one added.

@quote text="Every dependency is suspect until proven basic to the concept behind the object." cite="Evans, Domain-Driven Design, Chapter 10"
So his rule is blunt. Every dependency is suspect until proven basic to the concept behind the object.

@chapter Hidden concepts count
@art hidden-colour
Implicit concepts count as much as explicit ones. Primitives, strings and collections are always in mind, and add nothing. But in the paint example, three public integers were really a colour. Making colour a class didn't add a concept. It showed one that was already there.

@list heading="Standalone, with care" items="Remove what isn't essential@isn't essential|Inside a module costs less@inside one module|Intricate work goes to a standalone class@hardest computations|Don't reduce everything to primitives@primitives"
So scrutinise each association, and remove what isn't essential. Evans qualifies this at once. Dependencies inside one module do less harm. Move the hardest computations into classes that stand alone, like value objects. And don't dumb a model down by reducing everything to primitives.

@chapter Closure of operations
@math heading="Closure" items="real × real → real@multiplying two;;Fare.plus(Fare) → Fare@returns the type"
That last point is where closure comes in. The real numbers are closed under multiplication: multiplying two of them never leaves the set. So where it fits, give an operation a result of the same type as its arguments. It returns the type it takes, counting the receiver as an argument.

@art closed-chain
Such an operation gives a high level interface without depending on any other concept, and closed operations are easy to chain. It's mostly a property of value objects, though asking an employee for a supervisor returns an employee. And halfway closure still helps, when the other type is a primitive.

@chapter A tangled fare
@code block=1 lines=1-13 focus="3@a ride, a rider and a membership|5@reaches through the ride|8-10@membership is active"
Now a bike share fare, written for the lesson. One class computes it from a ride, a rider and a membership. It reaches through the ride to compare zones. And if the membership is active, a quarter comes off.

@art tangled-calculator
That reach goes to the docks the ride started and ended at. So the calculator depends on Dock, and Dock appears in no signature.

@art dock-ripple
The lab follows a change to Dock. On the tangled design, two classes depend on it directly, the fare calculator and the ride, and three are reached in all, with the invoice two steps away.

@chapter Standing alone
@code block=2 lines=1-17 focus="2-3@long and int|5@plus|6-8@less percent|13-16@Tariff"
In the standalone design, the arithmetic lives in Fare, which depends on nothing but long and int. Plus is closed under Fare. Less percent is halfway, taking an int, which costs a reader almost nothing. And Tariff states the rule over plain numbers, and answers with a Fare. A billing service does the connecting.

@math heading="Who a change reaches" items="tangled, change Dock:  2 direct · 3 in all@tangled design;;standalone, change Dock:  1 direct · 2 in all@one class directly;;standalone, change Fare:  2 direct · 3 in all@Fare itself"
On the tangled design, a change to Dock reaches two classes directly and three in all. On the standalone one, it reaches one class directly, the ride, and two in all, the ride and billing. The fare rule is out of reach. And a change to Fare itself reaches two directly, invoice and tariff, and three in all.

@art value-holders
That's the shape of a value. Its holders depend on it, and it depends on none of them. Read it the other way, too. To understand the fare calculator you hold five concepts in mind. To understand Tariff, you need Fare. To understand Fare, nothing.

@chapter Where people slip
@list heading="Common slips" items="Stripping the interface to primitives@The first|Counting only the signatures@The second|Aiming at zero dependencies@And the third"
The first slip is making a class standalone by stripping its interface to primitives. Fare plus Fare is richer than long plus long. The second is counting only the types in a class's signatures. The calculator names no dock, yet a change to Dock reaches it. And the third is aiming at zero dependencies everywhere. The goal is to remove the inessential ones.

@chapter Try it
@code block=3 lines=1-4 focus="1@Loan|2@Fine|3@Notice|4@depend on no class"
Your turn. A library model. Loan depends on book, member and due date. Fine depends on loan and money. Notice depends on fine and member. The rest depend on no class of the model. Give every class Notice depends on, directly and in all, and name the standalone ones. Then follow a change to due date.

@end text="Cut what isn't basic"
Enter the edges in the lab to check, on Learn. That's learn dot get er done dot I O.
