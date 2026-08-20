# Student Performance Prediction System

Predicts whether a student is likely to pass or fail using
attendance, daily study hours and previous examination marks.

## Problem
Students at risk of failing are usually identified only after
the final exam. This system flags them beforehand so that
teachers can intervene in time.

## Dataset
200 records, 4 columns (Attendance, Study_Hours,
Previous_Marks, Result). 128 Pass, 72 Fail. Generated with
a rule plus random noise; no missing values.

## Model
Logistic Regression (scikit-learn), 80/20 train-test split.

## Results
Accuracy         : 90%
Recall (Fail)    : 0.79  (caught 11 of 14 at-risk students)
Recall (Pass)    : 0.96

## Tech stack
Python, pandas, scikit-learn, joblib, Streamlit

## How to run
pip install -r requirements.txt
python dataset/make_dataset.py
python model/train_model.py
streamlit run app.py

## Limitations
The dataset is synthetic, so accuracy is higher than it would
be on real college data. Only three features are used; real
outcomes depend on many more.
