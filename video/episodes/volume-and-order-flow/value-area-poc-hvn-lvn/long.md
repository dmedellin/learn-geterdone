---
format: long
lesson: volume-and-order-flow/value-area-poc-hvn-lvn
title: Value area, POC, HVN and LVN: reading the auction's map
thumb: Inside value, or testing outside?
---

@chapter The question
@title text="Value Area, POC, HVN, LVN" sub="Volume and Order Flow" art=thumb
Once you've built a volume profile, it gives you a map. Some prices are crowded with trade, some are nearly empty, and one band holds most of the activity. This lesson names those places, and shows how price behaves around them.

@words text="Inside value: accepted" sub="outside value: being tested"
Here's the central idea. Inside value, trade is accepted. Outside value, the market tests whether new prices will be accepted.

@chapter The names
@art value-zone
The value area is a selected percentage of profile volume, concentrated around the Point of Control. Its top edge is the value area high, V A H. Its bottom is the value area low.

@art hvn-lvn
Two more names. A high volume node, H V N, is where the market transacted heavily. A low volume node, L V N, is a price area with relatively little profile volume, where the market transacted less and often moved quickly.

@words text="An LVN is not a promise of speed"
Thin areas are often crossed quickly. But a low volume node describes past trade, not a speed to come. It can equally be traded back through. So treat L V Ns as transition areas, not guaranteed acceleration.

@art hvn-lvn
And don't mix them up with the busy places. The highest volume price is the P O C, or a high volume node. An L V N is the thin part.

@chapter Building the value area
@art build-out
How is the value area drawn? Start at the P O C. Then keep adding neighbouring bins, the larger neighbour first, until the total reaches the target, about seventy percent of the profile's volume.

@math heading="Total 10,000 · target 70%" items="6,600 ÷ 10,000 = 66%@sixty six percent;;66% < 70% → add the 800 bin@short of seventy;;6,600 + 800 = 7,400@seventy four hundred;;7,400 ÷ 10,000 = 74%@seventy four percent"
Here's the lesson's example. A profile totals ten thousand contracts. Built out from the P O C, the value area holds sixty six hundred so far. That's sixty six percent, short of seventy. So the larger neighbouring bin, eight hundred, is added. Now it holds seventy four hundred, which is seventy four percent.

@words text="Approximately 70%"
The area overshoots the target slightly, which is why the lab says approximately seventy percent. And the P O C is where the area starts, not where it stops. Neighbours are added by size.

@chapter Acceptance above value
@art accept-above
Now watch price. It moves above the value area high, and it stays there. What's happening? Higher price acceptance, led by buyers. The market is building trade above the prior value area. That's volume at new prices, not its absence. And it's certainly not an immediate rejection, because rejection would return price into value. Staying above it is the opposite.

@words text="Holding above: buyers · holding below: sellers"
Holding above value shows buyers maintaining higher acceptance. Holding below value shows sellers maintaining lower acceptance.

@chapter Rejection
@art reject-above
Now a different picture. Price briefly moves above the value area high, then comes back inside. That's rejection of higher prices. Buyers failed to maintain trade outside prior value. A quick return means the higher prices attracted little trade.

@words text="Rejection ≠ a guaranteed bearish trend"
But be careful how far you take it. Rejection at the value area high returns price to prior value. It says nothing about whether the value area low holds.

@chapter Where people slip
@list heading="Common mistakes" items="Calling every VAH touch a short@The first|Assuming value equals intrinsic worth@The second|Ignoring how the range was selected@the third"
Three mistakes. The first is calling every touch of the value area high a short. The second is assuming value equals intrinsic worth. It only describes where trade happened. And the third is ignoring how the profile range was selected.

@art zone-not-tick
So use value as a zone, not an exact tick. And remember that acceptance requires time, or follow through, outside value.

@chapter Try it
@list heading="Reading steps" items="Locate current price@locate current price|Observe response@observe the response|State control@state control"
The lab's three steps put it together. First, locate current price. Is it inside, above, below, or moving through a thin node? Then observe the response. Acceptance means continued trade. Rejection means a return toward prior value. Then state control. Outside acceptance identifies which side is maintaining progress.

@words text="Synthetic educational data" sub="no live market connection"
The lab uses synthetic educational data, with no live market connection. Try moving price above value two ways, once where it holds and once where it returns, and describe each in those three steps.

@end text="Inside, above, below, or through?"
You can test acceptance and rejection around value in the lab, on Learn. That's learn dot get er done dot I O.
