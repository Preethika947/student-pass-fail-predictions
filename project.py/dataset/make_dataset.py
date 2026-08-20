"""
Creates dataset/student_performance.csv

Run this once, before train_model.py:
    python dataset/make_dataset.py
"""

import numpy as np
import pandas as pd

rng = np.random.default_rng(42)

N = 10000

attendance = np.round(rng.uniform(35, 100, N), 0)
study_hours = np.round(rng.uniform(0.5, 6.0, N) * 2) / 2
previous_marks = np.round(rng.uniform(25, 95, N), 0)

# A hidden "true" rule, plus random noise so the data is not perfect
score = (
    0.40 * attendance
    + 0.30 * (study_hours * 16)
    + 0.30 * previous_marks
)
score = score + rng.normal(0, 6, N)

result = np.where(score >= 55, "Pass", "Fail")

df = pd.DataFrame({
    "Attendance": attendance.astype(int),
    "Study_Hours": study_hours,
    "Previous_Marks": previous_marks.astype(int),
    "Result": result,
})

df.to_csv("dataset/student_performance.csv", index=False)

print("Created dataset/student_performance.csv")
print("Rows:", len(df))
print(df["Result"].value_counts())
print(df.head())
