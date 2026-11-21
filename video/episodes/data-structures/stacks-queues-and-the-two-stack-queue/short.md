---
format: short
lesson: data-structures/stacks-queues-and-the-two-stack-queue
title: One dequeue cost four, and that's fine
---

@art pour-across
A queue built from two stacks has one dequeue that costs four times the rest.

@math items="E E E D D D@three enqueues;;1, 1, 1, 4, 1, 1 = 9@nine in total"
Three enqueues, three dequeues. The first dequeue pours three elements across, then pops, so it costs four. Nine in total.

@words text="Pushed once, moved once, popped once" sub="≤ 3 per arrival"
Every element is pushed once, moved once and popped once. So the total is at most three per arrival, however bad one step gets.

@end text="Full lesson on Learn"
The full lesson, with the credit balance running, is on Learn.
