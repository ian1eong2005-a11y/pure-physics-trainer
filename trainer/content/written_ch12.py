"""Chapter 12 Light: written-answer questions, two per level (reflection terms, refraction, refractive index, critical angle,
total internal reflection and optical fibres, lens images)."""
from .. import figs2
from ..marker import Pitfall, Point
from .base import written

P = Point
PF = Pitfall

# ---------------------------------------------------------------- L1
written("w12_define_angle_of_incidence", 12, 1, "12a",
        stem="Fig. 1 shows a ray of light striking a plane mirror. State what is meant by the angle of incidence.",
        points=[P("the angle between the incident ray and the normal (at the point of incidence)", ["incident ray and the normal", "between the ray and the normal", "ray and normal", "incident ray normal", "measured from the normal", "to the normal"])],
        pitfalls=[PF(["ray and the mirror", "ray and the surface", "from the mirror", "from the surface"], "The angle is measured from the NORMAL (the line at 90° to the mirror), not from the mirror surface.")],
        model_answer="The angle of incidence is the angle between the incident ray and the normal, the line drawn at right angles to the mirror at the point where the ray strikes it.",
        hints=["Two lines make this angle. One is the incoming ray; what is the other?",
               "The other line is drawn perpendicular to the mirror where the ray hits.",
               "Name both lines in one sentence."],
        keywords="angle between incident ray and normal",
        figure=lambda: figs2.mirror_reflection(35, label_i="i", label_r="r"),
        sample_pass=["The angle between the incident ray and the normal", "it is the angle the incoming ray makes with the normal at the point of incidence"],
        sample_fail=["The angle between the ray and the mirror", "The angle the light turns through"])

written("w12_define_refractive_index", 12, 1, "12e",
        stem="Define the refractive index of a medium in terms of the speed of light.",
        points=[P("the ratio of the speed of light in a vacuum to the speed of light in the medium", ["speed of light in a vacuum", "speed in vacuum", "speed of light in vacuum divided", "vacuum to the speed", "c divided by v", "ratio of the speed"]),
                P("vacuum speed divided by medium speed (vacuum on top)", ["divided by the speed of light in the medium", "to the speed in the medium", "over the speed in the medium", "÷ speed in the medium", "/ speed in the medium", "in the medium"])],
        pitfalls=[PF(["medium divided by", "medium over the", "medium to the speed"], "The ratio is the other way round: vacuum speed ÷ medium speed, so that n is greater than 1.")],
        model_answer="The refractive index of a medium is the ratio of the speed of light in a vacuum to the speed of light in the medium: n = c ÷ v.",
        hints=["The definition compares two speeds of light.",
               "One speed is in a vacuum (the fastest possible); the other is in the medium.",
               "Write the ratio with the vacuum speed on top."],
        keywords="speed of light in vacuum ÷ speed of light in the medium",
        sample_pass=["The speed of light in a vacuum divided by the speed of light in the medium", "n = c / v, the ratio of the speed of light in vacuum to that in the medium"],
        sample_fail=["The speed of light in the medium divided by the speed in a vacuum", "The angle at which light bends"])

# ---------------------------------------------------------------- L2
written("w12_define_critical_angle", 12, 2, "12f",
        stem="State what is meant by the critical angle of a medium.",
        points=[P("the angle of incidence in the (denser) medium", ["angle of incidence", "incident angle", "angle in the glass", "angle in the medium", "angle in the denser"]),
                P("for which the angle of refraction (in air) is 90°, i.e. the refracted ray travels along the boundary", ["90", "ninety", "along the boundary", "along the surface", "grazes", "refraction is 90"])],
        pitfalls=[PF(["angle of reflection is 90"], "It is the angle of REFRACTION that becomes 90°, with the refracted ray running along the boundary.")],
        model_answer="The critical angle is the angle of incidence in the denser medium for which the angle of refraction in the less dense medium is 90°, so that the refracted ray travels along the boundary.",
        hints=["It is a particular angle of incidence, measured inside the denser medium (e.g. glass).",
               "What happens to the refracted ray at this angle? Think about where it goes.",
               "State the angle of incidence condition and what the refracted ray does."],
        keywords="angle of incidence in the denser medium when the angle of refraction is 90°",
        sample_pass=["The angle of incidence in glass for which the angle of refraction is 90 degrees", "the incident angle at which the refracted ray goes along the boundary"],
        sample_fail=["The angle at which light reflects off a mirror", "45 degrees"])

written("w12_two_conditions_tir", 12, 2, "12f",
        stem="State the two conditions needed for total internal reflection to take place.",
        points=[P("light must be travelling from a denser (optically) medium towards a less dense medium, e.g. from glass to air", ["denser to less dense", "denser medium to a less dense", "from glass to air", "from water to air", "optically denser", "higher refractive index to lower", "denser medium into", "towards a less dense"]),
                P("the angle of incidence must be greater than the critical angle", ["greater than the critical angle", "exceeds the critical angle", "more than the critical angle", "larger than the critical angle", "above the critical angle", "bigger than the critical", "i larger than c", "i greater than c", "i more than c", "i bigger than c", "i exceeds c", "i > c", "larger than c", "greater than c", "exceeds c", "above c"])],
        pitfalls=[PF(["less than the critical angle", "smaller than the critical angle"], "The angle of incidence must be GREATER than the critical angle for total internal reflection."),
                  PF(["air to glass", "less dense to denser", "air into glass"], "Light must travel from the DENSER medium towards the less dense one, e.g. glass to air.")],
        model_answer="First, the light must be travelling from an optically denser medium towards a less dense medium, for example from glass towards air. Second, the angle of incidence in the denser medium must be greater than the critical angle.",
        hints=["One condition is about which way the light is travelling between the two media.",
               "The other is about the size of the angle of incidence compared with a special angle.",
               "State both: direction (denser to less dense) and angle (greater than critical)."],
        keywords="denser to less dense medium; angle of incidence > critical angle",
        sample_pass=["Light goes from glass towards air and the angle of incidence is greater than the critical angle", "travelling from a denser to a less dense medium with i larger than c"],
        sample_fail=["Light must hit the surface at exactly 90 degrees", "The glass must be very thick and polished"])

# ---------------------------------------------------------------- L3
written("w12_pencil_looks_bent", 12, 3, "12c",
        stem="A pencil standing in a glass of water appears bent at the water surface. Explain why.",
        points=[P("light from the part of the pencil under water is refracted as it passes from water into air", ["refracted", "refraction", "bends", "changes direction"]),
                P("it bends away from the normal because light speeds up (water is denser than air)", ["away from the normal", "speeds up", "faster in air", "less dense", "denser"]),
                P("the eye assumes light travels in straight lines, so the submerged part appears raised / displaced", ["straight line", "appears to come from", "appears higher", "appears raised", "displaced", "shallower", "image"])],
        min_points=2,
        model_answer="Light from the submerged part of the pencil is refracted as it passes from water into air: it speeds up and bends away from the normal. The eye assumes the light has travelled in a straight line, so the underwater part appears to be higher (nearer the surface) than it really is, making the pencil look bent at the surface.",
        hints=["What happens to light leaving the water on its way to your eye?",
               "Which way does it bend, and why does that fool the eye?",
               "Explain the refraction, its direction, and why the eye is misled."],
        keywords="refraction water to air, away from the normal, eye traces straight lines, part appears raised",
        figure=lambda: figs2.refraction(30, 42, upper="water", lower="air"),
        sample_pass=["Light from the underwater part refracts away from the normal as it leaves the water, and the eye traces it back in a straight line so that part looks raised",
                     "refraction at the water surface makes the submerged part appear higher than it is"],
        sample_fail=["The water pushes the pencil sideways", "Water reflects light like a mirror"])

written("w12_fibre_telecom_advantages", 12, 3, "12g",
        stem="Fig. 1 shows light travelling along an optical fibre. Explain how the light is kept inside the fibre, and give two advantages of optical fibres over copper cables for telecommunications.",
        points=[P("total internal reflection at the glass-air (or core-cladding) boundary because the angle of incidence exceeds the critical angle", ["total internal reflection", "totally internally reflected", "critical angle", "reflected inside", "reflects off the inside"]),
                P("advantage 1: carries much more information / higher data rate / more signals", ["more information", "more data", "more signals", "higher capacity", "bandwidth", "more calls"]),
                P("advantage 2: less signal loss over long distances (fewer repeaters), no electrical interference, thinner and lighter, more secure", ["less loss", "less signal loss", "weaker less", "fewer repeaters", "interference", "thinner", "lighter", "secure", "cheaper material"])],
        min_points=2,
        model_answer="The light strikes the inside surface of the fibre at an angle of incidence greater than the critical angle, so it is totally internally reflected each time and stays inside the glass. Optical fibres can carry far more information than copper cables, lose less signal over long distances so fewer repeaters are needed, and are not affected by electrical interference; they are also thinner and lighter.",
        hints=["What happens to light hitting the inside wall of the glass at a large angle of incidence?",
               "Think about how much data a fibre carries, how far the signal travels before fading, and interference.",
               "Name the reflection effect and give two advantages."],
        keywords="total internal reflection (i > c); more data, less signal loss, no electrical interference",
        figure=lambda: figs2.optical_fibre(),
        sample_pass=["Total internal reflection keeps the light in because the angle of incidence is bigger than the critical angle; fibres carry more data and suffer less signal loss",
                     "light is totally internally reflected at the walls; advantages: no electrical interference and higher capacity"],
        sample_fail=["The fibre is painted black so light cannot escape", "Copper is a better conductor of light"])

# ---------------------------------------------------------------- L4
written("w12_image_between_f_2f", 12, 4, "12k",
        stem="Fig. 1 shows an object placed between F and 2F of a thin converging lens. Describe the image formed, and explain how the ray diagram shows that the image is real.",
        points=[P("the image is real, inverted and magnified", ["real", "inverted", "upside down", "magnified", "larger", "enlarged"]),
                P("it is formed beyond 2F on the other side of the lens", ["beyond 2F", "further than 2F", "other side", "opposite side", "past 2F"]),
                P("real because the refracted rays actually meet (converge) at the image, so it can be formed on a screen", ["actually meet", "rays meet", "rays cross", "converge", "on a screen", "actual rays"])],
        min_points=2,
        model_answer="The image is real, inverted and magnified, and it is formed beyond 2F on the opposite side of the lens from the object. It is real because the refracted rays actually meet at the image position, so the image could be caught on a screen placed there.",
        hints=["Give three characteristics: real or virtual, upright or inverted, magnified or diminished. Then say where it is.",
               "On the diagram, do the rays after the lens really meet, or do they only appear to come from a point?",
               "Describe the image and explain 'real' in terms of the rays meeting."],
        keywords="real, inverted, magnified, beyond 2F; rays actually converge, can be shown on a screen",
        figure=lambda: figs2.lens_rays(4, 6),
        sample_pass=["The image is real, inverted and magnified, beyond 2F on the other side; it is real because the rays actually cross there and could form on a screen",
                     "a magnified inverted real image past 2F, formed where the refracted rays converge"],
        sample_fail=["The image is virtual and upright", "The image is the same size and at F"])

written("w12_endoscope", 12, 4, "12g",
        stem="A doctor uses an endoscope, a bundle of optical fibres, to see inside a patient's stomach. Explain how the endoscope allows the doctor to see the stomach lining.",
        points=[P("light is sent down one bundle of fibres to illuminate the inside of the stomach", ["sent down", "illuminate", "light up", "shine light", "one bundle carries light in", "to the stomach"]),
                P("light reflected from the stomach lining enters a second bundle and is carried back out to the doctor's eye or a camera", ["reflected from the stomach", "reflected light", "carried back", "second bundle", "to the eye", "to a camera", "image is carried"]),
                P("the light stays inside each fibre by repeated total internal reflection, so the fibres can bend round corners", ["total internal reflection", "totally internally reflected", "critical angle", "bend", "flexible", "round corners"])],
        min_points=2,
        model_answer="One bundle of fibres carries light down into the stomach to illuminate the lining. Light reflected from the lining enters a second bundle and is carried back up to the doctor's eyepiece or a camera, each fibre keeping its light by repeated total internal reflection. Because the light stays inside the fibres however they bend, the endoscope can be flexible and reach around corners.",
        hints=["Two things must travel along the endoscope: light going in, and light coming back.",
               "What keeps the light inside each fibre even when the tube bends?",
               "Describe the light in, the light out, and total internal reflection."],
        keywords="light carried in by one bundle; reflected light carried back by another; total internal reflection lets fibres bend",
        sample_pass=["Light is sent down some fibres to light up the stomach and the reflected light travels back up other fibres by total internal reflection to the doctor",
                     "one bundle illuminates the lining, another carries the reflected image out; TIR keeps the light inside even where the tube bends"],
        sample_fail=["The endoscope uses X-rays to see through the stomach wall", "Sound echoes are used to build a picture"])

# ---------------------------------------------------------------- L5
written("w12_claim_tir_any_boundary", 12, 5, "12f",
        stem="A student claims: 'Whenever light inside a glass block reaches the surface, it is totally internally reflected.' Evaluate this claim.",
        points=[P("the claim is wrong / only partly true", ["wrong", "incorrect", "not always", "only if", "not true", "false", "partly"]),
                P("total internal reflection happens only when the angle of incidence is greater than the critical angle (about 42° for glass)", ["greater than the critical angle", "exceeds the critical angle", "above the critical angle", "42", "critical angle"]),
                P("below the critical angle most of the light refracts out into the air (with some partial reflection)", ["refracts out", "refracted", "passes out", "escapes", "leaves the glass", "partial reflection", "partially reflected"])],
        min_points=2,
        model_answer="The claim is wrong. Light inside glass is totally internally reflected only when it meets the surface at an angle of incidence greater than the critical angle (about 42° for glass). At smaller angles most of the light is refracted out into the air, bending away from the normal, and only a little is reflected.",
        hints=["Is there a condition on the angle of incidence for total internal reflection?",
               "What happens to light that meets the surface at a small angle of incidence?",
               "Judge the claim, give the condition, and say what happens otherwise."],
        keywords="only if i > critical angle; otherwise light refracts out (partial reflection)",
        figure=lambda: figs2.tir(30, 42),
        sample_pass=["The claim is false: total internal reflection only occurs when the angle of incidence is greater than the critical angle; otherwise the light refracts out of the glass",
                     "not always, it needs i above about 42 degrees for glass, or the light mostly passes out into the air"],
        sample_fail=["The claim is right because glass is shiny", "Light can never leave a glass block"])

written("w12_design_periscope_or_fibre", 12, 5, "12f",
        stem="Glass prisms are used instead of mirrors to turn light through 90° in good-quality binoculars and periscopes. Suggest why prisms using total internal reflection are preferred to ordinary mirrors.",
        points=[P("total internal reflection reflects all of the light (no energy absorbed by a silver coating), so the image is brighter", ["all of the light", "100", "brighter", "no loss", "none is lost", "completely reflected", "totally reflected"]),
                P("a mirror's silvering can tarnish / wear away, and its glass front gives multiple faint images; a prism needs no coating and gives a single sharp image", ["tarnish", "wear", "scratch", "peel", "coating", "multiple images", "double image", "sharper", "single image", "no silvering"]),
                P("the light must strike the prism face at an angle greater than the critical angle (45° > 42° for glass)", ["45", "critical angle", "greater than the critical"])],
        min_points=2,
        model_answer="In a prism the light is totally internally reflected, so all of it is reflected and the image is brighter; an ordinary mirror absorbs some light in its silvered coating and the glass front produces faint extra images. The silvering of a mirror can also tarnish or wear away, whereas a prism has no coating to damage. The light meets the prism face at 45°, which is greater than the critical angle of glass (about 42°), so total internal reflection takes place.",
        hints=["How much of the light does total internal reflection reflect, compared with a silvered mirror?",
               "What can go wrong with the silver coating on a mirror over time, and what about reflections from the mirror's glass front?",
               "Give two advantages and mention the critical-angle condition."],
        keywords="TIR reflects all the light (brighter); no silvering to tarnish, no multiple images; 45° > critical angle 42°",
        sample_pass=["Total internal reflection reflects all the light so the image is brighter, and there is no silver coating to tarnish or give multiple images",
                     "prisms give a brighter, single sharp image because none of the light is absorbed and there is no coating to wear away; 45 degrees exceeds the critical angle"],
        sample_fail=["Prisms are cheaper because they are made of plastic", "Mirrors cannot reflect light through 90 degrees"])
