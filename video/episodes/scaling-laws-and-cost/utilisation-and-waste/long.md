---
format: long
lesson: scaling-laws-and-cost/utilisation-and-waste
title: Sixty nine percent idle, and you still can't cut it
thumb: Bought for the peak, used at the mean
---

@chapter Bought for the peak
@title text="Utilisation and Waste" sub="Scaling Laws and Cost" art=thumb
Your fleet is sixty nine percent idle. That sounds like money on the floor. It is, but you can't just pick it up, and here's why.

@art daily-profile
Capacity is bought for the busiest hour. Nobody runs that hour at a hundred percent, because waiting explodes as utilisation nears one. So you buy the peak divided by a target utilisation, and the headroom in that division is bought on purpose.

@art paid-vs-used
But averaged over the day, you only use the mean. So the share you paid for and didn't use is one minus the mean times the target, over the peak.

@math heading="Waste" items="paid = peak / ρ_target@peak over rho;;used = mean@Used is the mean;;waste = 1 − mean · ρ_target / peak@one minus"
Paid is the peak over rho target. Used is the mean. And waste is one minus mean times rho target over peak. Rho here is the same rho as always, demand over the capacity in service.

@chapter Worked out
@math heading="peak 12 000 rps at 21:00,  mean 5 250,  ρ = 7/10" items="paid = 12 000 ÷ 7/10 = 17 142.86 rps@seventeen thousand;;waste = 1 − 5 250 × 0.7 / 12 000 = 1 − 49/160@forty nine over a hundred and sixty;;= 111/160 = 69.375%@sixty nine point three seven five"
Take a peak of twelve thousand requests a second at nine in the evening, a mean of five thousand two hundred and fifty, and a target of seventy percent. You buy about seventeen thousand one hundred and forty three. The waste is one minus forty nine over a hundred and sixty, a hundred and eleven over a hundred and sixty, sixty nine point three seven five percent.

@art ten-times-same
Notice what's in that. A ratio, peak over mean, sixteen sevenths. And a fraction, the target. Both are pure numbers. Multiply every hour by ten, and the waste is a hundred and eleven over a hundred and sixty again. Growth doesn't improve it. It just makes it ten times the money.

@chapter Cut it to the mean?
@art cut-to-mean
So cut the fleet to the five thousand two hundred and fifty you use on average? Then nine of the twenty four hours are over capacity, the worst by six thousand seven hundred and fifty requests a second. The fleet isn't sixty nine percent too big at any hour. It's far too big at four in the morning, and exactly right at nine at night.

@words text="ρ at the peak = 12 000/5 250 = 16/7 > 1"
At the peak hour, utilisation would be sixteen sevenths. That isn't a busy queue. It's above one, where there's no steady state, and the backlog grows for as long as the hour lasts. The waste figure gives no warning, because it's a mean, and the failure is at the maximum.

@art headroom-gap
And some of that waste isn't waste. A perfectly flat profile still reports one minus the target, thirty percent. That residue is the price of a latency target, the headroom.

@chapter What actually moves it
@list heading="Three levers" items="Run the peak hotter@run the peak hour hotter|Flatten the profile@move work out|Fill the trough@put work in the trough"
Only three moves change the number. Run the peak hour hotter. Move work out of the peak, so peak over mean falls. Or put work in the trough that doesn't care when it runs.

@words text="ρ_target 80%:  waste = 65%"
Raise the target from seventy to eighty percent, and the waste falls to sixty five percent. Ten points of utilisation moved it more than four points, and it cost latency, not reliability.

@art fill-the-trough
That's why batch jobs, index rebuilds and backfills go in the quiet hours. That capacity is the cheapest in the building, because it's already paid for.

@chapter Where people slip
@list heading="Common slips" items="Reading the waste as slack to cut@The first|Counting the headroom as waste@The second|Expecting growth to improve it@the third"
The first slip is reading the waste as slack that can be cut. The second is counting the deliberate headroom as waste. And the third is expecting growth to improve the number, when traffic cancels out of it entirely.

@chapter Try it
@words text="The business profile" sub="two humps either side of lunch"
Your turn. Take the business profile, two humps either side of lunch, which is flatter. Predict whether its waste is above or below sixty nine point four percent at the same target. Then read the peak, mean and waste off the lab, and say which factor did the work.

@end text="Shape and target, nothing else"
You can switch profiles and move the target and watch the waste, on Learn. That's learn dot get er done dot I O.
