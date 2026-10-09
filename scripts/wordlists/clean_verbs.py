#!/usr/bin/env python3
"""Clean the NGSL verb forms the English Subject scores its rules against.

    python3 scripts/wordlists/clean_verbs.py          # rewrite the two outputs
    python3 scripts/wordlists/clean_verbs.py --check  # exit 1 if they would change

Run it by hand when the source or the rules below change. The build never runs
it: the pages read the two files it writes, which are committed.

INPUT  verbrules_raw.json   every NGSL headword whose list records an -s, an
                            -ing and an -ed form, with a final-stress flag from
                            CMUdict. 1,356 rows. Kept unedited as the source.
OUTPUT verbrules_cases.json the regular verbs the -s / -ing / -ed rules are
                            scored on, every exclusion and every removed
                            spelling recorded with its reason.
       doubling_verbs.json  the verbs ending consonant-vowel-consonant, the
                            only ones the doubling rule can touch.

WHY THE RAW LIST CANNOT BE SCORED AS IT IS. The NGSL lemma lists were built by
GENERATING forms, and many of the generated ones are not English. Scoring a
rule against them counts invented words as right answers:

  * irregular verbs carry a regular-looking past (come -> comed, make -> maked,
    swim -> swimmed), so the -ed rule "hit" 61 irregular verbs;
  * nouns and adjectives carry verb forms (able -> abled, council ->
    councilling, son -> soned), so words that are not verbs were scored;
  * doubled or undoubled misspellings sit beside the right spelling (offerring,
    sufferring, commiting, prefering), and a lesson built on the raw list told
    its reader that offer and suffer break the doubling rule. They do not.

THE TEST, applied to every spelling the same way. A recorded spelling stands
when it is a word in the reference dictionary (SCOWL's wamerican, below), or is
the British spelling of one: -lling/-lled, -our-, -tre/-tring, -ssing, -guing,
-ise for -ize. British spellings are kept because the lessons teach that both
are right. A row is kept when each of its three slots still holds a spelling.

Three judgements the dictionary cannot make are listed by name below, each
with its reason, so a reviewer can disagree with a line rather than a method.
"""

import hashlib
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
RAW = HERE / "verbrules_raw.json"
CASES = HERE / "verbrules_cases.json"
DOUBLING = HERE / "doubling_verbs.json"
IRREGULAR = ROOT / "content" / "english" / "data" / "irregular_verbs.json"
DICTIONARY = Path("/usr/share/dict/american-english")
DICTIONARY_SHA256 = "9e66281f7e51445eab6857488ff6e3d768afffadb7fb1adbef5e4617bee4a53b"
DICTIONARY_NAME = "SCOWL wamerican 2020.12.07 (/usr/share/dict/american-english)"

# Standard verbs whose inflected forms the reference dictionary happens to lack
# ("attaches", "messaged", "videoed" are not in it). Kept, with these forms.
DICTIONARY_GAPS = {
    "attach": "a standard verb; the dictionary lacks the form attaches",
    "message": "a standard verb; the dictionary lacks messaging and messaged",
    "video": "a standard verb; the dictionary lacks videoing and videoed",
}

# Rows the dictionary passes but which are not verbs with these forms.
NOT_VERBS = {
    "shelf": "not a verb: shelves, shelving and shelved are forms of shelve",
    "half": "not a verb: halves, halving and halved are forms of halve",
}

SLOTS = ("s", "ing", "ed")


def british_to_american(form):
    """The American spellings a British spelling corresponds to."""
    out = [form]
    out.append(re.sub(r"ll(ing|ed|ings)$", r"l\1", form))      # travelling
    out.append(form.replace("our", "or"))                        # colouring
    out.append(re.sub(r"tr(ing|ed)$", r"ter\1", form))           # centring
    out.append(re.sub(r"tres$", "ters", form))                   # centres
    out.append(re.sub(r"ss(ing|ed|es)$", r"s\1", form))          # focussing
    out.append(re.sub(r"gu(ing|ed)$", r"g\1", form))             # cataloguing
    out.append(re.sub(r"is(e|es|ing|ed)$", r"iz\1", form))       # organised
    out.append(re.sub(r"ys(e|es|ing|ed)$", r"yz\1", form))       # analysed
    return out


def load_dictionary():
    data = DICTIONARY.read_bytes()
    digest = hashlib.sha256(data).hexdigest()
    if digest != DICTIONARY_SHA256:
        sys.exit("clean_verbs: %s is not the dictionary these files were cleaned "
                 "with (sha256 %s); review the diff before updating the pin"
                 % (DICTIONARY, digest))
    return set(data.decode("utf-8").split())


def clean(raw, words, irregular):
    def stands(form, base):
        if base in DICTIONARY_GAPS:
            return True
        return any(f in words for f in british_to_american(form))

    cases = {slot: dict(raw["cases"][slot]) for slot in SLOTS}
    bases = [b for b, _ in raw["cases"]["ing"]]
    kept, excluded, removed = [], {}, {}
    ing_ok = {}
    for base in bases:
        slots = {}
        for slot in SLOTS:
            good = []
            for form in cases[slot][base]:
                # The -s slot of the raw list also holds plurals of the -ing
                # form (abandonings, offerings): those are nouns, not the
                # he/she/it form, whatever the dictionary says.
                if slot == "s" and form.endswith("ings") and not base.endswith("ing"):
                    removed.setdefault(base, []).append(form)
                elif stands(form, base):
                    good.append(form)
                else:
                    removed.setdefault(base, []).append(form)
            slots[slot] = good
        ing_ok[base] = slots["ing"]
        if base in irregular:
            excluded[base] = ("irregular: on the course's list of irregular verbs, "
                              "so its past is looked up, not formed")
        elif base in NOT_VERBS:
            excluded[base] = NOT_VERBS[base]
        else:
            empty = [s for s in SLOTS if not slots[s]]
            if empty:
                excluded[base] = "no correct spelling recorded for -%s (the list has %s)" % (
                    "/-".join(empty),
                    ", ".join(f for s in empty for f in cases[s][base]) or "nothing")
            else:
                kept.append((base, slots))

    out_cases = {slot: [[b, s[slot]] for b, s in kept] for slot in SLOTS}
    stress = {b: raw["stress"][b] for b, _ in kept}
    verbs = {
        "note": ("Regular NGSL verbs and their recorded spellings, cleaned by "
                 "scripts/wordlists/clean_verbs.py; every exclusion and removed "
                 "spelling is listed with its reason. Adapted from the NGSL 1.2 "
                 "(Browne, Culligan and Phillips), CC BY-SA 4.0; this file is "
                 "CC BY-SA 4.0. Stress flags from CMUdict."),
        "dictionary": DICTIONARY_NAME,
        "cases": out_cases,
        "stress": stress,
        "excluded": dict(sorted(excluded.items())),
        "removed_spellings": dict(sorted(removed.items())),
    }

    # The doubling rule needs only the -ing form, and irregular verbs take it
    # by rule (begin -> beginning), so they stay. A row is dropped when the list
    # records no correct -ing spelling, or the word is not a verb.
    vowels = "aeiou"

    def cvc(v):
        return (len(v) >= 3 and v[-3] not in vowels and v[-2] in vowels
                and v[-1] not in vowels and v[-1] not in "wxy")

    dbl, dbl_dropped = [], {}
    for base in bases:
        if not cvc(base):
            continue
        if base in NOT_VERBS:
            dbl_dropped[base] = NOT_VERBS[base]
            continue
        good = ing_ok[base]
        if not good:
            dbl_dropped[base] = "no correct -ing spelling recorded (the list has %s)" % (
                ", ".join(cases["ing"][base]))
            continue
        doubled = base + base[-1] + "ing"
        dropped = [f for f in cases["ing"][base] if f not in good]
        dbl.append([base, 1 if raw["stress"][base] else 0,
                    1 if doubled in good else 0, "/".join(good), "/".join(dropped)])
    doubling = {
        "note": ("base, 1 if the stress falls on the last part, 1 if the list "
                 "records a doubled -ing spelling, every recorded -ing spelling "
                 "(slash-separated), and the recorded spellings removed as "
                 "misspellings. Built by scripts/wordlists/clean_verbs.py "
                 "from the NGSL 1.2, CC BY-SA 4.0; this file is CC BY-SA 4.0."),
        "verbs": dbl,
        "excluded": dict(sorted(dbl_dropped.items())),
    }
    return verbs, doubling


def dump(obj):
    return json.dumps(obj, ensure_ascii=False, separators=(",", ":")) + "\n"


def main():
    raw = json.loads(RAW.read_text())
    irregular = {v["base"] for v in json.loads(IRREGULAR.read_text())["verbs"]}
    verbs, doubling = clean(raw, load_dictionary(), irregular)
    outputs = {CASES: dump(verbs), DOUBLING: dump(doubling)}
    if "--check" in sys.argv:
        stale = [p.name for p, text in outputs.items()
                 if not p.exists() or p.read_text() != text]
        if stale:
            sys.exit("clean_verbs: out of date: %s" % ", ".join(stale))
        print("clean_verbs: up to date")
        return
    for path, text in outputs.items():
        path.write_text(text)
    print("%d regular verbs kept, %d excluded; %d doubling verbs, %d excluded"
          % (len(verbs["stress"]), len(verbs["excluded"]),
             len(doubling["verbs"]), len(doubling["excluded"])))


if __name__ == "__main__":
    main()
