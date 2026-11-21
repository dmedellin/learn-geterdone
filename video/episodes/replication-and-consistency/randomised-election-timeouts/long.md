---
format: long
lesson: replication-and-consistency/randomised-election-timeouts
title: Randomised election timeouts: why a fixed timeout never elects a leader
thumb: Fixed timeout, zero leaders
---

@chapter The question
@title text="Randomised Election Timeouts" sub="Replication and Consistency" art=thumb
The leader crashes. Every follower times out and stands for election at once. Why do consensus systems randomise that timeout? Because without it, the cluster never elects anyone. Not rarely. Never.

@art split-vote
In an election round, each candidate waits a timeout, then asks for votes. If two stand at the same instant, they each collect part of the cluster, and neither reaches a majority. That's a split vote, and everyone tries again.

@chapter A clean round
@art crowded-slot
A round is clean when exactly one candidate holds the earliest timeout. If two share that earliest slot, it's a split. The winner doesn't win by argument. It wins because it started strictly before all the others.

@art slots
Model the timeout as one of T equally likely slots. T is roughly the width of the random window, divided by the round trip time. It's the resolution at which two candidates can still tell each other apart.

@chapter The sum
@math heading="n candidates, T slots" items="who wins: n choices@n choices;;winner picks slot j: 1/T@one over T;;everyone else strictly later: ((T − j)/T)ⁿ⁻¹@every other candidate;;P(clean) = Σⱼ n · (1/T) · ((T − j)/T)ⁿ⁻¹@add them up"
Condition on the winner's slot, j. There are n choices of who wins. The winner picks slot j with probability one over T. And every other candidate must pick a strictly later slot. The events for different slots can't both happen, so you add them up.

@math heading="n = 5, T = 10 (units of 1/100 000)" items="j = 1:  5/10 · (9/10)⁴ = 32 805@slot one;;j = 2:  20 480 · j = 3:  12 005@slot two;;j = 4 … 9:  6480 + 3125 + 1280 + 405 + 80 + 5@then;;j = 10:  0@the last slot;;total = 76 665/100 000 = 15 333/20 000 = 76.665%@seventy six point six"
With five candidates and ten slots, slot one contributes thirty two thousand eight hundred and five, in units of a hundred thousandth. Slot two, twenty thousand four hundred and eighty. Slot three, twelve thousand and five. Then they shrink fast. The last slot is zero. In total, seventy six point six six five percent.

@art early-win
Nearly half the mass is in the first two slots. A clean round is usually won early, because winning late needs everyone else to have chosen later still. And the final slot can't win at all.

@chapter Expected rounds
@math heading="Rounds are independent" items="expected rounds = 1/P@one over P;;T = 10:  20 000/15 333 = 1.3044@one point three oh;;T = 20:  P = 87.9166%,  1.1374@twenty slots"
Each round redraws every slot, so the number of rounds until a clean one is geometric, with expectation one over P. At ten slots, that's one point three oh four four rounds, about a third of an extra election. At twenty slots, one point one three seven four.

@chapter A fixed timeout
@math heading="T = 1" items="P(clean) = 5 · (1/1) · (0/1)⁴ = 0@five times;;expected rounds = 1/0@one over zero"
Now remove the randomisation. With one slot, every candidate picks it. P clean is five times one times zero, exactly zero. And the expected rounds is one over zero. That's what it never elects looks like.

@art identical-retry
It's not a worse point on a spectrum. It's broken. Every retry reproduces the tie. A cluster that elects instantly in testing, where clocks and loads differ, and never elects on identical hardware, is showing you this.

@chapter The window's cost
@art window-tradeoff
Wider windows have a price. Twenty slots raise the clean chance, but each round waits up to twice as long. What users feel is rounds times round length, and that has a best point in the middle. That's why implementations use a few round trips, not the widest window possible.

@words text="All three assumptions are pessimistic"
And the model is pessimistic in three ways. It assumes every candidate starts at once, that slots are discrete, and that every follower stands. That's the safe direction for sizing a timeout.

@chapter Where people slip
@list heading="Common slips" items="Expecting a fixed timeout to mostly work@The first|Reading 76.665% as the chance of ever electing@The second|Widening the window for the clean probability@The third"
The first slip is expecting a fixed timeout to work most of the time. It works none of the time. The second is reading seventy six point six percent as the chance of ever electing. It's the first round. The third is widening the window just because it raises the clean probability.

@chapter Try it
@words text="n = 8 candidates, T = 10" sub="j = 1 term: 8/10 · (9/10)⁷"
Your turn. A nine node cluster loses its leader, so eight candidates, still ten slots. The exponent becomes seven. Predict whether the clean probability rises or falls, compute it, and find the T that restores one point three oh four four rounds.

@end text="Set the slots, count the rounds"
You can set the candidates and slots and see every term of the sum, on Learn. That's learn dot get er done dot I O.
