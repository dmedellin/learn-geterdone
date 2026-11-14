"""Spoken forms for runs whose notation is ambiguous to read-out.

Keyed by the exact run text; see content/AGENTS.md, "Write math a voice can read".
Each course adds only a block headed with its own title, as
SPOKEN.update({...}) under a "# <Course title>" comment.
"""

SPOKEN = {}

# The Kingdom of Darkness, and the Review and Conclusion
SPOKEN.update({
    "k → c: then the kingdom has come": "k implies c, then the kingdom has come",
    "c → s: it comes with the second coming": "c implies s, it comes with the second coming",
    "drop c → s and the argument fails": "drop c implies s and the argument fails",
    "premise c → s with s false needs c false: 2 rows": "premise c implies s with s false needs c false, 2 rows",
    "premise k → c with c false needs k false: 1 row": "premise k implies c with c false needs k false, 1 row",
})
