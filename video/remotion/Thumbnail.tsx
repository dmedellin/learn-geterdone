import React from 'react';
import { AbsoluteFill, Img, staticFile } from 'remotion';
import { C, SANS } from './theme';
import type { VideoProps } from './types';

// YouTube thumbnail: the episode's title-card art with a short, very large title.
export const Thumbnail: React.FC<VideoProps> = (p) => {
  const t = p.scenes.find((s) => s.kind === 'title');
  const art = t && t.kind === 'title' ? t.art : '';
  return (
    <AbsoluteFill style={{ background: C.bg, fontFamily: SANS }}>
      {art ? <Img src={staticFile(art)} style={{ position: 'absolute', right: 50, top: 90, height: '78%' }} /> : null}
      <div style={{ position: 'absolute', left: 60, top: 70, width: 540 }}>
        <div style={{ display: 'inline-block', background: C.accent, color: C.onAccent, fontWeight: 800, fontSize: 34, padding: '6px 18px', borderRadius: 12, marginBottom: 20 }}>learn</div>
        <div style={{ fontSize: 32, color: C.muted, fontWeight: 700, marginBottom: 26 }}>{p.track}</div>
        <div style={{ fontSize: p.lesson.length > 18 ? 92 : 120, fontWeight: 900, color: '#fff', lineHeight: 0.98, letterSpacing: -3 }}>{p.lesson}</div>
        <div style={{ marginTop: 34, fontSize: 46, fontWeight: 800, color: C.warn, lineHeight: 1.1 }}>{p.thumb}</div>
      </div>
    </AbsoluteFill>
  );
};
