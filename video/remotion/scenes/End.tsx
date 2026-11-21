import React from 'react';
import { AbsoluteFill, interpolate, spring, useCurrentFrame, useVideoConfig } from 'remotion';
import { C, MONO, useBox } from '../theme';
import type { Scene } from '../types';

export const EndScene: React.FC<{ s: Extract<Scene, { kind: 'end' }> }> = ({ s }) => {
  const f = useCurrentFrame();
  const { fps } = useVideoConfig();
  const box = useBox();
  const pop = spring({ frame: f - 6, fps, config: { damping: 12 } });
  const [host, ...rest] = s.url.split('/');
  return (
    <AbsoluteFill style={{ alignItems: 'center', justifyContent: 'center', textAlign: 'center', paddingBottom: box.wide ? 0 : 480 }}>
      <div style={{ fontSize: box.wide ? 80 : 76, fontWeight: 800, marginBottom: 46 }}>{s.text}</div>
      <div style={{ transform: `scale(${0.85 + 0.15 * pop})`, background: C.accent, color: C.onAccent, borderRadius: 26, padding: '26px 46px', fontWeight: 800, fontSize: box.wide ? 64 : 58 }}>{host}</div>
      <div style={{ marginTop: 28, fontFamily: MONO, fontSize: 30, color: C.muted, opacity: interpolate(f, [12, 22], [0, 1], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' }) }}>/{rest.join('/')}</div>
    </AbsoluteFill>
  );
};
