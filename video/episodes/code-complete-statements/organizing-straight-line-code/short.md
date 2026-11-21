---
format: short
lesson: code-complete-statements/organizing-straight-line-code
title: Four calls, twenty four orders, one right answer
---

@art hidden-object
These four calls compile in every one of their twenty four orders.

@code block=3 lines=1-6 label=Java focus="2-5@load rates"
Load rates, add surcharges, add insurance, print. Each takes nothing and returns nothing, so neither you nor the compiler can see which must come first.

@art parameter-chain
The fix is to pass the data. Have each call return what the next one takes, and the order is written into the code.

@end text="Full lesson on Learn"
The full lesson, with a lab that counts the arrows, is on Learn.
