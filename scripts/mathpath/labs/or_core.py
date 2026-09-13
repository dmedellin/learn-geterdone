"""The exact engine the Operations Research labs share.

Nine of the twelve kits on this path end in a solved linear program, so the
solver is the subject rather than a utility, and it is exact.

WHY EXACT, stated once.  Every entry of a simplex tableau is an entry of
`B^-1 [A | b]` for `B` the basic columns of the ORIGINAL matrix, and by Cramer's
rule each one is a ratio of two determinants of submatrices of the original
data.  Denominators therefore do not compound from pivot to pivot the way a
naive "divide at every step" reading suggests: they are bounded by the largest
basis determinant, which for lesson-sized integer data is a few digits.  A 4x9
tableau pivoted fifteen times has entries no wider than the ones it started
with.  There is no growth problem here, so there is no reason to round.  The
same argument covers `(I - Q)^-1`, `piP = pi` and every ranging breakpoint: all
of them are solutions of a linear system in the original data.

And exactness here is LOAD BEARING rather than stylistic.  Two of this path's
lessons are about things a float destroys.  Beale's example returns to its
starting tableau after six pivots and the lesson's claim is that the tableau is
IDENTICAL -- a statement about equality of numbers, which a double cannot make
about 1/50 and -1/25.  Klee-Minty's pivot count is 2^n - 1 only because every
degenerate-looking comparison lands exactly; a decimal that rounds one of them
away collapses the count and takes the lesson with it.  Both are written as
named regression tests in scripts/mathcheck.js.

WHAT ROUNDS.  This path has exactly four irrational quantities and this module
owns one of them:

  * the economic order quantity and its cost -- `eoq` returns them as EXACT
    surds `{q, k}` meaning q*sqrt(k), and `surdDec` in ORFMT_JS is the only
    function here that rounds.  It says so, and every page that prints it says
    so.
  * a standard error, `e^-lambda` in a Poisson limit, and the secretary
    problem's n/e are `standardErrorApprox` and `expNegApprox` from
    `sysdesign_core.APPROX_JS` -- borrowed, not re-implemented, so the two
    subjects cannot disagree about them.

`Rfixed`/`Rshort`/`Rpct` round a rational for DISPLAY at a stated number of
places.  They are printers, not arithmetic: nothing downstream reads their
output back in.  And `surdValueCmp` in INV_JS, which compares two costs of the
form `r + q*sqrt(k)`, does NOT round: same radicand is settled by one squaring,
and different radicands by rational brackets refined until they separate, which
is a proof rather than an approximation.

THIRTEEN BLOCKS, not one.  A kit concatenates only the blocks it needs, and
that is the single biggest lever on page weight -- the measured ceiling on this
repository is 62 KB gzipped (AGENTS.md, section "A note on page weight").  All
thirteen concatenated are 52 KB gzipped and no kit takes all thirteen; measured
per kit, the engine share is

    simulate 4.8 KB   markov / birthdeath 5.9   inventory 5.9   dpseq 6.1
    lp 9.4   transport 11.6   simplex 12.2   duality 17.0   network 17.6
    integer 23.2   schedule 27.2

so the two heaviest kits have to be measured as pages before they are believed:
`schedule` leaves about 35 KB for nine modes of drawing, markup and prose.
Re-derive these rather than trusting them; they go stale as the blocks grow.

Every block is a raw string of TOP-LEVEL functions, so
scripts/mathcheck.js executes the SHIPPED source and not a transcription of it,
and so nothing here can close over a DOM element.  (That mistake is why the
existing `drawSeries` and graph `draw` helpers are unreusable outside the file
that defines them.)

WHAT EACH BLOCK NEEDS ABOVE IT.  Everything needs `algebra_core.RATIONAL_JS`
and this module's own `ORFMT_JS`.  Beyond that:

    TABLEAU_JS   nothing more
    PHASE_JS     TABLEAU_JS
    DUAL_JS      TABLEAU_JS, PHASE_JS, algebra_systems.MATRIX_JS
    RANGE_JS     TABLEAU_JS, PHASE_JS, DUAL_JS
    NET_JS       algebra_systems.MATRIX_JS (for submatrixDet's Mdet)
    TRANS_JS     NET_JS (hungarian reads the cover out of bipartiteMatch)
    IP_JS        TABLEAU_JS, PHASE_JS, DUAL_JS, RANGE_JS (addRow, rhsCurve),
                 sysdesign_core.RCEIL_JS
    SCHED_JS     NET_JS (jobShopAll and crash both score by longestPath)
    DPSEQ_JS     algebra_systems.MATRIX_JS, sysdesign_core.HARMONIC_JS
    CHAIN_JS     algebra_systems.MATRIX_JS
    SIM_JS       nothing more
    INV_JS       algebra_core.SURD_JS (Rsurd and quadroots ship there already),
                 sysdesign_core.PMF_JS (pmfConvolve)

A MODEL, the one shape every solver function takes:

    { max: true,                          /* false for a minimisation      */
      names: ['x1', 'x2'],
      obj:  [R, R],                       /* in the ORIGINAL sense         */
      cons: [ { a: [R, R], rel: 'le'|'ge'|'eq', b: R, name: 'labour' } ],
      free: [1] }                         /* indices NOT held >= 0, rare   */
"""

# ---------------------------------------------------------------- printing

ORFMT_JS = r"""
  /* Printing a rational this path can actually produce.

     algebra_core's Rdec and Rnum both go through Number, and this path
     produces rationals Number cannot hold: P^12 on a five-state chain with
     denominator-20 entries has entries of 15 digits over 16 (measured), and
     (19/20)^400 is 512 digits over 521, of which Number() makes NaN.  So
     decimals here are long division in BigInt.  queue.py already solved this for the System
     Design queueing course; this is that solution lifted, not a fourteenth
     one, so the two courses print the same number the same way. */

  /* Decimal by BigInt long division, rounded half up at the last digit. */
  function Rfixed(a, places) {
    if (places === undefined) places = 3;
    var neg = a.n < 0n, n = neg ? -a.n : a.n, d = a.d;
    var scale = 10n ** BigInt(places);
    var q = (2n * n * scale + d) / (2n * d);          /* round half up */
    var whole = q / scale, frac = (q % scale).toString();
    while (frac.length < places) frac = '0' + frac;
    var body = places > 0 ? whole + '.' + frac : String(whole);
    return (neg ? '-' : '') + body;
  }

  /* The exact fraction when a reader can read it, a decimal when the exact
     form has run to twenty digits.  Both are the same number; only one of them
     is evidence.  The cut is on DIGITS, not on magnitude, so it is the same
     rule on every page of the Subject. */
  function Rshort(a, places, digits) {
    if (digits === undefined) digits = 9;
    var wide = String(a.n < 0n ? -a.n : a.n).length > digits || String(a.d).length > digits;
    return wide ? Rfixed(a, places === undefined ? 4 : places) : Rtext(a);
  }
  function Rpct(a, places) {
    return Rfixed(Rmul(a, R(100n, 1n)), places === undefined ? 2 : places) + '%';
  }

  /* The fractional part a - floor(a), EXACT -- which is what makes a Gomory
     cut a cut and not an approximation of one.  The floor is computed inline
     rather than by calling Rfloor, because sysdesign_core.RCEIL_JS declares
     that name and a kit concatenating both blocks would hold two of it. */
  function Rfrac(a) {
    var q = a.n / a.d;
    if (a.n < 0n && q * a.d !== a.n) q -= 1n;
    return Rsub(a, R(q, 1n));
  }

  /* Floor of the integer square root of a BigInt.  algebra_core's bisqrt
     returns null for a non-square, which is right for deciding exactness and
     useless for printing one: this never returns null. */
  function bifloor(n) {
    if (n < 0n) return 0n;
    if (n < 2n) return n;
    var x = n, y = (x + 1n) / 2n;
    while (y < x) { x = y; y = (x + n / x) / 2n; }
    return x;
  }

  /* THE ONE FUNCTION IN THIS MODULE THAT ROUNDS.  A surd {q, k} means
     q*sqrt(k) and is exact; its decimal is not, and an EOQ of 40*sqrt(3) is
     read off a page as 69.28 whatever we would prefer.  The digits come from
     bifloor(q.n^2 * k * 10^(2p)) = floor(q.n * 10^p * sqrt k), computed with
     three guard places and then rounded once, so the printed last digit is the
     correctly rounded one.  Every lesson that calls this says it is rounded. */
  function surdDec(s, places) {
    if (places === undefined) places = 4;
    var p = places + 3;
    var neg = Rsign(s.q) < 0, n = neg ? -s.q.n : s.q.n;
    var floored = bifloor(n * n * s.k * 10n ** BigInt(2 * p));
    var v = R(floored, s.q.d * 10n ** BigInt(p));
    return Rfixed(neg ? Rneg(v) : v, places);
  }
"""


# ------------------------------------------- standard form, pivot, ratio test

TABLEAU_JS = r"""
  /* Construction, pivot and ratio test.

     One internal convention, stated once so no kit has to guess: the solver
     always MAXIMISES.  A minimisation is negated on the way in and `maximised`
     records that it was, so `tabRead(tab).zOrig` is the number the lesson's
     objective actually takes.  Reading `tab.z[ncols]` on a minimisation and
     printing it is the sign error this convention exists to prevent. */

  /* ---- standard form -------------------------------------------------- */

  /* Every constraint becomes an equality with a non-negative right-hand side.
     `kinds[j]` says what each column is and `sentences[j]` says what it
     MEASURES, because "s2 = 7" is not an answer and "seven hours of the
     machine went unused" is. */
  function stdForm(model) {
    var nvar = model.obj.length, m = model.cons.length;
    var given = model.names ? model.names.slice() : [];
    while (given.length < nvar) given.push('x' + (given.length + 1));
    /* A variable the lesson did not hold at >= 0 cannot be a tableau column as
       it stands.  x <= 0 becomes a column for -x, and a FREE x becomes the two
       columns x+ - x-.  `varMap` records the substitution so stdPoint reads the
       reader's variables back out of a solution rather than the solver's.  The
       dual of an equality row is a free variable, so this is not a corner case:
       it is what makes dualModel's output solvable by the same lpSolve. */
    var free = model.free || [], nonpos = model.nonpos || [];
    var varMap = [], vcol = [], names = [], kinds = [], sentences = [], j;
    for (j = 0; j < nvar; j += 1) {
      if (free.indexOf(j) >= 0) {
        varMap.push({ plus: vcol.length, minus: vcol.length + 1, sign: 1, free: true });
        vcol.push({ from: j, sign: 1 }); vcol.push({ from: j, sign: -1 });
        names.push(given[j] + '+'); names.push(given[j] + '-');
        kinds.push('decision'); kinds.push('decision');
        sentences.push(given[j] + ' is free, so it is carried as ' + given[j] + '+ minus ' + given[j] + '-, both >= 0');
        sentences.push('the negative part of ' + given[j]);
      } else if (nonpos.indexOf(j) >= 0) {
        varMap.push({ plus: vcol.length, minus: null, sign: -1, free: false });
        vcol.push({ from: j, sign: -1 });
        names.push('-' + given[j]); kinds.push('decision');
        sentences.push(given[j] + ' is held at <= 0, so the column carries -' + given[j] + ' >= 0');
      } else {
        varMap.push({ plus: vcol.length, minus: null, sign: 1, free: false });
        vcol.push({ from: j, sign: 1 });
        names.push(given[j]); kinds.push('decision');
        sentences.push('how much ' + given[j] + ' the plan does');
      }
    }
    var nd = vcol.length;
    /* Rows first: flip any row whose right-hand side is negative, so that the
       slack basis is feasible whenever there is one.  rowSign remembers the
       flip, because a sensitivity range quoted in flipped units is wrong. */
    var rows = [], b = [], rels = [], rowSign = [], i;
    for (i = 0; i < m; i += 1) {
      var k = model.cons[i], rb = k.b, rel = k.rel || 'le', flip = Rsign(rb) < 0;
      var a = vcol.map(function (v) {
        var e = k.a[v.from];
        if (v.sign < 0) e = Rneg(e);
        return flip ? Rneg(e) : e;
      });
      if (flip) {
        rb = Rneg(rb);
        rel = rel === 'le' ? 'ge' : (rel === 'ge' ? 'le' : 'eq');
        rowSign.push(-1);
      } else rowSign.push(1);
      rows.push(a); b.push(rb); rels.push(rel);
    }
    /* Then the added columns, in row order, so a reader reads x1 x2 s1 e2 a2
       down the header and can see which row each one came from. */
    var extra = [], identity = [], rowSlack = [];
    for (i = 0; i < m; i += 1) {
      var label = model.cons[i].name || ('row ' + (i + 1));
      if (rels[i] === 'le') {
        rowSlack.push(nd + extra.length);
        identity.push(nd + extra.length);
        extra.push({ row: i, sign: 1, kind: 'slack', name: 's' + (i + 1),
                     text: 'the part of ' + label + ' left unused' });
      } else if (rels[i] === 'ge') {
        rowSlack.push(nd + extra.length);
        extra.push({ row: i, sign: -1, kind: 'surplus', name: 'e' + (i + 1),
                     text: 'how far ' + label + ' is exceeded' });
        identity.push(nd + extra.length);
        extra.push({ row: i, sign: 1, kind: 'artificial', name: 'a' + (i + 1),
                     text: 'how far ' + label + ' is from being satisfiable at all; it must reach 0' });
      } else {
        rowSlack.push(-1);
        identity.push(nd + extra.length);
        extra.push({ row: i, sign: 1, kind: 'artificial', name: 'a' + (i + 1),
                     text: 'how far ' + label + ' is from holding; it must reach 0' });
      }
    }
    var ncols = nd + extra.length;
    var A = [];
    for (i = 0; i < m; i += 1) {
      var r = rows[i].slice();
      for (j = 0; j < extra.length; j += 1) {
        r.push(extra[j].row === i ? R(BigInt(extra[j].sign), 1n) : R0);
      }
      A.push(r);
    }
    for (j = 0; j < extra.length; j += 1) {
      names.push(extra[j].name); kinds.push(extra[j].kind); sentences.push(extra[j].text);
    }
    /* The objective, twice: as the lesson wrote it, and in the max form the
       tableau uses. */
    var cOrig = [], c = [];
    for (j = 0; j < ncols; j += 1) {
      var v = j < nd ? (vcol[j].sign < 0 ? Rneg(model.obj[vcol[j].from]) : model.obj[vcol[j].from]) : R0;
      cOrig.push(v);
      c.push(model.max === false ? Rneg(v) : v);
    }
    return { A: A, b: b, c: c, cOrig: cOrig, names: names, kinds: kinds,
             sentences: sentences, maximised: model.max !== false,
             identity: identity, rowSlack: rowSlack, rowSign: rowSign,
             rels: rels, m: m, n: ncols, nd: nd, nvar: nvar, varMap: varMap,
             given: given, model: model };
  }

  /* The reader's variables, read back out of a standard-form solution. */
  function stdPoint(std, x) {
    return std.varMap.map(function (v) {
      var val = v.sign < 0 ? Rneg(x[v.plus]) : x[v.plus];
      return v.minus === null ? val : Rsub(val, x[v.minus]);
    });
  }

  /* The value the LESSON's objective takes, given the internal max value. */
  function zOriginal(std, z) { return std.maximised ? z : Rneg(z); }

  /* ---- the tableau ---------------------------------------------------- */

  /* `T` is the body: m rows of ncols + 1 rationals, the last entry the
     right-hand side.  `z` is the objective row, ncols + 1 long, entry j being
     the reduced cost z_j - c_j and the last entry the objective value.
     `basis[i]` is the column basic in row i.

     `forbid[j]` keeps the artificial columns out of Phase II without deleting
     them, which matters: their columns ARE B^-1 whenever the row began with a
     >= or an =, and dualVector and rhsRange read B^-1 out of exactly there. */
  function tabInit(std, costs) {
    var c = costs || std.c, i, j;
    var T = [], basis = std.identity.slice();
    for (i = 0; i < std.m; i += 1) T.push(std.A[i].slice().concat([std.b[i]]));
    var forbid = [];
    for (j = 0; j < std.n; j += 1) forbid.push(std.kinds[j] === 'artificial' && !costs);
    var tab = { T: T, z: [], basis: basis, names: std.names, kinds: std.kinds,
                c: c, cOrig: std.cOrig, identity: std.identity.slice(),
                rowSlack: std.rowSlack, rowSign: std.rowSign, forbid: forbid,
                m: std.m, n: std.n, nd: std.nd, maximised: std.maximised, std: std };
    tabCost(tab, c);
    return tab;
  }

  /* Rebuild the objective row from the basis that is there.  Phase II calls
     this on Phase I's final tableau, which is the whole of "the artificials
     did their job and are now dead weight". */
  function tabCost(tab, c) {
    tab.c = c;
    var row = [], j, i;
    for (j = 0; j <= tab.n; j += 1) {
      var s = R0;
      for (i = 0; i < tab.m; i += 1) s = Radd(s, Rmul(c[tab.basis[i]], tab.T[i][j]));
      row.push(j < tab.n ? Rsub(s, c[j]) : s);
    }
    tab.z = row;
    return tab;
  }

  function tabCopy(tab) {
    return { T: tab.T.map(function (r) { return r.slice(); }), z: tab.z.slice(),
             basis: tab.basis.slice(), names: tab.names, kinds: tab.kinds,
             c: tab.c, cOrig: tab.cOrig, identity: tab.identity, rowSlack: tab.rowSlack,
             rowSign: tab.rowSign, forbid: tab.forbid.slice(), m: tab.m, n: tab.n,
             nd: tab.nd, maximised: tab.maximised, std: tab.std };
  }
  /* The body and the objective row as ONE matrix, which is what Mtable and
     Mtrace from algebra_systems.MATRIX_JS already know how to print. */
  function tabMatrix(tab) {
    return tab.T.map(function (r) { return r.slice(); }).concat([tab.z.slice()]);
  }

  /* The basic feasible solution this tableau stands for. */
  function tabRead(tab) {
    var x = [], j, i;
    for (j = 0; j < tab.n; j += 1) x.push(R0);
    var degenerate = false, zeros = [];
    for (i = 0; i < tab.m; i += 1) {
      x[tab.basis[i]] = tab.T[i][tab.n];
      if (Rzero(tab.T[i][tab.n])) { degenerate = true; zeros.push(i); }
    }
    var tightRows = [];
    for (i = 0; i < tab.m; i += 1) {
      var s = tab.rowSlack[i];
      if (s < 0 || Rzero(x[s])) tightRows.push(i);
    }
    var z = tab.z[tab.n];
    return { x: x, z: z, zOrig: tab.maximised ? z : Rneg(z), basis: tab.basis.slice(),
             reduced: tab.z.slice(0, tab.n), degenerate: degenerate,
             degenerateRows: zeros, tightRows: tightRows,
             values: tab.basis.map(function (b, k) { return { col: b, name: tab.names[b], value: tab.T[k][tab.n] }; }) };
  }

  /* ---- the two rules that are the lesson ------------------------------- */

  /* THE TIE-BREAK IS LESSON CONTENT AND IS CHOSEN HERE, NOT BY ACCIDENT.
       dantzig          most negative z_j - c_j, ties by LOWEST column index
       bland            the SMALLEST index with z_j - c_j < 0, no tie possible
       bestImprovement  largest rate * step = the largest actual change in z
       lastIndex        the largest index with z_j - c_j < 0
     Under dantzig (with tabRatio's lowest-row tie-break) Beale's example
     cycles; under bland it terminates.  That contrast is C2 L7.

     There is NO steepest-edge rule on this path: it scores a column by its
     norm, which is a square root, and nothing here rounds that a ratio test
     can decide.  bestImprovement is exact -- both factors are rationals -- and
     it is what C2 L4's "rate * step = dz" panel compares against Dantzig. */
  function tabEnter(tab, rule) {
    rule = rule || 'dantzig';
    var rates = [], j;
    for (j = 0; j < tab.n; j += 1) {
      var basic = tab.basis.indexOf(j) >= 0;
      var red = tab.z[j];
      var eligible = !basic && !tab.forbid[j] && Rsign(red) < 0;
      var entry = { j: j, name: tab.names[j], reduced: red, rate: Rneg(red),
                    basic: basic, eligible: eligible, step: null, delta: null,
                    unbounded: false };
      if (eligible) {
        var rt = tabRatio(tab, j, rule);
        if (rt.unbounded) { entry.unbounded = true; entry.delta = null; }
        else {
          entry.step = rt.rows[rt.leave].ratio;
          entry.delta = Rmul(entry.rate, entry.step);
        }
      }
      rates.push(entry);
    }
    var pick = -1, why = '', k;
    if (rule === 'bland') {
      for (j = 0; j < tab.n; j += 1) if (rates[j].eligible) { pick = j; break; }
      why = pick < 0 ? 'no column has a negative reduced cost, so this basis is optimal'
        : 'Bland: the smallest-index column with a negative reduced cost is ' + tab.names[pick];
    } else if (rule === 'lastIndex') {
      for (j = tab.n - 1; j >= 0; j -= 1) if (rates[j].eligible) { pick = j; break; }
      why = pick < 0 ? 'no column has a negative reduced cost, so this basis is optimal'
        : 'last index: the largest-index column with a negative reduced cost is ' + tab.names[pick];
    } else if (rule === 'bestImprovement') {
      for (j = 0; j < tab.n; j += 1) {
        if (!rates[j].eligible) continue;
        if (rates[j].unbounded) { pick = j; break; }
        if (pick < 0 || Rcmp(rates[j].delta, rates[pick].delta) > 0) pick = j;
      }
      why = pick < 0 ? 'no column has a negative reduced cost, so this basis is optimal'
        : (rates[pick].unbounded
           ? 'best improvement: ' + tab.names[pick] + ' improves z without limit'
           : 'best improvement: ' + tab.names[pick] + ' moves z by rate ' + Rtext(rates[pick].rate)
             + ' times step ' + Rtext(rates[pick].step) + ' = ' + Rtext(rates[pick].delta)
             + ', the largest actual change on offer');
    } else {
      for (j = 0; j < tab.n; j += 1) {
        if (!rates[j].eligible) continue;
        if (pick < 0 || Rcmp(rates[j].reduced, rates[pick].reduced) < 0) pick = j;
      }
      why = pick < 0 ? 'no column has a negative reduced cost, so this basis is optimal'
        : 'Dantzig: ' + tab.names[pick] + ' has the most negative reduced cost, '
          + Rtext(rates[pick].reduced) + ' (ties go to the lowest column index)';
    }
    return { enter: pick, rates: rates, why: why, rule: rule };
  }

  /* The ratio test on column k.  Ties on the minimum ratio go to the LOWEST
     ROW INDEX under every rule but bland, which breaks them by the smallest
     index of the LEAVING BASIC VARIABLE -- the second half of Bland's rule,
     and the half a textbook usually forgets to state. */
  function tabRatio(tab, k, rule) {
    var rows = [], i, best = null;
    for (i = 0; i < tab.m; i += 1) {
      var a = tab.T[i][k], bi = tab.T[i][tab.n], eligible = Rsign(a) > 0;
      var ratio = eligible ? Rdiv(bi, a) : null;
      rows.push({ i: i, b: bi, a: a, ratio: ratio, eligible: eligible,
                  leaving: tab.basis[i], name: tab.names[tab.basis[i]],
                  why: eligible
                    ? Rtext(bi) + ' / ' + Rtext(a) + ' = ' + Rtext(ratio)
                      + ', the most ' + tab.names[k] + ' can grow before ' + tab.names[tab.basis[i]] + ' hits 0'
                    : (Rzero(a) ? tab.names[k] + ' does not appear in this row, so it never binds'
                       : 'the entry is ' + Rtext(a) + ' < 0, so ' + tab.names[tab.basis[i]]
                         + ' GROWS as ' + tab.names[k] + ' does and never binds') });
      if (eligible && (best === null || Rcmp(ratio, best) < 0)) best = ratio;
    }
    if (best === null) {
      var ray = [];
      for (i = 0; i < tab.n; i += 1) ray.push(R0);
      ray[k] = R1;
      for (i = 0; i < tab.m; i += 1) ray[tab.basis[i]] = Rneg(tab.T[i][k]);
      return { rows: rows, leave: -1, tie: [], unbounded: true, ray: ray, min: null };
    }
    var tie = [];
    for (i = 0; i < tab.m; i += 1) if (rows[i].eligible && Requ(rows[i].ratio, best)) tie.push(i);
    var leave = tie[0];
    if (rule === 'bland') {
      for (i = 0; i < tie.length; i += 1) if (tab.basis[tie[i]] < tab.basis[leave]) leave = tie[i];
    }
    return { rows: rows, leave: leave, tie: tie, unbounded: false, ray: null, min: best };
  }

  /* ---- the pivot ------------------------------------------------------- */

  /* `ops` comes back in exactly the shape algebra_systems.Mrref returns --
     {op, why, after} -- so a reader moving from Gaussian elimination to a
     tableau reads the same trace, printed by the same Mtrace. */
  function tabPivot(tab, r, k) {
    var out = tabCopy(tab), ops = [], i;
    var p = out.T[r][k];
    if (Rzero(p)) throw new Error('cannot pivot on a zero entry');
    var label = function (i2) { return i2 < out.m ? 'R' + (i2 + 1) : 'z'; };
    if (!Requ(p, R1)) {
      var s = Rinv(p);
      out.T[r] = out.T[r].map(function (v) { return Rmul(v, s); });
      ops.push({ op: 'R' + (r + 1) + ' -&gt; ' + Rterm(s) + 'R' + (r + 1),
                 why: 'divides the pivot row by ' + Rtext(p) + ', which makes the pivot 1',
                 after: tabMatrix(out) });
    }
    for (i = 0; i < out.m; i += 1) {
      if (i === r || Rzero(out.T[i][k])) continue;
      var mlt = Rneg(out.T[i][k]);
      out.T[i] = out.T[i].map(function (v, cc) { return Radd(v, Rmul(mlt, out.T[r][cc])); });
      ops.push({ op: label(i) + ' -&gt; ' + label(i) + ' + ' + Rterm(mlt) + 'R' + (r + 1),
                 why: 'clears ' + out.names[k] + ' out of row ' + (i + 1),
                 after: tabMatrix(out) });
    }
    if (!Rzero(out.z[k])) {
      var mz = Rneg(out.z[k]);
      out.z = out.z.map(function (v, cc) { return Radd(v, Rmul(mz, out.T[r][cc])); });
      ops.push({ op: 'z -&gt; z + ' + Rterm(mz) + 'R' + (r + 1),
                 why: 'clears ' + out.names[k] + ' out of the objective row, which is what moves z',
                 after: tabMatrix(out) });
    }
    out.basis[r] = k;
    out.ops = ops;
    out.entered = k;
    out.left = tab.basis[r];
    out.pivotRow = r;
    return out;
  }
"""


# ------------------------------- Phase I, the certificate, and the driver

PHASE_JS = r"""
  /* Phase I, the infeasibility certificate, and the driver that runs pivots
     until something stops it.  Needs TABLEAU_JS above it. */

  /* A basis is a SET of columns, so the signature sorts.  Two tableaux with
     the same basic columns in a different row order stand for the same basic
     solution, and cycling is a statement about the solution returning. */
  function basisKey(basis) {
    return basis.slice().sort(function (a, b) { return a - b; }).join(',');
  }
  /* The index at which a basis first repeats, or -1.  `bases` is the list
     simplexRun collects, one entry per tableau including the starting one. */
  function cycleIndex(bases) {
    var seen = {}, i;
    for (i = 0; i < bases.length; i += 1) {
      var k = basisKey(bases[i]);
      if (seen[k] !== undefined) return i;
      seen[k] = i;
    }
    return -1;
  }

  /* THE DRIVER.  status is one of optimal | unbounded | cycled | limit.

     It must detect a repeated BASIS and stop with `cycled`, not run out at
     opts.maxPivots.  A lab that reports "limit reached" where the lesson says
     "it returned to where it started" has taught the wrong thing -- and the
     difference is visible only because the tableau comparison is exact. */
  function simplexRun(tab, opts) {
    opts = opts || {};
    var rule = opts.rule || 'dantzig';
    var maxPivots = opts.maxPivots === undefined ? 200 : opts.maxPivots;
    var cur = tabCopy(tab), path = [cur], bases = [cur.basis.slice()], steps = [];
    var seen = {}, status = 'optimal', ray = null, cycle = null;
    seen[basisKey(cur.basis)] = 0;
    while (true) {
      var e = tabEnter(cur, rule);
      if (e.enter < 0) { status = 'optimal'; break; }
      var rt = tabRatio(cur, e.enter, rule);
      if (rt.unbounded) { status = 'unbounded'; ray = rt.ray; break; }
      var before = cur;
      cur = tabPivot(cur, rt.leave, e.enter);
      steps.push({ enter: e.enter, enterName: cur.names[e.enter], leave: cur.left,
                   leaveName: cur.names[cur.left], row: rt.leave, rule: rule,
                   whyEnter: e.why, whyLeave: rt.rows[rt.leave].why,
                   rates: e.rates, ratio: rt, ops: cur.ops,
                   zBefore: before.z[before.n], zAfter: cur.z[cur.n],
                   delta: Rsub(cur.z[cur.n], before.z[before.n]) });
      path.push(cur); bases.push(cur.basis.slice());
      var key = basisKey(cur.basis);
      if (seen[key] !== undefined) {
        status = 'cycled';
        cycle = { at: path.length - 1, from: seen[key] };
        break;
      }
      seen[key] = path.length - 1;
      if (steps.length >= maxPivots) { status = 'limit'; break; }
    }
    var z = cur.z[cur.n];
    return { path: path, bases: bases, steps: steps, pivots: steps.length,
             status: status, ray: ray, cycle: cycle, tab: cur, z: z,
             zOrig: cur.maximised ? z : Rneg(z) };
  }

  /* ---- Phase I --------------------------------------------------------- */

  /* Minimise the sum of the artificials.  `feasible` is value === 0 -- not
     "value is small", which is the sentence exactness removes from the page.

     Bland's rule here, not Dantzig's: Phase I is machinery rather than lesson
     content, and Bland is the rule that provably cannot cycle. */
  function phaseOne(std, opts) {
    opts = opts || {};
    var arts = [], j;
    for (j = 0; j < std.n; j += 1) if (std.kinds[j] === 'artificial') arts.push(j);
    if (!arts.length) {
      return { T: tabInit(std), value: R0, feasible: true, artificialsAtZero: [],
               needed: false, redundant: [], run: null,
               why: 'every row is a <= with a non-negative right-hand side, so the slack basis is already feasible and there is no Phase I to run' };
    }
    var w = [];
    for (j = 0; j < std.n; j += 1) w.push(std.kinds[j] === 'artificial' ? R(-1n, 1n) : R0);
    var run = simplexRun(tabInit(std, w), { rule: opts.rule || 'bland', maxPivots: opts.maxPivots || 300 });
    var T = run.tab;
    var value = Rneg(T.z[T.n]);                 /* we maximised -sum, so flip */
    var feasible = Rzero(value);
    /* An artificial left basic at zero is not an obstruction, but it must come
       out before Phase II or the basis is not a basis of the real problem.
       When no real column can replace it, that row is REDUNDANT -- it is a
       combination of the others -- and saying so is better than hiding it. */
    var atZero = [], redundant = [], i, k;
    if (feasible) {
      for (i = 0; i < T.m; i += 1) {
        if (std.kinds[T.basis[i]] !== 'artificial') continue;
        atZero.push({ row: i, col: T.basis[i], name: T.names[T.basis[i]] });
        var swap = -1;
        for (k = 0; k < T.n; k += 1) {
          if (std.kinds[k] === 'artificial' || T.basis.indexOf(k) >= 0) continue;
          if (!Rzero(T.T[i][k])) { swap = k; break; }
        }
        if (swap < 0) redundant.push(i);
        else T = tabPivot(T, i, swap);
      }
    }
    return { T: T, value: value, feasible: feasible, artificialsAtZero: atZero,
             needed: true, redundant: redundant, run: run, artificials: arts,
             why: feasible
               ? 'the artificials can all be driven to zero, so the original constraints have a common solution'
               : 'the artificials cannot be driven below ' + Rtext(value)
                 + ', so no point satisfies every constraint at once' };
  }

  /* Phase II: keep Phase I's tableau, restore the real objective, and lock the
     artificial columns out.  The columns stay because they ARE B^-1 wherever a
     row began as a >= or an =, and dualVector reads B^-1 out of exactly there. */
  function phaseTwo(std, ph1) {
    var T = tabCopy(ph1.T), j;
    for (j = 0; j < std.n; j += 1) T.forbid[j] = std.kinds[j] === 'artificial';
    tabCost(T, std.c);
    return T;
  }

  /* THE INFEASIBILITY CERTIFICATE.  When Phase I stops positive, its final
     objective row holds a y with y'A <= 0 and y'b > 0 -- a proof, by Farkas,
     that no x can satisfy the constraints, and the reason a lab can say "there
     is none" rather than "I did not find one".

     Where y comes from: the Phase I costs are 0 on real columns and -1 on
     artificials, so for the column that started as e_i the objective entry is
     y_i on a slack and y_i + 1 on an artificial.  Negating gives the
     certificate in the direction Farkas states it.  The per-row arithmetic
     comes back in `checks` so the page can SHOW the verification rather than
     assert it. */
  function farkasCertificate(T) {
    var std = T.std, m = std.m, i, j;
    var y = [];
    for (i = 0; i < m; i += 1) {
      var col = std.identity[i];
      var raw = T.z[col];
      y.push(std.kinds[col] === 'artificial' ? Rsub(R1, raw) : Rneg(raw));
    }
    var columns = [];
    for (j = 0; j < std.n; j += 1) {
      if (std.kinds[j] === 'artificial') continue;
      var s = R0, parts = [];
      for (i = 0; i < m; i += 1) {
        s = Radd(s, Rmul(y[i], std.A[i][j]));
        parts.push('(' + Rtext(y[i]) + ')(' + Rtext(std.A[i][j]) + ')');
      }
      columns.push({ j: j, name: std.names[j], value: s, ok: Rsign(s) <= 0,
                     text: parts.join(' + ') + ' = ' + Rtext(s) + ' &lt;= 0' });
    }
    var bs = R0, bparts = [];
    for (i = 0; i < m; i += 1) {
      bs = Radd(bs, Rmul(y[i], std.b[i]));
      bparts.push('(' + Rtext(y[i]) + ')(' + Rtext(std.b[i]) + ')');
    }
    var allCols = columns.every(function (c) { return c.ok; });
    return { y: y, checks: { columns: columns,
                             b: { value: bs, ok: Rsign(bs) > 0,
                                  text: bparts.join(' + ') + ' = ' + Rtext(bs) + ' &gt; 0' } },
             ok: allCols && Rsign(bs) > 0, rowSign: std.rowSign.slice() };
  }

  /* ---- one call, end to end -------------------------------------------- */

  /* Assembly over the five functions above, not new mathematics: a kit that
     only wants "solve this" should not have to re-write the Phase I hand-off,
     because every kit that re-wrote it would re-write it slightly differently. */
  function lpSolve(model, opts) {
    opts = opts || {};
    var std = stdForm(model);
    var p1 = phaseOne(std, opts);
    if (!p1.feasible) {
      return { std: std, phase1: p1, status: 'infeasible', tab: p1.T,
               certificate: farkasCertificate(p1.T), run: null, z: null, zOrig: null,
               x: null, read: null };
    }
    var tab = phaseTwo(std, p1);
    var run = simplexRun(tab, opts);
    var read = tabRead(run.tab);
    return { std: std, phase1: p1, tab: run.tab, run: run, status: run.status,
             read: read, x: stdPoint(std, read.x), xcols: read.x, z: read.z, zOrig: read.zOrig,
             ray: run.ray, certificate: null };
  }
"""


# --------------------------------- the second program, B^-1, dual simplex

DUAL_JS = r"""
  /* The dual, the vector that reads out of the final tableau, and the dual
     simplex.  Needs TABLEAU_JS, PHASE_JS and algebra_systems.MATRIX_JS above
     it -- basisInverse is assembly over Mrref, Maug, Mtake, Mid and Mmul,
     which already ship, and Mrref already returns the narrated ops list. */

  /* ---- the second program ---------------------------------------------- */

  /* One dual variable per primal ROW, one dual constraint per primal COLUMN,
     and a sign rule on each.  `pairs` carries the pairing and the rule that
     fixed it, because "the dual of a <= row in a max problem is a y >= 0" is
     the content of the lesson and an unlabelled matrix transpose is not.

     Feeding dualModel its own output returns the primal -- the toggle C3 L1
     offers -- and that is a property of these four rules, not a special case. */
  function dualModel(model) {
    var maxP = model.max !== false, m = model.cons.length, nv = model.obj.length;
    var free = model.free || [], nonpos = model.nonpos || [];
    var names = [], obj = [], cons = [], pairs = [], dfree = [], dnonpos = [], i, j;
    for (i = 0; i < m; i += 1) {
      var rel = model.cons[i].rel || 'le', label = model.cons[i].name || ('row ' + (i + 1));
      var sign, rule;
      if (rel === 'eq') {
        sign = 'free'; dfree.push(i);
        rule = 'an = row binds in both directions, so its price is unrestricted in sign';
      } else if (maxP ? rel === 'le' : rel === 'ge') {
        sign = 'ge0';
        rule = maxP ? 'a <= row in a maximisation prices a scarce resource, so y >= 0'
                    : 'a >= row in a minimisation prices a requirement, so y >= 0';
      } else {
        sign = 'le0'; dnonpos.push(i);
        rule = maxP ? 'a >= row in a maximisation is a floor, and relaxing it cannot help, so y <= 0'
                    : 'a <= row in a minimisation is a cap, so y <= 0';
      }
      names.push('y' + (i + 1)); obj.push(model.cons[i].b);
      pairs.push({ kind: 'row', index: i, primal: label, dual: 'y' + (i + 1),
                   rel: rel, sign: sign, rule: rule });
    }
    var pnames = model.names || [];
    for (j = 0; j < nv; j += 1) {
      var a = [];
      for (i = 0; i < m; i += 1) a.push(model.cons[i].a[j]);
      var pn = pnames[j] || ('x' + (j + 1)), rel2, rule2;
      if (free.indexOf(j) >= 0) {
        rel2 = 'eq';
        rule2 = pn + ' is free, so its dual constraint holds with equality';
      } else if (maxP ? nonpos.indexOf(j) >= 0 : nonpos.indexOf(j) < 0) {
        rel2 = maxP ? 'le' : 'le';
        rule2 = maxP ? pn + ' <= 0 flips the direction of its dual constraint'
                     : 'in a minimisation, ' + pn + ' >= 0 gives a dual constraint that may not exceed its cost';
      } else {
        rel2 = 'ge';
        rule2 = maxP ? pn + ' >= 0 means the priced resources it uses must be worth at least what it earns'
                     : pn + ' <= 0 flips the direction of its dual constraint';
      }
      cons.push({ a: a, rel: rel2, b: model.obj[j], name: 'the ' + pn + ' column' });
      pairs.push({ kind: 'col', index: j, primal: pn, dual: 'the ' + pn + ' column',
                   rel: rel2, rule: rule2 });
    }
    return { max: !maxP, names: names, obj: obj, cons: cons,
             free: dfree, nonpos: dnonpos, pairs: pairs, ofPrimal: model };
  }

  /* ---- y, read straight out of the final tableau ----------------------- */

  /* y = c_B' B^-1, and the columns that hold B^-1 are the ones that STARTED as
     the identity.  On a <= row that is the slack; on a >= row the slack is the
     SURPLUS column, which is -e_i and holds nothing of the sort -- the
     artificial next to it is the identity column.  C2 L8's named misconception
     is exactly that confusion, so this returns the column indices it used and
     the kind of each, rather than assuming a reader knows. */
  function dualVector(tab) {
    var std = tab.std, m = std.m, i, j;
    var yInt = [], columns = [];
    for (i = 0; i < m; i += 1) {
      var col = std.identity[i];
      yInt.push(Radd(tab.z[col], tab.c[col]));
      columns.push({ row: i, col: col, name: std.names[col], kind: std.kinds[col],
                     isSlack: std.kinds[col] === 'slack' });
    }
    var y = std.maximised ? yInt.slice() : yInt.map(Rneg);
    var want = std.maximised ? 'ge' : 'le';
    var check = [];
    for (j = 0; j < std.n; j += 1) {
      if (std.kinds[j] === 'artificial') continue;
      var s = R0, parts = [];
      for (i = 0; i < m; i += 1) {
        s = Radd(s, Rmul(y[i], std.A[i][j]));
        parts.push('(' + Rtext(y[i]) + ')(' + Rtext(std.A[i][j]) + ')');
      }
      var gap = Rsub(s, std.cOrig[j]);
      check.push({ j: j, name: std.names[j], value: s, cost: std.cOrig[j], gap: gap,
                   ok: want === 'ge' ? Rsign(gap) >= 0 : Rsign(gap) <= 0,
                   text: parts.join(' + ') + ' = ' + Rtext(s) + ' '
                     + (want === 'ge' ? '&gt;=' : '&lt;=') + ' ' + Rtext(std.cOrig[j]) });
    }
    var value = R0;
    for (i = 0; i < m; i += 1) value = Radd(value, Rmul(y[i], std.b[i]));
    return { y: y, yInternal: yInt, columns: columns, check: check, value: value,
             rowSign: std.rowSign.slice(),
             ok: check.every(function (c) { return c.ok; }) };
  }

  /* B, B^-1 with its reduction trace, and the three products written out
     beside the tableau, entry for entry.  New mathematics: none.  What did NOT
     exist before this function is the part that knows WHICH columns are the
     basis, which is the half a reader gets wrong. */
  function basisInverse(tab, model) {
    var std = model ? stdForm(model) : tab.std, m = std.m, i, j;
    var B = [], bcol = [];
    for (i = 0; i < m; i += 1) {
      var row = [];
      for (j = 0; j < m; j += 1) row.push(std.A[i][tab.basis[j]]);
      B.push(row);
    }
    for (j = 0; j < m; j += 1) bcol.push({ col: tab.basis[j], name: std.names[tab.basis[j]] });
    var red = Mrref(Maug(B, Mid(m)), { cols: m });
    var Binv = red.rank === m ? Mtake(red.M, m, m) : null;
    var bmat = std.b.map(function (v) { return [v]; });
    var BinvA = Binv ? Mmul(Binv, std.A) : null;
    var Binvb = Binv ? Mmul(Binv, bmat) : null;
    var zrow = null;
    if (BinvA) {
      zrow = [];
      for (j = 0; j < std.n; j += 1) {
        var s = R0;
        for (i = 0; i < m; i += 1) s = Radd(s, Rmul(tab.c[tab.basis[i]], BinvA[i][j]));
        zrow.push(Rsub(s, tab.c[j]));
      }
    }
    return { B: B, Binv: Binv, ops: red.ops, columns: bcol, BinvA: BinvA,
             Binvb: Binvb, zrow: zrow, singular: red.rank !== m, A: std.A, b: bmat };
  }

  /* ---- the dual simplex ------------------------------------------------ */

  /* The primal simplex keeps feasibility and hunts optimality; this keeps
     optimality and hunts feasibility, which is what makes it the right engine
     for a cut or a branch -- both leave the objective row alone and break the
     right-hand side.

     Leaving row: the most negative b_i, ties by lowest index.  Entering
     column: the dual ratio test min |z_j - c_j| / |a_rj| over a_rj < 0.  When
     no entry in that row is negative, the row says a non-negative combination
     of the variables must be negative, and the problem is INFEASIBLE. */
  function dualPivot(tab) {
    var rows = [], i, j, leave = -1;
    for (i = 0; i < tab.m; i += 1) {
      var bi = tab.T[i][tab.n];
      rows.push({ i: i, b: bi, basic: tab.basis[i], name: tab.names[tab.basis[i]],
                  negative: Rsign(bi) < 0 });
      if (Rsign(bi) < 0 && (leave < 0 || Rcmp(bi, tab.T[leave][tab.n]) < 0)) leave = i;
    }
    if (leave < 0) {
      return { leave: -1, rows: rows, enter: -1, tie: [], infeasible: false,
               ratios: [], feasible: true,
               why: 'every basic variable is already non-negative, so this basis is primal feasible' };
    }
    var dr = dualRatio(tab, leave);
    return { leave: leave, rows: rows, enter: dr.enter, tie: dr.tie,
             infeasible: dr.enter < 0, ratios: dr.ratios, feasible: false,
             why: dr.enter < 0
               ? 'row ' + (leave + 1) + ' has no negative entry, so it asserts that a non-negative combination is negative: the problem is infeasible'
               : tab.names[dr.enter] + ' wins the dual ratio test in row ' + (leave + 1) };
  }

  /* The dual ratio test on ONE named row.  Split out because rhsCurve needs it
     on a row whose right-hand side is exactly zero -- the breakpoint where a
     basic variable is about to go negative -- which dualPivot, hunting the most
     negative entry, would never choose. */
  function dualRatio(tab, r) {
    var ratios = [], enter = -1, best = null, j;
    for (j = 0; j < tab.n; j += 1) {
      if (tab.basis.indexOf(j) >= 0 || tab.forbid[j]) continue;
      var a = tab.T[r][j];
      if (Rsign(a) >= 0) {
        ratios.push({ j: j, name: tab.names[j], a: a, ratio: null, eligible: false,
                      why: 'the entry is ' + Rtext(a) + ', not negative, so raising ' + tab.names[j]
                        + ' cannot lift a negative right-hand side' });
        continue;
      }
      var q = Rdiv(Rabs(tab.z[j]), Rabs(a));
      ratios.push({ j: j, name: tab.names[j], a: a, ratio: q, eligible: true,
                    why: '|' + Rtext(tab.z[j]) + '| / |' + Rtext(a) + '| = ' + Rtext(q)
                      + ', the cost of bringing ' + tab.names[j] + ' in' });
      if (best === null || Rcmp(q, best) < 0) { best = q; enter = j; }
    }
    var tie = ratios.filter(function (t) { return t.eligible && Requ(t.ratio, best); })
                    .map(function (t) { return t.j; });
    return { ratios: ratios, enter: enter, tie: tie, min: best };
  }

  function dualSimplexRun(tab, opts) {
    opts = opts || {};
    var maxPivots = opts.maxPivots === undefined ? 200 : opts.maxPivots;
    var cur = tabCopy(tab), path = [cur], bases = [cur.basis.slice()], steps = [];
    var status = 'optimal';
    while (true) {
      var dp = dualPivot(cur);
      if (dp.leave < 0) { status = 'optimal'; break; }
      if (dp.infeasible) { status = 'infeasible'; break; }
      var before = cur;
      cur = tabPivot(cur, dp.leave, dp.enter);
      steps.push({ enter: dp.enter, enterName: cur.names[dp.enter], leave: cur.left,
                   leaveName: cur.names[cur.left], row: dp.leave, pivot: dp,
                   whyLeave: 'b = ' + Rtext(before.T[dp.leave][before.n]) + ' is the most negative right-hand side',
                   whyEnter: dp.why, ops: cur.ops,
                   zBefore: before.z[before.n], zAfter: cur.z[cur.n],
                   delta: Rsub(cur.z[cur.n], before.z[before.n]) });
      path.push(cur); bases.push(cur.basis.slice());
      if (steps.length >= maxPivots) { status = 'limit'; break; }
    }
    var z = cur.z[cur.n];
    return { path: path, bases: bases, steps: steps, pivots: steps.length,
             status: status, ray: null, cycle: null, tab: cur, z: z,
             zOrig: cur.maximised ? z : Rneg(z) };
  }
"""


# -------------------------------------------- sensitivity, all by ratio test

RANGE_JS = r"""
  /* Sensitivity.  Every answer here is a ratio test on numbers already in the
     final tableau -- there is no second solve and no re-derivation, which is
     the lesson: the tableau you finished with already knows how far the data
     can move.  Needs TABLEAU_JS, PHASE_JS and DUAL_JS above it. */

  /* B^-1, gathered out of the columns that started as the identity.  Column i
     of B^-1 is the tableau column standing over identity[i], because that
     column of the ORIGINAL A is e_i. */
  function rangeBinvCol(tab, i) {
    var col = tab.std.identity[i], out = [], r;
    for (r = 0; r < tab.m; r += 1) out.push(tab.T[r][col]);
    return out;
  }
  /* Recompute the right-hand side, and the objective value with it, for a new
     b -- without re-solving, because the basis has not changed. */
  function tabSetRhs(tab, bnew) {
    var out = tabCopy(tab), r, i, k;
    /* The standard form travels with the tableau and rhsRange reads b out of
       it, so a new right-hand side has to reach BOTH or the next range comes
       back quoted against the old data. */
    var std2 = {};
    for (k in out.std) if (Object.prototype.hasOwnProperty.call(out.std, k)) std2[k] = out.std[k];
    std2.b = bnew.slice();
    out.std = std2;
    var z = R0;
    for (r = 0; r < out.m; r += 1) {
      var s = R0;
      for (i = 0; i < out.m; i += 1) s = Radd(s, Rmul(out.T[r][out.std.identity[i]], bnew[i]));
      out.T[r][out.n] = s;
      z = Radd(z, Rmul(out.c[out.basis[r]], s));
    }
    out.z[out.n] = z;
    return out;
  }

  /* The interval of b_i over which THIS basis stays optimal, from
     B^-1 b + d * (B^-1)_{.i} >= 0.  Optimality is untouched by b, so the only
     question is when a basic variable would go negative -- a ratio test again.

     Quoted in the READER's units: a row the solver flipped to make its
     right-hand side non-negative has rowSign -1, and a range quoted in flipped
     units is a wrong answer that looks right. */
  function rhsRange(tab, i) {
    var sign = tab.std.rowSign[i], col = rangeBinvCol(tab, i);
    var bi = Rmul(R(BigInt(sign), 1n), tab.std.b[i]);
    var lo = null, hi = null, loRow = -1, hiRow = -1, rows = [], r;
    for (r = 0; r < tab.m; r += 1) {
      var g = sign < 0 ? Rneg(col[r]) : col[r];
      var xb = tab.T[r][tab.n], bound = null, dir = '';
      if (!Rzero(g)) {
        bound = Rneg(Rdiv(xb, g));
        if (Rsign(g) > 0) {
          dir = 'lower';
          if (lo === null || Rcmp(bound, lo) > 0) { lo = bound; loRow = r; }
        } else {
          dir = 'upper';
          if (hi === null || Rcmp(bound, hi) < 0) { hi = bound; hiRow = r; }
        }
      }
      rows.push({ row: r, basic: tab.basis[r], name: tab.names[tab.basis[r]],
                  value: xb, coef: g, bound: bound, dir: dir,
                  why: Rzero(g)
                    ? tab.names[tab.basis[r]] + ' does not move with this right-hand side'
                    : Rtext(xb) + ' + d(' + Rtext(g) + ') >= 0 gives d '
                      + (Rsign(g) > 0 ? '&gt;= ' : '&lt;= ') + Rtext(bound) });
    }
    var dv = dualVector(tab);
    return { lo: lo === null ? null : Radd(bi, lo), hi: hi === null ? null : Radd(bi, hi),
             b: bi, dLo: lo, dHi: hi, loRow: loRow, hiRow: hiRow, rows: rows,
             y_i: dv.y[i], basis: tab.basis.slice(), column: col };
  }

  /* The interval of c_j.  THE TWO CASES ARE DIFFERENT FORMULAS, and believing
     they are one is the misconception C3 L6 is named after.

       nonbasic j:  changing c_j moves only its own reduced cost, so the basis
                    survives until that one reduced cost reaches zero.
       basic j:     changing c_j moves EVERY nonbasic reduced cost, by d times
                    that column's entry in j's own row, so it is a ratio test
                    over all of them and the interval is two-sided. */
  function costRange(tab, j) {
    var basicRow = tab.basis.indexOf(j);
    var lo = null, hi = null, terms = [], k;
    if (basicRow < 0) {
      hi = tab.z[j];
      terms.push({ k: j, name: tab.names[j], coef: R1, reduced: tab.z[j], bound: hi,
                   why: 'its own reduced cost ' + Rtext(tab.z[j]) + ' falls by d, and must stay >= 0' });
    } else {
      for (k = 0; k < tab.n; k += 1) {
        if (tab.basis.indexOf(k) >= 0 || tab.forbid[k]) continue;
        var a = tab.T[basicRow][k];
        if (Rzero(a)) continue;
        var bound = Rneg(Rdiv(tab.z[k], a));
        if (Rsign(a) > 0) { if (lo === null || Rcmp(bound, lo) > 0) lo = bound; }
        else { if (hi === null || Rcmp(bound, hi) < 0) hi = bound; }
        terms.push({ k: k, name: tab.names[k], coef: a, reduced: tab.z[k], bound: bound,
                     why: Rtext(tab.z[k]) + ' + d(' + Rtext(a) + ') >= 0 gives d '
                       + (Rsign(a) > 0 ? '&gt;= ' : '&lt;= ') + Rtext(bound) });
      }
    }
    /* Back into the lesson's sense: a minimisation was negated on the way in,
       so its interval is the reflection of the one computed here. */
    var c = tab.std.cOrig[j], loOut, hiOut;
    if (tab.maximised) {
      loOut = lo === null ? null : Radd(c, lo);
      hiOut = hi === null ? null : Radd(c, hi);
    } else {
      loOut = hi === null ? null : Rsub(c, hi);
      hiOut = lo === null ? null : Rsub(c, lo);
    }
    return { lo: loOut, hi: hiOut, c: c, basic: basicRow >= 0, row: basicRow,
             terms: terms, basis: tab.basis.slice() };
  }

  /* z*(b_i) as an exact piecewise-linear function, every breakpoint and the
     basis on each piece.  The walk is exact rather than sampled: at the end of
     a basis's range some basic variable is exactly zero, and the dual ratio
     test on THAT row names the basis that takes over.  No epsilon is chosen
     anywhere, which is why the breakpoints are the breakpoints.

     schedule:crash's time-cost curve is this function on the project-deadline
     right-hand side.  It is the same function, not a second implementation. */
  function rhsCurve(model, i, lo, hi, opts) {
    opts = opts || {};
    var maxPieces = opts.maxPieces || 24;
    var base = stdForm(model);
    var start = { max: model.max, names: model.names, obj: model.obj, free: model.free,
                  nonpos: model.nonpos,
                  cons: model.cons.map(function (k, q) {
                    return q === i ? { a: k.a, rel: k.rel, b: lo, name: k.name } : k;
                  }) };
    var sol = lpSolve(start, opts);
    if (sol.status !== 'optimal') {
      return { pieces: [], breakpoints: [], status: sol.status, why:
        'at b = ' + Rtext(lo) + ' the problem is ' + sol.status + ', so there is no curve to draw yet' };
    }
    var cur = sol.tab, pieces = [], breaks = [], guard = 0, status = 'optimal';
    var bstd = base.b.slice();
    while (guard < maxPieces) {
      guard += 1;
      var rg = rhsRange(cur, i);
      var from = (rg.lo === null || Rcmp(rg.lo, lo) < 0) ? lo : rg.lo;
      var to = (rg.hi === null || Rcmp(rg.hi, hi) > 0) ? hi : rg.hi;
      var zHere = cur.z[cur.n];
      var zFrom = Radd(zHere, Rmul(rg.y_i, Rsub(from, rg.b)));
      var zTo = Radd(zHere, Rmul(rg.y_i, Rsub(to, rg.b)));
      pieces.push({ from: from, to: to, slope: rg.y_i, basis: cur.basis.slice(),
                    names: cur.basis.map(function (c) { return cur.names[c]; }),
                    z: cur.maximised ? zFrom : Rneg(zFrom),
                    zEnd: cur.maximised ? zTo : Rneg(zTo) });
      if (Rcmp(to, hi) >= 0) break;
      breaks.push(to);
      /* Move to the breakpoint exactly, then pivot out the basic variable that
         is sitting at zero and would go negative one step further on. */
      bstd[i] = Rmul(R(BigInt(base.rowSign[i]), 1n), to);
      cur = tabSetRhs(cur, bstd);
      var sign = base.rowSign[i], col = rangeBinvCol(cur, i), r, hit = -1;
      for (r = 0; r < cur.m; r += 1) {
        var g = sign < 0 ? Rneg(col[r]) : col[r];
        if (Rzero(cur.T[r][cur.n]) && Rsign(g) < 0) { hit = r; break; }
      }
      if (hit < 0) { status = 'stalled'; break; }
      var dr = dualRatio(cur, hit);
      if (dr.enter < 0) { status = 'infeasible beyond ' + Rtext(to); break; }
      cur = tabPivot(cur, hit, dr.enter);
    }
    return { pieces: pieces, breakpoints: breaks, status: status,
             concave: model.max !== false };
  }

  /* The efficient frontier of max (1 - L) f1 + L f2, exactly.

     For a FIXED basis the reduced costs are affine in L -- the tableau does not
     move, only the costs do -- so the range of L keeping a basis optimal is a
     one-line intersection of intervals, and the breakpoint is where one of
     them reaches zero.  Sampling L on a grid would find the same corners and
     would not prove there are no others between them.

     `corners` is the supported efficient set, in L order.  A kit wanting EVERY
     corner of a two-variable region already has algebra_systems.Ccorners. */
  function paramFront(model, c1, c2, opts) {
    opts = opts || {};
    var m1 = { max: model.max, names: model.names, obj: c1, cons: model.cons,
               free: model.free, nonpos: model.nonpos };
    var sol = lpSolve(m1, opts);
    if (sol.status !== 'optimal') {
      return { corners: [], efficient: [], breakpoints: [], status: sol.status };
    }
    var std = sol.std, cur = sol.tab, corners = [], breaks = [], guard = 0;
    /* Both cost vectors go through stdForm's OWN column map, so a split free
       variable or a flipped row is costed the same way in both. */
    var c1full = std.c.slice();
    var c2full = stdForm({ max: model.max, names: model.names, obj: c2, cons: model.cons,
                           free: model.free, nonpos: model.nonpos }).c.slice();
    var status = 'optimal';
    while (guard < (opts.maxPieces || 24)) {
      guard += 1;
      var u = tabCost(tabCopy(cur), c1full).z.slice();
      var v = tabCost(tabCopy(cur), c2full).z.slice();
      var read = tabRead(cur);
      var f1 = R0, f2 = R0, k;
      for (k = 0; k < std.n; k += 1) {
        f1 = Radd(f1, Rmul(c1full[k], read.x[k]));
        f2 = Radd(f2, Rmul(c2full[k], read.x[k]));
      }
      var lamLo = R0, lamHi = R1, cut = -1;
      for (k = 0; k < std.n; k += 1) {
        if (cur.basis.indexOf(k) >= 0 || cur.forbid[k]) continue;
        var a = u[k], bta = Rsub(v[k], u[k]);          /* a + L*b >= 0 */
        if (Rzero(bta)) continue;
        var bound = Rneg(Rdiv(a, bta));
        if (Rsign(bta) > 0) { if (Rcmp(bound, lamLo) > 0) lamLo = bound; }
        else if (Rcmp(bound, lamHi) < 0) { lamHi = bound; cut = k; }
      }
      corners.push({ from: lamLo, to: lamHi, x: stdPoint(std, read.x),
                     f1: std.maximised ? f1 : Rneg(f1), f2: std.maximised ? f2 : Rneg(f2),
                     basis: cur.basis.slice() });
      if (Rcmp(lamHi, R1) >= 0 || cut < 0) break;
      breaks.push(lamHi);
      var rt = tabRatio(cur, cut, 'dantzig');
      if (rt.unbounded) { status = 'unbounded'; break; }
      cur = tabPivot(cur, rt.leave, cut);
    }
    /* Pareto: keep the corners no other corner beats on both objectives. */
    var efficient = [];
    corners.forEach(function (p, i) {
      var dominated = corners.some(function (q, j2) {
        return j2 !== i && Rcmp(q.f1, p.f1) >= 0 && Rcmp(q.f2, p.f2) >= 0
          && (Rcmp(q.f1, p.f1) > 0 || Rcmp(q.f2, p.f2) > 0);
      });
      if (!dominated) efficient.push(i);
    });
    return { corners: corners, efficient: efficient, breakpoints: breaks, status: status };
  }

  /* Price a new activity: is it worth what it uses?  c_j - y'A_j, and the one
     pivot that brings it in when the answer is yes. */
  function priceColumn(tab, col, cost) {
    var std = tab.std, m = std.m, i, r;
    var dv = dualVector(tab), used = R0, parts = [];
    for (i = 0; i < m; i += 1) {
      used = Radd(used, Rmul(dv.y[i], col[i]));
      parts.push('(' + Rtext(dv.y[i]) + ')(' + Rtext(col[i]) + ')');
    }
    var reduced = Rsub(cost, used);
    var enters = std.maximised ? Rsign(reduced) > 0 : Rsign(reduced) < 0;
    /* The new column INSIDE the tableau is B^-1 A_j, and its objective entry
       is y'A_j - c_j in the internal max sense. */
    var inside = [];
    for (r = 0; r < m; r += 1) {
      var s = R0;
      for (i = 0; i < m; i += 1) {
        s = Radd(s, Rmul(tab.T[r][std.identity[i]],
                         Rmul(R(BigInt(std.rowSign[i]), 1n), col[i])));
      }
      inside.push(s);
    }
    var after = null, pivot = null;
    if (enters) {
      var ext = tabCopy(tab);
      var cInt = std.maximised ? cost : Rneg(cost);
      ext.T = ext.T.map(function (row, q) {
        var out = row.slice(); out.splice(ext.n, 0, inside[q]); return out;
      });
      ext.z = ext.z.slice(); ext.z.splice(ext.n, 0, Rneg(std.maximised ? reduced : Rneg(reduced)));
      ext.names = ext.names.concat([]); ext.names.splice(ext.n, 0, 'new');
      ext.kinds = ext.kinds.slice(); ext.kinds.splice(ext.n, 0, 'decision');
      ext.forbid = ext.forbid.slice(); ext.forbid.splice(ext.n, 0, false);
      ext.c = ext.c.slice(); ext.c.splice(ext.n, 0, cInt);
      ext.n += 1;
      ext.std = rangeExtendStd(std, inside, cost, cInt, 'new');
      var rt = tabRatio(ext, ext.n - 1, 'dantzig');
      if (!rt.unbounded) { after = tabPivot(ext, rt.leave, ext.n - 1); pivot = rt; }
      else after = ext;
    }
    return { reduced: reduced, used: used, enters: enters, column: inside, after: after,
             ratio: pivot, y: dv.y,
             text: Rtext(cost) + ' - (' + parts.join(' + ') + ') = ' + Rtext(reduced) };
  }
  /* A standard form with one more column, so the tableau priceColumn/addRow
     hand back is still readable by dualVector, rhsRange and tabRead. */
  function rangeExtendStd(std, colInside, cost, cInt, name) {
    var out = {}, k;
    for (k in std) if (Object.prototype.hasOwnProperty.call(std, k)) out[k] = std[k];
    out.names = std.names.concat([name]);
    out.kinds = std.kinds.concat(['decision']);
    out.sentences = std.sentences.concat(['the activity added after the fact']);
    out.cOrig = std.cOrig.concat([cost]);
    out.c = std.c.concat([cInt]);
    out.A = std.A.map(function (row) { return row.concat([R0]); });
    out.n = std.n + 1;
    return out;
  }

  /* A new CONSTRAINT, appended and then restored by dual simplex.  The row
     arrives in the reader's variables; it has to be written in terms of the
     NONBASIC ones before it says anything, and that subtraction is the step a
     reader skips. */
  function addRow(tab, row, opts) {
    var std = tab.std, i, j, r;
    var rel = row.rel || 'le', a = row.a.slice(), b = row.b;
    if (rel === 'ge') { a = a.map(Rneg); b = Rneg(b); rel = 'le'; }
    var slack = std.n;                               /* the new slack column */
    var A2 = std.A.map(function (rw) { return rw.concat([R0]); });
    var newRow = [];
    for (j = 0; j < std.n; j += 1) newRow.push(j < std.nd ? a[j] : R0);
    newRow.push(R1);
    A2.push(newRow);
    var std2 = {}, k;
    for (k in std) if (Object.prototype.hasOwnProperty.call(std, k)) std2[k] = std[k];
    std2.A = A2; std2.b = std.b.concat([b]); std2.m = std.m + 1; std2.n = std.n + 1;
    std2.c = std.c.concat([R0]); std2.cOrig = std.cOrig.concat([R0]);
    std2.names = std.names.concat(['s' + (std.m + 1)]);
    std2.kinds = std.kinds.concat(['slack']);
    std2.sentences = std.sentences.concat(['the part of the added constraint left unused']);
    std2.identity = std.identity.concat([slack]);
    std2.rowSlack = std.rowSlack.concat([slack]);
    std2.rowSign = std.rowSign.concat([row.rel === 'ge' ? -1 : 1]);
    std2.rels = std.rels.concat(['le']);
    var out = tabCopy(tab);
    out.T = out.T.map(function (rw) { var c = rw.slice(); c.splice(out.n, 0, R0); return c; });
    out.z = out.z.slice(); out.z.splice(out.n, 0, R0);
    out.names = std2.names.slice(); out.kinds = std2.kinds.slice();
    out.forbid = out.forbid.slice(); out.forbid.splice(out.n, 0, false);
    out.c = std2.c.slice(); out.cOrig = std2.cOrig.slice();
    out.identity = std2.identity.slice(); out.rowSlack = std2.rowSlack.slice();
    out.rowSign = std2.rowSign.slice();
    out.n += 1; out.m += 1;
    out.std = std2;
    var body = newRow.slice(); body.push(b);
    out.T.push(body);
    out.basis = out.basis.concat([slack]);
    /* Eliminate the basic variables from the new row. */
    var ops = [];
    for (i = 0; i < out.m - 1; i += 1) {
      var coef = out.T[out.m - 1][out.basis[i]];
      if (Rzero(coef)) continue;
      var mlt = Rneg(coef);
      out.T[out.m - 1] = out.T[out.m - 1].map(function (v, cc) {
        return Radd(v, Rmul(mlt, out.T[i][cc]));
      });
      ops.push({ op: 'R' + out.m + ' -&gt; R' + out.m + ' + ' + Rterm(mlt) + 'R' + (i + 1),
                 why: 'clears the basic ' + out.names[out.basis[i]] + ' out of the new row',
                 after: tabMatrix(out) });
    }
    var run = dualSimplexRun(out, opts);
    return { tab: out, ops: ops, run: run, restored: run.tab, status: run.status,
             cutRow: out.m - 1, slack: slack };
  }
"""


# ------------------------------------------------ what the LP does not give

NET_JS = r"""
  /* Networks.  A node is an id, an arc is {from, to, cost, cap}, and every
     number is a rational.  Needs algebra_systems.MATRIX_JS for Mdet.

     graph.py's GRAPH_JS cannot be reused for any of this and the reason is
     worth stating: its routines close over module-level N, A and LESSON rather
     than taking a graph; link(M, i, j) writes both directions, so every graph
     it builds is undirected; its weights come from the formula
     ((7a + 13b) % 9) + 1 rather than from data; and dijkstra runs on Infinity
     and Number.  Its circular layout is four lines inline in a drawing routine
     rather than a shared function, so "the SVG layout can be shared" is not
     true as written -- and a source and a sink on a circle is unreadable
     anyway, which is why `network` gets its own layered layout, kit-local. */

  function netIndex(nodes) {
    var ix = {}, i;
    for (i = 0; i < nodes.length; i += 1) ix[nodes[i]] = i;
    return ix;
  }

  /* The node-arc incidence matrix: +1 at the tail, -1 at the head.  Every
     network problem on this path is one LP with this matrix and different
     data, which is the claim C4 L2 makes and this function is the evidence. */
  function incidence(nodes, arcs) {
    var ix = netIndex(nodes), M = [], i, j;
    for (i = 0; i < nodes.length; i += 1) {
      var row = [];
      for (j = 0; j < arcs.length; j += 1) {
        row.push(ix[arcs[j].from] === i ? R1 : (ix[arcs[j].to] === i ? R(-1n, 1n) : R0));
      }
      M.push(row);
    }
    return M;
  }

  /* Net flow out of every node, and the nodes where it does not match what the
     node is supposed to supply.  Naming the violated nodes is the point: "the
     flow is invalid" is not a lesson and "node C sends out 3 more than it takes
     in, and it is supposed to send 0" is. */
  function conservation(nodes, arcs, flow, supply) {
    var ix = netIndex(nodes), net = [], out = [], into = [], i, j;
    for (i = 0; i < nodes.length; i += 1) { net.push(R0); out.push(R0); into.push(R0); }
    for (j = 0; j < arcs.length; j += 1) {
      var f = flow[j] === undefined ? R0 : flow[j];
      out[ix[arcs[j].from]] = Radd(out[ix[arcs[j].from]], f);
      into[ix[arcs[j].to]] = Radd(into[ix[arcs[j].to]], f);
    }
    var violated = [], rows = [];
    for (i = 0; i < nodes.length; i += 1) {
      net[i] = Rsub(out[i], into[i]);
      var want = (supply && supply[nodes[i]] !== undefined) ? supply[nodes[i]] : R0;
      var ok = Requ(net[i], want);
      rows.push({ node: nodes[i], out: out[i], into: into[i], net: net[i], want: want, ok: ok,
                  why: Rtext(out[i]) + ' out - ' + Rtext(into[i]) + ' in = ' + Rtext(net[i])
                    + ', and ' + nodes[i] + ' must net ' + Rtext(want) });
      if (!ok) violated.push(nodes[i]);
    }
    return { net: net, rows: rows, violated: violated, ok: violated.length === 0 };
  }

  /* The determinant of any chosen rows and columns, exact.  Mtake slices a
     CONTIGUOUS block, so the gather is here and the determinant is Mdet's. */
  function submatrixDet(M, rows, cols) {
    var sub = rows.map(function (i) { return cols.map(function (j) { return M[i][j]; }); });
    return Mdet(sub);
  }
  /* Every k x k determinant up to kmax, with the ones outside {0, +-1} listed.
     Totally unimodular means every one of them is in that set, and the only
     honest way to show it at lesson size is to look at all of them. */
  function unimodularSweep(M, kmax, cap) {
    cap = cap || 20000;
    var nr = M.length, nc = nr ? M[0].length : 0, k, seen = 0;
    var bad = [], counts = [], stop = false;
    var pick = function (n, k2) {
      var out = [], idx = [], i;
      for (i = 0; i < k2; i += 1) idx.push(i);
      while (true) {
        out.push(idx.slice());
        var p = k2 - 1;
        while (p >= 0 && idx[p] === n - k2 + p) p -= 1;
        if (p < 0) break;
        idx[p] += 1;
        for (i = p + 1; i < k2; i += 1) idx[i] = idx[i - 1] + 1;
      }
      return out;
    };
    for (k = 1; k <= Math.min(kmax, nr, nc) && !stop; k += 1) {
      var rs = pick(nr, k), cs = pick(nc, k), a, b, count = 0;
      for (a = 0; a < rs.length && !stop; a += 1) {
        for (b = 0; b < cs.length; b += 1) {
          seen += 1; count += 1;
          if (seen > cap) { stop = true; break; }
          var d = submatrixDet(M, rs[a], cs[b]);
          if (!(Rzero(d) || Requ(d, R1) || Requ(d, R(-1n, 1n)))) {
            bad.push({ k: k, rows: rs[a], cols: cs[b], det: d });
          }
        }
      }
      counts.push({ k: k, checked: count });
    }
    return { bad: bad, counts: counts, checked: seen, truncated: stop,
             unimodular: bad.length === 0 && !stop };
  }

  /* ---- order, and the longest path ------------------------------------- */

  /* An order, or the cycle that prevents one.  A project network with a cycle
     has no schedule and saying which activities form the loop is the answer. */
  function topoOrder(nodes, arcs) {
    var ix = netIndex(nodes), n = nodes.length, deg = [], adj = [], i, j;
    for (i = 0; i < n; i += 1) { deg.push(0); adj.push([]); }
    for (j = 0; j < arcs.length; j += 1) {
      adj[ix[arcs[j].from]].push(ix[arcs[j].to]);
      deg[ix[arcs[j].to]] += 1;
    }
    var queue = [], order = [];
    for (i = 0; i < n; i += 1) if (deg[i] === 0) queue.push(i);
    while (queue.length) {
      var v = queue.shift();
      order.push(nodes[v]);
      for (i = 0; i < adj[v].length; i += 1) {
        deg[adj[v][i]] -= 1;
        if (deg[adj[v][i]] === 0) queue.push(adj[v][i]);
      }
    }
    if (order.length === n) return { order: order, cycle: null };
    /* Walk forward inside what is left until a node repeats: that walk IS a
       cycle, and every node left has an incoming arc from the leftovers. */
    var left = {}, k;
    for (i = 0; i < n; i += 1) left[i] = deg[i] > 0;
    var start = -1;
    for (i = 0; i < n; i += 1) if (left[i]) { start = i; break; }
    var seen = {}, walk = [], cur = start;
    while (seen[cur] === undefined) {
      seen[cur] = walk.length; walk.push(cur);
      var nxt = -1;
      for (k = 0; k < adj[cur].length; k += 1) if (left[adj[cur][k]]) { nxt = adj[cur][k]; break; }
      if (nxt < 0) break;
      cur = nxt;
    }
    var cyc = seen[cur] === undefined ? walk : walk.slice(seen[cur]);
    return { order: order, cycle: cyc.map(function (q) { return nodes[q]; }) };
  }

  /* The longest path, by relaxation in topological order.  Longest is the
     right question for a project network and it is only well posed because the
     graph is acyclic -- which topoOrder has just checked. */
  function longestPath(nodes, arcs, s, t) {
    var top = topoOrder(nodes, arcs);
    if (top.cycle) return { dist: null, path: null, arcs: null, value: null, cycle: top.cycle, order: null };
    var ix = netIndex(nodes), dist = [], pred = [], predArc = [], i, j;
    for (i = 0; i < nodes.length; i += 1) {
      dist.push(s === undefined ? R0 : (nodes[i] === s ? R0 : null));
      pred.push(-1); predArc.push(-1);
    }
    for (i = 0; i < top.order.length; i += 1) {
      var v = ix[top.order[i]];
      if (dist[v] === null) continue;
      for (j = 0; j < arcs.length; j += 1) {
        if (ix[arcs[j].from] !== v) continue;
        var w = ix[arcs[j].to], cand = Radd(dist[v], arcs[j].cost || R0);
        if (dist[w] === null || Rcmp(cand, dist[w]) > 0) { dist[w] = cand; pred[w] = v; predArc[w] = j; }
      }
    }
    var end = -1;
    if (t !== undefined) end = ix[t];
    else for (i = 0; i < nodes.length; i += 1) if (dist[i] !== null && (end < 0 || Rcmp(dist[i], dist[end]) > 0)) end = i;
    var path = [], used = [];
    if (end >= 0 && dist[end] !== null) {
      var cur = end;
      while (cur >= 0) {
        path.unshift(nodes[cur]);
        if (predArc[cur] >= 0) used.unshift(predArc[cur]);
        cur = pred[cur];
      }
    }
    return { dist: dist, pred: pred, path: path, arcs: used,
             value: end >= 0 ? dist[end] : null, order: top.order, cycle: null };
  }

  /* The forward and backward passes, and everything a CPM table holds.
     `activities` is [{id, dur, pred: [id]}].  `paths` is every critical path,
     not one of them -- "shorten a critical activity and watch a SECOND path
     become critical" is the lesson, and it needs the plural. */
  function cpmPasses(activities) {
    var ix = {}, i, j;
    for (i = 0; i < activities.length; i += 1) ix[activities[i].id] = i;
    var nodes = activities.map(function (a) { return a.id; }), arcs = [];
    for (i = 0; i < activities.length; i += 1) {
      var ps = activities[i].pred || [];
      for (j = 0; j < ps.length; j += 1) arcs.push({ from: ps[j], to: activities[i].id, cost: R0 });
    }
    var top = topoOrder(nodes, arcs);
    if (top.cycle) return { cycle: top.cycle, ES: null, critical: null, paths: null };
    var ES = [], EF = [], LS = [], LF = [], slack = [];
    for (i = 0; i < activities.length; i += 1) { ES.push(R0); EF.push(R0); }
    for (i = 0; i < top.order.length; i += 1) {
      var v = ix[top.order[i]], ps2 = activities[v].pred || [], e = R0;
      for (j = 0; j < ps2.length; j += 1) if (Rcmp(EF[ix[ps2[j]]], e) > 0) e = EF[ix[ps2[j]]];
      ES[v] = e; EF[v] = Radd(e, activities[v].dur);
    }
    var makespan = R0;
    for (i = 0; i < activities.length; i += 1) if (Rcmp(EF[i], makespan) > 0) makespan = EF[i];
    var succ = [];
    for (i = 0; i < activities.length; i += 1) { LF.push(null); LS.push(null); succ.push([]); }
    for (i = 0; i < activities.length; i += 1) {
      var ps3 = activities[i].pred || [];
      for (j = 0; j < ps3.length; j += 1) succ[ix[ps3[j]]].push(i);
    }
    for (i = top.order.length - 1; i >= 0; i -= 1) {
      var v2 = ix[top.order[i]];
      if (!succ[v2].length) LF[v2] = makespan;
      else {
        var l = null;
        for (j = 0; j < succ[v2].length; j += 1) {
          var cand = LS[succ[v2][j]];
          if (l === null || Rcmp(cand, l) < 0) l = cand;
        }
        LF[v2] = l;
      }
      LS[v2] = Rsub(LF[v2], activities[v2].dur);
    }
    var critical = [];
    for (i = 0; i < activities.length; i += 1) {
      slack.push(Rsub(LS[i], ES[i]));
      if (Rzero(slack[i])) critical.push(activities[i].id);
    }
    /* Every critical path: a chain of zero-slack activities each starting when
       its predecessor finishes. */
    var paths = [], build = function (i2, acc) {
      if (paths.length > 200) return;
      var nxt = [], k;
      for (k = 0; k < succ[i2].length; k += 1) {
        var w = succ[i2][k];
        if (Rzero(slack[w]) && Requ(ES[w], EF[i2])) nxt.push(w);
      }
      if (!nxt.length) { paths.push(acc.slice()); return; }
      for (k = 0; k < nxt.length; k += 1) { acc.push(activities[nxt[k]].id); build(nxt[k], acc); acc.pop(); }
    };
    for (i = 0; i < activities.length; i += 1) {
      if (!Rzero(slack[i]) || (activities[i].pred || []).length) continue;
      build(i, [activities[i].id]);
    }
    return { ES: ES, EF: EF, LS: LS, LF: LF, slack: slack, critical: critical,
             paths: paths, makespan: makespan, order: top.order, cycle: null,
             ids: activities.map(function (a) { return a.id; }) };
  }

  /* ---- labels, potentials, residuals, cuts ----------------------------- */

  /* Bellman-Ford round by round, on RATIONAL arc costs.  The n-th round is not
     bookkeeping: an improvement there is the certificate of a negative cycle,
     and the cycle comes back with the arcs that make its cost negative. */
  function bellmanRounds(nodes, arcs, s) {
    var ix = netIndex(nodes), n = nodes.length, dist = [], pred = [], predArc = [], i, j, k;
    for (i = 0; i < n; i += 1) { dist.push(nodes[i] === s ? R0 : null); pred.push(-1); predArc.push(-1); }
    var rounds = [{ round: 0, dist: dist.slice(), changed: [] }];
    var negative = false, hit = -1;
    for (k = 1; k <= n; k += 1) {
      var changed = [];
      for (j = 0; j < arcs.length; j += 1) {
        var u = ix[arcs[j].from], v = ix[arcs[j].to];
        if (dist[u] === null) continue;
        var cand = Radd(dist[u], arcs[j].cost);
        if (dist[v] === null || Rcmp(cand, dist[v]) < 0) {
          dist[v] = cand; pred[v] = u; predArc[v] = j; changed.push(nodes[v]);
        }
      }
      rounds.push({ round: k, dist: dist.slice(), changed: changed });
      if (k === n && changed.length) { negative = true; hit = ix[changed[0]]; }
      if (!changed.length) break;
    }
    var cycle = null, cycleCost = null, cycleArcs = null;
    if (negative) {
      var cur = hit;
      for (i = 0; i < n; i += 1) cur = pred[cur];      /* walk into the cycle */
      var seen = [], at = cur;
      do { seen.push(at); at = pred[at]; } while (at !== cur && seen.length <= n + 1);
      seen.push(cur);
      seen.reverse();
      cycle = seen.map(function (q) { return nodes[q]; });
      cycleArcs = []; cycleCost = R0;
      for (i = 1; i < seen.length; i += 1) {
        cycleArcs.push(predArc[seen[i]]);
        cycleCost = Radd(cycleCost, arcs[predArc[seen[i]]].cost);
      }
    }
    return { rounds: rounds, dist: dist, pred: pred, negative: negative,
             cycle: cycle, cycleArcs: cycleArcs, cycleCost: cycleCost, nodes: nodes };
  }

  /* Every arc tested against pi_j - pi_i <= c_ij, the tight-arc subgraph, and
     pi_t - pi_s.  Feasible potentials exist exactly when no negative cycle
     does, so this is the dual reading of bellmanRounds and the two must agree. */
  function potentialCheck(nodes, arcs, pi, s, t) {
    var ix = netIndex(nodes), rows = [], violated = [], tight = [], j;
    for (j = 0; j < arcs.length; j += 1) {
      var gap = Rsub(pi[ix[arcs[j].to]], pi[ix[arcs[j].from]]);
      var slackv = Rsub(arcs[j].cost, gap), ok = Rsign(slackv) >= 0;
      rows.push({ arc: j, from: arcs[j].from, to: arcs[j].to, cost: arcs[j].cost,
                  gap: gap, slack: slackv, ok: ok, tight: Rzero(slackv),
                  why: Rtext(pi[ix[arcs[j].to]]) + ' - ' + Rtext(pi[ix[arcs[j].from]]) + ' = '
                    + Rtext(gap) + (ok ? ' &lt;= ' : ' &gt; ') + Rtext(arcs[j].cost) });
      if (!ok) violated.push(j);
      if (Rzero(slackv)) tight.push(j);
    }
    return { rows: rows, violated: violated, tight: tight, ok: violated.length === 0,
             value: (s !== undefined && t !== undefined) ? Rsub(pi[ix[t]], pi[ix[s]]) : null };
  }

  /* The residual network: what is left forward, and what can be undone. */
  function residual(arcs, flow) {
    var out = [], j;
    for (j = 0; j < arcs.length; j += 1) {
      var f = flow[j] === undefined ? R0 : flow[j], cap = arcs[j].cap;
      var fwd = Rsub(cap, f);
      if (Rsign(fwd) > 0) out.push({ from: arcs[j].from, to: arcs[j].to, cap: fwd, of: j, kind: 'forward' });
      if (Rsign(f) > 0) out.push({ from: arcs[j].to, to: arcs[j].from, cap: f, of: j, kind: 'backward' });
    }
    return out;
  }
  /* The source side of the minimum cut, once no augmenting path is left. */
  function reachable(nodes, resArcs, s) {
    var seen = {}, queue = [s], order = [];
    seen[s] = true;
    while (queue.length) {
      var v = queue.shift(); order.push(v);
      for (var j = 0; j < resArcs.length; j += 1) {
        if (resArcs[j].from !== v || seen[resArcs[j].to]) continue;
        seen[resArcs[j].to] = true; queue.push(resArcs[j].to);
      }
    }
    return { set: order, inSet: seen,
             other: nodes.filter(function (v) { return !seen[v]; }) };
  }
  /* The capacity of ANY cut the reader picks, so >= can be exhibited rather
     than asserted.  Only arcs LEAVING S count -- arcs coming back are free,
     and that asymmetry is the half a reader gets wrong. */
  function cutCapacity(nodes, arcs, S) {
    var inS = {}, i, j, total = R0, crossing = [], back = [];
    for (i = 0; i < S.length; i += 1) inS[S[i]] = true;
    for (j = 0; j < arcs.length; j += 1) {
      if (inS[arcs[j].from] && !inS[arcs[j].to]) { total = Radd(total, arcs[j].cap); crossing.push(j); }
      else if (!inS[arcs[j].from] && inS[arcs[j].to]) back.push(j);
    }
    return { capacity: total, crossing: crossing, back: back, S: S.slice() };
  }

  /* ---- matching, and the cover Koenig gives -------------------------- */

  /* A maximum matching by augmenting paths, the MINIMUM VERTEX COVER read off
     the alternating-reachable set by Koenig's theorem, and Hall's deficient
     set S with |N(S)| < |S| when the matching is imperfect.

     This is what makes the Hungarian method's minimum cover COMPUTABLE.  The
     "draw lines until you cannot" heuristic a textbook shows is not an
     algorithm, and a lab that implements it is guessing; the cover here is the
     one Koenig's theorem names, and its size equals the matching's by
     construction.

     `edges` is [[leftId, rightId], ...]. */
  function bipartiteMatch(left, right, edges) {
    var li = netIndex(left), ri = netIndex(right), i, j;
    var adj = left.map(function () { return []; });
    for (j = 0; j < edges.length; j += 1) adj[li[edges[j][0]]].push(ri[edges[j][1]]);
    var matchL = left.map(function () { return -1; });
    var matchR = right.map(function () { return -1; });
    var tryAugment = function (u, seen) {
      for (var k = 0; k < adj[u].length; k += 1) {
        var v = adj[u][k];
        if (seen[v]) continue;
        seen[v] = true;
        if (matchR[v] < 0 || tryAugment(matchR[v], seen)) { matchR[v] = u; matchL[u] = v; return true; }
      }
      return false;
    };
    for (i = 0; i < left.length; i += 1) if (matchL[i] < 0) tryAugment(i, {});
    /* Alternating reachability from the UNMATCHED left vertices. */
    var zl = {}, zr = {}, stack = [];
    for (i = 0; i < left.length; i += 1) if (matchL[i] < 0) { zl[i] = true; stack.push(i); }
    while (stack.length) {
      var u2 = stack.pop();
      for (j = 0; j < adj[u2].length; j += 1) {
        var v2 = adj[u2][j];
        if (matchL[u2] === v2 || zr[v2]) continue;          /* cross unmatched edges */
        zr[v2] = true;
        if (matchR[v2] >= 0 && !zl[matchR[v2]]) { zl[matchR[v2]] = true; stack.push(matchR[v2]); }
      }
    }
    var matching = [], coverL = [], coverR = [], S = [], NS = [];
    for (i = 0; i < left.length; i += 1) {
      if (matchL[i] >= 0) matching.push({ left: left[i], right: right[matchL[i]], li: i, ri: matchL[i] });
      if (!zl[i]) coverL.push(left[i]); else S.push(left[i]);
    }
    for (j = 0; j < right.length; j += 1) if (zr[j]) { coverR.push(right[j]); NS.push(right[j]); }
    return { matching: matching, size: matching.length,
             cover: { left: coverL, right: coverR, size: coverL.length + coverR.length },
             deficient: { S: S, N: NS, gap: S.length - NS.length,
                          hall: S.length > NS.length },
             alternating: { left: S.slice(), right: NS.slice() },
             perfect: matching.length === Math.min(left.length, right.length),
             matchL: matchL, matchR: matchR };
  }
"""


# ------------------------------------------------ the transportation tableau

TRANS_JS = r"""
  /* The transportation tableau.  Needs NET_JS above it: `hungarian` reads its
     minimum cover out of bipartiteMatch, by Koenig, rather than drawing lines.

     A basic solution here is a list of cells [{i, j, x}], and it has m + n - 1
     of them -- a spanning tree of the row/column bipartite graph.  Every
     routine below is that fact used twice: the potentials are the tree solved,
     and the stepping-stone cycle is the one cycle an extra edge creates. */

  /* Total supply and total demand are rarely equal and the difference is
     always MEANINGFUL: goods that stay in the warehouse, or demand that goes
     unmet.  The dummy row or column is where that meaning lives. */
  function balance(supply, demand, cost) {
    var ts = supply.reduce(Radd, R0), td = demand.reduce(Radd, R0);
    var s = supply.slice(), d = demand.slice(), c = cost ? cost.map(function (r) { return r.slice(); }) : null;
    var cmp = Rcmp(ts, td), dummy = null, amount = R0, why;
    if (cmp > 0) {
      dummy = 'col'; amount = Rsub(ts, td); d.push(amount);
      if (c) c = c.map(function (r) { return r.concat([R0]); });
      why = 'supply exceeds demand by ' + Rtext(amount)
        + ', so a zero-cost dummy DESTINATION holds what is never shipped';
    } else if (cmp < 0) {
      dummy = 'row'; amount = Rsub(td, ts); s.push(amount);
      if (c) { var w = []; for (var j = 0; j < d.length; j += 1) w.push(R0); c = c.concat([w]); }
      why = 'demand exceeds supply by ' + Rtext(amount)
        + ', so a zero-cost dummy SOURCE carries the shortfall, and whoever is assigned it goes unserved';
    } else why = 'supply and demand already balance at ' + Rtext(ts) + ', so no dummy is needed';
    return { supply: s, demand: d, cost: c, dummy: dummy, amount: amount,
             totalSupply: ts, totalDemand: td, why: why };
  }

  /* The north-west corner rule: allocate at the top-left cell still open.  It
     ignores cost entirely, which is the point -- it gives a starting basis,
     not a good one, and MODI improves it. */
  function northwest(cost, supply, demand) {
    var m = supply.length, n = demand.length, s = supply.slice(), d = demand.slice();
    var x = [], basis = [], steps = [], i = 0, j = 0, degenerate = false;
    for (var a = 0; a < m; a += 1) { var row = []; for (var b = 0; b < n; b += 1) row.push(R0); x.push(row); }
    while (i < m && j < n) {
      var amt = Rcmp(s[i], d[j]) < 0 ? s[i] : d[j];
      x[i][j] = amt; basis.push({ i: i, j: j, x: amt });
      steps.push({ i: i, j: j, amount: amt, supplyLeft: Rsub(s[i], amt), demandLeft: Rsub(d[j], amt),
                   why: 'cell (' + (i + 1) + ',' + (j + 1) + ') is the open north-west corner; it takes min('
                     + Rtext(s[i]) + ', ' + Rtext(d[j]) + ') = ' + Rtext(amt) });
      s[i] = Rsub(s[i], amt); d[j] = Rsub(d[j], amt);
      if (i === m - 1 && j === n - 1) break;
      if (Rzero(s[i]) && Rzero(d[j])) {
        degenerate = true;
        if (i < m - 1) i += 1; else j += 1;
      } else if (Rzero(s[i])) i += 1; else j += 1;
    }
    return transFinish(x, basis, steps, degenerate, m, n, cost, 'north-west corner');
  }

  /* The least-cost rule: always fill the cheapest open cell.  Better starts,
     same machinery, and the comparison of the two is the lesson. */
  function leastCost(cost, supply, demand) {
    var m = supply.length, n = demand.length, s = supply.slice(), d = demand.slice();
    var x = [], basis = [], steps = [], rows = [], cols = [], i, j, degenerate = false;
    for (i = 0; i < m; i += 1) { var row = []; for (j = 0; j < n; j += 1) row.push(R0); x.push(row); rows.push(i); }
    for (j = 0; j < n; j += 1) cols.push(j);
    while (rows.length && cols.length) {
      var bi = -1, bj = -1;
      for (var a = 0; a < rows.length; a += 1) {
        for (var b = 0; b < cols.length; b += 1) {
          if (bi < 0 || Rcmp(cost[rows[a]][cols[b]], cost[bi][bj]) < 0) { bi = rows[a]; bj = cols[b]; }
        }
      }
      var amt = Rcmp(s[bi], d[bj]) < 0 ? s[bi] : d[bj];
      x[bi][bj] = amt; basis.push({ i: bi, j: bj, x: amt });
      steps.push({ i: bi, j: bj, amount: amt, cost: cost[bi][bj],
                   why: 'cell (' + (bi + 1) + ',' + (bj + 1) + ') is the cheapest still open at '
                     + Rtext(cost[bi][bj]) + '; it takes ' + Rtext(amt) });
      s[bi] = Rsub(s[bi], amt); d[bj] = Rsub(d[bj], amt);
      if (rows.length + cols.length === 2) break;
      if (Rzero(s[bi]) && Rzero(d[bj])) { degenerate = true; rows.splice(rows.indexOf(bi), 1); }
      else if (Rzero(s[bi])) rows.splice(rows.indexOf(bi), 1);
      else cols.splice(cols.indexOf(bj), 1);
    }
    return transFinish(x, basis, steps, degenerate, m, n, cost, 'least cost');
  }

  /* m + n - 1 basic cells or the solution is not a basic one, and the cells
     that carry zero are the named epsilons rather than an embarrassment. */
  function transFinish(x, basis, steps, degenerate, m, n, cost, rule) {
    var want = m + n - 1, eps = [], total = R0, k;
    for (k = 0; k < basis.length; k += 1) {
      if (Rzero(basis[k].x)) eps.push({ i: basis[k].i, j: basis[k].j });
      if (cost) total = Radd(total, Rmul(cost[basis[k].i][basis[k].j], basis[k].x));
    }
    return { x: x, basis: basis, steps: steps, rule: rule,
             degenerate: degenerate || eps.length > 0, epsilon: eps,
             count: basis.length, want: want, cost: total,
             why: basis.length === want
               ? 'the ' + rule + ' rule left ' + basis.length + ' basic cells, which is m + n - 1 = ' + want
                 + (eps.length ? ', ' + eps.length + ' of them carrying zero (the named epsilon cells)' : '')
               : 'the ' + rule + ' rule left ' + basis.length + ' basic cells where m + n - 1 = ' + want };
  }

  /* u_i + v_j = c_ij on the basic cells, with ONE free variable set to zero --
     the tree has m + n - 1 edges and m + n nodes, so exactly one degree of
     freedom, and the choice of which u to zero moves every number without
     moving any reduced cost.  c_ij - u_i - v_j on the rest. */
  function uvPotentials(cost, basis, m, n) {
    m = m || cost.length; n = n || cost[0].length;
    var u = [], v = [], i, j, k;
    for (i = 0; i < m; i += 1) u.push(null);
    for (j = 0; j < n; j += 1) v.push(null);
    u[0] = R0;
    var order = [{ kind: 'u', at: 0, value: R0, why: 'u1 is set to 0; the system has one degree of freedom and this uses it' }];
    var moved = true;
    while (moved) {
      moved = false;
      for (k = 0; k < basis.length; k += 1) {
        var c = basis[k], cij = cost[c.i][c.j];
        if (u[c.i] !== null && v[c.j] === null) {
          v[c.j] = Rsub(cij, u[c.i]); moved = true;
          order.push({ kind: 'v', at: c.j, value: v[c.j], cell: [c.i, c.j],
                       why: 'v' + (c.j + 1) + ' = ' + Rtext(cij) + ' - ' + Rtext(u[c.i]) + ' = ' + Rtext(v[c.j])
                         + ', from the basic cell (' + (c.i + 1) + ',' + (c.j + 1) + ')' });
        } else if (v[c.j] !== null && u[c.i] === null) {
          u[c.i] = Rsub(cij, v[c.j]); moved = true;
          order.push({ kind: 'u', at: c.i, value: u[c.i], cell: [c.i, c.j],
                       why: 'u' + (c.i + 1) + ' = ' + Rtext(cij) + ' - ' + Rtext(v[c.j]) + ' = ' + Rtext(u[c.i])
                         + ', from the basic cell (' + (c.i + 1) + ',' + (c.j + 1) + ')' });
        }
      }
    }
    var isBasic = {};
    for (k = 0; k < basis.length; k += 1) isBasic[basis[k].i + ',' + basis[k].j] = true;
    var reduced = [], entering = null, connected = true;
    for (i = 0; i < m; i += 1) if (u[i] === null) connected = false;
    for (j = 0; j < n; j += 1) if (v[j] === null) connected = false;
    for (i = 0; i < m; i += 1) {
      var row = [];
      for (j = 0; j < n; j += 1) {
        if (!connected || u[i] === null || v[j] === null) { row.push(null); continue; }
        var r = Rsub(cost[i][j], Radd(u[i], v[j]));
        row.push(r);
        if (!isBasic[i + ',' + j] && Rsign(r) < 0
            && (entering === null || Rcmp(r, entering.value) < 0)) entering = { i: i, j: j, value: r };
      }
      reduced.push(row);
    }
    return { u: u, v: v, reduced: reduced, entering: entering, order: order,
             connected: connected, optimal: entering === null && connected };
  }

  /* The stepping-stone cycle: the UNIQUE cycle an entering cell creates in the
     spanning forest of basic cells, as an ordered, signed list starting at the
     entering cell.  theta is the minimum over the minus cells, and the cell
     that attains it leaves.

     Found by a path search in the tree, not by "look for a rectangle" -- the
     cycle is rectangular only in the easy pictures, and a lab that assumes it
     is fails on the first realistic tableau. */
  function stoneCycle(basis, enter, m, n) {
    var adj = {}, k, key = function (kind, i) { return kind + i; };
    for (k = 0; k < basis.length; k += 1) {
      var a = key('r', basis[k].i), b = key('c', basis[k].j);
      (adj[a] = adj[a] || []).push({ to: b, cell: basis[k] });
      (adj[b] = adj[b] || []).push({ to: a, cell: basis[k] });
    }
    var start = key('r', enter.i), goal = key('c', enter.j);
    var seen = {}, path = null;
    var walk = function (at, acc) {
      if (at === goal) { path = acc.slice(); return true; }
      seen[at] = true;
      var list = adj[at] || [];
      for (var q = 0; q < list.length; q += 1) {
        if (seen[list[q].to]) continue;
        acc.push(list[q].cell);
        if (walk(list[q].to, acc)) return true;
        acc.pop();
      }
      return false;
    };
    walk(start, []);
    if (path === null) return { cells: null, theta: null, leaving: null, found: false,
                                why: 'the basic cells do not connect row ' + (enter.i + 1)
                                  + ' to column ' + (enter.j + 1) + ', so no stepping-stone cycle exists' };
    var cells = [{ i: enter.i, j: enter.j, x: R0, sign: 1, entering: true }];
    for (k = 0; k < path.length; k += 1) {
      cells.push({ i: path[k].i, j: path[k].j, x: path[k].x, sign: (k % 2 === 0) ? -1 : 1 });
    }
    var theta = null, leaving = null;
    for (k = 0; k < cells.length; k += 1) {
      if (cells[k].sign > 0) continue;
      if (theta === null || Rcmp(cells[k].x, theta) < 0) { theta = cells[k].x; leaving = cells[k]; }
    }
    return { cells: cells, theta: theta, leaving: leaving, found: true,
             minus: cells.filter(function (c) { return c.sign < 0; }),
             why: 'theta = ' + (theta === null ? '-' : Rtext(theta))
               + ', the smallest allocation on a minus cell; cell ('
               + (leaving ? (leaving.i + 1) + ',' + (leaving.j + 1) : '-') + ') leaves' };
  }

  /* The Hungarian method, with the cover computed rather than drawn.

     Steps 1 and 2 are the row and column reductions.  Step 3 is the part every
     textbook hand-waves: the MINIMUM number of lines covering all the zeros.
     By Koenig's theorem that number is the size of a maximum matching on the
     zero cells, and the cover itself falls out of the alternating-reachable
     set -- which is what bipartiteMatch returns.  The "draw lines until you
     cannot" recipe is not an algorithm and cannot be implemented honestly. */
  function hungarian(cost) {
    var n = cost.length, i, j, steps = [];
    var M = cost.map(function (r) { return r.slice(); });
    var rowMin = [], colMin = [];
    for (i = 0; i < n; i += 1) {
      var mn = M[i][0];
      for (j = 1; j < n; j += 1) if (Rcmp(M[i][j], mn) < 0) mn = M[i][j];
      rowMin.push(mn);
      for (j = 0; j < n; j += 1) M[i][j] = Rsub(M[i][j], mn);
    }
    steps.push({ kind: 'rows', amounts: rowMin.slice(), M: M.map(function (r) { return r.slice(); }),
                 why: 'each row loses its own minimum; every assignment uses exactly one cell of each row, so this shifts every total by the same amount and changes no ranking' });
    for (j = 0; j < n; j += 1) {
      var mc = M[0][j];
      for (i = 1; i < n; i += 1) if (Rcmp(M[i][j], mc) < 0) mc = M[i][j];
      colMin.push(mc);
      for (i = 0; i < n; i += 1) M[i][j] = Rsub(M[i][j], mc);
    }
    steps.push({ kind: 'cols', amounts: colMin.slice(), M: M.map(function (r) { return r.slice(); }),
                 why: 'and each column loses its own minimum, for the same reason' });
    var left = [], right = [], guard = 0, match = null;
    for (i = 0; i < n; i += 1) { left.push('r' + i); right.push('c' + i); }
    while (guard < 4 * n + 4) {
      guard += 1;
      var edges = [];
      for (i = 0; i < n; i += 1) for (j = 0; j < n; j += 1) if (Rzero(M[i][j])) edges.push(['r' + i, 'c' + j]);
      match = bipartiteMatch(left, right, edges);
      steps.push({ kind: 'cover', size: match.cover.size, cover: match.cover,
                   matching: match.matching.map(function (p) { return [Number(p.left.slice(1)), Number(p.right.slice(1))]; }),
                   M: M.map(function (r) { return r.slice(); }),
                   why: 'a maximum matching on the zero cells has ' + match.size
                     + ' pairs, so by Koenig the minimum cover has ' + match.cover.size
                     + ' lines -- ' + (match.cover.size === n ? 'enough, so an assignment exists among the zeros'
                       : 'fewer than ' + n + ', so the zeros cannot carry an assignment yet') });
      if (match.cover.size >= n) break;
      var covR = {}, covC = {};
      for (i = 0; i < match.cover.left.length; i += 1) covR[Number(match.cover.left[i].slice(1))] = true;
      for (j = 0; j < match.cover.right.length; j += 1) covC[Number(match.cover.right[j].slice(1))] = true;
      var theta = null;
      for (i = 0; i < n; i += 1) for (j = 0; j < n; j += 1) {
        if (covR[i] || covC[j]) continue;
        if (theta === null || Rcmp(M[i][j], theta) < 0) theta = M[i][j];
      }
      if (theta === null) break;
      for (i = 0; i < n; i += 1) for (j = 0; j < n; j += 1) {
        if (!covR[i] && !covC[j]) M[i][j] = Rsub(M[i][j], theta);
        else if (covR[i] && covC[j]) M[i][j] = Radd(M[i][j], theta);
      }
      steps.push({ kind: 'adjust', theta: theta, M: M.map(function (r) { return r.slice(); }),
                   why: 'the smallest uncovered entry is ' + Rtext(theta)
                     + '; it comes off every uncovered entry and goes onto every doubly covered one, which creates a new zero without destroying the old ones' });
    }
    var assignment = [], value = R0;
    for (i = 0; i < n; i += 1) assignment.push(-1);
    for (i = 0; i < match.matching.length; i += 1) {
      var r = Number(match.matching[i].left.slice(1)), c = Number(match.matching[i].right.slice(1));
      assignment[r] = c; value = Radd(value, cost[r][c]);
    }
    return { steps: steps, matching: match.matching, cover: match.cover,
             assignment: assignment, value: value, reduced: M,
             complete: match.size === n };
  }
"""


# ----------------------------------------------------- integer programming

IP_JS = r"""
  /* Integer programming.  Needs TABLEAU_JS, PHASE_JS, DUAL_JS and
     sysdesign_core.RCEIL_JS (Rfloor, Rceil) above it.

     Everything here is the same LP solved again with more constraints, which
     is the Subject's claim and is why nothing below re-implements a solver. */

  /* The two children: x_j <= floor(v) and x_j >= ceil(v).  The gap between
     them is where the LP optimum was, and saying so is the lesson. */
  function branchPair(model, j, v) {
    var lo = Rfloor(v), hi = Rceil(v);
    var unit = model.obj.map(function (_, k) { return k === j ? R1 : R0; });
    var name = (model.names && model.names[j]) || ('x' + (j + 1));
    var down = { max: model.max, names: model.names, obj: model.obj, free: model.free,
                 nonpos: model.nonpos,
                 cons: model.cons.concat([{ a: unit, rel: 'le', b: R(lo, 1n),
                                            name: name + ' <= ' + lo }]) };
    var up = { max: model.max, names: model.names, obj: model.obj, free: model.free,
               nonpos: model.nonpos,
               cons: model.cons.concat([{ a: unit, rel: 'ge', b: R(hi, 1n),
                                          name: name + ' >= ' + hi }]) };
    return { down: down, up: up, floor: lo, ceil: hi, j: j, name: name, value: v,
             why: name + ' came back at ' + Rtext(v) + ', which no integer plan can do; every integer plan has '
               + name + ' <= ' + lo + ' or ' + name + ' >= ' + hi + ', and those two cases are the children' };
  }

  /* The tree.  Each child is re-solved FROM ITS PARENT'S TABLEAU by dual
     simplex -- addRow appends the branch and restores feasibility -- because
     re-solving from scratch at every node hides the one thing branch and bound
     is for, which is that a child is a small correction to its parent.

     opts.order is depthFirst or bestBound, and the two node counts on the same
     instance are C5 L7's whole comparison.  opts.maxNodes is a REFUSAL, not a
     silent truncation: a tree that stopped early and did not say so reports a
     wrong optimum with a straight face. */
  function bbTree(model, opts) {
    opts = opts || {};
    var order = opts.order === 'bestBound' ? 'bestBound' : 'depthFirst';
    var maxNodes = opts.maxNodes || 60;
    var maximise = model.max !== false;
    var ints = opts.integers || model.obj.map(function (_, j) { return j; });
    var root = lpSolve(model, opts);
    if (root.status !== 'optimal') {
      return { nodes: [], incumbents: [], bounds: [], gaps: [], counts: { explored: 0 },
               status: root.status, best: null, refused: false };
    }
    var nodes = [], open = [], incumbents = [], bounds = [], gaps = [];
    var best = null, bestX = null, refused = false, id = 0;
    var push = function (sol, parent, label) {
      var node = { id: id, parent: parent, depth: parent === null ? 0 : nodes[parent].depth + 1,
                   label: label, status: sol.status, bound: sol.status === 'optimal' ? sol.zOrig : null,
                   relaxation: sol.status === 'optimal' ? sol.x : null,
                   model: sol.model, sol: sol, prunedBy: null, children: [] };
      id += 1; nodes.push(node);
      if (parent !== null) nodes[parent].children.push(node.id);
      return node;
    };
    root.model = model;
    var r0 = push(root, null, 'root');
    open.push(r0.id);
    while (open.length) {
      if (nodes.length > maxNodes) { refused = true; break; }
      var pick = 0, k;
      if (order === 'bestBound') {
        for (k = 1; k < open.length; k += 1) {
          var a = nodes[open[k]].bound, b = nodes[open[pick]].bound;
          if (a === null) continue;
          if (b === null || (maximise ? Rcmp(a, b) > 0 : Rcmp(a, b) < 0)) pick = k;
        }
      } else pick = open.length - 1;
      var nid = open.splice(pick, 1)[0], node = nodes[nid];
      if (node.status !== 'optimal') { node.prunedBy = 'infeasible'; continue; }
      if (best !== null && (maximise ? Rcmp(node.bound, best) <= 0 : Rcmp(node.bound, best) >= 0)) {
        node.prunedBy = 'bound'; continue;
      }
      var frac = -1;
      for (k = 0; k < ints.length; k += 1) {
        if (!Rint(node.relaxation[ints[k]])) { frac = ints[k]; break; }
      }
      if (frac < 0) {
        node.prunedBy = 'integral';
        if (best === null || (maximise ? Rcmp(node.bound, best) > 0 : Rcmp(node.bound, best) < 0)) {
          best = node.bound; bestX = node.relaxation.slice();
          incumbents.push({ at: nodes.length, node: node.id, value: best, x: bestX.slice() });
        }
        continue;
      }
      node.branchOn = frac;
      var pair = branchPair(node.model, frac, node.relaxation[frac]);
      node.branch = pair;
      var kids = [['down', pair.down, pair.name + ' <= ' + pair.floor],
                  ['up', pair.up, pair.name + ' >= ' + pair.ceil]];
      var made = [];
      for (k = 0; k < kids.length; k += 1) {
        var child = bbChild(node, kids[k][1], frac, kids[k][0] === 'down' ? pair.floor : pair.ceil,
                            kids[k][0], opts);
        child.model = kids[k][1];
        var cn = push(child, node.id, kids[k][2]);
        made.push(cn.id);
      }
      /* depth-first wants the first child on top of the stack last. */
      if (order === 'depthFirst') { open.push(made[1]); open.push(made[0]); }
      else { open.push(made[0]); open.push(made[1]); }
      var gb = null;
      for (k = 0; k < open.length; k += 1) {
        var bd = nodes[open[k]].bound;
        if (bd === null) continue;
        if (gb === null || (maximise ? Rcmp(bd, gb) > 0 : Rcmp(bd, gb) < 0)) gb = bd;
      }
      bounds.push({ at: nodes.length, bound: gb, incumbent: best });
      if (gb !== null && best !== null) gaps.push({ at: nodes.length, gap: Rabs(Rsub(gb, best)) });
    }
    return { nodes: nodes, incumbents: incumbents, bounds: bounds, gaps: gaps,
             counts: { explored: nodes.length, order: order },
             best: best, x: bestX, refused: refused,
             status: refused ? 'refused' : (best === null ? 'no integer point' : 'optimal'),
             why: refused ? 'the tree passed ' + maxNodes + ' nodes, so it stopped and says so rather than reporting an optimum it has not proved' : '' };
  }

  /* One child, from its parent's tableau: append the branch as a row and let
     the dual simplex put feasibility back.  When the parent's tableau is not
     available -- the root came from Phase I with artificials still around --
     it falls back to a fresh solve, and says which it did. */
  function bbChild(node, childModel, j, bound, side, opts) {
    var std = node.sol.std;
    if (node.sol.tab && std.varMap && !std.varMap[j].free && std.varMap[j].sign > 0) {
      var col = std.varMap[j].plus, a = [], q;
      for (q = 0; q < std.nd; q += 1) a.push(q === col ? R1 : R0);
      var added = addRow(node.sol.tab, side === 'down'
        ? { a: a, rel: 'le', b: R(bound, 1n) } : { a: a, rel: 'ge', b: R(bound, 1n) }, opts);
      if (added.status === 'optimal') {
        var read = tabRead(added.restored);
        return { std: added.restored.std, tab: added.restored, run: added.run, status: 'optimal',
                 read: read, x: stdPoint(std, read.x), z: read.z, zOrig: read.zOrig,
                 from: 'dual simplex on the parent tableau', addRow: added };
      }
      if (added.status === 'infeasible') {
        return { status: 'infeasible', tab: null, x: null, zOrig: null,
                 from: 'dual simplex on the parent tableau', addRow: added };
      }
    }
    var fresh = lpSolve(childModel, opts);
    fresh.from = 'a fresh solve';
    return fresh;
  }

  /* A Gomory cut off row r: sum of frac(a_rj) x_j >= frac(b_r).

     EXACT because Rfrac of a rational is a rational -- which is the whole
     reason this is a cut and not a nudge.  It comes back in both coordinate
     systems: in the tableau's variables, where it is derived, and in the
     reader's, where it can be drawn on the lattice picture.  A lesson that
     shows only the first has not shown a cut, because nobody can see it. */
  function gomoryCut(tab, r) {
    var std = tab.std, j, i;
    var f = [], f0 = Rfrac(tab.T[r][tab.n]);
    for (j = 0; j < std.n; j += 1) f.push(Rfrac(tab.T[r][j]));
    /* Into the reader's variables: every added column is a known affine
       function of the decision ones, so substitute it. */
    var g = [], h = f0;
    for (j = 0; j < std.nd; j += 1) g.push(f[j]);
    for (j = std.nd; j < std.n; j += 1) {
      if (Rzero(f[j])) continue;
      var row = -1, kind = std.kinds[j], q;
      for (q = 0; q < std.m; q += 1) if (std.identity[q] === j || std.rowSlack[q] === j) { row = q; break; }
      if (row < 0 || kind === 'artificial') continue;
      /* slack   s_i = b_i - sum A_ij x_j    surplus  e_i = sum A_ij x_j - b_i */
      var sgn = kind === 'slack' ? -1 : 1;
      for (q = 0; q < std.nd; q += 1) {
        g[q] = Radd(g[q], Rmul(f[j], Rmul(R(BigInt(sgn), 1n), std.A[row][q])));
      }
      h = Rsub(h, Rmul(f[j], Rmul(R(BigInt(-sgn), 1n), std.b[row])));
    }
    var text = function (coefs, rhs, names) {
      var parts = [];
      for (var q2 = 0; q2 < coefs.length; q2 += 1) {
        if (Rzero(coefs[q2])) continue;
        parts.push(Rterm(coefs[q2]) + names[q2]);
      }
      return (parts.length ? parts.join(' + ') : '0') + ' &gt;= ' + Rtext(rhs);
    };
    return { cut: { a: f.slice(), b: f0 },
             row: r, basic: tab.basis[r], basicName: tab.names[tab.basis[r]],
             fracB: f0, integral: Rzero(f0),
             inTableau: { a: f.slice(), b: f0, rel: 'ge',
                          text: text(f, f0, std.names) },
             inOriginal: { a: g, b: h, rel: 'ge',
                           text: text(g, h, std.given || std.names) },
             why: 'row ' + (r + 1) + ' says ' + tab.names[tab.basis[r]] + ' = ' + Rtext(tab.T[r][tab.n])
               + '; rounding every coefficient down cannot increase the left side, so every INTEGER point satisfies the cut, and the current fractional one does not' };
  }

  /* Every integer point in the box, marked feasible or not, with its
     objective.  The exhaustive picture C5 L1 draws, and the only honest way to
     say "the integer optimum is NOT next to the LP optimum". */
  function latticePoints(model, box, cap) {
    cap = cap || 4000;
    var n = box.length, pts = [], counter = box.map(function (b) { return b[0]; });
    var total = 1, i, j;
    for (i = 0; i < n; i += 1) total *= Number(box[i][1] - box[i][0] + 1n);
    if (total > cap) return { points: [], truncated: true, total: total, cap: cap,
                              why: 'that box holds ' + total + ' lattice points and this lab draws at most ' + cap };
    var best = null;
    while (true) {
      var x = counter.map(function (v) { return R(v, 1n); });
      var ok = true, rows = [];
      for (i = 0; i < model.cons.length; i += 1) {
        var s = R0;
        for (j = 0; j < n; j += 1) s = Radd(s, Rmul(model.cons[i].a[j], x[j]));
        var rel = model.cons[i].rel || 'le', c = Rcmp(s, model.cons[i].b);
        var good = rel === 'le' ? c <= 0 : (rel === 'ge' ? c >= 0 : c === 0);
        rows.push({ i: i, value: s, ok: good });
        if (!good) ok = false;
      }
      var obj = R0;
      for (j = 0; j < n; j += 1) obj = Radd(obj, Rmul(model.obj[j], x[j]));
      if (ok && (best === null || (model.max !== false ? Rcmp(obj, best.objective) > 0 : Rcmp(obj, best.objective) < 0))) {
        best = { x: x.slice(), objective: obj };
      }
      pts.push({ x: x, feasible: ok, objective: obj, rows: rows });
      var p = n - 1;
      while (p >= 0 && counter[p] >= box[p][1]) { counter[p] = box[p][0]; p -= 1; }
      if (p < 0) break;
      counter[p] += 1n;
    }
    return { points: pts, truncated: false, total: total, best: best,
             feasibleCount: pts.filter(function (q) { return q.feasible; }).length };
  }

  /* The knapsack three ways in ONE call, because the lesson is the comparison:
     the LP relaxation with its one fractional item, what greed gets, and the
     exact optimum by enumeration.  Quoting any one of them alone is the
     mistake the mode exists to correct. */
  function knapsackExact(items, cap) {
    var n = items.length, i;
    var order = items.map(function (it, k) { return k; }).sort(function (a, b) {
      var ra = Rdiv(items[a].value, items[a].weight), rb = Rdiv(items[b].value, items[b].weight);
      var c = Rcmp(rb, ra);
      return c !== 0 ? c : a - b;
    });
    var left = cap, relax = R0, fractional = null, relaxTake = [], greedy = R0, greedySet = [], gLeft = cap;
    for (i = 0; i < n; i += 1) {
      var it = items[order[i]];
      if (Rcmp(it.weight, left) <= 0) {
        relax = Radd(relax, it.value); left = Rsub(left, it.weight);
        relaxTake.push({ item: order[i], part: R1 });
      } else if (Rsign(left) > 0 && fractional === null) {
        var part = Rdiv(left, it.weight);
        relax = Radd(relax, Rmul(it.value, part));
        fractional = { item: order[i], name: it.name, part: part };
        relaxTake.push({ item: order[i], part: part });
        left = R0;
      }
      if (Rcmp(it.weight, gLeft) <= 0) { greedy = Radd(greedy, it.value); gLeft = Rsub(gLeft, it.weight); greedySet.push(order[i]); }
    }
    var best = R0, bestSet = [];
    if (n <= 22) {
      var limit = 1 << n, mask, w, v, set;
      for (mask = 0; mask < limit; mask += 1) {
        w = R0; v = R0; set = [];
        for (i = 0; i < n; i += 1) {
          if (!(mask & (1 << i))) continue;
          w = Radd(w, items[i].weight); v = Radd(v, items[i].value); set.push(i);
        }
        if (Rcmp(w, cap) <= 0 && Rcmp(v, best) > 0) { best = v; bestSet = set; }
      }
    }
    return { relaxation: relax, fractionalItem: fractional, take: relaxTake,
             greedy: greedy, greedySet: greedySet, optimum: best, subset: bestSet,
             ratios: order.map(function (k) { return { item: k, name: items[k].name,
               ratio: Rdiv(items[k].value, items[k].weight) }; }),
             exhaustive: n <= 22, count: n <= 22 ? (1 << n) : null };
  }

  /* ---- the travelling salesman, at lesson size ------------------------- */

  /* Every distinct tour, the best of them, and how many there were.  Distinct
     means: city 0 is fixed, and on a SYMMETRIC matrix a tour and its reversal
     are the same tour, so the count is (n-1)!/2 rather than (n-1)!.  Getting
     that count wrong is how a lesson ends up claiming twice the work. */
  function tspExact(d, opts) {
    opts = opts || {};
    var n = d.length, i, j, symmetric = true;
    for (i = 0; i < n; i += 1) for (j = 0; j < n; j += 1) if (i !== j && !Requ(d[i][j], d[j][i])) symmetric = false;
    if (n > (opts.maxCities || 8)) {
      return { tours: [], best: null, count: null, truncated: true, symmetric: symmetric,
               why: 'this enumerates every tour and ' + n + ' cities is past the point where that is a drawing' };
    }
    var rest = [], tours = [], best = null;
    for (i = 1; i < n; i += 1) rest.push(i);
    var keep = opts.keepTours !== false;
    var go = function (used, acc) {
      if (acc.length === n - 1) {
        if (symmetric && acc.length > 1 && acc[0] > acc[acc.length - 1]) return;
        var cost = R0, prev = 0, k;
        for (k = 0; k < acc.length; k += 1) { cost = Radd(cost, d[prev][acc[k]]); prev = acc[k]; }
        cost = Radd(cost, d[prev][0]);
        var tour = [0].concat(acc, [0]);
        if (keep) tours.push({ tour: tour, cost: cost });
        if (best === null || Rcmp(cost, best.cost) < 0) best = { tour: tour, cost: cost };
        return;
      }
      for (var k2 = 0; k2 < rest.length; k2 += 1) {
        if (used[rest[k2]]) continue;
        used[rest[k2]] = true; acc.push(rest[k2]);
        go(used, acc);
        acc.pop(); used[rest[k2]] = false;
      }
    };
    go({}, []);
    return { tours: tours, best: best, count: keep ? tours.length : null,
             symmetric: symmetric, truncated: false };
  }

  /* Branch and bound with the ASSIGNMENT bound and subtour cuts -- Little's
     method.  The relaxation drops the "one cycle" requirement and keeps "each
     city entered once and left once", which is exactly the assignment problem
     `hungarian` already solves; when its answer happens to be a single cycle
     it is a tour and the bound is attained.  Otherwise the shortest subtour is
     forbidden one arc at a time, which is the branching. */
  /* The assignment relaxation: each city entered once and left once, with the
     "one cycle" requirement dropped.  Solved by a recursion over subsets of
     columns -- exact, and at the seven cities this mode caps at, instant.

     NOT by calling TRANS_JS's hungarian.  `integer` does not carry the
     transportation kit's blocks and a thirty-kilobyte dependency to get one
     number back is the wrong trade.  It is also a genuinely DIFFERENT
     algorithm, so when mathcheck holds the two to the same answer they agree
     by arithmetic rather than by sharing an implementation. */
  function assignMin(cost) {
    var n = cost.length, full = 1 << n, i, mask, j;
    var f = [], pick = [];
    for (i = 0; i <= n; i += 1) {
      var frow = [], prow = [];
      for (mask = 0; mask < full; mask += 1) { frow.push(null); prow.push(-1); }
      f.push(frow); pick.push(prow);
    }
    f[0][0] = R0;
    for (i = 0; i < n; i += 1) {
      for (mask = 0; mask < full; mask += 1) {
        if (f[i][mask] === null) continue;
        for (j = 0; j < n; j += 1) {
          if (mask & (1 << j)) continue;
          var next = mask | (1 << j), v = Radd(f[i][mask], cost[i][j]);
          if (f[i + 1][next] === null || Rcmp(v, f[i + 1][next]) < 0) { f[i + 1][next] = v; pick[i + 1][next] = j; }
        }
      }
    }
    var assignment = [], left = full - 1;
    for (i = 0; i < n; i += 1) assignment.push(-1);
    for (i = n; i > 0; i -= 1) { var c = pick[i][left]; assignment[i - 1] = c; left ^= (1 << c); }
    return { value: f[n][full - 1], assignment: assignment };
  }

  function tspBranch(d, opts) {
    opts = opts || {};
    var n = d.length, maxNodes = opts.maxNodes || 60, i, j;
    var big = R1;
    for (i = 0; i < n; i += 1) for (j = 0; j < n; j += 1) big = Radd(big, Rabs(d[i][j]));
    var withBans = function (bans) {
      var M = [], b;
      for (i = 0; i < n; i += 1) {
        var row = [];
        for (j = 0; j < n; j += 1) row.push(i === j ? big : d[i][j]);
        M.push(row);
      }
      for (b = 0; b < bans.length; b += 1) M[bans[b][0]][bans[b][1]] = big;
      return M;
    };
    var cycles = function (perm) {
      var seen = {}, out = [], k;
      for (k = 0; k < n; k += 1) {
        if (seen[k]) continue;
        var cyc = [], at = k;
        while (!seen[at]) { seen[at] = true; cyc.push(at); at = perm[at]; }
        out.push(cyc);
      }
      return out;
    };
    var nodes = [], open = [], best = null, bestTour = null, id = 0, refused = false;
    var make = function (bans, parent, label) {
      var h = assignMin(withBans(bans));
      var cy = cycles(h.assignment);
      var node = { id: id, parent: parent, bans: bans.slice(), label: label,
                   bound: h.value, assignment: h.assignment.slice(), cycles: cy,
                   tour: cy.length === 1, prunedBy: null,
                   depth: parent === null ? 0 : nodes[parent].depth + 1 };
      id += 1; nodes.push(node);
      return node;
    };
    open.push(make([], null, 'root').id);
    while (open.length) {
      if (nodes.length > maxNodes) { refused = true; break; }
      var nid = open.pop(), node = nodes[nid];
      if (best !== null && Rcmp(node.bound, best) >= 0) { node.prunedBy = 'bound'; continue; }
      if (Rcmp(node.bound, big) >= 0) { node.prunedBy = 'infeasible'; continue; }
      if (node.tour) {
        node.prunedBy = 'a complete tour';
        if (best === null || Rcmp(node.bound, best) < 0) {
          best = node.bound;
          var t = [0], at = node.assignment[0];
          while (at !== 0) { t.push(at); at = node.assignment[at]; }
          t.push(0); bestTour = t;
        }
        continue;
      }
      var shortest = node.cycles[0], k2;
      for (k2 = 1; k2 < node.cycles.length; k2 += 1) if (node.cycles[k2].length < shortest.length) shortest = node.cycles[k2];
      node.cut = shortest.slice();
      var kids = [];
      for (k2 = 0; k2 < shortest.length; k2 += 1) {
        var from = shortest[k2], to = node.assignment[from];
        var child = make(node.bans.concat([[from, to]]), node.id,
                         'ban ' + from + '->' + to);
        kids.push(child.id);
      }
      node.children = kids;
      for (k2 = kids.length - 1; k2 >= 0; k2 -= 1) open.push(kids[k2]);
    }
    return { nodes: nodes, best: best, tour: bestTour, refused: refused,
             counts: { explored: nodes.length },
             status: refused ? 'refused' : 'optimal' };
  }
"""


# ------------------------------------------------------------- scheduling

SCHED_JS = r"""
  /* Scheduling.  A job is {id, p, w, d} -- processing time, weight, due date --
     and a sequence is an array of indices into that list.  Needs NET_JS above
     it: jobShopAll and the crashing network are both scored by longestPath.

     The Greek in the spec does not survive as a JavaScript identifier, so the
     sums are sumC, sumWC and sumT, and Lmax / Tmax keep their names. */

  /* EVERY OBJECTIVE FROM ONE SEQUENCE IN ONE CALL.  C6 L1's whole point is
     that a schedule is not "good" or "bad" -- it is good at one objective and
     bad at another, and a reader who drags jobs around has to see all eight
     move at once or they will believe the first one they were shown. */
  function seqObjectives(seq, jobs) {
    var t = R0, rows = [], sumC = R0, sumWC = R0, sumT = R0, sumU = 0, k;
    var Lmax = null, Tmax = null;
    for (k = 0; k < seq.length; k += 1) {
      var j = jobs[seq[k]];
      t = Radd(t, j.p);
      var L = Rsub(t, j.d), T = Rsign(L) > 0 ? L : R0, U = Rsign(L) > 0 ? 1 : 0;
      sumC = Radd(sumC, t);
      sumWC = Radd(sumWC, Rmul(j.w === undefined ? R1 : j.w, t));
      sumT = Radd(sumT, T); sumU += U;
      if (Lmax === null || Rcmp(L, Lmax) > 0) Lmax = L;
      if (Tmax === null || Rcmp(T, Tmax) > 0) Tmax = T;
      rows.push({ pos: k, job: seq[k], id: j.id, p: j.p, d: j.d,
                  w: j.w === undefined ? R1 : j.w, C: t, L: L, T: T, U: U });
    }
    return { C: rows.map(function (r) { return r.C; }), rows: rows,
             sumC: sumC, sumWC: sumWC, sumT: sumT, sumU: sumU,
             Lmax: Lmax === null ? R0 : Lmax, Tmax: Tmax === null ? R0 : Tmax,
             makespan: t, seq: seq.slice() };
  }

  /* Swap the jobs at positions i and i + 1, and DECOMPOSE the difference
     exactly.  Only the two swapped jobs change completion time, so the whole
     of Smith's rule is one subtraction: sum wC moves by w_a p_b - w_b p_a, and
     that is negative exactly when p_a/w_a > p_b/w_b. */
  function adjacentSwap(seq, i, jobs) {
    var after = seq.slice(), t = after[i];
    after[i] = after[i + 1]; after[i + 1] = t;
    var a = jobs[seq[i]], b = jobs[seq[i + 1]];
    var wa = a.w === undefined ? R1 : a.w, wb = b.w === undefined ? R1 : b.w;
    var before = seqObjectives(seq, jobs), now = seqObjectives(after, jobs);
    var dC = Rsub(b.p, a.p), dWC = Rsub(Rmul(wa, b.p), Rmul(wb, a.p));
    return { seq: after, before: before, after: now,
             deltaSumC: dC, deltaSumWC: dWC,
             checkC: Requ(Rsub(now.sumC, before.sumC), dC),
             checkWC: Requ(Rsub(now.sumWC, before.sumWC), dWC),
             ratios: { a: Rdiv(a.p, wa), b: Rdiv(b.p, wb) },
             why: 'swapping ' + a.id + ' and ' + b.id + ' moves sum C by p_' + b.id + ' - p_' + a.id
               + ' = ' + Rtext(dC) + ' and sum wC by w_' + a.id + 'p_' + b.id + ' - w_' + b.id + 'p_'
               + a.id + ' = ' + Rtext(dWC) + '; nothing else in the schedule moves at all' };
  }

  /* Moore-Hodgson, one step at a time with the set discarded so far.  Take the
     jobs in due-date order; the moment the schedule is late, throw out the
     LONGEST job accepted so far -- not the late one, which is the swap a
     reader expects and the reason the algorithm is worth showing. */
  function mooreHodgson(jobs) {
    var order = jobs.map(function (_, k) { return k; }).sort(function (a, b) {
      var c = Rcmp(jobs[a].d, jobs[b].d);
      return c !== 0 ? c : a - b;
    });
    var kept = [], discarded = [], t = R0, steps = [], k;
    for (k = 0; k < order.length; k += 1) {
      var j = order[k];
      kept.push(j); t = Radd(t, jobs[j].p);
      var step = { job: j, id: jobs[j].id, added: true, time: t, removed: null,
                   kept: kept.slice(), discarded: discarded.slice(),
                   why: jobs[j].id + ' joins; the schedule now finishes at ' + Rtext(t)
                     + ' against a due date of ' + Rtext(jobs[j].d) };
      if (Rcmp(t, jobs[j].d) > 0) {
        var worst = kept[0], q;
        for (q = 1; q < kept.length; q += 1) if (Rcmp(jobs[kept[q]].p, jobs[worst].p) > 0) worst = kept[q];
        kept.splice(kept.indexOf(worst), 1);
        discarded.push(worst); t = Rsub(t, jobs[worst].p);
        step.removed = worst; step.removedId = jobs[worst].id; step.time = t;
        step.kept = kept.slice(); step.discarded = discarded.slice();
        step.why += '; that is late, so the LONGEST job accepted so far, ' + jobs[worst].id
          + ' at ' + Rtext(jobs[worst].p) + ', is thrown out and the finish drops to ' + Rtext(t);
      }
      steps.push(step);
    }
    var seq = kept.concat(discarded);
    return { seq: seq, kept: kept, discarded: discarded, steps: steps,
             sumU: discarded.length, objectives: seqObjectives(seq, jobs) };
  }

  /* Johnson's rule for two machines: everything faster on the first machine
     goes first, in increasing order of that time; everything else goes last,
     in decreasing order of its second time. */
  function johnsonRule(jobs) {
    var front = [], back = [], k;
    for (k = 0; k < jobs.length; k += 1) {
      if (Rcmp(jobs[k].p1, jobs[k].p2) < 0) front.push(k); else back.push(k);
    }
    front.sort(function (a, b) { var c = Rcmp(jobs[a].p1, jobs[b].p1); return c !== 0 ? c : a - b; });
    back.sort(function (a, b) { var c = Rcmp(jobs[b].p2, jobs[a].p2); return c !== 0 ? c : a - b; });
    var seq = front.concat(back);
    return { seq: seq, front: front, back: back, makespan: flowshopMakespan(seq, jobs),
             why: front.length + ' job(s) are quicker on machine 1 and go first in increasing p1; the rest go last in decreasing p2' };
  }
  /* The two-machine flow shop: machine 2 starts a job when both that job is
     off machine 1 and machine 2 is free.  The max is the whole idea. */
  function flowshopMakespan(seq, jobs) {
    var t1 = R0, t2 = R0, rows = [], k;
    for (k = 0; k < seq.length; k += 1) {
      var j = jobs[seq[k]];
      t1 = Radd(t1, j.p1);
      t2 = Radd(Rcmp(t1, t2) > 0 ? t1 : t2, j.p2);
      rows.push({ job: seq[k], id: j.id, off1: t1, off2: t2 });
    }
    return { value: t2, rows: rows };
  }

  /* The exhaustive optimum over all n! orders, and the COUNT, so a lesson can
     say what it cost to be sure.  `obj` is a key of seqObjectives, or a
     function of its result. */
  function bestSequence(jobs, obj, opts) {
    opts = opts || {};
    var n = jobs.length, cap = opts.maxJobs || 8;
    if (n > cap) return { seq: null, value: null, count: null, truncated: true,
                          why: n + ' jobs is ' + n + '! orders, past the point where checking them all is a demonstration' };
    var score = typeof obj === 'function' ? obj : function (o) { return o[obj]; };
    var best = null, bestSeq = null, ties = 0, count = 0;
    var go = function (used, acc) {
      if (acc.length === n) {
        count += 1;
        var o = seqObjectives(acc, jobs), v = score(o);
        var rv = typeof v === 'number' ? R(BigInt(v), 1n) : v;
        if (best === null || Rcmp(rv, best) < 0) { best = rv; bestSeq = acc.slice(); ties = 1; }
        else if (Requ(rv, best)) ties += 1;
        return;
      }
      for (var k = 0; k < n; k += 1) {
        if (used[k]) continue;
        used[k] = true; acc.push(k); go(used, acc); acc.pop(); used[k] = false;
      }
    };
    go({}, []);
    return { seq: bestSeq, value: best, count: count, ties: ties, truncated: false,
             objectives: seqObjectives(bestSeq, jobs) };
  }

  /* Parallel machines: what LPT gets, what the exhaustive optimum is, and BOTH
     lower bounds the 4/3 ratio is proved against.  The bounds matter more than
     the heuristic: a reader who has only seen the heuristic has no way to know
     whether a schedule is 5% off or 40%. */
  function parallelAssign(jobs, m, rule, opts) {
    opts = opts || {};
    var n = jobs.length, k, i;
    var order = jobs.map(function (_, q) { return q; }).sort(function (a, b) {
      var c = Rcmp(jobs[b].p, jobs[a].p);
      if (rule === 'SPT') c = Rcmp(jobs[a].p, jobs[b].p);
      return c !== 0 ? c : a - b;
    });
    var loads = [], assign = [], steps = [];
    for (i = 0; i < m; i += 1) loads.push(R0);
    for (k = 0; k < n; k += 1) assign.push(-1);
    for (k = 0; k < order.length; k += 1) {
      var pick = 0;
      for (i = 1; i < m; i += 1) if (Rcmp(loads[i], loads[pick]) < 0) pick = i;
      assign[order[k]] = pick; loads[pick] = Radd(loads[pick], jobs[order[k]].p);
      steps.push({ job: order[k], id: jobs[order[k]].id, machine: pick, load: loads[pick] });
    }
    var makespan = loads[0];
    for (i = 1; i < m; i += 1) if (Rcmp(loads[i], makespan) > 0) makespan = loads[i];
    var total = R0, maxP = R0;
    for (k = 0; k < n; k += 1) {
      total = Radd(total, jobs[k].p);
      if (Rcmp(jobs[k].p, maxP) > 0) maxP = jobs[k].p;
    }
    var avg = Rdiv(total, R(BigInt(m), 1n));
    var bound = Rcmp(avg, maxP) > 0 ? avg : maxP;
    var best = null, bestAssign = null, count = 0, truncated = false;
    if (Math.pow(m, n) <= (opts.maxStates || 20000)) {
      var cur = [];
      for (k = 0; k < n; k += 1) cur.push(0);
      while (true) {
        count += 1;
        var ld = [];
        for (i = 0; i < m; i += 1) ld.push(R0);
        for (k = 0; k < n; k += 1) ld[cur[k]] = Radd(ld[cur[k]], jobs[k].p);
        var ms = ld[0];
        for (i = 1; i < m; i += 1) if (Rcmp(ld[i], ms) > 0) ms = ld[i];
        if (best === null || Rcmp(ms, best) < 0) { best = ms; bestAssign = cur.slice(); }
        var p = n - 1;
        while (p >= 0 && cur[p] === m - 1) { cur[p] = 0; p -= 1; }
        if (p < 0) break;
        cur[p] += 1;
      }
    } else truncated = true;
    return { assign: assign, loads: loads, makespan: makespan, steps: steps, rule: rule || 'LPT',
             optimum: best, optimumAssign: bestAssign, count: count, truncated: truncated,
             bounds: { average: avg, longest: maxP, best: bound },
             ratio: best === null ? null : Rdiv(makespan, best),
             overBound: Rdiv(makespan, bound) };
  }

  /* The job shop, exhaustively.  `ops` is [{job, machine, dur}] in each job's
     own order.  Every pair of operations on the same machine must be oriented
     one way or the other; there are 2^k ways and this scores all of them by
     longestPath, counting the ones whose orientation creates a CYCLE -- a
     deadlock, which is a real answer and not an error. */
  function jobShopAll(ops, opts) {
    opts = opts || {};
    var k, i, j;
    var byJob = {}, byMachine = {};
    for (k = 0; k < ops.length; k += 1) {
      (byJob[ops[k].job] = byJob[ops[k].job] || []).push(k);
      (byMachine[ops[k].machine] = byMachine[ops[k].machine] || []).push(k);
    }
    var pairs = [];
    for (var mkey in byMachine) {
      if (!Object.prototype.hasOwnProperty.call(byMachine, mkey)) continue;
      var list = byMachine[mkey];
      for (i = 0; i < list.length; i += 1) for (j = i + 1; j < list.length; j += 1) pairs.push([list[i], list[j]]);
    }
    if (pairs.length > (opts.maxPairs || 12)) {
      return { best: null, orientations: [], cyclic: 0, critical: null, truncated: true,
               pairs: pairs.length,
               why: pairs.length + ' disjunctive pairs is 2^' + pairs.length + ' orientations, past what a page can enumerate' };
    }
    var nodes = ['S'].concat(ops.map(function (_, q) { return 'o' + q; })).concat(['T']);
    var base = [];
    for (var jkey in byJob) {
      if (!Object.prototype.hasOwnProperty.call(byJob, jkey)) continue;
      var chain = byJob[jkey];
      base.push({ from: 'S', to: 'o' + chain[0], cost: R0 });
      for (i = 1; i < chain.length; i += 1) {
        base.push({ from: 'o' + chain[i - 1], to: 'o' + chain[i], cost: ops[chain[i - 1]].dur });
      }
      base.push({ from: 'o' + chain[chain.length - 1], to: 'T', cost: ops[chain[chain.length - 1]].dur });
    }
    var out = [], best = null, cyclic = 0, total = 1 << pairs.length;
    for (var mask = 0; mask < total; mask += 1) {
      var arcs = base.slice();
      for (k = 0; k < pairs.length; k += 1) {
        var a = pairs[k][0], b = pairs[k][1];
        if (mask & (1 << k)) arcs.push({ from: 'o' + a, to: 'o' + b, cost: ops[a].dur });
        else arcs.push({ from: 'o' + b, to: 'o' + a, cost: ops[b].dur });
      }
      var lp = longestPath(nodes, arcs, 'S', 'T');
      if (lp.cycle) { cyclic += 1; out.push({ mask: mask, makespan: null, cyclic: true, cycle: lp.cycle }); continue; }
      out.push({ mask: mask, makespan: lp.value, cyclic: false, path: lp.path, arcs: lp.arcs });
      if (best === null || Rcmp(lp.value, best.makespan) < 0) best = { mask: mask, makespan: lp.value, path: lp.path, arcs: lp.arcs };
    }
    return { best: best, orientations: out, cyclic: cyclic, pairs: pairs,
             critical: best ? best.path : null, truncated: false, total: total };
  }

  /* The crashing LP, ready for stdForm.  Variables are a start time per
     activity, a crash amount per activity, and the project finish; the
     objective is the crash bill and the deadline is ONE right-hand side --
     which is why the exact time-cost curve is rhsCurve on that row rather than
     a second implementation of anything. */
  function crashModel(activities, deadline) {
    var n = activities.length, i, j, k;
    var ix = {}, names = [], obj = [], cons = [];
    for (i = 0; i < n; i += 1) ix[activities[i].id] = i;
    for (i = 0; i < n; i += 1) names.push('t_' + activities[i].id);
    for (i = 0; i < n; i += 1) names.push('y_' + activities[i].id);
    names.push('F');
    var nv = 2 * n + 1, rates = [];
    for (i = 0; i < nv; i += 1) obj.push(R0);
    for (i = 0; i < n; i += 1) {
      var a = activities[i];
      var span = Rsub(a.normal, a.crash);
      var rate = Rzero(span) ? R0 : Rdiv(Rsub(a.crashCost, a.normalCost), span);
      rates.push(rate);
      obj[n + i] = rate;
    }
    var zero = function () { var v = []; for (k = 0; k < nv; k += 1) v.push(R0); return v; };
    var hasSucc = [];
    for (i = 0; i < n; i += 1) hasSucc.push(false);
    for (i = 0; i < n; i += 1) {
      var ps = activities[i].pred || [];
      for (j = 0; j < ps.length; j += 1) {
        var u = ix[ps[j]], row = zero();
        row[u] = R1; row[i] = R(-1n, 1n); row[n + u] = R(-1n, 1n);
        cons.push({ a: row, rel: 'le', b: Rneg(activities[u].normal),
                    name: activities[u].id + ' must finish before ' + activities[i].id + ' starts' });
        hasSucc[u] = true;
      }
    }
    for (i = 0; i < n; i += 1) {
      if (hasSucc[i]) continue;
      var r2 = zero();
      r2[i] = R1; r2[n + i] = R(-1n, 1n); r2[nv - 1] = R(-1n, 1n);
      cons.push({ a: r2, rel: 'le', b: Rneg(activities[i].normal),
                  name: activities[i].id + ' must finish before the project does' });
    }
    for (i = 0; i < n; i += 1) {
      var r3 = zero();
      r3[n + i] = R1;
      cons.push({ a: r3, rel: 'le', b: Rsub(activities[i].normal, activities[i].crash),
                  name: activities[i].id + ' cannot be crashed past ' + Rtext(activities[i].crash) });
    }
    var r4 = zero();
    r4[nv - 1] = R1;
    var deadlineRow = cons.length;
    cons.push({ a: r4, rel: 'le', b: deadline, name: 'the project deadline' });
    var normalCost = R0;
    for (i = 0; i < n; i += 1) normalCost = Radd(normalCost, activities[i].normalCost);
    return { model: { max: false, names: names, obj: obj, cons: cons },
             deadlineRow: deadlineRow, rates: rates, normalCost: normalCost,
             names: names, activities: activities,
             why: 'the objective is only the crash bill; the normal cost of ' + Rtext(normalCost)
               + ' is paid whatever the deadline, so it shifts the curve and does not bend it' };
  }
"""


# ------------------------------------------------------- backward recursion

DPSEQ_JS = r"""
  /* Dynamic programming, backwards.  Needs algebra_systems.MATRIX_JS (for the
     exact fixed point) and sysdesign_core.HARMONIC_JS (for the secretary sum).

     Every table here is filled from the END, which is the half of the subject
     a reader finds strange and the half that makes it work: the value of being
     somewhere is the cost of the step plus the value of where it leads, and
     the only place that recursion bottoms out is the finish. */

  /* The stage-by-stage value table, with TIES KEPT.

     "The optimal policy is unique" is the misconception C7 L1 is built on, and
     the only way to refute it on a page is to carry every argmin rather than
     the first one found.  `stages` is an array of arrays of node ids, earliest
     first; `arcs` is [{from, to, cost}]. */
  function backwardStages(stages, arcs, opts) {
    opts = opts || {};
    var minimise = opts.maximise !== true;
    var f = {}, argmin = {}, ties = [], s, i, j;
    var last = stages[stages.length - 1];
    for (i = 0; i < last.length; i += 1) f[last[i]] = opts.terminal && opts.terminal[last[i]] !== undefined
      ? opts.terminal[last[i]] : R0;
    for (s = stages.length - 2; s >= 0; s -= 1) {
      for (i = 0; i < stages[s].length; i += 1) {
        var v = stages[s][i], best = null, picks = [];
        for (j = 0; j < arcs.length; j += 1) {
          if (arcs[j].from !== v || f[arcs[j].to] === undefined) continue;
          var val = Radd(arcs[j].cost, f[arcs[j].to]);
          var better = best === null || (minimise ? Rcmp(val, best) < 0 : Rcmp(val, best) > 0);
          if (better) { best = val; picks = [{ arc: j, to: arcs[j].to, value: val }]; }
          else if (Requ(val, best)) picks.push({ arc: j, to: arcs[j].to, value: val });
        }
        f[v] = best === null ? null : best;
        argmin[v] = picks;
        if (picks.length > 1) ties.push({ node: v, stage: s, picks: picks.slice() });
      }
    }
    /* Every optimal path, not one: the ties are the point. */
    var policy = [], start = stages[0];
    var walk = function (v, acc) {
      if (policy.length > 200) return;
      if (!argmin[v] || !argmin[v].length) { policy.push(acc.slice()); return; }
      for (var k = 0; k < argmin[v].length; k += 1) {
        acc.push(argmin[v][k].to); walk(argmin[v][k].to, acc); acc.pop();
      }
    };
    for (i = 0; i < start.length; i += 1) walk(start[i], [start[i]]);
    return { f: f, argmin: argmin, policy: policy, ties: ties,
             value: start.length === 1 ? f[start[0]] : null, stages: stages };
  }

  /* The finite-horizon stochastic recursion on exact rationals.
     P[a][i][j], r[a][i], T periods, V_T = 0 unless a terminal value is given. */
  function stochasticDp(states, acts, P, r, T, opts) {
    opts = opts || {};
    var maximise = opts.minimise !== true, n = states.length, a, i, j, t;
    var V = [], policy = [], table = [];
    var vT = [];
    for (i = 0; i < n; i += 1) vT.push(opts.terminal ? opts.terminal[i] : R0);
    V[T] = vT;
    for (t = T - 1; t >= 0; t -= 1) {
      var row = [], pol = [], detail = [];
      for (i = 0; i < n; i += 1) {
        var best = null, arg = -1, per = [];
        for (a = 0; a < acts.length; a += 1) {
          var v = r[a][i];
          for (j = 0; j < n; j += 1) v = Radd(v, Rmul(P[a][i][j], V[t + 1][j]));
          per.push({ act: a, name: acts[a], value: v });
          if (best === null || (maximise ? Rcmp(v, best) > 0 : Rcmp(v, best) < 0)) { best = v; arg = a; }
        }
        row.push(best); pol.push(arg);
        detail.push({ state: states[i], best: best, act: acts[arg], options: per });
      }
      V[t] = row; policy[t] = pol; table[t] = detail;
    }
    return { V: V, policy: policy, table: table, states: states, acts: acts, T: T };
  }

  /* ---- lot sizing ------------------------------------------------------ */

  /* Wagner-Whitin: the exact minimum-cost order plan.  F(t) is the cheapest
     way to cover periods 1..t, and the recursion is over the period the LAST
     order was placed in -- which works because an optimal plan never orders
     while stock remains, so every plan is a partition into order intervals. */
  function wagnerWhitin(demand, K, h) {
    var T = demand.length, F = [R0], from = [0], detail = [], t, j;
    for (t = 1; t <= T; t += 1) {
      var best = null, arg = -1, opts = [];
      for (j = 1; j <= t; j += 1) {
        var hold = R0, i;
        for (i = j; i <= t; i += 1) hold = Radd(hold, Rmul(R(BigInt(i - j), 1n), demand[i - 1]));
        var v = Radd(F[j - 1], Radd(K, Rmul(h, hold)));
        opts.push({ orderAt: j, value: v, holding: Rmul(h, hold), before: F[j - 1] });
        if (best === null || Rcmp(v, best) < 0) { best = v; arg = j; }
      }
      F.push(best); from.push(arg);
      detail.push({ t: t, value: best, orderAt: arg, options: opts });
    }
    var plan = [], t2 = T;
    while (t2 > 0) {
      var j2 = from[t2], q = R0, i2;
      for (i2 = j2; i2 <= t2; i2 += 1) q = Radd(q, demand[i2 - 1]);
      plan.unshift({ period: j2, quantity: q, covers: [j2, t2] });
      t2 = j2 - 1;
    }
    return { F: F, plan: plan, orders: plan.length, cost: F[T], detail: detail, from: from };
  }

  /* Silver-Meal (least average cost per PERIOD) and least-unit-cost (least
     average cost per UNIT), both traced, both measured against the exact
     answer.  They are different heuristics and they can disagree with each
     other as well as with Wagner-Whitin, which is the lesson. */
  function lotsizeHeuristics(demand, K, h) {
    var T = demand.length;
    var run = function (perUnit) {
      var t = 0, plan = [], steps = [], cost = R0;
      while (t < T) {
        var hold = R0, qty = R0, best = null, span = 1, k;
        var trail = [];
        for (k = 0; k + t < T; k += 1) {
          hold = Radd(hold, Rmul(R(BigInt(k), 1n), demand[t + k]));
          qty = Radd(qty, demand[t + k]);
          var total = Radd(K, Rmul(h, hold));
          var avg = perUnit ? (Rzero(qty) ? null : Rdiv(total, qty)) : Rdiv(total, R(BigInt(k + 1), 1n));
          trail.push({ periods: k + 1, total: total, average: avg, quantity: qty });
          if (avg === null) continue;
          if (best === null || Rcmp(avg, best) < 0) { best = avg; span = k + 1; }
          else break;                       /* the averages have turned up */
        }
        var q2 = R0, hold2 = R0;
        for (k = 0; k < span; k += 1) {
          q2 = Radd(q2, demand[t + k]);
          hold2 = Radd(hold2, Rmul(R(BigInt(k), 1n), demand[t + k]));
        }
        cost = Radd(cost, Radd(K, Rmul(h, hold2)));
        plan.push({ period: t + 1, quantity: q2, covers: [t + 1, t + span] });
        steps.push({ from: t + 1, span: span, trail: trail });
        t += span;
      }
      return { plan: plan, steps: steps, cost: cost, orders: plan.length };
    };
    var exact = wagnerWhitin(demand, K, h);
    var sm = run(false), luc = run(true);
    sm.gap = Rsub(sm.cost, exact.cost);
    luc.gap = Rsub(luc.cost, exact.cost);
    sm.excess = Rzero(exact.cost) ? null : Rdiv(sm.gap, exact.cost);
    luc.excess = Rzero(exact.cost) ? null : Rdiv(luc.gap, exact.cost);
    return { silverMeal: sm, leastUnitCost: luc, exact: exact };
  }

  /* ---- stopping -------------------------------------------------------- */

  /* Sell-or-wait with T periods left and a search cost c: the threshold in
     each period is the value of carrying on, and an offer is taken exactly
     when it beats that.  V(0) = 0; V(t) = E[max(x, V(t-1))] - c.

     An offer is money, so this pmf's VALUES are rationals -- unlike the
     integer-valued ones pmfConvolve builds for the inventory kit. */
  function stopThresholds(pmf, T, c) {
    var v = R0, rows = [], t, k;
    for (t = 1; t <= T; t += 1) {
      var e = R0;
      for (k = 0; k < pmf.length; k += 1) {
        var x = pmf[k][0], val = Rcmp(x, v) > 0 ? x : v;
        e = Radd(e, Rmul(pmf[k][1], val));
      }
      var next = Rsub(e, c);
      rows.unshift({ left: t, threshold: v, continuation: next,
                     accept: pmf.filter(function (p) { return Rcmp(p[0], v) > 0; })
                                .map(function (p) { return p[0]; }),
                     why: 'with ' + t + ' period(s) left, carrying on is worth ' + Rtext(next)
                       + ', so an offer is taken when it beats ' + Rtext(v) });
      v = next;
    }
    return { rows: rows, value: v, thresholds: rows.map(function (r) { return r.threshold; }) };
  }

  /* The secretary problem, exactly:
       P(success | r) = ((r-1)/n) * sum_{i=r}^{n} 1/(i-1),   and P(1) = 1/n.
     The sum is harmonic() from sysdesign_core.HARMONIC_JS, so the whole table
     is rational and the "1/e" a textbook quotes is the LIMIT beside it, not
     the answer -- it is n * expNegApprox(1), and it rounds. */
  function secretaryExact(n) {
    var probs = [], r, best = 1, bestP = R(1n, BigInt(n));
    probs.push({ r: 1, p: bestP });
    for (r = 2; r <= n; r += 1) {
      var sum = Rsub(harmonic(n - 1, 1), harmonic(r - 2, 1));
      var p = Rmul(R(BigInt(r - 1), BigInt(n)), sum);
      probs.push({ r: r, p: p });
      if (Rcmp(p, bestP) > 0) { bestP = p; best = r; }
    }
    return { probs: probs, best: best, bestP: bestP, n: n };
  }

  /* ---- decision trees -------------------------------------------------- */

  /* Fold a decision tree back to its root.  A node is
       {kind: 'leaf', value}
       {kind: 'chance',   children: [{p, node, label}]}
       {kind: 'decision', children: [{node, label}]}
     and every node comes back with the value it folded to.

     EVPI and EVSI need more than a tree -- they need to know WHICH states the
     chance nodes share -- so they are computed only when the tree carries a
     payoff matrix, a prior, and (for EVSI) a likelihood.  Returning null
     rather than a number invented from the tree's shape is the honest half. */
  function foldBack(tree) {
    var values = [], order = [];
    var fold = function (node, path) {
      var out = { node: node, path: path, kind: node.kind, label: node.label };
      if (node.kind === 'leaf') out.value = node.value;
      else if (node.kind === 'chance') {
        var e = R0, k;
        for (k = 0; k < node.children.length; k += 1) {
          var c = fold(node.children[k].node, path + '.' + k);
          e = Radd(e, Rmul(node.children[k].p, c.value));
        }
        out.value = e;
      } else {
        var best = null, arg = -1, k2;
        for (k2 = 0; k2 < node.children.length; k2 += 1) {
          var c2 = fold(node.children[k2].node, path + '.' + k2);
          if (best === null || Rcmp(c2.value, best) > 0) { best = c2.value; arg = k2; }
        }
        out.value = best; out.choice = arg; out.choiceLabel = node.children[arg].label;
      }
      values.push(out); order.push(path);
      return out;
    };
    var root = fold(tree.root || tree, '0');
    var evpi = null, evsi = null, perfect = null, priorBest = null;
    if (tree.payoff && tree.prior) {
      var A = tree.payoff.length, S = tree.prior.length, a, s;
      priorBest = null;
      for (a = 0; a < A; a += 1) {
        var v = R0;
        for (s = 0; s < S; s += 1) v = Radd(v, Rmul(tree.prior[s], tree.payoff[a][s]));
        if (priorBest === null || Rcmp(v, priorBest) > 0) priorBest = v;
      }
      perfect = R0;
      for (s = 0; s < S; s += 1) {
        var bs = null;
        for (a = 0; a < A; a += 1) if (bs === null || Rcmp(tree.payoff[a][s], bs) > 0) bs = tree.payoff[a][s];
        perfect = Radd(perfect, Rmul(tree.prior[s], bs));
      }
      evpi = Rsub(perfect, priorBest);
      if (tree.likelihood) {
        /* likelihood[signal][state] = P(signal | state) */
        var withInfo = R0, g;
        for (g = 0; g < tree.likelihood.length; g += 1) {
          var pg = R0, joint = [];
          for (s = 0; s < S; s += 1) {
            var jj = Rmul(tree.prior[s], tree.likelihood[g][s]);
            joint.push(jj); pg = Radd(pg, jj);
          }
          if (Rzero(pg)) continue;
          var bestA = null;
          for (a = 0; a < A; a += 1) {
            var v2 = R0;
            for (s = 0; s < S; s += 1) v2 = Radd(v2, Rmul(joint[s], tree.payoff[a][s]));
            if (bestA === null || Rcmp(v2, bestA) > 0) bestA = v2;
          }
          withInfo = Radd(withInfo, bestA);     /* already weighted by P(signal) */
        }
        evsi = Rsub(withInfo, priorBest);
      }
    }
    return { root: root, values: values, value: root.value,
             evpi: evpi, evsi: evsi, perfect: perfect, prior: priorBest };
  }

  /* Value iteration beside the exact fixed point.  v_{k+1} = r + gamma P v_k
     from v_0 = 0 -- with its denominators growing one power of gamma's
     denominator per step, which is worth SEEING -- against
     v* = (I - gamma P)^-1 r by Mrref, and the gap column between them. */
  function discountedValue(P, r, gamma, T) {
    var n = P.length, i, j, k;
    var v = [], iter = [];
    for (i = 0; i < n; i += 1) v.push(R0);
    iter.push(v.slice());
    for (k = 0; k < T; k += 1) {
      var nv = [];
      for (i = 0; i < n; i += 1) {
        var s = r[i];
        for (j = 0; j < n; j += 1) s = Radd(s, Rmul(gamma, Rmul(P[i][j], v[j])));
        nv.push(s);
      }
      v = nv; iter.push(v.slice());
    }
    var A = [];
    for (i = 0; i < n; i += 1) {
      var row = [];
      for (j = 0; j < n; j += 1) row.push(Rsub(i === j ? R1 : R0, Rmul(gamma, P[i][j])));
      row.push(r[i]);
      A.push(row);
    }
    var red = Mrref(A, { cols: n });
    var star = [];
    for (i = 0; i < n; i += 1) star.push(red.M[i][n]);
    var gap = [];
    for (i = 0; i < n; i += 1) gap.push(Rsub(v[i], star[i]));
    return { vT: v, v: star, gap: gap, iterations: iter, ops: red.ops,
             singular: red.rank !== n, system: A };
  }
"""


# ------------------------------ chains, decisions, and the birth-death queue

CHAIN_JS = r"""
  /* Markov chains, Markov decision processes, and the birth-death queue they
     all reduce to.  Needs algebra_systems.MATRIX_JS above it.

     A transition matrix is rows-sum-to-one over rationals, and everything here
     stays rational: P^12 on a five-state chain with denominator-20 entries has
     entries 15 digits over 16, which is exactly the size Number stops being
     able to hold and exactly where a lesson about long-run behaviour starts. */

  /* P^n by repeated multiplication.

     NOT NAMED Mpow.  algebra_basics.MONO_JS already defines Mpow -- and its
     own Mmul -- for MONOMIAL LISTS, and a kit concatenating both blocks would
     silently get the wrong one and report a plausible wrong matrix.  The
     collision is the reason for the name. */
  function chainPow(P, n) {
    var out = Mid(P.length), base = P.map(function (r) { return r.slice(); }), e = n;
    while (e > 0) {
      if (e & 1) out = Mmul(out, base);
      base = Mmul(base, base);
      e >>= 1;
    }
    return out;
  }

  /* Communicating classes, by reachability on the SUPPORT digraph: i leads to
     j when P[i][j] > 0, and i and j communicate when each leads to the other.
     A class is recurrent when nothing leaves it -- a chain that can leave and
     not come back is transient, which is a statement about arcs and not about
     probabilities. */
  function chainClasses(P) {
    var n = P.length, i, j, k;
    var reach = [];
    for (i = 0; i < n; i += 1) {
      var row = [];
      for (j = 0; j < n; j += 1) row.push(i === j || !Rzero(P[i][j]));
      reach.push(row);
    }
    for (k = 0; k < n; k += 1) for (i = 0; i < n; i += 1) for (j = 0; j < n; j += 1)
      if (reach[i][k] && reach[k][j]) reach[i][j] = true;
    var seen = [], classes = [];
    for (i = 0; i < n; i += 1) seen.push(false);
    for (i = 0; i < n; i += 1) {
      if (seen[i]) continue;
      var cls = [];
      for (j = 0; j < n; j += 1) if (reach[i][j] && reach[j][i]) { cls.push(j); seen[j] = true; }
      var closed = true, leaves = [];
      for (j = 0; j < cls.length; j += 1) {
        for (k = 0; k < n; k += 1) {
          if (Rzero(P[cls[j]][k]) || cls.indexOf(k) >= 0) continue;
          closed = false; leaves.push([cls[j], k]);
        }
      }
      classes.push({ states: cls, recurrent: closed, transient: !closed, leaves: leaves,
                     why: closed
                       ? 'nothing leaves {' + cls.join(',') + '}, so once the chain is in it, it stays: recurrent'
                       : 'from ' + (leaves.length ? leaves[0][0] + ' the chain can reach ' + leaves[0][1] : '')
                         + ' and not return, so {' + cls.join(',') + '} is transient' });
    }
    return { classes: classes, reach: reach,
             irreducible: classes.length === 1 };
  }

  /* The period of a class: the gcd of the lengths of every cycle through one
     of its states.  Computed by levelling the class from that state and taking
     the gcd of (level[u] + 1 - level[v]) over its arcs, which is the same
     number without enumerating cycles. */
  function chainPeriod(P, cls) {
    var inCls = {}, i, j;
    for (i = 0; i < cls.length; i += 1) inCls[cls[i]] = true;
    var level = {}, queue = [cls[0]], g = 0;
    level[cls[0]] = 0;
    while (queue.length) {
      var u = queue.shift();
      for (j = 0; j < P.length; j += 1) {
        if (Rzero(P[u][j]) || !inCls[j]) continue;
        if (level[j] === undefined) { level[j] = level[u] + 1; queue.push(j); }
        else {
          var d = level[u] + 1 - level[j];
          if (d < 0) d = -d;
          var a = g, b = d;
          while (b) { var t = a % b; a = b; b = t; }
          g = a;
        }
      }
    }
    return { period: g === 0 ? 1 : g, levels: level,
             aperiodic: (g === 0 ? 1 : g) === 1 };
  }

  /* pi P = pi with sum pi = 1.  The n balance equations are dependent -- their
     columns sum to the same thing -- so ONE of them is dropped by name and
     the normalisation takes its place.  `dropped` says which, because "we drop
     an equation" without saying which one is where a reader loses the thread. */
  function steadyState(P, dropIndex) {
    var n = P.length, i, j;
    var drop = dropIndex === undefined ? n - 1 : dropIndex;
    var A = [];
    for (j = 0; j < n; j += 1) {
      if (j === drop) continue;
      var row = [];
      for (i = 0; i < n; i += 1) row.push(Rsub(P[i][j], i === j ? R1 : R0));
      row.push(R0);
      A.push(row);
    }
    var last = [];
    for (i = 0; i < n; i += 1) last.push(R1);
    last.push(R1);
    A.push(last);
    var red = Mrref(A, { cols: n });
    var pi = [];
    for (i = 0; i < n; i += 1) pi.push(red.rank === n ? red.M[i][n] : null);
    var sum = R0;
    for (i = 0; i < n; i += 1) if (pi[i] !== null) sum = Radd(sum, pi[i]);
    return { system: A, dropped: drop, pi: pi, ops: red.ops, rank: red.rank,
             unique: red.rank === n, sum: sum,
             why: 'balance equation ' + (drop + 1) + ' is dropped because the n equations are dependent -- '
               + 'every column of P - I sums to zero -- and sum pi = 1 takes its place' };
  }

  /* An absorbing chain, in the canonical blocks.
       N = (I - Q)^-1  the expected visits to each transient state
       t = N 1         the expected steps before absorption
       B = N R         which absorbing state the chain ends in
     `partials` is I + Q + ... + Q^k beside N, because N is the SUM of those
     powers and a reader who has only been told the inverse formula has been
     told the answer without the reason. */
  function absorbing(P, abs, kmax) {
    var n = P.length, i, j, k;
    var isAbs = {}, trans = [];
    for (i = 0; i < abs.length; i += 1) isAbs[abs[i]] = true;
    for (i = 0; i < n; i += 1) if (!isAbs[i]) trans.push(i);
    var Q = [], Rm = [];
    for (i = 0; i < trans.length; i += 1) {
      var qr = [], rr = [];
      for (j = 0; j < trans.length; j += 1) qr.push(P[trans[i]][trans[j]]);
      for (j = 0; j < abs.length; j += 1) rr.push(P[trans[i]][abs[j]]);
      Q.push(qr); Rm.push(rr);
    }
    var m = trans.length;
    var IQ = Msub(Mid(m), Q);
    var red = Mrref(Maug(IQ, Mid(m)), { cols: m });
    var N = red.rank === m ? Mtake(red.M, m, m) : null;
    var t = null, Bm = null;
    if (N) {
      t = [];
      for (i = 0; i < m; i += 1) {
        var s = R0;
        for (j = 0; j < m; j += 1) s = Radd(s, N[i][j]);
        t.push(s);
      }
      Bm = Mmul(N, Rm);
    }
    var partials = [], acc = Mid(m), pw = Mid(m);
    partials.push(acc.map(function (r) { return r.slice(); }));
    for (k = 1; k <= (kmax === undefined ? 6 : kmax); k += 1) {
      pw = Mmul(pw, Q);
      acc = Madd(acc, pw);
      partials.push(acc.map(function (r) { return r.slice(); }));
    }
    return { Q: Q, R: Rm, N: N, t: t, B: Bm, partials: partials, ops: red.ops,
             transient: trans, absorbing: abs.slice(), singular: red.rank !== m };
  }

  /* ---- Markov decision processes --------------------------------------- */

  /* Evaluate ONE policy: v = r_pi + gamma P_pi v, solved exactly rather than
     iterated, so the page can show the iteration converging TO something. */
  function policyEvaluate(P, r, policy, gamma) {
    var n = policy.length, i, j;
    var Ppi = [], rpi = [];
    for (i = 0; i < n; i += 1) { Ppi.push(P[policy[i]][i].slice()); rpi.push(r[policy[i]][i]); }
    var A = [];
    for (i = 0; i < n; i += 1) {
      var row = [];
      for (j = 0; j < n; j += 1) row.push(Rsub(i === j ? R1 : R0, Rmul(gamma, Ppi[i][j])));
      row.push(rpi[i]);
      A.push(row);
    }
    var red = Mrref(A, { cols: n });
    var v = [];
    for (i = 0; i < n; i += 1) v.push(red.rank === n ? red.M[i][n] : null);
    return { system: A, v: v, ops: red.ops, Ppi: Ppi, rpi: rpi, singular: red.rank !== n };
  }

  /* Policy iteration: evaluate exactly, improve greedily, repeat.  It stops
     because there are finitely many policies and the value never decreases --
     which is a better reason than "the numbers stopped moving". */
  function policyIterate(P, r, gamma, opts) {
    opts = opts || {};
    var n = r[0].length, acts = P.length, i, a, j;
    var policy = opts.start ? opts.start.slice() : [];
    while (policy.length < n) policy.push(0);
    var rounds = [], guard = 0;
    while (guard < (opts.maxRounds || 20)) {
      guard += 1;
      var ev = policyEvaluate(P, r, policy, gamma);
      var next = [], improve = [];
      for (i = 0; i < n; i += 1) {
        var best = null, arg = policy[i], per = [];
        for (a = 0; a < acts; a += 1) {
          var q = r[a][i];
          for (j = 0; j < n; j += 1) q = Radd(q, Rmul(gamma, Rmul(P[a][i][j], ev.v[j])));
          per.push({ act: a, value: q });
          if (best === null || Rcmp(q, best) > 0) { best = q; arg = a; }
        }
        next.push(arg);
        improve.push({ state: i, was: policy[i], now: arg, q: per, best: best });
      }
      rounds.push({ policy: policy.slice(), v: ev.v.slice(), improve: improve, system: ev.system, ops: ev.ops });
      var same = true;
      for (i = 0; i < n; i += 1) if (next[i] !== policy[i]) same = false;
      policy = next;
      if (same) break;
    }
    /* A few value-iteration steps beside the exact answer, with their
       denominators growing one power of gamma's denominator per step.  Written
       out here rather than handed to DPSEQ_JS's discountedValue: `markov` does
       not carry that block, and ten lines is a better trade than fourteen
       kilobytes to get one column back. */
    var iteration = null;
    if (opts.valueSteps) {
      var best = rounds[rounds.length - 1].policy, v = [], iters = [], step;
      for (i = 0; i < n; i += 1) v.push(R0);
      iters.push(v.slice());
      for (step = 0; step < opts.valueSteps; step += 1) {
        var nv = [];
        for (i = 0; i < n; i += 1) {
          var acc = r[best[i]][i];
          for (j = 0; j < n; j += 1) acc = Radd(acc, Rmul(gamma, Rmul(P[best[i]][i][j], v[j])));
          nv.push(acc);
        }
        v = nv; iters.push(v.slice());
      }
      var gap = [];
      for (i = 0; i < n; i += 1) gap.push(Rsub(v[i], rounds[rounds.length - 1].v[i]));
      iteration = { vT: v, v: rounds[rounds.length - 1].v.slice(), gap: gap, iterations: iters };
    }
    return { rounds: rounds, policy: policy, v: rounds[rounds.length - 1].v,
             iterations: rounds.length, valueIteration: iteration };
  }

  /* ---- the birth-death queue ------------------------------------------- */

  /* THE KIT'S UNIFYING OBJECT.  Cut the chain between n and n + 1: what
     crosses upward must cross back down, so pi_{n+1} mu_{n+1} = pi_n lam_n,
     and every queue on this path is that one equation with different rates.
     M/M/1 is lam_n = lam, mu_n = mu; M/M/s is mu_n = min(n, s) mu, and Erlang
     C falls out of the same pi as a reading rather than a second formula.

     `lam[n]` is the arrival rate in state n, for n = 0 .. N - 1.
     `mu[n]`  is the service rate OUT OF state n + 1, that is mu_{n+1}.
     The chain therefore has states 0 .. N.

     `stable` answers the question about the UNTRUNCATED chain -- would this
     still be a distribution if the last pair of rates went on forever -- which
     is the question a reader is actually asking. */
  function birthDeath(lam, mu, opts) {
    opts = opts || {};
    var s = opts.servers === undefined ? 1 : opts.servers;
    var N = lam.length, n, ratios = [R1], cuts = [];
    for (n = 0; n < N; n += 1) {
      if (Rzero(mu[n])) break;
      ratios.push(Rmul(ratios[n], Rdiv(lam[n], mu[n])));
      cuts.push({ n: n, lam: lam[n], mu: mu[n], ratio: Rdiv(lam[n], mu[n]),
                  why: 'pi_' + (n + 1) + ' = pi_' + n + ' * ' + Rtext(lam[n]) + ' / ' + Rtext(mu[n])
                    + ' -- what crosses the cut between ' + n + ' and ' + (n + 1) + ' upward must cross back down' });
    }
    var total = R0;
    for (n = 0; n < ratios.length; n += 1) total = Radd(total, ratios[n]);
    var pi = ratios.map(function (v) { return Rdiv(v, total); });
    var L = R0, Lq = R0, lamEff = R0;
    for (n = 0; n < pi.length; n += 1) {
      L = Radd(L, Rmul(R(BigInt(n), 1n), pi[n]));
      if (n > s) Lq = Radd(Lq, Rmul(R(BigInt(n - s), 1n), pi[n]));
      if (n < lam.length) lamEff = Radd(lamEff, Rmul(pi[n], lam[n]));
    }
    var W = Rzero(lamEff) ? null : Rdiv(L, lamEff);
    var Wq = Rzero(lamEff) ? null : Rdiv(Lq, lamEff);
    var stable = N > 0 && !Rzero(mu[N - 1]) && Rcmp(lam[N - 1], mu[N - 1]) < 0;
    return { pi: pi, ratios: ratios, cuts: cuts, L: L, Lq: Lq, W: W, Wq: Wq,
             lambdaEffective: lamEff, servers: s, stable: stable,
             busy: Rsub(R1, pi[0]), states: pi.length,
             why: 'Little\'s Law closes the loop: L = ' + Rtext(L) + ' and the rate that actually gets in is '
               + Rtext(lamEff) + ', so W = L / lambda_eff' };
  }
"""


# ---------------------------------------- sample statistics that stay exact

SIM_JS = r"""
  /* Simulation output analysis, exactly.

     A simulation's numbers come from a SEEDED stream, so they are data and not
     noise, and every statistic of them is a ratio of integers.  Keeping them
     that way is what lets a page say "these two estimators have variances in
     the ratio 47/3" rather than showing two decimals a reader cannot check.

     Streams are NOT new and nothing here re-implements one: lcgStream,
     streamUniform and sampleFromPmf all ship in sysdesign_core.STREAM_JS, and
     inverse-transform sampling is C10 L1's whole lesson.  number.py's lcgRun
     is a CYCLE DETECTOR and is the wrong tool, but its hullDobell(a, c, m) is
     the right one for the full-period certificate the lesson prints beside the
     stream. */

  function sampleMean(xs) {
    if (!xs.length) return null;
    var s = R0, k;
    for (k = 0; k < xs.length; k += 1) s = Radd(s, xs[k]);
    return Rdiv(s, R(BigInt(xs.length), 1n));
  }
  /* n - 1 in the denominator, and the lesson says why: the sample mean is
     already fitted to the data, so one degree of freedom has been spent. */
  function sampleVar(xs) {
    var n = xs.length;
    if (n < 2) return null;
    var m = sampleMean(xs), s = R0, k;
    for (k = 0; k < n; k += 1) { var d = Rsub(xs[k], m); s = Radd(s, Rmul(d, d)); }
    return Rdiv(s, R(BigInt(n - 1), 1n));
  }
  function sampleCov(xs, ys) {
    var n = xs.length;
    if (n < 2 || ys.length !== n) return null;
    var mx = sampleMean(xs), my = sampleMean(ys), s = R0, k;
    for (k = 0; k < n; k += 1) s = Radd(s, Rmul(Rsub(xs[k], mx), Rsub(ys[k], my)));
    return Rdiv(s, R(BigInt(n - 1), 1n));
  }
  /* RHO SQUARED, NOT RHO.  rho is a covariance over a product of two square
     roots and is irrational at almost any data; rho^2 is a ratio of rationals
     and is the number every variance-reduction claim is actually about.  Only
     rho^2 is ever printed on this path. */
  function rhoSquared(xs, ys) {
    var c = sampleCov(xs, ys), vx = sampleVar(xs), vy = sampleVar(ys);
    if (c === null || Rzero(vx) || Rzero(vy)) return null;
    return Rdiv(Rmul(c, c), Rmul(vx, vy));
  }

  /* Chebyshev coverage, counted by comparing SQUARES.

     (xbar - mu)^2 >= k^2 * var  is the same statement as |xbar - mu| >= k*sd,
     and the first one takes no square root, so the count is exact.  The bound
     it is measured against is 1 - 1/k^2, also exact. */
  function chebyshevCover(reps, mu, k, variance) {
    var kk = Rmul(k, k), thresh = Rmul(kk, variance), rows = [], inside = 0, j;
    for (j = 0; j < reps.length; j += 1) {
      var d = Rsub(reps[j], mu), dd = Rmul(d, d), out = Rcmp(dd, thresh) >= 0;
      if (!out) inside += 1;
      rows.push({ rep: j, value: reps[j], squared: dd, outside: out,
                  why: Rtext(dd) + (out ? ' &gt;= ' : ' &lt; ') + Rtext(thresh) });
    }
    return { rows: rows, inside: inside, outside: reps.length - inside,
             coverage: Rdiv(R(BigInt(inside), 1n), R(BigInt(reps.length), 1n)),
             bound: Rsub(R1, Rinv(kk)), threshold: thresh,
             holds: Rcmp(Rdiv(R(BigInt(inside), 1n), R(BigInt(reps.length), 1n)), Rsub(R1, Rinv(kk))) >= 0 };
  }

  /* A single-server FIFO event calendar, as a list of per-event snapshots.

     The calendar is the lesson, not the averages: a reader who has watched the
     next-event clock JUMP over the idle time understands why a simulation is
     not a loop over seconds, and a reader shown only the mean wait does not. */
  function desRun(arrivals, services) {
    var n = arrivals.length, i;
    var starts = [], departs = [], free = R0;
    for (i = 0; i < n; i += 1) {
      var s = Rcmp(arrivals[i], free) > 0 ? arrivals[i] : free;
      starts.push(s); free = Radd(s, services[i]); departs.push(free);
    }
    var evs = [];
    for (i = 0; i < n; i += 1) {
      evs.push({ t: arrivals[i], kind: 'arrival', who: i });
      evs.push({ t: departs[i], kind: 'departure', who: i });
    }
    evs.sort(function (a, b) {
      var c = Rcmp(a.t, b.t);
      if (c !== 0) return c;
      if (a.kind !== b.kind) return a.kind === 'departure' ? -1 : 1;
      return a.who - b.who;
    });
    var inSystem = 0, events = [];
    for (i = 0; i < evs.length; i += 1) {
      inSystem += evs[i].kind === 'arrival' ? 1 : -1;
      events.push({ t: evs[i].t, kind: evs[i].kind, who: evs[i].who, inSystem: inSystem,
                    calendarAfter: evs.slice(i + 1).map(function (e) {
                      return { t: e.t, kind: e.kind, who: e.who }; }) });
    }
    var waits = [], sojourn = [];
    for (i = 0; i < n; i += 1) {
      waits.push(Rsub(starts[i], arrivals[i]));
      sojourn.push(Rsub(departs[i], arrivals[i]));
    }
    var busy = R0;
    for (i = 0; i < n; i += 1) busy = Radd(busy, services[i]);
    return { events: events, starts: starts, departs: departs, waits: waits,
             sojourn: sojourn, meanWait: sampleMean(waits), meanSojourn: sampleMean(sojourn),
             busy: busy, horizon: departs.length ? departs[n - 1] : R0,
             utilisation: departs.length && !Rzero(departs[n - 1]) ? Rdiv(busy, departs[n - 1]) : null };
  }

  /* Warm-up discard and batch means.  The discard is the honest half: an
     average over a run that started empty is an average of a system that was
     never in steady state, and the fix is to throw the beginning away and SAY
     how much. */
  function batchMeans(xs, w, b) {
    var kept = xs.slice(w), size = Math.floor(kept.length / b), out = [], k;
    if (size < 1) return { discarded: w, batches: [], means: [], size: 0,
                           why: 'after discarding ' + w + ' observations there are not enough left for ' + b + ' batches' };
    var batches = [];
    for (k = 0; k < b; k += 1) {
      var part = kept.slice(k * size, (k + 1) * size);
      batches.push(part); out.push(sampleMean(part));
    }
    return { discarded: w, kept: kept, batches: batches, means: out, size: size,
             grand: sampleMean(out), variance: sampleVar(out),
             naive: sampleMean(xs),
             why: 'the first ' + w + ' observations are thrown away and the rest split into '
               + b + ' batches of ' + size + '; a batch mean is much closer to independent than an observation is' };
  }

  /* The control-variate variance as an EXACT QUADRATIC in b.

     Var(X - b(C - mu_C)) = Var X - 2b Cov(X,C) + b^2 Var C, and b* = Cov/Var C
     is its vertex.  Returning the quadratic rather than only its minimum is
     what lets a reader drag b and watch the parabola, which is the mode. */
  function controlB(xs, cs) {
    var vx = sampleVar(xs), vc = sampleVar(cs), cov = sampleCov(xs, cs);
    if (vx === null || vc === null || Rzero(vc)) return { quadratic: null, bStar: null, varAt: null };
    var quad = [vx, Rneg(Rmul(R(2n, 1n), cov)), vc];     /* c0 + c1 b + c2 b^2 */
    var bStar = Rdiv(cov, vc);
    return { quadratic: quad, bStar: bStar, varAt: controlVarAt(quad, bStar),
             varRaw: vx, cov: cov, varC: vc, rho2: rhoSquared(xs, cs),
             reduction: Rzero(vx) ? null : Rdiv(Rsub(vx, controlVarAt(quad, bStar)), vx) };
  }
  function controlVarAt(quad, b) {
    return Radd(quad[0], Radd(Rmul(quad[1], b), Rmul(quad[2], Rmul(b, b))));
  }

  /* Importance sampling, with the refusal that makes it honest.

     The likelihood ratio p/q is undefined wherever q puts no mass and p does,
     and an estimator that quietly skips those outcomes is biased in a way no
     variance figure reveals.  So this REFUSES rather than returning a number.

     `p` and `q` are [value, rational] pairs over the same values, in the same
     order; `indicator` is a function of the value. */
  function importanceRun(p, q, indicator) {
    var k, rows = [], theta = R0, second = R0, refuse = null;
    for (k = 0; k < p.length; k += 1) {
      if (Rzero(q[k][1]) && !Rzero(p[k][1])) {
        refuse = { value: p[k][0],
                   why: 'q puts no mass on ' + Rtext(p[k][0]) + ' and p puts ' + Rtext(p[k][1])
                     + ' there; the likelihood ratio is undefined and an estimator that skips the outcome is biased, so there is no answer to give' };
        break;
      }
    }
    if (refuse) return { refused: true, why: refuse.why, at: refuse.value, rows: [],
                         estimate: null, varCrude: null, varIS: null, ratio: null };
    for (k = 0; k < p.length; k += 1) {
      var ind = indicator(p[k][0]) ? R1 : R0;
      var w = Rzero(q[k][1]) ? R0 : Rdiv(p[k][1], q[k][1]);
      theta = Radd(theta, Rmul(p[k][1], ind));
      if (!Rzero(ind)) second = Radd(second, Rmul(q[k][1], Rmul(Rmul(w, w), ind)));
      rows.push({ value: p[k][0], p: p[k][1], q: q[k][1], w: w, indicator: !Rzero(ind),
                  contribution: Rmul(q[k][1], Rmul(w, ind)) });
    }
    var varCrude = Rmul(theta, Rsub(R1, theta));
    var varIS = Rsub(second, Rmul(theta, theta));
    return { refused: false, rows: rows, estimate: theta,
             varCrude: varCrude, varIS: varIS,
             ratio: Rzero(varIS) ? null : Rdiv(varCrude, varIS),
             why: 'both estimators are unbiased for ' + Rtext(theta)
               + '; the whole difference is the variance' };
  }
"""


# ------------------------------------------------------------- inventory

INV_JS = r"""
  /* Inventory.  Needs algebra_core.SURD_JS (Rsurd, quadroots -- both already
     ship) and sysdesign_core.PMF_JS (pmfConvolve) above it.

     THE ECONOMIC ORDER QUANTITY IS A SQUARE ROOT AND THIS MODULE KEEPS IT AS
     ONE.  sqrt(2KD/h) for rational data is either rational or irrational, and
     the second case is the answer, not a failure: a page that prints
     282.842712474619 has replaced a fact a reader can check with a decimal
     they cannot.  The surd is carried as {q, k} meaning q*sqrt(k), every cost
     comparison below is exact, and only surdDec rounds -- at the point of
     printing, where the page says so. */

  /* Q* = sqrt(2KD/h) and the cost at it, C* = sqrt(2KDh).  Both exact. */
  function eoq(K, D, h) {
    var two = R(2n, 1n);
    return { Qsurd: Rsurd(Rdiv(Rmul(two, Rmul(K, D)), h)),
             costSurd: Rsurd(Rmul(two, Rmul(K, Rmul(D, h)))),
             K: K, D: D, h: h };
  }
  /* The cost at ANY rational Q, which is what makes the curve drawable and the
     "the EOQ is flat near its minimum" claim checkable. */
  function eoqCostAt(Q, K, D, h) {
    if (Rzero(Q)) return null;
    return Radd(Rdiv(Rmul(K, D), Q), Rdiv(Rmul(h, Q), R(2n, 1n)));
  }
  /* THE EOQ BY DISCRIMINANT.  "Is there a Q costing at most T" is
     hQ^2/2 - TQ + KD = 0, and its two roots are the ends of the interval that
     does.  They MERGE exactly when the discriminant is zero, that is at
     T = sqrt(2hKD) -- which is C*, derived rather than asserted.  The roots
     come from quadroots, which ships in algebra_core.SURD_JS. */
  function eoqDiscriminant(K, D, h, T) {
    var a = Rdiv(h, R(2n, 1n)), qr = quadroots(a, Rneg(T), Rmul(K, D));
    var star = eoq(K, D, h);
    return { disc: qr.disc, kind: qr.kind, roots: qr, target: T,
             merge: star.costSurd, atMinimum: Rzero(qr.disc),
             feasible: Rsign(qr.disc) >= 0,
             why: Rsign(qr.disc) < 0
               ? 'the discriminant is ' + Rtext(qr.disc) + ' &lt; 0: no order quantity costs as little as ' + Rtext(T)
               : (Rzero(qr.disc)
                  ? 'the discriminant is exactly 0, so the two roots have merged: ' + Rtext(T)
                    + ' is the minimum cost and the single Q that achieves it is the EOQ'
                  : 'the discriminant is ' + Rtext(qr.disc)
                    + ' &gt; 0, so an interval of order quantities costs at most ' + Rtext(T)) };
  }
  /* The robustness ratio: ordering t times the EOQ costs (t + 1/t)/2 times the
     minimum, whatever K, D and h were.  Exact at every rational t, and the
     reason a 20% error in Q costs under 2%. */
  function eoqRatio(t) {
    if (Rzero(t)) return null;
    return Rdiv(Radd(t, Rinv(t)), R(2n, 1n));
  }

  /* ---- comparing surd-valued costs, exactly --------------------------- */

  /* A cost of the form  r + q*sqrt(k)  -- a purchase bill plus an EOQ cost --
     compared without rounding.  Same radicand: one squaring settles it.
     Different radicands: both sides are BRACKETED by rationals from bifloor at
     growing precision until the brackets separate, which is a proof and not an
     approximation; identical numbers never separate and come back equal. */
  function surdValue(r, s) { return { r: r, s: s || { q: R0, k: 1n } }; }
  function surdBounds(v, p) {
    var scale = 10n ** BigInt(p);
    var lo = bifloor(v.s.k * scale * scale), hi = lo + 1n;
    var a = Rmul(v.s.q, R(lo, scale)), b = Rmul(v.s.q, R(hi, scale));
    var low = Rcmp(a, b) < 0 ? a : b, high = Rcmp(a, b) < 0 ? b : a;
    return [Radd(v.r, low), Radd(v.r, high)];
  }
  function surdValueCmp(A, Bv) {
    if (A.s.k === Bv.s.k) {
      var d = Rsub(A.r, Bv.r), e = Rsub(Bv.s.q, A.s.q);   /* sign of d - e sqrt(k) */
      if (Rzero(e)) return Rsign(d);
      var sd = Rsign(d), se = Rsign(e);
      if (sd >= 0 && se < 0) return (sd === 0 && se === 0) ? 0 : 1;
      if (sd <= 0 && se > 0) return -1;
      var l = Rmul(d, d), rr = Rmul(Rmul(e, e), R(A.s.k, 1n));
      var c = Rcmp(l, rr);
      return sd > 0 ? c : -c;
    }
    for (var p = 6; p <= 60; p += 12) {
      var a = surdBounds(A, p), b = surdBounds(Bv, p);
      if (Rcmp(a[0], b[1]) > 0) return 1;
      if (Rcmp(a[1], b[0]) < 0) return -1;
    }
    return 0;
  }

  /* All-units quantity discounts.  For each price band, the EOQ computed with
     THAT band's holding rate; when it falls inside the band it is a candidate,
     and when it does not, the band's own lower boundary is.  The curve is
     DISCONTINUOUS at every break -- the total cost drops as the price does --
     which is why the cheapest candidate is not the one with the smallest EOQ.

     `breaks` is [{from, price, h}], lowest `from` first; h defaults to the
     given h.  Costs are (purchase + ordering + holding) per unit time. */
  function discountCandidates(breaks, K, D, h) {
    var out = [], i;
    for (i = 0; i < breaks.length; i += 1) {
      var band = breaks[i], hb = band.h || h;
      var e = eoq(K, D, hb), q = e.Qsurd;
      var hiEdge = i + 1 < breaks.length ? breaks[i + 1].from : null;
      /* Is q inside [from, hiEdge)?  q is a surd: compare squares. */
      var qsq = Rmul(Rmul(q.q, q.q), R(q.k, 1n));
      var aboveFrom = Rcmp(qsq, Rmul(band.from, band.from)) >= 0;
      var belowTop = hiEdge === null || Rcmp(qsq, Rmul(hiEdge, hiEdge)) < 0;
      var buy = Rmul(D, band.price);
      var entry;
      if (aboveFrom && belowTop) {
        entry = { band: i, price: band.price, at: 'the EOQ', Qsurd: q, Q: null,
                  cost: surdValue(buy, e.costSurd), valid: true,
                  why: 'the EOQ for this price sits inside the band, so it is the band\'s best quantity' };
      } else {
        var Q = aboveFrom ? (hiEdge === null ? band.from : Rsub(hiEdge, R1)) : band.from;
        entry = { band: i, price: band.price, at: 'the band edge', Qsurd: null, Q: Q,
                  cost: surdValue(Radd(buy, eoqCostAt(Q, K, D, hb)), { q: R0, k: 1n }),
                  valid: true,
                  why: aboveFrom
                    ? 'the EOQ for this price is above the band, so the band\'s best quantity is its top'
                    : 'the EOQ for this price is below the band, so the band\'s best quantity is its floor of ' + Rtext(band.from) };
      }
      entry.from = band.from; entry.to = hiEdge;
      out.push(entry);
    }
    var best = null;
    for (i = 0; i < out.length; i += 1) {
      if (!out[i].valid) continue;
      if (best === null || surdValueCmp(out[i].cost, out[best].cost) < 0) best = i;
    }
    return { candidates: out, best: best, bestCost: best === null ? null : out[best].cost };
  }

  /* The economic PRODUCTION quantity, with planned backorders.

     Stock builds at P - D while producing and falls at D after, so the average
     on hand is scaled by f = 1 - D/P; backorders at cost pi per unit per time
     shift the sawtooth below zero.  Cost per unit time at any rational Q and
     backorder level b:
         KD/Q + h(fQ - b)^2 / (2fQ) + pi b^2 / (2fQ)
     With P infinite (f = 1) it IS the EOQ with backorders, and with b = 0 it
     IS the EPQ -- one formula, and the two named models are readings of it. */
  function epqCostAt(Q, b, K, D, h, P, pi) {
    if (Rzero(Q)) return null;
    var f = P === null ? R1 : Rsub(R1, Rdiv(D, P));
    if (Rsign(f) <= 0) return null;
    var fQ = Rmul(f, Q), two = R(2n, 1n);
    var on = Rsub(fQ, b);
    return Radd(Rdiv(Rmul(K, D), Q),
                Radd(Rdiv(Rmul(h, Rmul(on, on)), Rmul(two, fQ)),
                     Rzero(b) ? R0 : Rdiv(Rmul(pi, Rmul(b, b)), Rmul(two, fQ))));
  }
  function epqCost(K, D, h, P, b, pi) {
    var f = P === null ? R1 : Rsub(R1, Rdiv(D, P)), two = R(2n, 1n);
    if (Rsign(f) <= 0) {
      return { factor: f, feasible: false, Qsurd: null, costSurd: null,
               why: 'demand is at least the production rate, so the machine can never build stock and there is no cycle' };
    }
    var backlog = (pi && !Rzero(pi)) ? Rdiv(Radd(h, pi), pi) : R1;
    var Qstar = Rsurd(Rmul(Rdiv(Rmul(two, Rmul(K, D)), Rmul(h, f)), backlog));
    var Cstar = Rsurd(Rdiv(Rmul(two, Rmul(K, Rmul(D, Rmul(h, f)))), backlog));
    return { factor: f, feasible: true, Qsurd: Qstar, costSurd: Cstar,
             backlogFactor: backlog, bStar: Rmul(Rmul(f, Qstar.q), Rdiv(h, Radd(h, backlog === R1 ? h : pi))),
             why: 'the holding rate is scaled by 1 - D/P = ' + Rtext(f)
               + (pi && !Rzero(pi) ? ' and divided again by (h + pi)/pi = ' + Rtext(backlog)
                  + ', because a backorder is cheaper to carry than a unit of stock' : '') };
  }

  /* The newsvendor, by the critical ratio and by the whole cost curve.

     Q* is the smallest Q whose CDF reaches cu/(cu + co), and the expected cost
     at EVERY Q is tabulated beside it so the reader sees that the crossing is
     the minimum rather than being told.

     A pmf here is [integer value, rational probability] pairs, the same shape
     pmfConvolve produces, so newsvendor, reorderPoint and baseStock all read
     the same distribution. */
  function newsvendor(pmf, cu, co) {
    var ratio = Rdiv(cu, Radd(cu, co)), cum = R0, rows = [], k, j, star = null;
    for (k = 0; k < pmf.length; k += 1) {
      cum = Radd(cum, pmf[k][1]);
      var over = R0, under = R0, Q = pmf[k][0];
      for (j = 0; j < pmf.length; j += 1) {
        var d = pmf[j][0];
        if (d < Q) over = Radd(over, Rmul(pmf[j][1], R(BigInt(Q - d), 1n)));
        else under = Radd(under, Rmul(pmf[j][1], R(BigInt(d - Q), 1n)));
      }
      var cost = Radd(Rmul(co, over), Rmul(cu, under));
      rows.push({ Q: Q, p: pmf[k][1], cdf: cum, cost: cost,
                  overage: over, underage: under, reaches: Rcmp(cum, ratio) >= 0 });
      if (star === null && Rcmp(cum, ratio) >= 0) star = k;
    }
    var best = 0;
    for (k = 1; k < rows.length; k += 1) if (Rcmp(rows[k].cost, rows[best].cost) < 0) best = k;
    return { ratio: ratio, rows: rows, Q: star === null ? null : rows[star].Q,
             index: star, cheapest: rows[best].Q, cost: star === null ? null : rows[star].cost,
             agrees: star !== null && Requ(rows[star].cost, rows[best].cost),
             why: 'the critical ratio is ' + Rtext(ratio) + ' and the CDF first reaches it at Q = '
               + (star === null ? '(never)' : rows[star].Q) };
  }

  /* The reorder point: the expected shortage per cycle, exact.

     `pmf` is the demand in ONE period; the lead-time demand is the L-fold
     convolution of it, by pmfConvolve, which is the same function the latency
     course adds a serial chain with. */
  function reorderPoint(pmf, L, r) {
    var lead = pmf, k;
    for (k = 1; k < L; k += 1) lead = pmfConvolve(lead, pmf);
    var shortage = R0, service = R0, rows = [], demand = R0;
    for (k = 0; k < lead.length; k += 1) {
      var x = lead[k][0], p = lead[k][1];
      demand = Radd(demand, Rmul(R(BigInt(x), 1n), p));
      if (x > r) shortage = Radd(shortage, Rmul(p, R(BigInt(x - r), 1n)));
      else service = Radd(service, p);
      rows.push({ x: x, p: p, short: x > r ? x - r : 0 });
    }
    return { lead: lead, shortage: shortage, cycleService: service, rows: rows,
             r: r, meanDemand: demand, safety: Rsub(R(BigInt(r), 1n), demand),
             why: 'over ' + L + ' period(s) the expected demand is ' + Rtext(demand)
               + ', so a reorder point of ' + r + ' carries ' + Rtext(Rsub(R(BigInt(r), 1n), demand))
               + ' of safety stock and still runs short ' + Rtext(shortage) + ' units a cycle on average' };
  }

  /* Periodic review: the base-stock level covers R + L periods of demand,
     because an order placed now is the last one that can arrive before the
     NEXT order does.  The convolution is pmfConvolve, R + L times. */
  function baseStock(pmf, R_, L, alpha) {
    var lead = pmf, k;
    for (k = 1; k < R_ + L; k += 1) lead = pmfConvolve(lead, pmf);
    var cum = R0, rows = [], S = null, mean = R0;
    for (k = 0; k < lead.length; k += 1) {
      cum = Radd(cum, lead[k][1]);
      mean = Radd(mean, Rmul(R(BigInt(lead[k][0]), 1n), lead[k][1]));
      rows.push({ x: lead[k][0], p: lead[k][1], cdf: cum });
      if (S === null && alpha !== undefined && Rcmp(cum, alpha) >= 0) S = lead[k][0];
    }
    return { demand: lead, rows: rows, periods: R_ + L, S: S, alpha: alpha === undefined ? null : alpha,
             mean: mean,
             why: 'the order placed now covers ' + (R_ + L) + ' periods -- ' + R_
               + ' until the next review plus ' + L + ' of lead time -- so it is that convolution that has to be quantiled, not one period\'s' };
  }
"""


__all__ = ["ORFMT_JS", "TABLEAU_JS", "PHASE_JS", "DUAL_JS", "RANGE_JS",
           "NET_JS", "TRANS_JS", "IP_JS", "SCHED_JS", "DPSEQ_JS", "CHAIN_JS",
           "SIM_JS", "INV_JS"]
