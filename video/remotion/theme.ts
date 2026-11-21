import { useVideoConfig } from 'remotion';

// Learn's dark theme (scripts/mathpath/theme.py :root tokens).
export const C = {
  bg: '#071019', panel: '#101f2e', text: '#edf7ff', muted: '#95aabd', line: '#203448',
  accent: '#37d7e7', accentSoft: '#0e2a36', ok: '#41e39b', warn: '#ffc857',
  codeBg: '#0b1622', grey: '#3a4f63', bad: '#ff7b86', purple: '#b69cff', onAccent: '#041116',
};
export const SANS = '"Noto Sans", "DejaVu Sans", "Liberation Sans", sans-serif';
export const MONO = '"DejaVu Sans Mono", "Liberation Mono", monospace';

// Where content may go. Portrait keeps clear of the platform UI (bottom ~360 px,
// right strip) and leaves a caption band; landscape leaves room for YouTube's
// own captions at the bottom.
export type Box = { x: number; y: number; w: number; h: number; wide: boolean; s: number };
export function useBox(): Box {
  const { width, height } = useVideoConfig();
  const wide = width > height;
  return wide
    ? { x: 140, y: 150, w: width - 280, h: 790, wide, s: 1 }
    : { x: 70, y: 250, w: width - 140, h: 1040, wide, s: 1 };
}
