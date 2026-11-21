# Lesson videos

Turns a Learn lesson into two videos: a full lesson (16:9, 1920x1080, chapters)
and a short (9:16, 1080x1920, burned-in captions). Ported from
loop-geterdone's `video/`, and it shares that pipeline's tools and cache. Runs on
the ThinkCentre; nothing here is part of the site build or the image. How the
videos reach the site is in `docs/VIDEO.md`.

    bash video/setup.sh                                                   # once; no sudo
    python3 video/make_video.py --check                                    # check scripts (stdlib)
    ~/.cache/loop-reels/venv/bin/python video/make_video.py <course>/<lesson>          # short and long
    ~/.cache/loop-reels/venv/bin/python video/make_video.py <course>/<lesson>/long     # one of them
    VIDEO_DEST=... python3 video/publish.py <course>/<lesson>              # upload and list as live

Output in `video/out/<course>/<lesson>/`: `long.mp4`, `short.mp4`, a `.jpg`
(thumbnail or cover), `.vtt` captions for the page's player, `.srt`, and a
`.json` with the length and chapters that `publish.py` copies into
`video/published.json`.

## How it works

1. **Script** (`video/episodes/<course>/<lesson>/long.md`, `short.md`): written by
   Claude to be read aloud, retelling the lesson in its own words. The format is in
   the `video/episode.py` docstring. Code on screen is the lesson's own code block
   (`@code block=N`), so a video cannot show code the page does not.
2. **Art**: Codex draws each lesson's illustrations on a magenta sheet
   (`video/art/<lesson>-scenes.prompt.md`, `-thumb.prompt.md`) and
   `video/art/slice.py --art` cuts them into `video/assets/art/`.
3. **Voice**: Kokoro `af_heart`, sentence by sentence, as on Loop.
4. **Timing**: Whisper word timings, so code highlights and list items land on the
   words that name them.
5. **Animation**: Remotion (`video/remotion/`), in Learn's dark palette.
6. **Assembly**: FFmpeg, voice at -14 LUFS, H.264 at CRF 26 with `+faststart` so the
   page can start playing before the file has downloaded.

Remotion is free for individuals and companies of up to three people.
