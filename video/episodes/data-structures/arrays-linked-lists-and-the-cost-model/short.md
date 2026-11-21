---
format: short
lesson: data-structures/arrays-linked-lists-and-the-cost-model
title: Linked list insertion isn't really constant time
---

@art list-walk
Linked lists insert in constant time? Only if you're already standing there.

@math items="splice:  1@The splice;;arrive at position i:  i + 1@getting there;;insert at i:  i + 2@So inserting"
The splice really is a fixed number of pointer writes. But getting there costs i plus one hops. So inserting at position i costs i plus two.

@words text="The front is free only because you hold it"
Inserting at the front costs one only because the front is the one place you already hold a pointer to.

@end text="Full lesson on Learn"
The full lesson, with both counters running, is on Learn.
