import streamlit as st
import random

# ---------------------------------------------------------
# QUESTION OPTIONS
# ---------------------------------------------------------
MOOD_OPTIONS = ["Tired", "Normal", "Energized"]
TIME_OPTIONS = ["< 20 minutes", "20–40 minutes", "> 40 minutes"]
GOAL_OPTIONS = ["Relax / De-stress", "General Fitness", "Build Strength", "High Intensity / Sweat"]
LOCATION_OPTIONS = ["Home (no equipment)", "Home (some equipment)", "Gym"]
LEVEL_OPTIONS = ["Beginner", "Intermediate", "Advanced"]

# ---------------------------------------------------------
# IMAGE MAP
# ---------------------------------------------------------
IMAGE_MAP = {
    "squat": "images/squat.jpg",
    "pushup": "images/pushup.jpg",
    "bridge": "images/bridge.jpg",
    "lunge": "images/lunge.jpg",
    "deadbug": "images/deadbug.jpg",
    "row": "images/row.jpg",
    "rdl": "images/rdl.jpg",
    "dip": "images/dip.jpg",
    "deadlift": "images/deadlift.jpg",
    "highknees": "images/highknees.jpg",
    "burpee": "images/burpee.jpg",
    "mountainclimber": "images/mountainclimber.jpg",
    "jump_squat": "images/jump_squat.jpg",
    "plankjack": "images/plankjack.jpg",
    "tuckjump": "images/tuckjump.jpg",
    "skater": "images/skater.jpg",
    "sprint": "images/sprint.jpg",
    "neckroll": "images/neckroll.jpg",
    "shouldercircle": "images/shouldercircle.jpg",
    "hamstring": "images/hamstring.jpg",
    "childpose": "images/childpose.jpg",
    "catcow": "images/catcow.jpg",
    "forwardfold": "images/forwardfold.jpg",
    "hipflexor": "images/hipflexor.jpg",
    "pigeon": "images/pigeon.jpg",
    "bridge_mobility": "images/bridge_mobility.jpg",
    "spinaltwist": "images/spinaltwist.jpg",
    "frogpose": "images/frogpose.jpg",
    "pancake": "images/pancake.jpg",
    "quadstretch": "images/quadstretch.jpg",
    "boxjump": "images/boxjump.jpg"
}

# ---------------------------------------------------------
# ROUTINE POOL (WITH IMAGES)
# ---------------------------------------------------------
ROUTINE_POOL = {
    "strength": {
        "Beginner": [
            [
                ("Bodyweight squats – 3×8", IMAGE_MAP["squat"]),
                ("Wall push‑ups – 3×8", IMAGE_MAP["pushup"]),
                ("Glute bridges – 3×10", IMAGE_MAP["bridge"])
            ],
            [
                ("Step‑back lunges – 3×6 each leg", IMAGE_MAP["lunge"]),
                ("Incline push‑ups – 3×8", IMAGE_MAP["pushup"]),
                ("Dead bugs – 3×10", IMAGE_MAP["deadbug"])
            ]
        ],
        "Intermediate": [
            [
                ("Squats – 3×10", IMAGE_MAP["squat"]),
                ("Push‑ups – 3×8", IMAGE_MAP["pushup"]),
                ("Dumbbell rows – 3×10", IMAGE_MAP["row"])
            ],
            [
                ("Lunges – 3×10", IMAGE_MAP["lunge"]),
                ("Bench press or push‑ups – 3×10", IMAGE_MAP["pushup"]),
                ("Romanian deadlifts – 3×10", IMAGE_MAP["rdl"])
            ]
        ],
        "Advanced": [
            [
                ("Weighted squats – 4×8", IMAGE_MAP["squat"]),
                ("Dips – 4×10", IMAGE_MAP["dip"]),
                ("Deadlifts – 4×8", IMAGE_MAP["deadlift"])
            ],
            [
                ("Front squats – 4×6", IMAGE_MAP["squat"]),
                ("Weighted dips – 4×8", IMAGE_MAP["dip"]),
                ("Barbell rows – 4×8", IMAGE_MAP["row"])
            ]
        ]
    },

    "hiit": {
        "Beginner": [
            [
                ("20 sec work → 40 sec rest", IMAGE_MAP["highknees"]),
                ("Marching / step jacks / knee lifts", IMAGE_MAP["highknees"]),
                ("3 rounds", IMAGE_MAP["highknees"])
            ],
            [
                ("15 sec work → 45 sec rest", IMAGE_MAP["burpee"]),
                ("Slow burpees / step‑back lunges", IMAGE_MAP["lunge"]),
                ("3 rounds", IMAGE_MAP["burpee"])
            ]
        ],
        "Intermediate": [
            [
                ("30 sec work → 30 sec rest", IMAGE_MAP["burpee"]),
                ("Burpees / mountain climbers / jump squats", IMAGE_MAP["mountainclimber"]),
                ("4 rounds", IMAGE_MAP["jump_squat"])
            ],
            [
                ("40 sec work → 20 sec rest", IMAGE_MAP["highknees"]),
                ("High knees / plank jacks / squat jumps", IMAGE_MAP["plankjack"]),
                ("4 rounds", IMAGE_MAP["jump_squat"])
            ]
        ],
        "Advanced": [
            [
                ("40 sec work → 20 sec rest", IMAGE_MAP["sprint"]),
                ("Sprints / burpees / tuck jumps", IMAGE_MAP["tuckjump"]),
                ("5–6 rounds", IMAGE_MAP["burpee"])
            ],
            [
                ("45 sec work → 15 sec rest", IMAGE_MAP["jump_squat"]),
                ("Box jumps / explosive push‑ups / skater jumps", IMAGE_MAP["boxjump"]),
                ("6 rounds", IMAGE_MAP["skater"])
            ]
        ]
    },

    "stretch": {
        "Beginner": [
            [
                ("Neck rolls – 30 sec", IMAGE_MAP["neckroll"]),
                ("Shoulder circles – 1 min", IMAGE_MAP["shouldercircle"]),
                ("Hamstring stretch – 1 min", IMAGE_MAP["hamstring"]),
                ("Child’s pose – 1 min", IMAGE_MAP["childpose"])
            ],
            [
                ("Cat‑cow – 1 min", IMAGE_MAP["catcow"]),
                ("Seated forward fold – 1 min", IMAGE_MAP["forwardfold"]),
                ("Hip opener stretch – 1 min", IMAGE_MAP["hipflexor"]),
                ("Deep breathing – 1 min", IMAGE_MAP["childpose"])
            ]
        ],
        "Intermediate": [
            [
                ("Cat‑cow – 1 min", IMAGE_MAP["catcow"]),
                ("Hip flexor stretch – 2 min", IMAGE_MAP["hipflexor"]),
                ("Thoracic rotations – 2 min", IMAGE_MAP["spinaltwist"]),
                ("Forward fold – 1 min", IMAGE_MAP["forwardfold"])
            ],
            [
                ("Pigeon pose – 2 min", IMAGE_MAP["pigeon"]),
                ("Bridge mobility – 2 min", IMAGE_MAP["bridge_mobility"]),
                ("Hamstring stretch – 2 min", IMAGE_MAP["hamstring"]),
                ("Spinal twist – 1 min", IMAGE_MAP["spinaltwist"])
            ]
        ],
        "Advanced": [
            [
                ("Deep lunge stretch – 2 min", IMAGE_MAP["hipflexor"]),
                ("Pigeon pose – 2 min", IMAGE_MAP["pigeon"]),
                ("Bridge mobility – 2 min", IMAGE_MAP["bridge_mobility"]),
                ("Deep hamstring stretch – 2 min", IMAGE_MAP["hamstring"])
            ],
            [
                ("Pancake stretch – 2 min", IMAGE_MAP["pancake"]),
                ("Frog pose – 2 min", IMAGE_MAP["frogpose"]),
                ("Backbend prep – 2 min", IMAGE_MAP["bridge_mobility"]),
                ("Deep quad stretch – 2 min", IMAGE_MAP["quadstretch"])
            ]
        ]
    }
}

# ---------------------------------------------------------
# SCORING ENGINE
# ---------------------------------------------------------
def score_workout(mood, time, goal, location, level):
    scores = {
        "stretch": 0,
        "light_cardio": 0,
        "moderate_cardio": 0,
        "hiit": 0,
        "strength": 0,
    }

    # Mood scoring
    if mood == "Tired":
        scores["stretch"] += 3
        scores["light_cardio"] += 1
    elif mood == "Normal":
        scores["moderate_cardio"] += 2
        scores["strength"] += 1
    elif mood == "Energized":
        scores["hiit"] += 3
        scores["strength"] += 2
        scores["moderate_cardio"] += 1

    # Time scoring
    if time == "< 20 minutes":
        scores["stretch"] += 1
        scores["light_cardio"] += 1
        scores["hiit"] += 2
    elif time == "20–40 minutes":
        scores["moderate_cardio"] += 2
        scores["strength"] += 2
        scores["hiit"] += 1
    elif time == "> 40 minutes":
        scores["moderate_cardio"] += 2
        scores["strength"] += 3

    # Goal scoring
    if goal == "Relax / De-stress":
        scores["stretch"] += 4
        scores["light_cardio"] += 1
    elif goal == "General Fitness":
        scores["moderate_cardio"] += 3
        scores["light_cardio"] += 1
    elif goal == "Build Strength":
        scores["strength"] += 4
        scores["moderate_cardio"] += 1
    elif goal == "High Intensity / Sweat":
        scores["hiit"] += 4
        scores["moderate_cardio"] += 2

    # Location scoring
    if location == "Home (no equipment)":
        scores["stretch"] += 2
        scores["light_cardio"] += 2
        scores["hiit"] += 1
    elif location == "Home (some equipment)":
        scores["strength"] += 2
        scores["moderate_cardio"] += 1
    elif location == "Gym":
        scores["strength"] += 3
        scores["moderate_cardio"] += 2
        scores["hiit"] += 1

    # Level scoring
    if level == "Beginner":
        scores["stretch"] += 2
        scores["light_cardio"] += 2
    elif level == "Intermediate":
        scores["moderate_cardio"] += 2
        scores["strength"] += 1
    elif level == "Advanced":
        scores["hiit"] += 3
        scores["strength"] += 2

    return scores

# ---------------------------------------------------------
# RECOMMENDATION LOGIC
# ---------------------------------------------------------
def workout_recommendation(scores):
    best_type = max(scores, key=scores.get)

    descriptions = {
        "stretch": "A gentle stretching or mobility session is ideal for recovery, relaxation, and reducing tension.",
        "light_cardio": "Light cardio helps you move without overexertion. Great for low‑energy days.",
        "moderate_cardio": "A steady‑state cardio session will give you a solid fitness boost without being too intense.",
        "hiit": "You’re ready for intensity. HIIT will give you maximum results in minimum time.",
        "strength": "Strength training is the best match today. Focus on compound movements for maximum benefit."
    }

    return best_type, descriptions.get(best_type, "A balanced workout is recommended.")

# ---------------------------------------------------------
# RANDOMIZED ROUTINE GENERATOR
# ---------------------------------------------------------
def generate_sample_routine(workout_type, level):
    return random.choice(ROUTINE_POOL.get(workout_type, {}).get(level, []))

# ---------------------------------------------------------
# STREAMLIT UI
# ---------------------------------------------------------
st.set_page_config(page_title="Workout Recommender", page_icon="💪", layout="centered")
st.title("💪 Personalized Workout Recommender")
st.caption("Rule‑based AI logic that adapts to your mood, time, goals, location, and fitness level.")

st.markdown("### Tell me about your day")

mood = st.selectbox("How do you feel right now?", MOOD_OPTIONS)
time = st.selectbox("How much time do you have?", TIME_OPTIONS)
goal = st.selectbox("What’s your main goal for this session?", GOAL_OPTIONS)
location = st.selectbox("Where will you work out?", LOCATION_OPTIONS)
level = st.selectbox("What is your fitness level?", LEVEL_OPTIONS)

# Initialize session state
if "scores" not in st.session_state:
    st.session_state.scores = None
if "best_type" not in st.session_state:
    st.session_state.best_type = None
if "description" not in st.session_state:
    st.session_state.description = None

# First button: generate recommendation
if st.button("Get My Workout Recommendation"):
    st.session_state.scores = score_workout(mood, time, goal, location, level)
    best_type, desc = workout_recommendation(st.session_state.scores)
    st.session_state.best_type = best_type
    st.session_state.description = desc

# If a recommendation exists, show it
if st.session_state.scores is not None and st.session_state.best_type is not None:
    st.markdown("---")
    st.subheader(f"Recommended Workout: **{st.session_state.best_type.replace('_', ' ').title()}**")
    st.write(st.session_state.description)

    with st.expander("See how this was decided"):
        st.json(st.session_state.scores)

    # Second button: randomized routine
    if st.button("Generate Randomized Routine"):
        routine = generate_sample_routine(st.session_state.best_type, level)
        st.markdown(f"### 🎲 Randomized {level} Routine")

        for step, img in routine:
            st.write(f"**{step}**")
            st.image(img, width=250)
