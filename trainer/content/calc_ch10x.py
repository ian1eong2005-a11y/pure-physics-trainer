"""Chapter 10 General Properties of Waves (6091) bank extension: calculation and data-reading templates, 10 per level,
each LO at least twice. Contexts adapted from the question bank (SEAB 2016-2025: ripple tank with a dipper, echo from a cliff,
sound through a steel rail, sonar and ultrasound scans, oscilloscope traces of two notes; school papers 2024-2025)."""
from .. import figs2, sketches
from .base import fmt, md_table, mk, mkt, nice, template

V_AIR = 340


# ================================================================== L1
@template("c10x_period_simple", chapter=10, level=1, lo="10c")
def period_simple(rng):
    n = nice(rng, 10, 20, 25, 40)
    t = nice(rng, 4, 5, 8, 10)
    f = n / t
    return mk(rng, f, [(t / n, "That is the PERIOD; frequency = number of waves ÷ time."), (n * t, "Divide the number of waves by the time."), (n, "Divide by the time.")],
              "Hz", f"A float on a pond bobs up and down as waves pass.\n\n{md_table(['quantity', 'value'], [['number of complete waves passing', n], ['time taken', f'{t} s']])}\n\nWhat is the frequency of the waves?",
              "f = number of waves ÷ time", [f"f = {n} ÷ {t} = **{fmt(f)} Hz**"],
              ["Frequency = waves per second.", "Divide the number by the time.", "Unit: Hz."])


@template("c10x_speed_simple", chapter=10, level=1, lo="10d")
def speed_simple(rng):
    f = nice(rng, 2, 4, 5, 10)
    lam = nice(rng, 0.02, 0.05, 0.1, 0.2)
    return mk(rng, f * lam, [(f / lam, "v = f × λ."), (lam / f, "Multiply f by λ."), (f * lam * 100, "λ is in metres, so v is in m/s.")],
              "m/s", f"Water waves in a ripple tank (Fig. 1).\n\n{md_table(['quantity', 'value'], [['frequency', f'{f} Hz'], ['wavelength', f'{fmt(lam)} m']])}\n\nWhat is the speed of the waves?",
              "v = f λ", [f"v = {f} × {fmt(lam)} = **{fmt(f * lam)} m/s**"],
              ["Use the wave equation.", "v = f λ.", "Multiply."], figure=sketches.wavefronts_sketch(5, f"λ = {fmt(lam)} m between neighbours"))


@template("c10x_thunder_distance", chapter=10, level=1, lo="10f")
def thunder_distance(rng):
    t = nice(rng, 2, 3, 4, 5, 6)
    return mk(rng, V_AIR * t, [(V_AIR / t, "d = v × t."), (V_AIR * t / 2, "The sound travels one way only (not an echo)."), (V_AIR * t * 2, "Do not double: the sound travels from the lightning to you once.")],
              "m", f"Lightning is seen and the thunder is heard a short time later.\n\n{md_table(['quantity', 'value'], [['time between flash and thunder', f'{t} s'], ['speed of sound in air', '340 m/s']])}\n\nHow far away is the storm? (Light arrives almost instantly.)",
              "d = v t (one way)", [f"d = 340 × {t} = **{340 * t} m**"],
              ["Light arrives almost at once.", "Sound takes t seconds.", "d = v t."], dp=0)


@template("c10x_fastest_medium", chapter=10, level=1, lo="10f")
def fastest_medium(rng):
    rows = [("air", 340), ("water", 1500), ("steel", 5000), ("wood", 3800)]
    rng.shuffle(rows)
    target = rng.choice(["fastest", "slowest"])
    ans = (max if target == "fastest" else min)(rows, key=lambda r: r[1])[0]
    wrongs = {n: "Compare the speeds in the table." for n, v in rows if n != ans}
    table = md_table(["medium", "speed of sound / m/s"], [[n, v] for n, v in rows])
    return mkt(rng, ans, wrongs, f"{table}\n\nIn which medium does sound travel **{target}**?",
               "sound is generally fastest in solids, slowest in gases", [f"**{ans}**"],
               ["Read the speeds.", f"Find the {target}.", "Solids fastest, gases slowest."])


@template("c10x_echo_simple", chapter=10, level=1, lo="10i")
def echo_simple(rng):
    t = nice(rng, 0.4, 0.5, 0.6, 1.0, 1.2)
    d = V_AIR * t / 2
    return mk(rng, d, [(V_AIR * t, "The sound goes TO the wall AND back: halve it."), (V_AIR / t, "d = v t ÷ 2."), (V_AIR * t / 4, "Halve only once.")],
              "m", f"A student claps and hears the echo from a wall **{fmt(t)} s** later (Fig. 1). The speed of sound is 340 m/s. How far away is the wall?",
              "d = v t ÷ 2 (there and back)", [f"total path = 340 × {fmt(t)} = {fmt(V_AIR * t)} m", f"d = {fmt(V_AIR * t)} ÷ 2 = **{fmt(d)} m**"],
              ["Echo: the sound travels there and back.", "Total distance = v t.", "Halve it."], figure=sketches.echo_sketch("d = ?", f"echo after {fmt(t)} s"))


@template("c10x_echo_time_simple", chapter=10, level=1, lo="10i")
def echo_time_simple(rng):
    d = nice(rng, 85, 170, 255, 340)
    t = 2 * d / V_AIR
    return mk(rng, t, [(d / V_AIR, "The echo travels there AND back: double the distance."), (V_AIR / d, "t = 2d ÷ v."), (4 * d / V_AIR, "Double the distance only once.")],
              "s", f"A shout is made **{d} m** from a cliff (Fig. 1). The speed of sound is 340 m/s. After how long is the echo heard?",
              "t = 2 d ÷ v", [f"t = 2 × {d} ÷ 340 = **{fmt(t)} s**"],
              ["The sound goes to the cliff and back.", "Total distance = 2d.", "t = distance ÷ speed."], figure=sketches.echo_sketch(f"{d} m", "t = ?", right="cliff"))


@template("c10x_ultrasound_check", chapter=10, level=1, lo="10j")
def ultrasound_check(rng):
    freqs = rng.sample([5, 50, 500, 5000, 15000, 25000, 40000, 2000000], 4)
    if not any(f > 20000 for f in freqs):
        freqs[0] = 40000
    if sum(f > 20000 for f in freqs) > 1:
        keep = max(f for f in freqs if f > 20000)
        freqs = [f for f in freqs if f <= 20000][:3] + [keep]
        while len(freqs) < 4:
            freqs.insert(0, rng.choice([10, 100, 1000, 10000]))
    rng.shuffle(freqs)
    names = ["P", "Q", "R", "S"]
    ans = names[[f > 20000 for f in freqs].index(True)]
    wrongs = {n: "This frequency is within (or below) the human hearing range." for n, f in zip(names, freqs) if n != ans}
    table = md_table(["sound", "frequency / Hz"], [[n, f] for n, f in zip(names, freqs)])
    return mkt(rng, ans, wrongs, f"{table}\n\nWhich sound is ultrasound?",
               "ultrasound: frequency above 20 000 Hz (20 kHz)", [f"**{ans}** is above 20 kHz"],
               ["Human hearing: about 20 Hz to 20 kHz.", "Ultrasound is above that.", "Pick the frequency above 20 000 Hz."])


@template("c10x_sonar_depth_simple", chapter=10, level=1, lo="10j")
def sonar_depth_simple(rng):
    t = nice(rng, 0.2, 0.4, 0.6, 0.8, 1.0)
    d = 1500 * t / 2
    return mk(rng, d, [(1500 * t, "The pulse goes down AND back up: halve."), (340 * t / 2, "Use the speed of sound in SEA WATER (1500 m/s)."), (1500 / t, "d = v t ÷ 2.")],
              "m", f"A ship's sonar sends a pulse of ultrasound to the sea bed.\n\n{md_table(['quantity', 'value'], [['time for echo to return', f'{fmt(t)} s'], ['speed of sound in sea water', '1500 m/s']])}\n\nHow deep is the sea?",
              "depth = v t ÷ 2", [f"depth = 1500 × {fmt(t)} ÷ 2 = **{fmt(d)} m**"],
              ["The pulse travels down and back.", "Total = v t.", "Halve for the depth."])


# ================================================================== L2
@template("c10x_wavelength_from_speed", chapter=10, level=2, lo="10d")
def wavelength_from_speed(rng):
    v = nice(rng, 340, 330)
    f = nice(rng, 170, 256, 440, 680, 1000)
    lam = v / f
    return mk(rng, lam, [(f / v, "λ = v ÷ f."), (v * f, "Divide v by f."), (lam * 100, "The answer is in metres.")],
              "m", f"A tuning fork produces a note in air.\n\n{md_table(['quantity', 'value'], [['frequency', f'{f} Hz'], ['speed of sound', f'{v} m/s']])}\n\nWhat is the wavelength of the sound?",
              "λ = v ÷ f", [f"λ = {v} ÷ {f} = **{fmt(lam)} m**"],
              ["Rearrange v = f λ.", "λ = v ÷ f.", "Calculate."])


@template("c10x_frequency_from_speed", chapter=10, level=2, lo="10d")
def frequency_from_speed(rng):
    v = nice(rng, 1.5, 2.0, 3.0)
    lam = nice(rng, 0.5, 0.6, 0.75, 1.0)
    return mk(rng, v / lam, [(v * lam, "f = v ÷ λ."), (lam / v, "Speed goes on top."), (v, "Divide by the wavelength.")],
              "Hz", f"Ocean swells travel towards a beach.\n\n{md_table(['quantity', 'value'], [['speed', f'{fmt(v)} m/s'], ['wavelength', f'{fmt(lam)} m']])}\n\nWhat is the frequency of the waves?",
              "f = v ÷ λ", [f"f = {fmt(v)} ÷ {fmt(lam)} = **{fmt(v / lam)} Hz**"],
              ["Rearrange v = f λ.", "f = v ÷ λ.", "Divide."])


@template("c10x_echo_cliff_speed", chapter=10, level=2, lo="10i")
def echo_cliff_speed(rng):
    d = nice(rng, 100, 150, 200)
    t = nice(rng, 0.6, 0.9, 1.2)
    v = 2 * d / t
    return mk(rng, v, [(d / t, "The sound travels 2d (there and back)."), (t / (2 * d), "v = 2d ÷ t."), (4 * d / t, "Double the distance only once.")],
              "m/s", f"A student stands **{d} m** from a cliff and claps. A friend times the echo (Fig. 1).\n\n{md_table(['quantity', 'value'], [['distance to cliff', f'{d} m'], ['time for echo', f'{fmt(t)} s']])}\n\nWhat value does this give for the speed of sound?",
              "v = 2d ÷ t", [f"v = 2 × {d} ÷ {fmt(t)} = **{fmt(v)} m/s**"],
              ["Total path = 2 × distance.", "Speed = distance ÷ time.", "v = 2d ÷ t."], figure=sketches.echo_sketch(f"{d} m", f"echo after {fmt(t)} s", right="cliff"))


@template("c10x_clap_rhythm", chapter=10, level=2, lo="10i")
def clap_rhythm(rng):
    d = nice(rng, 50, 60, 80)
    n = nice(rng, 20, 25, 30)
    T_total = nice(rng, 6.0, 8.0, 10.0)
    t_one = T_total / n
    v = 2 * d / t_one
    return mk(rng, v, [(d / t_one, "Each echo travels 2d."), (2 * d / T_total, "Divide the total time by the number of claps first."), (2 * d * n * T_total, "v = 2d ÷ (time per clap).")],
              "m/s", f"A student claps in time with the echoes from a wall, so each clap coincides with the echo of the previous one.\n\n{md_table(['quantity', 'value'], [['distance to wall', f'{d} m'], ['number of intervals between claps timed', n], ['total time', f'{fmt(T_total)} s']])}\n\nWhat is the speed of sound?",
              "time for one echo = total ÷ n; v = 2d ÷ t", [f"t = {fmt(T_total)} ÷ {n} = {fmt(t_one)} s", f"v = 2 × {d} ÷ {fmt(t_one)} = **{fmt(v)} m/s**"],
              ["Find the time for one echo.", "Each echo travels to the wall and back.", "v = 2d ÷ t."])


@template("c10x_cro_frequency", chapter=10, level=2, lo="10h")
def cro_frequency(rng):
    p_div = nice(rng, 2, 2.5, 4, 5)
    tb = nice(rng, 0.5, 1.0, 2.0)
    T = p_div * tb / 1000
    f = 1 / T
    return mk(rng, f, [(1 / (p_div * tb), "Convert ms to s: T = divisions × time-base (in s)."), (p_div * tb, "That is the period in ms; f = 1 ÷ T."), (f / 2, "Count the divisions for ONE complete wave.")],
              "Hz", f"Fig. 1 shows the trace of a sound on an oscilloscope. The time-base is set to **{fmt(tb)} ms per division**. What is the frequency of the sound?",
              "T = (divisions per wave) × time-base; f = 1 ÷ T", [f"one wave spans {fmt(p_div)} divisions → T = {fmt(p_div)} × {fmt(tb)} ms = {fmt(T * 1000)} ms", f"f = 1 ÷ {fmt(T)} s = **{fmt(f)} Hz**"],
              ["Count the divisions for one wave.", "Multiply by the time-base to get T.", "f = 1 ÷ T."], figure=figs2.cro_trace(p_div, 3, f"time-base: 1 division = {fmt(tb)} ms"))


@template("c10x_audible_range", chapter=10, level=2, lo="10h")
def audible_range(rng):
    rows = [("A", 12), ("B", nice(rng, 300, 440, 1000)), ("C", nice(rng, 25000, 30000)), ("D", nice(rng, 8, 15))]
    rng.shuffle(rows)
    ans = next(n for n, f in rows if 20 <= f <= 20000)
    wrongs = {n: ("Below 20 Hz: infrasound, too low to hear." if f < 20 else "Above 20 kHz: ultrasound, too high to hear.") for n, f in rows if n != ans}
    table = md_table(["sound", "frequency / Hz"], [[n, f] for n, f in rows])
    return mkt(rng, ans, wrongs, f"{table}\n\nWhich sound can a person with normal hearing hear?",
               "human hearing range: about 20 Hz to 20 000 Hz", [f"**{ans}** is between 20 Hz and 20 kHz"],
               ["Recall the audible range.", "About 20 Hz to 20 kHz.", "Pick the one inside it."])


@template("c10x_crest_trough_distance", chapter=10, level=2, lo="10c")
def crest_trough_distance(rng):
    a = nice(rng, 2, 3, 4, 5)
    h = 2 * a
    return mk(rng, a, [(h, "That is crest-to-trough; amplitude is HALF of it."), (h * 2, "Amplitude is measured from the rest position."), (a / 2, "Halve the crest-to-trough height once.")],
              "cm", f"A rope is shaken to make a wave.\n\n{md_table(['quantity', 'value'], [['vertical distance from a crest to a trough', f'{h} cm']])}\n\nWhat is the amplitude of the wave?",
              "amplitude = (crest to trough) ÷ 2", [f"A = {h} ÷ 2 = **{a} cm**"],
              ["Amplitude is from the rest position to a crest.", "Crest-to-trough is twice that.", "Halve."], dp=0)


# ================================================================== L3
@template("c10x_wavelength_n_waves", chapter=10, level=3, lo="10c")
def wavelength_n_waves(rng):
    n = nice(rng, 3, 4, 5)
    lam = nice(rng, 4, 5, 6, 8)
    L = n * lam
    return mk(rng, lam, [(L, "That is the length of ALL the waves."), (L / (n - 1), "Count complete waves, not crests."), (L / (2 * n), "Divide by the number of complete waves.")],
              "cm", f"Fig. 1 shows a wave on a string. **{n}** complete waves fit into a length of **{L} cm**. What is the wavelength?",
              "λ = length ÷ number of complete waves", [f"λ = {L} ÷ {n} = **{lam} cm**"],
              ["Wavelength = length of one complete wave.", "Count the complete waves.", "Divide."], figure=sketches.wave_graph(2, lam, "distance", cycles=n), dp=0)


@template("c10x_period_from_f_ms", chapter=10, level=3, lo="10c")
def period_from_f_ms(rng):
    f = nice(rng, 200, 250, 400, 500, 800)
    T = 1 / f * 1000
    return mk(rng, T, [(1 / f, "That is in s; the answer is in ms."), (f / 1000, "T = 1 ÷ f."), (1000 * f, "T = 1 ÷ f, then × 1000 for ms.")],
              "ms", f"{md_table(['quantity', 'value'], [['frequency of a note', f'{f} Hz']])}\n\nWhat is the period of the sound wave, in milliseconds?",
              "T = 1 ÷ f", [f"T = 1 ÷ {f} = {fmt(1 / f)} s", f"= **{fmt(T)} ms**"],
              ["Period and frequency are reciprocals.", "T = 1 ÷ f.", "Convert to ms."])


@template("c10x_ripple_tank_speed", chapter=10, level=3, lo="10a")
def ripple_tank_speed(rng):
    n = nice(rng, 5, 6, 8)
    span = nice(rng, 8.0, 10.0, 12.0)
    f = nice(rng, 5, 8, 10)
    lam = span / (n - 1)
    v = f * lam
    return mk(rng, v, [(f * span / n, "n wavefronts have (n − 1) gaps between them."), (f * span, "Find λ first: span ÷ (n − 1)."), (v / 100, "The answer is in cm/s.")],
              "cm/s", f"Fig. 1 shows **{n}** straight wavefronts in a ripple tank spread over **{fmt(span)} cm**. The dipper vibrates at **{f} Hz**. What is the speed of the waves?",
              "λ = span ÷ (n − 1); v = f λ", [f"λ = {fmt(span)} ÷ {n - 1} = {fmt(lam)} cm", f"v = {f} × {fmt(lam)} = **{fmt(v)} cm/s**"],
              ["n wavefronts have n − 1 spaces.", "Each space is one wavelength.", "v = f λ."], figure=sketches.wavefronts_sketch(n, f"{fmt(span)} cm"))


@template("c10x_wavefront_time", chapter=10, level=3, lo="10a")
def wavefront_time(rng):
    v = nice(rng, 12, 15, 20)
    d = nice(rng, 30, 45, 60)
    return mk(rng, d / v, [(v / d, "t = d ÷ v."), (d * v, "Divide distance by speed."), (d / v * 2, "The wavefront travels one way.")],
              "s", f"A straight wavefront in a ripple tank travels from the dipper to the far side.\n\n{md_table(['quantity', 'value'], [['distance to far side', f'{d} cm'], ['wave speed', f'{v} cm/s']])}\n\nHow long does it take?",
              "t = d ÷ v", [f"t = {d} ÷ {v} = **{fmt(d / v)} s**"],
              ["Wavefronts move at the wave speed.", "t = d ÷ v.", "Divide."])


@template("c10x_speed_from_two_graphs", chapter=10, level=3, lo="10d")
def speed_from_two_graphs(rng):
    lam = nice(rng, 20, 40, 50, 80)
    T = nice(rng, 0.2, 0.4, 0.5)
    v = lam / 100 / T
    return mk(rng, v, [(lam / T, "Convert λ from cm to m."), (lam / 100 * T, "v = λ ÷ T."), (T / (lam / 100), "v = λ ÷ T, not T ÷ λ.")],
              "m/s", f"Fig. 1 shows the displacement–distance graph of a wave. Each particle completes one oscillation in **{fmt(T)} s**. What is the wave speed?",
              "v = λ ÷ T (= f λ)", [f"from the graph λ = {lam} cm = {fmt(lam / 100)} m", f"v = {fmt(lam / 100)} ÷ {fmt(T)} = **{fmt(v)} m/s**"],
              ["Read λ from the graph.", "Convert to m.", "v = λ ÷ T."], figure=sketches.wave_graph(3, lam, "distance", cycles=2))


@template("c10x_echo_two_cliffs", chapter=10, level=3, lo="10i")
def echo_two_cliffs(rng):
    t1 = nice(rng, 0.4, 0.6, 0.8)
    t2 = nice(rng, 1.0, 1.2, 1.4)
    d = V_AIR * (t1 + t2) / 2
    return mk(rng, d, [(V_AIR * (t1 + t2), "Each echo travels there and back: halve each."), (V_AIR * (t2 - t1) / 2, "Add the two distances to the cliffs."), (V_AIR * t2 / 2, "Include both cliffs.")],
              "m", f"A student stands between two cliffs and claps. She hears two echoes.\n\n{md_table(['echo', 'time after clap / s'], [['first', fmt(t1)], ['second', fmt(t2)]])}\n\nThe speed of sound is 340 m/s. How far apart are the cliffs?",
              "distance to each cliff = v t ÷ 2; add", [f"near cliff: 340 × {fmt(t1)} ÷ 2 = {fmt(V_AIR * t1 / 2)} m", f"far cliff: 340 × {fmt(t2)} ÷ 2 = {fmt(V_AIR * t2 / 2)} m", f"separation = **{fmt(d)} m**"],
              ["Find the distance to each cliff.", "Each echo is there and back.", "Add the two distances."])


@template("c10x_foetus_scan", chapter=10, level=3, lo="10j")
def foetus_scan(rng):
    v = 1500
    t_us = nice(rng, 40, 60, 80, 100)
    d = v * t_us * 1e-6 / 2 * 100
    return mk(rng, d, [(v * t_us * 1e-6 * 100, "The pulse travels to the boundary and back: halve."), (v * t_us / 2 * 100, "Convert µs to s (× 10⁻⁶)."), (d / 100, "The answer is in cm.")],
              "cm", f"An ultrasound scanner sends a pulse into the body.\n\n{md_table(['quantity', 'value'], [['time for echo from a boundary', f'{t_us} µs'], ['speed of ultrasound in soft tissue', '1500 m/s']])}\n\nHow deep is the boundary below the skin, in cm?",
              "depth = v t ÷ 2", [f"t = {t_us} × 10⁻⁶ s", f"depth = 1500 × {t_us} × 10⁻⁶ ÷ 2 = {fmt(d / 100)} m = **{fmt(d)} cm**"],
              ["Convert µs to s.", "The echo is there and back.", "Convert m to cm."])


@template("c10x_ultrasound_wavelength", chapter=10, level=3, lo="10j")
def ultrasound_wavelength(rng):
    f_mhz = nice(rng, 1.5, 2.0, 3.0, 5.0)
    v = 1500
    lam = v / (f_mhz * 1e6) * 1000
    return mk(rng, lam, [(v / f_mhz * 1000, "Convert MHz to Hz (× 10⁶)."), (lam / 1000, "That is in m; the answer is in mm."), (f_mhz * 1e6 / v, "λ = v ÷ f.")],
              "mm", f"{md_table(['quantity', 'value'], [['frequency of ultrasound', f'{fmt(f_mhz)} MHz'], ['speed in soft tissue', '1500 m/s']])}\n\nWhat is its wavelength in the tissue, in mm?",
              "λ = v ÷ f", [f"λ = 1500 ÷ {fmt(f_mhz)} × 10⁶ = {fmt(lam / 1000)} m", f"= **{fmt(lam)} mm**"],
              ["Convert MHz to Hz.", "λ = v ÷ f.", "Convert to mm."])


# ================================================================== L4
@template("c10x_rail_time_difference", chapter=10, level=4, lo="10f")
def rail_time_difference(rng):
    d = nice(rng, 510, 850, 1020, 1700)
    v_s = 5100
    dt = d / V_AIR - d / v_s
    return mk(rng, dt, [(d / V_AIR, "That is the time through air only; subtract the time through steel."), (d / v_s, "That is the time through steel only."), (d / (v_s - V_AIR), "Find each time, then subtract.")],
              "s", f"A hammer strikes one end of a long steel rail. A listener at the other end hears two sounds: one through the rail and one through the air.\n\n{md_table(['quantity', 'value'], [['length of rail', f'{d} m'], ['speed of sound in steel', '5100 m/s'], ['speed of sound in air', '340 m/s']])}\n\nWhat is the time between the two sounds?",
              "Δt = d ÷ v_air − d ÷ v_steel", [f"air: {d} ÷ 340 = {fmt(d / V_AIR)} s; steel: {d} ÷ 5100 = {fmt(d / v_s)} s", f"Δt = **{fmt(dt)} s**"],
              ["Find the time through each medium.", "t = d ÷ v.", "Subtract."])


@template("c10x_underwater_distance", chapter=10, level=4, lo="10f")
def underwater_distance(rng):
    t_air = nice(rng, 2.0, 3.0, 4.0)
    d = V_AIR * t_air
    t_water = d / 1500
    return mk(rng, t_water, [(t_air, "Sound travels faster in water, so it arrives sooner."), (d * 1500, "t = d ÷ v."), (t_air * 1500 / V_AIR, "Water is FASTER: the time is shorter.")],
              "s", f"A sound travels the same distance through air and through water.\n\n{md_table(['quantity', 'value'], [['time through air', f'{fmt(t_air)} s'], ['speed in air', '340 m/s'], ['speed in water', '1500 m/s']])}\n\nHow long does it take through water?",
              "d = v_air t_air; t_water = d ÷ v_water", [f"d = 340 × {fmt(t_air)} = {fmt(d)} m", f"t = {fmt(d)} ÷ 1500 = **{fmt(t_water)} s**"],
              ["Find the distance first.", "Then the time in water.", "Faster speed → shorter time."])


@template("c10x_phase_points", chapter=10, level=4, lo="10c")
def phase_points(rng):
    lam = nice(rng, 20, 40, 60)
    k = nice(rng, 1, 2, 3)
    d = k * lam
    return mk(rng, d, [(k * lam / 2, "Points in phase are WHOLE wavelengths apart."), (lam, f"They are {k} wavelengths apart."), (d * 2, "Multiply λ by the number of wavelengths.")],
              "cm", f"Fig. 1 shows a wave. Two particles move exactly in step (in phase) and are **{k}** wavelength(s) apart. How far apart are they?",
              "points in phase are a whole number of wavelengths apart", [f"from the graph λ = {lam} cm", f"distance = {k} × {lam} = **{d} cm**"],
              ["Read λ from the graph.", "In phase → whole wavelengths apart.", "Multiply."], figure=sketches.wave_graph(2, lam, "distance", cycles=3), dp=0)


@template("c10x_frequency_change_speed", chapter=10, level=4, lo="10c")
def frequency_change_speed(rng):
    lam1 = nice(rng, 0.4, 0.6, 0.8)
    k = nice(rng, 2, 4)
    lam2 = lam1 / k
    return mk(rng, lam2, [(lam1 * k, "Higher frequency → SHORTER wavelength (v is fixed)."), (lam1, "The wavelength changes."), (lam1 / (k * k), "λ ∝ 1/f, not 1/f².")],
              "m", f"Sound waves travel in air at a fixed speed.\n\n{md_table(['', 'frequency', 'wavelength / m'], [['note 1', 'f', fmt(lam1)], ['note 2', f'{k}f', '?']])}\n\nWhat is the wavelength of note 2?",
              "v = f λ fixed → λ ∝ 1/f", [f"λ₂ = {fmt(lam1)} ÷ {k} = **{fmt(lam2)} m**"],
              ["The speed is the same.", "f × λ is constant.", f"{k} × f → λ ÷ {k}."])


@template("c10x_speed_in_medium", chapter=10, level=4, lo="10d")
def speed_in_medium(rng):
    f = nice(rng, 500, 1000, 2000)
    lam_w = nice(rng, 0.75, 1.5, 3.0)
    v_w = f * lam_w
    lam_a = V_AIR / f
    return mk(rng, lam_w / lam_a, [(lam_a / lam_w, "Water is FASTER, so λ is LONGER there."), (v_w, "That is the speed; find the ratio of wavelengths."), (lam_w - lam_a, "Find the ratio, not the difference.")],
              "times", f"A sound of the same frequency travels from air into water.\n\n{md_table(['quantity', 'value'], [['frequency', f'{f} Hz'], ['wavelength in water', f'{fmt(lam_w)} m'], ['speed in air', '340 m/s']])}\n\nHow many times longer is the wavelength in water than in air?",
              "f unchanged; λ = v ÷ f in each", [f"λ_air = 340 ÷ {f} = {fmt(lam_a)} m", f"ratio = {fmt(lam_w)} ÷ {fmt(lam_a)} = **{fmt(lam_w / lam_a)}**"],
              ["The frequency does not change.", "Find λ in air.", "Divide."])


@template("c10x_echo_sounder_speed", chapter=10, level=4, lo="10i")
def echo_sounder_speed(rng):
    d = nice(rng, 300, 450, 600)
    t = nice(rng, 0.4, 0.6, 0.8)
    v = 2 * d / t
    return mk(rng, v, [(d / t, "The pulse travels 2d."), (2 * d * t, "v = 2d ÷ t."), (4 * d / t, "Double the depth only once.")],
              "m/s", f"An echo sounder is used where the sea is known to be **{d} m** deep (Fig. 1). The echo returns after **{fmt(t)} s**. What is the speed of sound in this sea water?",
              "v = 2d ÷ t", [f"v = 2 × {d} ÷ {fmt(t)} = **{fmt(v)} m/s**"],
              ["The pulse goes down and back.", "Distance = 2d.", "v = distance ÷ time."], figure=sketches.echo_sketch(f"{d} m", f"{fmt(t)} s", left="ship", right="sea bed"))


@template("c10x_echo_minimum_distance", chapter=10, level=4, lo="10i")
def echo_minimum_distance(rng):
    t_min = nice(rng, 0.1, 0.15, 0.2)
    d = V_AIR * t_min / 2
    return mk(rng, d, [(V_AIR * t_min, "The echo travels there and back: halve."), (V_AIR / t_min, "d = v t ÷ 2."), (d / 2, "Halve only once.")],
              "m", f"The ear can only hear an echo separately if it arrives at least **{fmt(t_min)} s** after the original sound.\n\n{md_table(['quantity', 'value'], [['minimum delay', f'{fmt(t_min)} s'], ['speed of sound', '340 m/s']])}\n\nWhat is the minimum distance from a wall for a separate echo to be heard?",
              "d = v t ÷ 2", [f"d = 340 × {fmt(t_min)} ÷ 2 = **{fmt(d)} m**"],
              ["The echo travels to the wall and back.", "Total path = v t.", "Halve."])


@template("c10x_sonar_shoal", chapter=10, level=4, lo="10j")
def sonar_shoal(rng):
    t1 = nice(rng, 0.2, 0.3)
    t2 = nice(rng, 0.8, 1.0, 1.2)
    v = 1500
    gap = v * (t2 - t1) / 2
    return mk(rng, gap, [(v * (t2 - t1), "Halve: each echo is there and back."), (v * t2 / 2, "That is the depth of the sea bed; subtract the shoal's depth."), (v * (t1 + t2) / 2, "Subtract, do not add.")],
              "m", f"A fishing boat's sonar receives two echoes from one pulse.\n\n{md_table(['echo from', 'time / s'], [['shoal of fish', fmt(t1)], ['sea bed', fmt(t2)]])}\n\nThe speed of sound in sea water is 1500 m/s. How far above the sea bed is the shoal?",
              "depth = v t ÷ 2 for each; subtract", [f"shoal: {fmt(v * t1 / 2)} m; sea bed: {fmt(v * t2 / 2)} m", f"height above bed = **{fmt(gap)} m**"],
              ["Find each depth.", "Each echo is there and back.", "Subtract."])


@template("c10x_ultrasound_crack", chapter=10, level=4, lo="10j")
def ultrasound_crack(rng):
    v = 5900
    t_back = nice(rng, 20, 30, 40)
    t_crack = t_back * nice(rng, 0.25, 0.4, 0.5)
    depth = v * t_crack * 1e-6 / 2 * 1000
    return mk(rng, depth, [(v * t_crack * 1e-6 * 1000, "Halve: the pulse goes to the crack and back."), (v * t_back * 1e-6 / 2 * 1000, "That is the thickness of the plate; use the CRACK echo."), (depth / 1000, "The answer is in mm.")],
              "mm", f"Ultrasound is used to check a steel plate for cracks.\n\n{md_table(['quantity', 'value'], [['time for echo from back of plate', f'{t_back} µs'], ['time for echo from a crack', f'{fmt(t_crack)} µs'], ['speed of ultrasound in steel', '5900 m/s']])}\n\nHow deep below the surface is the crack, in mm?",
              "depth = v t ÷ 2 (crack echo)", [f"depth = 5900 × {fmt(t_crack)} × 10⁻⁶ ÷ 2 = {fmt(depth / 1000)} m", f"= **{fmt(depth)} mm**"],
              ["Use the echo from the crack.", "Convert µs to s.", "Halve, then convert to mm."])


# ================================================================== L5
@template("c10x_two_observer_speed", chapter=10, level=5, lo="10i")
def two_observer_speed(rng):
    d = nice(rng, 400, 500, 600)
    times = [nice(rng, 1.42, 1.48, 1.52), nice(rng, 1.46, 1.50, 1.54), nice(rng, 1.44, 1.47, 1.56)]
    avg = sum(times) / 3
    v = d / avg
    return mk(rng, v, [(2 * d / avg, "The sound travels one way only (no echo)."), (d / times[0], "Use the average of the three times."), (d / sum(times), "Divide the total time by 3 first.")],
              "m/s", f"Two students stand **{d} m** apart. One fires a starting pistol; the other starts a stopwatch on seeing the smoke and stops it on hearing the bang.\n\n{md_table(['trial', 'time / s'], [[i + 1, fmt(t)] for i, t in enumerate(times)])}\n\nWhat is the speed of sound from these results?",
              "average t; v = d ÷ t", [f"average t = {fmt(avg, sf=3)} s", f"v = {d} ÷ {fmt(avg, sf=3)} = **{fmt(v)} m/s**"],
              ["Average the times.", "The sound travels d once.", "v = d ÷ t."])


@template("c10x_echo_moving_ship", chapter=10, level=5, lo="10i")
def echo_moving_ship(rng):
    t = nice(rng, 4.0, 5.0, 6.0)
    v_ship = nice(rng, 10, 15, 20)
    v = V_AIR
    D = (v + v_ship) * t / 2
    return mk(rng, D, [(v * t / 2, "The ship moves towards the cliff while the sound travels."), ((v - v_ship) * t / 2, "The ship moves TOWARDS the cliff, shortening the return path."), ((v + v_ship) * t, "Halve the combined distance.")],
              "m", f"A ship sails straight towards a cliff and sounds its horn. The echo is heard back on the ship.\n\n{md_table(['quantity', 'value'], [['time for echo', f'{fmt(t)} s'], ['speed of ship', f'{v_ship} m/s'], ['speed of sound', '340 m/s']])}\n\nHow far was the ship from the cliff when the horn sounded?",
              "sound path + ship path = 2D → D = (v_sound + v_ship) t ÷ 2", [f"sound travels {fmt(v * t)} m; ship moves {fmt(v_ship * t)} m", f"D = ({fmt(v * t)} + {fmt(v_ship * t)}) ÷ 2 = **{fmt(D)} m**"],
              ["Draw the paths of the sound and the ship.", "Together they cover twice the starting distance.", "Halve the sum."])


@template("c10x_pulse_rate_sonar", chapter=10, level=5, lo="10j")
def pulse_rate_sonar(rng):
    depth = nice(rng, 750, 1500, 3000)
    t = 2 * depth / 1500
    f = 1 / t
    return mk(rng, f, [(1500 / depth, "Each pulse must travel down AND back before the next."), (t, "That is the time; the maximum rate is 1 ÷ t."), (2 * f, "Use the full round-trip time.")],
              "pulses per second", f"A sonar must receive each echo before sending the next pulse.\n\n{md_table(['quantity', 'value'], [['depth of sea', f'{depth} m'], ['speed of sound in sea water', '1500 m/s']])}\n\nWhat is the greatest number of pulses it can send each second?",
              "round-trip time t = 2d ÷ v; max rate = 1 ÷ t", [f"t = 2 × {depth} ÷ 1500 = {fmt(t)} s", f"rate = 1 ÷ {fmt(t)} = **{fmt(f)} pulses per second**"],
              ["Find the round-trip time.", "One pulse per round trip.", "Rate = 1 ÷ t."])


@template("c10x_bat_insect", chapter=10, level=5, lo="10j")
def bat_insect(rng):
    d = nice(rng, 1.7, 3.4, 5.1)
    f = nice(rng, 40000, 50000, 80000)
    t = 2 * d / V_AIR
    lam = V_AIR / f * 1000
    return mk(rng, t * 1000, [(d / V_AIR * 1000, "The ultrasound travels to the insect AND back."), (t, "That is in s; the answer is in ms."), (lam, "That is the wavelength in mm, not the time.")],
              "ms", f"A bat emits ultrasound to find an insect.\n\n{md_table(['quantity', 'value'], [['distance to insect', f'{fmt(d)} m'], ['frequency of ultrasound', f'{f} Hz'], ['speed of sound in air', '340 m/s']])}\n\nHow long after emitting a pulse does the bat hear the echo, in ms?",
              "t = 2 d ÷ v", [f"t = 2 × {fmt(d)} ÷ 340 = {fmt(t)} s", f"= **{fmt(t * 1000)} ms**"],
              ["The frequency is not needed for the time.", "The echo travels 2d.", "Convert s to ms."])


@template("c10x_cro_compare_notes", chapter=10, level=5, lo="10c")
def cro_compare_notes(rng):
    p1 = nice(rng, 4, 5)
    k = nice(rng, 2, 2.5)
    p2 = p1 / k
    tb = nice(rng, 0.5, 1.0)
    f2 = 1 / (p2 * tb / 1000)
    return mk(rng, f2, [(1 / (p1 * tb / 1000), "That is the frequency of the DASHED (lower) note."), (1 / (p2 * tb), "Convert ms to s."), (f2 / k, "Use the solid trace's period.")],
              "Hz", f"Fig. 1 shows two notes on an oscilloscope set to **{fmt(tb)} ms per division**: one solid, one dashed. What is the frequency of the note shown by the SOLID trace?",
              "T = divisions × time-base; f = 1 ÷ T", [f"solid: one wave spans {fmt(p2)} divisions → T = {fmt(p2 * tb)} ms", f"f = 1 ÷ {fmt(p2 * tb / 1000)} s = **{fmt(f2)} Hz**"],
              ["Identify the solid trace.", "Count divisions for one of its waves.", "T then f."], figure=figs2.cro_trace(p2, 3, f"time-base: 1 division = {fmt(tb)} ms", (p1, 1.5)))


@template("c10x_wave_displacement_time", chapter=10, level=5, lo="10c")
def wave_displacement_time(rng):
    T = nice(rng, 0.2, 0.4, 0.5)
    lam = nice(rng, 0.6, 0.8, 1.2)
    f = 1 / T
    d = lam * f * nice(rng, 3, 5)
    t = d / (f * lam)
    return mk(rng, t, [(d / lam, "That is the number of wavelengths; multiply by the period."), (d * f * lam, "t = d ÷ v."), (t / 2, "Use v = λ ÷ T.")],
              "s", f"Fig. 1 shows the displacement–time graph for one particle of a wave. The wavelength is **{fmt(lam)} m**. How long does the wave take to travel **{fmt(d)} m**?",
              "read T; v = λ ÷ T; t = d ÷ v", [f"from the graph T = {fmt(T)} s, so v = {fmt(lam)} ÷ {fmt(T)} = {fmt(lam / T)} m/s", f"t = {fmt(d)} ÷ {fmt(lam / T)} = **{fmt(t)} s**"],
              ["Read the period from the graph.", "Find the wave speed.", "t = d ÷ v."], figure=sketches.wave_graph(2, T, "time", cycles=2))


@template("c10x_ripple_depth_change", chapter=10, level=5, lo="10a")
def ripple_depth_change(rng):
    f = nice(rng, 5, 8, 10)
    lam_deep = nice(rng, 2.0, 2.4, 3.0)
    k = nice(rng, 0.5, 0.6, 0.75)
    lam_sh = lam_deep * k
    v_sh = f * lam_sh
    return mk(rng, v_sh, [(f * lam_deep, "That is the speed in DEEP water; λ is shorter in shallow water."), (lam_sh / f, "v = f λ."), (f * lam_sh / 100, "Keep cm/s.")],
              "cm/s", f"Waves in a ripple tank pass from deep into shallow water. The frequency does not change.\n\n{md_table(['region', 'wavelength / cm'], [['deep', fmt(lam_deep)], ['shallow', fmt(lam_sh)]])}\n\nThe dipper vibrates at **{f} Hz**. What is the wave speed in the shallow water?",
              "f unchanged; v = f λ in each region", [f"v_shallow = {f} × {fmt(lam_sh)} = **{fmt(v_sh)} cm/s**"],
              ["The frequency is set by the dipper.", "Use the shallow-water wavelength.", "v = f λ."])


@template("c10x_wavefronts_count", chapter=10, level=5, lo="10a")
def wavefronts_count(rng):
    v = nice(rng, 15, 20, 24)
    f = nice(rng, 5, 6, 8)
    L = nice(rng, 30, 40, 48)
    lam = v / f
    n = L / lam
    return mk(rng, n, [(L * f / v + 1, "Count wavelengths in the length (gaps), not wavefront lines."), (L / v, "That is a time, not a number of waves."), (n / 2, "Number of wavelengths = L ÷ λ.")],
              "wavelengths", f"Straight waves cross a ripple tank.\n\n{md_table(['quantity', 'value'], [['wave speed', f'{v} cm/s'], ['frequency', f'{f} Hz'], ['length of tank', f'{L} cm']])}\n\nHow many complete wavelengths fit across the tank at any instant?",
              "λ = v ÷ f; number = L ÷ λ", [f"λ = {v} ÷ {f} = {fmt(lam)} cm", f"number = {L} ÷ {fmt(lam)} = **{fmt(n)}**"],
              ["Find the wavelength.", "Divide the length by λ.", "That gives the number of wavelengths."])
