from flask import Flask, render_template, request
import pickle
import numpy as np


# Initialize Flask app
app = Flask(__name__)

# Load the pre-trained model using pickle
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

# Home route with a form
@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    if request.method == "POST":
        # Retrieve form data
        daily_time_spent = float(request.form["daily_time_spent"])
        age = int(request.form["age"])
        area_income = float(request.form["area_income"])
        daily_internet_usage = float(request.form["daily_internet_usage"])
        male = int(request.form["male"])

        # Prepare the data for the model
        input_data = np.array([[daily_time_spent, age, area_income, daily_internet_usage, male]])

        # Make a prediction
        prediction = model.predict(input_data)[0]
        prediction = "Clicked on Ad" if prediction == 1 else "Did not Click on Ad"

    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)
