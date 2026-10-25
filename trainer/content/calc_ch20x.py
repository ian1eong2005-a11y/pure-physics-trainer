"""Chapter 20 Radioactivity (6091) bank extension: nucleon counting, isotopes, decay equations, absorption and deflection data,
background correction, half-life, uses and safety, fission and fusion equations; 10 per level, each LO at least twice. Contexts adapted
from the question bank (SEAB 2016-2025: GM tube readings with absorbers, decay curves, tracers, thickness gauges, carbon dating,
fission of uranium-235, fusion of hydrogen isotopes; school papers 2024-2025)."""
from .. import figs3
from .base import fmt, md_table, mk, mkt, nice, template

NUCLIDES = [("C", 6, 14), ("Na", 11, 24), ("Co", 27, 60), ("Sr", 38, 90), ("I", 53, 131), ("Cs", 55, 137), ("Ra", 88, 226), ("U", 92, 238), ("Am", 95, 241), ("Th", 90, 234), ("Rn", 86, 222)]
SUP = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")
SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")


def nuc(A, Z, X):
    return f"{str(A).translate(SUP)}{str(Z).translate(SUB)}{X}"


# ================================================================== L1
@template("c20x_nucleons_atom", chapter=20, level=1, lo="20a")
def nucleons_atom(rng):
    Z = rng.randint(2, 5)
    N = Z + rng.choice([1, 2])
    return mk(rng, Z + N, [(Z, "That counts the protons only. Nucleons are protons AND neutrons."), (N, "That counts the neutrons only."),
                           (2 * Z + N, "Electrons are not nucleons: they are outside the nucleus.")],
              "", "Fig. 1 shows a model of an atom. The nucleus contains protons (+) and neutrons. How many nucleons are in the nucleus?",
              "nucleon number = protons + neutrons", [f"protons = {Z}, neutrons = {N}", f"nucleons = {Z} + {N} = **{Z + N}**"],
              ["What are nucleons?", "The particles in the nucleus.", "Count the protons and neutrons."],
              figure=figs3.atom_diagram(Z, N))


@template("c20x_electrons_neutral", chapter=20, level=1, lo="20a")
def electrons_neutral(rng):
    X, Z, A = rng.choice(NUCLIDES)
    N = A - Z
    table = md_table(["particle in the nucleus", "number"], [["protons", Z], ["neutrons", N]])
    return mk(rng, Z, [(N, "Neutrons are uncharged; the electrons balance the protons."), (A, "That is the number of nucleons."),
                       (2 * Z, "Each proton (+1) is balanced by ONE electron (−1).")],
              "", f"The table describes the nucleus of a neutral atom of {X}.\n\n{table}\n\nHow many electrons does the atom have?",
              "neutral atom: number of electrons = number of protons", [f"protons = {Z}", f"electrons = **{Z}**"],
              ["What makes an atom neutral?", "Equal positive and negative charge.", "Electrons = protons."])


@template("c20x_proton_from_table", chapter=20, level=1, lo="20b")
def proton_from_table(rng):
    X, Z, A = rng.choice(NUCLIDES)
    N = A - Z
    table = md_table(["quantity", "value"], [["nucleon number", A], ["number of neutrons", N]])
    return mk(rng, Z, [(A, "That is the nucleon number: protons + neutrons."), (N, "That is the number of neutrons."),
                       (A + N, "Proton number = nucleon number − neutrons.")],
              "", f"The table gives data for a nucleus of {X}.\n\n{table}\n\nWhat is its proton number?",
              "proton number Z = nucleon number A − neutron number N", [f"Z = {A} − {N}", f"= **{Z}**"],
              ["What does the nucleon number count?", "Protons and neutrons together.", "Subtract the neutrons."])


@template("c20x_isotope_pick", chapter=20, level=1, lo="20b")
def isotope_pick(rng):
    X, Z, A = rng.choice(NUCLIDES)
    labels = ["P", "Q", "R", "S"]
    rng.shuffle(labels)
    d = rng.choice([1, 2])
    rows = [(labels[0], A + d, Z), (labels[1], A, Z + 1), (labels[2], A + 1, Z + 1), (labels[3], A + d + 3, Z + 2)]
    ans = labels[0]
    wrongs = {labels[1]: "Same nucleon number but a different proton number: a different element.",
              labels[2]: "A different proton number means a different element, even if the neutron number is the same.",
              labels[3]: "Both numbers differ, so it is a different element."}
    table = md_table(["nucleus", "nucleon number", "proton number"], [[f"{X}-{A} (given)", A, Z]] + sorted([list(r) for r in rows]))
    return mkt(rng, ans, wrongs, f"The table gives data for a nucleus of {X}-{A} and four other nuclei.\n\n{table}\n\nWhich nucleus is an isotope of {X}-{A}?",
               "isotopes: same proton number, different nucleon (neutron) number", [f"{ans}: proton number {Z} (same), nucleon number {A + d} (different) → **{ans}**"],
               ["What must isotopes have in common?", "The same proton number.", "And what must differ?"])


@template("c20x_nucleon_read", chapter=20, level=1, lo="20c")
def nucleon_read(rng):
    X, Z, A = rng.choice(NUCLIDES)
    return mk(rng, A, [(Z, "That is the proton number (bottom)."), (A - Z, "That is the number of neutrons."), (A + Z, "The top number already counts all the nucleons.")],
              "", f"Fig. 1 shows the nuclide notation for a nucleus of {X}. How many nucleons does the nucleus contain?",
              "top number = nucleon number A", [f"top number = **{A}**"],
              ["Which number is on top?", "The nucleon number.", "It counts protons and neutrons."],
              figure=figs3.nuclide(A, Z, X))


@template("c20x_one_half_life", chapter=20, level=1, lo="20h")
def one_half_life(rng):
    C = nice(rng, 400, 600, 800, 1000, 1200)
    T = nice(rng, 3, 5, 8, 12)
    table = md_table(["quantity", "value"], [["initial count rate", f"{C} counts/min"], ["half-life", f"{T} hours"], ["time passed", f"{T} hours"]])
    return mk(rng, C / 2, [(C / 4, "That is after TWO half-lives."), (C, "The source decays, so the count rate falls."), (C - T, "The count rate halves; you do not subtract the time.")],
              "counts/min", f"A radioactive source is measured (background already subtracted).\n\n{table}\n\nWhat is the count rate now?",
              "after one half-life the count rate halves", [f"{C} ÷ 2 = **{fmt(C / 2)} counts/min**"],
              ["How many half-lives have passed?", "One.", "Halve the count rate."])


@template("c20x_absorber_stops", chapter=20, level=1, lo="20e")
def absorber_stops(rng):
    case = rng.choice(["paper", "aluminium", "lead"])
    q = {"paper": "is stopped by a sheet of paper", "aluminium": "passes through paper but is stopped by a few millimetres of aluminium",
         "lead": "passes through aluminium and is only reduced by several centimetres of lead"}[case]
    ans = {"paper": "alpha", "aluminium": "beta", "lead": "gamma"}[case]
    wrongs = {r: {"alpha": "Alpha is stopped by paper.", "beta": "Beta passes through paper but is stopped by a few mm of aluminium.",
                  "gamma": "Gamma passes through paper and aluminium."}[r] for r in ("alpha", "beta", "gamma") if r != ans}
    wrongs["all three"] = "The three radiations have very different penetrating powers."
    return mkt(rng, ans, wrongs, f"Fig. 1 shows the absorbers that stop the three types of radiation. Which radiation {q}?",
               "α: paper; β: a few mm aluminium; γ: reduced by thick lead", [f"**{ans}**"],
               ["Which is the least penetrating?", "Alpha, then beta, then gamma.", "Match the absorber."],
               figure=figs3.penetration())


@template("c20x_charge_pick", chapter=20, level=1, lo="20e")
def charge_pick(rng):
    charge = rng.choice(["+2", "−1", "0"])
    ans = {"+2": "alpha", "−1": "beta", "0": "gamma"}[charge]
    wrongs = {"alpha": "An alpha particle (helium nucleus) has a charge of +2.", "beta": "A beta particle (electron) has a charge of −1.", "gamma": "Gamma is an electromagnetic wave: no charge."}
    wrongs = {k: v for k, v in wrongs.items() if k != ans}
    wrongs["none of them"] = "One of the three has exactly this charge."
    table = md_table(["radiation", "what it is"], [["alpha", "a helium nucleus (2 protons, 2 neutrons)"], ["beta", "a fast-moving electron"], ["gamma", "an electromagnetic wave"]])
    return mkt(rng, ans, wrongs, f"The table describes the three types of radiation.\n\n{table}\n\nWhich radiation has a charge of **{charge}**?",
               "α: +2 (2 protons); β: −1 (electron); γ: 0 (EM wave)", [f"charge {charge} → **{ans}**"],
               ["What charge does each particle carry?", "Protons +1, electrons −1, waves 0.", "Match the charge."])


# ================================================================== L2
@template("c20x_isotope_neutron_diff", chapter=20, level=2, lo="20b")
def isotope_neutron_diff(rng):
    X, Z, A1, A2 = rng.choice([("C", 6, 12, 14), ("U", 92, 235, 238), ("Co", 27, 59, 60), ("I", 53, 127, 131), ("Cl", 17, 35, 37)])
    dA = A2 - A1
    table = md_table(["isotope", "nucleon number", "proton number"], [[f"{X}-{A1}", A1, Z], [f"{X}-{A2}", A2, Z]])
    return mk(rng, dA, [(A2, "That is the nucleon number of the heavier isotope."), (A2 - Z, "That is the number of neutrons in the heavier isotope."),
                        (2 * dA, "The proton numbers are equal, so the whole difference in nucleons is neutrons.")],
              "", f"The table gives data for two isotopes of {X}.\n\n{table}\n\nHow many more neutrons does {X}-{A2} have than {X}-{A1}?",
              "isotopes have the same protons, so the difference in A is all neutrons", [f"{A2} − {A1} = **{dA}**"],
              ["What is the same for isotopes?", "The proton number.", "So the extra nucleons are neutrons."])


@template("c20x_isotope_protons", chapter=20, level=2, lo="20b")
def isotope_protons(rng):
    X, Z, A1, A2 = rng.choice([("C", 6, 12, 14), ("U", 92, 235, 238), ("Co", 27, 59, 60), ("I", 53, 127, 131), ("Cl", 17, 35, 37)])
    table = md_table(["isotope", "nucleon number", "proton number"], [[f"{X}-{A1}", A1, Z], [f"{X}-{A2}", A2, "?"]])
    return mk(rng, Z, [(A2 - Z, "That is the number of neutrons in the second isotope."), (A2, "That is its nucleon number."),
                       (Z + A2 - A1, "Isotopes have the SAME proton number; the extra nucleons are neutrons.")],
              "", f"The table gives data for two isotopes of {X}.\n\n{table}\n\nWhat is the proton number of {X}-{A2}?",
              "isotopes of an element have the same proton number", [f"same element → proton number = **{Z}**"],
              ["What does the proton number decide?", "Which element it is.", "Isotopes are the same element."])


@template("c20x_notation_pick", chapter=20, level=2, lo="20c")
def notation_pick(rng):
    X, Z, A = rng.choice(NUCLIDES)
    N = A - Z
    ans = nuc(A, Z, X)
    wrongs = {nuc(Z, A, X): "The nucleon number goes on TOP and the proton number at the bottom.",
              nuc(N, Z, X): "The top number is the nucleon number (protons + neutrons), not the neutron number.",
              nuc(A, N, X): "The bottom number is the proton number, not the neutron number."}
    table = md_table(["particle", "number in the nucleus"], [["protons", Z], ["neutrons", N]])
    return mkt(rng, ans, wrongs, f"The table describes a nucleus of {X}.\n\n{table}\n\nWhich is the correct nuclide notation for this nucleus?",
               "nuclide notation: nucleon number A on top, proton number Z at the bottom", [f"A = {Z} + {N} = {A}, Z = {Z} → **{ans}**"],
               ["Work out the nucleon number.", "A = protons + neutrons.", "A on top, Z at the bottom."])


@template("c20x_neutrons_from_name", chapter=20, level=2, lo="20c")
def neutrons_from_name(rng):
    picks = rng.sample(NUCLIDES, 4)
    X, Z, A = picks[0]
    table = md_table(["element", "proton number"], sorted([[p[0], p[1]] for p in picks]))
    return mk(rng, A - Z, [(A, "That is the nucleon number in the name."), (Z, "That is the proton number."), (A + Z, "Neutrons = nucleon number − proton number.")],
              "", f"The table gives the proton numbers of some elements.\n\n{table}\n\nHow many neutrons are in a nucleus of **{X}-{A}**?",
              "the number in the name is the nucleon number A; N = A − Z", [f"A = {A}, Z = {Z} (from the table)", f"N = {A} − {Z} = **{A - Z}**"],
              ["What does the number in the name mean?", "It is the nucleon number.", "Find Z in the table and subtract."])


@template("c20x_background_subtract", chapter=20, level=2, lo="20g")
def background_subtract(rng):
    bg = nice(rng, 15, 18, 20, 25, 30)
    m = nice(rng, 180, 240, 300, 420, 510)
    return mk(rng, m - bg, [(m, "That includes the background radiation."), (m + bg, "Background must be SUBTRACTED, not added."), (bg, "That is the background count rate.")],
              "counts/min", f"Fig. 1 shows a GM tube and counter used to measure a source. The measured count rate is **{m} counts/min**. What is the count rate due to the source alone?",
              "source count rate = measured − background", [f"{m} − {bg}", f"= **{m - bg} counts/min**"],
              ["What else does the GM tube detect?", "Background radiation.", "Subtract it."],
              figure=figs3.detector_setup([f"background count rate = {bg} counts/min"]))


@template("c20x_background_average", chapter=20, level=2, lo="20g")
def background_average(rng):
    mean = nice(rng, 16, 18, 20, 24)
    offs = rng.choice([[-3, 2, 0, 4, -3], [1, -2, 3, -4, 2], [2, -1, -3, 0, 2], [-2, 3, 1, -4, 2]])
    vals = [mean + o for o in offs]
    avg = sum(vals) / 5
    table = md_table(["minute", "1", "2", "3", "4", "5"], [["counts", *vals]])
    return mk(rng, avg, [(sum(vals), "That is the total for 5 minutes; divide by 5."), (max(vals), "That is the largest reading; background varies randomly, so take the mean."),
                         (min(vals), "That is the smallest reading; take the mean of all five.")],
              "counts/min", f"With no source present, a GM tube records these counts in five one-minute intervals.\n\n{table}\n\nWhat is the mean background count rate?",
              "mean = total ÷ number of readings (background varies randomly)", [f"total = {sum(vals)}", f"mean = {sum(vals)} ÷ 5 = **{fmt(avg, sf=3)} counts/min**"],
              ["Why are the readings different?", "Decay is random.", "Average them."])


@template("c20x_after_n_half_lives", chapter=20, level=2, lo="20h")
def after_n_half_lives(rng):
    n = rng.choice([3, 4, 5])
    A0 = nice(rng, 640, 960, 1280, 1600)
    T = nice(rng, 2, 4, 6)
    table = md_table(["quantity", "value"], [["initial activity", f"{A0} Bq"], ["half-life", f"{T} days"], ["time passed", f"{n * T} days"]])
    return mk(rng, A0 / 2 ** n, [(A0 / (2 * n), f"Halve {n} times; do not divide by 2 × {n}."), (A0 / 2 ** (n + 1), "That is one half-life too many."),
                                 (A0 / 2, "That is after only ONE half-life.")],
              "Bq", f"A radioactive sample is stored.\n\n{table}\n\nWhat is its activity at the end?",
              "after n half-lives, activity = A₀ ÷ 2ⁿ", [f"n = {n * T} ÷ {T} = {n}", f"activity = {A0} ÷ 2^{n}", f"= **{fmt(A0 / 2 ** n, sf=3)} Bq**"],
              ["How many half-lives have passed?", f"{n * T} ÷ {T}.", "Halve that many times."])


@template("c20x_count_half_lives", chapter=20, level=2, lo="20h")
def count_half_lives(rng):
    n = rng.choice([3, 4, 5])
    T = nice(rng, 2, 5, 8, 15)
    t = n * T
    table = md_table(["quantity", "value"], [["half-life", f"{T} hours"], ["time passed", f"{t} hours"]])
    return mk(rng, n, [(t * T, "Divide the time by the half-life; do not multiply."), (t - T, "Divide; do not subtract."), (T / t, "Upside down: time ÷ half-life.")],
              "", f"A sample decays.\n\n{table}\n\nHow many half-lives have passed?",
              "number of half-lives = time passed ÷ half-life", [f"{t} ÷ {T} = **{n}**"],
              ["What is one half-life?", f"{T} hours.", "How many fit into the time?"], dp=0)


# ================================================================== L3
@template("c20x_name_the_particle", chapter=20, level=3, lo="20f")
def name_the_particle(rng):
    kind = rng.choice(["alpha", "beta", "gamma"])
    if kind == "alpha":
        X, Z, A = rng.choice([n for n in NUCLIDES if n[1] > 80])
        A2, Z2 = A - 4, Z - 2
    elif kind == "beta":
        X, Z, A = rng.choice([n for n in NUCLIDES if n[1] < 60])
        A2, Z2 = A, Z + 1
    else:
        X, Z, A = rng.choice(NUCLIDES)
        A2, Z2 = A, Z
    ans = {"alpha": "an alpha particle", "beta": "a beta particle", "gamma": "a gamma ray"}[kind]
    wrongs = {"an alpha particle": "Alpha emission lowers A by 4 and Z by 2.", "a beta particle": "Beta emission keeps A the same and raises Z by 1.",
              "a gamma ray": "Gamma emission changes neither A nor Z.", "a neutron": "Losing a neutron lowers A by 1 and leaves Z the same."}
    wrongs.pop(ans)
    wrongs = dict(list(wrongs.items())[:3])
    table = md_table(["", "nucleon number", "proton number"], [["parent nucleus", A, Z], ["nucleus after the decay", A2, Z2]])
    return mkt(rng, ans, wrongs, f"A nucleus of {X} decays and emits one type of radiation.\n\n{table}\n\nWhat is emitted?",
               "α: A − 4, Z − 2; β: A same, Z + 1; γ: no change", [f"change: A {A2 - A:+d}, Z {Z2 - Z:+d} → **{ans}**"],
               ["How much does A change?", "How much does Z change?", "Match the changes to a radiation."])


@template("c20x_beta_daughter_pair", chapter=20, level=3, lo="20f")
def beta_daughter_pair(rng):
    X, Z, A = rng.choice([n for n in NUCLIDES if n[1] < 60])
    ans = f"nucleon number {A}, proton number {Z + 1}"
    wrongs = {f"nucleon number {A - 1}, proton number {Z + 1}": "The electron has negligible mass: the nucleon number does not change.",
              f"nucleon number {A}, proton number {Z - 1}": "In beta decay a neutron becomes a proton, so Z RISES by 1.",
              f"nucleon number {A - 4}, proton number {Z - 2}": "That is alpha decay."}
    return mkt(rng, ans, wrongs, f"Fig. 1 shows a nucleus that decays by emitting a beta particle. What are the nucleon number and proton number of the new nucleus?",
               "β decay: a neutron → proton + electron; A unchanged, Z + 1", [f"A = {A}, Z = {Z} + 1 = {Z + 1}", f"**{ans}**"],
               ["What happens inside the nucleus in beta decay?", "A neutron changes into a proton.", "So A stays the same and Z rises by 1."],
               figure=figs3.nuclide(A, Z, X))


@template("c20x_counts_to_rate", chapter=20, level=3, lo="20g")
def counts_to_rate(rng):
    t = nice(rng, 2, 4, 5)
    b = nice(rng, 20, 24, 30)
    rate = nice(rng, 150, 200, 260, 320)
    N = (rate + b) * t
    return mk(rng, N / t - b, [(N / t, "Subtract the background rate."), (N - b, "Turn the counts into a count rate (÷ time) before subtracting."),
                               ((N - b) / t, "Subtract the background RATE from the count RATE.")],
              "counts/min", f"Fig. 1 shows a source and a GM tube. The counter records **{N} counts in {t} minutes**. What is the corrected count rate due to the source?",
              "count rate = counts ÷ time; corrected = count rate − background", [f"count rate = {N} ÷ {t} = {fmt(N / t)} counts/min", f"corrected = {fmt(N / t)} − {b} = **{fmt(N / t - b)} counts/min**"],
              ["First find the count rate.", "Then remove the background.", "Both must be per minute."],
              figure=figs3.detector_setup([f"background count rate = {b} counts/min"]))


@template("c20x_corrected_half_life", chapter=20, level=3, lo="20g")
def corrected_half_life(rng):
    bg = nice(rng, 20, 30, 40)
    c0 = nice(rng, 640, 800, 960)
    T = nice(rng, 2, 3, 4, 5)
    rows = [[k * T, fmt(c0 / 2 ** k + bg)] for k in range(4)]
    table = md_table(["time / min", "measured count rate / counts per minute"], rows)
    return mk(rng, T, [(2 * T, "That is the time for the corrected count rate to fall to a QUARTER."), (T / 2, "Subtract the background, then find when the count rate halves."),
                       (3 * T, "That is the last time in the table.")],
              "min", f"The background count rate is **{bg} counts/min**. The measured count rates from a source are shown.\n\n{table}\n\nWhat is the half-life of the source?",
              "subtract background first, then find the time to halve", [f"corrected: {fmt(c0)} → {fmt(c0 / 2)} counts/min", f"this takes **{T} min**"],
              ["Correct each reading for background.", f"The corrected starting value is {fmt(c0)}.", "When does it reach half of that?"])


@template("c20x_plate_deflection", chapter=20, level=3, lo="20e")
def plate_deflection(rng):
    top = rng.choice(["+", "−"])
    bottom = "−" if top == "+" else "+"
    case = rng.choice(["top", "bottom", "none"])
    toward = {"top": top, "bottom": bottom}
    if case == "none":
        q = "passes straight through without being deflected"
        ans = "gamma"
    else:
        q = f"is deflected towards the {case} plate"
        ans = "alpha" if toward[case] == "−" else "beta"
    wrongs = {r: {"alpha": "Alpha is positive, so it bends towards the NEGATIVE plate.", "beta": "Beta is negative, so it bends towards the POSITIVE plate.",
                  "gamma": "Gamma has no charge and is not deflected."}[r] for r in ("alpha", "beta", "gamma") if r != ans}
    wrongs["all three equally"] = "The radiations have different charges, so they behave differently."
    table = md_table(["plate", "charge"], [["top", top], ["bottom", bottom]])
    return mkt(rng, ans, wrongs, f"Radiation passes between two charged plates.\n\n{table}\n\nWhich radiation {q}?",
               "α (+) → negative plate; β (−) → positive plate; γ undeflected", [f"**{ans}**"],
               ["What is the charge of each radiation?", "Opposite charges attract.", "Which plate has the opposite charge?"])


@template("c20x_range_in_air", chapter=20, level=3, lo="20e")
def range_in_air(rng):
    labels = ["P", "Q", "R"]
    rng.shuffle(labels)
    ra, rb = nice(rng, 3, 4, 5), nice(rng, 50, 80, 100)
    rows = [(labels[0], f"{ra} cm"), (labels[1], f"{rb} cm"), (labels[2], "many metres (only gradually reduced)")]
    asked = rng.choice(["alpha", "beta", "gamma"])
    ans = labels[["alpha", "beta", "gamma"].index(asked)]
    wrongs = {lab: "Alpha has the shortest range in air (a few cm), beta about a metre, gamma a very long range." for lab in labels if lab != ans}
    wrongs["none of them"] = "Each of the three ranges matches one radiation."
    table = md_table(["radiation", "range in air"], sorted([list(r) for r in rows]))
    return mkt(rng, ans, wrongs, f"The table shows the ranges in air of three radiations.\n\n{table}\n\nWhich one is **{asked}**?",
               "range in air: α a few cm; β up to about 1 m; γ many metres", [f"{asked} → **{ans}**"],
               ["Which radiation is the most ionising?", "It loses its energy fastest: shortest range.", "Order the ranges."])


@template("c20x_tracer_choice", chapter=20, level=3, lo="20i")
def tracer_choice(rng):
    labels = ["P", "Q", "R", "S"]
    rng.shuffle(labels)
    h = nice(rng, 6, 8, 13)
    rows = [(labels[0], "gamma", f"{h} hours"), (labels[1], "alpha", f"{h} hours"), (labels[2], "gamma", f"{nice(rng, 30, 50)} years"), (labels[3], "beta", f"{nice(rng, 2, 3)} minutes")]
    ans = labels[0]
    wrongs = {labels[1]: "Alpha cannot pass out of the body to the detector, and it is very ionising inside it.",
              labels[2]: "A half-life of years means the patient stays radioactive for far too long.",
              labels[3]: "Beta is absorbed by the body, and a half-life of minutes is too short to complete the test."}
    table = md_table(["isotope", "radiation", "half-life"], sorted([list(r) for r in rows]))
    return mkt(rng, ans, wrongs, f"A hospital needs a tracer to inject into a patient so that it can be detected outside the body.\n\n{table}\n\nWhich isotope is most suitable?",
               "medical tracer: gamma (escapes the body, weakly ionising) with a half-life of hours", [f"{ans}: gamma, half-life {h} hours → **{ans}**"],
               ["Which radiation can escape the body?", "Gamma.", "Which half-life is long enough for the test but short enough to be safe?"])


@template("c20x_thickness_gauge", chapter=20, level=3, lo="20i")
def thickness_gauge(rng):
    R0 = nice(rng, 400, 500, 600)
    d = nice(rng, 60, 80, 100)
    case = rng.choice(["higher", "lower"])
    R = R0 + d if case == "higher" else R0 - d
    ans = "the paper is too thin" if case == "higher" else "the paper is too thick"
    wrongs = {("the paper is too thick" if case == "higher" else "the paper is too thin"): "Thicker paper absorbs MORE beta, so the count rate would FALL.",
              "the paper is the correct thickness": "The count rate has changed, so the thickness has changed.",
              "the source has nearly decayed": "A long half-life source is chosen so that its count rate stays almost constant."}
    table = md_table(["", "count rate / counts per minute"], [["paper of the correct thickness", R0], ["reading now", R]])
    return mkt(rng, ans, wrongs, f"A paper mill uses a beta source on one side of the paper and a detector on the other, with a source of long half-life.\n\n{table}\n\nWhat does the new reading show?",
               "more beta reaches the detector when the paper is thinner", [("count rate higher → less beta absorbed" if case == "higher" else "count rate lower → more beta absorbed"), f"**{ans}**"],
               ["What happens to beta passing through paper?", "Some is absorbed.", "Thicker paper absorbs more."])


# ================================================================== L4
@template("c20x_mixture_identify", chapter=20, level=4, lo="20e")
def mixture_identify(rng):
    kind = rng.choice(["ab", "bg", "ag"])
    bg = 20
    a, b, g = nice(rng, 300, 400), nice(rng, 200, 250), nice(rng, 100, 150)
    comp = {"ab": (a, b, 0), "bg": (0, b, g), "ag": (a, 0, g)}[kind]
    none = sum(comp) + bg
    paper = comp[1] + comp[2] + bg
    alum = comp[2] + bg
    names = {"ab": "alpha and beta", "bg": "beta and gamma", "ag": "alpha and gamma"}
    ans = names[kind]
    wrongs = {"alpha and beta": "With alpha and beta only, the count rate would fall to background with aluminium.",
              "beta and gamma": "With no alpha, adding paper would hardly change the count rate.",
              "alpha and gamma": "With no beta, adding aluminium after paper would hardly change the count rate.",
              "alpha, beta and gamma": "With all three, the count rate would drop at paper AND at aluminium and stay above background."}
    wrongs.pop(ans)
    table = md_table(["absorber", "count rate / counts per minute"], [["none", none], ["paper", paper], ["5 mm aluminium", alum]])
    return mkt(rng, ans, wrongs, f"The background count rate is {bg} counts/min. Different absorbers are placed between a source and a GM tube.\n\n{table}\n\nWhich radiations does the source emit?",
               "a drop at paper → α present; a further drop at aluminium → β present; above background after aluminium → γ present",
               [f"paper: {none} → {paper}", f"aluminium: {paper} → {alum} (background {bg})", f"**{ans}**"],
               ["Where does the count rate drop?", "A drop at paper means alpha; a drop at aluminium means beta.", "Is anything left above background?"])


@template("c20x_background_sources", chapter=20, level=4, lo="20g")
def background_sources(rng):
    radon = nice(rng, 1.2, 1.3, 1.5)
    med = nice(rng, 0.4, 0.5, 0.6)
    food = nice(rng, 0.3, 0.4)
    cosmic = nice(rng, 0.3, 0.4)
    ground = nice(rng, 0.4, 0.5)
    total = radon + med + food + cosmic + ground
    pct = radon / total * 100
    table = md_table(["source", "average dose / mSv per year"], [["radon gas", fmt(radon)], ["medical", fmt(med)], ["food and drink", fmt(food)], ["cosmic rays", fmt(cosmic)], ["rocks and buildings", fmt(ground)]])
    return mk(rng, pct, [(radon, "That is the dose in mSv, not a percentage."), (radon / total, "That is the fraction; multiply by 100."),
                         (radon / 5 * 100, "Divide by the TOTAL dose, not by the number of sources.")],
              "%", f"The table shows a person's average yearly radiation dose from different sources.\n\n{table}\n\nWhat percentage of the total comes from radon gas?",
              "% = radon dose ÷ total dose × 100", [f"total = {fmt(total, sf=3)} mSv", f"% = {fmt(radon)} ÷ {fmt(total, sf=3)} × 100 = **{fmt(pct, sf=3)}%**"],
              ["Add up all the doses.", "Divide the radon dose by the total.", "Multiply by 100."])


@template("c20x_half_life_from_ratio", chapter=20, level=4, lo="20h")
def half_life_from_ratio(rng):
    n = rng.choice([3, 4])
    T = nice(rng, 2, 3, 5, 6)
    t = n * T
    A0 = nice(rng, 800, 1200, 1600)
    A = A0 / 2 ** n
    table = md_table(["time / days", "activity / Bq"], [[0, A0], [t, fmt(A)]])
    return mk(rng, T, [(t, "That is the total time, which covers several half-lives."), (t / 2 ** n, f"The activity fell by a factor of {2 ** n}, which is {n} halvings: divide the time by {n}."),
                       (t / (n + 1), "Count the halvings again.")],
              "days", f"The activity of a sample is measured twice.\n\n{table}\n\nWhat is the half-life?",
              "count the halvings, then half-life = time ÷ number of half-lives",
              [f"{A0} → {fmt(A)} is ÷ {2 ** n} = {n} halvings", f"T = {t} ÷ {n} = **{T} days**"],
              ["By what factor did the activity fall?", "How many halvings is that?", "Divide the time by that number."])


@template("c20x_mass_decayed", chapter=20, level=4, lo="20h")
def mass_decayed(rng):
    n = rng.choice([3, 4])
    m0 = nice(rng, 16, 32, 48, 64)
    T = nice(rng, 5, 8, 12)
    table = md_table(["quantity", "value"], [["initial mass of the isotope", f"{m0} g"], ["half-life", f"{T} days"], ["time passed", f"{n * T} days"]])
    return mk(rng, m0 - m0 / 2 ** n, [(m0 / 2 ** n, "That is the mass REMAINING; the question asks how much has decayed."), (m0 / 2, "That is after one half-life."),
                                      (m0 - m0 / (2 * n), f"Halve {n} times; do not divide by 2 × {n}.")],
              "g", f"A sample of a radioactive isotope decays.\n\n{table}\n\nWhat mass of the isotope has decayed?",
              "remaining = m₀ ÷ 2ⁿ; decayed = m₀ − remaining", [f"n = {n}", f"remaining = {m0} ÷ {2 ** n} = {fmt(m0 / 2 ** n)} g", f"decayed = **{fmt(m0 - m0 / 2 ** n)} g**"],
              ["How many half-lives?", "Work out what remains.", "Subtract from the starting mass."])


@template("c20x_alpha_then_beta", chapter=20, level=4, lo="20f")
def alpha_then_beta(rng):
    X, Z, A = rng.choice([n for n in NUCLIDES if n[1] > 80])
    kind = rng.choice(["proton", "nucleon"])
    if kind == "proton":
        ans, wr = Z - 1, [(Z - 2, "The beta decay then RAISES the proton number by 1."), (Z - 3, "Beta decay increases Z; it does not decrease it."), (Z + 1, "Alpha decay lowers Z by 2 first.")]
    else:
        ans, wr = A - 4, [(A - 5, "Beta decay does not change the nucleon number."), (A - 3, "Alpha lowers A by 4; beta leaves it unchanged."), (A, "Alpha decay removes 4 nucleons.")]
    return mk(rng, ans, wr, "", f"Fig. 1 shows a nucleus that emits an alpha particle, and the new nucleus then emits a beta particle. What is the **{kind} number** of the final nucleus?",
              "α: A − 4, Z − 2; β: A same, Z + 1", [f"after α: A = {A - 4}, Z = {Z - 2}", f"after β: A = {A - 4}, Z = {Z - 1}", f"**{ans}**"],
              ["Apply the alpha decay first.", "Then the beta decay.", "Track A and Z separately."],
              figure=figs3.nuclide(A, Z, X))


@template("c20x_daughter_element", chapter=20, level=4, lo="20f")
def daughter_element(rng):
    els = {82: "lead (Pb)", 83: "bismuth (Bi)", 84: "polonium (Po)", 85: "astatine (At)", 86: "radon (Rn)", 87: "francium (Fr)", 88: "radium (Ra)", 89: "actinium (Ac)", 90: "thorium (Th)", 91: "protactinium (Pa)"}
    Z = rng.choice([86, 87, 88, 89])
    kind = rng.choice(["alpha", "beta"])
    Zd = Z - 2 if kind == "alpha" else Z + 1
    ans = els[Zd]
    cands = {Z - 2: "That would be alpha decay.", Z + 1: "That would be beta decay.", Z - 1: "Neither decay lowers Z by exactly 1.", Z: "The element changes when alpha or beta is emitted.", Z + 2: "No single decay raises Z by 2."}
    wrongs = {els[k]: v for k, v in cands.items() if k != Zd and k in els}
    wrongs = dict(list(wrongs.items())[:3])
    table = md_table(["proton number", "element"], [[k, v] for k, v in els.items() if Z - 3 <= k <= Z + 3])
    return mkt(rng, ans, wrongs, f"A nucleus of {els[Z].split(' ')[0]} (proton number {Z}) emits a **{kind}** particle.\n\n{table}\n\nWhich element is formed?",
               "α decay: Z − 2; β decay: Z + 1", [f"Z = {Z} {'− 2' if kind == 'alpha' else '+ 1'} = {Zd}", f"**{ans}**"],
               ["How does this decay change the proton number?", "α: −2; β: +1.", "Look up the new proton number."])


@template("c20x_fission_neutrons", chapter=20, level=4, lo="20j")
def fission_neutrons(rng):
    (X1, Z1, A1), (X2, Z2, A2) = rng.choice([(("Ba", 56, 141), ("Kr", 36, 92)), (("Xe", 54, 140), ("Sr", 38, 94)), (("Cs", 55, 137), ("Rb", 37, 96)),
                                             (("La", 57, 145), ("Br", 35, 88)), (("Te", 52, 137), ("Zr", 40, 97))])
    x = 236 - A1 - A2
    table = md_table(["nucleus or particle", "nucleon number", "proton number"], [["uranium-235", 235, 92], ["neutron (absorbed)", 1, 0], [f"{X1}", A1, Z1], [f"{X2}", A2, Z2]])
    return mk(rng, x, [(x + 1, "Include the absorbed neutron on the left: 235 + 1 = 236 nucleons."), (x - 1, "Count again: the nucleon numbers must balance."),
                       (x + 2, "The total nucleon number on each side must be the same.")],
              "", f"A uranium-235 nucleus absorbs a neutron and splits into {X1}-{A1}, {X2}-{A2} and some neutrons.\n\n{table}\n\nHow many neutrons are released?",
              "nucleon number is conserved: 235 + 1 = A₁ + A₂ + number of neutrons", [f"236 = {A1} + {A2} + x", f"x = **{x}**"],
              ["Add the nucleon numbers on the left.", "Add those of the two fragments.", "The difference is the neutrons released."], dp=0)


@template("c20x_fusion_particle", chapter=20, level=4, lo="20j")
def fusion_particle(rng):
    r = rng.choice([("hydrogen-2", (2, 1), "hydrogen-3", (3, 1), "helium-4", (4, 2), "a neutron"),
                    ("hydrogen-2", (2, 1), "hydrogen-2", (2, 1), "helium-3", (3, 2), "a neutron"),
                    ("hydrogen-2", (2, 1), "hydrogen-2", (2, 1), "hydrogen-3", (3, 1), "a proton"),
                    ("hydrogen-2", (2, 1), "helium-3", (3, 2), "helium-4", (4, 2), "a proton")])
    n1, (a1, z1), n2, (a2, z2), n3, (a3, z3), ans = r
    A, Z = a1 + a2 - a3, z1 + z2 - z3
    wrongs = {k: v for k, v in {"a neutron": "A neutron has nucleon number 1 and proton number 0.", "a proton": "A proton has nucleon number 1 and proton number 1.",
                                "an electron": "An electron has nucleon number 0.", "an alpha particle": "An alpha particle has nucleon number 4."}.items() if k != ans}
    table = md_table(["nucleus", "nucleon number", "proton number"], [[n1, a1, z1], [n2, a2, z2], [n3, a3, z3]])
    return mkt(rng, ans, wrongs, f"In a fusion reaction, {n1} and {n2} join to form {n3} and a particle X.\n\n{table}\n\nWhat is X?",
               "nucleon and proton numbers are conserved", [f"X: nucleon number {a1} + {a2} − {a3} = {A}, proton number {z1} + {z2} − {z3} = {Z}", f"**{ans}**"],
               ["Balance the nucleon numbers.", "Balance the proton numbers.", "Which particle has those numbers?"])


# ================================================================== L5
@template("c20x_chain_counts", chapter=20, level=5, lo="20f")
def chain_counts(rng):
    p, d, a, b = rng.choice([(("U", 92, 238), ("Pb", 82, 206), 8, 6), (("Th", 90, 232), ("Pb", 82, 208), 6, 4), (("U", 92, 235), ("Pb", 82, 207), 7, 4), (("Ra", 88, 226), ("Pb", 82, 206), 5, 4)])
    ans = f"{a} alpha and {b} beta"
    wrongs = {f"{b} alpha and {a} beta": "Use the nucleon numbers first: only alpha changes A (by 4 each).",
              f"{a} alpha and 0 beta": f"{a} alpha decays would lower Z by {2 * a}; the betas raise it back to {d[1]}.",
              f"{a} alpha and {a} beta": "Work out the betas from the proton numbers after the alphas."}
    table = md_table(["nucleus", "nucleon number", "proton number"], [[f"{p[0]}-{p[2]} (start)", p[2], p[1]], [f"{d[0]}-{d[2]} (end)", d[2], d[1]]])
    return mkt(rng, ans, wrongs, f"A nucleus decays by a series of alpha and beta emissions.\n\n{table}\n\nHow many alpha and beta particles are emitted?",
               "alphas = ΔA ÷ 4; then betas = Z after alphas − final Z",
               [f"ΔA = {p[2] - d[2]} → {a} alphas", f"Z after alphas = {p[1]} − {2 * a} = {p[1] - 2 * a}", f"betas = {d[1]} − {p[1] - 2 * a} = {b}", f"**{ans}**"],
               ["Only alpha decay changes the nucleon number.", "Each alpha lowers A by 4.", "Then use the proton numbers to find the betas."])


@template("c20x_carbon_dating", chapter=20, level=5, lo="20h")
def carbon_dating(rng):
    n = rng.choice([2, 3, 4])
    T = 5700
    A_live = nice(rng, 16, 32, 64)
    A_old = A_live / 2 ** n
    table = md_table(["quantity", "value"], [["count rate from 1 g of living wood", f"{A_live} counts/min"], ["count rate from 1 g of ancient wood", f"{fmt(A_old)} counts/min"], ["half-life of carbon-14", f"{T} years"]])
    return mk(rng, n * T, [((n - 1) * T, "Count the halvings again."), ((n + 1) * T, "Count the halvings again."), (T * 2 ** n, f"The count rate fell by a factor of {2 ** n}, which is {n} half-lives, not {2 ** n}.")],
              "years", f"Carbon-14 is used to date an ancient piece of wood (background already subtracted).\n\n{table}\n\nHow old is the wood?",
              "count the halvings; age = number of half-lives × half-life", [f"{A_live} → {fmt(A_old)}: {n} halvings", f"age = {n} × {T} = **{n * T} years**"],
              ["By what factor has the count rate fallen?", "How many halvings is that?", "Multiply by the half-life."])


@template("c20x_background_levels_off", chapter=20, level=5, lo="20g")
def background_levels_off(rng):
    bg = nice(rng, 18, 22, 26)
    c5, c10, c20 = nice(rng, 900, 1000), nice(rng, 420, 480), nice(rng, 150, 180)
    table = md_table(["distance from the source / cm", "count rate / counts per minute"], [[5, c5 + bg], [10, c10 + bg], [20, c20 + bg], [100, bg], [150, bg], [200, bg]])
    return mk(rng, c10, [(c10 + bg, "That includes background. The steady value far away is the background."), (c10 + 2 * bg, "Subtract the background, do not add it."),
                         (c10 + bg - c20 - bg, "Correct one reading for background; do not subtract two readings.")],
              "counts/min", f"A GM tube is moved away from a source of beta radiation.\n\n{table}\n\nWhat is the count rate due to the source alone at 10 cm?",
              "far away the beta is absorbed by air, so the steady reading is background; corrected = measured − background",
              [f"steady reading far away = background = {bg} counts/min", f"at 10 cm: {c10 + bg} − {bg} = **{c10} counts/min**"],
              ["Why does the reading stop changing far away?", "Beta cannot reach the tube; only background is detected.", "Subtract that background."])


@template("c20x_background_long_count", chapter=20, level=5, lo="20g")
def background_long_count(rng):
    Nb = nice(rng, 180, 200, 240, 250)
    tb = 10
    t = nice(rng, 2, 4)
    rate = nice(rng, 300, 350, 420)
    M = (rate + Nb / tb) * t
    ans = M / t - Nb / tb
    table = md_table(["measurement", "counts", "time / min"], [["no source (background)", Nb, tb], ["with the source", fmt(M), t]])
    return mk(rng, ans, [(M / t, "Subtract the background count rate."), (M / t - Nb, "Turn the background counts into a rate (÷ 10 min) first."),
                         ((M - Nb) / t, "The two counts were taken over different times: compare RATES.")],
              "counts/min", f"A student measures the background for 10 minutes and then the source for {t} minutes.\n\n{table}\n\nWhat is the count rate due to the source?",
              "convert both to counts per minute, then subtract", [f"background = {Nb} ÷ {tb} = {fmt(Nb / tb)} counts/min", f"with source = {fmt(M)} ÷ {t} = {fmt(M / t)} counts/min", f"source = **{fmt(ans)} counts/min**"],
              ["Why measure the background for longer?", "Decay is random; a longer count averages it out.", "Compare rates, not counts."])


@template("c20x_source_for_use", chapter=20, level=5, lo="20i")
def source_for_use(rng):
    labels = ["W", "X", "Y", "Z"]
    rng.shuffle(labels)
    srcs = {"smoke detector": (labels[0], "alpha", f"{nice(rng, 430, 460)} years"), "sterilising medical equipment": (labels[1], "gamma", f"{nice(rng, 5, 30)} years"),
            "controlling the thickness of paper": (labels[2], "beta", f"{nice(rng, 28, 30)} years"), "a medical tracer": (labels[3], "gamma", f"{nice(rng, 6, 8)} hours")}
    use = rng.choice(list(srcs))
    ans = srcs[use][0]
    why = {"smoke detector": "alpha ionises the air strongly, has a short range, and a long half-life",
           "sterilising medical equipment": "gamma penetrates the packaging and kills microbes, with a long half-life",
           "controlling the thickness of paper": "beta is partly absorbed by paper, so changes in thickness change the count rate",
           "a medical tracer": "gamma escapes the body, and a half-life of hours keeps the dose low"}
    wrongs = {s[0]: f"Source {s[0]} ({s[1]}, half-life {s[2]}) is suited to {u}." for u, s in srcs.items() if u != use}
    table = md_table(["source", "radiation", "half-life"], sorted([list(s) for s in srcs.values()]))
    return mkt(rng, ans, wrongs, f"The table shows four radioactive sources.\n\n{table}\n\nWhich source is most suitable for **{use}**?",
               "choose the radiation for its penetration/ionisation, and a half-life suited to the use", [f"{why[use]} → **{ans}**"],
               ["What must the radiation do in this use?", "Which radiation can do that?", "Is the half-life suitable?"])


@template("c20x_dose_hours", chapter=20, level=5, lo="20i")
def dose_hours(rng):
    L = nice(rng, 6, 10, 20)
    r = nice(rng, 2.5, 4.0, 5.0, 8.0, 10.0)
    hrs = L * 1000 / r
    table = md_table(["quantity", "value"], [["yearly dose limit for the worker", f"{L} mSv"], ["dose rate in the work area", f"{fmt(r)} µSv per hour"]])
    return mk(rng, hrs, [(L / r, "Convert mSv to µSv first: 1 mSv = 1000 µSv."), (L * 1e6 / r, "1 mSv = 1000 µSv, not 10⁶ µSv."), (L * 1000 * r, "Divide the limit by the dose rate.")],
              "hours", f"A radiation worker must stay below a yearly dose limit.\n\n{table}\n\nWhat is the maximum time the worker can spend in the area each year?",
              "time = dose limit ÷ dose rate (same units)", [f"{L} mSv = {L * 1000} µSv", f"time = {L * 1000} ÷ {fmt(r)}", f"= **{fmt(hrs, sf=3)} hours**"],
              ["Put the limit and the rate in the same units.", "1 mSv = 1000 µSv.", "Divide the limit by the rate."])


@template("c20x_fission_product", chapter=20, level=5, lo="20j")
def fission_product(rng):
    (X1, Z1, A1), (X2, Z2, A2), x = rng.choice([(("Ba", 56, 141), ("Kr", 36, 92), 3), (("Xe", 54, 140), ("Sr", 38, 94), 2), (("Cs", 55, 137), ("Rb", 37, 96), 3),
                                                (("La", 57, 145), ("Br", 35, 88), 3)])
    ans = f"nucleon number {A2}, proton number {Z2}"
    wrongs = {f"nucleon number {A2 + x}, proton number {Z2}": "The released neutrons carry away nucleons too: subtract them.",
              f"nucleon number {A2 - 1}, proton number {Z2}": "Include the absorbed neutron on the left: 235 + 1 = 236.",
              f"nucleon number {A2}, proton number {A2 - Z2}": "That is the neutron number, not the proton number. Use 92 − " + str(Z1) + "."}
    table = md_table(["", "nucleon number", "proton number"], [["uranium-235", 235, 92], ["neutron absorbed", 1, 0], [f"{X1} produced", A1, Z1], [f"neutrons released", f"{x} × 1", 0]])
    return mkt(rng, ans, wrongs, f"A uranium-235 nucleus absorbs a neutron and splits into {X1}, a nucleus Y and {x} neutrons.\n\n{table}\n\nWhat are the nucleon number and proton number of Y?",
               "nucleon number and proton number are both conserved", [f"A = 236 − {A1} − {x} = {A2}", f"Z = 92 − {Z1} = {Z2}", f"**{ans}** ({X2})"],
               ["Balance the nucleon numbers.", "Remember the neutrons on both sides.", "Balance the proton numbers."])


@template("c20x_reaction_type", chapter=20, level=5, lo="20j")
def reaction_type(rng):
    labels = ["P", "Q", "R", "S"]
    rng.shuffle(labels)
    rx = [(labels[0], f"{nuc(2, 1, 'H')} + {nuc(3, 1, 'H')} → {nuc(4, 2, 'He')} + n", "fusion"),
          (labels[1], f"{nuc(235, 92, 'U')} + n → {nuc(141, 56, 'Ba')} + {nuc(92, 36, 'Kr')} + 3n", "fission"),
          (labels[2], f"{nuc(238, 92, 'U')} → {nuc(234, 90, 'Th')} + {nuc(4, 2, 'He')}", "alpha decay"),
          (labels[3], f"{nuc(14, 6, 'C')} → {nuc(14, 7, 'N')} + e", "beta decay")]
    asked = rng.choice(["fusion", "fission"])
    ans = labels[0] if asked == "fusion" else labels[1]
    wrongs = {lab: f"Reaction {lab} is {kind}." for lab, _, kind in rx if lab != ans}
    table = md_table(["reaction", "equation"], sorted([[lab, eq] for lab, eq, _ in rx]))
    return mkt(rng, ans, wrongs, f"The table shows four nuclear reactions.\n\n{table}\n\nWhich reaction is **{asked}**?",
               "fusion: light nuclei join; fission: a heavy nucleus splits (after absorbing a neutron)", [f"**{ans}** is {asked}"],
               ["Fusion joins light nuclei.", "Fission splits a heavy nucleus.", "Alpha and beta decay emit one particle from one nucleus."])
