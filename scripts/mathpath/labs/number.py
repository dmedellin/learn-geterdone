"""Labs for course 6: number theory and cryptography."""

from .common import Lab, cfg_literal

NT_JS = r"""
  /* Everything here is BigInt. Modular exponentiation with 4-digit moduli
     already overflows exact double arithmetic, and a cryptography lab that
     silently rounded would produce ciphertext that does not decrypt -- with no
     sign that arithmetic rather than the method was at fault.

     The functions below are the arithmetic; the modes further down only
     display it. scripts/mathcheck.js extracts this block and executes it,
     which is the only check in the repository that can tell a wrong gcd from
     a right one. */
  function bgcd(a, b) { a = a < 0n ? -a : a; b = b < 0n ? -b : b; while (b) { var t = a % b; a = b; b = t; } return a; }
  function egcd(a, b) {
    /* Returns [g, x, y] with a*x + b*y = g. The coefficients are what make
       Bezout's identity constructive rather than an existence claim. */
    var old_r = a, r = b, old_s = 1n, s = 0n, old_t = 0n, t = 1n;
    while (r !== 0n) {
      var q = old_r / r;
      var tmp = old_r - q * r; old_r = r; r = tmp;
      tmp = old_s - q * s; old_s = s; s = tmp;
      tmp = old_t - q * t; old_t = t; t = tmp;
    }
    return [old_r, old_s, old_t];
  }
  function egcdTrace(a, b) {
    /* The same algorithm on |a| and |b|, keeping every row. On each row
       r = |a|*s + |b|*t holds -- that is the loop invariant, and it is why the
       last nonzero row IS Bezout's identity with no back-substitution. The
       signs of the coefficients are restored at the end so the identity is
       stated for the inputs as typed. */
    var A = a < 0n ? -a : a, B = b < 0n ? -b : b;
    var rows = [{ r: A, q: null, s: 1n, t: 0n }, { r: B, q: null, s: 0n, t: 1n }];
    var old_r = A, r = B, old_s = 1n, s = 0n, old_t = 0n, t = 1n;
    while (r !== 0n && rows.length < 400) {
      var q = old_r / r;
      var nr = old_r - q * r, ns = old_s - q * s, nt = old_t - q * t;
      old_r = r; r = nr; old_s = s; s = ns; old_t = t; t = nt;
      rows.push({ r: r, q: q, s: s, t: t });
    }
    var sa = a < 0n ? -1n : 1n, sb = b < 0n ? -1n : 1n;
    return { rows: rows, g: old_r, x: old_s * sa, y: old_t * sb };
  }
  function modpow(base, exp, mod) {
    var result = 1n; base %= mod;
    if (base < 0n) base += mod;
    while (exp > 0n) {
      if (exp & 1n) result = result * base % mod;
      base = base * base % mod;
      exp >>= 1n;
    }
    return result;
  }
  function modpowTrace(base, exp, mod, limit) {
    /* Square and multiply, one row per bit of the exponent. The count is what
       the loop actually did: one squaring per row except the last (whose
       square is never used) and one multiplication per set bit. */
    var rows = [], b = ((base % mod) + mod) % mod, e = exp, result = 1n, bit = 0, mults = 0;
    while (e > 0n && bit < limit) {
      var use = (e & 1n) === 1n;
      if (use) { result = result * b % mod; mults += 1; }
      rows.push({ bit: bit, use: use, power: b, result: use ? result : null });
      b = b * b % mod; e >>= 1n; bit += 1;
    }
    return { rows: rows, result: result, squarings: rows.length ? rows.length - 1 : 0, mults: mults, complete: e === 0n };
  }
  function modinv(a, m) {
    var e = egcd(((a % m) + m) % m, m);
    if (e[0] !== 1n) return null;
    return ((e[1] % m) + m) % m;
  }
  function isPrimeBig(n) {
    if (n < 2n) return false;
    if (n % 2n === 0n) return n === 2n;
    for (var d = 3n; d * d <= n; d += 2n) if (n % d === 0n) return false;
    return true;
  }
  function factorize(n) {
    /* Trial division, the lesson-2 method: [[p, e], ...] with p increasing.
       Stops at sqrt(remaining), which is the bound lesson 2 proves. */
    var out = [], left = n < 0n ? -n : n;
    if (left < 2n) return out;
    for (var d = 2n; d * d <= left; d += (d === 2n ? 1n : 2n)) {
      var e = 0n;
      while (left % d === 0n) { left /= d; e += 1n; }
      if (e > 0n) out.push([d, e]);
    }
    if (left > 1n) out.push([left, 1n]);
    return out;
  }
  function totient(n) {
    /* phi(n) = n * prod (1 - 1/p), computed as n / p * (p - 1) per prime so
       every intermediate is an integer. This is lesson 11's formula, not a
       count over 1..n, so it costs sqrt(n) rather than n. */
    var phi = n;
    factorize(n).forEach(function (pe) { phi = phi / pe[0] * (pe[0] - 1n); });
    return phi;
  }
  function divisorCount(n) {
    var c = 1n;
    factorize(n).forEach(function (pe) { c *= pe[1] + 1n; });
    return c;
  }
  function crtPair(a1, m1, a2, m2) {
    /* x = a1 (mod m1), x = a2 (mod m2) for ANY positive moduli. Coprime
       moduli are the theorem. Otherwise the system is consistent exactly
       when a1 = a2 (mod gcd), and then the solution is unique modulo the
       LCM, not the product -- which is what lesson 10's "coprimality is not
       optional" section says and what its lab must be able to show. */
    var g = bgcd(m1, m2), l = m1 / g * m2;
    var r1 = ((a1 % m1) + m1) % m1, r2 = ((a2 % m2) + m2) % m2;
    var diff = r2 - r1;
    if (((diff % g) + g) % g !== 0n) return { g: g, lcm: l, r1: r1, r2: r2, x: null };
    var m2g = m2 / g, inv = modinv((m1 / g) % m2g, m2g);
    var k = inv === null ? 0n : ((((diff / g) % m2g) + m2g) % m2g) * inv % m2g;
    var x = ((r1 + m1 * k) % l + l) % l;
    return { g: g, lcm: l, r1: r1, r2: r2, x: x };
  }
  function lcgRun(a, c, m, seed, limit) {
    /* Iterate x -> (a x + c) mod m until a value repeats or `limit` values
       have been produced. `start` is the index the repeated value first
       appeared at, so the period is seq.length - start and the values before
       `start` are a tail the cycle never returns to. */
    var seen = {}, seq = [], x = ((seed % m) + m) % m, i = 0;
    while (!(x.toString() in seen) && i < limit) {
      seen[x.toString()] = i; seq.push(x);
      x = ((a * x + c) % m + m) % m; i += 1;
    }
    var start = (x.toString() in seen) ? seen[x.toString()] : -1;
    return { seq: seq, next: x, start: start, period: start < 0 ? -1 : seq.length - start };
  }
  function hullDobell(a, c, m) {
    /* The three conditions of the Hull-Dobell theorem, in the lesson's order:
       gcd(c, m) = 1; every prime dividing m divides a - 1; 4 | m implies 4 | a - 1. */
    var ps = factorize(m).map(function (pe) { return pe[0]; });
    return [bgcd(c, m) === 1n,
            ps.every(function (p) { return ((a - 1n) % p + p) % p === 0n; }),
            m % 4n !== 0n || ((a - 1n) % 4n + 4n) % 4n === 0n];
  }
  function affineMap(a, b, m) {
    /* x -> (a x + b) mod m on 0..m-1, with the number of distinct images.
       Injective exactly when gcd(a, m) = 1, which is when `inv` exists. */
    var out = [], images = {};
    for (var x = 0n; x < m; x += 1n) {
      var y = (((a * x + b) % m) + m) % m;
      out.push(y); images[y.toString()] = 1;
    }
    return { map: out, distinct: Object.keys(images).length, inv: modinv(a, m) };
  }
"""

# Above this, trial division to sqrt(n) finishes in well under a second in
# BigInt; a reader who types a 15-digit number into the factor mode would
# otherwise freeze the tab for minutes, which teaches nothing lesson 14 does
# not already say.
TRIAL_LIMIT = "1000000000000n"


def number_lab(cfg):
    """One lab, twelve modes, each showing the ALGORITHM rather than its output.

    A gcd that appears is a fact to memorize; a gcd with its division steps
    laid out is a method the reader can run on paper afterwards. Every mode
    here prints its trace. The config may carry `a`, `b`, `m` and `n` so a
    lesson opens on its own example rather than on the workbench's default.
    """
    markup = """      <div class="lab-toolbar">
        <div class="lab-title"><strong id="ntTitle">Number theory workbench</strong><span id="ntSub"></span></div>
        <div class="inline-legend"><span class="tone-cyan"><i class="legend-swatch"></i>the step that decides</span></div>
      </div>
      <div class="lab-stage"><div class="table-wrap" id="ntOut"></div></div>
      <div class="status-banner" id="ntStatus" style="margin-top:12px;"></div>"""
    controls = """        <div class="field">
          <label for="ntMode">Mode</label>
          <select id="ntMode">
            <option value="div">Division algorithm: a = qb + r</option>
            <option value="euclid">Euclidean algorithm: gcd(a, b)</option>
            <option value="bezout">Extended Euclid: ax + by = gcd</option>
            <option value="modtable">Modular arithmetic tables</option>
            <option value="modexp">Modular exponentiation by squaring</option>
            <option value="congr">Solve ax &equiv; b (mod m)</option>
            <option value="crt">Chinese remainder theorem</option>
            <option value="fermat">Fermat and Euler</option>
            <option value="sieve">Sieve of Eratosthenes</option>
            <option value="factor">Prime factorisation</option>
            <option value="lcg">Linear congruential generator</option>
            <option value="affine">Affine cipher on 26 letters</option>
          </select>
        </div>
        <div class="field" id="ntAWrap">
          <label for="ntA" id="ntALabel">a</label>
          <input id="ntA" type="number" value="1071" />
        </div>
        <div class="field" id="ntBWrap">
          <label for="ntB" id="ntBLabel">b</label>
          <input id="ntB" type="number" value="462" />
        </div>
        <div class="field" id="ntMWrap">
          <label for="ntM" id="ntMLabel">m (modulus)</label>
          <input id="ntM" type="number" value="26" />
        </div>
        <div class="field" id="ntNWrap">
          <label for="ntN" id="ntNLabel">n</label>
          <input id="ntN" type="number" value="5" />
        </div>
        <div class="kpi-grid">
          <div class="kpi"><span id="ntK1Label">gcd</span><strong id="ntK1">&mdash;</strong></div>
          <div class="kpi"><span id="ntK2Label">steps</span><strong id="ntK2">&mdash;</strong></div>
        </div>"""

    preset = {k: cfg[k] for k in ("a", "b", "m", "n") if k in cfg}

    script = NT_JS + cfg_literal("PRESET", preset) + r"""
  var TRIAL_LIMIT = """ + TRIAL_LIMIT + r""";
  var modeSel = document.getElementById('ntMode');
  var aIn = document.getElementById('ntA'), bIn = document.getElementById('ntB');
  var mIn = document.getElementById('ntM'), nIn = document.getElementById('ntN');
  var out = document.getElementById('ntOut'), status = document.getElementById('ntStatus');
  var title = document.getElementById('ntTitle'), sub = document.getElementById('ntSub');
  var k1 = document.getElementById('ntK1'), k2 = document.getElementById('ntK2');
  var k1L = document.getElementById('ntK1Label'), k2L = document.getElementById('ntK2Label');

  function table(head, rows) {
    return '<table class="tt"><thead><tr>' + head.map(function (h) { return '<th>' + h + '</th>'; }).join('')
      + '</tr></thead><tbody>' + rows.join('') + '</tbody></table>';
  }
  function row(cells, focus) {
    return '<tr' + (focus ? ' class="focus"' : '') + '>' + cells.map(function (c) { return '<td>' + c + '</td>'; }).join('') + '</tr>';
  }
  function clamp(v, lo, hi) { return Math.max(lo, Math.min(hi, v)); }
  function tooBig(n) { return (n < 0n ? -n : n) > TRIAL_LIMIT; }
  function refuse(what) {
    out.innerHTML = '';
    status.innerHTML = '<strong>' + what + ' is too large for this lab.</strong> Its only method is trial division up to '
      + 'the square root, which is fine below 10<sup>12</sup> and would freeze this page for minutes above it. That '
      + 'the cost climbs like that is exactly what lesson 14 relies on; a number this size is best factored on paper, '
      + 'which is to say not at all.';
  }
  function letter(x) { return String.fromCharCode(65 + Number(x)); }

  /* Which inputs a mode uses, and what it calls them. Everything else is hidden
     by the id on its wrapper, never by walking up from the input. */
  function show(spec) {
    ['A', 'B', 'M', 'N'].forEach(function (f) {
      var on = Object.prototype.hasOwnProperty.call(spec, f);
      document.getElementById('nt' + f + 'Wrap').hidden = !on;
      if (on) document.getElementById('nt' + f + 'Label').textContent = spec[f];
    });
  }

  var MODES = {
    div: function (a, b) {
      show({ A: 'a (dividend)', B: 'b (divisor)' });
      title.textContent = 'Division algorithm';
      sub.textContent = 'a = qb + r with 0 ≤ r < |b|';
      if (b === 0n) { out.innerHTML = ''; status.textContent = 'b must not be 0 — division by zero has no quotient.'; return; }
      var q = a / b, r = a - q * b;
      if (r < 0n) { q -= (b > 0n ? 1n : -1n); r = a - q * b; }
      out.innerHTML = table(['a', 'b', 'q', 'r', 'check a = qb + r'],
        [row([a, b, q, r, q + '·' + b + ' + ' + r + ' = ' + (q * b + r)], true)]);
      k1L.textContent = 'remainder'; k1.textContent = r;
      k2L.textContent = 'quotient'; k2.textContent = q;
      status.innerHTML = 'The theorem says this q and r are <strong>unique</strong>: exactly one pair satisfies '
        + 'a = qb + r with 0 ≤ r &lt; |b|. The remainder is never negative here even when a is'
        + (a < 0n ? ' — the quotient rounded toward −∞ to make ' + r + ' land in [0, ' + (b < 0n ? -b : b) + ')' : '')
        + ' — which is why −7 mod 3 is 2, not −1.';
    },
    euclid: function (a, b) {
      show({ A: 'a', B: 'b' });
      title.textContent = 'Euclidean algorithm';
      sub.textContent = 'replace (a, b) by (b, a mod b) until b = 0';
      var rows = [], x = a < 0n ? -a : a, y = b < 0n ? -b : b, steps = 0;
      while (y !== 0n) {
        var q = x / y, r = x % y;
        rows.push(row([x, y, q, r], r === 0n));
        x = y; y = r; steps += 1;
        if (steps > 400) break;
      }
      out.innerHTML = table(['a', 'b', 'q = ⌊a/b⌋', 'r = a mod b'], rows);
      k1L.textContent = 'gcd'; k1.textContent = x;
      k2L.textContent = 'divisions'; k2.textContent = steps;
      status.innerHTML = 'gcd(' + a + ', ' + b + ') = <strong>' + x + '</strong> in ' + steps + ' division' + (steps === 1 ? '' : 's') + '. '
        + 'Each line is justified by one fact: gcd(a, b) = gcd(b, a mod b), because any common divisor of a and b '
        + 'divides a − qb. The gcd is the last <em>nonzero</em> remainder — the highlighted row\'s b, not its r. '
        + 'Listing divisors of ' + a + ' instead would take vastly longer.';
    },
    bezout: function (a, b) {
      show({ A: 'a', B: 'b' });
      title.textContent = 'Extended Euclidean algorithm';
      sub.textContent = 'every row keeps r = a·s + b·t';
      var e = egcdTrace(a, b);
      var A = a < 0n ? -a : a, B = b < 0n ? -b : b;
      var last = e.rows.length - 2;
      var rows = e.rows.map(function (rw, i) {
        return row([i, rw.r, rw.q === null ? '—' : rw.q, rw.s, rw.t,
                    A + '·(' + rw.s + ') + ' + B + '·(' + rw.t + ') = ' + (A * rw.s + B * rw.t)], i === last);
      });
      out.innerHTML = table(['row', 'r', 'q', 's', 't', 'check'], rows);
      k1L.textContent = 'gcd'; k1.textContent = e.g;
      k2L.textContent = 'x, y'; k2.textContent = e.x + ', ' + e.y;
      var inverse = '';
      if (e.g === 1n && B > 1n) {
        var red = ((e.x % B) + B) % B;
        inverse = ' Because the gcd is 1, x is an inverse of ' + a + ' modulo ' + B + '; reduced into [0, ' + B + ') it is <strong>'
          + red + '</strong>, and ' + a + '·' + red + ' = ' + (a * red) + ' ≡ 1 (mod ' + B + ').';
      } else if (e.g !== 1n && e.g !== 0n) {
        inverse = ' The gcd is ' + e.g + ', not 1, so ' + a + ' has no inverse modulo ' + B + ': there is no x with '
          + a + 'x ≡ 1, because every ' + a + 'x + ' + B + 'y is a multiple of ' + e.g + '.';
      }
      status.innerHTML = 'Bézout: <strong>' + a + '·(' + e.x + ') + ' + b + '·(' + e.y + ') = ' + e.g + '</strong>. '
        + 'The two starting rows are a = a·1 + b·0 and b = a·0 + b·1; each later row is the one above minus q times the one '
        + 'before it, in all three of r, s and t, so the check column holds on every line without back-substitution. '
        + 'The highlighted row is the last nonzero remainder.' + inverse;
    },
    modtable: function (a, b, m) {
      show({ M: 'm (modulus)' });
      title.textContent = 'Arithmetic modulo ' + m;
      sub.textContent = 'addition and multiplication tables';
      if (m < 2n || m > 16n) { out.innerHTML = ''; status.textContent = 'Choose a modulus between 2 and 16 so the tables fit.'; return; }
      var n = Number(m);
      function build(op, symbol) {
        var head = [symbol];
        for (var i = 0; i < n; i += 1) head.push(i);
        var rows = [];
        for (var r = 0; r < n; r += 1) {
          var cells = ['<strong>' + r + '</strong>'];
          for (var c = 0; c < n; c += 1) cells.push(op(r, c));
          rows.push(row(cells, false));
        }
        return table(head, rows);
      }
      out.innerHTML = '<div style="margin-bottom:14px;">' + build(function (x, y) { return (x + y) % n; }, '+')
        + '</div>' + build(function (x, y) { return (x * y) % n; }, '×');
      var units = [];
      for (var u = 1; u < n; u += 1) if (bgcd(BigInt(u), m) === 1n) units.push(u);
      k1L.textContent = 'units'; k1.textContent = units.length;
      k2L.textContent = 'prime?'; k2.textContent = isPrimeBig(m) ? 'yes' : 'no';
      status.innerHTML = 'The ' + units.length + ' elements with a multiplicative inverse are '
        + units.join(', ') + ' — exactly those coprime to ' + m + ', and their rows of the × table are permutations of 0 … ' + (n - 1) + '. '
        + (isPrimeBig(m)
            ? 'Because ' + m + ' is prime, every nonzero element is invertible, so this is a field.'
            : 'Because ' + m + ' is composite, some nonzero products are 0 (zero divisors), and those elements have no inverse.');
    },
    modexp: function (a, b, m) {
      show({ A: 'a (base)', B: 'b (exponent)', M: 'm (modulus)' });
      title.textContent = 'Modular exponentiation';
      sub.textContent = 'a^b mod m by repeated squaring';
      if (m < 2n) { out.innerHTML = ''; status.textContent = 'The modulus must be at least 2.'; return; }
      if (b < 0n) { out.innerHTML = ''; status.textContent = 'Use a non-negative exponent.'; return; }
      var tr = modpowTrace(a, b, m, 64);
      var rows = tr.rows.map(function (rw) {
        return row([rw.bit, rw.use ? '1' : '0', rw.power, rw.use ? rw.result : '—'], rw.use);
      });
      out.innerHTML = table(['bit of b', 'value', 'a^(2^bit) mod m', 'running result'], rows);
      var answer = modpow(a, b, m);
      k1L.textContent = 'a^b mod m'; k1.textContent = answer;
      k2L.textContent = 'squarings + mults'; k2.textContent = tr.squarings + ' + ' + tr.mults;
      var absA = a < 0n ? -a : a, digits = null;
      if (absA > 1n && b > 0n) {
        var est = Number(b) * Math.log10(Number(absA));
        digits = isFinite(est) ? Math.floor(est) + 1 : null;
      }
      status.innerHTML = '<strong>' + a + '^' + b + ' mod ' + m + ' = ' + answer + '</strong>, found in '
        + tr.squarings + ' squaring' + (tr.squarings === 1 ? '' : 's') + ' and ' + tr.mults + ' multiplication'
        + (tr.mults === 1 ? '' : 's') + ' — one squaring per row except the last, whose square is never used, and one '
        + 'multiplication per set bit — rather than ' + (b > 0n ? (b - 1n) : 0n) + ' multiplications the naive way. '
        + 'Reducing mod m at every step keeps every intermediate below m² = ' + (m * m) + '; '
        + (digits !== null
            ? a + '^' + b + ' itself has ' + (digits > 1e9 ? 'more than a billion' : digits.toLocaleString('en-GB')) + ' digits.'
            : 'the power itself is not the point.')
        + (tr.complete ? '' : ' Only the first 64 bits of the exponent are shown; the result in the corner uses them all.');
    },
    congr: function (a, b, m) {
      show({ A: 'a (coefficient)', B: 'b (right-hand side)', M: 'm (modulus)' });
      title.textContent = 'Linear congruence';
      sub.textContent = 'ax ≡ b (mod m)';
      if (m < 2n) { out.innerHTML = ''; status.textContent = 'The modulus must be at least 2.'; return; }
      var g = bgcd(((a % m) + m) % m, m);
      var solutions = [];
      if (((b % g) + g) % g === 0n) {
        var m2 = m / g, a2 = (((a / g) % m2) + m2) % m2, b2 = (((b / g) % m2) + m2) % m2;
        var inv = m2 === 1n ? 0n : modinv(a2, m2);
        if (inv !== null) {
          var x0 = ((b2 * inv) % m2 + m2) % m2;
          for (var i = 0n; i < g; i += 1n) solutions.push((x0 + i * m2) % m);
        }
      }
      var rows = solutions.length
        ? solutions.map(function (x) { return row([x, ((a * x) % m + m) % m, ((b % m) + m) % m, '✓'], true); })
        : [row(['none', '—', ((b % m) + m) % m, 'no solution'], true)];
      out.innerHTML = table(['x', 'ax mod m', 'b mod m', ''], rows);
      k1L.textContent = 'gcd(a, m)'; k1.textContent = g;
      k2L.textContent = 'solutions'; k2.textContent = solutions.length;
      status.innerHTML = solutions.length
        ? 'gcd(a, m) = ' + g + ' divides b, so there are exactly <strong>' + g + '</strong> solution' + (g === 1n ? '' : 's') + ' modulo ' + m
          + (g === 1n ? '' : ', spaced ' + (m / g) + ' apart') + '. The count is the gcd — not one, and not m. '
          + (g === 1n ? 'Since the gcd is 1, a is invertible and x ≡ a⁻¹b.'
                      : 'Dividing a, b AND m by ' + g + ' gives ' + (a / g) + 'x ≡ ' + (b / g) + ' (mod ' + (m / g) + '), whose one solution lifts to these ' + g + '.')
        : 'gcd(a, m) = ' + g + ' does <strong>not</strong> divide ' + b + ', so there is <strong>no solution at all</strong>. '
          + 'That is the whole solvability criterion, and it is checkable before any work is done.';
    },
    crt: function (a, b, m, n) {
      show({ A: 'a₁ (remainder mod m₁)', B: 'a₂ (remainder mod m₂)', M: 'm₁', N: 'm₂' });
      title.textContent = 'Chinese remainder theorem';
      sub.textContent = 'x ≡ a₁ (mod m₁), x ≡ a₂ (mod m₂)';
      if (m < 2n || n < 2n) { out.innerHTML = ''; status.textContent = 'Both moduli must be at least 2.'; return; }
      var sol = crtPair(a, m, b, n);
      var m1 = m, m2 = n, r1 = sol.r1, r2 = sol.r2;
      if (sol.g === 1n) {
        var M = m1 * m2;
        var inv1 = modinv(m2 % m1, m1), inv2 = modinv(m1 % m2, m2);
        var t1 = r1 * m2 * inv1 % M, t2 = r2 * m1 * inv2 % M;
        var rows = [
          row(['x ≡ ' + r1 + ' (mod ' + m1 + ')', m2, inv1, t1, (t1 % m1) + ', ' + (t1 % m2)], false),
          row(['x ≡ ' + r2 + ' (mod ' + m2 + ')', m1, inv2, t2, (t2 % m1) + ', ' + (t2 % m2)], false),
          row(['<strong>x</strong>', '', '', '<strong>' + sol.x + ' (mod ' + M + ')</strong>', (sol.x % m1) + ', ' + (sol.x % m2)], true)
        ];
        out.innerHTML = table(['congruence', 'Mᵢ = M/mᵢ', 'yᵢ = Mᵢ⁻¹ mod mᵢ', 'term aᵢMᵢyᵢ mod M', 'mod m₁, mod m₂'], rows);
        k1L.textContent = 'x'; k1.textContent = sol.x;
        k2L.textContent = 'modulus'; k2.textContent = M;
        status.innerHTML = 'gcd(' + m1 + ', ' + m2 + ') = 1, so the theorem applies: <strong>x = ' + sol.x + '</strong>, unique modulo '
          + M + '. The last column is the point of the construction — each term is 0 modulo the other modulus and the right '
          + 'remainder modulo its own, so adding them cannot spoil either congruence. Check: ' + sol.x + ' mod ' + m1 + ' = '
          + (sol.x % m1) + ' and ' + sol.x + ' mod ' + m2 + ' = ' + (sol.x % m2) + '.';
        return;
      }
      var rowsN = [
        row(['x ≡ ' + r1 + ' (mod ' + m1 + ')', r1 % sol.g], false),
        row(['x ≡ ' + r2 + ' (mod ' + m2 + ')', r2 % sol.g], false)
      ];
      if (sol.x !== null) rowsN.push(row(['<strong>x</strong>', '<strong>' + sol.x + ' (mod ' + sol.lcm + ')</strong>'], true));
      else rowsN.push(row(['<strong>x</strong>', '<strong>no solution</strong>'], true));
      out.innerHTML = table(['congruence', 'remainder mod gcd = ' + sol.g], rowsN);
      k1L.textContent = 'x'; k1.textContent = sol.x === null ? 'none' : sol.x;
      k2L.textContent = 'modulus'; k2.textContent = sol.x === null ? '—' : sol.lcm;
      status.innerHTML = 'gcd(' + m1 + ', ' + m2 + ') = ' + sol.g + ', so the theorem does <strong>not</strong> apply. '
        + (sol.x === null
            ? 'The system is <strong>inconsistent</strong>: any x has one remainder modulo ' + sol.g + ', but the two congruences demand '
              + (r1 % sol.g) + ' and ' + (r2 % sol.g) + '. No integer satisfies both.'
            : 'The remainders agree modulo ' + sol.g + ' (both ' + (r1 % sol.g) + '), so the system is consistent, and its solution '
              + '<strong>x = ' + sol.x + '</strong> is unique modulo lcm(' + m1 + ', ' + m2 + ') = ' + sol.lcm + ' — not modulo the product '
              + (m1 * m2) + ', which would list ' + (m1 * m2 / sol.lcm) + ' copies of the same answer. Check: ' + sol.x + ' mod ' + m1 + ' = '
              + (sol.x % m1) + ' and ' + sol.x + ' mod ' + m2 + ' = ' + (sol.x % m2) + '.');
    },
    fermat: function (a, b, m) {
      show({ A: 'a (base)', M: 'm (modulus)' });
      title.textContent = "Fermat's little theorem and Euler's theorem";
      sub.textContent = 'a^φ(m) ≡ 1 (mod m) when gcd(a, m) = 1';
      if (m < 2n) { out.innerHTML = ''; status.textContent = 'The modulus must be at least 2.'; return; }
      if (tooBig(m)) { refuse('m = ' + m); return; }
      var fac = factorize(m), prime = fac.length === 1 && fac[0][1] === 1n;
      var phi = totient(m);
      var base = ((a % m) + m) % m;
      var coprime = bgcd(base, m) === 1n;
      var limit = coprime ? Number(phi < 23n ? phi + 1n : 24n) : Number(m < 14n ? m : 14n);
      var rows = [], order = -1;
      for (var e = 1; e <= limit; e += 1) {
        var v = modpow(base, BigInt(e), m);
        if (v === 1n && order < 0) order = e;
        rows.push(row([e, v, v === 1n ? '← 1' : (e === Number(phi) ? '← e = φ(m)' : '')], v === 1n));
      }
      if (coprime && order < 0) {
        var cap = phi < 200000n ? phi : 200000n;
        for (var e2 = BigInt(limit + 1); e2 <= cap; e2 += 1n) if (modpow(base, e2, m) === 1n) { order = Number(e2); break; }
      }
      out.innerHTML = table(['e', a + '^e mod ' + m, ''], rows);
      k1L.textContent = 'φ(m)'; k1.textContent = phi;
      k2L.textContent = 'a^φ(m) mod m'; k2.textContent = coprime ? modpow(base, phi, m) : 'not 1 — ever';
      var formula = prime
        ? 'φ(' + m + ') = ' + m + ' − 1 = ' + phi + ' because ' + m + ' is prime'
        : 'φ(' + m + ') = ' + m + fac.map(function (pe) { return '·(1 − 1/' + pe[0] + ')'; }).join('') + ' = ' + phi
          + ', from ' + m + ' = ' + fac.map(function (pe) { return pe[0] + (pe[1] > 1n ? '^' + pe[1] : ''); }).join(' · ');
      status.innerHTML = coprime
        ? formula + '. gcd(' + a + ', ' + m + ') = 1, so the theorem applies and ' + a + '^' + phi + ' ≡ '
          + modpow(base, phi, m) + ' (mod ' + m + '). '
          + (prime ? 'With a prime modulus this is Fermat\'s little theorem, the special case φ(p) = p − 1. '
                   : 'With a composite modulus Fermat says nothing; Euler still does, and φ(m) counts the units, not m − 1. ')
          + (order > 0
              ? 'The powers first return to 1 at e = ' + order + ', the <strong>order</strong> of ' + a + ', which divides φ(m)'
                + (order > limit ? ' — beyond the rows shown.' : '.')
              : 'The order of ' + a + ' is beyond what this table searches.')
        : formula + '. But <strong>gcd(' + a + ', ' + m + ') = ' + bgcd(base, m) + ' ≠ 1</strong>, so neither theorem applies: '
          + 'both require a coprime to the modulus, and no power of ' + a + ' can ever be 1 mod ' + m + ', because every power '
          + 'shares that factor with ' + m + '.';
    },
    sieve: function (a, b, m) {
      show({ A: 'N (sieve up to)' });
      title.textContent = 'Sieve of Eratosthenes';
      sub.textContent = 'cross out the multiples of each prime in turn';
      var N = clamp(Number(a), 10, 200);
      var composite = new Array(N + 1).fill(false), killedBy = new Array(N + 1).fill(0);
      for (var p = 2; p * p <= N; p += 1) {
        if (composite[p]) continue;
        for (var q = p * p; q <= N; q += p) if (!composite[q]) { composite[q] = true; killedBy[q] = p; }
      }
      var cells = '';
      var primes = 0;
      for (var i = 2; i <= N; i += 1) {
        if (!composite[i]) primes += 1;
        cells += '<span class="chip' + (composite[i] ? '' : ' ok') + '" title="'
          + (composite[i] ? 'first crossed out as a multiple of ' + killedBy[i] : 'prime') + '">' + i + '</span>';
      }
      out.innerHTML = '<div>' + cells + '</div>';
      k1L.textContent = 'primes ≤ N'; k1.textContent = primes;
      k2L.textContent = 'N'; k2.textContent = N;
      status.innerHTML = 'There are <strong>' + primes + '</strong> primes up to ' + N + '. Sieving stops at √N = '
        + Math.floor(Math.sqrt(N)) + ': any composite has a factor no larger than its square root, so anything still '
        + 'standing after that is prime. Hover a crossed-out number to see which prime removed it.'
        + (N < 10 || N > 200 ? '' : (Number(a) !== N ? ' N is kept between 10 and 200 so the chips fit.' : ''));
    },
    factor: function (a) {
      show({ A: 'n' });
      title.textContent = 'Prime factorisation';
      sub.textContent = 'the unique decomposition guaranteed by the fundamental theorem';
      var n = a < 0n ? -a : a;
      if (n < 2n) { out.innerHTML = ''; status.textContent = 'Factorisation is defined for integers greater than 1.'; return; }
      if (tooBig(n)) { refuse('n = ' + n); return; }
      var fac = factorize(n), rows = [], parts = [], left = n;
      fac.forEach(function (pe, i) {
        for (var k = 0n; k < pe[1]; k += 1n) left /= pe[0];
        rows.push(row([pe[0], pe[1], left], i === fac.length - 1));
        parts.push(pe[0] + (pe[1] > 1n ? '^' + pe[1] : ''));
      });
      out.innerHTML = table(['prime', 'exponent', 'remaining'], rows);
      k1L.textContent = 'distinct primes'; k1.textContent = fac.length;
      k2L.textContent = 'divisors'; k2.textContent = divisorCount(n);
      status.innerHTML = '<strong>' + n + ' = ' + parts.join(' · ') + '</strong>. '
        + 'The fundamental theorem of arithmetic says this decomposition exists and is unique up to order — '
        + 'which is exactly what makes the exponent counting (' + fac.map(function (pe) { return '(' + pe[1] + '+1)'; }).join('')
        + ' = ' + divisorCount(n) + ') give the number of divisors.'
        + (fac.length === 1 && fac[0][1] === 1n ? ' ' + n + ' is prime: nothing up to √' + n + ' divided it.' : '');
    },
    lcg: function (a, c, m, seed) {
      show({ A: 'a (multiplier)', B: 'c (increment)', M: 'm (modulus)', N: 'x₀ (seed)' });
      title.textContent = 'Linear congruential generator';
      sub.textContent = 'xₙ₊₁ = (a·xₙ + c) mod m';
      if (m < 2n) { out.innerHTML = ''; status.textContent = 'The modulus must be at least 2.'; return; }
      if (tooBig(m)) { refuse('m = ' + m); return; }
      var run = lcgRun(a, c, m, seed, Number(m < 5000n ? m + 1n : 5000n));
      var shown = Math.min(run.seq.length, 40);
      var rows = [];
      for (var i = 0; i < shown; i += 1) rows.push(row([i, run.seq[i], i === run.start ? '← the cycle starts here' : ''], i === run.start));
      if (shown < run.seq.length) rows.push(row(['…', '…', (run.seq.length - shown) + ' more value' + (run.seq.length - shown === 1 ? '' : 's')], false));
      rows.push(row([run.seq.length, run.next, run.start >= 0 ? '= x' + run.start + ', repeats' : 'not yet repeated'], true));
      out.innerHTML = table(['n', 'xₙ', ''], rows);
      var hd = hullDobell(a, c, m), full = run.period === Number(m) && run.start === 0;
      k1L.textContent = 'period'; k1.textContent = run.period < 0 ? '> ' + run.seq.length : run.period;
      k2L.textContent = 'distinct values'; k2.textContent = run.seq.length + ' of ' + m;
      var primes = factorize(m).map(function (pe) { return pe[0]; });
      var checks = '<br />Hull–Dobell: gcd(c, m) = gcd(' + c + ', ' + m + ') = ' + bgcd(c, m) + (hd[0] ? ' ✓' : ' ✗')
        + '; a − 1 = ' + (a - 1n) + ' divisible by every prime of m (' + primes.join(', ') + ')' + (hd[1] ? ' ✓' : ' ✗')
        + '; ' + (m % 4n === 0n ? '4 | m, so 4 | a − 1 needed' + (hd[2] ? ' ✓' : ' ✗') : '4 ∤ m, third condition vacuous ✓') + '.';
      status.innerHTML = (run.period < 0
        ? 'No repeat within ' + run.seq.length + ' values; the period is longer than this lab follows.'
        : full
          ? '<strong>Full period ' + m + '</strong>: every residue appears once and the sequence returns to the seed.'
          : 'Period <strong>' + run.period + '</strong>' + (run.start > 0 ? ' after a tail of ' + run.start + ' value' + (run.start === 1 ? '' : 's') + ' the cycle never revisits' : '')
            + ' — out of ' + m + ' possible values, so most of the range is never produced.')
        + checks
        + (hd[0] && hd[1] && hd[2]
            ? ' All three hold, so the theorem promises full period from <em>every</em> seed.'
            : ' A condition fails, so the theorem promises nothing — and the period above shows what that costs.');
    },
    affine: function (a, b) {
      show({ A: 'a (multiplier)', B: 'b (shift)' });
      title.textContent = 'Affine cipher';
      sub.textContent = 'E(x) = (a·x + b) mod 26 on A = 0 … Z = 25';
      var M = 26n, am = affineMap(a, b, M), g = bgcd(a, M);
      var counts = {};
      am.map.forEach(function (y) { counts[y.toString()] = (counts[y.toString()] || 0) + 1; });
      var chips = '';
      for (var x = 0n; x < M; x += 1n) {
        var y = am.map[Number(x)], clash = counts[y.toString()] > 1;
        chips += '<span class="chip' + (clash ? ' no' : (x === 7n || x === 4n || x === 19n ? ' hi' : '')) + '" title="'
          + letter(x) + ' = ' + x + ' → ' + a + '·' + x + ' + ' + b + ' = ' + (a * x + b) + ' ≡ ' + y + ' = ' + letter(y) + '">'
          + letter(x) + '→' + letter(y) + '</span>';
      }
      out.innerHTML = '<div>' + chips + '</div>';
      k1L.textContent = 'gcd(a, 26)'; k1.textContent = g;
      k2L.textContent = 'a⁻¹ mod 26'; k2.textContent = am.inv === null ? 'none' : am.inv;
      var H = am.map[7];
      status.innerHTML = (am.inv !== null
        ? 'gcd(' + a + ', 26) = 1, so all <strong>26</strong> ciphertext letters are distinct and the cipher can be undone: '
          + 'a⁻¹ ≡ ' + am.inv + ' (' + a + '·' + am.inv + ' = ' + (a * am.inv) + ' ≡ 1), so D(y) = ' + am.inv + '·(y − ' + b + ') mod 26. '
          + 'H = 7 encrypts to ' + a + '·7 + ' + b + ' = ' + (a * 7n + b) + ' ≡ ' + H + ' = ' + letter(H) + ', and D(' + H + ') = '
          + am.inv + '·(' + H + ' − ' + b + ') ≡ ' + ((((H - b) * am.inv) % M) + M) % M + ' = H again.'
        : '<strong>gcd(' + a + ', 26) = ' + g + ' ≠ 1</strong>, so ' + a + ' has no inverse modulo 26 and this is not a cipher: only '
          + am.distinct + ' distinct ciphertext letter' + (am.distinct === 1 ? '' : 's') + ' appear' + (am.distinct === 1 ? 's' : '')
          + ', the red chips share their output with another letter, and no decryption rule exists — the map is not injective.')
        + ' Hover a chip for its arithmetic; E, H and T are marked.';
    }
  };

  function redraw() {
    var a, b, m, n;
    try {
      a = BigInt(aIn.value || '0'); b = BigInt(bIn.value || '0'); m = BigInt(mIn.value || '2'); n = BigInt(nIn.value || '2');
    } catch (e) {
      status.textContent = 'Enter whole numbers.';
      return;
    }
    MODES[modeSel.value](a, b, m, n);
  }

  [aIn, bIn, mIn, nIn].forEach(function (el) { el.addEventListener('input', redraw); });
  modeSel.addEventListener('change', function () {
    var d = DEFAULTS[modeSel.value];
    if (d) { aIn.value = d[0]; bIn.value = d[1]; mIn.value = d[2]; nIn.value = d[3]; }
    redraw();
  });

  var DEFAULTS = {
    div: [1071, 462, 26, 5], euclid: [1071, 462, 26, 5], bezout: [1071, 462, 26, 5],
    modtable: [3, 5, 12, 5], modexp: [7, 128, 13, 5], congr: [6, 9, 15, 5],
    crt: [2, 3, 3, 5], fermat: [7, 0, 13, 5], sieve: [100, 0, 26, 5], factor: [360, 0, 26, 5],
    lcg: [5, 3, 16, 1], affine: [5, 8, 26, 5]
  };

  modeSel.value = """ + '"%s"' % cfg.get("mode", "euclid") + r""";
  (function () {
    var d = (DEFAULTS[modeSel.value] || DEFAULTS.euclid).slice();
    if (PRESET.a !== undefined) d[0] = PRESET.a;
    if (PRESET.b !== undefined) d[1] = PRESET.b;
    if (PRESET.m !== undefined) d[2] = PRESET.m;
    if (PRESET.n !== undefined) d[3] = PRESET.n;
    aIn.value = d[0]; bIn.value = d[1]; mIn.value = d[2]; nIn.value = d[3];
  })();
  """ + (cfg.get("overrides_js") or "") + r"""
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="Number theory workbench",
        subtitle="Algorithms with their traces",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Choose an algorithm"),
        panel_intro=cfg.get(
            "panel_intro",
            "Every mode prints the steps, not only the answer, so the method is "
            "something you can carry to paper.",
        ),
        script=script,
    )


def rsa_lab(cfg):
    """RSA end to end on numbers small enough to check by hand.

    The keys are GENERATED from the primes you choose, the message is actually
    encrypted and decrypted, and the lab shows that d is recoverable by
    factoring n -- which is the honest way to teach why the real thing uses
    primes with hundreds of digits rather than two-digit ones.
    """
    markup = """      <div class="lab-toolbar">
        <div class="lab-title"><strong>RSA with small primes</strong><span>Key generation, encryption, decryption, and the attack</span></div>
        <div class="inline-legend"><span class="tone-cyan"><i class="legend-swatch"></i>public</span><span class="tone-red"><i class="legend-swatch"></i>private</span></div>
      </div>
      <div class="lab-stage"><div class="table-wrap" id="rsaOut"></div></div>
      <div class="status-banner" id="rsaStatus" style="margin-top:12px;"></div>"""
    controls = """        <div class="field">
          <label for="rsaP">p (prime)</label>
          <input id="rsaP" type="number" value="61" />
        </div>
        <div class="field">
          <label for="rsaQ">q (prime)</label>
          <input id="rsaQ" type="number" value="53" />
        </div>
        <div class="field">
          <label for="rsaE">e (public exponent, coprime to &phi;(n))</label>
          <input id="rsaE" type="number" value="17" />
        </div>
        <div class="field">
          <label for="rsaM">m (message, 0 &le; m &lt; n)</label>
          <input id="rsaM" type="number" value="65" />
        </div>
        <div class="kpi-grid">
          <div class="kpi"><span>n = pq</span><strong id="rsaN">&mdash;</strong></div>
          <div class="kpi"><span>&phi;(n)</span><strong id="rsaPhi">&mdash;</strong></div>
          <div class="kpi"><span>d</span><strong id="rsaD">&mdash;</strong></div>
        </div>"""

    script = NT_JS + r"""
  var pIn = document.getElementById('rsaP'), qIn = document.getElementById('rsaQ');
  var eIn = document.getElementById('rsaE'), mIn = document.getElementById('rsaM');
  var out = document.getElementById('rsaOut'), status = document.getElementById('rsaStatus');
  /* Above this the attack below -- trial division to sqrt(n) -- takes seconds
     rather than microseconds, and a reader who typed a 12-digit prime would
     freeze the page for hours. Refusing says why, which is lesson 14's point. */
  var PRIME_LIMIT = 10000000n;

  function redraw() {
    var p, q, e, m;
    try {
      p = BigInt(pIn.value || '0'); q = BigInt(qIn.value || '0');
      e = BigInt(eIn.value || '0'); m = BigInt(mIn.value || '0');
    } catch (err) { status.textContent = 'Enter whole numbers.'; return; }

    if (p > PRIME_LIMIT || q > PRIME_LIMIT || p < 0n || q < 0n) {
      out.innerHTML = '';
      status.innerHTML = '<strong>Keep both primes below 10<sup>7</sup>.</strong> The attack at the end of this lab is trial '
        + 'division up to √n, which finishes in under a second at that size and would take days at 10<sup>15</sup> and '
        + 'longer than the universe at 1024 bits. That climb is the whole security argument; freezing the page does not '
        + 'demonstrate it any better.';
      return;
    }
    if (!isPrimeBig(p) || !isPrimeBig(q)) {
      out.innerHTML = '';
      status.innerHTML = '<strong>p and q must both be prime.</strong> '
        + (isPrimeBig(p) ? q + ' is not.' : p + ' is not.')
        + ' RSA rests on φ(n) = (p−1)(q−1), and that formula is only correct for two distinct primes.';
      return;
    }
    if (p === q) {
      out.innerHTML = '';
      status.innerHTML = '<strong>p and q must be different.</strong> With p = q, φ(n) = p(p−1), not (p−1)², '
        + 'and n = p² is trivially factorable by taking a square root.';
      return;
    }
    var n = p * q, phi = (p - 1n) * (q - 1n);
    if (e < 2n || bgcd(e, phi) !== 1n) {
      out.innerHTML = '';
      status.innerHTML = '<strong>e = ' + e + ' is not a valid public exponent' + (e < 2n ? ': it must exceed 1.' : ' — it is not coprime to φ(n) = ' + phi + '</strong> (their gcd is '
        + bgcd(e, phi) + '), so e has no inverse mod φ(n) and no decryption exponent exists. ')
        + 'Try 17, or 65537, or any number coprime to ' + phi + ' — e does not have to be prime, only coprime to φ(n).';
      return;
    }
    var d = modinv(e, phi);
    if (m < 0n || m >= n) {
      out.innerHTML = '';
      status.innerHTML = '<strong>The message must satisfy 0 ≤ m &lt; n = ' + n + '.</strong> '
        + 'Anything larger is indistinguishable from m mod n after encryption — which is why real messages '
        + 'are split into blocks smaller than the modulus.';
      return;
    }

    var c = modpow(m, e, n), back = modpow(c, d, n);

    /* The attack, run for real: factor n by trial division, recompute phi,
       recompute d. On these primes it takes microseconds, and that is the
       point being made. */
    var t0 = (typeof performance !== 'undefined' && performance.now) ? performance.now() : 0;
    var f = 0n;
    for (var t = 2n; t * t <= n; t += 1n) if (n % t === 0n) { f = t; break; }
    var t1 = (typeof performance !== 'undefined' && performance.now) ? performance.now() : 0;
    var recovered = f ? modinv(e, (f - 1n) * (n / f - 1n)) : null;

    var rows = [
      ['p, q', p + ', ' + q, 'private — the only secret that matters'],
      ['n = pq', n.toString(), 'public'],
      ['φ(n) = (p−1)(q−1)', phi.toString(), 'private (computable from p and q)'],
      ['e', e.toString(), 'public, coprime to φ(n)'],
      ['d = e⁻¹ mod φ(n)', d.toString(), 'private; check: ed mod φ(n) = ' + (e * d % phi)],
      ['message m', m.toString(), ''],
      ['ciphertext c = mᵉ mod n', c.toString(), 'what an eavesdropper sees'],
      ['decrypted cᵈ mod n', back.toString(), back === m ? 'matches m' : 'DOES NOT match m']
    ];
    out.innerHTML = '<table class="tt"><thead><tr><th>quantity</th><th>value</th><th>role</th></tr></thead><tbody>'
      + rows.map(function (r, i) {
          return '<tr' + (i === 7 ? ' class="focus"' : '') + '><td>' + r[0] + '</td><td>' + r[1] + '</td><td>' + r[2] + '</td></tr>';
        }).join('') + '</tbody></table>';

    document.getElementById('rsaN').textContent = n;
    document.getElementById('rsaPhi').textContent = phi;
    document.getElementById('rsaD').textContent = d;

    status.innerHTML = (back === m
      ? 'Decryption returned the original message, and it did so because of Euler\'s theorem: '
        + 'ed ≡ 1 (mod φ(n)) makes m^(ed) ≡ m (mod n). '
      : '<span class="tone-red">Decryption did not return m.</span> ')
      + '<br /><strong>Now the attack.</strong> This lab factored n = ' + n + ' by trial division in '
      + (f ? Math.max(0.001, (t1 - t0)).toFixed(3) + ' ms, finding p = ' + f + ', and recomputed d = ' + recovered
          + ' — the private key, from public information alone.' : 'no time at all.')
      + ' Nothing about the method resists that; only the SIZE of the primes does. Production keys use primes of '
      + 'about 1024 bits each, where the same trial division would outlast the universe.';
  }

  [pIn, qIn, eIn, mIn].forEach(function (el) { el.addEventListener('input', redraw); });
  redraw();
  window.redrawLab = redraw;
"""
    return Lab(
        title="RSA, generated and broken",
        subtitle="Small enough to check by hand",
        markup=markup,
        controls=controls,
        panel_title=cfg.get("panel_title", "Choose the primes"),
        panel_intro=cfg.get(
            "panel_intro",
            "Every value below is computed from the four inputs. The last paragraph "
            "recovers the private key by factoring, because that is the honest way "
            "to show what the security actually rests on.",
        ),
        script=script,
    )
