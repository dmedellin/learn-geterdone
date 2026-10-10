#!/usr/bin/env python3
"""The printed lines and the play excerpt for the English kit's second half.

    python3 scripts/wordlists/b_concordance.py --sources DIR          # rewrite the outputs
    python3 scripts/wordlists/b_concordance.py --sources DIR --check  # exit 1 if they would change

DIR holds the files docs/english-v2/measure/fetch.sh downloads (default:
docs/english-v2/measure/data). The build never runs this; the pages read the
files it writes, which are committed.

OUTPUT (content/english/data/)
  b_wilde_excerpt.json       the 1,975-word run of Act II of The Importance of
                             Being Earnest, from "CECILY. Oh, I merely came
                             back to water the roses." to "if I may speak
                             candidly--", cut at speech boundaries
                             (contractions, coverage)
  b_compare_concordance.json every -er/-est form of an adjective and every
                             more/most + adjective in the novel, the play and
                             the two modern documents, with the adjective, its
                             parts (CMUdict) and the form used (compare)
  b_phrasal_concordance.json every verb + particle and verb + preposition +
                             pronoun line in the novel and the play (phrasal)

WHAT DECIDES A ROW, so a reviewer can disagree with a line rather than a
method. An adjective is an NGSL headword Moby tags as an adjective and not as a
noun or verb, or one of the adjectives named in HAND_ADJECTIVES (Moby tags
happy, quiet and simple as nouns or verbs as well). A verb is a form on the
two printed verb lists (scripts/wordlists/verbrules_cases.json and
content/english/data/irregular_verbs.json). Moby and CMUdict are read here and
nowhere else; the files carry the facts, not the lists.
"""

import json
import re
import sys
from collections import Counter, OrderedDict, defaultdict

from b_sources import (ADJ, NOUN, ROOT, VERB, dump, load_cmudict, load_moby, load_ngsl,
                       modern_docs, norm, novel, play, provenance, sources_dir, syllables,
                       words, write_or_check)

DATA = ROOT / "content" / "english" / "data"
CMU_NOTE = ("The parts of each adjective are counted from CMUdict, Copyright (C) 1993-2015 "
            "Carnegie Mellon University, BSD two-clause licence; the full notice is "
            "scripts/wordlists/b_CMUDICT_LICENSE.")

# Adjectives the comparative scan accepts although Moby also tags them as a
# noun or a verb. Carried over unchanged from the design measurement
# (docs/english-v2/measure/m_follow.py, part j), so the page and the design
# count the same tokens.
HAND_ADJECTIVES = set("""happy pretty early easy busy lucky angry heavy lovely pleasant quiet
simple narrow clever gentle common handsome polite stupid remote severe minute little great
small young old fine high low long short strong poor rich large big deep wide late near dear
sweet warm cold hot kind proud wise safe sure fair dark light bright soft hard fast slow quick
cheap thick thin clean full few new cool fond grave idle humble noble able feeble subtle
sincere obscure mature profound elegant agreeable amiable""".split())

# -er/-est words that are not comparatives of an adjective, set aside by name.
NOT_COMPARATIVE = set("""other over under ever never after rather former latter either neither
whether together farther further upper inner outer utter mere best worst least most interest
rest forest request guest chest test nest harvest manifest protest contest arrest invest
suggest digest quest vest west east modest honest earnest""".split())

PARTICLES = ("up", "out", "off", "down", "away", "back", "over")
PREPOSITIONS = ("at", "to", "for", "of", "with")
# Object pronouns; never `her`, which is also the possessive (lift up her eyes).
OBJECTS = ("me", "him", "us", "them", "it", "you")
NOT_PHRASAL = {"be", "have", "do", "will", "can", "may", "must", "shall", "need", "dare"}


def wilde_excerpt(src):
    p = play(src)
    a = p.index("CECILY.\nOh, I merely came back to water the roses.")
    b = p.index("if I may speak candidly—") + len("if I may speak candidly—")
    speeches = []
    for block in re.split(r"\n\s*\n", p[a:b].strip()):
        lines = [ln.strip() for ln in block.strip().split("\n") if ln.strip()]
        if not lines:
            continue
        if re.fullmatch(r"[A-Z][A-Z .]+\.", lines[0]) and len(lines) > 1:
            speeches.append(lines[0] + " " + " ".join(lines[1:]))
        else:
            speeches.append(" ".join(lines))
    return "\n\n".join(speeches)


def window(toks, i, before, after):
    """[the words around token i, as printed; where token i stands in them]."""
    start = max(0, i - before)
    return [" ".join(toks[start:i + after + 1]), i - start]


def comparatives(text, heads, moby, cmu):
    def is_adj(c):
        p = moby.get(c, set())
        return c in cmu and ((c in heads and p & ADJ and not p & (NOUN | VERB)) or c in HAND_ADJECTIVES)

    def stem_of(t):
        for suf in ("iest", "ier", "est", "er"):
            if t.endswith(suf) and len(t) > len(suf) + 2:
                stem = t[:-len(suf)]
                cands = [stem, stem + "e"]
                if suf.startswith("i"):
                    cands.append(stem + "y")
                if len(stem) > 2 and stem[-1] == stem[-2]:
                    cands.append(stem[:-1])
                for c in cands:
                    if is_adj(c):
                        return c
        return None

    toks = words(text)
    low = [t.lower() for t in toks]
    rows, aside = [], Counter()
    for i, t in enumerate(low):
        stem = stem_of(t)
        if stem:
            if stem in NOT_COMPARATIVE or t in NOT_COMPARATIVE:
                aside[(t, "not a comparative of an adjective")] += 1
                continue
            rows.append(window(toks, i, 3, 3) + [stem, syllables(cmu[stem][0]), "i"])
        elif t in ("more", "most") and i + 1 < len(low):
            nxt = low[i + 1]
            p = moby.get(nxt, set())
            if nxt in heads and p & ADJ and nxt in cmu:
                if p & (NOUN | VERB):
                    aside[(t + " " + nxt, "the next word is also a noun or a verb")] += 1
                    continue
                rows.append(window(toks, i, 3, 4) + [nxt, syllables(cmu[nxt][0]), "m"])
    return rows, [[w, why, n] for (w, why), n in
                  sorted(aside.items(), key=lambda kv: (-kv[1], kv[0]))]


def verb_forms():
    verbs = json.loads((ROOT / "scripts" / "wordlists" / "verbrules_cases.json").read_text())
    irr = json.loads((DATA / "irregular_verbs.json").read_text())
    forms = defaultdict(set)
    for slot in ("s", "ing", "ed"):
        for b, fs in verbs["cases"][slot]:
            forms[b] |= set(fs) | {b}
    for v in irr["verbs"]:
        b = v["base"]
        forms[b] |= {b} | set(v["past"].split("/")) | set(v["pp"].split("/"))
        forms[b].add(b + "s")
        forms[b].add((b[:-1] if b.endswith("e") else b) + "ing")
    extra = {"sit": {"sitting"}, "get": {"getting"}, "put": {"putting"}, "set": {"setting"},
             "run": {"running"}, "shut": {"shutting"}, "give": {"giving"}, "take": {"taking"},
             "make": {"making"}, "come": {"coming"}, "go": {"goes"}, "have": {"has", "having"},
             "do": {"does"}}
    for b, e in extra.items():
        forms[b] |= e
    form2base = {}
    for b in sorted(forms):
        for f in sorted(forms[b]):
            form2base.setdefault(f, b)
    return form2base


def phrasal(text, form2base):
    toks = words(text)
    low = [t.lower() for t in toks]
    part_rows, prep_rows = [], []
    for i in range(len(low) - 2):
        base = form2base.get(low[i])
        if not base or base in NOT_PHRASAL:
            continue
        if low[i + 1] in PARTICLES or (low[i + 1] in OBJECTS and low[i + 2] in PARTICLES):
            part_rows.append(window(toks, i, 2, 3) + [base])
        if low[i + 1] in PREPOSITIONS and low[i + 2] in OBJECTS:
            prep_rows.append(window(toks, i, 1, 2) + [base])
    return part_rows, prep_rows


def main(argv):
    src = sources_dir(argv)
    cmu = load_cmudict(src)
    moby = load_moby(src)
    _forms, heads = load_ngsl()
    novel_text = norm(novel(src))
    play_text = norm(play(src))
    modern_text = norm(modern_docs())

    excerpt = wilde_excerpt(src)
    comp = OrderedDict()
    for name, text in (("austen", novel_text), ("wilde", play_text), ("modern", modern_text)):
        rows, aside = comparatives(text, heads, moby, cmu)
        comp[name] = {"rows": rows, "aside": aside}
    form2base = verb_forms()
    phr = OrderedDict()
    for name, text in (("austen", novel_text), ("wilde", play_text)):
        part_rows, prep_rows = phrasal(text, form2base)
        phr[name] = {"rows": part_rows, "prep": prep_rows}

    outputs = {
        DATA / "b_wilde_excerpt.json": dump({
            "note": "The Importance of Being Earnest, Oscar Wilde, 1895. Public domain. Act II, "
                    "from the speech beginning “Oh, I merely came back to water the roses” "
                    "to “if I may speak candidly—”, cut at speech boundaries; each "
                    "speech is one paragraph led by its speaker, stage directions kept.",
            "sources": provenance(["pg844.txt"]),
            "words": len(words(excerpt)), "text": excerpt}),
        DATA / "b_compare_concordance.json": dump({
            "note": "Every -er or -est form of an adjective, and every more or most directly "
                    "before an adjective: [the words around it as printed, where the form stands "
                    "in them (counting from 0), the adjective, its parts, i (-er/-est) or m "
                    "(more/most)]. An adjective is an NGSL headword Moby Part-of-Speech tags "
                    "as an adjective and not a noun or verb, or one of the hand list in "
                    "scripts/wordlists/b_concordance.py; aside lists what was set aside, with "
                    "the reason and the count: more or most before a word Moby also tags as "
                    "a noun or verb, and -er/-est words named as not comparatives. The novel "
                    "(1813) whole, the play (1895) whole, and the two modern documents. "
                    + CMU_NOTE,
            "sources": provenance(["pg1342.txt", "pg844.txt", "cmudict.dict", "mobypos.txt"]),
            "texts": comp}),
        DATA / "b_phrasal_concordance.json": dump({
            "note": "rows: a verb form from the two printed verb lists followed by a particle "
                    "(up out off down away back over), directly or with one object pronoun "
                    "between. prep: a verb form, one of at to for of with, then an object "
                    "pronoun. Each row: [the words around it as printed, where the verb "
                    "stands in them (counting from 0), the verb's base form]; the page reads "
                    "the particle, preposition and pronoun off the words that follow. Her is never counted as "
                    "an object, because it is also the possessive. The novel (1813) and the "
                    "play (1895), whole.",
            "sources": provenance(["pg1342.txt", "pg844.txt"]),
            "texts": phr}),
    }
    write_or_check(outputs, argv)
    for name, d in comp.items():
        print("compare %s: %d rows, %d set aside" % (name, len(d["rows"]), sum(row[-1] for row in d["aside"])))
    for name, d in phr.items():
        print("phrasal %s: %d particle rows, %d preposition rows" % (name, len(d["rows"]), len(d["prep"])))
    print("excerpt: %d words" % len(words(excerpt)))


if __name__ == "__main__":
    main(sys.argv[1:])
