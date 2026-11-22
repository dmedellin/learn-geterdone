---
format: short
lesson: backtesting-and-trading-systems/trade-execution-simulation
title: Your stop at 100 can fill at 98.50
---

@art gap-through-stop
Your stop is at one hundred. You can still get out at ninety eight fifty.

@math items="stop 100.00 · next open 98.50@next bar opens;;exit = 98.50@exit;;1.50 beyond the stop@one point five"
If the next bar opens at ninety eight point five and never trades above ninety nine, the exit is ninety eight point five. That's one point five beyond the stop.

@words text="A stop is a trigger, not a price"
A gap triggers the stop. The fill comes at the first available price.

@end text="Full lesson on Learn"
Simulate gaps and fills in the full lesson on Learn.
