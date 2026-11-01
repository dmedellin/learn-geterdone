"""Spoken forms for runs whose notation is ambiguous to read-out.

Keyed by the exact run text; see content/AGENTS.md, "Write math a voice can read".
Each course adds only a block headed with its own title, as
SPOKEN.update({...}) under a "# <Course title>" comment.
"""

SPOKEN = {}

# Behavioral Patterns I: Requests, Languages and Traversal
SPOKEN.update({
    "n·(n − 1)/2 links against n": "n times n minus 1, over 2, links against n",
})

# Behavioral Patterns II: Notification, State and Algorithms, and the Conclusion
# Worked-example lines are sums, not Java assignments, so the code reader's "is
# set to" for `=` is replaced by "which is"; record names such as staff-cap are
# read as words, not subtractions; a decision breakdown is read as counts.
SPOKEN.update({
    "reprice: 2 + 3 = 5": "reprice, 2 plus 3, which is 5",
    "matinee: 2 + 2 + 3 = 7": "matinee, 2 plus 2 plus 3, which is 7",
    "exchange: 3 + 3 = 6": "exchange, 3 plus 3, which is 6",
    "direct: 3 + 5 + 7 + 6 = 21": "direct, 3 plus 5 plus 7 plus 6, which is 21",
    "managed: 3 + 3 + 4 + 3 = 13": "managed, 3 plus 3 plus 4 plus 3, which is 13",
    "saved: 21 − 13 = 8": "saved, 21 minus 13, which is 8",
    "branches: 9 + 5 = 14; classes: 5 + 2 = 7":
        "branches, 9 plus 5, which is 14, and classes, 5 plus 2, which is 7",
    "line 17: if on the method, and &&: +2":
        "line 17, an if on the method and an and, plus 2",
    "1 + if 3 + case 3 + && 1 = 8":
        "1, plus 3 ifs, plus 3 cases, plus 1 and, which is 8",
    "after: 1 + if 2 = 3": "after, 1 plus 2 ifs, which is 3",
    "steps: 3 fixed + 2 primitive + 2 hooks = 7":
        "steps, 3 fixed plus 2 primitive plus 2 hooks, which is 7",
    "whole: 7 × 3 subclasses = 21": "whole, 7 times 3 subclasses, which is 21",
    "base: 3 fixed + 2 hook defaults = 5":
        "base, 3 fixed plus 2 hook defaults, which is 5",
    "overrides: 3 + 2 + 2 = 7": "overrides, 3 plus 2 plus 2, which is 7",
    "with the template: 5 + 7 = 12": "with the template, 5 plus 7, which is 12",
    "accepts: 8 × 2 visitors = 16; visits: 16":
        "accepts, 8 times 2 visitors, which is 16, and visits, 16",
    "element classes: 1 + 3 = 4": "element classes, 1 plus 3, which is 4",
    "visitor classes: 1 + 2 = 3": "visitor classes, 1 plus 2, which is 3",
    "with Visitor: 3 × 2 + 3 = 9 methods":
        "with visitor, 3 times 2 plus 3, which is 9 methods",
    "on the elements: 3 × 2 = 6 methods":
        "on the elements, 3 times 2, which is 6 methods",
    "five devices: n = 5": "five devices, n is 5",
    "pairwise: 5 · 4 / 2 = 10 to build":
        "pairwise, 5 times 4 over 2, which is 10 to build",
    "one device changes: 5 − 1 = 4": "one device changes, 5 minus 1, which is 4",
    "eight devices: 8 · 7 / 2 = 28, 7 to change":
        "eight devices, 8 times 7 over 2, which is 28, and 7 to change",
    "black-box reuse replaces white-box": "black box reuse replaces white box",
    "senior-discount: orders, till, printing, reports: 4":
        "senior discount, orders, till, printing, reports, 4",
    "staff-cap: orders, printing: 2": "staff cap, orders, printing, 2",
    "loyalty-stamps: loyalty, orders: 2": "loyalty stamps, loyalty, orders, 2",
    "receipt-logo: printing: 1": "receipt logo, printing, 1",
    "total: 4 + 2 + 2 + 1 = 9; confined: 1":
        "total, 4 plus 2 plus 2 plus 1, which is 9, and confined, 1",
    "after: 2 + 1 + 2 + 1 = 6; confined: 2":
        "after, 2 plus 1 plus 2 plus 1, which is 6, and confined, 2",
})

# Structural Patterns
# Worked-example lines are sums, not Java assignments, so the code reader's "is
# set to" for `=` is replaced by "which is"; bracketed groups are read as sums.
SPOKEN.update({
    "desk, target and vendor classes: 1 + 1 + 3 = 5":
        "desk, target and vendor classes, 1 plus 1 plus 3, which is 5",
    "class adapter design: 5 + 3 = 8 classes":
        "class adapter design, 5 plus 3, which is 8 classes",
    "object adapter design: 5 + 1 = 6 classes":
        "object adapter design, 5 plus 1, which is 6 classes",
    "uses: 1 + 3 × 2 + 2 = 9 against 1 + 2 + 2 = 5":
        "uses, 1 plus 3 times 2 plus 2, which is 9, against 1 plus 2 plus 2, which is 5",
    "guides × players: 3 × 3 = 9":
        "guides by players, 3 times 3, which is 9",
    "a subclass per guide and player: 9 + 1 = 10":
        "a subclass per guide and player, 9 plus 1, which is 10",
    "guide and player hierarchies: (3 + 1) + (3 + 1) = 8":
        "guide and player hierarchies, 3 plus 1, plus 3 plus 1, which is 8",
    "garden nodes: 4 zones + 6 emitters = 10":
        "garden nodes, 4 zones plus 6 emitters, which is 10",
    "garden calls: 1 from the client + 9 forwarded = 10":
        "garden calls, 1 from the client plus 9 forwarded, which is 10",
    "front: 2.5 + 4 = 6.5":
        "front, 2.5 plus 4, which is 6.5",
    "beds: 1.5 + 3.25 = 4.75":
        "beds, 1.5 plus 3.25, which is 4.75",
    "back: 12.5 + 4.75 = 17.25":
        "back, 12.5 plus 4.75, which is 17.25",
    "garden: 6.5 + 17.25 + 6 = 29.75":
        "garden, 6.5 plus 17.25 plus 6, which is 29.75",
    "fee: 32 + 2.50 = 34.50":
        "fee, 32 plus 2.50, which is 34.50",
    "member: 34.50 × 0.9 = 31.05":
        "member, 34.50 times 0.9, which is 31.05",
    "insurance: 31.05 + 1.75 = 32.80":
        "insurance, 31.05 plus 1.75, which is 32.80",
    "reversed: (32 + 1.75) × 0.9 + 2.50 = 32.875":
        "reversed, 32 plus 1.75, times 0.9, plus 2.50, which is 32.875",
    "direct: courier 4 + kiosk 3 + desk 3 = 10":
        "direct, courier 4 plus kiosk 3 plus desk 3, which is 10",
    "uses in the direct design: 10 + 2 = 12":
        "uses in the direct design, 10 plus 2, which is 12",
    "uses in the facade design: 4 + 4 + 2 = 10":
        "uses in the facade design, 4 plus 4 plus 2, which is 10",
    "plants: 120 + 300 + 450 + 80 = 950":
        "plants, 120 plus 300 plus 450 plus 80, which is 950",
    "without sharing: 950 × (2048 + 8) = 1953200":
        "without sharing, 950 times the sum of 2048 and 8, which is 1953200",
    "sprites: 4 × 2048 = 8192":
        "sprites, 4 times 2048, which is 8192",
    "positions: 950 × 8 = 7600":
        "positions, 950 times 8, which is 7600",
    "references: 950 × 4 = 3800":
        "references, 950 times 4, which is 3800",
    "with sharing: 8192 + 7600 + 3800 = 19592":
        "with sharing, 8192 plus 7600 plus 3800, which is 19592",
    "scans loaded, in all: 120 + 300 + 150 + 400 + 80 = 1050":
        "scans loaded, in all, 120 plus 300 plus 150 plus 400 plus 80, which is 1050",
    "views × renderers × frames: 3 × 2 × 3 = 18":
        "views by renderers by frames, 3 times 2 times 3, which is 18",
    "a subclass per view, renderer and frame: 18 + 1 = 19":
        "a subclass per view, renderer and frame, 18 plus 1, which is 19",
    "view, renderer and frame hierarchies: (3 + 1) + (2 + 1) + (3 + 1) = 11":
        "view, renderer and frame hierarchies, 3 plus 1, plus 2 plus 1, plus 3 plus 1, which is 11",
    "a fourth frame, subclassing: 3 × 2 = 6":
        "a fourth frame, subclassing, 3 times 2, which is 6",
    "saved: N(I + X) − (F·I + N·X + N·R)":
        "saved, N times the sum of I and X, minus the sum of F times I, N times X and N times R",
})
