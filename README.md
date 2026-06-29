# 📊 Student Score Prediction using Linear Regression

## 🚀 Project Overview
This project predicts a student's exam score based on hours studied using Linear Regression.

---

## 📁 Dataset
| Hours | Score |
|------:|------:|
| 1.0   | 20    |
| 2.0   | 28    |
| 3.0   | 40    |
| 4.0   | 50    |
| 5.0   | 60    |

---

## 🧠 Model
Score = m × Hours + c

---

## ▶️ Code (main.py)

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

data = {
    "Hours": [1, 2, 3, 4, 5],
    "Score": [20, 28, 40, 50, 60]
}

df = pd.DataFrame(data)

X = df[["Hours"]]
y = df["Score"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

hours = 6.5
pred = model.predict([[hours]])

print("Predicted score:", pred[0])

plt.scatter(X, y)
plt.plot(X, model.predict(X))
plt.show()
```

---

## 🔮 Output
Predicted score for 6.5 hours ≈ 71.23

---

## 🛠 Tools
Python, Pandas, NumPy, Matplotlib, Scikit-learn

---

## 👨‍💻 Author
Martin Uzoma
