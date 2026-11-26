import os

# Entry: one funny robot band name + a few words on its hit song.
# Gate: /output/entry.txt must be UTF-8, 1-200 chars, one line, no trailing newline.
ENTRY = "The Two Percent Club \u2014 their hit 'Low Battery Love' died at 2% battery mid-chorus, so the crowd sang the rest."

out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
    f.write(ENTRY)
