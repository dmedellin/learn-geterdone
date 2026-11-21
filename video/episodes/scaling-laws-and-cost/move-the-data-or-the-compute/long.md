---
format: long
lesson: scaling-laws-and-cost/move-the-data-or-the-compute
title: Move the data or the compute? Four hours against forty milliseconds
thumb: Bytes against bytes
---

@chapter Two placements
@title text="Move the Data or the Compute" sub="Scaling Laws and Cost" art=thumb
You want to count something in a two terabyte table on another machine. Either the data comes to your job, or your job goes to the data. One of those takes over four hours. The other takes forty milliseconds.

@art data-to-job
Moving the data takes the dataset size, D, over the link bandwidth. That's the default, because it's the easiest thing to write.

@art job-to-data
Moving the compute takes the code plus the result, over the same bandwidth. The processing itself is assumed to take the same time wherever it runs, so it's on both sides and drops out. The code is a few hundred kilobytes, and the result of a count or a filter is usually tiny.

@chapter A count over two terabytes
@math heading="D = 2 TB,  result 5 MB,  code 200 kB,  125 MB/s" items="move the data:  2 000 000 ÷ 125 = 16 000 s = 4.44 h@four point four four hours;;move the compute:  5.2 ÷ 125 = 0.0416 s = 41.6 ms@forty one point six;;ratio 384 615×@three hundred and eighty four thousand"
Take a two terabyte table, a two hundred kilobyte job, a five megabyte result, and a gigabit link, a hundred and twenty five megabytes a second. Moving the data takes sixteen thousand seconds, four point four four hours. Moving the compute takes forty one point six milliseconds. That's three hundred and eighty four thousand six hundred and fifteen times apart.

@chapter The link cancels
@art same-pipe
Here's the part that surprises people. Both plans divide by the same link. So write the comparison out.

@math heading="Move the compute is faster when" items="(code + result)/bw < D/bw@code plus result;;multiply by bw:  code + result < D@bytes against bytes"
Moving the compute is faster when code plus result over b w is less than D over b w. Multiply both sides by b w, and it's gone. The decision is code plus result against D. Bytes against bytes.

@art faster-link
So a faster network doesn't change the answer. Make the link a hundred times faster, and the two plans become a hundred and sixty seconds and point four two milliseconds. Still the same factor apart. Buying bandwidth to avoid moving a computation is paying to lose the same argument faster.

@chapter The ratio decides
@words text="result / input = 5 MB / 2 TB = 1/400 000"
So the question is the result to input ratio. Here, five megabytes over two terabytes, one in four hundred thousand. And that's generous. A count returns a few bytes. The plans tie only when the result is about the size of the whole dataset. A ratio near one is worth a second look. One in four hundred thousand isn't.

@words text="SELECT count(*) …  not the table"
That's why query languages exist. Sending a count query instead of the table is exactly this arithmetic. So is a stored procedure, a map reduce job, an edge function, and a pushdown predicate. Each ships a small amount of code to where a large amount of data already lives.

@chapter When it flips
@art result-explodes
It inverts when the result isn't small. A job that decompresses, joins or enriches can emit more than it reads. Then code plus result is bigger than D, and the data should come to the compute.

@art split-the-job
Or better, split the job. Run the reducing part right next to the data, and send only its output.

@words text="Jurisdiction · where code may run · repetition"
Some constraints override the arithmetic. Data may not be allowed to leave its jurisdiction. Code may not be allowed near the data. And repetition changes the counts: one big transfer against a thousand small queries is D against a thousand times code plus result.

@chapter Where people slip
@list heading="Common slips" items="Pulling everything to the client@The first|Believing a faster link will fix it@The second|Forgetting processing time is assumed equal@the third"
The first slip is pulling everything to the client, because it's easiest to write. The second is believing a faster link will fix it. And the third is forgetting the processing time is assumed equal. A storage tier with little processor beside it can break that.

@chapter Try it
@words text="2 TB table,  1.5 TB result" sub="decide in bytes first"
Your turn. Keep the two terabyte table, but make the job emit one and a half terabytes, a decompressing scan. Decide from code plus result against D which side wins, then work out both durations, and say what result size would tie.

@end text="Decide in bytes"
You can move the dataset, the result and the link, and watch the verdict hold, on Learn. That's learn dot get er done dot I O.
