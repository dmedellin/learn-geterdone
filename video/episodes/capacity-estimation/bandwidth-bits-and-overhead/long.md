---
format: long
lesson: capacity-estimation/bandwidth-bits-and-overhead
title: Bandwidth: the factor of eight and the header crossover
thumb: Bits, not bytes
---

@chapter The question
@title text="Bandwidth: Bits, Bytes and Overhead" sub="Capacity Estimation" art=thumb
Two thousand requests a second, each about a kilobyte. What link do you need? There are two traps in that question. One is a factor of eight. The other is the bytes you forgot to send.

@art bits-and-bytes
A link is sold in bits per second. A payload is measured in bytes. A byte is eight bits, so bytes per second times eight is bits per second. A megabit per second is ten to the six bits a second, decimal, because that's how links are sold.

@chapter The chain
@math heading="2 000 req/s, 1 200 bytes each" items="2 000 req/s × 1 200 B/req = 2 400 000 B/s@twelve hundred;;× 8 bit/B = 19 200 000 bit/s@times eight;;÷ 10⁶ bit/Mbit = 19.2 Mbit/s@nineteen point two"
Write it as a chain. Two thousand requests a second times twelve hundred bytes a request is two point four million bytes a second. Times eight bits per byte is nineteen point two million bits a second. Divide by a million and that's nineteen point two megabits a second.

@words text="2.4 “Mbit/s” = the truth ÷ 8"
Skip the times eight and you'd call it two point four. That's exactly an eighth of the truth, for every input. And it looks perfectly plausible, because an eighth of a reasonable number is another reasonable number. Writing bits per byte on its own row is the fix.

@art link-pipe
So the chain runs requests per second, bytes per request, bits per byte, bits per megabit. Four rows, three of them conversion factors, each carrying its unit. Written out, the eight is impossible to miss. Done in your head, it's the most common defect in a bandwidth estimate.

@chapter Overhead
@art header-and-payload
Now the second trap. Every request carries overhead: request and response headers, framing, acknowledgements. It's charged once per request, whatever the payload. So the bytes on the wire are payload plus header.

@math heading="Header share" items="share = h/(p + h)@h over p plus h;;p = 1 000 B, h = 200 B@a thousand bytes;;200/1 200 = 1/6 = 16.7%@one sixth"
The header share is h over p plus h. In our example the payload is a thousand bytes and the header is two hundred, so twelve hundred on the wire. The headers are two hundred over twelve hundred, one sixth, about sixteen point seven percent.

@chapter The crossover
@math heading="When are headers half the traffic?" items="h/(p + h) ≥ 1/2@at least a half;;2h ≥ p + h@multiply through;;h ≥ p@so"
When are the headers at least half of what's on the wire? Start from h over p plus h is at least a half. Both are positive, so multiply through by two times p plus h. That gives two h is at least p plus h. So h is at least p. Every step reverses, so it's an exact equivalence.

@art crossover-point
So the crossover payload is the header size itself. With two hundred bytes of headers, a two hundred byte payload is exactly half overhead, and anything smaller is mostly overhead.

@math heading="Same headers, three shares" items="p = 1 000 B:  1/6@a kilobyte;;p = 200 B:  1/2@two hundred bytes;;p = 50 B:  4/5@fifty bytes"
At a kilobyte payload, the headers are one sixth. At two hundred bytes, one half. At fifty bytes, four fifths. Same headers, three very different percentages.

@chapter Why the fixed cost matters
@art fixed-toll
Two hundred bytes is nothing on its own. But it's a fixed toll on every single request, and its share of the traffic is set by the payload, not by anything about the link.

@art split-requests
That's why add ten percent for overhead is wrong. Overhead isn't a percentage of the payload. Split each kilobyte request into five two hundred byte ones, and the traffic rises, because the header is now charged five times instead of once. Count the per operation cost, and control the number of operations.

@chapter Where people slip
@list heading="Common slips" items="Dividing bytes by a million@The first|Mixing 1024 and 1000@The second|A flat percentage for overhead@The third"
The first slip is dividing bytes by a million and calling it megabits. The second is mixing ten twenty four based and decimal units in one chain. Pick one base, state it at the top, and convert at the boundary. The third is adding a flat percentage for overhead instead of adding it per request.

@chapter Try it
@words text="5 000 req/s · 300 B payload · 200 B headers" sub="bytes per request: 500"
Your turn. Five thousand requests a second, three hundred byte payloads, two hundred bytes of headers. That's five hundred bytes per request. Work out the link rate in megabits, the header share as a fraction, and the payload where headers would be half. Say the share before you check it.

@end text="Count the header per request"
You can drag the payload past the header size and watch the share cross a half, on Learn. That's learn dot get er done dot I O.
