---
format: short
lesson: code-complete-high-quality-code/design-heuristics-and-information-hiding
title: Hiding a secret added a module, and still won
---

@art exposed-format
Hiding a file format made the design bigger. Here's why that's a win.

@words text="5 modules know the format"
Five modules each read a CSV format themselves. Change it, and you edit all five.

@art hidden-format
Move the format inside one module, store. Now the change reaches one more module, because store is new. But only one module knows the secret.

@words text="Edit 1, not 5"
So you edit one, not five. That's information hiding.

@end text="Full lesson on Learn"
The full lesson, with a lab to count who knows a secret, is on Learn.
