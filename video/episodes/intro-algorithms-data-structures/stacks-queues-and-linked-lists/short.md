---
format: short
lesson: intro-algorithms-data-structures/stacks-queues-and-linked-lists
title: Why a circular queue wastes one slot
---

@art circular-queue
A queue in n slots can only ever hold n minus one items. Here's why.

@math items="empty: head = tail@empty;;if full also had head = tail…@If you filled"
The queue is empty when head equals tail. If you filled every slot, the tail would wrap round onto the head again, and full would look exactly like empty.

@words text="Leave one slot unused"
So full means the tail is one step behind the head. One slot always stays empty.

@end text="Full lesson on Learn"
Run a queue round its array in the full lesson on Learn.
