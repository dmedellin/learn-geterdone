---
format: short
lesson: intro-algorithms-design-techniques/longest-common-subsequence
title: STONE and NOTES share only two letters in order
---

@art substring-vs-subsequence
STONE and NOTES use exactly the same letters. Their longest common subsequence is two.

@words text="Same letters, different order"
A common subsequence has to keep its letters in order in both words. Rearranging the letters breaks almost every match.

@art arrow-path
The LCS table counts order, not letters. Fill it, follow the arrows back from the corner, and you can check it yourself.

@end text="Full lesson on Learn"
Fill the table in the full lesson on Learn.
