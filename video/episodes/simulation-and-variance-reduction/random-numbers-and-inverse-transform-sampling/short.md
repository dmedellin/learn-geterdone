---
format: short
lesson: simulation-and-variance-reduction/random-numbers-and-inverse-transform-sampling
title: The sampling shortcut that ignores your probabilities
---

@art uniform-shortcut
The most common sampling shortcut ignores every probability you gave it.

@words text="⌊k·U⌋ + 1"
Floor of k times U, plus one, picks each of k values equally often, whatever the table says.

@art draw-lands
Instead, build the cumulative table and return the first value whose cumulative probability is above U. Each band's width is exactly that value's probability.

@end text="Full lesson on Learn"
The full lesson, with every draw shown, is on Learn.
