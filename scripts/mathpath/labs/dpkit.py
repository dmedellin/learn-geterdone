"""Dynamic Programming and Optimal Substructure -- course 5's kit, nine modes.

WHAT A DYNAMIC PROGRAM ACTUALLY IS, and what this kit is built to make
checkable. A DP is three things: a table, a fill ORDER, and a recurrence. The
thing readers get wrong is never the recurrence. It is WHICH CELLS A CELL READS
and whether those cells are filled yet, which is invisible in a finished table
and fatal in a wrong one. So `algo_core.dpFill` records, for every cell, the
cells the recurrence's own `get` asked for while that cell was being computed,
and the modes paint them. That dependency list cannot disagree with what the
code did, because it is not a description of the recurrence -- it is a
recording of it.

THREE ROUTES TO EVERY ANSWER, which is the discipline this kit is held to.
A table is easy to fill confidently and wrongly, and a wrong table looks
exactly like a right one. So no mode prints a table's answer alone:

    memo        a memo-free recursion, a memoised one, and the table. Three
                routes; the counts differ by orders of magnitude and the
                ANSWER does not.
    knapsack    the table against ORACLE_JS.knapsackBrute, and the picks the
                reconstruction returns are re-weighed against the capacity and
                re-valued against the table's number.
    edit        the table against a memo-free recursion, and the edit script
                is APPLIED to the first string -- character by character,
                refusing if a delete does not find the character it names --
                and the result compared with the second.
    chain       the table against every parenthesisation, enumerated; and the
                split tree the reconstruction returns is re-costed from the
                dimensions alone.
    lis         the n^2 table, the tails array, and every one of the 2^n
                subsequences. Three lengths; and the subsequence returned is
                checked to be increasing AND to be a subsequence of the input,
                which the tails array is not.
    coins       the DP row against a memo-free counting recursion, and the
                combinations listed one by one at small amounts.
    tree        the one-pass tree DP against DP_JS's misBrute over every
                subset, and the chosen set re-checked independent.
    game        the labelled table against a memo-free minimax recursion.
    tsp         Held-Karp against ORACLE_JS.tspBrute, and the tour it returns
                re-measured from the distance matrix.

EVERY PRESET PINS WHAT IT PRINTS, AND NO PRESET CARRIES PROSE ANY MORE. Each
of the 36 presets used to carry a `note`, and this kit RENDERED the selected
one into its status banner -- which is as visible as a string in this
repository ever gets, and the fifteen-kit sweep still found five or six of the
36 false about the lab they described. One said the memo turned tens of
thousands of calls "into nineteen", in the same banner line where the page
printed 50 and 18.
Rendering prose does not check it. So the note is gone from every preset here,
and the slot it occupied holds `expect`: {kpi element id: the exact text the
page prints}. scripts/labcheck.js selects the option on the BUILT page,
dispatches the menu's own change handler and compares the tile's textContent.
See `_expect` below and scripts/mathpath/AGENTS.md for the rule.

THE FILL ORDER IS A FIRST-CLASS CONTROL, in `chain` and in `coins`, because
both lessons ARE the order:

  * matrix chain filled row-major reads cells that are still null, and null
    plus a number is a number, so the table finishes and is wrong. The mode
    runs both orders and prints both answers beside the enumeration. Nothing
    is described; the wrong number is on the screen.
  * counting change with the coins outside counts COMBINATIONS and with the
    amounts outside counts ORDERED SEQUENCES, and readers write the second
    while meaning the first. Both are computed and, at small amounts, the
    objects themselves are listed so the difference is visible rather than
    numeric.

EXACTNESS. Every count of ways is a BigInt, because they overflow a double
long before they stop being interesting: the number of ordered ways to make 60
from {1, 2, 5} is past 2^53 and a page that printed it as a float would print
a number that is merely close. `countWays` returns BigInt and this kit never
converts one to a Number. Distances, values, weights, table entries, call
counts and cell counts are integers. Two ratios are fractions and are printed
as fractions over RATIONAL_JS: the calls a memo saves, and Held-Karp's work
against brute force's. Nothing on these pages is rounded except where `Rfixed`
renders a decimal BESIDE a fraction, at a stated number of places, for
reading.

WHAT IS REUSED AND WHAT THIS KIT ADDS. `algo_core.DP_JS` holds dpOrder,
dpFill, reconstruct, lisTails, treeDp, misBrute, countWays, listCombinations,
oneRow, gameLabels and heldKarp, and nothing here reimplements one. What this
kit adds is the second and third routes, and the checks on what comes back:

  naiveMinCoins/
  memoMinCoins        the same recursion twice, one with a memo and one
                      without, both counted. The point of the mode is the
                      ratio between the two call counts and the fact that the
                      answers are equal.
  reconstructPicks    walks dpFill's `from` back to the origin and returns the
                      items, which `reconstruct` gives as cell coordinates and
                      not as an answer.
  packCheck           re-weighs and re-values a set of picks. A reconstruction
                      that returns the wrong items still returns a plausible
                      list, and only re-costing it catches that.
  editScript/
  applyScript         the script as operations, and the operations performed.
                      applyScript refuses when a delete or a keep does not
                      find the character it names, so a script that is the
                      right LENGTH and the wrong content cannot pass.
  editNaive           the same distance by a memo-free recursion.
  everyParenthesisation  every way of bracketing the product, by a recursion
                      that has no table at all. Catalan(n-1) of them.
  chainSplitTree/
  parenCost           the reconstruction as a tree, re-costed from the
                      dimensions. The table's number and the tree's cost are
                      then two numbers rather than one printed twice.
  lisTable            the n^2 dynamic program with predecessors, which
                      `lisTails` is not -- the tails array has the right
                      LENGTH and usually the wrong contents.
  lisBrute            every one of the 2^n subsequences.
  isIncreasingRun/
  isSubsequenceOf     the two properties the answer must have, checked
                      separately, because a sorted copy of the input has one
                      of them and is not an answer.
  countBrute          the number of combinations and of ordered sequences by
                      memo-free recursion, in BigInt.
  treeFromEdges/
  isIndependentSet    an edge list read as a tree -- refusing anything that is
                      not one -- and the chosen set checked against the edges.
  gameBrute           win and lose by memo-free minimax, so the labelled table
                      is checked and not merely displayed.
  tourValid/
  tourLength          the tour visits every city exactly once and returns to
                      the start, and its length is re-added from the matrix.

  dpGridSvg           the table drawn, with the cell being explained and the
                      cells it read painted differently. Shared by four modes,
                      and it takes the table as an argument and returns a
                      string, which is what makes it testable at all.

TWO OBSERVATIONS ABOUT ROUTINES THIS KIT DOES NOT OWN, recorded here because
both cost time to rediscover:

  * `heldKarp` and `tspBrute` return a tour as an OPEN list of n cities
    beginning at 0. The leg home is counted in the length and is NOT in the
    list, so re-measuring the list as written gives a tour one leg short --
    which looks like an off-by-one in the DP rather than a convention. This
    kit's `tourLength` closes the cycle, `tourValid` checks the list is a
    permutation starting at 0, and scripts/mathcheck.js asserts the convention
    directly so it cannot change quietly.
  * `dpFill`'s `get` returns null for a cell outside the table AND for a cell
    inside it that has not been filled yet, and `null + 3` is `3`. That is not
    a defect -- it is what makes the `chain` mode's wrong fill order produce a
    finished table with a wrong number rather than a crash -- but any new
    recurrence has to know it, because a recurrence that reads too early will
    not tell you.

THE MODES, and the lesson each belongs to:

  memo      the same recursion three ways, and the call counts that separate
            them
  knapsack  the grid, what each cell read, the reconstruction re-weighed, and
            the one-row version with the two loop directions
  edit      the table, the script, and the script performed
  chain     fill by length against fill by row, and every parenthesisation
  lis       the table, the tails array, and every subsequence
  coins     the loop order that decides whether you are counting combinations
            or sequences
  tree      one postorder pass against every subset
  game      won and lost positions, and the period a reader is asked to find
  tsp       2^n subsets against (n-1)! tours, both as exact integers

PAGE WEIGHT, MEASURED RATHER THAN ESTIMATED. One core for the kit,
concatenated once, as `heap.py` does. It is 66.2 KB raw and 19.9 KB gzipped,
and a rendered lesson page runs from 39.4 KB gzipped (`game`) to 40.4 KB
(`memo`) against a measured ceiling of 62 KB (AGENTS.md).

TREEDRAW_JS is used by `tree` alone and SERIES_JS by `memo` alone, so the other
seven modes carry 9.1 KB raw -- 2.9 KB gzipped -- of drawing code they never
call. That is the price of a kit that cannot call a function its page turned
out not to carry, and at 40 KB against 62 it is worth paying.
"""

from .algebra_core import RATIONAL_JS
from .algo_core import (
    COUNT_JS,
    DP_JS,
    ORACLE_JS,
    RFIXED_JS,
    SERIES_JS,
    TREEDRAW_JS,
)
from .common import Lab
from .counting import BIGINT_JS

# ---------------------------------------------------------------------------
# The arithmetic this kit adds. Top-level functions, no element touched, so
# scripts/mathcheck.js executes exactly the source that ships.
# ---------------------------------------------------------------------------

DPKIT_JS = r"""
  /* A cell that has no answer yet. Not Infinity: dpFill stores what the
     recurrence returns and a panel has to print it, and "1000000000" read as
     "no way to do it" is a caption, while Infinity read through a table
     renderer is a special case in five places. Every comparison below is
     against this constant. */
  var DP_NONE = 1000000000;
  function dpUnreachable(v) { return v === null || v >= DP_NONE; }

  /* ================================================== what a reader types */
  function dpParseNums(text, cap, lo, hi) {
    cap = cap === undefined ? 14 : cap;
    var out = [], bad = null;
    String(text).split(/[\s,]+/).forEach(function (t) {
      if (!t || bad) return;
      var v = parseInt(t, 10);
      if (!isFinite(v) || String(v) !== t) { bad = '"' + t + '" is not a whole number'; return; }
      if (lo !== undefined && v < lo) { bad = t + ' is below ' + lo; return; }
      if (hi !== undefined && v > hi) { bad = t + ' is above ' + hi; return; }
      if (out.length >= cap) { bad = 'at most ' + cap + ' numbers here'; return; }
      out.push(v);
    });
    if (!bad && !out.length) bad = 'no numbers were read';
    return { values: out, bad: bad };
  }
  function dpParseItems(text, cap) {
    cap = cap === undefined ? 8 : cap;
    var out = [], bad = null;
    String(text).split(',').forEach(function (piece) {
      var t = piece.replace(/\s+/g, '');
      if (!t || bad) return;
      var m = /^(\d+)\/(\d+)$/.exec(t);
      if (!m) { bad = 'an item is written weight/value, as 3/4; "' + t + '" is not'; return; }
      var w = parseInt(m[1], 10), v = parseInt(m[2], 10);
      if (w <= 0) { bad = 'an item of weight 0 would be taken for nothing'; return; }
      if (out.length >= cap) { bad = 'at most ' + cap + ' items, because every subset is tried'; return; }
      out.push({ w: w, v: v, label: String.fromCharCode(65 + out.length) });
    });
    if (!bad && !out.length) bad = 'no items were read';
    return { items: out, bad: bad };
  }
  /* A word, restricted to letters, because the table is drawn with one column
     per character and a space is a column a reader cannot see. */
  function dpParseWord(text, cap) {
    cap = cap === undefined ? 10 : cap;
    var t = String(text).replace(/\s+/g, '');
    if (!/^[A-Za-z]*$/.test(t)) return { word: null, bad: 'letters only, so every column is visible' };
    if (t.length > cap) return { word: null, bad: 'at most ' + cap + ' letters, or the table leaves the page' };
    return { word: t, bad: null };
  }
  /* An edge list, `1-2, 1-3`, read as a TREE: n - 1 edges over n vertices,
     connected and acyclic. Anything else is refused, because the one-pass DP
     is a fact about trees and a graph with a cycle would produce a number. */
  function dpParseTree(text, cap) {
    cap = cap === undefined ? 12 : cap;
    var edges = [], bad = null, top = 0;
    String(text).split(',').forEach(function (piece) {
      var t = piece.replace(/\s+/g, '');
      if (!t || bad) return;
      var m = /^(\d+)-(\d+)$/.exec(t);
      if (!m) { bad = 'an edge is written 1-2; "' + t + '" is not'; return; }
      var a = parseInt(m[1], 10) - 1, b = parseInt(m[2], 10) - 1;
      if (a === b) { bad = 'a vertex cannot be joined to itself'; return; }
      if (a < 0 || b < 0) { bad = 'vertices are numbered from 1'; return; }
      top = Math.max(top, a + 1, b + 1);
      if (top > cap) { bad = 'at most ' + cap + ' vertices, because every subset is tried'; return; }
      edges.push([a, b]);
    });
    if (bad) return { bad: bad };
    if (!edges.length) return { bad: 'no edges were read' };
    var n = top;
    if (edges.length !== n - 1) {
      return { bad: 'a tree on ' + n + ' vertices has ' + (n - 1) + ' edges, and ' + edges.length + ' were given' };
    }
    var p = [], i;
    for (i = 0; i < n; i += 1) p.push(i);
    function find(a) { while (p[a] !== a) { p[a] = p[p[a]]; a = p[a]; } return a; }
    for (i = 0; i < edges.length; i += 1) {
      var ra = find(edges[i][0]), rb = find(edges[i][1]);
      if (ra === rb) return { bad: 'these edges contain a cycle, so they are not a tree' };
      p[ra] = rb;
    }
    var root = find(0);
    for (i = 0; i < n; i += 1) if (find(i) !== root) return { bad: 'vertex ' + (i + 1) + ' is not connected to vertex 1' };
    return { tree: treeFromEdges(edges, n), edges: edges, n: n, bad: null };
  }
  function treeFromEdges(edges, n) {
    var tree = {}, i;
    for (i = 0; i < n; i += 1) tree[i] = [];
    edges.forEach(function (e) { tree[e[0]].push(e[1]); tree[e[1]].push(e[0]); });
    return tree;
  }
  /* A square distance matrix, rows separated by semicolons. Asymmetric is
     allowed and nothing here assumes the triangle inequality. */
  function dpParseMatrix(text, cap) {
    cap = cap === undefined ? 8 : cap;
    var rows = [], bad = null;
    String(text).split(';').forEach(function (piece) {
      var t = piece.trim();
      if (!t || bad) return;
      var r = dpParseNums(t, 12, 0, 999);
      if (r.bad) { bad = r.bad; return; }
      rows.push(r.values);
    });
    if (bad) return { bad: bad };
    if (rows.length < 3) return { bad: 'at least three cities' };
    if (rows.length > cap) return { bad: 'at most ' + cap + ' cities, because every tour is tried' };
    for (var i = 0; i < rows.length; i += 1) {
      if (rows[i].length !== rows.length) {
        return { bad: 'row ' + (i + 1) + ' has ' + rows[i].length + ' entries and the matrix has ' + rows.length + ' rows' };
      }
    }
    return { D: rows, bad: null };
  }

  /* ============================================ memo: one recursion, three ways

     Minimum coins to make an amount. The recursion is f(0) = 0 and
     f(a) = 1 + min over coins of f(a - c), which is the shortest possible
     statement of optimal substructure, and it is run three times: with no
     memo, with one, and as a table. The three answers must agree; the three
     costs do not. */
  function naiveMinCoins(coins, amount, cap) {
    cap = cap === undefined ? 26 : cap;
    oracleCap('naiveMinCoins', amount, cap);
    var c = counter();
    function f(left) {
      c.calls += 1;
      if (left === 0) return 0;
      var best = DP_NONE;
      for (var i = 0; i < coins.length; i += 1) {
        if (coins[i] > left) continue;
        var v = f(left - coins[i]);
        if (v + 1 < best) best = v + 1;
      }
      return best;
    }
    var out = f(amount);
    return runOf({ coins: dpUnreachable(out) ? null : out }, usedCounts(c), []);
  }
  function memoMinCoins(coins, amount) {
    var c = counter(), memo = {};
    function f(left) {
      c.calls += 1;
      if (left === 0) return 0;
      if (memo[left] !== undefined) { c.reads += 1; return memo[left]; }
      var best = DP_NONE;
      for (var i = 0; i < coins.length; i += 1) {
        if (coins[i] > left) continue;
        var v = f(left - coins[i]);
        if (v + 1 < best) best = v + 1;
      }
      memo[left] = best;
      c.writes += 1;
      return best;
    }
    var out = f(amount);
    return runOf({ coins: dpUnreachable(out) ? null : out, distinct: Object.keys(memo).length },
                 usedCounts(c), []);
  }
  /* The same thing as a table, so the dependency painting has something to
     paint: one row per coin type, one column per amount. */
  function minCoinTable(coins, amount) {
    return dpFill({
      rows: coins.length + 1, cols: amount + 1, order: 'rowmajor',
      base: function (i, j) {
        if (i === 0) return j === 0 ? 0 : DP_NONE;
        return undefined;
      },
      cell: function (i, j, get) {
        var skip = get(i - 1, j), best = skip, from = [i - 1, j];
        if (coins[i - 1] <= j) {
          var take = get(i, j - coins[i - 1]);
          if (take + 1 < best) { best = take + 1; from = [i, j - coins[i - 1]]; }
        }
        return { v: best, from: from };
      }
    });
  }
  /* The coins the table says to use, walked back through `from`. */
  function minCoinPicks(filled, coins, amount) {
    var at = [coins.length, amount], out = [], guard = 0;
    while (guard < 4 * (amount + coins.length + 4)) {
      guard += 1;
      var f = filled.result.from[at[0]][at[1]];
      if (!f) break;
      if (f[0] === at[0]) out.push(coins[at[0] - 1]);
      at = f;
      if (at[1] === 0 && at[0] === 0) break;
    }
    return out.sort(function (a, b) { return b - a; });
  }

  /* ============================================================== knapsack */
  function knapTable(items, W) {
    return dpFill({
      rows: items.length + 1, cols: W + 1, order: 'rowmajor',
      base: function (i, j) { return i === 0 ? 0 : undefined; },
      cell: function (i, j, get) {
        var skip = get(i - 1, j);
        if (items[i - 1].w > j) return { v: skip, from: [i - 1, j] };
        var take = items[i - 1].v + get(i - 1, j - items[i - 1].w);
        return take > skip ? { v: take, from: [i - 1, j - items[i - 1].w] }
                           : { v: skip, from: [i - 1, j] };
      }
    });
  }
  /* The ITEMS, not the cells. `reconstruct` returns a path of coordinates,
     which is the right primitive and is not an answer: an item was taken
     exactly where the path's row drops AND its column moves. */
  function reconstructPicks(filled, items, W) {
    var path = reconstruct(filled.result, [items.length, W]), picks = [];
    for (var k = 0; k + 1 < path.length; k += 1) {
      var a = path[k], b = path[k + 1];
      if (a[0] - b[0] === 1 && a[1] !== b[1]) picks.push(a[0] - 1);
    }
    return { picks: picks.sort(function (x, y) { return x - y; }), path: path };
  }
  /* Re-weigh and re-value. A reconstruction that returns the wrong items
     returns a perfectly plausible list, and only re-costing it catches that. */
  function packCheck(items, picks, W, claimed) {
    var w = 0, v = 0;
    picks.forEach(function (i) { w += items[i].w; v += items[i].v; });
    return { weight: w, value: v, fits: w <= W, matches: v === claimed,
             ok: w <= W && v === claimed };
  }

  /* ========================================================= edit distance */
  function editTable(a, b) {
    return dpFill({
      rows: a.length + 1, cols: b.length + 1, order: 'rowmajor',
      base: function (i, j) {
        if (i === 0) return j;
        if (j === 0) return i;
        return undefined;
      },
      cell: function (i, j, get) {
        var same = a.charAt(i - 1) === b.charAt(j - 1);
        var sub = get(i - 1, j - 1) + (same ? 0 : 1);
        var del = get(i - 1, j) + 1;
        var ins = get(i, j - 1) + 1;
        var best = sub, from = [i - 1, j - 1];
        if (del < best) { best = del; from = [i - 1, j]; }
        if (ins < best) { best = ins; from = [i, j - 1]; }
        return { v: best, from: from };
      }
    });
  }
  /* The script, as operations on the first string. Walked back from the last
     cell and then reversed, so it reads in the order it would be performed. */
  function editScript(filled, a, b) {
    var i = a.length, j = b.length, out = [], guard = 0;
    while ((i > 0 || j > 0) && guard < (a.length + b.length + 4) * 2) {
      guard += 1;
      var f = filled.result.from[i][j];
      if (!f) {
        if (i > 0 && j === 0) { out.push({ op: 'delete', ch: a.charAt(i - 1), at: i }); i -= 1; continue; }
        if (j > 0 && i === 0) { out.push({ op: 'insert', ch: b.charAt(j - 1), at: j }); j -= 1; continue; }
        break;
      }
      if (f[0] === i - 1 && f[1] === j - 1) {
        if (a.charAt(i - 1) === b.charAt(j - 1)) out.push({ op: 'keep', ch: a.charAt(i - 1), at: i });
        else out.push({ op: 'substitute', from: a.charAt(i - 1), to: b.charAt(j - 1), at: i });
        i -= 1; j -= 1;
      } else if (f[0] === i - 1) {
        out.push({ op: 'delete', ch: a.charAt(i - 1), at: i });
        i -= 1;
      } else {
        out.push({ op: 'insert', ch: b.charAt(j - 1), at: j });
        j -= 1;
      }
    }
    out.reverse();
    return out;
  }
  /* PERFORM the script. Every operation names the character it acts on and
     this refuses if that character is not there, so a script of the right
     LENGTH and the wrong content cannot pass -- which is the failure a
     reconstruction actually has. */
  function applyScript(a, script) {
    var out = '', i = 0;
    for (var k = 0; k < script.length; k += 1) {
      var op = script[k];
      if (op.op === 'keep') {
        if (a.charAt(i) !== op.ch) return null;
        out += a.charAt(i); i += 1;
      } else if (op.op === 'substitute') {
        if (a.charAt(i) !== op.from) return null;
        out += op.to; i += 1;
      } else if (op.op === 'delete') {
        if (a.charAt(i) !== op.ch) return null;
        i += 1;
      } else if (op.op === 'insert') {
        out += op.ch;
      } else {
        return null;
      }
    }
    return i === a.length ? out : null;
  }
  function editCost(script) {
    var n = 0;
    script.forEach(function (op) { if (op.op !== 'keep') n += 1; });
    return n;
  }
  /* The same distance with no table at all, so the table is checked against
     something rather than against itself. Exponential, hence the cap. */
  function editNaive(a, b, cap) {
    cap = cap === undefined ? 8 : cap;
    oracleCap('editNaive', Math.max(a.length, b.length), cap);
    var c = counter();
    function f(i, j) {
      c.calls += 1;
      if (i === 0) return j;
      if (j === 0) return i;
      var same = a.charAt(i - 1) === b.charAt(j - 1);
      var best = f(i - 1, j - 1) + (same ? 0 : 1);
      var del = f(i - 1, j) + 1, ins = f(i, j - 1) + 1;
      if (del < best) best = del;
      if (ins < best) best = ins;
      return best;
    }
    return runOf({ distance: f(a.length, b.length) }, usedCounts(c), []);
  }

  /* ========================================================== matrix chain */
  function chainTable(dims, order) {
    var n = dims.length - 1;
    return dpFill({
      rows: n, cols: n, order: order || 'bylength',
      base: function (i, j) { return i === j ? 0 : (i > j ? 0 : undefined); },
      cell: function (i, j, get) {
        var best = null, at = null;
        for (var k = i; k < j; k += 1) {
          var left = get(i, k), right = get(k + 1, j);
          var v = left + right + dims[i] * dims[k + 1] * dims[j + 1];
          if (best === null || v < best) { best = v; at = [i, k]; }
        }
        return { v: best, from: at };
      }
    });
  }
  /* Every way of bracketing the product, by a recursion with no table at all.
     Catalan(n-1) of them: 42 at six matrices, 429 at eight, which is the cap. */
  function everyParenthesisation(dims, cap) {
    cap = cap === undefined ? 8 : cap;
    var n = dims.length - 1;
    oracleCap('everyParenthesisation', n, cap);
    var count = 0, best = null, bestTree = null;
    function walk(i, j) {
      if (i === j) return [{ leaf: i, cost: 0 }];
      var out = [];
      for (var k = i; k < j; k += 1) {
        var lefts = walk(i, k), rights = walk(k + 1, j);
        for (var p = 0; p < lefts.length; p += 1) {
          for (var q = 0; q < rights.length; q += 1) {
            out.push({ l: lefts[p], r: rights[q], split: k,
                       cost: lefts[p].cost + rights[q].cost + dims[i] * dims[k + 1] * dims[j + 1] });
          }
        }
      }
      return out;
    }
    var all = walk(0, n - 1), worst = null;
    all.forEach(function (t) {
      count += 1;
      if (best === null || t.cost < best) { best = t.cost; bestTree = t; }
      if (worst === null || t.cost > worst) worst = t.cost;
    });
    return { cost: best, worstCost: worst, count: count, tree: bestTree };
  }
  /* The reconstruction as a tree, and its cost re-derived from the dimensions
     alone -- so the table's number and the tree's cost are two computations
     rather than one number printed twice. */
  function chainSplitTree(filled, i, j) {
    if (i === j) return { leaf: i };
    var f = filled.result.from[i][j];
    var k = f ? f[1] : i;
    return { split: k, l: chainSplitTree(filled, i, k), r: chainSplitTree(filled, k + 1, j) };
  }
  function parenCost(tree, dims) {
    if (tree.leaf !== undefined) return { cost: 0, lo: tree.leaf, hi: tree.leaf };
    var L = parenCost(tree.l, dims), Rt = parenCost(tree.r, dims);
    return { cost: L.cost + Rt.cost + dims[L.lo] * dims[L.hi + 1] * dims[Rt.hi + 1],
             lo: L.lo, hi: Rt.hi };
  }
  function parenText(tree) {
    if (tree.leaf !== undefined) return 'A' + (tree.leaf + 1);
    return '(' + parenText(tree.l) + parenText(tree.r) + ')';
  }

  /* ==================================================================== lis */
  function lisTable(a) {
    var c = counter(), best = new Array(a.length).fill(1), prev = new Array(a.length).fill(-1);
    var i, j, top = 0, at = -1;
    for (i = 0; i < a.length; i += 1) {
      for (j = 0; j < i; j += 1) {
        c.compares += 1;
        if (a[j] < a[i] && best[j] + 1 > best[i]) { best[i] = best[j] + 1; prev[i] = j; }
      }
      if (best[i] > top) { top = best[i]; at = i; }
    }
    var out = [];
    while (at !== -1) { out.push(a[at]); at = prev[at]; }
    out.reverse();
    return runOf({ length: top, table: best, prev: prev, subsequence: out }, usedCounts(c), []);
  }
  function lisBrute(a, cap) {
    cap = cap === undefined ? 16 : cap;
    oracleCap('lisBrute', a.length, cap);
    var best = 0, bestSet = [], examined = 0;
    forEachSubset(a.length, function (mask) {
      examined += 1;
      var m = maskMembers(mask, a.length), ok = true;
      for (var i = 1; i < m.length; i += 1) if (a[m[i - 1]] >= a[m[i]]) { ok = false; break; }
      if (ok && m.length > best) { best = m.length; bestSet = m; }
    });
    return runOf({ length: best, subsequence: bestSet.map(function (i) { return a[i]; }) },
                 { nodes: examined }, []);
  }
  function isIncreasingRun(s) {
    for (var i = 1; i < s.length; i += 1) if (s[i - 1] >= s[i]) return false;
    return true;
  }
  function isSubsequenceOf(sub, a) {
    var i = 0;
    for (var k = 0; k < a.length && i < sub.length; k += 1) if (a[k] === sub[i]) i += 1;
    return i === sub.length;
  }

  /* ================================================================= coins

     The counting recursion, with no table, in BigInt. Combinations: coin
     types in a fixed order, so each multiset is reached once. Sequences: any
     coin at any step, so the orderings are counted separately. Both are the
     recurrences the DP loops implement, run without the loops. */
  function countBrute(coins, amount, order, cap) {
    /* Two caps, because the two recursions cost wildly different amounts. The
       combination recursion visits about one node per combination and there are
       hundreds of those; the sequence recursion visits one per SEQUENCE and
       there are 2 x 10^18 of them at an amount of 80. A single cap would
       either refuse a check that is free or accept one that freezes the tab. */
    if (cap === undefined) cap = order === 'permutations' ? 26 : 120;
    oracleCap('countBrute', amount, cap);
    var nodes = 0;
    function budget() {
      nodes += 1;
      if (nodes > 2000000) throw new Error('countBrute: more than 2 million recursive calls');
    }
    if (order === 'permutations') {
      var seq = function (left) {
        budget();
        if (left === 0) return 1n;
        var t = 0n;
        for (var i = 0; i < coins.length; i += 1) if (coins[i] <= left) t += seq(left - coins[i]);
        return t;
      };
      return seq(amount);
    }
    var comb = function (i, left) {
      budget();
      if (left === 0) return 1n;
      if (i >= coins.length) return 0n;
      var t = comb(i + 1, left);
      if (coins[i] <= left) t += comb(i, left - coins[i]);
      return t;
    };
    return comb(0, amount);
  }

  /* ================================================================== tree */
  function isIndependentSet(edges, set) {
    var inSet = {};
    set.forEach(function (v) { inSet[v] = true; });
    for (var i = 0; i < edges.length; i += 1) {
      if (inSet[edges[i][0]] && inSet[edges[i][1]]) return false;
    }
    return true;
  }
  function setWeight(w, set) {
    var t = 0;
    set.forEach(function (v) { t += w[v]; });
    return t;
  }
  /* The rooted tree as something TREEDRAW_JS can lay out: children are the
     neighbours other than the parent, and a node is wrapped so that vertex 0
     is not read as a missing child. */
  function rootedNodes(tree, root) {
    var seen = {};
    function build(v, parent) {
      seen[v] = true;
      var kids = (tree[v] || []).filter(function (u) { return u !== parent; })
                                .map(function (u) { return build(u, v); });
      return { v: v, kids: kids };
    }
    return build(root === undefined ? 0 : root, -1);
  }
  function rootedKids(nd) { return nd.kids; }

  /* ================================================================== game

     Win and lose with no table: a position is winning when some move reaches a
     losing one. Memo-free, so gameLabels' table is checked against a second
     computation rather than displayed and believed. */
  function gameBrute(moveSet, p, cap) {
    cap = cap === undefined ? 24 : cap;
    oracleCap('gameBrute', p, cap);
    function win(at) {
      for (var i = 0; i < moveSet.length; i += 1) {
        if (moveSet[i] <= at && !win(at - moveSet[i])) return true;
      }
      return false;
    }
    return win(p) ? 'W' : 'L';
  }

  /* =================================================================== tsp

     A NOTE ON WHAT heldKarp AND tspBrute RETURN, because it is not obvious
     and getting it wrong is how a tour gets re-measured one leg short. Both
     return the tour as an OPEN list of n cities beginning at 0 -- the leg back
     to 0 is counted in the length and is not in the list. So the checks below
     treat the list as a cycle: it must be a permutation of the cities starting
     at 0, and its length is the n - 1 legs plus the return. */
  function tourValid(tour, n) {
    if (!tour || tour.length !== n) return false;
    if (tour[0] !== 0) return false;
    var seen = {};
    for (var i = 0; i < n; i += 1) {
      if (tour[i] < 0 || tour[i] >= n || seen[tour[i]]) return false;
      seen[tour[i]] = true;
    }
    return true;
  }
  function tourLength(D, tour) {
    if (!tour || !tour.length) return 0;
    var t = 0;
    for (var i = 0; i + 1 < tour.length; i += 1) t += D[tour[i]][tour[i + 1]];
    return t + D[tour[tour.length - 1]][tour[0]];
  }

  /* ============================================================== drawings */
  function dpGridSvg(table, opts) {
    opts = opts || {};
    var rows = table.length, cols = rows ? table[0].length : 0;
    var w = opts.width === undefined ? 660 : opts.width;
    var left = opts.left === undefined ? 40 : opts.left;
    var top = opts.top === undefined ? 24 : opts.top;
    var cw = Math.max(13, Math.min(44, Math.floor((w - left - 10) / Math.max(1, cols))));
    var ch = opts.cellH === undefined ? 21 : opts.cellH;
    var shown = Math.min(cols, Math.floor((w - left - 10) / cw));
    var hi = {}, dep = {}, path = {};
    (opts.highlight || []).forEach(function (c) { hi[c[0] + ',' + c[1]] = true; });
    (opts.deps || []).forEach(function (c) { dep[c[0] + ',' + c[1]] = true; });
    (opts.path || []).forEach(function (c) { path[c[0] + ',' + c[1]] = true; });
    var s = '', i, j;
    for (j = 0; j < shown; j += 1) {
      s += '<text x="' + (left + j * cw + cw / 2).toFixed(1) + '" y="' + (top - 6)
        + '" text-anchor="middle" font-size="9" fill="var(--muted)">'
        + (opts.colLabel ? opts.colLabel(j) : j) + '</text>';
    }
    for (i = 0; i < rows; i += 1) {
      s += '<text x="' + (left - 6) + '" y="' + (top + i * ch + ch - 6)
        + '" text-anchor="end" font-size="9" fill="var(--muted)">'
        + (opts.rowLabel ? opts.rowLabel(i) : i) + '</text>';
      for (j = 0; j < shown; j += 1) {
        var key = i + ',' + j, v = table[i][j];
        var fill = hi[key] ? 'var(--cyan)' : (dep[key] ? 'var(--amber)'
                   : (path[key] ? 'var(--purple)' : 'var(--panel-3)'));
        var ink = (hi[key] || dep[key] || path[key]) ? 'var(--on-accent)' : 'var(--text)';
        var text = v === null ? '·' : (opts.cellText ? opts.cellText(v, i, j) : String(v));
        s += '<rect x="' + (left + j * cw) + '" y="' + (top + i * ch) + '" width="' + (cw - 2)
          + '" height="' + (ch - 2) + '" rx="2" fill="' + fill
          + '" stroke="var(--line-strong)" stroke-width="0.9" />'
          + '<text x="' + (left + j * cw + (cw - 2) / 2).toFixed(1) + '" y="'
          + (top + i * ch + ch - 8) + '" text-anchor="middle" font-size="9" fill="' + ink
          + '">' + text + '</text>';
      }
    }
    if (shown < cols) {
      s += '<text x="' + (left + shown * cw + 4) + '" y="' + (top + 12)
        + '" font-size="9" fill="var(--muted)">' + (cols - shown) + ' more columns</text>';
    }
    return s;
  }
  function drawDpGrid(el, table, opts) {
    var s = dpGridSvg(table, opts);
    if (el) el.innerHTML = s;
    return s;
  }
  function tourSvg(tour, n, opts) {
    opts = opts || {};
    var w = opts.width === undefined ? 300 : opts.width;
    var h = opts.height === undefined ? 200 : opts.height;
    var cx = w / 2, cy = h / 2, rad = Math.min(cx, cy) - 26, pts = [], i;
    for (i = 0; i < n; i += 1) {
      var ang = -Math.PI / 2 + (2 * Math.PI * i) / Math.max(1, n);
      pts.push({ x: cx + rad * Math.cos(ang), y: cy + rad * Math.sin(ang) });
    }
    var s = '';
    for (i = 0; tour && i + 1 < tour.length; i += 1) {
      var a = pts[tour[i]], b = pts[tour[i + 1]];
      if (!a || !b) continue;
      s += '<line x1="' + a.x.toFixed(1) + '" y1="' + a.y.toFixed(1) + '" x2="' + b.x.toFixed(1)
        + '" y2="' + b.y.toFixed(1) + '" stroke="var(--cyan)" stroke-width="2.4" />';
    }
    pts.forEach(function (p, v) {
      s += '<circle cx="' + p.x.toFixed(1) + '" cy="' + p.y.toFixed(1) + '" r="12" fill="'
        + (v === 0 ? 'var(--purple)' : 'var(--panel-3)')
        + '" stroke="var(--line-strong)" stroke-width="1.6" />'
        + '<text x="' + p.x.toFixed(1) + '" y="' + (p.y + 4).toFixed(1)
        + '" text-anchor="middle" font-size="11" font-weight="800" fill="'
        + (v === 0 ? 'var(--on-accent)' : 'var(--text)') + '">' + (v + 1) + '</text>';
    });
    return s;
  }
"""

_CORE_JS = (RATIONAL_JS + COUNT_JS + RFIXED_JS + BIGINT_JS + ORACLE_JS
            + TREEDRAW_JS + SERIES_JS + DP_JS + DPKIT_JS)


# ---------------------------------------------------------------------------
# Control furniture -- the shared shapes. Drawings take the two viewBox widths
# theme.py gives a horizontal-scroll minimum, 520 and 660.
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
    """A text box. No value here may contain `>`; see greedy.py's note."""
    if ">" in str(value):
        raise ValueError("dpkit: a control value may not contain '>': %r" % value)
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
    rows = []
    for p in presets:
        body = ", ".join("%s: %s" % (k, _js(p[k])) for k in keys)
        rows.append("    '%s': { %s }" % (p["id"], body))
    return "  var %s = {\n%s\n  };\n" % (name, ",\n".join(rows))


def _options(presets):
    return [(p["id"], p["label"]) for p in presets]


def _expect(presets):
    """{preset id: {kpi element id: the exact text the page prints}}.

    A preset's `label` is prose about an instance and no check in this
    repository can read it. This is the other half of the same claim, and it is
    the half a machine can hold: what the page PRINTS once the preset is
    selected. scripts/labcheck.js selects the option on the BUILT page,
    dispatches the menu's own change handler and compares
    getElementById(kpi).textContent with the string here. Every figure below
    was read off the running kit with `node scripts/labcheck.js --observe
    <page>`, never copied out of the code that computes it.

    Tiles are read with every OTHER control at the value the markup ships, so a
    claim that only becomes visible once another control moves cannot be pinned
    here; those are named in a comment beside the preset that makes them.
    """
    return {p["id"]: dict(p.get("expect") or {}) for p in presets}


def _chosen(presets, cfg):
    want = str(cfg.get("preset", presets[0]["id"]))
    for p in presets:
        if p["id"] == want:
            return p
    raise ValueError(
        "dpkit: no preset %r; this mode has %s"
        % (want, ", ".join(p["id"] for p in presets))
    )


# The sentence every mode carries in some form.
_TWO_ROUTES = (
    "  /* A filled table is the easiest thing in this course to get confidently\n"
    "     wrong: a recurrence that reads one cell too early still finishes, and\n"
    "     the result looks exactly like an answer. So no number below is read\n"
    "     off the table alone. Every one of them is computed a second time by a\n"
    "     route that has no table -- an exhaustive search, a memo-free\n"
    "     recursion, or a re-costing of the answer that came back -- and where\n"
    "     the two disagree the panel prints both. */\n"
)


# ---------------------------------------------------------------------------
# memo -- one recursion, three ways
# ---------------------------------------------------------------------------

_MM_PRESETS = [
    {
        "id": "canonical",
        "label": "coins 1, 2, 5 and an amount of 18",
        "coins": "1 2 5",
        "amount": "18",
        "expect": {
            "mmNaive": "22089",
            "mmMemo": "50",
            "mmSaved": "22089/50 = 441.8 times fewer",
        },
    },
    {
        "id": "awkward",
        "label": "coins 1, 3, 4 — where taking the largest first is wrong",
        "coins": "1 3 4",
        "amount": "6",
        # The instance is here because the largest coin first gives 4 + 1 + 1, and the
        # recurrence finds 3 + 3. Only the second of those is on the page: no tile runs
        # a greedy rule, so what is pinned is the answer the three routes agree on.
        "expect": {
            "mmBest": "2",
        },
    },
    {
        "id": "sparse",
        "label": "coins 4, 7 and an amount of 17",
        "coins": "4 7",
        "amount": "17",
        # Nine amounts below 17 cannot be made from 4 and 7 and 17 is the largest of
        # them, which is the row of dots in the table rather than a tile; the amount
        # this preset ships is the largest one, and that one IS a tile.
        "expect": {
            "mmBest": "cannot be made",
        },
    },
    {
        "id": "wide",
        "label": "five coin types, amount 20",
        "coins": "1 2 5 10 20",
        "amount": "20",
        "expect": {
            "mmNaive": "66282",
            "mmCells": "126",
        },
    },
]


def _memo(cfg):
    chosen = _chosen(_MM_PRESETS, cfg)
    markup = (
        _toolbar(
            "The same recurrence, three times",
            "no memo, a memo, and a table — one answer, three costs",
            [("cyan", "the cell being computed"), ("amber", "the cells it read"),
             ("purple", "the coins the answer uses")],
        )
        + _stage(_svg("mmGrid", "0 0 660 180",
                      "The table, one row per coin type and one column per amount.")
                 + _svg("mmPlot", "0 0 520 220",
                        "Calls made by the plain recursion and by the memoised one, against "
                        "the amount."))
        + _table("mmRoutes")
        + _banner("mmStatus")
    )
    controls = (
        _select("mmPreset", "Coins and amount", _options(_MM_PRESETS), chosen["id"])
        + _text("mmCoins", "Coin denominations", chosen["coins"])
        + _text("mmAmount", "Amount to make", chosen["amount"])
        + _range("mmCell", "Explain the cell at column", 0, 26, 0)
        + _kpis([("Fewest coins", "mmBest"), ("Calls, no memo", "mmNaive"),
                 ("Calls, with a memo", "mmMemo"),
                 ("Calls saved, as a fraction", "mmSaved"),
                 ("Cells the table fills", "mmCells"),
                 ("All three agree", "mmAgree")])
        + _hint(
            "mmHint",
            "The recurrence is the whole lesson: <em>the fewest coins for n is one more than "
            "the fewest for n minus some coin</em>. Run it as written and the same subproblem "
            "is solved thousands of times. Write each answer down the first time and it is "
            "solved once. Fill the answers bottom-up and there is no recursion at all. The "
            "three costs are wildly different and the three answers are the same number.",
        )
    )
    script = _CORE_JS + _TWO_ROUTES + _presets_js(
        "MMP", _MM_PRESETS, ["coins", "amount"]) + r"""
  var presetIn = document.getElementById('mmPreset'), coinsIn = document.getElementById('mmCoins');
  var amtIn = document.getElementById('mmAmount');
  var cellIn = document.getElementById('mmCell'), cellOut = document.getElementById('mmCellOut');
  var grid = document.getElementById('mmGrid'), plot = document.getElementById('mmPlot');
  var routesT = document.getElementById('mmRoutes'), status = document.getElementById('mmStatus');
  var KPIS = ['mmBest', 'mmNaive', 'mmMemo', 'mmSaved', 'mmCells', 'mmAgree'];

  function blank(why) {
    grid.innerHTML = ''; plot.innerHTML = ''; routesT.innerHTML = '';
    for (var i = 0; i < KPIS.length; i += 1) document.getElementById(KPIS[i]).textContent = '—';
    status.innerHTML = '<span class="tone-red">' + why + '.</span>';
  }

  function redraw() {
    var cr = dpParseNums(coinsIn.value, 6, 1, 50);
    if (cr.bad) { blank('the coins: ' + cr.bad); return; }
    var coins = cr.values.slice().sort(function (a, b) { return a - b; });
    var amount = parseInt(amtIn.value, 10);
    if (!isFinite(amount) || amount < 0 || amount > 26) {
      blank('the amount is a whole number between 0 and 26'); return;
    }

    var table = minCoinTable(coins, amount);
    var memo = memoMinCoins(coins, amount);
    var naive = null, why = '';
    try { naive = naiveMinCoins(coins, amount); } catch (err) { why = String(err.message); }
    var tableAnswer = table.result.table[coins.length][amount];
    var best = dpUnreachable(tableAnswer) ? null : tableAnswer;
    var picks = best === null ? [] : minCoinPicks(table, coins, amount);
    var agree = memo.result.coins === best
      && (naive === null || naive.result.coins === best);

    cellIn.max = amount;
    var col = Math.max(0, Math.min(amount, parseInt(cellIn.value, 10)));
    cellOut.textContent = String(col);
    var row = coins.length;
    var deps = table.result.deps[row][col] || [];

    document.getElementById('mmBest').textContent = best === null ? 'cannot be made' : String(best);
    document.getElementById('mmNaive').textContent = naive ? String(naive.counts.calls) : 'refused';
    document.getElementById('mmMemo').textContent = String(memo.counts.calls);
    var saved = naive
      ? R(BigInt(naive.counts.calls), BigInt(Math.max(1, memo.counts.calls))) : null;
    document.getElementById('mmSaved').textContent = saved
      ? Rtext(saved) + ' = ' + Rfixed(saved, 1) + ' times fewer' : '—';
    document.getElementById('mmCells').textContent = String(table.counts.cells);
    document.getElementById('mmAgree').textContent = agree ? 'yes' : 'NO';

    grid.innerHTML = dpGridSvg(table.result.table, {
      highlight: [[row, col]], deps: deps,
      rowLabel: function (i) { return i === 0 ? 'none' : String(coins[i - 1]); },
      cellText: function (v) { return dpUnreachable(v) ? '·' : String(v); }
    });

    /* The curve stops at 16 whatever the amount is. It is redrawn on every
       keystroke and the unmemoised arm is re-run at every x, so plotting to 26
       is a few million calls per redraw for a picture that already makes its
       point. The KPI above is the full amount; this is the shape. */
    var xs = [], naiveCalls = [], memoCalls = [], curve = [];
    var top = Math.min(amount, 16);
    for (var n = 1; n <= top; n += 1) {
      xs.push(n);
      memoCalls.push(memoMinCoins(coins, n).counts.calls);
      var run = null;
      try { run = naiveMinCoins(coins, n); } catch (e2) { run = null; }
      naiveCalls.push(run ? run.counts.calls : NaN);
      curve.push(Math.pow(2, n / 2));
    }
    plot.innerHTML = xs.length > 1 ? seriesSvg([
      { label: 'no memo', values: naiveCalls, colour: 'var(--red)', points: true },
      { label: 'with a memo', values: memoCalls, colour: 'var(--cyan)', points: true },
      { label: '2^(n/2)', values: curve, colour: 'var(--muted)', dashed: true }
    ], xs, { xlabel: 'amount', log: true, box: { left: 26, right: 470, base: 190, top: 14 } }) : '';

    var rows = '';
    rows += '<tr><th class="rowhead">recursion, no memo</th><td>'
      + (naive ? (naive.result.coins === null ? 'cannot be made' : naive.result.coins) : '—')
      + '</td><td>' + (naive ? naive.counts.calls + ' calls' : 'refused: ' + why) + '</td></tr>';
    rows += '<tr><th class="rowhead">recursion, with a memo</th><td>'
      + (memo.result.coins === null ? 'cannot be made' : memo.result.coins) + '</td><td>'
      + memo.counts.calls + ' calls, ' + memo.result.distinct + ' distinct subproblems</td></tr>';
    rows += '<tr class="tone-cyan"><th class="rowhead">the table, bottom-up</th><td>'
      + (best === null ? 'cannot be made' : best) + '</td><td>' + table.counts.cells
      + ' cells, ' + table.counts.reads + ' reads, no recursion at all</td></tr>';
    if (picks.length) {
      rows += '<tr class="tone-purple"><th class="rowhead">the coins it uses</th><td>'
        + picks.join(' + ') + ' = '
        + picks.reduce(function (t, x) { return t + x; }, 0) + '</td><td>'
        + (picks.length === best && picks.reduce(function (t, x) { return t + x; }, 0) === amount
            ? 'that is ' + picks.length + ' coins adding to ' + amount + ', re-added here'
            : '<span class="tone-red">the reconstruction does not add up</span>') + '</td></tr>';
    }
    routesT.innerHTML = '<thead><tr><th>route</th><th>answer</th><th>what it cost</th>'
      + '</tr></thead><tbody>' + rows + '</tbody>';

    status.innerHTML = 'Making ' + amount + ' from {' + coins.join(', ') + '} needs <strong>'
      + (best === null ? 'no number of these coins' : best + ' coin' + (best === 1 ? '' : 's'))
      + '</strong>. ' + (naive
          ? 'The plain recursion reached that in <strong>' + naive.counts.calls
            + '</strong> calls; with a memo it took <strong>' + memo.counts.calls
            + '</strong>, which is ' + Rtext(saved) + ' times fewer, and the memo holds only '
            + memo.result.distinct + ' distinct subproblems — that number is the whole reason '
            + 'a memo works, and it is small because the recursion keeps asking the same '
            + 'questions.'
          : '<span class="tone-amber">The unmemoised run was refused: ' + why + '.</span>')
      + ' The table fills ' + table.counts.cells + ' cells in a fixed order and recurses not at '
      + 'all. ' + (agree
          ? 'All three agree on the answer, which is what makes the cost comparison worth '
            + 'anything.'
          : '<span class="tone-red">The three do not agree</span>, so one of them is wrong and '
            + 'the page says so rather than showing the prettiest.')
      + ' The highlighted cell read ' + deps.length + ' other cell'
      + (deps.length === 1 ? '' : 's') + ', painted amber — that list was recorded by the '
      + 'recurrence\'s own reads, not written down beside it.';
  }

  presetIn.addEventListener('change', function () {
    var p = MMP[presetIn.value];
    if (p) { coinsIn.value = p.coins; amtIn.value = p.amount; }
    redraw();
  });
  [coinsIn, amtIn, cellIn].forEach(function (el) {
    el.addEventListener('input', redraw);
    el.addEventListener('change', redraw);
  });
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="One recurrence, three costs, one answer",
        subtitle="The same definition run without a memo, with one, and as a table",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Choose the coins and the amount"),
        panel_intro=cfg.get(
            "panel_intro",
            "The three routes are three pieces of code, not three descriptions. If they ever "
            "disagree the panel says so; the only thing the comparison of their costs is worth "
            "anything for is that they do not.",
        ),
        script=script,
        expect={"mmPreset": _expect(_MM_PRESETS)},
    )


# ---------------------------------------------------------------------------
# knapsack -- the grid, the dependencies, the reconstruction re-weighed
# ---------------------------------------------------------------------------

_KN_PRESETS = [
    {
        "id": "small",
        "label": "four items, capacity 7",
        "spec": "1/1, 3/4, 4/5, 5/7",
        "cap": "7",
        "expect": {
            "knValue": "9",
            "knBrute": "9",
            "knCheck": "7 of 7, worth 9",
        },
    },
    {
        "id": "ties",
        "label": "two items of equal value",
        "spec": "2/3, 2/3, 3/4",
        "cap": "4",
        "expect": {
            "knValue": "6",
            "knCheck": "4 of 4, worth 6",
        },
    },
    {
        "id": "wasteful",
        "label": "capacity that cannot be filled",
        "spec": "4/5, 4/5, 4/5",
        "cap": "9",
        "expect": {
            "knValue": "10",
            "knCheck": "8 of 9, worth 10",
        },
    },
    {
        "id": "unbounded",
        "label": "three items, capacity 11, worth comparing one-row",
        "spec": "2/3, 3/5, 5/9",
        "cap": "11",
        "expect": {
            "knValue": "17",
            "knBack": "17",
            "knFwd": "19",
        },
    },
]


def _knapsack(cfg):
    chosen = _chosen(_KN_PRESETS, cfg)
    markup = (
        _toolbar(
            "The grid, and what each cell actually read",
            "the reconstruction is re-weighed against the capacity it claims to fit",
            [("cyan", "the cell being explained"), ("amber", "the cells it read"),
             ("purple", "the path the reconstruction walked")],
        )
        + _stage(_svg("knGrid", "0 0 660 220",
                      "The table, one row per item and one column per capacity.")
                 + _svg("knOneRow", "0 0 660 80",
                        "The same problem in one row, filled forward and backward."))
        + _table("knPath")
        + _banner("knStatus")
    )
    controls = (
        _select("knPreset", "Instance", _options(_KN_PRESETS), chosen["id"])
        + _text("knSpec", "Items, written weight/value", chosen["spec"])
        + _text("knCap", "Capacity", chosen["cap"])
        + _range("knRow", "Explain the cell in row", 0, 8, 2)
        + _range("knCol", "and column", 0, 24, 5)
        + _kpis([("The table's answer", "knValue"), ("Every subset says", "knBrute"),
                 ("Reconstruction re-weighed", "knCheck"),
                 ("Cells filled", "knCells"),
                 ("One row, filled backward", "knBack"),
                 ("One row, filled forward", "knFwd")])
        + _hint(
            "knHint",
            "An item is <span class=\"tt\">3/4</span>: weight 3, value 4. Each cell asks one "
            "question &mdash; is this item worth taking at this capacity? &mdash; and answers "
            "it from two cells in the row above. The cells it read are painted amber, and that "
            "list was recorded as the recurrence read them. The second drawing is the same "
            "problem in a single row: filled backward it is still 0/1, filled forward each "
            "item can be taken any number of times, and that one loop direction is the whole "
            "difference.",
        )
    )
    script = _CORE_JS + _TWO_ROUTES + _presets_js(
        "KNP", _KN_PRESETS, ["spec", "cap"]) + r"""
  var presetIn = document.getElementById('knPreset'), specIn = document.getElementById('knSpec');
  var capIn = document.getElementById('knCap');
  var rowIn = document.getElementById('knRow'), rowOut = document.getElementById('knRowOut');
  var colIn = document.getElementById('knCol'), colOut = document.getElementById('knColOut');
  var grid = document.getElementById('knGrid'), rowPlot = document.getElementById('knOneRow');
  var pathT = document.getElementById('knPath'), status = document.getElementById('knStatus');
  var KPIS = ['knValue', 'knBrute', 'knCheck', 'knCells', 'knBack', 'knFwd'];

  function blank(why) {
    grid.innerHTML = ''; rowPlot.innerHTML = ''; pathT.innerHTML = '';
    for (var i = 0; i < KPIS.length; i += 1) document.getElementById(KPIS[i]).textContent = '—';
    status.innerHTML = '<span class="tone-red">' + why + '.</span> An item is '
      + '<span class="tt">3/4</span>: weight, then value.';
  }

  function redraw() {
    var parsed = dpParseItems(specIn.value);
    if (parsed.bad) { blank(parsed.bad); return; }
    var items = parsed.items;
    var W = parseInt(capIn.value, 10);
    if (!isFinite(W) || W < 1 || W > 24) { blank('the capacity is between 1 and 24'); return; }

    var filled = knapTable(items, W);
    var value = filled.result.table[items.length][W];
    var brute = knapsackBrute(items, W);
    var rec = reconstructPicks(filled, items, W);
    var check = packCheck(items, rec.picks, W, value);
    var back = oneRow(items, W, 'backward'), fwd = oneRow(items, W, 'forward');

    rowIn.max = items.length; colIn.max = W;
    var r = Math.max(0, Math.min(items.length, parseInt(rowIn.value, 10)));
    var c = Math.max(0, Math.min(W, parseInt(colIn.value, 10)));
    rowOut.textContent = r === 0 ? 'no items' : ('first ' + r);
    colOut.textContent = String(c);
    var deps = filled.result.deps[r][c] || [];

    document.getElementById('knValue').textContent = String(value);
    document.getElementById('knBrute').textContent = String(brute.result.value);
    document.getElementById('knCheck').textContent = check.ok
      ? (check.weight + ' of ' + W + ', worth ' + check.value) : 'DOES NOT MATCH';
    document.getElementById('knCells').textContent = String(filled.counts.cells);
    document.getElementById('knBack').textContent = String(back.result.value);
    document.getElementById('knFwd').textContent = String(fwd.result.value);

    grid.innerHTML = dpGridSvg(filled.result.table, {
      highlight: [[r, c]], deps: deps, path: rec.path,
      rowLabel: function (i) { return i === 0 ? '—' : items[i - 1].label; }
    });
    rowPlot.innerHTML = dpGridSvg([back.result.row, fwd.result.row], {
      cellH: 22, rowLabel: function (i) { return i === 0 ? 'back' : 'fwd'; }
    });

    var rows = '';
    rec.path.forEach(function (cell, i) {
      if (i + 1 >= rec.path.length) return;
      var next = rec.path[i + 1], took = cell[0] - next[0] === 1 && cell[1] !== next[1];
      rows += '<tr class="' + (took ? 'tone-cyan' : '') + '"><th class="rowhead">('
        + cell[0] + ', ' + cell[1] + ')</th><td>'
        + (cell[0] === 0 ? '—' : items[cell[0] - 1].label) + '</td><td>'
        + (took ? 'taken' : 'skipped') + '</td><td>(' + next[0] + ', ' + next[1] + ')</td></tr>';
    });
    rows += '<tr class="tone-amber"><th class="rowhead">re-weighed</th><td>'
      + rec.picks.map(function (i) { return items[i].label; }).join(' ') + '</td><td>weight '
      + check.weight + ' of ' + W + '</td><td>value ' + check.value
      + (check.matches ? '' : ' <span class="tone-red">≠ ' + value + '</span>') + '</td></tr>';
    rows += '<tr><th class="rowhead">every subset</th><td>'
      + brute.result.members.map(function (i) { return items[i].label; }).join(' ')
      + '</td><td>' + brute.counts.nodes + ' tried</td><td>value ' + brute.result.value
      + '</td></tr>';
    pathT.innerHTML = '<thead><tr><th>cell</th><th>item</th><th>decision</th><th>goes to</th>'
      + '</tr></thead><tbody>' + rows + '</tbody>';

    status.innerHTML = 'The table says <strong>' + value + '</strong> and the best of all '
      + brute.counts.nodes + ' subsets says <strong>' + brute.result.value + '</strong>'
      + (value === brute.result.value
          ? ' — two routes, one number.'
          : ' <span class="tone-red">— and they disagree, so the recurrence is wrong.</span>')
      + ' The reconstruction walked ' + (rec.path.length - 1) + ' steps back through the table '
      + 'and returned ' + (rec.picks.length ? rec.picks.map(function (i) {
            return items[i].label; }).join(', ') : 'nothing') + ', which weighs '
      + check.weight + ' against a capacity of ' + W + ' and is worth ' + check.value + ' — '
      + (check.ok
          ? 'both re-derived from the items rather than carried along, which is the only way a '
            + 'reconstruction can be shown to be the answer it claims.'
          : '<span class="tone-red">and that does not match the table.</span>')
      + ' The cell at (' + r + ', ' + c + ') read ' + deps.length + ' cell'
      + (deps.length === 1 ? '' : 's') + '. In one row, filling backward gives ' + back.result.value
      + ' and filling forward gives ' + fwd.result.value + ' — '
      + (fwd.result.value >= back.result.value
          ? 'forward reuses each item within its own row, so it solves the UNBOUNDED problem, '
            + 'and the difference between the two numbers is one loop running the other way.'
          : 'which should not happen: forward can only do better.');
  }

  presetIn.addEventListener('change', function () {
    var p = KNP[presetIn.value];
    if (p) { specIn.value = p.spec; capIn.value = p.cap; }
    redraw();
  });
  [specIn, capIn, rowIn, colIn].forEach(function (el) {
    el.addEventListener('input', redraw);
    el.addEventListener('change', redraw);
  });
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="The grid, what each cell read, and the answer re-weighed",
        subtitle="0/1 against every subset, and the one loop direction that makes it unbounded",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Choose the items and the capacity"),
        panel_intro=cfg.get(
            "panel_intro",
            "The amber cells are the ones the recurrence actually read while computing the "
            "highlighted cell &mdash; recorded by its own reads, so the picture cannot "
            "disagree with the code. The reconstruction is re-weighed and re-valued from the "
            "items.",
        ),
        script=script,
        expect={"knPreset": _expect(_KN_PRESETS)},
    )


# ---------------------------------------------------------------------------
# edit -- the table, the script, and the script performed
# ---------------------------------------------------------------------------

_ED_PRESETS = [
    {
        "id": "kitten",
        "label": "kitten to sitting",
        "a": "kitten", "b": "sitting",
        "expect": {
            "edDist": "3",
            "edApply": "sitting",
        },
    },
    {
        "id": "sunday",
        "label": "sunday to saturday",
        "a": "sunday", "b": "saturday",
        "expect": {
            "edDist": "3",
            "edApply": "saturday",
        },
    },
    {
        "id": "prefix",
        "label": "one word is a prefix of the other",
        "a": "dog", "b": "dogma",
        # That every one of the operations is an insertion is in the script table, one
        # row per operation, and not in any tile; the count of them and the word they
        # build are.
        "expect": {
            "edDist": "2",
            "edOps": "2",
            "edApply": "dogma",
        },
    },
    {
        "id": "disjoint",
        "label": "nothing in common",
        "a": "abc", "b": "xyz",
        "expect": {
            "edDist": "3",
            "edApply": "xyz",
        },
    },
]


def _edit(cfg):
    chosen = _chosen(_ED_PRESETS, cfg)
    markup = (
        _toolbar(
            "The table, the script, and the script carried out",
            "every operation names the character it acts on, and is performed on it",
            [("cyan", "the cell being explained"), ("amber", "the cells it read"),
             ("purple", "the alignment the script walked")],
        )
        + _stage(_svg("edGrid", "0 0 660 260",
                      "The edit-distance table, one row per character of the first word and "
                      "one column per character of the second."))
        + _table("edScript")
        + _banner("edStatus")
    )
    controls = (
        _select("edPreset", "Pair of words", _options(_ED_PRESETS), chosen["id"])
        + _text("edA", "First word", chosen["a"])
        + _text("edB", "Second word", chosen["b"])
        + _range("edRow", "Explain the cell in row", 0, 10, 3)
        + _range("edCol", "and column", 0, 10, 3)
        + _kpis([("Edit distance", "edDist"), ("Memo-free recursion says", "edNaive"),
                 ("Operations in the script", "edOps"),
                 ("The script performed gives", "edApply"),
                 ("Cells filled", "edCells"),
                 ("Calls the recursion made", "edCalls")])
        + _hint(
            "edHint",
            "Each cell is the cost of turning the first <em>i</em> characters into the first "
            "<em>j</em>, and it reads exactly three cells: the one above (delete), the one to "
            "the left (insert), and the one diagonally back (keep or substitute). The script "
            "under the table is then <em>performed</em> on the first word, character by "
            "character, and refuses if an operation names a character that is not there.",
        )
    )
    script = _CORE_JS + _TWO_ROUTES + _presets_js(
        "EDP", _ED_PRESETS, ["a", "b"]) + r"""
  var presetIn = document.getElementById('edPreset');
  var aIn = document.getElementById('edA'), bIn = document.getElementById('edB');
  var rowIn = document.getElementById('edRow'), rowOut = document.getElementById('edRowOut');
  var colIn = document.getElementById('edCol'), colOut = document.getElementById('edColOut');
  var grid = document.getElementById('edGrid');
  var scriptT = document.getElementById('edScript'), status = document.getElementById('edStatus');
  var KPIS = ['edDist', 'edNaive', 'edOps', 'edApply', 'edCells', 'edCalls'];

  function blank(why) {
    grid.innerHTML = ''; scriptT.innerHTML = '';
    for (var i = 0; i < KPIS.length; i += 1) document.getElementById(KPIS[i]).textContent = '—';
    status.innerHTML = '<span class="tone-red">' + why + '.</span>';
  }

  function redraw() {
    var pa = dpParseWord(aIn.value), pb = dpParseWord(bIn.value);
    if (pa.bad) { blank('the first word: ' + pa.bad); return; }
    if (pb.bad) { blank('the second word: ' + pb.bad); return; }
    var a = pa.word, b = pb.word;

    var filled = editTable(a, b);
    var dist = filled.result.table[a.length][b.length];
    var script = editScript(filled, a, b);
    var made = applyScript(a, script);
    var naive = null, why = '';
    try { naive = editNaive(a, b); } catch (err) { why = String(err.message); }

    rowIn.max = a.length; colIn.max = b.length;
    var r = Math.max(0, Math.min(a.length, parseInt(rowIn.value, 10)));
    var c = Math.max(0, Math.min(b.length, parseInt(colIn.value, 10)));
    rowOut.textContent = r === 0 ? 'empty' : a.slice(0, r);
    colOut.textContent = c === 0 ? 'empty' : b.slice(0, c);
    var deps = filled.result.deps[r][c] || [];
    var path = reconstruct(filled.result, [a.length, b.length]);

    document.getElementById('edDist').textContent = String(dist);
    document.getElementById('edNaive').textContent = naive ? String(naive.result.distance) : 'refused';
    document.getElementById('edOps').textContent = String(editCost(script));
    document.getElementById('edApply').textContent = made === null ? 'REFUSED' : made;
    document.getElementById('edCells').textContent = String(filled.counts.cells);
    document.getElementById('edCalls').textContent = naive ? String(naive.counts.calls) : '—';

    grid.innerHTML = dpGridSvg(filled.result.table, {
      highlight: [[r, c]], deps: deps, path: path, cellH: 22,
      rowLabel: function (i) { return i === 0 ? '—' : a.charAt(i - 1); },
      colLabel: function (j) { return j === 0 ? '—' : b.charAt(j - 1); }
    });

    var rows = '', so = '';
    script.forEach(function (op, i) {
      if (op.op === 'keep') so += op.ch;
      else if (op.op === 'substitute') so += op.to;
      else if (op.op === 'insert') so += op.ch;
      rows += '<tr class="' + (op.op === 'keep' ? '' : 'tone-cyan') + '">'
        + '<th class="rowhead">' + (i + 1) + '</th><td>' + op.op + '</td><td>'
        + (op.op === 'substitute' ? op.from + ' by ' + op.to : op.ch) + '</td><td class="tt">'
        + so + '</td></tr>';
    });
    rows += '<tr class="' + (made === b ? 'tone-amber' : 'tone-red') + '">'
      + '<th class="rowhead">result</th><td>the script performed</td><td class="tt">'
      + (made === null ? 'refused' : made) + '</td><td>'
      + (made === b ? 'which is the second word' : 'which is NOT the second word') + '</td></tr>';
    scriptT.innerHTML = '<thead><tr><th>step</th><th>operation</th><th>on</th>'
      + '<th>the word so far</th></tr></thead><tbody>' + rows + '</tbody>';

    status.innerHTML = 'Turning <span class="tt">' + (a || 'the empty word') + '</span> into '
      + '<span class="tt">' + (b || 'the empty word') + '</span> costs <strong>' + dist
      + '</strong> operations. ' + (naive
          ? 'A recursion with no table at all, which made ' + naive.counts.calls
            + ' calls against the table\'s ' + filled.counts.cells + ' cells, gets '
            + naive.result.distance + ' — '
            + (naive.result.distance === dist
                ? 'the same number by a route with no memory in it.'
                : '<span class="tone-red">a different number, so one of them is wrong.</span>')
          : '<span class="tone-amber">The recursion was refused: ' + why + '.</span>')
      + ' The script has ' + editCost(script) + ' non-trivial operation'
      + (editCost(script) === 1 ? '' : 's') + ', and performing it on the first word '
      + (made === null
          ? '<span class="tone-red">failed: an operation named a character that was not '
            + 'there</span>, which is exactly the defect a length check would have missed'
          : (made === b
              ? 'gives <span class="tt">' + made + '</span> — the second word, so the script is '
                + 'the answer and not merely the right length'
              : 'gives <span class="tone-red">' + made + '</span>, which is not the second word'))
      + '.';
  }

  presetIn.addEventListener('change', function () {
    var p = EDP[presetIn.value];
    if (p) { aIn.value = p.a; bIn.value = p.b; }
    redraw();
  });
  [aIn, bIn, rowIn, colIn].forEach(function (el) {
    el.addEventListener('input', redraw);
    el.addEventListener('change', redraw);
  });
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="A distance, and the edit script that realises it",
        subtitle="The table checked against a recursion, and the script checked by performing it",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Choose the two words"),
        panel_intro=cfg.get(
            "panel_intro",
            "A number alone would not show that the alignment is right. The script is carried "
            "out on the first word, one operation at a time, refusing whenever an operation "
            "names a character that is not where it says it is.",
        ),
        script=script,
        expect={"edPreset": _expect(_ED_PRESETS)},
    )


# ---------------------------------------------------------------------------
# chain -- the fill order, and every parenthesisation
# ---------------------------------------------------------------------------

_CH_PRESETS = [
    {
        "id": "clrs",
        "label": "six matrices, the usual worked example",
        "dims": "30 35 15 5 10 20 25",
        # Tiles are read with chOrder at the value the markup ships, by interval length.
        # Row-major on this instance prints 9000 for the same table, which is the mode's
        # point and cannot be pinned from here because it needs the other menu moved.
        "expect": {
            "chValue": "15125",
            "chBrute": "15125",
            "chCount": "42",
        },
    },
    {
        "id": "thin",
        "label": "a thin matrix in the middle",
        "dims": "10 100 5 50",
        "expect": {
            "chValue": "7500",
            "chWorst": "75000",
        },
    },
    {
        "id": "square",
        "label": "all the same size",
        "dims": "10 10 10 10 10",
        "expect": {
            "chValue": "3000",
            "chWorst": "3000",
        },
    },
    {
        "id": "long",
        "label": "seven matrices",
        "dims": "5 10 3 12 5 50 6 4",
        # Row-major fill prints 200 here against the table's 2052 -- the widest the two
        # orders come apart in the kit -- and that number needs chOrder moved, so it is
        # recorded here rather than pinned.
        "expect": {
            "chValue": "2052",
            "chCount": "132",
        },
    },
]


def _chain(cfg):
    chosen = _chosen(_CH_PRESETS, cfg)
    markup = (
        _toolbar(
            "Fill by length, or fill by row and be wrong",
            "the same recurrence, two orders, two answers, one of them checked",
            [("cyan", "the cell being explained"), ("amber", "the cells it read"),
             ("red", "a cell that was read before it was filled")],
        )
        + _stage(_svg("chGrid", "0 0 660 200",
                      "The table filled in the chosen order, one row and column per matrix.")
                 + _svg("chWrong", "0 0 660 200",
                        "The same table filled row by row, for comparison."))
        + _table("chOrders")
        + _banner("chStatus")
    )
    controls = (
        _select("chPreset", "Dimensions", _options(_CH_PRESETS), chosen["id"])
        + _text("chDims", "Dimensions: n+1 numbers for n matrices", chosen["dims"])
        + _select("chOrder", "Fill the table",
                  [("bylength", "by interval length, shortest first"),
                   ("rowmajor", "row by row, left to right")], "bylength")
        + _range("chRow", "Explain the cell in row", 0, 8, 0)
        + _range("chCol", "and column", 0, 8, 3)
        + _kpis([("This order's answer", "chValue"),
                 ("Every bracketing says", "chBrute"),
                 ("Bracketings tried", "chCount"),
                 ("The bracketing itself", "chParen"),
                 ("Re-costed from the dimensions", "chRecost"),
                 ("The worst bracketing costs", "chWorst")])
        + _hint(
            "chHint",
            "Seven numbers describe six matrices: <span class=\"tt\">30 35 15 5 10 20 25</span> "
            "is 30&times;35, then 35&times;15, and so on. A cell covers an interval of the "
            "chain and reads two shorter intervals, so the shorter ones have to be filled "
            "first. Fill row by row instead and some of them are not &mdash; the table still "
            "finishes, and the number it finishes with is wrong.",
        )
    )
    script = _CORE_JS + _TWO_ROUTES + _presets_js(
        "CHP", _CH_PRESETS, ["dims"]) + r"""
  var presetIn = document.getElementById('chPreset'), dimsIn = document.getElementById('chDims');
  var orderIn = document.getElementById('chOrder');
  var rowIn = document.getElementById('chRow'), rowOut = document.getElementById('chRowOut');
  var colIn = document.getElementById('chCol'), colOut = document.getElementById('chColOut');
  var grid = document.getElementById('chGrid'), wrongGrid = document.getElementById('chWrong');
  var ordersT = document.getElementById('chOrders'), status = document.getElementById('chStatus');
  var KPIS = ['chValue', 'chBrute', 'chCount', 'chParen', 'chRecost', 'chWorst'];

  function blank(why) {
    grid.innerHTML = ''; wrongGrid.innerHTML = ''; ordersT.innerHTML = '';
    for (var i = 0; i < KPIS.length; i += 1) document.getElementById(KPIS[i]).textContent = '—';
    status.innerHTML = '<span class="tone-red">' + why + '.</span>';
  }

  function redraw() {
    var dr = dpParseNums(dimsIn.value, 9, 1, 500);
    if (dr.bad) { blank('the dimensions: ' + dr.bad); return; }
    var dims = dr.values;
    if (dims.length < 3) { blank('at least three numbers, which is two matrices'); return; }
    var n = dims.length - 1;

    var good = chainTable(dims, 'bylength'), bad = chainTable(dims, 'rowmajor');
    var here = orderIn.value === 'rowmajor' ? bad : good;
    var value = here.result.table[0][n - 1];
    var every = null, why = '';
    try { every = everyParenthesisation(dims); } catch (err) { why = String(err.message); }
    var tree = chainSplitTree(good, 0, n - 1);
    var recost = parenCost(tree, dims);

    rowIn.max = n - 1; colIn.max = n - 1;
    var r = Math.max(0, Math.min(n - 1, parseInt(rowIn.value, 10)));
    var c = Math.max(0, Math.min(n - 1, parseInt(colIn.value, 10)));
    rowOut.textContent = 'A' + (r + 1);
    colOut.textContent = 'A' + (c + 1);
    var deps = here.result.deps[r][c] || [];
    /* A dependency that had not been filled when it was read. The order is
       dpOrder's, so this is a fact about the run and not about the recurrence. */
    var order = dpOrder({ rows: n, cols: n, order: orderIn.value });
    var position = {};
    order.forEach(function (rc, k) { position[rc[0] + ',' + rc[1]] = k; });
    var early = [];
    order.forEach(function (rc, k) {
      (here.result.deps[rc[0]][rc[1]] || []).forEach(function (d) {
        var key = d[0] + ',' + d[1];
        if (position[key] !== undefined && position[key] > k) early.push([rc, d]);
      });
    });

    document.getElementById('chValue').textContent = String(value);
    document.getElementById('chBrute').textContent = every ? String(every.cost) : 'refused';
    document.getElementById('chCount').textContent = every ? String(every.count) : '—';
    document.getElementById('chParen').textContent = parenText(tree);
    document.getElementById('chRecost').textContent = String(recost.cost);
    document.getElementById('chWorst').textContent = every ? String(every.worstCost) : '—';

    grid.innerHTML = dpGridSvg(here.result.table, {
      highlight: [[r, c]], deps: deps, cellH: 22,
      rowLabel: function (i) { return 'A' + (i + 1); },
      colLabel: function (j) { return 'A' + (j + 1); }
    });
    wrongGrid.innerHTML = dpGridSvg(bad.result.table, {
      cellH: 22,
      rowLabel: function (i) { return 'A' + (i + 1); },
      colLabel: function (j) { return 'A' + (j + 1); }
    });

    var rows = '';
    rows += '<tr class="tone-cyan"><th class="rowhead">by interval length</th><td>'
      + good.result.table[0][n - 1] + '</td><td>the shorter intervals are filled first, so '
      + 'every read hits a finished cell</td></tr>';
    rows += '<tr class="' + (bad.result.table[0][n - 1] === good.result.table[0][n - 1]
        ? '' : 'tone-red') + '"><th class="rowhead">row by row</th><td>'
      + bad.result.table[0][n - 1] + '</td><td>'
      + (bad.result.table[0][n - 1] === good.result.table[0][n - 1]
          ? 'the same here, which is luck and not a reason'
          : 'a cell was read before it was filled, and null plus a number is a number')
      + '</td></tr>';
    if (every) {
      rows += '<tr class="tone-amber"><th class="rowhead">every bracketing</th><td>'
        + every.cost + '</td><td>' + every.count + ' of them, enumerated by a recursion with no '
        + 'table at all</td></tr>';
    }
    rows += '<tr><th class="rowhead">the bracketing re-costed</th><td>' + recost.cost
      + '</td><td class="tt">' + parenText(tree) + '</td></tr>';
    rows += '<tr><th class="rowhead">cells read too early</th><td>' + early.length
      + '</td><td>' + (early.length
          ? early.slice(0, 3).map(function (e) {
              return '(' + e[0][0] + ',' + e[0][1] + ') read (' + e[1][0] + ',' + e[1][1] + ')';
            }).join('; ')
          : 'none in this order') + '</td></tr>';
    ordersT.innerHTML = '<thead><tr><th>route</th><th>answer</th><th>why</th></tr></thead>'
      + '<tbody>' + rows + '</tbody>';

    status.innerHTML = 'Filling ' + (orderIn.value === 'rowmajor' ? 'row by row' : 'by interval '
      + 'length') + ' gives <strong>' + value + '</strong> multiplications for '
      + n + ' matrices. '
      + (every
          ? 'Enumerating all <strong>' + every.count + '</strong> bracketings — a recursion '
            + 'with no table in it — the cheapest costs <strong>' + every.cost + '</strong>, '
            + (value === every.cost
                ? 'which this order reached, and the most expensive costs ' + every.worstCost + '.'
                : '<span class="tone-red">which this order did not reach.</span>')
          : '<span class="tone-amber">The enumeration was refused: ' + why + '.</span>')
      + ' The bracketing the table reconstructs is <span class="tt">' + parenText(tree)
      + '</span>, and re-multiplying it out from the dimensions alone costs ' + recost.cost
      + (recost.cost === good.result.table[0][n - 1]
          ? ' — the same number the table holds, derived a second time.'
          : ' <span class="tone-red">— which is not what the table holds.</span>')
      + ' In this fill order <strong>' + early.length + '</strong> read'
      + (early.length === 1 ? '' : 's') + ' landed on a cell that had not been filled yet'
      + (early.length
          ? ', and a null read as zero is how a table finishes with a number nobody can use.'
          : '.');
  }

  presetIn.addEventListener('change', function () {
    var p = CHP[presetIn.value];
    if (p) dimsIn.value = p.dims;
    redraw();
  });
  [dimsIn, orderIn, rowIn, colIn].forEach(function (el) {
    el.addEventListener('input', redraw);
    el.addEventListener('change', redraw);
  });
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="The order the cells are filled in is part of the algorithm",
        subtitle="By interval length against row by row, both against every bracketing",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Choose the dimensions and the fill order"),
        panel_intro=cfg.get(
            "panel_intro",
            "Both orders run the same recurrence. One of them reads cells that are still "
            "empty, and the page counts those reads rather than describing them. The answer "
            "is checked against every bracketing, enumerated without a table.",
        ),
        script=script,
        expect={"chPreset": _expect(_CH_PRESETS)},
    )


# ---------------------------------------------------------------------------
# lis -- the table, the tails array, and every subsequence
# ---------------------------------------------------------------------------

_LS_PRESETS = [
    {
        "id": "classic",
        "label": "ten values, the usual worked example",
        "spec": "10 9 2 5 3 7 101 18 4 8",
        "expect": {
            "lsTable": "4",
            "lsBrute": "4",
            "lsSame": "no",
        },
    },
    {
        "id": "sorted",
        "label": "already increasing",
        "spec": "1 2 3 4 5 6 7 8",
        "expect": {
            "lsTable": "8",
            "lsSame": "on this input, yes",
        },
    },
    {
        "id": "reversed",
        "label": "strictly decreasing",
        "spec": "9 8 7 6 5 4 3 2",
        "expect": {
            "lsTable": "1",
            "lsBrute": "1",
        },
    },
    {
        "id": "ties",
        "label": "repeated values",
        "spec": "3 1 4 1 5 9 2 6 5 3",
        "expect": {
            "lsTable": "4",
            "lsBrute": "4",
            "lsSame": "no",
        },
    },
]


def _lis(cfg):
    chosen = _chosen(_LS_PRESETS, cfg)
    markup = (
        _toolbar(
            "The tails array has the right length and the wrong contents",
            "three routes to the length, and two checks on the subsequence",
            [("cyan", "in the subsequence the table reconstructs"),
             ("amber", "in the tails array"), ("muted", "in neither")],
        )
        + _stage(_svg("lsPlot", "0 0 660 200",
                      "The sequence, with the reconstructed subsequence marked.")
                 + _svg("lsGrid", "0 0 660 70",
                        "The per-position table: the length of the best subsequence ending "
                        "there."))
        + _table("lsSteps")
        + _banner("lsStatus")
    )
    controls = (
        _select("lsPreset", "Sequence", _options(_LS_PRESETS), chosen["id"])
        + _text("lsSpec", "The sequence", chosen["spec"])
        + _range("lsStep", "Tails array after position", 1, 14, 14)
        + _kpis([("Length, from the table", "lsTable"),
                 ("Length, from the tails array", "lsTails"),
                 ("Length, over every subsequence", "lsBrute"),
                 ("The answer is increasing", "lsInc"),
                 ("And is a subsequence of the input", "lsSub"),
                 ("Tails array equals the answer", "lsSame")])
        + _hint(
            "lsHint",
            "Two algorithms, one answer. The <em>n</em><sup>2</sup> table stores, for each "
            "position, the length of the best increasing run ending there, and a predecessor "
            "so the run itself can be read back. The tails array keeps the smallest possible "
            "last value for each length and finds the same number with a binary search "
            "&mdash; but it is not the subsequence, and the panel checks whether the two "
            "coincide on this input.",
        )
    )
    script = _CORE_JS + _TWO_ROUTES + _presets_js(
        "LSP", _LS_PRESETS, ["spec"]) + r"""
  var presetIn = document.getElementById('lsPreset'), specIn = document.getElementById('lsSpec');
  var stepIn = document.getElementById('lsStep'), stepOut = document.getElementById('lsStepOut');
  var plot = document.getElementById('lsPlot'), grid = document.getElementById('lsGrid');
  var stepsT = document.getElementById('lsSteps'), status = document.getElementById('lsStatus');
  var KPIS = ['lsTable', 'lsTails', 'lsBrute', 'lsInc', 'lsSub', 'lsSame'];

  function blank(why) {
    plot.innerHTML = ''; grid.innerHTML = ''; stepsT.innerHTML = '';
    for (var i = 0; i < KPIS.length; i += 1) document.getElementById(KPIS[i]).textContent = '—';
    status.innerHTML = '<span class="tone-red">' + why + '.</span>';
  }

  function redraw() {
    var pr = dpParseNums(specIn.value, 14, -99, 999);
    if (pr.bad) { blank(pr.bad); return; }
    var a = pr.values;

    var table = lisTable(a), tails = lisTails(a);
    var brute = null, why = '';
    try { brute = lisBrute(a); } catch (err) { why = String(err.message); }
    var answer = table.result.subsequence;
    var inc = isIncreasingRun(answer), sub = isSubsequenceOf(answer, a);
    var same = tails.result.tails.join(',') === answer.join(',');

    stepIn.max = a.length;
    var k = Math.max(1, Math.min(a.length, parseInt(stepIn.value, 10)));
    stepOut.textContent = k + ' of ' + a.length;
    var here = tails.trace[k - 1] || { tails: [] };

    document.getElementById('lsTable').textContent = String(table.result.length);
    document.getElementById('lsTails').textContent = String(tails.result.length);
    document.getElementById('lsBrute').textContent = brute ? String(brute.result.length) : 'refused';
    document.getElementById('lsInc').textContent = inc ? 'yes' : 'NO';
    document.getElementById('lsSub').textContent = sub ? 'yes' : 'NO';
    document.getElementById('lsSame').textContent = same ? 'on this input, yes' : 'no';

    plot.innerHTML = dpGridSvg([a, table.result.table], {
      cellH: 24,
      rowLabel: function (i) { return i === 0 ? 'value' : 'best'; },
      colLabel: function (j) { return String(j); }
    });
    grid.innerHTML = dpGridSvg([here.tails.length ? here.tails : [0]], {
      cellH: 24, rowLabel: function () { return 'tails'; },
      colLabel: function (j) { return 'len ' + (j + 1); }
    });

    var rows = '';
    tails.trace.forEach(function (st, i) {
      rows += '<tr class="' + (i === k - 1 ? 'tone-cyan' : '') + '"><th class="rowhead">'
        + (i + 1) + '</th><td>' + st.value + '</td><td>' + st.position + '</td><td>'
        + st.tails.join(' ') + '</td></tr>';
    });
    rows += '<tr class="tone-amber"><th class="rowhead">answer</th><td colspan="2">'
      + answer.join(' ') + '</td><td>from the table\'s predecessors, not from the tails</td></tr>';
    if (brute) {
      rows += '<tr><th class="rowhead">every subsequence</th><td colspan="2">'
        + brute.result.subsequence.join(' ') + '</td><td>' + brute.counts.nodes
        + ' of them tried</td></tr>';
    }
    stepsT.innerHTML = '<thead><tr><th>step</th><th>value</th><th>lands at</th>'
      + '<th>tails after it</th></tr></thead><tbody>' + rows + '</tbody>';

    status.innerHTML = 'The longest increasing subsequence has length <strong>'
      + table.result.length + '</strong> by the table, <strong>' + tails.result.length
      + '</strong> by the tails array'
      + (brute ? ', and <strong>' + brute.result.length + '</strong> over all '
                 + brute.counts.nodes + ' subsequences'
               : ' (<span class="tone-amber">the enumeration was refused: ' + why + '</span>)')
      + ' — '
      + ((table.result.length === tails.result.length
          && (!brute || brute.result.length === table.result.length))
          ? 'three routes, one number.'
          : '<span class="tone-red">they disagree, so at least one is wrong.</span>')
      + ' The subsequence itself is <span class="tt">' + answer.join(' ')
      + '</span>, which is ' + (inc ? 'increasing' : '<span class="tone-red">not increasing</span>')
      + ' and ' + (sub ? 'a subsequence of the input' : '<span class="tone-red">not a '
          + 'subsequence of the input</span>')
      + ' — both checked, because a sorted copy of the input has the first property and is not '
      + 'an answer. The tails array ends as <span class="tt">'
      + tails.result.tails.join(' ') + '</span>, which '
      + (same ? 'happens to be the same list on this input — a coincidence, and the reason the '
                + 'misconception survives'
              : 'is <span class="tone-amber">a different list</span>: it has the right length '
                + 'and the wrong contents, which is what it is for')
      + '.';
  }

  presetIn.addEventListener('change', function () {
    var p = LSP[presetIn.value];
    if (p) specIn.value = p.spec;
    redraw();
  });
  [specIn, stepIn].forEach(function (el) {
    el.addEventListener('input', redraw);
    el.addEventListener('change', redraw);
  });
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="The right length, and the wrong list",
        subtitle="Three routes to the length, and two separate checks on the subsequence",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Choose the sequence"),
        panel_intro=cfg.get(
            "panel_intro",
            "The tails array is the fast algorithm and it is not the answer. The page prints "
            "both, says whether they coincide on this input, and checks the answer against "
            "the two properties it must have.",
        ),
        script=script,
        expect={"lsPreset": _expect(_LS_PRESETS)},
    )


# ---------------------------------------------------------------------------
# coins -- the loop order that decides what you are counting
# ---------------------------------------------------------------------------

_CO_PRESETS = [
    {
        "id": "small",
        "label": "coins 1, 2, 5 and an amount of 5",
        "coins": "1 2 5",
        "amount": "5",
        "expect": {
            "coComb": "4",
            "coPerm": "9",
            "coList": "4",
        },
    },
    {
        "id": "big",
        "label": "coins 1, 2, 5 and an amount of 100",
        "coins": "1 2 5",
        "amount": "100",
        "expect": {
            "coComb": "541",
            "coPerm": "91197869007632925819218",
            "coBig": "yes, the sequence count is",
        },
    },
    {
        "id": "sparse",
        "label": "coins 3, 7 and an amount of 20",
        "coins": "3 7",
        "amount": "20",
        # Six amounts below 20 have no representation in 3 and 7, 11 the largest, and
        # that is the run of zeros in the table rather than a tile. What the tiles hold
        # is the one amount this preset ships.
        "expect": {
            "coComb": "1",
            "coPerm": "6",
        },
    },
    {
        "id": "uk",
        "label": "the old British change problem",
        "coins": "1 2 5 10 20 50",
        "amount": "40",
        "expect": {
            "coComb": "236",
            "coPerm": "1255678045",
        },
    },
]


def _coins(cfg):
    chosen = _chosen(_CO_PRESETS, cfg)
    markup = (
        _toolbar(
            "Which loop is outside decides what you are counting",
            "combinations and ordered sequences, both exact, both listed where they fit",
            [("cyan", "the row after this coin type"), ("amber", "the target amount"),
             ("muted", "amounts below the coin")],
        )
        + _stage(_svg("coGrid", "0 0 660 180",
                      "One row per coin type, the number of ways to make each amount using "
                      "the coin types so far."))
        + _table("coWays")
        + _banner("coStatus")
    )
    controls = (
        _select("coPreset", "Coins and amount", _options(_CO_PRESETS), chosen["id"])
        + _text("coCoins", "Coin denominations", chosen["coins"])
        + _text("coAmount", "Amount", chosen["amount"])
        + _range("coRow", "Show the row after coin type", 1, 6, 1)
        + _kpis([("Combinations", "coComb"), ("Ordered sequences", "coPerm"),
                 ("Combinations, by recursion", "coCombB"),
                 ("Sequences, by recursion", "coPermB"),
                 ("Past what a double holds", "coBig"),
                 ("Combinations listed", "coList")])
        + _hint(
            "coHint",
            "Two nested loops, and swapping them changes the question. With the coin types on "
            "the outside each combination is built in one fixed order and is counted once. "
            "With the amounts on the outside, 1 then 2 and 2 then 1 are different sequences "
            "and both are counted. Readers write the second while meaning the first, so both "
            "are computed here and, where the amount is small, the objects themselves are "
            "listed.",
        )
    )
    script = _CORE_JS + _TWO_ROUTES + _presets_js(
        "COP", _CO_PRESETS, ["coins", "amount"]) + r"""
  var presetIn = document.getElementById('coPreset'), coinsIn = document.getElementById('coCoins');
  var amtIn = document.getElementById('coAmount');
  var rowIn = document.getElementById('coRow'), rowOut = document.getElementById('coRowOut');
  var grid = document.getElementById('coGrid');
  var waysT = document.getElementById('coWays'), status = document.getElementById('coStatus');
  var KPIS = ['coComb', 'coPerm', 'coCombB', 'coPermB', 'coBig', 'coList'];
  var TWO53 = 9007199254740992n;

  function blank(why) {
    grid.innerHTML = ''; waysT.innerHTML = '';
    for (var i = 0; i < KPIS.length; i += 1) document.getElementById(KPIS[i]).textContent = '—';
    status.innerHTML = '<span class="tone-red">' + why + '.</span>';
  }

  function redraw() {
    var cr = dpParseNums(coinsIn.value, 6, 1, 100);
    if (cr.bad) { blank('the coins: ' + cr.bad); return; }
    var coins = cr.values.slice().sort(function (a, b) { return a - b; });
    var amount = parseInt(amtIn.value, 10);
    if (!isFinite(amount) || amount < 0 || amount > 120) {
      blank('the amount is a whole number between 0 and 120'); return;
    }

    var comb = countWays(coins, amount, 'combinations');
    var perm = countWays(coins, amount, 'permutations');
    var combB = null, permB = null, combWhy = '', permWhy = '';
    try { combB = countBrute(coins, amount, 'combinations'); }
    catch (err) { combWhy = String(err.message); }
    try { permB = countBrute(coins, amount, 'permutations'); }
    catch (err2) { permWhy = String(err2.message); }
    var listed = null;
    try { listed = listCombinations(coins, amount); } catch (err2) { listed = null; }

    rowIn.max = coins.length;
    var k = Math.max(1, Math.min(coins.length, parseInt(rowIn.value, 10)));
    rowOut.textContent = String(coins[k - 1]);

    document.getElementById('coComb').textContent = String(comb.result.count);
    document.getElementById('coPerm').textContent = String(perm.result.count);
    document.getElementById('coCombB').textContent = combB === null ? 'refused' : String(combB);
    document.getElementById('coPermB').textContent = permB === null ? 'too many to count one by one' : String(permB);
    document.getElementById('coBig').textContent = perm.result.count > TWO53
      ? 'yes, the sequence count is' : 'no, both fit';
    document.getElementById('coList').textContent = listed
      ? String(listed.length) : 'not at this amount';

    var rows = comb.result.rows.map(function (r) { return r.row.map(function (x) { return x; }); });
    var shown = rows.slice(0, k);
    grid.innerHTML = shown.length ? dpGridSvg(shown, {
      cellH: 22,
      rowLabel: function (i) { return String(coins[i]); },
      colLabel: function (j) { return String(j); },
      highlight: [[shown.length - 1, amount]],
      cellText: function (v) { return String(v).length > 5 ? String(v).slice(0, 4) + '…' : String(v); }
    }) : '';

    var wrows = '';
    wrows += '<tr class="tone-cyan"><th class="rowhead">combinations</th><td>'
      + comb.result.count + '</td><td>coin types outside, amounts inside</td><td>'
      + (combB === null ? 'refused: ' + combWhy : (combB === comb.result.count
          ? 'a memo-free recursion agrees' : '<span class="tone-red">the recursion disagrees: '
            + combB + '</span>')) + '</td></tr>';
    wrows += '<tr class="tone-purple"><th class="rowhead">ordered sequences</th><td>'
      + perm.result.count + '</td><td>amounts outside, coin types inside</td><td>'
      + (permB === null ? 'refused: ' + permWhy : (permB === perm.result.count
          ? 'a memo-free recursion agrees' : '<span class="tone-red">the recursion disagrees: '
            + permB + '</span>')) + '</td></tr>';
    if (listed) {
      listed.slice(0, 8).forEach(function (m, i) {
        wrows += '<tr><th class="rowhead">' + (i + 1) + '</th><td>'
          + m.slice().sort(function (a, b) { return b - a; }).join(' + ')
          + '</td><td colspan="2">one combination, written large coin first</td></tr>';
      });
      if (listed.length > 8) {
        wrows += '<tr><th class="rowhead">…</th><td colspan="3">' + (listed.length - 8)
          + ' more, and ' + listed.length + ' in all — which is the number above</td></tr>';
      }
    }
    waysT.innerHTML = '<thead><tr><th>what is counted</th><th>how many</th><th>loop order</th>'
      + '<th>second route</th></tr></thead><tbody>' + wrows + '</tbody>';

    status.innerHTML = 'There are <strong>' + comb.result.count + '</strong> combinations of {'
      + coins.join(', ') + '} making ' + amount + ', and <strong>' + perm.result.count
      + '</strong> ordered sequences — the same two loops, swapped. '
      + (combB !== null && combB !== comb.result.count
          ? '<span class="tone-red">A memo-free recursion disagrees with the combination '
            + 'count.</span>'
          : (permB !== null && permB !== perm.result.count
              ? '<span class="tone-red">A memo-free recursion disagrees with the sequence '
                + 'count.</span>'
              : (combB !== null && permB !== null
                  ? 'Both were recomputed by recursions with no table at all, and both agree.'
                  : (combB !== null
                      ? 'The combination count was recomputed by a recursion with no table and '
                        + 'agrees; the sequence count could not be — <span class="tone-amber">'
                        + permWhy + '</span> — which is itself the reason the table exists.'
                      : '<span class="tone-amber">Neither check could run here: ' + combWhy
                        + '.</span>'))))
      + (listed
          ? ' The ' + listed.length + ' combinations are listed above, so the count is not a '
            + 'number to be believed but a list to be counted; there are ' + listed.length
            + ' of them and the table says ' + comb.result.count + '.'
          : ' At this amount the combinations are too many to list, and the table is the only '
            + 'route left.')
      + (perm.result.count > TWO53
          ? ' The sequence count is past 2^53, so a page holding it as a double would print a '
            + 'number that is <em>close</em>. This one is a BigInt and the digits are the '
            + 'digits.'
          : ' Both counts fit in a double here; they do not at larger amounts, which is why '
            + 'they are BigInts throughout.');
  }

  presetIn.addEventListener('change', function () {
    var p = COP[presetIn.value];
    if (p) { coinsIn.value = p.coins; amtIn.value = p.amount; }
    redraw();
  });
  [coinsIn, amtIn, rowIn].forEach(function (el) {
    el.addEventListener('input', redraw);
    el.addEventListener('change', redraw);
  });
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="Two loops, and the one you put outside is the question you asked",
        subtitle="Combinations and ordered sequences, exact in BigInt, both checked twice",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Choose the coins and the amount"),
        panel_intro=cfg.get(
            "panel_intro",
            "Both counts are BigInts: the number of ordered sequences passes what a double can "
            "hold at quite small amounts, and a count that is nearly right is not a count. "
            "Where the amount is small the combinations are listed, so the number can be "
            "checked by counting them.",
        ),
        script=script,
        expect={"coPreset": _expect(_CO_PRESETS)},
    )


# ---------------------------------------------------------------------------
# tree -- one postorder pass against every subset
# ---------------------------------------------------------------------------

_TR_PRESETS = [
    {
        "id": "star",
        "label": "a centre with four leaves",
        "spec": "1-2, 1-3, 1-4, 1-5",
        "weights": "3 4 2 1 5",
        "expect": {
            "trValue": "12",
            "trBrute": "12",
        },
    },
    {
        "id": "path",
        "label": "a path of six",
        "spec": "1-2, 2-3, 3-4, 4-5, 5-6",
        "weights": "5 1 5 1 5 1",
        "expect": {
            "trValue": "15",
            "trBrute": "15",
        },
    },
    {
        "id": "binary",
        "label": "a small binary tree",
        "spec": "1-2, 1-3, 2-4, 2-5, 3-6, 3-7",
        "weights": "10 2 2 4 4 4 4",
        "expect": {
            "trValue": "26",
            "trBrute": "26",
            "trIndep": "yes",
        },
    },
    {
        "id": "caterpillar",
        "label": "a spine with legs",
        "spec": "1-2, 2-3, 3-4, 2-5, 3-6, 4-7",
        "weights": "1 6 6 6 1 1 1",
        "expect": {
            "trValue": "13",
            "trBrute": "13",
        },
    },
]


def _tree(cfg):
    chosen = _chosen(_TR_PRESETS, cfg)
    markup = (
        _toolbar(
            "Two numbers per vertex, one pass, and every subset beside it",
            "the chosen set is re-checked against the edges and re-weighed",
            [("cyan", "chosen"), ("amber", "adjacent to a chosen vertex"),
             ("muted", "not chosen")],
        )
        + _stage(_svg("trTree", "0 0 520 240",
                      "The tree, each vertex labelled with its weight and the two numbers the "
                      "pass computed for it."))
        + _table("trPass")
        + _banner("trStatus")
    )
    controls = (
        _select("trPreset", "Tree", _options(_TR_PRESETS), chosen["id"])
        + _text("trSpec", "Edges, written 1-2", chosen["spec"])
        + _text("trWeights", "A weight per vertex", chosen["weights"])
        + _kpis([("Best total, one pass", "trValue"),
                 ("Best over every subset", "trBrute"),
                 ("The chosen set is independent", "trIndep"),
                 ("Re-weighed", "trWeight"),
                 ("Vertices visited", "trCalls"),
                 ("Subsets the check tried", "trSubsets")])
        + _hint(
            "trHint",
            "For each vertex the pass computes two numbers: the best total in its subtree "
            "<em>with</em> that vertex, and the best <em>without</em> it. With it, no child "
            "can be taken; without it, each child contributes whichever of its own two numbers "
            "is larger. One postorder pass answers the whole tree, and the answer is checked "
            "against every one of the 2<sup>n</sup> subsets.",
        )
    )
    script = _CORE_JS + _TWO_ROUTES + _presets_js(
        "TRP", _TR_PRESETS, ["spec", "weights"]) + r"""
  var presetIn = document.getElementById('trPreset'), specIn = document.getElementById('trSpec');
  var wIn = document.getElementById('trWeights');
  var tree = document.getElementById('trTree');
  var passT = document.getElementById('trPass'), status = document.getElementById('trStatus');
  var KPIS = ['trValue', 'trBrute', 'trIndep', 'trWeight', 'trCalls', 'trSubsets'];

  function blank(why) {
    tree.innerHTML = ''; passT.innerHTML = '';
    for (var i = 0; i < KPIS.length; i += 1) document.getElementById(KPIS[i]).textContent = '—';
    status.innerHTML = '<span class="tone-red">' + why + '.</span> An edge is '
      + '<span class="tt">1-2</span>, and they are separated by commas.';
  }

  function redraw() {
    var parsed = dpParseTree(specIn.value);
    if (parsed.bad) { blank(parsed.bad); return; }
    var wr = dpParseNums(wIn.value, 12, -99, 999);
    if (wr.bad) { blank('the weights: ' + wr.bad); return; }
    if (wr.values.length !== parsed.n) {
      blank('there are ' + parsed.n + ' vertices and ' + wr.values.length + ' weights');
      return;
    }
    var w = wr.values;

    var run = treeDp(parsed.tree, w);
    var brute = null, why = '';
    try { brute = misBrute(parsed.tree, w); } catch (err) { why = String(err.message); }
    var chosen = run.result.chosen;
    var indep = isIndependentSet(parsed.edges, chosen);
    var weight = setWeight(w, chosen);

    document.getElementById('trValue').textContent = String(run.result.value);
    document.getElementById('trBrute').textContent = brute ? String(brute.result.value) : 'refused';
    document.getElementById('trIndep').textContent = indep ? 'yes' : 'NO';
    document.getElementById('trWeight').textContent = weight === run.result.value
      ? String(weight) : (weight + ' ≠ ' + run.result.value);
    document.getElementById('trCalls').textContent = String(run.counts.calls);
    document.getElementById('trSubsets').textContent = brute ? String(brute.counts.nodes) : '—';

    var pick = {};
    chosen.forEach(function (v) { pick[v] = true; });
    var near = {};
    parsed.edges.forEach(function (e) {
      if (pick[e[0]]) near[e[1]] = true;
      if (pick[e[1]]) near[e[0]] = true;
    });
    tree.innerHTML = drawTree(null, rootedNodes(parsed.tree, 0), rootedKids,
      function (nd) { return String(w[nd.v]); },
      { width: 500, height: 220, radius: 14,
        fill: function (n) {
          return pick[n.node.v] ? 'var(--cyan)'
               : (near[n.node.v] ? 'var(--amber)' : 'var(--panel-3)');
        },
        note: function (n) {
          return (n.node.v + 1) + ': ' + run.result.withV[n.node.v] + '/'
            + run.result.without[n.node.v];
        } });

    var rows = '';
    run.result.order.forEach(function (v) {
      rows += '<tr class="' + (pick[v] ? 'tone-cyan' : '') + '"><th class="rowhead">'
        + (v + 1) + '</th><td>' + w[v] + '</td><td>' + run.result.withV[v] + '</td><td>'
        + run.result.without[v] + '</td><td>' + (pick[v] ? 'chosen' : '') + '</td></tr>';
    });
    rows += '<tr class="tone-amber"><th class="rowhead">answer</th><td colspan="2">{'
      + chosen.map(function (v) { return v + 1; }).join(', ') + '}</td><td>' + weight
      + '</td><td>' + (indep ? 'no two are joined by an edge' : 'NOT INDEPENDENT') + '</td></tr>';
    if (brute) {
      rows += '<tr><th class="rowhead">every subset</th><td colspan="2">{'
        + brute.result.members.map(function (v) { return v + 1; }).join(', ') + '}</td><td>'
        + brute.result.value + '</td><td>' + brute.counts.nodes + ' tried</td></tr>';
    }
    passT.innerHTML = '<thead><tr><th>vertex</th><th>weight</th><th>with it</th>'
      + '<th>without it</th><th></th></tr></thead><tbody>' + rows + '</tbody>';

    status.innerHTML = 'One postorder pass over ' + parsed.n + ' vertices — '
      + run.counts.calls + ' visits — gives <strong>' + run.result.value + '</strong>. '
      + (brute
          ? 'Trying all ' + brute.counts.nodes + ' subsets gives <strong>'
            + brute.result.value + '</strong>, '
            + (brute.result.value === run.result.value
                ? 'the same number by a route that knows nothing about subtrees.'
                : '<span class="tone-red">a different number, so the pass is wrong.</span>')
          : '<span class="tone-amber">The exhaustive check was refused: ' + why + '.</span>')
      + ' The set it chose is {' + chosen.map(function (v) { return v + 1; }).join(', ')
      + '}, which was checked against every edge — '
      + (indep ? 'no two of them are joined' : '<span class="tone-red">two of them are '
          + 'joined, so it is not an independent set at all</span>')
      + ' — and re-weighed to ' + weight
      + (weight === run.result.value
          ? ', which is the number above, added a second time from the weights.'
          : ' <span class="tone-red">, which is not the number above.</span>');
  }

  presetIn.addEventListener('change', function () {
    var p = TRP[presetIn.value];
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
        title="A dynamic program with no table at all",
        subtitle="Two numbers per vertex, one pass, and every subset as the check",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Choose the tree and the weights"),
        panel_intro=cfg.get(
            "panel_intro",
            "The subproblems here are subtrees rather than prefixes, and the order is a "
            "postorder walk rather than a loop. The answer is checked against every subset, "
            "and the set it returns is re-checked independent and re-weighed.",
        ),
        script=script,
        expect={"trPreset": _expect(_TR_PRESETS)},
    )


# ---------------------------------------------------------------------------
# game -- won and lost positions, and the period
# ---------------------------------------------------------------------------

_GM_PRESETS = [
    {
        "id": "subtract123",
        "label": "take 1, 2 or 3",
        "moves": "1 2 3",
        "upto": "16",
        "expect": {
            "gmLose": "0 4 8 12 16",
            "gmPeriod": "4",
        },
    },
    {
        "id": "subtract12",
        "label": "take 1 or 2",
        "moves": "1 2",
        "upto": "14",
        "expect": {
            "gmLose": "0 3 6 9 12",
            "gmPeriod": "3",
        },
    },
    {
        "id": "subtract134",
        "label": "take 1, 3 or 4",
        "moves": "1 3 4",
        "upto": "18",
        "expect": {
            "gmLose": "0 2 7 9 14 16",
            "gmPeriod": "7",
        },
    },
    {
        "id": "subtract25",
        "label": "take 2 or 5",
        "moves": "2 5",
        "upto": "18",
        "expect": {
            "gmLose": "0 1 4 7 8 11 14 15 18",
            "gmPeriod": "7",
        },
    },
]


def _game(cfg):
    chosen = _chosen(_GM_PRESETS, cfg)
    markup = (
        _toolbar(
            "Won and lost, computed from the definition",
            "a position loses exactly when every move from it wins",
            [("cyan", "a winning position"), ("red", "a losing position"),
             ("muted", "unreachable")],
        )
        + _stage(_svg("gmGrid", "0 0 660 90",
                      "Each position from zero upward, labelled won or lost."))
        + _table("gmRows")
        + _banner("gmStatus")
    )
    controls = (
        _select("gmPreset", "Subtraction set", _options(_GM_PRESETS), chosen["id"])
        + _text("gmMoves", "How many may be taken", chosen["moves"])
        + _text("gmUpto", "Positions to label, from zero up to", chosen["upto"])
        + _kpis([("Losing positions", "gmLose"),
                 ("The pattern repeats every", "gmPeriod"),
                 ("A memo-free recursion agrees", "gmAgree"),
                 ("Positions labelled", "gmN"),
                 ("Calls the table made", "gmCalls"),
                 ("Position 0 is", "gmZero")])
        + _hint(
            "gmHint",
            "Two players alternate and take between them the numbers you type; whoever cannot "
            "move loses. A position is <em>losing</em> exactly when every move from it leads "
            "to a winning position, and <em>winning</em> when some move leads to a losing one. "
            "That is the whole definition and the table is it, evaluated upward from zero. The "
            "period is then a fact about the table rather than a claim about the game.",
        )
    )
    script = _CORE_JS + _TWO_ROUTES + _presets_js(
        "GMP", _GM_PRESETS, ["moves", "upto"]) + r"""
  var presetIn = document.getElementById('gmPreset'), movesIn = document.getElementById('gmMoves');
  var uptoIn = document.getElementById('gmUpto');
  var grid = document.getElementById('gmGrid');
  var rowsT = document.getElementById('gmRows'), status = document.getElementById('gmStatus');
  var KPIS = ['gmLose', 'gmPeriod', 'gmAgree', 'gmN', 'gmCalls', 'gmZero'];

  function blank(why) {
    grid.innerHTML = ''; rowsT.innerHTML = '';
    for (var i = 0; i < KPIS.length; i += 1) document.getElementById(KPIS[i]).textContent = '—';
    status.innerHTML = '<span class="tone-red">' + why + '.</span>';
  }

  function redraw() {
    var mr = dpParseNums(movesIn.value, 5, 1, 12);
    if (mr.bad) { blank('the subtraction set: ' + mr.bad); return; }
    var moveSet = mr.values.slice().sort(function (a, b) { return a - b; });
    var upto = parseInt(uptoIn.value, 10);
    if (!isFinite(upto) || upto < 1 || upto > 24) { blank('label between 1 and 24 positions'); return; }

    var positions = [];
    for (var i = 0; i <= upto; i += 1) positions.push(i);
    var run = gameLabels(function (p) {
      return moveSet.map(function (m) { return p - m; }).filter(function (q) { return q >= 0; });
    }, positions);

    var disagree = [], why = '';
    try {
      positions.forEach(function (p) {
        if (gameBrute(moveSet, p) !== run.result.label[p]) disagree.push(p);
      });
    } catch (err) { why = String(err.message); }

    document.getElementById('gmLose').textContent = run.result.losing.join(' ') || 'none';
    document.getElementById('gmPeriod').textContent = run.result.period === null
      ? 'no repeat found' : String(run.result.period);
    document.getElementById('gmAgree').textContent = why
      ? 'refused' : (disagree.length ? 'NO, at ' + disagree.join(' ') : 'every position');
    document.getElementById('gmN').textContent = String(positions.length);
    document.getElementById('gmCalls').textContent = String(run.counts.calls);
    document.getElementById('gmZero').textContent = run.result.label[0] === 'L'
      ? 'losing, as it must be' : 'WINNING, which is wrong';

    grid.innerHTML = dpGridSvg([positions.map(function (p) { return run.result.label[p]; })], {
      cellH: 24, rowLabel: function () { return 'W/L'; },
      colLabel: function (j) { return String(j); },
      highlight: run.result.losing.map(function (p) { return [0, p]; })
    });

    var rows = '';
    positions.forEach(function (p) {
      if (p > 18) return;
      var opts = moveSet.filter(function (m) { return m <= p; });
      rows += '<tr class="' + (run.result.label[p] === 'L' ? 'tone-red' : '')
        + '"><th class="rowhead">' + p + '</th><td>'
        + (opts.length ? opts.map(function (m) {
              return (p - m) + run.result.label[p - m]; }).join(' ') : 'no moves')
        + '</td><td>' + (run.result.label[p] === 'L' ? 'lost' : 'won') + '</td><td>'
        + (run.result.label[p] === 'L'
            ? (opts.length ? 'every move leads to a win for the other player'
                           : 'the player to move cannot move')
            : 'some move leads to a loss for the other player') + '</td></tr>';
    });
    rowsT.innerHTML = '<thead><tr><th>position</th><th>moves lead to</th><th>verdict</th>'
      + '<th>why</th></tr></thead><tbody>' + rows + '</tbody>';

    status.innerHTML = 'Taking from {' + moveSet.join(', ') + '}, the losing positions up to '
      + upto + ' are <strong>' + (run.result.losing.join(', ') || 'none') + '</strong>'
      + (run.result.period === null
          ? ', and no repeat was found in this range.'
          : ', and the labels repeat every <strong>' + run.result.period
            + '</strong> positions — a repeat found by comparing the table with itself, not a '
            + 'pattern asserted from the first few rows.')
      + ' ' + (why
          ? '<span class="tone-amber">The checking recursion was refused: ' + why + '.</span>'
          : (disagree.length
              ? '<span class="tone-red">A memo-free recursion disagrees at ' + disagree.join(', ')
                + '.</span>'
              : 'Every label was recomputed by a recursion with no table, and all '
                + positions.length + ' agree.'))
      + ' Position 0 is losing because the player to move has no move at all, which is where '
      + 'the whole table starts.';
  }

  presetIn.addEventListener('change', function () {
    var p = GMP[presetIn.value];
    if (p) { movesIn.value = p.moves; uptoIn.value = p.upto; }
    redraw();
  });
  [movesIn, uptoIn].forEach(function (el) {
    el.addEventListener('input', redraw);
    el.addEventListener('change', redraw);
  });
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="Won and lost, one position at a time",
        subtitle="The definition evaluated upward, and checked against a recursion",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Choose the subtraction set"),
        panel_intro=cfg.get(
            "panel_intro",
            "Every label comes from the definition applied to positions already labelled. The "
            "period is detected by comparing the table with itself, and every label is "
            "recomputed by a memo-free recursion.",
        ),
        script=script,
        expect={"gmPreset": _expect(_GM_PRESETS)},
    )


# ---------------------------------------------------------------------------
# tsp -- 2^n subsets against (n-1)! tours
# ---------------------------------------------------------------------------

_TS_PRESETS = [
    {
        "id": "four",
        "label": "four cities, asymmetric",
        "spec": "0 2 9 10; 1 0 6 4; 15 7 0 8; 6 3 12 0",
        "expect": {
            "tsHK": "21",
            "tsBrute": "21",
        },
    },
    {
        "id": "five",
        "label": "five cities on a rough circle",
        "spec": "0 3 4 2 7; 3 0 4 6 3; 4 4 0 5 8; 2 6 5 0 6; 7 3 8 6 0",
        "expect": {
            "tsHK": "19",
            "tsWorkHK": "800",
            "tsWorkBF": "24",
        },
    },
    {
        "id": "six",
        "label": "six cities, where the counts pull apart",
        "spec": "0 4 7 3 9 5; 4 0 6 8 2 7; 7 6 0 5 8 3; 3 8 5 0 6 4; 9 2 8 6 0 5; 5 7 3 4 5 0",
        "expect": {
            "tsHK": "22",
            "tsWorkHK": "2304",
            "tsWorkBF": "120",
        },
    },
    {
        "id": "trap",
        "label": "a matrix that violates the triangle inequality",
        "spec": "0 1 1 50; 1 0 1 1; 1 1 0 1; 50 1 1 0",
        "expect": {
            "tsHK": "4",
            "tsBrute": "4",
        },
    },
]


def _tsp(cfg):
    chosen = _chosen(_TS_PRESETS, cfg)
    markup = (
        _toolbar(
            "Exponential is not the same as hopeless",
            "n squared times two to the n, against n minus one factorial",
            [("cyan", "the tour"), ("purple", "the city the tour starts and ends at"),
             ("muted", "an edge not used")],
        )
        + _stage(_svg("tsPlot", "0 0 300 210",
                      "The cities on a circle with the optimal tour drawn.")
                 + _svg("tsGrid", "0 0 300 210",
                        "The Held-Karp table: one row per subset size, one column per end "
                        "city."))
        + _table("tsRows")
        + _banner("tsStatus")
    )
    controls = (
        _select("tsPreset", "Distance matrix", _options(_TS_PRESETS), chosen["id"])
        + _text("tsSpec", "Distances, rows separated by semicolons", chosen["spec"])
        + _range("tsStep", "Show the table after subset", 1, 63, 1)
        + _kpis([("Shortest tour, Held-Karp", "tsHK"),
                 ("Shortest tour, every ordering", "tsBrute"),
                 ("The tour re-measured", "tsCheck"),
                 ("The tour is a tour", "tsValid"),
                 ("Held-Karp work, n squared 2 to the n", "tsWorkHK"),
                 ("Brute-force work, n minus 1 factorial", "tsWorkBF")])
        + _hint(
            "tsHint",
            "A row is one city's distances to all of them, and the diagonal is zero. The "
            "matrix need not be symmetric and nothing here assumes the triangle inequality. "
            "Held-Karp fills one entry per (subset, end city) pair, which is "
            "<em>n</em>2<sup>n</sup> entries and <em>n</em><sup>2</sup>2<sup>n</sup> work; "
            "trying every ordering is (<em>n</em>&minus;1)! tours. Both figures are printed "
            "as exact integers, because the whole point is how fast they pull apart.",
        )
    )
    script = _CORE_JS + _TWO_ROUTES + _presets_js(
        "TSP", _TS_PRESETS, ["spec"]) + r"""
  var presetIn = document.getElementById('tsPreset'), specIn = document.getElementById('tsSpec');
  var stepIn = document.getElementById('tsStep'), stepOut = document.getElementById('tsStepOut');
  var plot = document.getElementById('tsPlot'), grid = document.getElementById('tsGrid');
  var rowsT = document.getElementById('tsRows'), status = document.getElementById('tsStatus');
  var KPIS = ['tsHK', 'tsBrute', 'tsCheck', 'tsValid', 'tsWorkHK', 'tsWorkBF'];

  function blank(why) {
    plot.innerHTML = ''; grid.innerHTML = ''; rowsT.innerHTML = '';
    for (var i = 0; i < KPIS.length; i += 1) document.getElementById(KPIS[i]).textContent = '—';
    status.innerHTML = '<span class="tone-red">' + why + '.</span> A row is the distances from '
      + 'one city, and rows are separated by semicolons.';
  }

  function redraw() {
    var parsed = dpParseMatrix(specIn.value, 7);
    if (parsed.bad) { blank(parsed.bad); return; }
    var D = parsed.D, n = D.length;

    var hk = heldKarp(D);
    var brute = null, why = '';
    try { brute = tspBrute(D); } catch (err) { why = String(err.message); }
    var valid = tourValid(hk.result.tour, n);
    var measured = valid ? tourLength(D, hk.result.tour) : null;

    stepIn.max = Math.max(1, hk.result.table.length);
    var k = Math.max(1, Math.min(hk.result.table.length, parseInt(stepIn.value, 10)));
    stepOut.textContent = k + ' of ' + hk.result.table.length;
    var shown = hk.result.table.slice(0, k).map(function (r) {
      return r.row.map(function (v) { return v === null ? null : v; });
    });

    document.getElementById('tsHK').textContent = String(hk.result.length);
    document.getElementById('tsBrute').textContent = brute ? String(brute.result.length) : 'refused';
    document.getElementById('tsCheck').textContent = measured === null ? 'NOT A TOUR' : String(measured);
    document.getElementById('tsValid').textContent = valid ? 'yes' : 'NO';
    document.getElementById('tsWorkHK').textContent = String(hk.result.heldKarpWork);
    document.getElementById('tsWorkBF').textContent = String(hk.result.bruteWork);

    plot.innerHTML = tourSvg(hk.result.tour, n, { width: 290, height: 200 });
    grid.innerHTML = dpGridSvg(shown, {
      width: 290, left: 44, cellH: 18,
      rowLabel: function (i) { return 'S' + (i + 1); },
      colLabel: function (j) { return String(j + 2); },
      cellText: function (v) { return v === null ? '·' : String(v); }
    });

    var rows = '';
    rows += '<tr class="tone-cyan"><th class="rowhead">Held-Karp</th><td>'
      + hk.result.tour.map(function (c) { return c + 1; }).join(' to ') + '</td><td>'
      + hk.result.length + '</td><td>' + hk.counts.reads + ' table reads</td></tr>';
    if (brute) {
      rows += '<tr><th class="rowhead">every ordering</th><td>'
        + (brute.result.tour || []).concat([0]).map(function (c) { return c + 1; }).join(' to ')
        + '</td><td>' + brute.result.length + '</td><td>' + brute.counts.nodes
        + ' tours tried</td></tr>';
    }
    rows += '<tr class="tone-amber"><th class="rowhead">re-measured</th><td>'
      + (valid ? 'visits every city once and returns' : 'NOT A VALID TOUR') + '</td><td>'
      + (measured === null ? '—' : measured) + '</td><td>'
      + (measured === hk.result.length ? 'added again from the matrix'
                                       : '<span class="tone-red">does not match</span>')
      + '</td></tr>';
    rows += '<tr><th class="rowhead">work</th><td>n^2 2^n = ' + hk.result.heldKarpWork
      + '</td><td>(n-1)! = ' + hk.result.bruteWork + '</td><td>'
      + (hk.result.heldKarpWork > hk.result.bruteWork
          ? 'at this n the table is the more expensive of the two, which is worth seeing'
          : 'the table is already cheaper, and the gap grows without bound')
      + '</td></tr>';
    rowsT.innerHTML = '<thead><tr><th>route</th><th>tour</th><th>length</th><th>cost</th>'
      + '</tr></thead><tbody>' + rows + '</tbody>';

    status.innerHTML = 'The shortest tour of these ' + n + ' cities is <strong>'
      + hk.result.length + '</strong>' + (brute
          ? ', and trying all ' + brute.counts.nodes + ' orderings gives ' + brute.result.length
            + ' — '
            + (brute.result.length === hk.result.length
                ? 'the same number by a route that fills no table.'
                : '<span class="tone-red">a different number.</span>')
          : ' (<span class="tone-amber">the enumeration was refused: ' + why + '</span>)')
      + ' The tour it returns '
      + (valid
          ? 'visits every city exactly once and comes back to the first, and re-adding its '
            + n + ' legs from the matrix gives ' + measured
            + (measured === hk.result.length
                ? ' — the number above, derived a second time.'
                : ' <span class="tone-red">, which is not the number above.</span>')
          : '<span class="tone-red"> is not a tour at all.</span>')
      + ' Held-Karp does about n^2 2^n = <strong>' + hk.result.heldKarpWork
      + '</strong> units of work against brute force\'s (n-1)! = <strong>'
      + hk.result.bruteWork + '</strong>. Both are exact integers. '
      + (hk.result.heldKarpWork > hk.result.bruteWork
          ? 'At this size the table LOSES, which is the honest part: 2^n beats n! only once n '
            + 'is large enough, and here it is not.'
          : 'The table wins here, and the margin grows without bound — but 2^n is still '
            + 'exponential, and no amount of it makes this problem tractable.');
  }

  presetIn.addEventListener('change', function () {
    var p = TSP[presetIn.value];
    if (p) specIn.value = p.spec;
    redraw();
  });
  [specIn, stepIn].forEach(function (el) {
    el.addEventListener('input', redraw);
    el.addEventListener('change', redraw);
  });
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="A table over subsets, and the factorial it replaces",
        subtitle="Held-Karp against every ordering, with both costs as exact integers",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Choose the distance matrix"),
        panel_intro=cfg.get(
            "panel_intro",
            "The subproblem here is a set rather than a prefix, which is the last shape of "
            "dynamic program this course meets. The tour that comes back is re-measured from "
            "the matrix, and the two work figures are exact integers rather than classes.",
        ),
        script=script,
        expect={"tsPreset": _expect(_TS_PRESETS)},
    )


# ---------------------------------------------------------------------------
# An unknown mode raises; see greedy.py's note on why a default would be worse.
# ---------------------------------------------------------------------------

_MODES = {
    "memo": _memo,
    "knapsack": _knapsack,
    "edit": _edit,
    "chain": _chain,
    "lis": _lis,
    "coins": _coins,
    "tree": _tree,
    "game": _game,
    "tsp": _tsp,
}

MODES = tuple(sorted(_MODES))


def dpkit_lab(cfg):
    """The dynamic-programming course's kit. `cfg["mode"]` chooses the lesson."""
    mode = (cfg or {}).get("mode")
    if mode not in _MODES:
        raise ValueError(
            "dpkit_lab: unknown mode %r; the nine dynamic-programming modes are %s"
            % (mode, ", ".join(MODES))
        )
    return _MODES[mode](cfg or {})


__all__ = ["dpkit_lab", "DPKIT_JS", "MODES"]
