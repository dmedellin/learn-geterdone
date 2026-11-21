---
format: long
lesson: enterprise-patterns-distribution/distribution-strategies
title: Fowler's First Law: don't distribute your objects
thumb: Cluster, don't split by class
---

@chapter The allure
@title text="Distribution Strategies" sub="Patterns of Enterprise Application Architecture, Chapter 7" art=thumb
Fowler says he was shown this design again and again in design reviews. It looks like good engineering. His chapter argues that it's the opposite.

@art by-class-nodes
An ordering system is split by kind of object. One remote component for customers, another for orders, and so on, each on a machine of its own. The reason given is performance: if one component gets busy, give it more boxes.

@words text="Transparency" sub="it hides where the callee is, not what the call costs"
The vendors' promise behind it is transparency: an object can call another without knowing whether it's local or remote. Fowler grants transparency its value, but not speed. The cost of a call is the one thing middleware can't hide.

@chapter Remote and local
@art remote-call-cost
Here's why. A call inside your own process costs almost nothing. A call between two processes is orders of magnitude slower, and another machine slower again.

@art fine-vs-coarse
So a remote interface has to be different. Locally, fine grained is best: an address with separate methods for the city, the state and the rest. Remotely, you want the city, state and postcode in one call. And any object that might be remote needs that awkward coarse interface. One class can't be both.

@code block=1 lines=1-6 label=Java focus="2@extends Java's Remote|3-5@three methods"
Here's the mistake in six lines. RemoteCustomer extends Java's Remote, so each of its three methods is a call across the network. A screen showing a customer's name, city and credit makes three round trips where one would do. Locally, those three getters would be exactly right.

@chapter The law
@quote text="Hence, we get to my First Law of Distributed Object Design: Don't distribute your objects!" cite="Fowler, Patterns of Enterprise Application Architecture, Chapter 7"
Hence, we get to my First Law of Distributed Object Design: Don't distribute your objects!

@art clustering
The alternative is clustering. Keep the whole application in one process, and run copies of it on each machine. Every call inside a copy is local, every class keeps its fine grained interface, and the load is spread by the number of copies, not by the class of object.

@chapter Count the cost
@math heading="by-class: four classes, four nodes" items="screen→order 20 · order→customer 10 · product 30 · pricing 15@twenty times;;calls: 75, all remote@seventy five;;75 × 1,000 µs = 75,000 µs@seventy five thousand;;one node: 75 × 1 µs = 75 µs · 1,000×@one node"
The lab prices one design. A screen calls an order twenty times. The order calls a customer ten times, a product thirty, and a pricing object fifteen. Each is on its own node. That's seventy five calls, all remote. At a thousand microseconds each, seventy five thousand. On one node, at one microsecond, seventy five. A thousand times slower.

@words text="The ratio is illustrative" sub="Fowler's point survives any ratio much above one"
That thousand to one is an illustrative ratio, standing in for Fowler's orders of magnitude. On your own machines, the ratio is whatever you measure. But his point survives any ratio much above one.

@chapter Where you must
@art unavoidable-boundaries
There are limits to clustering. Fowler's advice is to fight like a cornered rat to remove process boundaries, knowing you won't remove them all. Client and server. The application server and the database. Often the web tier and the application tier. A vendor's package. And now and then, a split in the application server itself.

@art boundary-facade
Where a boundary stays, keep fine grained objects inside the process, and put coarse grained objects on the boundary, whose only job is to be a remote interface. That's Remote Facade, with Data Transfer Object to carry the data, the next two lessons.

@words text="XML over HTTP · a direct remote call" sub="XML web services only when nothing more direct will do"
And across that boundary, what kind of interface? XML over HTTP carries a lot of structured data in one round trip, and crosses platforms and firewalls, but it adds a burden to each call. So Fowler would reach for XML web services only when nothing more direct will do.

@chapter Where people slip
@list heading="Common slips" items="Distributing by class spreads the load@The first|A remote call is a slower local call@The second|Transparent middleware removes the cost@And the third"
The first slip is thinking distribution by class spreads the load. It spreads the cost of calls. The second is treating a remote call as a slower local call. It changes the interface. And the third is trusting transparent middleware. It hides where the callee is, not what the call costs.

@chapter Try it
@list heading="Your design" items="web→cart 12 · cart→stock 8 · cart→tax 8 · tax→rates 16@twelve|web on front · tax, rates on back · cart, stock on main@front node|remote 800 µs · local 2 µs@eight hundred"
Your turn. Web calls cart twelve times. Cart calls stock eight, and tax eight. Tax calls rates sixteen. Web is on a front node, tax and rates on a back node, cart and stock on main. A remote call is eight hundred microseconds, a local one two. Find the totals, and which pair stays local away from main.

@end text="Move a class, watch the cost"
You can move classes between nodes and watch which calls cross, on Learn. That's learn dot get er done dot I O.
