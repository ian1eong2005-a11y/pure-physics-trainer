"""Student view: one question at a time, scripted hint tutor after a wrong answer, level banners."""
import random
import time

import streamlit as st

from .config import (CATEGORIES, CHAPTERS, DOWN_STREAK, EXPLAIN_LEVEL_NAMES, LEVEL_NAMES, OLEVEL_LEVEL_NAMES, UP_STREAK,
                     WRITTEN_LEVEL_NAMES, p2_2026_note)
from .content import TEMPLATES, chapters_with_content
from .engine import apply_first_attempt, levels_available, repeat_until_correct, select_template
from .marker import mark
from .store import Attempt

LEVEL_NAME_SETS = {"calc": LEVEL_NAMES, "explain": EXPLAIN_LEVEL_NAMES, "written": WRITTEN_LEVEL_NAMES, "olevel": OLEVEL_LEVEL_NAMES}

_rng = random.Random()


def _qs():
    return st.session_state.setdefault("qs", {})


def _pool(cat):
    """Templates to draw from: for the O-level set, optionally only the outcomes the 2026 Paper 2 did not test."""
    if cat == "olevel" and st.session_state.get("olevel_not_p2"):
        return [t for t in TEMPLATES if t.category == "olevel" and p2_2026_note(t.lo)]
    return TEMPLATES


def _serve(store, rec, cat, chapters):
    state = rec.states[cat]
    tpl = select_template(_pool(cat), cat, state.level, chapters, rec.recent[cat], _rng)
    q = tpl.make(_rng.randrange(1_000_000_000))
    rec.recent[cat].append(tpl.id)
    rec.current[cat] = q
    st.session_state["qs"] = dict(
        cat=cat, question=q, level=state.level, phase="answer", wrong=set(), hints_shown=0, hints_used=0,
        formula_shown=False, chat=[], event=None, retry_correct=False, serial=_rng.randrange(1 << 30), served_at=time.time(),
    )
    store.touch(rec.key)
    return st.session_state["qs"]


def _written_feedback(result, first=True):
    lead = "Not quite yet." if first else "Still not there."
    parts = [f"{lead} You have **{result.score}** marking points so far."]
    if result.too_short:
        parts.append("Write a full sentence or two; a word or two is not enough here.")
    if result.hit:
        parts.append("✔ " + "; ".join(result.hit) + ".")
    if result.missed:
        n = len(result.missed)
        parts.append(f"✘ {n} marking point{'s' if n > 1 else ''} still missing. Ask for a hint or the key words.")
    for msg in result.pitfalls:
        parts.append("⚠ " + msg)
    return " ".join(parts)


def _answer(store, rec, response):
    """response: an option letter (MCQ) or the typed answer (written)."""
    qs = _qs()
    q, cat = qs["question"], qs["cat"]
    state = rec.states[cat]
    if q.kind == "written":
        result = mark(response, q.points, q.pitfalls, q.min_points)
        correct, chosen = result.passed, response.strip()[:80]
        qs["mark"], qs["last_answer"] = result, response
    else:
        correct, chosen = response == q.key, response
    first = qs["phase"] == "answer"
    if first:                                                   # first attempt: the only one that counts
        qs["event"] = apply_first_attempt(state, correct)
        store.log_attempt(rec.key, Attempt(time.time(), cat, q.template_id, q.chapter, qs["level"], chosen, q.key, correct, False, 0))
    else:                                                       # retry: no streak credit
        store.log_attempt(rec.key, Attempt(time.time(), cat, q.template_id, q.chapter, qs["level"], chosen, q.key, correct, True, qs["hints_used"]))
    if correct:
        qs["phase"] = "solved"
        qs["retry_correct"] = not first
    else:
        if q.kind == "written":
            msg = _written_feedback(qs["mark"], first)
        else:
            qs["wrong"].add(response)
            msg = (f"Not quite. You chose **{response}**. " if first else f"Still not it. You chose **{response}**. ") + \
                q.misconceptions.get(response, "That value does not follow from the correct method.")
        if first or repeat_until_correct(cat, qs["level"]):
            qs["phase"] = "hints"
            qs["chat"].append(("tutor", msg))
        else:
            qs["phase"] = "revealed"
    store.touch(rec.key)


def _box(colour):
    return f'<span style="display:inline-block;width:16px;height:16px;border-radius:3px;margin:0 2px;vertical-align:middle;background:{colour}"></span>'


def _streak_strip(state):
    boxes = _box("#2e9e5b") * state.correct_streak + _box("#dcdfe4") * max(0, UP_STREAK - state.correct_streak)
    wrong = _box("#d64545") * state.wrong_streak + _box("#dcdfe4") * max(0, DOWN_STREAK - state.wrong_streak)
    return f"Correct in a row: {boxes}&nbsp;&nbsp;&nbsp; Wrong in a row: {wrong}"


def render_student(store, rec):
    store.touch(rec.key)
    ss = st.session_state

    with st.sidebar:
        st.markdown(f"### {rec.name}\n{rec.cls}")
        for cat, label in CATEGORIES.items():
            s = rec.states[cat]
            acc = "–" if s.accuracy is None else f"{round(100 * s.accuracy)}%"
            st.markdown(f"**{label}**: L{s.level} · {s.attempted} done · {acc} correct")
        if st.button("Log out", width="stretch"):
            for k in ("student_key", "qs", "category", "chapters"):
                ss.pop(k, None)
            st.rerun()

    # ---- practice settings
    cat = st.radio("Practise", list(CATEGORIES), format_func=CATEGORIES.get, horizontal=True,
                   index=list(CATEGORIES).index(ss.get("category", "calc")), key="category_radio")
    if cat != ss.get("category"):
        ss["category"] = cat
        ss.pop("qs", None)
    available = chapters_with_content(cat)
    if cat == "olevel":
        only = st.checkbox("Only questions NOT in P2 2026", value=ss.get("olevel_not_p2", False),
                           help="Skip outcomes the 2026 O-Level Paper 2 already tested. Outcomes tested only in the "
                                "either/or Q10 or Q11 are kept.")
        if only != ss.get("olevel_not_p2", False):
            ss["olevel_not_p2"] = only
            ss.pop("qs", None)
        if only:
            available = sorted({t.chapter for t in _pool(cat)})
    with st.expander("Chapters", expanded=False):
        default = [c for c in ss.get("chapters", available) if c in available] or available
        chapters = st.multiselect("Practise these chapters", available, default=default,
                                  format_func=lambda c: f"Ch {c} {CHAPTERS[c]}", key=f"chapters_ms_{cat}")
        missing = [c for c in CHAPTERS if c not in available]
        if missing:
            if cat == "olevel":
                st.caption("No questions NOT in P2 2026 for " + ", ".join(f"Ch {c}" for c in missing)
                           + ": the 2026 O-Level Paper 2 tested every outcome there. Untick the box to practise them.")
            else:
                st.caption("No " + CATEGORIES[cat].lower() + " questions yet for: " + ", ".join(f"Ch {c}" for c in missing) + ".")
    if not chapters:
        chapters = available
    if chapters != ss.get("chapters"):
        ss["chapters"] = chapters
        ss.pop("qs", None)

    state = rec.states[cat]
    names = LEVEL_NAME_SETS[cat]
    st.markdown(f"#### {CATEGORIES[cat]} · Level {state.level}")
    st.caption(names[state.level])
    st.markdown(_streak_strip(state), unsafe_allow_html=True)

    top = max(levels_available(TEMPLATES, cat))
    if state.level > top:
        st.info(f"You have cleared all the {CATEGORIES[cat].lower()} levels available so far (up to L{top}). More are on the way; keep practising at L{top}.")

    qs = ss.get("qs")
    if not qs or qs.get("cat") != cat:
        qs = _serve(store, rec, cat, chapters)
    q = qs["question"]

    # ---- the question
    st.divider()
    st.caption(f"Ch {q.chapter} {CHAPTERS[q.chapter]} · L{q.level}")
    note = p2_2026_note(q.lo) if q.category == "olevel" else None
    if note:
        st.markdown(f":orange-badge[{note}]")
    st.markdown(q.stem)
    if q.figure:
        st.image(q.figure, caption="Fig. 1", width=480)

    phase = qs["phase"]
    answering = phase in ("answer", "retry")
    if q.kind == "written":
        if answering:
            text = st.text_area("Your answer", value=qs.get("last_answer", "") if phase == "retry" else "", height=120,
                                key=f"ans_{qs['serial']}", placeholder="Write one or two sentences in your own words.")
            if st.button("Submit answer", type="primary", width="stretch", key=f"submit_{qs['serial']}"):
                if text.strip():
                    _answer(store, rec, text)
                    st.rerun()
                else:
                    st.warning("Type an answer first.")
        else:
            st.markdown("**Your answer:** " + (qs.get("last_answer") or "").replace("\n", " "))
            res = qs.get("mark")
            if res is not None:
                st.caption(f"Marking points: {res.score}" + (" · " + "; ".join(res.hit) if res.hit else ""))
    else:
        for letter, text in q.options.items():
            disabled = (not answering) or (letter in qs["wrong"])
            label = f"**{letter}**&nbsp;&nbsp; {text}"
            if phase in ("solved", "revealed") and letter == q.key:
                label = f"✅ {label}"
            elif letter in qs["wrong"]:
                label = f"❌ {label}"
            if st.button(label, key=f"opt_{letter}_{qs['serial']}", width="stretch", disabled=disabled):
                _answer(store, rec, letter)
                st.rerun()

    # ---- banners
    if qs["event"] == "up":
        st.success(f"Level up! You are now on **L{state.level}**: {names[state.level]}")
    elif qs["event"] == "down":
        st.warning(f"Back to **L{state.level}** to consolidate. You will move up again after {UP_STREAK} correct in a row.")

    # ---- outcome panels
    if phase == "solved":
        if qs["retry_correct"]:
            st.info("Correct on the second try. Retries do not count towards your streak, so keep going.")
        else:
            st.success("Correct!" if q.kind != "written" else f"Correct! {qs['mark'].score} marking points.")
        with st.expander("Show working" if q.kind != "written" else "Model answer"):
            for line in q.working:
                st.markdown(f"- {line}")
        if st.button("Next question ➜", type="primary", width="stretch", key=f"next_{qs['serial']}"):
            _serve(store, rec, cat, chapters)
            st.rerun()

    elif phase == "revealed":
        if q.kind == "written":
            st.error("Not enough marking points this time. Compare your answer with the model answer below.")
        else:
            st.error(f"The correct answer is **{q.key}**: {q.options[q.key]}")
        st.markdown("**Working**" if q.kind != "written" else "**Model answer**")
        for line in q.working:
            st.markdown(f"- {line}")
        if st.button("Next question ➜", type="primary", width="stretch", key=f"next_{qs['serial']}"):
            _serve(store, rec, cat, chapters)
            st.rerun()

    elif phase == "hints":
        _tutor_panel(store, rec, qs, q)

    elif phase == "retry":
        verb = "Edit your answer and submit again." if q.kind == "written" else "Choose again."
        st.info(verb if not repeat_until_correct(cat, qs["level"]) else verb + " This question comes back until you get it right.")
        with st.expander("Tutor chat"):
            for role, text in qs["chat"]:
                with st.chat_message("assistant" if role == "tutor" else "user"):
                    st.markdown(text)


def _tutor_panel(store, rec, qs, q):
    st.markdown("##### 🧑‍🏫 Tutor")
    for role, text in qs["chat"]:
        with st.chat_message("assistant" if role == "tutor" else "user"):
            st.markdown(text)
    n = qs["hints_shown"]
    c1, c2, c3 = st.columns(3)
    with c1:
        if st.button(f"💡 Give me a hint ({min(n + 1, 3)}/3)", disabled=n >= 3, width="stretch", key=f"hint_{qs['serial']}_{n}"):
            qs["chat"].append(("student", "Give me a hint"))
            qs["chat"].append(("tutor", q.hints[n]))
            qs["hints_shown"] = n + 1
            qs["hints_used"] += 1
            store.touch(rec.key)
            st.rerun()
    with c2:
        is_written = q.kind == "written"
        label = "🔑 Show key words" if is_written else "📐 Show formula"
        if st.button(label, disabled=(not q.formula) or qs["formula_shown"], width="stretch", key=f"formula_{qs['serial']}"):
            qs["chat"].append(("student", "What should I include?" if is_written else "What is the formula?"))
            qs["chat"].append(("tutor", (f"Key ideas to include: **{q.formula}**. Put them into your own sentences." if is_written
                                         else f"Use: **{q.formula}**. Now put the numbers from the question into it.")))
            qs["formula_shown"] = True
            qs["hints_used"] += 1
            store.touch(rec.key)
            st.rerun()
    with c3:
        if st.button("🔁 Try again", type="primary", width="stretch", key=f"retry_{qs['serial']}"):
            if repeat_until_correct(qs["cat"], qs["level"]) and q.kind == "mcq":
                qs["question"] = q.shuffled(_rng)        # same question, new order
                qs["wrong"] = set()
            qs["phase"] = "retry"
            qs["serial"] = _rng.randrange(1 << 30)
            store.touch(rec.key)
            st.rerun()
    if n == 0:
        st.caption("The tutor gives one hint at a time and never the answer. Ask for the "
                   + ("key words if you are not sure what to include." if q.kind == "written" else "formula if you are stuck on the first step."))
