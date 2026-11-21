---
format: short
lesson: enterprise-patterns-concurrency-and-session-state/session-state
title: Client session state is not free
---

@art client-round-trip
Your server stores nothing. So why is the network groaning?

@math items="a megabyte of state, out and back: 2,000,000 bytes a request@two million;;20 requests: 40,000,000 bytes@forty million"
Client session state crosses the wire with every request, out and back. For a megabyte session, that's two million bytes a request, and forty million over twenty requests.

@art id-on-wire
Keep the cart on the server or in the database, and the wire carries just a thirty two byte id.

@end text="Full lesson on Learn"
The full lesson, with a lab that counts the bytes, is on Learn.
