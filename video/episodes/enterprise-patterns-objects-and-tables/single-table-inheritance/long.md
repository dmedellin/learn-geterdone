---
format: long
lesson: enterprise-patterns-objects-and-tables/single-table-inheritance
title: Single Table Inheritance: a whole class hierarchy in one table
thumb: One table, a type column
---

@chapter Inheritance in tables
@title text="Single Table Inheritance" sub="Patterns of Enterprise Application Architecture, Chapters 3 and 12" art=thumb
Relational databases have no inheritance. So how do you store a hierarchy of classes, like staff, employees, managers and contractors? Fowler says there are basically three ways.

@art three-mappings
One table for every class in the hierarchy is Single Table Inheritance. One table for each class, holding only the fields it declares, is Class Table Inheritance. And one table for each concrete class, holding its inherited fields too, is Concrete Table Inheritance.

@quote text="The trade-offs are all between duplication of data structure and speed of access." cite="Fowler, Patterns of Enterprise Application Architecture, Chapter 3"
How do you choose? In Chapter three's words, the trade offs are all between duplication of data structure and speed of access.

@chapter One table
@art one-table
Single Table Inheritance puts every class in one table. Every row has columns for all the fields of every class, and each row uses only its own class's. So the rest are empty. That's wasted space, though Fowler notes many databases compress it well.

@art big-table-lock
And the one table can grow large, with many indexes and frequent locking, and become a bottleneck. What it buys is a single home for the whole hierarchy. A change has one table to touch, and no load ever needs a join.

@words text="Start with the single table"
Fowler won't name a winner. But he says what he usually does: start with the single table, because it's simple and survives most reshuffling of the classes. Reach for the other two when particular subclasses bring too many columns nobody else uses.

@chapter The type code
@art type-switch
The table needs a column that says which class each row is. A class name takes space and ties the schema to the class names. A code needs translating, and grows with the hierarchy. On load, the code is read first, to choose the class.

@code block=1 lines=1-14 label=Java focus="3@reads the type code|4-5@every person has|6-8@A contractor|9@reads salary once|10-12@a manager|13@plain employee"
Here's a single table load. It reads the type code, then the columns every person has. A contractor adds only a day rate. Everyone else is an employee, so it reads salary once. A manager adds reports as well. Otherwise, it builds a plain employee.

@words text="One namespace for every column"
Two more things from Chapter twelve. A field pushed up or down the hierarchy needs no change to the database. But the columns share one namespace, so two classes can't use one name for different fields.

@chapter The count
@art hierarchy-tree
The lab takes a staff hierarchy. A person, with three fields, not concrete. An employee with two, and a manager under the employee, with two more. And a contractor under person, with two.

@math heading="staff · single, class, concrete" items="tables: 1, 4, 3@the tables;;columns: 11, 13, 20@the columns;;single: key + type + 3 + 2 + 2 + 2 = 11@a key, a type"
Under the three mappings, the tables are one, four and three, and the columns eleven, thirteen and twenty. The single table's eleven are a key, a type, and three plus two plus two plus two, nine field columns.

@math heading="Loading a manager" items="uses 3 + 2 + 2 = 7 fields, 2 of 9 empty@seven fields;;tables touched: 1, 3, 1@touches;;an employee: 4 empty · 1, 2, 1@an employee"
A manager's row uses seven fields, so two of the nine are empty, the contractor's two. Loading a manager touches one table, three joined, or one. Load an employee instead, and four columns are empty, and the load touches one, two, and one.

@art empty-cells
However the hierarchy changes, the single table has one table to read and one to alter. That's the single place Fowler's advantage names. The empty columns are what it costs.

@chapter Where people slip
@list heading="Common slips" items="It's the beginner's mapping@The first|The empty columns waste most of it@The second|The type column keeps itself@And the third"
The first slip is calling it the beginner's mapping. Fowler usually starts with it. The second is thinking the empty columns waste most of the table. Here, two of nine. And the third is forgetting the type column has to be kept, and its translation grows with every new class.

@chapter Try it
@words text="vehicle 4 · car 2 · van 3 · truck 5" sub="load a van"
Your turn. A vehicle has four fields, and car, van and truck, all concrete, add two, three and five. Load a van. Give the single table's columns, the columns empty in a van's row, then the columns and tables of the other two mappings.

@end text="Map a hierarchy yourself"
You can type a class hierarchy and compare all three mappings, on Learn. That's learn dot get er done dot I O.
