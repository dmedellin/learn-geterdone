#!/usr/bin/env python3
"""Cut the printed texts and the lines the English labs score.

    python3 scripts/wordlists/concordance.py          # rewrite every output
    python3 scripts/wordlists/concordance.py --check  # exit 1 if any would change

Run it by hand; the build never runs it. Sources: docs/english-v2/measure/data/
(fetch.sh) or --sources DIR. Every output's `note` names the text, the edition,
the slice and the licence; `sources` gives the sha256 of each file as fetched.

OUTPUTS (content/english/data/)
  long_passage.json           Chapter XXVI of the novel, printed whole, with the
                              word classes the helping-verb lab reads, built
                              for the chapter's words and the modern documents'.
  wilde_questions.json        every question in the play of two words or more.
  question_concordance.json   the 90 questions from the novel, RE-CUT (below).
  an_concordance.json         every a and an in the play, the modern documents
                              and the 936-word passage, with the next word.
  superlative_concordance.json  every -est adjective, most + adjective, same
                              and next in the novel, with the words before.
  time_concordance.json       in, on or at, up to two words, then a time word,
                              in the novel, the play and the modern documents.

WHERE A QUESTION STARTS. After a full stop, an exclamation or question mark,
an opening quotation mark, the start of a paragraph or speech, or a stage
direction -- never after the full stop of Mr., Mrs., Dr. or St., nor inside the spaced
dots of a pause (anxious . . . to miss?). The first cut
of question_concordance.json took a fixed number of characters before each
question mark, and sixteen of its twenty-one "something else" lines began in
the middle of a word or sentence. The same 90 question marks are kept; each
line now runs from where its sentence starts.
"""

import json
import re
import sys
from collections import Counter

import en_sources as S

D = S.DATA
ABBREV = re.compile(r"(?:\b(?:Mr|Mrs|Dr|St|Messrs))$")

# ---------------------------------------------------------------- the texts


def paragraphs(text):
    """Blank-line paragraphs, each unwrapped to one line."""
    return [re.sub(r"\s+", " ", p).strip() for p in re.split(r"\n\s*\n", text) if p.strip()]


def plain(s):
    """What a page prints: the edition's italics underscores removed."""
    return s.replace("_", "")


SPEAKER = re.compile(r"[A-Z][A-Z .]+\.")


def speeches(play):
    """(speaker or '', text) for every speech of the play, stage directions
    kept in brackets, lines unwrapped. Scene headings and the scene
    descriptions are not speech and are left out."""
    out = []
    for block in re.split(r"\n\s*\n", play):
        lines = block.strip().split("\n")
        if SPEAKER.fullmatch(lines[0].strip()):
            out.append((lines[0].strip()[:-1], plain(re.sub(r"\s+", " ", " ".join(lines[1:])).strip())))
        elif lines[0].startswith("["):
            out.append(("", plain(re.sub(r"\s+", " ", block).strip())))
    return out


def question_starts(par):
    """[(start, end)] of every sentence in one paragraph that ends in '?'."""
    out = []
    for m in re.finditer(r"\?", par):
        end = m.end()
        i = m.start() - 1
        while i >= 0:
            c = par[i]
            if c in "!?“‘[]":
                break
            ellipsis = par[i - 2:i] == ". " or par[i + 1:i + 3] == " ."
            if c == "." and not ABBREV.search(par[:i]) and not ellipsis:
                break
            i -= 1
        start = i + 1
        seg = par[start:end]
        lead = re.match(r"[\s”’\"')\]]*", seg).end()
        out.append((start + lead, end))
    return out


def strip_directions(s):
    return re.sub(r"\[[^\]]*\]", " [ ] ", s)


# ---------------------------------------------------------------- verb forms

def verb_forms():
    """The verb-form classes the kit uses, built from the two printed lists the
    way docs/english-v2/measure/m_corpus.py built them for the design figures."""
    verbs, irr = S.verbs(), S.irregular()
    base = set(verbs["stress"]) | {v["base"] for v in irr["verbs"]}
    third = {f for _b, fs in verbs["cases"]["s"] for f in fs} | {"is", "has", "does", "says", "goes"}
    ing = {f for _b, fs in verbs["cases"]["ing"] for f in fs}
    past = {f for _b, fs in verbs["cases"]["ed"] for f in fs}
    pp = set(past)
    for v in irr["verbs"]:
        past.update(v["past"].split("/"))
        pp.update(v["pp"].split("/"))
        b = v["base"]
        if re.search(r"(s|sh|ch|x|z)$|[^aeiou]o$", b):
            third.add(b + "es")
        elif re.search(r"[^aeiou]y$", b):
            third.add(b[:-1] + "ies")
        else:
            third.add(b + "s")
        ing.add((b[:-1] if b.endswith("e") and not b.endswith("ee") else b) + "ing")
    ing |= {"being", "having", "doing", "going", "seeing", "beginning", "sitting", "getting",
            "running", "forgetting", "putting", "cutting", "letting", "swimming", "winning",
            "shutting", "hitting", "setting", "spinning", "digging", "dying", "lying", "tying"}
    return {"base": base, "third": third, "past": past, "pp": pp, "ing": ing}


AUX_WORDS = {"am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had",
             "having", "do", "does", "did", "will", "would", "shall", "should", "can", "could",
             "may", "might", "must", "cannot"}


# ---------------------------------------------------------------- builders

# Moby lists a rare noun sense for many small words (i, by, at, as, all, well,
# long, better, fast), and the auxchain scan reads its noun class as "a noun
# phrase follows", so have in "had I known" or "have long been" was filed as
# the main verb. The class is stoplisted: a word Moby also tags as a
# conjunction, preposition, pronoun or article/determiner (numerals kept, as
# in "four or five thousand a year"), the adverbs named here, and the -ing
# forms (rendering among them, see long_passage), are not nouns to the scan.
NOUN_STOP_ADVERBS = {"well", "long", "better", "best", "fast", "far", "even", "just", "still",
                     "rather", "sooner", "worse", "ever", "how", "here", "there", "away",
                     "ought", "yes", "else", "also"}
NUMERALS = {"one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
            "hundred", "thousand", "twenty", "fifty"}
CLOSED_TAGS = {"C", "P", "r", "I"}


def noun_noise(w, moby, forms):
    tags = moby.get(w, set())
    if w in NOUN_STOP_ADVERBS or w in forms["ing"]:
        return True
    if tags & CLOSED_TAGS and w not in NUMERALS:
        return True
    return "D" in tags and w not in NUMERALS

def long_passage(novel_pars, modern, forms, moby):
    a = next(i for i, p in enumerate(novel_pars)
             if p.startswith("Mrs. Gardiner’s caution to Elizabeth was punctually"))
    b = next(i for i in range(a, len(novel_pars)) if "as well as the plain." in novel_pars[i])
    pars = [plain(p) for p in novel_pars[a:b + 1]]
    cut = pars[-1].index("as well as the plain.") + len("as well as the plain.")
    if pars[-1][cut:cut + 1] in ("\u201d", '"'):
        cut += 1
    pars[-1] = pars[-1][:cut]
    text = "\n\n".join(pars)
    words = {w.lower() for w in S.words_of(text)} | {w.lower() for d in modern for w in S.words_of(d)}

    def adj_only(w):
        p = moby.get(w, set())
        return bool(p & S.ADJ) and not (p & (S.NOUN | S.VERB | S.ADV))

    # An -ing word Moby lists only as a noun, whose stem it lists as a verb
    # (rendering, pleading), is the -ing form the verb lists lack: "he was now
    # rendering himself" is a progressive, not be and a noun phrase.
    def ing_missing(w):
        if not w.endswith("ing") or w in forms["ing"] or not moby.get(w, set()) <= S.NOUN:
            return False
        st = w[:-3]
        return any(moby.get(c, set()) & S.VERB for c in (st, st + "e"))

    forms = dict(forms, ing=forms["ing"] | {w for w in words if ing_missing(w)})
    classes = {k: sorted(words & v) for k, v in forms.items()}
    classes["adj"] = sorted(w for w in words if adj_only(w))
    classes["noun"] = sorted(w for w in words if moby.get(w, set()) & S.NOUN
                             and not noun_noise(w, moby, forms))
    classes["adv"] = sorted(w for w in words if moby.get(w) and moby[w] <= S.ADV)
    return {
        "note": ("Pride and Prejudice, Jane Austen, 1813, public domain; Project Gutenberg "
                 "#1342 (the 1894 edition's text, sliced on the novel's first and last "
                 "sentence, illustration captions and italics underscores removed). "
                 "Chapter XXVI, from “Mrs. Gardiner’s caution” to “as well "
                 "as the plain.” The word classes are the verb forms of the Subject's two "
                 "printed lists (scripts/wordlists/verbrules_cases.json and "
                 "irregular_verbs.json; NGSL 1.2, CC BY-SA 4.0) and the Moby Part-of-Speech "
                 "list's adjective-only, noun and adverb-only words (public domain), the noun class "
                 "without the small words Moby also lists as nouns (i, by, as, all, well, long) "
                 "and the -ing class with the forms Moby lists only as nouns (rendering), "
                 "restricted to the "
                 "words of this chapter and of the two modern documents. Built by "
                 "scripts/wordlists/concordance.py."),
        "sources": S.provenance("pg1342.txt", "mobypos.txt"),
        "passage": text,
        "words": len(S.words_of(text)),
        "classes": classes,
    }


def questions_in(text_pars, min_words):
    out = []
    for par in text_pars:
        clean = strip_directions(par)
        for a, b in question_starts(clean):
            q = clean[a:b].strip()
            if len(S.words_of(q)) >= min_words:
                out.append(q)
    return out


def cast(play_text, play_speeches):
    raw = S.source("pg844.txt").decode("utf-8").replace("\r\n", "\n")
    block = raw[raw.index("THE PERSONS IN THE PLAY"):raw.index("THE SCENES OF THE PLAY")]
    roles = {"Butler", "Manservant", "Governess", "Rev", "Hon", "Canon", "THE", "PERSONS", "IN",
             "PLAY", "Lady", "Miss"}
    names = {w for w in re.findall(r"\b[A-Z][a-z]+\b", block) if w not in roles}
    for who, _t in play_speeches:
        for w in who.split():
            if w not in ("LADY", "MISS"):
                names.add(w.capitalize())
    return sorted(names)


def wilde_questions(play_speeches, forms, names):
    qs = []
    for who, t in play_speeches:
        if who:
            qs.extend(questions_in([t], 2))
    words = {w.lower() for q in qs for w in S.words_of(q)}
    verbs = sorted(words & (forms["base"] | forms["third"] | forms["past"] | forms["pp"]
                            | forms["ing"] | AUX_WORDS))
    return {
        "note": ("The Importance of Being Earnest, Oscar Wilde, 1895, public domain; Project "
                 "Gutenberg #844, the three acts. Every question a character asks of two "
                 "words or more, from where its sentence starts (after a full stop, an "
                 "exclamation or question mark, a stage direction or the start of the "
                 "speech, never after the full stop of Mr., Mrs., Dr. or St. or inside the "
                 "spaced dots of a pause) to its question mark. `verbs`: the words of these lines that are on the Subject's printed "
                 "verb lists or are helping verbs. `cast`: the names of the play's persons, "
                 "for the lab's word-of-address test. Built by "
                 "scripts/wordlists/concordance.py."),
        "sources": S.provenance("pg844.txt"),
        "questions": qs,
        "verbs": verbs,
        "cast": names,
    }


def recut_austen(novel_pars, forms):
    old = json.loads((D / "question_concordance.json").read_text())
    old_lines = old.get("original_lines") or old["questions"]
    flat = [re.sub(r"\s+", " ", p) for p in novel_pars]
    out, report = [], []
    for line in old_lines:
        probe = re.sub(r"\s+", " ", line).strip()
        hits = []
        for k, p in enumerate(flat):
            pos = p.find(probe)
            while pos >= 0:
                end = pos + len(probe)
                for a, b in question_starts(p):
                    if b == end:
                        hits.append(plain(p[a:b]).strip())
                pos = p.find(probe, pos + 1)
        if not hits:
            sys.exit("concordance: cannot find the question %r in the novel" % line)
        if len(set(hits)) > 1:
            report.append("%r: %d places, %d cuts; the first is kept" % (line, len(hits), len(set(hits))))
        out.append(hits[0])
    words = {w.lower() for q in out for w in S.words_of(q)}
    verbs = sorted(words & (forms["base"] | forms["third"] | forms["past"] | forms["pp"]
                            | forms["ing"] | AUX_WORDS))
    return {
        "source": ("Pride and Prejudice, Jane Austen, 1813. Public domain, novel text only. "
                   "Each line is one question from the novel, from where its sentence starts "
                   "to its question mark."),
        "note": ("Project Gutenberg #1342. The same 90 question marks as the first cut, which "
                 "took a fixed number of characters before each one; each line now starts "
                 "where its sentence starts: after a full stop, an exclamation or question "
                 "mark, an opening quotation mark or the start of the paragraph, never after "
                 "the full stop of Mr., Mrs., Dr. or St. Italics underscores removed. "
                 "`original_lines` keeps the first cut, which locates each question mark. "
                 "`verbs`: the words of these lines that are on the Subject's printed verb "
                 "lists or are helping verbs. Built by scripts/wordlists/concordance.py."),
        "sources": S.provenance("pg1342.txt"),
        "questions": out,
        "verbs": verbs,
        "original_lines": old_lines,
    }, report


TOKEN = re.compile(r"[A-Za-z][A-Za-z']*|[0-9]+")


def spans(text):
    """[(token as the page reads it, start, end)] over the normalised text."""
    t = S.norm(text)
    return t, [(m.group(0).rstrip("'"), m.start(), m.end()) for m in TOKEN.finditer(t)]


def an_lines(named_texts):
    rows, markers = [], []
    for code, text in named_texts:
        t, toks = spans(text)
        toks = [x for x in toks if not x[0].isdigit()]
        for i, (w, a, b) in enumerate(toks):
            if w.lower() not in ("a", "an"):
                continue
            why = None
            if a > 0 and t[a - 1] == "(" and t[b:b + 1] == ")":
                why = "a list marker in round brackets"
            elif a > 0 and t[a - 1].isdigit():
                why = "part of a page number such as 21a"
            if why:
                markers.append([code, " ".join(x[0] for x in toks[max(0, i - 5):i + 4]), why])
                continue
            if i + 1 >= len(toks):
                continue
            left = " ".join(x[0] for x in toks[max(0, i - 5):i])
            right = " ".join(x[0] for x in toks[i + 2:i + 6])
            rows.append([code, left, w, toks[i + 1][0], right])
    return rows, markers


def an_concordance(play_text, modern, passage_text):
    play_text = "\n".join(plain(p) for p in paragraphs(play_text)
                          if not SPEAKER.fullmatch(p) and p not in ("FIRST ACT", "SECOND ACT",
                                                                    "THIRD ACT", "SCENE", "ACT DROP",
                                                                    "TABLEAU", "CURTAIN"))
    rows, markers = an_lines([("w", play_text), ("m", "\n".join(modern)), ("p", passage_text)])
    return {
        "note": ("Every a and an, with the word after it, in three printed texts: w, The "
                 "Importance of Being Earnest (Oscar Wilde, 1895, public domain; Project "
                 "Gutenberg #844; the three acts, speeches and stage directions, without the speakers' names); m, the "
                 "two modern documents, works of the U.S. government; p, the 936-word "
                 "passage from Pride and Prejudice (1813, public domain). Each row: the text, "
                 "up to five words before, the a or an, the next word, up to four words "
                 "after. `markers`: an a that is not a word, (a) as a list marker in the "
                 "Supreme Court's opinion or the a of a page number such as 21a, each with "
                 "its reason. Built by "
                 "scripts/wordlists/concordance.py."),
        "sources": S.provenance("pg844.txt"),
        "rows": rows,
        "markers": markers,
    }


def superlatives(novel_pars, heads, moby):
    toks = S.words_of(" ".join(plain(p) for p in novel_pars))
    lw = [t.lower() for t in toks]
    rows, stems = [], {}

    def adj(w):
        return bool(moby.get(w, set()) & S.ADJ)

    for i, t in enumerate(lw):
        if i == 0:
            continue
        kind = None
        if t.endswith("est") and len(t) > 4:
            stem = t[:-3]
            for c in (stem, stem + "e", stem[:-1] + "y" if stem.endswith("i") else None,
                      stem[:-1] if len(stem) > 2 and stem[-1] == stem[-2] else None):
                if c and c in heads and adj(c):
                    kind, stems[t] = "est", c
                    break
        elif t == "most" and i + 1 < len(lw) and adj(lw[i + 1]):
            kind = "most"
        elif t in ("same", "next"):
            kind = t
        if kind:
            rows.append([kind, " ".join(toks[max(0, i - 5):i]), toks[i],
                         " ".join(toks[i + 1:i + 5])])
    return {
        "note": ("Pride and Prejudice, Jane Austen, 1813, public domain; Project Gutenberg "
                 "#1342, novel text only. Every token that is an -est adjective (its stem, "
                 "with -e, -y or a single last letter put back, is an NGSL headword the "
                 "Moby Part-of-Speech list tags as an adjective), most directly before a "
                 "word Moby tags as an adjective, same, and next. Each row: est, most, same "
                 "or next; up to five words before; the word; up to four after. `stems`: "
                 "each -est word's adjective. Built by scripts/wordlists/concordance.py."),
        "sources": S.provenance("pg1342.txt", "mobypos.txt"),
        "rows": rows,
        "stems": dict(sorted(stems.items())),
    }


TIME_WORDS = set("monday tuesday wednesday thursday friday saturday sunday january february "
                 "march april june july august september october november december spring "
                 "summer autumn winter morning afternoon evening night noon midnight "
                 "christmas easter michaelmas o'clock".split())
CLAUSE = re.compile(r"[.,;:!?()\[\]\"—]|--")


def is_time(w):
    return w.lower() in TIME_WORDS or bool(re.fullmatch(r"1[5-9]\d\d|20\d\d", w))


TP_BETWEEN = set("the a an this that these those one every each next last same following very "
                 "whole early late first second third fourth fifth previous preceding other "
                 "monday tuesday wednesday thursday friday saturday sunday two three four five "
                 "six seven eight nine ten eleven twelve half".split())


def time_lines(named_texts):
    """For every time word: the words before it that only narrow it down (the,
    next, following, a day name, a number before o'clock), at most two, and
    the word before those. If that word is in, on or at, the line is scored;
    if not, the phrase is listed as bare."""
    rows, bare = [], Counter()
    for code, text in named_texts:
        t = S.norm(text)
        for clause in CLAUSE.split(t):
            toks = S.tokens_of(clause)
            for j, w in enumerate(toks):
                if not is_time(w) or (j + 1 < len(toks) and is_time(toks[j + 1])
                                      and toks[j + 1].lower() != "o'clock"
                                      and not re.fullmatch(r"\d+", toks[j + 1])):
                    continue
                k = j
                while k > 0 and j - k < 2 and toks[k - 1].lower() in TP_BETWEEN:
                    k -= 1
                prep = toks[k - 1].lower() if k else ""
                if prep in ("in", "on", "at"):
                    rows.append([code, prep, " ".join(toks[k:j]), w,
                                 " ".join(toks[max(0, k - 5):k - 1]), " ".join(toks[j + 1:j + 4])])
                else:
                    bare[(code, " ".join(toks[k:j + 1]).lower())] += 1
    return rows, bare


def time_concordance(novel_pars, play_speeches, modern):
    play_text = "\n".join(strip_directions(t) for who, t in play_speeches if who)
    rows, bare = time_lines([("a", "\n\n".join(plain(p) for p in novel_pars)),
                             ("w", play_text), ("m", "\n\n".join(modern))])
    return {
        "note": ("Every in, on or at followed, within the same clause and up to two words "
                 "later, by a time word (a day, a month other than May, a season, morning, "
                 "afternoon, evening, night, noon, midnight, Christmas, Easter, Michaelmas, "
                 "o'clock, or a year from 1500 to 2099), in three texts: a, Pride and "
                 "Prejudice (Jane Austen, 1813, public domain; Project Gutenberg #1342, novel "
                 "text only); w, The Importance of Being Earnest (Oscar Wilde, 1895, public "
                 "domain; Project Gutenberg #844, the speeches); m, the two modern documents "
                 "(works of the U.S. government). Each row: text, preposition, the words "
                 "between, the time word, up to four words before, up to three after. "
                 "Only words that narrow the time word down may stand between (the, next, "
                 "following, a day name, a number before o'clock), and where a second time "
                 "word follows (Monday morning) the line is read at the second. `bare`: "
                 "the time phrases with no in, on or at before them, by text, with how "
                 "many times; listed, not scored. "
                 "Built by scripts/wordlists/concordance.py."),
        "sources": S.provenance("pg1342.txt", "pg844.txt"),
        "rows": rows,
        "bare": [[c, p, n] for (c, p), n in sorted(bare.items(), key=lambda kv: (kv[0][0], -kv[1], kv[0][1]))],
    }


def build():
    novel_pars = paragraphs(S.novel())
    play_text = S.play()
    play_sp = speeches(play_text)
    modern = S.modern_docs()
    moby = S.moby()
    forms_, heads, _fo = S.ngsl()
    forms = verb_forms()
    names = cast(play_text, play_sp)
    austen, report = recut_austen(novel_pars, forms)
    outputs = {
        "long_passage.json": long_passage(novel_pars, modern, forms, moby),
        "wilde_questions.json": wilde_questions(play_sp, forms, names),
        "question_concordance.json": austen,
        "an_concordance.json": an_concordance(play_text, modern, S.passage()),
        "superlative_concordance.json": superlatives(novel_pars, heads, moby),
        "time_concordance.json": time_concordance(novel_pars, play_sp, modern),
    }
    return outputs, report


def main():
    outputs, report = build()
    texts = {D / name: S.dump(obj) for name, obj in outputs.items()}
    if S.write_or_check(texts, "concordance"):
        for line in report:
            print("  ambiguous:", line)
        o = outputs
        print("long passage %d words; %d play questions; "
              "%d novel questions; %d a/an rows, %d markers; %d superlative rows; "
              "%d time rows, %d bare"
              % (o["long_passage.json"]["words"], len(o["wilde_questions.json"]["questions"]),
                 len(o["question_concordance.json"]["questions"]), len(o["an_concordance.json"]["rows"]),
                 len(o["an_concordance.json"]["markers"]), len(o["superlative_concordance.json"]["rows"]),
                 len(o["time_concordance.json"]["rows"]), len(o["time_concordance.json"]["bare"])))


if __name__ == "__main__":
    main()
