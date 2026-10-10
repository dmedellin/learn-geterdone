"""Follow-up measurements that decide lesson shapes and data choices."""
import sys, re, json, gzip
from collections import Counter, defaultdict
sys.path.insert(0, str(__import__("pathlib").Path(__file__).resolve().parent))
from common_en import *

cmu = load_cmudict(); moby = load_moby(); forms, heads, forms_of = load_ngsl(); scowl = load_scowl()
verbs = load_verbs(); irr = load_irregular()
NOUN = {"N", "h"}; VERBP = {"V", "t", "i"}; ADJ = {"A"}; ADV = {"v"}
def confirmed(f): return f in scowl

# (a) noun-only nouns with no confirmed plural; irregular plural handling
print("== (a) noun-only headwords with no dictionary-confirmed plural ==")
noun_only = [w for w in heads if (moby.get(w, set()) & NOUN) and not (moby[w] & (VERBP | ADJ | ADV)) and w.isalpha()]
def plural_cands(w):
    return [f for f in forms_of[w] if f != w and confirmed(f) and (f == w + "s" or f == w + "es" or (w.endswith("y") and f == w[:-1] + "ies") or re.sub(r"fe?$", "ves", w) == f or f.endswith("men") or f in ("children", "feet", "teeth", "mice", "geese", "people", "oxen", "dice", "pence") or (w.endswith("is") and f == w[:-2] + "es") or (w.endswith("us") and f == w[:-2] + "i") or (w.endswith("um") and f == w[:-2] + "a") or (w.endswith("on") and f == w[:-2] + "a") or (w.endswith("ex") and f == w[:-2] + "ices") or (w.endswith("ix") and f == w[:-2] + "ices"))]
nopl = sorted(w for w in noun_only if not plural_cands(w))
print(len(noun_only), "noun-only;", len(nopl), "with no plural:", nopl)
# which nouns have a confirmed REGULAR plural only because the dictionary has a verb form (mans, foots)
for w in ("man", "foot", "mouse", "goose", "person", "child", "woman", "tooth", "sheep", "fish", "fireman", "policeman", "businessman", "spokesman"):
    print("  ", w, w in heads, forms_of.get(w, [])[:8], "confirmed:", [f for f in forms_of.get(w, []) if confirmed(f)])

# (b) -ly refined
print("\n== (b) adjective + ly, scored only where SOME -ly adverb exists ==")
def ly_rule(w):
    if w.endswith("ic") and w != "public": return w + "ally"
    if w.endswith("ll"): return w + "y"
    if w.endswith("le") and len(w) > 3 and w[-3] not in "aeiou": return w[:-1] + "y"
    if w.endswith("ue"): return w[:-1] + "ly"
    if w.endswith("y") and len(w) > 2 and w[-2] not in "aeiou": return w[:-1] + "ily"
    return w + "ly"
def any_ly(w):
    cands = {w + "ly", w + "ally", w + "ily", w[:-1] + "ily" if w.endswith("y") else "", w[:-1] + "y" if w.endswith("le") else "", w[:-1] + "ly" if w.endswith("e") else "", w + "y" if w.endswith("ll") else ""}
    return [c for c in cands if c and confirmed(c)]
for label, pool in (("Moby adjective (any)", [w for w in heads if (moby.get(w, set()) & ADJ) and w.isalpha()]), ("adjective-only", [w for w in heads if (moby.get(w, set()) & ADJ) and not (moby[w] & (NOUN | VERBP | ADV)) and w.isalpha()])):
    has = [w for w in pool if any_ly(w)]; none = [w for w in pool if not any_ly(w)]
    hit = [w for w in has if confirmed(ly_rule(w))]; miss = [(w, ly_rule(w), any_ly(w)) for w in has if not confirmed(ly_rule(w))]
    print("--", label, len(pool), "| an -ly adverb exists for", len(has), "| none for", len(none))
    show("the spelling rule gives the attested adverb", len(hit), len(has), ["%s -> %s (dict has %s)" % m for m in miss], 40)
    plain_hit = [w for w in has if confirmed(w + "ly")]
    show("plain +ly, same pool", len(plain_hit), len(has))
    print("   no -ly adverb at all (first 60):", none[:60])

# (c) magic e without -re
print("\n== (c) silent e, one-syllable CVCe words, r excluded ==")
LONG = {"a": {"EY"}, "e": {"IY"}, "i": {"AY"}, "o": {"OW"}, "u": {"UW"}}
hit = n = 0; res = []
for w in heads:
    m = re.fullmatch(r"[a-z]*[^aeiou]([aeiou])([^aeiouwxyr])e", w)
    if not m or w not in cmu or syllables(cmu[w][0]) != 1: continue
    v = m.group(1); phs = cmu[w][0]; vowel = [strip_stress(p) for p in phs if p[-1].isdigit()][0]
    n += 1
    if vowel in LONG[v]: hit += 1
    else: res.append("%s (%s)" % (w, vowel))
show("CVCe, last consonant not r", hit, n, res, 60)
rw = [w for w in heads if re.fullmatch(r"[a-z]*[^aeiou][aeiou]re", w) and w in cmu and syllables(cmu[w][0]) == 1]
print("   the -re words (%d):" % len(rw), sorted(rw))

# (d) schwa in unstressed syllables
print("\n== (d) unstressed syllables: how many are the flat vowel ==")
c = Counter(); n = 0
for w in heads:
    if w not in cmu: continue
    p = cmu[w][0]
    if syllables(p) < 2: continue
    for ph in p:
        if ph[-1] == "0":
            n += 1; c[strip_stress(ph)] += 1
print("unstressed vowels in NGSL words of 2+ syllables:", n, "| AH (schwa)", pct(c["AH"], n), "| IH", pct(c["IH"], n), "| ER", pct(c["ER"], n), "| IY", pct(c["IY"], n), "| OW", pct(c["OW"], n), "| rest", pct(n - c["AH"] - c["IH"] - c["ER"] - c["IY"] - c["OW"], n))
print("   full:", c.most_common())

# (e) the long passage: candidate chapters
print("\n== (e) a longer Austen passage for the helping-verb course ==")
novel = norm(pp_novel())
parts = re.split(r"\n\s*(CHAPTER [IVXLC]+\.?)\s*\n", novel)
chapters = [(parts[i].strip(), parts[i + 1]) for i in range(1, len(parts) - 1, 2)]
SUBJ = {"i", "you", "he", "she", "it", "we", "they"}
rows = []
for name, text in chapters:
    toks = [t.lower() for t in words(text)]; nw = len(toks)
    if 1800 <= nw <= 2400:
        subj = sum(1 for t in toks if t in SUBJ); ing = sum(1 for i, t in enumerate(toks[:-1]) if t in ("am", "is", "are", "was", "were", "been") and toks[i + 1].endswith("ing"))
        nots = toks.count("not"); modals = sum(1 for t in toks if t in ("can", "could", "may", "might", "must", "shall", "should", "will", "would")); haves = sum(1 for t in toks if t in ("have", "has", "had"))
        an = sum(1 for t in toks if t in ("a", "an"))
        rows.append((name, nw, subj, ing, nots, modals, haves, an, len(gzip.compress(text.encode(), 9))))
print("chapters 1,800-2,400 words: (name, words, pronoun subjects, be+ing, not, modals, have, a/an, gz)")
for r in sorted(rows, key=lambda r: -r[2]): print("  ", r)

# (f) the Wilde excerpt: a 1,500-word window of Act II with the most question marks
print("\n== (f) the Wilde excerpt ==")
play = norm(wilde_play())
a2 = play.index("SECOND ACT"); a3 = play.index("THIRD ACT")
act2 = play[a2:a3]
# cut at speech boundaries: speeches start with an uppercase NAME. at line start
speeches = re.split(r"\n\n(?=[A-Z][a-z]+(?: [A-Z][a-z]+)*\.  )", act2)
best = None
for s in range(len(speeches)):
    acc = []; nw = 0
    for t in speeches[s:]:
        acc.append(t); nw += len(words(t))
        if nw >= 1500: break
    txt = "\n\n".join(acc)
    q = txt.count("?"); nt = len(re.findall(r"n't\b", txt)) + len(re.findall(r"\b\w+'(s|ll|m|re|ve|d)\b", txt))
    if best is None or q + nt > best[0]: best = (q + nt, s, nw, q, nt, txt)
print("best window: speeches from", best[1], "words", best[2], "question marks", best[3], "contractions", best[4], "gz", len(gzip.compress(best[5].encode(), 9)))
print(best[5][:600].replace("\n", " | "))
print("...", best[5][-300:].replace("\n", " | "))
ex = best[5]
print("   n't", len(re.findall(r"n't\b", ex)), "not", len(re.findall(r"\bnot\b", ex)), "tags", len(re.findall(r",\s*(?:do|does|did|is|are|was|were|have|has|had|will|would|shall|should|can|could|must|may|might|don't|doesn't|didn't|isn't|aren't|wasn't|weren't|haven't|hasn't|won't|wouldn't|shan't|can't|couldn't)\s+(?:not\s+)?(?:I|you|he|she|it|we|they)(?:\s+not)?\s*\?", ex)))
print("   a/an in the excerpt:", sum(1 for t in words(ex) if t.lower() in ("a", "an")))

# (g) time prepositions: in/on/at only, strict rule
print("\n== (g) in / on / at before a time word, strict ==")
DAYS = {"monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"}
MONTHS = {"january", "february", "march", "april", "june", "july", "august", "september", "october", "november", "december"}
SEASONS = {"spring", "summer", "autumn", "winter"}
PARTS = {"morning", "afternoon", "evening"}
CLOCK = {"one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "half", "noon", "midnight", "night", "christmas", "easter", "michaelmas", "present"}
def rule(kind, cue):
    if kind in ("day",): return "on"
    if kind in ("month", "year", "season", "part of day"): return "in"
    return "at"
texts = [("Austen", novel), ("Wilde", play), ("modern", norm(modern_docs()))]
for label, text in texts:
    lw = [t.lower() for t in words(text)]; raw = words(text); n = Counter(); res = Counter(); lines = []
    for i in range(2, len(lw)):
        t = lw[i]; kind = None
        if t in DAYS: kind = "day"
        elif t in MONTHS: kind = "month"
        elif t in SEASONS: kind = "season"
        elif t in PARTS: kind = "part of day"
        elif t in ("night", "noon", "midnight", "christmas", "easter", "michaelmas"): kind = "point/festival"
        elif t == "o'clock" or (t in CLOCK - {"night", "noon", "midnight", "christmas", "easter", "michaelmas", "present"} and i + 1 < len(lw) and lw[i + 1] in ("o'clock",)): kind = "clock"
        elif re.fullmatch(r"1[5-9]\d\d|20\d\d", t): kind = "year"
        if not kind: continue
        prev = lw[i - 1]; prev2 = lw[i - 2]
        if prev in ("in", "on", "at"): prep = prev
        elif prev in ("the", "that", "this", "a", "one", "every", "each", "next", "last", "same", "following", "early", "late") and prev2 in ("in", "on", "at"): prep = prev2
        else: continue
        want = rule(kind, t)
        n[(kind, prep, prep == want)] += 1
        if prep != want: res["%s %s %s" % (prep, prev if prev != prep else "", t)] += 1
    tot = sum(n.values()); hit = sum(v for k, v in n.items() if k[2])
    print("--", label, "in/on/at + time word:", tot, "rule right:", hit, pct(hit, tot))
    print("   by kind:", sorted(((k[0], k[1], v) for k, v in n.items()), key=lambda x: (x[0], -x[2])))
    print("   residue:", res.most_common(15))
# "on the morning/evening"
print("   Austen 'on ... morning/evening':", re.findall(r"\bon (?:the |that |a )?(?:\w+ )?(?:morning|evening|afternoon)\b", novel)[:12])

# (h) the modern a/an artefacts
print("\n== (h) a/an artefacts in the modern documents ==")
md = norm(modern_docs())
for m in re.finditer(r"\b[Aa]n? (?:As|a|addresses)\b", md): print("   ...", md[max(0, m.start() - 40):m.end() + 20].replace("\n", " "))

# (j) comparatives: two rule variants
print("\n== (j) comparatives: rule variants ==")
def adj_stem(t):
    for suf in ("iest", "ier", "est", "er"):
        if t.endswith(suf) and len(t) > len(suf) + 2:
            stem = t[:-len(suf)]; cands = [stem, stem + "e"]
            if suf.startswith("i"): cands.append(stem + "y")
            if len(stem) > 2 and stem[-1] == stem[-2]: cands.append(stem[:-1])
            for c in cands:
                if c in heads and (moby.get(c, set()) & ADJ) and c in cmu and not (moby.get(c, set()) & (NOUN | VERBP)) or (c in ("happy", "pretty", "early", "easy", "busy", "lucky", "angry", "heavy", "lovely", "pleasant", "quiet", "simple", "narrow", "clever", "gentle", "common", "handsome", "polite", "stupid", "remote", "severe", "minute", "little", "great", "small", "young", "old", "fine", "high", "low", "long", "short", "strong", "poor", "rich", "large", "big", "deep", "wide", "late", "near", "dear", "sweet", "warm", "cold", "hot", "kind", "proud", "wise", "safe", "sure", "fair", "dark", "light", "bright", "soft", "hard", "fast", "slow", "quick", "cheap", "thick", "thin", "clean", "full", "few", "new", "cool", "fond", "grave", "idle", "humble", "noble", "able", "feeble", "simple", "subtle", "sincere", "obscure", "mature", "profound", "elegant", "agreeable", "amiable")) and c in cmu:
                    return c, suf
    return None, None
def pred_a(stem):
    s = syllables(cmu[stem][0])
    return "inflect" if s == 1 or (s == 2 and stem.endswith("y")) else "more"
def pred_b(stem):
    s = syllables(cmu[stem][0])
    return "inflect" if s == 1 or (s == 2 and (stem.endswith("y") or stem.endswith("ow") or stem.endswith("le") or stem.endswith("er"))) else "more"
for label, text in texts:
    lw = [t.lower() for t in words(text)]; n = {"a": Counter(), "b": Counter()}; res = {"a": Counter(), "b": Counter()}; tot = 0
    for i, t in enumerate(lw):
        stem, suf = adj_stem(t)
        used = None
        if stem and stem not in ("other", "over", "under", "ever", "never", "after", "rather", "former", "latter", "either", "neither", "whether", "together", "farther", "further", "upper", "inner", "outer", "utter", "mere", "best", "worst", "least", "most", "interest", "rest", "forest", "request", "guest", "chest", "test", "nest", "harvest", "manifest", "protest", "contest", "arrest", "invest", "suggest", "digest", "quest", "vest", "west", "east", "modest", "honest", "earnest"): used = "inflect"; adj = stem
        elif t in ("more", "most") and i + 1 < len(lw) and lw[i + 1] in heads and (moby.get(lw[i + 1], set()) & ADJ) and not (moby.get(lw[i + 1], set()) & (NOUN | VERBP)) and lw[i + 1] in cmu: used = "more"; adj = lw[i + 1]
        if not used: continue
        tot += 1
        for k, f in (("a", pred_a), ("b", pred_b)):
            p = f(adj); n[k][p == used] += 1
            if p != used: res[k][t if used == "inflect" else t + " " + adj] += 1
    print("--", label, tot, "tokens | rule A (1 syll, or 2 ending -y):", pct(n["a"][True], tot), "| rule B (+ -ow -le -er):", pct(n["b"][True], tot))
    print("   A residue:", res["a"].most_common(14)); print("   B residue:", res["b"].most_common(14))

# (k) phrasal verbs with adverbial particles only
print("\n== (k) phrasal verbs: particles up/out/off/down/away/back/over only ==")
PART = {"up", "out", "off", "down", "away", "back", "over"}
PREPW = {"at", "to", "for", "with", "upon", "of", "from", "into", "after", "about", "on", "in"}
OBJ = {"me", "him", "her", "us", "them", "it", "you"}
vb_forms = defaultdict(set)
for b, fs in verbs["cases"]["s"]: vb_forms[b] |= set(fs) | {b}
for b, fs in verbs["cases"]["ing"]: vb_forms[b] |= set(fs)
for b, fs in verbs["cases"]["ed"]: vb_forms[b] |= set(fs)
for v in irr["verbs"]:
    b = v["base"]; vb_forms[b] |= {b} | set(v["past"].split("/")) | set(v["pp"].split("/"))
    vb_forms[b].add(b + "s"); vb_forms[b].add((b[:-1] if b.endswith("e") else b) + "ing")
for b, extra in {"sit": {"sitting"}, "get": {"getting"}, "put": {"putting"}, "set": {"setting"}, "run": {"running"}, "shut": {"shutting"}, "give": {"giving"}, "take": {"taking"}, "make": {"making"}, "come": {"coming"}, "go": {"goes"}, "have": {"has", "having"}, "do": {"does"}}.items(): vb_forms[b] |= extra
form2base = {}
for b, fs in vb_forms.items():
    for f in fs: form2base.setdefault(f, b)
for label, text in texts:
    lw = [t.lower() for t in words(text)]; direct = Counter(); between = Counter(); after = Counter(); prep_after = Counter(); prep_between = Counter(); lines_between = []
    for i in range(len(lw) - 2):
        b = form2base.get(lw[i])
        if not b or b in ("be", "have", "do", "will", "can", "may", "must", "shall", "need", "dare"): continue
        if lw[i + 1] in PART: direct[b + " " + lw[i + 1]] += 1
        if lw[i + 1] in OBJ and lw[i + 2] in PART: between[b + " " + lw[i + 2]] += 1
        if lw[i + 1] in PART and lw[i + 2] in OBJ: after[b + " " + lw[i + 1]] += 1
        if lw[i + 1] in PREPW and lw[i + 2] in OBJ: prep_after[b + " " + lw[i + 1]] += 1
        if lw[i + 1] in OBJ and lw[i + 2] in PREPW and i + 3 < len(lw) and lw[i + 3] not in ("the", "a", "an", "his", "her", "their", "my", "your", "our", "its", "this", "that", "these", "those", "all", "every", "any", "some", "no", "such", "what", "which", "whom", "it", "him", "her", "them", "me", "us", "you"): prep_between[b + " " + lw[i + 2]] += 1
    print("--", label, "verb+particle", sum(direct.values()), "| pronoun between", sum(between.values()), "| pronoun after particle", sum(after.values()), "| verb+preposition+pronoun", sum(prep_after.values()))
    print("   between:", between.most_common(12)); print("   after:", after.most_common(12)); print("   top verb+particle:", direct.most_common(15))
    print("   verb+prep+pronoun:", prep_after.most_common(10))

# (n) agreement, 'was' with I allowed
print("\n== (n) agreement against the rule, corrected ==")
S_ONLY = ({f for _b, fs in verbs["cases"]["s"] for f in fs} - set(verbs["stress"])) | {"is", "has", "does"}
for label, text in texts:
    lw = [t.lower() for t in words(text)]; res = Counter(); n3 = Counter(); npl = Counter()
    for i, t in enumerate(lw[:-1]):
        if t not in SUBJ: continue
        nxt = lw[i + 1]
        if t in ("he", "she", "it"):
            if nxt in S_ONLY or nxt == "was": n3["-s / is / has / does / was"] += 1
            elif nxt in ("are", "were", "have", "do", "am"): n3["a plural or I form"] += 1; res[t + " " + nxt] += 1
        elif t == "i":
            if nxt in ("am", "was"): npl["am/was"] += 1
            elif nxt in S_ONLY: npl["-s after I"] += 1; res[t + " " + nxt] += 1
        else:
            if nxt in S_ONLY or nxt == "was": npl["-s/was after you/we/they"] += 1; res[t + " " + nxt] += 1
            elif nxt in ("are", "were", "have", "do"): npl["are/were/have/do"] += 1
    print("--", label, dict(n3), dict(npl)); print("   against:", res.most_common(14))

# (o) Austen's a/an residue lines
print("\n== (o) a/an residue in Austen ==")
for m in re.finditer(r"\b([Aa]n? (?:[Hh]our(?:'s)?|[Hh]onou?r(?:able)?|one|[Uu]ni\w+|[Ee]urop\w+|[Hh]umble|[Hh]undred|[Hh]istor\w+|[Hh]eir|[Hh]onest\w*))\b", novel):
    print("   ...", novel[max(0, m.start() - 30):m.end() + 15].replace("\n", " "))
