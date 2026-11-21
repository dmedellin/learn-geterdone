---
format: long
lesson: paradoxes-and-their-exits/achilles-and-the-tortoise
title: Achilles and the tortoise: where the gaps add up to
thumb: He passes at 1000/9
---

@chapter The race
@title text="Achilles and the Tortoise" sub="Paradoxes and Their Exits" art=thumb
Achilles runs ten times as fast as a tortoise, and gives it a head start of a hundred metres. Zeno argues that Achilles can never catch it.

@art race-track
To pass the tortoise, Achilles must first reach the place it started. By then it's moved on. He must reach that place, and by then it's moved on again. Each stage leaves a gap, and a gap that's still positive means the tortoise is still ahead.

@list heading="Zeno's argument" items="He must reach where the tortoise just was@must reach|Each time, a positive gap remains@still positive|Infinitely many stages, the gap never reaches zero@never reaches zero|So he never passes it@never passes"
Before Achilles passes the tortoise, he must reach the place it just left. Each time he does, there's a gap that's still positive. There are infinitely many such stages, and the gap never reaches zero. So he never passes the tortoise.

@chapter The gaps
@art shrinking-gaps
The third premise is true, and it's worth saying so. No stage ends with a gap of zero. But the conclusion doesn't follow from it, and the series shows why.

@math heading="Gaps: each a tenth of the last" items="100 + 10 + 1 + 1/10 + …@a hundred;;r = tortoise speed / Achilles' speed = 1/10@The ratio;;limit = 100 / (1 − 1/10) = 1000/9@the limit"
Achilles runs a hundred metres while the tortoise runs ten. Then he runs ten while it runs one. Then one while it runs a tenth. The gaps are a hundred, ten, one, each a tenth of the last. The ratio is the tortoise's speed over his, one tenth. So the limit is a hundred over one minus a tenth, which is a thousand ninths.

@art meeting-point
That's a little over a hundred and eleven metres. It's the total distance Achilles has run when he draws level. Every stage of Zeno's argument happens before that point. After all the gaps together, which is the limit, he's level. And from there, he's past.

@chapter The same answer by algebra
@math heading="Check" items="10t = 100 + t@ten t;;t = 100/9 seconds@a hundred ninths;;run = 10t = 1000/9 metres@having run"
Ordinary algebra agrees. Achilles runs at ten, the tortoise at one, from a start a hundred ahead. He draws level when ten t equals a hundred plus t, at a hundred ninths of a second, having run a thousand ninths of a metre. The series and the equation describe one race.

@chapter The ratio decides
@art slow-closing
Now change the speeds. Achilles runs at ten and the tortoise at nine, so the ratio is nine tenths. The gaps are a hundred, ninety, eighty one, which sum to two hundred and seventy one after three stages. The limit is a thousand. A race that closes more slowly takes a longer run, and still ends.

@art equal-speeds
And here's the case where Zeno is right. If the speeds are equal, the ratio is one, every gap is a hundred, and the sum just grows. There's no limit. The tortoise stays a hundred metres ahead. The argument's structure is unchanged. What differs is the ratio.

@chapter Which exit?
@art milestones
As set out, the three premises are true, and the conclusion doesn't follow. That's exit two, a step that only looked valid. It borrowed an unstated premise: that a list of stages with no last member goes on forever, in distance as in time. Write that in, and it's the previous lesson's exit. Deny the added premise, and the series refutes it. Both descriptions are one repair. And at a ratio of one, that unstated premise is true of the race.

@chapter Where people slip
@list heading="Common slips" items="Gaps never reach zero, so he never catches up@The first|Trusting the form to decide the race@The second|Mixing up the two speed ratios@And the third"
The first slip is concluding he never catches up because the gaps never reach zero. The meeting is the limit of the stages, not any stage. The second is trusting the paradox's form to decide the race. The same form describes the equal speed race. Look at the ratio. And the third is dividing the speeds the wrong way, which gives growing gaps.

@chapter Try it
@words text="r = 1/2" sub="the tortoise half as fast"
Change the ratio to one half, so the tortoise runs half as fast as Achilles. Work out the limit by the series, then check it with the algebra. You should get two hundred metres either way.

@end text="Sum the gaps of the race"
You can change the speeds and sum the gaps yourself, on Learn. That's learn dot get er done dot I O.
