---
format: long
lesson: options-trading/expiration-and-time-decay
title: Time decay: why an option loses value faster as expiry nears
thumb: Time runs out, not evenly
---

@chapter The question
@title text="Expiration and Time Decay" sub="Options Trading" art=thumb
Hold the stock still. Hold volatility still. Change nothing but the calendar. A long option still loses value. Why, how fast, and why isn't it the same amount every day?

@words text="Extrinsic value is the price of time"
The short answer is that extrinsic value is the price of time, and time runs out. To see how, you need three ideas: expiration, the decay of extrinsic value, and theta.

@chapter Expiration
@art expiry-date
An option contract ends on its expiration date. After that, the holder has no remaining option rights. Whatever the option is worth at that moment is all it will ever be worth.

@art value-split
So split the value in two. Intrinsic value is what the option is in the money by. Extrinsic value is everything above that. Only the extrinsic part is directly exposed to disappearing at expiration.

@words text="At expiration: intrinsic value only"
At expiration, a long option is worth its intrinsic value, and nothing more. If it finishes out of the money, it has no intrinsic value, so everything the holder paid for it was extrinsic, and all of it has gone.

@chapter The decay curve
@art decay-curve
Now watch extrinsic value across the life of the option, with stock and implied volatility held constant. It reaches zero at expiration. But the path toward zero is not a straight line. It slopes gently when there's lots of time left, and steepens as expiration nears.

@words text="Same option, priced on every day of its life"
That's exactly what the lesson's lab draws. Hold the stock and volatility still, slide the days remaining, and the curve is the same option priced at every day of its life.

@chapter Theta
@art theta-slope
Theta puts a number on it. Theta estimates how much the option's value changes when one day passes, with the other model inputs held constant. Think of it as the slope of that decay curve at today's date.

@math heading="Theta in contract dollars" items="Theta on screen: −0.05@minus zero point zero five;;Per share: −$0.05 a day@per share;;One contract: −0.05 × 100 ≈ −$5 a day@five dollars a day"
Theta is quoted per share. So a theta of minus zero point zero five on the screen is per share, and a one contract position loses about five dollars a day. A broker's position view will show it that way. Three contracts would be about fifteen dollars a day.

@art steepening-days
And because the curve steepens, the daily figure isn't fixed. It grows as expiry nears. Near term options can change rapidly, especially when the stock is around the strike. So you can't multiply today's theta by the days left and call it the total.

@chapter Time in the plan
@art exit-flag
So what do you do with this? Put time into the plan from the start, and mark the point where you'll get out, well before the steep end of the curve.

@list heading="Evaluate time exposure" items="Match expiration to the thesis@Match|Separate intrinsic and extrinsic@separate|Inspect theta and days to expiration@inspect theta|Define an exit before expiration@an exit"
Time has to be part of the trade plan, not an afterthought. Match the expiration to the thesis, with enough time for the move you expect and any known events. Separate intrinsic from extrinsic value. Inspect theta and the days to expiration. And define an exit before expiration, rather than relying on automatic handling as a management plan.

@chapter Where people slip
@list heading="Common mistakes" items="Assuming decay is linear@The first|Too little time because it's cheaper@The second|Holding through expiration with no plan@The third|Reading theta as a contract figure@the fourth"
Four mistakes. The first is assuming decay is linear. The second is buying too little time because the premium is cheaper. The third is holding through expiration without a plan. And the fourth is reading theta as a contract figure.

@words text="Cheaper can mean faster decay" sub="and less time for the thesis"
The second one is tempting. A shorter expiration usually costs less. But that lower premium can come with faster decay, and with less time for the move you expect to actually happen.

@words text="Expiration is not a plan"
And the third is easy to drift into. Around expiration, exercise, assignment and after hours price moves can create positions you never intended. Decide before you enter what you'll do as expiration approaches.

@chapter Try it
@words text="Theta in contract dollars · which expiration decays faster?"
Your turn. Say what a long option is worth at expiration. Say which way its extrinsic value moves as days pass, with everything else held still, and why the daily figure grows as expiry nears. Then turn a theta into contract dollars, and decide which of two expirations decays faster. Neither needs the chart.

@end text="Slide the days remaining"
You can slide the days remaining and watch the same option decay, on Learn. That's learn dot get er done dot I O.
