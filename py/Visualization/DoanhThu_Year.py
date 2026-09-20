import matplotlib.pyplot as plt

import pandas as pd
df = pd.read_csv(r"D:\Retail_Sales\kaggle\query_sql\Revenue_Year.csv")

plt.plot(df["year"], df["total_revenue"],marker = "o", color = "red")

plt.xticks(df["year"])
plt.show()