# Writing a lesson's videos

Every lesson gets four files. `<key>` is `<course-slug>/<lesson-slug>`.

    video/episodes/<key>/long.md        full lesson, 16:9, about 4 to 5 minutes (600 to 750 spoken words)
    video/episodes/<key>/short.md       short, 9:16, 20 to 40 seconds (60 to 100 spoken words)
    video/art/<key>/scenes.prompt.md    Codex prompt for six illustrations
    video/art/<key>/thumb.prompt.md     Codex prompt for the thumbnail art

The finished example to copy is Chain of Responsibility:
`video/episodes/gof-behavioral-requests/chain-of-responsibility/` and its prompts in
`video/art/chain-of-responsibility-*.prompt.md` (older naming; new lessons use the
layout above). The scene format is the docstring of `video/episode.py`. Read the
lesson first: `python3 -c "import sys; sys.path.insert(0,'.'); from video import lessons as L; print(L.outline(L.find('<key>')[2]))"`.

Check as you go: `python3 video/make_video.py --check`. Every error except
"art ... is not in video/assets/art" must be fixed (art is drawn later on the
ThinkCentre from your prompts).

## Voice

- Written to be **read aloud** by one calm, friendly narrator explaining at a
  whiteboard. Second person ("you"), short sentences, contractions. No "In this
  video", no "Welcome back", no "smash that like button".
- **Retell the lesson in your own words.** The lesson is the source; the video is
  not a reading of the page. Keep every fact, number and worked result exactly as
  the lesson has it. Never invent a result, a quotation or a statistic. Where the
  lesson quotes a book, a `@quote` may use the lesson's own quotation, word for word.
- The narration may contain only letters, digits and `. , ? ! ' : ; % -`. Write
  symbols as words: "x squared", "a over b", "the square root of two", "minus",
  "less than or equal to", "pi". Say numbers the way a person says them.
  On-screen text (`text=`, `sub=`, `items=`, `heading=`) can use any symbol.
- Every word on screen should be spoken in the same scene, at about the moment it
  appears (a `@list` or `@math` item appears when its `@phrase` is said; the phrase
  must be copied exactly from that scene's narration).
- A scene's narration is 1 to 4 sentences (at most about 60 words), so the picture
  changes at least every 15 to 20 seconds.

## Shape

**long.md**: `format: long`, `lesson: <key>`, `title:` (a natural YouTube title),
`thumb:` (2 to 6 words, the payoff). Six to nine `@chapter`s, for example: the
question or problem, the idea, the method, a worked example (step by step with
`@math`), common mistakes (`@list`), when to use it, a practice prompt taken from
the lesson's exercise or worked example, and `@end`. Open with `@title` using
`art=thumb`. Use the six illustrations once or twice each, and mix `@words`,
`@math`, `@list`, `@code` (only the lesson's own code blocks, by number) and
`@quote` so the screen keeps changing. End with
`@end text="..."` and a last line that names Learn: "...on Learn. That's learn dot
get er done dot I O."

**short.md**: `format: short`, same lesson. One idea only: a hook of at most 14
words in the first scene (a question or a surprising fact), two to four scenes
that land the idea, then `@end text="Full lesson on Learn"` with one sentence.

## Art prompts

Copy `video/art/chain-of-responsibility-scenes.prompt.md` and change only the
save path, the subject sentence and the six cells. Keep the STYLE block word for
word, except the line naming what the cyan and yellow mean in this lesson.

- Save path line: `` save it as `video/art/<key>/scenes.png` `` (thumb: `thumb.png`).
- Keep `Strict grid: 2 columns x 3 rows.`
- Each cell is one numbered line **starting with its art name and a colon**:
  `1. number-line: a long horizontal white line with ...`. The names (lowercase,
  digits, hyphens) are what the scripts use in `@art <name>`; the batch tool cuts
  the sheet into those files in that order.
- **Absolutely no text, letters or numbers in the art**, so do not draw anything
  whose meaning depends on digits or symbols (show a number line as ticks and
  dots, a graph as axes and a curve, a fraction as a split shape). Put the actual
  mathematics in `@math` and `@words` scenes instead.
- The thumbnail prompt is the chain one with the composition sentence changed;
  its art is named `thumb`.
