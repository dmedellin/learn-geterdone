"""Concordance measurements on Austen (novel text), Wilde (play) and the two modern documents."""
import sys, re, json
from collections import Counter, defaultdict
sys.path.insert(0, str(__import__("pathlib").Path(__file__).resolve().parent))
from common_en import *

cmu = load_cmudict(); moby = load_moby(); forms, heads, forms_of = load_ngsl()
verbs = load_verbs(); irr = load_irregular(); passage = load_passage()["passage"]
NOUN = {"N", "h"}; VERBP = {"V", "t", "i"}; ADJ = {"A"}; ADV = {"v"}
TEXTS = [("Austen", pp_novel()), ("Wilde", wilde_play()), ("modern", modern_docs()), ("passage", passage)]

# verb form sets, built the way the kit would: from the two printed lists
base = set(verbs["stress"]) | {v["base"] for v in irr["verbs"]}
third = {f for _b, fs in verbs["cases"]["s"] for f in fs} | {"is", "has", "does", "says", "goes"}
ing = {f for _b, fs in verbs["cases"]["ing"] for f in fs}
past = {f for _b, fs in verbs["cases"]["ed"] for f in fs}
pp = set(past)
for v in irr["verbs"]:
    for x in v["past"].split("/"): past.add(x)
    for x in v["pp"].split("/"): pp.add(x)
    b = v["base"]
    third.add(b + "es" if re.search(r"(s|sh|ch|x|z)$|[^aeiou]o$", b) else (b[:-1] + "ies" if re.search(r"[^aeiou]y$", b) else b + "s"))
    ing.add((b[:-1] if b.endswith("e") and not b.endswith("ee") else b) + "ing")
ing |= {"being", "having", "doing", "going", "seeing", "beginning", "sitting", "getting", "running", "forgetting", "putting", "cutting", "letting", "swimming", "winning", "shutting", "hitting", "setting", "spinning", "digging", "dying", "lying", "tying"}
third |= {"has", "is"}
for b in ("am", "are", "was", "were", "been"): pass
MODAL = {"can", "could", "may", "might", "must", "shall", "should", "will", "would"}
BE = {"am", "is", "are", "was", "were", "be", "been", "being"}
HAVE = {"have", "has", "had", "having"}
DO = {"do", "does", "did"}
AUX = MODAL | BE | HAVE | DO
SUBJ = {"i", "you", "he", "she", "it", "we", "they"}
OBJ = {"me", "him", "her", "us", "them", "it", "you"}
DET = {"a", "an", "the", "no", "my", "your", "his", "her", "its", "our", "their", "some", "any", "much", "many", "more", "most", "little", "few", "every", "each", "this", "that", "these", "those", "such", "what", "which", "all", "both", "another", "other", "one", "two", "three", "several", "nothing", "something", "anything", "everything", "great", "good", "very", "so", "too", "half", "enough"}
ADVS = {w for w, p in moby.items() if p <= ADV} | {"not", "never", "always", "often", "ever", "soon", "certainly", "really", "rather", "quite", "just", "only", "also", "still", "already", "yet", "even", "scarcely", "hardly", "probably", "perhaps", "then", "now", "once", "indeed", "generally", "almost", "frequently", "sometimes", "usually", "immediately", "very", "much"}
def adj_only(w): p = moby.get(w, set()); return bool(p & ADJ) and not (p & (NOUN | VERBP | ADV))
def noun_like(w): p = moby.get(w, set()); return bool(p & NOUN)

def tokens(text):
    return [t.lower() for t in words(text)]

# ---------------------------------------------------------------- modal + base
print("== Modal verb, then the base form ==")
for label, text in TEXTS:
    toks = tokens(text); n = Counter(); res = []
    for i, t in enumerate(toks[:-1]):
        if t not in MODAL: continue
        j = i + 1
        while j < len(toks) and (toks[j] == "not" or toks[j] in ADVS and toks[j] not in base) and j < i + 3: j += 1
        nxt = toks[j] if j < len(toks) else ""
        direct = toks[i + 1]
        if direct in base or direct in BE or direct in HAVE or direct in DO: n["base directly"] += 1
        elif direct == "not": n["not between"] += 1
        elif direct in SUBJ: n["pronoun (a question)"] += 1
        elif nxt in base or nxt in BE or nxt in HAVE or nxt in DO: n["adverb between, then base"] += 1
        elif direct in third or direct in past or direct in ing: n["a formed verb (-s/-ed/-ing)"] += 1; res.append("%s %s" % (t, direct))
        else: n["other"] += 1; res.append("%s %s" % (t, direct))
    tot = sum(n.values())
    print("--", label, tot, "modals")
    for k, v in n.most_common(): print("   %-32s %5d %s" % (k, v, pct(v, tot)))
    print("   other/formed examples:", Counter(res).most_common(14))

# ---------------------------------------------------------------- have + participle
print("\n== have: helping verb or main verb ==")
for label, text in TEXTS:
    toks = tokens(text); n = Counter(); res = []
    for i, t in enumerate(toks[:-1]):
        if t not in HAVE: continue
        j = i + 1
        while j < len(toks) and (toks[j] == "not" or (toks[j] in ADVS and toks[j] not in pp)) and j < i + 3: j += 1
        nxt = toks[j] if j < len(toks) else ""
        if nxt in pp or nxt == "been": n["participle (perfect)"] += 1
        elif nxt == "to": n["have to"] += 1
        elif nxt in DET or noun_like(nxt) and nxt not in pp: n["a noun phrase (main verb have)"] += 1
        elif nxt in SUBJ: n["pronoun (a question)"] += 1
        elif nxt in OBJ: n["object pronoun (main verb)"] += 1
        else: n["other"] += 1; res.append("%s %s" % (t, nxt))
    tot = sum(n.values()); print("--", label, tot, "forms of have")
    for k, v in n.most_common(): print("   %-32s %5d %s" % (k, v, pct(v, tot)))
    print("   other examples:", Counter(res).most_common(12))

# ---------------------------------------------------------------- be + what
print("\n== be: what follows it ==")
PREP = {"in", "at", "on", "of", "to", "for", "with", "by", "from", "about", "into", "under", "upon", "over", "near", "out", "up", "down", "off", "away", "here", "there"}
for label, text in TEXTS:
    toks = tokens(text); n = Counter(); res = []
    for i, t in enumerate(toks[:-1]):
        if t not in BE: continue
        j = i + 1
        while j < len(toks) and (toks[j] == "not" or (toks[j] in ADVS and toks[j] not in pp and toks[j] not in ing)) and j < i + 3: j += 1
        nxt = toks[j] if j < len(toks) else ""
        if nxt in ing: n["-ing form (progressive)"] += 1
        elif nxt in pp: n["participle (passive, or adjective)"] += 1
        elif adj_only(nxt): n["adjective"] += 1
        elif nxt in DET: n["a noun phrase"] += 1
        elif nxt in PREP: n["preposition or place word"] += 1
        elif nxt in SUBJ: n["pronoun (a question)"] += 1
        elif nxt == "to": n["to (be to / be about to)"] += 1
        elif noun_like(nxt): n["a noun or name"] += 1
        else: n["other"] += 1; res.append("%s %s" % (t, nxt))
    tot = sum(n.values()); print("--", label, tot, "forms of be")
    for k, v in n.most_common(): print("   %-36s %5d %s" % (k, v, pct(v, tot)))
    print("   other examples:", Counter(res).most_common(12))

# ---------------------------------------------------------------- not
print("\n== not: the word before it ==")
for label, text in TEXTS:
    raw = norm(text); n = Counter(); res = []
    for m in re.finditer(r"(?<![A-Za-z'])(\w+)?([ ,;:.\"!?-]+)?\bnot\b", raw):
        pass
    toks = words(text); lw = [t.lower() for t in toks]
    for i, t in enumerate(lw):
        if t != "not" and not t.endswith("n't"): continue
        prev = lw[i - 1] if i else ""
        if t.endswith("n't"): n["n't (contracted)"] += 1; continue
        if prev in AUX or prev in ("cannot",): n["after a helping verb"] += 1
        elif prev in SUBJ or prev in OBJ: n["after a pronoun (question/inversion)"] += 1
        elif prev in third or prev in past or prev in base: n["after a main verb (know not)"] += 1; res.append("%s not" % prev)
        elif prev in ("or", "and", "but", "if", "whether", "than", "as", "that", "though", "yet", "why", "certainly", "perhaps", "probably", "do", "does", "did"): n["after a joining word (or not, if not)"] += 1
        else: n["other"] += 1; res.append("%s not" % prev)
    tot = sum(n.values()); print("--", label, tot, "nots")
    for k, v in n.most_common(): print("   %-40s %5d %s" % (k, v, pct(v, tot)))
    print("   examples:", Counter(res).most_common(14))

# ---------------------------------------------------------------- agreement
print("\n== Agreement: the -s form belongs to he, she, it ==")
S_ONLY = (third - base - past) | {"is", "has", "does", "was"}
for label, text in TEXTS:
    lw = tokens(text); n = Counter(); res = []
    for i, t in enumerate(lw[:-1]):
        if t not in SUBJ: continue
        nxt = lw[i + 1]
        who = "he/she/it" if t in ("he", "she", "it") else ("I" if t == "i" else "you/we/they")
        if nxt in ("is", "has", "does", "was"): kind = "is/has/does/was"
        elif nxt in ("am",): kind = "am"
        elif nxt in ("are", "were", "have", "do"): kind = "are/were/have/do"
        elif nxt in S_ONLY: kind = "-s form"
        elif nxt in base and nxt not in past: kind = "base form"
        elif nxt in past: kind = "past form"
        elif nxt in MODAL: kind = "modal"
        else: kind = "other"
        n[(who, kind)] += 1
        if (who != "he/she/it" and kind in ("-s form", "is/has/does/was")) or (who == "he/she/it" and kind in ("am", "are/were/have/do")): res.append("%s %s" % (t, nxt))
    print("--", label)
    for who in ("he/she/it", "I", "you/we/they"):
        row = {k[1]: v for k, v in n.items() if k[0] == who}; tot = sum(row.values())
        print("   %-12s %5d:" % (who, tot), ", ".join("%s %d" % (k, v) for k, v in sorted(row.items(), key=lambda kv: -kv[1])))
    print("   against the rule:", Counter(res).most_common(12))

# ---------------------------------------------------------------- the twelve boxes
print("\n== The twelve boxes, on pronoun-subject verb phrases ==")
def classify_chain(lw, i):
    j = i + 1; chain = []
    while j < len(lw) and j < i + 6:
        t = lw[j]
        if t == "not" or (t in ADVS and t not in base and t not in pp and t not in ing): j += 1; continue
        if t in MODAL or t in HAVE or t in BE or t in DO: chain.append(t); j += 1; continue
        break
    main = lw[j] if j < len(lw) else ""
    c = chain
    m_pp = main in pp; m_ing = main in ing; m_s = main in S_ONLY; m_base = main in base; m_past = main in past and not m_pp or (main in past and main in pp)
    if not c:
        if main in S_ONLY or main in base and main not in past: return "present simple"
        if main in past: return "past simple"
        return "no verb found"
    if c[0] in MODAL:
        rest = c[1:]
        if rest == ["have"] and m_pp: return "modal/future perfect"
        if rest == ["be"] and m_ing: return "modal/future progressive"
        if rest == ["have", "been"] and m_ing: return "modal/future perfect progressive"
        if rest == ["be"] and m_pp: return "modal + passive"
        if not rest and (m_base or main in ("be", "have", "do")): return "future/modal simple (will, would, can...)"
        if not rest and main == "": return "modal, nothing after"
        return "modal, other"
    if c[0] in HAVE:
        rest = c[1:]
        if rest == ["been"] and m_ing: return ("present" if c[0] in ("have", "has") else "past") + " perfect progressive"
        if rest == ["been"] and m_pp: return "perfect passive"
        if not rest and m_pp: return ("present" if c[0] in ("have", "has") else "past") + " perfect"
        if not rest: return "have as main verb"
        return "have, other"
    if c[0] in BE:
        if len(c) == 1 and m_ing: return ("present" if c[0] in ("am", "is", "are") else "past") + " progressive"
        if len(c) == 1 and m_pp: return "be + participle (passive or adjective)"
        if len(c) == 1: return "be as main verb"
        return "be, other"
    if c[0] in DO:
        if len(c) == 1 and (m_base or main == "not"): return ("present" if c[0] != "did" else "past") + " simple with do"
        return "do, other"
    return "other"
for label, text in TEXTS:
    lw = tokens(text); n = Counter()
    for i, t in enumerate(lw[:-1]):
        if t in SUBJ: n[classify_chain(lw, i)] += 1
    tot = sum(n.values()); print("--", label, tot, "pronoun subjects")
    for k, v in n.most_common(): print("   %-44s %5d %s" % (k, v, pct(v, tot)))

# ---------------------------------------------------------------- prepositions of time
print("\n== in / on / at before a time word ==")
DAYS = {"monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"}
MONTHS = {"january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"}
SEASONS = {"spring", "summer", "autumn", "winter"}
PARTS = {"morning", "afternoon", "evening"}
POINTS = {"night", "noon", "midnight", "christmas", "easter", "michaelmas", "present", "once", "first", "last", "length", "moment"}
for label, text in TEXTS:
    lw = tokens(text); n = Counter(); res = Counter()
    for i, t in enumerate(lw):
        if i < 1: continue
        kind = None
        if t in DAYS: kind = "day"
        elif t in MONTHS and t != "may": kind = "month"
        elif t in SEASONS: kind = "season"
        elif t in PARTS: kind = "part of day"
        elif t in ("night", "noon", "midnight"): kind = "night/noon/midnight"
        elif t in ("christmas", "easter", "michaelmas"): kind = "festival"
        elif t == "o'clock": kind = "clock time"
        elif re.fullmatch(r"1[5-9]\d\d|20\d\d", t): kind = "year"
        if not kind: continue
        prev = lw[i - 1]; prev2 = lw[i - 2] if i > 1 else ""
        if prev in ("the", "that", "this", "next", "last", "same", "very", "whole", "following", "a", "one", "every", "each", "early", "late", "first", "second", "th", "of") and prev2 in ("in", "on", "at", "by", "for", "during", "till", "until", "since", "before", "after", "from"): prep = prev2 + " (the)"
        elif prev in ("in", "on", "at", "by", "for", "during", "till", "until", "since", "before", "after", "from", "to"): prep = prev
        else: prep = "(none)"
        n[(kind, prep.split()[0])] += 1
    print("--", label)
    for kind in ("day", "month", "year", "season", "part of day", "night/noon/midnight", "festival", "clock time"):
        row = {k[1]: v for k, v in n.items() if k[0] == kind}; tot = sum(row.values())
        if tot: print("   %-20s %4d:" % (kind, tot), ", ".join("%s %d" % (k, v) for k, v in sorted(row.items(), key=lambda kv: -kv[1])))
# raw contexts for 'in the morning' vs 'on ... morning', and years in modern docs
raw = norm(modern_docs())
print("   modern: in <year>", len(re.findall(r"\bin (?:1[89]|20)\d\d", raw)), " on <Month day>", len(re.findall(r"\bon (?:January|February|March|April|May|June|July|August|September|October|November|December) \d", raw)), " in <Month>", len(re.findall(r"\bin (?:January|February|March|April|May|June|July|August|September|October|November|December)\b", raw)))
rawA = norm(pp_novel())
for pat in (r"\b(in|on|at) the (morning|evening|afternoon)\b", r"\b(in|on|at) (Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday)\b", r"\bat night\b", r"\bin the night\b", r"\b(at|in|on) Christmas\b", r"\bat Michaelmas\b", r"\b(in|at) (a )?(week|fortnight|month)\b", r"\b(on|in) (the )?(next|following) (day|morning)\b", r"\bo'clock\b", r"\b(at|by) (one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|half)\b"):
    hits = re.findall(pat, rawA); print("   Austen %-55s %4d" % (pat, len(hits)), Counter(h if isinstance(h, str) else " ".join(h) for h in hits).most_common(6))

# ---------------------------------------------------------------- question tags
print("\n== Question tags ==")
TAG = re.compile(r",\s*(do|does|did|is|are|was|were|have|has|had|will|would|shall|should|can|could|must|may|might)\s+(not\s+)?(I|you|he|she|it|we|they)(\s+not)?\s*\?", re.I)
TAGN = re.compile(r",\s*(don't|doesn't|didn't|isn't|aren't|wasn't|weren't|haven't|hasn't|hadn't|won't|wouldn't|shan't|shouldn't|can't|couldn't|mustn't)\s+(I|you|he|she|it|we|they)\s*\?", re.I)
for label, text in TEXTS[:3]:
    raw = norm(text); a = TAG.findall(raw); b = TAGN.findall(raw)
    print("--", label, "tags:", len(a) + len(b), "| full-form", len(a), "contracted", len(b))
    ex = [m.group(0) for m in TAG.finditer(raw)][:12] + [m.group(0) for m in TAGN.finditer(raw)][:12]
    print("   ", ex)
    qs = raw.count("?"); print("   question marks:", qs, "per 1,000 words:", "%.1f" % (1000.0 * qs / len(words(raw))))

# ---------------------------------------------------------------- contractions
print("\n== Contractions ==")
for label, text in TEXTS[:3]:
    raw = norm(text); n = len(words(raw))
    c = Counter()
    for m in re.finditer(r"\b[A-Za-z]+('s|'t|'ll|'d|'m|'re|'ve)\b", raw): c[m.group(1)] += 1
    nt = len(re.findall(r"n't\b", raw)); nots = len(re.findall(r"\bnot\b", raw))
    print("--", label, "words", n, dict(c), "per 1,000:", "%.1f" % (1000.0 * sum(c.values()) / n), "| n't", nt, "not", nots, "share contracted", pct(nt, nt + nots))
    print("   commonest:", Counter(m.group(0).lower() for m in re.finditer(r"\b[A-Za-z]+'(s|t|ll|d|m|re|ve)\b", raw)).most_common(15))

# ---------------------------------------------------------------- phrasal verbs
print("\n== Phrasal verbs and where the pronoun goes ==")
PHR = ["give up", "take off", "put on", "turn out", "find out", "go on", "come back", "come in", "sit down", "get up", "look up", "make up", "pick up", "set off", "bring up", "carry on", "go out", "come out", "give in", "take up", "put off", "look out", "turn up", "go away", "send away", "come on", "get on", "keep up", "put up", "take away", "go back", "come down", "break off", "call out", "run away", "sit up", "stand up", "get out", "come up", "look on", "wait on", "call on", "think over", "give away", "make out", "point out", "carry out", "set out", "put down", "take in", "turn away", "get over", "look back", "go off", "shut up", "hold out", "write down", "fall in"]
PART = {"up", "down", "out", "off", "on", "in", "away", "back", "over", "about", "along", "round", "through"}
PREPW = {"at", "to", "for", "with", "upon", "of", "from", "into", "after", "by", "about"}
def vforms(b):
    out = {b}
    for v in irr["verbs"]:
        if v["base"] == b: out |= set(v["past"].split("/")) | set(v["pp"].split("/"))
    for slot in ("s", "ing", "ed"):
        for bb, fs in verbs["cases"][slot]:
            if bb == b: out |= set(fs)
    if b in {"be"}: out |= BE
    out.add(b + "s"); out.add((b[:-1] if b.endswith("e") else b) + "ing")
    EXTRA = {"go": {"goes", "went", "gone", "going"}, "come": {"came", "coming", "comes"}, "sit": {"sat", "sitting", "sits"}, "get": {"got", "getting", "gets", "gotten"}, "put": {"puts", "putting"}, "set": {"sets", "setting"}, "run": {"ran", "running", "runs"}, "take": {"took", "taken", "taking"}, "give": {"gave", "given", "giving"}, "make": {"made", "making"}, "find": {"found", "finding"}, "bring": {"brought", "bringing"}, "stand": {"stood", "standing"}, "hold": {"held", "holding"}, "think": {"thought", "thinking"}, "break": {"broke", "broken", "breaking"}, "fall": {"fell", "fallen", "falling"}, "send": {"sent", "sending"}, "keep": {"kept", "keeping"}, "shut": {"shutting"}, "write": {"wrote", "written", "writing"}, "look": {"looked", "looking", "looks"}, "turn": {"turned", "turning", "turns"}, "call": {"called", "calling", "calls"}, "carry": {"carried", "carrying", "carries"}, "point": {"pointed", "pointing", "points"}, "pick": {"picked", "picking", "picks"}, "wait": {"waited", "waiting", "waits"}}
    out |= EXTRA.get(b, set())
    return out
for label, text in TEXTS[:3]:
    lw = tokens(text); cnt = Counter(); between = Counter(); after = Counter(); prepafter = Counter(); prepbetween = Counter()
    for pv in PHR:
        vb, part = pv.split(); fs = vforms(vb)
        for i, t in enumerate(lw[:-2]):
            if t not in fs: continue
            if lw[i + 1] == part: cnt[pv] += 1
            elif lw[i + 1] in OBJ and lw[i + 2] == part: cnt[pv] += 1; between[pv] += 1
            if lw[i + 1] == part and lw[i + 2] in OBJ: after[pv] += 1
    # prepositions: verb + prep + pronoun vs verb + pronoun + prep, for a few verbs
    for vb in ("look", "wait", "call", "laugh", "listen", "depend", "think", "speak", "talk", "agree", "belong", "come", "go", "attend", "apply"):
        fs = vforms(vb)
        for i, t in enumerate(lw[:-2]):
            if t not in fs: continue
            if lw[i + 1] in PREPW and lw[i + 2] in OBJ: prepafter[vb + " " + lw[i + 1]] += 1
            if lw[i + 1] in OBJ and lw[i + 2] in PREPW: prepbetween[vb + " " + lw[i + 2]] += 1
    tot = sum(cnt.values()); print("--", label, "phrasal-verb tokens:", tot, "per 1,000:", "%.1f" % (1000.0 * tot / len(lw)))
    print("   top:", cnt.most_common(15))
    print("   pronoun BETWEEN verb and particle:", sum(between.values()), between.most_common(8))
    print("   pronoun AFTER the particle:", sum(after.values()), after.most_common(8))
    print("   preposition THEN pronoun (look at him):", sum(prepafter.values()), prepafter.most_common(8))
    print("   pronoun THEN preposition (look him at):", sum(prepbetween.values()), prepbetween.most_common(6))

# ---------------------------------------------------------------- the + superlative
print("\n== the before a superlative or ordinal ==")
POSS = {"my", "your", "his", "her", "its", "our", "their", "whose"}
for label, text in TEXTS[:3]:
    lw = tokens(text); n = Counter(); res = Counter()
    for i, t in enumerate(lw):
        if i == 0: continue
        sup = None
        if t.endswith("est") and len(t) > 4:
            stem = t[:-3]
            for cand in (stem, stem + "e", stem[:-1] + "y" if stem.endswith("i") else None, stem[:-1] if len(stem) > 2 and stem[-1] == stem[-2] else None):
                if cand and cand in heads and moby.get(cand, set()) & ADJ: sup = "-est"; break
        elif t == "most" and i + 1 < len(lw) and (moby.get(lw[i + 1], set()) & ADJ): sup = "most + adj"
        elif t in ("first", "last", "next", "same", "only", "second", "third"): sup = t
        if not sup: continue
        prev = lw[i - 1]; prev2 = lw[i - 2] if i > 1 else ""
        if prev == "the": w = "the"
        elif prev in POSS or prev.endswith("'s"): w = "possessive"
        elif prev in ("a", "an"): w = "a/an"
        elif prev in ("very", "at"): w = prev
        else: w = "other"
        n[(sup, w)] += 1
        if w == "other": res[prev + " " + t] += 1
    print("--", label)
    for sup in ("-est", "most + adj", "first", "last", "next", "same", "only", "second"):
        row = {k[1]: v for k, v in n.items() if k[0] == sup}; tot = sum(row.values())
        if tot: print("   %-12s %4d:" % (sup, tot), ", ".join("%s %d" % (k, v) for k, v in sorted(row.items(), key=lambda kv: -kv[1])))
    print("   other:", res.most_common(12))

# ---------------------------------------------------------------- countable / uncountable
print("\n== Uncountable nouns: a/an before them, and plural forms ==")
UNC = ["advice", "information", "news", "furniture", "money", "luggage", "weather", "knowledge", "happiness", "music", "bread", "work", "time", "love", "progress", "research", "traffic", "homework", "equipment", "evidence", "health", "help", "patience", "pleasure", "poetry", "rain", "sense", "silence", "society", "truth", "water", "wealth", "beauty", "business", "company", "conversation", "attention", "courage", "fun", "luck", "paper", "milk", "coffee", "tea", "sugar", "wine", "food", "fruit", "hair", "light", "noise", "room", "space", "experience", "behaviour", "behavior", "trouble", "pride", "anger", "fear", "hope", "pain", "power", "safety", "wisdom", "youth", "age", "comfort", "danger"]
for label, text in TEXTS[:3]:
    lw = tokens(text); rows = []
    for u in UNC:
        a = sum(1 for i in range(1, len(lw)) if lw[i] == u and lw[i - 1] in ("a", "an"))
        pl = sum(1 for t in lw if t == u + "s" or (u.endswith("y") and t == u[:-1] + "ies"))
        tot = sum(1 for t in lw if t == u)
        much = sum(1 for i in range(1, len(lw)) if lw[i] == u and lw[i - 1] in ("much", "little"))
        many = sum(1 for i in range(1, len(lw)) if lw[i] in (u + "s",) and lw[i - 1] in ("many", "few"))
        if tot: rows.append((u, tot, a, pl, much, many))
    print("--", label, "(noun, count, a/an+noun, plural forms, much/little+noun, many/few+plural)")
    print("   ", [r for r in rows if r[2] or r[3]][:40])
    print("    clean (no a/an, no plural):", [r[0] for r in rows if not r[2] and not r[3]])

# ---------------------------------------------------------------- adjective position
print("\n== Where the adjective goes ==")
LINK = BE | {"seem", "seems", "seemed", "look", "looks", "looked", "feel", "feels", "felt", "become", "became", "appear", "appeared", "appears", "grow", "grew", "sound", "remain", "remained", "so", "very", "too", "more", "most", "as", "quite", "rather", "how", "less", "exceedingly", "extremely", "perfectly", "really", "particularly", "equally", "much"}
for label, text in TEXTS[:3]:
    toks = words(text); lw = [t.lower() for t in toks]; raw = norm(text)
    n = Counter(); res = Counter()
    for i, t in enumerate(lw[:-1]):
        if not adj_only(t) or t not in heads: continue
        nxt = lw[i + 1]; prev = lw[i - 1] if i else ""
        if noun_like(nxt) and not (moby.get(nxt, set()) & VERBP and not (moby.get(nxt, set()) & NOUN)) and nxt not in AUX and nxt not in DET: n["before a noun"] += 1
        elif adj_only(nxt) or nxt == "and": n["before another adjective / and"] += 1
        elif prev in LINK: n["after be / a linking word / very"] += 1
        elif nxt in ("to", "of", "for", "with", "in", "at", "that", "as", "than", "by", "about", "from"): n["before a preposition or that"] += 1
        elif prev in ("something", "anything", "nothing", "everything", "somebody", "anybody", "nobody", "everybody", "someone", "anyone"): n["after something / nothing"] += 1
        elif noun_like(prev) and prev not in DET and prev not in AUX: n["directly after a noun"] += 1; res[prev + " " + t] += 1
        else: n["other"] += 1; res[prev + " " + t + " " + nxt] += 1
    tot = sum(n.values()); print("--", label, tot, "adjective tokens (Moby adjective-only, in the NGSL)")
    for k, v in n.most_common(): print("   %-40s %5d %s" % (k, v, pct(v, tot)))
    print("   examples:", res.most_common(16))

# ---------------------------------------------------------------- comparatives by syllable
print("\n== Comparatives and superlatives: -er/-est against more/most ==")
def adj_stem(t):
    for suf in ("iest", "ier", "est", "er"):
        if t.endswith(suf) and len(t) > len(suf) + 2:
            stem = t[:-len(suf)]
            cands = [stem, stem + "e"]
            if suf.startswith("i"): cands.append(stem + "y")
            if len(stem) > 2 and stem[-1] == stem[-2]: cands.append(stem[:-1])
            for c in cands:
                if c in heads and (moby.get(c, set()) & ADJ) and c in cmu: return c, ("-er" if suf.endswith("er") else "-est")
    return None, None
def predict(stem):
    s = syllables(cmu[stem][0])
    if s == 1: return "inflect"
    if s == 2 and (stem.endswith("y") or stem.endswith("ow") or stem.endswith("le") or stem.endswith("er")): return "inflect"
    return "more"
for label, text in TEXTS[:3]:
    lw = tokens(text); n = Counter(); res = Counter(); bysyl = Counter()
    for i, t in enumerate(lw):
        stem, kind = adj_stem(t)
        if stem and stem not in ("other", "over", "under", "ever", "never", "after", "rather", "former", "latter", "either", "neither", "whether", "together", "farther", "further", "upper", "inner", "outer", "utter", "proper", "clever", "eager", "tender", "bitter", "sober", "sheer", "mere", "sinister", "modest", "honest", "earnest", "west", "east", "best", "worst", "least", "most", "interest", "rest", "forest", "request", "guest", "chest", "test", "nest", "harvest", "manifest", "protest", "contest", "arrest", "invest", "suggest", "digest", "quest", "vest", "fever", "river", "paper", "letter", "matter", "water", "dinner", "manner", "sister", "brother", "mother", "father", "daughter", "master", "character", "chapter", "number", "member", "order", "power", "answer", "offer", "suffer", "wonder", "consider", "remember", "deliver", "discover", "prefer", "refer", "enter", "gather", "differ", "border", "corner", "quarter", "shoulder", "summer", "winter", "silver", "butter", "copper", "ladder", "leather", "weather", "feather", "finger", "linger", "anger", "danger", "stranger", "hunger", "soldier", "lawyer", "officer", "partner", "owner", "lover", "cover", "hover"):
            pr = predict(stem); used = "inflect"; n[(pr, used)] += 1; bysyl[(syllables(cmu[stem][0]), used)] += 1
            if pr != used: res[t] += 1
        elif t in ("more", "most") and i + 1 < len(lw):
            nxt = lw[i + 1]
            if nxt in heads and adj_only(nxt) and nxt in cmu and nxt not in ("than",):
                pr = predict(nxt); used = "more"; n[(pr, used)] += 1; bysyl[(syllables(cmu[nxt][0]), used)] += 1
                if pr != used: res[t + " " + nxt] += 1
    tot = sum(n.values()); hit = n[("inflect", "inflect")] + n[("more", "more")]
    print("--", label, "tokens:", tot, "rule right:", hit, pct(hit, tot), dict(n))
    print("   by syllables of the adjective:", sorted(bysyl.items()))
    print("   against the rule:", res.most_common(20))

# ---------------------------------------------------------------- coverage, zipf, family vs flemma
print("\n== Coverage by NGSL band; the commonest words; family against flemma ==")
AFFIX_SUF = ["ly", "ness", "ment", "tion", "sion", "er", "or", "ful", "less", "able", "ible", "ity", "ous", "ive", "al", "ish", "ist", "ism", "ance", "ence", "ure", "age", "ess"]
AFFIX_PRE = ["un", "re", "dis", "in", "im", "mis", "non", "over", "under", "pre"]
def family_hit(t):
    for p in AFFIX_PRE:
        if t.startswith(p) and t[len(p):] in forms: return True
    for s in AFFIX_SUF:
        if t.endswith(s):
            stem = t[:-len(s)]
            for c in (stem, stem + "e", stem[:-1] + "y" if stem.endswith("i") else None, stem[:-1] if len(stem) > 2 and stem[-1] == stem[-2] else None):
                if c and c in forms: return True
    return False
for label, text in TEXTS:
    toks = words(text); lw = [t.lower().replace("'s", "") for t in toks]
    n = len(lw); b1 = sum(1 for t in lw if forms.get(t) == 1); b2 = sum(1 for t in lw if forms.get(t, 9) <= 2); b3 = sum(1 for t in lw if t in forms)
    # proper nouns: capitalised, not sentence-initial (approximation: previous raw token not ending a sentence)
    sent_init = set(); raw = norm(text)
    for m in re.finditer(r"(?:^|[.!?]\s+|\n\n)([A-Z][a-z']*)", raw): sent_init.add(m.start(1))
    caps = sum(1 for t in toks if t[0].isupper() and t.lower() not in forms)
    off = Counter(t for t in lw if t not in forms and not t[0].isupper())
    fam = sum(1 for t in lw if t not in forms and family_hit(t))
    c = Counter(lw); top = c.most_common(100)
    def cum(k): return sum(v for _, v in top[:k])
    print("--", label, "tokens", n)
    print("   band 1 %s | bands 1-2 %s | bands 1-3 %s | +capitalised %s | +family affixes %s" % (pct(b1, n), pct(b2, n), pct(b3, n), pct(b3 + caps, n), pct(b3 + caps + fam, n)))
    print("   top 10 words cover %s, top 50 %s, top 100 %s; distinct words %d" % (pct(cum(10), n), pct(cum(50), n), pct(cum(100), n), len(c)))
    print("   top 10:", [w for w, _ in top[:10]])
    print("   commonest off-list:", off.most_common(25))

# ---------------------------------------------------------------- Wilde: questions by the rule
print("\n== Questions in the play, scored by the course-3 rule ==")
AUXQ = {"is", "are", "was", "were", "be", "am", "have", "has", "had", "do", "does", "did", "will", "would", "shall", "should", "can", "could", "may", "might", "must", "cannot"}
WH = {"what", "where", "when", "why", "who", "whom", "whose", "how", "which"}
raw = norm(wilde_play())
qs = [q.strip() for q in re.findall(r"(?:(?<=[.!?\]])|^)\s*([^.!?\n\[\]]*\?)", raw)]
qs = [q for q in qs if len(q.split()) >= 2]
n = Counter()
for q in qs:
    lw = [t.lower() for t in words(q)]
    if not lw: continue
    if lw[0] in AUXQ or lw[0].endswith("n't"): n["auxiliary first"] += 1
    elif lw[0] in WH and len(lw) > 1 and (lw[1] in AUXQ or lw[1].endswith("n't")): n["wh-word then auxiliary"] += 1
    elif lw[0] in WH: n["wh-word, no auxiliary after"] += 1
    elif lw[0] in ("and", "but", "or", "so", "then"): n["joining word first"] += 1
    elif lw[0] in SUBJ: n["pronoun first (statement with ?)"] += 1
    else: n["something else"] += 1
tot = sum(n.values()); print("Wilde questions:", tot)
for k, v in n.most_common(): print("   %-36s %5d %s" % (k, v, pct(v, tot)))
print("   examples of 'something else':", [q for q in qs if words(q) and words(q)[0].lower() not in AUXQ | WH | {"and", "but", "or", "so", "then"} | SUBJ][:10])
