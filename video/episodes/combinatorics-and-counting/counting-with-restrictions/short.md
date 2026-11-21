---
format: short
lesson: combinatorics-and-counting/counting-with-restrictions
title: Why the second digit gets nine choices
---

@art freed-value
All digits different, no leading zero. So why nine choices for the second digit?

@math items="first: 9, anything but 0@nine choices;;second: 9, anything but the first@also nine;;9 · 9 · 8 · 7 = 4536@four thousand five hundred and thirty six"
The first digit can't be zero, so it has nine choices. The second can be anything except the first digit, and that includes zero, so it's also nine. Then eight, then seven: four thousand five hundred and thirty six.

@words text="Kept out here, free there"
Keeping zero out of the first position is exactly what frees it for the second.

@end text="Full lesson on Learn"
The full lesson, with cases and complements, is on Learn.
