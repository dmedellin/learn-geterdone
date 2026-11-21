---
format: short
lesson: caching-and-hit-rates/popularity-is-skewed
title: Five keys out of fifty carry ninety percent of the traffic
---

@art head-shaded
Cache a tenth of your keys, serve a tenth of your requests? Not even close.

@math items="H(5, 2) / H(50, 2) = 90.06%@the top five"
Under a Zipf law with exponent two, fifty keys, the top five carry ninety point oh six percent of the requests.

@words text="9.01× better than proportional"
That's nine times what their share of the catalogue suggests. A small cache isn't small at all when popularity is skewed.

@end text="Full lesson on Learn"
The full lesson, with the rank curve to drag, is on Learn.
