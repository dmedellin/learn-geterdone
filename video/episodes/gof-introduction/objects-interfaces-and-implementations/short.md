---
format: short
lesson: gof-introduction/objects-interfaces-and-implementations
title: Why adding a class should not edit the client
---

@art fourth-sender
Add a fourth sender to this app, and you have to edit the app. Why?

@code block=1 lines=3-5 focus="3-5@names all three"
Because it names all three concrete senders itself.

@code block=2 lines=2-4 focus="2-4@one interface"
Give them one interface instead, and the app only knows that type. A new sender implements it, and the app isn't touched.

@words text="Program to an interface"
That's the Gang of Four's first principle. Program to an interface, not an implementation.

@end text="Full lesson on Learn"
The full lesson, with a lab that counts the dependencies, is on Learn.
