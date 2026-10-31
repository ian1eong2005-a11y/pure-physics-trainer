"""The 'O level 2026 MCQ practice' category (added 31 Oct 2026): every 6091 learning outcome, every MCQ of the SEAB 6091 specimen
Paper 1 (the only official 6091 Paper 1 on file), and a 'NOT in P2 2026' note worked out from each question's learning outcome."""
import re
from collections import Counter

from trainer.config import CATEGORIES, OLEVEL_LEVEL_NAMES, P2_2026_NOT_TESTED, P2_2026_Q10_ONLY, P2_2026_Q11_ONLY, p2_2026_note
from trainer.content import TEMPLATES

OLEVEL = [t for t in TEMPLATES if t.category == "olevel"]

# Every learning outcome of the 2026 6091 syllabus (_2027 tools/knowledge/6091_lo.json)
ALL_LOS = [f"{ch}{letter}" for ch, n in
           [(1, 7), (2, 9), (3, 13), (4, 6), (5, 7), (6, 7), (7, 5), (8, 5), (9, 9), (10, 10), (11, 4), (12, 11), (13, 9), (14, 11),
            (15, 10), (16, 9), (17, 5), (18, 6), (19, 6), (20, 10)]
           for letter in "abcdefghijklm"[:n]]

# The teacher's mapping of the 2026 6091 Paper 2 (OLEVEL_MCQ_BUILD_PROMPT.md, 31 Oct 2026)
TOS_NOT_TESTED = set("1a 1d 1e 2a 2d 2e 2f 2g 2h 2i 3a 3b 3c 3d 3e 3f 3i 3j 3k 3l 3m 4a 4b 4c 4d 4e 4f 5a 5c 5f 5g 6a 6d 6e 6g "
                     "7c 7d 7e 8b 8d 9d 9e 9f 9h 9i 10a 10b 10c 10d 10e 10f 10g 10h 10i 10j 11d 12a 12g 12h 12i 12j 12k "
                     "13a 13b 13c 13d 13e 13f 13g 13h 13i 14a 14b 14e 14f 14g 14j 14k 15a 15d 15e 15h 15i 15j "
                     "16a 16b 16c 16g 16h 16i 17a 17b 17c 17d 17e 18a 18e 18f 19a 19b 19c 20a 20g 20h 20i".split())
TOS_Q10_ONLY = set("5b 5d 5e 7a 7b".split())
TOS_Q11_ONLY = set("20b 20c 20d 20e 20f 20j".split())

SPECIMEN = list(range(1, 41))      # SEAB 6091 specimen Paper 1 (2024): 40 MCQs, all within the syllabus


def cited_specimen():
    """Numbers of the specimen MCQs named in an O-level item's working."""
    out = set()
    for t in OLEVEL:
        text = " ".join(t.make(0).working)
        for m in re.finditer(r"SEAB 6091 specimen paper 2024 MCQ (\d+)((?: and MCQ \d+)*)", text):
            out.add(int(m.group(1)))
            for mm in re.finditer(r"and MCQ (\d+)", m.group(2)):
                out.add(int(mm.group(1)))
    return out


def test_category_registered():
    assert CATEGORIES["olevel"] == "O level 2026 MCQ practice"
    assert set(OLEVEL_LEVEL_NAMES) == {1, 2, 3, 4, 5}


def test_inventory():
    assert len(OLEVEL) >= 160
    assert {t.chapter for t in OLEVEL} == set(range(1, 21))
    assert set(Counter(t.level for t in OLEVEL)) == {1, 2, 3, 4, 5}


def test_every_learning_outcome_has_a_question():
    assert len(ALL_LOS) == 159
    have = {t.lo for t in OLEVEL}
    assert not set(ALL_LOS) - have, f"no O-level question for {sorted(set(ALL_LOS) - have)}"
    assert have <= set(ALL_LOS), f"unknown LO tags {sorted(have - set(ALL_LOS))}"


def test_every_specimen_mcq_is_in():
    missing = [q for q in SPECIMEN if q not in cited_specimen()]
    assert not missing, f"SEAB 6091 specimen Paper 1 MCQs with no O-level item: {missing}"


def test_notes_match_the_teachers_p2_mapping():
    assert P2_2026_NOT_TESTED == TOS_NOT_TESTED and len(TOS_NOT_TESTED) == 105
    assert P2_2026_Q10_ONLY == TOS_Q10_ONLY and P2_2026_Q11_ONLY == TOS_Q11_ONLY
    assert not (TOS_NOT_TESTED & (TOS_Q10_ONLY | TOS_Q11_ONLY)) and not (TOS_Q10_ONLY & TOS_Q11_ONLY)
    assert (TOS_NOT_TESTED | TOS_Q10_ONLY | TOS_Q11_ONLY) <= set(ALL_LOS)
    for lo in ALL_LOS:
        note = p2_2026_note(lo)
        if lo in TOS_NOT_TESTED:
            assert note == "NOT in P2 2026"
        elif lo in TOS_Q10_ONLY | TOS_Q11_ONLY:
            assert note.startswith("NOT in P2 2026 Section A (only in either/or Q1")
        else:
            assert note is None, f"{lo} was tested in Paper 2, so it carries no note"


def test_every_item_cites_its_source():
    for t in OLEVEL:
        q = t.make(0)
        assert any("Adapted from" in w for w in q.working), f"{t.id}: say which past-paper question it was adapted from"
