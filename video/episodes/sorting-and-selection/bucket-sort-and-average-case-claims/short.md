---
format: short
lesson: sorting-and-selection/bucket-sort-and-average-case-claims
title: Same bucket sort, six times the work
---

@art one-bucket
Same code, the same number of keys, and six times the work.

@math items="uniform keys:  90@Spread uniformly;;clustered keys:  592@clustered"
Spread uniformly, the keys cost ninety comparisons. Clustered in a twentieth of the range, they all land in one bucket, and cost five ninety two.

@words text="Expected over the data, not the coins"
Bucket sort's linear time assumes the keys are uniform. When they aren't, nothing in the algorithm can notice.

@end text="Full lesson on Learn"
The full lesson, with three distributions, is on Learn.
