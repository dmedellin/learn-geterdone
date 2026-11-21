---
format: short
lesson: integer-programming/either-or-constraints-and-disjunctions
title: Writing both constraints made my schedule infeasible
---

@art contradiction-arrows
Two jobs, one machine. Write both orders into the model, and nothing is feasible.

@math items="x₁ − x₂ ≤ −4@minus four;;−x₁ + x₂ ≤ −3@minus three;;0 ≤ −7@zero"
Job one before job two is x one minus x two, at most minus four. Job two first is minus x one plus x two, at most minus three. Add them: zero at most minus seven.

@words text="Constraints hold together. Use a binary."
Rows are simultaneous, so writing both asks for both. A binary picks one.

@end text="Full lesson on Learn"
The full lesson, with both branches solved, is on Learn.
