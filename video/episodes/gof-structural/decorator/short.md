---
format: short
lesson: gof-structural/decorator
title: Same three wrappers, different price
---

@art nested-wrappers
Same seat, same three add ons. Why do you get two different prices?

@art in-and-out
Each decorator wraps the price inside it, and works on what that one returns.

@math items="(32 + 2.50) × 0.9 + 1.75 = 32.8@fee first;;(32 + 1.75) × 0.9 + 2.50 = 32.875@reverse it"
Fee first, then the discount, then insurance: thirty two point eight. Reverse it, and you get thirty two point eight seven five.

@words text="Order is part of the design"
The discount applied after the fee discounts the fee too.

@end text="Full lesson on Learn"
That's Decorator. The full lesson is on Learn.
