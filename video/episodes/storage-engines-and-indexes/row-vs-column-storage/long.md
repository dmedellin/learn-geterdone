---
format: long
lesson: storage-engines-and-indexes/row-vs-column-storage
title: Row vs column storage: 100 GB or 6 GB, for the same query
thumb: Faster at which query?
---

@chapter What a scan reads
@title text="Row vs Column Storage" sub="Storage Engines and Indexes" art=thumb
Columnar storage is always faster. That's the claim. It's true for one kind of query, the analytical scan, by a large factor, and false for another, by a factor just as large.

@art row-layout
A row store keeps the values of one row together. A column store keeps the values of one column together. And a scan reads whatever the layout makes contiguous. So in a row store, a query that names three columns of twenty still reads whole rows.

@art column-layout
In a column store, each column is its own run, so the same query reads only the three columns it named.

@math heading="Bytes scanned" items="row store = r · w / ρ_row@r times w;;column store = r · (w/c) · j / ρ_col@j named columns"
For r rows of width w across c columns, the row store reads r times w, over its compression ratio. The column store reads r times one column's width, times j named columns, over its own ratio. The row store's formula has no j in it at all. Naming fewer columns can't make it read less.

@chapter A billion rows
@math heading="10⁹ rows,  200 B,  20 columns,  3 named,  1 GB/s" items="row:  10⁹ × 200 B ÷ 2 = 100.00 GB  →  100.00 s@a hundred gigabytes;;column:  10⁹ × 30 B ÷ 5 = 6.00 GB  →  6.00 s@six gigabytes;;100.00 / 6.00 = 16.67×@sixteen point six seven"
A billion rows of two hundred bytes, twenty columns of ten bytes each, and a query naming three. The row store compresses two times, so it reads a hundred gigabytes, a hundred seconds at one gigabyte a second. The column store compresses five times, so six gigabytes, six seconds. Sixteen point six seven times faster.

@chapter Where the extra comes from
@art compress-column
That's more than you might expect from naming three of twenty. Part of it is compression. A column holds lots of values of one type and often one distribution, and that compresses well.

@art compress-row
A row holds a timestamp, a name and a price side by side, and that doesn't.

@math heading="16.67× =" items="20/3 from the columns named = 6.67×@twenty over three;;5/2 from the compression = 2.50×@five over two"
So the speedup splits into twenty over three from the columns, six point six seven, times five over two from compression, two point five. Quote a columnar figure without its ratio, and half the effect is hidden.

@chapter Where it reverses
@math heading="Crossover in named columns" items="j* = c × ρ_col / ρ_row = 20 × 5/2 = 50@ratio over the row ratio;;ρ_col = 2×:  j* = 20@falls to exactly twenty"
Set the byte counts equal and solve for the named columns. That's c times the column ratio over the row ratio, fifty. There are only twenty columns, so no scan flips it here. Drop the columnar ratio to two times, as happens with values that don't compress, and the crossover falls to exactly twenty.

@art whole-row-fetch
The query that really flips it isn't a scan. Fetch one whole row by key. In a row store, it's one page read, because the row is contiguous. In a column store, it's twenty page reads, one per column. That's a factor of twenty, the other way.

@art two-workloads
So the honest claim names the query shape. For scans over a few columns of many rows, columnar wins big. For whole rows one at a time, the row store wins by the column count. A system doing both keeps the data twice, and that's a storage bill, not a trick.

@words text="Same 1 GB/s in both layouts" sub="the whole effect is bytes"
Two things were held fixed. The scan runs at one gigabyte a second in both layouts, so the whole effect is bytes. And the compression ratio is an input, measured on your own data, not derived. Whether decompressing is worth the CPU is a separate question, about cost.

@chapter Where people slip
@list heading="Common slips" items="Treating speed as a property of storage@The first|Leaving out the compression ratio@The second|Costing a point lookup at a scan's rate@the third"
The first slip is treating the comparison as a property of the storage, rather than of the query. The second is leaving out the compression ratio. And the third is costing a whole row fetch in bytes, when it's priced in I O's at a seek.

@chapter Try it
@words text="Same table, 10 columns named" sub="first move: columnar scan = 20.00 GB"
Your turn. Same table, but name ten columns. The columnar scan becomes twenty gigabytes. Work out both times and the ratio, then say what the crossover becomes if columnar compression falls to three times.

@end text="Name the query shape"
You can change the columns named and the compression, and watch the bytes, on Learn. That's learn dot get er done dot I O.
