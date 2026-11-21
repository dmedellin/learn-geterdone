#!/usr/bin/env python3
"""Cut a Codex sheet (flat magenta background, COLSxROWS grid) into transparent PNG icons.

    ~/.cache/loop-reels/venv/bin/python video/art/slice.py --art video/art/<sheet>.png 2x3 name1,name2,...

--bg RRGGBB keys out a flat background of that colour instead of magenta.
Names map to cells left to right, top to bottom; "-" skips a cell. Writes
video/assets/icons/<name>.png at 256x256 (with --art: video/assets/art/<name>.png, longest side 1600, shape kept). Same method as the pixelbattle.me
posters: chroma key on "magenta-ness", despill the edges, cut by gap detection
(falling back to an even grid), crop to the icon, pad square.
"""
import sys
from pathlib import Path

import numpy as np
from PIL import Image

HERE = Path(__file__).resolve().parent
OUT = HERE.parent / "assets" / "icons"


def key_flat(img, hexcol):
    """Key out a flat non-magenta background (e.g. a thumbnail drawn on navy)."""
    a = np.asarray(img.convert("RGB")).astype(np.int16)
    bg = np.array([int(hexcol[i:i + 2], 16) for i in (0, 2, 4)])
    d = np.abs(a - bg).sum(axis=2)
    alpha = np.clip((d - 18) * 255 / 40, 0, 255)
    return Image.fromarray(np.dstack([a, alpha]).astype(np.uint8), "RGBA"), alpha > 40


def key(img):
    a = np.asarray(img.convert("RGB")).astype(np.int16)
    r, g, b = a[..., 0], a[..., 1], a[..., 2]
    m = np.minimum(r, b) - g                       # ~255 on pure magenta, <= 0 on white or blue
    alpha = np.clip((150 - m) * 255 / 90, 0, 255)
    alpha[m < 60] = 255
    k = np.clip(m, 0, None)
    edge = (alpha < 255) | (m > 20)
    r = np.where(edge, np.clip(r - k, 0, 255), r)
    b = np.where(edge, np.clip(b - k, 0, 255), b)
    rgba = np.dstack([r, g, b, alpha]).astype(np.uint8)
    return Image.fromarray(rgba, "RGBA"), alpha > 40


def bands(proj, n):
    on = proj > 0
    runs, start = [], None
    for i, v in enumerate(on):
        if v and start is None:
            start = i
        if not v and start is not None:
            runs.append((start, i))
            start = None
    if start is not None:
        runs.append((start, len(on)))
    runs = [r for r in runs if r[1] - r[0] > 8]
    if len(runs) == n:
        return runs
    step = len(proj) / n
    return [(int(i * step), int((i + 1) * step)) for i in range(n)]


def _main_run(proj, gap=70):
    """The longest stretch of non-empty rows/columns, bridging gaps up to `gap` px."""
    on = np.nonzero(proj)[0]
    if not len(on):
        return 0, len(proj)
    runs, start, last = [], on[0], on[0]
    for v in on[1:]:
        if v - last > gap:
            runs.append((start, last + 1))
            start = v
        last = v
    runs.append((start, last + 1))
    return max(runs, key=lambda r: proj[r[0]:r[1]].sum())


def main_block(cell):
    """Drop specks that bled in from a neighbouring cell: keep the main block only."""
    out = np.zeros_like(cell)
    y0, y1 = _main_run(cell.sum(axis=1), gap=30)
    x0, x1 = _main_run(cell[y0:y1].sum(axis=0))
    out[y0:y1, x0:x1] = cell[y0:y1, x0:x1]
    return out


def main():
    args = [a for i, a in enumerate(sys.argv[1:], 1) if not a.startswith("--") and sys.argv[i - 1] not in ("--bg", "--out")]
    src, grid, names = args[0], args[1], args[2].split(",")
    hero = "--art" in sys.argv           # scene illustrations: assets/art/, longest side 1600 px
    out_dir, size = (OUT.parent / "art", 1600) if hero else (OUT, 256)
    if "--out" in sys.argv:              # e.g. video/assets/art/<course>/<lesson>
        out_dir = Path(sys.argv[sys.argv.index("--out") + 1])
    cols, rows = map(int, grid.split("x"))
    assert len(names) == cols * rows, "%d names for %d cells" % (len(names), cols * rows)
    bg = sys.argv[sys.argv.index("--bg") + 1] if "--bg" in sys.argv else None
    rgba, solid = key_flat(Image.open(src), bg) if bg else key(Image.open(src))
    out_dir.mkdir(parents=True, exist_ok=True)
    rb = bands(solid.sum(axis=1), rows)
    for r, (y0, y1) in enumerate(rb):
        cb = bands(solid[y0:y1].sum(axis=0), cols)
        for c, (x0, x1) in enumerate(cb):
            name = names[r * cols + c]
            if name == "-":
                continue
            cell = main_block(solid[y0:y1, x0:x1])
            ys, xs = np.nonzero(cell)
            box = (x0 + xs.min(), y0 + ys.min(), x0 + xs.max() + 1, y0 + ys.max() + 1)
            icon = rgba.crop(box)
            if hero:  # keep the illustration's own shape; the title card fits it
                k = size / max(icon.size)
                icon.resize((round(icon.size[0] * k), round(icon.size[1] * k)), Image.LANCZOS).save(out_dir / (name + ".png"))
                print(name, box)
                continue
            side = int(max(icon.size) * 1.08)
            sq = Image.new("RGBA", (side, side), (0, 0, 0, 0))
            sq.paste(icon, ((side - icon.size[0]) // 2, (side - icon.size[1]) // 2))
            sq.resize((size, size), Image.LANCZOS).save(out_dir / (name + ".png"))
            print(name, box)


if __name__ == "__main__":
    main()
