---
format: short
lesson: code-complete-high-quality-code/exceptions-and-barricades
title: Validate at the wall, assert inside it
---

@art watertight-hull
Error handling or an assertion? Ask which side of the wall it's on.

@art operating-room
Steve McConnell calls it a barricade. Choose the interfaces where data crosses into your program, and check and clean everything there. Inside, the data is supposed to be clean already.

@words text="Outside: validate · Inside: assert"
So outside, use error handling. Inside, use assertions. Bad data found inside is a bug.

@end text="Full lesson on Learn"
The full lesson, with a lab to apply the rule, is on Learn.
