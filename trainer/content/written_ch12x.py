"""Chapter 12 Light written-answer bank extension: fills each level to at least 10 with every LO at least twice."""
from ..marker import Pitfall, Point
from .base import written

P = Point
PF = Pitfall

# ---------------------------------------------------------------- L1
written("w12x_define_normal", 12, 1, "12a",
        stem="State what is meant by the normal at the point where a ray meets a surface.",
        points=[P("a line at right angles (perpendicular / 90°) to the surface", ["right angles", "perpendicular", "90", "90°"]),
                P("drawn at the point where the ray meets the surface (point of incidence)", ["point of incidence", "where the ray", "at the point", "meets the surface", "strikes"])],
        model_answer="The normal is a line drawn at right angles (perpendicular) to the surface at the point where the ray meets it (the point of incidence).",
        hints=["It is an imaginary line.", "At what angle to the surface?", "Where is it drawn?"],
        keywords="perpendicular to surface; at point of incidence",
        sample_pass=["A line perpendicular to the surface at the point of incidence", "a line at 90° to the mirror where the ray strikes it"],
        sample_fail=["A line along the mirror", "The reflected ray"])

written("w12x_n_speed_meaning", 12, 1, "12e",
        stem="Glass has a refractive index of 1.5. State what this tells you about the speed of light in glass.",
        points=[P("light travels 1.5 times slower in glass than in a vacuum (air)", ["1.5 times slower", "slower", "slows"]),
                P("v = c ÷ 1.5 = 2.0 × 10⁸ m/s", ["2.0 × 10", "2 × 10", "2.0 x 10", "200 000 000", "c / 1.5", "c ÷ 1.5"])],
        pitfalls=[PF(["faster"], "Light is SLOWER in glass: v = c ÷ n.")],
        min_points=1,
        model_answer="Light travels 1.5 times slower in glass than in a vacuum: its speed is c ÷ 1.5 = 2.0 × 10⁸ m/s.",
        hints=["n = c ÷ v.", "What does n = 1.5 mean?", "Find v."],
        keywords="1.5 times slower; v = 2.0 × 10⁸ m/s",
        sample_pass=["Light is 1.5 times slower in glass, 2.0 × 10⁸ m/s", "its speed is c ÷ 1.5, which is slower than in air"],
        sample_fail=["Light is 1.5 times faster in glass", "Glass is 1.5 cm thick"])

written("w12x_law_reflection", 12, 1, "12b",
        stem="State the two laws of reflection.",
        points=[P("the angle of incidence equals the angle of reflection", ["angle of incidence equals the angle of reflection", "angle of incidence = angle of reflection", "i = r", "equal"]),
                P("the incident ray, reflected ray and normal lie in the same plane", ["same plane", "one plane"])],
        model_answer="The angle of incidence equals the angle of reflection; and the incident ray, the reflected ray and the normal all lie in the same plane.",
        hints=["One law is about angles.", "The other is about a plane.", "State both."],
        keywords="i = r; same plane",
        sample_pass=["The angle of incidence equals the angle of reflection and the rays and normal are in the same plane", "i = r, and the incident ray, reflected ray and normal lie in one plane"],
        sample_fail=["Light bends towards the normal", "The image is virtual"])

written("w12x_mirror_image", 12, 1, "12b",
        stem="State three characteristics of the image formed by a plane mirror.",
        points=[P("virtual", ["virtual"]),
                P("upright (erect)", ["upright", "erect", "the right way up"]),
                P("same size / same distance behind / laterally inverted", ["same size", "same distance", "laterally inverted", "left and right", "as far behind"])],
        min_points=3,
        model_answer="The image is virtual, upright, the same size as the object, as far behind the mirror as the object is in front, and laterally inverted.",
        hints=["Can it be shown on a screen?", "Which way up is it?", "Size and distance?"],
        keywords="virtual; upright; same size, same distance; laterally inverted",
        sample_pass=["virtual, upright and the same size", "upright, virtual, laterally inverted"],
        sample_fail=["real, inverted, magnified", "real and smaller"])

written("w12x_define_focal_length", 12, 1, "12i",
        stem="Define the focal length of a converging lens.",
        points=[P("the distance between the optical centre and the principal focus", ["optical centre", "centre of the lens", "principal focus", "focal point"])],
        model_answer="The focal length is the distance between the optical centre of the lens and its principal focus.",
        hints=["It is a distance.", "From where?", "To where?"],
        keywords="optical centre to principal focus",
        sample_pass=["The distance from the optical centre to the principal focus", "distance between the centre of the lens and the focal point"],
        sample_fail=["The distance from the object to the image", "The thickness of the lens"])

written("w12x_define_principal_focus", 12, 1, "12i",
        stem="State what is meant by the principal focus of a converging lens.",
        points=[P("the point where rays parallel to the principal axis converge (meet) after refraction", ["parallel", "meet", "converge", "come together", "focus"]),
                P("on the principal axis", ["principal axis", "on the axis"])],
        model_answer="The principal focus is the point on the principal axis where rays parallel to the axis converge (meet) after passing through the lens.",
        hints=["Think of a parallel beam.", "What happens after the lens?", "Where do the rays meet?"],
        keywords="parallel rays converge; on the principal axis",
        sample_pass=["The point on the principal axis where parallel rays meet after the lens", "rays parallel to the principal axis converge at this point"],
        sample_fail=["The centre of the lens", "Where the object is placed"])

written("w12x_bend_air_glass", 12, 1, "12c",
        stem="A ray of light enters a glass block from air at an angle. State which way it bends and why.",
        points=[P("it bends towards the normal", ["towards the normal"]),
                P("because it slows down in the glass (glass is optically denser)", ["slows down", "slower", "denser", "speed decreases"])],
        pitfalls=[PF(["away from the normal"], "Entering a denser medium, light bends TOWARDS the normal.")],
        model_answer="It bends towards the normal, because it slows down on entering the optically denser glass.",
        hints=["Is glass optically denser than air?", "What happens to the speed?", "Which way does it bend?"],
        keywords="towards normal; slows down",
        sample_pass=["Towards the normal because it slows down in the glass", "it bends towards the normal since glass is denser"],
        sample_fail=["Away from the normal", "It does not bend"])

written("w12x_bend_glass_air", 12, 1, "12c",
        stem="A ray of light leaves a glass block into air at an angle. State which way it bends and why.",
        points=[P("it bends away from the normal", ["away from the normal"]),
                P("because it speeds up in the air (air is less dense)", ["speeds up", "faster", "less dense", "speed increases"])],
        pitfalls=[PF(["towards the normal"], "Leaving glass for air, light bends AWAY from the normal.")],
        model_answer="It bends away from the normal, because it speeds up on entering the less dense air.",
        hints=["Is air optically less dense?", "What happens to the speed?", "Which way does it bend?"],
        keywords="away from normal; speeds up",
        sample_pass=["Away from the normal because it speeds up in air", "it bends away from the normal since air is less dense"],
        sample_fail=["Towards the normal", "It is absorbed"])

# ---------------------------------------------------------------- L2
written("w12x_mirror_ray_diagram", 12, 2, "12b",
        stem="Describe how to locate the image of a point object in a plane mirror using a ray diagram.",
        points=[P("draw two rays from the object to the mirror and reflect them using i = r", ["two rays", "reflect", "i = r", "law of reflection", "angle of incidence"]),
                P("extend the reflected rays backwards behind the mirror (dashed)", ["extend", "backwards", "behind the mirror", "dashed", "trace back"]),
                P("the image is where the extended rays meet", ["meet", "cross", "intersect"])],
        min_points=2,
        model_answer="Draw two rays from the object to the mirror and reflect each so that the angle of reflection equals the angle of incidence. Extend the reflected rays backwards behind the mirror as dashed lines; the image is where they meet.",
        hints=["How many rays are needed?", "How is each reflected?", "Where is the image?"],
        keywords="two rays, i = r; extend back; meet",
        sample_pass=["Draw two rays, reflect them with i = r, extend them behind the mirror; the image is where they meet", "trace the reflected rays back as dashed lines and find where they cross"],
        sample_fail=["Measure the object", "Draw one ray straight through the mirror"])

written("w12x_mirror_same_distance", 12, 2, "12b",
        stem="A boy stands 2.0 m in front of a plane mirror and walks 0.5 m towards it. State the new distance between the boy and his image, and explain.",
        points=[P("3.0 m", ["3.0", "3 m"]),
                P("the image is always as far behind the mirror as the object is in front (1.5 m each)", ["as far behind", "same distance", "1.5", "behind the mirror"])],
        model_answer="He is now 1.5 m from the mirror, and his image is also 1.5 m behind it, so the boy and his image are 3.0 m apart.",
        hints=["How far is he from the mirror now?", "Where is the image?", "Add the distances."],
        keywords="3.0 m; image as far behind as object in front",
        sample_pass=["3.0 m, because the image is the same distance behind the mirror, 1.5 m", "1.5 m in front and 1.5 m behind, so 3 m"],
        sample_fail=["4.0 m", "1.5 m"])

written("w12x_refraction_speed_reason", 12, 2, "12c",
        stem="Explain why light changes direction when it passes at an angle from air into water.",
        points=[P("light slows down in water", ["slows down", "slower", "speed decreases", "changes speed"]),
                P("the part of the wavefront entering first slows first, so the ray bends (towards the normal)", ["wavefront", "one side", "part of the beam", "first", "bends", "towards the normal"])],
        model_answer="Light slows down in water. When a beam meets the surface at an angle, the side of the wavefront that enters the water first slows down first, so the beam changes direction, bending towards the normal.",
        hints=["What happens to the speed?", "Which part of the beam enters first?", "How does that turn the beam?"],
        keywords="changes speed; one side slows first → bends",
        sample_pass=["It slows down in water and one side of the wavefront slows first, so it bends towards the normal", "the speed decreases, so the beam bends"],
        sample_fail=["Water attracts light", "Light reflects from the water"])

written("w12x_apparent_depth_written", 12, 2, "12c",
        stem="Explain why a swimming pool looks shallower than it really is.",
        points=[P("light from the bottom refracts away from the normal as it leaves the water", ["away from the normal", "refract", "bends"]),
                P("the eye traces the rays back in straight lines to a point higher than the real bottom", ["straight lines", "traces back", "appears higher", "higher", "virtual image"])],
        model_answer="Light from the bottom of the pool is refracted away from the normal as it leaves the water. The eye assumes light travels in straight lines, so it traces the rays back to a point higher than the real bottom; the pool looks shallower.",
        hints=["What happens to light leaving the water?", "How does the eye interpret it?", "Where does the bottom seem to be?"],
        keywords="refraction away from normal; eye traces back → appears higher",
        sample_pass=["Light bends away from the normal leaving the water and the eye traces it back in straight lines to a higher point", "refraction bends the light away from the normal, so the bottom appears higher"],
        sample_fail=["The water magnifies the pool", "Light reflects from the bottom"])

written("w12x_snell_state", 12, 2, "12d",
        stem="State Snell's law and write the equation for the refractive index in terms of angles.",
        points=[P("the ratio sin i ÷ sin r is constant for two given media", ["sin i / sin r", "sin i ÷ sin r", "constant", "ratio"]),
                P("n = sin i ÷ sin r", ["n = sin i", "n ="])],
        model_answer="Snell's law: for light passing between two given media, sin i ÷ sin r is a constant. This constant is the refractive index: n = sin i ÷ sin r.",
        hints=["It involves sines.", "What stays constant?", "Write n."],
        keywords="sin i ÷ sin r constant; n = sin i ÷ sin r",
        sample_pass=["sin i / sin r is constant, and n = sin i / sin r", "the ratio of sin i to sin r is constant; n = sin i ÷ sin r"],
        sample_fail=["i = r", "n = c × v"])

written("w12x_n_from_angles_written", 12, 2, "12d",
        stem="A ray enters a block from air at an angle of incidence of 40° and is refracted at 25°. Calculate the refractive index of the block, showing your working.",
        points=[P("n = sin 40° ÷ sin 25°", ["sin 40", "sin i / sin r", "sin i ÷ sin r"]),
                P("n = 1.52 (1.5)", ["1.52", "1.5"])],
        model_answer="n = sin i ÷ sin r = sin 40° ÷ sin 25° = 0.643 ÷ 0.423 = 1.52.",
        hints=["Use Snell's law.", "Take sines of both angles.", "Divide."],
        keywords="n = sin 40° ÷ sin 25° = 1.52",
        sample_pass=["n = sin 40 / sin 25 = 1.52", "sin i ÷ sin r = 0.643 ÷ 0.423 = 1.5"],
        sample_fail=["n = 40 ÷ 25 = 1.6", "n = 0.62"])

written("w12x_fibre_how", 12, 2, "12g",
        stem="Describe how light travels along an optical fibre.",
        points=[P("light enters one end and hits the inner surface at an angle greater than the critical angle", ["greater than the critical angle", "more than the critical angle", "exceeds the critical angle", "critical angle"]),
                P("it is totally internally reflected repeatedly along the fibre", ["total internal reflection", "totally internally reflected", "tir"])],
        model_answer="Light enters one end and meets the boundary of the core at an angle greater than the critical angle, so it is totally internally reflected; this happens again and again along the fibre until the light leaves the far end.",
        hints=["What happens at the boundary?", "Compare the angle with the critical angle.", "Name the process."],
        keywords="i > c; repeated total internal reflection",
        sample_pass=["The light meets the sides at more than the critical angle and is totally internally reflected many times", "repeated total internal reflection keeps the light inside, as it hits the sides above the critical angle"],
        sample_fail=["It is refracted out of the sides", "A mirror coating reflects it"])

written("w12x_fibre_uses_two", 12, 2, "12g",
        stem="State two uses of optical fibres.",
        points=[P("one use: telecommunications / internet / endoscopes / decorative lights", ["telecommunication", "internet", "broadband", "telephone", "endoscope", "medical", "decorative", "cable"]),
                P("a second, different use", ["telecommunication", "internet", "broadband", "telephone", "endoscope", "medical", "decorative", "cable", "tv"])],
        min_points=2,
        model_answer="Carrying telephone and internet signals (telecommunications), and in endoscopes to see inside the body.",
        hints=["Think of communication.", "Think of medicine.", "Two uses."],
        keywords="telecommunications; endoscopes",
        sample_pass=["Telecommunications and endoscopes", "internet cables and medical endoscopes"],
        sample_fail=["Cooking and heating", "X-ray photography"])

# ---------------------------------------------------------------- L3
written("w12x_pencil_bent_l3", 12, 3, "12c",
        stem="Explain why a straight ruler dipped at an angle into water appears to bend at the surface.",
        points=[P("light from the underwater part refracts (bends away from the normal) at the surface", ["refract", "bends away", "away from the normal"]),
                P("the eye sees the underwater part higher than it is, so the ruler looks bent", ["higher", "appears", "traces back", "straight lines", "shallower"])],
        model_answer="Light from the underwater part of the ruler is refracted away from the normal as it leaves the water. The eye traces the rays back in straight lines, so the underwater part appears higher than it is, and the ruler appears bent at the surface.",
        hints=["What happens to light leaving the water?", "Where does the eye think the ruler is?", "Why does it look bent?"],
        keywords="refraction at surface; underwater part appears higher",
        sample_pass=["Light refracts away from the normal at the surface, so the underwater part appears higher", "the eye traces refracted rays back in straight lines, making the ruler look bent"],
        sample_fail=["The water bends the ruler", "Light reflects off the ruler"])

written("w12x_fibre_vs_copper", 12, 3, "12g",
        stem="Give two advantages of optical fibres over copper cables for carrying telephone signals.",
        points=[P("can carry much more information (data)", ["more information", "more data", "more signals", "higher capacity", "more calls"]),
                P("less signal loss / no electrical interference / lighter / cheaper / more secure", ["less loss", "less signal loss", "interference", "lighter", "cheaper", "secure", "thinner"])],
        min_points=2,
        model_answer="Optical fibres can carry far more information at once, and they suffer less signal loss and no electrical interference (they are also lighter and more secure).",
        hints=["Compare the amount of data.", "Compare signal quality.", "Two advantages."],
        keywords="more data; less loss/no interference/lighter",
        sample_pass=["They carry more information and have less signal loss", "more data, lighter and no electrical interference"],
        sample_fail=["They conduct electricity better", "They are made of metal"])

written("w12x_tir_conditions_explain", 12, 3, "12f",
        stem="Light travels inside a glass block towards the glass–air surface. Describe what happens as the angle of incidence is gradually increased.",
        points=[P("at small angles most light refracts out, bending away from the normal (some reflects)", ["refract", "bends away", "most light", "leaves"]),
                P("at the critical angle the refracted ray travels along the surface (r = 90°)", ["critical angle", "along the surface", "90"]),
                P("above the critical angle all the light is totally internally reflected", ["total internal reflection", "totally internally reflected", "tir", "all the light"])],
        min_points=2,
        model_answer="At small angles most light refracts out into the air, bending away from the normal, with a weak reflection. At the critical angle the refracted ray grazes along the surface (r = 90°). Above the critical angle all the light is totally internally reflected.",
        hints=["Small angles?", "At the critical angle?", "Beyond it?"],
        keywords="refraction → grazing at c → TIR above c",
        sample_pass=["It refracts out at first, at the critical angle it goes along the surface, then above it is totally internally reflected", "above the critical angle there is total internal reflection"],
        sample_fail=["It always refracts", "It reflects at all angles"])

written("w12x_critical_from_n_written", 12, 3, "12f",
        stem="A plastic has a refractive index of 1.49. Calculate its critical angle, showing your working.",
        points=[P("sin c = 1 ÷ n = 1 ÷ 1.49", ["1 / 1.49", "1 ÷ 1.49", "sin c = 1", "0.671"]),
                P("c = 42°", ["42", "42°", "42 degrees"])],
        model_answer="sin c = 1 ÷ n = 1 ÷ 1.49 = 0.671, so c = 42°.",
        hints=["sin c = 1 ÷ n.", "Calculate 1 ÷ 1.49.", "Take sin⁻¹."],
        keywords="sin c = 1/1.49; c = 42°",
        sample_pass=["sin c = 1 / 1.49 = 0.671 so c = 42°", "sin c = 1 / 1.49 so c = 42 degrees"],
        sample_fail=["c = 1.49°", "c = 67°"])

written("w12x_magnifier_use", 12, 3, "12k",
        stem="Explain where an object must be placed to use a converging lens as a magnifying glass, and describe the image.",
        points=[P("closer to the lens than the principal focus (between F and the lens)", ["closer than", "inside f", "less than the focal length", "between f and the lens", "within the focal length"]),
                P("the image is virtual, upright and magnified", ["virtual", "upright", "magnified", "enlarged"])],
        model_answer="The object must be placed closer to the lens than the principal focus (less than one focal length away). The image is virtual, upright and magnified, on the same side as the object.",
        hints=["Where must the object be relative to F?", "Can the image be projected?", "Describe it."],
        keywords="object inside F; virtual, upright, magnified",
        sample_pass=["Closer than the focal length; the image is virtual, upright and magnified", "inside F, giving an upright, enlarged virtual image"],
        sample_fail=["Beyond 2F; real image", "At F"])

written("w12x_camera_image_written", 12, 3, "12k",
        stem="A camera lens forms an image of a distant tree on the sensor. Describe the image and state where it forms.",
        points=[P("real, inverted and diminished (smaller)", ["real", "inverted", "diminished", "smaller"]),
                P("between F and 2F on the other side of the lens (close to F for a very distant object)", ["between f and 2f", "near f", "close to f", "at f", "beyond f"])],
        model_answer="The image is real, inverted and diminished, and it forms on the other side of the lens between F and 2F, close to F for a very distant object.",
        hints=["Where is the tree compared with 2F?", "What kind of image forms?", "Where?"],
        keywords="real, inverted, diminished; between F and 2F",
        sample_pass=["Real, inverted and smaller, between F and 2F", "an inverted, diminished real image near F"],
        sample_fail=["Virtual and upright", "Magnified, at 2F"])

written("w12x_n_def_speed_l3", 12, 3, "12e",
        stem="Light travels at 2.25 × 10⁸ m/s in water. Calculate the refractive index of water and explain what it means.",
        points=[P("n = c ÷ v = 3.0 × 10⁸ ÷ 2.25 × 10⁸", ["c / v", "c ÷ v", "3.0 × 10", "2.25"]),
                P("n = 1.33", ["1.33"]),
                P("light is 1.33 times slower in water than in a vacuum", ["slower", "times"])],
        min_points=2,
        model_answer="n = c ÷ v = 3.0 × 10⁸ ÷ 2.25 × 10⁸ = 1.33. This means light travels 1.33 times slower in water than in a vacuum.",
        hints=["n = c ÷ v.", "Divide.", "What does the number mean?"],
        keywords="n = c ÷ v = 1.33; 1.33 times slower",
        sample_pass=["n = c ÷ v = 1.33, so light is 1.33 times slower in water", "3.0 × 10⁸ / 2.25 × 10⁸ = 1.33"],
        sample_fail=["n = 0.75", "n = 2.25"])

written("w12x_wavelength_change", 12, 3, "12e",
        stem="Light passes from air into glass. State and explain what happens to its frequency, speed and wavelength.",
        points=[P("frequency stays the same", ["frequency stays", "same frequency", "frequency is unchanged", "frequency does not change"]),
                P("speed decreases", ["speed decreases", "slows", "slower"]),
                P("wavelength decreases (λ = v ÷ f)", ["wavelength decreases", "shorter wavelength", "wavelength is shorter"])],
        min_points=2,
        model_answer="The frequency stays the same, as it is set by the source. The speed decreases in glass, so from v = f λ the wavelength decreases.",
        hints=["What is set by the source?", "Does the speed change?", "Use v = f λ."],
        keywords="f same; v decreases; λ decreases",
        sample_pass=["The frequency stays the same, the speed decreases and so the wavelength decreases", "same frequency, slower, shorter wavelength"],
        sample_fail=["The frequency decreases", "Everything increases"])

# ---------------------------------------------------------------- L4
written("w12x_endoscope_coherent", 12, 4, "12g",
        stem="An endoscope contains two bundles of optical fibres. Explain the purpose of each bundle.",
        points=[P("one bundle carries light into the body to illuminate the area", ["into the body", "illuminate", "light in", "light up"]),
                P("the other carries the image (reflected light) back to the eye or camera", ["image", "back", "reflected light", "to the eye", "camera"]),
                P("light stays in each fibre by total internal reflection", ["total internal reflection", "tir"])],
        min_points=2,
        model_answer="One bundle carries light into the body to illuminate the area being examined. The other bundle carries the reflected light, forming an image, back to the doctor's eyepiece or camera. In both, light stays inside the fibres by total internal reflection.",
        hints=["How does light get inside the body?", "How does the image get out?", "What keeps light in the fibres?"],
        keywords="one bundle: light in; other: image out; TIR",
        sample_pass=["One bundle carries light into the body and the other carries the image back by total internal reflection", "light goes in to illuminate the stomach and the reflected light comes back to the camera"],
        sample_fail=["Both carry X-rays", "One heats the body"])

written("w12x_projector_explain", 12, 4, "12k",
        stem="Explain where the slide must be placed in a projector and why it must be put in upside down.",
        points=[P("between F and 2F of the lens", ["between f and 2f"]),
                P("so the image is real and magnified on a distant screen", ["real", "magnified", "enlarged", "screen"]),
                P("the image is inverted, so the slide is put in upside down to give an upright picture", ["inverted", "upside down", "upright picture"])],
        min_points=2,
        model_answer="The slide is placed between F and 2F of the lens, so a real, magnified image forms on a distant screen. This image is inverted, so the slide is put in upside down to give an upright picture.",
        hints=["Where must the object be for a magnified real image?", "Which way up is the image?", "So how is the slide loaded?"],
        keywords="between F and 2F; real, magnified; inverted → slide upside down",
        sample_pass=["Between F and 2F to get a real magnified image; it is inverted so the slide goes in upside down", "the image is real, enlarged and inverted, so put the slide upside down"],
        sample_fail=["Inside F; virtual image", "At 2F; same-size image"])

written("w12x_snell_graph", 12, 4, "12d",
        stem="A student measures angles of refraction for several angles of incidence. Explain how a graph can be used to find the refractive index accurately.",
        points=[P("plot sin i against sin r", ["sin i against sin r", "sin i vs sin r", "sin i on the y", "sin i and sin r"]),
                P("draw a best-fit straight line through the origin", ["best-fit", "best fit", "straight line", "through the origin"]),
                P("the gradient equals the refractive index", ["gradient"])],
        min_points=2,
        model_answer="Plot sin i (y-axis) against sin r (x-axis) for all the readings and draw the best-fit straight line through the origin. The gradient of the line equals the refractive index n; using many readings reduces random error.",
        hints=["Which quantities give a straight line?", "What is the shape?", "What does the gradient give?"],
        keywords="sin i vs sin r; best-fit line through origin; gradient = n",
        sample_pass=["Plot sin i against sin r, draw a best-fit straight line and the gradient is n", "a straight line graph of sin i vs sin r through the origin; gradient = refractive index"],
        sample_fail=["Plot i against time", "Average the angles"])

written("w12x_snell_error", 12, 4, "12d",
        stem="A student finds n for a glass block using only one ray at a small angle of incidence. Suggest two ways to make the result more reliable.",
        points=[P("use several (larger) angles of incidence / repeat readings", ["several", "many", "repeat", "larger angles", "different angles", "range of angles"]),
                P("plot sin i against sin r and take the gradient / average the results", ["gradient", "graph", "average", "mean"]),
                P("use a thin ray (ray box with narrow slit) and mark ray positions far apart", ["thin ray", "narrow", "far apart", "pins", "sharp pencil"])],
        min_points=2,
        model_answer="Measure r for several, larger angles of incidence (small angles give large percentage errors), and plot sin i against sin r, taking the gradient. Also use a thin ray and mark points far apart along each ray to draw the lines accurately.",
        hints=["Is one reading enough?", "Are small angles easy to measure accurately?", "How can the rays be drawn more accurately?"],
        keywords="many/larger angles; graph gradient or average; thin ray, points far apart",
        sample_pass=["Use several larger angles and plot a graph of sin i against sin r", "repeat with different angles and average; use a narrow ray"],
        sample_fail=["Use a thicker block only", "Turn off the lights"])

written("w12x_ray_diagram_steps", 12, 4, "12j",
        stem="Describe how to draw a ray diagram to find the position of the image formed by a converging lens.",
        points=[P("draw a ray from the top of the object parallel to the axis, refracted through F", ["parallel to the axis", "parallel", "through f"]),
                P("draw a ray from the top of the object through the optical centre, undeviated", ["optical centre", "centre of the lens", "straight through", "undeviated"]),
                P("the image (top) is where the rays meet", ["meet", "cross", "intersect"])],
        min_points=2,
        model_answer="From the top of the object, draw one ray parallel to the principal axis, which is refracted through the principal focus F on the other side, and another ray through the optical centre, which passes straight through. The top of the image is where these rays meet.",
        hints=["Which ray is parallel to the axis?", "Which ray is not bent?", "Where is the image?"],
        keywords="parallel ray → F; ray through centre undeviated; meet",
        sample_pass=["Draw a ray parallel to the axis that passes through F, and a ray through the optical centre; the image is where they cross", "one ray through the centre of the lens goes straight, one parallel ray goes through F; they meet at the image"],
        sample_fail=["Draw one ray through the lens", "Measure the object"])

written("w12x_ray_diagram_nature", 12, 4, "12j",
        stem="Explain how a ray diagram shows whether the image formed by a converging lens is real or virtual.",
        points=[P("real: the refracted rays actually meet (on the far side of the lens)", ["actually meet", "real rays meet", "rays cross", "rays meet"]),
                P("virtual: the rays diverge and only appear to meet when traced back (dashed lines)", ["appear to meet", "traced back", "dashed", "diverge", "extended backwards"])],
        model_answer="If the refracted rays actually meet on the far side of the lens, the image is real and could be formed on a screen. If the rays diverge after the lens and only appear to come from a point when traced back (dashed lines), the image is virtual.",
        hints=["Do the rays actually meet?", "Or do they spread out?", "Link to real/virtual."],
        keywords="real: rays meet; virtual: rays appear to meet when traced back",
        sample_pass=["A real image is where the rays actually meet; a virtual image is where they appear to meet when traced back", "if the rays cross it is real, if they diverge and are extended backwards it is virtual"],
        sample_fail=["Real images are upright", "Virtual images are on screens"])

written("w12x_tir_fibre_bend", 12, 4, "12f",
        stem="Explain why an optical fibre can carry light around gentle bends but loses light at very sharp bends.",
        points=[P("at gentle bends the angle of incidence at the boundary stays greater than the critical angle, so TIR continues", ["greater than the critical angle", "more than the critical angle", "above the critical angle", "tir continues", "still totally internally reflected"]),
                P("at sharp bends the angle of incidence falls below the critical angle, so some light refracts out", ["less than the critical angle", "below the critical angle", "refracts out", "escapes", "leaks"])],
        model_answer="At gentle bends, the light still meets the core boundary at angles greater than the critical angle, so total internal reflection continues. At very sharp bends, the angle of incidence can fall below the critical angle, so some light is refracted out and lost.",
        hints=["What must be true for TIR?", "What does a sharp bend do to the angle?", "What happens to the light?"],
        keywords="gentle: i > c, TIR; sharp: i < c, light escapes",
        sample_pass=["At gentle bends the angle stays above the critical angle, but at sharp bends it falls below it and light escapes", "at gentle bends the angle stays above the critical angle, but sharp bends make i less than the critical angle so the light refracts out"],
        sample_fail=["Light cannot go round bends", "Sharp bends make the fibre longer"])

written("w12x_tir_prism_binoculars", 12, 4, "12f",
        stem="Explain how a 45° glass prism turns light through 90° in a periscope, and why the glass must have a critical angle less than 45°.",
        points=[P("light enters one face along the normal and meets the long face at 45°", ["45", "45°", "along the normal", "meets the long face", "hypotenuse"]),
                P("if 45° is greater than the critical angle, the light is totally internally reflected", ["greater than the critical angle", "more than the critical angle", "total internal reflection", "totally internally reflected"]),
                P("the light leaves the other face along the normal, turned through 90°", ["90", "90°", "turned", "leaves"])],
        min_points=2,
        model_answer="Light enters one short face along the normal and meets the long face at 45°. Because 45° is greater than the critical angle of the glass (about 42°), it is totally internally reflected, and it leaves through the other short face along the normal, turned through 90°.",
        hints=["At what angle does the light meet the long face?", "What condition gives TIR?", "How much is the light turned?"],
        keywords="meets long face at 45°; 45° > c → TIR; turned 90°",
        sample_pass=["The light hits the long face at 45°, which is greater than the critical angle, so it is totally internally reflected through 90°", "45 is more than the critical angle so there is total internal reflection"],
        sample_fail=["The prism refracts the light by 90°", "Mirrors inside the prism reflect it"])

# ---------------------------------------------------------------- L5
written("w12x_eval_fibre_copper_claim", 12, 5, "12g",
        stem="A student says optical fibres work because light reflects off a mirror coating inside the fibre. Evaluate this and explain how fibres really work.",
        points=[P("the claim is wrong: there is no mirror coating", ["wrong", "no mirror", "incorrect", "not a mirror"]),
                P("light is kept in by total internal reflection at the core–cladding boundary", ["total internal reflection", "tir", "cladding"]),
                P("because the light meets the boundary at angles greater than the critical angle (core has higher n)", ["greater than the critical angle", "more than the critical angle", "higher refractive index", "critical angle"])],
        min_points=2,
        model_answer="The claim is wrong: there is no mirror coating. Light stays inside by total internal reflection at the boundary between the core and the cladding, which has a lower refractive index; the light meets this boundary at angles greater than the critical angle.",
        hints=["Is there a mirror?", "What process keeps light inside?", "What condition is needed?"],
        keywords="wrong; TIR at core–cladding; i > c",
        sample_pass=["Wrong, there is no mirror; light is totally internally reflected at the cladding because it hits it at more than the critical angle", "not a mirror: total internal reflection keeps the light inside"],
        sample_fail=["Correct, fibres have mirrors", "Light is absorbed and re-emitted"])

written("w12x_eval_fibre_medicine", 12, 5, "12g",
        stem="Evaluate the use of an endoscope compared with surgery for examining a patient's stomach.",
        points=[P("advantage: only a small opening (or mouth), so less pain, risk and recovery time", ["less pain", "smaller", "no large cut", "less risk", "recovery", "less invasive", "keyhole"]),
                P("light and images are carried by optical fibres using total internal reflection", ["total internal reflection", "optical fibre", "fibres"]),
                P("limitation: limited view / some discomfort / cannot treat everything", ["limited", "discomfort", "cannot", "only", "small area"])],
        min_points=2,
        model_answer="An endoscope can be passed in through the mouth or a tiny cut, so there is less pain, less risk of infection and a quicker recovery than surgery. Optical fibres carry light in and the image out by total internal reflection. However, the view is limited and it can be uncomfortable, and not every problem can be treated this way.",
        hints=["What is the main advantage?", "How does it work?", "Any limitation?"],
        keywords="less invasive; fibres by TIR; limited view",
        sample_pass=["It is less invasive with quicker recovery; the fibres carry light by total internal reflection, but the view is limited", "less pain and risk than surgery because only a small opening is needed"],
        sample_fail=["It uses X-rays", "It is always worse"])

written("w12x_eval_image_claim", 12, 5, "12k",
        stem="A student says: 'A converging lens always forms an upside-down image.' Evaluate this statement.",
        points=[P("the statement is wrong", ["wrong", "not always", "incorrect", "not true"]),
                P("objects beyond F give real, inverted images", ["beyond f", "real", "inverted"]),
                P("objects inside F give virtual, upright images (magnifying glass)", ["inside f", "virtual", "upright", "magnifying"])],
        min_points=2,
        model_answer="The statement is wrong. When the object is further than F from the lens, the image is real and inverted. But when the object is closer than F, as in a magnifying glass, the image is virtual and upright.",
        hints=["Where is the object for a projector?", "And for a magnifying glass?", "Compare the images."],
        keywords="wrong; beyond F: inverted; inside F: upright, virtual",
        sample_pass=["Wrong, objects inside F give a virtual upright image, though objects beyond F give inverted images", "not always: a magnifying glass gives an upright virtual image"],
        sample_fail=["Correct, lenses always invert", "Correct because light crosses over"])

written("w12x_eval_camera_vs_eye", 12, 5, "12k",
        stem="Compare the image formed in a camera with the image formed by a projector lens, giving one similarity and one difference.",
        points=[P("similarity: both are real and inverted", ["both real", "both inverted", "real and inverted", "both are real"]),
                P("difference: camera image is diminished, projector image is magnified", ["diminished", "magnified", "smaller", "larger", "enlarged"]),
                P("because the camera's object is beyond 2F, the projector's between F and 2F", ["beyond 2f", "between f and 2f"])],
        min_points=2,
        model_answer="Both images are real and inverted. The camera's image is diminished, because the object is beyond 2F, while the projector's image is magnified, because the slide is between F and 2F.",
        hints=["Are both real?", "Which is larger?", "Why?"],
        keywords="both real, inverted; camera diminished (u > 2F), projector magnified (F < u < 2F)",
        sample_pass=["Both are real and inverted; the camera image is smaller and the projector image is magnified", "both real; the camera's object is beyond 2F giving a diminished image, the projector's is between F and 2F"],
        sample_fail=["Both are virtual", "The camera image is magnified"])

written("w12x_eval_rainbow_dispersion", 12, 5, "12c",
        stem="A student says that a glass prism adds colours to white light. Evaluate this statement.",
        points=[P("the statement is wrong: white light is already a mixture of colours", ["wrong", "mixture", "already contains", "made of"]),
                P("each colour is refracted by a different amount (different refractive index / speed in glass)", ["different amount", "different refractive index", "different speeds", "refracted differently", "different angles"]),
                P("so the colours spread out (dispersion)", ["spread", "dispersion", "separate"])],
        min_points=2,
        model_answer="The statement is wrong. White light is already a mixture of colours. Each colour travels at a slightly different speed in glass, so it is refracted by a different amount, and the colours spread out (dispersion).",
        hints=["What is white light made of?", "Is each colour bent equally?", "What is the effect?"],
        keywords="wrong; white is a mixture; different refraction → dispersion",
        sample_pass=["Wrong, white light is a mixture and each colour is refracted by a different amount so they spread out", "wrong: white light is a mixture, and the prism separates the colours because each is refracted by a different amount"],
        sample_fail=["Correct, the prism colours the light", "The prism reflects colours"])

written("w12x_eval_refraction_claim", 12, 5, "12c",
        stem="A student says: 'Light always changes direction when it passes from one material to another.' Evaluate this statement.",
        points=[P("the statement is not always true", ["not always", "wrong", "incorrect", "not true"]),
                P("light along the normal (i = 0) does not change direction", ["along the normal", "i = 0", "0°", "perpendicular", "at right angles to the surface"]),
                P("its speed still changes even though its direction does not", ["speed still changes", "speed changes", "slows", "speeds up"])],
        min_points=2,
        model_answer="The statement is not always true. If light meets the boundary along the normal (i = 0°), it passes straight through without changing direction, although its speed still changes.",
        hints=["Is there a special angle?", "What happens along the normal?", "Does the speed change?"],
        keywords="not always; along normal no bending; speed still changes",
        sample_pass=["Not always: light along the normal does not bend, though its speed still changes", "wrong, at i = 0° it goes straight through"],
        sample_fail=["Correct, light always bends", "Light never bends"])

written("w12x_eval_snell_experiment", 12, 5, "12d",
        stem="Two students measure n for the same glass block. One gets 1.48 and the other 1.55. Suggest reasons for the difference and how to decide which is more reliable.",
        points=[P("errors in drawing the normal or marking the rays / measuring angles with a protractor", ["normal", "protractor", "marking", "drawing", "measuring the angles", "thick ray"]),
                P("too few readings / small angles giving large percentage errors", ["few readings", "one reading", "small angles", "percentage error", "repeat"]),
                P("repeat with many angles and use the gradient of a sin i–sin r graph", ["gradient", "graph", "many angles", "repeat", "average"])],
        min_points=2,
        model_answer="The difference could come from errors in drawing the normal, marking the rays (a thick ray) or reading the protractor, and from taking too few readings or using small angles, which give large percentage errors. The more reliable value comes from many readings over a range of angles, using the gradient of a sin i against sin r graph.",
        hints=["Where can errors creep in?", "How many readings were taken?", "How can a better value be found?"],
        keywords="drawing/measurement errors; few readings; use graph gradient",
        sample_pass=["Errors in drawing the normal and measuring angles; repeat for many angles and use the gradient of a graph", "too few readings at small angles and errors in measuring the angles; plot sin i against sin r and use the gradient"],
        sample_fail=["The glass changed", "Both are exactly right"])

written("w12x_eval_wavelength_n", 12, 5, "12d",
        stem="A student says that because n = sin i ÷ sin r, the refractive index changes if you change the angle of incidence. Evaluate this statement.",
        points=[P("the statement is wrong: n is a constant for the material", ["wrong", "constant", "does not change", "incorrect"]),
                P("when i changes, r changes so that sin i ÷ sin r stays the same", ["r changes", "ratio stays", "stays the same", "both change"])],
        model_answer="The statement is wrong. The refractive index is a property of the material and is constant. If i changes, r also changes in such a way that sin i ÷ sin r stays the same.",
        hints=["Is n a property of the glass?", "What happens to r when i changes?", "What stays constant?"],
        keywords="wrong; n constant; r changes to keep ratio",
        sample_pass=["Wrong, n is constant; r changes so that sin i / sin r stays the same", "incorrect: both angles change but the ratio does not"],
        sample_fail=["Correct, n depends on the angle", "n doubles if i doubles"])
