# Build the "O level 2026 MCQ practice" category (Pure Physics trainer, 6091)

**Goal.** Add a fourth category, "O level 2026 MCQ practice", to the Pure Physics trainer
(`pure-physics-trainer`, live at https://qtss-pure-physics.streamlit.app): a complete MCQ revision bank for the
6091 Physics Paper 1, covering **every** learning outcome (LO) of Ch 1–20, for the O-Level MCQ paper in the week
after 31 Oct 2026. It mirrors the category of the same name in the G3 Science (Physics) trainer
(`g3-physics-trainer`, rebuilt 31 Oct 2026 from `student-trainer/OLEVEL_MCQ_REBUILD_PROMPT.md`), whose code is the
model for the mechanism.

**1. Cover all LOs.** Every 6091 LO (the trainer's own `lo` tags, e.g. `3j`, `20a`, which follow the 2026 syllabus
`6091_y26_sy.pdf`) that can be tested by an MCQ gets at least one question, two where the sources allow. LOs the
2026 Paper 2 tested stay in: Paper 1 is set on the whole syllabus.

**2. Flag the LOs the 2026 Paper 2 did not test.** The authority is the teacher's mapping of every part of the 2026
6091 Paper 2 to LOs, reproduced at the end of this file:
- LOs not tested at all → every question on them shows the note **"NOT in P2 2026"**;
- LOs tested only in the Section B either/or Q10 (5b, 5d, 5e, 7a, 7b) or only in either/or Q11 (20b–20f, 20j) →
  **"NOT in P2 2026 Section A (only in either/or Q10)"** or **"... Q11"**, so a student who skipped that question
  knows it was not covered for them;
- questions on LOs that Paper 2 did test carry no note.
The note comes from one function of the question's LO (`p2_2026_note(lo)` in `trainer/config.py`, sets
`P2_2026_NOT_TESTED`, `P2_2026_Q10_ONLY`, `P2_2026_Q11_ONLY`), so it can never disagree with the list. Students see it
as an orange badge above the stem and can tick **"Only questions NOT in P2 2026"** to practise just those.

**3. SEAB first, and all of it.** The only official 6091 Paper 1 on file is the **2024 specimen Paper 1**
(`Sec 3 and 4 G3 Pure Physics/key reference documents/specimen paper/6091_y24_sp_1.pdf`, mark scheme
`6091_y24_sm_1.pdf`; 40 MCQs). Every one of its 40 MCQs must be in the bank, cited as
"Adapted from SEAB 6091 specimen paper 2024 MCQ n". The yearly TYS PDFs 2016–2025 (`Sec 4E PURE Resources/TYS/`)
hold Paper 2 only, so they contribute no MCQs; do not search them for Paper 1. Keep the house approach, which
matters more here because the repo is public: same context, skill and answer logic, figures redrawn sharp with the
trainer's drawers, numbers changed slightly where there is a calculation, wording the setter's own. Read each
question's picture, not just its text.

**4. School papers for everything else.** Where an LO is not covered by the specimen, adapt questions from other
schools' 6091 Paper 1 prelims, newest first:
- 2026: QTSS's own prelims, `Sec 4E PURE Resources/Prelims/2026/QTSS 6091 PHY Prelims 2026 P1 QP.docx` with its MS;
- 2025: `Sec 4E PURE Resources/4E Pure OSP 2025/` (about 30 schools) and
  `Documents/QTSS Stuff/4G3 Phy from kez June 26/2025 Phy 4G3 P3 PLM OSP/merged 2025 papers (P1 and P2)/`;
- 2024: `Documents/QTSS Stuff/2024 OSP from QTSS Bank/2024 Pure Phy Prelims/other sch papers - 6092 Phy 2024_Prelim/02. 2024 'O' Physics 4E Written/`
  (about 35 schools, most with mark schemes) and the copies under
  `Sec 3 and 4 G3 Pure Physics/Sample past year papers to extract questions from/`.
Cite the school, year and question ("Adapted from HYSS 2025 prelim MCQ 12"). Spend the extra questions on the
biggest gaps the mapping shows: Ch 4, 10, 13 and 17 (untouched by Paper 2), lenses, the d.c. motor, the a.c.
generator and half-life.

**5. Mechanism: port it from the G3 trainer, do not reinvent it.** From
`Sec 3 and 4 G3 ScPhysics/student-trainer/g3-physics-trainer/`:
- `trainer/config.py`: `CATEGORIES["olevel"]`, `OLEVEL_LEVEL_NAMES` (L1 recall a definition or fact … L5),
  the `P2_2026_*` sets and `p2_2026_note()`; `HISTORY_LEN = 1000` with the shuffled-deck `select_template` in
  `trainer/engine.py` (so the bigger pool does not repeat; the pure trainer still has `RECENT_AVOID = 10`);
- `trainer/ui_student.py`: the badge, the checkbox, `_pool(cat)`, the chapter list limited to chapters with notes
  when the box is ticked;
- `tests/test_olevel.py` (adapted: ALL_LOS = the pure trainer's LO tags, the three TOS sets from the list below,
  every specimen MCQ 1–40 cited, every LO has a question, notes equal the list, every item says "Adapted from");
- `tools/olevel_coverage.py` → `OLEVEL_MCQ_COVERAGE.md` (every specimen MCQ → trainer item; every LO → its
  questions and note; counts by source and note);
- drawers `trainer/sketches3.py` / `sketches4.py` where a figure type is missing from the pure trainer's
  `figs*.py` / `sketches.py`.
Content goes in `trainer/content/olevel_*.py` (`explain_mcqs(items, category="olevel")` for fixed MCQs,
`@template(..., category="olevel")` + `calc_q(...)` for ones with varying numbers), ids `o26_*`, chapters 1–20,
levels 1–5 with the olevel level names, every item with three wrong options each carrying a reason, three hints,
and a "Fig. 1" only when it has a figure.

**6. Checks and release.** Run the full test suite (background; several minutes). Update README.md. Commit
locally. **Pushing redeploys the live app and clears the live dashboard data**, and the pure trainer's rule is
"push once at the end" (teacher, 25 Oct 2026): push when the category is complete, before the students start
revising for the paper, and tell the teacher the dashboard was cleared. Then log in on the live app as a test
student, open the category and confirm the badge, the checkbox and a specimen-adapted question appear; if the
app still shows the old version, reboot it from https://share.streamlit.io (app menu ⋮ → Reboot).

## The teacher's mapping of the 2026 6091 Paper 2 (31 Oct 2026)

Paper 1 is set to cover the whole syllabus; this list decides the notes, never what to leave out.

**Not tested at all in 2026 Paper 2**
- Ch 1 Measurement: 1a, 1d, 1e
- Ch 2 Kinematics: 2a, 2d, 2e, 2f, 2g, 2h, 2i
- Ch 3 Dynamics: 3a, 3b, 3c, 3d, 3e, 3f, 3i, 3j, 3k, 3l, 3m
- Ch 4 Turning Effects: 4a, 4b, 4c, 4d, 4e, 4f (all)
- Ch 5 Pressure: 5a, 5c, 5f, 5g
- Ch 6 Energy: 6a, 6d, 6e, 6g
- Ch 7 Kinetic Particle Model: 7c, 7d, 7e
- Ch 8 Thermal Processes: 8b, 8d
- Ch 9 Thermal Properties: 9d, 9e, 9f, 9h, 9i
- Ch 10 General Properties of Waves: 10a–10j (all)
- Ch 11 EM Spectrum: 11d
- Ch 12 Light: 12a, 12g, 12h, 12i, 12j, 12k
- Ch 13 Static Electricity: 13a–13i (all)
- Ch 14 Current: 14a, 14b, 14e, 14f, 14g, 14j, 14k
- Ch 15 D.C. Circuits: 15a, 15d, 15e, 15h, 15i, 15j
- Ch 16 Practical Electricity: 16a, 16b, 16c, 16g, 16h, 16i
- Ch 17 Magnetism: 17a–17e (all)
- Ch 18 Electromagnetism: 18a, 18e, 18f
- Ch 19 Electromagnetic Induction: 19a, 19b, 19c
- Ch 20 Radioactivity: 20a, 20g, 20h, 20i

**Tested only in either/or Q10:** 5b, 5d, 5e, 7a, 7b
**Tested only in either/or Q11:** 20b, 20c, 20d, 20e, 20f, 20j

Every other LO was tested in Section A or in a compulsory Section B question and carries no note.
