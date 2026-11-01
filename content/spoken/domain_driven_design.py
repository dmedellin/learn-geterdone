"""Spoken forms for runs whose notation is ambiguous to read-out.

Keyed by the exact run text; see content/AGENTS.md, "Write math a voice can read".
Each course adds only a block headed with its own title, as
SPOKEN.update({...}) under a "# <Course title>" comment.
"""

SPOKEN = {}

# Analysis Patterns, Design Patterns and Refactoring
# Worked-example lines are sums, not Java assignments, so the code reader's "is
# set to" for `=` is replaced by "which is"; record names such as ticket-income
# and window-48h are read as words, not subtractions; a decision breakdown is
# read as counts of each kind.
SPOKEN.update({
    "t1: 120.00 − 120.00 = 0": "t 1, 120.00 minus 120.00, which is 0",
    "t2: 50.00 − 50.00 = 0": "t 2, 50.00 minus 50.00, which is 0",
    "t3: 30.00 − 3.00 = +27.00": "t 3, 30.00 minus 3.00, which is plus 27.00",
    "total: +27.00 − 24.00 = +3.00": "total, plus 27.00 minus 24.00, which is plus 3.00",
    "restore on e1: 0.05 × 412.50 = 20.625":
        "restore on e 1, 0.05 times 412.50, which is 20.625",
    "restore on e2: 0.05 × 96.30 = 4.815":
        "restore on e 2, 0.05 times 96.30, which is 4.815",
    "agency on e3: 0.12 × 180.00 = 21.60":
        "agency on e 3, 0.12 times 180.00, which is 21.60",
    "ticket-income: 508.80 − 25.45 = 483.35":
        "ticket income, 508.80 minus 25.45, which is 483.35",
    "rounding left: −0.005 − 0.005 = −0.01":
        "rounding left, minus 0.005 minus 0.005, which is minus 0.01",
    "line 3: if, and &&: +2": "line 3, an if and an and, plus 2",
    "line 16: if, and ||: +2": "line 16, an if and an or, plus 2",
    "window-48h: ui, scheduling, billing: 3":
        "window 48 h, u i, scheduling, billing, 3",
    "urgent-exempt: ui, billing, patients: 3":
        "urgent exempt, u i, billing, patients, 3",
    "fee-amount: billing: 1": "fee amount, billing, 1",
    "reminder-text: scheduling: 1": "reminder text, scheduling, 1",
    "total: 3 + 3 + 1 + 1 = 8": "total, 3 plus 3 plus 1 plus 1, which is 8",
    "after: 1 + 2 + 1 + 1 = 5, confined 3":
        "after, 1 plus 2 plus 1 plus 1, which is 5, with 3 confined",
})

# Putting the Domain Model to Work
# Keyed only on whole records from this course's models: the exercise
# candidate's cells are read as attribute and value, and a lone - in a
# glossary record means the audience has no name, read "none".
SPOKEN.update({
    "request_d, minutes=30, load=196, urgent=no, notice=2":
        "request d, minutes 30, load 196, urgent no, notice 2",
    "day_pass, -, day_pass, day_pass;": "day pass, none, day pass, day pass",
    "morning_peak, morning_peak, morning_peak, -;":
        "morning peak, morning peak, morning peak, none",
})

# The Building Blocks of a Model-Driven Design
# Keyed only on runs from this course's lessons: its exercise records, read as
# names, ends and attributes rather than subtractions and assignments.
SPOKEN.update({
    "City, Dock, 1-n, both, no; Dock, Bike, 1-n, both, no; Member, Ride, 1-n, both, no; Ride, Bike, n-1, both, no; Member, Bike, n-n, both, no":
        "city and dock, one to many, both ways, not qualified, dock and bike, one to many, "
        "both ways, not qualified, member and ride, one to many, both ways, not qualified, "
        "ride and bike, many to one, both ways, not qualified, member and bike, many to many, "
        "both ways, not qualified",
    "class-7c": "class 7 C",
    "m1, L-301, name=kim-lee, joined=2019, branch=north":
        "m 1, L 301, name kim lee, joined 2019, branch north",
    "m2, L-301, name=kim-lee, joined=2019, branch=south":
        "m 2, L 301, name kim lee, joined 2019, branch south",
    "m3, L-455, name=kim-lee, joined=2019, branch=north":
        "m 3, L 455, name kim lee, joined 2019, branch north",
    "m4, L-455, name=kim-lee, joined=2019, branch=north":
        "m 4, L 455, name kim lee, joined 2019, branch north",
})
