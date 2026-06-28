import pandas as pd 

data = pd.read_csv("datasets/student_scores.csv")

#print(data)
#print(data.head())
#print(data.tail())
#print(data.shape)
#print(data.columns)

#data.info()
print(data.describe())


import pandas as pd

data = pd.read_csv("datasets/student_scores.csv")

print(data)
print(data.head())
print(data.tail())
print(data.shape)
print(data.columns)

data.info()
print(data.describe())