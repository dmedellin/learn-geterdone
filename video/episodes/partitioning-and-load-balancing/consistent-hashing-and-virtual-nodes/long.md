---
format: long
lesson: partitioning-and-load-balancing/consistent-hashing-and-virtual-nodes
title: Virtual nodes: a hundred times the tokens, ten times the evenness
thumb: Evenness costs a square root
---

@chapter A ring doesn't balance itself
@title text="Virtual Nodes" sub="Partitioning and Load Balancing" art=thumb
Consistent hashing is great when a node joins, because only one arc of keys moves. But it has a quieter problem. With one token per node, the shares of the ring are nothing like equal.

@art one-token-ring
Put eight nodes on a ring, one token each. The ring is cut at eight random points, and each node owns the arc ending at its cut. Random cut points don't make equal arcs.

@math heading="8 nodes, V = 1, seed 5" items="equal share = 1/8 = 12.50%@twelve and a half;;largest = 28.29% = 2.263 × mean@twenty eight point two nine;;smallest = 2.95% = 0.236 × mean@two point nine five"
An equal share would be twelve and a half percent. On the drawn ring, the largest node took twenty eight point two nine percent, two point two six three times the mean. The smallest took just two point nine five percent.

@words text="The shares sum to 1" sub="nothing is missing, they just aren't equal"
And yes, the shares add to one. They always do, that's what makes them shares. That checks nothing was lost. It isn't evidence of balance. What consistent hashing gives you is stability under growth, not balance.

@chapter Virtual nodes
@art many-token-ring
The fix is virtual nodes, or tokens. Give each physical node V positions on the ring. Its share is now the total length of V arcs, and sums of independent draws concentrate. Keys still go to the first token at or after their position, clockwise.

@chapter Two ways to measure
@art share-bars
There are two numbers for how uneven the shares are. Max over mean is what the fullest node costs you, and it's the number a capacity plan needs. The relative spread, the root mean square deviation over the mean share, is the one that falls at a clean rate.

@math heading="8 nodes, 8 seeds" items="V = 1:   max/mean 3.349   spread 1.0370   1/√V 1.0000@at one token;;V = 10:   max/mean 1.520   spread 0.3309   1/√V 0.3162@at ten;;V = 100:   max/mean 1.141   spread 0.0959   1/√V 0.1000@at a hundred"
At one token, max over mean is three point three four nine and the spread is one point oh three seven. At ten, one point five two and point three three oh nine. At a hundred, one point one four one and point oh nine five nine. The last column is one over root V, stated, and the measurements track it to about five percent.

@art sqrt-curve
So the spread falls like one over the square root of V, not one over V. Halving it costs four times the tokens. A tenth of it costs a hundred times. A hundred times the tokens buys ten times the evenness.

@chapter The two don't go to the same place
@art max-floor
And the spread goes to zero, but max over mean goes to one, never below. At a hundred tokens, the spread is about a tenth of what it was, but the fullest node is still fourteen percent over the mean. A tenth of the spread isn't a tenth of the imbalance.

@math heading="100 000 req/s on 8 nodes" items="fair share = 12 500 /s@twelve thousand five hundred;;V = 1:  busiest takes 28 290 /s@twenty eight thousand two hundred and ninety;;V = 100:  worst node ≈ 1.141 × mean@a fourteen percent margin"
Put a hundred thousand requests a second on that one token ring. A fair share is twelve thousand five hundred, but the busiest node takes twenty eight thousand two hundred and ninety. At a hundred tokens, the worst node averages one point one four one times the mean, a fourteen percent margin instead of a hundred and twenty six percent.

@chapter What a token costs
@art ring-table-cost
Tokens aren't free. Each one is a ring entry that routers, clients and the membership protocol all carry, and the lookup is over N times V entries. Eight nodes at a hundred tokens is eight hundred rows, nothing. A thousand nodes at a thousand tokens is a million.

@list heading="What tokens don't fix" items="What moves when a node joins@what moves|A single hot key@a single hot key"
And two things tokens don't change. They don't change what moves when a node joins, which is still roughly one over N plus one of the keys. And they do nothing for a single hot key, which sits in one arc however finely you cut the ring.

@chapter Where people slip
@list heading="Common slips" items="Shares sum to one, so it's balanced@The first|Expecting V tokens to divide the spread by V@The second|Reading the spread as max/mean@the third"
The first slip is believing a ring is balanced because the shares sum to one. The second is expecting V tokens to divide the spread by V. And the third is quoting the falling spread in a capacity conversation, when capacity is bought against max over mean.

@chapter Try it
@words text="8 nodes, V = 25" sub="first move: 1/√25 = 0.2000"
Your turn. Stay at eight nodes and take V to twenty five. The stated rate is one over root twenty five, point two. Predict the spread the lab will report, then check how far off you were. Then predict whether max over mean lands nearer one point five two or one point one four one, and say why that's a different question.

@end text="More tokens, slower gains"
You can add tokens to the ring and watch both numbers fall, on Learn. That's learn dot get er done dot I O.
