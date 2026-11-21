---
format: short
lesson: code-complete-code-improvements/code-tuning-techniques
title: Same loop change, 34% faster in Java, 4% in Python
---

@art stopwatch-pair
One loop change: a third faster in Java, four percent in Python.

@math items="100 × 5 → 600 passes@six hundred;;5 × 100 → 505 passes@five oh five"
Put the busiest loop inside. A hundred outside and five inside makes six hundred passes. Swapped, it's five oh five.

@words text="C++ 33% · Java 34% · PHP 12% · Python 4%"
The book timed that swap. Thirty three percent in C plus plus, thirty four in Java, twelve in PHP, four in Python. Count, then measure.

@end text="Full lesson on Learn"
The full lesson, with a nest lab, is on Learn.
