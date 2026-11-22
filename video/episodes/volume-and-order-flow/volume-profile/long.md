---
format: long
lesson: volume-and-order-flow/volume-profile
title: Volume profile: where the market spent its activity
thumb: Volume by price, not time
---

@chapter The question
@title text="Volume Profile" sub="Volume and Order Flow" art=thumb
Ordinary volume bars sit under the chart, one per time period. They tell you when trading happened. But often the better question is where. At which prices did the market actually do its business?

@art profile-sideways
A volume profile answers that by turning volume on its side. It organises traded volume by price rather than time. Each horizontal bar is the total volume assigned to one price bin, over a range you select.

@words text="High volume = acceptance" sub="low volume = limited trade"
The core reading is this. High volume prices show acceptance. Low volume prices show limited trade, where price moved through quickly.

@chapter The Point of Control
@art poc-bar
The longest bar has a name. The Point of Control, or P O C, is the price bin with the greatest measured volume. It's where trade concentrated, the price the whole window kept returning to.

@words text="Not the highest price · not the last close"
So it isn't the highest price. The top of the range is usually one of the thinnest bins. And it isn't the last close. The last close is a point in time. The P O C is a price.

@chapter Worked example
@math heading="Four bins" items="99: 400 · 100: 1,200 · 101: 900 · 102: 300@four bins;;total = 2,800@twenty eight hundred;;POC = 100 (1,200)@the busiest bin"
Here's the lesson's example. Four bins hold four hundred, twelve hundred, nine hundred and three hundred contracts, at prices ninety nine, one hundred, one oh one and one oh two. The total is twenty eight hundred. The busiest bin is one hundred, with twelve hundred. That's the P O C.

@math heading="The two busiest bins" items="1,200 + 900 = 2,100@together they hold;;2,100 ÷ 2,800 = 75%@seventy five percent;;✗  1,200 ÷ 2,800 ≈ 43%: POC alone@forty three percent;;✗  900 ÷ 2,800 ≈ 32%: one bin@thirty two"
Now, what share do the two busiest bins hold? Together they hold twelve hundred plus nine hundred, twenty one hundred. Twenty one hundred over twenty eight hundred is seventy five percent. Forty three percent would be the P O C bin alone, and thirty two percent is the nine hundred bin by itself.

@words text="75% > 70%"
That seventy five percent already exceeds the seventy percent a value area is drawn to contain. That's the next lesson's idea, but you can see it forming here.

@chapter Shape
@art two-bulges
Beyond the P O C, the whole shape tells you something. A profile's distribution can reveal concentrated acceptance in one place, multiple value areas, or thin transition zones in between.

@art thin-zone
A high volume node most directly represents strong acceptance and repeated trade. The market spent substantial activity there. It's not guaranteed support. A node can attract price back, or be traded through, and the volume count doesn't decide which.

@chapter What it can't tell you
@art both-sides
Can a total volume profile identify buyer initiated versus seller initiated volume? By itself, no. It sums all the volume at each price, so both sides of every trade land in the same bin. Even the P O C is just a bigger bin, not a different kind.

@words text="Where both sides were willing to transact"
That's why the lesson is careful. A profile doesn't say buyers or sellers won by itself. It shows where both sides were willing to transact, and where price moved through quickly.

@chapter Where people slip
@art range-choice
One more thing matters a lot. The selected range changes the profile. Build it from one session, one swing, or the visible chart, and you'll get different shapes from the same prices.

@list heading="Common mistakes" items="Every high-volume node is support@The first|Comparing profiles from different ranges@The second|Reading aggressor from total volume@the third"
Three mistakes follow. The first is treating every high volume node as support. The second is comparing profiles built from different ranges without noting it. And the third is inferring the trade aggressor from total volume at price.

@chapter Try it
@list heading="Reading steps" items="Define the range@define the range|Locate concentration@locate concentration|Locate transitions@locate transitions"
The lab's steps are these. First, define the range: a session, a swing, a visible range, or another fixed sample. Then locate concentration, the P O C and high volume areas. Then locate transitions, the thin areas where price spent little volume.

@words text="Synthetic educational data" sub="no live market connection"
The lab runs on synthetic educational data, with no live market connection. Remember that the P O C identifies activity, not automatic fair value forever. Combine profile location with current price behaviour.

@end text="Turn volume on its side"
You can build profiles from different ranges in the lab, on Learn. That's learn dot get er done dot I O.
