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
const NUMBER_SOURCE = path.join(__dirname, 'mathpath', 'labs', 'number.py');
const numberSrc = fs.readFileSync(NUMBER_SOURCE, 'utf8');
const GRAPH_SOURCE = path.join(__dirname, 'mathpath', 'labs', 'graph.py');
const graphSrc = fs.readFileSync(GRAPH_SOURCE, 'utf8');
const ALGO_SOURCE = path.join(__dirname, 'mathpath', 'labs', 'algorithms.py');
const algoSrc = fs.readFileSync(ALGO_SOURCE, 'utf8');
const SYSD_SOURCE = path.join(__dirname, 'mathpath', 'labs', 'sysdesign_core.py');
const sysdSrc = fs.readFileSync(SYSD_SOURCE, 'utf8');
const ESTIMATE_SOURCE = path.join(__dirname, 'mathpath', 'labs', 'estimate.py');
const estimateSrc = fs.readFileSync(ESTIMATE_SOURCE, 'utf8');
const LATENCY_SOURCE = path.join(__dirname, 'mathpath', 'labs', 'latency.py');
const latencySrc = fs.readFileSync(LATENCY_SOURCE, 'utf8');

/* Each block is  NAME = r"""..."""  in the Python module. */
function blockFrom(text, name, where) {
  const m = new RegExp(name + ' = r"""([\\s\\S]*?)"""', 'm').exec(text);
  if (!m) { console.error('cannot find ' + name + ' in ' + where); process.exit(2); }
  return m[1];
}
function block(name) { return blockFrom(src, name, SOURCE); }
function logicBlock(name) { return blockFrom(logicSrc, name, LOGIC_SOURCE); }
function sysdBlock(name) { return blockFrom(sysdSrc, name, SYSD_SOURCE); }
function estimateBlock(name) { return blockFrom(estimateSrc, name, ESTIMATE_SOURCE); }
function latencyBlock(name) { return blockFrom(latencySrc, name, LATENCY_SOURCE); }
function countingBlock(name) { return blockFrom(countingSrc, name, COUNTING_SOURCE); }
function probBlock(name) { return blockFrom(probSrc, name, PROB_SOURCE); }
function numberBlock(name) { return blockFrom(numberSrc, name, NUMBER_SOURCE); }
function graphBlock(name) { return blockFrom(graphSrc, name, GRAPH_SOURCE); }
function algoBlock(name) { return blockFrom(algoSrc, name, ALGO_SOURCE); }

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

// -------------------------------------------------------- number theory
console.log('number theory in BigInt (course 6 labs)');
{
  /* The course-6 footer promises exact big-integer arithmetic, and lesson 14
     promises that the key the lab generates decrypts and is then recovered by
     factoring. The functions below are the shipped ones, extracted from
     number.py. The case that motivated this section: the lesson-14 worked
     example printed c = 3 for 9^7 mod 143 while the lab under it printed 48;
     the lab was right, and nothing checked either. */
  eval(numberBlock('NT_JS'));

  eq(bgcd(1071n, 462n), 21n, 'gcd(1071, 462) = 21 (lesson 5 worked example)');
  eq(bgcd(264n, 84n), 12n, 'gcd(264, 84) = 12 (lesson 4 worked example)');
  eq(bgcd(-12n, 18n), 6n, 'gcd ignores sign');
  eq(bgcd(17n, 0n), 17n, 'gcd(a, 0) = a, the base case');
  eq(egcd(1071n, 462n).join(','), '21,-3,7', '1071·(−3) + 462·7 = 21 (lesson 6 body)');
  eq(egcd(17n, 3120n).join(','), '1,-367,2', '17·(−367) + 3120·2 = 1 (lesson 6 worked example)');
  const tr = egcdTrace(17n, 3120n);
  eq(tr.g + ',' + tr.x + ',' + tr.y, '1,-367,2', 'the trace ends where egcd does');
  eq(tr.rows.every((r) => 17n * r.s + 3120n * r.t === r.r), true, 'r = a·s + b·t holds on every row of the trace');
  eq(tr.rows.map((r) => r.r).join(','), '17,3120,17,9,8,1,0', 'the remainders are the worked example\'s 9, 8, 1, 0');
  const trn = egcdTrace(-1071n, 462n);
  eq(-1071n * trn.x + 462n * trn.y, trn.g, 'a negative input keeps the identity true as typed');
  eq(modinv(17n, 3120n), 2753n, '17⁻¹ mod 3120 = 2753, the RSA private exponent');
  eq(modinv(7n, 26n), 15n, '7⁻¹ mod 26 = 15 (lesson 9 example, lesson 6 standard)');
  eq(modinv(5n, 26n), 21n, '5⁻¹ mod 26 = 21 (lesson 13 example)');
  eq(modinv(15n, 26n), 7n, '15⁻¹ mod 26 = 7 (lesson 13 worked example)');
  eq(modinv(6n, 9n), null, 'no inverse when the gcd is not 1');
  eq(modinv(2n, 4n), null, '2 has no inverse mod 4');
  eq(modinv(-367n, 3120n), 17n, 'the inverse of −367 ≡ 2753 is 17: a negative representative is reduced first');

  eq(modpow(7n, 128n, 13n), 3n, '7^128 mod 13 = 3 (lesson 8 body)');
  eq(modpow(3n, 200n, 50n), 1n, '3^200 mod 50 = 1 (lesson 8 worked example)');
  eq(modpow(5n, 117n, 19n), 1n, '5^117 mod 19 (lesson 8 standard)');
  eq(modpow(7n, 100n, 10n), 1n, '7^100 ends in 1 (lesson 7 worked example)');
  eq(modpow(7n, 1000n, 13n), 9n, '7^1000 mod 13 = 9 (lesson 11 body)');
  eq(modpow(3n, 1234567n, 100n), 87n, '3^1234567 mod 100 = 87 (lesson 11 worked example)');
  eq(modpow(2n, 1000000n, 77n), 23n, '2^1000000 mod 77 (lesson 11 standard) equals 2^40 mod 77');
  eq(modpow(2n, 40n, 77n), 23n, 'because the exponent reduces modulo φ(77) = 60');
  eq(modpow(2n, 10n, 7n), 2n, '2^10 mod 7 = 2, not the 1 that reducing the exponent mod 7 gives (lesson 11 mistake 1)');
  eq(modpow(-7n, 3n, 10n), 7n, 'a negative base is reduced into [0, m) first');
  eq(modpow(65n, 17n, 3233n), 2790n, '65^17 mod 3233 = 2790 (the textbook key)');
  eq(modpow(2790n, 2753n, 3233n), 65n, 'and 2790^2753 mod 3233 = 65 decrypts it');
  eq(modpow(9n, 7n, 143n), 48n, '9^7 mod 143 = 48 — the lesson-14 worked example, which once said 3');
  eq(modpow(48n, 103n, 143n), 9n, 'and 48^103 mod 143 = 9 decrypts it');
  eq(modpow(3n, 103n, 143n), 16n, 'the old ciphertext 3 would not have decrypted to 9');
  const mt = modpowTrace(7n, 128n, 13n, 64);
  eq(mt.result, 3n, 'the trace reaches the same answer as modpow');
  eq(mt.rows.length + ',' + mt.squarings + ',' + mt.mults, '8,7,1', '7^128: eight rows, seven squarings, one multiplication');
  eq(mt.rows.map((r) => r.power).join(','), '7,10,9,3,9,3,9,3', 'the powers 7, 10, 9, 3, 9, 3, 9, 3 the body lists');
  const mt2 = modpowTrace(3n, 200n, 50n, 64);
  eq(mt2.rows.map((r) => r.power).join(','), '3,9,31,11,21,41,31,11', 'the worked example\'s column: 3, 9, 31, 11, 21, 41, 31, 11');
  eq(mt2.rows.map((r) => (r.use ? 1 : 0)).join(''), '00010011', 'set bits at positions 3, 6 and 7');
  eq(mt2.squarings + ',' + mt2.mults + ',' + mt2.result, '7,3,1', 'seven squarings, three multiplications, result 1');
  eq(modpowTrace(5n, 117n, 19n, 64).squarings + ',' + modpowTrace(5n, 117n, 19n, 64).mults, '6,5', '5^117: six squarings, five set bits');
  eq(modpowTrace(7n, 2n ** 100n, 13n, 64).complete, false, 'a 101-bit exponent is reported as truncated at 64 rows');

  eq(isPrimeBig(2n), true, '2 is prime');
  eq(isPrimeBig(1n), false, '1 is not prime');
  eq(isPrimeBig(101n), true, '101 is prime (lesson 2: four divisions)');
  eq(isPrimeBig(149n), true, '149 is prime (lesson 2 quiz)');
  eq(isPrimeBig(561n), false, '561, a Carmichael number, is composite');
  eq(isPrimeBig(30031n), false, '2·3·5·7·11·13 + 1 is composite');
  eq(factorize(360n).map((pe) => pe.join('^')).join(','), '2^3,3^2,5^1', '360 = 2³·3²·5 (lesson 2 worked example)');
  eq(divisorCount(360n), 24n, '360 has 24 divisors');
  eq(divisorCount(2520n), 48n, '2520 has 48 divisors (lesson 2 standard)');
  eq(factorize(30031n).map((pe) => pe[0]).join(','), '59,509', '30031 = 59 · 509');
  eq(factorize(1071n).map((pe) => pe.join('^')).join(','), '3^2,7^1,17^1', '1071 = 3²·7·17');
  eq(factorize(1n).length, 0, '1 has no prime factors');
  eq(factorize(97n).map((pe) => pe.join('^')).join(','), '97^1', 'a prime is its own factorisation');
  eq(totient(7n), 6n, 'φ(7) = 6');
  eq(totient(9n), 6n, 'φ(9) = 6');
  eq(totient(12n), 4n, 'φ(12) = 4');
  eq(totient(15n), 8n, 'φ(15) = 8 (lesson 11 quiz)');
  eq(totient(35n), 24n, 'φ(35) = 24');
  eq(totient(100n), 40n, 'φ(100) = 40 (lesson 11 worked example)');
  eq(totient(77n), 60n, 'φ(77) = 60 (lesson 11 standard)');
  eq(totient(3120n), 768n, 'φ(3120) = 768');
  eq(totient(26n), 12n, 'φ(26) = 12, the affine multipliers');
  eq(totient(1n), 1n, 'φ(1) = 1');
  eq(modpow(7n, totient(13n), 13n), 1n, 'Fermat at the lesson-11 preset: 7^12 ≡ 1 (mod 13)');
  eq(modpow(2n, totient(4n), 4n), 0n, '2^φ(4) ≡ 0 (mod 4): the theorem needs a coprime base');

  const sun = crtPair(2n, 3n, 3n, 5n);
  eq(sun.x + ' mod ' + sun.lcm, '8 mod 15', 'x ≡ 2 (3), x ≡ 3 (5) gives 8 mod 15 (lesson 10 preset)');
  const sun2 = crtPair(8n, 15n, 2n, 7n);
  eq(sun2.x + ' mod ' + sun2.lcm, '23 mod 105', 'then with x ≡ 2 (7): Sun Tzu\'s 23 mod 105');
  const std = crtPair(crtPair(1n, 5n, 2n, 7n).x, 35n, 3n, 9n);
  eq(std.x + ' mod ' + std.lcm, '156 mod 315', 'the lesson-10 standard: 156 mod 315');
  const bad = crtPair(1n, 4n, 2n, 6n);
  eq(bad.x === null && bad.g === 2n, true, 'x ≡ 1 (4), x ≡ 2 (6) is inconsistent modulo gcd 2');
  const ok = crtPair(1n, 4n, 3n, 6n);
  eq(ok.x + ' mod ' + ok.lcm, '9 mod 12', 'x ≡ 1 (4), x ≡ 3 (6) is 9 modulo the lcm 12, not 24');
  eq(crtPair(1n, 2n, 3n, 4n).x, 3n, 'one modulus dividing the other');
  eq(crtPair(-1n, 4n, 5n, 6n).x, 11n, 'negative remainders are reduced first');
  {
    /* The construction the lab displays for coprime moduli must agree with the
       general solver: Σ aᵢMᵢyᵢ mod M. */
    const M = 15n, t1 = 2n * 5n * modinv(5n, 3n) % M, t2 = 3n * 3n * modinv(3n, 5n) % M;
    eq((t1 + t2) % M, sun.x, 'the displayed construction agrees with crtPair');
  }

  const g1 = lcgRun(5n, 3n, 8n, 0n, 9);
  eq(g1.seq.join(','), '0,3,2,5,4,7,6,1', 'a = 5, c = 3, m = 8 from 0: the lesson-12 body sequence');
  eq(g1.start + ',' + g1.period, '0,8', 'full period 8');
  const g2 = lcgRun(4n, 3n, 8n, 0n, 9);
  eq(g2.seq.join(',') + ' then ' + g2.next, '0,3,7 then 7', 'a = 4 collapses: 0, 3, 7, 7, …');
  eq(g2.start + ',' + g2.period, '2,1', 'period 1 after a tail of 2');
  const g3 = lcgRun(5n, 3n, 16n, 1n, 17);
  eq(g3.seq.join(','), '1,8,11,10,5,12,15,14,9,0,3,2,13,4,7,6', 'the worked example\'s good generator at m = 16');
  eq(g3.period, 16, 'period 16 — every value once');
  const g4 = lcgRun(6n, 3n, 16n, 1n, 17);
  eq(g4.seq.join(',') + ' then ' + g4.next + ',' + g4.period, '1,9 then 9,1', 'a = 6: 1, 9, 9, 9, … period 1');
  eq(hullDobell(5n, 3n, 16n).join(','), 'true,true,true', 'Hull–Dobell passes for (5, 3, 16)');
  eq(hullDobell(6n, 3n, 16n).join(','), 'true,false,false', 'and (6, 3, 16) fails the second and third: 2 ∤ 5 and 4 ∤ 5');
  eq(hullDobell(4n, 3n, 8n).join(','), 'true,false,false', '(4, 3, 8): a − 1 = 3 is divisible by neither 2 nor 4');
  eq(hullDobell(21n, 1n, 100n).join(','), 'true,true,true', '(21, 1, 100) passes: a full-period generator for the standard');
  eq(lcgRun(21n, 1n, 100n, 0n, 101).period, 100, 'and it does have period 100');
  eq(hullDobell(5n, 3n, 7n).join(','), 'true,false,true', 'm = 7: the third condition is vacuous, the second fails');
  eq(lcgRun(5n, 3n, 7n, 0n, 8).period + ',' + lcgRun(5n, 3n, 7n, 1n, 8).period, '6,1',
     'so the period depends on the seed: 6 from 0, and 1 from the fixed point 1');

  const af = affineMap(5n, 8n, 26n);
  eq(af.map[7], 17n, 'H = 7 → 17 = R under (5, 8) (lesson 13 body)');
  eq(af.distinct + ',' + af.inv, '26,21', 'all 26 letters distinct, a⁻¹ = 21');
  eq((((17n - 8n) * 21n) % 26n + 26n) % 26n, 7n, 'D(17) = 21·(17 − 8) ≡ 7 = H');
  const af2 = affineMap(15n, 9n, 26n);
  eq(af2.map[4] + ',' + af2.map[19], '17,8', 'the recovered key (15, 9) sends E → R and T → I (lesson 13 worked example)');
  const af3 = affineMap(3n, 24n, 26n);
  eq(af3.map[4] + ',' + af3.map[19], '10,3', 'the standard\'s key (3, 24) sends E → K and T → D');
  const af13 = affineMap(13n, 0n, 26n);
  eq(af13.distinct + ',' + af13.inv, '2,null', 'a = 13 gives two outputs and no inverse');
  eq(affineMap(2n, 5n, 26n).distinct, 13, 'an even multiplier gives thirteen outputs');
}

// ---------------------------------------------------------------- graphs
console.log('graph algorithms (course 7 workbench)');
{
  /* Every course-7 lesson renders through one workbench, and the panels quote
     what it prints at their presets: distances, visit orders, Kruskal's
     decisions, the clique bound, the planarity counts. The functions below
     are the shipped ones, extracted from graph.py. The case that motivated
     this section: lesson 8's panel promised that BFS and DFS draw different
     trees on a preset that was itself a tree, and nothing could have said so. */
  eval(graphBlock('GRAPH_JS'));
  const L = (a) => a.map((v) => v + 1).join(' ');
  const S = (a) => '{' + L(a) + '}';
  const tree = (parent) => parent.map((p, v) => (p === -1 ? null : (p + 1) + '-' + (v + 1))).filter(Boolean).join(',');
  function load(preset, n) { N = n; useLessonWeights = false; A = PRESETS[preset](n); }
  function custom(n, list) { LESSON = lessonFrom(list); useLessonWeights = true; N = n; A = PRESETS.lesson(n); }
  const degs = () => { const d = []; for (let v = 0; v < N; v += 1) d.push(degree(v)); return d.join(''); };

  load('complete', 5);
  eq(edges().length, 10, 'K5 has 10 edges (lesson 1 preset)');
  eq(degs(), '44444', 'every degree 4');
  load('bipartite', 6);
  eq(edges().length + ',' + degs(), '9,333333', 'K_{3,3}: 9 edges, every degree 3');
  load('cycle', 6);
  eq(edges().length + ',' + degs(), '6,222222', 'C6: 6 edges, every degree 2');

  custom(8, [[1, 2], [1, 3], [1, 5], [2, 4], [2, 6], [3, 4], [3, 7], [4, 8], [5, 6], [5, 7], [6, 8], [7, 8]]);
  eq(degs() + ',' + edges().length, '33333333,12', 'Q3 (lesson 2 preset): eight vertices of degree 3, twelve edges');
  eq(twoColour().conflict, null, 'and Q3 is bipartite');
  eq(hamilton().circuit !== null, true, 'and has a Hamilton circuit');

  load('cycle', 4);
  eq(JSON.stringify(matrixPower(2)), '[[2,0,2,0],[0,2,0,2],[2,0,2,0],[0,2,0,2]]', 'A² of C4 (lesson 3 worked example)');
  eq(matrixPower(3)[0][3] + ',' + triangles(), '4,0', 'A³[1][4] = 4 and no triangle');
  load('petersen', 6);
  eq(triangles() + ',' + edges().length, '2,7', 'two triangles joined: 2 triangles, 7 edges');

  custom(7, [[1, 2], [2, 3], [3, 1], [3, 4], [5, 6]]);
  eq(componentsOf().map(S).join(' '), '{1 2 3 4} {5 6} {7}', 'lesson 4 worked example: three components');
  {
    const c = cuts();
    eq(c.bridges.map((b) => L(b.edge)).join(','), '3 4,5 6', 'bridges 3–4 and 5–6');
    eq(L(c.cutVertices), '3', 'the one cut vertex is 3');
    eq(c.bridges[0].sides.map(S).join(' '), '{1 2 3} {4}', 'removing 3–4 separates {1, 2, 3} from {4}');
    eq(componentsOf(2).length, 4, 'deleting vertex 3 leaves four components');
  }
  load('tree', 7);
  eq(cuts().bridges.length + ',' + L(cuts().cutVertices), '6,1 2 3', 'on the tree preset every edge is a bridge and every internal vertex a cut vertex');
  load('cycle', 6);
  eq(cuts().bridges.length + ',' + cuts().cutVertices.length, '0,0', 'a cycle has no bridge and no cut vertex');

  custom(6, [[1, 2], [2, 3], [3, 1], [4, 5], [5, 6], [6, 4]]);
  eq(degs() + ',' + componentsOf().length, '222222,2', 'two disjoint triangles (lesson 5 preset): 2-regular, two components');
  load('cycle', 6);
  eq(degs() + ',' + componentsOf().length, '222222,1', 'C6: the same degrees, one component');

  load('cycle', 6);
  eq(twoColour().colour.join(''), '010101', 'C6 two-coloured by parity: X = {1, 3, 5}');
  load('cycle', 5);
  eq(L(twoColour().conflict), '3 4', 'C5: the conflict is at vertices 3 and 4 (lesson 6 worked example)');
  load('cycle', 6); link(A, 0, 2);
  eq(twoColour().conflict !== null, true, 'C6 plus the chord 1–3 is not bipartite');
  load('cycle', 6); link(A, 0, 3);
  eq(twoColour().conflict, null, 'C6 plus the chord 1–4 still is');

  load('cycle', 6);
  eq(L(hamilton().circuit), '1 2 3 4 5 6', 'C6 has a Hamilton circuit (lesson 7 preset)');
  A[0][1] = 0; A[1][0] = 0;
  eq(degs().split('').map((d, i) => (d % 2 ? i + 1 : null)).filter(Boolean).join(','), '1,2', 'minus 1–2: the odd vertices are 1 and 2');
  eq(L(hamilton().path) + '|' + hamilton().circuit, '1 6 5 4 3 2|null', 'a Hamilton path and no circuit');

  custom(6, [[1, 2], [1, 3], [2, 4], [3, 4], [4, 5], [5, 6]]);
  {
    const b = bfs(0), d = dfs(0);
    eq(b.dist.join(' '), '0 1 1 2 3 4', 'lesson 8 worked example: BFS distances');
    eq(L(b.order), '1 2 3 4 5 6', 'BFS order');
    eq(tree(b.parent), '1-2,1-3,2-4,4-5,5-6', 'BFS tree edges');
    eq(L(d.order), '1 2 4 3 5 6', 'DFS order');
    eq(tree(d.parent), '1-2,4-3,2-4,4-5,5-6', 'DFS tree edges: 4–3 is a tree edge, so 3–1 is the back edge');
  }
  load('tree', 7);
  eq(tree(bfs(0).parent) === tree(dfs(0).parent), true, 'on a tree BFS and DFS draw the same tree');

  custom(4, [[1, 2, 10], [1, 3, 3], [3, 2, 2], [2, 4, 1], [3, 4, 9]]);
  eq(weight(0, 1) + ',' + weight(1, 2), '10,2', 'the lesson preset carries its own weights');
  {
    const r = dijkstra(0);
    eq(r.dist.join(' '), '0 5 3 6', 'lesson 9 worked example: s = 0, a = 5, b = 3, t = 6');
    let v = 3; const route = []; while (v !== -1) { route.unshift(v); v = r.parent[v]; }
    eq(L(route), '1 3 2 4', 'route s → b → a → t');
    eq(bfs(0).dist[3], 2, 'against a fewest-edge distance of 2');
  }
  useLessonWeights = false;
  eq(weight(0, 1), 5, 'off the lesson preset the formula weight returns');
  load('complete', 6);
  eq(dijkstra(0).dist[5] + ',' + bfs(0).dist[5], '3,1', 'on K6 the cheapest route 1 → 6 is the direct edge');

  custom(6, [[1, 2], [2, 3], [3, 1], [4, 5], [5, 6]]);
  eq(componentsOf().length + ',' + edges().length + ',' + (edges().length === N - componentsOf().length), '2,5,false',
     'lesson 10 graph C: two components, five edges, not acyclic');
  load('path', 6);
  eq(componentsOf().length + ',' + edges().length + ',' + degs(), '1,5,122221', 'graph A is a path with leaves 1 and 6');

  load('tree', 7);
  {
    const o = rootedOrders(0);
    eq(L(o.pre), '1 2 4 5 3 6 7', 'preorder on the tree preset (lesson 11)');
    eq(L(o.ino), '4 2 5 1 6 3 7', 'inorder');
    eq(L(o.post), '4 5 2 6 7 3 1', 'postorder');
    eq(L(o.level), '1 2 3 4 5 6 7', 'level order');
    eq(o.treeEdges + ',' + o.reached, '6,7', 'six tree edges reach all seven');
  }
  load('star', 7);
  eq(rootedOrders(0).ino + ',' + (rootedOrders(0).tooMany + 1), 'null,1', 'on a star inorder is undefined and vertex 1 is why');
  load('cycle', 5);
  eq(L(rootedOrders(0).pre) + ',' + rootedOrders(0).treeEdges, '1 2 3 4 5,4', 'on C5 the orders are those of the DFS spanning tree, one edge left out');

  custom(5, [[1, 2, 1], [2, 3, 2], [3, 4, 3], [4, 5, 4], [1, 5, 5], [1, 3, 6], [2, 4, 7]]);
  {
    const k = kruskal();
    eq(k.total + ',' + k.chosen.length, '10,4', 'lesson 12 worked example: total 10, four edges');
    eq(k.considered.map((c) => L(c[0].slice(0, 2)) + (c[1] ? '+' : '-')).join(','), '1 2+,2 3+,3 4+,4 5+,1 5-,1 3-,2 4-',
       'AB, BC, CD, DE taken; AE, AC, BD rejected, in weight order');
    eq(dijkstra(0).dist[4], 5, 'Dijkstra 1 → 5 on the same graph is the rejected edge of weight 5');
  }
  load('complete', 6);
  eq(kruskal().total + ',' + kruskal().chosen.length, '12,5', 'Kruskal on K6 with the formula weights');
  load('petersen', 6); A[0][3] = 0; A[3][0] = 0;
  eq(kruskal().chosen.length, 4, 'a disconnected graph gives a spanning forest with n − c edges');

  custom(5, [[1, 2], [1, 3], [2, 3], [2, 4], [3, 4], [4, 5]]);
  eq(greedyColour().join(''), '01201', 'lesson 13 worked example: greedy colours 1, 2, 3, 1, 2');
  eq(cliqueNumber().size + ',' + S(cliqueNumber().vertices), '3,{1 2 3}', 'clique number 3 on the triangle');
  eq(Math.max(...degs().split('').map(Number)), 3, 'Δ = 3, so the greedy bound is 4');
  custom(6, [[1, 4], [1, 6], [3, 2], [3, 6], [5, 2], [5, 4]]);
  eq(Math.max(...greedyColour()) + 1 + ',' + twoColour().conflict + ',' + cliqueNumber().size, '3,null,2',
     'the bipartite trap: greedy uses three colours on a bipartite graph');
  load('cycle', 5);
  eq(Math.max(...greedyColour()) + 1 + ',' + cliqueNumber().size, '3,2', 'C5: greedy 3, clique 2, the odd cycle supplies the third');

  load('complete', 5);
  {
    const p = planarity();
    eq(p.verdict + ',' + p.E + ',' + p.bound, 'bound,10,9', 'K5: 10 > 3·5 − 6 = 9 (lesson 14 preset)');
  }
  load('bipartite', 6);
  {
    const p = planarity();
    eq(p.verdict + ',' + p.triangles + ',' + p.bound + ',' + p.bound2, 'bound2,0,12,8', 'K_{3,3}: passes 12, triangle-free, fails 8');
  }
  load('complete', 4);
  eq(planarity().verdict + ',' + planarity().E + ',' + planarity().bound, 'planar,6,6', 'K4: 6 ≤ 6 and planar');
  load('petersen', 6);
  eq(planarity().verdict, 'planar', 'seven edges: no subdivision of K5 or K_{3,3} fits');
  custom(8, [[1, 2], [1, 3], [1, 4], [1, 5], [2, 3], [2, 4], [2, 5], [3, 4], [3, 5], [4, 5]]);
  eq(planarity().verdict + ',' + S(planarity().k5), 'k5,{1 2 3 4 5}', 'K5 on eight vertices passes both bounds and is caught as a subgraph');
  custom(7, [[1, 4], [1, 5], [1, 6], [2, 4], [2, 5], [2, 6], [3, 4], [3, 5], [3, 6]]);
  {
    const p = planarity();
    eq(p.verdict + ',' + S(p.k33.left) + ',' + S(p.k33.right), 'k33,{1 2 3},{4 5 6}', 'K_{3,3} plus an isolated vertex passes 10 and is caught as a subgraph');
  }
  custom(7, [[1, 4], [1, 5], [1, 6], [2, 4], [2, 5], [2, 6], [3, 4], [3, 5], [3, 7], [7, 6]]);
  eq(planarity().verdict, 'open', 'a subdivided K_{3,3} passes the bounds, has no K_{3,3} subgraph, and is reported open, not planar');
  load('cycle', 4); link(A, 0, 2); link(A, 1, 3);
  eq(planarity().verdict + ',' + planarity().triangles, 'planar,4', 'K4 built by hand: four triangles, planar');
}

// ------------------------------------------------------------ algorithms
console.log('algorithm counts and the witness verdict (course 8 lab)');
{
  /* Every course-8 lesson renders through one lab, and its panels quote what
     it prints: comparison counts, the loop-nest sums, the invariant trace,
     the dynamic array's copies, the master theorem's case, the amounts where
     greedy fails. The functions below are the shipped ones, extracted from
     algorithms.py. The case that motivated this section: the witness mode
     searched C ≤ 1000 over n ≤ 64 and reported n² = O(n) with C = 100,
     contradicting the lesson's own example directly above it. */
  eval(algoBlock('ALGO_JS'));
  const F = { one: 0, log: 1, n: 2, nlogn: 3, n2: 4, n3: 5, exp: 6, fact: 7, poly: 8, hundred: 9 };
  const W = (f, g) => { const w = witnessSearch(F[f], F[g], 16); return w ? w.C + ',' + w.k : 'none'; };
  eq(bigO(F.poly, F.n2) + ':' + W('poly', 'n2'), 'true:4,13', '3n² + 5n + 100 = O(n²) with C = 4, k = 13 (lesson 4 preset)');
  eq(bigO(F.n, F.n2) + ':' + W('n', 'n2'), 'true:1,1', 'n = O(n²) with C = 1, k = 1 (lesson 4 quiz)');
  eq(bigO(F.n2, F.n), false, 'n² ≠ O(n) — the lesson 4 example the old search contradicted');
  eq(bigO(F.nlogn, F.n), false, 'n log n ≠ O(n), though a search to n = 10⁹ would find C = 50');
  eq([bigO(F.n3, F.n2), bigO(F.log, F.one), bigO(F.fact, F.exp), bigO(F.exp, F.n3)].join(','), 'false,false,false,false',
     'n³ vs n², log n vs 1, n! vs 2ⁿ, 2ⁿ vs n³ are all false');
  eq(bigO(F.one, F.log) + ':' + W('one', 'log'), 'true:1,2', '1 = O(log n) needs k = 2 because log 1 = 0');
  eq(bigO(F.exp, F.fact) + ':' + W('exp', 'fact'), 'true:1,4', '2ⁿ = O(n!) from n = 4');
  eq(W('n3', 'exp'), '1,10', 'n³ ≤ 2ⁿ from n = 10');
  eq(W('hundred', 'n'), '100,1', '100n = O(n) with C = 100');
  {
    let bad = 0;
    for (let f = 0; f < FUNCS.length; f += 1) for (let g = 0; g < FUNCS.length; g += 1) if (bigO(f, g) && !witnessSearch(f, g, 16)) bad += 1;
    eq(bad, 0, 'every true relation among the ten functions has a witness in the grid');
  }
  eq(ratioAt(F.n2, F.n, 1000000), 1000000, 'the ratio n²/n at 10⁶ is 10⁶ — the disproof column');

  const S = (n, kind) => bubbleSort(makeArray(n, kind)) + ',' + insertionSort(makeArray(n, kind)) + ',' + mergeSort(makeArray(n, kind));
  eq(S(16, 'shuffle'), '120,77,48', 'n = 16 shuffled: bubble 120, insertion 77, merge 48 (lesson 6 worked example)');
  eq(insertionSort(makeArray(16, 'sorted')) + ',' + insertionSort(makeArray(16, 'reverse')), '15,120', 'insertion sort: 15 on sorted, 120 on reversed input');
  eq(S(24, 'shuffle'), '276,174,82', 'n = 24 shuffled');
  eq(S(1000, 'shuffle'), '499500,235149,7387', 'n = 1000: bubble 499 500 = n(n−1)/2, merge 7 387');
  eq(makeArray(16, 'shuffle').join(' '), '8 16 9 2 12 6 3 15 14 1 5 11 10 4 13 7', 'the shuffle is the same permutation for every reader');
  eq(linearSearch(makeArray(16, 'sorted'), 16) + ',' + binaryWorst(16), '16,5', 'linear 16, binary ⌊log₂16⌋ + 1 = 5');
  {
    let ok = true;
    for (let n = 2; n <= 64; n += 1) if (binaryWorst(n) !== ilog2(n) + 1) ok = false;
    eq(ok, true, 'binary search worst case is ⌊log₂ n⌋ + 1 for every n to 64');
  }
  eq(binaryWorst(1000), 10, 'and 10 at n = 1000');

  const nest = countNests(16);
  eq([nest.A, nest.B, nest.C, nest.D].join(','), '4096,136,64,816', 'lesson 5 nests at n = 16: n³, n(n+1)/2, n⌊log₂n⌋, n(n+1)(n+2)/6');
  {
    let ok = true;
    for (let n = 1; n <= 64; n += 1) { const r = countNests(n); if (r.A !== r.predA || r.B !== r.predB || r.C !== r.predC || r.D !== r.predD) ok = false; }
    eq(ok, true, 'every nest equals its formula for every n to 64');
  }

  const p = powerTrace(3, 13);
  eq([p.rows.every((r) => r.ok), p.rows.length, p.squarings, p.mults, p.value].join(','), 'true,5,4,3,1594323',
     'POWER(3, 13): the invariant holds on all five rows, 4 squarings, 3 multiplications, 3¹³ (lesson 2 preset)');
  eq(powerTrace(3, 1000).squarings + ',' + powerTrace(3, 1000).mults, '10,6', 'x¹⁰⁰⁰: 10 squarings and 6 multiplications against 999');
  eq(powerTrace(2, 64).value, 18446744073709551616n, '2⁶⁴ exactly, beyond double precision');

  const d16 = dynamicArray(16, 'double');
  eq([d16.copies, d16.total, d16.worst, d16.worstAt].join(','), '15,31,9,9', 'doubling, 16 inserts: 15 copies, total 31, worst insertion 9 at element 9 (lesson 8 worked example)');
  eq(d16.events.map((e) => e.at + ':' + e.from + '>' + e.to).join(' '), '2:1>2 3:2>4 5:4>8 9:8>16', 'resizes at inserts 2, 3, 5, 9');
  const d17 = dynamicArray(17, 'double');
  eq([d17.copies, d17.total, d17.amortised < 3].join(','), '31,48,true', '17 inserts: total 48, above 2n and still under 3n');
  eq(dynamicArray(16, 'one').copies, 120, 'growing by one copies 1 + ⋯ + 15 = 120');
  {
    let ok = true;
    for (let n = 2; n <= 64; n += 1) if (dynamicArray(n, 'double').amortised >= 3 || dynamicArray(n, 'half').amortised >= 4) ok = false;
    eq(ok, true, 'doubling stays under 3 and ×1.5 under 4 per insertion for every n to 64');
  }

  const M = (a, b, d) => { const m = masterCase(a, b, d); return m.which + ':' + m.result; };
  eq(M(4, 2, 1), '3:Θ(n^2)', 'lesson 7 baseline 4T(n/2) + n: case 3, Θ(n²)');
  eq(M(4, 2, 0), '3:Θ(n^2)', 'faster combining, d = 0: still Θ(n²)');
  eq(M(3, 2, 1), '3:Θ(n^log_2 3) ≈ Θ(n^1.585)', 'one fewer subproblem: Θ(n^1.585)');
  eq(M(9, 3, 2), '2:Θ(n^2 log n)', 'the standard\'s 9T(n/3) + n²: balanced');
  eq([M(2, 2, 1), M(1, 2, 0), M(2, 4, 1), M(7, 2, 2)].join('|'), '2:Θ(n log n)|2:Θ(log n)|1:Θ(n)|3:Θ(n^log_2 7) ≈ Θ(n^2.807)',
     'merge sort, binary search, course 3 lesson 11\'s last row, Strassen');

  eq(greedyFailures([1, 3, 4], 24).join(','), '6,10,14,18,22', 'greedy with {1, 3, 4} fails first at 6 (lesson 9 preset)');
  eq(greedyCoins([1, 3, 4], 6).picks.join('+') + ' vs ' + dpCoins([1, 3, 4], 6).picks.join('+'), '4+1+1 vs 3+3', 'at 6: 4 + 1 + 1 against 3 + 3');
  eq(dpCoins([1, 3, 4], 8).table.join(' '), '0 1 2 1 1 2 2 2 2', 'the lesson 10 table best[0..8]');
  eq(greedyFailures([1, 5, 10, 25], 99).length, 0, 'with {1, 5, 10, 25} greedy is optimal for every amount to 99');
}


// ---------------------------------- capacity, latency, queues and availability
console.log('system design: exact capacity, queueing and availability');
{
  eval(countingBlock('BIGINT_JS') + sysdBlock('HARMONIC_JS') + sysdBlock('RCEIL_JS')
       + sysdBlock('PERCENTILE_JS') + sysdBlock('PMF_JS') + sysdBlock('QUEUE_JS')
       + sysdBlock('SLOTTED_JS') + sysdBlock('TRACE_JS') + sysdBlock('STREAM_JS')
       + sysdBlock('REPLAY_JS') + sysdBlock('AVAIL_JS') + sysdBlock('APPROX_JS'));

  /* Zipf popularity: the cache hit rate is a ratio of harmonics, and it is the
     ratio that makes a small cache of a skewed workload worth having. */
  eq(Rtext(harmonic(4, 1)), '25/12', 'H(4,1) = 1 + 1/2 + 1/3 + 1/4');
  eq(Rtext(harmonic(3, 2)), '49/36', 'H(3,2) = 1 + 1/4 + 1/9');
  eq(Rtext(zipfHit(1, 4, 1)), '12/25', 'the most popular of four keys, s = 1');
  eq(Rtext(zipfHit(4, 4, 1)), '1', 'caching everything hits everything');

  /* Nearest rank, so a percentile is a value some request actually took. */
  eq(percentileRank(10, R(9n, 10n)), 9, 'p90 of ten samples is the 9th');
  eq(percentileRank(10, R(99n, 100n)), 10, 'p99 of ten samples is the 10th, not an interpolation');
  eq(percentileRank(100, R(1n, 2n)), 50, 'p50 of a hundred');
  const lat = [1, 2, 3, 4, 5, 6, 7, 8, 9, 100];
  eq(percentile(lat, R(9n, 10n)), 9, 'the p90 of that sample');
  eq(Rtext(empiricalCdf(lat, 5)), '1/2', 'P(X <= 5)');

  /* A latency budget adds distributions; fan-out takes their maximum. */
  const coin = [[0, R(1n, 2n)], [1, R(1n, 2n)]];
  eq(pmfConvolve(coin, coin).map(p => p[0] + ':' + Rtext(p[1])).join(' '),
     '0:1/4 1:1/2 2:1/4', 'two independent stages add by convolution');
  eq(Rtext(pmfMean(pmfConvolve(coin, coin))), '1', 'and their means add');
  eq(pmfMax(coin, 2).map(p => p[0] + ':' + Rtext(p[1])).join(' '),
     '0:1/4 1:3/4', 'the max of two: the tail is what fan-out costs');
  eq(Rtext(pmfTail(pmfConvolve(coin, coin), 0)), '3/4', 'P(sum > 0)');

  /* M/M/1 from the cut equations. */
  const q = mm1(R(1n, 1n), R(2n, 1n));
  eq(Rtext(q.rho) + ' ' + Rtext(q.L) + ' ' + Rtext(q.W) + ' ' + Rtext(q.Lq),
     '1/2 1 1 1/2', 'M/M/1 at lam = 1, mu = 2');
  eq(mm1(R(3n, 1n), R(2n, 1n)).stable, false, 'rho >= 1 does not settle');
  /* The knee: the last tenth of utilisation costs more than the first nine. */
  eq(Rtext(mm1(R(9n, 10n), R(1n, 1n)).L), '9', 'rho = 0.9 queues 9');
  eq(Rtext(mm1(R(99n, 100n), R(1n, 1n)).L), '99', 'rho = 0.99 queues 99');

  /* Erlang C must agree with M/M/1 at one server -- and s = 1 is exactly the
     case that cannot distinguish a from rho, so s = 2 and 3 are checked too. */
  eq(Rtext(erlangC(R(1n, 1n), R(2n, 1n), 1).pWait), '1/2', 'Erlang C at s = 1 is rho');
  eq(Rtext(erlangC(R(1n, 1n), R(2n, 1n), 1).L), Rtext(q.L), 'and its L is M/M/1 L');
  const e2 = erlangC(R(1n, 1n), R(1n, 1n), 2);
  eq(Rtext(e2.p0) + ' ' + Rtext(e2.pWait) + ' ' + Rtext(e2.L), '1/3 1/3 4/3', 'M/M/2 at a = 1');
  const e3 = erlangC(R(2n, 1n), R(1n, 1n), 3);
  eq(Rtext(e3.p0) + ' ' + Rtext(e3.pWait), '1/9 4/9', 'M/M/3 at a = 2');
  /* Pooling: one queue of two servers beats two queues of one. */
  eq(Rcmp(erlangC(R(1n, 1n), R(1n, 1n), 2).Wq, mm1(R(1n, 2n), R(1n, 1n)).Wq), -1,
     'a pooled M/M/2 waits less than two separate M/M/1s at the same load');

  /* A bounded queue is stable at any load, and Little's law must use the
     EFFECTIVE arrival rate, not the offered one. */
  const fk = mm1k(R(1n, 1n), R(1n, 1n), 3);
  eq(Rtext(fk.blocking), '1/4', 'M/M/1/3 at rho = 1 blocks a quarter');
  eq(Rtext(fk.L), '3/2', 'and holds 3/2 on average');
  eq(Rtext(fk.lamEff), '3/4', 'the effective rate is lam(1 - pK)');

  /* Availability composes three ways, and the three must agree where they meet. */
  eq(Rtext(availSeries([R(9n, 10n), R(9n, 10n)])), '81/100', 'series multiplies down');
  eq(Rtext(availParallel([R(9n, 10n), R(9n, 10n)])), '99/100', 'parallel multiplies up');
  const three = [R(9n, 10n), R(9n, 10n), R(9n, 10n)];
  eq(Rtext(availKofN(R(9n, 10n), 3, 3)), Rtext(availSeries(three)), 'n-of-n is series');
  eq(Rtext(availKofN(R(9n, 10n), 1, 3)), Rtext(availParallel(three)), '1-of-n is parallel');
  eq(Rtext(availKofN(R(1n, 2n), 2, 3)), '1/2', 'majority of three fair coins');
  /* Ten 99.9% dependencies in series are 99.0%, not "as good as the weakest". */
  const ten = []; for (let i = 0; i < 10; i += 1) ten.push(R(999n, 1000n));
  near(Number(Rdec(availSeries(ten), 6)), 0.990045, 1e-6, 'ten 99.9% dependencies give 99.0%');

  /* Retries: the geometric sum, and what it costs when p is high. */
  eq(Rtext(retryAttempts(R(1n, 2n), 2)), '7/4', 'two retries at p = 1/2 cost 7/4 attempts');
  eq(Rtext(retrySuccess(R(1n, 2n), 2)), '7/8', 'and succeed 7/8 of the time');
  eq(Rtext(retryAttempts(R(9n, 10n), 3)), '3439/1000', 'at p = 0.9 the amplification approaches r + 1');

  /* The slotted queue is NOT M/M/1, and this is the assertion that stops a
     lesson claiming the continuous formula is "checked against the simulation".
     At p = 2/5, q = 1/2 the exact slotted mean is 12/5; rho/(1 - rho) is 4. */
  const slot = geoGeo1(R(2n, 5n), R(1n, 2n));
  eq(Rtext(slot.ratio), '2/3', 'Geo/Geo/1 ratio p(1-q)/(q(1-p))');
  eq(Rtext(slot.p0), '1/5', 'and its empty probability');
  eq(Rtext(slot.L), '12/5', 'the EXACT slotted mean');
  eq(Rtext(slot.rho), '4/5', 'at the same utilisation');
  eq(Rtext(mm1(R(4n, 5n), R(1n, 1n)).L), '4', 'where the continuous formula says 4');
  eq(Rcmp(slot.L, mm1(R(4n, 5n), R(1n, 1n)).L), -1,
     'the slotted mean is strictly below M/M/1 -- the two agree only in the limit');
  /* A second point with q != 1/2. At q = 1/2, (1 - q) = q and the ratio
     p(1-q)/(q(1-p)) is indistinguishable from pq/(q(1-p)) -- so one point
     cannot check the formula at all. */
  const slot2 = geoGeo1(R(1n, 4n), R(1n, 3n));
  eq(Rtext(slot2.ratio), '2/3', 'Geo/Geo/1 ratio at p = 1/4, q = 1/3');
  eq(Rtext(slot2.p0) + ' ' + Rtext(slot2.L), '1/4 9/4', 'its empty probability and exact mean');
  eq(Rtext(mm1(R(3n, 4n), R(1n, 1n)).L), '3', 'against 3 from the continuous formula');

  /* Little's Law as an identity about a trace, which is how it is proved here.
     Three customers, each in the system 2 slots, over a horizon of 6:
     area 6, L = 1, lambda = 1/2, W = 2, and L = lambda*W exactly. */
  const tr = littleFromTrace([0, 2, 4], [2, 4, 6]);
  eq(Rtext(tr.L) + ' ' + Rtext(tr.lambda) + ' ' + Rtext(tr.W), '1 1/2 2', 'L, lambda, W from the trace');
  eq(Rtext(tr.L), Rtext(Rmul(tr.lambda, tr.W)), 'L = lambda * W, exactly, with no model');
  eq(occupancyTrace([0, 2, 4], [2, 4, 6], 6).join(''), '111111', 'N(t) is 1 throughout');
  /* The same three customers, arriving together instead of spread out: the same
     total time in system over a third of the horizon, so L triples and W does
     not move. That is the identity doing work. */
  const tr2 = littleFromTrace([0, 0, 0], [2, 2, 2]);
  eq(Rtext(tr2.L) + ' ' + Rtext(tr2.W), '3 2', 'stacked arrivals triple L and leave W alone');
  eq(Rtext(tr2.L), Rtext(Rmul(tr2.lambda, tr2.W)), 'and the identity still holds');

  /* A seeded stream: same seed, same values, or a reader cannot check a lab. */
  eq(lcgStream(1103515245, 12345, 2147483648, 1, 3).join(','),
     '1103527590,377401575,662824084', 'the stream is these values, not merely repeatable');
  eq(lcgStream(1103515245, 12345, 2147483648, 1, 3).join(','),
     lcgStream(1103515245, 12345, 2147483648, 1, 3).join(','), 'and the same on a second call');
  const fair = [[1, R(1n, 2n)], [2, R(1n, 2n)]];
  eq(sampleFromPmf(fair, R(1n, 4n)), 1, 'inverse transform below the first mass');
  eq(sampleFromPmf(fair, R(3n, 4n)), 2, 'and above it');
  /* The boundary: u exactly at the cumulative mass. Half-open [lo, hi) is what
     keeps the sampler's frequencies equal to the pmf, so u = 1/2 is the SECOND
     value, and a <= here would bias every sampled distribution low. */
  eq(sampleFromPmf(fair, R(1n, 2n)), 2, 'u exactly on the boundary falls to the second value');
  eq(sampleFromPmf(fair, R(0n, 1n)), 1, 'and u = 0 to the first');

  /* Ceiling and floor, because 3.2 machines is four. */
  eq(Rceil(R(16n, 5n)), 4n, 'ceil(3.2) = 4 -- the sizing answer');
  eq(Rfloor(R(16n, 5n)), 3n, 'floor(3.2) = 3');
  eq(Rceil(R(4n, 1n)), 4n, 'an exact integer does not round up');
  eq(Rfloor(R(-16n, 5n)), -4n, 'floor of a negative goes down, not toward zero');
  eq(Rceil(R(-16n, 5n)), -3n, 'and ceil goes up');
  /* The case the sign guard exists for: an EXACT negative integer must not be
     pushed a further step. Without it -4 floors to -5. */
  eq(Rfloor(R(-4n, 1n)), -4n, 'floor of an exact negative integer is itself');
  eq(Rceil(R(-4n, 1n)), -4n, 'and so is its ceiling');

  /* Replacement policies on a trace, and the bound the lesson rests on.
     Trace A B C A B D A B C D, three slots. */
  const tr3 = ['A','B','C','A','B','D','A','B','C','D'];
  const opt = replayPolicy(tr3, 3, 'opt'), lru = replayPolicy(tr3, 3, 'lru');
  /* Exact rates, not merely an ordering: "OPT >= LRU" holds for several WRONG
     policies too, including one that evicts the nearest-future key. */
  eq(Rtext(opt.rate), '1/2', 'farthest-in-future gets 5 of 10');
  eq(Rtext(lru.rate), '2/5', 'LRU gets 4');
  eq(Rcmp(opt.rate, lru.rate) > 0, true, 'and the bound is strict on this trace');
  eq(replayPolicy(tr3, 10, 'lru').misses, 4, 'a cache big enough misses only the compulsory four');
  eq(Rtext(replayPolicy(['A','A','A','A'], 1, 'lru').rate), '3/4', 'one key, one slot');

  /* The four places this subject rounds, and only these. */
  near(expNegApprox(1, 1e-15), Math.exp(-1), 1e-12, 'e^-1 by series');
  near(expNegApprox(5, 1e-15), Math.exp(-5), 1e-12, 'e^-5 by series');
  /* The arguments that expose a cancelling implementation. Summing the
     ALTERNATING series for e^-x is exact at 1 and 5 -- which is why the first
     version of this test passed -- and then 0.4% out at 17, 173% out at 20, and
     NEGATIVE past 21. A probability cannot be negative, so these are pinned by
     relative error rather than absolute, at arguments where the absolute error
     of a badly wrong answer is still tiny. */
  for (const x of [10, 12, 15, 17, 20, 21, 25, 40]) {
    const got = expNegApprox(x, 1e-15), want = Math.exp(-x);
    eq(got > 0, true, 'e^-' + x + ' is positive');
    eq(Math.abs(got - want) / want < 1e-10, true,
       'e^-' + x + ' is right to a relative 1e-10, not merely a small absolute error');
  }
  near(expNegApprox(-2, 1e-15), Math.exp(2), 1e-10, 'a negative argument gives e^|x|');
  near(standardErrorApprox(0.5, 100), 0.05, 1e-12, 'the standard error of a proportion');
  /* 1.44*log2(1/0.01) = 9.57 bits per key is the canonical 1% figure, and the
     rate it actually delivers at k = 7 is what the lesson quotes. */
  near(bloomApprox(9585, 1000, 7), 0.01004, 1e-4, 'a Bloom filter at 9.585 bits per key is ~1%');
  /* 9.585, not the 9.57 a textbook quotes: that figure uses 1.44 in place of
     1/ln2 = 1.4427. The lesson should give the exact form and note the rounding. */
  near(bitsPerKeyApprox(0.01), 9.585, 0.001, '1% costs 9.585 bits per key');
  near(sqrtApprox(R(2n, 1n), 1e-15), Math.SQRT2, 1e-12, 'a root that rounds, and says so');
  near(sqrtApprox(R(9n, 4n), 1e-15), 1.5, 1e-12, 'agreeing with Rsqrt where Rsqrt is exact');
  near(harmonicApprox(1000000, 1), 14.392727, 1e-4, 'the Zipf normaliser past where exact is readable');
}

// ------------------------------------- system design C2: latency and the tail
/* The `latency` kit's own arithmetic, on the numbers its eleven lessons print.
   Every assertion below is a figure that appears on a page, so a change that
   moves one of them is a change to what a lesson claims. */
console.log('system design: latency, percentiles and the tail');
{
  eval(block('RATIONAL_JS') + sysdBlock('RCEIL_JS') + sysdBlock('PERCENTILE_JS')
       + sysdBlock('PMF_JS') + sysdBlock('APPROX_JS') + latencyBlock('LATENCY_JS'));

  /* Rfixed exists because Rdec cannot do this. 0.999^693 has a 2079-digit
     numerator; Number() of it is Infinity and Infinity/Infinity is NaN, so the
     fan-out lesson at p99.9 would print NaN. Long division in BigInt instead. */
  eq(Rfixed(R(1n, 3n), 6), '0.333333', 'a third to six places');
  eq(Rfixed(R(2n, 3n), 6), '0.666667', 'two thirds, rounded half up at the last digit');
  eq(Rfixed(R(-1n, 8n), 3), '-0.125', 'a negative rational keeps its sign');
  eq(Rfixed(R(7n, 1n), 0), '7', 'no places asked for, no decimal point');
  eq(Rfixed(Rpow(R(999n, 1000n), 693), 6), '0.499900', '0.999^693, which Number cannot hold');
  eq(String(Number(Rpow(R(999n, 1000n), 693).n)), 'Infinity', 'and this is why Rdec would give NaN');
  eq(Rpct(R(1n, 400n), 4), '0.2500%', 'a probability as a percentage');

  /* L1 and L3: the two terms, and the size at which they cross. */
  eq(Rtext(transferMs(64000, 100)), '128/25', '64 kB over 100 Mbit/s is 5.12 ms');
  eq(Rtext(bdpBytes(100, 80)), '1000000', '100 Mbit/s x 80 ms holds exactly one megabyte');
  eq(Rtext(linkTimeMs(5, 80, 14000, 10)), '2056/5', '5 round trips at 80 ms plus 14 kB at 10 Mbit/s');
  eq(Rtext(crossoverBytes(5, 80, 10)), '500000', 'the bytes catch 5 round trips at 500 kB');
  /* The crossover for ONE round trip IS the bandwidth-delay product -- L1 and
     L3 are the same fact, and if these ever disagree one of the two is wrong. */
  eq(Rtext(crossoverBytes(1, 80, 100)), Rtext(bdpBytes(100, 80)), 'k = 1 crossover is the BDP');

  /* L2: the floor. c is exact by definition, so this is an exact fraction. */
  eq(Rtext(lightFloorMs(5585)), '8377500000/149896229', 'New York to London, exactly');
  eq(Rfixed(lightFloorMs(5585), 3), '55.889', 'which is the 56 ms the course quotes');
  eq(Rfixed(unexplainedMs(76, 5585), 3), '20.111', 'a measured 76 ms leaves 20 ms to explain');
  eq(Rcmp(unexplainedMs(40, 5585), R(0n, 1n)) < 0, true, 'a measurement under the floor goes negative');

  /* L4: the longest path, its slack, and the two edges the lesson toggles. */
  const dagT = [4, 18, 6, 22, 55, 12, 3];
  const dagE = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 4], [3, 5], [4, 5], [5, 6]];
  const base = dagSchedule(dagT, dagE);
  eq(base.length, 92, 'the critical path is 92 ms, not the 120 ms the stages total');
  eq(base.slack.join(','), '0,0,12,33,0,0,0', 'cache has 12 ms spare and enrich 33');
  eq(base.path.join('-'), '0-1-4-5-6', 'gateway, authz, db, render, respond');
  /* Speeding up an off-path stage changes nothing: enrich to 1 ms is still 92. */
  eq(dagSchedule([4, 18, 6, 1, 55, 12, 3], dagE).length, 92, 'making enrich instant saves nothing');
  eq(dagSchedule([4, 18, 6, 22, 55, 12, 2], dagE).length, 91, 'a critical stage saves its whole millisecond');
  /* Serialising the cache behind authz puts it ON the path and costs 6 ms. */
  const serial = dagSchedule(dagT, dagE.concat([[1, 2]]));
  eq(serial.length + ' ' + serial.slack[2], '98 0', 'authz -> cache moves cache onto the path');
  /* Making the db wait for the enrichment costs the whole 22 ms of it. */
  const after = dagSchedule(dagT, dagE.concat([[3, 4]]));
  eq(after.length + ' ' + after.path.join('-'), '114 0-1-3-4-5-6', 'enrich -> db reroutes the path');

  /* L5: the rank, the value it selects, and the mean that is neither. */
  const s5 = parseSample('12, 13, 14, 14, 15, 15, 16, 17, 18, 19, 21, 22, 24, 27, 31, 38, 52, 96, 180, 420');
  eq(s5.length, 20, 'twenty measurements');
  eq(percentile(s5, R(1n, 2n)) + ' ' + percentile(s5, R(95n, 100n)) + ' ' + percentile(s5, R(99n, 100n)),
     '19 180 420', 'p50, p95 and p99 by nearest rank');
  eq(Rtext(sampleMean(s5)), '266/5', 'the mean is 53.2 ms');
  eq(countBelow(s5, sampleMean(s5)), 17, '17 of 20 requests are faster than the average');
  /* Nothing in the sample IS the mean, which is the lesson. */
  eq(s5.indexOf(53), -1, 'and no request took 53 ms');
  eq(parseSample('   '), 'null', 'an empty sample is refused rather than guessed at');

  /* L6: p^n, the break-even n, and the same number from pmfMax. */
  eq(Rfixed(Rpow(R(99n, 100n), 69), 6), '0.499837', '0.99^69 is just under a half');
  eq(fanoutBreakEven(R(99n, 100n), 20000), 69, 'a p99 becomes the median at a fan-out of 69');
  eq(fanoutBreakEven(R(9n, 10n), 20000), 7, 'a p90 at 7');
  eq(fanoutBreakEven(R(19n, 20n), 20000), 14, 'a p95 at 14');
  eq(fanoutBreakEven(R(999n, 1000n), 20000), 693, 'and a p99.9 at 693');
  /* 68 must NOT be the answer: at n = 68 the probability is still above a half,
     and an off-by-one here is the whole content of the lesson. */
  eq(Rcmp(Rpow(R(99n, 100n), 68), R(1n, 2n)) > 0, true, '68 calls are still better than even');
  const twoWay = pmfMax([[0, R(99n, 100n)], [1, R(1n, 100n)]], 69);
  eq(Rtext(twoWay[0][1]), Rtext(Rpow(R(99n, 100n), 69)), 'pmfMax agrees with p^n exactly');

  /* L7: the hedge. The preset is 100 measured calls as run lengths. */
  const hSpec = parsePmfSpec('10:40, 12:25, 15:15, 20:10, 30:5, 50:3, 120:1, 300:1');
  const hPmf = pmfFromSpec(hSpec);
  eq(expandSpec(hSpec).length, 100, 'the run lengths expand to a hundred calls');
  eq(pmfPercentile(hPmf, R(99n, 100n)) + ' ' + pmfPercentile(hPmf, R(95n, 100n))
     + ' ' + pmfPercentile(hPmf, R(1n, 2n)), '120 30 12', 'p99, p95 and p50 of the service');
  eq(Rtext(hedgeLoad(hPmf, 30)), '1/20', 'a hedge at the p95 costs 5% more traffic');
  eq(Rtext(Rpow(hedgeLoad(hPmf, 30), 2)), '1/400', 'and the tail past it is that squared');
  eq(Rtext(hedgedTail(hPmf, 30, 42)), '7/400', 'P(hedged > 42) = P(X > 42) P(X > 12)');
  eq(hedgedQuantile(hPmf, 30, R(99n, 100n)), 45, 'the hedged p99 is 45 ms, down from 120');
  eq(hedgedQuantile(hPmf, 30, R(1n, 2n)), 12, 'and the median does not move');
  /* Hedging at the median doubles the load, which is the misconception. */
  eq(Rtext(hedgeLoad(hPmf, 12)), '7/20', 'hedging at the p50 sends a backup for a third of requests');

  /* L8: percentiles do not add. Two stages, seven atoms each. */
  const A = pmfFromSpec(parsePmfSpec('4:520, 6:250, 9:120, 14:60, 22:30, 38:16, 70:4'));
  const B = pmfFromSpec(parsePmfSpec('12:420, 17:300, 24:150, 34:80, 48:36, 72:12, 130:2'));
  const S = pmfNormalise(pmfConvolve(A, B));
  const q99 = R(99n, 100n);
  eq(pmfPercentile(A, q99) + ' ' + pmfPercentile(B, q99), '38 72', 'each stage has its own p99');
  eq(pmfPercentile(S, q99), 78, 'the SUM has a p99 of 78 ms');
  eq(pmfPercentile(A, q99) + pmfPercentile(B, q99), 110, 'while the two p99s add to 110');
  eq(pmfPercentile(S, q99) < pmfPercentile(A, q99) + pmfPercentile(B, q99), true,
     'p99(A + B) < p99(A) + p99(B) on these distributions');
  /* Means DO add, exactly -- the contrast the lesson is built on. */
  eq(Rtext(pmfMean(A)) + ' ' + Rtext(pmfMean(B)) + ' ' + Rtext(pmfMean(S)),
     '881/125 2414/125 659/25', 'the two means and the sum of the two stages');
  eq(Rtext(Radd(pmfMean(A), pmfMean(B))), Rtext(pmfMean(S)), 'expectation is linear; percentiles are not');
  eq(S.length, 43, '43 attainable totals from 7 x 7 pairs');
  eq(Rtext(pmfCdfAt(S, 78)), '3096/3125', 'the cumulative at 78 ms, exactly');
  eq(Rcmp(pmfCdfAt(S, 78), q99) >= 0, true, 'which does reach 99/100');
  eq(Rcmp(pmfCdfAt(S, 77), q99) < 0, true, 'while the atom below it does not -- so 78 is the rank');
  eq(parsePmfSpec('4:520, oops'), 'null', 'an unreadable stage is refused, not half-parsed');
  eq(parsePmfSpec('4:0'), 'null', 'and a zero weight is not a distribution');

  /* L9: the budget, allocated backwards from a 400 ms SLO. */
  const plan = budgetPlan(400, 208, [8, 20, 150, 40]);
  eq(Rtext(plan.avail) + ' ' + Rtext(plan.share), '192 48', '192 ms left, 48 ms each on an even split');
  eq(Rtext(plan.residual), '-26', 'the plan is 26 ms short');
  eq(plan.rows.map(function (r) { return r.fits ? 'y' : 'n'; }).join(''), 'yyny', 'search is the stage that cannot fit');
  eq(Rtext(plan.rows[2].residual), '-102', 'by 102 ms');
  eq(Rtext(plan.spare) + ' ' + Rtext(plan.need), '76 102', 'the others release 76 ms against a need of 102');
  eq(plan.balanced, true, 'and the residual balances both ways of counting it');
  /* Raise the SLO until it fits, and the two ways of counting still agree. */
  const roomy = budgetPlan(500, 208, [8, 20, 150, 40]);
  eq(Rtext(roomy.residual) + ' ' + roomy.balanced, '74 true', 'at a 500 ms SLO the plan fits');

  /* L10: the timeout, the retries and the calls it kills. */
  const tSpec = parsePmfSpec('8:45, 11:25, 16:15, 24:8, 45:4, 90:2, 400:1');
  const tSample = expandSpec(tSpec);
  eq(tSample.length, 100, 'a hundred measured calls');
  eq(Rtext(worstCaseMs(90, 1)), '180', 'one retry at a 90 ms timeout is 180 ms worst case');
  eq(Rtext(killFraction(tSample, 90)), '1/100', 'a timeout at the p99 kills one call in a hundred');
  eq(Rtext(allAttemptsLost(R(1n, 100n), 1)), '1/10000', 'and both attempts fail once in ten thousand');
  eq(Rtext(sampleMean(tSample)), '1827/100', 'the mean of that sample is 18.27 ms');
  /* The misconception, priced: a timeout at the mean throws away 15% of calls
     that were going to succeed. */
  eq(Rtext(killFraction(tSample, 18)), '3/20', 'a timeout at the mean kills 15% of good calls');
  eq(Rtext(killFraction(tSample, 400)), '0', 'a timeout past the maximum kills none');

  /* L11: the one rounded figure on the course, and the reason it rounds. */
  near(mathisMbitsApprox(1460, 100, R(1n, 100n)), 1.168, 1e-9, '1% loss at 100 ms bounds a flow at 1.168 Mbit/s');
  eq(streamsToFillApprox(10000, mathisMbitsApprox(1460, 100, R(1n, 100n))), 8562,
     'so 8562 streams are needed to fill a 10 Gbit/s link');
  /* Halving the loss multiplies the bound by sqrt(2), not by 2 -- the whole
     shape of the result is in that square root. */
  near(mathisMbitsApprox(1460, 100, R(1n, 200n)) / mathisMbitsApprox(1460, 100, R(1n, 100n)),
       Math.SQRT2, 1e-9, 'halving the loss buys a factor of sqrt 2');
  eq(Rsqrt(R(1n, 50n)), 'null', 'and 2% loss has no rational root at all, which is why sqrtApprox is used');
  near(mathisMbitsApprox(1460, 100, R(1n, 50n)), 0.826, 1e-3,
       'and twice the loss is not half the bound: 2% gives 0.826, not 0.584');
}


// ------------------------------------------- capacity estimation (kit: estimate)
/* The arithmetic of System Design course 1. Every case below is a claim some
   lesson on that course makes out loud, so a failure here is a page asserting
   something false, not a style regression. */
console.log('capacity estimation: intervals, unit chains, series and ceilings');
{
  eval(countingBlock('BIGINT_JS') + sysdBlock('RCEIL_JS') + sysdBlock('APPROX_JS')
       + estimateBlock('ESTIMATE_JS'));

  /* Printing an exact rational at a size that defeats Rdec. This is not
     cosmetic: Rdec goes through Number(n)/Number(d), and the storage mode
     routinely holds 10^15 over 10^72. */
  eq(Rround(R(1n, 3n), 4), '0.3333', 'a third to four places');
  eq(Rround(R(2n, 3n), 4), '0.6667', 'two thirds rounds up, not down');
  eq(Rround(R(1n, 2n), 0), '1', 'a half rounds half-up at zero places');
  eq(Rround(R(-1n, 3n), 3), '-0.333', 'and the sign survives');
  eq(Rround(R(10n ** 24n + 1n, 1n), 0), '1000000000000000000000001',
     '10^24 + 1 exactly, where a double would have said 1e+24');
  eq(Number(Rdec(R(10n ** 24n + 1n, 1n))) === 1e24, true,
     'which is exactly what Rdec does say, and why Rround exists');
  eq(groupDec('1234567.89'), '1 234 567.89', 'grouping stops at the decimal point');
  eq(groupDec('-1000'), '-1 000', 'and does not eat the sign');
  eq(showR(R(1234567n, 100n), 1), '12 345.7', 'a figure as a capacity page shows it');
  eq(Rtextg(R(100000n, 1n)), '100 000', 'an exact ratio, grouped');
  eq(Rtextg(R(125n, 108n)), '125/108', 'a small fraction is left alone');
  eq(powTen(5) + ' ' + powTen(-3), '10⁵ 10⁻³', 'decades read as decades');

  /* Widths in powers of ten: an exact integer search, and its rounded gloss. */
  eq(decadeBracket(R(64n, 1n)), 1, '64 is between 10^1 and 10^2');
  eq(decadeBracket(R(1n, 1n)), 0, '1 sits in decade 0');
  eq(decadeBracket(R(1000n, 1n)), 3, 'an exact power belongs to its own decade, not the one below');
  eq(decadeBracket(R(1n, 1000n)), -3, 'and a thousandth to -3');
  eq(decadeBracket(R(999n, 1000n)), -1, 'just under 1 is decade -1');
  near(log10Approx(R(1000n, 1n)), 3, 1e-12, 'log10 of a thousand');
  near(log10Approx(R(64n, 1n)), 1.80617997, 1e-6, 'log10 of the width three doubling factors give');
  /* The case Rnum cannot do: both ends past 2^53, the ratio small. */
  near(log10Approx(Rdiv(R(10n ** 40n, 1n), R(10n ** 37n, 1n))), 3, 1e-9,
       'a ratio of two numbers a double cannot hold');
  near(ratioApprox(R(3n * 10n ** 40n, 1n), R(10n ** 40n, 1n)), 3, 1e-9,
       'and the same ratio as a Number, for pixels');

  /* L1. Three factors at a factor of two: the product is at a factor of EIGHT,
     the interval is 64x end to end, and the arithmetic midpoint is four times
     the estimate -- which is the misconception the lesson names. */
  const C = [R(10000000n, 1n), R(100n, 1n), R(1000n, 1n)];
  const two = [R(2n, 1n), R(2n, 1n), R(2n, 1n)];
  const iv = productInterval(C, two, two);
  eq(Rtext(iv.centre), '1000000000000', 'the product of the central values');
  eq(Rtext(iv.lo) + ' ' + Rtext(iv.hi), '125000000000 8000000000000', 'the product interval');
  eq(Rtext(iv.down) + ' ' + Rtext(iv.up), '8 8', 'three half-widths of 2 multiply to 8, not to 6');
  eq(Rtext(iv.ratio), '64', 'and end to end the interval is 64x');
  eq(Rtext(Rdiv(arithMid(iv.lo, iv.hi), iv.centre)), '65/16',
     'the arithmetic midpoint is 65/16 of the estimate: it is dragged to the high end');
  eq(Rtext(geoMeanExact(iv.lo, iv.hi)), '1000000000000',
     'the geometric centre of a symmetric interval IS the product of the centres, exactly');
  /* Asymmetric: the root is irrational, so the page must round and say so. */
  const skew = productInterval(C, two, [R(2n, 1n), R(3n, 1n), R(2n, 1n)]);
  eq(Rtext(skew.up), '12', 'one factor skewed high widens only the high end');
  eq(geoMeanExact(skew.lo, skew.hi), 'null', 'and its geometric centre is not rational');
  near(geoMeanApprox(skew.lo, skew.hi), Math.sqrt(1.5) * 1e12, 1e4,
       'so it is computed by the rounded root, which is sqrt(3/2) x the centre');
  /* A factor known exactly contributes nothing to the width. */
  const one3 = [R(1n, 1n), R(1n, 1n), R(1n, 1n)];
  eq(Rtext(productInterval(C, one3, one3).ratio), '1', 'three exact factors give a point, not an interval');

  /* L2. 86400 against 10^5, in both directions -- the lesson's own numbers. */
  eq(Rtext(rpsExact(R(10000000n, 1n), R(100n, 1n))), '312500/27', '10M users x 100 actions a day, per second');
  eq(Rtext(rpsRounded(R(10000000n, 1n), R(100n, 1n))), '10000', 'and with the 10^5-second day');
  eq(Rtext(dayLengthRatio()), '125/108', 'the shortcut day is 125/108 of a real one');
  eq(Rtext(rateShortfallRatio()), '108/125', 'so the rate it gives is 108/125 of the truth');
  eq(Rtext(Rdiv(rpsExact(R(7n, 1n), R(13n, 1n)), rpsRounded(R(7n, 1n), R(13n, 1n)))), '125/108',
     'and the ratio does not depend on the volume, which is why it is quotable');
  eq(Rtrim(Rround(Rmul(Rsub(dayLengthRatio(), R(1n, 1n)), R(100n, 1n)), 2)), '15.74',
     'the 15.7% the lesson quotes is the DAY being long');
  eq(Rtext(Rmul(Rsub(R(1n, 1n), rateShortfallRatio()), R(100n, 1n))), '68/5',
     'the rate is low by 13.6%, which is a different number and the reader will confuse them');
  /* Turning it back: rate x 86400 must return the daily volume it came from. */
  eq(Rtext(Rmul(rpsExact(R(10000000n, 1n), R(100n, 1n)), R(86400n, 1n))), '1000000000',
     'the chain read upward returns where it started');

  /* L3. 100:1 is 1/101, not 1%. */
  const sp = splitRates(R(10000n, 1n), R(100n, 1n));
  eq(Rtext(sp.writeShare), '1/101', 'a 100:1 read/write ratio makes writes one part in 101');
  eq(Rtext(sp.readShare), '100/101', 'and reads the other hundred');
  eq(Rtext(Radd(sp.readShare, sp.writeShare)), '1', 'the two shares are a partition');
  eq(Rtext(sp.naiveWriteShare), '1/100', 'the instinct says 1/100');
  eq(Requ(sp.writeShare, sp.naiveWriteShare), false, 'which is not the same number');
  eq(Rtext(sp.naiveOver), '101/100', 'and overstates the write rate by exactly (r+1)/r');
  eq(Rtext(sp.writes) + ' ' + Rtext(sp.reads), '10000/101 1000000/101', 'the two rates, exactly');
  eq(Rtext(Radd(sp.writes, sp.reads)), '10000', 'and they add back to the total');
  eq(Rtext(splitRates(R(2n, 1n), R(1n, 1n)).writeShare), '1/2', '1:1 is half and half');

  /* L5. Bits, bytes, and the header that is charged once per request. */
  eq(Rtext(bandwidthMbit(R(2000n, 1n), R(1000n, 1n), R(200n, 1n))), '96/5',
     '2000 req/s of 1200 B is 19.2 Mbit/s');
  eq(Rtrim(Rround(bandwidthMbit(R(2000n, 1n), R(1000n, 1n), R(200n, 1n)), 2)), '19.2', 'read as a decimal');
  eq(Rtext(Rdiv(bandwidthMbit(R(2000n, 1n), R(1000n, 1n), R(200n, 1n)),
                bandwidthNoEight(R(2000n, 1n), R(1000n, 1n), R(200n, 1n)))), '8',
     'forgetting the factor of 8 is out by exactly 8, at every rate and every size');
  eq(Rtext(headerShare(R(1000n, 1n), R(200n, 1n))), '1/6', 'headers are a sixth of a 1 kB request');
  eq(Rtext(headerShare(R(200n, 1n), R(200n, 1n))), '1/2',
     'and half of one whose payload equals the header');
  eq(Rtext(headerCrossover(R(200n, 1n))), '200', 'which is why the crossover payload IS the header size');
  eq(Rcmp(headerShare(R(199n, 1n), R(200n, 1n)), R(1n, 2n)) > 0, true, 'below it they are the majority');

  /* L4. Storage as a series, with growth compounding once a month. */
  const gb500 = R(500n * 10n ** 9n, 1n);
  const terms = growthTerms(gb500, 90, R(5n, 100n));
  eq(terms.length, 3, '90 days is three monthly blocks');
  eq(terms.map(function (t) { return t.days; }).join(','), '30,30,30', 'each of them full');
  eq(Rtext(terms[2].rate), '551250000000', 'by the third month the daily ingest has compounded twice');
  eq(Rtext(terms[2].running), '47287500000000', 'and 47.2875 TB has accumulated');
  eq(Rtext(storageGrowth(gb500, 90, R(5n, 100n), 3)), '141862500000000', 'three copies of it');
  eq(Rtext(storageFlat(gb500, 90, 3)), '135000000000000', 'against 135 TB if ingest never grew');
  /* The invariant that catches an off-by-one in the block loop. */
  eq(Rtext(storageGrowth(gb500, 90, R(0n, 1n), 3)), Rtext(storageFlat(gb500, 90, 3)),
     'at zero growth the geometric series IS the arithmetic one');
  eq(Rtext(storageGrowth(gb500, 1, R(5n, 100n), 1)), Rtext(gb500), 'one day is one day of ingest');
  /* A part-month: 45 days is 30 at the first rate and 15 at the second. */
  const part = growthTerms(R(10n, 1n), 45, R(1n, 10n));
  eq(part.map(function (t) { return t.days; }).join(','), '30,15', 'the last block is short');
  eq(Rtext(part[1].rate), '11', 'and runs at the compounded rate');
  eq(Rtext(part[1].running), '465', '30x10 + 15x11');

  /* L6. The ratio between two rungs, exactly. */
  eq(Rtext(rungRatio(10000000, 100)), '100000',
     '10^5 main-memory references fit inside one disk seek -- the lesson’s headline');
  eq(Rtext(rungRatio(150000000, 1)), '150000000', 'and the whole ruler spans that from L1');
  eq(Rtext(rungRatio(4, 3)), '4/3', 'two rungs that do not divide stay a fraction');

  /* L7. Twenty-four buckets, a peak, a mean, and their ratio. */
  eq(profileWeights('flat', 12, 5).join(','), new Array(24).fill(10).join(','),
     'a flat profile is flat whatever the amplitude');
  const office = profileWeights('office', 21, 6);
  eq(office[21], 46, 'the busy hour carries 10 + 6x6');
  eq(office.reduce(function (a, b) { return a + b; }, 0), 456, 'and the day totals 456 weight');
  eq(office[9], 10, 'twelve hours away the profile is back at the floor');
  const spike = profileWeights('spike', 19, 10);
  eq(spike[19] + ',' + spike[18] + ',' + spike[20], '130,10,10', 'a spike is one bucket and nothing else');
  let shapeThrew = false;
  try { profileWeights('nonesuch', 0, 1); } catch (e) { shapeThrew = true; }
  eq(shapeThrew, true, 'an unknown profile shape raises rather than quietly going flat');
  const buckets = office.map(function (w) { return R(BigInt(w) * 1000000n, 1n); });
  const ps = peakStats(buckets);
  eq(ps.peakHour, 21, 'the peak is where the shape put it');
  eq(Rtext(ps.total), '456000000', 'the day’s total');
  eq(Rtext(ps.peakRps), '115000/9', 'peak requests a second');
  eq(Rtext(ps.meanRps), '47500/9', 'mean requests a second');
  eq(Rtext(ps.ratio), '46/19', 'peak over mean is 24 x the busiest bucket over the total, exactly');
  eq(Rtext(peakStats(new Array(24).fill(R(7n, 1n))).ratio), '1',
     'and a day with no shape at all has a multiplier of 1, which is the sanity check');

  /* L8. The ceiling, and the headroom named rather than assumed. */
  const mc = machineCount(R(20000n, 1n), R(40n, 1n), 8, R(60n, 100n));
  eq(Rtext(mc.capacity), '200', 'one 8-core machine at 40 ms a request serves 200 req/s');
  eq(Rtext(mc.usable), '120', 'of which 60% may be used');
  eq(Rtext(mc.exact), '500/3', 'so the fleet needs 500/3 machines');
  eq(mc.n, 167n, 'and machines are integers, so N = 167');
  eq(mc.nFull, 100n, 'sizing at 100% would have said 100');
  eq(Rtext(mc.spare), '13400', 'N leaves 13 400 req/s of headroom');
  eq(Rtext(Rmul(mc.utilisation, R(100n, 1n))), '10000/167',
     'the peak then sits at 10000/167 % of the fleet, which is 59.88');
  eq(Rtrim(Rround(Rmul(mc.utilisation, R(100n, 1n)), 2)), '59.88', 'read as a percentage');
  /* The ceiling must not round a whole number up: that is the off-by-one that
     buys a machine nobody needs, on every page that sizes anything. */
  eq(machineCount(R(24000n, 1n), R(40n, 1n), 8, R(60n, 100n)).n, 200n,
     'an exact 200 machines is 200, not 201');
  eq(machineCount(R(1n, 1n), R(40n, 1n), 8, R(60n, 100n)).n, 1n, 'and any positive load needs at least one');

  /* L9. The working set, and the inverse that the whole lesson rests on. */
  const hot = R(1n, 10n), share = R(9n, 10n);
  eq(Rtext(workingSetFraction(hot, share, R(8n, 10n))), '4/45',
     '80% of the hits from a tenth of the data that takes 90% of the reads');
  eq(Rtext(workingSetFraction(R(5n, 100n), R(75n, 100n), R(95n, 100n))), '81/100',
     'and 95% costs 81% of the data once the target is past the knee');
  eq(Rtext(hitRateAt(hot, share, hot)), '9/10', 'caching exactly the hot region gets exactly its share');
  eq(Rtext(hitRateAt(hot, share, R(1n, 1n))), '1', 'caching everything hits everything');
  eq(Rtext(hitRateAt(hot, share, R(0n, 1n))), '0', 'caching nothing hits nothing');
  eq(Rtext(workingSetFraction(hot, share, R(1n, 1n))), '1', 'and a 100% target needs all of it');
  /* Inverse, at ten targets either side of the knee. A sizing lesson whose
     curve and whose inverse disagree is giving the reader a number that its own
     graph contradicts. */
  let inverseOk = true;
  for (let t = 1; t <= 10; t += 1) {
    const target = R(BigInt(t), 10n);
    if (!Requ(hitRateAt(hot, share, workingSetFraction(hot, share, target)), target)) inverseOk = false;
  }
  eq(inverseOk, true, 'the memory a target needs, put back into the curve, returns that target');
  eq(Rtext(workingSetBytes(R(5n * 10n ** 12n, 1n), hot, share, R(8n, 10n))), '4000000000000/9',
     '5 TB, a tenth hot, 80% wanted: 444.4 GB');
  /* No skew at all: caching x of the data buys x of the hits, which is the
     "caching is not worth it here" case the lesson needs to be able to show. */
  eq(Rtext(workingSetFraction(R(1n, 2n), R(1n, 2n), R(9n, 10n))), '9/10',
     'with no skew the cache must hold as much as the hit rate you want');

  /* L10. Two routes, their ratio, the band, and the shared factor. */
  const routeA = [R(500000n, 1n), R(20n, 1n), R(2000000n, 1n)];
  const routeB = [R(10000000n, 1n), R(1800000n, 1n)];
  eq(Rtext(routeProduct(routeA)), '20000000000000', 'route A');
  eq(Rtext(routeProduct(routeB)), '18000000000000', 'route B');
  eq(Rtext(routeRatio(routeProduct(routeA), routeProduct(routeB))), '10/9', 'and the ratio between them');
  eq(Rtext(routeProduct([])), '1', 'an empty chain is the empty product');
  eq(withinBand(R(10n, 9n), R(8n, 1n)), true, '10/9 is inside a band of 8');
  eq(withinBand(R(9n, 10n), R(8n, 1n)), true, 'and so is its reciprocal');
  eq(withinBand(R(9n, 1n), R(8n, 1n)), false, 'nine is outside');
  /* The direction a naive check gets wrong: a ratio far BELOW 1 is just as much
     a disagreement as one far above, and "ratio < k" alone would pass it. */
  eq(withinBand(R(1n, 9n), R(8n, 1n)), false, 'and so is a ninth');
  eq(withinBand(R(1n, 1n), R(1n, 1n)), true, 'a band of 1 admits only exact agreement');
  eq(sharedFactors(['users', 'sessions', 'bytes'], [R(5n), R(3n), R(7n)],
                   ['rows', 'bytes'], [R(9n), R(7n)]).join(','), 'bytes',
     'a factor in both chains with the same value is shared');
  eq(sharedFactors(['bytes'], [R(7n)], ['bytes'], [R(8n)]).length, 0,
     'the same NAME at a different value is not: route B measured it for itself');
  eq(sharedFactors(['bytes'], [R(7n)], ['rows'], [R(7n)]).length, 0,
     'and a coincidence of value under another name is not either');

  /* Units and the slider ladder. */
  eq(fmtBytes(R(1500n, 1n), 2), '1.5 kB', 'kB is 1000 B, decimal, as a disk is sold');
  eq(fmtBytes(R(999n, 1n), 2), '999 B', 'and below that it stays bytes');
  eq(fmtBytes(R(47287500000000n, 1n), 2), '47.29 TB', 'the storage lesson’s own total');
  eq(fmtBytes(R(10n ** 15n, 1n), 2), '1 PB', 'and a petabyte is a petabyte');
  eq(Rtext(ladderValue(0)) + ' ' + Rtext(ladderValue(1)) + ' ' + Rtext(ladderValue(6)), '1 3/2 10',
     'the 1, 1.5, 2, 3, 5, 7 ladder, one rung per decade step');
  eq(Rtext(ladderValue(ladderIndex(0, 7))), '10000000', '10 million is a rung, so lesson 1 can open on it');
  eq(Rtext(ladderValue(ladderIndex(2, 6))), '2000000', 'and so is 2 MB');
}

// ------------------------------------------- caching and hit rates (kit: cache)
/* The `cache` kit's own arithmetic, on the numbers its ten lessons print.
   Every assertion below is a figure that appears on a page, so a change that
   moves one of them is a change to what a lesson claims.

   Three of them are not figures but PINS. The stepper this kit uses to show a
   policy's cache contents duplicates the eviction rules of the core's
   replayPolicy, which is the tested one, so it is checked against it on every
   trace and every size below; the byte hit rate is checked against zipfHit at
   the shifted exponent it must equal; and the phase-averaged TTL simulation is
   checked against the closed form it is meant to confirm. A duplicated rule
   that nothing compares is a rule that has already drifted. */
console.log('system design: caching, skew, replacement and staleness');
{
  const CACHE_SOURCE = path.join(__dirname, 'mathpath', 'labs', 'cache.py');
  const cacheSrc = fs.readFileSync(CACHE_SOURCE, 'utf8');
  const cacheBlock = (name) => blockFrom(cacheSrc, name, CACHE_SOURCE);
  eval(block('RATIONAL_JS') + sysdBlock('RCEIL_JS') + sysdBlock('HARMONIC_JS')
       + sysdBlock('QUEUE_JS') + sysdBlock('REPLAY_JS') + sysdBlock('APPROX_JS')
       + cacheBlock('CACHE_JS'));

  /* --- printing. Rnum goes through Number and this course overflows it. --- */
  eq(Rshow(R(1n, 3n), 3), '0.333', 'long division in BigInt');
  eq(Rshow(R(2n, 3n), 3), '0.667', 'rounded half up at the last digit');
  eq(Rshow(R(1n, 2n), 0), '1', 'and half rounds up, not to even');
  eq(Rshow(R(-1n, 3n), 3), '-0.333', 'the sign survives the division');
  /* The reason Rshow exists: a byte weight over fifty ranks leaves a double. */
  eq(Rnum(R(10n ** 400n + 1n, 3n * 10n ** 400n)), NaN, 'Rnum of a 400-digit ratio is NaN');
  eq(Rshow(R(10n ** 400n + 1n, 3n * 10n ** 400n), 4), '0.3333', 'Rshow of the same is a third');
  eq(Rpercent(R(1n, 3n), 2), '33.33%', 'a percentage of an exact probability');
  eq(groupNum(1234567), '1 234 567', 'digit grouping');
  eq(bytesText(1500), '1.50 kB', 'a kB is 1000 B: egress is billed in decimal units');
  eq(bytesText(40000000000n), '40.00 GB', 'and so is a GB');
  eq(moneyText(R(2400000n, 1n)), '$24 000.00', 'cents to dollars');

  /* --- L1: the backend sees the miss rate ---------------------------------
     The lesson's whole claim is the ratio: 90% to 99% is a tenfold cut, and
     99% to 99.9% is another one. Asserting the two loads alone would not
     catch a formula that had (1 - h) right and lambda wrong. */
  eq(Rtext(backendRate(R(10000n, 1n), R(9n, 10n))), '1000', '10k rps at 90% leaves 1000');
  eq(Rtext(backendRate(R(10000n, 1n), R(99n, 100n))), '100', 'and at 99%, 100');
  eq(Rtext(backendRho(R(10000n, 1n), R(9n, 10n), R(2000n, 1n))), '1/2', 'the backend sits at rho = 1/2');
  eq(Rtext(missMultiple(R(9n, 10n), R(99n, 100n))), '10', '90% to 99% divides the load by 10');
  eq(Rtext(missMultiple(R(99n, 100n), R(999n, 1000n))), '10', 'and 99% to 99.9% by 10 again');
  eq(missMultiple(R(9n, 10n), R(1n, 1n)), null, 'a perfect cache has no ratio, and says so');

  /* --- L2: an expectation, and a percentile that steps --------------------- */
  eq(Rtext(meanLatency(R(19n, 20n), R(1n, 1n), R(40n, 1n))), '59/20', 'the lesson mean, 2.95 ms');
  eq(Rtext(latencyQuantile(R(19n, 20n), R(1n, 1n), R(40n, 1n), R(1n, 2n))), '1', 'the p50 is a hit');
  eq(Rtext(latencyQuantile(R(19n, 20n), R(1n, 1n), R(40n, 1n), R(99n, 100n))), '40',
     'at h = 95% the p99 is the MISS latency -- the misconception, refuted');
  eq(Rtext(latencyQuantile(R(99n, 100n), R(1n, 1n), R(40n, 1n), R(99n, 100n))), '1',
     'and it flips exactly at h = q, not gradually');
  eq(Rtext(latencyQuantile(R(9899n, 10000n), R(1n, 1n), R(40n, 1n), R(99n, 100n))), '40',
     'one ten-thousandth below q and it is the miss latency again');

  /* --- L3, L4: Zipf, exactly ---------------------------------------------- */
  eq(Rtext(rankTerm(2, 3)) + ' ' + Rtext(rankTerm(2, -3)) + ' ' + Rtext(rankTerm(5, 0)), '8 1/8 1',
     'i^e for e positive, negative and zero');
  eq(Rtext(zipfProb(1, 4, 1)), '12/25', 'the most popular of four keys at s = 1');
  eq(Rtext(zipfShare(4, 20, 1, 50).exact), '6466460/11167027',
     'the top 4 of 20 at s = 1 -- the L3 worked example, exactly');
  eq(zipfShare(4, 20, 1, 50).rounded, false, 'and it is not rounded');
  eq(Rtext(zipfHit(4, 20, 0)), '1/5', 's = 0 IS uniform popularity: 20% of the keys, 20% of the hits');
  eq(Rtext(zipfShare(0, 20, 1, 50).exact) + ' ' + Rtext(zipfShare(25, 20, 1, 50).exact), '0 1',
     'an empty cache hits nothing and a complete one hits everything');
  /* Past the limit the page must ROUND and must say so. A silent switch would
     print an approximation in the shape of an exact fraction. */
  eq(zipfShare(20, 200, 1, 50).rounded, true, 'past N = 50 the share is rounded');
  eq(zipfShare(20, 200, 1, 50).exact, null, 'and there is no exact fraction to offer');
  near(zipfShare(20, 200, 1, 50).value, 0.612101, 1e-5, 'the rounded value at N = 200');
  /* Sizing: the C a target costs, and the diminishing returns that follow. */
  eq(sizeForTarget(50, 2, R(9n, 10n)), 5, 'at N = 50, s = 2, ninety per cent costs 5 keys');
  eq(sizeForTarget(50, 2, R(99n, 100n)), 28, 'and ninety-nine per cent costs 28 -- the next nine');
  eq(sizeForTarget(20, 0, R(1n, 2n)), 10, 'under uniform popularity it IS proportional: half for half');
  eq(JSON.stringify(sizeTarget(200, 1, R(9n, 10n), 50)), '{"c":111,"rounded":true}',
     'past the limit the search rounds, and reports that it did');
  eq(hitCurve(4, 1, 50).join(' '), '0.48 0.72 0.88 1', 'h(C) for C = 1..4 at N = 4, s = 1');

  /* --- L10: the byte hit rate is a different number ------------------------
     It is the same harmonic ratio at exponent s - b, so the two must agree
     wherever both are defined. That identity is the assertion: it catches a
     sign error in the exponent, which no single value would. */
  eq(Rtext(byteWeight(20, 1, 0)), Rtext(harmonic(20, 1)), 'at b = 0 the byte weight IS the harmonic');
  eq(Rtext(byteHit(4, 20, 1, 0)), Rtext(zipfHit(4, 20, 1)),
     'so at b = 0 the byte hit rate IS the request hit rate -- the control');
  eq(Rtext(byteHit(4, 20, 2, 1)), Rtext(zipfHit(4, 20, 1)), 'and in general it is zipfHit at s - b');
  eq(Rtext(byteHit(4, 20, 1, 1)), '1/5',
     'at b = s it collapses to C/N: 57.9% of the requests, 20% of the bytes');
  eq(Rtext(byteHit(2, 4, 1, 2)), '3/10', 'b > s is allowed, and harmonicApprox could not compute it');
  near(byteHitApprox(4, 20, 1, 1), 0.2, 1e-12, 'the rounded path agrees with the exact one');
  eq(Rtext(objectBytes(3, 1, 100000)), '300000', 'rank 3 at b = 1 is three times the base size');
  eq(Rtext(egressCost(R(40000n * 1000000000n, 1n), R(2n, 1n), 30)), '2400000',
     '40 TB a day at 2c/GB is $24 000 a month');

  /* --- L5: replacement, and the bound the lesson rests on ------------------ */
  const T1 = parseTrace('A B C A B D A B C D');
  eq(T1.join(''), 'ABCABDABCD', 'the course trace parses');
  eq(parseTrace('a,b--c  A!!b').join('|'), 'A|B|C|A|B', 'any separator, and case folds');
  eq(traceKeys(T1).join(''), 'ABCD', 'four distinct keys, in first-use order');
  eq(Rtext(replayTrace(T1, 3, 'opt').rate), '1/2', 'farthest-in-future gets 5 of 10');
  eq(Rtext(replayTrace(T1, 3, 'lru').rate), '2/5', 'LRU gets 4');
  eq(Rtext(replayTrace(T1, 3, 'fifo').rate), '1/5', 'FIFO gets 2');
  /* THE PIN. The stepper duplicates the core's eviction rules so that it can
     report cache contents; if the two ever disagree the page is showing one
     run and counting another. Checked on five traces at six sizes. */
  {
    let mismatches = 0;
    const traces = [T1, parseTrace('1 2 3 4 1 2 5 1 2 3 4 5'), parseTrace('A A A B C B C B C'),
                    parseTrace('A B C D E A B C D E A B'), parseTrace('A')];
    for (const t of traces) {
      for (let k = 1; k <= 6; k += 1) {
        for (const p of ['fifo', 'lru', 'opt']) {
          if (replayTrace(t, k, p).hits !== replayPolicy(t, k, p).hits) mismatches += 1;
        }
      }
    }
    eq(mismatches, 0, 'the kit stepper agrees with the core replay on every trace, size and policy');
  }
  /* LFU is the one policy the core does not implement, so it needs a trace
     that separates it from the two it would otherwise be mistaken for. On
     A A A B C B C B C at two slots it keeps the stale hot key and gets 2
     where FIFO, LRU and OPT all get 6. */
  const T2 = parseTrace('A A A B C B C B C');
  eq(replayTrace(T2, 2, 'lfu').hits, 2, 'LFU holds the once-hot key and thrashes on the rest');
  eq(replayTrace(T2, 2, 'lru').hits, 6, 'LRU lets it go');
  eq(replayTrace(T2, 2, 'fifo').hits, 6, 'so does FIFO');
  eq(replayTrace(T2, 2, 'opt').hits, 6, 'and the bound is 6 as well, so LFU is losing 4 hits');
  /* An unknown policy must throw. The core silently treats one as FIFO, which
     would show a FIFO run under an LFU heading. */
  {
    let threw = false;
    try { replayTrace(T1, 3, 'random'); } catch (err) { threw = true; }
    eq(threw, true, 'an unknown policy throws rather than quietly becoming FIFO');
  }
  /* Belady's anomaly, measured. FIFO misses 9 times with three slots and 10
     with four; LRU and OPT are stack algorithms and never rise. */
  const BEL = parseTrace('1 2 3 4 1 2 5 1 2 3 4 5');
  eq(missBySize(BEL, 'fifo', 6).join(','), '12,12,9,10,5,5', 'FIFO misses against cache size');
  eq(missBySize(BEL, 'lru', 6).join(','), '12,12,10,8,5,5', 'LRU never rises');
  eq(missBySize(BEL, 'opt', 6).join(','), '12,9,7,6,5,5', 'nor does the bound');
  eq(JSON.stringify(firstAnomaly(BEL, 'fifo', 6)), '{"k":3,"up":4,"from":9,"to":10}',
     "Belady's anomaly, found rather than asserted");
  eq(firstAnomaly(BEL, 'lru', 6), null, 'and LRU has none');
  eq(firstAnomaly(BEL, 'opt', 6), null, 'and neither has OPT');
  eq(firstAnomaly(T1, 'fifo', 6), null, 'the course trace does not show one, which is why the kit ships both');

  /* --- L6: TTL and staleness ---------------------------------------------- */
  eq(Rtext(staleFraction(R(10n, 1n), R(60n, 1n))), '1/12', 'T/(2U) below U');
  eq(Rtext(staleFraction(R(120n, 1n), R(60n, 1n))), '3/4', '1 - U/(2T) above it');
  eq(Rtext(staleFraction(R(60n, 1n), R(60n, 1n))), '1/2', 'and the two branches meet at T = U');
  eq(Rtext(ttlMissRate(R(5n, 1n), R(10n, 1n))), '1/50', 'a 10 s TTL at 5 reads/s misses 2%');
  eq(Rtext(ttlMissRate(R(5n, 1n), R(1n, 10n))), '1',
     'a TTL shorter than the gap between reads misses everything, and the rate caps at 1');
  /* The boundary the simulation turns on: a refresh at the same instant as an
     update picks up the NEW value, so the next update is strictly after. */
  eq(Rtext(nextUpdateAfter(R(0n, 1n), R(0n, 1n), R(60n, 1n))), '60',
     'an update at the refresh instant does not make the copy stale');
  eq(Rtext(nextUpdateAfter(R(0n, 1n), R(10n, 1n), R(60n, 1n))), '10', 'the next one does');
  /* THE SECOND PIN: the phase-averaged simulation must reproduce the closed
     form it is printed beside, or the page is showing two models. */
  eq(Rtext(staleRun(R(10n, 1n), R(60n, 1n), R(15n, 1n), 24).fraction), '1/12', 'one run at one phase');
  eq(Rtext(staleAverage(R(10n, 1n), R(60n, 1n), 24, 24)), Rtext(staleFraction(R(10n, 1n), R(60n, 1n))),
     'and 24 midpoint phases reproduce T/(2U) exactly');
  eq(Rtext(staleAverage(R(120n, 1n), R(60n, 1n), 24, 2)), Rtext(staleFraction(R(120n, 1n), R(60n, 1n))),
     'the same on the other branch');
  eq(Rtext(staleAverage(R(25n, 1n), R(60n, 1n), 24, 10)), '5/24',
     'and with T not dividing U it still lands on the formula');

  /* --- L7: the stampede ---------------------------------------------------- */
  eq(Rtext(stampedeSize(R(500n, 1n), R(40n, 1n))), '20', 'lambda*d: 500 rps through a 40 ms window');
  eq(Rtext(stampedeSize(R(500n, 1n), R(1n, 1n))), '1/2', 'a 1 ms window lets half a request through');
  eq(String(stampedeCount(R(500n, 1n), R(1n, 1n))), '1', 'which the backend counts as one');
  eq(Rtext(stampedeTotal(R(500n, 1n), R(40n, 1n), 10)), '200', 'ten hot keys expiring together');

  /* --- L8: write-through against write-back -------------------------------- */
  const W = parseTrace('A B A C A B A D A B');
  eq(distinctPerWindow(W, 5).map((x) => x.distinct).join(','), '3,3', 'three distinct keys per flush');
  eq(coalescing(W, 5).writes + ' ' + coalescing(W, 5).distinct + ' ' + Rtext(coalescing(W, 5).ratio),
     '10 6 5/3', 'ten writes become six, a ratio of 5/3');
  eq(coalescing(W, 5).peak, 3, 'and the largest dirty set is three keys');
  eq(Rtext(coalescing(W, 1).ratio), '1', 'flushing every write coalesces nothing');
  eq(Rtext(coalescing(W, 99).ratio), '5/2', 'and one flush for the whole trace coalesces most');
  eq(Rtext(bytesAtRisk(3, 4000)), '12000', 'three 4 kB keys is 12 kB at risk');

  /* --- L9: the second level is conditional --------------------------------- */
  eq(Rtext(globalHit(R(4n, 5n), R(1n, 2n))), '9/10', '80% then half the rest is 90%, not 130%');
  eq(Rtext(globalMiss(R(4n, 5n), R(1n, 2n))), '1/10', 'the global miss is the PRODUCT');
  eq(Rtext(Radd(globalHit(R(4n, 5n), R(1n, 2n)), globalMiss(R(4n, 5n), R(1n, 2n)))), '1',
     'and the two account for everything');
  eq(Rtext(levelLatency(R(4n, 5n), R(1n, 2n), R(1n, 1n), R(5n, 1n), R(50n, 1n))), '7',
     't1 + (1-h1)(t2 + (1-h2)t3) = 7 ms');
  eq(Rtext(naiveSumHit(R(4n, 5n), R(1n, 2n))), '13/10',
     'adding the rates gives 130%, which is how you know it is the wrong operation');
  eq(Rtext(conditionalShare(R(4n, 5n), R(1n, 2n))), '1/10',
     "L2's measured 50% is 10% of all requests, not 50%");
}

// ------------------------------- system design C3: queues and utilisation
/* The `queue` kit's own arithmetic, on the numbers its thirteen lessons print.

   The block this section exists for is the Geo/Geo/1 convergence. A slotted
   simulation is NOT M/M/1 at finite slot size, and a lesson that says its
   formula is "checked against the simulation" is comparing two models. The
   assertions below pin the exact discrete mean at three slot sizes and the rate
   at which it approaches the continuous one, so a change that quietly restores
   the false claim fails here rather than on the page. */
console.log('system design: queues, Little\'s Law and the slotted chain');
{
  const QUEUE_SOURCE = path.join(__dirname, 'mathpath', 'labs', 'queue.py');
  const queueSrc = fs.readFileSync(QUEUE_SOURCE, 'utf8');
  const queueBlock = (name) => blockFrom(queueSrc, name, QUEUE_SOURCE);
  eval(block('RATIONAL_JS') + countingBlock('BIGINT_JS') + sysdBlock('RCEIL_JS')
       + sysdBlock('QUEUE_JS') + sysdBlock('SLOTTED_JS') + sysdBlock('TRACE_JS')
       + sysdBlock('STREAM_JS') + sysdBlock('APPROX_JS') + queueBlock('QUEUE_KIT_JS'));

  /* --- L1: mu is a rate ------------------------------------------------- */
  eq(Rtext(muFromServiceMs(1)), '1000', 'a 1 ms service is 1000 per second, not 1');
  eq(Rtext(muFromServiceMs(4)), '250', 'a 4 ms service is 250 per second');
  eq(Rtext(serviceMsFromMu(muFromServiceMs(4))), '4', 'and back again');
  eq(Rtext(Rdiv(R(800n, 1n), muFromServiceMs(1))), '4/5', 'rho = lambda/mu at the lesson preset');
  eq(Rtext(growthPerSec(R(1200n, 1n), muFromServiceMs(1))), '200', 'above rho = 1 the backlog grows at lambda - mu');
  eq(Rtext(backlogAfter(R(1200n, 1n), muFromServiceMs(1), 60)), '12000', 'a minute of that is 12 000 waiting');
  eq(Rtext(backlogAfter(R(800n, 1n), muFromServiceMs(1), 60)), '0', 'and below rho = 1 nothing accumulates');

  /* --- L2: Little's Law inside a window ---------------------------------- */
  /* The lesson's trace: five customers over ten slots, area 17. */
  const A = [0, 1, 2, 5, 6], D = [3, 4, 6, 8, 10];
  const w10 = littleWindow(A, D, 10);
  eq(w10.area + ' ' + w10.arrived + ' ' + w10.done + ' ' + w10.inflight, '17 5 5 0', 'the whole trace, counted');
  eq(Rtext(w10.L) + ' ' + Rtext(w10.lambda) + ' ' + Rtext(w10.W), '17/10 1/2 17/5', 'L, lambda and W over it');
  eq(Rtext(w10.lamW), Rtext(w10.L), 'and lambda*W IS L, with no model assumed');
  eq(w10.holds, true, 'the identity holds on a window everyone has left');
  eq(occupancyTrace(A, D, 10).join(''), '1232122211', 'the N(t) staircase the area is under');
  eq(Rtext(littleFromTrace(A, D).L), Rtext(w10.L), 'and the core agrees at the full horizon');
  /* Cut the window short and it stops holding -- which is the misconception,
     and the assertion that keeps the lab honest about WHY. */
  const w8 = littleWindow(A, D, 8);
  eq(w8.inflight, 1, 'at T = 8 one customer is still in the system');
  eq(Rtext(w8.L) + ' vs ' + Rtext(w8.lamW), '15/8 vs 65/32', 'so L and lambda*W part company');
  eq(w8.holds, false, 'the law did not fail; the window did');

  /* --- L3: the same identity, solved three ways -------------------------- */
  eq(Rtext(littleSolve('L', R(1n, 2n), R(4n, 1n))), '2', 'L = lambda*W');
  eq(Rtext(littleSolve('W', R(2n, 1n), R(1n, 2n))), '4', 'W = L/lambda');
  eq(Rtext(littleSolve('lambda', R(2n, 1n), R(4n, 1n))), '1/2', 'lambda = L/W');
  /* The unit trap the lesson is about: 500/s at 40 ms is 20, not 20 000. */
  eq(Rtext(poolForRate(R(500n, 1n), R(40n, 1n))), '20', '500 per second at 40 ms needs 20 connections');
  eq(Rtext(poolCapPerSec(20, R(40n, 1n))), '500', 'and 20 connections at 40 ms cap at 500 per second');
  eq(Rtext(poolForRate(poolCapPerSec(20, R(40n, 1n)), R(40n, 1n))), '20', 'the two are inverses');

  /* --- L4, L7: the slotted chain, which is the point of this section ------ */
  /* The closed form the kit's docstring states, checked against the core's
     geoGeo1 at four points. One point would not do it: at q = 1/2 several wrong
     formulas coincide with the right one. */
  function closed(p, q) {
    const rho = Rdiv(p, q);
    return Rdiv(Rmul(rho, Rsub(R(1n, 1n), p)), Rsub(R(1n, 1n), rho));
  }
  const pts = [[2, 5, 1, 2], [4, 5, 1, 1], [1, 4, 1, 3], [2, 25, 1, 10]];
  pts.forEach(function (t) {
    const p = R(BigInt(t[0]), BigInt(t[1])), q = R(BigInt(t[2]), BigInt(t[3]));
    eq(Rtext(geoGeo1(p, q).L), Rtext(closed(p, q)),
       'Geo/Geo/1 L = rho(1-p)/(1-rho) at p = ' + Rtext(p) + ', q = ' + Rtext(q));
    eq(Rtext(geoGeo1(p, q).p0), Rtext(Rsub(R(1n, 1n), Rdiv(p, q))),
       'and its empty probability is 1 - rho at p = ' + Rtext(p));
  });
  /* The convergence panel L7 ships, exactly. At lambda = 4/5, mu = 1 the
     largest legal slot is 1, and each tenth of it closes the gap by a factor of
     ten -- linear in Delta, because the gap is rho*p/(1 - rho) and p = lambda*Delta. */
  eq(Rtext(largestLegalSlot(R(4n, 5n), R(1n, 1n))), '1', 'the largest slot where lambda*D and mu*D are probabilities');
  eq(Rtext(largestLegalSlot(R(1n, 1n), R(2n, 1n))), '1/2', 'and it is set by whichever rate is larger');
  const conv = convergenceRows(R(4n, 5n), R(1n, 1n), 3);
  eq(conv.map(r => Rtext(r.delta) + ':' + Rtext(r.L)).join(' '),
     '1:4/5 1/10:92/25 1/100:496/125', 'the exact slotted mean at Delta = 1, 1/10, 1/100');
  eq(conv.map(r => Rtext(r.gap)).join(' '), '16/5 8/25 4/125',
     'and the shortfall against rho/(1-rho), falling by exactly ten each step');
  eq(Rtext(Rdiv(conv[0].gap, conv[1].gap)) + ' ' + Rtext(Rdiv(conv[1].gap, conv[2].gap)), '10 10',
     'exactly ten, because the gap is linear in the slot');
  eq(Rtext(mm1(R(4n, 5n), R(1n, 1n)).L), '4', 'while the continuous formula says 4 at every slot size');
  eq(Rtext(slottedMean(R(4n, 5n), R(1n, 1n), R(1n, 2n))), '12/5',
     'and at Delta = 1/2 the slotted mean is the docstring\'s 12/5, not 4');
  /* A slot too big is not a small error, it is not a model: p must be a
     probability, and the panel must refuse rather than print a number. */
  eq(slottedMean(R(2n, 1n), R(3n, 1n), R(1n, 1n)), 'null', 'lambda*Delta > 1 is not a Bernoulli slot');
  eq(slottedMean(R(1n, 2n), R(3n, 1n), R(1n, 1n)), 'null', 'nor is mu*Delta > 1');
  /* Lq = L - rho, because exactly rho of the time there is one in service. */
  eq(Rtext(geoGeo1Lq(R(2n, 5n), R(1n, 2n))), '8/5', 'the slotted Lq is L - rho');
  eq(Rtext(slottedCa2(R(2n, 5n))) + ' ' + Rtext(slottedCs2(R(1n, 2n))), '3/5 1/2',
     'and the chain\'s own coefficients of variation are 1 - p and 1 - q');

  /* --- L4: the simulation must match the chain it claims to be ----------- */
  const p25 = R(2n, 5n), q12 = R(1n, 2n);
  eq(drawBelow(0, 100, R(2n, 5n)), true, 'a draw at 0 is below any positive probability');
  eq(drawBelow(39, 100, R(2n, 5n)), true, 'and 39/100 is below 2/5');
  eq(drawBelow(40, 100, R(2n, 5n)), false, 'while 40/100 is NOT -- the boundary is half-open, or every rate is biased high');
  eq(slottedRun(p25, q12, 7, 12).join(''), slottedRun(p25, q12, 7, 12).join(''), 'the same seed gives the same run');
  eq(slottedRun(p25, q12, 7, 12).join('') === slottedRun(p25, q12, 8, 12).join(''), false,
     'and a different seed does not');
  /* 40 000 slots, warm-up discarded: the measured mean must land near 12/5. A
     loose tolerance, because this asserts the SIMULATOR implements the chain,
     not that a finite sample equals its mean. */
  const longRun = slottedRun(p25, q12, 11, 40000);
  near(Number(Rdec(runMean(longRun, 4000), 6)), 2.4, 0.12, 'a long slotted run converges on the chain\'s exact 12/5');
  eq(Rtext(runMean([0, 1, 2, 3], 0)) + ' ' + Rtext(runMean([0, 1, 2, 3], 2)), '3/2 5/2', 'the mean, and the mean after a warm-up');
  eq(queueOf([0, 1, 2, 3]).join(''), '0012', 'those waiting is N - 1, floored at zero');
  eq(runMax([0, 3, 1]), 3, 'and the peak of a run');
  /* D/D/1 at the same rho: never a queue, and the mean IS rho. That is lesson
     4's whole claim, and it is exact rather than measured. */
  eq(Rtext(runMean(ddRun(5, 4, 4000), 0)), '4/5', 'clockwork arrivals at rho = 4/5 hold exactly 4/5');
  eq(runMax(ddRun(5, 4, 4000)), 1, 'and never more than the one in service -- nothing ever waits');
  eq(runMax(ddRun(4, 1, 100)), 1, 'the same at a light load');
  /* Deterministic service, same arrival stream: it must wait LESS than
     geometric service at the same rho, which is lesson 9 seen from lesson 4. */
  eq(Rcmp(runMean(queueOf(slottedDetRun(p25, 2, 11, 40000)), 4000),
          runMean(queueOf(slottedRun(p25, q12, 11, 40000)), 4000)) < 0, true,
     'fixed service waits less than geometric service on the same arrivals');
  /* The initial transient: E[N] over an ensemble starts low and climbs. This is
     the assertion behind the sentence "the simulation starts empty". */
  const curve = transientCurve(p25, q12, 1, 24, 160);
  eq(Rtext(curve[0]) === '0' || Rcmp(curve[0], R(1n, 1n)) < 0, true, 'the ensemble starts near empty');
  eq(Rcmp(curveMean(curve, 0, 20), curveMean(curve, 80, 160)) < 0, true,
     'and the early mean is BELOW the late one -- the bias a warm-up removes');
  eq(runningMeans([1, 1, 1, 1], 0, 2).map(r => r[0] + ':' + Rtext(r[1])).join(' '), '2:1 4:1',
     'the running mean, sampled, and exact at each cut-off');

  /* --- L5: geometric to exponential -------------------------------------- */
  eq(Rtext(geoTail(R(1n, 2n), 2, 2)), '81/256', '(1 - 1/2*1/2)^(2/(1/2)) = (3/4)^4, exactly');
  eq(Rtext(geoTail(R(1n, 1n), 1, 3)), '0', 'lambda*Delta = 1 means it always arrives in the first slot');
  /* Rfixed, not Rdec: 200^400 has 921 digits and Number() of it is Infinity, so
     Rdec returns NaN on exactly the case the lesson is about. */
  near(parseFloat(Rfixed(geoTail(R(1n, 2n), 10, 4), 8)), 0.1285121, 1e-6, '(19/20)^40, the lesson\'s exact tail');
  near(parseFloat(Rfixed(geoTail(R(1n, 2n), 100, 4), 8)), 0.1346580, 1e-6, 'a hundred times finer');
  near(expNegApprox(2, 1e-15), 0.13533528, 1e-7, 'and e^-2, which is where it is going');
  eq(Rcmp(geoTail(R(1n, 2n), 100, 4), geoTail(R(1n, 2n), 10, 4)) > 0, true, 'the gap closes from below');
  /* Memorylessness is EXACT at every slot size, for every s. Not a limit. */
  [0, 1, 3, 5].forEach(function (s) {
    eq(Rtext(geoCondTail(R(1n, 2n), 10, s, 4)), Rtext(geoTail(R(1n, 2n), 10, 4)),
       'P(T > s+4 | T > s) = P(T > 4) at s = ' + s + ', exactly');
  });

  /* --- L6: the binomial exactly, Poisson as its limit --------------------- */
  /* binomRow is a recurrence; this checks it against the closed form it
     replaced, which is the only way to know the recurrence is the same
     distribution and not merely a fast one. */
  const row = binomRow(20, 10, 20);
  let mass = R(0n, 1n);
  for (let k = 0; k <= 20; k += 1) {
    mass = Radd(mass, row[k]);
    eq(Rtext(row[k]), Rtext(Rmul(R(comb(20, k), 1n), Rmul(Rpow(R(1n, 2n), k), Rpow(R(1n, 2n), 20 - k)))),
       'binomRow[' + k + '] is comb(n,k)p^k(1-p)^(n-k)');
  }
  eq(Rtext(mass), '1', 'and the row is a distribution');
  eq(Rtext(binomPmf(20, 10, 10)), '46189/262144', 'ten heads in twenty tosses');
  eq(Rtext(binomTail(20, 10, 19)), '1/1048576', 'a tail past n-1 is the last atom, (1/2)^20');
  eq(Rtext(binomTail(20, 10, 10)), '215955/524288', 'and P(more than half heads) at n = 20');
  eq(Rtext(binomTail(20, 10, 20)), '0', 'nothing exceeds n');
  eq(Rtext(binomVar(100, 10)), '9', 'the binomial variance m(1 - m/n) at n = 100');
  eq(Rtext(binomVar(1000, 10)), '99/10', 'closer to the mean as the window is chopped finer');
  near(Number(Rdec(binomTail(200, 10, 15), 8)), 0.0443561, 1e-5, 'P(count > 15) exactly, at 20 chances per unit');
  near(poissonTailApprox(10, 15), 0.0487404, 1e-6, 'and by the Poisson limit, which rounds');
  near(poissonPmfApprox(10, 10), 0.1251100, 1e-6, 'e^-m m^k/k! at the mean');
  eq(headroomForApprox(10, 0.01, 400), 18, 'a mean of 10 needs headroom 18 for a 1% overflow');
  eq(headroomForApprox(10, 0.001, 400), 21, 'and 21 for 0.1% -- the price of the tail');
  eq(headroomForApprox(12, 0.01, 400), 21, 'and 21 at a mean of 12, the largest this lab offers');
  /* Every Poisson figure above is checked against the same recurrence started
     from Math.exp rather than from the core's series, because the two agree only
     inside the range the block below pins. */
  function refPoissonTail(m, C) { let t = Math.exp(-m), h = t; for (let k = 1; k <= C; k += 1) { t = t * m / k; h += t; } return 1 - h; }
  near(poissonTailApprox(10, 15), refPoissonTail(10, 15), 1e-8, 'the Poisson tail matches a Math.exp reference at m = 10');
  near(poissonTailApprox(12, 20), refPoissonTail(12, 20), 1e-6, 'and at m = 12, the edge of the usable range');

  /* --- e^-x has a range, and the kit stops inside it ---------------------- *
     sysdesign_core's expNegApprox sums the ALTERNATING series for e^-x, whose
     largest term is about e^x/sqrt(2 pi x) while the answer is e^-x. It
     therefore loses roughly 2x/ln(10) significant digits to cancellation:
     measured, the relative error is 3e-9 at x = 10, 1.6e-7 at x = 12, 4e-3 at
     x = 17 and 173% at x = 20, and past x = 21 the SIGN is wrong.

     That is a defect in the core, not in this kit, and the fix belongs there --
     1/exp(x) by a positive-term series would be correct at every x. Until then
     the kit bounds the two modes that call it and refuses outside the bound,
     because a wrong number under a promise of a checkable one is worse than no
     number. These assertions pin both halves: that the method is good where the
     lab uses it, and that the lab's own functions refuse where it is not. */
  near(expNegSafe(10), Math.exp(-10), Math.exp(-10) * 1e-6, 'e^-10 is still good to six figures');
  near(expNegSafe(12), Math.exp(-12), Math.exp(-12) * 1e-5, 'e^-12, the bound, to five');
  eq(expNegSafe(20), 'NaN', 'past the bound the kit returns NaN rather than a confident 173% error');
  eq(expNegSafe(-1), 'NaN', 'and refuses a negative x outright');
  eq(poissonTailApprox(20, 25), 'NaN', 'so the Poisson tail refuses too');
  eq(headroomForApprox(20, 0.01, 400), -1, 'and the headroom search reports that it has no answer');
  eq(Number.isNaN(expTailApprox(R(2n, 1n), 12)), true, 'lambda*t = 24 is outside the method');
  eq(expTailApprox(R(3n, 2n), 8) > 0, true, 'lambda*t = 12 is inside it');

  /* --- L8: the knee ------------------------------------------------------ */
  eq(Rtext(kneeFactor(R(1n, 2n))) + ' ' + Rtext(kneeFactor(R(9n, 10n))) + ' ' + Rtext(kneeFactor(R(99n, 100n))),
     '2 10 100', 'W/S at 50%, 90% and 99%');
  eq(Rtext(Rdiv(kneeFactor(R(9n, 10n)), kneeFactor(R(1n, 2n)))), '5', '50% to 90% multiplies the wait by five');
  eq(Rtext(Rdiv(kneeFactor(R(99n, 100n)), kneeFactor(R(9n, 10n)))), '10', 'and 90% to 99% by ten more');
  eq(Rtext(rhoForFactor(10)) + ' ' + Rtext(rhoForFactor(100)), '9/10 99/100', 'the rho at which W = kS is (k-1)/k');
  eq(Rtext(kneeFactor(rhoForFactor(7))), '7', 'and the two are inverses at every k');

  /* --- L9: Kingman, whose model is the approximation --------------------- */
  /* At c_a^2 = c_s^2 = 1 the formula must reproduce M/M/1 EXACTLY. If it does
     not, the disagreement the lesson shows is an arithmetic bug rather than a
     modelling one, and the page would be teaching the wrong lesson. */
  [[1, 2], [4, 5], [9, 10]].forEach(function (r) {
    const rho = R(BigInt(r[0]), BigInt(r[1])), mu = R(1n, 1n);
    const S = Rinv(mu), lam = Rmul(rho, mu);
    eq(Rtext(kingmanWq(rho, R(1n, 1n), R(1n, 1n), S)), Rtext(mm1(lam, mu).Wq),
       'Kingman at c^2 = 1, 1 IS the M/M/1 Wq at rho = ' + Rtext(rho));
  });
  eq(Rtext(kingmanWq(R(4n, 5n), R(1n, 1n), R(0n, 1n), R(2n, 1n))), '4', 'M/D/1 waits half of M/M/1');
  eq(Rtext(kingmanWq(R(4n, 5n), R(1n, 1n), R(1n, 1n), R(2n, 1n))), '8', 'which is 8');
  eq(kingmanWq(R(1n, 1n), R(1n, 1n), R(1n, 1n), R(1n, 1n)), 'null', 'and it says nothing at rho = 1');
  /* The disagreement itself, as a number: at the chain's own coefficients
     Kingman says 22/5 and the exact chain says 4. */
  eq(Rtext(kingmanWq(R(4n, 5n), slottedCa2(R(2n, 5n)), slottedCs2(R(1n, 2n)), R(2n, 1n))), '22/5',
     'Kingman at the slotted chain\'s true c^2');
  eq(Rtext(Rdiv(geoGeo1Lq(R(2n, 5n), R(1n, 2n)), R(2n, 5n))), '4', 'against the chain\'s exact 4');

  /* --- L10: pooling ------------------------------------------------------ */
  /* The lesson's worked example: lambda = 3, mu = 1, s = 4. */
  const pooled = erlangC(R(3n, 1n), R(1n, 1n), 4), separate = mm1(R(3n, 4n), R(1n, 1n));
  eq(Rtext(pooled.pWait) + ' ' + Rtext(pooled.Lq) + ' ' + Rtext(pooled.Wq), '27/53 81/53 27/53',
     'Erlang C at a = 3, s = 4');
  eq(Rtext(separate.Wq), '3', 'against 3 for one of four separate queues at the same load');
  eq(Rtext(Rdiv(separate.Wq, pooled.Wq)), '53/9', 'so splitting the traffic costs 53/9 times the wait');
  eq(Rtext(Rdiv(R(3n, 1n), Rmul(R(4n, 1n), R(1n, 1n)))), '3/4', 'at an identical rho of 3/4 either way');

  /* --- L11: the two W values a lossy system separates -------------------- */
  const fin = mm1k(R(4n, 5n), R(1n, 1n), 4);
  eq(Rtext(fin.blocking), '256/2101', 'the lesson preset blocks 256/2101');
  eq(Rtext(fin.L) + ' ' + Rtext(fin.lamEff), '3284/2101 1476/2101', 'its L and its ADMITTED rate');
  eq(Rtext(fin.W), '821/369', 'W from the admitted rate, which is the right one');
  eq(Rtext(Rdiv(fin.L, R(4n, 5n))), '4105/2101', 'W from the offered rate, which is the wrong one');
  eq(Rtext(Rdiv(fin.W, Rdiv(fin.L, R(4n, 5n)))), Rtext(Rinv(Rsub(R(1n, 1n), fin.blocking))),
     'and the error is exactly the factor 1/(1 - piK)');
  eq(smallestBuffer(R(4n, 5n), R(1n, 1n), R(1n, 100n), 60), 14, 'a 1% loss target needs K = 14 here');
  eq(smallestBuffer(R(4n, 5n), R(1n, 1n), R(1n, 1000n), 60), 24, 'and 0.1% needs K = 24');
  eq(Rtext(bufferLatencyCap(R(1n, 1n), 14)), '14', 'which caps the wait near K/mu -- the bufferbloat trade');
  /* A finite chain is stable at every rho, which is the other half of L11. */
  eq(Rtext(mm1k(R(1n, 1n), R(1n, 1n), 4).blocking), '1/5', 'at rho = 1 every state is equally likely');
  eq(Rtext(mm1k(R(2n, 1n), R(1n, 1n), 3).L) !== '', true, 'and even above rho = 1 there is an answer');

  /* --- L12: the bucket and the window it replaces ------------------------ */
  const TRACE = [0, 200, 400, 600, 800, 900, 900, 900, 900, 900,
                 1000, 1000, 1000, 1000, 1000, 1400, 1600, 1800, 2000, 2200];
  const bkt = bucketRun(TRACE, R(5n, 1n), 3);
  eq(bkt.admitted + '/' + bkt.rejected, '13/7', 'the lesson trace through a bucket of 3 refilling at 5/s');
  eq(bkt.rows.map(r => (r.admit ? '+' : '-')).join(''), '+++++++---+----+++++', 'and which arrival got what');
  eq(largestBurst(bkt.rows, 1000) <= 3 + 5, true, 'no second exceeds the b + rt bound');
  eq(largestBurst(bkt.rows, 1000), 7, 'the largest it actually allows here is 7');
  /* The misconception, as a number: a fixed window of the same nominal limit
     lets nearly twice that through across a boundary. */
  const win = fixedWindowRun(TRACE, 5, 1000);
  eq(win.admitted + '/' + win.rejected, '12/8', 'the same trace through a fixed window at 5 per second');
  eq(largestBurst(win.rows, 1000), 9, 'which lets 9 through in one second while claiming 5');
  eq(largestBurst(win.rows, 1000) > largestBurst(bkt.rows, 1000), true, 'worse than the bucket it replaces');
  eq(Rtext(bucketRun([0, 1000, 2000], R(1n, 1n), 1).rows[2].tokens), '0', 'tokens are exact, not drifting floats');
  /* The lid, which is what makes b a burst allowance rather than a savings
     account. Idle for twenty seconds at one token a second and the bucket has
     earned twenty; it may keep three. Without the cap a quiet night pays for an
     unbounded morning and the b + rt guarantee is gone. */
  const idle = bucketRun([0, 20000, 20000, 20000, 20000, 20000, 20000], R(1n, 1n), 3);
  eq(idle.admitted + '/' + idle.rejected, '4/3', 'twenty idle seconds still buy only b tokens');
  eq(idle.rows.map(r => (r.admit ? '+' : '-')).join(''), '++++---', 'the burst stops at b, not at what was earned');
  eq(Rtext(bucketRun([0, 20000], R(1n, 1n), 3).rows[1].tokens), '2',
     'the level is capped at b before the arrival is charged, so it is 2 and not 21');
  eq(bucketRun([0, 0, 0, 0], R(5n, 1n), 2).admitted, 2, 'a burst with no gap spends the bucket and stops');
  eq(parseTimes('0 10  20', 9).join(','), '0,10,20', 'times parse and sort');
  eq(parseTimes('', 9), 'null', 'and an empty trace is refused rather than guessed at');

  /* --- L13: a spike is an area ------------------------------------------- */
  const plan = backlogPlan(R(1000n, 1n), R(800n, 1n), R(1500n, 1n), 60, R(800n, 1n));
  eq(Rtext(plan.excess) + ' ' + Rtext(plan.peak), '500 30000', 'the excess rate, and the area it builds');
  eq(Rtext(plan.headroom) + ' ' + Rtext(plan.drainSecs), '200 150', 'the headroom left, and the drain it buys');
  eq(Rtext(plan.maxLagSecs), '30', 'the worst lag is backlog/mu');
  eq(Rtext(plan.totalSecs), '210', 'so a 60 second spike is a 210 second incident');
  eq(Rtext(backlogAt(plan, 60, 30)) + ' ' + Rtext(backlogAt(plan, 60, 60)), '15000 30000', 'the backlog rises to its peak AT the end of the spike');
  eq(Rtext(backlogAt(plan, 60, 135)) + ' ' + Rtext(backlogAt(plan, 60, 210)), '15000 0', 'and falls from there');
  eq(Rtext(backlogAt(plan, 60, 400)), '0', 'never going negative');
  const never = backlogPlan(R(1000n, 1n), R(800n, 1n), R(1500n, 1n), 60, R(1000n, 1n));
  eq(never.drains, false, 'with no headroom afterwards it never drains');
  eq(never.drainSecs, 'null', 'and there is no drain time to print');
  eq(Rtext(backlogPlan(R(1000n, 1n), R(800n, 1n), R(900n, 1n), 60, R(800n, 1n)).peak), '0',
     'a "spike" under mu builds nothing at all');

  /* --- the kit's own printing -------------------------------------------- */
  eq(Rfixed(R(1n, 3n), 4), '0.3333', 'long division in BigInt');
  eq(Rfixed(R(2n, 3n), 4), '0.6667', 'rounded half up at the last digit');
  eq(Rfixed(R(-1n, 8n), 3), '-0.125', 'and signed');
  eq(Rpct(R(4n, 5n), 1), '80.0%', 'a percentage of an exact probability');
  eq(Rshort(R(17n, 10n), 4), '17/10', 'a readable fraction stays a fraction');
  eq(Rshort(R(272378807820n, 68618940391n), 4), '3.9694', 'and a twelve-digit one becomes a decimal');
  eq(commas(1234567), '1 234 567', 'digit grouping');
}

// --------------------------------------- availability and failure (kit: avail)
/* The `avail` kit's own arithmetic, on the numbers its thirteen lessons print.
   Every assertion below is a figure that appears on a page, so a change that
   moves one of them is a change to what a lesson claims.

   Four of them are not figures but IDENTITIES, and they are the reason this
   section exists. k-of-n at k = n must be the series product and at k = 1 the
   parallel form; the break-even common cause must be exactly the point at
   which a pair is no better than one machine; halving the repair window must
   divide the loss probability by 2^(N-1) and not by two; and the overlap
   distribution of shuffle sharding must sum to one. Each is exact, each is
   checkable, and each is a claim a lesson makes in prose. */
console.log('system design: availability, retries, durability and blast radius');
{
  const AVAIL_SOURCE = path.join(__dirname, 'mathpath', 'labs', 'avail.py');
  const availSrc = fs.readFileSync(AVAIL_SOURCE, 'utf8');
  const availBlock = (name) => blockFrom(availSrc, name, AVAIL_SOURCE);
  eval(block('RATIONAL_JS') + countingBlock('BIGINT_JS') + sysdBlock('AVAIL_JS')
       + sysdBlock('STREAM_JS') + sysdBlock('APPROX_JS') + availBlock('AVAILKIT_JS'));

  /* --- printing. Rdec goes through Number; the storm iterates past it. ----- */
  eq(Rfixed(R(1n, 3n), 6), '0.333333', 'long division in BigInt');
  eq(Rfixed(R(2n, 3n), 6), '0.666667', 'rounded half up at the last digit');
  eq(Rfixed(R(-1n, 8n), 3), '-0.125', 'a negative rational keeps its sign');
  eq(Rpct(R(999n, 1000n), 5), '99.90000%', 'three nines as a percentage');
  eq(Rpct(R(9999n, 10000n), 5), '99.99000%', 'and four, which two places could not tell apart');
  /* RpctAuto widens with the answer, because a fixed width prints a five-nines
     quorum as 100.000000% -- which is the exact claim these lessons deny. */
  eq(RpctAuto(R(999n, 1000n)), '99.90000%', 'three nines gets five places');
  eq(RpctAuto(Rsub(R(1n, 1n), R(1n, 10n ** 10n))), '99.999999990000%',
     'ten nines gets twelve places, rather than rounding to 100%');
  eq(Rpct(Rsub(R(1n, 1n), R(1n, 10n ** 10n)), 6), '100.000000%',
     'which a fixed six places would have printed as a hundred per cent');
  eq(RpctAuto(R(1n, 1n)), '100%', 'and only an exact one prints as 100%');
  eq(RpctAuto(R(1n, 2n)), '50.0000%', 'while a coin-flip availability gets four');
  /* The reason Rfixed exists here: an iterate of the retry map overflows Number. */
  eq(String(Number(Rpow(R(999n, 1000n), 400).n)), 'Infinity',
     'Number() of 0.999^400 is Infinity');
  eq(Rfixed(Rpow(R(999n, 1000n), 400), 6), '0.670186', 'Rfixed prints it anyway');

  /* --- L1: nines and downtime, in both directions ------------------------- */
  eq(Rtext(periodSeconds('month')), '2628000', 'a month is a twelfth of a 365-day year');
  eq(Rtext(periodSeconds('year')), '31536000', 'and a year is 365 days');
  eq(Rtext(Rmul(periodSeconds('month'), R(12n, 1n))), Rtext(periodSeconds('year')),
     'twelve of those months are exactly the year');
  eq(Rtext(downtimeSeconds(R(999n, 1000n), periodSeconds('month'))), '2628',
     '99.9% is 2628 seconds a month');
  eq(durText(downtimeSeconds(R(999n, 1000n), periodSeconds('month'))), '43 min 48 s',
     'which is the 43.8 minutes the lesson quotes');
  eq(durText(downtimeSeconds(R(9999n, 10000n), periodSeconds('month'))), '4 min 22.80 s',
     'and one more nine is a tenth of it, not 0.09% more');
  eq(durText(downtimeSeconds(R(999n, 1000n), periodSeconds('year'))), '8 h 45 min 36 s',
     '8.76 hours a year');
  /* The two directions are inverses, which is what makes the budget selector
     and the target selector the same lesson rather than two. */
  eq(Rtext(availFromDowntime(R(2628n, 1n), periodSeconds('month'))), '999/1000',
     'a 2628-second budget IS three nines');
  eq(Rtext(availFromDowntime(downtimeSeconds(R(99991n, 100000n), periodSeconds('week')),
                             periodSeconds('week'))), '99991/100000',
     'and the round trip returns the availability it started from');
  eq(ninesOf(R(999n, 1000n)), 3, '99.9% has three nines');
  eq(ninesOf(R(9995n, 10000n)), 3, '99.95% has three, not three and a half');
  eq(ninesOf(R(9n, 10n)), 1, '90% has one');
  eq(ninesOf(R(1n, 2n)), 0, 'and 50% has none');

  /* --- L2: MTBF, MTTR, and the identity that makes the lesson -------------- */
  eq(Rtext(availFromMtbf(R(1000n, 1n), R(1n, 1n))), '1000/1001', 'A = MTBF/(MTBF + MTTR)');
  /* THE IDENTITY: halving the repair time is worth exactly as much as doubling
     the time between failures. A(2M, R) = 2M/(2M+R) = M/(M+R/2) = A(M, R/2).
     The lesson says "worth as much"; this is the sense in which that is exact. */
  eq(Requ(availFromMtbf(Rmul(R(1000n, 1n), R(2n, 1n)), R(1n, 1n)),
          availFromMtbf(R(1000n, 1n), Rdiv(R(1n, 1n), R(2n, 1n)))), true,
     'doubling MTBF and halving MTTR give the SAME fraction');
  eq(Requ(availFromMtbf(Rmul(R(37n, 5n), R(2n, 1n)), R(3n, 7n)),
          availFromMtbf(R(37n, 5n), Rdiv(R(3n, 7n), R(2n, 1n)))), true,
     'and on numbers with nothing round about them');
  /* The target solvers invert the availability formula, so putting their
     answer back in must return the target exactly. */
  eq(Rtext(availFromMtbf(R(1000n, 1n), mttrForTarget(R(1000n, 1n), R(9999n, 10000n)))), '9999/10000',
     'the MTTR a target needs, put back through A, returns the target');
  eq(Rtext(availFromMtbf(mtbfForTarget(R(1n, 1n), R(999n, 1000n)), R(1n, 1n))), '999/1000',
     'and so does the MTBF a target needs');
  eq(Rtext(failuresPerPeriod(Radd(R(3600000n, 1n), R(3600n, 1n)), periodSeconds('year'))), '8760/1001',
     '1000 h up plus 1 h down is 8.75 cycles a year');

  /* --- L3: the chain, and how far under the weakest link it lands ---------- */
  eq(Rtext(pctToFraction('99.9')), '999/1000', 'a typed percentage is an exact fraction');
  eq(Rtext(pctToFraction('99.95')), '1999/2000', 'and in lowest terms');
  eq(parseChain('99.9, 99.99, 100').length, 3, 'a chain of three');
  eq(parseChain('99.9, banana'), null, 'and a typo is refused rather than guessed at');
  const ten = parseChain('99.9, 99.9, 99.9, 99.9, 99.9, 99.9, 99.9, 99.9, 99.9, 99.9');
  eq(Rtext(availSeries(ten)), Rtext(Rpow(R(999n, 1000n), 10)), 'ten of them is the tenth power');
  eq(Rfixed(availSeries(ten), 7), '0.9900449', 'ten 99.9% dependencies give 99.0%, not 99.9%');
  /* The misconception, as a number: the chain is TEN TIMES the downtime of its
     own weakest link, not equal to it. */
  eq(Rfixed(Rdiv(Rsub(R(1n, 1n), availSeries(ten)), Rsub(R(1n, 1n), R(999n, 1000n))), 2), '9.96',
     'the chain is 9.96x the downtime of the weakest link in it');
  eq(Rcmp(availSeries(ten), R(999n, 1000n)) < 0, true, 'and strictly worse than it');
  eq(Rtext(availSeries(parseChain('100, 100'))), '1', 'a chain of perfect parts is perfect');

  /* --- L4: parallel, and the failover the formula does not contain --------- */
  const two99 = [R(99n, 100n), R(99n, 100n)];
  eq(Rtext(availParallel(two99)), '9999/10000', 'two 99% paths are four nines, ideally');
  const charged = parallelWithFailover(two99, R(30n, 1n), R(12n, 1n), periodSeconds('year'));
  eq(Rtext(charged.ideal), '9999/10000', 'the ideal figure is untouched');
  eq(Rtext(charged.charge), '1/87600', '12 failovers of 30 s is 360 s a year');
  eq(Rtext(charged.adjusted), Rtext(Rsub(R(9999n, 10000n), R(1n, 87600n))),
     'and the real availability is the ideal one minus that');
  eq(Rfixed(charged.adjusted, 8), '0.99988858', 'four nines becomes three');
  eq(ninesOf(charged.ideal) + ' ' + ninesOf(charged.adjusted), '4 3',
     'the switch costs a whole nine, which is what "failover is not free" means');
  eq(Rtext(parallelWithFailover(two99, R(0n, 1n), R(12n, 1n), periodSeconds('year')).adjusted),
     '9999/10000', 'an instant switch costs nothing, which is the formula as written');

  /* --- L5: k-of-n, AND THE TWO IDENTITIES ---------------------------------- */
  /* These are the assertions the course rests on: the binomial tail is not a
     third model, it is the other two with k moved. If either fails, one of
     three lessons is teaching a different arithmetic from the other two. */
  const A99 = R(99n, 100n);
  for (const n of [1, 2, 3, 5, 8, 12]) {
    const copies = [];
    for (let i = 0; i < n; i += 1) copies.push(A99);
    eq(Requ(availKofN(A99, n, n), availSeries(copies)), true,
       'k = n is the series product at n = ' + n);
    eq(Requ(availKofN(A99, 1, n), availParallel(copies)), true,
       'k = 1 is the parallel form at n = ' + n);
    eq(Rtext(kofnTotal(A99, n)), '1', 'and all ' + (n + 1) + ' terms sum to one');
  }
  /* The same two identities on an availability with an ugly denominator, since
     99/100 is exactly the kind of number a wrong coefficient survives. */
  const Augly = R(7n, 11n), uglyCopies = [Augly, Augly, Augly, Augly];
  eq(Requ(availKofN(Augly, 4, 4), availSeries(uglyCopies)), true, 'k = n at A = 7/11');
  eq(Requ(availKofN(Augly, 1, 4), availParallel(uglyCopies)), true, 'k = 1 at A = 7/11');
  eq(Rtext(kofnTotal(Augly, 4)), '1', 'and its terms still sum to one');
  eq(Rtext(availKofN(R(1n, 2n), 2, 3)), '1/2', 'a majority of three fair coins');
  eq(Rfixed(availKofN(A99, 3, 5), 6), '0.999990', '3 of 5 at 99% is five nines');
  /* "More replicas always means more available" is false, and this is where. */
  eq(Rcmp(availKofN(A99, 5, 5), A99) < 0, true, '5-of-5 is WORSE than 1-of-1');
  eq(Rtext(kofnTerms(A99, 3)[3].term), Rtext(Rpow(A99, 3)), 'the j = n term is the series product');
  eq(String(kofnTerms(A99, 5)[2].c), '10', 'the coefficients are C(n, j)');

  /* --- L6: the common cause, and where redundancy stops paying ------------- */
  eq(Rtext(pairBothDown(R(0n, 1n), R(1n, 100n))), '1/10000', 'at c = 0 the pair is p^2');
  eq(Rtext(pairBothDown(R(1n, 1000n), R(1n, 100n))), '10999/10000000',
     'a 0.1% common cause against a 10^-4 pair');
  eq(Rfixed(Rdiv(pairBothDown(R(1n, 1000n), R(1n, 100n)), R(1n, 10000n)), 2), '11.00',
     'which is eleven times what independence promised');
  eq(Rtext(correlatedBreakEven(R(1n, 100n))), '1/101', 'the break-even c is p/(1 + p)');
  /* THE IDENTITY: at that c the pair is EXACTLY as available as one machine.
     The lesson asks the reader to find "the c at which redundancy buys
     nothing"; this is the sense in which that c is exact rather than a
     reading off a curve. */
  for (const p of [R(1n, 100n), R(1n, 3n), R(7n, 1000n)]) {
    eq(Rtext(pairBothDown(correlatedBreakEven(p), p)), Rtext(p),
       'at c = p/(1+p) the pair is down exactly as often as one machine, p = ' + Rtext(p));
    eq(Rtext(redundancyGain(correlatedBreakEven(p), p)), '1',
       'so the redundancy gain there is exactly 1');
  }
  eq(Rtext(redundancyGain(R(0n, 1n), R(1n, 100n))), '100', 'and 1/p under independence');

  /* --- L7: the error budget, in requests rather than minutes --------------- */
  const reqs = Rmul(R(1000n, 1n), periodSeconds('month'));
  eq(Rtext(reqs), '2628000000', '1000 rps for a month');
  eq(Rtext(budgetRequests(R(999n, 1000n), reqs)), '2628000', 'is a budget of 2.628 M failures');
  eq(Rtext(incidentBurn(R(1000n, 1n), R(1800n, 1n), R(1n, 1n))), '1800000',
     'a 30-minute total outage costs 1.8 M of them');
  eq(Rtext(Rdiv(incidentBurn(R(1000n, 1n), R(1800n, 1n), R(1n, 1n)),
                budgetRequests(R(999n, 1000n), reqs))), '50/73', 'which is 68.5% of the budget');
  /* Severity is a multiplier, which is the whole difference between an SLO on
     requests and an SLO on the clock. */
  eq(Rtext(incidentBurn(R(1000n, 1n), R(1800n, 1n), R(1n, 2n))), '900000',
     'the same 30 minutes at half severity costs half as much');
  eq(Rtext(budgetSeconds(R(999n, 1000n), periodSeconds('month'))), '2628',
     'and the budget as a full outage is the L1 downtime figure again');

  /* --- L8: retries as load ------------------------------------------------- */
  eq(Rtext(retryAttempts(R(1n, 10n), 2)), '111/100', 'two retries at p = 0.1 cost 1.11 attempts');
  eq(Rtext(retrySuccess(R(1n, 10n), 2)), '999/1000', 'and succeed 99.9% of the time');
  eq(Rtext(amplifiedLoad(R(500n, 1n), R(1n, 10n), 2)), '555', '500 rps becomes 555 attempts a second');
  eq(Rtext(duplicateShare(R(1n, 10n), 2)), '11/111', 'of which 9.9% is retry traffic');
  /* The geometric sum, checked against the sum it stands for: the expected
     attempts are the probabilities of reaching each attempt, added up. */
  for (const p of [R(1n, 10n), R(9n, 10n), R(1n, 3n)]) {
    for (const r of [0, 1, 3, 6]) {
      let s = R(0n, 1n);
      for (let i = 0; i <= r; i += 1) s = Radd(s, attemptReach(p, i));
      eq(Rtext(s), Rtext(retryAttempts(p, r)),
         'sum of p^i for i <= r IS the closed form, p = ' + Rtext(p) + ', r = ' + r);
    }
  }
  /* The amplification is worst exactly when the service is worst, and its
     ceiling is the retry budget itself. */
  eq(Rcmp(retryAttempts(R(9n, 10n), 3), retryAttempts(R(1n, 10n), 3)) > 0, true,
     'a worse failure rate costs more attempts, not fewer');
  eq(Rtext(retryAttempts(R(9n, 10n), 3)), '3439/1000', 'p = 0.9 with 3 retries is 3.439 attempts');
  eq(Rcmp(retryAttempts(R(99n, 100n), 3), R(4n, 1n)) < 0, true, 'and it never reaches r + 1');

  /* --- L9: the retry storm, its iteration and its fixed point -------------- */
  const lam = R(95n, 100n), cap = R(1n, 1n), base = R(1n, 10n);
  eq(Rtext(stormFailure(R(1n, 2n), cap, base)), '1/10', 'under capacity the failure rate is the base');
  eq(Rtext(stormFailure(R(2n, 1n), cap, base)), '11/20',
     'at twice capacity half the excess fails on top of it');
  eq(Rtext(stormNext(lam, cap, base, 0, lam).load), Rtext(lam),
     'with no retries the map is the identity, so the offered load IS the answer');
  const run = stormRun(lam, cap, base, 3, 5, 3000);
  eq(run.rows.length, 5, 'five iterations');
  eq(Rtext(run.rows[0].amp), '1111/1000', 'the first amplification, exactly');
  eq(Rtext(run.rows[0].out), '21109/20000', 'and the first iterate, which is already over capacity');
  eq(Rcmp(run.rows[0].out, cap) > 0, true, 'from an offered load that was NOT');
  eq(Rcmp(run.rows[4].out, run.rows[0].out) > 0, true, 'the iterates climb');
  /* The fixed point is an ENCLOSURE and the bracket is what makes it exact:
     the map is increasing, so a sign change between two fractions traps a
     fixed point between them. Both ends are checked in the right direction. */
  const fp = stormFixedPoint(lam, cap, base, 3, 24);
  eq(Rcmp(stormNext(lam, cap, base, 3, fp.lo).load, fp.lo) >= 0, true,
     'the map pushes the low end up');
  eq(Rcmp(stormNext(lam, cap, base, 3, fp.hi).load, fp.hi) <= 0, true,
     'and the high end down, so the fixed point is between them');
  eq(Rcmp(fp.lo, fp.hi) <= 0, true, 'and the bracket is the right way round');
  eq(Rfixed(fp.lo, 5), '1.72736', 'the fixed point of the preset');
  /* THE LESSON: the un-retried load was serviceable and the fixed point is not. */
  eq(Rcmp(lam, cap) <= 0, true, '0.95 of capacity was fine');
  eq(Rcmp(fp.lo, cap) > 0, true, 'and the retries alone put the fixed point above capacity');
  eq(Rcmp(stormFixedPoint(lam, cap, base, 0, 24).hi, cap) < 0, true,
     'with retries switched off the same load settles below capacity');
  /* The digit budget stops the table rather than hanging the page. */
  eq(stormRun(lam, cap, base, 3, 12, 200).stopped, true,
     'a tight digit budget stops the iteration and says so');
  eq(stormRun(lam, cap, base, 3, 12, 200).rows.length < 12, true, 'with fewer rows than asked for');

  /* --- L10: backoff waves, seeded ----------------------------------------- */
  eq([1, 2, 3, 4].map((i) => backoffDelayMs(1000, i)).join(','), '1000,2000,4000,8000',
     'the waves land at 1, 2, 4 and 8 seconds');
  const noJit = backoffHistogram(600, 20, 1000, 0, 8, 40, 7, 200);
  eq(noJit.plain.join(',') === noJit.jitter.join(','), true,
     'jitter of zero width IS the un-jittered schedule, which is the check that the spread is centred');
  eq(peakOf(noJit.plain), 600, 'and every client lands in one slot');
  const jit = backoffHistogram(600, 20, 1000, 100, 8, 40, 7, 200);
  eq(peakOf(jit.jitter) < peakOf(jit.plain), true, 'jitter lowers the peak');
  eq(peakOf(jit.plain), 600, 'while the un-jittered arm is unchanged by the jitter slider');
  eq(totalOf(jit.plain), 3600, 'six waves of 600 without jitter');
  /* Seeded, and the seed is actually used: same seed same bars, other seed not. */
  eq(backoffHistogram(600, 20, 1000, 100, 8, 40, 7, 200).jitter.join(','),
     jit.jitter.join(','), 'the same seed draws the same histogram');
  eq(backoffHistogram(600, 20, 1000, 100, 8, 40, 8, 200).jitter.join(',') === jit.jitter.join(','),
     false, 'and a different seed does not');
  eq(perSecond(jit.jitter, 200).length <= 40, true, 'the per-second fold covers the horizon');
  eq(totalOf(perSecond(jit.jitter, 200)), totalOf(jit.jitter), 'and loses no retries');

  /* --- L11: shedding against collapse ------------------------------------- */
  const capacity = R(1000n, 1n);
  eq(Rtext(goodputShed(R(2000n, 1n), capacity, R(900n, 1n))), '900',
     'shedding above 90% of capacity delivers 900 rps at twice the load');
  eq(Rtext(goodputUnshed(R(2000n, 1n), capacity)), '500', 'not shedding delivers 500');
  eq(Rcmp(goodputShed(R(2000n, 1n), capacity, R(900n, 1n)),
          goodputUnshed(R(2000n, 1n), capacity)) > 0, true,
     'so rejecting requests served MORE users than accepting them');
  eq(Rtext(goodputUnshed(capacity, capacity)), '1000', 'the collapse model is continuous at the knee');
  eq(Rtext(goodputUnshed(R(500n, 1n), capacity)), '500', 'and is the offered load below it');
  eq(Rtext(goodputShed(R(500n, 1n), capacity, R(900n, 1n))), '500',
     'a shedder under its threshold sheds nothing');
  eq(Rtext(rejectedFraction(R(2000n, 1n), R(900n, 1n))), '11/20', 'and rejects 55% at twice capacity');
  eq(Rtext(rejectedFraction(R(500n, 1n), R(900n, 1n))), '0', 'nothing at all below it');
  /* A threshold set above capacity is not a shedder: what it admits collapses
     exactly as the unshed arm does, which is the failure mode of a limit copied
     from the load generator rather than measured from the service. */
  eq(Rtext(goodputShed(R(2000n, 1n), capacity, R(1200n, 1n))),
     Rtext(goodputUnshed(R(1200n, 1n), capacity)), 'a threshold above capacity sheds into collapse');
  eq(Rtext(goodputShed(R(2000n, 1n), capacity, R(1200n, 1n))), '2500/3',
     'and delivers less than a threshold at 90% would');
  eq(Rtext(admittedLoad(R(2000n, 1n), R(900n, 1n))), '900', 'the shedder admits the threshold');
  eq(Rtext(admittedLoad(R(500n, 1n), R(900n, 1n))), '500', 'or the offered load, whichever is smaller');
  eq(Rtext(Rdiv(admittedLoad(R(2000n, 1n), R(900n, 1n)), capacity)), '9/10',
     'so utilisation under the shedder is the ADMITTED load over capacity, not the goodput');

  /* --- L12: durability, the one approximation ----------------------------- */
  /* The exact fraction of the first-order formula, which is what the page
     prints beside the float so that the reader can see WHICH part rounds. */
  eq(Rtext(durabilityLossExact(3, R(1n, 50n), R(24n, 1n))), '3/8326562500',
     'three copies, 2% a year, a 24 h repair window');
  near(durabilityLossApprox(3, R(1n, 50n), R(24n, 1n)), 3.6029e-10, 1e-14,
     'and the float agrees with it');
  near(durabilityLossApprox(3, R(1n, 50n), R(24n, 1n)),
       Number(durabilityLossExact(3, R(1n, 50n), R(24n, 1n)).n)
       / Number(durabilityLossExact(3, R(1n, 50n), R(24n, 1n)).d), 1e-20,
       'the rounding is in the MODEL, not in the division');
  /* THE IDENTITY: halving the window divides by 2^(N-1), not by two. This is
     the lesson's "R matters as much as f", and it is exact. */
  for (const n of [2, 3, 4, 6]) {
    eq(Rtext(Rdiv(durabilityLossExact(n, R(1n, 50n), R(24n, 1n)),
                  durabilityLossExact(n, R(1n, 50n), R(12n, 1n)))), String(Math.pow(2, n - 1)),
       'halving R divides the loss probability by 2^(N-1) at N = ' + n);
  }
  /* "Three copies is three times the durability" is false: it is a factorial
     times the Nth power of the failure rate. */
  eq(Rtext(Rdiv(durabilityLossExact(1, R(1n, 50n), R(24n, 1n)),
                durabilityLossExact(3, R(1n, 50n), R(24n, 1n)))),
     Rtext(Rdiv(R(1n, 1n), Rmul(R(6n, 1n), Rmul(Rpow(R(1n, 50n), 2), Rpow(R(1n, 365n), 2))))),
     'a third copy is worth f^2 R^2 times a factorial, not a factor of three');
  eq(Rtext(durabilityLossExact(1, R(1n, 50n), R(24n, 1n))), '1/50',
     'and one copy is just the failure rate');
  /* The truncation itself: the first-order term stands in for 1 - e^-x, and
     the page shows the gap rather than claiming there is none. */
  const gap = truncationGap(2 * 0.02 * 24 / 8760);
  eq(gap.first > gap.exact, true, 'the first-order term overstates 1 - e^-x');
  near((gap.first - gap.exact) / gap.first, 5.48e-5, 1e-6, 'here by 0.0055%');

  /* --- L13: shuffle sharding, exactly ------------------------------------- */
  eq(String(comb(16, 2)), '120', 'sixteen nodes, two each, is 120 shards');
  eq(Rtext(shuffleDisjoint(16, 2)), '91/120', 'two tenants share no node 91 times in 120');
  eq(Rtext(shuffleIdentical(16, 2)), '1/120', 'and hold the identical set once');
  eq(Rtext(shuffleOverlap(16, 2, 1)), '7/30', 'overlapping in exactly one is the rest');
  /* THE IDENTITY: the overlap distribution is a distribution. This is
     Vandermonde, and a wrong coefficient anywhere breaks it. */
  for (const [n, k] of [[16, 2], [8, 3], [40, 8], [10, 5], [6, 1], [5, 3]]) {
    let s = R(0n, 1n);
    for (let j = 0; j <= k; j += 1) s = Radd(s, shuffleOverlap(n, k, j));
    eq(Rtext(s), '1', 'the overlap terms sum to one at n = ' + n + ', k = ' + k);
  }
  /* Where a disjoint pair is impossible the probability must be zero, not
     small: with k > n/2 there are not enough nodes left to miss you. */
  eq(Rtext(shuffleDisjoint(5, 3)), '0', 'with 3 of 5 nodes, no second tenant can miss you');
  eq(Rtext(shuffleIdentical(5, 3)), '1/10', 'and one pairing in ten is identical');
  eq(Rtext(blastFraction(16, 2)), '1/8', 'one bad node degrades an eighth of the tenants');
  /* The sample assignment is drawn from the same seeded stream the page uses,
     so what it shows and what it claims come from one run. */
  const sets = shuffleAssign(16, 2, 12, 3);
  eq(sets.length, 12, 'twelve tenants drawn');
  eq(sets.every((s) => s.length === 2), true, 'each holding exactly k nodes');
  eq(sets.every((s) => s[0] !== s[1]), true, 'and never the same node twice');
  eq(sets.every((s) => s.every((v) => v >= 0 && v < 16)), true, 'all inside the fleet');
  eq(shuffleAssign(16, 2, 12, 3).join('|'), sets.join('|'), 'the same seed draws the same assignment');
  eq(shuffleAssign(16, 2, 12, 4).join('|') === sets.join('|'), false, 'a different seed does not');
  eq(identicalCount([[1, 2], [1, 2], [3, 4]]), 1, 'one tenant holds the exact set of the first');
  eq(disjointCount([[1, 2], [1, 2], [3, 4]]), 1, 'and one shares nothing with it');
}

if (fails) {
  console.log('\n' + fails + ' assertion(s) FAILED');
  process.exit(1);
}
console.log('\nevery arithmetic assertion passes');
