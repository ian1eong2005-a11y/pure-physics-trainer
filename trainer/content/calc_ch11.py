"""Chapter 11 Electromagnetic Spectrum: all EM waves travel at 3 × 10⁸ m/s in vacuum; v = f λ applied to EM waves."""
from .. import sketches
from .base import fmt, nice, numeric_options, template

C = 3e8


@template("c11_wavelength_from_frequency", chapter=11, level=3, lo="11a")
def wavelength_from_frequency(rng):
    f_mhz = nice(rng, 75, 100, 150, 200, 300, 600)
    lam = C / (f_mhz * 1e6)
    opts, key, mis = numeric_options(rng, lam, [
        (C / f_mhz, "You left the frequency in MHz. 1 MHz = 1 000 000 Hz."),
        (f_mhz * 1e6 / C, "You divided the wrong way round: λ = c ÷ f."),
        (lam * 1000, "You converted MHz with 1000 instead of 1 000 000."),
    ], unit="m")
    return dict(
        stem=f"Fig. 1 shows the electromagnetic spectrum. A radio station broadcasts at **{fmt(f_mhz)} MHz**. Radio waves travel at **3 × 10⁸ m/s**. What is the wavelength of the broadcast?",
        figure=sketches.em_spectrum(highlight="radio waves"),
        options=opts, key=key, misconceptions=mis,
        formula="c = f λ, so λ = c ÷ f with f in Hz (MHz × 1 000 000)",
        working=[f"f = {fmt(f_mhz)} MHz = {fmt(f_mhz * 1e6, sf=4)} Hz", f"λ = c ÷ f = 3 × 10⁸ ÷ {fmt(f_mhz * 1e6, sf=4)}", f"= **{fmt(lam)} m**"],
        hints=["All electromagnetic waves obey v = f λ with v = 3 × 10⁸ m/s. Rearrange for λ.",
               f"{fmt(f_mhz)} MHz = {fmt(f_mhz)} × 10⁶ Hz. Divide the speed by this.",
               f"λ = 300 000 000 ÷ {fmt(f_mhz * 1e6, sf=4)}."],
    )


@template("c11_frequency_from_wavelength", chapter=11, level=4, lo="11a")
def frequency_from_wavelength(rng):
    lam_cm = nice(rng, 1, 2, 3, 5, 6, 10, 15, 30)
    f_ghz = 30 / lam_cm
    opts, key, mis = numeric_options(rng, f_ghz, [
        (3e8 / lam_cm / 1e9, "You left the wavelength in cm. Convert to metres first."),
        (f_ghz / 1000, "You divided by an extra 1000: check the conversion from Hz to GHz (÷ 10⁹)."),
        (f_ghz * 2, "You doubled. Check the arithmetic: f = 3 × 10⁸ ÷ λ."),
    ], unit="GHz")
    return dict(
        stem=f"Fig. 1 shows the electromagnetic spectrum. A microwave oven uses waves of wavelength **{fmt(lam_cm)} cm**. Electromagnetic waves travel at **3 × 10⁸ m/s**. What is the frequency of the microwaves, in GHz (1 GHz = 10⁹ Hz)?",
        figure=sketches.em_spectrum(highlight="microwaves"),
        options=opts, key=key, misconceptions=mis,
        formula="f = c ÷ λ with λ in m; then ÷ 10⁹ for GHz",
        working=[f"λ = {fmt(lam_cm)} cm = {fmt(lam_cm / 100)} m", f"f = 3 × 10⁸ ÷ {fmt(lam_cm / 100)} = {fmt(3e8 / (lam_cm / 100), sf=4)} Hz",
                 f"= **{fmt(f_ghz)} GHz**"],
        hints=["Rearrange c = f λ for f. Which unit must the wavelength be in?",
               f"λ = {fmt(lam_cm)} cm = {fmt(lam_cm / 100)} m. f = 3 × 10⁸ ÷ {fmt(lam_cm / 100)} Hz.",
               f"Divide the answer in Hz by 10⁹ to get GHz."],
    )


@template("c11_signal_time", chapter=11, level=5, lo="11a")
def signal_time(rng):
    d_km = nice(rng, 3000, 6000, 15000, 36000, 45000, 60000)
    t = d_km * 1000 / C
    opts, key, mis = numeric_options(rng, t, [
        (d_km / C, "You left the distance in km. 1 km = 1000 m."),
        (C / (d_km * 1000), "You divided the wrong way round: time = distance ÷ speed."),
        (2 * d_km * 1000 / C, "You doubled the distance. The question asks for a ONE-WAY signal."),
    ], unit="s")
    return dict(
        stem=f"Fig. 1 shows a radio signal sent from a ground station to a satellite **{fmt(d_km)} km** away. Radio waves travel at **3 × 10⁸ m/s**. How long does the signal take to reach the satellite?",
        figure=sketches.two_bodies_sketch(["ground station"], [f"d = {fmt(d_km)} km"], left_name="Earth", right_name="satellite"),
        options=opts, key=key, misconceptions=mis,
        formula="time = distance ÷ speed, with distance in metres",
        working=[f"d = {fmt(d_km)} km = {fmt(d_km * 1000, sf=4)} m", f"t = {fmt(d_km * 1000, sf=4)} ÷ 3 × 10⁸", f"= **{fmt(t)} s**"],
        hints=["Radio waves are electromagnetic, so they travel at the speed of light. time = distance ÷ speed.",
               f"{fmt(d_km)} km = {fmt(d_km * 1000, sf=4)} m.",
               f"t = {fmt(d_km * 1000, sf=4)} ÷ 300 000 000."],
    )
