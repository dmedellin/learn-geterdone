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

Measured: lesson one 99.0% with no glossary, lesson two 99.6% with two terms
(`consonant`, `vowel`), course home 98.5%, path page 99.4%.

**Five tokeniser bugs were found in `bandcheck.py` by running it, and every one
made the number look WORSE than the truth** — the direction that passes for
rigour. Hyphenated number words counted as unknown vocabulary; `<title>` leaked
the site's own domain into the prose stream; affixes (`-ing`, `-ed`) counted as
unknown words when they are the lesson's own subject; element boundaries joined
with no separator, inventing `ideaswhat` and `libraryenglishevery`; possessives
double-counted.

## 4. Licence

NGSL 1.2 (Browne, Culligan and Phillips) **CC BY-SA 4.0** for word lists,
CMUdict **BSD-2** for pronunciation, **public-domain** text for passages.
Nation's and Laufer's coverage thresholds are **quoted as published figures and
never embedded**, so no non-commercial term rides on the Subject.

Cost of the swap, and it is a teaching point rather than a defect: NGSL counts
**flemmas** (inflections only) where Nation counts **families** (headword plus
eighty-odd derivational affixes), so coverage figures land three to six points
lower. The lesson quotes by family, computes by flemma, and says which.

## 5. The measurements the courses are built on

Every figure below was computed, and every one was recounted independently
before it was written into a lesson.

### Course 1 — Tense Tables

| rule | hit rate | residue |
|---|---|---|
| `-s` | **99.85%** | shelf, stomach |
| `-ing` | **98.97%** | busing, counselling, formatting, inputting |
| `-ed` | **98.67%** | bred, bused, counselled, formatted |

Measured over the 1,356 regular verbs of the NGSL against that list's own
attested forms. The shipped JavaScript reproduces all three to the digit
(`scripts/wordlists/verbrules_check.js`).

**A rule that was refuted.** The `-s` residue first read `radio -> radioes,
shelf -> shelfs`. Two fixes suggested themselves: `-o` takes `-es` only after a
consonant, and `f`/`fe` becomes `ves`. The first was right. The second made the
rules **worse**, 99.7% to 99.6%, because *brief*, *golf*, *proof* and *roof* are
verbs that take `-s` and `f -> ves` is a rule about nouns. `vbThirdWithVes` keeps
the refuted version so the page can print the comparison.

**The doubling rule**, over the 232 verbs it can touch:

| | |
|---|---|
| double every one *(the version most books print)* | 117/232 = **50.4%** |
| double none | 115/232 = 49.6% |
| double when the last part is the strong part | 210/232 = **90.5%** |

Of the 22 still wrong, **13 end in `-l`** — the British doubling rule, which is a
second rule rather than a list of oddities.

**Which cells English uses**, over 1,951 pronoun-subject verb phrases: present
and past simple 73.5%, plus future/modal 87.1%, perfect 7.3%, **progressive
1.4%**, future perfect progressive 0.1%.

### Course 2 — Irregular Verbs

183 irregular verbs compiled; **132 survive the NGSL filter** (72.1%). Class
partition is exhaustive and sums: `past = participle` 60, `all different, -n
participle` 37, `all three the same` 21, `all different, other` 9,
`base = participle` 4, `base = past` 1.

**The overclaim this Subject must not make.** "The top 20 cover most of it" is
87.65% of irregular tokens *including* be/have/do — but **73.89%** without them,
and be/have/do alone are **59.5%** of the irregular total. Seventeen of the
twenty slots do far less work than the headline implies, and the lesson says so.

### Course 3 — Word Order

Subject pronouns, novel only: **5,990 instances, 88.7% followed directly by a
verb.** The residue is four named buckets, not one: a modifier between pronoun
and verb 63% (*they both knew*, *we all*), lexicon gap 16%, **inversion 15%**,
other 6%. Object pronouns score **93.2%**. Frequency adverbs in mid-position
**81.8%**.

**Genuine word-order violations: zero.** Every inversion is the quotation-tag
device — *"But it is," returned she* — verified by sampling and by a surrounding
-window check (88% sit beside quoted speech).

**Questions fail and ship stated-not-computed.** 55.4% on Austen, and the
largest residue bucket is connective-fronted (*"And what…"*, *"But why…"*) at
45%.

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
Two public-domain modern passages (a Supreme Court opinion and a Census Bureau
story) carry **4.5× fewer** target pronouns per thousand words than Austen, 4.4×
fewer frequency adverbs, and **zero questions in 1,844 words** against Austen's
one every 256. That is not a reason to prefer Austen quietly — it is itself a
finding worth teaching, because it explains why a learner who reads only formal
writing is unprepared for speech.
