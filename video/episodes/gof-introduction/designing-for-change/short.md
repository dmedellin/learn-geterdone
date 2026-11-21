---
format: short
lesson: gof-introduction/designing-for-change
title: The interface that made one change worse
---

@art irrigation-garden
Put a weather service behind an interface, and one change gets worse.

@math items="new vendor: 3 modules → 1@a new vendor;;hourly forecast: 2 modules → 3@hourly forecast"
A new vendor used to touch three modules. Now it touches one. But an hourly forecast changes the interface itself, so it reaches three modules instead of two.

@words text="Robust to a particular kind of change"
Each pattern protects against a particular kind of change. Not against change.

@end text="Full lesson on Learn"
The full lesson, with the eight causes of redesign, is on Learn.
