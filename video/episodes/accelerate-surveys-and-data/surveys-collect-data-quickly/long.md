---
format: long
lesson: accelerate-surveys-and-data/surveys-collect-data-quickly
title: Why ask people when your tools log everything?
thumb: The log missed a fifth
---

@chapter Why survey at all?
@title text="Surveys Allow You to Collect and Analyze Data Quickly" sub="Accelerate, Chapter 14" art=thumb
Tools on the market already report lead time. So why did the authors of Accelerate ask people instead? Chapter fourteen gives five reasons, and this lesson reads the first two.

@quote text="Often, the strongest reason to use surveys is speed and ease of data collection." cite="Forsgren, Humble and Kim, Accelerate, Chapter 14"
The first reason, in their words. Often, the strongest reason to use surveys is speed and ease of data collection.

@list heading="Five reasons for a survey" items="Speed@quick|The full stack@full stack|Completeness@completeness|Trust@trusted|What only asking can measure@only be measured"
The authors call what instrumenting the toolchain yields system data. Their five reasons for also surveying: a survey is quick, the full stack is hard to measure from system data, so is completeness, survey data can be trusted, and some things can only be measured by asking.

@chapter Speed
@art four-rounds
The data in the book was collected four times, each over four to six weeks, from thousands of respondents at thousands of organizations around the world. Now imagine the legal clearances, data specifications and transfers needed to gather system data from that many teams in the same weeks.

@art same-word
The deeper obstacle is what the data means. Teams use the same name for different measures, like lead time and cycle time, which are often confused. If one team's cycle time is another's lead time, an analyst can't tell which variable is which. A vetted survey item fixes the words for everyone.

@chapter The full stack
@art storage-box
The second reason is that system data is rarely exhaustive. One of the authors once tuned large disk storage machines. Her team measured every layer inside the box, and the figures said it ran well. Yet customers kept saying it was slow.

@art many-voices
The box was fast. What nobody had measured was the interface, how customers used it. People's reports were less precise than the logs, minutes against milliseconds, yet they showed the team where to look. So ask everyone who builds and runs the system, not just a few loud voices.

@chapter The log and the gap
@art hidden-path
Now a team of the lesson's own. Fourteen days of a pipeline log hold eight deploys. The team also pushes emergency fixes by hand, outside the pipeline, and the log knows nothing of them.

@math heading="Preset pipeline-log" items="8 deploys, 4 a week@eight deployments;;median lead time: (26 + 48) ÷ 2 = 37 h@thirty seven hours;;change fail rate: 0%@zero percent;;median time to restore: 2.5 h@two and a half hours"
From the log, the lab counts eight deployments, four a week. Sort the lead times and the middle two are twenty six and forty eight hours, so the median is thirty seven hours. The change fail rate is zero percent, because the pipeline marks a deploy failed only when the pipeline itself fails. And two incidents give a median time to restore of two and a half hours.

@math heading="Preset with-hotfixes" items="10 deploys, 5 a week@ten deployments;;median lead time: (26 + 26) ÷ 2 = 26 h@twenty six hours;;change fail rate: 2 ÷ 10 = 20%@twenty percent"
Add the two hand deploys, made two and one and a half hours after their commits, and mark the two deploys that really failed. Now there are ten deployments, five a week. The median lead time is twenty six hours. And the change fail rate is twenty percent, two of ten.

@art log-scroll
The log was exact about what it covered. It missed a fifth of the deploys, gave a median lead time eleven hours too long, and showed no failures where the team had two. But a survey isn't the cure either: people don't have perfect visibility. The two views together show more than one.

@chapter Where people slip
@list heading="Common slips" items="Trusting a number because it's precise@precise|Reading this as drop your logs@drop|A quick survey is a short one@short one"
Three slips. Trusting a measure because it's precise. Reading the chapter as telling teams to drop their logs. And taking a quick survey to be a short one. A survey is fast to run because so much work went into its wording first.

@chapter Try it
@words text="logged: e1 10→30 · e2 40→70 · e3 80→120 · e4 100→150 · by hand: m1 31→34 · m2 125→130" sub="hours: committed → deployed"
Your turn, over seven days. Four logged deploys: committed at hour ten and deployed at thirty, forty to seventy, eighty to a hundred and twenty, a hundred to a hundred and fifty. Two by hand: thirty one to thirty four, which repaired the failed first one, and a hundred and twenty five to a hundred and thirty. Compute the four measures both ways.

@end text="Find the path your log misses"
Check your count in the lab, on Learn. That's learn dot get er done dot I O.
