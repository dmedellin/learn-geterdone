---
format: short
lesson: measuring-systems/sampling-and-rare-events
title: 1% sampling catches a 10-request problem 9.56% of the time
---

@art sparse-sample
You sample one percent of requests. A problem makes ten slow ones. You'll probably see none of them.

@math items="1 − (99/100)¹⁰ = 9.56%@one minus;;95% needs s = 25.9%@ninety five percent"
The chance of catching at least one is one minus ninety nine hundredths to the tenth, nine point five six percent. For ninety five percent confidence, you'd need to sample twenty five point nine percent.

@words text="Keep the tail, and reweight the rest"
Or keep every slow request, and count the rest by their rate.

@end text="Full lesson on Learn"
The full lesson, with reweighting worked out, is on Learn.
