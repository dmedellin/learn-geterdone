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
| Serving | `deploy/Caddyfile` `handle /video/*` from `/srv-media`, CSP `media-src 'self'` | production container |

The videos are not in the image: about 1,400 lessons times two videos is tens of
gigabytes. They live on the production host and are bind-mounted read-only into
the container. A lesson that is not in `published.json` renders byte for byte as
it did before videos existed, and the page still loads nothing until the reader
presses play, so the self-containment invariant (AGENTS.md section 2) holds.

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
   pages; commit `video/published.json` and the pages, and release as usual.

The Trading Subject's hand-written lessons are not covered yet (they are not built
by `scripts/build_paths.py`); they need the same strip added through
`scripts/add_progress_marks.py`.
