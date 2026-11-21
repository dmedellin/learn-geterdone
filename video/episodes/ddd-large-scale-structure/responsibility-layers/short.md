---
format: short
lesson: ddd-large-scale-structure/responsibility-layers
title: Five layers Evans keeps finding in business software
---

@art layer-stack
Most business software has the same five layers hiding in its domain.

@list items="Potential: what could we do?@could do|Operations: what are we doing?@doing|Decision Support: what should we do?@should do|Policy and Commitment@rules"
Potential: what the business could do. Operations: what it's doing. Decision Support: what it should do. And Policy and Commitment, the rules and the promises.

@words text="Depend only downward"
Each layer may use the ones below, and nothing above. Keep it to four or five.

@end text="Full lesson on Learn"
Find the upward dependencies in the full lesson on Learn.
