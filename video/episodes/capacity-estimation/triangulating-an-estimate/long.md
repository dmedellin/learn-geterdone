---
format: long
lesson: capacity-estimation/triangulating-an-estimate
title: Triangulating an estimate: a check that can fail
thumb: Two routes, no shared factor
---

@chapter The question
@title text="Triangulating an Estimate" sub="Capacity Estimation" art=thumb
How do you check an estimate? Not by redoing it. Redoing the arithmetic can only find arithmetic slips, and the arithmetic was never where the uncertainty lived. An assumption can only be tested against evidence that didn't come from it.

@art two-routes
So you triangulate. You compute the same quantity by a second route whose factors are independent of the first, so no factor appears in both chains. Then you compare the two answers by their ratio. Route A and route B have to arrive at the same quantity through different data. That's the only property that makes the second one informative.

@chapter Two routes
@math heading="Route A: from the people" items="500 000 uploaders@five hundred thousand;;× 20 photos per day@twenty photos;;× 2 000 000 B per photo@two megabytes;;= 2.0·10¹³ B/day@two times ten to the thirteen"
Say you want bytes uploaded per day. Route A goes from people: five hundred thousand daily uploaders, times twenty photos each, times an assumed two megabytes per photo. That's two times ten to the thirteen bytes a day.

@math heading="Route B: from the object store" items="10 000 000 objects per day@ten million;;× 1 800 000 B measured on disk@one point eight;;= 1.8·10¹³ B/day@one point eight times ten to the thirteen"
Route B goes from the object store: ten million objects written a day, times a mean size of one point eight megabytes, measured on disk. That's one point eight times ten to the thirteen bytes a day.

@chapter Do they agree?
@math heading="Compare by ratio" items="A / B = 20/18 = 10/9 ≈ 1.1111@ten ninths;;band ÷8 … ×8@the band;;1/8 ≤ 10/9 ≤ 8  →  agree@inside"
The ratio is twenty over eighteen, ten ninths. Is that agreement? It depends on the band, the half-width the inputs earned. Three factors at a factor of two give divide by eight up to times eight. Ten ninths is well inside, so the routes agree.

@art band-check
Agree means inside the band, not close. Against factors known to a few percent, the same ten ninths would be a serious disagreement. And fix the band before you compare, from the inputs. Widening it after seeing the ratio makes the check unfailable after the fact.

@chapter The sabotaged check
@art sabotage
Now watch what happens when the second route quietly borrows a factor from the first. It's a common way for a check to go wrong.

@math heading="Route B borrows route A's 2 MB" items="10 000 000 × 2 000 000 = 2.0·10¹³@two megabytes;;A / B = 1  exactly@exactly one;;for any value of the shared factor@any value"
Now give route B the assumed two megabytes per photo, instead of the measured one point eight. Both routes say two times ten to the thirteen. The ratio is exactly one. It looks better than before. But it's worth nothing, because it stays at one for any value of that shared factor.

@art cancelling-factor
A factor that appears in both products divides out of their quotient. So no value of it could ever make the check fail. An agreement that nothing could have broken has tested nothing.

@chapter Invisible from the inside
@art slider-frozen
A fake check doesn't feel like a failure. It feels like an unusually clean result. So the test is mechanical: list the factors of both chains and look for a name that appears twice. If one does, say that factor remains untested, rather than reporting the ratio.

@chapter When they disagree
@art suspects
A disagreement outside the band is the useful outcome. It means an assumption is wrong. The suspects are the factors the routes don't share, and the one they disagree about most is the one to go and measure. Rechecking the multiplication is the wrong response.

@words text="Build route B before you look at route A again"
One more rule. Build the second route before looking at the first answer again. A route built with the target in mind will reach it, through small, defensible choices, and that agreement is as empty as a shared factor.

@chapter Where people slip
@list heading="Common slips" items="A second route that shares a factor@The first|Judging agreement by closeness@The second|Treating disagreement as a mistake@The third"
The first slip is calling a second route a check when it shares a factor. The second is deciding agreement by how close the numbers look, instead of by the band. And the third is treating a disagreement as an arithmetic slip, when it's the most valuable thing the estimate can tell you.

@chapter Try it
@words text="users × sessions × requests per session" sub="vs log sessions × log requests per session"
Your turn. Requests a day: daily users times sessions each times requests per session, against sessions counted in the access log times requests per session counted in the log. Fix the band first. Then decide whether the two routes are really independent.

@end text="Drag the shared factor"
You can drag the assumed size and watch one route move while the other stays put, on Learn. That's learn dot get er done dot I O.
