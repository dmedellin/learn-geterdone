"""itakit_b -- family B of the Introduction to Algorithms kit: structures and tables.

Specified in docs/intro-algorithms/PLAN.md section D (family B); the seam with
family A (itakit.py: the entry point, the shared ITA_CORE_JS and modes growth to
fft) is docs/intro-algorithms/kit-contract.md; the report an author configures a
lesson from is the "Family B" section of docs/intro-algorithms/kit-report.md.
Nine modes:

  rod        (rdi)  cut                       CLRS 15.1
  lcs        (lci)  table                     CLRS 15.4
  obst       (obi)  table                     CLRS 15.5
  amortized  (ami)  counter, stack, table     CLRS 17.1-17.4
  rbtree     (rbi)  check, insert             CLRS 13.1-13.3
  btree      (bti)  insert                    CLRS 18.2
  fibheap    (fhi)  ops, cascade              CLRS 19.1-19.4
  veb        (vbi)  ops                       CLRS 20.2-20.3
  bfs        (bfi)  search                    CLRS 22.2

Each mode has one base block <PREFIX>_JS defining the pure function
<prefix>Compute(view, inst, opts), which scripts/mathcheck.js calls (section
"itakit (Introduction to Algorithms), family B"), and one block per view. A page
ships the base block and its own view's block only. Every procedure follows the
semantics of the book's procedure it names; where the book leaves a choice open
(where a root goes in a Fibonacci heap's root list, proto-vEB deletion) the
view's rules text states the choice the lab makes.

THE INSTANCES ARE THE LESSON'S. No price list, string, probability, key
sequence or graph is a constant here: every one arrives in a preset. Nothing
typed is evaluated as script.

IDS. Every JS function and variable and every element id begins with its mode's
prefix (the PLAN's two letters plus i, kit-contract.md section 0). Grepped
against scripts/mathpath/labs/*.py on 2026-10-31: none is used by another kit.
"""

from . import eakit_core as ea
from .itakit import mode_lab

# ---------------------------------------------------------------------------
# rod (rdi): rod cutting, CLRS 15.1
# ---------------------------------------------------------------------------

RDI_JS = r"""
  var RDI_VIEW = {};
  function rdiCompute(view, inst, opts) { return eaRun(RDI_VIEW[view], inst, opts); }
"""

RDI_VIEW_JS = {}

RDI_VIEW_JS["cut"] = r"""
  RDI_VIEW.cut = function (inst) {
    var p = inst.prices, n = p.length, r = [R0], s = [0], inner = 0, rows = [], j, i, q, v;
    /* EXTENDED-BOTTOM-UP-CUT-ROD: a strictly larger revenue replaces q, so a
       tie keeps the smallest first piece. */
    for (j = 1; j <= n; j += 1) {
      q = null;
      for (i = 1; i <= j; i += 1) {
        inner += 1;
        v = Radd(p[i - 1], r[j - i]);
        if (q === null || Rcmp(q, v) < 0) { q = v; s[j] = i; }
      }
      r[j] = q;
    }
    /* MEMOIZED-CUT-ROD-AUX, run, every call counted (the first included). */
    var memo = [], calls = 0;
    function rdiAux(m) {
      calls += 1;
      if (memo[m] !== undefined) return memo[m];
      var best = m === 0 ? R0 : null, k, t;
      for (k = 1; k <= m; k += 1) {
        t = Radd(p[k - 1], rdiAux(m - k));
        if (best === null || Rcmp(best, t) < 0) best = t;
      }
      memo[m] = best;
      return best;
    }
    if (!Requ(rdiAux(n), r[n])) throw new Error('rod: the memoized and bottom-up revenues differ');
    function rdiPieces(len) { var out = []; while (len > 0) { out.push(s[len]); len -= s[len]; } return out; }
    for (j = 1; j <= n; j += 1) {
      rows.push([String(j), eaNum(p[j - 1]), eaNum(r[j]), String(s[j]), rdiPieces(j).join(' + ')]);
    }
    var pieces = rdiPieces(n);
    return {
      tiles: { rdiRevenue: eaNum(r[n]), rdiCuts: pieces.length === 1 ? n + ' (no cut)' : pieces.join(' + '),
        rdiNaive: eaInt(2n ** BigInt(n)), rdiWays: eaInt(2n ** BigInt(n - 1)), rdiMemo: eaInt(calls), rdiInner: eaInt(inner) },
      status: 'A rod of length ' + n + ' sells for at most ' + eaNum(r[n]) + ' cut as ' + pieces.join(' + ') + '. '
        + 'CUT-ROD would make ' + eaInt(2n ** BigInt(n)) + ' calls; the lab computes that count and does not run them. '
        + 'The memoized routine made ' + eaInt(calls) + ' and the bottom-up loop ran its body ' + eaInt(inner) + ' times.',
      table: { caption: 'Each length j: its price, the best revenue r_j and the first piece s_j',
        head: ['j', 'p_j', 'r_j', 's_j', 'cut as'], rows: rows }
    };
  };
"""

# ---------------------------------------------------------------------------
# lcs (lci): longest common subsequence, CLRS 15.4
# ---------------------------------------------------------------------------

LCI_JS = r"""
  var LCI_VIEW = {};
  function lciCompute(view, inst, opts) { return eaRun(LCI_VIEW[view], inst, opts); }
  var LCI_MAX = 30, LCI_SHOW = 15;
"""

LCI_VIEW_JS = {}

LCI_VIEW_JS["table"] = r"""
  LCI_VIEW.table = function (inst) {
    var x = inst.x, y = inst.y, m = x.length, n = y.length, i, j;
    if (m > LCI_MAX) eaRefuse('X has ' + m + ' characters; this lab takes at most ' + LCI_MAX);
    if (n > LCI_MAX) eaRefuse('Y has ' + n + ' characters; this lab takes at most ' + LCI_MAX);
    var c = [], b = [], count = { d: 0, u: 0, l: 0 };
    for (i = 0; i <= m; i += 1) { c.push([]); b.push([]); for (j = 0; j <= n; j += 1) { c[i].push(0); b[i].push(''); } }
    /* LCS-LENGTH: a match goes diagonally; otherwise up when c[i-1,j] >= c[i,j-1], else left. */
    for (i = 1; i <= m; i += 1) {
      for (j = 1; j <= n; j += 1) {
        if (x.charAt(i - 1) === y.charAt(j - 1)) { c[i][j] = c[i - 1][j - 1] + 1; b[i][j] = '↖'; count.d += 1; }
        else if (c[i - 1][j] >= c[i][j - 1]) { c[i][j] = c[i - 1][j]; b[i][j] = '↑'; count.u += 1; }
        else { c[i][j] = c[i][j - 1]; b[i][j] = '←'; count.l += 1; }
      }
    }
    /* PRINT-LCS's walk back from (m, n). */
    var on = {}, out = [];
    i = m; j = n;
    while (i > 0 && j > 0) {
      on[i + ',' + j] = true;
      if (b[i][j] === '↖') { out.unshift(x.charAt(i - 1)); i -= 1; j -= 1; }
      else if (b[i][j] === '↑') i -= 1;
      else j -= 1;
    }
    var table = null;
    if (m <= LCI_SHOW && n <= LCI_SHOW) {
      var head = ['i  x_i', 'j = 0'], rows = [], row;
      for (j = 1; j <= n; j += 1) head.push(j + ' ' + y.charAt(j - 1));
      for (i = 0; i <= m; i += 1) {
        row = [i === 0 ? '0' : i + ' ' + x.charAt(i - 1)];
        for (j = 0; j <= n; j += 1) {
          var cell = String(c[i][j]) + b[i][j];
          row.push(on[i + ',' + j] ? '[' + cell + ']' : cell);
        }
        rows.push(row);
      }
      table = { caption: 'The c table with the b arrows; the cells PRINT-LCS walks through are in brackets', head: head, rows: rows };
    }
    var lcs = out.join('');
    return {
      tiles: { lciLength: eaInt(c[m][n]), lciLcs: lcs === '' ? '(empty)' : lcs,
        lciCells: m + ' × ' + n + ' = ' + eaInt(m * n), lciArrows: '↖ ' + count.d + ', ↑ ' + count.u + ', ← ' + count.l },
      status: 'LCS-LENGTH filled ' + eaInt(m * n) + ' cells; PRINT-LCS read ' + (lcs === '' ? 'no common subsequence' : lcs)
        + ' off the arrows. Another longest common subsequence may exist: the tie rule decides which one is printed.'
        + (table ? '' : ' The table is printed when both strings have at most ' + LCI_SHOW + ' characters.'),
      table: table
    };
  };
"""

# ---------------------------------------------------------------------------
# obst (obi): optimal binary search trees, CLRS 15.5
# ---------------------------------------------------------------------------

OBI_JS = r"""
  var OBI_VIEW = {};
  function obiCompute(view, inst, opts) { return eaRun(OBI_VIEW[view], inst, opts); }
  var OBI_BRUTE = 7;
"""

OBI_VIEW_JS = {}

OBI_VIEW_JS["table"] = r"""
  OBI_VIEW.table = function (inst) {
    var n = inst.p.length, sc = inst.scale, i, j, l, r, t;
    if (inst.q.length !== n + 1) {
      eaRefuse('There ' + (n === 1 ? 'is 1 key' : 'are ' + n + ' keys') + ', so there are ' + (n + 1)
        + ' dummy probabilities q0 to q' + n + ', and ' + inst.q.length + (inst.q.length === 1 ? ' is' : ' are') + ' given');
    }
    var p = [null].concat(inst.p.map(function (v) { return Rdiv(v, sc); })), q = inst.q.map(function (v) { return Rdiv(v, sc); });
    var total = Radd(eaSum(p.slice(1)), eaSum(q));
    if (!Requ(total, R1)) eaRefuse('The probabilities sum to ' + eaNum(total) + ', not 1');
    /* OPTIMAL-BST: e[i][j], w[i][j] for 1 <= i <= n+1, i-1 <= j <= n; a
       strictly smaller cost replaces the root, so a tie keeps the smallest r. */
    var e = [], w = [], root = [];
    for (i = 1; i <= n + 1; i += 1) { e[i] = []; w[i] = []; root[i] = []; e[i][i - 1] = q[i - 1]; w[i][i - 1] = q[i - 1]; }
    for (l = 1; l <= n; l += 1) {
      for (i = 1; i <= n - l + 1; i += 1) {
        j = i + l - 1;
        e[i][j] = null;
        w[i][j] = Radd(Radd(w[i][j - 1], p[j]), q[j]);
        for (r = i; r <= j; r += 1) {
          t = Radd(Radd(e[i][r - 1], e[r + 1][j]), w[i][j]);
          if (e[i][j] === null || Rcmp(t, e[i][j]) < 0) { e[i][j] = t; root[i][j] = r; }
        }
      }
    }
    function obiText(a, b) {
      if (b === a - 1) return 'd' + b;
      var k = root[a][b];
      return 'k' + k + '(' + obiText(a, k - 1) + ' ' + obiText(k + 1, b) + ')';
    }
    /* Brute force: every binary search tree on the keys, each costed from its
       own depths, sum over keys and dummies of (depth + 1) x probability. */
    var brute;
    if (n <= OBI_BRUTE) {
      var obiAll = function (a, b, d) {
        if (b === a - 1) return [Rmul(R(BigInt(d + 1)), q[a - 1])];
        var out = [], k, L, Rr, x, y, here;
        for (k = a; k <= b; k += 1) {
          L = obiAll(a, k - 1, d + 1); Rr = obiAll(k + 1, b, d + 1);
          here = Rmul(R(BigInt(d + 1)), p[k]);
          for (x = 0; x < L.length; x += 1) for (y = 0; y < Rr.length; y += 1) out.push(Radd(here, Radd(L[x], Rr[y])));
        }
        return out;
      };
      var all = obiAll(1, n, 0), best = all[0], ties = 0;
      all.forEach(function (v) { if (Rcmp(v, best) < 0) best = v; });
      all.forEach(function (v) { if (Requ(v, best)) ties += 1; });
      brute = eaInt(all.length) + ' trees; least ' + eaNum(best) + ' (' + eaPlural(ties, 'tree', 'trees') + '); '
        + (Requ(best, e[1][n]) ? 'agrees' : 'DISAGREES');
    } else {
      brute = 'not run at n = ' + n + ' (the lab enumerates trees up to n = ' + OBI_BRUTE + ')';
    }
    var rows = [], roots = [];
    for (i = 1; i <= n; i += 1) {
      var line = [];
      for (j = i; j <= n; j += 1) line.push(root[i][j]);
      roots.push(i + ': ' + line.join(' '));
    }
    for (l = 0; l <= n; l += 1) {
      for (i = 1; i <= n - l + 1; i += 1) {
        j = i + l - 1;
        rows.push([String(i), String(j), eaNum(w[i][j]), eaNum(e[i][j]), j >= i ? 'k' + root[i][j] : '—']);
      }
    }
    return {
      tiles: { obiCost: eaNum(e[1][n]), obiTree: obiText(1, n), obiRoots: roots.join('; '), obiBrute: brute },
      status: 'The expected search cost of the optimal tree is e[1,' + n + '] = ' + eaNum(e[1][n])
        + ', counting one for every node a search visits, the dummy leaf it ends at included.',
      table: { caption: 'Each subproblem (i, j), shortest first: its weight w, its cost e and its root', head: ['i', 'j', 'w[i,j]', 'e[i,j]', 'root'], rows: rows }
    };
  };
"""

# ---------------------------------------------------------------------------
# amortized (ami): the binary counter, the multipop stack, the dynamic table, CLRS 17
# ---------------------------------------------------------------------------

AMI_JS = r"""
  var AMI_VIEW = {}, AMI_ROWS = 60, AMI_OPS = 1000;
  function amiCompute(view, inst, opts) { return eaRun(AMI_VIEW[view], inst, opts); }
  /* Read an operation list: each word from `words`, a whole number after a word
     in `repeat` repeats it, a whole number after a word in `needs` is its
     argument (required). Returns [{op, k}], one entry an operation. */
  function amiOps(toks, words, repeat, needs) {
    var out = [], i = 0, t, n, what = 'Operations';
    var isNum = function (s) { return /^\d+$/.test(s); };
    while (i < toks.length) {
      t = toks[i];
      if (isNum(t)) eaRefuse(what + ', entry ' + (i + 1) + ': "' + t + '" follows no ' + repeat.concat(needs).join(' or '));
      if (words.indexOf(t) < 0) eaRefuse(what + ', entry ' + (i + 1) + ': "' + t + '" should be ' + words.slice(0, -1).join(', ') + ' or ' + words[words.length - 1]);
      n = null;
      if (i + 1 < toks.length && isNum(toks[i + 1])) { n = Number(toks[i + 1]); i += 1; }
      if (n !== null && (n < 1 || n > AMI_OPS)) eaRefuse(what + ', entry ' + (i + 1) + ': the number after ' + t + ' is from 1 to ' + AMI_OPS + ', and it is ' + toks[i]);
      if (needs.indexOf(t) >= 0) {
        if (n === null) eaRefuse(what + ', entry ' + (i + 1) + ': ' + t + ' needs a number after it');
        out.push({ op: t, k: n });
      } else {
        for (var r = 0; r < (n === null ? 1 : n); r += 1) out.push({ op: t, k: null });
      }
      if (out.length > AMI_OPS) eaRefuse(what + ': this lab runs at most ' + AMI_OPS + ' operations, and these are more');
      i += 1;
    }
    return out;
  }
  function amiShown(rows) { return rows.length > AMI_ROWS ? rows.slice(0, AMI_ROWS) : rows; }
  function amiMore(rows) { return rows.length > AMI_ROWS ? ' The table shows the first ' + AMI_ROWS + ' of ' + eaInt(rows.length) + ' operations.' : ''; }
"""

AMI_VIEW_JS = {}

AMI_VIEW_JS["counter"] = r"""
  AMI_VIEW.counter = function (inst) {
    var k = Number(inst.bits.n), n = Number(inst.increments.n), x = inst.start.n, top = 2n ** BigInt(k);
    if (x >= top) eaRefuse('A ' + k + '-bit counter holds 0 to ' + eaInt(top - 1n) + ', and the start is ' + eaInt(x));
    var A = [], ones = 0, b, i;
    for (b = 0; b < k; b += 1) { A.push(Number((x >> BigInt(b)) & 1n)); ones += A[b]; }
    var phi0 = ones, total = 0, amort = 0, credit = 0, low = 0, most = null, per = [], rows = [];
    for (b = 0; b < k; b += 1) per.push(0);
    var bits = function () { var s = ''; for (var q = k - 1; q >= 0; q -= 1) s += A[q]; return s; };
    for (var op = 1; op <= n; op += 1) {
      /* INCREMENT: reset the low run of 1s, then set the first 0 (none when every bit is 1). */
      i = 0;
      while (i < k && A[i] === 1) { A[i] = 0; per[i] += 1; i += 1; }
      var resets = i, set = i < k ? 1 : 0;
      if (set) { A[i] = 1; per[i] += 1; }
      var c = resets + set, before = ones;
      ones = ones - resets + set;
      var a = c + ones - before;
      total += c; amort += a; credit += 2 * set - c;
      if (credit < low) low = credit;
      if (most === null || a > most) most = a;
      rows.push([String(op), bits(), String(resets), String(set), String(c), String(ones), String(a), eaInt(credit)]);
    }
    var perText = per.map(function (f, q) { return 'bit ' + q + ': ' + eaInt(f); }).join(', ');
    return {
      tiles: { amiActual: eaInt(total), amiPerBit: perText, amiBound: '2n = ' + eaInt(2 * n),
        amiCredit: eaInt(credit) + ' (least ' + eaInt(low) + ')', amiPhi: 'Φ0 = ' + phi0 + ', Φn = ' + ones,
        amiAmortized: eaInt(amort), amiMax: eaInt(most), amiValue: eaInt(BigInt('0b' + bits())) + ' (' + bits() + ')' },
      status: eaPlural(n, 'increment', 'increments') + ' flipped ' + eaPlural(total, 'bit', 'bits') + ' in all.'
        + (x === 0n ? ' From 0, bit i flips once every 2^i increments, so the total is below 2n.'
          : ' The counter did not start at 0: the aggregate bound 2n and the accounting assume it does; the potential method gives total ≤ 2n − Φn + Φ0 = ' + eaInt(2 * n - ones + phi0) + '.')
        + amiMore(rows),
      table: { caption: 'Each INCREMENT: the bits after it (highest first), its cost, Φ after it, its amortized cost and the credit',
        head: ['op', 'bits', 'reset', 'set', 'actual', 'Φ', 'amortized', 'credit'], rows: amiShown(rows) }
    };
  };
"""

AMI_VIEW_JS["stack"] = r"""
  AMI_VIEW.stack = function (inst) {
    var ops = amiOps(inst.ops, ['push', 'pop', 'multipop'], ['push', 'pop'], ['multipop']);
    var s = 0, pushes = 0, total = 0, amort = 0, credit = 0, most = null, rows = [];
    ops.forEach(function (o, idx) {
      var c, before = s;
      if (o.op === 'push') { s += 1; pushes += 1; c = 1; credit += 2 - c; }
      else if (o.op === 'pop') {
        if (s === 0) eaRefuse('Operation ' + (idx + 1) + ' pops an empty stack');
        s -= 1; c = 1; credit -= c;
      } else { c = Math.min(s, o.k); s -= c; credit -= c; }
      var a = c + s - before;
      total += c; amort += a;
      if (most === null || a > most) most = a;
      rows.push([String(idx + 1), o.op === 'multipop' ? 'multipop ' + o.k : o.op, String(s), String(c), String(s), String(a), eaInt(credit)]);
    });
    return {
      tiles: { amiActual: eaInt(total), amiBound: '2 × ' + eaPlural(pushes, 'push', 'pushes') + ' = ' + eaInt(2 * pushes),
        amiCredit: eaInt(credit), amiPhi: 'Φ0 = 0, Φn = ' + s, amiAmortized: eaInt(amort), amiMax: eaInt(most),
        amiOpCount: eaInt(ops.length) },
      status: eaPlural(ops.length, 'operation', 'operations') + ' cost ' + eaInt(total) + ' in all. Every object popped was pushed first, '
        + 'so the pops, multipops included, cost at most the ' + eaPlural(pushes, 'push', 'pushes') + ', and the total is at most twice the pushes.' + amiMore(rows),
      table: { caption: 'Each operation: the stack size after it, its cost, Φ after it, its amortized cost and the credit',
        head: ['op', 'operation', 'size', 'actual', 'Φ', 'amortized', 'credit'], rows: amiShown(rows) }
    };
  };
"""

AMI_VIEW_JS["table"] = r"""
  /* Equation 17.6: 2 num - size when the load factor is at least 1/2, else
     size/2 - num; an empty table (num = size = 0) has load factor 1. */
  function amiPhi(num, size) {
    if (size === 0) return R0;
    return 2 * num >= size ? R(BigInt(2 * num - size)) : Rsub(R(BigInt(size), 2n), R(BigInt(num)));
  }
  AMI_VIEW.table = function (inst) {
    var ops = amiOps(inst.ops, ['insert', 'delete'], ['insert', 'delete'], []);
    var num = 0, size = 0, total = 0, amort = R0, ins = 0, del = 0, exp = 0, con = 0, moved = 0, rows = [];
    var most = { insert: null, 'delete': null }, low = null;
    ops.forEach(function (o, idx) {
      var c, before = amiPhi(num, size), what = '';
      if (o.op === 'insert') {
        ins += 1;
        if (size === 0) { size = 1; c = 1; what = 'allocate 1 slot'; }
        else if (num === size) { c = num + 1; moved += num; size *= 2; exp += 1; what = 'expand to ' + size + ', move ' + num; }
        else c = 1;
        num += 1;
      } else {
        if (num === 0) eaRefuse('Operation ' + (idx + 1) + ' deletes from an empty table');
        del += 1; num -= 1; c = 1;
        if (num === 0) { size = 0; what = 'free the table'; }
        else if (4 * num < size) { size /= 2; c = 1 + num; moved += num; con += 1; what = 'contract to ' + size + ', move ' + num; }
      }
      var after = amiPhi(num, size), a = Radd(R(BigInt(c)), Rsub(after, before));
      total += c; amort = Radd(amort, a);
      if (most[o.op] === null || Rcmp(a, most[o.op]) > 0) most[o.op] = a;
      if (size > 0 && (low === null || Rcmp(R(BigInt(num), BigInt(size)), low) < 0)) low = R(BigInt(num), BigInt(size));
      rows.push([String(idx + 1), o.op, String(num), String(size), String(c), eaNum(after), eaNum(a), what]);
    });
    var mx = [];
    if (most.insert !== null) mx.push('insert ' + eaNum(most.insert));
    if (most['delete'] !== null) mx.push('delete ' + eaNum(most['delete']));
    var phiN = amiPhi(num, size);
    return {
      tiles: { amiActual: eaInt(total), amiBound: '3 × ' + ins + ' + 2 × ' + del + ' = ' + eaInt(3 * ins + 2 * del),
        amiCredit: eaNum(Rsub(amort, R(BigInt(total)))), amiPhi: 'Φ0 = 0, Φn = ' + eaNum(phiN), amiAmortized: eaNum(amort),
        amiMax: mx.join(', '), amiSize: 'num ' + num + ', size ' + size + (size ? ', load ' + eaNum(R(BigInt(num), BigInt(size))) : ''),
        amiResize: 'expansions ' + exp + ', contractions ' + con + ', items moved ' + eaInt(moved) },
      status: eaPlural(ops.length, 'operation', 'operations') + ' cost ' + eaInt(total) + ' elementary insertions and deletions.'
        + (low !== null ? ' The load factor after an operation was never below ' + eaNum(low) + '.' : '') + amiMore(rows),
      table: { caption: 'Each operation: items and slots after it, its cost, Φ after it and its amortized cost',
        head: ['op', 'operation', 'num', 'size', 'actual', 'Φ', 'amortized', 'resize'], rows: amiShown(rows) }
    };
  };
"""

# ---------------------------------------------------------------------------
# rbtree (rbi): red-black trees, CLRS 13.1-13.3
# ---------------------------------------------------------------------------

RBI_JS = r"""
  var RBI_VIEW = {};
  function rbiCompute(view, inst, opts) { return eaRun(RBI_VIEW[view], inst, opts); }
  /* Nodes are {key, color: 'R' | 'B', left, right, p}; T.nil is the black sentinel. */
  function rbiTree() { var nil = { key: null, color: 'B' }; nil.left = nil; nil.right = nil; nil.p = nil; return { nil: nil, root: nil }; }
  function rbiText(T, x) {
    if (x === T.nil) return '-';
    var me = x.key + x.color;
    if (x.left === T.nil && x.right === T.nil) return me;
    return me + '(' + rbiText(T, x.left) + ' ' + rbiText(T, x.right) + ')';
  }
  /* Height: the edges from the root down to its deepest NIL leaf (a lone node has height 1). */
  function rbiHeight(T, x) { return x === T.nil ? 0 : 1 + Math.max(rbiHeight(T, x.left), rbiHeight(T, x.right)); }
  function rbiCount(T, x) { return x === T.nil ? 0 : 1 + rbiCount(T, x.left) + rbiCount(T, x.right); }
  /* bh(x): black nodes below x on its leftmost path down to NIL, the NIL counted. */
  function rbiBh(T, x) { var h = 0; x = x.left; while (true) { if (x.color === 'B') h += 1; if (x === T.nil) return h; x = x.left; } }
  /* log_b(a/d) rounded to two places, half up, by exact integer comparison. */
  function rbiLog(a, d, base) {
    var A200 = a ** 200n, D200 = d ** 200n, m = 0n, t = base;
    while (t * D200 <= A200) { m += 1n; t *= base; }
    var k = (m + 1n) / 2n, exact = a ** 100n === base ** k * d ** 100n;
    var txt = (k / 100n).toString() + (k % 100n === 0n && exact ? '' : '.' + String(k % 100n).padStart(2, '0'));
    return (exact ? '= ' : '≈ ') + txt;
  }
  function rbiBound(n) { var m = BigInt(n + 1); return '2 lg ' + (n + 1) + ' ' + rbiLog(m * m, 1n, 2n); }
"""

RBI_VIEW_JS = {}

RBI_VIEW_JS["check"] = r"""
  RBI_VIEW.check = function (inst) {
    var T = rbiTree(), by = {}, roots = [];
    inst.nodes.forEach(function (r) {
      var k = Number(r.key.n);
      if (Object.prototype.hasOwnProperty.call(by, k)) eaRefuse('Nodes names ' + k + ' twice');
      by[k] = { key: k, color: r.color === 'red' ? 'R' : 'B', left: T.nil, right: T.nil, p: T.nil, par: r.parent };
    });
    inst.nodes.forEach(function (r) {
      var x = by[Number(r.key.n)];
      if (r.parent === '-') { roots.push(x.key); return; }
      if (!/^\d+$/.test(r.parent) || !Object.prototype.hasOwnProperty.call(by, Number(r.parent))) eaRefuse(x.key + '\'s parent ' + r.parent + ' is not a key of the tree');
      var y = by[Number(r.parent)];
      if (y === x) eaRefuse(x.key + ' is its own parent');
      var side = x.key < y.key ? 'left' : 'right';
      if (y[side] !== T.nil) eaRefuse(y.key + ' has two ' + side + ' children, ' + y[side].key + ' and ' + x.key + ' (a child smaller than its parent is its left child)');
      y[side] = x; x.p = y;
    });
    if (roots.length !== 1) eaRefuse(roots.length ? 'The tree has ' + roots.length + ' roots (' + roots.join(', ') + '); give exactly one node the parent -' : 'The tree has no root: give one node the parent -');
    T.root = by[roots[0]];
    var n = rbiCount(T, T.root);
    if (n !== inst.nodes.length) {
      var lost = inst.nodes.map(function (r) { return Number(r.key.n); }).filter(function (k) {
        var z = by[k], steps = 0;
        while (z.p !== T.nil && steps <= inst.nodes.length) { z = z.p; steps += 1; }
        return z !== T.root;
      });
      eaRefuse('The parents form a cycle through ' + lost.join(', ') + ', which the root never reaches');
    }
    /* In order, preorder, postorder. */
    var ino = [], pre = [], post = [];
    (function walk(x) { if (x === T.nil) return; pre.push(x); walk(x.left); ino.push(x); walk(x.right); post.push(x); })(T.root);
    var bst = 'holds';
    for (var i = 1; i < ino.length; i += 1) {
      if (ino[i - 1].key > ino[i].key) { bst = 'fails: ' + ino[i - 1].key + ' comes before ' + ino[i].key + ' in the inorder walk'; break; }
    }
    var p2 = T.root.color === 'B' ? 'holds' : 'fails: the root ' + T.root.key + ' is red';
    var p4 = 'holds';
    for (i = 0; i < pre.length; i += 1) {
      var x = pre[i];
      if (x.color === 'R' && (x.left.color === 'R' || x.right.color === 'R')) {
        p4 = 'fails at ' + x.key + ': red, with red child ' + (x.left.color === 'R' ? x.left.key : x.right.key);
        break;
      }
    }
    /* Black counts down each side, bottom up; the first node in postorder whose sides differ. */
    var down = new Map(), p5 = 'holds';
    down.set(T.nil, 1);
    post.forEach(function (x) {
      var l = down.get(x.left), r = down.get(x.right);
      if (l !== r && p5 === 'holds') p5 = 'fails at ' + x.key + ': ' + eaPlural(l, 'black node', 'black nodes') + ' down its left side, ' + r + ' down its right';
      down.set(x, Math.max(l, r) + (x.color === 'B' ? 1 : 0));
    });
    var fails = [];
    if (p2 !== 'holds') fails.push(2);
    if (p4 !== 'holds') fails.push(4);
    if (p5 !== 'holds') fails.push(5);
    var bh = p5 === 'holds' ? String(rbiBh(T, T.root)) : '— (property 5 fails)', h = rbiHeight(T, T.root);
    var rows = ino.map(function (x) {
      var d = 0, z = x; while (z.p !== T.nil) { d += 1; z = z.p; }
      return [String(x.key), x.color === 'R' ? 'red' : 'black', x.p === T.nil ? '-' : String(x.p.key), x.p === T.nil ? 'root' : (x.p.left === x ? 'left' : 'right'), String(d),
        String(down.get(x.left)) + ' / ' + String(down.get(x.right))];
    });
    return {
      tiles: { rbiP1: 'holds', rbiP2: p2, rbiP3: 'holds', rbiP4: p4, rbiP5: p5, rbiBst: bst,
        rbiVerdict: fails.length || bst !== 'holds' ? 'no' + (fails.length ? ': property ' + fails.join(', ') + (fails.length === 1 ? ' fails' : ' fail') : ': not in search-tree order') : 'yes',
        rbiNodes: eaInt(n), rbiBh: bh, rbiHeight: String(h), rbiBound: rbiBound(n) },
      status: 'Every record names red or black, so property 1 holds, and the NIL leaves are black by definition, so property 3 holds. '
        + 'The height is ' + h + (2n ** BigInt(h) <= BigInt(n + 1) ** 2n ? ', within' : ', beyond') + ' Lemma 13.1\'s 2 lg(n + 1), which a red-black tree always meets.',
      table: { caption: 'Each node in key order, with the black nodes below it on each side (NIL leaves counted)',
        head: ['key', 'color', 'parent', 'side', 'depth', 'black below left / right'], rows: rows }
    };
  };
"""

RBI_VIEW_JS["insert"] = r"""
  function rbiRotL(T, x, st) {
    var y = x.right; x.right = y.left; if (y.left !== T.nil) y.left.p = x; y.p = x.p;
    if (x.p === T.nil) T.root = y; else if (x === x.p.left) x.p.left = y; else x.p.right = y;
    y.left = x; x.p = y; st.rot += 1;
  }
  function rbiRotR(T, x, st) {
    var y = x.left; x.left = y.right; if (y.right !== T.nil) y.right.p = x; y.p = x.p;
    if (x.p === T.nil) T.root = y; else if (x === x.p.right) x.p.right = y; else x.p.left = y;
    y.right = x; x.p = y; st.rot += 1;
  }
  function rbiPaint(x, c, st) { if (x.color !== c) { x.color = c; st.recolor += 1; } }
  /* RB-INSERT, then RB-INSERT-FIXUP; st collects the cases, recolorings and rotations. */
  function rbiInsert(T, key, st) {
    var z = { key: key, color: 'R', left: T.nil, right: T.nil, p: T.nil }, y = T.nil, x = T.root;
    while (x !== T.nil) { y = x; x = key < x.key ? x.left : x.right; }
    z.p = y;
    if (y === T.nil) T.root = z; else if (key < y.key) y.left = z; else y.right = z;
    while (z.p.color === 'R') {
      if (z.p === z.p.p.left) {
        y = z.p.p.right;
        if (y.color === 'R') { rbiPaint(z.p, 'B', st); rbiPaint(y, 'B', st); rbiPaint(z.p.p, 'R', st); z = z.p.p; st.cases.push('1'); }
        else {
          if (z === z.p.right) { z = z.p; rbiRotL(T, z, st); st.cases.push('2'); }
          rbiPaint(z.p, 'B', st); rbiPaint(z.p.p, 'R', st); rbiRotR(T, z.p.p, st); st.cases.push('3');
        }
      } else {
        y = z.p.p.left;
        if (y.color === 'R') { rbiPaint(z.p, 'B', st); rbiPaint(y, 'B', st); rbiPaint(z.p.p, 'R', st); z = z.p.p; st.cases.push('1′'); }
        else {
          if (z === z.p.left) { z = z.p; rbiRotR(T, z, st); st.cases.push('2′'); }
          rbiPaint(z.p, 'B', st); rbiPaint(z.p.p, 'R', st); rbiRotL(T, z.p.p, st); st.cases.push('3′');
        }
      }
    }
    rbiPaint(T.root, 'B', st);
  }
  RBI_VIEW.insert = function (inst) {
    var T = rbiTree(), seen = {}, rows = [], recolor = 0, rot = 0, most = 0, tally = {};
    var keys = inst.keys.map(function (r) { return Number(r.n); });
    keys.forEach(function (k, i) {
      if (seen[k]) eaRefuse('Keys, entry ' + (i + 1) + ': ' + k + ' is already in the tree; this lab inserts distinct keys');
      seen[k] = true;
    });
    keys.forEach(function (k) {
      var st = { cases: [], recolor: 0, rot: 0 };
      rbiInsert(T, k, st);
      recolor += st.recolor; rot += st.rot; if (st.rot > most) most = st.rot;
      st.cases.forEach(function (c) { tally[c] = (tally[c] || 0) + 1; });
      rows.push([String(k), st.cases.length ? st.cases.join(', ') : 'none', String(st.recolor), String(st.rot),
        String(T.root.key), String(rbiBh(T, T.root)), String(rbiHeight(T, T.root))]);
    });
    var order = ['1', '2', '3', '1′', '2′', '3′'], cases = order.filter(function (c) { return tally[c]; }).map(function (c) { return 'case ' + c + ' ×' + tally[c]; });
    var n = keys.length;
    return {
      tiles: { rbiCases: cases.length ? cases.join(', ') : 'none', rbiRecolor: eaInt(recolor), rbiRotate: eaInt(rot),
        rbiMostRot: String(most), rbiFinal: rbiText(T, T.root), rbiBh: String(rbiBh(T, T.root)),
        rbiHeight: String(rbiHeight(T, T.root)), rbiBound: rbiBound(n) },
      status: eaPlural(n, 'insertion', 'insertions') + ' made ' + eaPlural(rot, 'rotation', 'rotations') + ' and ' + eaPlural(recolor, 'recoloring', 'recolorings')
        + '; no insertion made more than ' + most + ' (RB-INSERT-FIXUP never makes more than two).',
      table: { caption: 'Each insertion: the fix-up cases in order (′ marks the mirror case), its recolorings and rotations, and the tree after it',
        head: ['key', 'cases', 'recolorings', 'rotations', 'root', 'black-height', 'height'], rows: rows }
    };
  };
"""

# ---------------------------------------------------------------------------
# btree (bti): B-tree insertion, CLRS 18.2
# ---------------------------------------------------------------------------

BTI_JS = r"""
  var BTI_VIEW = {};
  function btiCompute(view, inst, opts) { return eaRun(BTI_VIEW[view], inst, opts); }
  /* log_b(a/d) rounded to two places, half up, by exact integer comparison. */
  function btiLog(a, d, base) {
    var A200 = a ** 200n, D200 = d ** 200n, m = 0n, t = base;
    while (t * D200 <= A200) { m += 1n; t *= base; }
    var k = (m + 1n) / 2n, exact = a ** 100n === base ** k * d ** 100n;
    var txt = (k / 100n).toString() + (k % 100n === 0n && exact ? '' : '.' + String(k % 100n).padStart(2, '0'));
    return (exact ? '= ' : '≈ ') + txt;
  }
"""

BTI_VIEW_JS = {}

BTI_VIEW_JS["insert"] = r"""
  BTI_VIEW.insert = function (inst) {
    var t = Number(inst.t.n), keys = inst.keys.map(function (r) { return Number(r.n); }), seen = {};
    keys.forEach(function (k, i) {
      if (seen[k]) eaRefuse('Keys, entry ' + (i + 1) + ': ' + k + ' is already in the tree; this lab inserts distinct keys');
      seen[k] = true;
    });
    /* B-TREE-CREATE: one empty leaf (its DISK-WRITE is not in the totals). */
    var T = { root: { keys: [], c: [], leaf: true } }, st = { reads: 0, writes: 0, splits: 0, nodes: 1 };
    function btiSplit(x, i) {
      var y = x.c[i], z = { leaf: y.leaf, keys: y.keys.slice(t), c: y.leaf ? [] : y.c.slice(t) };
      var mid = y.keys[t - 1];
      y.keys = y.keys.slice(0, t - 1);
      if (!y.leaf) y.c = y.c.slice(0, t);
      x.c.splice(i + 1, 0, z); x.keys.splice(i, 0, mid);
      st.writes += 3; st.splits += 1; st.nodes += 1;
    }
    function btiNonfull(x, k) {
      var i = 0;
      while (i < x.keys.length && k > x.keys[i]) i += 1;
      if (x.leaf) { x.keys.splice(i, 0, k); st.writes += 1; return; }
      st.reads += 1;
      if (x.c[i].keys.length === 2 * t - 1) { btiSplit(x, i); if (k > x.keys[i]) i += 1; }
      btiNonfull(x.c[i], k);
    }
    function btiHeight() { var h = 0, x = T.root; while (!x.leaf) { h += 1; x = x.c[0]; } return h; }
    var rows = [];
    keys.forEach(function (k) {
      var r0 = st.reads, w0 = st.writes, s0 = st.splits, r = T.root;
      if (r.keys.length === 2 * t - 1) {
        var s = { keys: [], c: [r], leaf: false };
        T.root = s; st.nodes += 1;
        btiSplit(s, 0);
        btiNonfull(s, k);
      } else btiNonfull(r, k);
      rows.push([String(k), String(st.splits - s0), String(st.reads - r0), String(st.writes - w0), String(btiHeight())]);
    });
    var levels = [], level = [T.root];
    while (level.length) {
      levels.push(level.map(function (x) { return '[' + x.keys.join(' ') + ']'; }).join(' '));
      var next = [];
      level.forEach(function (x) { if (!x.leaf) next = next.concat(x.c); });
      level = next;
    }
    var n = keys.length, h = btiHeight(), arg = R(BigInt(n + 1), 2n);
    var argText = Rint(arg) ? eaInt(arg.n) : eaFixed(arg, 1);
    return {
      tiles: { btiHeight: String(h), btiNodes: eaInt(st.nodes), btiSplits: eaInt(st.splits), btiReads: eaInt(st.reads),
        btiWrites: eaInt(st.writes), btiBound: 'log_' + t + ' ' + argText + ' ' + btiLog(BigInt(n + 1), 2n, BigInt(t)), btiLevels: levels.join(' / ') },
      status: eaPlural(n, 'key', 'keys') + ' inserted with minimum degree t = ' + t + ' (at most ' + (2 * t - 1) + ' keys a node). '
        + 'The height is ' + h + '; Theorem 18.1 bounds it by log_t((n + 1)/2) for every B-tree on n keys.',
      table: { caption: 'Each insertion: the splits it made, its DISK-READs and DISK-WRITEs, and the height after it',
        head: ['key', 'splits', 'reads', 'writes', 'height'], rows: rows }
    };
  };
"""

# ---------------------------------------------------------------------------
# fibheap (fhi): Fibonacci heaps, CLRS 19
# ---------------------------------------------------------------------------

FHI_JS = r"""
  var FHI_VIEW = {}, FHI_OPS = 120;
  function fhiCompute(view, inst, opts) { return eaRun(FHI_VIEW[view], inst, opts); }
  /* Read "insert K | min | extract | decrease K V | delete K" into ops. */
  function fhiOps(toks) {
    var out = [], i = 0, t, what = 'Operations';
    var num = function (j, after) {
      if (j >= toks.length || !/^\d+$/.test(toks[j])) eaRefuse(what + ', entry ' + (j) + ': ' + after + ' needs a key (a whole number) after it');
      var v = Number(toks[j]);
      if (v > 1000000) eaRefuse(what + ', entry ' + (j + 1) + ': a key is at most 1,000,000, and it is ' + toks[j]);
      return v;
    };
    while (i < toks.length) {
      t = toks[i];
      if (t === 'insert' || t === 'delete') { out.push({ op: t, k: num(i + 1, t) }); i += 2; }
      else if (t === 'decrease') { var k = num(i + 1, t); out.push({ op: t, k: k, v: num(i + 2, 'decrease ' + k) }); i += 3; }
      else if (t === 'min' || t === 'extract') { out.push({ op: t }); i += 1; }
      else if (/^\d+$/.test(t)) eaRefuse(what + ', entry ' + (i + 1) + ': "' + t + '" follows no insert, decrease or delete');
      else eaRefuse(what + ', entry ' + (i + 1) + ': "' + t + '" should be insert, min, extract, decrease or delete');
    }
    return out;
  }
  /* The heap: roots in root-list order (a circle read from index 0), min a node.
     Node: {key (null is minus infinity), children: [], p, mark}. */
  function fhiLess(a, b) { return a.key === null ? b.key !== null : (b.key !== null && a.key < b.key); }
  function fhiHeap() { return { roots: [], min: null, n: 0, nodes: {} }; }
  /* A new root goes immediately left of H.min (CLRS Figure 19.3). INSERT then
     updates H.min; CUT does not (DECREASE-KEY does, after its cuts). */
  function fhiAddRoot(H, x, update) {
    if (H.min === null) { H.roots = [x]; H.min = x; return; }
    H.roots.splice(H.roots.indexOf(H.min), 0, x);
    if (update && fhiLess(x, H.min)) H.min = x;
  }
  function fhiMarks(H) { var m = 0; Object.keys(H.nodes).forEach(function (k) { if (H.nodes[k].mark) m += 1; }); return m; }
  function fhiPhi(H) { return H.roots.length + 2 * fhiMarks(H); }
  function fhiInsert(H, k, st) { var x = { key: k, children: [], p: null, mark: false }; H.nodes[k] = x; H.n += 1; fhiAddRoot(H, x, true); st.actual += 1; }
  function fhiExtract(H, st) {
    var z = H.min, idx = H.roots.indexOf(z), kids = z.children;
    kids.forEach(function (x) { x.p = null; });
    H.roots.splice.apply(H.roots, [idx, 1].concat(kids));
    st.actual += 1 + kids.length;
    st.moved = kids.length;
    if (z.key !== null) delete H.nodes[z.key];
    H.n -= 1;
    if (H.roots.length === 0) { H.min = null; st.scanned = 0; return z; }
    /* CONSOLIDATE, starting at z's right neighbour and going right round the circle. */
    var start = (idx + kids.length) % H.roots.length, order = H.roots.slice(start).concat(H.roots.slice(0, start)), A = [];
    st.scanned = order.length; st.actual += order.length;
    order.forEach(function (w) {
      var x = w, d = x.children.length, y, tmp;
      while (A[d]) {
        y = A[d];
        if (fhiLess(y, x)) { tmp = x; x = y; y = tmp; }
        x.children.push(y); y.p = x; y.mark = false; st.links += 1;
        A[d] = null; d += 1;
      }
      A[d] = x;
    });
    H.roots = []; H.min = null;
    A.forEach(function (x) { if (x) { H.roots.push(x); if (H.min === null || fhiLess(x, H.min)) H.min = x; } });
    return z;
  }
  function fhiCut(H, x, y, st) {
    y.children.splice(y.children.indexOf(x), 1);
    x.p = null; x.mark = false; fhiAddRoot(H, x, false);
    st.cuts += 1; st.actual += 1;
  }
  function fhiCascade(H, y, st) {
    st.calls += 1;
    var z = y.p;
    if (z !== null) {
      if (!y.mark) y.mark = true;
      else { fhiCut(H, y, z, st); st.cascades += 1; fhiCascade(H, z, st); }
    }
  }
  function fhiDecrease(H, x, v, st) {
    if (x.key !== null) delete H.nodes[x.key];
    x.key = v;
    if (v !== null) H.nodes[v] = x;
    st.actual += 1;
    var y = x.p;
    if (y !== null && fhiLess(x, y)) { fhiCut(H, x, y, st); fhiCascade(H, y, st); }
    if (fhiLess(x, H.min)) H.min = x;
  }
  function fhiDegree(H) {
    var d = 0;
    (function walk(list) { list.forEach(function (x) { if (x.children.length > d) d = x.children.length; walk(x.children); }); })(H.roots);
    return d;
  }
  /* D(n) = floor(log_phi n): the largest k with phi^k <= n, where
     phi^k = (L_k + F_k sqrt 5)/2, tested in integers. */
  function fhiDn(n) {
    var k = 0, L = 2n, F = 0n, L1 = 1n, F1 = 1n, N = BigInt(n), t;
    while (true) {
      var rhs = 2n * N - L1;
      if (rhs < 0n || 5n * F1 * F1 > rhs * rhs) return k;
      k += 1; t = L1; L1 = L1 + L; L = t; t = F1; F1 = F1 + F; F = t;
    }
  }
  function fhiRootText(H) {
    if (H.min === null) return 'empty';
    var i = H.roots.indexOf(H.min), out = [];
    for (var j = 0; j < H.roots.length; j += 1) { var x = H.roots[(i + j) % H.roots.length]; out.push(x.key + (j === 0 ? ' (min)' : '')); }
    return out.join(', ');
  }
  function fhiSize(x) { var s = 1; x.children.forEach(function (c) { s += fhiSize(c); }); return s; }
  /* Run every operation; each row is {label, result, st, before, after, t, m, deg, n}. */
  function fhiRun(toks) {
    var ops = fhiOps(toks), H = fhiHeap(), log = [];
    if (ops.length > FHI_OPS) eaRefuse('Operations: this lab runs at most ' + FHI_OPS + ' operations, and there are ' + ops.length);
    ops.forEach(function (o, i) {
      var st = { actual: 0, links: 0, cuts: 0, cascades: 0, calls: 0, moved: 0, scanned: 0 }, before = fhiPhi(H), label, res = '';
      var at = 'Operation ' + (i + 1) + ' (' + o.op + (o.k !== undefined ? ' ' + o.k : '') + (o.v !== undefined ? ' ' + o.v : '') + ')';
      var has = function (k) { return Object.prototype.hasOwnProperty.call(H.nodes, k); };
      if (o.op === 'insert') {
        if (has(o.k)) eaRefuse(at + ': ' + o.k + ' is already in the heap; this lab keeps the keys distinct');
        fhiInsert(H, o.k, st); label = 'insert ' + o.k;
      } else if (o.op === 'min') {
        if (H.min === null) eaRefuse(at + ': the heap is empty');
        st.actual = 1; label = 'min'; res = String(H.min.key);
      } else if (o.op === 'extract') {
        if (H.min === null) eaRefuse(at + ': the heap is empty');
        res = String(fhiExtract(H, st).key); label = 'extract-min';
      } else if (o.op === 'decrease') {
        if (!has(o.k)) eaRefuse(at + ': ' + o.k + ' is not in the heap');
        if (o.v > o.k) eaRefuse(at + ': the new key ' + o.v + ' is greater than ' + o.k);
        if (o.v !== o.k && has(o.v)) eaRefuse(at + ': ' + o.v + ' is already in the heap; this lab keeps the keys distinct');
        fhiDecrease(H, H.nodes[o.k], o.v, st); label = 'decrease ' + o.k + ' → ' + o.v;
      } else {
        if (!has(o.k)) eaRefuse(at + ': ' + o.k + ' is not in the heap');
        fhiDecrease(H, H.nodes[o.k], null, st);
        fhiExtract(H, st); label = 'delete ' + o.k;
      }
      var m = fhiMarks(H);
      log.push({ label: label, op: o.op, result: res, st: st, before: before, after: H.roots.length + 2 * m, t: H.roots.length, m: m,
        deg: fhiDegree(H), n: H.n, roots: fhiRootText(H) });
    });
    return { H: H, log: log };
  }
  function fhiAm(e) { return e.st.actual + e.after - e.before; }
  function fhiDegText(H) { return 'max degree ' + fhiDegree(H) + (H.n ? '; ⌊log_φ ' + H.n + '⌋ = ' + fhiDn(H.n) : ''); }
  var FHI_NAME = { insert: 'insert', min: 'min', extract: 'extract-min', decrease: 'decrease-key', 'delete': 'delete' };
"""

FHI_VIEW_JS = {}

FHI_VIEW_JS["ops"] = r"""
  FHI_VIEW.ops = function (inst) {
    var run = fhiRun(inst.ops), H = run.H, total = 0, am = 0, most = {}, order = [], rows = [];
    run.log.forEach(function (e) {
      var a = fhiAm(e);
      total += e.st.actual; am += a;
      if (most[e.op] === undefined) { most[e.op] = a; order.push(e.op); } else if (a > most[e.op]) most[e.op] = a;
      rows.push([e.label, e.result, String(e.st.actual), String(e.t), String(e.m), String(e.after), eaSigned(BigInt(e.after - e.before)), String(a), e.roots]);
    });
    var m = fhiMarks(H);
    return {
      tiles: { fhiActual: eaInt(total), fhiAmortized: eaInt(am), fhiPhi: 't(H) + 2m(H) = ' + H.roots.length + ' + 2 × ' + m + ' = ' + (H.roots.length + 2 * m),
        fhiMostAm: order.map(function (o) { return FHI_NAME[o] + ' ' + most[o]; }).join(', '), fhiRoots: fhiRootText(H),
        fhiDegree: fhiDegText(H), fhiN: eaInt(H.n) },
      status: 'The amortized costs add up to the actual costs plus the final potential (' + eaInt(am) + ' = ' + eaInt(total) + ' + ' + fhiPhi(H)
        + ', the heap starting empty); since Φ is never negative, they bound the actual total.',
      table: { caption: 'Each operation: its actual cost, t(H), m(H) and Φ after it, ΔΦ, its amortized cost and the root list from H.min',
        head: ['operation', 'result', 'actual', 't', 'm', 'Φ', 'ΔΦ', 'amortized', 'root list'], rows: rows }
    };
  };
"""

FHI_VIEW_JS["cascade"] = r"""
  FHI_VIEW.cascade = function (inst) {
    var run = fhiRun(inst.ops), H = run.H, cuts = 0, casc = 0, calls = 0, dec = 0, decAm = [], rows = [];
    run.log.forEach(function (e) {
      if (e.op === 'decrease' || e.op === 'delete') {
        cuts += e.st.cuts; casc += e.st.cascades; calls += e.st.calls; dec += 1;
        if (e.op === 'decrease') decAm.push(fhiAm(e));
      }
      rows.push([e.label, String(e.st.cuts), String(e.st.cascades), String(e.st.calls), String(e.m), String(e.st.actual), eaSigned(BigInt(e.after - e.before)), String(fhiAm(e))]);
    });
    var marked = Object.keys(H.nodes).map(Number).sort(function (a, b) { return a - b; }).filter(function (k) { return H.nodes[k].mark; });
    /* Lemma 19.4: size(x) >= F(degree + 2), F(1) = F(2) = 1; the closest node is the least size / F. */
    var fib = [0, 1]; for (var i = 2; i < 40; i += 1) fib.push(fib[i - 1] + fib[i - 2]);
    var holds = true, close = null, count = 0;
    Object.keys(H.nodes).map(Number).sort(function (a, b) { return a - b; }).forEach(function (k) {
      var x = H.nodes[k], d = x.children.length, s = fhiSize(x), f = fib[d + 2];
      count += 1;
      if (s < f) holds = false;
      if (close === null || s * close.f < close.s * f || (s * close.f === close.s * f && d > close.d)) close = { k: k, d: d, s: s, f: f };
    });
    var lemma = count === 0 ? 'the heap is empty' : (holds ? 'holds at all ' + count : 'FAILS') + '; closest ' + close.k + ': degree ' + close.d + ', size ' + close.s + ', F(' + (close.d + 2) + ') = ' + close.f;
    var mx = decAm.length ? Math.max.apply(null, decAm) : null;
    return {
      tiles: { fhiCuts: eaInt(cuts), fhiCascades: eaInt(casc), fhiCalls: eaInt(calls), fhiMarked: eaCount(marked.map(String)),
        fhiMostDec: mx === null ? '— (no decrease-key)' : String(mx), fhiLemma: lemma, fhiDegree: fhiDegText(H), fhiRoots: fhiRootText(H) },
      status: dec ? eaPlural(cuts, 'cut', 'cuts') + ' in ' + eaPlural(dec, 'decrease or delete', 'decreases and deletes') + ', ' + eaInt(casc) + ' of them cascading. '
        + 'A cascading cut unmarks a node and adds a root, so Φ falls by one and pays for it.' : 'No key is decreased or deleted, so nothing is cut.',
      table: { caption: 'Each operation: its cuts, the cascading cuts among them, its calls to CASCADING-CUT, m(H) after it, its actual cost, ΔΦ and its amortized cost',
        head: ['operation', 'cuts', 'cascading', 'CASCADING-CUT calls', 'm', 'actual', 'ΔΦ', 'amortized'], rows: rows }
    };
  };
"""

# ---------------------------------------------------------------------------
# veb (vbi): proto-vEB and van Emde Boas trees, CLRS 20.2-20.3
# ---------------------------------------------------------------------------

VBI_JS = r"""
  var VBI_VIEW = {}, VBI_OPS = 60;
  function vbiCompute(view, inst, opts) { return eaRun(VBI_VIEW[view], inst, opts); }
  function vbiRoot(u) { var b = 0; while ((1 << (2 * b)) < u) b += 1; return 1 << b; }
  /* proto-vEB(u): u = 2 holds A[0..1]; otherwise a summary and sqrt(u)
     clusters, made empty when first touched (the book allocates them all). */
  function vbiProto(u) { return u === 2 ? { u: 2, A: [0, 0] } : { u: u, s: vbiRoot(u), summary: null, cluster: {} }; }
  function vbiPS(V) { if (!V.summary) V.summary = vbiProto(V.s); return V.summary; }
  function vbiPC(V, i) { if (!V.cluster[i]) V.cluster[i] = vbiProto(V.s); return V.cluster[i]; }
  function vbiPMember(V, x, c) { c.n += 1; if (V.u === 2) return V.A[x] === 1; return vbiPMember(vbiPC(V, Math.floor(x / V.s)), x % V.s, c); }
  function vbiPMin(V, c) {
    c.n += 1;
    if (V.u === 2) return V.A[0] ? 0 : (V.A[1] ? 1 : null);
    var mc = vbiPMin(vbiPS(V), c);
    if (mc === null) return null;
    return mc * V.s + vbiPMin(vbiPC(V, mc), c);
  }
  function vbiPSucc(V, x, c) {
    c.n += 1;
    if (V.u === 2) return x === 0 && V.A[1] ? 1 : null;
    var h = Math.floor(x / V.s), off = vbiPSucc(vbiPC(V, h), x % V.s, c);
    if (off !== null) return h * V.s + off;
    var sc = vbiPSucc(vbiPS(V), h, c);
    if (sc === null) return null;
    return sc * V.s + vbiPMin(vbiPC(V, sc), c);
  }
  function vbiPInsert(V, x, c) {
    c.n += 1;
    if (V.u === 2) { V.A[x] = 1; return; }
    var h = Math.floor(x / V.s);
    vbiPInsert(vbiPC(V, h), x % V.s, c);
    vbiPInsert(vbiPS(V), h, c);
  }
  /* The book leaves proto-vEB deletion to Exercise 20.2-2: the lab deletes from
     the cluster, asks the cluster's minimum, and deletes from the summary when
     the cluster is empty. */
  function vbiPDelete(V, x, c) {
    c.n += 1;
    if (V.u === 2) { V.A[x] = 0; return; }
    var h = Math.floor(x / V.s);
    vbiPDelete(vbiPC(V, h), x % V.s, c);
    if (vbiPMin(vbiPC(V, h), c) === null) vbiPDelete(vbiPS(V), h, c);
  }
  /* vEB(u): min and max held apart (min not in any cluster). */
  function vbiVeb(u) { return { u: u, s: u === 2 ? 0 : vbiRoot(u), min: null, max: null, summary: null, cluster: {} }; }
  function vbiVS(V) { if (!V.summary) V.summary = vbiVeb(V.s); return V.summary; }
  function vbiVC(V, i) { if (!V.cluster[i]) V.cluster[i] = vbiVeb(V.s); return V.cluster[i]; }
  function vbiVMember(V, x, c) {
    c.n += 1;
    if (x === V.min || x === V.max) return true;
    if (V.u === 2) return false;
    return vbiVMember(vbiVC(V, Math.floor(x / V.s)), x % V.s, c);
  }
  function vbiVSucc(V, x, c) {
    c.n += 1;
    if (V.u === 2) return x === 0 && V.max === 1 ? 1 : null;
    if (V.min !== null && x < V.min) return V.min;
    var h = Math.floor(x / V.s), lo = x % V.s, maxLow = vbiVC(V, h).max;
    if (maxLow !== null && lo < maxLow) return h * V.s + vbiVSucc(vbiVC(V, h), lo, c);
    var sc = vbiVSucc(vbiVS(V), h, c);
    if (sc === null) return null;
    return sc * V.s + vbiVC(V, sc).min;
  }
  function vbiVInsert(V, x, c) {
    c.n += 1;
    if (V.min === null) { V.min = x; V.max = x; return; }
    if (x < V.min) { var t = x; x = V.min; V.min = t; }
    if (V.u > 2) {
      var h = Math.floor(x / V.s), lo = x % V.s, cl = vbiVC(V, h);
      if (cl.min === null) { vbiVInsert(vbiVS(V), h, c); cl.min = lo; cl.max = lo; }
      else vbiVInsert(cl, lo, c);
    }
    if (x > V.max) V.max = x;
  }
  function vbiVDelete(V, x, c) {
    c.n += 1;
    if (V.min === V.max) { V.min = null; V.max = null; return; }
    if (V.u === 2) { V.min = x === 0 ? 1 : 0; V.max = V.min; return; }
    if (x === V.min) { var fc = vbiVS(V).min; x = fc * V.s + vbiVC(V, fc).min; V.min = x; }
    var h = Math.floor(x / V.s);
    vbiVDelete(vbiVC(V, h), x % V.s, c);
    if (vbiVC(V, h).min === null) {
      vbiVDelete(vbiVS(V), h, c);
      if (x === V.max) {
        var sm = vbiVS(V).max;
        V.max = sm === null ? V.min : sm * V.s + vbiVC(V, sm).max;
      }
    } else if (x === V.max) V.max = h * V.s + vbiVC(V, h).max;
  }
  /* The members of a vEB node, its min included. */
  function vbiAll(V) {
    var out = [];
    if (V.min === null) return out;
    out.push(V.min);
    if (V.u === 2) { if (V.max !== V.min) out.push(V.max); return out; }
    Object.keys(V.cluster).map(Number).sort(function (a, b) { return a - b; }).forEach(function (i) {
      vbiAll(V.cluster[i]).forEach(function (lo) { out.push(i * V.s + lo); });
    });
    return out;
  }
  function vbiOps(toks, u) {
    var out = [], i = 0, t, what = 'Operations', words = ['insert', 'member', 'successor', 'delete'];
    while (i < toks.length) {
      t = toks[i];
      if (/^\d+$/.test(t)) eaRefuse(what + ', entry ' + (i + 1) + ': "' + t + '" follows no insert, member, successor or delete');
      if (words.indexOf(t) < 0) eaRefuse(what + ', entry ' + (i + 1) + ': "' + t + '" should be insert, member, successor or delete');
      if (i + 1 >= toks.length || !/^\d+$/.test(toks[i + 1])) eaRefuse(what + ', entry ' + (i + 1) + ': ' + t + ' needs a number after it');
      var x = Number(toks[i + 1]);
      if (x >= u) eaRefuse(what + ', entry ' + (i + 2) + ': with u = ' + eaInt(u) + ' an element is from 0 to ' + eaInt(u - 1) + ', and it is ' + toks[i + 1]);
      out.push({ op: t, x: x });
      i += 2;
    }
    if (out.length > VBI_OPS) eaRefuse(what + ': this lab runs at most ' + VBI_OPS + ' operations, and there are ' + out.length);
    return out;
  }
"""

VBI_VIEW_JS = {}

VBI_VIEW_JS["ops"] = r"""
  VBI_VIEW.ops = function (inst) {
    var k = Number(inst.k.n), u = Math.pow(2, Math.pow(2, k)), ops = vbiOps(inst.ops, u);
    var P = vbiProto(u), V = vbiVeb(u), members = {}, rows = [], answers = [], pt = 0, vt = 0, most = { p: 0, v: 0 };
    ops.forEach(function (o, i) {
      var cp = { n: 0 }, cv = { n: 0 }, res = '', a, b, at = 'Operation ' + (i + 1) + ' (' + o.op + ' ' + o.x + ')';
      if (o.op === 'insert') {
        if (members[o.x]) eaRefuse(at + ': ' + o.x + ' is already a member; VEB-TREE-INSERT assumes it is not');
        vbiPInsert(P, o.x, cp); vbiVInsert(V, o.x, cv); members[o.x] = true;
      } else if (o.op === 'delete') {
        if (!members[o.x]) eaRefuse(at + ': ' + o.x + ' is not a member; VEB-TREE-DELETE assumes it is');
        vbiPDelete(P, o.x, cp); vbiVDelete(V, o.x, cv); delete members[o.x];
      } else if (o.op === 'member') {
        a = vbiPMember(P, o.x, cp); b = vbiVMember(V, o.x, cv);
        if (a !== b) throw new Error('veb: the two structures disagree on member ' + o.x);
        res = a ? 'yes' : 'no'; answers.push('member ' + o.x + ': ' + res);
      } else {
        a = vbiPSucc(P, o.x, cp); b = vbiVSucc(V, o.x, cv);
        if (a !== b) throw new Error('veb: the two structures disagree on successor ' + o.x);
        res = a === null ? 'none' : String(a); answers.push('successor ' + o.x + ': ' + res);
      }
      pt += cp.n; vt += cv.n;
      if (cp.n > most.p) most.p = cp.n;
      if (cv.n > most.v) most.v = cv.n;
      rows.push([o.op + ' ' + o.x, res, String(cp.n), String(cv.n)]);
    });
    var all = vbiAll(V), top;
    if (V.min === null) top = 'empty';
    else {
      var parts = ['min ' + V.min + ', max ' + V.max];
      if (u > 2) {
        parts.push('summary: ' + eaNames(V.summary ? vbiAll(V.summary).map(String) : []));
        Object.keys(V.cluster).map(Number).sort(function (a, b) { return a - b; }).forEach(function (i) {
          var m = vbiAll(V.cluster[i]);
          if (m.length) parts.push('cluster ' + i + ': ' + m.map(function (lo) { return lo + ' (' + (i * V.s + lo) + ')'; }).join(', '));
        });
      }
      top = parts.join('; ');
    }
    return {
      tiles: { vbiU: 'u = ' + eaInt(u) + ', √u = ' + (u > 2 ? vbiRoot(u) : '—') + ', lg lg u = ' + k, vbiProto: eaInt(pt), vbiVeb: eaInt(vt),
        vbiMost: 'proto-vEB ' + most.p + ', vEB ' + most.v, vbiAnswers: answers.length ? answers.join('; ') : 'none asked',
        vbiMembers: eaCount(all.map(String)), vbiTop: top },
      status: 'Both structures ran every operation and gave the same answers. A vEB operation makes at most one call that '
        + 'recurses below it at each of the ' + k + ' levels under the top, so its calls stay near lg lg u = ' + k + '; proto-vEB can recurse twice at a level.',
      table: { caption: 'Each operation: its answer and the calls it made in each structure, the top call included',
        head: ['operation', 'answer', 'proto-vEB calls', 'vEB calls'], rows: rows }
    };
  };
"""

# ---------------------------------------------------------------------------
# bfs (bfi): breadth-first search, CLRS 22.2
# ---------------------------------------------------------------------------

BFI_JS = r"""
  var BFI_VIEW = {}, BFI_MAX = 30;
  function bfiCompute(view, inst, opts) { return eaRun(BFI_VIEW[view], inst, opts); }
"""

BFI_VIEW_JS = {}

BFI_VIEW_JS["search"] = r"""
  BFI_VIEW.search = function (inst) {
    var directed = inst.graph === 'directed', V = [], adj = {}, seenEdge = {}, E = 0;
    var add = function (v) { if (!Object.prototype.hasOwnProperty.call(adj, v)) { adj[v] = []; V.push(v); } };
    inst.vertices.forEach(add);
    inst.edges.forEach(function (e, i) {
      var a = e.from, b = e.to;
      if (!directed && a === b) eaRefuse('Edges, record ' + (i + 1) + ': ' + a + ' to itself is a self-loop, which an undirected graph does not have');
      var key = directed ? a + ' ' + b : (a < b ? a + ' ' + b : b + ' ' + a);
      if (seenEdge[key]) eaRefuse('Edges, record ' + (i + 1) + ': the edge ' + a + ', ' + b + ' is given twice');
      seenEdge[key] = true; E += 1;
      add(a); add(b);
      adj[a].push(b);
      if (!directed) adj[b].push(a);
    });
    var s = inst.source;
    if (!Object.prototype.hasOwnProperty.call(adj, s)) eaRefuse('The source ' + s + ' is not a vertex of the graph');
    if (V.length > BFI_MAX) eaRefuse('The graph has ' + V.length + ' vertices; this lab takes at most ' + BFI_MAX);
    /* BFS: every vertex white, d infinite; the source gray at 0; a FIFO queue. */
    var d = {}, pi = {}, color = {}, Q = [s], head = 0, enq = 1, scans = 0, order = [];
    V.forEach(function (v) { color[v] = 'white'; d[v] = null; pi[v] = null; });
    color[s] = 'gray'; d[s] = 0;
    while (head < Q.length) {
      var u = Q[head]; head += 1; order.push(u);
      adj[u].forEach(function (v) {
        scans += 1;
        if (color[v] === 'white') { color[v] = 'gray'; d[v] = d[u] + 1; pi[v] = u; Q.push(v); enq += 1; }
      });
      color[u] = 'black';
    }
    var layers = [];
    order.forEach(function (v) { if (!layers[d[v]]) layers[d[v]] = []; layers[d[v]].push(v); });
    var unreached = V.filter(function (v) { return d[v] === null; });
    var rows = V.map(function (v) {
      return [v, eaNames(adj[v]), d[v] === null ? '∞' : String(d[v]), pi[v] === null ? (v === s ? '— (source)' : '—') : pi[v],
        d[v] === null ? '—' : String(order.indexOf(v) + 1)];
    });
    var listTotal = directed ? E : 2 * E;
    return {
      tiles: { bfiDist: V.map(function (v) { return v + ' ' + (d[v] === null ? '∞' : d[v]); }).join(', '),
        bfiParent: order.filter(function (v) { return v !== s; }).map(function (v) { return v + ' ← ' + pi[v]; }).join(', ') || 'none',
        bfiLayers: layers.map(function (l, i) { return i + ': ' + l.join(' '); }).join('; '),
        bfiEnqueued: eaInt(enq) + ' of ' + eaPlural(V.length, 'vertex', 'vertices'),
        bfiScanned: eaInt(scans) + ' of ' + eaInt(listTotal) + ' (' + (directed ? 'E' : '2E') + ')',
        bfiUnreached: eaCount(unreached) },
      status: 'BFS enqueued each reachable vertex once and scanned each of their adjacency lists once, in the order the edges were given: '
        + eaInt(enq) + ' enqueues and ' + eaInt(scans) + ' adjacency entries, within O(V + E).'
        + (unreached.length ? ' ' + eaPlural(unreached.length, 'vertex is', 'vertices are') + ' not reachable from ' + s + ' and keep d = ∞.' : ''),
      table: { caption: 'Each vertex: its adjacency list in input order, its distance d, its parent π and when it was dequeued',
        head: ['vertex', 'adjacency list', 'd', 'π', 'dequeued'], rows: rows }
    };
  };
"""

# ---------------------------------------------------------------------------
# Python: the build-time mirrors of every JS refusal (each sentence as the page says it)
# ---------------------------------------------------------------------------


def _ops_list(what, hi, rows=2):
    return dict(what=what, control="area", rows=rows, kind="list", lo=1, hi=hi, things="words and numbers",
                each=dict(ea.PARENT))


def _int_list(what, lo, hi, things, each):
    return dict(what=what, control="text", kind="list", lo=lo, hi=hi, things=things, each=each)


def _check_lcs(inst, fixed):
    for name in ("x", "y"):
        if len(inst[name]) > 30:
            raise ValueError("%s has %d characters; this lab takes at most 30" % (name.upper(), len(inst[name])))


def _check_obst(inst, fixed):
    n, m = len(inst["p"]), len(inst["q"])
    if m != n + 1:
        raise ValueError("There %s, so there are %d dummy probabilities q0 to q%d, and %d %s given"
                         % ("is 1 key" if n == 1 else "are %d keys" % n, n + 1, n, m, "is" if m == 1 else "are"))
    total = (sum(inst["p"]) + sum(inst["q"])) / inst["scale"]
    if total != 1:
        raise ValueError("The probabilities sum to %s, not 1" % ea.ftext(total))


def _check_counter(inst, fixed):
    k, x = int(inst["bits"]), int(inst["start"])
    if x >= 2 ** k:
        raise ValueError("A %d-bit counter holds 0 to %s, and the start is %s" % (k, ea.grp(2 ** k - 1), ea.grp(x)))


def _am_ops(toks, words, repeat, needs):
    """Mirror of amiOps."""
    out, i = [], 0
    while i < len(toks):
        t = toks[i]
        if t.isdigit():
            raise ValueError('Operations, entry %d: "%s" follows no %s' % (i + 1, t, " or ".join(repeat + needs)))
        if t not in words:
            raise ValueError('Operations, entry %d: "%s" should be %s or %s' % (i + 1, t, ", ".join(words[:-1]), words[-1]))
        n = None
        if i + 1 < len(toks) and toks[i + 1].isdigit():
            n = int(toks[i + 1])
            i += 1
        if n is not None and not 1 <= n <= 1000:
            raise ValueError("Operations, entry %d: the number after %s is from 1 to 1000, and it is %s" % (i + 1, t, toks[i]))
        if t in needs:
            if n is None:
                raise ValueError("Operations, entry %d: %s needs a number after it" % (i + 1, t))
            out.append((t, n))
        else:
            out.extend([(t, None)] * (1 if n is None else n))
        if len(out) > 1000:
            raise ValueError("Operations: this lab runs at most 1000 operations, and these are more")
        i += 1
    return out


def _check_stack(inst, fixed):
    s = 0
    for idx, (op, k) in enumerate(_am_ops(inst["ops"], ["push", "pop", "multipop"], ["push", "pop"], ["multipop"])):
        if op == "push":
            s += 1
        elif op == "pop":
            if s == 0:
                raise ValueError("Operation %d pops an empty stack" % (idx + 1))
            s -= 1
        else:
            s -= min(s, k)


def _check_table(inst, fixed):
    num = 0
    for idx, (op, _k) in enumerate(_am_ops(inst["ops"], ["insert", "delete"], ["insert", "delete"], [])):
        if op == "insert":
            num += 1
        else:
            if num == 0:
                raise ValueError("Operation %d deletes from an empty table" % (idx + 1))
            num -= 1


def _distinct(keys):
    seen = set()
    for i, k in enumerate(keys):
        if k in seen:
            raise ValueError("Keys, entry %d: %d is already in the tree; this lab inserts distinct keys" % (i + 1, k))
        seen.add(k)


def _check_rb_insert(inst, fixed):
    _distinct([int(k) for k in inst["keys"]])


def _check_btree(inst, fixed):
    _distinct([int(k) for k in inst["keys"]])


def _check_rb_check(inst, fixed):
    by, roots = {}, []
    for r in inst["nodes"]:
        k = int(r["key"])
        if k in by:
            raise ValueError("Nodes names %d twice" % k)
        by[k] = {"parent": None, "left": None, "right": None}
    for r in inst["nodes"]:
        k, par = int(r["key"]), r["parent"]
        if par == "-":
            roots.append(k)
            continue
        if not par.isdigit() or int(par) not in by:
            raise ValueError("%d's parent %s is not a key of the tree" % (k, par))
        y = int(par)
        if y == k:
            raise ValueError("%d is its own parent" % k)
        side = "left" if k < y else "right"
        if by[y][side] is not None:
            raise ValueError("%d has two %s children, %d and %d (a child smaller than its parent is its left child)"
                             % (y, side, by[y][side], k))
        by[y][side] = k
        by[k]["parent"] = y
    if len(roots) != 1:
        raise ValueError("The tree has %d roots (%s); give exactly one node the parent -"
                         % (len(roots), ", ".join(map(str, roots))) if roots else
                         "The tree has no root: give one node the parent -")
    lost = []
    for r in inst["nodes"]:
        z, steps = int(r["key"]), 0
        while by[z]["parent"] is not None and steps <= len(inst["nodes"]):
            z, steps = by[z]["parent"], steps + 1
        if z != roots[0]:
            lost.append(int(r["key"]))
    if lost:
        raise ValueError("The parents form a cycle through %s, which the root never reaches" % ", ".join(map(str, lost)))


def _fh_ops(toks):
    """Mirror of fhiOps."""
    out, i = [], 0

    def num(j, after):
        if j >= len(toks) or not toks[j].isdigit():
            raise ValueError("Operations, entry %d: %s needs a key (a whole number) after it" % (j, after))
        v = int(toks[j])
        if v > 1000000:
            raise ValueError("Operations, entry %d: a key is at most 1,000,000, and it is %s" % (j + 1, toks[j]))
        return v

    while i < len(toks):
        t = toks[i]
        if t in ("insert", "delete"):
            out.append((t, num(i + 1, t), None))
            i += 2
        elif t == "decrease":
            k = num(i + 1, t)
            out.append((t, k, num(i + 2, "decrease %d" % k)))
            i += 3
        elif t in ("min", "extract"):
            out.append((t, None, None))
            i += 1
        elif t.isdigit():
            raise ValueError('Operations, entry %d: "%s" follows no insert, decrease or delete' % (i + 1, t))
        else:
            raise ValueError('Operations, entry %d: "%s" should be insert, min, extract, decrease or delete' % (i + 1, t))
    return out


def _check_fibheap(inst, fixed):
    ops = _fh_ops(inst["ops"])
    if len(ops) > 120:
        raise ValueError("Operations: this lab runs at most 120 operations, and there are %d" % len(ops))
    keys = set()
    for i, (op, k, v) in enumerate(ops):
        at = "Operation %d (%s%s%s)" % (i + 1, op, "" if k is None else " %d" % k, "" if v is None else " %d" % v)
        if op == "insert":
            if k in keys:
                raise ValueError("%s: %d is already in the heap; this lab keeps the keys distinct" % (at, k))
            keys.add(k)
        elif op in ("min", "extract"):
            if not keys:
                raise ValueError("%s: the heap is empty" % at)
            if op == "extract":
                keys.remove(min(keys))
        elif op == "decrease":
            if k not in keys:
                raise ValueError("%s: %d is not in the heap" % (at, k))
            if v > k:
                raise ValueError("%s: the new key %d is greater than %d" % (at, v, k))
            if v != k and v in keys:
                raise ValueError("%s: %d is already in the heap; this lab keeps the keys distinct" % (at, v))
            keys.remove(k)
            keys.add(v)
        else:
            if k not in keys:
                raise ValueError("%s: %d is not in the heap" % (at, k))
            keys.remove(k)


def _check_veb(inst, fixed):
    u, toks = 2 ** (2 ** int(inst["k"])), inst["ops"]
    ops, i, words = [], 0, ("insert", "member", "successor", "delete")
    while i < len(toks):
        t = toks[i]
        if t.isdigit():
            raise ValueError('Operations, entry %d: "%s" follows no insert, member, successor or delete' % (i + 1, t))
        if t not in words:
            raise ValueError('Operations, entry %d: "%s" should be insert, member, successor or delete' % (i + 1, t))
        if i + 1 >= len(toks) or not toks[i + 1].isdigit():
            raise ValueError("Operations, entry %d: %s needs a number after it" % (i + 1, t))
        x = int(toks[i + 1])
        if x >= u:
            raise ValueError("Operations, entry %d: with u = %s an element is from 0 to %s, and it is %s"
                             % (i + 2, ea.grp(u), ea.grp(u - 1), toks[i + 1]))
        ops.append((t, x))
        i += 2
    if len(ops) > 60:
        raise ValueError("Operations: this lab runs at most 60 operations, and there are %d" % len(ops))
    members = set()
    for i, (op, x) in enumerate(ops):
        at = "Operation %d (%s %d)" % (i + 1, op, x)
        if op == "insert":
            if x in members:
                raise ValueError("%s: %d is already a member; VEB-TREE-INSERT assumes it is not" % (at, x))
            members.add(x)
        elif op == "delete":
            if x not in members:
                raise ValueError("%s: %d is not a member; VEB-TREE-DELETE assumes it is" % (at, x))
            members.remove(x)


def _check_bfs(inst, fixed):
    directed = inst["graph"] == "directed"
    verts, seen = list(inst["vertices"]), set()
    for i, e in enumerate(inst["edges"]):
        a, b = e["from"], e["to"]
        if not directed and a == b:
            raise ValueError("Edges, record %d: %s to itself is a self-loop, which an undirected graph does not have" % (i + 1, a))
        key = (a, b) if directed else tuple(sorted((a, b)))
        if key in seen:
            raise ValueError("Edges, record %d: the edge %s, %s is given twice" % (i + 1, a, b))
        seen.add(key)
        for v in (a, b):
            if v not in verts:
                verts.append(v)
    if inst["source"] not in verts:
        raise ValueError("The source %s is not a vertex of the graph" % inst["source"])
    if len(verts) > 30:
        raise ValueError("The graph has %d vertices; this lab takes at most 30" % len(verts))


# ---------------------------------------------------------------------------
# The modes: fields, tiles, rules (kit-contract.md section 2)
# ---------------------------------------------------------------------------

_KEY = ea.whole(0, 10 ** 6)

ROD = {
    "prefix": "rdi", "fn": "rdiCompute", "title": "Rod cutting", "js": RDI_JS,
    "views": {
        "cut": {
            "fields": [("prices", _int_list("Prices p_1 to p_n, for pieces of length 1 to n", 1, 20, "prices",
                                            ea.num(lo=0)), None)],
            "tiles": [("Best revenue r_n", "rdiRevenue"), ("Pieces", "rdiCuts"), ("CUT-ROD calls, 2^n", "rdiNaive"),
                      ("Ways to cut, 2^(n−1)", "rdiWays"), ("MEMOIZED-CUT-ROD-AUX calls", "rdiMemo"),
                      ("BOTTOM-UP inner-loop runs", "rdiInner")],
            "check": None, "subtitle": "naive, memoized and bottom-up rod cutting",
            "rules": "The rod's length n is the number of prices. r_j is the most a rod of length j sells for, "
                     "max over 1 ≤ i ≤ j of p_i + r_(j−i), with r_0 = 0; a tie keeps the smallest first piece i (the "
                     "book's strict comparison), and the pieces are read back from those first pieces. CUT-ROD's calls "
                     "obey T(0) = 1, T(n) = 1 + T(0) + … + T(n − 1), so T(n) = 2^n: the lab computes that count and "
                     "does not make the calls. MEMOIZED-CUT-ROD-AUX's calls are counted as they happen, the first one "
                     "included. The bottom-up count is the runs of the inner loop, one for each pair 1 ≤ i ≤ j ≤ n.",
            "js": RDI_VIEW_JS["cut"],
        },
    },
}

LCS = {
    "prefix": "lci", "fn": "lciCompute", "title": "Longest common subsequence", "js": LCI_JS,
    "views": {
        "table": {
            "fields": [("x", ea.field("X (letters, digits, . _ or -)", ea.NAME), None),
                       ("y", ea.field("Y (letters, digits, . _ or -)", ea.NAME), None)],
            "tiles": [("LCS length", "lciLength"), ("One LCS (PRINT-LCS)", "lciLcs"), ("Cells filled, m × n", "lciCells"),
                      ("Arrows in the b table", "lciArrows")],
            "check": _check_lcs, "subtitle": "the c and b tables of LCS-LENGTH",
            "rules": "Characters are compared exactly (A and a differ). LCS-LENGTH fills c[i, j] for i = 1 to m, row by "
                     "row, and j = 1 to n: when x_i = y_j it is c[i − 1, j − 1] + 1 with arrow ↖; otherwise, when "
                     "c[i − 1, j] ≥ c[i, j − 1], it is c[i − 1, j] with arrow ↑ (a tie goes up), else c[i, j − 1] with "
                     "arrow ←. Row 0 and column 0 are 0 and are not counted as filled. PRINT-LCS starts at (m, n), "
                     "prints x_i at every ↖ and follows the arrows to row or column 0.",
            "js": LCI_VIEW_JS["table"],
        },
    },
}

OBST = {
    "prefix": "obi", "fn": "obiCompute", "title": "Optimal binary search trees", "js": OBI_JS,
    "views": {
        "table": {
            "fields": [("p", _int_list("Key probabilities p_1 to p_n", 1, 8, "key probabilities", ea.num(lo=0)), None),
                       ("q", _int_list("Dummy probabilities q_0 to q_n", 2, 9, "dummy probabilities", ea.num(lo=0)), None),
                       ("scale", ea.field("Divide every entry by (1 when they are probabilities already)", ea.whole(1)), "1")],
            "tiles": [("Expected search cost e[1, n]", "obiCost"), ("The optimal tree", "obiTree"),
                      ("root[i, j], row i, j = i to n", "obiRoots"), ("Brute force over every tree", "obiBrute")],
            "check": _check_obst, "subtitle": "the e, w and root tables of OPTIMAL-BST",
            "rules": "Each entry is divided by the divisor, so whole-number weights over a common denominator give exact "
                     "fractions; the probabilities must then sum to exactly 1. The cost of a tree is the sum over the keys "
                     "k_i and the dummy keys d_i of (depth + 1) × probability, the root at depth 0. OPTIMAL-BST fills "
                     "w[i, j] = w[i, j − 1] + p_j + q_j and e[i, j] = min over i ≤ r ≤ j of e[i, r − 1] + e[r + 1, j] + "
                     "w[i, j], with e[i, i − 1] = w[i, i − 1] = q_(i−1), shortest ranges first; a tie keeps the smallest "
                     "root. The tree is written k_r(left right) with dummy leaves d_i. Up to 7 keys the lab also builds "
                     "every binary search tree on the keys and costs each one from its depths.",
            "js": OBI_VIEW_JS["table"],
        },
    },
}

_AM_TILES_COMMON = [("Actual cost, total", "amiActual"), ("Aggregate bound", "amiBound"),
                    ("Credit left (accounting)", "amiCredit"), ("Potential before and after", "amiPhi"),
                    ("Amortized cost, total (potential)", "amiAmortized"), ("Largest amortized cost of one operation", "amiMax")]

AMORTIZED = {
    "prefix": "ami", "fn": "amiCompute", "title": "Amortized analysis", "js": AMI_JS,
    "views": {
        "counter": {
            "fields": [("bits", ea.field("Bits k", ea.whole(1, 20)), None),
                       ("increments", ea.field("Increments n", ea.whole(1, 1000)), None),
                       ("start", ea.field("Start value (0 in the book)", ea.whole(0, 2 ** 20 - 1)), "0")],
            "tiles": _AM_TILES_COMMON[:1] + [("Flips of each bit", "amiPerBit")] + _AM_TILES_COMMON[1:]
                     + [("Counter after", "amiValue")],
            "check": _check_counter, "subtitle": "a k-bit binary counter, three ways",
            "rules": "INCREMENT costs the bits it flips: it resets the low run of 1s to 0 and sets the next 0 to 1 (when "
                     "every bit is 1 it resets them all, sets nothing, and the counter wraps to 0). Aggregate: from 0, "
                     "bit i flips ⌊n/2^i⌋ times, fewer than 2n flips in all. Accounting: setting a bit is charged 2 and "
                     "resetting one 0; the credit is the charges less the costs so far, starting at 0, and the least "
                     "credit is the lowest it went. Potential: Φ is the number of 1 bits, and an operation's amortized "
                     "cost is its actual cost + Φ after − Φ before.",
            "js": AMI_VIEW_JS["counter"],
        },
        "stack": {
            "fields": [("ops", _ops_list("Operations (push, pop, multipop k; a number after push or pop repeats it)", 400),
                        None)],
            "tiles": _AM_TILES_COMMON + [("Operations run", "amiOpCount")],
            "check": _check_stack, "subtitle": "a stack with MULTIPOP, three ways",
            "rules": "PUSH and POP cost 1; MULTIPOP k pops min(s, k) objects from a stack of s and costs that many; a POP "
                     "of an empty stack is refused. Aggregate: an object is popped at most once for each time it is "
                     "pushed, so the total is at most 2 × the pushes. Accounting: PUSH is charged 2, POP and MULTIPOP 0; "
                     "the credit is the charges less the costs so far. Potential: Φ is the number of objects on the "
                     "stack; amortized cost = actual + Φ after − Φ before.",
            "js": AMI_VIEW_JS["stack"],
        },
        "table": {
            "fields": [("ops", _ops_list("Operations (insert, delete; a number after one repeats it)", 400), None)],
            "tiles": [(label, cid) for label, cid in _AM_TILES_COMMON if cid != "amiCredit"]
                     + [("Amortized less actual, total", "amiCredit"), ("Items and slots after", "amiSize"),
                        ("Resizes", "amiResize")],
            "check": _check_table, "subtitle": "a dynamic table that doubles when full and halves at a quarter",
            "rules": "Costs are elementary insertions and deletions. TABLE-INSERT into a table with no slots allocates "
                     "1 and costs 1; into a full table it allocates twice the slots, moves the num items and inserts, "
                     "costing num + 1; otherwise 1. TABLE-DELETE costs 1; when it leaves the table less than 1/4 full "
                     "it halves the slots and moves the num items left, costing num + 1; when it leaves no item the "
                     "table is freed (size 0, the book's assumption), with nothing to move. Φ = 2·num − size when the "
                     "load factor num/size is at least 1/2 (an empty table counts as 1), else size/2 − num (equation "
                     "17.6); amortized cost = actual + Φ after − Φ before. The bound is the book's: at most 3 an "
                     "insertion and 2 a deletion.",
            "js": AMI_VIEW_JS["table"],
        },
    },
}

_RB_SHAPE = ("The height counts the edges from the root down to its deepest NIL leaf, so a lone node has height 1; "
             "black-height bh(x) counts the black nodes below x on a path down to a NIL leaf, the NIL leaf counted "
             "and x not. Lemma 13.1's bound 2 lg(n + 1) is printed to two places, rounded half up by exact integer "
             "comparison, with = only when it is exact.")

RBTREE = {
    "prefix": "rbi", "fn": "rbiCompute", "title": "Red-black trees", "js": RBI_JS,
    "views": {
        "check": {
            "fields": [("nodes", ea.rec("Nodes (key, color: red or black, parent key; - for the root)",
                                        [("key", _KEY), ("color", ea.word("red", "black")), ("parent", ea.PARENT)],
                                        unique=True, rows=4), None)],
            "tiles": [("A red-black tree", "rbiVerdict"), ("1. Every node red or black", "rbiP1"),
                      ("2. The root black", "rbiP2"), ("3. Every leaf (NIL) black", "rbiP3"),
                      ("4. A red node's children black", "rbiP4"), ("5. Equal black counts below each node", "rbiP5"),
                      ("Search-tree order", "rbiBst"), ("Nodes n", "rbiNodes"), ("Black-height of the root", "rbiBh"),
                      ("Height", "rbiHeight"), ("Lemma 13.1 bound", "rbiBound")],
            "check": _check_rb_check, "subtitle": "the five red-black properties, checked",
            "rules": "Each record is a node: its key, its color and its parent's key. A child with a smaller key than "
                     "its parent is the left child, otherwise the right; every missing child is a black NIL leaf. "
                     "Property 4 names the first red node with a red child in preorder (root, left subtree, right "
                     "subtree). Property 5 names the first node, in postorder (left subtree, right subtree, node), whose "
                     "two sides have different numbers of black nodes down to their NIL leaves. Search-tree order names "
                     "the first pair out of order in the inorder walk. " + _RB_SHAPE,
            "js": RBI_VIEW_JS["check"],
        },
        "insert": {
            "fields": [("keys", _int_list("Keys, inserted in this order", 1, 31, "keys", _KEY), None)],
            "tiles": [("Fix-up cases, in all", "rbiCases"), ("Recolorings", "rbiRecolor"), ("Rotations", "rbiRotate"),
                      ("Most rotations in one insertion", "rbiMostRot"), ("Final tree", "rbiFinal"),
                      ("Black-height of the root", "rbiBh"), ("Height", "rbiHeight"), ("Lemma 13.1 bound", "rbiBound")],
            "check": _check_rb_insert, "subtitle": "RB-INSERT and RB-INSERT-FIXUP, counted",
            "rules": "Each key goes in by RB-INSERT (down the tree, left when smaller, as a red leaf), then "
                     "RB-INSERT-FIXUP runs while z's parent is red. With z's parent a left child: case 1, the uncle is "
                     "red; case 2, the uncle is black and z is a right child (z moves up, one left rotation); case 3, "
                     "the uncle is black and z is a left child (one right rotation). 1′, 2′ and 3′ are the same cases "
                     "with left and right exchanged. A recoloring is a color assignment that changes a node's color: "
                     "case 1 makes 3, case 3 makes 2, and the final root := black counts 1 when the root was red. The "
                     "new node's red is not a recoloring. The final tree is written key and color (R or B), then its "
                     "two subtrees in parentheses, - for a NIL child. " + _RB_SHAPE,
            "js": RBI_VIEW_JS["insert"],
        },
    },
}

BTREE = {
    "prefix": "bti", "fn": "btiCompute", "title": "B-trees", "js": BTI_JS,
    "views": {
        "insert": {
            "fields": [("t", ea.field("Minimum degree t", ea.whole(2, 5)), None),
                       ("keys", _int_list("Keys, inserted in this order", 1, 60, "keys", _KEY), None)],
            "tiles": [("Height h", "btiHeight"), ("Nodes", "btiNodes"), ("Splits", "btiSplits"),
                      ("DISK-READs", "btiReads"), ("DISK-WRITEs", "btiWrites"),
                      ("Theorem 18.1 bound log_t((n + 1)/2)", "btiBound"), ("The tree by level, root first", "btiLevels")],
            "check": _check_btree, "subtitle": "B-TREE-INSERT, splitting full nodes on the way down",
            "rules": "A node holds t − 1 to 2t − 1 keys (the root at least 1). The tree starts as B-TREE-CREATE's empty "
                     "root; that DISK-WRITE is not in the totals. B-TREE-INSERT splits a full root first (a new root "
                     "above it), then B-TREE-INSERT-NONFULL walks down: at a leaf it inserts the key and writes the leaf "
                     "(1 write); at an inner node it reads the child it will descend to (1 read; the root is never read, "
                     "it stays in memory) and, when that child is full, splits it before descending, which writes the "
                     "two halves and the parent (3 writes). After a split the walk takes the new right half without "
                     "reading it. Height counts the edges from the root to a leaf, so a lone root has height 0. The "
                     "bound is printed to two places, rounded half up by exact integer comparison.",
            "js": BTI_VIEW_JS["insert"],
        },
    },
}

_FH_OPS = ("ops", _ops_list("Operations (insert k, min, extract, decrease k v, delete k)", 400, rows=3), None)

_FH_RULES = ("Keys are distinct whole numbers and name their nodes. The root list is a circle: INSERT and a cut put "
             "the new root just left of H.min; EXTRACT-MIN puts the minimum's children where it was, in their child "
             "order, then CONSOLIDATE takes every root once, starting at the old minimum's right neighbour and going "
             "right, linking the larger key of two equal-degree roots under the smaller (as its last child, mark "
             "cleared) and rebuilding the root list in order of degree. DELETE is DECREASE-KEY to minus infinity, then "
             "EXTRACT-MIN. Actual cost, in steps: INSERT 1; MIN 1; EXTRACT-MIN 1 for the minimum + 1 for each child "
             "moved to the root list + 1 for each root CONSOLIDATE takes (a link is part of taking a root; the pass "
             "over the degree array is not counted); DECREASE-KEY 1 + 1 for each cut, its own and the cascading ones; "
             "DELETE the sum of its two parts. Φ = t(H) + 2m(H), roots plus twice the marked nodes; amortized cost = "
             "actual + ΔΦ.")

FIBHEAP = {
    "prefix": "fhi", "fn": "fhiCompute", "title": "Fibonacci heaps", "js": FHI_JS,
    "views": {
        "ops": {
            "fields": [_FH_OPS],
            "tiles": [("Actual cost, total", "fhiActual"), ("Amortized cost, total", "fhiAmortized"),
                      ("Potential now", "fhiPhi"), ("Largest amortized cost, by operation", "fhiMostAm"),
                      ("Root list from H.min", "fhiRoots"), ("Degree against D(n)", "fhiDegree"), ("Nodes n", "fhiN")],
            "check": _check_fibheap, "subtitle": "lazy insertion and consolidation in EXTRACT-MIN",
            "rules": _FH_RULES + " D(n) = ⌊log_φ n⌋ is found exactly, from φ^k = (L_k + F_k√5)/2.",
            "js": FHI_VIEW_JS["ops"],
        },
        "cascade": {
            "fields": [_FH_OPS],
            "tiles": [("Cuts", "fhiCuts"), ("Cascading cuts among them", "fhiCascades"),
                      ("Calls to CASCADING-CUT", "fhiCalls"), ("Marked now", "fhiMarked"),
                      ("Largest amortized DECREASE-KEY", "fhiMostDec"), ("size(x) ≥ F(degree + 2)", "fhiLemma"),
                      ("Degree against D(n)", "fhiDegree"), ("Root list from H.min", "fhiRoots")],
            "check": _check_fibheap, "subtitle": "cuts, cascading cuts and the degree bound",
            "rules": _FH_RULES + " DECREASE-KEY cuts x from its parent y when the new key is below y's, then calls "
                     "CASCADING-CUT on y: a root does nothing, an unmarked node is marked, a marked node is cut and the "
                     "call goes on to its parent. A cut unmarks the node it moves. Lemma 19.4 is checked at every node: "
                     "size(x), x and its descendants, against F(k + 2) for degree k, with F(1) = F(2) = 1; the closest "
                     "node has the least size/F.",
            "js": FHI_VIEW_JS["cascade"],
        },
    },
}

VEB = {
    "prefix": "vbi", "fn": "vbiCompute", "title": "van Emde Boas trees", "js": VBI_JS,
    "views": {
        "ops": {
            "fields": [("k", ea.field("k, where u = 2^(2^k) (1 to 4: u = 4, 16, 256 or 65,536)", ea.whole(1, 4)), None),
                       ("ops", _ops_list("Operations (insert x, member x, successor x, delete x)", 120), None)],
            "tiles": [("Universe", "vbiU"), ("proto-vEB calls, total", "vbiProto"), ("vEB calls, total", "vbiVeb"),
                      ("Most calls in one operation", "vbiMost"), ("Answers", "vbiAnswers"),
                      ("Members after", "vbiMembers"), ("vEB top level", "vbiTop")],
            "check": _check_veb, "subtitle": "proto-vEB against vEB, calls counted",
            "rules": "Both structures run every operation, x split into high(x) = ⌊x/√u⌋ and low(x) = x mod √u. A call "
                     "is one call of a structure procedure, the top call included. proto-vEB counts PROTO-vEB-MEMBER, "
                     "-MINIMUM, -SUCCESSOR, -INSERT and -DELETE; the book leaves deletion to Exercise 20.2-2, and the "
                     "lab deletes from the cluster, asks that cluster's minimum, and deletes from the summary when it is "
                     "empty. vEB counts VEB-TREE-MEMBER, -SUCCESSOR, -INSERT and -DELETE; VEB-TREE-MINIMUM and -MAXIMUM "
                     "read a field and VEB-EMPTY-TREE-INSERT sets two, and none of the three is counted. A vEB tree "
                     "keeps its minimum out of its clusters, so the top level lists it apart; a cluster lists the low parts it "
                     "holds, each with its element in parentheses.",
            "js": VBI_VIEW_JS["ops"],
        },
    },
}

BFS = {
    "prefix": "bfi", "fn": "bfiCompute", "title": "Breadth-first search", "js": BFI_JS,
    "views": {
        "search": {
            "fields": [("edges", ea.rec("Edges (from, to)", [("from", ea.NAME), ("to", ea.NAME)], rows=3, lo=0), None),
                       ("graph", ea.choice("Graph", "undirected", "directed"), None),
                       ("source", ea.field("Source s", ea.NAME), None),
                       ("vertices", dict(what="Vertices in order (optional; adds vertices no edge names)", control="text",
                                         kind="list", lo=0, hi=30, things="vertices", each=dict(ea.NAME)), "")],
            "tiles": [("Distance d from s", "bfiDist"), ("Parent π (breadth-first tree)", "bfiParent"),
                      ("Vertices by layer", "bfiLayers"), ("Enqueued", "bfiEnqueued"),
                      ("Adjacency entries examined", "bfiScanned"), ("Not reachable", "bfiUnreached")],
            "check": _check_bfs, "subtitle": "BFS distances and the breadth-first tree",
            "rules": "Vertices are listed in the order given, then in the order the edges first name them. Adjacency "
                     "lists follow the edges' order: an undirected edge u, v puts v on u's list and u on v's, a directed "
                     "one v on u's only. BFS colors s gray at distance 0 and enqueues it; it dequeues u, examines every "
                     "entry v of u's list in order, and a white v becomes gray with d = d[u] + 1 and π = u and is "
                     "enqueued. An entry examined counts once, whatever its color; the lists hold 2E entries in an "
                     "undirected graph and E in a directed one. A vertex never reached keeps d = ∞.",
            "js": BFI_VIEW_JS["search"],
        },
    },
}

SPECS = {"rod": ROD, "lcs": LCS, "obst": OBST, "amortized": AMORTIZED, "rbtree": RBTREE, "btree": BTREE,
         "fibheap": FIBHEAP, "veb": VEB, "bfs": BFS}


def rod_lab(cfg):
    return mode_lab(cfg, "rod", ROD)


def lcs_lab(cfg):
    return mode_lab(cfg, "lcs", LCS)


def obst_lab(cfg):
    return mode_lab(cfg, "obst", OBST)


def amortized_lab(cfg):
    return mode_lab(cfg, "amortized", AMORTIZED)


def rbtree_lab(cfg):
    return mode_lab(cfg, "rbtree", RBTREE)


def btree_lab(cfg):
    return mode_lab(cfg, "btree", BTREE)


def fibheap_lab(cfg):
    return mode_lab(cfg, "fibheap", FIBHEAP)


def veb_lab(cfg):
    return mode_lab(cfg, "veb", VEB)


def bfs_lab(cfg):
    return mode_lab(cfg, "bfs", BFS)


MODES = {"rod": rod_lab, "lcs": lcs_lab, "obst": obst_lab, "amortized": amortized_lab, "rbtree": rbtree_lab,
         "btree": btree_lab, "fibheap": fibheap_lab, "veb": veb_lab, "bfs": bfs_lab}

__all__ = ["MODES", "SPECS"]
