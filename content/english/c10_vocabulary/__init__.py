# -*- coding: utf-8 -*-
"""Vocabulary and Reading: how much of a page the 2,800 words cover.

Every figure in this course is read off a lab tile with labcheck.js --observe,
except the ones marked quoted. The passage is the one the Word Order course
prints (the end of Chapter 52 of Pride and Prejudice and the first lines of
Chapter 53, Gutenberg edition, with the chapter heading and the illustration
captions cut out by scripts/wordlists/en_passage.py); the lab reads 936 words,
keeping don't and aunt's as one word each. Counted on the page (coverage lab):
  passage (936 words, 361 different)   first 1,000 words 85.0%, first 2,000 89.2%,
        all 2,800 91.0%, and names 94.3%, and families 95.6%; 41 words not
        covered; commonest ten 25.6%, fifty 54.5%, hundred 67.7%
  play excerpt (1972 words, 605 different)   79.5 / 83.9 / 85.9 / 94.6 / 95.4%;
        91 not covered; 24.9 / 50.5 / 63.3%
  modern documents (1685 words, 603 different)   76.0 / 84.7 / 87.3 / 92.7 / 93.7%;
        106 not covered; 24.7 / 47.3 / 60.6%
Counted offline against the full list of recorded forms (not on the page;
reproduced 2026-10-10 by running the shipped cvBand over ngsl.tsv in node):
  the rules reach 9,925 of the 10,296 recorded forms, 9,920 of them to their
  own headword (the five wrong: emphasised and its forms to emphasis, won to
  win); the 371 missed are 152 British spellings, 74 spoken and cut-short
  forms, 64 number words (fourth, twentieth), 17 old or irregular forms
  (cometh, bade, borne, gotten, farther), 11 plurals from Latin and Greek
  (crises, phenomena) and 53 misspellings and oddities (arguement, e-mail);
  coverage of the whole list, forms list against rules:
  passage 90.8 against 91.0, play 83.6 against 85.9, modern 87.1 against 87.3.
  The play's gap is the contractions (don't eleven times) the forms list does
  not record, nine -ly adverbs, and one false hit: Worthing, a surname the
  -ing rule reads as a form of worth (six times).
Quoted: Nation (2006), 98%; Browne, Culligan and Phillips, 92% of general text;
  the whole novel, counted once by the design scan: 80.7 / 86.1 / 88.4 / 93.0%,
  94.6% with families, commonest ten 22.4%, fifty 48.1%, hundred 58.9%, 6,308
  different words.

Spoken forms: content/spoken/english_c10_vocabulary.py.
"""

from .part_a import LESSONS as _A

COURSE = {
    "slug": "vocabulary-and-reading",
    "title": "Vocabulary and Reading",
    "level": "Intermediate",
    "blurb": (
        "How many words do you need to read a page? This course counts. It "
        "checks every word of a passage from a novel, part of a play and two "
        "modern documents "
        "against the 2,800 words of the list, prints the words that are left, "
        "and lets you paste a text of your own. Then it shows which ten words "
        "make up a quarter of any page, and what changes when a word and its "
        "family are counted as one."
    ),
    "summary": (
        "The usual advice is to learn more words. This course says how many, "
        "and which, by measuring. The 2,800 words cover about nine words in "
        "ten of a passage from a novel, and fewer of a play or of two modern "
        "documents; names bring each of them to between 92 and 95 in 100; a "
        "reader needs 98. The gap is a list of words you can read off the "
        "page, and the lab prints it. The course ends with the choice that "
        "moves the number: whether to count a word, or a word with all its "
        "family."
    ),
    "assumes_short": (
        "Tense Tables, Irregular Verbs, Nouns and Articles, and Small Words "
        "and Comparisons."
    ),
    "assumes_long": (
        "Tense Tables, Irregular Verbs, Nouns and Articles, and Small Words "
        "and Comparisons. The lab in this course runs their rules backwards: "
        "it takes “walked” back to “walk”, “children” "
        "back to “child” and “happier” back to “happy” "
        "before it asks whether the word is on the list. You do not need to "
        "have learned the rules by heart, but you will meet each of them again."
    ),
    "how_to": [
        "Read the printed list of words the lab did not cover, not only the "
        "share. The share says how far you are from a reader's 98%; the list "
        "says which words would take you there.",
        "Change one thing at a time. The lab has a menu for the text and a menu "
        "for the list under the numbers. Change the text and watch the shares "
        "move; change the list and watch the table.",
        "Paste a page you have to read. A figure for a passage from 1813 is "
        "interesting, but the figure for the page on your desk is the one you "
        "can use.",
    ],
    "outcomes_intro": (
        "By the end you can say how much of a page you know, name the words "
        "that stand between you and an easy read, and say what a figure "
        "counts when someone gives it to you."
    ),
    "outcomes": [
        ("Work out the share of a page that a word list covers",
         "The first 1,000, the first 2,000 and all 2,800 words, counted on a "
         "passage from a novel, part of a play and two modern documents, each "
         "with the number of words read printed beside it."),
        ("Compare your figure with the one a reader needs",
         "98%, quoted from Nation, against the share the lab prints, and the "
         "number of words in a page that the gap stands for."),
        ("Say what a name costs and what it does not",
         "A name is read without being learned, so the lab sets it apart; the "
         "share with names is the fairer one to hold against 98%."),
        ("Read a frequency list the right way round",
         "The ten commonest words make up about a quarter of a page, and they "
         "are the small grammar words, not the words that carry the story."),
        ("Tell a word from a word family",
         "A word with its endings is one thing to count; a word with the words "
         "made from it is another. The lab shows how many points the second "
         "choice adds."),
        ("Test a text of your own",
         "Paste fifty words or more and read the share, the words not "
         "covered and the commonest words, all counted on your page."),
    ],
    "syllabus_intro": (
        "The share first, because the other two lessons change what it "
        "counts. Then the commonest words, which are a small part of the list "
        "and a large part of every page. Last, the choice between counting a "
        "word and counting its family."
    ),
    "not_covered": [
        "The meaning of a word. The lab reads spellings. It cannot tell which "
        "meaning of <em>light</em> or <em>run</em> a sentence uses, or that a "
        "phrase means something its words do not. A share of 94% says how "
        "many words you can find in the list. It does not say how many "
        "you can follow.",
        "Words past the list. The list stops at about 2,800 words. What to learn "
        "after it depends on what you read, and the lab prints the words your "
        "own text needs, which is a better guide than any other list.",
        "How to learn a word. Spacing, repeating and using a word are real "
        "skills, and no count on this page measures them. The course says "
        "which words, not how.",
        "Special texts. A page of law, medicine or machines will fall below "
        "98% whatever you do with these 2,800 words. The modern documents show "
        "it, and the lab lets you see it for yourself.",
    ],
    "key": [
        "98% known     a reader can follow",
        "91.0%  the passage, all 2,800 words",
        "94.3%  and names",
        "95.6%  and families",
        "25.6%  the commonest ten words",
        "67.7%  the commonest hundred",
    ],
    "footer_lead": (
        "<strong>Educational course material.</strong> Every share on this "
        "course is counted in your browser on the text named beside it. Word "
        "list: the New General Service List (Browne, Culligan and Phillips), "
        "CC BY-SA 4.0. The passage is the end of Chapter 52 and the first "
        "lines of Chapter 53 of <em>Pride and Prejudice</em> (1813; Project "
        "Gutenberg, public domain), the same passage the course Word Order "
        "prints, and the "
        "excerpt is from <em>The Importance of Being Earnest</em> (1895; "
        "Project Gutenberg, public domain). The two modern documents are "
        "<em>Stanley v. City of Sanford</em> (2025) and &ldquo;U.S. Population "
        "Aging as Nation Turns 250&rdquo; (2026), both U.S. government works. "
        "The irregular verbs and plurals the lab uses come from the lists of "
        "the earlier courses. Nation's and Browne's figures are quoted and "
        "never embedded."
    ),
    "lessons": list(_A),
}
