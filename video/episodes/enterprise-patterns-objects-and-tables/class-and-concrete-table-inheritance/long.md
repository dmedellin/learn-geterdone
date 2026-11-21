---
format: long
lesson: enterprise-patterns-objects-and-tables/class-and-concrete-table-inheritance
title: Class Table vs Concrete Table Inheritance
thumb: Join to load, or alter everywhere
---

@chapter Opposite trades
@title text="Class and Concrete Table Inheritance" sub="Patterns of Enterprise Application Architecture, Chapter 12" art=thumb
The single table keeps a whole hierarchy in one place. The other two inheritance mappings split it up, and they make opposite trades. One pays when you load. The other pays when you search, or change.

@chapter Class Table Inheritance
@art class-tables
Class Table Inheritance gives every class a table of the fields it declares. No row carries a column it doesn't use, so nothing is wasted. And classes and tables correspond one to one, which makes the mapping easy to follow.

@words text="One shared key, or a key and a foreign key"
The rows of one object can share one key value across the tables. Or each table can have its own key, and a foreign key into the superclass table.

@quote text="You need to touch multiple tables to load an object, which means a join or multiple queries and sewing in memory." cite="Fowler, Patterns of Enterprise Application Architecture, Chapter 12"
But here's the first weakness the pattern lists. You need to touch multiple tables to load an object, which means a join, or multiple queries and sewing in memory.

@code block=1 lines=1-7 label=Java focus="3@names a column from each|5-6@JOIN the three tables"
Here's the query a class table load needs. A manager's name is in person, its salary in employee, and its reports in manager. So the SELECT names a column from each, and they JOIN the three tables on the shared key.

@art join-three
A join across more than three or four tables is slow on most databases. A query for objects of mixed classes doesn't know which tables to join. And the superclass tables, read on every access, can become a bottleneck.

@chapter Concrete Table Inheritance
@art concrete-tables
Concrete Table Inheritance makes the opposite trade. Each concrete class gets one self contained table, with all its fields. So loading an object of a known class reads one table.

@art superclass-change
But superclass fields are duplicated across the tables. A superclass change alters every table that holds the field. A find on the superclass must look in all of them. Keys must be unique across the tables, and the database can't enforce a reference to the abstract class, which has no table.

@chapter The count
@math heading="staff-find-person · single, class, concrete" items="load a manager: 1, 3, 1@loads a manager;;find every person: 1, 4, 3@Finding every person;;add a field to person: 1, 1, 3@Adding a field"
On the last lesson's staff hierarchy, the lab loads a manager. That touches one table, three, or one. Finding every person, subclasses included, reads one, four, three. And adding a field to person alters one, one, three.

@math heading="staff-find-employee" items="load a contractor: 1, 2, 1@Loading a contractor;;find every employee: 1, 3, 2@Finding every employee;;add a field to employee: 1, 1, 2@adding a field to employee"
Now move down the hierarchy. Loading a contractor touches one, two, one. Finding every employee reads one, three, two. And adding a field to employee alters one, one, two.

@art union-find
So the lower the class, the more a class table load joins, and the fewer tables a concrete table change or find touches. Class table pays on every load, and never alters more than one table. Concrete table pays nothing to load a class it knows, and pays in every table below the class it finds or alters.

@words text="Load by name, or search and change?"
Which costs more depends on whether your system mostly loads objects it can name, or mostly searches and changes the hierarchy. The count doesn't know that. You do.

@chapter Inheritance Mappers
@art mapper-chain
Behind all three is Inheritance Mappers. Each domain class has a mapper that handles its own fields, and calls its superclass's mapper for the rest. A mapper for the abstract class works out which concrete mapper should handle a request. Copying the superclass's mapping into every mapper is, in Fowler's phrase, a heinous crime.

@words text="Mix them, at a cost"
And Chapter three reminds you that the three mappings can be mixed in one hierarchy, at the cost of more complexity.

@chapter Where people slip
@list heading="Common slips" items="Concrete table is the fast one@The first|Every load joins every table@The second|Copy the superclass mapping@And the third"
The first slip is choosing concrete table as the fast one. It loads fast, but finds and changes touch every table. The second is expecting every load to join every table. It joins the loaded object's chain. And the third is copying the superclass's mapping into each mapper.

@chapter Try it
@words text="account → saving → isa, bond · account → current" sub="load a bond · find savings · add a field to saving"
Your turn. A bank has accounts, with an abstract saving kind holding isa and bond, and a current account. Load a bond, find every saving account, and add a field to saving. Give the tables each touches, under all three mappings.

@end text="Compare the mappings yourself"
You can type a hierarchy and see what each operation touches, on Learn. That's learn dot get er done dot I O.
