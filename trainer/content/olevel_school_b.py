"""O level 2026 MCQ practice, Ch 11-20: learning outcomes the SEAB specimen Paper 1 does not reach, adapted from schools' 2024-2026
6091 Paper 1 prelims (added 31 Oct 2026). Same context and skill as the source question; numbers changed; figures redrawn.
Where no 6091 paper on file tests an outcome, the item is adapted from a 2024 Science (Physics) 5086 prelim or an SEAB O-Level
Paper 1 (noted in the source)."""
import math

from .. import figs2, figs3
from .base import calc_q, explain_mcqs, fmt, md_table, nice, sci, template, text_options

CAT = "olevel"


def cite(text):
    return f"_Adapted from {text}._"


# ================================================================== Ch 11 Electromagnetic spectrum
explain_mcqs([
    dict(id="o26s_uv_vs_light", chapter=11, level=3, lo="11a", source="QTSS 2026 prelim MCQ 21",
         stem="The Sun emits ultraviolet radiation and visible light. Light from the Sun takes about 8 minutes to reach the Earth. Which row is correct for the ultraviolet radiation?",
         correct="reaches the Earth in about 8 minutes; wavelength shorter than light",
         wrongs={"reaches the Earth in less than 8 minutes; wavelength shorter than light": "All electromagnetic waves travel at the same speed in a vacuum, so ultraviolet takes the same time as light.",
                 "reaches the Earth in about 8 minutes; wavelength longer than light": "Ultraviolet lies BEYOND the violet end of the visible spectrum: higher frequency, shorter wavelength.",
                 "reaches the Earth in less than 8 minutes; wavelength longer than light": "Both parts are wrong: same speed as light, and a shorter wavelength."},
         hints=["All members of the electromagnetic spectrum travel at 3 × 10⁸ m/s in a vacuum.", "Same speed over the same distance means the same time.",
                "In the spectrum, ultraviolet is next to violet light on the short-wavelength side."]),
    dict(id="o26s_ir_xray_common", chapter=11, level=2, lo="11a", source="AMKSS 2025 prelim MCQ 23",
         stem="Infrared radiation and X-rays are both electromagnetic waves. Which statement about them is correct?",
         correct="They travel at the same speed in a vacuum.",
         wrongs={"They have the same frequency.": "They are different regions of the spectrum: X-rays have a far higher frequency than infrared.",
                 "They need a medium to travel through.": "Electromagnetic waves travel through a vacuum; that is how sunlight reaches the Earth.",
                 "They are longitudinal waves.": "All electromagnetic waves are transverse."},
         hints=["What do ALL electromagnetic waves have in common?", "They are transverse and need no medium.", "In a vacuum they all travel at 3 × 10⁸ m/s."]),
    dict(id="o26s_em_order_wavelength", chapter=11, level=2, lo="11b", source="XMSS 2024 prelim MCQ 24",
         stem="Which list of electromagnetic radiations is in order of **increasing** wavelength?",
         correct="gamma rays, ultraviolet, infrared, radio waves",
         wrongs={"radio waves, infrared, ultraviolet, gamma rays": "That is increasing FREQUENCY (decreasing wavelength).",
                 "infrared, radio waves, ultraviolet, gamma rays": "Radio waves have the longest wavelength of all, so they must come last.",
                 "ultraviolet, radio waves, gamma rays, infrared": "The order is jumbled: gamma rays have the shortest wavelength and radio the longest."},
         hints=["Gamma rays have the shortest wavelength and highest frequency.", "Radio waves have the longest wavelength.",
                "Remember the order: radio, micro, infrared, visible, ultraviolet, X, gamma, and reverse it for increasing wavelength."]),
    dict(id="o26s_em_left_to_right", chapter=11, level=2, lo="11b", source="BRD 2024 prelim MCQ 23",
         stem="The electromagnetic spectrum is written in the order: radio waves, microwaves, infrared, visible light, ultraviolet, X-rays, gamma rays. "
              "Which quantity increases from left to right along this list?",
         correct="frequency",
         wrongs={"wavelength": "Wavelength DECREASES from radio waves (kilometres) to gamma rays (smaller than an atom).",
                 "speed in a vacuum": "All electromagnetic waves travel at the same speed in a vacuum.",
                 "amplitude": "Amplitude depends on the intensity of a particular wave, not on its position in the spectrum."},
         hints=["Radio waves have wavelengths of metres to kilometres; gamma rays are tiny.", "v = f λ with v the same for all, so as λ falls, f rises.",
                "Which quantity goes UP as you move towards gamma rays?"]),
    dict(id="o26s_microwave_application", chapter=11, level=2, lo="11c", source="HGV 2024 prelim MCQ 26",
         stem="In the electromagnetic spectrum, region P lies between radio waves and infrared. What is a typical use of P?",
         correct="radar and satellite communication",
         wrongs={"treating cancer": "That uses gamma rays, at the opposite end of the spectrum.",
                 "intruder alarms": "Intruder alarms detect infrared radiation from a warm body.",
                 "sterilising medical equipment": "Sterilising uses ultraviolet or gamma rays, which can kill bacteria."},
         hints=["Between radio waves and infrared lie the microwaves.", "Microwaves pass easily through the atmosphere to satellites.",
                "They are also used in radar and mobile phone signals."]),
    dict(id="o26s_uv_hazard", chapter=11, level=2, lo="11d", source="GESS 2025 prelim MCQ 22",
         stem="Which is a hazard of over-exposure to ultraviolet radiation?",
         correct="sunburn and an increased risk of skin cancer, because the radiation damages living cells",
         wrongs={"internal heating of the body's tissues, as in a microwave oven": "Heating of tissue is the hazard of microwaves and infrared; ultraviolet damages cells by its ionising effect.",
                 "a loss of hearing, because the frequency is too high": "Hearing involves sound waves, not electromagnetic waves.",
                 "no hazard, because ultraviolet cannot pass through the skin": "Ultraviolet IS absorbed by the skin, and that absorption damages the cells there."},
         hints=["Ultraviolet has enough energy to damage (ionise) the molecules in living cells.", "It is absorbed mostly in the skin and the eyes.",
                "Think about why sunscreen is used."]),
], category=CAT)


# ================================================================== Ch 12 Light
explain_mcqs([
    dict(id="o26s_curved_mirror_normal", chapter=12, level=3, lo="12a", source="NAS 2025 prelim MCQ 23",
         stem="A ray strikes a curved mirror at a point where the tangent to the surface is the line PQ. The ray makes an angle of 70° with PQ. Which row is correct?",
         correct="PQ is not the normal; the angle of incidence is 20°",
         wrongs={"PQ is the normal; the angle of incidence is 70°": "The normal is the line at RIGHT ANGLES to the surface at that point; the tangent PQ lies along the surface.",
                 "PQ is not the normal; the angle of incidence is 70°": "Angles of incidence are measured from the normal, not from the surface: 90° − 70° = 20°.",
                 "PQ is the normal; the angle of incidence is 20°": "PQ is the tangent to the surface, not the normal."},
         hints=["The normal is perpendicular to the surface at the point of incidence.", "The tangent PQ lies along the surface, so the normal is at 90° to PQ.",
                "Angle of incidence = angle between the ray and the normal."]),
    dict(id="o26s_refractive_index_three", chapter=12, level=3, lo="12d", source="QTSS 2026 prelim MCQ 23",
         stem="A ray of light passes from air (speed v_a, wavelength λ_a, frequency f_a) into glass (speed v_g, wavelength λ_g, frequency f_g) with angle of incidence i and angle of refraction r. "
              "Three suggestions for the refractive index n of the glass are made:\n\n1  n = v_a / v_g\n\n2  n = f_a / f_g\n\n3  n = sin i / sin r\n\nWhich suggestions are correct?",
         correct="1 and 3 only",
         wrongs={"1, 2 and 3": "The frequency does NOT change on entering the glass, so f_a / f_g = 1, which is not the refractive index.",
                 "1 and 2 only": "Suggestion 2 is wrong (frequency is unchanged), and suggestion 3 is Snell's law, which is correct.",
                 "2 and 3 only": "Frequency is unchanged by refraction; the speed ratio (1) is a correct definition of n."},
         hints=["Which wave property stays the same when light enters glass?", "n is defined as the ratio of the speed of light in vacuum (or air) to that in the medium.",
                "Snell's law: sin i / sin r = n for light entering from air."]),
    dict(id="o26s_optical_fibre_use", chapter=12, level=2, lo="12g", source="QTSS 2026 prelim MCQ 19",
         stem="Pulses of infrared light carry telephone signals along a glass optical fibre. Which statement explains how the light stays inside the fibre, and gives an advantage of optical fibres?",
         correct="The light is totally internally reflected at the core's boundary because it meets it at more than the critical angle; the fibre carries far more information than a copper cable.",
         wrongs={"The light is refracted back into the core at each boundary; the fibre carries more information than a copper cable.": "Refraction would let light ESCAPE into the cladding. The light is kept in by total internal reflection.",
                 "The light is absorbed and re-emitted by the glass; the fibre is heavier and stronger than copper cable.": "Glass fibre guides light by reflection, and it is lighter and thinner than copper, not heavier.",
                 "The light is totally internally reflected; the signal travels more slowly than electricity in copper, so it is safer.": "Light in glass is still extremely fast; the advantages are capacity, low loss and freedom from electrical interference."},
         hints=["Inside the fibre the light meets the glass-air (or glass-cladding) boundary at a large angle of incidence.", "What happens at a boundary when the angle of incidence exceeds the critical angle?",
                "Optical fibres carry huge amounts of data with little loss and no electrical interference."]),
    dict(id="o26s_lens_focus_length", chapter=12, level=2, lo="12h", source="XMSS 2024 prelim MCQ 27",
         stem="Fig. 1 shows a beam of light parallel to the principal axis passing through a thin converging lens. Which statement is correct?",
         correct="The rays converge to the principal focus, and the focal length is the distance from the optical centre of the lens to that point.",
         wrongs={"The rays converge to the principal focus, and the focal length is the distance from the object to the lens.": "The focal length is a property of the lens alone: it is measured from the lens to the principal focus.",
                 "The rays spread out after the lens, and the focal length is the distance to where they appear to come from.": "That describes a DIVERGING lens; a converging lens brings parallel rays together.",
                 "The rays pass straight through without bending.": "Only the ray through the optical centre is undeviated; the others refract towards the axis."},
         hints=["A converging lens bends parallel rays towards the axis.", "The point where they meet is the principal focus F.",
                "Focal length = distance from the lens to F."],
         figure=lambda: figs2.lens_beam(3.0, label="f")),
    dict(id="o26s_object_for_real_enlarged", chapter=12, level=3, lo="12j", source="QTSS 2026 prelim MCQ 25",
         stem="An object is placed in front of a thin converging lens of focal length f. The lens forms a real, enlarged image. Where is the object?",
         correct="between f and 2f from the lens",
         wrongs={"closer to the lens than f": "Inside the focal length the image is VIRTUAL (upright and enlarged), as in a magnifying glass.",
                 "exactly at 2f": "At 2f the real image is the same size as the object.",
                 "further from the lens than 2f": "Beyond 2f the real image is smaller than the object (diminished)."},
         hints=["Draw the ray diagram for an object at each position.", "Inside f: virtual image. Beyond 2f: real, diminished. At 2f: real, same size.",
                "Which region gives a real image larger than the object?"]),
    dict(id="o26s_image_inside_f", chapter=12, level=3, lo="12k", source="NAS 2025 prelim MCQ 26",
         stem="An object is placed **4 cm** from a converging lens of focal length **8 cm**. What type of image is formed?",
         correct="virtual, upright and magnified",
         wrongs={"real, inverted and magnified": "A real image needs the object OUTSIDE the focal length; here the object is inside it.",
                 "real, upright and diminished": "A converging lens never forms a real upright image, and an object inside f gives a magnified image.",
                 "virtual, inverted and diminished": "Virtual images from a converging lens are upright and magnified (the magnifying glass)."},
         hints=["Compare the object distance with the focal length.", "An object inside the focal length acts like the object of a magnifying glass.",
                "The rays diverge after the lens, so the image is on the same side as the object."]),
], category=CAT)


@template("o26s_mirror_moved_distance", chapter=12, level=3, lo="12b", category=CAT)
def mirror_moved_distance(rng):
    d, extra = nice(rng, (4, 2), (3, 2), (5, 1), (2, 3))
    total = 2 * (d + extra)
    return calc_q(rng, f"A boy stands **{d} m** in front of a plane mirror. The mirror is then moved **{extra} m** further away from him. What is the distance between the boy and his image now?",
                  total,
                  [(d + extra, "That is the boy's distance from the MIRROR. The image is the same distance again behind the mirror."),
                   (2 * d + extra, "After the move the boy is (d + extra) from the mirror, and the image is that far behind it: double the NEW distance."),
                   (2 * d, "That is the distance before the mirror was moved.")],
                  "m", "image distance behind the mirror = object distance in front; separation = 2 × object distance",
                  [f"New distance to the mirror = {d} + {extra} = {d + extra} m", f"Image is {d + extra} m behind the mirror: separation = 2 × {d + extra} = **{total} m**",
                   cite("BGSS 2024 prelim MCQ 20")],
                  ["A plane mirror's image is as far behind the mirror as the object is in front.", "Work out the new distance from the boy to the mirror.", "Double it."])


@template("o26s_angle_of_refraction_out", chapter=12, level=4, lo="12c", category=CAT)
def angle_of_refraction_out(rng):
    v, i = nice(rng, (2.0e8, 30), (2.4e8, 40), (1.8e8, 25), (2.25e8, 35))
    n = 3e8 / v
    r = math.degrees(math.asin(n * math.sin(math.radians(i))))
    return calc_q(rng, f"A ray of light inside a transparent block meets the boundary with air at an angle of incidence of **{i}°**. The speed of light in the block is **{sci(v, 3)} m/s**. "
                  "What is the angle of refraction in the air?", r,
                  [(math.degrees(math.asin(math.sin(math.radians(i)) / n)), "That bends the ray TOWARDS the normal. Going from the block into air (less dense), the ray bends AWAY from the normal."),
                   (i, "The ray changes direction at the boundary; only a ray along the normal goes straight through."),
                   (90 - r, "That is the angle between the refracted ray and the surface, not the angle of refraction (measured from the normal).")],
                  "°", "n = c / v; sin(angle in air) = n sin(angle in block)",
                  [f"n = 3 × 10⁸ / {sci(v, 3)} = {fmt(n)}", f"sin r = {fmt(n)} × sin {i}° = {fmt(n * math.sin(math.radians(i)))}  ⇒  r = **{fmt(r)}°**",
                   cite("BPGHS 2024 prelim MCQ 23")],
                  ["First find the refractive index from the speeds: n = c / v.", "For a ray leaving the block: n sin(angle in block) = sin(angle in air).",
                   "The angle in air is larger: the ray bends away from the normal."], sf=2)


@template("o26s_critical_angle_speed", chapter=12, level=4, lo="12e", category=CAT)
def critical_angle_speed(rng):
    v = nice(rng, 1.24e8, 1.25e8, 1.20e8, 1.30e8)
    n = 3e8 / v
    c = math.degrees(math.asin(1 / n))
    return calc_q(rng, f"Light travels at **{sci(v, 3)} m/s** in a gemstone. What is the critical angle of the gemstone?", c,
                  [(math.degrees(math.asin(v / 3e8 if False else 1 / n)) + 20 if c + 20 < 90 else 60, "Check: sin c = 1/n with n = c_light / v. A larger n gives a SMALLER critical angle."),
                   (math.degrees(math.acos(1 / n)), "Use sin, not cos: sin c = 1 / n."),
                   (90 - c, "That is the complement of the critical angle.")],
                  "°", "n = c / v; sin C = 1 / n",
                  [f"n = 3.0 × 10⁸ / {sci(v, 3)} = {fmt(n)}", f"sin C = 1 / {fmt(n)} = {fmt(1 / n)}  ⇒  C = **{fmt(c)}°**", cite("QTSS 2026 prelim MCQ 24")],
                  ["Refractive index = speed of light in vacuum ÷ speed in the medium.", "sin (critical angle) = 1 / n.", "A high refractive index means a small critical angle."], sf=2)


@template("o26s_focal_length_plane_mirror", chapter=12, level=3, lo="12i", category=CAT)
def focal_length_plane_mirror(rng):
    f = nice(rng, 12.0, 15.0, 8.0, 20.0)
    return calc_q(rng, "A converging lens is placed in front of a plane mirror. An illuminated cross is moved along the axis until a sharp image of the cross is formed beside the cross itself. "
                  f"The cross is then **{fmt(f)} cm** from the lens. What is the focal length of the lens?", f,
                  [(f / 2, "The light goes through the lens twice, but that does not halve the distance: the object sits AT the focal point."),
                   (2 * f, "The object is at the focal point, not at 2f: parallel light returns from the mirror and refocuses at the same distance."),
                   (f * 1.5, "The method gives the focal length directly as the object-to-lens distance.")],
                  "cm", "object at F ⇒ parallel rays to the mirror ⇒ reflected back parallel ⇒ image at F",
                  [f"With the cross at the principal focus, rays leave the lens parallel, reflect back parallel and refocus at the focus, beside the cross.",
                   f"f = **{fmt(f)} cm**", cite("BGSS 2024 prelim MCQ 22")],
                  ["Rays from a point at the principal focus leave a converging lens parallel to the axis.", "A plane mirror sends parallel rays straight back.",
                   "Parallel rays returning through the lens focus at the principal focus."])


# ================================================================== Ch 13 Static electricity
explain_mcqs([
    dict(id="o26s_one_coulomb", chapter=13, level=1, lo="13a", source="FHSS 2024 prelim (5086) MCQ 16",
         stem="Electric charge is measured in coulombs. Which statement about charge is correct?",
         correct="There are two kinds of charge, positive and negative, and one coulomb is the charge that passes when a current of 1 A flows for 1 s.",
         wrongs={"There is only one kind of charge, and one coulomb is the charge on one electron.": "There are two kinds of charge, and an electron carries a tiny 1.6 × 10⁻¹⁹ C, not 1 C.",
                 "There are two kinds of charge, and one coulomb is the charge that passes when 1 V is applied for 1 s.": "The coulomb is defined from current and time (Q = I t), not from voltage.",
                 "Charge is measured in amperes.": "The ampere is the unit of current (charge per second); charge itself is in coulombs."},
         hints=["Like charges repel; unlike charges attract: so there are two kinds.", "Q = I t.", "1 C = 1 A × 1 s."]),
    dict(id="o26s_three_spheres_signs", chapter=13, level=4, lo="13b", source="XMSS 2024 prelim MCQ 28",
         stem="Three charged metal spheres A, B and C hang near one another. A repels B, B attracts C and A attracts C. At least two of the spheres are positively charged. "
              "Which sphere, if any, could be negatively charged?",
         correct="C",
         wrongs={"A": "A repels B, so A and B carry the SAME sign; with at least two positive, A and B are both positive.",
                 "B": "B is repelled by A, so B has the same sign as A: positive.",
                 "none of them": "C is attracted by both A and B (both positive), so C carries the opposite sign: negative."},
         hints=["Like charges repel, unlike charges attract.", "A and B repel, so they have the same sign; with two positives required, both are positive.",
                "C is attracted to positive spheres: what is its sign?"]),
    dict(id="o26s_electric_field_statements", chapter=13, level=3, lo="13c", source="HGV 2024 prelim MCQ 27",
         stem="Three statements are made about electric fields:\n\n1 An electron placed in an electric field experiences a force.\n\n2 Electric field lines never cross.\n\n"
              "3 Field lines point from a negatively charged object towards a positively charged object.\n\nWhich statements are correct?",
         correct="1 and 2 only",
         wrongs={"1, 2 and 3": "Field lines show the force on a POSITIVE charge, so they point from positive to negative, not the other way.",
                 "1 and 3 only": "Statement 3 has the direction reversed, and statement 2 is correct: crossing lines would mean two directions of force at one point.",
                 "2 and 3 only": "Statement 1 is correct: an electric field is a region where a charge (positive or negative) experiences a force."},
         hints=["An electric field is a region in which a charge experiences a force.", "The direction of a field line is the direction of the force on a positive charge.",
                "Two lines crossing would give two different force directions at one point: impossible."]),
    dict(id="o26s_negative_point_field", chapter=13, level=2, lo="13d", source="QTSS 2026 prelim MCQ 26",
         stem="Which description matches the electric field pattern of an isolated negative point charge?",
         correct="straight lines pointing radially inwards towards the charge, spaced evenly around it",
         wrongs={"straight lines pointing radially outwards from the charge": "Outward lines belong to a POSITIVE charge: a positive test charge would be pushed away from it.",
                 "closed loops circling the charge": "Closed loops are the pattern around a current-carrying wire (a magnetic field), not an electric charge.",
                 "parallel straight lines passing the charge": "Parallel lines show a UNIFORM field, as between two oppositely charged plates."},
         hints=["Field lines show the direction of the force on a small positive charge.", "A positive charge is attracted TOWARDS a negative charge.",
                "The pattern around a point charge is symmetrical in all directions."]),
    dict(id="o26s_lightning_energy_hazard", chapter=13, level=3, lo="13h", source="RGT 2024 prelim MCQ 29",
         stem="A thundercloud discharges **60 C** of charge to the ground through a lightning stroke across a potential difference of **2 × 10⁸ V**. Which statement explains why static electricity is a hazard here?",
         correct="About 1.2 × 10¹⁰ J of energy is released in a fraction of a second, enough to heat the air explosively and start fires.",
         wrongs={"About 60 J of energy is released, which can give a person an electric shock.": "Energy = Q V = 60 × 2 × 10⁸ J, enormously more than 60 J.",
                 "No energy is released, because the charges simply cancel out.": "Charges moving through a potential difference transfer energy: E = Q V.",
                 "The hazard is only that the cloud becomes neutral and cannot produce rain.": "The danger is the huge energy of the discharge, not the cloud losing charge."},
         hints=["Energy transferred = charge × potential difference.", "60 C × 2 × 10⁸ V is a very large number of joules.",
                "Released in a few milliseconds, that energy heats the air and anything in the path."]),
    dict(id="o26s_precipitator", chapter=13, level=3, lo="13i", source="QTSS 2026 prelim MCQ 27",
         stem="In an electrostatic precipitator, dusty air is blown past highly charged metal rods and then past earthed metal plates. How are the dust particles removed?",
         correct="The dust particles gain electrons from the negatively charged rods and are then attracted to the plates.",
         wrongs={"The dust particles gain protons and move away from the plates.": "Protons are fixed inside nuclei and are never transferred; only electrons move.",
                 "The dust particles lose electrons and move away from the plates.": "The particles become CHARGED and are ATTRACTED to the oppositely charged (or earthed) plates, where they stick.",
                 "The dust particles lose protons and are attracted to the plates.": "Charging is always by the transfer of electrons, never protons."},
         hints=["Only electrons are transferred when objects are charged.", "A charged particle near an earthed plate is attracted to it (induction).",
                "The dust collects on the plates, which are shaken clean."]),
], category=CAT)


@template("o26s_two_spheres_field", chapter=13, level=3, lo="13e", category=CAT)
def two_spheres_field(rng):
    signs = nice(rng, ("+", "-"), ("+", "+"), ("-", "-"), ("-", "+"))
    name = {"+": "positive", "-": "negative"}
    correct = f"P {name[signs[0]]}, Q {name[signs[1]]}"
    others = [("+", "-"), ("+", "+"), ("-", "-"), ("-", "+")]
    wrongs = {}
    for s in others:
        if s == signs:
            continue
        wrongs[f"P {name[s[0]]}, Q {name[s[1]]}"] = ("Lines leave a positive charge and arrive at a negative one. Like charges have lines that curve AWAY from the gap between them; "
                                                      "unlike charges are joined by lines running from one to the other.")
    opts, key, mis = text_options(rng, correct, wrongs)
    return dict(stem="Fig. 1 shows the electric field pattern around two charged spheres P (left) and Q (right). What are the charges on P and Q?",
                options=opts, key=key, misconceptions=mis, formula="field lines point away from positive and towards negative charge",
                working=[("Lines run from P to Q: unlike charges." if signs[0] != signs[1] else "Lines from the two spheres push apart and none joins them: like charges."),
                         f"Arrow direction gives the sign of each: P is {name[signs[0]]}, Q is {name[signs[1]]}.", f"Correct answer: **{correct}**",
                         cite("BGSS 2024 prelim MCQ 29 and BPGHS 2024 prelim MCQ 27")],
                hints=["Field lines start on positive charges and end on negative charges.", "Look at the arrows on the lines near each sphere.",
                       "If lines connect the two spheres they are unlike; if the lines push apart in the gap they are alike."],
                figure=figs3.two_charges_field(signs))


# ================================================================== Ch 14 Current of electricity
explain_mcqs([
    dict(id="o26s_ampere_units", chapter=14, level=1, lo="14a", source="QTSS 2026 prelim MCQ 30",
         stem="Current is the rate of flow of charge. Which two units are used to define the ampere?",
         correct="coulomb and second",
         wrongs={"coulomb and joule": "The joule is energy; current does not involve energy directly.",
                 "volt and ohm": "V/Ω does equal an ampere numerically, but the ampere is DEFINED as charge per unit time.",
                 "volt and joule": "Volts and joules define each other through charge; neither defines current."},
         hints=["I = Q / t.", "Q is in coulombs and t in seconds.", "1 A = 1 C per second."]),
    dict(id="o26s_conventional_current", chapter=14, level=1, lo="14b", source="Punggol 2024 prelim MCQ 24",
         stem="Which statement best describes conventional current?",
         correct="the direction in which positive charge would flow, from the positive terminal to the negative terminal, measured in amperes",
         wrongs={"the direction in which electrons flow, from negative to positive, measured in amperes": "Electron flow is the opposite way round to conventional current.",
                 "the flow of positive charge, measured in coulombs": "The coulomb measures the charge; current (the RATE of flow) is in amperes.",
                 "the flow of electrons, measured in coulombs": "Both parts are wrong: conventional current is taken as positive charge flowing, and it is measured in amperes."},
         hints=["Conventional current was defined before electrons were discovered.", "It points from + to − outside the cell.",
                "Electrons, being negative, actually move the other way."]),
    dict(id="o26s_emf_definition", chapter=14, level=1, lo="14d", source="SEAB O-Level (5076) 2021 MCQ 17",
         stem="The e.m.f. of a cell is 1.5 V. What does this mean?",
         correct="The cell does 1.5 J of work on each coulomb of charge that it drives round a complete circuit.",
         wrongs={"The cell drives a current of 1.5 A round the circuit.": "The current depends on the resistance of the circuit; e.m.f. is energy per unit charge, not current.",
                 "The cell stores 1.5 J of energy.": "1.5 V is the energy per COULOMB; the total energy stored depends on how much charge the cell can deliver.",
                 "The cell has a resistance of 1.5 Ω.": "E.m.f. is measured in volts (J/C), not ohms."},
         hints=["E.m.f. is measured in volts, and 1 V = 1 J/C.", "It is the work done per unit charge by the source.",
                "Think: how many joules for every coulomb?"]),
    dict(id="o26s_cells_series_emf", chapter=14, level=2, lo="14e", source="XMSS 2024 prelim MCQ 31",
         stem="Four circuits each contain identical lamps and identical 1.5 V cells. In one circuit, three cells are connected in series, all the same way round, with one lamp. "
              "What is the total e.m.f. driving the lamp in that circuit, and why is it the brightest of the four?",
         correct="4.5 V; the e.m.f.s of cells in series add, so this lamp has the largest p.d. across it",
         wrongs={"1.5 V; cells in series share the current, so the lamp is brightest": "In series the e.m.f.s ADD: three 1.5 V cells give 4.5 V.",
                 "4.5 V; cells in series halve the resistance of the lamp": "The lamp's resistance does not change; the larger e.m.f. drives a larger current through it.",
                 "0.5 V; the e.m.f. is shared between the three cells": "Sharing happens to the p.d. across components in series, not to the e.m.f. of sources: sources in series add."},
         hints=["For sources in series (same way round), total e.m.f. = sum of the e.m.f.s.", "3 × 1.5 V.",
                "A larger p.d. across the same lamp means a larger current and a brighter lamp."]),
    dict(id="o26s_graphs_xyz_components", chapter=14, level=3, lo="14k", source="NAS 2025 prelim MCQ 28",
         stem="Three I-V graphs are sketched: graph X is a straight line through the origin; graph Y curves so that the current rises more and more slowly as V increases; "
              "graph Z shows almost no current until a certain p.d. and then a steeply rising current. Which row identifies the components?",
         correct="X: metal wire at constant temperature; Y: filament lamp; Z: semiconductor diode",
         wrongs={"X: filament lamp; Y: metal wire at constant temperature; Z: semiconductor diode": "A metal wire at constant temperature obeys Ohm's law: a straight line through the origin, which is X.",
                 "X: metal wire at constant temperature; Y: semiconductor diode; Z: filament lamp": "A diode conducts only beyond a threshold p.d. (Z); the lamp's resistance rises as it heats, bending its graph (Y).",
                 "X: semiconductor diode; Y: filament lamp; Z: metal wire at constant temperature": "A diode's graph is far from a straight line through the origin."},
         hints=["Ohm's law (constant resistance) gives a straight line through the origin.", "A filament gets hotter as the current rises, so its resistance rises: the graph bends over.",
                "A diode passes almost no current until the p.d. reaches about 0.6 V, then the current rises sharply."]),
    dict(id="o26s_diode_resistance_change", chapter=14, level=4, lo="14k", source="QTSS 2026 prelim MCQ 31",
         stem="The I-V graph of a semiconductor diode shows almost zero current from X (0 V) to Y, then a current that rises steeply beyond Y. "
              "What is the resistance of the diode between X and Y, and how does it change as the p.d. increases beyond Y?",
         correct="very large between X and Y; decreases beyond Y",
         wrongs={"very large between X and Y; increases beyond Y": "Beyond Y the current rises faster than the p.d., so V/I (the resistance) FALLS.",
                 "zero between X and Y; decreases beyond Y": "Almost no current at a non-zero p.d. means a very LARGE resistance, not zero.",
                 "zero between X and Y; increases beyond Y": "Both parts are wrong: no current means a huge resistance, and the steep rise afterwards means a falling resistance."},
         hints=["R = V / I. What is R when I is almost zero but V is not?", "Beyond Y a small extra p.d. gives a large extra current.",
                "Resistance = V/I at each point: compare V/I as the curve gets steeper."]),
    dict(id="o26s_thinnest_wire_graph", chapter=14, level=3, lo="14i", source="QTSS 2026 prelim MCQ 32",
         stem="I-V graphs are plotted for four wires of the same material and length. The gradients of the lines (current per volt) are: wire A 0.50 A/V, wire B 0.25 A/V, wire C 0.10 A/V, wire D 0.40 A/V. "
              "Which wire is the thinnest?",
         correct="wire C",
         wrongs={"wire A": "The steepest I-V line has the SMALLEST resistance, so it is the thickest wire.",
                 "wire B": "Wire B has a larger gradient (smaller resistance) than wire C, so it is thicker than C.",
                 "wire D": "A gradient of 0.40 A/V means a resistance of 2.5 Ω: a thick wire."},
         hints=["On an I-V graph the gradient is 1/R.", "Resistance is inversely proportional to cross-sectional area for the same length and material.",
                "The thinnest wire has the largest R and so the smallest gradient."]),
], category=CAT)


@template("o26s_lightning_current", chapter=14, level=2, lo="14c", category=CAT)
def lightning_current(rng):
    Q, t_ms = nice(rng, (150, 0.5), (120, 0.4), (90, 0.3), (200, 0.8))
    I = Q / (t_ms / 1000)
    return calc_q(rng, f"A lightning stroke transfers **{Q} C** of charge from a cloud to the ground in **{fmt(t_ms)} ms**. What is the average current in the stroke?", I,
                  [(Q / t_ms, "The time is in MILLIseconds: 1 ms = 0.001 s, so the current is 1000 times larger than this."),
                   (Q * t_ms / 1000, "That multiplies charge by time. Current = charge ÷ time."),
                   (I / 10, "Check the power of ten when converting ms to s.")],
                  "A", "I = Q / t",
                  [f"t = {fmt(t_ms)} ms = {fmt(t_ms / 1000)} s", f"I = {Q} / {fmt(t_ms / 1000)} = **{fmt(I)} A**", cite("BGSS 2024 prelim MCQ 31")],
                  ["Convert the time to seconds first.", "Current = charge ÷ time.", "Expect a very large number: lightning currents are enormous."])


@template("o26s_resistance_from_table", chapter=14, level=2, lo="14g", category=CAT)
def resistance_from_table(rng):
    R = nice(rng, 4.0, 5.0, 6.0, 2.5)
    Vs = (1.0, 2.0, 3.0)
    rows = [[fmt(V), fmt(V / R, dp=2)] for V in Vs]
    return calc_q(rng, "A resistor is connected to a variable supply. The p.d. across it and the current through it are measured:\n\n" + md_table(["p.d. / V", "current / A"], rows)
                  + "\n\nWhat is the resistance of the resistor?", R,
                  [(1 / R, "That is current ÷ p.d., the wrong way up. Resistance = p.d. ÷ current."),
                   (R * 3, "Use a matching PAIR of readings: 3.0 V with its own current, not 3.0 V with the first current."),
                   (3.0 / R, "That is a current reading, not a resistance.")],
                  "Ω", "R = V / I",
                  [f"Any pair: R = {fmt(Vs[2])} / {fmt(Vs[2] / R, dp=2)} = **{fmt(R)} Ω** (the same for every row, so the resistor obeys Ohm's law)",
                   cite("KCPSS 2024 prelim (5086) MCQ 16")],
                  ["Resistance = p.d. ÷ current.", "Pick one row of the table and divide.", "Check with another row: the answer should be the same."])


@template("o26s_wires_resistance_order", chapter=14, level=3, lo="14i", category=CAT)
def wires_resistance_order(rng):
    data = nice(rng, ((4.0, 2.0), (5.0, 1.0), (8.0, 6.0)), ((3.0, 1.5), (6.0, 1.0), (9.0, 6.0)), ((2.0, 0.5), (4.0, 2.0), (6.0, 1.0)))
    names = ("X", "Y", "Z")
    ratios = {n: L / A for n, (L, A) in zip(names, data)}
    order = sorted(names, key=lambda n: ratios[n])
    correct = ", ".join(order)
    wrongs = {", ".join(reversed(order)): "That is DESCENDING order. R ∝ L/A: the smallest L/A has the smallest resistance.",
              ", ".join(sorted(names, key=lambda n: data[names.index(n)][0])): "Ordering by length alone ignores the cross-sectional area.",
              ", ".join(sorted(names, key=lambda n: -data[names.index(n)][1])): "Ordering by area alone ignores the length."}
    wrongs = {k: v for k, v in wrongs.items() if k != correct}
    while len(wrongs) < 3:
        import itertools
        for p in itertools.permutations(names):
            s = ", ".join(p)
            if s != correct and s not in wrongs:
                wrongs[s] = "Work out L/A for each wire and sort from smallest to largest."
                break
    opts, key, mis = text_options(rng, correct, wrongs)
    rows = [[n, fmt(L), fmt(A)] for n, (L, A) in zip(names, data)]
    return dict(stem="Three copper wires have the dimensions shown.\n\n" + md_table(["wire", "length / m", "cross-sectional area / mm²"], rows)
                     + "\n\nWhich row lists the wires in order of **increasing** resistance?",
                options=opts, key=key, misconceptions=mis, formula="R ∝ L / A",
                working=[" ; ".join(f"{n}: L/A = {fmt(ratios[n])}" for n in names), f"Increasing resistance: **{correct}**", cite("NAS 2025 prelim MCQ 29")],
                hints=["Resistance is proportional to length and inversely proportional to cross-sectional area.", "Work out L ÷ A for each wire.", "Sort from the smallest value to the largest."])


explain_mcqs([
    dict(id="o26s_replacement_wire", chapter=14, level=4, lo="14i", source="XMSS 2024 prelim MCQ 29",
         stem="A heating wire of resistance R breaks and is replaced by a wire of the same length but **twice the diameter**, made of a metal with **twice the resistivity**. "
              "What is the resistance of the replacement wire?",
         correct="R / 2",
         wrongs={"R": "Doubling the diameter QUADRUPLES the area (R ÷ 4), and doubling the resistivity doubles R: net ÷ 2, not unchanged.",
                 "2R": "Doubling the diameter does more than halve the resistance: area ∝ diameter², so the resistance falls by a factor of 4.",
                 "4R": "Twice the diameter means a LARGER area and a SMALLER resistance; the resistivity only doubles it back partly."},
         hints=["R ∝ ρ L / A.", "Area ∝ diameter², so twice the diameter means four times the area.", "Combine: × 2 for resistivity, ÷ 4 for area."]),
    dict(id="o26s_torch_fridge_series", chapter=14, level=5, lo="14h", source="HGV 2024 prelim MCQ 33",
         stem="A torch bulb rated **3 V, 0.5 A** and a refrigerator lamp rated **240 V, 12 W** are connected in series across a 240 V supply. What happens when the circuit is switched on?",
         correct="The torch bulb glows very dimly, while the refrigerator lamp appears to work almost normally.",
         wrongs={"The torch bulb burns out at once, so no current flows.": "The torch bulb's resistance (6 Ω) is tiny compared with the lamp's (4800 Ω), so almost all the 240 V is across the lamp; the bulb gets only about 0.3 V.",
                 "Both work normally.": "In series the same current flows through both; the lamp's normal current (0.05 A) is far below the bulb's normal 0.5 A.",
                 "The torch bulb works normally, but the refrigerator lamp is dim.": "It is the other way round: the current is set by the high-resistance lamp, and that current is far too small for the bulb."},
         hints=["Find each component's resistance from its rating: R = V/I and R = V²/P.", "In series the p.d. is shared in proportion to resistance.",
                "The 4800 Ω lamp takes almost all of the 240 V; the current (≈ 0.05 A) is a tenth of what the bulb needs."]),
], category=CAT)


# ================================================================== Ch 15 D.C. circuits
explain_mcqs([
    dict(id="o26s_measure_resistance_circuit", chapter=15, level=2, lo="15a", source="BSS 2024 prelim (5086) MCQ 17",
         stem="Students draw a circuit diagram to measure the resistance of a resistor R using an ammeter and a voltmeter. Which arrangement is correct?",
         correct="the ammeter in series with R, and the voltmeter in parallel across R",
         wrongs={"the ammeter in parallel across R, and the voltmeter in series with R": "A voltmeter has a very high resistance: in series it would stop the current. An ammeter in parallel would short out R.",
                 "both meters in series with R": "A voltmeter must be connected ACROSS the component whose p.d. it measures.",
                 "both meters in parallel across R": "An ammeter must be in the path of the current it measures, in series."},
         hints=["An ammeter measures the current THROUGH a component: it goes in series.", "A voltmeter measures the p.d. ACROSS a component: it goes in parallel.",
                "Then R = V / I."]),
    dict(id="o26s_series_ammeters_same", chapter=15, level=2, lo="15b", source="NAS 2025 prelim MCQ 31",
         stem="A cell, a 4.0 Ω resistor and a 2.0 Ω resistor are connected in series with three ammeters: A₁ next to the cell, A₂ between the resistors and A₃ after the second resistor. "
              "A₁ reads 0.60 A. What do A₂ and A₃ read?",
         correct="A₂ = 0.60 A; A₃ = 0.60 A",
         wrongs={"A₂ = 0.40 A; A₃ = 0.20 A": "Current is not 'used up' by resistors. In a single loop the same current passes through every component.",
                 "A₂ = 0.30 A; A₃ = 0.30 A": "Nothing splits the current: there is only one path, so every ammeter reads the same.",
                 "A₂ = 0.60 A; A₃ = 0 A": "Charge cannot pile up: whatever flows into the last resistor flows out of it."},
         hints=["In a series circuit there is only one path for the current.", "The current at every point in a series circuit is the same.",
                "The resistors set the SIZE of the current, but it is the same size everywhere."]),
    dict(id="o26s_pd_series_ratio", chapter=15, level=3, lo="15c", source="XMSS 2024 prelim MCQ 33",
         stem="A 10 Ω resistor and a 20 Ω resistor are connected in series across a battery. How does the potential difference across the 20 Ω resistor compare with that across the 10 Ω resistor?",
         correct="It is twice as large.",
         wrongs={"It is the same.": "The same CURRENT flows through both, so V = I R is larger for the larger resistance.",
                 "It is half as large.": "V = I R with equal I: the 20 Ω resistor has the LARGER p.d.",
                 "It is four times as large.": "p.d. is proportional to resistance in series: 20 Ω gives twice, not four times, the p.d. of 10 Ω."},
         hints=["In series the same current flows through both resistors.", "V = I R for each.", "Compare 20 × I with 10 × I."]),
    dict(id="o26s_parallel_branch_pd", chapter=15, level=4, lo="15e", source="XMSS 2024 prelim MCQ 33",
         stem="A 40 Ω resistor is connected in parallel with a series pair of a 10 Ω and a 20 Ω resistor, and the combination is connected to a battery. Which statement is correct?",
         correct="The p.d. across the 40 Ω resistor equals the sum of the p.d.s across the 10 Ω and the 20 Ω resistors.",
         wrongs={"The p.d. across the 40 Ω resistor equals the p.d. across the 20 Ω resistor.": "The 40 Ω branch is in parallel with the WHOLE series pair, so its p.d. equals the pair's total p.d., not one part of it.",
                 "The current in the 40 Ω resistor equals the current in the 10 Ω resistor.": "The two branches have different resistances (40 Ω and 30 Ω), so they carry different currents.",
                 "The p.d. across the 10 Ω resistor equals the p.d. across the 20 Ω resistor.": "They are in series with the same current, so the 20 Ω has twice the p.d. of the 10 Ω."},
         hints=["Components in parallel have the same p.d. across them.", "What is in parallel with the 40 Ω: one resistor or the pair?",
                "The p.d. across a series pair is the sum of the two p.d.s."]),
    dict(id="o26s_parallel_no_increase", chapter=15, level=4, lo="15f", source="QTSS 2026 prelim MCQ 33",
         stem="A 20 Ω resistor is connected in series with an ammeter across a 2.0 V supply. A second component is then connected in parallel with the 20 Ω resistor. "
              "Which component would **not** increase the ammeter reading?",
         correct="a voltmeter",
         wrongs={"another 20 Ω resistor": "Adding a parallel resistor lowers the combined resistance to 10 Ω, so the current doubles.",
                 "a 5 Ω resistor": "A 5 Ω path in parallel takes a large extra current: the reading rises a lot.",
                 "a piece of copper wire": "A wire short-circuits the resistor: the resistance drops to almost zero and the current shoots up."},
         hints=["Adding a parallel path LOWERS the total resistance unless the path carries almost no current.", "Which component is designed to carry almost no current?",
                "A voltmeter has a very high resistance."]),
    dict(id="o26s_ldr_brighter_dark", chapter=15, level=4, lo="15i", source="QTSS 2026 prelim MCQ 34",
         stem="A lamp and an LDR are connected in series across a battery, and a second lamp is connected in parallel with the LDR. The room becomes darker. What happens to the second lamp?",
         correct="It becomes brighter, because the LDR's resistance rises and a larger share of the p.d. appears across the LDR and the lamp in parallel with it.",
         wrongs={"It becomes dimmer, because the LDR's resistance falls in the dark.": "An LDR's resistance RISES when the light level falls.",
                 "It becomes dimmer, because less current flows in the whole circuit.": "The total current does fall a little, but the p.d. across the LDR-lamp pair rises, and that is what sets this lamp's brightness.",
                 "It does not change, because the lamp is not an LDR.": "The lamp shares the LDR's p.d., and that p.d. changes with the light level."},
         hints=["An LDR has a HIGH resistance in the dark and a LOW resistance in bright light.", "In a series chain, a component with more resistance takes a larger share of the p.d.",
                "The second lamp is in parallel with the LDR, so it has the same p.d. as the LDR."]),
    dict(id="o26s_ldr_light_current", chapter=15, level=2, lo="15i", source="XMSS 2024 prelim MCQ 32",
         stem="An LDR is connected in series with an ammeter and a cell. The light falling on the LDR becomes brighter. What happens to the ammeter reading?",
         correct="It increases.",
         wrongs={"It decreases.": "Brighter light LOWERS the resistance of an LDR, so more current flows.",
                 "It does not change.": "The LDR's resistance depends on the light level, so the current changes.",
                 "It becomes zero.": "The LDR still conducts; in bright light it conducts better than before."},
         hints=["LDR stands for light-dependent resistor.", "More light means a lower resistance.", "Lower resistance with the same e.m.f. means a larger current."]),
], category=CAT)


@template("o26s_effective_resistance_mixed", chapter=15, level=3, lo="15f", category=CAT)
def effective_resistance_mixed(rng):
    R1, R2, R3 = nice(rng, (2.0, 3.0, 5.0), (4.0, 2.0, 6.0), (1.0, 3.0, 4.0), (6.0, 6.0, 4.0))
    series = R1 + R2
    R = series * R3 / (series + R3)
    return calc_q(rng, f"A **{fmt(R1)} Ω** resistor and a **{fmt(R2)} Ω** resistor are connected in series, and this pair is connected in parallel with a **{fmt(R3)} Ω** resistor. "
                  "What is the effective resistance of the combination?", R,
                  [(R1 + R2 + R3, "That adds all three as if they were in series. The third resistor is in PARALLEL with the pair."),
                   (1 / (1 / R1 + 1 / R2 + 1 / R3), "That treats all three as parallel. The first two are in series with each other."),
                   (series + R3, "Add the series pair first, then combine that total in PARALLEL with the third resistor (1/R = 1/R_pair + 1/R₃).")],
                  "Ω", "R_pair = R₁ + R₂; 1/R = 1/R_pair + 1/R₃",
                  [f"Series pair: {fmt(R1)} + {fmt(R2)} = {fmt(series)} Ω", f"1/R = 1/{fmt(series)} + 1/{fmt(R3)}  ⇒  R = **{fmt(R)} Ω**", cite("NAS 2025 prelim MCQ 30")],
                  ["Combine the series pair first by adding.", "Then combine that result in parallel with the third resistor.",
                   "For two resistors in parallel: R = product ÷ sum."])


@template("o26s_divider_find_r", chapter=15, level=4, lo="15j", category=CAT)
def divider_find_r(rng):
    E, R2, V = nice(rng, (6.0, 9.0, 1.5), (6.0, 6.0, 2.0), (12.0, 9.0, 3.0), (9.0, 6.0, 3.0))
    R = V * R2 / (E - V)
    return calc_q(rng, f"In a potential divider a resistor R is in series with a **{fmt(R2)} Ω** resistor across a **{fmt(E)} V** supply. A voltmeter across R reads **{fmt(V)} V**. What is the value of R?", R,
                  [(V * R2 / E, "The p.d. across the {fmt(R2)} Ω resistor is E − V, not E."),
                   (R2 * E / V, "That gives the total resistance scaled the wrong way: use V_R / V_other = R / R_other."),
                   (R2, "If R equalled the other resistor the voltmeter would read half the supply.")],
                  "Ω", "p.d. shares in proportion to resistance: V / (E − V) = R / R₂",
                  [f"p.d. across the {fmt(R2)} Ω = {fmt(E)} − {fmt(V)} = {fmt(E - V)} V", f"R / {fmt(R2)} = {fmt(V)} / {fmt(E - V)}  ⇒  R = **{fmt(R)} Ω**",
                   cite("BGSS 2024 prelim MCQ 32")],
                  ["The two p.d.s add up to the supply voltage.", "In series the p.d.s are in the same ratio as the resistances.", "Set up the ratio and solve for R."])


# ================================================================== Ch 16 Practical electricity
explain_mcqs([
    dict(id="o26s_heating_effect_appliances", chapter=16, level=1, lo="16a", source="WDL 2024 prelim MCQ 33",
         stem="A fan heater contains a small motor that drives the fan and two heating elements. Which parts of the heater work by the **heating effect** of a current?",
         correct="the heating elements only",
         wrongs={"the motor only": "The motor works by the MAGNETIC effect of a current (a force on a current-carrying coil).",
                 "the motor and the heating elements": "The motor's job is to turn, not to heat; any warming of the motor is wasted energy.",
                 "neither; the heater uses the chemical effect of a current": "Kettles, ovens and heaters all rely on current heating a resistance wire."},
         hints=["A current in a high-resistance wire transfers energy to its internal store: the wire gets hot.", "That is what a heating element is.",
                "A motor turns because of the force on a current in a magnetic field."]),
    dict(id="o26s_not_a_hazard", chapter=16, level=2, lo="16d", source="NAS 2025 prelim MCQ 34",
         stem="Which of these is **not** an electrical hazard?",
         correct="fitting the switch of an appliance in the live wire",
         wrongs={"exposed wires where the insulation is damaged": "Touching an exposed live wire gives a shock; damaged insulation is a hazard.",
                 "using electrical appliances with wet hands": "Water lowers the resistance of the skin, so a shock current is much larger.",
                 "fitting the fuse in the neutral wire": "With the fuse in the neutral, the appliance stays connected to the live wire even after the fuse blows."},
         hints=["Three hazards in the syllabus: damaged insulation, overheating cables, damp conditions.", "Switches and fuses BELONG in the live wire.",
                "Which option is correct practice rather than a danger?"]),
    dict(id="o26s_plug_wires_statement", chapter=16, level=2, lo="16h", source="HGV 2024 prelim MCQ 32 and QTSS 2026 prelim MCQ 35",
         stem="In a three-pin plug, wire P is green-and-yellow, wire Q is blue and wire R is brown. Which statement is **not** correct?",
         correct="Wire P carries the current to the appliance.",
         wrongs={"Wire P carries current only if there is a fault that makes the casing live.": "Correct: P is the earth wire, a safety path that normally carries no current.",
                 "Wire Q is the neutral wire that completes the circuit back to the supply.": "Correct: blue is neutral.",
                 "Wire R is connected to the fuse and the switch.": "Correct: brown is live, and the fuse and switch are fitted in the live wire."},
         hints=["Green-and-yellow = earth, blue = neutral, brown = live.", "The live wire brings the current in at high potential; the neutral takes it back.",
                "The earth wire carries current only when something goes wrong."]),
    dict(id="o26s_switch_fuse_neutral", chapter=16, level=4, lo="16i", source="RGT 2024 prelim MCQ 36",
         stem="By mistake, the switch and the fuse of an electric kettle are connected in the neutral wire instead of the live wire. Which statement is correct?",
         correct="The kettle works when switched on, but its heating element stays at mains potential even when the switch is off.",
         wrongs={"The kettle does not work when the switch is closed.": "The circuit is still complete through live, element, switch and neutral, so the kettle heats normally.",
                 "The kettle works even when the switch is open.": "An open switch anywhere in the loop breaks the circuit; the fault is about SAFETY, not operation.",
                 "The fuse can no longer blow, however large the current.": "The fuse still melts if the current is too large; the problem is that the live side stays connected after it does."},
         hints=["Switching off should disconnect the appliance from the LIVE (high-potential) wire.", "With the switch in the neutral, the element is still joined to the live wire when off.",
                "Touching the element could then still give a shock."]),
], category=CAT)


@template("o26s_lamp_energy", chapter=16, level=2, lo="16b", category=CAT)
def lamp_energy(rng):
    V, I, mins = nice(rng, (3.0, 0.20, 2), (6.0, 0.25, 2), (3.0, 0.30, 3), (4.5, 0.20, 5))
    E = V * I * mins * 60
    return calc_q(rng, f"A lamp works from a **{fmt(V)} V** supply and takes a current of **{fmt(I)} A**. It is switched on for **{mins} minutes**. How much electrical energy does it use?", E,
                  [(V * I * mins, "The time must be in SECONDS: multiply the minutes by 60."),
                   (V * I, "That is the power in watts (energy per second). Multiply by the time in seconds."),
                   (V / I * mins * 60, "V / I is the resistance, not the power. Energy = V × I × t.")],
                  "J", "E = V I t",
                  [f"t = {mins} × 60 = {mins * 60} s", f"E = {fmt(V)} × {fmt(I)} × {mins * 60} = **{fmt(E)} J**", cite("QTSS 2026 prelim MCQ 29")],
                  ["Power P = V I.", "Energy = power × time.", "Change minutes into seconds."])


@template("o26s_fuse_rating", chapter=16, level=3, lo="16e", category=CAT)
def fuse_rating(rng):
    P = nice(rng, 720, 960, 600, 1800)
    I = P / 240
    fuses = [1, 2, 3, 5, 10, 13]
    correct_f = next(f for f in fuses if f > I)
    correct = f"{correct_f} A"
    below = max(f for f in fuses if f < I) if any(f < I for f in fuses) else 1
    above2 = next((f for f in fuses if f > correct_f), 13)
    wrongs = {f"{below} A": f"The normal current is {fmt(I)} A: a {below} A fuse would melt during normal use.",
              f"{above2} A": f"A {above2} A fuse lets a dangerously large current flow before it melts. Choose the smallest rating ABOVE the normal current.",
              f"{int(round(I)) if int(round(I)) not in (below, correct_f, above2) else 20} A": "The fuse rating must be a little above the working current, not equal to it or far from it."}
    opts, key, mis = text_options(rng, correct, wrongs)
    return dict(stem=f"An appliance is rated **240 V, {P} W**. Fuses of 1 A, 2 A, 3 A, 5 A, 10 A and 13 A are available. Which fuse is most suitable?",
                options=opts, key=key, misconceptions=mis, formula="I = P / V; choose the smallest fuse rating above the normal current",
                working=[f"I = P / V = {P} / 240 = {fmt(I)} A", f"The smallest available rating above {fmt(I)} A is **{correct}**", cite("NAS 2025 prelim MCQ 33")],
                hints=["Find the normal working current from P = V I.", "The fuse must NOT melt in normal use, so its rating is above that current.",
                       "But only a little above, so it melts quickly if a fault occurs."])


@template("o26s_plug_currents", chapter=16, level=3, lo="16g", category=CAT)
def plug_currents(rng):
    P = nice(rng, 1500, 1200, 2400, 960)
    I = P / 240
    correct = f"live {fmt(I)} A; neutral {fmt(I)} A; earth 0 A"
    wrongs = {f"live {fmt(I)} A; neutral 0 A; earth 0 A": "The current that flows in through the live wire must flow back out through the neutral wire: the circuit is a loop.",
              f"live {fmt(I)} A; neutral {fmt(I)} A; earth {fmt(I)} A": "The earth wire carries current only when there is a fault; normally it carries none.",
              f"live 0 A; neutral 0 A; earth {fmt(I)} A": "The earth wire is a safety connection; the working current flows in the live and neutral wires."}
    opts, key, mis = text_options(rng, correct, wrongs)
    return dict(stem=f"A **{P} W** kettle works normally from the **240 V** mains. What are the currents in the live, neutral and earth wires of its plug?",
                options=opts, key=key, misconceptions=mis, formula="I = P / V in live and neutral; earth carries current only under a fault",
                working=[f"I = P / V = {P} / 240 = {fmt(I)} A in the live wire and the same in the neutral wire (the return path).",
                         "The earth wire carries no current unless the live wire touches the casing.", f"Correct answer: **{correct}**", cite("BGSS 2024 prelim MCQ 35")],
                hints=["I = P / V.", "The current goes in through the live and comes back through the neutral.", "The earth wire is only for faults."])


# ================================================================== Ch 17 Magnetism
explain_mcqs([
    dict(id="o26s_compass_turntable", chapter=17, level=3, lo="17a", source="XMSS 2024 prelim MCQ 35",
         stem="A bar magnet lies on a turntable with a plotting compass placed just beyond one end. The turntable is rotated slowly clockwise. What does the compass needle do?",
         correct="It rotates, following the magnet's field as the poles move round.",
         wrongs={"It does not move.": "The needle lines up with the field at its position, and that field direction changes as the magnet turns.",
                 "It points towards geographic north throughout.": "The bar magnet's field near the compass is far stronger than the Earth's, so the needle follows the magnet.",
                 "It spins continuously at high speed.": "The needle simply keeps pointing along the local field, so it turns at the same slow rate as the turntable."},
         hints=["A compass needle is a small magnet that lines up with the field where it is.", "As the bar magnet turns, which way does its field point at the compass?",
                "The needle keeps lining up with the changing field."]),
    dict(id="o26s_rod_both_poles_attract", chapter=17, level=3, lo="17a", source="HGV 2024 prelim MCQ 34",
         stem="End X of a metal rod is attracted when it is brought near the N pole of a magnet, and also attracted when brought near the S pole. "
              "How will end Y of the rod behave near each pole?",
         correct="attracted by the N pole and attracted by the S pole",
         wrongs={"attracted by the N pole and repelled by the S pole": "Repulsion happens only between two magnets. X was attracted by BOTH poles, so the rod is not a magnet; Y cannot repel either pole.",
                 "repelled by the N pole and attracted by the S pole": "An unmagnetised iron rod is attracted by either pole at either end.",
                 "repelled by both poles": "Repulsion by both poles is impossible for any rod."},
         hints=["Repulsion is the only sure test for a magnet.", "If X is attracted by both poles, the rod is an unmagnetised magnetic material.",
                "An unmagnetised iron rod is attracted by either pole at either end."]),
    dict(id="o26s_sheets_shield_clips", chapter=17, level=4, lo="17c", source="QTSS 2026 prelim MCQ 37",
         stem="A magnet is fixed on top of a matchbox cover and iron paperclips cling to the bottom of the cover. A thin metal sheet is slid inside the cover, between the magnet and the clips. "
              "With sheet X in place the clips stay attached; with sheet Y in place they all fall off. Which metals could the sheets be made from?",
         correct="X aluminium; Y iron",
         wrongs={"X iron; Y aluminium": "An iron sheet would carry the magnetic field through itself (magnetic shielding) and the clips would FALL; aluminium lets the field pass.",
                 "X iron; Y copper": "Iron shields the clips from the field, so the clips would fall with X, not stay.",
                 "X bronze; Y aluminium": "Neither bronze nor aluminium is magnetic: both would let the field through and the clips would stay in both cases."},
         hints=["Aluminium, copper and bronze are non-magnetic: a magnetic field passes straight through them.", "Iron is a soft magnetic material: it channels the field lines through itself.",
                "Which sheet lets the field reach the clips, and which one 'steals' the field?"]),
    dict(id="o26s_compass_near_pole", chapter=17, level=2, lo="17d", source="Punggol 2024 prelim MCQ 32 and ACSBR 2024 prelim MCQ 36",
         stem="A plotting compass is used to trace the field around a bar magnet. When the compass is placed a short distance beyond the magnet's N pole, along the axis, which way does its needle point?",
         correct="directly away from the N pole, along the axis of the magnet",
         wrongs={"directly towards the N pole": "The needle's own N end is repelled by the magnet's N pole and points away from it, along the field line.",
                 "at right angles to the axis": "On the axis beyond a pole the field runs along the axis, so the needle lies along it.",
                 "towards geographic north": "Close to a bar magnet its field is much stronger than the Earth's; the needle follows the magnet's field."},
         hints=["A compass needle points along the magnetic field line at its position.", "Field lines leave the N pole of a magnet.",
                "Beyond the N pole, the field points away from the magnet."]),
    dict(id="o26s_bar_magnet_field_lines", chapter=17, level=2, lo="17e", source="ACSBR 2024 prelim MCQ 36",
         stem="Fig. 1 shows the magnetic field pattern around a bar magnet. Which statement about the field lines is correct?",
         correct="They leave the N pole and enter the S pole, and they are closest together near the poles where the field is strongest.",
         wrongs={"They leave the S pole and enter the N pole.": "Outside the magnet, field lines run from N to S (the direction a compass needle's N end points).",
                 "They are spaced evenly everywhere, because the field strength is the same all round the magnet.": "The lines crowd together near the poles: that is where the field is strongest.",
                 "They cross one another between the poles.": "Field lines never cross: a compass at a crossing point would have to point two ways at once."},
         hints=["The arrows on field lines show which way a compass's N end points.", "A compass N end is attracted to the magnet's S pole.",
                "Closer lines mean a stronger field."],
         figure=lambda: figs3.bar_magnet_field()),
], category=CAT)


# ================================================================== Ch 18 Electromagnetism
explain_mcqs([
    dict(id="o26s_magnet_attracted_coil", chapter=18, level=2, lo="18b", source="QTSS 2026 prelim MCQ 36",
         stem="A magnet hanging near a coil of wire is attracted to the coil only while there is a current in the coil. Which statement explains this?",
         correct="The current in the coil produces a magnetic field.",
         wrongs={"The coil is made of soft iron.": "A copper coil is not magnetic on its own; the attraction appears only when current flows.",
                 "The current induces an electric charge on the magnet.": "Charge is not involved; the force is magnetic, from the field around the current.",
                 "The coil has its own gravitational field.": "Gravitational attraction between a coil and a magnet is far too small to notice, and it would not switch on and off with the current."},
         hints=["What appears around a wire only when current flows through it?", "A coil carrying a current behaves like a bar magnet.",
                "Switch the current off and the field disappears."]),
    dict(id="o26s_electron_beam_deflect", chapter=18, level=4, lo="18c", source="XMSS 2024 prelim MCQ 36 and BGSS 2024 prelim MCQ 37",
         stem="A beam of electrons travels from left to right across the page and enters a magnetic field directed **into** the page. In which direction is the beam deflected as it enters the field?",
         correct="towards the bottom of the page",
         wrongs={"towards the top of the page": "Electrons are NEGATIVE: conventional current is from right to LEFT. Fleming's left-hand rule then gives the force downwards.",
                 "into the page": "The force is always at right angles to BOTH the field and the motion; it cannot be along the field.",
                 "out of the page": "The force is perpendicular to the field, so it cannot point along the field direction."},
         hints=["Conventional current is opposite to the electron flow: here it points to the left.", "Fleming's left-hand rule: First finger = Field (into the page), seCond finger = Current (left), thuMb = Motion.",
                "Set your hand up and read the thumb's direction."]),
    dict(id="o26s_wire_between_poles_force", chapter=18, level=3, lo="18d", source="QTSS 2026 prelim MCQ 39",
         stem="Fig. 1 shows a straight wire between the poles of a magnet. The field points from left to right and the current in the wire is into the page. In which direction is the force on the wire?",
         correct="downwards",
         wrongs={"upwards": "Check the rule: First finger along the field (to the right), seCond finger along the current (into the page); the thuMb then points DOWN.",
                 "to the left, towards the N pole": "The force is at right angles to the field, so it cannot be along the field direction.",
                 "out of the page": "The force is at right angles to the current, so it cannot be along the wire."},
         hints=["Use Fleming's left-hand rule.", "First finger: field (N to S). Second finger: conventional current.", "The thumb gives the force on the wire."],
         figure=lambda: figs3.flemings_lhr(field="right", current="into", show_force=False)),
    dict(id="o26s_motor_faster_reverse", chapter=18, level=3, lo="18e", source="BRD 2024 prelim MCQ 37",
         stem="A simple d.c. motor turns anticlockwise when a small current flows through its coil from P to Q. Which change makes the coil turn **clockwise** and **faster**?",
         correct="pass a larger current through the coil from Q to P",
         wrongs={"pass a larger current through the coil from P to Q": "A larger current makes it faster, but keeping the same current direction keeps the same direction of rotation.",
                 "pass a smaller current through the coil from Q to P": "Reversing the current reverses the rotation, but a smaller current gives a SMALLER turning effect.",
                 "pass a smaller current through the coil from P to Q": "That makes the motor slower and leaves it turning the same way."},
         hints=["Reversing the current (or the field) reverses the direction of rotation.", "The turning effect grows with the current, the number of turns and the field strength.",
                "Pick the option that does both."]),
    dict(id="o26s_commutator_function", chapter=18, level=2, lo="18f", source="ACSBR 2024 prelim MCQ 38",
         stem="What is the main function of the split-ring commutator in a simple d.c. motor?",
         correct="to reverse the direction of the current in the coil every half turn, so that the coil keeps turning the same way",
         wrongs={"to allow current to flow into the coil": "The brushes and rings do connect the coil to the supply, but SLIP rings would do that too; the SPLIT is there to reverse the current.",
                 "to stop the connecting wires twisting": "Avoiding twisted wires is a side benefit of any ring-and-brush contact, not the purpose of the split.",
                 "to split the current equally between the two halves of the coil": "The same current flows round the whole coil; the commutator changes its DIRECTION, not its size."},
         hints=["Think about the coil just after it passes the vertical.", "Without a change, the force on each side would push it back the way it came.",
                "The split ring swaps the connections at that moment."]),
], category=CAT)


# ================================================================== Ch 19 Electromagnetic induction
explain_mcqs([
    dict(id="o26s_induced_emf_factor", chapter=19, level=2, lo="19a", source="NAS 2025 prelim MCQ 37",
         stem="A bar magnet is pushed into one end of a long coil connected to a sensitive meter. Which change affects the **size** of the meter's deflection?",
         correct="the number of turns in the coil",
         wrongs={"which end of the coil the magnet is pushed into": "That changes the DIRECTION of the induced current, not its size.",
                 "which pole of the magnet enters first": "Swapping the pole reverses the direction of the induced e.m.f.; its size is unchanged.",
                 "the direction in which the coil is wound": "Winding direction only affects which way the meter deflects."},
         hints=["Faraday: the induced e.m.f. depends on the rate of change of magnetic flux and the number of turns.", "Speed of the magnet, strength of the magnet and number of turns change the size.",
                "Direction of motion, pole or winding changes only the sign."]),
    dict(id="o26s_no_induced_current", chapter=19, level=3, lo="19a", source="BRD 2024 prelim MCQ 38",
         stem="A coil is connected to a sensitive ammeter and a bar magnet is held near it. Which action does **not** produce a reading on the ammeter?",
         correct="moving the coil and the magnet together in the same direction at the same speed",
         wrongs={"pushing the magnet into the coil": "The magnetic field through the coil changes, so an e.m.f. is induced.",
                 "pulling the coil away from the stationary magnet": "Relative motion changes the field through the coil: a current is induced.",
                 "turning the magnet round end to end near the coil": "Reversing the magnet changes the field through the coil, inducing an e.m.f."},
         hints=["An e.m.f. is induced only while the magnetic field through the coil is CHANGING.", "If the coil and magnet move together, does the field through the coil change?",
                "No relative motion means no change in flux."]),
    dict(id="o26s_ring_over_magnet_lenz", chapter=19, level=5, lo="19a", source="BGSS 2024 prelim MCQ 38",
         stem="A copper ring is dropped over a vertical bar magnet, N pole uppermost, falling from above the N pole (X) past the middle to below the S pole (Y). Viewed from above, which statement about the induced current in the ring is correct?",
         correct="It flows one way as the ring approaches the N pole at X and the opposite way as it leaves the S pole at Y.",
         wrongs={"It flows clockwise throughout the fall.": "By Lenz's law the current opposes the motion: it repels the approaching N pole, then ATTRACTS the receding S pole, which needs the opposite direction.",
                 "It flows anticlockwise throughout the fall.": "The direction must reverse: the flux through the ring first increases and then decreases.",
                 "No current flows because the ring is not connected to a cell.": "A changing magnetic field through a closed conducting loop induces a current without any cell."},
         hints=["Lenz's law: the induced current opposes the change producing it.", "Approaching the N pole, the ring acts like a N pole on its top face to repel the magnet.",
                "Leaving the S pole, the ring acts to attract the magnet back: its current must reverse."]),
    dict(id="o26s_ac_output_devices", chapter=19, level=3, lo="19b", source="QTSS 2026 prelim MCQ 38 and HGV 2024 prelim MCQ 36",
         stem="Three devices are described: X, a coil rotating in a magnetic field connected to the circuit through two slip rings; Y, the same coil connected through a split-ring commutator; "
              "Z, a chemical cell. Which devices give an alternating current (a.c.) output?",
         correct="X only",
         wrongs={"X and Y": "The split-ring commutator in Y reverses the connections every half turn, so its output is always in the same direction (d.c.).",
                 "Y only": "A commutator makes the output one-directional; the slip-ring machine X is the a.c. generator.",
                 "X and Z": "A cell gives a steady direct current, never a.c."},
         hints=["Slip rings keep each end of the coil joined to the same brush: the output reverses every half turn.", "A commutator swaps the connections every half turn, cancelling that reversal.",
                "A cell is a d.c. source."]),
], category=CAT)


@template("o26s_transformer_turns_pair", chapter=19, level=3, lo="19d", category=CAT)
def transformer_turns_pair(rng):
    Vp, Vs = nice(rng, (240, 4800), (240, 2400), (120, 2400), (240, 6000))
    ratio = Vs // Vp
    good = nice(rng, (50, 50 * ratio), (100, 100 * ratio), (40, 40 * ratio))
    correct = f"N_p = {good[0]}, N_s = {good[1]}"
    wrongs = {f"N_p = {good[1]}, N_s = {good[0]}": "That is a STEP-DOWN transformer: more turns on the primary gives a lower secondary voltage.",
              f"N_p = {good[0]}, N_s = {good[1] * 2}": f"That ratio is {2 * ratio} : 1, which would give {Vp * 2 * ratio} V, double what is needed.",
              f"N_p = {Vp}, N_s = {Vs * 10}": f"The turns ratio must equal the voltage ratio ({ratio} : 1); this pair has a ratio of {10 * ratio} : 1."}
    opts, key, mis = text_options(rng, correct, wrongs)
    return dict(stem=f"A transformer is needed to change an alternating supply of **{Vp} V** into **{Vs} V**. Which pair of coils is suitable?",
                options=opts, key=key, misconceptions=mis, formula="N_s / N_p = V_s / V_p",
                working=[f"V_s / V_p = {Vs} / {Vp} = {ratio}, so the secondary needs {ratio} times as many turns as the primary.", f"Correct answer: **{correct}**",
                         cite("NAS 2025 prelim MCQ 39")],
                hints=["The voltages are in the same ratio as the numbers of turns.", f"{Vs} ÷ {Vp} tells you how many times more turns the secondary needs.",
                       "A step-up transformer has more turns on the secondary."])


@template("o26s_transmission_loss", chapter=19, level=4, lo="19f", category=CAT)
def transmission_loss(rng):
    P_kw, V_kv, R = nice(rng, (150, 25, 8.0), (200, 25, 6.0), (120, 20, 10.0), (300, 50, 8.0))
    I = P_kw * 1000 / (V_kv * 1000)
    loss = I * I * R
    return calc_q(rng, f"A power station delivers **{P_kw} kW** to a factory along cables of total resistance **{fmt(R)} Ω**, at a transmission voltage of **{V_kv} kV**. "
                  "What is the power lost in the cables?", loss,
                  [(I * R, "I × R is the p.d. DROPPED along the cables (in volts), not the power lost."),
                   ((V_kv * 1000) ** 2 / R, "V²/R uses the full transmission voltage, but only a small part of it is dropped across the cables. Use I²R."),
                   (loss / 10, "Check the current: I = P / V with both in base units (W and V).")],
                  "W", "I = P / V; P_loss = I² R",
                  [f"I = {P_kw * 1000} / {V_kv * 1000} = {fmt(I)} A", f"P_loss = I² R = {fmt(I)}² × {fmt(R)} = **{fmt(loss)} W**", cite("HGV 2024 prelim MCQ 38")],
                  ["First find the current in the cables: I = P / V.", "Power lost as heat in a resistance = I² R.", "Notice how small the loss is at high voltage."])


# ================================================================== Ch 20 Radioactivity
explain_mcqs([
    dict(id="o26s_radium_atom_statement", chapter=20, level=2, lo="20a", source="BPGHS 2024 prelim MCQ 38",
         stem="A neutral atom of radium has the nuclide notation ²²⁶₈₈Ra. Which statement about the atom is correct?",
         correct="88 electrons move around a nucleus that contains 88 protons and 138 neutrons.",
         wrongs={"There are 88 electrons in the nucleus.": "Electrons are outside the nucleus; the nucleus contains only protons and neutrons.",
                 "There are 138 protons in the nucleus.": "The proton number is the lower number, 88. 138 is the number of NEUTRONS (226 − 88).",
                 "There are 226 neutrons in the nucleus.": "226 is the nucleon number: protons and neutrons together."},
         hints=["The lower number is the proton (atomic) number.", "The upper number is the nucleon number: protons + neutrons.", "A neutral atom has as many electrons as protons."]),
    dict(id="o26s_carbon_isotopes", chapter=20, level=2, lo="20b", source="FHSS 2025 prelim Paper 2 Q8",
         stem="Carbon-12 and carbon-14 are isotopes of carbon. How does a nucleus of carbon-14 differ from a nucleus of carbon-12?",
         correct="It has the same number of protons but two more neutrons.",
         wrongs={"It has two more protons and the same number of neutrons.": "Two more protons would make it a different ELEMENT (oxygen), not an isotope of carbon.",
                 "It has the same number of protons and neutrons but two more electrons.": "Electrons are not in the nucleus, and isotopes differ in their neutron number.",
                 "It has two more protons and two more neutrons.": "Isotopes of the same element always have the SAME proton number."},
         hints=["Isotopes are atoms of the same element: same proton number.", "The nucleon numbers differ: 12 and 14.", "The extra nucleons must be neutrons."]),
    dict(id="o26s_decay_random", chapter=20, level=1, lo="20d", source="FMSS 2024 prelim (5086) MCQ 20",
         stem="Which statement about radioactive decay is correct?",
         correct="It is a random and spontaneous process: it cannot be predicted when a particular nucleus will decay, and it is unaffected by temperature or pressure.",
         wrongs={"It happens faster when the sample is heated.": "Decay is a nuclear process; heating affects the electrons and the motion of atoms, not the nucleus.",
                 "Every nucleus in a sample decays at exactly the same moment.": "Decay is random: individual nuclei decay at unpredictable times, which is why a sample has a half-life.",
                 "It only happens when the nucleus is struck by another particle.": "Spontaneous means it happens on its own, without any trigger."},
         hints=["'Random' means you cannot say which nucleus will decay next.", "'Spontaneous' means nothing needs to trigger it.",
                "External conditions like temperature make no difference."]),
    dict(id="o26s_alpha_nature", chapter=20, level=1, lo="20e", source="XMSS 2024 prelim MCQ 39 and BGSS 2024 prelim MCQ 39",
         stem="Which statement about an alpha particle is correct?",
         correct="It is a helium nucleus, positively charged and strongly ionising.",
         wrongs={"It is an electron emitted from the nucleus.": "That describes a BETA particle.",
                 "It is a type of electromagnetic radiation with no charge.": "That describes GAMMA radiation.",
                 "It is a helium nucleus that can pass through thick paper.": "Alpha particles are stopped by a sheet of paper or a few centimetres of air."},
         hints=["An alpha particle is two protons and two neutrons.", "Its double positive charge and large mass make it very ionising.", "Ionising strongly means it loses energy quickly: low penetration."]),
    dict(id="o26s_smoke_detector_alpha", chapter=20, level=3, lo="20i", source="Punggol 2024 prelim MCQ 38",
         stem="Smoke detectors use an alpha source. Which row explains why alpha particles are suitable?",
         correct="high ionising ability, so they make the air conduct a small current; low penetrating power, so they are stopped by smoke and cannot leave the detector",
         wrongs={"high ionising ability; high penetrating power, so they pass through the smoke": "If the particles passed through the smoke unchanged, the current would not drop and the alarm would not sound.",
                 "low ionising ability, to keep the device safe; high penetrating power": "Alpha particles are the MOST ionising radiation, and the detector relies on that to produce a current.",
                 "low ionising ability; low penetrating power": "Low ionisation would give almost no current in the air gap: the detector would not work."},
         hints=["The source ionises the air between two plates so a tiny current flows.", "Smoke absorbs the alpha particles, the current falls and the alarm sounds.",
                "Low penetration also keeps the radiation inside the casing."]),
    dict(id="o26s_fusion_statement", chapter=20, level=1, lo="20j", source="QTSS 2026 prelim MCQ 40",
         stem="Which statement describes nuclear fusion?",
         correct="Two light nuclei join to form one heavier nucleus, releasing energy.",
         wrongs={"A heavy nucleus splits into two lighter nuclei, releasing energy.": "That is nuclear FISSION, as in a nuclear power station.",
                 "An unstable nucleus loses energy by emitting a particle or radiation.": "That is radioactive DECAY.",
                 "A fast nucleus knocks electrons off atoms to form ions.": "That is IONISATION, the effect of radiation passing through matter."},
         hints=["'Fuse' means join together.", "It is the process that powers the Sun, where hydrogen nuclei join to make helium.", "Very high temperatures are needed to overcome the repulsion between the nuclei."]),
], category=CAT)


@template("o26s_beta_decay_change", chapter=20, level=2, lo="20f", category=CAT)
def beta_decay_change(rng):
    kind = nice(rng, "beta", "alpha")
    if kind == "beta":
        correct, why = "proton number +1; nucleon number unchanged", "In β decay a neutron becomes a proton and an electron: Z rises by 1 and A is unchanged."
        wrongs = {"proton number −1; nucleon number unchanged": "A β⁻ particle is a NEGATIVE electron leaving the nucleus, so the nucleus becomes MORE positive: Z goes UP.",
                  "proton number +1; nucleon number +1": "The electron leaving has almost no mass and is not a nucleon, so A does not change.",
                  "proton number −2; nucleon number −4": "That is the change for ALPHA decay."}
    else:
        correct, why = "proton number −2; nucleon number −4", "An α particle is 2 protons + 2 neutrons, so Z falls by 2 and A by 4."
        wrongs = {"proton number −2; nucleon number −2": "An alpha particle carries away 4 nucleons (2 protons AND 2 neutrons).",
                  "proton number +1; nucleon number unchanged": "That is the change for BETA decay.",
                  "proton number −4; nucleon number −2": "The numbers are the wrong way round: Z − 2 and A − 4."}
    opts, key, mis = text_options(rng, correct, wrongs)
    return dict(stem=f"A nucleus emits {'a β-particle' if kind == 'beta' else 'an α-particle'}. What change does this make to the proton number and the nucleon number of the nucleus?",
                options=opts, key=key, misconceptions=mis, formula="α: A−4, Z−2;  β: A unchanged, Z+1",
                working=[why, f"Correct answer: **{correct}**", cite("NAS 2025 prelim MCQ 40")],
                hints=["Write the particle in nuclide notation: α = ⁴₂He, β = ⁰₋₁e.", "Both A and Z must balance on each side of the decay equation.",
                       "Subtract the particle's numbers from the parent nucleus."])


@template("o26s_two_beta_one_alpha", chapter=20, level=4, lo="20f", category=CAT)
def two_beta_one_alpha(rng):
    Z, N = nice(rng, (90, 144), (88, 138), (92, 146), (86, 136))
    Z2, N2 = Z + 2 - 2, N - 2 - 2
    correct = f"{Z2} protons and {N2} neutrons"
    wrongs = {f"{Z - 4} protons and {N}  neutrons".replace("  ", " "): "Each β decay turns a neutron INTO a proton (Z + 1, N − 1); the α then removes 2 protons and 2 neutrons.",
              f"{Z2} protons and {N - 2} neutrons": "Two β decays each convert one neutron, and the α removes two more: four neutrons fewer in all.",
              f"{Z - 2} protons and {N - 2} neutrons": "That counts only the α decay and ignores the two β decays."}
    opts, key, mis = text_options(rng, correct, wrongs)
    return dict(stem=f"A nucleus has **{Z} protons and {N} neutrons**. It emits two β-particles and then one α-particle. How many protons and neutrons does the final nucleus have?",
                options=opts, key=key, misconceptions=mis, formula="β: n → p (Z+1, N−1); α: Z−2, N−2",
                working=[f"Two β decays: protons {Z} → {Z + 2}, neutrons {N} → {N - 2}", f"One α decay: protons {Z + 2} → {Z2}, neutrons {N - 2} → {N2}",
                         f"Correct answer: **{correct}**", cite("Commonwealth 2025 prelim MCQ 38 and CCHM 2025 prelim MCQ 38")],
                hints=["Deal with the decays one at a time.", "β: a neutron changes into a proton (and an electron leaves).", "α: two protons and two neutrons leave together."])


@template("o26s_half_life_counts", chapter=20, level=3, lo="20h", category=CAT)
def half_life_counts(rng):
    n0, n, T = nice(rng, (9600, 600, 40), (8000, 500, 60), (6400, 400, 24), (4800, 300, 32))
    halves = round(math.log2(n0 / n))
    hl = T / halves
    return calc_q(rng, f"A radioactive source emits **{n0} α-particles per second**. After **{T} hours** the rate has fallen to **{n} per second**. What is the half-life of the source?", hl,
                  [(T / 2, "Halving the time is not it: count how many HALVINGS take {n0} down to {n}."),
                   (T, "In one half-life the rate only halves; here it has fallen by a factor of " + str(n0 // n) + "."),
                   (T / (halves + 1), "Count the halvings carefully: " + " → ".join(str(n0 // 2 ** k) for k in range(halves + 1)) + f" is {halves} half-lives.")],
                  "hours", "number of half-lives = log₂(N₀/N); half-life = total time ÷ number of half-lives",
                  [f"{n0} → " + " → ".join(str(n0 // 2 ** k) for k in range(1, halves + 1)) + f": {halves} half-lives in {T} h",
                   f"half-life = {T} / {halves} = **{fmt(hl)} hours**", cite("HGV 2024 prelim MCQ 40")],
                  ["Keep halving the starting rate until you reach the final rate.", "Count how many halvings that took.", "Divide the total time by that number."])


@template("o26s_atoms_disintegrated", chapter=20, level=3, lo="20h", category=CAT)
def atoms_disintegrated(rng):
    N0, k = nice(rng, (12000, 2), (8000, 3), (16000, 2), (6000, 1))
    left = N0 / 2 ** k
    gone = N0 - left
    return calc_q(rng, f"A sample contains **{N0} atoms** of a radioactive nuclide. After **{k} half-li{'fe' if k == 1 else 'ves'}**, how many of these atoms have decayed?", gone,
                  [(left, "That is the number of atoms REMAINING. The question asks how many have decayed."),
                   (N0 / (2 * k) if k > 1 else N0 / 3, f"After {k} half-lives the fraction left is 1/2^{k}, not 1/(2 × {k})."),
                   (N0, "Not all the atoms decay: half of what is present survives each half-life.")],
                  "atoms", "remaining = N₀ / 2ⁿ; decayed = N₀ − remaining",
                  [f"Remaining = {N0} / 2^{k} = {fmt(left)}", f"Decayed = {N0} − {fmt(left)} = **{fmt(gone)}**", cite("XMSS 2024 prelim MCQ 40")],
                  ["After each half-life, half of the remaining atoms are left.", f"Halve {N0} {k} time{'s' if k > 1 else ''}.", "Subtract what is left from the starting number."], sf=4)


@template("o26s_half_life_background", chapter=20, level=4, lo="20g", category=CAT)
def half_life_background(rng):
    bg, start, end, T = nice(rng, (10, 290, 45, 60), (12, 332, 52, 90), (8, 248, 38, 45), (10, 170, 30, 40))
    a0, a1 = start - bg, end - bg
    halves = round(math.log2(a0 / a1))
    hl = T / halves
    return calc_q(rng, f"A detector near a radioactive source reads **{start} counts per second**. **{T} minutes** later it reads **{end} counts per second**. "
                  f"The background count rate is **{bg} counts per second**. What is the half-life of the source?", hl,
                  [(T / round(math.log2(start / end)) if round(math.log2(start / end)) else T, "The background count must be SUBTRACTED from both readings before comparing them."),
                   (T, f"The corrected rate falls from {a0} to {a1}: that is more than one halving."),
                   (T / (halves + 1), "Count the halvings of the corrected rate: " + " → ".join(str(a0 // 2 ** k) for k in range(halves + 1)) + ".")],
                  "min", "subtract background, then count half-lives",
                  [f"Corrected rates: {start} − {bg} = {a0}; {end} − {bg} = {a1}", f"{a0} → " + " → ".join(str(a0 // 2 ** k) for k in range(1, halves + 1)) + f": {halves} half-lives in {T} min",
                   f"half-life = {T} / {halves} = **{fmt(hl)} min**", cite("BPGHS 2024 prelim MCQ 37")],
                  ["Background radiation is always present and is not from the source: subtract it from every reading.", "Then see how many times the source's own count rate has halved.",
                   "Divide the time by the number of half-lives."])
