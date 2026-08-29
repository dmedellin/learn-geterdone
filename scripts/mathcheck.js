#!/usr/bin/env node
/*
 * Test the ARITHMETIC the generated paths are built on.
 *
 * WHY THIS EXISTS, and why it is separate from labcheck.js. That harness proves
 * every published lab runs and paints. It cannot prove the numbers are right: a
 * lab that confidently reports the wrong roots passes it, and passes every
 * markup assertion in tests/ too. The footer of every algebra page promises the
 * reader that each figure is computed from the stated definition and that the
 * arithmetic is exact. This file is what makes that promise checkable.
 *
 * The same holds for the logic course: its truth tables and quantifier
 * verdicts are computed by evaluators in scripts/mathpath/labs/logic.py, and a
 * quantifier lab whose status text reasons about a different statement than
 * its evaluator computes runs, paints, and passes labcheck while teaching a
 * falsehood. That defect shipped once; the logic section below is what now
 * catches it.
 *
 * The JavaScript under test IS the JavaScript that ships. It is extracted from
 * scripts/mathpath/labs/algebra_core.py and scripts/mathpath/labs/logic.py,
 * which hold it as raw strings, so there is no second copy to drift -- testing
 * a transcription would prove nothing about the published pages.
 *
 * Usage:  node scripts/mathcheck.js
 */

const fs = require('fs');
const path = require('path');

const SOURCE = path.join(__dirname, 'mathpath', 'labs', 'algebra_core.py');
const src = fs.readFileSync(SOURCE, 'utf8');
const LOGIC_SOURCE = path.join(__dirname, 'mathpath', 'labs', 'logic.py');
const logicSrc = fs.readFileSync(LOGIC_SOURCE, 'utf8');
const COUNTING_SOURCE = path.join(__dirname, 'mathpath', 'labs', 'counting.py');
const countingSrc = fs.readFileSync(COUNTING_SOURCE, 'utf8');
const PROB_SOURCE = path.join(__dirname, 'mathpath', 'labs', 'probability.py');
const probSrc = fs.readFileSync(PROB_SOURCE, 'utf8');

/* Each block is  NAME = r"""..."""  in the Python module. */
function blockFrom(text, name, where) {
  const m = new RegExp(name + ' = r"""([\\s\\S]*?)"""', 'm').exec(text);
  if (!m) { console.error('cannot find ' + name + ' in ' + where); process.exit(2); }
  return m[1];
}
function block(name) { return blockFrom(src, name, SOURCE); }
function logicBlock(name) { return blockFrom(logicSrc, name, LOGIC_SOURCE); }
function countingBlock(name) { return blockFrom(countingSrc, name, COUNTING_SOURCE); }
function probBlock(name) { return blockFrom(probSrc, name, PROB_SOURCE); }

let fails = 0;
function eq(got, want, label) {
  if (String(got) !== String(want)) { fails += 1; console.log('  FAIL ' + label + ': got ' + got + ', want ' + want); }
}
function near(got, want, tol, label) {
  if (!(Math.abs(got - want) <= tol)) { fails += 1; console.log('  FAIL ' + label + ': got ' + got + ', want ~' + want); }
}

/* A minimal SVG DOM, the same shape scripts/labcheck.js gives a real page. */
function El(name) { this.name = name; this.attrs = {}; this.children = []; this._text = ''; }
El.prototype.setAttribute = function (k, v) { this.attrs[k] = String(v); };
El.prototype.getAttribute = function (k) { return this.attrs[k]; };
El.prototype.appendChild = function (c) { this.children.push(c); return c; };
Object.defineProperty(El.prototype, 'textContent', {
  get: function () { return this._text; },
  set: function (v) { this._text = String(v); if (v === '') this.children = []; }
});
global.document = { createElementNS: function (_ns, n) { return new El(n); } };
function all(el, name, out) {
  out = out || [];
  el.children.forEach(function (c) { if (c.name === name) out.push(c); all(c, name, out); });
  return out;
}

eval(block('RATIONAL_JS') + block('POLY_JS') + block('EXPR_JS') + block('SURD_JS') + block('PLOT_JS'));

// ------------------------------------------------- exact rational arithmetic
console.log('exact rationals');
eq(Rtext(Radd(R(1n, 3n), R(1n, 6n))), '1/2', '1/3 + 1/6');
eq(Rtext(Rmul(R(2n, 3n), R(9n, 4n))), '3/2', '2/3 * 9/4');
eq(Rtext(Rdiv(R(-3n, 4n), R(6n, 8n))), '-1', '-3/4 / 3/4');
eq(Rtext(Rpow(R(2n, 3n), 3)), '8/27', '(2/3)^3');
eq(Rtext(Rpow(R(2n), -3)), '1/8', '2^-3');
eq(Rtext(Rparse('-7/14')), '-1/2', 'parse -7/14 in lowest terms');
eq(Rtext(Rparse('0.375')), '3/8', 'a decimal becomes an exact fraction');
eq(Rtext(Rsqrt(R(4n, 9n))), '2/3', 'sqrt(4/9)');
eq(Rsqrt(R(2n)), 'null', 'sqrt(2) is not rational, and says so');
eq(Rcmp(R(1n, 3n), R(1n, 2n)), -1, 'comparison');
/* Exactness is the whole promise: forty additions of a third stay a third. */
let big = R(1n, 3n);
for (let i = 0; i < 40; i += 1) big = Radd(big, R(1n, 3n));
eq(Rtext(big), '41/3', '41 thirds, exactly');

// ------------------------------------------------------ polynomials over Q
console.log('polynomials over Q');
function P() { return Array.prototype.slice.call(arguments).map(v => (typeof v === 'object' ? v : R(BigInt(v)))); }
eq(Ptext(P(-6, 1, 1)), 'x^2 + x - 6', 'standard form');
eq(Ptext(P(0, 0, 3)), '3x^2', 'a monomial');
eq(Ptext(P(1, -1)), '-x + 1', 'a leading -1 is written as a sign');
eq(Ptext([R(3n, 4n), R(1n)]), 'x + (3/4)', 'a fractional coefficient is bracketed');
eq(Ptext([]), '0', 'the zero polynomial');
eq(Pdeg([]), -1, 'the zero polynomial has degree -1');
eq(Ptext(Pmul(P(-2, 1), P(3, 1))), 'x^2 + x - 6', '(x-2)(x+3) expands');
eq(Rtext(Peval(P(-6, 1, 1), R(2n))), '0', 'p(2) = 0');
eq(Ptext(Pderiv(P(-6, 1, 1))), '2x + 1', 'derivative');
const dm = Pdivmod(P(-6, 1, 1), P(-2, 1));
eq(Ptext(dm.q) + ' r ' + Ptext(dm.r), 'x + 3 r 0', 'exact division');
const dm2 = Pdivmod(P(1, 0, 0, 1), P(-1, 1));
eq(Ptext(dm2.q) + ' r ' + Ptext(dm2.r), 'x^2 + x + 1 r 2', 'x^3+1 divided by x-1');
eq(Ptext(Pgcd(P(-6, 1, 1), P(-4, 0, 1))), 'x - 2', 'polynomial gcd');

// ---------------------------------------- the rational root theorem, applied
console.log('rational roots and factoring');
eq(Prationalroots(P(-6, 1, 1)).map(Rtext).join(','), '-3,2', 'roots of x^2+x-6');
eq(Prationalroots(P(-3, 5, 2)).map(Rtext).join(','), '-3,1/2', 'roots of 2x^2+5x-3');
eq(Prationalroots(P(1, 0, 1)).length, 0, 'x^2+1 has no rational root');
/* Factors come out in ascending order of their root: deterministic and stated. */
eq(Pfactortextfull(P(-6, 1, 1)), '(x + 3)(x - 2)', 'factor x^2+x-6');
eq(Pfactortextfull(P(-3, 5, 2)), '(x + 3)(2x - 1)', 'factor 2x^2+5x-3');
eq(Pfactortextfull(P(4, -4, 1)), '(x - 2)^2', 'a perfect square keeps its multiplicity');
eq(Pfactortextfull(P(1, 0, 1)), 'x^2 + 1', 'an irreducible polynomial is written as itself');
eq(Pfactortextfull(P(-4, 0, 1)), '(x + 2)(x - 2)', 'difference of squares');
eq(Pfactortextfull(P(0, -9, 0, 1)), 'x(x + 3)(x - 3)', 'x^3-9x');
eq(Pfactortextfull(P(6, -5, 1)), '(x - 2)(x - 3)', 'x^2-5x+6');
/* 4x^3-8x-12 = 4(x^3-2x-3), and +-1, +-3 are the only candidates: none works. */
eq(Pfactortextfull(P(-12, -8, 0, 4)), '4(x^3 - 2x - 3)', 'the content comes out, the cubic stays');
eq(Pfactor(P(-12, -8, 0, 4)).complete, false, 'a cubic leftover is not claimed complete');
eq(Pfactor(P(1, 0, 1)).complete, true, 'a quadratic leftover is complete');

// ------------------------------------------------------- expression parsing
console.log('the expression parser');
const ev = (s, x) => Eeval(Eparse(s), { x: x });
const pol = (s) => { const p = Epolyof(s); return p === null ? 'null' : Ptext(p); };
eq(ev('2x', 3), 6, 'implicit multiplication: 2x');
eq(ev('3(x+1)', 4), 15, '3(x+1)');
eq(ev('(x+1)(x-2)', 5), 18, '(x+1)(x-2)');
eq(ev('4x^2', 3), 36, '4x^2');
eq(ev('2sqrt(x)', 9), 6, '2sqrt(x)');
eq(Eeval(Eparse('xy'), { x: 3, y: 4 }), 12, 'xy is a product of two variables');
/* The two places a reader is marked wrong. */
eq(ev('-x^2', 3), -9, '-x^2 means -(x^2)');
eq(ev('(-x)^2', 3), 9, '(-x)^2');
eq(ev('2^3^2', 0), 512, '^ is right-associative');
eq(ev('8/2/2', 0), 2, '/ is left-associative');
eq(ev('2*3^2', 0), 18, 'power before times');
eq(isNaN(ev('sqrt(x)', -1)), true, 'outside the domain gives NaN, not an exception');
/* Errors are named rather than swallowed. */
const msg = (s) => { try { Eparse(s); return ''; } catch (e) { return e.message; } };
eq(msg('2x +'), 'the expression ends early', 'a trailing operator');
eq(msg('sqrtt(x)'), 'unknown function "sqrtt"', 'a typo in a function name');
eq(msg('x $ 2'), 'unexpected character "$"', 'a stray character');
eq(msg('(x+1'), 'expected ")"', 'an unclosed bracket');
/* Typed input reaches the EXACT machinery, not a float approximation of it. */
eq(pol('(x+1)(x-2)'), 'x^2 - x - 2', 'a typed product expands exactly');
eq(pol('(x/3) + 1/2'), '(1/3)x + (1/2)', 'rational coefficients stay exact');
eq(pol('(2x-1)^3'), '8x^3 - 12x^2 + 6x - 1', 'a typed cube expands');
eq(pol('sqrt(x)'), 'null', 'sqrt(x) is not a polynomial');
eq(pol('1/x'), 'null', 'division by x is not a polynomial');
eq(pol('0.1x + 0.2x'), '(3/10)x', '0.1 + 0.2 is 3/10, not 0.30000000000000004');

// ----------------------------------------------- surds and quadratic roots
console.log('exact surds and quadratic roots');
const Q = (v) => R(BigInt(v));
eq(surdtext(Rsurd(Q(9))), '3', 'sqrt(9)');
eq(surdtext(Rsurd(Q(8))), '2sqrt(2)', 'sqrt(8)');
eq(surdtext(Rsurd(R(1n, 2n))), '(1/2)sqrt(2)', 'sqrt(1/2)');
eq(surdtext(Rsurd(Q(72))), '6sqrt(2)', 'sqrt(72)');
let r = quadroots(Q(1), Q(-5), Q(6));
eq(r.kind + ' ' + r.roots.map(Rtext).join(','), 'rational 2,3', 'x^2-5x+6');
r = quadroots(Q(1), Q(-2), Q(-4));
eq(r.kind + ' ' + pmtext(r.p, r.s), 'irrational 1 +- sqrt(5)', 'x^2-2x-4 keeps its surd');
r = quadroots(Q(1), Q(-4), Q(4));
eq(r.kind + ' ' + Rtext(r.roots[0]), 'double 2', 'a repeated root');
r = quadroots(Q(1), Q(0), Q(1));
eq(r.kind + ' ' + pmtext(r.p, r.s, true), 'complex +-i', 'x^2+1');
r = quadroots(Q(1), Q(-2), Q(5));
eq(r.kind + ' ' + pmtext(r.p, r.s, true), 'complex 1 +- 2i', 'x^2-2x+5');
eq(quadroots(Q(2), Q(5), Q(-3)).roots.map(Rtext).join(','), '-3,1/2', '2x^2+5x-3');
r = quadroots(Q(3), Q(-6), Q(2));
eq(pmtext(r.p, r.s), '1 +- (1/3)sqrt(3)', '3x^2-6x+2');
/* The irrational pair really are roots: substitute them back. */
{
  const a = 3, b = -6, c = 2;
  const pv = Rnum(r.p), sv = Rnum(r.s.q) * Math.sqrt(Number(r.s.k));
  eq(Math.abs(a * (pv + sv) * (pv + sv) + b * (pv + sv) + c) < 1e-12, true, 'the + root checks out');
  eq(Math.abs(a * (pv - sv) * (pv - sv) + b * (pv - sv) + c) < 1e-12, true, 'the - root checks out');
}

// ------------------------------------------------------------- the grapher
console.log('the grapher');
{
  const svg = new El('svg');
  const p = Plot(svg, { xmin: -5, xmax: 5, ymin: -10, ymax: 10 });
  near(p.sx(-5), 44, 0.01, 'left edge');
  near(p.sx(5), 644, 0.01, 'right edge');
  near(p.sx(0), 344, 0.01, 'x = 0 is centred');
  near(p.sy(10), 16, 0.01, 'top edge');
  near(p.sy(-10), 386, 0.01, 'bottom edge');
  eq(p.sy(5) < p.sy(-5), true, 'positive y is higher on screen');
  p.frame();
  eq(svg.getAttribute('viewBox'), '0 0 660 420', 'viewBox');
  const axes = all(svg, 'line').filter(l => l.attrs.class === 'plot-axis');
  eq(axes.length, 2, 'two axes');
  near(parseFloat(axes[0].attrs.y1), 201, 0.01, 'the x-axis sits at y = 0');
  near(parseFloat(axes[1].attrs.x1), 344, 0.01, 'the y-axis sits at x = 0');
}
{
  /* A window with zero out of view still gets a labelled frame. */
  const svg = new El('svg');
  Plot(svg, { xmin: 10, xmax: 20, ymin: 100, ymax: 200 }).frame();
  const axes = all(svg, 'line').filter(l => l.attrs.class === 'plot-axis');
  near(parseFloat(axes[0].attrs.y1), 386, 0.01, 'the x-axis pins to the near edge');
  near(parseFloat(axes[1].attrs.x1), 44, 0.01, 'the y-axis pins to the near edge');
}
function runs(fn) {
  const svg = new El('svg');
  Plot(svg, { xmin: -5, xmax: 5, ymin: -10, ymax: 10 }).frame().curve(fn);
  return all(svg, 'polyline');
}
eq(runs(x => x * x - 4).length, 1, 'a parabola is one unbroken run');
/* Joining across a pole draws a vertical line that is not part of the graph,
   which is exactly why readers believe 1/x is connected.
   The curve breaks for TWO different reasons and both need testing. A pole the
   sampler lands on exactly returns Infinity and breaks on the non-finite check;
   a pole it steps over returns two large finite values of opposite sign and can
   only be caught by the jump check. Sampling runs from -5 to 5 in 480 steps, so
   x = 0 IS a sample and x = 0.3 is not -- and a test using only 1/x passes with
   the jump check deleted, which is how this gap was found. */
eq(runs(x => 1 / x).length, 2, '1/x: a pole landed on exactly');
eq(runs(x => 1 / (x - 0.3)).length, 2, '1/(x-0.3): a pole stepped over');
eq(runs(x => 1 / (x * x - 0.09)).length, 3, 'two stepped-over poles give three runs');
{
  const rs = runs(x => Math.sqrt(x));
  eq(rs.length, 1, 'sqrt(x) is one run');
  eq(parseFloat(rs[0].attrs.points.split(' ')[0].split(',')[0]) >= 343.9, true,
     'sqrt(x) starts at x = 0 and not before');
}
{
  const svg = new El('svg');
  const pl = Plot(svg, { xmin: -5, xmax: 5, ymin: -10, ymax: 10 }).frame();
  pl.point(2, -4, 'plot-point root', '2');
  const c = all(svg, 'circle').filter(e => e.attrs.class === 'plot-point root');
  near(parseFloat(c[0].attrs.cx), 464, 0.01, 'a marked point lands where the number says');
  near(parseFloat(c[0].attrs.cy), 275, 0.01, 'and at the right height');
  pl.vline(3, 'plot-asym', 'x = 3');
  near(parseFloat(all(svg, 'line').filter(e => e.attrs.class === 'plot-asym')[0].attrs.x1), 524, 0.01,
       'an asymptote lands where the number says');
  const before = all(svg, 'circle').length;
  pl.point(NaN, 3); pl.point(1, Infinity);
  eq(all(svg, 'circle').length, before, 'a non-finite point is skipped, not drawn at NaN');
}
{
  const svg = new El('svg');
  NumberLine(svg, -10, 10).interval(-3, 5, true, false);
  const ends = all(svg, 'circle');
  eq(ends.length, 2, 'an interval has two endpoints');
  eq(ends[0].attrs.class, 'plot-end closed', 'a closed end is filled');
  eq(ends[1].attrs.class, 'plot-end open', 'an open end is hollow');
  near(parseFloat(ends[0].attrs.cx), 30 + (7 / 20) * 600, 0.01, 'the closed end is placed correctly');
}

// ---------------------------------------------------- propositional logic
console.log('propositional logic (course 1 labs)');
eval(logicBlock('PARSER_JS'));
{
  const T = { p: true }, F = { p: false };
  const env = (p, q) => ({ p, q });
  /* The conditional's one false row, and vacuous truth in both false-p rows. */
  const imp = parse('p -> q');
  eq(evalNode(imp, env(true, false)), false, 'T -> F is the one false row');
  eq(evalNode(imp, env(false, true)), true, 'F -> T is vacuously true');
  eq(evalNode(imp, env(false, false)), true, 'F -> F is vacuously true');
  /* Precedence: ~ binds tighter than &, and ~p & q differs from ~(p & q). */
  eq(evalNode(parse('~p & q'), env(false, false)), false, '~p & q at FF: negation binds tight');
  eq(evalNode(parse('~(p & q)'), env(false, false)), true, '~(p & q) at FF');
  /* Inclusive or vs xor part company in exactly the TT row. */
  eq(evalNode(parse('p | q'), env(true, true)), true, 'inclusive or is true at TT');
  eq(evalNode(parse('p ^ q'), env(true, true)), false, 'xor is false at TT');
  /* -> is right-associative: p -> q -> r is p -> (q -> r). */
  eq(evalNode(parse('p -> q -> r'), { p: true, q: true, r: false }), false, 'p->q->r at TTF');
  eq(evalNode(parse('p -> q -> r'), { p: false, q: true, r: false }), true, 'p->q->r at FTF: right-associative');
  /* Constants, so ⊤ and ⊥ mean what the pages say they mean. */
  eq(evalNode(parse('⊤'), {}), true, 'top is true');
  eq(evalNode(parse('⊥ -> p'), F), true, 'ex falso: bottom implies anything');
  /* Whole-table facts, over every assignment: the identities the lessons teach. */
  function rowsFor(vars) { return assignments(vars); }
  function agreeEverywhere(aSrc, bSrc, vars) {
    const a = parse(aSrc), b = parse(bSrc);
    return rowsFor(vars).every((e) => evalNode(a, e) === evalNode(b, e));
  }
  eq(agreeEverywhere('~(p & q)', '~p | ~q', ['p', 'q']), true, 'De Morgan over all four rows');
  eq(agreeEverywhere('p -> q', '~q -> ~p', ['p', 'q']), true, 'contraposition over all four rows');
  eq(agreeEverywhere('p -> q', 'q -> p', ['p', 'q']), false, 'the converse is NOT equivalent');
  const mt = parse('((p -> q) & ~q) -> ~p');
  eq(rowsFor(['p', 'q']).every((e) => evalNode(mt, e)), true, 'modus tollens is a tautology');
  const ac = parse('((p -> q) & q) -> p');
  eq(rowsFor(['p', 'q']).every((e) => evalNode(ac, e)), false, 'affirming the consequent is not');
  /* The row order the lessons teach: T before F, rightmost fastest. */
  eq(rowsFor(['p', 'q']).map((e) => (e.p ? 'T' : 'F') + (e.q ? 'T' : 'F')).join(' '),
     'TT TF FT FF', 'conventional row order');
}

// ------------------------------------------------------- quantifier verdicts
console.log('quantifier verdicts (course 1 labs)');
eval(logicBlock('QUANT_EVAL_JS'));
{
  /* Exhaustive over every 3x3 predicate: 512 grids. This is the check that
     would have caught the shipped row/column confusion, so it is done by
     enumeration rather than by trusting a handful of examples. */
  const N = 3;
  let thmOk = true, mirrorOk = true, negOk = true;
  for (let bits = 0; bits < 512; bits += 1) {
    const P = [], C = [];
    for (let x = 0; x < N; x += 1) {
      P.push([]); C.push([]);
      for (let y = 0; y < N; y += 1) {
        const v = ((bits >> (x * N + y)) & 1) === 1;
        P[x].push(v); C[x].push(!v);
      }
    }
    /* The lesson's theorem, and its mirror -- each in its own variables. */
    if (qExistsYForallX(P, N).v && !qForallXExistsY(P, N).v) thmOk = false;
    if (qExistsXForallY(P, N).v && !qForallYExistsX(P, N).v) mirrorOk = false;
    /* Lesson 10: negation flips every quantifier. Three dual pairs. */
    if (qForallForall(P, N).v !== !qExistsExists(C, N).v) negOk = false;
    if (qForallXExistsY(P, N).v !== !qExistsXForallY(C, N).v) negOk = false;
    if (qExistsYForallX(P, N).v !== !qForallYExistsX(C, N).v) negOk = false;
  }
  eq(thmOk, true, 'exists-y-forall-x implies forall-x-exists-y, all 512 grids');
  eq(mirrorOk, true, 'exists-x-forall-y implies forall-y-exists-x, all 512 grids');
  eq(negOk, true, 'negation duality across all three pairs, all 512 grids');

  /* A full row is not a full column: the regression that shipped. */
  const rowGrid = [[true, true, true], [false, false, false], [false, false, false]];
  eq(qExistsXForallY(rowGrid, N).v, true, 'a full row satisfies exists-x-forall-y');
  eq(qExistsYForallX(rowGrid, N).v, false, 'a full row does NOT satisfy exists-y-forall-x');
  eq(qForallXExistsY(rowGrid, N).v, false, 'and forall-x-exists-y fails: x = 2 has no y');

  /* The presets, on the 4-element universe the lessons publish. */
  function fill(n, fn) {
    const P = [];
    for (let x = 0; x < n; x += 1) { P.push([]); for (let y = 0; y < n; y += 1) P[x].push(!!fn(x + 1, y + 1)); }
    return P;
  }
  const diag = fill(4, (x, y) => x === y);
  eq(qForallXExistsY(diag, 4).v, true, 'identity: every x has its own y');
  eq(qExistsYForallX(diag, 4).v, false, 'identity: no single y serves every x — the lesson-9 separator');
  const succ = fill(4, (x, y) => y === x + 1);
  eq(qForallXExistsY(succ, 4).v, false, 'successor on {1..4}: forall-x-exists-y FAILS');
  eq(qForallXExistsY(succ, 4).why, 'x = 4 has no y at all', 'and names the top element as the reason');
  const le = fill(4, (x, y) => x <= y);
  const leVerdicts = [qForallForall(le, 4), qForallXExistsY(le, 4), qExistsYForallX(le, 4),
                      qForallYExistsX(le, 4), qExistsXForallY(le, 4), qExistsExists(le, 4)];
  eq(leVerdicts.filter((r) => r.v).length, 5, 'order preset: five of six verdicts true, as lesson 10 says');
  const leC = fill(4, (x, y) => !(x <= y));
  const leCVerdicts = [qForallForall(leC, 4), qForallXExistsY(leC, 4), qExistsYForallX(leC, 4),
                       qForallYExistsX(leC, 4), qExistsXForallY(leC, 4), qExistsExists(leC, 4)];
  eq(leCVerdicts.filter((r) => r.v).map((r) => r.why).join(';'),
     'x = 2, y = 1 works', 'complemented order preset: only exists-exists survives');
}

// ------------------------------------------------------------- counting
console.log('counting in BigInt (course 4 labs)');
{
  /* The course-4 labs promise the reader that every count is exact and that
     the derangement lab's three routes agree. The functions below are the
     shipped ones, extracted from counting.py; a wrong comb() would reach
     every page that lists selections, and a wrong derangeTerms() would ship a
     table that confidently disagrees with the lesson above it. */
  eval(countingBlock('BIGINT_JS') + countingBlock('DERANGE_JS'));

  eq(fact(0), 1n, '0! = 1');
  eq(fact(20), 2432902008176640000n, '20! exactly');
  eq(perm(10, 3), 720n, 'P(10,3) = 720');
  eq(perm(24, 12), 1295295050649600n, 'P(24,12), the largest P the lab can show');
  eq(perm(3, 5), 0n, 'P(n, r) with r > n is 0');
  eq(comb(52, 5), 2598960n, 'C(52,5) = 2 598 960');
  eq(comb(35, 12), 834451800n, 'C(35,12), the largest C(n+r-1, r) the lab can show');
  eq(comb(7, 5), 21n, 'C(7,5) = 21: five doughnuts from three kinds');
  eq(comb(6, 2), comb(5, 1) + comb(5, 2), "Pascal's rule at the lesson-5 preset");
  eq(comb(4, 7), 0n, 'C(n, r) with r > n is 0');
  eq(group(1295295050649600n), '1 295 295 050 649 600', 'digit grouping');

  const D = [1n, 0n, 1n, 2n, 9n, 44n, 265n, 1854n, 14833n, 133496n];
  for (let n = 0; n < D.length; n += 1) {
    eq(derangeFormula(n), D[n], 'D_' + n + ' by the alternating sum');
    eq(derangeRec(n), D[n], 'D_' + n + ' by the recurrence');
    if (n <= 8) eq(derangeBrute(n), D[n], 'D_' + n + ' by listing');
  }
  eq(derangeFormula(12), 176214841n, 'D_12, the largest n the slider allows');
  eq(derangeList(4).sort().join(','), '2143,2341,2413,3142,3412,3421,4123,4312,4321', 'the nine derangements of 1..4');
  const rows6 = derangeTerms(6).map((r) => r.running.toString()).join(',');
  eq(rows6, '720,0,360,240,270,264,265', 'the running total at n = 6 swings and settles on 265');
  eq(ratioDigits(265n, 720n, 7), '0.3680556', 'D_6/6! to seven places, rounded');
  eq(ratioDigits(1854n, 5040n, 7), '0.3678571', 'D_7/7! to seven places');
  eq(ratioDigits(14833n, 40320n, 7), '0.3678819', 'D_8/8! to seven places (the lesson table row)');
  eq(ratioDigits(1n, 3n, 4), '0.3333', 'ratioDigits pads and truncates correctly');
  eq(ratioDigits(0n, 1n, 7), '0.0000000', 'ratioDigits at zero');
  eq(ratioDigits(1n, 2n, 3), '0.500', 'ratioDigits at one half');
}

// ---------------------------------------------------------- probability
console.log('probability as exact fractions and summed distributions (course 5 labs)');
{
  /* The course-5 footer promises every probability is an exact fraction from
     the enumerated sample space, and that the distributions are summed term by
     term and compared with the closed forms. The functions below are the
     shipped ones, extracted from probability.py. The geometric case is the one
     that failed: a sum stopped at thirty terms reads 5.848 against a closed
     form of 6 at p = 1/6, and the lab printed both side by side. */
  eval(probBlock('FRACTION_JS') + probBlock('DIST_JS') + probBlock('BAYES_JS'));

  eq(frac(6, 36).text, '1/6', '6/36 reduces to 1/6');
  eq(frac(0, 15).text, '0', 'an empty event is 0, not 0/15');
  eq(frac(15, 15).text, '1', 'the whole space is 1');
  eq(frac(3, 0).text, 'undefined', 'conditioning on an empty event is undefined');
  eq(pct(frac(1, 6)), '16.67%', 'pct rounds to two places');
  eq(frac(18 * 6, 36 * 36).text, '1/12', 'P(A)·P(B) for first-even and sum-7, the lesson-5 pair');

  eq(comb(52, 5), 2598960, 'C(52,5) in doubles is still exact');
  eq(comb(20, 5), 15504, 'C(20,5)');

  const bin = binomialPmf(20, 0.25), mb = moments(bin.ks, bin.probs);
  near(bin.probs[5], 0.2023311518569244, 1e-12, 'P(X = 5) at n = 20, p = 1/4 (lesson 11 worked example)');
  near(mb.E, 5, 1e-12, 'E[X] summed = np = 5');
  near(mb.V, 3.75, 1e-12, 'Var(X) summed = np(1-p) = 3.75');
  near(mb.total, 1, 1e-12, 'the binomial sums to 1');
  near(bin.probs.slice(10).reduce((s, x) => s + x, 0), 0.01386441694376117, 1e-12, 'P(X >= 10) = 0.0139');
  const bin10 = binomialPmf(10, 0.5);
  near(bin10.probs[5], 0.24609375, 1e-15, 'P(exactly 5 heads in 10) = 252/1024');
  near(moments(bin10.ks, bin10.probs).E, 5, 1e-12, 'E[X] = 5 at n = 10, p = 1/2 (lesson 9 preset)');

  const K = geometricTerms(1 / 6);
  eq(K > 30, true, 'the geometric sum runs past the thirty drawn bars');
  eq(Math.pow(5 / 6, K) < 1e-15, true, 'and stops only when the tail is below 1e-15');
  const geo = geometricPmf(1 / 6, K), mg = moments(geo.ks, geo.probs);
  near(geo.probs[0], 1 / 6, 1e-15, 'P(X = 1) = 1/6, the mode');
  near(geo.probs[5], 0.06697959533607682, 1e-15, 'P(X = 6) = (5/6)^5 / 6');
  near(mg.E, 6, 1e-9, 'E[X] summed = 1/p = 6 (lesson 12 worked example)');
  near(mg.V, 30, 1e-6, 'Var(X) summed = (1-p)/p^2 = 30');
  near(mg.total, 1, 1e-12, 'the geometric sums to 1');
  near(moments(geo.ks.slice(0, 30), geo.probs.slice(0, 30)).E, 5.848342071608853, 1e-9,
       'thirty terms alone give 5.848 -- the figure the lab used to print beside 6');
  const geo12 = geometricPmf(1 / 12, geometricTerms(1 / 12)), mg12 = moments(geo12.ks, geo12.probs);
  near(mg12.E, 12, 1e-9, 'E[X] = 12 at the smallest p the slider allows');
  near(mg12.V, 132, 1e-6, 'Var(X) = 132 there');

  const uni = uniformPmf(6), mu = moments(uni.ks, uni.probs);
  near(mu.E, 3.5, 1e-12, 'a fair die: E[X] = 3.5 (lesson 8 preset)');
  near(mu.V, 35 / 12, 1e-12, 'a fair die: Var(X) = 35/12 (lesson 10)');
  const dice = diceSumPmf(), md = moments(dice.ks, dice.probs);
  eq(dice.probs.map((x) => Math.round(x * 36)).join(','), '1,2,3,4,5,6,5,4,3,2,1', 'the triangle over 36 (lesson 7 table)');
  near(md.E, 7, 1e-12, 'sum of two dice: E[X] = 7');
  near(md.V, 35 / 6, 1e-12, 'sum of two dice: Var(X) = 35/6, the lesson-10 worked example by another route');

  const cells = bayesCounts(1000000, 1000, 99, 5);
  eq([cells.D, cells.TP, cells.FN, cells.H, cells.FP, cells.TN].join(','), '1000,990,10,999000,49950,949050',
     'the four cells at 1 in 1000, 99%, 5%');
  eq(cells.posterior.text, '11/566', 'P(D|+) = 990/50940 = 11/566');
  near(cells.posterior.dec, 0.019434628975265017, 1e-15, 'about 2%, the lesson-6 answer');
  near(cells.npv.dec, 949050 / 949060, 1e-15, 'P(no D | -) from the same cells');
  eq(bayesCounts(1000000, 300000, 99, 5).posterior.text, '297/332', 'the worked example: prior 0.30 gives 297/332 = 0.895');
  eq(bayesCounts(1000000, 20000, 95, 10).posterior.text, '19/117', 'the standard: 2%, 95%, 10% gives 19/117');
  const rare = bayesCounts(1000000, 100, 99, 1);
  eq(rare.FP / rare.TP, 101, 'concept 3: 1 in 10 000 at a 1% false-positive rate is about 100 false positives per true one');
  eq(grp(50940), '50 940', 'digit grouping');
  eq(dec(990, 1000000), '0.00099', 'decimals are printed without trailing zeros');
  eq(dec(99, 100), '0.99', 'and a percentage as its decimal');
}

if (fails) {
  console.log('\n' + fails + ' assertion(s) FAILED');
  process.exit(1);
}
console.log('\nevery arithmetic assertion passes');
