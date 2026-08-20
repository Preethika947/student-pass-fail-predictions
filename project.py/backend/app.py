"""
backend/app.py
--------------
Flask backend for the Student Performance Prediction System.

Folder structure:
  backend/
    app.py               ← this file
    model/
      student_model.pkl  ← trained ML model
      train_model.py     ← model training script
    dataset/             ← raw data files
    requirements.txt

  frontend/
    templates/           ← Jinja2 HTML templates (index.html, result.html)
    static/
      css/style.css      ← shared stylesheet
      js/main.js         ← shared JS

Run:
  cd backend
  python app.py
"""

import os
from flask import Flask, request, render_template
import pandas as pd
import joblib

# ── Point Flask at the frontend folders ──────────────────────────────────────
# Go one level up from backend/ to reach the project root, then into frontend/
BASE_DIR      = os.path.dirname(os.path.abspath(__file__))   # .../project.py/backend
FRONTEND_DIR  = os.path.join(BASE_DIR, '..', 'frontend')     # .../project.py/frontend

app = Flask(
    __name__,
    template_folder=os.path.join(FRONTEND_DIR, 'templates'),  # frontend/templates/
    static_folder  =os.path.join(FRONTEND_DIR, 'static'),     # frontend/static/
)

# ── Load the trained ML model ────────────────────────────────────────────────
MODEL_PATH = os.path.join(BASE_DIR, 'model', 'student_model.pkl')
model = joblib.load(MODEL_PATH)


# ── Routes ───────────────────────────────────────────────────────────────────

@app.route('/')
def home():
    """Render the prediction form (index.html)."""
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    """
    Accept form data, run the ML model, and render the result page.

    Form fields:
        attendance      (float, 0–100)
        study_hours     (float, 0–24)
        previous_marks  (float, 0–100)
    """
    try:
        attendance     = float(request.form['attendance'])
        study_hours    = float(request.form['study_hours'])
        previous_marks = float(request.form['previous_marks'])

        # Build a DataFrame matching the training feature columns
        data = pd.DataFrame(
            [[attendance, study_hours, previous_marks]],
            columns=["Attendance", "Study_Hours", "Previous_Marks"]
        )

        prediction_val = model.predict(data)[0]                        # 0 = Fail, 1 = Pass
        result_text    = "PASS" if prediction_val == 1 else "FAIL"

        return render_template(
            'result.html',
          result=result_text,
        )

    except Exception as e:
        return f"<h2>Error processing request</h2><pre>{e}</pre>", 400


# ── Entry point ───────────────────────────────────────────────────────────────

if __name__ == '__main__':
    app.run(debug=True)
