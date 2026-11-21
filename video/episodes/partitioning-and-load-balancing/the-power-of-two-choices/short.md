---
format: short
lesson: partitioning-and-load-balancing/the-power-of-two-choices
title: One extra lookup flattens your load
---

@art two-probes
Want a flatter fleet for one extra lookup? Look at two bins, not one.

@math items="one choice:  max 5 or 6@five or six;;two choices:  max 3, every seed@every single seed"
A thousand and twenty four keys into a thousand and twenty four bins. One random choice left a fullest bin of five or six. Picking the lighter of two random bins left three, on every single seed.

@words text="Lower and steadier"
No global view, no coordination. Just one extra look.

@end text="Full lesson on Learn"
The full lesson, with both rules side by side, is on Learn.
