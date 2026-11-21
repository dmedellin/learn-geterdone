---
format: short
lesson: availability-and-failure/backoff-and-jitter
title: Exponential backoff without jitter still hits you all at once
---

@art synced-waves
Six hundred clients fail together. With backoff, they all retry together, too.

@math items="no jitter:  3000/s@three thousand a second;;100% jitter:  925/s@full width jitter"
Every client doubles the same delay, so the retries arrive in waves. Measured in fifth of a second slots, that's three thousand a second at each wave. Add full width jitter, and the peak drops to nine hundred and twenty five.

@words text="Backoff fixes the total · jitter fixes the peak"
Backoff fixes the total. Jitter fixes the peak.

@end text="Full lesson on Learn"
The full lesson, with a seeded outage to replay, is on Learn.
