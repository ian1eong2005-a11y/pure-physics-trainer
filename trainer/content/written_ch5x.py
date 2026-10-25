"""Chapter 5 Pressure written-answer bank extension: fills each level to at least 10 with every LO at least twice."""
from .. import figs2
from ..marker import Pitfall, Point
from .base import written

P = Point
PF = Pitfall

# ---------------------------------------------------------------- L1
written("w5x_pascal_unit", 5, 1, "5a",
        stem="State the SI unit of pressure and write it in terms of newtons and metres.",
        points=[P("pascal (Pa)", ["pascal", "pa"]),
                P("1 Pa = 1 N/m²", ["n/m2", "newton per square metre", "newtons per square metre", "n m-2"])],
        model_answer="The pascal (Pa); 1 Pa = 1 N/m² (one newton per square metre).",
        hints=["It is named after a scientist.", "Pressure = force ÷ area.", "Write the unit of force ÷ unit of area."],
        keywords="pascal; N/m²",
        sample_pass=["pascal, which is N/m²", "Pa = newton per square metre"],
        sample_fail=["newton", "kg/m³"])

written("w5x_density_meaning", 5, 1, "5d",
        stem="Two blocks have the same volume, but block A has a larger mass. State which block is denser and explain why.",
        points=[P("block A is denser", ["a is denser", "block a", "a has a larger density", "a has the larger density", "a has higher density", "a is more dense"]),
                P("density = mass ÷ volume, and A has more mass in the same volume", ["mass / volume", "mass divided by volume", "mass per unit volume", "more mass in the same volume", "same volume", "more mass per"])],
        model_answer="Block A is denser, because density = mass ÷ volume and A has more mass in the same volume.",
        hints=["Recall the definition of density.", "The volumes are equal.", "Which has more mass per cm³?"],
        keywords="A; density = mass ÷ volume; more mass in same volume",
        sample_pass=["A is denser because density is mass divided by volume and it has more mass in the same volume", "block A, it has more mass per unit volume"],
        sample_fail=["B is denser", "They have the same density because they are the same size"])

written("w5x_camel_feet", 5, 1, "5b",
        stem="Camels have wide, flat feet. Explain how this helps them walk on soft sand.",
        points=[P("their weight is spread over a large area", ["large area", "larger area", "spread", "wide area", "big area"]),
                P("so the pressure on the sand is small and they do not sink", ["pressure is small", "small pressure", "less pressure", "lower pressure", "smaller pressure", "pressure is reduced", "reduces the pressure"])],
        model_answer="Wide, flat feet spread the camel's weight over a large area, so the pressure on the sand is small and the camel does not sink in.",
        hints=["What do wide feet do to the area?", "p = F ÷ A.", "Link to sinking."],
        keywords="large area → small pressure → does not sink",
        sample_pass=["The weight is spread over a large area so the pressure is small", "a larger area gives less pressure on the sand so it does not sink"],
        sample_fail=["Camels are light", "Their feet are strong"])

written("w5x_pressure_force_area", 5, 1, "5b",
        stem="State two ways of increasing the pressure that a force exerts on a surface.",
        points=[P("increase the force", ["increase the force", "larger force", "bigger force", "more force", "greater force"]),
                P("decrease the area", ["decrease the area", "smaller area", "reduce the area", "less area", "smaller contact area"])],
        model_answer="Increase the force, or apply the same force over a smaller area.",
        hints=["p = F ÷ A.", "What happens if F goes up?", "What happens if A goes down?"],
        keywords="increase force; decrease area",
        sample_pass=["Increase the force or use a smaller area", "a bigger force, or reduce the area"],
        sample_fail=["Increase the area", "Make it heavier and wider"])

written("w5x_liquid_pressure_factors", 5, 1, "5e",
        stem="State the three quantities that the pressure due to a liquid at a point depends on.",
        points=[P("depth (height of liquid above the point)", ["depth", "height"]),
                P("density of the liquid", ["density"]),
                P("gravitational field strength g", ["gravitational field strength", "g"])],
        min_points=3,
        model_answer="The depth of the point below the surface, the density of the liquid and the gravitational field strength g (p = h ρ g).",
        hints=["Write the equation for liquid pressure.", "There are three symbols.", "Name each."],
        keywords="depth; density; g",
        sample_pass=["depth, density and gravitational field strength", "the height of liquid above it, its density and g"],
        sample_fail=["the area and shape of the container", "the volume of the liquid"])

written("w5x_submarine_strong", 5, 1, "5e",
        stem="Explain why a submarine that dives very deep must have a very strong hull.",
        points=[P("pressure in water increases with depth", ["increases with depth", "pressure increases", "greater pressure", "larger pressure", "higher pressure", "more pressure"]),
                P("so a very large force acts on the hull", ["large force", "larger force", "greater force", "big force", "huge force", "crush"])],
        model_answer="Water pressure increases with depth, so deep down a very large pressure, and therefore a very large force, acts on the hull; a weak hull would be crushed.",
        hints=["How does pressure change with depth?", "What does pressure do to the hull?", "Force = pressure × area."],
        keywords="pressure increases with depth → large force on hull",
        sample_pass=["The pressure increases with depth so there is a large force on the hull", "deep water has greater pressure which would crush a weak hull"],
        sample_fail=["Submarines are heavy", "Fish might bite it"])

written("w5x_hydraulic_principle", 5, 1, "5c",
        stem="State the property of liquids that makes hydraulic machines work.",
        points=[P("liquids are (almost) incompressible", ["incompressible", "hardly compressed", "cannot be compressed", "cannot be squashed", "almost incompressible", "hardly compress"]),
                P("so pressure applied is transmitted equally throughout the liquid", ["transmitted", "transmit", "passed on", "equally throughout", "same pressure", "transfers the pressure"])],
        model_answer="Liquids are almost incompressible, so a pressure applied at one point is transmitted equally throughout the liquid.",
        hints=["Can a liquid be squashed?", "What happens to a pressure applied to it?", "Transmitted equally."],
        keywords="incompressible; pressure transmitted equally",
        sample_pass=["Liquids are incompressible so they transmit pressure equally", "they cannot be squashed and the pressure is passed on throughout"],
        sample_fail=["Liquids are heavy", "Liquids flow fast"])

written("w5x_hydraulic_output", 5, 1, "5c",
        stem="In a hydraulic jack, explain why the large piston exerts a larger force than the force applied to the small piston.",
        points=[P("the pressure is the same at both pistons", ["pressure is the same", "same pressure", "equal pressure", "pressure is equal", "pressure is transmitted"]),
                P("force = pressure × area and the large piston has a larger area", ["larger area", "bigger area", "greater area", "pressure × area", "pressure x area", "pressure times area"])],
        model_answer="The pressure is transmitted equally, so it is the same at both pistons. Since force = pressure × area and the large piston has a larger area, it exerts a larger force.",
        hints=["What is transmitted by the liquid?", "F = p × A.", "Compare the areas."],
        keywords="same pressure; larger area → larger force",
        sample_pass=["The pressure is the same but the large piston has a larger area so the force is larger", "same pressure, and force = pressure x area, so the bigger area gives a bigger force"],
        sample_fail=["The large piston is heavier", "The pressure is bigger at the large piston"])

# ---------------------------------------------------------------- L2
written("w5x_skis", 5, 2, "5b",
        stem="Explain why a skier does not sink into soft snow while a person in ordinary shoes does.",
        points=[P("skis have a much larger area", ["larger area", "large area", "bigger area", "greater area", "wide"]),
                P("for the same weight, the pressure on the snow is smaller", ["pressure is smaller", "smaller pressure", "less pressure", "lower pressure", "pressure is less", "reduces the pressure"])],
        model_answer="The skis have a much larger area than shoes, so the same weight gives a much smaller pressure on the snow, and the skier does not sink.",
        hints=["Compare the areas.", "The weight is the same.", "p = F ÷ A."],
        keywords="larger area → smaller pressure",
        sample_pass=["The skis have a larger area so the pressure on the snow is smaller", "same weight over a bigger area means less pressure"],
        sample_fail=["Skis are lighter than shoes", "Skiers move fast"])

written("w5x_water_tower", 5, 2, "5e",
        stem="Water towers are built on high ground or on tall supports. Explain why, in terms of pressure.",
        points=[P("a greater height of water above the taps", ["greater height", "greater depth", "higher", "height of water", "taller column", "more height"]),
                P("gives a greater water pressure at the taps", ["greater pressure", "higher pressure", "larger pressure", "more pressure", "pressure increases"])],
        model_answer="The greater the height of water above the taps in homes, the greater the water pressure there (p = h ρ g), so water flows out strongly.",
        hints=["What does p = h ρ g depend on?", "What does a tall tower change?", "Link to the pressure at the tap."],
        keywords="greater height (depth) → greater pressure at taps",
        sample_pass=["A greater height of water gives a greater pressure at the taps", "higher water means more pressure, so it flows out strongly"],
        sample_fail=["So the water stays cool", "So birds cannot drink it"])

written("w5x_ears_deep", 5, 2, "5e",
        stem="Swimmers feel pain in their ears when they dive to the bottom of a deep pool. Explain why.",
        points=[P("water pressure increases with depth", ["increases with depth", "pressure increases", "greater pressure", "higher pressure", "more pressure", "larger pressure"]),
                P("the pressure pushes on the eardrum", ["eardrum", "ear drum", "on the ear", "pushes on the ear", "presses on the ear"])],
        model_answer="Water pressure increases with depth, so at the bottom of the pool a large pressure pushes on the eardrum, causing pain.",
        hints=["How does water pressure change with depth?", "What does it push on?", "Link to the ear."],
        keywords="pressure increases with depth; pushes on eardrum",
        sample_pass=["The pressure increases with depth and pushes on the eardrum", "deeper water has higher pressure on the ear"],
        sample_fail=["The water is cold", "The water is dirty"])

written("w5x_brake_fluid", 5, 2, "5c",
        stem="Explain how pressing the brake pedal of a car pushes the brake pads against the wheels.",
        points=[P("the pedal pushes a piston, creating pressure in the brake fluid", ["pressure in the fluid", "pressure in the brake fluid", "creates a pressure", "produces a pressure", "pressure is applied"]),
                P("the pressure is transmitted through the fluid to the brake pistons", ["transmitted", "passed on", "transfers", "through the fluid", "to the brake pistons"]),
                P("larger brake pistons give a larger force on the pads", ["larger area", "larger force", "bigger force", "greater force", "bigger area"])],
        min_points=2,
        model_answer="The pedal pushes a small piston, creating a pressure in the brake fluid. The fluid is incompressible, so the pressure is transmitted through the pipes to the brake pistons, whose larger area gives a larger force pushing the pads against the wheels.",
        hints=["What does the pedal push?", "How does the pressure reach the wheels?", "Why is the force at the pads large?"],
        keywords="pressure in fluid; transmitted; larger area → larger force",
        sample_pass=["The pedal creates a pressure in the brake fluid which is transmitted to the brake pistons, giving a larger force", "pressure in the fluid is passed on to pistons with a bigger area so a greater force pushes the pads"],
        sample_fail=["A cable pulls the pads", "The brakes use magnets"])

written("w5x_hydraulic_distance", 5, 2, "5c",
        stem="In a hydraulic jack, the small piston moves much further than the large piston. Explain why.",
        points=[P("the volume of liquid pushed out by the small piston equals the volume moving the large piston", ["same volume", "volume is the same", "equal volume", "volume of liquid", "volume moved"]),
                P("the large piston has a larger area, so it moves a smaller distance", ["larger area", "bigger area", "greater area", "smaller distance", "moves less"])],
        model_answer="The liquid is incompressible, so the volume pushed out by the small piston equals the volume that moves the large piston. Since volume = area × distance and the large piston has a larger area, it moves a smaller distance.",
        hints=["What is the same at both pistons apart from pressure?", "Volume = area × distance.", "Compare the areas."],
        keywords="same volume; larger area → smaller distance",
        sample_pass=["The same volume of liquid moves, and the large piston has a larger area so it moves a smaller distance", "equal volume; the bigger area means it moves less"],
        sample_fail=["The large piston is heavier", "Friction stops the large piston"])

written("w5x_barometer_works", 5, 2, "5f",
        stem="Explain why the mercury in a barometer tube stays up at a height of about 76 cm.",
        points=[P("atmospheric pressure pushes down on the mercury in the dish", ["atmospheric pressure", "air pressure", "atmosphere pushes", "air pushes"]),
                P("the column's pressure (h ρ g) balances atmospheric pressure; there is a vacuum above", ["balances", "equal", "equals", "vacuum", "h ρ g", "hρg"])],
        model_answer="Atmospheric pressure pushes down on the mercury in the dish. The pressure of the mercury column, h ρ g, balances it; there is a vacuum above the column, so no air pushes down from the top.",
        hints=["What pushes on the dish?", "What is above the column?", "Balance the pressures."],
        keywords="atmospheric pressure on dish; balanced by column; vacuum above",
        sample_pass=["Atmospheric pressure on the dish balances the pressure of the mercury column", "air pressure pushes the mercury up and there is a vacuum at the top"],
        sample_fail=["Mercury sticks to the glass", "The tube is sealed at the bottom"])

written("w5x_altitude_pressure", 5, 2, "5f",
        stem="State and explain how atmospheric pressure changes as you climb a mountain.",
        points=[P("atmospheric pressure decreases", ["decreases", "lower", "less", "falls", "drops", "smaller"]),
                P("there is less air above to press down", ["less air above", "less air", "thinner air", "fewer air", "air is less dense", "smaller height of air"])],
        pitfalls=[PF(["increases"], "Atmospheric pressure DECREASES with height.")],
        model_answer="Atmospheric pressure decreases, because there is less air above you pressing down (and the air is less dense).",
        hints=["What causes atmospheric pressure?", "The weight of air above.", "Less air above at the top."],
        keywords="decreases; less air above",
        sample_pass=["It decreases because there is less air above", "the pressure is lower since the air is thinner"],
        sample_fail=["It increases because you are closer to the Sun", "It stays the same"])

# ---------------------------------------------------------------- L3
written("w5x_dam_shape", 5, 3, "5e",
        stem="Explain why the wall of a dam is much thicker at the bottom than at the top.",
        points=[P("water pressure increases with depth", ["increases with depth", "pressure increases", "greater pressure", "higher pressure", "larger pressure", "pressure is greatest"]),
                P("so the force on the bottom of the wall is greatest; a thicker wall withstands it", ["greatest force", "larger force", "greater force", "withstand", "stronger", "thicker"])],
        model_answer="Water pressure increases with depth, so the pressure and therefore the force on the lowest part of the wall is greatest. The wall is thicker there to withstand this force.",
        hints=["How does pressure vary with depth?", "Where is the force on the wall greatest?", "Why make that part thicker?"],
        keywords="pressure increases with depth; greatest force at bottom; thicker to withstand",
        sample_pass=["The pressure increases with depth so the force is greatest at the bottom and the wall must be thicker to withstand it", "greater pressure at the bottom needs a stronger, thicker wall"],
        sample_fail=["To look nice", "Because the water is denser at the bottom"])

written("w5x_drip_height", 5, 3, "5e",
        stem="In hospitals, an intravenous drip bag is hung high above the patient's arm. Explain why, and what happens if it is lowered.",
        points=[P("a greater height gives a greater pressure in the liquid at the arm", ["greater height", "greater pressure", "higher pressure", "height of liquid", "h ρ g", "hρg"]),
                P("this pressure must be greater than the blood pressure to push the liquid in", ["blood pressure", "greater than the pressure in the vein", "push the liquid in", "flow into"]),
                P("if lowered, the pressure falls and the flow slows or stops", ["slows", "stops", "less flow", "flow decreases", "pressure falls", "pressure decreases"])],
        min_points=2,
        model_answer="The height of liquid above the arm gives a pressure h ρ g in the tube; hanging the bag high makes this pressure greater than the blood pressure in the vein, so liquid flows in. If the bag is lowered, the pressure falls and the flow slows or stops.",
        hints=["What does the height of liquid give?", "Compare with the blood pressure.", "What happens if h is smaller?"],
        keywords="height → pressure h ρ g > blood pressure; lower → flow slows",
        sample_pass=["A greater height gives a greater pressure than the blood pressure, so the liquid flows in; lowering it slows the flow", "the pressure from the height of liquid pushes it into the vein; if lowered, the pressure falls and it stops"],
        sample_fail=["So the patient can see it", "To keep it cold"])

written("w5x_water_barometer", 5, 3, "5f",
        stem="Explain why a barometer made with water would need a tube about 10 m tall, while a mercury barometer is less than 1 m tall.",
        points=[P("water is much less dense than mercury", ["less dense", "lower density", "smaller density", "density of water is less", "mercury is denser", "mercury is more dense"]),
                P("for the same atmospheric pressure, h ρ g is the same, so the height must be much greater", ["same pressure", "h ρ g", "hρg", "taller", "greater height", "higher column", "larger height"])],
        model_answer="Both columns must balance the same atmospheric pressure, so h ρ g is the same. Water is about 13.6 times less dense than mercury, so its column must be about 13.6 times taller, about 10 m.",
        hints=["What must each column balance?", "p = h ρ g.", "Compare the densities."],
        keywords="same atmospheric pressure; water less dense → taller column",
        sample_pass=["Water is less dense than mercury, so for the same pressure h rho g the column must be taller", "mercury is denser, so a water column needs a greater height to balance atmospheric pressure"],
        sample_fail=["Water is denser than mercury", "Water evaporates so more is needed"])

written("w5x_straw", 5, 3, "5f",
        stem="Explain how you are able to drink through a straw.",
        points=[P("sucking lowers the air pressure inside the straw", ["lowers the pressure", "reduces the pressure", "lower pressure", "reduces the air pressure", "pressure inside decreases", "less pressure", "greater than inside", "lower inside"]),
                P("atmospheric pressure on the drink surface is greater and pushes the liquid up", ["atmospheric pressure", "air pressure outside", "pushes the liquid up", "pushes the drink up", "greater pressure outside"])],
        model_answer="Sucking removes air and lowers the pressure inside the straw. Atmospheric pressure on the surface of the drink is now greater, so it pushes the liquid up the straw.",
        hints=["What does sucking do to the air in the straw?", "What presses on the drink in the cup?", "Compare the pressures."],
        keywords="lower pressure inside; atmospheric pressure pushes liquid up",
        sample_pass=["Sucking lowers the pressure in the straw and atmospheric pressure pushes the drink up", "the air pressure outside is greater than inside, so it pushes the liquid up"],
        sample_fail=["The straw pulls the water", "Suction force drags the liquid"])

written("w5x_manometer_how", 5, 3, "5g",
        stem="Describe how a U-tube manometer shows that a gas supply is at a pressure greater than atmospheric pressure.",
        points=[P("connect one arm to the gas and leave the other open to the atmosphere", ["one arm", "connect", "open to the atmosphere", "open end", "other side open", "other arm open"]),
                P("the liquid is pushed down on the gas side and rises on the open side", ["pushed down", "lower on the gas side", "rises on the open side", "higher on the open side", "level difference"]),
                P("the level difference h gives the excess pressure h ρ g", ["h ρ g", "hρg", "excess pressure", "difference in pressure", "pressure difference", "height difference"])],
        min_points=2,
        model_answer="One arm is connected to the gas supply and the other is open to the atmosphere. The greater gas pressure pushes the liquid down on the gas side so it rises on the open side; the level difference h gives the excess pressure, h ρ g.",
        hints=["How is the manometer connected?", "Which way does the liquid move?", "What does the level difference measure?"],
        keywords="one arm to gas, other open; liquid pushed down on gas side; h ρ g = excess pressure",
        sample_pass=["Connect one arm to the gas and leave the other open; the liquid is pushed down on the gas side and the level difference gives the pressure difference", "the liquid is lower on the gas side and higher on the open side; h rho g is the excess pressure"],
        sample_fail=["The gas makes the liquid bubble", "The liquid turns colour"])

written("w5x_manometer_oil_better", 5, 3, "5g",
        stem="A student uses a manometer to measure a small pressure difference. Explain why oil would give a more precise reading than mercury.",
        points=[P("oil is less dense than mercury", ["less dense", "lower density", "smaller density", "mercury is denser"]),
                P("so the level difference is larger for the same pressure, easier to measure precisely", ["larger difference", "larger level difference", "bigger difference", "greater height", "larger height", "taller", "easier to measure"])],
        model_answer="Oil is much less dense than mercury, so for the same pressure difference (h ρ g) the level difference h is much larger, which can be measured with a smaller percentage error.",
        hints=["Compare the densities.", "h = Δp ÷ (ρ g).", "Is a larger h easier to measure?"],
        keywords="oil less dense → larger h → more precise",
        sample_pass=["Oil is less dense so the level difference is larger and easier to measure", "lower density gives a greater height for the same pressure"],
        sample_fail=["Mercury is poisonous", "Oil is cheaper"])

# ---------------------------------------------------------------- L4
written("w5x_pressure_shape_independent", 5, 4, "5e",
        stem="A wide tank and a narrow pipe are filled with water to the same depth. Explain why the pressure at the bottom is the same in both, even though the tank holds much more water.",
        points=[P("liquid pressure depends only on depth, density and g (p = h ρ g)", ["h ρ g", "hρg", "depth", "depends on depth", "depends only on"]),
                P("the extra weight of water in the tank acts on a proportionally larger area", ["larger area", "bigger area", "greater area", "spread over", "weight / area", "per unit area"])],
        model_answer="Liquid pressure depends only on depth, density and g (p = h ρ g), which are the same for both. The tank holds more water, but that greater weight acts on a proportionally larger area, so the pressure is the same.",
        hints=["Which equation gives liquid pressure?", "Does it include the area?", "Think about weight ÷ area."],
        keywords="p = h ρ g; more weight but larger area",
        sample_pass=["Pressure depends only on depth and density, and the extra weight in the tank is spread over a larger area", "p = h rho g is the same; the tank's bigger weight acts on a bigger area"],
        sample_fail=["The tank has more water so more pressure", "The pipe has more pressure because it is narrow"])

written("w5x_diver_total_pressure", 5, 4, "5e",
        stem="A diver is 20 m below the surface of the sea. Explain why the total pressure on the diver is greater than the pressure due to the water alone, and how to find it.",
        points=[P("atmospheric pressure also acts on the surface of the sea", ["atmospheric pressure", "air pressure", "atmosphere"]),
                P("total pressure = atmospheric pressure + h ρ g", ["+ h ρ g", "plus h ρ g", "add", "atmospheric pressure +", "sum", "total"])],
        model_answer="Atmospheric pressure acts on the surface of the sea and is transmitted down through the water, so total pressure = atmospheric pressure + h ρ g.",
        hints=["What presses on the surface of the sea?", "Is it transmitted downwards?", "Add the two."],
        keywords="atmospheric pressure + h ρ g",
        sample_pass=["Atmospheric pressure also acts, so total = atmospheric pressure + h rho g", "add air pressure to the water pressure h ρ g to get the total"],
        sample_fail=["The diver's weight adds to it", "Total = h ρ g only"])

written("w5x_hydraulic_lift_design", 5, 4, "5c",
        stem="A garage needs a hydraulic lift that lifts a car with a small force. Explain two features of its design.",
        points=[P("the output piston has a much larger area than the input piston", ["larger area", "bigger area", "large piston", "area of the large piston", "greater area"]),
                P("the fluid is an incompressible liquid (oil) with no air bubbles", ["incompressible", "oil", "liquid", "air bubbles", "no air", "cannot be compressed"]),
                P("the pressure is transmitted so force = pressure × area is larger at the output", ["pressure is transmitted", "same pressure", "pressure × area", "pressure x area", "transmitted"])],
        min_points=2,
        model_answer="The output piston has a much larger area than the input piston, so the transmitted pressure gives a much larger force (F = p × A). The fluid is an incompressible oil with no air bubbles, so the pressure is transmitted fully.",
        hints=["What should the areas be like?", "What fluid should it use?", "Explain each with pressure."],
        keywords="larger output area; incompressible oil; pressure transmitted",
        sample_pass=["The large piston has a bigger area and the fluid is incompressible oil, so the transmitted pressure gives a larger force", "use oil with no air bubbles and make the output piston area large"],
        sample_fail=["Use a long lever", "Use air in the pipes"])

written("w5x_hydraulic_air_bubble", 5, 4, "5c",
        stem="A mechanic says that air bubbles must be removed from the brake fluid. Explain why.",
        points=[P("air is compressible", ["compressible", "can be compressed", "squashed", "compresses", "can be squashed"]),
                P("so the pressure is not fully transmitted and the brakes are less effective", ["not fully transmitted", "less effective", "pressure is reduced", "less force", "smaller force", "spongy", "brakes may fail"])],
        model_answer="Air is compressible, so pressing the pedal squashes the air bubbles instead of transmitting the pressure fully to the brake pistons; the brakes give less force and are less effective.",
        hints=["How is air different from a liquid?", "What happens when the pedal is pressed?", "Link to braking."],
        keywords="air compressible; pressure not fully transmitted; brakes less effective",
        sample_pass=["Air is compressible so the pressure is not fully transmitted and the brakes are less effective", "the air gets squashed so there is less force on the pads"],
        sample_fail=["Air makes the fluid too hot", "Bubbles make noise"])

written("w5x_manometer_gas_lower", 5, 4, "5g",
        stem="A manometer is connected to a flask from which some air has been removed. The liquid is higher on the flask side. Explain this and state how to find the pressure in the flask.",
        points=[P("the pressure in the flask is less than atmospheric", ["less than atmospheric", "lower than atmospheric", "below atmospheric", "smaller than atmospheric"]),
                P("atmospheric pressure pushes the liquid towards the flask", ["atmospheric pressure pushes", "pushed towards the flask", "air pressure pushes", "pushes the liquid up"]),
                P("p_flask = atmospheric pressure − h ρ g", ["- h ρ g", "minus h ρ g", "subtract", "atmospheric pressure -", "atmospheric pressure minus"])],
        min_points=2,
        model_answer="The pressure in the flask is less than atmospheric, so atmospheric pressure on the open side pushes the liquid up towards the flask. The pressure in the flask = atmospheric pressure − h ρ g.",
        hints=["Which side has the higher pressure?", "Which way is the liquid pushed?", "Add or subtract h ρ g?"],
        keywords="flask below atmospheric; liquid pushed towards flask; p = p_atm − h ρ g",
        sample_pass=["The flask pressure is less than atmospheric so atmospheric pressure pushes the liquid up; p = atmospheric pressure minus h rho g", "lower than atmospheric, subtract h ρ g from atmospheric pressure"],
        sample_fail=["The flask pressure is higher than atmospheric", "The liquid is attracted to the flask"])

written("w5x_manometer_independent", 5, 4, "5g",
        stem="A student says that a manometer with a wider tube will show a smaller level difference for the same gas supply. Explain whether the student is right.",
        points=[P("the student is wrong", ["wrong", "incorrect", "not right", "disagree"]),
                P("the level difference depends only on the pressure difference and the liquid's density (h = Δp ÷ ρ g), not the width", ["h ρ g", "hρg", "depends only on", "density", "pressure difference"])],
        model_answer="The student is wrong: the level difference h is fixed by the pressure difference and the liquid's density (Δp = h ρ g); the width of the tube does not appear, so h stays the same.",
        hints=["Which equation links h and pressure?", "Does it contain the area?", "So is the student right?"],
        keywords="wrong; Δp = h ρ g has no area",
        sample_pass=["Wrong, because the level difference depends only on the pressure difference and density, h rho g", "incorrect: h = Δp ÷ ρ g, so width has no effect"],
        sample_fail=["Right, a wider tube has more liquid", "Right, because the pressure is spread out"])

# ---------------------------------------------------------------- L5
written("w5x_evaluate_deep_snorkel", 5, 5, "5e",
        stem="A swimmer suggests using a 4 m long snorkel to breathe while lying at the bottom of a deep pool. Evaluate this idea using ideas about pressure.",
        points=[P("at 4 m, the water pressure on the chest is much greater than atmospheric pressure", ["greater than atmospheric", "water pressure", "pressure on the chest", "h ρ g", "large pressure"]),
                P("the air in the snorkel is only at atmospheric pressure", ["atmospheric pressure", "air pressure", "only atmospheric"]),
                P("so the lungs cannot expand / breathing is impossible; the idea does not work", ["cannot breathe", "cannot expand", "does not work", "will not work", "unable to breathe", "impossible", "lungs collapse"])],
        min_points=2,
        model_answer="At 4 m the water pressure on the chest (h ρ g ≈ 40 kPa above atmospheric) is much greater than the pressure of the air in the snorkel, which is only atmospheric. The chest muscles cannot expand the lungs against this difference, so the swimmer cannot breathe in: the idea does not work.",
        hints=["What is the pressure on the chest at 4 m?", "What is the pressure of the air in the snorkel?", "Can the lungs expand?"],
        keywords="large water pressure on chest; air only atmospheric; lungs cannot expand",
        sample_pass=["The water pressure on the chest is greater than atmospheric but the air in the snorkel is only at atmospheric pressure, so they cannot breathe", "h rho g on the chest is large; lungs cannot expand, so it does not work"],
        sample_fail=["Good idea, the snorkel is long enough", "It works if the snorkel is wide"])

written("w5x_evaluate_wide_dam", 5, 5, "5e",
        stem="An engineer is told that a dam holding back a long, wide reservoir must be stronger than one holding back a narrow lake of the same depth. Evaluate this claim.",
        points=[P("the claim is wrong / not necessary", ["wrong", "incorrect", "not necessary", "disagree", "not true"]),
                P("the pressure on the dam depends only on depth (and density, g), not on the size of the lake", ["depends only on depth", "depth", "h ρ g", "hρg", "not on the size", "not the volume"]),
                P("dams of the same depth and width face the same pressure and force", ["same pressure", "same force", "equal pressure", "equally strong"])],
        min_points=2,
        model_answer="The claim is wrong. The pressure on the dam depends only on the depth of water, its density and g (p = h ρ g), not on how long or wide the reservoir is, so dams of the same width holding the same depth of water face the same pressure and force.",
        hints=["What does liquid pressure depend on?", "Does the length of the reservoir matter?", "Compare the forces on the dams."],
        keywords="wrong; p = h ρ g depends on depth only; same force",
        sample_pass=["Wrong, the pressure depends only on depth, not the size of the lake, so both dams face the same pressure", "not true: h rho g is the same, so the force is the same"],
        sample_fail=["Correct, more water pushes harder", "Correct, the big reservoir weighs more"])

written("w5x_evaluate_barometer_air", 5, 5, "5f",
        stem="When setting up a mercury barometer, a little air is trapped at the top of the tube. Explain the effect on the reading and how a student could check for trapped air.",
        points=[P("the trapped air exerts a pressure on top of the column", ["trapped air exerts", "air pushes down", "pressure on top", "air at the top", "air pressure at the top"]),
                P("so the column is shorter and the reading is too low", ["shorter", "too low", "smaller reading", "lower reading", "reads low", "less than"]),
                P("check: tilt the tube; mercury should fill the top completely if there is a vacuum", ["tilt", "fills the top", "reach the top", "fill the tube"])],
        min_points=2,
        model_answer="The trapped air exerts a pressure on top of the mercury, so the column is shorter and the reading is too low. To check, tilt the tube: if there is a vacuum the mercury rises to fill the top of the tube completely; a bubble remains if air is trapped.",
        hints=["What should be above the mercury?", "What does air at the top do?", "How could tilting help?"],
        keywords="air pushes down → column shorter, reading low; tilt to check",
        sample_pass=["The trapped air pushes down so the column is shorter and the reading too low; tilt the tube to see if the mercury fills the top", "air at the top gives a lower reading; tilting the tube should make mercury reach the top"],
        sample_fail=["It makes the reading higher", "No effect because air is light"])

written("w5x_evaluate_altitude_weather", 5, 5, "5f",
        stem="A hiker's barometer shows a lower reading at the top of a hill than at the bottom. A friend says this means a storm is coming. Evaluate the friend's claim.",
        points=[P("the reading is lower mainly because of the height: less air above", ["less air above", "height", "altitude", "higher up", "less air"]),
                P("so it does not necessarily mean a storm; weather changes are shown by a change at the same place over time", ["not necessarily", "same place", "over time", "does not mean", "cannot tell", "not a storm"])],
        model_answer="The reading is lower mainly because the hiker is higher up, with less air above pressing down. This does not necessarily mean a storm: a weather change would be shown by the pressure falling at the same place over time.",
        hints=["Why is pressure lower at the top?", "Is that about weather?", "How would weather show up on a barometer?"],
        keywords="lower due to altitude; storm shown by falling pressure at same place over time",
        sample_pass=["The pressure is lower because there is less air above at that height, so it does not necessarily mean a storm", "it is due to altitude; you need a fall at the same place over time to predict weather"],
        sample_fail=["The friend is right, low pressure always means storms", "The barometer is broken"])

written("w5x_evaluate_jack_claim", 5, 5, "5c",
        stem="An advert says: 'Our hydraulic jack multiplies your force 50 times, so you do 50 times less work!' Evaluate this claim.",
        points=[P("the force can be multiplied (large piston has 50 times the area)", ["multiplied", "50 times the area", "larger area", "force is larger", "larger force"]),
                P("but the large piston moves 50 times less distance", ["smaller distance", "less distance", "moves less", "50 times less distance", "moves a smaller distance", "small piston moves further"]),
                P("so the work done is not reduced (work = force × distance); the claim is wrong", ["work is the same", "same work", "not reduced", "claim is wrong", "not less work", "wrong"])],
        min_points=2,
        model_answer="The force can be multiplied 50 times if the large piston has 50 times the area, but the large piston then moves only 1/50 of the distance moved by the small piston. Work = force × distance is not reduced (it is slightly more because of friction), so the claim about work is wrong.",
        hints=["Can the force be multiplied?", "What about the distances moved?", "Work = force × distance."],
        keywords="force × 50 but distance ÷ 50; work not reduced",
        sample_pass=["The force is multiplied but the large piston moves a smaller distance, so the work is the same; the claim is wrong", "larger force, but the small piston moves further so you do not do less work"],
        sample_fail=["True, hydraulics save energy", "True because the pressure is multiplied"])

written("w5x_evaluate_crusher_design", 5, 5, "5c",
        stem="A student designs a hydraulic can-crusher with input piston area 2 cm² and output piston area 4 cm². Evaluate the design and suggest an improvement.",
        points=[P("the force is only doubled, which is a small gain", ["only doubled", "twice", "doubled", "small gain", "only 2 times", "small increase"]),
                P("make the output piston much larger compared with the input piston (or the input smaller)", ["much larger", "larger output", "bigger output", "increase the area", "smaller input", "larger area ratio"])],
        model_answer="The output force is only twice the input force (area ratio 4 ÷ 2 = 2), so the gain is small. The output piston should be made much larger relative to the input piston (or the input piston made smaller) to multiply the force more.",
        hints=["Find the ratio of areas.", "How much is the force multiplied?", "How could it be multiplied more?"],
        keywords="ratio 2 → force only doubled; make output area much larger",
        sample_pass=["The force is only doubled, so make the output piston much larger", "only twice the force; use a smaller input piston"],
        sample_fail=["It is perfect", "Make both pistons the same size"])
