---
format: short
lesson: sorting-and-selection/k-way-merge-and-external-sorting
title: The heap merge loses on comparisons and wins on disk
---

@art run-heads
Merging eight runs through a heap makes more comparisons than merging them in pairs.

@math items="heap:  302 comparisons,  1 pass@through a heap;;pairs:  180 comparisons,  7 passes@in pairs"
Sixty four items through a heap cost three hundred and two comparisons in one pass. In pairs, a hundred and eighty comparisons, but seven passes.

@words text="On disk, a pass is the cost"
When the data lives on disk, every pass rereads everything. So the heap wins.

@end text="Full lesson on Learn"
The full lesson, with the pass formula, is on Learn.
