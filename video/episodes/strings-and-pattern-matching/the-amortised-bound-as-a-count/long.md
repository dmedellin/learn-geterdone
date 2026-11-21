---
format: long
lesson: strings-and-pattern-matching/the-amortised-bound-as-a-count
title: Amortised analysis as a count: building the KMP failure function in linear time
thumb: Falls can't outnumber rises
---

@chapter The question
@title text="The Amortised Bound, as a Count" sub="Strings and Pattern Matching" art=thumb
Some loops run many times for one input step, and hardly at all for others. Amortised means the total stays small anyway. The only honest evidence for that is the total. So let's count it.

@art outer-inner
Building the failure function walks along the pattern, holding k, the length of the current border. If the next character matches, the border grows and k rises by one. If not, k falls to fail of k, and the test repeats. That repetition is the inner loop, and it's the only part whose cost isn't one per character.

@chapter The potential argument
@art potential-meter
Treat k as a potential. It starts at zero, and never goes negative. Each step of the outer loop raises it by at most one, so over the whole pattern it rises by at most m minus one. Every inner loop step lowers it by at least one, since a border is shorter than the string it belongs to.

@math heading="Rises pay for falls" items="total rise ≤ m − 1@total rise;;each inner iteration: fall ≥ 1@each inner;;inner iterations ≤ m − 1@at most m minus one;;total work ≤ 2m − 1  →  O(m)@two m"
So the total rise is at most m minus one. Each inner iteration is a fall of at least one. Falls can't outnumber rises, so there are at most m minus one inner iterations. Add one comparison per character, and the whole construction is at most two m minus one operations.

@art staircase
Notice what the argument never does. It never bounds one character's work. One character really can cost m. But that expensive character is spending rises that earlier cheap characters paid for.

@chapter Counting it on aabaaab
@math heading="aabaaab" items="fail[1..7] = 0, 1, 0, 1, 2, 2, 3@zero, one, zero;;position 3 (b): 1 → 0@at the b;;position 6 (a): 2 → 1, then extends to 2@position six;;inner iterations: 2  ·  bound 2m = 14@two in total"
For a a b a a a b, the failure function is zero, one, zero, one, two, two, three. The inner loop fires twice. Once at the b, where a border of length one falls to zero. And once at position six, where length two falls to one, then extends back to two. Two in total, against fourteen.

@list heading="Inner iterations on the shipped patterns" items="ababaca: 2 of 14@a b a b a c a|aaaaa: 0 of 10@five a's|abcabcabd: 2 of 18@a b c a b c a b d|abcdefg: 0 of 14@a b c d e f g"
Across the other patterns, the biggest total is also two. A b a b a c a, two of fourteen. Five a's, none at all, because every character extends the border. A b c a b c a b d, two. And a b c d e f g, none, because k is zero throughout.

@art one-vs-two
On a b a b a c a, both iterations happen at a single character, the c. On a a b a a a b, it's one each at two characters. Same total. That's where amortised reasoning earns its keep, because a per character argument can't bound the first.

@chapter Small totals, honest bound
@art far-under
Two against fourteen is a factor of seven. That doesn't make the bound loose. Patterns exist whose construction does a number of fallbacks proportional to m. None of them happens to be among the presets, which is a fact about the presets.

@chapter Construction and search
@list heading="Text aabaaabaaabaabaaab, n = 18" items="Build fail: 2 inner + 6 outer@Building|Search: 19 comparisons, bound 2n = 36@the search|Naive: 42 comparisons@naive"
Building and searching are separate claims, counted separately. Building the array costs two inner iterations and six outer comparisons. The search over this eighteen character text makes nineteen comparisons, against a bound of thirty six, and finds three occurrences. The naive matcher makes forty two.

@art two-counters
The search bound uses the same argument. K rises at most once per text character, so fallbacks total at most n, and the search is at most two n. The factor of two is the fallbacks, the price of never moving the text pointer back.

@chapter Where people slip
@list heading="Common slips" items="Bounding from the worst single character@The first|Reading a small total as a tighter bound@The second|Merging construction and search costs@The third"
The first slip is arguing from the worst single character, and concluding order m squared. The second is reading a small measured total as a tighter bound. The third is merging the construction cost into the search cost. They're order m and order n, proved separately.

@chapter Try it
@words text="aaaaab"
Your turn. Build the failure function for five a's followed by a b, counting every inner loop iteration. Find the single character that costs most, then check the total is still no more than m minus one.

@end text="Count the inner loop yourself"
You can type any pattern and count every inner loop iteration against its bound, on Learn. That's learn dot get er done dot I O.
