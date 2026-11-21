---
format: short
lesson: availability-and-failure/retry-storms
title: The retries aren't a response to the overload. They are the overload.
---

@art feedback-loop
Ninety five percent load, three retries. Your service settles at a hundred and seventy three percent.

@math items="0.95  →  1.06  →  1.11  →  1.17  →  1.24@point nine five;;settles at 1.727@settles"
Retries add load, load adds failures, failures add retries. Point nine five, one point oh six, one point one one, and up. It settles at one point seven two seven times capacity.

@words text="Retries off  →  0.95"
Switch the retries off, and the load drops straight back to point nine five.

@end text="Full lesson on Learn"
The full lesson, with the fixed point bracketed, is on Learn.
