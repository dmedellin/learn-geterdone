# Review: wealth-stock-and-money (Course 7, Stock, Money and Banks)

Files: `content/wealth_of_nations/c07_stock/part_a.py`. No spoken forms were needed.

## Gates

- Before: `preview_subject.py --course wealth-stock-and-money` printed OK (5 pages, 5
  pinned). `quotes.py`: no MISS.
- After: OK (5 pages, 5 pinned, 0 failing). `quotes.py`: no MISS.

## Fixes

**Accuracy against the text.**
1. Lesson 1, lab and prose: the weaver's food until his web is sold was classed as
   circulating capital. Smith's Chapter 1 puts exactly that food in the stock reserved
   "for his immediate consumption", meaning what "may maintain him till this revenue
   begins to come in" (l. 8915–8919), and lesson 2 opens on that very sentence. In all
   three presets the food is now `consumption`. I re-pinned from my own sums, and the
   page agrees: capital is 1/2 for the weaver, 3/4 once the work is divided, and 5/14 for
   the long wait. I rewrote the body, the worked lines, mistake 3 and quiz 3. Quiz 3 now
   says "food for his own table", its answer moves to nine twentieths, and three quarters
   is the distractor for counting food as capital. The body says that food a master
   advances as wages would be circulating capital to the master (l. 8963–8966). The lesson
   also gained a point it lacked: a longer wait needs more stock and adds no capital.
2. Lesson 4: cash accounts were called "a Scottish peculiarity". Smith says credits of
   this kind are granted "in all different parts of the world" and that only the easy
   terms of repayment were peculiar to the Scots. He calls those terms "perhaps" the
   principal cause of the benefit (l. 9616–9626). Corrected.
3. Lesson 4: the £5 note rule had been presented as Smith's demand. It is his "It were
   better, perhaps, that no bank notes were issued…" (l. 10533), and it is now quoted
   with its hedge.
4. Lesson 5: the image is "The house is crazy, says a weary traveller" (l. 10051–10053),
   not an inn that "is rotten".
5. Lesson 5, mistake 3: it quoted "proportioned to their capitals", which occurs only as
   "disproportioned to their capitals" in Book II Chapter 4 (l. 13875). quotes.py passed
   it as a substring. It now quotes II.2's own advice to borrow "upon bond or mortgage, of
   such private people as propose to live upon the interest of their money"
   (l. 9973–9974).
6. Lesson 5: "Eight per cent is at or above the ordinary profit" did not fit Smith's
   "between six and ten" (l. 10077–10078). It now says eight would take most or all of
   such a profit.
7. Lesson 3: "a note on a bankrupt, like a guinea no one will take" turned Smith's
   comparison round. He says a guinea that could buy nothing would be "like a bill upon a
   bankrupt" (l. 9344). The muddled "Smith has the same thought on his side" was removed.
8. Source comments: lesson 4's ranges for cash accounts and the forty thousand pounds
   were corrected, and lesson 5 gained the bill's privileges (l. 10036–10053). The other
   ranges were checked and are right.

**Labs and teaching.**
9. In every lesson the body now names each preset by its id (weaver, divided, long-wait;
   parish, farmer, iron-work; undertaker, cheaper-machinery, country, paper; banker,
   million, forty, forty-four; two-months, ayr-bank, three-months) beside its figure. It
   used to say "the third preset". The long-wait preset had no body paragraph at all and
   now has one.
10. Lesson 5, quiz 1: the distractor "18 per cent" matched no mistaken method. It is now
    42 per cent, which is the year's interest charged at every draw.
11. Lesson 4: the worked example said a reserve tile "should be read against his
    fourteen thousand". It now gives what the tile prints: £14,000, £3,000 more than the
    quarter kept.

**Prose.**
12. Lesson 1 opened with a quotation that started in mid-sentence ("in which there is no
    division…"). It now has a lead-in. The forty-thousand case got the same treatment.
13. Lesson 2: a run-on sentence beginning "Their purpose is 'the sole end and purpose…'
    to maintain" was recast. "The three preset farms" became "the three presets", since
    only one of them is a farm.
14. Lesson 3: a quotation that read "may in that of other people" was rebuilt so that it
    makes sense standing alone.

## Checked and left

Every pinned tile in lessons 2–5 against my own arithmetic, including the compound redraw
cost of ≈ 8.27%. The claims about Marx, Ricardo, the 1797–1821 Restriction, Thornton
(1802) and the Ayr bank (1769–72). Every lesson closes on what the lab cannot settle.

## Left undone

- Lessons 2–5 have the same answer positions (2, 1, 3, 0). Each lesson is spread within
  itself, so I left them.
