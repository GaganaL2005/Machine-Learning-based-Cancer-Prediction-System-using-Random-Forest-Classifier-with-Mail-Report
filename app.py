from flask import Flask, request, render_template
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
from twilio.rest import Client
from mailersend import MailerSendClient, EmailBuilder
import os

ms = MailerSendClient(api_key="")


# -------------------------------------------------
# Flask App Initialization
# -------------------------------------------------
app = Flask(__name__)

# -------------------------------------------------
# Load Dataset
# -------------------------------------------------
df = pd.read_csv('cancer.csv')

selected_features = [
    'Air Pollution',
    'Genetic Risk',
    'Obesity',
    'Balanced Diet',
    'OccuPational Hazards',
    'Coughing of Blood'
]

X = df[selected_features]
y = df['Level']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

rf_clf = RandomForestClassifier(n_estimators=100, random_state=42)
rf_clf.fit(X_train, y_train)

y_pred = rf_clf.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)

print("Accuracy:", accuracy * 100)
print("Confusion Matrix:\n", conf_matrix)


# -------------------------------------------------
# Routes
# -------------------------------------------------
@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():

    air_pollution = float(request.form['Air Pollution'])
    genetic_risk = float(request.form['Genetic Risk'])
    obesity = float(request.form['Obesity'])
    balanced_diet = float(request.form['Balanced Diet'])
    occupational_hazards = float(request.form['Occupational Hazards'])
    coughing_of_blood = float(request.form['coughing_of_blood'])
    PatientName = str(request.form['Patient_Name'])

    input_data = [[
        air_pollution,
        genetic_risk,
        obesity,
        balanced_diet,
        occupational_hazards,
        coughing_of_blood
    ]]

    prediction = rf_clf.predict(input_data)
    prediction_proba = rf_clf.predict_proba(input_data)

    predicted_class = prediction[0]
    predicted_prob = max(prediction_proba[0]) * 100

    # -------------------------------------------------
    # Create Health Report
    # -------------------------------------------------
    report_text = f"""
        Cancer Risk Assessment Report
        
        Hi! {PatientName}, Below is your Health Report.

        Risk Level: {predicted_class}
        Confidence: {predicted_prob:.2f}%

        Input Details:
        Air Pollution: {air_pollution}
        Genetic Risk: {genetic_risk}
        Obesity: {obesity}
        Balanced Diet: {balanced_diet}
        Occupational Hazards: {occupational_hazards}
        Coughing of Blood: {coughing_of_blood}

        This is an AI-based prediction.
        Consult a medical professional for confirmation.
    """

    
    # -------------------------------------------------
    # Send Email (MailerSend)
    # -------------------------------------------------
    email =(
      EmailBuilder()
        .from_email("info@", "Cancer Risk System")
        .to_many([{"email":"@gmail.com", "name": "Recipient"}])
        .subject("Cancer Risk Assessment Report")
        .html(f"<pre>{report_text}</pre>")
        .text(report_text)
        .build()
    )

    ms.emails.send(email)

    print("Email sent successfully")

    result = {
        'predicted_class': predicted_class,
        'predicted_probability': dict(zip(rf_clf.classes_, prediction_proba[0]))
    }

    return render_template('index.html', result=result)


# -------------------------------------------------
# Run App
# -------------------------------------------------
if __name__ == '__main__':
    app.run(debug=True)
    