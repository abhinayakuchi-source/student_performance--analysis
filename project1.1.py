import pandas as pd

data = {
    'Student':['A','B','C','D','E'],
    'Marks':[80,70,90,75,85]
}

df = pd.DataFrame(data)

print(df)
print(df.describe())
print(df.isnull().sum())