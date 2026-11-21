---
format: long
lesson: caching-and-hit-rates/cdn-egress-and-origin-load
title: CDN egress: why the request hit rate halves your bill forecast
thumb: Billed in bytes, not requests
---

@chapter The question
@title text="CDN Egress and Origin Load" sub="Caching and Hit Rates" art=thumb
Your CDN dashboard says fifty eight percent of requests are served from the edge. So your origin egress bill should be about forty two percent of the total, right? It's nearly twice that. Here's why.

@art edge-ring
A CDN is billed in bytes, for what leaves the origin. So the hit rate that decides the invoice is a byte hit rate, the share of bytes served from the edge, not the share of requests.

@art small-and-large
And on most edge workloads, the popular objects are the small ones. The cheap hits are the cheap ones.

@chapter Two hit rates
@math heading="Top C of N objects" items="p_i ∝ 1/iˢ · size_i ∝ i^b@popularity;;request hit = share of requests from the top C@the request hit rate;;byte hit = Σ i^(b−s) over top C ÷ Σ i^(b−s) over all@the byte hit rate"
Popularity is Zipf, one over i to the s. Size grows with rank as i to the b. The request hit rate is the share of requests the top C serve. The byte hit rate weights each rank by its size, so it's the same harmonic ratio, with the exponent b minus s.

@list heading="Three cases" items="b = 0: same size, byte = request@b equals zero|b = s: every rank equal bytes, byte = C/N@b equals s|b > 0: popular is small, byte < request@b is greater than zero"
That gives three cases. When b equals zero, every object is the same size, and the two rates are equal. When b equals s, every rank carries the same bytes, so the byte rate is just C over N. And when b is greater than zero, popular objects are smaller, so the byte rate falls below the request rate.

@chapter Twenty objects
@math heading="N = 20, s = 1, C = 4, b = 1" items="request hit = H(4,1)/H(20,1) = 57.91%@fifty seven point nine one;;b = s  →  byte hit = C/N = 4/20 = 20.00%@twenty percent;;gap = 37.91 points@thirty seven point nine one"
Take twenty objects, s equals one, the edge holding the top four, and size proportional to rank. The request hit rate is H of four over H of twenty, fifty seven point nine one percent. But b equals s, so the byte hit rate is four over twenty, exactly twenty percent. A gap of thirty seven point nine one points.

@art two-profiles
Push the sizes harder, b equals two, and the byte hit rate falls to four point seven six percent, while the request rate stays at fifty seven point nine one. The edge serves over half the requests, and a twentieth of the bytes.

@chapter The invoice
@math heading="50 000 GB/day at 2¢/GB" items="origin = (1 − 0.20) × 50 000 = 40 000 GB/day@forty thousand;;bill = 40 000 × 30 × $0.02 = $24 000.00@twenty four thousand"
Origin egress is one minus the byte hit rate, times total bytes. At fifty thousand gigabytes a day and a twenty percent byte rate, forty thousand still leave the origin. At two cents a gigabyte over thirty days, that's twenty four thousand dollars.

@math heading="Billed from the wrong rate" items="origin ≈ (1 − 0.5791) × 50 000 ≈ 21 047 GB/day@the request hit rate;;bill ≈ $12 627.98@twelve thousand"
Now use the request hit rate instead. You'd predict about twenty one thousand and forty seven gigabytes a day, and a bill of about twelve thousand six hundred and twenty eight dollars. Barely half the real invoice.

@art bill-stack
That's nearly twice the bill, from using the number that was right there on the dashboard.

@art optimistic-plan
And the error is one sided. Edge workloads normally have b above zero, so the request rate always underestimates origin egress. The same gap hits the origin's capacity. A link and a fleet sized for twenty one thousand gigabytes meet forty thousand on the day the video catalogue gets popular.

@chapter What to do about it
@art segments
Two moves change the byte rate directly. Cache by bytes served, admitting large popular objects even though they cost more slots. And split large objects into range cacheable pieces, so one big miss becomes many small hits. That's why video is served in segments.

@words text="Real catalogues are lumpy" sub="measure the byte hit rate itself"
One caution. Size proportional to i to the b is smooth, and real catalogues are lumpy. Use the model for the direction and the rough size of the gap, and measure the byte hit rate before you budget.

@chapter Where people slip
@list heading="Common slips" items="Using the request hit rate to forecast egress@The first|Assuming the two rates must be close@The second|Mixing decimal and binary gigabytes@The third"
The first slip is forecasting egress from the request hit rate. The second is assuming the two rates must be close. At b equals two, they're a factor of twelve apart. The third is mixing decimal and binary gigabytes. Egress is billed in decimal, and the difference is about seven percent.

@chapter Try it
@words text="N = 20, s = 1, C = 4, b = 0" sub="the two rates must now be equal"
Your turn. Keep twenty objects and s equals one, but set b to zero. Confirm the two rates are now equal, then compute the origin egress and the bill. And say which case describes a video CDN, and which describes a cache of thumbnails.

@end text="Set b to zero and close the gap"
You can watch the share of requests and the share of bytes pull apart as you change the size profile, on Learn. That's learn dot get er done dot I O.
