"""Chapter 2 Kinematics written-answer bank extension: 5 more per level (10 per level), every LO at least twice."""
from .. import figs
from ..marker import Pitfall, Point
from .base import written

P = Point
PF = Pitfall


def vt(pts, ylabel="velocity / m/s"):
    xs, ys = zip(*pts)
    return lambda: figs.graph(pts, max(xs), max(ys) * 1.25 + 1, max(1, round(max(xs) / 6)), max(1, round(max(ys) * 1.25 / 5)), ylabel=ylabel)


# ---------------------------------------------------------------- L1
written("w2b_uniform_accel_meaning", 2, 1, "2c",
        stem="State what is meant by uniform acceleration.",
        points=[P("the velocity changes by the same amount every second / constant rate of change of velocity", ["same amount every second", "same amount each second", "constant rate", "constant acceleration", "changes by equal amounts", "steadily"])],
        pitfalls=[PF(["constant velocity", "constant speed"], "Constant VELOCITY means zero acceleration. Uniform acceleration means the velocity changes at a constant rate.")],
        model_answer="Uniform acceleration means the velocity changes by the same amount every second, i.e. the rate of change of velocity is constant.",
        hints=["Acceleration is about how velocity changes.", "What does 'uniform' tell you about that change?", "Same change in each second."],
        keywords="velocity changes at a constant rate",
        sample_pass=["The velocity changes by the same amount every second", "a constant rate of change of velocity"],
        sample_fail=["Moving at a constant velocity", "Speeding up faster and faster"])

written("w2b_gradient_vt", 2, 1, "2e",
        stem="State what the gradient of a velocity-time graph represents.",
        points=[P("the acceleration", ["acceleration", "accelerat"])],
        pitfalls=[PF(["distance", "displacement"], "The AREA under a v-t graph gives displacement; the gradient gives acceleration.")],
        model_answer="The gradient of a velocity-time graph represents the acceleration.",
        hints=["Gradient = rise ÷ run on these axes.", "Change in velocity ÷ time.", "Name the quantity."],
        keywords="acceleration",
        sample_pass=["acceleration", "It represents the acceleration of the object"],
        sample_fail=["the distance travelled", "the speed"])

written("w2b_g_value_meaning", 2, 1, "2i",
        stem="The acceleration of free fall near the Earth is about 10 m/s². State what this tells you about the speed of a falling stone (with no air resistance).",
        points=[P("its speed increases by 10 m/s every second", ["increases by 10 m/s every second", "10 m/s each second", "10 m/s every second", "gains 10 m/s", "10 m/s per second"])],
        model_answer="Its speed increases by 10 m/s every second it falls.",
        hints=["Acceleration = change in velocity per second.", "So what is added to the speed each second?", "Say it in one sentence."],
        keywords="speed increases by 10 m/s each second",
        sample_pass=["Its speed increases by 10 m/s every second", "it gains 10 m/s of speed each second"],
        sample_fail=["It falls 10 m every second", "It falls at a constant 10 m/s"])

written("w2b_define_average_speed", 2, 1, "2b",
        stem="State the equation used to calculate average speed.",
        points=[P("average speed = total distance travelled ÷ total time taken", ["total distance", "distance travelled divided by", "distance / time", "distance ÷ time", "distance over time", "distance divided by time"])],
        pitfalls=[PF(["time divided by distance", "time / distance", "time ÷ distance"], "It is distance ÷ time, not time ÷ distance.")],
        model_answer="Average speed = total distance travelled ÷ total time taken.",
        hints=["It is about a whole journey.", "Which two totals are needed?", "Write it as an equation in words."],
        keywords="total distance ÷ total time",
        sample_pass=["average speed = total distance travelled / total time taken", "distance travelled divided by time taken"],
        sample_fail=["time divided by distance", "the top speed divided by two"])

written("w2b_speed_unit", 2, 1, "2b",
        stem="State the SI unit of speed and one other unit that is commonly used for the speed of cars.",
        points=[P("metre per second (m/s)", ["m/s", "metre per second", "metres per second", "m s-1"]),
                P("kilometre per hour (km/h)", ["km/h", "kilometre per hour", "kilometres per hour", "kmh"])],
        model_answer="The SI unit is the metre per second (m/s); cars commonly use kilometres per hour (km/h).",
        hints=["Speed = distance ÷ time in SI units.", "Look at a car's speedometer for the other.", "Give both."],
        keywords="m/s; km/h",
        sample_pass=["m/s and km/h", "metres per second, kilometres per hour"],
        sample_fail=["m/s² and newtons", "metres and seconds"])

# ---------------------------------------------------------------- L2
written("w2b_measure_average_speed", 2, 2, "2b",
        stem="Describe how to measure the average speed of a student walking along a corridor.",
        points=[P("measure the distance (e.g. 20 m) with a measuring tape", ["measure the distance", "measuring tape", "tape", "measure a distance", "metre rule"]),
                P("time the walk with a stopwatch", ["stopwatch", "time the", "time how long", "time taken"]),
                P("average speed = distance ÷ time", ["distance divided by time", "distance / time", "distance ÷ time", "divide the distance by the time"])],
        min_points=2,
        model_answer="Measure a distance along the corridor, for example 20 m, with a measuring tape. Time the student walking that distance with a stopwatch. Average speed = distance ÷ time.",
        hints=["Which two quantities do you need?", "Which instrument measures each?", "How do you combine them?"],
        keywords="measure distance (tape); time with stopwatch; speed = distance ÷ time",
        sample_pass=["Measure the distance with a measuring tape, time the walk with a stopwatch, then divide distance by time", "use a tape to measure 20 m, time it with a stopwatch and calculate distance / time"],
        sample_fail=["Ask the student how fast they walk", "Use a thermometer and a balance"])

written("w2b_nonuniform_example", 2, 2, "2d",
        stem="Give an example of motion with non-uniform acceleration and describe how its acceleration changes.",
        points=[P("example: a falling skydiver / car moving off and approaching top speed / object falling through air or oil", ["skydiver", "parachutist", "falling through air", "car approaching its top speed", "falling in oil", "raindrop", "car pulling away"]),
                P("the acceleration decreases (or changes) as air resistance / drag increases with speed", ["decreases", "gets smaller", "changes", "air resistance increases", "drag increases", "less and less"])],
        model_answer="A skydiver falling before terminal velocity: her acceleration starts at about 10 m/s² and decreases as air resistance increases with speed, until it becomes zero.",
        hints=["Non-uniform means the acceleration itself is changing.", "Think of something affected by air resistance.", "Give the example and say how the acceleration changes."],
        keywords="e.g. skydiver; acceleration decreases as air resistance grows",
        sample_pass=["A skydiver: the acceleration decreases as the air resistance increases", "a raindrop falling through air, whose acceleration gets smaller as drag increases"],
        sample_fail=["A car at a constant 50 km/h", "A stone in a vacuum accelerating at 10 m/s²"])

written("w2b_dt_straight_slope", 2, 2, "2f",
        stem="Fig. 1 is a distance-time graph that is a straight line sloping upwards. Describe the motion and explain how the graph shows it.",
        points=[P("the object moves with constant (uniform) speed / velocity", ["constant speed", "uniform speed", "constant velocity", "steady speed", "uniform velocity"]),
                P("because the gradient (speed) is constant: a straight line has the same gradient everywhere", ["gradient is constant", "same gradient", "constant gradient", "straight line", "gradient is the speed"])],
        model_answer="The object is moving at a constant speed. The gradient of a distance-time graph is the speed, and a straight line has the same gradient everywhere.",
        hints=["What does the gradient of a d-t graph represent?", "Is the gradient changing along a straight line?", "Describe and explain."],
        keywords="constant speed; constant gradient",
        figure=vt([(0, 0), (8, 24)], ylabel="distance / m"),
        sample_pass=["Constant speed, because the gradient of the straight line is constant", "it moves at a steady speed since the gradient is the same everywhere"],
        sample_fail=["It is accelerating because the line rises", "It is at rest"])

written("w2b_vt_on_axis", 2, 2, "2g",
        stem="Describe the motion shown by a velocity-time graph that runs along the time axis, then rises in a straight line, then is horizontal.",
        points=[P("at rest at first (velocity zero)", ["at rest", "stationary", "not moving", "zero velocity"]),
                P("then uniform acceleration (straight sloping line)", ["uniform acceleration", "constant acceleration", "accelerates uniformly", "speeds up steadily"]),
                P("then constant velocity (horizontal line)", ["constant velocity", "uniform velocity", "constant speed", "steady speed"])],
        min_points=2,
        model_answer="At first the object is at rest (zero velocity). Then it accelerates uniformly (straight sloping line). Finally it moves with a constant velocity (horizontal line).",
        hints=["What does a line ON the time axis mean?", "What does a straight sloping line mean?", "And a horizontal line above the axis?"],
        keywords="at rest; uniform acceleration; constant velocity",
        figure=vt([(0, 0), (3, 0), (7, 12), (12, 12)]),
        sample_pass=["At rest, then uniform acceleration, then constant velocity", "it is stationary, accelerates at a constant rate, then moves at a steady speed"],
        sample_fail=["It falls, rises and stops", "It is decelerating throughout"])

written("w2b_area_meaning", 2, 2, "2h",
        stem="Explain why the area under a velocity-time graph gives the displacement.",
        points=[P("each strip of area = velocity × time interval", ["velocity × time", "velocity x time", "velocity times time", "speed times time", "height times width", "velocity multiplied by time"]),
                P("velocity × time = displacement (distance moved), so adding all the strips gives the total displacement", ["displacement", "distance moved", "distance travelled", "add up", "total"])],
        model_answer="The area of each thin strip under the graph is velocity × time interval, and velocity × time is the displacement in that interval. Adding all the strips gives the total displacement.",
        hints=["What are the units of the area: (m/s) × s?", "Velocity × time = ?", "Explain with a strip of area."],
        keywords="area = velocity × time = displacement",
        sample_pass=["Each strip is velocity times time, which is the displacement, so the total area is the total displacement", "area = height × width = velocity × time = distance travelled"],
        sample_fail=["Because the area gives the acceleration", "The area is the speed"])

# ---------------------------------------------------------------- L3
written("w2b_average_two_parts", 2, 3, "2b",
        stem="A bus travels 6 km in 10 minutes and then 2 km in 10 minutes. A student says the average speed is the average of the two speeds. Explain how to find the correct average speed and whether the student is right in this case.",
        points=[P("average speed = total distance ÷ total time = 8 km ÷ 20 min", ["total distance", "8 km", "20 min", "20 minutes", "divided by the total time"]),
                P("= 0.4 km/min = 24 km/h (6.7 m/s)", ["24 km/h", "0.4 km/min", "6.7 m/s", "6.67"]),
                P("here the times are equal, so averaging the speeds (36 and 12 km/h) happens to give the same answer", ["times are equal", "equal times", "same time", "happens to", "only because", "36 and 12"])],
        min_points=2,
        model_answer="Average speed = total distance ÷ total time = 8 km ÷ 20 min = 0.4 km/min = 24 km/h. Because the two parts take equal times, the average of the two speeds (36 km/h and 12 km/h) happens to give the same value; in general it does not.",
        hints=["Use the totals.", "Convert to km/h if you like.", "When does averaging the speeds work?"],
        keywords="total distance ÷ total time = 24 km/h; equal times so the speed average works here",
        sample_pass=["Total distance 8 km divided by total time 20 minutes gives 24 km/h; it works here only because the times are equal", "8 km in 20 min is 24 km/h, the student is right only because the two times are the same"],
        sample_fail=["Add 6 and 2 and divide by 2", "The average speed is 6 km per 10 minutes"])

written("w2b_accel_from_rest_meaning", 2, 3, "2c",
        stem="A car accelerates from rest at 2 m/s². Describe how its velocity changes during the first 3 s.",
        points=[P("velocity increases by 2 m/s every second", ["2 m/s every second", "2 m/s each second", "increases by 2", "2 m/s per second", "2 m/s after 1 s", "4 m/s after 2 s"]),
                P("so it is 2, 4 and 6 m/s after 1, 2 and 3 s", ["6 m/s", "2, 4", "2 m/s, 4 m/s", "4 m/s"])],
        model_answer="Its velocity increases by 2 m/s every second: 2 m/s after 1 s, 4 m/s after 2 s and 6 m/s after 3 s.",
        hints=["What does 2 m/s² mean each second?", "Start from 0.", "Give the velocity at the end of each second."],
        keywords="+2 m/s each second: 2, 4, 6 m/s",
        sample_pass=["It increases by 2 m/s every second, reaching 6 m/s after 3 s", "2 m/s after 1 s, 4 m/s after 2 s and 6 m/s after 3 s"],
        sample_fail=["It moves 2 m every second", "It stays at 2 m/s"])

written("w2b_read_graph_steps", 2, 3, "2e",
        stem="Fig. 1 is the velocity-time graph of a lift. Describe how to find the total distance it travels from the graph.",
        points=[P("the distance is the area under the graph", ["area under", "area of the graph", "area"]),
                P("split the area into simple shapes (triangles and rectangle) and add their areas", ["triangle", "rectangle", "trapezium", "split", "add"]),
                P("use the axis units: area = velocity × time in m", ["velocity × time", "velocity x time", "units", "metres", "m/s × s"])],
        min_points=2,
        model_answer="The distance is the area under the velocity-time graph. Split it into simple shapes, two triangles and a rectangle here, work out each area using the axis values (velocity × time, giving metres) and add them.",
        hints=["Which feature of a v-t graph gives distance?", "How do you find the area of an awkward shape?", "Use the axis values."],
        keywords="area under graph; split into triangles + rectangle; add",
        figure=vt([(0, 0), (2, 3), (8, 3), (10, 0)]),
        sample_pass=["Find the area under the graph by splitting it into triangles and a rectangle and adding them", "the distance is the area, so add the areas of the two triangles and the rectangle"],
        sample_fail=["Read the highest point of the graph", "Find the gradient of the line"])

written("w2b_vt_curve_flattening", 2, 3, "2g",
        stem="Fig. 1 shows the velocity-time graph of a car pulling away. The curve becomes less steep with time. Explain what this shows about the car's acceleration.",
        points=[P("the gradient of a v-t graph is the acceleration", ["gradient is the acceleration", "gradient represents acceleration", "gradient = acceleration", "gradient gives the acceleration"]),
                P("the gradient is decreasing, so the acceleration is decreasing (non-uniform acceleration)", ["decreasing", "gets smaller", "less steep", "acceleration decreases", "non-uniform"])],
        model_answer="The gradient of a velocity-time graph is the acceleration. The curve becomes less steep, so the gradient, and therefore the acceleration, is decreasing: the car still speeds up, but more slowly.",
        hints=["What does the gradient of a v-t graph represent?", "Is the gradient increasing or decreasing?", "Link the two."],
        keywords="gradient = acceleration; gradient decreasing → acceleration decreasing",
        figure=vt([(0, 0), (2, 8), (4, 13), (6, 15.5), (8, 16.5)]),
        sample_pass=["The gradient is the acceleration and it is decreasing, so the acceleration decreases", "less steep means the gradient gets smaller so the car's acceleration decreases"],
        sample_fail=["The car is slowing down", "The acceleration is constant"])

written("w2b_freefall_distance_rises", 2, 3, "2i",
        stem="A ball is dropped from a high window. Explain why it falls a greater distance in the second second than in the first second (ignore air resistance).",
        points=[P("it accelerates (at 10 m/s²), so its speed increases", ["accelerates", "speed increases", "gets faster", "speeds up", "10 m/s²", "10 m/s every second"]),
                P("its average speed during the second second is greater, so it covers more distance in the same time", ["average speed is greater", "moving faster", "greater speed", "more distance in the same time", "faster during the second", "travels further", "goes further", "further in the second"])],
        model_answer="The ball accelerates at 10 m/s², so its speed keeps increasing. During the second second it is moving faster on average than during the first, so it covers a greater distance in the same time (5 m in the first second, 15 m in the second).",
        hints=["Is the ball's speed constant?", "Distance in each second depends on the speed during that second.", "Explain the difference."],
        keywords="accelerates, speed increases; faster in the second second → more distance",
        sample_pass=["It accelerates so it moves faster during the second second and covers more distance", "its speed increases by 10 m/s each second so in the second second it travels further"],
        sample_fail=["Gravity gets stronger as it falls", "It falls the same distance each second"])

# ---------------------------------------------------------------- L4
written("w2b_accel_negative_forward", 2, 4, "2c",
        stem="A cyclist moving forwards has an acceleration of −1.5 m/s². Explain what this means, and describe what happens to her velocity over the next 4 s if she starts at 8 m/s.",
        points=[P("negative acceleration (opposite to the motion) means she is slowing down / decelerating", ["slowing down", "decelerat", "opposite to the motion", "speed decreases"]),
                P("her velocity falls by 1.5 m/s every second", ["1.5 m/s every second", "1.5 m/s each second", "falls by 1.5", "decreases by 1.5"]),
                P("after 4 s her velocity is 8 − 6 = 2 m/s", ["2 m/s", "8 - 6", "8 − 6", "2 m/s after 4 s"])],
        min_points=2,
        model_answer="The acceleration is opposite to her motion, so she is slowing down: her velocity decreases by 1.5 m/s every second. After 4 s her velocity is 8 − 4 × 1.5 = 2 m/s.",
        hints=["What does the minus sign mean when she is moving forwards?", "How much does her velocity change each second?", "Work out the velocity after 4 s."],
        keywords="slowing down; −1.5 m/s each second; 2 m/s after 4 s",
        sample_pass=["She is slowing down; her velocity falls by 1.5 m/s each second, so after 4 s it is 2 m/s", "deceleration of 1.5 m/s every second, 8 - 6 = 2 m/s"],
        sample_fail=["She is moving backwards at 1.5 m/s", "Her velocity increases to 14 m/s"])

written("w2b_rain_drop_motion", 2, 4, "2d",
        stem="Describe and explain how the velocity of a raindrop changes as it falls from a cloud, from the moment it starts to fall until it reaches a steady speed.",
        points=[P("at first it accelerates at about 10 m/s² (air resistance negligible)", ["10 m/s²", "accelerates", "speeds up", "air resistance is small", "only weight"]),
                P("as its speed increases, air resistance increases, so the resultant force and acceleration decrease", ["air resistance increases", "drag increases", "resultant force decreases", "acceleration decreases"]),
                P("when air resistance equals its weight the resultant force is zero and it falls at a constant (terminal) velocity", ["terminal velocity", "constant velocity", "constant speed", "steady speed", "equals its weight", "balanced"])],
        min_points=2,
        model_answer="At first the drop accelerates at about 10 m/s², because air resistance is negligible at low speed. As its speed increases, air resistance increases, so the resultant force and the acceleration decrease. When air resistance equals the weight, the resultant force is zero and the drop falls at a constant terminal velocity.",
        hints=["Which forces act at the start, and later?", "How does air resistance depend on speed?", "What happens when the forces balance?"],
        keywords="starts at 10 m/s²; air resistance grows, acceleration falls; terminal velocity when balanced",
        sample_pass=["It accelerates at first, then air resistance increases so the acceleration decreases until air resistance equals the weight and it reaches terminal velocity",
                     "speeds up, drag increases, the resultant force falls to zero and it moves at a constant velocity"],
        sample_fail=["It falls at a constant speed from the start", "It keeps accelerating at 10 m/s² until it hits the ground"])

written("w2b_dt_vt_same_motion", 2, 4, "2e",
        stem="An object moves at a constant velocity of 3 m/s for 5 s. Describe the shapes of its distance-time and velocity-time graphs, and explain how each shows the same motion.",
        points=[P("distance-time: a straight line through the origin with gradient 3 m/s", ["straight line", "sloping", "gradient 3", "rises steadily", "through the origin"]),
                P("velocity-time: a horizontal line at 3 m/s", ["horizontal line", "horizontal at 3", "flat line", "horizontal"]),
                P("the d-t gradient is the speed (constant); the v-t area (3 × 5 = 15 m) is the distance", ["gradient is the speed", "area", "15 m", "constant gradient"])],
        min_points=2,
        model_answer="The distance-time graph is a straight line rising from the origin with a constant gradient of 3 m/s; its gradient is the speed. The velocity-time graph is a horizontal line at 3 m/s; the area under it, 3 × 5 = 15 m, is the distance, which matches the final distance on the d-t graph.",
        hints=["What shape shows constant speed on a d-t graph?", "What shape shows constant velocity on a v-t graph?", "Link gradient and area to the same motion."],
        keywords="d-t straight sloping line (gradient 3); v-t horizontal line at 3; area 15 m",
        sample_pass=["The distance-time graph is a straight sloping line with gradient 3 and the velocity-time graph is a horizontal line at 3 m/s, whose area is 15 m",
                     "a straight line on the d-t graph and a horizontal line on the v-t graph; the gradient is the speed and the area is the distance"],
        sample_fail=["Both graphs are horizontal lines", "Both graphs are curves"])

written("w2b_dt_curving_down", 2, 4, "2f",
        stem="Fig. 1 is a distance-time graph that rises steeply at first, then curves until it is horizontal. Describe and explain the motion.",
        points=[P("the gradient (speed) decreases, so the object slows down", ["slows down", "slowing", "speed decreases", "gradient decreases", "decelerat"]),
                P("when the graph is horizontal the gradient is zero, so it is at rest", ["at rest", "stops", "stationary", "gradient is zero", "speed is zero"])],
        model_answer="The gradient of the distance-time graph is the speed. The gradient decreases, so the object slows down; when the graph becomes horizontal the gradient is zero and the object is at rest.",
        hints=["What does the gradient represent?", "How does the gradient change along the curve?", "What does a horizontal section mean?"],
        keywords="gradient = speed decreasing → slowing; horizontal → at rest",
        figure=vt([(0, 0), (1, 7), (2, 12), (3, 15), (4, 16), (6, 16)], ylabel="distance / m"),
        sample_pass=["The gradient decreases so it slows down, and when horizontal it is at rest", "it decelerates until it stops because the gradient falls to zero"],
        sample_fail=["It speeds up then moves at constant speed", "It moves backwards"])

written("w2b_dt_two_objects", 2, 4, "2f",
        stem="Two cars P and Q have straight-line distance-time graphs. P's line starts at the origin; Q's line starts at 50 m and is less steep. Compare their motions.",
        points=[P("both move at constant speeds (straight lines)", ["both constant", "constant speed", "steady speeds", "uniform speeds", "straight lines"]),
                P("P is faster (steeper gradient)", ["p is faster", "p has a greater speed", "p's line is steeper", "p moves faster"]),
                P("Q started 50 m ahead (from 50 m) but P catches up where the lines cross", ["50 m ahead", "starts 50 m", "ahead", "head start", "lines cross", "catches up", "overtakes"])],
        min_points=2,
        model_answer="Both cars move at constant speeds, because both lines are straight. P is faster because its line is steeper. Q starts 50 m further along, but P catches it up where the two lines cross.",
        hints=["What do straight lines mean?", "Which car is faster? How can you tell?", "What does Q's starting point mean?"],
        keywords="both constant speeds; P faster (steeper); Q starts 50 m ahead; P catches up at the crossing",
        sample_pass=["Both have constant speeds, P is faster because its line is steeper, and Q started 50 m ahead", "P's gradient is bigger so it is faster; Q had a head start of 50 m but P catches up where the lines cross"],
        sample_fail=["Q is faster because it starts higher", "Both cars are accelerating"])

# ---------------------------------------------------------------- L5
written("w2b_eval_speed_velocity_claim", 2, 5, "2a",
        stem="A student says: 'Speed and velocity are the same because both are measured in m/s.' Evaluate this claim, using an example.",
        points=[P("the claim is wrong: having the same unit does not make them the same quantity", ["wrong", "incorrect", "same unit does not", "not the same"]),
                P("speed is a scalar (magnitude only); velocity is a vector (magnitude and direction)", ["scalar", "vector", "direction"]),
                P("example: a car going round a roundabout at constant speed has a changing velocity / two cars at 20 m/s in opposite directions have different velocities", ["roundabout", "opposite directions", "circle", "bend", "round a track", "different velocities"])],
        min_points=2,
        model_answer="The claim is wrong. Sharing a unit does not make two quantities the same. Speed is a scalar (magnitude only), while velocity is a vector (magnitude and direction). For example, a car going round a roundabout at a constant speed has a changing velocity because its direction changes.",
        hints=["Does sharing a unit make two quantities identical?", "Which one includes direction?", "Give an example where they differ."],
        keywords="wrong; speed scalar, velocity vector; e.g. roundabout at constant speed",
        sample_pass=["Wrong, speed is a scalar but velocity is a vector with direction; a car on a roundabout has constant speed but changing velocity",
                     "incorrect, the same unit does not mean the same quantity: two cars at 20 m/s in opposite directions have different velocities"],
        sample_fail=["Correct, they are the same thing", "Speed is always larger than velocity"])

written("w2b_eval_deceleration_graph", 2, 5, "2c",
        stem="A student says: 'If the velocity-time graph of a car is above the time axis, the car cannot be decelerating.' Evaluate.",
        points=[P("the claim is wrong", ["wrong", "incorrect", "not true", "false"]),
                P("above the axis only means the velocity is positive (moving forwards)", ["positive velocity", "moving forwards", "velocity is positive", "direction"]),
                P("if the line slopes downwards (negative gradient) the car is slowing down / decelerating while still moving forwards", ["slopes downwards", "negative gradient", "line falls", "slowing down", "velocity decreasing"])],
        min_points=2,
        model_answer="The claim is wrong. A line above the axis only shows that the velocity is positive, i.e. the car is moving forwards. If that line slopes downwards (negative gradient), the velocity is decreasing, so the car is decelerating while still moving forwards.",
        hints=["What does being above the axis tell you?", "What does the slope tell you?", "Can a car move forwards and slow down?"],
        keywords="wrong; above axis = moving forwards; downward slope = decelerating",
        sample_pass=["Wrong, above the axis just means it moves forwards; a downward slope means it is decelerating", "incorrect, if the line slopes down the velocity is decreasing even though it is positive"],
        sample_fail=["Correct, deceleration needs a negative velocity", "Correct because the graph is above zero"])

written("w2b_eval_area_gradient", 2, 5, "2e",
        stem="A student finds the distance travelled by a car from the GRADIENT of its velocity-time graph. Evaluate this method and state the correct one.",
        points=[P("the method is wrong: the gradient gives the acceleration", ["wrong", "incorrect", "gradient gives the acceleration", "gradient is the acceleration"]),
                P("the distance is the area under the velocity-time graph", ["area under", "area"]),
                P("units check: gradient has units m/s², area has units (m/s) × s = m", ["m/s²", "units", "m/s × s", "(m/s) x s", "metres"])],
        min_points=2,
        model_answer="The method is wrong: the gradient of a velocity-time graph gives the acceleration (units m/s²). The distance is the area under the graph, whose units are (m/s) × s = m.",
        hints=["What does the gradient of a v-t graph give?", "Which feature gives distance?", "Check with units."],
        keywords="wrong; gradient = acceleration; area = distance; units check",
        sample_pass=["Wrong, the gradient gives the acceleration; the distance is the area under the graph", "incorrect, use the area under the v-t graph, since the gradient has units m/s²"],
        sample_fail=["Correct, gradient gives the distance", "Read the highest velocity on the graph"])

written("w2b_eval_dt_speed_claim", 2, 5, "2f",
        stem="A student says that a steep distance-time graph always shows a large acceleration. Evaluate.",
        points=[P("the claim is wrong: steepness of a d-t graph shows SPEED, not acceleration", ["wrong", "incorrect", "speed", "gradient is the speed"]),
                P("a steep straight line means a high constant speed, i.e. zero acceleration", ["zero acceleration", "no acceleration", "constant speed", "straight line"]),
                P("acceleration is shown by a CHANGING gradient (a curve) on a d-t graph", ["curve", "changing gradient", "gradient changes", "curved"])],
        min_points=2,
        model_answer="The claim is wrong. The gradient of a distance-time graph is the speed, so a steep line shows a high speed. If the steep line is straight, the speed is constant and the acceleration is zero. Acceleration is shown on a distance-time graph by a changing gradient, i.e. a curve.",
        hints=["What does the gradient of a d-t graph represent?", "What does a straight steep line mean?", "How would acceleration show on a d-t graph?"],
        keywords="wrong; steep = fast; straight = zero acceleration; acceleration = curve",
        sample_pass=["Wrong, steepness shows speed; a straight steep line has zero acceleration, acceleration shows as a curve", "incorrect, the gradient is the speed, so a steep straight line means a high constant speed and no acceleration"],
        sample_fail=["Correct, steep lines always mean acceleration", "The steepness shows the distance"])

written("w2b_eval_freefall_mass", 2, 5, "2i",
        stem="A student drops a 1 kg ball and a 5 kg ball from 2 m and says the 5 kg ball must land five times sooner. Evaluate, explaining what you would actually observe.",
        points=[P("the claim is wrong", ["wrong", "incorrect", "not true", "false"]),
                P("in free fall all objects have the same acceleration (about 10 m/s²), whatever their mass", ["same acceleration", "10 m/s²", "regardless of mass", "independent of mass", "does not depend on mass"]),
                P("so both balls land at (almost) the same time; air resistance over 2 m is negligible for dense balls", ["same time", "together", "at the same time", "air resistance is negligible", "air resistance is small"])],
        min_points=2,
        model_answer="The claim is wrong. In free fall all objects have the same acceleration of about 10 m/s², whatever their mass, because a heavier ball has a proportionally larger weight. Over 2 m air resistance on dense balls is negligible, so both balls land at almost the same time.",
        hints=["Does mass affect the acceleration of free fall?", "Why not, in terms of weight and mass?", "What would you actually see?"],
        keywords="wrong; same acceleration g for all masses; land together (air resistance negligible)",
        sample_pass=["Wrong, both have the same acceleration of 10 m/s² so they land at the same time", "incorrect, mass does not affect the acceleration of free fall and air resistance is small, so they land together"],
        sample_fail=["Correct, heavier objects fall faster", "The 1 kg ball lands first"])
