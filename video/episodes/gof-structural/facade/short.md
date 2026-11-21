---
format: short
lesson: gof-structural/facade
title: Does a facade hide the subsystem?
---

@art tangled-clients
Three apps reach into a parcel locker's five classes. Ten uses cross the line.

@art facade-front
Put one class in front: a facade. Deposit a parcel, and it finds the locker, opens it and texts the pin.

@words text="10 crossing uses → 4"
Now the crossings drop from ten to four.

@art direct-still
Four, not three, because the support desk still reads the ledger directly. A facade doesn't forbid that. It's a simpler default, not a wall.

@end text="Full lesson on Learn"
The full lesson, with the counts, is on Learn.
