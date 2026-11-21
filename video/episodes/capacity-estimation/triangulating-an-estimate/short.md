---
format: short
lesson: capacity-estimation/triangulating-an-estimate
title: The estimate check that can never fail
---

@art cancelling-factor
Your two estimates agree perfectly. That might mean you checked nothing.

@math items="A = users · photos · 2 MB@route A;;B = objects · 2 MB@route B;;A / B = 1, for any 2 MB@exactly one"
If route A and route B both multiply by the same assumed two megabytes per photo, that factor cancels out of their ratio. The ratio comes out exactly one, whatever the true size is.

@words text="A check must be able to fail"
A real check shares no factor with the first route, so it can fail.

@end text="Full lesson on Learn"
The full lesson, with the shared factor on a slider, is on Learn.
