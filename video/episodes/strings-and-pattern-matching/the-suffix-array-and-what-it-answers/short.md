---
format: short
lesson: strings-and-pattern-matching/the-suffix-array-and-what-it-answers
title: Find the longest repeat by sorting suffixes
---

@art contiguous-block
To find the longest repeat in a text, you only need to compare neighbours.

@words text="a · ana · anana · banana · na · nana"
Sort every suffix of banana. Any substring that appears twice starts two suffixes, and sorting puts them in one block.

@words text="largest overlap: ana (3)"
So check each suffix against the one above it. The biggest overlap, a n a and a n a n a, is the longest repeat.

@end text="Full lesson on Learn"
Try any text on Learn.
