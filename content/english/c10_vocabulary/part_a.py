# -*- coding: utf-8 -*-
"""Vocabulary and Reading, lessons one to three (all use the coverage lab).

Every figure is read off a lab tile with labcheck.js --observe unless marked
quoted. See the course docstring for the full list.

Spoken forms: content/spoken/english_c10_vocabulary.py.
"""

LESSONS = [
    {
        "slug": "how-much-of-a-page-you-know",
        "module": "How much you know",
        "title": "How Much of a Page You Know",
        "one_line": "Check every word of a page against the list, and read the share you know and the words you do not.",
        "standard": (
            "Finish when you can say what share of a page a word list covers, and what is missing.",
            "You should be able to read the share for the first 1,000, "
            "2,000 and 2,800 words off the lab, say what a name does to the "
            "share, compare it with the 98% a reader needs, work out how "
            "many words of a page that gap stands for, and test a text of "
            "your own.",
        ),
        "summary": (
            "A page is a count of words, and a list of words either has each "
            "one or does not. On a passage from a novel, the 2,800 words of "
            "the list cover 91.0% of what is printed, and 94.3% once names "
            "are set apart. A reader needs 98%. The gap is not a feeling "
            "about difficulty: it is a list of words you can read off the "
            "page, and this lesson shows you how to find it for any text."
        ),
        "key_label": "Three printed texts, all 2,800 words",
        "key": [
            "the passage          91.0%   94.3% with names",
            "the play excerpt     85.9%   94.6% with names",
            "the modern papers    87.3%   92.7% with names",
            "",
            "a reader needs       98%   quoted from Nation",
        ],
        "concepts_intro": "Three ideas. The third is the one most people get wrong.",
        "concepts": (
            (
                "Coverage counts every word, each time it appears",
                "The passage has 936 words and 361 different ones. If the "
                "list has <em>the</em>, then all 26 times that <em>the</em> "
                "appears count as known. This is why a short list of common "
                "words does so much: the first 1,000 words cover 85.0% of "
                "the passage, and the next 1,000 add only 4.2 points, to "
                "89.2%. The rest of the list adds 1.8 more, to 91.0%.",
            ),
            (
                "A name is read, not learned",
                "A word in capitals in the middle of a sentence, such as "
                "<em>Darcy</em> or <em>Meryton</em>, is a name, and nobody "
                "looks a name up. The lab sets names apart. With them the "
                "passage is covered 94.3%, the play 94.6% and the modern "
                "documents 92.7%. This is the fairer figure to hold against "
                "a reader's 98%.",
            ),
            (
                "98% is a high bar, and the gap is a list",
                "Nation (2006) puts the share a reader needs for an easy "
                "read at 98%, which is one unknown word in every 50. The "
                "passage has 936 words, so 98% would leave about 19 words "
                "unknown. After names and families, the lab finds 41. The "
                "words that make up the gap are printed, and a list of 41 "
                "can be learned.",
            ),
        ),
        "steps_title": "Reading a figure for a text in front of you",
        "steps_intro": "Five steps, in this order.",
        "steps": (
            (
                "How many words did the lab read?",
                "Look at the first number. A share of a short text moves a lot "
                "when one word changes, which is why the lab asks for fifty "
                "words or more.",
            ),
            (
                "Read the three shares for the list",
                "The first 1,000 words, the first 2,000 and all 2,800. Each "
                "step adds less than the one before, and that is how the "
                "list was made: the commonest words first.",
            ),
            (
                "Read the share with names",
                "This is the figure to hold against 98%. If it is above, you "
                "can read the text without looking words up. If it is "
                "below, the next step says how far.",
            ),
            (
                "Turn the gap into words",
                "Take the share from 100 and divide 100 by what is left. "
                "At 94.3% the gap is 5.7, and 100 divided by 5.7 is about 18, so about "
                "one word in 18 is a word you may not know. At 98% it is one "
                "in 50.",
            ),
            (
                "Read the table of words not covered",
                "Sort them into kinds before you learn them. A word that "
                "appears twice is worth more than a word that appears once.",
            ),
        ),
        "lab": ("english", {
            "mode": "coverage",
            "text": "passage",
            "show": "bands",
            "panel_title": "Check a page against the 2,800 words",
            "panel_intro": (
                "Every word of the text is checked against the 2,800 "
                "headwords. A form such as <em>walked</em> or "
                "<em>happier</em> counts when the rules of the earlier "
                "courses turn it back into a headword. Choose the passage "
                "(1813), the excerpt from the play (1895), the two modern "
                "documents, or &ldquo;a text of your own&rdquo; and paste "
                "fifty words or more. The table lists the words that are "
                "not covered and the names."
            ),
        }),
        "read_title": "The 41 words the passage leaves",
        "read_intro": (
            "The table under the numbers lists every word the lab could not "
            "cover. Read it once through before you read the next section."
        ),
        "worked": {
            "title": "The passage's words not covered, in kinds",
            "intro": [
                "Here are all 41 words from the table under the passage, "
                "sorted into seven kinds by what they have in common. The "
                "table prints 40 rows, because <em>oh</em> appears twice.",
            ],
            "lines": [
                "feeling, manners    affection, affectionate, compassion,",
                "                    envy, fond, gallantry, saucy,",
                "                    ungracious, commendation, sensation",
                "house and church    parsonage, sermon, sermons,",
                "                    housekeeper, patron",
                "verbs not listed    provoke, provoked, interrupt,",
                "                    interruption, humbled, roused,",
                "                    subsisted, distressed, quarrel,",
                "                    repine, ramble",
                "British spelling    honour, humoured",
                "a cut not made      afterwards, conditionally,",
                "                    separation, twelvemonth",
                "formal words        departure, exertion, affirmative,",
                "                    steadfastly, palatable, solitary",
                "the rest            oh (twice), de",
            ],
            "after": [
                "Ten, five, eleven, two, four, six and three make 41, the "
                "number the lab prints. The first kind is a matter of the "
                "year: words of manners and feeling in a novel from 1813. "
                "The second is a matter of the setting: a country house and "
                "a church. The third is the one to read with care. The "
                "table lists forms, not headwords, so one missing verb can "
                "fill two rows: <em>provoke</em> and <em>provoked</em>, and "
                "the same for <em>sermon</em> and for <em>interrupt</em>. "
                "The rules would reach the second row if the first were on "
                "the list; it is not, so both rows stand. Learn the eleven "
                "as nine words. Two words are only a British spelling of a "
                "listed word (<em>honor</em>, <em>humor</em>). Four are made "
                "from listed words by a cut the lab does not make: "
                "<em>after</em> with an ending, <em>condition</em> with two, "
                "<em>separate</em> with one, and <em>twelve</em> and "
                "<em>month</em> joined. Six are formal words "
                "whose roots are not listed either. <em>Oh</em> is a word "
                "said in surprise, and <em>de</em> is the small word in the "
                "middle of one name, with no capital to mark it.",
                "Now read the other two tables the same way. The play has "
                "91 words not covered in 1,972 words, and the modern "
                "documents have 106 in 1,685. A reader of the first is "
                "short of words about love and manners; a reader of the "
                "second is short of the words of law and population, "
                "<em>mortality</em> and <em>discrimination</em> among them.",
            ],
        },
        "note": (
            "The 98% is a reader's figure for an easy read of a novel, "
            "quoted from Nation (2006). The list's own authors, Browne, "
            "Culligan and Phillips, say it covers about 92% of general "
            "English text; that is a claim about a large mixed collection, "
            "quoted here and not counted on this page. The passage, at "
            "91.0% by headword and 94.3% with names, sits on either side of "
            "it. One chapter from one 1813 novel is a sample, not a "
            "measurement of English."
        ),
        "mistakes": (
            (
                "Thinking 2,800 words is enough to read a page",
                "On these pages the 2,800 words cover between 85.9% and "
                "91.0% of what is printed, and between 92.7% and 94.6% once "
                "names are set apart. Both are below 98%. At 94.3% about one "
                "word in 18 is unknown, where a reader at 98% meets one in "
                "50. The same list was counted once over the whole novel, a "
                "count no page can carry, and the quoted result, from a count "
                "whose rules differ a little from the lab's, is 80.7%, "
                "86.1% and 88.4% for the three steps and 93.0% with names. "
                "The list is a start, not the end.",
            ),
            (
                "Reading a share as a count of different words",
                "The passage has 361 different words, and 91.0% is not "
                "91.0% of those. It is the share of all 936 words that are "
                "on the list, with each repeat counted. A word that appears "
                "26 times counts 26 times. That is why learning the commonest "
                "words moves the share so much.",
            ),
            (
                "Taking the share for one text as the share for all of them",
                "The same 2,800 words cover 91.0% of the passage, 85.9% of "
                "the play and 87.3% of the modern documents. A text with "
                "its own subject and its own words has its own share. The "
                "figure for a page you have to read is the one you need, and "
                "the lab will give it to you.",
            ),
        ),
        "quiz_title": "Check yourself",
        "quiz": (
            {
                "q": "On the passage, the first 1,000 words cover 85.0% and "
                     "all 2,800 cover 91.0%. How many points do the rest of "
                     "the words add?",
                "a": ["85.0 points", "91.0 points", "6.0 points",
                      "1,800 points"],
                "c": 2,
                "why": (
                    "91.0 minus 85.0 is 6.0. Those words add less than "
                    "the first 1,000, because the list puts the commonest "
                    "words first."
                ),
            },
            {
                "q": "A text has 500 words, and the reader does not know 25 "
                     "of them. Does the reader reach the 98% that Nation "
                     "gives?",
                "a": [
                    "No: the reader knows 95%, which is below 98%",
                    "Yes: 25 is a small number",
                    "No: the reader knows 5%",
                    "Yes: 95% rounds up to 98%",
                ],
                "c": 0,
                "why": (
                    "25 of 500 is 5%, so the reader knows 95%. That is below "
                    "98%, and 95% does not round to 98%. At 98% the reader "
                    "would not know 10 words."
                ),
            },
            {
                "q": "Why does the share go up when names are counted?",
                "a": [
                    "Names are counted twice",
                    "Names are in the first 1,000 words",
                    "The lab guesses at them",
                    "A name can be read without being learned from a list, "
                    "so the lab does not count it as unknown",
                ],
                "c": 3,
                "why": (
                    "The lab sets a name apart, and the share with names is "
                    "the one to hold against 98%. A name is not a word you "
                    "look up."
                ),
            },
            {
                "q": "What does the lab do with a pasted text of forty words?",
                "a": [
                    "It shows every share as 100%",
                    "It shows a dash for every tile and asks for at least "
                    "fifty words",
                    "It reads the first forty words and shows the shares",
                    "It shows nothing at all",
                ],
                "c": 1,
                "why": (
                    "Below fifty words one word moves the share too far to "
                    "mean anything, so the lab says so and counts nothing."
                ),
            },
        ),
        "body": [
            ("p",
             "How much of a page do you know? Most people answer with a "
             "feeling. This lesson answers with a count. The lab takes a "
             "printed text and asks one question of every word: is it on "
             "the list? The list is the 2,800 <dfn>headwords</dfn> of the "
             "New General Service List. A <dfn>headword</dfn> is the word "
             "the list files the others under: <em>walk</em> for "
             "<em>walks</em>, <em>walked</em> and <em>walking</em>. The "
             "answer is a share, and the share is the <dfn>coverage</dfn> of "
             "the list on that text."),
            ("h3", "Three steps of the list"),
            ("p",
             "The list comes in three bands. The first holds the commonest "
             "1,000 headwords and, beside them, the numbers, the days and "
             "the months, 1,050 in all; the second holds the next 1,000, "
             "and the third the last 809. That is 2,859 headwords, which "
             "this Subject calls 2,800 everywhere. On the passage, 936 "
             "words from the end of a chapter of <em>Pride and "
             "Prejudice</em>, the first 1,000 cover 85.0%, the "
             "first 2,000 cover 89.2%, and all 2,800 cover 91.0%. On the "
             "part of the play printed here, 1,972 words, the same steps give "
             "79.5%, 83.9% and 85.9%. On the two modern documents, 1,685 "
             "words in all, they give 76.0%, 84.7% and 87.3%."),
            ("h3", "How the lab knows a form"),
            ("p",
             "The list holds headwords, and a page holds forms. The lab "
             "closes the gap with the rules of the earlier courses, run "
             "backwards. It takes <em>-s</em>, <em>-ed</em> and "
             "<em>-ing</em> off a verb, with the spelling changes put back; "
             "it takes a plural off a noun, the irregular ones too; it "
             "takes <em>-er</em>, <em>-est</em> and <em>-ly</em> off a "
             "word; it turns <em>n't</em> into <em>not</em>; it files "
             "<em>him</em> and <em>his</em> under <em>he</em>, as the list "
             "does; and it knows "
             "the irregular verbs. If the word that comes out is on the "
             "list, the form is covered. The menu calls the passage "
             "936 words, the count this lab reads, with <em>don't</em> "
             "and <em>aunt's</em> one word each."),
            ("p",
             "Does this work? It was checked away from this page, against "
             "the full list of 10,296 forms the list records. "
             "The rules take 9,925 of them back to a headword, and 9,920 of "
             "those to their own headword. The 371 they miss are of six "
             "kinds: 152 British spellings (<em>colour</em>, "
             "<em>centre</em>, words in <em>-ise</em>); 74 spoken forms "
             "and words cut short (<em>gonna</em>, <em>comin</em>); 64 "
             "number words (<em>fourth</em>, <em>twentieth</em>); 17 old "
             "or irregular forms (<em>cometh</em>, <em>bade</em>, "
             "<em>borne</em>, <em>farther</em>); 11 plurals from Latin and "
             "Greek (<em>crises</em>, <em>phenomena</em>); and 53 wrong "
             "spellings and the rest (<em>arguement</em>, <em>e-mail</em>). "
             "The rules also reach words the list does not record, so the "
             "lab gives a little more cover than looking each word up in "
             "the list of forms would: 91.0% against 90.8% on the passage "
             "and 87.3% against 87.1% on the modern documents. On the play "
             "the gap is wider, 85.9% against 83.6%, and most of it is "
             "<em>don't</em> and the other short forms with an apostrophe: "
             "the forms list does not record them, and the rules take them "
             "apart. One extra hit is wrong: <em>Worthing</em>, a family "
             "name, is read as a form of <em>worth</em> six times."),
            ("h3", "What counts as a name"),
            ("p",
             "The lab asks about the list first, so a listed word that "
             "happens to carry a capital is covered, not a name. A word "
             "the list lacks is a name if its capital letter does not "
             "start a sentence. So is a word in capitals all through, "
             "which is how "
             "the play prints the name of each speaker, and a word that "
             "stands with a capital in the middle of a sentence somewhere "
             "else in the text, even where it opens a sentence. "
             "<em>Mr</em> and <em>Mrs</em> fall in this set too. The "
             "capital is the whole test, and the lab cannot tell a name "
             "from a word that happens to have one. Read the passage's 31 "
             "names and you find <em>Lord</em>, from <em>Oh, Lord!</em>. "
             "In the play, <em>Ahem</em>, "
             "a sound written as a word, is a name three times."),
            ("h3", "What is left"),
            ("p",
             "Now compare the share with names with the 98% a reader needs. "
             "For the passage the gap is 5.7 points at 94.3%. The play is "
             "at 94.6% and the modern documents at 92.7%. All three fall "
             "short, and the table says which words make the difference. "
             "The words are not the same in each. Read the three tables: "
             "the passage lacks words of manner, such as "
             "<em>affection</em> and <em>gallantry</em>; the play lacks "
             "words of feeling, such as <em>darling</em> and "
             "<em>passionately</em>, and its biggest single miss is the "
             "word of surprise it says fourteen times; and the modern "
             "documents lack the words of two trades, law and population "
             "counting."),
            ("h3", "A text of your own"),
            ("p",
             "Choose &ldquo;a text of your own&rdquo; and paste a page. Below "
             "fifty words the lab says so and counts nothing. Above it, you "
             "get the same tiles and the same table. The words under "
             "<em>not covered</em> are the ones to learn first for that "
             "page, and the ones that appear most often come first."),
        ],
    },
    {
        "slug": "ten-words-are-a-quarter-of-the-page",
        "module": "The commonest words",
        "title": "Ten Words Are a Quarter of the Page",
        "one_line": "Rank the words of a page by how often they appear, and the top ten turn out to be the small words that hold a sentence together.",
        "standard": (
            "Finish when you can rank a page's words by count and say what the top ten, fifty and hundred cover.",
            "You should be able to read a ranked list off the lab, work out "
            "the share the first ten, fifty and hundred words cover, name "
            "the kind of word that fills the top, and say why the top of "
            "one text is not the top of another.",
        ),
        "summary": (
            "Rank the 361 different words of the passage by how often they "
            "appear, and the first ten cover 25.6% of the page. The first "
            "fifty cover 54.5%, and the first hundred 67.7%. None of the "
            "ten names a thing or an act: they are <em>I</em>, "
            "<em>she</em>, <em>you</em>, <em>and</em>, <em>the</em>, "
            "<em>to</em>, <em>of</em>, <em>was</em>, <em>it</em> and "
            "<em>that</em>. They hold the sentence together, and a "
            "page is built round them."
        ),
        "key_label": "Share of the page, by rank",
        "key": [
            "the passage    ten 25.6%   fifty 54.5%",
            "               hundred 67.7%",
            "the play       ten 24.9%   fifty 50.5%",
            "               hundred 63.3%",
            "modern papers  ten 24.7%   fifty 47.3%",
            "               hundred 60.6%",
        ],
        "concepts_intro": "Three ideas about a ranked list.",
        "concepts": (
            (
                "A few words do a great deal of the work",
                "On the passage, ten words fill 240 of the 936 places, "
                "which is 25.6%. Fifty words fill 54.5%, and a hundred "
                "fill 67.7%. The other 261 different words share the last "
                "32.3%. A page is mostly the same small words, over and "
                "over, with the rest of the words as the thin part.",
            ),
            (
                "The top is made of grammar words",
                "The passage's ten are <em>I</em>, <em>she</em>, "
                "<em>you</em>, <em>and</em>, <em>the</em>, <em>to</em>, "
                "<em>of</em>, <em>was</em>, <em>it</em> and <em>that</em>. "
                "Four are pronouns; <em>and</em> and <em>that</em> join one "
                "part of a sentence to the next; <em>the</em>, <em>to</em> "
                "and <em>of</em> stand in front of a noun or a verb; and "
                "<em>was</em> is the verb <em>be</em>. They carry the "
                "grammar, and they say very little about what the page is "
                "about.",
            ),
            (
                "Each text has its own top",
                "The play has <em>I</em> first and <em>you</em> second, "
                "and then a name, <em>Cecily</em>. The modern "
                "documents, which include a report on an older population, "
                "have <em>age</em> itself in the ten. The shares are "
                "close, 25.6%, 24.9% and 24.7%, but the words are not "
                "the same, and the difference is the text's own subject.",
            ),
        ),
        "steps_title": "Reading a ranked list for a text in front of you",
        "steps_intro": "Four steps.",
        "steps": (
            (
                "Switch the list to the commonest words",
                "Choose &ldquo;the commonest words, ranked&rdquo; under the "
                "text. The table now shows rank, word, times, and the share "
                "of the page so far.",
            ),
            (
                "Read down the share so far",
                "The last number in the row for rank 10 is the share the "
                "top ten cover. Do the same at rank 50 and rank 100.",
            ),
            (
                "Name the kind of each word at the top",
                "Is it a word for a thing, an act or a quality? Or is it a "
                "small word that joins, stands for another word, goes in "
                "front of a noun, or is a form of <em>be</em>? Count each "
                "kind.",
            ),
            (
                "Compare two texts",
                "Switch the text and read the top ten again. Which words "
                "stayed, and which are the new text's own?",
            ),
        ),
        "lab": ("english", {
            "mode": "coverage",
            "text": "passage",
            "show": "top",
            "panel_title": "Rank the words of a page",
            "panel_intro": (
                "The table lists the hundred commonest words of the text you "
                "choose, with the number of times each appears and the "
                "share of the page so far. Words with the same count are "
                "put in the order of the alphabet. A name is a word too, so "
                "it is ranked with the rest."
            ),
        }),
        "read_title": "The ten commonest words of the passage",
        "read_intro": (
            "The list is the lab's first ten rows. Read it as a list of "
            "kinds, not as a list of words to learn."
        ),
        "worked": {
            "title": "The first ten rows, with the share so far",
            "intro": [
                "Each line is a row of the lab's table: the rank, the word, "
                "how many times it appears in the 936 words, and the share "
                "of the page that the words down to it fill.",
            ],
            "lines": [
                "1   I      30    3.2%",
                "2   she    29    6.3%",
                "3   you    27    9.2%",
                "4   and    26   12.0%",
                "5   the    26   14.7%",
                "6   to     25   17.4%",
                "7   of     21   19.7%",
                "8   was    20   21.8%",
                "9   it     19   23.6%",
                "10  that   17   25.6%",
            ],
            "after": [
                "Add the ten counts: 30, 29, 27, 26, 26, 25, 21, 20, 19 and "
                "17 make 240, and 240 of 936 is 25.6%. Not one of the ten "
                "names a thing or an act. Three are pronouns for people "
                "(<em>I</em>, <em>she</em>, <em>you</em>) and one for a "
                "thing (<em>it</em>); the rest join, stand in front of a "
                "noun or a verb, or are the verb <em>be</em>. <em>And</em> "
                "and <em>the</em> have the same count, 26, and the lab puts "
                "<em>and</em> first only because it comes first in the "
                "alphabet.",
                "The passage is a conversation, which is why <em>I</em> and "
                "<em>you</em> are so high. Switch to the play and the "
                "ten are <em>I</em> (89), <em>you</em> (68), "
                "<em>Cecily</em> (64), <em>the</em> (51), <em>to</em> "
                "(47), <em>of</em> (38), <em>Algernon</em> (37), "
                "<em>a</em> (34), <em>it</em> (33) and <em>is</em> (31). "
                "Two of them are names, and most of those counts are the "
                "name printed before each speech. On the modern documents "
                "the ten are <em>the</em> (117), <em>to</em>, "
                "<em>and</em>, <em>in</em>, <em>of</em>, <em>a</em>, "
                "<em>for</em>, <em>age</em> (21), <em>as</em> and "
                "<em>that</em>. Nine of them are grammar words; "
                "<em>age</em> is the subject of the report.",
            ],
        },
        "note": (
            "The lab ranks spellings. <em>Light</em> as a thing and "
            "<em>light</em> as a quality are one word to it, and so are "
            "<em>can</em> the verb and <em>can</em> the tin. The whole "
            "novel was counted once, which no page can carry, and the "
            "quoted result is 22.4% for the top ten, 48.1% for fifty and "
            "58.9% for a hundred, in 6,308 different words. It is a longer "
            "text with more kinds of word in it, so the shares are lower."
        ),
        "mistakes": (
            (
                "Thinking the commonest words are the ones to learn first "
                "because they carry the meaning",
                "They carry the grammar. The passage's ten commonest "
                "words fill a quarter of the page and say almost nothing "
                "about what it is about. A reader at this level has "
                "almost certainly met every one of them. The words that "
                "stand between you and an easy read are further down, and "
                "the lab's other list, the words not covered, is where "
                "they are printed. The course called Listening shows the "
                "same small words from the other side: they are the ones "
                "fast speech says weakly.",
            ),
            (
                "Reading the share as a count of words learned",
                "The first hundred words cover 67.7% of the passage, but "
                "they are 100 of its 361 different words. Every repeat of "
                "a word counts, so the first words you learn are worth far "
                "more than the last. The next hundred are worth less than "
                "the first hundred, and the last 261 share 32.3% between "
                "them.",
            ),
            (
                "Taking the top of one text for the top of every text",
                "The play puts two names in its ten and the modern "
                "documents put <em>age</em> in theirs. A ranked list is a "
                "list for one text. Its grammar part travels from text to "
                "text and its subject part does not.",
            ),
        ),
        "quiz_title": "Check yourself",
        "quiz": (
            {
                "q": "The ten commonest words of the passage fill 25.6% of "
                     "it. What kind of words are they?",
                "a": [
                    "Words for the people in the story",
                    "Words for the things and acts in the story",
                    "Words that describe the story",
                    "Small grammar words, such as <em>the</em>, "
                    "<em>to</em>, <em>of</em> and <em>was</em>, and "
                    "pronouns",
                ],
                "c": 3,
                "why": (
                    "All ten are pronouns, small words that join or stand "
                    "in front of a noun, or the verb <em>be</em>. None names "
                    "a thing or an act."
                ),
            },
            {
                "q": "On the passage, the commonest hundred words cover "
                     "67.7%. What does this say about the other 261 "
                     "different words?",
                "a": [
                    "They share the last 32.3% of the page",
                    "They cover nothing",
                    "They are all names",
                    "They cover another 67.7%",
                ],
                "c": 0,
                "why": (
                    "100 minus 67.7 is 32.3. The hundred words come first "
                    "because they appear most often, so the rest, though "
                    "more of them, share less."
                ),
            },
            {
                "q": "Why is <em>Cecily</em> one of the ten commonest words "
                     "of the play excerpt?",
                "a": [
                    "It is a word on the list",
                    "Most of its 64 appearances are the name printed "
                    "before each speech, and the lab counts a name as a "
                    "word",
                    "The lab counts it twice",
                    "It is a grammar word",
                ],
                "c": 1,
                "why": (
                    "A play prints the speaker's name before each speech, "
                    "and the lab ranks every word of the text, names "
                    "included. A report on age puts <em>age</em> in its "
                    "ten for the same kind of reason: the text is about it."
                ),
            },
            {
                "q": "Which words does a reader at this level most need to "
                     "learn to reach 98% on the passage?",
                "a": [
                    "The ten commonest words",
                    "The names",
                    "The words in the table of words not covered",
                    "The words of the first 1,000",
                ],
                "c": 2,
                "why": (
                    "The ten commonest are almost certainly known, and "
                    "names are read without being learned. The 41 words "
                    "not covered, with the 12 the family step reaches, are "
                    "what stands between 94.3% and the 98% a reader needs."
                ),
            },
        ),
        "body": [
            ("p",
             "The last lesson counted how much of a page a list covers. "
             "This one turns the question round. Ignore the list and count "
             "the page: which words appear most, and how much of the page "
             "do they fill? The answer does not depend on any list. It is "
             "a fact about the text."),
            ("h3", "The rank of a word"),
            ("p",
             "The lab counts every word of the text, ranks the different "
             "ones from the commonest down, and adds up the share as it "
             "goes. The passage has 936 words and 361 different ones. The "
             "commonest, <em>I</em>, appears 30 times and is 3.2% of the "
             "page. The commonest ten together are 25.6%."),
            ("h3", "Ten, fifty, a hundred"),
            ("p",
             "Three numbers sum up the shape of the list. On the passage, "
             "the ten commonest words cover 25.6%, the fifty commonest "
             "cover 54.5% and the hundred commonest cover 67.7%. On the "
             "play excerpt, with 605 different words, they cover 24.9%, "
             "50.5% and 63.3%. On the modern documents, with 603 different "
             "words, 24.7%, 47.3% and 60.6%. The shapes are close. A "
             "quarter of a page is ten words, and about two thirds is a "
             "hundred."),
            ("h3", "What kind of word"),
            ("p",
             "Read the first ten of the passage and sort them. There are "
             "three pronouns for people, <em>I</em>, <em>she</em> and "
             "<em>you</em>, and <em>it</em>, which stands for a thing. "
             "There is <em>and</em>, which joins, and <em>that</em>, which "
             "in this passage joins too: in fourteen of its seventeen "
             "places it ties a verb to what follows (<em>persuaded "
             "that</em>, <em>I find that</em>), and in three it points "
             "(<em>on that point</em>). There are <em>the</em>, <em>to</em> "
             "and <em>of</em>, which go in front of a noun or a verb. And "
             "there is <em>was</em>, the past of <em>be</em>. Do not call "
             "it a helping verb here: the course Helping Verbs found that "
             "<em>be</em> is mostly a main verb, and in this passage not one "
             "of the twenty <em>was</em> is followed by an <em>-ing</em> "
             "verb. It stands before a quality (<em>was proud</em>), a "
             "participle (<em>was roused</em>) or a thing (<em>there was a "
             "time</em>)."),
            ("p",
             "This is why a quarter of a page costs a reader almost "
             "nothing, and also why knowing the ten does not get you "
             "through the page. They are the frame. The words that say "
             "what the page is about are in the other three quarters."),
            ("h3", "Where the subject shows"),
            ("p",
             "Text by text, the grammar part of the list stays the same and "
             "the subject part changes. In the play, the speakers' names "
             "<em>Cecily</em> and <em>Algernon</em> are in the ten. In "
             "the modern documents, <em>age</em> is, because a report on "
             "an older population says it again and again. The lab shows "
             "this when you switch the text, and the switch is worth "
             "making before you read the quiz."),
            ("h3", "The rest of the page"),
            ("p",
             "After the hundred, the list falls steeply. The passage's "
             "361 different words, less the first hundred, share 32.3% of "
             "the page. Many of them appear once. These are the words that "
             "say what the passage is about, and the table of words not "
             "covered, in the lesson before, lists the ones you have to "
             "look up."),
        ],
    },
    {
        "slug": "word-or-word-family",
        "module": "Word and family",
        "title": "Word or Word Family",
        "one_line": "A word with its endings and a word with every word made from it are two different things to count, and the lab shows the difference.",
        "standard": (
            "Finish when you can say what a flemma counts and what a family counts, and how far apart the two figures are.",
            "You should be able to say what a flemma and a family each "
            "include, switch the lab to the words a family adds, read how "
            "many points the family step adds to the share, and say which "
            "of the lab's rows are real families and which are only "
            "spellings that look like them.",
        ),
        "summary": (
            "The list counts <dfn>flemmas</dfn>: a word with its endings. "
            "Nation's 98% counts <dfn>families</dfn>: a word with the words "
            "made from it. On the passage the lab's share with names is "
            "94.3%, and 95.6% when the family step is added. Those 1.3 "
            "points are 12 words, and reading them shows what a family "
            "step can do and what it cannot."
        ),
        "key_label": "Names, then families, on three texts",
        "key": [
            "the passage          94.3% to 95.6%",
            "the play excerpt     94.6% to 95.4%",
            "the modern papers    92.7% to 93.7%",
            "",
            "a flemma: walk, walks, walked, walking",
            "a family: delight, delightful",
        ],
        "concepts_intro": "Three ideas, and the second is where the figure comes from.",
        "concepts": (
            (
                "A flemma is a word with its endings",
                "<em>Walk</em>, <em>walks</em>, <em>walked</em> and "
                "<em>walking</em> are one flemma. So are <em>child</em> and "
                "<em>children</em>, and <em>good</em>, <em>better</em> and "
                "<em>best</em>. A flemma only adds the endings the first "
                "courses taught. The 2,800 words of the list are counted "
                "this way, and so is the lab's share up to the names.",
            ),
            (
                "A family is a flemma and the words made from it",
                "<em>Delight</em> with <em>delightful</em>, and <em>care</em> "
                "with <em>careless</em>, are two families, each of two "
                "flemmas. A family keeps the same root and adds a beginning "
                "such as <em>un-</em> or <em>re-</em>, which turns the "
                "meaning, or an ending such as <em>-ful</em>, "
                "<em>-less</em>, <em>-ness</em> or <em>-ly</em>, which "
                "changes the kind of word. Nation's "
                "98% is counted by family, which means a reader who knows "
                "the root is counted as knowing the longer word.",
            ),
            (
                "The step the lab adds is a spelling test",
                "The family step takes one beginning or one ending off a "
                "word the list does not cover. If what is left is on the "
                "list, the word is counted as a family member. It tests "
                "spellings, not meanings, so it also passes some words "
                "whose meaning has moved away from their root.",
            ),
        ),
        "steps_title": "Counting a word that is not on the list",
        "steps_intro": "Four questions, asked of each word the list lacks.",
        "steps": (
            (
                "Is it a form of a word on the list?",
                "If the rules of the earlier courses take it back to a "
                "word on the list, it is a flemma of that word and the list "
                "covers it. Stop.",
            ),
            (
                "Is it a name?",
                "A capital letter in the middle of a sentence, or "
                "capitals all through, and the lab sets it apart. Stop.",
            ),
            (
                "Take off one beginning or one ending",
                "<em>Unwelcome</em> loses <em>un-</em> and leaves "
                "<em>welcome</em>. <em>Careless</em> loses <em>-less</em> "
                "and leaves <em>care</em>. If what is left is on the "
                "list, the word joins that word's family.",
            ),
            (
                "Ask whether the meaning followed the spelling",
                "The lab cannot. You can. <em>Notable</em> loses "
                "<em>-able</em> and leaves <em>not</em>, which is on the "
                "list, but the word does not mean <em>not able</em>: it is "
                "made from <em>note</em>, and the lab stopped at the first "
                "cut that found a listed word.",
            ),
        ),
        "lab": ("english", {
            "mode": "coverage",
            "text": "passage",
            "show": "family",
            "panel_title": "What a family adds",
            "panel_intro": (
                "The table lists the words that are not on the list as "
                "they stand, but are on the list when one beginning or "
                "one ending is taken off. Each row shows the word, what "
                "it was made from, and how many times it appears. The two "
                "tiles to compare are &ldquo;and names&rdquo; and "
                "&ldquo;and families&rdquo;. Switch the text to see "
                "the others."
            ),
        }),
        "read_title": "The twelve family words in the passage",
        "read_intro": (
            "With the passage chosen, the table holds twelve rows. Read each "
            "one and ask whether it is the same word family as its root."
        ),
        "worked": {
            "title": "Six rows of the table, and a note on each",
            "intro": [
                "These are rows from the passage, the play and the modern "
                "documents, with a note on each from a reader, not from "
                "the lab.",
            ],
            "lines": [
                "delightful (delight + -ful)      one family",
                "unwilling (un- + willing)        one family",
                "recollect (re- + collect)        one family",
                "notable (note + -able)           one family",
                "resides (re- + sides)            a spelling only",
                "endure (end + -ure)              a spelling only",
            ],
            "after": [
                "The first four are what a family means. A reader who "
                "knows <em>delight</em>, <em>willing</em>, <em>collect</em> "
                "and <em>note</em> has most of what the longer word says. "
                "<em>Notable</em> also contains <em>not</em>, which is on "
                "the list, but the lab tries the stem with an <em>e</em> "
                "first, so it finds <em>note</em>. The last two are wrong. "
                "To reside has nothing to do with sides, and to endure "
                "nothing to do with an end. The lab passes both, because it "
                "reads spellings, and its count includes them. The passage's twelve rows "
                "also include <em>carriage</em> from <em>carry</em>, "
                "which is a judgement of the same kind.",
                "Two things follow. The lab's family step cannot take a wrong "
                "row away, so you have to read the rows. And it uses a "
                "short list of beginnings and endings, so a full family "
                "count, with every beginning and ending a full list "
                "gives, would add more.",
            ],
        },
        "note": (
            "The whole novel was counted once, which no page can carry, and "
            "the quoted result is 93.0% with names and 94.6% with families, "
            "a gain of 1.6 points. The design notes behind this Subject put "
            "the cost of counting flemmas instead of families on general "
            "text at three to six points. That is an estimate with no "
            "count behind it that you can see, and nothing on this page "
            "measures it. "
            "The lab's gain is smaller, and one reason is that its family "
            "step uses only a short list of beginnings and endings."
        ),
        "mistakes": (
            (
                "Holding the lab's share against 98% without asking what "
                "each one counts",
                "Nation's 98% is counted by family. The list, and so the "
                "lab, counts flemmas. The two are not the same thing, and "
                "the difference is real: on the passage the lab's share "
                "goes from 94.3% to 95.6% when the family step is added, "
                "on the play from 94.6% to 95.4%, and on the modern "
                "documents from 92.7% to 93.7%. To compare like with like, "
                "use the figure with families. It is still below 98%, "
                "on every text.",
            ),
            (
                "Thinking a family is any word that contains another",
                "<em>Resides</em> contains <em>re-</em> and <em>sides</em>, "
                "and <em>endure</em> contains <em>end</em>. "
                "Neither is their family. The lab's step cuts a "
                "beginning or an ending and looks at what is left, and it "
                "passes any cut that leaves a listed word. You must read the "
                "rows and decide.",
            ),
            (
                "Thinking the family step finds the words you need to learn",
                "It finds the words you may not need to. A reader who "
                "knows <em>delight</em> can probably read "
                "<em>delightful</em>. The words you need to learn are the "
                "ones still in the table of words not covered after the "
                "family step, and on the passage there are 41 of them.",
            ),
        ),
        "quiz_title": "Check yourself",
        "quiz": (
            {
                "q": "Which pair is one flemma?",
                "a": [
                    "<em>delight</em> and <em>delightful</em>",
                    "<em>walk</em> and <em>walked</em>",
                    "<em>kind</em> and <em>unkind</em>",
                    "<em>care</em> and <em>careless</em>",
                ],
                "c": 1,
                "why": (
                    "A flemma adds only endings of the kind the first "
                    "courses taught. <em>Walked</em> is <em>walk</em> and "
                    "<em>-ed</em>. The other three pairs differ by a "
                    "beginning or an ending that makes a new kind of word, "
                    "so they are one family but two flemmas."
                ),
            },
            {
                "q": "On the passage, the share goes from 94.3% to 95.6% "
                     "when the family step is added. What are the 1.3 "
                     "points?",
                "a": [
                    "Words the list does not cover and the step makes "
                    "known, such as <em>delightful</em>",
                    "Names the lab found",
                    "Words the lab guessed",
                    "Repeats of the words in the first 1,000",
                ],
                "c": 0,
                "why": (
                    "The step takes one beginning or one ending off a word "
                    "the list lacks, and counts the word if what is left is "
                    "a listed word. The twelve rows of the table are those "
                    "words."
                ),
            },
            {
                "q": "The family step passes <em>resides</em> as "
                     "<em>re-</em> and <em>sides</em>. What does that "
                     "show?",
                "a": [
                    "The step is always right",
                    "<em>Resides</em> is a name",
                    "The step reads spellings, so a row can be wrong in "
                    "meaning",
                    "The list is too short",
                ],
                "c": 2,
                "why": (
                    "The step asks only whether what is left is a "
                    "listed word. It does not ask whether the meaning is "
                    "kept: <em>resides</em> has nothing to do with "
                    "<em>sides</em>, and the word is made from "
                    "<em>reside</em>."
                ),
            },
            {
                "q": "Nation counts families and the list counts flemmas. "
                     "Which figure on the passage is the closer match for "
                     "Nation's 98%?",
                "a": [
                    "91.0%, the first 2,800 words",
                    "94.3%, with names",
                    "85.0%, the first 1,000 words",
                    "95.6%, with names and families",
                ],
                "c": 3,
                "why": (
                    "It is the only one of the four that counts the family "
                    "of a word as well as its endings. It is still below "
                    "98%, which is the point."
                ),
            },
        ),
        "body": [
            ("p",
             "The last two lessons counted words. This one asks what a word "
             "is. When someone says a reader needs to know 98% of the words "
             "of a page, they have counted in a certain way, and the lab "
             "counts in another. The two ways have names, and the "
             "difference is about one point."),
            ("h3", "A word, a flemma, a family"),
            ("p",
             "A <dfn>flemma</dfn> is a word and the forms made from it by "
             "the endings you met in the first courses: <em>-s</em>, "
             "<em>-ed</em>, <em>-ing</em>, <em>-er</em>, <em>-est</em>, "
             "and the forms that do not follow the rules. <em>Walk</em> and "
             "<em>walked</em> are one flemma. A <dfn>family</dfn> is a "
             "flemma and the words made from it with a beginning or a "
             "different kind of ending: <em>happy</em>, <em>unhappy</em> and "
             "<em>happiness</em> are one family. The word list counts "
             "flemmas. Nation counts families."),
            ("h3", "Three steps of the lab's count"),
            ("p",
             "The lab reads a page in this order. First it asks if a word "
             "is on the list, by the rules, and counts it as covered if "
             "so. Second, if not, it asks if the word is a name. Third, "
             "if not, it takes off one beginning or one ending and asks "
             "again. A word that passes the third step is counted as a "
             "family word. A word that passes none is not covered."),
            ("p",
             "So the three numbers are in order, each including the one "
             "before. On the passage they read 91.0% for the list, 94.3% "
             "with names, and 95.6% with families. The second step adds "
             "3.3 points and the third adds 1.3. The passage has 12 family "
             "words, each appearing once, and 1.3 points is 12 in 936."),
            ("h3", "The words a family adds"),
            ("p",
             "Set the second menu to the words a family adds. On the "
             "passage the rows include <em>delightful</em>, "
             "<em>unwelcome</em>, <em>unwilling</em>, <em>recollect</em> "
             "and <em>overtaken</em>. On the modern documents the first "
             "row is <em>disability</em>, made from <em>dis-</em> and "
             "<em>ability</em>, and it appears ten times. The step adds "
             "1.0 point to that text, from 92.7% to 93.7%. On the play "
             "it adds 0.8, from 94.6% to 95.4%."),
            ("h3", "What the step cannot see"),
            ("p",
             "The step cuts a spelling and looks at what is left. "
             "<em>Notable</em> could be cut to <em>not</em> and "
             "<em>-able</em>, since both are on the list; the lab tries "
             "<em>note</em> first, so its cut is the right one. In the "
             "play, <em>resides</em> becomes <em>re-</em> and "
             "<em>sides</em>, and <em>endure</em> becomes <em>end</em> and "
             "<em>-ure</em>: there the row is wrong too, and the share "
             "counts both. The cut is right for <em>delightful</em>, and "
             "the lab cannot tell which is which."),
            ("h3", "Why the gap is small here"),
            ("p",
             "The design notes behind this Subject put the gap between "
             "counting flemmas and counting families on general text at "
             "three to six points; that is an estimate, not a count you "
             "can see. The gap the lab shows on these three texts is "
             "between 0.8 and 1.3 points. The lab uses a short list of "
             "beginnings and endings, and a full family count uses many "
             "more. So a full count would add more than the lab does, "
             "though some of the lab's rows are only spellings."),
            ("p",
             "Either way you count, the answer for these texts is the "
             "same: below 98%. The words that stand between you and an "
             "easy read are the ones in the table of words not covered, "
             "and the family step has already taken out the ones it can."),
        ],
    },
]
