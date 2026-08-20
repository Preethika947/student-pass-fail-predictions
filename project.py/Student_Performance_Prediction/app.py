import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="Student Performance Prediction")


# Load the saved model once, not on every click
@st.cache_resource
def load_model():
    return joblib.load("model/student_model.pkl")


model = load_model()

st.title("Student Performance Prediction System")
st.write("Enter the student details to predict Pass or Fail.")

# ---- Input fields ----
attendance = st.number_input(
    "Attendance (%)",
    min_value=0.0, max_value=100.0, value=75.0, step=1.0
)

study_hours = st.number_input(
    "Study Hours per Day",
    min_value=0.0, max_value=24.0, value=3.0, step=0.5
)

previous_marks = st.number_input(
    "Previous Marks",
    min_value=0.0, max_value=100.0, value=60.0, step=1.0
)

# ---- Predict button ----
if st.button("Predict"):
    data = pd.DataFrame(
        [[attendance, study_hours, previous_marks]],
        columns=["Attendance", "Study_Hours", "Previous_Marks"]
    )

    prediction = model.predict(data)[0]
    confidence = model.predict_proba(data)[0][prediction]

    if prediction == 1:
        st.success("Prediction: PASS")
    else:
        st.error("Prediction: FAIL")

    st.caption("Confidence: %.1f%%" % (confidence * 100))
