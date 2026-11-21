---
format: short
lesson: intro-algorithms-sorting/radix-sort-and-bucket-sort
title: Radix sort starts at the wrong end, on purpose
---

@art lsd-passes
Radix sort sorts on the last digit first. That sounds backwards, and it's exactly right.

@art stable-pass
Each pass sorts the whole array on one digit, and keeps keys with equal digits in the order they arrived. So the earlier passes' work survives.

@words text="Unstable pass: 158 before 145"
Use an unstable pass, and it breaks. One fifty eight lands ahead of one forty five.

@end text="Full lesson on Learn"
Break it yourself in the full lesson on Learn.
