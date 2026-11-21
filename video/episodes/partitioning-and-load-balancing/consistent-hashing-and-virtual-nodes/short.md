---
format: short
lesson: partitioning-and-load-balancing/consistent-hashing-and-virtual-nodes
title: A hundred times the tokens, only ten times as even
---

@art one-token-ring
Eight nodes on a hash ring. The biggest one owns more than twice its share.

@math items="V = 1:  spread 1.0370@one token;;V = 100:  spread 0.0959@a hundred tokens"
Give each node more tokens and the shares even out. But slowly. The spread goes from about one at one token, to about a tenth at a hundred tokens.

@words text="Spread falls like 1/√V"
A hundred times the tokens buys ten times the evenness.

@end text="Full lesson on Learn"
The full lesson, with the token count on a slider, is on Learn.
