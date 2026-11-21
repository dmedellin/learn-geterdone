---
format: long
lesson: accelerate-technical-practices/deployability-and-testability
title: It's not the system type, it's the coupling
thumb: Test alone, deploy alone
---

@chapter Does it work on a mainframe?
@title text="Types of Systems and Deployability" sub="Accelerate, Chapter 5" art=thumb
Continuous delivery began in web systems. So can it work on mainframes, on firmware, on the tangle of thousands of tightly coupled systems found in many enterprises? Chapter five starts there.

@quote text="We found that high performance is possible with all kinds of systems, provided that systems—and the teams that build and maintain them—are loosely coupled." cite="Forsgren, Humble and Kim, Accelerate, Chapter 5"
Here's the answer. We found that high performance is possible with all kinds of systems, provided that systems, and the teams that build and maintain them, are loosely coupled.

@chapter Searching for a pattern
@art system-types
The survey asked about eleven kinds of system, from new systems not yet released to systems of record, packaged software, embedded software and mainframes. Both as the main system a team develops, and as a service it integrates against.

@list heading="Low performers more likely to report" items="Custom software written by another company@another company|Mainframe systems@mainframe"
Low performers were more likely to say their software was custom software written by another company, such as an outsourcing partner, and more likely to work on mainframes. Integrating against a mainframe wasn't significantly correlated with performance.

@words text="All other kinds: no significant correlation"
For all the other kinds, there was no significant correlation. The authors were surprised. They'd expected packaged software, systems of record and embedded systems to do worse, and new systems to do better.

@art bring-in-house
So it's the architecture's characteristics that count, not the implementation. And since delivery affects organizational performance, they add, the capability to build core, strategic products should be brought in house.

@chapter Two properties that mattered
@list heading="More common among high performers" items="Testability: test without an integrated environment@test most of their work|Deployability: release without lock-step@release on their own"
Two properties were more common among high performers. Teams could test most of their work without a shared integrated environment. And they could release on their own, without lock step with the services they use. Testability and deployability.

@art loose-coupling
Both follow from loose coupling: systems that can be changed and validated independently. In twenty seventeen, a loosely coupled, well encapsulated architecture was the biggest contributor to continuous delivery, bigger than test and deployment automation.

@words text="Change · test · deploy without waiting for other teams"
It was gauged by questions like these. Can a team change its design, test and deploy without asking or waiting for other teams? And can it deploy in working hours without an outage?

@art fake-services
Service oriented architecture and microservices are supposed to deliver this. But in practice, many so called service oriented architectures don't let services be tested and deployed independently, and won't lift performance.

@chapter Release groups
@art release-groups
Now the count. The lab takes a list of components, and a list of ties, pairs that must be released together, and finds the release groups. A group is a set where you can walk from any component to any other along ties.

@math heading="An invented shop" items="cart–checkout · cart–pricing · checkout–payments · pricing–catalog · catalog–search@five ties;;group: cart, checkout, payments, pricing, catalog, search = 6@a group of six;;email · reviews: alone@email and reviews;;3 groups · largest 6 · alone 2@three groups"
An invented shop has eight services and five ties. Follow them and you get a group of six: cart, checkout, payments, pricing, catalog and search. Then email and reviews, with no ties at all. So three groups, the largest six, and two services that can be released alone.

@chapter Cut one tie
@art cut-tie
Now take away one tie and see what it buys. In a real system that might mean giving two services their own databases, or their own release calendars.

@math heading="Remove cart–pricing" items="cart, checkout, payments = 3@cart, checkout and payments;;pricing, catalog, search = 3@pricing, catalog and search;;4 groups · largest 3 · alone still 2@still two"
Remove the tie between cart and pricing. Now cart, checkout and payments are one group, and pricing, catalog and search another. Four groups, the largest three. But the number deployable alone is still two. Halving the biggest group freed nobody to ship alone.

@words text="Ledger: 3 groups · 2 alone · largest 3"
A second preset is a bank's mainframe ledger and four other services. The ledger has no tie, so it can be released alone. That's only an illustration of what the chapter says, not evidence.

@chapter Where people slip
@list heading="Common slips" items="System type predicts performance@The first|Microservices equal loose coupling@The second|Legacy systems can't perform@the third"
The first slip is expecting the kind of system to predict performance. The second is treating microservices as the same thing as loose coupling. And the third is concluding legacy systems can't perform.

@chapter Try it
@words text="booking–reminders · reminders–notes · billing–labs"
Your turn. A clinic has booking, notes, billing, reminders and labs, with three ties. Find the release groups, how many can be released alone, and the largest group. Then pick a tie whose removal shrinks the largest group.

@end text="Find your release groups"
You can type in your own services and ties and find the groups, on Learn. That's learn dot get er done dot I O.
