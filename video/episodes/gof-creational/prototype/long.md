---
format: long
lesson: gof-creational/prototype
title: Prototype: copy a sample, and decide what the copy shares
thumb: What does the clone share?
---

@chapter Copy, don't name
@title text="Prototype" sub="Design Patterns, Chapter 3" art=thumb
Prototype makes new objects by asking a sample instance to copy itself. That removes the factory classes, and brings what the authors call the pattern's hardest part: implementing the copy correctly.

@quote text="Specify the kinds of objects to create using a prototypical instance, and create new objects by copying this prototype." cite="Gamma, Helm, Johnson and Vlissides, Design Patterns, Chapter 3"
Here's the intent. Specify the kinds of objects to create using a prototypical instance, and create new objects by copying this prototype.

@art palette-tools
The book's example is a music score editor built on a general framework for graphical editors. The framework's tool class creates a graphic and adds it to the document, but it can't know the application's note classes. So each palette tool is an instance of the one tool class, given a different prototype graphic to clone.

@words text="Whole note, half note: instances, not classes"
And the authors go further. Whole notes and half notes needn't be classes at all. They can be instances of one note class, with different images and durations, each installed as a prototype.

@chapter When and who
@art state-combinations
That's the idea in a picture: one class, a few samples that differ only in their values, each ready to be copied.

@list heading="Use it when" items="Classes are known only at run time@only at run time|No factory classes shadowing products@shadowing|A few combinations of state@a few combinations"
Prototype applies when the classes to create are known only at run time, loaded dynamically for instance. When you want no factory classes shadowing the product classes one for one. Or when instances come in only a few combinations of state, so one prototype per combination is simpler.

@list heading="Consequences" items="Add products at run time@while the program runs|New kinds by value@by values|New objects by structure@by structure|Less subclassing@subclassing is reduced|Liability: every class must clone@liability"
The authors list consequences of its own. Products can be added while the program runs, by registering a prototype. New kinds can be specified by values, or by structure, like a subcircuit offered on a palette. Subclassing is reduced. The main liability is that every prototype class must implement cloning, which is hard for existing classes, or ones with cycles.

@chapter What a clone shares
@quote text="Cloning forces you to decide what if anything will be shared." cite="Gamma, Helm, Johnson and Vlissides, Design Patterns, Chapter 3"
And here's the sentence that closes their discussion of copying. Cloning forces you to decide what if anything will be shared.

@art shallow-deep
A shallow copy shares every referenced part between original and clone. It's simple, and often enough. A prototype with structure usually needs a deep copy, where the clone's parts are clones of the prototype's parts. Java's own clone copies fields one for one, a shallow copy.

@code block=1 lines=2-19 focus="4@a part that can change|11-13@shares it|15-17@owns one"
So the lesson's playlist writes both copies out. Its track list is a part that can change. The shallow copy passes the same list along, so it shares it. The deep copy makes a new list, so the clone owns one.

@art prototype-manager
The first implementation issue is where the samples live.

@code block=2 lines=2-15 focus="5-7@register|9-14@create"
The prototype manager is a store keyed by name. Clients register and unregister templates while the program runs, and create a playlist by name, as a deep copy of its template. And since a uniform clone can't take arguments, clients reset state after cloning.

@chapter Who sees the change?
@art runners-template
Now the lab. A template playlist, a workout mix, is the prototype, and three runners, Ana, Ben and Cy, clone it. Then Ben adds a track through his copy.

@math heading="Shallow clones" items="4 holders of one list@four holders;;4 see the change@four that see;;3 surprised: template, Ana, Cy@three surprised"
With shallow copies, the template and all three clones hold the one list. So the lab counts four holders, four that see the change, and three surprised: the template, Ana and Cy, who saw a change they didn't make. And because the template is surprised, every later clone starts with Ben's track.

@math heading="Deep, then immutable" items="deep: 1 sees it, 0 surprised@each copy has its own;;shallow, immutable: 1 sees it, 1 new value@an immutable one"
With deep clones, each copy has its own list. Ben's change reaches one holder, himself, and nobody is surprised, at the price of a list copied for every clone. Share one list again, but an immutable one, and Ben's change gives him a new list. One sees it, none are surprised, and one new value is made.

@art immutable-share
So a shallow copy is safe for any part that can't change. That's why the decision is made part by part.

@chapter Where people slip
@list heading="Common slips" items="Assuming a copy is independent@The first|Deep-copying everything@The second|Passing values through clone@And the third"
The first slip is assuming a copy is independent of its prototype. The second is deep copying everything to be safe, which is wrong for parts meant to be shared. And the third is passing initial values through the clone operation, instead of resetting state afterwards.

@chapter Try it
@words text="A quiz template" sub="q1, q2, q4 shallow · q3 deep · reword through q2"
Your turn. A quiz app clones a multiple choice template for four questions. Three clones are shallow, and one is deep. Through q two, an option is reworded. For a mutable list, then an immutable one, count the holders, who sees the change, who's surprised, and the new values made.

@end text="Count who sees the change"
Then check it in the lab, on Learn. That's learn dot get er done dot I O.
