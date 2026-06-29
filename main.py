# ==========================================================
# PROJECT 1: STUDENT SCORE PREDICTION
# Lesson 7 - Training and Evaluating a Linear Regression Model
# ==========================================================

# ==========================
# Import Libraries
# ==========================

import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

# ==========================
# Load Dataset
# ==========================

data = pd.read_csv("datasets/student_scores.csv")

print("\n========== DATASET ==========\n")
print(data)

# ==========================
# Display Basic Information
# ==========================

print("\n========== FIRST FIVE ROWS ==========\n")
print(data.head())

print("\n========== LAST FIVE ROWS ==========\n")
print(data.tail())

print("\n========== DATASET SHAPE ==========\n")
print(data.shape)

print("\n========== COLUMN NAMES ==========\n")
print(data.columns)

print("\n========== DATA INFORMATION ==========\n")
print(data.info())

print("\n========== STATISTICAL SUMMARY ==========\n")
print(data.describe())

# ==========================
# Features and Target
# ==========================

X = data[["Hours"]]

y = data["Score"]

print("\n========== FEATURES (X) ==========\n")
print(X)

print("\n========== TARGET (y) ==========\n")
print(y)

# ==========================
# Split Dataset
# ==========================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("\n========== DATA SPLIT ==========")
print("Training Samples :", len(X_train))
print("Testing Samples  :", len(X_test))

# ==========================
# Create Linear Regression Model
# ==========================

model = LinearRegression()

# ==========================
# Train Model
# ==========================

model.fit(X_train, y_train)

print("\nModel has been trained successfully!")

# ==========================
# Predictions on Test Data
# ==========================

y_pred = model.predict(X_test)

# ==========================
# Evaluate Model
# ==========================

mae = mean_absolute_error(y_test, y_pred)

mse = mean_squared_error(y_test, y_pred)

rmse = mse ** 0.5

r2 = r2_score(y_test, y_pred)

print("\n========== MODEL EVALUATION ==========\n")

print(f"Mean Absolute Error (MAE): {mae:.2f}")

print(f"Mean Squared Error (MSE): {mse:.2f}")

print(f"Root Mean Squared Error (RMSE): {rmse:.2f}")

print(f"R² Score: {r2:.4f}")

# ==========================
# Predict One New Student
# ==========================

new_student = pd.DataFrame({
    "Hours": [7.5]
})

prediction = model.predict(new_student)

print("\n========== SINGLE PREDICTION ==========\n")

print(f"A student who studied 7.5 hours is predicted to score {prediction[0]:.2f} marks.")

# ==========================
# Predict Multiple Students
# ==========================

students = pd.DataFrame({
    "Hours": [3, 5, 7, 9, 12]
})

predictions = model.predict(students)

print("\n========== MULTIPLE PREDICTIONS ==========\n")

for hour, score in zip(students["Hours"], predictions):
    print(f"{hour} Hours ---> {score:.2f} Marks")

# ==========================
# Visualize the Data
# ==========================

plt.figure(figsize=(8,5))

# Scatter Plot
plt.scatter(
    X,
    y,
    color="blue",
    label="Actual Data"
)

# Regression Line
plt.plot(
    X,
    model.predict(X),
    color="red",
    linewidth=2,
    label="Regression Line"
)

plt.title("Student Score Prediction")

plt.xlabel("Hours Studied")

plt.ylabel("Exam Score")

plt.legend()

plt.grid(True)

plt.show()