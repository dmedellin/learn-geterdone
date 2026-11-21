---
format: long
lesson: availability-and-failure/redundancy-and-parallel-paths
title: Redundancy: two 99 percent paths make 99.99, until you count the failover
thumb: The switch is not free
---

@chapter The question
@title text="Parallel: Redundancy" sub="Availability and Failure" art=thumb
Put two servers side by side, each ninety nine percent available. Together they're ninety nine point nine nine. That's the promise of redundancy. Then you charge for the switching, and the story changes.

@art parallel-paths
Paths are in parallel when any one of them can serve the request. So the whole thing is down only when every path is down at once.

@chapter The formula
@math heading="Parallel availability" items="1 − A = ∏ (1 − Aᵢ)@the chance that all;;A = 1 − ∏ (1 − Aᵢ)@one minus"
Under independence, the chance that all are down is the product of their unavailabilities. So A is one minus that product. Working with the complement turns an or over many events into an and, which is much easier.

@math heading="Each path 99/100" items="n = 1:  1/100  →  99%@one path;;n = 2:  1/10 000  →  99.99%@two paths;;n = 3:  1/10⁶  →  99.9999%@three;;n = 4:  1/10⁸  →  99.999999%@four"
Each path is down a hundredth of the time. With one path, you're ninety nine percent. Two paths are both down one time in ten thousand, four nines. Three gives six nines, and four gives eight.

@words text="Parallel: unavailabilities multiply" sub="Series: unavailabilities add"
So two nines plus two nines is four nines, in parallel. Be precise about why, because the same reader will add nines in series, where it's false. In parallel, the unavailabilities multiply. In series, they add.

@chapter Charging for the failover
@art failover-gap
But that formula assumes the switch is instant. Real cutovers take a health check, a timeout, a decision and a reconnection. Every second of that is a second the request isn't served.

@math heading="30 s failover, 12 times a year" items="charge = (30 s × 12) / 31 536 000 s@thirty seconds;;= 360/31 536 000 = 1/87 600@one eighty seven;;n = 2:  99.990000%  →  99.988858%@two paths"
The correction is arithmetic. Failover seconds times events, over the period. Thirty seconds twelve times a year is three hundred and sixty seconds, one eighty seven thousand six hundredth of a year. Two paths go from ninety nine point nine nine to ninety nine point nine eight eight eight five eight percent.

@art flat-charge
That's six minutes a year, and it doesn't shrink when you add a replica, because it isn't a property of the replicas. It's a property of the switching.

@chapter Where replicas stop paying
@list heading="Real availability" items="2 paths: 99.988858%@two paths|3 paths: 99.998758%@three give|4 paths: 99.998857%@four give"
With that failover, two paths give ninety nine point nine eight eight eight five eight. Three give ninety nine point nine nine eight seven five eight. Four give ninety nine point nine nine eight eight five seven. The ideal goes from four nines to eight. The real figure has essentially stopped by three.

@chapter Quiet assumptions
@art overloaded-survivor
The formula assumes three more things. That paths fail independently, which is the next lesson. That one path can carry the whole load: two paths at sixty percent each leave an overloaded system when one goes.

@art standby-dust
And it assumes the redundancy is exercised. A standby that has never served a request is a component with an unmeasured availability, and it is not point nine nine.

@art series-in-disguise
Here's a trap. A cache is added in front of a database, and a cache error fails the request. That's not redundancy. The request needs both, so it's in series. Point nine nine nine times point nine nine nine is ninety nine point eight percent, below the database alone. The error handling decides, not the diagram.

@chapter Two regions
@math heading="Two regions at 999/1000" items="ideal: (1/1000)² = 1/10⁶  →  99.9999%@six nines;;4 × 90 s = 6 min a year@four regional failovers;;real: 99.998758%  ·  four nines@four nines in the year"
Two regions at three nines each give an ideal six nines, thirty one and a half seconds a year. But four regional failovers at ninety seconds is six minutes a year. The real figure is ninety nine point nine nine eight seven five eight. Six nines on the slide, four nines in the year.

@chapter Where people slip
@list heading="Common slips" items="Taking the ideal figure into a plan@The first|Calling a required component redundant@The second|Adding replicas after switching dominates@The third"
The first slip is taking the ideal figure into a plan. Quote the charged figure, and the charge separately. The second is calling a required component redundant. The third is adding replicas once the switching dominates. The next replica improves a term that no longer matters.

@chapter Try it
@words text="Third region, or a 45 s failover?" sub="write the ideal and the charge separately"
Your turn. Keep two regions. You can add a third region, or halve the failover to forty five seconds. Write the ideal unavailability and the charge separately, and see which one each option touches. Then say which you'd buy, and what you assumed about independence.

@end text="Charge the failover yourself"
You can add replicas and failover time and watch which term dominates, on Learn. That's learn dot get er done dot I O.
