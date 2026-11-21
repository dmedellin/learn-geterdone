---
format: long
lesson: scaling-laws-and-cost/reserved-vs-on-demand
title: Reserved instances: never reserve the peak
thumb: Reserve the floor, not the peak
---

@chapter A bet on hours
@title text="Reserved vs On-demand" sub="Scaling Laws and Cost" art=thumb
A reserved instance is cheaper per hour. So reserve everything you need at the peak, and save the most? That plan costs more than reserving nothing at all.

@art duty-cycle
A reserved instance costs r an hour, for every hour of the term, whether it runs or not. On demand costs d an hour, only when it runs. So reserving wins exactly when the instance runs more than r over d of the time.

@math heading="Break-even utilisation" items="u* = r / d@r over d;;7¢ / 12¢ = 7/12 = 58.3%@seven twelfths"
That's u star, r over d. At seven cents reserved and twelve cents on demand, it's seven twelfths, fifty eight point three percent. Read it as a duty cycle. Up for more than fourteen hours of every twenty four? Reserve it. The term length cancels out.

@chapter From a threshold to a level
@art layered-profile
Now stack the day's load as layers. Layer k is the k th instance, and it runs only in the hours when demand is at least k. So its utilisation is the share of hours the profile spends at or above k. The bottom layer runs all day. The top one runs for an hour.

@art margin-step
Raise the reserved level one instance at a time. Each step costs twenty four times r, a dollar sixty eight a day. It saves d for every hour the profile is above that level. So keep going while the share of hours above it beats u star.

@math heading="Where it stops" items="hours above 12:  11 of 24 = 45.8%@eleven of twenty four;;45.8% < 58.3%  →  stop at 12@stop at twelve;;a full scan of 0 to 36 also gives 12  ✓@a full scan"
On this profile the crossing is at twelve instances. Eleven of twenty four hours are above it, forty five point eight percent, below the threshold. So stop at twelve. And a full scan of every level from zero to thirty six agrees. That's the check.

@chapter Three bills
@math heading="432 instance-hours a day, peak 36" items="reserve nothing:  432 × $0.12 = $51.84@fifty one dollars eighty four;;reserve 12:  $20.16 + $17.28 = $37.44@thirty seven forty four;;reserve the peak:  864 × $0.07 = $60.48@sixty dollars forty eight"
This profile uses four hundred and thirty two instance hours a day. All on demand, that's fifty one dollars eighty four. Reserve twelve, and it's twenty dollars sixteen of reserved plus seventeen twenty eight on demand, thirty seven forty four, saving fourteen forty, twenty seven point eight percent. Reserve the peak of thirty six, and it's sixty dollars forty eight.

@art reserve-the-peak
That's eight dollars sixty four worse than reserving nothing. The peak instances run for one hour in twenty four, four point two percent, against a threshold of fifty eight. Reserving them buys twenty three idle hours each, every day. A commitment is a bet on hours, not on importance.

@art reserved-floor
The opposite error is quieter. Reserve nothing, and the bottom twelve instances, which run every hour of every day, pay the on demand premium. That's the fourteen forty a day the optimum gets back.

@chapter Spot
@art spot-reclaim
Spot is a third option, and it isn't just the cheapest column. A spot hour can be taken back, and the work still has to be done, so an interrupted hour gets bought again on demand.

@math heading="s = $0.04,  q = 15%" items="delivered = s + q·d = 0.04 + 0.15 × 0.12 = $0.058@five point eight cents;;beats on demand while q < (d − s)/d = 2/3@two in three"
With a reclaim probability q, a delivered spot hour costs s plus q times d. At four cents and fifteen percent, that's five point eight cents, not four. It beats on demand only while reclaims are rarer than two in three. Put it on the burst layer, the one too spiky to reserve.

@chapter Where people slip
@list heading="Common slips" items="Reserving for the peak@The first|Comparing totals instead of the margin@The second|Quoting spot at its sticker price@the third"
The first slip is reserving for the peak. The second is comparing total bills instead of the margin, which can't tell you whether eleven or thirteen was better. And the third is quoting spot at its sticker price, with no reclaim rate beside it.

@chapter Try it
@words text="r = 10¢,  d = 12¢" sub="first move: the new u*"
Your turn. Raise the reserved price to ten cents, and keep on demand at twelve. Work out the new u star first, and predict whether the best level rises or falls. Then find it and the three daily bills, and say how much of the saving survived.

@end text="Reserve the floor"
You can move the prices and watch the reserved level settle, on Learn. That's learn dot get er done dot I O.
