#!/usr/bin/env python3
"""Take the pronunciation facts the English labs need out of CMUdict.

    python3 scripts/wordlists/sounds.py          # rewrite the outputs
    python3 scripts/wordlists/sounds.py --check  # exit 1 if any would change

Run it by hand after clean_nouns.py and concordance.py, whose outputs it reads;
the build never runs it. CMUdict is read from docs/english-v2/measure/data/
(fetch.sh) or --sources DIR. It is BSD-2-Clause, and its notice travels with
the data in scripts/wordlists/CMUDICT_LICENSE.

A FACT, NOT A JUDGEMENT. Every value here is a lookup: the last sound of a
word in CMUdict's first pronunciation, the first sound of a word, the sound
CMUdict records at the end of a written -ed or -s form. No page carries a
CMUdict symbol; sounds are written in the IPA letters a reader can learn.

OUTPUTS
  verb_sounds.json  verbs: for every regular verb of verbrules_cases.json, its
                    last sound and the sound its first -ed and -s forms in
                    CMUdict end in; plurals: the same for every noun of
                    plural_nouns.json with a regular plural (+s, +es, -ies).
                    A word CMUdict lacks, or whose forms it lacks, is listed
                    under skipped, not scored.
  an_sounds.json    for every word that follows a or an in an_concordance.json,
                    whether CMUdict's first pronunciation begins with a vowel
                    sound (V) or a consonant sound (C), and that sound.
"""

import json
import re

import en_sources as S

OUT_VERBS = S.HERE / "verb_sounds.json"
OUT_AN = S.HERE / "an_sounds.json"


def ipa(ph):
    b = S.bare(ph)
    if b == "AH" and ph.endswith("0"):
        return "ə"
    if b == "ER" and ph.endswith("0"):
        return "ɚ"
    return S.IPA[b]


def ending(pron, base_last, kind):
    """The sound a written -ed (kind 'ed') or -s ('s') form ends in, from its
    CMUdict pronunciation: t, d or id; s, z or iz. The extra part (id, iz) is
    read as a weak vowel before the last consonant that the base does not have."""
    tail = [S.bare(x) for x in pron[-2:]]
    last = tail[-1]
    extra = len(tail) == 2 and tail[0] in ("IH", "AH") and S.bare(base_last) not in ("IH", "AH")
    if kind == "ed":
        if last == "D" and extra:
            return "id"
        return {"T": "t", "D": "d"}.get(last, "?")
    if last == "Z" and extra:
        return "iz"
    return {"S": "s", "Z": "z"}.get(last, "?")


def rows_for(pairs, cmu, kind):
    """pairs: [(base, [recorded forms])]. -> (rows, skipped)."""
    rows, skipped = [], {}
    for base, forms in pairs:
        if base not in cmu:
            skipped[base] = "CMUdict does not carry %s" % base
            continue
        form = next((f for f in forms if f in cmu), None)
        if form is None:
            skipped[base] = "CMUdict does not carry %s" % " or ".join(forms)
            continue
        bp = cmu[base][0]
        rows.append("%s %s %s %s" % (base, form if not form.startswith(base) else "~" + form[len(base):],
                                     ipa(bp[-1]), ending(cmu[form][0], bp[-1], kind)))
    return rows, skipped


def build():
    cmu = S.cmudict()
    verbs = S.verbs()
    nouns = json.loads((S.HERE / "plural_nouns.json").read_text())
    ed_rows, ed_skip = rows_for(verbs["cases"]["ed"], cmu, "ed")
    s_rows, s_skip = rows_for(verbs["cases"]["s"], cmu, "s")
    plural_pairs = []
    for row in nouns["rows"].split("|"):
        w, pl = row.split(" ")
        forms = [w + f[1:] if f.startswith("~") else f for f in pl.split("/")]
        regular = [f for f in forms if f in (w + "s", w + "es", w[:-1] + "ies")]
        if regular:
            plural_pairs.append((w, regular))
    pl_rows, pl_skip = rows_for(plural_pairs, cmu, "s")
    verb_sounds = {
        "note": ("Rows: word, the form scored (~ stands for the word), the word's last "
                 "sound, and the sound the form ends in, all from CMUdict's first "
                 "pronunciation of each (BSD-2-Clause; see scripts/wordlists/"
                 "CMUDICT_LICENSE). ed and s: the regular verbs of verbrules_cases.json "
                 "and their first -ed or -s spelling CMUdict carries. plural: the nouns of "
                 "plural_nouns.json with a regular plural. skipped: words CMUdict does not "
                 "carry, listed and not scored. Built by scripts/wordlists/sounds.py; the "
                 "word lists are adapted from the " + S.NGSL_NOTE + "."),
        "sources": S.provenance("cmudict.dict"),
        "ed": "|".join(ed_rows), "s": "|".join(s_rows), "plural": "|".join(pl_rows),
        "skipped": {"ed": ed_skip, "s": s_skip, "plural": pl_skip},
    }
    an = json.loads((S.DATA / "an_concordance.json").read_text())
    nxt = sorted({r[3].lower() for r in an["rows"]})
    first = {}
    for w in nxt:
        key = w if w in cmu else (w[:-2] if w.endswith("'s") and w[:-2] in cmu else None)
        if key:
            ph = cmu[key][0][0]
            first[w] = ("V" if S.bare(ph) in S.CMU_VOWELS else "C") + " " + ipa(ph)
    an_sounds = {
        "note": ("For every word that follows a or an in content/english/data/"
                 "an_concordance.json: V if CMUdict's first pronunciation of it (or of it "
                 "without 's) begins with a vowel sound, C if with a consonant sound, and "
                 "that sound. A word CMUdict does not carry is absent, and the page lists "
                 "it rather than scoring it. CMUdict is BSD-2-Clause; see scripts/wordlists/"
                 "CMUDICT_LICENSE. Built by scripts/wordlists/sounds.py."),
        "sources": S.provenance("cmudict.dict"),
        "first": first,
    }
    return verb_sounds, an_sounds


def main():
    vs, an = build()
    if S.write_or_check({OUT_VERBS: S.dump(vs), OUT_AN: S.dump(an)}, "sounds"):
        print("-ed %d rows (%d skipped), -s %d (%d), plural %d (%d); %d next words with a first sound"
              % (vs["ed"].count("|") + 1, len(vs["skipped"]["ed"]), vs["s"].count("|") + 1,
                 len(vs["skipped"]["s"]), vs["plural"].count("|") + 1, len(vs["skipped"]["plural"]),
                 len(an["first"])))


if __name__ == "__main__":
    main()
