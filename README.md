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

---

## ✅ Setup Instructions

### 1. Clone the Repository
git clone https://github.com/YOUR_USERNAME/HealthMate.git
cd HealthMate

2. Create Virtual Environment (Optional but Recommended)
python -m venv venv
venv\Scripts\activate  # On Windows

3. Install Dependencies
pip install -r requirements.txt

4. Run the App
streamlit run app/main.py
🧠 Model Info
The machine learning model is a simple Decision Tree Classifier trained on synthetic health data.

📄 Sample Output
The app generates a health report PDF with inputs and risk level.

📧 Optional: Enable Email Feature
To enable email, configure SMTP in utils/email_service.py.

📃 License
MIT License – feel free to use and adapt!
