from flask import Flask, request, render_template
import pandas as pd
import joblib

app = Flask(__name__)

# Load the trained model
model = joblib.load('model/student_model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        attendance = float(request.form['attendance'])
        study_hours = float(request.form['study_hours'])
        previous_marks = float(request.form['previous_marks'])
        
        data = pd.DataFrame(
            [[attendance, study_hours, previous_marks]],
            columns=["Attendance", "Study_Hours", "Previous_Marks"]
        )
        
        prediction_val = model.predict(data)[0]
        result_text = "PASS" if prediction_val == 1 else "FAIL"
        
        return render_template('result.html', result=result_text)
    except Exception as e:
        return f"Error processing request: {e}"

if __name__ == "__main__":
    app.run(debug=True)
