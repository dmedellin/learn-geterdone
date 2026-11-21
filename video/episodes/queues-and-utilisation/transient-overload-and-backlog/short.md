---
format: short
lesson: queues-and-utilisation/transient-overload-and-backlog
title: A one minute spike is a three and a half minute incident
---

@art asymmetric-triangle
Traffic spiked for one minute. Why was the incident three and a half minutes long?

@math items="build: 500/s × 60 s = 30 000@five hundred;;drain: 30 000 ÷ 200/s = 150 s@two hundred"
The backlog built at five hundred a second for sixty seconds, thirty thousand requests. Afterwards, only two hundred a second of headroom was left to clear it. That's a hundred and fifty more seconds.

@words text="It drains at the headroom, not at μ"
It drains at the headroom, not at mu. And the worst lag comes at the moment the spike ends.

@end text="Full lesson on Learn"
The full lesson, with the spike to reshape, is on Learn.
