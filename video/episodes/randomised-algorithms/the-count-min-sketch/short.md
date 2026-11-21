---
format: short
lesson: randomised-algorithms/the-count-min-sketch
title: Counting a stream with a tiny grid of counters
---

@art counter-grid
Count a whole stream of keys in a few dozen counters, and never undercount.

@art one-key-rows
Each key bumps one counter per row. Other keys can only add to those counters, never subtract. So the smallest of a key's counters is never below its true count.

@words text="key 1: estimate 42, true 40"
On the lab's stream of sixty four updates, the heavy hitter reads forty two against a true forty.

@end text="Full lesson on Learn"
The full lesson on the Count-Min sketch is on Learn.
