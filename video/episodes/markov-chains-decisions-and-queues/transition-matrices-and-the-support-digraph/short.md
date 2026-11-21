---
format: short
lesson: markov-chains-decisions-and-queues/transition-matrices-and-the-support-digraph
title: The matrix check that passes and is still wrong
---

@art bad-row
Your transition matrix adds up perfectly, and it still isn't a Markov chain.

@words text="Each row must sum to 1"
Every row is a distribution, where the chain goes next from that state. So each row must sum to exactly one.

@art matrix-rows
One row over by a quarter, another under by a quarter, and the total looks fine. Check row by row, or every answer after it means nothing.

@end text="Full lesson on Learn"
The full lesson, with your own matrix, is on Learn.
