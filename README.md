# AdClickPredictor-LogesticRegression

This project builds a **Logistic Regression model** to predict whether a user will click on an advertisement based on user attributes. It uses **Flask** for creating a web application and provides an intuitive front-end built with HTML and CSS.

---

## 📋 Project Overview

The application:
1. Trains a **Logistic Regression** model on a fake advertising dataset.
2. Saves the trained model as `model.pkl` using **pickle**.
3. Uses a **Flask server** to create a web application where users can input their details.
4. Predicts whether the user will **click on an ad** or not.

---

## ⚙️ Features

- Input fields for user details:
  - **Daily Time Spent on Site** (minutes)
  - **Age**
  - **Area Income**
  - **Daily Internet Usage** (minutes)
  - **Gender** (Male/Female)
- Real-time predictions:
  - "Clicked on Ad" or "Did not Click on Ad".
- A user-friendly **HTML/CSS frontend**.

---

## 🛠️ Technologies Used

- **Python** (Logistic Regression Model)
- **Flask** (Web Framework)
- **scikit-learn** (Model Training)
- **Pickle** (Model Serialization)
- **HTML/CSS** (Frontend)

---

├── app.py                # Flask backend code
├── train_model.py        # Script to train and save the model
├── model.pkl             # Pre-trained Logistic Regression model
├── templates/
│   └── index.html        # HTML frontend
├── static/
│   └── style.css         # Optional CSS file (if separate)
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation

