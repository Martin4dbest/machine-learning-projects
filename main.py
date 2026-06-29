"""
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Load dataset
data = pd.read_csv("datasets/student_scores.csv")

# Feature
X = data[["Hours"]]

# Target
y = data["Score"]

# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Create the model
model = LinearRegression()

# Train the model
model.fit(X_train, y_train)

# Predict test data
y_pred = model.predict(X_test)


new_student = pd.DataFrame({
    "Hours": [7.5]
})

prediction = model.predict(new_student)

print("Predicted Score:", prediction[0])

"""


# ============================
# TRAIN A MODEL TO PREDICT STUDENT SCORES
# ============================

import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Load the dataset
data = pd.read_csv("datasets/student_scores.csv")

# Feature (Input)
X = data[["Hours"]]

# Target (Output)
y = data["Score"]

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Display the training and testing data
print("\n========== TRAINING DATA ==========")
print(X_train)

print("\n========== TESTING DATA ==========")
print(X_test)

# Create the Linear Regression model
model = LinearRegression()

# Train the model
model.fit(X_train, y_train)

# Display the equation of the line
print("\n========== MODEL DETAILS ==========")
print("Slope (Coefficient):", model.coef_[0])
print("Intercept:", model.intercept_)

# Predict the test data
y_pred = model.predict(X_test)

print("\n========== TEST PREDICTIONS ==========")
for actual_hours, actual_score, predicted_score in zip(
    X_test["Hours"],
    y_test,
    y_pred
):
    print(
        f"Hours: {actual_hours} | "
        f"Actual Score: {actual_score} | "
        f"Predicted Score: {predicted_score:.2f}"
    )

# Predict a new student's score
new_guy = pd.DataFrame({
    "Hours": [6.5]
})

prediction = model.predict(new_guy)

print("\n========== NEW STUDENT ==========")
print("Hours Studied:", new_guy["Hours"][0])
print("Predicted Score:", prediction[0])