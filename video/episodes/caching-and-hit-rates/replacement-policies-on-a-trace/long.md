---
format: long
lesson: caching-and-hit-rates/replacement-policies-on-a-trace
title: Replacement policies on a trace, and the cache that got worse when it grew
thumb: More memory, more misses
---

@chapter The question
@title text="Replacement Policies on a Trace" sub="Caching and Hit Rates" art=thumb
Your cache is full and a miss arrives. Something has to go. Which one? Every policy has a sensible sounding rule. But a policy is judged by the hits it gets, not by how its rule sounds.

@art reference-string
So you measure it on a reference string, the sequence of keys the cache is asked for. Run the string through a cache of k slots and count the hits. The first reference to each key always misses, whatever you do. Those are the compulsory misses.

@chapter Four rules
@list heading="Who gets evicted" items="FIFO: the earliest arrival@FIFO evicts|LRU: the least recently used@LRU evicts|LFU: the smallest use count@LFU evicts|Farthest-in-future: next used furthest ahead@farthest in future"
FIFO evicts the key that entered earliest, whatever happened since. LRU evicts the key used least recently. LFU evicts the one with the smallest use count, ties broken by insertion order. And farthest in future evicts the key whose next use is furthest ahead, or never comes.

@art crystal-ball
That last one is special. Farthest in future, also called Belady's algorithm or OPT, has the fewest misses of any policy on a given trace. But it reads the rest of the trace, and no cache can do that. So nobody runs it. It's the ceiling. The proof that it's optimal lives in the Algorithms course.

@chapter Twelve references, three slots
@words text="1 2 3 4 1 2 5 1 2 3 4 5" sub="12 references · 5 distinct keys · 5 compulsory misses"
Here's the trace: one, two, three, four, one, two, five, one, two, three, four, five. Twelve references over five keys, so five compulsory misses for any policy at any size.

@math heading="k = 3 slots" items="OPT:  5 hits = 5/12@the bound;;FIFO:  3 hits = 1/4@FIFO gets three;;LRU:  2 hits = 1/6@LRU gets two;;LFU:  2 hits = 1/6@and LFU"
With three slots, the bound gets five hits, five twelfths. FIFO gets three, a quarter. LRU gets two, a sixth, and LFU gets two, a sixth. FIFO, the policy nobody defends, wins.

@art gap-to-bound
The gap between the bound and LRU is a quarter of all references. That's the most any better online policy could recover, and none recovers all of it, because the bound reads the future. Now your hit rate of a sixth has context: the best possible was five twelfths.

@chapter Four slots
@math heading="k = 4 slots" items="OPT:  6 hits = 1/2@the optimum;;LRU:  4 hits = 1/3@LRU improves;;LFU:  4 hits = 1/3@LFU;;FIFO:  2 hits = 1/6@FIFO goes"
Give the same trace four slots. LRU improves from two hits to four. LFU from two to four. The optimum goes from five to six. And FIFO goes from three hits down to two.

@art bigger-worse
FIFO's misses rose from nine to ten. A larger cache made it worse. That's Belady's anomaly, and here it's not a claim, it's a count.

@chapter Stack algorithms
@art nested-sets
Why can't LRU do that? It's a stack algorithm. At every point of every trace, a k slot cache holds a subset of what a k plus one slot cache holds. So every hit at k is a hit at k plus one, and misses can't rise as the cache grows.

@art evict-oldest
FIFO isn't one. Its eviction order depends on insertion times, and those change when the size changes. FIFO behaves well on most traces. But without that guarantee, no trace is safe.

@words text="12 references are a fact about 12 references" sub="and nothing here is about bookkeeping cost"
Two limits. A hit count on twelve references is a fact about those twelve references, not about your system. A trace with a hot key ranks the policies differently from a round robin. And nothing here prices the bookkeeping LRU needs and FIFO doesn't.

@chapter Where people slip
@list heading="Common slips" items="Believing a bigger cache can never hurt@The first|Comparing policies on one trace at one size@The second|Reading the bound as a target@The third"
The first slip is believing a bigger cache can never hurt. That guarantee belongs to stack algorithms. The second is comparing policies on one trace at one size. FIFO beats LRU at three slots and loses at four. The third is reading the bound as a target. It's the most a change could recover, not what one will.

@chapter Try it
@words text="A B C A B D A B C D" sub="k = 3 and k = 4 · OPT gets 5 hits at k = 3"
Your turn. Run A, B, C, A, B, D, A, B, C, D at three slots and four. You're told the optimum gets five hits at three slots. Find LRU and FIFO at both sizes, say whose ranking changed, and whether any miss count rose.

@end text="Replay your own trace"
You can replay your own trace through all four policies and scan every cache size for the anomaly, on Learn. That's learn dot get er done dot I O.
