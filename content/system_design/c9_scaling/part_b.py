"""Scaling Laws and Cost, lessons 07-11 - the lag, the unit cost, and the three transfer break-evens."""

LESSONS = [
    # ---------------------------------------------------------------- 07
    {
        "slug": "autoscaling-lag",
        "title": "Autoscaling Lag",
        "module": "Paying for the peak",
        "one_line": "Compute the requests a boot window costs during a ramp, and the warm reserve that removes the shortfall entirely.",
        "summary": (
            "Capacity does not arrive when it is ordered. During a ramp the fleet is "
            "permanently the boot window behind demand, and the requests lost to that "
            "gap are the area between two lines: a triangle while the boot and the ramp "
            "overlap, then a rectangle for the rest of it. The only thing that removes "
            "it is capacity that was already warm."
        ),
        "key": [
            "shortfall = r·τ·(D − τ/2)     r = 50 rps/s, τ = 90 s, D = 300 s",
            "          = 4 500 × 255 = 1 147 500 requests",
            "triangle 202 500 + rectangle 945 000 = the same 1 147 500",
            "the fleet is permanently r·τ = 4 500 rps behind",
            "worst instant  λ = 9 500, μ = 5 000, ρ = λ/μ = 19/10 > 1",
            "a warm reserve of r·τ = 4 500 rps makes the shortfall exactly zero",
        ],
        "key_label": "A trapezoid, and the reserve that flattens it",
        "concepts_intro": (
            "The geometry is easy. What is worth taking from the page is what the area "
            "means: not slow requests, but requests that were never served."
        ),
        "concepts": [
            ("The fleet is behind by r·τ, constantly",
             "Demand rises at `r` a second; capacity responds to the demand of `τ` "
             "seconds ago, because that is when the instances now arriving were ordered. "
             "So once the ramp is under way the gap is `r·τ` and it stays there: "
             "`50 × 90 = 4 500 rps` here, at every instant from the boot window until "
             "the ramp stops. It is not a transient that closes as the fleet grows."),
            ("The shortfall is an area, and it has two parts",
             "While the boot window and the ramp overlap, the gap is growing and the "
             "region is a triangle of `½·r·τ² = 202 500` requests. After that the gap is "
             "constant and the region is a rectangle, `r·τ·(D − τ) = 945 000`. Added, "
             "they are `r·τ·(D − τ/2) = 1 147 500` &mdash; the closed form, and the two "
             "routes must agree."),
            ("Above ρ = 1 there is no steady state, so the backlog is not a queue",
             "`ρ` here is `λ/μ`, the same definition &ldquo;λ, μ and ρ&rdquo; gives, "
             "with `μ` the capacity actually in service rather than the capacity "
             "ordered. At the worst instant `λ = 9 500` against `μ = 5 000`, so "
             "`ρ = 19/10`. Above one there is no steady state at all: the backlog grows "
             "at `λ − μ = 4 500` requests a second, and `1/(1 − ρ)` is not a number."),
        ],
        "read_title": "A boot window, the area it costs, and the only thing that removes it",
        "read_intro": (
            "Where the trapezoid comes from, why the backlog never drains, and what a "
            "warm reserve is actually buying."
        ),
        "body": [
            ("def", ("Autoscaling shortfall",
                     "Let demand rise from a level the fleet already serves at a rate "
                     "`r` requests per second per second, for a ramp of duration `D`. "
                     "Let `τ` be the time between ordering an instance and it serving "
                     "traffic. With no warm reserve, the <strong>shortfall</strong> "
                     "&mdash; the number of requests demanded and not served &mdash; is",
                     "`r·τ·(D − τ/2)`  for `D ≥ τ`,",
                     "which is the area between the demand line and the capacity line "
                     "over the ramp.")),
            ("p", "The derivation is geometry. For the first `τ` seconds capacity does "
                  "not move at all, so the gap grows linearly from zero to `r·τ`: a "
                  "triangle of area `½·r·τ²`. After that, capacity rises at the same "
                  "rate as demand but `τ` seconds later, so the gap is a constant `r·τ` "
                  "for the remaining `D − τ` seconds: a rectangle of area `r·τ·(D − τ)`."),
            ("math", [
                "r = 50 rps/s     τ = 90 s     D = 300 s     base load 5 000 rps",
                "",
                "triangle    ½ · r · τ²      = ½ × 50 × 8 100   =   202 500",
                "rectangle   r · τ · (D − τ) = 4 500 × 210      =   945 000",
                "                                              ------------",
                "total                                           1 147 500 requests",
                "",
                "closed form r · τ · (D − τ/2) = 4 500 × 255   = 1 147 500   ✓",
            ]),
            ("p", "Both routes give the same integer, which is the check. The closed "
                  "form is the area of a trapezoid: the mean of the two gaps &mdash; "
                  "zero at the start and `r·τ` from the boot window on &mdash; taken "
                  "over the ramp, with the `τ/2` recording that the gap spent the first "
                  "boot window opening rather than open."),
            ("h3", "What the area is made of"),
            ("p", "It is worth being exact about what `1 147 500` counts. It is not "
                  "requests that were slow; it is demand that arrived while there was no "
                  "capacity for it. Whether those requests queue, retry or fail is a "
                  "property of the system in front of the fleet, and every one of those "
                  "outcomes is bad in a different way."),
            ("math", [
                "moment                     λ        μ in service     ρ = λ/μ",
                "t = 0 s   ramp starts    5 000        5 000            1",
                "t = 45 s  mid-boot       7 250        5 000          29/20",
                "t = 90 s  τ: first ready 9 500        5 000          19/10",
                "t = 300 s D: ramp ends  20 000       15 500          40/31",
                "t = 390 s caught up     20 000       20 000            1",
            ]),
            ("p", "Every row above `ρ = 1` is a row with no steady state. The backlog "
                  "grows at `λ − μ` for as long as the row lasts, which at the worst "
                  "instant is `4 500` requests a second. This is the same `ρ` as "
                  "&ldquo;λ, μ and ρ&rdquo;, and the only thing this page adds is that "
                  "`μ` must be the capacity in service rather than the capacity "
                  "requested &mdash; the difference between those two is exactly the "
                  "subject of the lesson."),
            ("h3", "The backlog never drains"),
            ("p", "Look at the last row. When the ramp stops, capacity catches up and "
                  "the two lines end level at `20 000 rps`. Level means no spare: there "
                  "is no surplus with which to work through what accumulated, so the "
                  "backlog built during the ramp is still there when the ramp is over. "
                  "It drains only when demand falls, or never."),
            ("p", "That is why &ldquo;autoscaling handles spikes&rdquo; is the wrong "
                  "model. Autoscaling handles <em>growth</em>: given enough time it "
                  "tracks a rising load with a fixed lag and a bounded gap. A spike is "
                  "precisely the case where there is not enough time, and the mechanism "
                  "arrives after the event it was meant to absorb."),
            ("example", ("The reserve that removes it exactly",
                         "Hold `r·τ = 4 500 rps` warm and the shortfall is zero, not "
                         "small. The reserve covers exactly the capacity the boot window "
                         "costs: for the first `τ` seconds it absorbs the growing gap, "
                         "and by the time it is exhausted the first ordered instances "
                         "are in service. Set the reserve to `2 000 rps` instead and the "
                         "shortfall is reduced rather than removed — the lab shades "
                         "what is left.")),
            ("p", "A reserve is idle capacity, which is the waste of &ldquo;Utilisation "
                  "and Waste&rdquo; deliberately bought. That is the honest framing of "
                  "the trade: the shortfall is priced in requests and the reserve is "
                  "priced in instance-hours, and choosing between them is a decision "
                  "rather than an optimisation."),
            ("p", "Two knobs change `r·τ` without buying a reserve, and both are worth "
                  "more than they sound. Halving `τ` &mdash; a smaller image, a warmer "
                  "pool, a faster health check &mdash; halves the gap and quarters the "
                  "triangle. Scaling on a leading signal rather than on the utilisation "
                  "that results from it starts the boot earlier, which is the same "
                  "saving bought with a prediction instead of with money."),
        ],
        "lab": ("scale", {
            "mode": "autoscale",
            "panel_title": "Set the ramp, the boot time and the reserve",
            "panel_intro": (
                "The shortfall is the exact area between demand and the capacity "
                "actually in service, and `r·τ·(D − τ/2)` is printed beside it as the "
                "check. `ρ` is `λ/μ` &mdash; the definition of &ldquo;λ, μ and ρ&rdquo;, "
                "not a second one &mdash; so the same two consequences apply: above `1` "
                "the backlog grows at `λ − μ`, and below it the response-time multiplier "
                "is `1/(1 − ρ)`. Raise the reserve to `4 500 rps` and watch the shaded "
                "area disappear."
            ),
        }),
        "steps_title": "Sizing a boot window against a ramp",
        "steps_intro": "The gap first, because it is one multiplication and everything else is its area.",
        "steps": [
            ("Multiply the ramp rate by the boot time",
             "`r·τ` is how far behind the fleet runs for the whole of the ramp: "
             "`4 500 rps` here. Quote it in the same units as the load, because it is "
             "directly comparable with the base load &mdash; `4 500` against `5 000` is "
             "a fleet running at nearly double what it can serve."),
            ("Compute the area both ways",
             "Triangle plus rectangle, then `r·τ·(D − τ/2)`. They must agree to the "
             "request. Two routes to one figure is what stops a factor of two in the "
             "triangle going unnoticed, and a factor of two here is half a million "
             "requests."),
            ("Find the worst instant and take ρ there",
             "`λ/μ` with `μ` the capacity in service. If it is above `1`, say so in "
             "those terms: no steady state, backlog growing at `λ − μ`. A utilisation "
             "above one is not a busy system, and reporting it as `190%` invites it to "
             "be read as one."),
            ("Check whether there is any surplus after the ramp",
             "Compare capacity and demand at the end. Level means the backlog never "
             "drains on its own. This single comparison is what turns the shortfall from "
             "a transient into a permanent debt, and it is one subtraction."),
            ("Price the reserve against the shortfall",
             "`r·τ` of warm capacity removes the area exactly. That capacity is idle "
             "most of the time, so the decision is instance-hours against requests, and "
             "both sides of it now have numbers."),
        ],
        "worked": {
            "title": "A 90-second boot against a 300-second ramp at 50 rps a second",
            "intro": [
                "The base load is 5 000 rps and the fleet is exactly sized for it when "
                "the ramp begins."
            ],
            "lines": [
                "r = 50 rps/s      τ = 90 s      D = 300 s",
                "",
                "the constant gap          r·τ = 50 × 90 = 4 500 rps",
                "",
                "first 90 s   gap grows 0 → 4 500",
                "             triangle  ½ × 90 × 4 500     =    202 500 requests",
                "next 210 s   gap constant at 4 500",
                "             rectangle 210 × 4 500        =    945 000 requests",
                "                                             -------------",
                "                                               1 147 500 requests",
                "",
                "check        r·τ·(D − τ/2) = 4 500 × (300 − 45)",
                "                           = 4 500 × 255 = 1 147 500      ✓",
                "",
                "worst instant, t = 90 s:",
                "   λ = 5 000 + 50×90 = 9 500 rps      μ = 5 000 rps",
                "   ρ = λ/μ = 19/10 > 1   ⟹   no steady state",
                "   backlog grows at λ − μ = 4 500 requests a second",
                "",
                "end of the ramp, t = 300 s:  λ = 20 000,  μ = 15 500",
                "the fleet levels at t = 390 s:  λ = μ = 20 000, and nothing spare",
                "   ⟹ the 1 147 500 never drains",
                "",
                "with a warm reserve of r·τ = 4 500 rps:  shortfall = 0",
            ],
            "after": [
                "The check line matters more than it looks. `½·r·τ² + r·τ·(D − τ)` and "
                "`r·τ·(D − τ/2)` are the same quantity written two ways, and computing "
                "both is how you find out that you used `D` where you meant `D − τ`.",
                "The `nothing spare` line is the one that changes what the shortfall "
                "means. If the fleet ended above demand, the backlog would clear and the "
                "shortfall would be a latency event. It ends level, so the shortfall is "
                "a permanent loss of just over a million requests, and no later "
                "behaviour of the autoscaler recovers it.",
                "For a faded attempt, halve the boot window to `45 s` and keep "
                "everything else. Predict before computing what happens to the triangle "
                "and to the total &mdash; one of them falls by a factor of four and the "
                "other does not &mdash; then read both off the lab and say what a warm "
                "reserve would now have to be."
            ],
        },
        "quiz_title": "Boot windows, areas and reserves",
        "quiz": [
            {"q": "Demand ramps at `50 rps` a second for `300 s` and instances take `90 s` to boot. How many requests does the boot window cost?",
             "a": ["`4 500`", "`202 500`", "`945 000`", "`1 147 500`"],
             "c": 3,
             "why": "`r·τ·(D − τ/2) = 4 500 × 255 = 1 147 500`, which is also the "
                    "triangle `202 500` plus the rectangle `945 000`. `4 500` is the "
                    "constant gap in rps &mdash; a rate, not a count. The other two are "
                    "the halves of the area, each correct on its own and neither the "
                    "total."},
            {"q": "At the worst instant `λ = 9 500 rps` and the capacity in service is `μ = 5 000 rps`. What does `ρ = 19/10` mean here?",
             "a": ["The fleet is 90% busier than usual",
                   "There is no steady state: the backlog grows at `λ − μ = 4 500` requests a second",
                   "Response time is multiplied by `1/(1 − ρ)`",
                   "The fleet is running at 190% utilisation and will be slower by that factor"],
             "c": 1,
             "why": "`ρ > 1` means demand exceeds the capacity in service, so nothing "
                    "settles and the backlog accumulates at the difference &mdash; "
                    "`4 500` a second. `1/(1 − ρ)` is defined only below one and is "
                    "negative here, which is the signal that the formula does not apply. "
                    "The other two readings treat `ρ > 1` as a busy-but-working system, "
                    "which is exactly the error the threshold exists to prevent."},
            {"q": "The ramp ends and the fleet catches up. What happens to the requests that were missed during the ramp?",
             "a": ["They are served late, once capacity catches up",
                   "They are not recovered: capacity and demand end level, so there is no surplus to drain a backlog with",
                   "They are absorbed by the reserve",
                   "They are re-tried automatically and add to the shortfall"],
             "c": 1,
             "why": "Catching up means capacity equals demand, and equality leaves "
                    "nothing over. Draining a backlog needs `μ > λ`, which never happens "
                    "on this ramp. There is no reserve in this configuration &mdash; "
                    "that is the point of the lesson &mdash; and whether the missed "
                    "requests retry is a property of the caller, not of the autoscaler."},
            {"q": "What warm reserve makes the shortfall exactly zero?",
             "a": ["`r·D = 15 000 rps`", "`r·τ = 4 500 rps`", "`r·τ/2 = 2 250 rps`", "`λ_peak = 20 000 rps`"],
             "c": 1,
             "why": "The gap is `r·τ` at every instant once the boot window has passed, "
                    "and it starts at zero, so a reserve of `r·τ` covers the whole "
                    "trapezoid: it absorbs the growing gap for the first `τ` seconds and "
                    "is relieved exactly when the first ordered instances arrive. "
                    "`r·D` is the whole ramp, which is capacity you were going to order "
                    "anyway. Half the gap halves nothing and removes nothing entirely. "
                    "`λ_peak` is the demand at the end of the ramp, not a reserve."},
        ],
        "mistakes": [
            ("Believing autoscaling handles spikes",
             "It handles growth, with a fixed lag and a bounded gap. A spike is the case "
             "where the ramp is short against `τ`, and there the mechanism arrives after "
             "the event: over a `90 s` boot window nothing whatever happens except that "
             "the gap opens to `r·τ`. The instrument that covers a spike is capacity "
             "that is already warm."),
            ("Taking `ρ` against the capacity that was ordered",
             "`μ` is the capacity in service. Counting instances that are booting puts "
             "`ρ` below one and reports a busy system, when the truth is `19/10` and an "
             "unbounded backlog. The boot window is precisely the interval in which the "
             "two counts differ, so using the wrong one here erases the whole effect."),
            ("Reporting the shortfall as latency",
             "The area is demand that arrived with no capacity behind it. It becomes "
             "latency only if something queues it and there is later surplus to work it "
             "off; here the fleet ends level with demand, so there is none. Calling "
             "`1 147 500` requests &ldquo;a slow period&rdquo; makes a permanent loss "
             "sound like a transient."),
        ],
        "standard": ("Finish when a boot window reads as an area rather than as a delay.",
                     "You should be able to compute `r·τ`, produce the shortfall by both "
                     "the two-region route and the closed form, evaluate `ρ = λ/μ` at "
                     "the worst instant with `μ` the capacity in service, say whether "
                     "the backlog drains, and name the reserve that removes the area."),
        "note": "That is the last of the three ways capacity is paid for. What remains "
                "is the cost of a single request, and the surprise in it: the term that "
                "dominates a per-request bill is usually not the one that was sized. "
                "&ldquo;Cost per Request&rdquo; decomposes it into four, and the largest "
                "of them is the bytes going out of the door.",
    },
    # ---------------------------------------------------------------- 08
    {
        "slug": "cost-per-request",
        "title": "Cost per Request",
        "module": "What bytes cost",
        "one_line": "Decompose a monthly bill into cost per request and name the term that dominates it.",
        "summary": (
            "A per-request cost is a fixed charge shared out plus three charges that do "
            "not move with volume at all: compute, the storage a request leaves behind "
            "for as long as it is retained, and the bytes sent back to the caller. Only "
            "the first falls as traffic grows, and it is rarely the largest."
        ),
        "key": [
            "cost/req = fixed/V + compute + storage + egress",
            "V = 500 000 000 a month, fixed $4 000, compute 1 µ$, 120 kB out, 2 kB kept 12 months",
            "fixed    $0.00000800   39.3%      the only term that falls with volume",
            "compute  $0.00000100    4.9%      storage  $0.00000055   2.7%",
            "egress   $0.00001080   53.1%      the biggest, and 10.8× the compute",
            "total    $0.00002035 a request  =  $10 176 a month",
            "V* = fixed ÷ egress-per-request = 370 370 370 a month",
        ],
        "key_label": "Four terms, and only one of them is a curve",
        "concepts_intro": (
            "The arithmetic is addition. The content of the lesson is which of the four "
            "addends turns out to be largest, and what that implies for how the bill "
            "moves."
        ),
        "concepts": [
            ("Only the fixed term is a function of volume",
             "`fixed/V` falls like `1/V`; compute, storage-per-request and egress are "
             "flat per request whatever `V` is. So the unit cost falls with scale and "
             "the monthly total rises linearly with it, and both statements are true at "
             "once. &ldquo;Cost scales with users&rdquo; gets the total right and the "
             "unit cost exactly backwards."),
            ("Storage accrues with retention, not with traffic",
             "Each request leaves `2 000` bytes behind and they are billed every month "
             "they are kept. Doubling the retention from twelve months to twenty-four "
             "doubles that term while the request rate is untouched, which makes "
             "retention the only lever on this page that changes a cost without changing "
             "any rate. Here it is `$0.00000055`, or `$276` a month."),
            ("Egress is usually the term that surprises",
             "`120 kB` of response at `$0.090` a gigabyte is `$0.00001080` a request "
             "&mdash; `53.1%` of the bill and `10.8×` the compute the request consumed. "
             "It is the term nobody sizes, because it is a property of the response body "
             "rather than of the code, and it is the first place to look when a bill "
             "does not match the machines."),
        ],
        "read_title": "Four terms, their shares, and the crossing where the largest changes",
        "read_intro": (
            "How each term is built, why only one of them is a curve, and the equality "
            "that locates the volume at which the biggest term changes hands."
        ),
        "body": [
            ("def", ("Cost per request",
                     "For a monthly volume `V`, a fixed monthly cost `F`, a compute cost "
                     "`c` per request, `b` bytes stored per request held for `R` months "
                     "at `p_s` per gigabyte-month, and `e` bytes of egress per request "
                     "at `p_e` per gigabyte, the <strong>cost per request</strong> is",
                     "`F/V + c + (b·R·p_s)/10⁹ + (e·p_e)/10⁹`.",
                     "The monthly total is that figure times `V`. Only the first term "
                     "depends on `V`.")),
            ("p", "Keeping the four terms apart is the whole technique. A single "
                  "&ldquo;cost per request&rdquo; tells you what you are paying; the "
                  "decomposition tells you what to change, and those are almost never "
                  "the same number."),
            ("math", [
                "V = 500 000 000 a month      F = $4 000      c = 1 µ$",
                "stored 2 000 B a request, kept 12 months at $0.023 a GB-month",
                "egress 120 000 B a request at $0.090 a GB",
                "",
                "term           $ per request    share     $ a month",
                "fixed           0.00000800      39.3%       4 000",
                "compute         0.00000100       4.9%         500",
                "storage         0.00000055       2.7%         276",
                "egress          0.00001080      53.1%       5 400",
                "               ------------     -----      ------",
                "total           0.00002035       100%      10 176",
            ]),
            ("p", "Two of those rows deserve a second look. The storage row is `1 000` "
                  "gigabytes of new data a month billed for twelve months, which is "
                  "`$276` &mdash; and it would be `$552` at a two-year retention with "
                  "exactly the same traffic. The egress row is `60 000` gigabytes going "
                  "out of the door, which is nearly seven times the compute and the "
                  "storage put together and `10.8×` the compute alone."),
            ("h3", "The unit cost falls while the bill rises"),
            ("p", "Both of these are consequences of the same decomposition and they "
                  "sound contradictory only if the two quantities are confused. At ten "
                  "times the volume the fixed term falls to `$0.00000080` and the other "
                  "three do not move, so the unit cost drops to `$0.00001315` &mdash; "
                  "and the monthly bill rises to `$65 760`, because there are ten times "
                  "as many requests paying it."),
            ("example", ("Where the fixed term stops being the largest",
                         "At low volume the fixed charge dominates everything. It stops "
                         "being larger than egress when `F/V = e·p_e/10⁹`, that is at "
                         "`V* = F ÷ egress-per-request = 4 000 ÷ 0.0000108 = "
                         "370 370 370` requests a month. Below that, the thing to "
                         "optimise is the fixed cost; above it, the response body. That "
                         "is an equality solved, not a curve read off a chart by eye.")),
            ("h3", "What each term responds to"),
            ("ul", [
                "<strong>Fixed</strong> &mdash; load balancers, minimum fleet, "
                "licences, the control plane. Falls per request as traffic grows and "
                "never falls in total.",
                "<strong>Compute</strong> &mdash; the work the request does. Reduced by "
                "making the request cheaper, and by nothing else.",
                "<strong>Storage</strong> &mdash; bytes multiplied by how long they are "
                "kept. Reduced by retention, by compression, or by tiering, which is the "
                "subject of the next lesson.",
                "<strong>Egress</strong> &mdash; bytes sent back. Reduced by sending "
                "less: smaller payloads, compression on the wire, caching closer to the "
                "caller so the bytes do not leave twice.",
            ]),
            ("p", "The reason this list is worth writing down is that a team with a "
                  "cost problem almost always starts on the second line, because that is "
                  "the line their tools measure. On this profile the second line is "
                  "`4.9%` of the bill, and halving it saves `$250` a month against the "
                  "`$5 400` sitting in the fourth."),
            ("example", ("A cache changes two terms at once",
                         "Serving a fifth of requests from a cache in front of the "
                         "service removes their compute and their egress from the origin "
                         "&mdash; but only the second if the cache is on the other side "
                         "of the metered boundary. Whether a cached response still pays "
                         "egress is a question about topology rather than about hit "
                         "rates, and it decides whether the saving is `4.9%` of a fifth "
                         "or `58%` of a fifth. &ldquo;Caching and Hit Rates&rdquo; "
                         "supplies the hit rate; this page supplies what a hit is worth.")),
            ("p", "One thing this decomposition deliberately does not do is forecast. "
                  "Every term here is priced at a volume you state, and the question of "
                  "what `V` will be in eighteen months is capacity planning under "
                  "uncertainty, which this course does not cover. What it does give you "
                  "is the shape: a curve that falls toward a floor made of three flat "
                  "terms, and the floor is where a mature service lives."),
        ],
        "lab": ("scale", {
            "mode": "unit",
            "panel_title": "Set the volume, the costs and the retention",
            "panel_intro": (
                "Each of the four terms is an exact fraction of the inputs, and only the "
                "fixed one depends on volume. The crossing where it stops being the "
                "largest is `fixed ÷ egress-per-request` &mdash; an equality solved, not "
                "a curve read off by eye. Drag the volume across the decades and watch "
                "the unit cost fall onto the floor the other three terms make."
            ),
        }),
        "steps_title": "Decomposing a bill into a unit cost",
        "steps_intro": "Four terms computed separately, because the total on its own does not tell you what to change.",
        "steps": [
            ("Fix the volume and the period, and say both",
             "A cost per request is meaningless without the volume it was computed at, "
             "because one of the four terms depends on it. `$0.00002035` at "
             "`500 000 000` a month is a fact; `$0.00002035` on its own is not."),
            ("Compute the three flat terms first",
             "Compute per request, bytes stored times retention times the storage price, "
             "bytes out times the egress price. None of them mentions `V`, so they are "
             "the floor the unit cost is falling toward and they are worth knowing "
             "before anything else."),
            ("Add the fixed term and take the shares",
             "`F/V`, then each term as a percentage of the total. The shares are the "
             "output that matters: they say which line an hour of engineering should be "
             "spent on, and they are usually a surprise."),
            ("Multiply back to a monthly total and check it",
             "`unit × V` must reproduce the bill you started from. If it does not, one "
             "of the terms is in the wrong units &mdash; gigabytes against gibibytes, or "
             "a per-month price used per request."),
            ("Locate the crossing between the two largest terms",
             "`F ÷ (largest flat term per request)` is the volume at which the fixed "
             "charge stops dominating. Report it, because it tells the reader whether "
             "they are on the falling part of the curve or on the floor."),
        ],
        "worked": {
            "title": "500 000 000 requests a month, 120 kB out, 2 kB kept for a year",
            "intro": [
                "Every term is computed per request and then multiplied back up, so the "
                "two views of the same bill can be checked against each other."
            ],
            "lines": [
                "V = 500 000 000 requests a month",
                "",
                "fixed     $4 000 ÷ 500 000 000            = $0.00000800   39.3%",
                "compute   given                            = $0.00000100    4.9%",
                "storage   2 000 B × 12 months × $0.023/GB-month",
                "            = 1 000 GB/month × 12 × $0.023 = $276 a month",
                "            $276 ÷ 500 000 000             = $0.00000055    2.7%",
                "egress    120 000 B × $0.090/GB",
                "            = 60 000 GB × $0.090           = $5 400 a month",
                "            $5 400 ÷ 500 000 000           = $0.00001080   53.1%",
                "                                            ------------  ------",
                "total                                       $0.00002035    100%",
                "",
                "monthly   $0.00002035 × 500 000 000        = $10 176",
                "check     4 000 + 500 + 276 + 5 400        = $10 176        ✓",
                "",
                "biggest term            egress, at 10.8× the compute",
                "fixed = egress at       V* = 4 000 ÷ 0.0000108 = 370 370 370 a month",
                "",
                "at ten times the volume:",
                "  fixed 0.00000080, others unchanged  ⟹  unit $0.00001315",
                "  monthly $65 760 — the unit cost fell and the bill rose",
            ],
            "after": [
                "Money is shown to eight decimal places, so the exact "
                "`$0.000020352` a request appears in the panel as `$0.00002035`; the "
                "monthly totals are exact. "
                "The check line is not ceremony. Computing the bill twice &mdash; four "
                "monthly figures added, and one unit cost multiplied by the volume "
                "&mdash; catches a units error in the byte terms, which is where they "
                "all live.",
                "The two lines at the bottom are the misconception answered with "
                "numbers. The unit cost fell by `35%` and the bill rose by a factor of "
                "ten, and neither of those is a contradiction: one is a ratio with `V` "
                "in the denominator and the other has `V` in the numerator.",
                "For a faded attempt, halve the response to `60 kB` and double the "
                "retention to twenty-four months. Predict the direction and rough size "
                "of each of the four terms before computing, then read the unit cost, "
                "the monthly total and the new biggest term off the lab."
            ],
        },
        "quiz_title": "Terms, shares and what moves them",
        "quiz": [
            {"q": "At `500 000 000` requests a month with `$4 000` fixed, `1 µ$` of compute, `2 kB` kept for twelve months and `120 kB` of egress, which term is largest?",
             "a": ["fixed, at `$0.00000800`", "compute, at `$0.00000100`", "storage, at `$0.00000055`", "egress, at `$0.00001080`"],
             "c": 3,
             "why": "Egress is `53.1%` of the `$0.00002035` total &mdash; `$5 400` of a "
                    "`$10 176` bill, and `10.8×` the compute. Fixed is second at "
                    "`39.3%` and would be first below `370 370 370` requests a month. "
                    "Compute and storage together are `7.6%`, which is why sizing the "
                    "fleet is rarely where a bill of this shape is won."},
            {"q": "Traffic grows tenfold with everything else unchanged. What happens to the cost per request and to the monthly bill?",
             "a": ["Both rise tenfold", "Both fall", "The unit cost falls to `$0.00001315`; the bill rises to `$65 760`", "The unit cost is unchanged; the bill rises tenfold"],
             "c": 2,
             "why": "Only `F/V` moves: it falls from `$0.00000800` to `$0.00000080`, so "
                    "the unit cost drops onto the floor the three flat terms make. The "
                    "bill is unit times volume and rises. &ldquo;Both rise&rdquo; and "
                    "&ldquo;unchanged unit cost&rdquo; are the two halves of "
                    "&ldquo;cost scales with users&rdquo;, and each gets one of the two "
                    "quantities wrong."},
            {"q": "Retention is doubled from twelve months to twenty-four, with no change in traffic. Which figure moves?",
             "a": ["The compute term, since more data is read",
                   "The storage term, from `$276` to `$552` a month",
                   "The fixed term, since more capacity is needed",
                   "Nothing, until the extra data is actually accessed"],
             "c": 1,
             "why": "Storage is bytes multiplied by the months they are kept, so "
                    "doubling the retention doubles it exactly &mdash; `$0.00000055` "
                    "becomes `$0.00000110` a request. No request is served differently, "
                    "so compute does not move; the fixed term is a monthly charge "
                    "unrelated to stored bytes; and storage is billed for being held, "
                    "not for being read."},
            {"q": "Below what monthly volume is the fixed charge the largest of the four terms?",
             "a": ["`500 000 000`", "`370 370 370`", "`4 000 000`", "It is always the largest at low volume and there is no crossing"],
             "c": 1,
             "why": "Set `F/V` equal to the egress term: `4 000/V = 0.0000108` gives "
                    "`V* = 370 370 370` requests a month. `500 000 000` is the operating "
                    "point, where egress has already overtaken it. `4 000 000` confuses "
                    "the fixed dollars with a volume. And there is a crossing precisely "
                    "because `F/V` falls while the other terms do not."},
        ],
        "mistakes": [
            ("Reading “cost scales with users” as a single claim",
             "It is two claims and they point in opposite directions. The monthly total "
             "rises roughly linearly with volume because three of the four terms are "
             "flat per request; the cost per request falls, because the fourth is "
             "`F/V`. Deciding anything from the total alone will reject growth that "
             "makes every request cheaper."),
            ("Optimising the term your tools measure",
             "Compute is the term with dashboards attached to it, and on this profile "
             "it is `4.9%` of the bill. Egress is `53.1%` and appears on no CPU graph "
             "anywhere. The decomposition exists so that the largest term is chosen by "
             "arithmetic rather than by which number was easiest to find."),
            ("Quoting a cost per request without the volume",
             "The figure contains `F/V`, so it is a statement about a specific volume "
             "and it changes when the volume does. `$0.00002035` at `500 000 000` a "
             "month becomes `$0.00001315` at ten times that, with nothing else altered "
             "&mdash; a difference of `35%` that looks like an efficiency gain and is "
             "arithmetic."),
        ],
        "standard": ("Finish when a bill arrives as four terms with shares rather than as one number.",
                     "You should be able to compute each of the four terms per request, "
                     "reproduce the monthly total two ways, name the largest term and "
                     "its multiple of the smallest, and locate the volume at which the "
                     "fixed charge stops dominating."),
        "note": "Two of those four terms are bytes: the ones you keep and the ones you "
                "send. The rest of this course is about both, and each question turns "
                "out to be a single equality. &ldquo;Storage Tiers and the Access "
                "Break-even&rdquo; takes the bytes you keep and finds the access rate at "
                "which a cheaper, slower tier stops paying for itself.",
    },
    # ---------------------------------------------------------------- 09
    {
        "slug": "storage-tiers",
        "title": "Storage Tiers and the Access Break-even",
        "module": "What bytes cost",
        "one_line": "Compute the access rate at which a cold tier stops paying, and the age at which a decaying access profile reaches it.",
        "summary": (
            "A cold tier is cheaper to keep and dearer to read. Setting the monthly "
            "saving equal to the retrieval charges gives one access rate, `a*`, above "
            "which cold costs more than hot. Data is then tiered by age, because access "
            "rates fall with age &mdash; and the age at which the profile crosses `a*` "
            "is the boundary."
        ),
        "key": [
            "a* = (hot − cold)/retrieval = ($0.023 − $0.004)/$0.010 = 19/10 reads a GB-month",
            "reads halve with age:  8, 4, 2, 1, …    a* is crossed at month 3",
            "month 2   $23.00 hot   against   $4.00 + $20.00 = $24.00 cold   stay hot",
            "month 3   $23.00 hot   against   $4.00 + $10.00 = $14.00 cold   go cold",
            "21 000 of 24 000 GB move    $552.00 → $173.00 a month, saving $379.00",
            "c is the cold-tier price throughout, and is never a server count",
        ],
        "key_label": "One equality, then one integer search over ages",
        "concepts_intro": (
            "The break-even is a single equation. The part that is easy to get wrong is "
            "which side of it old data is on, and the answer is not always the obvious "
            "one."
        ),
        "concepts": [
            ("The saving is monthly and the cost is per access",
             "Moving a gigabyte from hot to cold saves `hot − cold` every month it "
             "stays there, and costs `retrieval` every time it is read back. Those are "
             "different units, and setting them equal is what produces a rate: "
             "`a* = (hot − cold)/retrieval` reads per gigabyte per month. Below that "
             "rate cold is cheaper; above it, the retrieval charges swallow the saving."),
            ("Age is a proxy for access rate, and only a proxy",
             "Data is tiered by age because access usually decays with age, not because "
             "old bytes are cheaper to store. The decision is always about the rate: "
             "here reads halve each month from eight per gigabyte, so `a*` is crossed "
             "at month three, and that is the age boundary. A profile that does not "
             "decay has no boundary at all."),
            ("Everything old going cold is a real way to lose money",
             "At month zero a gigabyte is read eight times, which costs `$0.080` in "
             "retrieval against a `$0.019` saving. Moving it costs four times what "
             "keeping it hot would have. The rule that works is not &ldquo;old goes "
             "cold&rdquo; but &ldquo;below `a*` goes cold&rdquo;, and on this profile "
             "those coincide only from month three."),
        ],
        "read_title": "Two prices, a retrieval charge, and the rate where they meet",
        "read_intro": (
            "The break-even as an equality, the integer search that turns it into an "
            "age, and what the whole-archive bill looks like on either side of it."
        ),
        "body": [
            ("def", ("Access break-even",
                     "Let `h` be the hot price per gigabyte-month, `c` the cold price "
                     "per gigabyte-month and `t` the retrieval charge per gigabyte read "
                     "back from cold. A gigabyte read `a` times a month costs `h` hot "
                     "and `c + a·t` cold, so cold is cheaper exactly when",
                     "`a < a* = (h − c)/t`.",
                     "`c` on this page is the cold-tier price throughout and is never a "
                     "server count.")),
            ("p", "At `h = $0.023`, `c = $0.004` and `t = $0.010` the break-even is "
                  "`(0.023 − 0.004)/0.010 = 19/10`, or `1.9` reads a gigabyte a month. "
                  "A gigabyte read twice a month belongs hot; one read once a month "
                  "belongs cold; and the difference between those two cases is a third "
                  "of a cent, which is why this is done for petabytes rather than for "
                  "gigabytes."),
            ("math", [
                "h = $0.023/GB-month    c = $0.004/GB-month    t = $0.010/GB read",
                "",
                "a* = (h − c)/t = (0.023 − 0.004)/0.010 = 1.9 = 19/10 reads/GB-month",
                "",
                "reads by age, halving each month:   8, 4, 2, 1, 1/2, 1/4, …",
                "",
                " age      reads      all hot          cold: keep + read back     tier",
                " m 0        8        $23.00          $4.00 + $80.00 = $84.00     hot",
                " m 1        4        $23.00          $4.00 + $40.00 = $44.00     hot",
                " m 2        2        $23.00          $4.00 + $20.00 = $24.00     hot",
                " m 3        1        $23.00          $4.00 + $10.00 = $14.00     cold",
                " m 4        1/2      $23.00          $4.00 +  $5.00 =  $9.00     cold",
                " m 23    1/2²⁰       $23.00          $4.00 +  $0.00 =  $4.00     cold",
            ]),
            ("p", "Each row above is a bucket of `1 000` gigabytes, one for every month "
                  "of the archive&rsquo;s twenty-four-month retention, which is why the "
                  "hot column is a flat `$23.00`. The verdict flips between month two "
                  "and month three, and nothing about the flip is approximate: it is a "
                  "comparison of two exact figures at each integer age."),
            ("h3", "The age boundary is found by counting, not by solving"),
            ("p", "The access profile here is `8 × (1/2)ᵐ` reads a gigabyte in month "
                  "`m`, and the boundary is the smallest `m` with `8 × (1/2)ᵐ < 19/10`. "
                  "Evaluating that at each integer gives `8, 4, 2, 1` &mdash; the "
                  "crossing is at `m = 3`. A logarithm would give `2.07…` and then need "
                  "rounding in a direction that has to be argued for; the search needs "
                  "no argument."),
            ("example", ("The whole archive, both ways",
                         "Twenty-four monthly buckets of `1 000 GB` is `24 000 GB`. All "
                         "hot: `24 000 × $0.023 = $552.00` a month. Tiered at month "
                         "three: three hot buckets at `$23.00` is `$69.00`, twenty-one "
                         "cold buckets at `$4.00` is `$84.00`, and the reads on those "
                         "cold buckets come to about `$20.00`, for `$173.00` in all. "
                         "The saving is `$379.00` a month, and `21 000 GB` moved to "
                         "earn it.")),
            ("h3", "The two ways the calculation goes wrong"),
            ("p", "Moving too early is the expensive one. The month-zero bucket read "
                  "eight times a gigabyte costs `$84.00` cold against `$23.00` hot: "
                  "tiering it more than triples its bill. Anyone applying &ldquo;archive "
                  "anything over thirty days&rdquo; to a profile whose reads have not "
                  "yet decayed is doing exactly this."),
            ("p", "Moving too late is cheap and dull. Leaving the month-twenty-three "
                  "bucket hot costs `$23.00` instead of `$4.00`, a loss of `$19.00` a "
                  "month on that bucket. It is real money at scale and it never causes "
                  "an incident, which is why it is the error that survives in production "
                  "for years."),
            ("p", "One quantity is deliberately absent from `a*`: the amount of data. "
                  "The break-even is a rate per gigabyte, so it is the same for a "
                  "terabyte and a petabyte. Volume decides how much the decision is "
                  "worth, not which way it goes &mdash; and that is why the archive-wide "
                  "figures above are a separate calculation from the break-even itself."),
            ("p", "Retrieval latency is not priced here at all. A cold tier that takes "
                  "hours to restore is a different product from one that responds in "
                  "milliseconds, and if the access has a deadline the cheaper tier may "
                  "be unusable at any price. This page decides cost; the deadline is a "
                  "constraint applied before it."),
        ],
        "lab": ("scale", {
            "mode": "tier",
            "panel_title": "Set both prices, the retrieval charge and the decay",
            "panel_intro": (
                "`a* = (hot − cold)/retrieval` is exact, and the age at which the "
                "profile reaches it is an integer search over exact powers of the decay "
                "factor &mdash; not a curve read off by eye. Here `c` is the cold-tier "
                "price and is never a server count. Slow the decay and watch the "
                "boundary slide later while `a*` does not move at all."
            ),
        }),
        "steps_title": "Deciding what to tier",
        "steps_intro": "One division, then one pass over the ages. The archive-wide figures come last.",
        "steps": [
            ("Compute `a* = (h − c)/t` and state its units",
             "Reads per gigabyte per month. Units matter here because the numerator is a "
             "monthly price difference and the denominator is a per-read charge, and "
             "getting them the wrong way up gives a plausible-looking number that is a "
             "month per read."),
            ("Write the access profile as a rate at each age",
             "Reads per gigabyte per month at age `0, 1, 2, …`. This is the step that "
             "usually has to be measured rather than assumed, and a profile that does "
             "not decay is a finding: it means there is no age boundary to find."),
            ("Find the first age below `a*` by evaluating, not by taking a logarithm",
             "`8, 4, 2, 1` against `1.9` gives month three. Every comparison is between "
             "two exact numbers, so there is no rounding to argue about and no "
             "direction to justify."),
            ("Cost the whole archive on both plans",
             "All hot, and tiered at the boundary. Include the retrieval charges on the "
             "cold buckets &mdash; they are the term the plan is trading against, and a "
             "saving computed without them is not a saving."),
            ("Check the deadline before you commit to the boundary",
             "A restore time is a constraint, not a cost. If the data is needed within "
             "seconds and the cold tier answers in hours, the arithmetic above is "
             "irrelevant for that data however favourable it looks."),
        ],
        "worked": {
            "title": "Hot 2.3¢, cold 0.4¢, retrieval 1¢: a boundary at month 3",
            "intro": [
                "The archive keeps twenty-four monthly buckets of 1 000 GB each, and "
                "reads halve with every month of age from eight per gigabyte."
            ],
            "lines": [
                "h = $0.023   c = $0.004   t = $0.010    per GB, per GB-month",
                "",
                "a* = (h − c)/t = 0.019/0.010 = 19/10 = 1.9 reads a GB-month",
                "",
                "reads at age m:  8 × (1/2)ᵐ",
                "   m = 0   8      ≥ 1.9   hot",
                "   m = 1   4      ≥ 1.9   hot",
                "   m = 2   2      ≥ 1.9   hot          (2 is above 1.9, only just)",
                "   m = 3   1      < 1.9   cold   ←  the boundary",
                "",
                "per 1 000 GB bucket:",
                "   m = 2   hot $23.00   cold $4.00 + 2×1 000×$0.010 = $24.00   hot wins",
                "   m = 3   hot $23.00   cold $4.00 + 1×1 000×$0.010 = $14.00   cold wins",
                "",
                "whole archive, 24 buckets = 24 000 GB:",
                "   all hot        24 000 × $0.023                  = $552.00",
                "   tiered at 3     3 hot × $23.00                   =  $69.00",
                "                  21 cold × $4.00                   =  $84.00",
                "                  retrieval on the cold buckets     ≈  $20.00",
                "                                                     --------",
                "                                                      $173.00",
                "   saving                                            $379.00 a month",
                "   moved                                             21 000 GB",
            ],
            "after": [
                "The `m = 2` row is the one worth pausing on. Two reads a gigabyte is "
                "above the break-even of `1.9` by a tenth, and the bill agrees by a "
                "dollar: `$24.00` cold against `$23.00` hot. A break-even is a crossing, "
                "and a bucket sitting a tenth of a read above it really does cost more "
                "in the cheaper tier.",
                "The retrieval line on the tiered plan is what a saving computed from "
                "storage prices alone would have left out. It is small here &mdash; "
                "about `$20.00` against a `$379.00` saving &mdash; only because the "
                "boundary was chosen where reads had already decayed. Move the boundary "
                "to month zero and that line becomes the whole bill.",
                "For a faded attempt, slow the decay so that reads fall to `70%` of the "
                "previous month rather than `50%`. Predict first whether `a*` moves, "
                "then find the new boundary age by evaluating the profile, and read the "
                "new saving off the lab."
            ],
        },
        "quiz_title": "Tiers, rates and ages",
        "quiz": [
            {"q": "Hot storage costs `$0.023` a GB-month, cold `$0.004`, and reading back from cold costs `$0.010` a GB. Above what access rate is cold more expensive than hot?",
             "a": ["`0.19` reads a GB-month", "`1.9` reads a GB-month", "`2.3` reads a GB-month", "`5.75` reads a GB-month"],
             "c": 1,
             "why": "`a* = (h − c)/t = 0.019/0.010 = 1.9` reads a gigabyte-month. "
                    "`0.19` is the same division with a decimal point misplaced. `2.3` "
                    "is the hot price read as a rate, which ignores both the cold price "
                    "and the retrieval charge. `5.75` is `h/c`, the ratio of the two storage "
                    "prices &mdash; a pure number, not a rate. The break-even needs "
                    "the retrieval charge in the denominator, because that is what "
                    "a read costs."},
            {"q": "A bucket of data is read twice per GB per month, against a break-even of `1.9`. Where does it belong?",
             "a": ["Cold, since `2` is close to `1.9`", "Hot, because `2 > 1.9`: the retrieval charges exceed the storage saving", "Cold, because it is read only twice", "It makes no difference either way"],
             "c": 1,
             "why": "Cold costs `$4.00 + 2 × 1 000 × $0.010 = $24.00` for a "
                    "`1 000 GB` bucket against `$23.00` hot, so cold is a dollar worse. "
                    "The break-even is a crossing and being just above it puts you on "
                    "the wrong side of it. &ldquo;Only twice&rdquo; is an intuition "
                    "about how often, not a comparison against `a*`, and the two figures "
                    "differ, so it does make a difference."},
            {"q": "Reads decay by half each month from eight per GB in month 0. Why does the lesson find the boundary by evaluating `8 × (1/2)ᵐ` rather than by taking a logarithm?",
             "a": ["Because the logarithm would give the wrong answer",
                   "Because every comparison is then between exact numbers and needs no rounding decision",
                   "Because logarithms are not covered on this path",
                   "Because the profile is not exactly geometric"],
             "c": 1,
             "why": "`8 × (1/2)ᵐ` is an exact fraction at every integer `m`, so "
                    "comparing it with `19/10` is exact and the first `m` below is "
                    "unambiguous. The logarithm gives `2.07…`, which is not wrong but "
                    "needs a rounding direction argued for. Logarithms are assumed "
                    "background for this course, and the profile here is exactly "
                    "geometric by construction."},
            {"q": "An archive policy says &ldquo;move everything older than thirty days to cold&rdquo;. On this profile, what does that cost?",
             "a": ["Nothing; month 1 onward is past the break-even",
                   "The month-1 bucket is read four times a GB, so cold costs `$44.00` against `$23.00` hot",
                   "It saves more than tiering at month 3, since more data is cold",
                   "It is the same bill, because the data is the same size"],
             "c": 1,
             "why": "At month one the rate is `4` reads a gigabyte, well above the "
                    "break-even of `1.9`, so the cold bill is "
                    "`$4.00 + 4 × 1 000 × $0.010 = $44.00` for that bucket against "
                    "`$23.00` hot. Moving data is not free once it is read, so more "
                    "cold is not automatically cheaper, and the bill differs precisely "
                    "because retrieval is charged per read rather than per byte held."},
        ],
        "mistakes": [
            ("Tiering by age without checking the rate",
             "Age is a proxy for access rate and the decision is about the rate. On this "
             "profile a thirty-day rule moves a bucket still read four times a gigabyte "
             "a month, whose cold bill is `$44.00` against `$23.00` hot. When the decay "
             "is slower, the same rule is wrong for longer."),
            ("Computing the saving from the storage prices alone",
             "`hot − cold` is `$0.019` a gigabyte-month and looks like the whole prize. "
             "The retrieval charges are the other half of the trade and they are what "
             "the break-even is built from; a saving quoted without them is the answer "
             "to a question about data nobody ever reads."),
            ("Reading `c` as a machine count",
             "Every other course on this path uses `c` for a count of something. Here it "
             "is the cold-tier price per gigabyte-month, it appears in "
             "`a* = (h − c)/t`, and it is a price throughout. The lab prints it as a "
             "price in dollars for this reason."),
        ],
        "standard": ("Finish when a tiering decision is stated as an access rate and an age is only how it gets applied.",
                     "You should be able to compute `a* = (h − c)/t` with its units, "
                     "evaluate a decaying access profile at each integer age to find the "
                     "first one below it, and cost the whole archive on both plans with "
                     "the retrieval charges included."),
        "note": "Bytes held are one half of what a system pays for. The other half is "
                "bytes moved, and the next question about them is whether to spend "
                "processor time shrinking them first. &ldquo;Compress or Not&rdquo; "
                "makes that a single equality too, and the surprise in it is that the "
                "size of the file cancels out of the answer completely.",
    },
    # ---------------------------------------------------------------- 10
    {
        "slug": "compress-or-not",
        "title": "Compress or Not",
        "module": "What bytes cost",
        "one_line": "Time a transfer with and without compression, and compute the link speed at which compressing stops paying.",
        "summary": (
            "Compressing before sending trades processor time for wire time. Setting "
            "the two total times equal cancels the size of the file completely and "
            "leaves a relation between three numbers: the link, the compressor and the "
            "ratio. Above a bandwidth of `rate·(k − 1)/k`, sending it raw is faster."
        ),
        "key": [
            "raw          size/bw  =  10 GB ÷ 125 MB/s  =  80 s",
            "compressed   size/rate + size/(k·bw)  =  40 s + 20 s  =  60 s",
            "1/bw = 1/rate + 1/(k·bw)          the size cancels out entirely",
            "bw* = rate·(k − 1)/k = 187.5 MB/s = 1 500 Mbit/s   faster links send raw",
            "rate* = bw·k/(k − 1) = 166.67 MB/s                 slower compressors lose",
        ],
        "key_label": "Two times, and an equality with no size in it",
        "concepts_intro": (
            "Both plans are one subtraction away from each other. The surprise is what "
            "drops out of the comparison when you set them equal."
        ),
        "concepts": [
            ("The compressed plan has two stages and the raw plan has one",
             "Raw: `size/bw`. Compressed: `size/rate` to squeeze, then `size/(k·bw)` to "
             "send `k` times fewer bytes. At `10 GB`, `k = 4`, a `250 MB/s` compressor "
             "and a `125 MB/s` link that is `80 s` against `40 + 20 = 60 s`, so "
             "compressing wins by `1.33×`. Both stages are on the critical path, which "
             "is why a fast compressor matters as much as a good ratio."),
            ("The size cancels out of the break-even",
             "Set the two times equal and every term carries one factor of `size`, so it "
             "divides away: `1/bw = 1/rate + 1/(k·bw)`. How much you are moving decides "
             "how long both plans take and nothing whatever about which of them is "
             "faster. That is the single most useful thing on this page, because it "
             "means the decision can be made once for a link rather than per file."),
            ("A fast enough link outruns every compressor",
             "Rearranged, the break-even bandwidth is `rate·(k − 1)/k = 187.5 MB/s`, or "
             "`1 500 Mbit/s`. Above that the wire is quicker than the processor and "
             "compression costs time. Read the other way round, on a `125 MB/s` link you "
             "would need a compressor faster than `166.67 MB/s` for it to be worth "
             "doing at all."),
        ],
        "read_title": "Two plans, the equality between them, and what falls out of it",
        "read_intro": (
            "Where each time comes from, the algebra that removes the file size, and the "
            "two readings of the same break-even."
        ),
        "body": [
            ("def", ("The two transfer times",
                     "For a payload of `size` bytes, a link of `bw` bytes a second, a "
                     "compressor running at `rate` bytes of input a second and a "
                     "compression ratio `k` (so the output is `size/k`):",
                     "<strong>raw</strong> takes `size/bw`;",
                     "<strong>compressed</strong> takes `size/rate + size/(k·bw)`.",
                     "Decompression at the far end is counted only when it is on the "
                     "critical path; here the receiver stores the compressed form, so it "
                     "is not.")),
            ("math", [
                "size = 10 GB = 10 000 MB     bw = 1 000 Mbit/s = 125 MB/s",
                "k = 4                        rate = 250 MB/s",
                "",
                "raw           10 000 ÷ 125            =  80 s",
                "",
                "compressed    squeeze  10 000 ÷ 250   =  40 s      66.7%",
                "              send      2 500 ÷ 125   =  20 s      33.3%",
                "                                        ------",
                "                                         60 s",
                "",
                "verdict       compress, by 80/60 = 1.33×",
                "on the wire   2.5 GB instead of 10 GB",
            ]),
            ("p", "The `66.7%` is worth noticing: two thirds of the compressed "
                  "plan&rsquo;s time is the compressor, not the network. That is the "
                  "usual shape once links are fast, and it is why the break-even is "
                  "about the compressor&rsquo;s throughput rather than about the ratio "
                  "alone."),
            ("h3", "Setting them equal"),
            ("p", "The break-even is one equation. Write the two times, set them equal, "
                  "and divide both sides by `size` &mdash; which is legitimate because "
                  "`size` appears exactly once in every term."),
            ("math", [
                "            size/bw  =  size/rate + size/(k·bw)",
                "",
                "divide by size:",
                "              1/bw   =  1/rate + 1/(k·bw)",
                "",
                "              1/bw − 1/(k·bw)  =  1/rate",
                "              (1/bw)(1 − 1/k)  =  1/rate",
                "",
                "              bw*  =  rate·(k − 1)/k        = 250 × 3/4 = 187.5 MB/s",
                "              rate* = bw·k/(k − 1)          = 125 × 4/3 = 166.67 MB/s",
            ]),
            ("p", "Two readings of one equality. Fix the compressor and you get a "
                  "bandwidth: above `187.5 MB/s` &mdash; `1 500 Mbit/s` &mdash; raw is "
                  "faster, so a datacentre link defeats this compressor and a wide-area "
                  "link does not. Fix the link and you get a throughput: on `125 MB/s` "
                  "the compressor must beat `166.67 MB/s`, and many do not."),
            ("example", ("Why the same file gets a different answer on two links",
                         "Send the same `10 GB` over a `10 Gbit/s` link, which is "
                         "`1 250 MB/s`. Raw: `8 s`. Compressed: `40 s` to squeeze plus "
                         "`2 s` to send, which is `42 s`. Compression is now more than "
                         "five times slower, and nothing about the file changed. The "
                         "file never mattered: `1 250 MB/s` is above `bw* = 187.5`, and "
                         "`125 MB/s` is below it.")),
            ("h3", "Where the ratio helps, and where it does not"),
            ("p", "`(k − 1)/k` is `1/2` at `k = 2`, `3/4` at `k = 4` and `9/10` at "
                  "`k = 10`, so it saturates fast. Doubling the ratio from four to eight "
                  "moves the break-even bandwidth from `187.5` to `218.75 MB/s`, a gain "
                  "of `17%`; doubling the compressor&rsquo;s throughput moves it from "
                  "`187.5` to `375 MB/s`. When both are on offer, the faster compressor "
                  "is nearly always the better trade."),
            ("p", "That is the arithmetic behind a decade of compression libraries "
                  "choosing speed over ratio. Past `k = 4` or so, extra ratio buys "
                  "very little on the wire and is usually paid for with a great deal of "
                  "processor time, which enters the plan at full weight."),
            ("h3", "When decompression counts"),
            ("p", "If the receiver has to expand the payload before doing anything with "
                  "it, the far end&rsquo;s time is on the critical path and the "
                  "compressed plan gains a third term, `size/(k·drate)` in the "
                  "compressed domain. The equality is the same shape with that term "
                  "added to the per-byte cost, and it moves the break-even against "
                  "compression. Whether it applies is a question about what the receiver "
                  "does, and it should be answered before the arithmetic rather than "
                  "after."),
            ("p", "One units caution, because it causes more wrong answers here than "
                  "the algebra does. Links are quoted in bits a second and payloads in "
                  "bytes, so a `1 000 Mbit/s` link is `125 MB/s` and a factor of eight "
                  "separates them. On this course `MB/s` is `10⁶` bytes a second and "
                  "`Mbit/s` is `10⁶` bits a second, and the lab divides by eight rather "
                  "than leaving it to be remembered."),
        ],
        "lab": ("scale", {
            "mode": "compress",
            "panel_title": "Set the file, the ratio, the compressor and the link",
            "panel_intro": (
                "Both times are exact fractions. The break-even bandwidth is the "
                "equality solved rather than a curve read off: the size cancels out of "
                "it completely, so how much you are moving decides how long both plans "
                "take and nothing at all about which one wins. Change the file size and "
                "watch the verdict stay exactly where it was."
            ),
        }),
        "steps_title": "Deciding whether to compress a transfer",
        "steps_intro": "Times first so the sizes are concrete, then the break-even so the answer generalises.",
        "steps": [
            ("Put the link and the compressor in the same units",
             "Bytes a second for both. A `1 000 Mbit/s` link is `125 MB/s`, and a "
             "compressor quoted in MB/s is already there. Most wrong answers on this "
             "page are a factor of eight."),
            ("Time both plans at the size you actually have",
             "`size/bw` against `size/rate + size/(k·bw)`. Keep the two stages of the "
             "compressed plan separate, because their shares tell you which of the two "
             "inputs to improve."),
            ("Solve the equality and report `bw*`",
             "`rate·(k − 1)/k`. This is the number worth carrying away, because it is "
             "about the link and the compressor rather than about the file, and it "
             "answers the question for every transfer over that link."),
            ("State the same break-even as a compressor throughput",
             "`bw·k/(k − 1)`. It is the form a library is chosen against: on a "
             "`125 MB/s` link, anything slower than `166.67 MB/s` is making the transfer "
             "worse however good its ratio is."),
            ("Decide whether the far end is on the critical path",
             "If the receiver must expand before it can act, add its time and redo the "
             "comparison. If it stores or forwards the compressed bytes, do not &mdash; "
             "and say which of the two you assumed."),
        ],
        "worked": {
            "title": "10 GB over a gigabit link, compressing 4× at 250 MB/s",
            "intro": [
                "The receiver stores the compressed form, so decompression is not on the "
                "critical path here."
            ],
            "lines": [
                "size 10 GB = 10 000 MB      bw 1 000 Mbit/s = 125 MB/s",
                "k = 4                        rate 250 MB/s",
                "",
                "raw            10 000 ÷ 125          =  80 s",
                "",
                "compressed     squeeze 10 000 ÷ 250  =  40 s",
                "               send     2 500 ÷ 125  =  20 s",
                "               total                 =  60 s",
                "",
                "verdict        compress, 80/60 = 1.33× faster",
                "on the wire    2.5 GB",
                "",
                "break-even:    size/bw = size/rate + size/(k·bw)",
                "               1/bw    = 1/rate + 1/(k·bw)          size gone",
                "               bw*     = rate·(k − 1)/k = 250 × 3/4 = 187.5 MB/s",
                "                                                  = 1 500 Mbit/s",
                "               rate*   = bw·k/(k − 1)  = 125 × 4/3 = 166.67 MB/s",
                "",
                "the same file on a 10 Gbit/s link (1 250 MB/s):",
                "               raw        10 000 ÷ 1 250   =   8 s",
                "               compressed 40 + 2            =  42 s",
                "               verdict    send it raw, by 5.25×",
            ],
            "after": [
                "The line where `size` disappears is the whole lesson. It means the two "
                "blocks at the top and bottom did not need to be computed twice: "
                "`125 MB/s` is below `bw* = 187.5` and `1 250 MB/s` is above it, and "
                "that single comparison decides both cases for every file of every size.",
                "The `66.7%` share of the compressed plan that is the compressor is why "
                "`rate*` is the more actionable form. Ratio is easy to shop for and "
                "throughput is the thing that actually moves the break-even: doubling "
                "`k` from four to eight raises `bw*` by `17%`, and doubling `rate` "
                "doubles it.",
                "For a faded attempt, keep the gigabit link and take a slower, stronger "
                "compressor: `k = 10` at `60 MB/s`. Predict from `rate*` alone which way "
                "the verdict goes before timing anything, then compute both times and "
                "check against the lab."
            ],
        },
        "quiz_title": "Times, links and break-evens",
        "quiz": [
            {"q": "A `10 GB` payload, a `125 MB/s` link, a `250 MB/s` compressor and a ratio of `4`. How long does the compressed plan take?",
             "a": ["`20 s`", "`40 s`", "`60 s`", "`80 s`"],
             "c": 2,
             "why": "`10 000/250 = 40 s` to squeeze plus `2 500/125 = 20 s` to send, "
                    "which is `60 s`. `20 s` is the send stage alone, which omits the "
                    "compressor. `40 s` is the squeeze alone. `80 s` is the raw plan, "
                    "and the comparison is `60` against `80`."},
            {"q": "The same transfer is moved to a `10 Gbit/s` link. What happens to the verdict?",
             "a": ["Compression wins by more, since there are fewer bytes to send",
                   "Raw wins, because `1 250 MB/s` is above `bw* = 187.5 MB/s`",
                   "It is unchanged; the verdict depends on the ratio, not the link",
                   "It depends on the file size"],
             "c": 1,
             "why": "The break-even bandwidth is `rate·(k − 1)/k = 187.5 MB/s`, and "
                    "`1 250 MB/s` is well above it: raw takes `8 s` against `42 s` "
                    "compressed. The link is exactly what the verdict depends on. And "
                    "the file size cancels out of the break-even entirely, which is why "
                    "the same answer holds for every payload on that link."},
            {"q": "Why does the file size not appear in the break-even?",
             "a": ["Because it is small compared with the link speed",
                   "Because every term in both times is proportional to it, so it divides out when they are set equal",
                   "Because compression ratios are independent of size",
                   "Because the break-even is measured per byte by convention"],
             "c": 1,
             "why": "`size/bw = size/rate + size/(k·bw)` has one factor of `size` in "
                    "every term, so dividing through leaves `1/bw = 1/rate + 1/(k·bw)`, "
                    "a relation among three rates. It is an exact cancellation rather "
                    "than an approximation, so it holds for a kilobyte and a petabyte "
                    "alike &mdash; the size decides how long both plans take and nothing "
                    "about which wins."},
            {"q": "On a `125 MB/s` link with a ratio of `4`, what compressor throughput is needed for compression to be worth doing?",
             "a": ["faster than `125 MB/s`", "faster than `166.67 MB/s`", "faster than `187.5 MB/s`", "faster than `500 MB/s`"],
             "c": 1,
             "why": "`rate* = bw·k/(k − 1) = 125 × 4/3 = 166.67 MB/s`. `125 MB/s` is "
                    "the link itself, which would only break even if compression were "
                    "free. `187.5 MB/s` is `bw*`, the break-even bandwidth for a "
                    "`250 MB/s` compressor &mdash; the same equality read in the other "
                    "direction. `500 MB/s` is `bw·k`, which charges the compressor for "
                    "the bytes it emits rather than the bytes it reads."},
        ],
        "mistakes": [
            ("Always compressing",
             "It is a habit from slow links and it inverts on fast ones: the same "
             "`10 GB` that gains `1.33×` on a gigabit link loses by `5.25×` on a "
             "ten-gigabit one. The test is one comparison &mdash; is the link above "
             "`rate·(k − 1)/k`? &mdash; and it is answered once per link rather than "
             "once per transfer."),
            ("Shopping for ratio instead of throughput",
             "`(k − 1)/k` saturates: going from `k = 4` to `k = 8` moves the break-even "
             "bandwidth by `17%`, while doubling the compressor&rsquo;s speed doubles "
             "it. Since the squeeze is two thirds of the compressed plan here, "
             "throughput is where the time actually is."),
            ("Leaving the far end out when it is on the critical path",
             "If the receiver must expand the payload before it can act, its time "
             "belongs in the comparison and it pushes the answer toward sending raw. "
             "Omitting it is correct when the receiver stores or forwards the compressed "
             "bytes, and wrong otherwise &mdash; so the assumption has to be stated "
             "rather than inherited."),
        ],
        "standard": ("Finish when the compress-or-not question is answered for a link rather than for a file.",
                     "You should be able to time both plans in matching units, derive "
                     "`1/bw = 1/rate + 1/(k·bw)` and show the size cancelling, and "
                     "report the break-even both as a bandwidth and as a compressor "
                     "throughput."),
        "note": "Shrinking the bytes is one way to make a transfer cheaper. Not "
                "transferring them is the other, and it is usually worth far more. "
                "&ldquo;Move the Data or the Compute&rdquo; compares shipping a dataset "
                "against shipping the job that reads it, and the comparison turns out "
                "not to contain the bandwidth at all.",
    },
    # ---------------------------------------------------------------- 11
    {
        "slug": "move-the-data-or-the-compute",
        "title": "Move the Data or the Compute",
        "module": "What bytes cost",
        "one_line": "Time both placements of a computation and compute the result-to-input ratio at which they tie.",
        "summary": (
            "Either the data goes to the job or the job goes to the data. Both plans "
            "divide by the same link, so the bandwidth cancels and the comparison is "
            "`code + result` against the whole dataset. Since results are almost always "
            "far smaller than inputs, one side of that wins by orders of magnitude."
        ),
        "key": [
            "move the data       D/bw = 2 TB ÷ 125 MB/s = 16 000 s = 4.44 h",
            "move the compute    (code + result)/bw = 5.2 MB ÷ 125 MB/s = 41.6 ms",
            "384 615× apart, and bw divides both sides:",
            "     the comparison is   code + result   against   D",
            "result/input = 5 MB / 2 TB = 1/400 000",
            "the two plans tie at 2 TB of result, which is the whole dataset",
        ],
        "key_label": "Two placements, and a comparison with no link in it",
        "concepts_intro": (
            "One ratio decides this, and the reason the answer is usually so lopsided is "
            "that the ratio is usually tiny."
        ),
        "concepts": [
            ("Both plans cross the same link, so it cancels",
             "`D/bw` against `(code + result)/bw`. The bandwidth divides both sides, so "
             "the comparison reduces to `code + result` against `D` &mdash; bytes "
             "against bytes. A faster link changes how long both plans take and nothing "
             "at all about which of them is quicker, which makes this the most portable "
             "decision on the course."),
            ("The result-to-input ratio is the whole question",
             "The plans tie when `code + result = D`, and since code is negligible that "
             "is when the result is the size of the dataset. Here the result is `5 MB` "
             "against `2 TB`, a ratio of `1/400 000`, so moving the compute wins by "
             "`384 615×`. Aggregations, filters and counts all produce ratios in that "
             "region, which is why the answer is so consistent."),
            ("This is why query languages exist",
             "Sending `SELECT count(*) …` instead of the table is exactly this "
             "arithmetic, and so is a stored procedure, a map-reduce job, an edge "
             "function and a pushdown predicate. Each is a mechanism for shipping a "
             "small amount of code to where a large amount of data already is, and each "
             "is worth precisely the ratio above."),
        ],
        "read_title": "Two placements, the cancellation, and the ratio that decides",
        "read_intro": (
            "Where each time comes from, why the link drops out, and the cases in which "
            "the usual answer is the wrong one."
        ),
        "body": [
            ("def", ("The two placements",
                     "For a computation over a dataset of `D` bytes that emits `result` "
                     "bytes, with `code` bytes of program, across a link of `bw` bytes a "
                     "second:",
                     "<strong>move the data</strong> takes `D/bw`;",
                     "<strong>move the compute</strong> takes `(code + result)/bw`.",
                     "The processing itself is assumed to take the same time wherever it "
                     "runs, so it appears on both sides and cancels with the "
                     "bandwidth.")),
            ("math", [
                "D = 2 TB = 2 000 000 MB     result = 5 MB     code = 200 kB",
                "bw = 1 000 Mbit/s = 125 MB/s",
                "",
                "move the data       2 000 000 ÷ 125   = 16 000 s  =  4.44 h",
                "move the compute          5.2 ÷ 125    = 0.0416 s  =  41.6 ms",
                "",
                "ratio of the two    16 000/0.0416      = 384 615.4×",
                "result/input        5 MB / 2 TB        = 1/400 000",
                "",
                "the tie             code + result = D  ⟹  result ≈ 2 TB",
            ]),
            ("p", "`4.44` hours against `41.6` milliseconds is not a close call, and "
                  "the gap is not a property of this link. Put both plans on a "
                  "connection a hundred times faster and they become `160` seconds and "
                  "`0.42` milliseconds &mdash; the same factor of `384 615`, because "
                  "both numerators were divided by the same thing."),
            ("h3", "The cancellation, written out"),
            ("p", "It is worth doing explicitly, because the conclusion that a faster "
                  "network does not change the decision is counter-intuitive enough to "
                  "need the algebra rather than the assertion."),
            ("math", [
                "move the compute is faster when",
                "",
                "        (code + result)/bw   <   D/bw",
                "",
                "multiply both sides by bw > 0:",
                "",
                "         code + result       <   D",
                "",
                "no bandwidth anywhere: the decision is bytes against bytes,",
                "and the link only sets how long the winner takes.",
            ]),
            ("example", ("A count over two terabytes",
                         "The dataset is `2 TB`; the job is a few hundred kilobytes of "
                         "code; the answer is a single number. Moving the data takes "
                         "`4.44` hours and moving the compute takes `41.6` milliseconds, "
                         "and the ratio `1/400 000` is generous &mdash; a count returns "
                         "a few bytes, so the true ratio is nearer `10⁻¹²`. Every "
                         "database that pushes a predicate down to the storage layer is "
                         "making this comparison implicitly.")),
            ("h3", "When the usual answer is wrong"),
            ("p", "The comparison inverts exactly when the result is not small. A job "
                  "that decompresses, joins or enriches can emit more than it reads, and "
                  "then `code + result > D` and the data should come to the compute "
                  "&mdash; or, better, the job should be split so that the reducing part "
                  "runs next to the data and only its output travels."),
            ("p", "There are also constraints that are not about time at all. The data "
                  "may not be allowed to leave its jurisdiction, in which case the "
                  "compute moves regardless of sizes; or the code may not be allowed to "
                  "run next to the data, in which case it cannot move whatever the "
                  "arithmetic says. Both are constraints applied before this "
                  "calculation, not terms inside it."),
            ("p", "The third case is repetition. One transfer of `2 TB` followed by a "
                  "thousand local queries is a different plan from a thousand remote "
                  "queries, and the comparison to make is `D` against "
                  "`1 000 × (code + result)`. That is still bytes against bytes, with "
                  "the same cancellation; only the counts changed."),
            ("p", "The assumption that the processing takes the same time in both places "
                  "is the one this model leans on, and it is the one to check. If the "
                  "data&rsquo;s home is a storage tier with little processor beside it, "
                  "moving the compute there may be slower in total even though it moves "
                  "almost no bytes &mdash; and then the right answer is the one the "
                  "measurement gives rather than the one the ratio suggests."),
        ],
        "lab": ("scale", {
            "mode": "placement",
            "panel_title": "Set the dataset, the result, the code and the link",
            "panel_intro": (
                "Both times are exact. The crossing is `code + result` against the "
                "dataset &mdash; the bandwidth divides both sides and cancels &mdash; so "
                "a faster link changes how long both plans take and nothing about which "
                "of them wins. Grow the result toward the size of the dataset and watch "
                "the verdict flip at the only place it can."
            ),
        }),
        "steps_title": "Placing a computation",
        "steps_intro": "Three sizes and a comparison. The link is needed only to turn the answer into a duration.",
        "steps": [
            ("Write down the three byte counts",
             "The dataset, the result and the code. Do not start with the link: it "
             "cancels, and reaching for it first is what makes people believe a network "
             "upgrade could change the answer."),
            ("Compare `code + result` with `D`",
             "That is the decision, in bytes. Here `5.2 MB` against `2 TB`, which is not "
             "close, and the verdict is stable against anything the network does."),
            ("Report the result-to-input ratio",
             "`result/D`, as a fraction. `1/400 000` here. It is the number that says "
             "how safe the verdict is: a ratio near one is a case worth re-examining, "
             "and a ratio of `10⁻⁶` is not."),
            ("Divide by the link only to state the durations",
             "`4.44 h` and `41.6 ms`. These are what a reader remembers, and they are "
             "downstream of a decision that was already made, so present them in that "
             "order."),
            ("Check the constraints and the repetition count",
             "Jurisdiction and where code is allowed to run override the arithmetic. "
             "Repetition changes which side is multiplied: one big transfer against "
             "`n` small ones is the same comparison with a count in it."),
        ],
        "worked": {
            "title": "An aggregation over a 2 TB table, returning 5 MB",
            "intro": [
                "The job is 200 kB of code, the link is a gigabit, and the processing "
                "time is taken to be the same wherever it runs."
            ],
            "lines": [
                "D      = 2 TB    = 2 000 000 MB",
                "result = 5 MB",
                "code   = 200 kB  = 0.2 MB",
                "bw     = 1 000 Mbit/s = 125 MB/s",
                "",
                "decide first, in bytes:",
                "   code + result = 5.2 MB      against      D = 2 000 000 MB",
                "   ⟹ move the compute, by a factor of 384 615",
                "",
                "then state the durations:",
                "   move the data     2 000 000 ÷ 125 = 16 000 s = 4.44 h",
                "   move the compute        5.2 ÷ 125 = 0.0416 s = 41.6 ms",
                "",
                "result-to-input    5 MB / 2 TB = 1/400 000",
                "                   (the panel shows this rounded, as 0.0003%)",
                "",
                "the tie            code + result = D",
                "                   ⟹ result = 2 TB − 200 kB ≈ 2 TB of result",
                "",
                "a 100× faster link:   160 s   against   0.42 ms",
                "                      still 384 615× apart",
            ],
            "after": [
                "The order of the two blocks is the method. The decision is taken in "
                "bytes, where the link does not appear; the durations are then computed "
                "from it, and they are the only place the link is used at all.",
                "The last block is the claim worth defending. A hundredfold faster "
                "network divided both numerators by a hundred and left the ratio exactly "
                "where it was. Bandwidth buys you a faster winner, never a different "
                "one.",
                "For a faded attempt, keep the `2 TB` table and make the job emit "
                "`1.5 TB` &mdash; a decompressing scan rather than an aggregation. "
                "Predict from `code + result` against `D` which side wins before timing "
                "anything, compute both durations, and say what result size would have "
                "made it a tie."
            ],
        },
        "quiz_title": "Placements, ratios and the link that cancels",
        "quiz": [
            {"q": "A `2 TB` dataset, a `5 MB` result, `200 kB` of code and a `125 MB/s` link. Which plan is faster and by roughly how much?",
             "a": ["Move the data, by about `4.44 h`", "Move the compute, by a factor of about `384 615`", "They are within an order of magnitude of each other", "It depends on how fast the link is"],
             "c": 1,
             "why": "`16 000 s` against `0.0416 s` is a factor of `384 615`. Moving the "
                    "data is the slower plan, and `4.44 h` is how long it takes rather "
                    "than a margin. The link does not decide it: it divides both times "
                    "equally, so the factor is the same on any connection."},
            {"q": "The link is upgraded from `1 Gbit/s` to `100 Gbit/s`. What happens to the comparison?",
             "a": ["Moving the data becomes competitive, since the dataset now transfers quickly",
                   "Nothing: `bw` divides both sides, so the ratio is unchanged at `384 615`",
                   "Moving the compute wins by more, since the result is smaller",
                   "The comparison has to be redone from the byte counts"],
             "c": 1,
             "why": "Both plans divide by the same `bw`, so it cancels out of the "
                    "comparison entirely: `160 s` against `0.42 ms` is the same factor. "
                    "A faster link makes both plans quicker and neither one "
                    "relatively better, which is why the decision is made in bytes and "
                    "the link is used only to state durations."},
            {"q": "A job reads `2 TB` and emits `3 TB`, decompressing as it goes. Where should it run?",
             "a": ["Next to the data, as always",
                   "Next to the consumer: `code + result` exceeds `D`, so moving the data is the cheaper transfer",
                   "Either way; the totals are close enough not to matter",
                   "Next to the data, but only if the link is slow"],
             "c": 1,
             "why": "The rule is `code + result` against `D`, and here `3 TB` beats "
                    "`2 TB`, so shipping the input is the smaller transfer. This is the "
                    "case the usual advice gets wrong, and it is not close &mdash; a "
                    "terabyte apart. The link is irrelevant to the verdict, as always."},
            {"q": "At what result size do the two plans tie, for a `2 TB` dataset and `200 kB` of code?",
             "a": ["`5 MB`", "`1 TB`", "just under `2 TB`", "It depends on the bandwidth"],
             "c": 2,
             "why": "They tie when `code + result = D`, so `result = 2 TB − 200 kB`, "
                    "which is `2 TB` to any useful precision. `5 MB` is this "
                    "example&rsquo;s actual result, which is `400 000` times below the "
                    "tie. `1 TB` would still favour moving the compute, by a factor of "
                    "two. And bandwidth cancels, so it cannot move the crossing."},
        ],
        "mistakes": [
            ("Pulling everything to the client",
             "It is the default because it is the easiest thing to write, and on this "
             "example it is `4.44` hours instead of `41.6` milliseconds. The error is "
             "about the result-to-input ratio rather than about bandwidth: it is wrong "
             "exactly when the result is smaller than the input, which is nearly "
             "always."),
            ("Believing a faster link will fix it",
             "`bw` divides both plans, so it cancels out of the comparison completely. A "
             "hundredfold upgrade turns `4.44 h` into `160 s` and leaves the other plan "
             "`384 615` times quicker still. Buying bandwidth to avoid moving a "
             "computation is paying to lose the same argument faster."),
            ("Forgetting the processing time is assumed equal",
             "The model cancels the computation itself because it assumes it costs the "
             "same in both places. A storage tier with little processor beside it breaks "
             "that assumption, and there the plan that moves almost no bytes can still "
             "be slower overall. The ratio says where the bytes should go, not where the "
             "work will be fast."),
        ],
        "standard": ("Finish when a placement decision is made in bytes and the link is used only to report durations.",
                     "You should be able to compare `code + result` with `D`, show the "
                     "bandwidth cancelling from the inequality, report the "
                     "result-to-input ratio as a fraction, and name the result size at "
                     "which the two plans would tie."),
        "note": "That closes the course: what another machine buys, what a shape costs, "
                "the three ways capacity is paid for, and the break-evens about moving "
                "bytes. Every one of them was an equality located exactly rather than a "
                "rule of thumb, and the one figure that had to be rounded &mdash; the "
                "square root in the Universal Scalability Law&rsquo;s peak &mdash; was "
                "printed beside the integer it glosses. &ldquo;Measuring Systems&rdquo; "
                "asks the question all of this has been deferring: how would you know "
                "any of these numbers from a system that is actually running?",
    },
]
