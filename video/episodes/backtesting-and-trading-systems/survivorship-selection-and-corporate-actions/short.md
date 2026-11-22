---
format: short
lesson: backtesting-and-trading-systems/survivorship-selection-and-corporate-actions
title: The fake 50% loss in your backtest
---

@art split-cliff
Your backtest says this stock lost half its value overnight. It didn't.

@math items="111.33  →  55.66@one hundred and eleven;;55.66 × 2 ÷ 111.33 − 1 ≈ 0%@Twice the shares"
It split two for one, from one hundred and eleven point three three to fifty five point six six. Twice the shares at half the price: the adjusted return is zero.

@words text="Unadjusted, it books −50%"
An unadjusted series books a fifty percent loss that no holder ever took.

@end text="Full lesson on Learn"
Toggle split adjustment yourself in the full lesson on Learn.
