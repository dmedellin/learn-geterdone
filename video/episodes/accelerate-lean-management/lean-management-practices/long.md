---
format: long
lesson: accelerate-lean-management/lean-management-practices
title: WIP limits alone don't predict much. Here's what does.
thumb: Limits alone aren't enough
---

@chapter Managing software work
@title text="Lean Management Practices" sub="Accelerate, Chapter 7" art=thumb
Chapter seven opens with a short history of managing software work: project and program management, the Agile methods after twenty oh one, and the Lean movement, from Toyota, adapted for software by Mary and Tom Poppendieck. Then it asks how Lean practices drive delivery performance.

@list heading="Lean management, three components" items="Limit work in progress@capping work in progress|Visual displays of work and quality@visual displays|Decide daily with monitoring data@monitoring"
The authors modelled Lean management with three components. Capping work in progress, and letting the cap drive improvement. Keeping visual displays of the work's status and of key quality measures, open to engineers and leaders alike. And deciding by the day with data from application and infrastructure monitoring.

@chapter The surprise
@quote text="WIP limits on their own do not strongly predict delivery performance." cite="Forsgren, Humble and Kim, Accelerate, Chapter 7"
And here's the finding the lesson turns on. WIP limits on their own do not strongly predict delivery performance.

@art three-together
Only when limits are combined with visual displays, and a feedback loop from production monitoring back to the teams or the business, do the authors see a strong effect. With all three together, the effect on delivery is far larger.

@chapter What they measured
@art obstacle-visible
How they measured it explains why. The survey didn't only ask whether a team limits its work in progress. It asked whether the limits bring obstacles to flow into view, and whether the team clears them by improving the process, so throughput rises. A limit nobody acts on isn't what they measured.

@art visual-board
For visual displays it asked what's shown, to whom, and how easily it can be had. Visibility, and the communication it enables, are in their words the key.

@words text="Less burnout · a more generative culture"
The practices together raise delivery performance, they report, and also go with less burnout and a more generative culture. Throughout, the word is predict: a statistical relationship in their survey, with the survey's limits.

@chapter Little's law
@art wip-limit
So what does a limit do, arithmetically? A limit caps how many items can be in progress at once. Everything else waits outside until something finishes.

@math heading="Little's law" items="lead time = WIP ÷ throughput@lead time is;;18 in progress ÷ 2 a day = 9 days@eighteen;;limit of 6 ÷ 2 a day = 3 days@a limit of six"
Little's law says lead time is work in progress divided by throughput. An invented team finishes two items a day. With eighteen in progress, lead time is eighteen over two, nine days. With a limit of six, it's six over two, three days.

@words text="Throughput held at 2: an assumption"
But the lab holds throughput at two in both cases. That's an assumption, not a finding. A team that cuts its work in progress might finish more items a day, or fewer. The book's point is that a limit helps when it exposes obstacles the team then removes.

@chapter Reading a board
@art board-log
The law can also be read from a log. Six items were started and done over eight days. Their lead times are two, four, two, four, two and four days.

@math heading="Six items over 8 days" items="item-days: 2 + 4 + 2 + 4 + 2 + 4 = 18@eighteen item days;;average WIP: 18 / 8 = 2.25@two point two five;;throughput: 6 / 8 = 0.75 a day@zero point seven five;;lead time: 18 / 6 = 3 days@three days"
That's eighteen item days in all. Over eight days, the average work in progress is eighteen over eight, two point two five. The throughput is six over eight, zero point seven five a day. And the average lead time is eighteen over six, three days.

@math heading="Check the law" items="2.25 ÷ 0.75 = 3 days ✓@divided by"
Check it: two point two five divided by zero point seven five is three days. The two agree because both come from the same eighteen item days. On a log the law is arithmetic, not a finding about the team.

@art open-item
It would differ if an item were still open at the end of the window. An unfinished item counts toward work in progress, but not toward lead time.

@chapter Where people slip
@list heading="Common slips" items="A WIP limit alone makes a team faster@The first|The lab's drop in lead time is a promise@The second|Any board is visual management@the third"
The first slip is thinking a WIP limit alone makes a team faster. The second is reading the lab's drop in lead time as a promise. And the third is treating any board as visual management. A board that shows status to one manager doesn't meet the description.

@chapter Try it
@words text="P 0–3 · Q 0–1 · R 1–5 · S 2–4 · T 3–6 · U 5–6"
Your turn. A board watched from day zero to day six, with six items. Work out each lead time, the average work in progress, the throughput and the average lead time, and check that the law holds. Then say what you'd change to make an obstacle visible.

@end text="Limit, show, and feed back"
You can read your own board through Little's law in the lab, on Learn. That's learn dot get er done dot I O.
