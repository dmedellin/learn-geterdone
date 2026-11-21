---
format: long
lesson: latency-and-the-tail/latency-budgets
title: Latency budgets: allocate backwards from the objective
thumb: Start from the promise
---

@chapter The question
@title text="Latency Budgets" sub="Latency and the Tail" art=thumb
You've promised a p ninety nine of four hundred milliseconds across four stages. Does the plan fit? You can find out before anyone writes a line of code, and the answer usually names the stage that can't.

@art top-down
A budget is built from the objective downwards, not from the stages upwards. Start with the number you promised. Subtract everything no code can remove. What's left is all the code may spend. Build it the other way and you only ever report what the system already does.

@chapter Subtract the floors
@math heading="SLO: p99 ≤ 400 ms" items="− light-speed floor, NY–London: 56 ms@fifty six;;− 2 handshake round trips × 76 ms: 152 ms@two sequential round trips;;available for the code: 192 ms@a hundred and ninety two"
The route has a light speed floor of fifty six milliseconds, New York to London, rounded. The connection costs two sequential round trips at a measured seventy six, so a hundred and fifty two. Those aren't negotiable. That leaves a hundred and ninety two milliseconds for the code.

@art floors-eaten
That's two hundred and eight milliseconds of a four hundred millisecond objective gone before a line of code is considered. More than half. It belongs to physics and protocol, and it's why a four hundred millisecond promise across the Atlantic is much tighter than it sounds.

@chapter Share and residual
@art stage-boxes
Four stages share what's left: a gateway, auth, search and render.

@math heading="Even share: 192 / 4 = 48 ms" items="gateway: floor 8 → residual +40@gateway;;auth: floor 20 → +28@auth;;search: floor 150 → −102@search;;render: floor 40 → +8@render"
Divide by four stages, and each gets forty eight. A stage's residual is its share minus its own floor. For the gateway, the floor is eight, so its residual is plus forty. Auth, plus twenty eight. Search has a floor of a hundred and fifty, so its residual is minus a hundred and two. Render, plus eight.

@words text="residual < 0: cannot fit under any implementation"
A positive residual is headroom a stage can release to another. A negative one is a stage that can't meet its allocation under any implementation. That's the finding, not a failure of the method.

@chapter Check it both ways
@math heading="Shortfall, two ways" items="192 − (8 + 20 + 150 + 40) = 192 − 218 = −26 ms@floors total;;spare 40 + 28 + 8 = 76, need 102@spare;;76 − 102 = −26 ms  ✓@agree"
Count the shortfall two ways. The floors total two hundred and eighteen, and a hundred and ninety two minus two hundred and eighteen is minus twenty six. The spare from the stages that fit is seventy six, and search needs a hundred and two. Seventy six minus a hundred and two is also minus twenty six. They agree. The plan is infeasible by twenty six milliseconds, and search is the stage.

@art even-split
The even split is a diagnostic, not a design. Nobody thinks a gateway and a search engine deserve the same forty eight milliseconds. It's there because it shows, in one line, which stage the objective can't hold.

@chapter Four ways out
@list heading="What each option buys" items="Raise the SLO to 500 ms: +74 ms@raise the objective|Drop the two handshakes: +126 ms@remove a floor|Search floor 100 ms: +24 ms@make search cheaper|Take work off the critical path@take work off"
The arithmetic prices each fix. Raise the objective to five hundred, and the overall residual becomes plus seventy four. Remove a floor, dropping the two handshakes, and it's plus a hundred and twenty six. Make search cheaper, at a hundred milliseconds, and it's plus twenty four. Or take work off the critical path, which is a graph question.

@art subsidy
Look at that third option. The plan is now feasible, but search is still fifty two above the even share. It only fits because the other three stages are subsidising it. The even split makes that visible.

@chapter Percentiles all the way down
@art budget-scale
If the objective is a p ninety nine, every figure in the table must be a p ninety nine. Budget in means, and it'll fit comfortably and be violated on slow requests. And once you've filled in a p ninety nine per stage, don't add them up and call that the end to end p ninety nine. Compute it by convolution and check.

@chapter Where people slip
@list heading="Common slips" items="Budgeting upward from current costs@The first|Budgeting in means@The second|Leaving the floors out@The third"
The first slip is building the budget upward from what stages cost today. That gives a total, not a budget. The second is budgeting in means when the objective is a percentile. And the third is leaving the fixed floors out, or discovering them last.

@chapter Try it
@words text="SLO 350 ms · floor 40 ms · 1 round trip of 76 ms" sub="available: 350 − 116 = 234 ms"
Your turn. Same four stages, an objective of three hundred and fifty, a forty millisecond floor, and one round trip of seventy six. The available time is two hundred and thirty four. Compute the even share, the four residuals, and the shortfall both ways. Does it fit?

@end text="Allocate from the promise down"
You can change the objective, the floors and the stages and watch every residual, on Learn. That's learn dot get er done dot I O.
