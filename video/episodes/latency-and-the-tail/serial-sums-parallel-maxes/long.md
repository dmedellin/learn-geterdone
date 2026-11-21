---
format: long
lesson: latency-and-the-tail/serial-sums-parallel-maxes
title: Serial sums, parallel maxes: find the critical path
thumb: Only the longest path counts
---

@chapter The question
@title text="Serial Sums, Parallel Maxes" sub="Latency and the Tail" art=thumb
A request has seven stages, and their times add up to a hundred and twenty milliseconds. But the request takes ninety two. And making one of those stages instant changes nothing at all. Here's why.

@art series-parallel
There are only two rules. Stages that run one after another add their times. Stages that run beside each other, where both must finish, take the maximum. That's why a fan out of ten fast calls and one slow one costs what the slow one costs.

@chapter The preset
@art stage-graph
A gateway takes four milliseconds. Then two things start at once: authorisation at eighteen and a cache lookup at six. The database read, fifty five, needs both. An enrich step of twenty two needs only authorisation. Render, twelve, waits for the database and the enrichment, and respond takes three.

@words text="critical path = the longest path" sub="its length is the end-to-end time"
Put both rules together, and the end to end time is the longest path through the graph. That's the critical path. A stage on it has zero slack: any increase in its time increases the total by the same amount.

@chapter The forward pass
@math heading="Earliest start = largest finish it waits for" items="gateway 0 → 4@gateway;;authz 4 → 22,  cache 4 → 10@Authorisation;;enrich 22 → 44@Enrich"
Go stage by stage, recording when each can start: the largest finishing time among the stages it waits for. The gateway runs from zero to four. Authorisation runs from four to twenty two, and cache from four to ten. Enrich runs from twenty two to forty four.

@math heading="Where the paths meet" items="db starts at max(22, 10) = 22 → 77@The database;;render starts at max(77, 44) = 77 → 89@Render;;respond 89 → 92@respond"
The database starts at the larger of twenty two and ten, so twenty two, and ends at seventy seven. Render starts at the larger of seventy seven and forty four, and ends at eighty nine. And respond ends at ninety two.

@art critical-path
So the critical path is gateway, authorisation, database, render, respond. Ninety two milliseconds, not a hundred and twenty.

@chapter Slack
@math heading="Slack" items="cache: 22 − 10 = 12 ms@the cache;;enrich: 77 − 44 = 33 ms@the enrichment;;everything else: 0, critical@Everything else"
The cache finished at ten, but the database couldn't start until twenty two. That's twelve milliseconds of slack for the cache. The enrichment finished at forty four, and render didn't start until seventy seven, so it has thirty three. Everything else is critical.

@art slack-gap
Slack is the list of optimisations that change nothing. Drag enrich from twenty two milliseconds down to one, and the total stays at ninety two. Drag respond from three to two, and the total falls to ninety one. Enrich is the second largest stage and the least useful to improve. Rank by slack, not by duration.

@chapter The trap on the other side
@math heading="Speeding up the database" items="db 55 → 45:  total 92 → 82@forty five;;db → 22:  total 59@twenty two;;db → 10:  total still 59@ten"
Take the database from fifty five to forty five and the total falls from ninety two to eighty two, the full ten milliseconds. At twenty two, the total is fifty nine. Take it to ten, and it's still fifty nine. Below twenty two, the path through enrich has taken over.

@art path-switch
Shortening a critical stage pays in full only until a second path becomes the longest one.

@chapter Adding a dependency
@art new-edge
Now make the cache lookup wait for authorisation instead of running beside it. No stage got slower, but the total is now ninety eight. Make the database wait for enrich instead, and it's a hundred and fourteen, with the critical path rerouted. These arrive as refactors and correctness fixes, and they never show up in a profile.

@chapter Where people slip
@list heading="Common slips" items="Adding the stage times@The first|Optimising the largest stage@The second|Adding a dependency unnoticed@The third"
The first slip is adding the stage times, which here overstates by about thirty percent. The second is optimising the largest stage rather than a critical one. And the third is adding a dependency without noticing it's a latency change.

@chapter Try it
@words text="enrich → db: present" sub="db now starts at max(22, 44) = 44"
Your turn. Make the database wait for enrich. Its earliest start is now the larger of twenty two and forty four, which is forty four. Carry the forward pass through to respond, name the new critical path, and say which stage has just gained slack, and how much.

@end text="Rank stages by slack"
You can drag every stage and add dependencies and watch the critical path move, on Learn. That's learn dot get er done dot I O.
