---
format: long
lesson: combinatorics-and-counting/inclusion-exclusion
title: Inclusion–exclusion: add, subtract, add back
thumb: Add, subtract, add back
---

@chapter The over-count
@title text="Inclusion–Exclusion" sub="Combinatorics and Counting" art=thumb
When sets overlap, the sum rule over counts. Inclusion and exclusion corrects that exactly. Add the sizes, subtract the pairs, and add back the triples.

@art two-venn
With two sets, anything in both was counted twice. So the size of A union B is the size of A, plus the size of B, minus the size of their intersection.

@math heading="Two sets" items="|A ∪ B| = |A| + |B| − |A ∩ B|@A union B;;20 + 15 − 6 = 29@twenty plus fifteen"
Put numbers on it. If A has twenty elements, B has fifteen, and six are in both, then A union B has twenty plus fifteen minus six: twenty nine.

@chapter Three sets
@art three-venn
With three sets, it takes one more step. Add the three sizes. Subtract the three pairwise intersections. Then add back the triple intersection.

@art sign-arrows
Why add it back? An element in all three was counted three times by the singles, then subtracted three times by the pairs. That leaves it at zero. One addition restores it to exactly one.

@math heading="Three sets" items="|A ∪ B ∪ C| = Σ|A| − Σ|A ∩ B| + |A ∩ B ∩ C|@add the singles"
So: add the singles, subtract the pairs, add the triple. With more sets the pattern continues, alternating over every non empty group of the sets.

@chapter Why the signs work
@math heading="An element in exactly m sets" items="C(m,1) − C(m,2) + C(m,3) − ⋯@C of m, one;;= 1 − [C(m,0) − C(m,1) + C(m,2) − ⋯]@one minus;;= 1 − 0 = 1@exactly one"
Take an element in exactly m of the sets. It's counted C of m, one times, then minus C of m, two, then plus C of m, three, and so on. That's one minus the alternating row sum of Pascal's triangle, which is zero. So it's counted exactly one time.

@words text="the signs are forced"
So the signs aren't a rule to memorise. They're exactly what it takes to make every element count once. An element in none of the sets adds nothing to any term.

@chapter None of the properties
@art complement-ring
Usually you want the complement: the objects with none of the properties. That's the total minus the union, the same alternating sum, starting from everything.

@math heading="1 to 1000, divisible by none of 2, 3, 5" items="1000 − (500 + 333 + 200)@A thousand minus;;+ (166 + 100 + 66)@Plus a hundred and sixty six;;− 33@Minus thirty three;;= 266@two hundred and sixty six"
How many of one to a thousand are divisible by none of two, three and five? A thousand minus five hundred, three hundred and thirty three, and two hundred. Plus a hundred and sixty six, a hundred, and sixty six for the pairs. Minus thirty three for all three. That's two hundred and sixty six.

@art number-sieve
Each term is a floor division. Multiples of both two and three are the multiples of six, and a thousand over six, rounded down, is a hundred and sixty six. In general, use the least common multiple. Of one to a hundred, those divisible by four and six are the multiples of twelve: eight of them, not four.

@chapter Counting surjections
@art function-arrows
How many functions from a five element set onto a three element set hit every target? There are three to the fifth, two hundred and forty three functions in all. The direct count is hard, but the violations are easy. Let A x be the functions that miss target x.

@math heading="Onto functions, 5 → 3" items="|Aₓ| = 2⁵ = 32, three of them@thirty two;;|Aₓ ∩ A_y| = 1⁵ = 1, three of them@just one function;;all three: 0⁵ = 0@all three;;243 − (3·32 − 3·1 + 0) = 150@a hundred and fifty"
Missing one target leaves two choices per element: thirty two, and there are three such sets. Missing two leaves just one function, three times over. Missing all three is impossible. So ninety three functions miss a target, and the surjections number a hundred and fifty.

@chapter Where people slip
@list heading="Common slips" items="Getting the sign pattern wrong@The first|Missing an intersection term@The second|Assuming every intersection is equal@And the third"
The first slip is getting the sign pattern wrong, so write down which form you're using. The second is missing an intersection term. With four sets there are fifteen terms. And the third is assuming the intersections are all equal. Often they are, by symmetry, but check. Then sanity check the size: the answer must lie between zero and the total.

@chapter Try it
@words text="permutations of 1 to 6, nothing in its own place" sub="Aᵢ = “i stays put”"
Your turn. Count the permutations of one to six in which no element stays in its own position. Let A i be the permutations where i stays put, compute the intersections, and alternate. That count has a name, and it's the next lesson.

@end text="Build the alternating sum yourself"
You can build the alternating sum term by term, and check it against a direct count, on Learn. That's learn dot get er done dot I O.
