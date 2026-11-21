---
format: long
lesson: enterprise-patterns-objects-and-tables/identity-field-and-foreign-keys
title: Identity Field and Foreign Keys: parents first
thumb: Write the parent first
---

@chapter References and keys
@title text="Identity Field and Foreign Keys" sub="Patterns of Enterprise Application Architecture, Chapters 3 and 12" art=thumb
In memory, an order points at its customer. In the database, it can't. How do an object's links survive the trip, and why does the order you write rows in matter?

@quote text="Relational databases handle links by forming a key into another table." cite="Fowler, Patterns of Enterprise Application Architecture, Chapter 3"
Objects hold references, which mean something only in a running program. Rows hold keys. As Chapter three puts it, relational databases handle links by forming a key into another table.

@art reversed-collection
And there's a second problem. Objects hold collections, but a table can't hold a many valued field. So the structure is reversed. An order holds its lines, but in the tables, each line row holds the order's key, and the order row knows nothing of its lines.

@chapter Identity Field
@art reference-vs-key
Fowler's answer to the first problem is to keep each object's key in the object, an Identity Field, and translate between references and keys on every load and save, with the Identity Map as the lookup table.

@art meaningless-key
Which key? A meaningful one, like a national identity number, should be unique and immutable, and human error makes it neither. Mistype it and fix the mistake, and every row that refers to it must change too. So Fowler takes, in his words, a rare stand on the side of meaninglessness.

@chapter Getting a new key
@art key-table
Getting a new key is harder than it sounds. An auto generated field is easiest, until you need the order's key for its lines before the transaction commits. A GUID is long and hard to read. A database sequence is perfect where you have one. Rolling your own, he prefers a separate key table, updated in its own short transaction.

@chapter Foreign keys
@art association-table
Foreign Key Mapping turns a reference into a key, and reverses a collection into keys held by the children. A many to many link has no single valued end, so Association Table Mapping adds a table of key pairs. And Dependent Mapping lets an owner's mapper save children nothing else refers to.

@chapter The order of writes
@words text="Defer the checks to commit, if you can"
Now the order of writes. Where the database can defer its integrity checks to the end of the transaction, Chapter three says there's no reason not to. Then the order doesn't matter. Otherwise, every write is checked, and the updates must go in the right order.

@code block=1 lines=1-9 label=Java focus="3@key table|4@inserts the parent row|7@only then"
Here's a save against a database that checks every statement. It takes the order's key from a key table, inserts the parent row, and only then inserts each line, with the order's key in it. Swap those two inserts, and the first line row would name an order that isn't there yet.

@math heading="order-schema" items="orders → customer · line → orders · line → product · payment → orders@The keys;;insert: customer, orders, payment, product, line@parents first;;delete: line, product, payment, orders, customer@delete order"
The lab sorts the writes. Here are the keys: orders to customer, line to orders, line to product, and payment to orders. With parents first, the insert order is customer, orders, payment, product, line. The delete order is the reverse.

@math heading="As someone happened to list them" items="line, orders, customer, product, payment@as someone listed;;breaks 3: orders before customer@breaks three;;line before orders · line before product@line comes before orders"
Now check an order as someone listed it: line, orders, customer, product, payment. It breaks three keys. Orders comes before customer, and line comes before orders and before product.

@art parents-first
Ties are broken alphabetically, so the insert order is one valid order of several. Product could equally go first. And deferred to commit, none of this would matter.

@chapter Where people slip
@list heading="Common slips" items="A meaningful key saves a column@The first|The tables mirror the objects@The second|Ordering when the database can wait@And the third"
The first slip is using a meaningful key to save a column. The second is expecting the object's structure in the tables. It's reversed. And the third is carefully ordering writes when the database could simply defer its checks.

@chapter Try it
@words text="booking → guest · booking → room" sub="room → hotel · charge → booking"
Your turn. Booking holds keys to guest and room, room to hotel, and charge to booking. Someone proposes hotel, guest, booking, room, charge. Find the keys that breaks, then write a valid insert order and a valid delete order.

@end text="Sort the writes yourself"
You can type a schema's keys and see which orders break them, on Learn. That's learn dot get er done dot I O.
