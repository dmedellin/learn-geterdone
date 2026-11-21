---
format: long
lesson: storage-engines-and-indexes/the-height-of-a-b-tree
title: A billion keys in four levels: the height of a B-tree
thumb: A billion keys, two reads
---

@chapter Is a billion slow?
@title text="The Height of a B-tree" sub="Storage Engines and Indexes" art=thumb
You've got a billion keys in an index. Surely finding one is slow? It isn't, and the reason is one multiplication you can do in your head.

@art wide-tree
In a B-tree, every internal node holds up to B children. A 4 kilobyte page with five hundred index entries gives a fanout of five hundred. So every level multiplies the reach by five hundred.

@words text="h = smallest h with Bʰ ≥ N" sub="= ⌈log_B N⌉"
The height is the smallest h where B to the h is at least N, the number of keys. That's the ceiling of log base B of N. A lookup goes down one node per level, one page per node, so an uncached lookup costs h page reads.

@chapter Multiply, don't take logs
@math heading="N = 10⁹,  B = 500" items="h = 1:  500  < N@five hundred;;h = 2:  250 000  < N@two hundred and fifty thousand;;h = 3:  125 000 000  < N@a hundred and twenty five million;;h = 4:  62 500 000 000  ≥ N@sixty two and a half billion"
Multiply it out. Five hundred, less than a billion. Two hundred and fifty thousand, less. A hundred and twenty five million, still less. Sixty two and a half billion, at least a billion. Stop. Height four.

@art multiply-steps
That table isn't an illustration of the answer. It is the computation. Four multiplications and four comparisons, in exact integers. And there's a reason to do it this way, not with a logarithm.

@math heading="The logarithm trap" items="log(9) / log(3) = 2.0000000000000004@two point zero;;ceiling → 3,  but 3² = 9  so h = 2@the ceiling"
At an exact power of the fanout, a floating point quotient of logs can land just above the integer. Log nine over log three comes out at two point zero, with a four in the sixteenth place. The ceiling then says three, but three squared is nine, so the true height is two. That's a whole extra disk read, on a page about counting them.

@chapter Where the height moves
@words text="10⁶ → 3   ·   10⁹ → 4   ·   10¹² → 5" sub="B = 500"
Hold B at five hundred and grow N. A million keys is three levels. A billion is four. A trillion is five. Three orders of magnitude buy one level. The height only changes when N crosses a whole power of B, so every tree from just over a hundred and twenty five million keys to sixty two and a half billion is exactly four levels deep. That's a range of five hundred to one.

@art narrow-vs-wide
So don't reason as if the base were two. Log base two of a billion is about thirty. Log base five hundred of a billion is about three point three three. A B-tree exists to make the base the number of entries a page holds.

@chapter The cache takes the top off
@art level-sizes
Now look at the size of each level, not the count. At four kilobytes a page, the root is four kilobytes. The second level is two megabytes. The third is one gigabyte. The fourth is five hundred gigabytes.

@art cached-top
So the levels that are cheap to keep in memory are exactly the ones every lookup passes through. Keep the top two, about two megabytes, and a four read lookup becomes a two read lookup. The height didn't change.

@math heading="10 000 lookups /s" items="nothing cached:  4 × 10 000 = 40 000 reads/s@forty thousand;;top two cached:  2 × 10 000 = 20 000 reads/s@twenty thousand"
At ten thousand lookups a second, with nothing cached, that's forty thousand disk reads a second. With the top two levels resident, twenty thousand. Two megabytes halved the device's day.

@art descent-path
Two assumptions. Nodes are taken as full, and real nodes are between half full and full, so the true height is occasionally one more. Both errors point the same way.

@chapter Where people slip
@list heading="Common slips" items="Taking the height from a floating-point log@The first|Quoting the height as the lookup cost@The second|Reasoning as if the base were two@the third"
The first slip is taking the height from a floating point logarithm. The second is quoting the height as the cost of a lookup, when the cost is the levels the cache doesn't hold. And the third is reasoning about the height as if the base were two.

@chapter Try it
@words text="N = 10⁹,  B = 100" sub="first move: 100³ = 10⁶, far short of N"
Your turn. A billion keys with a fanout of a hundred, a longer key. A hundred cubed is a million, far short. Finish the search, state the height, and say how many levels must be resident to keep a lookup at two disk reads.

@end text="Multiply the fanout out"
You can move the fanout and the key count and watch the levels, on Learn. That's learn dot get er done dot I O.
