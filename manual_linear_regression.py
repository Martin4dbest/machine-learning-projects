import pandas as pd

#Load dataset
data = pd.read_csv("datasets/student_scores.csv")

#Extract the Columns
hours = data["Hours"]
scores = data["Score"]

#Calculate the means
mean_hours = hours.mean()
mean_scores = scores.mean()

print("Mean Hours :", mean_hours)
print("Mean Scores :", mean_scores)

#Calculate the numerator
numerator = 0
for x, y in zip(hours, scores):
    numerator += (x - mean_hours) * (y - mean_scores)

#calculate the denominator
denominator = 0

for x in hours:
    denominator += (x - mean_hours) ** 2

#Calculate the slope
m = numerator / denominator

#calculate the intercept
b = mean_scores - (m * mean_hours)

print("\nSlope (m):", round(m, 4))
print("Intercept (b):", round(b, 4))

#Predict score
hours_studied = 7.5

predicted_score = (m *hours_studied) + b

print(f"\nPredicted Score for {hours_studied} hours: {predicted_score:.2f}")