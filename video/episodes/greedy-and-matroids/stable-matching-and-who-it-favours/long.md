---
format: long
lesson: greedy-and-matroids/stable-matching-and-who-it-favours
title: Stable matching: always stable, never neutral
thumb: Stable is not fair
---

@chapter The question
@title text="Stable Matching, and Who It Favours" sub="Greedy Algorithms and Matroids" art=thumb
You've got two groups, proposers and receivers, and everyone ranks everyone on the other side. Can you pair them up so nobody has a reason to break away? Yes, always. The more interesting question is which pairing you get, and who it suits.

@art blocking-pair
A matching pairs each proposer with exactly one receiver. A blocking pair is a proposer and a receiver who aren't matched together, but who'd both rather have each other than their current partners. A matching with no blocking pair is stable.

@chapter Deferred acceptance
@list heading="Deferred acceptance" items="A free proposer asks the best receiver not yet tried@A free proposer|A free receiver accepts@A free receiver|An engaged receiver trades up, or rejects@An engaged receiver|Stop when everyone is engaged@It stops"
A free proposer asks the best receiver they haven't tried yet. A free receiver accepts. An engaged receiver accepts only if they prefer the newcomer, releasing the old partner, and otherwise rejects. It stops when everyone is engaged.

@art proposal-arrows
The greedy part is that proposers work down their lists and never go back up. The deferred part is that receivers hold the best offer so far, and can let it go. If receivers accepted for good, the result wouldn't be stable.

@chapter Why it works
@words text="at most n² proposals" sub="each proposer asks each receiver at most once"
It always ends, because each proposer asks each receiver at most once, so there are at most n squared proposals. And everyone gets matched, because a receiver who's had any proposal stays engaged and only trades up.

@art trade-up
Now suppose p and r were a blocking pair, so p prefers r to their partner. Then p proposed to r earlier. Either r rejected p, already holding someone better, or r accepted and later swapped p for someone better. Either way r only improved, so r doesn't prefer p. No blocking pair.

@chapter Four on each side
@words text="4 proposals · 12 ordered pairs · 0 blocking" sub="proposer i ↔ receiver i"
On the opening instance, with four on each side, the algorithm makes four proposals, well under the bound of sixteen, and every one is accepted at once. Proposer i gets receiver i. The panel tests all twelve ordered pairs, and the list of blocking pairs is empty.

@math heading="All 24 matchings: 6 stable" items="1234 · 1243 · 2134 · 2143 · 2341 · 4321@six are stable;;proposers' mean rank: 1, 3/2, 3/2, 2, 5/2, 7/2@mean ranks"
Then it tests all twenty four matchings against the definition, and six are stable. Written as each proposer's partner in order: one two three four, one two four three, two one three four, two one four three, two three four one, and four three two one. For the proposers, their mean ranks run from one, up to seven halves.

@art two-sides
The algorithm returned one two three four, mean rank one for the proposers, the best of all six. The receivers' mean rank is four, the worst possible. Swap the sides, let the receivers propose, and you get four three two one, with mean ranks seven halves and one.

@chapter Who it favours
@words text="Every proposer gets their best stable partner" sub="simultaneously"
That's the theorem. Every proposer gets the best partner they have in any stable matching, all at the same time. No proposer can point to another stable matching where they personally do better. And every receiver gets their worst.

@art rank-ladders
So stability is a guarantee, and fairness isn't one. Stability forbids exactly one thing, a pair who'd both rather have each other. It still allows a whole side to end up at the bottom of the ladder.

@art stable-list
The panel checks that the right way round. It doesn't trust the algorithm to describe its own output. It reads each proposer's best possible partner off the list of all stable matchings, objects the algorithm never saw, and compares.

@chapter Where people slip
@list heading="Common slips" items="Reading stability as fairness@The first|Stopping at the stability verdict@The second|Trusting a caption over the trace@The third"
The first slip is reading stability as fairness. Here, one whole side gets its worst stable partner. The second is stopping at the stability verdict, when the real question is which stable matching you got. The third is trusting a caption over the trace. Extra proposals come from rejections, and a rejection needn't displace anyone.

@chapter Try it
@words text="Swap the sides" sub="receivers propose"
Your turn. Take the opening instance and let the receivers propose instead. Check that you get four three two one, list its blocking pairs, and work out who did best this time.

@end text="Run the proposals yourself"
You can run deferred acceptance, list every stable matching, and swap the sides, on Learn. That's learn dot get er done dot I O.
