"""Spoken forms for the English Subject.

Keyed by the exact run text; see content/AGENTS.md, "Write math a voice can read".

The ambiguity detector in scripts/speechcheck.py looks for the shapes of
mathematical notation, and English's monospace runs hold words, endings and
sounds instead, so it reported nothing and this file once shipped empty. Read
aloud by the rules, though, an ending such as `-s` became "negative s", a
slash list such as `know / knew / known` became "know over knew over known",
and a pronunciation such as `tə` was read letter by letter. Each run below was
read on the page and given the words a listener should hear. They are specific
to English's own lines, so none of them changes a reading in another Subject;
tests/test_speech.py checks that a reading is never claimed twice.
"""

SPOKEN = {
    'base   he, she, it   -ing   past   after have': 'base, he, she, it, the ing form, past, after have',
    'be + -ing form       still going on': 'be plus the ing form, still going on',
    '-s 99.92%   -ing 99.34%   -ed 99.26%': 'the s rule 99.92 percent, the ing rule 99.34 percent, the ed rule 99.26 percent',
    '-s 99.92%    -ing 99.34%    -ed 99.26%': 'the s rule 99.92 percent, the ing rule 99.34 percent, the ed rule 99.26 percent',
    '-ing form       walking': 'the ing form, walking',
    '-s      1209 of 1210 right     99.92%': 'the s rule, 1209 of 1210 right, 99.92 percent',
    '-ing    1202 of 1210 right     99.34%': 'the ing rule, 1202 of 1210 right, 99.34 percent',
    '-ed     1201 of 1210 right     99.26%': 'the ed rule, 1201 of 1210 right, 99.26 percent',
    'of the 18 still wrong, 11 end in -l': 'of the 18 still wrong, 11 end in the letter l',
    'ending in -l   cancel, channel, counsel,': 'ending in the letter l, cancel, channel, counsel',
    'base / past / form after have': 'base, past, form after have',
    'walk / walked / walked': 'walk, walked, walked',
    'bring / brought / brought': 'bring, brought, brought',
    '60: past = form after have (bring)': '60, the past equals the form after have, as in bring',
    '37: all differ, ends in -n (know)': '37, all three differ and the last ends in n, as in know',
    '21: all three the same (put)': '21, all three the same, as in put',
    '9: all differ, not -n (go, sing)': '9, all three differ and the last does not end in n, as in go and sing',
    '4: base = form after have (come)': '4, the base equals the form after have, as in come',
    '1: base = past (beat)': '1, the base equals the past, as in beat',
    'know / knew / known: ends in n': 'know, knew, known, ends in n',
    'go / went / gone: ends in e': 'go, went, gone, ends in e',
    'sing / sang / sung: ends in g': 'sing, sang, sung, ends in g',
    'all three differ, -n     37': 'all three differ, ending in n, 37',
    'you know       ->  do you know?': 'you know becomes do you know',
    'she went       ->  did she go?': 'she went becomes did she go',
    'she can go     ->  can she go?': 'she can go becomes can she go',
    'she went where ->  where did she go?': 'she went where becomes where did she go',
    'to = tə     of = əv     and = ən': 'to is said tuh, of is said uv, and is said un',
    'and     ən        the     ðə': 'and is said un, the is said thuh',
    'to      tə        of      əv': 'to is said tuh, of is said uv',
    'was     wəz       that    ðət': 'was is said wuz, that is said thut',
    'for     fə        have    həv': 'for is said fuh, have is said huv',
    'can     kən       you     jə': 'can is said kun, you is said yuh',
    'S = said hardest   . = said lightly': 'capital S marks the part said hardest, a dot marks a part said lightly',
    's = some weight, but not the most': 'a small s marks a part with some weight, but not the most',
    'FAther  ANswer  CARriage': 'father, answer, carriage, each said hardest on its first part',
    'beLIEVE  aGAIN  reTURN': 'believe, again, return, each said hardest on its second part',
    'FAther  S.       beLIEVE   .S': 'father, strong then light, believe, light then strong',
    'ANswer  S.       aGAIN     .S': 'answer, strong then light, again, light then strong',
    'MARket   S.      reTURN    .S': 'market, strong then light, return, light then strong',
    'HAPpiness S..    aNOTHer   .S.': 'happiness, strong then light then light, another, light then strong then light',
    '   the -ed rule builds both': 'the ed rule builds both',
    # Sounds and stress marks written into prose (speech.islands), not math runs
    'tə': 'tuh',
    'fə': 'fuh',
    'fər': 'fur',
    's.S': 'some weight, light, strong, light',
}
