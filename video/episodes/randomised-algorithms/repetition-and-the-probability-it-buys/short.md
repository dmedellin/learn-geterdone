---
format: short
lesson: randomised-algorithms/repetition-and-the-probability-it-buys
title: Ten runs turn 37% into 99%
---

@art independent-runs
This algorithm finds the right answer only thirty seven per cent of the time. Run it ten times.

@math items="one run:  13/35 ≈ 0.37@one run;;all 10 fail:  (22/35)¹⁰ ≈ 0.0096@all ten"
One run of Karger's algorithm on the bridge graph succeeds thirteen thirty fifths of the time. Keep the best of ten independent runs. All ten fail with probability twenty two thirty fifths to the tenth, under one per cent.

@words text="Failures multiply"
Successes don't add up. Failures multiply.

@end text="Full lesson on Learn"
The full lesson is on Learn.
