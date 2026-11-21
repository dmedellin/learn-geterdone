import React from 'react';
import { AbsoluteFill, Sequence, interpolate, useCurrentFrame, useVideoConfig } from 'remotion';
import { C, SANS } from './theme';
import type { Scene, VideoProps, Caption } from './types';
import { TitleScene } from './scenes/Title';
import { ArtScene } from './scenes/Art';
import { QuoteScene } from './scenes/Quote';
import { MathScene } from './scenes/Math';
import { CodeScene } from './scenes/Code';
import { WordsScene } from './scenes/Words';
import { ListScene } from './scenes/List';
import { EndScene } from './scenes/End';

const Body: React.FC<{ s: Scene }> = ({ s }) => {
  switch (s.kind) {
    case 'title': return <TitleScene s={s} />;
    case 'art': return <ArtScene s={s} />;
    case 'quote': return <QuoteScene s={s} />;
    case 'math': return <MathScene s={s} />;
    case 'code': return <CodeScene s={s} />;
    case 'words': return <WordsScene s={s} />;
    case 'list': return <ListScene s={s} />;
    case 'end': return <EndScene s={s} />;
  }
};

// Soft cross-fade in; no flashy transitions.
const Fade: React.FC<{ dur: number; children: React.ReactNode }> = ({ dur, children }) => {
  const f = useCurrentFrame();
  const o = interpolate(f, [0, 9, dur - 4, dur], [0, 1, 1, 0.6], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' });
  return <AbsoluteFill style={{ opacity: o }}>{children}</AbsoluteFill>;
};

// Long-form: a quiet chapter label that slides in when a chapter starts, then settles.
const ChapterLabel: React.FC<{ n: number; title: string }> = ({ n, title }) => {
  const f = useCurrentFrame();
  const a = interpolate(f, [0, 12], [0, 1], { extrapolateRight: 'clamp' });
  return (
    <div style={{ position: 'absolute', top: 56, left: 140, display: 'flex', gap: 16, alignItems: 'center', fontFamily: SANS,
                  opacity: a, transform: `translateX(${(1 - a) * -30}px)` }}>
      <div style={{ fontSize: 26, fontWeight: 800, color: C.accent }}>{String(n).padStart(2, '0')}</div>
      <div style={{ fontSize: 28, color: C.muted }}>{title}</div>
    </div>
  );
};

const Brand: React.FC<{ wide: boolean; track: string }> = ({ wide, track }) => (
  <div style={{ position: 'absolute', top: wide ? 48 : 110, right: wide ? 140 : undefined, left: wide ? undefined : 70, fontFamily: SANS,
                display: 'flex', gap: 14, alignItems: 'center' }}>
    <div style={{ background: C.accent, color: C.onAccent, fontWeight: 800, fontSize: wide ? 28 : 34, padding: wide ? '6px 18px' : '8px 22px', borderRadius: 12 }}>learn</div>
    <div style={{ color: C.muted, fontSize: wide ? 26 : 30, fontWeight: 600 }}>{track}</div>
  </div>
);

const Captions: React.FC<{ captions: Caption[] }> = ({ captions }) => {
  const f = useCurrentFrame();
  const { fps } = useVideoConfig();
  const t = f / fps;
  const cur = captions.find((c, i) => t >= c.s - 0.05 && t < (captions[i + 1] ? Math.min(captions[i + 1].s - 0.05, c.e + 0.5) : c.e + 0.5));
  if (!cur) return null;
  return (
    <div style={{ position: 'absolute', top: 1330, left: 70, right: 70, height: 230, display: 'flex', alignItems: 'center',
                  justifyContent: 'center', flexWrap: 'wrap', gap: '6px 18px', fontFamily: SANS }}>
      {cur.words.map((w, i) => {
        const on = t >= w.s - 0.03 && t < w.e + 0.05;
        return (
          <span key={i} style={{ fontSize: 74, fontWeight: 800, lineHeight: 1.15, color: on ? C.onAccent : '#fff', background: on ? C.warn : 'transparent',
                                 borderRadius: 14, padding: '0 12px', textShadow: on ? 'none' : '0 4px 14px rgba(0,0,0,.85)' }}>{w.w}</span>
        );
      })}
    </div>
  );
};

export const Video: React.FC<VideoProps> = (p) => {
  const f = useCurrentFrame();
  const wide = p.format === 'long';
  return (
    <AbsoluteFill style={{ background: C.bg, color: C.text, fontFamily: SANS }}>
      <div style={{ position: 'absolute', inset: 0, background: `radial-gradient(${wide ? '1400px 900px at 90% 0%' : '1200px 900px at 85% 5%'}, ${C.accentSoft} 0%, transparent 60%)` }} />
      {p.scenes.map((s, i) => (
        <Sequence key={i} from={s.from} durationInFrames={s.dur}>
          <Fade dur={s.dur}><Body s={s} /></Fade>
        </Sequence>
      ))}
      {wide ? p.scenes.map((s, i) => {
        if (!s.chapter) return null;
        const next = p.scenes.findIndex((x, j) => j > i && x.chapter);
        const end = next < 0 ? p.durationInFrames : p.scenes[next].from;
        return <Sequence key={'c' + i} from={s.from} durationInFrames={end - s.from}><ChapterLabel n={s.chapter.n} title={s.chapter.title} /></Sequence>;
      }) : null}
      <Brand wide={wide} track={p.track} />
      {!wide ? <div style={{ position: 'absolute', top: 0, left: 0, height: 10, width: `${(100 * f) / p.durationInFrames}%`, background: C.accent }} /> : null}
      {!wide ? <Captions captions={p.captions} /> : null}
    </AbsoluteFill>
  );
};
