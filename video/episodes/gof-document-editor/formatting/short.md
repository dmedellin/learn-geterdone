---
format: short
lesson: gof-document-editor/formatting
title: Change the algorithm while the program runs
---

@art compositor-composition
How should an editor break text into lines? Fast, or beautiful? Both.

@words text="The algorithm is an object"
The Gang of Four put the line breaking algorithm in an object of its own, a compositor. The document holds one and asks it to compose.

@art runtime-switch
Want better pages? Hand the document a slower, finer compositor, while it runs. New glyphs and new algorithms never touch each other.

@words text="That's Strategy"
That's the Strategy pattern.

@end text="Full lesson on Learn"
The full lesson, with a lab that counts the classes, is on Learn.
