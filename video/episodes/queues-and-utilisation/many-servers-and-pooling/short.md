---
format: short
lesson: queues-and-utilisation/many-servers-and-pooling
title: One shared queue, nearly six times less waiting
---

@art separate-vs-pooled
Four servers, four separate lines. Or one line for all four. Same load. Does it matter?

@math items="four separate queues:  3 s@separate;;one pooled queue:  27/53 s ≈ 0.51 s@pooled"
At three quarters utilisation, each separate queue waits three seconds. The pooled queue waits twenty seven fifty thirds of a second, about half a second. Nearly six times less.

@words text="A separate queue can sit idle while another waits"
Separate lines waste every moment one server is free while another line isn't.

@end text="Full lesson on Learn"
The full lesson, with both arrangements side by side, is on Learn.
