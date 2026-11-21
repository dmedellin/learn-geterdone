import React from 'react';
import { AbsoluteFill, interpolate, spring, useCurrentFrame, useVideoConfig } from 'remotion';
import { C, useBox } from '../theme';
import type { Scene } from '../types';

// A worked line of mathematics, one step at a time: each line arrives when the voice reaches it,
// the line being spoken is bright and the earlier ones settle back.
export const MathScene: React.FC<{ s: Extract<Scene, { kind: 'math' }> }> = ({ s }) => {
  const f = useCurrentFrame();
  const { fps } = useVideoConfig();
  const box = useBox();
  const current = s.itemsAt.reduce((cur, at, i) => (f >= at ? i : cur), -1);
  const longest = Math.max(...s.items.map((x) => x.length), 8);
  const size = Math.min(box.wide ? 84 : 72, Math.floor((box.wide ? 1500 : box.w) / (longest * 0.55)));
  return (
    <AbsoluteFill style={{ justifyContent: 'center', alignItems: 'center', padding: box.wide ? '120px 140px 0' : `0 ${box.x}px 420px` }}>
      {s.heading ? <div style={{ fontSize: box.wide ? 38 : 44, color: C.accent, fontWeight: 700, letterSpacing: 3, textTransform: 'uppercase', marginBottom: 46,
                                 opacity: interpolate(f, [0, 8], [0, 1], { extrapolateRight: 'clamp' }) }}>{s.heading}</div> : null}
      {s.items.map((it, i) => {
        const a = spring({ frame: f - s.itemsAt[i], fps, config: { damping: 18, mass: 0.6 } });
        const on = i === current;
        return (
          <div key={i} style={{ fontFamily: '"DejaVu Serif", Georgia, serif', fontSize: size, lineHeight: 1.45, whiteSpace: 'pre',
                                color: on ? C.text : C.muted, opacity: Math.min(1, a * 1.4) * (on ? 1 : 0.55),
                                transform: `translateY(${(1 - a) * 24}px)` }}>{it}</div>
        );
      })}
    </AbsoluteFill>
  );
};
