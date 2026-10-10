"""CMUdict-based rule measurements: -ed and -s pronunciation, stress, letters to sounds, a/an, linking."""
import sys, re, json
from collections import Counter, defaultdict
sys.path.insert(0, str(__import__("pathlib").Path(__file__).resolve().parent))
from common_en import *

cmu = load_cmudict()
moby = load_moby()
forms, heads, forms_of = load_ngsl()
verbs = load_verbs()
irr = load_irregular()
print("CMUdict entries:", len(cmu), " Moby words:", len(moby), " NGSL heads:", len(heads))

def pron(w):
    p = cmu.get(w.lower())
    return p[0] if p else None

# ---------------------------------------------------------------- -ed
print("\n== -ed pronunciation on the 1,210 regular verbs ==")
ed_forms = dict(verbs["cases"]["ed"])
hit = 0; total = 0; miss = []; skipped = 0
for base in verbs["stress"]:
    bp = pron(base)
    f = None
    for cand in ed_forms[base]:
        if cand in cmu:
            f = cand; break
    if not bp or not f:
        skipped += 1; continue
    last = strip_stress(bp[-1])
    pred = "ID" if last in ("T", "D") else ("T" if last in VOICELESS else "D")
    ok = False; actual = None
    for fp in cmu[f]:
        tail = [strip_stress(x) for x in fp[-2:]]
        if tail[-1] == "D" and tail[-2] in ("IH", "AH") and last not in ("IH", "AH"):
            a = "ID"
        elif tail[-1] == "T":
            a = "T"
        elif tail[-1] == "D":
            a = "D"
        else:
            a = "?" + tail[-1]
        if actual is None: actual = a
        if a == pred: ok = True
    total += 1
    if ok and actual == pred: hit += 1
    else: miss.append("%s->%s (%s, said %s)" % (base, f, pred, actual))
show("-ed rule (t/d -> id; voiceless -> t; else d)", hit, total, miss)
print("   skipped (base or -ed form not in CMUdict):", skipped)

# ---------------------------------------------------------------- -s on verbs
print("\n== -s pronunciation on the 1,210 regular verbs ==")
s_forms = dict(verbs["cases"]["s"])
def s_rule(last):
    return "IZ" if last in SIBILANT else ("S" if last in VOICELESS else "Z")
def s_actual(fp, last):
    tail = [strip_stress(x) for x in fp[-2:]]
    if tail[-1] == "Z" and tail[-2] in ("IH", "AH") and last not in ("IH", "AH"):
        return "IZ"
    return tail[-1] if tail[-1] in ("S", "Z") else "?" + tail[-1]
hit = total = skipped = 0; miss = []
for base in verbs["stress"]:
    bp = pron(base); f = None
    for cand in s_forms[base]:
        if cand in cmu: f = cand; break
    if not bp or not f: skipped += 1; continue
    last = strip_stress(bp[-1]); pred = s_rule(last)
    acts = [s_actual(fp, last) for fp in cmu[f]]
    total += 1
    if acts[0] == pred: hit += 1
    else: miss.append("%s->%s (%s, said %s)" % (base, f, pred, acts[0]))
show("-s rule (sibilant -> iz; voiceless -> s; else z)", hit, total, miss)
print("   skipped:", skipped)

# ---------------------------------------------------------------- 2-syllable stress by POS
print("\n== Two-syllable words: noun-only vs verb-only stress ==")
def pos_only(w, kinds, not_kinds):
    p = moby.get(w)
    return bool(p) and bool(p & kinds) and not (p & not_kinds)
NOUN = {"N", "h"}; VERB = {"V", "t", "i"}; ADJ = {"A"}; ADV = {"v"}
two = [w for w in heads if w in cmu and syllables(cmu[w][0]) == 2]
print("two-syllable NGSL headwords in CMUdict:", len(two))
for label, kinds, notk, want in (("noun-only", NOUN, VERB | ADJ | ADV, 0), ("verb-only", VERB, NOUN | ADJ | ADV, 1), ("adjective-only", ADJ, NOUN | VERB | ADV, 0)):
    ws = [w for w in two if pos_only(w, kinds, notk)]
    hit = [w for w in ws if stress_index(cmu[w][0]) == want]
    miss = [w for w in ws if stress_index(cmu[w][0]) != want]
    show("%s stressed on syllable %d" % (label, want + 1), len(hit), len(ws), miss, 60)
# noun/verb pairs with two CMUdict entries differing in stress position
pairs = []
for w in two:
    p = moby.get(w, set())
    if not (p & NOUN and p & VERB): continue
    idx = {stress_index(x) for x in cmu[w] if syllables(x) == 2}
    if idx == {0, 1}: pairs.append(w)
print("noun+verb words with BOTH stress patterns in CMUdict (%d):" % len(pairs), ", ".join(sorted(pairs)))

# ---------------------------------------------------------------- suffix stress
print("\n== Suffixes and where the stress falls ==")
def syl_from_end(pron, idx):
    n = syllables(pron); return n - idx  # 1 = last syllable
tests = [("-tion/-sion", re.compile(r"(tion|sion)$"), 2), ("-ic (not -ics)", re.compile(r"ic$"), 2),
         ("-ical", re.compile(r"ical$"), 3), ("-ity", re.compile(r"ity$"), 3), ("-ate (3+ syll)", re.compile(r"ate$"), 3),
         ("-ize/-ise (3+ syll)", re.compile(r"i[sz]e$"), 3), ("-ogy/-graphy", re.compile(r"(ogy|graphy)$"), 3),
         ("-ee/-eer/-ese/-ette", re.compile(r"(ee|eer|ese|ette)$"), 1), ("-ous", re.compile(r"ous$"), None)]
for label, rx, want in tests:
    ws = [w for w in heads if rx.search(w) and w in cmu and syllables(cmu[w][0]) >= (want or 2) and (not label.startswith("-ate") or (moby.get(w, set()) & VERB))]
    if want is None:
        c = Counter(syl_from_end(cmu[w][0], stress_index(cmu[w][0])) for w in ws); print(label, len(ws), dict(c)); continue
    hit = [w for w in ws if syl_from_end(cmu[w][0], stress_index(cmu[w][0])) == want]
    miss = [w for w in ws if w not in hit]
    show("%s: stress %d from the end" % (label, want), len(hit), len(ws), miss, 60)
# neutral suffixes: stem's stressed syllable index unchanged
print("-- neutral suffixes: stress index unchanged from the stem --")
for suf in ("ly", "ness", "ment", "ful", "less", "er", "ish", "able"):
    ws = []
    for w in heads:
        if not w.endswith(suf) or w not in cmu: continue
        stem = w[:-len(suf)]
        for cand in (stem, stem + "e", stem[:-1] if stem.endswith("i") else None, stem[:-1] + "y" if stem.endswith("i") else None):
            if cand and cand in cmu and cand in heads:
                ws.append((w, cand)); break
    hit = [(w, s) for w, s in ws if stress_index(cmu[w][0]) == stress_index(cmu[s][0])]
    miss = [(w, s) for w, s in ws if (w, s) not in hit]
    show("-%s keeps the stem's stress" % suf, len(hit), len(ws), ["%s/%s" % m for m in miss], 30)

# ---------------------------------------------------------------- soft c, soft g
print("\n== Soft c and soft g (words where the letter is the only source of the sound) ==")
def letter_sound(letter, soft_ph, hard_ph, forbid_rx, extra_letters):
    hit = miss = 0; res = []; n = 0
    for w in heads:
        if w.count(letter) != 1 or re.search(forbid_rx, w) or any(ch in w for ch in extra_letters) or w not in cmu:
            continue
        i = w.index(letter)
        soft = i + 1 < len(w) and w[i + 1] in "eiy"
        phs = {strip_stress(p) for p in cmu[w][0]}
        has_soft = soft_ph in phs; has_hard = hard_ph in phs
        if not (has_soft ^ has_hard): continue
        n += 1
        pred_soft = soft
        if pred_soft == has_soft: hit += 1
        else: res.append(w)
    return hit, n, res
h, n, r = letter_sound("c", "S", "K", r"ch|ck|sc|cc|cq|qu", "skqxz")
show("c before e, i, y says s; otherwise k", h, n, r, 60)
h, n, r = letter_sound("g", "JH", "G", r"gh|ng|dg|gg|gu", "j")
show("g before e, i, y says j; otherwise g", h, n, r, 80)

# ---------------------------------------------------------------- magic e
print("\n== Silent final e makes the vowel say its name (one-syllable CVCe words) ==")
LONG = {"a": {"EY"}, "e": {"IY"}, "i": {"AY"}, "o": {"OW"}, "u": {"UW", "YUW"}}
hit = 0; n = 0; res = []
for w in heads:
    m = re.fullmatch(r"[a-z]*[^aeiou]([aeiou])[^aeiouwxy]e", w)
    if not m or w not in cmu or syllables(cmu[w][0]) != 1: continue
    v = m.group(1); phs = cmu[w][0]
    vowel = [strip_stress(p) for p in phs if p[-1].isdigit()][0]
    # y as in 'u' -> Y UW
    said_long = vowel in LONG[v] or (v == "u" and "Y" in [strip_stress(p) for p in phs] and vowel == "UW")
    n += 1
    if said_long: hit += 1
    else: res.append("%s (%s)" % (w, vowel))
show("CVCe one-syllable words: vowel says its name", hit, n, res, 80)

# ---------------------------------------------------------------- i before e
print("\n== i before e except after c (NGSL headwords) ==")
hit = n = 0; res = []; hit2 = n2 = 0; res2 = []
for w in heads:
    for m in re.finditer(r"(?=(ie|ei))", w):
        pair = m.group(1); i = m.start()
        after_c = i > 0 and w[i - 1] == "c"
        pred = "ei" if after_c else "ie"
        n += 1
        if pred == pair: hit += 1
        else: res.append(w)
        # the 'when it sounds like ee' variant: only count words whose pair vowel is IY
        if w in cmu:
            phs = [strip_stress(p) for p in cmu[w][0] if p[-1].isdigit()]
            if "IY" in phs:
                n2 += 1
                if pred == pair: hit2 += 1
                else: res2.append(w)
show("i before e except after c (every ie/ei)", hit, n, res, 80)
show("...only when the word has an ee sound somewhere (rough)", hit2, n2, res2, 60)

# ---------------------------------------------------------------- silent letters
print("\n== Silent letters ==")
def silent(label, rx, test):
    ws = [w for w in heads if re.search(rx, w) and w in cmu]
    hit = [w for w in ws if test(w, cmu[w][0])]
    show(label, len(hit), len(ws), [w for w in ws if w not in hit], 40)
    print("     words:", ", ".join(sorted(ws)[:40]))
silent("kn- : k is silent", r"^kn", lambda w, p: strip_stress(p[0]) == "N")
silent("wr- : w is silent", r"^wr", lambda w, p: strip_stress(p[0]) == "R")
silent("-mb at the end: b is silent", r"mb$", lambda w, p: strip_stress(p[-1]) == "M")
silent("-mn at the end: n is silent", r"mn$", lambda w, p: strip_stress(p[-1]) == "M")
silent("gh after a vowel: silent or f", r"[aeiou]gh", lambda w, p: "G" not in {strip_stress(x) for x in p})
silent("-alk/-olk: l is silent", r"(alk|olk)$", lambda w, p: "L" not in {strip_stress(x) for x in p})
silent("-alm/-alf: l is silent", r"(alm|alf)$", lambda w, p: "L" not in {strip_stress(x) for x in p})
silent("-stle/-sten/-stl: t is silent", r"st(le|en|ly)$", lambda w, p: strip_stress(p[-2]) != "T" and "T" not in {strip_stress(x) for x in p[-3:]})
silent("h- : words where the h is silent", r"^h[aeiou]", lambda w, p: strip_stress(p[0]) != "HH")
silent("initial ps-/pn-: p is silent", r"^p[sn]", lambda w, p: strip_stress(p[0]) != "P")

# ---------------------------------------------------------------- ough
print("\n== ough ==")
for w in sorted(w for w in heads if "ough" in w and w in cmu):
    print("  ", w, " ".join(cmu[w][0]))

# ---------------------------------------------------------------- a / an
print("\n== a / an by letter and by sound ==")
def a_an(text, label):
    toks = words(text); hitL = hitS = n = 0; resL = []; resS = []; nocmu = Counter()
    for i, t in enumerate(toks[:-1]):
        tl = t.lower()
        if tl not in ("a", "an"): continue
        nxt = toks[i + 1]; nl = nxt.lower().strip("'")
        if nl not in cmu:
            nocmu[nxt] += 1; continue
        n += 1
        predL = "an" if nl[0] in "aeiou" else "a"
        first = strip_stress(cmu[nl][0][0]); predS = "an" if first in VOWELS else "a"
        if predL == tl: hitL += 1
        else: resL.append("%s %s" % (t, nxt))
        if predS == tl: hitS += 1
        else: resS.append("%s %s" % (t, nxt))
    print("--", label, "--")
    show("by the next LETTER", hitL, n, sorted(set(resL)), 60)
    show("by the next SOUND", hitS, n, sorted(set(resS)), 60)
    print("   next word not in CMUdict:", sum(nocmu.values()), nocmu.most_common(12))
a_an(pp_novel(), "Pride and Prejudice, novel text")
a_an(wilde_play(), "The Importance of Being Earnest")
a_an(modern_docs(), "the two modern documents")
a_an(load_passage()["passage"], "the printed 949-word passage")

# ---------------------------------------------------------------- linking on the passage
print("\n== Linking on the printed passage (word boundaries with only a space between) ==")
text = norm(load_passage()["passage"])
pairs = re.findall(r"([A-Za-z][A-Za-z']*) ([A-Za-z][A-Za-z']*)", text)
kinds = Counter(); nocmu = 0; same = 0
for a, b in pairs:
    pa, pb = cmu.get(a.lower().strip("'")), cmu.get(b.lower().strip("'"))
    if not pa or not pb: nocmu += 1; continue
    fa = strip_stress(pa[0][-1]); fb = strip_stress(pb[0][0])
    k = ("V" if fa in VOWELS else "C") + ">" + ("V" if fb in VOWELS else "C")
    kinds[k] += 1
    if k == "C>C" and fa == fb: same += 1
tot = sum(kinds.values())
print("boundaries:", len(pairs), "scored:", tot, "not in CMUdict:", nocmu)
for k, v in kinds.most_common(): print("  ", k, v, pct(v, tot))
print("   C>C with the same consonant twice (said once):", same)
pw = set(w.lower().strip("'") for w in words(text)); print("passage words in CMUdict:", len([w for w in pw if w in cmu]), "of", len(pw), "missing:", sorted(w for w in pw if w not in cmu)[:30])
