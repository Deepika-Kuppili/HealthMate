import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import joblib
import os

# Generate dummy health data
data = pd.DataFrame({
    "age": [25, 35, 45, 60, 30, 55, 40, 50],
    "bp": [120, 140, 160, 180, 110, 150, 135, 145],
    "glucose": [90, 100, 130, 200, 85, 160, 120, 140],
    "steps": [5000, 3000, 2000, 1000, 7000, 1500, 4000, 2500],
    "sleep": [7.0, 6.0, 5.0, 4.0, 8.0, 4.5, 6.5, 5.5],
    "risk": ["Low", "Moderate", "High", "High", "Low", "High", "Moderate", "Moderate"]
})

X = data[["age", "bp", "glucose", "steps", "sleep"]]
y = LabelEncoder().fit_transform(data["risk"])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save model
os.makedirs("ml_models", exist_ok=True)
joblib.dump(model, "ml_models/model.pkl")
