---
format: long
lesson: ddd-large-scale-structure/responsibility-layers
title: Responsibility Layers: layers that tell the domain's story
thumb: Depend only downward
---

@chapter Beyond handcrafted objects
@title text="Responsibility Layers" sub="Domain-Driven Design, Chapter 16" art=thumb
Throughout the book, each object has a narrow set of related responsibilities. But when every one is handcrafted, there's no way to reason about large regions of the model at once.

@art strata
In some domains, deep understanding reveals a natural stratification. Some concepts sit against a background of others that change independently, at a different rate and for different reasons. Layering is the established way to use that.

@chapter The pattern
@art layer-stack
So name a few broad responsibilities the domain itself shows, far wider than any object's. Refactor until every object, aggregate and module belongs to exactly one. Members of a layer may use the layers beneath, and know nothing of those above. Evans prefers the relaxed variant, where a layer may reach any lower layer, not only the next.

@words text="Not UI · application · domain · infrastructure" sub="this divides the domain layer itself"
This is a different cut from Chapter four's layered architecture, which separates the user interface, application, domain and infrastructure. Responsibility layers divide the domain layer itself, and they should tell the story of the system's purpose.

@art shipping-layers
In the book's shipping example, the team notices that schedules can be discussed without the cargo they carry, but not the other way round. They name two layers, then a third for the routing service. And when a new regulation arrives, they pick a design that respects the layers, because consistency across a team is worth modest trade offs.

@chapter Choosing layers
@quote text="Choosing a large-scale structure is less a technical decision than a business modeling decision." cite="Evans, Domain-Driven Design, Chapter 16"
Look for three things. Storytelling: the layers should bring out the business's priorities. Conceptual dependency: upper concepts mean something against lower ones, and lower ones make sense alone. And conceptual contours, where things change at different rates. Choosing a large scale structure is less a technical decision than a business modeling decision.

@list heading="Five layers that recur" items="Potential: what could we do?@Potential|Operations: what are we doing?@Operations|Decision Support: what should we do?@Decision Support|Policy: the rules and goals@Policy|Commitment: what we've promised@Commitment"
Evans has seen five layers recur in enterprise systems. Potential asks what the business could do. Operations, what it's doing. Decision Support, what it should do. Policy holds rules and goals that constrain the others. And Commitment records what has been promised.

@words text="Four, or possibly five" sub="examples, not a template"
He ends on restraint. Beyond four, or possibly five, layers stop telling a story. And a domain unlike these may need layers of its own. Start somewhere, and let the order evolve.

@chapter A box office in four layers
@code block=1 lines=1-14 focus="3-4@performance and its tickets|5@concession rule|10@asks policy"
Now the count: a theatre box office in four layers, decision, policy, operations and potential. A booking is operations. It holds its performance and its tickets, and also its concession rule, a policy object. And to price itself, operations asks policy.

@math heading="as-first-written: 11 dependencies" items="6 downward · 3 within · 2 upward@six downward;;upward: Booking on ConcessionRule, Auditorium on Performance@two upward;;1 skip: PricingAdvisor on Booking@skips"
The lab counts eleven dependencies. Six downward, three within a layer, and two upward: the booking on its concession rule, and the auditorium on its performances, because each auditorium kept a list. One downward dependency, the pricing advisor on a booking, skips over policy, which relaxed layering allows.

@art upward-dependency
Those two upward arrows break the story. An operational booking shouldn't need to know about policy, and an auditorium, which is potential, shouldn't need to know what's playing in it.

@art turned-round
The refactoring turns the first one round.

@code block=2 lines=1-14 focus="3-9@reads the booking|11-13@a single ticket"
Now the rule reads the booking, and the booking never names the rule. It halves the face price of a single ticket if it's a concession. And the auditorium's list goes, replaced by asking a repository for an auditorium's performances.

@math heading="refactored: 10 dependencies" items="7 downward · 3 within · 0 upward@seven downward"
Now there are ten dependencies, seven downward, three within, and none upward, with the same one skip. Every remaining dependency runs the way the layers' story says.

@chapter Where people slip
@list heading="Common slips" items="Confusing them with Chapter 4's layers@The first|Using the five as a template@The second|Counting a skip as a violation@And the third"
The first slip is taking responsibility layers for the user interface, application, domain and infrastructure layers. The second is treating Evans's five layers as a template every system must fill. And the third is counting a dependency that skips a layer as a violation. Only upward ones break it.

@chapter Try it
@art clinic-layers
Your turn. A clinic in the same four layers: clinicians and rooms, appointments and visits, a booking limit, and a schedule optimizer, with seven dependencies. Sort them into downward, within a layer and upward. Name the upward ones, and count the downward ones that skip a layer.

@end text="Depend only downward"
Type the model into the lab and compare, on Learn. That's learn dot get er done dot I O.
