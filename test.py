import pandas as pd

import matplotlib.pyplot as plt

data = pd.read_csv("datasets/test_data.csv")

data.info()

print(data)

plt.figure(figsize=(8, 5))
plt.scatter(data["Hours"], data["Score"])
plt.title("Graph of Hours studied Vs Exam Scores")
plt.xlabel("Hours studied")
plt.ylabel("Exam student")

plt.grid(True)
plt.show()




"""
print(data)
print(data.head())
print(data.tail())
print(data.shape)
print(data.columns)

data.info()
print(data.describe())

plt.figure(figsize=(8,5))
plt.scatter(data["Hours"], data["Score"])
plt.title("Hours studied Vs Exam Score")

plt.xlabel("Hours studied")
plt.ylabel("Exam score")

plt.grid(True)
plt.show()
"""
