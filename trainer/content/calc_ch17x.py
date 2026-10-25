"""Chapter 17 Magnetism (6091) bank extension: data-reading and calculation templates (data-reading counts as calculation for
descriptive chapters), 10 per level, each LO at least twice. Contexts adapted from the question bank (SEAB 2016-2025: iron and
steel bars picking up pins, magnetising in a solenoid, plotting compasses round a bar magnet, attraction and repulsion tests)."""
from .. import figs3
from .base import fmt, md_table, mk, mkt, nice, template


# ================================================================== L1
@template("c17x_pins_iron_steel", chapter=17, level=1, lo="17c")
def pins_iron_steel(rng):
    i_on, s_on = nice(rng, 20, 24, 30), nice(rng, 12, 15)
    i_off, s_off = nice(rng, 0, 1), nice(rng, 8, 10)
    which = rng.choice(["iron", "steel"])
    ans = i_on if which == "iron" else s_on
    return mk(rng, ans, [((s_on if which == "iron" else i_on), f"That is the other bar; read the row for {which}."), ((i_off if which == "iron" else s_off) + 1, "Read the value while the magnet is touching the bar."), (i_on + s_on, "Read one value.")],
              "pins", f"Bars of iron and steel touch a strong magnet and pick up pins.\n\n{md_table(['bar', 'pins held while touching magnet', 'pins held after magnet removed'], [['iron', i_on, i_off], ['steel', s_on, s_off]])}\n\nHow many pins does the **{which}** bar hold while touching the magnet?",
              "read the table", [f"{which}, while touching: **{ans} pins**"],
              ["Find the right row.", "Find the right column.", "Read the value."], dp=0)


@template("c17x_retained_pins", chapter=17, level=1, lo="17c")
def retained_pins(rng):
    rows = [("iron", nice(rng, 22, 25), nice(rng, 0, 1)), ("steel", nice(rng, 14, 16), nice(rng, 9, 11))]
    ans = "steel"
    wrongs = {"iron": "Iron loses almost all its magnetism when the magnet is removed (temporary magnet).",
              "both equally": "Compare the 'after' column.", "neither": "Steel keeps much of its magnetism."}
    table = md_table(["bar", "pins while touching magnet", "pins after magnet removed"], [[n, a, b] for n, a, b in rows])
    return mkt(rng, ans, wrongs, f"{table}\n\nWhich material would make the better permanent magnet?",
               "a permanent magnet keeps its magnetism: most pins held after removal", ["steel keeps more pins after removal → **steel**"],
               ["Which bar keeps its magnetism?", "Look at the 'after' column.", "More pins kept → permanent."])


@template("c17x_induced_pole_end", chapter=17, level=1, lo="17b")
def induced_pole_end(rng):
    near = rng.choice(["N", "S"])
    ans = "S" if near == "N" else "N"
    wrongs = {near: "The near end gets the OPPOSITE pole, which is why it is attracted.", "no pole": "The bar becomes an induced magnet.", "both N and S at the near end": "Each end has one pole."}
    return mkt(rng, ans, wrongs, f"An unmagnetised iron bar is placed near the **{near}** pole of a bar magnet (as in Fig. 1). What pole is induced at the end of the bar NEAREST the magnet?",
               "induced pole at the near end is opposite to the magnet's pole", [f"near a {near} pole → near end becomes **{ans}**"],
               ["Induced magnetism gives attraction.", "Unlike poles attract.", "Opposite pole at the near end."], figure=figs3.induced_magnetism("iron"))


@template("c17x_induced_far_end", chapter=17, level=1, lo="17b")
def induced_far_end(rng):
    near = rng.choice(["N", "S"])
    ans = near
    wrongs = {("S" if near == "N" else "N"): "That is the near end's pole; the FAR end has the same pole as the magnet.",
              "no pole": "Both ends of the induced magnet have poles.", "it depends on the length": "The far end always has the same pole as the magnet."}
    return mkt(rng, ans, wrongs, f"An iron nail is held by induction near the **{near}** pole of a magnet (as in Fig. 1). What pole is induced at the FREE (far) end of the nail?",
               "near end: opposite pole; far end: same pole as the magnet", [f"far end → **{ans}**"],
               ["What pole is at the near end?", "The opposite pole.", "The far end has the other pole."], figure=figs3.induced_magnetism("iron"))


@template("c17x_stroke_magnetise", chapter=17, level=1, lo="17b")
def stroke_magnetise(rng):
    strokes = [10, 20, 30, 40]
    pins = [nice(rng, 3, 4), nice(rng, 7, 8), nice(rng, 10, 11), nice(rng, 12, 13)]
    k = rng.randrange(4)
    return mk(rng, pins[k], [(pins[(k + 1) % 4], "Read the row for this number of strokes."), (strokes[k], "That is the number of strokes, not pins."), (pins[k] + 5, "Read the table.")],
              "pins", f"A steel needle is stroked with a magnet and then tested.\n\n{md_table(['number of strokes', 'pins picked up'], [[s, p] for s, p in zip(strokes, pins)])}\n\nHow many pins does it pick up after **{strokes[k]}** strokes?",
              "read the table (more strokes → stronger magnet)", [f"after {strokes[k]} strokes: **{pins[k]} pins**"],
              ["Find the number of strokes.", "Read across.", "Stronger with more strokes."], dp=0)


@template("c17x_magnetic_material_pick", chapter=17, level=1, lo="17a")
def magnetic_material_pick(rng):
    mags = ["iron", "steel", "nickel", "cobalt"]
    non = ["copper", "aluminium", "brass", "plastic", "wood", "gold"]
    ans = rng.choice(mags)
    wrongs = {n: f"{n.capitalize()} is not a magnetic material." for n in rng.sample(non, 3)}
    return mkt(rng, ans, wrongs, f"{md_table(['material', 'attracted to a magnet?'], [[ans, '?']] + [[n, '?'] for n in list(wrongs)])}\n\nWhich material is attracted to a magnet?",
               "magnetic materials: iron, steel, nickel, cobalt", [f"**{ans}**"],
               ["Recall the magnetic materials.", "Iron, steel, nickel, cobalt.", "Pick the one listed."])


@template("c17x_compass_field_direction", chapter=17, level=1, lo="17d")
def compass_field_direction(rng):
    position = rng.choice(["right", "left"])
    flip = rng.choice([False, True])
    base = "left"
    if flip:
        base = "right"
    ans = f"to the {base}"
    other = "right" if base == "left" else "left"
    wrongs = {f"to the {other}": "The needle's N points along the field: away from N, towards S.", "upwards": "Near the ends the field runs along the magnet's axis.", "it spins round": "It settles along the field."}
    return mkt(rng, ans, wrongs, f"Fig. 1 shows a plotting compass placed at the **{position}** end of a bar magnet. In which direction does the compass N pole point?",
               "compass N points along the field: away from the magnet's N pole, towards its S pole", [f"**{ans}**"],
               ["Which pole of the magnet is nearest?", "Field lines leave N and enter S.", "The compass points along the field."], figure=figs3.compass_near_magnet(position, flip=flip))


@template("c17x_earth_pole_compass", chapter=17, level=1, lo="17d")
def earth_pole_compass(rng):
    wrongs = {"a magnetic north pole": "The compass N pole is attracted to it, so it must be a magnetic SOUTH pole.",
              "not a magnetic pole": "It is where the Earth's field lines enter.", "a positive charge": "Magnetism is not electric charge."}
    table = md_table(["observation", ""], [["compass N pole points to", "geographic North Pole"]])
    return mkt(rng, "a magnetic south pole", wrongs, f"{table}\n\nUsing the rule for attraction between poles, what kind of magnetic pole is near the Earth's geographic North Pole?",
               "unlike poles attract: the compass N is pulled towards a S pole", ["the compass N is attracted there → **magnetic south pole**"],
               ["What attracts a N pole?", "A S pole.", "So the geographic north has a magnetic S pole."])


# ================================================================== L2
@template("c17x_attract_repel_table", chapter=17, level=2, lo="17a")
def attract_repel_table(rng):
    pairs = [("A", "N", "N"), ("B", "N", "S"), ("C", "S", "S"), ("D", "S", "N")]
    rng.shuffle(pairs)
    target = rng.choice(["attract", "repel"])
    ans = " and ".join(sorted(n for n, a, b in pairs if (a != b) == (target == "attract")))
    opts = ["A and C", "B and D", "A and B", "C and D"]
    wrongs = {o: "Like poles repel; unlike poles attract." for o in opts if o != ans}
    table = md_table(["pair", "pole of first magnet", "pole of second magnet"], [[n, a, b] for n, a, b in pairs])
    return mkt(rng, ans, dict(list(wrongs.items())[:3]), f"Poles of bar magnets are brought together.\n\n{table}\n\nWhich pairs **{target}**?",
               "like poles repel, unlike poles attract", [f"**{ans}**"],
               ["Like or unlike?", "Unlike attract.", "Like repel."])


@template("c17x_test_magnet_table", chapter=17, level=2, lo="17a")
def test_magnet_table(rng):
    rows = [("P", "attracted", "attracted"), ("Q", "attracted", "repelled"), ("R", "no effect", "no effect"), ("S", "repelled", "attracted")]
    rng.shuffle(rows)
    magnets = sorted(n for n, a, b in rows if "repelled" in (a, b))
    ans = " and ".join(magnets)
    opts = ["P only", "Q and S", "P and R", "R only"]
    wrongs = {o: "Only repulsion proves a bar is a magnet; attraction can also happen with unmagnetised iron." for o in opts if o != ans}
    table = md_table(["bar", "end 1 near magnet's N pole", "end 2 near magnet's N pole"], [[n, a, b] for n, a, b in rows])
    return mkt(rng, ans, dict(list(wrongs.items())[:3]), f"Four metal bars are tested with the N pole of a known magnet.\n\n{table}\n\nWhich bars are magnets?",
               "repulsion is the only sure test for a magnet", [f"repelled at one end → **{ans}**"],
               ["Which effect proves magnetism?", "Repulsion.", "Find the bars that repel."])


@template("c17x_repel_attract_count", chapter=17, level=2, lo="17a")
def repel_attract_count(rng):
    n = nice(rng, 5, 6, 8)
    k = rng.randrange(1, n)
    return mk(rng, k, [(n - k, "Count the ones that REPEL: only magnets can repel."), (n, "Not all of them repel."), (0, "Some of them did repel.")],
              "bars", f"A student tests **{n}** bars by bringing each end near a known N pole.\n\n{md_table(['result', 'number of bars'], [['repelled at one end', k], ['attracted at both ends', n - k]])}\n\nHow many of the bars are definitely magnets?",
              "only repulsion proves a magnet", [f"repelled: **{k}**"],
              ["Which result proves magnetism?", "Repulsion.", "Count those bars."], dp=0)


@template("c17x_compass_points_round", chapter=17, level=2, lo="17d")
def compass_points_round(rng):
    position = rng.choice(["above", "below"])
    flip = rng.choice([False, True])
    base = "right" if not flip else "left"
    ans = f"to the {base}"
    other = "left" if base == "right" else "right"
    wrongs = {f"to the {other}": "Above and below the magnet, the field runs from the N pole's end towards the S pole's end.", "towards the magnet": "Beside the middle, the field runs parallel to the magnet.", "away from the magnet": "The field is parallel to the magnet here."}
    return mkt(rng, ans, wrongs, f"Fig. 1 shows a plotting compass **{position}** the middle of a bar magnet. In which direction does its N pole point?",
               "outside the magnet, field lines run from N to S", [f"**{ans}**"],
               ["Trace a field line from N round to S.", "Above or below the middle it runs parallel to the magnet.", "Point from N towards S."], figure=figs3.compass_near_magnet(position, flip=flip))


@template("c17x_compass_deflection_wire", chapter=17, level=2, lo="17d")
def compass_deflection_wire(rng):
    d = [2, 4, 6, 8]
    ang = [nice(rng, 60, 70), nice(rng, 35, 40), nice(rng, 20, 25), nice(rng, 12, 15)]
    k = rng.randrange(4)
    return mk(rng, ang[k], [(ang[(k + 1) % 4], "Read the row for this distance."), (d[k], "That is the distance, not the angle."), (ang[0], "Read the correct row.")],
              "°", f"A plotting compass is moved away from a bar magnet. Its needle turns from north by a smaller angle the further it is.\n\n{md_table(['distance from pole / cm', 'deflection of compass / °'], [[x, a] for x, a in zip(d, ang)])}\n\nWhat is the deflection at **{d[k]} cm**?",
              "read the table: the field weakens with distance", [f"at {d[k]} cm: **{ang[k]}°**"],
              ["Find the distance.", "Read across.", "The field is weaker further away."], dp=0)


@template("c17x_percentage_retained", chapter=17, level=2, lo="17c")
def percentage_retained(rng):
    on = nice(rng, 20, 25, 40)
    off = on * nice(rng, 0.6, 0.7, 0.8)
    pct = off / on * 100
    return mk(rng, pct, [(on / off * 100, "Divide pins kept by pins at first."), (100 - pct, "That is the percentage LOST."), (off, "Give a percentage.")],
              "%", f"A steel bar is magnetised and tested.\n\n{md_table(['test', 'pins held'], [['while touching the magnet', on], ['an hour after removal', fmt(off)]])}\n\nWhat percentage of its magnetism (measured by pins) does it keep?",
              "% kept = after ÷ before × 100%", [f"= {fmt(off)} ÷ {on} × 100% = **{fmt(pct)}%**"],
              ["Compare the two readings.", "Divide.", "× 100%."])


@template("c17x_temporary_choice", chapter=17, level=2, lo="17c")
def temporary_choice(rng):
    rows = [("W", 25, 1), ("X", 20, 12), ("Y", 18, 15), ("Z", 5, 0)]
    rng.shuffle(rows)
    ans = "W"
    wrongs = {n: ("This keeps its magnetism: not suitable for an electromagnet core." if b > 5 else "It is only weakly magnetised.") for n, a, b in rows if n != ans}
    table = md_table(["material", "pins while in solenoid", "pins after current switched off"], [[n, a, b] for n, a, b in rows])
    return mkt(rng, ans, wrongs, f"Four materials are tested as the core of an electromagnet for a scrapyard crane.\n\n{table}\n\nWhich is best?",
               "electromagnet core: strongly magnetised, loses magnetism when switched off", ["W: many pins on, almost none off → **W**"],
               ["What must the crane do?", "Pick up AND release.", "Strong but temporary."])


@template("c17x_solenoid_turns", chapter=17, level=2, lo="17b")
def solenoid_turns(rng):
    turns = [50, 100, 150, 200]
    pins = [nice(rng, 5, 6), nice(rng, 11, 12), nice(rng, 16, 17), nice(rng, 22, 23)]
    k = rng.randrange(4)
    return mk(rng, pins[k], [(pins[(k + 1) % 4], "Read the row for this number of turns."), (turns[k], "That is the number of turns."), (pins[k] - 4, "Read the table.")],
              "pins", f"An electromagnet with an iron core is tested with different numbers of turns (same current).\n\n{md_table(['number of turns', 'pins lifted'], [[t, p] for t, p in zip(turns, pins)])}\n\nHow many pins are lifted with **{turns[k]}** turns?",
              "read the table: more turns → stronger electromagnet", [f"{turns[k]} turns: **{pins[k]} pins**"],
              ["Find the row.", "Read across.", "More turns, more pins."], dp=0)


# ================================================================== L3
@template("c17x_iron_vs_steel_diff", chapter=17, level=3, lo="17c")
def iron_vs_steel_diff(rng):
    i_off, s_off = nice(rng, 0, 1, 2), nice(rng, 9, 10, 12)
    return mk(rng, s_off - i_off, [(s_off, "Find how many MORE: subtract."), (i_off, "That is iron's value."), (s_off + i_off, "Subtract.")],
              "pins", f"{md_table(['bar', 'pins held after magnet removed'], [['iron', i_off], ['steel', s_off]])}\n\nHow many more pins does the steel bar keep than the iron bar?",
              "difference of the 'after' readings", [f"{s_off} − {i_off} = **{s_off - i_off} pins**"],
              ["Read both values.", "Subtract.", "Steel keeps its magnetism."], dp=0)


@template("c17x_iron_vs_steel_ratio", chapter=17, level=3, lo="17c")
def iron_vs_steel_ratio(rng):
    i_on, s_on = nice(rng, 24, 30, 36), nice(rng, 12, 15, 18)
    return mk(rng, i_on / s_on, [(s_on / i_on, "Iron holds MORE while touching: iron ÷ steel."), (i_on - s_on, "Find the ratio."), (i_on, "Divide by steel's value.")],
              "times", f"{md_table(['bar', 'pins held while touching magnet'], [['iron', i_on], ['steel', s_on]])}\n\nHow many times more pins does iron hold than steel while touching the magnet?",
              "ratio = iron ÷ steel", [f"= {i_on} ÷ {s_on} = **{fmt(i_on / s_on)}**"],
              ["Iron is easily magnetised.", "Divide.", "Iron ÷ steel."])


@template("c17x_demagnetise_heat", chapter=17, level=3, lo="17b")
def demagnetise_heat(rng):
    temps = [20, 200, 400, 600, 800]
    pins = [20, 18, 12, nice(rng, 5, 6), 0]
    k = rng.randrange(1, 4)
    loss = pins[0] - pins[k]
    return mk(rng, loss, [(pins[k], "That is the number held; find how many FEWER than at 20 °C."), (pins[0], "That is the starting value."), (pins[k - 1] - pins[k], "Compare with the value at 20 °C.")],
              "pins", f"A steel magnet is heated and tested at each temperature.\n\n{md_table(['temperature / °C', 'pins held'], [[t, p] for t, p in zip(temps, pins)])}\n\nHow many fewer pins does it hold at **{temps[k]} °C** than at 20 °C?",
              "heating demagnetises; loss = start − value", [f"{pins[0]} − {pins[k]} = **{loss} pins**"],
              ["Read both values.", "Subtract.", "Heating demagnetises a magnet."], dp=0)


@template("c17x_demagnetise_ac", chapter=17, level=3, lo="17b")
def demagnetise_ac(rng):
    dist = [0, 10, 20, 40]
    pins = [nice(rng, 15, 16), nice(rng, 9, 10), nice(rng, 4, 5), 0]
    ans = 40
    return mk(rng, ans, [(20, "Some magnetism remains at 20 cm."), (0, "That is the starting position."), (10, "Find where no pins are held.")],
              "cm", f"A magnet is placed in a solenoid carrying a.c. and pulled slowly away. Its strength is tested as it is moved out.\n\n{md_table(['distance pulled out / cm', 'pins held afterwards'], [[d, p] for d, p in zip(dist, pins)])}\n\nAfter being pulled out how far is it fully demagnetised?",
              "read where the pins held fall to zero", ["pins = 0 at **40 cm**"],
              ["Find where the pins reach zero.", "a.c. demagnetises as it is withdrawn.", "Read the distance."], dp=0)


@template("c17x_field_strength_pins", chapter=17, level=3, lo="17e")
def field_strength_pins(rng):
    rows = [("at the N pole", nice(rng, 12, 14)), ("at the S pole", nice(rng, 12, 14)), ("at the middle", 0), ("halfway to the middle", nice(rng, 4, 5))]
    rng.shuffle(rows)
    ans = "at the middle"
    wrongs = {n: "The field is strongest at the poles and weakest in the middle." for n, v in rows if n != ans}
    table = md_table(["position on bar magnet", "pins attracted"], [[n, v] for n, v in rows])
    return mkt(rng, ans, wrongs, f"{table}\n\nWhere is the magnetic field of the bar magnet weakest?",
               "fewest pins → weakest field (field strongest at the poles)", ["no pins at the middle → **at the middle**"],
               ["Which position attracts fewest pins?", "That is the weakest field.", "The middle of the magnet."])


@template("c17x_field_lines_count", chapter=17, level=3, lo="17e")
def field_lines_count(rng):
    rows = [("P", nice(rng, 8, 10)), ("Q", nice(rng, 3, 4)), ("R", nice(rng, 1, 2)), ("S", nice(rng, 5, 6))]
    rng.shuffle(rows)
    target = rng.choice(["strongest", "weakest"])
    ans = (max if target == "strongest" else min)(rows, key=lambda r: r[1])[0]
    wrongs = {n: "Closer field lines (more per cm) mean a stronger field." for n, v in rows if n != ans}
    table = md_table(["region of field diagram", "field lines crossing 1 cm"], [[n, v] for n, v in rows])
    return mkt(rng, ans, wrongs, f"{table}\n\nIn which region is the magnetic field **{target}**?",
               "more lines per cm → stronger field", [f"**{ans}**"],
               ["What does line spacing show?", "Close lines = strong field.", f"Pick the {target}."])


@template("c17x_induced_attract_distance", chapter=17, level=3, lo="17a")
def induced_attract_distance(rng):
    d = [1, 2, 3, 4]
    F = [nice(rng, 80, 90), nice(rng, 25, 30), nice(rng, 10, 12), nice(rng, 5, 6)]
    k = rng.randrange(1, 4)
    return mk(rng, F[0] - F[k], [(F[k], "Find the DECREASE from 1 cm."), (F[0], "That is the force at 1 cm."), (F[k - 1] - F[k], "Compare with the value at 1 cm.")],
              "mN", f"The force between two magnets is measured at different separations.\n\n{md_table(['separation / cm', 'force / mN'], [[x, f] for x, f in zip(d, F)])}\n\nBy how much does the force fall when the separation increases from 1 cm to **{d[k]} cm**?",
              "decrease = F(1 cm) − F(d)", [f"{F[0]} − {F[k]} = **{F[0] - F[k]} mN**"],
              ["Read both forces.", "Subtract.", "Magnetic forces weaken quickly with distance."], dp=0)


@template("c17x_attract_or_not", chapter=17, level=3, lo="17a")
def attract_or_not(rng):
    objs = [("steel paper clip", "attracted"), ("copper coin", "no effect"), ("aluminium can", "no effect"), ("nickel coin", "attracted"), ("iron nail", "attracted"), ("plastic ruler", "no effect")]
    sample = rng.sample(objs, 4)
    if not any(r == "no effect" for _, r in sample):
        sample[0] = ("copper coin", "no effect")
    if not any(r == "attracted" for _, r in sample):
        sample[1] = ("iron nail", "attracted")
    n = sum(1 for _, r in sample if r == "attracted")
    return mk(rng, n, [(4 - n, "Count the MAGNETIC materials (iron, steel, nickel, cobalt)."), (4, "Not all materials are magnetic."), (n + 1, "Check each material.")],
              "objects", f"A magnet is brought near four objects.\n\n{md_table(['object'], [[o] for o, _ in sample])}\n\nHow many of them will be attracted?",
              "magnetic materials: iron, steel, nickel, cobalt", [", ".join(f"{o}: {r}" for o, r in sample), f"attracted: **{n}**"],
              ["Which materials are magnetic?", "Iron, steel, nickel, cobalt.", "Count them."], dp=0)


@template("c17x_compass_plot_count", chapter=17, level=3, lo="17d")
def compass_plot_count(rng):
    L = nice(rng, 12, 15, 18)
    step = nice(rng, 1.5, 2.0, 3.0)
    n = round(L / step)
    return mk(rng, n, [(n + 1, "Count the steps (moves), not the dots."), (L, "That is the length of the line."), (step, "Divide the length by the step.")],
              "moves", f"A student plots a field line by moving a plotting compass along it, marking a dot at the needle's tip each time.\n\n{md_table(['quantity', 'value'], [['length of the field line', f'{L} cm'], ['distance moved each step', f'{fmt(step)} cm']])}\n\nHow many moves are needed to plot the whole line?",
              "number of moves = length ÷ step", [f"{L} ÷ {fmt(step)} = **{n}**"],
              ["Each move covers one step.", "Divide.", "Round to a whole number."], dp=0)


@template("c17x_compass_neutral", chapter=17, level=3, lo="17d")
def compass_neutral(rng):
    pts = [("A", "points away from magnet"), ("B", "points towards magnet"), ("X", "points to geographic north (no effect from magnet)"), ("C", "points along the magnet")]
    rng.shuffle(pts)
    ans = "X"
    wrongs = {n: "At a neutral point the magnet's field is cancelled, so only the Earth's field acts on the compass." for n, d in pts if n != ans}
    table = md_table(["compass position", "observation"], [[n, d] for n, d in pts])
    return mkt(rng, ans, wrongs, f"A compass is placed at four points near a bar magnet.\n\n{table}\n\nAt which point is the magnet's field cancelled by the Earth's field (a neutral point)?",
               "neutral point: compass behaves as if the magnet were absent", ["**X**"],
               ["What happens to a compass at a neutral point?", "The magnet has no net effect.", "It points as if no magnet were there."])


# ================================================================== L4
@template("c17x_two_magnets_force_table", chapter=17, level=4, lo="17a")
def two_magnets_force_table(rng):
    d = [1, 2, 4]
    F1 = nice(rng, 64, 80, 96)
    F = [F1, F1 / 4, F1 / 16]
    return mk(rng, F[0] / F[2], [(F[0] / F[1], "Compare 1 cm with 4 cm."), (4, "The force falls much faster than 1/d."), (F[0] - F[2], "Find the ratio.")],
              "times", f"{md_table(['separation / cm', 'force between magnets / mN'], [[x, fmt(f)] for x, f in zip(d, F)])}\n\nHow many times stronger is the force at 1 cm than at 4 cm?",
              "ratio = F(1 cm) ÷ F(4 cm)", [f"{fmt(F[0])} ÷ {fmt(F[2])} = **{fmt(F[0] / F[2])}**"],
              ["Read both forces.", "Divide.", "The force falls rapidly with distance."])


@template("c17x_magnet_or_iron_test", chapter=17, level=4, lo="17a")
def magnet_or_iron_test(rng):
    results = {"repels end A, attracts end B": "magnet", "attracts both ends": "unmagnetised iron (or steel)", "no effect at either end": "non-magnetic material"}
    obs = rng.choice(list(results))
    ans = results[obs]
    wrongs = {v: "Use: repulsion → magnet; attraction only → magnetic but unmagnetised; nothing → non-magnetic." for k, v in results.items() if v != ans}
    wrongs["a charged insulator"] = "This is a magnetic test, not an electric one."
    return mkt(rng, ans, dict(list(wrongs.items())[:3]), f"A bar is tested with the N pole of a known magnet.\n\n{md_table(['test', 'result'], [['N pole near each end in turn', obs]])}\n\nWhat is the bar?",
               "repulsion → magnet; attraction only → magnetic material; no effect → non-magnetic", [f"**{ans}**"],
               ["Is there any repulsion?", "Repulsion means a magnet.", "Attraction alone is not proof."])


@template("c17x_current_electromagnet", chapter=17, level=4, lo="17b")
def current_electromagnet(rng):
    I = [0.5, 1.0, 1.5, 2.0]
    pins = [nice(rng, 4, 5), nice(rng, 9, 10), nice(rng, 13, 15), nice(rng, 18, 20)]
    return mk(rng, pins[3] - pins[1], [(pins[3], "Find the INCREASE."), (pins[1], "That is the value at 1.0 A."), (pins[3] - pins[0], "Compare 1.0 A with 2.0 A.")],
              "pins", f"The current in an electromagnet is increased.\n\n{md_table(['current / A', 'pins lifted'], [[fmt(i), p] for i, p in zip(I, pins)])}\n\nHow many more pins are lifted at 2.0 A than at 1.0 A?",
              "increase = pins(2.0 A) − pins(1.0 A)", [f"{pins[3]} − {pins[1]} = **{pins[3] - pins[1]} pins**"],
              ["Read both values.", "Subtract.", "More current → stronger electromagnet."], dp=0)


@template("c17x_magnetising_coil_steps", chapter=17, level=4, lo="17b")
def magnetising_coil_steps(rng):
    before = 0
    after = nice(rng, 12, 15, 18)
    weeks = nice(rng, 2, 4)
    later = after - nice(rng, 1, 2)
    return mk(rng, (after - later) / after * 100, [(after - later, "Express the loss as a percentage of the value just after magnetising."), (later / after * 100, "That is the percentage KEPT."), ((after - later) / later * 100, "Divide by the value just after magnetising.")],
              "%", f"A steel bar is magnetised in a solenoid with d.c. and tested.\n\n{md_table(['time', 'pins held'], [['before', before], ['just after magnetising', after], [f'after {weeks} weeks', later]])}\n\nWhat percentage of its strength has it lost after {weeks} weeks?",
              "% lost = (after − later) ÷ after × 100%", [f"loss = {after} − {later} = {after - later} pins", f"% = **{fmt((after - later) / after * 100)}%**"],
              ["Find the loss.", "Divide by the value just after magnetising.", "× 100%."])


@template("c17x_core_material_compare", chapter=17, level=4, lo="17c")
def core_material_compare(rng):
    rows = [("soft iron", nice(rng, 30, 35), nice(rng, 0, 1)), ("steel", nice(rng, 20, 22), nice(rng, 12, 14)), ("no core", nice(rng, 4, 5), 0)]
    which = rng.choice(["electromagnet in a relay", "permanent magnet in a door catch"])
    ans = "soft iron" if "relay" in which else "steel"
    wrongs = {n: ("It keeps its magnetism, so the relay would not release." if n == "steel" else ("It does not keep magnetism, so it cannot be a permanent magnet." if n == "soft iron" else "Without a core the magnetism is weak.")) for n, a, b in rows if n != ans}
    wrongs["copper"] = "Copper is not magnetic."
    table = md_table(["core", "pins while current on", "pins after current off"], [[n, a, b] for n, a, b in rows])
    return mkt(rng, ans, dict(list(wrongs.items())[:3]), f"{table}\n\nWhich material should be used for a **{which}**?",
               "temporary (electromagnet): soft iron; permanent: steel", [f"**{ans}**"],
               ["Must it keep its magnetism?", "Relay: no. Door catch: yes.", "Soft iron vs steel."])


@template("c17x_core_strength_factor", chapter=17, level=4, lo="17c")
def core_strength_factor(rng):
    no_core = nice(rng, 3, 4, 5)
    iron = no_core * nice(rng, 6, 8, 10)
    return mk(rng, iron / no_core, [(no_core / iron, "The iron core makes it STRONGER: iron ÷ no core."), (iron - no_core, "Find the ratio."), (iron, "Divide by the no-core value.")],
              "times", f"A solenoid is tested with and without a soft-iron core (same current).\n\n{md_table(['core', 'pins lifted'], [['none', no_core], ['soft iron', iron]])}\n\nHow many times stronger is it with the iron core?",
              "factor = iron ÷ no core", [f"{iron} ÷ {no_core} = **{fmt(iron / no_core)}**"],
              ["Compare the two readings.", "Divide.", "Iron concentrates the field."])


@template("c17x_compass_deflect_angle_change", chapter=17, level=4, lo="17d")
def compass_deflect_angle_change(rng):
    a1 = nice(rng, 0, 5)
    a2 = nice(rng, 40, 55, 70)
    return mk(rng, a2 - a1, [(a2, "Find the CHANGE in direction."), (a1, "That is the starting direction."), (a2 + a1, "Subtract.")],
              "°", f"A plotting compass first points north. A magnet is brought near and the needle turns.\n\n{md_table(['', 'needle direction (degrees east of north)'], [['before', a1], ['with magnet near', a2]])}\n\nThrough what angle does the needle turn?",
              "angle turned = final − initial", [f"{a2} − {a1} = **{a2 - a1}°**"],
              ["Read both directions.", "Subtract.", "The magnet's field turns the needle."], dp=0)


@template("c17x_compass_earth_vs_magnet", chapter=17, level=4, lo="17d")
def compass_earth_vs_magnet(rng):
    d = [5, 10, 20, 40, 80]
    ang = [85, 60, 25, 6, 1]
    limit = 5
    ans = next(x for x, a in zip(d, ang) if a <= limit + 1)
    return mk(rng, ans, [(20, "The magnet still turns the needle a lot at 20 cm."), (80, "The needle is already nearly unaffected before 80 cm."), (10, "Find where the deflection becomes small.")],
              "cm", f"A compass is moved away from a magnet along an east–west line.\n\n{md_table(['distance / cm', 'deflection from north / °'], [[x, a] for x, a in zip(d, ang)])}\n\nAt about what distance does the magnet's field become small compared with the Earth's (deflection about 6° or less)?",
              "read where the deflection falls to a few degrees", [f"deflection ≈ 6° at **{ans} cm**"],
              ["Look for a small deflection.", "Near zero means the Earth's field dominates.", "Read the distance."], dp=0)


# ================================================================== L5
@template("c17x_solenoid_end_pole", chapter=17, level=5, lo="17b")
def solenoid_end_pole(rng):
    view = rng.choice(["clockwise", "anticlockwise"])
    ans = "S" if view == "clockwise" else "N"
    wrongs = {("N" if ans == "S" else "S"): "Clockwise current (seen from the end) gives a S pole; anticlockwise gives N.", "no pole": "A current-carrying solenoid has poles at its ends.", "it depends on the core only": "The current direction decides the poles."}
    return mkt(rng, ans, wrongs, f"Looking at one end of a solenoid, the current flows **{view}**.\n\n{md_table(['view of end', 'current direction'], [['end facing you', view]])}\n\nWhat pole is at this end?",
               "end rule: clockwise → S, anticlockwise → N", [f"{view} → **{ans}**"],
               ["Use the end rule.", "Draw S or N with arrows.", "Clockwise S, anticlockwise N."])


@template("c17x_domains_aligned", chapter=17, level=5, lo="17b")
def domains_aligned(rng):
    total = nice(rng, 200, 400, 500)
    frac = nice(rng, 0.25, 0.5, 0.8)
    aligned = total * frac
    return mk(rng, frac * 100, [((1 - frac) * 100, "That is the percentage NOT aligned."), (aligned, "Give a percentage."), (total / aligned * 100, "Divide aligned by total.")],
              "%", f"In a model of a magnetised steel bar, small regions (domains) are counted.\n\n{md_table(['domains', 'number'], [['total', total], ['aligned in the same direction', fmt(aligned)]])}\n\nWhat percentage of the domains are aligned?",
              "% aligned = aligned ÷ total × 100%", [f"= {fmt(aligned)} ÷ {total} × 100% = **{fmt(frac * 100)}%**"],
              ["More aligned domains → stronger magnet.", "Divide.", "× 100%."])


@template("c17x_strength_compare_materials", chapter=17, level=5, lo="17c")
def strength_compare_materials(rng):
    i_on, i_off = nice(rng, 30, 32), nice(rng, 1, 2)
    s_on, s_off = nice(rng, 18, 20), nice(rng, 12, 14)
    ri, rs = i_off / i_on * 100, s_off / s_on * 100
    return mk(rng, rs - ri, [(rs, "That is steel's retention; find the difference."), (ri, "That is iron's retention."), (rs + ri, "Subtract.")],
              "percentage points", f"{md_table(['bar', 'pins while touching magnet', 'pins after removal'], [['iron', i_on, i_off], ['steel', s_on, s_off]])}\n\nHow many percentage points more of its magnetism does steel retain than iron?",
              "retention % = after ÷ before × 100; subtract", [f"iron: {fmt(ri)}%; steel: {fmt(rs)}%", f"difference = **{fmt(rs - ri)}**"],
              ["Find each percentage kept.", "Subtract.", "Steel retains far more."])


@template("c17x_permanent_choice_data", chapter=17, level=5, lo="17c")
def permanent_choice_data(rng):
    rows = [("A", 30, 2, "cheap"), ("B", 18, 15, "moderate"), ("C", 25, 20, "expensive"), ("D", 10, 9, "cheap")]
    rng.shuffle(rows)
    ans = "C"
    wrongs = {n: ("It loses most of its magnetism." if b < 5 else "It keeps its magnetism but is weaker.") for n, a, b, c in rows if n != ans}
    table = md_table(["material", "pins while magnetised", "pins a week later", "cost"], [[n, a, b, c] for n, a, b, c in rows])
    return mkt(rng, ans, wrongs, f"A loudspeaker needs the STRONGEST possible permanent magnet; cost is not important.\n\n{table}\n\nWhich material should be chosen?",
               "permanent and strong: most pins a week later", ["C keeps the most pins (20) → **C**"],
               ["What matters: strength after a week.", "Ignore cost here.", "Most pins a week later."])


@template("c17x_field_neutral_position", chapter=17, level=5, lo="17e")
def field_neutral_position(rng):
    gap = nice(rng, 8, 10, 12)
    equal = rng.choice([True, False])
    if equal:
        x = gap / 2
        ans_note = "midway"
    else:
        x = gap / 3
        ans_note = "closer to the weaker magnet"
    return mk(rng, x, [(gap - x, "Measure from the magnet named in the question."), (gap, "That is the whole gap."), (gap / 4, "The neutral point is where the fields balance.")],
              "cm", f"Two magnets are placed with like (N) poles facing, **{gap} cm** apart. {'They are identical.' if equal else 'Magnet A is weaker than magnet B, and the neutral point is one third of the way from A.'}\n\n{md_table(['quantity', 'value'], [['gap between poles', f'{gap} cm'], ['magnets', 'identical' if equal else 'A weaker than B']])}\n\nHow far from magnet A's pole is the neutral point?",
              "neutral point: fields cancel (midway for identical magnets)", [f"{ans_note}: **{fmt(x)} cm** from A"],
              ["Where do the fields cancel?", "Equal magnets: midway.", "Weaker magnet: closer to it."])


@template("c17x_field_strength_ratio", chapter=17, level=5, lo="17e")
def field_strength_ratio(rng):
    n1, n2 = nice(rng, 12, 16), nice(rng, 3, 4)
    return mk(rng, n1 / n2, [(n2 / n1, "More lines per cm → stronger: pole ÷ middle region."), (n1 - n2, "Find the ratio."), (n1, "Divide.")],
              "times", f"On a field diagram, the number of lines crossing 1 cm is counted.\n\n{md_table(['region', 'lines per cm'], [['near the pole', n1], ['further away', n2]])}\n\nHow many times stronger is the field near the pole (taking field strength ∝ lines per cm)?",
              "ratio = lines per cm near pole ÷ further away", [f"{n1} ÷ {n2} = **{fmt(n1 / n2)}**"],
              ["Line density shows field strength.", "Divide.", "Near the pole ÷ further."])


@template("c17x_compass_two_magnets_effect", chapter=17, level=5, lo="17d")
def compass_two_magnets_effect(rng):
    facing = rng.choice(["NS", "NN"])
    ans = "it points from the N pole towards the S pole, along the line joining them" if facing == "NS" else "it points in no fixed direction from the magnets (neutral point): only the Earth's field acts"
    allo = ["it points from the N pole towards the S pole, along the line joining them", "it points in no fixed direction from the magnets (neutral point): only the Earth's field acts", "it points towards the N pole", "it points at right angles to the magnets"]
    wrongs = {o: "Think about the field between the two poles." for o in allo if o != ans}
    return mkt(rng, ans, wrongs, f"Fig. 1 shows two bar magnets with {'unlike (N and S)' if facing == 'NS' else 'like (N and N)'} poles facing. A compass is placed midway between them. What does the compass do?",
               "unlike poles: strong field from N to S between them; like poles: neutral point midway", [f"**{ans}**"],
               ["Unlike or like poles?", "Unlike: field lines go straight across.", "Like: fields cancel midway."], figure=figs3.two_magnets(facing))


@template("c17x_earth_field_compass_angle", chapter=17, level=5, lo="17d")
def earth_field_compass_angle(rng):
    name = rng.choice(["east", "south", "west"])
    ans = "north"
    wrongs = {name: "The needle does not turn with you; it lines up with the Earth's field.", ("south" if name != "south" else "east"): "The compass N pole is attracted towards the Earth's magnetic pole in the north.",
              "it spins continuously": "It settles along the Earth's field."}
    return mkt(rng, ans, dict(list(wrongs.items())[:3]), f"A hiker walks due {name} holding a compass far from any magnets.\n\n{md_table(['quantity', 'value'], [['direction of walking', name]])}\n\nIn which direction does the compass needle's N pole point?",
               "the compass aligns with the Earth's field: N pole points (magnetic) north", ["the needle points **north** whichever way the hiker walks"],
               ["What field does the compass follow?", "The Earth's.", "It always points north."])


@template("c17x_compass_reverse_flip", chapter=17, level=5, lo="17d")
def compass_reverse_flip(rng):
    position = rng.choice(["right", "left", "above", "below"])
    base = {"left": "left", "right": "left", "above": "right", "below": "right"}[position]
    ans = "it reverses, pointing " + ("right" if base == "left" else "left")
    wrongs = {"it stays the same": "Turning the magnet round reverses its field at the compass.", "it points north": "Near the magnet, its field is much stronger than the Earth's.",
              "it turns through 90°": "The field reverses direction, a turn of 180°."}
    return mkt(rng, ans, wrongs, f"Fig. 1 shows a compass {position} {'of ' if position in ('left', 'right') else ''}a bar magnet. The magnet is turned round so its poles swap ends. What happens to the compass needle?",
               "reversing the magnet reverses the field direction at every point", [f"originally points {base}; after swapping → **{ans}**"],
               ["Which way does it point now?", "What does swapping the poles do to the field?", "It reverses."], figure=figs3.compass_near_magnet(position))
