---
format: short
lesson: measuring-systems/how-long-to-run-a-load-test
title: Your one minute load test can't see its p99.9
---

@art short-run
Six hundred requests, and a p ninety nine point nine in the report. It's probably just the maximum.

@math items="1 − (999/1000)⁶⁰⁰ = 45.14%@forty five;;95% needs n = 2 995@two thousand nine hundred and ninety five"
The chance a six hundred request run meets the slowest tenth of a percent at all is forty five point one four percent. For ninety five percent confidence, you need two thousand nine hundred and ninety five requests.

@words text="And ten times that to measure it"
That's only enough to meet the tail once.

@end text="Full lesson on Learn"
The full lesson, with the exact scan, is on Learn.
