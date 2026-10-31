"""Spoken forms for runs whose notation is ambiguous to read-out.

Keyed by the exact run text; see content/AGENTS.md, "Write math a voice can read".
Each course adds only a block headed with its own title.
"""

SPOKEN = {}

# Distribution and Putting It Together
# Key and worked lines, read by the code reader: it says "minus" for the
# hyphen in "coarse-grained", splits grouped thousands at the comma, and reads
# µs as "micro s". Each line is read as written.
SPOKEN.update({
    "remote interfaces are coarse-grained":
        "remote interfaces are coarse grained",
    "a remote interface must be coarse-grained":
        "a remote interface must be coarse grained",
    "a local interface is best fine-grained":
        "a local interface is best fine grained",
    "time: 75 calls at 1,000 µs, 75,000 µs":
        "time, 75 calls at 1000 microseconds, 75000 microseconds",
    "one node: 75 calls at 1 µs, 75 µs":
        "one node, 75 calls at 1 microsecond, 75 microseconds",
    "ratio: 75,000 over 75, which is 1,000":
        "ratio, 75000 over 75, which is 1000",
    "fine-grained: 11 trips at 20.5 ms":
        "fine grained, 11 trips at 20.5 milliseconds",
    "fine-grained time: 225.5 ms":
        "fine grained time, 225.5 milliseconds",
    "speed-up: 225.5 over 45.5, about 5 times":
        "speed up, 225.5 over 45.5, about 5 times",
    "getters: 2,066 bytes at 1,000 a ms":
        "getters, 2066 bytes at 1000 a millisecond",
    "one object: 6,066 bytes at 1,000 a ms":
        "one object, 6066 bytes at 1000 a millisecond",
    "remote: 7 calls at 2,000 µs, 14,000 µs":
        "remote, 7 calls at 2000 microseconds, 14000 microseconds",
    "local: 67 calls at 1 µs, 67 µs":
        "local, 67 calls at 1 microsecond, 67 microseconds",
    "time: 14,067 µs":
        "time, 14067 microseconds",
    "facade: 2 trips at 20 ms, which is 40 ms":
        "facade, 2 trips at 20 milliseconds, which is 40 milliseconds",
    "facade work: 11 calls at 0.5 ms, 5.5 ms":
        "facade work, 11 calls at 0.5 milliseconds, 5.5 milliseconds",
    "facade time: 45.5 ms":
        "facade time, 45.5 milliseconds",
    "getters: 5 trips at 20 ms, 100 ms":
        "getters, 5 trips at 20 milliseconds, 100 milliseconds",
    "getter time: about 102.07 ms":
        "getter time, about 102.07 milliseconds",
    "one object: 1 trip, 20 ms":
        "one object, 1 trip, 20 milliseconds",
    "object time: about 26.07 ms":
        "object time, about 26.07 milliseconds",
    # Prose runs: grouped thousands in a fraction, and a class=node pair, which
    # the code reader would say as "is set to".
    "51,033/500 ≈ 102.07 ms":
        "51033 over 500, about 102.07 milliseconds",
    "13,033/500 ≈ 26.07 ms":
        "13033 over 500, about 26.07 milliseconds",
    "53,099/500 ≈ 106.20 ms":
        "53099 over 500, about 106.20 milliseconds",
    "19,099/500 ≈ 38.20 ms":
        "19099 over 500, about 38.20 milliseconds",
    "class=node":
        "class equals node",
    "4,007/200 ≈ 20.04 ms":
        "4007 over 200, about 20.04 milliseconds",
    "8,907/200 ≈ 44.54 ms":
        "8907 over 200, about 44.54 milliseconds",
    "2,007/200 ≈ 10.04 ms":
        "2007 over 200, about 10.04 milliseconds",
    "20 × (15 + 1) = 320 ms":
        "20 times the sum of 15 and 1, which is 320 milliseconds",
    "3 × 15 + 20 × 1 = 65 ms":
        "3 times 15, plus 20 times 1, which is 65 milliseconds",
    "5 × 20 = 100 ms":
        "5 times 20, which is 100 milliseconds",
})

# Layers and Performance
# The Subject page's key (PATH["key"]) and this course's key lines. They are
# formulas, not Java statements, so the code reader would say "is set to" for
# `=`, "minus" for the hyphen in "fine-grained", and "ms" and "tps" as letters;
# each line is read as written.
SPOKEN.update({
    "fine-grained time = n·(latency + work)":
        "fine grained time equals n times the quantity latency plus work",
    "coarse-grained time = m·latency + n·work":
        "coarse grained time equals m times latency, plus n times work",
    "lazy load = 1 + one query per parent used":
        "lazy load equals 1, plus one query per parent used",
    "stateless objects = users·service/think":
        "stateless objects equal users times service time, divided by think time",
    "change a user: rise in ms / rise in users":
        "change a user, the rise in milliseconds divided by the rise in users",
    "gain: rise in tps / servers added":
        "gain, the rise in transactions a second divided by the servers added",
    "at n: last tps + gain * (n - last n)":
        "at n servers, the last throughput plus the gain times the quantity n minus the last n",
    # Worked lines: the quantity, not "open bracket".
    "swordfish at n: 20 + 15 * (n - 1)":
        "swordfish at n servers, 20 plus 15 times the quantity n minus 1",
    "camel at n: 40 + 10 * (n - 1)":
        "camel at n servers, 40 plus 10 times the quantity n minus 1",
    "equal when 5 * (n - 1) is 20: n is 5":
        "equal when 5 times the quantity n minus 1 is 20, so n is 5",
    # Record formats and dependency records: read as who uses whom, so a
    # listener can tell which name depends on which.
    "system, users, ms":
        "system, users, then response time in milliseconds",
    "system, servers, tps":
        "system, servers, then transactions a second",
    "dependent, dependency":
        "dependent, then what it depends on",
    "report, invoice; invoice, pdfwriter; pdfwriter, fontlib":
        "report uses invoice, invoice uses pdf writer, pdf writer uses font lib",
    "invoice, pdfwriter":
        "invoice uses pdf writer",
    "pdfwriter, invoice":
        "pdf writer uses invoice",
    "main, pdfwriter":
        "main uses pdf writer",
    "pdfwriter":
        "pdf writer",
    "fontlib":
        "font lib",
    "jdbc":
        "J D B C",
    # The exercises' measurement records, read as measurements so that no
    # field pair sounds like a grouped thousand.
    "north, 5, 400; north, 25, 1400; south, 5, 900; south, 25, 1000":
        "north at 5 users, 400 milliseconds, north at 25 users, 1400 milliseconds, "
        "south at 5 users, 900 milliseconds, south at 25 users, 1000 milliseconds",
    "heron, 1, 30; heron, 3, 54; stork, 1, 45; stork, 3, 57":
        "heron on 1 server, 30, heron on 3 servers, 54, "
        "stork on 1 server, 45, stork on 3 servers, 57",
})

# Talking to the Database
# Table names with a hyphen (the code reader says "minus"), the exercises'
# dependency and statement records, SELECT *, and the key and worked lines,
# whose `·` products and "ms" the code reader would read as symbols and
# letters. Each is read as written.
SPOKEN.update({
    "price-table": "price table",
    "member-table": "member table",
    "signup, member-table; profile, member-table; mailer, member-table; profile, mailer":
        "signup uses member table, profile uses member table, mailer uses member table, "
        "profile uses mailer",
    "web, invoice; invoice, customer; invoicemapper, invoice; invoicemapper, jdbc; "
    "customermapper, customer; customermapper, jdbc; main, invoicemapper; main, customermapper":
        "web uses invoice, invoice uses customer, invoice mapper uses invoice, invoice "
        "mapper uses J D B C, customer mapper uses customer, customer mapper uses J D B C, "
        "main uses invoice mapper, main uses customer mapper",
    "insert-invoice, 1; insert-items, 40":
        "insert invoice, 1 statement, insert items, 40 statements",
    "SELECT *": "select star",
    "keyed: wanted·(latency + row time)":
        "keyed, wanted times the quantity latency plus row time",
    "broad: latency + broad·(row time)":
        "broad, latency plus broad times row time",
    "batched: batches·latency + wanted·(row time)":
        "batched, batches times latency, plus wanted times row time",
    "one at a time: n·(latency + work)":
        "one at a time, n times the quantity latency plus work",
    "batched: m·latency + n·work":
        "batched, m times latency, plus n times work",
    "keyed: 50 statements of 5 + 0.1 ms":
        "keyed, 50 statements of 5 plus 0.1 milliseconds",
    "keyed: 50 × 5.1, which is 255 ms":
        "keyed, 50 times 5.1, which is 255 milliseconds",
    "broad: 5 + 200 × 0.1, which is 25 ms":
        "broad, 5 plus 200 times 0.1, which is 25 milliseconds",
    "batched: 5 × 5 + 50 × 0.1, which is 30 ms":
        "batched, 5 times 5, plus 50 times 0.1, which is 30 milliseconds",
    "one at a time: 25 × (2 + 0.5), 62.5 ms":
        "one at a time, 25 times the quantity 2 plus 0.5, 62.5 milliseconds",
    "batched: 3 × 2 + 25 × 0.5, 18.5 ms":
        "batched, 3 times 2, plus 25 times 0.5, 18.5 milliseconds",
    "waiting, one at a time: 25 × 2, 50 ms":
        "waiting, one at a time, 25 times 2, 50 milliseconds",
})

# Objects and Tables
# Tree and hierarchy records whose "-" marks the root (the code reader says
# "minus"), and lesson 4.2's shared-objects tile, whose "×" it reads as
# "times".
# Each is read as written.
SPOKEN.update({
    "root, -; a, root; b, a; c, b; d, c; e, root":
        "root, no parent, a under root, b under a, c under b, d under c, e under root",
    "account, -, 3, no; saving, account, 2, no; isa, saving, 1, yes; bond, saving, 2, yes; "
    "current, account, 2, yes":
        "account, no parent, 3 fields, not concrete, saving under account, 2, not concrete, "
        "isa under saving, 1, concrete, bond under saving, 2, concrete, "
        "current under account, 2, concrete",
    "vehicle, -, 4, no; car, vehicle, 2, yes; van, vehicle, 3, yes; truck, vehicle, 5, yes":
        "vehicle, no parent, 4 fields, not concrete, car under vehicle, 2, concrete, "
        "van under vehicle, 3, concrete, truck under vehicle, 5, concrete",
    "customer 7 ×3, product 5 ×2":
        "customer 7, three times, product 5, twice",
})

# Concurrency and Session State
# The exercises' event records end a commit with "-", which the code reader
# says as "minus"; a group pair's "=" would be "is set to"; the worked lines'
# grouped thousands would be split at each comma; and inside OPTIMISTIC_SAVE's
# SQL string the "=" and "+ 1" would go unspoken. Each is read as written.
SPOKEN.update({
    '        "UPDATE invoice SET total = ?, version = version + 1"':
        "string, update invoice set total equals placeholder, version equals version plus 1",
    '        + " WHERE id = ? AND version = ?");':
        "plus the string, where id equals placeholder and version equals placeholder",
    "9, bo, commit, -;": "9, bo, commit, no record",
    "12, ann, commit, -": "12, ann, commit, no record",
    "5, ana, commit, -;": "5, ana, commit, no record",
    "30, ben, commit, -;": "30, ben, commit, no record",
    "40, cy, commit, -": "40, cy, commit, no record",
    "3, ann, commit, -;": "3, ann, commit, no record",
    "7, bo, commit, -;": "7, bo, commit, no record",
    "8, cy, commit, -": "8, cy, commit, no record",
    "record=group": "record equals group",
    "line1=order9": "line 1 equals order 9",
    "line2=order9": "line 2 equals order 9",
    "room1=floor1; room2=floor1; room3=floor2":
        "room 1 equals floor 1, room 2 equals floor 1, room 3 equals floor 2",
    "busy share: 1,000 / 10,000 is 1/10":
        "busy share, 1000 divided by 10000, which is one tenth",
    "idle share: 1 − 1/10 is 9/10":
        "idle share, 1 minus one tenth, which is nine tenths",
    "stateless: 100 × 1/10 is 10 objects":
        "stateless, 100 times one tenth, which is 10 objects",
    "users an object serves: 10,000 / 1,000":
        "users an object serves, 10000 divided by 1000",
    "client, a request: 2 × 1,000,000":
        "client, a request, 2 times 1000000",
    "so 2,000,000 bytes on the wire":
        "so 2000000 bytes on the wire",
    "client, a session: 2,000,000 × 20":
        "client, a session, 2000000 times 20",
    "so 40,000,000 bytes on the wire":
        "so 40000000 bytes on the wire",
    "server memory: 100 × 1,000,000":
        "server memory, 100 times 1000000",
    "database, a request: 2,000,000 bytes":
        "database, a request, 2000000 bytes",
})
