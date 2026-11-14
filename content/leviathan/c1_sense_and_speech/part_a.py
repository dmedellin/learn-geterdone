"""Sense, Imagination and Speech, lessons 1-5 -- the Epistle and Introduction, Chapters 1-4.

Every quotation is from Hobbes's text of 1651 as the operator's copy of Tuck's
student edition prints it (Hobbes's spelling, capitals and punctuation; italics
dropped), checked against the page image. The comment beside each lesson gives
the chapter, the 1651 page and the PDF page of that copy. Nothing from the
editor's apparatus is used.

"""

LESSONS = [
    # ---------------------------------------------------------------- 01
    # Introduction, 1651 p. 1; PDF p. 105 of the operator's copy (Epistle PDF p. 99-100; Introduction PDF p. 105-107).
    {
        "slug": "the-artificial-man",
        "title": "The Artificial Man",
        "module": "The Introduction",
        "one_line": "Hobbes builds his book on one picture, a commonwealth that is an artificial man, and one rule, that you learn other men by reading yourself.",
        "summary": (
            "The Epistle Dedicatory and the Introduction say what the book is: the "
            "making of an artificial man, a commonwealth, whose parts answer to the "
            "parts of a natural one. Hobbes then argues that whoever looks into himself "
            "can read the passions of all other men. Set that argument out as premises "
            "and a conclusion and ask what it needs in order to be valid."
        ),
        "key": [
            "commonwealth = an artificial man",
            "sovereignty = its artificial soul",
            "read thyself: same passions, other objects",
            "valid needs a bridge premise",
            "valid does not mean true",
        ],
        "key_label": "The Introduction in five lines",
        "concepts_intro": (
            "The Introduction is two pages long. It says what the book will build, "
            "how it will be built, and how you will be able to check it."
        ),
        "concepts": [
            ("The artificial man",
             "Nature is God's art, and men imitate it: a watch has an artificial life, "
             "and a commonwealth is an artificial man, bigger and stronger than the "
             "natural one, made to protect it. Every part of the state has a counterpart "
             "in the body, from the sovereign, the soul, to civil war, which is death."),
            ("The four parts of the plan",
             "Hobbes will consider the matter and the maker of the commonwealth, both of "
             "which are men; then how it is made by covenants, and what the rights of a "
             "sovereign are; then what a Christian commonwealth is; and last what the "
             "kingdom of darkness is. The book follows that order."),
            ("Read thyself",
             "The old saying <em>nosce teipsum</em> does not tell you to flatter or "
             "despise anyone. It tells you that your own thoughts and passions are the "
             "key to everyone's, because the passions are alike in all men, though the "
             "things they are aimed at differ."),
        ],
        "read_title": "The passage first, then the Introduction line by line",
        "read_intro": (
            "The passage comes first: the sentence in which the book names itself. "
            "After it, the order is Hobbes's own: the machine, the plan and the rule "
            "for reading."
        ),
        "body": [
            ("p", "<strong>Introduction.</strong> &ldquo;For by Art is created that great "
                  "LEVIATHAN called a COMMON-WEALTH, or STATE, (in latine Civitas) which is "
                  "but an Artificiall Man; though of greater stature and strength than the "
                  "Naturall, for whose protection and defence it was intended; and in which, "
                  "the Soveraignty is an Artificiall Soul, as giving life and motion to the "
                  "whole body;&rdquo;"),
            ("p", "Start with the step before it, which is easy to read past. Hobbes asks "
                  "why we may not say &ldquo;that all Automata (Engines that move themselves "
                  "by springs and wheeles as doth a watch) have an artificiall life?&rdquo; "
                  "If life is only a motion of the limbs, begun somewhere inside, then a "
                  "watch moves much as a man does, and the heart is a spring and the nerves "
                  "are strings. Nothing in the sentence is meant as ornament. It is a "
                  "claim about what life is, and the commonwealth is the next step on the "
                  "same road: art that imitates &ldquo;that Rationall and most excellent "
                  "worke of Nature, Man&rdquo;."),
            ("p", "Then comes the list, and it repays going through slowly. The "
                  "sovereign is the soul. The magistrates and other officers are "
                  "&ldquo;artificiall Joynts&rdquo;, and &ldquo;Reward and Punishment&rdquo; "
                  "are the nerves that move each joint to its duty. The wealth of the "
                  "members is the strength, the counsellors are the memory, and equity and "
                  "laws are &ldquo;an artificiall Reason and Will&rdquo;. Health and "
                  "sickness have their counterparts too: &ldquo;Concord, Health; Sedition, "
                  "Sicknesse; and Civill war, Death.&rdquo; The word that matters most is "
                  "<em>artificial</em>. This man was made, and the last item on the list "
                  "says by whom: the &ldquo;Pacts and Covenants&rdquo; that first set the "
                  "parts together resemble the <em>Let us make man</em> that God spoke in "
                  "the Creation. A commonwealth is not an organism that grew. It is a "
                  "device people built, and so people can be asked how it should be built."),
            ("def", ("Artificial man",
                     "Hobbes's name for the commonwealth: a body made by covenant, with "
                     "the sovereignty as its soul. The first edition's title page shows "
                     "the same thing in a picture, a crowned giant rising over a town "
                     "and its fields, his body made of many small figures, with a sword "
                     "in one hand and a crozier in the other.")),
            ("p", "The book is dated from Paris, in 1651. Hobbes had left England in "
                  "1640, as the quarrel between the King and Parliament became a war; "
                  "King Charles was executed in 1649, and the man who wrote the dedication "
                  "to Francis Godolphin knew that its readers on both sides would be "
                  "looking for offence. He says so himself: it is &ldquo;a way beset "
                  "with those that contend, on one side for too great Liberty, and on the "
                  "other side for too much Authority, &rsquo;tis hard to passe between the "
                  "points of both unwounded.&rdquo; He adds that he speaks of the "
                  "&ldquo;Seat of Power&rdquo; and not of the men who sit on it, and that "
                  "what may offend most is his use of Scripture, which he calls "
                  "&ldquo;the Outworks of the Enemy&rdquo;. Keep that in mind for the "
                  "later parts."),
            ("p", "Next the plan. After the matter and maker of the artificial man, "
                  "&ldquo;both which is Man&rdquo;, he will take &ldquo;Secondly, How, and "
                  "by what Covenants it is made&rdquo;, then a Christian commonwealth, and "
                  "&ldquo;Lastly, what is the Kingdome of Darkness.&rdquo; Those are the "
                  "four Parts, and the nine courses of this Subject follow them."),
            ("p", "The first Part has to say what a man is made of, so the question "
                  "is how anyone could know that. Hobbes starts from a saying then "
                  "&ldquo;much usurped of late, That Wisedome is acquired, not by reading "
                  "of Books, but of Men.&rdquo; He answers with an older one, <em>Nosce "
                  "teipsum</em>, &ldquo;Read thy self&rdquo;, and spells out what it asks: "
                  "&ldquo;whosoever looketh into himself, and considereth what he doth, "
                  "when he does think, opine, reason, hope, feare, &amp;c, and upon what "
                  "grounds; he shall thereby read and know, what are the thoughts, and "
                  "Passions of all other men, upon the like occasions.&rdquo; The limit "
                  "matters as much as the rule. It is &ldquo;the similitude of Passions, "
                  "which are the same in all men, desire, feare, hope, &amp;c; not the "
                  "similitude of the objects of the Passions&rdquo;, since what a man "
                  "wants or fears depends on his temper and upbringing, and a man's "
                  "heart is hidden by dissembling. To read another from his actions "
                  "without comparing them with your own is &ldquo;to decypher without a "
                  "key&rdquo;."),
            ("p", "Set the rule out as an argument. Let `p` be &ldquo;the passions are "
                  "the same in all men&rdquo;, `q` be <em>a man looks into himself and "
                  "considers what he does when he thinks and hopes and fears</em>, and "
                  "`r` be <em>he thereby reads the passions of other men on like "
                  "occasions</em>. In the bare preset the premises are `p` and `q` and "
                  "the conclusion is `r`. The table has eight rows, and exactly one of "
                  "them makes both premises true and `r` false: the one where the passions "
                  "are alike, the man has looked, and he reads nothing. So as stated the "
                  "argument is invalid. What closes the gap is a third premise, that "
                  "<em>if</em> the passions are alike and a man looks into himself, then "
                  "he reads others. The bridged preset adds it and the counterexample "
                  "row is gone. It is the sentence Hobbes means, and the one he does "
                  "not spell out. The third preset, without-looking, keeps the bridge "
                  "and drops `q`: the table again finds one row, where the passions are "
                  "alike, no one has looked, and no one reads anything. The rule works "
                  "only for the man who actually does the looking."),
            ("p", "Whether the premises are true is a different matter, and the "
                  "lab cannot say. Hobbes's reply is on the next page: the pains he "
                  "leaves to the reader &ldquo;will be onely to consider, if he also find "
                  "not the same in himself. For this kind of Doctrine, admitteth no "
                  "other Demonstration.&rdquo; The test is each reader's own "
                  "introspection. Critics, then and since, have answered that a man who "
                  "reads himself finds his own temper, and that Hobbes's reading of "
                  "mankind may be the portrait of one anxious and ambitious sort of "
                  "man, taken for all. His reply is in the passage: the passions, not the "
                  "objects, are what you compare, and you are invited to say if you do "
                  "not find them in yourself."),
            ("p", "The next lesson takes Hobbes at his word and does what the rule "
                  "says: it begins at Chapter 1 with the first thing in a man, sense, "
                  "and asks what he says happens when you see, hear and touch."),
        ],
        "lab": ("argkit", {
            "mode": "validity",
            "preset": "bare",
            "show": "all",
            "presets": [
                {"id": "bare", "label": "Alike passions and looking, so reading",
                 "premises": ["p", "q"], "conclusion": "r",
                 "expect": {"vaVerdict": "Invalid", "vaCounter": "1"}},
                {"id": "bridged", "label": "The same, with the bridge premise",
                 "premises": ["p", "q", "p & q -> r"], "conclusion": "r",
                 "expect": {"vaVerdict": "Valid", "vaCounter": "0"}},
                {"id": "without-looking", "label": "The bridge, but no one looks",
                 "premises": ["p", "p & q -> r"], "conclusion": "r",
                 "expect": {"vaVerdict": "Invalid", "vaCounter": "1"}},
            ],
            "panel_title": "Does reading oneself support reading others?",
            "panel_intro": (
                "Each row is a case. A highlighted row makes every premise true and the "
                "conclusion false. Choose bare and find the one such row, then bridged "
                "and compare, then without-looking and say what the highlighted row "
                "describes. The table says what follows from the premises, not whether "
                "they are true."
            ),
        }),
        "steps_title": "Finding the premise an argument leans on",
        "steps_intro": "Four moves, for any passage that says &ldquo;whosoever does this will find that&rdquo;.",
        "steps": [
            ("Find the conclusion",
             "Ask what the passage says you will end up able to do or know. Here "
             "it is that you will read the passions of other men."),
            ("List what is stated",
             "Give each stated claim a letter: the passions are alike, you look into "
             "yourself. Do not add anything the passage does not say."),
            ("Run the table",
             "Look for a row that makes every stated premise true and the conclusion "
             "false. If there is none, the argument is valid as stated."),
            ("Read the counterexample row",
             "The row describes the case the author must be assuming away. Write it "
             "as a sentence, and that is the bridge premise to be defended."),
        ],
        "worked": {
            "title": "The one row that fails",
            "intro": [
                "Take the bare preset: premises `p` and `q`, conclusion `r`. There are "
                "three letters, so `2 · 2 · 2 = 8` rows.",
            ],
            "lines": [
                "rows:  2 · 2 · 2 = 8",
                "premises both true:  p true, q true  (2 rows: r true or false)",
                "counterexample:  p true, q true, r false  (1 row)",
                "bridge:  if p and q then r  rules that row out",
            ],
            "after": [
                "The two rows where both premises are true differ only in `r`, and "
                "one of them refutes the argument. The bridge premise is false in "
                "exactly that row and true in the other seven, so adding it leaves "
                "nothing to refute: the bridged preset has 0 counterexample rows.",
            ],
        },
        "quiz_title": "What the Introduction needs",
        "quiz": [
            {"q": "In the bare preset the lab finds one counterexample row. What does "
                  "that row say?",
             "a": ["Both premises are true and the conclusion is false: the passions are alike, "
                   "the man has looked, and he reads nothing",
                   "The conclusion is true and both premises are false",
                   "Neither premise is true, so the argument says nothing",
                   "The passions are not alike in all men"],
             "c": 0,
             "why": "A counterexample row makes every premise true and the conclusion false. "
                    "A row with false premises cannot refute an argument, and the lab does "
                    "not decide whether the passions are alike: it only shows that the "
                    "stated premises do not by themselves rule out the case."},
            {"q": "In his rule, what does Hobbes say one learns by reading oneself?",
             "a": ["What particular things other men desire, fear and hope for",
                   "That other men will always act as one would oneself",
                   "The thoughts and passions of all other men upon like occasions, "
                   "though not the objects they are aimed at",
                   "What God has decreed for each man"],
             "c": 2,
             "why": "He separates &ldquo;the similitude of Passions&rdquo; from &ldquo;the "
                    "similitude of the objects of the Passions&rdquo;. The first is alike in "
                    "all men; the second varies with temper and education, and is easy to "
                    "keep from other people's knowledge."},
            {"q": "Which sentence is the bridge that makes the argument valid?",
             "a": ["If a man reads others, the passions are alike",
                   "If the passions are alike and a man looks into himself, then he "
                   "reads the passions of others",
                   "The passions are alike in all men",
                   "A man looks into himself"],
             "c": 1,
             "why": "The bridge is a conditional that joins both premises to the conclusion. "
                    "The converse in the second option runs the wrong way and leaves the "
                    "counterexample row in place, and the last two are the premises "
                    "already stated."},
            {"q": "What does Hobbes say about how the Introduction's claim is to be "
                  "demonstrated?",
             "a": ["By experiment on many men",
                   "By citing the authority of the ancients",
                   "By each reader considering whether he finds the same in himself",
                   "It cannot be demonstrated and need not be"],
             "c": 2,
             "why": "He says the pains left to another &ldquo;will be onely to consider, if he "
                    "also find not the same in himself. For this kind of Doctrine, admitteth "
                    "no other Demonstration.&rdquo; So he does claim a demonstration, of one "
                    "kind only."},
        ],
        "mistakes": [
            ("Thinking reading yourself tells you what other men want",
             "Hobbes limits the rule: it is the passions that are alike, desire, fear, "
             "hope, and not their objects. What a particular man wants depends on his "
             "constitution and his education, and Hobbes says those are easy to hide. "
             "Reading yourself gives you the key, not the message."),
            ("Reading the artificial man as a figure of speech only",
             "The picture is a claim: life is a motion of the limbs, and a commonwealth "
             "is a made thing with parts that answer to a man's. The word Hobbes stresses "
             "is <em>artificial</em>, a body set up by &ldquo;Pacts and Covenants&rdquo; "
             "and not grown. If it was made, it can be made well or badly, and the "
             "later Parts ask how."),
            ("Taking a valid argument to be a true one",
             "The bridged preset has no counterexample row, and that shows only that "
             "the conclusion follows if the three premises are true. Whether the "
             "passions are alike in all men is the book's own question, and the lab "
             "leaves it where it was."),
        ],
        "standard": (
            "Finish when you can set the rule out as premises and a conclusion.",
            "Given a passage that says what follows if you do something, list its stated "
            "claims as premises, find the counterexample row if any, and state the "
            "bridge premise that rules it out."
        ),
        "note": (
            "The lab shows that the argument is valid once the bridge is added, and "
            "invalid without it. It cannot say whether the passions are alike in all men, "
            "which is the premise Hobbes asks each reader to test in himself, nor whether "
            "the bridge is true. The three letters are a simplification of two sentences "
            "of Hobbes's, written for this lesson."
        ),
    },
    # ---------------------------------------------------------------- 02
    # Leviathan ch. 1, 1651 p. 4; PDF p. 110 of the operator's copy (Chapters 1-2: PDF p. 109-115).
    {
        "slug": "sense-and-imagination",
        "title": "Sense and Imagination",
        "module": "Chapters 1 and 2 · Of Sense; Of Imagination",
        "one_line": "Sense is the pressure of bodies on our organs, and what we call colour and sound is the fancy that pressure causes in us.",
        "summary": (
            "Hobbes begins with the thoughts of one man, singly. Sense, he says, is "
            "motion in the organs, and the qualities we sense are the appearance of that "
            "motion. Imagination is sense decaying; memory is its other name; dreams are "
            "imagination in sleep. Set out his argument from the echo as premises, check "
            "that it is valid, and find the premise a critic would deny."
        ),
        "key": [
            "sense: pressure on an organ, seen as fancy",
            "colour and sound: motions in the object",
            "imagination = decaying sense",
            "memory and imagination: one thing",
            "echo argument: valid; deny premise two",
        ],
        "key_label": "Chapters 1 and 2 in five lines",
        "concepts_intro": (
            "Chapter 1 is a page and a half, and Chapter 2 is five pages. Between them "
            "they give the stock of ideas the rest of Part I uses."
        ),
        "concepts": [
            ("Sense as seeming",
             "An object presses an organ, the pressure is carried by the nerves to the "
             "brain and heart, and the heart's counter-pressure, because it is outward, "
             "&ldquo;seemeth to be some matter without&rdquo;. That seeming is sense. "
             "Colours and sounds are in the object only as motions of its matter; the "
             "appearance of them is in us."),
            ("Imagination and memory",
             "When the object is gone, the motion does not stop at once. What remains is "
             "imagination, which Hobbes calls decaying sense; seen as fading, old and past "
             "it is memory, and much memory is experience. Imagining one thing as it was "
             "seen is simple; joining a man and a horse into a centaur is compound."),
            ("Dreams and apparitions",
             "A dream is imagination in sleep, set going by the body's inward motions, "
             "clearer than waking thought because the senses are quiet. Hobbes takes the "
             "ghosts and visions men report to be dreams or strong fancies mistaken for "
             "sense, and he notes who profits from the mistake."),
        ],
        "read_title": "The passage first, then the two chapters line by line",
        "read_intro": (
            "The passage is Hobbes's claim about what qualities are. After it the "
            "lesson goes through the argument for the claim, the schools' rival "
            "account, and then Chapter 2."
        ),
        "body": [
            ("p", "<strong>Chapter 1.</strong> &ldquo;All which qualities called "
                  "Sensible, are in the object that causeth them, but so many several "
                  "motions of the matter, by which it presseth our organs diversly. "
                  "Neither in us that are pressed, are they any thing else, but divers "
                  "motions; (for motion, produceth nothing but motion.) But their "
                  "apparence to us is Fancy, the same waking, that dreaming.&rdquo;"),
            ("p", "Hobbes has just said that he will take the thoughts of a man "
                  "&ldquo;singly&rdquo; and then in a train. Singly, each is a "
                  "representation of some quality of a body outside us, and the origin "
                  "of all of them is sense: &ldquo;there is no conception in a mans mind, "
                  "which hath not at first, totally, or by parts, been begotten upon the "
                  "organs of Sense.&rdquo; Everything else is derived from that. The "
                  "cause of sense is the body outside, which presses the organ, "
                  "immediately in taste and touch and mediately in seeing, hearing and "
                  "smelling, and the pressure is carried inwards until the heart's "
                  "endeavour to deliver itself outward &ldquo;seemeth to be some matter "
                  "without&rdquo;."),
            ("p", "Now read the passage again. Heat, cold, colour, sound, hardness are "
                  "called sensible qualities. In the thing they are only motions of its "
                  "matter, and in us they are only motions too, so there is no colour "
                  "travelling from the object into the eye. What we have is the "
                  "&ldquo;apparence&rdquo;, the fancy, and it is the same whether we "
                  "wake or dream. Notice what he does not say. The object is real and it "
                  "is the cause. What he denies is that redness, as we see it, is a "
                  "property of the object."),
            ("p", "He gives two arguments. The first is from the body: &ldquo;pressing, "
                  "rubbing, or striking the Eye, makes us fancy a light&rdquo;, and "
                  "pressing the ear makes a din, so when we see a body the same fancy "
                  "comes of a strong though unobserved action. The second is the one the "
                  "lab takes: &ldquo;if those Colours, and Sounds, were in the Bodies, or "
                  "Objects that cause them, they could not bee severed from them, as by "
                  "glasses, and in Ecchoes by reflection, wee see they are; where we know "
                  "the thing we see, is in one place; the apparence, in another.&rdquo; "
                  "Put it as premises. Let `a` be <em>colours and sounds are in the "
                  "objects</em> and `b` be <em>they cannot be severed from the "
                  "objects</em>. The first premise is that if `a`, then `b`. The second "
                  "is that not `b`: a mirror and an echo show them apart. The conclusion "
                  "is that not `a`. In the echo preset the table has four rows and no "
                  "counterexample, and the lab names the form, modus tollens. The "
                  "argument is valid. Whatever is wrong with it, it is not the logic."),
            ("p", "So a critic must deny a premise, and the lab shows what each denial "
                  "costs. In the no-conditional preset the first premise is dropped, so "
                  "only the second remains, and now there is one counterexample row: the "
                  "colour is in the object and it can still be shown apart. That row is "
                  "the opening for a critic who says that a quality may be in a thing and "
                  "also be carried from it, which is just what the schools said. A "
                  "critic can also deny the second premise: a modern physicist might say "
                  "that the colour of a body is its disposition to reflect some light and "
                  "not others, which stays in the body when the mirror shows only the "
                  "light. Then nothing has been severed from the body. Hobbes's premise "
                  "and his critic's depend on what is counted as the colour. The other "
                  "two presets take the first argument, the pressed eye. In pressed, the only "
                  "premise is `e`, that pressing the eye makes us fancy a light, and the "
                  "conclusion is `m`, that sense is a motion in us; the lab finds one "
                  "counterexample row, because Hobbes reasons by analogy (&ldquo;so do the "
                  "bodies also we see&rdquo;), and an analogy is a premise. The analogy "
                  "preset adds it as `e → m`, and the argument is then valid."),
            ("p", "The schools, which Hobbes names, &ldquo;through all the Universities "
                  "of Christendome, grounded upon certain Texts of Aristotle, teach "
                  "another doctrine&rdquo;. As he reports it, the thing seen sends out "
                  "&ldquo;a visible species (in English) a visible shew, apparition, or "
                  "aspect, or a being seen&rdquo;, and receiving it is seeing. Hearing "
                  "and even understanding have their species too. Hobbes says that he is "
                  "not disapproving the use of the universities, but that he must show on "
                  "the way what needs mending in them, and &ldquo;the frequency of "
                  "insignificant Speech is one.&rdquo; He is already thinking of Part II, "
                  "where he will argue about their office in a commonwealth."),
            ("p", "Chapter 2 starts with motion, and it matters for the rest. "
                  "&ldquo;When a Body is once in motion, it moveth (unless something els "
                  "hinder it) eternally&rdquo;, and men think otherwise only because they "
                  "measure other things by themselves and by their own weariness. So the "
                  "schools' saying that heavy bodies fall &ldquo;out of an appetite to "
                  "rest&rdquo; is, he says, absurd. Then the account of imagination: after "
                  "the object is removed &ldquo;wee still retain an image of the thing "
                  "seen, though more obscure&rdquo;, and &ldquo;IMAGINATION therefore is "
                  "nothing but decaying sense&rdquo;. The decay is an obscuring, as the "
                  "light of the Sun hides the stars by day, and as a man's voice is "
                  "lost in the noise of the day. When we want to name the thing itself "
                  "we say imagination, and when we want to say that it is fading and past "
                  "we say memory: &ldquo;So that Imagination and Memory, are but one thing, "
                  "which for divers considerations hath divers names.&rdquo; Then: "
                  "&ldquo;Much memory, or memory of many things, is called Experience.&rdquo; "
                  "Lesson 3 will put that to work."),
            ("p", "Dreams come next. Hobbes says the brain and nerves are benumbed in "
                  "sleep, so only the body's inward motions can start an image, and "
                  "&ldquo;lying cold breedeth Dreams of Feare&rdquo;. He then answers a "
                  "question that René Descartes had made famous, in the Meditations of "
                  "1641, to which Hobbes wrote one set of objections: how can one tell "
                  "waking from dreaming? His answer is modest. Many think it impossible "
                  "to tell exactly, but he is &ldquo;well satisfied, that being awake, I "
                  "know I dreame not; though when I dreame, I think my selfe awake.&rdquo; "
                  "His grounds are that in dreams he does not constantly think of the "
                  "same persons and places, nor remember so long a train of coherent "
                  "thoughts, and that &ldquo;waking I often observe the absurdity of "
                  "Dreames, but never dream of the absurdities of my waking "
                  "Thoughts&rdquo;. A critic will say that a dream can be perfectly "
                  "coherent, and Hobbes allows the case where a man does not notice "
                  "he has slept. His example is Brutus before Philippi, whose "
                  "apparition he takes to have been a short dream."),
            ("p", "Why does a book about the commonwealth have these pages? "
                  "Because the fears people have of apparitions are a way to govern them. "
                  "Hobbes says the fear of ghosts and fairies has been &ldquo;on purpose, "
                  "either taught, or not confuted, to keep in credit the use of "
                  "Exorcisme, of Crosses, of holy Water&rdquo;, and that if this "
                  "superstitious fear were taken away, &ldquo;men would be much more fitted "
                  "than they are for civill Obedience.&rdquo; Witches, he thinks, have no "
                  "real power, yet are &ldquo;justly punished, for the false beliefe they "
                  "have, that they can do such mischiefe&rdquo;. The schools, who should "
                  "have cleared the matter up, instead teach that imaginations rise of "
                  "themselves or are breathed in by God or the devil, or pass from the "
                  "senses to the common sense and on to the fancy and memory &ldquo;like "
                  "handing of things from one to another, with many words making nothing "
                  "understood.&rdquo; Next comes the train of imaginations, Chapter 3, "
                  "which is how one image leads to another."),
        ],
        "lab": ("argkit", {
            "mode": "validity",
            "preset": "echo",
            "show": "all",
            "presets": [
                {"id": "echo", "label": "If in the object, then not severable; severed; so not in the object",
                 "premises": ["a -> b", "~b"], "conclusion": "~a",
                 "expect": {"vaVerdict": "Valid", "vaCounter": "0", "vaForm": "modus tollens"}},
                {"id": "no-conditional", "label": "Severed, so not in the object, without the first premise",
                 "premises": ["~b"], "conclusion": "~a",
                 "expect": {"vaVerdict": "Invalid", "vaCounter": "1"}},
                {"id": "pressed", "label": "The eye pressed makes a light, so sense is a motion in us",
                 "premises": ["e"], "conclusion": "m",
                 "expect": {"vaVerdict": "Invalid", "vaCounter": "1"}},
                {"id": "analogy", "label": "The same with the analogy as a premise",
                 "premises": ["e", "e -> m"], "conclusion": "m",
                 "expect": {"vaVerdict": "Valid", "vaCounter": "0"}},
            ],
            "panel_title": "Hobbes's argument from the echo",
            "panel_intro": (
                "Each row is a case. A highlighted row makes every premise true and the "
                "conclusion false. In the echo preset there is none. Delete the first "
                "premise with the no-conditional preset and find the row that appears; "
                "then compare the pressed preset, where `e` is that pressing the eye makes "
                "us fancy a light and `m` is that sense is a motion in us, with the analogy "
                "preset that adds Hobbes's step."
            ),
        }),
        "steps_title": "Testing an argument against what it denies",
        "steps_intro": "Four moves, for any argument whose conclusion is a denial.",
        "steps": [
            ("Put the conclusion as a denial",
             "Here it is that colours and sounds are not in the objects. Give the "
             "thing denied a letter, `a`."),
            ("Write the test as a conditional",
             "If `a` were so, something else would follow: here, that the quality "
             "could not be severed from its object. Give that a letter, `b`."),
            ("Add the observation",
             "State what is seen: it is severed, as in the mirror and the echo. If the "
             "premises are the conditional and not `b`, the denial follows."),
            ("Ask which premise a critic would deny",
             "Delete each in turn in the lab and read the counterexample row. The row "
             "tells you what the critic must hold: that the quality can be in the "
             "object and carried from it, or that nothing has been severed."),
        ],
        "worked": {
            "title": "The echo, row by row",
            "intro": [
                "Take the echo preset: premises `a → b` and `¬b`, conclusion `¬a`. "
                "Two letters give four rows.",
            ],
            "lines": [
                "a true,  b true:   P2 (not b) false",
                "a true,  b false:  P1 (if a then b) false",
                "a false, b true:   P2 false",
                "a false, b false:  P1 true, P2 true, conclusion (not a) true",
            ],
            "after": [
                "Only the last row makes both premises true, and in it the conclusion "
                "is true. That is why there is no counterexample. Drop the first "
                "premise, as in the no-conditional preset, and the second row, where the "
                "colour is in the object and still severed, now has every premise "
                "true and the conclusion false.",
            ],
        },
        "quiz_title": "Sense, imagination and the echo",
        "quiz": [
            {"q": "On Hobbes's account in Chapter 2, what is imagination?",
             "a": ["A power that receives the species of things sent forth by objects",
                   "Nothing but decaying sense",
                   "A faculty that rises of itself and has no cause",
                   "A sense that works only in sleep"],
             "c": 1,
             "why": "He says &ldquo;IMAGINATION therefore is nothing but decaying sense&rdquo;, "
                    "found in men waking and sleeping. The species belong to the schools' "
                    "account of seeing, and the view that imaginations rise of themselves is "
                    "one he reports from the schools as a mistake."},
            {"q": "In the no-conditional preset the lab finds one counterexample row. What "
                  "does it describe?",
             "a": ["The colour is not in the object and it is not severed",
                   "The colour is in the object and it can nevertheless be shown apart "
                   "from it",
                   "The colour is not in the object and it is severed",
                   "The colour is in the object and cannot be severed"],
             "c": 1,
             "why": "The row makes `¬b` true (it is severed) and the conclusion `¬a` false "
                    "(the colour is in the object). It is the case the first premise, "
                    "that what is in the object cannot be severed, is there to rule out."},
            {"q": "How does Hobbes relate imagination and memory?",
             "a": ["Imagination is of things seen and memory of things heard",
                   "They are two faculties, one of images and one of judgement",
                   "They are one thing with two names, memory being the name when we "
                   "mean that the sense is fading and past",
                   "Memory is stronger than imagination because it is of things "
                   "that really happened"],
             "c": 2,
             "why": "He writes that &ldquo;Imagination and Memory, are but one thing, which for "
                    "divers considerations hath divers names&rdquo;. Memory expresses the "
                    "decay, and the other options give it a separate faculty or a "
                    "difference of strength that he does not claim."},
            {"q": "What test does Hobbes offer for knowing, when awake, that he is not "
                  "dreaming?",
             "a": ["Dreams are always dimmer than waking thoughts",
                   "In dreams he does not constantly think of the same persons and places, "
                   "nor remember a long coherent train, and he never dreams of the "
                   "absurdities of his waking thoughts",
                   "A man who is dreaming cannot think himself awake",
                   "The organs of sense are numb in waking and active in dreams"],
             "c": 1,
             "why": "These are his grounds. He says a dream &ldquo;must needs be more cleare&rdquo; "
                    "than waking thoughts, so the first is false. He also says that when he "
                    "dreams he thinks himself awake, so the third is false, and the organs "
                    "are benumbed in sleep, not in waking, so the last is false."},
        ],
        "mistakes": [
            ("Thinking Hobbes says the world is only appearance",
             "He says the object is real and is the cause of sense: it presses on the "
             "organ. What is only appearance is the colour or sound as we have it. In "
             "the object these qualities are &ldquo;so many several motions of the "
             "matter&rdquo;, and Hobbes does not say they are nothing."),
            ("Thinking a valid argument shows its conclusion",
             "The echo argument is valid, with no counterexample row. It shows that if "
             "colour were in the object it could not be shown apart from it, and that "
             "the mirror and echo do show it apart. A critic who denies either premise "
             "is not refuted by the table."),
            ("Treating imagination and memory as two faculties",
             "Hobbes says that &ldquo;Imagination and Memory, are but one thing&rdquo;. "
             "The same decaying sense is called imagination when we mean the image and "
             "memory when we mean that it is old. Experience, the next idea, is "
             "much memory."),
        ],
        "standard": (
            "Finish when you can set out the echo argument and say what denying each premise "
            "claims.",
            "Put Hobbes's argument that qualities are not in the object as premises, "
            "check the validity, and for each premise say what a critic who denied it "
            "would have to hold."
        ),
        "note": (
            "The lab shows that the echo argument is valid and what each denial would "
            "have to claim. It cannot say whether colour is in the object, which depends "
            "on what counts as a colour, nor whether a mirror severs a colour from a "
            "thing. Hobbes's physics is that of 1651; the lab does not test it."
        ),
    },
    # ---------------------------------------------------------------- 03
    # Leviathan ch. 3, 1651 p. 9; PDF p. 117 of the operator's copy (Chapter 3: PDF p. 116-120).
    {
        "slug": "the-train-of-imaginations",
        "title": "The Train of Imaginations",
        "module": "Chapter 3 · Of the Consequence or Trayne of Imaginations",
        "one_line": "Thoughts follow one another as they followed in sense, and prudence is a presumption from experience that can be strong and never certain.",
        "summary": (
            "Chapter 3 asks how one thought follows another. Without a purpose the train "
            "wanders; under a desire it seeks causes or effects. Foresight is a presumption "
            "from signs observed before, and the more often they are observed the less "
            "uncertain the sign. Model a man who has watched an assize and update his "
            "presumption one observation at a time; see how far experience carries."
        ),
        "key": [
            "train: one thought follows as in sense",
            "regulated train: seeks causes or effects",
            "prudence = presumption from experience",
            "sign: antecedent and consequent seen before",
            "more experience, less uncertain, never sure",
        ],
        "key_label": "Chapter 3 in five lines",
        "concepts_intro": (
            "Chapter 3 is five pages and has one idea: thought has an order, and the "
            "order is the order of experience."
        ),
        "concepts": [
            ("The train of thoughts",
             "Thoughts do not succeed one another at random. What followed together in "
             "sense follows together in imagination. Where there is no desire to govern "
             "the thoughts they wander, as in a dream, yet one can often trace the way. "
             "Under a desire the train is regulated and seeks either the causes of an "
             "effect, as man and beast do, or the effects of a cause, which Hobbes saw "
             "only in man."),
            ("Prudence as presumption",
             "Foresight, prudence or providence is a presumption of the future drawn "
             "from experience of the past. Hobbes says the conjecture is fallacious "
             "because all the circumstances cannot be observed, and that the more "
             "experience a man has the more prudent he is and the less often his "
             "expectation fails. He also says that in its own nature prudence is but "
             "presumption."),
            ("Signs",
             "A sign is the antecedent event of a consequent, and the consequent of the "
             "antecedent, when like consequences have been observed before. The oftener "
             "they have been observed the less uncertain the sign. The best natural prophet "
             "is the best guesser, the man most studied in the matter, who has the most "
             "signs to guess by."),
        ],
        "read_title": "The passage first, then the chapter line by line",
        "read_intro": (
            "The passage is Hobbes's own example of a wandering train, and it is "
            "the clearest in the chapter. After it the lesson goes through the "
            "regulated train and then to signs and prudence."
        ),
        "body": [
            ("p", "<strong>Chapter 3.</strong> &ldquo;For in a Discourse of our present "
                  "civill warre, what could seem more impertinent, than to ask (as one "
                  "did) what was the value of a Roman Penny? Yet the Cohaerence to me was "
                  "manifest enough. For the Thought of the warre, introduced the Thought "
                  "of the delivering up the King to his Enemies; The Thought of that, "
                  "brought in the Thought of the delivering up of Christ; and that again "
                  "the Thought of the 30 pence, which was the price of that treason: and "
                  "thence easily followed that malicious question; and all this in a "
                  "moment of time; for Thought is quick.&rdquo;"),
            ("p", "Read it as a piece of evidence. Hobbes had been in a conversation "
                  "about the war, and someone asked a question that seemed to have nothing to do "
                  "with it. He traced the chain: the King delivered up to his enemies, "
                  "most likely the Scots handing Charles to Parliament, which he does not "
                  "say; then Christ delivered up, then the thirty pence, then the "
                  "question what a Roman penny was worth. The sting is in the "
                  "last step, and Hobbes calls the question malicious. The general claim "
                  "is the point: &ldquo;Not every Thought to every Thought succeeds "
                  "indifferently.&rdquo; We have no transition from one imagination to "
                  "another &ldquo;whereof we never had the like before in our "
                  "Senses&rdquo;, because the motions that followed one another in sense "
                  "keep together afterwards, like water on a table drawn the way a "
                  "finger guides it."),
            ("p", "Two sorts of train follow. The first is unguided and wanders, with "
                  "no passionate thought to govern it, as in a dream or in the mind of a "
                  "man alone and careless. The second is &ldquo;regulated by some desire, "
                  "and designe&rdquo;: from the end desired comes the thought of means we "
                  "have seen produce the like, then means to that means, &ldquo;till we "
                  "come to some beginning within our own power&rdquo;. An old precept, "
                  "<em>Respice finem</em>, says to look often at what you want, because "
                  "that keeps the thoughts on the road. This regulated train is of two "
                  "kinds. In the one, seeing an effect, we seek its causes; this is common "
                  "to man and beast. In the other, imagining anything, we seek all the "
                  "possible effects, what we can do with it; and Hobbes says he has "
                  "&ldquo;not at any time seen any signe, but in man onely&rdquo;. "
                  "He calls it seeking, and likens it to a man sweeping a room for a "
                  "jewel, &ldquo;as a Spaniel ranges the field, till he finds a "
                  "sent&rdquo;."),
            ("p", "Now the case the lesson computes. A man wants to know what will "
                  "become of an offender, and &ldquo;re-cons what he has seen follow on "
                  "the like Crime before; having this order of thoughts, The Crime, the "
                  "Officer, the Prison, the Judge, and the Gallowes.&rdquo; This kind of "
                  "thought, Hobbes says, is called foresight, prudence or providence, "
                  "&ldquo;though such conjecture, through the difficulty of observing all "
                  "circumstances, be very fallacious&rdquo;. And he gives the reason: "
                  "&ldquo;The Present onely has a being in Nature&rdquo;; the past is in "
                  "memory and the future is &ldquo;a fiction of the mind, applying the "
                  "sequels of actions Past, to the actions that are Present&rdquo;. "
                  "&ldquo;And though it be called Prudence, when the Event answereth our "
                  "Expectation; yet in its own nature, it is but Presumption.&rdquo;"),
            ("p", "A sign is what makes the presumption. Hobbes defines it: &ldquo;A "
                  "Signe, is the Event Antecedent, of the Consequent; and contrarily, the "
                  "Consequent of the Antecedent, when the like Consequences have been "
                  "observed, before: And the oftner they have been observed, the lesse "
                  "uncertain is the Signe.&rdquo; He does not say how much less. To "
                  "see the shape of the claim, the lab uses a tool Hobbes did not have, "
                  "an exact update on a stated model, and says so plainly: the model is "
                  "written for this lesson. There are two possible benches, a severe one "
                  "that hangs four in five of the offenders brought before it and a "
                  "lenient one that hangs one in five. The man begins with no opinion, "
                  "half and half, and watches the court."),
            ("p", "After one hanging, the one preset gives the severe bench a chance of "
                  "`4/5`. The Bayes factor, the ratio of how likely the observation is on "
                  "each bench, is 4, and the chance that the next offender will hang is "
                  "`17/25`. After three hangings in a row, the three preset gives "
                  "`64/65` for the severe bench, a factor of 64, and a chance of `257/325` "
                  "that the next one hangs. A pardon in the middle takes much of that "
                  "away: in the mixed preset, two hangings and a pardon, the severe "
                  "bench is again at `4/5` with a factor of 4, no better than after one "
                  "hanging, because the pardon cancels one of the hangings. This is what "
                  "Hobbes means by experience: more observations leave the sign less "
                  "uncertain. It is not the number of observations but how they fall."),
            ("p", "The last preset shows how far experience carries. After six hangings "
                  "in a row the many preset puts the severe bench at `4096/4097`, which "
                  "is as good as certain, and yet the chance that the next offender "
                  "hangs is `3277/4097`, a little under four in five. Knowing the "
                  "court perfectly could not raise it above the court's own "
                  "four in five. That is Hobbes's point that conjecture is "
                  "&ldquo;fallacious&rdquo; even in the best-informed man. What experience "
                  "buys is a better presumption about the habit of the thing, and the "
                  "habit itself is only usually so. He adds the sentence that follows "
                  "from it: &ldquo;The best Prophet naturally is the best guesser; "
                  "and the best guesser, he that is most versed and studied in the "
                  "matters he guesses at: for he hath most Signes to guesse by.&rdquo; "
                  "Actual prophecy, he says, is supernatural."),
            ("p", "It is not prudence that sets man apart: &ldquo;Neverthelesse it is "
                  "not Prudence that distinguisheth man from beast.&rdquo; Some beasts at "
                  "a year old observe more, and pursue what is good for them more "
                  "prudently, than a child of ten. The same presumption looks backwards "
                  "too: a man who has seen how a flourishing state came to civil war "
                  "and ruin will guess the same course for another state whose ruins he "
                  "sees. The chapter ends on infinity: &ldquo;Whatsoever we imagine, is "
                  "Finite.&rdquo; Since every image began in sense, we cannot imagine the "
                  "infinite, and when we say a thing is infinite we mean only that we "
                  "cannot conceive its ends, &ldquo;having no Conception of the thing, but "
                  "of our own inability&rdquo;. The name of God, he says, is used not "
                  "to make us conceive him, but that we may honour him. The next lesson "
                  "is about how names, and the things that cannot be imagined, go wrong."),
            ("p", "A limit, and a reader who was not satisfied. David Hume, born "
                  "after Hobbes's death, asked what justifies presuming that the future "
                  "will be like the past, and Hobbes does not ask it. He says presumption "
                  "rests &ldquo;onely upon Experience&rdquo; and stops. The lab updates "
                  "within a model in which the court has one of two settled habits; it "
                  "takes for granted what Hume would question, that the habit of the "
                  "court stays the same."),
            ("p", "Chapter 3 shows how a thought follows a thought. Chapter 4, in the "
                  "next two lessons, is about the thing that lets a man do more with "
                  "that train than any beast can: speech."),
        ],
        "lab": ("choicekit", {
            "mode": "update",
            "preset": "one",
            "presets": [
                {"id": "one", "label": "One hanging",
                 "hyps": ["severe bench", "lenient bench"], "prior": ["1/2", "1/2"],
                 "outcomes": ["hanged", "pardoned"], "lik": [["4/5", "1/5"], ["1/5", "4/5"]],
                 "data": ["hanged"], "payoffs": None,
                 "expect": {"upPost": "4/5", "upBF": "4", "upPred": "17/25"}},
                {"id": "three", "label": "Three hangings in a row",
                 "hyps": ["severe bench", "lenient bench"], "prior": ["1/2", "1/2"],
                 "outcomes": ["hanged", "pardoned"], "lik": [["4/5", "1/5"], ["1/5", "4/5"]],
                 "data": ["hanged", "hanged", "hanged"], "payoffs": None,
                 "expect": {"upPost": "64/65", "upBF": "64", "upPred": "257/325"}},
                {"id": "mixed", "label": "Two hangings and a pardon",
                 "hyps": ["severe bench", "lenient bench"], "prior": ["1/2", "1/2"],
                 "outcomes": ["hanged", "pardoned"], "lik": [["4/5", "1/5"], ["1/5", "4/5"]],
                 "data": ["hanged", "hanged", "pardoned"], "payoffs": None,
                 "expect": {"upPost": "4/5", "upBF": "4", "upPred": "17/25"}},
                {"id": "many", "label": "Six hangings in a row",
                 "hyps": ["severe bench", "lenient bench"], "prior": ["1/2", "1/2"],
                 "outcomes": ["hanged", "pardoned"], "lik": [["4/5", "1/5"], ["1/5", "4/5"]],
                 "data": ["hanged", "hanged", "hanged", "hanged", "hanged", "hanged"], "payoffs": None,
                 "expect": {"upPost": "4096/4097", "upBF": "4096", "upPred": "3277/4097"}},
            ],
            "panel_title": "What a man learns from watching a court",
            "panel_intro": (
                "Two benches, one that hangs four in five offenders and one that hangs "
                "one in five, begin at one half each. The data are the outcomes the man "
                "has seen. Run the four presets in order and compare the tile for the "
                "severe bench with the tile for the next offender; the second never "
                "passes four fifths."
            ),
        }),
        "steps_title": "Updating a presumption on a sign",
        "steps_intro": "Five moves, for any presumption drawn from what has been seen before.",
        "steps": [
            ("State the habits that might be in play",
             "Here, a severe bench and a lenient one. They are the possibilities the "
             "man thinks there are, and the answer is only as good as the list."),
            ("Say how each habit would show itself",
             "For each, how likely each outcome is: the severe bench hangs four in five, "
             "the lenient one one in five. These are the likelihoods."),
            ("Start from what he thought before",
             "Half and half here. Say so, because a different start gives a "
             "different answer after a few observations."),
            ("Update on each observation in turn",
             "Multiply each habit's chance by how likely the outcome was on it, and "
             "divide by the total. The result is the new starting point for the next "
             "observation."),
            ("Predict the next, and compare",
             "The chance of the next outcome is each habit's chance times how likely "
             "it makes that outcome. Compare it with the likelihood of the "
             "best habit: it cannot pass it."),
        ],
        "worked": {
            "title": "One hanging, and three",
            "intro": [
                "Prior one half each. The severe bench hangs four in five, the lenient "
                "bench one in five. First, one hanging.",
            ],
            "lines": [
                "severe:  1/2 · 4/5 = 2/5     lenient:  1/2 · 1/5 = 1/10",
                "total:  2/5 + 1/10 = 1/2",
                "posterior severe:  (2/5) / (1/2) = 4/5",
                "next hanged:  4/5 · 4/5 + 1/5 · 1/5 = 17/25",
                "three hangings:  (4/5)³ = 64/125  against  (1/5)³ = 1/125",
                "posterior severe:  64 / (64 + 1) = 64/65",
            ],
            "after": [
                "Each hanging multiplies the odds by 4, so the odds are 4 after one, "
                "64 after three, and `4096` after six. The chance of the next hanging "
                "is `(64/65)·(4/5) + (1/65)·(1/5) = 257/325`, which is "
                "below `4/5`, and it approaches `4/5` and never reaches it.",
            ],
        },
        "quiz_title": "Presumption from experience",
        "quiz": [
            {"q": "In the one preset the man has seen one hanging. What is his chance "
                  "for the severe bench?",
             "a": ["1/2", "17/25", "64/65", "4/5"],
             "c": 3,
             "why": "The severe bench gives `1/2 · 4/5 = 2/5` and the lenient bench "
                    "`1/2 · 1/5 = 1/10`, a total of `1/2`, so the severe bench is "
                    "`(2/5)/(1/2) = 4/5`. The other figures are the prior, the chance of "
                    "the next hanging and the figure after three hangings."},
            {"q": "In the mixed preset the man sees two hangings and a pardon. How "
                  "does his view of the severe bench compare with the one preset?",
             "a": ["It is the same, because the pardon cancels one hanging",
                   "It is stronger, because there are more observations",
                   "It is weaker, because a pardon was seen",
                   "It cannot be computed because the evidence conflicts"],
             "c": 0,
             "why": "Two hangings multiply the odds by `4 · 4 = 16`; one pardon divides "
                    "them by 4, leaving 4, the same as after one hanging: `4/5`. "
                    "The count of observations is not what moves the answer; "
                    "how they fall is."},
            {"q": "In the many preset the severe bench is at 4096/4097, and the chance "
                  "that the next offender hangs is 3277/4097. Why is the second "
                  "figure so much smaller?",
             "a": ["Six observations are too few to trust",
                   "Even the severe bench hangs only four in five, and that "
                   "limits what the man can expect of the next case",
                   "The lab rounds the second figure down",
                   "The lenient bench still has a quarter of the weight"],
             "c": 1,
             "why": "The next offender hangs with chance `(4096/4097)·(4/5) + "
                    "(1/4097)·(1/5)`, which is below `4/5` however certain the "
                    "man is about the court. That is the sense in which Hobbes calls "
                    "such conjecture fallacious. The lab does not round, and the "
                    "lenient bench has `1/4097`, not a quarter."},
            {"q": "On Hobbes's account in Chapter 3, what makes one man more prudent "
                  "than another?",
             "a": ["A quicker natural wit",
                   "Supernatural knowledge of what God has willed",
                   "More experience of things past, and so more signs to guess by",
                   "A larger vocabulary"],
             "c": 2,
             "why": "He says that &ldquo;by how much one man has more experience of things "
                    "past, than another; by so much also he is more Prudent&rdquo;, and "
                    "that such a man is not equalled by any advantage of natural and "
                    "extemporary wit. Providence he assigns to God alone."},
        ],
        "mistakes": [
            ("Thinking more experience makes a prediction certain",
             "Hobbes says that the oftner a sign has been observed &ldquo;the lesse "
             "uncertain is the Signe&rdquo;, not that it becomes certain. In the many "
             "preset the man is as good as sure of the bench, and the next offender "
             "still hangs with chance `3277/4097`, because the bench itself is only "
             "usually severe."),
            ("Counting observations instead of reading them",
             "Two hangings and a pardon leave the severe bench where one hanging did, "
             "at `4/5`. What matters is how the observations fall, for and against."),
            ("Taking prudence for what distinguishes men from beasts",
             "Hobbes says the opposite: &ldquo;it is not Prudence that distinguisheth "
             "man from beast&rdquo;, and some beasts at a year old pursue their good "
             "more prudently than a child of ten. What he thinks is peculiar to man "
             "is the seeking of effects, and, as Chapter 4 says, speech."),
        ],
        "standard": (
            "Finish when you can update a presumption on a run of observations and say why "
            "it stops short of certainty.",
            "Given the habits that might be in play, their likelihoods and a run of "
            "observations, compute the chance of each habit and of the next outcome, and "
            "say what limits the second."
        ),
        "note": (
            "The lab updates on a model that the lesson wrote, with two benches and "
            "four-in-five odds; Hobbes gives no numbers, and the Bayes factor is a modern "
            "tool, not his. It shows how a presumption from experience behaves when the "
            "habit is fixed and the possibilities are listed. It cannot say whether the "
            "future resembles the past, nor whether the list of possibilities is complete."
        ),
    },
]

# Lessons 4 and 5, on levkit, configured from docs/leviathan/kit-report.md.
_VOCAB_SIMPLE = ["body", "living", "sensible", "rational", "peter-self", "observes-laws", "neighs"]

_VOCAB_DEFS = [
    ["living-creature", "body living sensible"],
    ["man", "living-creature rational"],
    ["horse", "living-creature neighs"],
    ["peter", "man peter-self"],
    ["just", "man observes-laws"],
]

LESSONS += [
    # ---------------------------------------------------------------- 04
    # Leviathan ch. 4, 1651 p. 12; PDF p. 120 of the operator's copy (Chapter 4 to its account of truth: PDF p. 120-123).
    {
        "slug": "speech-and-names",
        "title": "Of Speech",
        "module": "Chapter 4 · Of Speech",
        "one_line": "Speech is names and their connexion, and reasoning is a reckoning with names: a name of larger signification contains the smaller.",
        "summary": (
            "Chapter 4 calls speech the most noble invention and says what it is for: "
            "registering the consequences of thoughts, and signifying them to others. "
            "Names are proper or common, and nothing in the world is universal but names. "
            "Treat a name as the sum of the names it is made of, and compute which "
            "affirmations are true by the definitions."
        ),
        "key": [
            "speech = names and their connexion",
            "uses: register, signify, teach, please",
            "proper name: one thing; common: many",
            "nothing universal but names",
            "A is B: every part of B is a part of A",
        ],
        "key_label": "The first half of Chapter 4 in five lines",
        "concepts_intro": (
            "The first half of Chapter 4 says what speech is, what it is for, and how "
            "names are of different breadth."
        ),
        "concepts": [
            ("What speech is for",
             "Speech turns a train of thoughts into a train of words, for two "
             "commodities: registering the consequences of our thoughts, so that they "
             "need not be found again, and signifying them to others. Within those, "
             "four uses: to acquire arts, to teach and counsel, to make our wills "
             "known, and to please. Each has an abuse."),
            ("Proper and common names",
             "A proper name belongs to one thing, as Peter or this tree. A common name, "
             "man or horse, is one name for many things, which is why it is a universal. "
             "Hobbes says there is nothing in the world universal but names, since the "
             "things named are every one individual and singular."),
            ("Names of larger and smaller extent",
             "A larger name comprehends the less large: body comprehends man. Several "
             "words together can make one name, as the words for a man who keeps the "
             "laws of his country make one name, <em>just</em>. By imposing names we "
             "turn the reckoning of consequences of things into a reckoning of the "
             "consequences of appellations."),
        ],
        "read_title": "The passage first, then the chapter line by line",
        "read_intro": (
            "The passage is Hobbes's praise of speech. The rest of the lesson "
            "goes through his account of it up to the point where he asks what "
            "makes an affirmation true."
        ),
        "body": [
            ("p", "<strong>Chapter 4.</strong> &ldquo;But the most noble and profitable "
                  "invention of all other, was that of SPEECH, consisting of Names or "
                  "Appellations, and their Connexion; whereby men register their Thoughts; "
                  "recall them when they are past; and also declare them one to another "
                  "for mutuall utility and conversation; without which, there had been "
                  "amongst men, neither Common-wealth, nor Society, nor Contract, nor "
                  "Peace, no more than amongst Lyons, Bears, and Wolves.&rdquo;"),
            ("p", "Hobbes sets the passage against a rival. &ldquo;The Invention of "
                  "Printing, though ingenious, compared with the invention of Letters, is "
                  "no great matter.&rdquo; Letters first, whoever found them: he repeats "
                  "the story that Cadmus brought them into Greece, and says it is not "
                  "known who was first. But letters write speech down, and speech is "
                  "what makes men different from lions and wolves. Look at the "
                  "list of what is lost without it: commonwealth, society, contract, "
                  "peace. These are the book's subjects, and he has put them down as "
                  "consequences of a power to name. Its origin he leaves to Scripture: "
                  "&ldquo;The first author of Speech was God himself, that instructed "
                  "Adam how to name such creatures as he presented to his sight; For the "
                  "Scripture goeth no further in this matter.&rdquo; After that, need, the "
                  "mother of invention, did the rest, and the Tower of Babel explains the "
                  "tongues."),
            ("p", "The general use of speech, he says, is to transfer a train of thoughts "
                  "into a train of words, for two commodities. One is &ldquo;the Registring "
                  "of the Consequences of our Thoughts&rdquo;, since they slip out of "
                  "memory and would otherwise have to be worked out again, so that &ldquo;the "
                  "first use of names, is to serve for Markes, or Notes of remembrance&rdquo;. "
                  "The other is that when many use the same words they signify to one "
                  "another what they conceive, and then the names are called "
                  "&ldquo;Signes&rdquo;. Out of those come four special uses: to register "
                  "causes and effects, &ldquo;which in summe, is acquiring of Arts&rdquo;; "
                  "to &ldquo;Counsell, and Teach one another&rdquo;; &ldquo;to make known to "
                  "others our wills, and purposes&rdquo;; and &ldquo;to please and delight "
                  "our selves, and others, by playing with our words, for pleasure or "
                  "ornament, innocently.&rdquo; And four abuses answer them: registering "
                  "thoughts wrong &ldquo;by the inconstancy of the signification of their "
                  "words&rdquo;, using words &ldquo;metaphorically&rdquo; to deceive others, "
                  "declaring a will one does not have, and using words &ldquo;to grieve "
                  "one another&rdquo;."),
            ("p", "Then names. &ldquo;some are Proper, and singular to one onely thing; "
                  "as Peter, John, This man, this Tree&rdquo;, and some are common to many, "
                  "and these are universals, &ldquo;there being nothing in the world "
                  "Universall but Names; for the things named, are every one of them "
                  "Individuall and Singular.&rdquo; A universal name is imposed on many "
                  "things &ldquo;for their similitude in some quality, or other "
                  "accident&rdquo;. The schools had argued for centuries about whether "
                  "universals are real things or only names, and this is Hobbes's side of it, "
                  "stated in two sentences. A realist would answer that the similitude "
                  "among the things is itself something real that the name picks out. "
                  "Hobbes would reply that what the things share is a likeness, and a "
                  "likeness is not a further thing."),
            ("p", "Names also differ in breadth: &ldquo;the Name Body is of larger "
                  "signification than the word Man, and comprehendeth it&rdquo;. And a "
                  "name need not be one word. &ldquo;Hee that in his actions observeth the "
                  "Lawes of his Country, make but one Name, equivalent to this one word, "
                  "Just.&rdquo; This is what lets him say that by imposing names &ldquo;we "
                  "turn the reckoning of the consequences of things imagined in the mind, "
                  "into a reckoning of the consequences of Appellations.&rdquo; His "
                  "example is the triangle. A deaf man who sees that one triangle has "
                  "its angles equal to two right angles must look again at the next; the "
                  "man with words notes that it was only the straight sides and the three "
                  "angles that mattered, and writes &ldquo;Every triangle hath its three "
                  "angles equall to two right angles.&rdquo; The same holds of counting: "
                  "&ldquo;without words, there is no possibility of reckoning of "
                  "Numbers&rdquo;, and a man who cannot say the numerals in order may "
                  "&ldquo;observe every stroak of the Clock&rdquo; and never know what hour "
                  "it strikes."),
            ("p", "The lab turns the reckoning of appellations into one you can "
                  "check, on a model of the lesson's own. Each name is either simple, a "
                  "name the reckoning starts from, or defined as the sum of other names. "
                  "Expand every definition down to the simple names; an affirmation "
                  "<em>A is B</em> is then true when every simple name in B's "
                  "expansion is in A's, and false when not. This is the lab's reading of "
                  "Hobbes's rule in the next paragraph of the chapter, and it is only one "
                  "reading, because his sentence is short and runs on extent as much as on "
                  "parts. It has a consequence he does not state: a name with more parts "
                  "covers fewer things. The vocabulary is a sample written for this "
                  "lesson: living-creature is body, living and sensible; man is "
                  "living-creature and rational; horse is living-creature and neighs; "
                  "Peter is man and peter-self, a part only he has; just is man and "
                  "observes-laws."),
            ("p", "The vocab preset states six affirmations. Man is a living-creature, "
                  "true, because body, living and sensible are all in man. Peter is a "
                  "man, true. Man is Peter, false, for man lacks peter-self; a common "
                  "name does not name one thing. Horse is a man, false. Just is rational, "
                  "true, since a just man is a man and a man is rational. Man is just, "
                  "false, since not every man observes the laws. Three are true and "
                  "three false. The breadth preset reads the same pairs the other way "
                  "about: man is body is true and body is man is false, which is what "
                  "Hobbes means by a larger name comprehending the less large. "
                  "The compound preset defines Peter as a just man and checks that "
                  "Peter is just and Peter is a man, both true, while man is just "
                  "stays false. One limit of the lab is worth saying aloud. Hobbes calls "
                  "the names man and rational &ldquo;of equall extent, comprehending "
                  "mutually one another&rdquo;, and a model that reads names as bundles "
                  "of parts cannot show that: here rational is a part of man and not the "
                  "other way round."),
            ("p", "What is contested is whether this is all that meaning is. Critics "
                  "of the view that reasoning is only the reckoning of names have said "
                  "that it makes truth depend on how we choose to define our words, and "
                  "Hobbes comes close to saying so, as the next lesson shows. Others "
                  "have said that general names pick out real kinds in nature, which "
                  "would make the definitions answerable to something beyond the "
                  "speaker. What the lab can say is narrower: given definitions like "
                  "these, which affirmations follow."),
            ("p", "The next lesson takes the part of Chapter 4 where Hobbes says "
                  "what truth is, and what goes wrong when the definitions do."),
        ],
        "lab": ("levkit", {
            "mode": "reckon",
            "view": "names",
            "preset": "vocab",
            "presets": [
                {"id": "vocab", "label": "A sample vocabulary: man, horse, Peter, just",
                 "simple": _VOCAB_SIMPLE, "defs": _VOCAB_DEFS, "opposed": [],
                 "claims": [
                     ["c1", "man", "living-creature"],
                     ["c2", "peter", "man"],
                     ["c3", "man", "peter"],
                     ["c4", "horse", "man"],
                     ["c5", "just", "rational"],
                     ["c6", "man", "just"]],
                 "expect": {"lrkVerdicts": "c1 true; c2 true; c3 false; c4 false; c5 true; c6 false", "lrkCounts": "3 true, 3 false, 0 absurd, 0 insignificant"}},
                {"id": "breadth", "label": "A larger name and a smaller",
                 "simple": _VOCAB_SIMPLE, "defs": _VOCAB_DEFS, "opposed": [],
                 "claims": [
                     ["c1", "man", "body"],
                     ["c2", "body", "man"],
                     ["c3", "man", "living-creature"],
                     ["c4", "living-creature", "man"],
                     ["c5", "horse", "body"]],
                 "expect": {"lrkVerdicts": "c1 true; c2 false; c3 true; c4 false; c5 true", "lrkCounts": "3 true, 2 false, 0 absurd, 0 insignificant"}},
                {"id": "compound", "label": "Peter, a man who observes the laws",
                 "simple": _VOCAB_SIMPLE,
                 "defs": [d for d in _VOCAB_DEFS if d[0] != "peter"]
                         + [["peter", "just peter-self"]],
                 "opposed": [],
                 "claims": [
                     ["c1", "just", "man"],
                     ["c2", "man", "just"],
                     ["c3", "peter", "just"],
                     ["c4", "peter", "man"]],
                 "expect": {"lrkVerdicts": "c1 true; c2 false; c3 true; c4 true", "lrkCounts": "3 true, 1 false, 0 absurd, 0 insignificant"}},
            ],
            "panel_title": "Which affirmations follow from the definitions",
        }),
        "steps_title": "Reckoning with names",
        "steps_intro": "Four steps, for any small vocabulary and any affirmation about it.",
        "steps": [
            ("List the simple names",
             "These are the names the reckoning starts from and does not define: "
             "body, living, rational. Everything else will be reduced to them."),
            ("Define the rest as sums",
             "Write each other name as the sum of names it is made of. A proper name "
             "is a common name with one more part that only its bearer has."),
            ("Expand each name to its simple parts",
             "Replace every defined name by its definition until only simple names "
             "remain, and list them. A larger name has fewer parts."),
            ("Test the affirmation",
             "<em>A is B</em> is true when every simple part of B is among the "
             "parts of A. If one is missing, it is false, and the missing part says why."),
        ],
        "worked": {
            "title": "Man is a living-creature, and Peter is not just",
            "intro": [
                "Take the vocab preset's vocabulary. Expand the names that appear.",
            ],
            "lines": [
                "living-creature = body, living, sensible",
                "man = body, living, sensible, rational",
                "peter = body, living, sensible, rational, peter-self",
                "just = body, living, sensible, rational, observes-laws",
                "man is living-creature: 3 parts, all in man: true",
                "peter is just: observes-laws is not in peter: false",
            ],
            "after": [
                "The affirmation is false, and the lab says which part is missing. "
                "In the compound preset Peter is defined as just and peter-self, and "
                "then every part of just is in Peter, so the same affirmation is true.",
            ],
        },
        "quiz_title": "Names, breadth and affirmations",
        "quiz": [
            {"q": "In the vocab preset, which affirmation is false?",
             "a": ["Peter is a man",
                   "Just is rational",
                   "Man is a living-creature",
                   "Man is Peter"],
             "c": 3,
             "why": "Man lacks peter-self, which is a part of Peter, so every part of "
                    "Peter is not in man. The other three are true: Peter contains all of "
                    "man, a just man is a man and so rational, and man contains "
                    "living-creature."},
            {"q": "What does Hobbes say is universal?",
             "a": ["Names only, since every thing named is individual and singular",
                   "Things that are alike in some quality",
                   "The natures that names stand for",
                   "Nothing: even names are only singular sounds"],
             "c": 0,
             "why": "He writes that there is &ldquo;nothing in the world Universall but "
                    "Names; for the things named, are every one of them Individuall and "
                    "Singular&rdquo;. A universal name is imposed on many things for their "
                    "similitude, but the similitude is not a further universal thing."},
            {"q": "Hobbes gives four uses of speech. Which of these is one?",
             "a": ["To conceal our thoughts from our enemies",
                   "To make known to others our wills and purposes",
                   "To raise a likeness of an absent object in the senses",
                   "To prove that a thing exists"],
             "c": 1,
             "why": "The third use is &ldquo;to make known to others our wills, and "
                    "purposes, that we may have the mutuall help of one another&rdquo;. "
                    "Declaring a will one does not have is the third abuse, not a "
                    "use, and the other two options are not in his list."},
            {"q": "In the breadth preset, which pair of verdicts is right?",
             "a": ["Body is man: true; man is body: false",
                   "Man is body: true; body is man: false",
                   "Both are true, since man and body are alike",
                   "Both are false, since neither contains the other"],
             "c": 1,
             "why": "Body is a larger name and has fewer parts, so every part of body "
                    "is in man and man is body is true, while man has parts body "
                    "lacks and body is man is false. This is the sense of a name "
                    "that &ldquo;comprehendeth&rdquo; a smaller one."},
        ],
        "mistakes": [
            ("Reading <em>A is B</em> as symmetrical",
             "Man is a living-creature does not mean living-creature is a man. The "
             "lab tests the parts of B against the parts of A, in that order, "
             "and reversing the order changes the verdict, as the breadth preset "
             "shows."),
            ("Thinking a universal name names a universal thing",
             "Hobbes says the thing named is always individual and that a common name "
             "is imposed on many individuals for their likeness. A realist denies "
             "this, and the lesson states both."),
            ("Treating the lab's reading of a true affirmation as Hobbes's words",
             "His sentence is brief: if the later name signifies all that the former "
             "signifies, the affirmation is true. The lab's test, that every part of "
             "the predicate is in the subject, is one reading of it, and it cannot "
             "show what he says of man and rational being of equal extent."),
        ],
        "standard": (
            "Finish when you can say whether an affirmation is true from a list of definitions.",
            "Given a small vocabulary of simple names and defined names, expand each defined "
            "name, test an affirmation by the parts, and say which part is missing when it "
            "is false."
        ),
        "note": (
            "The lab shows which affirmations follow from the definitions written for this "
            "lesson, read as sums of names. It cannot say that these are the right "
            "definitions of man or just, nor that meaning is only a sum of parts. Hobbes's "
            "own test of an affirmation is in his sentence about the later name signifying "
            "all that the former signifies, and the lab's reading of it is one of "
            "several."
        ),
    },
    # ---------------------------------------------------------------- 05
    # Leviathan ch. 4, 1651 pp. 14-15; PDF p. 123 of the operator's copy (Chapter 4 from true and false to the end: PDF p. 123-127).
    {
        "slug": "truth-and-definitions",
        "title": "True and False, and Definitions",
        "module": "Chapter 4 · Of Speech",
        "one_line": "Truth is a matter of how names are ordered, so everything rests on definitions, and a name made of contradictory names signifies nothing.",
        "summary": (
            "The second half of Chapter 4 says that true and false belong to speech, "
            "that definitions come first in any reckoning, that one error in a "
            "definition multiplies, and that some names are only sounds. Change one "
            "definition in the vocabulary and see which affirmations change; then meet an "
            "absurd affirmation and an insignificant one."
        ),
        "key": [
            "true and false belong to speech, not things",
            "definitions first; errors multiply",
            "words are wise men's counters",
            "absurd: names that cannot be added",
            "insignificant: a name that names nothing",
        ],
        "key_label": "The rest of Chapter 4 in five lines",
        "concepts_intro": (
            "The second half of Chapter 4 draws the consequence of the first: if "
            "reasoning is reckoning with names, everything depends on what the "
            "names mean."
        ),
        "concepts": [
            ("Truth belongs to speech",
             "True and false are attributes of speech, not of things; where there is "
             "no speech there is neither truth nor falsehood, only error, as when we "
             "expect what shall not be. Truth is the right ordering of names in "
             "affirmations, so whoever seeks it must remember what each name stands "
             "for."),
            ("Definitions first",
             "Geometers begin by settling the significations of their words, and "
             "call that definition. An error in a definition is not one error: "
             "&ldquo;the errours of Definitions multiply themselves&rdquo; as the "
             "reckoning goes on. Words are wise men's counters and the money of fools."),
            ("Absurd and insignificant names",
             "All names but the positive and negative ones are insignificant sounds: "
             "either new names with no definition, or names put together from names "
             "whose significations contradict, like round quadrangle or incorporeal "
             "body. Names of virtues and vices are of inconstant signification, because "
             "men take them according to their passions."),
        ],
        "read_title": "The passage first, then the chapter line by line",
        "read_intro": (
            "The passage is Hobbes's definition of truth. After it the lesson goes "
            "through definitions, the kinds of names, and the sounds that are "
            "no names at all."
        ),
        "body": [
            ("p", "<strong>Chapter 4.</strong> &ldquo;When two Names are joyned together "
                  "into a Consequence, or Affirmation; as thus, A man is a living "
                  "creature; or thus, if he be a man, he is a living creature, If the "
                  "later name Living creature, signifie all that the former name Man "
                  "signifieth, then the affirmation, or consequence is true; otherwise "
                  "false. For True and False are attributes of Speech, not of Things. And "
                  "where Speech is not, there is neither Truth nor Falshood.&rdquo;"),
            ("p", "This is the sentence that the lab of the last lesson modelled. Read "
                  "what is claimed. Truth is not a relation between a sentence and the "
                  "world that a thing could have without anyone speaking: it is a "
                  "property of an ordering of names. And Hobbes draws the "
                  "consequence for animals and for mistakes: &ldquo;Errour there may be, "
                  "as when wee expect that which shall not be; or suspect what has not "
                  "been: but in neither case can a man be charged with Untruth.&rdquo; A "
                  "wrong expectation is an error, and not a lie, because no affirmation "
                  "was made."),
            ("p", "So a man who wants precise truth &ldquo;had need to remember what "
                  "every name he uses stands for&rdquo;, or he will be &ldquo;entangled in "
                  "words, as a bird in lime-twiggs; the more he struggles, the more "
                  "belimed.&rdquo; Geometry, he says, is &ldquo;the onely Science that it "
                  "hath pleased God hitherto to bestow on mankind&rdquo;, and it begins "
                  "by settling the significations of its words, which it calls "
                  "definitions, &ldquo;and place them in the beginning of their "
                  "reckoning.&rdquo; Then the reason: &ldquo;the errours of Definitions "
                  "multiply themselves, according as the reckoning proceeds&rdquo;. Men who "
                  "trust books add up many little sums into a greater without asking "
                  "whether the little sums were right. When the error shows they cannot "
                  "find it, and flutter over their books like birds in a room. "
                  "&ldquo;words are wise mens counters, they do but reckon by them: but "
                  "they are the mony of fooles, that value them by the authority of an "
                  "Aristotle, a Cicero, or a Thomas, or any other Doctor whatsoever, if "
                  "but a man.&rdquo; This was an attack on a way of teaching. In the "
                  "universities of 1651 philosophy meant, to a great extent, the reading "
                  "of Aristotle and the commentators on him."),
            ("p", "The lab's bad-definition preset makes the point in one line. "
                  "Take the vocabulary of the last lesson and define man as "
                  "living-creature alone, forgetting rational. Man is rational "
                  "flips from true to false. Peter is defined from man, so Peter is "
                  "rational flips too, and just, defined from man, so just is rational "
                  "flips as well. Three affirmations change because of one error, and "
                  "the claim man is a living-creature does not: it is still true. "
                  "That is what Hobbes means by errors that multiply. He adds that "
                  "&ldquo;between true Science, and erroneous Doctrines, Ignorance is in "
                  "the middle&rdquo;: the man who takes his instruction from the authority "
                  "of books is as far below the ignorant as the man of true science is "
                  "above him. And &ldquo;Naturall sense and imagination, are not "
                  "subject to absurdity&rdquo;, since absurdity is a fault of "
                  "speech."),
            ("p", "Then the account of what names are of. Names stand for what can "
                  "enter an account, to be added and subtracted; Hobbes notes that the "
                  "Latins called items in a bill <em>nomina</em>, names, and that the "
                  "Greeks had one word for speech and reason, &ldquo;not that they thought "
                  "there was no Speech without Reason; but no Reasoning without "
                  "Speech&rdquo;. Names are of four general kinds: of matter or body, "
                  "such as living or hot; of accidents, such as life or heat, which he "
                  "calls abstract names; of the properties of our own bodies, our fancies "
                  "of colour and sound; and names of names and of speeches, such as "
                  "universal and syllogism. There are also negative names, &ldquo;Nothing, "
                  "no man, infinite, indocible, three want foure&rdquo;, which are of use "
                  "in correcting a reckoning."),
            ("p", "&ldquo;All other Names, are but insignificant sounds&rdquo;, he says, "
                  "and of two sorts. One is a new name whose meaning is not explained by "
                  "definition, of which the schoolmen and puzzled philosophers have coined "
                  "an abundance, and he names &ldquo;Entity, Intentionality, Quiddity, and "
                  "other insignificant words of the School&rdquo;. The other is a name "
                  "made of two names whose significations contradict: &ldquo;an "
                  "incorporeall body, or (which is all one) an incorporeall "
                  "substance&rdquo;, or a &ldquo;round quadrangle&rdquo;, which is &ldquo;a "
                  "meere sound&rdquo;. The lab keeps these apart. In the "
                  "absurd-and-empty preset round and quadrangle are declared opposed, so "
                  "that they cannot be added, and the affirmation round-quadrangle is "
                  "man is absurd; and quiddity is a name with no definition and "
                  "not simple, so quiddity is man is insignificant. They are not "
                  "false, and they differ from one another: the first adds names that "
                  "cannot be added and the second has a name that stands for nothing. Hobbes "
                  "himself says that when an affirmation is false the two names put "
                  "together signify nothing. The lab does not go as far as that: it "
                  "keeps three verdicts apart, true or false by the parts, absurd, and "
                  "insignificant, as the lesson's own distinction."),
            ("p", "The stakes were not only in the schools. To say that an "
                  "&ldquo;incorporeall substance&rdquo; is a contradiction in terms is "
                  "to deny the existence of immaterial spirits, as Hobbes's "
                  "contemporaries understood at once. Bishop Bramhall, who had "
                  "debated freedom with him in Paris and answered <em>Leviathan</em> "
                  "in 1658, read it as a step towards atheism, and Hobbes in later "
                  "chapters says carefully what he means by spirit. The lab can "
                  "say only what follows once the pair is declared opposed. The "
                  "objection is that the names were not contradictory to begin with: "
                  "those who hold that there are immaterial substances deny that "
                  "incorporeal and substance cannot be added. That is a dispute about "
                  "the definitions, not a result of the lab."),
            ("p", "Last, the names of the passions. &ldquo;For one man calleth "
                  "Wisedome, what another calleth feare; and one cruelty, what another "
                  "justice; one prodigality, what another magnanimity; and one gravity, "
                  "what another stupidity.&rdquo; Such names have a signification of the "
                  "speaker's nature and interest, and so &ldquo;can never be true grounds "
                  "of any ratiocination&rdquo;. Two presets show the effect on one name. In "
                  "just-by-law, just is man and observes-laws, Peter is a man who "
                  "observes the laws, and Peter is just is true. In just-by-might, just "
                  "is man and yields-to-the-strongest, Peter is the same man, and Peter "
                  "is just is false. The words are the same, the man is the same, "
                  "and the verdict is opposite. Understanding, Hobbes adds, is "
                  "&ldquo;conception caused by Speech&rdquo;, so of absurd universal "
                  "affirmations &ldquo;there can be no Understanding; though many think "
                  "they understand, then, when they do but repeat the words "
                  "softly&rdquo;."),
            ("p", "Chapter 4 ends the first course. The next, Reason, Science and the "
                  "Passions, begins with Chapter 5, where reason is defined as exactly the "
                  "reckoning this chapter prepared."),
        ],
        "lab": ("levkit", {
            "mode": "reckon",
            "view": "names",
            "preset": "bad-definition",
            "presets": [
                {"id": "bad-definition", "label": "Man defined without rational",
                 "simple": _VOCAB_SIMPLE,
                 "defs": [["living-creature", "body living sensible"],
                          ["man", "living-creature"],
                          ["peter", "man peter-self"],
                          ["just", "man observes-laws"]],
                 "opposed": [],
                 "claims": [
                     ["c1", "man", "living-creature"],
                     ["c2", "man", "rational"],
                     ["c3", "peter", "rational"],
                     ["c4", "just", "rational"]],
                 "expect": {"lrkVerdicts": "c1 true; c2 false; c3 false; c4 false", "lrkCounts": "1 true, 3 false, 0 absurd, 0 insignificant"}},
                {"id": "absurd-and-empty", "label": "A round quadrangle and a quiddity",
                 "simple": _VOCAB_SIMPLE + ["round", "quadrangle"],
                 "defs": _VOCAB_DEFS + [["round-quadrangle", "round quadrangle"]],
                 "opposed": [["round", "quadrangle"]],
                 "claims": [
                     ["c1", "man", "living-creature"],
                     ["c2", "man", "horse"],
                     ["c3", "round-quadrangle", "man"],
                     ["c4", "quiddity", "man"]],
                 "expect": {"lrkVerdicts": "c1 true; c2 false; c3 absurd; c4 insignificant", "lrkCounts": "1 true, 1 false, 1 absurd, 1 insignificant"}},
                {"id": "just-by-law", "label": "Just as Hobbes's keeper of the laws",
                 "simple": _VOCAB_SIMPLE,
                 "defs": [["living-creature", "body living sensible"],
                          ["man", "living-creature rational"],
                          ["peter", "man peter-self observes-laws"],
                          ["just", "man observes-laws"]],
                 "opposed": [],
                 "claims": [["c1", "peter", "just"]],
                 "expect": {"lrkVerdicts": "c1 true", "lrkCounts": "1 true, 0 false, 0 absurd, 0 insignificant"}},
                {"id": "just-by-might", "label": "Just as one who yields to the strongest",
                 "simple": _VOCAB_SIMPLE + ["yields-to-the-strongest"],
                 "defs": [["living-creature", "body living sensible"],
                          ["man", "living-creature rational"],
                          ["peter", "man peter-self observes-laws"],
                          ["just", "man yields-to-the-strongest"]],
                 "opposed": [],
                 "claims": [["c1", "peter", "just"]],
                 "expect": {"lrkVerdicts": "c1 false", "lrkCounts": "0 true, 1 false, 0 absurd, 0 insignificant"}},
            ],
            "panel_title": "What changes when a definition does",
        }),
        "steps_title": "Checking a reckoning for bad names",
        "steps_intro": "Five steps, before trusting any chain of affirmations.",
        "steps": [
            ("Ask what each name is defined as",
             "If a name has no definition and is not one of the starting names, "
             "stop. The affirmation is insignificant, and nothing follows from it."),
            ("Check that the parts can be added",
             "If the expansions of subject, predicate or both contain a pair that "
             "cannot be added, the affirmation is absurd, whatever else it says."),
            ("Test the affirmation by its parts",
             "Otherwise the verdict is true or false, by whether every part of the "
             "predicate is among the parts of the subject."),
            ("Trace an error to its dependants",
             "If a definition is wrong, list every name defined from it. Each "
             "affirmation about them may change, and that is how one error multiplies."),
            ("Ask whose definition it is",
             "Where the name is one of virtue or vice, check which meaning each "
             "speaker gives it. If they differ, the same sentence has two verdicts."),
        ],
        "worked": {
            "title": "One wrong definition, three changed verdicts",
            "intro": [
                "Take the bad-definition preset. Man is defined as living-creature only. "
                "Peter is man with peter-self, and just is man with observes-laws.",
            ],
            "lines": [
                "man = body, living, sensible",
                "peter = body, living, sensible, peter-self",
                "just = body, living, sensible, observes-laws",
                "man is living-creature: true (unchanged)",
                "man is rational: false (was true)",
                "peter is rational, just is rational: false (were true)",
            ],
            "after": [
                "One omitted part changes three of four verdicts, and all three "
                "were about names defined from man. The lab shows the error "
                "multiplying along the definitions. Which of the two sets of "
                "definitions is right is not something it can decide.",
            ],
        },
        "quiz_title": "Truth, definitions and empty names",
        "quiz": [
            {"q": "In the bad-definition preset, how many of the four affirmations are true?",
             "a": ["One", "Four", "Three", "None"],
             "c": 0,
             "why": "Only man is living-creature stays true, since man still contains body, "
                    "living and sensible. Man, Peter and just are no longer rational, "
                    "because rational was left out of man and the other two are defined "
                    "from man."},
            {"q": "In the absurd-and-empty preset, why is round-quadrangle is man absurd "
                  "and not merely false?",
             "a": ["Because a quadrangle is not a man",
                   "Because it has a name with no definition",
                   "Because round and quadrangle are declared opposed and cannot be added "
                   "into one name",
                   "Because Hobbes says every false affirmation is absurd"],
             "c": 2,
             "why": "The lab marks an affirmation absurd when an expansion contains a pair "
                    "declared opposed, as round and quadrangle are. The second option "
                    "describes the other verdict, insignificant, which is quiddity is man; "
                    "and Hobbes says a false affirmation makes its names signify nothing, "
                    "not that it is absurd."},
            {"q": "What does Hobbes say true and false are attributes of?",
             "a": ["Things, which are true or false copies of their ideas",
                   "Thoughts, which are true or false as they match their objects",
                   "God's word alone",
                   "Speech, so where there is no speech there is neither truth nor falsehood"],
             "c": 3,
             "why": "He writes &ldquo;True and False are attributes of Speech, not of "
                    "Things. And where Speech is not, there is neither Truth nor "
                    "Falshood.&rdquo; He allows error where speech is absent, as in a "
                    "mistaken expectation, but not untruth."},
            {"q": "In the two just presets, Peter is the same man. What explains the "
                  "different verdicts on Peter is just?",
             "a": ["The lab is inconsistent",
                   "Peter changed between the presets",
                   "The name just is defined differently, and Peter is tested against "
                   "each definition",
                   "Peter is just is neither true nor false in either"],
             "c": 2,
             "why": "In just-by-law just needs observes-laws, which Peter has; in "
                    "just-by-might it needs yields-to-the-strongest, which he lacks. "
                    "Hobbes's example is names that a man takes according to his own "
                    "passions: one calls cruelty what another calls justice."},
        ],
        "mistakes": [
            ("Thinking an absurd affirmation is just a false one",
             "A false affirmation can be sensible: man is a horse is false, and one "
             "could understand it. An absurd one adds names that cannot be added, "
             "as round and quadrangle, and an insignificant one has a name that "
             "stands for nothing. The lab keeps the three apart."),
            ("Taking an error in a definition for one error",
             "Hobbes says the errors of definitions multiply as the reckoning proceeds. "
             "In the bad-definition preset one omitted part changes three verdicts, "
             "because every name defined from man inherits the omission."),
            ("Concluding that the lab shows there are no incorporeal substances",
             "It shows that if incorporeal and body are declared opposed, then a "
             "name joining them is absurd. Whether they are opposed is what "
             "defenders of immaterial substances deny, and Hobbes argues it "
             "in later chapters."),
        ],
        "standard": (
            "Finish when you can classify an affirmation as true, false, absurd or insignificant "
            "from the definitions.",
            "Given a vocabulary, opposed pairs and an affirmation, say whether it is true, false, "
            "absurd or insignificant, and trace how one change of definition changes the rest."
        ),
        "note": (
            "The lab classifies affirmations by the definitions and the opposed pairs the "
            "lesson states. It cannot say which definitions are right, whether incorporeal "
            "and body cannot be added, or whether truth is only a matter of the ordering of "
            "names. Those are what Chapter 4 argues and its critics dispute, and Hobbes's "
            "later chapters return to them."
        ),
    },
]
