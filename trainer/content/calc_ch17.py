"""Chapter 17 Magnetism (6091): data-reading templates (descriptive chapter): pole tables, magnetic materials, compass
directions, induced poles, iron vs steel data, strength-distance data, solenoid poles."""
from .. import figs, figs3
from .base import fmt, md_table, nice, numeric_options, template, text_options


# ---------------------------------------------------------------- L1
@template("c17_which_pair_attracts", chapter=17, level=1, lo="17a")
def which_pair_attracts(rng):
    norths = set(rng.sample("PQRS", 2))
    ends = [(n, "N" if n in norths else "S") for n in "PQRS"]
    pole = dict(ends)
    pairs = [("P", "Q"), ("P", "R"), ("Q", "S"), ("R", "S"), ("P", "S"), ("Q", "R")]
    rng.shuffle(pairs)
    attract = [f"{a} and {b}" for a, b in pairs if pole[a] != pole[b]]
    repel = [f"{a} and {b}" for a, b in pairs if pole[a] == pole[b]]
    ans = attract[0]
    wrongs = {p: f"{p.split(' and ')[0]} and {p.split(' and ')[1]} are both {pole[p.split(' and ')[0]]} poles: like poles repel." for p in repel[:2]}
    wrongs["none of the pairs"] = "Unlike poles (one N, one S) always attract, and the table contains both N and S ends."
    opts, key, mis = text_options(rng, ans, wrongs)
    table = md_table(["end of magnet", "pole"], [[n, p] for n, p in sorted(ends)])
    return dict(
        stem=f"The table shows the poles at four ends of two bar magnets.\n\n{table}\n\nWhich two ends **attract** each other when brought close?",
        options=opts, key=key, misconceptions=mis,
        formula="like poles repel; unlike poles attract",
        working=[f"{ans.split(' and ')[0]} is {pole[ans.split(' and ')[0]]} and {ans.split(' and ')[1]} is {pole[ans.split(' and ')[1]]}", "unlike poles attract", f"**{ans}**"],
        hints=["State the rule for poles.", "Attraction needs one N and one S.", "Find the pair with different poles."],
    )


@template("c17_magnetic_material_table", chapter=17, level=1, lo="17a")
def magnetic_material_table(rng):
    mats = [("iron", True), ("steel", True), ("nickel", True), ("cobalt", True), ("copper", False), ("aluminium", False), ("brass", False), ("plastic", False), ("wood", False)]
    mag = rng.choice([m for m in mats if m[1]])
    non = rng.sample([m for m in mats if not m[1]], 3)
    rows = [mag] + non
    rng.shuffle(rows)
    letters = dict(zip("WXYZ", rows))
    ans = next(k for k, v in letters.items() if v[1])
    wrongs = {k: f"Sample {k} is {v[0]}, which is not a magnetic material, so it is not attracted." for k, v in letters.items() if not v[1]}
    opts, key, mis = text_options(rng, ans, wrongs)
    table = md_table(["sample", "material"], [[k, v[0]] for k, v in letters.items()])
    return dict(
        stem=f"A magnet is brought close to four samples.\n\n{table}\n\nWhich sample is attracted to the magnet?",
        options=opts, key=key, misconceptions=mis,
        formula="magnetic materials: iron, steel, nickel, cobalt (and their alloys); other metals and non-metals are not attracted",
        working=[f"{mag[0]} is a magnetic material; the others are not", f"sample **{ans}** is attracted"],
        hints=["Only a few materials are magnetic.", "Iron, steel, nickel and cobalt. Copper, aluminium and brass are metals but NOT magnetic.", "Which sample is one of the four magnetic materials?"],
    )


# ---------------------------------------------------------------- L2
@template("c17_compass_direction", chapter=17, level=2, lo="17d")
def compass_direction(rng):
    position = rng.choice(["right", "left", "above", "below"])
    flip = rng.choice([False, True])
    # N on the left (flip False): field leaves N heading left, loops over top heading right, enters S heading left
    base = {"left": "left", "right": "left", "above": "right", "below": "right"}[position]
    if flip:
        base = "right" if base == "left" else "left"
    ans = f"to the {base}"
    other = "right" if base == "left" else "left"
    wrongs = {f"to the {other}": "The compass needle lines up with the field line at that point, pointing the way a free N pole would move: from the magnet's N pole round to its S pole.",
              "upwards (towards the top of the page)": "The field near the ends and along the sides of a bar magnet runs mainly left-right in this view.",
              "in no particular direction": "A compass always lines up with the local field; near a bar magnet that field is much stronger than the Earth's."}
    opts, key, mis = text_options(rng, ans, wrongs)
    return dict(
        stem=f"Fig. 1 shows a bar magnet with a plotting compass placed {position} {'of' if position in ('left', 'right') else ''} it. (The needle shown is unmarked.) In which direction does the N pole of the compass needle point?".replace("  ", " "),
        figure=figs3.compass_near_magnet(position, flip=flip),
        options=opts, key=key, misconceptions=mis,
        formula="a compass N pole points along the field: away from the magnet's N pole and towards its S pole",
        working=["field lines run from the N pole, round the outside, to the S pole", f"at the {position} the field points **{ans}**"],
        hints=["Which way do field lines go outside a bar magnet?", "The compass N pole points along the field line at its position.", f"Trace the line from N round to S past the compass."],
    )


@template("c17_induced_pole", chapter=17, level=2, lo="17b")
def induced_pole(rng):
    material = rng.choice(["iron", "steel", "nickel"])
    ans = "the near end becomes a S pole and the far end a N pole"
    wrongs = {"the near end becomes a N pole and the far end a S pole": "The bar is attracted, so the end nearest the magnet's N pole must be the OPPOSITE pole: S.",
              "the whole bar becomes a N pole": "A magnet always has two poles; induced magnetism gives the bar an S end and an N end.",
              "the bar is not affected because it is not a magnet": f"{material.capitalize()} is a magnetic material: it becomes an induced magnet in the field."}
    opts, key, mis = text_options(rng, ans, wrongs)
    return dict(
        stem=f"Fig. 1 shows an unmagnetised {material} bar placed close to the N pole of a bar magnet. What happens to the {material} bar?",
        figure=figs3.induced_magnetism(material),
        options=opts, key=key, misconceptions=mis,
        formula="induced magnetism: the end of the magnetic material nearest the magnet becomes the opposite pole (so it is attracted)",
        working=[f"the {material} becomes an induced magnet", "the end near the N pole becomes S (unlike poles attract), the far end becomes N", f"**{ans}**"],
        hints=["Is the bar attracted or repelled by the magnet?", "It is attracted, so the near end must be the opposite pole to N.", "Induced magnet: S near, N far."],
    )


# ---------------------------------------------------------------- L3
@template("c17_iron_vs_steel_data", chapter=17, level=3, lo="17c")
def iron_vs_steel_data(rng):
    a_pins_in = nice(rng, 18, 20, 24)
    b_pins_in = a_pins_in - rng.choice([2, 4])
    a_after, b_after = rng.choice([0, 1]), rng.choice([8, 10, 12])
    rows = [("A", a_pins_in, a_after), ("B", b_pins_in, b_after)]
    ans = "B is steel, because it keeps most of its magnetism when the magnet is removed"
    wrongs = {"A is steel, because it picks up more pins while the magnet is present": "Picking up more pins while in the field shows A magnetises more EASILY (iron). Steel is identified by what it KEEPS afterwards.",
              "A is steel, because it loses its magnetism quickly": "Losing magnetism quickly is the behaviour of a temporary magnet, which is IRON.",
              "Both are iron, because both pick up pins": "Both magnetise in the field, but only B stays magnetised: that is steel."}
    opts, key, mis = text_options(rng, ans, wrongs)
    table = md_table(["bar", "pins held while touching the magnet", "pins held after the magnet is removed"], [list(r) for r in rows])
    return dict(
        stem=f"Two identical-looking bars, A and B, are each touched to a strong magnet and dipped into pins, then the magnet is removed. One bar is iron and one is steel.\n\n{table}\n\nWhich bar is steel, and why?",
        options=opts, key=key, misconceptions=mis,
        formula="iron: magnetises easily and loses its magnetism easily (temporary); steel: harder to magnetise but keeps its magnetism (permanent)",
        working=[f"A: {a_pins_in} pins with the magnet, {a_after} after: loses its magnetism (iron)", f"B: {b_pins_in} with the magnet, {b_after} after: keeps its magnetism (steel)", f"**{ans}**"],
        hints=["Compare what each bar does AFTER the magnet is taken away.", "Iron loses its induced magnetism; steel keeps it.", "Which bar still holds pins?"],
    )


@template("c17_pins_distance_table", chapter=17, level=3, lo="17e")
def pins_distance_table(rng):
    counts = [nice(rng, 20, 24, 30), 0, 0, 0]
    counts[1] = counts[0] // 2
    counts[2] = counts[1] // 2
    counts[3] = max(1, counts[2] // 2)
    d = [0, 1, 2, 3]
    i = rng.choice([1, 2])
    diff = counts[0] - counts[i]
    opts, key, mis = numeric_options(rng, diff, [
        (counts[i], f"That is the number held at {d[i]} cm, not how many FEWER than at 0 cm."),
        (counts[0], "That is the number held at 0 cm. Subtract the number held at the other distance."),
        (counts[0] + counts[i], "You added. Find the difference."),
    ], unit="pins")
    table = md_table(["distance of card from magnet / cm", "pins held through the card"], [[dd, c] for dd, c in zip(d, counts)])
    return dict(
        stem=f"A student measures the strength of a magnet by counting how many pins it can hold through a stack of cards of different thickness.\n\n{table}\n\nHow many fewer pins are held at **{d[i]} cm** than at 0 cm?",
        options=opts, key=key, misconceptions=mis,
        formula="the magnetic field gets weaker with distance from the pole (field lines spread out); read the table and subtract",
        working=[f"at 0 cm: {counts[0]} pins; at {d[i]} cm: {counts[i]} pins", f"difference = {counts[0]} − {counts[i]} = **{diff}**"],
        hints=["The field is strongest at the pole and weaker further away.", f"Read the counts at 0 cm and at {d[i]} cm.", "Subtract."],
    )


# ---------------------------------------------------------------- L4
@template("c17_force_distance_graph", chapter=17, level=4, lo="17e")
def force_distance_graph(rng):
    F0 = nice(rng, 8, 10, 12)
    pts = [(0, F0), (1, F0 * 0.5), (2, F0 * 0.25), (3, F0 * 0.125), (4, F0 * 0.0625)]
    ask = rng.choice([1, 2])
    ans = dict(pts)[ask]
    opts, key, mis = numeric_options(rng, ans, [
        (F0, "That is the force at 0 cm. Read the curve at the asked distance."),
        (dict(pts)[ask + 1], "You read the graph 1 cm too far along."),
        (F0 - ask * F0 / 4, "The force does not fall in a straight line; read the actual curve, which halves for every centimetre here."),
    ], unit="N", sf=3)
    return dict(
        stem=f"Fig. 1 shows how the force between a magnet and a small iron plate changes with the distance between them. What is the force when the distance is **{ask} cm**?",
        figure=figs.graph(pts, 4, F0 * 1.2 // 1 + 1, 1, 2, xlabel="distance / cm", ylabel="force / N"),
        options=opts, key=key, misconceptions=mis,
        formula="read the graph: the force falls rapidly as the distance grows because the field lines spread out",
        working=[f"at {ask} cm the curve gives **{fmt(ans, sf=3)} N**", f"(the force halves for each extra centimetre: {F0} → {F0 / 2:g} → {F0 / 4:g} N)"],
        hints=["Find the distance on the horizontal axis and go up to the curve.", "Read across to the force axis.", "The force is much smaller than at 0 cm."],
    )


@template("c17_field_between_poles", chapter=17, level=4, lo="17e")
def field_between_poles(rng):
    facing = rng.choice(["NS", "NN", "SS"])
    if facing == "NS":
        ans = "a strong, almost uniform field running from the N pole to the S pole"
        wrongs = {"a point where the field is zero": "A neutral point forms between LIKE poles. Between unlike poles the fields reinforce.",
                  "field lines curving away from the gap": "Between N and S the lines run straight across the gap.",
                  "no field, because the magnets cancel": "Unlike poles facing produce the strongest field of all in the gap."}
    else:
        ans = "a neutral point X where the two fields cancel and the resultant field is zero"
        wrongs = {"a strong uniform field across the gap": "That is the pattern between UNLIKE poles. Like poles push their fields apart.",
                  "field lines running straight from one pole to the other": "Field lines never join like poles; they curve away from each other.",
                  "a field twice as strong as one magnet alone": "The fields point in opposite directions at X and cancel."}
    opts, key, mis = text_options(rng, ans, wrongs)
    return dict(
        stem=f"Fig. 1 shows two bar magnets with {'unlike' if facing == 'NS' else 'like'} poles facing each other. What is found at the point X midway between the poles?",
        figure=figs3.two_magnets(facing),
        options=opts, key=key, misconceptions=mis,
        formula="unlike poles facing: lines run across the gap (strong field); like poles facing: lines repel, neutral point between them",
        working=[f"the facing poles are {facing[0]} and {facing[1]}", f"**{ans}**"],
        hints=["Which poles face each other?", "Unlike: lines cross the gap. Like: lines bend away and there is a neutral point.", "Describe X accordingly."],
    )


# ---------------------------------------------------------------- L5
@template("c17_solenoid_pole", chapter=17, level=5, lo="17b")
def solenoid_pole(rng):
    l2r = rng.choice([True, False])
    # with the coil wound as drawn (front of each turn goes downward when current enters at the top-left), current left-to-right makes Q the N pole
    ans = "Q" if l2r else "P"
    other = "P" if l2r else "Q"
    wrongs = {other: "Use the right-hand grip rule: fingers curl with the current round the coil, thumb points to the N pole. Reversing the current reverses the poles.",
              "neither end: a solenoid has no poles": "A current-carrying solenoid has a field like a bar magnet's, with an N end and an S end.",
              "both ends are N poles": "Any magnet has one N pole and one S pole."}
    opts, key, mis = text_options(rng, ans, wrongs)
    return dict(
        stem=f"Fig. 1 shows a solenoid carrying a steady current in the direction marked, with a steel rod placed inside it. Using the right-hand grip rule, which end of the solenoid, P or Q, is its N pole (so the rod's N pole is induced at that end)?",
        figure=figs3.solenoid(current_left_to_right=l2r),
        options=opts, key=key, misconceptions=mis,
        formula="right-hand grip rule for a solenoid: curl the fingers in the direction of the conventional current round the coil; the thumb points to the N pole",
        working=["grip the coil with the right hand, fingers following the current", f"the thumb points towards **{ans}**, the N pole; the steel inside is magnetised the same way"],
        hints=["Which rule gives the poles of a solenoid?", "Fingers follow the current around the turns; the thumb gives N.", "Reversing the current swaps the poles."],
    )
