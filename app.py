from flask import Flask, render_template, request

import numpy as np
import joblib
from src.utils.preprocessing import scale_features


app= Flask(__name__)

# Load model and scaler
model= joblib.load("src/model/artifacts/phishing_model.pkl")
scaler = joblib.load("src/data/artifacts/scaler.pkl")


@app.route("/", methods=["GET","POST"])
def home():
    if request.method == "POST":
        try:
            # Extract 49 features from form
            features = [float(request.form[f"feature{i}"]) for i in range(1, 50)]
            input_array = np.array([features])
            X_scaled, _ = scale_features(input_array, scaler)
            prediction = model.predict(X_scaled)[0]
            result = "Phishing 🚨" if prediction == 1 else "Legitimate ✅"
            return render_template("index.html", result=result)
        except Exception as e:
            return render_template("index.html", result=f"Error: {str(e)}")
    return render_template("index.html", result=None)


if __name__ == "__main__":
    app.run(debug= True)