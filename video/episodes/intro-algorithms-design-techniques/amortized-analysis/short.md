---
format: short
lesson: intro-algorithms-design-techniques/amortized-analysis
title: Why doubling a table costs only 3 per insert
---

@art table-doubling
Copying a whole table sounds expensive. Spread out, it costs three per insert.

@list items="1 to insert the item@pays to insert|1 to move it later@pays to move it|1 to move an older item@pays to move an item"
Charge each insertion three. One pays to insert the item. One pays to move it at the next doubling. And one pays to move an item that's already moved once.

@words text="n insertions < 3n"
So any n insertions cost less than three n, even though one of them might copy everything.

@end text="Full lesson on Learn"
Price a table yourself in the full lesson on Learn.
