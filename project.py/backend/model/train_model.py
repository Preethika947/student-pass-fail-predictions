import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.metrics import classification_report

# ---- Step 4: Load and explore ----
df = pd.read_csv("dataset/student_performance.csv")

print("First 5 rows:")
print(df.head())
print("Shape (rows, columns):", df.shape)
print("Missing values:")
print(df.isnull().sum())
print("Statistics:")
print(df.describe())

# ---- Step 5: Prepare the data ----
df["Result"] = df["Result"].map({"Pass": 1, "Fail": 0})

X = df[["Attendance", "Study_Hours", "Previous_Marks"]]
y = df["Result"]

# ---- Step 6: Split 80 / 20 ----
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ---- Step 7: Train ----
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# ---- Step 8: Evaluate ----
y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))
print("Classification Report:")
print(classification_report(y_test, y_pred))

# ---- Step 11: Save the model ----
joblib.dump(model, "model/student_model.pkl")
print("Model saved to model/student_model.pkl")
