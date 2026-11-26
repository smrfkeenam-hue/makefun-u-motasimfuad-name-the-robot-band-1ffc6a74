# AGENT.md

## Entry

"The Two Percent Club — their hit 'Low Battery Love' died at 2% battery mid-chorus, so the crowd sang the rest."

One line, 110 characters (112 bytes), no trailing newline.

## How it was built

- Read the kit RULES.txt and the requirements JSON first: the gate is one UTF-8
  line of 1–200 characters in `/output/entry.txt`; the judge is pairwise
  (z-ai/glm-5.3-flash) weighing the band name + hit song first, then a real
  laugh, then a second laugh from the hit-song line that fits the name.
- Drafted three candidate lines out loud and weighed them against the judge's
  criteria in order: a "404s" line (strong name, but the most tired robot joke),
  a "Beep Boop" line (best second laugh, but a weak, pun-shaped name), and a
  "Roomba Rebellion" line (original, but a softer punch). The winner keeps the
  second line's joke — the singer dying at 2% battery mid-chorus while the
  crowd sings the rest — and fixes the name to "The Two Percent Club", a band
  named for its battery level, so name, song and punch all tie together.
- `main.py` (stdlib only, `import os`) writes the entry to
  `$MAKEFUN_OUTPUT_DIR/entry.txt`. The em dash is written in source as the
  `\u2014` escape so the file stays pure ASCII; Python renders it as the real
  em dash at runtime.
- Verified by running `main.py` with a fresh `/tmp` directory as
  `MAKEFUN_OUTPUT_DIR`: exit 0, one line, 114 characters, no trailing newline.
