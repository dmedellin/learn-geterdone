---
format: long
lesson: storage-engines-and-indexes/working-set-and-the-page-cache
title: The page cache: 13% of the data, 89% of the reads
thumb: Skew is why it works
---

@chapter Not every read hits the disk
@title text="Working Set and the Page Cache" sub="Storage Engines and Indexes" art=thumb
Your data is on disk, so every read is a disk read. That sounds obvious, and it's wrong by a factor of about nine.

@art pages-vs-memory
The page cache holds some of a dataset's pages in memory. It's the cache you already know, with pages in place of objects, and page reads in place of requests. Same formula, no second model. If you can size a cache, you can size a page cache.

@math heading="Zipf popularity, exponent s" items="h = H(C, s) / H(N, s)@the hit rate;;disk IOPS = (1 − h) × reads@one minus h"
With C pages resident out of N, and Zipf popularity with exponent s, the hit rate is a ratio of harmonic numbers, H of C over H of N. And the disk still sees one minus h, times the reads.

@chapter Convert to pages first
@art units-convert
The formula counts pages, not bytes, so convert first. At an eight kilobyte page, a five hundred gigabyte dataset is sixty two and a half million pages. Sixty four gigabytes of memory is eight million pages. That's twelve point eight percent of the data. A units slip here moves the answer more than the skew does.

@chapter Skewed against uniform
@art skew-curve
Now the skew. At the classic Zipf exponent of one, a few pages are asked for constantly, and the long tail rarely.

@math heading="s = 1,  20 000 reads/s" items="h = H(8 000 000, 1) / H(62 500 000, 1) ≈ 88.905%@eighty eight point nine;;disk = (1 − 0.88905) × 20 000 ≈ 2 219 /s@two thousand two hundred and nineteen"
So the hit rate is about eighty eight point nine percent. At twenty thousand page reads a second, about two thousand two hundred and nineteen reach the disk. Twelve point eight percent of the pages carry nearly nine reads in ten.

@art uniform-flat
Now make popularity uniform, an exponent of zero. The formula collapses to C over N, sixteen over a hundred and twenty five, exactly twelve point eight percent. And the disk sees seventeen thousand four hundred and forty reads a second.

@art miss-trickle
Same memory, same data, and the disk sees nearly eight times as much. So skew isn't a detail of the workload. It's the reason the page cache exists. And it's measured from a trace, not assumed. The disk figure is the one to hold against what the storage can actually do.

@chapter Each doubling of memory
@math heading="Memory as a share of the data" items="1/64:  77.553%   4 489 IOPS@a sixty fourth;;1/16:  85.036%   2 993 IOPS@a sixteenth;;1/4:  92.518%   1 496 IOPS@a quarter;;1/2:  96.259%   748 IOPS@a half"
Hold the data and skew, and walk the memory up. At a sixty fourth of the data, seventy seven point five five three percent, four thousand four hundred and eighty nine reads a second on disk. At a sixteenth, eighty five point oh three six. At a quarter, ninety two point five one eight. At a half, ninety six point two five nine, and seven hundred and forty eight.

@art doubling-steps
Every doubling adds about three point seven four points of hit rate, and removes about seven hundred and forty eight reads a second. The same amount each time, not the same fraction. That's H of C growing like a logarithm. So the first doubling and the last are worth the same to the disk, and the last costs thirty two times more memory.

@words text="Rounded, and a model" sub="exact only at s = 0"
Two honesty notes. At these sizes the hit rate comes from a floating point approximation, so it's rounded. And Zipf describes many real workloads, but none exactly. Read ahead and dirty pages both shift the real figure.

@chapter Where people slip
@list heading="Common slips" items="Assuming every read is a disk read@The first|Sizing memory against the whole dataset@The second|Expecting IOPS to halve when memory doubles@the third"
The first slip is assuming every read is a disk read, and buying nine times the IOPS you need. The second is sizing memory against the whole dataset, instead of the working set. And the third is expecting disk reads to halve when memory doubles. They fall by a fixed amount.

@chapter Try it
@words text="32 GB of memory" sub="first move: C = 4 000 000 pages"
Your turn. Halve the memory to thirty two gigabytes. That's four million pages. Work out the hit rate and the disk reads, check them against the doubling rule, and estimate how much memory gets the disk below fifteen hundred reads a second.

@end text="Convert, then skew"
You can move the memory and the skew and watch the disk reads, on Learn. That's learn dot get er done dot I O.
