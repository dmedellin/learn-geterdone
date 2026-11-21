---
format: long
lesson: gof-structural/facade
title: Facade: one simple front for a complicated subsystem
thumb: One door, not ten
---

@chapter Too many classes
@title text="Facade" sub="Design Patterns, chapter 4" art=thumb
A subsystem that's well divided into small classes is reusable, and hard to use. Facade is the Gang of Four's answer to that, and it's simpler, and less strict, than people often think.

@quote text="Provide a unified interface to a set of interfaces in a subsystem." cite="Gamma, Helm, Johnson and Vlissides, Design Patterns, Chapter 4"
That's the first sentence of the intent. Provide a unified interface to a set of interfaces in a subsystem. The second says the facade works a level above them, so the subsystem is simpler to work with.

@words text="Subsystems should rely on each other as little as possible"
The argument starts from an observation. Dividing a system into subsystems reduces complexity, and a common aim is then to have subsystems talk to, and rely on, each other as little as possible.

@chapter The compiler
@art compiler-parts
The book's example is a compiler subsystem: a scanner, a parser, parse tree classes, a bytecode stream and a builder. A few specialised tools need those classes directly. Most clients just want their code compiled.

@art facade-front
So the subsystem also offers a compiler class that does the common thing in one call. The subsystem's classes do the actual work, and know nothing of the facade. Clients that use it need not touch them at all.

@chapter The code
@code block=1 lines=1-20 label=Java focus="3-6@four subsystem classes|13-19@deposit"
Here's the lesson's parcel locker. The facade, called lockers, holds four subsystem classes: the locker bank, the door controller, the pin generator and the text message gateway. A courier calls deposit, and the facade finds a free locker, opens its door, issues a pin, and texts it to the customer. One call, four classes.

@chapter Three benefits
@list heading="Consequences" items="Shields clients from components@shields clients|Promotes weak coupling@weak coupling|Doesn't stop direct use@doesn't stop"
The consequences are three benefits. The facade shields clients from the subsystem's components, so they deal with fewer objects. It promotes weak coupling, so the classes behind it can change without clients noticing. And it doesn't stop applications using the subsystem's classes when they need to.

@art direct-still
That third one is often missed. A facade doesn't hide the subsystem. Each client can trade simplicity for the full set of options, and look past the facade when it needs to.

@chapter Count it
@art tangled-clients
Now the lab. The subsystem has five classes, the four you saw plus a ledger. Three applications use it: the courier's app, the kiosk at the lockers, and the support desk. Going straight in, there are eight classes and twelve distinct uses.

@math heading="Uses across the boundary" items="direct: 4 + 3 + 3 = 10@four plus three plus three;;direct total: 10 + 2 = 12@ten plus two;;facade: 3 clients → Lockers, desk → Ledger: 4@through the facade;;facade total: 4 + 4 + 2 = 10@four plus four plus two"
The courier uses four classes, the kiosk three, the desk three: four plus three plus three is ten crossing uses. Plus the subsystem's own two, ten plus two, twelve. Now through the facade. All three clients use lockers, and the desk still reads the ledger, which is four. The facade's own four uses, and the two inside: four plus four plus two, ten.

@words text="Crossing the boundary: 10 → 4" sub="one more class · fan-out moves to the facade"
So the uses that cross the boundary fall from ten to four, for one more class. The subsystem can now change behind lockers, and only the desk's one direct use goes with it.

@chapter Where people slip
@list heading="Common slips" items="Thinking it hides the subsystem@The first|Expecting it to fix inner coupling@The second|Giving it every option@And the third"
The first slip is thinking a facade hides the subsystem. It doesn't. The second is expecting it to remove the subsystem's own coupling. It only changes the uses that cross the boundary. And the third is giving the facade every option the subsystem has.

@art bloated-facade
That last one defeats the point. A facade that takes on every client's special case grows into the subsystem's whole interface again. The authors' own sample code ends on that trade off: a parameter or two can earn its place, but not every participant.

@art layers
One more use. In a layered system, a facade can be each layer's entry point. And the book notes that, unlike a mediator, whose colleagues talk to it, the subsystem classes don't even know a facade exists. It's often a Singleton.

@chapter Try it
@words text="The desk goes through Lockers too"
Your turn. Change the support desk to read the ledger through lockers as well. By hand, give the classes, the distinct uses, the uses that cross into the subsystem, and the facade's fan out.

@end text="Count the boundary"
Then edit the records in the lab and check, on Learn. That's learn dot get er done dot I O.
