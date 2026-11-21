import React from 'react';
import { AbsoluteFill, interpolate, spring, useCurrentFrame, useVideoConfig } from 'remotion';
import { C, useBox } from '../theme';
import type { Scene } from '../types';

// Items arrive when the voice gets to them; the one being talked about is bright.
export const ListScene: React.FC<{ s: Extract<Scene, { kind: 'list' }> }> = ({ s }) => {
  const f = useCurrentFrame();
  const { fps } = useVideoConfig();
  const box = useBox();
  const current = s.itemsAt.reduce((cur, at, i) => (f >= at ? i : cur), -1);
  return (
    <AbsoluteFill style={{ padding: `${box.y + (box.wide ? 60 : 20)}px ${box.x}px 0` }}>
      {s.heading ? <div style={{ fontSize: box.wide ? 40 : 46, color: C.accent, fontWeight: 700, letterSpacing: 3, textTransform: 'uppercase', marginBottom: 50,
                                 opacity: interpolate(f, [0, 8], [0, 1], { extrapolateRight: 'clamp' }) }}>{s.heading}</div> : null}
      {s.items.map((it, i) => {
        const a = spring({ frame: f - s.itemsAt[i], fps, config: { damping: 16, mass: 0.6 } });
        const on = i === current;
        return (
          <div key={i} style={{ display: 'flex', gap: 34, alignItems: 'center', marginBottom: box.wide ? 40 : 46, opacity: Math.min(1, a * 1.4) * (on ? 1 : 0.5),
                                transform: `translateX(${(1 - a) * 60}px)` }}>
            <div style={{ flex: '0 0 auto', width: 76, height: 76, borderRadius: 22, background: on ? C.accent : C.accentSoft, color: on ? C.onAccent : C.accent,
                          fontSize: 38, fontWeight: 800, display: 'flex', alignItems: 'center', justifyContent: 'center' }}>{i + 1}</div>
            <div style={{ fontSize: box.wide ? 58 : 60, fontWeight: 700, lineHeight: 1.18 }}>{it}</div>
          </div>
        );
      })}
    </AbsoluteFill>
  );
};
