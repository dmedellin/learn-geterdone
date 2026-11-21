import React from 'react';
import { Composition, Still } from 'remotion';
import { Video } from './Video';
import { Thumbnail } from './Thumbnail';
import type { VideoProps } from './types';

const sample: VideoProps = {
  format: 'long', width: 1920, height: 1080, fps: 30, durationInFrames: 90, title: 'Studio sample', thumb: '', lesson: 'Chain of Responsibility',
  track: 'Design Patterns', captions: [],
  scenes: [{ kind: 'words', from: 0, dur: 90, text: 'Who takes the request?', sub: '' }],
};

// make_video.py passes real props; size and length follow them.
export const Root: React.FC = () => (
  <>
    <Composition
      id="Video"
      component={Video as unknown as React.FC<Record<string, unknown>>}
      width={1920}
      height={1080}
      fps={30}
      durationInFrames={90}
      defaultProps={sample as unknown as Record<string, unknown>}
      calculateMetadata={({ props }) => {
        const p = props as unknown as VideoProps;
        return { durationInFrames: p.durationInFrames, fps: p.fps, width: p.width, height: p.height };
      }}
    />
    <Still id="Thumbnail" component={Thumbnail as unknown as React.FC<Record<string, unknown>>} width={1280} height={720}
           defaultProps={sample as unknown as Record<string, unknown>} />
  </>
);
