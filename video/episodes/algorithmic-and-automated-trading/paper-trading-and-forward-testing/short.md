---
format: short
lesson: algorithmic-and-automated-trading/paper-trading-and-forward-testing
title: The 108 basis points your backtest missed
---

@art shadow-mode
Your backtest assumed two basis points per fill. Shadow mode says eleven.

@math items="11 − 2 = 9 bps per fill@eleven minus two;;12 × 9 = 108 bps ≈ 1.1%@twelve times nine"
Over twelve signals, the gap is eleven minus two, nine basis points per fill. Twelve times nine is a hundred and eight basis points, about one point one percent.

@words text="Name every basis point"
Each one needs a cause before you go further.

@end text="Full lesson on Learn"
Compare backtest and shadow in the full lesson on Learn.
