---
format: short
lesson: measuring-systems/histograms-and-bucket-error
title: Your histogram p99 is a factor of two wide
---

@art interval-not-point
The true p ninety nine is a hundred and thirty seven milliseconds. Your histogram can only say a hundred to two hundred.

@math items="relative width = r − 1@r minus one;;r = 2:  100%@a hundred percent"
With geometric buckets, each one's relative width is r minus one. Buckets that double give a hundred percent, so every percentile is known only to within a factor of two.

@words text="More traffic won't narrow it. Finer buckets will."
It's not noise, so waiting longer doesn't help.

@end text="Full lesson on Learn"
The full lesson, with the boundaries on a slider, is on Learn.
