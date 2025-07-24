import joblib
import os
import numpy as np

# Load model once
model_path = os.path.join(os.path.dirname(__file__), "../ml_models/model.pkl")
model = joblib.load(model_path)

# Label decoder (ensure order matches training)
label_map = {0: "High", 1: "Low", 2: "Moderate"}  # may vary by encoding

def predict_risk(input_df):
    try:
        prediction = model.predict(input_df)[0]
        return label_map.get(prediction, "Unknown")
    except Exception as e:
        return f"Prediction error: {e}"
