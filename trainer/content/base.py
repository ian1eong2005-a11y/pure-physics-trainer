"""Shared building blocks for question templates."""
import math
import random
from dataclasses import dataclass, field
from typing import Callable, Dict, List, Optional

LETTERS = "ABCD"


@dataclass
class Question:
    template_id: str
    category: str          # calc | explain
    chapter: int
    level: int
    seed: int
    stem: str              # markdown
    options: Dict[str, str]
    key: str
    working: List[str]
    hints: List[str]
    misconceptions: Dict[str, str]   # wrong letter -> why that answer is tempting
    formula: Optional[str] = None
    figure: Optional[bytes] = None
    lo: str = ""
    kind: str = "mcq"                       # mcq | written
    points: Optional[list] = None           # written: marker.Point list
    pitfalls: Optional[list] = None         # written: marker.Pitfall list
    model_answer: Optional[str] = None
    min_points: Optional[int] = None        # written: how many points pass (default all)
    samples: Optional[tuple] = None         # written: (answers that must pass, answers that must fail) for the tests

    def shuffled(self, rng: random.Random) -> "Question":
        """Same question, options in a new order (used when a recall question is re-served)."""
        if self.kind != "mcq":
            return Question(**self.__dict__)
        items = list(self.options.items())
        rng.shuffle(items)
        new_opts, new_mis, new_key = {}, {}, None
        for new_letter, (old_letter, text) in zip(LETTERS, items):
            new_opts[new_letter] = text
            if old_letter == self.key:
                new_key = new_letter
            elif old_letter in self.misconceptions:
                new_mis[new_letter] = self.misconceptions[old_letter]
        return Question(**{**self.__dict__, "options": new_opts, "key": new_key, "misconceptions": new_mis})


@dataclass
class Template:
    id: str
    category: str
    chapter: int
    level: int
    lo: str
    make: Callable[[int], Question]


TEMPLATES: List[Template] = []


def template(id: str, chapter: int, level: int, lo: str, category: str = "calc"):
    """Register a generator. The wrapped function takes a random.Random and returns a dict with
    stem, options, key, working, hints, misconceptions and optionally formula, figure."""
    def deco(fn):
        def make(seed: int) -> Question:
            rng = random.Random(seed)
            fields = fn(rng)
            return Question(template_id=id, category=category, chapter=chapter, level=level, seed=seed, lo=lo, **fields)
        TEMPLATES.append(Template(id=id, category=category, chapter=chapter, level=level, lo=lo, make=make))
        return make
    return deco


def written(id: str, chapter: int, level: int, lo: str, stem: str, points, model_answer: str, hints, keywords: str,
            pitfalls=(), min_points: Optional[int] = None, figure: Optional[Callable[[], bytes]] = None,
            sample_pass=(), sample_fail=()):
    """Register a written-answer question (fixed text; marked by trainer.marker).
    Teacher rule: no fill-in-the-blank prompts. A hint written with gaps is replaced by a prompt to write a full sentence."""
    clean_hints = [h if "___" not in h else f"Write one or two full sentences of your own that use these ideas: {keywords}." for h in hints]

    def make(seed: int) -> Question:
        return Question(template_id=id, category="written", chapter=chapter, level=level, seed=seed, lo=lo, stem=stem,
                        options={}, key="", working=[f"**Model answer:** {model_answer}"], hints=list(clean_hints), misconceptions={},
                        formula=keywords, figure=figure() if figure else None, kind="written", points=list(points),
                        pitfalls=list(pitfalls), model_answer=model_answer, min_points=min_points,
                        samples=(list(sample_pass), list(sample_fail)))
    TEMPLATES.append(Template(id=id, category="written", chapter=chapter, level=level, lo=lo, make=make))
    return make


# ------------------------------------------------------------------ numbers
_SUP = str.maketrans("0123456789-", "⁰¹²³⁴⁵⁶⁷⁸⁹⁻")


def sci(x: float, sf: int = 3) -> str:
    """Standard form with a real multiplication sign and superscript exponent, e.g. 4.5 × 10⁻⁹."""
    if x == 0:
        return "0"
    e = int(math.floor(math.log10(abs(x))))
    mant = float(f"{x / 10 ** e:.{sf}g}")
    if abs(mant) >= 10:
        mant, e = mant / 10, e + 1
    ms = f"{mant:.6f}".rstrip("0").rstrip(".")
    return f"{ms} × 10{str(e).translate(_SUP)}"


def fmt(x, sf: Optional[int] = 3, dp: Optional[int] = None) -> str:
    """Plain number string: no float noise, 3 s.f. by default, or fixed decimals with dp.
    Very small or very large magnitudes (below 10⁻⁴ or 10⁹ and above) are written in standard form so they never collapse to '0'."""
    if dp is not None:
        return f"{x:.{dp}f}"
    if x != 0 and (abs(x) < 1e-4 or abs(x) >= 1e9):
        return sci(x, sf or 3)
    if sf:
        x = float(f"{x:.{sf}g}")
    s = f"{x:.6f}".rstrip("0").rstrip(".")
    return s if s not in ("", "-0") else "0"


def numeric_options(rng: random.Random, correct: float, wrongs, unit: str = "", sf: int = 3, dp: Optional[int] = None):
    """Four shuffled options for a numeric MCQ.
    wrongs: list of (value, reason). Duplicates (after formatting) and non-positive values are dropped; the list is padded
    with near values if needed. Returns (options dict, key letter, misconceptions dict)."""
    def text(v):
        return f"{fmt(v, sf, dp)} {unit}".strip()

    chosen = [(text(correct), None)]
    seen = {text(correct)}
    for v, reason in wrongs:
        if v is None or not math.isfinite(v) or v <= 0:
            continue
        t = text(v)
        if t in seen:
            continue
        seen.add(t)
        chosen.append((t, reason))
        if len(chosen) == 4:
            break
    for mult in (2, 0.5, 10, 0.1, 1.5, 4, 0.25, 3):
        if len(chosen) == 4:
            break
        t = text(correct * mult)
        if t not in seen:
            seen.add(t)
            chosen.append((t, "This value does not come from the correct formula with the numbers given."))
    rng.shuffle(chosen)
    options, misconceptions, key = {}, {}, None
    for letter, (t, reason) in zip(LETTERS, chosen):
        options[letter] = t
        if reason is None:
            key = letter
        else:
            misconceptions[letter] = reason
    return options, key, misconceptions


def text_options(rng: random.Random, correct: str, wrongs: Dict[str, str]):
    """Four shuffled options for a word-answer MCQ. wrongs: option text -> why it is wrong."""
    items = [(correct, None)] + list(wrongs.items())[:3]
    rng.shuffle(items)
    options, misconceptions, key = {}, {}, None
    for letter, (t, reason) in zip(LETTERS, items):
        options[letter] = t
        if reason is None:
            key = letter
        else:
            misconceptions[letter] = reason
    return options, key, misconceptions


def nice(rng: random.Random, *choices):
    return rng.choice(choices)


# ------------------------------------------------------------------ compact builders (6091 bank extension, 25 Oct 2026)
def mk(rng, answer, wrongs, unit, stem, formula, working, hints, figure=None, sf=3, dp=None):
    """Numeric calculation question in one call: four options from the answer and (value, misconception) pairs."""
    opts, key, mis = numeric_options(rng, answer, wrongs, unit=unit, sf=sf, dp=dp)
    return dict(stem=stem, options=opts, key=key, misconceptions=mis, formula=formula, working=working, hints=hints, figure=figure)


def mkt(rng, correct, wrongs, stem, formula, working, hints, figure=None):
    """Word-answer calculation / data-reading question: wrongs maps option text -> misconception."""
    opts, key, mis = text_options(rng, correct, wrongs)
    return dict(stem=stem, options=opts, key=key, misconceptions=mis, formula=formula, working=working, hints=hints, figure=figure)


def X(id, level, lo, stem, correct, wrongs, hints, figure=None):
    """One explanation MCQ item (fixed text, options shuffled when served). Register a chapter's list with explain_bank()."""
    return dict(id=id, level=level, lo=lo, stem=stem, correct=correct, wrongs=wrongs, hints=hints, figure=figure)


def explain_bank(chapter, items):
    for item in items:
        def make(rng, item=item):
            opts, key, mis = text_options(rng, item["correct"], item["wrongs"])
            fig = item.get("figure")
            hints = [h if "___" not in h else "Rule out the options that contradict what you know, then choose the one that matches the definition exactly." for h in item["hints"]]
            return dict(stem=item["stem"], options=opts, key=key, misconceptions=mis, hints=hints,
                        working=[f"Correct answer: **{item['correct']}**"], formula=None, figure=fig() if fig else None)
        template(item["id"], chapter=chapter, level=item["level"], lo=item["lo"], category="explain")(make)


def explain_mcqs(items, category: str = "explain"):
    """Register fixed-text MCQs for any category (O level 2026 MCQ practice uses category="olevel"). Each item: id, chapter, level,
    lo, stem, correct, wrongs {text: why wrong} (3), hints (3), optional figure (callable returning PNG bytes; the stem must then say
    'Fig. 1'), optional why, optional source (shown under the working, e.g. 'SEAB 6091 specimen paper 2024 MCQ 9')."""
    for item in items:
        def make(rng, item=item):
            opts, key, mis = text_options(rng, item["correct"], item["wrongs"])
            fig = item.get("figure")
            hints = [h if "___" not in h else "Rule out the options that contradict what you know, then choose the one that matches exactly." for h in item["hints"]]
            return dict(stem=item["stem"], options=opts, key=key, misconceptions=mis, hints=hints,
                        working=[f"Correct answer: **{item['correct']}**"] + ([item["why"]] if item.get("why") else [])
                        + ([f"_Adapted from {item['source']}._"] if item.get("source") else []),
                        formula=None, figure=fig() if fig else None)
        template(item["id"], chapter=item["chapter"], level=item["level"], lo=item["lo"], category=category)(make)


def calc_q(rng: random.Random, stem: str, answer: float, wrongs, unit: str, formula: str, working, hints, figure=None,
           sf: Optional[int] = 3, dp: Optional[int] = None):
    """Build the dict a calculation template returns: numeric options with misconception messages, plus the rest."""
    opts, key, mis = numeric_options(rng, answer, wrongs, unit=unit, sf=sf, dp=dp)
    return dict(stem=stem, figure=figure, options=opts, key=key, misconceptions=mis, formula=formula,
                working=list(working), hints=list(hints))


def md_table(headers, rows):
    out = ["| " + " | ".join(headers) + " |", "|" + "|".join(["---"] * len(headers)) + "|"]
    for r in rows:
        out.append("| " + " | ".join(str(c) for c in r) + " |")
    return "\n".join(out)
