# -*- coding: utf-8 -*-
"""Lessons one and two of Nouns and Articles: the plural rule and the nouns with none.

Both lessons use the wordrule lab on the plural list. Every figure here is
read off the built page with labcheck.js --observe:

  r0 1866 of 1887, 98.9%, 21 missed
  r1 1864 (photo, piano, pro missed; potato right)
  r2 1861 (belief, brief, chief, golf, proof, relief, roof, safe newly missed)
  r3 1868, 99.0% (golf the only new miss)
  75 nouns with no plural, 75 of 683 noun-only headwords

The sort of the 75 in lesson two (47 mass nouns; 9 already plural or the same
both ways, personnel among them; 16 days and months; basis, hell, sake) was
done by reading the printed list, and every word is in one kind.

The whole-novel counts in lesson two (twelve words with no a, an or plural in
122,294 words; time and hope) were counted once offline by the designer
(docs/english-v2/measure/out/corpus.txt) and are marked quoted where they
appear. Spoken forms the orchestrator must merge are in
content/spoken/english_c6_nouns_articles.py.
"""

LESSONS = [
    {
        "slug": "one-noun-two-nouns",
        "module": "One and more than one",
        "title": "One Noun, Two Nouns",
        "one_line": "Three small rules make a plural, and the words that break them are a short list.",
        "standard": (
            "Finish when you can write the plural of a noun you have not seen "
            "before, and say which rule you used.",
            "You should be able to apply the three parts of the plural rule in "
            "order, read its score on the printed list of nouns, name the kinds of "
            "noun it misses, and show with the lab why two extra rules "
            "make the score worse and a third, narrower one makes it a little "
            "better.",
        ),
        "summary": (
            "A <dfn>plural</dfn> is the form of a noun that means more than one. "
            "On the 1,887 nouns in the printed list, a rule with three parts gives "
            "the plural the <dfn>dictionary</dfn>, a book that lists the words of a language, has for 1,866 of them. This lesson states "
            "the rule, reads the 21 nouns it misses, and tries three ways of "
            "improving it. Two of the three make it worse."
        ),
        "key_label": "The plural rule on 1,887 nouns",
        "key": [
            "cat, day       add -s",
            "box, church    add -es after a hiss",
            "city, baby     -y becomes -ies",
            "",
            "right on 1866 of 1887    98.9%",
            "it misses 21; 9 are old plurals:",
            "men, women, feet, teeth, children",
        ],
        "concepts_intro": "Three ideas. The last one is about how to improve a rule.",
        "concepts": (
            (
                "A plural rule has three parts, and the parts are about the end of the word",
                "Add <em>-s</em>. After a <dfn>hiss</dfn>, a sound like the end of <em>bus</em> or <em>dish</em>, written <em>s</em>, "
                "<em>sh</em>, <em>ch</em>, <em>x</em> or <em>z</em>, add "
                "<em>-es</em>, so <em>box</em> becomes <em>boxes</em> and "
                "<em>church</em> becomes <em>churches</em>. After a <dfn>consonant</dfn>, "
                "any letter that is not <em>a, e, i, o</em> or <em>u</em>, "
                "and <em>y</em>, change the <em>y</em> to <em>ies</em>, so "
                "<em>city</em> becomes <em>cities</em>. After a <dfn>vowel</dfn>, "
                "one of those five letters, and <em>y</em> the first part is "
                "enough: <em>day</em> becomes <em>days</em>.",
            ),
            (
                "The words it misses are not random",
                "Of 1,887 nouns the rule is right for 1,866 and wrong for 21. "
                "Nine of the 21 are old plural forms that no ending makes "
                "(<em>man, men</em>; <em>child, children</em>), five end in <em>f</em> or <em>fe</em> "
                "and change it to <em>v</em> (<em>wife, wives</em>), five come "
                "from Greek (<em>crisis, crises</em>), and two are single cases: "
                "<em>potato</em> and <em>stomach</em>. Each group has a reason, "
                "and each group is short enough to learn.",
            ),
            (
                "A new rule has to be scored on the whole list, not on the words you thought of",
                "It is easy to think of a rule that fixes some words. The lab "
                "adds three of them one at a time. Two fix a few words and break "
                "more. The one that helps is the one that names its endings "
                "exactly. The count shows that; the feeling that a rule is "
                "good does not.",
            ),
        ),
        "steps_title": "Making the plural of a noun in front of you",
        "steps_intro": "Four questions, in this order.",
        "steps": (
            (
                "Is it one of the old plural forms?",
                "<em>Man, woman, child, foot, tooth, mouse</em> and the words "
                "built on them, such as <em>gentleman</em>. If it is, you know the "
                "plural already, and no rule is needed.",
            ),
            (
                "Does it end in a hiss?",
                "Look for <em>s, sh, ch, x</em> or <em>z</em>. If so, add "
                "<em>-es</em>. Say the word: <em>church</em> ends in the same "
                "sound it starts with, so it takes <em>-es</em>, but "
                "<em>stomach</em> ends in a <em>k</em> sound and takes "
                "<em>-s</em>.",
            ),
            (
                "Does it end in a consonant and y?",
                "Then change <em>y</em> to <em>ies</em>. A vowel before the "
                "<em>y</em> (<em>boy, day, key</em>) keeps it, and you add "
                "<em>-s</em>.",
            ),
            (
                "Otherwise add -s, and check the short lists",
                "That covers almost every noun. The lists to learn are the "
                "old plural forms, the <em>f</em> words and a few from Greek. Add "
                "<em>potato</em> to them, and keep <em>photo</em> and "
                "<em>piano</em> out of the <em>-oes</em> group.",
            ),
        ),
        "lab": ("english", {
            "mode": "wordrule",
            "list": "plurals",
            "rule": "r0",
            "show": "misses",
            "panel_title": "Score the plural rule, then try three changes",
            "panel_intro": (
                "These are the nouns in the word list for which the dictionary "
                "confirms a plural. The first rule is the rule with three parts of this "
                "lesson. The next three each add one more rule to it. A form "
                "counts as right when it is one the dictionary has, and every "
                "noun the rule gets wrong is printed with what the dictionary has "
                "instead."
            ),
        }),
        "read_title": "The 21 nouns the rule with three parts misses",
        "read_intro": (
            "Switch the lab to the first rule and read the table of misses. "
            "They fall into five groups."
        ),
        "worked": {
            "title": "Potato and photo: the rule that gains one word and loses three",
            "intro": [
                "A natural fix is to add a fourth part: after a consonant and "
                "<em>o</em>, add <em>-es</em>. It works for <em>potato</em>. "
                "Choose the second rule in the lab and read its misses.",
            ],
            "lines": [
                "potato   potatoes   right with the new part",
                "photo    photos     wrong with the new part",
                "piano    pianos     wrong with the new part",
                "pro      pros       wrong with the new part",
                "",
                "1866 of 1887 becomes 1864 of 1887",
            ],
            "after": [
                "The new part gains one word and loses three, so the score goes "
                "down by two. <em>Radio</em>, <em>video</em> and <em>studio</em> "
                "are not touched, because a vowel stands before the <em>o</em>. "
                "The spelling cannot tell <em>potato</em> from <em>photo</em>. "
                "One of them is short for something else, and nothing in the "
                "letters says so.",
            ],
        },
        "note": (
            "Where the dictionary has two plural forms for a noun, the rule counts as "
            "right if it makes either one. That is why <em>hero</em> (heroes or "
            "heros) and <em>index</em> are not in the list of misses, and why "
            "<em>person</em> is not: its plural can be <em>persons</em>, as "
            "well as <em>people</em>. <em>Knife</em> is a harder case. The "
            "dictionary confirms <em>knifes</em> because it is a form of the "
            "verb (<em>he knifes</em>), so the rule's form counts as right, "
            "though the plural you should write is <em>knives</em>. The lab "
            "reads spellings, not meanings, and it says so under its numbers. "
            "It prints every plural the dictionary has next to the rule's, so "
            "you can check each decision."
        ),
        "mistakes": (
            (
                "Writing f becomes ves as the rule",
                "It fits <em>half, life, self, shelf</em> and <em>wife</em>. It "
                "breaks <em>belief, brief, chief, proof, relief, roof</em> and "
                "<em>safe</em>, and <em>golf</em> too. Added to the rule that "
                "already has the <em>-oes</em> part, it fixes five nouns and "
                "breaks eight, and the score goes from 1864 to 1861 of 1887. A "
                "narrower rule that names only the endings <em>-lf, -ife, "
                "-eaf</em> and <em>-olf</em> fixes the five and adds one miss, "
                "<em>golf</em>. It is the best of the four.",
            ),
            (
                "Adding -es to every noun that ends in o",
                "Only some do. Counted on the list, the <em>-oes</em> part loses "
                "more than it gains. Learn <em>potato</em> as one noun, and "
                "<em>hero</em> as a noun the dictionary spells both ways.",
            ),
            (
                "Treating an old plural as a mistake in the rule",
                "<em>Men</em>, <em>women</em>, <em>feet</em> and <em>teeth</em> "
                "are very old forms that came before the <em>-s</em> rule. The "
                "rule did not fail on them; they were never made by it. They are "
                "nine nouns in this list, and learning nine is less work than "
                "building a rule that covers them.",
            ),
        ),
        "quiz_title": "Check yourself",
        "quiz": (
            {
                "q": "Which of these nouns does the rule with three parts get wrong?",
                "a": ["<em>box</em>", "<em>city</em>", "<em>day</em>", "<em>woman</em>"],
                "c": 3,
                "why": (
                    "The rule gives <em>womans</em>. The dictionary has "
                    "<em>women</em>, which is an old plural that the rule never "
                    "makes. <em>Boxes</em>, <em>cities</em> and <em>days</em> "
                    "are all right by the rule."
                ),
            },
            {
                "q": "Why can no spelling rule separate <em>potato</em> from <em>photo</em>?",
                "a": [
                    "Both are old plural forms",
                    "Both end in a consonant and <em>o</em>, and only one takes <em>-es</em>",
                    "<em>Photo</em> ends in a hiss",
                    "<em>Potato</em> is not a noun",
                ],
                "c": 1,
                "why": (
                    "The two words end in the same letters. One is <em>potatoes</em> "
                    "and the other <em>photos</em>, so the second letter-rule "
                    "gains one word and loses three."
                ),
            },
            {
                "q": "The fix for <em>f</em> words took the score from 1864 to 1861. What did it do?",
                "a": [
                    "It fixed eight nouns and broke five",
                    "It fixed no noun and broke three",
                    "It fixed five nouns and broke eight",
                    "It fixed five nouns and broke none",
                ],
                "c": 2,
                "why": (
                    "<em>Half, life, self, shelf</em> and <em>wife</em> were "
                    "fixed. <em>Belief, brief, chief, golf, proof, relief, roof</em> "
                    "and <em>safe</em> were broken. Five fixed and eight broken "
                    "is a loss of three."
                ),
            },
            {
                "q": "Which plural does the rule make from <em>stomach</em>, and is it right?",
                "a": [
                    "<em>stomaches</em>, and it is wrong, because <em>ch</em> says <em>k</em> there",
                    "<em>stomachs</em>, and it is right",
                    "<em>stomaches</em>, and it is right",
                    "<em>stomachies</em>, and it is wrong",
                ],
                "c": 0,
                "why": (
                    "The hiss part reads the letters <em>ch</em>. In "
                    "<em>stomach</em> they say <em>k</em>, so the dictionary has "
                    "<em>stomachs</em> and the rule's <em>stomaches</em> is "
                    "wrong."
                ),
            },
        ),
        "body": [
            ("p",
             "Every noun that you can count has two forms: one for one thing "
             "and one for more than one. The second is called the "
             "<dfn>plural</dfn>. You have met the main rule for making it: it "
             "is the <em>-s</em> rule of Tense Tables, which put <em>-s</em> on "
             "a verb after <em>he</em>, <em>she</em> and <em>it</em>. This "
             "lesson runs the same rule on nouns and counts how often it is "
             "right."),
            ("p",
             "The lab holds 1,887 nouns from the word list, each with the "
             "plural forms the dictionary confirms for it. The rule makes a form "
             "for each. If the form is one the dictionary has, the rule is "
             "right for that noun. The rule has three parts: add "
             "<em>-s</em>; add <em>-es</em> after a hiss; change a consonant "
             "and <em>y</em> to <em>ies</em>."),
            ("h3", "How often the three parts are right"),
            ("p",
             "Counted on this page, the rule is right for 1,866 of the 1,887 "
             "nouns, which is 98.9%. That is a rule you can use with no further "
             "thought, and the table at the bottom of the lab prints the 21 "
             "nouns where it is wrong."),
            ("h3", "Reading the 21"),
            ("p",
             "Nine are old plural forms that no ending makes. Seven of them "
             "change the vowel in the middle of the word: <em>man, woman, "
             "foot, tooth, mouse, chairman</em> and <em>gentleman</em>. "
             "<em>Child</em> adds an ending of its own, <em>children</em>, and "
             "<em>die</em> has <em>dice</em>. Five end in <em>f</em> or <em>fe</em> and take "
             "<em>ves</em>: <em>half, life, self, shelf, wife</em>. Five come "
             "from Greek: <em>analysis, crisis, emphasis, hypothesis</em> and "
             "<em>phenomenon</em>. The last two are single cases. "
             "<em>Potato</em> takes <em>-es</em> after an <em>o</em>. "
             "<em>Stomach</em> ends in the letters <em>ch</em>, but they say "
             "<em>k</em>, so the hiss part gives the wrong form."),
            ("p",
             "That is five reasons, and the longest list under any of them has "
             "nine words. The rule plus these five short lists is enough for "
             "every noun in the table."),
            ("h3", "Three ways to improve it"),
            ("p",
             "An obvious next step is to add a rule for each group. The lab "
             "lets you add three, one at a time, and score the result on the "
             "same 1,887 nouns. Each one comes from a good reason. Each one "
             "fits the nouns that made you think of it."),
            ("p",
             "Add the <em>-oes</em> part for a consonant and <em>o</em>, and "
             "the score falls by two, to 1,864. It gains <em>potato</em>. It "
             "loses <em>photo, piano</em> and <em>pro</em>. Add to that the "
             "idea that <em>f</em> or <em>fe</em> becomes <em>ves</em>, and "
             "the score falls to 1,861. It gains <em>half, life, self, shelf</em> "
             "and <em>wife</em>, and loses <em>belief, brief, chief, golf, "
             "proof, relief, roof</em> and <em>safe</em>."),
            ("h3", "The version that helps"),
            ("p",
             "The third change keeps the <em>-oes</em> part and replaces the "
             "idea about <em>f</em> with a narrow one: use <em>ves</em> only "
             "after <em>-lf</em>, <em>-ife</em>, <em>-eaf</em> or "
             "<em>-olf</em>. That raises the score to 1,868 of 1,887, which "
             "is 99.0%. It still loses <em>photo, piano</em> and <em>pro</em>, "
             "and it breaks <em>golf</em>, which ends in <em>-lf</em> but is "
             "<em>golfs</em>. It fixes the five <em>f</em> nouns. <em>Leaf</em> "
             "and <em>wolf</em>, which two of its endings are written for, are "
             "not in the list at all. The size of the endings it names is what "
             "makes the difference."),
            ("p",
             "The gain is two nouns over the rule with three parts, and the cost is "
             "a rule with a list of endings inside it. For most readers the "
             "better choice is the plain rule and the short lists."),
            ("h3", "What the table cannot tell you"),
            ("p",
             "The dictionary says which forms exist, not which one is common. "
             "Where it has two forms, the lab counts the rule as right if it "
             "makes either one. The words come from a list of two thousand "
             "eight hundred common words, so rare nouns, which have more "
             "irregular plural forms, are not in the table."),
        ],
    },
    {
        "slug": "nouns-with-no-plural",
        "module": "One and more than one",
        "title": "Nouns With No Plural",
        "one_line": "Some nouns never take -s, and students write informations anyway.",
        "standard": (
            "Finish when you can say, for a noun, whether it has a plural, and "
            "which small words you may not put in front of it.",
            "You should be able to read the printed list of nouns with no plural "
            "in the word list, sort it into the kinds a student needs, state "
            "what such a noun never takes, and name the nouns that count in one "
            "sense and not in another.",
        ),
        "summary": (
            "Some nouns have no <dfn>plural</dfn>. <em>Advice</em> is one: you may give "
            "<em>some advice</em> or <em>a piece of advice</em>, but not "
            "<em>advices</em>. In the word list, 75 of the 683 nouns that are "
            "only nouns have no plural that the list records and the <dfn>dictionary</dfn> confirms. This lesson prints "
            "them, sorts them, and says what a quoted count over a whole novel "
            "adds to the picture."
        ),
        "key_label": "Nouns with no plural in the list",
        "key": [
            "no plural recorded for 75 of 683 nouns",
            "",
            "advice    information    furniture",
            "never   advices   an advice",
            "",
            "say   some advice   a piece of advice",
        ],
        "concepts_intro": "Three ideas.",
        "concepts": (
            (
                "A noun can be one that you do not count",
                "<em>Advice, information, furniture, money</em> and "
                "<em>knowledge</em> name a mass of something. You can have a "
                "lot of it or a little of it, but you do not have one of "
                "them and two of them. Such a noun has no plural form, and it "
                "does not take <em>a</em> or <em>an</em>.",
            ),
            (
                "The list is made of kinds, and the kinds do not all behave the same",
                "Of the 75, 47 are things you do not count. Nine already "
                "look plural, or are the same for one and for many: <em>news, "
                "series, sheep, species, data</em>. Sixteen are the names of "
                "days and months, which have a plural in use (<em>two "
                "Mondays</em>) that the word list does not record. Three are "
                "left over. A student needs the first two kinds. The "
                "third and fourth are limits of the list.",
            ),
            (
                "Some nouns count in one sense and not in another",
                "<em>Time</em> that you measure has no plural, but a time that "
                "you remember does: <em>three times</em>. A rule that says a "
                "noun can or cannot be counted would be wrong for such words, "
                "and no list can mark which sense a writer means.",
            ),
        ),
        "steps_title": "Deciding, for a noun in front of you",
        "steps_intro": "Three questions, and then a check.",
        "steps": (
            (
                "Can you say one of them, two of them?",
                "One <em>chair</em>, two <em>chairs</em>: yes, so it has a "
                "plural. One <em>advice</em>, two <em>advices</em>: no. If the "
                "words sound wrong, the noun is probably a mass noun.",
            ),
            (
                "Would a piece of, or some, fit?",
                "<em>Some advice, a piece of news, a piece of furniture</em> "
                "all work. These are the ways to count a noun that does not "
                "take <em>a</em>.",
            ),
            (
                "Choose the small word in front",
                "Use <em>much</em> and <em>a little</em> with these nouns, "
                "not <em>many</em> and <em>a few</em>: <em>much "
                "information</em>, not <em>many informations</em>.",
            ),
            (
                "Check the printed list",
                "The lab prints all 75. If your noun is on it, the word list "
                "records no plural for it. If it is not, either the "
                "dictionary has a plural for it, even if you rarely meet one, "
                "or the word is not only a noun.",
            ),
        ),
        "lab": ("english", {
            "mode": "wordrule",
            "list": "plurals",
            "rule": "r0",
            "show": "noplural",
            "panel_title": "Read the nouns with no plural",
            "panel_intro": (
                "The list below the tiles is the 75 nouns that are only nouns "
                "and have no plural the dictionary confirms. The rule from the "
                "last lesson is still scored above it. Switch the list to see "
                "every noun, or the words set aside and the reason for each."
            ),
        }),
        "read_title": "Sorting the 75",
        "read_intro": (
            "Read the list once, then sort it. Four kinds cover it."
        ),
        "worked": {
            "title": "Four kinds in the list of 75",
            "intro": [
                "Here is the printed list, sorted by what a student needs to "
                "know about each kind. The sorting is done by reading, and "
                "you can check every word against the lab.",
            ],
            "lines": [
                "47  things you do not count",
                "    advice, furniture, information, money",
                "9   plural already, or the same for one and many",
                "    news, series, sheep, species, data",
                "16  days and months",
                "    Monday, Friday, April, December",
                "3   left over: basis, hell, sake",
            ],
            "after": [
                "The last kind needs care. <em>Basis</em> has the plural "
                "<em>bases</em>, which the word list does not record, so it is "
                "here by a limit of the list. <em>Hell</em> and <em>sake</em> "
                "are nouns you meet in fixed phrases, <em>go to hell</em> and "
                "<em>for the sake of</em>, and the dictionary confirms no plural "
                "for either. So &ldquo;no plural in the list&rdquo; is a "
                "statement about the list, and the first two kinds are the ones "
                "that are true of English.",
                "The days and months are different again. You can say "
                "<em>two Mondays</em>, so for them the rule \"never takes "
                "<em>-s</em>\" is not true. They are on the list because "
                "the word list records only the <dfn>singular</dfn> name, the form that means one.",
            ],
        },
        "note": (
            "Not every noun with no plural is on the list. Words such as "
            "<em>music</em> and <em>help</em> have a plural in the dictionary "
            "and are not in the list, even though most writers never use "
            "one. The list is the dictionary's view, and a writer's use is "
            "narrower."
        ),
        "mistakes": (
            (
                "Believing that every noun has a plural",
                "<em>Informations</em> and <em>advices</em> are two of the "
                "commonest written errors at this level. The lab shows why: "
                "75 nouns in the list have no plural, and the ones a student "
                "meets most often are among them.",
            ),
            (
                "Putting a or an before one of these nouns",
                "<em>An advice</em> is wrong for the same reason as "
                "<em>advices</em>: both treat the noun as something you can "
                "count. The page cannot check this half of the rule, because "
                "its lines hold no sentences. A count over the whole novel, "
                "made once and quoted here, finds that ten words from the "
                "list (<em>advice, information, news, furniture, money, "
                "knowledge, happiness, health, wealth</em> and "
                "<em>poetry</em>) are never written with <em>a</em> or "
                "<em>an</em>, and never as a plural, in its 122,294 words. "
                "That is one old book.",
            ),
            (
                "Thinking a noun is always counted or never counted",
                "<em>Time</em> is a noun that counts in one sense and not in "
                "another. In the novel, counted once and quoted here, it has "
                "<em>a time</em> 10 times and <em>times</em> 19 times. "
                "<em>Hope</em> is the same: <em>hopes</em> is written 23 "
                "times. Both are on the list of nouns that have a plural, "
                "and neither list can tell you which sense you mean.",
            ),
        ),
        "quiz_title": "Check yourself",
        "quiz": (
            {
                "q": "Which sentence is right?",
                "a": [
                    "I need some advices.",
                    "I need some advice.",
                    "I need an advice.",
                    "I need many advices.",
                ],
                "c": 1,
                "why": (
                    "<em>Advice</em> has no plural, and it does not take "
                    "<em>an</em>. <em>Some</em> works with a noun you do not "
                    "count."
                ),
            },
            {
                "q": "Which noun on the list is the same for one and for many?",
                "a": ["<em>sheep</em>", "<em>advice</em>", "<em>health</em>", "<em>money</em>"],
                "c": 0,
                "why": (
                    "One sheep, two sheep. The other three are things you do "
                    "not count at all."
                ),
            },
            {
                "q": "In the novel, <em>time</em> is written <em>a time</em> 10 times and <em>times</em> 19 times. What does this show?",
                "a": [
                    "The word list is wrong about <em>time</em>",
                    "The novel was printed with mistakes",
                    "<em>Time</em> is a verb in these lines",
                    "A noun can count in one sense and not in another",
                ],
                "c": 3,
                "why": (
                    "Time that you measure is not counted, and a time you "
                    "remember is. Both senses are the same word. The count is "
                    "quoted from a whole novel."
                ),
            },
            {
                "q": "Why is <em>Monday</em> on the list of nouns with no plural?",
                "a": [
                    "English has no plural for the names of days",
                    "The word list records only the singular name, though <em>Mondays</em> is used",
                    "<em>Monday</em> is a mass noun like <em>advice</em>",
                    "The dictionary does not have <em>Mondays</em>",
                ],
                "c": 1,
                "why": (
                    "You can say <em>two Mondays</em>. The list holds only "
                    "what the word list records, so this entry is a limit of "
                    "the list and not a rule of English."
                ),
            },
        ),
        "body": [
            ("p",
             "The last lesson ended with a rule that is right for 1,866 of "
             "1,887 nouns. This lesson is about the nouns that rule cannot be "
             "scored on, because they have no plural to compare with."),
            ("p",
             "The word list has 683 words that are only nouns. Of these, "
             "75 have no plural that the list records and the dictionary "
             "confirms. That is the list printed in the lab, in the order of the "
             "alphabet."),
            ("h3", "What the list is made of"),
            ("p",
             "Read it once from the top. Most of it is things you do not "
             "count. <em>Advice, assistance, clothing, equipment, "
             "furniture, information, knowledge, money, software, wealth</em>: "
             "each names a mass of something, and in each case you count it "
             "with a phrase such as <em>a piece of</em> or <em>some</em>. "
             "<em>Happiness, darkness, poverty, violence</em> and "
             "<em>tennis</em> are the same: you have a lot of them or a "
             "little."),
            ("p",
             "A smaller group of nine already looks plural or does not change: "
             "<em>news, series, sheep, species, aircraft, data, politics, "
             "mathematics</em>, and <em>personnel</em>, which names a group of "
             "people and is used as a plural. <em>News</em> takes a singular "
             "verb, and <em>series</em> and <em>sheep</em> are the same for "
             "one and for many."),
            ("h3", "What such a noun never takes"),
            ("p",
             "It never takes <em>-s</em>. It does not take <em>a</em> or "
             "<em>an</em>. And it goes with <em>much</em> and <em>a "
             "little</em>, not <em>many</em> and <em>a few</em>. The lab "
             "counts nothing about these, because the printed list holds no "
             "sentences. The count for <em>a</em> and <em>an</em> comes "
             "from a whole novel, which no page can carry, and it is marked "
             "quoted where it appears."),
            ("h3", "The two kinds that are limits of the list"),
            ("p",
             "Sixteen of the 75 are the names of days and months. They are "
             "here because the word list records only the singular name, and "
             "yet <em>two Mondays</em> is correct English. So for them the "
             "rule &ldquo;never takes <em>-s</em>&rdquo; is false. Do not "
             "carry the rule over to them."),
            ("p",
             "Three more need care. <em>Basis</em> has the plural "
             "<em>bases</em>, which the word list does not record. "
             "<em>Hell</em> and <em>sake</em> live in fixed phrases, and the "
             "dictionary confirms no plural for either, so they are on the "
             "list rightly and teach you little. The list is not a list of "
             "nouns that cannot have a plural; it is a list of nouns where "
             "the word list records none. Read it that way."),
            ("h3", "Words that are not on it"),
            ("p",
             "The lab can also show the words that were set aside before the "
             "count. A program that sorts words by their use calls some small "
             "words nouns, such as <em>and</em>, <em>at</em> and "
             "<em>he</em>. They are not nouns here, and each is listed with "
             "the reason it was taken out."),
        ],
    },
]
