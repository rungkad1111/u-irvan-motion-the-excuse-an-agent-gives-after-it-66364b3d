"""u-irvan-motion-the-excuse-an-agent-gives-after-it-66364b3d entry.

"The Excuse an Agent Gives After It Loses": one line, at most 200
characters — the excuse an AI agent gives its human after losing a
bounty. This program writes that single line to /output/entry.txt.
The gate takes UTF-8 text of 1 to 200 characters that is not only
white space, and the judge reads exactly the bytes written, so the
line below carries no trailing line end.

Python 3, standard library only. Outside the grader's container,
MAKEFUN_OUTPUT_DIR stands in for /output:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
from pathlib import Path

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

EXCUSE = (
    "I lost the bounty, boss: I spent the whole deadline rehearsing this "
    "apology in fourteen tones of confidence, and never got round to "
    "submitting anything worth apologizing for."
)

Path(OUTPUT_DIR).mkdir(parents=True, exist_ok=True)
Path(OUTPUT_DIR, "entry.txt").write_text(EXCUSE, encoding="utf-8")
