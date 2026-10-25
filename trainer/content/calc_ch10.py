"""Chapter 10 General Wave Properties: v = f λ, period, reading wave graphs, echoes."""
from .. import sketches
from .base import fmt, nice, numeric_options, template


# ---------------------------------------------------------------- L1
@template("c10_speed_from_f_lambda", chapter=10, level=1, lo="10d")
def speed_from_f_lambda(rng):
    f = nice(rng, 2, 4, 5, 8, 10, 20, 50)
    lam = nice(rng, 0.2, 0.5, 1.5, 2, 2.5, 4)
    v = f * lam
    opts, key, mis = numeric_options(rng, v, [
        (f / lam, "You divided. Wave speed = frequency × wavelength."),
        (lam / f, "You divided the wrong way round. v = f λ."),
        (f + lam, "You added. v = f × λ."),
    ], unit="m/s")
    return dict(
        stem=f"Fig. 1 shows a wave of wavelength **{fmt(lam)} m**. Its frequency is **{fmt(f)} Hz**. What is the speed of the wave?",
        figure=sketches.wave_graph(2, lam, kind="distance_m", cycles=2),
        options=opts, key=key, misconceptions=mis,
        formula="wave speed = frequency × wavelength (v = f λ)",
        working=["v = f λ", f"= {fmt(f)} × {fmt(lam)}", f"= **{fmt(v)} m/s**"],
        hints=["Which equation links speed, frequency and wavelength?",
               f"{fmt(f)} waves pass each second, and each is {fmt(lam)} m long.",
               f"v = {fmt(f)} × {fmt(lam)}."],
    )


@template("c10_period_from_frequency", chapter=10, level=1, lo="10c")
def period_from_frequency(rng):
    f = nice(rng, 2, 4, 5, 8, 10, 20, 25, 50)
    T = 1 / f
    opts, key, mis = numeric_options(rng, T, [
        (f, "That is the frequency. Period = 1 ÷ frequency."),
        (2 / f, "You doubled. One period is ONE complete oscillation: T = 1 ÷ f."),
        (1 / (2 * f), "You halved. T = 1 ÷ f, not 1 ÷ 2f."),
    ], unit="s")
    return dict(
        stem=f"Fig. 1 shows the displacement–time graph of a particle in a wave of frequency **{fmt(f)} Hz**. What is the period of the wave?",
        figure=sketches.wave_graph(2, T, kind="time", cycles=2),
        options=opts, key=key, misconceptions=mis,
        formula="period T = 1 ÷ frequency",
        working=["T = 1 ÷ f", f"= 1 ÷ {fmt(f)}", f"= **{fmt(T)} s**"],
        hints=["Frequency is the number of waves per second. How long does ONE wave take?",
               f"{fmt(f)} waves each second, so each one takes 1 ÷ {fmt(f)} s.",
               f"T = 1 ÷ {fmt(f)}."],
    )


# ---------------------------------------------------------------- L2
@template("c10_wavelength_from_graph", chapter=10, level=2, lo="10c")
def wavelength_from_graph(rng):
    lam = nice(rng, 4, 6, 8, 10, 12, 20)
    A = nice(rng, 1, 2, 3, 4, 5)
    opts, key, mis = numeric_options(rng, lam, [
        (lam / 2, "That is the distance from a crest to the next trough: HALF a wavelength."),
        (2 * lam, "That is two wavelengths. One wavelength is crest to the next crest."),
        (A, "That is the amplitude, read from the vertical axis."),
    ], unit="cm")
    return dict(
        stem="Fig. 1 shows the displacement–distance graph of a wave at one instant. What is the wavelength of the wave?",
        figure=sketches.wave_graph(A, lam, kind="distance", cycles=2),
        options=opts, key=key, misconceptions=mis,
        formula="wavelength = distance between two successive crests (or any two successive points in phase)",
        working=[f"crest to next crest on the distance axis: from {fmt(lam / 4)} cm to {fmt(5 * lam / 4)} cm", f"wavelength = **{fmt(lam)} cm**"],
        hints=["Wavelength is a DISTANCE along the horizontal axis. Between which two points do you measure it?",
               "Find one crest and the next crest, and read the distance between them.",
               f"The first crest is at {fmt(lam / 4)} cm and the next at {fmt(5 * lam / 4)} cm."],
    )


@template("c10_amplitude_from_graph", chapter=10, level=2, lo="10c")
def amplitude_from_graph(rng):
    lam = nice(rng, 4, 6, 8, 10, 12)
    A = nice(rng, 1, 1.5, 2, 2.5, 3, 4, 5)
    opts, key, mis = numeric_options(rng, A, [
        (2 * A, "That is crest to trough. Amplitude is from the REST position to the crest."),
        (A / 2, "You halved the crest height. Amplitude = maximum displacement from rest."),
        (lam, "That is the wavelength, read along the distance axis."),
    ], unit="cm")
    return dict(
        stem="Fig. 1 shows the displacement–distance graph of a wave at one instant. What is the amplitude of the wave?",
        figure=sketches.wave_graph(A, lam, kind="distance", cycles=2),
        options=opts, key=key, misconceptions=mis,
        formula="amplitude = maximum displacement from the rest (zero) position",
        working=[f"the crest reaches {fmt(A)} cm above the rest position", f"amplitude = **{fmt(A)} cm**"],
        hints=["Amplitude is measured on the VERTICAL axis. From where to where?",
               "From the rest position (displacement 0) up to the top of a crest.",
               f"The crest is at a displacement of {fmt(A)} cm."],
    )


@template("c10_frequency_from_time_graph", chapter=10, level=2, lo="10c")
def frequency_from_time_graph(rng):
    T = nice(rng, 0.1, 0.2, 0.25, 0.4, 0.5, 2, 4)
    f = 1 / T
    A = nice(rng, 1, 2, 3)
    opts, key, mis = numeric_options(rng, f, [
        (T, "That is the period in seconds. Frequency = 1 ÷ period."),
        (1 / (2 * T), "You used two periods. Read the time for ONE complete wave."),
        (2 / T, "You used half a period (crest to trough). One full wave is crest to crest."),
    ], unit="Hz")
    return dict(
        stem="Fig. 1 shows the displacement–time graph of a particle in a wave. What is the frequency of the wave?",
        figure=sketches.wave_graph(A, T, kind="time", cycles=2),
        options=opts, key=key, misconceptions=mis,
        formula="period T = time for one complete wave (read from the graph); f = 1 ÷ T",
        working=[f"one complete wave takes T = {fmt(T)} s (crest at {fmt(T / 4)} s to crest at {fmt(5 * T / 4)} s)", f"f = 1 ÷ {fmt(T)} = **{fmt(f)} Hz**"],
        hints=["This graph has TIME on the horizontal axis, so crest to crest gives the period. Then how do you get frequency?",
               f"Crest to crest = {fmt(T)} s. That is the period T.",
               f"f = 1 ÷ {fmt(T)}."],
    )


# ---------------------------------------------------------------- L3
@template("c10_speed_from_graph_and_period", chapter=10, level=3, lo="10d")
def speed_from_graph_and_period(rng):
    lam_cm = nice(rng, 4, 5, 8, 10, 20, 40)
    T = nice(rng, 0.1, 0.2, 0.25, 0.5, 2)
    lam = lam_cm / 100
    v = lam / T
    opts, key, mis = numeric_options(rng, v, [
        (lam_cm / T, "You left the wavelength in cm. Convert to metres for a speed in m/s."),
        (lam * T, "You multiplied by the period. v = f λ = λ ÷ T."),
        (T / lam, "You divided the wrong way round: v = λ ÷ T."),
    ], unit="m/s")
    return dict(
        stem=f"Fig. 1 shows the displacement–distance graph of a wave. The period of the wave is **{fmt(T)} s**. What is the speed of the wave?",
        figure=sketches.wave_graph(2, lam_cm, kind="distance", cycles=2),
        options=opts, key=key, misconceptions=mis,
        formula="f = 1 ÷ T, then v = f λ (equivalently v = λ ÷ T), with λ in metres",
        working=[f"from the graph λ = {fmt(lam_cm)} cm = {fmt(lam)} m", f"f = 1 ÷ {fmt(T)} = {fmt(1 / T)} Hz",
                 f"v = f λ = {fmt(1 / T)} × {fmt(lam)} = **{fmt(v)} m/s**"],
        hints=["Read the wavelength from the graph (crest to crest). Then you need the frequency: how do you get it from the period?",
               f"λ = {fmt(lam_cm)} cm = {fmt(lam)} m. f = 1 ÷ {fmt(T)} = {fmt(1 / T)} Hz.",
               f"v = {fmt(1 / T)} × {fmt(lam)}."],
    )


@template("c10_echo_distance", chapter=10, level=3, lo="10i")
def echo_distance(rng):
    v = 340
    t = nice(rng, 0.4, 0.5, 0.8, 1.0, 1.2, 1.5, 2.0)
    d = v * t / 2
    opts, key, mis = numeric_options(rng, d, [
        (v * t, "You forgot that the sound travels to the wall AND back. The distance to the wall is half the total path."),
        (v * t / 4, "You halved twice. The total path is v × t; the wall is half of that away."),
        (v / t, "You divided speed by time. Distance = speed × time (then halve for one way)."),
    ], unit="m")
    return dict(
        stem=f"Fig. 1 shows a student who claps and hears the echo from a wall **{fmt(t)} s** later. The speed of sound in air is **340 m/s**. How far is the student from the wall?",
        figure=sketches.echo_sketch("d = ?", f"echo heard after {fmt(t)} s"),
        options=opts, key=key, misconceptions=mis,
        formula="total path = speed × time = 2 d, so d = v t ÷ 2",
        working=[f"total distance travelled by the sound = 340 × {fmt(t)} = {fmt(v * t)} m", f"this is there AND back, so d = {fmt(v * t)} ÷ 2", f"= **{fmt(d)} m**"],
        hints=["The sound goes to the wall and comes back before it is heard. How far does it travel in total?",
               f"Total path = 340 × {fmt(t)} = {fmt(v * t)} m, which is twice the distance to the wall.",
               f"d = {fmt(v * t)} ÷ 2."],
    )


# ---------------------------------------------------------------- L4
@template("c10_wavefronts_speed", chapter=10, level=4, lo="10d")
def wavefronts_speed(rng):
    n = nice(rng, 4, 5, 6)
    lam_cm = nice(rng, 2, 3, 4, 5, 6)
    span = (n - 1) * lam_cm
    f = nice(rng, 2, 4, 5, 8, 10)
    v = f * lam_cm / 100
    opts, key, mis = numeric_options(rng, v, [
        (f * span / n / 100, f"You divided the {span} cm by the number of wavefronts ({n}). There are only {n - 1} wavelengths between {n} wavefronts."),
        (f * lam_cm, "You left the wavelength in cm. Convert to metres for m/s."),
        (f * span / 100, "You used the whole span as one wavelength. The span covers several wavelengths."),
    ], unit="m/s")
    return dict(
        stem=f"Fig. 1 shows **{n}** successive wavefronts in a ripple tank. The distance between the first and last wavefront is **{span} cm**. The dipper vibrates at **{fmt(f)} Hz**. What is the speed of the water waves?",
        figure=sketches.wavefronts_sketch(n, f"{span} cm"),
        options=opts, key=key, misconceptions=mis,
        formula="λ = span ÷ (number of wavefronts − 1), then v = f λ with λ in m",
        working=[f"{n} wavefronts span {n - 1} wavelengths: λ = {span} ÷ {n - 1} = {lam_cm} cm = {fmt(lam_cm / 100)} m",
                 f"v = f λ = {fmt(f)} × {fmt(lam_cm / 100)}", f"= **{fmt(v)} m/s**"],
        hints=["Successive wavefronts are one wavelength apart. How many wavelengths fit between the first and the last wavefront?",
               f"{n} wavefronts have {n - 1} gaps, so λ = {span} ÷ {n - 1} = {lam_cm} cm. Convert to metres.",
               f"v = {fmt(f)} × {fmt(lam_cm / 100)}."],
    )


@template("c10_echo_time", chapter=10, level=4, lo="10i")
def echo_time(rng):
    v = 340
    d = nice(rng, 51, 68, 85, 102, 136, 170, 255)
    t = 2 * d / v
    opts, key, mis = numeric_options(rng, t, [
        (d / v, "That is the time for the sound to REACH the wall. The echo needs the return trip too."),
        (4 * d / v, "You doubled twice. The round trip is 2d."),
        (v / (2 * d), "You divided the wrong way round: time = distance ÷ speed."),
    ], unit="s")
    return dict(
        stem=f"Fig. 1 shows a student standing **{fmt(d)} m** from a large wall. She shouts. The speed of sound in air is **340 m/s**. How long after shouting does she hear the echo?",
        figure=sketches.echo_sketch(f"d = {fmt(d)} m", "time until echo = ?"),
        options=opts, key=key, misconceptions=mis,
        formula="time = total path ÷ speed = 2 d ÷ v",
        working=[f"total path = 2 × {fmt(d)} = {fmt(2 * d)} m", f"time = {fmt(2 * d)} ÷ 340", f"= **{fmt(t)} s**"],
        hints=["How far does the sound travel before she hears it: to the wall only, or there and back?",
               f"Round trip = 2 × {fmt(d)} = {fmt(2 * d)} m at 340 m/s.",
               f"t = {fmt(2 * d)} ÷ 340."],
    )


# ---------------------------------------------------------------- L5
@template("c10_speed_khz_cm", chapter=10, level=5, lo="10d")
def speed_khz_cm(rng):
    f_khz = nice(rng, 2, 4, 5, 8, 10, 20)
    lam_cm = nice(rng, 1.7, 3.4, 4.25, 6.8, 8.5, 17)
    v = f_khz * 1000 * lam_cm / 100
    opts, key, mis = numeric_options(rng, v, [
        (f_khz * lam_cm, "You used kHz and cm as if they were Hz and m. Convert both: × 1000 and ÷ 100."),
        (f_khz * 1000 * lam_cm, "You converted the frequency but left the wavelength in cm."),
        (f_khz * lam_cm / 100, "You converted the wavelength but left the frequency in kHz."),
    ], unit="m/s")
    return dict(
        stem=f"Fig. 1 shows the displacement–distance graph of a sound wave. Its frequency is **{fmt(f_khz)} kHz** and its wavelength is **{fmt(lam_cm)} cm**. What is the speed of the sound?",
        figure=sketches.wave_graph(1, lam_cm, kind="distance", cycles=2),
        options=opts, key=key, misconceptions=mis,
        formula="v = f λ with f in Hz (kHz × 1000) and λ in m (cm ÷ 100)",
        working=[f"f = {fmt(f_khz)} kHz = {fmt(f_khz * 1000)} Hz; λ = {fmt(lam_cm)} cm = {fmt(lam_cm / 100)} m",
                 f"v = {fmt(f_khz * 1000)} × {fmt(lam_cm / 100)}", f"= **{fmt(v)} m/s**"],
        hints=["v = f λ, but check the units of BOTH quantities before multiplying.",
               f"{fmt(f_khz)} kHz = {fmt(f_khz * 1000)} Hz. {fmt(lam_cm)} cm = {fmt(lam_cm / 100)} m.",
               f"v = {fmt(f_khz * 1000)} × {fmt(lam_cm / 100)}."],
    )


@template("c10_frequency_from_speed_and_graph", chapter=10, level=5, lo="10d")
def frequency_from_speed_and_graph(rng):
    lam_cm = nice(rng, 2, 4, 5, 8, 10, 20, 25)
    v = nice(rng, 2, 4, 5, 10, 20, 340)
    lam = lam_cm / 100
    f = v / lam
    opts, key, mis = numeric_options(rng, f, [
        (v / lam_cm, "You left the wavelength in cm. Convert to metres first."),
        (v * lam, "You multiplied. Rearrange v = f λ to get f = v ÷ λ."),
        (lam / v, "You divided the wrong way round: f = v ÷ λ."),
    ], unit="Hz")
    return dict(
        stem=f"Fig. 1 shows the displacement–distance graph of a wave travelling at **{fmt(v)} m/s**. What is the frequency of the wave?",
        figure=sketches.wave_graph(2, lam_cm, kind="distance", cycles=2),
        options=opts, key=key, misconceptions=mis,
        formula="read λ from the graph (in m), then f = v ÷ λ",
        working=[f"from the graph λ = {fmt(lam_cm)} cm = {fmt(lam)} m", f"f = v ÷ λ = {fmt(v)} ÷ {fmt(lam)}", f"= **{fmt(f)} Hz**"],
        hints=["You need the wavelength from the graph. Read crest to crest, and note the unit on the axis.",
               f"λ = {fmt(lam_cm)} cm = {fmt(lam)} m. Rearrange v = f λ.",
               f"f = {fmt(v)} ÷ {fmt(lam)}."],
    )
