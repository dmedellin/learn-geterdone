# -*- coding: utf-8 -*-
"""Lessons three and four of Small Words and Comparisons.

Every figure is read off the lab with labcheck.js --observe.

Happily, Simply, Truly (wordrule, list ly): 153 adjectives that are only
adjectives; 126 have an -ly adverb in the dictionary. Plain +ly 98 of 126
(77.8%); the five changes 126 of 126 (100.0%); 27 of 153 with none. The 28
plain misses sort as: -y 7 (angry, crazy, extraordinary, guilty, healthy,
lazy, necessary); -le 12; -ic 8; tall 1 (right under the changes only because
the changed spelling, tally, is a word).

Give It Up, Not Give Up It (phrasal): novel 473 lines, commonest five go away
32, sit down 29, find out 20, come back 16, give up 12; 34 with the pronoun
between, 8 with it after, 81.0%; 347 verb, preposition, pronoun lines. Play
149 lines, sit down 11, go out 9, break off 8, pick up 7, come up 5; 16
between, 5 after, 76.2%; 93 preposition lines. The 8 and 5 'after' rows were
read by eye in the lab's table: none puts a pronoun object after a particle.

Spoken forms: content/spoken/english_c7_small_words.py.
"""

LESSONS = [
    {
        "slug": "happily-simply-truly",
        "module": "Making an adverb",
        "title": "Happily, Simply, Truly: Making an Adverb",
        "one_line": "Add -ly, and the rule is right on four words in five; five spelling changes fix the rest.",
        "standard": (
            "Finish when you can make the -ly adverb from an adjective and say when there is none.",
            "You should be able to apply the five spelling changes, read the "
            "rule's score against a dictionary, sort the words that adding "
            "-ly alone gets wrong by their endings, and name adjectives that "
            "have no -ly adverb.",
        ),
        "summary": (
            "The usual rule is to add <em>-ly</em>. On the 126 <dfn>adjectives</dfn> in "
            "this lab that have an <em>-ly</em> adverb, that is right 98 times. "
            "The 28 words it gets wrong end in three ways, and five spelling "
            "changes turn all 126 right. Another 27 adjectives have no "
            "<em>-ly</em> adverb the <dfn>dictionary</dfn> knows, and they are worth "
            "learning as a short list."
        ),
        "key_label": "The same 126 adjectives, two rules",
        "key": [
            "add ly              98 of 126    77.8%",
            "add ly with changes 126 of 126  100.0%",
            "",
            "angry      angrily",
            "capable    capably",
            "dramatic   dramatically",
            "27 of 153 have no ly adverb",
        ],
        "concepts_intro": "Three ideas. The last is about words the rule cannot touch.",
        "concepts": (
            (
                "Adding -ly is a rule with about a fifth missing",
                "Run it on the list and it is right on 98 of 126, which is "
                "77.8%. The 28 it gets wrong are not spread about at random. Twelve end in "
                "<em>-le</em>, eight in <em>-ic</em>, seven in <em>-y</em>, "
                "and one is <em>tall</em>.",
            ),
            (
                "Each ending has its own change",
                "<em>-y</em> becomes <em>-ily</em>, <em>-le</em> becomes "
                "<em>-ly</em>, <em>-ic</em> becomes <em>-ically</em>, <em>-ue</em> "
                "becomes <em>-uly</em>, and <em>-ll</em> becomes <em>-lly</em>. "
                "With these the rule is right on all 126. Two of the five are "
                "hardly tested: no word in the list ends in <em>-ue</em>, and "
                "the only one that ends in <em>-ll</em> is <em>tall</em>.",
            ),
            (
                "Some adjectives have no -ly adverb",
                "27 of the 153 have none in the dictionary. Some end in "
                "<em>-ly</em> already, some are about a person's state, some "
                "name a place or a kind of thing, and two are not adjectives at "
                "all. The list is short enough to read in a minute.",
            ),
        ),
        "steps_title": "Making the adverb from an adjective in front of you",
        "steps_intro": "Look at the ending first.",
        "steps": (
            (
                "Does the adjective already end in -ly?",
                "Then stop. <em>Elderly</em>, <em>ugly</em> and "
                "<em>unlikely</em> are adjectives and have no adverb of this kind.",
            ),
            (
                "Does it end in -y?",
                "Change the <em>y</em> to <em>i</em> and add <em>-ly</em>: "
                "<em>angry</em> becomes <em>angrily</em>.",
            ),
            (
                "Does it end in a consonant and -le?",
                "Change the <em>-le</em> to <em>-ly</em>: "
                "<em>capable</em> becomes <em>capably</em>.",
            ),
            (
                "Does it end in -ic?",
                "Add <em>-ally</em>: <em>dramatic</em> becomes "
                "<em>dramatically</em>. <em>Public</em> is the one that takes "
                "plain <em>-ly</em>.",
            ),
            (
                "Otherwise add -ly",
                "<em>Careful</em> becomes <em>carefully</em>. A word ending "
                "<em>-ue</em> loses the <em>e</em> (<em>true</em>, "
                "<em>truly</em>), and a word ending <em>-ll</em> loses one "
                "<em>l</em> (<em>full</em>, <em>fully</em>).",
            ),
        ),
        "lab": ("english", {
            "mode": "wordrule",
            "list": "ly",
            "rule": "plain",
            "show": "misses",
            "panel_title": "Score the rule on 153 adjectives",
            "panel_intro": (
                "These are the words in the word list that are adjectives and "
                "nothing else, so a form like <em>fast</em> that is also an "
                "adverb is not here. The sorting was done at build time from a "
                "list of parts of speech, and it is not perfect: two of the 153, "
                "<em>through</em> and <em>toward</em>, are not adjectives in "
                "ordinary use, and the lesson names them. Each word is checked "
                "against a dictionary of real spellings. Choose a rule and read "
                "the table: it shows the "
                "adjective, the spelling the rule makes and the spelling the "
                "dictionary has. The last list shows the adjectives that have "
                "no <em>-ly</em> adverb there."
            ),
        }),
        "read_title": "The 28 words that adding -ly gets wrong",
        "read_intro": (
            "Switch the rule from the plain one to the one with changes, and "
            "the table of misses is empty. Switch back, and read it."
        ),
        "worked": {
            "title": "Five adjectives from the list, five ways",
            "intro": [
                "Each line is a row of the lab's table: the adjective, the "
                "change, and the adverb.",
            ],
            "lines": [
                "angry      y becomes ily       angrily",
                "capable    le becomes ly       capably",
                "dramatic   ic becomes ically   dramatically",
                "guilty     y becomes ily       guiltily",
                "careful    add ly              carefully",
            ],
            "after": [
                "Each of the first four is a miss for plain <em>-ly</em>: "
                "<em>angryly</em>, <em>capablely</em>, <em>dramaticly</em> and "
                "<em>guiltyly</em> are spellings nobody writes. Sorted by "
                "ending, the 28 misses are <em>-le</em> 12 (<em>acceptable</em>, "
                "<em>comfortable</em>, <em>horrible</em>, <em>terrible</em> and "
                "eight more), <em>-ic</em> 8 (<em>democratic</em>, "
                "<em>economic</em>, <em>historic</em>, <em>scientific</em> and "
                "four more), <em>-y</em> 7 (<em>angry</em>, <em>crazy</em>, "
                "<em>lazy</em>, <em>necessary</em> and three more) and "
                "<em>tall</em>.",
                "<em>Tall</em> deserves a warning. The dictionary has "
                "<em>tally</em>, which is what the <em>-ll</em> change makes, "
                "and so the lab counts <em>tall</em> as right. <em>Tally</em> is a "
                "different word and no one says <em>tally</em> for <em>tall</em>. "
                "The check shows that a spelling is a word, not that it is "
                "this word. <em>Unlike</em> is the same case: adding <em>-ly</em> "
                "makes <em>unlikely</em>, which is a word, and is an adjective "
                "and not the adverb of <em>unlike</em>.",
            ],
        },
        "note": (
            "The lab reads spellings and not meanings. The dictionary confirms "
            "that <em>hardly</em>, <em>lately</em> and <em>highly</em> are "
            "words. It cannot say that they do not mean <em>hard</em>, "
            "<em>late</em> and <em>high</em>, and the adverbs that look just "
            "like the adjective (<em>fast</em>, <em>hard</em>) are named here "
            "and not counted. <em>Happy</em>, <em>simple</em>, <em>basic</em>, "
            "<em>true</em> and <em>full</em> are not in the list either, because "
            "the word list also files them under another part of speech; the "
            "rules above are the same for them."
        ),
        "mistakes": (
            (
                "Adding -ly and thinking you are done",
                "<em>Angryly</em>, <em>capablely</em> and <em>dramaticly</em> "
                "are what adding <em>-ly</em> alone makes, and it makes 28 such "
                "spellings in this list. The ending of the adjective tells you "
                "the change. <em>Public</em> is the one word that ends in "
                "<em>-ic</em> and does not take <em>-ally</em>: the adverb is "
                "<em>publicly</em>. It is not in the printed list, so the lab "
                "does not count it.",
            ),
            (
                "Thinking every word that ends in -ly is an adverb",
                "<em>Elderly</em>, <em>ugly</em> and <em>unlikely</em> are in "
                "the list of adjectives with no <em>-ly</em> adverb. "
                "<em>Friendly</em> is an adjective too. The "
                "ending alone does not tell you the part of speech.",
            ),
            (
                "Trusting a dictionary check to tell you the meaning",
                "A check that finds <em>hardly</em> in the dictionary shows "
                "that the word exists. It does not show that <em>hardly</em> is "
                "the adverb of <em>hard</em>. It is not: <em>hardly</em> means "
                "almost not. The same holds for <em>lately</em> and "
                "<em>highly</em>.",
            ),
        ),
        "quiz_title": "Check yourself",
        "quiz": (
            {
                "q": "Which is the <em>-ly</em> adverb of <em>capable</em>?",
                "a": ["capablely", "capablly", "capabley", "capably"],
                "c": 3,
                "why": (
                    "<em>Capably</em>. The ending <em>-le</em> becomes "
                    "<em>-ly</em>. The other three are what adding "
                    "<em>-ly</em> or dropping one letter wrongly makes."
                ),
            },
            {
                "q": "Adding <em>-ly</em> alone gets 28 of the 126 wrong. "
                     "Which ending accounts for the most of them?",
                "a": ["<em>-y</em>", "<em>-ic</em>", "<em>-le</em>", "<em>-ll</em>"],
                "c": 2,
                "why": (
                    "<em>-le</em> accounts for 12. <em>-ic</em> has 8, "
                    "<em>-y</em> has 7 and <em>-ll</em> has one, <em>tall</em>."
                ),
            },
            {
                "q": "Which of these words ends in <em>-ly</em> and is an "
                     "adjective, not an adverb?",
                "a": ["quickly", "elderly", "happily", "angrily"],
                "c": 1,
                "why": (
                    "<em>Elderly</em> is an adjective, and it is one of the 27 "
                    "words in the lab's list with no adverb. The other three "
                    "are adverbs made from <em>quick</em>, <em>happy</em> and "
                    "<em>angry</em>."
                ),
            },
            {
                "q": "Why can the dictionary check not tell that <em>hardly</em> "
                     "is not the adverb of <em>hard</em>?",
                "a": [
                    "It shows that a spelling is a word, not what the word means",
                    "It only holds words from the novel",
                    "It does not have the word <em>hard</em>",
                    "It checks sounds and not spellings",
                ],
                "c": 0,
                "why": (
                    "The check asks whether a spelling is in the dictionary. "
                    "<em>Hardly</em> is, and so the check passes it, though the "
                    "meaning is different. The lab says so in its limit "
                    "sentence."
                ),
            },
        ),
        "body": [
            ("p",
             "An <dfn>adjective</dfn> says what a thing is like. An <dfn>adverb</dfn> says "
             "how, when or how much, and many <dfn>adverbs</dfn> are made from an "
             "adjective by adding <em>-ly</em>: <em>careful</em>, "
             "<em>carefully</em>. That is the rule you were given. This lesson "
             "scores it."),
            ("p",
             "The list is every word in the 2,800 that a list of parts of speech "
             "tags as an adjective and nothing else, 153 in all; the list is "
             "not perfect, and its two mistakes are named below. A dictionary was asked for the "
             "<em>-ly</em> spellings of each. For 126 of them there is at least "
             "one. For the other 27 there is none."),
            ("h3", "Adding -ly"),
            ("p",
             "Add <em>-ly</em> to the 126 and compare with the dictionary. "
             "98 come out right, which is 77.8%. The 28 that come out wrong are "
             "not odd words. <em>Terrible</em>, <em>comfortable</em>, "
             "<em>necessary</em>, <em>economic</em>: they are ordinary words, "
             "and the rule makes <em>terriblely</em> and <em>economicly</em> "
             "out of them."),
            ("h3", "Five changes"),
            ("p",
             "The failures group by ending, and each ending has a change. "
             "A word that ends in <em>-y</em> after a <dfn>consonant</dfn> turns the "
             "<em>y</em> into <em>i</em>: <em>angry</em> becomes "
             "<em>angrily</em>. A word ending in <em>-le</em> changes it "
             "to <em>-ly</em>: <em>capable</em> becomes <em>capably</em>. A word "
             "ending in <em>-ic</em> takes <em>-ally</em>: <em>dramatic</em> "
             "becomes <em>dramatically</em>. A word ending in <em>-ue</em> "
             "loses the <em>e</em>: <em>true</em> becomes <em>truly</em>. A "
             "word ending in <em>-ll</em> loses one <em>l</em>: <em>full</em> "
             "becomes <em>fully</em>."),
            ("p",
             "With the five changes the rule is right on 126 of 126, which is "
             "100.0%. That is an honest 100% with three limits. No word in the "
             "list ends in <em>-ue</em>, so that change is never tested. The "
             "only <em>-ll</em> word is <em>tall</em>, which the check passes "
             "because <em>tally</em> is a word. And <em>unlike</em> is in the "
             "list, and its spelling with <em>-ly</em>, <em>unlikely</em>, is a "
             "word too, but an adjective."),
            ("h3", "Adjectives with no -ly adverb"),
            ("p",
             "27 of the 153 have no <em>-ly</em> adverb in the dictionary. "
             "Three already end in <em>-ly</em>: <em>elderly</em>, <em>ugly</em> "
             "and <em>unlikely</em>. Six are about the state of a person or a "
             "thing: <em>afraid</em>, <em>alive</em>, <em>aware</em>, "
             "<em>pregnant</em>, <em>sorry</em> and <em>unable</em>. Eleven "
             "name a place or a kind: <em>eastern</em>, <em>northern</em>, "
             "<em>southern</em>, <em>rural</em>, <em>solar</em>, "
             "<em>nuclear</em>, <em>literary</em>, <em>corporate</em>, "
             "<em>agricultural</em>, <em>institutional</em> and "
             "<em>everyday</em>. Five that remain are "
             "<em>available</em>, <em>difficult</em>, <em>foreign</em>, "
             "<em>numerous</em> and <em>unclear</em>. The last two, "
             "<em>through</em> and <em>toward</em>, are not adjectives in any "
             "ordinary use: the list of parts of speech that picked the 153 tags "
             "them so, and they are set aside here by name."),
            ("p",
             "When you want an adverb for one of these, you do not make one. "
             "You say it with other words: not an adverb of <em>difficult</em> "
             "but <em>with difficulty</em>, and not an adverb of <em>foreign</em> "
             "but <em>in a foreign way</em>."),
            ("h3", "What the check cannot see"),
            ("p",
             "The dictionary confirms that <em>hardly</em>, <em>lately</em> and "
             "<em>highly</em> are words. It cannot say that none of them means "
             "what <em>hard</em>, <em>late</em> or <em>high</em> means when "
             "used as an adverb. <em>Fast</em> and <em>hard</em> are adverbs "
             "with no ending at all. Those are named here and not counted."),
        ],
    },
    {
        "slug": "give-it-up-not-give-up-it",
        "module": "Prepositions and particles",
        "title": "Give It Up, Not Give Up It",
        "one_line": "Where a pronoun goes tells you whether the small word is a particle or a preposition.",
        "standard": (
            "Finish when you can place a pronoun with a verb and a small word, and say why.",
            "You should be able to tell a particle from a preposition by where "
            "the pronoun goes, read the rule's score off the printed lines, "
            "explain the lines that look like exceptions, and name the phrasal "
            "verbs a text uses most.",
        ),
        "summary": (
            "<em>Find it out</em>, but <em>look at it</em>. Both are a verb and a "
            "small word, and the pronoun goes in a different place. In "
            "473 lines of the novel, the <dfn>pronoun</dfn> stands between the verb and "
            "the small word 34 times and after it 8, and the 8 turn out "
            "not to be exceptions."
        ),
        "key_label": "Where the pronoun goes",
        "key": [
            "find it out    give it up    put it off",
            "pronoun between verb and particle",
            "",
            "look at it     think of it",
            "pronoun after the preposition",
            "",
            "the novel: 34 of 42 lines, 81.0%",
        ],
        "concepts_intro": "Three ideas. The second explains the 8.",
        "concepts": (
            (
                "A particle goes with the verb; a preposition goes with the "
                "noun after it",
                "<em>Up</em>, <em>out</em>, <em>off</em>, <em>down</em>, "
                "<em>away</em>, <em>back</em> and <em>over</em> can be a "
                "particle. <em>At</em>, <em>to</em>, <em>for</em>, <em>of</em> and "
                "<em>with</em> are prepositions. The test between them is the "
                "pronoun: it goes between the verb and a particle, and after "
                "a preposition.",
            ),
            (
                "The lines that look like exceptions are not",
                "The lab finds 34 lines with a pronoun between verb and "
                "particle and 8 with the pronoun after. Read the 8. Five begin "
                "a new sentence or clause (<em>came away. It was</em>, "
                "<em>sit down You are</em>). Three have <em>over</em> as a "
                "preposition: <em>get over it</em> twice and <em>glancing over "
                "it</em>. None puts a pronoun object after a true particle.",
            ),
            (
                "A few phrasal verbs make up most of what is used",
                "A <dfn>phrasal verb</dfn> is a verb and a particle that act as "
                "one. The novel's commonest are <em>go away</em> 32, "
                "<em>sit down</em> 29, <em>find out</em> 20, <em>come back</em> "
                "16, and then <em>give up</em> and <em>set off</em> with 12 "
                "each; the tile names <em>give up</em>, the first of the two by "
                "spelling. The play's are <em>sit down</em> 11, <em>go out</em> "
                "9, <em>break off</em> 8, <em>pick up</em> 7, and <em>come "
                "up</em> and <em>go over</em> with 5 each.",
            ),
        ),
        "steps_title": "Placing a pronoun after a verb and a small word",
        "steps_intro": "Three questions, then one check.",
        "steps": (
            (
                "Is the small word at, to, for, of or with?",
                "Then it is a preposition. The pronoun comes after it: "
                "<em>look at it</em>, <em>think of it</em>.",
            ),
            (
                "Is it up, out, off, down, away, back or over?",
                "It may be a particle. Say the pronoun and check the next step.",
            ),
            (
                "If it is a particle and the object is a pronoun, put the "
                "pronoun between",
                "<em>Find it out</em>, <em>give it up</em>, <em>put it off</em>. "
                "Not <em>find out it</em>.",
            ),
            (
                "If the object is a noun, either place is possible",
                "<em>Give up the idea</em> and <em>give the idea up</em> are "
                "both said. Only the pronoun is fixed.",
            ),
            (
                "Check over with care",
                "<em>Get it over</em> and <em>get over it</em> are both in the "
                "novel. <em>Over</em> can be either, and the pronoun's place "
                "tells you which.",
            ),
        ),
        "lab": ("english", {
            "mode": "phrasal",
            "rule": "pronoun",
            "source": "austen",
            "panel_title": "Count the pronouns, then read the 8",
            "panel_intro": (
                "Each row is a printed line with a verb and one of the seven "
                "particles. Choose the novel (1813) or the play (1895). The "
                "table shows the verb, the particle and whether a pronoun is "
                "between them or after them. The second list shows lines with "
                "<em>at</em>, <em>to</em>, <em>for</em>, <em>of</em> or "
                "<em>with</em> and a pronoun. <em>Her</em> is left out, because "
                "it is also a possessive."
            ),
        }),
        "read_title": "The 8 lines with the pronoun after",
        "read_intro": (
            "34 of the 42 lines with a pronoun put it between. Read the other 8."
        ),
        "worked": {
            "title": "Six phrases from the printed lines",
            "intro": [
                "Each is a line, or the same kind of line. Name the small word, "
                "then the place of the pronoun.",
            ],
            "lines": [
                "find it out       particle, pronoun between",
                "give it up        particle, pronoun between",
                "put it off        particle, pronoun between",
                "look at it        preposition, pronoun after",
                "think of it       preposition, pronoun after",
                "get over it       over as a preposition",
            ],
            "after": [
                "The first three are among the 34. The next two are of the 347 "
                "lines in the lab's second list, in which a verb, one of five "
                "prepositions and a pronoun stand together. In every one of the "
                "347 the pronoun is after the preposition, but that is how the "
                "lines were chosen, so it shows how common the pattern is and "
                "not that no one writes otherwise.",
                "The last is one of the 8. In <em>get over it</em> the word "
                "<em>over</em> is a preposition, and the pronoun follows it as "
                "it follows <em>at</em>. In <em>get it over</em> the same word "
                "is a particle. The rule is not broken. The word has two jobs.",
            ],
        },
        "note": (
            "The lab counts spellings and not meanings: it finds a verb and "
            "one of seven small words, and it cannot tell whether the pair means "
            "something new, as <em>give up</em> does. A few rows are not "
            "phrasal verbs at all, for example <em>any great advantage "
            "over the country</em>, where the word before <em>over</em> is a "
            "noun. The play gives a smaller sample: 149 lines, 16 with the "
            "pronoun between and 5 after, 76.2%, and 93 lines with a "
            "preposition."
        ),
        "mistakes": (
            (
                "Thinking look at it proves give up it",
                "<em>At</em> is a preposition, so the pronoun follows it. "
                "<em>Up</em> is a particle, so the pronoun goes before it. "
                "Both are a verb and a small word, and the pronoun's place is "
                "the test that tells them apart.",
            ),
            (
                "Treating a small word as one job",
                "<em>Over</em> is a particle in <em>get it over</em> and a "
                "preposition in <em>get over it</em>. The novel has both. "
                "Three of the 8 lines that look like exceptions are this.",
            ),
            (
                "Moving a noun and a pronoun the same way",
                "<em>Give up the idea</em> is fine, and so is <em>give the "
                "idea up</em>. A noun can go either side. A pronoun cannot: "
                "<em>give up it</em> is the error this lesson is named for.",
            ),
        ),
        "quiz_title": "Check yourself",
        "quiz": (
            {
                "q": "Which is correct?",
                "a": ["give up it", "give it up", "give it to up", "up give it"],
                "c": 1,
                "why": (
                    "<em>Up</em> is a particle, so the pronoun goes between "
                    "the verb and the particle. The other three are not "
                    "English."
                ),
            },
            {
                "q": "Which of these has a preposition and not a particle?",
                "a": ["find it out", "put it off", "think of it", "give it up"],
                "c": 2,
                "why": (
                    "<em>Of</em> is a preposition, and the pronoun follows it. "
                    "<em>Out</em>, <em>off</em> and <em>up</em> are particles."
                ),
            },
            {
                "q": "In the novel, 34 lines put the pronoun between and 8 put it "
                     "after. What does reading the 8 show?",
                "a": [
                    "The rule fails in 8 lines",
                    "The novel breaks the rule often",
                    "The lab counted wrongly",
                    "None puts a pronoun object after a particle",
                ],
                "c": 3,
                "why": (
                    "The 8 are <em>get over it</em> twice, <em>glancing over "
                    "it</em>, and five lines where the next word begins a new "
                    "clause, such as <em>sit down You are</em>. The rule holds."
                ),
            },
            {
                "q": "Which phrasal verb is the commonest in the novel's lines?",
                "a": ["go away", "sit down", "find out", "give up"],
                "c": 0,
                "why": (
                    "<em>Go away</em>, 32 times. <em>Sit down</em> is next with "
                    "29, then <em>find out</em> 20 and <em>give up</em> 12."
                ),
            },
        ),
        "body": [
            ("p",
             "A <dfn>particle</dfn>, plural <dfn>particles</dfn>, is a small word such as <em>up</em>, "
             "<em>out</em> or <em>off</em> that joins a verb to make one "
             "action: <em>give up</em>, <em>find out</em>, <em>put off</em>. A "
             "<dfn>preposition</dfn> (plural <dfn>prepositions</dfn>) is a small word such as <em>at</em> or "
             "<em>of</em> that joins a noun to the verb. On the page they look "
             "the same, and they follow different rules."),
            ("h3", "The test"),
            ("p",
             "Take a pronoun, <em>it</em>, as the object. After a verb and "
             "<em>up</em>, it goes in the middle: <em>give it up</em>. After a "
             "verb and <em>at</em>, it goes at the end: <em>look at it</em>. "
             "The place of the pronoun tells you which small word you have."),
            ("p",
             "The lab runs this on 473 lines from the novel. It finds a verb "
             "and one of seven particles, and looks for a pronoun. 34 lines "
             "have the pronoun between, among them <em>find it out</em>, "
             "<em>give it up</em> and <em>put it off</em>. 8 have it after, "
             "and that gives 81.0% for the rule."),
            ("h3", "The 8 lines"),
            ("p",
             "81.0% looks like a rule with exceptions. Read the 8 and it "
             "is not. Five of them are a verb and a particle at the end of a "
             "clause, with the next clause starting with a pronoun: "
             "<em>when we came away it was</em>, <em>let us sit down You "
             "are</em>. The lab sees a pronoun after the particle, and the "
             "pronoun is not its object. The other three are <em>get over "
             "it</em>, twice, and <em>glancing over it</em>. There <em>over</em> "
             "is a preposition, and the pronoun follows it as the rule for "
             "prepositions says."),
            ("p",
             "So the 34 are the whole story for a pronoun object. The play "
             "reads the same way. Its sample is smaller, 149 lines, with 16 "
             "between and 5 after, which is 76.2%. Of the 5, three begin a "
             "new clause, as <em>sitting down You can</em> does, and two follow "
             "a noun, <em>a good influence over him</em> and <em>her hand over "
             "it</em>, so again none puts the object after a particle."),
            ("h3", "The preposition side"),
            ("p",
             "The second list under the table holds the contrast: 347 lines in "
             "the novel with a verb, <em>at</em>, <em>to</em>, <em>for</em>, "
             "<em>of</em> or <em>with</em>, and a pronoun. <em>Look at it</em>, "
             "<em>think of it</em>, <em>dance with him</em>. Every one has "
             "the pronoun last. These lines were gathered that way, so the "
             "count says how common the pattern is. It does not say that "
             "no one could write it otherwise."),
            ("h3", "Which phrasal verbs are used"),
            ("p",
             "The novel's 473 lines are not 473 different verbs. Five make up "
             "a large share of them: <em>go away</em> 32, <em>sit down</em> 29, "
             "<em>find out</em> 20, <em>come back</em> 16 and <em>give up</em> "
             "12, with <em>set off</em> also at 12 just behind it in the full "
             "table. The play's 149 lines lead with <em>sit down</em> 11, then "
             "<em>go out</em> 9, <em>break off</em> 8, <em>pick up</em> 7 and "
             "<em>come up</em> 5, with <em>go over</em> at 5 beside it. "
             "<em>Sit down</em> is in both lists."),
            ("p",
             "What the lab cannot tell you is the meaning. <em>Give up</em> "
             "does not mean give and up, and the lab does not know that. It "
             "finds spellings. A few rows are not phrasal verbs at all, such as "
             "<em>any great advantage over the country</em>, where the word "
             "before <em>over</em> is a noun. You are looking at a count, "
             "and the table is there so that you can see where it is soft."),
        ],
    },
]
