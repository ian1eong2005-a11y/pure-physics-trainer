"""Chapter 3 Dynamics written-answer bank extension: fills each level to at least 10 with every LO at least twice."""
from .. import figs, figs2
from ..marker import Pitfall, Point
from .base import written

P = Point
PF = Pitfall

# ---------------------------------------------------------------- L1
written("w3x_contact_examples", 3, 1, "3a",
        stem="Name two contact forces and two non-contact forces.",
        points=[P("contact: two of friction, air resistance, tension, normal force", ["friction", "air resistance", "tension", "normal", "drag", "upthrust"]),
                P("non-contact: two of gravitational, magnetic, electrostatic", ["gravitational", "gravity", "weight", "magnetic", "electrostatic", "electric"])],
        model_answer="Contact forces: friction and tension. Non-contact forces: gravitational force and magnetic force.",
        hints=["Contact forces need touching surfaces.", "Non-contact forces act at a distance.", "Two of each."],
        keywords="contact: friction, tension, normal force, air resistance; non-contact: gravity, magnetic, electrostatic",
        sample_pass=["Contact: friction and tension; non-contact: gravitational and magnetic", "friction, normal force; gravity and electrostatic force"],
        sample_fail=["Speed and acceleration", "Mass and volume"])

written("w3x_define_mass", 3, 1, "3b",
        stem="State what is meant by the mass of a body and give its SI unit.",
        points=[P("the amount of matter in the body", ["amount of matter", "quantity of matter", "matter in"]),
                P("unit: kilogram (kg)", ["kilogram", "kg"])],
        pitfalls=[PF(["newton", "force of gravity"], "That describes WEIGHT. Mass is the amount of matter, in kilograms.")],
        model_answer="Mass is a measure of the amount of matter in a body; its SI unit is the kilogram (kg).",
        hints=["Mass does not change from place to place.", "It measures how much matter there is.", "Give the unit."],
        keywords="amount of matter; kilogram",
        sample_pass=["The amount of matter in a body, measured in kilograms", "how much matter it contains, kg"],
        sample_fail=["The force of gravity on it, in newtons", "How big the object is"])

written("w3x_define_g_unit", 3, 1, "3d",
        stem="State the meaning of gravitational field strength and its unit.",
        points=[P("gravitational force per unit mass", ["force per unit mass", "force per kilogram", "force on each kilogram", "weight per unit mass", "per unit mass"]),
                P("unit: N/kg", ["n/kg", "newtons per kilogram", "newton per kilogram"])],
        model_answer="Gravitational field strength is the gravitational force per unit mass at a point; its unit is the newton per kilogram (N/kg).",
        hints=["It is a force divided by something.", "Per what?", "Give the unit too."],
        keywords="force per unit mass; N/kg",
        sample_pass=["The gravitational force per unit mass, in N/kg", "force on each kilogram, newtons per kilogram"],
        sample_fail=["The mass of the Earth", "The speed of falling objects in m/s"])

written("w3x_fbd_book", 3, 1, "3h",
        stem="A book rests on a table. Name the two forces acting on the book and state their directions.",
        points=[P("weight (gravitational force) acting downwards", ["weight downwards", "weight acts down", "gravity downwards", "weight down", "gravitational force downwards", "gravity pulls it down", "pulls it down"]),
                P("normal (contact/reaction) force from the table acting upwards", ["normal force upwards", "reaction upwards", "normal force up", "contact force upwards", "upward force from the table", "reaction pushes it up", "pushes it up"])],
        model_answer="The book's weight acts downwards and the normal (contact) force from the table acts upwards; they are equal in size.",
        hints=["One force is due to gravity.", "The other comes from the table.", "Give the directions."],
        keywords="weight down; normal force up",
        sample_pass=["Weight downwards and the normal force from the table upwards", "gravity pulls it down and the table's reaction pushes it up"],
        sample_fail=["Friction and air resistance", "Only its weight"])

written("w3x_newton_second_words", 3, 1, "3j",
        stem="State the relationship between resultant force, mass and acceleration, giving the units of each quantity.",
        points=[P("resultant force = mass × acceleration (F = m a)", ["mass × acceleration", "mass x acceleration", "mass times acceleration", "f = ma", "f = m a", "m × a"]),
                P("units: N, kg, m/s²", ["n kg m/s2", "newtons", "kg", "m/s2", "m/s²"])],
        model_answer="Resultant force = mass × acceleration (F = m a), with F in newtons (N), m in kilograms (kg) and a in m/s².",
        hints=["Which equation links the three?", "Write it in words or symbols.", "Add the units."],
        keywords="F = m a; N, kg, m/s²",
        sample_pass=["Resultant force = mass × acceleration, in N, kg and m/s²", "F = m a where F is in newtons, m in kg and a in m/s²"],
        sample_fail=["Force = mass × velocity", "Force = mass ÷ acceleration"])

written("w3x_friction_define", 3, 1, "3l",
        stem="State what friction is and the direction in which it acts.",
        points=[P("a contact force between two surfaces", ["contact force", "between two surfaces", "surfaces in contact", "rubbing"]),
                P("it opposes the relative motion (or attempted motion) of the surfaces", ["opposes", "opposite to the motion", "against the motion", "resists the motion"])],
        model_answer="Friction is a contact force between two surfaces that acts to oppose the relative motion (or attempted motion) of the surfaces.",
        hints=["Where does friction act?", "Which way does it act?", "Define it."],
        keywords="contact force between surfaces; opposes relative motion",
        sample_pass=["A contact force between surfaces that opposes their relative motion", "it is a force between surfaces in contact acting against the motion"],
        sample_fail=["A force that pushes objects forwards", "The weight of an object"])

# ---------------------------------------------------------------- L2
written("w3x_weight_calc_explain", 3, 2, "3e",
        stem="Explain how to find the weight of a 2.5 kg bag on Earth and state its weight (g = 10 N/kg).",
        points=[P("weight = mass × gravitational field strength (W = m g)", ["w = mg", "w = m g", "mass × g", "mass x g", "mass times", "multiply by g"]),
                P("W = 2.5 × 10 = 25 N", ["25 n", "25n", "25 newtons"])],
        model_answer="Weight = mass × gravitational field strength: W = m g = 2.5 × 10 = 25 N.",
        hints=["Which equation links weight and mass?", "Use g = 10 N/kg.", "Give the answer with its unit."],
        keywords="W = m g = 25 N",
        sample_pass=["W = mg = 2.5 × 10 = 25 N", "multiply the mass by g to get 25 N"],
        sample_fail=["2.5 kg", "W = m ÷ g = 0.25 N"])

written("w3x_mass_weight_compare", 3, 2, "3f",
        stem="State two differences between mass and weight.",
        points=[P("mass is the amount of matter; weight is the gravitational force on it", ["amount of matter", "gravitational force", "force of gravity", "pull of gravity"]),
                P("mass is a scalar in kg and constant everywhere; weight is a vector in N and varies with g", ["kg", "newton", "scalar", "vector", "same everywhere", "changes with g", "varies"])],
        model_answer="Mass is the amount of matter in a body, while weight is the gravitational force acting on it. Mass is a scalar measured in kilograms and is the same everywhere; weight is a vector measured in newtons and changes with the gravitational field strength.",
        hints=["What does each one measure?", "Units? Scalar or vector?", "Does each change on the Moon?"],
        keywords="mass: matter, kg, scalar, constant; weight: force, N, vector, depends on g",
        sample_pass=["Mass is the amount of matter in kg and is the same everywhere; weight is the gravitational force in N and changes with g", "mass is the amount of matter and a scalar; weight is the force of gravity, a vector that varies with g"],
        sample_fail=["They are the same", "Mass is measured in newtons and weight in kilograms"])

written("w3x_friction_two_effects", 3, 2, "3l",
        stem="Describe one useful effect and one unwanted effect of friction.",
        points=[P("useful: grip for walking, braking, tyres on roads, holding a nail", ["walk", "brak", "grip", "tyre", "hold", "useful"]),
                P("unwanted: heating and wear in machines, wasting energy", ["heat", "wear", "waste", "energy", "unwanted"])],
        model_answer="Useful: friction between our shoes and the ground lets us walk, and friction lets brakes stop a car. Unwanted: friction in machine parts causes heating and wear and wastes energy.",
        hints=["When do you need friction?", "When is it a problem?", "One of each."],
        keywords="useful: walking, braking, grip; unwanted: heat, wear, wasted energy",
        sample_pass=["It lets us walk without slipping, but it causes wear and heating in engines", "brakes need friction; friction wastes energy as heat in machines"],
        sample_fail=["Friction makes things heavier", "Friction pulls things towards the Earth"])

written("w3x_terminal_two_forces", 3, 2, "3m",
        stem="A raindrop falls at its terminal velocity. Name the two forces on it and compare their sizes.",
        points=[P("weight (downwards) and air resistance (upwards)", ["weight", "air resistance", "drag", "gravity"]),
                P("they are equal in size, so the resultant force is zero", ["equal", "the same size", "balance", "resultant is zero", "zero resultant"])],
        model_answer="Its weight acts downwards and air resistance acts upwards. At terminal velocity they are equal in size, so the resultant force is zero.",
        hints=["Which force pulls it down? Which opposes the motion?", "What does terminal velocity tell you about the forces?", "Compare."],
        keywords="weight and air resistance; equal, resultant zero",
        sample_pass=["Weight and air resistance, which are equal so the resultant is zero", "gravity down and drag up balance each other"],
        sample_fail=["There are no forces on it", "Air resistance is bigger than its weight"])

# ---------------------------------------------------------------- L3
written("w3x_moon_spring_balance", 3, 3, "3e",
        stem="A 2.0 kg mass hangs from a spring balance on Earth and then on the Moon (g = 1.6 N/kg). Explain the two readings.",
        points=[P("on Earth the reading is W = 2.0 × 10 = 20 N", ["20 n", "20n", "2.0 × 10", "2 x 10"]),
                P("on the Moon the reading is 2.0 × 1.6 = 3.2 N", ["3.2 n", "3.2n", "2.0 × 1.6", "2 x 1.6"]),
                P("the spring balance measures weight (force), which depends on g; the mass stays 2.0 kg", ["measures weight", "measures force", "depends on g", "mass stays", "mass is the same"])],
        min_points=2,
        model_answer="A spring balance measures weight, W = m g, which depends on g. On Earth it reads 2.0 × 10 = 20 N; on the Moon it reads 2.0 × 1.6 = 3.2 N. The mass is 2.0 kg in both places.",
        hints=["What does a spring balance measure?", "Use W = m g with each value of g.", "What stays the same?"],
        keywords="spring balance measures weight; 20 N on Earth, 3.2 N on Moon; mass unchanged",
        sample_pass=["It reads 20 N on Earth and 3.2 N on the Moon because it measures weight, which depends on g", "W = mg gives 20 N and 3.2 N; the mass is still 2 kg"],
        sample_fail=["It reads 2 kg in both places", "It reads more on the Moon"])

written("w3x_same_force_two_masses", 3, 3, "3j",
        stem="The same resultant force is applied to a 2 kg trolley and a 4 kg trolley. Explain how their accelerations compare.",
        points=[P("a = F ÷ m", ["a = f / m", "a = f ÷ m", "f = ma", "f = m a", "force divided by mass", "f/m", "a = f/m"]),
                P("the 4 kg trolley has half the acceleration of the 2 kg trolley (double mass, half acceleration)", ["half", "halved", "twice as large", "double the acceleration", "smaller acceleration"])],
        model_answer="From a = F ÷ m, with the same force, doubling the mass halves the acceleration: the 4 kg trolley accelerates at half the rate of the 2 kg trolley.",
        hints=["Rearrange F = m a for a.", "What happens to a if m doubles?", "Compare."],
        keywords="a = F/m; double mass → half acceleration",
        sample_pass=["a = F/m so the 4 kg trolley has half the acceleration", "the heavier trolley accelerates half as much because a = F ÷ m"],
        sample_fail=["They have the same acceleration", "The 4 kg trolley accelerates twice as fast"])

written("w3x_skydiver_start", 3, 3, "3m",
        stem="Explain why a skydiver's acceleration is about 10 m/s² at the moment she jumps but less a few seconds later.",
        points=[P("at the start her speed is zero, so air resistance is (almost) zero and the only force is her weight: a = g", ["speed is zero", "no air resistance", "only weight", "only force is weight", "a = g", "free fall"]),
                P("as she speeds up, air resistance increases, so the resultant force (W − air resistance) decreases", ["air resistance increases", "drag increases", "resultant force decreases", "resultant decreases"]),
                P("a smaller resultant force gives a smaller acceleration (a = F/m)", ["smaller acceleration", "acceleration decreases", "a = f/m", "less acceleration"])],
        min_points=2,
        model_answer="When she jumps her speed is zero, so there is almost no air resistance and the only force is her weight; her acceleration is g, about 10 m/s². As she speeds up, air resistance increases, so the resultant force (weight − air resistance) decreases, and by a = F/m her acceleration decreases.",
        hints=["What is the air resistance at zero speed?", "How does air resistance change as she speeds up?", "How does that affect the resultant force and the acceleration?"],
        keywords="start: only weight, a = g; air resistance grows; resultant and acceleration decrease",
        sample_pass=["At first there is no air resistance so a = g; then air resistance increases, the resultant force decreases and so does the acceleration",
                     "her speed is zero so only her weight acts; later drag increases so the resultant force and acceleration get smaller"],
        sample_fail=["Her weight decreases as she falls", "Gravity gets weaker further from the plane"])

written("w3x_equilibrium_three_forces", 3, 3, "3i",
        stem="Fig. 1 shows a ring held still by three forces. Explain how a scale drawing can be used to check that the forces are in equilibrium.",
        points=[P("draw the forces to scale, tip to tail, in the correct directions", ["to scale", "tip to tail", "head to tail", "scale drawing", "in turn"]),
                P("if the forces are in equilibrium they form a closed triangle", ["closed triangle", "triangle closes", "closes", "returns to the start", "ends where it started"]),
                P("so the resultant force is zero", ["resultant is zero", "zero resultant", "no resultant", "balanced"])],
        min_points=2,
        model_answer="Draw the three forces to scale one after another, tip to tail, each in its correct direction. If the forces are in equilibrium, the last arrow ends exactly where the first began, forming a closed triangle: the resultant force is zero.",
        hints=["How are the forces drawn in a force triangle?", "What shape do balanced forces make?", "What does that mean for the resultant?"],
        keywords="draw to scale tip to tail; closed triangle; resultant zero",
        figure=lambda: figs2.vector_grid([("A", 4, 0), ("B", 0, 3)], nx=8, ny=6, origin=(1, 1)),
        sample_pass=["Draw them to scale tip to tail; if they form a closed triangle the resultant is zero and they are in equilibrium", "a scale drawing of the forces tip to tail closes into a triangle"],
        sample_fail=["Add the three forces as numbers to get zero", "Check that all three forces are the same size"])

written("w3x_hanging_sign_forces", 3, 3, "3i",
        stem="A sign hangs at rest from two ropes. Explain why the tension in each rope can be larger than the weight of the sign.",
        points=[P("the ropes are at an angle, so only part of each tension acts upwards (vertical component)", ["at an angle", "part of the tension", "vertical part", "vertical component", "only part"]),
                P("the upward parts must add up to the weight, so the tensions must be larger when the angle is large (ropes nearly horizontal)", ["add up to the weight", "balance the weight", "larger angle", "nearly horizontal", "flatter", "more tension"])],
        model_answer="The ropes pull at an angle, so only the vertical part of each tension supports the sign. These upward parts must add up to the weight. When the ropes are nearly horizontal the vertical parts are small, so the tensions must be very large; they can exceed the weight.",
        hints=["Do the ropes pull straight up?", "Which part of each tension holds the sign up?", "What happens as the ropes get flatter?"],
        keywords="only vertical part supports the weight; flatter ropes → larger tension",
        sample_pass=["Only the vertical part of each tension holds up the sign, so if the ropes are nearly horizontal the tension must be much larger than the weight", "the ropes are at an angle so part of each tension is wasted sideways; the tension must be bigger to balance the weight"],
        sample_fail=["The ropes get heavier", "Tension can never be larger than the weight"])

# ---------------------------------------------------------------- L4
written("w3x_field_definition", 3, 4, "3c",
        stem="State what is meant by a gravitational field and explain why a satellite in orbit is still in the Earth's gravitational field.",
        points=[P("a region in which a mass experiences a (gravitational) force", ["region", "mass experiences a force", "force on a mass", "a mass feels a force"]),
                P("the Earth's field extends far into space (weakening with distance), so the satellite still experiences a gravitational force which keeps it in orbit", ["extends", "far into space", "weaker", "still pulled", "keeps it in orbit", "gravitational force"])],
        model_answer="A gravitational field is a region in which a mass experiences a gravitational force. The Earth's field extends far into space, becoming weaker with distance, so a satellite in orbit still experiences a gravitational force towards the Earth; that force keeps it moving in its orbit.",
        hints=["Define a field in terms of a force on something.", "Does the Earth's field stop at the atmosphere?", "Why doesn't the satellite fly off?"],
        keywords="region where a mass experiences a force; field extends into space; force keeps satellite in orbit",
        sample_pass=["A region where a mass experiences a force; the field extends into space so the satellite is still pulled towards the Earth", "a region in which masses feel a gravitational force, which still acts on the satellite and keeps it in orbit"],
        sample_fail=["A region with air in it", "There is no gravity in space"])

written("w3x_pushing_wall", 3, 4, "3g",
        stem="A girl on roller skates pushes against a wall and moves away from it. Explain this using Newton's laws.",
        points=[P("she exerts a force on the wall; the wall exerts an equal and opposite force on her (third law)", ["equal and opposite", "wall pushes back", "wall pushes her", "third law", "reaction"]),
                P("this is the only (or resultant) horizontal force on her, so she accelerates away from the wall", ["resultant force", "unbalanced", "accelerates", "f = ma", "moves away"]),
                P("the wall does not move because it is fixed to the ground (huge effective mass / balanced by other forces)", ["wall does not move", "fixed", "huge mass", "attached", "balanced"])],
        min_points=2,
        model_answer="She pushes on the wall, and by Newton's third law the wall pushes back on her with an equal and opposite force. That force is the resultant horizontal force on her (friction on skates is small), so she accelerates away from the wall. The wall does not move because it is fixed to the building and ground.",
        hints=["What does the wall do when she pushes it?", "What is the resultant force on her?", "Why doesn't the wall move?"],
        keywords="third law: wall pushes back; resultant force on her → she accelerates",
        sample_pass=["The wall pushes back on her with an equal and opposite force, which is the resultant force on her, so she accelerates away", "by the third law the wall pushes her, an unbalanced force, so she moves away"],
        sample_fail=["Her pushing force pushes herself away", "The wall moves towards her"])

written("w3x_box_rough_floor", 3, 4, "3l",
        stem="A box is given a push and then slides across a rough floor. Describe and explain its motion after the push stops.",
        points=[P("after the push stops, friction is the only horizontal force (opposing the motion)", ["only horizontal force", "only friction", "friction acts against", "friction opposes"]),
                P("this resultant backward force gives a deceleration (a = F/m)", ["decelerat", "slows down", "resultant force backwards", "f = ma", "unbalanced"]),
                P("the box slows down and comes to rest, after which friction stops acting", ["comes to rest", "stops", "then stationary", "until it stops"])],
        min_points=2,
        model_answer="After the push stops, friction is the only horizontal force on the box, acting opposite to its motion. This resultant force gives the box a deceleration (a = F/m), so the box slows down and comes to rest; once it is at rest, friction no longer acts.",
        hints=["Which horizontal forces act after the push stops?", "What does an unbalanced force do?", "What finally happens?"],
        keywords="only friction acts; resultant backward force → deceleration; comes to rest",
        sample_pass=["Friction is the only horizontal force, so there is a resultant force backwards and the box decelerates until it stops", "friction opposes the motion so the box slows down and comes to rest"],
        sample_fail=["It keeps moving at constant speed", "It speeds up because of its inertia"])

written("w3x_parachute_stages", 3, 4, "3m",
        stem="A parachutist falls at terminal velocity and then opens her parachute. Describe and explain how her velocity changes until she reaches a new terminal velocity.",
        points=[P("opening the parachute greatly increases air resistance, so it becomes larger than her weight", ["air resistance increases", "drag increases", "larger than her weight", "bigger than the weight"]),
                P("the resultant force is upwards, so she decelerates", ["resultant force upwards", "decelerat", "slows down"]),
                P("as she slows, air resistance decreases until it again equals her weight: a new, lower terminal velocity", ["air resistance decreases", "equals her weight", "lower terminal velocity", "smaller terminal velocity", "new terminal velocity"])],
        min_points=2,
        model_answer="Opening the parachute greatly increases air resistance, so it becomes larger than her weight. The resultant force is upwards and she decelerates. As she slows down, air resistance decreases until it again equals her weight, and she falls at a new, lower terminal velocity.",
        hints=["What does opening the parachute do to air resistance?", "What is the direction of the resultant force?", "What happens to air resistance as she slows?"],
        keywords="drag > weight → deceleration; drag falls as she slows; new lower terminal velocity",
        sample_pass=["Air resistance becomes larger than her weight so she decelerates, then the air resistance decreases until it equals her weight at a lower terminal velocity",
                     "drag increases, the resultant force is upwards so she slows down to a new smaller terminal velocity where the forces balance"],
        sample_fail=["She shoots upwards", "Her weight decreases when the parachute opens"])

# ---------------------------------------------------------------- L5
written("w3x_eval_astronaut_mass", 3, 5, "3f",
        stem="An astronaut says: 'On the Moon I am lighter, so I have less mass and it is easier to stop me when I run.' Evaluate.",
        points=[P("partly wrong: she has less weight (smaller g), but her mass is unchanged", ["mass is unchanged", "same mass", "mass does not change", "less weight"]),
                P("inertia depends on mass, so she is just as hard to stop (same force needed for the same deceleration, F = m a)", ["inertia", "just as hard", "same force", "f = ma", "same mass"])],
        model_answer="The claim is partly wrong. Her weight is less on the Moon because g is smaller, but her mass is unchanged. Inertia depends on mass, so stopping her needs the same force for the same deceleration (F = m a): she is just as hard to stop.",
        hints=["Which changes on the Moon: mass or weight?", "What property decides how hard it is to stop her?", "Judge both parts of the claim."],
        keywords="weight less, mass same; inertia depends on mass; same F for same deceleration",
        sample_pass=["Her weight is less but her mass is the same, so her inertia is the same and she is just as hard to stop", "wrong about mass: mass does not change, and by F = ma the same force is needed"],
        sample_fail=["Correct, lighter means less mass", "She has no mass on the Moon"])

written("w3x_eval_third_law_cancel", 3, 5, "3g",
        stem="A student says: 'When I push a box, the box pushes back on me with an equal force, so the forces cancel and the box can never move.' Evaluate.",
        points=[P("wrong: the two forces act on different objects (one on the box, one on the student)", ["different objects", "different bodies", "one on the box", "on me"]),
                P("forces can only cancel when they act on the same object; the box moves if the resultant force ON THE BOX (push − friction) is not zero", ["same object", "resultant force on the box", "friction", "unbalanced", "forces on the box"])],
        model_answer="The student is wrong. The action and reaction act on different objects: one on the box and one on the student, so they cannot cancel. Whether the box moves depends only on the forces on the box: if the push is bigger than friction, the resultant force on the box is not zero and it accelerates.",
        hints=["Which object does each force act on?", "Can forces on different objects cancel?", "What decides whether the box moves?"],
        keywords="different objects, can't cancel; box moves if resultant force on box ≠ 0",
        sample_pass=["Wrong, the forces act on different objects so they cannot cancel; the box moves if the push is bigger than friction", "incorrect, the forces act on different objects; only forces on the same object cancel, and the resultant force on the box is not zero"],
        sample_fail=["Correct, nothing can ever be moved", "The box pushes back with a smaller force"])

written("w3x_eval_tyres_friction", 3, 5, "3l",
        stem="A student suggests making car tyres completely smooth to reduce friction and save fuel. Evaluate the suggestion.",
        points=[P("smooth tyres would reduce rolling resistance a little, but reduce grip", ["reduce grip", "less grip", "lose grip", "less friction with the road"]),
                P("friction between tyres and road is needed to accelerate, brake and turn; without it the car would skid", ["brak", "accelerate", "turn", "skid", "slip", "steer"]),
                P("in wet conditions treads are needed to remove water; smooth tyres are dangerous", ["wet", "water", "treads", "aquaplan", "dangerous", "unsafe"])],
        min_points=2,
        model_answer="The suggestion is unsafe. Smooth tyres might reduce rolling resistance slightly, but they would reduce grip. Friction between the tyres and the road is what lets the car accelerate, brake and turn; with too little grip the car skids. In wet conditions, treads are needed to push water away, so smooth tyres would be dangerous.",
        hints=["What is friction between tyres and road used for?", "What happens on a wet road?", "Weigh the fuel saving against safety."],
        keywords="less grip; friction needed to accelerate, brake, turn; treads clear water; unsafe",
        sample_pass=["Bad idea: friction is needed to brake and turn, so smooth tyres would skid, especially in the wet where treads remove water", "it saves a little fuel but the car would lose grip and be unable to brake safely"],
        sample_fail=["Good idea, friction is always wasteful", "Smooth tyres give more grip"])

written("w3x_eval_heavy_parachute", 3, 5, "3m",
        stem="A student says two skydivers of different mass, in the same position, must reach the same terminal velocity because 'gravity pulls everything equally'. Evaluate.",
        points=[P("wrong: g is the same, but the heavier diver has a larger weight", ["larger weight", "heavier diver has more weight", "weight is larger", "more weight"]),
                P("terminal velocity is reached when air resistance equals weight; air resistance increases with speed", ["air resistance equals weight", "drag equals weight", "increases with speed", "balances the weight"]),
                P("so the heavier diver must fall faster to produce the larger air resistance: higher terminal velocity", ["fall faster", "higher terminal velocity", "greater terminal velocity", "larger terminal velocity"])],
        min_points=2,
        model_answer="The claim is wrong. Gravity gives every kilogram the same force, but the heavier diver has a larger total weight. Terminal velocity is reached when air resistance equals weight, and air resistance increases with speed. The heavier diver must therefore fall faster before air resistance becomes large enough, so his terminal velocity is higher.",
        hints=["Is the weight the same for both?", "What condition gives terminal velocity?", "How does air resistance depend on speed?"],
        keywords="wrong; heavier → bigger weight; drag must equal weight; drag rises with speed → higher terminal velocity",
        sample_pass=["Wrong, the heavier diver has a larger weight so needs more air resistance, which means falling faster, so a higher terminal velocity", "incorrect, terminal velocity is when drag equals weight, and the heavier one has more weight so must go faster"],
        sample_fail=["Correct, they fall at the same speed", "The lighter diver reaches a higher terminal velocity"])
