"""Chapter 16 Practical Electricity written-answer bank extension: fills each level to at least 10 with every LO at least twice."""
from .. import figs3
from ..marker import Pitfall, Point
from .base import written

P = Point
PF = Pitfall

# ---------------------------------------------------------------- L1
written("w16x_kwh_vs_joule", 16, 1, "16c",
        stem="State how many joules are equal to one kilowatt-hour, and show how this is found.",
        points=[P("1 kWh = 1000 W × 3600 s", ["1000", "3600"]),
                P("= 3.6 × 10⁶ J (3.6 MJ)", ["3.6 × 10", "3.6 x 10", "3 600 000", "3600000", "3.6 mj", "3.6 million"])],
        model_answer="1 kWh = 1000 W × 3600 s = 3.6 × 10⁶ J (3.6 MJ).",
        hints=["1 kW = 1000 W.", "1 h = 3600 s.", "Multiply."],
        keywords="1000 W × 3600 s = 3.6 × 10⁶ J",
        sample_pass=["1000 W × 3600 s = 3.6 × 10⁶ J", "1 kWh = 1000 x 3600 = 3 600 000 J"],
        sample_fail=["1 kWh = 1000 J", "1 kWh = 60 J"])

written("w16x_three_wires_roles", 16, 1, "16g",
        stem="State the job of the live wire and of the neutral wire in a mains circuit.",
        points=[P("live: carries the supply at high potential (about 230 V)", ["high potential", "230", "high voltage", "supplies", "carries the current to"]),
                P("neutral: completes the circuit, at about 0 V", ["completes the circuit", "0 v", "returns", "zero", "back to"])],
        model_answer="The live wire carries the current to the appliance at a high potential of about 230 V. The neutral wire completes the circuit and is at about 0 V.",
        hints=["Which wire is at high potential?", "Which completes the circuit?", "Give both jobs."],
        keywords="live: 230 V supply; neutral: completes circuit at 0 V",
        sample_pass=["The live wire is at 230 V and carries the supply; the neutral completes the circuit at 0 V", "live carries the current at high potential, neutral returns it at zero volts"],
        sample_fail=["Live is safe; neutral is at 230 V", "Both are earth wires"])

written("w16x_heating_uses", 16, 1, "16a",
        stem="Name two appliances that use the heating effect of an electric current.",
        points=[P("one heating appliance, e.g. kettle, iron, toaster, heater, hair dryer, cooker", ["kettle", "iron", "toaster", "heater", "hair dryer", "cooker", "oven", "water heater"]),
                P("a second, different heating appliance", ["kettle", "iron", "toaster", "heater", "hair dryer", "cooker", "oven", "rice cooker"])],
        min_points=2,
        model_answer="An electric kettle and an electric iron (also toasters, heaters and hair dryers).",
        hints=["Which appliances are meant to make heat?", "Think of the kitchen.", "Two examples."],
        keywords="kettle, iron, toaster, heater",
        sample_pass=["A kettle and a toaster", "an electric iron and a heater"],
        sample_fail=["A television and a radio", "A fan and a lamp"])

written("w16x_heating_element", 16, 1, "16a",
        stem="State two properties of the wire used for the heating element of an electric kettle.",
        points=[P("high resistance (high resistivity)", ["high resistance", "high resistivity", "large resistance"]),
                P("high melting point / does not oxidise easily", ["high melting point", "does not melt", "oxidise", "corrode"])],
        model_answer="It has a high resistance (high resistivity), so it gets hot, and a high melting point, so it does not melt.",
        hints=["How does it produce heat?", "Why doesn't it melt?", "Two properties."],
        keywords="high resistance; high melting point",
        sample_pass=["High resistance and a high melting point", "a large resistance and it does not melt easily"],
        sample_fail=["Low resistance and magnetic", "It is a good insulator"])

written("w16x_power_equations", 16, 1, "16b",
        stem="Write down two equations for the electrical power of an appliance.",
        points=[P("P = V I", ["p = v i", "p = vi", "v × i", "v x i", "voltage × current", "voltage x current"]),
                P("P = I² R or P = V² ÷ R", ["i2 r", "i² r", "i2r", "v2 / r", "v² / r", "i squared"])],
        model_answer="P = V I, and P = I² R (or P = V² ÷ R).",
        hints=["One uses V and I.", "One uses I and R.", "Write both."],
        keywords="P = VI; P = I²R",
        sample_pass=["P = VI and P = I²R", "p = v x i, and p = v² / r"],
        sample_fail=["P = V ÷ I", "P = I ÷ R"])

written("w16x_power_calc_written", 16, 1, "16b",
        stem="A lamp takes a current of 0.25 A from the 230 V mains. Calculate its power, showing your working.",
        points=[P("P = V I = 230 × 0.25", ["230 × 0.25", "230 x 0.25", "v i", "p = vi", "p = v i"]),
                P("P = 57.5 W (about 58 W)", ["57.5", "58"])],
        model_answer="P = V I = 230 × 0.25 = 57.5 W.",
        hints=["P = V I.", "Substitute.", "Unit W."],
        keywords="P = 230 × 0.25 = 57.5 W",
        sample_pass=["P = VI = 230 × 0.25 = 57.5 W", "230 x 0.25 = 58 W"],
        sample_fail=["920 W", "0.0011 W"])

written("w16x_hazard_damp", 16, 1, "16d",
        stem="Explain why it is dangerous to touch a light switch with wet hands.",
        points=[P("water can conduct (impure water)", ["water conducts", "conduct", "conductor"]),
                P("so current could flow through the body, causing an electric shock", ["shock", "through the body", "through you", "electrocuted"])],
        model_answer="Water (which contains dissolved impurities) conducts electricity, so water could make a path from the live parts to your hand, and current could flow through your body, giving an electric shock.",
        hints=["Does water conduct?", "What path could form?", "What would happen to you?"],
        keywords="water conducts; current through body → shock",
        sample_pass=["Water conducts, so current could flow through your body and give a shock", "wet hands conduct and you could be electrocuted"],
        sample_fail=["Water makes the switch rust", "The switch gets cold"])

written("w16x_hazard_overload", 16, 1, "16d",
        stem="State why plugging too many appliances into one socket adaptor is dangerous.",
        points=[P("the total current is very large", ["large current", "too much current", "currents add", "total current"]),
                P("the cables overheat and may cause a fire", ["overheat", "fire", "melt", "hot"])],
        model_answer="The appliances' currents add up, so a very large total current flows in the adaptor and its cable. The cable can overheat, melt the insulation and start a fire.",
        hints=["How do the currents combine?", "What does a large current do to a cable?", "What could happen?"],
        keywords="large total current; overheating, fire",
        sample_pass=["The total current is too large and the cables overheat, causing a fire", "too much current makes the wires hot and could start a fire"],
        sample_fail=["The voltage gets too high", "The appliances get less current"])

# ---------------------------------------------------------------- L2
written("w16x_hazard_insulation", 16, 2, "16d",
        stem="Explain why a cable with damaged insulation is a hazard.",
        points=[P("the live wire may be exposed", ["exposed", "bare", "live wire"]),
                P("touching it could cause an electric shock, or a short circuit could cause a fire", ["shock", "fire", "short circuit", "electrocuted"])],
        model_answer="Damaged insulation may expose the live wire. Touching it could give a fatal electric shock, and if the bare wires touch each other a short circuit could cause sparks and a fire.",
        hints=["What does insulation cover?", "What if it is exposed?", "Two dangers."],
        keywords="exposed live wire; shock or fire",
        sample_pass=["The live wire could be exposed, giving an electric shock or a fire", "bare wires can cause a shock or a short circuit fire"],
        sample_fail=["The cable becomes heavy", "The fuse rating increases"])

written("w16x_fuse_how_written", 16, 2, "16e",
        stem="Explain how a fuse protects a circuit when the current becomes too large.",
        points=[P("the large current heats the thin fuse wire", ["heats", "gets hot", "heating"]),
                P("the wire melts and breaks the circuit, stopping the current", ["melts", "breaks the circuit", "stops the current", "blows"])],
        model_answer="When the current is too large, it heats the thin fuse wire until it melts. This breaks the circuit and stops the current, protecting the cable from overheating.",
        hints=["What does a large current do to a thin wire?", "What happens next?", "How does this protect the circuit?"],
        keywords="heats, melts, breaks circuit",
        sample_pass=["The large current heats the fuse wire, which melts and breaks the circuit", "the fuse wire gets hot and blows, stopping the current"],
        sample_fail=["The fuse reduces the voltage", "The fuse stores the extra current"])

written("w16x_earth_how_written", 16, 2, "16f",
        stem="Explain how the earth wire protects a person if the live wire touches the metal case of an appliance.",
        points=[P("the earth wire provides a low-resistance path from the case to earth", ["low-resistance path", "low resistance", "path to earth", "to the ground"]),
                P("a large current flows, which blows the fuse (cutting off the live supply)", ["large current", "fuse blows", "fuse melts", "cuts off"])],
        model_answer="The earth wire connects the metal case to earth through a low-resistance path. If the live wire touches the case, a large current flows to earth, which blows the fuse and cuts off the live supply, so the case does not stay live.",
        hints=["What does the earth wire connect?", "What happens to the current in a fault?", "What happens to the fuse?"],
        keywords="low-resistance path to earth; large current blows fuse",
        sample_pass=["It gives a low resistance path to earth, so a large current flows and the fuse blows", "the current goes to the ground and the fuse melts"],
        sample_fail=["The earth wire stops the current", "It makes the case an insulator"])

written("w16x_double_insulation_written", 16, 2, "16f",
        stem="Explain what is meant by a 'double-insulated' appliance and why it does not need an earth wire.",
        points=[P("the live parts are insulated twice / the case is made of an insulator (plastic)", ["plastic", "insulator", "insulated twice", "two layers", "non-conducting"]),
                P("so the case cannot become live, and an earth wire is not needed", ["cannot become live", "case cannot", "not needed", "no earth needed", "cannot give a shock"])],
        model_answer="A double-insulated appliance has its live parts insulated twice, usually with an outer case made of an insulator such as plastic. The case cannot become live, so an earth wire is not needed.",
        hints=["What is the case made of?", "Can it become live?", "So is earthing needed?"],
        keywords="insulating case; cannot become live; no earth needed",
        sample_pass=["The case is plastic, an insulator, so it cannot become live and no earth is needed", "the live parts are insulated twice so the case cannot give a shock"],
        sample_fail=["It has two earth wires", "It uses a larger fuse"])

written("w16x_switch_live_written", 16, 2, "16i",
        stem="Explain why the switch of an appliance must be connected in the live wire.",
        points=[P("so that switching off disconnects the appliance from the high potential (live)", ["disconnects", "isolates", "not connected to the live", "no longer live", "high potential"]),
                P("it is then safe to touch/repair the appliance when switched off", ["safe", "no shock", "repair", "touch"])],
        model_answer="With the switch in the live wire, switching off disconnects the appliance from the high-potential live supply, so it is safe to touch or repair when off.",
        hints=["Which wire is at high potential?", "What does switching off do?", "Why is that safer?"],
        keywords="disconnects live; safe when off",
        sample_pass=["So switching off disconnects the appliance from the live wire, making it safe to touch", "the appliance is no longer live when switched off, so it is safe to touch"],
        sample_fail=["So the appliance uses less power", "To make the fuse blow faster"])

written("w16x_fuse_live_written", 16, 2, "16i",
        stem="Explain why the fuse is placed in the live wire and not in the neutral wire.",
        points=[P("when the fuse blows, the live supply is disconnected from the appliance", ["live supply is disconnected", "disconnects the live", "cuts off the live", "isolates"]),
                P("if it were in the neutral, the appliance would still be live after the fuse blew", ["still be live", "still live", "remains live", "still connected"])],
        model_answer="When the fuse blows, it disconnects the appliance from the live supply. If the fuse were in the neutral wire, the appliance would stop working but would still be connected to the live wire, so it could still give a shock.",
        hints=["What does a blown fuse do?", "Which wire must be disconnected?", "What if it were in neutral?"],
        keywords="blown fuse cuts live; in neutral appliance stays live",
        sample_pass=["So a blown fuse disconnects the live supply; in the neutral the appliance would still be live", "the fuse cuts off the live wire, otherwise it remains live"],
        sample_fail=["Because neutral carries no current", "Because the fuse is brown"])

written("w16x_wire_colours_written", 16, 2, "16g",
        stem="State the colours of the live, neutral and earth wires in a modern plug.",
        points=[P("live: brown", ["brown"]),
                P("neutral: blue", ["blue"]),
                P("earth: green and yellow", ["green and yellow", "green/yellow", "green-yellow", "yellow and green"])],
        min_points=3,
        model_answer="Live: brown. Neutral: blue. Earth: green and yellow.",
        hints=["Three wires.", "Three colours.", "Match each."],
        keywords="brown, blue, green/yellow",
        sample_pass=["live brown, neutral blue, earth green and yellow", "brown, blue and green/yellow"],
        sample_fail=["red, black, green", "blue, brown, red"])

written("w16x_earth_wire_role", 16, 2, "16g",
        stem="State the purpose of the earth wire and what it is connected to inside an appliance.",
        points=[P("it is connected to the metal case", ["metal case", "case"]),
                P("it is a safety wire that carries current to earth only in a fault", ["safety", "fault", "to earth", "to the ground"])],
        model_answer="The earth wire is connected to the metal case of the appliance. It is a safety wire, carrying current to earth only if there is a fault.",
        hints=["What does it connect to?", "When does it carry current?", "Why?"],
        keywords="connected to metal case; safety, carries current in a fault",
        sample_pass=["It is connected to the metal case and carries current to earth in a fault", "a safety wire joined to the case"],
        sample_fail=["It carries the current in normal use", "It is connected to the fuse"])

# ---------------------------------------------------------------- L3
written("w16x_earth_case_l3", 16, 3, "16f",
        stem="A washing machine has a metal case. Explain what could happen in a fault if the earth wire were not connected.",
        points=[P("if the live wire touched the case, the case would become live (at 230 V)", ["case would become live", "case becomes live", "230", "live"]),
                P("a person touching it could get a fatal shock as current flows through them to earth", ["shock", "through them", "through the person", "electrocuted"]),
                P("the fuse might not blow, as there is no low-resistance path", ["fuse might not blow", "fuse does not blow", "no low-resistance path", "not blow"])],
        min_points=2,
        model_answer="If the live wire touched the case, the case would become live at 230 V. With no earth path the fuse might not blow, so a person touching the case could receive a fatal shock as current flows through them to earth.",
        hints=["What happens to the case in a fault?", "Is there a path for the fuse to blow?", "What happens to a person touching it?"],
        keywords="case becomes live; fuse may not blow; person shocked",
        sample_pass=["The case would become live and a person touching it would get a shock because the fuse might not blow", "it would be at 230 V, giving a fatal shock"],
        sample_fail=["Nothing would happen", "The machine would work better"])

written("w16x_fuse_neutral_l3", 16, 3, "16i",
        stem="A plug has its fuse wrongly placed in the neutral wire. Explain the danger when the fuse blows.",
        points=[P("the appliance stops working but is still connected to the live wire", ["still connected to the live", "still live", "remains live", "stays live"]),
                P("so a person repairing or touching it could get a shock", ["shock", "electrocuted", "dangerous to touch"])],
        model_answer="When the fuse in the neutral blows, the appliance stops working but is still connected to the live wire at 230 V. A person who thinks it is safe could touch a live part and get a shock.",
        hints=["Which wire is disconnected?", "Is the appliance still live?", "What is the danger?"],
        keywords="appliance still live; risk of shock",
        sample_pass=["The appliance is still connected to the live wire so someone could get a shock", "it stays live even though it stops working, so touching it could give a shock"],
        sample_fail=["The appliance works normally", "The fuse in neutral is safer"])

written("w16x_plug_identify_fault", 16, 3, "16h",
        stem="Fig. 1 shows a wired plug. Identify the fault and explain why it is dangerous.",
        points=[P("the live (brown) and neutral (blue) wires are swapped", ["swapped", "wrong way", "reversed", "live and neutral"]),
                P("the fuse is now in the neutral wire, so the appliance stays live when the fuse blows or is switched off", ["fuse is in the neutral", "stays live", "still live", "fuse in neutral"])],
        model_answer="The live (brown) and neutral (blue) wires have been swapped, so the fuse is now in the neutral wire. If the fuse blows, or the switch is off, the appliance is still connected to the live supply and could give a shock.",
        hints=["Check the colours at each terminal.", "Where is the fuse now?", "What is the danger?"],
        keywords="L and N swapped; fuse in neutral; stays live",
        sample_pass=["The live and neutral are swapped, so the fuse is in the neutral and the appliance stays live", "the brown and blue wires are the wrong way round; the fuse is in neutral"],
        sample_fail=["The earth wire is missing", "Nothing is wrong"],
        figure=lambda: figs3.plug_wiring("LN_swapped"))

written("w16x_plug_wiring_rules", 16, 3, "16h",
        stem="List three checks you would make to confirm that a three-pin plug is wired safely.",
        points=[P("brown to live (with fuse), blue to neutral, green/yellow to earth", ["brown", "blue", "green"]),
                P("the correct fuse rating is fitted", ["fuse rating", "correct fuse", "right fuse"]),
                P("the cable grip holds the outer sheath; no bare wire showing; screws tight", ["cable grip", "no bare", "tight", "sheath"])],
        min_points=2,
        model_answer="Check that brown goes to live (through the fuse), blue to neutral and green/yellow to earth; that the correct fuse rating is fitted; and that the cable grip holds the outer sheath, with no bare wire showing and all screws tight.",
        hints=["Are the colours on the right terminals?", "Is the fuse correct?", "Is the cable held firmly?"],
        keywords="colours to correct pins; correct fuse; cable grip, no bare wire",
        sample_pass=["Brown to live, blue to neutral, green and yellow to earth; the right fuse; the cable grip is tight", "check the fuse rating and that no bare wire shows"],
        sample_fail=["Check the plug is clean", "Check the colour of the plug case"])

written("w16x_cost_method", 16, 3, "16c",
        stem="Explain how to calculate the cost of running a 2 kW heater for 3 hours if electricity costs 30 cents per kWh.",
        points=[P("energy = power × time = 2 × 3 = 6 kWh", ["6 kwh", "2 × 3", "2 x 3", "power × time"]),
                P("cost = 6 × 30 = 180 cents ($1.80)", ["180", "1.80"])],
        model_answer="Energy used = power × time = 2 kW × 3 h = 6 kWh. Cost = 6 × 30 cents = 180 cents ($1.80).",
        hints=["Find the energy in kWh.", "kW × h.", "Multiply by the price."],
        keywords="6 kWh; 180 cents",
        sample_pass=["2 kW × 3 h = 6 kWh, so the cost is 6 × 30 = 180 cents", "6 kWh at 30 cents is $1.80"],
        sample_fail=["2 × 30 = 60 cents", "3 × 30 = 90 cents"])

written("w16x_cost_save", 16, 3, "16c",
        stem="Suggest two ways a household could reduce its electricity bill, explaining how each saves energy.",
        points=[P("use lower-power / more efficient appliances (e.g. LED lamps)", ["led", "lower power", "efficient", "energy-saving"]),
                P("use appliances for less time / switch off (no standby)", ["less time", "switch off", "standby", "turn off"]),
                P("so fewer kWh are used (energy = power × time)", ["fewer kwh", "less energy", "power × time", "less kwh"])],
        min_points=2,
        model_answer="Replace filament lamps with LED lamps (lower power for the same light) and switch appliances off instead of leaving them on standby (less time on). Both reduce the kWh used, since energy = power × time.",
        hints=["Energy = power × time.", "Reduce the power…", "…or the time."],
        keywords="lower power (LEDs); less time (switch off); fewer kWh",
        sample_pass=["Use LED lamps and switch off appliances on standby, so fewer kWh are used", "use more efficient appliances and use them for less time"],
        sample_fail=["Use more appliances", "Use thicker cables"])

written("w16x_fuse_choose_written", 16, 3, "16e",
        stem="A 230 V hair dryer has a power of 1.2 kW. Calculate its current and choose a suitable fuse from 3 A, 5 A and 13 A, giving a reason.",
        points=[P("I = P ÷ V = 1200 ÷ 230 = 5.2 A", ["5.2", "1200 / 230", "1200 ÷ 230"]),
                P("13 A fuse, because 5 A would blow and 13 A is the next rating above", ["13 a", "13"])],
        model_answer="I = P ÷ V = 1200 ÷ 230 = 5.2 A. A 13 A fuse should be used: a 5 A fuse would blow in normal use, and 13 A is the next rating above 5.2 A.",
        hints=["I = P ÷ V.", "Compare with the ratings.", "Choose the next one above."],
        keywords="I = 5.2 A; 13 A fuse",
        sample_pass=["I = 1200 / 230 = 5.2 A, so a 13 A fuse, as 5 A would blow", "5.2 A, choose 13 A"],
        sample_fail=["3 A fuse", "5 A fuse because it is closest"])

written("w16x_breaker_vs_fuse_written", 16, 3, "16e",
        stem="State two advantages of a circuit breaker over a fuse.",
        points=[P("it can be reset (no need to replace)", ["reset", "no need to replace", "reused", "switched back"]),
                P("it acts faster / more precisely", ["faster", "quicker", "more quickly", "more sensitive", "more precise"])],
        model_answer="A circuit breaker can be reset after it trips instead of being replaced, and it cuts off the current more quickly and at a more precise current.",
        hints=["What must be done after a fuse blows?", "Which reacts faster?", "Two advantages."],
        keywords="resettable; faster",
        sample_pass=["It can be reset and it acts faster", "you just switch it back on, and it is quicker than a fuse"],
        sample_fail=["It is cheaper and heavier", "It never trips"])

# ---------------------------------------------------------------- L4
written("w16x_earth_and_fuse_together", 16, 4, "16f",
        stem="Explain how the earth wire and the fuse together make a metal-cased appliance safe in a fault.",
        points=[P("in a fault, current flows from the live wire through the case and earth wire to earth", ["earth wire", "to earth", "through the case"]),
                P("the earth path has low resistance, so the current is very large", ["low resistance", "very large", "large current"]),
                P("the large current melts the fuse, disconnecting the live supply", ["fuse melts", "fuse blows", "disconnecting", "cuts off"])],
        min_points=2,
        model_answer="If the live wire touches the case, current flows through the case and the earth wire to earth. This path has a very low resistance, so the current is very large, which melts the fuse and disconnects the live supply; the case is no longer live.",
        hints=["Where does the fault current go?", "How large is it?", "What does it do to the fuse?"],
        keywords="current via earth wire; large current; fuse melts",
        sample_pass=["The current flows through the earth wire, which has low resistance, so the large current melts the fuse", "a large current goes to earth and the fuse blows, cutting off the live"],
        sample_fail=["The earth wire stops the current", "The fuse connects the case to earth"])

written("w16x_plug_no_earth_written", 16, 4, "16h",
        stem="Fig. 1 shows a plug for a metal toaster with the earth wire not connected. Explain why this is dangerous.",
        points=[P("if a fault makes the case live, there is no path to earth", ["no path to earth", "no earth path", "no earth"]),
                P("the fuse would not blow, so the case stays live", ["fuse would not blow", "fuse does not blow", "stays live", "remains live"]),
                P("touching the case could cause a fatal shock", ["shock", "electrocuted", "fatal"])],
        min_points=2,
        model_answer="If a fault connects the live wire to the metal case, there is no path to earth, so no large current flows and the fuse does not blow. The case stays live, and anyone touching it could get a fatal shock.",
        hints=["What does the earth wire usually do?", "Without it, does the fuse blow?", "What is the risk?"],
        keywords="no earth path; fuse does not blow; case live; shock",
        sample_pass=["There is no path to earth, so the fuse does not blow and the case stays live, giving a shock", "without earth the case remains live and could electrocute someone"],
        sample_fail=["The toaster will not heat", "It uses more electricity"],
        figure=lambda: figs3.plug_wiring("no_earth"))

written("w16x_cable_thickness", 16, 4, "16d",
        stem="Explain why a cooker needs a much thicker cable than a table lamp.",
        points=[P("the cooker takes a much larger current", ["larger current", "more current", "higher current"]),
                P("a thicker cable has lower resistance, so it does not overheat (less I²R heating)", ["lower resistance", "less resistance", "does not overheat", "less heating", "i²r", "i2r"])],
        model_answer="The cooker has a much higher power, so it takes a much larger current. A thicker cable has a lower resistance, so the heating in the cable (I²R) stays small and the cable does not overheat.",
        hints=["Which takes more current?", "How does thickness affect resistance?", "Link to heating."],
        keywords="larger current; thicker → lower R → less heating",
        sample_pass=["The cooker takes a larger current, and a thicker cable has lower resistance so it does not overheat", "more current needs a thick cable with less resistance so it does not overheat"],
        sample_fail=["Thicker cables give more voltage", "The cooker is heavier"])

written("w16x_hazard_three", 16, 4, "16d",
        stem="Describe three different electrical hazards in the home and how each can be avoided.",
        points=[P("damaged insulation — replace damaged cables", ["damaged insulation", "frayed", "bare wire"]),
                P("overloading sockets — do not plug too many appliances into one socket", ["overload", "too many", "adaptor"]),
                P("damp conditions / wet hands — keep water away, dry hands", ["damp", "wet", "water"])],
        min_points=3,
        model_answer="Damaged insulation can expose live wires: replace damaged cables. Overloading a socket can overheat cables and cause a fire: do not plug too many appliances into one socket. Damp conditions or wet hands can conduct current through the body: keep electrical equipment away from water and use it with dry hands.",
        hints=["Think about cables.", "Think about sockets.", "Think about water."],
        keywords="damaged insulation; overloading; damp/water",
        sample_pass=["Damaged insulation, overloading sockets, and using appliances with wet hands; replace cables, use fewer plugs, keep dry", "frayed wires, too many plugs in an adaptor and water near sockets"],
        sample_fail=["Bright lights and loud noise", "Using LED lamps"])

written("w16x_power_heater_resistance", 16, 4, "16b",
        stem="Explain why a heater with a lower-resistance element gives out more heat on the same 230 V supply.",
        points=[P("P = V² ÷ R", ["v2 / r", "v² / r", "v squared"]),
                P("with the same V, a smaller R gives a larger current and a larger power", ["larger current", "larger power", "more power", "more current", "smaller r"])],
        model_answer="P = V² ÷ R. With the same p.d., a smaller resistance allows a larger current (I = V ÷ R), so the power P = V I is larger and more heat is produced per second.",
        hints=["Which power equation includes V and R?", "V is fixed.", "What does a smaller R do?"],
        keywords="P = V²/R; smaller R → more current → more power",
        sample_pass=["P = V squared ÷ R, so with the same voltage a smaller resistance gives more power", "P is V squared over R, so a lower resistance gives a larger current and more power"],
        sample_fail=["A higher resistance gives more power", "Resistance does not matter"])

written("w16x_power_cable_loss", 16, 4, "16b",
        stem="Explain why the heating in a cable increases greatly if the current through it is doubled.",
        points=[P("power wasted in the cable = I² R", ["i2 r", "i² r", "i2r", "i squared"]),
                P("doubling I makes the heating four times larger", ["four times", "4 times", "quadruple", "×4", "x4"])],
        model_answer="The power converted to heat in the cable is P = I² R. Doubling the current makes I² four times larger, so the heating is four times greater.",
        hints=["Which equation gives heating in a wire?", "How does it depend on I?", "Double I…"],
        keywords="P = I²R; four times",
        sample_pass=["P = I²R, so doubling the current makes the heating four times larger", "the heating is I squared R, which quadruples"],
        sample_fail=["The heating doubles", "The heating halves"])

written("w16x_switch_lamp_change", 16, 4, "16i",
        stem="A student changes a light bulb after switching off at a switch that is (wrongly) in the neutral wire. Explain the danger.",
        points=[P("the lamp holder is still connected to the live wire (230 V)", ["still connected to the live", "still live", "230", "live"]),
                P("touching the holder's contacts could give an electric shock", ["shock", "electrocuted"])],
        model_answer="With the switch in the neutral, switching off stops the current, but the lamp holder is still connected to the live wire at 230 V. Touching the contacts while changing the bulb could give an electric shock.",
        hints=["Which wire does the switch break?", "Is the holder still connected to live?", "What could happen?"],
        keywords="holder still live; shock",
        sample_pass=["The lamp holder is still live, so the student could get a shock", "it is still connected to the live wire at 230 V, so touching it could give a shock"],
        sample_fail=["The bulb will be too bright", "It is completely safe"])

written("w16x_fuse_switch_live_why", 16, 4, "16i",
        stem="Both the fuse and the switch carry the same current whether they are in the live or neutral wire. Explain why they must still be in the live wire.",
        points=[P("the danger comes from the high potential of the live wire, not the size of the current", ["high potential", "live wire is at 230", "potential", "voltage"]),
                P("breaking the live wire leaves the appliance at 0 V (safe) when off or when the fuse blows", ["0 v", "safe", "not live", "disconnected from the live", "isolated"])],
        model_answer="Although the current is the same, the danger comes from the high potential of the live wire. Breaking the circuit in the live wire disconnects the appliance from 230 V, leaving it at about 0 V, so it is safe when switched off or when the fuse blows.",
        hints=["Is the current different in the two wires?", "What makes the live wire dangerous?", "What does breaking it achieve?"],
        keywords="danger is high potential; breaking live leaves appliance safe",
        sample_pass=["The live wire is at 230 V, so breaking it leaves the appliance safe at 0 V", "the danger is the high potential; disconnecting the live makes it safe"],
        sample_fail=["Because the live wire carries more current", "Because neutral is thinner"])

# ---------------------------------------------------------------- L5
written("w16x_eval_earth_plastic", 16, 5, "16f",
        stem="A student says that every appliance must be connected to an earth wire to be safe. Evaluate this statement.",
        points=[P("the statement is wrong / not always true", ["wrong", "not always", "incorrect", "not true"]),
                P("double-insulated appliances with insulating cases do not need earthing", ["double-insulated", "double insulated", "plastic case", "insulating case"]),
                P("appliances with metal cases do need earthing", ["metal case", "metal cases", "need earthing", "need an earth"])],
        min_points=2,
        model_answer="The statement is not always true. Appliances with metal cases must be earthed, but double-insulated appliances have insulating (plastic) cases that cannot become live, so they do not need an earth wire.",
        hints=["Which appliances need earthing?", "Which do not?", "Why?"],
        keywords="not always; metal cases need earth; double-insulated do not",
        sample_pass=["Not always: metal cases need earthing but double-insulated appliances with plastic cases do not", "wrong, double insulated appliances don't need an earth"],
        sample_fail=["Correct, all appliances need earth", "No appliance needs earth"])

written("w16x_eval_earth_rccb", 16, 5, "16f",
        stem="Evaluate why modern homes use RCCBs (residual current circuit breakers) as well as earthing and fuses.",
        points=[P("an RCCB detects a difference between the live and neutral currents (leakage)", ["difference", "leakage", "live and neutral", "imbalance"]),
                P("it trips very quickly at a small current, e.g. current through a person", ["very quickly", "small current", "through a person", "fast"]),
                P("a fuse only blows at large currents, so it may not protect a person from a shock", ["fuse only", "large currents", "may not protect", "too slow"])],
        min_points=2,
        model_answer="An RCCB compares the currents in the live and neutral wires. If some current leaks to earth, for example through a person, the currents differ and the RCCB trips within milliseconds, even for a small current. A fuse only blows when the current is large, so it might not protect a person from a shock.",
        hints=["What does an RCCB compare?", "How fast and at what current?", "What can a fuse not do?"],
        keywords="detects live/neutral difference; fast, small current; fuse needs large current",
        sample_pass=["An RCCB detects a difference between live and neutral currents and trips quickly at small currents, unlike a fuse", "it trips fast if current leaks through a person; a fuse only blows at large currents"],
        sample_fail=["RCCBs make appliances cheaper", "RCCBs increase the voltage"])

written("w16x_eval_plug_design", 16, 5, "16h",
        stem="Evaluate the design features of a three-pin plug that make it safe.",
        points=[P("fuse in the live wire protects against overheating", ["fuse", "live"]),
                P("earth pin is longer so it connects first", ["earth pin", "longer", "connects first"]),
                P("plastic/rubber case insulates; cable grip prevents wires pulling out; brass pins conduct well", ["insulat", "plastic", "cable grip", "brass", "pulling out"])],
        min_points=2,
        model_answer="The fuse in the live wire melts if the current is too large, protecting the cable. The earth pin is longer, so the appliance is earthed before the live connection is made. The plastic case insulates the user, the cable grip stops the wires being pulled out, and the brass pins conduct well without corroding.",
        hints=["What protects against too much current?", "What about the earth pin?", "What about the case and cable grip?"],
        keywords="fuse in live; long earth pin; insulating case, cable grip",
        sample_pass=["The fuse is in the live wire, the earth pin is longer, and the plastic case insulates", "a cable grip stops the wires pulling out and the fuse protects the cable"],
        sample_fail=["The plug is heavy", "The plug is colourful"])

written("w16x_eval_plug_student", 16, 5, "16h",
        stem="A student wires a plug with the brown wire to the earth pin and the green/yellow wire to the live pin. Evaluate the safety of this plug.",
        points=[P("very dangerous", ["dangerous", "unsafe", "very dangerous"]),
                P("the metal case would be connected to the live supply (230 V)", ["case would be live", "case live", "230", "connected to the live"]),
                P("touching the case would give a fatal shock immediately", ["shock", "electrocuted", "fatal"])],
        min_points=2,
        model_answer="This is extremely dangerous. The earth wire, which is connected to the metal case, would be joined to the live pin, so the case would be at 230 V as soon as the plug is in. Anyone touching the case would receive a fatal shock.",
        hints=["What is the green/yellow wire connected to inside the appliance?", "Which pin is it on now?", "What is the result?"],
        keywords="dangerous; case connected to live; fatal shock",
        sample_pass=["Very dangerous: the metal case is connected to the live supply and would give a fatal shock", "unsafe, the case would be at 230 V"],
        sample_fail=["Safe, the colours don't matter", "Safe if the fuse is correct"])

written("w16x_eval_cost_claim_written", 16, 5, "16c",
        stem="A student says: 'A 3 kW heater costs ten times as much to run as a 300 W TV.' Evaluate this statement.",
        points=[P("it is only true if they are used for the same time", ["same time", "only true if", "equal time"]),
                P("cost depends on energy = power × time (kWh), not power alone", ["power × time", "power x time", "kwh", "energy", "time"]),
                P("the TV used for much longer could cost as much or more", ["longer", "more hours", "could cost more", "as much"])],
        min_points=2,
        model_answer="It is only true if they are used for the same time. The cost depends on the energy used in kWh, which is power × time. If the TV is used for ten times longer, it costs as much as the heater.",
        hints=["What does cost depend on?", "Energy = power × time.", "What about the times?"],
        keywords="only for same time; cost ∝ kWh = P × t",
        sample_pass=["Only true for the same time, since cost depends on energy = power × time", "the TV could cost more if used for longer; cost depends on kWh"],
        sample_fail=["True, power decides the cost", "False, TVs always cost more"])

written("w16x_eval_standby_claim", 16, 5, "16c",
        stem="A student says leaving devices on standby is not worth worrying about because each uses only a few watts. Evaluate this statement.",
        points=[P("standby power is small but it is used for many hours (all day, every day)", ["many hours", "all day", "every day", "long time", "24 hours"]),
                P("the energy (kWh) adds up over a year and across many devices", ["adds up", "over a year", "many devices", "kwh"]),
                P("this wastes money and energy (increases bills / emissions)", ["waste", "money", "cost", "bill", "emissions"])],
        min_points=2,
        model_answer="The statement is weak. Although standby power is only a few watts, devices are left on standby for many hours, every day, so the energy (kWh) adds up over a year and across many devices. This wastes energy and money, so switching off is worthwhile.",
        hints=["How long are devices on standby?", "How does the energy add up?", "Is it worth switching off?"],
        keywords="small power but long time; kWh adds up; wastes money",
        sample_pass=["Each uses little power but for many hours every day, so the kWh add up over a year and waste money", "the energy adds up across many devices and costs money"],
        sample_fail=["Correct, standby uses no energy", "Standby makes devices last longer"])

written("w16x_eval_overload_claim", 16, 5, "16d",
        stem="A student says it is safe to plug a 2 kW heater, a 2 kW kettle and a 1 kW iron into one 13 A adaptor because each is below 13 A. Evaluate this statement.",
        points=[P("the statement is wrong", ["wrong", "unsafe", "incorrect", "not safe"]),
                P("the currents add: total = 5000 ÷ 230 ≈ 22 A", ["22", "21.7", "add", "total"]),
                P("this exceeds 13 A, overheating the adaptor/cable and risking fire", ["exceeds", "more than 13", "overheat", "fire"])],
        min_points=2,
        model_answer="The statement is wrong. The appliances are in parallel, so their currents add: the total power is 5000 W, giving 5000 ÷ 230 ≈ 22 A. This is more than 13 A, so the adaptor and its cable could overheat and start a fire (or the fuse will blow).",
        hints=["Do the currents add?", "Find the total current.", "Compare with 13 A."],
        keywords="wrong; currents add to ≈ 22 A > 13 A; overheating",
        sample_pass=["Wrong, the currents add to about 22 A, which exceeds 13 A and could overheat the cable", "unsafe: total 5000 W gives 21.7 A, more than 13 A"],
        sample_fail=["Correct, each is below 13 A", "Safe because they are in parallel"])

written("w16x_eval_extension_reel", 16, 5, "16d",
        stem="An extension cable reel carries a warning to unwind it fully when using a high-power heater. Evaluate why.",
        points=[P("a large current heats the cable (I²R)", ["heats", "i²r", "i2r", "large current", "heat"]),
                P("when coiled, the heat cannot escape easily, so the temperature rises", ["cannot escape", "trapped", "coiled", "heat builds up"]),
                P("the insulation could melt, causing a short circuit or fire", ["melt", "fire", "short circuit"])],
        min_points=2,
        model_answer="A high-power heater draws a large current, which heats the cable (I²R). When the cable is coiled, the heat cannot escape easily, so its temperature rises. The insulation could melt, causing a short circuit or a fire, so the cable should be unwound fully.",
        hints=["What does a large current do to a cable?", "What does coiling do to the heat?", "What could happen?"],
        keywords="current heats cable; coiled traps heat; insulation melts/fire",
        sample_pass=["The large current heats the cable and when coiled the heat cannot escape, so the insulation could melt and cause a fire", "heat builds up in the coiled cable, risking fire"],
        sample_fail=["Coiling increases the voltage", "Unwinding makes the heater hotter"])
