"""Chapter 1 written-answer bank extension: 5 more per level so that each level has 10 questions and every LO appears at least twice."""
from .. import figs2, sketches
from ..marker import Pitfall, Point
from .base import written

P = Point
PF = Pitfall

# ---------------------------------------------------------------- L1
written("w1b_magnitude_unit_example", 1, 1, "1a",
        stem="A student writes the length of a desk as '120'. State what is missing and why it matters.",
        points=[P("the unit is missing (e.g. cm)", ["unit is missing", "no unit", "missing unit", "without a unit", "needs a unit", "unit"]),
                P("without a unit the number has no meaning: 120 cm and 120 m are very different", ["no meaning", "meaningless", "could be cm or m", "120 m", "different", "cannot tell"])],
        model_answer="The unit is missing. A physical quantity needs a numerical magnitude AND a unit; without the unit '120' has no meaning, since 120 cm and 120 m are very different lengths.",
        hints=["A physical quantity has two parts. Which part is given?", "What would make '120' a length?", "State what is missing and why it matters."],
        keywords="unit missing; magnitude alone has no meaning",
        sample_pass=["The unit is missing, so we cannot tell if it is 120 cm or 120 m", "there is no unit, and without it the number is meaningless"],
        sample_fail=["The desk is too long", "It should have more decimal places"])

written("w1b_six_base_units", 1, 1, "1b",
        stem="State the SI base units of electric current, temperature and amount of substance.",
        points=[P("current: ampere (A)", ["ampere", "amp", "current a"]),
                P("temperature: kelvin (K)", ["kelvin", "temperature k"]),
                P("amount of substance: mole (mol)", ["mole", "mol"])],
        pitfalls=[PF(["degree celsius", "degrees celsius"], "The SI base unit of temperature is the KELVIN, not the degree Celsius."),
                  PF(["coulomb"], "The coulomb is the unit of charge; current is measured in amperes.")],
        model_answer="Electric current: ampere (A). Temperature: kelvin (K). Amount of substance: mole (mol).",
        hints=["These are three of the six base quantities.", "One is named after Ampère, one after Lord Kelvin.", "State all three units."],
        keywords="ampere, kelvin, mole",
        sample_pass=["Ampere, kelvin and mole", "current A, temperature K, amount of substance mol"],
        sample_fail=["Coulomb, degree Celsius and gram", "Volt, joule and newton"])

written("w1b_milli_micro", 1, 1, "1c",
        stem="State the meaning of the prefixes micro (µ) and nano (n).",
        points=[P("micro = 10⁻⁶ (one millionth)", ["10^-6", "10⁻⁶", "millionth", "0.000001", "10 to the power of -6"]),
                P("nano = 10⁻⁹ (one thousand-millionth)", ["10^-9", "10⁻⁹", "billionth", "0.000000001", "thousand millionth", "10 to the power of -9"])],
        model_answer="Micro means 10⁻⁶ (one millionth); nano means 10⁻⁹ (one thousand-millionth).",
        hints=["Both are sub-multiples (less than 1).", "Micro is three powers of ten below milli; nano is three below micro.", "Give both as powers of ten."],
        keywords="micro 10⁻⁶, nano 10⁻⁹",
        sample_pass=["micro is 10^-6 and nano is 10^-9", "micro means a millionth and nano means a billionth"],
        sample_fail=["micro is 10^6 and nano is 10^9", "Both mean one thousandth"])

written("w1b_define_precision", 1, 1, "1e",
        stem="State the precision of (a) digital calipers and (b) a digital micrometer.",
        points=[P("digital calipers: 0.01 mm", ["0.01 mm", "0.001 cm", "hundredth of a millimetre"]),
                P("digital micrometer: 0.001 mm", ["0.001 mm", "0.0001 cm", "thousandth of a millimetre"])],
        model_answer="Digital calipers read to 0.01 mm; a digital micrometer reads to 0.001 mm.",
        hints=["Precision = the smallest reading the instrument can show.", "One reads to two decimal places of a millimetre, the other to three.", "State both, with units."],
        keywords="calipers 0.01 mm; micrometer 0.001 mm",
        sample_pass=["Calipers 0.01 mm and micrometer 0.001 mm", "digital calipers read to 0.01 mm, the digital micrometer to 0.001 mm"],
        sample_fail=["Both read to 1 mm", "Calipers 0.1 cm and micrometer 0.01 cm"])

written("w1b_define_vector", 1, 1, "1f",
        stem="State what is meant by a vector quantity and give two examples.",
        points=[P("a vector has both magnitude and direction", ["magnitude and direction", "size and direction", "has a direction", "direction as well"]),
                P("examples: force, velocity, displacement, acceleration, weight", ["force", "velocity", "displacement", "acceleration", "weight", "momentum"])],
        model_answer="A vector quantity has both magnitude and direction, for example force and velocity.",
        hints=["How does a vector differ from a scalar?", "Think of quantities that point somewhere.", "Define it and name two."],
        keywords="magnitude and direction; force, velocity",
        sample_pass=["It has magnitude and direction, e.g. force and velocity", "a quantity with size and direction such as displacement and acceleration"],
        sample_fail=["A quantity with a large magnitude like mass and energy", "Anything measured in metres"])

# ---------------------------------------------------------------- L2
written("w1b_order_prefixes", 1, 2, "1c",
        stem="Arrange the prefixes deci, kilo, micro, centi and mega in order from the largest to the smallest, giving the power of ten for each.",
        points=[P("mega (10⁶), kilo (10³) first", ["mega 10^6 kilo 10^3", "mega 10⁶ kilo 10³", "mega kilo", "mega, kilo"], ordered=True),
                P("then deci (10⁻¹), centi (10⁻²), micro (10⁻⁶)", ["deci centi micro", "deci, centi, micro", "deci 10^-1 centi 10^-2 micro 10^-6", "deci 10⁻¹ centi 10⁻² micro 10⁻⁶"], ordered=True)],
        model_answer="Mega (10⁶), kilo (10³), deci (10⁻¹), centi (10⁻²), micro (10⁻⁶).",
        hints=["Write each prefix as a power of ten first.", "Two are multiples (positive powers), three are sub-multiples.", "Order from the largest power down."],
        keywords="mega 10⁶ > kilo 10³ > deci 10⁻¹ > centi 10⁻² > micro 10⁻⁶",
        sample_pass=["mega 10^6, kilo 10^3, deci 10^-1, centi 10^-2, micro 10^-6", "mega, kilo, deci, centi, micro"],
        sample_fail=["micro, centi, deci, kilo, mega", "kilo, mega, centi, deci, micro"])

written("w1b_scalar_vector_examples", 1, 2, "1f",
        stem="Classify each quantity as scalar or vector: speed, displacement, energy, weight.",
        points=[P("scalars: speed and energy", ["speed and energy are scalars", "speed energy scalar", "scalars speed energy", "speed scalar", "energy scalar"]),
                P("vectors: displacement and weight", ["displacement and weight are vectors", "displacement weight vector", "vectors displacement weight", "displacement vector", "weight vector"])],
        pitfalls=[PF(["weight is a scalar", "speed is a vector"], "Weight is a force, so it is a VECTOR; speed has no direction, so it is a SCALAR.")],
        min_points=2,
        model_answer="Scalars: speed and energy (magnitude only). Vectors: displacement and weight (magnitude and direction).",
        hints=["Ask of each: does it have a direction?", "Weight is a force; speed is just how fast.", "Give two of each."],
        keywords="scalar: speed, energy; vector: displacement, weight",
        sample_pass=["Speed and energy are scalars; displacement and weight are vectors", "scalars are speed, energy and vectors are displacement, weight"],
        sample_fail=["All four are vectors", "Speed and weight are vectors"])

written("w1b_speed_velocity_difference", 1, 2, "1f",
        stem="Two cars travel at 20 m/s, one going north and one going south. State whether they have the same speed and the same velocity, and explain.",
        points=[P("same speed (20 m/s): speed is a scalar, magnitude only", ["same speed", "speed is the same", "speeds are equal", "speed is a scalar"]),
                P("different velocities: velocity is a vector and their directions are opposite", ["different velocities", "velocity is different", "velocities are different", "not the same velocity", "opposite directions", "velocity is a vector"])],
        model_answer="They have the same speed, 20 m/s, because speed is a scalar (magnitude only). Their velocities are different, because velocity is a vector and they travel in opposite directions.",
        hints=["Speed: how fast. Velocity: how fast and which way.", "Do the cars move the same way?", "Compare both quantities."],
        keywords="same speed (scalar); different velocity (vector, opposite directions)",
        sample_pass=["Same speed but different velocities because they move in opposite directions", "speed is the same since it is a scalar; velocity differs as it is a vector and the directions are opposite"],
        sample_fail=["Same speed and same velocity", "Different speeds because one goes north"])

written("w1b_base_or_derived", 1, 2, "1b",
        stem="State which of these are base quantities: mass, force, time, volume. Explain how you decided.",
        points=[P("base quantities: mass and time", ["mass and time", "mass time", "base mass", "time and mass"]),
                P("force and volume are derived: built from base quantities (force from mass, length, time; volume from length)", ["derived", "built from", "made from", "combination of", "from length", "not base"])],
        pitfalls=[PF(["force is a base", "volume is a base"], "Force and volume are DERIVED quantities; the base quantities are mass, length, time, current, temperature and amount of substance.")],
        model_answer="Mass and time are base quantities. Force and volume are derived quantities: force comes from mass, length and time (F = ma), and volume from length cubed.",
        hints=["There are six base quantities. Which of these are in the list?", "Can force or volume be built from other quantities?", "Name the base ones and explain the others."],
        keywords="mass, time base; force, volume derived from base quantities",
        sample_pass=["Mass and time are base quantities; force and volume are derived from them", "mass and time are base, the other two are made from base quantities like length"],
        sample_fail=["Force and volume are base quantities", "All four are base quantities"])

written("w1b_ampere_mole", 1, 2, "1b",
        stem="A student lists the base quantities as 'mass, length, time, weight, temperature and current'. Identify the mistake and correct it.",
        points=[P("weight is not a base quantity (it is a force, a derived quantity)", ["weight is not a base", "weight is a force", "weight is derived", "remove weight", "weight should not"]),
                P("the missing base quantity is amount of substance (mole)", ["amount of substance", "mole", "mol"])],
        model_answer="Weight should not be in the list: it is a force, a derived quantity. The missing base quantity is amount of substance, measured in moles.",
        hints=["Is weight one of the six?", "Which base quantity is missing?", "Name the wrong one and the missing one."],
        keywords="weight is derived (force); missing: amount of substance (mol)",
        sample_pass=["Weight is not a base quantity; it should be amount of substance", "remove weight, which is a force, and add amount of substance measured in mol"],
        sample_fail=["Temperature should be replaced by heat", "The list is correct"])

# ---------------------------------------------------------------- L3
written("w1b_estimate_atoms_line", 1, 3, "1d",
        stem="An atom is about 10⁻¹⁰ m across. Explain how to estimate the number of atoms that would fit side by side across a 1 mm gap, and give the estimate.",
        points=[P("convert 1 mm to metres: 10⁻³ m", ["10^-3", "10⁻³", "0.001 m", "1 mm = 0.001"]),
                P("divide the gap by the size of one atom: 10⁻³ ÷ 10⁻¹⁰", ["divide", "÷", "/"]),
                P("about 10⁷ atoms", ["10^7", "10⁷", "10 million", "ten million", "10 000 000"])],
        min_points=2,
        model_answer="Change 1 mm into metres: 1 mm = 10⁻³ m. Divide the gap by the diameter of one atom: 10⁻³ ÷ 10⁻¹⁰ = 10⁷. About ten million atoms fit across the gap.",
        hints=["Put both lengths in the same unit.", "How many atom-widths fit into the gap?", "Divide and give the order of magnitude."],
        keywords="1 mm = 10⁻³ m; divide by 10⁻¹⁰; about 10⁷",
        sample_pass=["1 mm is 10^-3 m; dividing by 10^-10 gives about 10^7 atoms", "convert to 0.001 m and divide by the atom size to get 10 million"],
        sample_fail=["About 100 atoms", "Atoms are too small to count"])

written("w1b_scalar_vector_reason", 1, 3, "1f",
        stem="Explain why temperature is a scalar but force is a vector.",
        points=[P("temperature has magnitude only: it does not point in any direction", ["magnitude only", "no direction", "size only", "does not have a direction", "does not point", "temperature does not"]),
                P("force has magnitude and direction: the same size force in a different direction has a different effect", ["magnitude and direction", "has a direction", "size and direction", "push or pull in a direction", "direction matters"])],
        model_answer="Temperature has magnitude only: '30 °C' has no direction. Force has magnitude and direction: a 10 N push to the left has a different effect from a 10 N push to the right.",
        hints=["Can you say 'a temperature of 30 °C to the left'?", "Does the direction of a force change what it does?", "Explain each."],
        keywords="temperature: magnitude only; force: magnitude and direction",
        sample_pass=["Temperature has only magnitude and no direction, while force has magnitude and direction", "a force acts in a direction, temperature does not"],
        sample_fail=["Temperature can be negative so it is a vector", "Force is bigger than temperature"])

written("w1b_resultant_same_line", 1, 3, "1g",
        stem="A tug pulls a ship forward with 8000 N while the water exerts 3000 N of drag backwards. Explain how to find the resultant force and state it.",
        points=[P("the forces act in opposite directions along the same line, so subtract", ["opposite directions", "subtract", "take away", "minus", "difference"]),
                P("resultant = 8000 − 3000 = 5000 N forward (in the direction of the pull)", ["5000", "5 000", "5 kn", "5kn"]),
                P("direction: forward / in the direction of the larger force", ["forward", "direction of the pull", "direction of the larger", "towards the tug"])],
        min_points=2,
        model_answer="The two forces act in opposite directions along the same line, so the resultant is their difference: 8000 − 3000 = 5000 N, acting forwards in the direction of the tug's pull.",
        hints=["Are the forces in the same or opposite directions?", "Opposite forces along a line: subtract.", "Give the size and the direction."],
        keywords="opposite directions → subtract; 5000 N forward",
        sample_pass=["They are opposite so subtract: 5000 N forward", "the resultant is 8000 - 3000 = 5000 N in the direction of the pull"],
        sample_fail=["Add them to get 11 000 N", "The resultant is 3000 N backwards"])

written("w1b_resultant_right_angles", 1, 3, "1g",
        stem="Fig. 1 shows two forces of 6 N and 8 N acting at right angles on an object. Explain how to find the resultant force by a graphical method, and state its magnitude.",
        points=[P("draw both forces to scale from the same point (e.g. 1 cm : 1 N)", ["to scale", "scale", "1 cm", "draw both forces", "same point"]),
                P("complete the rectangle / parallelogram and draw the diagonal from the point where the forces act", ["parallelogram", "rectangle", "diagonal", "complete", "tip to tail"]),
                P("measure the diagonal and convert using the scale: 10 N", ["10 n", "10n", "measure", "10 newtons", "length of the diagonal"])],
        min_points=2,
        model_answer="Choose a scale, e.g. 1 cm : 1 N, and draw the 6 N and 8 N forces from the same point at right angles. Complete the rectangle and draw the diagonal from that point; this is the resultant. Measure the diagonal (10 cm) and convert with the scale: the resultant is 10 N.",
        hints=["A graphical method is a scale drawing. What do you draw first?", "How do you get the resultant from the two drawn forces?", "Measure and convert; state the answer."],
        keywords="scale drawing from one point; complete parallelogram/rectangle; diagonal = resultant = 10 N",
        figure=lambda: figs2.vector_grid([("6 N", 6, 0), ("8 N", 0, 8)], nx=9, ny=10, origin=(1, 1)),
        sample_pass=["Draw them to scale from one point, complete the rectangle and measure the diagonal: 10 N", "use a scale of 1 cm to 1 N, draw a parallelogram, the diagonal is 10 N"],
        sample_fail=["Add the forces to get 14 N", "Subtract to get 2 N"])

written("w1b_repeat_average_reason", 1, 3, "1e",
        stem="Explain why a student takes several readings of the diameter of a ball bearing at different orientations and averages them.",
        points=[P("the ball may not be perfectly round / readings vary (random errors)", ["not perfectly round", "not perfectly spherical", "vary", "random error", "different readings", "not uniform"]),
                P("averaging reduces the effect of random errors, giving a more reliable/accurate value", ["average", "mean", "reduces", "more reliable", "more accurate"])],
        model_answer="The ball bearing may not be perfectly round and individual readings vary because of random errors. Taking several readings at different orientations and averaging them reduces the effect of these random errors, giving a more reliable value of the diameter.",
        hints=["Would every reading be exactly the same?", "What does averaging do to random variations?", "Explain both."],
        keywords="readings vary (shape, random error); averaging reduces random error",
        sample_pass=["The ball may not be perfectly round so readings vary; averaging reduces random errors", "different readings have random errors and the mean is more reliable"],
        sample_fail=["To remove the zero error", "Because the calipers are broken"])

# ---------------------------------------------------------------- L4
written("w1b_scale_drawing_steps", 1, 4, "1g",
        stem="Two forces of 5.0 N and 7.0 N act at 60° to each other on a point. Describe fully how to find the magnitude and direction of the resultant by a scale drawing.",
        points=[P("choose and state a scale, e.g. 1 cm : 1 N", ["scale", "1 cm", "1cm"]),
                P("draw the two forces from one point at 60° to each other using a protractor", ["protractor", "60", "same point", "from one point"]),
                P("complete the parallelogram and draw the diagonal from the starting point", ["parallelogram", "diagonal", "complete"]),
                P("measure the diagonal's length (convert with the scale) and its angle to one force", ["measure", "length", "angle", "convert", "direction"])],
        min_points=3,
        model_answer="Choose a scale such as 1 cm : 1 N. Draw the 5.0 N force as a 5.0 cm line, then with a protractor draw the 7.0 N force as a 7.0 cm line from the same point at 60° to the first. Complete the parallelogram and draw the diagonal from the starting point: this is the resultant. Measure its length and convert with the scale to get the magnitude, and measure the angle between the diagonal and one of the forces to give its direction.",
        hints=["What must be chosen and written before drawing?", "How do you draw the second force at the right angle?", "How do you get both the size and the direction of the resultant?"],
        keywords="scale; draw both from one point at 60° (protractor); complete parallelogram; diagonal: measure length and angle",
        sample_pass=["Use a scale of 1 cm to 1 N, draw both forces from one point at 60 degrees with a protractor, complete the parallelogram, then measure the length and angle of the diagonal",
                     "state a scale, draw the forces at 60° from the same point, complete the parallelogram, measure the diagonal and convert using the scale, and measure its angle"],
        sample_fail=["Add 5 and 7 to get 12 N", "Use Pythagoras because there are two forces"])

written("w1b_resultant_depends_angle", 1, 4, "1g",
        stem="Explain how the resultant of two forces of 4 N and 6 N changes as the angle between them increases from 0° to 180°.",
        points=[P("at 0° (same direction) the resultant is largest: 10 N", ["10 n", "largest", "maximum", "same direction", "add"]),
                P("as the angle increases the resultant decreases", ["decreases", "gets smaller", "becomes smaller", "falls", "less"]),
                P("at 180° (opposite) it is smallest: 2 N", ["2 n", "smallest", "minimum", "opposite"])],
        min_points=2,
        model_answer="At 0° the forces act in the same direction and the resultant is largest, 4 + 6 = 10 N. As the angle increases, the forces work less together and the resultant decreases. At 180° they act in opposite directions and the resultant is smallest, 6 − 4 = 2 N.",
        hints=["What is the resultant when the forces point the same way?", "And when they point opposite ways?", "Describe the trend between."],
        keywords="0°: 10 N maximum; decreases with angle; 180°: 2 N minimum",
        sample_pass=["It is largest at 0 degrees (10 N) and decreases as the angle increases until it is smallest at 180 degrees (2 N)", "the resultant gets smaller as the angle increases, from a maximum of 10 N to a minimum of 2 N"],
        sample_fail=["It stays at 10 N", "It increases as the angle increases"])

written("w1b_order_magnitude_compare", 1, 4, "1d",
        stem="Explain what is meant by saying that the diameter of the Earth is about '10¹⁷ times' the diameter of an atom, using orders of magnitude.",
        points=[P("Earth about 10⁷ m, atom about 10⁻¹⁰ m", ["10^7", "10⁷", "10^-10", "10⁻¹⁰"]),
                P("dividing: 10⁷ ÷ 10⁻¹⁰ = 10¹⁷ (subtract the powers of ten)", ["divide", "÷", "subtract the powers", "7 - (-10)", "7 + 10", "10^17", "10¹⁷"])],
        model_answer="The Earth's diameter is about 10⁷ m and an atom's about 10⁻¹⁰ m. Dividing, 10⁷ ÷ 10⁻¹⁰ = 10¹⁷: the Earth is about 10¹⁷ times wider, an order-of-magnitude comparison.",
        hints=["Give each size as a power of ten in metres.", "How do you compare them?", "Divide by subtracting the powers."],
        keywords="Earth 10⁷ m, atom 10⁻¹⁰ m; ratio 10¹⁷",
        sample_pass=["The Earth is about 10^7 m and an atom 10^-10 m, so dividing gives 10^17", "10⁷ ÷ 10⁻¹⁰ = 10¹⁷"],
        sample_fail=["The Earth has 10^17 atoms", "The atom is 10^17 m across"])

written("w1b_choose_instrument_justify", 1, 4, "1e",
        stem="A student needs the thickness of a single sheet of paper (about 0.1 mm). Suggest a method using a digital micrometer that gives an accurate value, and explain why it is better than measuring one sheet with a rule.",
        points=[P("measure a stack of many sheets (e.g. 50) with the micrometer (or calipers) and divide by the number of sheets", ["stack", "many sheets", "50 sheets", "100 sheets", "divide by the number"]),
                P("a rule reads only to 1 mm, which is ten times the thickness of one sheet, so a direct reading is useless", ["1 mm", "too coarse", "larger than the sheet", "not precise", "cannot measure"]),
                P("the micrometer reads to 0.001 mm and dividing a large reading reduces the percentage error", ["0.001 mm", "percentage error", "smaller error", "more precise", "reduces the error"])],
        min_points=2,
        model_answer="Measure the thickness of a stack of, say, 50 sheets with the digital micrometer (reading to 0.001 mm) and divide by 50. A rule reads only to 1 mm, ten times the thickness of one sheet, so measuring one sheet directly with it is useless; measuring a stack with a precise instrument and dividing makes the percentage error very small.",
        hints=["How can you make a very thin object easier to measure?", "Compare the rule's precision with 0.1 mm.", "Describe the method and explain the gain in accuracy."],
        keywords="measure a stack, divide by number; rule 1 mm too coarse; micrometer 0.001 mm, small % error",
        sample_pass=["Measure a stack of 50 sheets with the micrometer and divide by 50; a rule only reads to 1 mm which is bigger than a sheet", "use many sheets and divide; the micrometer is more precise so the percentage error is smaller"],
        sample_fail=["Fold one sheet in half and measure it with a rule", "Weigh the sheet on a balance"])

# ---------------------------------------------------------------- L5
written("w1b_eval_displacement_claim", 1, 5, "1f",
        stem="A student walks 3 km north and then 4 km east and claims her displacement is 7 km. Evaluate the claim.",
        points=[P("the claim is wrong: 7 km is the distance travelled, not the displacement", ["wrong", "incorrect", "distance travelled", "that is the distance", "7 km is the distance"]),
                P("displacement is the straight line from start to finish: √(3² + 4²) = 5 km", ["5 km", "5km", "pythagoras", "straight line", "hypotenuse"]),
                P("in a direction north-east of the start (about 53° east of north)", ["north-east", "north east", "53", "east of north", "direction"])],
        min_points=2,
        model_answer="The claim is wrong: 7 km is the distance travelled. Displacement is the straight-line distance from start to finish with a direction: √(3² + 4²) = 5 km, north-east of the start (about 53° east of north).",
        hints=["What does 7 km represent?", "What is displacement, and how is it found for legs at right angles?", "Give the size and direction."],
        keywords="7 km is distance; displacement 5 km (Pythagoras), north-east",
        sample_pass=["Wrong, 7 km is the distance; the displacement is 5 km north-east by Pythagoras", "incorrect, her displacement is the straight line from start to finish, 5 km"],
        sample_fail=["Correct, 3 + 4 = 7 km", "Her displacement is 1 km"])

written("w1b_eval_scalar_negative", 1, 5, "1f",
        stem="A student says: 'Temperature can be −5 °C, so it must be a vector because it has a negative sign.' Evaluate this argument.",
        points=[P("the argument is wrong: temperature is a scalar", ["wrong", "incorrect", "scalar", "not a vector"]),
                P("the negative sign shows a value below zero on a scale, not a direction in space", ["below zero", "on a scale", "not a direction", "no direction", "less than zero"]),
                P("a vector must have a direction; temperature has magnitude only", ["magnitude only", "must have a direction", "has no direction", "direction in space"])],
        min_points=2,
        model_answer="The argument is wrong: temperature is a scalar. A minus sign on a temperature only means the value is below zero on the scale; it does not point in any direction in space. A vector must have a direction, while temperature has magnitude only.",
        hints=["What does the minus sign in −5 °C mean?", "Does it describe a direction?", "Judge the argument."],
        keywords="wrong; negative = below zero on a scale, not a direction; temperature is a scalar",
        sample_pass=["Wrong, temperature is a scalar; the negative sign just means below zero, not a direction", "the minus shows a value below zero on the scale, temperature has no direction so it is a scalar"],
        sample_fail=["Correct, negative numbers are always vectors", "Temperature is a vector because it can change"])

written("w1b_eval_forces_cancel", 1, 5, "1g",
        stem="Three ropes pull on a ring. A student says the ring will stay still only if all three forces are equal in size. Evaluate the claim.",
        points=[P("the claim is wrong: the forces need not be equal", ["wrong", "incorrect", "not necessarily", "need not be equal", "do not have to be equal"]),
                P("the ring stays still if the resultant of the three forces is zero (they form a closed triangle when drawn tip to tail)", ["resultant is zero", "zero resultant", "closed triangle", "cancel", "balance", "tip to tail"]),
                P("e.g. 3 N, 4 N and 5 N at suitable angles balance; equal forces must be at 120° to balance", ["3 n, 4 n and 5 n", "3, 4 and 5", "120", "angles", "different sizes"])],
        min_points=2,
        model_answer="The claim is wrong. The ring stays still when the resultant of the three forces is zero, i.e. when the forces drawn tip to tail form a closed triangle. The forces need not be equal: 3 N, 4 N and 5 N at suitable angles balance. Three equal forces balance only when they are at 120° to one another.",
        hints=["What is the condition for an object to stay still under several forces?", "Can unequal forces cancel?", "Give a counter-example."],
        keywords="wrong; resultant must be zero (closed triangle); unequal forces can balance (3, 4, 5 N)",
        sample_pass=["Wrong, the forces only need a zero resultant, forming a closed triangle; 3 N, 4 N and 5 N can balance", "incorrect, they do not have to be equal, they just have to cancel out"],
        sample_fail=["Correct, unequal forces always make it move", "The ring moves towards the largest force always"])

written("w1b_eval_prefix_answer", 1, 5, "1c",
        stem="A student converts 2.5 mm² into m² and writes 2.5 × 10⁻³ m². Evaluate the answer and give the correct value.",
        points=[P("the answer is wrong: the area factor must be squared", ["wrong", "incorrect", "squared", "square the factor", "two dimensions"]),
                P("1 mm² = (10⁻³ m)² = 10⁻⁶ m²", ["10^-6", "10⁻⁶", "0.000001"]),
                P("so 2.5 mm² = 2.5 × 10⁻⁶ m²", ["2.5 × 10⁻⁶", "2.5 x 10^-6", "2.5 × 10^-6", "2.5x10^-6", "0.0000025"])],
        min_points=2,
        model_answer="The answer is wrong: for an area the length factor must be squared. 1 mm = 10⁻³ m, so 1 mm² = (10⁻³ m)² = 10⁻⁶ m². The correct value is 2.5 × 10⁻⁶ m².",
        hints=["How many dimensions does an area have?", "Square the conversion factor for mm → m.", "Correct the value."],
        keywords="square the factor; 1 mm² = 10⁻⁶ m²; 2.5 × 10⁻⁶ m²",
        sample_pass=["Wrong, the factor must be squared: 1 mm² = 10^-6 m², so 2.5 × 10^-6 m²", "incorrect, it should be 2.5 x 10^-6 m² because area uses the square of the conversion"],
        sample_fail=["Correct, milli means 10^-3", "It should be 2.5 × 10^3 m²"])

written("w1b_eval_volume_conversion", 1, 5, "1c",
        stem="A student says that a 500 cm³ bottle has a volume of 5 m³ because '1 m = 100 cm'. Evaluate the reasoning and give the correct volume.",
        points=[P("wrong: for a volume the factor 100 must be cubed", ["wrong", "incorrect", "cubed", "cube the factor", "three dimensions"]),
                P("1 m³ = 100 × 100 × 100 = 1 000 000 cm³", ["1 000 000", "1000000", "10^6", "10⁶", "million"]),
                P("so 500 cm³ = 500 ÷ 10⁶ = 5 × 10⁻⁴ m³", ["5 × 10⁻⁴", "5 x 10^-4", "0.0005", "5x10^-4", "5 × 10^-4"])],
        min_points=2,
        model_answer="The reasoning is wrong: a volume has three length dimensions, so the factor must be cubed. 1 m³ = 100 × 100 × 100 = 1 000 000 cm³. So 500 cm³ = 500 ÷ 1 000 000 = 5 × 10⁻⁴ m³.",
        hints=["A cube 1 m on each side is how many cm on each side?", "Cube that number.", "Divide 500 by it."],
        keywords="cube the factor; 1 m³ = 10⁶ cm³; 5 × 10⁻⁴ m³",
        sample_pass=["Wrong, 1 m³ is 1 000 000 cm³ so the volume is 5 x 10^-4 m³", "incorrect, the factor of 100 must be cubed, giving 0.0005 m³"],
        sample_fail=["Correct, divide by 100", "The volume is 50 m³"])


# ---------------------------------------------------------------- additions to complete the L4 / L5 pools
written("w1b_size_ladder", 1, 4, "1d",
        stem="Place a human hair, a bacterium and an atom in order of size and give the order of magnitude of each in metres. Explain why a light microscope can show the bacterium but not the atom.",
        points=[P("atom about 10⁻¹⁰ m < bacterium about 10⁻⁶ m < hair about 10⁻⁴ m", ["10^-10", "10⁻¹⁰", "10^-6", "10⁻⁶", "10^-4", "10⁻⁴"]),
                P("order: atom, bacterium, hair (smallest first)", ["atom bacterium hair", "atom, bacterium, hair", "atom then bacterium then hair"], ordered=True),
                P("the atom is about 10 000 times smaller than the bacterium, far too small to see with visible light", ["10 000 times", "10^4 times", "too small", "far smaller", "much smaller"])],
        min_points=2,
        model_answer="Atom (about 10⁻¹⁰ m), bacterium (about 10⁻⁶ m), hair (about 10⁻⁴ m). A bacterium is large enough to be seen in a light microscope, but an atom is about 10 000 times smaller still, far too small to be seen with visible light.",
        hints=["Give each a power of ten.", "Which is smallest?", "Compare the atom with the bacterium."],
        keywords="atom 10⁻¹⁰ m < bacterium 10⁻⁶ m < hair 10⁻⁴ m; atom ~10⁴ times smaller than bacterium",
        sample_pass=["atom 10^-10 m, bacterium 10^-6 m, hair 10^-4 m; the atom is 10 000 times smaller than the bacterium so it is too small to see",
                     "atom, bacterium, hair; the atom is about 10⁻¹⁰ m, much smaller than the 10⁻⁶ m bacterium"],
        sample_fail=["hair, atom, bacterium", "They are all about the same size"])

written("w1b_eval_triangle_method", 1, 5, "1g",
        stem="To find the resultant of two forces, a student draws the first force, then draws the second force starting from the TAIL of the first, and joins the two tips. Evaluate the method.",
        points=[P("the method is wrong as described: joining the two tips gives the difference, not the resultant", ["wrong", "incorrect", "difference", "not the resultant"]),
                P("in the triangle method the second force starts at the TIP (head) of the first (tip to tail)", ["tip to tail", "head to tail", "from the tip", "at the end of the first", "from the head"]),
                P("the resultant runs from the tail of the first force to the tip of the second (or use the parallelogram diagonal from the common point)", ["tail of the first to the tip of the second", "start of the first to the end of the second", "diagonal", "parallelogram"])],
        min_points=2,
        model_answer="The method is wrong as described: drawing both forces from the same tail and joining their tips gives the difference of the vectors, not their sum. For the triangle method the second force must start at the tip of the first (tip to tail), and the resultant runs from the tail of the first to the tip of the second; alternatively, complete the parallelogram and draw the diagonal from the common point.",
        hints=["In the triangle method, where does the second arrow start?", "What does the line joining two tips represent?", "Judge the method and describe the correct one."],
        keywords="joining tips gives the difference; draw tip to tail; resultant from first tail to second tip (or parallelogram diagonal)",
        sample_pass=["Wrong, joining the tips gives the difference; the second force should be drawn tip to tail and the resultant goes from the tail of the first to the tip of the second",
                     "incorrect, use tip to tail or draw the parallelogram diagonal instead"],
        sample_fail=["Correct, that is the parallelogram method", "Add the lengths of the two arrows"])
