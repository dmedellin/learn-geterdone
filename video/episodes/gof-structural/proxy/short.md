---
format: short
lesson: gof-structural/proxy
title: Does a lazy proxy always save work?
---

@art eager-shelf
Load six scans up front, and you pay thirteen hundred before anyone reads one.

@art lazy-load
Put a virtual proxy in front of each. It loads its scan on the first request, then forwards. Seven requests cost ten fifty.

@words text="Saved: only what's never read"
The saving is the one scan nobody asked for. Read all six, and the proxy saves nothing, and adds a check to every call.

@end text="Full lesson on Learn"
That's Proxy. The full lesson, with all four kinds, is on Learn.
