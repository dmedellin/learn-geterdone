# English for speakers of other languages — the design, and what measurement changed

Kept in the repository rather than a scratchpad, because the first copy of this
document lived in a shared scratch directory and was destroyed when two agents
rebuilt it. Nothing that took measurement to establish should live anywhere a
`rm -rf` can reach.

## 1. The test every lesson passes

`labs.build(key, cfg)` is unconditional in `scripts/mathpath/render.py`, so a
lesson without a lab does not render, and every path promises that each figure
is computed in the browser from the definition the lesson states.

For English the honest form of that promise is:

> **State a rule. Measure its hit rate on printed text. Show the residue.**

Grammar explanation survives as *the stated definition the lab tests*. The
residue — which rules to trust, where the exceptions live — is the part a learner
needs and never gets. A lesson that cannot be written this way does not ship.

The sharper test, which killed two earlier drafts of this Subject: **is the
lab's input a definition, or a human annotation?** Exact arithmetic over asserted
inputs gives an exact answer to the wrong question, and the lab is decorative
even when every widget is honest.

## 2. What was refused, and why

- **Literary English, stylometry, metre, rhyme.** Draft one. Useless to a
  learner, and six of its ten courses computed over stress marks and parse trees
  the author had supplied.
- **Idiom, pragmatics, politeness.** Not computable. They fail the way
  `docs/FUTURE-SUBJECTS.md` records biographies failing.
- **Collocation.** On a page-sized sample nearly every co-occurrence count is 0
  or 1, so the table must be quoted from a corpus the reader cannot see.
- **Spaced repetition.** Exact, computable, and *not English* — the identical lab
  would ship unchanged in a Spanish path. That is the tell.
- **Adjective order as 8! = 40,320.** Vacuous. Real noun phrases carry two
  adjectives, and the order is a gradient preference, not a slot grammar.
- **Audio.** No media budget, pages are self-contained. The Subject says which
  contrasts matter and sends the reader elsewhere to hear them.

## 3. The band contract

Every page is written inside the NGSL 2,809 plus at most twenty glossary terms
defined with `<dfn>` before first use, and `scripts/bandcheck.py` refuses the
build below **98%**. The first course teaches that 98% coverage is what a reader
needs; a page that teaches it and misses it has failed its own lesson.

Measured on the 52 published pages of the second version: every page between 98.3% and 100.0% (`python3 scripts/bandcheck.py --report`).

**Five tokeniser bugs were found in `bandcheck.py` by running it, and every one
made the number look WORSE than the truth** — the direction that passes for
rigour. Hyphenated number words counted as unknown vocabulary; `<title>` leaked
the site's own domain into the prose stream; affixes (`-ing`, `-ed`) counted as
unknown words when they are the lesson's own subject; element boundaries joined
with no separator, inventing `ideaswhat` and `libraryenglishevery`; possessives
double-counted.

## 4. Data sources and licences

Every byte the Subject ships is permissively licensed or a U.S. government
work. The table is the Subject's own copy of `docs/english-v2/PLAN.md` §I; where
the two ever differ, the plan's table and the files named in it win.

| source | what it supplies | licence | where it lives |
|---|---|---|---|
| NGSL 1.2 (Browne, Culligan and Phillips) | headwords, bands, recorded forms | **CC BY-SA 4.0**; lists derived from it carry the same licence | `scripts/wordlists/ngsl.tsv` |
| CMUdict (cmusphinx/cmudict) | first and last sounds, stress marks, parts | **BSD-2**; only facts are shipped, as derived JSON, and the notice ships with them | `scripts/wordlists/CMUDICT_LICENSE`, `b_CMUDICT_LICENSE` |
| Moby Part-of-Speech (Gutenberg #3203) | which headwords are nouns, verbs or adjectives | **public domain**, used at **build time only**; the list itself is not shipped | nothing shipped |
| SCOWL wamerican | confirms that a recorded form is a word | permissive; facts only | `/usr/share/dict/american-english`, sha pinned in `clean_verbs.py` |
| *Pride and Prejudice* (1813; Gutenberg #1342, 1894 edition) | the passage, Chapter XXVI, every Austen concordance | **public domain**; sliced on the novel's own first and last sentence, never on the Gutenberg markers (§6) | `content/english/data/` |
| *The Importance of Being Earnest* (1895; Gutenberg #844) | the excerpt, the 256 questions, the *a/an* lines, the comparatives and phrasal verbs | **public domain** | `content/english/data/` |
| *Stanley v. City of Sanford* (2025); "U.S. Population Aging as Nation Turns 250" (2026) | the modern comparison text | **U.S. government works** | `content/english/data/` |
| Nation (2006), Laufer (1989), Cutler and Carter (1987), Pinker (1999) | thresholds and figures | **quoted, never embedded** | prose only |

Nation's and Laufer's coverage thresholds are quoted as published figures, so
no non-commercial term rides on the Subject. Moby is the one source that is
used and not shipped: the noun, verb and adjective lists were cut with it when
the word lists were built, and each course home that relied on it says so.
CMUdict's notice has to travel with any file derived from it, which is why the
licence text sits beside the derived JSON.

Cost of the NGSL swap, and it is a teaching point rather than a defect: NGSL
counts **flemmas** (inflections only) where Nation counts **families**
(headword plus eighty-odd derivational affixes), so coverage figures land three
to six points lower. The lesson quotes by family, computes by flemma, and says
which (Vocabulary and Reading, *Word or Word Family*).

The design measurements, their scripts and their raw outputs are in
`docs/english-v2/measure/`; its `README.md` gives the commands and the sha256 of
every source as fetched.

## 5. The measurements the courses are built on

Every figure below was computed, and every one was recounted independently
before it was written into a lesson. The ten courses are in path order and are
named by title, because a course's number is its place on the path and not its
package prefix (`c3_word_order` is fifth, `c4_listening` ninth). The first two
courses and Word Order keep the prose they were measured in; the other seven
are tables with one row per lesson: the rule, the figure the page prints, and
the residue. Figures marked *quoted* are counted over a whole text that no page
can carry and are labelled so on the pages; every other figure is computed in
the browser on printed text.

### Tense Tables

| rule | hit rate | residue |
|---|---|---|
| `-s` | **99.92%** (1209/1210) | stomach |
| `-ing` | **99.34%** (1202/1210) | bus, format, initial, input, output, panic, traffic, up |
| `-ed` | **99.26%** (1201/1210) | bus, counsel, format, initial, input, output, panic, traffic, up |

Measured **in the browser** over the 1,210 regular verbs of the cleaned NGSL
list (`scripts/wordlists/verbrules_cases.json`, inlined on the page) against
that list's own recorded forms; the figures are pinned in the table lab's
`Score a rule on the list` menu and `scripts/wordlists/verbrules_check.js`
reproduces them with the same shipped code.

**The list was cleaned first, and the lesson says so.** The raw NGSL lemma
list (kept as `verbrules_raw.json`) was generated, and scored raw it counted
invented forms as hits: 61 irregular verbs scored as `-ed` hits on *comed*,
*maked*, *swimmed*; *offerring*, *sufferring*, *commiting*, *councilling*
recorded as spellings; nouns and adjectives (*able*, *son*, *council*) given
verb forms. `scripts/wordlists/clean_verbs.py` applies one test to every
spelling (in SCOWL wamerican, or the British spelling of a word that is) and
records every exclusion with its reason: 1,356 → 1,210, 146 left out (90
irregular, 54 whose recorded spelling for a slot the reference dictionary
does not confirm, *shelf* and *half* not verbs). Not all of the 54 are
misspelt: for *theme*, *resource*, *version* and a few others the recorded
forms are correct English that the dictionary simply lacks, and the page
says "not confirmed" rather than "wrong". The page prints the exclusions under `List`. The earlier residues
*shelf*, *bred*, *counselling*, *bused* were all artefacts of the raw list.

**A rule that was refuted, now computed on the page.** Before the `-o` fix
(every `-o` takes `-es`) the `-s` rule scores 1207/1210 = 99.75%, missing
*radio* and *video*. With `f`/`fe` → `ves` added it scores 1205/1210 =
99.59%, missing *brief*, *golf*, *proof*, *roof*: `f -> ves` is a rule about
nouns. `vbThirdBeforeFix` and `vbThirdWithVes` keep both versions so the page
prints the comparison rather than asserting it.

**The doubling rule**, over the 217 CVC-final verbs of the cleaned list
(`scripts/wordlists/doubling_verbs.json`; the list includes irregular verbs
such as *begin* and *swim*, whose `-ing` follows the rule, so it is not a
subset of the 1,210):

| | |
|---|---|
| double every one *(the version most books print)* | 107/217 = **49.3%** |
| double none | 110/217 = 50.7% |
| double when the last part is the strong part | 199/217 = **91.7%** |

Note the order flipped on cleaning: "double none" now scores slightly higher
than "double all". Of the 18 still wrong, **11 end in `-l`** (cancel, channel,
counsel, label, level, model, panel, rival, signal, total, travel) — the
British doubling rule, a second rule rather than a list of oddities. The other
seven: benefit, focus and program (both spellings recorded), format, input and
output (double against the stress), bus (the one verb the rule doubles and the
list does not). *offer*, *suffer* and *council* left the residue when their
misspellings were removed; *metal* was dropped because the dictionary
confirms neither *metalling* nor *metaling*.

**Two different scoring questions, said on the page.** The table lab counts a
hit when the rule's form is any recorded spelling, so *traveling* is right
there. The doubling lab asks whether the list ever records a doubled spelling,
so *travel* is wrong there. The doubling lesson explains the difference
explicitly, because a reader sees the same verb pass one page and fail the
next.

**Which cells English uses**, over 1,951 pronoun-subject verb phrases: present
and past simple 73.5%, plus future/modal 87.1%, perfect 7.3%, **progressive
1.4%**, future perfect progressive 0.1%. Measured, but **not taught by any
lesson**: no page computes it, so the course home and path key no longer
promise it (the 2026-10-08 pedagogy pass removed "four of the twelve boxes").

### Irregular Verbs

183 irregular verbs compiled; **132 survive the NGSL filter** (72.1%). Class
partition is exhaustive and sums: `past = participle` 60, `all different, -n
participle` 37, `all three the same` 21, `all different, other` 9,
`base = participle` 4, `base = past` 1.

**The denominator, because a share needs one.** The token figures below are
over **122,294 word tokens**, counted with the page's own tokeniser (a typographic
apostrophe is part of the word) over the novel text with the 154 illustration
captions removed: **15,147 irregular forms, 12.39%**, and **5.01%** without
be/have/do (recounted 2026-10-10; recipe in docs/pedagogy/english-irregular-verbs.md).
The earlier 15,192/123,611 = 12.29% and 4.98% came from a `[A-Za-z]+` count of
the raw Gutenberg slice, which split every U+2019 apostrophe and kept the
captions; they are withdrawn.

**The overclaim this Subject must not make.** "The top 20 cover most of it" is
87.66% of irregular tokens *including* be/have/do — but **73.90%** without them,
and be/have/do alone are **59.5%** of the irregular total. Seventeen of the
twenty slots do far less work than the headline implies, and the lesson says so.

### Helping Verbs

Six lessons, all scored on one printed chapter of the novel (Chapter XXVI) and
read against the two modern documents.

| lesson | rule | page figure | residue |
|---|---|---|---|
| The -s Belongs to He, She and It | *-s* after *he, she, it*; *are/were/have/do* or a bare form after *you, we, they* | holds in **74 of 75** pairs | the one pair against it, *if I were not afraid*, a *were* form |
| After a Modal, the Verb Is Bare | nine modals, then a verb with no ending | **65 of 76**, **0** followed by a verb with an ending | the other 11 rows break nothing: 2 questions (*will you come*), 2 where the scan reads past a full stop or comma, 7 a gap in the lists; quoted: no true exception in 2,738 whole-novel rows |
| Have Is Two Words | the next word says helper or main verb | the scan files **17 of 37** as helpers; read by hand **24 of 37, 64.9%** | the gap is the one-word scan, not the sample: 7 more are perfects (2 inverted conditionals, 2 with a phrase between, 3 with a participle the list lacks); 11 mean *own*; 2 are *had better* and *would have you be*; quoted: 59.5% over the novel |
| Be Is Mostly a Main Verb | what follows *be* | an *-ing* form after **6 of 137**, 4.4%; by hand **7 of 137, 5.1%** | the scan finds *-ing* forms from a 52-word list, so two progressives sit in the noun-phrase group (*was now fast approaching*); none of the 19 "something else" rows has a bare verb after *be* |
| Where Not Goes, and When Do Arrives | *not* after the first helper; *do* when there is none | **29 of 39**, 74.4% | the other ten are not mistakes; of five that look like old word order only *said not a word* is 1813 |
| Which of the Twelve Boxes Get Used | sort each pronoun-and-verb phrase into its box | of **216** phrases: simple 55, modal 57, perfect 4, progressive 3, *be* + participle 4, no verb found 42 | 27 of the 57 modal rows are "modal, other" (mostly *be* as the main verb); 42 are no verb found; quoted: all progressives together are 143 of 8,864, 1.6% |

### Nouns and Articles

| lesson | rule | page figure | residue |
|---|---|---|---|
| One Noun, Two Nouns | *-s*; *-es* after a hiss; *-y* becomes *-ies* | **1,866 of 1,887, 98.9%** | 21 misses: nine old forms no ending makes (seven are vowel changes, with *child* and *die* apart), five *f* words, five from Greek, *potato*, *stomach*. Two "improvements" lower the score (*-oes* to 1,864, *f* to *ves* to 1,861) |
| Nouns With No Plural | the list records no plural | **75 of 683** nouns | 47 mass nouns, 9 already plural or the same both ways, 16 days and months, 3 that need care (*basis, hell, sake*); the *no a/an* half is quoted |
| A or An: by Sound, Not by Letter | *an* before a vowel letter, against before a vowel sound | **486 of 493, 98.6%**, against **493 of 493, 100.0%** | the seven lines that separate them (*an hour*, *a university*); quoted: 2,266 *a/an* lines in the novel |
| The Before the Only One | *the* or a possessive before an *-est* word, *same*, *next*, *most* | *-est* **127 of 142, 89.4%**; *same* **69 of 69**; *next* **49 of 72, 68.1%**; *most* **40 of 122, 32.8%** | the 15 *-est* misses sort 4 + 3 + 2 + 6; *most* has a second meaning, *very*, which the one-word scan cannot tell from a superlative |

### Word Order

Two kinds of figure, and the lessons say which is which. **Whole-novel figures
are quoted** in the prose and labelled quoted, because no page can carry the
novel: subject pronouns **5,990 instances, 88.7% followed directly by a verb**,
residue a modifier between pronoun and verb 63% (*they both knew*, *we all*),
lexicon gap 16%, **inversion 15%**, other 6%; object pronouns **93.2%**;
frequency adverbs in mid-position **81.8%** of 577 (51 lexicon gap, 23 in a
phrase, 10 end, 7 start, 14 other); questions **55.4%**, connective-fronted
**45%** of the misses. These were recounted when written (2026-10-06) and
nobody has re-run them since; the kit engineer did not dispute them and did
not reproduce them.

**Page figures are computed in the browser** on printed text, pinned in the
kit's presets and read back with `labcheck.js --observe` (2026-10-08):

| lab | printed text | rule holds | residue |
|---|---|---|---|
| `svo`, subject | 936-word passage, 80 pronouns | **72 of 80, 90.0%** | 5 modifier between, 2 next word not in list, 1 inverted (a speech tag; the tile is called *word order broken*) |
| `svo`, object (*me, him, us, them*; *her* excluded as also possessive) | same passage, 17 | 15 of 17, 88.2% | 2 word before not in list |
| `adverbs` | 120 concordance lines, 8 adverbs | **85 of 120, 70.8%** | 6 a preposition follows, 29 something else (5 lexicon gaps, 3 *as soon as*, 5 before an adjective, clause-start, clause-end, one lone *Sometimes.*); *rarely* has no rows, so the menu leaves it out; the modern-documents count still searches for it |
| `questions` | 90 concordance lines, re-cut at sentence boundaries | **52 of 90, 57.8%** | 16 joining word first (**16 of 38, 42.1%**), 7 wh-word with no auxiliary after it, 2 address word, 4 pronoun first, 9 something else |
| `questions`, play | 256 questions of two words or more | **89 of 256, 34.8%** | 35 joining word first (21.0% of the misses), 27 pronoun first, 24 wh-word alone, 20 address, 14 no verb, 47 something else |

**Genuine word-order violations: zero.** Every inversion is the quotation-tag
device — *"But it is," returned she* — verified by sampling and by a surrounding
-window check (88% sit beside quoted speech, quoted). On the printed passage
the one inversion is *"My dear sister," said he*.

**Questions no longer ship stated-not-computed.** The lab counts the 90
printed questions; the whole-novel 55.4% and 45% are quoted beside the page's
57.8% and 42.1%, with the sentence that 90 lines are a sample.

### Small Words and Comparisons

| lesson | rule | page figure | residue |
|---|---|---|---|
| In, On or At: Time | choose by the kind of time word | **103 of 109, 94.5%** (novel 77 of 79, play 9 of 13, modern 17 of 17) | six misses in three kinds: a named day before *night*; a day picked out by words after the time word; *evening parties*, which is not a time phrase |
| Bigger or More Big | one part takes *-er*; the rest take *more* | **337 of 367, 91.8%** in the novel | 30 misses: 22 two-part adjectives the novel inflects, 3 *oftener*, 5 the other way; the modern documents score 32 of 32 |
| Happily, Simply, Truly | add *-ly*, then five spelling changes | add *-ly* **98 of 126, 77.8%**; with the changes **126 of 126, 100.0%** | the 28 misses end in *-le*, *-ic*, *-y* and *tall*; 27 of 153 adjectives have no *-ly* adverb |
| Give It Up, Not Give Up It | a pronoun goes between verb and particle, after a preposition | the novel: **34 of 42, 81.0%** of 473 lines | the 8 after the particle are clause boundaries and *over* as a preposition, so the rule stands |

### Spelling to Sound

| lesson | rule | page figure | residue |
|---|---|---|---|
| C and G Before E, I and Y | soft *c* says *s*, soft *g* says *j* | *c* **348 of 348**; *g* **177 of 187** | the ten *g* words that stay hard (*get, give, girl*) |
| The Silent E and the Vowel's Name | a silent *e* makes the vowel say its name | **131 of 140** | nine words you use every day, in three groups (*have, give*: the *e* is there for the *v*); before *r* the rule is right 1 of 19 |
| I Before E, and Its Failure Rate | *i before e, except after c* | **36 of 58, 62.1%**; only where the letters say *ee*, **14 of 18, 77.8%** | 22 misses: *eigh* 8, *cie* 9, five loners; after *c* the second half is right 2 of 11 |
| Letters You Do Not Say | six silent places | *gh* after a vowel is never *g* **42 of 42**; one silent letter **19 of 19**; *h* said **77 of 80** | the 42 *gh* words are 35 silent and 7 said *f*; *ough* has 5 sounds in 10 words and is a count, not a rule |
| -tion, -sion and -ture | each ending has one sound | *tion* **123 of 127**; *sion* **24 of 25**; *ture* **19 of 20**; *cial*, *tial* **12 of 12** | a few named misses; *intention* misses only on CMUdict's first entry |

### Word Stress

| lesson | rule | page figure | residue |
|---|---|---|---|
| Nouns at the Front, Verbs at the Back | a two-part noun is strong on the first part, a verb on the second | nouns **207 of 231**; verbs **134 of 150**; adjectives **35 of 47**; 49 words said both ways | 24 noun misses: ten made from a verb, three numbers and a month, eleven French loans; most verb misses end in a weak ending |
| Endings That Pull the Stress | the strong part is fixed by the ending | *-tion/-sion* **151 of 152**; *-ic* **28 of 28**; *-ical* **16 of 16**; *-ity* **27 of 27**; *-ate* **36 of 36**; *-ize* **13 of 14**; *-ee* **8 of 12** | *-ee* puts the push on the ending itself and is the contrast case |
| Endings That Leave It Alone | the word keeps the strong part it had | *-ly* **83 of 87**; *-ment* **31 of 32**; *-er* **48 of 50**; *-ness* **6 of 6**; *-ful* **7 of 7**; *-able* **10 of 10**; **185 of 192** pairs | the seven that move are mostly easy to explain; three *-ly* words where a secondary beat becomes the main one |
| The Flat Vowel | a weak part is said with the flat vowel | **1,387 of 2,628** weak parts, 52.8% | the other kinds: 400 with *r*, 352 the vowel of *sit*, 348 the vowel of *see* |

### Listening

| lesson | rule | page figure | residue |
|---|---|---|---|
| Why It Sounds Too Fast | fewer than fifty small words take a weak form | **387 of 936** words, 41.3%, from only 43 different words | the common small words that do not change are not on the list |
| Where a Word Begins | a word that carries meaning starts on its strong part | **390 of 474**, 82.3% | the 84 that start light, mostly with a small piece such as *a-* or *be-* |
| Where the Small Words Went | *not* is written *n't* in a text made to be said | play **22 of 36** (61.1%); novel **1 of 13** (7.7%); modern documents **0 of 10**; quoted: whole play 168 against 143 = 54.0%, whole novel 0.9% | the full form behind *'d* and *'s* is a choice the reader makes by hand |
| Why Words Run Together | a consonant before a vowel goes with the next word | **740** scored places: consonant then vowel **124, 16.8%**; vowel then vowel **53, 7.2%**; same consonant **16, 2.2%** | 17 places the dictionary lacks are not scored |

### Vocabulary and Reading

| lesson | rule | page figure | residue |
|---|---|---|---|
| How Much of a Page You Know | the share of a page the 2,800 words cover | passage **91.0%**, **94.3%** with names; play 85.9%, 94.6%; modern documents 87.3%, 92.7% | against Nation's quoted 98%; the passage leaves **41** words, sorted into kinds |
| Ten Words Are a Quarter of the Page | rank a page's words by count | ten words **25.6%**, fifty **54.5%**, a hundred **67.7%** of the passage (play 24.9%, 50.5%, 63.3%; modern 24.7%, 47.3%, 60.6%) | none of the ten names a thing or an act; the ten are the words that hold a sentence together |
| Word or Word Family | a flemma counts a word with its endings; a family counts the words made from it | passage **94.3% to 95.6%** (play 94.6% to 95.4%; modern 92.7% to 93.7%) | the 1.3 points are 12 words, and some rows are a real family while others are a cut that happened to land on a listed word |

## 6. Two landmines, both found the hard way

**The Gutenberg *Pride and Prejudice* (#1342) is the 1894 George Allen edition
and carries a Victorian critical preface by George Saintsbury INSIDE the usual
START/END markers.** The novel does not begin until roughly character 35,259.
Slicing on the markers mixes 1894 editorial prose into a figure labelled
"Austen, 1810s". My first SVO measurement did exactly that and reported 94.2%
over 6,121 pronouns; the correct figures are **5,990** and **88.7%**. Slice on
the novel's own first and last sentence — `"It is a truth universally
acknowledged"` to the last `"uniting them."` — which gives 122,396 whitespace
tokens against the commonly cited ~122k, and that agreement is the check.

**Modern formal prose does not contain the structures this Subject teaches.**
Two public-domain modern documents — *Stanley v. City of Sanford*, 606 U.S. 46
(2025), opinion of the Court, Parts I and II.A, and the Census Bureau's "U.S.
Population Aging as Nation Turns 250" (Rogers and Hayward, 2026-04-09) — are
inlined and printed on the Word Order pages and counted there: **1,723
letter-words** (1,843 whitespace tokens; the first draft's 1,844 counted
numbers, the § sign and citation strings). Against the printed passage, the
subject pronouns run **84.3 per 1,000 against 13.9, 6.1× fewer**, the object
pronouns **19.0 against 1.7, 10.9× fewer**; the nine adverbs occur **2 times,
1.2 per 1,000**; there are **zero question marks**. The first draft's 4.5×,
4.4× and "one every 256" were whole-novel ratios that could not be reproduced
(an offline re-run gave about 3.4×, 5.5× and 1 in 268, the last including
Gutenberg front matter), and no lesson states them any more. That is not a
reason to prefer Austen quietly — it is itself a finding worth teaching,
because it explains why a learner who reads only formal writing is unprepared
for speech.

## Scope

Ten courses and 41 lessons are the Subject as published (English v2,
`docs/english-v2/PLAN.md`), and the path page says so. It is narrow on purpose:
§1's test admits only a rule that can be run over printed words and scored in
the browser. A further course is added when its rule passes that test and its
residue can be printed, and not before; nothing is announced without a page.
