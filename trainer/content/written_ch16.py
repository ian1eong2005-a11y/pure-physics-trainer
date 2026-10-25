"""Chapter 16 Practical Electricity: written-answer questions, two per level (kWh, plug wiring, hazards, fuses and circuit
breakers, earthing and double insulation, evaluating fuse choices)."""
from .. import figs3
from ..marker import Pitfall, Point
from .base import written

P = Point
PF = Pitfall

# ---------------------------------------------------------------- L1
written("w16_define_kwh", 16, 1, "16c",
        stem="State what is meant by one kilowatt-hour (kWh).",
        points=[P("the energy transferred by a 1 kW appliance (power of 1 kilowatt) in one hour", ["1 kw", "one kilowatt", "1 kilowatt", "1000 w"]),
                P("in a time of one hour (it is a unit of energy, = 3.6 MJ)", ["one hour", "1 hour", "an hour", "3.6"])],
        pitfalls=[PF(["unit of power", "measures power", "a power of"], "The kilowatt-hour is a unit of ENERGY, not power: it is the energy transferred by a 1 kW device in 1 hour.")],
        model_answer="One kilowatt-hour is the energy transferred by an appliance of power 1 kW working for one hour. It is a unit of energy equal to 3.6 million joules.",
        hints=["kilowatt × hour: a power multiplied by a time gives what quantity?",
               "Think of a 1 kW heater left on for 1 hour.",
               "State the power, the time and the quantity being measured."],
        keywords="energy used by a 1 kW appliance in 1 hour",
        sample_pass=["The energy used by a 1 kW appliance in one hour", "the amount of energy transferred when 1 kilowatt is used for an hour"],
        sample_fail=["A unit of power equal to 1000 W", "The current drawn by a kettle in one hour"])

written("w16_wire_colours", 16, 1, "16g",
        stem="Fig. 1 shows a three-pin plug. Name the three wires and state the colour of the insulation on each.",
        points=[P("live: brown", ["live brown", "brown live", "brown is live", "live is brown", "brown for live", "brown wire is the live"]),
                P("neutral: blue", ["neutral blue", "blue neutral", "blue is neutral", "neutral is blue", "blue for neutral"]),
                P("earth: green and yellow (striped)", ["earth green", "green and yellow earth", "earth is green", "green yellow", "green/yellow", "yellow and green"])],
        model_answer="The live wire is brown, the neutral wire is blue, and the earth wire is green and yellow.",
        hints=["There are three wires: live, neutral and earth.",
               "One is brown, one is blue, one is striped green and yellow.",
               "Match each name to its colour."],
        keywords="live brown; neutral blue; earth green/yellow",
        figure=lambda: figs3.plug_wiring(),
        sample_pass=["Live is brown, neutral is blue and earth is green and yellow", "brown = live, blue = neutral, green/yellow = earth"],
        sample_fail=["Live is red, neutral is black, earth is green", "Positive is red and negative is black"])

# ---------------------------------------------------------------- L2
written("w16_three_hazards", 16, 2, "16d",
        stem="Describe three situations in which using mains electricity can be dangerous, and say why each is dangerous.",
        points=[P("damaged insulation: exposed live wire can be touched, giving an electric shock, or can touch other conductors causing a short circuit", ["damaged insulation", "worn insulation", "frayed", "exposed wire", "bare wire", "insulation is damaged"]),
                P("overheating of cables: too large a current (overloaded socket / too thin cable) heats the wires, which can melt the insulation and start a fire", ["overheat", "overload", "too many appliances", "too much current", "fire", "melt"]),
                P("damp conditions: water conducts, so wet hands or appliances give a path for current through the body, causing a shock", ["damp", "wet", "water conducts", "moisture", "bathroom"])],
        min_points=2,
        model_answer="Damaged insulation can expose the live wire, so anyone touching it receives a shock, and bare wires touching each other cause a short circuit. Overheating of cables happens when too large a current flows, for example when a socket is overloaded, and the hot wire can melt its insulation and start a fire. In damp conditions water conducts electricity, so wet hands or wet appliances provide a path for current through the body, giving a shock.",
        hints=["The syllabus names three hazards: think about the wire's covering, how hot a cable gets, and water.",
               "For each, say what goes wrong and what harm results (shock or fire).",
               "Describe at least two of the three with reasons."],
        keywords="damaged insulation (shock, short circuit); overheated cables (fire); damp conditions (water conducts, shock)",
        sample_pass=["Damaged insulation exposes live wires and can give a shock; overloaded cables overheat and can cause a fire; damp conditions let current pass through the body because water conducts",
                     "worn insulation can cause a shock, too much current overheats the cable and starts a fire, wet hands conduct electricity"],
        sample_fail=["Using too little electricity makes the lights dim", "Switching appliances off wastes energy"])

written("w16_fuse_purpose", 16, 2, "16e",
        stem="State the purpose of a fuse in a plug, and explain how it works.",
        points=[P("to protect the appliance and cable (and prevent fire) by cutting off the current when it becomes too large", ["protect", "prevents fire", "stop a fire", "cuts off", "breaks the circuit", "too large a current", "too much current", "excess current", "fault"]),
                P("it is a thin wire that melts (blows) when the current exceeds its rating, breaking the circuit", ["melts", "blows", "thin wire", "exceeds its rating", "above its rating", "more than the rated"])],
        model_answer="A fuse protects the appliance and its cable: if a fault makes the current too large, the thin fuse wire heats up and melts, breaking the circuit and cutting off the current before the cable overheats and catches fire. The fuse is chosen with a rating slightly above the normal operating current.",
        hints=["What would happen to a cable if a fault let a very large current flow?",
               "What is a fuse made of, and what happens to it when too much current flows?",
               "State the purpose and describe the melting action."],
        keywords="protects against excess current; thin wire melts when current exceeds rating, breaking the circuit",
        sample_pass=["It protects the appliance from too large a current: the thin wire melts and breaks the circuit", "the fuse blows when the current exceeds its rating, cutting off the supply to prevent a fire"],
        sample_fail=["It increases the current to the appliance", "It stores charge so the appliance keeps working in a power cut"])

# ---------------------------------------------------------------- L3
written("w16_fuse_in_live", 16, 3, "16i",
        stem="Explain why the fuse and the switch of an appliance are always connected in the live wire and not in the neutral wire.",
        points=[P("the live wire is at a high potential (about 230 V) while the neutral is at about 0 V (earth potential)", ["high potential", "230", "high voltage", "neutral is at 0", "neutral is at earth potential", "neutral is at zero", "live carries the high"]),
                P("if the fuse/switch were in the neutral, the appliance would still be connected to the live wire when the fuse blew or the switch was off", ["still connected to the live", "still live", "remain live", "would still be live", "connected to the high voltage", "still at 230"]),
                P("so someone touching the appliance could get a shock; with the fuse/switch in the live wire the appliance is isolated from the high voltage", ["shock", "isolated", "disconnects the appliance from the live", "cuts off the live", "safe to touch", "no longer live"])],
        min_points=2,
        model_answer="The live wire is at a high potential of about 230 V, while the neutral wire is at about 0 V. If the fuse or switch were in the neutral wire, then when the fuse blew or the switch was opened the appliance would still be connected to the live wire and would remain at 230 V, so anyone touching a faulty part could receive a shock. Placing the fuse and switch in the live wire isolates the appliance from the high voltage.",
        hints=["Which of the two wires is at the dangerous high voltage?",
               "Imagine the switch in the neutral wire and the switch 'off': is the appliance still connected to the live wire?",
               "Explain the potentials and the consequence for safety."],
        keywords="live at 230 V, neutral at 0 V; fuse/switch in neutral leaves appliance live; shock risk; in live wire isolates it",
        sample_pass=["The live wire is at 230 V; if the fuse were in the neutral, the appliance would still be live when it blew and could give a shock",
                     "the switch in the live wire disconnects the appliance from the high voltage, in the neutral it would stay live"],
        sample_fail=["Because the live wire is thicker so it can hold the fuse", "The neutral wire carries more current"])

written("w16_earth_metal_case", 16, 3, "16f",
        stem="Fig. 1 shows a plug with an earth wire. Explain why appliances with metal cases are connected to the earth wire.",
        points=[P("if a fault makes the live wire touch the metal case, the case would become live (at 230 V)", ["live wire touches the case", "case becomes live", "case is live", "fault", "live touches the metal", "casing becomes live"]),
                P("the earth wire provides a low-resistance path so a large current flows to earth", ["low resistance", "large current", "current flows to earth", "flows to the ground", "path to earth", "current to earth"]),
                P("this large current blows the fuse, cutting off the supply, so the case cannot give a shock", ["blows the fuse", "fuse melts", "fuse blows", "breaks the circuit", "cuts off the supply", "cannot give a shock", "prevents a shock", "no shock"])],
        min_points=2,
        model_answer="If a fault allowed the live wire to touch the metal case, the case would become live at 230 V and anyone touching it would receive a shock. The earth wire connects the case to earth through a low-resistance path, so when this happens a very large current flows to earth. This large current blows the fuse, cutting off the supply, so the case cannot remain live.",
        hints=["What could happen inside a faulty appliance to make its metal case dangerous?",
               "Where does the earth wire let the current go, and how big is that current?",
               "Describe the fault, the current to earth, and what the fuse does."],
        keywords="fault makes case live; earth wire gives low-resistance path, large current to earth; fuse blows, supply cut off",
        figure=lambda: figs3.plug_wiring(),
        sample_pass=["If the live wire touches the case, the earth wire lets a large current flow to earth which blows the fuse, so the case does not stay live",
                     "the earth wire gives a low resistance path for current if the case becomes live, and the big current melts the fuse"],
        sample_fail=["The earth wire makes the appliance work on 230 V", "It stops the appliance from getting too hot"])

# ---------------------------------------------------------------- L4
written("w16_double_insulation", 16, 4, "16f",
        stem="A hair dryer has a plastic case and is marked 'double insulated'. Explain what double insulation means and why such an appliance does not need an earth wire.",
        points=[P("the live parts are insulated and, in addition, the case itself is an insulator (plastic)", ["two layers", "plastic case", "case is an insulator", "case is plastic", "second layer", "insulating case", "two layers of insulation"]),
                P("so even if the internal insulation fails, the case cannot become live", ["cannot become live", "case cannot be live", "never becomes live", "no live part can be touched", "case will not conduct", "cannot conduct"]),
                P("there is no metal part that could carry current to the user, so earthing is unnecessary", ["no metal", "nothing to earth", "no conducting case", "earth wire is not needed", "unnecessary", "no need for an earth"])],
        min_points=2,
        model_answer="Double insulation means that the live parts inside are insulated and the outer case is itself made of an insulator such as plastic, giving two layers of insulation. Even if the internal insulation fails, the plastic case cannot become live, and there is no exposed metal part that could carry current to the user. So there is nothing that needs earthing, and the appliance uses only live and neutral wires.",
        hints=["What are the two layers of insulation?",
               "If the inner insulation failed, could the case conduct electricity to the user?",
               "Explain why there is nothing for an earth wire to protect."],
        keywords="insulated live parts plus insulating (plastic) case; case cannot become live; no metal to earth",
        sample_pass=["The wiring is insulated and the case is plastic, so even if the inner insulation fails the case cannot become live and there is no metal part to earth",
                     "two layers of insulation; the plastic case cannot conduct so no earth wire is needed"],
        sample_fail=["Double insulation means it works on two voltages", "The plastic case is earthed through the floor"])

written("w16_plug_fault", 16, 4, "16h",
        stem="Fig. 1 shows how a student has wired a three-pin plug. Identify the mistake and explain why it is dangerous.",
        points=[P("the live (brown) and neutral (blue) wires are swapped: brown is connected to the neutral pin and blue to the live (fused) pin", ["swapped", "wrong way round", "brown is connected to the neutral", "blue is connected to the live", "live and neutral are reversed", "reversed", "brown to the neutral pin", "blue to the live"]),
                P("so the fuse and the appliance's switch are now in the neutral wire, not the live wire", ["fuse is in the neutral", "switch is in the neutral", "fuse in the neutral", "not in the live", "fuse no longer in the live"]),
                P("so when the fuse blows or the switch is off, the appliance stays connected to the live supply and can give a shock", ["still live", "remains live", "still connected to the live", "shock", "stays at 230"])],
        min_points=2,
        model_answer="The brown (live) wire has been connected to the neutral pin and the blue (neutral) wire to the live pin, so live and neutral are swapped. The fuse and the appliance's switch are therefore in the neutral wire instead of the live wire. When the switch is off or the fuse has blown, the appliance is still connected to the live supply and could give a shock.",
        hints=["Check the colour of the wire going to each pin. Which pin should the brown wire go to?",
               "If the brown and blue wires are swapped, where does that put the fuse?",
               "Name the mistake and explain the danger."],
        keywords="live and neutral swapped; fuse and switch now in neutral; appliance stays live when off",
        figure=lambda: figs3.plug_wiring("LN_swapped"),
        sample_pass=["The live and neutral wires are swapped, so the fuse is in the neutral and the appliance stays live when the fuse blows",
                     "brown is on the neutral pin and blue on the live pin: the switch is in the neutral so the appliance can still give a shock when switched off"],
        sample_fail=["The earth wire is too long", "The plug has no fuse at all"])

# ---------------------------------------------------------------- L5
written("w16_claim_bigger_fuse", 16, 5, "16e",
        stem="A 3 A fuse in the plug of a 700 W lamp keeps blowing. A student suggests replacing it with a 13 A fuse 'so that it will not blow again'. Evaluate this suggestion.",
        points=[P("the normal current is I = P ÷ V = 700 ÷ 230 ≈ 3.0 A, so a 3 A fuse is marginal; the correct choice is the next rating above the normal current, 5 A", ["700 / 230", "700 ÷ 230", "3.0 a", "about 3 a", "3 amps", "5 a", "5 amp", "next rating", "just above"]),
                P("a 13 A fuse is far too large: a fault current of up to 13 A could flow without blowing it, overheating the cable and risking a fire", ["too large", "too big", "too high", "13 a would not blow", "would not blow", "overheat", "fire", "not protect", "does not protect"]),
                P("the fuse keeps blowing because its rating is barely above the operating current (or because of a fault); the fuse should be slightly above the normal current, not much higher", ["slightly above", "just above", "a little above", "not much higher", "barely above", "fault"])],
        min_points=2,
        model_answer="The lamp's normal current is I = P ÷ V = 700 ÷ 230 ≈ 3.0 A, so a 3 A fuse is only just adequate and blows easily. The suggestion of a 13 A fuse is unsafe: a fuse must have a rating only slightly above the normal current so that it blows soon after a fault. With a 13 A fuse, a fault current of up to 13 A could flow without the fuse blowing, overheating the cable and risking a fire. The correct replacement is a 5 A fuse.",
        hints=["Work out the normal current: I = P ÷ V with V = 230 V.",
               "What is the rule for choosing a fuse rating? What goes wrong if the rating is much too high?",
               "Give the current, judge the 13 A suggestion, and state the right fuse."],
        keywords="I = 700/230 ≈ 3 A; 13 A too large, would not blow on a fault, fire risk; choose 5 A (just above normal current)",
        sample_pass=["The current is 700/230 = 3 A so the 3 A fuse is marginal; a 13 A fuse is far too high and would let a fault current overheat the cable; a 5 A fuse is the right choice",
                     "13 A would not blow when a fault happens so it does not protect the cable; the fuse should be just above 3 A, i.e. 5 A"],
        sample_fail=["Good idea, a bigger fuse always makes the lamp brighter", "Use a 1 A fuse so that it blows even faster"])

written("w16_choose_fuse_justify", 16, 5, "16e",
        stem="A 2 kW electric heater is to be connected to the 230 V mains. Calculate the current it takes, choose a suitable fuse from 3 A, 5 A and 13 A, and justify your choice.",
        points=[P("I = P ÷ V = 2000 ÷ 230 ≈ 8.7 A", ["2000 / 230", "2000 ÷ 230", "8.7", "8.69", "8.7 a", "about 9 a", "p / v", "p divided by v"]),
                P("choose the 13 A fuse", ["13 a", "13 amp", "thirteen"]),
                P("because the fuse rating must be above the normal current (so it does not blow in normal use) but as close to it as possible (so it blows quickly on a fault); 3 A and 5 A would blow immediately", ["above the normal current", "higher than the normal", "would blow immediately", "would blow straight away", "3 a and 5 a would blow", "too small", "close to the normal", "just above", "nearest rating above"])],
        min_points=2,
        model_answer="I = P ÷ V = 2000 ÷ 230 ≈ 8.7 A. The 3 A and 5 A fuses would melt as soon as the heater was switched on, so the 13 A fuse must be used. It is the smallest available rating above the normal current of 8.7 A, so it allows normal operation but will still blow if a fault makes the current rise above 13 A.",
        hints=["Use P = V I to find the current.",
               "The fuse must not blow in normal use. Which ratings are below 8.7 A?",
               "State the current, choose the fuse, and give the reason."],
        keywords="I = 2000/230 ≈ 8.7 A; 13 A fuse; smallest rating above the normal current",
        sample_pass=["I = 2000/230 = 8.7 A, so choose the 13 A fuse because 3 A and 5 A would blow immediately and 13 A is the nearest rating above the normal current",
                     "the current is about 8.7 amps so the 13 A fuse is needed, being the smallest one higher than the working current"],
        sample_fail=["Choose the 3 A fuse because it is the safest", "The heater does not need a fuse because it has a thermostat"])
