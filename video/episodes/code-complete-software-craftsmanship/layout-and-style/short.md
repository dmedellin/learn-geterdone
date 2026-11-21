---
format: short
lesson: code-complete-software-craftsmanship/layout-and-style
title: This indentation lies about your code
---

@art else-binding
This else is indented under the wrong if, and Java doesn't care.

@code block=1 lines=1-8 label=Java focus="5-6@the else"
It looks like inactive users get a letter. But neither if has braces, and the else belongs to the nearest if without one. So inactive users get nothing.

@art braces-fix
Layout should show the structure the compiler reads. Use braces, and the indentation can't lie.

@end text="Full lesson on Learn"
The full lesson, with a layout lab, is on Learn.
