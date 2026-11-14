# Review: Taxes and Public Debts (wealth-taxes-and-public-debts)

Files changed: `content/wealth_of_nations/c13_taxes/__init__.py`, `part_a.py` and
`part_b.py`. No spoken forms were needed.

## Gates

- Before: `preview_subject.py --course wealth-taxes-and-public-debts` printed OK
  (7 pages, 7 pinned, 0 failing). `quotes.py` reported no MISS.
- After: OK (7 pages, 7 pinned, 0 failing). `quotes.py` reported no MISS.

## Fixes

**Accuracy against the text**

1. L1: the claim that 3 per cent was "the rate to which the public funds had by then
   fallen" is not in Part I. The rate is now tied to where it comes from: Smith's Bank
   of England example, in which the government "could borrow this capital at three per
   cent." (l. 26607). I made the same correction in the worked example's intro.
2. L1 mistake: "the cost to the country is three times the revenue" is now "the people
   lose three times what the proprietors do" (l. 26810-26813).
3. L2: the garbled quotation `so that "which valuation is not afterwards to be altered"`
   has been rewritten so that it reads correctly.
4. L3: the window tax compares houses of "ten pounds rent" and "five hundred pounds
   rent" (l. 27669-27671). The prose had "a £10 house", which reads as the house's
   price; it now says rent.
5. L5: "He closes the chapter with a comparison" is now "Near the end of the chapter".
   The Holland paragraph comes after the comparison (l. 29788).
6. L6: in the war preset the loan is added at the end of year 6, after six payments,
   which is the kit's rule. The prose said "paid for five years", and the worked line
   read "interest 3", which was meaningless. Both now give the hand-computed figures:
   debt ≈ 122.53 after six payments, ≈ 222.53 after the loan, and interest ≈ 6.68,
   which is more than the 4.87 payment.
7. L7 mistake: "the colonies' cost is a project of the imagination" is now Smith's
   claim, that the empire has been "the project of an empire" (l. 31288).

**Accuracy about others**

8. L6: the lesson said "Robert Barro in 1974 gave this the name of Ricardian
   equivalence". Barro revived the argument, but the name came later and was not his.
   The sentence now says "it has since been called". I also tightened Ricardo's
   reasoning, and added that he doubted taxpayers see it that way.
9. L2: the lesson said Mill's equality of sacrifice "leads to a heavier rate on the
   rich". Mill asked for an untaxed minimum and proportional rates above it, and it was
   later writers who drew progression from his rule. The lesson now says so.
10. Checked and kept: Henry George, Ricardo on taxes on rent and on wages, Lerner's
    "owe it to ourselves", Swift's saying, Marx on the national debt as a lever of
    primitive accumulation, and the three Capital lesson titles, which match
    `content/capital`.

**One-ninth, and the debase tiles**

11. L4's prose already called Smith's one-eighth a slip for one-ninth, which agrees
    with the kit's rule sentence. I made the `tenth` preset's label say so as well:
    "he says one-eighth, a slip: his rule gives one-ninth".
12. The debase tiles now read Metal owed and Metal paid, and the as is copper. The
    course and lesson key line "silver paid = debt × new silver / old silver" is now
    "metal paid = debt × new metal / old metal".

**Labs**

13. In L1, `improved` showed two tiles reading "no second rate given", and
    `crown-sale` one reading "no present yield given". `improved` now also prices the
    £1,000 rent at forty years' purchase: £40,000, +£10,000, +1/3. `crown-sale` now
    carries its £250 yield: £10,000 is forty years of it. Both are hand-checked,
    re-pinned from `--observe`, and described in the prose.

## Checked, no change

I checked every figure against its line, and all of them held:
- Bank of England: £10,780,000, 5½%, £592,900, £323,400 and £269,500.
- The ten and twenty millions, and the third of the produce.
- Tithe: 5/10 → 4/10 and 2/10 → 1/10, which is four and ten shillings in the pound.
- The £60 and £50 houses.
- Stock taxed at 24 and 20 shillings; the Dutch 2% as 13s 4d in the pound.
- Wages: 10s → 12s 6d; 100/9; 13s 4d.
- Bohemia: £9 7s 6d.
- The salt, leather, soap, candle and coal duties.
- Customs for 1755: £5,068,000 → £2,455,500.
- Every debt figure from 1697 to 1775: 21.5, 16.4, 53.7, 46.95, 78.3, 122.6 and
  129.1 millions.
- Debasement: £21,333,333 6s 8d and £5,333,333 6s 8d, and the 6s 8d of the alloy.
- The empire: 13 millions → £16.25m, £15.25m and £6.25m.

The quiz arithmetic and distractors also hold, and the correct answers are spread
across positions. The last lesson closes the book and the Subject, and points to
Capital as the next read-along.

## Left undone

Nothing.
