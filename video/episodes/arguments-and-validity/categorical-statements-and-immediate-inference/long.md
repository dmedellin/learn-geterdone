---
format: long
lesson: arguments-and-validity/categorical-statements-and-immediate-inference
title: All, No, Some: reading categorical statements as regions
thumb: Empty or occupied?
---

@chapter Four forms
@title text="Categorical Statements and Immediate Inference" sub="Arguments and Validity" art=thumb
All squares are rectangles. Does it follow that all rectangles are squares? Of course not. But there's a method that shows you why, and it works for every one-step inference of this kind.

@list heading="Four forms" items="A: All S are P@All S are P|E: No S are P@No S are P|I: Some S are P@Some S are P|O: Some S are not P@Some S are not P"
A categorical statement relates two terms, a subject S and a predicate P, in one of four forms. A: All S are P. E: No S are P. I: Some S are P. And O: Some S are not P.

@chapter Regions
@art two-circles
Draw one circle for the S things and one for the P things. They make four regions: S only, both, P only, and neither. Every categorical statement says something about whether a region is empty or occupied.

@math heading="What each claims" items="All S are P:  S outside P is empty@All S are P empties;;No S are P:  S inside P is empty@No S are P empties;;Some S are P:  S inside P is occupied@Some S are P occupies;;Some S are not P:  S outside P is occupied@Some S are not P occupies"
All S are P empties the part of S outside P. No S are P empties the overlap. Some S are P occupies the overlap. And Some S are not P occupies S outside P. So universal statements remove, and particular statements require.

@art blank-region
This is the Boolean reading. A universal statement says a region has nothing in it, and doesn't say any other region has anything in it. So all S are P is true if there are no S at all. And a region you haven't marked is open. Blank isn't occupied. It's permission.

@chapter The test
@art overlap-shaded
An immediate inference has one premise, and the test is the same as for any argument. With two terms, there are four regions, each empty or occupied, so sixteen patterns. A premise that fixes one region leaves the other three open, so eight patterns survive it. If the conclusion fails in any of those, that pattern is the counterexample. If it fails in none, the inference is valid.

@chapter Squares and rectangles
@art squares-rectangles
All squares are rectangles empties one region only: squares that aren't rectangles. It says nothing about rectangles that aren't squares, which is where the two by one rectangle lives. Now try converting it: all rectangles are squares. That needs rectangles outside squares to be empty.

@math heading="Convert All squares are rectangles" items="premise: squares outside rectangles empty@The premise empties;;conclusion: rectangles outside squares empty@the conclusion needs;;counterexample: only rectangles outside squares occupied@So the counterexample"
The premise empties squares outside rectangles. But the conclusion needs rectangles outside squares to be empty, and the premise never mentions that region. So the counterexample is the pattern where only that region is occupied. A premise can force one region without forcing its mirror image.

@chapter Three one-step moves
@art conversion-swap
Conversion swaps subject and predicate. No S are P converts to No P are S, because both empty the single overlap. Some works too, because it occupies that overlap. But All S are P and All P are S empty different regions. And Some S are not P fails the same way, with occupied in place of empty.

@art complement-ring
Contraposition swaps the terms and takes the complement of each, written non P. All S are P becomes all non P are non S, and both empty S outside P. Obversion changes the quality and complements the predicate. All S are P becomes no S are non P. Again, one region emptied.

@list heading="Which moves are valid" items="Conversion: E and I only@Conversion|Contraposition: A and O only@Contraposition|Obversion: all four@Obversion"
So here's the scorecard. Conversion is valid for E and I, and invalid for A and O. Contraposition is valid for A and O, and invalid for E and I. Obversion is valid for all four. And you don't memorise any of it. You read it off which region each statement constrains.

@chapter Where people slip
@list heading="Common slips" items="Converting All S are P@The first|Reading some as some but not all@The second|Taking a blank region as occupied@the third"
The first slip is converting All S are P to All P are S. The second is reading some as some but not all. Some means at least one, and it's compatible with every S being a P. And the third is taking an unshaded region to be occupied. A premise that's silent about a region allows it either way.

@chapter Try it
@words text="Some S are not P" sub="∴ Some P are not S?"
Here's one to try. Does some S are not P let you conclude some P are not S? Mark the region the premise occupies, then ask whether it forces the region the conclusion needs. If it doesn't, describe the counterexample in one sentence.

@end text="Shade the regions yourself"
You can run these inferences and see each counterexample drawn, on Learn. That's learn dot get er done dot I O.
