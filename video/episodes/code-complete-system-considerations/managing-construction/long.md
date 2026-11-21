---
format: long
lesson: code-complete-system-considerations/managing-construction
title: Managing construction: why an estimate is a range
thumb: Same project, half to fourfold
---

@chapter The moment
@title text="Managing Construction" sub="Code Complete, chapter 28" art=thumb
Someone's asked you how long the next feature will take, and you gave a number. Chapter twenty eight is written for that moment, from both sides. What a manager has to worry about, and how management looks from the developer's chair.

@chapter Encouraging good code
@art shared-code
How do you encourage good code? Not with standards handed down from management. If there are to be standards, a respected architect should set them and the team should accept them. Lighter means work too. Two people on every part of the code, a review of every line, good code circulated, and code treated as the project's property, not its author's.

@chapter Controlling change
@art change-batch
Configuration management, or change control, keeps a system's integrity. Handle requirements and design changes in groups, not as each occurs to you. Estimate each one's cost, including its ripple through design, code, tests and documents. And treat a high volume of change as a sign the upstream work wasn't finished.

@words text="Version control · backups you've restored" sub="far more projects suffer from too little control than too much"
For code, that means version control, and backups whose restore you've actually tried. The risk of overcontrol is real, but McConnell reports seeing far more projects suffer from no change control than from too much.

@chapter Estimating
@quote text="Good software estimation is a significant challenge. Keys to success are using multiple approaches, tightening down your estimates as you work your way into the project, and making use of data to create the estimates." cite="McConnell, Code Complete, 2nd ed., Chapter 28, p. 688"
Then estimation. Good software estimation is a significant challenge. Keys to success are using multiple approaches, tightening down your estimates as you work your way into the project, and making use of data to create the estimates.

@list heading="Three steps that carry it" items="Estimate at a low level of detail@low level|Use several techniques and compare@several techniques|Estimate again as you go@again"
The book adapts a procedure from Boehm. Three steps carry the argument. Estimate at a low level of detail, so the pieces' errors tend to cancel. Use several techniques and compare them. And estimate again as the project goes.

@art dial-factors
Then the influences on the schedule. A table from Cocomo the second gives each factor a helpful and a harmful percentage. Programmer capability, minus twenty four and plus thirty four. Requirements analyst capability, minus twenty nine and plus forty two. Product complexity, minus twenty seven and plus seventy four.

@chapter Work the multipliers
@math heading="Nominal: 100 staff-months" items="strong team:  0.76 × 0.71 ≈ 0.54 → 53.96@strong team;;weak team:  1.34 × 1.42 ≈ 1.90 → 190.28@weak team;;hard product:  1.74 × 1.63 × 1.46 ≈ 4.14 → 414.09@hard product"
Turn each percentage into a multiplier and multiply. From a hundred staff months, a strong team, point seven six times point seven one, gives fifty three point nine six. A weak team gives one hundred and ninety point two eight. And a hard product, with high complexity and tight time and storage constraints, gives about four hundred and fourteen.

@art estimate-range
Two factors about the people move the same estimate from about half to nearly twice. Three about the product, more than fourfold. So an estimate made before you know the team and the product is a range. And these multipliers are averages fitted to other people's projects. Your own records are the test.

@chapter Behind schedule
@art brooks-law
What if you're behind? Hoping to catch up rarely works. A survey of over three hundred projects found delays growing toward the end, not shrinking. And Brooks's law says adding people to a late project makes it later. New people must learn, teaching them takes others' time, and more people means more communication.

@words text="One woman: a baby in nine months" sub="nine women: not in one month"
One woman can have a baby in nine months. Nine women can't have one in a month. McConnell qualifies it, though. Where tasks can be divided and done independently, people added late can help. The other remedy is to cut the scope.

@chapter Measuring and people
@art people-spread
Any measurement of a project beats none, and people work on what's measured. And programmers are people. The book reports differences of an order of magnitude among programmers of similar experience. On religious issues, like braces and naming, a manager should suggest rather than rule.

@chapter Where people slip
@list heading="Common slips" items="Thinking an estimate is a number@The first|More people bring a late project in earlier@The second|A rough measurement is worse than none@the third"
The first slip is thinking an estimate is a number. It's a range that tightens as you go. The second is thinking more people will bring a late project in earlier. It's a question about the work, not a rule about headcount. And the third is thinking a rough measurement is worse than none.

@chapter Try it
@words text="50 staff-months" sub="programmer capability +34% · software tools −22%"
Your turn. Start from a nominal fifty staff months. Programmer capability is at the harmful end, plus thirty four percent. Use of software tools is at the helpful end, minus twenty two. Turn them into multipliers, multiply, and give the adjusted effort.

@end text="Move an estimate yourself"
You can try your own factors in the estimate lab, on Learn. That's learn dot get er done dot I O.
