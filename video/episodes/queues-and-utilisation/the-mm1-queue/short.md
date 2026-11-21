---
format: short
lesson: queues-and-utilisation/the-mm1-queue
title: The whole M/M/1 queue from one line
---

@art cut-between-states
How many are in a queue on average? One line of balance tells you.

@math items="λπₙ = μπₙ₊₁@crosses the line;;πₙ = (1 − ρ)ρⁿ@geometrically;;L = ρ/(1 − ρ)@the mean"
In the long run, the system crosses the line between n and n plus one as often upward as downward. So each state is rho times the one before, the states decay geometrically, and the mean is rho over one minus rho.

@words text="ρ = 4/5 → L = 4"
At four fifths utilisation, that's four in the system.

@end text="Full lesson on Learn"
The full lesson, with every closed form worked out, is on Learn.
