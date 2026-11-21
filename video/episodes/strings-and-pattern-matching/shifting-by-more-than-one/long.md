---
format: long
lesson: strings-and-pattern-matching/shifting-by-more-than-one
title: Horspool's algorithm: read the window from the right, then jump
thumb: 48 characters never read
---

@chapter The question
@title text="Shifting by More Than One" sub="Strings and Pattern Matching" art=thumb
Every matcher so far moves the pattern one place at a time, or reads every text character at least once. Horspool's algorithm jumps. On ordinary text, it never even looks at most of the characters.

@art right-to-left
Here's how it works. Put the pattern's window over the text, and compare from the right end, moving left, until something disagrees or the whole pattern matches. Then shift the window. And the shift is read from one fixed place, the text character under the window's last position, wherever the comparison actually failed.

@chapter The shift table
@math heading="shift[c]" items="shift[c] = m − 1 − j,  j = last index ≤ m − 2 with p[j] = c@m minus one minus j;;shift[c] = m  if c is not in p[0..m−2]@isn't among"
The table has one entry per character. Find the last place c occurs in the pattern, ignoring the final position. If that's index j, shift by m minus one minus j. If c isn't among the first m minus one characters at all, shift by the full m.

@math heading="Pattern mainly" items="m → 5 · a → 4 · i → 3 · n → 2 · l → 1@m goes to five;;everything else → 6,  including y@everything else"
For the pattern mainly, m goes to five, a to four, i to three, n to two, and l to one. Everything else shifts the full six, including y, the pattern's own last letter, because the table leaves out the final position.

@art y-shifts-six
That y entry is deliberate. If the window ends on a y and the comparison still failed, the failure was further left. No alignment before the full jump could succeed either. And at the other end, l shifts only one, so a pattern whose second last letter is common loses most of the benefit.

@chapter Why no match is skipped
@art no-skip
Why is a jump safe? Suppose a match started somewhere inside the jump. The character under the window's last position would sit inside that match, at some pattern index before the last. So it occurs in the pattern there, and the table's shift is never longer than the distance to its last such occurrence. A contradiction.

@words text="checked against a scan of every offset" sub="a shorter list of matches looks just like a right one"
The lab doesn't just trust that argument. A skipping algorithm's failure mode is jumping over an answer, and returning a shorter list of positions, which looks exactly like a correct answer. So the matches are compared with a scan of every offset, on every keystroke.

@chapter On the rain in Spain
@words text="the rain in spain stays mainly in the plain and never in the hills" sub="66 characters · pattern: mainly"
The lab opens on the rain in spain stays mainly in the plain and never in the hills, sixty six characters, searching for mainly.

@list heading="What Horspool does" items="14 of 61 alignments examined@fourteen|7 of 14 shifts are the full 6@seven of its fourteen|13 fail at once + 1 match of 6 = 19 comparisons@thirteen|19 comparisons at 18 positions@eighteen"
Naive matching would try sixty one alignments. Horspool examines fourteen, and seven of its fourteen shifts are the full six. Thirteen alignments fail on the first comparison, and the match at offset twenty four costs six. That's nineteen comparisons, at only eighteen distinct positions.

@art never-read
Position twenty four gets compared twice, once as a window's last character, then again inside the match. So forty eight of the sixty six characters are never compared to anything at all. That's what the algorithm is famous for.

@math heading="Average shift" items="sum of shifts = 66@sixty six;;66 / 14 = 33/7 ≈ 4.71@thirty three over seven"
The shifts add up to sixty six, the text length, because the window walks past the end exactly once. Divide by the fourteen alignments, and the average shift is thirty three over seven, about four point seven one.

@chapter What didn't improve
@list heading="Same text" items="Naive: 66 · worst case m(n − m + 1)@Naive|KMP: 66 · worst case 2n@KMP|Horspool: 19 · worst case m(n − m + 1)@Horspool"
Naive takes sixty six comparisons here, and so does KMP. Horspool takes nineteen, three and a half times better. But its worst case is the same as naive's, m times n minus m plus one, while KMP's stays two n. The fastest one here has the weakest guarantee.

@art three-guarantees
There's no contradiction there, and no ranking either. Three measurements and three bounds are six statements about different things. Only the bounds hold for texts nobody has typed yet.

@chapter Where people slip
@list heading="Common slips" items="Reading the shift from the mismatching character@The first|Assuming a big alphabet guarantees big shifts@The second|Quoting comparisons as characters examined@The third"
The first slip is reading the shift from the character that mismatched. That makes the algorithm wrong, not just slow. The second is assuming a big alphabet guarantees big shifts. On the four letter DNA preset, the average drops to two point seven one. The third is quoting the comparison count as the characters examined. Nineteen against eighteen, here.

@chapter Try it
@art jump-table
Your turn. Build the shift table for plain, from its first four letters. Which letters shift one, two, three and four, and what does everything else shift? Then predict whether the n in the text shifts the window far.

@end text="Watch Horspool skip"
You can search any text and see exactly which characters Horspool never reads, on Learn. That's learn dot get er done dot I O.
