import React from 'react';
import { AbsoluteFill, Easing, Img, interpolate, staticFile, useCurrentFrame } from 'remotion';
import { useBox } from '../theme';
import type { Scene } from '../types';

// A purpose-made illustration, slowly pushing in (or out) while it is talked through.
export const ArtScene: React.FC<{ s: Extract<Scene, { kind: 'art' }> }> = ({ s }) => {
  const f = useCurrentFrame();
  const box = useBox();
  const [a, b] = s.zoom === 'out' ? [1.08, 1.0] : [1.0, 1.08];
  const z = interpolate(f, [0, s.dur], [a, b], { easing: Easing.inOut(Easing.sin) });
  return (
    <AbsoluteFill>
      <div style={{ position: 'absolute', left: box.x, top: box.y, width: box.w, height: box.h - (box.wide ? 0 : 60), display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
        <Img src={staticFile(s.art)} style={{ maxWidth: '100%', maxHeight: '100%', objectFit: 'contain', transform: `scale(${z})` }} />
      </div>
    </AbsoluteFill>
  );
};
