---
format: short
lesson: code-complete-code-improvements/debugging-as-science
title: Find one bad change in a thousand with ten tests
---

@art halving-line
A thousand changes, and one of them broke a test. You need ten tests.

@words text="Test the middle. Keep the half that fails."
The old build passes. Today's fails. Test the build in the middle, and keep the half that still holds the defect. Then do it again.

@math items="2¹⁰ = 1,024 ≥ 1,000@two to the tenth"
Each test halves the suspects, and two to the tenth is more than a thousand. Just stabilise the failure first, or a passing test means nothing.

@end text="Full lesson on Learn"
The full lesson, with a halving lab, is on Learn.
