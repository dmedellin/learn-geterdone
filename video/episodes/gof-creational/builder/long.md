---
format: long
lesson: gof-creational/builder
title: Builder: one construction process, many representations
thumb: The director knows the steps
---

@chapter One reader, many formats
@title text="Builder" sub="Design Patterns, Chapter 3" art=thumb
Builder is the second creational pattern. It splits the code that knows how a complex object is put together from the code that decides what each part becomes.

@quote text="Separate the construction of a complex object from its representation so that the same construction process can create different representations." cite="Gamma, Helm, Johnson and Vlissides, Design Patterns, Chapter 3"
Here's its intent. Separate the construction of a complex object from its representation so that the same construction process can create different representations.

@art rtf-converters
The book's example is a reader for R T F, the Rich Text Format, which must convert documents into an open ended number of formats: plain text, TeX, an editable text widget. The answer is to give the reader a converter. As it parses, it hands each token to the converter, and each converter decides what that token becomes. The plain text one ignores all but plain text.

@words text="Converters are builders · the reader is the director"
In the pattern's terms, the converters are builders, and the reader is the director. And the parsing is written once, for every output there will ever be.

@chapter The roles
@list heading="Participants" items="Builder: an operation per part@the builder|ConcreteBuilder: its own representation@each concrete builder|Director: drives the builder@the director|Product@and the product"
The participants are the builder, an interface with an operation per part. Each concrete builder, which assembles its own representation and offers a way to retrieve it. The director, which constructs through the builder interface. And the product.

@art director-builder-client
The collaboration is a short script. The client makes a director and gives it the builder it wants. The director calls the builder whenever a part should be built. And the client takes the finished product from the builder, not from the director.

@chapter A recipe book
@code block=1 lines=2-17 focus="2-6@every part|9@shopping list|13-15@only ingredients|17@result"
Here's the lesson's recipe builder. It has an operation for every part a recipe can have, and the defaults do nothing. The shopping list builder overrides only ingredients, and keeps them. And it hands back its result when asked.

@code block=2 lines=2-14 focus="5-6@a title|7-9@an ingredient|10-11@a step"
And here's the director. It knows the markup, and nothing of what's built from it. A line starting with a hash is a title. A line starting with a dash is an ingredient. Anything else is a step.

@chapter Consequences
@list heading="Three consequences" items="The representation can vary@can vary|Construction and representation apart@separate code|Finer control over construction@finer control"
The authors give three consequences. A product's representation can vary, because the director sees only the abstract builder. Construction and representation live in separate code, so different directors can reuse the same builders. And construction is under finer control, made a step at a time and collected only when it's finished.

@art part-by-part
That third one is what sets Builder apart. Its interface follows the construction process more closely than the other creational patterns do.

@art sgml-reuse
The book imagines a reader for S G M L driving the very converters written for R T F. That's the second consequence: a new director reuses every builder already written.

@words text="Empty defaults · no common product class" sub="Abstract Factory returns at once; Builder at the end"
Two implementation points. Build operations are left empty, so a builder overrides only the parts it cares about. And products often get no common class, because plain text and a widget have little to share. Abstract Factory returns each product at once, while Builder assembles one and returns it at the end.

@chapter Count it
@art sources-outputs
The lab's recipe app reads from three sources, a markup file, a web form and a scanned card, and makes four outputs: a printed page, a shopping list, a spoken walkthrough and an index card.

@math heading="3 sources × 4 outputs" items="pairings: 3 × 4 = 12 → 13 classes@three times four;;split: (3 + 1) + (4 + 1) = 9@three plus one;;13/9 ≈ 1.4×@thirteen ninths"
As one class per pairing, that's three times four, twelve, and thirteen with the base. Split into directors and builders, it's three plus one, plus four plus one: nine. That's thirteen ninths, about one point four times.

@art pairings-vs-split
One design grows by a product, the other by a sum.

@math heading="Growth, and the counterweight" items="nutrition card: 13 → 16 vs 9 → 10@a nutrition card;;website import: 13 → 17 vs 9 → 10@a website;;one source: 5 vs 7@a single markup reader"
Add a nutrition card: three classes as pairings, one as a builder. Add a website import: four pairings, against one new director. But here's the fair counterweight. With a single markup reader, pairings take five classes and the split takes seven. When only one side varies, the split adds classes.

@chapter Where people slip
@list heading="Common slips" items="The process inside the builder@The first|Every builder implements every part@The second|Asking the director for the result@And the third"
The first slip is putting the construction process inside the builder, which repeats the parsing for every output. The second is expecting every builder to implement every part. And the third is asking the director for the result. The client chose the builder, so it asks the builder.

@chapter Try it
@words text="A quiz exporter" sub="sources: sheet, editor · outputs: web-page, print-sheet, answer-key"
Your turn. A quiz app reads quizzes from a sheet and an editor, and builds a web page, a print sheet and an answer key. Next term it adds audio. Count the combinations, the classes in each design, and what audio adds to each.

@end text="Directors and builders"
Then check it in the lab, on Learn. That's learn dot get er done dot I O.
