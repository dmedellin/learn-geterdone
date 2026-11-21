import React from 'react';
import { AbsoluteFill, Img, interpolate, spring, staticFile, useCurrentFrame, useVideoConfig } from 'remotion';
import { C, useBox } from '../theme';
import type { Scene } from '../types';

export const TitleScene: React.FC<{ s: Extract<Scene, { kind: 'title' }> }> = ({ s }) => {
  const f = useCurrentFrame();
  const { fps } = useVideoConfig();
  const box = useBox();
  const pop = spring({ frame: f - 4, fps, config: { damping: 15 } });
  const bar = interpolate(f, [10, 26], [0, 1], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' });
  const sub = interpolate(f, [16, 28], [0, 1], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' });
  const z = interpolate(f, [0, s.dur], [1.0, 1.05]);
  return (
    <AbsoluteFill>
      {s.art ? (
        <div style={{ position: 'absolute', inset: 0, display: 'flex', alignItems: box.wide ? 'center' : 'flex-end', justifyContent: 'flex-end' }}>
          <Img src={staticFile(s.art)} style={box.wide ? { height: '72%', marginRight: 140, transform: `scale(${z})`, transformOrigin: 'right center' }
                                                     : { width: '100%', marginBottom: 640, transform: `scale(${z})` }} />
        </div>
      ) : null}
      <div style={{ position: 'absolute', left: box.x, top: box.wide ? 360 : box.y + 40, maxWidth: box.wide ? 820 : box.w }}>
        <div style={{ fontSize: box.wide ? 112 : 128, fontWeight: 800, lineHeight: 1.0, letterSpacing: -2, opacity: pop, transform: `translateY(${(1 - pop) * 24}px)` }}>{s.text}</div>
        <div style={{ height: 12, width: 300 * bar, background: C.accent, borderRadius: 6, margin: '36px 0 30px' }} />
        {s.sub ? <div style={{ fontSize: box.wide ? 50 : 54, color: C.muted, opacity: sub }}>{s.sub}</div> : null}
      </div>
    </AbsoluteFill>
  );
};
