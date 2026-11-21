---
format: short
lesson: gof-behavioral-requests/iterator
title: Eighth, fifth, or tenth?
---

@art tree-preorder
One question in a quiz's tree. Is it eighth, fifth, or tenth?

@words text="Pre · post · level"
All three. Walk the tree pre order, node before children, and it's eighth. Post order, children first, it's fifth. Level by level, it's last.

@art two-walks
That's the Iterator pattern's point. The walk lives in the iterator, not the tree, so you can change the order by changing the iterator.

@end text="Full lesson on Learn"
The full lesson is on Learn.
