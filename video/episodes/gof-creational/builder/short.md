---
format: short
lesson: gof-creational/builder
title: Write the parser once, for every format
---

@art rtf-converters
One document reader, an endless list of output formats. Do you rewrite the parser each time?

@art director-builder-client
No. The reader is a director. It walks the input and tells a builder which part comes next. Each builder decides what that part becomes: plain text, a page, a shopping list.

@words text="A new format is one builder"
The parsing is written once. A new output is one new class. That's Builder.

@end text="Full lesson on Learn"
The full lesson, with a recipe book to count, is on Learn.
