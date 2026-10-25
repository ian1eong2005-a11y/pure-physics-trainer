"""Chapter 20 Radioactivity (6091): nuclide counting, alpha and beta decay equations, half-life from tables and decay curves,
fraction remaining, background correction, identifying radiation from absorption data."""
from .. import figs3
from .base import fmt, md_table, nice, numeric_options, template, text_options

NUCLIDES = [("C", 6, 14), ("Na", 11, 24), ("Co", 27, 60), ("Sr", 38, 90), ("I", 53, 131), ("Cs", 55, 137), ("Ra", 88, 226), ("U", 92, 238), ("Am", 95, 241), ("Pu", 94, 239), ("Th", 90, 234), ("Rn", 86, 222)]


# ---------------------------------------------------------------- L1
@template("c20_neutron_number", chapter=20, level=1, lo="20c")
def neutron_number(rng):
    X, Z, A = rng.choice(NUCLIDES)
    N = A - Z
    opts, key, mis = numeric_options(rng, N, [
        (A, "That is the nucleon (mass) number A: protons + neutrons together."),
        (Z, "That is the proton (atomic) number Z."),
        (A + Z, "Neutrons = A − Z, not A + Z."),
    ], unit="")
    return dict(
        stem=f"Fig. 1 shows the nuclide notation for an isotope of {X}. How many neutrons are in one nucleus of this nuclide?",
        figure=figs3.nuclide(A, Z, X),
        options=opts, key=key, misconceptions=mis,
        formula="nucleon number A (top) = protons + neutrons; proton number Z (bottom); neutrons N = A − Z",
        working=[f"A = {A}, Z = {Z}", f"N = A − Z = {A} − {Z}", f"= **{N}**"],
        hints=["Which number in the notation is the total number of nucleons, and which is the number of protons?", "Top = nucleon number A; bottom = proton number Z.", f"{A} − {Z} = ?"],
    )


@template("c20_half_life_from_table", chapter=20, level=1, lo="20h")
def half_life_from_table(rng):
    T = nice(rng, 2, 3, 4, 5, 6, 8)
    C0 = nice(rng, 800, 960, 640, 1200)
    rows = [(k * T, C0 / 2 ** k) for k in range(5)]
    opts, key, mis = numeric_options(rng, T, [
        (2 * T, "That is the time for the count rate to fall to a QUARTER. The half-life is the time to fall to half."),
        (T / 2, "Read the table again: find the time for the count rate to halve from its starting value."),
        (4 * T, "That is the total time in the table, covering four half-lives."),
    ], unit="min")
    table = md_table(["time / min", "corrected count rate / counts per minute"], [[t, fmt(c)] for t, c in rows])
    return dict(
        stem=f"The table shows how the count rate from a radioactive sample changes with time.\n\n{table}\n\nWhat is the half-life of the sample?",
        options=opts, key=key, misconceptions=mis,
        formula="half-life = time for the count rate (activity) to fall to half its value",
        working=[f"{fmt(C0)} → {fmt(C0 / 2)} counts per minute", f"this takes {T} min", f"half-life = **{T} min**"],
        hints=["What does 'half-life' mean in terms of the count rate?", f"Find when the count rate has fallen from {fmt(C0)} to {fmt(C0 / 2)}.", "Read the time in that row."],
    )


# ---------------------------------------------------------------- L2
@template("c20_alpha_decay_mass_number", chapter=20, level=2, lo="20f")
def alpha_decay_mass_number(rng):
    X, Z, A = rng.choice([n for n in NUCLIDES if n[1] > 80])
    kind = rng.choice(["nucleon", "proton"])
    ans = A - 4 if kind == "nucleon" else Z - 2
    wrongs_vals = [(A - 2 if kind == "nucleon" else Z - 4, "An alpha particle is a helium nucleus: 2 protons and 2 neutrons. A falls by 4 and Z falls by 2."),
                   (A if kind == "nucleon" else Z, "Emitting an alpha particle changes the nucleus: it loses 2 protons and 2 neutrons."),
                   (A - 1 if kind == "nucleon" else Z + 1, "That would fit beta decay (Z rises by 1, A unchanged). Alpha decay removes 4 nucleons, 2 of them protons.")]
    opts, key, mis = numeric_options(rng, ans, wrongs_vals, unit="")
    return dict(
        stem=f"Fig. 1 shows the nuclide {X}-{A}. It decays by emitting an **alpha particle**. What is the **{kind} number** of the new nucleus?",
        figure=figs3.nuclide(A, Z, X, extra="emits an α-particle"),
        options=opts, key=key, misconceptions=mis,
        formula="alpha particle = ⁴₂He: A decreases by 4, Z decreases by 2",
        working=[f"{A} → {A - 4} (nucleon number); {Z} → {Z - 2} (proton number)", f"{kind} number = **{ans}**"],
        hints=["What is an alpha particle made of?", "2 protons + 2 neutrons = 4 nucleons.", f"Take {'4 from A' if kind == 'nucleon' else '2 from Z'}."],
    )


@template("c20_beta_decay_proton_number", chapter=20, level=2, lo="20f")
def beta_decay_proton_number(rng):
    X, Z, A = rng.choice([n for n in NUCLIDES if n[1] < 92])
    kind = rng.choice(["nucleon", "proton"])
    ans = A if kind == "nucleon" else Z + 1
    wrongs_vals = [((A - 1) if kind == "nucleon" else Z - 1, "In beta-minus decay a neutron becomes a proton and an electron is emitted: Z goes UP by 1 and A stays the same."),
                   ((A - 4) if kind == "nucleon" else Z - 2, "That is alpha decay. Beta decay does not change the nucleon number."),
                   ((A + 1) if kind == "nucleon" else Z, "The proton number increases by 1; the nucleon number is unchanged.")]
    opts, key, mis = numeric_options(rng, ans, wrongs_vals, unit="")
    return dict(
        stem=f"Fig. 1 shows the nuclide {X}-{A}. It decays by emitting a **beta particle** (β⁻). What is the **{kind} number** of the new nucleus?",
        figure=figs3.nuclide(A, Z, X, extra="emits a β-particle"),
        options=opts, key=key, misconceptions=mis,
        formula="β⁻ decay: a neutron → a proton + an electron (emitted); A unchanged, Z increases by 1",
        working=[f"A stays {A}; Z goes from {Z} to {Z + 1}", f"{kind} number = **{ans}**"],
        hints=["What happens inside the nucleus in beta-minus decay?", "A neutron changes into a proton; the electron is emitted.", "Total nucleons unchanged; one more proton."],
    )


# ---------------------------------------------------------------- L3
@template("c20_fraction_remaining", chapter=20, level=3, lo="20h")
def fraction_remaining(rng):
    T = nice(rng, 5, 6, 8, 10, 12, 15, 20)
    n = nice(rng, 2, 3, 4)
    m0 = nice(rng, 80, 160, 320, 640, 48, 96)
    t = n * T
    m = m0 / 2 ** n
    unit = rng.choice(["days", "hours", "years"])
    opts, key, mis = numeric_options(rng, m, [
        (m0 / (2 * n), f"You divided by 2 × {n}. Each half-life HALVES what is left, so after {n} half-lives the mass is divided by 2^{n} = {2 ** n}."),
        (m0 - m, "That is the mass that has DECAYED. The question asks how much remains."),
        (m0 / 2, "That is after ONE half-life only."),
    ], unit="g", sf=3)
    table = md_table(["quantity", "value"], [["initial mass of the isotope", f"{m0} g"], ["half-life", f"{T} {unit}"], ["time elapsed", f"{t} {unit}"]])
    return dict(
        stem=f"A sample contains a radioactive isotope.\n\n{table}\n\nWhat mass of the isotope remains undecayed?",
        options=opts, key=key, misconceptions=mis,
        formula="number of half-lives = time ÷ half-life; remaining = initial ÷ 2ⁿ",
        working=[f"n = {t} ÷ {T} = {n} half-lives", f"remaining = {m0} ÷ 2^{n} = {m0} ÷ {2 ** n}", f"= **{fmt(m, sf=3)} g**"],
        hints=["How many half-lives have passed?", "Each half-life halves the amount left.", f"Halve {m0} g {n} times."],
    )


@template("c20_half_life_from_curve", chapter=20, level=3, lo="20h")
def half_life_from_curve(rng):
    T = nice(rng, 2, 4, 5, 8, 10)
    n0 = nice(rng, 400, 600, 800, 1000)
    opts, key, mis = numeric_options(rng, T, [
        (2 * T, "That is the time for the count rate to fall to a quarter of its start value."),
        (T / 2, "Read where the curve reaches HALF of its initial value."),
        (n0 / 2 / 10, "That is a count-rate reading, not a time."),
    ], unit="min", sf=3)
    return dict(
        stem=f"Fig. 1 shows the decay curve for a radioactive sample. Use the graph to find the half-life of the sample.",
        figure=figs3.decay_curve(n0, T, 5 * T),
        options=opts, key=key, misconceptions=mis,
        formula="half-life = time for the count rate to fall to half (from any starting point on the curve)",
        working=[f"initial count rate = {n0}; half of it = {n0 // 2}", f"the curve reaches {n0 // 2} at t = {T} min", f"half-life = **{T} min**"],
        hints=["Read the starting count rate and halve it.", f"Find {n0 // 2} on the vertical axis, go across to the curve, then down to the time axis.", "Check: from that point the count rate halves again after the same time."],
    )


# ---------------------------------------------------------------- L4
@template("c20_background_correction", chapter=20, level=4, lo="20g")
def background_correction(rng):
    bg = nice(rng, 20, 24, 30, 36)
    T = nice(rng, 2, 3, 4, 5)
    c0 = nice(rng, 400, 480, 640, 800)
    k = rng.choice([1, 2])
    measured_t = c0 / 2 ** k + bg
    ans = c0 / 2 ** k
    opts, key, mis = numeric_options(rng, ans, [
        (measured_t, "That is the MEASURED count rate, which includes background. Subtract the background first."),
        (measured_t + bg, "You added the background. Background radiation is always present, so it must be SUBTRACTED."),
        (c0 / 2 ** (k + 1), "That would be one more half-life than has passed."),
    ], unit="counts/min", sf=3)
    table = md_table(["time / min", "measured count rate / counts per minute"], [[0, fmt(c0 + bg)], [k * T, fmt(measured_t)]])
    return dict(
        stem=f"Fig. 1 shows a source, an absorber position and a GM tube. With no source present the counter records a background count rate of **{bg} counts/min**.\n\n{table}\n\nWhat is the corrected count rate due to the source at {k * T} min?",
        figure=figs3.detector_setup([f"background = {bg} counts/min"]),
        options=opts, key=key, misconceptions=mis,
        formula="corrected count rate = measured count rate − background count rate",
        working=[f"measured at {k * T} min = {fmt(measured_t)}", f"corrected = {fmt(measured_t)} − {bg}", f"= **{fmt(ans, sf=3)} counts/min**"],
        hints=["The counter picks up background radiation as well as radiation from the source.", "To find the source's contribution, take the background away.", f"{fmt(measured_t)} − {bg}."],
    )


@template("c20_identify_radiation", chapter=20, level=4, lo="20e")
def identify_radiation(rng):
    kind = rng.choice(["alpha", "beta", "gamma"])
    bg = 20
    base = nice(rng, 500, 600, 800)
    data = {"alpha": (base, bg, bg, bg), "beta": (base, base, bg, bg), "gamma": (base, base, round(base * 0.9), round(base * 0.5))}[kind]
    absorbers = ["none", "paper", "5 mm aluminium", "2 cm lead"]
    names = {"alpha": "alpha (α) only", "beta": "beta (β) only", "gamma": "gamma (γ) only"}
    ans = names[kind]
    wrongs = {v: {"alpha (α) only": "Alpha is stopped by paper: the count would drop to background as soon as paper is added.",
                  "beta (β) only": "Beta passes through paper but is stopped by a few mm of aluminium.",
                  "gamma (γ) only": "Gamma passes through paper and aluminium, and is only reduced by thick lead."}[v] for k2, v in names.items() if k2 != kind}
    wrongs["a mixture of alpha and beta"] = "A mixture would show a DROP at paper (alpha removed) and another drop at aluminium (beta removed)."
    opts, key, mis = text_options(rng, ans, dict(list(wrongs.items())[:3]))
    table = md_table(["absorber", "count rate / counts per minute"], [[a, c] for a, c in zip(absorbers, data)])
    return dict(
        stem=f"Fig. 1 shows how different absorbers are placed between a source and a GM tube. The background count rate is {bg} counts per minute.\n\n{table}\n\nWhat radiation does the source emit?",
        figure=figs3.penetration(),
        options=opts, key=key, misconceptions=mis,
        formula="α stopped by paper; β stopped by a few mm of aluminium; γ only reduced by thick lead",
        working=["look for the absorber at which the count rate falls to background", {"alpha": "falls to background with paper → alpha", "beta": "unchanged with paper, background with aluminium → beta", "gamma": "unchanged by paper and aluminium, reduced by lead → gamma"}[kind], f"**{ans}**"],
        hints=["Remember which absorber stops each type of radiation.", "Compare each count rate with the one before it and with the background.", "Where does the count rate drop, and to what?"],
    )


# ---------------------------------------------------------------- L5
@template("c20_time_to_fall", chapter=20, level=5, lo="20h")
def time_to_fall(rng):
    T = nice(rng, 6, 8, 12, 15, 24)
    n = nice(rng, 3, 4, 5)
    a0 = nice(rng, 1600, 3200, 6400, 4800)
    a1 = a0 / 2 ** n
    t = n * T
    unit = rng.choice(["hours", "days"])
    opts, key, mis = numeric_options(rng, t, [
        ((n - 1) * T, f"Count the halvings carefully: {fmt(a0)} → {fmt(a1)} is {n} halvings, not {n - 1}."),
        (T * a0 / a1 / 2, "Activity does not fall in a straight line: count how many halvings are needed, each taking one half-life."),
        (T * n * 2, "Each halving takes ONE half-life."),
    ], unit=unit, sf=3)
    table = md_table(["quantity", "value"], [["initial activity", f"{fmt(a0)} Bq"], ["activity at which the source is replaced", f"{fmt(a1)} Bq"], ["half-life", f"{T} {unit}"]])
    return dict(
        stem=f"A hospital source must be replaced when its activity has fallen to a set value.\n\n{table}\n\nHow long after delivery must the source be replaced?",
        options=opts, key=key, misconceptions=mis,
        formula="count the halvings from the initial to the final activity; time = number of half-lives × half-life",
        working=[" → ".join(fmt(a0 / 2 ** k) for k in range(n + 1)) + f" Bq ({n} halvings)", f"time = {n} × {T}", f"= **{t} {unit}**"],
        hints=["Keep halving the activity until you reach the replacement value.", "Count how many halvings that took.", f"Multiply by the half-life ({T} {unit})."],
    )


@template("c20_daughter_after_chain", chapter=20, level=5, lo="20f")
def daughter_after_chain(rng):
    X, Z, A = rng.choice([("U", 92, 238), ("Th", 90, 232), ("Ra", 88, 226), ("Rn", 86, 222)])
    na = rng.choice([1, 2])
    nb = rng.choice([1, 2])
    kind = rng.choice(["proton", "nucleon"])
    Zf, Af = Z - 2 * na + nb, A - 4 * na
    ans = Zf if kind == "proton" else Af
    wrongs_vals = [(Z - 2 * na - nb if kind == "proton" else A - 4 * na - nb, "Beta decay INCREASES the proton number by 1 (and leaves the nucleon number unchanged)."),
                   (Z - 2 * na if kind == "proton" else A - 4 * na + nb, "You left out the effect of the beta decays." if kind == "proton" else "Beta decay does not change the nucleon number."),
                   (Z - na + nb if kind == "proton" else A - 2 * na, "Each alpha decay reduces Z by 2 and A by 4.")]
    opts, key, mis = numeric_options(rng, ans, wrongs_vals, unit="")
    return dict(
        stem=f"Fig. 1 shows the nuclide {X}-{A}. It decays by emitting **{na} alpha particle{'s' if na > 1 else ''}** followed by **{nb} beta particle{'s' if nb > 1 else ''}**. What is the **{kind} number** of the final nucleus?",
        figure=figs3.nuclide(A, Z, X, extra=f"{na} α then {nb} β"),
        options=opts, key=key, misconceptions=mis,
        formula="each α: A − 4, Z − 2; each β⁻: A unchanged, Z + 1",
        working=[f"after {na} α: A = {A} − {4 * na} = {A - 4 * na}, Z = {Z} − {2 * na} = {Z - 2 * na}", f"after {nb} β: A = {A - 4 * na}, Z = {Z - 2 * na} + {nb} = {Zf}", f"{kind} number = **{ans}**"],
        hints=["Deal with the alpha decays first, then the beta decays.", "Alpha: A − 4, Z − 2 each time. Beta: Z + 1 each time, A unchanged.", f"Apply {na} alpha change{'s' if na > 1 else ''} and {nb} beta change{'s' if nb > 1 else ''}."],
    )
