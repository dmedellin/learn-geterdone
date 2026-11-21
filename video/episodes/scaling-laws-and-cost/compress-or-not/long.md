---
format: long
lesson: scaling-laws-and-cost/compress-or-not
title: Compress or not? The file size doesn't matter
thumb: Faster links send raw
---

@chapter Processor time for wire time
@title text="Compress or Not" sub="Scaling Laws and Cost" art=thumb
Always compress before you send. It's a habit from slow links. On a fast one, the same file goes over five times slower compressed. Here's how to tell which side you're on.

@art raw-send
Sending raw takes the size over the link bandwidth. One stage.

@art squeeze-then-send
Compressing has two stages. First squeeze it at the compressor's rate, then send k times fewer bytes. Here the receiver stores the compressed form, so decompression isn't on the critical path.

@math heading="Two transfer times" items="raw = size / bw@size over b w;;compressed = size / rate + size / (k · bw)@size over rate"
So raw is size over b w. Compressed is size over rate, plus size over k times b w.

@chapter A gigabit link
@math heading="10 GB,  1 000 Mbit/s = 125 MB/s,  k = 4,  250 MB/s" items="raw = 10 000 ÷ 125 = 80 s@eighty seconds;;squeeze = 10 000 ÷ 250 = 40 s@forty seconds;;send = 2 500 ÷ 125 = 20 s@takes twenty;;compressed = 60 s,  1.33× faster@sixty seconds"
Take ten gigabytes over a gigabit link, which is a hundred and twenty five megabytes a second. Raw takes eighty seconds. Compressing four to one at two hundred and fifty megabytes a second takes forty seconds, then sending two and a half gigabytes takes twenty. Sixty seconds, so compressing wins by one point three three.

@words text="Squeeze: 66.7% of the compressed plan"
Notice two thirds of that is the compressor, not the network. That's the usual shape once links are fast.

@chapter Set them equal
@math heading="Break-even" items="size/bw = size/rate + size/(k·bw)@set the two times equal;;1/bw = 1/rate + 1/(k·bw)@divide by size;;bw* = rate · (k − 1)/k = 250 × 3/4 = 187.5 MB/s@one eighty seven point five;;rate* = bw · k/(k − 1) = 125 × 4/3 = 166.67 MB/s@a hundred and sixty six"
Now set the two times equal. Every term has one factor of size, so divide by size and it disappears. Rearrange, and the break even bandwidth is rate times k minus one over k, one eighty seven point five megabytes a second. Or fix the link, and the compressor needs to beat a hundred and sixty six point six seven.

@art size-cancels
That's the most useful fact here. The file size decides how long both plans take, and nothing about which is faster. So you decide once per link, not once per file. Fix the compressor, and you get a bandwidth. Above fifteen hundred megabits a second, raw is faster, so a datacentre link defeats this compressor and a wide area link doesn't. Fix the link instead, and you get a throughput the compressor has to beat.

@chapter A ten gigabit link
@art fast-link
Send the same ten gigabytes over ten gigabits a second, twelve hundred and fifty megabytes. Raw, eight seconds. Compressed, forty to squeeze plus two to send, forty two. Compression is now five point two five times slower. Nothing about the file changed. Twelve fifty is just above the break even.

@chapter Ratio or throughput?
@art ratio-saturates
The factor k minus one over k saturates fast. It's a half at two, three quarters at four, nine tenths at ten. Doubling the ratio from four to eight moves the break even from a hundred and eighty seven point five to two hundred and eighteen point seven five, seventeen percent.

@art throughput-doubles
Doubling the compressor's speed doubles it, to three hundred and seventy five. So when both are on offer, the faster compressor is nearly always the better trade. That's the arithmetic behind years of compression libraries choosing speed over ratio. Past about four to one, extra ratio buys little on the wire.

@words text="1 000 Mbit/s = 125 MB/s" sub="divide by eight"
And one units warning. Links are quoted in bits, payloads in bytes. A factor of eight causes more wrong answers here than the algebra does.

@chapter Where people slip
@list heading="Common slips" items="Always compressing@The first|Shopping for ratio instead of throughput@The second|Leaving out the far end when it counts@the third"
The first slip is always compressing. The second is shopping for ratio instead of throughput. And the third is leaving decompression out when the receiver must expand the data before it can act. Then it's on the critical path, and it pushes the answer toward sending raw. If the receiver just stores or forwards the compressed bytes, leave it out, and say which you assumed.

@chapter Try it
@words text="Gigabit link,  k = 10 at 60 MB/s" sub="first move: rate*"
Your turn. Keep the gigabit link and take a slower, stronger compressor, ten to one at sixty megabytes a second. Predict from rate star alone which way the verdict goes. Then time both plans and check.

@end text="Decide once per link"
You can move the link, the ratio and the compressor and watch the verdict, on Learn. That's learn dot get er done dot I O.
