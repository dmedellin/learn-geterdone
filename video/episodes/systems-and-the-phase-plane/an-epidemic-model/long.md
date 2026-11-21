---
format: long
lesson: systems-and-the-phase-plane/an-epidemic-model
title: The SIR epidemic model: threshold, peak, and why it ends
thumb: It ends before everyone's ill
---

@chapter The question
@title text="An Epidemic Model" sub="Systems and the Phase Plane" art=thumb
An infection spreads through a population. Does it take off at all? When does it peak? And when it finally dies out, is that because everyone has caught it? The last answer is no, and two equations show why.

@chapter The model
@math heading="SIR, without the recovered" items="S′ = −β·S·I@S prime equals;;I′ = β·S·I − γ·I@I prime equals;;R₀ = β·S₀/γ@R nought"
S is the fraction who can still be infected, and I the fraction infected now. S prime equals minus beta S I, and I prime equals beta S I minus gamma I. Beta is the transmission rate, gamma the recovery rate, and R nought, beta S nought over gamma, is the basic reproduction number at the start.

@art mixing
The assumptions are named. A fixed population, everyone mixing equally, immunity after recovery, and no births or deaths. The recovered need no equation of their own, because nothing depends on them.

@chapter The threshold
@math heading="I′ = I·(β·S − γ)" items="grows while S > γ/β@grow while;;peaks when S = γ/β@peaks;;falls after@falls"
Factor the second equation: I prime is I times beta S minus gamma. So the infected grow while S is above gamma over beta. Since S only ever goes down, I peaks exactly when S reaches gamma over beta, and falls after.

@math heading="β = 1/2,   γ = 1/4,   S₀ = 9/10" items="R₀ = (1/2)(9/10) / (1/4) = 9/5 > 1@nine fifths;;γ/β = (1/4)/(1/2) = 1/2@a half"
Take beta a half, gamma a quarter, and start with nine tenths susceptible and one tenth infected. R nought is a half times nine tenths, over a quarter, which is nine fifths, greater than one. And gamma over beta is a quarter over a half, which is a half.

@art peak-curve
So the outbreak grows at first, and the infected fraction peaks exactly when S falls to a half. After that, each infected person passes it on to fewer than one other before recovering.

@chapter Below the threshold
@words text="γ = 1:   R₀ = 9/20 < 1" sub="I falls from the start"
Now raise the recovery rate to one, with the same beta and start. R nought is nine twentieths, less than one. The peak would be at S equals two, which S never reaches. So I falls at once. Same disease, faster recovery, and it never takes off. That's what the single number R nought is for.

@art below-threshold
And R nought only compares rates at the start. It says whether I grows at first, not how big the peak is. Start with ninety nine hundredths susceptible and R nought is larger, but the peak is still at S equals a half. Its place depends on gamma over beta alone.

@chapter A line of equilibria
@math heading="every (S, 0) is an equilibrium" items="at (9/10, 0):  rows 0 −9/20 and 0 1/5@nine tenths, zero;;Δ = 0,   λ = 0  and  1/5@one fifth"
Both rates have a factor of I, so every point with I equal to zero is an equilibrium. At nine tenths, zero, the Jacobian has rows zero, minus nine twentieths and zero, one fifth. The determinant is zero, and the roots are zero and one fifth.

@art line-of-rest
The equilibria aren't isolated. They form a whole line. And the positive root, one fifth, is the outbreak: a few infected at nine tenths susceptible start to grow.

@chapter Why it ends
@math heading="W = S + I − (γ/β)·ln S" items="W′ = S′ + I′ − (γ/β)·S′/S@W prime;;= −β·S·I + (β·S·I − γ·I) + γ·I = 0@cancel in pairs"
Call W the quantity S plus I minus gamma over beta times the log of S. Differentiate along a solution. W prime is S prime plus I prime, minus gamma over beta times S prime over S. Substitute, and the terms cancel in pairs. W is constant.

@art s-levels-off
Now suppose S went to zero. Then minus gamma over beta times log S would grow without limit, while S and I stay between zero and one. W couldn't stay constant. So S stays above zero. The epidemic ends because the infected run out, not the susceptibles.

@art phase-hump
In the plane with S across and I up, the path only moves left, because S only falls. It rises while S is above a half, peaks right at a half, and comes back down to the line of equilibria, landing with S still above zero.

@chapter Where people slip
@list heading="Common slips" items="It ends because everyone was infected@The first|R₀ > 1 describes the whole outbreak@The second|Expecting a single equilibrium@And the third"
The first slip is believing an epidemic ends because everyone has been infected. The second is reading R nought above one as a statement about the whole outbreak. And the third is expecting a single equilibrium. There's a whole line of them, and the Jacobian's zero determinant is why the peak is found from the equations instead.

@chapter Try it
@words text="β = 1/2,   γ = 1/4,   S₀ = 9/10" sub="R₀ and the peak"
Your turn. Read beta and gamma off the equations, compute R nought from the start, and compare it with one. Then find where I peaks, and say in a sentence why the outbreak ends.

@end text="Run the outbreak yourself"
You can change the rates and watch the outbreak rise, peak and end on Learn. That's learn dot get er done dot I O.
