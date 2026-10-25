# Pure Physics Trainer

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

## Question bank (first round, 25 Oct 2026)

| Ch | Topic | Calculation (L1–L5) | Explanation (L1–L5) | Written (L1–L5) | Total |
|---|---|---|---|---|---|
| 1 | Physical Quantities, Units and Measurement | 11 (2/3/2/2/2) | 10 (4/5/1/0/0) | 25 (5/5/5/5/5) | 46 |
| 2 | Kinematics | 14 (3/1/3/4/3) | 8 (4/3/1/0/0) | 25 (5/5/5/5/5) | 47 |
| 3 | Dynamics | 11 (2/2/2/2/3) | 8 (4/4/0/0/0) | 33 (8/7/6/6/6) | 52 |
| 4 | Turning Effects of Forces | 9 (2/1/2/2/2) | 8 (3/3/2/0/0) | 25 (5/5/5/5/5) | 42 |
| 5 | Pressure | 16 (2/3/4/4/3) | 8 (2/3/3/0/0) | 17 (2/3/4/4/4) | 41 |
| 6 | Energy | 12 (2/3/2/3/2) | 8 (3/4/1/0/0) | 25 (5/5/5/5/5) | 45 |
| 7 | Kinetic Particle Model of Matter | 9 (2/1/2/2/2) | 8 (3/2/3/0/0) | 14 (3/3/3/2/3) | 31 |
| 8 | Thermal Processes | 8 (2/1/2/2/1) | 8 (2/5/1/0/0) | 25 (5/5/5/5/5) | 41 |
| 9 | Thermal Properties of Matter | 10 (2/2/2/2/2) | 8 (2/4/2/0/0) | 11 (2/2/2/3/2) | 29 |
| 10 | General Properties of Waves | 11 (2/3/2/2/2) | 8 (4/3/1/0/0) | 25 (5/5/5/5/5) | 44 |
| 11 | Electromagnetic Spectrum | 8 (1/1/2/3/1) | 8 (4/4/0/0/0) | 25 (5/5/5/5/5) | 41 |
| 12 | Light | 10 (2/2/2/2/2) | 10 (3/2/3/1/1) | 10 (2/2/2/2/2) | 30 |
| 13 | Static Electricity | 9 (2/2/2/2/1) | 10 (3/2/3/1/1) | 10 (2/2/2/2/2) | 29 |
| 14 | Current of Electricity | 11 (2/3/2/2/2) | 10 (3/3/2/1/1) | 10 (2/2/2/2/2) | 31 |
| 15 | D.C. Circuits | 10 (2/2/2/2/2) | 10 (3/3/3/0/1) | 10 (2/2/2/2/2) | 30 |
| 16 | Practical Electricity | 10 (2/2/2/2/2) | 10 (3/3/2/1/1) | 10 (2/2/2/2/2) | 30 |
| 17 | Magnetism | 9 (2/2/2/2/1) | 10 (2/3/2/2/1) | 10 (2/2/2/2/2) | 29 |
| 18 | Electromagnetism | 9 (2/2/2/2/1) | 10 (3/3/2/1/1) | 10 (2/2/2/2/2) | 29 |
| 19 | Electromagnetic Induction | 10 (2/2/2/2/2) | 10 (3/3/2/1/1) | 10 (2/2/2/2/2) | 30 |
| 20 | Radioactivity | 10 (2/2/2/2/2) | 10 (3/3/2/1/1) | 10 (2/2/2/2/2) | 30 |
| | **All** | **207** | **180** | **340** | **727** |

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
