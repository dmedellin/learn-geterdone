---
format: long
lesson: ddd-life-cycle/repositories
title: Repositories: stored objects as if they were in memory
thumb: Ask for objects, not rows
---

@chapter Getting a reference
@title text="Repositories and Relational Databases" sub="Domain-Driven Design, Chapter 6" art=thumb
Before you can do anything with an object, you need hold of it. Evans asks how.

@quote text="To do anything with an object, you have to hold a reference to it. How do you get that reference?" cite="Evans, Domain-Driven Design, Chapter 6"
To do anything with an object, you have to hold a reference to it. How do you get that reference?

@list heading="Three ways" items="Create it@create|Traverse from one you hold@traverse|Search the database@search"
He counts three ways. Create the object. Traverse an association from an object you already hold. Or search the database by attributes, and rebuild what you find. One team tried to manage with the first two alone, and built the very tangle he'd warned against.

@art query-leak
The third way is necessary and dangerous. A client that writes its own queries, gets rows back and feeds them to constructors is thinking about the technology, not the domain. It's tempted to grab exactly the data it wants, past the aggregates. Rules drift into query code, and entities become containers of data.

@chapter The pattern
@art collection-illusion
So give a type one object that clients can treat as if it simply held every such object in memory. Clients add and remove objects through it, and ask for the ones matching a condition, getting whole objects back. It alone talks to the store.

@list heading="Only for" items="Aggregate roots@aggregate roots|that can't be reached by traversal@following references"
Only aggregate roots get one, and only those clients can't reach by following references. In return, clients get a simple model, persistence is decoupled from the domain, and tests can use an in memory stand in.

@chapter Querying
@code block=1 lines=1-14 label=Java focus="2@withNumber|3-4@satisfying|10-13@DueForService"
Here's a bike-share's repository. It has a hard coded query, withNumber. And it accepts a specification, through satisfying and countSatisfying. DueForService is the workshop's question: a bike is due if it's docked, and either has done eight hundred kilometres since its last service, or has an open fault.

@math heading="fleet · 5 bikes" items="b101: docked, 950 km ✓@b one oh one;;b102: docked, 300 km, 2 faults ✓@b one oh two;;b103, b104, b105 ✗@selects two"
The lab holds five bikes and asks that question. It selects two. B one oh one is docked at nine hundred and fifty kilometres. B one oh two is docked at three hundred, but with two faults.

@art bike-fleet
Of the three that fail, b one oh three fails first on being docked. It's out on a ride. B one oh four and b one oh five fail on kilometres, at four hundred and twenty and seven hundred and ninety-nine.

@math heading="worn-only" items="status = docked and km ≥ 800@docked and;;selects only b101@only"
A simpler repository might offer only a hard coded query: docked and at least eight hundred kilometres. That selects only b one oh one. B one oh two's faults no longer count.

@chapter Know what it costs
@art memory-blowup
Encapsulation doesn't excuse ignorance. Client code can ignore how a repository works, but its developers can't. In Kyle Brown's story, a system ran out of memory after hours in production, because a summary was computed by fetching every object in the plant.

@words text="The client commits" sub="it knows where the unit of work ends"
So abstract the type, use the freedom to cache or change strategy, and leave the commit to the client, which knows where the unit of work begins and ends.

@chapter Factories and tables
@art make-versus-find
Factories and repositories meet at reconstitution. One creates what didn't exist. The other finds what already does, and may hand the rebuilding to a factory. Evans advises against a combined find or create, since the difference usually matters in the domain.

@art rows-match-objects
And when the schema exists to store this system's objects, keep the tables close to the model. A row holds an object, a foreign key becomes a reference, with names that match. And keep other processes out, since they can break the objects' invariants.

@chapter Where people slip
@list heading="Common slips" items="A repository for every class@The first|Clients needn't know the cost@The second|A repository is a factory@And the third"
The first slip is giving every stored class a repository. The docks here belong to a station's aggregate, and get none. The second is thinking a repository's developers needn't understand its cost. And the third is treating a repository as a factory because it builds objects from rows.

@chapter Try it
@words text="b201 · b202 · b203" sub="docked and (km ≥ 800 or faults ≥ 1)"
Your turn. Three more bikes. B two oh one, docked, eight hundred kilometres, no faults. B two oh two, in repair, fifty kilometres, three faults. B two oh three, docked, six hundred and forty, no faults. Which does the specification select, and where does each other one first fail?

@end text="Ask the repository"
Type them into the lab to check, on Learn. That's learn dot get er done dot I O.
