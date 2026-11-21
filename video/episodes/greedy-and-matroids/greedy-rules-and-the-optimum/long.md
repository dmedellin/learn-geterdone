---
format: long
lesson: greedy-and-matroids/greedy-rules-and-the-optimum
title: Four greedy rules, one optimum: which ones are actually right?
thumb: Matching once proves nothing
---

@chapter The question
@title text="Greedy Rules and the Optimum" sub="Greedy Algorithms and Matroids" art=thumb
A greedy algorithm makes a choice and never takes it back. That makes it fast. It also means one bad early choice is never repaired. So how do you tell a greedy rule that works from one that only looks like it does?

@art interval-bars
Here's the problem. You're given intervals, each one a span from a start to a finish. Pick as many as you can so that no two overlap. Intervals that only touch, one finishing exactly where the next starts, don't count as overlapping.

@words text="Greedy = an order + no regrets"
Every greedy rule here is the same pattern. Fix an order on the intervals. Walk it once. Take the current one if it fits, and skip it forever if it doesn't. The only thing that changes from rule to rule is the order.

@chapter Four rules
@list heading="Four orders" items="Earliest finish@Earliest finish|Earliest start@earliest start|Shortest first@Shortest first|Fewest conflicts first@fewest conflicts"
Earliest finish sorts by finish time. Earliest start sorts by start time. Shortest first sorts by length. And fewest conflicts counts how many others each interval overlaps, and sorts by that count.

@art finish-pointer
Then each rule sweeps its order and keeps just one number, the finish time of the last interval it took. A candidate is taken if it starts no earlier than that. For earliest finish, that's the same as fitting with everything chosen. For the other three orders, it isn't.

@chapter Eleven intervals
@words text="A 1–4 · B 3–5 · C 0–6 · D 5–7 · E 3–9 · F 5–9" sub="G 6–10 · H 8–11 · I 8–12 · J 2–14 · K 12–16"
The lab opens on eleven intervals, labelled A to K. A runs from one to four, B from three to five, C from zero to six, and so on, up to K, from twelve to sixteen.

@list heading="Four answers" items="Earliest finish: A D H K  →  4@Earliest finish takes|Earliest start: C G K  →  3@Earliest start takes|Shortest first: B D H K  →  4@Shortest first takes|Fewest conflicts: K  →  1@fewest conflicts takes"
Earliest finish takes A, D, H and K, four intervals. Earliest start takes C, G and K, three. Shortest first takes B, D, H and K, four. And fewest conflicts takes K alone, just one.

@art subset-grid
Is four good? Eleven intervals have two thousand and forty eight subsets. Try every one, keep the feasible ones, and the largest has four intervals: A, D, H and K. So two rules hit the optimum here, one is one short, and one is three short.

@chapter A match is not a proof
@art short-blocks
Shortest first got four, which is optimal. But it's not a correct rule. Take three intervals: zero to five, four to six, and five to ten. Shortest first grabs the two unit interval in the middle, which blocks both others. It ends with one. The best of the eight subsets is two.

@words text="One counterexample is enough" sub="One success proves nothing"
That's the whole lesson in miniature. One instance where a rule is wrong is all it takes to reject it. One instance where it's right is worth nothing at all.

@chapter Every loser has its instance
@art long-day
Earliest start fails on zero to ten, then one to two, three to four, five to six and seven to eight. The interval that starts first fills the whole day. The rule takes it and stops at one, when the optimum is four.

@words text="0–2 · 2–4 · 4–6 · 6–8 · 1–3 · 3–5 · 5–7" sub="fewest conflicts: 2 · optimum: 4"
Fewest conflicts fails on seven intervals. It takes the two ends, each with one conflict, and returns two, against an optimum of four. The middle isn't unusable. The sweep's finish pointer just stands at eight, and the middle intervals start behind it.

@chapter Stays ahead
@art stays-ahead
Earliest finish has no such instance. It's optimal on every input, and that needs a proof, not a lab. On the opening instance, greedy's finish times are four, seven, eleven and sixteen, and it never falls behind the optimum at any step.

@math heading="Stays ahead" items="gᵢ = greedy's i-th finish time@g i;;oᵢ = the optimum's i-th finish time@o i;;gᵢ ≤ oᵢ  for every i, on every input@less than or equal to"
Write g i for greedy's i th finish time, and o i for the optimum's. The claim is that g i is less than or equal to o i for every i, on every input. That's induction, not four numbers.

@chapter Where people slip
@list heading="Common slips" items="Reading a match as a proof@The first|Trusting a size without checking feasibility@The second|Assuming the panel runs your textbook's rule@The third"
The first slip is reading a match with the optimum as a proof. The second is trusting a size without checking the selection is feasible, pair by pair. The third is assuming the panel's fewest conflicts rule is your textbook's. It counts conflicts once, in the full instance, and never recounts.

@chapter Try it
@words text="0–5 · 4–6 · 5–10" sub="run all four rules, then try all 8 subsets"
Your turn. Take zero to five, four to six and five to ten. Run each of the four rules by hand, then list all eight subsets and find the best. Which rules match, and which one would you trust?

@end text="Run the four rules yourself"
You can type your own intervals and see every rule against the true optimum, on Learn. That's learn dot get er done dot I O.
