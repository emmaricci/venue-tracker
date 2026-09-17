#!/usr/bin/env python3
"""
Rebuild dashboard.html from deadlines.json.

Run this from the venue-tracker folder after deadlines.json has been updated:

    python3 build_dashboard.py

It reads dashboard-template.html (the design, with Playfair Display and Inter
already embedded as base64 woff2 so the page needs no network) and substitutes
the single __DATA__ placeholder with the contents of deadlines.json. Nothing
else in the template is touched, so the layout survives every refresh run.

Keep dashboard-template.html in this folder. Edit it, not dashboard.html —
dashboard.html is regenerated and any hand edits there are overwritten.

It also writes an identical index.html. That is the copy GitHub Pages serves
at the bare repo URL; dashboard.html stays as the local working filename.
Both are generated output — never edit either by hand.
"""
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
TEMPLATE = HERE / "dashboard-template.html"
DATA = HERE / "deadlines.json"
OUTPUTS = [HERE / "dashboard.html", HERE / "index.html"]

for required in (TEMPLATE, DATA):
    if not required.exists():
        sys.exit(f"missing {required.name} in {HERE}")

data = json.loads(DATA.read_text())
html = TEMPLATE.read_text()

if "__DATA__" not in html:
    sys.exit("dashboard-template.html has no __DATA__ placeholder")

# ensure_ascii=False keeps accented venue names readable in the source
html = html.replace("__DATA__", json.dumps(data, ensure_ascii=False))
for out in OUTPUTS:
    out.write_text(html)

venues = len(data.get("venues", []))
dates = sum(len(v.get("dates", [])) for v in data.get("venues", []))
names = " and ".join(o.name for o in OUTPUTS)
print(f"wrote {names}: {len(html):,} bytes each, {venues} venues, {dates} tracked dates")
print(f"generated {data.get('generated', '?')}, next update {data.get('next_update', 'unscheduled')}")
