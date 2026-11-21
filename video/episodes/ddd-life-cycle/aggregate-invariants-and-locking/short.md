---
format: short
lesson: ddd-life-cycle/aggregate-invariants-and-locking
title: Twelve places, fourteen booked
---

@words text="12 places · 14 booked"
A class with twelve places ends up with fourteen booked, and every check passed.

@art two-copies
Pat and Sam each edit a different party. Each checks the total in their own copy: twelve, and eleven. Both commit. The stored sum is fourteen.

@art refused-wait
Lock the whole aggregate instead, and Sam's edit is refused. The sum stays at twelve. The rule holds, and Sam waits.

@end text="Full lesson on Learn"
Run both locking schemes in the full lesson on Learn.
