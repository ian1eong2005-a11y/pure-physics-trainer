"""Write OLEVEL_MCQ_COVERAGE.md: every 6091 learning outcome -> its O-level practice questions and P2 2026 note, and every MCQ of the
SEAB 6091 specimen Paper 1 -> the item that adapts it. Run: python tools/olevel_coverage.py"""
import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "tests"))

from test_olevel import ALL_LOS, OLEVEL, SPECIMEN  # noqa: E402

from trainer.config import CHAPTERS, p2_2026_note  # noqa: E402

src_of, cites = {}, defaultdict(list)
for t in OLEVEL:
    text = " ".join(t.make(0).working)
    m = re.search(r"_Adapted from (.+?)\._", text)
    src_of[t.id] = m.group(1) if m else "?"
    for mm in re.finditer(r"SEAB 6091 specimen paper 2024 MCQ (\d+)((?: and MCQ \d+)*)", text):
        cites[int(mm.group(1))].append(t.id)
        for m2 in re.finditer(r"and MCQ (\d+)", mm.group(2)):
            cites[int(m2.group(1))].append(t.id)

by_lo = defaultdict(list)
for t in OLEVEL:
    by_lo[t.lo].append(t)
n_spec = sum(1 for t in OLEVEL if "SEAB 6091 specimen" in src_of[t.id])
n_seab_other = sum(1 for t in OLEVEL if src_of[t.id].startswith("SEAB") and "SEAB 6091 specimen" not in src_of[t.id])
n_5086 = sum(1 for t in OLEVEL if "(5086)" in src_of[t.id])
n_school = len(OLEVEL) - n_spec - n_seab_other
notes = defaultdict(int)
for t in OLEVEL:
    notes[p2_2026_note(t.lo) or "tested in P2 2026 (no note)"] += 1
out = ["# O level 2026 MCQ practice: coverage", "",
       f"{len(OLEVEL)} questions: {n_spec} adapted from the SEAB 6091 specimen Paper 1 (2024, all 40 MCQs), {n_school} adapted from schools' "
       f"2024-2026 Paper 1 prelims ({n_5086} of them from 2024 Science (Physics) 5086 prelims, for outcomes no 6091 paper on file tests) and "
       f"{n_seab_other} from SEAB O-Level 5076 Paper 1. Every one of the {len(ALL_LOS)} learning outcomes has at least one question.",
       "", "The note comes from the teacher's mapping of the 2026 6091 Paper 2 to learning outcomes (`OLEVEL_MCQ_BUILD_PROMPT.md`).", "",
       "| note | questions |", "|---|---|"] + [f"| {k} | {v} |" for k, v in sorted(notes.items())] + [
       "", "## By learning outcome", "", "| LO | note | questions | sources |", "|---|---|---|---|"]
for lo in ALL_LOS:
    ts = by_lo[lo]
    out.append(f"| {lo} | {p2_2026_note(lo) or 'tested in P2 2026'} | {len(ts)} | " + "; ".join(sorted({src_of[t.id] for t in ts})) + " |")
out += ["", "## By chapter", "", "| Ch | topic | questions | L1 / L2 / L3 / L4 / L5 |", "|---|---|---|---|"]
for ch, name in CHAPTERS.items():
    ts = [t for t in OLEVEL if t.chapter == ch]
    lv = [sum(1 for t in ts if t.level == L) for L in range(1, 6)]
    out.append(f"| {ch} | {name} | {len(ts)} | {' / '.join(map(str, lv))} |")
out += ["", "## Every MCQ of the SEAB 6091 specimen Paper 1", "", "| MCQ | trainer item(s) |", "|---|---|"]
for q in SPECIMEN:
    out.append(f"| {q} | {', '.join(sorted(set(cites.get(q, [])))) or 'MISSING'} |")
(ROOT / "OLEVEL_MCQ_COVERAGE.md").write_text("\n".join(out) + "\n", encoding="utf-8")
print("written", len(OLEVEL), "items;", sum(1 for l in out if "MISSING" in l), "missing")
