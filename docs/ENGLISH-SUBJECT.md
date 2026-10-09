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

### Course 2 — Irregular Verbs

183 irregular verbs compiled; **132 survive the NGSL filter** (72.1%). Class
partition is exhaustive and sums: `past = participle` 60, `all different, -n
participle` 37, `all three the same` 21, `all different, other` 9,
`base = participle` 4, `base = past` 1.

**The denominator, because a share needs one.** The token figures below are
over **123,611 word tokens** (letters and apostrophes only), not the 122,396
whitespace tokens the same text gives. 15,192/123,611 = 12.29%; 15,192/122,396
would be 12.41%. An agent caught the two not dividing to the printed figure.

**The overclaim this Subject must not make.** "The top 20 cover most of it" is
87.65% of irregular tokens *including* be/have/do — but **73.89%** without them,
and be/have/do alone are **59.5%** of the irregular total. Seventeen of the
twenty slots do far less work than the headline implies, and the lesson says so.

### Course 3 — Word Order

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
| `svo`, subject | 949-word passage, 80 pronouns | **72 of 80, 90.0%** | 5 modifier between, 2 next word not in list, 1 inverted (a speech tag; the tile is called *word order broken*) |
| `svo`, object (*me, him, us, them*; *her* excluded as also possessive) | same passage, 18 | 16 of 18, 88.9% | 2 word before not in list |
| `adverbs` | 120 concordance lines, 8 adverbs | **85 of 120, 70.8%** | 6 a preposition follows, 29 something else (5 lexicon gaps, 3 *as soon as*, 5 before an adjective, clause-start, clause-end, one lone *Sometimes.*); *rarely* has no rows, so the menu leaves it out; the modern-documents count still searches for it |
| `questions` | 90 concordance lines | **48 of 90, 53.3%** | 13 joining word first (**13 of 42, 31.0%**), 6 wh-word with no auxiliary after it, 2 address word, 21 something else — **16 of the 21 are lines cut mid-sentence** (fixed window, or the full stop in *Mr.*/*Mrs.*) |

**Genuine word-order violations: zero.** Every inversion is the quotation-tag
device — *"But it is," returned she* — verified by sampling and by a surrounding
-window check (88% sit beside quoted speech, quoted). On the printed passage
the one inversion is *"My dear sister," said he*.

**Questions no longer ship stated-not-computed.** The lab counts the 90
printed questions; the whole-novel 55.4% and 45% are quoted beside the page's
53.3% and 31.0%, with the sentence that 90 lines are a sample.

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
inlined and printed on the three word-order pages and counted there: **1,723
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

Four courses and ten lessons are the Subject as published, and the path page
says so. It is narrow on purpose: §2's test admits only a rule that can be run
over printed words and scored in the browser. A further course (for example
articles, or prepositions of time) is added when its rule passes that test and
its residue can be printed, and not before; nothing is announced without a page.
