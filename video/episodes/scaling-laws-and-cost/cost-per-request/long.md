---
format: long
lesson: scaling-laws-and-cost/cost-per-request
title: Cost per request: it's probably the bytes going out
thumb: Egress is the biggest line
---

@chapter Four terms
@title text="Cost per Request" sub="Scaling Laws and Cost" art=thumb
Your cloud bill is too high. Where do you look first? Most teams start with compute, because that's what their dashboards show. On a typical profile, it's one of the smallest lines.

@art four-terms
Break the cost of one request into four terms. A fixed monthly charge, like load balancers, a minimum fleet and licences, shared out over the volume. Compute, the work the request does. Storage, the bytes it leaves behind, for as long as they're kept. And egress, the bytes sent back to the caller.

@math heading="Cost per request" items="F/V + c + b·R·p_s/10⁹ + e·p_e/10⁹@F over V;;only F/V depends on V@only the first"
That's F over V, plus compute, plus bytes stored times retention times the storage price, plus bytes out times the egress price. Only the first term depends on volume.

@chapter A real-looking bill
@math heading="500 000 000 requests a month" items="fixed  $4 000 ÷ 5×10⁸ = $0.00000800   39.3%@fixed charge;;compute  $0.00000100   4.9%@compute is;;storage  2 kB × 12 months → $0.00000055   2.7%@storage is;;egress  120 kB × $0.090/GB → $0.00001080   53.1%@egress is"
Take five hundred million requests a month. The fixed charge is four thousand dollars, eight millionths of a dollar a request, thirty nine point three percent. Compute is one millionth, four point nine percent. Storage is two kilobytes kept a year, point five five millionths, two point seven percent. And egress is a hundred and twenty kilobytes out, ten point eight millionths, fifty three point one percent.

@art egress-out
Egress is more than half the bill, sixty thousand gigabytes out the door, five thousand four hundred dollars a month. That's ten point eight times the compute. It's a property of the response body, not the code, so nobody sizes it.

@words text="$10 176 a month" sub="4 000 + 500 + 276 + 5 400"
Add the four monthly figures, four thousand, five hundred, two seventy six, and five thousand four hundred, and you get ten thousand one hundred and seventy six dollars. Multiply the unit cost by the volume, and you get the same. That check catches units errors in the byte terms.

@chapter Unit cost falls, bill rises
@art fixed-falls
Only the fixed term falls as traffic grows. The other three are flat per request. So the unit cost falls toward a floor made of those three.

@math heading="At ten times the volume" items="fixed → $0.00000080@eight tenths of a millionth;;unit cost → $0.00001315@thirteen point one five;;monthly bill → $65 760@sixty five thousand"
At ten times the volume, the fixed term falls to eight tenths of a millionth, and the unit cost to thirteen point one five millionths. And the monthly bill rises to sixty five thousand seven hundred and sixty dollars.

@art bill-rises
Both are true at once. One has V on the bottom, the other has V on top. So cost scales with users gets the total right and the unit cost exactly backwards. And a cost per request without its volume isn't a number you can compare.

@chapter Which term to chase
@art crossing-terms
When does the fixed term stop being the biggest? When F over V equals the egress per request. That's four thousand over ten point eight millionths, three hundred and seventy million, three hundred and seventy thousand, three hundred and seventy requests a month. Below it, chase the fixed cost. Above it, the response body.

@art retention-stack
And storage accrues with retention, not traffic. Keep the data two years instead of one, and that term doubles to five hundred and fifty two dollars a month, with exactly the same traffic.

@words text="Halving compute saves $250" sub="$5 400 sits in egress"
So on this profile, halving compute saves two hundred and fifty dollars a month, while five thousand four hundred sits in egress. Smaller payloads, compression on the wire, or caching closer to the caller.

@chapter Where people slip
@list heading="Common slips" items="Reading “cost scales with users” as one claim@The first|Optimising the term your tools measure@The second|Quoting a unit cost without the volume@the third"
The first slip is reading cost scales with users as one claim, when it's two pointing opposite ways. The second is optimising the term your tools measure. And the third is quoting a cost per request without the volume.

@chapter Try it
@words text="60 kB out,  24 months kept" sub="predict each term first"
Your turn. Halve the response to sixty kilobytes, and double the retention to twenty four months. Predict the direction and rough size of each term first. Then read the unit cost, the monthly total, and the new biggest term off the lab.

@end text="Decompose, then chase the biggest"
You can move each term and watch the shares change, on Learn. That's learn dot get er done dot I O.
