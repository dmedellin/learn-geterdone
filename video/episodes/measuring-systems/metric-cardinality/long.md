---
format: long
lesson: measuring-systems/metric-cardinality
title: Metric cardinality: one more label multiplies everything
thumb: A label is a multiplier
---

@chapter Not one series
@title text="Metric Cardinality" sub="Measuring Systems" art=thumb
It's one more label on the metric. That's how it gets said in review. A label isn't a column. It's a multiplier, and one label can multiply your whole metrics bill by ten thousand.

@art series-grid
A time series is identified by a metric name plus a complete set of label values. So a labelled metric isn't one series. It's one series for every distinct combination of values that has ever been seen.

@art label-product
The cardinality of a label is how many values it takes. The series count is at most the product of the cardinalities. Real systems reach some fraction of it, but the product is what you plan against.

@chapter Five ordinary labels
@math heading="Series" items="service 40 × endpoint 120 × status 6 × instance 30 × method 4@forty services;;= 3 456 000 series@three million"
Forty services, a hundred and twenty endpoints, six status classes, thirty instances, and four methods. Each is reasonable on its own. Multiply them, and that's three million four hundred and fifty six thousand series, for one metric family.

@math heading="Storage at a 15 s scrape" items="86 400 / 15 = 5 760 samples per day per series@five thousand seven hundred and sixty;;× 2 bytes per sample@two bytes;;3 456 000 × 5 760 × 2 = 39.81 GB per day@thirty nine point eight one"
At a fifteen second scrape, each series is written five thousand seven hundred and sixty times a day. At two bytes a sample, that's thirty nine point eight one gigabytes a day, about fourteen and a half terabytes a year.

@chapter The sixth label
@art one-more-label
Now add a sixth label. Region and zone, at fifty values, multiplies everything by fifty, about two terabytes a day. Large, but survivable.

@math heading="The sixth label" items="× customer (500):  19.91 TB/day@a customer label;;× user_id (10 000):  34 560 000 000 series,  398.13 TB/day@A user id at ten thousand;;× request_id (10⁶):  39 813 TB/day@a request id"
A customer label at five hundred gives nineteen point nine one terabytes a day. A user id at ten thousand gives thirty four and a half billion series, three hundred and ninety eight terabytes a day. And a request id is worse still.

@words text="Unbounded is a different kind of number"
A request id isn't a big number. It's unbounded. It grows with traffic, and every series is written once and then kept for the retention period. A metric with an unbounded label is a log with the worst possible storage engine.

@art templated-path
The sneaky version is a URL path. Endpoint equals users slash one two three four five slash orders has a cardinality of the number of users. The templated route, users slash id slash orders, has cardinality one. If you can't state a label's cardinality without querying production, it's probably unbounded.

@chapter Where the pain arrives
@art index-memory
The bytes on disk are the easy part. Every series needs an index entry, usually held in memory, and consulted on every query. A panel that was fast at three thousand series doesn't get slow at three million. It times out. And histogram buckets are label values too, so finer buckets draw from this same budget. Resolution in the tail and the labels you can afford come out of one account.

@art churn
And series that stop being written don't stop costing. An instance label that changes on every deploy adds a fresh set each release, and the old ones stay in the index until they age out. That's churn, and it's why a correctly sized system falls over three months later.

@words text="Bucket · move to logs · template · bound"
What to do instead. Bucket the label, so status is four classes, not sixty codes. Move high cardinality identifiers to logs and traces. Template anything from a path. And bound what you can't template, with an allow list and an other value.

@chapter Where people slip
@list heading="Common slips" items="Treating a label as a field, not a multiplier@The first|Pricing the bytes and forgetting the index@The second|Assuming a dead series stops costing@the third"
The first slip is treating a label as a field rather than a multiplier. The second is pricing the bytes and forgetting the index. And the third is assuming a series stops costing when it stops being written.

@chapter Try it
@words text="30 s scrape,  + region × zone (50)" sub="first move: 3 456 000 × 50"
Your turn. Keep the five labels, set the scrape to thirty seconds, and add region and zone at fifty. The series count is three million four hundred and fifty six thousand times fifty. Work out the daily bytes, and say which change your storage will notice first.

@end text="Multiply before you ship the label"
You can add labels and watch the series count multiply, on Learn. That's learn dot get er done dot I O.
