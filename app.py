import streamlit as st

from sports import SportService
from diseases import Diseases
from nutrition import nutrition
from Clinic import Clinic

st.set_page_config(page_title="Al-Shifa Hospital", page_icon="🏥", layout="wide")

# here we change the colors so it looks like a hospital app
st.markdown("""
<style>
.stApp { background: #f3f8f8; }
[data-testid="stSidebar"] { background: #0f4c5c; }
[data-testid="stSidebar"] * { color: #ffffff !important; }
[data-testid="stSidebar"] input, [data-testid="stSidebar"] [data-baseweb="select"] * { color: #0f4c5c !important; }

.banner {
    background: linear-gradient(120deg, #0f4c5c, #2a9d8f);
    color: white; padding: 26px 32px; border-radius: 18px; margin-bottom: 22px;
}
.banner h1 { color: white; margin: 0; font-size: 2.1rem; }
.banner p { margin: 4px 0 0; opacity: .85; }

.card {
    background: white; border-radius: 16px; padding: 20px;
    border-top: 5px solid #2a9d8f; box-shadow: 0 2px 10px rgba(0,0,0,.06);
    height: 100%;
}
.card h3 { margin-top: 0; color: #0f4c5c; }
.card p { color: #555; margin-bottom: 0; }

.ticket {
    background: white; border: 2px dashed #2a9d8f; border-radius: 16px; padding: 22px;
}
.ticket .row { display: flex; justify-content: space-between; padding: 6px 0; border-bottom: 1px solid #eef3f3; }
.ticket .row span:first-child { color: #777; }
.ticket .row span:last-child { font-weight: 600; color: #0f4c5c; }

.tag { display: inline-block; padding: 3px 12px; border-radius: 20px; font-weight: 600; color: white; }
.Urgent { background: #e63946; }
.Soon { background: #f4a261; }
.Routine { background: #2a9d8f; }

div.stButton > button {
    background: #2a9d8f; color: white; border: none; border-radius: 10px; padding: 8px 22px;
}
div.stButton > button:hover { background: #0f4c5c; color: white; }
</style>
""", unsafe_allow_html=True)


def banner(title, text): # the green box on top of every page
    st.markdown('<div class="banner"><h1>' + title + '</h1><p>' + text + '</p></div>', unsafe_allow_html=True)


def card(title, text): # white box with a title and small text
    st.markdown('<div class="card"><h3>' + title + '</h3><p>' + text + '</p></div>', unsafe_allow_html=True)


# sidebar menu
st.sidebar.markdown("## 🏥 Al-Shifa")
page = st.sidebar.radio("Go to", ["Home", "Diseases", "Nutrition", "Sports", "Clinic"])

# patient info in the sidebar so the user enters it one time for all pages
st.sidebar.markdown("---")
st.sidebar.markdown("### 🗂️ Patient file")
patient_id = st.sidebar.text_input("Patient ID", "P-1001")
name = st.sidebar.text_input("Name", "Guest")
age = st.sidebar.number_input("Age", 1, 120, 25)
gender = st.sidebar.selectbox("Gender", ["male", "female"])
weight = st.sidebar.number_input("Weight (kg)", 20.0, 250.0, 70.0)
height = st.sidebar.number_input("Height (cm)", 100.0, 230.0, 170.0)


if page == "Home": # home page
    banner("🏥 Al-Shifa Hospital", "Welcome " + name + ", how can we help you today?")

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        card("🦠 Diseases", "Answer a few questions about how you feel and get a quick assessment.")
    with col2:
        card("🥗 Nutrition", "Find your BMR, daily calories and a meal plan for your activity level.")
    with col3:
        card("🏃 Sports", "Check if you are ready for a run and get a recovery plan after it.")
    with col4:
        card("🩺 Clinic", "We send you to the right department and book your appointment.")

    st.write("")
    st.info("👈 Fill your patient file on the left first, then pick a section.")


elif page == "Diseases": # diseases page
    banner("🦠 Disease Assessment", "Tick what you are feeling right now")

    d = Diseases(patient_id, name, age, gender, {})
    d.display_questions() # the questions from the diseases class

    if st.button("Check"):
        d.display_info()


elif page == "Nutrition": # nutrition page
    banner("🥗 Nutrition", "Calories and meals based on how active you are")

    level_names = ["Low activity", "Lightly active", "Moderately active", "Very active", "Extra active"]
    level_name = st.select_slider("Activity level", options=level_names, value="Lightly active")
    activity_level = level_names.index(level_name) + 1 # the class needs a number from 1 to 5

    n = nutrition(name, age, gender, weight, height, activity_level)
    bmr, calories = n.calculate_calories()

    col1, col2 = st.columns(2)
    col1.metric("BMR", str(round(bmr)) + " kcal")
    col2.metric("Daily calories", str(round(calories)) + " kcal")

    meals = n.weight_loss_meals()
    st.subheader("🍽️ Weight loss meals (" + meals["level"].strip() + ")")
    st.text(meals["meals"])


elif page == "Sports": # sports page
    banner("🏃 Sports", "Are you ready for the run?")

    col1, col2 = st.columns(2)
    avg_sleep = col1.slider("Average sleep (hours)", 3.0, 12.0, 7.0, 0.5)
    activity = col2.selectbox("Activity (sedentary = 0 days, light = 1-2, moderate = 3-4, high = 5+)",
                              ["sedentary", "light", "moderate", "high"])

    s = SportService(name, age, height, weight, avg_sleep, activity)

    col1, col2 = st.columns(2)
    col1.metric("BMI", s.calc_bmi())
    col2.metric("Readiness", s.readiness_level())

    st.subheader("Your run")
    col1, col2 = st.columns(2)
    distance = col1.number_input("Distance (km)", 1.0, 50.0, 5.0)
    pace = col2.number_input("Pace (min per km)", 3.0, 15.0, 7.0)

    tips, fluids = s.recovery_plan(distance, pace)

    col1, col2 = st.columns(2)
    col1.metric("🔥 Calories burned", s.calories_burned(distance, pace))
    col2.metric("💧 Water to drink", str(fluids) + " L")

    st.subheader("Recovery plan")
    for tip in tips:
        st.write("-", tip)


elif page == "Clinic": # clinic page
    banner("🩺 Clinic", "Tell us your symptoms and we book you with the right doctor")

    # we save the patient in session_state because streamlit reruns the whole file on every click
    # and without it the queue number keeps going up
    if "clinic" not in st.session_state:
        st.session_state.clinic = Clinic(patient_id, name, age, gender, {}, False)
    c = st.session_state.clinic

    c.patient_id = patient_id # update the info if the user changes the sidebar
    c.name = name
    c.age = age
    c.gender = gender

    left, right = st.columns([3, 2])

    with left:
        c.display_questions() # this method comes from the diseases class
        c.has_insurance = st.checkbox("I have health insurance")

        department = c.pick_department()
        level = c.triage_level()
        st.markdown("**Department:** " + department + " &nbsp; | &nbsp; **Priority:** <span class='tag " + level + "'>" + level + "</span>",
                    unsafe_allow_html=True)

        col1, col2 = st.columns(2)
        day = col1.selectbox("Day", Clinic.work_days)
        time = col2.selectbox("Time", Clinic.time_slots)

        if st.button("Book appointment"):
            booked, message = c.book_appointment(day, time)
            if booked == True:
                st.success(message)
            else:
                st.error(message)

    with right:
        summary = c.visit_summary()

        if summary == None: # no booking yet
            card("🎫 No booking yet", "Your ticket will show here after you book.")
        else:
            rows = ""
            for key in summary: # make a row for every info in the ticket
                rows += '<div class="row"><span>' + key + '</span><span>' + str(summary[key]) + '</span></div>'
            st.markdown('<div class="ticket"><h3>🎫 Your ticket</h3>' + rows + '</div>', unsafe_allow_html=True)

            if st.button("New patient"): # start again with a new patient
                del st.session_state.clinic
                st.rerun()
