# Second review: Software Craftsmanship (Course 7, `code-complete-software-craftsmanship`)

Reviewer role: ACCURACY (`docs/code-complete/SECOND-REVIEW.md`). Scope: `content/code_complete/c7_craftsmanship/__init__.py` and `part_a.py` (four lessons), against the book's text (printed page = PDF page − 37), PLAN §C Course 7, §D.4 and §S.2.

**No course files were edited.** The orchestrator's brief for this pass says to write only this review file, so every fix below is a recommendation with replacement text.

## Checks run

- Preview: `python3 scripts/preview_subject.py code_complete --course code-complete-software-craftsmanship --out …/scratchpad/ACCURACY-c7`. Result: 5 pages; labcheck 4 pages executed, 4 with pinned figures, 0 failing; final line **OK**.
- `grep -n "# F[0-9]"` finds **5 figure comments**: F27 p. 737, F28 p. 792, F29 p. 820, F14 p. 458 and F15 p. 445 (the last two restated on p. 848). Every book figure in the course has one. Each was checked on its page: Miara 20–30%, six spaces second lowest, none lowest; IBM via Jones 2000, about one comment per 10 statements, with fewer and more both worse; Sackman et al. 1968 and later studies, 10 to 1; §34.7 more than about 10 decision points and more than three levels of nesting. All match §S.2 at the same strength, with one exception (see SF-5).
- `cc_quotes.py` gives **5 of 5 OK**: p. 775 (15 words), p. 817 (22), p. 835 (23), p. 853 (27), and the phrase “true laziness” on p. 830 (2 words; lesson 3 totals 25). Every opening quotation is §C's **Quote**. “true laziness” is recorded in §C 7.3's Read line.
- Snippets: every constant matches `presets.py` and §D.4. The one exception is the documented rename `notify` → `notifyUser`. `NESTED_SHIPPING` is byte-identical to Course 4's constant.
- `labcheck.js --observe` on every preset, with my own hand count and §C's figures, agree in every case:
  - `dangling-else`: 2, "5, 6". `two-statements`: 1, "4". `braced`: 0, none.
  - `comments-repeat`: 12 / 7 / 5 / 5 / 0 / 1 / "1 = 100%". `comments-intent`: 8 / 7 / 5 / 1 / 0 / 1 / "1/5 = 20%".
  - `weekly-report`: 35, "7/2 = 3.50", "340/3 ≈ 113.33". `rare-task`: 18, 72, "−29/15 ≈ −1.93". `big-tool`: 267, "267/5 = 53.40", "−1".
  - `retry-delay`: 7, "1 + if 3 + for 1 + && 1 + || 1", "6–10", depth 2 at line 9. `nested-shipping`: 9, depth 5 at line 14.
- Playwright on the served pages, with every exercise entered in its lab:
  - `clamp`: 1, "6", and the gutter marks "▸ 6 mis-indented".
  - `isLeapYear`: 5 lines, 3 code, 2 statement, 2 comment, "1 = 100%".
  - The 2 h / 5 / 0 / 5 script: 24, "24/5 = 4.80", "59/3 ≈ 19.67".
  - A `?:` routine: the banner states the kit's choice.

  Every quiz `why` I recomputed by hand is right: the 4/20 density, the −29/15 net, and 59/3 = (260·5/60) − 2.
- Java, traced by hand:
  - The `else` on line 5 of `dangling-else` binds to line 3's `if`, so an inactive user gets nothing.
  - `two-statements` archives every account.
  - In `clamp`, line 6's `return high;` is unconditional, so `javac` rejects line 7 as an unreachable statement. The snippet has no second fault.
  - `average` on an empty array gives 0.0/0, which is NaN, as the lesson says.
  - `isLeapYear` is the Gregorian rule.
  - `retryDelayMillis` cannot overflow, because of the 10000 cap.
- Read-out: `speechcheck.py` does not cover `code_complete` (author-notes item 3). I ran `speech.say_code` over every key line, worked line, backtick run and code block, and read the built pages' `data-say` spans. No negation is lost: `!order.isExpress()` is read "not order dot is express". One garble is in SF-1.

## Findings

Must-fix: none. I found no figure misstated against its page, no quotation that fails, no snippet that does something other than what its lesson says, and no tile that disagrees with the prose.

### Should-fix

**SF-1 (Themes of Craftsmanship; read-out).** A bare `&&` in plain text is not given a spoken form. The renderer auto-wraps a bare `||` as "or" but leaves `&&` raw, so a listener hears whatever the speech engine does with two ampersands. It occurs in four places:
- the body: "printed as 1 + if 3 + for 1 + && 1 + || 1", and again in the `nested-shipping` paragraph. In the built page only the tail "1 + || 1" carries `data-say="1 plus or 1"`.
- step 1: "case, && and ||".
- quiz item 1, both the stem and the `why`: "case, && and ||" and "five leaves out && and ||".

Recommendation: put the runs in backticks, as Course 4 does in its quiz `why`s:
- `1 + if 3 + for 1 + && 1 + || 1` (and the nested one) as one backtick run;
- "`&&` and `||`" in the step and the quiz item.

This is also a gap in the checker: the preview printed OK with a bare `&&` in prose, so a bare `&&` outside backticks is not flagged.

**SF-2 (Self-Documenting Code; exercise answer on the page).** PLAN §B and §E.4 item 4 say the exercise's answer may appear only in the quiz `why`. Two other places give it away:
- The summary ends "and see two routines with the same density and comments of opposite worth". The two presets have different densities (100%, 20%), so "same density" can only mean the exercise.
- `mistakes[0]` says "The exercise has the same density as comments-repeat with every comment useful".

§C's own misconception line has the same clause, so §C should change with the lesson. Replacement text:
- Summary: "…sort each comment by the chapter's kinds, and see why a density cannot tell a useful comment from a useless one."
- `mistakes[0]`: delete the sentence, or put in its place "The exercise is a routine to test this on."

**SF-3 (Self-Documenting Code; the Commento's voices).** The lesson's main warning is to watch whose voice is speaking, and it has two of the voices wrong.
- Thrasymachus does more than want a standard. He also speaks the line the book flags as a KEY POINT, that good comments do not repeat or explain the code but clarify its intent, at a higher level of abstraction (p. 782). Ismene answers "Right" and adds the headings analogy. As the lesson stands, a reader would credit the intent principle to Ismene and take the purist for a man who only wants rules.
- "With a cast named from Plato" is wrong for Ismene, who comes from Sophocles. The book says nothing about where the names come from.

Replacement: "…set at the end of a team's daily stand-up, with characters given ancient Greek names. Its voices are not all McConnell's… Thrasymachus, a green purist, wants a standard that requires comments, and states the principle the chapter flags: good comments do not repeat the code but clarify its intent. Callicles…" The quiz `why` ("Thrasymachus wants a standard that requires comments") can stay.

**SF-4 (Self-Documenting Code; how firmly the exercise's comments are classified).** The quiz `why` says "Both are intent comments". Line 1 is intent ("True if the year has 366 days"). Line 3, "divisible by 4, except centuries, except every fourth century", turns line 4's expression into a sentence, clause by clause. That is close to the book's *summary* kind. It is in problem terms, which leans it towards intent. The book itself says the line between intent and summary "isn't always clear, and it's usually not important" (p. 788), and both kinds are kept in finished code, so the quiz answer stands. The `why` should not settle more than the chapter does. Replacement: "…line 3 states the calendar's rule that line 4 implements, in the problem's words: intent, or a summary at the problem's level, a line the chapter says is seldom clear and seldom matters (p. 788). Both are kinds the chapter keeps."

**SF-5 (Self-Documenting Code and Personal Character; figures described beyond the page).**
- Lesson 2 calls the IBM one-in-ten figure "an average from other people's programs" (body). `mistakes[2]` and the `note` say it is "IBM's, from whole programs". The book says only that studies at IBM found clarity "seemed to peak" at about one comment per ten statements (p. 792). It does not call the figure an average and says nothing of whole programs. Replacement: "That is a finding from other people's programs, reported at second hand…" and "The figure is from IBM studies, as Jones reports it."
- Lesson 3's `note` calls "the 10-to-1 differences … averages from other people's studies". A 10-to-1 ratio is a spread between the best and the worst, not an average. Replacement: "The 10-to-1 differences are spreads between the fastest and slowest programmers in other people's studies, reported by the book…"

**SF-6 (Personal Character; what F29 is cited for).** "McConnell's point in citing them is that character, not intelligence, is the more decisive factor." On p. 820 the 10-to-1 studies are cited to show that "the potential for improvement is huge". The claim that character is "the more decisive factor" follows as McConnell's own statement, with no study behind it. As written, the sentence lets the studies appear to support a claim they do not test. Replacement: "McConnell cites them to show how much room there is to improve. That character, not intelligence, is the more decisive factor is his own claim, which the next sections argue."

**SF-7 (Personal Character; hustle ranked).** The body says "Hustle, visible effort for its own sake, comes off worse than any of them." The book does not rank hustle against the three kinds of laziness. It calls hustle extra, unnecessary effort that shows eagerness, not progress (p. 830), and it treats hustle as a trait that matters less than you might think (start of §33.8). Replacement: "Hustle, visible effort for its own sake, the chapter counts as no virtue at all: it shows eagerness, not progress."

**SF-8 (Themes of Craftsmanship; "inside the book's warning signs").** The worked `after` says "Seven points and a depth of two put the routine inside the book's warning signs". `mistakes[1]` says they "sit inside the book's warning signs". Both mean below the thresholds of §34.7, which are more than about 10 decision points and more than three levels. A reader can take "inside" the other way. The body has just said that 7 falls in Table 19-2's 6–10 band, where the book says to start thinking about simplifying. Replacement: "…put the routine below the thresholds Section 34.7 names (more than about 10, more than three levels), though in Table 19-2's band to start thinking about simplifying, and the counts still point at the loop of lines 6 to 11."

**SF-9 (Layout and Style; research stated in the lesson's voice).** "In 1973 Chase and Simon found…" and "Ben Shneiderman found the same of programmers in 1976" say the work found it outright. §S.1 asks for "as the book cites it". Neither work is in §S.1, and Fjelstad and Hamlen 1979 in lesson 2 is not either. The paragraph opens "The section answers with a line of research", so the fix is small: "Chase and Simon, the book reports, found in 1973…" Add Chase and Simon 1973, Shneiderman 1976 and Fjelstad and Hamlen 1979 to §S.1. All three are on pp. 733–734 and 788.

**SF-10 (Themes of Craftsmanship; near-verbatim without quotation marks).** The quiz `why` on §34.9 reads "rather than latch on to the latest fad, use a mixture of methods, experimenting with new ones and banking on old and dependable ones". That is close to p. 851's two sentences, word for word for about a dozen words, and it is not marked as a quotation. Either paraphrase it ("use several methods: try the new ones, and depend on the proven ones") or quote it with its page. Lesson 4 has 33 words of room.

### Consider

- **C-1 (Layout and Style).** "Section 31.1 opens with cases of this kind (pp. 732–733)". Section 31.1 opens with the three layouts of one routine (pp. 730–732). The cases of human and computer readings come after, under "Human and Computer Interpretations", and are an unbraced `for` (Listing 31-4) and spacing against precedence (31-5). Say "Section 31.1 shows cases of this kind".
- **C-2 (Layout and Style).** `mistakes[1]`: "Six-space indentation looked pleasing to the subjects". The subjects *felt it was easier to use*. "Looks pleasing" is McConnell's guess at why (p. 737). Replacement: "Many of the subjects felt six-space indentation was easier to use, and it scored second lowest…"
- **C-3 (Layout and Style).** Emulating pure blocks is described as "the closing brace as the block's last line". On p. 740 the closing brace is the construct's own end, aligned with the control statement (statement D). Suggest "…and the closing brace, aligned with the `if`, as the end of the construct".
- **C-4 (course).** The course uses two depth conventions without saying so. The layout lesson counts the routine's body as one level ("line 5: depth 2, so 8 spaces"; the key line "expected spaces is depth × indent"). Themes counts depth below the routine's own braces. A sentence in Themes would remove the confusion: "This is not the layout lesson's depth, which counted the routine's body as one level."
- **C-5 (Layout and Style; voice).** The `note`'s "Most editors now re-indent code…" and `not_covered`'s "now done by an editor on save" are a second "since 2004" remark beside lesson 2's designated aside. They do not take a side against the book, so §F.4's limit arguably does not apply, but each should stay at one sentence.
- **C-6 (Themes of Craftsmanship; voice).** "Chapter 34 is the book's account of why it feels that way" credits the chapter with a purpose it does not state. Suggest "Chapter 34 names what such a routine has lost sight of."
- **C-7 (Self-Documenting Code; §S.1).** Martin, *Clean Code* (2008), and Ousterhout, *A Philosophy of Software Design* (2018), are the course's one modern aside, and both are characterised fairly, I believe. They are not in §S.1. Add them there as works outside the book.
- **C-8 (PLAN §C 7.1).** §C gives §§31.4–31.8 as pp. 745–768. Section 31.8 starts on p. 768 and runs to p. 773 (the checklist). The lesson's "pp. 745–772" is closer. Correct §C to 745–773.
- **C-9 (Themes of Craftsmanship; code).** If `request.millisToDeadline()` returns a `long`, line 13 does not compile, because a `long` cannot be assigned to an `int` without a cast. The type is undeclared and the fragment is acceptable. If the lesson ever names the type, make it `int`.

## Claims I could not settle against the page

- Hank and Tony: the lesson says "two reviewers of his first edition, Hank and Tony". The book (p. 734) says Hank reviewed the manuscript and that "both Tony and me" argued for one style. That Tony was also a reviewer is implied, not stated. It is harmless, but "Hank, a reviewer of his first edition, and Tony, a colleague of Hank's," would be safer.
- The characterisations of Martin 2008 and Ousterhout 2018 rest on my own knowledge of those books. I did not check them online.

## Where I disagree with the pedagogy assessment

No pedagogy assessment exists yet for this course. Neither `docs/pedagogy/code-complete-software-craftsmanship.md` nor `docs/reviews/code-complete-software-craftsmanship-pedagogy-review.md` was present when this file was written. I have nothing to compare against. When it lands, check SF-2, SF-3 and SF-8 in particular against any praise of the same passages.
