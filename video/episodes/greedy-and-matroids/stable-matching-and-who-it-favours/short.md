---
format: short
lesson: greedy-and-matroids/stable-matching-and-who-it-favours
title: Stable matching picks a side
---

@art two-sides
The stable matching algorithm always picks a side.

@words text="6 stable matchings" sub="the algorithm returns one"
On the opening instance, six different matchings are stable. Deferred acceptance returns just one of them.

@words text="proposers: mean rank 1 · receivers: 4"
It's the one every proposer likes best, and every receiver likes worst. Let the receivers propose, and it flips. Stable doesn't mean fair. It only means no two people would both rather have each other.

@end text="Full lesson on Learn"
Swap the sides yourself on Learn.
