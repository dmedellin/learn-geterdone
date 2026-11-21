---
format: long
lesson: greedy-and-matroids/caching-and-the-offline-bound
title: The optimal cache you can't build, and the bigger cache that does worse
thumb: More cache, fewer hits
---

@chapter The question
@title text="Caching and the Offline Bound" sub="Greedy Algorithms and Matroids" art=thumb
A cache holds a few pages. When a page you need isn't there, you have to load it and throw something out. Which page should go? There's a perfect answer, and no real cache can use it.

@art cache-slots
Here's the setup. A cache holds k pages, and a trace is a sequence of page requests. A request for a page that's already there is a hit. Otherwise it's a miss, the page is loaded, and if the cache is full, one page is evicted. A policy is just the rule for choosing which.

@chapter Three policies
@list heading="Who gets evicted?" items="FIFO: resident longest@FIFO|LRU: unused for longest@LRU|Farthest in future: next used latest@Farthest in future"
FIFO evicts the page that's been in the cache longest. LRU evicts the page that's gone unused for longest. And farthest in future evicts the page whose next use comes latest, and a page never used again goes first.

@words text="1 2 3 4 1 2 5 1 2 3 4 5" sub="three slots · twelve requests"
The lab opens on twelve requests over five pages: one, two, three, four, one, two, five, one, two, three, four, five, with three slots.

@math heading="Hits on the opening trace" items="FIFO: 3 hits = 1/4@FIFO gets;;LRU: 2 hits = 1/6@LRU gets;;Farthest in future: 5 hits = 5/12@farthest in future gets"
FIFO gets three hits, a rate of one quarter. LRU gets two, one sixth. And farthest in future gets five, five twelfths. LRU usually beats FIFO, but that's not a theorem, and on this trace it loses by one.

@chapter A bound, not a policy
@art look-ahead
Farthest in future needs the whole trace in advance. No real cache knows the requests that haven't happened yet. So it isn't a policy you can build. It's a bound, the best that any policy could do.

@words text="Farthest in future is optimal" sub="every trace · every cache size"
And it is optimal. For every trace and every cache size, no policy, online or offline, gets more hits. The proof is an exchange argument, the same shape as the one for intervals, swapping an optimal schedule's evictions for farthest in future's without losing a hit.

@art state-search
The lab doesn't run that proof. It checks this instance directly, by searching every eviction a three slot cache could make. On the opening trace, that search visits forty three states, and the best it can find is five hits. Exactly what farthest in future got.

@words text="1 2 3 4 · 1 2 3 4 · 1 2 3 4" sub="FIFO 0 · LRU 0 · offline optimum 6 of 12"
Online policies can fall a long way short. Loop one, two, three, four three times, with three slots. FIFO and LRU both get zero. The offline optimum gets six of twelve.

@art loop-trace
On that loop, each online policy evicts exactly the page that's about to be used. On every miss, the offline optimum throws out the page whose turn comes last, rather than the one whose turn comes next.

@chapter Belady's anomaly
@math heading="FIFO, slots 1 to 6" items="0, 0, 3, 2, 7, 7@zero, zero, three, two;;3 slots: 3 hits → 4 slots: 2 hits@three slots"
Now sweep FIFO from one slot up to six, on the opening trace. The hits read zero, zero, three, two, seven, seven. Going from three slots to four costs you a hit. A bigger cache does worse. That's Belady's anomaly.

@art bigger-cache
It happens because the extra slot changes which pages are resident when each request arrives. FIFO's order doesn't respect what's about to be used, so the change can go the wrong way.

@math heading="LRU, slots 1 to 6" items="0, 0, 2, 4, 7, 7@zero, zero, two, four"
LRU on the same trace reads zero, zero, two, four, seven, seven, and never falls. That's not luck.

@art stack-sets
LRU is a stack policy. The pages it holds with k slots are always among those it would hold with k plus one, so more cache can't hurt.

@chapter Where people slip
@list heading="Common slips" items="Treating farthest in future as a policy to build@The first|Assuming more cache can't hurt@The second|Reading FIFO's sweep as a fact about caching@The third"
The first slip is treating farthest in future as something to implement. It's a yardstick. The second is assuming more cache can't hurt. For FIFO it can. The third is reading the panel's sweep, which is always FIFO's, as a statement about caching in general.

@chapter Try it
@words text="1 2 3 1 4 1 2 5 1 2 3 4 5" sub="three slots"
Your turn. Take this thirteen request trace with three slots. Run FIFO and LRU by hand. Both should get four hits, while farthest in future gets six. Then try FIFO with four slots, and see whether it gets better or worse.

@end text="Sweep the cache size yourself"
You can run every policy on your own trace and sweep the cache size, on Learn. That's learn dot get er done dot I O.
