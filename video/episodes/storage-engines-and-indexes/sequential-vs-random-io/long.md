---
format: long
lesson: storage-engines-and-indexes/sequential-vs-random-io
title: Same gigabyte, 250 times slower: sequential vs random I/O
thumb: Count the seeks first
---

@chapter The same gigabyte
@title text="Sequential vs Random I/O" sub="Storage Engines and Indexes" art=thumb
Read a gigabyte off a disk in one sweep and it takes about ten seconds. Read the same gigabyte four kilobytes at a time and it takes forty two minutes. Same bytes, same disk. So where did the time go?

@art two-terms
A read has two costs. A fixed cost for every place it starts, the seek, when the arm moves and nothing is transferred. And a cost for every byte it moves. Write both down separately, before you add them.

@math heading="Read time" items="time = s × t_seek + B / bw@s seeks times;;sequential:  s = 1@a sequential read;;random, chunks of c:  s = ⌈B / c⌉@chunks of c"
The read time is s seeks times the seek time, plus the bytes over the bandwidth. A sequential read is s equals one. A random read in chunks of c is B over c seeks, rounded up. It's one formula, and only s changes between the two rows.

@chapter Worked out
@art one-sweep
Take a disk with a ten millisecond seek and a hundred megabytes a second. One sweep of a gigabyte is one seek, ten milliseconds, plus ten seconds of bytes. Ten point oh one seconds.

@art many-seeks
Now read it four kilobytes at a time. That's a billion over four thousand, two hundred and fifty thousand seeks.

@math heading="1 GB,  10 ms,  100 MB/s" items="sequential:  0.01 s + 10.00 s = 10.01 s@ten point oh one;;random 4 kB:  250 000 × 0.01 s = 2 500.00 s@two thousand five hundred;;+ 10.00 s = 2 510 s ≈ 41.8 min@forty one point eight;;ratio = 2 510 / 10.01 = 250.75@two hundred and fifty point seven five"
Against the sweep's ten point oh one seconds, two hundred and fifty thousand seeks at ten milliseconds is two thousand five hundred seconds. Add the same ten seconds of bytes, and you get two thousand five hundred and ten seconds, about forty one point eight minutes. The ratio is two hundred and fifty point seven five.

@words text="The bytes term: 10.00 s on both rows"
The bytes term didn't move. It's ten seconds on both rows. Every one of those forty two minutes is seeking. So size over bandwidth isn't a model of reading. It's a model of one access pattern.

@chapter The crossover chunk
@art crossover-point
Here's a number worth carrying around. Ask for the chunk size where one seek costs exactly what one chunk of transfer costs. Seek time equals c over bandwidth, so c equals seek time times bandwidth. Call it c star. Below it, the arm decides the time and the size of each read barely matters. Above it, the bandwidth decides and the seek barely matters.

@math heading="c* = t_seek × bw" items="disk:  10 ms × 100 MB/s = 1 MB@one megabyte;;ratio ≈ 1 + c*/c = 1 + 10⁶/4 000 = 251@two hundred and fifty one;;c = c*:  2,   c = 4 MB:  1.25@one point two five"
For the disk, ten milliseconds times a hundred megabytes a second is one megabyte. Then the ratio is about one plus c star over c, one plus a million over four thousand, two hundred and fifty one, against the exact two fifty point seven five. At c star itself, the ratio is two. At four megabytes, one point two five.

@chapter Faster hardware
@art three-devices
Change the device. A solid state drive with a hundred microsecond seek and five hundred megabytes a second has c star at fifty kilobytes, and the four kilobyte ratio falls to thirteen point five. Still more than ten times.

@words text="NVMe: c* = 60 kB,  4 kB ratio 16.00"
Now NVMe, twenty microseconds and three thousand megabytes a second. Its c star is sixty kilobytes, larger, and its four kilobyte ratio is sixteen, slightly worse. Bandwidth grew faster than the seek fell. The penalty isn't about how old the device is.

@art spec-vs-workload
And the spec sheet is just the bandwidth term. That hundred megabyte a second disk, under four kilobyte random reads, moves about four hundred kilobytes a second. Both are true of the same device.

@chapter Where people slip
@list heading="Common slips" items="Quoting size ÷ bandwidth as the read time@The first|Reading the spec as your throughput@The second|Assuming new hardware makes it stop mattering@the third"
The first slip is quoting size over bandwidth as the read time. The second is reading the spec sheet as throughput on your workload. And the third is assuming newer hardware makes the pattern stop mattering. It shrinks the ratio, but never removes it.

@chapter Try it
@words text="1 GB on SATA SSD: 100 µs, 500 MB/s" sub="first move: c* = 50 kB"
Your turn. Same gigabyte, the solid state preset. Its c star is fifty kilobytes. Predict the four kilobyte ratio from that alone, then compute both times and check. Then find a chunk size that reads the gigabyte in under three seconds.

@end text="Count the seeks first"
You can move the chunk size and the device, and watch the two terms, on Learn. That's learn dot get er done dot I O.
