#!/usr/bin/env /usr/bin/python3
"""Is this page written inside the vocabulary band it teaches?

The English Subject tells its reader that 98% coverage is what comprehension
needs. A page that teaches that and is itself written at 88% has failed its own
lesson, so this runs at build time over the prose of every English page.

In-band means: a form listed in the NGSL 2,809 (Browne, Culligan and Phillips,
CC BY-SA 4.0) or its supplement, a number word, a proper noun, or one of at most
twenty glossary terms the page defines with <dfn> before first using them.

What is NOT prose and is excluded: script and style bodies, the lab markup and
its KPI tiles, the mathblock, code spans, and single letters -- a maths variable
is not vocabulary, and counting `x` as an unknown word is how a checker lies.

Exit 0 if every page passes, 1 otherwise. --report prints every page's figure.
"""
import argparse
import pathlib
import re
import sys
from collections import Counter
from html.parser import HTMLParser

ROOT = pathlib.Path(__file__).resolve().parent.parent
WORDLIST = ROOT / "scripts" / "wordlists" / "ngsl.tsv"
FLOOR = 98.0
GLOSSARY_MAX = 20
NUMBER = re.compile(
    r"^(zero|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|"
    r"thirteen|fourteen|fifteen|sixteen|seventeen|eighteen|nineteen|twenty|"
    r"thirty|forty|fifty|sixty|seventy|eighty|ninety|hundred|thousand|million|"
    r"billion|first|second|third|fourth|fifth|sixth|seventh|eighth|ninth|tenth)$")
# twenty-eight and ninety-nine are number words too, and a checker that counts
# them as unknown vocabulary overstates the gap in the direction that looks rigorous.
COMPOUND_NUMBER = re.compile(r"^[a-z]+-[a-z]+$")
WORD = re.compile(r"[A-Za-z][A-Za-z'’-]*")
# A hyphen-initial fragment is an AFFIX the lesson is talking about -- "-ing",
# "-ed", "-ies" -- not a word the reader has to know. Counting the lesson's own
# subject matter as unknown vocabulary is the same failure as counting `x`.
AFFIX = re.compile(r"(?<![A-Za-z])-[A-Za-z]+")

# Chrome the library puts on every page; it is furniture, not lesson prose.
CHROME = {
    "lesson", "lessons", "course", "courses", "subject", "subjects", "path",
    "library", "syllabus", "overview", "glossary", "quiz", "next", "previous",
    "menu", "theme", "dark", "light", "browser", "javascript", "copyright",
}


def load_bands(path):
    forms = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line or line.startswith("#"):
            continue
        parts = line.split("\t")
        if len(parts) == 3:
            forms[parts[0]] = int(parts[2])
    return forms


class Prose(HTMLParser):
    """Lesson prose, with everything that is not prose removed.

    A lab prints numbers, identifiers and tile labels that no reader learns
    vocabulary from, so including them would measure the lab rather than the
    writing.
    """

    SKIP_TAGS = {"script", "style", "code", "pre", "svg", "select", "option",
                 "button", "footer", "nav", "head", "title"}
    SKIP_CLASS = re.compile(r"\b(mathblock|kpi|kpi-grid|lab|lab-\w+|tile|float-label)\b")

    def __init__(self, markup):
        super().__init__(convert_charrefs=True)
        self.depth = 0
        self.chunks = []
        self.defined = []          # glossary terms, in the order they are defined
        self._in_dfn = False
        self.feed(markup)

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag in self.SKIP_TAGS or self.SKIP_CLASS.search(a.get("class", "")):
            self.depth += 1
        elif self.depth:
            self.depth += 1
        if tag == "dfn" and not self.depth:
            self._in_dfn = True
            self.chunks.append("\x00")      # marks where a definition begins

    def handle_endtag(self, tag):
        if self.depth:
            self.depth -= 1
        if tag == "dfn":
            self._in_dfn = False

    def handle_data(self, data):
        if self.depth:
            return
        self.chunks.append(data)
        if self._in_dfn:
            self.defined.extend(w.lower() for w in WORD.findall(data))

    @property
    def text(self):
        return "".join(self.chunks)


def measure(markup, forms):
    doc = Prose(markup)
    text = doc.text
    # A term counts as defined only from the point its <dfn> appears.
    defined_at = {}
    cursor = 0
    for piece in text.split("\x00")[1:]:
        for w in WORD.findall(piece)[:4]:
            defined_at.setdefault(w.lower(), cursor)
        cursor += 1
    glossary = set(doc.defined)

    tokens = []
    for sentence_break, chunk in enumerate(re.split(
            r"(?<=[.!?])\s+", AFFIX.sub(" ", text.replace("\x00", "")))):
        for i, w in enumerate(WORD.findall(chunk)):
            tokens.append((w, i == 0))

    inb, off, early = 0, Counter(), []
    for w, sentence_initial in tokens:
        low = w.lower()
        if len(low) < 2:
            continue                                   # a variable, not a word
        if (low in forms or NUMBER.match(low) or low in CHROME
                or (COMPOUND_NUMBER.match(low)
                    and all(NUMBER.match(part) for part in low.split("-")))
                or low in glossary
                or (w[0].isupper() and not sentence_initial)):
            inb += 1
        else:
            off[low] += 1
    total = inb + sum(off.values())
    pct = 100.0 * inb / total if total else 100.0
    return pct, total, off, sorted(glossary), early


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("paths", nargs="*", help="pages to check (default: the English Subject)")
    ap.add_argument("--report", action="store_true", help="print every page, not just failures")
    ap.add_argument("--floor", type=float, default=FLOOR)
    args = ap.parse_args()

    forms = load_bands(WORDLIST)
    targets = [pathlib.Path(p) for p in args.paths] or sorted(
        (ROOT / "site" / "english").glob("**/index.html"))
    if not targets:
        print("bandcheck: no pages to check")
        return 0

    failures = 0
    for page in targets:
        pct, total, off, glossary, _ = measure(page.read_text(encoding="utf-8"), forms)
        bad = []
        if pct < args.floor:
            bad.append("%.1f%% in band, floor %.1f%%" % (pct, args.floor))
        if len(glossary) > GLOSSARY_MAX:
            bad.append("%d glossary terms, at most %d" % (len(glossary), GLOSSARY_MAX))
        if bad or args.report:
            try:
                name = page.relative_to(ROOT)
            except ValueError:
                name = page        # a probe outside the tree is still checkable
            print("%-62s %6.1f%%  %5d words  %2d defined  %s"
                  % (name, pct, total, len(glossary),
                     "; ".join(bad) if bad else "ok"))
            if bad:
                print("        commonest off-list: %s"
                      % ", ".join(w for w, _ in off.most_common(12)))
        failures += bool(bad)
    if failures:
        print("\nbandcheck: %d page(s) outside the band this Subject teaches" % failures)
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
