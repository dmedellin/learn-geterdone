---
format: short
lesson: simulation-and-variance-reduction/discrete-event-simulation-of-a-queue
title: Two ways to average a queue, and only one is right
---

@art weighted-average
One customer for nine hundred slots, nine for a hundred. What's the average?

@math items="time average: 1.8@one point eight;;average of the states: 5@five"
Weight by time, and it's one point eight. Average the two states, and it's five.

@art step-function
The number in the system is a step function. Its time average is the area underneath, divided by the length of the window. That's the number anyone actually wants.

@end text="Full lesson on Learn"
The full lesson, with a whole run, is on Learn.
