"""Chapter 18 Electromagnetism (6091): rule-based and data-reading templates: Fleming's left-hand rule, the field round a wire,
reversing current or field, electromagnet strength data, force proportional to current, commutator reversals, motor factors,
electron-beam deflection."""
from .. import figs3
from .base import fmt, md_table, nice, numeric_options, template, text_options

DIRS = ["upwards", "downwards", "to the left", "to the right"]


def _flip(d):
    return {"upwards": "downwards", "downwards": "upwards", "to the left": "to the right", "to the right": "to the left"}[d]


# ---------------------------------------------------------------- L1
@template("c18_lhr_direction", chapter=18, level=1, lo="18d")
def lhr_direction(rng):
    field = rng.choice(["right", "left"])
    current = rng.choice(["into", "out"])
    f = figs3.lhr_force(field, current)
    ans = "upwards" if f == "up" else "downwards"
    wrongs = {_flip(ans): "You have the force reversed. With Fleming's LEFT hand: First finger = Field (N to S), seCond finger = Current, thuMb = Motion (force).",
              f"to the {field}": "That is the direction of the magnetic field (N to S). The force is at right angles to both the field and the current.",
              "there is no force": "A current-carrying wire at right angles to a magnetic field always experiences a force."}
    opts, key, mis = text_options(rng, ans, wrongs)
    return dict(
        stem=f"Fig. 1 shows a wire carrying a current **{current} the page** between the poles of a magnet. In which direction is the force on the wire?",
        figure=figs3.flemings_lhr(field=field, current=current),
        options=opts, key=key, misconceptions=mis,
        formula="Fleming's left-hand rule: First finger = Field (N → S), seCond finger = Current (conventional), thuMb = Motion / force",
        working=[f"field: from N to S, i.e. to the {field}", f"current: {current} the page", f"thumb (force) points **{ans}**"],
        hints=["Which hand and which rule give the direction of the force on a current in a magnetic field?",
               "Point your first finger along the field (N to S) and your second finger along the current.",
               "Your thumb now gives the direction of the force."],
    )


@template("c18_wire_field_direction", chapter=18, level=1, lo="18a")
def wire_field_direction(rng):
    current = rng.choice(["out", "into"])
    ans = "anticlockwise" if current == "out" else "clockwise"
    other = "clockwise" if ans == "anticlockwise" else "anticlockwise"
    wrongs = {other: "Use the right-hand grip rule: thumb along the current, fingers curl in the direction of the field. Reversing the current reverses the field.",
              "radially outwards from the wire": "The field lines round a straight wire are CIRCLES centred on the wire, not straight lines out from it.",
              "parallel to the wire": "The field lines go round the wire, in planes at right angles to it."}
    opts, key, mis = text_options(rng, ans, wrongs)
    return dict(
        stem=f"Fig. 1 shows a straight wire seen end-on, with the current flowing **{current} of** the page. As seen in the figure, in which direction do the magnetic field lines go round the wire?".replace("into of", "into"),
        figure=figs3.wire_field(current),
        options=opts, key=key, misconceptions=mis,
        formula="right-hand grip rule: thumb along the conventional current, curled fingers give the direction of the field",
        working=[f"current {current} of the page: point the right thumb {'towards you' if current == 'out' else 'away from you'}".replace("into of", "into"), f"the fingers curl **{ans}**"],
        hints=["Which rule gives the direction of the field round a current-carrying wire?",
               "Right-hand grip: thumb along the current.",
               f"With the thumb pointing {'out of' if current == 'out' else 'into'} the page, which way do your fingers curl?"],
    )


# ---------------------------------------------------------------- L2
@template("c18_reverse_current_or_field", chapter=18, level=2, lo="18c")
def reverse_current_or_field(rng):
    start = rng.choice(DIRS)
    change = rng.choice(["the current only", "the magnetic field only", "both the current and the magnetic field"])
    ans = start if change.startswith("both") else _flip(start)
    other_axis = [d for d in DIRS if d not in (start, _flip(start))]
    wrongs = {(_flip(ans)): ("Reversing BOTH the current and the field reverses the force twice, so it is back where it started." if change.startswith("both")
                             else f"Reversing only one of them ({change}) reverses the force."),
              other_axis[0]: "The force stays at right angles to the field and the current; reversing one of them can only reverse it, not turn it through 90°.",
              "the force becomes zero": "The current and field are still at right angles, so there is still a force of the same size."}
    opts, key, mis = text_options(rng, ans, wrongs)
    table = md_table(["", "current", "field", "force on the wire"], [["experiment 1", "original", "original", start], ["experiment 2", "reversed" if "current" in change else "original", "reversed" if "field" in change else "original", "?"]])
    return dict(
        stem=f"A wire carrying a current in a magnetic field experiences a force. In experiment 2 the student reverses **{change}**.\n\n{table}\n\nIn which direction is the force in experiment 2?",
        options=opts, key=key, misconceptions=mis,
        formula="reversing the current OR the field reverses the force; reversing both leaves it unchanged",
        working=[f"changed: {change}", "each reversal reverses the force", f"force in experiment 2: **{ans}**"],
        hints=["What happens to the force if just one of the two (current or field) is reversed?",
               "And what if both are reversed?",
               "One reversal flips the force; two reversals flip it back."],
    )


@template("c18_electromagnet_strongest", chapter=18, level=2, lo="18b")
def electromagnet_strongest(rng):
    rows = [("P", 50, 1.0), ("Q", 100, 1.0), ("R", 50, 2.0), ("S", 100, 2.0)]
    core = rng.choice(["soft iron", "air"])
    rng.shuffle(rows)
    ans = "S" if True else None
    strongest = max(rows, key=lambda r: r[1] * r[2])[0]
    wrongs = {r[0]: f"Coil {r[0]} has {r[1]} turns and {fmt(r[2])} A. Field strength increases with BOTH the number of turns and the current, so it is weaker than the coil that has the most of both." for r in rows if r[0] != strongest}
    opts, key, mis = text_options(rng, strongest, wrongs)
    table = md_table(["coil", "number of turns", "current / A", "core"], [[r[0], r[1], fmt(r[2]), core] for r in rows])
    return dict(
        stem=f"Four solenoids are made with the same length and the same {core} core.\n\n{table}\n\nWhich coil produces the strongest magnetic field?",
        options=opts, key=key, misconceptions=mis,
        formula="the field of a solenoid is stronger with more turns and with a larger current (and with a soft-iron core)",
        working=["compare turns × current for each coil", f"coil **{strongest}** has the most turns AND the largest current"],
        hints=["Which two quantities in the table make an electromagnet stronger?",
               "More turns → stronger. More current → stronger.",
               "Find the coil that has both the most turns and the largest current."],
    )


# ---------------------------------------------------------------- L3
@template("c18_force_proportional_current", chapter=18, level=3, lo="18c")
def force_proportional_current(rng):
    I1 = nice(rng, 1.0, 1.5, 2.0, 2.5)
    F1 = nice(rng, 0.020, 0.030, 0.040, 0.050)
    k = nice(rng, 2, 3, 4)
    I2 = I1 * k
    F2 = F1 * k
    opts, key, mis = numeric_options(rng, F2, [
        (F1, "The force is not fixed: it is proportional to the current in the wire."),
        (F1 * k * k, "The force is proportional to the current, not to the current squared."),
        (F1 / k, "A larger current gives a LARGER force."),
    ], unit="N", sf=3)
    table = md_table(["current in wire / A", "force on wire / N"], [[fmt(I1), fmt(F1)], [fmt(I2), "?"]])
    return dict(
        stem=f"A student measures the force on a wire placed at right angles to a uniform magnetic field. The force is proportional to the current.\n\n{table}\n\nWhat is the force when the current is **{fmt(I2)} A**?",
        options=opts, key=key, misconceptions=mis,
        formula="in a fixed field, force on the wire ∝ current",
        working=[f"current × {fmt(k)}", f"force × {fmt(k)} = {fmt(F1)} × {fmt(k)}", f"= **{fmt(F2, sf=3)} N**"],
        hints=["How many times larger is the new current?", f"{fmt(I2)} ÷ {fmt(I1)} = {fmt(k)}.", f"Multiply the force by {fmt(k)}."],
    )


@template("c18_electromagnet_pins", chapter=18, level=3, lo="18b")
def electromagnet_pins(rng):
    n1 = nice(rng, 40, 50, 60)
    I = nice(rng, 1.0, 1.5, 2.0)
    pins1 = nice(rng, 6, 8, 10, 12)
    k = nice(rng, 2, 3)
    pins2 = pins1 * k
    opts, key, mis = numeric_options(rng, pins2, [
        (pins1, "Adding turns makes the electromagnet stronger, so it picks up more pins."),
        (pins1 + k, f"The strength roughly doubles or triples with the number of turns; multiply, do not add {k}."),
        (pins1 * k * k, "The pattern in the data is proportional: × the number of turns, not × its square."),
    ], unit="pins")
    table = md_table(["turns on coil", "current / A", "pins picked up"], [[n1, fmt(I), pins1], [n1 * k, fmt(I), "?"]])
    return dict(
        stem=f"A student tests an electromagnet by counting the pins it picks up. Over this range the number of pins is proportional to the number of turns.\n\n{table}\n\nHow many pins should the second coil pick up?",
        options=opts, key=key, misconceptions=mis,
        formula="with the same current, the field (and pins picked up, over this range) ∝ number of turns",
        working=[f"turns × {k} at the same current", f"pins = {pins1} × {k}", f"= **{pins2}**"],
        hints=["What is the same and what changes between the two rows?", f"The turns are multiplied by {k}.", f"Multiply the pins by {k}."],
    )


# ---------------------------------------------------------------- L4
@template("c18_commutator_reversals", chapter=18, level=4, lo="18f")
def commutator_reversals(rng):
    rpm = nice(rng, 300, 600, 900, 1200, 1500)
    rps = rpm / 60
    rev = 2 * rps
    opts, key, mis = numeric_options(rng, rev, [
        (rps, "The split-ring commutator reverses the current every HALF turn, i.e. twice per revolution."),
        (2 * rpm, "That is reversals per MINUTE. Convert revolutions per minute to per second first."),
        (rpm, "That is the revolutions per minute. The current reverses twice per revolution, and the question asks per second."),
    ], unit="per second", sf=3)
    return dict(
        stem=f"Fig. 1 shows a simple d.c. motor with a split-ring commutator. The coil turns at **{rpm} revolutions per minute**. How many times per second does the commutator reverse the current in the coil?",
        figure=figs3.motor_diagram(),
        options=opts, key=key, misconceptions=mis,
        formula="the split-ring commutator reverses the current in the coil every half turn (when the coil is vertical): 2 reversals per revolution",
        working=[f"{rpm} rev/min = {fmt(rps)} rev/s", "2 reversals per revolution", f"= 2 × {fmt(rps)} = **{fmt(rev, sf=3)}** per second"],
        hints=["When does the commutator reverse the current? Each time the coil passes the vertical position.",
               "That happens twice in each complete turn.",
               f"Convert {rpm} rev per minute to rev per second, then double."],
    )


@template("c18_motor_faster_change", chapter=18, level=4, lo="18e")
def motor_faster_change(rng):
    base_turns = nice(rng, 50, 100, 200)
    ans = rng.choice([f"increase the number of turns on the coil from {base_turns} to {2 * base_turns}", "increase the current in the coil"])
    wrongs = {"reverse the direction of the current": "Reversing the current makes the motor turn the other way; it does not make the turning effect bigger.",
              "replace the soft-iron core with a wooden one": "A soft-iron core strengthens the field and the turning effect; wood would weaken it.",
              "swap the positions of the N and S poles": "Swapping the poles reverses the direction of rotation, not its strength."}
    opts, key, mis = text_options(rng, ans, wrongs)
    table = md_table(["feature of the motor", "value"], [["number of turns on the coil", base_turns], ["core", "soft iron"], ["current", "2.0 A"]])
    return dict(
        stem=f"Fig. 1 shows a simple d.c. motor.\n\n{table}\n\nWhich change would increase the turning effect on the coil?",
        figure=figs3.motor_diagram(),
        options=opts, key=key, misconceptions=mis,
        formula="the turning effect on the coil increases with the number of turns, the current, and the strength of the field (soft-iron core)",
        working=["the force on each side of the coil ∝ current, and there is one such force per turn", f"so **{ans}** increases the turning effect"],
        hints=["The syllabus lists two ways to increase the turning effect on a motor coil.",
               "Think about the current in the coil and the number of turns.",
               "Changes that only REVERSE something change the direction, not the size."],
    )


# ---------------------------------------------------------------- L5
@template("c18_electron_beam_deflection", chapter=18, level=5, lo="18c")
def electron_beam_deflection(rng):
    field = rng.choice(["right", "left"])
    electrons = rng.choice(["into", "out"])
    conv = "out" if electrons == "into" else "into"        # conventional current is opposite to the electron flow
    f = figs3.lhr_force(field, conv)
    ans = "upwards" if f == "up" else "downwards"
    wrongs = {_flip(ans): "Fleming's left-hand rule uses CONVENTIONAL current. Electrons are negative, so the current is opposite to their motion: reverse the electron direction before applying the rule.",
              f"to the {field}": "That is the field direction. The force is at right angles to both the field and the beam.",
              "the beam is not deflected": "A moving charge crossing a magnetic field at right angles feels a force, just like a current in a wire."}
    opts, key, mis = text_options(rng, ans, wrongs)
    return dict(
        stem=f"A beam of electrons travels **{electrons} the page** through the magnetic field shown in Fig. 1 (the marked wire position shows where the beam crosses). In which direction is the beam deflected?",
        figure=figs3.flemings_lhr(field=field, current=electrons),
        options=opts, key=key, misconceptions=mis,
        formula="a beam of electrons is a current in the OPPOSITE direction to the electrons' motion; then apply Fleming's left-hand rule",
        working=[f"electrons {electrons} the page → conventional current {conv} the page", f"field to the {field}", f"force (thumb) **{ans}**"],
        hints=["Fleming's rule uses conventional current. Which way is the current for a beam of negative electrons?",
               f"Current is {conv} the page. Now point the first finger along the field (to the {field}).",
               "Second finger along the current; the thumb gives the force."],
    )
