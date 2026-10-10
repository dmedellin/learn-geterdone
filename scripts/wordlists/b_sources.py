"""Loaders for the downloaded sources the English kit's second half derives from.

Shared by b_sounds.py and b_concordance.py. Nothing here is shipped: the two
scripts read the sources once, by hand, and write the small JSON files the
pages carry. The sources are fetched by docs/english-v2/measure/fetch.sh into
docs/english-v2/measure/data/ (or any directory passed as --sources) and are
pinned by sha256 below, so a changed upstream file stops the scripts rather
than silently moving every figure.

    CMUdict (cmusphinx/cmudict, master)   BSD-2; the notice travels with every
                                           derived file (b_CMUDICT_LICENSE)
    Moby Part-of-Speech (Gutenberg #3203)  public domain; BUILD TIME ONLY -- it
                                           picks which headwords are nouns,
                                           verbs or adjectives and no page
                                           carries any of it
    Pride and Prejudice (Gutenberg #1342)  public domain
    The Importance of Being Earnest (#844) public domain
"""

import hashlib
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
DEFAULT_SOURCES = ROOT / "docs" / "english-v2" / "measure" / "data"

PINS = {
    "cmudict.dict": "81917843c7f44ce2b094ac63873c2c7a4cf802040792c455ba3ca406891c3d22",
    "cmudict_LICENSE": "bd4ce8e44170a5f9f481310ca85c51de3c4f851a65e679b40e603b143bd3542a",
    "mobypos.txt": "cc81458b820a36253fbeb8106045166a345209d0fbf4cbfc20be2b189f24af82",
    "pg1342.txt": "3f6bb9d6f78e0293b56acd4714dd68cb7d6d1d293402031ce9d5a216bcaf9d75",
    "pg844.txt": "1b8a58099bb1cdef6a845277a4bacf2f4a268702c165bde30124d4b5105d1851",
}

SOURCE_NOTES = {
    "cmudict.dict": "CMUdict, cmusphinx/cmudict master, "
                    "https://raw.githubusercontent.com/cmusphinx/cmudict/master/cmudict.dict, "
                    "BSD-2 (notice in scripts/wordlists/b_CMUDICT_LICENSE)",
    "mobypos.txt": "Moby Part-of-Speech, Grady Ward, Gutenberg #3203, "
                   "https://www.gutenberg.org/files/3203/files/mobypos.txt, public domain; "
                   "used at build time only",
    "pg1342.txt": "Pride and Prejudice, Jane Austen, 1813; Gutenberg #1342 (1894 edition), "
                  "https://www.gutenberg.org/cache/epub/1342/pg1342.txt, public domain; "
                  "novel text only, sliced on its first and last sentence",
    "pg844.txt": "The Importance of Being Earnest, Oscar Wilde, 1895; Gutenberg #844, "
                 "https://www.gutenberg.org/cache/epub/844/pg844.txt, public domain; "
                 "the three acts only",
}

WORD = re.compile(r"[A-Za-z][A-Za-z']*")
VOWELS = {"AA", "AE", "AH", "AO", "AW", "AY", "EH", "ER", "EY", "IH", "IY", "OW", "OY", "UH", "UW"}
NOUN, VERB, ADJ, ADV = {"N", "h"}, {"V", "t", "i"}, {"A"}, {"v"}


def sources_dir(argv):
    if "--sources" in argv:
        return Path(argv[argv.index("--sources") + 1])
    return DEFAULT_SOURCES


def read_pinned(src, name):
    """The bytes of one source, refused unless its sha256 is the pinned one."""
    path = src / name
    if not path.exists():
        sys.exit("missing %s: run docs/english-v2/measure/fetch.sh (or pass --sources DIR)" % path)
    data = path.read_bytes()
    digest = hashlib.sha256(data).hexdigest()
    if digest != PINS[name]:
        sys.exit("%s changed upstream (sha256 %s, pinned %s); review before re-pinning"
                 % (name, digest, PINS[name]))
    return data


def provenance(names):
    return [{"source": SOURCE_NOTES[n], "sha256": PINS[n]} for n in names]


def norm(text):
    return (text.replace("’", "'").replace("‘", "'")
                .replace("“", '"').replace("”", '"'))


def words(text):
    return WORD.findall(norm(text))


def strip_stress(ph):
    return re.sub(r"\d", "", ph)


def syllables(pron):
    return sum(1 for p in pron if p[-1].isdigit())


def stress_index(pron):
    """0-based part carrying the FIRST primary stress, or None."""
    k = 0
    for p in pron:
        if p[-1].isdigit():
            if p[-1] == "1":
                return k
            k += 1
    return None


def last_stress_index(pron):
    """0-based part carrying the LAST primary stress (engineer has two)."""
    k, found = 0, None
    for p in pron:
        if p[-1].isdigit():
            if p[-1] == "1":
                found = k
            k += 1
    return found


def vowels_of(pron):
    return [(strip_stress(p), p[-1]) for p in pron if p[-1].isdigit()]


def load_cmudict(src):
    d = defaultdict(list)
    raw = read_pinned(src, "cmudict.dict").decode("utf-8", errors="replace")
    for line in raw.splitlines():
        if not line or line.startswith(";;;"):
            continue
        parts = line.split(" #", 1)[0].strip().split()
        if len(parts) < 2:
            continue
        d[re.sub(r"\(\d+\)$", "", parts[0])].append(parts[1:])
    return d


def load_moby(src):
    pos = {}
    for line in read_pinned(src, "mobypos.txt").decode("latin-1").splitlines():
        line = line.strip("\r\n")
        if "\\" not in line:
            continue
        w, codes = line.rsplit("\\", 1)
        if " " in w or not w.isascii():
            continue
        pos.setdefault(w.lower(), set()).update(codes)
    return pos


def load_ngsl():
    """forms: form -> band; heads: headword -> band (file order kept)."""
    forms, heads = {}, {}
    for line in (HERE / "ngsl.tsv").read_text(encoding="utf-8").splitlines():
        if not line or line.startswith("#"):
            continue
        f, h, b = line.split("\t")
        forms[f] = int(b)
        heads[h] = int(b)
    return forms, heads


def novel(src):
    raw = read_pinned(src, "pg1342.txt").decode("utf-8")
    a = raw.index("It is a truth universally acknowledged")
    b = raw.rindex("uniting them.") + len("uniting them.")
    t = re.sub(r"\[Illustration[^\]]*\]", " ", raw[a:b], flags=re.S)
    return t.replace("_", "").replace("\r\n", "\n")


def play(src):
    raw = read_pinned(src, "pg844.txt").decode("utf-8")
    a = raw.index("FIRST ACT")
    b = raw.index("*** END OF THE PROJECT GUTENBERG")
    return raw[a:b].replace("\r\n", "\n")


def modern_docs():
    out = []
    for name in ("scotus_stanley.txt", "census_aging.txt"):
        raw = (ROOT / "content" / "english" / "data" / name).read_text(encoding="utf-8")
        out.append(raw.split("\n---\n", 1)[1].strip())
    return "\n\n".join(out)


def passage():
    return json.loads((ROOT / "content" / "english" / "data" / "wordorder_passage.json")
                      .read_text(encoding="utf-8"))["passage"]


def dump(obj):
    """The one serialisation every b_ file uses, so --check compares bytes."""
    return json.dumps(obj, ensure_ascii=False, indent=0, sort_keys=False) + "\n"


def write_or_check(outputs, argv):
    """outputs: {Path: text}. --check exits 1 if any committed file differs."""
    stale = [p for p, text in outputs.items()
             if not p.exists() or p.read_text(encoding="utf-8") != text]
    if "--check" in argv:
        for p in stale:
            print("STALE: %s" % p.relative_to(ROOT))
        if stale:
            sys.exit(1)
        print("ok: %d file(s) current" % len(outputs))
        return
    for p, text in outputs.items():
        p.write_text(text, encoding="utf-8")
        print("wrote %s (%d bytes)" % (p.relative_to(ROOT), len(text.encode("utf-8"))))
