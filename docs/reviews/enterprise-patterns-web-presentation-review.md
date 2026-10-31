# Review (accuracy and teaching): Enterprise Application Patterns, Course 5 — Web Presentation

Course: `enterprise-patterns-web-presentation`
(`content/enterprise_patterns/c5_web_presentation/__init__.py`, `part_a.py`), six
lessons. Built to `docs/enterprise-patterns/PLAN.md` §C Course 5, §D.5, §E, §F, §R
and `docs/enterprise-patterns/AUTHORING.md`; every lab is cckit
(`docs/code-complete/kit-report.md`). Reviewed 2026-10-31 against the private
extraction of the operator's copy (PDF pages; Chapter 4 is pp. 65–71, Chapter 14
pp. 299–350), reading the page behind every "Fowler says / argues / calls" sentence
with `eapage.py` and `eabook.py`, never the file whole.

**Scope.** This reviewer wrote only this file. Nothing in the course, in
`presets.py` or in the PLAN was changed. Every finding is a recommendation, with
replacement text where the fix is mechanical. No book text is reproduced here
beyond the six-to-fifteen-word runs that finding 1 has to identify.

## Gates

- **Preview:** `python3 scripts/preview_subject.py enterprise_patterns --course
  enterprise-patterns-web-presentation --out …/scratchpad/c5rev/out` → 7 pages;
  labcheck 6 executed, 6 with pinned figures, 0 failing; **OK**.
- **Presets, in Chromium (Playwright), at 1280 px. Every tile matches the body prose,
  the worked lines and §C:** `model-knows-html` 1: concert / 3: concert,
  concertpage, concertreport; `separated` 1: concertpage / 1: concertpage;
  `concert-page` 5, `1 + if 3 + && 1`, 0–5, 1, line 5; `concert-page-split` 1, 1,
  0–5, 0, line 4; `pages-repeat` 1 / 6 / lines 2–4 and lines 9–11;
  `page-superclass` and `front-handler` 0 / 0 / none; `ticket-row` 5,
  `1 + if 2 + && 1 + || 1`, 0–5, 1, line 5; `ticket-helper` 3, `1 + && 1 + || 1`,
  0–5, 2, line 6; `one-step` 3: concertpage, tourpage, venuepage (both tiles);
  `two-step` 1: renderer (both); `flow-repeat` 1 / 6 / lines 2–4 and lines 9–11;
  `next-screen` 0 / 0 / none.
- **Every exercise worked in the lab, typed or pasted as the body asks.** 5.1
  `CHECKOUT_DEPS` → 2: basket, checkoutpage / 3: basket, basketapi, checkoutpage;
  without `basket, widgets` → 1: checkoutpage both; quiz 4's `a, b; b, c` → 1: b /
  2: a, b. 5.2 `BOOKING_PAGE` → 7, `1 + if 3 + && 1 + || 2` (band 6–10). 5.3
  `REPORTS_REPEAT` → 1 / 4 / lines 2–3 and lines 9–10; quiz 4's renamed-variable
  pair → 0 / 0 / none. 5.4 `PRICE_CELL` → 5, `1 + if 2 + && 1 + || 1`. 5.5
  `SCREEN_DEPS`, changed `screen` → 5 / 5: account, home, printrenderer, renderer,
  search; changed `look` → 1: renderer. 5.6 `CLAIM_FLOW` → 1 / 6 / lines 2–4 and
  lines 9–11. Every result agrees with its quiz `why`, and every cited line number
  was checked against the numbered listing.
- **375 px:** every lesson has `scrollWidth` 375 (no page scroll); long code lines
  scroll inside their own block, as on every course. No console errors at either
  width.
- **Rendered text** (scripts and styles stripped): no stray backticks, no literal
  `<code>`, no unrendered entities.
- **Snippets:** all fifteen constants are byte-identical to `presets.py` `S[...]`;
  every one is ≤ 20 lines of ≤ 72 characters; each preset's `code` is the same
  constant as its body block.
- **`ea_quotes.py`: 6 quotations, all OK, all on the stated page.** 5.1 p. 301 (16
  words), 5.2 p. 65 (26), 5.3 p. 314 (21), 5.4 p. 67 (21), 5.5 p. 333 (22), 5.6
  p. 346 (28). Each is §C's **Quote**, with its page in the dict comment. But see
  finding 1: several unmarked verbatim runs would push the true totals up.
- **`# F` comments:** F24 (p. 336), the only book figure in the course, has its
  comment and is called the book's illustration in the quiz `why` and the `note`.
- **Attributions checked on the page:** Reenskaug, Smalltalk, late 1970s (p. 300);
  Rob Mee's two-stage handler (p. 313); Intercepting Filter in Alur, Crupi and Malks,
  *Core J2EE Patterns*, Prentice Hall 2001 (pp. 313, 452); Knight and Dai, IEEE
  Software, March/April 2002 (pp. 346, 453), and Further Reading's terminology
  (p. 71); the Brown model's controller/mediator (p. 107); the `how_to` author list
  matches the title page (p. 5). No Course 5 pattern has a contributing author, so
  §F rule 6 does not apply.
- **`speechcheck.py`:** prints no row for enterprise-patterns (the Subject is not in
  `GENERATED_PATHS` yet), so it checks nothing here. I ran `say_code` over every
  backtick run, key line and worked line by hand; two faults (finding 10).
- **Shape:** bodies 15–16 blocks; 4 quiz items and 4 steps each; the last step is
  §C's **Own**; the last `p` names the next lesson; one §F.3 aside (5.4's `note`),
  stated at strength and left open; no "let's", "outdated" or "studies show".

## Counts

**2 MUST-FIX, 9 SHOULD-FIX, 8 NOTE.**

## MUST-FIX

### 1. All lessons — unmarked verbatim runs from the book (PLAN §E.3)

An n-gram scan of every prose string against Chapter 4 and Chapter 14 found the six
quotations, as expected. It also found runs of 10 to 15 consecutive words copied
exactly, with no quotation marks and no page comment. §E.3 allows quoted text only,
counted against the 40/60 limits, and AUTHORING says never to copy any stretch of
the text. The longest:

| lesson | where | words copied from the book | page |
| --- | --- | --- | --- |
| 5.6 | body p 3 ("Fowler's test fits in a line: …") and quiz 2 `why` | the Chapter 4 test, nearly whole: 15 words exact, then "if the user is in control, you do not" | 66 |
| 5.4 | body p 5 and quiz 4 `why` (twice) | "the common implementations make it too easy to put complicated logic in the page" (14) | 321 |
| 5.4 | body p 2 | "you must be very disciplined to keep programming logic out of the page" (13) | 67 |
| 5.2 | body p 3 | "two responsibilities: handling the HTTP request and deciding what to do with it" (13) | 70 |
| 5.1 | body p 5, mistakes[0] | "the direction of the dependencies: the presentation depends on the model" (12) | 301 |
| 5.5 | body p 2 | "A single-stage view mostly has one view component for each screen" (12) | 67 |
| 5.5 | body p 3 | "share a common logical screen, which may not be possible" (10) | 69 |
| 5.1 | body p 3 | "the models are completely separated from the web presentation" (10) | 66 |
| 5.3 | body p 4, quiz 3 `why` | "explicit logic, compile-time error checking on the dispatch and" (10) | 313 |

Runs of seven to nine words (for example "based on a single Boolean property of the
helper", "a lot of logic about the order of screens") are each a short identifying
phrase and can stay.

**Fix.** Rewrite each row in the lesson's own words. Alternatively, mark it as a
quotation with its page comment and count it, but only where the lesson's 60 words
allow (5.6 cannot quote the whole test: 28 + 20 = 48 is allowed, but the quiz
`why` would repeat it). Suggested rewrites:

- 5.6 body: "Fowler's test fits in a line: when the application decides which screen
  the user sees next, you want an Application Controller; when the user decides, you
  do not." Quiz 2 `why`: "When the application decides the order of screens, it
  needs one; when the user decides, it does not. …"
- 5.4 body p 5: "Its two weaknesses are that the usual tools make it all too easy to let
  complicated logic into the page, and that it is hard to test outside a web
  server." Quiz 4 `why`: "… that the usual implementations let complicated logic
  into the page too easily, and that …"
- 5.4 body p 2: "If you use server pages, the section warns, it takes real
  discipline to keep the program out of the page, often with a helper object."
- 5.2 body p 3: "Any input controller, the section goes on, does two things: it deals
  with the HTTP request, and it decides what should happen as a result."
- 5.1 body p 5 and mistakes[0]: "The key point, he says, is which way the
  dependencies run: the presentation uses the model, and the model never uses the
  presentation, …"
- 5.5 body p 2: "In a single-stage view there is, for the most part, one view
  component per screen, which …"; p 3: "Every look must fit one logical screen, and
  very different interfaces may not."
- 5.1 body p 3: "… is that the models are kept entirely apart from the web
  presentation, …"
- 5.3 body p 4 and quiz 3 `why`: "… which makes the logic explicit, lets the
  compiler check the dispatch, and leaves the URLs free in their shape."

### 2. 5.3 Front Controller — `FRONT_HANDLER` contradicts the lesson, and loops on its own login page

The snippet's handler reads the session and redirects to `/login` when there is no
user, for every request. As the body admits ("As written it would also send the
login page's own request to the login page…"), the request for `/login` has no user
either, so it is redirected to itself without end. The same lines also contradict
three statements on the same page:

- Concept *Web handler*: "It produces no response itself." A redirect is a response.
  The book says the handler produces no response (p. 313).
- Body p 4: "the handler's only job is to choose the command". The snippet's handler
  also authenticates, redirects and audits.
- mistakes[0]: the handler "does only what every request shares". The login check
  is the one thing the login request does *not* share.

Publishing a pattern's example with a known defect and an apology paragraph is
weaker than fixing it. The fix is cheap, and it keeps the snippet at 8 lines of
≤ 72 characters with the dupes count still 0. It compiles with `javac --release 8`
against stubs:

```java
// One handler for every request; a command does each page's part.
void handle(Request req, Response res) throws IOException {
    Command c = commands.get(req.path());
    User u = sessions.user(req);
    if (u == null && c.needsLogin()) { res.redirect("/login"); return; }
    audit.log(u, req.path());
    c.run(req, res);
}
```

Then:

- Replace the body `p` after `PAGES_SUPERCLASS` with: "In <code>front-handler</code> one
  handler looks the request's path up in a table of commands, sends a visitor with
  no session to the login page unless the command is public, writes the audit
  record, and runs the command; each page's part would be a command's `run`. Again
  0, 0, none. The pages under `SecurePage` never needed that exemption, because the
  login page simply does not extend it; a handler that sees every request has to be
  told which ones are open."
- Concept *Web handler*: change "It produces no response itself." to "It renders no
  page itself: once it has chosen the command, the command chooses the view."
- Body p 4, last sentence: change it to "Whichever way it is built, the commands
  choose the view; once the handler has chosen the command, it plays no further
  part in the request."
- Change `S["FRONT_HANDLER"]` in `presets.py` and §D.4 at the same time (AUTHORING
  requires the lesson's constant to be identical). The line count stays 8.

## SHOULD-FIX

### 3. 5.3 Front Controller — the body hardens Fowler's "much of"

Body p 9: "Removing duplicated lines is not a reason to prefer a Front Controller,
because a superclass removes them too". On p. 314 Fowler grants only that a
superclass Page Controller can do *much* of the factoring. The lesson's own
mistakes[1] and Read keep the hedge, so only this sentence drops it (§F.2). **Fix:**
"Removing duplicated lines is a weak reason on its own to prefer a Front Controller,
because a superclass can do much of it too; the reasons Fowler gives for one
handler are …".

### 4. 5.3 Front Controller — the `front-handler` 0 is guaranteed by the listing

`PAGES_SUPERCLASS` is the whole design: the superclass and both pages. Its 0 means
the pages really share nothing now. `FRONT_HANDLER` is one routine with the
commands left out, and the dupes view cannot find a repeat inside one routine, so
its 0 says nothing. "The count cannot choose between the second and third designs:
both reach 0. That is Fowler's point in a number" compares a design with a
fragment. **Fix (smaller):** add to body p 9: "The handler's listing is a single
routine with its commands left out, so its 0 is certain; the commands, each one
page's `forward`, differ as the pages' last lines did." **Fix (fuller):** add two
three-line commands to the preset listing (the handler plus `OrderCommand` and
`InvoiceCommand`, about 16 lines). It still prints 0, but now for the same reason
the superclass listing does.

### 5. 5.3 Front Controller — quiz 4's stem defends its own wrong answer

"Two routines each open with `User u = sessions.user(req);` and the null check on
`u`, but the second names its variable `user` throughout." Read literally, both
open with the identical line, which supports "1 block, 4 lines". **Fix:** "The first
routine opens with `User u = sessions.user(req);` and a null check on `u`; the second
opens with the same two lines but calls the variable `user`. What does the lab
report for those opening lines?"

### 6. 5.6 Application Controller — quiz 1's `why` asks for a check the listing cannot settle

The `why` says one `nextStep` asking for photos first replaces both controllers
"once you have checked, as the lesson did for the address, that asking for photos
first gives each controller's old answer." The address check worked because the
address step itself supplies the address. Nothing in `CLAIM_FLOW` shows that a
claim reaching `afterDetails` has photos: neither controller routes to the other's
step. For a claim with no photos, `nextStep` sends `afterDetails` to `/photos`,
where the old code sent it on to the assessor, medical or bank screen. The answer
changes. **Fix:** say so. "… replaces them, with one difference to decide: a claim
with no photos leaving the details step now goes to `/photos`, where the old
controller sent it on. If the details step can come before the photos, that is a
change in the flow, and possibly the fix it needed; if it cannot, the answers are
the same."

### 7. 5.6 Application Controller — concept *Mediating layer* contradicts itself

"A layer between two others that each talks to but that neither needs to know
about." If both layers talk to it, both know about it: the input controllers ask
the Application Controller by name. The point of a mediator (p. 107) is that the
outer two need not know *each other*. **Fix:** "A layer between two others that both
talk to, so that neither needs to know the other. …"

### 8. 5.4 Template and Transform View — the book's own illustration, unattributed

mistakes[1] ends: "a method that renders a customer and loops over its orders,
calling a method that renders an order, is one." That is Fowler's own imperative
illustration on p. 327, with its domain, its method names and its sentence shape,
presented as the lesson's. **Fix:** use the lesson's domain: "a method that renders a
concert and loops over its ticket sections, calling a method that renders a
section, is one." Or attribute it ("Fowler's own example is a method that …") and
paraphrase further.

### 9. Course `not_covered` — the lessons do not name the examples

`not_covered[0]` says "Chapter 14's examples, in Java servlets and JSP, XSLT and
ASP.NET, are named in the lessons and not reproduced". No lesson names one. §C has
"examples pointed to" for 5.2, 5.3 and 5.5, and the dict comments say "pointed to".
**Fix:** add one clause at the end of each lesson's pattern paragraph, by the
book's titles. 5.2: the servlet controller with a JSP view, the JSP as handler, and
the C# code-behind page handler. 5.3: the simple display. 5.4: the JSP as view with
a separate controller, the ASP.NET server page, and the simple transform. 5.5: the
two-stage XSLT, and JSP with custom tags. 5.6: the state-model controller. Each
clause reads, for example, "the pattern's examples, a servlet controller with a JSP
view and a C# code-behind page, are worth reading in the book." Or change
`not_covered[0]` to "… are left to the book."

### 10. Read-out — two lines misread, and no spoken block for this course

With PATH `speech: "code"`, key and worked lines go through `say_code`, which reads
an apostrophe as a character literal:

- 5.4 key: "a helper holds the page's logic" is read as "a helper holds the page the
  character s logic".
- 5.3 worked: "lines 2 and 9: read the session's user" is read as "… read the
  session the character s user".

`content/spoken/enterprise_patterns.py` has no `# Web Presentation` block, and
`speechcheck.py` does not cover this Subject yet, so nothing caught them. **Fix:**
reword to drop the possessive ("a helper holds the logic of the page"; "lines 2 and
9: read the user from the session"), or add a `# Web Presentation` block with both
lines' spoken forms.

### 11. 5.4 and 5.6 — the exercises are clones of the worked presets

`PRICE_CELL` prints exactly what `ticket-row` prints (5, `1 + if 2 + && 1 + || 1`).
`CLAIM_FLOW` prints exactly what `flow-repeat` prints (1 / 6 / lines 2–4 and lines
9–11), from the same shape: a three-line block, and one extra check at the top of
the second routine. In both lessons the body states those strings for the preset,
so the exercise's answer is on the page outside the quiz `why`. A reader can match
the shape without counting. **Fix (needs a §C change):** 5.4: add a third
connective, for example `item.stock() == 0 || item.isWithdrawn() ||
item.isRecalled()` on line 9, which gives 6, `1 + if 2 + && 1 + || 2`. 5.6: give
`afterPhotos` two lines before the shared block (a photo check and a size check),
so the copies are at lines 2–4 and 10–12. Update the quiz options to match.

## NOTE

12. **5.2, body p 9: "Read the five as three kinds of question."** Five is 1 plus
    four decisions, and the base 1 is no question. The text then counts the `&&` as
    both a domain predicate (`hasSeatMap`) and presentation. The worked "after"
    repeats the mismatch: one + three + "the choice". Suggest: "Leave aside the 1
    every routine starts with. Of the four decisions, the test `c == null` on line 4
    is about the request; `isSoldOut`, `isSeated` and `hasSeatMap` are questions the
    concert answers; and using their answers to pick one of four pages is
    presentation."
13. **5.1, names.** The listing's classes are `Concert` and `ConcertView`, and the lab
    calls the view `concertpage`. Body p 10 says "the design is the listing's", but
    the listing never says `concertpage`. Add "(`concertpage` is the listing's
    `ConcertView`)" once.
14. **5.2, quiz 1 `why`.** By the lesson's own step 2 ("is it well formed"), the seat
    range `n < 1 || n > 8` could be sorted as request validation. One clause settles
    it: "the limit of eight seats is a rule about bookings, not about the form".
15. **5.5, quiz 3 `why`: "Single-appearance sites are the easiest case".** On p. 333
    Fowler calls them the easiest case *to consider first*, which is about the order
    of his explanation. Suggest: "single-appearance sites are the common case and
    gain from one second stage; multiappearance sites gain most".
16. **5.5, exercise.** mistakes[1], the key line "a change of screen: every stage"
    and body p 12 state the exercise's principle, though not its count. This is
    §C's **Also**, so acceptable, but mistakes[1] could be cut to "… is the
    expensive one; the exercise counts it."
17. **5.6, body p 6: "he took from them the very terms input controller and
    application controller".** On p. 71 he says he took the terminology for
    *separating* input and application controllers. Suggest: "Chapter 4's Further
    Reading credits them with the vocabulary that separates input controllers from
    application controllers."
18. **5.4, `TICKET_ROW` is a script.** The quotation and the argument are about
    scriptlets in a server page, but the "before" listing is Java that builds HTML
    as strings, which is the script style Template View sets out to replace (p.
    318). Add to body p 8: "The lab reads Java, so the row stands in for a server
    page whose scriptlets make the same two decisions."
19. **Read-out, minor.** `if (a && b)` (5.2 quiz 2) is read "if A and b", with the
    variable `a` heard as the article. Rename it to `p && q`, or leave it.

## What is right, briefly

The cckit uses fit the argument in all six lessons; none is shoehorned. 5.1's
ripple is Fowler's direction of dependencies as a count. 5.2 and 5.4 are honest
that the decisions move rather than vanish, and say what the move buys (testing
without a web server). 5.3's superclass preset carries MF-10's correction well: the
reader sees the count fail to choose. 5.5's exercise turns the pattern's cost into
a count. 5.6's check that `nextScreen` answers like `afterAddress` is exactly the
care the move needs. The claims checked on the page are correct and at the book's
strength, apart from findings 3, 15 and 17:

- the two separations and their ranking, Smalltalk's irony, and the rich-client and
  web split (pp. 300–301);
- the one-controller-per-action refinement (pp. 70, 302) and the three jobs (p. 303);
- the four advantages and the cool treatment of duplication (p. 314);
- the bad smell, the focused tag and the single Boolean (pp. 319–320);
- the two weaknesses (p. 321), and Transform View's organisation and any-language
  point (p. 327);
- F24 and the costs (pp. 336–337);
- the two responsibilities, no UI links, the smoker case and When to Use It (pp.
  344–346).

No book listing, table, figure or example domain is used (the only album is 5.2's
quotation, which §R MF-4 allows). The voice follows §F.
