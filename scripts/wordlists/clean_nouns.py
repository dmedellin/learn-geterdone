#!/usr/bin/env python3
"""Build the noun list the plural rule is scored on.

    python3 scripts/wordlists/clean_nouns.py          # rewrite plural_nouns.json
    python3 scripts/wordlists/clean_nouns.py --check  # exit 1 if it would change

Run it by hand when a source or a rule below changes; the build never runs it.
Sources are read from docs/english-v2/measure/data/ (fetch.sh) or --sources DIR.

INPUT   ngsl.tsv (headwords and the forms the NGSL records), the Moby
        Part-of-Speech list (which headwords are nouns), and the reference
        dictionary clean_verbs.py uses (which recorded forms are words).
OUTPUT  plural_nouns.json:
          rows      every NGSL headword Moby tags as a noun that has a plural
                    the dictionary confirms, with every such plural;
          noplural  the headwords Moby tags ONLY as a noun for which the
                    dictionary confirms no plural at all;
          excluded  every other noun headword, each with its reason.

THE TEST FOR A PLURAL. A form the NGSL records for the headword stands when
the dictionary has it (or its American spelling) and it has the shape of a
plural of that headword: +s, +es, -y to -ies, f or fe to ves, -is to -es, -us
to -i, -um or -on to -a, -ex or -ix to -ices, -man to -men.

FOUR JUDGEMENTS THE DICTIONARY CANNOT MAKE, listed by name below.

  * IRREGULAR: the hand list of irregular plurals OVERRIDES the regular forms
    the dictionary confirms, because those are verb forms or rarities (mans,
    foots, mouses, childs, dies). person keeps persons beside people: both
    are in use, and the NGSL records persons for it.
  * NGSL_GAPS: three plurals the dictionary has and the NGSL list files
    elsewhere (life, lives), added by name so a noun with a plural is not
    printed as a noun without one.
  * STOPLIST: Moby tags function words as nouns somewhere (and, as, at, he,
    six); they are set aside, each with its reason, rather than scored.
  * A headword Moby also tags as a verb, adjective or adverb, with no plural
    confirmed, is set aside: nothing says it is a noun that never takes one.
"""

import re
import sys

import en_sources as S

OUT = S.HERE / "plural_nouns.json"

IRREGULAR = {
    "child": ["children"], "man": ["men"], "woman": ["women"], "foot": ["feet"],
    "tooth": ["teeth"], "mouse": ["mice"], "goose": ["geese"], "ox": ["oxen"],
    "louse": ["lice"], "die": ["dice"], "penny": ["pence"],
    "person": ["people", "persons"],
}
# Plurals the dictionary has that the NGSL does not record for the headword
# (it files lives under live, statistics under statistics). Added, by name.
NGSL_GAPS = {"life": ["lives"], "statistic": ["statistics"], "status": ["statuses"]}
# -man compounds take -men; human is not a compound of man.
NOT_MAN_COMPOUND = {"human"}

_STOP = {
    "a pronoun": "i he she it you who mine anybody somebody nobody anything nothing none",
    "an article or a word of quantity": "a no all few many more most other little plenty",
    "a preposition or a word of direction": ("above at behind beyond by despite for in of off on "
                                             "over per till up down out away forth near"),
    "a joining word": "and as but if nor while",
    "a question word": "how when where why",
    "an adverb": "else far now once so there",
    "a number word": ("one two three four five six seven eight nine ten eleven twelve thirteen "
                      "fourteen fifteen sixteen seventeen eighteen nineteen twenty thirty forty "
                      "fifty sixty seventy eighty ninety hundred thousand million billion "
                      "trillion quadrillion quintillion dozen"),
    "a greeting": "hi hello",
    "a verb: the NGSL's forms of it are the verb's (does, goes)": "do go",
}
STOPLIST = {w: "Moby tags it as a noun somewhere, but it is %s" % why
            for why, ws in _STOP.items() for w in ws.split()}


def american(f):
    return [f, re.sub(r"our", "or", f), re.sub(r"re$", "er", f), re.sub(r"res$", "ers", f),
            re.sub(r"is(e|es)$", r"iz\1", f)]


def plural_shape(w, f):
    return (f in (w + "s", w + "es") or (w.endswith("y") and f == w[:-1] + "ies")
            or (re.search(r"fe?$", w) and f == re.sub(r"fe?$", "ves", w))
            or (w.endswith("is") and f == w[:-2] + "es") or (w.endswith("us") and f == w[:-2] + "i")
            or (re.search(r"(um|on)$", w) and f == w[:-2] + "a")
            or (re.search(r"(ex|ix)$", w) and f == w[:-2] + "ices")
            or (w.endswith("man") and f == w[:-3] + "men"))


def build():
    moby = S.moby()
    forms, heads, forms_of = S.ngsl()
    words = S.dictionary()

    def confirmed(f):
        return any(x in words for x in american(f))

    nouns = sorted(w for w in heads if (moby.get(w, set()) & S.NOUN) and w.isalpha())
    rows, noplural, excluded, irregular = [], [], {}, {}
    noun_only = 0
    for w in nouns:
        if w in STOPLIST:
            excluded[w] = STOPLIST[w]
            continue
        only = not (moby[w] & (S.VERB | S.ADJ | S.ADV))
        noun_only += only
        if w in IRREGULAR:
            pl = IRREGULAR[w]
            irregular[w] = pl
        elif w.endswith("man") and w not in NOT_MAN_COMPOUND:
            pl = [w[:-3] + "men"]
            irregular[w] = pl
        else:
            pl = [f for f in forms_of[w] if f != w and confirmed(f) and plural_shape(w, f)]
            pl += [f for f in NGSL_GAPS.get(w, []) if f not in pl and confirmed(f)]
        if pl:
            rows.append((w, pl))
        elif only:
            noplural.append(w)
        else:
            excluded[w] = ("Moby also tags it as a verb, adjective or adverb, and the "
                           "dictionary confirms no plural for it")

    def rel(w, f):
        return "~" + f[len(w):] if f.startswith(w) else f

    text = "|".join("%s %s" % (w, "/".join(rel(w, f) for f in pl)) for w, pl in rows)
    data = {
        "note": ("Every NGSL headword the Moby Part-of-Speech list tags as a noun, with "
                 "each plural the NGSL records for it that the reference dictionary "
                 "confirms. rows: headword, a space, the plurals separated by /, with ~ "
                 "standing for the headword (box ~es is box, boxes). noplural: the "
                 "headwords Moby tags only as a noun with no plural confirmed. "
                 "irregular: the hand list that overrides a confirmed regular form. "
                 "excluded: every other noun headword and why. Built by "
                 "scripts/wordlists/clean_nouns.py. Adapted from the " + S.NGSL_NOTE +
                 "; this file is CC BY-SA 4.0. Parts of speech from the Moby list, "
                 "public domain, used at build time only."),
        "sources": S.provenance("mobypos.txt"),
        "dictionary": S.DICTIONARY_NAME,
        "rows": text,
        "noun_only": noun_only,
        "noplural": noplural,
        "irregular": irregular,
        "excluded": dict(sorted(excluded.items())),
    }
    return data


def main():
    data = build()
    if S.write_or_check({OUT: S.dump(data)}, "clean_nouns"):
        print("%d nouns with a plural, %d noun-only with none (of %d noun-only), %d set aside"
              % (data["rows"].count("|") + 1, len(data["noplural"]), data["noun_only"],
                 len(data["excluded"])))


if __name__ == "__main__":
    main()
