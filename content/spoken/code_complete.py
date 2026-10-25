"""Spoken forms for runs whose notation is ambiguous to read-out.

Keyed by the exact run text; see content/AGENTS.md, "Write math a voice can read".
"""

SPOKEN = {}

# The Subject page's key (PATH["key"]). These are formulas and a maxim, not
# Java statements, so the code reader would say "is set to" for `=`, "negative"
# for a spaced `−` and "A" for the article; each line is read as written.
SPOKEN.update({
    "points = 1 + each if, for, while, case, &&, ||":
        "decision points equal 1, plus one for each if, for, while, case, and operator and or operator",
    "span = lines between two references":
        "span equals the lines between two references",
    "live time = last line − first line + 1":
        "live time equals the last line minus the first line, plus 1",
    "paths in a team of n = n·(n − 1)/2":
        "paths in a team of n equal n times the quantity n minus 1, over 2",
    "left = N·(1 − e₁)·(1 − e₂)·…":
        "defects left equal N, times 1 minus e 1, times 1 minus e 2, and so on",
    "speedup = old time / new time":
        "speedup equals the old time divided by the new time",
    # A worked line (Unusual Control Structures): `calls` is a function, and
    # "calls of n minus 1" could be calls(n) - 1.
    "calls(n) is 1 + calls(n - 1) + calls(n - 2)":
        "calls of n is 1, plus calls of the quantity n minus 1, plus calls of the quantity n minus 2",
    "a count is a reason to look, not a verdict":
        "a count is a reason to look, not a verdict",
})

# System Considerations
SPOKEN.update({
    "paths among n people: n·(n − 1)/2":
        "paths among n people, n times the quantity n minus 1, halved",
    "defects = size in KLOC × errors per KLOC":
        "defects equal the size in K L O C times the errors per K L O C",
    "effort = nominal × each factor":
        "effort equals the nominal estimate times each factor",
    "paths = n·(n − 1)/2":
        "paths equal n times the quantity n minus 1, halved",
    "defects = KLOC × errors per KLOC":
        "defects equal K L O C times errors per K L O C",
    "staff-years = lines / lines per year":
        "staff years equal lines divided by lines per year",
    "spread = high rate / low rate":
        "spread equals the high rate divided by the low rate",
    "paths: 50 × 49 / 2 = 1,225":
        "paths, 50 times 49, divided by 2, is 1225",
    "defects: 1,000 × 4 = 4,000 up to 1,000 × 100 = 100,000":
        "defects, 1000 times 4 is 4000, up to 1000 times 100, which is 100000",
    "fast end: 1,000,000 / 10,000 = 100 staff-years":
        "fast end, 1000000 divided by 10000 is 100 staff years",
    "slow end: 1,000,000 / 700 ≈ 1,428.57 staff-years":
        "slow end, 1000000 divided by 700 is about 1428.57 staff years",
    "spread: 10,000 / 700 ≈ 14.29":
        "spread, 10000 divided by 700 is about 14.29",
    "effort = nominal × each multiplier":
        "effort equals the nominal estimate times each multiplier",
    "−24 percent is a multiplier of 0.76":
        "minus 24 percent is a multiplier of 0.76",
    "+34 percent is a multiplier of 1.34":
        "plus 34 percent is a multiplier of 1.34",
    "programmers: 1 − 0.24 = 0.76":
        "programmers, 1 minus 0.24 is 0.76",
    "analysts: 1 − 0.29 = 0.71":
        "analysts, 1 minus 0.29 is 0.71",
    "product: 0.76 × 0.71 = 0.5396":
        "product, 0.76 times 0.71 is 0.5396",
    "effort: 100 × 0.5396 = 53.96 staff-months":
        "effort, 100 times 0.5396 is 53.96 staff months",
    "app: main.o util.o":
        "app depends on main dot o and util dot o",
    "main.o: main.c util.h":
        "main dot o depends on main dot c and util dot h",
    "util.o: util.c util.h":
        "util dot o depends on util dot c and util dot h",
})
