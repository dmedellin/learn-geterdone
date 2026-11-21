---
format: long
lesson: accelerate-measuring-performance/the-four-measures
title: The four measures of software delivery performance
thumb: Two for tempo, two for stability
---

@chapter What to measure
@title text="Measuring Software Delivery Performance" sub="Accelerate, Chapter 2" art=thumb
If lines of code, velocity and utilization are the wrong measures, what's the right one? The authors give their measure two criteria before they pick anything.

@quote text="it should focus on a global outcome to ensure teams aren't pitted against each other" cite="Forsgren, Humble and Kim, Accelerate, Chapter 2"
First, it should focus on a global outcome to ensure teams aren't pitted against each other. Pay developers for throughput and operations for stability, and you build a wall of confusion between them.

@art wall-of-confusion
Second, it should be an outcome, not output, so it can't be raised with busywork. They settle on four measures: delivery lead time, deployment frequency, time to restore service, and change fail rate.

@chapter Lead time
@art two-halves
Lead time is the Lean measure of how long it takes from a customer's request to its satisfaction. In product development it has two parts. Designing and validating a feature is uncertain and highly variable, the fuzzy front end. Delivering it is easier to measure and steadier.

@words text="Lead time = commit → running in production"
So the authors measure only the delivery half: the time from code committed to code running in production. The survey offered six answers, from less than one hour to more than six months.

@chapter Deployment frequency
@art small-batches
The second measure is about batch size. Smaller batches shorten cycle times, speed feedback and cut risk. But software has no visible inventory, so the authors needed a stand in that people can report: deployment frequency, to production or an app store.

@words text="Deployment frequency ≈ batch size" sub="from on demand to fewer than once every six months"
Its six answers run from on demand, meaning several deploys a day, down to fewer than once every six months. Lead time and deployment frequency together are the tempo of delivery.

@chapter Stability
@art restore-service
Do teams that speed up give up stability? To find out, the authors add two measures. Traditionally reliability is the time between failures. But in complex, quickly changing systems failure is inevitable, so the question becomes how quickly service is restored after an incident.

@list heading="The four measures" items="Lead time: tempo@Lead time|Deployment frequency: tempo@deployment frequency|Time to restore service: stability@time to restore|Change fail rate: stability@change fail rate"
The fourth is the change fail rate: the percentage of changes to production that degrade service or have to be remedied. So lead time and deployment frequency are tempo, and time to restore and change fail rate are stability.

@chapter What kind of data
@art survey-choice
Notice what kind of data these are. In the book, each measure is a respondent's answer about their primary application, picked from a short list. That's why Fowler's foreword says they capture perceptions. The lesson's lab does something the survey didn't: it computes the four from a log.

@chapter A fortnight's log
@math heading="Lead times, in hours" items="6, 4, 26, 3, 8, 2, 20, 4, 5, 3@ten changes;;sorted: 2, 3, 3, 4, 4, 5, 6, 8, 20, 26@Sort the;;median = (4 + 5) / 2 = 4.5 h@four and a half"
Here's one team's log over fourteen days: ten changes. Sort the lead times. With an even count, the median is the mean of the middle two, four plus five over two, which is four and a half hours: less than one day.

@math heading="The other three" items="10 deploys in 14 days = 5 a week@five a week;;1 / 10 failed = 10%@one in ten;;restore: 3 h and 12 h → median 7.5 h@seven and a half"
Ten deploys in fourteen days is five a week, between once a day and once a week. One in ten failed, ten percent, in the zero to fifteen percent band. And the two incidents took three and twelve hours to restore, a median of seven and a half: less than one day.

@words text="The median hides 20 h and 26 h"
But look at the spread. Two changes took twenty and twenty six hours, waits that ran overnight, and the median hides them. The mean would be eight point one hours.

@math heading="A batched team, 28 days" items="7 changes in 3 deployments@seven changes;;median lead time 140 h@one hundred and forty;;2 of 7 failed = 28.6%@twenty eight point six;;restore 48 h and 24 h → median 36 h@thirty six"
Now a team that gathers its changes and ships them together: seven changes in three deployments over twenty eight days. The median lead time is one hundred and forty hours, because a change waits for the next release. Two of seven failed, twenty eight point six percent, and the median restore is thirty six hours.

@art tempo-stability
The lesson wrote that sample so the long wait, the failures and the slow recovery land on the same team. A real log wouldn't have to. Whether tempo and stability really go together is the next lesson's question.

@chapter Where people slip
@list heading="Common slips" items="Throughput for devs, stability for ops@The first|Starting the clock at the request@The second|Trusting a median for every change@And the third"
The first slip is measuring developers on throughput and operations on stability. The second is taking lead time to start at the customer's request. And the third is trusting a median to describe every change. Which events you record as commit, deploy, failure and restore is the measurement.

@chapter Try it
@words text="7 days · 4 changes · 1 failed · 1 incident"
Your turn. A third team's week has four changes, one of which failed, and one incident from three thirty to six thirty. Work out each lead time, the median, the change fail rate and the time to restore, and find the book's answer for each.

@end text="Compute the four from a log"
You can type a log into the lab and read all four measures, on Learn. That's learn dot get er done dot I O.
