"""Chapter 7 Kinetic Particle Model of Matter written-answer bank extension: fills each level to at least 10 with every LO at least twice."""
from .. import figs2
from ..marker import Pitfall, Point
from .base import written

P = Point
PF = Pitfall

# ---------------------------------------------------------------- L1
written("w7x_temp_cool_ke", 7, 1, "7d",
        stem="A hot drink cools down. State what happens to the average kinetic energy of its particles.",
        points=[P("the average kinetic energy decreases", ["decreases", "decrease", "falls", "goes down", "lower", "less", "reduces"]),
                P("the particles move more slowly on average", ["slower", "more slowly", "slow down", "move less"])],
        pitfalls=[PF(["increases"], "Cooling LOWERS the average kinetic energy.")],
        model_answer="The average kinetic energy of the particles decreases: they move more slowly on average.",
        hints=["Cooling means a falling temperature.", "Temperature is linked to average KE.", "Faster or slower?"],
        keywords="average KE decreases; particles slower",
        sample_pass=["The average kinetic energy decreases as the particles move more slowly", "it falls, the particles slow down"],
        sample_fail=["It increases", "The particles get smaller"])

written("w7x_three_states_shape", 7, 1, "7a",
        stem="State whether a solid, a liquid and a gas each have a fixed shape and a fixed volume.",
        points=[P("solid: fixed shape and fixed volume", ["solid fixed shape", "solid has a fixed shape", "solid: fixed shape", "solid both", "solid has fixed shape and volume"]),
                P("liquid: fixed volume but no fixed shape", ["liquid fixed volume", "liquid has a fixed volume", "liquid: fixed volume", "liquid takes the shape"]),
                P("gas: neither fixed shape nor fixed volume", ["gas has neither", "gas: neither", "gas no fixed", "gas has no fixed", "gas neither"])],
        min_points=3,
        model_answer="A solid has a fixed shape and a fixed volume. A liquid has a fixed volume but no fixed shape. A gas has neither a fixed shape nor a fixed volume.",
        hints=["Which state can be poured?", "Which state fills any container?", "Go through each state."],
        keywords="solid: both fixed; liquid: volume fixed; gas: neither",
        sample_pass=["Solid has a fixed shape and volume, liquid has a fixed volume but takes the shape of its container, gas has neither", "solid: fixed shape and volume; liquid: fixed volume only; gas: neither"],
        sample_fail=["All three have a fixed volume", "Gas has a fixed shape"])

written("w7x_gas_compress_l1", 7, 1, "7a",
        stem="A syringe full of air can be pushed in easily, but a syringe full of water cannot. State what this shows about gases and liquids.",
        points=[P("gases can be compressed (are compressible)", ["gas can be compressed", "gases can be compressed", "gas is compressible", "gases are compressible", "air can be compressed", "air is compressible"]),
                P("liquids are almost incompressible", ["liquid cannot be compressed", "liquids cannot be compressed", "incompressible", "water cannot be compressed", "hardly compressed", "liquids are not compressible"])],
        model_answer="Gases can be compressed easily, but liquids are almost incompressible.",
        hints=["What happens to the air?", "What happens to the water?", "Use the word 'compressed'."],
        keywords="gases compressible; liquids almost incompressible",
        sample_pass=["Gases can be compressed but liquids are incompressible", "air is compressible and water cannot be compressed"],
        sample_fail=["Water is heavier", "Air is lighter"])

written("w7x_brownian_what_seen", 7, 1, "7c",
        stem="Fig. 1 shows a smoke cell viewed through a microscope. Describe what is seen.",
        points=[P("bright specks (smoke particles)", ["bright specks", "smoke particles", "specks of light", "bright spots", "points of light"]),
                P("moving in a random, zig-zag way", ["random", "zig-zag", "zigzag", "jerky", "irregular"])],
        model_answer="Tiny bright specks of light (smoke particles reflecting light) are seen moving about in a random, zig-zag way.",
        hints=["What reflects the light?", "How do they move?", "Random and zig-zag."],
        keywords="bright specks; random zig-zag motion",
        sample_pass=["Bright specks moving randomly in a zig-zag", "smoke particles moving in a jerky, random way"],
        sample_fail=["Air molecules moving in straight lines", "Smoke rising steadily"],
        figure=lambda: figs2.brownian_cell(4))

written("w7x_brownian_cause_l1", 7, 1, "7c",
        stem="State what causes the random motion of smoke particles in a smoke cell.",
        points=[P("collisions with air molecules", ["collisions with air molecules", "air molecules collide", "hit by air molecules", "bombarded by air", "air molecules hit", "collide with air"]),
                P("the air molecules are moving randomly at high speed / the impacts are uneven", ["random", "high speed", "fast", "uneven", "unequal", "from all directions"])],
        model_answer="The smoke particles are hit by fast-moving, randomly moving air molecules; the impacts are uneven, so the smoke particles are pushed about randomly.",
        hints=["What surrounds the smoke particles?", "Are those particles moving?", "What do they do to the smoke?"],
        keywords="uneven collisions with fast, random air molecules",
        sample_pass=["Air molecules collide with them unevenly from all directions", "they are hit by fast moving air molecules at random"],
        sample_fail=["Convection currents", "The smoke is hot"])

written("w7x_gas_pressure_l1", 7, 1, "7e",
        stem="Explain how a gas exerts a pressure on the walls of its container.",
        points=[P("the gas molecules collide with (hit) the walls", ["collide with the walls", "hit the walls", "collisions with the walls", "bounce off the walls", "strike the walls"]),
                P("each collision exerts a force on the wall; force per unit area is pressure", ["force", "per unit area", "push on the wall", "exert a force"])],
        model_answer="The gas molecules move rapidly and collide with the walls. Each collision exerts a small force on the wall, and the total force per unit area is the pressure.",
        hints=["What do gas molecules do?", "What happens when one hits the wall?", "Pressure = force ÷ area."],
        keywords="molecules collide with walls; force per unit area",
        sample_pass=["The molecules collide with the walls and exert a force, giving force per unit area", "they hit the walls, which pushes on the wall"],
        sample_fail=["The gas is heavy", "The molecules are attracted to the walls"])

written("w7x_pump_tyre", 7, 1, "7e",
        stem="Explain why pumping more air into a tyre increases the pressure inside it (temperature constant).",
        points=[P("there are more air molecules in the tyre", ["more molecules", "more air molecules", "more particles", "more air particles"]),
                P("so there are more collisions with the walls per second", ["more collisions", "collide more often", "hit the walls more often", "more frequent collisions", "more often"])],
        model_answer="Pumping adds more air molecules to the tyre, so there are more collisions with each area of the tyre wall per second, increasing the pressure.",
        hints=["What does pumping add?", "What happens to the collisions?", "Link to pressure."],
        keywords="more molecules → more collisions per second",
        sample_pass=["There are more molecules so more collisions with the walls per second", "more air particles hit the walls more often"],
        sample_fail=["The molecules move faster", "The air expands"])

# ---------------------------------------------------------------- L2
written("w7x_liquid_volume_fixed", 7, 2, "7a",
        stem="Explain, using the particle model, why a liquid has a fixed volume but takes the shape of its container.",
        points=[P("the particles are close together, held by attractive forces (fixed volume)", ["close together", "attractive forces", "held together", "forces of attraction", "close to each other"]),
                P("the particles can move past each other (no fixed shape)", ["move past", "slide past", "move around", "move freely past", "not fixed"])],
        model_answer="The particles of a liquid are close together and held by attractive forces, so the volume is fixed. They are not in fixed positions and can slide past one another, so the liquid takes the shape of its container.",
        hints=["How close are the particles?", "What holds them together?", "Can they move past each other?"],
        keywords="close, attractive forces → fixed volume; slide past → takes shape",
        sample_pass=["The particles are close together with attractive forces, but they can slide past each other", "held together closely but able to move past one another"],
        sample_fail=["The particles are far apart", "The particles are fixed in place"])

written("w7x_brownian_evidence", 7, 2, "7c",
        stem="Explain what Brownian motion tells us about the particles of a gas or liquid.",
        points=[P("the fluid is made of tiny particles (molecules) too small to see", ["tiny", "too small to see", "invisible", "small particles", "molecules"]),
                P("the particles are in constant, random motion", ["random motion", "constantly moving", "moving randomly", "constant motion", "always moving", "move randomly"])],
        model_answer="It shows that a gas or liquid is made of tiny particles, too small to see, which are in constant random motion and collide with the larger visible particles.",
        hints=["What pushes the visible specks?", "Can we see it?", "How must it be moving?"],
        keywords="tiny invisible particles; constant random motion",
        sample_pass=["It shows the fluid is made of tiny molecules in constant random motion", "there are invisible particles that are always moving randomly"],
        sample_fail=["It shows smoke is alive", "It shows air is still"])

written("w7x_brownian_small_specks", 7, 2, "7c",
        stem="Explain why very small smoke particles show more vigorous Brownian motion than larger ones.",
        points=[P("fewer molecules hit a small particle at any instant, so the impacts are more uneven", ["fewer molecules", "fewer collisions", "more uneven", "less balanced", "do not cancel", "unbalanced"]),
                P("a small particle has less mass, so it is moved more by each impact", ["less mass", "smaller mass", "lighter", "moved more easily", "accelerates more"])],
        model_answer="At any instant fewer air molecules hit a small particle, so the impacts on different sides are more unbalanced. A small particle also has less mass, so these unbalanced pushes move it more.",
        hints=["How many molecules hit each speck at once?", "Do the pushes cancel?", "Does mass matter?"],
        keywords="fewer, unbalanced impacts; less mass",
        sample_pass=["Fewer molecules hit it so the forces are unbalanced, and it has less mass", "the collisions are more uneven and the lighter particle moves more easily"],
        sample_fail=["Small particles are hotter", "Small particles are pulled by gravity"])

written("w7x_temp_two_beakers", 7, 2, "7d",
        stem="Beaker A contains water at 30 °C and beaker B contains water at 70 °C. Compare the motion of the water molecules in the two beakers.",
        points=[P("molecules in B move faster on average", ["b move faster", "b faster", "faster in b", "b are faster", "70 °c move faster", "hotter move faster"]),
                P("so they have a greater average kinetic energy", ["greater average kinetic energy", "more kinetic energy", "higher average kinetic energy", "larger kinetic energy", "greater kinetic energy"])],
        model_answer="The molecules in B (70 °C) move faster on average than those in A, so they have a greater average kinetic energy.",
        hints=["Which beaker is hotter?", "How does temperature affect speed?", "Link to kinetic energy."],
        keywords="B faster; greater average KE",
        sample_pass=["The molecules in B move faster and have a greater average kinetic energy", "faster in B, so more kinetic energy"],
        sample_fail=["They move the same", "The molecules in A move faster"])

written("w7x_thermometer_meaning", 7, 2, "7d",
        stem="State what a rise in temperature of a body tells us about its particles.",
        points=[P("the average kinetic energy of the particles has increased", ["average kinetic energy", "kinetic energy increases", "more kinetic energy", "increase in kinetic energy", "greater kinetic energy"]),
                P("the particles move (or vibrate) faster on average", ["faster", "more quickly", "vibrate more", "speed up", "move more"])],
        model_answer="A rise in temperature means the average kinetic energy of the particles has increased: they move or vibrate faster on average.",
        hints=["What does temperature measure?", "Average kinetic energy.", "Faster or slower?"],
        keywords="average KE increases; particles faster",
        sample_pass=["The average kinetic energy of the particles increases; they move faster", "the particles vibrate faster, so more kinetic energy"],
        sample_fail=["The particles get bigger", "There are more particles"])

written("w7x_volume_pressure", 7, 2, "7e",
        stem="A gas is slowly squashed into half its volume at constant temperature. Explain why its pressure increases.",
        points=[P("the same number of molecules are in a smaller space", ["smaller space", "smaller volume", "less space", "closer together", "same number"]),
                P("so they hit each area of the walls more often", ["more often", "more frequent", "more collisions", "collide more", "hit the walls more"])],
        pitfalls=[PF(["move faster"], "At constant temperature the molecules do NOT speed up; they hit the walls more often.")],
        model_answer="The same number of molecules is now in a smaller space, moving at the same speed, so they hit each area of the walls more often, which increases the pressure.",
        hints=["Is the temperature constant?", "What changes about the space?", "How often do molecules hit the walls?"],
        keywords="same molecules, smaller volume → more frequent collisions",
        sample_pass=["The molecules are in a smaller space so they hit the walls more often", "less space means more collisions with the walls per second"],
        sample_fail=["The molecules move faster", "The molecules become smaller"])

written("w7x_heat_can_pressure", 7, 2, "7e",
        stem="A sealed rigid can of gas is heated. Explain why its pressure increases.",
        points=[P("the molecules gain kinetic energy and move faster", ["move faster", "faster", "more kinetic energy", "gain kinetic energy", "speed up"]),
                P("they hit the walls more often and with more force", ["more often", "harder", "more force", "greater force", "more frequent", "more collisions"])],
        model_answer="Heating gives the molecules more kinetic energy, so they move faster. They hit the walls more often and with more force, so the pressure increases.",
        hints=["What happens to the molecules' speed?", "How do the collisions change?", "Two effects."],
        keywords="faster molecules; more frequent, harder collisions",
        sample_pass=["The molecules move faster and hit the walls more often and harder", "they gain kinetic energy so there are more collisions with greater force"],
        sample_fail=["The molecules expand", "The can shrinks"])

# ---------------------------------------------------------------- L3
written("w7x_melting_temp_constant", 7, 3, "7d",
        stem="While a solid melts at its melting point, energy is supplied but the temperature stays constant. Explain what this tells you about the average kinetic energy of the particles.",
        points=[P("the average kinetic energy stays the same", ["stays the same", "does not change", "constant", "unchanged", "remains the same"]),
                P("the energy is used to break the bonds / overcome the forces between particles", ["break", "overcome", "forces between", "bonds", "attractive forces", "potential energy"])],
        pitfalls=[PF(["kinetic energy increases"], "The temperature is constant, so the average KE does not change.")],
        model_answer="The average kinetic energy of the particles stays the same, because the temperature is constant. The energy supplied is used to break the bonds and overcome the attractive forces between the particles.",
        hints=["Temperature measures average KE.", "Is the temperature changing?", "Where does the energy go?"],
        keywords="average KE constant; energy breaks bonds",
        sample_pass=["The average kinetic energy stays the same; the energy is used to break the bonds between particles", "it does not change because the energy overcomes the forces between the particles"],
        sample_fail=["The kinetic energy increases", "The particles stop moving"])

written("w7x_gas_compressible_explain", 7, 3, "7a",
        stem="Explain, using the particle model, why gases are much easier to compress than solids.",
        points=[P("gas particles are far apart with large spaces between them", ["far apart", "large spaces", "lots of space", "big gaps", "large gaps"]),
                P("solid particles are closely packed with almost no space", ["closely packed", "close together", "no space", "touching", "little space"])],
        model_answer="The particles in a gas are far apart with large spaces between them, so they can be pushed closer together. The particles in a solid are already closely packed with almost no space between them.",
        hints=["How far apart are gas particles?", "How about solid particles?", "Space to squeeze into."],
        keywords="gas: far apart, large spaces; solid: closely packed",
        sample_pass=["Gas particles are far apart with large spaces but solid particles are closely packed", "there is lots of space between gas particles while solid particles are touching"],
        sample_fail=["Gas particles are softer", "Solid particles are larger"])

written("w7x_evaporation_vs_boiling", 7, 3, "7a",
        stem="State two differences between evaporation and boiling.",
        points=[P("evaporation happens at any temperature; boiling at a fixed temperature (the boiling point)", ["any temperature", "all temperatures", "boiling point", "fixed temperature"]),
                P("evaporation happens only at the surface; boiling happens throughout the liquid", ["surface", "throughout", "bubbles"])],
        model_answer="Evaporation happens at any temperature, but boiling happens only at the boiling point. Evaporation takes place only at the surface, while boiling takes place throughout the liquid, forming bubbles.",
        hints=["At what temperature does each happen?", "Where in the liquid?", "Two differences."],
        keywords="any temp vs boiling point; surface vs throughout",
        sample_pass=["Evaporation happens at any temperature and only at the surface; boiling happens at the boiling point and throughout the liquid", "boiling forms bubbles throughout at a fixed temperature, evaporation is at the surface at all temperatures"],
        sample_fail=["They are the same", "Boiling is slower"])

written("w7x_brownian_warm", 7, 3, "7c",
        stem="A smoke cell is gently warmed. Predict and explain how the motion of the smoke particles changes.",
        points=[P("the smoke particles move more vigorously (faster)", ["more vigorous", "more vigorously", "faster", "more rapidly", "jiggle more"]),
                P("because the air molecules move faster and hit them harder or more often", ["air molecules move faster", "molecules move faster", "hit harder", "more often", "greater force", "more energetic"])],
        model_answer="The smoke particles move more vigorously, because the warmer air molecules move faster and hit them harder and more often.",
        hints=["What does warming do to air molecules?", "How does that affect the collisions?", "So how do the smoke particles move?"],
        keywords="more vigorous; air molecules faster, harder collisions",
        sample_pass=["They move more vigorously because the air molecules move faster and hit them harder", "faster motion, since the molecules are more energetic and collide more often"],
        sample_fail=["They stop", "They rise because hot air rises"])

written("w7x_brownian_setup", 7, 3, "7c",
        stem="Describe how Brownian motion can be observed using a smoke cell.",
        points=[P("fill a small glass cell with smoke and seal it", ["smoke", "cell", "glass", "seal"]),
                P("light it from the side and view through a microscope", ["light", "lamp", "illuminate", "microscope"]),
                P("observe bright specks moving randomly", ["bright specks", "randomly", "random", "zig-zag", "jerky"])],
        min_points=2,
        model_answer="Smoke is put into a small glass cell, which is then covered. The cell is lit strongly from the side and viewed through a microscope; tiny bright specks (smoke particles) are seen moving randomly in a zig-zag way.",
        hints=["What goes in the cell?", "How is it lit and viewed?", "What is seen?"],
        keywords="smoke in glass cell; side light + microscope; bright specks moving randomly",
        sample_pass=["Put smoke in a glass cell, light it from the side and look through a microscope to see bright specks moving randomly", "use a microscope and a lamp to view the smoke cell; the specks move in a zig-zag"],
        sample_fail=["Heat some water", "Weigh the smoke"])

written("w7x_balloon_cold", 7, 3, "7e",
        stem="A balloon is taken from a warm room into a cold freezer. Explain why it shrinks.",
        points=[P("the gas molecules lose kinetic energy and move more slowly", ["move more slowly", "slower", "less kinetic energy", "lose kinetic energy", "slow down"]),
                P("they hit the balloon wall less often and with less force, so the pressure inside falls", ["less often", "less force", "fewer collisions", "pressure falls", "pressure decreases", "lower pressure"]),
                P("the outside pressure pushes the balloon smaller until the pressures balance", ["outside pressure", "atmospheric pressure", "pushes in", "balance", "squashes"])],
        min_points=2,
        model_answer="The molecules lose kinetic energy and move more slowly, so they hit the balloon wall less often and with less force; the pressure inside falls. The air pressure outside then pushes the balloon smaller until the pressures balance.",
        hints=["What happens to the molecules' speed?", "How does that change the collisions?", "What then happens to the balloon?"],
        keywords="slower molecules; fewer, weaker collisions; outside pressure shrinks balloon",
        sample_pass=["The molecules move more slowly and hit the wall less often, so the pressure falls and the outside pressure squashes it", "they lose kinetic energy, there are fewer collisions, the pressure decreases"],
        sample_fail=["The molecules shrink", "The air leaks out"])

written("w7x_syringe_block_heat", 7, 3, "7e",
        stem="The nozzle of a syringe of air is blocked and the plunger is held still. The syringe is placed in hot water. Explain what happens to the pressure of the air.",
        points=[P("the pressure increases", ["increases", "rises", "higher", "goes up", "greater"]),
                P("the molecules move faster and hit the walls more often and harder", ["move faster", "faster", "more often", "harder", "more force", "more collisions"])],
        model_answer="The pressure increases: the molecules gain kinetic energy and move faster, so they hit the walls and plunger more often and with greater force.",
        hints=["The volume is fixed.", "What happens to the molecules' speed?", "How do collisions change?"],
        keywords="pressure increases; faster, more frequent, harder collisions",
        sample_pass=["The pressure increases because the molecules move faster and hit the walls more often", "it rises, the molecules collide harder and more often"],
        sample_fail=["The pressure decreases", "Nothing happens"])

# ---------------------------------------------------------------- L4
written("w7x_states_forces_spacing", 7, 4, "7a",
        stem="Use the arrangement and forces between particles to explain why a solid cannot be poured but a liquid can.",
        points=[P("in a solid, strong forces hold particles in fixed positions", ["fixed positions", "strong forces", "held in place", "regular pattern", "cannot move past"]),
                P("in a liquid, particles can slide past each other (forces weaker)", ["slide past", "move past", "weaker forces", "not fixed", "move around"])],
        model_answer="In a solid, strong attractive forces hold the particles in fixed positions in a regular pattern, so they cannot move past each other and the solid cannot flow. In a liquid the forces are weaker and the particles can slide past one another, so it can be poured.",
        hints=["How are solid particles held?", "What can liquid particles do?", "Link to flowing."],
        keywords="solid: fixed positions, strong forces; liquid: slide past",
        sample_pass=["Solid particles are held in fixed positions by strong forces, but liquid particles can slide past each other", "in a liquid the particles move past one another; in a solid they are held in fixed positions"],
        sample_fail=["Solids are heavier", "Liquids are hotter"])

written("w7x_sublimation_freezer", 7, 4, "7a",
        stem="Ice cubes in a freezer at −18 °C slowly shrink over several weeks, although they never melt. Explain this using the particle model.",
        points=[P("some molecules at the surface have enough energy to escape", ["enough energy", "escape", "break free", "leave the surface", "most energetic"]),
                P("they change directly from solid to water vapour", ["directly", "water vapour", "vapour", "gas", "sublime", "sublimation"])],
        model_answer="Even below 0 °C, some molecules at the surface of the ice have enough energy to break free and escape, changing directly from solid ice to water vapour, so the ice cubes slowly lose mass and shrink.",
        hints=["Do all molecules have the same energy?", "Can some escape from the surface?", "Into what state?"],
        keywords="energetic surface molecules escape; solid → vapour directly",
        sample_pass=["Some molecules at the surface have enough energy to escape and become water vapour directly", "the most energetic molecules leave the surface and turn straight into vapour"],
        sample_fail=["The ice melts slowly", "The ice molecules shrink in the cold"])

written("w7x_brownian_larger_less", 7, 4, "7c",
        stem="Explain why Brownian motion is not seen for large objects such as a table-tennis ball floating on water.",
        points=[P("very many molecules hit the ball at the same time from all sides", ["many molecules", "very many", "huge number", "from all sides", "all directions"]),
                P("so the forces almost balance/cancel", ["balance", "cancel", "even out", "average out", "almost equal"]),
                P("and its large mass means any small unbalanced force has little effect", ["large mass", "heavy", "massive", "little effect", "hardly moves"])],
        min_points=2,
        model_answer="Very many water molecules hit the ball at the same time from all sides, so their forces almost cancel out. The ball's large mass also means any small unbalanced force produces almost no movement.",
        hints=["How many molecules hit it at once?", "Do the forces cancel?", "Does mass matter?"],
        keywords="many impacts from all sides cancel; large mass",
        sample_pass=["So many molecules hit it from all sides that the forces cancel, and it has a large mass", "the collisions balance out and it is too heavy to be moved noticeably"],
        sample_fail=["Water molecules do not hit large objects", "The ball is too smooth"])

written("w7x_brownian_conclusions", 7, 4, "7c",
        stem="State two conclusions about air molecules that can be drawn from the smoke-cell experiment, and the observation that supports each.",
        points=[P("air molecules move randomly — the smoke moves in random directions", ["random"]),
                P("air molecules are very small / invisible — they cannot be seen though they move the smoke", ["small", "invisible", "cannot be seen", "too small"]),
                P("air molecules move fast — the smoke particles are pushed about rapidly/vigorously", ["fast", "high speed", "rapidly", "vigorous", "quickly"])],
        min_points=2,
        model_answer="Air molecules move randomly, because the smoke particles move in random, changing directions. Air molecules are very small, because they cannot be seen even though they push the smoke about. They also move fast, since they push much heavier smoke particles vigorously.",
        hints=["How do the specks move?", "Can you see the air molecules?", "What does each tell you?"],
        keywords="random (random path); tiny (invisible); fast (vigorous)",
        sample_pass=["Air molecules move randomly since the smoke moves randomly, and they are too small to see", "they are invisible but move fast, because the smoke is pushed about vigorously"],
        sample_fail=["Air is hot", "Smoke is heavier than air"])

written("w7x_evaporation_cooling", 7, 4, "7d",
        stem="Sweat evaporating from the skin cools the body. Explain this using the kinetic particle model.",
        points=[P("the most energetic (fastest) molecules escape from the surface", ["most energetic", "fastest", "higher kinetic energy", "more energetic", "faster molecules escape"]),
                P("so the average kinetic energy of the remaining molecules falls", ["average kinetic energy falls", "average kinetic energy decreases", "lower average", "remaining molecules", "average decreases"]),
                P("so the temperature of the sweat falls and it absorbs energy from the skin", ["temperature falls", "cooler", "takes energy", "absorbs energy", "from the skin", "cools"])],
        min_points=2,
        model_answer="The most energetic molecules escape from the surface of the sweat, so the average kinetic energy of the remaining molecules falls and the sweat becomes cooler. It then absorbs thermal energy from the skin, cooling the body.",
        hints=["Which molecules escape?", "What happens to the average KE of those left?", "Link to temperature and the skin."],
        keywords="fastest escape; average KE of rest falls; takes energy from skin",
        sample_pass=["The most energetic molecules escape so the average kinetic energy of the remaining ones falls and it takes energy from the skin", "the fastest molecules leave, lowering the average; the sweat cools and absorbs energy from the skin"],
        sample_fail=["Sweat is cold", "The molecules get smaller"])

written("w7x_same_temp_different_states", 7, 4, "7d",
        stem="Water at 100 °C and steam at 100 °C are compared. Explain whether their molecules have the same average kinetic energy, and how the molecules differ.",
        points=[P("yes, the same average kinetic energy (same temperature)", ["same average kinetic energy", "same kinetic energy", "same temperature", "equal kinetic energy", "same average"]),
                P("steam molecules are much further apart (more potential energy, weaker forces)", ["further apart", "far apart", "more potential energy", "weaker forces", "more space"])],
        model_answer="Their molecules have the same average kinetic energy because they are at the same temperature. The steam molecules are much further apart, with very weak forces between them (they have more potential energy).",
        hints=["What sets average KE?", "Are the temperatures the same?", "How does the spacing differ?"],
        keywords="same average KE; steam far apart / more PE",
        sample_pass=["They have the same average kinetic energy since the temperature is the same, but steam molecules are further apart", "same kinetic energy; the steam molecules have more potential energy because they are far apart"],
        sample_fail=["Steam has more kinetic energy because it is a gas", "Water molecules are larger"])

written("w7x_pressure_two_changes", 7, 4, "7e",
        stem="A fixed mass of gas is heated while its volume is allowed to increase so that its pressure stays the same. Explain how this is possible in terms of molecules.",
        points=[P("heating makes the molecules move faster, hitting the walls harder", ["faster", "harder", "more force", "more kinetic energy"]),
                P("the larger volume means they hit each area of the wall less often", ["less often", "less frequently", "fewer collisions", "larger volume", "more space"]),
                P("the two effects cancel so the pressure is unchanged", ["cancel", "balance", "same pressure", "pressure stays the same", "unchanged"])],
        min_points=2,
        model_answer="Heating makes the molecules move faster, so each collision with the wall is harder. But the larger volume means they hit each area of the wall less often. These two effects cancel, so the pressure stays the same.",
        hints=["What does heating do?", "What does the larger volume do?", "How can the pressure stay constant?"],
        keywords="harder collisions; less frequent; effects cancel",
        sample_pass=["The molecules move faster and hit harder, but in a larger volume they hit less often, so the effects cancel", "harder collisions but fewer collisions per second, so the pressure stays the same"],
        sample_fail=["The molecules expand", "The pressure must increase"])

written("w7x_aerosol_warning", 7, 4, "7e",
        stem="Aerosol cans carry the warning 'Do not heat or puncture'. Explain the danger of heating an aerosol can in terms of molecules.",
        points=[P("heating makes the gas molecules move faster", ["move faster", "faster", "more kinetic energy", "speed up"]),
                P("they hit the walls more often and harder, so the pressure rises", ["pressure rises", "pressure increases", "higher pressure", "more often", "harder"]),
                P("the can may burst / explode", ["burst", "explode", "break", "rupture"])],
        min_points=2,
        model_answer="Heating makes the gas molecules move faster, so they hit the walls of the can more often and harder. The pressure rises, and the can may burst.",
        hints=["What does heating do to the molecules?", "What happens to the pressure?", "What could happen to the can?"],
        keywords="faster molecules; pressure rises; can bursts",
        sample_pass=["The molecules move faster, the pressure increases and the can may burst", "they hit the walls harder so the pressure rises and it could explode"],
        sample_fail=["The can melts", "The molecules expand and break the can"])

# ---------------------------------------------------------------- L5
written("w7x_eval_ice_floats", 7, 5, "7a",
        stem="Most substances are denser as solids than as liquids, but ice floats on water. Explain what this tells you about the arrangement of water molecules in ice.",
        points=[P("ice is less dense than liquid water", ["less dense", "lower density", "smaller density"]),
                P("the molecules in ice are held in an open (spaced-out) arrangement, further apart on average than in the liquid", ["open", "further apart", "more space", "spaced out", "takes up more space", "larger volume"])],
        model_answer="Ice floats, so it is less dense than liquid water. This means that in ice the molecules are held in an open arrangement and are, on average, further apart than in liquid water, so the same mass takes up more volume.",
        hints=["What does floating tell you about density?", "Same mass, larger volume…", "…so how are the molecules arranged?"],
        keywords="ice less dense; open arrangement, molecules further apart",
        sample_pass=["Ice is less dense, so the molecules must be in an open arrangement, further apart than in water", "it has a lower density because the molecules take up more space in the solid"],
        sample_fail=["Ice molecules are lighter", "Ice has air in it"])

written("w7x_eval_gas_diffusion_room", 7, 5, "7a",
        stem="Gas molecules move at about 500 m/s, yet a smell takes minutes to cross a room. Explain this.",
        points=[P("the molecules collide very frequently with air molecules", ["collide", "collisions", "bump into", "hit other molecules", "air molecules"]),
                P("so they change direction constantly and follow a random zig-zag path", ["change direction", "random", "zig-zag", "zigzag", "not a straight line"])],
        model_answer="The smell molecules collide very frequently with air molecules, so they keep changing direction and follow a random zig-zag path. Their overall progress across the room is therefore much slower than their speed.",
        hints=["Do the molecules travel in straight lines?", "What gets in their way?", "Link to the path."],
        keywords="frequent collisions; random zig-zag path",
        sample_pass=["They collide with air molecules and keep changing direction, so they follow a random zig-zag path", "lots of collisions mean the path is random, not a straight line"],
        sample_fail=["The molecules are slow", "The air is too thick"])

written("w7x_eval_brownian_alive", 7, 5, "7c",
        stem="When Brownian motion was first seen in pollen grains, it was thought that the grains were alive. Describe an observation that would show this idea is wrong, and explain the real cause.",
        points=[P("non-living particles (dust, smoke, old/dead pollen) show the same motion", ["dust", "smoke", "dead", "non-living", "not alive", "same motion"]),
                P("the real cause is uneven bombardment by moving water molecules", ["water molecules", "uneven", "bombard", "collide", "collisions", "hit by molecules"])],
        model_answer="Dead pollen, dust or smoke particles show exactly the same jiggling motion, so it cannot be due to life. The real cause is uneven bombardment by the moving water (or air) molecules around them.",
        hints=["Test something that is not alive.", "Does it still move?", "What really causes it?"],
        keywords="non-living particles also move; uneven bombardment by molecules",
        sample_pass=["Dust particles also move in the same way, so it is caused by uneven collisions with water molecules", "smoke shows the same motion, which is caused by molecules hitting it unevenly"],
        sample_fail=["The pollen stops after a while", "Pollen is too small to be alive"])

written("w7x_eval_brownian_model", 7, 5, "7c",
        stem="A teacher models Brownian motion with a large ball on a table and many small marbles rolling fast in all directions. Evaluate how well this models the smoke cell.",
        points=[P("good: the large ball is like a smoke particle, the marbles like air molecules", ["ball is like a smoke", "large ball", "smoke particle", "marbles like air", "marbles are air molecules", "air molecules"]),
                P("the ball jiggles randomly due to uneven impacts, like smoke", ["random", "uneven", "jiggles", "zig-zag", "collisions"]),
                P("limitation: it is two-dimensional, and the marbles slow down by friction (air molecules keep moving)", ["two-dimensional", "2d", "friction", "slow down", "flat", "real molecules are much smaller"])],
        min_points=2,
        model_answer="It is a good model: the large ball represents a smoke particle and the fast marbles represent air molecules; uneven impacts make the ball jiggle randomly, like smoke. However, it is only two-dimensional, the marbles slow down because of friction (air molecules keep moving), and real air molecules are far smaller than smoke particles.",
        hints=["What does each object represent?", "What does the ball do?", "How is it unlike the real thing?"],
        keywords="ball = smoke, marbles = air; random jiggling; limits: 2D, friction",
        sample_pass=["The large ball is like a smoke particle and the marbles like air molecules; it jiggles randomly, but the model is two-dimensional and the marbles slow down by friction", "good because the uneven collisions make the ball move randomly; limitation: it is flat"],
        sample_fail=["It is a perfect model", "Marbles are bigger than balls"])

written("w7x_eval_boyle_explain", 7, 5, "7e",
        stem="A student halves the volume of a fixed mass of gas at constant temperature and finds that the pressure doubles. Explain this result fully using the kinetic particle model.",
        points=[P("temperature constant, so the molecules' average speed (KE) is unchanged", ["same speed", "speed is unchanged", "same average kinetic energy", "temperature is constant", "same kinetic energy"]),
                P("in half the volume, the molecules hit each area of the wall twice as often", ["twice as often", "twice as many collisions", "double the collisions", "more often", "more frequent"]),
                P("so the force per unit area (pressure) doubles", ["force per unit area", "pressure doubles", "doubles the pressure", "twice the pressure"])],
        min_points=2,
        model_answer="The temperature is constant, so the molecules move with the same average speed. In half the volume they hit each area of the wall twice as often, so the force per unit area on the walls, the pressure, doubles.",
        hints=["Does the molecules' speed change?", "How often do they hit the walls now?", "Link to force per unit area."],
        keywords="same speed; twice as many collisions per area; pressure doubles",
        sample_pass=["The speed is unchanged, but the molecules hit the walls twice as often, so the pressure doubles", "same temperature means same kinetic energy; double the collisions per unit area so twice the pressure"],
        sample_fail=["The molecules move twice as fast", "The molecules become half the size"])

written("w7x_eval_balloon_altitude", 7, 5, "7e",
        stem="A sealed party balloon is released and rises high into the atmosphere, where it eventually bursts. Explain why, in terms of pressure and molecules.",
        points=[P("the outside atmospheric pressure falls with height", ["outside pressure falls", "atmospheric pressure decreases", "lower pressure outside", "less air", "pressure decreases with height"]),
                P("the gas inside pushes the balloon out (expands) until pressures balance", ["expands", "gets bigger", "pushes out", "volume increases", "balloon grows"]),
                P("the rubber stretches too far and bursts", ["stretches", "bursts", "too far", "breaks"])],
        min_points=2,
        model_answer="As the balloon rises, the atmospheric pressure outside falls. The molecules inside now push outwards harder than the air outside pushes in, so the balloon expands until the pressures balance. Eventually the rubber is stretched too far and bursts.",
        hints=["How does air pressure change with height?", "What does the gas inside do?", "What happens to the rubber?"],
        keywords="outside pressure falls; balloon expands; bursts",
        sample_pass=["The outside pressure decreases so the balloon expands until it stretches too far and bursts", "less air pressure outside, the gas pushes out, the balloon gets bigger and bursts"],
        sample_fail=["The balloon gets cold and shrinks", "The Sun melts it"])

written("w7x_eval_particles_solid_heat", 7, 5, "7b",
        stem="A student says: 'When a solid is heated, its particles get bigger, so the solid expands.' Evaluate the statement and give the correct explanation.",
        points=[P("the statement is wrong: the particles do not change size", ["wrong", "incorrect", "not get bigger", "same size", "do not change size"]),
                P("the particles vibrate more (with larger amplitude)", ["vibrate more", "larger vibrations", "vibrate faster", "more energy", "larger amplitude"]),
                P("so they take up more space / move further apart", ["further apart", "more space", "spaces increase", "distance between"])],
        min_points=2,
        model_answer="The statement is wrong: the particles stay the same size. When heated they gain energy and vibrate more, with a larger amplitude, so on average they are further apart and the solid expands.",
        hints=["Do particles change size?", "What do they do more of?", "How does that change the spacing?"],
        keywords="wrong, same size; vibrate more; further apart",
        sample_pass=["Wrong, the particles stay the same size but vibrate more and move further apart", "incorrect: they vibrate with larger amplitude and take up more space"],
        sample_fail=["Correct, the particles grow", "The number of particles increases"])
