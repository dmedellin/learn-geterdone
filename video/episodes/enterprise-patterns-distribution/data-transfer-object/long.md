---
format: long
lesson: enterprise-patterns-distribution/data-transfer-object
title: Data Transfer Object: send too much rather than call twice
thumb: One call carries it all
---

@chapter The argument
@title text="Data Transfer Object" sub="Patterns of Enterprise Application Architecture, Chapter 15" art=thumb
A Remote Facade needs coarse methods. So what do those methods take, and return? That's this pattern.

@quote text="Due to the latency costs of remote calls, its better to err on the side of sending too much data than have to make multiple calls." cite="Fowler, Patterns of Enterprise Application Architecture, Chapter 15, How It Works"
Here's the pattern's argument in one line. Due to the latency costs of remote calls, it's better to err on the side of sending too much data than have to make multiple calls.

@chapter The bag of fields
@art bag-of-fields
Each remote call is expensive, so each one has to carry more data. Many parameters might do for an update, awkwardly, but Java returns only one value. So you gather everything the call needs into one serializable object. Fowler admits it's the kind of object you were brought up not to write, a bag of fields and accessors.

@words text="Shaped by the client, not the domain"
What goes in it is decided by the client. It usually carries more than was asked for: data from the order, the customer, the lines and the delivery. Everything the client will want for a while.

@art domain-web
Why not send the domain objects themselves? They're tied into a web of references that's hard to serialize, and you wouldn't want the domain classes on the client. So the fields are primitives, strings, dates, and other transfer objects, in a simple hierarchy.

@code block=1 lines=1-8 label=Java focus="2@implements Serializable|3-7@what the order screen shows"
Here's one, shaped for one screen. It implements Serializable. Its fields hold what the order screen shows: the id, the customer's name, the status, the total, and a summary of each line. No domain behaviour, and nothing refers to a domain class.

@art assembler
And keep the two apart. The transfer object lives on both sides of the wire, so it mustn't depend on the domain. The domain shouldn't depend on it either, because its shape changes with the interface. A separate assembler builds one from the other.

@chapter Count it
@art getter-per-field
The lab compares two designs. One getter call per field the screen needs, or one transfer object carrying every field. The preset adds a four thousand byte notes field the screen doesn't show, as if the assembler copied the whole order.

@math heading="order-screen: 20 ms, 1,000 bytes/ms" items="5 getters: 51,033/500 ≈ 102.07 ms@five getters;;one DTO, 6,066 bytes: 13,033/500 ≈ 26.07 ms@one transfer object;;unneeded: 4,000 bytes@four thousand;;4 saved trips could carry 80,000 bytes@eighty thousand"
At twenty milliseconds and a thousand bytes a millisecond, five getters take about a hundred and two milliseconds. One transfer object of six thousand and sixty six bytes takes about twenty six, though four thousand of its bytes are never shown. The four round trips it saved could have carried eighty thousand bytes, twenty times the waste.

@chapter The encoding
@art encoding-size
Now send the same fields at three times their raw size, the lesson's stand in for a text encoding. That factor is illustrative, not the book's.

@math heading="as-xml: factor 3" items="getters: 53,099/500 ≈ 106.20 ms@getters now;;DTO, 18,198 bytes: 19,099/500 ≈ 38.20 ms@thirty eight"
The getters now take about a hundred and six milliseconds. The transfer object, eighteen thousand one hundred and ninety eight bytes, takes about thirty eight. The encoding costs the transfer object far more, because it sends more bytes, but it's still faster here.

@words text="Binary: compact, fragile · XML: larger, tolerant"
Size isn't the whole trade. Use the platform's own serialization when there is one. A direct binary form is fragile: adding one optional field can break an out of date client. XML can be written to tolerate that, but needs more bandwidth, and can be markedly slower.

@chapter Where people slip
@list heading="Common slips" items="Fetch each value only when asked@The first|A domain object with getters@The second|Choose the encoding by size alone@And the third"
The first slip is fetching each value only when the screen asks. A round trip costs more than most fields. The second is taking a transfer object for a domain object with getters. It has no behaviour, and an assembler builds it. And the third is choosing the encoding by size alone.

@chapter Try it
@art unneeded-bytes
Your turn, and this one tests the advice. A profile screen shows a name of thirty bytes and an email of forty. The server also holds a sixty thousand byte photo and a nine thousand byte history.

@words text="10 ms · 2,000 bytes/ms · factor 1"
At ten milliseconds and two thousand bytes a millisecond, time one getter per field, one transfer object with all four fields, and one with only the two shown. Which is fastest? And why doesn't the quotation settle it?

@end text="Weigh the bytes yourself"
You can weigh extra bytes against saved round trips in the lab, on Learn. That's learn dot get er done dot I O.
