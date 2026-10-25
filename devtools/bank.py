"""Read-only view of the paper-setting question bank (5086 / 5076 Combined Science physics + school papers) for writing
trainer questions. Prints a compact list: id, type, marks, first part of the text. Questions are ADAPTED, never copied.

    python devtools/bank.py 12            # 6091 chapter -> bank topic(s)
    python devtools/bank.py 12 --text "critical angle" --type mcq --n 30
"""
import argparse
import json
import sys
from pathlib import Path

BANK = Path(r"C:\Users\pirat\Downloads\Claude\Agent for paper setting\Sec 3 and 4 G3 ScPhysics\question-bank\bank.json")
# 6091 chapter -> 5086 topic numbers used to tag the bank
MAP = {1: [1], 2: [2], 3: [3, 4], 4: [5], 5: [3], 6: [6], 7: [7], 8: [8], 9: [7, 8], 10: [9], 11: [10], 12: [11], 13: [12],
       14: [12], 15: [13], 16: [14], 17: [15], 18: [15], 19: [15], 20: [16]}

if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser()
    ap.add_argument("chapter", type=int)
    ap.add_argument("--text")
    ap.add_argument("--type")
    ap.add_argument("--n", type=int, default=40)
    ap.add_argument("--width", type=int, default=260)
    ap.add_argument("--seab", action="store_true")
    a = ap.parse_args()
    recs = json.loads(BANK.read_text(encoding="utf-8"))
    topics = MAP[a.chapter]
    out = []
    for r in recs:
        if r.get("dup_of") or r.get("auto_subject") != "Physics":
            continue
        if not any(x["topic"] in topics and x["score"] >= 0.85 for x in r.get("auto", [])[:2]):
            continue
        if a.type and r["type"] != a.type:
            continue
        if a.seab and r.get("board") != "SEAB":
            continue
        if a.text and not all(w.lower() in r["text"].lower() for w in a.text.split()):
            continue
        out.append(r)
    out.sort(key=lambda r: (r.get("board") != "SEAB", -(r.get("year") or 0)))
    print(f"{len(out)} matching (showing {min(a.n, len(out))})")
    for r in out[: a.n]:
        t = " ".join(r["text"].split())[: a.width]
        print(f"[{r['id']}] {r.get('board')} {r.get('year')} {r['type']} {r['marks']}m: {t}")
