"""Shared loaders for the English v2 design measurements.

Data lives in ../data (downloaded, untrusted) and in the repo. Everything here
is read-only. Tokeniser matches the kit's wordsOf, with U+2019 normalised to
an ASCII apostrophe first (the kit does not, and misreads "don't" as "don").
"""
import json
import re
import sys
from pathlib import Path
from collections import Counter, defaultdict

HERE = Path(__file__).resolve().parent
DATA = HERE / "data"   # filled by fetch.sh; never committed
REPO = Path("/home/dmedellin/learn-geterdone-speech")

WORD = re.compile(r"[A-Za-z][A-Za-z']*")
VOWELS = {"AA", "AE", "AH", "AO", "AW", "AY", "EH", "ER", "EY", "IH", "IY", "OW", "OY", "UH", "UW"}
VOICELESS = {"P", "T", "K", "F", "TH", "S", "SH", "CH", "HH"}
SIBILANT = {"S", "Z", "SH", "ZH", "CH", "JH"}


def norm(text):
    return (text.replace("’", "'").replace("‘", "'")
                .replace("“", '"').replace("”", '"'))


def words(text):
    return WORD.findall(norm(text))


def load_cmudict():
    """word -> list of pronunciations (each a list of phonemes with stress digits)."""
    d = defaultdict(list)
    for line in (DATA / "cmudict.dict").read_text(encoding="utf-8", errors="replace").splitlines():
        if not line or line.startswith(";;;"):
            continue
        line = line.split(" #", 1)[0].strip()
        parts = line.split()
        if len(parts) < 2:
            continue
        w = re.sub(r"\(\d+\)$", "", parts[0])
        d[w].append(parts[1:])
    return d


def strip_stress(ph):
    return re.sub(r"\d", "", ph)


def syllables(pron):
    return sum(1 for p in pron if p[-1].isdigit())


def stress_index(pron):
    """0-based index of the syllable carrying primary stress, or None."""
    k = 0
    for p in pron:
        if p[-1].isdigit():
            if p[-1] == "1":
                return k
            k += 1
    return None


def load_moby():
    """word -> set of POS codes (Moby Part-of-Speech, public domain).

    N noun, p plural, h noun phrase, V verb (participle), t transitive verb,
    i intransitive verb, A adjective, v adverb, C conjunction, P preposition,
    ! interjection, r pronoun, D definite article, I indefinite article,
    o nominative."""
    pos = {}
    raw = (DATA / "mobypos.txt").read_bytes().decode("latin-1")
    for line in raw.splitlines():
        line = line.strip("\r\n")
        if "\\" not in line:
            continue
        w, codes = line.rsplit("\\", 1)
        if " " in w or not w.isascii():
            continue
        pos.setdefault(w.lower(), set()).update(codes)
    return pos


def load_ngsl():
    """forms: form -> band; heads: headword -> band; forms_of: headword -> [forms]."""
    forms, heads, forms_of = {}, {}, defaultdict(list)
    for line in (REPO / "scripts/wordlists/ngsl.tsv").read_text().splitlines():
        if not line or line.startswith("#"):
            continue
        f, h, b = line.split("\t")
        forms[f] = int(b)
        heads[h] = int(b)
        forms_of[h].append(f)
    return forms, heads, forms_of


def load_scowl():
    return set(Path("/usr/share/dict/american-english").read_text().split())


def load_verbs():
    return json.loads((REPO / "scripts/wordlists/verbrules_cases.json").read_text())


def load_irregular():
    return json.loads((REPO / "content/english/data/irregular_verbs.json").read_text())


def load_listening():
    return json.loads((REPO / "content/english/data/listening.json").read_text())


def load_passage():
    return json.loads((REPO / "content/english/data/wordorder_passage.json").read_text())


def pp_novel():
    """Pride and Prejudice, novel text only, sliced on its first and last sentence."""
    raw = (DATA / "pg1342.txt").read_text(encoding="utf-8")
    a = raw.index("It is a truth universally acknowledged")
    b = raw.rindex("uniting them.") + len("uniting them.")
    t = raw[a:b]
    t = re.sub(r"\[Illustration[^\]]*\]", " ", t, flags=re.S)
    t = t.replace("_", "")
    return t


def wilde_play():
    """The Importance of Being Earnest (1895), the three acts."""
    raw = (DATA / "pg844.txt").read_text(encoding="utf-8")
    a = raw.index("FIRST ACT")
    b = raw.index("*** END OF THE PROJECT GUTENBERG")
    return raw[a:b]


def modern_docs():
    out = []
    for name in ("scotus_stanley.txt", "census_aging.txt"):
        raw = (REPO / "content/english/data" / name).read_text(encoding="utf-8")
        out.append(raw.split("\n---\n", 1)[1].strip())
    return "\n\n".join(out)


def pct(a, b, places=1):
    return "%.*f%%" % (places, 100.0 * a / b) if b else "n/a"


def show(title, hit, total, residue=None, n=40):
    print("%s: %d of %d = %s" % (title, hit, total, pct(hit, total)))
    if residue:
        print("   residue (%d): %s" % (len(residue), ", ".join(str(r) for r in residue[:n])))
