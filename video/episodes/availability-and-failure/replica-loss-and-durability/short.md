---
format: short
lesson: availability-and-failure/replica-loss-and-durability
title: Halving your rebuild time cuts data loss risk by four
---

@art rebuild-lever
With three copies of your data, a faster rebuild is worth more than you think.

@math items="P ≈ N! × fᴺ × (R/8760)ᴺ⁻¹@N factorial;;R: 24 h → 12 h  ⇒  ÷ 4@halve the window"
The loss estimate is N factorial times f to the N, times the repair window fraction to the N minus one. Three copies means the window is squared. Halve the window, and the risk falls by four.

@words text="A week instead of a day: × 49"
And a week long rebuild instead of a day costs a factor of forty nine.

@end text="Full lesson on Learn"
The full lesson, with every lever to move, is on Learn.
