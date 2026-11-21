---
format: short
lesson: measuring-systems/percentiles-do-not-average
title: Your average p99 is below your median
---

@art average-summaries
Average three hosts' p ninety nines, and you can land below the fleet's median.

@math items="host p99s 12, 14, 400 ms  →  mean 142 ms@a hundred and forty two;;merged:  p99 400 ms,  p50 180 ms@merge the requests"
Three hosts report twelve, fourteen and four hundred milliseconds. The average is a hundred and forty two. But merge the requests, and the fleet p ninety nine is four hundred, and the median is a hundred and eighty.

@words text="Merge the requests, then take the percentile"
The busy host served ninety of the hundred requests.

@end text="Full lesson on Learn"
The full lesson, with requests you can move, is on Learn.
