"""Chapter 11 Electromagnetic Spectrum (6091 additions): speed of light and time, ordering by wavelength, frequency ratios,
satellite delays, microwave wavelength."""
import math

from .. import sketches
from .base import fmt, md_table, nice, numeric_options, template, text_options

C = 3.0e8


def _sci(x):
    e = int(math.floor(math.log10(abs(x))))
    mant = x / 10 ** e
    sup = str(e).replace("-", "⁻").translate(str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹"))
    return f"{fmt(mant, sf=2)} × 10{sup}"


@template("c11_light_travel_time", chapter=11, level=1, lo="11a")
def light_travel_time(rng):
    d_km, place = rng.choice([(384000, "the Moon"), (150000000, "the Sun"), (36000, "a geostationary satellite"), (3000, "a city 3000 km away")])
    d = d_km * 1000
    t = d / C
    opts, key, mis = numeric_options(rng, t, [
        (d_km / C, "You left the distance in kilometres. Convert to metres (× 1000) so the units match m/s."),
        (t * 2, "That is the time for a round trip there and back; the question asks for one way."),
        (C / d, "You divided the wrong way round: time = distance ÷ speed."),
    ], unit="s", sf=3)
    table = md_table(["quantity", "value"], [["distance to " + place, f"{_sci(d)} m"], ["speed of light", "3.0 × 10⁸ m/s"]])
    return dict(
        stem=f"Light (and every other electromagnetic wave) travels through space at 3.0 × 10⁸ m/s.\n\n{table}\n\nHow long does light take to reach us from {place}?",
        options=opts, key=key, misconceptions=mis,
        formula="time = distance ÷ speed",
        working=["t = d ÷ v", f"= {_sci(d)} ÷ (3.0 × 10⁸)", f"= **{fmt(t, sf=3)} s**"],
        hints=[
            "Speed = distance ÷ time. Rearrange for the time.",
            "Make sure the distance is in metres before dividing by a speed in m/s.",
            f"t = {_sci(d)} ÷ 3.0 × 10⁸.",
        ],
    )


@template("c11_region_from_wavelength_table", chapter=11, level=2, lo="11b")
def region_from_wavelength_table(rng):
    waves = [("P", 1e-10, "X-rays"), ("Q", 5e-7, "visible light"), ("R", 1e-5, "infrared"), ("S", 0.1, "microwaves")]
    ask = rng.choice(["has the highest frequency", "is visible light", "has the longest wavelength", "is infrared"])
    ans = {"has the highest frequency": "P", "is visible light": "Q", "has the longest wavelength": "S", "is infrared": "R"}[ask]
    region = {w[0]: w[2] for w in waves}
    wrongs = {w: f"Wave {w} has a wavelength of {_sci(l)} m, which puts it in the {r} region." for w, l, r in waves if w != ans}
    opts, key, mis = text_options(rng, ans, wrongs)
    rows = [[w, f"{_sci(l)}"] for w, l, _ in waves]
    rng.shuffle(rows)
    table = md_table(["wave", "wavelength / m"], rows)
    return dict(
        stem=f"The table gives the wavelengths of four electromagnetic waves in a vacuum.\n\n{table}\n\nWhich wave **{ask}**?",
        options=opts, key=key, misconceptions=mis,
        formula="all EM waves have the same speed, so the shortest wavelength has the highest frequency (v = f λ); visible light is about 4 × 10⁻⁷ to 7 × 10⁻⁷ m",
        working=["order by wavelength: P (10⁻¹⁰ m, X-rays) < Q (5 × 10⁻⁷ m, visible) < R (10⁻⁵ m, infrared) < S (0.1 m, microwaves)", f"the wave that {ask} is **{ans}** ({region[ans]})"],
        hints=[
            "Put the four wavelengths in order from shortest to longest.",
            "Shortest wavelength = highest frequency (same speed for all EM waves). Visible light is around half a micrometre (5 × 10⁻⁷ m).",
            "Match the order to the spectrum: X-rays, visible, infrared, microwaves.",
        ],
    )


@template("c11_frequency_ratio", chapter=11, level=3, lo="11a")
def frequency_ratio(rng):
    l1, l2 = rng.choice([(1.0, 0.25), (3.0, 0.5), (0.6, 0.12), (2.0, 0.4), (1.5, 0.3)])
    ratio = l1 / l2
    opts, key, mis = numeric_options(rng, ratio, [
        (l2 / l1, "You have the ratio upside down. The shorter wavelength has the HIGHER frequency, so the ratio f₂/f₁ is greater than 1."),
        (l1 - l2, "You subtracted the wavelengths. Frequencies are inversely proportional to wavelength: f = v ÷ λ."),
        (ratio * ratio, "Frequency ∝ 1/λ, not 1/λ²."),
    ], unit="", sf=3)
    table = md_table(["wave", "wavelength / m", "speed / m/s"], [["1", fmt(l1), "3.0 × 10⁸"], ["2", fmt(l2), "3.0 × 10⁸"]])
    return dict(
        stem=f"Two radio waves travel through air at the same speed.\n\n{table}\n\nHow many times greater is the frequency of wave 2 than the frequency of wave 1?",
        options=opts, key=key, misconceptions=mis,
        formula="v = f λ with the same v: f₂ / f₁ = λ₁ / λ₂",
        working=[f"f₁ = v ÷ {fmt(l1)}, f₂ = v ÷ {fmt(l2)}", f"f₂ ÷ f₁ = {fmt(l1)} ÷ {fmt(l2)}", f"= **{fmt(ratio, sf=3)}**"],
        hints=[
            "Same speed, so f = v ÷ λ for each wave. Which wave has the larger frequency?",
            "Dividing the two expressions, v cancels: f₂/f₁ = λ₁/λ₂.",
            f"{fmt(l1)} ÷ {fmt(l2)} = ?",
        ],
    )


@template("c11_satellite_round_trip", chapter=11, level=4, lo="11c")
def satellite_round_trip(rng):
    h_km = nice(rng, 36000, 35800, 20000, 1200)
    d = 2 * h_km * 1000
    t = d / C
    opts, key, mis = numeric_options(rng, t, [
        (t / 2, "That is the time for the signal to go up only. It must come back down to the second dish as well."),
        (2 * h_km / C, "You left the height in km. Convert to metres."),
        (t * 1000, "Check the powers of ten: the answer is a fraction of a second."),
    ], unit="s", sf=3)
    return dict(
        stem=f"A television signal (microwaves) is sent from a ground station up to a satellite **{h_km} km** above the Earth and straight back down to a dish nearby, as shown in Fig. 1. How long does the round trip take? (speed = 3.0 × 10⁸ m/s)",
        figure=sketches.echo_sketch(f"{h_km} km", "signal up and back", left="dish", right="satellite"),
        options=opts, key=key, misconceptions=mis,
        formula="total distance = 2 × height (up and down); time = distance ÷ speed",
        working=[f"distance = 2 × {h_km} km = {_sci(d)} m", f"t = {_sci(d)} ÷ (3.0 × 10⁸)", f"= **{fmt(t, sf=3)} s**"],
        hints=[
            "How far does the signal travel in total? It goes up to the satellite and back down again.",
            f"2 × {h_km} km, in metres, divided by the speed of light.",
            f"t = {_sci(d)} ÷ 3.0 × 10⁸.",
        ],
    )


@template("c11_microwave_wavelength", chapter=11, level=4, lo="11c")
def microwave_wavelength(rng):
    f_ghz = nice(rng, 2.45, 1.8, 5.0, 10.0, 24.0)
    f = f_ghz * 1e9
    lam = C / f
    opts, key, mis = numeric_options(rng, lam, [
        (C / f_ghz, "You used the frequency in GHz. 1 GHz = 10⁹ Hz."),
        (C / (f_ghz * 1e6), "1 GHz is 10⁹ Hz, not 10⁶ Hz (that is MHz)."),
        (f / C, "You divided the wrong way: λ = v ÷ f."),
    ], unit="m", sf=3)
    table = md_table(["quantity", "value"], [["frequency", f"{fmt(f_ghz)} GHz"], ["speed", "3.0 × 10⁸ m/s"]])
    return dict(
        stem=f"A microwave oven uses microwaves of frequency **{fmt(f_ghz)} GHz**.\n\n{table}\n\nWhat is the wavelength of these microwaves?",
        options=opts, key=key, misconceptions=mis,
        formula="v = f λ  →  λ = v ÷ f, with f in Hz (1 GHz = 10⁹ Hz)",
        working=[f"f = {fmt(f_ghz)} GHz = {_sci(f)} Hz", f"λ = v ÷ f = (3.0 × 10⁸) ÷ ({_sci(f)})", f"= **{fmt(lam, sf=3)} m**"],
        hints=[
            "Which equation links wave speed, frequency and wavelength?",
            "Convert GHz to Hz first: multiply by 10⁹.",
            f"λ = 3.0 × 10⁸ ÷ {_sci(f)}.",
        ],
    )
