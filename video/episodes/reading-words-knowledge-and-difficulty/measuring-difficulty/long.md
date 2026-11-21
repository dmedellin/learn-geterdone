---
format: long
lesson: reading-words-knowledge-and-difficulty/measuring-difficulty
title: Readability formulas: what three counts can and can't see
thumb: Three counts, one score
---

@chapter The question
@title text="Measuring Difficulty" sub="Reading Faster · Words, Knowledge and Difficulty" art=thumb
How do you put a number on how hard a text is? A readability formula does it with just three counts: words, sentences and syllables. Let's see what that number measures, and what it can't see.

@art three-counts
Count the words, the sentences, and the syllables. From those you get two averages: words per sentence, and syllables per word. Those two averages are the whole of what the formulas know about a text.

@chapter Two formulas
@math heading="Flesch Reading Ease (1948)" items="ease = 206.835 − 1.015 × W/S − 84.6 × Y/W@Reading Ease is"
Rudolf Flesch's nineteen forty eight Reading Ease is two oh six point eight three five, less one point oh one five times the words per sentence, less eighty four point six times the syllables per word.

@math heading="Flesch–Kincaid grade (1975)" items="grade = 0.39 × W/S + 11.8 × Y/W − 15.59@The grade is"
The Flesch Kincaid grade was derived by Kincaid and colleagues in nineteen seventy five, for Navy enlisted personnel. The grade is point three nine times words per sentence, plus eleven point eight times syllables per word, less fifteen point five nine.

@art two-scales
The two scales run opposite ways. Reading Ease falls as difficulty rises: the higher the score, the easier the text. The grade rises, and it's read as a school grade. The same two averages drive both, so they almost always agree on which text is harder.

@chapter Counting rules
@list heading="The kit's counting rule" items="Word: a token with a letter or digit@A word is|Sentence: ends at . ? or ! and a space@A sentence ends|Syllables: vowel groups, less a silent e@Syllables are counted"
The counts need rules. A word is a whitespace separated token with a letter or a digit in it. A sentence ends at a full stop, a question mark or an exclamation mark, followed by a space. Syllables are counted by vowel groups, less one for a silent e at the end, and at least one a word.

@words text="Every syllable figure is an approximation"
That rule miscounts some words, so every syllable figure is an approximation, and another program's counts will differ a little.

@chapter By hand
@math heading="100 words · 5 sentences · 140 syllables" items="W/S = 100 / 5 = 20@twenty words a sentence;;Y/W = 140 / 100 = 1.4@one point four syllables"
Work one by hand. A hundred words, five sentences, a hundred and forty syllables. That's twenty words a sentence, and one point four syllables a word.

@math heading="100 words · 5 sentences · 140 syllables" items="ease = 206.835 − 20.3 − 118.44 = 68.095@less twenty point three;;grade = 7.8 + 16.52 − 15.59 = 8.73@The grade is"
The ease is two oh six point eight three five, less twenty point three, less one eighteen point four four: sixty eight point oh nine five. The grade is seven point eight plus sixteen point five two, less fifteen point five nine: eight point seven three, in this Subject's standard band.

@chapter The passages
@math heading="Three passages" items="The Octopus: ease ≈ 79.8 · grade ≈ 6.8@The Octopus;;The Church Clock at Wexley: ease ≈ 70.2 · grade ≈ 9.3@The Church Clock;;Continents: ease ≈ 14.3 · grade ≈ 17.3@the continents passage"
Now the passages you've read. The Octopus has an ease of about seventy nine point eight, and a grade of about six point eight. The Church Clock at Wexley, the first passage you timed, is about seventy point two and grade nine point three. And the continents passage is about fourteen point three, and grade seventeen point three.

@art word-length-weight
Where does the gap come from? The hard passage's sentences are only about a third longer. But its words carry more than half as many syllables again, and syllables a word are multiplied by eighty four point six. Most of the gap between seventy nine point eight and fourteen point three is word length.

@chapter What it can't see
@art bands
That's the honest use of a formula: to sort many texts quickly. The passages in this Subject were sorted into bands by exactly these counts. Easy at grades five to seven, standard at eight to eleven, hard at thirteen and above.

@art blind-formula
The formulas can't see anything else. They don't know whether a word is common or rare, so a short technical word counts as easy. They don't know whether you know the subject.

@art linked-sentences
And they can't tell a passage of separate facts from one where every sentence depends on the last. A sentence of short words about an idea you've never met can score as easy as a nursery rhyme.

@chapter Where people slip
@list heading="Common slips" items="Taking the score for how hard it is to understand@The first|Reading the two scales the same way round@The second|Trusting the second decimal@And the third"
The first slip is taking a readability score for how hard a text is to understand. The second is reading the two scales the same way round. And the third is trusting the second decimal. A grade of nine point three against nine point four is no difference at all.

@chapter Try it
@words text="200 words · 10 sentences · 300 syllables" sub="Flesch–Kincaid grade?"
Your turn. A text has two hundred words, ten sentences and three hundred syllables. What's its grade? Twenty words a sentence, one point five syllables a word. Point three nine times twenty, plus eleven point eight times one point five, less fifteen point five nine: nine point nine one.

@end text="Count a text of your own"
You can paste a text of your own into the counter and compare its grade with the passages, on Learn. That's learn dot get er done dot I O.
