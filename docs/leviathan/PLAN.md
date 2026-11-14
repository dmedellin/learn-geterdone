# Leviathan, Read Along — the build specification

The curriculum, lab and authoring contract for the nineteenth Subject: a
read-along of Thomas Hobbes, *Leviathan, or the Matter, Forme, & Power of a
Common-wealth Ecclesiasticall and Civill* (London: Andrew Crooke, 1651), in
the operator's copy of the Cambridge Texts in the History of Political Thought
revised student edition, edited by Richard Tuck (Cambridge University Press,
1996). All four Parts and the Review and Conclusion, in Hobbes's order, one
lesson per chapter or group of chapters. The operator asked for it the same way
as the previous read-alongs ("schedule one then the other", after *The Wealth
of Nations*), all the way to live.

It is built the way *Capital* (`docs/capital/PLAN.md`) and *Accelerate*
(`docs/accelerate/PLAN.md`) were, and adopts their conventions by reference
wherever this one is silent: Capital's §E (package, quoting a public-domain
text, author's checklist) and §F (voice, after the three lectures), and the
Philosophy Subject's §D.0 (lab conventions) and §E (course and lesson fields).
Read before this: `AGENTS.md` §0, §1, §1a, §7, §8; `content/AGENTS.md`;
`docs/capital/AUTHORING.md`.

**This Subject is a book of definitions and consequences.** Hobbes says
reasoning is reckoning, the adding and subtracting of names, and builds his
commonwealth from definitions of sense, speech, passion, power and right. Its
labs therefore compute what follows from what a lesson states: whether an
affirmation is true by the definitions given, what a coalition of the weak can
do against the strong, when a covenant is worth keeping with and without a
sword, what an assembly's voices decide, who succeeds a monarch on Hobbes's
presumptions, what an equal tax on consumption charges each person, when a
punishment deters, and when a book was written by what it mentions. The
Philosophy Subject is its nearest neighbour: its game, iterated-game, commons,
vote, update, validity, syllogism and analysis labs are reused here, and the
lesson that meets a game written from Chapter 13 names the Philosophy lesson
"Hobbes and the State of Nature" (Games and the Social Contract) by title and
does not repeat its prose.

Contents: §0 the one question · §A PATH · §B courses · §C every lesson ·
§D the new kit and the kits reused · §E package, text, quoting · §F voice ·
§G left out · §H wiring

---

## §0 The one question: what does the reader compute?

Hobbes's claims are claims about what follows from definitions and from
interests. The reader computes:

1. **Names and affirmations.** A name defined as the sum of other names; whether
   "A is B" is true by those definitions (every part of B is a part of A);
   whether it is absurd (it adds names that cannot be added, "round
   quadrangle", "incorporeal body") or insignificant (it uses a name that
   stands for nothing defined); a syllogism as the adding of two affirmations
   (Chapters 4, 5, 8, 9, 34, 45, 46).
2. **Deliberation.** A sequence of appetites and aversions toward an action;
   the will as the last of them before the action or its omission; what the
   will would have been had deliberation stopped sooner (Chapter 6).
3. **Worth.** A person's powers priced by buyers with different needs; why the
   ranking is not absolute; the public worth a commonwealth sets against what
   each buyer would give (Chapter 10).
4. **Equality and the war.** Whether the weakest, alone or with others, can
   overcome the strongest; the game of competition and diffidence; the
   repeated game in which gratitude and pardon pay (Chapters 13, 15, 17).
5. **Covenants.** When the second party to a covenant does better to keep it,
   with no common power and with a sanction applied with a stated certainty;
   the least sanction that makes keeping the better choice; the Fool's
   calculation and its threshold (Chapters 14, 15, 20, Review and Conclusion).
6. **Assemblies and succession.** What a representative's voices decide, when
   an even assembly is mute, and who is liable for what a body politic decreed;
   how often an assembly of n splits evenly; who succeeds on Hobbes's
   presumptions (Chapters 16, 19, 22, 25).
7. **Law, punishment and taxes.** The liberties left in the silence of the law
   and those no law takes away; when a punishment exceeds the benefit of the
   crime; what an equal imposition on consumption charges against one on
   riches; a distribution by stated shares (Chapters 21, 24, 27, 28, 30).
8. **Scripture and its uses.** When a book was written, by the latest thing it
   mentions; who benefits from a set of doctrines; a prophet's credentials as a
   Bayesian update on a stated base rate (Chapters 32, 33, 36, 37, 47).

**What the lab never does** is decide whether Hobbes is right. Every figure is
computed from the names, payoffs and numbers the lesson states, on Hobbes's
definitions as the lesson states them. Whether men are as Hobbes describes
them, and whether his conclusions hold for any commonwealth, is what the book
argues and its critics dispute. The material clause (§A) says so, and every
lesson closes on that gap.

## §A PATH fields (`content/leviathan/__init__.py`)

```
"slug": "leviathan",
"title": "Leviathan, Read Along",
"level": "Introductory → Advanced",
"level_note": "no philosophy or political theory is assumed",
```

No `"speech"` key (prose, as Capital and Phenomenology). If a run reads badly
the author adds it to `content/spoken/leviathan.py`.

Catalog (`scripts/catalog.py`): `short_title` `"Leviathan"`, `"kind": "Read
along"`, last in the philosophy group (after Capital, and after *The Wealth of
Nations* if that Subject is on main when this one is wired), card:
"Hobbes&rsquo;s <em>Leviathan</em>, chapter by chapter, from sense and speech
to the commonwealth and the kingdom of darkness, with each argument worked as
a problem you can check." The philosophy group's note says "The two
read-alongs go through one book chapter by chapter"; with more read-alongs in
the group it becomes "The read-alongs each go through one book chapter by
chapter" (whoever wires last makes the count right). Course slug prefix
`leviathan-`; check-id prefix `lev`; package `leviathan` → slug `leviathan`
needs no `PACKAGE_OF_SLUG` entry.

**material** (unique; required by `TestGeneratedPathIsCurrent`):
"every figure on this path is computed in your browser from the names, payoffs
and numbers a lesson states, and shows what follows from them on Hobbes&rsquo;s
definitions; whether men are as Hobbes describes them, and whether his
conclusions follow for any commonwealth, is what the book argues and the lab
cannot settle."

`LEV_DISCLAIMER_RE = r"what follows from them on Hobbes"` (§H).

tagline / description: written by course 1's author from the final counts
(`test_the_tagline_and_description_state_the_real_counts`). The tagline names
the book with `<em>`, says each argument is worked as a problem you can check,
and ends "Nine courses and N lessons are available."

## §B The nine courses

| # | slug | title | chapters | lessons | module dir |
|---|---|---|---|---|---|
| 1 | `leviathan-sense-and-speech` | Sense, Imagination and Speech | Epistle, Introduction, 1–4 | 5 | `c1_sense_and_speech` |
| 2 | `leviathan-reason-and-passions` | Reason, Science and the Passions | 5–9 | 7 | `c2_reason_and_passions` |
| 3 | `leviathan-power-manners-religion` | Power, Manners and Religion | 10–12 | 5 | `c3_power_and_religion` |
| 4 | `leviathan-natural-condition` | The Natural Condition and the Laws of Nature | 13–15 | 7 | `c4_natural_condition` |
| 5 | `leviathan-generation-of-commonwealth` | Persons and the Generation of a Commonwealth | 16–19 | 6 | `c5_commonwealth` |
| 6 | `leviathan-dominion-and-liberty` | Dominion, Liberty and the Parts of a Commonwealth | 20–23 | 4 | `c6_dominion_and_liberty` |
| 7 | `leviathan-office-of-sovereign` | Wealth, Counsel, Law and the Office of the Sovereign | 24–31 | 8 | `c7_office_of_sovereign` |
| 8 | `leviathan-christian-commonwealth` | Of a Christian Commonwealth | 32–43 | 8 | `c8_christian_commonwealth` |
| 9 | `leviathan-kingdom-of-darkness` | The Kingdom of Darkness, and the Review and Conclusion | 44–47, Review and Conclusion | 5 | `c9_kingdom_of_darkness` |

55 lessons. Part I (Of Man, 1–16) is split by its own argument: the mind's
materials (1–4), reason and passion (5–9), the social passions and religion
(10–12), and the natural condition with its laws (13–15); Chapter 16, on
persons, opens Course 5 because it is the hinge into Part II and Chapter 17
needs it. Part II (Of Common-wealth, 17–31) is split between the making of the
commonwealth (16–19), its kinds of dominion and its parts (20–23), and its
functions (24–31). Part III (32–43) is one course; Part IV (44–47) takes the
Review and Conclusion, which closes the book.

Modules (the `module` field) are Hobbes's chapter titles in the 1651 spelling
as the operator's copy prints them, shortened only where a title is very long,
e.g. `"Chapter 13 · Of the Naturall Condition of Mankind"`; the Introduction is
`"The Introduction"`; the last is `"A Review, and Conclusion"`. Authors copy
the title from the text, not from this plan.

## §C Every lesson

Format: slug — Title — chapter and topic — lab `kit/mode` view — focus.
Instances are the lesson's own: a sample written for the lesson ("five men",
"an assembly of six", "a covenant between a buyer and a seller"), plainly
labelled. Hobbes's own definitions, lists and examples (his definitions of the
passions, his presumptions of succession, the Pentateuch's "unto this day")
are public domain and may be used as lab data, with the chapter cited. Lesson
slugs are at most 48 characters.

### Course 1 — Sense, Imagination and Speech (Epistle, Introduction, Chapters 1–4)

1. `the-artificial-man` — The Artificial Man — Epistle Dedicatory and Introduction: the commonwealth as an artificial man, the correspondence of its parts, "read thyself" and the plan of the four Parts — `argkit/validity` — the Introduction's argument that one learns others' passions by reading one's own, written as premises and a conclusion; whether it is valid as stated and the premise that would make it so.
2. `sense-and-imagination` — Sense and Imagination — Chapters 1–2: sense as motion in the organ, qualities as seemings, the schools' "intelligible species"; imagination as decaying sense, memory, dreams, apparitions — `argkit/validity` — Hobbes's argument that the qualities we sense are not in the object (the pressed eye, the echo), as premises; its validity and the premise a critic would deny.
3. `the-train-of-imaginations` — The Train of Imaginations — Chapter 3: unguided and regulated trains, seeking causes and effects, prudence as presumption from experience, signs that are only conjectural — `choicekit/update` — a prudent man's presumption from his own stated experience of a sign, updated on one more observation; how far experience carries and why the sign stays fallible.
4. `speech-and-names` — Of Speech — Chapter 4 to its account of names: the invention of letters and speech, its four uses and four abuses, proper and common names, universals as names only — `levkit/reckon` `names` — a small vocabulary with proper, common and compound names; which names each thing falls under; which affirmations are true by the definitions.
5. `truth-and-definitions` — True and False, and Definitions — Chapter 4 from "true and false" to the end: truth in the right ordering of names, definitions first, "words are wise men's counters", names of inconstant signification — `levkit/reckon` `names` — the same vocabulary with a bad definition and a name defined twice; which affirmations change; one absurd and one insignificant affirmation.

### Course 2 — Reason, Science and the Passions (Chapters 5–9)

1. `reason-is-reckoning` — Reason Is Reckoning — Chapter 5 to the causes of absurdity: reason as the adding and subtracting of names, affirmations and syllogisms; no one's reason is right reason — `argkit/syllogism` — a syllogism as two affirmations added; a valid and an invalid form, Hobbes's way and the Venn way.
2. `absurdity-and-science` — Absurdity and Science — Chapter 5 from the causes of absurdity to the end: the seven causes of absurd conclusions, science as knowledge of consequences, prudence and sapience — `levkit/reckon` `names` — Hobbes's own examples of names that cannot be added (an accident of a body given to a name, a body given to a name); each claim classified true, false, absurd or insignificant.
3. `the-passions` — The Passions — Chapter 6 to the simple passions and their compounds: vital and voluntary motion, endeavour, appetite and aversion, good and evil relative to the person, Hobbes's definitions of hope, despair, fear, courage, anger and the rest — `levkit/reckon` `names` — Hobbes's definitions of a dozen passions as compounds of appetite, aversion and opinion; which passion each case is; a case that is two passions at once.
4. `deliberation-and-will` — Deliberation and the Will — Chapter 6 from deliberation to the end: deliberation as alternating appetites and aversions, the will as the last appetite, felicity as continual progress — `levkit/deliberate` `will` — a deliberation step by step; the will and whether the act was done or omitted; the will had it stopped at each earlier step.
5. `discourse-belief-and-faith` — The Ends of Discourse — Chapter 7: judgement and doubt, science as conditional knowledge, opinion, belief and faith in a person — `argkit/validity` — a conditional chain ("if this be, that is") from definitions; what it shows and what it cannot show about fact.
6. `wit-and-madness` — Intellectual Virtues and Madness — Chapter 8: natural and acquired wit, fancy and judgement, passions as the cause of difference in wit, madness, the insignificant speech of the schoolmen — `levkit/reckon` `names` — the schoolmen's phrases Hobbes calls insignificant, against stated definitions; which are absurd and which are empty.
7. `the-subjects-of-knowledge` — The Several Subjects of Knowledge — Chapter 9: knowledge of fact and of consequence, history natural and civil, the table of sciences — `levkit/reckon` `names` — part of Hobbes's table as nested definitions; which sciences fall under natural philosophy, which under civil; one misplaced science.

### Course 3 — Power, Manners and Religion (Chapters 10–12)

1. `power-and-worth` — Power and Worth — Chapter 10 to worth: power natural and instrumental, the forms of power, worth as price set by the buyer — `levkit/worth` `price` — four men's powers priced by three buyers with different needs; each buyer's ranking; why no ranking is absolute.
2. `honour-and-dignity` — Honour, Dignity and Worthiness — Chapter 10 from honouring to the end: signs of honour, dignity as public worth set by the commonwealth, titles, worthiness distinct from worth — `levkit/worth` `price` (with `dignity`) — the same men with the dignity the commonwealth sets; who is honoured above or below what a buyer would give.
3. `a-restless-desire-of-power` — The Difference of Manners — Chapter 11: a perpetual and restless desire of power after power, competition, love of ease and fear of death, ignorance of causes, credulity — `choicekit/game` — two neighbours who may arm or not; the equilibrium when each fears the other's gain; why moderate men still seek more power.
4. `the-seeds-of-religion` — The Natural Seeds of Religion — Chapter 12 to the seeds: anxiety for the future, ignorance of second causes, devotion toward what men fear, taking things casual for prognostics — `choicekit/update` — a "prognostic" observed before good and bad events at the rates stated; what it should change and what it does.
5. `religion-and-policy` — Religion and Policy — Chapter 12 from the two sorts of cultivators to the end: religion of the Gentiles, Numa and Mahomet, the causes of change in religion (unpleasing priests, contradiction, want of miracles) — `argkit/validity` — Hobbes's argument that a priest who teaches contradictions cannot be believed, as premises; valid, and which premise does the work.

### Course 4 — The Natural Condition and the Laws of Nature (Chapters 13–15)

1. `equality-of-ability` — Equality of Ability — Chapter 13 to the three causes of quarrel: equality of body and of mind, the weakest's strength to kill the strongest by machination or confederacy, from equality diffidence — `levkit/equality` `coalition` — six men's strengths: who can be overcome, by how few, with and without the advantage of secret machination.
2. `the-war-of-every-man` — The War of Every Man Against Every Man — Chapter 13 from competition, diffidence and glory to the end: war as a disposition, the incommodities of war, the inference from locks and arms, nothing unjust where there is no common power — `choicekit/game` — competition and diffidence as two-person games (the dilemma and the stag hunt); each equilibrium; names the Philosophy lesson "Hobbes and the State of Nature" by title.
3. `right-and-law-of-nature` — The Right and the Law of Nature — Chapter 14 to the second law: right as liberty, law as obligation, the first and second laws, laying down a right by renouncing or transferring — `argkit/validity` — the derivation of the second law from the first and the right of nature; valid as written; the premise that carries "if others will too".
4. `contracts-and-covenants` — Contracts and Covenants — Chapter 14 from contract to merit: transfer of right, contract, covenant and free gift, signs express and by inference, merit — `levkit/covenant` `perform` — a covenant in which one party performs first; what each gains by keeping and breaking; whether performing first is reasonable.
5. `covenants-and-the-sword` — Covenants Made Void and Kept — Chapter 14 from mutual trust to the end: covenants void on reasonable suspicion in the condition of mere nature but not under a common power, covenants extorted by fear, no covenant not to defend oneself, oaths — `levkit/covenant` `perform` (with sanction) — the same covenant under a power that punishes breach with a stated certainty; the least sanction that makes keeping better.
6. `justice-and-the-fool` — Justice and the Fool — Chapter 15 to the reply to the Fool: the third law, justice and injustice, propriety and the coercive power, the Fool who says there is no justice — `levkit/covenant` `fool` — the Fool's expected gain from breaking at stated chances of being cast out; the threshold; Hobbes's reply that one cannot reasonably count on the errors of others.
7. `the-other-laws-of-nature` — The Other Laws of Nature — Chapter 15 from merit to the end: gratitude, complaisance, pardon, revenge for the future, against contumely, pride and arrogance, equity, lots, mediators, the negative golden rule, the laws in foro interno, moral philosophy as the science of them — `choicekit/iterated` — the repeated dilemma with strategies that reward, forgive and retaliate; the round robin; what the tournament does and does not show about the laws of nature.

### Course 5 — Persons and the Generation of a Commonwealth (Chapters 16–19)

1. `persons-authors-and-actors` — Persons, Authors and Actors — Chapter 16 to the multitude: natural and feigned persons, author and actor, authority, a covenant by authority binding the author — `argkit/validity` — "the author is bound by what the actor does by his authority" as premises about a stated case; valid; the case without authority.
2. `one-person-by-consent` — A Multitude Made One Person — Chapter 16 from the multitude to the end: unity of the representer not the represented, the voice of the greater number, the even assembly that is mute, the negative voice — `levkit/assembly` `voices` and `ties` — an assembly's voices on a motion; passes, fails or mute; how often an assembly of each size splits evenly when each member is as likely to say yes as no.
3. `the-generation-of-a-commonwealth` — The Generation of a Commonwealth — Chapter 17: covenants without the sword are but words, small numbers and great multitudes, why bees and ants need no covenant, the covenant of every man with every man, the definition of a commonwealth — `choicekit/commons` — many people each choosing to keep or break a peace; the equilibrium without a sovereign and with a stated penalty.
4. `the-rights-of-sovereigns` — The Rights of Sovereigns by Institution — Chapter 18: the twelve rights, why subjects cannot change the form, why the sovereign cannot breach a covenant he did not make, the minority bound, no injury from the sovereign, the indivisibility of the rights, the comparison of miseries — `argkit/validity` — the argument that the sovereign cannot forfeit by breach, as premises; valid; the premise Locke would deny.
5. `kinds-of-commonwealth` — The Several Kinds of Commonwealth — Chapter 19 to succession: monarchy, aristocracy and democracy, tyranny and oligarchy as names of dislike, the comparison of monarchy with sovereign assemblies, the inconstancy of assemblies — `choicekit/vote` — an assembly of three factions whose majority preferences cycle; why its resolution depends on the order of the votes, the inconstancy Hobbes names from number.
6. `the-right-of-succession` — The Right of Succession — Chapter 19 from succession to the end: who disposes of the succession, express words or testament, custom, the presumption of natural affection (children before others, male before female, elder before younger, the nearer in blood before the remoter) — `levkit/succession` `heir` — a royal family; the successor with and without a testament; the line in order; what changes when the eldest son dies.

### Course 6 — Dominion, Liberty and the Parts of a Commonwealth (Chapters 20–23)

1. `dominion-paternal-and-despotical` — Dominion Paternal and Despotical — Chapter 20: commonwealth by acquisition, dominion by generation (the mother's in the state of nature), dominion by conquest from the covenant of the vanquished, absolute power in every form — `levkit/covenant` `perform` — the vanquished's covenant (life and liberty of body for obedience) with the victor as first performer; why it binds when made from fear.
2. `liberty-and-necessity` — Liberty and Necessity — Chapter 21 to the liberty of subjects: liberty as the absence of external impediments, liberty and fear, liberty and necessity consistent, the liberty of subjects in the silence of the law — `levkit/law` `silence` — a set of actions and three laws; what is commanded, forbidden and left free.
3. `the-true-liberties-of-subjects` — The True Liberty of Subjects — Chapter 21 from the true liberties to the end: the liberties no covenant can transfer, the refusal to fight, the obligation that lasts as long as protection — `levkit/law` `silence` (with `inalienable`) — the same laws with one that commands what a subject may refuse; the liberties retained.
4. `systems-and-public-ministers` — Systems Subject and Public Ministers — Chapters 22–23: systems regular and irregular, political and private, bodies politic limited by their letters, an assembly's decree against the law binding only those who voted for it, leagues and factions; public ministers and counsellors — `levkit/assembly` `voices` (with `liable`) — a body politic's vote to borrow; who is liable for the debt and who is excused.

### Course 7 — Wealth, Counsel, Law and the Office of the Sovereign (Chapters 24–31)

1. `nutrition-and-procreation` — The Nutrition and Procreation of a Commonwealth — Chapter 24: plenty, distribution, propriety from the sovereign, the land of Canaan divided by lot with the Levites given a tenth, money as the blood, colonies — `levkit/tax` `shares` — a territory distributed by the shares stated, with a portion set apart; each share exact.
2. `counsel` — Of Counsel — Chapter 25: command and counsel, exhortation and dehortation, the marks of good counsel, counsellors heard apart rather than in an assembly — `choicekit/vote` (jury) — the chance a majority of n counsellors is right at a stated competence; what the theorem assumes that Hobbes's case against assemblies denies (independence).
3. `civil-laws` — Of Civil Laws — Chapter 26: the definition, the sovereign as sole legislator and not subject to the laws, custom, the law of nature and civil law containing each other, interpretation, written and unwritten law — `argkit/validity` — the argument that the sovereign is not subject to the civil laws; valid; the premise Coke's lawyers would deny.
4. `crimes-excuses-and-extenuations` — Crimes, Excuses and Extenuations — Chapter 27: sin and crime, ignorance of law and of the sovereign, the sources of crime (defect in understanding, false teachers, the passions, hope of not being discovered), excuses, degrees of crime — `levkit/law` `deter` — a crime with a stated gain and chance of being discovered; when hope of impunity makes it pay.
5. `punishments-and-rewards` — Punishments and Rewards — Chapter 28: the definition, the right to punish, punishment less than the benefit of the crime, punishment beyond the law, hurt to the innocent, reward as salary or grace, the name Leviathan — `levkit/law` `deter` (with `prescribed`) — the same crime with the penalty the law prescribed and the penalty inflicted; which is punishment and which is hostility by Hobbes's definitions.
6. `the-diseases-of-a-commonwealth` — The Dissolution of a Commonwealth — Chapter 29: imperfect institution, seditious doctrines, imitation of neighbours and of the Greeks and Romans, mixed government, want of money, monopolies, popular men, great towns, liberty of disputing — `choicekit/game` — two powers that divide the sovereignty and each may yield or insist; the equilibria of chicken; why Hobbes calls divided power "a Kingdome divided in it selfe".
7. `the-office-of-the-sovereign` — The Office of the Sovereign Representative — Chapter 30: the safety of the people, instruction against rebellion, equal justice, equal taxes on consumption rather than on riches, public charity, good laws, counsellors — `levkit/tax` `impose` — a revenue raised from five people by an equal rate on riches and by one on consumption; each person's share; who pays more under which.
8. `the-kingdom-of-god-by-nature` — The Kingdom of God by Nature — Chapter 31: God's natural kingdom by irresistible power, not creation, Job's afflictions, natural worship, the attributes of God as honour, the close of Part II — `argkit/validity` — the argument that God's right to rule comes from his power; valid; the premise a critic who grounds it in creation or goodness would deny.

### Course 8 — Of a Christian Commonwealth (Chapters 32–43)

1. `the-principles-of-christian-politics` — The Principles of Christian Politics — Chapter 32: natural reason and supernatural revelation, the two marks of a true prophet (miracles and agreement with the established religion), miracles ceased — `argkit/validity` — the two marks as a conjunction; which candidates pass; why one mark alone does not suffice on Hobbes's text.
2. `the-books-of-scripture` — The Books of Holy Scripture — Chapter 33: the canon as the sovereign's, the Pentateuch written after Moses ("unto this day"), Joshua, Judges, Samuel and Kings written long after, the authority of Scripture — `levkit/canon` `date` — books with the events each mentions and the death of its traditional author; which must have been written later, and the latest event each mentions.
3. `spirit-angel-and-inspiration` — Spirit, Angel and Inspiration — Chapter 34: spirit as subtle body, angels as apparitions or bodies, "incorporeal substance" as a contradiction, inspiration as metaphor — `levkit/reckon` `names` — "spirit", "body", "substance" and "incorporeal" by Hobbes's definitions; which affirmations are absurd on them and which are not.
4. `the-kingdom-of-god-and-the-word` — The Kingdom of God and the Word of God — Chapters 35–36: the kingdom of God as a civil kingdom over the Jews, holy, sacred and sacrament; the word of God, prophets, and how a prophet is known (Ahab's four hundred) — `choicekit/update` — a prophecy from one of many prophets of whom few are true, as a stated base rate; what one fulfilled prophecy does to the chance he is true.
5. `miracles-and-their-use` — Miracles and Their Use — Chapter 37: a miracle defined, relative to the spectator, the enchanters of Egypt, the sovereign as judge of miracles — `choicekit/update` — a reported wonder under the hypotheses miracle, trick and error at stated rates; the posterior; why Hobbes leaves the judgement to the lawful church.
6. `eternal-life-and-the-church` — Eternal Life and the Church — Chapters 38–39: eternal life on earth after the resurrection, hell and salvation; the church as a company assembled by a lawful sovereign, so that a Christian commonwealth and a church are the same thing — `argkit/analysis` — Hobbes's definition of a church against a case table (a congregation, a commonwealth, a sect, a universal church); which cases it admits and the formula that would fit.
7. `the-sovereigns-of-israel-and-christ` — The Sovereigns of Israel and the Office of Christ — Chapters 40–41: the rights of God's kingdom in Abraham, Moses, the high priests and the kings; Christ's threefold office as redeemer, pastor and king to come — `argkit/validity` — the argument that Moses' authority came from the people's covenant, not from inspiration alone; valid; the premise that carries it.
8. `power-ecclesiastical-and-salvation` — Power Ecclesiastical and What Is Necessary for Salvation — Chapters 42–43: ecclesiastical power as teaching, not commanding; Bellarmine answered; faith that Jesus is the Christ and obedience to laws as all that is necessary — `argkit/validity` — the argument that a Christian need never disobey the sovereign to be saved; valid; the premise a Covenanter would deny.

### Course 9 — The Kingdom of Darkness, and the Review and Conclusion (Chapters 44–47)

1. `spiritual-darkness` — Spiritual Darkness from Misinterpretation of Scripture — Chapter 44: the kingdom of darkness, the kingdom of God taken for the present church, consecration turned to conjuration, eternal torment and purgatory — `argkit/validity` — Hobbes's argument against the present church as God's kingdom, as premises; valid; the premise that carries it.
2. `demonology-and-images` — Demonology and the Relics of the Gentiles — Chapter 45: images of fancy taken for spirits, demons, the worship of images, the canonizing of saints — `levkit/reckon` `names` — "image", "phantasm", "spirit" and "body" by Hobbes's definitions; which affirmations about demons are absurd on them.
3. `vain-philosophy` — Vain Philosophy and Fabulous Traditions — Chapter 46: philosophy defined, the schools, Aristotle's metaphysics, separated essences, abstract essences, the nunc stans, the insignificant speech of the schoolmen — `levkit/reckon` `names` — the schoolmen's terms Hobbes attacks against stated definitions; which claims are insignificant.
4. `who-benefits-from-darkness` — Of the Benefit That Proceedeth from Such Darkness — Chapter 47: cui bono, the doctrines and who gains by them, the three knots untied — `levkit/canon` `benefit` — Hobbes's list of doctrines against the parties they benefit; the count for each party; the party served by the most.
5. `review-and-conclusion` — A Review, and Conclusion — the contrary faculties reconciled by education, the added law that every man is bound to protect in war the authority that protects him in peace, when a subject may submit to a conqueror, the occasion of the book — `levkit/covenant` `perform` — protection and obedience as a covenant whose first performer is the sovereign; what the subject owes when protection fails.

## §D The new kit and the kits reused

### D.0 Reused kits, with no change

`argkit` (modes `validity`, `syllogism`, `analysis`) and `choicekit` (modes
`update`, `game`, `iterated`, `commons`, `vote`) are used exactly as the
Philosophy Subject uses them; both are in `KITS_WITH_EXPECTATIONS`, so every
preset needs an `expect`. Their cfg is documented in `docs/philosophy/PLAN.md`
§D.1 and §D.2 and in the kit modules' docstrings; the best references are the
Philosophy lessons that use the same mode (`grep -rn '"mode": "validity"'
content/philosophy/` and so on) and the Phenomenology lessons that reuse
`argkit/validity`. Never edit either kit. If one cannot show what a lesson
needs, the author writes the lesson with what it can show and reports the gap.

### D.1 The new kit: `levkit`

Built on `eakit_core` exactly as `acckit` is: copy `acckit`'s `mode_lab`
pattern (import `eakit_core` as `ea`; one pure JS `<prefix>Compute(view, inst,
opts)` per mode returning `{tiles, status, table}` or `{refuse}`; a Python
`check` per view mirroring every JS refusal; presets with `expect`; listed in
`build_paths.KITS_WITH_EXPECTATIONS`; mathcheck cases in
`scripts/mathcheck.js`, each seen to fail when its function is broken). Two
modules: `levkit.py` (entry point, shared helpers, family A) and `levkit_b.py`
(family B), with a seam contract `docs/leviathan/kit-contract.md` in the shape
of `docs/accelerate/kit-contract.md`. Report for authors:
`docs/leviathan/kit-report.md`, same shape as `docs/accelerate/kit-report.md`
(every cfg field, input format, tile id, with a worked example per view).

Id prefixes: three letters beginning `l`, as listed below; family A's
engineer greps them free on main (and on any open branch it can see) and
changes any that collide, announcing it at the top of the contract. Shared
helpers begin `lvk` / `LVK_`, and only `levkit.py` defines them.

Everything is exact counting and exact rational arithmetic (`RATIONAL_JS`).
Probabilities and certainties are typed as exact fractions or decimals
(`1/3`, `0.25`) and printed as the fraction and its percentage to at most two
decimals. Nothing typed is evaluated as script; names are `ea.NAME`-shaped
(the kit decides; it must accept multi-word names the lessons need, such as
`round quadrangle` written `round-quadrangle` or `round_quadrangle` — the kit
report says which). Each view's rules sentence says what is computed, the rule
in words, and how ties and orders go. Every lab ends its status line with the
same caution in a few words: the figure follows from what the lesson states,
on Hobbes's definitions as stated.

The panel intro, unless a lesson overrides it: "A figure computed from what
the lesson states. It shows what follows on Hobbes&rsquo;s definitions as
written here; whether they describe men and commonwealths is what the book
argues."

**Family A (`levkit.py`)**: names, deliberation, worth, equality, covenants.

| mode (prefix) | views | input | tiles (at least) |
|---|---|---|---|
| `reckon` (lrk) | `names` | `defs`: records `name, parts` (a name defined as the sum of others, parts space-separated; a name may appear as a part of several); `simple`: names admitted with no definition (the bottom of the reckoning); `opposed`: records `a, b` (two simple names that cannot be added: `body`/`incorporeal`, `round`/`quadrangle`); `claims`: records `claim, subject, predicate` ("subject is predicate") | for each defined name its expansion into simple names (sorted, listed); for each claim one verdict — **true** (every simple name of the predicate is in the subject's expansion), **false** (not so, and neither is absurd), **absurd** (the subject's or the predicate's expansion, or their sum, contains an opposed pair), **insignificant** (a name in the claim is neither defined nor simple: it stands for nothing); counts of each; the table: each claim, the two expansions, the verdict and the reason (the missing part, the opposed pair, the empty name). A definition that refers to itself, directly or through others, is refused naming the cycle. |
| `deliberate` (lde) | `will` | `options`: the action deliberated (one name) ; `steps`: records `step, motion, toward` (motion `appetite`/`aversion`, or `hope`/`fear` read as appetite/aversion with the opinion stated; `toward` = `do`/`omit`); optional `end`: `done`, `omitted` or `impossible` (default: as the last motion goes) | number of steps; alternations (changes of direction); the will (the last appetite or aversion), stated as the will to do or to omit; the outcome; table: the will had deliberation ended after each step; how many of those earlier stops would have given the opposite will. |
| `worth` (lwo) | `price` | `powers`: names of powers (2–6: `strength`, `eloquence`, `riches`, `reputation`, …); `persons`: records `person, <power>…` (whole amounts); `buyers`: records `buyer, <power>…` (whole or rational need weights); optional `dignity`: records `person, value` (the public worth the commonwealth sets) | for each buyer each person's price (Σ need × amount, exact) and the buyer's ranking (ties shared, stated); the person each buyer would pay most for; whether every buyer ranks the same (yes/no, and the first pair they disagree on); with `dignity`: each person's dignity against each buyer's price (above / equal / below) and the persons whose public worth differs from every buyer's. |
| `equality` (leq) | `coalition` | `persons`: records `person, strength` (whole, ≥ 1; 2–10 persons); `machination`: a factor ≥ 1 (exact) applied to an attacker's strength for secret machination or a sleeping victim, default 1; `rule`: `exceed` (strictly greater, default) or `match` | the strongest (and weakest); for each person, the smallest number of others whose summed strength × factor overcomes them by the rule, and one such coalition (chosen from the strongest others down, ties by input order, stated); whether anyone is beyond every coalition; whether the weakest alone (with the factor) overcomes the strongest; the count of persons who can be overcome by two or fewer. |
| `covenant` (lcv) | `perform` | a covenant between `first` and `second` (names): `cost1` (what the first gives up by performing), `gain1` (what the first gets when the second performs), `cost2`, `gain2`, all exact; `sanction` (penalty for the second's breach, default 0) and `certainty` (chance the sanction is applied, 0–1, default 1) | the second's payoff if it keeps (gain2 − cost2) and if it breaks (gain2 − certainty × sanction), exact; whether the second does better to keep (rule for a tie stated: keeping when equal, cfg `tie` `keep`/`break`, default `keep`); the first's payoff from performing first given that choice, and from not performing (0); whether performing first is reasonable; the least sanction that makes keeping at least as good (cost2 / certainty; refused with the reason when certainty is 0); with sanction 0, the status names the condition of mere nature. |
|  | `fool` | `gain` (what breaking now gains), `loss` (what being cast out of the confederacy costs), `chances`: a list of chances of being found out and cast out (0–1, up to 8) | for each chance the expected value of breaking (gain − chance × loss) against keeping (0), exact; the threshold chance (gain / loss) at which they are equal; the chances at which the Fool's calculation favours breaking; the table. |

**Family B (`levkit_b.py`)**: assemblies, succession, taxes, law, scripture.

| mode (prefix) | views | input | tiles (at least) |
|---|---|---|---|
| `assembly` (las) | `voices` | `members`: records `member, voice` (`yes`/`no`/`abstain`; 1–60 members); `rule`: `greater` (the greater number of voices given, default) or `absolute` (more than half of all members); optional `liable`: yes/no (show who is answerable for the decree, Chapter 22: those who voted for it) | yes, no, abstain; the decision: passes, fails, or **mute** (an even split, Chapter 16), with the rule named; the margin; with `liable`, the members answerable and the members excused. |
|  | `ties` | `sizes`: a list of assembly sizes (1–60, up to 8); each member as likely to vote yes as no, independently (a stated model, not Hobbes's) | for each size the chance of an even split: C(n, n/2) / 2ⁿ exact and as a percentage, 0 for odd n; the table; the status says that odd assemblies are never mute on this model and that Hobbes's point is about even ones. |
| `succession` (lsu) | `heir` | `people`: records `person, parent, sex, born, alive` (`parent` `-` for the root; `sex` `m`/`f`; `born` a whole number giving birth order; `alive` yes/no; up to 20); `monarch`: a person; optional `named`: a successor named by express words or testament; optional `custom`: `none` (default) or `male-line` (only males, through males) | the successor and the rule that chose him or her (testament, custom, presumption); the line of succession in order (first 6); by presumption (Chapter 19): the monarch's own issue before others; among issue, male before female, elder before younger, the issue of a dead child standing in its place before the next child (stated as the kit's reading, not Hobbes's words); with no issue, the nearer in blood before the remoter (fewest steps through the nearest common ancestor), and among the equally near, male before female and elder before younger; a named successor who is dead or unknown is refused with the reason. |
| `tax` (ltx) | `impose` | `persons`: records `person, riches, consumption` (whole); `revenue`: the sum to raise (exact) | the rate on riches (revenue / total riches) and on consumption (revenue / total consumption), exact and as %; each person's tax under each; the difference; who pays more under consumption; each person's tax as a share of their consumption under each; the table. |
|  | `shares` | `total`: what is divided (whole or exact); `parties`: records `party, weight` (whole or exact weights); optional `setaside`: records `party, fraction` (a fraction of the total set apart first, e.g. a tenth) | each set-aside portion; the remainder; each party's share of the remainder by weight, exact; the table; shares that are not whole are printed as exact fractions, never rounded. |
| `law` (llw) | `silence` | `actions`: names (up to 12); `laws`: records `law, commands, forbids` (space-separated action names; `-` for none); optional `inalienable`: records `action, reason` (actions a subject keeps the liberty to refuse whatever is commanded: Chapter 21) | actions commanded, forbidden, and free (in the silence of the law); actions both commanded and forbidden (a contradiction in the laws, listed); with `inalienable`: commands a subject may still refuse, and the reason; the share of actions left free. |
|  | `deter` | `gain` (the benefit of the crime to the offender), `penalty`, `certainty` (chance the penalty is inflicted, 0–1); optional `prescribed` (the penalty the law set beforehand) and `inflicted` | the expected penalty (certainty × penalty), exact; whether it exceeds the gain (deterrence, as a stated model); the least penalty that does at this certainty (gain / certainty; refused when certainty is 0); with `prescribed`/`inflicted`: whether the inflicted penalty exceeds the prescribed (the excess is "not punishment, but an act of hostility", Chapter 28) and whether a prescribed penalty below the gain is, on Hobbes's definition, rather the price of the crime than a punishment. |
| `canon` (lcn) | `date` | `books`: records `book, author, author_death` (a whole year on a stated scale, e.g. years from the Exodus; negative allowed); `mentions`: records `book, event, year` | for each book the latest event it mentions (the earliest it can have been written); whether that is after the traditional author's death (then "written after"); the gap in years; the books that cannot be the traditional author's on this test; the table. A book with no mention prints "no test". |
|  | `benefit` | `parties`: names; `doctrines`: records `doctrine, benefits` (space-separated party names) | for each party the number of doctrines that benefit it and their names; the party served by the most (ties listed); doctrines that benefit no one listed; the table. |

**Never**: say who is right, decide a question the book argues, carry a
modern statistic as Hobbes's, run typed text as script, print a figure the
inputs do not determine, round a share.

## §E Package, text, quoting

Package `content/leviathan/`, one directory per course (§B), each with
`__init__.py` (COURSE dict, same fields as `content/capital/c01_commodities/
__init__.py`) and `part_a.py` (and `part_b.py` past five lessons, split at the
midpoint). Spoken forms in `content/spoken/leviathan.py`, one block per course.

**The text** is the operator's copy (Tuck's edition), OCR'd privately outside
the repository (see `docs/leviathan/AUTHORING.md`). Hobbes's text of 1651 is in
the public domain; **Tuck's introduction, note on the text, chronology,
further reading, notes and index are in copyright**: never quote or paraphrase
them, and never copy any stretch of them anywhere. The OCR is of a 72-dpi scan
and is imperfect: every quotation is checked against the page image
(`page.py N --png`), not only against the OCR text, and is quoted as the page
prints it.

**Quoting** (Capital §E.3, adapted): the first `body` block is a `p`:
`<strong>Chapter 13.</strong> &ldquo;…&rdquo;` — the chapter (and Part when it
helps), then the quotation, nothing else; at most 120 words; Hobbes's 1651
spelling, capitals and italics-as-plain stand inside quotation marks, exactly
as printed (including "Common-wealth", "warre", "mans"). A second short
quotation may appear later in the body. Beside the lesson dict, a comment
`# Leviathan ch. N, 1651 p. M; PDF p. K of the operator's copy` (the 1651 page
is the bracketed number Tuck prints in the margin, e.g. `(62)`; give it where
the OCR shows it). Every phrase inside `&ldquo;…&rdquo;` must be in the text.
Never quote from memory or from another edition. The lesson's own prose uses
modern spelling ("commonwealth", "war").

**Attribution.** The path's `prerequisites` name the edition: the text of
1651, quoted from the operator's copy of Richard Tuck's revised student
edition (Cambridge, 1996), which keeps Hobbes's spelling. Each course's
`how_to` says once: "Quotations are from Hobbes's text of 1651, in its
original spelling."

## §F Voice

Capital §F applies (the three lectures; read the exemplary paragraph twice):
the teacher reads the passage whole, then goes through it; tells the history
of ideas as a story with people in it (the Civil War, Paris exile, the
Engagement controversy, Bramhall, Clarendon, Filmer, Locke, Spinoza later);
reaches for an everyday example when the idea is abstract; talks to the reader
as "you"; is warm and lets one light remark through; no slang, no first-person
anecdotes, no "let's dive in". Hobbes is presented, not endorsed: state what
the chapter argues, at strength, and where it is contested, say who contests it
and why, at strength too. Parts III and IV are presented as Hobbes's arguments
about Scripture and its interpreters, fairly, neither mocked nor defended as
theology: the lesson says what he argues and why it mattered politically in
1651. The `note` says what the lesson's computation cannot settle. The last
`p` of the body points to the next lesson (at a course's end, to the next
course). Credit Hobbes; Tuck is named only in the attribution.

## §G What is left out, and why

- Tuck's introduction, note on the text, chronology, further reading and
  index: in copyright, not taught, never quoted.
- The Latin *Leviathan* of 1668 and its appendix: not in the operator's copy.
- The frontispiece is described in words in Course 1, never reproduced.
- The Contents of the Chapters (Hobbes's own table): its titles are used as
  module names; not taught as a lesson.

## §H Wiring notes for the orchestrator

As Capital §H and Accelerate's wiring, with these values:

- Package `leviathan`; path slug `leviathan`; check-id prefix `lev`. Check ids
  take the form `lev-course9-lesson-<lesson-slug>` (19 characters before the
  slug), so a lesson slug may be at most 53 characters under the cap; every
  slug in §C is at most 48.
- `LEV_DISCLAIMER_RE = r"what follows from them on Hobbes"`.
- `content/spoken/leviathan.py`; `leviathan_semantic_copy` in
  `test_public_copy`.
- `"levkit"` joins `KITS_WITH_EXPECTATIONS` when the kit is registered.
- Catalog entry last in the philosophy group; home page and auth pages
  re-rendered by `scripts/build_index.py` and `scripts/build_auth_pages.py`.
- Every Subject, course, lesson and page count in the repository is updated in
  the wiring commit (AGENTS.md §0 and §1, README, tests, contracts, CI and
  Containerfile enumerations), from the counts on main at the time — rebase on
  main after *The Wealth of Nations* lands and recount.
