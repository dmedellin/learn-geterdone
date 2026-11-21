---
format: short
lesson: capacity-estimation/peak-to-average
title: The correct number that sizes your system wrong
---

@art evening-gap
Your average rate is computed perfectly. And your system still falls over every evening.

@math items="mean 5 277.78 req/s@the mean;;peak 12 777.78 req/s@the busiest hour;;short by 7 500 req/s@seven thousand five hundred"
Four hundred and fifty six million requests a day is a mean of about five thousand two hundred and seventy eight a second. But the busiest hour runs at about twelve thousand seven hundred and seventy eight. Sized to the mean, you're seven thousand five hundred short.

@words text="Pay for the mean. Build for the peak."

You pay for the mean, and you build for the peak.

@end text="Full lesson on Learn"
The full lesson, with the day's profile to reshape, is on Learn.
