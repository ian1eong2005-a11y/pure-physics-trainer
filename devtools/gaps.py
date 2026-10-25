"""Coverage report: for every chapter, category and level, how many questions there are, how many distinct learning outcomes,
and which outcomes appear only once. Rule (teacher, 25 Oct 2026): each pool has >= 10 questions, >= 3 different LOs
(variety), and every LO in the pool appears at least twice (reinforcement).

    python devtools/gaps.py            # all chapters
    python devtools/gaps.py 12 13      # some chapters
"""
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from trainer.config import CHAPTERS  # noqa: E402
from trainer.content import TEMPLATES  # noqa: E402

TARGET, MIN_LOS = 10, 3
CATS = ("calc", "explain", "written")


def pool(ch, cat, lv):
    return [t for t in TEMPLATES if t.chapter == ch and t.category == cat and t.level == lv]


def report(chs):
    need_total = 0
    for ch in chs:
        lines = []
        for cat in CATS:
            for lv in range(1, 6):
                p = pool(ch, cat, lv)
                c = Counter(t.lo for t in p)
                singles = sorted(k for k, v in c.items() if v < 2)
                short = max(0, TARGET - len(p))
                ok = not short and len(c) >= MIN_LOS and not singles
                if not ok:
                    need = max(short, len(singles))
                    need_total += need
                    lines.append(f"  {cat:7s} L{lv}: {len(p):2d} q, LOs {dict(sorted(c.items()))}"
                                 + (f"  need +{short}" if short else "") + (f"  singles {singles}" if singles else "")
                                 + (f"  only {len(c)} LOs" if len(c) < MIN_LOS else ""))
        print(f"Ch {ch} {CHAPTERS[ch]}: {'OK' if not lines else ''}")
        for l in lines:
            print(l)
    print(f"-- about {need_total} questions still to add")


if __name__ == "__main__":
    report([int(a) for a in sys.argv[1:]] or list(CHAPTERS))
