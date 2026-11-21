import React from 'react';
import { AbsoluteFill, interpolate, spring, useCurrentFrame, useVideoConfig } from 'remotion';
import { C, useBox } from '../theme';
import type { Scene } from '../types';

// A short passage the lesson itself quotes, set like a pull quote, with its source.
export const QuoteScene: React.FC<{ s: Extract<Scene, { kind: 'quote' }> }> = ({ s }) => {
  const f = useCurrentFrame();
  const { fps } = useVideoConfig();
  const box = useBox();
  const pop = spring({ frame: f - 3, fps, config: { damping: 18 } });
  const cite = interpolate(f, [20, 32], [0, 1], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' });
  const long = s.text.length > 140;
  return (
    <AbsoluteFill style={{ justifyContent: 'center', padding: box.wide ? '0 220px' : `0 ${box.x}px 420px` }}>
      <div style={{ display: 'flex', gap: box.wide ? 48 : 34, opacity: pop, transform: `translateY(${(1 - pop) * 24}px)` }}>
        <div style={{ flex: '0 0 auto', width: 12, borderRadius: 6, background: C.accent }} />
        <div>
          <div style={{ fontFamily: 'Georgia, "DejaVu Serif", serif', fontStyle: 'italic', color: C.text, lineHeight: 1.3,
                        fontSize: box.wide ? (long ? 58 : 72) : (long ? 62 : 74) }}>&ldquo;{s.text}&rdquo;</div>
          {s.cite ? <div style={{ marginTop: 40, fontSize: box.wide ? 36 : 40, color: C.muted, opacity: cite }}>{s.cite}</div> : null}
        </div>
      </div>
    </AbsoluteFill>
  );
};
