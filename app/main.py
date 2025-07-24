import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
import pandas as pd

from utils.predict import predict_risk
import utils.report_generator as report_generator
from utils.report_generator import generate_pdf
import utils.email_service as email_service
from utils.email_service import send_email

st.set_page_config(page_title="HealthMate", page_icon="🩺")

st.title("🩺 HealthMate – Personal Health Tracker")

st.markdown("Enter your daily health data to get your health risk prediction:")

# User Inputs
age = st.number_input("Age", min_value=1, max_value=120, value=25)
bp = st.number_input("Blood Pressure (systolic)", min_value=80, max_value=200, value=120)
glucose = st.number_input("Glucose Level", min_value=50, max_value=300, value=90)
steps = st.number_input("Daily Steps", min_value=0, max_value=30000, value=5000)
sleep = st.number_input("Hours of Sleep", min_value=0.0, max_value=24.0, value=7.0)

import os

# Session state setup
if "prediction_done" not in st.session_state:
    st.session_state["prediction_done"] = False

if st.button("🧠 Predict Health Risk"):
    input_data = pd.DataFrame([[age, bp, glucose, steps, sleep]],
                               columns=["age", "bp", "glucose", "steps", "sleep"])
    try:
        risk = predict_risk(input_data)
        st.session_state["risk"] = risk
        st.session_state["prediction_done"] = True
        st.success(f"Predicted Health Risk: {risk}")
    except Exception as e:
        st.error(f"Error during prediction: {e}")
        st.session_state["prediction_done"] = False

# Show report generation section only after prediction
if st.session_state["prediction_done"]:
    st.markdown("### Generate PDF Report")

    if st.button("Generate PDF"):
        try:
            report_path = "weekly_report.pdf"
            inputs = {
                    "Age": int(age),
                    "Blood Pressure": int(bp),
                    "Glucose Level": int(glucose),
                    "Daily Steps": int(steps),
                    "Hours of Sleep": float(sleep)
            }
            generate_pdf(report_path, st.session_state["risk"], inputs)

            if os.path.exists(report_path):
                with open(report_path, "rb") as file:
                    st.download_button("Download Report", file, file_name="HealthMate_Report.pdf")
            else:
                st.error("PDF was not generated.")
        except Exception as e:
            st.error(f"Error generating PDF: {e}")
