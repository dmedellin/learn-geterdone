# English — the v2 build specification

This is the curriculum, lab and authoring contract for the second instalment of
the eighth Subject. Everything an author, the kit engineer, the wiring agent or
a reviewer needs is here; nothing in it is a suggestion. Where it says
"exactly", a test or a gate enforces it. Where it says "never", a published
English page has already been wrong for that reason (see
`docs/pedagogy/english-*.md`).

Read before this: `docs/ENGLISH-SUBJECT.md` (all of it — §1 is the test every
lesson passes, §6 the two landmines); `AGENTS.md` §0, §1, §1a and the
page-weight note; `content/AGENTS.md` (all of it); `scripts/mathpath/AGENTS.md`
("a preset's two claims"); `docs/philosophy/PLAN.md` §E–§F for the shape of a
lesson dict and the voice. This document does not repeat them.

**How to read a figure in this document.** Every number a lesson will state
carries one of two marks.

- **(m)** — *designer-measured*: computed on 2026-10-10 by the scripts in
  `docs/english-v2/measure/` over the sources `measure/fetch.sh` downloads and
  the lists already in the repository; the raw outputs are in `measure/out/`.
  These are design figures. The kit engineer re-derives each one from the
  built page with `node scripts/labcheck.js --observe`, pins what the page
  prints, and the author states what the page prints. Where page and plan
  differ, the page wins and this plan is corrected.
- **(k)** — *to be measured by the kit engineer*: the design names the
  computation and the data; no figure exists yet, and no author writes one
  until the page prints it.

A figure with neither mark is a count of things in this document (lessons,
pages) or a published figure quoted with its source. Nothing here is invented.

Contents

- §0 The assessment: the Subject as an ESL syllabus
- §A PATH fields
- §B The ten courses, in order
- §C Every lesson: 41 entries
- §D The kit: thirteen new modes, four extensions, the data pipeline
- §E Listen: what the sounds and endings need
- §F Package layout, the author's checklist, the voice guide
- §G What is left out, and why
- §H Wiring checklist for the orchestrator
- §I Data sources and licences

---

## §0 The assessment

### What the first instalment got right, and must keep

Four courses and ten lessons shipped on 2026-10-09. They hold to a test no
other English course holds to: **state a rule, measure its hit rate on printed
text, show the residue** (`docs/ENGLISH-SUBJECT.md` §1). Every page prints the
words it counted; every figure in prose is one the page computes or is marked
quoted; every page is written inside the NGSL 2,800 at 98% or better. The
pedagogy passes of 2026-10-08 fixed every false claim they found and recorded
what they could not fix. That discipline is the Subject's whole value and this
plan extends it; it does not loosen it.

### What a learner at A2–B2 needs that ten lessons cannot give

The instalment covers verb spelling, irregular verbs, three order rules and
two facts about listening. A syllabus for a learner between A2 and B2 — the
learner these pages are written for, who can read them — needs, and the
Subject lacks, every one of the following. Each is listed with the
computation that makes it admissible; anything without one is in §G.

1. **Helping verbs.** Agreement (*he goes*, not *he go*), the bare form after
   a modal (*she can go*, not *she can goes*), *have* and *be* as helping and
   as main verbs, where *not* goes and when *do* arrives, and which of the
   twelve tense boxes English actually uses. The first instalment promised
   the last of these and then withdrew it because no page computed it. All
   six are rules a scanner can score on a printed passage with the verb-form
   lists the Subject already carries. **New course.**
2. **Nouns and articles.** Plurals (the `-s` rule again, on its other home
   ground, with *children* and *photos* as residue), the nouns that take no
   plural, *a* against *an* by sound rather than letter, and *the* before a
   superlative. All four score on a word list or a concordance. Articles by
   *meaning* (first mention, generic plurals) do not, and are in §G. **New
   course.**
3. **Small words and comparisons.** *In/on/at* with time words, *-er/-est*
   against *more/most* by syllable count, the spelling of *-ly*, and where the
   pronoun goes with a phrasal verb. Each has a closed input (a time-word
   list, a syllable count from CMUdict, an adjective list, a particle list)
   and a concordance to score on. **New course.**
4. **Sound from spelling.** Soft *c* and *g*, the silent *e*, *i before e*
   and its famous failure rate, silent letters, and the endings *-tion*,
   *-sion*, *-ture*. CMUdict makes every one of these a scored rule rather
   than a mnemonic. **New course.**
5. **Word stress**, which the doubling lesson and both listening lessons lean
   on and nothing teaches: nouns at the front and verbs at the back of a
   two-syllable word, the endings that pull the stress and the endings that
   leave it alone, and the flat vowel of the unstressed syllable. CMUdict
   again. **New course.**
6. **How the endings are said** — *-ed* as /t/, /d/ or /ɪd/ and *-s* as /s/,
   /z/ or /ɪz/ — which is the first pronunciation rule any A2 course teaches
   and which scores at 99.4% and 99.8% (m) on the verbs the Subject already
   prints. **New lesson in Tense Tables.**
7. **Contractions and linking**, the two listening facts after weak forms
   and stress: that *n't* is speech (54% of *not* in a play, 0.9% in the
   novel (m)) and that a final consonant joins a following vowel. **Two new
   lessons in Listening.**
8. **How many words you need.** The Subject tells its reader that 98%
   coverage is what reading needs and never lets the reader compute coverage.
   The capstone course does, with the Subject's own rules as the
   lemmatiser. **New course.**

### Which existing lessons are weak or mis-sequenced

- **`five-forms-and-the-whole-table` carries three hard ideas** (build the
  table; score the rules; refute a rule) and sits at the renderer's ceiling of
  18 body blocks; its own review said the cut is after "The rules that make
  four of the five". It is split: the building stays, the scoring and the
  refuted *f → ves* rule become `scoring-a-rule-on-real-verbs`. Same lab mode,
  two panels.
- **Word Order assumes Helping Verbs that nobody has taught.** Its second
  lesson defines *helping verb* in passing and its third moves one and adds
  *do*. The path order is changed: Helping Verbs is course 3, Word Order
  course 5. URLs do not move; only `number` and the check-id prefixes do (§H).
- **`asking-a-question` is scored on cut lines.** Sixteen of its twenty-one
  "something else" misses begin mid-sentence because the concordance was cut a
  fixed distance before the question mark or at the full stop of *Mr.* The
  review called the honest fix upstream; this plan makes it: the concordance
  is re-cut at sentence boundaries, the pinned figures are re-read, and the
  lesson is rewritten against them. Its four-way sort gets four tiles.
- **`how-much-of-english-is-irregular` compares a computed share with a quoted
  top-twenty figure.** The kit gains the tile (`shTop`) so the comparison is
  made on the page as well as quoted.
- **`why-it-sounds-too-fast` says a listed word keeps its full shape at the
  end of a sentence and does not count how often that happens.** A tile.
- **The scanner stops at a typographic apostrophe**, so *I don't know* scores
  as *I don* on `who-does-what-to-whom`. The tokeniser normalises U+2019
  before matching; the affected residue is re-read.
- **Nothing is wrong with the Listening course's two lessons**, and nothing
  is wrong with the Irregular Verbs course's first two; they are kept with
  cross-references by title to the courses that now exist.

### What measurement allows, and the data that makes it possible

Three decisions widen what the Subject can honestly compute.

- **Pronunciation comes from CMUdict**, as the stress flags already do, and
  it is a lookup of a fact (final sound, first sound, stress position,
  syllable count), never a human judgement. That admits the endings, stress,
  letters-to-sounds, *a/an* and linking lessons.
- **Part of speech comes from the Moby Part-of-Speech list** (public domain,
  Gutenberg #3203), used only at build time to pick the noun, verb and
  adjective headwords of the NGSL. Moby tags generously (*and* is a noun
  somewhere), so every derived list is cleaned by the dictionary test
  `clean_verbs.py` already applies, and the cleaning script records every
  exclusion with its reason, as that one does.
- **A play joins the novel.** Oscar Wilde's *The Importance of Being
  Earnest* (1895, public domain, Gutenberg #844) is dialogue, which is what
  the novel and the two modern documents are short of: 13.1 question marks
  per 1,000 words against Austen's 3.9 and the modern documents' 0.0 (m);
  54% of its *not*s are *n't* against 0.9% in the novel (m). It is cut into
  a 1,975-word excerpt (printed) and a 256-question concordance.
  A longer Austen passage, Chapter XXVI (2,338 words, 216 pronoun subjects,
  76 modals (m)), carries the Helping Verbs course.

What measurement still refuses is listed in §G with the number that refused
it.

---

## §A PATH fields (`content/english/__init__.py`)

Unchanged: `slug`, `title`, `level`, `level_note`, `prerequisites`, `material`
(the test `ENG_DISCLAIMER_RE` matches "check by hand rather than something you
are told"; do not reword that clause).

**tagline** (counts are checked by
`test_the_tagline_and_description_state_the_real_counts` against the package;
the current tagline states none and may stay; if a count is written it must
read "Ten courses and 41 lessons"):

> Every rule you have been given about English, with the one thing no book
> prints beside it &mdash; how often it is actually right, and the words it
> gets wrong.

**description**: keep the first two sentences; replace the last with

> Written inside the 2,800 most common words of English, with every other
> word explained where it first appears. Ten courses and 41 lessons.

**key** (every line ≤ 46 characters; no second column): the current seven
lines stay, with the doubling pair replaced by two lines the new courses pin —
the kit engineer supplies the exact strings after `--observe`:

```
a rule, the share it gets right,
and the words it misses

-s 99.92%    -ing 99.34%    -ed 99.26%

a or an by sound, not letter: [sound %] (k)
i before e: [36 of 58] (m) — the famous rule
```

**sequence_intro** — rewrite for ten courses: the first six are grammar and
are in one order (forms, broken forms, helping verbs, nouns, order, small
words); the next three are sound (spelling to sound, stress, listening) and
can be read apart from the first six, Listening first if the reader wants; the
tenth uses every rule before it. Keep the closing sentence that nothing is
announced without a page.

**why_order**: one paragraph per course that needs explaining (ten entries);
the existing four are rewritten to their new positions. Helping Verbs comes
before Word Order "because the adverb and question rules move a helping verb,
and a reader should have met one first". Vocabulary comes last "because its
lab is the other nine courses' rules run as a reading machine".

**footer_lead**: add the play and the two build-time sources:

> … The older passages are public domain: <em>Pride and Prejudice</em>
> (1813) and <em>The Importance of Being Earnest</em> (1895). Pronunciation
> facts are from CMUdict (BSD licence); parts of speech were taken at build
> time from the Moby Part-of-Speech list (public domain) and checked against a
> dictionary, and no page carries either list. The two modern documents …
> are works of the U.S. government.

**Course numbering.** Replace the hard-coded `"number"` in each course dict
with the Philosophy pattern: `COURSES = [c for c in [...] if c is not None]`
and a loop that sets `_course["number"] = _index`. Position is the PATH
order in §B, not the package prefix.

---

## §B The ten courses, in order

Course slugs are global URL segments; the six new ones collide with none of the
68 existing course directories under `site/`. Release-contract check ids use
the prefix `eng` (`eng-course10-lesson-` is 20 characters, so a slug may be up
to 52; every slug here is ≤ 44). Existing packages keep their names; new
packages are `c5_` to `c10_` in path order among the new courses, so two
packages carry a prefix that is not their position (`c3_word_order` is
position 5, `c4_listening` is position 9). `COURSES.json` beside this file is
the manifest and names both.

| n | slug | package | title | level | lessons | status |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | `tense-tables` | `c1_tense_tables` | Tense Tables | Foundational | 4 | existing, 1 rewritten + 1 kept + 2 new |
| 2 | `irregular-verbs` | `c2_irregular_verbs` | Irregular Verbs | Foundational | 3 | existing, 2 kept + 1 rewritten |
| 3 | `helping-verbs` | `c5_helping_verbs` | Helping Verbs | Foundational | 6 | new |
| 4 | `nouns-and-articles` | `c6_nouns_articles` | Nouns and Articles | Foundational | 4 | new |
| 5 | `word-order` | `c3_word_order` | Word Order | Foundational | 4 | existing, 3 rewritten + 1 new |
| 6 | `small-words-and-comparisons` | `c7_small_words` | Small Words and Comparisons | Intermediate | 4 | new |
| 7 | `spelling-to-sound` | `c8_spelling_sound` | Spelling to Sound | Foundational | 5 | new |
| 8 | `word-stress` | `c9_word_stress` | Word Stress | Intermediate | 4 | new |
| 9 | `listening` | `c4_listening` | Listening | Foundational | 4 | existing, 2 rewritten + 2 new |
| 10 | `vocabulary-and-reading` | `c10_vocabulary` | Vocabulary and Reading | Intermediate | 3 | new |

Total: 41 lessons (10 existing — 7 rewritten, 3 kept — and 31 new), 10 course
homes, 1 path page = 52 pages (was 15). Site: 853 → 890 pages; 772 → 803 lessons; 68 → 74
courses; 721 → 758 generated pages.

**1. Tense Tables** (Foundational; assumes nothing). The five forms and the
four rules that build them; the rules scored on 1,210 real verbs and a rule
refuted; the doubling rule and the stress it needs; how the two endings are
said. The course the whole Subject's method is learned on.

**2. Irregular Verbs** (Foundational; assumes Tense Tables). Unchanged in
scope: the list, its six string classes, and how much of a page it is — now
with the top-twenty comparison computed on the passage as well as quoted.

**3. Helping Verbs** (Foundational; assumes Tense Tables and Irregular Verbs).
*Be*, *have*, *do* and the modals as the words that stand in front of a verb:
agreement, the bare form after a modal, *have* and *be* as two words each,
where *not* goes and when *do* arrives, and which of the twelve boxes get
used. Every rule is scored on one printed chapter of the novel (2,338 words)
and on the two modern documents, with every pronoun-and-verb row printed.

**4. Nouns and Articles** (Foundational; assumes Tense Tables, for the `-s`
rule). The plural rule on 1,936 nouns and the lists it leaves; the nouns with
no plural; *a* or *an* by the next sound; *the* before the one that is
only one. Everything is a word list scored against a dictionary or a
concordance scored against a closed list; nothing here is about meaning.

**5. Word Order** (Foundational; assumes Tense Tables, Irregular Verbs and
Helping Verbs). The three existing rules, now with the apostrophe fixed and
the question concordance cut honestly, and a fourth lesson that scores the
question rule on a play, where it covers a third and the residue is what
people actually say.

**6. Small Words and Comparisons** (Intermediate; assumes Nouns and Articles
and Word Stress for the syllable count — Word Stress is later in the path, so
the comparatives lesson defines "part" inline and sends the reader on).
*In/on/at* with time words, *-er* against *more*, *-ly* from an adjective, and
where the pronoun goes with a phrasal verb.

**7. Spelling to Sound** (Foundational; assumes nothing; uses CMUdict). Five
rules that take a spelling to a sound, each scored on the 2,800 words: soft
*c* and *g*, the silent *e*, *i before e*, silent letters, and *-tion*,
*-sion*, *-ture*.

**8. Word Stress** (Intermediate; assumes Spelling to Sound, for what a
CMUdict mark is, and Tense Tables, for the strong part). Where the strong
part falls and what moves it: nouns and verbs of two parts; endings that pull
the stress and endings that leave it alone; the flat vowel.

**9. Listening** (Foundational; assumes nothing; Word Stress helps). The two
existing lessons, plus contractions and linking, each counted on printed text.

**10. Vocabulary and Reading** (Intermediate; assumes Tense Tables, Irregular
Verbs, Nouns and Articles and Small Words and Comparisons, whose rules its lab
runs). How much of a page the 2,800 words cover, computed on the page and on
the reader's own text; the ten words that are a quarter of any page; and
word against word family.

---

## §C Every lesson

Format of each entry, as in `docs/philosophy/PLAN.md` §C:

- **slug** — Title — *module* — **status** (kept | rewrite | new)
- **Do:** the observable objective the `standard` field measures.
- **Lab:** `english` / mode; cfg; presets by id with the instance; the shipped
  value of redraw-only controls; the tiles each preset pins. Expected strings
  are read off the built page with `--observe`, never predicted.
- **Misconception:** the wrong model named as `mistakes[0]`.
- **Worked:** the single worked example, in one line.
- **Figures** the prose will state, each marked (m) or (k).

Cross-references in prose are by TITLE (“Five Forms Make Twelve”, Helping
Verbs), never by number. Every preset menu is `xxPreset`; a redraw-only
`<select>` is `xxShow` or `xxSource`. The lab's `panel_intro` says which of
the printed texts the figures come from and that the 1813 and 1895 texts are
old, where that matters.

### Course 1 — Tense Tables (`tense-tables`, 4)

Modules: *A table you can build* (1), *A rule needs a count* (2), *The rule
that needs the sound* (3–4).

1. **five-forms-and-the-whole-table** — Five Forms Make Twelve — *A table you can build* — **rewrite**
   - Do: take any regular verb, write its five forms by rule, say which of the four rules fired, and fill the twelve boxes by placing *have*, *be* and *will* in front.
   - Lab: `table` (existing). Presets `tbPreset`: walk, stop, carry, hope, listen, go, pinned as today; `tbScore` keeps its five pinned options. The panel intro points at the scoring menu in one sentence and sends the reader to “Scoring a Rule on 1,210 Real Verbs” for what it shows.
   - Misconception: the twelve boxes are twelve things to learn.
   - Worked: *walk* → walk, walks, walking, walked, walked; *has been walking* is the fourth form behind *has been*.
   - What leaves this lesson: the cleaning paragraph, the refuted rule, the three hit rates and the worked example of misses. The body falls to about 12 blocks. The `-ie → -ying` and `-ee/-oe/-ye` sub-cases the code runs are stated in the `-ing` bullet (one clause each).
   - Figures: none stated beyond the forms; 1,210 is mentioned once as the list the next lesson scores.

2. **scoring-a-rule-on-real-verbs** — Scoring a Rule on 1,210 Real Verbs — *A rule needs a count* — **new**
   - Do: run each of the three forming rules over the printed list, read its hit rate and every word it misses, name why each miss is there, and say why the list had to be cleaned before any rule could be scored.
   - Lab: `table` with cfg `focus: "score"` (the kit renders the scoring tiles and table above the twelve-cell grid when `focus` is `score`; same presets, same pins). Shipped `tbShow = residue`.
   - Misconception: a rule that sounds right is right — the *f → ves* rule drops the `-s` score from 1209 to 1205 of 1210.
   - Worked: `-ed` 1201 of 1210, 99.26%; the nine misses sorted into British spelling (*initial*, *counsel*), a *-k* no rule knows (*panic*, *traffic*), doubling against the stress (*format*, *input*, *output*), both spellings in use (*bus*) and no consonant before the vowel (*up*).
   - Figures: 99.92 / 99.34 / 99.26%, 1209 / 1202 / 1201 of 1210, 99.75% and 99.59% for the two variant rules, 146 words left out — all pinned today and unchanged.

3. **when-the-last-letter-doubles** — When the Last Letter Doubles — *The rule that needs the sound* — **kept**
   - One change: the forward reference to where the strong part is taught becomes a reference by title to Word Stress (“Nouns at the Front, Verbs at the Back”). Figures unchanged (199 / 107 / 110 of 217; 18 wrong, 11 in *-l*).

4. **how-ed-and-s-are-said** — How -ed and -s Are Said — *The rule that needs the sound* — **new**
   - Do: say, from the last sound of a verb, whether its *-ed* is said /t/, /d/ or /ɪd/ and its *-s* is said /s/, /z/ or /ɪz/; read the two rules' scores off the printed list; and explain the handful of verbs the rule misses.
   - Lab: `endings` (new, §D). Presets `enPreset`: `ed` (the past ending), `s` (the *he/she/it* ending), `plural` (the same `-s` rule on 1,869 noun plurals, previewing Nouns and Articles). Shipped `enShow = misses`. Pin `enHit`, `enPct`, `enFirst` on each.
   - Misconception: *-ed* is said "ed" — it is a syllable only after /t/ or /d/ (*wanted*, *needed*); after *walk* it is /t/, after *play* /d/.
   - Worked: *walk* ends in /k/, voiceless, so *walked* is /wɔːkt/; *play* ends in a vowel, so *played* is /pleɪd/; *want* ends in /t/, so *wanted* has its extra part — 1,111 of 1,118 verbs follow (m).
   - Figures (m, to be re-read): `-ed` 1,111 of 1,118 = 99.4%; residue *abused, closed, excused, housed, mouthed, used* (the *s* of the verb is /z/ where the dictionary's noun reading is /s/) and *legged*; 92 verbs not in CMUdict are listed as skipped, not counted. `-s` 1,187 of 1,189 = 99.8%; residue *knives*, *mouths* (the *th*/*f* turn voiced). Plural `-s` 1,865 of 1,869 = 99.8%; residue *does, mouths, paths, youths*. Share of plurals by sound: /z/ 1,187, /s/ 523, /ɪz/ 226 (m).
   - Glossary: `voiced` and `voiceless` as `<dfn>` ("said with the throat buzzing" / "without"); the IPA letters only inside `<dfn>` or key lines with spoken forms (§E).

### Course 2 — Irregular Verbs (`irregular-verbs`, 3)

Modules unchanged.

1. **the-verbs-that-break-the-rules** — The Verbs That Break the Rules — **kept**
   - No change beyond cross-references by title. Pins unchanged (133; 6; 60).

2. **six-patterns-not-one-hundred-and-eighty** — Six Patterns, Not One Hundred and Eighty — **kept**
   - No change. Pins unchanged (60 / 37 / 21 / 9 / 4 / 1; the vowel preset 7).

3. **how-much-of-english-is-irregular** — How Much of English Is Irregular — **rewrite**
   - Change: the `irrshare` mode gains `shTop` (the share of the passage's irregular forms covered by its top twenty verbs, under the menu's with/without choice) so the lesson's central comparison — 87.66% against 73.90%, quoted from the novel (recounted 2026-10-10 with the page's tokeniser over 122,294 words, captions removed: 15,147 forms, 12.39% with be/have/do and 5.01% without; the earlier 12.29%, 4.98% and 123,611 split every typographic apostrophe) — has a computed counterpart on the page. The worked example gains one line per menu option; the quiz's fourth question asks which figure the page computes. Pinned figures (149, 15.7%, 91, 61.1%, 58, 6.1%) unchanged; `shTop` (k).

### Course 3 — Helping Verbs (`helping-verbs`, 6)

Modules: *One verb, one helper* (1–2), *Two words each* (3–4), *Not, do and
the boxes* (5–6). All six lessons use `auxchain` (§D) on Chapter XXVI of the
novel (2,338 words) and the two modern documents, printed on every page; each
lesson ships with its own preset selected. The passage is 1813 prose and
each lesson says so where a figure depends on it.

1. **the-s-belongs-to-he-she-and-it** — The -s Belongs to He, She and It — *One verb, one helper* — **new**
   - Do: state which subject takes the *-s* form (and *is*, *has*, *does*, *was*), which take *are*, *were*, *have*, *do*, and which takes *am*; read the rule's score off every pronoun-and-verb pair in the chapter; and name the one kind of row that breaks it on purpose.
   - Lab: `auxchain`, cfg `rule: "agree"`. Pin `axHit`, `axPct`, `axBroken`.
   - Misconception: the *-s* marks the plural, as it does on nouns — on a verb it marks *he, she, it*.
   - Worked: *she was*, *he has*, *it does* against *they were*, *you have*, *we do*; the rows against the rule in the whole novel are *if it were*, *she were*, *he were* (m) — the old wish form, which the lesson names and sets aside.
   - Figures (m, novel-wide, quoted): after *he/she/it*, 1,214 third-person forms against 37 other (1,214 of 1,251; measure/out/corpus.txt, 1,081 + 133); after *you/we/they*, 487 plural forms against 5 third-person. Page figures on the chapter (k).

2. **after-a-modal-the-verb-is-bare** — After a Modal, the Verb Is Bare — *One verb, one helper* — **new**
   - Do: name the nine modals, state that the verb after one takes no ending, allow *not* or an adverb between, and read off the printed chapter what actually follows a modal.
   - Lab: `auxchain`, cfg `rule: "modal"`. Pin `axHit`, `axPct`, `axFormed`.
   - Misconception: *she can goes*, *he must went* — a modal takes the tense, the verb takes nothing.
   - Worked: *could not have been*: modal, *not*, two bare helpers, a participle — the first verb after the modal is bare every time.
   - Figures (m, novel-wide, quoted): 2,738 modals; a bare verb directly 58.5%, *not* between 14.9%, an adverb between 9.5%, a pronoun next (a question) 5.2%; a formed verb (*-s*, *-ed*, *-ing*) next 3 of 2,738 = 0.1%, and the three are printed. Chapter figures (k): 76 modals.

3. **have-is-two-words** — Have Is Two Words — *Two words each* — **new**
   - Do: tell *have* the helper (followed by a participle) from *have* the main verb (followed by a noun phrase), and *have to*; read the three shares off the chapter.
   - Lab: `auxchain`, cfg `rule: "have"`. Pin `axPerf`, `axPct`, `axMain`.
   - Misconception: *have* always means to own.
   - Worked: *had been*, *has written* against *have a sister*, *had no time*; on the whole novel 59.5% helper, 32.1% main verb, 1.1% *have to* (m).
   - Figures (m, quoted): 2,339 forms of *have*; the play 50.1% / 42.0% / 2.9%; the modern documents 69.6% helper. Chapter (k): 37 forms.

4. **be-is-mostly-a-main-verb** — Be Is Mostly a Main Verb — *Two words each* — **new**
   - Do: say what follows a form of *be* on a real page — an *-ing* form, a participle, an adjective, a noun phrase, a place — and read off the chapter how rare the *-ing* form is.
   - Lab: `auxchain`, cfg `rule: "be"`. Pin `axIng`, `axIngPct`, `axPP`.
   - Misconception: *be* is the progressive's helper first and a verb second. On the novel the *-ing* form follows it 4.7% of the time (m).
   - Worked: *is a truth*, *was humbled*, *were very happy*, *is in town*, *was going*: five rows, one of them progressive.
   - Figures (m, quoted): 5,858 forms of *be* in the novel: noun phrase 23.5%, participle (passive or adjective) 20.8%, noun or name 14.3%, preposition 12.6%, adjective 10.4%, *-ing* form 4.7%, a pronoun next 2.4%; the play 5.6% *-ing*. Chapter (page): 137 forms, 6 followed directly by an *-ing* word (4.4%), 7 by hand. The lesson says the scan cannot tell a passive from an adjective (*was pleased*) and prints both as one class.

5. **where-not-goes** — Where Not Goes, and When Do Arrives — *Not, do and the boxes* — **new**
   - Do: put *not* after the first helping verb, add *do* when there is none, and read off the chapter how often *not* sits where the rule says and what the other rows are.
   - Lab: `auxchain`, cfg `rule: "not"`. Pin `axHit`, `axPct`, `axOld`.
   - Misconception: *I know not* and *she likes not* are English — they were, in 1813, and the chapter shows how often; today *do* is required.
   - Worked: *could not*, *has not*, *do not know* against *know not*, *dared not*, *need not*; the novel puts *not* after a helping verb 78.8% of the time and after a main verb 6.3% (m), the play 86% after a helper with 53.5% of them contracted (m).
   - Figures (m, quoted): 1,440 *not*s in the novel; 10 in the modern documents, 8 after a helper. Chapter (k): 39.

6. **which-of-the-twelve-boxes-get-used** — Which of the Twelve Boxes Get Used — *Not, do and the boxes* — **new**
   - Do: sort every pronoun-subject verb phrase on the printed chapter into the twelve boxes (plus *be* and *have* as main verbs, *do*-support and the passive), read the shares, and say which two boxes carry most of real writing.
   - Lab: `auxchain`, cfg `rule: "boxes"`. Pin `axSimple`, `axProg`, `axPerf`.
   - Misconception: the progressive is the ordinary present — the box drilled hardest in classrooms is about one phrase in seventy in the novel (m).
   - Worked: *she had been*, *I am sure*, *they will come*, *he was reading*: past perfect, *be* as main verb, future simple, past progressive.
   - Figures (m, novel-wide, quoted; 8,864 pronoun subjects): past simple 18.2%, present simple 12.5%, *be* as main verb 15.5%, modal or future simple 8.4%, past perfect 2.8%, present perfect 1.8%, all progressives together 143 of 8,864, 1.6% (the 1.5% first written here summed rounded shares), passive 3.3%, no verb found 17.7% (lexicon gaps and *it* before a non-verb — the rows are printed). The 2026-10-08 design record's "progressive 1.4% over 1,951 phrases" is consistent and is superseded by what the page prints. Chapter (k): 216 pronoun subjects.

### Course 4 — Nouns and Articles (`nouns-and-articles`, 4)

Modules: *One and more than one* (1–2), *A, an and the* (3–4).

1. **one-noun-two-nouns** — One Noun, Two Nouns — *One and more than one* — **new**
   - Do: apply the plural rule (add *-s*; *-es* after a hiss; consonant + *-y* → *-ies*), read its score on the printed noun list, show that the two "improvements" (*-o → -oes*, *f → ves*) make it worse, and learn the irregular plurals as the short list they are.
   - Lab: `wordrule` (new, §D), cfg `list: "plurals"`. Presets `wrPreset`: `r0` (the three-part rule), `r1` (adding consonant + *-o* → *-oes*), `r2` (adding *f/fe → ves*), `r3` (adding *ves* for the short list *-lf, -ife, -eaf, -olf* only). Shipped `wrShow = misses`. Pin `wrHit`, `wrPct`, `wrFirst`.
   - Misconception: *f → ves* is the rule — on nouns it fits *knife, wife, half, self, shelf, wolf, leaf* and breaks *belief, chief, roof, proof, safe, cliff* (m).
   - Worked: *potato → potatoes* but *photo → photos*, *piano → pianos*, *radio → radios*; adding the *-oes* rule gains one word and loses five (m).
   - Figures (m, to be re-read after the irregular-plural override in §D): the three-part rule 1,918 of 1,936 = 99.1%; with *-oes* 1,916 (99.0%); with *ves* 1,911 (98.7%). Residue: *children, women, chairmen, gentlemen, teeth, halves, selves, shelves, wives, analyses, crises, emphases, hypotheses, phenomena, potatoes, stomachs* (its *-ch* is /k/), *heroes*; *men*, *feet*, *mice* join once the dictionary's verb forms *mans*, *foots*, *mouses* stop counting as plurals (§D). The hiss rule's one failure is the same *stomach* the verb rule missed.

2. **nouns-with-no-plural** — Nouns With No Plural — *One and more than one* — **new**
   - Do: read the list of nouns for which the dictionary confirms no plural, sort it into things you cannot count (*advice, furniture, information*), words that are already plural or the same both ways (*news, sheep, series, species, aircraft, data*), and names of days and months; and state the two things such a noun never takes (*-s*, and *a* or *an*).
   - Lab: `wordrule`, cfg `list: "plurals"`, shipped `wrShow = noplural`. Preset `wrPreset` = `r0`. Pin `wrNone` and `wrNoneOf`.
   - Misconception: every noun has a plural; *informations* and *advices* are the commonest written errors at A2.
   - Worked: of 738 noun-only headwords, 99 have no plural the dictionary confirms (m); the printed list, with the function words Moby mis-tags set aside by name.
   - Figures (m, to be re-read): 99 of 738; the quoted novel counts for twelve of them (*advice, information, news, furniture, money, knowledge, happiness, music, health, help, wealth, poetry*: 0 with *a/an* and 0 plurals in 122,294 words), beside *time* (*a time* 10, *times* 19) and *hope* (*hopes* 23) as nouns that count in one sense and not in another. The second half of the rule (no *a/an*) is a quoted count, and the lesson says so.

3. **a-or-an-by-sound-not-by-letter** — A or An: by Sound, Not by Letter — *A, an and the* — **new**
   - Do: choose *a* or *an* from the first SOUND of the next word, read both rules' scores on 455 printed lines, and name the words where letter and sound disagree.
   - Lab: `an` (new, §D). Presets `anPreset`: `letter` (an before a vowel letter), `sound` (an before a vowel sound). `anSource` redraw-only: all / the play / the modern documents / the passage; shipped `all`. Pin `anHit`, `anPct`, `anFirst`.
   - Misconception: *an* goes before a vowel letter — *an university*, *a hour*.
   - Worked: *a University*, *a utilitarian*, *an hour* are the three lines the letter rule misses and the sound rule gets (m); *an union* is Austen's 1813 habit, which the page quotes and the sound rule marks wrong.
   - Figures (m, to be re-read with the "(a)" list markers skipped, §D): the play, 455 lines, letter 448 (98.5%) against sound 455 (100.0%); the two modern documents 39 lines; the passage 9 lines, both rules 9 of 9. Quoted from the novel: 2,266 lines, letter 98.8%, sound 99.9%, the three sound misses *an union* (twice) and *an uniform*; *such a one*, *many a one*, and, on the novel, *hour*, *honour*, *honourable* and *one* as the letter rule's other losses (measure/out/cmudict.txt; the letter rule gets *a history* and *a hundred* right).

4. **the-before-the-only-one** — The Before the Only One — *A, an and the* — **new**
   - Do: put *the* (or a possessive) before a superlative, *same* and *next*; read the rule's score off the printed lines; and name what else stands there — *at first*, *at last*, *a most* as an intensifier.
   - Lab: `the_super` (new, §D). Presets `tsPreset`: `est` (*-est* adjectives), `same`, `next`, `most` (*most* + adjective). Pin `tsHit`, `tsPct`, `tsOther`; on `most` pin `tsA`.
   - Misconception: *most* always makes a superlative — in the novel *a most agreeable man* outnumbers *the most* (45 against 37) (m).
   - Worked: *the eldest*, *her youngest sister*, *the same* 69 of 69; *at first* and *at last* as the fixed phrases that keep *first* and *last* out of the count.
   - Figures (m, to be re-read): *-est* 142 lines, *the* 93 + a possessive 34 = 127 (89.4%); *same* 69 of 69 (100%); *next* 72 lines, *the* 45; *most* + adjective 122 lines, *the* 37, a possessive 3, *a/an* 45, other 37.

### Course 5 — Word Order (`word-order`, 4)

Modules: *Pronouns and verbs* (1), *The middle place* (2), *Questions* (3–4).

1. **who-does-what-to-whom** — Who Does What to Whom — **rewrite**
   - Changes only: the tokeniser normalises the typographic apostrophe, so *I don't know* is scanned as *don't*; the residue row and the sentence explaining *I don* are rewritten to what the page then prints (k). Helping Verbs is now referenced by title where "the small verbs such as *had*, *was* and *could*" are named. Pins re-read.

2. **where-the-adverb-goes** — Where the Adverb Goes — **rewrite**
   - Changes only: *helping verb* is no longer defined here with `<dfn>`; the lesson says "a helping verb, as Helping Verbs calls them" and the term is in the glossary once. Pins unchanged (85 of 120, 70.8%).

3. **asking-a-question** — Asking a Question — **rewrite**
   - Data: `question_concordance.json` re-cut by `scripts/wordlists/concordance.py` at sentence boundaries (a question starts after `.`, `!`, `?` or an opening quotation mark, never after the full stop of *Mr.*, *Mrs.*, *Miss*, *Dr.*, *St.*), 90 lines kept. Kit: `questions` gains tiles `quWh` (a wh-word with no helping verb after it), `quAddr` (a word of address first), `quFrag` (no verb at all) and `quStmt` (a pronoun first: a statement with a question mark) so the four-way sort the lesson teaches has four tiles. Every figure re-read (k); the lesson no longer explains cut lines because there are none.

4. **how-people-really-ask** — How People Really Ask — *Questions* — **new**
   - Do: score the same question rule on 256 questions from a play, read that it covers about a third, and name the five kinds of question that make up the rest.
   - Lab: `questions`, cfg `source: "wilde"`. Preset `quPreset`: `aux` as today. Pin `quHit`, `quPct`, `quFrag`.
   - Misconception: the low score means the rule is wrong; the score means most spoken questions are not full sentences.
   - Worked: *A hand-bag?*, *Gwendolen, will you marry me?*, *You don't mean to say that…?*, *Finished what, may I ask?* — a fragment, a name first, a statement with a question mark, an echo.
   - Figures (page, `wilde_questions.json` as shipped): 256 questions of two words or more, the rule holds for 89 (34.8%); joining word first 35 (21.0% of the 167 misses), pronoun first 27, wh-word with no helper after it 24, word of address 20, no verb 14, something else 47. Design figures, superseded (167 questions): helping verb first 38 (22.8%), wh-word then a helper 17 (10.2%), together 55 (32.9%); wh-word with no helper after it 18, a joining word first 18, a pronoun first 17, something else (names, fragments) 59. Austen's 90 questions, re-cut (k), beside them; question marks per 1,000 words: play 13.1, novel 3.9, modern documents 0.0 (m).

### Course 6 — Small Words and Comparisons (`small-words-and-comparisons`, 4)

Modules: *Prepositions and particles* (1, 4), *Making a comparison* (2), *Making an adverb* (3).

1. **in-on-at-for-time** — In, On or At: Time — *Prepositions and particles* — **new**
   - Do: state the three-part rule (*at* a clock time, *night*, *noon* and a festival; *on* a day, and on a particular day's morning or evening; *in* a month, a year, a season and the unspecified morning, afternoon or evening), read its score off every printed line, and name the residue.
   - Lab: `time_preps` (new, §D). Preset `tpPreset`: `all`, `austen`, `wilde`, `modern`. Pin `tpHit`, `tpPct`, `tpN`.
   - Misconception: *in the morning* makes *in Monday morning* — the day wins: *on Monday morning*.
   - Worked: *on Tuesday*, *in July*, *in 2025*, *at eight*, *at night*, *in the evening*, *on the following morning*.
   - Figures (m, to be re-read with the two-word window and digit tokens): the novel 73 lines, 72 by the rule (98.6%) before the "particular day's morning" clause, residue *on the evening*; *on Wednesday morning*, *on the following morning*, *on the very morning*, *on the third morning* are the clause's cases; the play 13 lines; the modern documents 12 (eleven of them *in* + a year). Time words with no preposition (*every morning*, *next Tuesday*) are listed, not scored.

2. **bigger-or-more-big** — Bigger or More Big — *Making a comparison* — **new**
   - Do: choose *-er/-est* or *more/most* by the number of parts in the adjective (one part: *-er*; two parts ending in *-y*: *-ier*; otherwise *more*), read the rule's score off every comparative on the printed lines, and name the two-part adjectives the novel inflects that a modern writer would not.
   - Lab: `compare` (new, §D). Preset `cpPreset`: `austen`, `wilde`, `modern`. `cpRule` redraw-only: A (one part, or two ending *-y*) / B (also two ending *-ow, -le, -er*); shipped A. Pin `cpHit`, `cpPct`, `cpFirst`.
   - Misconception: *more* is always safe — *more big*, *more happy* are the errors; *more angry* appears once in the novel and is the rule's one *more*-side miss (m).
   - Worked: *bigger*, *happier*, *more beautiful*; *handsomer* and *pleasanter* (Austen) against *more handsome*, *more pleasant* (now).
   - Figures (m, to be re-read): novel 367 tokens, rule A 91.8%, rule B 92.9%; residue *pleasanter* (4), *handsomest* (4), *handsomer* (3), *oftener* (3, an adverb), *pleasantest* (2), *quieter, stupider, commonest, minutest, gentlest, nobler, more strange, more angry, most likely*; the play 49 tokens, 89.8% / 91.8%; the modern documents 32 tokens, 100%. The syllable count is CMUdict's and the lesson says so.

3. **happily-simply-truly** — Happily, Simply, Truly: Making an Adverb — *Making an adverb* — **new**
   - Do: make the *-ly* adverb from an adjective with the four spelling changes (*-y → -ily*, *-le → -ly*, *-ic → -ically*, *-ue → -uly*, plus *full → fully*), read the rule's score against the dictionary, and name the adjectives that have no *-ly* adverb at all.
   - Lab: `wordrule`, cfg `list: "ly"`. Presets `wrPreset`: `plain` (adjective + *ly*), `changes` (with the spelling changes). Shipped `wrShow = misses`. Pin `wrHit`, `wrPct`, `wrFirst`; `wrNone` on both.
   - Misconception: add *-ly* and you are done — *happyly*, *simplely*, *basicly* are the errors, and *publicly* is the one *-ic* adjective that does not take *-ically* (m).
   - Worked: *happy → happily*, *simple → simply*, *basic → basically*, *true → truly*, *full → fully*; *afraid, alive, aware, difficult, elderly, foreign, pregnant, sorry, ugly* have no *-ly* adverb the dictionary knows (m).
   - Figures (m, to be re-read): 153 adjective-only headwords; an *-ly* adverb exists for 126; plain *+ly* spells 98 of them (77.8%), the rule with changes 126 of 126 (100.0%); 27 with none. The lesson states the limit: the dictionary confirms *hardly*, *lately*, *highly* as words and cannot say that they do not mean *hard*, *late*, *high*; the flat adverbs are named in prose, not counted.

4. **give-it-up-not-give-up-it** — Give It Up, Not Give Up It — *Prepositions and particles* — **new**
   - Do: tell a particle (*up, out, off, down, away, back, over*) from a preposition (*at, to, for, of, with*) by where a pronoun object goes — between the verb and a particle, after a preposition — read the rule's score off the printed lines, and read which phrasal verbs a page actually uses.
   - Lab: `phrasal` (new, §D). Presets `phPreset`: `pronoun` (where the pronoun goes), `freq` (the twenty-five commonest, ranked). Pin `phBetween`, `phPct` on `pronoun`; `phTop` on `freq`.
   - Misconception: *look at it* proves *give up it* — *at* is a preposition and *up* is a particle, and the pronoun's place is the test that tells them apart.
   - Worked: *find it out*, *give it up*, *put it off* against *look at him*, *think of it*, *get over it*; *go away* 32, *sit down* 29, *come back* 16 are the novel's three commonest (m).
   - Figures (m, to be re-read with *her* excluded as a possessive): novel 439 verb-plus-particle tokens; pronoun between 40; pronoun after the particle 28 before the *her* fix, of which *lift up her eyes*-type rows are possessives; verb-plus-preposition-plus-pronoun 803 (*look at* 26, *think of* 14, *speak to* 14); the play 133 tokens, between 17, after 7.

### Course 7 — Spelling to Sound (`spelling-to-sound`, 5)

Modules: *A letter and its sound* (1–2), *The famous rule* (3), *Letters you
do not say* (4), *Endings said one way* (5). All five use `letters` (§D);
each lesson's cfg `rules` lists only its own presets.

1. **c-and-g-before-e-i-and-y** — C and G Before E, I and Y — *A letter and its sound* — **new**
   - Do: say *c* as /s/ and *g* as /dʒ/ before *e, i, y* and as /k/ and /g/ otherwise; read both rules' scores on the 2,800 words; name the ten everyday words where *g* breaks it.
   - Lab: `letters`, cfg `rules: ["softc", "softg"]`. Pin `ltHit`, `ltPct`, `ltFirst`.
   - Misconception: the two rules are equally good — *c* is perfect and *g* fails on *get, give, girl, gift, begin, forget, gear, target, together, altogether* (m).
   - Worked: *city, cell, cycle* /s/; *cat, cold, cup* /k/; *gentle, giant, gym* /dʒ/; *get* — the first word every learner meets — /g/.
   - Figures (m, to be re-read): soft *c* 348 of 348 (100.0%); soft *g* 177 of 187 (94.7%). The lesson says which words were scored (those where the letter is the only possible source of the sound, §D) and how many were set aside.

2. **the-silent-e-and-the-vowels-name** — The Silent E and the Vowel's Name — *A letter and its sound* — **new**
   - Do: read a one-part word ending consonant-vowel-consonant-*e* with its vowel saying its name (*make, these, time, hope, cute*), read the rule's score, and learn the nine very common words that break it.
   - Lab: `letters`, cfg `rules: ["magic", "magic_r"]`. Pin `ltHit`, `ltPct`, `ltFirst`.
   - Misconception: the exceptions are rare words — they are *have, give, come, some, love, none, lose, move, prove* (m), among the commonest in the language.
   - Worked: *hop → hope*, *bit → bite*, *cut → cute*; *have* keeps its short vowel because English does not end a word in *v*.
   - Figures (m, to be re-read): 131 of 140 (93.6%) with *r* excluded; the 19 *-re* words (*care, more, sure, there, where*…) scored apart under `magic_r` because *r* changes every vowel before it; the page prints 1 of 19 for `magic_r`.

3. **i-before-e-and-its-failure-rate** — I Before E, and Its Failure Rate — *The famous rule* — **new**
   - Do: apply "i before e except after c" to every *ie* and *ei* in the 2,800 words, read its score, and sort the residue into the groups that make it fail (*eigh*, *ei* said /aɪ/ or /eɪ/, *cie* in *-cient*/*science*).
   - Lab: `letters`, cfg `rules: ["ie", "ie_ee"]`. Pin `ltHit`, `ltPct`, `ltFirst`.
   - Misconception: the rule is a rule — at 62% on common words it is a coin with a bias.
   - Worked: *believe, friend, receive* follow; *their, weight, height, foreign, either, science, society, species, sufficient* do not.
   - Figures (m, to be re-read): 36 of 58 occurrences (62.1%); restricted to the spots where the word's vowel is /iː/ by one-to-one alignment (`ie_ee`), the page prints 14 of 18; the design's rough 23 of 31 counted words with /iː/ anywhere.

4. **letters-you-do-not-say** — Letters You Do Not Say — *Letters you do not say* — **new**
   - Do: apply five silent-letter rules (*gh* after a vowel is silent or /f/; *kn-*, *wr-*, *-mb*, *-mn*, *-lk*, *-lm* drop a letter; *h* is said except in three words) and read what *ough* does across ten words.
   - Lab: `letters`, cfg `rules: ["gh", "kn_wr_mb", "h", "ough"]`. Pin `ltHit`, `ltPct`; on `ough` pin `ltSounds`.
   - Misconception: English spelling has no rules for silent letters — *gh* is never /g/ in 42 of 42 common words (m).
   - Worked: *knee, know, write, wrong, climb, bomb, autumn, column, walk, talk, calm, half*; *hour, honest, honour* against 77 *h* words said with an /h/.
   - Figures (m, to be re-read): *gh* 42 of 42; *kn* 5 of 5, *wr* 4 of 4, *mb* 2 of 2, *mn* 3 of 3, *lk* 3 of 3, *lm* 2 of 2 (one preset, 19 words); *h* said in 77 of 80; *ough* in 10 words takes 5 sounds (*though, through, thought, tough, cough*).

5. **tion-sion-and-ture** — -tion, -sion and -ture — *Endings said one way* — **new**
   - Do: say *-tion* as /ʃən/, *-sion* as /ʒən/ after a vowel letter and /ʃən/ after a consonant, *-ture* as /tʃə/, *-cial/-tial* as /ʃəl/, and read each rule's score.
   - Lab: `letters`, cfg `rules: ["tion", "sion", "ture", "cial"]`. Pin `ltHit`, `ltPct`, `ltFirst`.
   - Misconception: *-tion* is said as it is spelt — and *question*, *suggestion*, *equation* are the three that are not /ʃən/ (m).
   - Worked: *nation, station, decision, vision, tension, nature, picture, social, special*.
   - Figures (m, to be re-read): *-tion* 123 of 127 (96.9%), residue *question, suggestion, equation, intention*; *-sion* 24 of 25 (96.0%), residue *version*; *-ture* 19 of 20 (95.0%), residue *mature*; *-cial/-tial* 12 of 12.

### Course 8 — Word Stress (`word-stress`, 4)

Modules: *Where the strong part falls* (1), *Endings* (2–3), *The weak part*
(4). All four use `stress` (§D). The lesson defines a `<dfn>part</dfn>` as a
syllable in its first paragraph; the word *syllable* is not in the band and
is not used.

1. **nouns-at-the-front-verbs-at-the-back** — Nouns at the Front, Verbs at the Back — *Where the strong part falls* — **new**
   - Do: for a two-part word, put the strong part first if it is a noun and second if it is a verb; read both rules' scores; and read the 49 words that are both (*REcord*/*reCORD*).
   - Lab: `stress`, cfg `rules: ["nouns2", "verbs2", "adj2", "pairs"]`. Pin `stHit`, `stPct`, `stFirst`; on `pairs` pin `stCount`.
   - Misconception: the strong part has no rule — for two-part nouns and verbs it has one that is right nine times in ten (m).
   - Worked: *TAble, MOney, WINdow* against *beGIN, forGET, deCIDE*; *record* both ways.
   - Figures (m, to be re-read): nouns 207 of 231 (89.6%), residue *advice, affair, belief, complaint, decade, device, disease, event, hotel, July, machine*-type words; verbs 134 of 150 (89.3%), residue *alter, argue, differ, enter, govern, listen, marry, suffer, threaten*; adjectives 35 of 47 (74.5%); 49 noun-verb pairs with both patterns in CMUdict (*address, conduct, contract, decrease, increase, object, permit, present, produce, progress, project, protest, record, refuse, subject, survey, suspect, transfer, transport*…).

2. **endings-that-pull-the-stress** — Endings That Pull the Stress — *Endings* — **new**
   - Do: put the strong part on the part before *-tion*, *-sion*, *-ic*; two before *-ical*, *-ity*, *-ate*, *-ize*; on the ending itself for *-ee*, *-eer*, *-ese*; and read each rule's score.
   - Lab: `stress`, cfg `rules: ["tion", "ic", "ical", "ity", "ate", "ize", "ee"]`. Pin `stHit`, `stPct`, `stFirst`.
   - Misconception: the stress of *photograph* survives into *photography* — the ending moves it.
   - Worked: *NAtion → naTIONal*, *ECOnomy → ecoNOMic*, *ABle → aBILity*, *CELebrate*, *refuGEE*.
   - Figures (m, to be re-read): *-tion/-sion* 151 of 152 (99.3%, residue *television*); *-ic* 28 of 28; *-ical* 16 of 16; *-ity* 27 of 27; *-ate* verbs of three or more parts 36 of 36; *-ize* 13 of 14 (*characterize*); *-ee/-eer/-ese/-ette* (k) — the design count (16 of 21) read the first primary stress and CMUdict gives *engineer* two; the kit reads the last, and *coffee*, *committee*, *employee*, *refugee* are the expected residue.

3. **endings-that-leave-it-alone** — Endings That Leave It Alone — *Endings* — **new**
   - Do: add *-ly, -ness, -ment, -ful, -less, -er, -ish, -able* without moving the strong part, and read each pair's score.
   - Lab: `stress`, cfg `rules: ["ly", "ness", "ment", "er", "ful", "able"]`. Pin `stHit`, `stPct`, `stFirst`.
   - Misconception: every ending moves the stress.
   - Worked: *HAPpy → HAPpiness*, *aGREE → aGREEment*, *CAREful*, *TEACHer*; *adVERtise → adVERtisement* is the one *-ment* pair where American speech moves it (m).
   - Figures (m, to be re-read): *-ly* 83 of 87 (95.4%; residue *absolutely, necessarily, perfectly, primarily*), *-ment* 31 of 32, *-ness* 6 of 6, *-er* 48 of 50 (*career*, *researcher*), *-ful* 7 of 7, *-able* 10 of 10. Pairs are formed only where both stem and derived word are in the 2,800 and in CMUdict.

4. **the-flat-vowel** — The Flat Vowel — *The weak part* — **new**
   - Do: say that the weak part of a word usually takes the flat vowel whatever its spelling, read the share off the 2,800 words, and name the two endings that do not (*-y* as /iː/, *-ing* as /ɪ/).
   - Lab: `stress`, cfg `rules: ["schwa"]`. Pin `stSchwa`, `stPct`, `stIy`.
   - Misconception: a vowel letter is said as itself in every part of a word — in the weak part, *a, e, i, o, u* mostly collapse to one sound.
   - Worked: *about, taken, pencil, lemon, circus* — five spellings, one sound; Listening's small words do the same.
   - Figures (m, to be re-read): 2,628 weak parts in the 2,800 words of two or more parts; the flat vowel 1,387 (52.8%); the *r*-coloured flat vowel 400 (15.2%); /ɪ/ 352 (13.4%); /iː/ 348 (13.2%, the *-y* endings); other 141 of 2,628, 5.4% (the page's figure; 4.8% was written here first).

### Course 9 — Listening (`listening`, 4)

Modules unchanged for 1–2; *Where the small words went* (3), *No gaps* (4).

1. **why-it-sounds-too-fast** — Why It Sounds Too Fast — **rewrite**
   - Change: `listening` gains `lsFinal` (listed words standing last before a punctuation mark, the position where a weak form is said in full); the "most it could be" paragraph quotes it. Cross-reference Word Stress by title. Pins now 387 of 936 (41.3%), 43, 42, `lsFinal` 24 of 387, after the passage was re-cut without its Gutenberg furniture (was 388 of 949, 40.9%, 43, 42); `lsFinal` (k).

2. **where-a-word-begins** — Where a Word Begins — **rewrite**
   - Change: the sentence "there is no reliable rule from the spelling" becomes a pointer to Word Stress by title (there are rules by part of speech and by ending, and they are scored there). Pins unchanged (399 of 485, 82.3%).

3. **where-the-small-words-went** — Where the Small Words Went — *Where the small words went* — **new**
   - Do: expand every contraction to its full form (*n't* → *not*; *'ll* → *will*; *'m* → *am*; *'re* → *are*; *'ve* → *have*; *'d* → *would* or *had*; *'s* → *is*, *has* or a possessive), read off three printed texts how much of *not* is *n't*, and say which kind of text contracts.
   - Lab: `contractions` (new, §D). Presets `coPreset`: `wilde` (the 1,975-word excerpt), `austen` (the 936-word passage), `modern`. Pin `coNt`, `coPct`, `coK`.
   - Misconception: contractions are careless English — in the play a majority of *not*s are *n't*, in the novel almost none, and the difference is speech against print.
   - Worked: *don't, isn't, it's, I'm, won't, can't, I'll*: the seven commonest in the play (m); *won't* is the one whose full form is not inside it.
   - Figures (m, to be re-read): the excerpt, 22 *n't* against 14 *not* (61.1%; *cannot* counted as a *not*, page figure), 36 contractions, 8 question tags among them; the passage (k); the modern documents 0 *n't* against 10 *not*. Quoted: the whole play 168 against 143 (54.0%), 14.7 contractions per 1,000 words; the whole novel 12 against 1,397 (0.9%), of its 644 *'s* nearly all possessives (*Bingley's*, *Darcy's*).

4. **why-words-run-together** — Why Words Run Together — *No gaps* — **new**
   - Do: mark the word boundaries on a printed passage where a final consonant meets a first vowel (and is said as the start of the next word), where two vowels meet, and where the same consonant ends one word and begins the next (and is said once); read the three shares.
   - Lab: `linking` (new, §D). Presets `lkPreset`: `cv`, `vv`, `same`. Pin `lkCount`, `lkPct`.
   - Misconception: *an apple* has a gap in it — the listener hears *a napple* and has to know where the *n* belongs.
   - Worked: *an hour*, *take it*, *not at all*; *big game* said with one /g/.
   - Figures (m, to be re-read): 418 boundaries with only a space between on the passage, 408 scored (10 have a word CMUdict lacks); consonant-to-vowel 59 (14.5%); vowel-to-vowel 28 (6.9%); the same consonant twice 11; consonant-to-consonant 188 (46.1%).

### Course 10 — Vocabulary and Reading (`vocabulary-and-reading`, 3)

Modules: *How much you know* (1), *The commonest words* (2), *Word and
family* (3). All three use `coverage` (§D). The lab's word list is the 2,859
headwords with their band; every form is built on the page by the Subject's
own rules — the `-s/-ing/-ed` rules of Tense Tables, the irregular list, the
plural rule and irregular plurals of Nouns and Articles, the `-er/-est` and
`-ly` rules of Small Words and Comparisons — which is why this course is last.

1. **how-much-of-a-page-you-know** — How Much of a Page You Know — *How much you know* — **new**
   - Do: compute the share of a printed page covered by the first 1,000, 2,000 and 2,800 headwords; compare it with the 98% a reader needs (Nation, quoted) and the 92% the NGSL claims for general text (Browne, Culligan and Phillips, quoted); and paste a text of your own.
   - Lab: `coverage`. Presets `cvPreset`: `passage`, `wilde`, `modern`, `own` (a textarea; refused below fifty words). Pin `cvB1`, `cvB3`, `cvNames`.
   - Misconception: 2,800 words is enough to read — on these pages it is 88–91% by word and 93–95% once names are counted, and the lesson says what the missing five points cost (m).
   - Worked: the passage, 936 words: band 1 85.0%, bands 1–2 89.2%, bands 1–3 91.0%, with names 94.3% (page; the design's 84.0/88.5/90.6/94.6 are superseded); the unknown words printed as the list to learn next.
   - Figures (m, to be re-read): the passage as above; the modern documents 76.0 / 84.7 / 87.3 / 92.7% (page); the play excerpt 79.5 / 83.9 / 85.9 / 94.6% (page); quoted: the novel 80.7 / 86.1 / 88.4 / 93.0%. Nation's 98% and the NGSL's published 92% are quoted with sources and never embedded. The kit engineer measures and the lesson states the gap between coverage by the shipped forms list and coverage by the rules (k).

2. **ten-words-are-a-quarter-of-the-page** — Ten Words Are a Quarter of the Page — *The commonest words* — **new**
   - Do: rank the words of a printed page by how often they appear and read what share the top ten, fifty and hundred cover; name them as the grammar words Listening squashes.
   - Lab: `coverage`, shipped `cvShow = top`. Pin `cvTop10`, `cvTop50`, `cvTop100`.
   - Misconception: the commonest words are the ones worth learning first because they carry the meaning — they are *the, to, of, and, a, in, was, I, she, it*, and they carry the grammar.
   - Worked: on the passage the top ten cover 25.6%, the top fifty 54.5%, the top hundred 67.7% (page).
   - Figures (m, to be re-read): the passage as above; the modern documents 24.7 / 47.3 / 60.6% (page); quoted: the novel 22.4 / 48.1 / 58.9%, 6,308 distinct words.

3. **word-or-word-family** — Word or Word Family — *Word and family* — **new**
   - Do: say what a flemma (a headword with its inflections) and a family (a headword with its derived forms: *-ly, -ness, -ment, un-, re-*) each count, switch the lab between them, and read how many points the family adds to coverage.
   - Lab: `coverage`, shipped `cvShow = family`. Pin `cvB3`, `cvFam`.
   - Misconception: the published thresholds and the page's figure measure the same thing — Nation counts families, the NGSL counts flemmas, and the gap is three to six points on general text (quoted from `docs/ENGLISH-SUBJECT.md` §4) and 1–2 points on these pages (m).
   - Worked: *happiness*, *unhappy*, *carefully* are three words to a flemma count and one family to Nation.
   - Figures (m, to be re-read): the passage 94.3% → 95.6% (+1.3); the modern documents 92.7% → 93.7% (+1.0); the play 94.6% → 95.4% (+0.8) (page); quoted: the novel 93.0% → 94.6%.

---

## §D The kit

### D.0 Conventions every new mode obeys

- **Files.** `scripts/mathpath/labs/english.py` (the modes) and
  `scripts/mathpath/labs/english_core.py` (every rule function as JavaScript
  in a module-level string). `MODES` grows from 9 to 22. `english_lab` keeps
  raising on an unknown mode. `tests/test_english_kit.py` already requires
  every mode to be used by a lesson, to emit ES5, and to pin every preset
  option; it gains `--check` calls for every new data file (D.2).
- **Per-mode script assembly**, as today: a page ships `SCAN_JS`, the data its
  mode reads, and that mode's block. Nothing else. Budget: ≤ 48 KB gzipped per
  English lesson page, measured with the snippet in `AGENTS.md` before the
  kit is called done; the heaviest page today is 38.6 KB. Shipped exception:
  the three Vocabulary and Reading lessons are 51–52 KB, because the
  `coverage` lab carries the headword list and three texts; accepted under
  the library's 67 KB ceiling and recorded in AGENTS.md.
- **The tokeniser.** `wordsOf` normalises U+2019 and U+2018 to `'` before
  matching (the `svo` residue changes and is re-read). A second tokeniser
  `tokensOf` keeps digit runs, for the year tokens of `time_preps`. A token
  that the raw text wraps in brackets — `(a)`, `(d)` in the Supreme Court
  opinion — is a list marker and is not a word; `an` skips it.
- **One preset menu per mode**, `xxPreset`, every option pinned; a
  redraw-only `xxShow`/`xxSource`/`xxRule` never rewrites another control.
  Lessons that share a mode select their shipped preset through a cfg key
  named in the mode spec (`rule`, `list`, `rules`, `source`, `focus`) and may
  restrict the menu through `rules`; a restricted menu still pins every
  option it shows.
- **Tiles** are `<strong id>` in a `kpi-grid`, written with `textContent`.
  Formats: a count `N of M`; a share `share1` (one decimal and `%`); the
  table lab's `vbPct2` stays where it is used today and is not used in new
  modes. `—` is the em dash. A list tile is comma-separated in list order.
- **Every row is printed.** Every mode prints the rows it counted with the
  verdict beside each, in a scrolling table (`max-height` 18–24 rem), and the
  text it scanned where there is one. A mode that counts over a word list
  offers `xxShow`: misses / all / set aside (the list's exclusions with
  reasons).
- **One limit sentence.** Each mode writes one sentence under its tiles
  (`id="xxLimit"`) saying what it read and what it cannot tell: "spellings,
  not meanings", "the dictionary's first pronunciation", "1813 prose".
- **Refusals** are printed, specific and never silent: a typed verb that is
  not one word; a typed word CMUdict does not carry ("the page cannot hear a
  word it does not carry"); a pasted text under fifty words. The hostile
  sweep (`''`, `banana`, `0`, `-1`, `1/0`, `A>B`) must leave every tile `—`
  or a message, never an exception.
- **Reproduction under node.** `scripts/wordlists/verbrules_check.js`
  reproduces the forming rules' figures by evaluating `ENGLISH_VERB_JS`. Every
  new rule function lives in an `english_core.py` string so that a sibling
  harness, `scripts/wordlists/english_check.js`, can load the shipped code and
  print every figure a preset pins. The kit engineer breaks one rule on
  purpose and sees the harness disagree before trusting it.

### D.1 The data pipeline

Nothing that took measurement lives where `rm -rf` can reach. Every new data
file is written by a committed script with a `--check` mode, as
`clean_verbs.py` is, and records its sources (name, licence, URL, sha256 of
the file as fetched) in its `note`. The build never runs these scripts; the
files they write are committed.

| script (`scripts/wordlists/`) | reads | writes | size, gzipped (m) |
| --- | --- | --- | --- |
| `clean_nouns.py` | `ngsl.tsv`, Moby POS, `/usr/share/dict/american-english` | `plural_nouns.json` — every NGSL headword Moby tags as a noun, with the dictionary-confirmed plural forms the NGSL records; a hand list of irregular plurals (`men, women, children, feet, teeth, mice, geese, oxen, lice, dice, pence, people` and the `-men` compounds) that OVERRIDES a dictionary-confirmed regular form (`mans`, `foots`, `mouses` are verb forms or rarities); a stoplist of the function words Moby mis-tags (`and, as, at, for, of, nor, per, he, she, i, you, who, few, many, none, six…`), each set aside with its reason; `noplural` for the noun-only headwords with nothing confirmed (99 before the stoplist (m)) | ≈ 12 KB |
| `clean_adjectives.py` | the same | `ly_adjectives.json` — the 153 adjective-only headwords with every confirmed `-ly` spelling, and the 27 with none | ≈ 2 KB |
| `sounds.py` | CMUdict (first pronunciation unless the rule says otherwise), `verbrules_cases.json`, `plural_nouns.json`, `ngsl.tsv`, Moby POS, the printed texts | `verb_sounds.json` (base, final-sound class, `-ed` sound, `-s` sound; the noun plurals likewise; skipped words listed); `letters.json` (one row set per rule in D.3 `letters`); `stress.json` (word, parts, index of the strong part, class N/V/A, last-primary index, weak-vowel counts); `passage_sounds.json` (first- and last-sound class and phoneme for every word of the 936-word passage); `an_sounds.json` (first-sound class for every word that follows *a*/*an* in the printed texts) | 4 KB; 6 KB; 5–10 KB; 2 KB; 1 KB |
| `en_passage.py` | the novel as `en_sources.novel()` gives it (captions removed) | `content/english/data/wordorder_passage.json` — the printed passage, from *very ungracious sensation* to the *Mr.* after *nothing else to do.*, with the chapter heading (*CHAPTER LIII.*) cut out too, so every printed word is Austen's; 936 words as the page counts them; `--check` exits 1 if stale | (m) |
| `concordance.py` | the novel (sliced on its first and last sentence, illustration captions removed), the play (the three acts), the two modern documents | `content/english/data/long_passage.json` (Chapter XXVI: from "Mrs. Gardiner's caution to Elizabeth was punctually and kindly given" to "as well as the plain."), with the verb-form lists restricted to its words; `wilde_excerpt.json` (the 1,975-word run of Act II from "CECILY. Oh, I merely came back to water the roses." to "if I may speak candidly—", at speech boundaries); `wilde_questions.json` (167 lines); `question_concordance.json` re-cut; `an_concordance.json`; `superlative_concordance.json` (`-est`, `most` + adjective, `same`, `next`); `time_concordance.json`; `compare_concordance.json`; `phrasal_concordance.json` | 5.7; 4.7; 2.5; ≈3; ≈11; ≈9; ≈2; ≈8; ≈7 KB |

Each JSON's `note` names the text, the edition, the slice, and the licence,
as `wordorder_passage.json` does. `scripts/wordlists/CMUDICT_LICENSE` is
added (BSD-2 requires the notice to travel with derived data) and cited from
every page that uses a CMUdict-derived file.

### D.2 The thirteen new modes

Each entry: purpose; cfg; controls; the exact computation; tiles; presets;
refusals; data; which lessons it serves. Expected strings are read with
`--observe`; the figures in §C are the design's and are re-read.

#### endings
- Purpose: the sound of `-ed` and `-s` from the last sound of the base.
- cfg: `mode`, `rule` (`ed` | `s` | `plural`; the shipped preset), `panel_title`, `panel_intro`.
- Controls: `enPreset` (preset menu: `ed`, `s`, `plural`); `enShow` (redraw-only: misses | all | skipped); `enWord` (text: a word from the list; refuses one not on it with "not on the printed list: the page cannot hear it").
- Computation: class of the base's last sound from `verb_sounds.json` — `td` (/t/ or /d/), `voiceless` (/p k f θ s ʃ tʃ/), `sibilant` (/s z ʃ ʒ tʃ dʒ/), `voiced` (everything else, vowels included). `edSound(cls)`: `td → id`, `voiceless → t`, else `d`. `sSound(cls)`: `sibilant → iz`, `voiceless → s`, else `z`. A hit is the rule's sound equal to the recorded sound of the form's first CMUdict pronunciation. Words with no pronunciation are skipped and counted in `enSkipped`.
- Tiles: `enRule` (the rule in words); `enHit` (`1111 of 1118`); `enPct`; `enMiss` (count); `enFirst` (the missed words); `enSkipped`; `enWordSays` (for the typed word: class, rule, dictionary).
- Data: `scripts/wordlists/verb_sounds.json`.
- Serves: 1.4.

#### wordrule
- Purpose: a spelling rule scored on a word list against dictionary-confirmed forms (plurals; `-ly`). The `table` lab's scoring half, generalised.
- cfg: `list` (`plurals` | `ly`), `rule` (shipped preset id), `show` (`misses` | `all` | `noplural`/`none` | `excluded`).
- Controls: `wrPreset` (plurals: `r0`, `r1`, `r2`, `r3`; ly: `plain`, `changes`); `wrShow` (redraw-only).
- Computation: `plR0(w)`: `-es` after `s, sh, ch, x, z`; consonant + `y → ies`; else `+s`. `plR1`: `plR0` plus consonant + `o → oes`. `plR2`: `plR1` plus `f/fe → ves` (any `f`). `plR3`: `plR1` plus `ves` only for `-lf, -ife, -eaf, -olf`. A hit is the rule's form among the row's confirmed plurals (irregular override applied by the data script). `lyPlain(w) = w + "ly"`; `lyChanges(w)`: `-ic → -ically` (except *public*), `-ll → -lly`, consonant + `le → ly`, `-ue → -uly`, consonant + `y → ily`, else `+ly`; a hit is the rule's spelling among the confirmed adverb spellings; rows with no confirmed adverb are counted in `wrNone` and listed, not scored.
- Tiles: `wrRule`; `wrHit`; `wrPct`; `wrMiss`; `wrFirst`; `wrNone` (plurals: nouns with no plural; ly: adjectives with no adverb); `wrNoneOf` (`99 of 738`).
- Data: `plural_nouns.json`, `ly_adjectives.json`.
- Serves: 4.1, 4.2, 6.3.

#### an
- Purpose: *a* against *an* by the next letter and by the next sound.
- cfg: `rule` (`letter` | `sound`), `source` (`all` | `wilde` | `modern` | `passage`).
- Controls: `anPreset`; `anSource` (redraw-only).
- Computation: for every *a*/*an* in the chosen text(s), the next word; `letter`: *an* iff its first letter is `a e i o u`; `sound`: *an* iff `an_sounds.json` marks its first phoneme a vowel. A next word CMUdict lacks is listed and not scored. Bracketed single letters are skipped (D.0).
- Tiles: `anRule`; `anN` (lines scored); `anHit`; `anPct`; `anMiss`; `anFirst`; `anUnknown` (next words not in CMUdict).
- Data: `an_concordance.json`, `an_sounds.json`.
- Serves: 4.3.

#### the_super
- Purpose: what stands before a superlative, *same*, *next*, *most* + adjective.
- cfg: `rule` (`est` | `same` | `next` | `most`).
- Controls: `tsPreset`.
- Computation: for each line, the word before the target: `the`; a possessive (`my your his her its our their` or a word ending `'s`); `a`/`an`; `at`/`very`; other. The rule holds on `the` or a possessive. Targets: `-est` tokens whose stem (with `-e`, `-y`, undoubling restored) is a Moby adjective in the NGSL; `most` directly before a Moby adjective; `same`; `next`.
- Tiles: `tsN`; `tsHit`; `tsPct`; `tsThe`; `tsPoss`; `tsA`; `tsOther`.
- Data: `superlative_concordance.json`.
- Serves: 4.4.

#### auxchain
- Purpose: six rules about helping verbs on one printed chapter and the modern documents.
- cfg: `rule` (`agree` | `modal` | `have` | `be` | `not` | `boxes`), `source` (`chapter` | `modern`; shipped `chapter`).
- Controls: `axPreset` (the six rules); `axSource` (redraw-only); `axShow` (redraw-only: residue | all).
- Word classes (from `long_passage.json`, built offline for the chapter's own words): `base`, `third` (the `-s` forms plus *is has does says goes*), `past`, `pp`, `ing`, `adj` (Moby adjective-only words in the chapter); closed sets in JS: `MODAL` (*can could may might must shall should will would*), `BE`, `HAVE`, `DO`, `SUBJ` (*I you he she it we they*), `OBJ`, `DET` (articles, possessives, quantifiers, demonstratives), `PREP`, `ADV` (the frequency and degree adverbs the Word Order course lists plus *not*). A skipping step moves past *not* and adverbs, at most two words.
- Computation per rule:
  - `agree`: each `SUBJ` token and its next token. Third-person forms = `third` ∪ {*is has does was*}; plural forms = {*are were have do*}; *am*. Scored pairs are those whose verb is one of these or a `base` form; a hit is third-person form after *he/she/it*, plural form or base after *you/we/they*, *am/was* or base after *I*. `axHit`, `axPct`, `axBroken` (pairs against the rule, listed), `axPairs`.
  - `modal`: each `MODAL` token; next token directly `base`/`BE`/`HAVE`/`DO` → hit; *not* or an adverb then one of those → hit (counted apart in `axBetween`); a `SUBJ` next → `axQ`; a `third`/`past`/`ing` form → `axFormed`; else `axOther`. `axHit` = direct + between.
  - `have`: each `HAVE` token; after skipping: `pp` or *been* → `axPerf`; *to* → `axTo`; `DET`/noun-like/`OBJ` → `axMain`; `SUBJ` → `axQ`; else `axOther`. `axPct` = `axPerf` / all.
  - `be`: each `BE` token; after skipping: `ing` → `axIng`; `pp` → `axPP`; `adj` → `axAdj`; `DET`/noun → `axNP`; `PREP` → `axPrep`; `SUBJ` → `axQ`; else `axOther`. `axIngPct` = `axIng` / all.
  - `not`: each *not* and each *n't* token; the word before: `MODAL`/`BE`/`HAVE`/`DO` → hit; a verb form → `axOld`; `SUBJ`/`OBJ` → `axQ`; a joining word (*or and but if whether than as that though*) → `axJoin`; else `axOther`; `axNt` counts the contractions apart. `axHit`, `axPct`.
  - `boxes`: each `SUBJ` token; collect the chain of `MODAL`/`HAVE`/`BE`/`DO` tokens (skipping *not* and adverbs, at most five words) and the main word after; classify exactly as `measure/m_corpus.py` `classify_chain` does: present simple, past simple, future/modal simple, present/past perfect, present/past progressive, perfect progressive, modal perfect, modal progressive, passive (`be` + `pp`), perfect passive, `be` as main verb, `have` as main verb, present/past simple with *do*, no verb found, other. `axSimple` (present + past simple, with and without *do*), `axProg` (all progressives), `axPerf` (all perfects), `axModal`, `axPassive`, `axNone`, `axN`.
- Tiles: as listed; every rule also writes `axN` and the limit sentence.
- Data: `long_passage.json`; `MODERN_DATA` as the word-order modes use it.
- Serves: 3.1–3.6.

#### questions (extension of the existing mode)
- cfg gains `source` (`austen` | `wilde`). Verdicts gain: `a wh-word with no helping verb after it` (tile `quWh`), `a word of address first` (`quAddr`: *oh, well, pray, my dear*, or a capitalised word from the play's cast list followed by a comma), `no verb at all` (`quFrag`: no token in `AUX` ∪ the verb lists), `a pronoun first` (`quStmt`). `quOther` is what remains. The Austen data is re-cut (D.1).
- Data: `question_concordance.json` (re-cut), `wilde_questions.json`.
- Serves: 5.3, 5.4.

#### time_preps
- Purpose: *in/on/at* before a time word.
- cfg: `source` (`all` | `austen` | `wilde` | `modern`).
- Controls: `tpPreset` (= source).
- Computation: each line has a preposition (*in on at*), up to two words, and a time word; kinds: `day` (the seven), `month` (eleven; *may* excluded as ambiguous and the lesson says so), `year` (a four-digit token 1500–2099), `season`, `part` (*morning afternoon evening*), `point` (*night noon midnight*), `festival` (*Christmas Easter Michaelmas*), `clock` (a number word or *half* before *o'clock*, or *o'clock*). Rule: `day → on`; `month, year, season → in`; `part → in`, unless the words between name a particular day (a day name, *following*, *very*, *third*, *next*, *same*, *that*) → `on`; `point, festival, clock → at`.
- Tiles: `tpN`; `tpHit`; `tpPct`; `tpMiss`; `tpFirst`; a by-kind table.
- Data: `time_concordance.json` (lines extracted with `tokensOf`, so years survive).
- Serves: 6.1.

#### compare
- Purpose: `-er/-est` against `more/most` by the adjective's parts.
- cfg: `source` (`austen` | `wilde` | `modern`), `rule` (`A` | `B`; shipped `A`).
- Controls: `cpPreset` (= source); `cpRule` (redraw-only).
- Computation: each line carries the token, the adjective, its parts (CMUdict), and the form used (`inflect` | `more`). Rule A predicts `inflect` for one part, or two parts ending `-y`; else `more`. Rule B adds two parts ending `-ow, -le, -er`. A hit is prediction = form used. Tokens whose stem is not a Moby adjective in the NGSL were excluded by the data script and are listed under `cpShow = set aside`.
- Tiles: `cpN`; `cpHit`; `cpPct`; `cpMiss`; `cpFirst`; `cpBySyll` (a small table: parts × form used).
- Data: `compare_concordance.json`.
- Serves: 6.2.

#### phrasal
- Purpose: which phrasal verbs a text uses, and where the pronoun goes.
- cfg: `rule` (`pronoun` | `freq`), `source` (`austen` | `wilde`; shipped `austen`).
- Controls: `phPreset`; `phSource` (redraw-only).
- Computation: lines are a verb form from the printed verb list followed, directly or with one object pronoun between, by a particle (*up out off down away back over*). `freq`: count per (verb, particle), ranked; `phTop` lists the first five with counts. `pronoun`: lines with an object pronoun (*me him us them it you*; never *her*, which is also possessive) directly after the verb and the particle after it → `phBetween`; lines with the particle then a pronoun → `phAfter`; `phPct` = between / (between + after). A table of `verb + preposition + pronoun` lines (*look at him*) from the same text is printed under `phSource` as the contrast, with its count `phPrep`.
- Tiles: `phN`; `phTop`; `phBetween`; `phAfter`; `phPct`; `phPrep`.
- Data: `phrasal_concordance.json`.
- Serves: 6.4.

#### letters
- Purpose: a spelling-to-sound rule scored on the 2,800 words.
- cfg: `rules` (the preset ids the page shows; the first is shipped).
- Controls: `ltPreset`; `ltShow` (redraw-only: misses | all | set aside).
- Computation (each row set built by `sounds.py`; the page runs the rule and compares with the dictionary's fact):
  - `softc`: headwords with exactly one `c`, not in `ch ck sc cc cq qu`, containing none of `s k q x z`, whose first pronunciation has /s/ or /k/ but not both; rule: /s/ iff the letter after `c` is `e i y`. `softg`: likewise one `g`, not in `gh ng dg gg gu`, no `j`, with /dʒ/ or /g/ but not both.
  - `magic`: one-part headwords matching consonant-vowel-consonant-`e` with the consonant not `w x y r`; rule: the vowel is its name (/eɪ iː aɪ oʊ uː/, with /juː/ for `u`). `magic_r`: the same with `r`, scored apart.
  - `ie`: every `ie`/`ei` in a headword; rule: `ei` after `c`, else `ie`. `ie_ee`: the same, only where the word's vowel at that spot is /iː/ (k for the alignment the kit uses; the design counted words containing /iː/ anywhere).
  - `gh`: headwords with a vowel letter then `gh`; rule: no /g/. `kn_wr_mb`: `kn-` (no /k/), `wr-` (no /w/), `-mb` (no /b/), `-mn` (no /n/), `-lk`/`-lm` (no /l/). `h`: headwords beginning `h` + vowel; rule: /h/ is said; residue the three. `ough`: no rule; the tile `ltSounds` counts distinct pronunciations (5 of 10 words) and the table prints them.
  - `tion`: /ʃən/; `sion`: /ʒən/ after a vowel letter, /ʃən/ after a consonant; `ture`: /tʃə/; `cial`: `-cial`/`-tial` as /ʃəl/.
- Tiles: `ltRule`; `ltN`; `ltHit`; `ltPct`; `ltMiss`; `ltFirst`; `ltSounds` (ough only).
- Data: `letters.json`.
- Serves: 7.1–7.5.

#### stress
- Purpose: where the strong part falls, by class and by ending.
- cfg: `rules` (preset ids shown; first shipped).
- Controls: `stPreset`; `stShow`.
- Computation: `nouns2`/`verbs2`/`adj2`: two-part headwords whose Moby tags are noun-only / verb-only / adjective-only; rule: strong part first / second / first. `pairs`: two-part headwords tagged both noun and verb with two CMUdict pronunciations stressed on different parts; `stCount` and the list. `tion ic ical ity ate ize ee`: headwords with the ending (and ≥ the parts the rule needs; `ate` only Moby verbs); rule: the strong part is 2 / 2 / 3 / 3 / 3 / 3 from the end, or the last for `ee`; for `ee` the kit reads the LAST primary stress. `ly ness ment er ful able`: pairs (stem, stem + ending) both in the NGSL and CMUdict, with `-e`/`-y` restored; rule: same strong-part index. `schwa`: over every weak part of every headword of two or more parts: `stSchwa` (/ə/), `stEr` (/ɚ/), `stIh` (/ɪ/), `stIy` (/iː/), `stPct` = `stSchwa` / all.
- Tiles: `stRule`; `stN`; `stHit`; `stPct`; `stMiss`; `stFirst`; `stCount`; `stSchwa`, `stEr`, `stIh`, `stIy`.
- Data: `stress.json`.
- Serves: 8.1–8.4.

#### contractions
- Purpose: how much of *not* is *n't*, and the full form behind each contraction.
- cfg: `source` (`wilde` | `austen` | `modern`).
- Controls: `coPreset` (= source).
- Computation: tokens ending `n't` (`coNt`) against tokens *not* (`coNot`); `coPct` = n't / (n't + not); every token with `'s 'll 'm 're 've 'd 't` counted by type (`coTypes`, a list with counts) and per 1,000 words (`coK`); the table prints each contraction with the full form the rule gives (`'s`: "is, has, or belonging"; `'d`: "would or had"), so the reader sorts the ambiguous ones.
- Tiles: `coNt`; `coNot`; `coPct`; `coK`; `coTypes`.
- Data: `wilde_excerpt.json`; `wordorder_passage.json`; `MODERN_DATA`.
- Serves: 9.3.

#### linking
- Purpose: what meets at a word boundary.
- cfg: `rule` (`cv` | `vv` | `same`).
- Controls: `lkPreset`.
- Computation: over the 936-word passage, every pair of words with only a space between (418); from `passage_sounds.json` the last sound class of the first and the first sound class of the second; `cv`: consonant then vowel; `vv`: vowel then vowel; `same`: the same consonant phoneme on both sides. Boundaries with a word CMUdict lacks are counted in `lkUnknown` and not scored. The passage is printed with the chosen boundaries marked (`‿`).
- Tiles: `lkN` (`408 of 418 scored`); `lkCount`; `lkPct`; `lkUnknown`.
- Data: `passage_sounds.json`, `wordorder_passage.json`.
- Serves: 9.4.

#### coverage
- Purpose: how much of a text the 2,800 headwords cover, by band, by rank, by flemma and by family.
- cfg: `text` (`passage` | `wilde` | `modern` | `own`), `show` (`bands` | `top` | `family`).
- Controls: `cvPreset` (= text); `cvOwn` (textarea, shown for `own`); `cvShow` (redraw-only).
- Computation: tokens lowercased, a trailing `'s` stripped, digits and single letters dropped. A token is known at band b if it is a headword of band ≤ b, or reduces to one by the Subject's rules run backwards: `-s/-es/-ies` (verb or plural), `-ed/-ied/-d` with undoubling, `-ing` with `e` restored and undoubling, `-er/-est/-ier/-iest`, `-ly` with the four changes undone, `n't → not`, the irregular verbs' past and participle forms, the irregular plurals, and `better, worse, best, worst`. Capitalised tokens not at a sentence start are `cvNames`. `cvFam` adds tokens that reduce to a headword by stripping one derivational affix (`un- re- dis- in- im- mis- non- over- under- pre-`; `-ly -ness -ment -tion -sion -er -or -ful -less -able -ible -ity -ous -ive -al -ish -ist -ism -ance -ence -ure -age`). `top`: tokens ranked by count; `cvTop10/50/100` cumulative shares. The unknown tokens are printed as a list.
- Tiles: `cvN`; `cvB1`; `cvB2`; `cvB3`; `cvNames`; `cvFam`; `cvOff` (unknown count); `cvTop10`; `cvTop50`; `cvTop100`; `cvDistinct`.
- Refusals: fewer than 50 words in `cvOwn` → every tile `—` and "type at least fifty words".
- Data: the headword-and-band list (9.3 KB gzipped), `irregular_verbs.json`, the irregular plural list; the texts.
- Reproduction: the kit engineer runs the same reduction offline against the full forms list and records in the lesson how many of the 10,296 recorded forms the rules recover (k).
- Serves: 10.1–10.3.

### D.3 Extensions to existing modes

- `table`: cfg `focus` (`build` default | `score`) reorders the two halves of the markup; no new tile.
- `irrshare`: tile `shTop` — the share of the counted irregular forms covered by the twenty commonest verbs on the passage, under the menu's choice (k); pinned on both presets.
- `listening`: tile `lsFinal` — tokens of listed words followed by `. , ; : ? !` in the passage text (k); pinned on the `weak` preset.
- `svo`, `adverbs`, `questions`, `irrshare`, `listening`: the tokeniser fix in D.0 — every pinned figure re-read.

### D.4 Reusing what exists

`SCAN_JS` (`wordsOf`, `lower`, `setOf`, `share1`, `commas`), `MODERN_DATA` and
`MODERN_JS` (the two modern documents, printed and counted) are reused by
every concordance mode. `ENGLISH_VERB_JS` (`vbThird`, `vbIng`, `vbEd`,
`vbDoubles`, `vbPct2`) is reused by `coverage` for its reductions and by
`auxchain` to build form lists at build time. No mode from another kit fits:
the English kit counts words, and the library's other kits count numbers.

---

## §E Listen

`speech.islands` (`scripts/mathpath/speech.py`) treats a run containing any of
`əðʃʒŋɪʊæɑɒɔɜʌːˈˌ` as a sound island and a stress pattern such as `s.S.` as a
mark island; each needs a spoken form in `content/spoken/english.py` or
`tests/test_speech.py` fails. The rules:

- **Write sounds as IPA letters inside `<dfn>` or in key and worked lines**,
  never as CMUdict symbols (`AH0`, `SH`) — those are build-time data and no
  reader learns them. Every sound this plan needs is in the island set except
  /dʒ/, /tʃ/ and /θ/ (`θ` is also a math symbol and is deliberately excluded):
  write "the sound at the start of *judge*", "the sound at the start of
  *church*", "the sound at the start of *think*" in prose instead.
- **Slashes read as "over".** `/t/ /d/ /ɪd/` in a key line is spoken "t over
  d over ɪd" unless the line has a spoken form. Every key or worked line that
  carries a sound gets one, listed in the lesson's module docstring for the
  orchestrator. Prose avoids slashes around sounds and says "said as *t*".
- **Hyphen-initial endings** (`-ed`, `-tion`) read as "negative" without a
  form; the existing file shows the pattern (`'-s 99.92% …'`).
- **Spoken forms this plan needs** (exact run text is the author's; the
  words to say are these): `ə` → "uh"; `ɪ` → "ih"; `ɪd` → "id"; `ɪz` → "iz";
  `ʃ` → "sh"; `ʒ` → "zh"; `ʃən` → "shun"; `ʃəl` → "shul"; `tʃə` → "chur";
  `ʒən` → "zhun"; `ð` → "th, as in the"; `ŋ` → "ng"; `ɜː` → "er"; `iː` →
  "ee"; `eɪ` → "ay"; `aɪ` → "eye"; `oʊ` → "oh"; `uː` → "oo"; `juː` → "you".
  Key lines such as `-ed   /t/  /d/  /ɪd/` → "the ed ending: t, d, or id";
  `walk → walked  /t/` → "walk becomes walked, said with a t". Stress
  patterns (`S.`, `.S`, `s.S.`) already have forms; new ones (`S..`, `..S.`)
  need theirs.
- **One reading per run, library-wide**: a run already given a form in
  `content/spoken/english.py` keeps it; `test_one_reading_per_run` fails on a
  second reading, and `test_no_spoken_form_for_math_that_is_gone` fails on a
  form whose run no longer exists — so when a lesson is rewritten, its old
  runs' forms are removed.
- **`speechcheck.py` finds nothing in English** (its detector looks for math
  shapes), so authors read every key and worked line aloud in their head and
  list the ones that need a form. The reviewer checks the list against the
  built page's `data-say`.

---

## §F Package layout, the author's checklist, the voice

```
content/english/
  __init__.py                      PATH; COURSES = [... if c is not None]; the numbering loop
  c1_tense_tables/  part_a.py (1–2)  part_b.py (3–4)         existing package, two new lessons
  c2_irregular_verbs/  part_a.py  part_b.py  part_c.py       existing, lesson 3 touched
  c5_helping_verbs/  __init__.py  part_a.py (1–3)  part_b.py (4–6)
  c6_nouns_articles/  __init__.py  part_a.py (1–2)  part_b.py (3–4)
  c3_word_order/  part_a.py  part_b.py  part_c.py (3–4)      existing, lesson 4 new
  c7_small_words/  __init__.py  part_a.py (1–2)  part_b.py (3–4)
  c8_spelling_sound/  __init__.py  part_a.py (1–3)  part_b.py (4–5)
  c9_word_stress/  __init__.py  part_a.py (1–2)  part_b.py (3–4)
  c4_listening/  part_a.py  part_b.py (2–4)                   existing, two new lessons
  c10_vocabulary/  __init__.py  part_a.py (1–3)
  data/  long_passage.json  wilde_excerpt.json  wilde_questions.json
         an_concordance.json  superlative_concordance.json  time_concordance.json
         compare_concordance.json  phrasal_concordance.json  question_concordance.json (re-cut)
content/spoken/english.py         SPOKEN = {run: words}
scripts/wordlists/  clean_nouns.py  clean_adjectives.py  sounds.py  concordance.py  english_check.js
                    plural_nouns.json  ly_adjectives.json  verb_sounds.json  letters.json
                    stress.json  passage_sounds.json  an_sounds.json  CMUDICT_LICENSE
```

Mirror `content/philosophy/__init__.py` for the package `__init__` and
`content/english/c1_tense_tables/__init__.py` for a course `__init__`; a course
not yet written exports `COURSE = None`. **Course fields**: as the four
existing courses carry them — `slug`, `number` (set by the loop; do not write
it), `title`, `level`, `blurb`, `summary`, `assumes_short`, `assumes_long`,
`how_to` (3), `outcomes_intro`, `outcomes` (6 pairs), `syllabus_intro`,
`not_covered` (3–4, from §G), `key` (4–8 lines ≤ 46 chars), `footer_lead`
(names every text and data source the course's labs use, with licences),
`lessons`.

**Lesson fields and their enforced shapes** are exactly those of
`docs/philosophy/PLAN.md` §E (`concepts` exactly 3, `mistakes` exactly 3,
`steps` 4–5, `quiz` 3–4 with four distinct choices and one defensible answer,
`key` 3–8 lines ≤ 46 chars, `body` 7–18 blocks, `worked.lines` ≤ 60 chars,
escaped fields plain). The existing English lessons are the models; copy
their shape, not Philosophy's.

**The band.** Every page is written inside the NGSL 2,800 plus at most twenty
`<dfn>` terms, at 98% or better (`scripts/bandcheck.py`). The author runs
`scripts/preview_subject.py english --course <slug>` and then
`scripts/bandcheck.py <preview-dir>/<course>/<lesson>/index.html --report`
before handing a lesson over; a page below 98% is not finished. Terms this
plan knows will need `<dfn>`: *voiced*, *voiceless*, *participle* (already
defined in Irregular Verbs; define again where used), *helping verb*,
*modal*, *particle*, *preposition*, *possessive*, *superlative*, *part* (for
syllable), *concordance* (if used; prefer "the printed lines"), *flemma*,
*family*, *contraction*, *vowel*, *consonant* (both defined on the doubling
page; define again). Words outside the band that no `<dfn>` should carry:
*syllable*, *phoneme*, *auxiliary*, *inflection*, *suffix*, *lexeme* — write
*part*, *sound*, *helping verb*, *ending*, *ending*, *word*. Proper names and
the sounds themselves are not counted against the page.

**Per-lesson procedure.**

1. Write the dict from the §C entry; the §C misconception is `mistakes[0]`.
2. Leave every figure as `(k)` text until the kit's preset is pinned; then
   read the figures with `--observe` and write exactly what the page prints,
   with "counted on this page" or "quoted" beside each as the existing
   lessons do.
3. `scripts/preview_subject.py english --course <slug>`; fix any lab, shape
   or read-out failure it reports.
4. `scripts/bandcheck.py` on the preview pages, `--report`.
5. Try to argue for every quiz distractor; rewrite any you can.
6. Read every key and worked line aloud in your head; list the runs that
   need a spoken form in the module docstring.
7. Hand over with the list of figures stated and where each comes from.

**The voice.** The library's: careful prose by someone who has counted and is
telling you what they found. The English Subject adds:

- Say what was counted, on which printed text, in the sentence that gives the
  number. "On the 455 lines from the play, the letter rule is right 448
  times" — never "the letter rule is 98.5% accurate".
- A quoted figure is introduced as quoted every time it appears: "counted
  once over the whole novel, which no page can carry, and quoted here".
- The residue is content. Every miss list is sorted into kinds and each kind
  gets a reason the reader can use; "exceptions" alone is a defect.
- The text's age is said where it changes an answer: "1813 English put *not*
  after the verb; the chapter shows how often".
- Name the act: choose, say, read off, sort, mark. Never "understand".
- Short sentences, concrete words, no filler, no exclamation marks, no
  "In this lesson". British or American spelling, consistent within a course;
  the existing courses are British.
- Grammar words are kept to the glossary budget: *helping verb* not
  *auxiliary*, *the small word in front* where the first course says it,
  *strong part* for stress, *part* for syllable, *the flat vowel* for schwa.

One exemplary paragraph (a `p` block for “A or An: by Sound, Not by Letter”):

> The rule you were taught is about letters, and letters are the wrong thing
> to look at. On the 455 lines from the play printed under the lab, *an*
> before a vowel letter is right 448 times. Three lines break it, and all
> three break it the same way: *a University*, *a utilitarian*, *an hour*.
> The first two begin with a vowel letter said as a consonant, the last with a
> consonant letter that is not said at all. Change the rule to the first
> SOUND of the next word and it is right 455 times. Nothing about the lines
> changed; the question did.

---

## §G What is left out, and why

Stated once so every course's `not_covered` can draw on it and no author
builds a decorative lab to fill a gap. Each exclusion carries the number that
refused it where a number was taken.

- **Tense choice, article choice by meaning, countability by sense.** When to
  use the present perfect, whether a noun's first mention takes *a*, whether
  *time* is countable in this sentence. Not computable from printed words; the
  input would be a human annotation (`docs/ENGLISH-SUBJECT.md` §1). The
  Helping Verbs course shows which boxes are used; it never says which to use.
- **Question tags.** A real B1 item. The novel has 7, the play 19 (m): 26
  tags in 143,000 words, half of them in a form nobody now uses (*is it
  not?*). A lab over 26 lines is a list, not a measurement. Admitted when a
  second public-domain play lifts the count past about 80.
- **Adjective position.** The design scan put 58.3% of the novel's
  adjective-only tokens directly before a noun and 17.3% after a linking word
  (m), and could not classify the rest without a parser; the residue would
  have measured the tool. The rule is also near-exceptionless in English and
  teaches little by a count.
- **Much and many, few and little.** The pairing is real and the design count
  was too noisy to state (Moby tags *pretty* a noun); admitted when the
  plurals data and an adjective list let the scan skip to the noun honestly.
  Until then it is a sentence in “Nouns With No Plural”.
- **Prepositions of place.** *At Netherfield*, *in Hertfordshire*, *in
  London*: the rule needs the place classified (a house, a county, a town),
  which is annotation.
- **Conditionals, reported speech, relative clauses.** Each pairs a form in
  one clause with a form in another and needs a clause splitter the kit does
  not have; *who* against *which* needs animacy, which is meaning.
- **Verbs with two pasts** (*learnt/learned*, *burnt/burned*). Unmeasured;
  the list is short and a dictionary confirms both spellings of most, so a
  rule would have nothing to score. A sentence in Irregular Verbs.
- **Idiom, collocation, politeness, register; audio; spaced repetition;
  adjective order; literary English** — refused in `docs/ENGLISH-SUBJECT.md`
  §2 and still refused.
- **Accents.** The weak forms are southern British, the stress and sound
  facts are CMUdict's American. Each lesson that depends on one says so; no
  lesson measures the difference.
- **The 's that is a possessive against the 's that is *is*.** The
  contractions lesson prints every *'s* and lets the reader sort it; a rule
  would need the next word's class and a judgement about meaning.
- **The alignment of letters to sounds in general.** The `letters` mode
  scores only words where the letter in question is the only possible source
  of the sound, and says how many words that set aside. A general
  letter-to-phoneme alignment is a research tool, not a lesson.

---

## §H Wiring checklist for the orchestrator

Not an author's job; recorded so nobody asks. The numbers: 853 → 890 pages,
772 → 803 lessons, 68 → 74 courses, 721 → 758 generated pages, 85 → 98 lab
modes; English 4/10/15 → 10 courses, 41 lessons, 52 pages. Check ids for the
four existing courses change number: Word Order is `eng-course5-…`, Listening
`eng-course9-…`.

1. `content/english/__init__.py`: six imports; `COURSES` with the
   `COURSE = None` filter and the numbering loop in §B order; tagline,
   description, key, sequence_intro, why_order, footer_lead per §A. The
   `material` clause is unchanged. Register nothing in `build_paths.py`
   (English is already in `GENERATED_PATHS` and `"english"` already in
   `KITS_WITH_EXPECTATIONS` — so a new preset without `expect` fails the
   build immediately; the kit engineer pins before the first build of a page).
2. `tests/test_site_invariants.py`: `ENG_COURSE_1..10_HOME` / `_LESSONS`,
   `ENG_COURSES` in path order, `ENG_PATH_COURSE_COUNT = 10`,
   `REQUIRED_PAGES`; the hardcoded totals at lines ~1805 (853) and ~2434
   ("sixty-eight course homes and 772 lessons"); the tagline count test needs
   no change unless a count is written.
3. `scripts/smoke.py`: `ENG_COURSES` in path order (the ids are built from
   it); `ENG_PATH_PAGE_MARKERS` names the last course, now Vocabulary and
   Reading.
4. `release/contract.json`, `release/contract.example.json`,
   `release/contract.schema.json`: one check per new page (37) and renumbered
   ids for 14 existing ones; `minItems` 865 → 902; every id pinned by name
   under 72 characters; `scripts/validate_release_contract.py` green.
5. `.github/workflows/ci.yml` "Published URL space is complete": the
   backslash-continued list, no comment inside it, the `$pages/853` message
   → 890; `bash -n` the block. `Containerfile.release`: the English guard
   block extended to ten courses with the FATAL messages renumbered.
6. `tests/content_preservation.json`: `modules` entries for every `.py` in
   `content/english/` (fingerprints via `/usr/bin/python3` and the test
   module's `content_fingerprint`); `english_semantic_copy` REGENERATED from
   the rendered course homes — the current block is stale (it still says
   "1,356 verbs", "nine of them", "47.6%" and "Nothing here makes a sound").
7. Hardcoded totals: `tests/test_generation4.py:70` (772),
   `tests/test_responsive_ui.py:300` (772), `tests/test_generation5_catalog.py:37`
   (772), `tests/test_review_remediation.py:165` (853),
   `tests/test_course_ui.py:81` (68 / 772), `tests/test_canvas_contract.py:31`
   (853), `tests/test_public_copy.py:144,146,461` (853 / 772 / 68),
   `README.md` lines 5, 583, 598 (the English row), 944, 947; `AGENTS.md`
   §0 table row and lines 121, 129, 140, 530; the page-weight note
   re-measured with its snippet.
8. `site/index.html`: the English subject card's sentence covers ten
   courses; the search array gets one entry per course (ten) with lesson
   counts and descriptions as TEXT (no entities). `site/progress/index.html`
   and `site/oauth2/spa/callback/index.html`: re-run
   `scripts/build_auth_pages.py`.
9. `content/spoken/english.py`: the forms from every lesson's docstring;
   remove forms for runs the rewrites deleted; `tests/test_speech.py` green.
10. `scripts/wordlists/`: the four scripts, their JSON outputs, `CMUDICT_LICENSE`,
    `english_check.js`; `tests/test_english_kit.py` gains a `--check` test per
    script and asserts every new mode is used, pins, and is ES5.
11. `docs/ENGLISH-SUBJECT.md`: §4 gains Moby and the play with their licences;
    §5 gains one table per new course with the figures as read from the
    pages; the Scope section says ten courses and 41 lessons.
12. `docs/pedagogy/english-<course-slug>.md`: one review per course (six new,
    four updated) by the Fable reviewers, each reading every lesson of the
    course before changing any, as the four existing reviews did.
13. `node scripts/labcheck.js --generated`, `/usr/bin/python3 -m unittest
    discover -s tests`, `scripts/build_paths.py --check`, `scripts/bandcheck.py`
    (every English page ≥ 98%), `scripts/speechcheck.py`, and the page-weight
    snippet, all green before merge. `docs/english-v2/COURSES.json` and §C
    must agree (the fan-out manifest for authors).

---

## §I Data sources and licences

| source | what it supplies | licence | where |
| --- | --- | --- | --- |
| NGSL 1.2 (Browne, Culligan, Phillips) | headwords, bands, recorded forms | CC BY-SA 4.0 (derived lists carry it) | `scripts/wordlists/ngsl.tsv` |
| CMUdict (cmusphinx/cmudict, master) | final and first sounds, stress, parts | BSD-2; notice in `scripts/wordlists/CMUDICT_LICENSE` | derived JSON only |
| Moby Part-of-Speech (Gutenberg #3203) | which headwords are nouns, verbs, adjectives | public domain | build time only; nothing shipped |
| SCOWL wamerican 2020.12.07 | confirms a recorded form is a word | permissive (SCOWL); facts only | `/usr/share/dict/american-english`, sha pinned in `clean_verbs.py` |
| *Pride and Prejudice* (1813; Gutenberg #1342, 1894 edition — slice on the novel's first and last sentence, never on the Gutenberg markers) | the passage, Chapter XXVI, every Austen concordance | public domain | `content/english/data/` |
| *The Importance of Being Earnest* (1895; Gutenberg #844) | the excerpt, 256 questions, *a/an* lines, comparatives, phrasal verbs | public domain | `content/english/data/` |
| *Stanley v. City of Sanford* (2025); "U.S. Population Aging as Nation Turns 250" (2026) | the modern comparison, as today | U.S. government works | `content/english/data/` |
| Nation (2006), Laufer (1989), Cutler and Carter (1987), Pinker (1999) | thresholds and figures | quoted, never embedded | prose only |

The design measurements, their scripts and their raw outputs are in
`docs/english-v2/measure/`; its `README.md` gives the commands and the sha256
of every source as fetched.
