---
format: long
lesson: accelerate-surveys-and-data/you-can-trust-survey-data
title: Can you trust survey data more than a log?
thumb: One liar, one over n
---

@chapter People may lie
@title text="You Can Trust Survey Data" sub="Accelerate, Chapter 14" art=thumb
Every survey meets the same doubt: people may lie. Chapter fourteen of Accelerate turns that doubt around, and argues that a survey is harder to move than a log.

@quote text="In this case, the use of a survey actually protects us against bad actors." cite="Forsgren, Humble and Kim, Accelerate, Chapter 14"
In the authors' words. In this case, the use of a survey actually protects us against bad actors. But first, two more reasons to ask people.

@chapter What a system can't see
@art unchecked-files
A system knows only what happens inside its boundaries. Take version control. A team can say whether every production artifact is under it, because the team sees all its work. A system can count the files checked in, but not the files that never were. So it can't give the percentage that matters.

@chapter Logs go wrong too
@art one-bad-entry
The authors run a thought exercise with technologists. Few trust survey data. More trust their logs, because they feel untampered with. Then almost everyone admits they've seen bad data come out of a system. People build systems and make mistakes, and a single malicious author of code could make a system report false figures.

@art crowd-dilution
Here's the comparison the lesson turns on. A log can be bent by one person, and because a business watches only a handful of numbers, the error can sit there for months or years. A survey's liars are diluted by everyone else who answered.

@words text="23,000+ respondents · several hundred liars needed" sub="the authors' estimate"
With over twenty three thousand pooled respondents, the authors estimate a noticeable change would need several hundred people lying together, on every item of a construct, equally and in the same direction. That's their estimate, not a computation they show. Responses are also anonymous, and constructs pass tests of validity and reliability.

@chapter One respondent's weight
@math heading="Preset six-respondents" items="five respondents: mean 4.85@four point eight five;;r6 answers 7, 7, 7, 7 → 7, 7, 7, 1 = 5.5@seven to all four;;six respondents: 119/24 ≈ 4.96@four point nine six;;shift = (5.5 − 4.85) ÷ 6 = 0.108@nought point one oh eight"
Now the lab. Five respondents score a four item construct, the fourth reverse coded, with a mean of four point eight five. Then r six answers seven to all four. Turned round, that's seven, seven, seven, one: a score of five point five. The mean over six is about four point nine six. The shift is five point five minus four point eight five, over six: nought point one oh eight.

@math heading="Preset eleven-respondents" items="shift = (5.5 − 4.85) ÷ 11 ≈ 0.059@nought point oh five nine;;a log read as one number: n = 1@n equal to one"
Repeat the five honest patterns twice, then add r six. The shift is the same gap over eleven, about nought point oh five nine. That's the authors' argument in miniature. A log with one number the business reads has n equal to one, and the one entry decides.

@art straight-line
The reverse coded item raises the bar a little: r six's score tops out at five point five, not seven. But treat that as a prompt to look, not proof. A hurried respondent straight lines honestly, and a careful liar can answer seven, seven, seven, one. And a big pool doesn't reach a bias that many respondents share.

@chapter Only asking can measure it
@art turnover-door
The fifth reason: some things can only be measured by asking. Culture is the example, and turnover is the usual stand-in. But a leaver may have taken a much better paid offer, followed a partner who relocated, or left to study. One author knows someone who left a supportive team because its encouragement gave him the confidence to change career.

@list heading="Turnover can be gamed" items="Lay off a job seeker before they leave@lay them off|Block transfers to keep retention@block transfers"
And turnover can be gamed. A manager who learns an employee is looking may lay them off to keep them out of the turnover figure. A manager rewarded for retention may block transfers.

@art ask-bubble
Turnover can be useful if you're careful about what it measures. But to learn how people feel about risk, sharing information and working across boundaries, and why they behave as they do, you have to ask.

@chapter Where people slip
@list heading="Common slips" items="Logs can't lie, surveys can@Logs can't lie|A large pool cancels every bias@every bias|Turnover measures culture@Turnover"
Three slips. Thinking logs can't lie and surveys can: neither is immune, and the claim is about how much each can be moved. Believing a large pool cancels every bias. And using turnover as an objective measure of culture.

@chapter Try it
@words text="s1 6,6,5,2 · s2 5,5,5,3 · s3 7,6,6,1 · s4 4,4,5,4 · s5 1,1,1,1" sub="fourth item reverse-coded"
Your turn. Five respondents, the fourth item reverse coded. s1: six, six, five, two. s2: five, five, five, three. s3: seven, six, six, one. s4: four, four, five, four. s5: one, one, one, one. Score each, find the mean, then check s5's weight with s minus m over n.

@end text="Weigh one respondent"
Confirm it in the lab, on Learn. That's learn dot get er done dot I O.
