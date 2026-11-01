"""Spoken forms for runs whose notation is ambiguous to read-out.

Keyed by the exact run text; see content/AGENTS.md, "Write math a voice can read".
Each course adds only a block headed with its own title, as
SPOKEN.update({...}) under a "# <Course title>" comment.
"""

SPOKEN = {}

# Accelerate and Measuring Performance
# Worked-example lines are sums, not assignments, so the code reader's "is set
# to" for `=` is replaced by "which is"; the team names T01 and so on are read
# digit by digit; "Ward's" is a name, not a character.
SPOKEN.update({
    "in place: 4 + 1 + 2 + 3 + 4 = 14 of 24":
        "in place, 4 plus 1 plus 2 plus 3 plus 4, which is 14 of 24",
    "level 2: trunk-based development no, so level 2 is not met":
        "level 2, trunk based development no, so level 2 is not met",
    "lead = service time ÷ (1 − utilization)":
        "lead time is the service time divided by the quantity 1 minus utilization",
    "u = 80 percent = 4/5": "u is 80 percent, which is 4 fifths",
    "1 − u = 1/5": "1 minus u is 1 fifth",
    "wait = u/(1 − u) = (4/5)/(1/5) = 4 service times":
        "wait is u over the quantity 1 minus u, which is 4 fifths over 1 fifth, "
        "which is 4 service times",
    "lead time = 2 hours × (1 + 4) = 10 hours":
        "lead time is 2 hours times the quantity 1 plus 4, which is 10 hours",
    "check: 2 hours ÷ (1/5) = 10 hours":
        "check, 2 hours divided by 1 fifth, which is 10 hours",
    "median: (4 + 5) / 2 = 4.5 hours, less than one day":
        "median, the quantity 4 plus 5, over 2, which is 4.5 hours, less than one day",
    "deployments: 10 in 14 days = 5 a week":
        "deployments, 10 in 14 days, which is 5 a week",
    "change fail rate: 1 / 10 = 10 percent, band 0 to 15":
        "change fail rate, 1 in 10, which is 10 percent, band 0 to 15",
    "Ward's method: merge the cheapest pair":
        "Ward's method, merge the cheapest pair",
    "T01 (1, 1, 2, 2) to T03 (1, 1, 2, 1): 0 + 0 + 0 + 1 = 1":
        "T 0 1, with codes 1, 1, 2, 2, to T 0 3, with codes 1, 1, 2, 1, "
        "0 plus 0 plus 0 plus 1, which is 1",
    "T01 to T04 (1, 1, 1, 2): 1 as well, so the tie goes to T03":
        "T 0 1 to T 0 4, with codes 1, 1, 1, 2, 1 as well, so the tie goes to T 0 3",
    "two single teams merge at half: T01 + T03 cost 1/2":
        "two single teams merge at half, T 0 1 and T 0 3 cost 1 half",
    "centre of T01 and T03: (1, 1, 2, 1.5), and T04 is at (1, 1, 1, 2)":
        "centre of T 0 1 and T 0 3, 1, 1, 2, 1.5, and T 0 4 is at 1, 1, 1, 2",
    "squared distance: 0 + 0 + 1 + 0.25 = 1.25":
        "squared distance, 0 plus 0 plus 1 plus 0.25, which is 1.25",
    "T04 joins at (2 · 1 / 3) · 1.25 = 5/6":
        "T 0 4 joins at 2 times 1 over 3, times 1.25, which is 5 sixths",
    "high: 12 of 20 = 60 percent": "high, 12 of 20, which is 60 percent",
    "low: 6 of 20 = 30 percent": "low, 6 of 20, which is 30 percent",
    "ratio: 60 / 30 = 2.00": "ratio, 60 over 30, which is 2.00",
    "difference: 60 - 30 = 30 points": "difference, 60 minus 30, which is 30 points",
    "odds high: 12 to 8 = 3/2": "odds high, 12 to 8, which is 3 halves",
    "odds low: 6 to 14 = 3/7": "odds low, 6 to 14, which is 3 sevenths",
    "odds ratio: (3/2) / (3/7) = 7/2 = 3.50":
        "odds ratio, 3 halves over 3 sevenths, which is 7 halves, which is 3.50",
})


# The Science Behind the Book
# Formula and worked lines are statements of equality, not assignments, so the
# code reader's "is set to" is replaced by "which is" or "equals"; sigma, the
# square root and the subscripted letters are spoken in full.
SPOKEN.update({
    "mean  =  (sum of the values) / n": "mean equals the sum of the values, divided by n",
    "median  =  the middle value, or the mean of the two middle values":
        "median equals the middle value, or the mean of the two middle values",
    "mode  =  the value that appears most often":
        "mode equals the value that appears most often",
    "range  =  largest value − smallest value":
        "range equals the largest value minus the smallest value",
    "population standard deviation  =  √( Σ(x − mean)² / n )":
        "population standard deviation equals the square root of the sum of the squared "
        "distances from the mean, divided by n",
    "sample standard deviation  =  √( Σ(x − mean)² / (n − 1) )":
        "sample standard deviation equals the square root of the sum of the squared "
        "distances from the mean, divided by n minus 1",
    "sum = 1+3+4+5+5+6+6+6+7+7 = 50, n = 10":
        "sum, 1 plus 3 plus 4 plus 5 plus 5 plus 6 plus 6 plus 6 plus 7 plus 7, which is 50, and n is 10",
    "mean = 50 / 10 = 5": "mean, 50 over 10, which is 5",
    "5th and 6th values are 5 and 6: median = 5.5":
        "the 5th and 6th values are 5 and 6, so the median is 5.5",
    "6 appears three times: mode = 6": "6 appears three times, so the mode is 6",
    "range = 7 − 1 = 6": "range, 7 minus 1, which is 6",
    "population: 32 / 10 = 3.2, root ≈ 1.789":
        "population, 32 over 10, which is 3.2, and its root is about 1.789",
    "sample: 32 / 9 ≈ 3.556, root ≈ 1.886":
        "sample, 32 over 9, which is about 3.556, and its root is about 1.886",
    "r  =  Σ(x − mean of x)·(y − mean of y)":
        "r equals the sum, over all rows, of x minus the mean of x, times y minus the mean of y",
    "      ÷ √( Σ(x − mean of x)²  ·  Σ(y − mean of y)² )":
        "divided by the square root of the sum of the squared x distances, "
        "times the sum of the squared y distances",
    "Σx = 246, Σx² = 8550": "the sum of x is 246, the sum of x squared is 8550",
    "Σy = 585, Σy² = 43345": "the sum of y is 585, the sum of y squared is 43345",
    "Σxy = 18732": "the sum of x times y is 18732",
    "top = 8·18732 − 246·585 = 149856 − 143910 = 5946":
        "top, 8 times 18732 minus 246 times 585, which is 149856 minus 143910, which is 5946",
    "x part = 8·8550 − 246² = 68400 − 60516 = 7884":
        "x part, 8 times 8550 minus 246 squared, which is 68400 minus 60516, which is 7884",
    "y part = 8·43345 − 585² = 346760 − 342225 = 4535":
        "y part, 8 times 43345 minus 585 squared, which is 346760 minus 342225, which is 4535",
    "r = 5946 / √(7884·4535) = 5946 / √35753940":
        "r, 5946 over the square root of 7884 times 4535, which is 5946 over the square root of 35753940",
    "√35753940 ≈ 5979.5, so r ≈ 0.994":
        "the square root of 35753940 is about 5979.5, so r is about 0.994",
    "r (all rows)       =  Sxy / √(Sxx · Syy)":
        "r over all rows equals S x y over the square root of S x x times S y y",
    "r (within group g) =  Sxy(g) / √(Sxx(g) · Syy(g))":
        "r within group g equals S x y of g over the square root of S x x of g times S y y of g",
    "r (pooled within)  =  Σg Sxy(g) / √( Σg Sxx(g) · Σg Syy(g) )":
        "pooled within-group r equals the sum over groups of S x y, over the square root of "
        "the sum over groups of S x x, times the sum over groups of S y y",
    "where Sxx = Σ(x − mean of x)², Syy = Σ(y − mean of y)²,":
        "where S x x is the sum of the squared x distances from the mean of x, "
        "and S y y is the same for y,",
    "and Sxy = Σ(x − mean of x)·(y − mean of y)":
        "and S x y is the sum of x minus its mean, times y minus its mean",
    "small: x = 1,2,2,3  y = 1,3,2,2  Sxx = 2  Syy = 2  Sxy = 1":
        "small, x values 1, 2, 2, 3, y values 1, 3, 2, 2, S x x 2, S y y 2, S x y 1",
    "medium: x = 5,6,6,7  y = 4,6,5,5  Sxx = 2  Syy = 2  Sxy = 1":
        "medium, x values 5, 6, 6, 7, y values 4, 6, 5, 5, S x x 2, S y y 2, S x y 1",
    "large: x = 10,11,11,12  y = 11,9,10,10  Sxx = 2  Syy = 2  Sxy = −1":
        "large, x values 10, 11, 11, 12, y values 11, 9, 10, 10, S x x 2, S y y 2, S x y minus 1",
    "totals: Sxx = 6, Syy = 6, Sxy = 1": "totals, S x x 6, S y y 6, S x y 1",
    "pooled r = 1 / √(6·6) = 1/6 ≈ 0.167":
        "pooled r, 1 over the square root of 6 times 6, which is 1 sixth, about 0.167",
    "merge cost(A, B)  =  (nA · nB) / (nA + nB)  ·  Σ over measures of (a − b)²":
        "merge cost of groups A and B equals n A times n B, over n A plus n B, "
        "times the sum over the measures of a minus b, squared",
    "where a and b are the two groups' average codes on each measure":
        "where a and b are the two groups' average codes on each measure",
    "T1 = (6,6,6,6), T5 = (6,6,5,6): squared distance 1":
        "T 1 has codes 6, 6, 6, 6 and T 5 has 6, 6, 5, 6, squared distance 1",
    "cost = (1·1/2)·1 = 1/2": "cost, 1 times 1 over 2, times 1, which is 1 half",
    "T6 = (5,6,5,5) against the average of T1, T5 = (6,6,5.5,6)":
        "T 6 has 5, 6, 5, 5, against the average of T 1 and T 5, which is 6, 6, 5.5, 6",
    "squared distance 1+0+0.25+1 = 2.25; cost = (1·2/3)·2.25 = 3/2":
        "squared distance, 1 plus 0 plus 0.25 plus 1, which is 2.25, and cost, 1 times 2 over 3, "
        "times 2.25, which is 3 halves",
    "{T1,T5,T6} average (17/3, 6, 16/3, 17/3); {T3,T4,T9} (4, 10/3, 13/3, 11/3)":
        "the average of T 1, T 5 and T 6 is 17 thirds, 6, 16 thirds, 17 thirds, "
        "and of T 3, T 4 and T 9 is 4, 10 thirds, 13 thirds, 11 thirds",
    "squared distance 25/9+64/9+1+4 = 134/9":
        "squared distance, 25 ninths plus 64 ninths plus 1 plus 4, which is 134 ninths",
    "cost = (3·3/6)·(134/9) = 67/3":
        "cost, 3 times 3 over 6, times 134 ninths, which is 67 thirds",
    "reverse the third: 8 − 1 = 7": "reverse the third, 8 minus 1, which is 7",
    "R1 scored 5, 4, 7, 5: sum 21, mean 21/4 = 5.25":
        "R 1 scored 5, 4, 7, 5, sum 21, mean 21 quarters, which is 5.25",
    "R2 20/4, R3 17/4, R4 10/4, R5 26/4, R6 13/4":
        "R 2 is 20 quarters, R 3 is 17 quarters, R 4 is 10 quarters, R 5 is 26 quarters, R 6 is 13 quarters",
    "sum of the six quarters: 21+20+17+10+26+13 = 107":
        "sum of the six quarters, 21 plus 20 plus 17 plus 10 plus 26 plus 13, which is 107",
    "construct mean = 107/24 ≈ 4.458": "construct mean, 107 over 24, which is about 4.458",
    "first construct: (0.72 + 0.68 + 0.64) / 3 = 2.04 / 3 = 0.68":
        "first construct, 0.72 plus 0.68 plus 0.64, over 3, which is 2.04 over 3, which is 0.68",
    "second construct: (0.70 + 0.20 + 0.24) / 3 = 1.14 / 3 = 0.38":
        "second construct, 0.70 plus 0.20 plus 0.24, over 3, which is 1.14 over 3, which is 0.38",
    "cross pairs: 0.95 + 0.85 + 0.90 = 2.70, over 9 = 0.3":
        "cross pairs, 0.95 plus 0.85 plus 0.90, which is 2.70, over 9, which is 0.3",
    "B3 with its own: (0.20 + 0.24) / 2 = 0.22":
        "B 3 with its own construct, 0.20 plus 0.24, over 2, which is 0.22",
    "B3 with the first construct: (0.55 + 0.50 + 0.52) / 3 = 1.57 / 3 ≈ 0.523":
        "B 3 with the first construct, 0.55 plus 0.50 plus 0.52, over 3, which is 1.57 over 3, "
        "about 0.523",
    "0.523 > 0.22: B3 is listed": "0.523 is more than 0.22, so B 3 is listed",
    "α  =  k / (k − 1)  ·  ( 1 − Σ σᵢ² / σₜ² )":
        "alpha equals k over k minus 1, times the quantity 1 minus the sum of the item variances "
        "over the variance of the total",
    "k = number of items, σᵢ² = variance of item i,":
        "k is the number of items, and sigma i squared is the variance of item i,",
    "σₜ² = variance of the total score, the sum of the items":
        "and sigma t squared is the variance of the total score, the sum of the items",
    "signal 1: 8·139 − 31² = 1112 − 961 = 151":
        "signal 1, 8 times 139 minus 31 squared, which is 1112 minus 961, which is 151",
    "signal 2: 8·130 − 30² = 1040 − 900 = 140":
        "signal 2, 8 times 130 minus 30 squared, which is 1040 minus 900, which is 140",
    "signal 3: 8·117 − 29² = 936 − 841 = 95":
        "signal 3, 8 times 117 minus 29 squared, which is 936 minus 841, which is 95",
    "signal 4: 8·142 − 32² = 1136 − 1024 = 112":
        "signal 4, 8 times 142 minus 32 squared, which is 1136 minus 1024, which is 112",
    "sum of the four = 498": "sum of the four, which is 498",
    "day totals 4 15 12 17 15 19 19 21: Σ = 122, Σ² = 2062":
        "day totals 4, 15, 12, 17, 15, 19, 19, 21, sum 122, sum of squares 2062",
    "totals: 8·2062 − 122² = 16496 − 14884 = 1612":
        "totals, 8 times 2062 minus 122 squared, which is 16496 minus 14884, which is 1612",
    "α = (4/3)·(1 − 498/1612) = (4/3)·(1114/1612)":
        "alpha, 4 thirds times the quantity 1 minus 498 over 1612, which is 4 thirds times 1114 over 1612",
    "α = 1114/1209 ≈ 0.921": "alpha, 1114 over 1209, which is about 0.921",
    "distances from 5: −4 −2 −1 0 0 1 1 1 2 2":
        "distances from 5, minus 4, minus 2, minus 1, 0, 0, 1, 1, 1, 2, 2",
    "squares: 16 4 1 0 0 1 1 1 4 4, sum = 32":
        "squares, 16, 4, 1, 0, 0, 1, 1, 1, 4, 4, sum 32",
    "R1 answers 5, 4, 1, 5": "R 1 answers 5, 4, 1, 5",
})


# Surveys, Data and Statistical Methods
# Formula and worked lines are statements of equality, so the code reader's
# "is set to" becomes "equals"; Sxy, Sxx, Syy, AVE and CR are spelt out; a
# dash in a record of referrals is a dash, not a minus.
SPOKEN.update({
    "median = (26 + 48) / 2 = 37":
        "median equals, open bracket, 26 plus 48, close bracket, divided by 2 equals 37",
    "2 / 10 = 20 percent":
        "2 divided by 10 equals 20 percent",
    "r1: 6 5 6 and 8 − 2 = 6, sum 23, mean 5.75":
        "r 1, 6 5 6 and 8 minus 2 equals 6, sum 23, mean 5.75",
    "r2: 5 5 6 and 8 − 3 = 5, sum 21, mean 5.25":
        "r 2, 5 5 6 and 8 minus 3 equals 5, sum 21, mean 5.25",
    "r3: 4 5 4 and 8 − 4 = 4, sum 17, mean 4.25":
        "r 3, 4 5 4 and 8 minus 4 equals 4, sum 17, mean 4.25",
    "r4: 6 6 5 and 8 − 2 = 6, sum 23, mean 5.75":
        "r 4, 6 6 5 and 8 minus 2 equals 6, sum 23, mean 5.75",
    "r5: 3 4 3 and 8 − 5 = 3, sum 13, mean 3.25":
        "r 5, 3 4 3 and 8 minus 5 equals 3, sum 13, mean 3.25",
    "r6: 7 7 7 and 8 − 7 = 1, sum 22, mean 5.5":
        "r 6, 7 7 7 and 8 minus 7 equals 1, sum 22, mean 5.5",
    "five without r6: 24.25 / 5 = 4.85":
        "five without r 6, 24.25 divided by 5 equals 4.85",
    "six with r6: 29.75 / 6 = 4.958":
        "six with r 6, 29.75 divided by 6 equals 4.958",
    "shift: (5.5 − 4.85) / 6 = 0.108":
        "shift, open bracket, 5.5 minus 4.85, close bracket, divided by 6 equals 0.108",
    "a, -, east; b, -, west; c, a, east; d, a, east; e, b, west; f, c, east; g, c, east; h, e, west":
        "a, dash, east, b, dash, west, c, a, east, d, a, east, e, b, west, f, c, east, g, c, east, h, e, west",
    "ana's tree: 1 + 3 + 3 + 1 = 8, 8 / 20 = 40 percent":
        "ana's tree, 1 plus 3 plus 3 plus 1 equals 8, 8 divided by 20 equals 40 percent",
    "bo's tree: 1 + 2 + 4 + 2 = 9, 9 / 20 = 45 percent":
        "bo's tree, 1 plus 2 plus 4 plus 2 equals 9, 9 divided by 20 equals 45 percent",
    "cy: ida, then quin; tree 1 + 1 + 1 = 3, 15 percent":
        "cy, ida, then quin, tree 1 plus 1 plus 1 equals 3, 15 percent",
    "drop cy: 20 − 3 = 17; bank 9 / 17 = 52.9 percent":
        "drop cy, 20 minus 3 equals 17, bank 9 divided by 17 equals 52.9 percent",
    "E = (row total · column total) / N":
        "E equals, open bracket, row total times column total, close bracket, divided by N",
    "χ² = sum over the cells of (O − E)² / E":
        "chi squared equals the sum over the cells of the quantity O minus E, squared, divided by E",
    "degrees of freedom = (rows − 1) · (columns − 1)":
        "degrees of freedom equals, open bracket, rows minus 1, close bracket, times, open bracket, columns minus 1, close bracket",
    "row totals: small 30, medium 50, large 20; N = 100":
        "row totals, small 30, medium 50, large 20, N equals 100",
    "expected small: 30 · 60 / 100 = 18 early, 12 late":
        "expected small, 30 times 60 divided by 100 equals 18 early, 12 late",
    "small early: gap 6, 6 squared = 36, 36 / 18 = 2":
        "small early, gap 6, 6 squared equals 36, 36 divided by 18 equals 2",
    "small late: gap 6, 36 / 12 = 3":
        "small late, gap 6, 36 divided by 12 equals 3",
    "large early: gap 6, 36 / 12 = 3":
        "large early, gap 6, 36 divided by 12 equals 3",
    "large late: gap 6, 36 / 8 = 4.5":
        "large late, gap 6, 36 divided by 8 equals 4.5",
    "sum 2 + 3 + 0 + 0 + 3 + 4.5 = 12.5; 12.5 > 5.991":
        "sum 2 plus 3 plus 0 plus 0 plus 3 plus 4.5 equals 12.5, 12.5 is greater than 5.991",
    "AVE = (λ₁² + λ₂² + … + λₖ²) / k":
        "A V E equals, open bracket, lambda sub 1 squared plus lambda sub 2 squared plus and so on plus lambda sub k squared, close bracket, divided by k",
    "CR = (Σλ)² / ((Σλ)² + Σ(1 − λ²))":
        "C R equals, open bracket, the sum of lambda, close bracket, squared divided by, open bracket, open bracket, the sum of lambda, close bracket, squared plus the sum of, open bracket, 1 minus lambda squared, close bracket, close bracket",
    "AVE = 2.415 / 4 = 0.60375":
        "A V E equals 2.415 divided by 4 equals 0.60375",
    "root: 0.777 · 0.777 = 0.6037, so root = 0.777":
        "root, 0.777 times 0.777 equals 0.6037, so root equals 0.777",
    "errors: 4 − 2.415 = 1.585":
        "errors, 4 minus 2.415 equals 1.585",
    "CR = 9.61 / (9.61 + 1.585) = 9.61 / 11.195 = 0.858":
        "C R equals 9.61 divided by, open bracket, 9.61 plus 1.585, close bracket, equals 9.61 divided by 11.195 equals 0.858",
    "r = Sxy / √(Sxx · Syy)":
        "r equals S x y divided by the square root of, open bracket, S x x times S y y, close bracket",
    "Sxy = sum of (x − mean x) · (y − mean y)":
        "S x y equals sum of x minus mean x times, open bracket, y minus mean y, close bracket",
    "Sxx = sum of (x − mean x)², Syy = sum of (y − mean y)²":
        "S x x equals sum of x minus mean x squared, S y y equals sum of y minus mean y squared",
    "means: x = 15 / 5 = 3, y = 20 / 5 = 4":
        "means, x equals 15 divided by 5 equals 3, y equals 20 divided by 5 equals 4",
    "Sxx = 4 + 1 + 0 + 1 + 4 = 10":
        "S x x equals 4 plus 1 plus 0 plus 1 plus 4 equals 10",
    "Syy = 4 + 0 + 1 + 4 + 1 = 10":
        "S y y equals 4 plus 0 plus 1 plus 4 plus 1 equals 10",
    "Sxy = 4 + 0 + 0 + 2 + 2 = 8":
        "S x y equals 4 plus 0 plus 0 plus 2 plus 2 equals 8",
    "slope = 8 / 10 = 0.8; intercept = 4 − 0.8 · 3 = 1.6":
        "slope equals 8 divided by 10 equals 0.8, intercept equals 4 minus 0.8 times 3 equals 1.6",
    "r squared = 0.64; line accounts for 0.8 · 8 = 6.4 of 10":
        "r squared equals 0.64, line accounts for 0.8 times 8 equals 6.4 of 10",
    "the line: slope is Sxy over Sxx":
        "the line, slope is S x y over S x x",
    "root test: √AVE must exceed the absolute value of r":
        "root test, the square root of A V E must exceed the absolute value of r",
})
