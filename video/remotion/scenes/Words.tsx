import React from 'react';
import { AbsoluteFill, interpolate, spring, useCurrentFrame, useVideoConfig } from 'remotion';
import { C, useBox } from '../theme';
import type { Scene } from '../types';

// One key line, big and calm.
export const WordsScene: React.FC<{ s: Extract<Scene, { kind: 'words' }> }> = ({ s }) => {
  const f = useCurrentFrame();
  const { fps } = useVideoConfig();
  const box = useBox();
  const pop = spring({ frame: f - 3, fps, config: { damping: 16 } });
  const sub = interpolate(f, [18, 30], [0, 1], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' });
  return (
    <AbsoluteFill style={{ alignItems: 'center', justifyContent: 'center', textAlign: 'center', padding: box.wide ? '0 200px' : `0 ${box.x}px 420px` }}>
      <div style={{ fontSize: box.wide ? 104 : 112, fontWeight: 800, lineHeight: 1.1, letterSpacing: -1.5, opacity: pop, transform: `translateY(${(1 - pop) * 30}px)` }}>{s.text}</div>
      {s.sub ? <div style={{ marginTop: 40, fontSize: box.wide ? 44 : 50, color: C.muted, lineHeight: 1.3, opacity: sub, maxWidth: 1300 }}>{s.sub}</div> : null}
      <div style={{ marginTop: 50, height: 10, width: 220 * pop, background: C.accent, borderRadius: 5 }} />
    </AbsoluteFill>
  );
};
