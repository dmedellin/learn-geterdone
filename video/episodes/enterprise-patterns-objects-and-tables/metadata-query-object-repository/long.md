---
format: long
lesson: enterprise-patterns-objects-and-tables/metadata-query-object-repository
title: Metadata Mapping, Query Object and Repository
thumb: The mapping, held as data
---

@chapter The same finder twice
@title text="Metadata Mapping, Query Object and Repository" sub="Patterns of Enterprise Application Architecture, Chapters 3 and 13" art=thumb
You've probably written the same finder twice. Prepare a statement, bind the key, run it, step to the row, make the object, copy each column into a field, return it. Fowler says that's a sign of something.

@quote text="With simple and repetitive mapping this can lead to code that's simple and repetitive—and repetitive code is a sign of something wrong with the design." cite="Fowler, Patterns of Enterprise Application Architecture, Chapter 3"
Of the book's own hand written examples, he says: with simple and repetitive mapping, this can lead to code that's simple and repetitive, and repetitive code is a sign of something wrong with the design.

@art twin-finders
Some of the repetition can be factored out with inheritance and delegation. The more sophisticated answer is to boil the mapping down to metadata, a statement of which column maps to which field, and let code do the rest. That's why commercial mapping tools use metadata.

@chapter The count
@code block=1 lines=1-20 label=Java focus="3-5@lines three to five|13-15@thirteen to fifteen|7-8@field copies|17-18@differ in their names"
Here are two hand written finders. The lab finds one repeated block, six lines in all: lines three to five, and thirteen to fifteen. That's the bind, the execute, and the next. The field copies differ in their names, so they aren't counted. But they repeat in shape.

@words text="The repetition is wider than the count"
And that shape is exactly what the metadata holds. So the repetition the pattern removes is wider than the count of identical lines.

@chapter Metadata Mapping
@code block=2 lines=1-17 label=Java focus="2-3@member map|8-11@prepares, binds and runs|12@by reflection|13-16@copies each mapped column"
Now the mapping is data. The member map pairs each column with the field it fills. One generic find prepares, binds and runs the statement once, makes the object by reflection, and copies each mapped column into its field. The lab finds zero repeated lines. A shop needs only its own map.

@art mapping-pairs
Notice where the knowledge went. Each class now brings a small table of pairs, a column and its field, and its own statement. Everything else is shared, written once, and tested once.

@art generator-vs-reflection
How does metadata become running code? A generator can read it and write mapper classes during the build. Or a reflective program reads field names and sets them as it runs. Fowler usually counsels against reflection, but finds it quite appropriate here. Still, generated code is easier to debug, so he usually prefers it, which, he says, makes him unsophisticated.

@art ninety-percent
Here's the warning. By the pattern's rough guide, plain metadata covers about ninety percent of a mapping, and the odd cases left can make the generic code much harder to follow. For those, write hand coded subclasses that take over. Metadata can also get in the way of refactoring, since a renamed field is still named in the data.

@chapter Query Object
@art query-object
A Query Object builds on the metadata. It's an interpreter of criteria, written in terms of classes and fields, that turns itself into SQL. Its own advice is cautious: most projects with a hand built data source layer do without one. It's really needed only with a Domain Model and a Data Mapper, and serious use needs Metadata Mapping as well.

@chapter Repository
@art repository-collection
Repository, by Edward Hieatt and Rob Mee, sits above the mappers, and looks like a collection of domain objects. The client builds criteria and asks for the matching objects, never for a query to be run. Behind it sit the metadata and a Query Object, and its source need not be a database at all.

@chapter Where people slip
@list heading="Common slips" items="Metadata removes the mapping work@The first|A Repository is a renamed Data Mapper@The second|The duplicate count is the whole repetition@And the third"
The first slip is thinking metadata removes the mapping work. It moves it, into the metadata and the generic code. The second is taking a Repository for a Data Mapper renamed. It sits above the mappers. And the third is trusting the duplicate count as the whole repetition.

@chapter Try it
@code block=3 lines=1-20 label=Java focus="1-10@findInvoice|12-20@findReceipt"
Your turn. Here are two more finders, findInvoice and findReceipt. Mark the lines they repeat exactly. Then write the metadata, the column and field pairs, that the single metadata finder would read for each class.

@end text="Find the repetition yourself"
You can paste two finders into the lab and see what they share, on Learn. That's learn dot get er done dot I O.
