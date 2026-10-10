"""Last measurements: the Wilde excerpt, Chapter XXVI facts, data sizes, the SCOTUS '(a)' artefact."""
import sys, re, json, gzip
from collections import Counter
sys.path.insert(0, str(__import__("pathlib").Path(__file__).resolve().parent))
from common_en import *

play = norm(wilde_play()); novel = norm(pp_novel()); md = norm(modern_docs())
cmu = load_cmudict(); moby = load_moby(); forms, heads, forms_of = load_ngsl(); verbs = load_verbs(); irr = load_irregular()

# ---- Wilde excerpt: split on speaker lines (ALL CAPS name, own line, ending '.')
print("== Wilde excerpt ==")
a2 = play.index("SECOND ACT"); a3 = play.index("THIRD ACT")
act2 = play[a2:a3]
pieces = re.split(r"\n(?=(?:[A-Z][A-Z]+\.?\s?){1,3}\.\n)", act2)
print("speeches in Act II:", len(pieces))
TAG = re.compile(r",\s*(?:do|does|did|is|are|was|were|have|has|had|will|would|shall|should|can|could|must|may|might|don't|doesn't|didn't|isn't|aren't|wasn't|weren't|haven't|hasn't|won't|wouldn't|shan't|can't|couldn't)\s+(?:not\s+)?(?:I|you|he|she|it|we|they)(?:\s+not)?\s*\?", re.I)
best = None
for s in range(len(pieces)):
    acc = []; nw = 0
    for t in pieces[s:]:
        acc.append(t); nw += len(words(t))
        if nw >= 1900: break
    if nw < 1900: break
    txt = "\n".join(acc)
    q = txt.count("?"); nt = len(re.findall(r"n't\b", txt)); nots = len(re.findall(r"\bnot\b", txt)); con = len(re.findall(r"\b\w+'(?:s|ll|m|re|ve|d|t)\b", txt)); tags = len(TAG.findall(txt))
    score = q + con + 4 * tags
    if best is None or score > best[0]: best = (score, s, nw, q, nt, nots, con, tags, txt)
_, s, nw, q, nt, nots, con, tags, txt = best
print("chosen: speeches %d.., words %d, question marks %d, n't %d, not %d, contractions %d, tags %d, gz %d" % (s, nw, q, nt, nots, con, tags, len(gzip.compress(txt.encode(), 9))))
print("STARTS:", txt[:300].replace("\n", " | "))
print("ENDS:", txt[-200:].replace("\n", " | "))
print("tags:", TAG.findall(txt))
print("contraction types:", Counter(m.group(1) for m in re.finditer(r"\b\w+('(?:s|ll|m|re|ve|d|t))\b", txt)))
print("a/an:", sum(1 for t in words(txt) if t.lower() in ("a", "an")))
# questions in the excerpt by the rule
AUXQ = {"is", "are", "was", "were", "be", "am", "have", "has", "had", "do", "does", "did", "will", "would", "shall", "should", "can", "could", "may", "might", "must", "cannot"}
WH = {"what", "where", "when", "why", "who", "whom", "whose", "how", "which"}
qs = [x.strip() for x in re.findall(r"(?:(?<=[.!?\]])|^)\s*([^.!?\n\[\]]*\?)", txt) if len(x.split()) >= 1]
n = Counter()
for qq in qs:
    lw = [t.lower() for t in words(qq)]
    if not lw: n["no words"] += 1; continue
    if lw[0] in AUXQ or lw[0].endswith("n't"): n["aux first"] += 1
    elif lw[0] in WH and len(lw) > 1 and (lw[1] in AUXQ or lw[1].endswith("n't")): n["wh then aux"] += 1
    elif lw[0] in WH: n["wh, no aux after"] += 1
    elif lw[0] in ("and", "but", "or", "so", "then"): n["joining word"] += 1
    elif lw[0] in ("i", "you", "he", "she", "it", "we", "they"): n["pronoun first"] += 1
    else: n["something else"] += 1
print("questions in excerpt:", len(qs), dict(n))

# ---- Chapter XXVI facts
print("\n== Chapter XXVI ==")
parts = re.split(r"\n\s*(CHAPTER [IVXLC]+\.?)\s*\n", novel)
ch = dict((parts[i].strip().rstrip("."), parts[i + 1]) for i in range(1, len(parts) - 1, 2))
c26 = ch["CHAPTER XXVI"].strip()
print("words", len(words(c26)), "gz", len(gzip.compress(c26.encode(), 9)))
print("STARTS:", c26[:160].replace("\n", " ")); print("ENDS:", c26[-160:].replace("\n", " "))
lw = [t.lower() for t in words(c26)]
MODAL = {"can", "could", "may", "might", "must", "shall", "should", "will", "would"}; BE = {"am", "is", "are", "was", "were", "be", "been", "being"}; HAVE = {"have", "has", "had", "having"}; DO = {"do", "does", "did"}
print("modals", sum(t in MODAL for t in lw), "have", sum(t in HAVE for t in lw), "be", sum(t in BE for t in lw), "do", sum(t in DO for t in lw), "not", lw.count("not"), "n't", sum(t.endswith("n't") for t in lw))
SUBJ = {"i", "you", "he", "she", "it", "we", "they"}
print("pronoun subjects", sum(t in SUBJ for t in lw), "| he/she/it", sum(t in ("he", "she", "it") for t in lw), "| you/we/they", sum(t in ("you", "we", "they") for t in lw), "| I", lw.count("i"))
ing_after_be = sum(1 for i, t in enumerate(lw[:-1]) if t in BE and lw[i + 1].endswith("ing")); print("be + -ing (direct)", ing_after_be)
# words of the chapter not in the NGSL (lexicon for the verb lists)
pw = set(lw); print("distinct words", len(pw), "not in NGSL forms", len([w for w in pw if w not in forms]))
missing_cmu = sorted(w for w in pw if w.strip("'") not in cmu); print("not in CMUdict (%d):" % len(missing_cmu), missing_cmu[:40])

# ---- the SCOTUS '(a)' artefact
print("\n== modern docs: single letters in brackets ==")
print(re.findall(r"\(\w\)", md)[:20], "| 'a.' markers:", len(re.findall(r"\b[a-z]\.\s", md)))
for m in re.finditer(r"\ba (?:As|a|addresses)\b", md): print("   ...", md[max(0, m.start() - 50):m.end() + 10].replace("\n", " "))

# ---- data size estimates
print("\n== data size estimates (gz bytes) ==")
def gz(s): return len(gzip.compress(s.encode(), 9))
# a/an concordance from Wilde: every a/an with 5 words either side
toks = words(play); lines = []
for i, t in enumerate(toks):
    if t.lower() in ("a", "an"): lines.append(" ".join(toks[max(0, i - 5):i + 6]))
print("Wilde a/an lines", len(lines), gz(json.dumps(lines)))
# comparatives concordance (Austen + Wilde): -er/-est/more/most tokens with 6-word window
cmp_lines = []
for text in (novel, play):
    tk = words(text)
    for i, t in enumerate(tk):
        tl = t.lower()
        if (tl.endswith("er") or tl.endswith("est")) and len(tl) > 4 or tl in ("more", "most"):
            cmp_lines.append(" ".join(tk[max(0, i - 5):i + 6]))
print("comparative candidate lines (unfiltered)", len(cmp_lines), gz(json.dumps(cmp_lines)))
# Wilde questions
qs_all = [x.strip() for x in re.findall(r"(?:(?<=[.!?\]])|^)\s*([^.!?\n\[\]]*\?)", play) if len(x.split()) >= 2]
print("Wilde questions", len(qs_all), gz(json.dumps(qs_all)))
# superlative/same/next concordance in Austen
sup = []
tk = words(novel)
for i, t in enumerate(tk):
    tl = t.lower()
    if (tl.endswith("est") and len(tl) > 4) or tl in ("same", "next", "most"):
        sup.append(" ".join(tk[max(0, i - 5):i + 6]))
print("Austen superlative/same/next/most lines", len(sup), gz(json.dumps(sup)))
# phrasal concordance: verb + particle within Austen (approx: any token followed by a particle)
PART = {"up", "out", "off", "down", "away", "back", "over"}
ph = [" ".join(tk[max(0, i - 5):i + 7]) for i, t in enumerate(tk[:-2]) if tk[i + 1].lower() in PART or (tk[i + 1].lower() in ("it", "him", "them", "me", "us") and tk[i + 2].lower() in PART)]
print("Austen particle lines (unfiltered)", len(ph), gz(json.dumps(ph)))
# CMUdict-derived verb sounds table
rows = []
for base in verbs["stress"]:
    if base in cmu: rows.append("%s %s" % (base, strip_stress(cmu[base][0][-1])))
print("verb final-sound rows", len(rows), gz("|".join(rows)))
# stress table: NGSL words, syllables + stress index + pos class
st = []
for w in heads:
    if w in cmu:
        p = cmu[w][0]; st.append("%s %d %s" % (w, syllables(p), stress_index(p)))
print("stress rows", len(st), gz("|".join(st)))
# headword+band list for coverage
hb = "|".join(" ".join(sorted(k for k, v in heads.items() if v == b)) for b in (1, 2, 3))
print("headword+band", gz(hb), "| forms list", gz("|".join(" ".join(sorted(k for k, v in forms.items() if v == b)) for b in (1, 2, 3))))
# CMUdict first sounds for Wilde a/an next words
nxt = set(toks[i + 1].lower().strip("'") for i, t in enumerate(toks[:-1]) if t.lower() in ("a", "an"))
fs = "|".join("%s %s" % (w, strip_stress(cmu[w][0][0])) for w in sorted(nxt) if w in cmu)
print("first-sound rows for a/an next words", len(nxt), gz(fs))
