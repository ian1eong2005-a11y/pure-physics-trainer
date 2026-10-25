"""Chapter 12 Light (6091) bank extension: calculation and data-reading templates, 10 per level, each LO at least twice.
Contexts adapted from the question bank (SEAB 2016-2025: ray through a glass block, semicircular block and critical angle,
optical fibre, periscope prisms, converging lens as a magnifying glass and projector; school papers 2024-2025)."""
import math

from .. import figs2
from .base import fmt, md_table, mk, mkt, nice, template

C = 3.0e8
LENS = [(4, 6, 12), (5, 10, 10), (6, 9, 18), (4, 12, 6), (3, 6, 6), (6, 10, 15), (4, 8, 8), (5, 15, 7.5), (6, 12, 12), (3, 4, 12)]


def r_for(i, n):
    return math.degrees(math.asin(math.sin(math.radians(i)) / n))


def n_for(i, r):
    return math.sin(math.radians(i)) / math.sin(math.radians(r))


# ================================================================== L1
@template("c12x_reflection_angle", chapter=12, level=1, lo="12b")
def reflection_angle(rng):
    i = nice(rng, 25, 30, 35, 40, 50, 55)
    return mk(rng, i, [(90 - i, "That is the angle between the ray and the MIRROR; angles are measured from the normal."), (2 * i, "That is the angle between the two rays."), (180 - i, "The angle of reflection equals the angle of incidence.")],
              "°", f"A ray strikes a plane mirror at an angle of incidence of **{i}°** (Fig. 1). What is the angle of reflection?",
              "law of reflection: angle of reflection = angle of incidence (both from the normal)", [f"r = i = **{i}°**"],
              ["State the law of reflection.", "Both angles are measured from the normal.", "They are equal."], figure=figs2.mirror_reflection(i, f"{i}°", "r = ?"), dp=0)


@template("c12x_angle_from_mirror", chapter=12, level=1, lo="12a")
def angle_from_mirror(rng):
    g = nice(rng, 20, 25, 30, 40, 50)
    return mk(rng, 90 - g, [(g, "That is the angle with the MIRROR; the angle of incidence is measured from the normal."), (2 * g, "Subtract from 90°."), (180 - g, "The normal is at 90° to the mirror.")],
              "°", f"A ray of light makes an angle of **{g}°** with the surface of a plane mirror.\n\n{md_table(['quantity', 'value'], [['angle between ray and mirror surface', f'{g}°']])}\n\nWhat is the angle of incidence?",
              "angle of incidence = 90° − angle with the surface", [f"i = 90° − {g}° = **{90 - g}°**"],
              ["The normal is perpendicular to the mirror.", "Angles of incidence are measured from the normal.", "Subtract from 90°."], dp=0)


@template("c12x_normal_angle_glass", chapter=12, level=1, lo="12a")
def normal_angle_glass(rng):
    g = nice(rng, 30, 40, 50, 60)
    return mk(rng, 90 - g, [(g, "Measure from the NORMAL, not the surface."), (180 - g, "The normal makes 90° with the surface."), (g / 2, "Subtract from 90°.")],
              "°", f"A ray of light strikes a glass block at **{g}°** to its surface.\n\n{md_table(['quantity', 'value'], [['angle between ray and glass surface', f'{g}°']])}\n\nWhat is the angle of incidence?",
              "i = 90° − angle with the surface", [f"i = 90° − {g}° = **{90 - g}°**"],
              ["Draw the normal at the point of incidence.", "It is at 90° to the surface.", "i is measured from the normal."], dp=0)


@template("c12x_n_from_speeds", chapter=12, level=1, lo="12e")
def n_from_speeds(rng):
    v = nice(rng, 2.0e8, 2.25e8, 1.5e8, 1.25e8)
    return mk(rng, C / v, [(v / C, "n = c ÷ v: the speed in vacuum goes on top."), (C - v, "Divide the speeds."), (C / v * 2, "n = c ÷ v.")],
              "", f"{md_table(['quantity', 'value'], [['speed of light in vacuum', '3.0 × 10⁸ m/s'], ['speed of light in the material', f'{fmt(v)} m/s']])}\n\nWhat is the refractive index of the material?",
              "n = c ÷ v", [f"n = 3.0 × 10⁸ ÷ {fmt(v)} = **{fmt(C / v)}**"],
              ["Refractive index compares speeds.", "n = c ÷ v.", "No unit."])


@template("c12x_speed_from_n", chapter=12, level=1, lo="12e")
def speed_from_n(rng):
    n = nice(rng, 1.33, 1.5, 1.6, 2.4)
    return mk(rng, C / n, [(C * n, "Light is SLOWER in the material: v = c ÷ n."), (n, "That is the refractive index."), (C - n, "Divide c by n.")],
              "m/s", f"{md_table(['material', 'refractive index'], [['the material', n]])}\n\nWhat is the speed of light in the material? (c = 3.0 × 10⁸ m/s)",
              "v = c ÷ n", [f"v = 3.0 × 10⁸ ÷ {n} = **{fmt(C / n)} m/s**"],
              ["n = c ÷ v.", "Rearrange for v.", "Light slows down."])


@template("c12x_n_simple", chapter=12, level=1, lo="12d")
def n_simple(rng):
    i, r = rng.choice([(30, 19.5), (45, 28.1), (60, 35.3), (40, 25.4), (50, 30.7)])
    n = n_for(i, r)
    return mk(rng, n, [(i / r, "Use the SINES of the angles, not the angles."), (n_for(r, i), "n = sin i ÷ sin r (i in air)."), (math.sin(math.radians(i)), "Divide by sin r too.")],
              "", f"A ray passes from air into a glass block (Fig. 1).\n\n{md_table(['angle', 'value'], [['angle of incidence', f'{i}°'], ['angle of refraction', f'{r}°']])}\n\nWhat is the refractive index of the glass?",
              "n = sin i ÷ sin r", [f"n = sin {i}° ÷ sin {r}° = **{fmt(n)}**"],
              ["Snell's law.", "n = sin i ÷ sin r.", "Use sines."], figure=figs2.refraction(i, r, label_i=f"{i}°", label_r=f"{r}°"))


@template("c12x_n_from_sines_table", chapter=12, level=1, lo="12d")
def n_from_sines_table(rng):
    si = nice(rng, 0.50, 0.60, 0.70, 0.80)
    n = nice(rng, 1.4, 1.5, 1.6)
    sr = si / n
    return mk(rng, n, [(sr / si, "n = sin i ÷ sin r."), (si - sr, "Divide, do not subtract."), (si * sr, "Divide sin i by sin r.")],
              "", f"A student measures a ray entering a plastic block.\n\n{md_table(['quantity', 'value'], [['sin i', fmt(si)], ['sin r', fmt(sr, sf=3)]])}\n\nWhat is the refractive index of the plastic?",
              "n = sin i ÷ sin r", [f"n = {fmt(si)} ÷ {fmt(sr, sf=3)} = **{fmt(n)}**"],
              ["Use Snell's law.", "The sines are given.", "Divide."])


@template("c12x_focal_length_ruler", chapter=12, level=1, lo="12i")
def focal_length_ruler(rng):
    lens_x = nice(rng, 20, 30, 40)
    f = nice(rng, 8, 10, 12, 15)
    screen = lens_x + f
    return mk(rng, f, [(screen, "Measure from the LENS to the sharp image, not from the zero of the rule."), (lens_x, "That is the lens position."), (2 * f, "The image of a distant object forms at the focal point.")],
              "cm", f"A converging lens forms a sharp image of a distant window on a screen. Positions on a metre rule:\n\n{md_table(['object', 'position on rule / cm'], [['lens', lens_x], ['screen (sharp image)', screen]])}\n\nWhat is the focal length of the lens?",
              "distant object → image at F; f = lens-to-screen distance", [f"f = {screen} − {lens_x} = **{f} cm**"],
              ["Where does the image of a distant object form?", "At the principal focus.", "Distance from lens to screen."], dp=0)


@template("c12x_angle_between_rays_mirror", chapter=12, level=1, lo="12b")
def angle_between_rays_mirror(rng):
    i = nice(rng, 20, 25, 35, 40)
    return mk(rng, 2 * i, [(i, "That is just the angle of incidence."), (180 - 2 * i, "The angle between the rays is i + r."), (90 - i, "Add i and r.")],
              "°", f"A ray strikes a plane mirror at an angle of incidence of **{i}°** (Fig. 1). What is the angle between the incident ray and the reflected ray?",
              "angle between rays = i + r = 2i", [f"r = i = {i}°", f"angle = {i}° + {i}° = **{2 * i}°**"],
              ["r = i.", "The two rays are on either side of the normal.", "Add them."], figure=figs2.mirror_reflection(i, f"{i}°"), dp=0)


# ================================================================== L2
@template("c12x_mirror_rotate", chapter=12, level=2, lo="12b")
def mirror_rotate(rng):
    g = nice(rng, 30, 40, 50, 60)
    i = 90 - g
    return mk(rng, 2 * i, [(i, "Find the angle between the incident and reflected RAYS (i + r)."), (2 * g, "Use the angle from the normal, not from the mirror."), (g, "Convert to the angle of incidence first.")],
              "°", f"A ray of light hits a plane mirror, making **{g}°** with the mirror's surface.\n\n{md_table(['quantity', 'value'], [['angle between ray and mirror', f'{g}°']])}\n\nWhat is the angle between the incident and reflected rays?",
              "i = 90° − g; angle between rays = 2i", [f"i = 90° − {g}° = {i}°", f"angle = 2 × {i}° = **{2 * i}°**"],
              ["Find i from the normal.", "r = i.", "Add i and r."], dp=0)


@template("c12x_mirror_image_distance", chapter=12, level=2, lo="12b")
def mirror_image_distance(rng):
    d = nice(rng, 1.5, 2.0, 2.5, 3.0)
    return mk(rng, 2 * d, [(d, "That is the distance from the person to the MIRROR; the image is as far behind it."), (d / 2, "The image is behind the mirror."), (3 * d, "Image distance behind = object distance in front.")],
              "m", f"A girl stands in front of a plane mirror.\n\n{md_table(['quantity', 'value'], [['distance from girl to mirror', f'{fmt(d)} m']])}\n\nHow far is she from her image? (The image in a plane mirror is as far behind the mirror as the object is in front, as the law of reflection shows.)",
              "image distance behind mirror = object distance; separation = 2d", [f"separation = {fmt(d)} + {fmt(d)} = **{fmt(2 * d)} m**"],
              ["Where is the image?", "As far behind as she is in front.", "Add the two distances."])


@template("c12x_angle_refraction_from_n", chapter=12, level=2, lo="12d")
def angle_refraction_from_n(rng):
    i = nice(rng, 30, 40, 45, 50, 60)
    n = nice(rng, 1.33, 1.5, 1.6)
    r = r_for(i, n)
    return mk(rng, r, [(i / n, "Divide the SINE of i by n, then take sin⁻¹."), (i, "Light bends towards the normal in glass."), (r_for(i, 1 / n) if math.sin(math.radians(i)) * n < 1 else i * n, "sin r = sin i ÷ n.")],
              "°", f"A ray of light passes from air into a material.\n\n{md_table(['quantity', 'value'], [['angle of incidence', f'{i}°'], ['refractive index', n]])}\n\nWhat is the angle of refraction?",
              "sin r = sin i ÷ n", [f"sin r = sin {i}° ÷ {n} = {fmt(math.sin(math.radians(i)) / n, sf=3)}", f"r = **{fmt(r, sf=3)}°**"],
              ["Rearrange n = sin i ÷ sin r.", "sin r = sin i ÷ n.", "Then use sin⁻¹."], sf=3)


@template("c12x_n_from_ratio_v", chapter=12, level=2, lo="12e")
def n_from_ratio_v(rng):
    n1 = nice(rng, 1.5, 1.6)
    v = C / n1
    return mk(rng, v / C * 100, [(C / v * 100, "Find v ÷ c, the fraction of the vacuum speed."), (100 - v / C * 100, "That is the percentage DECREASE."), (n1, "That is n; express v as a percentage of c.")],
              "%", f"{md_table(['material', 'refractive index'], [['glass', n1]])}\n\nThe speed of light in the glass is what percentage of its speed in a vacuum?",
              "v ÷ c = 1 ÷ n", [f"v ÷ c = 1 ÷ {n1} = {fmt(1 / n1, sf=3)}", f"= **{fmt(100 / n1, sf=3)}%**"],
              ["n = c ÷ v.", "So v ÷ c = 1 ÷ n.", "× 100%."], sf=3)


@template("c12x_critical_angle_simple", chapter=12, level=2, lo="12f")
def critical_angle_simple(rng):
    n = nice(rng, 1.33, 1.5, 1.6, 2.42)
    c_ang = math.degrees(math.asin(1 / n))
    return mk(rng, c_ang, [(1 / n * 90, "sin c = 1 ÷ n, then take sin⁻¹."), (math.degrees(math.asin(1 / n)) * 2, "Use sin c = 1 ÷ n."), (90 - c_ang, "c is measured from the normal.")],
              "°", f"{md_table(['material', 'refractive index'], [['the material', n]])}\n\nWhat is the critical angle for light passing from this material into air?",
              "sin c = 1 ÷ n", [f"sin c = 1 ÷ {n} = {fmt(1 / n, sf=3)}", f"c = **{fmt(c_ang, sf=3)}°**"],
              ["Use sin c = 1 ÷ n.", "Calculate 1 ÷ n.", "Then sin⁻¹."], sf=3)


@template("c12x_tir_occurs_table", chapter=12, level=2, lo="12f")
def tir_occurs_table(rng):
    c_ang = nice(rng, 42, 41, 49)
    angles = [nice(rng, 30, 35), c_ang - 5, c_ang + 3, c_ang + 15]
    names = ["P", "Q", "R", "S"]
    pairs = list(zip(names, angles))
    rng.shuffle(pairs)
    ans_list = sorted(n for n, a in pairs if a > c_ang)
    ans = " and ".join(ans_list)
    wrongs = {"P and Q": "", "Q only": "", "all four": "Only rays meeting the surface at more than c are totally internally reflected.", "none": "Angles greater than c give TIR."}
    wrongs = {k: (v or "Compare each angle with the critical angle.") for k, v in wrongs.items() if k != ans}
    table = md_table(["ray inside glass", "angle of incidence at the glass–air surface / °"], [[n, a] for n, a in pairs])
    return mkt(rng, ans, dict(list(wrongs.items())[:3]), f"The critical angle of a glass is **{c_ang}°**.\n\n{table}\n\nWhich rays are totally internally reflected?",
               "TIR when the angle of incidence (in the denser medium) > c", [f"angles above {c_ang}°: **{ans}**"],
               ["What is the condition for TIR?", "i > c (and from denser to less dense).", "Check each ray."])


@template("c12x_focal_from_beam", chapter=12, level=2, lo="12i")
def focal_from_beam(rng):
    f = nice(rng, 4, 5, 6, 8)
    return mk(rng, f, [(2 * f, "Parallel rays meet at F, one focal length from the lens."), (f / 2, "Count to the point where the rays meet."), (f + 1, "Count squares from the centre of the lens.")],
              "cm", f"Fig. 1 shows a parallel beam of light passing through a converging lens (1 square = 1 cm). What is the focal length of the lens?",
              "focal length = distance from the lens to the principal focus F", [f"the rays meet {f} squares from the lens → **{f} cm**"],
              ["Where do parallel rays meet?", "At the principal focus.", "Count from the lens."], figure=figs2.lens_beam(f, "f = ?"), dp=0)


@template("c12x_power_from_f", chapter=12, level=2, lo="12i")
def power_from_f(rng):
    f_cm = nice(rng, 10, 20, 25, 50)
    return mk(rng, 2 * f_cm, [(f_cm, "That is F; 2F is twice as far."), (f_cm / 2, "2F means two focal lengths."), (3 * f_cm, "2F is at 2f.")],
              "cm", f"A converging lens has a focal length of **{f_cm} cm**.\n\n{md_table(['point', 'distance from lens'], [['F', f'{f_cm} cm'], ['2F', '?']])}\n\nHow far from the lens is the point 2F? (An object at 2F forms an image the same size, also at 2F.)",
              "2F is at twice the focal length", [f"2F = 2 × {f_cm} = **{2 * f_cm} cm**"],
              ["F is one focal length away.", "2F is two focal lengths.", "Double."], dp=0)


# ================================================================== L3
@template("c12x_n_semicircular", chapter=12, level=3, lo="12d")
def n_semicircular(rng):
    i, n = rng.choice([(20, 1.5), (25, 1.5), (30, 1.45), (20, 1.6)])
    r = math.degrees(math.asin(n * math.sin(math.radians(i))))
    return mk(rng, n, [(n_for(i, r), "The ray goes from glass INTO air: n = sin(angle in air) ÷ sin(angle in glass)."), (r / i, "Use sines."), (math.sin(math.radians(r)), "Divide by sin of the angle in glass.")],
              "", f"A ray travels inside a semicircular glass block and leaves into air at the flat face.\n\n{md_table(['angle', 'value'], [['angle in glass (from normal)', f'{i}°'], ['angle in air (from normal)', f'{fmt(r, sf=3)}°']])}\n\nWhat is the refractive index of the glass?",
              "n = sin(angle in air) ÷ sin(angle in glass)", [f"n = sin {fmt(r, sf=3)}° ÷ sin {i}° = **{fmt(n)}**"],
              ["The larger angle is in air.", "n = sin(air) ÷ sin(glass).", "Calculate."])


@template("c12x_angle_in_water", chapter=12, level=3, lo="12d")
def angle_in_water(rng):
    i = nice(rng, 30, 40, 50, 60)
    r = r_for(i, 1.33)
    dev = i - r
    return mk(rng, dev, [(r, "That is the angle of refraction; the deviation is i − r."), (i, "Find how much the ray turns: i − r."), (i + r, "Subtract.")],
              "°", f"A ray enters water (n = 1.33) from air at an angle of incidence of **{i}°** (Fig. 1). Through what angle is the ray deviated (turned) at the surface?",
              "sin r = sin i ÷ n; deviation = i − r", [f"r = sin⁻¹(sin {i}° ÷ 1.33) = {fmt(r, sf=3)}°", f"deviation = {i}° − {fmt(r, sf=3)}° = **{fmt(dev, sf=3)}°**"],
              ["Find r first.", "The ray bends towards the normal.", "Deviation = i − r."], figure=figs2.refraction(i, round(r), upper="air", lower="water", label_i=f"{i}°", label_r="r"), sf=3)


@template("c12x_time_through_block", chapter=12, level=3, lo="12e")
def time_through_block(rng):
    n = nice(rng, 1.5, 1.6)
    L_cm = nice(rng, 6, 9, 12, 15)
    t = L_cm / 100 / (C / n) * 1e9
    return mk(rng, t, [(L_cm / 100 / C * 1e9, "Light is slower in glass: v = c ÷ n."), (t / 1e9, "Convert to ns (× 10⁹)."), (L_cm / (C / n) * 1e9, "Convert cm to m.")],
              "ns", f"Light crosses a glass block straight through (along the normal).\n\n{md_table(['quantity', 'value'], [['thickness', f'{L_cm} cm'], ['refractive index', n], ['c', '3.0 × 10⁸ m/s']])}\n\nHow long does it take, in nanoseconds?",
              "v = c ÷ n; t = d ÷ v", [f"v = 3.0 × 10⁸ ÷ {n} = {fmt(C / n)} m/s", f"t = {fmt(L_cm / 100)} ÷ {fmt(C / n)} = **{fmt(t)} ns**"],
              ["Find the speed in glass.", "t = d ÷ v.", "1 ns = 10⁻⁹ s."])


@template("c12x_v_two_materials", chapter=12, level=3, lo="12e")
def v_two_materials(rng):
    n1, n2 = nice(rng, 1.33), nice(rng, 1.5, 1.6, 2.42)
    ratio = n2 / n1
    return mk(rng, ratio, [(n1 / n2, "Light is FASTER in the lower-index material: v₁ ÷ v₂ = n₂ ÷ n₁."), (n2 - n1, "Find a ratio."), (n2, "Divide the indices.")],
              "times", f"{md_table(['material', 'refractive index'], [['water', n1], ['the other material', n2]])}\n\nHow many times faster does light travel in water than in the other material?",
              "v = c ÷ n → v_water ÷ v_other = n_other ÷ n_water", [f"= {n2} ÷ {n1} = **{fmt(ratio, sf=3)}**"],
              ["v = c ÷ n for each.", "Divide the speeds.", "The c cancels."], sf=3)


@template("c12x_ray_diagram_virtual", chapter=12, level=3, lo="12j")
def ray_diagram_virtual(rng):
    f, u = rng.choice([(6, 3), (6, 4), (8, 4), (10, 5)])
    v = 1 / (1 / f - 1 / u)
    return mk(rng, abs(v), [(u, "That is the object distance; the virtual image is further from the lens."), (f, "That is the focal length."), (abs(v) / 2, "Trace the dashed rays back to where they meet.")],
              "cm", f"Fig. 1 is a scale ray diagram for a magnifying glass of focal length **{f} cm** with an object **{u} cm** from the lens (1 square = 1 cm). How far from the lens is the virtual image?",
              "rays diverge after the lens; trace them back to find the virtual image", [f"the dashed lines meet {fmt(abs(v))} squares from the lens → **{fmt(abs(v))} cm** (same side as the object)"],
              ["The object is inside F.", "The rays spread out after the lens.", "Trace them back."], figure=figs2.lens_rays(f, u))


@template("c12x_ray_diagram_height", chapter=12, level=3, lo="12j")
def ray_diagram_height(rng):
    f, u, v = rng.choice([t for t in LENS if t[1] > t[0] and t[2] <= 18])
    h = 1.0
    H = h * v / u
    return mk(rng, H, [(h, "The image is not the same size unless u = 2f."), (h * u / v, "Image height ÷ object height = v ÷ u."), (H * 2, "Measure the image height on the diagram.")],
              "cm", f"Fig. 1 is a scale ray diagram (1 square = 1 cm) for a converging lens of focal length **{f} cm**. The object is **1.0 cm** tall and **{u} cm** from the lens. How tall is the image?",
              "read the image height where the rays cross (or use v ÷ u)", [f"image at v = {fmt(v)} cm; height = 1.0 × {fmt(v)} ÷ {u} = **{fmt(H)} cm** (inverted)"],
              ["Find where the rays cross.", "Measure the height of the image.", "It is inverted."], figure=figs2.lens_rays(f, u, h=1.0))


@template("c12x_mirror_turn_ray", chapter=12, level=3, lo="12b")
def mirror_turn_ray(rng):
    D = nice(rng, 60, 80, 90, 100, 120)
    i = (180 - D) / 2
    return mk(rng, i, [(D / 2, "The ray turns through 180° − 2i, so i = (180° − D) ÷ 2."), (180 - D, "Halve it: i and r are equal."), (90 - D, "Use deviation = 180° − 2i.")],
              "°", f"A plane mirror is used to turn a ray of light so that its direction changes by **{D}°**.\n\n{md_table(['quantity', 'value'], [['change in direction of the ray', f'{D}°']])}\n\nWhat must the angle of incidence be? (Deviation = 180° − 2i.)",
              "deviation = 180° − 2i → i = (180° − D) ÷ 2", [f"i = (180° − {D}°) ÷ 2 = **{fmt(i)}°**"],
              ["Use the law of reflection: r = i.", "The ray turns through 180° − (i + r).", "Solve for i."])


@template("c12x_mirror_two_rotate", chapter=12, level=3, lo="12b")
def mirror_two_rotate(rng):
    th = nice(rng, 5, 10, 15, 20)
    return mk(rng, 2 * th, [(th, "When a mirror turns through θ, the reflected ray turns through 2θ."), (4 * th, "Double once."), (90 - th, "The reflected ray turns through twice the mirror's rotation.")],
              "°", f"A ray hits a plane mirror. The mirror is then rotated through **{th}°** while the incident ray stays fixed.\n\n{md_table(['quantity', 'value'], [['rotation of mirror', f'{th}°']])}\n\nThrough what angle does the reflected ray turn? (Use the law of reflection: i and r each change by θ.)",
              "i increases by θ and r by θ → reflected ray turns by 2θ", [f"turn = 2 × {th}° = **{2 * th}°**"],
              ["The normal turns with the mirror.", "i changes by θ; so does r.", "The reflected ray turns 2θ."], dp=0)


@template("c12x_critical_from_n_water", chapter=12, level=3, lo="12f")
def critical_from_n_water(rng):
    n = nice(rng, 1.33, 1.36, 1.47)
    c_ang = math.degrees(math.asin(1 / n))
    i = nice(rng, 40, 45, 50, 55)
    ans = "it is totally internally reflected" if i > c_ang else "it is refracted out into the air"
    wrongs = {("it is refracted out into the air" if ans.startswith("it is totally") else "it is totally internally reflected"): f"Compare {i}° with the critical angle {fmt(c_ang, sf=3)}°.",
              "it passes straight through without bending": "At an angle to the normal, the ray bends or reflects.",
              "it is absorbed completely": "Clear liquid does not absorb it."}
    return mkt(rng, ans, wrongs, f"A ray inside a liquid meets the liquid–air surface (Fig. 1).\n\n{md_table(['quantity', 'value'], [['refractive index of liquid', n], ['angle of incidence at surface', f'{i}°']])}\n\nWhat happens to the ray?",
               "sin c = 1 ÷ n; TIR if i > c", [f"c = sin⁻¹(1 ÷ {n}) = {fmt(c_ang, sf=3)}°", f"i = {i}° → **{ans}**"],
               ["Find the critical angle.", "Compare i with c.", "i > c → TIR."], figure=figs2.tir(i, round(c_ang), medium="liquid"))


# ================================================================== L4
@template("c12x_n_from_graph", chapter=12, level=4, lo="12d")
def n_from_graph(rng):
    n = nice(rng, 1.4, 1.5, 1.6)
    pts = [(0, 0), (0.5, 0.5 * n)]
    return mk(rng, n, [(1 / n, "Gradient = sin i ÷ sin r = n when sin i is on the y-axis."), (0.5 * n, "That is a single sin i value."), (n * 2, "Gradient = rise ÷ run.")],
              "", f"A student plots sin i (y-axis) against sin r (x-axis) for light entering a block. Fig. 1 shows the straight line through the origin. What is the refractive index?",
              "n = gradient = Δ(sin i) ÷ Δ(sin r)", [f"gradient = {fmt(0.5 * n)} ÷ 0.50 = **{fmt(n)}**"],
              ["What does the gradient represent?", "sin i ÷ sin r.", "Read two points."], figure=figs2.graph(pts, 0.8, 1.0, 0.1, 0.2, xlabel="sin r", ylabel="sin i"))


@template("c12x_angle_into_glass_from_water", chapter=12, level=4, lo="12d")
def angle_into_glass_from_water(rng):
    i = nice(rng, 40, 45, 50)
    n_w, n_g = 1.33, 1.5
    s_air = n_w * math.sin(math.radians(i))
    r = math.degrees(math.asin(s_air / n_g))
    return mk(rng, r, [(math.degrees(math.asin(math.sin(math.radians(i)) / n_g)), "The ray starts in WATER, not air: n_w sin i = n_g sin r."), (i, "The ray bends towards the normal in the denser glass."), (math.degrees(math.asin(math.sin(math.radians(i)) / n_w)), "Use both indices.")],
              "°", f"A ray passes from water into glass.\n\n{md_table(['quantity', 'value'], [['angle of incidence in water', f'{i}°'], ['n (water)', n_w], ['n (glass)', n_g]])}\n\nWhat is the angle of refraction in the glass? (n₁ sin θ₁ = n₂ sin θ₂)",
              "n₁ sin θ₁ = n₂ sin θ₂", [f"1.33 × sin {i}° = 1.5 × sin r", f"r = **{fmt(r, sf=3)}°**"],
              ["Use the general form of Snell's law.", "Water to glass.", "Solve for r."], sf=3)


@template("c12x_min_n_for_prism", chapter=12, level=4, lo="12f")
def min_n_for_prism(rng):
    i = 45
    n_min = 1 / math.sin(math.radians(i))
    return mk(rng, n_min, [(math.sin(math.radians(i)), "n_min = 1 ÷ sin 45°."), (1.5, "Calculate the minimum, not a typical value."), (2.0, "n = 1 ÷ sin c with c = 45°.")],
              "", f"A 45° prism in binoculars must totally internally reflect light that meets its face at 45°.\n\n{md_table(['quantity', 'value'], [['angle of incidence at the face', '45°']])}\n\nWhat is the minimum refractive index of the glass?",
              "TIR needs c ≤ 45° → n ≥ 1 ÷ sin 45°", [f"n = 1 ÷ sin 45° = **{fmt(n_min, sf=3)}**"],
              ["For TIR, i must be at least c.", "So c ≤ 45°.", "n = 1 ÷ sin c."], sf=3)


@template("c12x_critical_compare", chapter=12, level=4, lo="12f")
def critical_compare(rng):
    rows = [("water", 1.33), ("glass", 1.50), ("diamond", 2.42), ("perspex", 1.49)]
    rng.shuffle(rows)
    ans = max(rows, key=lambda r: r[1])[0]
    wrongs = {n: "A LARGER refractive index gives a SMALLER critical angle." for n, v in rows if n != ans}
    table = md_table(["material", "refractive index"], [[n, v] for n, v in rows])
    return mkt(rng, ans, wrongs, f"{table}\n\nWhich material has the smallest critical angle?",
               "sin c = 1 ÷ n → larger n, smaller c", [f"largest n → **{ans}** (c = {fmt(math.degrees(math.asin(1 / max(v for _, v in rows))), sf=3)}°)"],
               ["sin c = 1 ÷ n.", "Larger n → smaller sin c.", "Pick the largest n."])


@template("c12x_image_size_projector", chapter=12, level=4, lo="12k")
def image_size_projector(rng):
    f, u, v = rng.choice([(4, 6, 12), (6, 9, 18), (6, 10, 15), (3, 4, 12)])
    h = nice(rng, 1.0, 2.0)
    return mk(rng, h * v / u, [(h, "The image is magnified when the object is between F and 2F."), (h * u / v, "magnification = v ÷ u, not u ÷ v."), (h * v / u * 2, "Use v ÷ u once.")],
              "cm", f"A projector lens forms a sharp image on a screen.\n\n{md_table(['quantity', 'value'], [['object (slide) height', f'{fmt(h)} cm'], ['object distance', f'{u} cm'], ['image distance', f'{v} cm']])}\n\nHow tall is the image? (image height ÷ object height = v ÷ u)",
              "magnification = v ÷ u", [f"m = {v} ÷ {u} = {fmt(v / u)}", f"image height = {fmt(h)} × {fmt(v / u)} = **{fmt(h * v / u)} cm**"],
              ["Find the magnification.", "m = v ÷ u.", "Multiply by the object height."])


@template("c12x_image_type_table", chapter=12, level=4, lo="12k")
def image_type_table(rng):
    f = nice(rng, 10, 15, 20)
    case = rng.choice(["beyond 2F", "between F and 2F", "inside F"])
    u = {"beyond 2F": 3 * f, "between F and 2F": 1.5 * f, "inside F": 0.5 * f}[case]
    ans = {"beyond 2F": "real, inverted, diminished", "between F and 2F": "real, inverted, magnified", "inside F": "virtual, upright, magnified"}[case]
    allo = ["real, inverted, diminished", "real, inverted, magnified", "virtual, upright, magnified", "virtual, inverted, diminished"]
    wrongs = {o: ("That is for an object " + {"real, inverted, diminished": "beyond 2F", "real, inverted, magnified": "between F and 2F", "virtual, upright, magnified": "inside F"}.get(o, "nowhere: a converging lens never gives this") + ".") for o in allo if o != ans}
    return mkt(rng, ans, wrongs, f"{md_table(['quantity', 'value'], [['focal length of converging lens', f'{f} cm'], ['object distance', f'{fmt(u)} cm']])}\n\nWhich describes the image?",
               "u > 2f: diminished; f < u < 2f: magnified, real; u < f: virtual, upright", [f"u = {fmt(u)} cm is {case} → **{ans}**"],
               ["Compare u with f and 2f.", "Where is the object?", "Recall the image for that position."])


@template("c12x_speed_ratio_angles", chapter=12, level=4, lo="12e")
def speed_ratio_angles(rng):
    i, r = rng.choice([(40, 25), (50, 30), (60, 35)])
    n = n_for(i, r)
    v = C / n
    return mk(rng, v, [(C * n, "Light is slower in the block: v = c ÷ n."), (C / (i / r), "Use sines to find n."), (C, "Find n first.")],
              "m/s", f"A ray passes from air into a block.\n\n{md_table(['angle', 'value'], [['angle of incidence', f'{i}°'], ['angle of refraction', f'{r}°'], ['c', '3.0 × 10⁸ m/s']])}\n\nWhat is the speed of light in the block?",
              "n = sin i ÷ sin r; v = c ÷ n", [f"n = sin {i}° ÷ sin {r}° = {fmt(n)}", f"v = 3.0 × 10⁸ ÷ {fmt(n)} = **{fmt(v)} m/s**"],
              ["Find n from the angles.", "Then v = c ÷ n.", "Calculate."])


@template("c12x_apparent_depth", chapter=12, level=4, lo="12e")
def apparent_depth(rng):
    real = nice(rng, 1.2, 1.6, 2.0, 2.4)
    n = 1.33
    app = real / n
    return mk(rng, app, [(real * n, "The pool looks SHALLOWER: apparent depth = real ÷ n."), (real, "Refraction makes it look shallower."), (real - n, "Divide by n.")],
              "m", f"Looking straight down into a pool, its apparent depth is its real depth divided by the refractive index of water.\n\n{md_table(['quantity', 'value'], [['real depth', f'{fmt(real)} m'], ['refractive index of water', n]])}\n\nWhat is the apparent depth?",
              "apparent depth = real depth ÷ n", [f"= {fmt(real)} ÷ 1.33 = **{fmt(app)} m**"],
              ["Does the pool look deeper or shallower?", "Shallower.", "Divide by n."])


@template("c12x_ray_diagram_object_distance", chapter=12, level=4, lo="12j")
def ray_diagram_object_distance(rng):
    f, u, v = rng.choice([t for t in LENS if t[1] > t[0] and t[2] <= 18])
    return mk(rng, v - f, [(v, "That is the image distance; subtract the focal length."), (u - f, "Use the image side."), (v + f, "Subtract.")],
              "cm", f"Fig. 1 is a scale ray diagram (1 square = 1 cm) for a converging lens of focal length **{f} cm**. How far beyond the principal focus F (on the image side) does the image form?",
              "distance beyond F = v − f", [f"v = {fmt(v)} cm, f = {f} cm → **{fmt(v - f)} cm** beyond F"],
              ["Find the image distance.", "Subtract the focal length.", "Measure on the diagram."], figure=figs2.lens_rays(f, u))


# ================================================================== L5
@template("c12x_fibre_path_length", chapter=12, level=5, lo="12g")
def fibre_path_length(rng):
    L = nice(rng, 1.0, 2.0, 5.0)
    angle = nice(rng, 60, 70, 75)
    path = L / math.sin(math.radians(angle))
    n = 1.5
    t = path / (C / n) * 1e9
    return mk(rng, t, [(L / (C / n) * 1e9, "The zig-zag path is LONGER than the fibre."), (path / C * 1e9, "Light is slower in glass: v = c ÷ n."), (t / 2, "Use the full path length.")],
              "ns", f"A ray zig-zags along an optical fibre by total internal reflection, meeting the walls at **{angle}°** to the normal.\n\n{md_table(['quantity', 'value'], [['length of fibre', f'{fmt(L)} m'], ['refractive index of core', n], ['path length ÷ fibre length', f'1 ÷ sin {angle}°']])}\n\nHow long does the ray take to travel the length of the fibre, in ns?",
              "path = L ÷ sin θ; v = c ÷ n; t = path ÷ v", [f"path = {fmt(L)} ÷ sin {angle}° = {fmt(path)} m", f"v = {fmt(C / n)} m/s; t = **{fmt(t)} ns**"],
              ["Find the actual path length.", "Find the speed in glass.", "t = path ÷ v."])


@template("c12x_fibre_tir_check", chapter=12, level=5, lo="12f")
def fibre_tir_check(rng):
    n_core = nice(rng, 1.50, 1.52)
    n_clad = nice(rng, 1.46, 1.48)
    c_ang = math.degrees(math.asin(n_clad / n_core))
    return mk(rng, c_ang, [(math.degrees(math.asin(1 / n_core)), "The core meets CLADDING, not air: sin c = n_clad ÷ n_core."), (math.degrees(math.asin(n_core / n_clad)) if n_core < n_clad else 90 - c_ang, "Use sin c = n_clad ÷ n_core."), (c_ang / 2, "Take sin⁻¹ of the ratio.")],
              "°", f"An optical fibre has a glass core surrounded by cladding of lower refractive index.\n\n{md_table(['part', 'refractive index'], [['core', n_core], ['cladding', n_clad]])}\n\nWhat is the critical angle at the core–cladding boundary? (sin c = n_cladding ÷ n_core)",
              "sin c = n₂ ÷ n₁", [f"sin c = {n_clad} ÷ {n_core} = {fmt(n_clad / n_core, sf=3)}", f"c = **{fmt(c_ang, sf=3)}°**"],
              ["Which two materials meet?", "Core and cladding.", "sin c = n_clad ÷ n_core."], sf=3)


@template("c12x_angle_from_two_media", chapter=12, level=5, lo="12d")
def angle_from_two_media(rng):
    i = nice(rng, 30, 40)
    n = nice(rng, 1.5, 1.6)
    r = r_for(i, n)
    exit_angle = i
    return mk(rng, exit_angle, [(r, "That is the angle INSIDE the block; the ray leaves parallel to its original direction."), (90 - i, "Measure from the normal."), (2 * r, "For parallel faces, the emerging angle equals the original angle.")],
              "°", f"A ray enters a rectangular glass block with parallel faces at **{i}°** and leaves through the opposite face.\n\n{md_table(['quantity', 'value'], [['angle of incidence', f'{i}°'], ['refractive index', n]])}\n\nAt what angle to the normal does the ray leave the block?",
              "parallel faces: angle out = angle in (ray emerges parallel)", [f"inside: r = {fmt(r, sf=3)}°; at the second face sin(out) = n sin r = sin {i}°", f"angle out = **{i}°**"],
              ["Find the angle inside.", "At the second face, Snell's law works in reverse.", "The ray emerges parallel to the incident ray."], dp=0)


@template("c12x_n_from_critical", chapter=12, level=5, lo="12d")
def n_from_critical(rng):
    c_ang = nice(rng, 38, 40, 42, 45, 49)
    n = 1 / math.sin(math.radians(c_ang))
    return mk(rng, n, [(math.sin(math.radians(c_ang)), "n = 1 ÷ sin c."), (90 / c_ang, "Use the sine of c."), (1 / math.cos(math.radians(c_ang)), "Use sin, not cos.")],
              "", f"A student finds that light inside a block just grazes the surface when it meets it at **{c_ang}°**.\n\n{md_table(['quantity', 'value'], [['critical angle', f'{c_ang}°']])}\n\nWhat is the refractive index of the block?",
              "n = 1 ÷ sin c", [f"n = 1 ÷ sin {c_ang}° = **{fmt(n, sf=3)}**"],
              ["At the critical angle, r = 90°.", "n = 1 ÷ sin c.", "Calculate."], sf=3)


@template("c12x_tir_angle_needed", chapter=12, level=5, lo="12f")
def tir_angle_needed(rng):
    n = nice(rng, 1.5, 1.6, 1.8)
    c_ang = math.degrees(math.asin(1 / n))
    entry = nice(rng, 0, 10, 20)
    return mk(rng, 90 - c_ang, [(c_ang, "That is the critical angle at the side wall; the question asks for the angle with the AXIS."), (90 + c_ang, "Angle with axis = 90° − c."), (2 * c_ang, "Subtract c from 90°.")],
              "°", f"Light inside a straight glass rod hits the side wall. It is totally internally reflected if its angle of incidence at the wall is greater than the critical angle.\n\n{md_table(['quantity', 'value'], [['refractive index of rod', n]])}\n\nWhat is the largest angle the ray can make with the AXIS of the rod and still be totally internally reflected?",
              "c = sin⁻¹(1 ÷ n); angle with axis = 90° − angle with normal", [f"c = sin⁻¹(1 ÷ {n}) = {fmt(c_ang, sf=3)}°", f"largest angle with axis = 90° − {fmt(c_ang, sf=3)}° = **{fmt(90 - c_ang, sf=3)}°**"],
              ["Find c.", "The normal to the wall is perpendicular to the axis.", "Angle with axis = 90° − i."], sf=3)


@template("c12x_lens_find_f", chapter=12, level=5, lo="12j")
def lens_find_f(rng):
    f, u, v = rng.choice(LENS)
    return mk(rng, f, [(u * v / (u - v) if u != v else 2 * f, "Use 1/f = 1/u + 1/v (all positive for a real image)."), ((u + v) / 2, "That is not how f is found."), (u * v / (u + v) * 2, "1/f = 1/u + 1/v.")],
              "cm", f"On a scale ray diagram, an object **{u} cm** from a converging lens forms a real image **{fmt(v)} cm** from the lens. The lens formula is 1/f = 1/u + 1/v.\n\n{md_table(['quantity', 'value'], [['object distance u', f'{u} cm'], ['image distance v', f'{fmt(v)} cm']])}\n\nWhat is the focal length?",
              "1/f = 1/u + 1/v", [f"1/f = 1/{u} + 1/{fmt(v)}", f"f = **{fmt(f)} cm**"],
              ["Use the lens formula.", "Add the reciprocals.", "Invert."])


@template("c12x_magnifier_image", chapter=12, level=5, lo="12j")
def magnifier_image(rng):
    f, u = rng.choice([(6, 3), (8, 4), (10, 5), (6, 4)])
    v = abs(1 / (1 / f - 1 / u))
    m = v / u
    return mk(rng, m, [(1 / m, "A magnifier makes the image BIGGER: m = v ÷ u > 1."), (f / u, "Read v from the diagram first."), (m * 2, "m = v ÷ u.")],
              "times", f"Fig. 1 is a scale ray diagram (1 square = 1 cm) for a magnifying glass of focal length **{f} cm** with an object **{u} cm** away. What is the magnification?",
              "magnification = image distance ÷ object distance", [f"virtual image at {fmt(v)} cm; m = {fmt(v)} ÷ {u} = **{fmt(m)}**"],
              ["Find the image distance from the diagram.", "m = v ÷ u.", "It is upright and larger."], figure=figs2.lens_rays(f, u))


@template("c12x_camera_focus", chapter=12, level=5, lo="12k")
def camera_focus(rng):
    f = nice(rng, 5.0)
    u1, u2 = nice(rng, 200, 100), nice(rng, 25, 30)
    v1 = 1 / (1 / f - 1 / u1)
    v2 = 1 / (1 / f - 1 / u2)
    return mk(rng, (v2 - v1) * 10, [((v2 - v1), "That is in cm; the answer is in mm."), (v2 * 10, "Find the CHANGE in image distance."), ((v1 - v2) * 10 * -1 if v1 > v2 else (v1 + v2) * 10, "Subtract the image distances.")],
              "mm", f"A camera lens of focal length **{fmt(f)} cm** is moved to focus on a near object after a distant one. Use 1/f = 1/u + 1/v.\n\n{md_table(['', 'distant object', 'near object'], [['object distance u / cm', u1, u2], ['image distance v / cm', fmt(v1, sf=3), fmt(v2, sf=3)]])}\n\nHow far must the lens move away from the sensor, in mm?",
              "Δv = v₂ − v₁", [f"v₁ = {fmt(v1, sf=3)} cm, v₂ = {fmt(v2, sf=3)} cm", f"move = {fmt(v2 - v1, sf=3)} cm = **{fmt((v2 - v1) * 10, sf=3)} mm**"],
              ["A nearer object gives a larger v.", "Subtract the image distances.", "Convert to mm."], sf=3)


@template("c12x_projector_screen_distance", chapter=12, level=5, lo="12k")
def projector_screen_distance(rng):
    f = nice(rng, 5, 8, 10)
    m = nice(rng, 20, 25, 40)
    u = f * (m + 1) / m
    v = m * u
    return mk(rng, v / 100, [(u / 100, "That is the slide distance; the screen is m times further."), (v, "That is in cm; the answer is in m."), (f * m / 100, "Use v = m u with u from the lens formula.")],
              "m", f"A projector must make an image **{m} times** larger than the slide. Its lens has focal length **{f} cm**; this requires the slide to be **{fmt(u, sf=3)} cm** from the lens.\n\n{md_table(['quantity', 'value'], [['magnification', m], ['object distance u', f'{fmt(u, sf=3)} cm']])}\n\nHow far from the lens must the screen be, in m?",
              "v = m × u", [f"v = {m} × {fmt(u, sf=3)} = {fmt(v, sf=3)} cm", f"= **{fmt(v / 100, sf=3)} m**"],
              ["Magnification = v ÷ u.", "So v = m u.", "Convert cm to m."], sf=3)


@template("c12x_fibre_data_time", chapter=12, level=5, lo="12g")
def fibre_data_time(rng):
    L_km = nice(rng, 100, 500, 1000)
    n = 1.5
    t_fibre = L_km * 1000 / (C / n) * 1000
    t_air = L_km * 1000 / C * 1000
    return mk(rng, t_fibre - t_air, [(t_fibre, "Find the DIFFERENCE between fibre and air (radio) times."), (t_air, "That is the radio-link time."), ((t_fibre - t_air) * 1000, "The answer is in ms.")],
              "ms", f"A signal is sent {L_km} km either by optical fibre or by a direct radio link.\n\n{md_table(['quantity', 'value'], [['distance', f'{L_km} km'], ['refractive index of fibre core', n], ['c', '3.0 × 10⁸ m/s']])}\n\nHow much longer does the fibre signal take, ignoring the zig-zag path?",
              "t = d ÷ v; v_fibre = c ÷ n", [f"fibre: {fmt(t_fibre)} ms; radio: {fmt(t_air)} ms", f"difference = **{fmt(t_fibre - t_air)} ms**"],
              ["Speed in fibre = c ÷ n.", "Find both times.", "Subtract."])
