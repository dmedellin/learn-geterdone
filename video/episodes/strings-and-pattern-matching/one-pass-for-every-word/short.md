---
format: short
lesson: strings-and-pattern-matching/one-pass-for-every-word
title: Why she and he get found together
---

@art suffix-chain
Why do she and he get reported together, but a and a b never?

@words text="output links follow suffixes"
In Aho Corasick, each node's outputs include the words on its failure chain, and failure links point to suffixes. He is a suffix of she, so they report together.

@words text="a, ab, abc, abcd" sub="never two at one position"
Words nested as prefixes never do. The chain follows the tail, not the start.

@end text="Full lesson on Learn"
Try it on Learn.
