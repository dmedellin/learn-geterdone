"""Lesson videos: the episode scripts and the published list (video/, scripts/mathpath/video.py).

Stdlib only; nothing here needs the video toolchain, which lives on the ThinkCentre.
"""

import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from video import episode as E  # noqa: E402
from video import lessons as L  # noqa: E402


class EpisodeScripts(unittest.TestCase):
    def test_every_script_renders(self):
        """Every episode script parses, names a real lesson and only shows what that lesson has."""
        self.assertEqual(E.check_all(), [])

    def test_lessons_come_in_pairs(self):
        """A lesson gets both videos or neither, so the watch strip never offers half a pair."""
        for d in sorted({p.parent for p in E.all_scripts()}):
            names = sorted(p.stem for p in d.glob("*.md"))
            self.assertEqual(names, ["long", "short"], d)


class PublishedList(unittest.TestCase):
    def setUp(self):
        self.data = json.loads((ROOT / "video" / "published.json").read_text(encoding="utf-8"))

    def test_shape(self):
        for key, entry in self.data["lessons"].items():
            L.find(key)  # raises for a lesson that does not exist
            self.assertEqual(sorted(entry), ["long", "short"], key)
            for name in ("short", "long"):
                self.assertGreater(entry[name]["seconds"], 5, key)
                for c in entry[name].get("chapters", []):
                    self.assertLessEqual(c["t"], entry[name]["seconds"], key)

    def test_published_lessons_have_scripts(self):
        """A live video came from a script in the repository, not from nowhere."""
        for key in self.data["lessons"]:
            for name in ("short", "long"):
                self.assertTrue((E.EPISODES / key / (name + ".md")).exists(), "%s/%s" % (key, name))

    def test_pages_show_exactly_the_published_videos(self):
        site = ROOT / "site"
        for key in self.data["lessons"]:
            page = (site / key / "index.html").read_text(encoding="utf-8")
            self.assertIn('id="watchStage"', page, key)
        # and a lesson with no entry carries no player at all
        sample = next(k for k in (L.key(c, l) for _, c, l in L.all_lessons()) if k not in self.data["lessons"])
        self.assertNotIn('id="watchStage"', (site / sample / "index.html").read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
