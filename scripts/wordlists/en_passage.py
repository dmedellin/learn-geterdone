"""Cut content/english/data/wordorder_passage.json from the pinned novel.

The printed passage is one stretch of Pride and Prejudice, from "very
ungracious sensation" to the "Mr." that follows "nothing else to do." It is
cut from en_sources.novel(), which already drops the 1894 illustration
captions, and the edition's chapter headings ("CHAPTER LIII.") are taken out
too, so every printed word is Austen's prose. Whitespace is run together into
single spaces; nothing else is changed (underscores, the edition's italics,
stay, and the pages remove them when they print).

The "verbs" and "aux" lists are the lexicon printed with the passage; they are
carried over from the committed file unchanged.

    /usr/bin/python3 scripts/wordlists/en_passage.py           # write
    /usr/bin/python3 scripts/wordlists/en_passage.py --check   # exit 1 if stale
"""

import json
import re

from en_sources import DATA, MissingSources, dump, novel, write_or_check

START = "very ungracious sensation"
END = "They will have nothing else to do.” Mr."
CHAPTER = re.compile(r"\bCHAPTER\s+[IVXLC]+\.")
SOURCE = ("Pride and Prejudice, Jane Austen, 1813. Public domain. Novel text only: "
          "the Gutenberg edition carries an 1894 preface, illustration captions and "
          "chapter headings that are not Austen's prose, and all three are excluded here.")


def cut():
    text = CHAPTER.sub(" ", novel())
    flat = re.sub(r"\s+", " ", text)
    a = flat.index(START)
    b = flat.index(END, a) + len(END)
    return flat[a:b]


def main():
    path = DATA / "wordorder_passage.json"
    old = json.loads(path.read_text(encoding="utf-8"))
    out = {"source": SOURCE, "passage": cut(), "verbs": old["verbs"], "aux": old["aux"]}
    write_or_check({path: dump(out)}, "en_passage")


if __name__ == "__main__":
    try:
        main()
    except MissingSources as e:
        raise SystemExit(str(e))
