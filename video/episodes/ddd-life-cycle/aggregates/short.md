---
format: short
lesson: ddd-life-cycle/aggregates
title: Delete a person. Does the address go too?
---

@art shared-address
Delete a person from the database. Does their address go too?

@words text="Who owns what?"
If others share it, deleting it leaves them dangling. Keeping it piles up junk. Nobody said what the person owns.

@art car-and-tires
Evans's aggregate draws the line. One root, like a car. A boundary, holding its tires. Outsiders hold only the root.

@art strict-and-lagging
Rules inside hold after every change. Rules across boundaries may lag.

@end text="Full lesson on Learn"
Count a clinic's boundaries in the full lesson on Learn.
