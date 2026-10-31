# Review (accuracy and teaching): Enterprise Application Patterns, Course 6 — Concurrency and Session State

Course: `enterprise-patterns-concurrency-and-session-state`
(`content/enterprise_patterns/c6_concurrency_and_session_state/__init__.py`,
`part_a.py`, `part_b.py`, and its block in `content/spoken/enterprise_patterns.py`),
seven lessons. Built to `docs/enterprise-patterns/PLAN.md` §C Course 6, §D (lock and
session modes), §E, §F, §R (with §R.1's revised pessimistic lock) and
`docs/enterprise-patterns/AUTHORING.md`. Every lab is eakit
(`docs/enterprise-patterns/kit-report.md`). Reviewed 2026-10-31 against the private
extraction of the operator's copy. I read the page behind every "Fowler / Rice / the
authors say" sentence with `eapage.py`: Chapter 5 pp. 72–86, Chapter 6 pp. 87–91,
Chapter 16 pp. 374–403 and Chapter 17 pp. 405–411. I did not read the file whole.

**Scope.** I wrote only this file. Nothing in the course, `presets.py`, the PLAN or the
kit was changed. Every finding is a recommendation, with replacement text where the fix
is mechanical. No run of book text is reproduced here except the short phrases that
findings S9 and S5 have to identify.

**Counts: 1 MUST-FIX, 10 SHOULD-FIX, 14 NOTE.**

## Gates

- **Preview:** `python3 scripts/preview_subject.py enterprise_patterns --course
  enterprise-patterns-concurrency-and-session-state --out …/scratchpad/c6rev/preview` →
  8 pages; labcheck 7 executed, 7 with pinned figures, 0 failing; **OK**.
- **`speechcheck.py`:** enterprise-patterns 0 unresolved (66 spoken forms). But see S7:
  one snippet's read-out is wrong even though nothing is flagged as unresolved.
- **Presets, in Chromium (Playwright) at 1280 px.** Every tile matches the body prose,
  the worked lines and §C:
  - 6.1: `martin-and-david` 15 / 12 / 17 / "no: 15 is neither 12 nor 17"; `both-after`
    17 "yes: … after"; `both-before` 12 "yes: … before".
  - 6.2: `no-control` "2: david, martin", 1 lost, redo 0; `optimistic` "1: david",
    "1: martin", redo 10; `pessimistic` "1: martin", refused "1: david", redo 0, peak 1.
  - 6.3: `quarter-totals` 820, "no: 820 is neither 700 nor 870", read committed /
    unrepeatable; `only-a-new-row` 520, "yes: … after", "none needed"; `martin-and-david`
    phantom / serializable.
  - 6.4: `two-clerks` "1: lee", "1: kim", 20; `inconsistent-read` "2: lee, kim", "0:
    none", 0; `check-the-read` "1: lee", "1: kim", 6.
  - 6.5: `line-locks` "2: kim, lee", "0: none", peak 2; `order-lock` "1: kim", "1: lee",
    peak 1; `optimistic-groups` "1: kim", "1: lee", redo 4.
  - 6.6: `hundred-users` 100 / 10 / "9/10 = 90%" / 10; `busier` 100 / 50 / "1/2 = 50%" /
    2.
  - 6.7: `a-megabyte` 2,000,000 / 40,000,000 / 32 / 100,000,000 / 2,000,000;
    `a-small-cart` 4,000 / 80,000 / 32 / 200,000 / 4,000.
- **Every exercise was pasted into its lab.** Each result agrees with its quiz `why`:
  - 6.1: 900 / 1,000 / 1,000, "no: 900 is not 1,000, before or after".
  - 6.2 optimistic: "1: bo", "1: ann", redo 12. Pessimistic: "1: ann", refused "1: bo",
    redo 0, peak 1.
  - 6.3: 27 / 25 / 30, phantom, serializable.
  - 6.4: "2: ana, cy", "1: ben", redo 29.
  - 6.5: "2: ann, cy", refused "1: bo", redo 0, peak 2.
  - 6.6: 250 / 5 / "49/50 = 98%" / 50.
  - 6.7: 80,000 / 960,000 / 32 / 200,000,000 / 80,000.
  - I also ran 6.2's "delete Martin's commit" variant, which the body asks for.
    Pessimistic gives "0: none" committed and "1: david" refused. Optimistic gives "1:
    david" committed, no conflict, and the banner says martin neither commits nor
    fails. Both match the prose.
- **Timelines re-derived by hand.**
  - 6.2 pessimistic: Martin locks at his read at 0, David is refused at his read at 1,
    and redo is 1 − 1 = 0.
  - 6.4 `check-the-read`: rate v0 → v1 at 2, so Kim's commit at 6 fails on the read
    and redo is 6 − 0 = 6.
  - 6.5 exercise: floor1 held 0–3 and floor2 held 2–8, so the peak is 2 and bo is
    refused at 1.
  - Exercise 6.4: ben saw v0 at 1, v1 after 5, so his save fails at 30 and redo is 29.
    cy first sees v1 at 31 and commits.
  - All four agree with the kit and the prose.
- **375 px:** every lesson has `scrollWidth` 375. No console or page errors at either
  width. (Kit layout notes are under N11.)
- **Rendered text** (scripts and styles stripped): no stray backticks and no
  unrendered entities.
- **Snippets:** all seven constants are byte-identical to `presets.py` `S[...]`. Each is
  ≤ 20 lines of ≤ 72 characters (19 lines and 72 characters at most). Every line number
  cited in prose was checked: `COUNT_FILES` lines 3 and 4; `OPTIMISTIC_SAVE` lines 5–6
  and 10; `GROUP_LOCK` lines 3 and 6.
- **`ea_quotes.py`: 10 quotations, all OK, all on the stated page.**

  | Lesson | Page | Words |
  | --- | --- | --- |
  | 6.1 | p. 73 | 8 |
  | 6.2 | p. 76 | 24 |
  | 6.3 | p. 81 | 13, plus "database" p. 79, 1 |
  | 6.4 | p. 377 | 17 |
  | 6.5 | p. 382 | 9, plus Implicit Lock p. 400, 12 (total 21) |
  | 6.6 | p. 88 | 20 |
  | 6.7 | p. 89 | 10, plus "three Shakespeare plays worth" p. 90, 4 (total 14) |

  Every lesson is under 60 words of quotation. Unmarked near-verbatim runs, which would
  add to those totals, are listed in S9.
- **Attributions checked on the page.** All correct:
  - Chapter 5 by Fowler and Rice (p. 72), and every "the authors" or "we" in 6.1–6.3.
  - Optimistic Offline Lock, Pessimistic Offline Lock and Implicit Lock by Rice (pp.
    374, 382, 400).
  - Coarse-Grained Lock by Rice and Foemmel (p. 391), with "they" for its How It Works
    and When to Use It.
  - Evans and Siegel's aggregate (p. 392).
  - Kai Yu's twelve segments (p. 408).
  - Chapter 6 in Fowler's first person (pp. 87–91), which supports "which Fowler wrote
    alone".
  - Every chapter, section and pattern name used in prose.
- **Book claims checked at strength and correct.** These include:
  - the two essential problems and correctness against liveness (p. 73);
  - the execution contexts (p. 74), and isolation and immutability (p. 75);
  - the frequency-and-severity choice (p. 76);
  - read/write locks, version markers and temporal reads (p. 77);
  - the deadlock techniques (pp. 77–78);
  - ACID, long, request and late transactions, and lock escalation (pp. 79–80);
  - the four levels and the errors each lets through, stated without reproducing
    Table 5.1 (pp. 80–81);
  - the liveness sentence after the quotation (p. 81);
  - long transactions when concurrency needs are modest (p. 82);
  - the offline-pattern map and "not a technical detail" (p. 83);
  - process- and thread-per-request (pp. 84–85);
  - version in the `WHERE` and row count (p. 375);
  - clocks (p. 375);
  - the inconsistent read, reread only at repeatable read or stronger (p. 376);
  - merging (p. 377);
  - lock types, the lock manager and protocol (pp. 383–385);
  - twenty minutes, no waiting, timeouts (p. 385);
  - shared version and root lock (pp. 391–393);
  - Implicit Lock's exclusion of write locks (p. 401);
  - statelessness and the hundred-user experiment (p. 88);
  - session state, the three places and Fowler's preference (pp. 89–91);
  - the details of Chapter 17's three patterns (pp. 405–411).
- **Exercise answers** appear only in quiz `why`s. No body, worked, step or note text
  gives them. (6.2 splits its answer across two `why`s: N10.)
- **The kit's simplification is stated.** The panel's "How the lab counts" gives the
  full rule on every timeline page:
  - one exclusive write lock;
  - refused at once;
  - taken at the first read or edit of a group the session edits anywhere.

  6.2's body, quiz 2 stem and note, and 6.5's body ("these timelines have no reads…")
  and note restate it. S1 covers the one place a reader can still be misled.

## MUST-FIX

**M1. Optimistic and Pessimistic Control: `mistakes[1]` calls a true statement a
mistake, and the course and its lab contradict it.**

*What is wrong.* The mistake is headed "Thinking optimistic locking prevents lost
updates", and its body says "It prevents the overwrite, not the loss". In the
chapter's own terms, preventing the overwrite is preventing the lost update:

- The lost update is David's change being written over and "lost forever" (p. 73).
  Optimistic locks base their conflict detection on a version marker "to detect lost
  updates" (p. 77).
- On this lesson's `optimistic` preset the lab prints **Lost updates 0**, while
  `no-control` prints 1.
- The course itself says the opposite of the mistake. 6.4's `one_line`: "turns a lost
  update into a failed save the caller can see". 6.4's `mistakes[2]`: "Code that
  ignores the count has a version column and still loses updates." Both say that
  checking the version prevents the lost update.

*Evidence.* A careful reader can argue the "mistake" is right, using the tile next to
it. The real misconception (§C's "Also" line) is that detection costs nothing: the
second session's work is thrown away.

*Fix.* Retitle and reword so that the tile, the chapter and 6.4 agree:

> ("Thinking optimistic locking loses no work",
> "It does stop the lost update: Martin's commit is refused, David's change survives,
> and the lab counts 0 lost updates. But it stops it by throwing away the second
> session's work, not by saving it. Unless Martin can merge, everything he did is
> gone, and the section warns that business data is seldom easy to merge. On the
> lesson's timeline Martin redoes ten minutes.")

## SHOULD-FIX

**S1. Optimistic and Pessimistic Control: the body never says that David's read is
refused only because David edits later.**

*What is wrong.* The `pessimistic` paragraph says "Martin loads the design for editing
at minute 0 and takes the lock then … David is refused at minute 1". Two paragraphs
earlier the body has said that pessimistic schemes use read (shared) and write
(exclusive) locks, and that with enterprise data editing can stop others even reading.
A reader will reasonably take David's refusal as a read lock clashing with Martin's
lock. In the kit:

- it is the exclusive write lock;
- David's read takes the lock only because David edits the design at minute 5;
- a session that only read the design would not be refused.

The kit also knows each session's intent from the rest of the timeline, which a real
lock manager learns only because the session says "load for edit".

*Evidence.* §R.1 item 1 and the rendered rules ("a read of a group it never edits takes
none"). The body is silent on this, and so are the note and the steps. Step 3 says "a
record it will edit" but not why a read can be refused.

*Fix.* Add after "before he has done any work":

> "His read is refused because he goes on to edit the design: the lab's lock is the
> exclusive write lock, taken when a session loads a record it means to edit, as
> `tryLoadForEdit` asks for it. A session that only read the design would be let
> through."

**S2. Transactions and Isolation: `mistakes[1]` says "Writes are protected by locks
the database takes either way".**

*What is wrong.* The sentence goes beyond the book, which lists read errors only, and a
reader takes it to mean that no level allows a write anomaly. Read committed allows the
classic read-modify-write lost update. This course's own 6.3 aside names write skew
under snapshot isolation.

*Fix.* Replace the sentence:

> "The database's own write locks stop two transactions changing one row at the same
> instant at every level, but that is not the same as every write being safe: a
> transaction that reads a value and writes back a result can still lose another's
> update at a weak level. The levels, as the chapter states them, decide how
> consistent a transaction's reads are."

Or simply delete the sentence.

**S3. The Value of Statelessness: "Fowler's objection to stateful servers is
resources" gives Fowler a verdict he does not give.**

*What is wrong.* On p. 88 Fowler reports that for *many people* stateful servers are
disastrous, and asks why. Resources is his explanation of their objection. The next
page ends the section with "we may not want to" use a stateless server, and on p. 91 his
stated preference is Server Session State, which is a stateful server. 6.7 itself says
"Fowler prefers it". So the lesson has Fowler object to the design he prefers.

*Fix.* Change to:

> "Many people, Fowler says, regard stateful servers as nothing short of disastrous,
> and he explains why: the primary issue is resources. He makes the case with a
> thought experiment he calls completely unrealistic but helpful."

If the verbatim phrase is kept, it counts as quotation; otherwise use "a disaster".

**S4. The Value of Statelessness: `mistakes[1]` uses a non sequitur, "and moving it
costs too: on busier the saving falls to half".**

*What is wrong.* `busier` models users waiting less between requests. It has nothing to
do with the cost of moving state, which is 6.7's subject. "The saving falls to half" is
also ambiguous. The objects saved fall from 90 to 50; "half" is the stateless count
against the stateful.

*Fix.*

> "But the cart has to live somewhere, and moving it out of the server object has its
> own costs, which the next lesson counts; and the saving itself depends on idle time:
> on busier the stateless pool is 50 objects against 100, not 10."

**S5. Session State: "Expiring those rows can be contentious" misreads the book.**

*What is wrong.* On p. 408 a daemon deleting aged sessions "can lead to a lot of
contention on the session table". That is lock contention. "Contentious" means
disputed.

*Fix.* "Deleting expired rows with a daemon can cause heavy contention on the session
table; Kai Yu told Fowler of …"

**S6. Optimistic Offline Lock: the lab's table shows a version at Kim's and ben's
edits that they never saw, and the exercise asks for "the version seen".**

*What is wrong.* In `two-clerks` the row for minute 4 reads "kim | edit | invoice |
edit, version 1". In the exercise, ben's minute 6 row reads "edit, version 1". The
column gives the record's current version at the edit. Kim's and ben's sessions still
hold 0 from their reads, and the commit fails for exactly that reason. The exercise
asks the reader to "write the version seen", and the worked lines say "Kim saves with
version 0". A reader who checks against the table sees "version 1" on Kim's and ben's
own rows and can conclude they refreshed.

*Fix.* The fix is in the lesson, since the kit is fixed. Add one sentence to the lab
paragraph:

> "The table's version on each read or edit row is the record's version at that
> minute; what the session holds is the version at its first read or edit, which is
> why Kim's edit row shows 1 while she still holds the 0 she read."

Also note it in the kit gap list.

**S7. Optimistic Offline Lock: the read-out of `OPTIMISTIC_SAVE` drops the check
itself.**

*What is wrong.* The rendered `data-say` for lines 5 and 6 is "UPDATE invoice SET total
?, version version 1. … plus WHERE id ? AND version ?". Inside the SQL string the `=`
signs and the `+ 1` are not spoken. A listener hears neither the increment nor the
comparison, which are the two things the lesson says the line does. `speechcheck.py`
does not flag this, because nothing is unresolved.

*Fix.* Add two entries to the course's block in `content/spoken/enterprise_patterns.py`:

```
'"UPDATE invoice SET total = ?, version = version + 1"':
    'UPDATE invoice SET total equals placeholder, version equals version plus 1',
'+ " WHERE id = ? AND version = ?");':
    'plus WHERE id equals placeholder AND version equals placeholder',
```

Key them on the exact line text; check how the code dialect keys a line before
committing.

**S8. Pessimistic and Coarse-Grained Locks: `GROUP_LOCK` is a check-then-put on an
unsynchronised map, and the body does not say so. `TWO_CONTROLS` in 6.2 has the same
gap.**

*What is wrong.* Rice says that access to the lock table must be serialized (p. 384),
in the How It Works this lesson reads. Two threads can both find `holder == null` and
both "take" the lock. 6.7 flags the same problem for its `Carts` map ("which Chapter 5
says must be synchronised"), so the course is inconsistent.

*Fix.* Add a sentence to the snippet paragraph:

> "A real lock manager must also serialize access to that table, as Rice requires, so
> that two sessions cannot both find the key free; the snippet leaves that, like the
> release, to the code around it."

Add the same clause to 6.2's "The class leaves out …" sentence.

**S9. Several unmarked near-verbatim runs in quiz `why`s and prose (PLAN §E.3: nothing
closely paraphrased beyond the quotation limits).**

*What is wrong.* None is long, but each follows the book's sentence word for word:

- 6.4 quiz 4 `why`, and the body less closely: the sentence on system clocks being too
  unreliable when coordinating across servers. 11 of its 13 words are the book's
  (p. 375).
- 6.5 quiz 2 `why`, and option b: coding a wait involves timeouts and gets complicated,
  and throwing as soon as a lock is unavailable removes the burden of coping with
  deadlock (p. 385). There are two verbatim runs of 6–7 words.
- 6.3 quiz 3 `why`: serializable "messes up" liveness so that you "often have to reduce
  it to increase throughput" (p. 81).
- 6.3 quiz 4 `why`: the policy to avoid the need for explicit synchronisation and locks
  as much as possible (p. 84).
- 6.3 body: "works correctly 99 percent of the time and throws random fits" (p. 84).
- 6.3 `mistakes[2]`: modest concurrency needs … if you can get away with it … avoids a
  lot of awkward problems (p. 82).
- 6.7 quiz 2 `why`: particularly if the memento is stored remotely so it survives a
  server crash (p. 91).

*Fix.* Reword each in the lesson's own words. For example, for 6.4: "clocks on
different machines cannot be trusted to agree". Where the wording matters, mark it as a
quotation and count it. Every lesson has room under 60 words: 6.3 is at 14 and 6.4 at
17.

**S10. Quiz answers can be found without the material.**

*What is wrong.* There are two cues:

- Across all 26 items the correct option is never the fourth (`c` is 0, 1 or 2
  throughout).
- In 17 of 26 items the correct option is the longest, or ties for longest. In The
  Value of Statelessness it is the longest in all four items. In 6.5 items 1, 2 and 4
  and 6.3 item 3 the correct option is the only one with a qualifying clause.

*Fix.*

- Move the correct answer to position 3 in at least one item a lesson. 6.6 quiz 2 and
  6.7 quiz 3 can be reordered with no other change.
- Trim the qualifying clause from the correct option of 6.6 quiz 2 ("Yes: it keeps
  nothing between requests") and quiz 3 ("No: the state can be kept outside the
  server").
- Give one distractor in 6.5 quiz 2 a clause of equal length.

## NOTE

**N1. Optimistic and Pessimistic Control, concept "Deadlock".** "Chapter 5 prefers
schemes that keep it from happening to schemes that detect it afterwards." The book
prefers "very simple and conservative schemes" (p. 78), and its conservative example
adds a timeout, which deals with a deadlock when it occurs (p. 77). The body has it
right. Make the concept match: "and Chapter 5 prefers very simple, conservative schemes,
even at the cost of unnecessary victims."

**N2. Transactions and Isolation.** "so the authors see a lot to be said for processes".
The book names process-per-request (p. 84), giving equal scalability and better
robustness. Say "for process-per-request".

**N3. Pessimistic and Coarse-Grained Locks.** Two small hardenings of the book:

- "in the database once the servers are clustered": the book says an in-memory table
  won't work unless it is pinned to one server, and that the database is "probably more
  appropriate" (pp. 383–384).
- "consider a long transaction before it": the book says *also* consider one, as
  possibly no more damaging and easier to program, and load test before choosing
  (p. 385).

Also, "since locking every record turns a multi-user system into something close to a
single-user one" ties two separate points of p. 383 together with a "since" the book
does not use.

**N4. Optimistic Offline Lock, body and note.** Two sessions adding to one collection
"may break a rule that no version check sees" and "which Rice notes no version check
prevents". Rice says the *typical* Optimistic Offline Lock scheme won't prevent it
(p. 377). Use "the usual version check".

**N5. The Value of Statelessness.** "The banner adds the experiment's other unrealistic
part" and quiz 4's `why` "which Fowler calls the experiment's unrealistic part". Fowler
calls the whole experiment completely unrealistic (p. 88) and does not single out the
balanced requests. Say "the experiment also assumes perfectly balanced requests, and
real ones bunch".

**N6. Session State.** Two points:

- The snippet paragraph says "the two assumptions Chapter 17 names". The body lists
  three: enough memory, one server, and that a lost session is acceptable (p. 407).
  Say "two of the three assumptions".
- "must follow each user or be shared" leaves out the third choice, server affinity,
  which the body itself describes. With affinity the user follows the server. Say "must
  be reachable from whichever server takes the request, or each user must be pinned to
  one server".

**N7. Session State, the lab's table.** The "server" row shows 1,000,000 "held in server
memory" (one session, one request), while the `snMemory` tile shows 100,000,000 (every
user). The prose explains only the tile. Add: "The table is one user's request; the
tile multiplies the memory by the users."

**N8. Course `not_covered`.** It says the platform advice of Chapter 17 (HTTP sessions,
stateful session beans, .NET session state) "is named". No lesson names it; 6.7 says
only "a platform's own session support". Either name it once in 6.7's snippet paragraph
(PLAN §F rule 5: one sentence) or say "is left to the book".

**N9. Snippets, beyond what the prose claims.**

- `COUNT_SERIALIZABLE`: the routine "returns 12 or 17, never 15". A real serializable
  transaction may instead be aborted with a serialization failure and throw. There is
  no rollback on that path.
- `OPTIMISTIC_SAVE` never closes its `PreparedStatement`, and it leaves the caller's
  `Invoice` at the old version after a successful save.

None of this contradicts the prose. One clause each ("or throws if the database aborts
it"; "and the caller moves its own copy of the version on") would keep a careful reader
from tripping.

**N10. Optimistic and Pessimistic Control, exercise.** The answer is split across quiz
1's `why` (optimistic) and quiz 2's (pessimistic). AUTHORING and PLAN §E.4 item 4 say
"the `why` of one quiz item". The split is natural, because the exercise asks two
questions. Either accept it and record it in §C 6.2, or ask only the optimistic replay
in the exercise and leave the pessimistic one as quiz 2.

**N11. Kit display, for the kit list and not for this course.** On lock/timeline:

- The pessimistic banner says "skipped: events 3, 5". These are 1-based event
  positions, and on 6.2 they read like minutes: minute 5 is one of David's skipped
  events, and minute 3 does not exist.
- At 375 px the "what happens" column, the one that carries the result, is off-screen
  until the reader scrolls the table sideways.
- The caption "Each event, and what the scheme does with it" is clipped at the right
  edge.

**N12. Example domains near the book's.** None of these is book code, and all are
PLAN-approved instances. They are listed so the owner can decide:

- 6.4's `inconsistent-read` (an invoice computed from a rate that another session
  changes) sits close to Rice's billing example: a charge whose tax depends on an
  address (p. 376). The body also describes Rice's example in the abstract.
- 6.4's exercise record is a "policy", and 6.7's body uses "a half-edited policy". This
  is the insurance-policy example of Chapter 6 (p. 89).
- 6.7 quiz 4 uses the book's "book availability or daily revenue" (p. 410).

Renaming the 6.4 records (for example `quote` built from a `discount`) and dropping
"book availability" would put more distance between the lesson and the book.

**N13. Course `how_to`.** "Real concurrency bugs cannot be reproduced on demand, which
is the chapter's own reason for preferring designs that avoid them: isolation,
immutability, and transactions that the database manages for you." The book gives
hard-to-reproduce bugs as the reason for avoiding explicit synchronisation (p. 84) and
for seeking experienced help (p. 83). Isolation's stated reason is that it reduces the
chance of errors (p. 75). Say "which is one of the chapter's reasons for preferring
…".

**N14. Voice (PLAN §F rule 1).** 6.1, 6.6 and 6.7 say in the first paragraph whether
they read a narrative as an argument or a pattern as a tool. 6.2 and 6.3 say it only in
`read_title`. Adding "This is a narrative, read as an argument" to their first
paragraphs would make all seven consistent. Everything else in §F holds:

- one light remark a lesson, each the author's own (stay poor, Budweiser, three
  Shakespeare plays);
- the modern aside once, in 6.3, and not as `mistakes[0]`;
- the last `p` names the next lesson;
- no slang or "let's".
