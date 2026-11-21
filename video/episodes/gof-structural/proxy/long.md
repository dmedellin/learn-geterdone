---
format: long
lesson: gof-structural/proxy
title: Proxy: a stand-in that controls who reaches the real object
thumb: Load it when it's asked for
---

@chapter A placeholder
@title text="Proxy" sub="Design Patterns, chapter 4" art=thumb
Some objects are expensive to create, far away, or not for everyone. Proxy puts a stand in in front of them. By the end you'll know its four kinds, and how to count what one actually saves.

@quote text="Provide a surrogate or placeholder for another object to control access to it." cite="Gamma, Helm, Johnson and Vlissides, Design Patterns, Chapter 4"
That's the intent. Provide a surrogate or placeholder for another object to control access to it. Its other name is Surrogate.

@art image-placeholder
The book's example is a document editor whose documents embed large, slow images. Opening a document should be quick, and most images aren't on screen anyway. So the document holds an image proxy. It acts like the image, creates the real one when it's first asked to draw, and forwards every request after that.

@words text="It keeps the file name and the size"
It even keeps a little information, the file name and the image's size, so the layout can ask how big the image is without loading it.

@chapter Four kinds
@list heading="Kinds of proxy" items="Remote@a remote proxy|Virtual@a virtual proxy|Protection@a protection proxy|Smart reference@a smart reference"
The applicability section is really a list of kinds. A remote proxy stands in for an object in another address space. A virtual proxy creates costly objects on demand. A protection proxy controls access, when callers are allowed different things. And a smart reference does extra work whenever the object is reached, like counting references so it can be freed.

@art copy-on-write
They all follow from one fact: a proxy adds a level of indirection. And the authors add one more use it can hide: copy on write. Copying a large object is put off until someone actually modifies the copy. If nobody does, the copy is never paid for.

@chapter The code
@code block=1 lines=1-17 label=Java focus="1-3@the subject|8@null until|12-14@the costly step|15@forwards"
Here's the lesson's library archive. The subject is a scan, which gives you a page. The virtual proxy holds the real scan, null until it's first needed. On the first request, it does the costly step, loading from the store. Every request after that, it just forwards.

@code block=2 lines=10-15 label=Java focus="11-13@it refuses|14@otherwise"
And a protection proxy has the same interface, and a check. If the reader's rights don't allow this item, it refuses. Otherwise, it forwards to the scan inside.

@chapter Count it
@art eager-shelf
The archive has six scans, each with a loading cost: the map three hundred, letters a hundred and twenty, the ledger eighty, the diary a hundred and fifty, the atlas four hundred, the census two fifty. Load every scan at the start, and that's six creations and thirteen hundred, though nobody asks for the census.

@math heading="Seven requests behind virtual proxies" items="letters 120 · map 300 · diary 150@letters first;;atlas 400 · ledger 80 · letters reused twice@reused;;120 + 300 + 150 + 400 + 80 = 1050@ten fifty"
Now behind virtual proxies. Seven requests come in. Letters first, then the map, the diary, the atlas and the ledger, each loaded once. Letters is asked for twice more, and reused. That's five creations, ten fifty in all, and nothing at the start. Load afresh every time instead, and it's twelve ninety.

@art lazy-load
So the proxy saved two hundred and fifty over eager loading, because one scan of six is never read. But if every scan were read early, it would save nothing, and add a check to every call. It pays where many subjects are costly and few are used.

@art guard
Now put a protection proxy in front of each. The guest has no rights, so the guest's request for the atlas is refused. And nobody else asks for the atlas, so it's never loaded. Four creations, six hundred and fifty in all.

@chapter Where people slip
@list heading="Common slips" items="Thinking a proxy always saves work@The first|Treating every proxy as lazy loading@The second|Changing the interface@And the third"
The first slip is thinking a proxy always saves work. The second is treating every proxy as a lazy loader, when virtual is just one of four kinds. And the third is giving the proxy a different interface. A proxy offers the subject's own interface. A class that changes it is an adapter.

@art four-ways
So before you count anything, name the kind. Say what the proxy controls: where the subject lives, when it's created, who may reach it, or what happens on each access. The structure is the same. The purpose differs.

@chapter Try it
@words text="A different morning" sub="census · letters · census · atlas · diary"
Your turn. Five requests: the census, letters, the census again, the atlas and the diary, with no rights checked. Give the creations and the cost in all under eager loading, behind virtual proxies, and loading afresh each time.

@end text="Count the creations"
Then type the requests into the lab and switch schemes to check, on Learn. That's learn dot get er done dot I O.
