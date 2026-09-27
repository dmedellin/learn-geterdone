"""Reductions -- five modes, and in every one of them the reduction is BUILT.

A REDUCTION SHOWN AS AN ARROW BETWEEN TWO NAMES TEACHES NOTHING. "3-SAT
reduces to independent set" is a sentence a reader can repeat and cannot use.
A reduction is a CONSTRUCTION, and every mode here puts the whole construction
on the page, in four parts that no mode is allowed to skip:

    the instance            the thing the reader typed, in the source problem
    the transformed         f(instance), built in front of them, with the
    instance                gadget's structure visible rather than described
    the solution mapped     a solution of the transformed instance, carried
    back                    back through the map, and CHECKED in the original
                            problem by the original problem's own rules
    the map on solutions    both problems solved exhaustively, every solution
                            of each enumerated, and the map between the two
                            sets checked for soundness, for completeness and
                            for injectivity -- three verdicts, not one word

THE FOURTH PART IS THE ONE THAT USUALLY GETS ASSERTED, AND IT IS OFTEN FALSE.
Three of these five reductions really are bijections on solutions -- and the
page says so because it computed all three properties, not because a textbook
does. One is sound in both directions and is neither injective nor surjective,
and the page says THAT, with the two independent sets that map to one
assignment on screen and the reason the map back cannot hit every assignment
written beside them. The fifth is not a map between instances at all.

A lab that printed "bijection" over all five would be wrong about two of them
and no markup check anywhere would notice. What a reduction has to preserve is
the ANSWER; preserving the solutions one for one is a stronger property that
some reductions have and some do not, and the difference is exactly the thing
worth computing rather than asserting.

    selfreduce      search from decision: n + 1 calls to a yes/no oracle
                    build a satisfying assignment. Not a map between
                    instances at all -- a map between two KINDS of question --
                    so the fourth part here is that every restricted formula's
                    answer is checked against brute force and the assignment
                    is verified clause by clause at the end.
    independentset  3-SAT to independent set. Sound, and the reverse
                    construction works on every model, but the solution map is
                    neither injective nor surjective: a clause with two true
                    literals gives two independent sets that map to the same
                    assignment, and the map back leaves any variable no chosen
                    literal mentions at false, so an assignment that sets one
                    of those true is the image of nothing. The page computes
                    all four facts and names them separately.
    complement      independent set, vertex cover and clique in the
                    complement. A genuine bijection, and the page checks it on
                    EVERY subset rather than on the optimal ones: S is
                    independent exactly when V minus S is a cover, and exactly
                    when S is a clique in the complement.
    subsetsum       3-SAT to subset sum by the digit table. A genuine
                    bijection: each clause column needs 4, a satisfying
                    assignment contributes 1, 2 or 3 to it, and exactly one of
                    the four slack combinations makes up the difference.
    tsp             Hamilton circuit to travelling salesman. A bijection, and
                    the map is the IDENTITY on the vertex sequence -- the tours
                    within budget and the Hamilton circuits are literally the
                    same list, which is the cleanest form this idea takes.

EVERYTHING IS EXPONENTIAL HERE AND THE CAPS SAY SO OUT LOUD. Checking a
reduction means solving both instances exhaustively, and the transformed
instance is bigger than the original -- 3m vertices for m clauses, 2n + 2m
numbers for n variables and m clauses. So every mode refuses above a stated
size through `oracleCap` rather than freezing the tab, and the refusal names
the size and the cap. That the checking is exponential in both directions at
once is not an inconvenience; it is the course.

WHAT IS COMPUTED AND WHAT IS CHECKED AGAINST SOMETHING ELSE.
`algo_core.REDUCTION_JS` holds the constructions -- `fixVariable`,
`selfReduce`, `tspFromGraph`, `satToIndependentSet`, `complementGraph`,
`satToSubsetSum`, `subsetSumDp` -- and `algo_core.ORACLE_JS` holds the
exhaustive solvers. Nothing here reimplements either. What this kit adds is
the solution-level checking that turns a reduction into a fact:

  both answers, separately   every mode brute-forces the original instance and
                             the transformed one with routines that share no
                             code, and prints the two answers. `checkTspReduction`
                             and `checkIndependentSetReduction` already do this
                             for the YES/NO answer; the modes go a level down.
  every solution, both ways  `rdIsSolutions`, `rdSubsetSolutions`,
                             `rdTourSolutions` and `rdComplementCheck`
                             enumerate the full solution set of each side and
                             compare them as SETS.
  the reverse construction   soundness alone is half a reduction. Each mode
                             also builds a solution of the transformed
                             instance FROM each solution of the original and
                             checks it is one, which is the direction a page
                             that only maps back never tests.
  a second route to the      `subsetSumDp` reaches the target by dynamic
  same yes/no                programming while the enumeration reaches it by
                             brute force, and `dpllRun`-style shortcuts are
                             deliberately absent: two exhaustive routes that
                             agree are evidence, one clever route is not.

THE THREE DRAWINGS ARE IN THE BLOCK, NOT IN THE MODES. `rdChainSvg` draws the
self-reduction's branch chain, `rdColumnSvg` the digit table's column totals
against the base, and `rdMatrixSvg` the distance matrix with the tour's steps
coloured. Each takes what it draws and returns a string; each has an installer
that takes the element FIRST and may be handed null. That is algo_core's rule
and it is not stylistic: `rdMatrixSvg` spent a draft closed over the mode's
`mat` element, where it drew half of what the travelling-salesman mode claims
and no test could call it.

BLOCKS PER MODE. COUNT_JS, DIGRAPH_JS, ORACLE_JS, REDUCTION_JS and this kit's
own block are on every page here; RATIONAL_JS is added by nothing, because
there is not a single fraction in this kit -- every figure is a count, a size,
a digit or a yes/no. `subsetsum` is the only mode whose numbers leave the
exact-integer range of a double and they are BigInt throughout, from
`satToSubsetSum`'s digit builder to `subsetSumDp`'s keys.

Measured, gzipped, on a real shipped lesson page with this lab swapped in --
Algorithms course 1 lesson 1, whose body is heavier than the median. Against
the repository's 62 KB ceiling:

    selfreduce 43.8   complement 44.1   independentset 44.2   tsp 44.2
    subsetsum 44.3

Re-derive them rather than trusting them. The spread is under a kilobyte
because every mode here carries the same four blocks: REDUCTION_JS is one
block and a mode cannot take half of it.

WHAT REDUCTION_JS SHIPS THAT NO MODE HERE CALLS. `colouringEnumerate`, the
gadget-colouring counter. Its cap is nine vertices, and the smallest honest
3-colouring clause gadget needs the base triangle, two vertices per variable
and six more per clause -- past nine before the first clause is built. Showing
the variable half alone would be showing a reduction that does not reduce
anything, which is the failure mode this kit exists to avoid. It is tested in
mathcheck's algo_core section and it is waiting for a mode that can afford it.

NOTHING HERE ROUNDS AND NOTHING HERE IS A PROBABILITY. Every quantity is an
integer or a verdict.
"""

from .algo_core import COUNT_JS, DIGRAPH_JS, ORACLE_JS, REDUCTION_JS
from .common import Lab

# ---------------------------------------------------------------------------
# The kit's own arithmetic. Top-level functions, no element touched, so
# scripts/mathcheck.js executes exactly the source that ships.
# ---------------------------------------------------------------------------

RDKIT_JS = r"""
  /* ------------------------------------------------------ what a reader types

     Two grammars, 1-based, the same two the randomised kit uses and written
     out again here rather than shared: these are two separate pages and a
     shared parser would save nothing on the wire while coupling two courses.

       a clause     `1 2 -3`, literals separated by spaces, clauses by a
                    semicolon or a newline. `-3` is NOT x3.
       an edge      `1-2`. Undirected: every problem in this kit ignores
                    direction, and a reader who types an arrow gets an edge. */
  var RD_MAXVARS = 6;
  var RD_MAXCLAUSES = 6;
  var RD_MAXN = 10;

  function rdPieces(text, re) {
    var parts = String(text).split(re), out = [], i;
    for (i = 0; i < parts.length; i += 1) {
      var s = parts[i].trim();
      if (s) out.push(s);
    }
    return out;
  }
  function rdParseCnf(text, maxVars, maxClauses) {
    maxVars = maxVars === undefined ? RD_MAXVARS : maxVars;
    maxClauses = maxClauses === undefined ? RD_MAXCLAUSES : maxClauses;
    var cl = rdPieces(text, /[;\n]+/), clauses = [], n = 0, i, k;
    if (!cl.length) return { bad: 'write at least one clause' };
    if (cl.length > maxClauses) return { bad: 'that is more than ' + maxClauses + ' clauses' };
    for (i = 0; i < cl.length; i += 1) {
      var lits = rdPieces(cl[i], /[\s,]+/), out = [];
      for (k = 0; k < lits.length; k += 1) {
        if (!/^-?\d+$/.test(lits[k])) return { bad: 'cannot read "' + lits[k] + '" as a literal' };
        var lit = parseInt(lits[k], 10);
        if (lit === 0) return { bad: 'there is no variable 0; the literals are 1, -1, 2, -2 and so on' };
        if (Math.abs(lit) > maxVars) return { bad: 'variable ' + Math.abs(lit) + ' is past ' + maxVars };
        out.push(lit);
        if (Math.abs(lit) > n) n = Math.abs(lit);
      }
      if (!out.length) return { bad: 'clause ' + (i + 1) + ' is empty' };
      clauses.push(out);
    }
    return { formula: { n: n, clauses: clauses } };
  }
  function rdParseGraph(text, maxN) {
    maxN = maxN === undefined ? RD_MAXN : maxN;
    var cl = rdPieces(text, /[,;\n]+/), raw = [], n = 0, i, seen = {};
    if (!cl.length) return { bad: 'write at least one edge' };
    for (i = 0; i < cl.length; i += 1) {
      var m = /^(\d+)\s*(?:-|>|to)\s*(\d+)$/.exec(cl[i]);
      if (!m) return { bad: 'cannot read "' + cl[i] + '" as an edge' };
      var u = parseInt(m[1], 10), v = parseInt(m[2], 10);
      if (u < 1 || v < 1) return { bad: 'labels start at 1, and "' + cl[i] + '" does not' };
      if (u > maxN || v > maxN) return { bad: 'label ' + Math.max(u, v) + ' is past ' + maxN };
      if (u === v) return { bad: 'a loop at ' + u + ' belongs to no cover and no clique' };
      var key = Math.min(u, v) + '-' + Math.max(u, v);
      if (seen[key]) continue;                 /* a repeated edge is the same edge */
      seen[key] = true;
      raw.push([u, v]);
      if (u > n) n = u;
      if (v > n) n = v;
    }
    if (!raw.length) return { bad: 'every edge you wrote was a duplicate of another' };
    if (n < 2) return { bad: 'two vertices is the smallest graph with an edge' };
    var G = dgNew(n, false);
    for (i = 0; i < raw.length; i += 1) dgAdd(G, raw[i][0] - 1, raw[i][1] - 1, 1, 0);
    return { G: G, n: n };
  }
  function rdClauseText(cl) {
    return cl.map(function (l) { return (l < 0 ? '¬x' : 'x') + Math.abs(l); }).join(' ∨ ');
  }
  function rdFormulaText(F) {
    return F.clauses.map(function (cl) { return '(' + rdClauseText(cl) + ')'; }).join(' ∧ ');
  }
  function rdAssignText(a) {
    return (a || []).map(function (v, i) { return 'x' + (i + 1) + '=' + (v ? 'T' : 'F'); }).join(' ');
  }
  function rdAssignKey(a) {
    return (a || []).map(function (v) { return v ? '1' : '0'; }).join('');
  }
  function rdSetText(list) {
    return '{' + (list || []).map(function (v) { return v + 1; }).join(', ') + '}';
  }
  function rdPlural(k, one, many) { return k === 1 ? one : many; }
  function rdIsRefusal(e) { return /exceeds the exhaustive cap/.test(String(e && e.message)); }

  /* --------------------------------------------------- the map on solutions

     THE ONE PIECE EVERY MODE SHARES, and the reason it is a function rather
     than a sentence. Given the solution set of the original instance, the
     solution set of the transformed one, and the map back, this reports the
     three properties separately:

       sound        every solution of the transformed instance maps to a
                    solution of the original. Without this the reduction is
                    simply wrong.
       surjective   every solution of the original is the image of at least
                    one solution of the transformed instance. This is the one
                    people mean when they say "complete", and it is the one
                    that most often fails for a perfectly correct reduction --
                    when the map back has to invent values the transformed
                    instance does not carry. Where it fails, the mode also
                    builds a solution of the transformed instance FROM each
                    solution of the original, which is the completeness the
                    reduction actually needs and a different computation.
       injective    no two solutions of the transformed instance map to the
                    same solution of the original. This one is OFTEN FALSE and
                    the reduction is still perfectly good, so the collisions
                    are collected rather than treated as failures.

     Solutions are compared by a caller-supplied KEY, because "the same
     solution" means different things in different problems -- a set, an
     assignment, a cyclic sequence -- and letting each mode say so is what
     keeps this function honest about what it is comparing. */
  function rdSolutionMap(originalKeys, transformed, mapBack) {
    var want = {}, hit = {}, collisions = {}, bad = [], pairs = [];
    originalKeys.forEach(function (k) { want[k] = true; });
    transformed.forEach(function (t) {
      var image = mapBack(t);
      pairs.push({ from: t, to: image });
      if (!want[image]) { bad.push({ from: t, to: image }); return; }
      if (hit[image]) {
        if (!collisions[image]) collisions[image] = [hit[image]];
        collisions[image].push(t);
      } else hit[image] = t;
    });
    var unhit = originalKeys.filter(function (k) { return !hit[k]; });
    var collisionKeys = Object.keys(collisions);
    return { pairs: pairs, sound: bad.length === 0, unsound: bad,
             surjective: unhit.length === 0, unhit: unhit,
             injective: collisionKeys.length === 0, collisions: collisions,
             collisionKeys: collisionKeys,
             bijection: bad.length === 0 && unhit.length === 0 && collisionKeys.length === 0,
             originals: originalKeys.length, images: transformed.length };
  }
  /* Every satisfying assignment of a formula, as keys and as arrays. The
     ORIGINAL side of three of these five reductions. */
  function rdSatSolutions(formula, cap) {
    cap = cap === undefined ? 12 : cap;
    oracleCap('rdSatSolutions', formula.n, cap);
    var out = [];
    forEachSubset(formula.n, function (mask) {
      var a = maskAssign(mask, formula.n);
      if (satEval(formula, a) === formula.clauses.length) {
        out.push({ mask: mask, assign: a, key: rdAssignKey(a) });
      }
    });
    return out;
  }

  /* ---------------------------------------------- search from decision

     The reduction is between two KINDS of question and not between two
     instances, so what it produces is a sequence of restricted formulas. This
     wraps `selfReduce` and adds the check it does not make: at every step the
     restricted formula's yes/no answer is taken from brute force AGAIN, by a
     separate call, and the two are required to agree. */
  function rdSelfTrace(formula, cap) {
    cap = cap === undefined ? 12 : cap;
    oracleCap('rdSelfTrace', formula.n, cap);
    var run = selfReduce(formula);
    var steps = [], cur = formula, v;
    var decided = satBrute(formula).result.satisfiable;
    for (v = 1; v <= formula.n && run.result.satisfiable; v += 1) {
      var withTrue = fixVariable(cur, v, true), withFalse = fixVariable(cur, v, false);
      var okTrue = satBrute(withTrue).result.satisfiable
                   && !withTrue.clauses.some(function (cl) { return cl.length === 0; });
      var okFalse = satBrute(withFalse).result.satisfiable
                    && !withFalse.clauses.some(function (cl) { return cl.length === 0; });
      var took = run.result.assignment[v - 1];
      steps.push({ variable: v, ifTrue: okTrue, ifFalse: okFalse, took: took,
                   agrees: took === okTrue,
                   clausesBefore: cur.clauses.length,
                   restricted: took ? withTrue : withFalse,
                   clausesAfter: (took ? withTrue : withFalse).clauses.length });
      cur = took ? withTrue : withFalse;
    }
    var solutions = rdSatSolutions(formula, cap);
    var verified = run.result.assignment
      ? satEval(formula, run.result.assignment) === formula.clauses.length : null;
    return { run: run, steps: steps, decided: decided, verified: verified,
             satisfiable: run.result.satisfiable,
             calls: run.result.oracleCalls === undefined ? formula.n + 1 : run.result.oracleCalls,
             expectedCalls: formula.n + 1,
             bruteWork: Math.pow(2, formula.n),
             solutions: solutions,
             agrees: run.result.satisfiable === decided,
             everyStepAgrees: steps.every(function (s) { return s.agrees; }) };
  }

  /* ------------------------------------------ 3-SAT to independent set

     `satToIndependentSet` builds the graph: one vertex per literal occurrence,
     a triangle per clause so at most one vertex per clause can be chosen, and
     an edge between every contradictory pair so no two chosen literals
     disagree. An independent set of size m therefore picks exactly one true
     literal from each clause without contradiction, which IS an assignment.

     The two directions, both computed:
       forward   every independent set of size m, mapped back to an
                 assignment, must satisfy the formula.
       backward  every satisfying assignment, turned into an independent set
                 by taking the first true literal of each clause, must come
                 out independent and of size m.

     Variables the chosen literals never mention are left FALSE, which is why
     the map is not injective and, on some formulas, why two assignments that
     differ only on an unused variable are not both images. Both facts are
     computed below rather than explained away. */
  function rdIsBack(made, members) {
    var assign = [], i;
    for (i = 0; i < made.vars; i += 1) assign.push(false);
    members.forEach(function (idx) {
      var lit = made.nodes[idx].lit;
      assign[Math.abs(lit) - 1] = lit > 0;
    });
    return assign;
  }
  function rdIsForward(made, formula, assign) {
    /* the FIRST true literal of each clause, which is a canonical choice and
       therefore reproducible: two readers see the same set. The nodes are in
       clause order, so the first matching node of a clause is that literal. */
    var picked = [], ok = true;
    formula.clauses.forEach(function (cl, ci) {
      var chosen = -1;
      made.nodes.forEach(function (node, idx) {
        if (chosen >= 0 || node.clause !== ci) return;
        if ((node.lit > 0) === assign[Math.abs(node.lit) - 1]) chosen = idx;
      });
      if (chosen < 0) ok = false; else picked.push(chosen);
    });
    return { members: picked.sort(function (a, b) { return a - b; }), ok: ok };
  }
  function rdIsIndependent(adj, members) {
    for (var i = 0; i < members.length; i += 1) {
      for (var j = i + 1; j < members.length; j += 1) if (adj[members[i]][members[j]]) return false;
    }
    return true;
  }
  function rdIsSolutions(formula, cap) {
    cap = cap === undefined ? 15 : cap;
    var raw = satToIndependentSet(formula);
    var made = { graph: raw.graph, nodes: raw.nodes, k: raw.k, vars: formula.n };
    oracleCap('rdIsSolutions', made.graph.n, cap);
    var adj = dgAdjacency(made.graph), sets = [];
    forEachSubset(made.graph.n, function (mask) {
      if (popcount(mask) !== made.k) return;
      var members = maskMembers(mask, made.graph.n);
      if (!rdIsIndependent(adj, members)) return;
      sets.push(members);
    });
    var solutions = rdSatSolutions(formula, 12);
    var keys = solutions.map(function (s) { return s.key; });
    var map = rdSolutionMap(keys, sets, function (members) {
      return rdAssignKey(rdIsBack(made, members));
    });
    /* the backward construction, from every satisfying assignment */
    var back = solutions.map(function (s) {
      var built = rdIsForward(made, formula, s.assign);
      return { assign: s.assign, key: s.key, members: built.members,
               size: built.members.length, sized: built.members.length === made.k,
               independent: rdIsIndependent(adj, built.members) };
    });
    return { made: made, sets: sets, map: map, back: back, adj: adj,
             backwardWorks: back.every(function (b) { return b.sized && b.independent; }),
             vertices: made.graph.n, edges: made.graph.arcs.length, k: made.k,
             maximum: independentSetBrute(made.graph, made.k, cap).result.size,
             satisfiable: solutions.length > 0, models: solutions.length };
  }

  /* -------------------------------- independent set, cover and clique

     The bijection this kit can check on EVERY subset rather than on the
     optimal ones, which is the point: the identity "S is independent exactly
     when V minus S is a cover" is about all 2^n subsets, and checking it only
     on the optima would check the weakest possible case. */
  function rdIsCover(G, members) {
    var inSet = new Array(G.n).fill(false);
    members.forEach(function (v) { inSet[v] = true; });
    for (var i = 0; i < G.arcs.length; i += 1) {
      var a = G.arcs[i];
      if (a.u !== a.v && !inSet[a.u] && !inSet[a.v]) return false;
    }
    return true;
  }
  function rdIsCliqueIn(adj, members) {
    for (var i = 0; i < members.length; i += 1) {
      for (var j = i + 1; j < members.length; j += 1) if (!adj[members[i]][members[j]]) return false;
    }
    return true;
  }
  function rdComplementCheck(G, cap) {
    cap = cap === undefined ? 12 : cap;
    oracleCap('rdComplementCheck', G.n, cap);
    var H = complementGraph(G);
    var adjG = dgAdjacency(G), adjH = dgAdjacency(H);
    var full = (1 << G.n) - 1;
    var rows = [], independent = 0, covers = 0, cliques = 0;
    var coverMismatch = [], cliqueMismatch = [];
    forEachSubset(G.n, function (mask) {
      var S = maskMembers(mask, G.n), C = maskMembers(full ^ mask, G.n);
      var ind = rdIsIndependent(adjG, S);
      var cov = rdIsCover(G, C);
      var cli = rdIsCliqueIn(adjH, S);
      if (ind) independent += 1;
      if (rdIsCover(G, S)) covers += 1;
      if (cli) cliques += 1;
      if (ind !== cov) coverMismatch.push({ S: S, ind: ind, cov: cov });
      if (ind !== cli) cliqueMismatch.push({ S: S, ind: ind, cli: cli });
      rows.push({ mask: mask, S: S, C: C, independent: ind, complementCovers: cov, clique: cli });
    });
    var bestI = independentSetBrute(G, undefined, 16).result;
    var bestC = vertexCoverBrute(G, 16).result;
    var bestK = cliqueBrute(H, 16).result;
    return { H: H, rows: rows, subsets: rows.length,
             independentCount: independent, coverCount: covers, cliqueCount: cliques,
             coverMismatch: coverMismatch, cliqueMismatch: cliqueMismatch,
             coverBijection: coverMismatch.length === 0,
             cliqueBijection: cliqueMismatch.length === 0,
             countsAgree: independent === cliques && independent === covers,
             alpha: bestI.size, tau: bestC.size, omega: bestK.size,
             maxIndependent: bestI.members, minCover: bestC.members, maxClique: bestK.members,
             identity: bestI.size + bestC.size === G.n,
             cliqueMatches: bestK.size === bestI.size };
  }

  /* ---------------------------------------------- 3-SAT to subset sum

     `satToSubsetSum` builds the digit table: one base-10 column per variable
     and one per clause, two numbers per variable, two slack numbers per
     clause, and a target of 1s and 4s.

     WHY BASE TEN. No column can carry, and the page proves it rather than
     saying it: `rdColumnSums` adds every digit in each column, over EVERY row
     whether or not a solution takes it. A variable column totals 2 -- the two
     rows for that variable -- and a clause column totals at most 6: three
     literal occurrences plus the two slack numbers 1 and 2. Six is less than
     ten, so no column can ever carry into the next and the addition in every
     column is independent of every other. That independence is the whole
     reason the reduction works, and it is the step readers skip.

     THE MAP IS A BIJECTION, and here is why, computed rather than argued: a
     satisfying assignment puts 1, 2 or 3 into a clause column, the column must
     reach 4, and the slack numbers 1 and 2 make up a difference of 3, 2 or 1
     in exactly one way each. */
  function rdColumnSums(made) {
    var sums = new Array(made.columns).fill(0);
    made.rows.forEach(function (r) {
      r.digits.forEach(function (d, i) { sums[i] += d; });
    });
    return { sums: sums, max: sums.reduce(function (a, b) { return Math.max(a, b); }, 0) };
  }
  function rdSubsetSolutions(formula, cap) {
    cap = cap === undefined ? 16 : cap;
    var made = satToSubsetSum(formula);
    oracleCap('rdSubsetSolutions', made.rows.length, cap);
    var hits = [];
    forEachSubset(made.rows.length, function (mask) {
      var members = maskMembers(mask, made.rows.length), sum = 0n;
      members.forEach(function (i) { sum += made.rows[i].value; });
      if (sum === made.target) hits.push(members);
    });
    var solutions = rdSatSolutions(formula, 12);
    var keys = solutions.map(function (s) { return s.key; });
    var map = rdSolutionMap(keys, hits, function (members) {
      return rdAssignKey(rdSubsetBack(made, formula, members));
    });
    var dp = subsetSumDp(made.rows.map(function (r) { return r.value; }), made.target);
    return { made: made, hits: hits, map: map, columns: rdColumnSums(made),
             dp: dp, dpAgrees: dp.result.found === (hits.length > 0),
             solutions: solutions, models: solutions.length,
             rows: made.rows.length, target: made.target };
  }
  /* A subset back to an assignment: the variable rows are the first 2n of
     them, "x_i true" at 2(i-1) and "x_i false" at 2(i-1)+1. A subset that
     took neither or both for some variable is not a solution, and cannot be:
     the variable's own column would then read 0 or 2 rather than 1. */
  function rdSubsetBack(made, formula, members) {
    var assign = [], i;
    for (i = 0; i < formula.n; i += 1) assign.push(false);
    members.forEach(function (idx) {
      if (idx >= 2 * formula.n) return;               /* a slack number */
      if (idx % 2 === 0) assign[idx / 2] = true;
    });
    return assign;
  }

  /* ------------------------------------ Hamilton circuit to travelling
                                          salesman

     Distance 1 on an edge, 2 off it, budget n. A tour of length exactly n uses
     only edges of the graph, so it IS a Hamilton circuit; a tour using any
     non-edge costs at least n + 1. The map on solutions is the IDENTITY on the
     vertex sequence, which makes this the cleanest bijection of the five --
     the two solution sets are literally the same list, and the page checks
     that by comparing them.

     A tour is canonicalised: it starts at vertex 0 and its second vertex is
     smaller than its last, so a cycle and its reverse are one solution rather
     than two. On an undirected graph they are the same circuit, and counting
     them twice would make a bijection look like a two-to-one map. */
  function rdTourKey(tour) {
    return tour.map(function (v) { return v + 1; }).join('-');
  }
  function rdCanonicalTour(tour) {
    if (tour.length < 3) return tour.slice();
    var rev = [tour[0]].concat(tour.slice(1).reverse());
    return tour[1] <= tour[tour.length - 1] ? tour.slice() : rev;
  }
  function rdTourLength(D, tour) {
    var total = 0;
    for (var i = 0; i < tour.length; i += 1) total += D[tour[i]][tour[(i + 1) % tour.length]];
    return total;
  }
  function rdIsCircuit(adj, tour) {
    for (var i = 0; i < tour.length; i += 1) {
      if (!adj[tour[i]][tour[(i + 1) % tour.length]]) return false;
    }
    return true;
  }
  function rdTourSolutions(G, cap) {
    cap = cap === undefined ? 8 : cap;
    oracleCap('rdTourSolutions', G.n, cap);
    var made = tspFromGraph(G), D = made.D, adj = dgAdjacency(G);
    var tours = [], circuits = [], all = [];
    var rest = [], v;
    for (v = 1; v < G.n; v += 1) rest.push(v);
    (function walk(prefix, left) {
      if (!left.length) {
        var tour = [0].concat(prefix);
        if (tour.length > 2 && tour[1] > tour[tour.length - 1]) return;   /* the reverse */
        var len = rdTourLength(D, tour), circ = rdIsCircuit(adj, tour);
        all.push({ tour: tour, key: rdTourKey(tour), length: len, circuit: circ,
                   within: len <= made.budget });
        if (len <= made.budget) tours.push(rdTourKey(tour));
        if (circ) circuits.push(rdTourKey(tour));
        return;
      }
      for (var i = 0; i < left.length; i += 1) {
        walk(prefix.concat([left[i]]), left.slice(0, i).concat(left.slice(i + 1)));
      }
    })([], rest);
    var map = rdSolutionMap(circuits, tours, function (k) { return k; });
    var best = tspBrute(D, made.budget, cap);
    var ham = hamiltonBrute(G, cap);
    return { D: D, budget: made.budget, all: all, tours: tours, circuits: circuits,
             map: map, shortest: best.result.length, bestTour: best.result.tour,
             withinBudget: best.result.withinBudget,
             hasCircuit: ham.result.circuit !== null,
             answersAgree: (best.result.withinBudget === true) === (ham.result.circuit !== null),
             sameList: map.bijection, considered: all.length };
  }

  /* -------------------------------------------------------------- drawing

     A table is the right picture for four of these five modes, so the only
     drawing this kit adds is the one for a graph, and that is DIGRAPH_JS's
     `dgSvg` used as it ships. What is here is the colouring: which vertices
     are in the solution the page is showing. */
  function rdColours(n, members, tone) {
    var out = new Array(n).fill(-1);
    (members || []).forEach(function (v) { out[v] = tone === undefined ? 1 : tone; });
    return out;
  }
  /* The literal vertices of the SAT-to-independent-set graph, laid out one
     clause per column so a clause triangle is drawn as a triangle rather than
     as three chords of one big circle. A gadget the reader cannot see the
     shape of is a gadget they have to take on trust. */
  function rdClausePoints(made) {
    var sizes = {}, pts = [], seen = {};
    made.nodes.forEach(function (node) { sizes[node.clause] = (sizes[node.clause] || 0) + 1; });
    var cols = made.k;
    made.nodes.forEach(function (node) {
      var within = seen[node.clause] === undefined ? 0 : seen[node.clause];
      seen[node.clause] = within + 1;
      var cx = cols <= 1 ? 230 : 66 + (node.clause / (cols - 1)) * 328;
      var size = sizes[node.clause] || 1;
      var ang = -Math.PI / 2 + (2 * Math.PI * within) / size;
      pts.push([cx + 44 * Math.cos(ang), 150 + 66 * Math.sin(ang)]);
    });
    return pts;
  }

  /* The self-reduction as a chain: one box per variable, the two branches the
     oracle was asked about, and the one it allowed. Returns a string and
     touches nothing. */
  function rdChainSvg(steps, satisfiable) {
    var n = steps.length, W = 460, boxW = Math.min(96, (W - 30) / Math.max(1, n) - 8);
    var s = '';
    if (!n) {
      return '<text x="20" y="80" font-size="13" fill="var(--muted)">'
        + (satisfiable ? 'no variables to fix' : 'the first oracle call said NO, so the search stops')
        + '</text>';
    }
    steps.forEach(function (st, i) {
      var x = 20 + i * ((W - 30) / n), y = 26;
      s += '<rect x="' + x.toFixed(1) + '" y="' + y + '" width="' + boxW.toFixed(1)
        + '" height="34" rx="7" fill="var(--panel-3)" stroke="var(--line-strong)" />'
        + '<text x="' + (x + boxW / 2).toFixed(1) + '" y="' + (y + 22)
        + '" text-anchor="middle" font-size="13" font-weight="800" fill="var(--text)">x'
        + st.variable + '</text>';
      [['true', st.ifTrue, 84], ['false', st.ifFalse, 126]].forEach(function (row) {
        var took = (row[0] === 'true') === st.took;
        s += '<rect x="' + x.toFixed(1) + '" y="' + row[2] + '" width="' + boxW.toFixed(1)
          + '" height="30" rx="6" fill="' + (took ? 'var(--cyan)' : 'var(--panel-solid)')
          + '" stroke="' + (row[1] ? 'var(--green)' : 'var(--red)') + '" stroke-width="2" />'
          + '<text x="' + (x + boxW / 2).toFixed(1) + '" y="' + (row[2] + 20)
          + '" text-anchor="middle" font-size="11" font-weight="700" fill="'
          + (took ? 'var(--on-accent)' : (row[1] ? 'var(--green)' : 'var(--red)')) + '">'
          + row[0] + (row[1] ? ' ✓' : ' ✗') + '</text>';
      });
      s += '<line x1="' + (x + boxW / 2).toFixed(1) + '" y1="60" x2="' + (x + boxW / 2).toFixed(1)
        + '" y2="' + (st.took ? 84 : 126) + '" stroke="var(--cyan)" stroke-width="2" />';
      s += '<text x="' + (x + boxW / 2).toFixed(1) + '" y="180" text-anchor="middle" font-size="11"'
        + ' fill="var(--muted)">' + st.clausesAfter + ' left</text>';
    });
    return s;
  }
  function rdDrawChain(el, steps, satisfiable) {
    var out = rdChainSvg(steps, satisfiable);
    if (el) el.innerHTML = out;
    return out;
  }

  /* The column sums of the digit table against the base. Every bar has to sit
     below the line or a column could carry and the reduction would be wrong,
     so this is a drawing of a PROOF OBLIGATION rather than a decoration. */
  function rdColumnSvg(sums, base, labels) {
    var n = sums.length, box = { left: 34, right: 486, base: 176, top: 26 };
    var span = box.base - box.top, W = (box.right - box.left) / Math.max(1, n);
    var maxY = Math.max(base, 1);
    var s = '<line x1="' + box.left + '" y1="' + box.base + '" x2="' + (box.right + 4)
          + '" y2="' + box.base + '" stroke="var(--line-strong)" />';
    sums.forEach(function (v, i) {
      var h = (v / maxY) * span, x = box.left + i * W + W * 0.2;
      s += '<rect x="' + x.toFixed(1) + '" y="' + (box.base - h).toFixed(1) + '" width="'
        + (W * 0.6).toFixed(1) + '" height="' + h.toFixed(1) + '" fill="'
        + (v >= base ? 'var(--red)' : 'var(--cyan)') + '" opacity="0.9" />'
        + '<text x="' + (x + W * 0.3).toFixed(1) + '" y="' + (box.base - h - 4).toFixed(1)
        + '" text-anchor="middle" font-size="11" font-weight="700" fill="var(--text)">' + v + '</text>'
        + '<text x="' + (x + W * 0.3).toFixed(1) + '" y="' + (box.base + 14)
        + '" text-anchor="middle" font-size="10" fill="var(--muted)">'
        + (labels && labels[i] !== undefined ? labels[i] : i + 1) + '</text>';
    });
    s += '<line x1="' + box.left + '" y1="' + box.top + '" x2="' + box.right + '" y2="' + box.top
      + '" stroke="var(--red)" stroke-width="2" stroke-dasharray="6 4" />'
      + '<text x="' + (box.right - 2) + '" y="' + (box.top - 6)
      + '" text-anchor="end" font-size="11" font-weight="700" fill="var(--red)">the base, '
      + base + ' — a column reaching this would carry</text>';
    return s;
  }
  function rdDrawColumns(el, sums, base, labels) {
    var out = rdColumnSvg(sums, base, labels);
    if (el) el.innerHTML = out;
    return out;
  }

  /* The distance matrix, drawn, with the tour's steps filled in. It lives
     here rather than inside the mode for the reason SERIES_JS and dgSvg do:
     a helper closed over an element cannot be called from a test, and this
     one is half of what the travelling-salesman mode is claiming. A step that
     costs 1 is green and a step that costs 2 is red, so "every step is an
     edge" is a colour the reader can check against the graph beside it. */
  function rdMatrixSvg(D, tour) {
    var n = D.length, cell = Math.min(44, 380 / (n + 1)), x0 = 40, y0 = 40, s = '', i, j;
    var onPath = {};
    (tour || []).forEach(function (v, k) {
      var w = tour[(k + 1) % tour.length];
      onPath[v + ',' + w] = true; onPath[w + ',' + v] = true;
    });
    for (i = 0; i < n; i += 1) {
      s += '<text x="' + (x0 - 14) + '" y="' + (y0 + i * cell + cell / 2 + 4)
        + '" text-anchor="middle" font-size="12" font-weight="700" fill="var(--muted)">'
        + (i + 1) + '</text>'
        + '<text x="' + (x0 + i * cell + cell / 2) + '" y="' + (y0 - 8)
        + '" text-anchor="middle" font-size="12" font-weight="700" fill="var(--muted)">'
        + (i + 1) + '</text>';
      for (j = 0; j < n; j += 1) {
        var on = onPath[i + ',' + j], d = D[i][j];
        s += '<rect x="' + (x0 + j * cell) + '" y="' + (y0 + i * cell) + '" width="' + (cell - 2)
          + '" height="' + (cell - 2) + '" fill="'
          + (i === j ? 'var(--panel-3)' : (on ? (d === 1 ? 'var(--green)' : 'var(--red)')
              : 'var(--panel-solid)'))
          + '" stroke="var(--line)" />'
          + '<text x="' + (x0 + j * cell + cell / 2 - 1) + '" y="' + (y0 + i * cell + cell / 2 + 3)
          + '" text-anchor="middle" font-size="12" font-weight="700" fill="'
          + (on ? 'var(--on-accent)' : 'var(--text)') + '">' + d + '</text>';
      }
    }
    return s;
  }
  function rdDrawMatrix(el, D, tour) {
    var out = rdMatrixSvg(D, tour);
    if (el) el.innerHTML = out;
    return out;
  }
"""


# ---------------------------------------------------------------------------
# One core, for once. Every mode here builds a graph or a table and solves
# both sides exhaustively, so all five carry the same four blocks and there is
# nothing to leave out. RATIONAL_JS is absent because there is not a fraction
# in this kit.
# ---------------------------------------------------------------------------

_BASE_JS = COUNT_JS + DIGRAPH_JS + ORACLE_JS + REDUCTION_JS + RDKIT_JS


# ---------------------------------------------------------------------------
# Control furniture. The same shapes the other Algorithms kits use.
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


def _text(cid, label, value, placeholder=None):
    """A text box whose value ships in the markup.

    Nothing this kit's grammars use needs escaping in an attribute: a clause
    is `1 2 -3` and an edge is `1-2`, and neither carries a `>` or a quote.
    flowkit fills its box from the script because a flow arc does carry a `>`,
    which a value attribute cannot hold without an entity that
    scripts/labcheck.js does not decode.
    """
    return (
        '        <div class="field">\n          <label for="%s">%s</label>\n'
        '          <input id="%s" type="text" value="%s" inputmode="text" autocomplete="off"'
        ' placeholder="%s">\n'
        "        </div>\n" % (cid, label, cid, _attr(value), _attr(placeholder or value))
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


def _chosen(presets, cfg):
    want = str(cfg.get("preset", presets[0]["id"]))
    for p in presets:
        if p["id"] == want:
            return p
    raise ValueError(
        "reduction: no preset %r; this mode has %s"
        % (want, ", ".join(p["id"] for p in presets))
    )


# The four parts, spelled once so no mode can quietly ship three of them.
_FOUR_PARTS = (
    "  /* A reduction is a CONSTRUCTION, and every panel below shows all four\n"
    "     parts of it: the instance the reader typed, the transformed instance\n"
    "     built from it, one solution carried back and checked by the original\n"
    "     problem's own rules, and the map between the two full solution sets\n"
    "     with its three properties computed separately. Soundness, surjectivity\n"
    "     and injectivity are three different questions and this kit never\n"
    "     answers them with one word: two of its five reductions are bijections\n"
    "     on solutions and the others are not, and being told which is which is\n"
    "     the part a diagram with an arrow on it cannot give you. */\n"
)


# ---------------------------------------------------------------------------
# selfreduce -- search from decision, in n + 1 questions
# ---------------------------------------------------------------------------

_SR_PRESETS = [
    {
        "id": "three",
        "label": "three variables, four clauses — satisfiable",
        "cnf": "1 2 -3; -1 2 3; 1 -2 3; -1 -2 -3",
        "note": "four oracle calls build an assignment that eight would have been needed to find "
                "by search",
    },
    {
        "id": "forced",
        "label": "a formula with exactly one model",
        "cnf": "1; 2; -3",
        "note": "each question has only one allowed answer, and the trace shows the other branch "
                "being refused",
    },
    {
        "id": "unsat",
        "label": "unsatisfiable — the first call ends it",
        "cnf": "1 2; 1 -2; -1 2; -1 -2",
        "note": "the decision oracle says no once and the search stops without fixing a single "
                "variable",
    },
    {
        "id": "four",
        "label": "four variables, five clauses",
        "cnf": "1 2 -3; -1 3 4; 2 -4 1; -2 -3 -4; 1 -2 4",
        "note": "five calls against sixteen assignments, and the gap doubles with every variable "
                "added",
    },
    {
        "id": "free",
        "label": "a variable no clause mentions",
        "cnf": "1 2; -1 2",
        "note": "x2 is forced and x1 is free, so the oracle allows both branches at x1 and the "
                "reduction takes the first",
    },
]


def _selfreduce(cfg):
    chosen = _chosen(_SR_PRESETS, cfg)
    markup = (
        _toolbar(
            "Search from decision: n + 1 questions build the answer",
            "a yes-or-no oracle, asked once per variable, produces a satisfying assignment",
            [("cyan", "the branch the reduction took"), ("green", "the oracle allowed it"),
             ("red", "the oracle refused it")],
        )
        + _stage(_svg("srPlot", "0 0 480 200",
                      "One column per variable: the two branches the oracle was asked about, "
                      "which it allowed, and which the reduction took."))
        + _table("srSteps")
        + _table("srCheck")
        + _banner("srStatus")
    )
    controls = (
        _select("srPreset", "Worked example", _options(_SR_PRESETS), chosen["id"])
        + _text("srCnf", "Clauses, literals by spaces and clauses by a semicolon", chosen["cnf"])
        + _range("srStep", "Highlight the question asked about this variable", 1, 6, 1)
        + _kpis([("Variables and clauses", "srSize"),
                 ("The decision oracle says", "srDecide"),
                 ("Oracle calls used", "srCalls"),
                 ("Assignments a search would try", "srBrute"),
                 ("The assignment produced", "srFound"),
                 ("It satisfies every clause", "srVerify"),
                 ("Every step agrees with brute force", "srAgree"),
                 ("Models the formula has", "srModels")])
        + _hint(
            "srHint",
            "The oracle answers one question: <em>is this formula satisfiable</em>. It never "
            "returns an assignment. Fix <span class=\"tt\">x1</span> to true, ask again; if the "
            "answer is still yes, keep it, otherwise <span class=\"tt\">x1</span> must be false. "
            "After <span class=\"tt\">n</span> more questions every variable is fixed and what is "
            "left is the assignment. The oracle here is brute force, which is the joke: an "
            "exponential oracle is still an oracle, and what is being shown is the "
            "<em>reduction</em>, not an efficient algorithm.",
        )
    )
    script = _BASE_JS + _FOUR_PARTS + _presets_js("SRP", _SR_PRESETS, ["cnf", "note"]) + r"""
  var presetIn = document.getElementById('srPreset'), cnfIn = document.getElementById('srCnf');
  var stepIn = document.getElementById('srStep'), stepOut = document.getElementById('srStepOut');
  var plot = document.getElementById('srPlot');
  var stepsT = document.getElementById('srSteps'), checkT = document.getElementById('srCheck');
  var status = document.getElementById('srStatus');
  var KPIS = ['srSize', 'srDecide', 'srCalls', 'srBrute', 'srFound', 'srVerify', 'srAgree', 'srModels'];

  function blank(why) {
    plot.innerHTML = ''; stepsT.innerHTML = ''; checkT.innerHTML = '';
    for (var i = 0; i < KPIS.length; i += 1) document.getElementById(KPIS[i]).textContent = '—';
    status.innerHTML = '<span class="tone-red">' + why + '.</span> A clause is '
      + '<span class="tt">1 2 -3</span>, and clauses are separated by a semicolon.';
  }

  function redraw() {
    var parsed = rdParseCnf(cnfIn.value);
    if (parsed.bad) { blank(parsed.bad); return; }
    var F = parsed.formula;
    var trace;
    try { trace = rdSelfTrace(F); }
    catch (e) { if (!rdIsRefusal(e)) throw e; blank(e.message); return; }
    stepIn.max = Math.max(1, F.n);
    /* The label says this highlights the question about one variable, and
       that is all it does. A slider whose label promises more than its code
       delivers is the same defect as a figure that is wrong, and harder to
       see: nothing downstream can tell that the row it lit was not the row
       the caption named. */
    var at = Math.max(1, Math.min(Math.max(1, F.n), parseInt(stepIn.value, 10)));
    stepOut.textContent = trace.steps.length
      ? 'x' + at + ', question ' + at + ' of ' + F.n
      : 'no question was asked: the first oracle call ended it';

    plot.innerHTML = rdChainSvg(trace.steps, trace.satisfiable);

    document.getElementById('srSize').textContent = F.n + ' variables, ' + F.clauses.length + ' clauses';
    document.getElementById('srDecide').textContent = trace.decided ? 'yes, satisfiable' : 'no';
    document.getElementById('srCalls').textContent = trace.calls + ' — n + 1 is '
      + trace.expectedCalls + (trace.calls === trace.expectedCalls ? '' : ' — MISMATCH');
    document.getElementById('srBrute').textContent = String(trace.bruteWork);
    document.getElementById('srFound').textContent = trace.run.result.assignment
      ? rdAssignText(trace.run.result.assignment) : 'none, and there is none';
    document.getElementById('srVerify').textContent = trace.verified === null
      ? 'not applicable' : (trace.verified ? 'yes, checked clause by clause' : 'NO — a defect');
    document.getElementById('srAgree').textContent = trace.everyStepAgrees ? 'yes' : 'NO';
    document.getElementById('srModels').textContent = trace.solutions.length + ' of '
      + trace.bruteWork;

    var head = '<thead><tr><th>question</th><th>formula asked about</th>'
      + '<th>oracle says yes to true</th><th>and to false</th><th>taken</th>'
      + '<th>clauses left</th></tr></thead><tbody>';
    var body = '<tr><td>0</td><td class="tt">' + rdFormulaText(F) + '</td>'
      + '<td colspan="2" class="' + (trace.decided ? 'tone-green">satisfiable' : 'tone-red">not satisfiable')
      + '</td><td>—</td><td>' + F.clauses.length + '</td></tr>';
    trace.steps.forEach(function (st) {
      body += '<tr' + (st.variable === at ? ' class="on"' : '') + '><td>' + st.variable + '</td>'
        + '<td class="tt">' + (st.restricted.clauses.length
            ? rdFormulaText(st.restricted) : 'nothing left — every clause is satisfied') + '</td>'
        + '<td class="' + (st.ifTrue ? 'tone-green">yes' : 'tone-red">no') + '</td>'
        + '<td class="' + (st.ifFalse ? 'tone-green">yes' : 'tone-red">no') + '</td>'
        + '<td class="tone-cyan">x' + st.variable + ' = ' + (st.took ? 'T' : 'F') + '</td>'
        + '<td>' + st.clausesAfter + '</td></tr>';
    });
    stepsT.innerHTML = head + body + '</tbody>';

    checkT.innerHTML = '<thead><tr><th>the check</th><th>what was computed</th><th>verdict</th>'
      + '</tr></thead><tbody>'
      + '<tr><td>the reduction and the oracle agree about the answer</td>'
      + '<td>' + (trace.satisfiable ? 'yes' : 'no') + ' against ' + (trace.decided ? 'yes' : 'no')
      + '</td><td class="' + (trace.agrees ? 'tone-green">agree' : 'tone-red">DISAGREE') + '</td></tr>'
      + '<tr><td>each branch taken is the one brute force allows</td><td>' + trace.steps.length
      + ' steps checked separately</td><td class="'
      + (trace.everyStepAgrees ? 'tone-green">every one' : 'tone-red">NOT every one') + '</td></tr>'
      + '<tr><td>the assignment satisfies every clause</td><td>'
      + (trace.run.result.assignment ? rdAssignText(trace.run.result.assignment) : '—')
      + '</td><td class="' + (trace.verified === null ? 'tone-muted">no assignment to check'
          : (trace.verified ? 'tone-green">verified' : 'tone-red">NOT verified')) + '</td></tr>'
      + '<tr><td>calls used against variables</td><td>' + trace.calls + ' calls for ' + F.n
      + ' variables</td><td class="'
      + (trace.calls === trace.expectedCalls ? 'tone-green">n + 1, as promised'
          : 'tone-red">not n + 1') + '</td></tr>'
      + '<tr><td>what the oracle costs, and why that is beside the point</td>'
      + '<td>each call is a search over ' + trace.bruteWork + ' assignments</td>'
      + '<td class="tone-amber">the reduction is POLYNOMIAL in calls; the oracle is not '
      + 'polynomial in anything, and neither fact affects the other</td></tr></tbody>';

    status.innerHTML = '<strong>' + F.n + ' variables, ' + trace.calls + ' oracle calls, '
      + (trace.satisfiable
          ? 'and the assignment ' + rdAssignText(trace.run.result.assignment) + '.</strong> '
          : 'and no assignment, because there is none.</strong> ')
      + 'This is the one reduction in the kit that does not transform an instance: it transforms a '
      + 'QUESTION. The oracle only ever says yes or no, and asking it n + 1 times produces a '
      + 'witness it never returns. Fix x1 to true and ask again — if the answer is still yes, '
      + 'some model has x1 true and it is safe to commit; if it is no, every model has x1 false '
      + 'and that is safe too. Either way one variable is settled by one question. '
      + (trace.satisfiable
          ? 'The assignment produced is checked against the formula clause by clause and it '
            + (trace.verified ? '<span class="tone-green">satisfies every one</span>'
                : '<span class="tone-red">does not, which is a defect</span>')
            + '. Every branch the reduction took was separately re-asked of brute force and '
            + (trace.everyStepAgrees ? 'all ' + trace.steps.length + ' agree'
                : 'they do NOT all agree') + '. '
          : 'The first call answered no and the search stopped there, which is the right behaviour: '
            + 'there is nothing to build. ')
      + 'The formula has ' + trace.solutions.length + ' '
      + rdPlural(trace.solutions.length, 'model', 'models') + ' among ' + trace.bruteWork
      + ' assignments, and the reduction found one of them with ' + trace.calls
      + ' questions rather than ' + trace.bruteWork + ' guesses — which is the whole content of '
      + '"search reduces to decision", and it does not make either problem easy.';
  }

  function apply() {
    var p = SRP[presetIn.value];
    if (!p) return;
    cnfIn.value = p.cnf; stepIn.value = '1';
    redraw();
  }
  presetIn.addEventListener('change', apply);
  cnfIn.addEventListener('input', redraw);
  stepIn.addEventListener('input', redraw);
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="Search from decision: n + 1 questions build the answer",
        subtitle="The oracle only says yes or no, and asking it once per variable produces a satisfying assignment it never returned",
        markup=markup,
        controls=controls,
        panel_title="Edit the formula and watch a branch be refused",
        panel_intro=(
            "Every restricted formula is re-decided by brute force, separately from the reduction, "
            "and the two answers are required to agree at every step. The assignment at the end is "
            "checked clause by clause rather than assumed &mdash; a reduction that produced a "
            "confident wrong witness would look identical without that check."
        ),
        script=script,
    )


# ---------------------------------------------------------------------------
# independentset -- 3-SAT to independent set: sound, and NOT injective
# ---------------------------------------------------------------------------

_IS_PRESETS = [
    {
        "id": "two",
        "label": "two clauses — six vertices, and a collision",
        "cnf": "1 2 -3; -1 2 3",
        "note": "two independent sets of size 2 map to the same assignment, because a clause with "
                "two true literals can be satisfied by either",
    },
    {
        "id": "three",
        "label": "three clauses — nine vertices, twelve independent sets",
        "cnf": "1 2 -3; -1 2 3; 1 -2 3",
        "note": "every satisfying assignment is the image of at least one independent set here, "
                "and most are the image of several",
    },
    {
        "id": "unsat",
        "label": "unsatisfiable — no independent set reaches m",
        "cnf": "1 2; -1 2; 1 -2; -1 -2",
        "note": "the largest independent set is smaller than the number of clauses, which is the "
                "NO answer arriving on the other side",
    },
    {
        "id": "chain",
        "label": "a forced chain",
        "cnf": "1; -1 2; -2 3",
        "note": "one literal per clause leaves no choice at all, so the map is a bijection on this "
                "formula and on very few others",
    },
    {
        "id": "repeat",
        "label": "a clause that repeats a literal",
        "cnf": "1 1 2; -1 2 3",
        "note": "the triangle still allows only one of the two copies, so the gadget survives a "
                "clause the prose never mentions",
    },
]


def _independentset(cfg):
    chosen = _chosen(_IS_PRESETS, cfg)
    markup = (
        _toolbar(
            "3-SAT to independent set, gadget by gadget",
            "a triangle per clause, an edge between contradictory literals, and k = the number of clauses",
            [("cyan", "in the independent set shown"), ("purple", "a clause triangle"),
             ("red", "a contradictory pair")],
        )
        + _stage(_svg("isPlot", "0 0 460 300",
                      "The constructed graph: one vertex per literal occurrence, arranged as one "
                      "triangle per clause, with the independent set shown highlighted."))
        + _table("isSets")
        + _table("isMap")
        + _banner("isStatus")
    )
    controls = (
        _select("isPreset", "Worked example", _options(_IS_PRESETS), chosen["id"])
        + _text("isCnf", "Clauses, literals by spaces and clauses by a semicolon", chosen["cnf"])
        + _range("isPick", "Which independent set to carry back", 1, 40, 1)
        + _kpis([("The formula", "isSize"),
                 ("The graph built from it", "isGraph"),
                 ("k, which is the clause count", "isK"),
                 ("Independent sets of size k", "isCount"),
                 ("Satisfying assignments", "isModels"),
                 ("Every set maps to a model", "isSound"),
                 ("Every model builds a set", "isBack"),
                 ("Two sets sharing one model", "isInject")])
        + _hint(
            "isHint",
            "One vertex per <em>occurrence</em> of a literal, not per literal. The three vertices "
            "of a clause form a triangle, so an independent set can take at most one from each "
            "clause; an edge joins <span class=\"tt\">x</span> to <span class=\"tt\">¬x</span> "
            "wherever they occur, so it can never take two that contradict. An independent set of "
            "size <span class=\"tt\">k = m</span> therefore takes exactly one true literal from "
            "every clause, and reading those literals off is an assignment.",
        )
    )
    script = _BASE_JS + _FOUR_PARTS + _presets_js("ISP", _IS_PRESETS, ["cnf", "note"]) + r"""
  var presetIn = document.getElementById('isPreset'), cnfIn = document.getElementById('isCnf');
  var pickIn = document.getElementById('isPick'), pickOut = document.getElementById('isPickOut');
  var plot = document.getElementById('isPlot');
  var setsT = document.getElementById('isSets'), mapT = document.getElementById('isMap');
  var status = document.getElementById('isStatus');
  var KPIS = ['isSize', 'isGraph', 'isK', 'isCount', 'isModels', 'isSound', 'isBack', 'isInject'];
  var MAXROWS = 16;

  function blank(why) {
    plot.innerHTML = ''; setsT.innerHTML = ''; mapT.innerHTML = '';
    for (var i = 0; i < KPIS.length; i += 1) document.getElementById(KPIS[i]).textContent = '—';
    status.innerHTML = '<span class="tone-red">' + why + '.</span> A clause is '
      + '<span class="tt">1 2 -3</span>, and clauses are separated by a semicolon.';
  }

  function redraw() {
    var parsed = rdParseCnf(cnfIn.value, 6, 5);
    if (parsed.bad) { blank(parsed.bad); return; }
    var F = parsed.formula;
    var R;
    try { R = rdIsSolutions(F); }
    catch (e) { if (!rdIsRefusal(e)) throw e; blank(e.message); return; }
    var made = R.made, G = made.graph;
    pickIn.max = Math.max(1, R.sets.length);
    var at = R.sets.length ? Math.max(1, Math.min(R.sets.length, parseInt(pickIn.value, 10))) - 1 : -1;
    pickOut.textContent = R.sets.length ? (at + 1) + ' of ' + R.sets.length : 'none exists';

    var shown = at >= 0 ? R.sets[at] : [];
    var back = at >= 0 ? rdIsBack(made, shown) : null;
    var labels = made.nodes.map(function (node) {
      return (node.lit < 0 ? '¬' : '') + 'x' + Math.abs(node.lit);
    });
    plot.innerHTML = dgSvg(G, { points: rdClausePoints(made), label: 'none', labels: labels,
                                colours: rdColours(G.n, shown, 0),
                                highlight: [] });

    document.getElementById('isSize').textContent = F.n + ' variables, ' + F.clauses.length
      + ' clauses';
    document.getElementById('isGraph').textContent = R.vertices + ' vertices, ' + R.edges + ' edges';
    document.getElementById('isK').textContent = String(R.k);
    document.getElementById('isCount').textContent = String(R.sets.length);
    document.getElementById('isModels').textContent = R.models + ' of ' + Math.pow(2, F.n);
    document.getElementById('isSound').textContent = R.map.sound
      ? 'yes, all ' + R.sets.length : 'NO — ' + R.map.unsound.length + ' do not';
    document.getElementById('isBack').textContent = R.backwardWorks
      ? 'yes, all ' + R.models : 'NO — a defect';
    document.getElementById('isInject').textContent = R.map.injective
      ? 'none: the map is injective here'
      : R.map.collisionKeys.length + ' '
        + rdPlural(R.map.collisionKeys.length, 'model is', 'models are') + ' shared';

    var head = '<thead><tr><th>independent set</th><th>literals it takes</th>'
      + '<th>assignment it maps to</th><th>does it satisfy</th></tr></thead><tbody>';
    var body = '';
    R.sets.slice(0, MAXROWS).forEach(function (members, i) {
      var a = rdIsBack(made, members);
      var ok = satEval(F, a) === F.clauses.length;
      body += '<tr' + (i === at ? ' class="on"' : '') + '><td class="tt">' + rdSetText(members)
        + '</td><td class="tt">' + members.map(function (idx) {
            return (made.nodes[idx].lit < 0 ? '¬x' : 'x') + Math.abs(made.nodes[idx].lit);
          }).join(', ')
        + '</td><td class="tt">' + rdAssignText(a) + '</td>'
        + '<td class="' + (ok ? 'tone-green">yes' : 'tone-red">NO') + '</td></tr>';
    });
    if (!R.sets.length) {
      body = '<tr><td colspan="4" class="tone-red">There is no independent set of size ' + R.k
        + ' at all — the largest has ' + R.maximum + ' vertices. That is the NO answer arriving '
        + 'on the other side of the reduction, and the formula is '
        + (R.satisfiable ? 'satisfiable, which would be a DEFECT' : 'indeed unsatisfiable')
        + '.</td></tr>';
    } else if (R.sets.length > MAXROWS) {
      body += '<tr><td colspan="4" class="small-copy">and ' + (R.sets.length - MAXROWS)
        + ' more, all of them checked</td></tr>';
    }
    setsT.innerHTML = head + body + '</tbody>';

    var collisionRow = '';
    if (!R.map.injective) {
      var key = R.map.collisionKeys[0], group = R.map.collisions[key];
      collisionRow = '<tr><td>two different solutions, one image</td>'
        + '<td class="tt">' + group.slice(0, 2).map(rdSetText).join('  and  ') + '</td>'
        + '<td class="tone-amber">both map to ' + key + ', because that clause has two true '
        + 'literals and either one may be picked</td></tr>';
    }
    mapT.innerHTML = '<thead><tr><th>property of the map on solutions</th><th>what was computed</th>'
      + '<th>verdict</th></tr></thead><tbody>'
      + '<tr><td>sound: every independent set of size k is a model</td><td>all '
      + R.sets.length + ' mapped back and re-checked against the formula</td>'
      + '<td class="' + (R.map.sound ? 'tone-green">yes' : 'tone-red">NO') + '</td></tr>'
      + '<tr><td>the reverse construction: every model gives a set of size k</td><td>all '
      + R.models + ' turned into a set by taking each clause&rsquo;s first true literal</td>'
      + '<td class="' + (R.backwardWorks ? 'tone-green">yes' : 'tone-red">NO') + '</td></tr>'
      + '<tr><td>surjective: every model is the image of some set</td><td>'
      + (R.map.originals - R.map.unhit.length) + ' of ' + R.map.originals + ' models hit</td>'
      + '<td class="' + (R.map.surjective ? 'tone-green">yes'
          : 'tone-amber">no, and that is not a fault: the map back leaves a variable no chosen '
            + 'literal mentions at false, so only assignments of that shape are images')
      + '</td></tr>'
      + '<tr><td>injective: no two sets share an image</td><td>' + R.sets.length
      + ' sets over ' + (R.map.originals - R.map.unhit.length) + ' images</td>'
      + '<td class="' + (R.map.injective ? 'tone-green">yes'
          : 'tone-amber">no — and the reduction is still correct') + '</td></tr>'
      + collisionRow
      + '<tr><td>the two answers, computed separately</td>'
      + '<td>largest independent set ' + R.maximum + ' against k = ' + R.k + '; the formula is '
      + (R.satisfiable ? 'satisfiable' : 'unsatisfiable') + '</td>'
      + '<td class="' + ((R.maximum >= R.k) === R.satisfiable ? 'tone-green">agree'
          : 'tone-red">DISAGREE') + '</td></tr></tbody>';

    status.innerHTML = '<strong>' + F.clauses.length + ' clauses become ' + R.vertices
      + ' vertices and ' + R.edges + ' edges, and k is ' + R.k + '.</strong> '
      + 'The construction is on screen rather than described: each clause is a triangle, so at '
      + 'most one of its literals can be chosen, and every contradictory pair is joined, so no two '
      + 'chosen literals disagree. A set of size ' + R.k + ' therefore picks exactly one true '
      + 'literal per clause, which is an assignment. '
      + (R.sets.length
          ? 'There ' + (R.sets.length === 1 ? 'is one such set' : 'are ' + R.sets.length + ' of them')
            + ' and ' + (R.map.sound ? 'every one maps back to an assignment that satisfies the '
              + 'formula' : 'at least one does NOT, which is a defect') + '. '
          : 'There is none — the largest independent set has ' + R.maximum + ' vertices — and the '
            + 'formula is unsatisfiable, so the two answers agree. ')
      + 'The map is <span class="tone-amber">'
      + (R.map.bijection ? 'a bijection on this formula' : 'not a bijection')
      + '</span>, and saying so is the point of the third table. '
      + (R.map.injective ? '' : 'Two different independent sets map to the same assignment '
          + 'whenever a clause has two true literals, because either of them may be picked. ')
      + (R.map.surjective ? '' : 'And some satisfying assignments are the image of no set at all, '
          + 'because the map back leaves any variable the chosen literals never mention at false. ')
      + 'Neither of those is a fault. What a reduction must preserve is the ANSWER, and the last '
      + 'row shows that computed twice: an independent set of size k exists exactly when the '
      + 'formula is satisfiable.';
  }

  function apply() {
    var p = ISP[presetIn.value];
    if (!p) return;
    cnfIn.value = p.cnf; pickIn.value = '1';
    redraw();
  }
  presetIn.addEventListener('change', apply);
  cnfIn.addEventListener('input', redraw);
  pickIn.addEventListener('input', redraw);
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="3-SAT to independent set, gadget by gadget",
        subtitle="A triangle per clause and an edge between contradictory literals — the graph is built here, a set is carried back, and the map is checked in both directions",
        markup=markup,
        controls=controls,
        panel_title="Step through the independent sets and watch two of them give one assignment",
        panel_intro=(
            "Both problems are solved exhaustively: every independent set of size k, and every "
            "satisfying assignment. The map between them is checked for soundness, for surjectivity "
            "and for injectivity separately, because this reduction has the first and not the other "
            "two &mdash; and it is correct anyway."
        ),
        script=script,
    )


# ---------------------------------------------------------------------------
# complement -- one fact three ways, checked on every subset
# ---------------------------------------------------------------------------

_CM_PRESETS = [
    {
        "id": "cycle5",
        "label": "a five-cycle — α = 2, τ = 3",
        "spec": "1-2, 2-3, 3-4, 4-5, 5-1",
        "note": "an odd cycle, where the independent set and the cover are both awkward and the "
                "identity still holds exactly",
    },
    {
        "id": "path4",
        "label": "a path on four vertices",
        "spec": "1-2, 2-3, 3-4",
        "note": "two independent vertices, two in the cover, and the complement is a path's "
                "complement rather than a path",
    },
    {
        "id": "k4",
        "label": "K4 — every pair joined",
        "spec": "1-2, 1-3, 1-4, 2-3, 2-4, 3-4",
        "note": "the complement has no edges at all, so its largest clique is one vertex and so is "
                "the largest independent set here",
    },
    {
        "id": "star",
        "label": "a star — one hub, four leaves",
        "spec": "1-2, 1-3, 1-4, 1-5",
        "note": "the hub alone covers everything, and the four leaves are independent: 4 + 1 = 5",
    },
    {
        "id": "two",
        "label": "two disjoint triangles",
        "spec": "1-2, 2-3, 3-1, 4-5, 5-6, 6-4",
        "note": "the complement joins the two triangles into a complete bipartite graph, and its "
                "largest clique is one vertex from each",
    },
]


def _complement(cfg):
    chosen = _chosen(_CM_PRESETS, cfg)
    markup = (
        _toolbar(
            "Independent set, vertex cover and clique are one problem",
            "S is independent exactly when V minus S covers, and exactly when S is a clique in the complement",
            [("cyan", "the set S"), ("purple", "its complement V minus S"),
             ("green", "the identity holds"), ("red", "it does not")],
        )
        + _stage(_svg("cmPlot", "0 0 460 300",
                      "The graph, with the set S highlighted.")
                 + _svg("cmComp", "0 0 460 300",
                        "The complement graph, with the same set S highlighted — a clique there."))
        + _table("cmSubsets")
        + _table("cmMap")
        + _banner("cmStatus")
    )
    controls = (
        _select("cmPreset", "Worked example", _options(_CM_PRESETS), chosen["id"])
        + _text("cmSpec", "Edges, as u-v", chosen["spec"])
        + _range("cmPick", "Which subset to show", 0, 63, 0)
        + _select("cmShow", "Show in the table",
                  [("independent", "only the independent sets"),
                   ("all", "every subset"),
                   ("optimal", "only the extremes")], "independent")
        + _kpis([("Vertices and edges", "cmSize"),
                 ("Subsets checked", "cmSubsetCount"),
                 ("Independent sets", "cmInd"),
                 ("Vertex covers", "cmCov"),
                 ("Cliques in the complement", "cmCli"),
                 ("α and τ, and α + τ", "cmIdentity"),
                 ("S independent equals V−S covers", "cmBij1"),
                 ("S independent equals S a clique", "cmBij2")])
        + _hint(
            "cmHint",
            "These are the same question asked three ways. If no edge has both ends in "
            "<span class=\"tt\">S</span> then every edge has an end outside it, so "
            "<span class=\"tt\">V−S</span> is a cover; and if no edge of "
            "<span class=\"tt\">G</span> joins two members of <span class=\"tt\">S</span> then "
            "every pair of them is joined in the complement, so <span class=\"tt\">S</span> is a "
            "clique there. Both directions are checked here on <em>every</em> subset, not on the "
            "largest one &mdash; an identity tested only at the optimum is tested at its easiest "
            "case.",
        )
    )
    script = _BASE_JS + _FOUR_PARTS + _presets_js("CMP", _CM_PRESETS, ["spec", "note"]) + r"""
  var presetIn = document.getElementById('cmPreset'), specIn = document.getElementById('cmSpec');
  var pickIn = document.getElementById('cmPick'), pickOut = document.getElementById('cmPickOut');
  var showIn = document.getElementById('cmShow');
  var plot = document.getElementById('cmPlot'), comp = document.getElementById('cmComp');
  var subsetsT = document.getElementById('cmSubsets'), mapT = document.getElementById('cmMap');
  var status = document.getElementById('cmStatus');
  var KPIS = ['cmSize', 'cmSubsetCount', 'cmInd', 'cmCov', 'cmCli', 'cmIdentity', 'cmBij1', 'cmBij2'];
  var MAXROWS = 18;

  function blank(why) {
    plot.innerHTML = ''; comp.innerHTML = ''; subsetsT.innerHTML = ''; mapT.innerHTML = '';
    for (var i = 0; i < KPIS.length; i += 1) document.getElementById(KPIS[i]).textContent = '—';
    status.innerHTML = '<span class="tone-red">' + why + '.</span> An edge is '
      + '<span class="tt">1-2</span>.';
  }

  function redraw() {
    var parsed = rdParseGraph(specIn.value, 10);
    if (parsed.bad) { blank(parsed.bad); return; }
    var G = parsed.G, n = parsed.n;
    var C;
    try { C = rdComplementCheck(G); }
    catch (e) { if (!rdIsRefusal(e)) throw e; blank(e.message); return; }
    pickIn.max = C.subsets - 1;
    var at = Math.max(0, Math.min(C.subsets - 1, parseInt(pickIn.value, 10)));
    var row = C.rows[at];
    pickOut.textContent = rdSetText(row.S) + ' of ' + C.subsets;

    var pts = dgLayout(n, { cx: 230, cy: 150, radius: 108 });
    plot.innerHTML = dgSvg(G, { points: pts, label: 'none',
                                colours: rdColours(n, row.S, 0) });
    comp.innerHTML = C.H.arcs.length
      ? dgSvg(C.H, { points: pts, label: 'none', colours: rdColours(n, row.S, 0) })
      : '<text x="24" y="150" font-size="13" fill="var(--muted)">the complement has no edges at '
        + 'all: every pair of vertices is joined in the original</text>';

    document.getElementById('cmSize').textContent = n + ' vertices, ' + G.arcs.length + ' edges';
    document.getElementById('cmSubsetCount').textContent = String(C.subsets);
    document.getElementById('cmInd').textContent = String(C.independentCount);
    document.getElementById('cmCov').textContent = String(C.coverCount);
    document.getElementById('cmCli').textContent = String(C.cliqueCount);
    document.getElementById('cmIdentity').textContent = C.alpha + ' + ' + C.tau + ' = '
      + (C.alpha + C.tau) + (C.identity ? ', which is n' : ' — NOT n, a defect');
    document.getElementById('cmBij1').textContent = C.coverBijection
      ? 'on all ' + C.subsets + ' subsets' : 'FAILS on ' + C.coverMismatch.length;
    document.getElementById('cmBij2').textContent = C.cliqueBijection
      ? 'on all ' + C.subsets + ' subsets' : 'FAILS on ' + C.cliqueMismatch.length;

    var wanted = C.rows.filter(function (r) {
      if (showIn.value === 'all') return true;
      if (showIn.value === 'independent') return r.independent;
      return r.S.length === C.alpha && r.independent;
    });
    var head = '<thead><tr><th>S</th><th>independent in G</th><th>V − S</th>'
      + '<th>covers G</th><th>clique in the complement</th><th>the three agree</th>'
      + '</tr></thead><tbody>';
    var body = '';
    wanted.slice(0, MAXROWS).forEach(function (r) {
      var agree = r.independent === r.complementCovers && r.independent === r.clique;
      body += '<tr' + (r.mask === at ? ' class="on"' : '') + '><td class="tt">' + rdSetText(r.S)
        + '</td><td class="' + (r.independent ? 'tone-green">yes' : 'tone-muted">no') + '</td>'
        + '<td class="tt">' + rdSetText(r.C) + '</td>'
        + '<td class="' + (r.complementCovers ? 'tone-green">yes' : 'tone-muted">no') + '</td>'
        + '<td class="' + (r.clique ? 'tone-green">yes' : 'tone-muted">no') + '</td>'
        + '<td class="' + (agree ? 'tone-green">yes' : 'tone-red">NO') + '</td></tr>';
    });
    if (wanted.length > MAXROWS) {
      body += '<tr><td colspan="6" class="small-copy">and ' + (wanted.length - MAXROWS)
        + ' more; all ' + C.subsets + ' were checked whatever this filter shows</td></tr>';
    }
    subsetsT.innerHTML = head + body + '</tbody>';

    mapT.innerHTML = '<thead><tr><th>the claim</th><th>what was computed</th><th>verdict</th>'
      + '</tr></thead><tbody>'
      + '<tr><td>S is independent in G ⟺ V − S is a vertex cover of G</td>'
      + '<td>both sides evaluated on all ' + C.subsets + ' subsets</td>'
      + '<td class="' + (C.coverBijection ? 'tone-green">holds every time'
          : 'tone-red">FAILS on ' + C.coverMismatch.length) + '</td></tr>'
      + '<tr><td>S is independent in G ⟺ S is a clique in the complement</td>'
      + '<td>both sides evaluated on all ' + C.subsets + ' subsets</td>'
      + '<td class="' + (C.cliqueBijection ? 'tone-green">holds every time'
          : 'tone-red">FAILS on ' + C.cliqueMismatch.length) + '</td></tr>'
      + '<tr><td>so the three families have the same size</td><td>' + C.independentCount + ', '
      + C.coverCount + ', ' + C.cliqueCount + '</td>'
      + '<td class="' + (C.countsAgree ? 'tone-green">equal' : 'tone-red">NOT equal') + '</td></tr>'
      + '<tr><td>α + τ = n, from the optima found separately</td><td>largest independent '
      + rdSetText(C.maxIndependent) + ' and smallest cover ' + rdSetText(C.minCover) + '</td>'
      + '<td class="' + (C.identity ? 'tone-green">' + C.alpha + ' + ' + C.tau + ' = ' + n
          : 'tone-red">' + (C.alpha + C.tau) + ' is not ' + n) + '</td></tr>'
      + '<tr><td>ω(complement) = α(G), from a third routine</td><td>largest clique in the '
      + 'complement is ' + rdSetText(C.maxClique) + '</td>'
      + '<td class="' + (C.cliqueMatches ? 'tone-green">' + C.omega + ' = ' + C.alpha
          : 'tone-red">' + C.omega + ' is not ' + C.alpha) + '</td></tr>'
      + '<tr><td>the map is a bijection and its inverse is itself</td>'
      + '<td>S ↦ V − S applied twice returns S, on every subset</td>'
      + '<td class="tone-green">an involution, which is the strongest form this takes</td>'
      + '</tr></tbody>';

    status.innerHTML = '<strong>' + C.independentCount + ' independent sets, ' + C.coverCount
      + ' vertex covers, ' + C.cliqueCount + ' cliques in the complement — the same number three '
      + 'times.</strong> '
      + 'It is the same number because it is the same family under two renamings, and the table '
      + 'above checks that on all ' + C.subsets + ' subsets rather than on the largest one. '
      + 'An identity tested only at the optimum is tested at its easiest case: here every subset '
      + 'is a test, and ' + (C.coverBijection && C.cliqueBijection
          ? 'all of them pass' : 'some of them FAIL, which would be a defect') + '. '
      + 'This is the one reduction in the kit that is a bijection in the strongest sense — the map '
      + 'S ↦ V − S is its own inverse, so it is an involution on the subsets and carries '
      + 'independent sets to covers in both directions at once. '
      + 'The consequence is the identity α + τ = n: the largest independent set here is '
      + rdSetText(C.maxIndependent) + ' with ' + C.alpha + ' vertices, the smallest cover is '
      + rdSetText(C.minCover) + ' with ' + C.tau + ', and ' + C.alpha + ' + ' + C.tau + ' = '
      + (C.alpha + C.tau) + '. Those two were found by separate exhaustive searches that share no '
      + 'code, and a third search found the largest clique in the complement at ' + C.omega
      + ' vertices. Three routines, one answer. '
      + 'What follows for hardness is the part worth keeping: an efficient algorithm for any one '
      + 'of the three is an efficient algorithm for all three, because the translation costs a '
      + 'single pass over the vertex set.';
  }

  function apply() {
    var p = CMP[presetIn.value];
    if (!p) return;
    specIn.value = p.spec; pickIn.value = '0';
    redraw();
  }
  presetIn.addEventListener('change', apply);
  specIn.addEventListener('input', redraw);
  pickIn.addEventListener('input', redraw);
  showIn.addEventListener('change', redraw);
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="Independent set, vertex cover and clique are one problem",
        subtitle="S is independent exactly when V − S is a cover, and exactly when S is a clique in the complement — checked on every subset, not only the largest",
        markup=markup,
        controls=controls,
        panel_title="Step through the subsets and watch the three columns move together",
        panel_intro=(
            "The map here is an involution: apply it twice and you are back where you started, so "
            "it is a bijection in the strongest sense the kit contains. The three optima are found "
            "by three separate exhaustive searches, and α + τ = n falls out of them rather than "
            "being asserted."
        ),
        script=script,
    )


# ---------------------------------------------------------------------------
# subsetsum -- 3-SAT to subset sum, and the column that must not carry
# ---------------------------------------------------------------------------

_SS_PRESETS = [
    {
        "id": "two",
        "label": "two variables, two clauses — eight numbers",
        "cnf": "1 2; -1 2",
        "note": "four columns, a target of 1144, and two subsets that reach it",
    },
    {
        "id": "three",
        "label": "three variables, two clauses — the table gets wide fast",
        "cnf": "1 2 -3; -1 2 3",
        "note": "ten numbers of five digits each, and the numbers are exponential in the formula "
                "even though the table is not",
    },
    {
        "id": "forced",
        "label": "one satisfying assignment, one subset",
        "cnf": "1 -2; -1 2; 1 2",
        "note": "a single subset hits the target, and it is the single model read off the digits",
    },
    {
        "id": "unsat",
        "label": "unsatisfiable — nothing reaches the target",
        "cnf": "1 2; 1 -2; -1 2; -1 -2",
        "note": "no subset of the ten numbers adds to the target, which is the NO answer arriving "
                "on the other side",
    },
    {
        "id": "single",
        "label": "one clause — the smallest table there is",
        "cnf": "1 2",
        "note": "six numbers, three columns, and every step of the argument visible at once",
    },
]


def _subsetsum(cfg):
    chosen = _chosen(_SS_PRESETS, cfg)
    markup = (
        _toolbar(
            "3-SAT to subset sum, by the digit table",
            "one column per variable and per clause, and a base big enough that no column can carry",
            [("cyan", "a column total, safely under the base"),
             ("red", "a column that would carry"), ("green", "a row in the subset shown")],
        )
        + _stage(_svg("ssPlot", "0 0 520 200",
                      "The total of every digit in each column, against the base — every bar must "
                      "stay under the line or a column could carry."))
        + _table("ssTable")
        + _table("ssMap")
        + _banner("ssStatus")
    )
    controls = (
        _select("ssPreset", "Worked example", _options(_SS_PRESETS), chosen["id"])
        + _text("ssCnf", "Clauses, literals by spaces and clauses by a semicolon", chosen["cnf"])
        + _range("ssPick", "Which subset to carry back", 1, 40, 1)
        + _kpis([("The formula", "ssSize"),
                 ("Numbers built, and their width", "ssRows"),
                 ("The target", "ssTarget"),
                 ("Subsets that reach it", "ssHits"),
                 ("Satisfying assignments", "ssModels"),
                 ("Largest column total, against the base", "ssColumn"),
                 ("The map on solutions", "ssBij"),
                 ("The dynamic programme agrees", "ssDp")])
        + _hint(
            "ssHint",
            "Each variable contributes two numbers &mdash; <span class=\"tt\">x true</span> and "
            "<span class=\"tt\">x false</span> &mdash; each with a 1 in its own column and a 1 in "
            "every clause column it satisfies. The target has 1 in every variable column, which "
            "forces exactly one of each pair, and 4 in every clause column. A clause with "
            "<span class=\"tt\">k</span> true literals contributes "
            "<span class=\"tt\">k</span> to its column, and its two slack numbers 1 and 2 make up "
            "the difference in exactly one way &mdash; which is why this map is a bijection and "
            "why <span class=\"tt\">k = 0</span> can never be fixed.",
        )
    )
    script = _BASE_JS + _FOUR_PARTS + _presets_js("SSP", _SS_PRESETS, ["cnf", "note"]) + r"""
  var presetIn = document.getElementById('ssPreset'), cnfIn = document.getElementById('ssCnf');
  var pickIn = document.getElementById('ssPick'), pickOut = document.getElementById('ssPickOut');
  var plot = document.getElementById('ssPlot');
  var tableT = document.getElementById('ssTable'), mapT = document.getElementById('ssMap');
  var status = document.getElementById('ssStatus');
  var KPIS = ['ssSize', 'ssRows', 'ssTarget', 'ssHits', 'ssModels', 'ssColumn', 'ssBij', 'ssDp'];

  function blank(why) {
    plot.innerHTML = ''; tableT.innerHTML = ''; mapT.innerHTML = '';
    for (var i = 0; i < KPIS.length; i += 1) document.getElementById(KPIS[i]).textContent = '—';
    status.innerHTML = '<span class="tone-red">' + why + '.</span> A clause is '
      + '<span class="tt">1 2 -3</span>, and clauses are separated by a semicolon.';
  }

  function redraw() {
    var parsed = rdParseCnf(cnfIn.value, 4, 4);
    if (parsed.bad) { blank(parsed.bad); return; }
    var F = parsed.formula;
    var R;
    try { R = rdSubsetSolutions(F); }
    catch (e) { if (!rdIsRefusal(e)) throw e; blank(e.message); return; }
    var made = R.made;
    pickIn.max = Math.max(1, R.hits.length);
    var at = R.hits.length
      ? Math.max(1, Math.min(R.hits.length, parseInt(pickIn.value, 10))) - 1 : -1;
    pickOut.textContent = R.hits.length ? (at + 1) + ' of ' + R.hits.length : 'none exists';
    var shown = at >= 0 ? R.hits[at] : [];
    var inShown = {};
    shown.forEach(function (i) { inShown[i] = true; });

    var labels = [], i;
    for (i = 0; i < F.n; i += 1) labels.push('x' + (i + 1));
    for (i = 0; i < F.clauses.length; i += 1) labels.push('c' + (i + 1));
    plot.innerHTML = rdColumnSvg(R.columns.sums, 10, labels);

    document.getElementById('ssSize').textContent = F.n + ' variables, ' + F.clauses.length
      + ' clauses';
    document.getElementById('ssRows').textContent = R.rows + ' numbers of ' + made.columns
      + ' digits';
    document.getElementById('ssTarget').textContent = String(made.target);
    document.getElementById('ssHits').textContent = String(R.hits.length);
    document.getElementById('ssModels').textContent = R.models + ' of ' + Math.pow(2, F.n);
    document.getElementById('ssColumn').textContent = R.columns.max + ' against the base 10 — '
      + (R.columns.max < 10 ? 'no column can carry' : 'A COLUMN CAN CARRY, which breaks it');
    document.getElementById('ssBij').textContent = R.map.bijection
      ? 'a bijection: sound, surjective and injective'
      : (R.map.sound ? 'sound' : 'NOT SOUND') + ', '
        + (R.map.surjective ? 'surjective' : 'not surjective') + ', '
        + (R.map.injective ? 'injective' : 'not injective');
    document.getElementById('ssDp').textContent = (R.dp.result.found ? 'reaches the target'
      : 'cannot reach it') + (R.dpAgrees ? ' — agrees' : ' — DISAGREES with the enumeration');

    var head = '<thead><tr><th>number</th>';
    var i2;
    for (i2 = 0; i2 < F.n; i2 += 1) head += '<th>x' + (i2 + 1) + '</th>';
    for (i2 = 0; i2 < F.clauses.length; i2 += 1) head += '<th>c' + (i2 + 1) + '</th>';
    head += '<th>value</th><th>in the subset shown</th></tr></thead><tbody>';
    var body = '';
    made.rows.forEach(function (r, idx) {
      body += '<tr' + (inShown[idx] ? ' class="on"' : '') + '><td>' + r.label + '</td>';
      r.digits.forEach(function (d) {
        body += '<td class="' + (d ? 'tone-cyan' : 'tone-muted') + '">' + d + '</td>';
      });
      body += '<td class="tt">' + r.value + '</td><td class="'
        + (inShown[idx] ? 'tone-green">taken' : 'tone-muted">—') + '</td></tr>';
    });
    body += '<tr><td><strong>target</strong></td>';
    made.targetDigits.forEach(function (d) { body += '<td><strong>' + d + '</strong></td>'; });
    body += '<td class="tt"><strong>' + made.target + '</strong></td><td>—</td></tr>';
    body += '<tr><td><strong>every digit in the column</strong></td>';
    R.columns.sums.forEach(function (v) {
      body += '<td class="' + (v < 10 ? 'tone-cyan' : 'tone-red') + '"><strong>' + v
        + '</strong></td>';
    });
    body += '<td colspan="2" class="small-copy">all under 10, so no column can carry into the '
      + 'next and the columns are independent</td></tr>';
    if (shown.length) {
      var sum = 0n;
      shown.forEach(function (k) { sum += made.rows[k].value; });
      body += '<tr><td><strong>the subset shown adds to</strong></td><td colspan="' + made.columns
        + '" class="tt">' + shown.map(function (k) { return made.rows[k].label; }).join(' + ')
        + '</td><td class="tt"><strong>' + sum + '</strong></td><td class="'
        + (sum === made.target ? 'tone-green">hits the target' : 'tone-red">MISSES') + '</td></tr>';
    }
    tableT.innerHTML = head + body + '</tbody>';

    var backAssign = shown.length ? rdSubsetBack(made, F, shown) : null;
    mapT.innerHTML = '<thead><tr><th>property of the map on solutions</th><th>what was computed</th>'
      + '<th>verdict</th></tr></thead><tbody>'
      + '<tr><td>the solution carried back</td><td class="tt">'
      + (backAssign ? rdAssignText(backAssign) + ' — ' + rdFormulaText(F) : 'no subset to carry back')
      + '</td><td class="' + (backAssign
          ? (satEval(F, backAssign) === F.clauses.length ? 'tone-green">satisfies every clause'
              : 'tone-red">DOES NOT satisfy')
          : 'tone-muted">—') + '</td></tr>'
      + '<tr><td>sound: every subset hitting the target is a model</td><td>all ' + R.hits.length
      + ' carried back and re-checked</td><td class="'
      + (R.map.sound ? 'tone-green">yes' : 'tone-red">NO') + '</td></tr>'
      + '<tr><td>surjective: every model is hit</td><td>' + R.models + ' models, '
      + (R.map.originals - R.map.unhit.length) + ' of them hit</td><td class="'
      + (R.map.surjective ? 'tone-green">yes' : 'tone-red">no') + '</td></tr>'
      + '<tr><td>injective: no two subsets share a model</td><td>' + R.hits.length
      + ' subsets over ' + (R.map.originals - R.map.unhit.length) + ' models</td><td class="'
      + (R.map.injective ? 'tone-green">yes — the slack choice is forced'
          : 'tone-red">no') + '</td></tr>'
      + '<tr><td>so the map is</td><td>all three properties</td><td class="'
      + (R.map.bijection ? 'tone-green">a bijection' : 'tone-amber">not a bijection') + '</td></tr>'
      + '<tr><td>a second route to the same yes or no</td>'
      + '<td>the value-indexed dynamic programme reached ' + R.dp.result.reachable
      + ' distinct sums</td><td class="' + (R.dpAgrees ? 'tone-green">agrees with the enumeration'
          : 'tone-red">DISAGREES') + '</td></tr>'
      + '<tr><td>why that dynamic programme is not a polynomial algorithm</td>'
      + '<td>the target is ' + String(made.target).length + ' digits wide and the formula is '
      + (F.n + F.clauses.length) + ' symbols</td>'
      + '<td class="tone-amber">the table is polynomial in the VALUE and the value is exponential '
      + 'in the input length, which is what pseudo-polynomial means</td></tr></tbody>';

    status.innerHTML = '<strong>' + R.rows + ' numbers of ' + made.columns + ' digits, a target of '
      + made.target + ', and ' + R.hits.length + ' '
      + rdPlural(R.hits.length, 'subset that reaches it', 'subsets that reach it') + '.</strong> '
      + 'The construction is the table above and nothing else. Each variable gets two numbers so '
      + 'the target digit 1 in its own column forces exactly one of them; each clause column must '
      + 'reach 4, a satisfying assignment puts 1, 2 or 3 into it, and the slack numbers 1 and 2 '
      + 'make up a difference of 3, 2 or 1 in exactly one way each. A clause with no true literal '
      + 'would need 4 from slack and the slack only adds to 3, which is where an unsatisfying '
      + 'assignment fails. '
      + 'BASE TEN IS DOING WORK. The largest column total over every row is ' + R.columns.max
      + ', which is under 10, so no column can carry into the next and each column is an '
      + 'independent constraint. In base 2 the clause columns would carry and the argument would '
      + 'collapse — that is the step readers skip. '
      + 'The map is <span class="' + (R.map.bijection ? 'tone-green">a bijection'
          : 'tone-amber">not a bijection') + '</span>: '
      + R.hits.length + ' ' + rdPlural(R.hits.length, 'subset', 'subsets') + ' and ' + R.models
      + ' ' + rdPlural(R.models, 'model', 'models') + ', matched one for one. '
      + 'And the numbers are the catch. The dynamic programme that solves subset sum runs in time '
      + 'proportional to the TARGET, which is ' + String(made.target).length + ' digits here and '
      + 'grows by one digit per variable and per clause — exponential in the size of the formula. '
      + 'Subset sum is not easy because a table solves it; the table is as big as the numbers.';
  }

  function apply() {
    var p = SSP[presetIn.value];
    if (!p) return;
    cnfIn.value = p.cnf; pickIn.value = '1';
    redraw();
  }
  presetIn.addEventListener('change', apply);
  cnfIn.addEventListener('input', redraw);
  pickIn.addEventListener('input', redraw);
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="3-SAT to subset sum, by the digit table",
        subtitle="One column per variable and per clause, a target of 1s and 4s, and a base large enough that no column can carry",
        markup=markup,
        controls=controls,
        panel_title="Read the table as the construction, then carry a subset back",
        panel_intro=(
            "The column totals are computed over every row and drawn against the base, because "
            "&ldquo;no column carries&rdquo; is the proof obligation the whole reduction rests on. "
            "Both sides are solved exhaustively and the map between them is checked to be a "
            "bijection &mdash; which this one is, unlike the independent-set reduction."
        ),
        script=script,
    )


# ---------------------------------------------------------------------------
# tsp -- Hamilton circuit to travelling salesman, where the map is the
# identity and the two solution lists are literally the same list
# ---------------------------------------------------------------------------

_TS_PRESETS = [
    {
        "id": "cycle5",
        "label": "a five-cycle — one circuit, one tour within budget",
        "spec": "1-2, 2-3, 3-4, 4-5, 5-1",
        "note": "twelve tours to consider, one of length 5, and it is the cycle itself",
    },
    {
        "id": "chorded",
        "label": "a five-cycle with a chord — the chord changes nothing",
        "spec": "1-2, 2-3, 3-4, 4-5, 5-1, 1-3",
        "note": "an extra edge adds no new Hamilton circuit here, and the tour list does not move "
                "either",
    },
    {
        "id": "path",
        "label": "a path — no circuit, and every tour is over budget",
        "spec": "1-2, 2-3, 3-4",
        "note": "the shortest tour costs 5 against a budget of 4, which is the NO answer arriving "
                "on the other side",
    },
    {
        "id": "k4",
        "label": "K4 — three circuits, three tours",
        "spec": "1-2, 1-3, 1-4, 2-3, 2-4, 3-4",
        "note": "every ordering is a circuit, so the two lists are both the whole list",
    },
    {
        "id": "bowtie",
        "label": "two triangles sharing a vertex — no Hamilton circuit at all",
        "spec": "1-2, 2-3, 3-1, 3-4, 4-5, 5-3",
        "note": "a cut vertex makes a Hamilton circuit impossible, and every tour pays at least "
                "one distance of 2",
    },
]


def _tsp(cfg):
    chosen = _chosen(_TS_PRESETS, cfg)
    markup = (
        _toolbar(
            "Hamilton circuit to travelling salesman",
            "distance 1 on an edge, 2 off it, budget n — and the two solution lists come out identical",
            [("cyan", "the tour shown"), ("green", "within budget, so a circuit"),
             ("red", "a step that is not an edge")],
        )
        + _stage(_svg("tsPlot", "0 0 460 300",
                      "The graph, with the tour shown drawn over it.")
                 + _svg("tsMat", "0 0 460 300",
                        "The distance matrix built from the graph: 1 where there is an edge, 2 "
                        "where there is not."))
        + _table("tsTours")
        + _table("tsMap")
        + _banner("tsStatus")
    )
    controls = (
        _select("tsPreset", "Worked example", _options(_TS_PRESETS), chosen["id"])
        + _text("tsSpec", "Edges, as u-v", chosen["spec"])
        + _range("tsPick", "Which tour to show", 1, 2520, 1)
        + _select("tsFilter", "Show in the table",
                  [("all", "every tour"), ("within", "only the tours within budget"),
                   ("over", "only the tours over budget")], "all")
        + _kpis([("Vertices and edges", "tsSize"),
                 ("Distances built, and the budget", "tsBudget"),
                 ("Tours considered", "tsCount"),
                 ("Tours within budget", "tsWithin"),
                 ("Hamilton circuits", "tsCircuits"),
                 ("The two lists are the same list", "tsSame"),
                 ("Shortest tour there is", "tsShortest"),
                 ("The two answers agree", "tsAgree")])
        + _hint(
            "tsHint",
            "Every pair of cities gets a distance: <span class=\"tt\">1</span> if the graph has "
            "that edge and <span class=\"tt\">2</span> if it does not. A tour visits all "
            "<span class=\"tt\">n</span> cities and returns, so it has "
            "<span class=\"tt\">n</span> steps and costs at least <span class=\"tt\">n</span>; it "
            "costs exactly <span class=\"tt\">n</span> only if every step is an edge, which makes "
            "it a Hamilton circuit. A tour and its reverse are one circuit, so each is listed "
            "once, starting at city 1.",
        )
    )
    script = _BASE_JS + _FOUR_PARTS + _presets_js("TSP2", _TS_PRESETS, ["spec", "note"]) + r"""
  var presetIn = document.getElementById('tsPreset'), specIn = document.getElementById('tsSpec');
  var pickIn = document.getElementById('tsPick'), pickOut = document.getElementById('tsPickOut');
  var filterIn = document.getElementById('tsFilter');
  var plot = document.getElementById('tsPlot'), mat = document.getElementById('tsMat');
  var toursT = document.getElementById('tsTours'), mapT = document.getElementById('tsMap');
  var status = document.getElementById('tsStatus');
  var KPIS = ['tsSize', 'tsBudget', 'tsCount', 'tsWithin', 'tsCircuits', 'tsSame', 'tsShortest',
              'tsAgree'];
  var MAXROWS = 16;

  function blank(why) {
    plot.innerHTML = ''; mat.innerHTML = ''; toursT.innerHTML = ''; mapT.innerHTML = '';
    for (var i = 0; i < KPIS.length; i += 1) document.getElementById(KPIS[i]).textContent = '—';
    status.innerHTML = '<span class="tone-red">' + why + '.</span> An edge is '
      + '<span class="tt">1-2</span>.';
  }

  function redraw() {
    var parsed = rdParseGraph(specIn.value, 8);
    if (parsed.bad) { blank(parsed.bad); return; }
    var G = parsed.G, n = parsed.n;
    var R;
    try { R = rdTourSolutions(G); }
    catch (e) { if (!rdIsRefusal(e)) throw e; blank(e.message); return; }
    pickIn.max = Math.max(1, R.all.length);
    var at = Math.max(1, Math.min(R.all.length, parseInt(pickIn.value, 10))) - 1;
    var shown = R.all[at];
    pickOut.textContent = shown.key + ' of ' + R.all.length;

    var pts = dgLayout(n, { cx: 230, cy: 150, radius: 108 });
    var highlight = [];
    shown.tour.forEach(function (v, k) {
      var w = shown.tour[(k + 1) % shown.tour.length];
      var id = dgFind(G, v, w);
      if (id >= 0) highlight.push(id);
    });
    plot.innerHTML = dgSvg(G, { points: pts, label: 'none', highlight: highlight,
                                colours: rdColours(n, shown.tour, 0) });
    mat.innerHTML = rdMatrixSvg(R.D, shown.tour);

    document.getElementById('tsSize').textContent = n + ' vertices, ' + G.arcs.length + ' edges';
    document.getElementById('tsBudget').textContent = (n * n) + ' distances, budget ' + R.budget;
    document.getElementById('tsCount').textContent = R.all.length + ' — that is (n − 1)!/2';
    document.getElementById('tsWithin').textContent = String(R.tours.length);
    document.getElementById('tsCircuits').textContent = String(R.circuits.length);
    document.getElementById('tsSame').textContent = R.sameList
      ? 'yes, element for element' : 'NO — they differ, which is a defect';
    document.getElementById('tsShortest').textContent = R.shortest + ' against a budget of '
      + R.budget;
    document.getElementById('tsAgree').textContent = R.answersAgree
      ? (R.hasCircuit ? 'both yes' : 'both no') : 'THEY DISAGREE';

    var wanted = R.all.filter(function (t) {
      if (filterIn.value === 'within') return t.within;
      if (filterIn.value === 'over') return !t.within;
      return true;
    });
    var head = '<thead><tr><th>tour</th><th>steps that are edges</th><th>length in D</th>'
      + '<th>within budget ' + R.budget + '</th><th>a Hamilton circuit in G</th>'
      + '<th>the two agree</th></tr></thead><tbody>';
    var body = '';
    wanted.slice(0, MAXROWS).forEach(function (t) {
      var real = 0;
      t.tour.forEach(function (v, k) {
        if (R.D[v][t.tour[(k + 1) % t.tour.length]] === 1) real += 1;
      });
      body += '<tr' + (t.key === shown.key ? ' class="on"' : '') + '><td class="tt">' + t.key
        + '</td><td>' + real + ' of ' + n + '</td><td class="tt">' + t.length + '</td>'
        + '<td class="' + (t.within ? 'tone-green">yes' : 'tone-muted">no') + '</td>'
        + '<td class="' + (t.circuit ? 'tone-green">yes' : 'tone-muted">no') + '</td>'
        + '<td class="' + (t.within === t.circuit ? 'tone-green">yes' : 'tone-red">NO') + '</td></tr>';
    });
    if (wanted.length > MAXROWS) {
      body += '<tr><td colspan="6" class="small-copy">and ' + (wanted.length - MAXROWS)
        + ' more; all ' + R.all.length + ' were checked whatever this filter shows</td></tr>';
    }
    if (!wanted.length) {
      body = '<tr><td colspan="6" class="tone-muted">no tour matches that filter</td></tr>';
    }
    toursT.innerHTML = head + body + '</tbody>';

    mapT.innerHTML = '<thead><tr><th>property of the map on solutions</th><th>what was computed</th>'
      + '<th>verdict</th></tr></thead><tbody>'
      + '<tr><td>the map itself</td><td>a tour is a sequence of cities; a circuit is a sequence of '
      + 'vertices; the map is the identity</td>'
      + '<td class="tone-cyan">nothing is translated, which is what makes this the cleanest case</td></tr>'
      + '<tr><td>sound: every tour within budget is a circuit</td><td>all ' + R.tours.length
      + ' checked edge by edge in G</td><td class="'
      + (R.map.sound ? 'tone-green">yes' : 'tone-red">NO') + '</td></tr>'
      + '<tr><td>surjective: every circuit is a tour within budget</td><td>all '
      + R.circuits.length + ' priced in D</td><td class="'
      + (R.map.surjective ? 'tone-green">yes' : 'tone-red">NO') + '</td></tr>'
      + '<tr><td>injective: distinct tours stay distinct</td><td>' + R.tours.length
      + ' keys, none repeated</td><td class="'
      + (R.map.injective ? 'tone-green">yes' : 'tone-red">NO') + '</td></tr>'
      + '<tr><td>so the map is</td><td>all three properties</td><td class="'
      + (R.map.bijection ? 'tone-green">a bijection' : 'tone-red">not a bijection') + '</td></tr>'
      + '<tr><td>the two answers, computed by separate searches</td>'
      + '<td>the shortest tour is ' + R.shortest + ' against a budget of ' + R.budget
      + '; a Hamilton circuit ' + (R.hasCircuit ? 'exists' : 'does not exist') + '</td>'
      + '<td class="' + (R.answersAgree ? 'tone-green">agree' : 'tone-red">DISAGREE')
      + '</td></tr>'
      + '<tr><td>why 1 and 2 and not 1 and anything</td>'
      + '<td>a tour using one non-edge costs at least ' + (n + 1) + ', which is over the budget '
      + R.budget + '</td>'
      + '<td class="tone-amber">any second distance above 1 would do; 2 is the smallest, and it '
      + 'keeps the instance metric, which matters for the approximation course and not here</td>'
      + '</tr></tbody>';

    status.innerHTML = '<strong>' + R.all.length + ' tours considered, ' + R.tours.length
      + ' within the budget of ' + R.budget + ', and ' + R.circuits.length
      + ' Hamilton ' + rdPlural(R.circuits.length, 'circuit', 'circuits') + ' in the graph.</strong> '
      + (R.sameList
          ? 'Those last two are the SAME LIST, element for element, and that is the whole '
            + 'reduction: the map on solutions is the identity on the sequence of cities, so '
            + 'nothing has to be translated back at all. '
          : '<span class="tone-red">Those two lists differ, which is a defect.</span> ')
      + 'A tour has n steps and every distance is 1 or 2, so a tour costs at least n and costs '
      + 'exactly n only when every step is an edge of the graph — which is what a Hamilton '
      + 'circuit is. One non-edge costs ' + (n + 1) + ' and that is already over budget. '
      + (R.hasCircuit
          ? 'The shortest tour here is ' + R.shortest + ', it meets the budget, and it is '
            + (R.bestTour ? R.bestTour.map(function (v) { return v + 1; }).join('-') : '')
            + '. '
          : 'The shortest tour here is ' + R.shortest + ', which is over the budget of ' + R.budget
            + ', and the graph has no Hamilton circuit — the NO answer travelling across the '
            + 'reduction intact. ')
      + 'Both answers were computed separately, by two searches that share no code, and they '
      + (R.answersAgree ? 'agree' : 'DISAGREE') + '. '
      + 'What this buys is a hardness statement and not an algorithm: the transformation is a '
      + 'double loop over pairs of vertices, so an efficient travelling-salesman algorithm would '
      + 'be an efficient Hamilton-circuit algorithm, and nobody has one.';
  }

  function apply() {
    var p = TSP2[presetIn.value];
    if (!p) return;
    specIn.value = p.spec; pickIn.value = '1';
    redraw();
  }
  presetIn.addEventListener('change', apply);
  specIn.addEventListener('input', redraw);
  pickIn.addEventListener('input', redraw);
  filterIn.addEventListener('change', redraw);
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="Hamilton circuit to travelling salesman",
        subtitle="Distance 1 on an edge and 2 off it, budget n — the tours within budget and the Hamilton circuits come out as the same list",
        markup=markup,
        controls=controls,
        panel_title="Step through the tours and watch the budget do the separating",
        panel_intro=(
            "Every tour is enumerated and priced, and every one is separately checked against the "
            "graph to see whether it is a Hamilton circuit. The two lists are then compared as "
            "lists. This is the one reduction here whose solution map is the identity, which is "
            "what makes it the right first example and a misleading only example."
        ),
        script=script,
    )


# ---------------------------------------------------------------------------
# The dispatch. Unknown raises, and the raise is the contract: a kit that fell
# back to a default would render a finished-looking page carrying another
# lesson's widget, and nothing downstream would notice.
# ---------------------------------------------------------------------------

_MODES = {
    "selfreduce": _selfreduce,
    "independentset": _independentset,
    "complement": _complement,
    "subsetsum": _subsetsum,
    "tsp": _tsp,
}

MODES = tuple(sorted(_MODES))


def reduction_lab(cfg):
    """The reduction course's kit. `cfg["mode"]` chooses the lesson."""
    mode = (cfg or {}).get("mode")
    if mode not in _MODES:
        raise ValueError(
            "reduction_lab: unknown mode %r; the five reduction modes are %s"
            % (mode, ", ".join(MODES))
        )
    return _MODES[mode](cfg or {})


__all__ = ["reduction_lab", "RDKIT_JS", "MODES"]
