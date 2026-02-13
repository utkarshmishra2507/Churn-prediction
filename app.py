from flask import Flask, render_template, request
import joblib
import pandas as pd
import json

app = Flask(__name__)

# Load model
model = joblib.load("model_v1.pkl")

with open("metadata_v1.json") as f:
    metadata = json.load(f)

threshold = metadata["threshold"]


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    data = {
        "CreditScore": int(request.form["CreditScore"]),
        "Geography": request.form["Geography"],
        "Gender": request.form["Gender"],
        "Age": int(request.form["Age"]),
        "Tenure": int(request.form["Tenure"]),
        "Balance": float(request.form["Balance"]),
        "NumOfProducts": int(request.form["NumOfProducts"]),
        "HasCrCard": int(request.form["HasCrCard"]),
        "IsActiveMember": int(request.form["IsActiveMember"]),
        "EstimatedSalary": float(request.form["EstimatedSalary"])
    }

    df = pd.DataFrame([data])

    prob = model.predict_proba(df)[0][1]
    prediction = "Churn" if prob >= threshold else "No Churn"

    return render_template(
        "index.html",
        prediction_text=f"Prediction: {prediction}",
        probability=f"Probability: {round(prob, 4)}"
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

