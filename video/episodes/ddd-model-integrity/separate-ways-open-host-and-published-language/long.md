---
format: long
lesson: ddd-model-integrity/separate-ways-open-host-and-published-language
title: Separate Ways, Open Host Service and Published Language
thumb: Fifteen translators, or six?
---

@chapter Integration costs
@title text="Separate Ways, Open Host, Published Language" sub="Domain-Driven Design, Chapter 14" art=thumb
Every integration costs something. Besides coordinating teams, it forces compromise. A simple model made for one need gives way to a more abstract one. A technology that would make a feature easy is hard to fit in. A team may be hard to work with.

@quote text="Integration is always expensive. Sometimes the benefit is small." cite="Evans, Domain-Driven Design, Chapter 14"
So Evans heads the first pattern with two sentences. Integration is always expensive. Sometimes the benefit is small.

@chapter Separate Ways
@list heading="Need integrating?" items="Calls the other's functions?@call on each|Acts on shared objects?@act on objects|Shares data while running?@share data"
If two parts of a system don't call on each other's functions, don't act on objects both touch, and don't share data while they run, integrating them may bring nothing. Two features meeting in one use case is no proof they need integrating.

@art separate-apps-menu
So cut the context loose, and let its developers solve their narrow problem as simply as they can. His example is an insurance project that had stalled. A week of ruthless scoping found features that integration added little to. They shipped almost at once, as small unconnected applications launched from one menu.

@art insurance-stall
When the main project stalled again, those small applications were all it left behind. But Evans is fair to the cost. Models grown apart are hard to merge, and if integration is needed later, the translation may be complex.

@chapter Open Host Service
@art many-adapters
Now the opposite problem: a context many others need. A translator for each client is fine for one off integrations. But a subsystem in demand soon does the same work again and again, with more to keep and more to worry about at every change.

@art open-host
So describe the subsystem as a set of Services behind one protocol any team may use. Grow it for common needs, and give one team's unusual needs its own translator, so what everyone shares stays simple. It pays only with a coherent set of Services and many integrations. And every client is coupled to the host's dialect.

@chapter Published Language
@art shared-language
A domain model built for its own users carries features that only complicate exchange. And a model used as the exchange medium freezes, since it has to stay stable for everyone. So take a shared, well documented language, make it the common medium, and translate into and out of it.

@words text="Published = available + documented" sub="so independent readings agree"
Publishing means only that the language is available to anyone who might use it, and documented well enough that independent readings are compatible. It needn't be new. His example is the Chemical Markup Language, which made tools worth writing that no single database justified.

@chapter Counting translators
@math heading="n contexts" items="point to point:  n·(n − 1)/2 to build,  n − 1 to change@point to point;;published:  n to build,  1 to change@Through a Published Language"
Now the count. Point to point, every pair needs its own translation: n times n minus one, over two, two way translators. A change in one context touches n minus one of them. Through a Published Language, each context needs one translator, n in all, and one to change.

@math heading="six theatres" items="pairwise:  6 × 5 / 2 = 15 · change 5@fifteen;;published:  6 · change 1@six to build;;5/2 as many to build · 5 times as many to change@five halves"
The lesson's network is six theatres sharing a touring production's bookings. Point to point, fifteen to build, five to change. Published, six to build and one to change. That's five halves as many to build, and five times as many to change.

@art square-growth
The gap grows with the square of n, which is why a protocol pays when there are many integrations and not when there are two. With two contexts, point to point needs one translator, and a published language two. And the count leaves out the language itself, the hard part, which is why it has to be stable.

@chapter Where people slip
@list heading="Common slips" items="Integrating whatever shares a use case@The first|Exposing the host's model as the protocol@The second|Widening the protocol for each client@And the third"
The first slip is integrating everything that appears in one use case. The second is exposing the host's own domain model as its open protocol, which freezes it. And the third is widening the shared protocol for each client's special case.

@chapter Try it
@words text="Ten venues, all sharing bookings" sub="programme shop · seat maps · staff rota"
Your turn. Ten venues must all share bookings. Count the two way translators point to point and through a Published Language, and how many each scheme changes when one venue's model changes. Then a box office plans a programme shop, seat maps and a staff rota. Which could go its separate way?

@end text="Integrate only what needs it"
Check the counts in the lab, on Learn. That's learn dot get er done dot I O.
