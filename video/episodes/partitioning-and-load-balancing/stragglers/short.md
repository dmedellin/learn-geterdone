---
format: short
lesson: partitioning-and-load-balancing/stragglers
title: The half-percent tail that becomes your p99
---

@art wait-for-all
A partition is slow only half a percent of the time. At three partitions, that's your p ninety nine.

@math items="N = 2:  0.995² = 0.990025@At two;;N = 3:  0.995³ = 0.985075@At three"
A job waits for its slowest partition. The chance that all of them are fast is point nine nine five to the N. At two, that's still above point nine nine. At three, it falls below.

@words text="The job runs at the speed of its slowest part"
So the rare slow outcome, four hundred milliseconds, becomes the job's p ninety nine.

@end text="Full lesson on Learn"
The full lesson, with the whole table, is on Learn.
