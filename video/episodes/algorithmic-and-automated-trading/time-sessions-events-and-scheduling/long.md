---
format: long
lesson: algorithmic-and-automated-trading/time-sessions-events-and-scheduling
title: Market clocks for trading bots: calendars, time zones and late jobs
thumb: Not every minute is tradable
---

@chapter The problem
@title text="Time, Sessions, Events, and Scheduling" sub="Algorithmic and Automated Trading" art=thumb
A trading job that runs every weekday at the open sounds simple. Then a holiday arrives, or a half day, or the clocks change. Suddenly your job runs when the market is closed, or an hour early, or long after the move it was meant to catch.

@art session-day
The lesson's point is that the same signal can mean different things before the open, during regular trading, or after a market event. At the open, buyers and sellers can reprice quickly after overnight information. And a delayed scheduled job may act on a move that already happened.

@chapter Three ideas
@list heading="What to understand" items="Trading calendar@trading calendar|Event window@event window|Scheduler state@scheduler state"
Three ideas. A trading calendar: the open, close, holiday, half day and instrument session rules. An event window: a defined period around earnings, news, auctions or scheduled releases. And scheduler state: a record of the planned run, the actual run, any skipped run, the lateness, and the recovery action.

@art calendar-gaps
Why isn't a weekday check enough? Because markets have holidays and special sessions. Some weekdays have no session at all, and some have a shorter one. Brokers follow the exchange calendar. It's a scheduler written without one that doesn't. Ignoring early closes is one of the lesson's named mistakes.

@chapter Late signals
@art late-job
A late signal is a stale signal. A signal describes a moment, and the conditions that produced it expire. So a late signal should be evaluated against a freshness rule, not assumed valid forever, and not submitted with its original timestamp as if nothing had changed.

@words text="Missed jobs need revalidation"
The same goes for missed jobs. Running them later without revalidation is a named mistake. The market they were written for may be gone.

@chapter One authoritative clock
@list heading="Use one authoritative clock" items="Resolve the calendar and session state@Resolve|Schedule deterministic jobs with run IDs@Schedule|Guard: skip or ask when late or blocked@Guard"
The lesson's method uses one authoritative clock, with explicit timezone and session information on every event and decision. Resolve: load the correct calendar and current session state. Schedule: create deterministic jobs, with deadlines and unique run identifiers. Guard: skip, or require approval, when a job is late or inside a blocked event window.

@art run-identifier
That run identifier matters. It's an identifier the scheduler can be handed twice without running the job twice. A stable identifier supports deduplication and recovery. And every run leaves an audit record, so you always know what the scheduler did.

@art event-blackout
Event windows work the same way. Around earnings, news or a scheduled release, you can define an explicit blackout, and the guard keeps the job out of it. Session permissions say which parts of the day the system is allowed to trade at all.

@chapter Daylight saving
@math heading="Open 09:30 New York · job fixed at 13:30 UTC" items="summer: New York = UTC−4 → 09:30 EDT@summer;;November: New York = UTC−5 → 08:30 EST@November;;an hour before the open@an hour before"
Here's the lesson's worked example. The exchange opens at nine thirty New York time. A server on UTC schedules the open job at thirteen thirty UTC, all year. In summer, New York is four hours behind UTC, so that's nine thirty. But in November, New York is five hours behind. So the job runs at eight thirty, an hour before the open.

@art utc-offset
The calendar carries the offset. A scheduler that hard codes it is right for half the year. Assuming local server time equals exchange time, and ignoring daylight saving changes, are both on the lesson's list of mistakes.

@chapter Where people slip
@list heading="Common mistakes" items="Server time assumed to be exchange time@The first|Missed jobs run later without revalidation@The second|Early closes and daylight saving ignored@And the third"
The first mistake is assuming local server time equals exchange time. The second is running missed jobs later without revalidation. And the third is ignoring early closes and daylight saving changes. Use exchange calendars rather than fixed weekday logic, and define a maximum age for every signal and job.

@chapter Try it
@words text="Session rules · clock drift · scan frequency · blackouts"
In the lesson's lab, which uses deterministic synthetic educational data with no broker or live market connection, change the session rules, the clock drift, the scan frequency and the event blackouts. Watch which executions turn late, which get skipped, and which stay valid.

@end text="Drift the clock, watch the jobs"
You can drift the clock and watch jobs run late or get skipped, on Learn. That's learn dot get er done dot I O.
