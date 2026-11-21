---
format: long
lesson: ddd-life-cycle/factories
title: Factories in Domain-Driven Design: build it whole, or refuse
thumb: Whole, or not at all
---

@chapter Two wrong homes
@title text="Factories" sub="Domain-Driven Design, Chapter 6" art=thumb
Creating a complex object has to live somewhere. Evans's point is that the two obvious homes are both wrong.

@art engine-assembly
The first wrong home is the object itself. Nobody designs an engine block that grabs its own pistons, and the robot that assembles it isn't with you when you drive. Assembling a compound object is a different job from the one it does once it's built.

@art client-knows-parts
The second wrong home is the client. A client that assembles must know the product's internal structure and some of its rules. Even a constructor call ties it to concrete classes. And if the client is in the application layer, domain knowledge has leaked out of the domain.

@quote text="Complex object creation is a responsibility of the domain layer, yet that task does not belong to the objects that express the model." cite="Evans, Domain-Driven Design, Chapter 6"
So, in Evans's words: complex object creation is a responsibility of the domain layer, yet that task does not belong to the objects that express the model.

@chapter The pattern
@art factory-box
So he adds an element that corresponds to nothing in the model, but is still the domain layer's work. When building an object or aggregate is complicated, make it the job of a separate factory. Clients ask in their own terms, never naming the classes it puts together, and get back each aggregate complete.

@list heading="Two requirements" items="Each creation is atomic and consistent@atomic|Return the abstract type@abstract type"
Two requirements follow. Each creation method is atomic and produces only a consistent product, or raises an exception. And the factory returns the abstract type wanted, not the concrete class it built.

@list heading="Where it goes" items="A method on the aggregate root@root|A method on a closely involved object@closely involved|A standalone factory@standalone|Sometimes, just a constructor@constructor"
Where to put one follows from what it hides. A factory method on the root adds elements inside its aggregate. A method on an object closely involved in spawning another, like a brokerage account creating trade orders. A standalone factory, with no natural host. And sometimes a plain constructor is all you need, as long as it's atomic.

@chapter A seed bank's factory
@code block=1 lines=1-19 label=Java focus="2@issues the accession number|5-7@fewer than|11-13@too damp|17@returns"
Here's a seed bank's factory for a new accession, a stored lot of seed. It issues the accession number itself. It refuses a lot with fewer than four hundred seeds, germination under seventy percent, moisture over eight percent, or an unknown origin, like too damp to store. Otherwise it returns a complete accession.

@art seed-packets
Three lots arrive at the bank: a sound one, a damp one, and a small one.

@math heading="sound-lot" items="1,200 seeds ≥ 400 ✓ · 88% ≥ 70 ✓@twelve hundred;;6% ≤ 8 ✓ · origin known ✓@six percent;;admitted@admits"
The lab checks each request clause by clause, in order. The sound lot has twelve hundred seeds at eighty-eight percent germination, six percent moisture, and a known origin. All four clauses are true, and the factory admits it.

@math heading="damp-lot" items="900 ✓ · 81% ✓@nine hundred;;11% ≤ 8 ✗@eleven percent;;refused: too damp to store@too damp"
The damp lot has nine hundred seeds at eighty-one percent, but eleven percent moisture. Three clauses are true, and the first false one is moisture. The factory refuses: too damp to store.

@math heading="small-lot" items="150 ≥ 400 ✗@a hundred and fifty;;origin = known ✗@unknown origin;;first: the seed count@first"
The small lot has a hundred and fifty seeds from an unknown origin, at ninety-two percent and seven percent moisture. Two clauses are false, and the first is the seed count. That's the message a caller would see.

@art refused-request
Every refusal comes out as an exception. So a caller can never be handed an improper accession, and never has to check one.

@chapter Rebuilding is different
@art reconstitute
Reconstitution changes the rule. Rebuilding a stored object differs from creating one in two ways. Its identity comes in as an argument, because a new number would break its continuity. And a broken invariant can't just be refused, because the object already exists.

@code block=2 lines=1-9 label=Java focus="3@its number|5-7@flagForRegeneration"
Suppose the bank raised its minimum to four hundred seeds last year. A stored lot of three hundred is still a lot. So this method takes its number from the row, and calls flagForRegeneration instead of throwing.

@chapter Where people slip
@list heading="Common slips" items="A factory must stand for something@The first|Return half-built objects@The second|Reconstitution must pass creation rules@And the third"
The first slip is thinking a factory must stand for something in the domain. It needn't. The second is handing back a half-built object to finish later. And the third is expecting a reconstituted object to pass the creation rules.

@chapter Try it
@words text="seeds=450 · germination=69 · moisture=9 · origin=known"
Your turn. Four hundred and fifty seeds, sixty-nine percent germination, nine percent moisture, known origin. How many clauses are false, which does the factory report first, and what would reconstitution do with a stored lot like this?

@end text="Send a request to the factory"
Add the request in the lab and check, on Learn. That's learn dot get er done dot I O.
