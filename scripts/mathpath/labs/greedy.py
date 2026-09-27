"""Greedy Algorithms and Matroids -- course 4's kit, seven modes.

WHAT THIS KIT PROVES, AND WHAT IT ONLY MEASURES. Every other kit on this path
puts a measured count beside a proved bound. This one can do better, and the
reason is the whole shape of the course: a greedy rule commits to a choice and
never revisits it, so on a small instance the OPTIMUM IS ENUMERABLE and the
claim "greedy is optimal here" stops being a claim. Every mode below runs the
greedy rule and, beside it, an exhaustive search that has never heard of the
rule:

    intervals   every subset of the intervals, ORACLE_JS.bruteOptimal
    partition   every instant a start time falls on, for the depth
    huffman     every full binary tree on n leaves AND every assignment of the
                weights to its leaves
    knapsack    every subset of the items, ORACLE_JS.knapsackBrute
    matroid     every subset of the ground set, from the independence oracle,
                and then every weighting in {1,2,3}^n until greedy loses
    stable      every one of the n! perfect matchings, filtered by the
                blocking-pair test
    caching     every eviction decision, memoised on (position, cache)

So the figure a reader is asked to trust is never "greedy got 4". It is
"greedy got 4 and the best of the 512 subsets is 4", or "greedy got 3 and the
best of the 512 is 4, and here is the subset". A rule that is wrong is shown
losing on a named instance rather than described as heuristic.

NOTHING HERE IS ROUNDED, and two quantities are genuinely fractional. The
expected codeword length of a Huffman code is (total bits)/(total weight) and
the fractional knapsack's optimum is a sum of rationals; both are exact over
RATIONAL_JS's BigInt pairs and both are printed as fractions first. `Rfixed`
renders a decimal beside the fraction where a decimal reads better, and that
decimal is a rounding of the PRINTING, at a stated number of places -- the
fraction next to it is the number. Everything else on these pages is an
integer count.

WHAT IS REUSED AND WHAT THIS KIT ADDS. `algo_core.GREEDY_JS` holds the
algorithms -- greedyIntervals, greedyTrace, partitionRooms, depthOf,
huffmanBuild, codeCost, allFullBinaryTrees, shapeCost, fractionalKnapsack,
independenceEnumerate, exchangeTest, matroidGreedy, galeShapley,
blockingPairs -- and nothing here reimplements one. `caching` has no algorithm
of its own at all: `sysdesign_core.replayPolicy` already implements FIFO, LRU
and farthest-in-future on a reference trace, and it is reused exactly as it
ships. What this kit adds is the CHECKING, and each piece exists because the
corresponding claim was otherwise unverifiable:

  intervalsDisjoint   a selection is tested for feasibility before its size is
                      printed. A rule that returned a big number by choosing
                      overlapping intervals would otherwise look like the
                      winner, and the size alone cannot tell you.
  exchangeChain       the exchange argument EXECUTED: start from an optimum,
                      swap greedy's i-th choice in at position i, and check
                      after every swap that the set is still feasible and still
                      the same size. On the earliest-finish rule it survives
                      every swap; on the others it breaks at a named step, and
                      the step is where the textbook proof stops working.
  roomsValid          every room's intervals are pairwise disjoint and every
                      input interval appears in exactly one room.
  liveAt              the intervals alive at the instant that attains the
                      depth -- the certificate that no schedule uses fewer
                      rooms, listed rather than asserted.
  codesPrefixFree     checked pairwise. Huffman's tree makes it true by
                      construction and a check that trusts the construction
                      checks nothing.
  encodeSyms/
  decodeBits          the round trip. A message is encoded to bits and decoded
                      back, and the mode prints the decoded message, so a code
                      that is short and wrong cannot look like a code that is
                      short and right.
  huffmanBruteBits    the minimum total bits over every shape AND every
                      assignment of the weights to its leaves. `shapeCost`
                      places the heaviest weight on the shallowest leaf, which
                      is the rearrangement inequality and therefore a claim;
                      this enumerates the assignments instead, so the two check
                      each other.
  greedyKnapsack01    the three 0/1 greedy rules -- by density, by value, by
                      lightest -- each against knapsackBrute. `fractionalKnapsack`
                      ships the fractional optimum and the 0/1 optimum but no
                      0/1 GREEDY, and the lesson of the course is the gap
                      between the rule and the optimum, not between two optima.
  halfGuarantee       the better of (density greedy, the most valuable single
                      item that fits), which is at least half the optimum on
                      every instance. Both halves computed, the ratio exact.
  forestOracle,
  partitionOracle,
  uniformOracle,
  matchingOracle      four families as INDEPENDENCE ORACLES, because that is
                      the definition. Three are matroids; the matchings of a
                      path are not, and which is which is computed by
                      exchangeTest rather than labelled here.
  downwardClosed      greedy needs an independence system before it needs a
                      matroid, and those are different conditions.
  beatingWeights      Rado and Edmonds say greedy is optimal for EVERY
                      weighting exactly when the family is a matroid, so on a
                      family that is not one a bad weighting must exist. This
                      searches {1,2,3}^n and returns the first, which makes the
                      counterexample reproducible instead of quoted.
  everyStableMatching every one of the n! matchings, filtered by blockingPairs,
                      with each proposer's best and worst ACHIEVABLE partner
                      over the stable ones -- the fact proposer-optimality is
                      about, computed without running Gale-Shapley.
  everyEviction       the largest number of hits any offline demand-paging
                      policy can get, by searching every eviction decision with
                      a memo on (position, cache contents). replayPolicy's
                      'opt' arm is then a number to compare against, not a
                      number to trust.
  beladySweep         FIFO's hit count as the cache grows, so the anomaly is a
                      row a reader sees rather than a curiosity they are told
                      about.

ONE OBSERVATION ABOUT A ROUTINE THIS KIT DOES NOT OWN. `greedyIntervals`'s
`fewestConflicts` arm sorts ONCE, by the number of conflicts each interval has
in the full instance, and then sweeps; the rule as usually stated recomputes
the conflict counts after each removal. The shipped arm is the static-order
variant, both fail, and the `intervals` mode says which one it ran rather than
naming the other. It is described here so nobody reads the label and assumes
the other algorithm.

THE MODES, and the lesson each belongs to:

  intervals   the four rules, each checked feasible, each against the optimum,
              and the exchange argument run swap by swap
  partition   rooms against the depth, and the instant that certifies it
  huffman     the merge sequence, the tree, the exact expected length, the
              round trip, and the minimum over every shape
  knapsack    fractional exactly, 0/1 greedy three ways, the 0/1 optimum, and
              the half-guarantee
  matroid     four families from their oracles, the exchange property pair by
              pair, and the weighting that beats greedy on the one that is not
  stable      the proposal sequence, an empty blocking-pair list, every stable
              matching, and who the asymmetry favours
  caching     FIFO, LRU and farthest-in-future against the true offline
              optimum, and Belady's anomaly swept

PAGE WEIGHT, MEASURED RATHER THAN ESTIMATED. The core is concatenated once for
the kit rather than once per mode, which is what `heap.py` does and for the
same reason: a mode that built its own core would eventually call a function
its page turned out not to carry. The core is 71.4 KB raw and 21.0 KB gzipped,
and a rendered lesson page runs from 40.4 KB gzipped (`partition`) to 41.8 KB
(`matroid`) against this repository's measured ceiling of 62 KB (AGENTS.md).

The cost of the one-core choice is real here and is written down rather than
waved at. `caching` uses nothing at all from TREEDRAW_JS or GREEDY_JS, and
carries 19.1 KB raw -- 5.3 KB gzipped, an eighth of its page -- of them anyway.
That is accepted rather than optimised, because the page still lands at 40.8 KB
against 62 and because splitting the core is exactly the change that lets a
mode call a function its page does not have. If the ceiling ever binds,
`caching` is the first mode to give a core of its own: TREEDRAW_JS is used by
`huffman` alone, and GREEDY_JS by every mode except `caching`.
"""

from .algebra_core import RATIONAL_JS
from .algo_core import COUNT_JS, GREEDY_JS, ORACLE_JS, RFIXED_JS, TREEDRAW_JS
from .common import Lab
from .sysdesign_core import REPLAY_JS

# ---------------------------------------------------------------------------
# The arithmetic this kit adds. Top-level functions, no element touched, so
# scripts/mathcheck.js executes exactly the source that ships.
# ---------------------------------------------------------------------------

GKIT_JS = r"""
  /* =================================================== what a reader types

     An interval is `s-f`: two integers, the half-open span [s, f). Labels are
     A, B, C ... in the order typed and they are what every table and every
     drawing names, so one interval can be followed through four different
     orderings of the same instance. */
  function gyLabel(i) { return String.fromCharCode(65 + (i % 26)); }

  function gyParseIntervals(text, cap) {
    cap = cap === undefined ? 9 : cap;
    var items = [], bad = null;
    String(text).split(',').forEach(function (piece) {
      var t = piece.replace(/\s+/g, '');
      if (!t || bad) return;
      var m = /^(\d+)-(\d+)$/.exec(t);
      if (!m) { bad = 'an interval is written start-finish, as 3-8; "' + t + '" is not'; return; }
      var s = parseInt(m[1], 10), f = parseInt(m[2], 10);
      if (!(f > s)) { bad = t + ' does not finish after it starts'; return; }
      if (items.length >= cap) {
        bad = 'this mode tries every subset, so it takes at most ' + cap + ' intervals';
        return;
      }
      items.push({ s: s, f: f, label: gyLabel(items.length) });
    });
    if (!bad && !items.length) bad = 'no intervals were read';
    return { items: items, bad: bad };
  }

  function gyParseFreqs(text, cap) {
    cap = cap === undefined ? 8 : cap;
    var out = [], bad = null, seen = {};
    String(text).split(',').forEach(function (piece) {
      var t = piece.replace(/\s+/g, '');
      if (!t || bad) return;
      var m = /^([A-Za-z0-9_]+):(\d+)$/.exec(t);
      if (!m) { bad = 'a symbol is written name:weight, as a:45; "' + t + '" is not'; return; }
      var w = parseInt(m[2], 10);
      if (w <= 0) { bad = 'the weight of ' + m[1] + ' has to be positive'; return; }
      if (seen[m[1]]) { bad = m[1] + ' appears twice'; return; }
      if (out.length >= cap) { bad = 'at most ' + cap + ' symbols, so the tree stays readable'; return; }
      seen[m[1]] = true;
      out.push({ symbol: m[1], weight: w });
    });
    if (!bad && out.length < 2) bad = 'a code needs at least two symbols';
    return { freqs: out, bad: bad };
  }

  function gyParseItems(text, cap) {
    cap = cap === undefined ? 10 : cap;
    var out = [], bad = null;
    String(text).split(',').forEach(function (piece) {
      var t = piece.replace(/\s+/g, '');
      if (!t || bad) return;
      var m = /^(\d+)\/(\d+)$/.exec(t);
      if (!m) { bad = 'an item is written weight/value, as 20/100; "' + t + '" is not'; return; }
      var w = parseInt(m[1], 10), v = parseInt(m[2], 10);
      if (w <= 0) { bad = 'an item of weight 0 has no density, and would be free'; return; }
      if (out.length >= cap) {
        bad = 'at most ' + cap + ' items, because the optimum here is the best of 2^n subsets';
        return;
      }
      out.push({ w: w, v: v, label: gyLabel(out.length) });
    });
    if (!bad && !out.length) bad = 'no items were read';
    return { items: out, bad: bad };
  }

  /* Preference rows, one per line, semicolon separated, 1-based. A row that is
     not a ranking of ALL the partners is refused rather than padded: a partial
     ranking is a different problem with a different theorem. */
  function gyParsePrefs(text) {
    var rows = [], bad = null;
    String(text).split(';').forEach(function (piece) {
      var t = piece.trim();
      if (!t || bad) return;
      var nums = t.split(/[\s,]+/).map(function (x) { return parseInt(x, 10); });
      if (nums.some(function (x) { return !isFinite(x); })) {
        bad = '"' + t + '" is not a list of numbers';
        return;
      }
      rows.push(nums.map(function (x) { return x - 1; }));
    });
    if (bad) return { rows: null, bad: bad };
    if (rows.length < 2) return { rows: null, bad: 'at least two rows are needed' };
    var n = rows.length;
    for (var i = 0; i < n; i += 1) {
      var sorted = rows[i].slice().sort(function (a, b) { return a - b; });
      if (sorted.length !== n || sorted.some(function (x, k) { return x !== k; })) {
        return { rows: null, bad: 'row ' + (i + 1) + ' is not a ranking of all ' + n + ' partners' };
      }
    }
    return { rows: rows, bad: null };
  }

  function gyParseTrace(text, cap) {
    cap = cap === undefined ? 20 : cap;
    var out = [], bad = null;
    String(text).split(/[\s,]+/).forEach(function (t) {
      if (!t || bad) return;
      var v = parseInt(t, 10);
      if (!isFinite(v) || String(v) !== t || v < 1 || v > 20) {
        bad = '"' + t + '" is not a page number between 1 and 20';
        return;
      }
      if (out.length >= cap) {
        bad = 'at most ' + cap + ' references, because every eviction decision is searched';
        return;
      }
      out.push(v);
    });
    if (!bad && !out.length) bad = 'no references were read';
    return { trace: out, bad: bad };
  }

  /* Every permutation of a list, used by three oracles below. */
  function gyPermute(list, fn) {
    var n = list.length, cur = [], used = [];
    for (var i = 0; i < n; i += 1) used.push(false);
    (function step() {
      if (cur.length === n) { fn(cur); return; }
      for (var k = 0; k < n; k += 1) {
        if (used[k]) continue;
        used[k] = true; cur.push(list[k]);
        step();
        cur.pop(); used[k] = false;
      }
    })();
  }

  /* ================================================== intervals: scheduling

     A selection's SIZE is what every rule is judged on, and a size means
     nothing until the selection is known to be feasible. So nothing here
     prints a size it has not first run through this. */
  function intervalsDisjoint(sel) {
    var a = sel.slice().sort(function (x, y) { return x.s - y.s || x.f - y.f; });
    for (var i = 1; i < a.length; i += 1) if (a[i].s < a[i - 1].f) return false;
    return true;
  }
  function gyByFinish(a, b) { return a.f - b.f || a.s - b.s; }
  function gyNames(sel) { return sel.map(function (x) { return x.label; }).join(' '); }

  /* The optimum, over every subset. bruteOptimal maximises an objective that
     returns null for an infeasible set, and the feasibility test it is handed
     is the same one the panel uses on greedy's answer. */
  function intervalOptimum(items) {
    return bruteOptimal(items, function (members) {
      var sel = members.map(function (i) { return items[i]; });
      return intervalsDisjoint(sel) ? sel.length : null;
    });
  }
  var GY_RULES = ['earliestFinish', 'earliestStart', 'shortest', 'fewestConflicts'];
  function ruleReport(items) {
    var opt = intervalOptimum(items), rows = [];
    GY_RULES.forEach(function (rule) {
      var run = greedyIntervals(items, rule);
      rows.push({ rule: rule, chosen: run.chosen, size: run.chosen.length,
                  feasible: intervalsDisjoint(run.chosen),
                  optimal: run.chosen.length === opt.result.value,
                  short: opt.result.value - run.chosen.length,
                  compares: run.counts.compares || 0 });
    });
    return { rows: rows, optimum: opt.result.value,
             best: opt.result.members.map(function (i) { return items[i]; }).sort(gyByFinish),
             subsets: opt.counts.nodes, feasibleSets: opt.counts.calls };
  }

  /* THE EXCHANGE ARGUMENT, EXECUTED.

     The textbook proof takes an optimal solution, sorted by finish time, and
     replaces its i-th interval by greedy's i-th, arguing that the result is
     still feasible and still the same size. That argument is two checkable
     properties, so this performs the swaps and checks both after every one of
     them. Under the earliest-finish rule every swap survives and the optimum
     is transformed into greedy's own answer. Under a rule that is wrong the
     chain breaks -- either the set stops being feasible, or greedy's choice
     was already further down the list and the swap loses an interval -- and
     the step it breaks at is the step the proof cannot take. */
  function exchangeChain(items, rule) {
    var g = greedyIntervals(items, rule).chosen.slice().sort(gyByFinish);
    var opt = intervalOptimum(items);
    var start = opt.result.members.map(function (i) { return items[i]; }).sort(gyByFinish);
    var cur = start.slice(), steps = [], matched = 0;
    for (var i = 0; i < g.length && i < cur.length; i += 1) {
      var out = cur[i], dup = false;
      if (out !== g[i]) {
        cur = cur.slice();
        cur[i] = g[i];
        var j = cur.indexOf(g[i], i + 1);
        if (j > i) { cur.splice(j, 1); dup = true; }
      } else {
        out = null;
      }
      steps.push({ step: i + 1, into: g[i], out: out, duplicate: dup,
                   set: cur.slice(), feasible: intervalsDisjoint(cur),
                   size: cur.length, kept: cur.length === start.length });
    }
    for (i = 0; i < g.length && i < cur.length; i += 1) if (cur[i] === g[i]) matched += 1;
    var survived = steps.length > 0 && steps.every(function (s) { return s.feasible && s.kept; });
    return { start: start, steps: steps, end: cur, survived: survived, matched: matched,
             greedy: g, optimum: opt.result.value, size: cur.length };
  }

  /* ================================================ partitioning into rooms

     depthOf samples the START instants, which is right because the number of
     live intervals can only go up at a start; this sweeps the same instants
     and lists WHICH intervals are alive at the one that attains the maximum.
     That list is the certificate: those intervals pairwise overlap, so no
     schedule of any kind uses fewer rooms than there are of them. */
  function liveAt(items, t) {
    return items.filter(function (x) { return x.s <= t && t < x.f; });
  }
  function roomsValid(rooms, items) {
    var seen = [], disjoint = true;
    rooms.forEach(function (r) {
      if (!intervalsDisjoint(r)) disjoint = false;
      r.forEach(function (x) { seen.push(x); });
    });
    var covers = seen.length === items.length
      && items.every(function (x) { return seen.indexOf(x) !== -1; });
    return { disjoint: disjoint, covers: covers, ok: disjoint && covers, placed: seen.length };
  }
  /* Those live intervals pairwise overlap, which is what makes them a lower
     bound rather than a coincidence. Checked, because "they all contain the
     same instant" is the reason and the panel should be showing the reason. */
  function mutuallyOverlapping(sel) {
    for (var i = 0; i < sel.length; i += 1)
      for (var j = i + 1; j < sel.length; j += 1)
        if (!(sel[i].s < sel[j].f && sel[j].s < sel[i].f)) return false;
    return true;
  }

  /* ================================================================ Huffman */
  function codesPrefixFree(codes) {
    var list = Object.keys(codes).map(function (k) { return codes[k]; });
    for (var i = 0; i < list.length; i += 1)
      for (var j = 0; j < list.length; j += 1)
        if (i !== j && list[j].indexOf(list[i]) === 0) return false;
    return true;
  }
  function encodeSyms(codes, syms) {
    var out = '';
    for (var i = 0; i < syms.length; i += 1) {
      if (codes[syms[i]] === undefined) return null;
      out += codes[syms[i]];
    }
    return out;
  }
  /* Decoding takes the first codeword the buffer matches, which is only
     unambiguous BECAUSE the code is prefix-free. So the round trip is the
     property itself, run: a code that is short and wrong fails here. */
  function decodeBits(codes, bits) {
    var inv = {}, out = [], buf = '';
    Object.keys(codes).forEach(function (s) { inv[codes[s]] = s; });
    for (var i = 0; i < bits.length; i += 1) {
      buf += bits.charAt(i);
      if (inv[buf] !== undefined) { out.push(inv[buf]); buf = ''; }
    }
    return buf.length ? null : out;
  }
  /* The minimum total bits over every full binary tree on n leaves AND every
     assignment of the weights to its leaves. Catalan(n-1) shapes times n!
     assignments: 42 x 720 at six leaves, which is the cap. */
  function huffmanBruteBits(weights, cap) {
    cap = cap === undefined ? 6 : cap;
    oracleCap('huffmanBruteBits', weights.length, cap);
    var shapes = allFullBinaryTrees(weights.length, cap), best = null, tried = 0, bestDepths = null;
    shapes.forEach(function (shape) {
      var depths = [];
      (function walk(nd, d) {
        if (nd.leaf) { depths.push(d); return; }
        walk(nd.l, d + 1); walk(nd.r, d + 1);
      })(shape, 0);
      gyPermute(weights, function (perm) {
        tried += 1;
        var t = 0n;
        for (var i = 0; i < depths.length; i += 1) t += BigInt(depths[i]) * BigInt(perm[i]);
        if (best === null || t < best) { best = t; bestDepths = depths.slice(); }
      });
    });
    return { bits: best, shapes: shapes.length, assignments: tried, depths: bestDepths };
  }
  /* The fixed-length code the saving is measured against, and the two
     totals, so the panel never divides two numbers it did not print. */
  function codeLengths(codes) {
    var out = {};
    Object.keys(codes).forEach(function (s) { out[s] = codes[s].length; });
    return out;
  }

  /* ============================================================== knapsack */
  var GY_KNAP_RULES = {
    density: function (a, b) {
      return -Rcmp(R(BigInt(a.v), BigInt(a.w)), R(BigInt(b.v), BigInt(b.w))) || a.i - b.i;
    },
    value: function (a, b) { return b.v - a.v || a.i - b.i; },
    light: function (a, b) { return a.w - b.w || a.i - b.i; }
  };
  /* 0/1 greedy: sort, then take each item if it still fits. The density
     comparison is Rcmp on exact fractions and never v/w as a double, because
     two items whose densities differ in the fifteenth place would otherwise
     be ordered by rounding error. */
  function greedyKnapsack01(items, W, rule) {
    var cmp = GY_KNAP_RULES[rule];
    if (!cmp) throw new Error('unknown rule: ' + rule);
    var order = items.map(function (it, i) {
      return { i: i, w: it.w, v: it.v, label: it.label === undefined ? gyLabel(i) : it.label,
               d: R(BigInt(it.v), BigInt(it.w)) };
    });
    order.sort(cmp);
    var c = counter(), left = W, value = 0, picks = [], trace = [];
    order.forEach(function (it) {
      c.compares += 1;
      var fits = it.w <= left;
      if (fits) { left -= it.w; value += it.v; picks.push(it.i); }
      trace.push({ at: trace.length, item: it, taken: fits, left: left });
    });
    picks.sort(function (a, b) { return a - b; });
    return runOf({ value: value, weight: W - left, left: left, picks: picks, order: order },
                 usedCounts(c), trace);
  }
  /* The weight and value of a set of indices, so a reported value is checked
     against the items rather than accumulated and trusted. */
  function packValue(items, picks) {
    var w = 0, v = 0;
    picks.forEach(function (i) { w += items[i].w; v += items[i].v; });
    return { w: w, v: v };
  }
  /* Density greedy alone has no guarantee at all: skip one heavy, valuable
     item and the ratio is unbounded. The better of (density greedy, the most
     valuable single item that fits) does: its value is at least half the
     optimum, on every instance. Both halves are computed. */
  function halfGuarantee(items, W) {
    var g = greedyKnapsack01(items, W, 'density');
    var best = 0, at = -1;
    items.forEach(function (it, i) { if (it.w <= W && it.v > best) { best = it.v; at = i; } });
    var took = g.result.value >= best ? 'greedy' : 'single';
    return { greedy: g.result.value, single: best, at: at,
             value: Math.max(g.result.value, best), took: took };
  }
  function gyRatio(got, opt) {
    return opt === 0 ? R(1n, 1n) : R(BigInt(got), BigInt(opt));
  }

  /* ============================================================== matroids

     A family is given by a membership test on a subset, because that is the
     definition. independenceEnumerate turns the oracle into the family, and
     exchangeTest then tries every ordered pair. Four families ship and which
     of them are matroids is a verdict the page computes. */
  function uniformOracle(k) { return function (m) { return m.length <= k; }; }
  function partitionOracle(groups, caps) {
    return function (m) {
      var n = [], i;
      for (i = 0; i < caps.length; i += 1) n.push(0);
      for (i = 0; i < m.length; i += 1) n[groups[m[i]]] += 1;
      for (i = 0; i < caps.length; i += 1) if (n[i] > caps[i]) return false;
      return true;
    };
  }
  /* The graphic matroid: a set of edges is independent when it holds no cycle.
     Union-find is written out because the content of the mode is that Kruskal
     IS this greedy and not an algorithm that resembles it. */
  function forestOracle(edges, vertices) {
    return function (m) {
      var p = [], i;
      for (i = 0; i < vertices; i += 1) p.push(i);
      function find(a) { while (p[a] !== a) { p[a] = p[p[a]]; a = p[a]; } return a; }
      for (i = 0; i < m.length; i += 1) {
        var a = find(edges[m[i]][0]), b = find(edges[m[i]][1]);
        if (a === b) return false;
        p[a] = b;
      }
      return true;
    };
  }
  /* And one that is NOT a matroid: the matchings of a graph. On a path of
     three edges {A}, {C} and {A,C} are independent and {B} cannot be grown at
     all, which is the smallest failure of the exchange property there is. */
  function matchingOracle(edges) {
    return function (m) {
      var used = {};
      for (var i = 0; i < m.length; i += 1) {
        var e = edges[m[i]];
        if (used[e[0]] || used[e[1]]) return false;
        used[e[0]] = true; used[e[1]] = true;
      }
      return true;
    };
  }
  /* Greedy needs the family to be downward closed before it needs it to be a
     matroid, and those are two conditions rather than one. */
  function downwardClosed(family) {
    var key = {}, bad = [];
    family.forEach(function (s) { key[s.join(',')] = true; });
    family.forEach(function (s) {
      s.forEach(function (x) {
        var sub = s.filter(function (y) { return y !== x; });
        if (!key[sub.join(',')]) bad.push({ set: s, drop: x });
      });
    });
    return { ok: bad.length === 0, failures: bad };
  }
  /* THE WEIGHTING THAT BEATS GREEDY, found rather than quoted.

     Rado and Edmonds: greedy is optimal for EVERY weighting exactly when the
     family is a matroid. So on a family that is not one, a weighting must
     exist where greedy loses, and this walks {1,2,3}^n in a fixed order until
     it finds the first -- which makes the counterexample reproducible instead
     of hand-picked. On a matroid it walks the whole space and returns null,
     which is the other half of the theorem checked on this instance. */
  function beatingWeights(family, ground, cap) {
    cap = cap === undefined ? 7 : cap;
    oracleCap('beatingWeights', ground.length, cap);
    var n = ground.length, total = Math.pow(3, n), tried = 0;
    for (var code = 0; code < total; code += 1) {
      var w = [], t = code, i;
      for (i = 0; i < n; i += 1) { w.push((t % 3) + 1); t = Math.floor(t / 3); }
      tried += 1;
      var run = matroidGreedy(family, w, ground);
      if (!run.result.matches) {
        return { weights: w, greedy: run.result.value, optimum: run.result.optimum,
                 chosen: run.result.chosen, best: run.result.optimal, tried: tried,
                 total: total };
      }
    }
    return { weights: null, tried: tried, total: total };
  }
  /* A selection is independent, checked against the ORACLE and not against
     the enumerated family, so a family built wrongly cannot hide inside a
     membership test of its own making. */
  function isIndependent(oracle, set) {
    return oracle(set.slice().sort(function (a, b) { return a - b; }));
  }

  /* ======================================================= stable matching

     Every perfect matching, filtered by the blocking-pair test the panel uses
     on Gale-Shapley's own answer. n! of them, capped at 6, and from the stable
     ones each proposer's best and worst ACHIEVABLE partner -- which is a fact
     about the instance, computed without running the algorithm at all. */
  function everyStableMatching(prefsA, prefsB, cap) {
    cap = cap === undefined ? 6 : cap;
    var n = prefsA.length, i;
    oracleCap('everyStableMatching', n, cap);
    var all = 0, stable = [], idx = [];
    for (i = 0; i < n; i += 1) idx.push(i);
    gyPermute(idx, function (perm) {
      all += 1;
      if (blockingPairs(perm, prefsA, prefsB).stable) stable.push(perm.slice());
    });
    var bestRank = [], worstRank = [];
    for (i = 0; i < n; i += 1) {
      var ranks = stable.map(function (m) { return prefsA[i].indexOf(m[i]); });
      bestRank.push(ranks.length ? Math.min.apply(null, ranks) : null);
      worstRank.push(ranks.length ? Math.max.apply(null, ranks) : null);
    }
    return { matchings: all, stable: stable, bestRank: bestRank, worstRank: worstRank };
  }
  /* Did this matching give EVERY proposer their best achievable partner? The
     theorem says Gale-Shapley's does; the panel checks it row by row. */
  function proposerOptimal(matchA, prefsA, every) {
    var rows = [];
    for (var i = 0; i < matchA.length; i += 1) {
      rows.push({ a: i, got: prefsA[i].indexOf(matchA[i]),
                  best: every.bestRank[i], worst: every.worstRank[i] });
    }
    return { rows: rows, optimal: rows.every(function (r) { return r.got === r.best; }) };
  }
  /* The same run with the two sides swapped, which is the asymmetry the mode
     exists for: the receivers propose, and every rank moves the other way. */
  function meanRank(matchA, prefs) {
    var t = 0;
    for (var i = 0; i < matchA.length; i += 1) t += prefs[i].indexOf(matchA[i]) + 1;
    return R(BigInt(t), BigInt(matchA.length));
  }
  function invertMatch(matchA, n) {
    var out = [];
    for (var i = 0; i < n; i += 1) out.push(-1);
    matchA.forEach(function (b, a) { if (b >= 0) out[b] = a; });
    return out;
  }

  /* ================================================================ caching

     THE BOUND, COMPUTED. Farthest-in-future is optimal among offline
     demand-paging policies, and every lesson says so. This searches every
     eviction decision -- memoised on (position, the set in the cache), which
     is what keeps it finishing -- and returns the largest hit count any such
     policy could reach. replayPolicy's 'opt' arm is then a number to compare
     against rather than a number to trust.

     DEMAND PAGING is the model, stated because it is a real restriction: a
     miss always loads the page, and a policy that could decline to cache it
     is a different problem. replayPolicy loads on every miss too, so the
     comparison is like for like. */
  function everyEviction(trace, k, cap) {
    cap = cap === undefined ? 18 : cap;
    oracleCap('everyEviction', trace.length, cap);
    var memo = {}, states = 0;
    function best(i, cache) {
      if (i === trace.length) return 0;
      var key = i + '|' + cache.join(',');
      if (memo[key] !== undefined) return memo[key];
      states += 1;
      var page = trace[i], out, j;
      if (cache.indexOf(page) !== -1) {
        out = 1 + best(i + 1, cache);
      } else if (cache.length < k) {
        out = best(i + 1, cache.concat([page]).sort(function (a, b) { return a - b; }));
      } else {
        out = 0;
        for (j = 0; j < cache.length; j += 1) {
          var next = cache.slice();
          next.splice(j, 1);
          next = next.concat([page]).sort(function (a, b) { return a - b; });
          var v = best(i + 1, next);
          if (v > out) out = v;
        }
      }
      memo[key] = out;
      return out;
    }
    var hits = best(0, []);
    return { hits: hits, misses: trace.length - hits, states: states,
             rate: R(BigInt(hits), BigInt(trace.length)) };
  }
  /* Belady's anomaly: FIFO with a BIGGER cache can get FEWER hits. Swept
     rather than described, because a reader told that it happens assumes it is
     rare, and a reader shown the row does not. */
  function beladySweep(trace, kmax, policy) {
    var rows = [], anomalies = [];
    for (var k = 1; k <= kmax; k += 1) {
      var r = replayPolicy(trace, k, policy);
      rows.push({ k: k, hits: r.hits, misses: r.misses, rate: r.rate });
      if (k > 1 && r.hits < rows[k - 2].hits) {
        anomalies.push({ from: k - 1, to: k, lost: rows[k - 2].hits - r.hits });
      }
    }
    return { rows: rows, anomalies: anomalies };
  }
  /* The reference trace with a hit/miss mark per position, replayed by the
     same routine the rates come from, so the picture and the number cannot
     disagree. */
  function replayMarks(trace, k, policy) {
    var marks = [];
    for (var i = 1; i <= trace.length; i += 1) {
      var here = replayPolicy(trace.slice(0, i), k, policy);
      var before = i > 1 ? replayPolicy(trace.slice(0, i - 1), k, policy).hits : 0;
      marks.push(here.hits > before);
    }
    return marks;
  }

  /* ============================================================== drawings

     Every builder returns a string and touches no element; the installer takes
     the element first and may be handed null. That is the rule algo_core's
     three drawing blocks exist to state. */
  function gyScale(items, width, left) {
    var lo = Infinity, hi = -Infinity;
    items.forEach(function (x) { if (x.s < lo) lo = x.s; if (x.f > hi) hi = x.f; });
    if (!isFinite(lo)) { lo = 0; hi = 1; }
    if (hi <= lo) hi = lo + 1;
    return { lo: lo, hi: hi,
             x: function (t) { return left + ((t - lo) / (hi - lo)) * (width - left - 18); } };
  }
  function intervalsSvg(items, opts) {
    opts = opts || {};
    var w = opts.width === undefined ? 660 : opts.width;
    var sc = gyScale(opts.span || items, w, 34);
    var rowH = opts.rowH === undefined ? 24 : opts.rowH;
    var pick = {}, mark = {};
    (opts.chosen || []).forEach(function (x) { pick[x.label] = true; });
    (opts.mark || []).forEach(function (x) { mark[x.label] = true; });
    var s = '';
    items.forEach(function (x, i) {
      var y = 14 + i * rowH, x0 = sc.x(x.s), x1 = sc.x(x.f);
      var on = pick[x.label], amber = !on && mark[x.label];
      s += '<rect x="' + x0.toFixed(1) + '" y="' + y + '" width="'
        + Math.max(4, x1 - x0).toFixed(1) + '" height="' + (rowH - 7) + '" rx="3" fill="'
        + (on ? 'var(--cyan)' : (amber ? 'var(--amber)' : 'var(--panel-3)'))
        + '" stroke="var(--line-strong)" stroke-width="1.2" />'
        + '<text x="10" y="' + (y + rowH - 12) + '" font-size="11" font-weight="800" fill="'
        + (on ? 'var(--cyan)' : 'var(--muted)') + '">' + x.label + '</text>'
        + '<text x="' + (x0 + 5).toFixed(1) + '" y="' + (y + rowH - 12)
        + '" font-size="10" fill="' + (on || amber ? 'var(--on-accent)' : 'var(--muted)')
        + '">' + x.s + ' to ' + x.f + '</text>';
    });
    if (opts.at !== null && opts.at !== undefined) {
      var xv = sc.x(opts.at);
      s += '<line x1="' + xv.toFixed(1) + '" y1="6" x2="' + xv.toFixed(1) + '" y2="'
        + (14 + items.length * rowH) + '" stroke="var(--red)" stroke-width="2" '
        + 'stroke-dasharray="4 3" />'
        + '<text x="' + (xv + 4).toFixed(1) + '" y="' + (14 + items.length * rowH + 11)
        + '" font-size="10" fill="var(--red)">t = ' + opts.at + '</text>';
    }
    return s;
  }
  function drawIntervals(el, items, opts) {
    var s = intervalsSvg(items, opts);
    if (el) el.innerHTML = s;
    return s;
  }
  function roomsSvg(rooms, all, opts) {
    opts = opts || {};
    var w = opts.width === undefined ? 660 : opts.width;
    var sc = gyScale(all, w, 54), rowH = opts.rowH === undefined ? 26 : opts.rowH;
    var s = '';
    rooms.forEach(function (room, r) {
      var y = 14 + r * rowH;
      s += '<text x="8" y="' + (y + rowH - 13) + '" font-size="10" fill="var(--muted)">room '
        + (r + 1) + '</text>';
      room.forEach(function (x) {
        var x0 = sc.x(x.s), x1 = sc.x(x.f);
        s += '<rect x="' + x0.toFixed(1) + '" y="' + y + '" width="'
          + Math.max(4, x1 - x0).toFixed(1) + '" height="' + (rowH - 8)
          + '" rx="3" fill="var(--cyan)" stroke="var(--line-strong)" stroke-width="1.2" />'
          + '<text x="' + (x0 + 5).toFixed(1) + '" y="' + (y + rowH - 14)
          + '" font-size="10" font-weight="800" fill="var(--on-accent)">' + x.label + '</text>';
      });
    });
    if (opts.at !== null && opts.at !== undefined) {
      var xv = sc.x(opts.at);
      s += '<line x1="' + xv.toFixed(1) + '" y1="6" x2="' + xv.toFixed(1) + '" y2="'
        + (14 + rooms.length * rowH) + '" stroke="var(--red)" stroke-width="2" '
        + 'stroke-dasharray="4 3" />';
    }
    return s;
  }
  function edgesSvg(edges, vertices, opts) {
    opts = opts || {};
    var w = opts.width === undefined ? 300 : opts.width;
    var h = opts.height === undefined ? 170 : opts.height;
    var cx = w / 2, cy = h / 2, rad = Math.min(cx, cy) - 26, pts = [], i;
    for (i = 0; i < vertices; i += 1) {
      var ang = -Math.PI / 2 + (2 * Math.PI * i) / Math.max(1, vertices);
      pts.push({ x: cx + rad * Math.cos(ang), y: cy + rad * Math.sin(ang) });
    }
    var on = {};
    (opts.highlight || []).forEach(function (e) { on[e] = true; });
    var s = '';
    edges.forEach(function (e, k) {
      var a = pts[e[0]], b = pts[e[1]];
      s += '<line x1="' + a.x.toFixed(1) + '" y1="' + a.y.toFixed(1) + '" x2="' + b.x.toFixed(1)
        + '" y2="' + b.y.toFixed(1) + '" stroke="' + (on[k] ? 'var(--cyan)' : 'var(--line-strong)')
        + '" stroke-width="' + (on[k] ? 3.4 : 1.6) + '" />'
        + '<text x="' + ((a.x + b.x) / 2).toFixed(1) + '" y="' + ((a.y + b.y) / 2 - 4).toFixed(1)
        + '" text-anchor="middle" font-size="10" font-weight="800" fill="'
        + (on[k] ? 'var(--cyan)' : 'var(--muted)') + '">' + gyLabel(k)
        + (opts.weights ? ' ' + opts.weights[k] : '') + '</text>';
    });
    pts.forEach(function (p, v) {
      s += '<circle cx="' + p.x.toFixed(1) + '" cy="' + p.y.toFixed(1)
        + '" r="12" fill="var(--panel-3)" stroke="var(--line-strong)" stroke-width="1.6" />'
        + '<text x="' + p.x.toFixed(1) + '" y="' + (p.y + 4).toFixed(1)
        + '" text-anchor="middle" font-size="11" font-weight="800" fill="var(--text)">'
        + (v + 1) + '</text>';
    });
    return s;
  }
  function matchSvg(matchA, n, opts) {
    opts = opts || {};
    var w = opts.width === undefined ? 300 : opts.width;
    var h = opts.height === undefined ? 190 : opts.height;
    var step = opts.step === undefined
      ? Math.min(30, Math.max(14, (h - 34) / Math.max(1, n - 1))) : opts.step;
    var lx = 56, rx = w - 56, s = '', i;
    for (i = 0; i < n; i += 1) {
      var y = 20 + i * step;
      if (matchA[i] >= 0) {
        s += '<line x1="' + lx + '" y1="' + y + '" x2="' + rx + '" y2="'
          + (20 + matchA[i] * step) + '" stroke="var(--cyan)" stroke-width="2.4" />';
      }
    }
    for (i = 0; i < n; i += 1) {
      var yy = 20 + i * step;
      s += '<circle cx="' + lx + '" cy="' + yy + '" r="11" fill="var(--panel-3)" '
        + 'stroke="var(--line-strong)" stroke-width="1.6" />'
        + '<text x="' + lx + '" y="' + (yy + 4) + '" text-anchor="middle" font-size="11" '
        + 'font-weight="800" fill="var(--text)">' + (i + 1) + '</text>'
        + '<circle cx="' + rx + '" cy="' + yy + '" r="11" fill="var(--panel-3)" '
        + 'stroke="var(--line-strong)" stroke-width="1.6" />'
        + '<text x="' + rx + '" y="' + (yy + 4) + '" text-anchor="middle" font-size="11" '
        + 'font-weight="800" fill="var(--text)">' + (i + 1) + '</text>';
    }
    s += '<text x="' + lx + '" y="10" text-anchor="middle" font-size="10" fill="var(--muted)">'
      + (opts.leftLabel || 'proposers') + '</text>'
      + '<text x="' + rx + '" y="10" text-anchor="middle" font-size="10" fill="var(--muted)">'
      + (opts.rightLabel || 'receivers') + '</text>';
    return s;
  }
  function traceSvg(trace, marks, opts) {
    opts = opts || {};
    var w = opts.width === undefined ? 660 : opts.width;
    var cell = Math.max(16, Math.min(34, Math.floor((w - 24) / Math.max(1, trace.length))));
    var s = '';
    trace.forEach(function (p, i) {
      var x = 12 + i * cell, hit = marks[i];
      s += '<rect x="' + x + '" y="14" width="' + (cell - 3) + '" height="30" rx="4" fill="'
        + (hit ? 'var(--cyan)' : 'var(--panel-3)') + '" stroke="var(--line-strong)" '
        + 'stroke-width="1.3" />'
        + '<text x="' + (x + (cell - 3) / 2).toFixed(1) + '" y="34" text-anchor="middle" '
        + 'font-size="11" font-weight="800" fill="' + (hit ? 'var(--on-accent)' : 'var(--text)')
        + '">' + p + '</text>'
        + '<text x="' + (x + (cell - 3) / 2).toFixed(1) + '" y="58" text-anchor="middle" '
        + 'font-size="9" fill="' + (hit ? 'var(--cyan)' : 'var(--muted)') + '">'
        + (hit ? 'hit' : 'miss') + '</text>';
    });
    return s;
  }
"""

_CORE_JS = (RATIONAL_JS + COUNT_JS + RFIXED_JS + ORACLE_JS + TREEDRAW_JS
            + REPLAY_JS + GREEDY_JS + GKIT_JS)


# ---------------------------------------------------------------------------
# Control furniture -- the same shapes every kit on this path uses, so a reader
# moving between courses moves between the same widgets. Drawings take the two
# viewBox widths theme.py gives a horizontal-scroll minimum, 520 and 660.
# ---------------------------------------------------------------------------


def _attr(text):
    return (str(text).replace("&", "&amp;").replace('"', "&quot;")
            .replace("<", "&lt;").replace(">", "&gt;"))


def _range(cid, label, lo, hi, value, step=1):
    return (
        "        <div>\n"
        '          <div class="range-row"><label class="small-copy" for="%s">%s</label>'
        '<span class="range-value" id="%sOut">%s</span></div>\n'
        '          <input id="%s" type="range" min="%s" max="%s" step="%s" value="%s" />\n'
        "        </div>\n" % (cid, label, cid, value, cid, lo, hi, step, value)
    )


def _select(cid, label, options, chosen):
    opts = "".join(
        '<option value="%s"%s>%s</option>'
        % (_attr(v), " selected" if str(v) == str(chosen) else "", t)
        for v, t in options
    )
    return (
        '        <div class="field">\n          <label for="%s">%s</label>\n'
        '          <select id="%s">%s</select>\n        </div>\n' % (cid, label, cid, opts)
    )


def _text(cid, label, value):
    """A text box. No value here may contain `>`.

    scripts/labcheck.js reads a control's starting value out of the markup with
    a tag scan, and a raw `>` inside an attribute ends the tag as far as that
    scan is concerned while `&gt;` reaches the harness undecoded. Nothing this
    kit asks a reader to type needs one -- an interval is `3-8`, an item is
    `20/100`, a preference row is `2 1 3` -- so the restriction costs nothing
    and is recorded here rather than rediscovered.
    """
    if ">" in str(value):
        raise ValueError("greedy: a control value may not contain '>': %r" % value)
    return (
        '        <div class="field">\n          <label for="%s">%s</label>\n'
        '          <input id="%s" type="text" value="%s" inputmode="text" autocomplete="off">\n'
        "        </div>\n" % (cid, label, cid, _attr(value))
    )


def _kpis(items):
    cells = "".join(
        '          <div class="kpi"><span>%s</span><strong id="%s">&mdash;</strong></div>\n'
        % (label, cid) for label, cid in items
    )
    return '        <div class="kpi-grid">\n%s        </div>\n' % cells


def _hint(cid, text):
    return '        <p class="small-copy" id="%s" style="margin:0;">%s</p>' % (cid, text)


def _toolbar(name, subtitle, legend):
    swatches = "".join(
        '<span class="tone-%s"><i class="legend-swatch"></i>%s</span>' % (tone, text)
        for tone, text in legend
    )
    return (
        '      <div class="lab-toolbar">\n'
        '        <div class="lab-title"><strong>%s</strong><span>%s</span></div>\n'
        '        <div class="inline-legend">%s</div>\n'
        "      </div>\n" % (name, subtitle, swatches)
    )


def _stage(inner):
    return '      <div class="lab-stage">%s</div>\n' % inner


def _svg(cid, box, alt):
    return '<svg id="%s" viewBox="%s" role="img" aria-label="%s"></svg>' % (cid, box, alt)


def _table(cid, top=12):
    return ('      <div class="table-wrap" style="margin-top:%dpx;">'
            '<table class="tt" id="%s"></table></div>\n' % (top, cid))


def _banner(cid):
    return '      <div class="status-banner" id="%s" style="margin-top:12px;"></div>' % cid


def _js(text):
    return "'" + str(text).replace("\\", "\\\\").replace("'", "\\'").replace("\n", "\\n") + "'"


def _presets_js(name, presets, keys):
    """The preset table as data the script reads, not as branches.

    Every preset goes through the same parser the reader's own typing does, so
    a preset cannot put a figure on the page that the typed version would not.
    """
    rows = []
    for p in presets:
        body = ", ".join("%s: %s" % (k, _js(p[k])) for k in keys)
        rows.append("    '%s': { %s }" % (p["id"], body))
    return "  var %s = {\n%s\n  };\n" % (name, ",\n".join(rows))


def _options(presets):
    return [(p["id"], p["label"]) for p in presets]


def _chosen(presets, cfg):
    want = str(cfg.get("preset", presets[0]["id"]))
    for p in presets:
        if p["id"] == want:
            return p
    raise ValueError(
        "greedy: no preset %r; this mode has %s"
        % (want, ", ".join(p["id"] for p in presets))
    )


# The sentence every mode carries in some form. Spelled once so no mode can
# quietly drop it, and each mode gives it its own nouns.
_CHECKED = (
    "  /* Nothing on this page is a claim about greedy algorithms in general.\n"
    "     Every verdict below is about the instance on screen, and every one of\n"
    "     them was computed twice: once by running the rule, and once by an\n"
    "     exhaustive search that does not know what the rule is. Where the two\n"
    "     disagree the panel prints both and names the subset that beats the\n"
    "     rule. Where the search is too big to run, the page says so and\n"
    "     refuses rather than printing a number it cannot stand behind. */\n"
)


# ---------------------------------------------------------------------------
# intervals -- the four rules, and the exchange argument run
# ---------------------------------------------------------------------------

_IV_PRESETS = [
    {
        "id": "eleven",
        "label": "eleven activities, the usual worked example",
        "spec": "1-4, 3-5, 0-6, 5-7, 3-9, 5-9, 6-10, 8-11, 8-12, 2-14, 12-16",
        "note": "the earliest-finish rule takes four of the eleven, and four is the most any "
                "of the 2048 subsets can manage — shortest-first happens to reach it too, "
                "which is what being right on one instance looks like",
    },
    {
        "id": "shortestfails",
        "label": "three intervals that kill the shortest-first rule",
        "spec": "0-5, 4-6, 5-10",
        "note": "the short one in the middle blocks both of the others, so the rule that "
                "sounds most careful takes one where two fit",
    },
    {
        "id": "startfails",
        "label": "one long interval that kills the earliest-start rule",
        "spec": "0-10, 1-2, 3-4, 5-6, 7-8",
        "note": "starting first is not finishing first, and the interval that starts first "
                "here occupies the whole day",
    },
    {
        "id": "conflictfails",
        "label": "seven intervals that kill the fewest-conflicts rule",
        "spec": "0-2, 2-4, 4-6, 6-8, 1-3, 3-5, 5-7",
        "note": "the two intervals with the fewest conflicts are the two ends, A and D, and "
                "B and C still fit around them — the optimum is all four. What loses them is "
                "the single finish-time pointer: once D is taken nothing starts after 8",
    },
]


def _intervals(cfg):
    chosen = _chosen(_IV_PRESETS, cfg)
    markup = (
        _toolbar(
            "Four rules, one instance, one optimum",
            "the optimum is the best of every subset, so a rule is right or it is not",
            [("cyan", "the rule took it"), ("amber", "in the optimum, not in the rule's answer"),
             ("muted", "in neither")],
        )
        + _stage(_svg("ivPlot", "0 0 660 250",
                      "Every interval as a bar on a time line, with the ones the chosen rule "
                      "selected filled in."))
        + _table("ivRules")
        + _table("ivChain")
        + _banner("ivStatus")
    )
    controls = (
        _select("ivPreset", "Instance", _options(_IV_PRESETS), chosen["id"])
        + _text("ivSpec", "Intervals, written start-finish", chosen["spec"])
        + _select("ivRule", "Greedy rule",
                  [("earliestFinish", "earliest finish time"),
                   ("earliestStart", "earliest start time"),
                   ("shortest", "shortest interval first"),
                   ("fewestConflicts", "fewest conflicts first")], "earliestFinish")
        + _kpis([("Intervals typed", "ivN"), ("This rule selects", "ivSize"),
                 ("The most any subset fits", "ivOpt"),
                 ("The selection is feasible", "ivFeas"),
                 ("Subsets the optimum searched", "ivSubsets"),
                 ("Exchange argument survives", "ivExch")])
        + _hint(
            "ivHint",
            "An interval is <span class=\"tt\">3-8</span>: it occupies the time from 3 up to "
            "but not including 8, so <span class=\"tt\">3-8</span> and <span class=\"tt\">8-11"
            "</span> both fit. The table under the chart runs all four rules on the same "
            "instance; the one under that performs the textbook exchange argument one swap at "
            "a time and checks after every swap that the set is still feasible and still the "
            "same size.",
        )
    )
    script = _CORE_JS + _CHECKED + _presets_js(
        "IVP", _IV_PRESETS, ["spec", "note"]) + r"""
  var presetIn = document.getElementById('ivPreset'), specIn = document.getElementById('ivSpec');
  var ruleIn = document.getElementById('ivRule');
  var plot = document.getElementById('ivPlot');
  var rulesT = document.getElementById('ivRules'), chainT = document.getElementById('ivChain');
  var status = document.getElementById('ivStatus');
  var KPIS = ['ivN', 'ivSize', 'ivOpt', 'ivFeas', 'ivSubsets', 'ivExch'];
  var RULE_NAME = { earliestFinish: 'earliest finish', earliestStart: 'earliest start',
                    shortest: 'shortest first', fewestConflicts: 'fewest conflicts' };

  function blank(why) {
    plot.innerHTML = ''; rulesT.innerHTML = ''; chainT.innerHTML = '';
    for (var i = 0; i < KPIS.length; i += 1) document.getElementById(KPIS[i]).textContent = '—';
    status.innerHTML = '<span class="tone-red">' + why + '.</span> An interval is '
      + '<span class="tt">3-8</span>, and they are separated by commas.';
  }

  function redraw() {
    var parsed = gyParseIntervals(specIn.value, 11);
    if (parsed.bad) { blank(parsed.bad); return; }
    var items = parsed.items, rule = ruleIn.value;
    var report = ruleReport(items);
    var row = null;
    report.rows.forEach(function (r) { if (r.rule === rule) row = r; });
    var chain = exchangeChain(items, rule);

    document.getElementById('ivN').textContent = String(items.length);
    document.getElementById('ivSize').textContent = String(row.size);
    document.getElementById('ivOpt').textContent = String(report.optimum);
    document.getElementById('ivFeas').textContent = row.feasible ? 'yes' : 'NO';
    document.getElementById('ivSubsets').textContent = String(report.subsets);
    document.getElementById('ivExch').textContent = chain.survived ? 'every swap' : 'breaks';

    plot.innerHTML = intervalsSvg(items, { chosen: row.chosen, mark: report.best });

    var rows = '';
    report.rows.forEach(function (r) {
      rows += '<tr class="' + (r.rule === rule ? 'tone-cyan' : '') + '">'
        + '<th class="rowhead">' + RULE_NAME[r.rule] + '</th>'
        + '<td>' + (gyNames(r.chosen.slice().sort(gyByFinish)) || '(none)') + '</td>'
        + '<td>' + r.size + '</td>'
        + '<td class="' + (r.feasible ? '' : 'tone-red') + '">' + (r.feasible ? 'yes' : 'NO') + '</td>'
        + '<td class="' + (r.optimal ? 'tone-cyan' : 'tone-red') + '">'
        + (r.optimal ? 'matches the optimum' : r.short + ' short of it') + '</td></tr>';
    });
    rulesT.innerHTML = '<thead><tr><th>rule</th><th>it selects</th><th>size</th>'
      + '<th>feasible</th><th>against the optimum</th></tr></thead><tbody>' + rows + '</tbody>';

    var crows = '';
    chain.steps.forEach(function (st) {
      crows += '<tr><th class="rowhead">swap ' + st.step + '</th>'
        + '<td>' + (st.out ? st.out.label + ' out, ' + st.into.label + ' in'
                           : st.into.label + ' was already there') + '</td>'
        + '<td>' + gyNames(st.set) + '</td>'
        + '<td class="' + (st.feasible ? '' : 'tone-red') + '">'
        + (st.feasible ? 'still feasible' : 'OVERLAPS') + '</td>'
        + '<td class="' + (st.kept ? '' : 'tone-red') + '">' + st.size
        + (st.kept ? '' : ' — one was lost') + '</td></tr>';
    });
    chainT.innerHTML = '<thead><tr><th>exchange</th><th>what it does</th><th>the set after it</th>'
      + '<th>feasible</th><th>size</th></tr></thead><tbody>' + crows + '</tbody>';

    var note = IVP[presetIn.value] ? IVP[presetIn.value].note : '';
    status.innerHTML = 'The <strong>' + RULE_NAME[rule] + '</strong> rule selected <strong>'
      + row.size + '</strong> interval' + (row.size === 1 ? '' : 's')
      + ', and that selection ' + (row.feasible
          ? 'is feasible — no two of them overlap, which was checked rather than assumed'
          : '<span class="tone-red">overlaps, so its size means nothing</span>')
      + '. The best of all <strong>' + report.subsets + '</strong> subsets is <strong>'
      + report.optimum + '</strong>' + (report.optimum ? ', attained by ' + gyNames(report.best) : '')
      + '. ' + (row.optimal
          ? 'The two agree on this instance. '
          : '<span class="tone-red">They do not agree</span>, so this rule is wrong — and one '
            + 'instance where it is wrong is all it takes. ')
      + (chain.survived
          ? 'The exchange argument then survives every swap: the optimum can be turned into '
            + 'greedy\'s own answer one interval at a time without ever becoming infeasible or '
            + 'smaller, which is the proof.'
          : 'The exchange argument breaks — the table above names the swap — so the proof that '
            + 'works for the earliest-finish rule does not transfer to this one.')
      + (note ? ' <span class="tone-muted">' + note + '.</span>' : '');
  }

  presetIn.addEventListener('change', function () {
    var p = IVP[presetIn.value];
    if (p) specIn.value = p.spec;
    redraw();
  });
  [specIn, ruleIn].forEach(function (el) {
    el.addEventListener('input', redraw);
    el.addEventListener('change', redraw);
  });
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="A greedy rule is right or it is not, and the optimum settles it",
        subtitle="Four rules on one instance, each beside the best of every subset",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Choose the instance and the rule"),
        panel_intro=cfg.get(
            "panel_intro",
            "The optimum is found by trying every subset, which knows nothing about any of the "
            "four rules. The exchange argument below it is not described: it is performed, one "
            "swap at a time, with feasibility rechecked after each.",
        ),
        script=script,
    )


# ---------------------------------------------------------------------------
# partition -- rooms against the depth, and the instant that certifies it
# ---------------------------------------------------------------------------

_PT_PRESETS = [
    {
        "id": "lectures",
        "label": "ten lectures, three rooms needed",
        "spec": "0-3, 1-4, 2-5, 4-7, 5-8, 6-9, 8-11, 9-12, 10-13, 12-15",
        "note": "three lectures are live at the same instant, so three rooms is not a "
                "property of the algorithm but of the instance",
    },
    {
        "id": "staircase",
        "label": "a staircase: every interval overlaps the next",
        "spec": "0-4, 2-6, 4-8, 6-10, 8-12",
        "note": "each interval meets only its neighbour, so two rooms suffice however many "
                "intervals there are",
    },
    {
        "id": "pileup",
        "label": "five intervals over one instant",
        "spec": "0-9, 1-9, 2-9, 3-9, 4-9",
        "note": "all five are alive at t = 4, and no schedule of any kind uses fewer than "
                "five rooms",
    },
    {
        "id": "disjoint",
        "label": "nothing overlaps at all",
        "spec": "0-2, 2-4, 4-6, 6-8, 8-10",
        "note": "the depth is one, and one room is what greedy uses",
    },
]


def _partition(cfg):
    chosen = _chosen(_PT_PRESETS, cfg)
    markup = (
        _toolbar(
            "Rooms used, against rooms needed",
            "the depth is a lower bound for every schedule, and greedy meets it",
            [("cyan", "assigned to a room"), ("red", "the instant that attains the depth"),
             ("amber", "alive at that instant")],
        )
        + _stage(_svg("ptPlot", "0 0 660 280",
                      "The intervals in the rooms greedy assigned them to, one row per room.")
                 + _svg("ptDepth", "0 0 660 280",
                        "The same intervals as typed, with the instant that attains the depth "
                        "marked."))
        + _table("ptRooms")
        + _banner("ptStatus")
    )
    controls = (
        _select("ptPreset", "Instance", _options(_PT_PRESETS), chosen["id"])
        + _text("ptSpec", "Intervals, written start-finish", chosen["spec"])
        + _select("ptOrder", "Consider the intervals in order of",
                  [("start", "start time"), ("finish", "finish time")], "start")
        + _kpis([("Intervals", "ptN"), ("Rooms greedy used", "ptUsed"),
                 ("Depth: most alive at once", "ptNeeded"),
                 ("Every room conflict-free", "ptValid"),
                 ("Rooms = depth", "ptOptimal"),
                 ("Certificate at t =", "ptAt")])
        + _hint(
            "ptHint",
            "Greedy puts each interval into the first room whose last booking has already "
            "finished, and opens a new room only when none has. The lower bound is the "
            "<em>depth</em>: at the marked instant several intervals are live at once, they "
            "pairwise overlap, and so no schedule &mdash; greedy or otherwise &mdash; can use "
            "fewer rooms than there are of them. The two numbers are computed separately.",
        )
    )
    script = _CORE_JS + _CHECKED + _presets_js(
        "PTP", _PT_PRESETS, ["spec", "note"]) + r"""
  var presetIn = document.getElementById('ptPreset'), specIn = document.getElementById('ptSpec');
  var orderIn = document.getElementById('ptOrder');
  var plot = document.getElementById('ptPlot'), depthPlot = document.getElementById('ptDepth');
  var roomsT = document.getElementById('ptRooms'), status = document.getElementById('ptStatus');
  var KPIS = ['ptN', 'ptUsed', 'ptNeeded', 'ptValid', 'ptOptimal', 'ptAt'];

  function blank(why) {
    plot.innerHTML = ''; depthPlot.innerHTML = ''; roomsT.innerHTML = '';
    for (var i = 0; i < KPIS.length; i += 1) document.getElementById(KPIS[i]).textContent = '—';
    status.innerHTML = '<span class="tone-red">' + why + '.</span> An interval is '
      + '<span class="tt">3-8</span>, and they are separated by commas.';
  }

  function redraw() {
    var parsed = gyParseIntervals(specIn.value, 12);
    if (parsed.bad) { blank(parsed.bad); return; }
    var items = parsed.items;
    var run = partitionRooms(items, orderIn.value);
    var valid = roomsValid(run.result.rooms, items);
    var live = run.result.at === null ? [] : liveAt(items, run.result.at);
    var pairwise = mutuallyOverlapping(live);

    document.getElementById('ptN').textContent = String(items.length);
    document.getElementById('ptUsed').textContent = String(run.result.used);
    document.getElementById('ptNeeded').textContent = String(run.result.depth);
    document.getElementById('ptValid').textContent = valid.ok ? 'yes' : 'NO';
    document.getElementById('ptOptimal').textContent = run.result.optimal ? 'yes' : 'no';
    document.getElementById('ptAt').textContent = run.result.at === null ? '—' : String(run.result.at);

    plot.innerHTML = roomsSvg(run.result.rooms, items, { at: run.result.at });
    depthPlot.innerHTML = intervalsSvg(items, { mark: live, at: run.result.at });

    var rows = '';
    run.result.rooms.forEach(function (room, r) {
      rows += '<tr><th class="rowhead">room ' + (r + 1) + '</th><td>' + gyNames(room)
        + '</td><td>' + room.length + '</td><td class="'
        + (intervalsDisjoint(room) ? '' : 'tone-red') + '">'
        + (intervalsDisjoint(room) ? 'no two overlap' : 'OVERLAPS') + '</td></tr>';
    });
    rows += '<tr class="tone-amber"><th class="rowhead">live at t = '
      + (run.result.at === null ? '—' : run.result.at) + '</th><td>' + (gyNames(live) || '(none)')
      + '</td><td>' + live.length + '</td><td>'
      + (pairwise ? 'they pairwise overlap, so this many rooms are unavoidable'
                  : 'not pairwise overlapping') + '</td></tr>';
    roomsT.innerHTML = '<thead><tr><th>room</th><th>intervals</th><th>count</th>'
      + '<th>check</th></tr></thead><tbody>' + rows + '</tbody>';

    var note = PTP[presetIn.value] ? PTP[presetIn.value].note : '';
    status.innerHTML = 'Greedy opened <strong>' + run.result.used + '</strong> room'
      + (run.result.used === 1 ? '' : 's') + ', and every one of them was checked: '
      + (valid.ok
          ? 'no room holds two intervals that overlap, and all ' + items.length
            + ' intervals were placed exactly once'
          : '<span class="tone-red">the assignment is not valid</span>')
      + '. The depth is <strong>' + run.result.depth + '</strong>'
      + (live.length
          ? ', attained at t = ' + run.result.at + ' where ' + gyNames(live)
            + ' are all live at once. Those ' + live.length
            + ' intervals pairwise overlap, so no schedule can put two of them in one room and '
            + 'no schedule uses fewer than ' + run.result.depth + ' rooms'
          : '')
      + '. ' + (run.result.optimal
          ? 'The two numbers are equal, so greedy is optimal <em>on this instance</em> and the '
            + 'reason is on the screen rather than in a citation.'
          : '<span class="tone-red">The two numbers differ</span>, which on this problem should '
            + 'not happen — the greedy-by-start rule provably meets the depth.')
      + (note ? ' <span class="tone-muted">' + note + '.</span>' : '');
  }

  presetIn.addEventListener('change', function () {
    var p = PTP[presetIn.value];
    if (p) specIn.value = p.spec;
    redraw();
  });
  [specIn, orderIn].forEach(function (el) {
    el.addEventListener('input', redraw);
    el.addEventListener('change', redraw);
  });
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="The depth is the lower bound, and greedy meets it",
        subtitle="Rooms used and rooms needed, computed by two routines that share nothing",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Choose the instance and the order"),
        panel_intro=cfg.get(
            "panel_intro",
            "The number of rooms greedy opens is one calculation. The depth &mdash; the most "
            "intervals alive at any single instant &mdash; is another, and it is a bound on "
            "every schedule. The page prints the instant that attains it and the intervals "
            "that make it true.",
        ),
        script=script,
    )


# ---------------------------------------------------------------------------
# huffman -- the merges, the exact expected length, and the round trip
# ---------------------------------------------------------------------------

_HF_PRESETS = [
    {
        "id": "clrs",
        "label": "six symbols, the usual worked example",
        "spec": "a:45, b:13, c:12, d:16, e:9, f:5",
        "message": "abcdef",
        "note": "the expected length is 56/25 bits against 3 for a fixed-length code over six "
                "symbols",
    },
    {
        "id": "skewed",
        "label": "one symbol dominates",
        "spec": "a:60, b:20, c:10, d:5, e:5",
        "message": "aaabac",
        "note": "the common symbol gets one bit and the rare ones four, which is where the "
                "saving comes from",
    },
    {
        "id": "uniform",
        "label": "four equal weights",
        "spec": "a:10, b:10, c:10, d:10",
        "message": "abcd",
        "note": "with equal weights every codeword is two bits and Huffman saves nothing at "
                "all — the saving is a fact about the distribution, not about the algorithm",
    },
    {
        "id": "fibonacci",
        "label": "Fibonacci weights, the deepest possible tree",
        "spec": "a:1, b:1, c:2, d:3, e:5",
        "message": "abcde",
        "note": "each merge is the running total of everything merged so far — 2, then 4, 7, "
                "12 — and every one of those totals is at least the next weight, so the new "
                "node pairs with the next symbol every time: the tree is a path and the two "
                "rarest symbols need four bits",
    },
]


def _huffman(cfg):
    chosen = _chosen(_HF_PRESETS, cfg)
    markup = (
        _toolbar(
            "The merges, the tree, and the bits that come back",
            "the code is checked prefix-free, and the message is decoded again",
            [("cyan", "merged at this step"), ("amber", "a leaf"), ("muted", "an internal node")],
        )
        + _stage(_svg("hfTree", "0 0 520 240",
                      "The Huffman tree, each leaf a symbol and each internal node the total "
                      "weight below it."))
        + _table("hfMerges")
        + _table("hfCodes")
        + _banner("hfStatus")
    )
    controls = (
        _select("hfPreset", "Alphabet", _options(_HF_PRESETS), chosen["id"])
        + _text("hfSpec", "Symbols and weights, written name:weight", chosen["spec"])
        + _text("hfMessage", "A message to encode and decode again", chosen["message"])
        + _range("hfStep", "Merge", 1, 12, 1)
        + _kpis([("Symbols", "hfN"), ("Expected bits per symbol", "hfExp"),
                 ("A fixed-length code costs", "hfFixed"),
                 ("Prefix-free", "hfPrefix"),
                 ("Round trip returns the message", "hfTrip"),
                 ("At the minimum over every tree", "hfMin")])
        + _hint(
            "hfHint",
            "A symbol is <span class=\"tt\">a:45</span>. Each step merges the two lightest "
            "remaining weights, and the tree is what the merges built. The expected length is "
            "<em>total bits / total weight</em> &mdash; an exact fraction, printed as one. The "
            "last figure enumerates every full binary tree on this many leaves and every way "
            "of assigning the weights to them, so &ldquo;Huffman is optimal&rdquo; is checked "
            "here rather than cited.",
        )
    )
    script = _CORE_JS + _CHECKED + _presets_js(
        "HFP", _HF_PRESETS, ["spec", "message", "note"]) + r"""
  var presetIn = document.getElementById('hfPreset'), specIn = document.getElementById('hfSpec');
  var msgIn = document.getElementById('hfMessage');
  var stepIn = document.getElementById('hfStep'), stepOut = document.getElementById('hfStepOut');
  var tree = document.getElementById('hfTree');
  var mergesT = document.getElementById('hfMerges'), codesT = document.getElementById('hfCodes');
  var status = document.getElementById('hfStatus');
  var KPIS = ['hfN', 'hfExp', 'hfFixed', 'hfPrefix', 'hfTrip', 'hfMin'];

  function blank(why) {
    tree.innerHTML = ''; mergesT.innerHTML = ''; codesT.innerHTML = '';
    for (var i = 0; i < KPIS.length; i += 1) document.getElementById(KPIS[i]).textContent = '—';
    status.innerHTML = '<span class="tone-red">' + why + '.</span> A symbol is '
      + '<span class="tt">a:45</span>, and they are separated by commas.';
  }

  function clamp(v, hi) { return v < 0 ? 0 : (v > hi ? hi : v); }

  function redraw() {
    var parsed = gyParseFreqs(specIn.value);
    if (parsed.bad) { blank(parsed.bad); return; }
    var freqs = parsed.freqs;
    var run = huffmanBuild(freqs), codes = run.result.codes;
    var cost = codeCost(codes, freqs);
    var prefix = codesPrefixFree(codes);
    var syms = String(msgIn.value).split('').filter(function (ch) {
      return codes[ch] !== undefined;
    });
    var bits = encodeSyms(codes, syms);
    var back = bits === null ? null : decodeBits(codes, bits);
    var trip = back !== null && back.join('') === syms.join('');

    stepIn.max = Math.max(1, run.trace.length);
    var k = clamp(parseInt(stepIn.value, 10) - 1, Math.max(0, run.trace.length - 1));
    stepOut.textContent = (k + 1) + ' of ' + run.trace.length;
    var here = run.trace[k] || { took: [], made: 0, weights: [], remaining: 0 };

    var minimum = null, why = '';
    try {
      minimum = huffmanBruteBits(freqs.map(function (f) { return f.weight; }));
    } catch (err) {
      why = String(err.message);
    }

    document.getElementById('hfN').textContent = String(freqs.length);
    document.getElementById('hfExp').textContent = Rtext(cost.expected) + ' = '
      + Rfixed(cost.expected, 3);
    document.getElementById('hfFixed').textContent = Rtext(cost.fixed);
    document.getElementById('hfPrefix').textContent = prefix ? 'checked, yes' : 'NO';
    document.getElementById('hfTrip').textContent = trip ? 'yes' : (syms.length ? 'NO' : '—');
    document.getElementById('hfMin').textContent = minimum
      ? (String(cost.bits) === String(minimum.bits) ? 'yes' : 'NO') : 'not searched';

    var markSet = {};
    (here.took || []).forEach(function (s) { markSet[s === null ? '' : s] = true; });
    tree.innerHTML = run.result.root
      ? drawTree(null, run.result.root, huffKids,
                 function (nd) { return nd.l || nd.r ? String(nd.weight) : String(nd.symbol); },
                 { width: 500, height: 220, radius: 13,
                   fill: function (n) {
                     var nd = n.node;
                     if (!nd.l && !nd.r) return markSet[nd.symbol] ? 'var(--cyan)' : 'var(--amber)';
                     return 'var(--panel-3)';
                   },
                   note: function (n) {
                     var nd = n.node;
                     return (!nd.l && !nd.r) ? codes[nd.symbol] : '';
                   } })
      : '';

    var rows = '';
    run.trace.forEach(function (st, i) {
      rows += '<tr class="' + (i === k ? 'tone-cyan' : '') + '"><th class="rowhead">merge '
        + (i + 1) + '</th><td>' + st.took.join(' and ') + '</td><td>'
        + st.weights.join(' + ') + ' = ' + st.made + '</td><td>' + st.remaining
        + ' left</td></tr>';
    });
    mergesT.innerHTML = '<thead><tr><th>step</th><th>the two lightest</th><th>merged weight</th>'
      + '<th>remaining</th></tr></thead><tbody>' + rows + '</tbody>';

    var crows = '', lens = codeLengths(codes);
    freqs.forEach(function (f) {
      crows += '<tr><th class="rowhead">' + f.symbol + '</th><td>' + f.weight + '</td>'
        + '<td class="tt">' + codes[f.symbol] + '</td><td>' + lens[f.symbol] + '</td>'
        + '<td>' + (f.weight * lens[f.symbol]) + '</td></tr>';
    });
    crows += '<tr class="tone-cyan"><th class="rowhead">total</th><td>' + cost.total
      + '</td><td>—</td><td>—</td><td>' + cost.bits + '</td></tr>';
    codesT.innerHTML = '<thead><tr><th>symbol</th><th>weight</th><th>codeword</th>'
      + '<th>bits</th><th>weight x bits</th></tr></thead><tbody>' + crows + '</tbody>';

    var note = HFP[presetIn.value] ? HFP[presetIn.value].note : '';
    status.innerHTML = 'The code costs <strong>' + cost.bits + '</strong> bits over '
      + cost.total + ' symbols, so <strong>' + Rtext(cost.expected)
      + '</strong> bits each — exactly that fraction, and <span class="tone-muted">'
      + Rfixed(cost.expected, 3) + ' rounded to three places</span> only for reading. A '
      + 'fixed-length code over ' + freqs.length + ' symbols costs ' + Rtext(cost.fixed)
      + ', so the saving is ' + Rtext(cost.saving) + ' bits per symbol. The code is '
      + (prefix ? 'prefix-free, checked pair by pair rather than assumed from the tree'
                : '<span class="tone-red">not prefix-free</span>')
      + (syms.length
          ? ', and the message encodes to ' + bits.length + ' bits and decodes back to '
            + (trip ? '<span class="tone-cyan">exactly what went in</span>'
                    : '<span class="tone-red">something else</span>')
          : '')
      + '. ' + (minimum
          ? 'Every one of the ' + minimum.shapes + ' full binary trees on ' + freqs.length
            + ' leaves was tried, against all ' + minimum.assignments
            + ' assignments of these weights to their leaves, and the best of them costs '
            + minimum.bits + ' bits — '
            + (String(minimum.bits) === String(cost.bits)
                ? 'which is what Huffman produced, so on this alphabet it is optimal and that '
                  + 'is a computation rather than a citation.'
                : '<span class="tone-red">which Huffman did not reach</span>.')
          : '<span class="tone-amber">The exhaustive check was refused: ' + why
            + '.</span> The expected length above is still exact; what is missing is the proof '
            + 'that nothing beats it, and the page says so rather than implying it.')
      + (note ? ' <span class="tone-muted">' + note + '.</span>' : '');
  }

  presetIn.addEventListener('change', function () {
    var p = HFP[presetIn.value];
    if (p) { specIn.value = p.spec; msgIn.value = p.message; }
    redraw();
  });
  [specIn, msgIn, stepIn].forEach(function (el) {
    el.addEventListener('input', redraw);
    el.addEventListener('change', redraw);
  });
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="Huffman's code, and the proof that nothing shorter exists",
        subtitle="The merges, the exact expected length, and every tree it is measured against",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Choose the alphabet"),
        panel_intro=cfg.get(
            "panel_intro",
            "The expected codeword length is a fraction and is printed as one. The optimality "
            "claim is checked by building every full binary tree on this many leaves and "
            "trying every assignment of the weights to their leaves &mdash; a search that "
            "knows nothing about merging the two lightest.",
        ),
        script=script,
    )


# ---------------------------------------------------------------------------
# knapsack -- fractional exactly, 0/1 greedy three ways, and the gap
# ---------------------------------------------------------------------------

_KS_PRESETS = [
    {
        "id": "classic",
        "label": "three items, capacity 50",
        "spec": "10/60, 20/100, 30/120",
        "cap": "50",
        "note": "the fractional optimum is 240 and the 0/1 optimum 220, and the 20 between "
                "them is what refusing to cut that last item costs",
    },
    {
        "id": "densitytrap",
        "label": "the item that dense greedy skips",
        "spec": "1/2, 10/10, 10/10",
        "cap": "20",
        "note": "the tiny dense item is taken first and wastes a unit of capacity that one of "
                "the big items needed",
    },
    {
        "id": "halfway",
        "label": "density greedy at a fiftieth of the optimum",
        "spec": "1/2, 50/100",
        "cap": "50",
        "note": "density picks the crumb and stops; the single most valuable item alone does "
                "fifty times better, which is why the guarantee takes the better of the two",
    },
    {
        "id": "even",
        "label": "six items, everything is tight",
        "spec": "12/24, 7/13, 11/23, 8/15, 9/16, 5/9",
        "cap": "26",
        "note": "the fractional optimum is 421/8, which no subset of whole items can reach, "
                "and none of the three rules reaches the 0/1 optimum either",
    },
]


def _knapsack(cfg):
    chosen = _chosen(_KS_PRESETS, cfg)
    markup = (
        _toolbar(
            "Cut an item and greedy is right; refuse to cut it and it is not",
            "the fractional optimum is exact, the 0/1 optimum is the best of every subset",
            [("cyan", "taken whole"), ("amber", "taken in part"), ("red", "skipped")],
        )
        + _stage(_svg("ksPlot", "0 0 660 200",
                      "The items in the order the chosen rule considers them, with the ones it "
                      "took filled in."))
        + _table("ksOrder")
        + _table("ksRules")
        + _banner("ksStatus")
    )
    controls = (
        _select("ksPreset", "Instance", _options(_KS_PRESETS), chosen["id"])
        + _text("ksSpec", "Items, written weight/value", chosen["spec"])
        + _text("ksCap", "Capacity", chosen["cap"])
        + _select("ksRule", "0/1 greedy takes items in order of",
                  [("density", "value per unit weight"), ("value", "value, highest first"),
                   ("light", "weight, lightest first")], "density")
        + _kpis([("Fractional optimum", "ksFrac"), ("0/1 optimum", "ksOpt"),
                 ("This 0/1 rule gets", "ksGreedy"),
                 ("Ratio to the optimum", "ksRatio"),
                 ("Better of greedy and one item", "ksHalf"),
                 ("At least half the optimum", "ksGuar")])
        + _hint(
            "ksHint",
            "An item is <span class=\"tt\">20/100</span>: weight 20, value 100. Cutting items "
            "is allowed in the fractional problem and the densest-first rule is then provably "
            "optimal &mdash; the answer is an exact fraction. Refuse to cut, and the same rule "
            "has no guarantee at all. Taking the better of it and the single most valuable "
            "item that fits does have one: at least half the optimum, on every instance.",
        )
    )
    script = _CORE_JS + _CHECKED + _presets_js(
        "KSP", _KS_PRESETS, ["spec", "cap", "note"]) + r"""
  var presetIn = document.getElementById('ksPreset'), specIn = document.getElementById('ksSpec');
  var capIn = document.getElementById('ksCap'), ruleIn = document.getElementById('ksRule');
  var plot = document.getElementById('ksPlot');
  var orderT = document.getElementById('ksOrder'), rulesT = document.getElementById('ksRules');
  var status = document.getElementById('ksStatus');
  var KPIS = ['ksFrac', 'ksOpt', 'ksGreedy', 'ksRatio', 'ksHalf', 'ksGuar'];
  var RULE_NAME = { density: 'value per unit weight', value: 'value first', light: 'lightest first' };

  function blank(why) {
    plot.innerHTML = ''; orderT.innerHTML = ''; rulesT.innerHTML = '';
    for (var i = 0; i < KPIS.length; i += 1) document.getElementById(KPIS[i]).textContent = '—';
    status.innerHTML = '<span class="tone-red">' + why + '.</span> An item is '
      + '<span class="tt">20/100</span>: weight, then value.';
  }

  function redraw() {
    var parsed = gyParseItems(specIn.value);
    if (parsed.bad) { blank(parsed.bad); return; }
    var items = parsed.items;
    var W = parseInt(capIn.value, 10);
    if (!isFinite(W) || W <= 0) { blank('the capacity has to be a positive whole number'); return; }
    var rule = ruleIn.value;

    var frac = fractionalKnapsack(items, W);
    var brute = knapsackBrute(items, W);
    var greedy = greedyKnapsack01(items, W, rule);
    var checked = packValue(items, greedy.result.picks);
    var half = halfGuarantee(items, W);
    var ratio = gyRatio(greedy.result.value, brute.result.value);
    var guarantee = gyRatio(half.value, brute.result.value);
    var meetsHalf = Rcmp(guarantee, R(1n, 2n)) >= 0;

    document.getElementById('ksFrac').textContent = Rtext(frac.result.value);
    document.getElementById('ksOpt').textContent = String(brute.result.value);
    document.getElementById('ksGreedy').textContent = String(greedy.result.value);
    document.getElementById('ksRatio').textContent = Rtext(ratio) + ' = ' + Rfixed(ratio, 3);
    document.getElementById('ksHalf').textContent = String(half.value);
    document.getElementById('ksGuar').textContent = meetsHalf ? 'yes' : 'NO';

    var taken = {};
    greedy.result.picks.forEach(function (i) { taken[items[i].label] = true; });
    var bars = greedy.result.order.map(function (o, i) {
      return { s: i, f: i + 1, label: o.label };
    });
    plot.innerHTML = intervalsSvg(bars, {
      chosen: bars.filter(function (b) { return taken[b.label]; }),
      rowH: 22
    });

    var rows = '';
    greedy.trace.forEach(function (st, i) {
      rows += '<tr class="' + (st.taken ? 'tone-cyan' : '') + '"><th class="rowhead">'
        + (i + 1) + '</th><td>' + st.item.label + '</td><td>' + st.item.w + '</td>'
        + '<td>' + st.item.v + '</td><td>' + Rtext(st.item.d) + '</td>'
        + '<td>' + (st.taken ? 'taken' : 'does not fit') + '</td><td>' + st.left + '</td></tr>';
    });
    orderT.innerHTML = '<thead><tr><th>step</th><th>item</th><th>weight</th><th>value</th>'
      + '<th>density</th><th>decision</th><th>capacity left</th></tr></thead><tbody>'
      + rows + '</tbody>';

    var frows = '';
    frac.result.picks.forEach(function (p) {
      frows += '<tr><th class="rowhead">' + items[p.i].label + '</th><td>'
        + Rtext(p.take) + ' of it</td><td>'
        + Rtext(Rmul(p.take, R(BigInt(items[p.i].v), 1n))) + '</td></tr>';
    });
    frows += '<tr class="tone-cyan"><th class="rowhead">fractional total</th><td>—</td><td>'
      + Rtext(frac.result.value) + '</td></tr>';
    frows += '<tr><th class="rowhead">0/1 optimum</th><td>'
      + brute.result.members.map(function (i) { return items[i].label; }).join(' ')
      + '</td><td>' + brute.result.value + '</td></tr>';
    ['density', 'value', 'light'].forEach(function (r) {
      var g = greedyKnapsack01(items, W, r);
      frows += '<tr class="' + (r === rule ? 'tone-amber' : '') + '"><th class="rowhead">'
        + RULE_NAME[r] + '</th><td>'
        + g.result.picks.map(function (i) { return items[i].label; }).join(' ')
        + '</td><td>' + g.result.value + '</td></tr>';
    });
    rulesT.innerHTML = '<thead><tr><th>solution</th><th>what it takes</th><th>value</th>'
      + '</tr></thead><tbody>' + frows + '</tbody>';

    var note = KSP[presetIn.value] ? KSP[presetIn.value].note : '';
    status.innerHTML = 'Cutting allowed, the answer is <strong>' + Rtext(frac.result.value)
      + '</strong> — an exact fraction, from sorting by density and taking '
      + 'whatever fraction of the last item fits. Cutting refused, the best of all '
      + brute.counts.nodes + ' subsets is <strong>' + brute.result.value
      + '</strong>, and the ' + RULE_NAME[rule] + ' rule gets <strong>' + greedy.result.value
      + '</strong>' + (checked.v === greedy.result.value && checked.w <= W
          ? ' (its picks were re-weighed: ' + checked.w + ' of ' + W + ' used)'
          : ' <span class="tone-red">but its picks do not add up to that</span>')
      + ', a ratio of ' + Rtext(ratio) + '. '
      + (greedy.result.value === brute.result.value
          ? 'On this instance the rule happens to be right, which is a fact about the instance. '
          : 'The rule is <span class="tone-red">not optimal here</span>, and no 0/1 greedy rule '
            + 'is optimal in general. ')
      + 'Taking the better of density greedy (' + half.greedy + ') and the most valuable single '
      + 'item that fits (' + half.single + ') gives ' + half.value + ', which is '
      + Rtext(guarantee) + ' of the optimum — '
      + (meetsHalf ? 'at or above the one-half the guarantee promises'
                   : '<span class="tone-red">below one half, which should be impossible</span>')
      + '.' + (note ? ' <span class="tone-muted">' + note + '.</span>' : '');
  }

  presetIn.addEventListener('change', function () {
    var p = KSP[presetIn.value];
    if (p) { specIn.value = p.spec; capIn.value = p.cap; }
    redraw();
  });
  [specIn, capIn, ruleIn].forEach(function (el) {
    el.addEventListener('input', redraw);
    el.addEventListener('change', redraw);
  });
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="One problem greedy solves exactly, and its twin that it cannot",
        subtitle="Fractional as an exact fraction, 0/1 against the best of every subset",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Choose the items and the capacity"),
        panel_intro=cfg.get(
            "panel_intro",
            "Densities are compared as exact fractions, never as decimals, so two items whose "
            "densities differ in the fifteenth place are ordered by their values and not by "
            "rounding. The 0/1 optimum is the best of every subset and knows nothing about "
            "any rule.",
        ),
        script=script,
    )


# ---------------------------------------------------------------------------
# matroid -- the family from its oracle, and the weighting that beats greedy
# ---------------------------------------------------------------------------

_MT_PRESETS = [
    {
        "id": "uniform",
        "label": "uniform: any two of five",
        "kind": "uniform",
        "spec": "2",
        "weights": "9 7 5 3 1",
        "note": "the rank is 2 and every pair is a basis, which is the simplest matroid there "
                "is and the one every proof is sanity-checked on",
    },
    {
        "id": "graphic",
        "label": "graphic: the forests of a four-vertex graph",
        "kind": "graphic",
        "spec": "1-2, 2-3, 3-1, 3-4, 1-4",
        "weights": "8 6 5 4 2",
        "note": "greedy over this family IS Kruskal's algorithm, and the bases are the "
                "spanning trees",
    },
    {
        "id": "partition",
        "label": "partition: at most one from each group",
        "kind": "partition",
        "spec": "1 1 2 2 3",
        "weights": "7 6 5 4 3",
        "note": "three groups, one element each, so the rank is 3 and the greedy answer is the "
                "heaviest element of each group",
    },
    {
        "id": "matchings",
        "label": "NOT a matroid: the matchings of a path",
        "kind": "matching",
        "spec": "1-2, 2-3, 3-4",
        "weights": "2 3 2",
        "note": "the middle edge alone cannot be grown, while the two ends together can, which "
                "is the exchange property failing at the smallest possible instance",
    },
]


def _matroid(cfg):
    chosen = _chosen(_MT_PRESETS, cfg)
    markup = (
        _toolbar(
            "The exchange property, tested on every pair",
            "greedy is optimal for every weighting exactly when it holds",
            [("cyan", "greedy took it"), ("amber", "in the best set instead"),
             ("red", "a pair the exchange property fails on")],
        )
        + _stage(_svg("mtPlot", "0 0 520 200",
                      "The ground set drawn as a graph where the family is a graph's, and as a "
                      "row of elements otherwise."))
        + _table("mtFamily")
        + _table("mtRun")
        + _banner("mtStatus")
    )
    controls = (
        _select("mtPreset", "Family", _options(_MT_PRESETS), chosen["id"])
        + _text("mtSpec", "Its parameter: a rank, an edge list, or a group per element",
                chosen["spec"])
        + _text("mtWeights", "A weight per element", chosen["weights"])
        + _kpis([("Ground set", "mtN"), ("Independent sets", "mtFam"),
                 ("Rank", "mtRank"), ("Exchange pairs tested", "mtPairs"),
                 ("It is a matroid", "mtIs"),
                 ("Greedy = optimum, these weights", "mtGreedy")])
        + _hint(
            "mtHint",
            "A family of &ldquo;independent&rdquo; sets is given here by a membership test, "
            "because that is the definition; the family is then listed by running the test on "
            "all 2<sup>n</sup> subsets. The exchange property says that if one independent set "
            "is smaller than another, some element of the larger can join it. The page tests "
            "every ordered pair, and then searches weightings until it finds one where greedy "
            "loses &mdash; which, by Rado and Edmonds, exists exactly when the property fails.",
        )
    )
    script = _CORE_JS + _CHECKED + _presets_js(
        "MTP", _MT_PRESETS, ["kind", "spec", "weights", "note"]) + r"""
  var presetIn = document.getElementById('mtPreset'), specIn = document.getElementById('mtSpec');
  var wIn = document.getElementById('mtWeights');
  var plot = document.getElementById('mtPlot');
  var famT = document.getElementById('mtFamily'), runT = document.getElementById('mtRun');
  var status = document.getElementById('mtStatus');
  var KPIS = ['mtN', 'mtFam', 'mtRank', 'mtPairs', 'mtIs', 'mtGreedy'];

  function blank(why) {
    plot.innerHTML = ''; famT.innerHTML = ''; runT.innerHTML = '';
    for (var i = 0; i < KPIS.length; i += 1) document.getElementById(KPIS[i]).textContent = '—';
    status.innerHTML = '<span class="tone-red">' + why + '.</span>';
  }

  /* An edge list, `1-2, 2-3`, 1-based, for the two graph families. */
  function readEdges(text) {
    var edges = [], bad = null, top = 0;
    String(text).split(',').forEach(function (piece) {
      var t = piece.replace(/\s+/g, '');
      if (!t || bad) return;
      var m = /^(\d+)-(\d+)$/.exec(t);
      if (!m) { bad = 'an edge is written 1-2; "' + t + '" is not'; return; }
      var a = parseInt(m[1], 10) - 1, b = parseInt(m[2], 10) - 1;
      if (a === b) { bad = 'a loop is in no forest and no matching'; return; }
      if (edges.length >= 6) {
        bad = 'at most 6 edges: every subset is listed and then every ORDERED PAIR of the '
            + 'family is tested, which is quadratic in a family that is itself exponential';
        return;
      }
      top = Math.max(top, a + 1, b + 1);
      edges.push([a, b]);
    });
    if (!bad && !edges.length) bad = 'no edges were read';
    return { edges: edges, vertices: top, bad: bad };
  }
  function readInts(text) {
    var out = [], bad = null;
    String(text).split(/[\s,]+/).forEach(function (t) {
      if (!t || bad) return;
      var v = parseInt(t, 10);
      if (!isFinite(v)) { bad = '"' + t + '" is not a whole number'; return; }
      out.push(v);
    });
    if (!bad && !out.length) bad = 'nothing was read';
    return { values: out, bad: bad };
  }

  function build(kind, spec) {
    if (kind === 'uniform') {
      var k = parseInt(spec, 10);
      if (!isFinite(k) || k < 0) return { bad: 'the rank has to be a whole number' };
      return { ground: [0, 1, 2, 3, 4], oracle: uniformOracle(k), edges: null,
               describe: 'every subset of size at most ' + k };
    }
    if (kind === 'partition') {
      var g = readInts(spec);
      if (g.bad) return { bad: g.bad };
      var groups = g.values.map(function (v) { return v - 1; });
      var caps = [];
      groups.forEach(function (v) { while (caps.length <= v) caps.push(1); });
      if (groups.some(function (v) { return v < 0; })) return { bad: 'groups are numbered from 1' };
      return { ground: groups.map(function (_, i) { return i; }),
               oracle: partitionOracle(groups, caps), edges: null, groups: groups,
               describe: 'at most one element from each of the ' + caps.length + ' groups' };
    }
    var e = readEdges(spec);
    if (e.bad) return { bad: e.bad };
    if (kind === 'graphic') {
      return { ground: e.edges.map(function (_, i) { return i; }),
               oracle: forestOracle(e.edges, e.vertices), edges: e.edges, vertices: e.vertices,
               describe: 'the edge sets that contain no cycle' };
    }
    return { ground: e.edges.map(function (_, i) { return i; }),
             oracle: matchingOracle(e.edges), edges: e.edges, vertices: e.vertices,
             describe: 'the edge sets no two of which share a vertex' };
  }

  function redraw() {
    var p = MTP[presetIn.value];
    var kind = p ? p.kind : 'uniform';
    var fam = build(kind, specIn.value);
    if (fam.bad) { blank(fam.bad); return; }
    /* One guard for all four families rather than three: everything below
       enumerates 2^n subsets and then every ordered pair of what survives, and
       independenceEnumerate throws above ten. Refusing here, by name, is the
       difference between a panel that says why and a panel that is blank. */
    if (fam.ground.length > 6) {
      blank('this mode lists every subset and then tests every ordered pair of the family, so '
            + 'it takes at most 6 elements and was given ' + fam.ground.length);
      return;
    }
    var wr = readInts(wIn.value);
    if (wr.bad) { blank(wr.bad); return; }
    var weights = wr.values;
    if (weights.length !== fam.ground.length) {
      blank('there are ' + fam.ground.length + ' elements and ' + weights.length + ' weights');
      return;
    }

    var enumerated = independenceEnumerate(fam.ground, fam.oracle);
    var family = enumerated.result.family;
    var closed = downwardClosed(family);
    var ex = exchangeTest(family);
    var run = matroidGreedy(family, weights, fam.ground);
    var beat = null, why = '';
    try { beat = beatingWeights(family, fam.ground); } catch (err) { why = String(err.message); }

    document.getElementById('mtN').textContent = String(fam.ground.length);
    document.getElementById('mtFam').textContent = String(family.length);
    document.getElementById('mtRank').textContent = String(enumerated.result.rank);
    document.getElementById('mtPairs').textContent = String(ex.tested);
    document.getElementById('mtIs').textContent = ex.isMatroid ? 'yes' : 'no';
    document.getElementById('mtGreedy').textContent = run.result.matches ? 'yes' : 'NO';

    if (fam.edges) {
      plot.innerHTML = edgesSvg(fam.edges, fam.vertices,
                                { width: 500, height: 190, highlight: run.result.chosen,
                                  weights: weights });
    } else {
      var bars = fam.ground.map(function (_, i) { return { s: i, f: i + 1, label: gyLabel(i) }; });
      plot.innerHTML = intervalsSvg(bars, {
        width: 500, rowH: 22,
        chosen: bars.filter(function (b, i) { return run.result.chosen.indexOf(i) !== -1; })
      });
    }

    var rows = '';
    var shown = family.slice().sort(function (a, b) { return a.length - b.length; });
    shown.slice(0, 14).forEach(function (s) {
      rows += '<tr><td>{' + s.map(gyLabel).join(', ') + '}</td><td>' + s.length + '</td>'
        + '<td>' + (isIndependent(fam.oracle, s) ? 'the oracle agrees' : 'ORACLE DISAGREES')
        + '</td></tr>';
    });
    if (shown.length > 14) {
      rows += '<tr><td>…</td><td colspan="2">' + (shown.length - 14) + ' more</td></tr>';
    }
    ex.failures.slice(0, 4).forEach(function (f) {
      rows += '<tr class="tone-red"><td>{' + f.A.map(gyLabel).join(', ') + '}</td>'
        + '<td>{' + f.B.map(gyLabel).join(', ') + '}</td>'
        + '<td>nothing in the second can join the first</td></tr>';
    });
    famT.innerHTML = '<thead><tr><th>independent set</th><th>size</th><th>check</th></tr></thead>'
      + '<tbody>' + rows + '</tbody>';

    var rrows = '';
    run.trace.forEach(function (st) {
      rrows += '<tr class="' + (st.taken ? 'tone-cyan' : '') + '"><th class="rowhead">'
        + gyLabel(st.element) + '</th><td>' + st.weight + '</td><td>'
        + (st.taken ? 'added' : 'would break independence') + '</td></tr>';
    });
    rrows += '<tr class="tone-cyan"><th class="rowhead">greedy</th><td>' + run.result.value
      + '</td><td>{' + run.result.chosen.map(gyLabel).join(', ') + '}</td></tr>';
    rrows += '<tr class="tone-amber"><th class="rowhead">best in the family</th><td>'
      + run.result.optimum + '</td><td>{'
      + (run.result.optimal || []).map(gyLabel).join(', ') + '}</td></tr>';
    runT.innerHTML = '<thead><tr><th>element</th><th>weight</th><th>greedy</th></tr></thead>'
      + '<tbody>' + rrows + '</tbody>';

    var note = p ? p.note : '';
    status.innerHTML = 'The family is ' + fam.describe + ': <strong>' + family.length
      + '</strong> of the ' + enumerated.counts.nodes + ' subsets pass the test, the rank is '
      + enumerated.result.rank + ', and it '
      + (closed.ok ? 'is downward closed — dropping an element from an independent set leaves '
                     + 'one, which greedy needs before anything else'
                   : '<span class="tone-red">is not downward closed</span>')
      + '. The exchange property was tested on all <strong>' + ex.tested
      + '</strong> ordered pairs and '
      + (ex.isMatroid
          ? 'held on every one, so this is a <span class="tone-cyan">matroid</span>.'
          : 'failed on <span class="tone-red">' + ex.failures.length + '</span> of them, so it '
            + 'is <span class="tone-red">not</span> a matroid.')
      + ' On the weights typed, greedy gets ' + run.result.value + ' and the best member of the '
      + 'family is worth ' + run.result.optimum + '. '
      + (beat === null
          ? '<span class="tone-amber">The search over weightings was refused: ' + why + '.</span>'
          : (beat.weights
              ? 'Searching ' + beat.tried + ' of the ' + beat.total + ' weightings in {1,2,3}^'
                + fam.ground.length + ' found one where greedy loses: weights '
                + beat.weights.join(' ') + ' give greedy ' + beat.greedy + ' against '
                + beat.optimum + '. That is the half of Rado and Edmonds that bites — a family '
                + 'that is not a matroid always has such a weighting, and here it is.'
              : 'All ' + beat.total + ' weightings in {1,2,3}^' + fam.ground.length
                + ' were tried and greedy matched the optimum on every one of them, which is '
                + 'what the exchange property buys.'))
      + (note ? ' <span class="tone-muted">' + note + '.</span>' : '');
  }

  presetIn.addEventListener('change', function () {
    var p = MTP[presetIn.value];
    if (p) { specIn.value = p.spec; wIn.value = p.weights; }
    redraw();
  });
  [specIn, wIn].forEach(function (el) {
    el.addEventListener('input', redraw);
    el.addEventListener('change', redraw);
  });
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="What makes greedy work, exactly",
        subtitle="The exchange property on every pair, and the weighting that beats greedy when it fails",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Choose the family and the weights"),
        panel_intro=cfg.get(
            "panel_intro",
            "The family is defined by a membership test and listed by running that test on "
            "every subset. Nothing here labels a family a matroid: the exchange property is "
            "tested pair by pair, and the counterexample weighting is searched for rather "
            "than quoted.",
        ),
        script=script,
    )


# ---------------------------------------------------------------------------
# stable -- the proposal sequence, and every stable matching beside it
# ---------------------------------------------------------------------------

_SM_PRESETS = [
    {
        "id": "classic",
        "label": "four on each side, several stable matchings",
        "a": "1 2 3 4; 2 1 3 4; 3 4 1 2; 4 3 1 2",
        "b": "4 3 2 1; 3 4 1 2; 2 1 4 3; 1 2 3 4",
        "note": "the proposers all get their first choice and the receivers all get their "
                "last, which is the asymmetry in its starkest form",
    },
    {
        "id": "unique",
        "label": "three, and only one stable matching exists",
        "a": "1 2 3; 1 2 3; 1 2 3",
        "b": "1 2 3; 1 2 3; 1 2 3",
        "note": "everyone agrees on the ranking, so there is nothing for the algorithm to "
                "choose and both sides get the same answer",
    },
    {
        "id": "twosided",
        "label": "three, where the two sides want opposite things",
        "a": "1 2 3; 2 3 1; 3 1 2",
        "b": "2 3 1; 3 1 2; 1 2 3",
        "note": "three stable matchings exist and the algorithm reaches the one its proposers "
                "prefer",
    },
    {
        "id": "rejections",
        "label": "four, where one rejection already costs a fifth proposal",
        "a": "2 1 4 3; 2 3 1 4; 1 2 3 4; 4 1 3 2",
        "b": "3 4 1 2; 1 2 3 4; 2 1 4 3; 4 3 2 1",
        "note": "B2 is holding its own first choice when A2 asks, so A2 is refused and has "
                "to ask again — five proposals for four people, and nobody is ever displaced. "
                "The matching it reaches is the only stable one, and it gives every receiver "
                "their first choice",
    },
]


def _stable(cfg):
    chosen = _chosen(_SM_PRESETS, cfg)
    markup = (
        _toolbar(
            "Every proposal, and an empty list of blocking pairs",
            "stability is checked against every pair, and against every other matching",
            [("cyan", "matched"), ("amber", "a proposal that was rejected"),
             ("red", "a blocking pair")],
        )
        + _stage(_svg("smPlot", "0 0 300 190",
                      "The matching, proposers on the left and receivers on the right.")
                 + _svg("smFlip", "0 0 300 190",
                        "The same instance with the sides swapped, so the two answers can be "
                        "compared."))
        + _table("smSteps")
        + _table("smAll")
        + _banner("smStatus")
    )
    controls = (
        _select("smPreset", "Instance", _options(_SM_PRESETS), chosen["id"])
        + _text("smA", "Each proposer's ranking, rows separated by semicolons", chosen["a"])
        + _text("smB", "Each receiver's ranking", chosen["b"])
        + _kpis([("People on each side", "smN"), ("Proposals made", "smProps"),
                 ("Blocking pairs", "smBlock"),
                 ("Stable matchings in total", "smStable"),
                 ("Mean rank, proposers", "smRankA"),
                 ("Mean rank, receivers", "smRankB")])
        + _hint(
            "smHint",
            "A row is a full ranking: <span class=\"tt\">2 1 3 4</span> means this person "
            "prefers 2, then 1, then 3, then 4. A <em>blocking pair</em> is two people who "
            "would both rather have each other than their partners; a matching is stable when "
            "no such pair exists. The page prints the list and it is empty &mdash; and beside "
            "it, every one of the n! matchings, with the stable ones picked out by the same "
            "test.",
        )
    )
    script = _CORE_JS + _CHECKED + _presets_js(
        "SMP", _SM_PRESETS, ["a", "b", "note"]) + r"""
  var presetIn = document.getElementById('smPreset');
  var aIn = document.getElementById('smA'), bIn = document.getElementById('smB');
  var plot = document.getElementById('smPlot'), flip = document.getElementById('smFlip');
  var stepsT = document.getElementById('smSteps'), allT = document.getElementById('smAll');
  var status = document.getElementById('smStatus');
  var KPIS = ['smN', 'smProps', 'smBlock', 'smStable', 'smRankA', 'smRankB'];

  function blank(why) {
    plot.innerHTML = ''; flip.innerHTML = ''; stepsT.innerHTML = ''; allT.innerHTML = '';
    for (var i = 0; i < KPIS.length; i += 1) document.getElementById(KPIS[i]).textContent = '—';
    status.innerHTML = '<span class="tone-red">' + why + '.</span> A row is a full ranking, '
      + 'as <span class="tt">2 1 3</span>, and rows are separated by semicolons.';
  }

  function redraw() {
    var A = gyParsePrefs(aIn.value), B = gyParsePrefs(bIn.value);
    if (A.bad) { blank('the proposers: ' + A.bad); return; }
    if (B.bad) { blank('the receivers: ' + B.bad); return; }
    if (A.rows.length !== B.rows.length) {
      blank('there are ' + A.rows.length + ' proposers and ' + B.rows.length + ' receivers');
      return;
    }
    var n = A.rows.length;
    var run = galeShapley(A.rows, B.rows);
    var block = blockingPairs(run.result.matchA, A.rows, B.rows);
    var other = galeShapley(B.rows, A.rows);
    var otherA = invertMatch(other.result.matchA, n);
    var otherBlock = blockingPairs(otherA, A.rows, B.rows);
    var every = null, why = '';
    try { every = everyStableMatching(A.rows, B.rows); } catch (err) { why = String(err.message); }
    var po = every ? proposerOptimal(run.result.matchA, A.rows, every) : null;

    document.getElementById('smN').textContent = String(n);
    document.getElementById('smProps').textContent = String(run.result.proposals);
    document.getElementById('smBlock').textContent = String(block.pairs.length);
    document.getElementById('smStable').textContent = every ? String(every.stable.length) : '—';
    document.getElementById('smRankA').textContent = Rtext(run.result.meanProposerRank)
      + ' = ' + Rfixed(run.result.meanProposerRank, 2);
    document.getElementById('smRankB').textContent = Rtext(run.result.meanReceiverRank)
      + ' = ' + Rfixed(run.result.meanReceiverRank, 2);

    plot.innerHTML = matchSvg(run.result.matchA, n, { leftLabel: 'proposers', rightLabel: 'receivers' });
    flip.innerHTML = matchSvg(otherA, n, { leftLabel: 'same side, now asked', rightLabel: 'now proposing' });

    var rows = '';
    run.trace.forEach(function (st, i) {
      rows += '<tr class="' + (st.outcome === 'rejected' ? 'tone-amber' : '')
        + '"><th class="rowhead">' + (i + 1) + '</th><td>' + (st.proposer + 1) + '</td>'
        + '<td>' + (st.to + 1) + '</td><td>' + st.outcome + '</td></tr>';
    });
    stepsT.innerHTML = '<thead><tr><th>step</th><th>proposer</th><th>proposes to</th>'
      + '<th>outcome</th></tr></thead><tbody>' + rows + '</tbody>';

    var arows = '';
    if (every) {
      arows += '<tr class="tone-cyan"><th class="rowhead">proposers propose</th><td>'
        + run.result.matchA.map(function (b) { return b + 1; }).join(' ') + '</td><td>'
        + Rtext(meanRank(run.result.matchA, A.rows)) + '</td><td>'
        + Rtext(meanRank(invertMatch(run.result.matchA, n), B.rows)) + '</td></tr>';
      arows += '<tr class="tone-purple"><th class="rowhead">receivers propose</th><td>'
        + otherA.map(function (b) { return b + 1; }).join(' ') + '</td><td>'
        + Rtext(meanRank(otherA, A.rows)) + '</td><td>'
        + Rtext(meanRank(other.result.matchA, B.rows)) + '</td></tr>';
      every.stable.forEach(function (m, i) {
        if (i >= 6) return;
        arows += '<tr><th class="rowhead">stable #' + (i + 1) + '</th><td>'
          + m.map(function (b) { return b + 1; }).join(' ') + '</td><td>'
          + Rtext(meanRank(m, A.rows)) + '</td><td>'
          + Rtext(meanRank(invertMatch(m, n), B.rows)) + '</td></tr>';
      });
      if (every.stable.length > 6) {
        arows += '<tr><th class="rowhead">…</th><td colspan="3">'
          + (every.stable.length - 6) + ' more</td></tr>';
      }
    }
    allT.innerHTML = '<thead><tr><th>matching</th><th>partner of 1, 2, …</th>'
      + '<th>mean rank, proposers</th><th>mean rank, receivers</th></tr></thead><tbody>'
      + arows + '</tbody>';

    var note = SMP[presetIn.value] ? SMP[presetIn.value].note : '';
    status.innerHTML = 'The algorithm made <strong>' + run.result.proposals
      + '</strong> proposals and the matching it reached has <strong>' + block.pairs.length
      + '</strong> blocking pairs'
      + (block.pairs.length
          ? ': <span class="tone-red">' + block.pairs.map(function (p) {
              return (p[0] + 1) + ' and ' + (p[1] + 1); }).join(', ')
            + '</span>, which should be impossible'
          : ' — the list was built by checking every one of the ' + (n * (n - 1))
            + ' ordered pairs, and printing an empty list is the point')
      + '. ' + (every
          ? 'Of all ' + every.matchings + ' matchings, <strong>' + every.stable.length
            + '</strong> are stable, and this one '
            + (every.stable.some(function (m) {
                 return m.join(',') === run.result.matchA.join(','); })
                ? 'is among them. '
                : '<span class="tone-red">is not among them</span>. ')
            + (po && po.optimal
                ? 'Every proposer got the best partner they have in ANY stable matching, which '
                  + 'is proposer-optimality — computed from the list, not from the algorithm. '
                : '<span class="tone-red">Some proposer could do better in another stable '
                  + 'matching.</span> ')
          : '<span class="tone-amber">The enumeration was refused: ' + why + '.</span> ')
      + 'Swapping the sides gives a matching with '
      + otherBlock.pairs.length + ' blocking pairs and mean ranks '
      + Rtext(meanRank(otherA, A.rows)) + ' and ' + Rtext(meanRank(other.result.matchA, B.rows))
      + ', against ' + Rtext(run.result.meanProposerRank) + ' and '
      + Rtext(run.result.meanReceiverRank) + ' — '
      + (Rcmp(meanRank(otherA, A.rows), run.result.meanProposerRank) >= 0
          ? 'proposing is at least as good for the side that does it, on this instance.'
          : 'on this instance the side that proposes does no better, which happens when the '
            + 'stable matching is unique.')
      + (note ? ' <span class="tone-muted">' + note + '.</span>' : '');
  }

  presetIn.addEventListener('change', function () {
    var p = SMP[presetIn.value];
    if (p) { aIn.value = p.a; bIn.value = p.b; }
    redraw();
  });
  [aIn, bIn].forEach(function (el) {
    el.addEventListener('input', redraw);
    el.addEventListener('change', redraw);
  });
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="Stability, and who the algorithm favours",
        subtitle="An empty blocking-pair list, and every stable matching beside it",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Choose the preference lists"),
        panel_intro=cfg.get(
            "panel_intro",
            "The blocking-pair list is built by checking every ordered pair, and the same test "
            "is applied to all n! matchings. Proposer-optimality is then read off that list "
            "rather than taken from the algorithm that produced one of them.",
        ),
        script=script,
    )


# ---------------------------------------------------------------------------
# caching -- three policies against the true offline optimum
# ---------------------------------------------------------------------------

_CA_PRESETS = [
    {
        "id": "mixed",
        "label": "thirteen references over five pages",
        "spec": "1 2 3 1 4 1 2 5 1 2 3 4 5",
        "slots": "3",
        "note": "farthest-in-future beats both online policies here, and the gap is what no "
                "online policy can close",
    },
    {
        "id": "belady",
        "label": "the trace FIFO gets worse on",
        "spec": "1 2 3 4 1 2 5 1 2 3 4 5",
        "slots": "3",
        "note": "FIFO with four slots gets FEWER hits than with three, which is the anomaly "
                "and the reason a bigger cache is not automatically better",
    },
    {
        "id": "loop",
        "label": "a loop one page too long for the cache",
        "spec": "1 2 3 4 1 2 3 4 1 2 3 4",
        "slots": "3",
        "note": "LRU evicts exactly the page about to be used and scores nothing at all, while "
                "the offline optimum keeps most of the loop",
    },
    {
        "id": "hot",
        "label": "one hot page among cold ones",
        "spec": "1 2 1 3 1 4 1 5 1 6 1 7",
        "slots": "2",
        "note": "LRU and farthest-in-future both hold the hot page and get five hits; FIFO "
                "evicts it by age and gets three, so an easy workload is not where the "
                "policies stop differing",
    },
]


def _caching(cfg):
    chosen = _chosen(_CA_PRESETS, cfg)
    markup = (
        _toolbar(
            "Three policies, and the best any offline policy could do",
            "the bound is searched over every eviction decision, not quoted",
            [("cyan", "a hit"), ("muted", "a miss"), ("red", "a bigger cache doing worse")],
        )
        + _stage(_svg("caPlot", "0 0 660 80",
                      "The reference trace, each position marked hit or miss under the chosen "
                      "policy."))
        + _table("caPolicies")
        + _table("caSweep")
        + _banner("caStatus")
    )
    controls = (
        _select("caPreset", "Reference trace", _options(_CA_PRESETS), chosen["id"])
        + _text("caSpec", "Page numbers, in the order they are referenced", chosen["spec"])
        + _text("caSlots", "Cache slots", chosen["slots"])
        + _select("caPolicy", "Draw the marks for",
                  [("lru", "least recently used"), ("fifo", "first in, first out"),
                   ("opt", "farthest in future")], "lru")
        + _kpis([("References", "caN"), ("Hits under this policy", "caHits"),
                 ("Hit rate", "caRate"),
                 ("Best any offline policy can do", "caOpt"),
                 ("Farthest-in-future reaches it", "caReach"),
                 ("A bigger cache ever does worse", "caAnom")])
        + _hint(
            "caHint",
            "The cache holds a fixed number of pages and every miss loads the referenced page, "
            "so the only decision is which page to throw out. Farthest-in-future needs the "
            "whole trace in advance and is therefore not implementable &mdash; it is the "
            "<em>bound</em>. The last column checks it by searching every eviction decision "
            "the cache could ever make.",
        )
    )
    script = _CORE_JS + _CHECKED + _presets_js(
        "CAP", _CA_PRESETS, ["spec", "slots", "note"]) + r"""
  var presetIn = document.getElementById('caPreset'), specIn = document.getElementById('caSpec');
  var slotsIn = document.getElementById('caSlots'), polIn = document.getElementById('caPolicy');
  var plot = document.getElementById('caPlot');
  var polT = document.getElementById('caPolicies'), sweepT = document.getElementById('caSweep');
  var status = document.getElementById('caStatus');
  var KPIS = ['caN', 'caHits', 'caRate', 'caOpt', 'caReach', 'caAnom'];
  var POL_NAME = { lru: 'least recently used', fifo: 'first in, first out',
                   opt: 'farthest in future' };

  function blank(why) {
    plot.innerHTML = ''; polT.innerHTML = ''; sweepT.innerHTML = '';
    for (var i = 0; i < KPIS.length; i += 1) document.getElementById(KPIS[i]).textContent = '—';
    status.innerHTML = '<span class="tone-red">' + why + '.</span> A trace is page numbers '
      + 'separated by spaces.';
  }

  function redraw() {
    var parsed = gyParseTrace(specIn.value);
    if (parsed.bad) { blank(parsed.bad); return; }
    var trace = parsed.trace;
    var k = parseInt(slotsIn.value, 10);
    if (!isFinite(k) || k < 1 || k > 6) { blank('the cache holds between 1 and 6 pages'); return; }
    var policy = polIn.value;

    var here = replayPolicy(trace, k, policy);
    var best = null, why = '';
    try { best = everyEviction(trace, k); } catch (err) { why = String(err.message); }
    var optRun = replayPolicy(trace, k, 'opt');
    var sweep = beladySweep(trace, 6, 'fifo');

    document.getElementById('caN').textContent = String(trace.length);
    document.getElementById('caHits').textContent = String(here.hits);
    document.getElementById('caRate').textContent = Rtext(here.rate) + ' = ' + Rpct(here.rate, 1);
    document.getElementById('caOpt').textContent = best ? String(best.hits) : '—';
    document.getElementById('caReach').textContent = best
      ? (optRun.hits === best.hits ? 'yes' : 'NO') : '—';
    document.getElementById('caAnom').textContent = sweep.anomalies.length ? 'yes' : 'no';

    plot.innerHTML = traceSvg(trace, replayMarks(trace, k, policy), {});

    var rows = '';
    ['fifo', 'lru', 'opt'].forEach(function (p) {
      var r = replayPolicy(trace, k, p);
      rows += '<tr class="' + (p === policy ? 'tone-cyan' : '') + '"><th class="rowhead">'
        + POL_NAME[p] + '</th><td>' + r.hits + '</td><td>' + r.misses + '</td><td>'
        + Rtext(r.rate) + '</td><td>' + Rpct(r.rate, 1) + '</td></tr>';
    });
    if (best) {
      rows += '<tr class="tone-amber"><th class="rowhead">the best any offline policy can do'
        + '</th><td>' + best.hits + '</td><td>' + best.misses + '</td><td>'
        + Rtext(best.rate) + '</td><td>' + Rpct(best.rate, 1) + '</td></tr>';
    }
    polT.innerHTML = '<thead><tr><th>policy</th><th>hits</th><th>misses</th><th>rate</th>'
      + '<th>as a percentage</th></tr></thead><tbody>' + rows + '</tbody>';

    var srows = '';
    sweep.rows.forEach(function (r, i) {
      var worse = i > 0 && r.hits < sweep.rows[i - 1].hits;
      srows += '<tr class="' + (worse ? 'tone-red' : (r.k === k ? 'tone-cyan' : ''))
        + '"><th class="rowhead">' + r.k + ' slot' + (r.k === 1 ? '' : 's') + '</th><td>'
        + r.hits + '</td><td>' + r.misses + '</td><td>' + Rtext(r.rate) + '</td><td>'
        + (worse ? 'FEWER hits than with ' + (r.k - 1) : '') + '</td></tr>';
    });
    sweepT.innerHTML = '<thead><tr><th>FIFO cache size</th><th>hits</th><th>misses</th>'
      + '<th>rate</th><th></th></tr></thead><tbody>' + srows + '</tbody>';

    var note = CAP[presetIn.value] ? CAP[presetIn.value].note : '';
    status.innerHTML = 'Over ' + trace.length + ' references with ' + k + ' slot'
      + (k === 1 ? '' : 's') + ', ' + POL_NAME[policy] + ' gets <strong>' + here.hits
      + '</strong> hits, a rate of ' + Rtext(here.rate) + '. '
      + (best
          ? 'Searching every eviction decision — ' + best.states
            + ' distinct (position, cache) states — the most any offline policy can get is '
            + '<strong>' + best.hits + '</strong>, and farthest-in-future gets ' + optRun.hits
            + ', so it '
            + (optRun.hits === best.hits
                ? 'attains the bound. That is the optimality claim checked rather than cited, '
                  + 'and it is why no online policy can be compared against anything better.'
                : '<span class="tone-red">does not attain the bound</span>.')
          : '<span class="tone-amber">The exhaustive search was refused: ' + why + '.</span>')
      + ' Sweeping FIFO from one slot to six, '
      + (sweep.anomalies.length
          ? '<span class="tone-red">a bigger cache does worse</span> at '
            + sweep.anomalies.map(function (a) {
                return a.from + ' to ' + a.to + ' (' + a.lost + ' hit'
                  + (a.lost === 1 ? '' : 's') + ' lost)'; }).join(' and ')
            + ' — Belady\'s anomaly, on the trace in front of you rather than in a footnote.'
          : 'the hit count never falls as the cache grows on this trace, which is common and is '
            + 'not a guarantee: try the second preset.')
      + (note ? ' <span class="tone-muted">' + note + '.</span>' : '');
  }

  presetIn.addEventListener('change', function () {
    var p = CAP[presetIn.value];
    if (p) { specIn.value = p.spec; slotsIn.value = p.slots; }
    redraw();
  });
  [specIn, slotsIn, polIn].forEach(function (el) {
    el.addEventListener('input', redraw);
    el.addEventListener('change', redraw);
  });
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="The policy you cannot implement, and why it is still the answer",
        subtitle="FIFO, LRU and farthest-in-future against a search over every eviction",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Choose the trace and the cache size"),
        panel_intro=cfg.get(
            "panel_intro",
            "Farthest-in-future needs the whole trace in advance, so it is a bound rather than "
            "a policy. The bound is checked here by searching every eviction decision a cache "
            "of this size could make, which knows nothing about looking ahead.",
        ),
        script=script,
    )


# ---------------------------------------------------------------------------
# An unknown mode raises, and the raise is the contract rather than
# defensiveness: a kit that fell back to a default would render a
# finished-looking page carrying another lesson's widget under this lesson's
# title, and nothing downstream would notice.
# ---------------------------------------------------------------------------

_MODES = {
    "intervals": _intervals,
    "partition": _partition,
    "huffman": _huffman,
    "knapsack": _knapsack,
    "matroid": _matroid,
    "stable": _stable,
    "caching": _caching,
}

MODES = tuple(sorted(_MODES))


def greedy_lab(cfg):
    """The greedy course's kit. `cfg["mode"]` chooses the lesson; unknown raises."""
    mode = (cfg or {}).get("mode")
    if mode not in _MODES:
        raise ValueError(
            "greedy_lab: unknown mode %r; the seven greedy modes are %s"
            % (mode, ", ".join(MODES))
        )
    return _MODES[mode](cfg or {})


__all__ = ["greedy_lab", "GKIT_JS", "MODES"]
