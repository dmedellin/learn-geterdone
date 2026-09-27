"""Course 9, the linear-systems half: five modes over one transition matrix.

Course 9 is the second course on this path to take TWO kits, for the reason
course 4 does: `markov` solves linear systems and `birthdeath` draws a queue,
and forcing them into one kit would have produced a mode that answers a
different question under the same controls. The exception is deliberate and it
is recorded here and in the registry.

THE ONE SENTENCE THIS KIT EXISTS TO MAKE TRUE. The path's key line reads

    piP = pi                a steady state is a linear system, not a limit

and mode `steady` is that claim made checkable rather than repeated. The steady
state is computed by `or_core.steadyState`, which builds the n balance equations
pi(P - I) = 0, DROPS ONE OF THEM BY NAME because they are dependent -- every
column of P - I sums to zero -- puts sum pi = 1 in its place, and runs exact
Gauss-Jordan over rationals. Nothing iterates. The answer is a solution of a
linear system and it is exact.

Beside it the page runs the thing readers think a steady state is: repeated
multiplication, in floating point, for as many steps as they like. Three things
come out of the comparison and all three are computed on the page.

  * On an aperiodic irreducible chain the iteration agrees with the solve to
    about fifteen decimal places and then stops improving, because it has run
    out of double. The page prints the number of places, and the disagreement.
  * On a PERIODIC chain -- the `cycle` preset is a 3-cycle -- the linear system
    still has a unique solution, (1/3, 1/3, 1/3), and P^n never converges to
    anything at all: it returns to the identity every third step, for ever. The
    page shows both, side by side. That is the whole argument in one preset.
  * On a REDUCIBLE chain with two recurrent classes -- the `split` preset --
    the system is rank deficient and there is no unique steady state.
    `steadyState` reports `unique: false` and the page says so rather than
    printing one of the infinitely many answers as though it were the answer.
    With only ONE recurrent class -- the `leaky` preset -- it is unique again,
    and it puts exactly zero on every transient state.

WHAT IS STATED AND NOT PROVED, AND WHERE IT SAYS SO. The path's footer names
three results it states without proof, and one of them is this kit's: the
convergence of P^n to the steady state. `convergenceNote` below is the sentence
that says so, and mode `steady` and mode `chain` both print it. The hypotheses
-- irreducible and aperiodic -- are COMPUTED by `chainClasses` and `chainPeriod`
in mode `classify`, so the reader can check that a chain satisfies them even
though the theorem is not proved here. A stated theorem whose hypotheses are
checkable is a different thing from a stated theorem taken on trust.

NOTHING HERE ROUNDS EXCEPT THE FLOATING-POINT COLUMN, WHICH IS THE POINT.
P^12 on the `five` preset has entries fifteen digits over sixteen -- past what
a double can hold -- and `chainPow` computes them exactly by repeated Mmul. The
float column is labelled as an approximation everywhere it appears, and it is
there to be beaten.

The five modes, one lesson each.

  chain     the matrix as an object: row sums checked, the support digraph
            drawn, P^n exact at any n, and a starting distribution pushed
            forward n steps
  classify  communicating classes from the support digraph, recurrent against
            transient, and the period as a gcd of cycle lengths
  steady    piP = pi solved as a linear system, with the dropped equation
            named, verified on the page, and set beside a power iteration
  absorb    N = (I - Q)^-1 as the SUM of the powers of Q, the expected steps to
            absorption, and which absorbing state the chain ends in
  mdp       policy iteration: each policy evaluated by an exact linear solve,
            improved greedily, with value iteration shown converging to the
            answer the solve already has
"""

import json

from .algebra_core import RATIONAL_JS
from .algebra_systems import FORMAT_JS, MATRIX_JS
from .common import Lab
from .or_core import CHAIN_JS, ORFMT_JS

# ---------------------------------------------------------------------------
# The arithmetic this kit adds. Top-level functions, no DOM: scripts/mathcheck.js
# extracts this block and calls every one of them, the two renderers included --
# they return strings of SVG, so the drawing is assertable.
# ---------------------------------------------------------------------------

MARKOV_JS = r"""
  /* ------------------------------------------------- is it a transition matrix

     A matrix whose rows do not sum to one is not a chain, and every quantity
     below would still compute on it and mean nothing. So this refuses, names
     the row, and the modes blank rather than paint. That is the difference
     between a lab and a calculator with a Markov-shaped skin. */
  function chainValid(M) {
    if (!M || !M.length) return { ok: false, why: 'there is no matrix here' };
    var n = M.length, i, j;
    for (i = 0; i < n; i += 1) if (M[i].length !== n) {
      return { ok: false, why: 'a transition matrix is square, and row ' + (i + 1) + ' has '
        + M[i].length + ' entries against ' + n + ' rows' };
    }
    for (i = 0; i < n; i += 1) {
      for (j = 0; j < n; j += 1) {
        if (Rsign(M[i][j]) < 0) {
          return { ok: false, why: 'entry (' + (i + 1) + ',' + (j + 1) + ') is '
            + Rtext(M[i][j]) + ', and a probability cannot be negative' };
        }
        if (Rcmp(M[i][j], R1) > 0) {
          return { ok: false, why: 'entry (' + (i + 1) + ',' + (j + 1) + ') is '
            + Rtext(M[i][j]) + ', and a probability cannot exceed 1' };
        }
      }
    }
    var sums = [];
    for (i = 0; i < n; i += 1) {
      var s = R0;
      for (j = 0; j < n; j += 1) s = Radd(s, M[i][j]);
      sums.push(s);
      if (!Requ(s, R1)) {
        return { ok: false, sums: sums, row: i, why: 'row ' + (i + 1) + ' sums to ' + Rtext(s)
          + ', not to 1 -- from state ' + (i + 1) + ' the chain has to go somewhere, and these '
          + 'probabilities say it goes ' + (Rcmp(s, R1) > 0 ? 'more than' : 'less than')
          + ' once' };
      }
    }
    return { ok: true, sums: sums, n: n, why: 'every row sums to exactly 1, so this is a transition matrix' };
  }
  /* A distribution typed by a reader: non-negative and summing to one. Not
     normalised silently -- a distribution that does not sum to one is a typo,
     and rescaling it answers a question nobody asked. */
  function readDist(text, n) {
    var parts = String(text).trim().split(/[\s,;]+/).filter(function (t) { return t.length; });
    if (parts.length !== n) return null;
    var out = [], total = R0, k;
    for (k = 0; k < parts.length; k += 1) {
      var v = Rread(parts[k]);
      if (v === null || Rsign(v) < 0) return null;
      out.push(v); total = Radd(total, v);
    }
    return Requ(total, R1) ? out : null;
  }
  /* v P, one step of the row vector -- which is the direction a distribution
     moves and the reason pi is a LEFT eigenvector. */
  function pushDist(v, P) {
    var n = P.length, out = [], i, j;
    for (j = 0; j < n; j += 1) {
      var s = R0;
      for (i = 0; i < n; i += 1) s = Radd(s, Rmul(v[i], P[i][j]));
      out.push(s);
    }
    return out;
  }
  /* v P^n, kept step by step so the page can show the walk rather than the
     destination. Exact: the denominators grow and that is worth seeing. */
  function distWalk(v, P, n) {
    var rows = [v.slice()], k;
    for (k = 0; k < n; k += 1) rows.push(pushDist(rows[rows.length - 1], P));
    return rows;
  }

  /* --------------------------------------------- the check the page performs

     pi is claimed to satisfy piP = pi and to sum to 1. Neither is assumed here:
     piP is recomputed from the pi that came out of the solve, compared entry by
     entry with Requ -- exact equality of rationals, not "close enough" -- and
     the sum is added up. A page that asserted this instead of computing it
     would be a page a reader has to trust. */
  function steadyCheck(P, pi) {
    if (!pi || pi.indexOf(null) >= 0) {
      return { ok: false, residual: null, sum: null,
               why: 'the system has no unique solution, so there is nothing to check' };
    }
    var moved = pushDist(pi, P), n = pi.length, i, worst = null, at = -1;
    for (i = 0; i < n; i += 1) {
      var d = Rsub(moved[i], pi[i]);
      if (worst === null || Rcmp(Rabs(d), Rabs(worst)) > 0) { worst = d; at = i; }
    }
    var sum = R0;
    for (i = 0; i < n; i += 1) sum = Radd(sum, pi[i]);
    var exact = Rzero(worst) && Requ(sum, R1);
    return { ok: exact, moved: moved, residual: worst, at: at, sum: sum,
             why: exact
               ? 'the page recomputed piP from the solution and every entry came back EXACTLY equal to '
                 + 'pi, and the entries sum to exactly 1'
               : 'piP differs from pi in entry ' + (at + 1) + ' by ' + Rtext(worst)
                 + ' and the entries sum to ' + Rtext(sum) + ' -- either would mean the solve is wrong' };
  }

  /* --------------------------------- the iteration, which is a DIFFERENT thing

     This is the only floating-point arithmetic in the kit and it exists to be
     compared against. A rational is turned into a double through Rfixed's
     BigInt long division rather than through Number(n)/Number(d), because this
     path produces rationals whose numerator and denominator both overflow a
     double while their RATIO is perfectly ordinary. */
  function toFloat(r) { return parseFloat(Rfixed(r, 17)); }
  function floatMatrix(P) {
    return P.map(function (row) { return row.map(toFloat); });
  }
  /* v P^n in doubles, keeping only the vector. The whole point of the panel is
     that this can be run for thousands of steps and still not be the answer. */
  function floatWalk(Pf, start, n) {
    var v = start.slice(), out = [], i, j, k;
    for (k = 0; k < n; k += 1) {
      var next = [];
      for (j = 0; j < Pf.length; j += 1) {
        var s = 0;
        for (i = 0; i < Pf.length; i += 1) s += v[i] * Pf[i][j];
        next.push(s);
      }
      v = next;
      if (k < 8 || k === n - 1) out.push(v.slice());
    }
    return { v: v, sample: out };
  }
  /* How far the iteration got, and how far it did not. `places` is the number
     of decimal places the two agree to, floored -- and it is computed from the
     difference rather than assumed from the step count. */
  function floatGap(pi, v) {
    var worst = 0, at = -1, i;
    for (i = 0; i < pi.length; i += 1) {
      var d = Math.abs(v[i] - toFloat(pi[i]));
      if (d > worst) { worst = d; at = i; }
    }
    var places = worst === 0 ? Infinity : Math.floor(-Math.log(worst) / Math.LN10);
    return { gap: worst, at: at, places: places,
             why: worst === 0
               ? 'the iteration has reached the exact answer to every digit a double can hold, which is '
                 + 'not the same as reaching it'
               : 'the iteration is out by ' + worst.toExponential(3) + ' in entry ' + (at + 1)
                 + ', which is agreement to about ' + places + ' decimal places' };
  }
  /* The EXACT distance from P^n to the steady state, as a rational, which is
     what the float column cannot give. */
  function exactGap(P, pi, n) {
    if (!pi || pi.indexOf(null) >= 0) return null;
    var Pn = chainPow(P, n), worst = R0, at = null, i, j;
    for (i = 0; i < P.length; i += 1) {
      for (j = 0; j < P.length; j += 1) {
        var d = Rabs(Rsub(Pn[i][j], pi[j]));
        if (Rcmp(d, worst) > 0) { worst = d; at = [i, j]; }
      }
    }
    return { Pn: Pn, gap: worst, at: at };
  }
  /* Does P^n move at all between n and n + period? On a periodic chain it does
     not settle, it CYCLES, and saying "it has not converged yet" about a
     3-cycle is the misconception this answers. Exact equality, so the answer is
     yes or no rather than a tolerance. */
  function powerCycles(P, upto) {
    var seen = [], k;
    var cur = Mid(P.length);
    for (k = 0; k <= upto; k += 1) {
      var i;
      for (i = 0; i < seen.length; i += 1) if (Mequ(seen[i], cur)) {
        return { repeats: true, first: i, again: k, period: k - i,
                 why: 'P^' + k + ' is EXACTLY P^' + i + ', so the powers repeat with period ' + (k - i)
                   + ' and no limit exists -- the sequence does not fail to converge slowly, it does not '
                   + 'converge at all' };
      }
      seen.push(cur);
      cur = Mmul(cur, P);
    }
    return { repeats: false, first: -1, again: -1, period: 0,
             why: 'no power up to P^' + upto + ' repeats an earlier one exactly' };
  }
  /* The sentence the path's footer requires. One function, so the wording
     cannot drift between the two modes that print it. */
  function convergenceNote() {
    return 'The convergence of P&#8319; to the steady state is <strong>stated on this path and not '
      + 'proved</strong> &mdash; it is one of the three results the footer names. What is computed here '
      + 'is the steady state itself, as the exact solution of a linear system, and the hypotheses the '
      + 'theorem needs: mode <em>classify</em> checks irreducibility and aperiodicity on the same matrix.';
  }

  /* ------------------------------------------------ drawing the support graph

     The digraph of i -> j whenever P[i][j] > 0. Nodes on a circle, arcs bowed
     so an antiparallel pair does not hide behind itself, self-loops as a
     circle above the node. A string, with no element involved. */
  function chainSvg(P, opts) {
    opts = opts || {};
    var n = P.length, w = opts.w || 660, hgt = opts.h || 300;
    var cx = w / 2, cy = hgt / 2 + 4, rad = Math.min(w, hgt) / 2 - 54;
    var pos = [], i, j;
    for (i = 0; i < n; i += 1) {
      var a = -Math.PI / 2 + 2 * Math.PI * i / n;
      pos.push([cx + rad * Math.cos(a), cy + rad * Math.sin(a)]);
    }
    var defs = '<defs><marker id="mkArrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" '
      + 'markerHeight="6" orient="auto-start-reverse">'
      + '<path d="M 0 0 L 10 5 L 0 10 z" fill="var(--muted)" /></marker></defs>';
    var arcs = '', labels = '';
    for (i = 0; i < n; i += 1) {
      for (j = 0; j < n; j += 1) {
        if (Rzero(P[i][j])) continue;
        var tone = opts.arcTone ? opts.arcTone(i, j) : 'muted';
        if (i === j) {
          var lx = pos[i][0], ly = pos[i][1];
          var ox = (lx - cx) / (rad || 1) * 26, oy = (ly - cy) / (rad || 1) * 26;
          arcs += '<circle cx="' + (lx + ox).toFixed(1) + '" cy="' + (ly + oy).toFixed(1)
            + '" r="13" fill="none" stroke="var(--' + tone + ')" stroke-width="1.4" />';
          labels += '<text x="' + (lx + ox * 1.9).toFixed(1) + '" y="' + (ly + oy * 1.9).toFixed(1)
            + '" font-size="10" fill="var(--' + tone + ')" text-anchor="middle">' + Rtext(P[i][j]) + '</text>';
          continue;
        }
        var x1 = pos[i][0], y1 = pos[i][1], x2 = pos[j][0], y2 = pos[j][1];
        var dx = x2 - x1, dy = y2 - y1, len = Math.sqrt(dx * dx + dy * dy) || 1;
        var ux = dx / len, uy = dy / len;
        var sx = x1 + ux * 19, sy = y1 + uy * 19, ex = x2 - ux * 22, ey = y2 - uy * 22;
        /* bow every arc the same way round its own direction, so i->j and j->i
           are two visibly different curves rather than one line drawn twice */
        var mx = (sx + ex) / 2 - uy * 16, my = (sy + ey) / 2 + ux * 16;
        arcs += '<path d="M ' + sx.toFixed(1) + ' ' + sy.toFixed(1) + ' Q ' + mx.toFixed(1) + ' '
          + my.toFixed(1) + ' ' + ex.toFixed(1) + ' ' + ey.toFixed(1) + '" fill="none" stroke="var(--'
          + tone + ')" stroke-width="1.4" marker-end="url(#mkArrow)" />';
        labels += '<text x="' + mx.toFixed(1) + '" y="' + (my - 3).toFixed(1) + '" font-size="10" '
          + 'fill="var(--' + tone + ')" text-anchor="middle">' + Rtext(P[i][j]) + '</text>';
      }
    }
    var nodes = '';
    for (i = 0; i < n; i += 1) {
      var ntone = opts.nodeTone ? opts.nodeTone(i) : 'cyan';
      nodes += '<circle cx="' + pos[i][0].toFixed(1) + '" cy="' + pos[i][1].toFixed(1)
        + '" r="18" fill="var(--panel-solid)" stroke="var(--' + ntone + ')" stroke-width="2" />'
        + '<text x="' + pos[i][0].toFixed(1) + '" y="' + (pos[i][1] + 4).toFixed(1)
        + '" font-size="12" font-weight="700" fill="var(--' + ntone + ')" text-anchor="middle">'
        + (opts.names && opts.names[i] ? opts.names[i] : String(i + 1)) + '</text>';
    }
    return defs + arcs + labels + nodes;
  }
  /* A distribution as a row of bars, for watching one push forward. */
  function distSvg(rows, opts) {
    opts = opts || {};
    var w = opts.w || 660, hgt = opts.h || 190, L = 34, T = 14, B = 26;
    if (!rows.length) return '<text x="14" y="24" font-size="11" fill="var(--muted)">nothing yet</text>';
    var n = rows[0].length, steps = rows.length;
    var iw = (w - L - 14) / steps, out = '';
    out += '<line x1="' + L + '" y1="' + (T + hgt - T - B) + '" x2="' + (w - 14) + '" y2="'
      + (T + hgt - T - B) + '" stroke="var(--line-strong)" />';
    var base = hgt - B, k, i;
    for (k = 0; k < steps; k += 1) {
      var bw = Math.max(1.5, (iw - 6) / n);
      for (i = 0; i < n; i += 1) {
        var v = toFloat(rows[k][i]);
        var bh = (base - T) * Math.max(0, Math.min(1, v));
        out += '<rect x="' + (L + k * iw + 3 + i * bw).toFixed(2) + '" y="' + (base - bh).toFixed(2)
          + '" width="' + Math.max(1, bw - 1).toFixed(2) + '" height="' + bh.toFixed(2)
          + '" rx="1.5" fill="var(--' + ['cyan', 'purple', 'green', 'amber', 'blue', 'red'][i % 6]
          + ')" opacity="0.85" />';
      }
      if (steps <= 18) {
        out += '<text x="' + (L + k * iw + iw / 2).toFixed(2) + '" y="' + (base + 13)
          + '" font-size="9" fill="var(--muted)" text-anchor="middle">' + k + '</text>';
      }
    }
    out += '<text x="4" y="' + (T + 8) + '" font-size="10" fill="var(--muted)">1</text>'
      + '<text x="4" y="' + base + '" font-size="10" fill="var(--muted)">0</text>';
    if (opts.target) {
      for (i = 0; i < opts.target.length; i += 1) {
        var ty = base - (base - T) * Math.max(0, Math.min(1, toFloat(opts.target[i])));
        out += '<line x1="' + L + '" y1="' + ty.toFixed(2) + '" x2="' + (w - 14) + '" y2="' + ty.toFixed(2)
          + '" stroke="var(--' + ['cyan', 'purple', 'green', 'amber', 'blue', 'red'][i % 6]
          + ')" stroke-width="1" stroke-dasharray="3 3" opacity="0.7" />';
      }
    }
    return out;
  }
"""

_CORE_JS = RATIONAL_JS + FORMAT_JS + MATRIX_JS + ORFMT_JS + CHAIN_JS + MARKOV_JS


# ---------------------------------------------------------------------------
# The worked examples, typed the way a reader types them.
#
# `cycle` is the preset that carries mode `steady`: a 3-cycle whose steady state
# is (1/3, 1/3, 1/3) -- a unique solution of the linear system -- and whose
# powers never converge to anything, returning to the identity every third step
# for ever. One matrix, and the difference between a linear system and a limit
# is no longer an assertion.
# ---------------------------------------------------------------------------

CHAIN_PRESETS = {
    "weather": {
        "label": "Two states, both reachable from both",
        "P": "1/2 1/2; 1/4 3/4",
        "names": "fine, wet",
        "start": "1 0",
    },
    "market": {
        "label": "Three brands, with switching in every direction",
        "P": "7/10 2/10 1/10; 3/10 5/10 2/10; 1/10 3/10 6/10",
        "names": "A, B, C",
        "start": "1 0 0",
    },
    "cycle": {
        "label": "A 3-cycle: the system has an answer and the powers never settle",
        "P": "0 1 0; 0 0 1; 1 0 0",
        "names": "1, 2, 3",
        "start": "1 0 0",
    },
    "leaky": {
        "label": "One state that can leave and never return",
        "P": "1/2 1/4 1/4; 0 3/4 1/4; 0 1/2 1/2",
        "names": "trial, kept, lapsed",
        "start": "1 0 0",
    },
    "split": {
        "label": "Two closed groups: no unique steady state at all",
        "P": "1/2 1/2 0 0; 1/2 1/2 0 0; 0 0 1/3 2/3; 0 0 1/4 3/4",
        "names": "a, b, c, d",
        "start": "1 0 0 0",
    },
    "five": {
        "label": "Five states with denominator 20, where the powers outgrow a double",
        "P": ("4/20 4/20 4/20 4/20 4/20; 1/20 3/20 7/20 4/20 5/20; "
              "2/20 2/20 6/20 7/20 3/20; 9/20 1/20 1/20 4/20 5/20; 3/20 4/20 6/20 2/20 5/20"),
        "names": "1, 2, 3, 4, 5",
        "start": "1 0 0 0 0",
    },
}

ABSORB_PRESETS = {
    "ruin": {
        "label": "A gambler with 4 units, even stakes, ruined at 0 and finished at 4",
        "P": "1 0 0 0 0; 1/2 0 1/2 0 0; 0 1/2 0 1/2 0; 0 0 1/2 0 1/2; 0 0 0 0 1",
        "names": "0, 1, 2, 3, 4",
        "absorbing": "1 5",
    },
    "drunk": {
        "label": "A biased walk: twice as likely to step up as down",
        "P": "1 0 0 0 0; 1/3 0 2/3 0 0; 0 1/3 0 2/3 0; 0 0 1/3 0 2/3; 0 0 0 0 1",
        "names": "0, 1, 2, 3, 4",
        "absorbing": "1 5",
    },
    "trial": {
        "label": "A trial with two ways out and two states you can go back to",
        "P": "1/2 1/4 1/8 1/8; 1/4 1/2 1/8 1/8; 0 0 1 0; 0 0 0 1",
        "names": "new, review, accepted, rejected",
        "absorbing": "3 4",
    },
}

# `_mdp` heads its two action columns "action 1" and "action 2" deliberately -- the c9 lesson
# prose says so, and tells the reader that which real-world choice each stands for lives in the
# matrices and rewards they typed. So there is no per-preset action NAME here: a key holding
# one would be read by nothing, and the label already says what the two actions are.
MDP_PRESETS = {
    "machine": {
        "label": "Run it or service it: two states, two actions",
        "P0": "1/2 1/2; 1/4 3/4",
        "P1": "3/4 1/4; 1/2 1/2",
        "r0": "1 3",
        "r1": "2 1",
        "names": "good, worn",
    },
    "stock": {
        "label": "Hold or restock, with a penalty for being empty",
        "P0": "3/5 2/5 0; 0 1/2 1/2; 0 0 1",
        "P1": "1 0 0; 4/5 1/5 0; 3/5 2/5 0",
        "r0": "4 1 -3",
        "r1": "1 0 -1",
        "names": "full, low, empty",
    },
}


# ---------------------------------------------------------------------------
# Control furniture, the same shapes every kit on the path uses.
# ---------------------------------------------------------------------------


def _payload(name, values):
    return "  var %s = %s;\n" % (name, json.dumps(values).replace("</", "<\\/"))


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
        '<option value="%s"%s>%s</option>' % (v, " selected" if str(v) == str(chosen) else "", t)
        for v, t in options
    )
    return (
        '        <div class="field">\n          <label for="%s">%s</label>\n'
        '          <select id="%s">%s</select>\n        </div>\n' % (cid, label, cid, opts)
    )


def _text(cid, label, value):
    return (
        '        <div class="field">\n          <label for="%s">%s</label>\n'
        '          <input id="%s" type="text" value="%s" inputmode="text" autocomplete="off">\n'
        "        </div>\n" % (cid, label, cid, value)
    )


def _kpis(items):
    cells = "".join(
        '          <div class="kpi"><span>%s</span><strong id="%s">&mdash;</strong></div>\n' % (label, cid)
        for label, cid in items
    )
    return '        <div class="kpi-grid">\n%s        </div>\n' % cells


def _hint(cid, text):
    return '        <p class="small-copy" id="%s" style="margin:0;">%s</p>\n' % (cid, text)


def _toolbar(name, subtitle, legend):
    swatches = "".join(
        '<span class="tone-%s"><i class="legend-swatch"></i>%s</span>' % (tone, text) for tone, text in legend
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


def _table(cid):
    return '      <div class="table-wrap" style="margin-top:12px;"><table class="tt" id="%s"></table></div>\n' % cid


def _panel(cid):
    return '      <div id="%s" style="margin-top:12px;"></div>\n' % cid


def _banner(cid):
    return '      <div class="status-banner" id="%s" style="margin-top:12px;"></div>\n' % cid


def _lab(cfg, *, title, subtitle, markup, controls, script, panel_title, panel_intro):
    return Lab(
        title=title,
        subtitle=subtitle,
        markup=markup,
        controls=controls,
        script=script,
        panel_title=cfg.get("panel_title", panel_title),
        panel_intro=cfg.get("panel_intro", panel_intro),
    )


def _preset(cfg, presets, mode, default):
    chosen = cfg.get("preset", default)
    if chosen not in presets:
        raise ValueError(
            "markov_lab: mode %r has no preset %r; the presets are %s"
            % (mode, chosen, ", ".join(sorted(presets)))
        )
    return chosen, presets[chosen]


_READ_JS = r"""
  function nameList(text, count) {
    var parts = String(text || '').split(',').map(function (s) { return s.trim(); })
      .filter(function (s) { return s.length; });
    if (parts.length !== count) { parts = []; for (var k = 0; k < count; k += 1) parts.push(String(k + 1)); }
    return parts;
  }
  function setKpi(id, html) { document.getElementById(id).innerHTML = html; }
"""


# ---------------------------------------------------------------------------
# Mode `chain` -- the matrix as an object, and one step at a time
# ---------------------------------------------------------------------------


def _chain(cfg):
    chosen, here = _preset(cfg, CHAIN_PRESETS, "chain", "weather")

    markup = (
        _toolbar(
            "A row is a distribution, and that is the whole definition",
            "every row sums to 1, and P&#8319; is n of those steps taken at once",
            [
                ("cyan", "a state"),
                ("muted", "a transition with positive probability"),
                ("purple", "the distribution after n steps"),
                ("green", "row sums, checked"),
            ],
        )
        + _stage(_svg("mcGraph", "0 0 660 300",
                      "The support digraph of the chain: one node per state and an arc wherever the "
                      "transition probability is positive."))
        + _stage(_svg("mcDist", "0 0 660 190",
                      "The starting distribution pushed forward one step at a time, as bars."))
        + _table("mcRows")
        + _panel("mcPow")
        + _banner("mcStatus")
    )
    controls = (
        _select("mcPreset", "Worked example",
                [(k, CHAIN_PRESETS[k]["label"]) for k in
                 ("weather", "market", "cycle", "leaky", "five")], chosen)
        + _text("mcP", "Transition matrix &mdash; rows separated by &ldquo;;&rdquo;", here["P"])
        + _text("mcNames", "State names", here["names"])
        + _text("mcStart", "Starting distribution", here["start"])
        + _range("mcN", "Steps n", 1, 24, 6, 1)
        + _kpis(
            [
                ("States", "mcStatesK"),
                ("Rows sum to 1", "mcSumK"),
                ("Arcs", "mcArcsK"),
                ("Widest entry of P&#8319;", "mcWideK"),
                ("Distribution after n", "mcAfterK"),
                ("Largest denominator", "mcDenK"),
            ]
        )
        + _hint(
            "mcHint",
            "Push n up on the five-state example and watch the denominators of P&#8319; grow. At "
            "n = 12 the entries are fifteen digits over sixteen &mdash; past what a double can hold, "
            "which is why the powers here are computed in exact fractions and not in decimals. The "
            "distribution bars settle long before the fractions stop growing.",
        )
    )

    script = _CORE_JS + _READ_JS + _payload("PRESETS", CHAIN_PRESETS) + r"""
  var presetS = document.getElementById('mcPreset');
  var pIn = document.getElementById('mcP');
  var namesIn = document.getElementById('mcNames');
  var startIn = document.getElementById('mcStart');
  var nS = document.getElementById('mcN');
  var graphEl = document.getElementById('mcGraph');
  var distEl = document.getElementById('mcDist');
  var rowsEl = document.getElementById('mcRows');
  var powEl = document.getElementById('mcPow');
  var statusEl = document.getElementById('mcStatus');

  function blank(message) {
    graphEl.innerHTML = ''; distEl.innerHTML = ''; rowsEl.innerHTML = ''; powEl.innerHTML = '';
    ['mcStatesK', 'mcSumK', 'mcArcsK', 'mcWideK', 'mcAfterK', 'mcDenK'].forEach(function (id) {
      setKpi(id, '&mdash;');
    });
    statusEl.innerHTML = message;
  }

  function redraw() {
    var parsed = Mparse(pIn.value, 'the transition matrix');
    if (parsed.bad) { blank('<strong>' + parsed.bad + '.</strong>'); return; }
    var P = parsed.M, valid = chainValid(P);
    if (!valid.ok) {
      blank('<strong>That is not a transition matrix.</strong> ' + valid.why.charAt(0).toUpperCase()
        + valid.why.slice(1) + '. Nothing below is computed on a matrix that fails this test, because '
        + 'every quantity on this page would still produce a number and none of them would mean '
        + 'anything.');
      return;
    }
    var n = P.length, names = nameList(namesIn.value, n);
    var start = readDist(startIn.value, n);
    if (start === null) {
      blank('The starting distribution needs ' + n + ' non-negative numbers summing to exactly 1 '
        + '&mdash; they are not rescaled for you, because a distribution that does not sum to one is a '
        + 'typo and rescaling it answers a different question.');
      return;
    }
    var steps = Math.max(1, Math.min(24, +nS.value || 1));
    document.getElementById('mcNOut').textContent = String(steps);

    var arcs = 0, i, j;
    for (i = 0; i < n; i += 1) for (j = 0; j < n; j += 1) if (!Rzero(P[i][j])) arcs += 1;
    graphEl.innerHTML = chainSvg(P, { w: 660, h: 300, names: names });

    var walk = distWalk(start, P, Math.min(steps, 16));
    distEl.innerHTML = distSvg(walk, { w: 660, h: 190 });

    var rowsHtml = [];
    for (i = 0; i < n; i += 1) {
      var cells = [rowhead(names[i])];
      for (j = 0; j < n; j += 1) cells.push(td(Rtext(P[i][j]), Rzero(P[i][j]) ? 'tone-muted' : ''));
      cells.push(td('<span class="tone-green">' + Rtext(valid.sums[i]) + ' &check;</span>'));
      rowsHtml.push(tr(cells));
    }
    var heads = [th('from &rarr; to')];
    for (j = 0; j < n; j += 1) heads.push(th(names[j]));
    heads.push(th('row sum'));
    rowsEl.innerHTML = '<caption>The matrix as read, with every row added up here rather than assumed'
      + '</caption><thead>' + tr(heads) + '</thead><tbody>' + rowsHtml.join('') + '</tbody>';

    var Pn = chainPow(P, steps);
    var widest = 0, den = 1n;
    for (i = 0; i < n; i += 1) for (j = 0; j < n; j += 1) {
      var w = String(Pn[i][j].n < 0n ? -Pn[i][j].n : Pn[i][j].n).length;
      if (w > widest) widest = w;
      if (Pn[i][j].d > den) den = Pn[i][j].d;
    }
    powEl.innerHTML = Mtable('P raised to the power ' + steps + ', exactly', Pn,
      { heads: names, rowlabels: names });

    var after = walk[walk.length - 1];
    setKpi('mcStatesK', String(n));
    setKpi('mcSumK', '<span class="tone-green">all ' + n + ' &check;</span>');
    setKpi('mcArcsK', arcs + ' of ' + (n * n) + ' possible');
    setKpi('mcWideK', widest + ' digit' + (widest === 1 ? '' : 's'));
    setKpi('mcAfterK', after.map(function (v) { return Rshort(v, 4, 6); }).join(', '));
    setKpi('mcDenK', String(den).length + ' digits');

    statusEl.innerHTML = '<strong>' + valid.why.charAt(0).toUpperCase() + valid.why.slice(1)
      + '.</strong> The support digraph above has ' + arcs + ' arc' + (arcs === 1 ? '' : 's')
      + ' out of a possible ' + (n * n) + ', and an arc is drawn exactly where the probability is '
      + 'positive &mdash; the graph is a statement about which entries are nonzero, not about how large '
      + 'they are. P<sup>' + steps + '</sup> is computed by repeated multiplication in exact fractions: '
      + 'its widest numerator has ' + widest + ' digit' + (widest === 1 ? '' : 's')
      + ' and its largest denominator has ' + String(den).length + ' digit'
      + (String(den).length === 1 ? '' : 's') + '. '
      + (String(den).length > 15
          ? '<span class="tone-amber">That denominator is past what a double can hold</span>, so a '
            + 'decimal implementation would be returning the nearest number it could store and calling '
            + 'it the answer. '
          : '')
      + 'Starting from (' + start.map(Rtext).join(', ') + '), after ' + steps + ' step'
      + (steps === 1 ? '' : 's') + ' the distribution is (' + after.map(function (v) {
          return Rshort(v, 5, 7); }).join(', ') + '). ' + convergenceNote();
  }

  presetS.addEventListener('change', function () {
    var p = PRESETS[presetS.value];
    if (!p) return;
    pIn.value = p.P; namesIn.value = p.names; startIn.value = p.start;
    redraw();
  });
  [pIn, namesIn, startIn, nS].forEach(function (el) { el.addEventListener('input', redraw); });
  redraw();
  window.redrawLab = redraw;
"""
    return _lab(
        cfg,
        title="A matrix whose rows are distributions",
        subtitle="the support digraph, n steps at once, and denominators that outgrow a decimal",
        markup=markup,
        controls=controls,
        script=script,
        panel_title="Type a matrix, name the states, push a distribution forward",
        panel_intro="Every row is added up on this page before anything is computed from it: a matrix "
        "whose rows do not sum to one is refused rather than used. P&#8319; is exact repeated "
        "multiplication, which is why its entries can be wider than a decimal.",
    )


# ---------------------------------------------------------------------------
# Mode `classify` -- classes, recurrence, and the period
# ---------------------------------------------------------------------------


def _classify(cfg):
    chosen, here = _preset(cfg, CHAIN_PRESETS, "classify", "leaky")

    markup = (
        _toolbar(
            "Which states can reach which, and can they get back",
            "a class is recurrent when no arc leaves it &mdash; a statement about arcs, not about sizes",
            [
                ("green", "a recurrent class"),
                ("red", "a transient class"),
                ("amber", "an arc that leaves a class"),
                ("muted", "an arc inside one"),
            ],
        )
        + _stage(_svg("mkGraph", "0 0 660 300",
                      "The support digraph with each state coloured by its communicating class and the "
                      "arcs that leave a class picked out."))
        + _table("mkClasses")
        + _table("mkReach")
        + _banner("mkStatus")
    )
    controls = (
        _select("mkPreset", "Worked example",
                [(k, CHAIN_PRESETS[k]["label"]) for k in
                 ("leaky", "cycle", "split", "weather", "market")], chosen)
        + _text("mkP", "Transition matrix", here["P"])
        + _text("mkNames", "State names", here["names"])
        + _kpis(
            [
                ("Classes", "mkCountK"),
                ("Irreducible", "mkIrredK"),
                ("Recurrent classes", "mkRecK"),
                ("Transient states", "mkTransK"),
                ("Period", "mkPeriodK"),
                ("Aperiodic", "mkAperK"),
            ]
        )
        + _hint(
            "mkHint",
            "Irreducible and aperiodic are the two hypotheses the convergence theorem needs, and "
            "both are computed here rather than assumed. Try the 3-cycle: it is irreducible, so the "
            "steady state is unique, and its period is 3, so the powers never settle. One hypothesis "
            "without the other is not enough, and this is the matrix that shows why.",
        )
    )

    script = _CORE_JS + _READ_JS + _payload("PRESETS", CHAIN_PRESETS) + r"""
  var presetS = document.getElementById('mkPreset');
  var pIn = document.getElementById('mkP');
  var namesIn = document.getElementById('mkNames');
  var graphEl = document.getElementById('mkGraph');
  var classesEl = document.getElementById('mkClasses');
  var reachEl = document.getElementById('mkReach');
  var statusEl = document.getElementById('mkStatus');

  function blank(message) {
    graphEl.innerHTML = ''; classesEl.innerHTML = ''; reachEl.innerHTML = '';
    ['mkCountK', 'mkIrredK', 'mkRecK', 'mkTransK', 'mkPeriodK', 'mkAperK'].forEach(function (id) {
      setKpi(id, '&mdash;');
    });
    statusEl.innerHTML = message;
  }

  function redraw() {
    var parsed = Mparse(pIn.value, 'the transition matrix');
    if (parsed.bad) { blank('<strong>' + parsed.bad + '.</strong>'); return; }
    var P = parsed.M, valid = chainValid(P);
    if (!valid.ok) {
      blank('<strong>That is not a transition matrix.</strong> ' + valid.why.charAt(0).toUpperCase()
        + valid.why.slice(1) + '. Reachability would still compute on it, and it would be reachability '
        + 'in a graph that is not a chain.');
      return;
    }
    var n = P.length, names = nameList(namesIn.value, n);
    var cls = chainClasses(P);
    var of = [], i, j, k;
    for (i = 0; i < n; i += 1) of.push(-1);
    for (k = 0; k < cls.classes.length; k += 1) {
      for (i = 0; i < cls.classes[k].states.length; i += 1) of[cls.classes[k].states[i]] = k;
    }
    var leaving = {};
    for (k = 0; k < cls.classes.length; k += 1) {
      for (i = 0; i < cls.classes[k].leaves.length; i += 1) {
        leaving[cls.classes[k].leaves[i][0] + ',' + cls.classes[k].leaves[i][1]] = true;
      }
    }
    graphEl.innerHTML = chainSvg(P, {
      w: 660, h: 300, names: names,
      nodeTone: function (s) { return cls.classes[of[s]].recurrent ? 'green' : 'red'; },
      arcTone: function (a, b) { return leaving[a + ',' + b] ? 'amber' : 'muted'; }
    });

    var rows = [], transient = 0, recurrent = 0, periods = [];
    for (k = 0; k < cls.classes.length; k += 1) {
      var c = cls.classes[k];
      var per = chainPeriod(P, c.states);
      periods.push(per.period);
      if (c.recurrent) recurrent += 1; else transient += c.states.length;
      rows.push(tr([
        rowhead('{' + c.states.map(function (s) { return names[s]; }).join(', ') + '}'),
        td(c.recurrent ? '<span class="tone-green">recurrent</span>'
           : '<span class="tone-red">transient</span>'),
        td(String(per.period) + (per.aperiodic ? ' <span class="tone-green">aperiodic</span>' : '')),
        tdl(c.why)]));
    }
    classesEl.innerHTML = '<caption>The communicating classes, and why each is recurrent or '
      + 'transient</caption><thead>' + tr([th('class'), th('kind'), th('period'), th('reason')])
      + '</thead><tbody>' + rows.join('') + '</tbody>';

    var rr = [], heads = [th('from &rarr; can reach')];
    for (j = 0; j < n; j += 1) heads.push(th(names[j]));
    for (i = 0; i < n; i += 1) {
      var cells = [rowhead(names[i])];
      for (j = 0; j < n; j += 1) {
        var both = cls.reach[i][j] && cls.reach[j][i];
        cells.push(td(cls.reach[i][j] ? (both ? '&harr;' : '&rarr;') : '&middot;',
          both ? 'tone-green' : (cls.reach[i][j] ? 'tone-amber' : 'tone-muted')));
      }
      rr.push(tr(cells));
    }
    reachEl.innerHTML = '<caption>Reachability, closed under composition: &harr; means the two states '
      + 'communicate and therefore share a class</caption><thead>' + tr(heads) + '</thead><tbody>'
      + rr.join('') + '</tbody>';

    var wholePeriod = cls.irreducible ? periods[0] : null;
    setKpi('mkCountK', String(cls.classes.length));
    setKpi('mkIrredK', cls.irreducible ? '<span class="tone-green">yes</span>'
      : '<span class="tone-red">no, ' + cls.classes.length + ' classes</span>');
    setKpi('mkRecK', String(recurrent));
    setKpi('mkTransK', String(transient));
    setKpi('mkPeriodK', wholePeriod === null ? 'per class: ' + periods.join(', ') : String(wholePeriod));
    setKpi('mkAperK', wholePeriod === null ? '&mdash;'
      : (wholePeriod === 1 ? '<span class="tone-green">yes</span>'
         : '<span class="tone-red">no, period ' + wholePeriod + '</span>'));

    statusEl.innerHTML = '<strong>' + cls.classes.length + ' communicating class'
      + (cls.classes.length === 1 ? '' : 'es') + ', of which ' + recurrent + ' '
      + (recurrent === 1 ? 'is' : 'are') + ' recurrent.</strong> '
      + 'A class is recurrent when <em>nothing leaves it</em>. That is a statement about which arcs '
      + 'exist and not about how large the probabilities are: an arc of probability 1/1000 out of a '
      + 'class makes it transient just as surely as one of probability 1/2, because the chain takes it '
      + 'eventually and then cannot come back. '
      + (cls.irreducible
          ? 'This chain is <span class="tone-green">irreducible</span> &mdash; one class, everything '
            + 'reaches everything &mdash; with period ' + wholePeriod + '. '
            + (wholePeriod === 1
                ? 'It is also <span class="tone-green">aperiodic</span>, so it satisfies both '
                  + 'hypotheses of the convergence theorem.'
                : '<span class="tone-red">It is periodic</span>, so the second hypothesis fails: the '
                  + 'steady state still exists and is still unique, because it solves a linear system, '
                  + 'but P&#8319; does not approach it. Mode <em>steady</em> shows both on this matrix.')
          : 'This chain is <span class="tone-red">reducible</span>: it has ' + cls.classes.length
            + ' classes, so the convergence theorem does not apply. '
            + (recurrent === 1
                ? 'Exactly one of them is recurrent, so the balance equations still have a unique '
                  + 'solution &mdash; it puts probability 0 on every transient state, which is where '
                  + 'the chain spends finitely much of its time.'
                : recurrent + ' of them are recurrent, so the balance equations have a WHOLE FAMILY of '
                  + 'solutions: each closed group has its own steady state and every mixture of them is '
                  + 'stationary too. Mode <em>steady</em> on this matrix refuses to print one.'))
      + ' The period is computed as the gcd of the lengths of the cycles through a state, obtained by '
      + 'levelling the class by breadth-first search and taking the gcd of level(u) + 1 &minus; level(v) '
      + 'over its arcs &mdash; the same number without enumerating a single cycle.';
  }

  presetS.addEventListener('change', function () {
    var p = PRESETS[presetS.value];
    if (!p) return;
    pIn.value = p.P; namesIn.value = p.names;
    redraw();
  });
  [pIn, namesIn].forEach(function (el) { el.addEventListener('input', redraw); });
  redraw();
  window.redrawLab = redraw;
"""
    return _lab(
        cfg,
        title="Which states does the chain keep coming back to",
        subtitle="communicating classes, recurrence, and the period — the hypotheses, computed",
        markup=markup,
        controls=controls,
        script=script,
        panel_title="Type a matrix and read its structure off the arcs",
        panel_intro="Classes come from reachability on the support digraph, recurrence from whether any "
        "arc leaves a class, and the period from a gcd of cycle lengths. These are the two hypotheses "
        "the convergence theorem needs, and this page checks them.",
    )


# ---------------------------------------------------------------------------
# Mode `steady` -- the linear system, and the limit that is not the method
# ---------------------------------------------------------------------------


def _steady(cfg):
    chosen, here = _preset(cfg, CHAIN_PRESETS, "steady", "market")

    markup = (
        _toolbar(
            "&pi;P = &pi; is n equations, one of them redundant",
            "drop one by name, put &sum;&pi; = 1 in its place, and solve &mdash; exactly, once",
            [
                ("green", "the exact solution of the linear system"),
                ("purple", "a power iteration, in floating point"),
                ("amber", "the equation that was dropped"),
                ("red", "where the iteration is still wrong"),
            ],
        )
        + _panel("msSystem")
        + _stage(_svg("msConv", "0 0 660 190",
                      "The starting distribution pushed forward step by step, with the exact steady "
                      "state drawn as a dashed line for each state."))
        + _table("msCompare")
        + _banner("msStatus")
    )
    controls = (
        _select("msPreset", "Worked example",
                [(k, CHAIN_PRESETS[k]["label"]) for k in
                 ("market", "weather", "cycle", "split", "five")], chosen)
        + _text("msP", "Transition matrix", here["P"])
        + _text("msNames", "State names", here["names"])
        + _select("msDrop", "Balance equation to drop", [("auto", "the last one")], "auto")
        + _range("msIter", "Power-iteration steps", 1, 400, 60, 1)
        + _kpis(
            [
                ("&pi;, exactly", "msPiK"),
                ("Unique", "msUniqueK"),
                ("&pi;P &minus; &pi;", "msResidK"),
                ("&sum;&pi;", "msSumK"),
                ("Iteration gap", "msGapK"),
                ("Places agreed", "msPlacesK"),
            ]
        )
        + _hint(
            "msHint",
            "Change which equation is dropped and the answer does not move, because the equations "
            "are dependent: the columns of P &minus; I sum to zero, so any one of them is implied by "
            "the others. Then switch to the 3-cycle. The linear system still has exactly one "
            "solution and the iteration still has none, for ever &mdash; which is the difference "
            "between solving and waiting.",
        )
    )

    script = _CORE_JS + _READ_JS + _payload("PRESETS", CHAIN_PRESETS) + r"""
  var presetS = document.getElementById('msPreset');
  var pIn = document.getElementById('msP');
  var namesIn = document.getElementById('msNames');
  var dropS = document.getElementById('msDrop');
  var iterS = document.getElementById('msIter');
  var sysEl = document.getElementById('msSystem');
  var convEl = document.getElementById('msConv');
  var cmpEl = document.getElementById('msCompare');
  var statusEl = document.getElementById('msStatus');

  function blank(message) {
    sysEl.innerHTML = ''; convEl.innerHTML = ''; cmpEl.innerHTML = '';
    ['msPiK', 'msUniqueK', 'msResidK', 'msSumK', 'msGapK', 'msPlacesK'].forEach(function (id) {
      setKpi(id, '&mdash;');
    });
    statusEl.innerHTML = message;
  }
  function fillDrop(n, names) {
    var keep = dropS.value;
    var html = '<option value="auto">the last one</option>';
    for (var i = 0; i < n; i += 1) {
      html += '<option value="' + i + '">equation ' + (i + 1) + ' (state ' + names[i] + ')</option>';
    }
    if (dropS.innerHTML !== html) {
      dropS.innerHTML = html;
      dropS.value = (keep === 'auto' || Number(keep) < n) ? keep : 'auto';
    }
  }

  function redraw() {
    var parsed = Mparse(pIn.value, 'the transition matrix');
    if (parsed.bad) { blank('<strong>' + parsed.bad + '.</strong>'); return; }
    var P = parsed.M, valid = chainValid(P);
    if (!valid.ok) {
      blank('<strong>That is not a transition matrix.</strong> ' + valid.why.charAt(0).toUpperCase()
        + valid.why.slice(1) + '. The balance equations of a matrix whose rows do not sum to one have '
        + 'a solution too, and it is not a steady state of anything.');
      return;
    }
    var n = P.length, names = nameList(namesIn.value, n);
    fillDrop(n, names);
    var drop = dropS.value === 'auto' ? n - 1 : Math.max(0, Math.min(n - 1, Number(dropS.value)));
    var ss = steadyState(P, drop);
    var steps = Math.max(1, Math.min(400, +iterS.value || 1));
    document.getElementById('msIterOut').textContent = String(steps);

    /* The system as it was actually handed to the solver: n - 1 balance rows
       and the normalisation, with the augmented column separated. */
    sysEl.innerHTML = Mtable('The linear system solved &mdash; rows 1 to ' + (n - 1)
      + ' are balance equations with equation ' + (drop + 1) + ' dropped, and the last row is sum pi = 1',
      ss.system, { split: n });

    if (!ss.unique) {
      convEl.innerHTML = '';
      cmpEl.innerHTML = '';
      setKpi('msPiK', '<span class="tone-red">not unique</span>');
      setKpi('msUniqueK', '<span class="tone-red">no</span>');
      setKpi('msResidK', '&mdash;'); setKpi('msSumK', '&mdash;');
      setKpi('msGapK', '&mdash;'); setKpi('msPlacesK', '&mdash;');
      statusEl.innerHTML = '<strong>This system has no unique solution, and the page says so rather '
        + 'than printing one of the infinitely many.</strong> The reduced matrix has rank ' + ss.rank
        + ' against ' + n + ' unknowns. That happens exactly when the chain is reducible with more than '
        + 'one recurrent class: each closed group has its own steady state and every mixture of them is '
        + 'also stationary, so &ldquo;the&rdquo; steady state does not exist. Mode <em>classify</em> on '
        + 'the same matrix finds the classes. ' + convergenceNote();
      return;
    }

    var pi = ss.pi, chk = steadyCheck(P, pi);
    /* The iteration, from a corner rather than from pi, so it has somewhere to
       travel. Floating point on purpose: this is the column that cannot be
       exact, and the comparison is the lesson. */
    var startF = [], i, j;
    for (i = 0; i < n; i += 1) startF.push(i === 0 ? 1 : 0);
    var fw = floatWalk(floatMatrix(P), startF, steps);
    var gap = floatGap(pi, fw.v);
    var cyc = powerCycles(P, 3 * n + 3);

    var startR = [];
    for (i = 0; i < n; i += 1) startR.push(i === 0 ? R1 : R0);
    convEl.innerHTML = distSvg(distWalk(startR, P, Math.min(steps, 16)), { w: 660, h: 190, target: pi });

    var rows = [];
    for (i = 0; i < n; i += 1) {
      var fv = fw.v[i], ev = toFloat(pi[i]);
      rows.push(tr([rowhead(names[i]),
        td('<strong>' + Rtext(pi[i]) + '</strong>', 'tone-green'),
        td(Rfixed(pi[i], 12)),
        td(fv.toFixed(12), 'tone-purple'),
        td(Math.abs(fv - ev) === 0 ? '0' : Math.abs(fv - ev).toExponential(2),
           Math.abs(fv - ev) > 1e-9 ? 'tone-red' : 'tone-muted'),
        td(Rtext(chk.moved[i]) + (Requ(chk.moved[i], pi[i]) ? ' <span class="tone-green">&check;</span>'
           : ' <span class="tone-red">&ne; pi</span>'))]));
    }
    cmpEl.innerHTML = '<caption>The solve, the iteration, and the check that piP really is pi</caption>'
      + '<thead>' + tr([th('state'), th('&pi; exactly'), th('&pi; as a decimal'),
        th('after ' + steps + ' steps'), th('difference'), th('(&pi;P)&#7522;')])
      + '</thead><tbody>' + rows.join('') + '</tbody>';

    setKpi('msPiK', pi.map(function (v) { return Rshort(v, 5, 7); }).join(', '));
    setKpi('msUniqueK', '<span class="tone-green">yes, rank ' + ss.rank + '</span>');
    setKpi('msResidK', chk.ok ? '<span class="tone-green">exactly 0</span>'
      : '<span class="tone-red">' + Rtext(chk.residual) + '</span>');
    setKpi('msSumK', Rtext(chk.sum) + (Requ(chk.sum, R1) ? ' <span class="tone-green">&check;</span>' : ''));
    setKpi('msGapK', gap.gap === 0 ? '0 at double precision' : gap.gap.toExponential(3));
    setKpi('msPlacesK', gap.gap === 0 ? 'all of them' : String(gap.places));

    statusEl.innerHTML = '<strong>' + ss.why.charAt(0).toUpperCase() + ss.why.slice(1) + '.</strong> '
      + 'The solution is &pi; = (' + pi.map(Rtext).join(', ') + '), exactly, from one Gauss-Jordan '
      + 'elimination over rationals in ' + ss.ops.length + ' operation'
      + (ss.ops.length === 1 ? '' : 's') + '. '
      + '<strong>' + chk.why.charAt(0).toUpperCase() + chk.why.slice(1) + '.</strong> '
      + (cyc.repeats
          ? '<span class="tone-red">Now look at the iteration.</span> ' + cyc.why.charAt(0).toUpperCase()
            + cyc.why.slice(1) + '. So there is nothing for the iteration to converge to, at any number '
            + 'of steps, and the exact answer above is not a limit of it: it is the solution of '
            + 'n equations in n unknowns, which exists and is unique whether or not any limit does. '
            + '<strong>That is what &ldquo;a steady state is a linear system, not a limit&rdquo; '
            + 'means</strong>, and this matrix is where the two come apart.'
          : 'After ' + steps + ' steps the floating-point iteration is out by '
            + (gap.gap === 0 ? 'nothing a double can represent'
               : gap.gap.toExponential(3) + ' in state ' + names[gap.at])
            + ', which is agreement to about ' + (gap.gap === 0 ? 16 : gap.places)
            + ' decimal places. Push the slider up and the agreement stops improving: the iteration has '
            + 'run out of double, not out of steps. The exact column did not iterate at all.')
      + ' ' + convergenceNote();
  }

  presetS.addEventListener('change', function () {
    var p = PRESETS[presetS.value];
    if (!p) return;
    pIn.value = p.P; namesIn.value = p.names; dropS.value = 'auto';
    redraw();
  });
  dropS.addEventListener('change', redraw);
  [pIn, namesIn, iterS].forEach(function (el) { el.addEventListener('input', redraw); });
  redraw();
  window.redrawLab = redraw;
"""
    return _lab(
        cfg,
        title="The steady state is solved for, not waited for",
        subtitle="n dependent equations, one replaced by Σπ = 1, and an iteration that cannot match it",
        markup=markup,
        controls=controls,
        script=script,
        panel_title="Choose which equation to drop, and how long to iterate",
        panel_intro="The system is built and reduced here in exact fractions. Beside it a floating-point "
        "power iteration runs for as many steps as you like, and the page prints how far short it is "
        "&mdash; on one preset, for ever.",
    )


# ---------------------------------------------------------------------------
# Mode `absorb` -- N as a sum of powers, and where the chain ends up
# ---------------------------------------------------------------------------


def _absorb(cfg):
    chosen, here = _preset(cfg, ABSORB_PRESETS, "absorb", "ruin")

    markup = (
        _toolbar(
            "Once it stops, it stops",
            "N = (I &minus; Q)&#8315;&sup1; counts the visits, and it is the SUM of the powers of Q",
            [
                ("cyan", "a transient state"),
                ("green", "an absorbing state"),
                ("purple", "expected visits"),
                ("amber", "the partial sums closing on N"),
            ],
        )
        + _stage(_svg("maGraph", "0 0 660 300",
                      "The chain with absorbing states ringed, and the transitions between transient "
                      "states drawn."))
        + _panel("maN")
        + _table("maRows")
        + _table("maPartial")
        + _banner("maStatus")
    )
    controls = (
        _select("maPreset", "Worked example",
                [(k, ABSORB_PRESETS[k]["label"]) for k in ("ruin", "drunk", "trial")], chosen)
        + _text("maP", "Transition matrix", here["P"])
        + _text("maNames", "State names", here["names"])
        + _text("maAbs", "Absorbing states, by position", here["absorbing"])
        + _range("maK", "Powers of Q to add up", 0, 20, 6, 1)
        + _kpis(
            [
                ("Transient states", "maTransK"),
                ("Absorbing states", "maAbsK"),
                ("Longest expected wait", "maLongK"),
                ("From the middle", "maMidK"),
                ("Partial sum after k", "maPartK"),
                ("Still missing", "maMissK"),
            ]
        )
        + _hint(
            "maHint",
            "N is usually introduced as an inverse and then used as a count, which leaves the reader "
            "with a formula and no reason. Move the slider: the partial sums I + Q + &hellip; + Q&#7503; "
            "climb towards N entry by entry, and they do it because Q&#7503; is the probability of "
            "still being in each transient state after k steps. The inverse is what that sum adds up to.",
        )
    )

    script = _CORE_JS + _READ_JS + _payload("PRESETS", ABSORB_PRESETS) + r"""
  var presetS = document.getElementById('maPreset');
  var pIn = document.getElementById('maP');
  var namesIn = document.getElementById('maNames');
  var absIn = document.getElementById('maAbs');
  var kS = document.getElementById('maK');
  var graphEl = document.getElementById('maGraph');
  var nEl = document.getElementById('maN');
  var rowsEl = document.getElementById('maRows');
  var partEl = document.getElementById('maPartial');
  var statusEl = document.getElementById('maStatus');

  function blank(message) {
    graphEl.innerHTML = ''; nEl.innerHTML = ''; rowsEl.innerHTML = ''; partEl.innerHTML = '';
    ['maTransK', 'maAbsK', 'maLongK', 'maMidK', 'maPartK', 'maMissK'].forEach(function (id) {
      setKpi(id, '&mdash;');
    });
    statusEl.innerHTML = message;
  }

  function redraw() {
    var parsed = Mparse(pIn.value, 'the transition matrix');
    if (parsed.bad) { blank('<strong>' + parsed.bad + '.</strong>'); return; }
    var P = parsed.M, valid = chainValid(P);
    if (!valid.ok) {
      blank('<strong>That is not a transition matrix.</strong> ' + valid.why.charAt(0).toUpperCase()
        + valid.why.slice(1) + '.');
      return;
    }
    var n = P.length, names = nameList(namesIn.value, n), i, j;
    var picked = String(absIn.value).trim().split(/[\s,;]+/).filter(function (t) { return t.length; })
      .map(function (t) { return Number(t) - 1; });
    var bad = picked.filter(function (v) { return !(v >= 0 && v < n); });
    if (!picked.length || bad.length) {
      blank('Name the absorbing states by position, counting from 1 &mdash; for example '
        + '&ldquo;1 ' + n + '&rdquo;. There are ' + n + ' states here.');
      return;
    }
    var notAbs = picked.filter(function (s) { return !Requ(P[s][s], R1); });
    if (notAbs.length) {
      blank('State ' + names[notAbs[0]] + ' is listed as absorbing, but P['
        + (notAbs[0] + 1) + '][' + (notAbs[0] + 1) + '] = ' + Rtext(P[notAbs[0]][notAbs[0]])
        + ' rather than 1. An absorbing state is one the chain cannot leave, and that is a property of '
        + 'the matrix rather than a label put on it.');
      return;
    }
    var k = Math.max(0, Math.min(20, +kS.value || 0));
    document.getElementById('maKOut').textContent = String(k);
    var abs = absorbing(P, picked, k);
    if (abs.singular) {
      blank('<strong>I &minus; Q is singular here.</strong> That means some transient state cannot reach '
        + 'an absorbing one at all, so the chain never stops and there is no expected number of steps to '
        + 'absorption. Check the arcs: every state you have NOT listed as absorbing has to be able to '
        + 'reach one that you have.');
      return;
    }
    var isAbs = {};
    for (i = 0; i < picked.length; i += 1) isAbs[picked[i]] = true;
    graphEl.innerHTML = chainSvg(P, {
      w: 660, h: 300, names: names,
      nodeTone: function (s) { return isAbs[s] ? 'green' : 'cyan'; }
    });

    var tNames = abs.transient.map(function (s) { return names[s]; });
    var aNames = abs.absorbing.map(function (s) { return names[s]; });
    nEl.innerHTML = Mtable('N = (I &minus; Q)&#8315;&sup1; &mdash; the expected number of visits to each '
      + 'transient state, exactly', abs.N, { heads: tNames, rowlabels: tNames });

    var rows = [];
    for (i = 0; i < abs.transient.length; i += 1) {
      var cells = [rowhead(tNames[i]), td('<strong>' + Rtext(abs.t[i]) + '</strong>')];
      for (j = 0; j < abs.absorbing.length; j += 1) cells.push(td(Rtext(abs.B[i][j])));
      rows.push(tr(cells));
    }
    var heads = [th('starting from'), th('expected steps')];
    for (j = 0; j < aNames.length; j += 1) heads.push(th('ends at ' + aNames[j]));
    rowsEl.innerHTML = '<caption>t = N&middot;1 and B = N&middot;R: how long, and where it ends'
      + '</caption><thead>' + tr(heads) + '</thead><tbody>' + rows.join('') + '</tbody>';

    var pRows = [], acc = abs.partials[Math.min(k, abs.partials.length - 1)];
    for (i = 0; i < abs.transient.length; i += 1) {
      var cells2 = [rowhead(tNames[i])];
      for (j = 0; j < abs.transient.length; j += 1) {
        var miss = Rsub(abs.N[i][j], acc[i][j]);
        cells2.push(td(Rshort(acc[i][j], 5, 7) + (Rzero(miss) ? ' <span class="tone-green">&check;</span>'
          : ' <span class="tone-amber">&minus;' + Rshort(miss, 5, 6) + '</span>')));
      }
      pRows.push(tr(cells2));
    }
    partEl.innerHTML = '<caption>I + Q + &hellip; + Q<sup>' + k + '</sup>, with what is still missing from '
      + 'N beside each entry</caption><thead>'
      + tr([th('from &rarr; to')].concat(tNames.map(function (t) { return th(t); })))
      + '</thead><tbody>' + pRows.join('') + '</tbody>';

    var longest = R0, longAt = 0;
    for (i = 0; i < abs.t.length; i += 1) if (Rcmp(abs.t[i], longest) > 0) { longest = abs.t[i]; longAt = i; }
    var mid = Math.floor(abs.transient.length / 2);
    var worstMiss = R0;
    for (i = 0; i < abs.transient.length; i += 1) for (j = 0; j < abs.transient.length; j += 1) {
      var d = Rsub(abs.N[i][j], acc[i][j]);
      if (Rcmp(d, worstMiss) > 0) worstMiss = d;
    }
    setKpi('maTransK', abs.transient.length + ': ' + tNames.join(', '));
    setKpi('maAbsK', abs.absorbing.length + ': ' + aNames.join(', '));
    setKpi('maLongK', Rtext(longest) + ' from ' + tNames[longAt]);
    setKpi('maMidK', Rtext(abs.t[mid]) + ' from ' + tNames[mid]);
    setKpi('maPartK', 'k = ' + k);
    setKpi('maMissK', Rzero(worstMiss) ? '<span class="tone-green">nothing</span>'
      : Rshort(worstMiss, 6, 7) + ' at most');

    statusEl.innerHTML = '<strong>N is the sum of the powers of Q, and the slider is the proof rather '
      + 'than the illustration.</strong> Q&#7503;[i][j] is the probability of being in transient state j '
      + 'after exactly k steps having started at i, so adding those probabilities over all k counts the '
      + 'expected number of visits &mdash; which is what N means. The partial sum at k = ' + k
      + ' is short of N by at most ' + (Rzero(worstMiss) ? '0' : Rtext(worstMiss))
      + ', and that remainder is exactly the probability mass still sitting in transient states after '
      + k + ' step' + (k === 1 ? '' : 's') + '. '
      + 'The expected time to absorption is t = N&middot;1: from ' + tNames[longAt] + ' it is '
      + Rtext(longest) + ' step' + (Requ(longest, R1) ? '' : 's') + '. '
      + 'B = N&middot;R splits that by destination, and every row of B sums to 1 &mdash; '
      + (function () {
          var okRows = 0, r;
          for (r = 0; r < abs.B.length; r += 1) {
            var s = R0, c;
            for (c = 0; c < abs.B[r].length; c += 1) s = Radd(s, abs.B[r][c]);
            if (Requ(s, R1)) okRows += 1;
          }
          return okRows === abs.B.length
            ? '<span class="tone-green">checked here, all ' + okRows + ' of them</span>, which says the '
              + 'chain is absorbed with probability one'
            : '<span class="tone-red">and ' + (abs.B.length - okRows) + ' of them do not, which would '
              + 'mean the chain escapes absorption</span>';
        })() + '. Everything on this page is exact: (I &minus; Q)&#8315;&sup1; comes from Gauss-Jordan on '
      + '[I &minus; Q | I] over rationals, so the inverse of a matrix of halves and thirds is a matrix of '
      + 'halves and thirds and not a screen of decimals.';
  }

  presetS.addEventListener('change', function () {
    var p = PRESETS[presetS.value];
    if (!p) return;
    pIn.value = p.P; namesIn.value = p.names; absIn.value = p.absorbing;
    redraw();
  });
  [pIn, namesIn, absIn, kS].forEach(function (el) { el.addEventListener('input', redraw); });
  redraw();
  window.redrawLab = redraw;
"""
    return _lab(
        cfg,
        title="How long until it stops, and where it stops",
        subtitle="the fundamental matrix as a sum of powers rather than as an inverse to memorise",
        markup=markup,
        controls=controls,
        script=script,
        panel_title="Name the absorbing states and add up the powers of Q",
        panel_intro="The canonical blocks are extracted here from the matrix you typed. N is computed by "
        "exact elimination on [I &minus; Q | I], and the partial sums of the powers of Q are shown "
        "climbing towards it.",
    )


# ---------------------------------------------------------------------------
# Mode `mdp` -- policy iteration, with the evaluation step an exact solve
# ---------------------------------------------------------------------------


def _mdp(cfg):
    chosen, here = _preset(cfg, MDP_PRESETS, "mdp", "machine")

    markup = (
        _toolbar(
            "Evaluate exactly, improve greedily, repeat",
            "each round is one linear solve, and it stops for a reason better than &ldquo;nothing moved&rdquo;",
            [
                ("green", "the action the round chooses"),
                ("purple", "the action it rejects"),
                ("amber", "a state whose action changed this round"),
                ("cyan", "value iteration, converging to the same numbers"),
            ],
        )
        + _table("mdRounds")
        + _table("mdQ")
        + _table("mdIter")
        + _banner("mdStatus")
    )
    controls = (
        _select("mdPreset", "Worked example",
                [(k, MDP_PRESETS[k]["label"]) for k in ("machine", "stock")], chosen)
        + _text("mdP0", "Transition matrix under action 1", here["P0"])
        + _text("mdP1", "Transition matrix under action 2", here["P1"])
        + _text("mdR0", "Reward per state under action 1", here["r0"])
        + _text("mdR1", "Reward per state under action 2", here["r1"])
        + _text("mdNames", "State names", here["names"])
        + _range("mdGamma", "Discount &gamma;, in twentieths", 1, 19, 18, 1)
        + _range("mdSteps", "Value-iteration steps to show", 1, 40, 12, 1)
        + _kpis(
            [
                ("Rounds to stop", "mdRoundsK"),
                ("Best policy", "mdPolicyK"),
                ("Its value", "mdValueK"),
                ("Policies in total", "mdAllK"),
                ("Value iteration at step n", "mdVIK"),
                ("Still short by", "mdGapK"),
            ]
        )
        + _hint(
            "mdHint",
            "Policy iteration stops because there are finitely many policies and the value never "
            "decreases, so it cannot revisit one &mdash; a reason, not a tolerance. Value iteration "
            "below it stops when you stop looking. Raise the discount towards 1 and watch the second "
            "one slow down while the first takes the same two or three rounds.",
        )
    )

    script = _CORE_JS + _READ_JS + _payload("PRESETS", MDP_PRESETS) + r"""
  var presetS = document.getElementById('mdPreset');
  var p0In = document.getElementById('mdP0');
  var p1In = document.getElementById('mdP1');
  var r0In = document.getElementById('mdR0');
  var r1In = document.getElementById('mdR1');
  var namesIn = document.getElementById('mdNames');
  var gS = document.getElementById('mdGamma');
  var stepS = document.getElementById('mdSteps');
  var roundsEl = document.getElementById('mdRounds');
  var qEl = document.getElementById('mdQ');
  var iterEl = document.getElementById('mdIter');
  var statusEl = document.getElementById('mdStatus');

  function blank(message) {
    roundsEl.innerHTML = ''; qEl.innerHTML = ''; iterEl.innerHTML = '';
    ['mdRoundsK', 'mdPolicyK', 'mdValueK', 'mdAllK', 'mdVIK', 'mdGapK'].forEach(function (id) {
      setKpi(id, '&mdash;');
    });
    statusEl.innerHTML = message;
  }
  function readRow(text, n) {
    var parts = String(text).trim().split(/[\s,;]+/).filter(function (t) { return t.length; });
    if (parts.length !== n) return null;
    var out = [], k;
    for (k = 0; k < parts.length; k += 1) {
      var v = Rread(parts[k]);
      if (v === null) return null;
      out.push(v);
    }
    return out;
  }

  function redraw() {
    var a0 = Mparse(p0In.value, 'the matrix for action 1');
    if (a0.bad) { blank('<strong>' + a0.bad + '.</strong>'); return; }
    var a1 = Mparse(p1In.value, 'the matrix for action 2');
    if (a1.bad) { blank('<strong>' + a1.bad + '.</strong>'); return; }
    var v0 = chainValid(a0.M), v1 = chainValid(a1.M);
    if (!v0.ok || !v1.ok) {
      blank('<strong>Each action needs its own transition matrix.</strong> '
        + (!v0.ok ? 'Action 1: ' + v0.why : 'Action 2: ' + v1.why) + '.');
      return;
    }
    if (a0.M.length !== a1.M.length) {
      blank('The two actions have to act on the same states: one matrix is ' + a0.M.length
        + ' by ' + a0.M.length + ' and the other ' + a1.M.length + ' by ' + a1.M.length + '.');
      return;
    }
    var n = a0.M.length, names = nameList(namesIn.value, n);
    var r0 = readRow(r0In.value, n), r1 = readRow(r1In.value, n);
    if (r0 === null || r1 === null) {
      blank('Each action needs one reward per state, so ' + n + ' numbers in each reward box. They may '
        + 'be negative, and they may be fractions.');
      return;
    }
    var gNum = Math.max(1, Math.min(19, +gS.value || 18));
    var gamma = R(BigInt(gNum), 20n);
    document.getElementById('mdGammaOut').textContent = Rtext(gamma);
    var vSteps = Math.max(1, Math.min(40, +stepS.value || 1));
    document.getElementById('mdStepsOut').textContent = String(vSteps);

    var Ps = [a0.M, a1.M], rs = [r0, r1];
    var run = policyIterate(Ps, rs, gamma, { valueSteps: vSteps });
    var acts = ['action 1', 'action 2'];

    var rows = [], i, k;
    for (k = 0; k < run.rounds.length; k += 1) {
      var rd = run.rounds[k];
      var changed = rd.improve.filter(function (im) { return im.was !== im.now; }).length;
      rows.push(tr([rowhead('round ' + (k + 1)),
        td(rd.policy.map(function (a) { return acts[a]; }).join(' / ')),
        td(rd.v.map(function (v) { return Rshort(v, 4, 7); }).join(', ')),
        td(String(rd.ops.length)),
        td(changed === 0 ? '<span class="tone-green">nothing changed &mdash; stop</span>'
           : '<span class="tone-amber">' + changed + ' state' + (changed === 1 ? '' : 's')
             + ' improved</span>')]));
    }
    roundsEl.innerHTML = '<caption>Each round evaluates the current policy by an exact linear solve, then '
      + 'improves it</caption><thead>'
      + tr([th('round'), th('policy'), th('its value'), th('elimination steps'), th('what improved')])
      + '</thead><tbody>' + rows.join('') + '</tbody>';

    var last = run.rounds[run.rounds.length - 1];
    var qRows = [];
    for (i = 0; i < n; i += 1) {
      var im = last.improve[i];
      var cells = [rowhead(names[i])];
      for (k = 0; k < im.q.length; k += 1) {
        cells.push(td(Rshort(im.q[k].value, 4, 7),
          im.q[k].act === im.now ? 'tone-green' : 'tone-purple'));
      }
      cells.push(td('<strong>' + acts[im.now] + '</strong>'));
      qRows.push(tr(cells));
    }
    qEl.innerHTML = '<caption>The last round&rsquo;s comparison: r(s,a) + &gamma;&sum;P(s&rsquo;|s,a)v(s&rsquo;) '
      + 'for each action</caption><thead>'
      + tr([th('state')].concat(acts.map(function (a) { return th(a); })).concat([th('chosen')]))
      + '</thead><tbody>' + qRows.join('') + '</tbody>';

    var vi = run.valueIteration, iRows = [];
    if (vi) {
      var show = [0, 1, 2, 3, Math.floor(vSteps / 2), vSteps].filter(function (s, idx, arr) {
        return s <= vSteps && arr.indexOf(s) === idx;
      }).sort(function (x, y) { return x - y; });
      for (k = 0; k < show.length; k += 1) {
        var it = vi.iterations[show[k]];
        iRows.push(tr([rowhead('after ' + show[k] + ' step' + (show[k] === 1 ? '' : 's')),
          td(it.map(function (v) { return Rshort(v, 5, 8); }).join(', ')),
          td(it.map(function (v, idx) { return Rshort(Rabs(Rsub(vi.v[idx], v)), 5, 7); }).join(', ')),
          td(String(String(it[0].d).length) + ' digits')]));
      }
      iRows.push(tr([rowhead('<strong>the exact solve</strong>'),
        td('<strong>' + vi.v.map(Rtext).join(', ') + '</strong>', 'tone-green'),
        td('<span class="tone-green">0</span>'), td(String(String(vi.v[0].d).length) + ' digits')]));
    }
    iterEl.innerHTML = '<caption>Value iteration on the best policy, against the value the solve already '
      + 'had</caption><thead>'
      + tr([th('step'), th('v'), th('how far short'), th('denominator')])
      + '</thead><tbody>' + iRows.join('') + '</tbody>';

    var total = Math.pow(2, n);
    setKpi('mdRoundsK', String(run.iterations));
    setKpi('mdPolicyK', run.policy.map(function (a) { return acts[a]; }).join(' / '));
    setKpi('mdValueK', run.v.map(function (v) { return Rshort(v, 4, 7); }).join(', '));
    setKpi('mdAllK', String(total));
    setKpi('mdVIK', vi ? vi.vT.map(function (v) { return Rshort(v, 4, 6); }).join(', ') : '&mdash;');
    setKpi('mdGapK', vi ? vi.gap.map(function (v) { return Rshort(v, 5, 6); }).join(', ') : '&mdash;');

    statusEl.innerHTML = '<strong>Policy iteration stopped after ' + run.iterations + ' round'
      + (run.iterations === 1 ? '' : 's') + ', and it stopped for a reason.</strong> '
      + 'There are 2^' + n + ' = ' + total + ' policies on ' + n + ' states with two actions; the value never '
      + 'decreases from one round to the next and a policy that repeats would have to have the same '
      + 'value, so the loop cannot go round for ever. That is a termination proof, and it is a better '
      + 'reason to stop than &ldquo;the numbers stopped moving&rdquo;. '
      + 'The evaluation step is where the exactness matters: v = r + &gamma;P&#7529;v is n equations in n '
      + 'unknowns, solved by elimination over rationals, so the value of a policy is '
      + run.v.map(Rtext).join(', ') + ' and not a decimal near it. '
      + (vi
          ? 'Below, value iteration on the same policy is still BELOW that value by '
            + vi.gap.map(function (v) { return Rshort(Rabs(v), 5, 6); }).join(', ') + ' after ' + vSteps
            + ' step' + (vSteps === 1 ? '' : 's') + ' &mdash; it starts at zero and climbs, so it '
            + 'approaches the answer from underneath and never reaches it. Its denominators grow by one '
            + 'power of the discount&rsquo;s denominator at every step, from '
            + String(vi.iterations[1][0].d).length + ' digit'
            + (String(vi.iterations[1][0].d).length === 1 ? '' : 's') + ' to '
            + String(vi.iterations[vSteps][0].d).length + '. It is approaching a number the solve '
            + 'already has, exactly.'
          : '');
  }

  presetS.addEventListener('change', function () {
    var p = PRESETS[presetS.value];
    if (!p) return;
    p0In.value = p.P0; p1In.value = p.P1; r0In.value = p.r0; r1In.value = p.r1;
    namesIn.value = p.names;
    redraw();
  });
  [p0In, p1In, r0In, r1In, namesIn, gS, stepS].forEach(function (el) {
    el.addEventListener('input', redraw);
  });
  redraw();
  window.redrawLab = redraw;
"""
    return _lab(
        cfg,
        title="Choosing an action in every state, and knowing when to stop choosing",
        subtitle="each round is an exact linear solve, and the stopping argument is finiteness",
        markup=markup,
        controls=controls,
        script=script,
        panel_title="Two actions, two matrices, two reward vectors",
        panel_intro="Every policy is evaluated by solving v = r + &gamma;P&#7529;v exactly rather than by "
        "iterating it, which is what lets the page show value iteration converging TO something instead "
        "of stopping when it gets bored.",
    )


# ---------------------------------------------------------------------------
# The registry entry
# ---------------------------------------------------------------------------

_MODES = {
    "chain": _chain,
    "classify": _classify,
    "steady": _steady,
    "absorb": _absorb,
    "mdp": _mdp,
}

MODES = tuple(sorted(_MODES))


def markov_lab(cfg):
    """The chains kit. `cfg["mode"]` chooses the lesson; an unknown one raises.

    The raise is the contract. A kit that fell back to a default would render a
    finished-looking page carrying another lesson's widget: every markup
    assertion passes, labcheck passes, and the reader is shown the wrong
    arithmetic under the right title.
    """
    mode = (cfg or {}).get("mode")
    if mode not in _MODES:
        raise ValueError(
            "markov_lab: unknown mode %r; the five modes of the chains kit are %s"
            % (mode, ", ".join(MODES))
        )
    return _MODES[mode](cfg or {})
