# Lesson videos

Every lesson gets two videos: a **short** (9:16, under a minute, one idea) and the
**full lesson** (16:9, about five minutes, with chapters). The approach is the one
loop.geterdone.io uses (`dmedellin/loop-geterdone`, `video/`), ported so a script
reads and renders the same on both sites.

| Piece | Where | Runs on |
| --- | --- | --- |
| Episode scripts | `video/episodes/<course>/<lesson>/short.md`, `long.md` | written by Claude, checked in CI (`tests/test_video.py`) |
| Art | `video/art/*.prompt.md` (Codex), cut into `video/assets/art/` | ThinkCentre |
| Render | `video/make_video.py`: Kokoro voice, Whisper timing, Remotion, FFmpeg | ThinkCentre (`video/README.md`) |
| Upload | `video/publish.py`: rsync to the host, then checks each file over HTTPS | ThinkCentre |
| Live list | `video/published.json`, written by `publish.py` only after the files answer 200 | committed |
| Player | `scripts/mathpath/video.py`: two buttons under the lesson title; a click builds the `<video>` | every lesson listed in `published.json` |
| Reels feed | `scripts/mathpath/reels.py`: `/reels/`, every published short in one vertical feed | built by `scripts/build_paths.py` |
| Serving | `deploy/Caddyfile` `handle /video/*` from `/srv-media`, CSP `media-src 'self'` | production container |

The videos are not in the image: about 1,400 lessons times two videos is tens of
gigabytes. They live on the production host and are bind-mounted read-only into
the container. A lesson that is not in `published.json` renders byte for byte as
it did before videos existed, and the page still loads nothing until the reader
presses play, so the self-containment invariant (AGENTS.md section 2) holds.

## Reels

`/reels/` puts every lesson's short in one full-screen vertical feed, in library
order (Subjects as `scripts/catalog.py` lists them, then courses and lessons in
path order), like a social reel: snap scrolling, the reel in view plays and loops,
the one that leaves pauses, only the reel in view and its two neighbours hold a
`<video>`, arrow keys / `j` `k` / PageUp PageDown step, `m` toggles sound, a tap
pauses, and the URL fragment (`#<course>--<lesson>`) follows the reel. Each lesson
with a short links to its reel ("Open in Reels") beside its two buttons, and the
library index links to the feed.

The one difference from loop.geterdone.io, which autoplays muted on load: here the
page loads nothing until the reader acts (AGENTS.md section 2). Each reel is a
static card under a "Tap to start" overlay; the first tap, click or key press
starts the feed with sound, and from then on it autoplays. The media URLs live only
in the inline script. `TestReelsPage` in `tests/test_site_invariants.py` checks
that the markup carries no `src`/`poster`, that every published short is listed
once, and that the links both ways resolve. A newly published video reaches the
feed on the next `python3 scripts/build_paths.py`, with the lesson page.

## Host change needed (David, once)

Hosting on the Hetzner server's disk was chosen on 2026-11-21. The platform has no
host file server and no app volumes today (platform-ops `DEPLOYMENT_CONTRACT.md`,
`DATA_SAFETY_AND_ROLLBACK.md`), so this is a reviewed platform change, made on the
host and in `dmedellin/platform-ops`, not in this repository:

1. **Disk.** About 25 to 60 GB for all lessons (measured on the first sample;
   see the size note below). Check `df -h /` on `ubuntu-8gb-ash-1`; if there is
   not comfortably that much free, attach a Hetzner Cloud Volume (100 GB is a few
   euros a month) and mount it, for example at `/mnt/media`.
2. **Folder.** `/srv/platform-media/learn-geterdone/video/` (or a symlink to the
   Volume), readable by the container's UID 1000, writable only by the uploader.
3. **Mount.** In the Compose file the deploy wrapper renders for this app
   (`/etc/platform/templates/static-compose.yaml`, or a per-app override if the
   wrapper supports one), add one read-only bind mount:

       volumes:
         - /srv/platform-media/learn-geterdone:/srv-media:ro

   The container already serves `/video/*` from `/srv-media` (so a file at
   `/srv/platform-media/learn-geterdone/video/<course>/<lesson>/long.mp4` is
   `https://learn.geterdone.io/video/<course>/<lesson>/long.mp4`). Nothing else
   about the container changes: same image, read-only root, same user, same port.
   Record the mount in `apps/registry.yaml` in platform-ops as the reviewed
   exception (the app stays `stateless`: the folder is read-only content, not data
   the app writes).
4. **Uploader.** An SSH key from the ThinkCentre that can write only to that
   folder, for example a `media-upload` user whose `authorized_keys` line runs
   `rrsync /srv/platform-media/learn-geterdone/video`. Then on the ThinkCentre:

       export VIDEO_DEST=media-upload@<host>:/srv/platform-media/learn-geterdone/video
       python3 video/publish.py <course>/<lesson>

5. **Edge.** Nothing: host Caddy already proxies every path on
   learn.geterdone.io to the container. Range requests (seeking) pass through.

Until the mount exists, `/video/*` answers 404 and `publish.py` refuses to list
anything, so pages show no player. Shipping this code first is safe.

## Rolling out

1. Claude writes `short.md` and `long.md` for a batch of lessons (a course or a
   Subject at a time) and the art prompts; CI checks every script against its lesson.
2. On the ThinkCentre: art (Codex), then `make_video.py <course>/<lesson>` for each.
   A full lesson takes roughly its own length to render, a short about 1.5 minutes,
   so a Subject of 50 lessons is most of a day of rendering.
3. `publish.py` uploads and lists them; `python3 scripts/build_paths.py` rebuilds the
   pages (the lessons and `/reels/`); commit `video/published.json` and the pages,
   and release as usual.

## After publishing: run both scripts

The Trading Subject's 118 lessons are hand-written, so their pages are not built
by `scripts/build_paths.py`. After `publish.py` changes `video/published.json`,
run BOTH, in either order:

    python3 scripts/build_paths.py          # generated lessons, course homes, /reels/
    python3 scripts/add_progress_marks.py   # Trading lessons and course homes

then commit `video/published.json` and every page that changed. CI does not run
either script; it runs `python3 -m unittest discover -s tests`, where
`TestGeneratedPathIsCurrent` fails if `build_paths.py` would rewrite a page and
`TestTradingVideos` fails if a Trading page disagrees with `published.json`
(strip present without an entry, or entry without a strip).

How the patcher handles Trading (`scripts/add_progress_marks.py`):

- A Trading lesson listed in `published.json` gets the same watch strip
  (`video.markup`, with "Open in Reels" when it has a short) between
  `<!-- video-strip:begin -->` and `<!-- video-strip:end -->` right after the
  hero, its stylesheet (`video.CSS`) between `/* video-marks:begin */` and
  `/* video-marks:end */` in the FIRST `</style>` block, and the click handler in
  `<script data-video-marks>` before `</body>`.
- Each region is removed and re-inserted on every run, never edited in place, so
  a second run rewrites nothing, and a lesson that leaves `published.json` goes
  back to byte-identical unpatched text.
- A course home marks each published lesson card `data-video="yes"`; its CSS
  (`TRADING_LIST_CSS`, in the same marked block) draws the "Video" tag after
  the card title. The block is present only while some lesson of the course is
  published.
- `/reels/` is written by `build_paths.py`, which reads Trading's course and
  lesson titles from the published Trading pages (`trading_path()`). Trading
  appears where `scripts/catalog.py` puts it (last), as Subject "Trading".
