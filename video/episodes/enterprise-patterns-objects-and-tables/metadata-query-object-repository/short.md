---
format: short
lesson: enterprise-patterns-objects-and-tables/metadata-query-object-repository
title: Stop writing the same database finder twice
---

@art twin-finders
Two finders, almost line for line the same. That's a design problem.

@art generator-vs-reflection
Fowler's answer: hold the mapping as data, each column and the field it fills. Then one generic finder reads it, by generated code or by reflection.

@art ninety-percent
But plain metadata covers about ninety percent. Hand code the odd cases left over.

@end text="Full lesson on Learn"
The full lesson, with a lab that finds the repeats, is on Learn.
