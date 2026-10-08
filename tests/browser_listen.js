// Listen (scripts/mathpath/readout.py) in a real Chrome, with the speech engine
// replaced by a recorder: what is queued, in what order, and what the controls do.
// Not part of the unit suite (it launches Chrome); run it after touching readout.py:
//
//     node tests/browser_listen.js            # writes screenshots to $LISTEN_OUT or /tmp
'use strict';
const fs = require('node:fs'), path = require('node:path'), http = require('node:http');
const {launch, sleep} = require('./browser_cdp');

const ROOT = path.resolve(__dirname, '..'), SITE = path.join(ROOT, 'site');
const OUT = process.env.LISTEN_OUT || fs.mkdtempSync('/tmp/listen-');
const PAGES = [
  ['generated', '/sets-relations-functions/the-pigeonhole-principle/'],
  ['generated', '/sequences-and-series/infinite-geometric-series/'],
  ['trading', '/market-structure/market-structure/'],
];
// A recorder in place of window.speechSynthesis. Utterances end only when the
// test says so (or immediately, in auto mode), so the controls can be driven.
const FAKE = `
  window.__said = []; window.__auto = false; window.__last = null;
  const fake = { getVoices() { return []; }, speak(u) {
      window.__said.push(u.text); window.__rate = u.rate; window.__last = u;
      setTimeout(() => { u.onstart && u.onstart({}); if (window.__auto) setTimeout(() => u.onend && u.onend({}), 1); }, 1);
    }, cancel() {}, pause() {}, resume() {}, addEventListener() {} };
  Object.defineProperty(window, 'speechSynthesis', {value: fake, configurable: true});
  window.__end = () => { const u = window.__last; u && u.onend && u.onend({}); };`;
// Several voices of mixed quality, and an utterance class that accepts plain
// objects as voices (the real one only takes SpeechSynthesisVoice instances).
const VOICES = FAKE.replace('getVoices() { return []; }', `getVoices() { return [
    {name: 'eSpeak English', lang: 'en', localService: true, default: true, voiceURI: 'espeak'},
    {name: 'Microsoft Zira - English (United States)', lang: 'en-US', localService: true, voiceURI: 'zira'},
    {name: 'Google US English', lang: 'en-US', localService: false, voiceURI: 'google'},
    {name: 'Microsoft Aria Online (Natural) - English (United States)', lang: 'en-US', localService: false, voiceURI: 'aria'},
    {name: 'Thomas', lang: 'fr-FR', localService: true, voiceURI: 'thomas'}]; }`)
  + `window.SpeechSynthesisUtterance = function (t) { this.text = t; };
  const speak0 = window.speechSynthesis.speak;
  window.speechSynthesis.speak = function (u) { window.__voice = u.voice && u.voice.voiceURI; speak0.call(this, u); };`;
const NONE = `Object.defineProperty(window, 'speechSynthesis', {value: undefined, configurable: true});`;

const server = http.createServer((req, res) => {
  let file = path.join(SITE, decodeURIComponent(req.url.split('?')[0]));
  if (!file.startsWith(SITE)) { res.writeHead(403); return res.end(); }
  if (fs.existsSync(file) && fs.statSync(file).isDirectory()) file = path.join(file, 'index.html');
  try { res.setHeader('Content-Type', 'text/html; charset=utf-8'); res.end(fs.readFileSync(file)); }
  catch { res.writeHead(404); res.end(); }
});

const failures = [];
const check = (ok, what) => { if (!ok) failures.push(what); console.log((ok ? 'ok   ' : 'FAIL ') + what); };

async function withScript(c, source, fn) {
  const s = await c.send('Page.addScriptToEvaluateOnNewDocument', {source});
  try { return await fn(); } finally { await c.send('Page.removeScriptToEvaluateOnNewDocument', {identifier: s.identifier}); }
}

async function main() {
  await new Promise(r => server.listen(0, '127.0.0.1', r));
  const base = 'http://127.0.0.1:' + server.address().port;
  const c = await launch({dir: OUT, name: 'listen', base});
  try {
    for (const [kind, route] of PAGES) {
      const tag = kind + ' ' + route;
      await withScript(c, FAKE, () => c.navigate(route, {width: 1440, height: 900}));
      const btn = await c.evaluate(`(() => { const b = document.querySelector('.listen-start');
        return b && {text: b.textContent, inActions: !!b.closest('.hero-actions')}; })()`);
      check(btn && btn.text === 'Listen' && btn.inActions, tag + ': Listen button in the hero actions');

      // Controls, one utterance at a time.
      const h1 = await c.evaluate(`document.querySelector('main h1').textContent.trim()`);
      await c.evaluate(`document.querySelector('.listen-start').click()`); await sleep(30);
      let s = await c.evaluate(`({said: __said.slice(), bar: !document.querySelector('.listen-bar').hidden,
        status: document.querySelector('.listen-status').textContent,
        current: !!document.querySelector('.listen-current')})`);
      check(s.bar && s.said[0] === h1, tag + ': starts at the title, bar shown');
      check(/^1 of \d+$/.test(s.status) && s.current, tag + ': status and highlight');
      await c.evaluate(`__end()`); await sleep(30);
      check((await c.evaluate(`__said.length`)) === 2, tag + ': an ended utterance advances');
      const btns = `[...document.querySelectorAll('.listen-bar button')]`;
      await c.evaluate(`${btns}[2].click()`); await sleep(30);   // Next
      const afterNext = await c.evaluate(`document.querySelector('.listen-status').textContent`);
      await c.evaluate(`${btns}[0].click()`); await sleep(30);   // Back
      const afterBack = await c.evaluate(`document.querySelector('.listen-status').textContent`);
      check(parseInt(afterNext) === parseInt(afterBack) + 1, tag + ': Next and Back move one block (' + afterNext + ' / ' + afterBack + ')');
      await c.evaluate(`${btns}[3].click()`); await sleep(30);   // Speed
      const sp = await c.evaluate(`({label: ${btns}[3].textContent, stored: localStorage.getItem('learn-listen-rate'), rate: __rate})`);
      check(sp.label === '1.25×' && sp.stored === '1.25' && sp.rate === 1.25, tag + ': speed cycles, applies and is remembered');
      await c.evaluate(`${btns}[1].click()`); await sleep(30);   // Pause
      check((await c.evaluate(`${btns}[1].textContent`)) === 'Play', tag + ': pause');
      if (kind === 'generated' && route.includes('pigeonhole'))
        for (const theme of ['dark', 'light']) {
          await c.evaluate(`document.documentElement.dataset.theme = ${JSON.stringify(theme)}`); await sleep(50);
          const shot = await c.send('Page.captureScreenshot', {format: 'png'});
          fs.writeFileSync(path.join(OUT, 'bar-desktop-' + theme + '.png'), Buffer.from(shot.data, 'base64'));
        }
      await c.evaluate(`${btns}[4].click()`); await sleep(30);   // Stop
      check(await c.evaluate(`document.querySelector('.listen-bar').hidden && !document.querySelector('.listen-current')`),
            tag + ': stop hides the bar and the highlight');

      // The whole page, auto-advancing: what a listener actually hears.
      await c.evaluate(`__said.length = 0; __auto = true; document.querySelector('.listen-start').click()`);
      for (let i = 0; i < 400 && !(await c.evaluate(`document.querySelector('.listen-bar').hidden`)); i++) await sleep(20);
      const heard = await c.evaluate(`__said.slice()`);
      fs.writeFileSync(path.join(OUT, route.replace(/\W+/g, '_') + '.txt'), heard.join('\n') + '\n');
      check(heard.length > 10, tag + ': reads the whole page (' + heard.length + ' utterances)');
      check(await c.evaluate(`document.querySelector('.listen-bar').hidden`), tag + ': finishes and hides the bar');
      // Text only the lab holds; a heading the lab shares with the lesson does not count.
      const [lab, rest] = await c.evaluate(`(() => { const l = document.querySelector('#lab'); if (!l) return ['', ''];
        const m = document.querySelector('main').cloneNode(true); m.querySelector('#lab').remove();
        return [l.textContent, m.textContent]; })()`);
      const leaked = heard.filter(t => t.length > 25 && lab.includes(t) && !rest.includes(t));
      check(!leaked.length, tag + ': nothing from the lab is read' + (leaked.length ? ' ' + JSON.stringify(leaked[0]) : ''));
      const symbols = heard.filter(t => /[∀∃∈∪∩≤≥≠√Σ∑⟹→ℕℤℝ²³ⁿ₁₂ₙ|^_]/.test(t));
      if (kind === 'generated') check(!symbols.length, tag + ': no raw math symbols reach the voice' + (symbols.length ? ' ' + JSON.stringify(symbols[0]) : ''));
      const long = heard.filter(t => t.length > 400);
      check(!long.length, tag + ': utterances are short enough for a network voice');
      check(!c.events.exceptions.length, tag + ': no script errors');
      check(c.events.requests.every(r => r.url === base + route), tag + ': no request beyond the document');
    }

    // Phone width, light theme: the bar must fit.
    await withScript(c, FAKE, () => c.navigate(PAGES[0][1], {width: 390, height: 844, theme: 'system-light'}));
    await c.evaluate(`document.querySelector('.listen-start').click()`); await sleep(50);
    const fit = await c.evaluate(`(() => { const r = document.querySelector('.listen-bar').getBoundingClientRect();
      return r.left >= 0 && r.right <= innerWidth && document.documentElement.scrollWidth <= innerWidth; })()`);
    check(fit, 'phone: the bar fits the viewport with no horizontal scroll');
    const shot = await c.send('Page.captureScreenshot', {format: 'png'});
    fs.writeFileSync(path.join(OUT, 'bar-phone-light.png'), Buffer.from(shot.data, 'base64'));

    // Voice choice: the best-sounding voice in the page language first, the
    // reader's choice applied and remembered across a reload.
    await withScript(c, VOICES, () => c.navigate(PAGES[0][1], {width: 1440, height: 900}));
    await c.evaluate(`document.querySelector('.listen-start').click()`); await sleep(30);
    let v = await c.evaluate(`({voice: __voice, shown: !document.querySelector('.listen-voice').hidden,
      options: [...document.querySelectorAll('.listen-voice option')].map(o => o.textContent)})`);
    check(v.voice === 'aria', 'voices: a natural voice is chosen over eSpeak and the default (' + v.voice + ')');
    check(v.shown && v.options.length === 4 && v.options[0] === 'Aria Online (Natural)' && v.options[3] === 'eSpeak English',
          'voices: picker lists the page-language voices, best first ' + JSON.stringify(v.options));
    await c.evaluate(`(() => { const s = document.querySelector('.listen-voice'); s.selectedIndex = 2;
      s.dispatchEvent(new Event('change')); })()`); await sleep(30);
    v = await c.evaluate(`({voice: __voice, stored: localStorage.getItem('learn-listen-voice')})`);
    check(v.voice === 'zira' && v.stored === 'zira', 'voices: a chosen voice is applied and stored');
    const kept = await withScript(c, VOICES, async () => {
      await c.send('Page.reload'); await sleep(600);
      await c.evaluate(`document.querySelector('.listen-start').click()`); await sleep(30);
      return c.evaluate(`window.__voice`);
    });
    check(kept === 'zira', 'voices: the choice survives a reload (' + kept + ')');
    const fits = await withScript(c, VOICES, async () => {
      await c.navigate(PAGES[0][1], {width: 390, height: 844});
      await c.evaluate(`document.querySelector('.listen-start').click()`); await sleep(50);
      const shot = await c.send('Page.captureScreenshot', {format: 'png'});
      fs.writeFileSync(path.join(OUT, 'bar-phone-voices.png'), Buffer.from(shot.data, 'base64'));
      return c.evaluate(`(() => { const r = document.querySelector('.listen-bar').getBoundingClientRect();
        return r.left >= 0 && r.right <= innerWidth && document.documentElement.scrollWidth <= innerWidth; })()`);
    });
    check(fits, 'voices: the bar with a picker fits a phone');

    // No speech engine: no button, no error.
    await withScript(c, NONE, () => c.navigate(PAGES[0][1], {width: 1440, height: 900}));
    check(!(await c.evaluate(`!!document.querySelector('.listen-start')`)) && !c.events.exceptions.length,
          'no speech engine: no Listen button, no error');
  } finally {
    await c.close(); server.close();
  }
  console.log(failures.length ? failures.length + ' FAILED' : 'all passed', '-- output in', OUT);
  process.exit(failures.length ? 1 : 0);
}
main().catch(e => { console.error(e); process.exit(2); });
