"""The sources the English Subject's derived data files are built from.

Shared by clean_nouns.py, clean_adjectives.py, sounds.py and concordance.py.
Nothing here is shipped: the four downloaded sources are read at build time
only, each pinned by the sha256 it had when it was fetched, and a script that
finds a different file stops rather than silently writing different figures.

WHERE THE SOURCES LIVE. docs/english-v2/measure/fetch.sh downloads them into
docs/english-v2/measure/data/ (ignored by git: downloaded, untrusted). Pass
--sources DIR, or set EN_SOURCES, to read them from somewhere else.

THE TOKENISER is the page's: a word is a letter followed by letters and
apostrophes, after the typographic apostrophes U+2018 and U+2019 are written
as ', and with an apostrophe left hanging at the end of a word (a closing
quotation mark, or the plural possessive Bennets') taken off. `tokens_of`
also keeps digit runs, for the years of the time-preposition lines.
"""

import hashlib
import json
import os
import re
import sys
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
DATA = ROOT / "content" / "english" / "data"
DEFAULT_SOURCES = ROOT / "docs" / "english-v2" / "measure" / "data"

SOURCES = {
    "cmudict.dict": ("81917843c7f44ce2b094ac63873c2c7a4cf802040792c455ba3ca406891c3d22",
                     "CMUdict, cmusphinx/cmudict master, BSD-2-Clause "
                     "(https://raw.githubusercontent.com/cmusphinx/cmudict/master/cmudict.dict)"),
    "pg1342.txt": ("3f6bb9d6f78e0293b56acd4714dd68cb7d6d1d293402031ce9d5a216bcaf9d75",
                   "Pride and Prejudice, Jane Austen, 1813; Project Gutenberg #1342, public domain "
                   "(https://www.gutenberg.org/cache/epub/1342/pg1342.txt)"),
    "pg844.txt": ("1b8a58099bb1cdef6a845277a4bacf2f4a268702c165bde30124d4b5105d1851",
                  "The Importance of Being Earnest, Oscar Wilde, 1895; Project Gutenberg #844, "
                  "public domain (https://www.gutenberg.org/cache/epub/844/pg844.txt)"),
    "mobypos.txt": ("cc81458b820a36253fbeb8106045166a345209d0fbf4cbfc20be2b189f24af82",
                    "Moby Part-of-Speech list, Grady Ward; Project Gutenberg #3203, public domain "
                    "(https://www.gutenberg.org/files/3203/files/mobypos.txt)"),
}
DICTIONARY = Path("/usr/share/dict/american-english")
DICTIONARY_SHA256 = "9e66281f7e51445eab6857488ff6e3d768afffadb7fb1adbef5e4617bee4a53b"
DICTIONARY_NAME = "SCOWL wamerican 2020.12.07 (/usr/share/dict/american-english)"

NGSL_NOTE = "NGSL 1.2 (Browne, Culligan and Phillips), CC BY-SA 4.0"

# The guard the published pages are swept with: a word beside a digit reads as
# a numbered course or lesson. Every output is checked against it.
ORDINAL = re.compile(r"(?i)\bcourse\s+\d|\bcourses\s+\d+\s+(?:and|to|through)\s+\d+|\blesson\s+\d+\s+of\s+\d+")


class MissingSources(SystemExit):
    pass


def sources_dir():
    for i, arg in enumerate(sys.argv):
        if arg == "--sources" and i + 1 < len(sys.argv):
            return Path(sys.argv[i + 1])
    return Path(os.environ.get("EN_SOURCES", DEFAULT_SOURCES))


def source(name):
    """The bytes of one pinned source, after its sha256 is checked."""
    path = sources_dir() / name
    if not path.exists():
        raise MissingSources("%s: not found; run docs/english-v2/measure/fetch.sh or pass --sources DIR"
                             % path)
    data = path.read_bytes()
    digest = hashlib.sha256(data).hexdigest()
    want = SOURCES[name][0]
    if digest != want:
        sys.exit("%s has sha256 %s, not the %s these files were built from; "
                 "review the difference before changing the pin" % (path, digest, want))
    return data


def provenance(*names):
    """The sources a file was built from, with licence, URL and sha256."""
    return ["%s; sha256 %s" % (SOURCES[n][1], SOURCES[n][0]) for n in names]


# ---------------------------------------------------------------- text

def norm(text):
    return (text.replace("’", "'").replace("‘", "'")
                .replace("“", '"').replace("”", '"'))


WORD = re.compile(r"[A-Za-z][A-Za-z']*")
TOKEN = re.compile(r"[A-Za-z][A-Za-z']*|[0-9]+")


def words_of(text):
    return [w.rstrip("'") for w in WORD.findall(norm(text))]


def tokens_of(text):
    return [w.rstrip("'") for w in TOKEN.findall(norm(text))]


def novel():
    """Pride and Prejudice, the novel only: sliced on its first and last
    sentence (never on the Gutenberg markers, which would take in the 1894
    preface), with the illustration captions removed. Underscores, the
    edition's italics, are kept here and removed by whoever prints a line."""
    raw = source("pg1342.txt").decode("utf-8").replace("\r\n", "\n")
    a = raw.index("It is a truth universally acknowledged")
    b = raw.rindex("uniting them.") + len("uniting them.")
    return re.sub(r"\[Illustration[^\]]*\]", " ", raw[a:b], flags=re.S)


def play():
    """The Importance of Being Earnest, the three acts."""
    raw = source("pg844.txt").decode("utf-8").replace("\r\n", "\n")
    return raw[raw.index("FIRST ACT"):raw.index("*** END OF THE PROJECT GUTENBERG")]


def modern_docs():
    """The two modern documents, as content/english/data prints them."""
    out = []
    for name in ("scotus_stanley.txt", "census_aging.txt"):
        raw = (DATA / name).read_text(encoding="utf-8")
        out.append(raw.split("\n---\n", 1)[1].strip())
    return out


def passage():
    return json.loads((DATA / "wordorder_passage.json").read_text())["passage"]


# ---------------------------------------------------------------- lists

def cmudict():
    """word -> list of pronunciations, each a list of phonemes with stress digits."""
    d = defaultdict(list)
    for line in source("cmudict.dict").decode("utf-8", "replace").splitlines():
        if not line or line.startswith(";;;"):
            continue
        parts = line.split(" #", 1)[0].split()
        if len(parts) < 2:
            continue
        d[re.sub(r"\(\d+\)$", "", parts[0])].append(parts[1:])
    return d


def moby():
    """word -> set of Moby part-of-speech codes. N noun, h noun phrase, p plural,
    V participle, t transitive verb, i intransitive verb, A adjective, v adverb,
    C conjunction, P preposition, ! interjection, r pronoun, D definite article,
    I indefinite article, o nominative."""
    pos = {}
    for line in source("mobypos.txt").decode("latin-1").splitlines():
        line = line.strip("\r\n")
        if "\\" not in line:
            continue
        w, codes = line.rsplit("\\", 1)
        if " " in w or not w.isascii():
            continue
        pos.setdefault(w.lower(), set()).update(codes)
    return pos


NOUN = {"N", "h"}
VERB = {"V", "t", "i"}
ADJ = {"A"}
ADV = {"v"}


def ngsl():
    """forms: form -> band; heads: headword -> band; forms_of: headword -> [forms]."""
    forms, heads, forms_of = {}, {}, defaultdict(list)
    for line in (HERE / "ngsl.tsv").read_text().splitlines():
        if not line or line.startswith("#"):
            continue
        f, h, b = line.split("\t")
        forms[f] = int(b)
        heads[h] = int(b)
        forms_of[h].append(f)
    return forms, heads, forms_of


def dictionary():
    data = DICTIONARY.read_bytes()
    digest = hashlib.sha256(data).hexdigest()
    if digest != DICTIONARY_SHA256:
        sys.exit("%s is not the dictionary these files were built with (sha256 %s)"
                 % (DICTIONARY, digest))
    return set(data.decode("utf-8").split())


def verbs():
    return json.loads((HERE / "verbrules_cases.json").read_text())


def irregular():
    return json.loads((DATA / "irregular_verbs.json").read_text())


# ---------------------------------------------------------------- CMUdict facts

CMU_VOWELS = {"AA", "AE", "AH", "AO", "AW", "AY", "EH", "ER", "EY", "IH", "IY",
              "OW", "OY", "UH", "UW"}
# CMUdict symbol -> the IPA letter the pages print. Build-time only: no page
# carries a CMUdict symbol, because no reader learns them.
IPA = {"AA": "ɑ", "AE": "æ", "AH": "ʌ", "AO": "ɔ", "AW": "aʊ", "AY": "aɪ", "B": "b",
       "CH": "tʃ", "D": "d", "DH": "ð", "EH": "ɛ", "ER": "ɝ", "EY": "eɪ", "F": "f",
       "G": "ɡ", "HH": "h", "IH": "ɪ", "IY": "iː", "JH": "dʒ", "K": "k", "L": "l",
       "M": "m", "N": "n", "NG": "ŋ", "OW": "oʊ", "OY": "ɔɪ", "P": "p", "R": "r",
       "S": "s", "SH": "ʃ", "T": "t", "TH": "θ", "UH": "ʊ", "UW": "uː", "V": "v",
       "W": "w", "Y": "j", "Z": "z", "ZH": "ʒ"}


def bare(ph):
    return re.sub(r"\d", "", ph)


# ---------------------------------------------------------------- output

def dump(obj):
    return json.dumps(obj, ensure_ascii=False, separators=(",", ":")) + "\n"


def write_or_check(outputs, who):
    """outputs: {Path: text}. With --check, exit 1 naming any file that would
    change; otherwise write them. Every output is swept with the ordinal guard."""
    for path, text in outputs.items():
        m = ORDINAL.search(text)
        if m:
            sys.exit("%s: %s would carry %r, which the copy guards read as a numbered "
                     "course or lesson" % (who, path.name, m.group(0)))
    if "--check" in sys.argv:
        stale = [p.name for p, text in outputs.items() if not p.exists() or p.read_text() != text]
        if stale:
            sys.exit("%s: out of date: %s" % (who, ", ".join(stale)))
        print("%s: up to date" % who)
        return False
    for path, text in outputs.items():
        path.write_text(text)
    return True
