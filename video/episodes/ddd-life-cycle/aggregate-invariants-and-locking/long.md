---
format: long
lesson: ddd-life-cycle/aggregate-invariants-and-locking
title: Two correct edits, one broken rule: locking aggregates
thumb: Each edit passes, the sum fails
---

@chapter The order
@title text="Aggregate Invariants and Concurrent Change" sub="Domain-Driven Design, Chapter 6" art=thumb
Here's a puzzle. Two users each make a perfectly correct change. Each checks the rule. And together they break it.

@art order-lines
Evans's example is a purchase order broken into line items, each for a quantity of a catalogue part. One rule: the items' total may not pass the order's approval limit.

@art two-copies
The first scheme locks only the object a user starts to edit. Two buyers change two different lines of the same order. Each checks the total against the limit in their own copy, and each is within it. Neither line is locked by the other. Both commit, and the stored order is over its limit, with no one aware.

@chapter Lock more?
@art deadlock
Locking the whole order would have refused the second save. But a part's price can change too, breaking the rule from another direction. So Evans tries locking the parts as well. Users start waiting on one another over popular parts, and finally deadlock.

@chapter A better model
@list heading="What the business knows" items="Parts appear in many orders@many orders|Parts change less often than orders@less often|A price change needn't reach old orders@already placed"
The way out isn't a cleverer lock. It's more knowledge of the business. Parts appear in many orders. Parts change less often than orders. And a price change needn't reach orders already placed.

@art copied-price
So the price is copied into each line when it's added. The line no longer depends on the part's current price, and the order and its lines become one aggregate whose limit can be enforced.

@quote text="We need to find a model that leaves high-contention points looser and strict invariants tighter." cite="Evans, Domain-Driven Design, Chapter 6"
That's the goal Evans sets. We need to find a model that leaves high contention points looser, and strict invariants tighter. The loosened rule doesn't vanish: he suggests a daily list of items with outdated prices.

@art limit-bar
Notice two things about that last step. The rule that stays strict, the limit, is now wholly inside one boundary. And the ownership matches the business. An order and its lines are created and deleted together, while parts come and go on their own. Once the aggregate is drawn, the lock follows it.

@chapter A cookery class
@code block=1 lines=1-18 label=Java focus="4@places|7-13@resize|9-11@over"
Now the lab's version. A cookery school's Saturday class has twelve places. The class is the root, and resize checks the rule in memory: if the others plus the new size go over the places, it throws.

@math heading="Saturday class, 12 places" items="Walshes 4 · Okafors 3 · Lins 2 = 9@nine places;;Pat: Okafors → 5, then 6 · sum 12 ✓@Pat makes;;Sam: Lins → 4 · sum 11 ✓@Sam makes"
Three parties have booked: the Walshes with four, the Okafors with three, and the Lins with two. Nine places. Pat and Sam each read the class at minute zero. Pat makes the Okafors five, then six. In Pat's copy the sum is twelve. Sam makes the Lins four. In Sam's copy, eleven. Each passes the check.

@math heading="object-locks" items="2 commit · 0 refused@neither waits;;final 4, 6, 4 = 14 > 12@fourteen;;invariant broken · 0 edits lost@lost"
Under object locks, Pat locks the Okafors' line and Sam the Lins', so neither waits. Both commit. The final values are four, six and four: fourteen, against a limit of twelve. Neither did anything wrong. No edits were lost, because they changed different parties.

@math heading="aggregate-lock" items="1 commits · Sam refused@Sam's edit;;final 4, 6, 2 = 12@twelve;;invariant holds@holds"
Under an aggregate lock, Pat's first edit takes the whole class. Sam's edit is refused, and discarded until Sam reads the class again. The final values are four, six and two. Twelve, and the invariant holds.

@art refused-wait
The price is the refusal itself. Sam was changing a different party, and still had to wait.

@words text="same-party: object locks catch it"
And when both staff edit the Okafors, object locks do catch it. The second is refused on the same line. Object locks protect a rule about one object. The trouble starts when the rule is about the sum of several.

@chapter Where people slip
@list heading="Common slips" items="Every edit checks, so it's safe@The first|Lock everything the rule touches@The second|An aggregate lock is free@And the third"
The first slip is believing that if every edit checks the rule, the rule is safe. The second is locking everything the rule touches, which ends in deadlock. And the third is treating an aggregate lock as free.

@chapter Try it
@words text="limit 15 · ana 6, ben 5, cho 2" sub="kim and lee edit"
Your turn. A guided walk, limit fifteen. Ana's party has six, Ben's five, Cho's two. Kim changes Cho to three, then four. Lee changes Ben to six. Under each scheme, who commits, what's the sum, and does the limit hold?

@end text="Run both locking schemes"
Set the scheme in the lab and check, on Learn. That's learn dot get er done dot I O.
