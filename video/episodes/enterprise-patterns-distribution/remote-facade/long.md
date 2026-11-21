---
format: long
lesson: enterprise-patterns-distribution/remote-facade
title: Remote Facade: one remote call, many local ones
thumb: Remove the waits, not the work
---

@chapter The problem
@title text="Remote Facade" sub="Patterns of Enterprise Application Architecture, Chapter 15" art=thumb
The last lesson ended at the boundaries you can't remove. This one reads the pattern Fowler puts on them.

@art chatty-client
An object model works best with small objects and small methods, which means many calls. Between processes, each call is expensive. Data is marshalled, security may be checked, packets routed. So anything used remotely needs a coarse grained interface, and that seems to wreck the whole object structure.

@chapter The facade
@art tangle-behind-facade
Remote Facade keeps both. It puts one coarse grained object in front of a tangle of small ones, which stay purely local. In the simplest case, it replaces an address's getters and setters with one bulk getter and one bulk setter, which call the real accessors and do nothing more.

@art one-call-many
More often, one facade has many methods, each passing on data from several objects. Fowler prefers few facades with many methods, even a single one for a moderate application. A facade is shaped for one client's usage, typically a family of screens.

@quote text="Remote Facade has no domain logic." cite="Fowler, Patterns of Enterprise Application Architecture, Chapter 15"
And it must stay thin. Fowler asks you to repeat a sentence three times. Here it is once. Remote Facade has no domain logic.

@art thin-layer
Workflow goes in the fine grained objects, or in a Transaction Script that isn't remote. The application should still run, whole, in one process, with no facade at all. The facade's methods are a natural place for security and transactions: start one, do the work, commit before returning.

@chapter The code
@code block=1 lines=1-16 label=Java focus="9@calls moveHouse|10@finds the customer|11-13@sets the three parts|14@saves"
Here's one facade method. A remote client calls moveHouse once, with the new street, city and postcode. Inside the server, the facade finds the customer, sets the three parts of the address one by one, and saves. Nothing in it decides anything. If a postcode must match its city, that rule belongs to the address.

@chapter Count the waits
@math heading="move-house: 20 ms latency, 0.5 ms work" items="fine: 11 trips · 451/2 = 225.50 ms@eleven round trips;;waiting: 40/41 ≈ 97.6%@ninety seven point six"
The lab's preset has two facade methods, doing the work of five fine grained calls and six. At twenty milliseconds of latency and half a millisecond of work, the fine grained client makes eleven round trips. That takes two hundred and twenty five point five milliseconds, and ninety seven point six percent of it is waiting.

@math heading="move-house, through the facade" items="facade: 2 trips · 91/2 = 45.50 ms@makes two;;speed-up: 451/91 ≈ 5.0×@about five"
The facade makes two round trips, and takes forty five point five milliseconds. That's about five times faster, for the same work.

@math heading="on-a-fast-network: 1 ms latency" items="fine: 33/2 = 16.50 ms · 2/3 ≈ 66.7% waiting@sixteen point five;;facade: 15/2 = 7.50 ms@seven point five;;speed-up: 11/5 ≈ 2.2×@two point two"
Cut the latency to one millisecond. Now the fine grained calls take sixteen point five milliseconds, two thirds of it waiting. The facade takes seven point five. The speed-up is two point two.

@art waiting-vs-working
The facade removes waits, not work. So it saves most where the waits are most of the time. As the latency falls, the saving shrinks, but it doesn't vanish.

@chapter When to use it
@quote text="Use Remote Facade whenever you need remote access to a fine-grained object model." cite="Fowler, Patterns of Enterprise Application Architecture, Chapter 15, When to Use It"
Here's the rule. Use Remote Facade whenever you need remote access to a fine grained object model. Its usual place is between a user interface and a Domain Model in different processes.

@art two-processes-one-box
A shared machine isn't an exemption. Two processes on one box pay enough per call to need a coarse interface too. Within one process, you don't need it. And it's not usually used with a Transaction Script, which is coarse grained already.

@chapter Where people slip
@list heading="Common slips" items="Business logic in the facade@The first|Coarse domain objects@The second|Facades only between machines@And the third"
The first slip is putting business logic in the facade. Fowler calls it one of the biggest mistakes he sees. The second is making the domain objects themselves coarse, giving up what the fine grained model was for. And the third is thinking it matters only between machines. The line is the process.

@chapter Try it
@list heading="A trip-booking facade" items="bookTrip: 8 · cancelTrip: 3 · showTrip: 9@three methods|15 ms latency · 1 ms work@fifteen"
Your turn. A trip booking facade with three methods. bookTrip does the work of eight fine grained calls, cancelTrip of three, and showTrip of nine. The latency is fifteen milliseconds, with one of work per call. Find the round trips, both times, the speed-up, and the waiting share.

@end text="Change the latency yourself"
You can change the latency and watch the facade's saving move, on Learn. That's learn dot get er done dot I O.
