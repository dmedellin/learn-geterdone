# -*- coding: utf-8 -*-
"""Lessons one and two of the tense course: building the table, then scoring it.

The prose here is written inside the NGSL 2,809, because the Subject tells its
reader that 98% coverage is what reading needs and a page that teaches that at
90% has failed its own lesson. `scripts/bandcheck.py` is the check. One glossary
term, `dictionary`, is defined where the list-cleaning is explained (lesson two).

Lesson one states no hit rate. It builds the table and sends the reader to lesson
two by title. Lesson two carries every figure of the scoring half, and each is
one the page computes: the hit rates and the missed words are read off the
`Score a rule on the list` menu of the table lab with `labcheck.js --observe`
(1209, 1202 and 1201 of 1210; the variants 1207 and 1205). The count of 146
words left out, 90 of them irregular verbs, is the length of the list the lab
prints under `List`.

Runs that need a spoken form are listed in
content/spoken/english_c1_tense_tables.py: the key and worked lines that hold an
ending such as -ing or a plus sign.
"""

LESSONS = [
    # ---------------------------------------------------------------- 01
    {
        "slug": "five-forms-and-the-whole-table",
        "module": "A table you can build",
        "title": "Five Forms Make Twelve",
        "one_line": "Learn five forms of a verb and the twelve boxes fill themselves.",
        "standard": (
            "Finish when you can build the full table for a verb you have never "
            "seen, and name the rule that made each form.",
            "You should be able to take any regular verb, write its five forms "
            "by rule, say which of the four rules fired and why, and fill all "
            "twelve boxes by placing <em>have</em>, <em>be</em> and <em>will</em> "
            "in front of those forms.",
        ),
        "summary": (
            "A tense table has twelve boxes. Books print them and ask you to learn "
            "them. You do not have to. Every box is built from five forms of the "
            "verb, and four of those five follow rules you can state in one line "
            "each. This lesson gives you the rules and a table that fills itself "
            "for any verb you type."
        ),
        "key_label": "The five forms, and what fills the table",
        "key": [
            "base            walk",
            "he, she, it     walks",
            "-ing form       walking",
            "past            walked",
            "after have      walked",
            "",
            "two boxes are a form on its own",
            "ten are a form with have, be or will in front",
        ],
        "concepts_intro": "Three ideas carry the whole lesson.",
        "concepts": [
            (
                "Twelve boxes, but not twelve things to learn",
                "The table has three times down the side and four shapes across "
                "the top. That makes twelve boxes. But you never learn twelve forms "
                "of a verb, because ten of the boxes are the same few forms with "
                "<em>have</em>, <em>be</em> or <em>will</em> placed in front of "
                "them, and the other two are a form on its own. Learn five forms "
                "and you can write any box.",
            ),
            (
                "Four of the five follow a rule",
                "Only the base form has to be learned. The other four are made from "
                "it: add <em>-s</em>, add <em>-ing</em>, add <em>-ed</em>. What "
                "makes English feel hard is that each rule has a small change for "
                "certain endings, and those changes are what this lesson states "
                "exactly.",
            ),
            (
                "A rule is a claim, and a claim can be checked",
                "Anyone can give you a rule. The question is how often it is "
                "right. The rules in this lesson are the ones the lab runs, and "
                "the next lesson, &ldquo;Scoring a Rule on 1,210 Real "
                "Verbs&rdquo;, runs them over a printed list and counts. Here you "
                "only need to know that each one is a rule you can state and test, "
                "not a feeling about English.",
            ),
        ],
        "steps_title": "Building a box",
        "steps_intro": "To write any box of the table, do this.",
        "steps": [
            (
                "Start from the base form",
                "The form you would find in a word list. This is the one form you "
                "have to learn; the rest are made from it.",
            ),
            (
                "Make the other four forms",
                "Add <em>-s</em>, <em>-ing</em> and <em>-ed</em> by the rules "
                "below, or look the verb up if it is one of the few that break "
                "them. The lab names the rule it used beside each form.",
            ),
            (
                "Choose the time you mean",
                "Now, before, or later. This picks the row of the table.",
            ),
            (
                "Put the small word in front",
                "<em>Have</em> to look back, <em>be</em> with the <em>-ing</em> "
                "form for something still going on, <em>will</em> to move it later. "
                "This picks the column, and the box is written.",
            ),
        ],
        "lab": ("english", {
            "mode": "table",
            "panel_title": "Type any verb and watch the table fill",
            "panel_intro": (
                "Nothing here is looked up except the six verbs the page marks "
                "irregular. The three forms at the top are made by the rules this "
                "lesson states, and the box beside them names the rule that "
                "fired, so you can check the answer against the reason for it. "
                "Type a verb that is not in the list and the same rules run, with "
                "one gap: the page cannot hear a word it does not carry, so for a "
                "new verb it treats the last part as the strong part. The menu "
                "under <em>Score a rule on the list</em> counts how often a rule "
                "is right, and the next lesson, &ldquo;Scoring a Rule on 1,210 "
                "Real Verbs&rdquo;, shows what it prints."
            ),
        }),
        "read_title": "One verb, five forms, four boxes",
        "read_intro": (
            "Take <em>walk</em>. Write its five forms, then build four of the "
            "twelve boxes from them. The lab does the same for any verb you type."
        ),
        "worked": {
            "title": "walk, and four of its twelve boxes",
            "intro": [
                "The five forms come first. Then each box is one form with a small "
                "word in front, or no small word at all.",
            ],
            "lines": [
                "walk            the base",
                "walks           he, she, it",
                "walking         the -ing form",
                "walked          the past, and the form after have",
                "",
                "she walks             a form on its own",
                "she is walking        be + the -ing form",
                "she has walked        have + the form after have",
                "she has been walking  have + been + the -ing form",
            ],
            "after": [
                "The last box has two small words in front. <em>Has been</em> is "
                "<em>have</em> and <em>be</em> together, and <em>walking</em> is "
                "the <em>-ing</em> form behind them. Nothing new was learned: "
                "<em>walking</em> was already one of the five forms.",
                "Try <em>stop</em>, <em>carry</em> and <em>hope</em> in the lab. "
                "The five forms change, <em>stopping</em>, <em>carries</em>, "
                "<em>hoping</em>, and the box beside them says which rule did it. "
                "The twelve boxes do not change at all. <em>Have</em>, <em>be</em> "
                "and <em>will</em> have forms of their own, <em>has</em>, "
                "<em>was</em>, <em>been</em>, and the course called Helping Verbs "
                "takes those one at a time.",
            ],
        },
        "note": (
            "Five forms and four rules is a small thing to hold. Twelve boxes for "
            "every verb you meet is a very large one."
        ),
        "mistakes": [
            (
                "Treating the twelve boxes as twelve things to learn",
                "Twelve boxes for every verb is a very large number of things to "
                "hold. Five forms and four rules is a small one, and it works on a "
                "verb you have never met.",
            ),
            (
                "Doubling the last letter when the strong part is early",
                "<em>Stop</em> becomes <em>stopping</em>, but <em>listen</em> does "
                "not become <em>listenning</em>. The letter only doubles when the "
                "last part of the word is the strong part, which is why the rule "
                "needs the sound and not only the letters.",
            ),
            (
                "Putting -s or -ed on the verb behind will",
                "After <em>will</em> the verb is the base form: <em>she will "
                "walk</em>, not <em>she will walks</em>. After <em>have</em> it is "
                "the form after have: <em>she has walked</em>. The small word "
                "decides which form follows it.",
            ),
        ],
        "quiz_title": "Check yourself",
        "quiz": [
            {
                "q": "How many forms of a verb do you need to write any of the twelve boxes?",
                "a": ["Twelve", "Three", "Five", "Ten"],
                "c": 2,
                "why": (
                    "Five. The other boxes are those forms with <em>have</em>, "
                    "<em>be</em> or <em>will</em> placed in front. Ten is the "
                    "number of boxes that take a small word, not the number of "
                    "forms."
                ),
            },
            {
                "q": "Why does <em>stop</em> double its last letter but <em>listen</em> not?",
                "a": [
                    "The strong part of <em>stop</em> is at the end",
                    "<em>listen</em> is irregular",
                    "<em>stop</em> is shorter",
                    "Only verbs with one part ever double",
                ],
                "c": 0,
                "why": (
                    "The letter doubles when the word ends consonant, vowel, "
                    "consonant <em>and</em> the last part is the strong part. "
                    "In <em>listen</em> the strong part is the first one. Verbs "
                    "with two parts double too when the second is strong: "
                    "<em>admit</em>, <em>admitting</em>."
                ),
            },
            {
                "q": "Which form of <em>walk</em> comes after <em>will</em>?",
                "a": ["<em>walks</em>", "<em>walked</em>", "<em>walking</em>", "<em>walk</em>"],
                "c": 3,
                "why": (
                    "The base form. <em>Will</em> moves the box later and the verb "
                    "stays as it is in the word list: <em>she will walk</em>."
                ),
            },
            {
                "q": "<em>She has been walking</em> is built from which pieces?",
                "a": [
                    "<em>has</em> and the form after have",
                    "<em>has been</em> and the <em>-ing</em> form",
                    "<em>is</em> and the <em>-ing</em> form",
                    "<em>has</em> and the base",
                ],
                "c": 1,
                "why": (
                    "<em>Has been</em> is <em>have</em> and <em>be</em> together, "
                    "and the <em>-ing</em> form comes behind them. <em>She has "
                    "walked</em> uses the form after have, with no <em>been</em>."
                ),
            },
        ],
        "body": [
            ("p",
             "Open any book for learners and you will find a page with twelve boxes "
             "on it. Three times: now, before, later. Four shapes for each. "
             "Every box has a name, and the book asks you to learn the names and "
             "the forms that go in them."),
            ("p",
             "You do not have to do that, and this lesson is about why."),
            ("h3", "The five forms"),
            ("p",
             "A verb in English has five forms. For <em>walk</em> they are "
             "<em>walk</em>, <em>walks</em>, <em>walking</em>, <em>walked</em>, "
             "and the form used after <em>have</em>, which for this verb is also "
             "<em>walked</em>. One verb has more: <em>be</em> has eight "
             "(<em>am</em>, <em>is</em>, <em>are</em>, <em>was</em>, "
             "<em>were</em>, <em>be</em>, <em>being</em>, <em>been</em>), and "
             "the course called Irregular Verbs sets it apart from every other "
             "verb. The small helping words, <em>will</em> among them, have "
             "fewer, and they only ever stand in front."),
            ("p",
             "Those five fill all twelve boxes. Two of the boxes, <em>walk</em> "
             "and <em>walked</em>, are a form on its own. The other ten are simply "
             "one of these forms with a small word in front of it. <em>Have</em> "
             "gives you the shape that looks back from now. <em>Be</em> with the "
             "<em>-ing</em> form gives you the shape that is still going on. "
             "<em>Will</em> moves the whole thing later. That is the entire table."),
            ("ul", [
                "<strong>Simple</strong>: the verb on its own, or with "
                "<em>will</em>. <em>She walks. She walked. She will walk.</em>",
                "<strong>Progressive</strong>: <em>be</em> and the <em>-ing</em> "
                "form. <em>She is walking. She was walking. She will be "
                "walking.</em>",
                "<strong>Perfect</strong>: <em>have</em> and the form after "
                "have. <em>She has walked. She had walked. She will have "
                "walked.</em>",
                "<strong>Perfect progressive</strong>: <em>have</em>, "
                "<em>been</em> and the <em>-ing</em> form. <em>She has been "
                "walking. She had been walking. She will have been "
                "walking.</em>",
            ]),
            ("h3", "The rules that make four of the five"),
            ("p",
             "You learn the base form when you learn the word. The other four come "
             "from rules, and here they are, exactly as the lab runs them."),
            ("ul", [
                "For <em>he</em>, <em>she</em> or <em>it</em>, add <em>-s</em>. "
                "After a hissing sound, add <em>-es</em>: <em>passes</em>, "
                "<em>wishes</em>, <em>watches</em>. After a consonant and "
                "<em>-y</em>, the <em>-y</em> becomes <em>-ies</em>: "
                "<em>carries</em>. After a consonant and <em>-o</em>, add "
                "<em>-es</em> as well: <em>goes</em>.",
                "For the <em>-ing</em> form, add <em>-ing</em>, dropping a silent "
                "<em>-e</em> first: <em>hope</em>, <em>hoping</em>. A verb ending "
                "<em>-ie</em> becomes <em>-ying</em>: <em>lie</em>, <em>lying</em>. "
                "A verb ending <em>-ee</em>, <em>-oe</em> or <em>-ye</em> keeps "
                "its <em>-e</em>: <em>see</em>, <em>seeing</em>.",
                "For the past, add <em>-ed</em>. After a silent <em>-e</em> only "
                "<em>-d</em> is needed, <em>hope</em>, <em>hoped</em>, and the "
                "<em>-y</em> change is the same: <em>carry</em>, <em>carried</em>.",
                "If the word ends consonant, vowel, consonant, the last letter is "
                "not <em>w</em>, <em>x</em> or <em>y</em>, and the last part is "
                "the strong part, double that last letter before <em>-ing</em> "
                "and <em>-ed</em>: <em>stop</em>, <em>stopping</em>, "
                "<em>stopped</em>. Nothing ever doubles before <em>-s</em>.",
            ]),
            ("p",
             "That last rule is the only one needing the sound of the word and not "
             "only its letters. <em>Stop</em> is one part, so the last part is the "
             "strong part, and it doubles: <em>stopping</em>. <em>Listen</em> has "
             "two parts and the strong one is the first, so nothing doubles: "
             "<em>listening</em>. The lesson &ldquo;When the Last Letter "
             "Doubles&rdquo; takes this rule apart on its own."),
            ("p",
             "The lab applies all four, and it prints the one that fired beside "
             "every answer. Type a verb, read the three forms, then read the "
             "reason. If you had a different answer, find which rule you used "
             "and which one the lab used. The list of 1,210 verbs under the lab "
             "is the one the next lesson, &ldquo;Scoring a Rule on 1,210 Real "
             "Verbs&rdquo;, scores these rules on, with the words they miss."),
        ],
    },
    # ---------------------------------------------------------------- 02
    {
        "slug": "scoring-a-rule-on-real-verbs",
        "module": "A rule needs a count",
        "title": "Scoring a Rule on 1,210 Real Verbs",
        "one_line": "A rule you cannot count is an opinion; this one is counted, and every miss is printed.",
        "standard": (
            "Finish when you can read a rule's hit rate off the printed list, "
            "name the reason for each word it misses, and say why the list had "
            "to be cleaned first.",
            "You should be able to run each of the three forming rules over the "
            "list, read its score and every word it misses, sort the misses into "
            "kinds, say which rule change made the results worse and why, and "
            "explain why a list can make a right rule look wrong.",
        ),
        "summary": (
            "The last lesson stated rules. This one counts them. Each rule is run "
            "over 1,210 regular verbs and checked against the forms a word list "
            "records, and each is right more than 99 times in 100. The nine words "
            "the past rule misses are the content: every one has a reason, and "
            "one rule added for good reasons made the score worse."
        ),
        "key_label": "Three rules, 1,210 verbs",
        "key": [
            "-s 99.92%    -ing 99.34%    -ed 99.26%",
            "",
            "1,210 verbs, every miss printed",
            "a rule plus a short list of misses",
            "beats a long list of everything",
        ],
        "concepts_intro": "Three ideas, and the last is the one that saves time.",
        "concepts": [
            (
                "A hit rate is a count, not a feeling",
                "The lab runs the rule on every verb in the printed list and "
                "marks it right when the form it writes is one the list records. "
                "The share right is the number of rights over the number of "
                "verbs. Nobody had to be asked their opinion, and you can read "
                "every row.",
            ),
            (
                "Every miss has a reason",
                "A rule that is right 99.26% of the time is wrong on nine verbs. "
                "Those nine are not random. A British spelling, a letter no "
                "rule knows about, a word that doubles against the strong part: "
                "each kind can be named, and a named kind is something you can "
                "learn once.",
            ),
            (
                "A rule plus a short list beats a long list",
                "The alternative to a rule is a list of every form of every "
                "verb. The rule is right on all but nine, and the nine fit on "
                "one line. That is the whole saving, and it is why the rule "
                "is worth learning.",
            ),
        ],
        "steps_title": "Scoring a rule yourself",
        "steps_intro": "To judge any rule, do this.",
        "steps": [
            (
                "Choose the rule",
                "Pick one under <em>Score a rule on the list</em>. The lab names "
                "it in words beside the score.",
            ),
            (
                "Read the count and the share",
                "<em>Right</em> is how many verbs the rule got right out of how "
                "many it was run on. <em>Share right</em> is the same count as a "
                "percent.",
            ),
            (
                "Read every word it missed",
                "The table under the score lists each one, with the form the "
                "rule wrote and the forms the list records.",
            ),
            (
                "Sort the misses into kinds and name each kind",
                "A spelling that differs by country, a letter the rule does not "
                "know, a strong part it cannot hear. A kind with one word is a "
                "word to learn; a kind with ten is a new rule.",
            ),
        ],
        "lab": ("english", {
            "mode": "table",
            "focus": "score",
            "show": "residue",
            "panel_title": "Score a rule on the printed list",
            "panel_intro": (
                "The score comes first on this page. Choose a rule under "
                "<em>Score a rule on the list</em> and the page runs it on every "
                "regular verb in a list of the 2,800 most common words of "
                "English, 1,210 verbs, and counts the verbs where the form it "
                "writes is a spelling the list records. The table prints every "
                "word the rule misses; under <em>List</em> you can print every "
                "verb, or the words that were left out and the reason for each. "
                "The twelve boxes are below the score, and they work as before."
            ),
        }),
        "read_title": "What the rules got wrong",
        "read_intro": (
            "The rules are run over every regular verb in a list of the 2,800 "
            "most common words, and checked against the forms that list itself "
            "records. Here is how they did, and what they missed."
        ),
        "worked": {
            "title": "The nine verbs the past rule misses",
            "intro": [
                "Choose the past rule in the lab. It is right on 1201 of 1210 "
                "verbs, and the table lists the nine it is not.",
            ],
            "lines": [
                "-ed     1201 of 1210 right     99.26%",
                "",
                "British spelling                 initial, counsel",
                "a -k no rule knows               panic, traffic",
                "doubles against the strong part  format, input, output",
                "both spellings in use            bus",
                "no consonant before the vowel    up",
            ],
            "after": [
                "<em>Initial</em> and <em>counsel</em> are written one way in "
                "British English and another in American English. The list "
                "records only the British <em>-ll-</em>, so the rule's American "
                "form is marked wrong where nothing is wrong. <em>Panic</em> and "
                "<em>traffic</em> take a <em>-k</em> before the ending, "
                "<em>panicking</em>, which no rule here knows. <em>Format</em>, "
                "<em>input</em> and <em>output</em> double their last letter "
                "though the strong part comes first. <em>Bus</em> is "
                "<em>busing</em> in the list where the rule writes "
                "<em>bussing</em>, and writers use both. And <em>up</em> has no "
                "consonant before its vowel, so the rule never doubles it.",
                "The <em>-ing</em> rule misses the same words without "
                "<em>counsel</em>, which is eight. The <em>-s</em> rule misses "
                "one: <em>stomach</em> ends in <em>-ch</em> but does not hiss, "
                "so the rule writes <em>stomaches</em> and the list records "
                "<em>stomachs</em>. The rule reads letters and cannot hear.",
            ],
        },
        "note": (
            "The three lists of missed words are short enough to learn directly. "
            "That is the whole saving: a rule plus a short list beats a long list."
        ),
        "mistakes": [
            (
                "Believing a rule because it sounds right",
                "A rule turning <em>-f</em> into <em>-ves</em> looks correct, and "
                "for nouns it often is. Added here it made the results worse, "
                "because <em>brief</em>, <em>golf</em>, <em>proof</em> and "
                "<em>roof</em> are all verbs that simply add <em>-s</em>. The "
                "count caught it; the ear did not.",
            ),
            (
                "Scoring a rule against a list that is wrong",
                "The raw list had <em>offerring</em> and <em>commiting</em>. "
                "Scored against that, a right rule looks wrong and a wrong rule "
                "looks right. Read the list before you trust the score.",
            ),
            (
                "Reading a high score as a finished rule",
                "99.26% still leaves nine verbs. The score tells you how much is "
                "left; the words tell you what it is. A rule with its misses "
                "printed is a tool, and a rule with only its score is a claim.",
            ),
        ],
        "quiz_title": "Check yourself",
        "quiz": [
            {
                "q": "The past rule is right on 1201 of 1210 verbs. What is the useful thing to do with the other nine?",
                "a": [
                    "Throw the rule away",
                    "Ignore them, because 99.26% is high",
                    "Write a new rule for each word",
                    "Read them, because each has a reason you can name",
                ],
                "c": 3,
                "why": (
                    "The nine fall into five kinds, and each kind has a cause: a "
                    "British spelling, a <em>-k</em>, a doubling against the "
                    "strong part, a word written two ways, a word with no "
                    "consonant before its vowel. Knowing the kinds is the saving."
                ),
            },
            {
                "q": "Why was the word list cleaned before any rule was scored on it?",
                "a": [
                    "It was too long to read",
                    "It recorded spellings nobody writes, so a right rule looked wrong",
                    "It had capital letters in it",
                    "The rules could not read the raw list",
                ],
                "c": 1,
                "why": (
                    "The list was made by a machine and held forms such as "
                    "<em>offerring</em>. A rule that wrote <em>offering</em> was "
                    "marked wrong, and one that wrote the machine's mistake "
                    "would have been marked right."
                ),
            },
            {
                "q": "Why did the rule turning <em>-f</em> into <em>-ves</em> make the <em>-s</em> score worse?",
                "a": [
                    "<em>Brief</em>, <em>golf</em>, <em>proof</em> and <em>roof</em> are verbs that take plain <em>-s</em>",
                    "No noun ends in <em>-f</em>",
                    "The rule was written wrongly",
                    "The list has no words ending in <em>-f</em>",
                ],
                "c": 0,
                "why": (
                    "The rule is true of nouns such as <em>leaf</em>. The list is "
                    "of verbs, and verbs ending in <em>-f</em> simply add "
                    "<em>-s</em>. The score fell from 1209 to 1205 of 1210."
                ),
            },
            {
                "q": "<em>Panic</em> becomes <em>panicking</em>. Which kind of miss is that?",
                "a": [
                    "A British spelling",
                    "A word written two ways",
                    "A <em>-k</em> that no rule here knows about",
                    "A doubling against the strong part",
                ],
                "c": 2,
                "why": (
                    "<em>Panic</em> and <em>traffic</em> take a <em>-k</em> "
                    "before the ending. The rules do not know that, so they "
                    "write <em>panicing</em>, and the list records the "
                    "<em>-k</em> form."
                ),
            },
        ],
        "body": [
            ("p",
             "A rule with no number beside it is only an opinion. The last lesson "
             "gave you four rules that build the forms of a verb. This one asks "
             "how good they are, and the answer is a count."),
            ("h3", "How the count is made"),
            ("p",
             "The rules are run, on this page, over the 1,210 regular verbs in a "
             "list of the 2,800 most common English words. For each verb the rule "
             "writes a form, and the form is checked against the forms the list "
             "already records for that verb. A match is a hit and anything else "
             "is a miss. The lab prints both."),
            ("p",
             "They are right 99.92% of the time for <em>-s</em>, 99.34% for "
             "<em>-ing</em>, and 99.26% for the past. All three are counted on "
             "this page: 1209 of 1210, 1202 of 1210 and 1201 of 1210. The words "
             "they miss are listed in the lab and again in the worked example, "
             "and there are not many."),
            ("h3", "Reading the misses"),
            ("p",
             "The nine words the past rule misses are not random, and not all of "
             "them are mistakes. They sort into five kinds."),
            ("ul", [
                "<strong>A spelling that differs by country</strong>: "
                "<em>initial</em> and <em>counsel</em>. The list has only the "
                "British <em>-ll-</em>, so the American form is marked wrong "
                "where nothing is wrong.",
                "<strong>A letter no rule here knows</strong>: <em>panic</em> and "
                "<em>traffic</em> take a <em>-k</em>.",
                "<strong>Doubling against the strong part</strong>: "
                "<em>format</em>, <em>input</em> and <em>output</em>.",
                "<strong>Both spellings in use</strong>: <em>bus</em>, "
                "<em>busing</em> in the list and <em>bussing</em> from the rule.",
                "<strong>No consonant before the vowel</strong>: <em>up</em>, "
                "where the rule never doubles.",
            ]),
            ("p",
             "Each kind has a reason you can state. That is what a hit rate "
             "should come with, and it is why the lab prints the words and not "
             "only the number."),
            ("h3", "The list had to be cleaned first"),
            ("p",
             "The word list was made by a machine, and a machine can record a "
             "spelling nobody writes. The raw list had <em>offerring</em>, "
             "<em>commiting</em> and <em>councilling</em>; it gave verb forms to "
             "words that are not verbs, such as <em>able</em> and <em>son</em>; "
             "and it recorded <em>comed</em> and <em>maked</em>, so the past rule "
             "was being marked right for forms nobody writes. Scored against that "
             "list, a right rule looks wrong and a wrong rule looks right."),
            ("p",
             "So the list was cleaned by one test, applied to every spelling the "
             "same way: a spelling stays if a <dfn>dictionary</dfn>, a book that "
             "records the real spellings of a language, has it, or if it is the "
             "British spelling of one the dictionary has. In all, 146 words were "
             "left out, each with its reason, and the lab prints them all under "
             "<em>List</em>. Ninety of them are irregular verbs, left out because "
             "their past is not made by any rule; the course called Irregular "
             "Verbs takes them."),
            ("h3", "A rule that sounded right and was not"),
            ("p",
             "When the <em>-s</em> rule first ran, every <em>-o</em> took "
             "<em>-es</em>, and it turned <em>radio</em> and <em>video</em> into "
             "forms nobody writes. Choose <em>the -s rule before the -o fix</em> "
             "in the lab and you can watch it: 1207 of 1210, 99.75%, with "
             "<em>radio</em> and <em>video</em> among the misses. The fix was "
             "easy: <em>-o</em> takes <em>-es</em> only after a consonant, as in "
             "<em>goes</em>, and plain <em>-s</em> after a vowel."),
            ("p",
             "At the same time a second rule was added, because it also looked "
             "right: <em>-f</em> becomes <em>-ves</em>. For nouns that is often "
             "true: one <em>leaf</em>, two <em>leaves</em>. Choose it in the lab "
             "and the count falls to 1205 of 1210, 99.59%, because "
             "<em>brief</em>, <em>golf</em>, <em>proof</em> and <em>roof</em> are "
             "verbs and they simply take <em>-s</em>."),
            ("p",
             "This is worth more than any single rule in the lesson. A rule can "
             "sound right, come from a real pattern, and still cost you accuracy. "
             "The only way to know is to run it over real words and count. That is "
             "what every lesson on this path does."),
        ],
    },
]
