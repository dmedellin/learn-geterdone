import React from 'react';
import { AbsoluteFill, interpolate, useCurrentFrame } from 'remotion';
import { C, MONO, useBox } from '../theme';
import type { Scene } from '../types';

const KW: Record<string, Set<string>> = {
  python: new Set('def return if elif else while for in not and or is None True False import from class lambda with as pass break continue'.split(' ')),
  java: new Set('abstract class interface extends implements final private public protected static void return if else while for new null this super true false int long boolean String var import package try catch throw throws'.split(' ')),
  csharp: new Set('public private static class return if else while for foreach in new var int long bool string void true false null'.split(' ')),
};
const BUILTIN = new Set('len max min range list dict set int str sorted enumerate Math'.split(' '));
const TOKEN = /(#.*$|\/\/.*$|@\w+)|("(?:[^"\\]|\\.)*"|'(?:[^'\\]|\\.)*')|(\b\d+\b)|([A-Za-z_]\w*)|(\s+)|(.)/g;

function colour(line: string, lang: string): React.ReactNode[] {
  const out: React.ReactNode[] = [];
  const kw = KW[lang] || new Set<string>();
  let m: RegExpExecArray | null;
  TOKEN.lastIndex = 0;
  let i = 0;
  while ((m = TOKEN.exec(line)) !== null) {
    const [tok, com, str, num, word] = m;
    let color: string = C.text;
    if (com) color = '#7d8590';
    else if (str) color = C.ok;
    else if (num) color = '#f7a26b';
    else if (word) {
      const next = line.slice(TOKEN.lastIndex).trimStart()[0];
      if (kw.has(word)) color = '#c39bff';
      else if (BUILTIN.has(word)) color = C.warn;
      else if (next === '(') color = C.accent;
    }
    out.push(<span key={i++} style={{ color }}>{tok}</span>);
    if (tok.length === 0) TOKEN.lastIndex++;
  }
  return out;
}

const CHAR = 0.602;

// The lesson's code; each focus range lights up as the voice reaches it.
export const CodeScene: React.FC<{ s: Extract<Scene, { kind: 'code' }> }> = ({ s }) => {
  const f = useCurrentFrame();
  const box = useBox();
  const panelW = box.wide ? 1500 : box.w;
  const longest = Math.max(...s.lines.map((l) => l.length), 10) + 4;
  const size = Math.min(box.wide ? 40 : 34, Math.floor((panelW - 80) / (longest * CHAR)));
  const active = s.focus.filter((x) => x.at !== null && f >= (x.at as number)).pop();
  const lit = active ? interpolate(f, [active.at as number, (active.at as number) + 6], [0, 1], { extrapolateRight: 'clamp' }) : 0;
  return (
    <AbsoluteFill>
      <div style={{ position: 'absolute', left: box.wide ? (1920 - panelW) / 2 : box.x, top: box.y + (box.wide ? 40 : 40), width: panelW, borderRadius: 26,
                    background: C.codeBg, border: `3px solid ${C.line}`, boxShadow: '0 30px 80px rgba(0,0,0,.5)', overflow: 'hidden' }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: 14, padding: '20px 32px', borderBottom: `2px solid ${C.line}` }}>
          {['#f08a8a', C.warn, C.ok].map((c) => <div key={c} style={{ width: 18, height: 18, borderRadius: 9, background: c, opacity: 0.8 }} />)}
          <div style={{ marginLeft: 14, fontSize: 28, color: C.muted, fontWeight: 700 }}>{s.label}</div>
        </div>
        <div style={{ padding: '24px 0 30px', fontFamily: MONO, fontSize: size, lineHeight: 1.55 }}>
          {s.lines.map((line, i) => {
            const n = s.firstLine + i;
            const inFocus = !!active && n >= active.a && n <= active.b;
            const appear = interpolate(f, [2 + i * 2, 8 + i * 2], [0, 1], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' });
            const dim = active && !inFocus ? 1 - 0.55 * lit : 1;
            return (
              <div key={i} style={{ display: 'flex', whiteSpace: 'pre', opacity: appear * dim, padding: '0 32px',
                                    background: inFocus ? `rgba(240,192,96,${0.16 * lit})` : 'transparent',
                                    boxShadow: inFocus ? `inset 8px 0 0 rgba(240,192,96,${lit})` : 'none' }}>
                <span style={{ color: '#5b6270', width: '3ch', flex: '0 0 auto' }}>{n}</span>
                <span>{colour(line, s.lang)}</span>
              </div>
            );
          })}
        </div>
      </div>
    </AbsoluteFill>
  );
};
