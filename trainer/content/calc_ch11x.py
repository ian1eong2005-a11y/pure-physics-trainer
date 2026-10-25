"""Chapter 11 Electromagnetic Spectrum (6091) bank extension: calculation and data-reading templates, 10 per level,
each LO at least twice. Contexts adapted from the question bank (SEAB 2016-2025: radio station frequencies, microwave ovens,
satellite links, TV remote controls, X-ray and UV exposure, mobile phone signals; school papers 2024-2025)."""
from .. import sketches
from .base import fmt, md_table, mk, mkt, nice, sci, template

C = 3.0e8
REGIONS = [("radio waves", 1e-1, 1e5), ("microwaves", 1e-3, 1e-1), ("infrared", 7e-7, 1e-3), ("visible light", 4e-7, 7e-7),
           ("ultraviolet", 1e-8, 4e-7), ("X-rays", 1e-11, 1e-8), ("gamma rays", 1e-16, 1e-11)]


def region_of(lam):
    return next(n for n, lo, hi in REGIONS if lo <= lam < hi)


# ================================================================== L1
@template("c11x_c_from_f_lambda", chapter=11, level=1, lo="11a")
def c_from_f_lambda(rng):
    f = nice(rng, 1.0e8, 1.5e8, 2.0e8, 3.0e8)
    lam = C / f
    return mk(rng, lam, [(f / C, "λ = c ÷ f."), (C * f, "Divide c by f."), (lam * 100, "The answer is in metres.")],
              "m", f"A radio station broadcasts in a vacuum-like atmosphere.\n\n{md_table(['quantity', 'value'], [['frequency', f'{sci(f)} Hz'], ['speed of EM waves', '3.0 × 10⁸ m/s']])}\n\nWhat is the wavelength of the radio waves?",
              "c = f λ → λ = c ÷ f", [f"λ = 3.0 × 10⁸ ÷ {sci(f)} = **{fmt(lam)} m**"],
              ["All EM waves travel at 3.0 × 10⁸ m/s.", "λ = c ÷ f.", "Calculate."])


@template("c11x_region_from_wavelength", chapter=11, level=1, lo="11b")
def region_from_wavelength(rng):
    lam, ans = rng.choice([(5e-7, "visible light"), (1e-5, "infrared"), (3e-2, "microwaves"), (1e-10, "X-rays"), (2e-8, "ultraviolet"), (100, "radio waves")])
    others = [n for n, _, _ in REGIONS if n != ans]
    rng.shuffle(others)
    wrongs = {n: f"{n} have wavelengths outside this range." for n in others[:3]}
    table = md_table(["region", "typical wavelength range / m"], [[n, f"{sci(lo)} to {sci(hi)}"] for n, lo, hi in REGIONS])
    return mkt(rng, ans, wrongs, f"{table}\n\nAn electromagnetic wave has a wavelength of **{sci(lam)} m**. Which region is it in?",
               "match the wavelength to the range in the table", [f"{sci(lam)} m lies in the range for **{ans}**"],
               ["Find the row whose range contains the wavelength.", "Compare powers of ten.", "Pick that region."])


@template("c11x_order_wavelength", chapter=11, level=1, lo="11b")
def order_wavelength(rng):
    names = rng.sample([n for n, _, _ in REGIONS], 4)
    order = [n for n, _, _ in REGIONS if n in names]
    ans = order[0]
    wrongs = {n: ("That has the SHORTEST wavelength of these." if n == order[-1] else "Use the order of the spectrum: radio has the longest wavelength, gamma the shortest.") for n in names if n != ans}
    return mkt(rng, ans, wrongs, f"Fig. 1 shows the electromagnetic spectrum. Of **{', '.join(names)}**, which has the LONGEST wavelength?",
               "spectrum order (longest λ first): radio, microwaves, infrared, visible, UV, X-rays, gamma", [f"in spectrum order: {', '.join(order)} → **{ans}**"],
               ["Recall the order of the spectrum.", "Radio waves have the longest wavelength.", "Find the earliest of the four."], figure=sketches.em_spectrum())


@template("c11x_highest_frequency", chapter=11, level=1, lo="11b")
def highest_frequency(rng):
    names = rng.sample([n for n, _, _ in REGIONS], 4)
    order = [n for n, _, _ in REGIONS if n in names]
    ans = order[-1]
    wrongs = {n: ("That has the LOWEST frequency of these." if n == order[0] else "Frequency increases towards gamma rays.") for n in names if n != ans}
    return mkt(rng, ans, wrongs, f"Fig. 1 shows the electromagnetic spectrum. Of **{', '.join(names)}**, which has the HIGHEST frequency?",
               "frequency increases from radio towards gamma", [f"nearest the gamma end: **{ans}**"],
               ["Which end has the highest frequency?", "The gamma-ray end.", "Find the closest to it."], figure=sketches.em_spectrum())


@template("c11x_use_from_table", chapter=11, level=1, lo="11c")
def use_from_table(rng):
    uses = [("TV remote control", "infrared"), ("detecting forged bank notes", "ultraviolet"), ("satellite communication", "microwaves"), ("radio broadcasting", "radio waves"),
            ("killing cancer cells", "gamma rays"), ("photographing broken bones", "X-rays"), ("thermal imaging", "infrared")]
    use, ans = rng.choice(uses)
    others = [n for n, _, _ in REGIONS if n != ans]
    rng.shuffle(others)
    wrongs = {n: "That region has different uses." for n in others[:3]}
    return mkt(rng, ans, wrongs, f"Fig. 1 shows the electromagnetic spectrum. Which region is used for **{use}**?",
               "recall typical uses of each region", [f"{use} → **{ans}**"],
               ["Think of the device or job.", "Which waves does it use?", "Match to a region."], figure=sketches.em_spectrum())


@template("c11x_microwave_oven_lambda", chapter=11, level=1, lo="11c")
def microwave_oven_lambda(rng):
    f = nice(rng, 2.4e9, 2.45e9, 2.5e9)
    lam = C / f * 100
    return mk(rng, lam, [(C / f, "That is in metres; the answer is in cm."), (f / C * 100, "λ = c ÷ f."), (lam * 10, "Check the powers of ten.")],
              "cm", f"{md_table(['quantity', 'value'], [['frequency of microwave oven', f'{sci(f)} Hz'], ['speed of EM waves', '3.0 × 10⁸ m/s']])}\n\nWhat is the wavelength of the microwaves, in cm?",
              "λ = c ÷ f", [f"λ = 3.0 × 10⁸ ÷ {sci(f)} = {fmt(C / f)} m", f"= **{fmt(lam)} cm**"],
              ["Use c = f λ.", "λ = c ÷ f.", "Convert to cm."])


@template("c11x_phone_signal_time", chapter=11, level=1, lo="11c")
def phone_signal_time(rng):
    d_km = nice(rng, 3, 6, 15, 30)
    t = d_km * 1000 / C * 1e6
    return mk(rng, t, [(d_km * 1000 / C, "That is in seconds; the answer is in µs."), (d_km / C * 1e6, "Convert km to m."), (C / (d_km * 1000), "t = d ÷ c.")],
              "µs", f"A mobile phone signal (microwaves) travels to a mast.\n\n{md_table(['quantity', 'value'], [['distance to mast', f'{d_km} km'], ['speed of EM waves', '3.0 × 10⁸ m/s']])}\n\nHow long does the signal take, in microseconds?",
              "t = d ÷ c", [f"t = {d_km * 1000} ÷ 3.0 × 10⁸ = {sci(d_km * 1000 / C)} s", f"= **{fmt(t)} µs**"],
              ["Convert km to m.", "t = d ÷ c.", "1 s = 10⁶ µs."])


@template("c11x_uv_safe_time", chapter=11, level=1, lo="11d")
def uv_safe_time(rng):
    t0 = nice(rng, 10, 15, 20)
    spf = nice(rng, 15, 20, 30, 50)
    return mk(rng, t0 * spf, [(t0, "Sunscreen multiplies the safe time by its SPF."), (t0 / spf, "Multiply by the SPF, not divide."), (t0 + spf, "Multiply.")],
              "min", f"Ultraviolet radiation from the Sun can damage skin. A sunscreen's sun protection factor (SPF) multiplies the time before the skin burns.\n\n{md_table(['quantity', 'value'], [['time to burn without sunscreen', f'{t0} min'], ['SPF of sunscreen', spf]])}\n\nHow long before the skin burns with the sunscreen (ideally applied)?",
              "protected time = unprotected time × SPF", [f"= {t0} × {spf} = **{t0 * spf} min**"],
              ["What does the SPF do?", "It multiplies the safe time.", "Multiply."], dp=0)


@template("c11x_xray_dose_compare", chapter=11, level=1, lo="11d")
def xray_dose_compare(rng):
    chest = nice(rng, 0.02, 0.05, 0.1)
    ct = nice(rng, 5, 7, 10)
    return mk(rng, ct / chest, [(chest / ct, "The CT scan gives the LARGER dose."), (ct - chest, "Find how many times, so divide."), (ct, "Divide by the chest X-ray dose.")],
              "times", f"X-rays are ionising, so doses are kept low.\n\n{md_table(['scan', 'typical dose / mSv'], [['chest X-ray', fmt(chest)], ['CT scan of the body', ct]])}\n\nHow many chest X-rays give the same dose as one CT scan?",
              "ratio = CT dose ÷ chest X-ray dose", [f"= {ct} ÷ {fmt(chest)} = **{fmt(ct / chest)}**"],
              ["Compare the two doses.", "Divide.", "CT ÷ chest X-ray."])


# ================================================================== L2
@template("c11x_frequency_from_lambda", chapter=11, level=2, lo="11a")
def frequency_from_lambda(rng):
    lam_nm = nice(rng, 400, 500, 600, 700)
    f = C / (lam_nm * 1e-9)
    return mk(rng, f, [(C / lam_nm, "Convert nm to m (× 10⁻⁹)."), (lam_nm * 1e-9 / C, "f = c ÷ λ."), (C / (lam_nm * 1e-6), "1 nm = 10⁻⁹ m, not 10⁻⁶ m.")],
              "Hz", f"{md_table(['quantity', 'value'], [['wavelength of light', f'{lam_nm} nm'], ['speed of light', '3.0 × 10⁸ m/s']])}\n\nWhat is the frequency of the light?",
              "f = c ÷ λ, with λ in m", [f"λ = {lam_nm} × 10⁻⁹ m", f"f = 3.0 × 10⁸ ÷ {sci(lam_nm * 1e-9)} = **{sci(f)} Hz**"],
              ["Convert nm to m.", "f = c ÷ λ.", "Use standard form."])


@template("c11x_sun_light_time", chapter=11, level=2, lo="11a")
def sun_light_time(rng):
    d = nice(rng, 1.5e11, 1.08e11, 2.28e11)
    planet = {1.5e11: "Earth", 1.08e11: "Venus", 2.28e11: "Mars"}[d]
    t = d / C
    return mk(rng, t / 60, [(t, "That is in s; the answer is in minutes."), (d / C / 3600, "Divide by 60, not 3600."), (C / d / 60, "t = d ÷ c.")],
              "min", f"{md_table(['quantity', 'value'], [[f'distance from Sun to {planet}', f'{sci(d)} m'], ['speed of light', '3.0 × 10⁸ m/s']])}\n\nHow long does sunlight take to reach {planet}, in minutes?",
              "t = d ÷ c", [f"t = {sci(d)} ÷ 3.0 × 10⁸ = {fmt(t)} s", f"= **{fmt(t / 60)} min**"],
              ["t = d ÷ c.", "That gives seconds.", "÷ 60 for minutes."])


@template("c11x_same_speed_ratio", chapter=11, level=2, lo="11a")
def same_speed_ratio(rng):
    f1 = nice(rng, 1e8, 2e8)
    k = nice(rng, 10, 100, 1000)
    f2 = f1 * k
    return mk(rng, k, [(1 / k, "The higher-frequency wave has the SHORTER wavelength: λ₁ ÷ λ₂ = f₂ ÷ f₁."), (k * k, "λ ∝ 1/f, not 1/f²."), (1, "Their wavelengths differ even though their speeds are the same.")],
              "times", f"Two EM waves travel in a vacuum.\n\n{md_table(['wave', 'frequency / Hz'], [['A', sci(f1)], ['B', sci(f2)]])}\n\nHow many times longer is the wavelength of A than that of B?",
              "same speed c: λ ∝ 1/f → λ_A ÷ λ_B = f_B ÷ f_A", [f"ratio = {sci(f2)} ÷ {sci(f1)} = **{fmt(k)}**"],
              ["All EM waves have the same speed.", "So f × λ is the same.", "Ratio of frequencies."])


@template("c11x_hidden_region", chapter=11, level=2, lo="11b")
def hidden_region(rng):
    i = rng.randrange(1, 6)
    names = [n for n, _, _ in REGIONS]
    ans = names[i]
    wrongs = {names[i - 1]: "That is the region on one side of P.", names[i + 1]: "That is the region on the other side of P.", names[(i + 3) % 7]: "That region is elsewhere in the spectrum."}
    return mkt(rng, ans, wrongs, "Fig. 1 shows the electromagnetic spectrum with one region hidden as P. Which region is P?",
               "radio, microwaves, infrared, visible, UV, X-rays, gamma", [f"P lies between {names[i - 1]} and {names[i + 1]} → **{ans}**"],
               ["Recall the order.", "Look at the neighbours.", "Fill the gap."], figure=sketches.em_spectrum(hidden=[ans]))


@template("c11x_wifi_wavelength", chapter=11, level=2, lo="11c")
def wifi_wavelength(rng):
    f = nice(rng, 2.4e9, 5.0e9)
    lam = C / f * 100
    return mk(rng, lam, [(C / f, "Convert to cm."), (f / C * 100, "λ = c ÷ f."), (lam / 10, "Check the powers of ten.")],
              "cm", f"Wi-Fi routers use microwaves.\n\n{md_table(['quantity', 'value'], [['frequency', f'{sci(f)} Hz'], ['speed of EM waves', '3.0 × 10⁸ m/s']])}\n\nWhat is the wavelength in cm?",
              "λ = c ÷ f", [f"λ = 3.0 × 10⁸ ÷ {sci(f)} = {fmt(C / f)} m = **{fmt(lam)} cm**"],
              ["λ = c ÷ f.", "Use standard form.", "Convert m to cm."])


@template("c11x_radar_distance", chapter=11, level=2, lo="11c")
def radar_distance(rng):
    t_us = nice(rng, 20, 40, 100, 200)
    d = C * t_us * 1e-6 / 2 / 1000
    return mk(rng, d, [(C * t_us * 1e-6 / 1000, "The pulse goes there AND back: halve."), (C * t_us / 2 / 1000, "Convert µs to s."), (d * 1000, "The answer is in km.")],
              "km", f"Air traffic control radar sends out microwave pulses.\n\n{md_table(['quantity', 'value'], [['time for reflected pulse to return', f'{t_us} µs'], ['speed of microwaves', '3.0 × 10⁸ m/s']])}\n\nHow far away is the aircraft, in km?",
              "d = c t ÷ 2", [f"d = 3.0 × 10⁸ × {t_us} × 10⁻⁶ ÷ 2 = {fmt(d * 1000)} m", f"= **{fmt(d)} km**"],
              ["Radar works by echoes.", "Halve the round trip.", "Convert to km."])


@template("c11x_remote_control_lambda", chapter=11, level=2, lo="11c")
def remote_control_lambda(rng):
    lam_nm = nice(rng, 850, 940, 950)
    f = C / (lam_nm * 1e-9)
    return mk(rng, f, [(C / lam_nm, "Convert nm to m."), (lam_nm * 1e-9 * C, "f = c ÷ λ."), (f / 1000, "Check the powers of ten.")],
              "Hz", f"A TV remote control emits infrared.\n\n{md_table(['quantity', 'value'], [['wavelength', f'{lam_nm} nm'], ['speed of EM waves', '3.0 × 10⁸ m/s']])}\n\nWhat is its frequency?",
              "f = c ÷ λ", [f"f = 3.0 × 10⁸ ÷ {sci(lam_nm * 1e-9)} = **{sci(f)} Hz**"],
              ["Convert nm to m.", "f = c ÷ λ.", "Standard form."])


@template("c11x_radiographer_dose", chapter=11, level=2, lo="11d")
def radiographer_dose(rng):
    per = nice(rng, 0.001, 0.002, 0.005)
    n = nice(rng, 20, 30, 40)
    days = nice(rng, 200, 250)
    return mk(rng, per * n * days, [(per * n, "Multiply by the number of working days too."), (per * days, "Multiply by the number of scans per day too."), (per * n * days * 1000, "Keep mSv.")],
              "mSv", f"A radiographer stands behind a lead screen but still receives a tiny dose from each scan.\n\n{md_table(['quantity', 'value'], [['dose per scan', f'{fmt(per)} mSv'], ['scans per day', n], ['working days per year', days]])}\n\nWhat is the radiographer's yearly dose?",
              "yearly dose = dose per scan × scans per day × days", [f"= {fmt(per)} × {n} × {days} = **{fmt(per * n * days)} mSv**"],
              ["Find the daily dose.", "Multiply by the number of days.", "Units: mSv."])


@template("c11x_uv_index_time", chapter=11, level=2, lo="11d")
def uv_index_time(rng):
    rows = [(3, 60), (6, 30), (9, 20), (12, 15)]
    idx, t = rng.choice(rows)
    k = nice(rng, 2, 3)
    return mk(rng, t / k, [(t * k, "More UV → LESS safe time."), (t, "That is the safe time at this index for normal skin."), (t - k, "Divide by the factor.")],
              "min", f"The UV index measures the strength of the Sun's ultraviolet. A person with very fair skin burns **{k} times** faster than average.\n\n{md_table(['UV index', 'time to burn for average skin / min'], rows)}\n\nOn a day with UV index **{idx}**, how long before the fair-skinned person burns?",
              "time = average time ÷ factor", [f"average at index {idx}: {t} min", f"fair skin: {t} ÷ {k} = **{fmt(t / k)} min**"],
              ["Read the time at this UV index.", "The person burns faster.", "Divide by the factor."])


# ================================================================== L3
@template("c11x_region_from_frequency", chapter=11, level=3, lo="11b")
def region_from_frequency(rng):
    f, ans = rng.choice([(6e14, "visible light"), (3e13, "infrared"), (1e10, "microwaves"), (1e18, "X-rays"), (1e16, "ultraviolet"), (1e6, "radio waves")])
    lam = C / f
    others = [n for n, _, _ in REGIONS if n != ans]
    rng.shuffle(others)
    wrongs = {n: f"Find λ = c ÷ f first: λ = {sci(lam)} m, which is not in the {n} range." for n in others[:3]}
    table = md_table(["region", "wavelength range / m"], [[n, f"{sci(lo)} to {sci(hi)}"] for n, lo, hi in REGIONS])
    return mkt(rng, ans, wrongs, f"{table}\n\nAn EM wave has a frequency of **{sci(f)} Hz**. Which region is it in?",
               "λ = c ÷ f, then match the range", [f"λ = 3.0 × 10⁸ ÷ {sci(f)} = {sci(lam)} m → **{ans}**"],
               ["Convert frequency to wavelength.", "λ = c ÷ f.", "Match to the table."])


@template("c11x_wavelength_ratio_regions", chapter=11, level=3, lo="11b")
def wavelength_ratio_regions(rng):
    lam_r = nice(rng, 1.0, 3.0)
    lam_x = nice(rng, 1e-10, 3e-10)
    ratio = lam_r / lam_x
    return mk(rng, ratio, [(lam_x / lam_r, "Radio waves are LONGER; divide radio by X-ray."), (lam_r - lam_x, "Find the ratio."), (ratio / 1000, "Check the powers of ten.")],
              "times", f"{md_table(['wave', 'wavelength / m'], [['radio wave', fmt(lam_r)], ['X-ray', sci(lam_x)]])}\n\nHow many times longer is the radio wave's wavelength?",
              "ratio = λ_radio ÷ λ_X-ray", [f"= {fmt(lam_r)} ÷ {sci(lam_x)} = **{sci(ratio)}**"],
              ["Divide the two wavelengths.", "Use standard form.", "Radio ÷ X-ray."])


@template("c11x_order_three_frequencies", chapter=11, level=3, lo="11b")
def order_three_frequencies(rng):
    waves = [("P", 5e14), ("Q", 1e9), ("R", 1e17)]
    rng.shuffle(waves)
    order = [n for n, f in sorted(waves, key=lambda w: w[1])]
    ans = ", ".join(order)
    wrongs = {", ".join(reversed(order)): "That is from shortest to longest wavelength... check: low frequency = long wavelength.",
              ", ".join(n for n, _ in waves): "That is the table order; sort by frequency.",
              ", ".join(order[1:] + order[:1]): "Sort by frequency, lowest first."}
    wrongs = {k: v for k, v in wrongs.items() if k != ans}
    if len(wrongs) < 3:
        wrongs[", ".join([order[1], order[0], order[2]])] = "Sort by frequency, lowest first."
    table = md_table(["wave", "frequency / Hz"], [[n, sci(f)] for n, f in waves])
    return mkt(rng, ans, dict(list(wrongs.items())[:3]), f"{table}\n\nWhich list gives the waves in order of DECREASING wavelength?",
               "decreasing wavelength = increasing frequency", [f"increasing frequency: **{ans}**"],
               ["Long wavelength = low frequency.", "Sort by frequency, lowest first.", "That is decreasing wavelength."])


@template("c11x_satellite_tv_delay", chapter=11, level=3, lo="11c")
def satellite_tv_delay(rng):
    h = nice(rng, 3.6e7, 3.58e7)
    t = 2 * h / C
    return mk(rng, t, [(h / C, "The signal goes UP to the satellite and back DOWN."), (4 * h / C, "Up and down once each."), (2 * h * C, "t = distance ÷ c.")],
              "s", f"A TV signal is sent from a ground station up to a geostationary satellite and back down to a home.\n\n{md_table(['quantity', 'value'], [['height of satellite', f'{sci(h)} m'], ['speed of microwaves', '3.0 × 10⁸ m/s']])}\n\nWhat is the minimum delay? (Treat both paths as vertical.)",
              "t = 2h ÷ c", [f"t = 2 × {sci(h)} ÷ 3.0 × 10⁸ = **{fmt(t)} s**"],
              ["Up and down.", "Total distance 2h.", "t = d ÷ c."])


@template("c11x_gps_distance", chapter=11, level=3, lo="11c")
def gps_distance(rng):
    t_ms = nice(rng, 67, 70, 72, 75)
    d = C * t_ms / 1000 / 1000
    return mk(rng, d, [(C * t_ms / 1000, "That is in m; the answer is in km."), (C * t_ms / 1000 / 2 / 1000, "GPS signals travel ONE way."), (C * t_ms / 1000 / 1e6, "Check the conversion to km.")],
              "km", f"A GPS receiver measures how long a satellite's radio signal took to arrive.\n\n{md_table(['quantity', 'value'], [['travel time', f'{t_ms} ms'], ['speed of EM waves', '3.0 × 10⁸ m/s']])}\n\nHow far away is the satellite, in km?",
              "d = c t (one way)", [f"d = 3.0 × 10⁸ × {t_ms} × 10⁻³ = {sci(C * t_ms / 1000)} m", f"= **{fmt(d)} km**"],
              ["Convert ms to s.", "d = c t (no echo).", "Convert to km."])


@template("c11x_fibre_signal_time", chapter=11, level=3, lo="11c")
def fibre_signal_time(rng):
    L_km = nice(rng, 50, 100, 200)
    v = 2.0e8
    t = L_km * 1000 / v * 1000
    return mk(rng, t, [(L_km * 1000 / C * 1000, "Light travels SLOWER in glass: use 2.0 × 10⁸ m/s."), (t / 1000, "That is in s; the answer is in ms."), (L_km / v * 1000, "Convert km to m.")],
              "ms", f"Infrared signals travel along an optical fibre.\n\n{md_table(['quantity', 'value'], [['length of fibre', f'{L_km} km'], ['speed of light in the glass', '2.0 × 10⁸ m/s']])}\n\nHow long does a signal take, in ms?",
              "t = L ÷ v (speed in glass)", [f"t = {L_km * 1000} ÷ 2.0 × 10⁸ = {sci(L_km * 1000 / v)} s", f"= **{fmt(t)} ms**"],
              ["Use the speed in glass.", "Convert km to m.", "t = L ÷ v; convert to ms."])


@template("c11x_microwave_leak", chapter=11, level=3, lo="11d")
def microwave_leak(rng):
    P_in = nice(rng, 800, 1000, 1200)
    frac = nice(rng, 1e-6, 2e-6, 5e-6)
    P_leak = P_in * frac * 1000
    return mk(rng, P_leak, [(P_in * frac, "That is in W; the answer is in mW."), (P_in / frac, "Multiply by the fraction."), (P_leak / 1000, "Convert to mW.")],
              "mW", f"The metal case of a microwave oven keeps almost all the microwaves inside.\n\n{md_table(['quantity', 'value'], [['microwave power inside', f'{P_in} W'], ['fraction leaking out', sci(frac)]])}\n\nWhat power leaks out, in mW?",
              "P_leak = fraction × P", [f"= {sci(frac)} × {P_in} = {sci(P_in * frac)} W = **{fmt(P_leak)} mW**"],
              ["Multiply power by the fraction.", "Use standard form.", "1 W = 1000 mW."])


@template("c11x_dose_background", chapter=11, level=3, lo="11d")
def dose_background(rng):
    bg = nice(rng, 2.4, 3.0)
    scan = nice(rng, 0.1, 0.4, 1.0)
    days = scan / bg * 365
    return mk(rng, days, [(scan / bg, "That is in years; convert to days."), (bg / scan * 365, "Divide the scan dose by the yearly background."), (scan * 365, "Divide by the background dose per year first.")],
              "days", f"Doses from medical scans are compared with natural background radiation.\n\n{md_table(['quantity', 'value'], [['background dose per year', f'{fmt(bg)} mSv'], ['dose from one scan', f'{fmt(scan)} mSv']])}\n\nThe scan dose equals how many days of background radiation?",
              "days = scan ÷ (background per year) × 365", [f"= {fmt(scan)} ÷ {fmt(bg)} × 365 = **{fmt(days)} days**"],
              ["Find what fraction of a year's dose the scan is.", "Multiply by 365.", "Answer in days."])


# ================================================================== L4
@template("c11x_light_year", chapter=11, level=4, lo="11a")
def light_year(rng):
    yrs = nice(rng, 1, 4.2, 8.6)
    d = C * yrs * 365 * 24 * 3600
    return mk(rng, d, [(C * yrs * 365 * 24, "Convert years to SECONDS (× 3600 too)."), (C * yrs, "Convert the time to seconds."), (d / 1000, "The answer is in m.")],
              "m", f"Light from a star takes **{fmt(yrs)} years** to reach Earth.\n\n{md_table(['quantity', 'value'], [['speed of light', '3.0 × 10⁸ m/s'], ['1 year', '365 days']])}\n\nHow far away is the star?",
              "d = c t, t in seconds", [f"t = {fmt(yrs)} × 365 × 24 × 3600 = {sci(yrs * 365 * 24 * 3600)} s", f"d = **{sci(d)} m**"],
              ["Convert years to seconds.", "d = c t.", "Standard form."])


@template("c11x_radio_band_range", chapter=11, level=4, lo="11b")
def radio_band_range(rng):
    f_lo, f_hi = rng.choice([(88e6, 108e6), (0.5e6, 1.6e6), (470e6, 790e6)])
    lam_short = C / f_hi
    return mk(rng, lam_short, [(C / f_lo, "That is the LONGEST wavelength (lowest frequency)."), (f_hi / C, "λ = c ÷ f."), ((C / f_lo + C / f_hi) / 2, "Use the highest frequency for the shortest wavelength.")],
              "m", f"A radio band covers the frequencies shown.\n\n{md_table(['quantity', 'value'], [['lowest frequency', f'{sci(f_lo)} Hz'], ['highest frequency', f'{sci(f_hi)} Hz'], ['speed of EM waves', '3.0 × 10⁸ m/s']])}\n\nWhat is the SHORTEST wavelength in this band?",
              "shortest λ ↔ highest f: λ = c ÷ f_max", [f"λ = 3.0 × 10⁸ ÷ {sci(f_hi)} = **{fmt(lam_short)} m**"],
              ["Which frequency gives the shortest λ?", "The highest.", "λ = c ÷ f."])


@template("c11x_visible_range_f", chapter=11, level=4, lo="11b")
def visible_range_f(rng):
    which = rng.choice(["red (700 nm)", "violet (400 nm)"])
    lam = 700e-9 if "red" in which else 400e-9
    f = C / lam
    other = C / (400e-9 if "red" in which else 700e-9)
    return mk(rng, f, [(other, "That is the frequency at the OTHER end of the visible spectrum."), (C / (lam * 1e9), "Convert nm to m correctly (× 10⁻⁹)."), (f / 10, "Check the powers of ten.")],
              "Hz", f"{md_table(['colour', 'wavelength / nm'], [['red end', 700], ['violet end', 400]])}\n\nWhat is the frequency of **{which}** light? (c = 3.0 × 10⁸ m/s)",
              "f = c ÷ λ", [f"f = 3.0 × 10⁸ ÷ {sci(lam)} = **{sci(f)} Hz**"],
              ["Convert nm to m.", "f = c ÷ λ.", "Standard form."])


@template("c11x_phone_mast_power", chapter=11, level=4, lo="11c")
def phone_mast_power(rng):
    P = nice(rng, 20, 40, 50)
    A = nice(rng, 2.0, 4.0)
    d1, d2 = nice(rng, 10, 20), nice(rng, 40, 60, 80)
    I1 = P / (4 * 3.14 * d1 ** 2)
    ratio = (d2 / d1) ** 2
    return mk(rng, ratio, [(d2 / d1, "Intensity falls with distance SQUARED."), (1 / ratio, "The nearer point has the HIGHER intensity."), (ratio * 2, "Square the distance ratio.")],
              "times", f"The intensity of microwaves from a phone mast falls with the square of the distance (I ∝ 1/d²).\n\n{md_table(['position', 'distance from mast / m'], [['A', d1], ['B', d2]])}\n\nHow many times greater is the intensity at A than at B?",
              "I ∝ 1/d² → I_A ÷ I_B = (d_B ÷ d_A)²", [f"({d2} ÷ {d1})² = **{fmt(ratio)}**"],
              ["Intensity ∝ 1/d².", "Find the distance ratio.", "Square it."])


@template("c11x_uv_dose_distance", chapter=11, level=4, lo="11d")
def uv_dose_distance(rng):
    t1 = nice(rng, 10, 15)
    d1 = nice(rng, 1.0)
    d2 = nice(rng, 2.0, 3.0)
    t2 = t1 * (d2 / d1) ** 2
    return mk(rng, t2, [(t1 * d2 / d1, "Intensity ∝ 1/d², so time scales with d²."), (t1 / (d2 / d1) ** 2, "Further away → LONGER safe time."), (t1, "The safe time changes with distance.")],
              "min", f"A UV lamp in a laboratory. Its intensity follows I ∝ 1/d², and the safe exposure time is inversely proportional to intensity.\n\n{md_table(['distance from lamp / m', 'safe exposure time / min'], [[fmt(d1), t1], [fmt(d2), '?']])}\n\nWhat is the safe exposure time at the larger distance?",
              "t ∝ 1/I ∝ d²", [f"factor = ({fmt(d2)} ÷ {fmt(d1)})² = {fmt((d2 / d1) ** 2)}", f"t = {t1} × {fmt((d2 / d1) ** 2)} = **{fmt(t2)} min**"],
              ["Intensity falls as 1/d².", "Safe time ∝ 1/intensity.", "Multiply by the distance ratio squared."])


@template("c11x_xray_shield", chapter=11, level=4, lo="11d")
def xray_shield(rng):
    I0 = nice(rng, 800, 1000, 1600)
    n = nice(rng, 2, 3, 4)
    I = I0 / 2 ** n
    return mk(rng, I, [(I0 / (2 * n), "Each layer HALVES the intensity: divide by 2 each time."), (I0 / 2, "Apply the halving for every layer."), (I0 * 2 ** -1 * n, "Halve repeatedly.")],
              "units", f"Each 0.25 mm of lead halves the intensity of an X-ray beam.\n\n{md_table(['quantity', 'value'], [['intensity with no lead', f'{I0} units'], ['thickness of lead', f'{fmt(0.25 * n)} mm']])}\n\nWhat is the intensity after passing through the lead?",
              "I = I₀ ÷ 2ⁿ, n = number of halving thicknesses", [f"n = {fmt(0.25 * n)} ÷ 0.25 = {n}", f"I = {I0} ÷ 2^{n} = **{fmt(I)} units**"],
              ["How many halving thicknesses?", "Halve that many times.", "I₀ ÷ 2ⁿ."])


@template("c11x_sunbed_total", chapter=11, level=4, lo="11d")
def sunbed_total(rng):
    per = nice(rng, 10, 12, 15)
    n = nice(rng, 8, 10, 12)
    over = nice(rng, 20, 30, 40)
    limit = per * n - over
    return mk(rng, over, [(per * n, "Find how far ABOVE the limit."), (limit, "That is the limit; subtract it from the total."), (per + n, "Multiply sessions by time per session first.")],
              "min", f"Over-exposure to ultraviolet increases the risk of skin cancer. A sunbed user exceeds a recommended monthly limit.\n\n{md_table(['quantity', 'value'], [['minutes per session', per], ['sessions per month', n], ['recommended limit per month', f'{limit} min']])}\n\nBy how many minutes is the limit exceeded?",
              "excess = sessions × time − limit", [f"total = {per} × {n} = {per * n} min", f"excess = {per * n} − {limit} = **{over} min**"],
              ["Find the total time.", "Compare with the limit.", "Subtract."], dp=0)


# ================================================================== L5
@template("c11x_radio_delay_mars", chapter=11, level=5, lo="11a")
def radio_delay_mars(rng):
    d_lo, d_hi = 5.5e10, 4.0e11
    which = rng.choice(["closest", "furthest"])
    d = d_lo if which == "closest" else d_hi
    t_round = 2 * d / C / 60
    return mk(rng, t_round, [(d / C / 60, "A command and its reply make a ROUND trip."), (2 * d / C, "That is in seconds; convert to minutes."), (2 * (d_hi if which == 'closest' else d_lo) / C / 60, "Use the distance for the position asked.")],
              "min", f"Engineers send a radio command to a rover on Mars and wait for its reply.\n\n{md_table(['position', 'Earth–Mars distance / m'], [['closest', sci(d_lo)], ['furthest', sci(d_hi)]])}\n\nWhat is the shortest time to get a reply when Mars is at its **{which}**? (c = 3.0 × 10⁸ m/s)",
              "round trip t = 2d ÷ c", [f"t = 2 × {sci(d)} ÷ 3.0 × 10⁸ = {fmt(2 * d / C)} s", f"= **{fmt(t_round)} min**"],
              ["Command out, reply back.", "t = 2d ÷ c.", "Convert to minutes."])


@template("c11x_spectrum_wavelength_span", chapter=11, level=5, lo="11b")
def spectrum_wavelength_span(rng):
    f = nice(rng, 7.5e14, 6.0e14)
    f2 = nice(rng, 4.0e14, 4.3e14)
    dl = (C / f2 - C / f) * 1e9
    return mk(rng, dl, [(C / f2 * 1e9, "Find the DIFFERENCE between the two wavelengths."), ((C / f - C / f2) * 1e9, "Subtract the shorter from the longer."), (dl / 1e9, "Convert to nm.")],
              "nm", f"Visible light spans the frequencies shown.\n\n{md_table(['end of visible spectrum', 'frequency / Hz'], [['violet', sci(f)], ['red', sci(f2)]])}\n\nWhat is the width of the visible spectrum in wavelength, in nm? (c = 3.0 × 10⁸ m/s)",
              "λ = c ÷ f at each end; subtract", [f"violet: {fmt(C / f * 1e9)} nm; red: {fmt(C / f2 * 1e9)} nm", f"width = **{fmt(dl)} nm**"],
              ["Find λ at each end.", "Convert to nm.", "Subtract."])


@template("c11x_two_band_ratio", chapter=11, level=5, lo="11b")
def two_band_ratio(rng):
    lam_ir = nice(rng, 1e-5, 2e-5)
    lam_uv = nice(rng, 1e-7, 2e-7)
    ratio = lam_ir / lam_uv
    return mk(rng, ratio, [(1 / ratio, "UV has the HIGHER frequency, so f_UV ÷ f_IR > 1."), (ratio ** 2, "f ∝ 1/λ, not 1/λ²."), (lam_ir - lam_uv, "Find a ratio.")],
              "times", f"{md_table(['radiation', 'wavelength / m'], [['infrared', sci(lam_ir)], ['ultraviolet', sci(lam_uv)]])}\n\nHow many times greater is the frequency of the ultraviolet than that of the infrared?",
              "same c: f ∝ 1/λ → f_UV ÷ f_IR = λ_IR ÷ λ_UV", [f"= {sci(lam_ir)} ÷ {sci(lam_uv)} = **{fmt(ratio)}**"],
              ["Same speed for both.", "f × λ is constant.", "Ratio of wavelengths, inverted."])


@template("c11x_thermal_camera_peak", chapter=11, level=5, lo="11c")
def thermal_camera_peak(rng):
    T_c = nice(rng, 27, 37, 127)
    T = T_c + 273
    lam_peak = 2.9e-3 / T * 1e6
    return mk(rng, lam_peak, [(2.9e-3 / T_c * 1e6, "Use the temperature in KELVIN (θ + 273)."), (lam_peak / 1e6, "That is in m; the answer is in µm."), (2.9e-3 * T * 1e6, "λ = 2.9 × 10⁻³ ÷ T.")],
              "µm", f"A thermal imaging camera detects infrared. The wavelength at which a warm body emits most strongly is λ = (2.9 × 10⁻³ m K) ÷ T, where T is in kelvin (T = θ + 273).\n\n{md_table(['quantity', 'value'], [['temperature of object', f'{T_c} °C']])}\n\nAt what wavelength does it emit most strongly, in µm?",
              "T = θ + 273; λ = 2.9 × 10⁻³ ÷ T", [f"T = {T} K", f"λ = 2.9 × 10⁻³ ÷ {T} = {sci(2.9e-3 / T)} m = **{fmt(lam_peak)} µm**"],
              ["Convert to kelvin.", "Use the formula given.", "Convert m to µm (× 10⁶)."])


@template("c11x_satellite_phone_call", chapter=11, level=5, lo="11c")
def satellite_phone_call(rng):
    h = 3.6e7
    hops = nice(rng, 1, 2)
    t = 2 * h * hops / C
    reply = 2 * t
    return mk(rng, reply, [(t, "That is one way; a reply needs the signal to go and come back."), (h / C, "Each hop is up AND down."), (reply * 2, "Count the hops carefully.")],
              "s", f"A phone call between two continents is routed through **{hops}** geostationary satellite hop(s); each hop goes up to the satellite and down again.\n\n{md_table(['quantity', 'value'], [['height of satellite', '3.6 × 10⁷ m'], ['speed of microwaves', '3.0 × 10⁸ m/s']])}\n\nWhat is the minimum time between speaking and hearing the other person's immediate reply?",
              "one way = hops × 2h ÷ c; reply = 2 × one way", [f"one way = {hops} × 2 × 3.6 × 10⁷ ÷ 3.0 × 10⁸ = {fmt(t)} s", f"reply delay = **{fmt(reply)} s**"],
              ["Each hop: up and down.", "Your words go; the reply comes back.", "Double the one-way time."])


@template("c11x_microwave_oven_heating", chapter=11, level=5, lo="11c")
def microwave_oven_heating(rng):
    P = nice(rng, 700, 800, 900)
    eff = nice(rng, 0.6, 0.7)
    m = nice(rng, 0.25, 0.3)
    dT = nice(rng, 40, 50, 60)
    t = m * 4200 * dT / (P * eff)
    return mk(rng, t, [(m * 4200 * dT / P, "Only a fraction of the microwave power reaches the water."), (m * 4200 * dT * P * eff, "t = Q ÷ (useful power)."), (m * dT / (P * eff), "Q = m c Δθ with c = 4200.")],
              "s", f"A microwave oven heats a cup of water.\n\n{md_table(['quantity', 'value'], [['microwave power output', f'{P} W'], ['fraction absorbed by the water', f'{eff:g}'], ['mass of water', f'{fmt(m)} kg'], ['temperature rise', f'{dT} °C'], ['c (water)', '4200 J/(kg K)']])}\n\nHow long does this take?",
              "Q = m c Δθ; t = Q ÷ (fraction × P)", [f"Q = {fmt(m)} × 4200 × {dT} = {fmt(m * 4200 * dT)} J", f"useful power = {eff:g} × {P} = {fmt(P * eff)} W", f"t = **{fmt(t)} s**"],
              ["Find the energy needed.", "Find the useful power.", "t = Q ÷ P."])


@template("c11x_gamma_sterilise", chapter=11, level=5, lo="11d")
def gamma_sterilise(rng):
    rate = nice(rng, 2, 4, 5)
    need = nice(rng, 25, 30, 40)
    t = need / rate
    return mk(rng, t, [(need * rate, "Time = dose needed ÷ dose rate."), (rate / need, "Dose needed goes on top."), (t * 60, "The answer is in hours.")],
              "h", f"Gamma rays are used to sterilise medical equipment because they kill bacteria.\n\n{md_table(['quantity', 'value'], [['dose rate in the chamber', f'{rate} kGy per hour'], ['dose needed to sterilise', f'{need} kGy']])}\n\nHow long must the equipment stay in the chamber?",
              "t = dose ÷ dose rate", [f"t = {need} ÷ {rate} = **{fmt(t)} h**"],
              ["What is the dose rate?", "Dose needed ÷ rate.", "Answer in hours."])


@template("c11x_mobile_sar", chapter=11, level=5, lo="11d")
def mobile_sar(rng):
    sar = nice(rng, 0.8, 1.2, 1.5)
    m = nice(rng, 0.01)
    t = nice(rng, 600, 1200, 1800)
    E = sar * m * t
    return mk(rng, E, [(sar * t, "Multiply by the mass of tissue too."), (sar * m, "Multiply by the time too."), (E * 1000, "Keep joules.")],
              "J", f"The specific absorption rate (SAR) of a phone is the microwave power absorbed per kilogram of tissue.\n\n{md_table(['quantity', 'value'], [['SAR', f'{fmt(sar)} W/kg'], ['mass of tissue near the ear', f'{fmt(m)} kg'], ['length of call', f'{t} s']])}\n\nHow much microwave energy does this tissue absorb during the call?",
              "P = SAR × m; E = P t", [f"P = {fmt(sar)} × {fmt(m)} = {fmt(sar * m)} W", f"E = {fmt(sar * m)} × {t} = **{fmt(E)} J**"],
              ["Find the power absorbed.", "SAR × mass.", "E = P t."])


@template("c11x_lead_thickness_needed", chapter=11, level=5, lo="11d")
def lead_thickness_needed(rng):
    half = nice(rng, 0.25, 0.3, 0.5)
    n = nice(rng, 3, 4, 5)
    I0 = nice(rng, 1600, 3200)
    I = I0 / 2 ** n
    return mk(rng, n * half, [(half * I0 / I / 2, "Count HALVINGS: 2ⁿ = I₀ ÷ I, so n = number of halvings."), (half, "That is only one halving thickness."), ((n - 1) * half, "Count the halvings carefully.")],
              "mm", f"An X-ray room wall must reduce the beam intensity. Each **{fmt(half)} mm** of lead halves the intensity.\n\n{md_table(['quantity', 'value'], [['intensity of beam', f'{I0} units'], ['maximum safe intensity outside', f'{fmt(I)} units']])}\n\nWhat thickness of lead is needed?",
              "I₀ ÷ I = 2ⁿ; thickness = n × halving thickness", [f"{I0} ÷ {fmt(I)} = {2 ** n} = 2^{n} → n = {n}", f"thickness = {n} × {fmt(half)} = **{fmt(n * half)} mm**"],
              ["How many times must the intensity halve?", "Find n from 2ⁿ.", "Multiply by the halving thickness."])
