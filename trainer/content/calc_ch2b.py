"""Chapter 2 Kinematics (6091) bank extension: calculation templates so each level has 10, every LO at least twice.
Contexts adapted from the question bank (SEAB 2014-2025, school papers 2024-2025)."""
from .. import figs, figs2, sketches
from .base import fmt, md_table, mk, nice, template

G = 10


def vt(pts, xlabel="time / s", ylabel="velocity / m/s", labels=None):
    xs, ys = zip(*pts)
    xstep = next(s for s in (1, 2, 5, 10, 20, 50) if max(xs) / s <= 8)
    xmax = (int(max(xs) / xstep) + (1 if max(xs) % xstep else 0)) * xstep
    ystep = next(s for s in (1, 2, 5, 10, 20, 50, 100) if max(ys) / s <= 6)
    ymax = (int(max(ys) / ystep) + 1) * ystep
    return figs.graph(pts, xmax, ymax, xstep, ystep, xlabel=xlabel, ylabel=ylabel, labels=labels)


# ================================================================== L1
@template("c2b_time_from_distance_speed", chapter=2, level=1, lo="2b")
def time_from_distance_speed(rng):
    v = nice(rng, 2, 4, 5, 8, 12, 15, 25)
    t = nice(rng, 6, 8, 10, 20, 30, 40)
    d = v * t
    return mk(rng, t, [(d * v, "You multiplied. time = distance ÷ speed."), (v / d, "You divided the wrong way round: t = d ÷ v."), (d / 2 / v, "Use the full distance.")],
              "s", f"A cyclist travels **{d} m** at a steady speed of **{v} m/s** (Fig. 1). How long does the journey take?",
              "speed = distance ÷ time → time = distance ÷ speed", [f"t = {d} ÷ {v} = **{t} s**"],
              ["Which formula links speed, distance and time?", "Rearrange it for time.", f"{d} ÷ {v}."],
              figure=sketches.motion_sketch("start", "finish", f"{d} m at {v} m/s"))


@template("c2b_deceleration_magnitude", chapter=2, level=1, lo="2c")
def deceleration_magnitude(rng):
    u = nice(rng, 12, 15, 20, 24, 30)
    t = nice(rng, 2, 3, 4, 5, 6)
    v = u - nice(rng, 1, 2, 3) * t if u - 3 * t > 0 else 0
    a = (u - v) / t
    return mk(rng, a, [(u / t, "Use the CHANGE in velocity (initial − final), not the initial velocity alone." if v else "Check the change in speed."),
                       ((u + v) / t, "The change in velocity is final − initial, not their sum."), ((u - v) * t, "Divide the change by the time; do not multiply.")],
              "m/s²", f"A car brakes on a straight road.\n\n{md_table(['', 'value'], [['initial speed', f'{u} m/s'], ['final speed', f'{v} m/s'], ['time taken', f'{t} s']])}\n\nWhat is the magnitude of its deceleration?",
              "a = (v − u) ÷ t; deceleration = magnitude of a negative acceleration", [f"a = ({v} − {u}) ÷ {t} = {fmt(-a)} m/s²", f"deceleration = **{fmt(a)} m/s²**"],
              ["Acceleration = change in velocity ÷ time.", "The velocity decreases, so the change is negative.", f"({u} − {v}) ÷ {t}."])


@template("c2b_accel_from_rest", chapter=2, level=1, lo="2c")
def accel_from_rest(rng):
    a = nice(rng, 1.5, 2.0, 2.5, 3.0, 4.0, 0.5)
    t = nice(rng, 4, 5, 6, 8, 10)
    v = a * t
    return mk(rng, a, [(v * t, "Divide the change in velocity by the time."), (t / v, "a = Δv ÷ t, not t ÷ Δv."), (v / 2 / t, "There is no halving: the car starts from rest, so Δv = v.")],
              "m/s²", f"Fig. 1 shows a lorry starting from rest and reaching **{fmt(v)} m/s** in **{t} s** with uniform acceleration. What is its acceleration?",
              "a = (v − u) ÷ t", [f"a = ({fmt(v)} − 0) ÷ {t} = **{fmt(a)} m/s²**"],
              ["What is the starting velocity?", "Change in velocity = v − 0.", f"{fmt(v)} ÷ {t}."], figure=sketches.motion_sketch("0 m/s", f"{fmt(v)} m/s", f"{t} s", body_label="lorry"))


@template("c2b_freefall_speed", chapter=2, level=1, lo="2i")
def freefall_speed(rng):
    t = nice(rng, 1.0, 1.5, 2.0, 2.5, 3.0, 0.8)
    v = G * t
    return mk(rng, v, [(G * t * t / 2, "That is the distance fallen. The speed is g × t."), (G / t, "Multiply g by the time."), (9.8 * t if abs(9.8 * t - v) > 0.05 else v + 5, "Use g = 10 m/s² as in the O-level papers.")],
              "m/s", f"A stone is dropped from rest from a bridge. Air resistance is negligible.\n\n{md_table(['quantity', 'value'], [['acceleration of free fall', '10 m/s²'], ['time after release', f'{fmt(t)} s']])}\n\nWhat is its speed at this time?",
              "free fall from rest: v = g t (acceleration of free fall ≈ 10 m/s²)", [f"v = 10 × {fmt(t)} = **{fmt(v)} m/s**"],
              ["What is the acceleration of a freely falling object?", "Its speed increases by 10 m/s every second.", f"10 × {fmt(t)}."])


@template("c2b_freefall_time", chapter=2, level=1, lo="2i")
def freefall_time(rng):
    v = nice(rng, 15, 20, 25, 30, 35, 40)
    t = v / G
    return mk(rng, t, [(v * G, "You multiplied. t = v ÷ g."), (G / v, "t = v ÷ g, not g ÷ v."), (t * 2, "From rest, the time is v ÷ g; do not double it.")],
              "s", f"A ball falls from rest with negligible air resistance.\n\n{md_table(['quantity', 'value'], [['final speed', f'{v} m/s'], ['acceleration of free fall', '10 m/s²']])}\n\nHow long has it been falling?",
              "v = g t → t = v ÷ g", [f"t = {v} ÷ 10 = **{fmt(t)} s**"],
              ["The speed rises by 10 m/s each second.", "How many seconds to reach the final speed?", f"{v} ÷ 10."])


@template("c2b_dt_gradient_speed", chapter=2, level=1, lo="2e")
def dt_gradient_speed(rng):
    v = nice(rng, 2, 3, 4, 5, 6, 8)
    T = nice(rng, 5, 8, 10)
    pts = [(0, 0), (T, v * T)]
    return mk(rng, v, [(v * T, "That is the distance at the end. Speed = gradient = distance ÷ time."), (1 / v, "Gradient = rise ÷ run = distance ÷ time."), (v * T / 2, "Use the full distance and full time.")],
              "m/s", "Fig. 1 is the distance-time graph of a toy car. What is the speed of the car?",
              "speed = gradient of the distance-time graph", [f"gradient = {v * T} m ÷ {T} s = **{v} m/s**"],
              ["What does the gradient of a distance-time graph represent?", "Pick two points on the line.", "rise ÷ run."],
              figure=vt(pts, ylabel="distance / m"))


@template("c2b_read_vt_value", chapter=2, level=1, lo="2e")
def read_vt_value(rng):
    a = nice(rng, 1, 2, 3)
    T = nice(rng, 8, 10)
    t = nice(rng, 2, 3, 4, 5, 6)
    pts = [(0, 0), (T, a * T)]
    v = a * t
    return mk(rng, v, [(a * T, "That is the velocity at the end of the graph, not at the time asked."), (t, "That is the time, not the velocity."), (a * t * t / 2, "That is the area (distance). Read the velocity off the line.")],
              "m/s", f"Fig. 1 is the velocity-time graph of a trolley. What is its velocity at **t = {t} s**?",
              "read across from the graph", [f"at t = {t} s the line is at **{v} m/s**"],
              ["Find the time on the horizontal axis.", "Go up to the line, then across.", "Read the velocity axis."],
              figure=vt(pts))


# ================================================================== L2
@template("c2b_km_min_to_ms", chapter=2, level=2, lo="2b")
def km_min_to_ms(rng):
    d_km = nice(rng, 1.2, 1.8, 2.4, 3.0, 4.5, 6.0)
    t_min = nice(rng, 4, 5, 6, 8, 10, 12)
    v = d_km * 1000 / (t_min * 60)
    return mk(rng, v, [(d_km / t_min, "Convert km to m and minutes to seconds first."), (d_km * 1000 / t_min, "Convert the minutes to seconds as well."), (d_km / (t_min * 60), "Convert km to m (× 1000).")],
              "m/s", f"A runner covers **{fmt(d_km)} km** in **{t_min} minutes** (Fig. 1). What is the average speed in m/s?",
              "v = d ÷ t with d in m and t in s", [f"d = {fmt(d_km * 1000)} m, t = {t_min * 60} s", f"v = {fmt(d_km * 1000)} ÷ {t_min * 60} = **{fmt(v)} m/s**"],
              ["The answer is in m/s. Which units must change?", "km → m (× 1000), min → s (× 60).", "Divide."],
              figure=sketches.motion_sketch("start", "finish", f"{fmt(d_km)} km in {t_min} min", body="box"))


@template("c2b_distance_minutes", chapter=2, level=2, lo="2b")
def distance_minutes(rng):
    v = nice(rng, 1.5, 2.0, 2.5, 4.0, 5.0)
    t_min = nice(rng, 2, 3, 5, 8, 10)
    d = v * t_min * 60
    return mk(rng, d, [(v * t_min, "Convert minutes to seconds before multiplying by a speed in m/s."), (v * t_min * 60 / 1000, "That is in km; the answer is asked in m."), (v / (t_min * 60), "distance = speed × time.")],
              "m", f"An escalator moves at a steady **{fmt(v)} m/s**.\n\n{md_table(['quantity', 'value'], [['speed', f'{fmt(v)} m/s'], ['time', f'{t_min} min']])}\n\nHow far does a point on the escalator move?",
              "d = v t with t in seconds", [f"t = {t_min} × 60 = {t_min * 60} s", f"d = {fmt(v)} × {t_min * 60} = **{fmt(d)} m**"],
              ["Check that the units match.", "Change minutes into seconds.", "Multiply."])


@template("c2b_final_velocity", chapter=2, level=2, lo="2c")
def final_velocity(rng):
    u = nice(rng, 2, 4, 5, 6, 10)
    a = nice(rng, 0.5, 1.5, 2.0, 2.5, 3.0)
    t = nice(rng, 2, 4, 5, 6, 8)
    v = u + a * t
    return mk(rng, v, [(a * t, "That is only the GAIN in velocity. Add the initial velocity."), (u * a * t, "v = u + at: add, don't multiply u in."), (u + a / t, "Multiply a by t.")],
              "m/s", f"A motorcycle moving at **{u} m/s** accelerates uniformly at **{fmt(a)} m/s²** for **{t} s** (Fig. 1). What is its final velocity?",
              "a = (v − u) ÷ t → v = u + a t", [f"v = {u} + {fmt(a)} × {t} = **{fmt(v)} m/s**"],
              ["Acceleration tells you how much the velocity rises each second.", f"Gain = {fmt(a)} × {t}.", "Add it to the starting velocity."],
              figure=sketches.motion_sketch(f"{u} m/s", "v = ?", f"a = {fmt(a)} m/s² for {t} s", body_label="bike"))


@template("c2b_time_to_reach", chapter=2, level=2, lo="2c")
def time_to_reach(rng):
    a = nice(rng, 0.5, 1.5, 2.0, 2.5, 4.0)
    v = nice(rng, 10, 12, 15, 20, 30)
    t = v / a
    return mk(rng, t, [(v * a, "t = Δv ÷ a; you multiplied."), (a / v, "t = Δv ÷ a, not a ÷ Δv."), (t / 2, "From rest, the time is v ÷ a.")],
              "s", f"A train starts from rest.\n\n{md_table(['quantity', 'value'], [['acceleration', f'{fmt(a)} m/s²'], ['speed to reach', f'{v} m/s']])}\n\nHow long does it take to reach this speed?",
              "a = Δv ÷ t → t = Δv ÷ a", [f"t = {v} ÷ {fmt(a)} = **{fmt(t)} s**"],
              ["Rearrange a = Δv ÷ t for t.", "Δv = final − 0.", f"{v} ÷ {fmt(a)}."])


@template("c2b_accel_from_table", chapter=2, level=2, lo="2c")
def accel_from_table(rng):
    a = nice(rng, 1.5, 2.0, 2.5, 3.0)
    u = nice(rng, 2, 4, 5)
    ts = [0, 1, 2, 3, 4]
    rows = [[t, fmt(u + a * t)] for t in ts]
    return mk(rng, a, [(u + a * 4, "That is the velocity at 4 s, not the acceleration."), ((u + a * 4) / 4, "Use the CHANGE in velocity: (final − initial) ÷ time."), (a * 4, "That is the total change in velocity over 4 s; divide by 4 s.")],
              "m/s²", f"The velocity of a car is recorded every second.\n\n{md_table(['time / s', 'velocity / m/s'], rows)}\n\nWhat is the acceleration of the car?",
              "a = change in velocity ÷ time taken", [f"Δv = {fmt(u + 4 * a)} − {u} = {fmt(4 * a)} m/s in 4 s", f"a = **{fmt(a)} m/s²**"],
              ["By how much does the velocity rise each second?", "Or use the first and last rows.", "Δv ÷ Δt."])


@template("c2b_dt_offset_speed", chapter=2, level=2, lo="2e")
def dt_offset_speed(rng):
    d0 = nice(rng, 10, 20, 30)
    v = nice(rng, 2, 4, 5)
    T = nice(rng, 8, 10)
    pts = [(0, d0), (T, d0 + v * T)]
    return mk(rng, v, [((d0 + v * T) / T, "The graph does not start at 0 m. Use the CHANGE in distance."), (d0 / T, "Use the rise of the line over the time."), (v * T, "That is the distance covered, not the speed.")],
              "m/s", "Fig. 1 is the distance-time graph of a walker who starts some distance from a lamp-post. What is the walker's speed?",
              "speed = gradient = change in distance ÷ change in time", [f"gradient = ({d0 + v * T} − {d0}) ÷ {T} = **{v} m/s**"],
              ["Does the line start at the origin?", "Use the rise between two points.", "rise ÷ run."],
              figure=vt(pts, ylabel="distance / m"))


@template("c2b_vt_decreasing_read", chapter=2, level=2, lo="2e")
def vt_decreasing_read(rng):
    u = nice(rng, 20, 24, 30)
    T = nice(rng, 6, 8, 10)
    t = nice(rng, 2, 3, 4)
    v = u - u / T * t
    return mk(rng, v, [(u, "That is the starting velocity."), (u / T * t, "That is the drop in velocity, not the velocity at that time."), (u - t, "Read the graph: the velocity falls by more than 1 m/s per second.")],
              "m/s", f"Fig. 1 is the velocity-time graph of a car braking to a stop. What is the velocity at **t = {t} s**?",
              "read the velocity from the line at the given time", [f"at t = {t} s the line reads **{fmt(v)} m/s**"],
              ["Find the time on the horizontal axis.", "Go up to the line.", "Read across."],
              figure=vt([(0, u), (T, 0)]))


@template("c2b_area_rectangle", chapter=2, level=2, lo="2h")
def area_rectangle(rng):
    v = nice(rng, 4, 5, 6, 8, 10, 12)
    T = nice(rng, 5, 8, 10, 15, 20)
    return mk(rng, v * T, [(v * T / 2, "The area under a horizontal line is a RECTANGLE, not a triangle."), (v / T, "Distance = area = velocity × time."), (v + T, "Multiply, don't add.")],
              "m", "Fig. 1 is the velocity-time graph of a bus moving at constant velocity. How far does it travel?",
              "distance = area under the velocity-time graph (rectangle)", [f"area = {v} × {T} = **{v * T} m**"],
              ["What does the area under a velocity-time graph give?", "The shape is a rectangle.", "height × width."],
              figure=vt([(0, v), (T, v)]))


@template("c2b_area_triangle_rest", chapter=2, level=2, lo="2h")
def area_triangle_rest(rng):
    v = nice(rng, 6, 8, 10, 12, 16, 20)
    T = nice(rng, 4, 5, 8, 10)
    return mk(rng, v * T / 2, [(v * T, "The area is a TRIANGLE: ½ × base × height."), (v / T, "Distance = area, not gradient."), (v * T / 4, "Use ½ × base × height once.")],
              "m", "Fig. 1 is the velocity-time graph of a car accelerating uniformly from rest. How far does it travel in this time?",
              "distance = area under the graph = ½ × base × height", [f"area = ½ × {T} × {v} = **{fmt(v * T / 2)} m**"],
              ["Distance comes from the area under the line.", "Here the shape is a triangle.", "½ × base × height."],
              figure=vt([(0, 0), (T, v)]))


# ================================================================== L3
@template("c2b_vt_gradient_decel", chapter=2, level=3, lo="2e")
def vt_gradient_decel(rng):
    v = nice(rng, 12, 15, 18, 20, 24)
    t1 = nice(rng, 4, 5, 6)
    t2 = t1 + nice(rng, 3, 4, 5, 6)
    d = v / (t2 - t1)
    return mk(rng, d, [(v / t2, "Use only the time of the sloping part (when it is slowing down)."), (v / t1, "That uses the constant-speed time, not the braking time."), (v * (t2 - t1) / 2, "That is the area (braking distance), not the gradient.")],
              "m/s²", "Fig. 1 is the velocity-time graph of a cyclist who rides at constant speed and then brakes to rest. What is the deceleration while braking?",
              "deceleration = magnitude of the gradient of the sloping section", [f"gradient = (0 − {v}) ÷ ({t2} − {t1}) = −{fmt(d)} m/s²", f"deceleration = **{fmt(d)} m/s²**"],
              ["Which section shows the braking?", "Gradient = change in velocity ÷ time for that section.", f"{v} ÷ {t2 - t1}."],
              figure=vt([(0, v), (t1, v), (t2, 0)]))


@template("c2b_dt_second_segment", chapter=2, level=3, lo="2e")
def dt_second_segment(rng):
    v1, v2 = nice(rng, 2, 3, 4), nice(rng, 5, 6, 8)
    t1, t2 = nice(rng, 4, 5), nice(rng, 9, 10, 12)
    pts = [(0, 0), (t1, v1 * t1), (t2, v1 * t1 + v2 * (t2 - t1))]
    return mk(rng, v2, [(pts[2][1] / t2, "That is the AVERAGE speed for the whole journey. Use only the second section."), (v1, "That is the speed in the first section."), (pts[2][1] / (t2 - t1), "Use the change in distance during the second section only.")],
              "m/s", "Fig. 1 is the distance-time graph of a jogger. What is the jogger's speed during the **second** section of the journey?",
              "speed = gradient of that section", [f"Δd = {pts[2][1]} − {pts[1][1]} = {pts[2][1] - pts[1][1]} m in {t2 - t1} s", f"speed = **{v2} m/s**"],
              ["Which part of the line is the second section?", "Find the rise and run for that section only.", "Δd ÷ Δt."],
              figure=vt(pts, ylabel="distance / m"))


@template("c2b_average_two_segments", chapter=2, level=3, lo="2b")
def average_two_segments(rng):
    d1, t1 = nice(rng, 100, 120, 200), nice(rng, 20, 25, 40)
    d2, t2 = nice(rng, 60, 80, 150), nice(rng, 20, 30, 50)
    v = (d1 + d2) / (t1 + t2)
    return mk(rng, v, [((d1 / t1 + d2 / t2) / 2, "Average speed is total distance ÷ total time, not the average of the two speeds."), (d1 / t1, "That is the speed in the first part only."), ((d1 + d2) / t1, "Use the total time.")],
              "m/s", f"A swimmer's journey has two parts.\n\n{md_table(['part', 'distance / m', 'time / s'], [['1', d1, t1], ['2', d2, t2]])}\n\nWhat is the average speed for the whole journey?",
              "average speed = total distance ÷ total time", [f"total distance = {d1 + d2} m, total time = {t1 + t2} s", f"v = **{fmt(v)} m/s**"],
              ["Add the distances; add the times.", "Do NOT average the two speeds.", "Divide total distance by total time."])


@template("c2b_average_with_stop", chapter=2, level=3, lo="2b")
def average_with_stop(rng):
    d1, t1 = nice(rng, 300, 400, 500), nice(rng, 60, 80, 100)
    stop = nice(rng, 30, 40, 60)
    d2, t2 = nice(rng, 200, 300, 400), nice(rng, 40, 60, 80)
    v = (d1 + d2) / (t1 + stop + t2)
    return mk(rng, v, [((d1 + d2) / (t1 + t2), "The time spent stopped is still part of the journey time."), ((d1 / t1 + d2 / t2) / 2, "Average speed is total distance ÷ total time."), ((d1 + d2) / (t1 + t2 + 2 * stop), "Count the stop once.")],
              "m/s", f"A delivery rider makes a journey with a stop.\n\n{md_table(['stage', 'distance / m', 'time / s'], [['ride', d1, t1], ['stop', 0, stop], ['ride', d2, t2]])}\n\nWhat is the average speed for the whole journey?",
              "average speed = total distance ÷ total time (include the stop)", [f"total distance = {d1 + d2} m; total time = {t1 + stop + t2} s", f"v = **{fmt(v)} m/s**"],
              ["What is the total time, including the stop?", "Distance during the stop is zero.", "Divide."])


@template("c2b_initial_velocity", chapter=2, level=3, lo="2c")
def initial_velocity(rng):
    a = nice(rng, 1.5, 2.0, 2.5, 3.0)
    t = nice(rng, 2, 4, 5, 6)
    u = nice(rng, 4, 5, 6, 8, 10)
    v = u + a * t
    return mk(rng, u, [(v, "That is the final velocity."), (a * t, "That is the GAIN in velocity; subtract it from the final velocity."), (v + a * t, "Subtract the gain, don't add it.")],
              "m/s", f"A sprinter accelerates uniformly.\n\n{md_table(['quantity', 'value'], [['acceleration', f'{fmt(a)} m/s²'], ['time', f'{t} s'], ['final velocity', f'{fmt(v)} m/s']])}\n\nWhat was the velocity at the start of this time?",
              "v = u + a t → u = v − a t", [f"u = {fmt(v)} − {fmt(a)} × {t} = **{fmt(u)} m/s**"],
              ["Write v = u + at.", "Make u the subject.", f"{fmt(v)} − {fmt(a)} × {t}."])


@template("c2b_accel_vt_two_points", chapter=2, level=3, lo="2c")
def accel_vt_two_points(rng):
    u = nice(rng, 4, 5, 6, 8)
    a = nice(rng, 1, 2, 3)
    T = nice(rng, 5, 6, 8)
    v = u + a * T
    return mk(rng, a, [(v / T, "The line does not start at 0 m/s. Use the change in velocity."), (u / T, "Use the rise of the line, not its starting value."), (v, "That is the final velocity, not the acceleration.")],
              "m/s²", "Fig. 1 is the velocity-time graph of a van. What is its acceleration?",
              "a = gradient = (v − u) ÷ t", [f"a = ({v} − {u}) ÷ {T} = **{fmt(a)} m/s²**"],
              ["What does the gradient of a velocity-time graph represent?", "Read the starting and final velocities.", "Change ÷ time."],
              figure=vt([(0, u), (T, v)]))


@template("c2b_freefall_distance", chapter=2, level=3, lo="2i")
def freefall_distance(rng):
    t = nice(rng, 1.0, 1.5, 2.0, 2.5, 3.0)
    v = G * t
    d = v * t / 2
    return mk(rng, d, [(v * t, "That treats the speed as constant. The stone speeds up from 0, so use the triangle area (½ v t)."), (v, "That is the speed reached, not the distance."), (G * t, "The distance is the area under the v-t graph.")],
              "m", f"A stone is dropped from rest (g = 10 m/s², no air resistance). Fig. 1 is its velocity-time graph. How far does it fall in **{fmt(t)} s**?",
              "distance = area under the v-t graph = ½ × t × (g t)", [f"v after {fmt(t)} s = {fmt(v)} m/s", f"d = ½ × {fmt(t)} × {fmt(v)} = **{fmt(d)} m**"],
              ["What is its speed after that time?", "The graph is a triangle from the origin.", "½ × base × height."],
              figure=vt([(0, 0), (t, v)]))


@template("c2b_freefall_from_graph", chapter=2, level=3, lo="2i")
def freefall_from_graph(rng):
    T = nice(rng, 2, 3, 4)
    v = G * T
    return mk(rng, G, [(v, "That is the final speed, not the acceleration."), (v / 2 / T, "Gradient = Δv ÷ Δt, no halving."), (1 / G, "Gradient = rise ÷ run.")],
              "m/s²", "Fig. 1 is the velocity-time graph of a ball dropped from rest with negligible air resistance. Use the graph to find the acceleration of free fall.",
              "acceleration = gradient of the v-t graph", [f"gradient = {v} ÷ {T} = **10 m/s²**"],
              ["What does the gradient of a v-t graph give?", "Read the final velocity and time.", "rise ÷ run."],
              figure=vt([(0, 0), (T, v)]))


# ================================================================== L4
@template("c2b_vt_curve_compare", chapter=2, level=4, lo="2e")
def vt_curve_compare(rng):
    a1 = nice(rng, 2, 3, 4)
    a2 = a1 / 2
    T1 = nice(rng, 4, 5)
    pts = [(0, 0), (T1, a1 * T1), (T1 + 4, a1 * T1 + a2 * 4)]
    ratio = a1 / a2
    return mk(rng, ratio, [(1 / ratio, "The first section is STEEPER, so its acceleration is larger: ratio > 1."), (pts[1][1] / pts[2][1], "Compare gradients, not velocities."), (ratio * 2, "Compute both gradients carefully.")],
              "", "Fig. 1 is the velocity-time graph of a scooter that accelerates in two stages. How many times greater is the acceleration in the first stage than in the second?",
              "acceleration = gradient; compare the gradients of the two sections", [f"first: {a1 * T1} ÷ {T1} = {a1} m/s²; second: {fmt(a2 * 4)} ÷ 4 = {fmt(a2)} m/s²", f"ratio = **{fmt(ratio)}**"],
              ["Find the gradient of each section.", "Use the change in velocity for each section on its own.", "Divide the first by the second."],
              figure=vt(pts))


@template("c2b_freefall_compare_masses", chapter=2, level=4, lo="2i")
def freefall_compare_masses(rng):
    h_t = nice(rng, 1.5, 2.0, 2.5)
    m1, m2 = nice(rng, 0.5, 1.0), nice(rng, 2.0, 5.0)
    v = G * h_t
    return mk(rng, v, [(v * m2 / m1, "In free fall (no air resistance) all objects have the same acceleration, whatever their mass."), (v / 2, "Both reach the same speed in the same time."), (G * h_t * h_t / 2, "That is the distance fallen, not the speed.")],
              "m/s", f"Two balls are dropped together from a high tower with negligible air resistance.\n\n{md_table(['ball', 'mass / kg'], [['P', fmt(m1)], ['Q', fmt(m2)]])}\n\nWhat is the speed of ball **Q** after **{fmt(h_t)} s**?",
              "free fall: acceleration = g ≈ 10 m/s² for every mass; v = g t", [f"v = 10 × {fmt(h_t)} = **{fmt(v)} m/s** (the same for P and Q)"],
              ["Does the mass change the acceleration of free fall?", "No: both accelerate at 10 m/s².", f"10 × {fmt(h_t)}."])


@template("c2b_average_from_vt", chapter=2, level=4, lo="2b")
def average_from_vt(rng):
    v = nice(rng, 6, 8, 10, 12)
    t1, t2, t3 = nice(rng, 4, 5), nice(rng, 10, 12), nice(rng, 16, 18)
    area = 0.5 * t1 * v + (t2 - t1) * v + 0.5 * (t3 - t2) * v
    av = area / t3
    return mk(rng, av, [(v, "That is the top speed, not the average speed."), (v / 2, "The average is total distance ÷ total time, not half the top speed."), (area, "That is the distance; divide by the total time.")],
              "m/s", "Fig. 1 is the velocity-time graph of a train between two stations. What is its average speed?",
              "average speed = total area (distance) ÷ total time", [f"area = ½×{t1}×{v} + {t2 - t1}×{v} + ½×{t3 - t2}×{v} = {fmt(area)} m", f"average = {fmt(area)} ÷ {t3} = **{fmt(av)} m/s**"],
              ["First find the total distance from the area.", "Split the area into triangles and a rectangle.", "Divide by the total time."],
              figure=vt([(0, 0), (t1, v), (t2, v), (t3, 0)]))


@template("c2b_journey_table_average", chapter=2, level=4, lo="2b")
def journey_table_average(rng):
    v1, t1 = nice(rng, 20, 25, 30), nice(rng, 10, 15, 20)
    v2, t2 = nice(rng, 10, 12, 15), nice(rng, 20, 25, 30)
    d = v1 * t1 * 60 + v2 * t2 * 60
    av = d / ((t1 + t2) * 60)
    return mk(rng, av, [((v1 + v2) / 2, "The car spends different times at each speed, so you cannot simply average the speeds."), (d / (t1 + t2), "Convert minutes to seconds."), (v1, "That is the speed of the first part only.")],
              "m/s", f"A car's journey has two stages.\n\n{md_table(['stage', 'speed / m/s', 'time / min'], [['1', v1, t1], ['2', v2, t2]])}\n\nWhat is the average speed for the whole journey?",
              "average speed = total distance ÷ total time", [f"d = {v1}×{t1 * 60} + {v2}×{t2 * 60} = {d} m", f"t = {(t1 + t2) * 60} s", f"average = **{fmt(av)} m/s**"],
              ["Find the distance of each stage (speed × time in s).", "Add distances and times.", "Divide."])


@template("c2b_accel_ratio_graph", chapter=2, level=4, lo="2c")
def accel_ratio_graph(rng):
    vA, vB = nice(rng, 12, 16, 20), nice(rng, 6, 8, 10)
    tA, tB = nice(rng, 4, 5), nice(rng, 8, 10)
    aA, aB = vA / tA, vB / tB
    return mk(rng, aA / aB, [(aB / aA, "Car A's line is steeper, so its acceleration is larger."), (vA / vB, "Compare the gradients, not the final speeds."), (tB / tA, "Use both velocity and time for each car.")],
              "", f"Two cars start from rest.\n\n{md_table(['car', 'final velocity / m/s', 'time / s'], [['A', vA, tA], ['B', vB, tB]])}\n\nHow many times greater is the acceleration of car A than that of car B?",
              "a = Δv ÷ t for each; then divide", [f"a_A = {vA} ÷ {tA} = {fmt(aA)} m/s²; a_B = {vB} ÷ {tB} = {fmt(aB)} m/s²", f"ratio = **{fmt(aA / aB)}**"],
              ["Work out each acceleration.", "a = Δv ÷ t.", "Divide A's by B's."])


@template("c2b_accel_kmh", chapter=2, level=4, lo="2c")
def accel_kmh(rng):
    v_kmh = nice(rng, 36, 54, 72, 90, 108)
    t = nice(rng, 5, 6, 8, 10, 12)
    a = v_kmh / 3.6 / t
    return mk(rng, a, [(v_kmh / t, "Convert km/h to m/s first (÷ 3.6)."), (v_kmh * 3.6 / t, "km/h → m/s is ÷ 3.6, not × 3.6."), (v_kmh / 3.6 * t, "Divide by the time.")],
              "m/s²", f"A car accelerates uniformly from rest to **{v_kmh} km/h** in **{t} s** (Fig. 1). What is its acceleration?",
              "convert km/h to m/s (÷ 3.6), then a = Δv ÷ t", [f"{v_kmh} km/h = {fmt(v_kmh / 3.6)} m/s", f"a = {fmt(v_kmh / 3.6)} ÷ {t} = **{fmt(a)} m/s²**"],
              ["The acceleration must come out in m/s².", "Change km/h to m/s first.", "Then Δv ÷ t."],
              figure=sketches.motion_sketch("0 km/h", f"{v_kmh} km/h", f"{t} s"))


# ================================================================== L5
@template("c2b_catch_up_distance", chapter=2, level=5, lo="2h")
def catch_up_distance(rng):
    v = nice(rng, 10, 12, 15, 20)
    T = nice(rng, 10, 12, 16, 20)
    vp = 2 * v
    d = v * T
    return mk(rng, d, [(v * T / 2, "At the meeting time both have covered the SAME distance; the car's area is v × T."), (vp * T, "The police car accelerates from rest, so its area is a triangle, not a rectangle."), (v * T * 2, "Use the area of either graph at the meeting time.")],
              "m", f"A car passes a parked police car at a steady **{v} m/s**. At that instant the police car starts from rest with uniform acceleration and catches the car **{T} s** later, as shown in Fig. 1. How far from the start does it catch the car?",
              "both areas (distances) are equal at the catch-up time; car: v × T", [f"car: {v} × {T} = {d} m", f"police car: ½ × {T} × {vp} = {d} m ✓", f"**{d} m**"],
              ["At the catch-up moment, what is the same for both vehicles?", "Distance = area under each graph up to T.", "Use the car's rectangle (or the police car's triangle)."],
              figure=figs2.two_curves([("car", [(0, v), (T, v)]), ("police car", [(0, 0), (T, vp)])], T, vp + 5, 2 if T <= 16 else 5, 5, ylabel="velocity / m/s", xlabel="time / s"))


@template("c2b_stopping_with_reaction", chapter=2, level=5, lo="2c")
def stopping_with_reaction(rng):
    v = nice(rng, 12, 15, 20, 25)
    tr = nice(rng, 0.6, 0.7, 0.8)
    a = nice(rng, 5, 6, 8, 10)
    tb = v / a
    a_needed = a
    return mk(rng, a_needed, [(v / (tr + tb), "The car does NOT slow down during the reaction time. Use only the braking time."), (v / tr, "That uses the reaction time instead of the braking time."), (v * tb, "a = Δv ÷ t, not Δv × t.")],
              "m/s²", f"A driver moving at **{v} m/s** sees a hazard. After a reaction time of **{fmt(tr)} s** she brakes, stopping **{fmt(tb)} s** after the brakes are applied (Fig. 1). What is the deceleration while braking?",
              "deceleration = Δv ÷ braking time (the reaction time has constant speed)", [f"braking: {v} m/s → 0 in {fmt(tb)} s", f"a = {v} ÷ {fmt(tb)} = **{fmt(a)} m/s²**"],
              ["What happens to the speed during the reaction time?", "Only the braking section slows the car.", f"{v} ÷ {fmt(tb)}."],
              figure=vt([(0, v), (tr, v), (tr + tb, 0)]))


@template("c2b_decel_then_distance", chapter=2, level=5, lo="2c")
def decel_then_distance(rng):
    u = nice(rng, 16, 20, 24, 30)
    a = nice(rng, 2, 4, 5)
    t = u / a
    d = u * t / 2
    return mk(rng, t, [(d, "That is the stopping distance, not the time."), (u * a, "t = Δv ÷ a."), (t * 2, "From u to 0 at a constant deceleration takes u ÷ a.")],
              "s", f"A train moving at **{u} m/s** decelerates uniformly at **{a} m/s²** until it stops.\n\n{md_table(['quantity', 'value'], [['initial speed', f'{u} m/s'], ['deceleration', f'{a} m/s²']])}\n\nHow long does it take to stop?",
              "t = (u − v) ÷ deceleration", [f"t = ({u} − 0) ÷ {a} = **{fmt(t)} s**  (stopping distance ½×{fmt(t)}×{u} = {fmt(d)} m)"],
              ["The speed falls by a fixed amount every second.", f"How many seconds to lose {u} m/s at {a} m/s per second?", f"{u} ÷ {a}."])


@template("c2b_dt_curve_instant", chapter=2, level=5, lo="2f")
def dt_curve_instant(rng):
    k = nice(rng, 0.5, 1.0, 2.0)
    T = nice(rng, 6, 8)
    pts = [(t, k * t * t) for t in range(0, T + 1)]
    t0 = nice(rng, 2, 3, 4)
    v = 2 * k * t0          # tangent gradient
    return mk(rng, v, [(k * t0 * t0 / t0, "That is the AVERAGE speed from 0 to that time (chord), not the speed at that instant (tangent)."), (k * t0 * t0, "That is the distance at that time, not the speed."), (2 * k * T, "Use the tangent at the time asked.")],
              "m/s", f"Fig. 1 is the distance-time graph of a ball rolling down a slope (d = {fmt(k)}t²). A tangent drawn to the curve at **t = {t0} s** has a gradient equal to the speed at that instant. What is the speed at t = {t0} s?",
              "instantaneous speed = gradient of the TANGENT to the d-t curve (for d = k t², gradient = 2 k t)", [f"gradient of tangent at t = {t0} s = 2 × {fmt(k)} × {t0}", f"= **{fmt(v)} m/s**"],
              ["A curved d-t graph means the speed is changing.", "The speed at one instant is the gradient of the tangent there.", f"For d = {fmt(k)}t², the tangent gradient is 2 × {fmt(k)} × t."],
              figure=vt(pts, ylabel="distance / m", labels=[(t0, k * t0 * t0, "P", -14, 10)]))


@template("c2b_dt_rest_interval", chapter=2, level=5, lo="2b")
def dt_rest_interval(rng):
    v1 = nice(rng, 3, 4, 5)
    t1, t2, t3 = nice(rng, 4, 5), nice(rng, 8, 9, 10), nice(rng, 14, 15)
    d1 = v1 * t1
    v3 = nice(rng, 2, 3)
    d3 = d1 + v3 * (t3 - t2)
    av = d3 / t3
    return mk(rng, av, [(d3 / (t3 - (t2 - t1)), "The time at rest still counts in the total time."), ((v1 + v3) / 2, "Average speed = total distance ÷ total time."), (d3 / t1, "Use the total time.")],
              "m/s", "Fig. 1 is the distance-time graph of a dog's run, including a stop. What is the dog's average speed for the whole run?",
              "average speed = final distance ÷ total time (flat section = at rest, still part of the time)", [f"total distance = {d3} m; total time = {t3} s", f"average = **{fmt(av)} m/s**"],
              ["What does the flat section of a d-t graph show?", "Average speed uses the TOTAL time.", "Final distance ÷ final time."],
              figure=vt([(0, 0), (t1, d1), (t2, d1), (t3, d3)], ylabel="distance / m"))


@template("c2b_area_trapezium_find_v", chapter=2, level=5, lo="2h")
def area_trapezium_find_v(rng):
    u = nice(rng, 4, 6, 8)
    T = nice(rng, 5, 8, 10)
    v = nice(rng, 12, 14, 16, 20)
    d = (u + v) / 2 * T
    return mk(rng, v, [(d / T, "That is the AVERAGE velocity; the final velocity is larger."), (2 * d / T, "The trapezium area is ½(u + v)T, so v = 2d/T − u."), (d / T - u, "Rearrange carefully: v = 2d ÷ T − u.")],
              "m/s", f"A car accelerates uniformly from **{u} m/s** and travels **{fmt(d)} m** in **{T} s**, as shown in Fig. 1. What is its final velocity?",
              "distance = area of trapezium = ½(u + v) T → v = 2d ÷ T − u", [f"{fmt(d)} = ½({u} + v) × {T}", f"v = 2 × {fmt(d)} ÷ {T} − {u} = **{v} m/s**"],
              ["The distance is the area under the line: a trapezium.", "Area = ½ (u + v) × T.", "Rearrange for v."],
              figure=figs.graph([(0, u), (T, v)], T + 2, v + 6, 2, 4, labels=[(T, v, "v = ?", 10, 8)]))


@template("c2b_vt_negative_velocity", chapter=2, level=5, lo="2e")
def vt_negative_velocity(rng):
    u = nice(rng, 10, 15, 20)
    t_up = u / G
    up = u * t_up / 2
    return mk(rng, up, [(u * t_up, "Use the triangle area (½ × base × height)."), (u, "That is the launch speed, not the height."), (up * 2, "That is up AND back down; the question asks for the maximum height.")],
              "m", f"A ball is thrown vertically upwards at **{u} m/s** (g = 10 m/s², no air resistance). Fig. 1 is its velocity-time graph from launch until it reaches its highest point. What is the maximum height it reaches?",
              "max height = area under the v-t graph until v = 0", [f"time to top = {u} ÷ 10 = {fmt(t_up)} s", f"height = ½ × {fmt(t_up)} × {u} = **{fmt(up)} m**"],
              ["When is the ball at its highest point on the graph?", "Where the velocity is zero.", "Area of the triangle."],
              figure=figs.graph([(0, u), (t_up, 0)], t_up + 0.5, u + 5, 0.5, 5, ylabel="velocity / m/s", xlabel="time / s"))


@template("c2b_two_stage_area", chapter=2, level=5, lo="2e")
def two_stage_area(rng):
    v = nice(rng, 8, 10, 12)
    t1, t2 = nice(rng, 4, 5), nice(rng, 12, 15)
    target = v * t1 / 2 + v * (t2 - t1)
    return mk(rng, t2, [(target / v, "The first section is a triangle, not a rectangle; it covers only half the distance a constant speed would."), (t2 - t1, "That is the time at constant speed only."), (target / v + t1, "The triangle covers v × t1 ÷ 2, not v × t1.")],
              "s", f"A cyclist accelerates uniformly from rest to **{v} m/s** in **{t1} s**, then rides at constant speed, as in Fig. 1. At what time has she travelled **{fmt(target)} m**?",
              "area so far = triangle (½ v t₁) + rectangle (v (t − t₁)); solve for t", [f"triangle = ½ × {t1} × {v} = {fmt(v * t1 / 2)} m", f"rectangle needed = {fmt(target - v * t1 / 2)} m → {fmt((target - v * t1 / 2) / v)} s more", f"t = **{t2} s**"],
              ["Split the area into the triangle and the rectangle.", "How much distance does the triangle give?", "The rest comes from the constant-speed part."],
              figure=vt([(0, 0), (t1, v), (t2 + 3, v)]))
