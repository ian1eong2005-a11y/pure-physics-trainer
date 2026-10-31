"""Constants for the Pure Physics (6091) adaptive trainer. Change class lists and rules here only."""

APP_TITLE = "Pure Physics Trainer"
SCHOOL = "Queenstown Secondary School"

# Login dropdown, grouped by level. Add a class by adding its name to the right list.
CLASSES = {
    "Sec 3": ["3SG1"],
    "Sec 4": ["4SG1", "4SG2", "4SG3", "4SG4"],
}
CLASS_LIST = [c for group in CLASSES.values() for c in group]

# SEAB 6091 topic numbering (the same numbering as the school's 2026 content page)
CHAPTERS = {
    1: "Physical Quantities, Units and Measurement",
    2: "Kinematics",
    3: "Dynamics",
    4: "Turning Effects of Forces",
    5: "Pressure",
    6: "Energy",
    7: "Kinetic Particle Model of Matter",
    8: "Thermal Processes",
    9: "Thermal Properties of Matter",
    10: "General Properties of Waves",
    11: "Electromagnetic Spectrum",
    12: "Light",
    13: "Static Electricity",
    14: "Current of Electricity",
    15: "D.C. Circuits",
    16: "Practical Electricity",
    17: "Magnetism",
    18: "Electromagnetism",
    19: "Electromagnetic Induction",
    20: "Radioactivity",
}
SEC3_CHAPTERS = list(range(1, 12))      # taught in Sec 3 (Chapters 1-11); Sec 4 covers 12-20 and revises 1-11

CATEGORIES = {
    "calc": "Calculation",
    "explain": "Explanation",
    "written": "Written answer",
    "olevel": "O level 2026 MCQ practice",
}

# ---- O level 2026 MCQ practice (added 31 Oct 2026 for the 6091 Paper 1 the week after).
# The teacher's mapping of every part of the 2026 6091 Paper 2 to learning outcomes (OLEVEL_MCQ_BUILD_PROMPT.md).
P2_2026_NOT_TESTED = {
    "1a", "1d", "1e", "2a", "2d", "2e", "2f", "2g", "2h", "2i",
    "3a", "3b", "3c", "3d", "3e", "3f", "3i", "3j", "3k", "3l", "3m",
    "4a", "4b", "4c", "4d", "4e", "4f", "5a", "5c", "5f", "5g", "6a", "6d", "6e", "6g", "7c", "7d", "7e", "8b", "8d",
    "9d", "9e", "9f", "9h", "9i", "10a", "10b", "10c", "10d", "10e", "10f", "10g", "10h", "10i", "10j", "11d",
    "12a", "12g", "12h", "12i", "12j", "12k", "13a", "13b", "13c", "13d", "13e", "13f", "13g", "13h", "13i",
    "14a", "14b", "14e", "14f", "14g", "14j", "14k", "15a", "15d", "15e", "15h", "15i", "15j",
    "16a", "16b", "16c", "16g", "16h", "16i", "17a", "17b", "17c", "17d", "17e", "18a", "18e", "18f",
    "19a", "19b", "19c", "20a", "20g", "20h", "20i",
}
P2_2026_Q10_ONLY = {"5b", "5d", "5e", "7a", "7b"}                       # tested only in the either/or Q10
P2_2026_Q11_ONLY = {"20b", "20c", "20d", "20e", "20f", "20j"}           # tested only in the either/or Q11


def p2_2026_note(lo: str):
    """Note shown on an O-level practice question, worked out from its learning outcome; None if Paper 2 tested it."""
    if lo in P2_2026_NOT_TESTED:
        return "NOT in P2 2026"
    if lo in P2_2026_Q10_ONLY:
        return "NOT in P2 2026 Section A (only in either/or Q10)"
    if lo in P2_2026_Q11_ONLY:
        return "NOT in P2 2026 Section A (only in either/or Q11)"
    return None


OLEVEL_LEVEL_NAMES = {
    1: "L1 - recall a definition or fact (SEAB style)",
    2: "L2 - one step: a formula or a rule",
    3: "L3 - read a diagram or graph, or two steps",
    4: "L4 - link two ideas or interpret an experiment",
    5: "L5 - unfamiliar context, or a trap in the data",
}

WRITTEN_LEVEL_NAMES = {
    1: "L1 - state or define in a phrase",
    2: "L2 - state two facts or describe simply",
    3: "L3 - explain with a reason",
    4: "L4 - explain with a chain of reasoning",
    5: "L5 - apply or evaluate in a new situation",
}

LEVEL_NAMES = {
    1: "L1 - one formula, direct substitution",
    2: "L2 - one formula with a conversion, reading or rearrangement",
    3: "L3 - two steps, usually with a figure",
    4: "L4 - graphs and linked formulas",
    5: "L5 - multi-step with a trap or an unfamiliar context",
}
EXPLAIN_LEVEL_NAMES = {
    1: "L1 - recall and definitions",
    2: "L2 - identify and classify",
    3: "L3 - apply a concept",
    4: "L4 - explain with reasoning",
    5: "L5 - evaluate",
}

# Adaptive rules (confirmed by the teacher, 24 Oct 2026; kept for 6091, 25 Oct 2026)
UP_STREAK = 5          # correct in a row at a level -> level + 1
DOWN_STREAK = 3        # wrong in a row at a level -> level - 1
MIN_LEVEL, MAX_LEVEL = 1, 5
START_LEVEL = 1
HISTORY_LEN = 1000     # served template ids remembered per category; a question comes back only after its whole pool has been seen

ONLINE_SECONDS = 120   # "online" on the dashboard if active within this many seconds
DASHBOARD_REFRESH_S = 5

DEFAULT_TEACHER_PASSWORD = "physics"   # used only when no TEACHER_PASSWORD secret / env var is set

G = 10.0               # N/kg, as used in O-level papers
