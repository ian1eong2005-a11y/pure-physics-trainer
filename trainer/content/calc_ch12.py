"""Chapter 12 Light (6091): reflection angles, refractive index, speed in a medium, critical angle, lens ray diagrams and magnification."""
import math

from .. import figs2
from .base import fmt, nice, numeric_options, template

C = 3.0e8
LENS_TRIPLES = [(4, 6, 12), (5, 10, 10), (6, 9, 18), (4, 12, 6), (3, 6, 6), (6, 10, 15), (4, 8, 8), (5, 15, 7.5)]   # (f, u, v)


def _r_for(i, n):
    return round(math.degrees(math.asin(math.sin(math.radians(i)) / n)), 1)


# ---------------------------------------------------------------- L1
@template("c12_angle_between_rays", chapter=12, level=1, lo="12b")
def angle_between_rays(rng):
    i = nice(rng, 20, 25, 30, 35, 40, 45, 50, 55, 60)
    opts, key, mis = numeric_options(rng, 2 * i, [
        (i, "That is the angle of reflection alone. The question asks for the angle between the incident and reflected rays, which is i + r."),
        (90 - i, "That is the angle between the ray and the mirror surface. Angles of incidence and reflection are measured from the NORMAL."),
        (180 - 2 * i, "That is the angle on the other side. The angle between the two rays is i + r = 2i."),
    ], unit="°")
    return dict(
        stem=f"Fig. 1 shows a ray of light striking a plane mirror with an angle of incidence of **{i}°**. What is the angle between the incident ray and the reflected ray?",
        figure=figs2.mirror_reflection(i),
        options=opts, key=key, misconceptions=mis,
        formula="angle of reflection = angle of incidence (both measured from the normal); angle between the rays = i + r",
        working=[f"angle of reflection r = angle of incidence = {i}°", f"angle between the rays = i + r = {i}° + {i}°", f"= **{2 * i}°**"],
        hints=[
            "State the law of reflection. Which line are both angles measured from?",
            f"r = i = {i}°. The two rays lie on opposite sides of the normal.",
            f"Add the two angles: {i}° + {i}°.",
        ],
    )


@template("c12_focal_length_from_beam", chapter=12, level=1, lo="12i")
def focal_length_from_beam(rng):
    f = nice(rng, 4, 5, 6, 8, 10, 12, 15)
    opts, key, mis = numeric_options(rng, f, [
        (2 * f, "That is twice the focal length (the position of 2F). The focal point F is where the parallel rays meet."),
        (f / 2, "Read the distance from the centre of the lens to the point where the rays cross, F."),
        (f + 2, "Read the marked distance carefully: it runs from the lens to F."),
    ], unit="cm")
    return dict(
        stem=f"Fig. 1 shows a beam of rays parallel to the principal axis passing through a thin converging lens. The rays meet at F, **{f} cm** from the centre of the lens. What is the focal length of the lens?",
        figure=figs2.lens_beam(f, label=f"{f} cm"),
        options=opts, key=key, misconceptions=mis,
        formula="focal length = distance from the optical centre of the lens to the principal focus F",
        working=["rays parallel to the principal axis are refracted through the principal focus F", f"the distance from the lens to F is the focal length = **{f} cm**"],
        hints=[
            "What is the name of the point where rays parallel to the axis meet after the lens?",
            "The focal length is measured from the centre of the lens to that point.",
            "Read the distance marked on the diagram.",
        ],
    )


# ---------------------------------------------------------------- L2
@template("c12_refractive_index_from_angles", chapter=12, level=2, lo="12d")
def refractive_index_from_angles(rng):
    i = nice(rng, 30, 40, 45, 50, 60)
    n_true = nice(rng, 1.33, 1.50, 1.60)
    r = _r_for(i, n_true)
    n = math.sin(math.radians(i)) / math.sin(math.radians(r))
    opts, key, mis = numeric_options(rng, n, [
        (math.sin(math.radians(r)) / math.sin(math.radians(i)), "You have the ratio upside down: n = sin i ÷ sin r, which is greater than 1 for light entering glass."),
        (i / r, "You divided the angles themselves. The refractive index uses the SINES of the angles."),
        (math.sin(math.radians(i - r)), "You took the sine of the difference. Use sin i ÷ sin r."),
    ], unit="", sf=3)
    return dict(
        stem=f"Fig. 1 shows a ray of light passing from air into a block of {'water' if n_true == 1.33 else 'glass'}. The angle of incidence is **{i}°** and the angle of refraction is **{fmt(r, dp=1)}°**. What is the refractive index of the {'water' if n_true == 1.33 else 'glass'}?",
        figure=figs2.refraction(i, r, lower="water" if n_true == 1.33 else "glass"),
        options=opts, key=key, misconceptions=mis,
        formula="n = sin i ÷ sin r (i in air, r in the medium)",
        working=["n = sin i ÷ sin r", f"= sin {i}° ÷ sin {fmt(r, dp=1)}° = {fmt(math.sin(math.radians(i)), sf=3)} ÷ {fmt(math.sin(math.radians(r)), sf=3)}", f"= **{fmt(n, sf=3)}**"],
        hints=[
            "Which relationship links the angles of incidence and refraction to the refractive index?",
            "n = sin i ÷ sin r. Both angles are measured from the normal; i is in the air.",
            f"sin {i}° ÷ sin {fmt(r, dp=1)}°.",
        ],
    )


@template("c12_speed_in_medium", chapter=12, level=2, lo="12e")
def speed_in_medium(rng):
    n, medium = rng.choice([(1.33, "water"), (1.50, "glass"), (2.42, "diamond"), (1.60, "flint glass")])
    v = C / n
    opts, key, mis = numeric_options(rng, v, [
        (C * n, "You multiplied. Light is SLOWER in the medium, so divide the speed in a vacuum by n."),
        (C, "That is the speed in a vacuum. In a medium of refractive index n the speed is c ÷ n."),
        (C / n / 10, "Check the power of ten: the answer should be a little less than 3.0 × 10⁸ m/s."),
    ], unit="m/s", sf=3)
    return dict(
        stem=f"The refractive index of {medium} is **{fmt(n)}**. The speed of light in a vacuum is 3.0 × 10⁸ m/s.\n\n| quantity | value |\n|---|---|\n| refractive index of {medium} | {fmt(n)} |\n| speed of light in vacuum | 3.0 × 10⁸ m/s |\n\nWhat is the speed of light in {medium}?",
        options=opts, key=key, misconceptions=mis,
        formula="n = speed of light in vacuum ÷ speed of light in the medium  →  v = c ÷ n",
        working=["v = c ÷ n", f"= 3.0 × 10⁸ ÷ {fmt(n)}", f"= **{fmt(v, sf=3)} m/s**"],
        hints=[
            "How is refractive index defined in terms of speeds?",
            "n = c ÷ v, so v = c ÷ n. The answer must be less than c.",
            f"3.0 × 10⁸ ÷ {fmt(n)} = ?",
        ],
    )


# ---------------------------------------------------------------- L3
@template("c12_angle_of_refraction", chapter=12, level=3, lo="12d")
def angle_of_refraction(rng):
    i = nice(rng, 30, 35, 40, 45, 50, 55, 60)
    n, medium = rng.choice([(1.33, "water"), (1.50, "glass"), (1.60, "flint glass")])
    r = math.degrees(math.asin(math.sin(math.radians(i)) / n))
    opts, key, mis = numeric_options(rng, r, [
        (i / n, "You divided the angle by n. It is the SINE of the angle that is divided: sin r = sin i ÷ n."),
        (math.degrees(math.asin(min(1, math.sin(math.radians(i)) * n))) if math.sin(math.radians(i)) * n < 1 else 90 - r, "You multiplied sin i by n. Light entering a denser medium bends TOWARDS the normal, so r must be smaller than i."),
        (90 - r, "That is the angle between the refracted ray and the boundary. Angles are measured from the normal."),
    ], unit="°", sf=3)
    return dict(
        stem=f"Fig. 1 shows a ray of light entering {medium} (refractive index **{fmt(n)}**) from air at an angle of incidence of **{i}°**. What is the angle of refraction r?",
        figure=figs2.refraction(i, round(r), lower=medium, label_r="r"),
        options=opts, key=key, misconceptions=mis,
        formula="n = sin i ÷ sin r  →  sin r = sin i ÷ n",
        working=[f"sin r = sin {i}° ÷ {fmt(n)} = {fmt(math.sin(math.radians(i)), sf=3)} ÷ {fmt(n)} = {fmt(math.sin(math.radians(i)) / n, sf=3)}", f"r = sin⁻¹({fmt(math.sin(math.radians(i)) / n, sf=3)})", f"= **{fmt(r, sf=3)}°**"],
        hints=[
            "Start from n = sin i ÷ sin r and rearrange for sin r.",
            f"sin r = sin {i}° ÷ {fmt(n)}. Work out the number first, then take the inverse sine.",
            f"r = sin⁻¹(sin {i}° ÷ {fmt(n)}). It must be smaller than {i}°.",
        ],
    )


@template("c12_critical_angle", chapter=12, level=3, lo="12f")
def critical_angle(rng):
    n, medium = rng.choice([(1.33, "water"), (1.50, "glass"), (1.60, "flint glass"), (2.42, "diamond"), (1.40, "perspex")])
    c = math.degrees(math.asin(1 / n))
    opts, key, mis = numeric_options(rng, c, [
        (math.degrees(math.atan(1 / n)), "You used tan instead of sin. sin c = 1 ÷ n."),
        (90 - c, "That is the angle between the ray and the boundary at the critical angle, not the critical angle itself (measured from the normal)."),
        (n * 30, "The critical angle comes from sin c = 1 ÷ n; it is not simply proportional to n."),
    ], unit="°", sf=3)
    return dict(
        stem=f"Fig. 1 shows light travelling inside {medium} (refractive index **{fmt(n)}**) towards a boundary with air. What is the critical angle for {medium}?",
        figure=figs2.tir(round(c), c_deg=c, medium=medium, label="c"),
        options=opts, key=key, misconceptions=mis,
        formula="sin c = 1 ÷ n",
        working=[f"sin c = 1 ÷ {fmt(n)} = {fmt(1 / n, sf=3)}", f"c = sin⁻¹({fmt(1 / n, sf=3)})", f"= **{fmt(c, sf=3)}°**"],
        hints=[
            "At the critical angle the refracted ray travels along the boundary (angle of refraction 90°). Put r = 90° into n = sin r ÷ sin i for light leaving the medium.",
            "That gives sin c = 1 ÷ n.",
            f"c = sin⁻¹(1 ÷ {fmt(n)}).",
        ],
    )


# ---------------------------------------------------------------- L4
@template("c12_minimum_index_for_tir", chapter=12, level=4, lo="12f")
def minimum_index_for_tir(rng):
    i = nice(rng, 40, 42, 45, 48, 50, 55)
    n = 1 / math.sin(math.radians(i))
    opts, key, mis = numeric_options(rng, n, [
        (math.sin(math.radians(i)), "That is sin i itself. For total internal reflection the critical angle must be no more than i, so n ≥ 1 ÷ sin i."),
        (1 / math.cos(math.radians(i)), "You used cos. The critical angle condition is sin c = 1 ÷ n."),
        (i / 30, "The refractive index is not proportional to the angle; use sin c = 1 ÷ n with c = i."),
    ], unit="", sf=3)
    return dict(
        stem=f"Fig. 1 shows light inside a transparent block meeting the boundary with air at an angle of incidence of **{i}°**. The light is just totally internally reflected, so {i}° is the critical angle. What is the refractive index of the block?",
        figure=figs2.tir(i, c_deg=i - 0.01, label=f"{i}°"),
        options=opts, key=key, misconceptions=mis,
        formula="total internal reflection occurs when i ≥ c and sin c = 1 ÷ n, so n = 1 ÷ sin c",
        working=[f"critical angle c = {i}°", f"n = 1 ÷ sin c = 1 ÷ sin {i}° = 1 ÷ {fmt(math.sin(math.radians(i)), sf=3)}", f"= **{fmt(n, sf=3)}**"],
        hints=[
            "Total internal reflection just begins when the angle of incidence equals the critical angle. What links c and n?",
            f"sin c = 1 ÷ n with c = {i}°. Rearrange for n.",
            f"n = 1 ÷ sin {i}°.",
        ],
    )


@template("c12_image_distance_ray_diagram", chapter=12, level=4, lo="12j")
def image_distance_ray_diagram(rng):
    f, u, v = rng.choice([t for t in LENS_TRIPLES if t[1] > t[0]])
    opts, key, mis = numeric_options(rng, v, [
        (u, "That is the object distance. The image is where the two rays cross on the other side of the lens."),
        (f, "That is the focal length. The image forms where the rays meet, not at F (unless the object is very far away)."),
        (u + v, "That is the distance from the object to the image. Image distance is measured from the lens."),
    ], unit="cm", sf=3)
    return dict(
        stem=f"Fig. 1 is a scale ray diagram for a thin converging lens of focal length **{f} cm** with an object **{u} cm** from the lens (1 square = 1 cm). How far from the lens is the image?",
        figure=figs2.lens_rays(f, u),
        options=opts, key=key, misconceptions=mis,
        formula="on the diagram, the image forms where the ray through the optical centre meets the ray refracted through F; count the squares from the lens",
        working=["ray 1: parallel to the axis, refracted through F; ray 2: through the optical centre, undeviated", "the rays cross at the tip of the image", f"image distance = **{fmt(v, sf=3)} cm** (count the squares from the lens)"],
        hints=[
            "Follow the two rays drawn from the top of the object. Where do they cross after the lens?",
            "The crossing point is the top of the image. Count squares from the lens to that point along the axis.",
            f"The object is {u} cm from a lens of focal length {f} cm; the image is {'further from' if v > u else 'nearer to' if v < u else 'the same distance from'} the lens than the object.",
        ],
    )


# ---------------------------------------------------------------- L5
@template("c12_image_height", chapter=12, level=5, lo="12k")
def image_height(rng):
    f, u, v = rng.choice([t for t in LENS_TRIPLES if t[1] > t[0]])
    h = nice(rng, 1.0, 1.5, 2.0, 3.0)
    m = v / u
    hi = h * m
    opts, key, mis = numeric_options(rng, hi, [
        (h, "The image is the same height only when u = 2f. Use magnification = image distance ÷ object distance."),
        (h * u / v, "You have the magnification upside down: magnification = v ÷ u, not u ÷ v."),
        (h * v / f, "Magnification compares image distance with OBJECT distance, not with the focal length."),
    ], unit="cm", sf=3)
    return dict(
        stem=f"Fig. 1 shows a thin converging lens of focal length **{f} cm** forming an image of an object of height **{fmt(h)} cm** placed **{u} cm** from the lens. The image is **{fmt(v, sf=3)} cm** from the lens. What is the height of the image?",
        figure=figs2.lens_rays(f, u, h=min(h, 2.0)),
        options=opts, key=key, misconceptions=mis,
        formula="magnification = image distance ÷ object distance = image height ÷ object height",
        working=[f"magnification = v ÷ u = {fmt(v, sf=3)} ÷ {u} = {fmt(m, sf=3)}", f"image height = magnification × object height = {fmt(m, sf=3)} × {fmt(h)}", f"= **{fmt(hi, sf=3)} cm**"],
        hints=[
            "The ray through the optical centre is a straight line, so the object and image heights are in the same ratio as their distances from the lens.",
            f"magnification = v ÷ u = {fmt(v, sf=3)} ÷ {u}.",
            f"image height = (v ÷ u) × {fmt(h)} cm.",
        ],
    )


@template("c12_fibre_speed_time", chapter=12, level=5, lo="12g")
def fibre_speed_time(rng):
    L_km = nice(rng, 10, 20, 50, 100)
    n = nice(rng, 1.45, 1.50, 1.55)
    v = C / n
    t = L_km * 1000 / v
    opts, key, mis = numeric_options(rng, t, [
        (L_km * 1000 / C, "You used the speed of light in a vacuum. Inside the glass fibre light travels at c ÷ n."),
        (L_km / v, "You left the length in km. Convert to metres first."),
        (t * n, "You applied n twice. Find v = c ÷ n once, then t = distance ÷ v."),
    ], unit="s", sf=3)
    return dict(
        stem=f"Fig. 1 shows light travelling along an optical fibre by total internal reflection. The fibre is **{L_km} km** long and its glass has a refractive index of **{fmt(n)}**. Taking the speed of light in a vacuum as 3.0 × 10⁸ m/s, how long does a light pulse take to travel the length of the fibre? (Ignore the extra path from the zig-zag.)",
        figure=figs2.optical_fibre(),
        options=opts, key=key, misconceptions=mis,
        formula="speed in glass v = c ÷ n; time = distance ÷ speed",
        working=[f"v = c ÷ n = 3.0 × 10⁸ ÷ {fmt(n)} = {fmt(v, sf=3)} m/s", f"distance = {L_km} km = {L_km * 1000} m", f"t = {L_km * 1000} ÷ {fmt(v, sf=3)} = **{fmt(t, sf=3)} s**"],
        hints=[
            "Light in glass is slower than in a vacuum. First find its speed in the fibre.",
            f"v = 3.0 × 10⁸ ÷ {fmt(n)}. Then convert {L_km} km to metres.",
            f"t = {L_km * 1000} ÷ v.",
        ],
    )
