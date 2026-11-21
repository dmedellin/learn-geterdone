---
format: short
lesson: enterprise-patterns-domain-logic/service-layer
title: When your app needs a Service Layer
---

@art three-clients
A second kind of client is the moment to add a Service Layer.

@code block=1 lines=1-18 label=Java focus="4-8@begins a transaction|13-17@second copy"
A web page and a nightly import both place orders. Each begins a transaction, reserves the stock, confirms, commits, and sends the mail. That's five lines, and a second copy.

@art one-operation
Move them into one service operation, and each client just builds its order and calls it.

@end text="Full lesson on Learn"
The full lesson, with a lab that finds the copies, is on Learn.
