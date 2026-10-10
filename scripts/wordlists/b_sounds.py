#!/usr/bin/env python3
"""Pronunciation FACTS for the English kit's letters, stress and linking modes.

    python3 scripts/wordlists/b_sounds.py --sources DIR          # rewrite the outputs
    python3 scripts/wordlists/b_sounds.py --sources DIR --check  # exit 1 if they would change

DIR holds the files docs/english-v2/measure/fetch.sh downloads (default:
docs/english-v2/measure/data). The build never runs this; the pages read the
files it writes, which are committed.

OUTPUT (scripts/wordlists/)
  b_letters.json         one row set per spelling-to-sound rule of the
                         `letters` mode: the word and the dictionary's fact
                         about the sound in question, never the rule's answer
                         -- the page runs the rule and compares
  b_stress.json          one row set per stress rule of the `stress` mode
  b_passage_sounds.json  first and last sound of every word of the printed
                         936-word passage, for the `linking` mode
  b_CMUDICT_LICENSE      the CMUdict BSD-2 notice, which must travel with
                         data derived from it

WHAT IS SHIPPED. Facts read off CMUdict's FIRST pronunciation (the stress
'ee' rule reads its LAST primary stress, because CMUdict gives engineer two):
a sound, a part count, which part is strong. Moby Part-of-Speech decides only
which headwords enter a noun, verb or adjective row set; no page carries a
Moby tag, and every row set records what it set aside and why.

THE ONE-SOURCE RULE (docs/english-v2/PLAN.md section G). The letters rules
score only words where the letter in question is the only possible source of
the sound, so `c` is scored on words with one c and no s, k, q, x or z; every
word left out is listed by reason, so a reader can count what the rule was
not tried on.
"""

import re
import sys
from collections import OrderedDict

from b_sources import (ADJ, ADV, NOUN, VERB, HERE, VOWELS, dump, last_stress_index,
                       load_cmudict, load_moby, load_ngsl, norm, passage, provenance,
                       read_pinned, sources_dir, strip_stress, stress_index, syllables,
                       vowels_of, words, write_or_check)

LICENCE_NOTE = ("Pronunciation facts derived from CMUdict, Copyright (C) 1993-2015 "
                "Carnegie Mellon University, used under its BSD two-clause licence; "
                "the full notice is scripts/wordlists/b_CMUDICT_LICENSE.")

# The vowel a CMUdict symbol stands for, written so a reader can say it. The
# page prints these words and never the dictionary's symbols.
VOWEL_SAY = {"EY": "ay", "IY": "ee", "AY": "eye", "OW": "oh", "UW": "oo",
             "AE": "a as in cat", "EH": "e as in bed", "IH": "i as in sit",
             "AA": "o as in hot", "AH": "u as in cup", "AO": "aw", "UH": "oo as in book",
             "ER": "er", "AW": "ow", "OY": "oy"}
CONS_SAY = {"SH": "sh", "ZH": "zh", "CH": "ch", "JH": "j", "N": "n", "L": "l", "R": "r",
            "T": "t", "D": "d", "S": "s", "Z": "z", "K": "k", "G": "g", "F": "f", "V": "v",
            "M": "m", "P": "p", "B": "b", "HH": "h", "W": "w", "Y": "y", "NG": "ng",
            "TH": "th", "DH": "th"}
ENDING_SAY = {"AH": "u", "ER": "ur", "UH": "oo", "IH": "i", "IY": "ee", "EH": "e",
              "AA": "ah", "AE": "a", "AO": "aw", "OW": "oh", "UW": "oo", "EY": "ay", "AY": "eye"}


def respell(phones):
    return "".join(CONS_SAY.get(p) or ENDING_SAY.get(p, p.lower()) for p in phones)


def classes(moby, w):
    p = moby.get(w, set())
    return {"N": bool(p & NOUN), "V": bool(p & VERB), "A": bool(p & ADJ), "R": bool(p & ADV)}


def only(moby, w, kind):
    c = classes(moby, w)
    return c[kind] and not any(v for k, v in c.items() if k != kind)


def vowel_groups(w):
    """Vowel-letter runs, y a vowel except first; a final silent e dropped."""
    groups = [(m.start(), m.end()) for m in re.finditer(r"[aeiou]+|(?<=.)y+", w)]
    if (len(groups) > 1 and w.endswith("e") and groups[-1] == (len(w) - 1, len(w))
            and w[-2] not in "aeiou"):
        groups.pop()
    return groups


def aligned_vowel(w, pron, pos):
    """The vowel sound at letter `pos`, when letters and parts line up 1:1."""
    groups = vowel_groups(w)
    vs = vowels_of(pron)
    if len(groups) != len(vs):
        return None
    for k, (a, b) in enumerate(groups):
        if a <= pos < b:
            return vs[k][0]
    return None


def build_letters(cmu, heads):
    first = {w: cmu[w][0] for w in heads if w in cmu}
    out = OrderedDict()

    def one_source(letter, forbid, extra, soft, hard, soft_fact, hard_fact):
        rows, aside = [], OrderedDict()
        for w in heads:
            if letter not in w:
                continue
            why = None
            if w.count(letter) != 1:
                why = "more than one %s" % letter
            elif re.search(forbid, w):
                why = "the %s is part of %s" % (letter, forbid.replace("|", ", "))
            elif any(ch in w for ch in extra):
                why = "another letter (%s) could make the same sound" % ", ".join(extra)
            elif w not in first:
                why = "not in the dictionary"
            else:
                phs = {strip_stress(p) for p in first[w]}
                if (soft in phs) == (hard in phs):
                    why = "the dictionary has both sounds or neither"
            if why:
                aside.setdefault(why, []).append(w)
            else:
                rows.append([w, soft_fact if soft in {strip_stress(p) for p in first[w]} else hard_fact])
        return {"rows": rows, "aside": aside}

    out["softc"] = one_source("c", r"ch|ck|sc|cc|cq|qu", "skqxz", "S", "K", "s", "k")
    out["softg"] = one_source("g", r"gh|ng|dg|gg|gu", "j", "JH", "G", "j", "g")

    def magic(shape, label):
        rows, aside = [], OrderedDict()
        for w in heads:
            m = re.fullmatch(shape, w)
            if not m:
                continue
            if w not in first:
                aside.setdefault("not in the dictionary", []).append(w)
                continue
            pron = first[w]
            if syllables(pron) != 1:
                aside.setdefault("the dictionary says it in more than one part", []).append(w)
                continue
            v = vowels_of(pron)[0][0]
            phs = [strip_stress(p) for p in pron]
            say = VOWEL_SAY.get(v, v.lower())
            if v == "UW" and "Y" in phs[:phs.index("UW")]:
                say = "you"
            rows.append([w, say])
        return {"rows": rows, "aside": aside, "shape": label}

    out["magic"] = magic(r"[a-z]*[^aeiou][aeiou][^aeiouwxyr]e",
                         "one part, consonant then vowel then consonant then e; the consonant not w, x, y or r")
    aside = out["magic"]["aside"]
    for w in heads:
        if re.fullmatch(r"[a-z]*[^aeiou][aeiou][wxy]e", w):
            aside.setdefault("w, x or y before the e", []).append(w)
    out["magic_r"] = magic(r"[a-z]*[^aeiou][aeiou]re",
                           "one part, consonant then vowel then r then e")

    ie_rows, ee_rows, ee_aside = [], [], OrderedDict()
    for w in heads:
        for m in re.finditer(r"(?=(ie|ei))", w):
            pos = m.start()
            ie_rows.append([w, pos, m.group(1)])
            if w not in first:
                ee_aside.setdefault("not in the dictionary", []).append(w)
                continue
            v = aligned_vowel(w, first[w], pos)
            if v is None:
                ee_aside.setdefault("its letters and parts do not line up one to one", []).append(w)
            elif v == "IY":
                ee_rows.append([w, pos, m.group(1)])
            else:
                ee_aside.setdefault("said other than ee at that place", []).append(w)
    out["ie"] = {"rows": ie_rows, "aside": OrderedDict()}
    out["ie_ee"] = {"rows": ee_rows, "aside": ee_aside}

    gh = []
    for w in heads:
        if re.search(r"[aeiou]gh", w) and w in first:
            phs = {strip_stress(p) for p in first[w]}
            gh.append([w, "g" if "G" in phs else ("f" if "F" in phs and "f" not in w else "silent")])
    out["gh"] = {"rows": gh, "aside": OrderedDict()}

    groups = [("kn", r"^kn", lambda p: p[0] == "N"), ("wr", r"^wr", lambda p: p[0] == "R"),
              ("mb", r"mb$", lambda p: p[-1] == "M"), ("mn", r"mn$", lambda p: p[-1] == "M"),
              ("lk", r"(alk|olk)$", lambda p: "L" not in p), ("lm", r"(alm|alf)$", lambda p: "L" not in p)]
    rows = []
    for name, rx, silent in groups:
        for w in heads:
            if re.search(rx, w) and w in first:
                phs = [strip_stress(p) for p in first[w]]
                rows.append([w, name, "silent" if silent(phs) else "said"])
    out["kn_wr_mb"] = {"rows": rows, "aside": OrderedDict()}

    rows = []
    for w in heads:
        if re.match(r"h[aeiou]", w) and w in first:
            rows.append([w, "said" if first[w][0] == "HH" else "silent"])
    out["h"] = {"rows": rows, "aside": OrderedDict()}

    rows = []
    for w in heads:
        if "ough" not in w or w not in first:
            continue
        pron = first[w]
        pos = w.index("ough")
        groups_ = vowel_groups(w)
        vs = [i for i, p in enumerate(pron) if p[-1].isdigit()]
        k = next(i for i, (a, b) in enumerate(groups_) if a <= pos < b)
        at = vs[k]
        v = strip_stress(pron[at])
        nxt = strip_stress(pron[at + 1]) if at + 1 < len(pron) else ""
        say = {"OW": "oh", "UW": "oo", "AO": "aw", "AA": "o", "AH": "u", "AW": "ow"}.get(v, v.lower())
        if nxt == "F":
            say += "ff"
        elif v == "AO" and nxt == "T":
            say = "aw"
        rows.append([w, say])
    out["ough"] = {"rows": rows, "aside": OrderedDict()}

    def ending(rx, take):
        rows = []
        for w in heads:
            if re.search(rx, w) and w in first:
                phs = [strip_stress(p) for p in first[w]]
                rows.append([w, respell(take(phs))])
        return {"rows": rows, "aside": OrderedDict()}

    out["tion"] = ending(r"tion$", lambda p: p[-3:])
    out["sion"] = ending(r"sion$", lambda p: p[-3:])
    out["ture"] = ending(r"ture$", lambda p: p[-2:] if p[-1] == "ER" else p[-3:])
    out["cial"] = ending(r"(cial|tial)$", lambda p: p[-3:])
    return out


def build_stress(cmu, moby, heads):
    first = {w: cmu[w][0] for w in heads if w in cmu}
    out = OrderedDict()
    two = [w for w in heads if w in first and syllables(first[w]) == 2]
    for rule, kind in (("nouns2", "N"), ("verbs2", "V"), ("adj2", "A")):
        out[rule] = {"rows": [[w, stress_index(first[w]) + 1] for w in two if only(moby, w, kind)],
                     "aside": OrderedDict()}
    aside = OrderedDict()
    for w in two:
        if not any(only(moby, w, k) for k in "NVA"):
            c = classes(moby, w)
            why = ("Moby gives it no part of speech" if not any(c.values())
                   else "more than one part of speech, or an adverb")
            aside.setdefault(why, []).append(w)
    out["nouns2"]["aside"] = aside
    pairs = []
    for w in two:
        c = classes(moby, w)
        if c["N"] and c["V"]:
            idx = {stress_index(x) for x in cmu[w] if syllables(x) == 2}
            if idx == {0, 1}:
                pairs.append([w])
    out["pairs"] = {"rows": pairs, "aside": OrderedDict()}

    endings = [("tion", r"(tion|sion)$", 2, False), ("ic", r"ic$", 2, False),
               ("ical", r"ical$", 3, False), ("ity", r"ity$", 3, False),
               ("ate", r"ate$", 3, True), ("ize", r"i[sz]e$", 3, False),
               ("ee", r"(ee|eer|ese|ette)$", 2, False)]
    for rule, rx, need, verb_only in endings:
        rows, aside = [], OrderedDict()
        for w in heads:
            if not re.search(rx, w):
                continue
            if w not in first:
                aside.setdefault("not in the dictionary", []).append(w)
                continue
            n = syllables(first[w])
            if n < need:
                aside.setdefault("fewer than %s parts" % ("two", "two", "three")[need - 1], []).append(w)
                continue
            if verb_only and not classes(moby, w)["V"]:
                aside.setdefault("not a verb", []).append(w)
                continue
            idx = last_stress_index(first[w]) if rule == "ee" else stress_index(first[w])
            rows.append([w, n, idx + 1])
        out[rule] = {"rows": rows, "aside": aside}

    for suf in ("ly", "ness", "ment", "er", "ful", "able"):
        rows = []
        for w in heads:
            if not w.endswith(suf) or w not in first:
                continue
            stem = w[:-len(suf)]
            for cand in (stem, stem + "e", stem[:-1] if stem.endswith("i") else None,
                         stem[:-1] + "y" if stem.endswith("i") else None):
                if cand and cand in first and cand in heads:
                    rows.append([w, cand, stress_index(first[w]) + 1, stress_index(first[cand]) + 1])
                    break
        out[suf] = {"rows": rows, "aside": OrderedDict()}

    code = {"AH": "u", "ER": "r", "IH": "i", "IY": "e"}
    rows = []
    for w in heads:
        if w not in first or syllables(first[w]) < 2:
            continue
        weak = "".join(code.get(v, "x") for v, s in vowels_of(first[w]) if s == "0")
        if weak:
            rows.append([w, weak])
    out["schwa"] = {"rows": rows, "aside": OrderedDict()}
    return out


def build_passage(cmu):
    text = norm(passage())
    out = OrderedDict()
    missing = []
    for t in words(text):
        w = t.lower().strip("'")
        if w in out or w in missing:
            continue
        if w in cmu:
            p = [strip_stress(x) for x in cmu[w][0]]
            out[w] = p[0] + " " + p[-1]
        else:
            missing.append(w)
    return out, sorted(missing)


def main(argv):
    src = sources_dir(argv)
    cmu = load_cmudict(src)
    moby = load_moby(src)
    _forms, heads = load_ngsl()
    licence = read_pinned(src, "cmudict_LICENSE").decode("utf-8")

    letters = build_letters(cmu, heads)
    stress = build_stress(cmu, moby, heads)
    sounds, missing = build_passage(cmu)
    prov_c = provenance(["cmudict.dict"])
    prov_cm = provenance(["cmudict.dict", "mobypos.txt"])
    outputs = {
        HERE / "b_letters.json": dump({
            "note": "One row set per spelling-to-sound rule: [word, the dictionary's fact]. "
                    "Facts from the first CMUdict pronunciation of each NGSL headword. "
                    + LICENCE_NOTE,
            "sources": prov_c, "rules": letters}),
        HERE / "b_stress.json": dump({
            "note": "One row set per stress rule. Parts and the strong part are counted from "
                    "the front, from the first CMUdict pronunciation (the ee rule reads its "
                    "last primary stress). Moby Part-of-Speech chose which headwords are "
                    "noun-only, verb-only or adjective-only at build time; no tag is shipped. "
                    + LICENCE_NOTE,
            "sources": prov_cm, "rules": stress}),
        HERE / "b_passage_sounds.json": dump({
            "note": "First and last sound (CMUdict symbol, stress removed) of every word of "
                    "content/english/data/wordorder_passage.json, apostrophes normalised. "
                    + LICENCE_NOTE,
            "sources": prov_c, "sounds": sounds, "missing": missing}),
        HERE / "b_CMUDICT_LICENSE": licence,
    }
    write_or_check(outputs, argv)


if __name__ == "__main__":
    main(sys.argv[1:])
