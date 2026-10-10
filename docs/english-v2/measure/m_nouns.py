"""Noun plurals and -ly adverbs: rules scored on NGSL headwords against dictionary-confirmed forms."""
import sys, re, json
from collections import Counter
sys.path.insert(0, str(__import__("pathlib").Path(__file__).resolve().parent))
from common_en import *

cmu = load_cmudict(); moby = load_moby(); forms, heads, forms_of = load_ngsl(); scowl = load_scowl(); irr = load_irregular()
NOUN = {"N", "h"}; VERBP = {"V", "t", "i"}; ADJ = {"A"}; ADV = {"v"}
irr_bases = {v["base"] for v in irr["verbs"]}

def british(f):
    return [f, re.sub(r"our", "or", f), re.sub(r"re$", "er", f), re.sub(r"res$", "ers", f), re.sub(r"is(e|es|ing|ed)$", r"iz\1", f)]
def confirmed(f):
    return any(x in scowl for x in british(f))

# ---------------------------------------------------------------- the noun list
nouns = [w for w in heads if (moby.get(w, set()) & NOUN) and w.isalpha() and w not in ("i",)]
print("NGSL headwords Moby calls a noun (any other POS allowed):", len(nouns))
noun_only = [w for w in nouns if not (moby[w] & (VERBP | ADJ | ADV))]
print("noun-only:", len(noun_only))

# recorded plural candidates: an NGSL form of the headword that SCOWL confirms and that is not the headword
IRREG_PL = {"child": "children", "man": "men", "woman": "women", "foot": "feet", "tooth": "teeth", "mouse": "mice", "person": "people", "ox": "oxen", "goose": "geese", "louse": "lice", "die": "dice", "penny": "pence"}
LATIN = re.compile(r"(a|i|es|ices|ae)$")
def recorded_plurals(w):
    out = []
    for f in forms_of[w]:
        if f == w or not confirmed(f): continue
        if f.endswith("ing") or f.endswith("ed") or f.endswith("er") or f.endswith("est") or f.endswith("ly") or f.endswith("ness"): continue
        if f == w + "s" or f == w + "es" or (w.endswith("y") and f == w[:-1] + "ies") or (re.search(r"fe?$", w) and f == re.sub(r"fe?$", "ves", w)) \
           or f == IRREG_PL.get(w) or (w.endswith("is") and f == w[:-2] + "es") or (w.endswith("us") and f == w[:-2] + "i") \
           or (w.endswith("um") and f == w[:-2] + "a") or (w.endswith("on") and f == w[:-2] + "a") or (w.endswith("ex") and f == w[:-2] + "ices") or (w.endswith("ix") and f == w[:-2] + "ices") or (w.endswith("man") and f == w[:-3] + "men"):
            out.append(f)
    return out

def R0(w):  # add -s; -es after a hiss; consonant + y -> ies
    if re.search(r"(s|sh|ch|x|z)$", w): return w + "es"
    if re.search(r"[^aeiou]y$", w): return w[:-1] + "ies"
    return w + "s"
def R1(w):  # + consonant -o -> -oes
    if re.search(r"[^aeiou]o$", w): return w + "es"
    return R0(w)
def R2(w):  # + f/fe -> ves
    if re.search(r"(?:[^f]f|fe)$", w): return re.sub(r"fe?$", "ves", w)
    return R1(w)
def R3(w):  # R1 + ves ONLY for the short list the lesson can name (lf, ife, eaf, ief? no)
    if re.search(r"(lf|ife|eaf|arf|ief|olf)$", w) and w not in ("belief", "chief", "brief", "proof", "roof", "grief", "safe", "cafe", "cliff", "staff", "stuff", "cuff", "gulf", "golf", "self"):
        return re.sub(r"fe?$", "ves", w)
    return R1(w)

rows = []
noplural = []
for w in nouns:
    rec = recorded_plurals(w)
    if not rec:
        noplural.append(w); continue
    rows.append((w, rec))
print("nouns with a dictionary-confirmed plural recorded in the NGSL:", len(rows), "| with none:", len(noplural))
print("  no plural recorded (first 80):", sorted(noplural)[:80])
for label, rule in (("R0: -s, -es after a hiss, -y -> -ies", R0), ("R1: R0 + consonant-o -> -oes", R1), ("R2: R1 + f/fe -> ves", R2), ("R3: R1 + ves only for -lf/-ife/-eaf/-olf", R3)):
    hit = [w for w, rec in rows if rule(w) in rec]; miss = [(w, rule(w), "/".join(rec)) for w, rec in rows if rule(w) not in rec]
    show(label, len(hit), len(rows), ["%s -> %s (list: %s)" % m for m in miss], 60)
print("\n-o nouns and their recorded plurals:")
for w, rec in rows:
    if w.endswith("o"): print("   ", w, rec)
print("\n-f/-fe nouns and their recorded plurals:")
for w, rec in rows:
    if re.search(r"fe?$", w): print("   ", w, rec)
print("\nirregular plurals recorded:")
for w, rec in rows:
    if not any(r in (w + "s", w + "es", w[:-1] + "ies") for r in rec) and not re.search(r"fe?$", w) and not w.endswith("o"): print("   ", w, rec)
# zero plurals: check a few by hand against what the list records
for w in ("sheep", "fish", "deer", "series", "species", "means", "aircraft", "news", "people", "police", "data", "media", "criteria"):
    print("   zero/odd check", w, w in heads, forms_of.get(w), [f for f in forms_of.get(w, []) if confirmed(f)])

# ---------------------------------------------------------------- plural pronunciation
print("\n== Plural -s pronunciation (nouns, first recorded plural in CMUdict) ==")
def s_rule(last): return "IZ" if last in SIBILANT else ("S" if last in VOICELESS else "Z")
def s_actual(fp, last):
    tail = [strip_stress(x) for x in fp[-2:]]
    if tail[-1] == "Z" and tail[-2] in ("IH", "AH") and last not in ("IH", "AH"): return "IZ"
    return tail[-1] if tail[-1] in ("S", "Z") else "?" + tail[-1]
hit = total = 0; miss = []
for w, rec in rows:
    if w not in cmu: continue
    f = next((r for r in rec if r in cmu and r in (w + "s", w + "es", w[:-1] + "ies")), None)
    if not f: continue
    last = strip_stress(cmu[w][0][-1]); pred = s_rule(last); act = s_actual(cmu[f][0], last)
    total += 1
    if pred == act: hit += 1
    else: miss.append("%s->%s (%s, said %s)" % (w, f, pred, act))
show("plural -s: sibilant -> iz, voiceless -> s, else z", hit, total, miss, 40)
# what share of plurals is each sound
c = Counter()
for w, rec in rows:
    if w in cmu:
        c[s_rule(strip_stress(cmu[w][0][-1]))] += 1
print("   predicted sound over the noun list:", dict(c))

# ---------------------------------------------------------------- -ly adverbs
print("\n== Adjective + ly ==")
adjs = [w for w in heads if (moby.get(w, set()) & ADJ) and w.isalpha()]
adj_only = [w for w in adjs if not (moby[w] & (NOUN | VERBP))]
print("NGSL adjectives (Moby):", len(adjs), "adjective-only:", len(adj_only))
def ly(w):
    if w.endswith("ic") and w != "public": return w + "ally"
    if w.endswith("ll"): return w + "y"
    if w.endswith("le") and len(w) > 3 and w[-3] not in "aeiou": return w[:-1] + "y"
    if w.endswith("ue"): return w[:-1] + "ly"
    if w.endswith("y") and len(w) > 2 and w[-2] not in "aeiou": return w[:-1] + "ily"
    return w + "ly"
def ly_plain(w): return w + "ly"
for label, rule in (("plain: adjective + ly", ly_plain), ("with the spelling changes (-y -> -ily, -le -> -ly, -ic -> -ically, -ll -> -lly, -ue -> -uly)", ly)):
    hit = [w for w in adjs if confirmed(rule(w))]; miss = [w for w in adjs if not confirmed(rule(w))]
    show(label, len(hit), len(adjs), ["%s -> %s" % (w, rule(w)) for w in miss], 90)
print("   adjectives already ending in -ly:", sorted(w for w in adjs if w.endswith("ly"))[:40])
print("   -ic adjectives and whether -ically or -icly is the word:", [(w, confirmed(w + "ally"), confirmed(w + "ly")) for w in adjs if w.endswith("ic")][:40])
print("   recorded in the NGSL as an -ly form too:", sum(1 for w in adjs if ly(w) in forms), "of", len(adjs))
