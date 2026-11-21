---
format: short
lesson: latency-and-the-tail/round-trips-not-bytes
title: Halving your HTML saved 5.6 milliseconds
---

@art handshake-chain
Want a faster first page load? Stop shrinking the HTML.

@math items="k = 5:  5 × 80 = 400 ms@five round trips;;14 kB at 10 Mbit/s = 11.2 ms@fourteen kilobyte"
A cold connection makes five round trips before the answer starts: DNS, TCP, two for TLS one point two, and the request. At eighty milliseconds each, that's four hundred. The fourteen kilobyte page costs eleven point two.

@words text="Halve the HTML: 5.6 ms · Drop a handshake: 80 ms"
Halving the HTML saves five point six milliseconds. Removing one handshake saves eighty.

@end text="Full lesson on Learn"
The full lesson, with every handshake on a switch, is on Learn.
