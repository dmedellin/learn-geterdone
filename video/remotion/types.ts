export type Word = { w: string; s: number; e: number };
export type Caption = { s: number; e: number; words: Word[] };
type Base = { from: number; dur: number; chapter?: { n: number; title: string } };
export type Scene =
  | (Base & { kind: 'title'; text: string; sub: string; art: string })
  | (Base & { kind: 'art'; art: string; zoom: string })
  | (Base & { kind: 'code'; lang: string; label: string; firstLine: number; lines: string[]; focus: { a: number; b: number; at: number | null }[] })
  | (Base & { kind: 'words'; text: string; sub: string })
  | (Base & { kind: 'math'; heading: string; items: string[]; itemsAt: number[] })
  | (Base & { kind: 'quote'; text: string; cite: string })
  | (Base & { kind: 'list'; heading: string; items: string[]; itemsAt: number[] })
  | (Base & { kind: 'end'; text: string; url: string });
export type VideoProps = {
  format: 'long' | 'short';
  width: number;
  height: number;
  fps: number;
  durationInFrames: number;
  title: string;
  thumb: string;
  lesson: string;
  track: string;
  scenes: Scene[];
  captions: Caption[];
};
