---
format: long
lesson: capacity-estimation/peak-to-average
title: Peak to average: you pay for the mean, you build for the peak
thumb: Build for the busiest hour
---

@chapter The question
@title text="Peak to Average" sub="Capacity Estimation" art=thumb
Divide a day's requests by eighty six thousand four hundred and you get a real number about your system. It's just not the number to build for. Traffic has a shape, and the busy hour is where systems fall over.

@art daily-profile
A daily profile is the request count in each of the twenty four hours of a day. The mean rate is the daily total over eighty six thousand four hundred seconds. The peak rate is the busiest hour over three thousand six hundred seconds. And the provisioning multiplier is the ratio of the two.

@words text="the mean is what the day cost" sub="the peak is what the day required"
Both come from the same twenty four numbers, and neither is more real. The mean is what the day cost. The peak is what the day required.

@chapter A consumer app
@math heading="456 million requests a day" items="mean = 456 000 000 ÷ 86 400 = 5 277.78 req/s@the mean;;busiest hour, 21:00 = 46 000 000 req@nine in the evening;;peak = 46 000 000 ÷ 3 600 = 12 777.78 req/s@the peak"
Take a consumer app with four hundred and fifty six million requests a day. The mean is five thousand two hundred and seventy seven point seven eight a second. The busiest hour, at nine in the evening, carries forty six million. So the peak is twelve thousand seven hundred and seventy seven point seven eight a second.

@math heading="The multiplier" items="peak/mean = 24 · 46 000 000 / 456 000 000@twenty four times;;= 46/19 = 2.421×@forty six over nineteen;;short by 12 777.78 − 5 277.78 = 7 500 req/s@seven thousand five hundred"
Peak over mean is twenty four times the busiest hour over the daily total. That's forty six over nineteen, about two point four two one. Size the system to the mean, and you're seven thousand five hundred requests a second short, for an hour, every evening.

@art evening-gap
That failure is predictable and dated. It isn't a surprise overload. It's scheduled, at a known hour, the same size every day. What makes the mistake so durable is that the mean was computed correctly. Only its name was wrong.

@chapter Shape, not size
@art doubled-day
Look at that multiplier again: twenty four times the peak bucket over the total. Both are whole numbers, so it's an exact fraction, and it doesn't depend on how big the day is. Double every bucket and the ratio doesn't move. Change the shape of the day and it does.

@art three-shapes
So the multiplier is a statement about the shape of the day and nothing else. And shapes differ a lot.

@math heading="Three shapes" items="flat internal service:  1×@Flatten the day;;consumer app with an evening:  46/19 ≈ 2.421×@consumer app;;broadcast, one hour carries the day:  26/3 ≈ 8.667×@broadcast"
Flatten the day, like an internal service with no rhythm, and the multiplier is exactly one. The consumer app gives forty six over nineteen. A broadcast where one hour carries the day gives twenty six over three, about eight point six six seven. So distrust call it two times for peak. Measure it instead.

@chapter What an hour can't see
@art hidden-burst
The busiest hour is itself an average over three thousand six hundred seconds. A five minute burst inside it gets flattened. Re bucket the same day by the minute and the peak can only rise or stay the same. So an hourly multiplier is a lower bound. Say it with its resolution: two point four two one, measured hourly.

@art mix-by-hour
And the read write mix moves with the profile. A hundred to one over the day can be a different ratio in the busy hour, and it's the peak hour rates that get sized. If you're measuring the profile anyway, bucket the two request kinds separately.

@chapter Where people slip
@list heading="Common slips" items="Sizing to the daily total ÷ 86 400@The first|A remembered multiplier@The second|Treating the hourly peak as the real peak@The third"
The first slip is sizing to the daily total over eighty six thousand four hundred. The second is using a remembered multiplier instead of a measured one. And the third is reading the hourly peak as the real peak, when it's only a floor.

@chapter Try it
@words text="broadcast: 23 quiet hours + 1 big one" sub="nearer 3× or nearer 9×?"
Your turn. Take the broadcast example, where only one hour is lifted, so the day is twenty three quiet hours plus one large one. Predict whether the multiplier is nearer three or nearer nine. Then read off the peak, the mean and the ratio, and say what sizing to the mean would cost.

@end text="Shape the day, read the multiplier"
You can reshape the twenty four hours and watch the peak and the multiplier move, on Learn. That's learn dot get er done dot I O.
