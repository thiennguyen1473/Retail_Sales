import matplotlib.pyplot as plt

import pandas as pd
df = pd.read_csv(r"D:\Retail_Sales\kaggle\query_sql\DoanhThu_Year.csv")

plt.plot(df["year"], df["tong"],marker = "o", color = "red")

plt.xticks(df["year"])
plt.show()