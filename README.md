# 🩺 Cancer Risk Prediction Web Application

## 📌 Project Overview

This project is a **Flask-based Machine Learning Web Application** that predicts a patient’s cancer risk level based on selected health and environmental factors.

It uses the **Random Forest Classification Algorithm** to analyze input data and generate a risk assessment report. The system also sends the prediction report via email automatically.

> ⚠️ Note: This system is for educational and research purposes only. It does not replace professional medical diagnosis.

---

## 🚀 Technologies Used

- **Python**
- **Flask** (Web Framework)
- **Pandas** (Data Handling)
- **Scikit-learn** (Machine Learning)
- **Random Forest Classifier**
- **MailerSend API** (Email Service)
- **HTML (Frontend Template)**

---

## 📂 Dataset

The application uses a dataset named:

```
cancer.csv
```

### Selected Features Used for Prediction:

- Air Pollution  
- Genetic Risk  
- Obesity  
- Balanced Diet  
- Occupational Hazards  
- Coughing of Blood  

### Target Variable:

- **Level** (Cancer Risk Level)

---

## 🧠 Machine Learning Model

### Algorithm Used:
**Random Forest Classifier**

### Why Random Forest?

- Handles multiple input features effectively  
- Reduces overfitting  
- Provides better accuracy  
- Works well for classification problems  

### Model Training Process:

1. Load dataset using Pandas  
2. Select important features  
3. Split dataset into:
   - 70% Training Data  
   - 30% Testing Data  
4. Train model using:

```python
RandomForestClassifier(n_estimators=100, random_state=42)
```

5. Evaluate model using:
   - Accuracy Score  
   - Confusion Matrix  

---

## 🌐 Application Workflow

### Step 1: User Input

The user enters:

- Patient Name  
- Air Pollution Level  
- Genetic Risk  
- Obesity Level  
- Balanced Diet Score  
- Occupational Hazards  
- Coughing of Blood  

### Step 2: Prediction

- Input data is converted into model format.  
- The trained Random Forest model predicts:
  - Cancer Risk Level  
  - Prediction Confidence (%)  

### Step 3: Report Generation

The system generates a detailed **Cancer Risk Assessment Report** including:

- Patient Name  
- Risk Level  
- Confidence Percentage  
- Entered Health Details  
- Medical Disclaimer  

### Step 4: Email Notification

Using **MailerSend API**, the report is:

- Converted into text format  
- Sent to the configured email address  
- Delivered as both HTML and plain text  

---

## 📊 Model Evaluation

The system evaluates performance using:

- Accuracy Score  
- Confusion Matrix  

These metrics help measure how well the model performs on unseen test data.

---

## 📁 Project Structure

```
project-folder/
│
├── cancer.csv
├── app.py
├── templates/
│   └── index.html
└── README.md
```

---

## ▶️ How to Run the Project

### 1️⃣ Install Required Packages

```bash
pip install flask pandas scikit-learn mailersend
```

### 2️⃣ Add Your MailerSend API Key

Inside the code:

```python
ms = MailerSendClient(api_key="YOUR_API_KEY")
```

### 3️⃣ Run the Application

```bash
python app.py
```

### 4️⃣ Open in Browser

```
http://127.0.0.1:5000/
```

---

## 🔐 Important Notes

- This is an AI-based prediction system.  
- It should not be used for real medical decisions.  
- Always consult a medical professional for diagnosis and treatment.  
- API keys should not be exposed publicly.  

---

## 🎯 Key Features

✔️ Machine Learning-based Risk Prediction  
✔️ Real-time Web Interface  
✔️ Automatic Email Report Generation  
✔️ Probability Confidence Score  
✔️ Clean and Simple User Interface  

---

## 📌 Future Improvements

- Add data visualization charts  
- Improve model accuracy with feature engineering  
- Deploy on cloud (AWS / Render / Heroku)  
- Add user authentication  
- Store prediction history in database  
