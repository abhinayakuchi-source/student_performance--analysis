import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Student':['A','B','C','D','E'],
    'Maths':[80,70,90,75,85]
}

df = pd.DataFrame(data)

plt.bar(df['Student'], df['Maths'])
plt.title("Student Marks")
plt.xlabel("Student")
plt.ylabel("Marks")
plt.show()