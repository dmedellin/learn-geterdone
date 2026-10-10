#!/usr/bin/env python3
"""Build the adjective list the -ly rule is scored on.

    python3 scripts/wordlists/clean_adjectives.py          # rewrite ly_adjectives.json
    python3 scripts/wordlists/clean_adjectives.py --check  # exit 1 if it would change

Run it by hand; the build never runs it. Sources: docs/english-v2/measure/data/
(fetch.sh) or --sources DIR.

THE LIST. Every NGSL headword the Moby Part-of-Speech list tags as an
adjective and as nothing else that is a content word (no noun, verb or adverb
tag): words such as hard or fast, which are adverbs already, are left out
because the question "what is its -ly adverb" has two answers for them.

THE ADVERBS. For each adjective, every -ly spelling a writer could reach by any
of the spelling changes the lesson teaches (+ly, +ally, -y to -ily, -le to -ly,
-e dropped before -ly, -ll to -lly) that the reference dictionary has. An
adjective with none is listed under `none`, not scored: the page cannot score
a rule on a word that has no answer.

WHAT THE DICTIONARY CANNOT SAY. It confirms hardly, lately and highly as
words; it cannot say that they do not mean hard, late and high. The lessons
name the flat adverbs in prose; this file does not count them.
"""

import en_sources as S

OUT = S.HERE / "ly_adjectives.json"


def candidates(w):
    out = [w + "ly", w + "ally"]
    if w.endswith("y"):
        out.append(w[:-1] + "ily")
    if w.endswith("le"):
        out.append(w[:-1] + "y")
    if w.endswith("e"):
        out.append(w[:-1] + "ly")
    if w.endswith("ll"):
        out.append(w + "y")
    seen = []
    for c in out:
        if c not in seen:
            seen.append(c)
    return seen


def build():
    moby = S.moby()
    forms, heads, forms_of = S.ngsl()
    words = S.dictionary()
    pool = sorted(w for w in heads if (moby.get(w, set()) & S.ADJ) and w.isalpha()
                  and not (moby[w] & (S.NOUN | S.VERB | S.ADV)))
    rows, none = [], []
    for w in pool:
        have = [c for c in candidates(w) if c in words]
        if have:
            rows.append("%s %s" % (w, "/".join("~" + c[len(w):] if c.startswith(w) else c
                                               for c in have)))
        else:
            none.append(w)
    return {
        "note": ("Every NGSL headword the Moby Part-of-Speech list tags only as an "
                 "adjective, with every -ly adverb spelling the reference dictionary "
                 "has for it. rows: adjective, a space, the spellings separated by /, "
                 "with ~ standing for the adjective (basic ~ally is basic, basically). "
                 "none: the adjectives with no -ly adverb the dictionary has. Built by "
                 "scripts/wordlists/clean_adjectives.py. Adapted from the " + S.NGSL_NOTE +
                 "; this file is CC BY-SA 4.0. Parts of speech from the Moby list, "
                 "public domain, used at build time only."),
        "sources": S.provenance("mobypos.txt"),
        "dictionary": S.DICTIONARY_NAME,
        "rows": "|".join(rows),
        "none": none,
    }


def main():
    data = build()
    if S.write_or_check({OUT: S.dump(data)}, "clean_adjectives"):
        print("%d adjectives: %d with an -ly adverb, %d with none"
              % (data["rows"].count("|") + 1 + len(data["none"]),
                 data["rows"].count("|") + 1, len(data["none"])))


if __name__ == "__main__":
    main()
