import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Month':['Jan','Feb','Mar','Apr','May','Jun'],
    'Sales':[12000,15000,18000,17000,21000,25000]
}

df = pd.DataFrame(data)

plt.plot(df['Month'], df['Sales'], marker='o')
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()

print("Total Sales:", df['Sales'].sum())