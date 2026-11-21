---
format: long
lesson: ddd-building-blocks/the-smart-ui-anti-pattern
title: The Smart UI: when putting the logic in the screen is right
thumb: A fork, not a starting point
---

@chapter A fair hearing
@title text="The Smart UI Anti-Pattern" sub="Domain-Driven Design, Chapter 4" art=thumb
Evans has just argued for layers. Then he does something unusual: he gives the opposite approach a fair hearing, and says when it's the right choice.

@art simple-project
Picture a project with simple functions, mostly entering and displaying data, few business rules, and a team that isn't made of experienced object modellers. Hand them a layered, model driven design, and they face new technology and the hard work of learning to model, while every simple task gets slower.

@words text="Cancelled before it shows what it can do"
Evans's guess is that such a project gets cancelled before it shows what the approach could do. And if it does finish, it's built a simple system nobody asked to be rich.

@chapter The prescription
@art screen-apps
So, for those circumstances only: let each screen be a small application that carries its own rules. Keep the shared data in a relational store. And build the screens with whatever tools generate them fastest. Evans calls this heresy against his own gospel.

@list heading="Advantages" items="High productivity at once@productivity|Little training needed@little training|Prototypes fix weak requirements@prototype|Independent small applications@independent|A screen can be rewritten safely@rewrite"
Then he lists the advantages honestly. Productivity is high at once. Developers with little training can work this way. A prototype in users' hands can make up for weak requirements. The small applications are independent. And a maintainer can rewrite a screen they don't understand, since its effects stay inside it.

@list heading="Disadvantages" items="Joined only through the database@only through the database|Every rule duplicated@duplicated|Nothing to refactor@nothing to refactor|Complexity overwhelms it@overwhelms"
The disadvantages are just as plain. Applications can be joined only through the database. Nothing is reused, so each rule is duplicated in every operation that needs it. Prototyping stops paying when there's nothing to refactor. And complexity overwhelms the design quickly.

@chapter A fork in the road
@quote text="But SMART UI is an alternate, mutually exclusive fork in the road, incompatible with the approach of domain-driven design." cite="Evans, Domain-Driven Design, Chapter 4"
What makes it a fork is that there's no migration. But smart UI is an alternate, mutually exclusive fork in the road, incompatible with the approach of domain driven design.

@art fork-road
You leave a Smart UI only by replacing whole applications. So a team that chooses it should pick tools made for it. And a team that means to build a model driven design must isolate the domain layer from its very first iteration.

@chapter Count the touches
@code block=1 lines=1-11 label=Java focus="3-7@works out the fare|8-10@saves it"
Here's a bike-share fare: a dollar, and fifty cents more for each started quarter hour past thirty minutes. In a Smart UI, the return screen works out the fare itself, then saves it and shows it. The ride history and the monthly bill each do the same.

@math heading="fare-in-every-screen" items="fare rule: 3 modules@fare rule;;bill layout: 1 module@layout;;member discount: 2 modules@discount;;6 touches · 1 change in one module@six module touches"
Three changes are listed. The fare rule touches three modules. The bill's layout touches one. And a member discount touches two. That's six module touches, with only one change confined to one module.

@code block=2 lines=1-13 label=Java focus="2-10@once|13@one line"
Now put the rule in the domain layer, once, in a class called Fare. Each screen keeps one line that calls it.

@art one-rule
So every screen asks the domain for the fare, and none of them works it out for itself.

@math heading="fare-in-the-domain" items="fare rule → Fare@edits Fare;;discount → Discount@edits Discount;;layout → the bill@the bill alone;;3 touches · 3 changes in one module@three module touches"
The same three changes. The fare rule edits Fare, the discount edits Discount, and the layout edits the bill alone. Three module touches, all three confined to one module.

@art rule-copies
Notice the layout change costs the same in both designs. That's the Smart UI's own advantage: a screen's changes stay in the screen. What it can't do is keep a rule in one place.

@art duplicated-growth
Three edits for one rule, and a fourth the day a new screen needs fares.

@words text="The lab counts edits. It doesn't know the team."
The lab counts edits. It doesn't know the team. And that's not Evans's verdict. For three screens and two rules, three edits may be cheaper than a domain layer the team must first learn to build.

@chapter Where people slip
@list heading="Common slips" items="Nobody should ever choose it@The first|Start smart, refactor later@The second|Every change gets expensive@And the third"
The first slip is thinking nobody should choose a Smart UI. Evans recommends it for simple work. The second is planning to start with one and refactor into a model later. There's no path. And the third is thinking it makes every change expensive. Only shared rules multiply.

@chapter Try it
@words text="CheckIn · Booking · Statement" sub="four changes, two designs"
Your turn. A gym has three screens and four changes. For the Smart UI and for the layered version, count the module touches, the changes confined to one module, and the largest change. Then say what the team would need to know before choosing.

@end text="Count the module touches"
Check your counts in the lab, on Learn. That's learn dot get er done dot I O.
