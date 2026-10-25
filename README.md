# Pure Physics Trainer

**Live app:** https://qtss-pure-physics.streamlit.app  (teacher dashboard: add `?teacher=1` or use the sidebar)

Adaptive self-study trainer for O-Level Pure Physics (SEAB 6091), all 20 topics, numbered as in the syllabus and the school's
content page. Streamlit app, no database. Built from the G3 Physics Trainer (same engine, store, marker and UIs); content
re-mapped to 6091 and extended to Chapters 12–20.

## How it works

- Students log in with **name + class** (no password). Teacher view is password protected.
- Three categories: **Calculation** (parametrised templates, numbers change every time, every one with a diagram or data table
  drawn from the question's own numbers), **Explanation** (fixed MCQs, options reshuffled on every serve) and **Written answer**
  (marked by meaning, not word for word: `trainer/marker.py`, no LLM). For the descriptive chapters (7, 8, 11, 13, 17, 18, 20)
  the Calculation category holds data-reading questions (tables, graphs, rule-based directions), as agreed with the teacher.
- **5 correct in a row → level up. 3 wrong in a row → level down.** Everyone starts at L1. Only the first attempt counts.
- A wrong answer opens the scripted **tutor**: a message about the chosen option, up to 3 hints, the formula / key words on request,
  then one retry (correct retries never count towards the streak). L1 explanation and written questions come back until correct.
- **Teacher dashboard** (sidebar → Teacher, or `?teacher=1`): who is online, levels, streaks, accuracy, hints, last 20 attempts,
  reset / clear / CSV. Refreshes every 5 s. Data lives in memory only and disappears when the app restarts.

## Levels

| | Calculation | Explanation | Written answer |
|---|---|---|---|
| L1 | one formula, direct substitution | recall and definitions | state or define in a phrase |
| L2 | one formula with a conversion, reading or rearrangement | identify and classify | two facts or a simple description |
| L3 | two steps, usually with a figure | apply a concept | explain with a reason |
| L4 | graphs and linked formulas | explain with reasoning | explain with a chain of reasoning |
| L5 | multi-step with a trap or an unfamiliar context | evaluate | apply or evaluate in a new situation |

## Question bank (extended 25 Oct 2026)

Every chapter has at least 10 questions per level in each category, covering at least 3 learning outcomes, with every learning outcome in a pool appearing at least twice (`tests/test_content.py::test_pool_coverage`, survey with `python devtools/gaps.py <chapter>`). Questions are adapted from the question bank, never copied.

| Ch | Topic | Calculation (L1–L5) | Explanation (L1–L5) | Written (L1–L5) | Total |
|---|---|---|---|---|---|
| 1 | Physical Quantities, Units and Measurement | 51 (11/10/10/10/10) | 51 (10/10/11/10/10) | 51 (10/10/10/10/11) | 153 |
| 2 | Kinematics | 52 (10/10/11/10/11) | 53 (12/11/10/10/10) | 50 (10/10/10/10/10) | 155 |
| 3 | Dynamics | 53 (12/10/10/10/11) | 50 (10/10/10/10/10) | 56 (14/11/11/10/10) | 159 |
| 4 | Turning Effects of Forces | 51 (11/10/10/10/10) | 59 (13/13/12/11/10) | 50 (10/10/10/10/10) | 160 |
| 5 | Pressure | 50 (10/10/10/10/10) | 53 (11/11/11/10/10) | 50 (10/10/10/10/10) | 153 |
| 6 | Energy | 51 (10/10/10/10/11) | 57 (13/13/11/10/10) | 50 (10/10/10/10/10) | 158 |
| 7 | Kinetic Particle Model of Matter | 51 (10/10/11/10/10) | 55 (13/12/10/10/10) | 50 (10/10/10/10/10) | 156 |
| 8 | Thermal Processes | 52 (10/10/11/10/11) | 52 (12/10/10/10/10) | 50 (10/10/10/10/10) | 154 |
| 9 | Thermal Properties of Matter | 50 (10/10/10/10/10) | 54 (12/10/12/10/10) | 50 (10/10/10/10/10) | 154 |
| 10 | General Properties of Waves | 51 (10/10/10/11/10) | 54 (14/10/10/10/10) | 50 (10/10/10/10/10) | 155 |
| 11 | Electromagnetic Spectrum | 50 (10/10/10/10/10) | 50 (10/10/10/10/10) | 50 (10/10/10/10/10) | 150 |
| 12 | Light | 55 (11/10/11/11/12) | 51 (10/10/10/10/11) | 50 (10/10/10/10/10) | 156 |
| 13 | Static Electricity | 51 (10/10/11/10/10) | 51 (10/10/10/10/11) | 50 (10/10/10/10/10) | 152 |
| 14 | Current of Electricity | 53 (10/12/11/10/10) | 50 (10/10/10/10/10) | 50 (10/10/10/10/10) | 153 |
| 15 | D.C. Circuits | 52 (10/10/10/11/11) | 51 (10/10/11/10/10) | 51 (10/10/10/10/11) | 154 |
| 16 | Practical Electricity | 55 (10/10/11/12/12) | 51 (10/10/10/10/11) | 50 (10/10/10/10/10) | 156 |
| 17 | Magnetism | 52 (10/10/12/10/10) | 52 (10/10/10/12/10) | 52 (10/10/12/10/10) | 156 |
| 18 | Electromagnetism | 56 (11/11/12/12/10) | 50 (10/10/10/10/10) | 51 (10/10/10/10/11) | 157 |
| 19 | Electromagnetic Induction | 50 (10/10/10/10/10) | 50 (10/10/10/10/10) | 50 (10/10/10/10/10) | 150 |
| 20 | Radioactivity | 50 (10/10/10/10/10) | 50 (10/10/10/10/10) | 50 (10/10/10/10/10) | 150 |
| | **All** | **1036** | **1044** | **1011** | **3091** |

## Run locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

Default local teacher password is `physics`. Set `TEACHER_PASSWORD` as an environment variable or in `.streamlit/secrets.toml` to change it.

## Deploy on Streamlit Community Cloud

1. share.streamlit.io → **Create app** → repo `ian1eong2005-a11y/pure-physics-trainer`, branch `main`, main file `app.py`.
2. Advanced settings → **Secrets**: `TEACHER_PASSWORD = "choose-something"`.
3. Deploy. Every push to `main` redeploys automatically; live data is cleared on each redeploy.

## Tests

```bash
python -m pytest -q
```

`tests/test_content.py` builds every template with 20 seeds (four distinct options, key present, a misconception message for every
wrong option, three hints, a PNG figure whenever the stem says "Fig. 1", numbers that vary) and checks every chapter meets the agreed
minimum (8 calculation, 8 explanation, 10 written). Written questions must pass their own model answer and sample answers.

## Adding a question

- **Calculation**: one template = one function in `trainer/content/calc_chN.py`. Copy any existing one:

```python
@template("c15_my_question", chapter=15, level=2, lo="15f")
def my_question(rng):
    r1, r2 = nice(rng, 2, 4, 6), nice(rng, 3, 6, 12)
    ...
    opts, key, mis = numeric_options(rng, answer, [(wrong1, "why a student gets this"), ...], unit="Ω")
    return dict(stem=..., options=opts, key=key, misconceptions=mis, formula=..., working=[...], hints=[h1, h2, h3], figure=figs3.circuit(...))
```

- **Explanation**: add a dict to `RECALL3` (Ch 1–11) or `RECALL4` (Ch 12–20) in `trainer/content/recall3.py` / `recall4.py`.
- **Written answer**: add a `written(...)` call to `trainer/content/written_chN.py` with marking points, pitfalls, a model answer
  and sample pass/fail answers.
- Register any new module in `trainer/content/__init__.py`, then run the tests.

## Adding a class

Edit the `CLASSES` dict at the top of `trainer/config.py`, e.g. `"Sec 4": ["4SG1", "4SG2"]`.

## Layout

```
app.py                      entry point: login, routing
trainer/config.py           classes, chapters (6091 numbering), rules (5 up / 3 down), refresh interval
trainer/engine.py           adaptive rules (pure Python)
trainer/store.py            in-memory live store shared by all sessions
trainer/marker.py           meaning-based marker for written answers
trainer/figs.py             instrument and graph drawers (carried over)
trainer/sketches.py         scene sketches for Ch 2-11 (carried over)
trainer/figs2.py            digital instruments, vectors, liquid pressure, thermal set-ups, ray optics and lenses
trainer/figs3.py            electric fields, circuits, I-V graphs, plugs, magnets, electromagnetism, induction, radioactivity
trainer/content/            question templates: calc_ch*.py, recall*.py, written_ch*.py
trainer/ui_student.py       student screen + tutor panel
trainer/ui_teacher.py       live dashboard
tests/                      pytest
```
