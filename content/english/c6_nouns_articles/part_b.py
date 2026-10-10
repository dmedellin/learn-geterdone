# -*- coding: utf-8 -*-
"""Lessons three and four of Nouns and Articles: a or an, and the before the only one.

Every figure is read off the built page with labcheck.js --observe.

a-or-an (an lab, source all): 493 lines scored of 510, 17 next words not in
the dictionary. letter 486 of 493 (98.6%), misses a University, an hour (5),
a utilitarian. sound 493 of 493 (100.0%). By source: the play 448 and 455 of
455; the modern documents 29 of 29 both; the passage 9 of 9 both.

the-before-the-only-one (the_super lab): est 127 of 142 (89.4%: the 93,
possessive 34, other 15); same 69 of 69; next 49 of 72 (68.1%: the 45,
possessive 4, other 23); most 40 of 122 (32.8%: the 37, possessive 3, a or an
45, other 37).

Quoted, counted once over the whole novel offline (docs/english-v2/measure/out/
cmudict.txt): 2,266 lines, letter 2,239 (98.8%), sound 2,263 (99.9%), the three
sound misses an union (twice) and an uniform.

The sorts of the residue in the-before-the-only-one (the 15 -est lines into
4 + 3 + 2 + 6; the 23 other next lines into 7 + 4 + 8 + 4; the 15 of the 37
other most lines after a form of be or seemed) were done by reading the printed
rows, which the lab shows in full.
"""

LESSONS = [
    {
        "slug": "a-or-an-by-sound-not-by-letter",
        "module": "A, an and the",
        "title": "A or An: by Sound, Not by Letter",
        "one_line": "The rule you were taught is about letters, and letters are the wrong thing to look at.",
        "standard": (
            "Finish when you can choose a or an by saying the next word, and name "
            "the words where the first letter is wrong about the sound.",
            "You should be able to say the first sound of a word, choose the "
            "small word that goes before it, read both the letter rule's score "
            "and the sound rule's score off the printed lines, and name the "
            "kinds of word where the two rules disagree.",
        ),
        "summary": (
            "The usual rule says <em>an</em> goes before a <dfn>vowel</dfn> letter, "
            "one of <em>a, e, i, o</em> and <em>u</em>. On the "
            "493 printed lines where the <dfn>dictionary</dfn>, a book that lists the words of a language, can say how the next word "
            "begins, that rule is right 486 times. A rule about the first "
            "<em>sound</em> of the next word is right on all 493. The seven lines "
            "that separate them show what the first rule was really about."
        ),
        "key_label": "The same 493 lines, two rules",
        "key": [
            "an before a vowel letter",
            "                       486 of 493   98.6%",
            "an before a vowel sound",
            "                       493 of 493  100.0%",
            "",
            "a University   an hour   a utilitarian",
        ],
        "concepts_intro": "Three ideas.",
        "concepts": (
            (
                "The rule is about sounds, because the reason for it is about sounds",
                "<em>A</em> and <em>an</em> are one word in two shapes. The "
                "shape that ends in <em>n</em> is used so that two vowel sounds "
                "do not meet: <em>an egg</em>, not <em>a egg</em>. When the "
                "next word begins with a <dfn>consonant</dfn> sound, any sound "
                "that is not a vowel sound, there is nothing to "
                "separate, and <em>a</em> is enough. The reason is spoken, so "
                "the rule is spoken.",
            ),
            (
                "The letter rule is nearly right because spelling usually follows sound",
                "Most words that begin with a vowel letter begin with a vowel "
                "sound. The letter rule is right 486 times in 493 for that "
                "reason. It fails when the spelling and the sound come apart, "
                "and there are three ways for that to happen.",
            ),
            (
                "One question replaces the rule and its exceptions",
                "Say the next word. If it begins with a vowel sound, use "
                "<em>an</em>. If not, use <em>a</em>. Nothing about the lines "
                "changes. The question changes, and the number of exceptions "
                "falls from seven to none.",
            ),
        ),
        "steps_title": "Choosing a or an for a word in front of you",
        "steps_intro": "Four steps.",
        "steps": (
            (
                "Say the next word, and listen only to how it begins",
                "Ignore the spelling. In <em>hour</em> the first sound is the "
                "vowel sound in <em>our</em>. In <em>university</em> it is the "
                "sound at the start of <em>you</em>.",
            ),
            (
                "Is that sound a vowel?",
                "A vowel sound is made with the mouth open and the air not "
                "stopped. If yes, use <em>an</em>: <em>an hour, an egg, an "
                "answer</em>.",
            ),
            (
                "If it is a consonant sound, use a",
                "<em>A University, a utilitarian, a "
                "house</em>. <em>You</em> and <em>one</em> begin with a "
                "consonant sound, whatever the letter says.",
            ),
            (
                "Check the three kinds that fool the letter",
                "A <em>u</em> said like <em>you</em>, a silent <em>h</em>, "
                "and <em>one</em>. These are the words to remember. For "
                "everything else the letter and the sound agree.",
            ),
        ),
        "lab": ("english", {
            "mode": "an",
            "rule": "letter",
            "source": "all",
            "panel_title": "Score both rules on the same lines",
            "panel_intro": (
                "Each line is an <em>a</em> or <em>an</em> from the play (1895), "
                "the two modern documents, or the passage from the novel (1813), "
                "with the word that follows it. Both rules are run in your "
                "browser on the same lines, and only the question changes. "
                "Choose the sound rule and watch the misses go."
            ),
        }),
        "read_title": "The seven lines the letter rule misses",
        "read_intro": (
            "Choose the letter rule and read the table of misses. All seven "
            "are in the play."
        ),
        "worked": {
            "title": "Three words, and why each one fools the letter",
            "intro": [
                "The seven lines that the letter rule misses come from three "
                "words. In each case the first letter and the first sound "
                "disagree.",
            ],
            "lines": [
                "a University      u said like you",
                "a utilitarian     u said like you",
                "an hour (5 times) h not said",
                "",
                "letter rule   486 of 493",
                "sound rule    493 of 493",
            ],
            "after": [
                "The first two begin with a vowel letter said as a consonant. "
                "The third begins with a consonant letter that is not said at "
                "all. Five of the seven misses are <em>an hour</em>, which "
                "the play uses five times. A third kind is <em>one</em>, "
                "which begins with the sound of <em>w</em> and so takes "
                "<em>a</em>. It is not among the seven. It appears in the "
                "count over the whole novel, quoted here, as <em>a one</em> "
                "among the lines the letter rule misses.",
            ],
        },
        "note": (
            "The sounds are the way the dictionary first says each word, "
            "which is American. A speaker of another kind of English may say "
            "<em>an historic</em> and <em>a hotel</em> differently, and the "
            "page cannot hear that. 17 of the 510 lines have a next word that is "
            "not in the dictionary, for example <em>Bunburyist</em>, and the lab "
            "lists them and does not score them."
        ),
        "mistakes": (
            (
                "Believing that an goes before a vowel letter",
                "That is right 486 times in 493 on these lines, and it "
                "breaks on <em>a University</em>, <em>a utilitarian</em> and "
                "<em>an hour</em>. The rule you want is about the sound the "
                "next word starts with. The letter is a good guide, and a bad "
                "reason.",
            ),
            (
                "Treating an union as correct because an old book has it",
                "Jane Austen wrote <em>an union</em> and <em>an uniform</em> in "
                "1813. In a count over the whole novel, made once and quoted "
                "here, the sound rule is right on 2,263 of 2,266 lines, which "
                "is 99.9%, and those three lines are all it misses. The "
                "habit was real and is gone. The sound rule marks the lines "
                "wrong because it describes the English of today.",
            ),
            (
                "Reading the unknown words as errors",
                "17 of the 510 lines are not scored, because the dictionary "
                "does not have the next word. They are not wrong. The page "
                "says so in its own column, and the 493 are the lines it can "
                "judge.",
            ),
        ),
        "quiz_title": "Check yourself",
        "quiz": (
            {
                "q": "Which phrase is right?",
                "a": ["<em>a hour</em>", "<em>an hour</em>", "<em>an university</em>", "<em>an one</em>"],
                "c": 1,
                "why": (
                    "<em>Hour</em> begins with a vowel sound, because the "
                    "<em>h</em> is silent, so it takes <em>an</em>. "
                    "<em>University</em> and <em>one</em> begin with a "
                    "consonant sound and take <em>a</em>."
                ),
            },
            {
                "q": "Why does the letter rule fail on <em>a University</em>?",
                "a": [
                    "<em>University</em> is too long a word",
                    "<em>U</em> is a consonant letter",
                    "The <em>u</em> is said like the word <em>you</em>, which is a consonant sound",
                    "<em>An</em> is only used before short words",
                ],
                "c": 2,
                "why": (
                    "The letter is a vowel letter. The sound is a consonant "
                    "sound. The rule that looks at the sound gets it right."
                ),
            },
            {
                "q": "On the lines the dictionary can score, how often is the sound rule right?",
                "a": [
                    "On 448 of 493",
                    "On about half",
                    "On 486 of 493",
                    "On every one of the 493",
                ],
                "c": 3,
                "why": (
                    "The sound rule is right on 493 of 493. The figure 486 "
                    "belongs to the letter rule, and 448 is the letter rule's "
                    "count on the play alone."
                ),
            },
            {
                "q": "The sound rule marks Austen's <em>an union</em> wrong. What is the best reading?",
                "a": [
                    "The sound rule is broken",
                    "Austen did not know English",
                    "<em>Union</em> begins with a vowel sound",
                    "Her habit in 1813 differed from the rule the page scores",
                ],
                "c": 3,
                "why": (
                    "<em>Union</em> begins with the sound of <em>you</em>, a "
                    "consonant sound, so today <em>a union</em> is the form. "
                    "The old habit is a fact about 1813."
                ),
            },
        ),
        "body": [
            ("p",
             "The rule you were taught is about letters, and letters are the "
             "wrong thing to look at. The lab holds 493 lines from three texts, "
             "each with an <em>a</em> or <em>an</em> and the word that follows."),
            ("p",
             "Counted on this page, the rule that puts <em>an</em> before a "
             "vowel letter is right on 486 of the 493 lines, which is 98.6%. "
             "Seven lines break it. Look at what they are: <em>a "
             "University</em>, <em>a utilitarian</em> and <em>an hour</em>, "
             "which the play uses five times."),
            ("h3", "Why the rule was ever about letters"),
            ("p",
             "Most words begin with the sound their first letter suggests, "
             "and a rule about letters is easier to teach than a rule about "
             "sounds. That is the whole reason. The rule is a short way of "
             "writing the real one, and it is a good short way: 98.6% is a "
             "high score."),
            ("h3", "The rule about sounds"),
            ("p",
             "Change the question to the first <em>sound</em> of the next "
             "word, and the rule is right on all 493 lines. Nothing about "
             "the lines changed. The question changed. The same words are in "
             "the same table, and the column that said <em>missed</em> is "
             "empty."),
            ("p",
             "The dictionary gives the sound. That is the sound of "
             "<em>hour</em>, which is the vowel in <em>our</em>, and of "
             "<em>University</em>, which starts as <em>you</em> does. Seven "
             "of these lines, and no more, are what separated the two rules "
             "here."),
            ("h3", "Three sources, one result"),
            ("p",
             "Switch the lab to the play, to the modern documents or to the "
             "passage from the novel. The play has 455 lines. The letter rule "
             "is right on 448 of them and the sound rule on all 455. On the "
             "modern documents both rules are right on 29 of 29, and on the "
             "passage both are right on 9 of 9. The table also sets aside ten "
             "marks that look like <em>a</em> but are not the word, such as "
             "<em>(a)</em> and a page number <em>21a</em>."),
            ("p",
             "The modern documents show that the two rules agree for most "
             "words. The play is where they part, and all seven lines that "
             "separate them are in it."),
            ("h3", "The whole novel, quoted"),
            ("p",
             "The page cannot carry the whole of <em>Pride and "
             "Prejudice</em>. A count made once, away from this page, over its 2,266 "
             "lines gives the letter rule 2,239 right (98.8%) and the sound "
             "rule 2,263 right (99.9%). That count is quoted here and not "
             "computed on this page. The three lines the sound rule misses "
             "are <em>an union</em>, twice, and <em>an uniform</em>. They are "
             "Austen's habit, and the habit has gone."),
            ("h3", "What the page cannot tell you"),
            ("p",
             "It reads one way of saying each word, the American one. In a "
             "different kind of English some words begin with a different "
             "sound, and the choice of <em>a</em> or <em>an</em> follows. "
             "The lab says so in its own words, under the numbers, and lists "
             "the 17 lines the dictionary cannot score."),
        ],
    },
    {
        "slug": "the-before-the-only-one",
        "module": "A, an and the",
        "title": "The Before the Only One",
        "one_line": "You say the tallest, and you also say a most interesting young man.",
        "standard": (
            "Finish when you can put the right small word before a superlative, "
            "same or next, and say when most does not make a superlative.",
            "You should be able to read the word before each of the printed "
            "words, state the score of the rule for each, sort the lines it "
            "misses into kinds, and name the sense of most that takes a and not "
            "the.",
        ),
        "summary": (
            "A <dfn>superlative</dfn> names the one that is more than all the "
            "others: <em>the tallest</em>, <em>the most beautiful</em>. Because "
            "there is only one, it takes <em>the</em>. On 142 lines from a novel "
            "with an <em>-est</em> word, <em>the</em> or a possessive stands "
            "before it 127 times. With <em>most</em> the same test is right on "
            "only 40 of 122, and the reason is a second meaning of the word."
        ),
        "key_label": "What stands before the word",
        "key": [
            "-est word      127 of 142   89.4%",
            "same            69 of 69   100.0%",
            "next            49 of 72    68.1%",
            "most            40 of 122   32.8%",
            "",
            "the most 37     a most 45",
        ],
        "concepts_intro": "Three ideas.",
        "concepts": (
            (
                "There is only one, so the word is the",
                "<em>The tallest</em> girl is one girl. <em>The same</em> "
                "thing is one thing. When only one can fit the word, you point "
                "to it with <em>the</em>. A <dfn>possessive</dfn>, such as "
                "<em>her</em> or <em>our</em>, points to it as well: <em>her "
                "youngest sister</em>. The scan counts both.",
            ),
            (
                "Some words take it every time, and some almost never",
                "The rule is right on every one of the 69 lines with "
                "<em>same</em>. It is right on 127 of 142 with an "
                "<em>-est</em> word. With <em>next</em> it is right on 49 of "
                "72, because <em>next</em> is often a time word that stands "
                "alone: <em>next week</em>.",
            ),
            (
                "Most has two jobs",
                "<em>The most beautiful</em> names the one. <em>A most "
                "agreeable man</em> does not: <em>most</em> there means "
                "<em>very</em>, and the small word before it is <em>a</em>. "
                "In the novel, <em>a most</em> before an <dfn>adjective</dfn>, a "
                "word such as <em>kind</em> or <em>tall</em> that describes a "
                "noun, is written 45 times, and <em>the most</em> 37 times.",
            ),
        ),
        "steps_title": "Choosing the small word in front",
        "steps_intro": "Five questions.",
        "steps": (
            (
                "Is there a group, and does the word pick one from it?",
                "<em>The tallest</em> of the girls picks one. If nothing is "
                "being compared, the word is not a superlative.",
            ),
            (
                "Does it end in -est, or is it same?",
                "Then put <em>the</em> before it, or a possessive such as "
                "<em>her</em> or <em>Darcy&rsquo;s</em>. <em>Same</em> takes "
                "<em>the</em> on all 69 printed lines.",
            ),
            (
                "Is it most, and does it mean the highest?",
                "If it is the highest of a group, use <em>the most</em>: "
                "<em>the most beautiful of the sisters</em>. If it means "
                "<em>very</em>, use <em>a most</em> or no small word: "
                "<em>a most agreeable man</em>, <em>she was most kind</em>.",
            ),
            (
                "Is it next?",
                "With a noun the plain form is <em>the next day</em>. As a "
                "time word it stands alone: <em>next week</em>, <em>next "
                "year</em>.",
            ),
            (
                "Check the lines that look like exceptions",
                "<em>The two youngest</em> has <em>the</em> one word earlier, "
                "and <em>the best and safest</em> has it once for both. The "
                "lab shows the word directly before, so such lines count as "
                "misses.",
            ),
        ),
        "lab": ("english", {
            "mode": "the_super",
            "rule": "est",
            "panel_title": "Read the word before each one",
            "panel_intro": (
                "Each line is taken from the novel around one word. The scan "
                "reads only the word directly before it. The rule holds when "
                "that word is <em>the</em> or a possessive such as <em>her</em> "
                "or <em>Darcy&rsquo;s</em>. Choose the word at the top and "
                "read the lines."
            ),
        }),
        "read_title": "The 15 lines with an -est word that do not fit",
        "read_intro": (
            "Choose the first word in the lab and read the lines marked "
            "<em>not the rule</em>. They are not mistakes in the novel."
        ),
        "worked": {
            "title": "Four kinds of line the plain test calls a miss",
            "intro": [
                "Of the 142 lines with an <em>-est</em> word, 15 do not have "
                "<em>the</em> or a possessive directly before it. They are "
                "four kinds.",
            ],
            "lines": [
                "the two youngest     the is a word earlier",
                "the best and safest  one the, two words",
                "it would be wisest   no noun follows",
                "dearest Lizzy        a way of calling her",
            ],
            "after": [
                "None of the four is a break in the rule. Four lines have a "
                "number between (<em>the two youngest</em>) and three have one "
                "<em>the</em> for two words joined by <em>and</em> (<em>the "
                "best and safest</em>): in these seven <em>the</em> or a "
                "possessive is there, but the scan reads one word only. Two "
                "stand alone after <em>be</em> (<em>it would be wisest</em>). "
                "Six are a way of calling someone, in a letter or in speech "
                "(<em>dearest Lizzy</em>, <em>dearest, loveliest "
                "Elizabeth</em>), with no <em>my</em> in front.",
                "The same is true of <em>next</em>. Of its 23 other lines, "
                "seven are a time that stands alone (<em>next week</em>, "
                "<em>next year</em>), four are <em>next to</em>, which names "
                "a place, eight have <em>next</em> on its own after a verb "
                "(<em>when they next met</em>), and four have <em>the</em> a "
                "word or two earlier (<em>the very next day</em>, <em>the two "
                "next</em>). And one of its four possessives is a false hit: "
                "the scan reads <em>her</em> in <em>congratulate her</em> as "
                "a possessive because the line has no full stop, and <em>Next "
                "to being married</em> begins a new sentence.",
            ],
        },
        "note": (
            "The lines are from a novel of 1813, and the scan reads words, not "
            "meanings. It cannot tell a <em>most</em> that means <em>very</em> "
            "from one that means <em>the most</em>, except by the <em>a</em> in "
            "front. <em>First</em> and <em>last</em> are not counted here. "
            "<em>At first</em> and <em>at last</em> are fixed phrases that "
            "take no <em>the</em>."
        ),
        "mistakes": (
            (
                "Believing that most always makes a superlative",
                "In the novel, <em>a most</em> before an adjective is written "
                "45 times and <em>the most</em> 37 times. <em>A most "
                "agreeable man</em> does not say that he is more agreeable "
                "than the others. It says he is very agreeable. The rule "
                "for <em>most</em> is right on only 40 of 122 lines, and that "
                "is the reason.",
            ),
            (
                "Leaving out the because a possessive is there",
                "Say <em>the youngest sister</em> or <em>her youngest "
                "sister</em>, not both. A possessive takes the place of "
                "<em>the</em>, it does not join it. The scan counts either "
                "one: 93 lines have <em>the</em> and 34 have a possessive.",
            ),
            (
                "Reading a miss in the lab as a mistake in the writing",
                "Fifteen lines with an <em>-est</em> word are marked "
                "&ldquo;not the rule&rdquo;. Read them. Each is a correct "
                "sentence that the scan, looking at one word, cannot judge.",
            ),
        ),
        "quiz_title": "Check yourself",
        "quiz": (
            {
                "q": "What does <em>a most agreeable man</em> say?",
                "a": [
                    "He is the most agreeable man there is",
                    "He is a very agreeable man",
                    "He is less agreeable than other men",
                    "<em>Agreeable</em> is a noun here",
                ],
                "c": 1,
                "why": (
                    "After <em>a</em>, the word <em>most</em> means "
                    "<em>very</em>. A superlative would need <em>the</em>."
                ),
            },
            {
                "q": "Which sentence is right?",
                "a": [
                    "Lizzy is youngest girl in the room.",
                    "Lizzy is a youngest girl in the room.",
                    "Lizzy is most young girl in the room.",
                    "Lizzy is the youngest girl in the room.",
                ],
                "c": 3,
                "why": (
                    "There is one youngest girl, so the small word is "
                    "<em>the</em>. <em>Most young</em> is not how English "
                    "forms this; <em>-est</em> goes on a short adjective, as "
                    "the course Small Words and Comparisons scores."
                ),
            },
            {
                "q": "The scan counts 15 lines with an <em>-est</em> word as not fitting the rule. Which of these is one of them?",
                "a": [
                    "<em>the tallest girl</em>",
                    "<em>the two youngest</em>",
                    "<em>her greatest relief</em>",
                    "<em>the earliest of those</em>",
                ],
                "c": 1,
                "why": (
                    "In <em>the two youngest</em> the small word is <em>the</em>, "
                    "but the word directly before <em>youngest</em> is "
                    "<em>two</em>. The other three have <em>the</em> or "
                    "<em>her</em> directly before."
                ),
            },
            {
                "q": "Why is the rule right on only 40 of 122 lines with <em>most</em>?",
                "a": [
                    "<em>Most</em> is not a word",
                    "The rule is wrong for superlatives",
                    "Many lines use <em>most</em> to mean <em>very</em>, and 45 have <em>a</em> before it",
                    "The novel has few lines with <em>most</em>",
                ],
                "c": 2,
                "why": (
                    "The rule is right for the superlative and does not "
                    "apply to the other sense. The lab prints the word before "
                    "each line, so you can see the 45 with <em>a</em>."
                ),
            },
        ),
        "body": [
            ("p",
             "Take a word that names the one that is more than all the "
             "others: <em>tallest</em>, <em>youngest</em>, <em>greatest</em>. "
             "Because only one thing can be the tallest, the small word before "
             "it is <em>the</em>. The same is true of <em>same</em>, which "
             "names the one that is no different."),
            ("p",
             "The lab holds 405 lines from the novel, each with one of four "
             "words in the middle: an <em>-est</em> word, <em>same</em>, "
             "<em>next</em> or <em>most</em> before an adjective. The scan "
             "reads the word directly before it."),
            ("h3", "Three words that follow the rule"),
            ("p",
             "Counted on this page, the rule is right on 127 of the 142 "
             "lines with an <em>-est</em> word: 93 with <em>the</em> and 34 "
             "with a possessive, such as <em>her</em> or <em>our</em>. For "
             "<em>same</em> it is right on 69 of 69. That is the strongest "
             "rule in this course."),
            ("p",
             "<em>Next</em> is weaker: 49 of 72, or 68.1%. The reason is not a "
             "different meaning but a different use. <em>Next week</em> is "
             "a time, and it stands alone; <em>next to</em> names a place; "
             "and in <em>when they next met</em> the word is not before a "
             "noun at all."),
            ("h3", "What the 15 are"),
            ("p",
             "The 15 lines that do not fit are of four kinds. In "
             "<em>the two youngest</em> and <em>the best and safest</em>, "
             "<em>the</em> is there and the scan, which reads one word, does "
             "not see it. In <em>it would be wisest</em> there is no noun to "
             "point to. In <em>dearest Lizzy</em> the word is a name. So the "
             "rule is nearly right, and the misses are lines it cannot read."),
            ("h3", "The word that is two words"),
            ("p",
             "Choose <em>most</em>. Now the rule is right on 40 of 122 "
             "lines, which is 32.8%. Look at the column: the small word "
             "before <em>most</em> is <em>the</em> 37 times, a possessive "
             "3 times, and <em>a</em> or <em>an</em> 45 times. The other 37 "
             "have no small word at all."),
            ("p",
             "The 45 are the lesson. <em>A most delightful evening</em> and "
             "<em>a most excellent ball</em> do not name the best evening or "
             "the best ball. <em>Most</em> means <em>very</em>, and the "
             "small word is the one you use before any adjective and noun. "
             "Fifteen of the 37 others follow <em>was</em>, <em>been</em>, "
             "<em>am</em>, <em>is</em>, <em>be</em> or <em>seemed</em>: "
             "<em>she was most kind</em>. There too <em>most</em> means "
             "<em>very</em>."),
            ("h3", "What to do with it"),
            ("p",
             "Ask what the word is doing. If it picks the one from a group, "
             "use <em>the</em>. If it means <em>very</em>, use the small "
             "word you would use without it. The page can count the word "
             "before, but it cannot read meaning, so the second step is "
             "yours."),
            ("p",
             "The lines are from 1813. The meaning of <em>very</em> for "
             "<em>most</em> is old and formal, and is less common now. The "
             "lab cannot say how much less."),
        ],
    },
]
