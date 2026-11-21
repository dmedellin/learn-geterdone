---
format: long
lesson: randomised-algorithms/the-count-min-sketch
title: The Count-Min sketch: counting a stream in fixed memory
thumb: Never below the truth
---

@chapter Fixed memory
@title text="The Count-Min Sketch" sub="Randomised Algorithms" art=thumb
How do you count how often each key appears in a stream, when there are more distinct keys than you have memory for? A Count Min sketch uses a fixed grid of counters. Its estimates are never too low, and you can bound how high they go.

@art counter-grid
The sketch is d rows of w counters, all starting at zero, with one hash function per row. To update a key, increment its counter in every row. To estimate a key's count, take the minimum of its d counters. The space is d times w, fixed in advance.

@art stream-arrows
An exact frequency table grows with the number of distinct keys. A sketch stays the size you chose when you built it. The price is an error you can bound.

@chapter Never below the truth
@art one-key-rows
Every update of key x raises x's counter in each row. Other keys can land in the same cell and raise it further. Nothing ever lowers it. So every one of x's counters is at least its true count, and so is their minimum. On every stream, with every hash choice.

@chapter How far above
@art one-key-rows
So how far above the truth can it go? Let F one be the total number of updates in the stream.

@math heading="One row" items="E[overcount] ≤ F₁/w@F one over w;;Markov:  P(overcount ≥ 2F₁/w) ≤ 1/2@Markov's inequality;;d independent rows:  ≤ 2⁻ᵈ@two to the minus d"
In one row, each other update lands in x's cell with probability one over w, so the expected overcount is at most F one over w, by linearity. It's never negative, so Markov's inequality says it reaches two F one over w with probability at most a half. With independent rows, all d must overcount that much, so it's at most two to the minus d.

@words text="2/w and 2⁻ᵈ" sub="what Markov alone proves"
Markov's inequality does all the probabilistic work here, the one proved earlier in this course. The panel prints two over w and two to the minus d, because that's the guarantee you can derive with what you've been shown.

@chapter A heavy hitter
@words text="64 updates · 12 keys" sub="key 1 × 40 · keys 2, 3 × 3 · keys 4–12 × 2"
The lab's stream is sixty four updates over twelve keys. Key one arrives forty times. Keys two and three arrive three times each, and keys four to twelve twice each. The sketch has w equals eight and d equals three.

@math heading="w = 8,  d = 3" items="192 increments, 36 reads@a hundred and ninety two;;5 keys overcounted, each by exactly 2@five keys;;key 1: 42 vs 40@forty two;;bound: 2·64/8 = 16, with probability ≥ 7/8@sixteen"
That's a hundred and ninety two increments and thirty six reads. Every estimate is at or above the truth. Five keys are overcounted, each by exactly two. Key one reads forty two against forty. The bound allows an error of sixteen, with probability at least seven eighths. The worst seen was two.

@art relative-error
Look at who got overcounted. The heavy hitter, by two, five per cent. And four light keys, also by two. An estimate of four for a true count of two is off by a factor of two. The bound is additive in F one, and says nothing about relative error. That's why sketches find heavy hitters, not rare keys.

@chapter Two knobs
@art wide-vs-deep
w controls how big the error can be, and d controls the chance of exceeding it. Doubling w halves two F one over w. Adding a row halves two to the minus d. The space is their product, so the same memory can buy different guarantees.

@words text="w = 12, d = 4:  bound 32/3 ≈ 10.67, P ≤ 1/16" sub="worst overcount 0"
With w equals twelve and d equals four, over sixty four updates across twelve keys, the bound becomes thirty two thirds, about ten point six seven, with failure probability one sixteenth. And every estimate came out exactly right. A wider sketch collides less.

@art uniform-stream
When nothing collides in at least one row per key, the sketch is exact. Ten keys, six updates each, at eight by three: worst overcount zero. That's this stream being kind, not the structure promising accuracy. A different hash choice gives a different table.

@chapter Where people slip
@list heading="Common slips" items="Expecting close, not never low@The first|Quoting a sharper bound you can't derive@The second|Reading an exact table as exactness@And the third"
The first slip is expecting the estimate to be close, rather than never low. The guarantee allows sixteen out of sixty four here. The second is quoting a sharper textbook bound without a proof you can follow. And the third is reading an exact table as evidence the sketch is exact. Change the stream, and collisions return.

@end text="Never below the truth"
Stream your own keys into the grid and read the minimum, on Learn. That's learn dot get er done dot I O.
