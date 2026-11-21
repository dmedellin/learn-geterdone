---
format: long
lesson: strings-and-pattern-matching/one-pass-for-every-word
title: Aho-Corasick: one pass over the text for every word in the dictionary
thumb: Suffixes report together
---

@chapter The question
@title text="One Pass for Every Word" sub="Strings and Pattern Matching" art=thumb
Suppose you're searching a text for a whole dictionary of words, not just one. You could run a matcher once per word. Or you could build one structure, and find every occurrence of every word in a single scan.

@art trie-shape
Start with a trie. It's a rooted tree whose edges carry characters. Each path from the root spells a prefix of some word, and every distinct prefix appears as exactly one node. Nodes where a word ends are marked.

@chapter Ten nodes
@math heading="he, she, his, hers" items="h · he · her · hers · hi · his@h, h e;;s · sh · she@s, s h;;9 prefixes + root = 10 nodes@ten nodes"
Take the words he, she, his and hers. The distinct prefixes are h, h e, h e r, h e r s, h i, h i s, then s, s h and s h e. That's nine, plus the root, so ten nodes.

@art shared-prefix
The four words have twelve characters between them. The trie stores nine edges, because he sits inside hers, and h leads to both he and his. Shared prefixes are stored once.

@words text="array per node: 10 × 5 = 50 cells" sub="map per node: one entry per edge"
Space comes as two numbers. Give each node an array with a slot for every character, and five characters means ten times five, fifty cells. Give each node a map instead, and it costs one entry per edge that exists. Which is better depends on how dense the alphabet is.

@chapter Failure links
@art failure-links
Now add a failure link to every node. It points to the node spelling the longest proper suffix of that node's string that's also in the trie, or to the root if there's none. The links are set breadth first, so every shorter node's link is ready before it's needed.

@words text="outputs(v) = v's own word + outputs(fail(v))"
Each node's outputs are its own word, if it ends one, plus the outputs of the node its failure link points to. That's the output chain.

@chapter One scan
@art scan-walk
Feed the text in one character at a time. Follow the child edge if it exists. If not, follow failure links until a child exists, or you reach the root. After each character, the current node spells the longest suffix of the text so far that's in the trie.

@words text="words ending here = the failure chain's word ends"
The proof is induction, just like the single pattern machine. And the key step is this. A word ends at the current position exactly when it's a suffix of what's been read, so it's on the failure chain from the current node.

@list heading="ushers hers his she he" items="he at 2, 7, 17, 20@he at|she at 1, 16@she at|his at 12@his at|hers at 2, 7@hers at"
On ushers hers his she he, twenty two characters, one pass reports nine occurrences. He at two, seven, seventeen and twenty. She at one and sixteen. His at twelve. And hers at two and seven.

@math heading="Comparisons" items="one pass: 31@one pass;;four KMP passes: 23 + 25 + 26 + 24 = 98@four separate"
That one pass costs thirty one comparisons. Four separate KMP passes cost twenty three, twenty five, twenty six and twenty four, ninety eight in all. The saving isn't cleverness per character. It's one scan instead of four.

@chapter Suffixes, not prefixes
@art suffix-chain
At the end of u s h e, position three, the automaton reports both she and he, because he is a suffix of she, so it sits on she's failure chain. Position eighteen does the same. No other position reports two words.

@art nested-prefixes
Now take the dictionary a, a b, a b c, a b c d, where each word is a prefix of the next. Scan a b c d a b c a b. No position ever reports more than one word. None of b c d, c d or d is a word, so no failure chain from a b c d reaches another word end.

@chapter Where people slip
@list heading="Common slips" items="Expecting nested prefixes to report together@The first|Setting failure links in any order@The second|Quoting one space figure for a trie@The third"
The first slip is expecting nested prefixes to report together. The chain follows suffixes. The second is setting failure links in any order. Breadth first is part of the construction, or a word loses occurrences. The third is quoting one space figure for a trie.

@chapter Try it
@words text="dictionary: he, she · text: ashes"
Your turn. Build the trie for he and she, add the failure links, and scan ashes one character at a time. At which position do two words get reported, and why?

@end text="Scan for every word at once"
You can build a dictionary, see its failure links, and scan any text, on Learn. That's learn dot get er done dot I O.
