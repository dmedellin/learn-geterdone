---
format: long
lesson: greedy-and-matroids/interval-partitioning-and-the-depth
title: How many rooms do you need? Interval partitioning and the depth
thumb: The bound greedy meets exactly
---

@chapter The question
@title text="Interval Partitioning and the Depth" sub="Greedy Algorithms and Matroids" art=thumb
You've got a pile of lectures, each with a start and a finish, and every one of them has to happen. How few rooms can you get away with?

@art rooms-rows
That's interval partitioning. Unlike interval scheduling, nothing gets thrown away. Every interval goes into a room, and no room can hold two that overlap. The question is just how many rooms you need.

@chapter The greedy rule
@words text="Sort by start · first free room · else open a new one"
The greedy rule is simple. Sort the intervals by start time. Put each one in the lowest numbered room whose last booking has already finished. And only open a new room when none is free.

@words text="A 0–3 · B 1–4 · C 2–5 · D 4–7 · E 5–8" sub="F 6–9 · G 8–11 · H 9–12 · I 10–13 · J 12–15"
The lab opens on ten lectures. A runs from zero to three, B from one to four, C from two to five, and so on, up to J, from twelve to fifteen.

@list heading="Greedy by start time" items="Room 1: A D G J@Room one|Room 2: B E H@room two|Room 3: C F I@room three"
Greedy opens three rooms. Room one gets A, D, G and J. Room two gets B, E and H. And room three gets C, F and I. Every room is checked, and all ten were placed exactly once.

@chapter A bound on every schedule
@art alive-at-t
But is three the best? Here's a number no schedule can beat. Pick an instant, and look at the intervals alive at that moment. They all contain that instant, so every two of them overlap, so no two can share a room.

@math heading="Depth" items="alive at t:  s ≤ t < f@alive at t;;depth = most intervals alive at one instant@The depth"
An interval is alive at t when its start is less than or equal to t, and t is less than its finish. The depth is the most intervals alive at any single instant. Nothing in that definition mentions an algorithm, which is why it bounds all of them.

@words text="t = 2:  A 0–3 · B 1–4 · C 2–5" sub="depth 3 · greedy used 3"
On the ten lectures, the depth is three, at time two, where A, B and C are all alive. Those three pairwise overlap, so every schedule needs at least three rooms. Greedy used three. Two separate routines, and they agree.

@art certificate
That list of three intervals is a certificate. You don't have to trust that the depth is three. You can check by eye that A, B and C really overlap, in a few seconds.

@chapter Why greedy never needs more
@art busy-rooms
Now the proof that greedy always meets the depth. Suppose greedy opens room d plus one while placing some interval x. It only does that when rooms one through d are all busy, each holding an interval that hasn't finished by the start of x.

@math heading="Suppose room d + 1 opens for x" items="d busy intervals: s ≤ s(x) < f@So all d are alive;;plus x itself: d + 1 alive at s(x)@plus x itself;;so depth ≥ d + 1  ✗@contradiction"
Each of those started at or before x, because greedy goes in start order. So all d are alive at the start of x. Plus x itself, that's d plus one intervals alive at one instant. So the depth would be at least d plus one, a contradiction.

@art rooms-and-depth
This proof never mentions an optimal solution. It shows every schedule needs at least d rooms, and this one uses at most d. Two inequalities from two arguments, meeting. Later, approximation ratios use the same shape, with a gap between the two sides.

@chapter Does the order matter?
@art finish-order
The proof uses start order. The panel also offers finish order, and on all four shipped instances it opens the same number of rooms. It's tempting to conclude the order doesn't matter. That's four inputs, not all of them.

@math heading="0–1, 1–4, 2–5, 4–9, 5–8  ·  depth 2" items="by start:  A B D · C E  →  2 rooms@By start time;;by finish:  A B E · C · D  →  3 rooms@By finish time"
Type zero to one, one to four, two to five, four to nine, five to eight. The depth is two. By start time, greedy opens two rooms. By finish time, it opens three, because E slips into the first room, and then D fits nowhere.

@chapter Where people slip
@list heading="Common slips" items="Reading the depth off the schedule@The first|Concluding the order doesn't matter@The second|Filing this with stays ahead and exchange@The third"
The first slip is reading the depth off the schedule. Then the two numbers agree by construction and prove nothing. The second is concluding from the presets that the order doesn't matter. The third is treating this as the same kind of proof as stays ahead or exchange. This one never compares against an optimum.

@chapter Try it
@words text="0–1 · 1–4 · 2–5 · 4–9 · 5–8"
Your turn. Schedule these five by hand, first in start order, then in finish order. Then find an instant where two intervals are alive, and explain why it certifies that two rooms is the best possible.

@end text="Find the certificate yourself"
You can schedule your own intervals and see the depth and its certificate, on Learn. That's learn dot get er done dot I O.
