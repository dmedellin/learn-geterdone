---
format: long
lesson: data-structures/augmenting-a-tree
title: Augmenting a search tree: rank and select in log n
thumb: One number per node
---

@chapter The question
@title text="Augmenting a Tree" sub="Data Structures" art=thumb
What's the third smallest key in a search tree? Without help, you'd walk the whole thing in order and count. Store one extra number at each node, and you can answer in a single path.

@chapter The size field
@art size-tree
Each node x stores the size of its subtree: the size of its left subtree, plus the size of its right, plus one. An empty subtree has size zero. It's one word per node, and nothing else about the tree changes.

@chapter Select
@list heading="select(i): the i-th smallest" items="i = L + 1:  this node@equals L plus one|i ≤ L:  go left, same i@at most L|otherwise:  go right, i − (L + 1)@Otherwise"
At a node, let L be the size of its left subtree. If i equals L plus one, it's this node, because exactly L keys here are smaller. If i is at most L, go left with the same i. Otherwise, go right, and subtract L plus one from i.

@math heading="select(3), tree from 50 25 75 12 37 62 87 6 18" items="at 50:  L = 5,  3 ≤ 5,  left@at fifty;;at 25:  L = 3,  3 ≤ 3,  left@at twenty five;;at 12:  L = 1,  3 > 2,  i = 1,  right@at twelve;;at 18:  L = 0,  1 = 0 + 1  ⟹  18@at eighteen"
Here's a nine key tree. Select three. At fifty, L is five, and three is at most five, so go left. At twenty five, L is three, go left again. At twelve, L is one. Three is more than two, so i becomes one and we go right. At eighteen, L is zero, and one equals zero plus one. The answer is eighteen.

@art select-walk
That's four nodes visited, one path down. Without the size field, you'd need an in order traversal, counting as you go, and that's order n.

@chapter Rank
@art rank-walk
Rank goes the other way. How many keys are at most k? Walk toward k, keeping a count. Each time you go right, the whole left subtree and the node are below k, so add L plus one. Going left adds nothing. When you find k, add L plus one a last time.

@math heading="rank(62)" items="at 50:  go right,  add 5 + 1 = 6@add five plus one;;at 75:  go left,  add 0@add nothing;;at 62:  found,  add 0 + 1  ⟹  7@found it"
Rank of sixty two. At fifty, sixty two is bigger, so add five plus one, six, and go right. At seventy five, go left and add nothing. At sixty two, found it, add zero plus one. The rank is seven.

@words text="O(height)" sub="O(log n) only if the tree stays short"
Four nodes for select, three for rank. Each is one path, so the cost is order height. That's log n only when the tree is balanced, which is why an order statistic tree is an AVL tree with a size field.

@art range-count
And counting a range is two rank walks. How many keys lie between twenty and seventy? Count the keys at most seventy, and subtract those below twenty. The lab finds four: twenty five, thirty seven, fifty and sixty two, from seven nodes visited.

@chapter What can ride along
@words text="f(x) from key(x), f(left), f(right), in O(1)"
Here's the rule for any extra field. You can maintain it cheaply if a node can compute it in constant time from its own key and its two children's values. Then an insert only touches one path, and a rotation only touches two nodes.

@list heading="Can it ride along?" items="size:  1 + left + right ✓@Size qualifies|sum:  key + left + right ✓@sum|min:  min(key, left) ✓@min|median ✗@A median doesn't"
Size qualifies. So does sum, and min. A median doesn't.

@art median-no
Knowing one key and the medians of two subtrees doesn't tell you the median of the whole. So the field would have to be rebuilt, and the technique buys nothing. The question about any field isn't whether it's useful. It's whether a node can rebuild it from its two children.

@chapter The rotation update
@math heading="Rotate left at 25" items="25:  3 + 0 + 1 = 4@Recompute twenty five;;37:  4 + 0 + 1 = 5@then thirty seven;;50:  5 + 3 + 1 = 9, unchanged@fifty"
Every structural change must update the field. Rotate left at twenty five, and thirty seven rises. Recompute twenty five first: three plus zero plus one, four. Then thirty seven: four plus zero plus one, five. Fifty stays at nine, as it must.

@art stale-field
The order matters. The node that went down comes before the node that rose, because the riser depends on it. Skip the update, and the tree is still a correct search tree, but select returns the wrong key and nothing complains.

@chapter Where people slip
@list heading="Common slips" items="Not reducing i when select goes right@The first|Adding to the rank on a left turn@The second|Treating the field as free@And the third"
The first slip is forgetting to reduce i when select goes right, which gives answers consistently too small. The second is adding to the rank on a left turn, which counts nodes visited instead. And the third is treating the field as free, and skipping the rotation update.

@chapter Try it
@words text="select(6) and rank(37)" sub="tree from 50 25 75 12 37 62 87 6 18"
Your turn. On the same nine key tree, work out select of six and rank of thirty seven by walking one path each. Write down L at every node.

@end text="Walk the sizes yourself"
You can run rank and select on a size annotated tree and rotate it, on Learn. That's learn dot get er done dot I O.
