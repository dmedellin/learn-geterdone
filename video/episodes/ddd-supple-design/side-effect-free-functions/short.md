---
format: short
lesson: ddd-supple-design/side-effect-free-functions
title: Double one patient's dose, and two more doses double
---

@art shared-dose
Double one patient's dose, and two other patients' doses double too.

@math items="in place: 3 see it · 2 surprised@in place;;new value: 1 sees it · 0 surprised@new value"
Three prescriptions share one five milligram dose. Change it in place, and all three see it, so two are surprised. Return a new value for Ben instead, and only Ben sees it. Nobody is surprised.

@words text="Return a new value" sub="change nothing that exists"
That's a side effect free function. It calculates, returns a result, and changes nothing.

@end text="Full lesson on Learn"
Count the surprised holders yourself in the full lesson on Learn.
