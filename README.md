# 🩺 HealthMate – Personal Health Tracker

HealthMate is a simple and user-friendly Streamlit application that predicts your health risk level (Low, Moderate, High) based on daily health metrics like age, blood pressure, glucose level, steps, and sleep. It also generates a downloadable PDF health report.

---

## 🚀 Features

- 🔢 Input health data (age, BP, glucose, steps, sleep)
- 🤖 Predict health risk using a trained ML model
- 📄 Download a PDF health report with your data and risk level
- ✉️ [Optional] Email the report (if email feature is enabled)

---

## 🛠️ Tech Stack

- Python 3.11+
- Streamlit
- Scikit-learn
- Pandas
- fpdf
- joblib

---

## 📦 Project Structure
HealthMate/
├── app/
│ └── main.py # Streamlit application
├── ml_models/
│ └── model.pkl # Trained ML model
├── utils/
│ ├── predict.py # ML prediction logic
│ ├── report_generator.py # PDF report creation
│ └── email_service.py # (Optional) email functionality
├── .gitignore
├── requirements.txt
└── README.md

